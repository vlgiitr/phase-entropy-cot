import copy
import json
import time

import torch
import torch.nn as nn
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer
import os
from transformers import PreTrainedModel, PretrainedConfig, AutoConfig

from .modeling_llama_kv import LlamaForCausalLM as KVLlamaForCausalLM
from .modeling_mixtral_kv import MixtralForCausalLM as KVMixtralForCausalLM
#from .modeling_qwen2_kv import LlamaForCausalLM as KVQwen2ForCausalLM
from .modeling_qwen2_kv import Qwen2ForCausalLM as KVQwen2ForCausalLM
from .modeling_qwen3_kv import Qwen3ForCausalLM as KVQwen3ForCausalLM
from .utils import *
from .kv_cache import initialize_past_key_values

from .cnets import Model
from .cnets1 import Model as Model1
from .configs import EConfig


class EaModel(nn.Module):

    def __init__(
            self,
            use_eagle3,
            base_model,
            base_model_name_or_path,
            ea_model_path,
            total_token,
            depth,
            top_k,
            threshold,
            ea_layer_state_dict,
    ):

        super().__init__()
        self.base_model = base_model
        self.config = base_model.config
        self.hidden_size = base_model.lm_head.weight.shape[-1]
        self.vocab_size = base_model.lm_head.weight.shape[0]
        self.base_model_name_or_path = base_model_name_or_path
        self.tokenizer = AutoTokenizer.from_pretrained(self.base_model_name_or_path, use_fast=False)
        self.use_eagle3 = use_eagle3
        config = EConfig.from_pretrained(ea_model_path)
        with open(ea_model_path, "r") as f:
            con = json.loads(f.read())
        try:
            bias = con["bias"]
        except:
            bias = True
        if use_eagle3:
            self.ea_layer = Model(config, bias=bias, total_tokens=total_token, depth=depth, top_k=top_k,
                                  threshold=threshold, path=base_model_name_or_path,load_emb=True)
        else:
            self.ea_layer = Model1(config, bias=bias, total_tokens=total_token, depth=depth, top_k=top_k,
                                  threshold=threshold, path=base_model_name_or_path,load_emb=True)

        low_memory = False

        device = base_model.model.layers[-1].self_attn.q_proj.weight.device
        if device != base_model.lm_head.weight.device:
            self.ea_layer.diff_device = True
            if not low_memory:
                self.ea_layer.headweight = base_model.lm_head.weight.clone().to(device)
            else:
                self.ea_layer.layer_device = device

        else:
            self.ea_layer.diff_device = False
        if self.use_eagle3 and config.vocab_size==config.draft_vocab_size:
            del self.ea_layer.d2t,self.ea_layer.t2d
        load_=self.ea_layer.load_state_dict(ea_layer_state_dict, strict=False)
        self.ea_layer.to(self.base_model.dtype).to(device)
        self.ea_layer.init_tree()
        self._inside_think = False
        self._think_start_token_id = self.tokenizer.convert_tokens_to_ids("<think>")
        self._think_end_token_id = self.tokenizer.convert_tokens_to_ids("</think>")

    def get_tokenizer(self):
        """Get the tokenizer of the base model.

        Returns:
            Tokenizer: The tokenizer of the base model.
        """
        return self.tokenizer

    @classmethod
    def from_pretrained(
            cls,
            use_eagle3=True,
            base_model_path=None,
            ea_model_path=None,
            total_token=60,
            depth=7,
            top_k=10,
            threshold=1.0,
            **kwargs,
    ):
        # assert Type=="LLaMA" or "Mixtral"
        Type = AutoConfig.from_pretrained(base_model_path).architectures[0]

        if Type == 'LlamaForCausalLM':
            base_model = KVLlamaForCausalLM.from_pretrained(
                base_model_path, **kwargs
            )
        elif Type == 'Qwen2ForCausalLM':
            base_model = KVQwen2ForCausalLM.from_pretrained(
                base_model_path, **kwargs
            )
        elif Type == 'Qwen3ForCausalLM':
            base_model = KVQwen3ForCausalLM.from_pretrained(
                base_model_path, **kwargs
            )
        else:
            base_model = KVMixtralForCausalLM.from_pretrained(
                base_model_path, **kwargs
            )

        configpath = os.path.join(ea_model_path, "config.json")
        if not os.path.exists(configpath):
            configpath = hf_hub_download(ea_model_path, "config.json")

        try:
            load_model_path = os.path.join(ea_model_path, "pytorch_model.bin")
            if not os.path.exists(load_model_path):
                load_model_path = hf_hub_download(ea_model_path, "pytorch_model.bin")
            ea_layer_state_dict = torch.load(load_model_path,
                                             map_location=base_model.device)
        except:
            from safetensors.torch import load_file
            load_model_path = os.path.join(ea_model_path, "model.safetensors")
            if not os.path.exists(load_model_path):
                load_model_path = hf_hub_download(ea_model_path, "model.safetensors")
            ea_layer_state_dict = load_file(load_model_path)
        model = cls(
            use_eagle3,
            base_model,
            base_model_path,
            configpath,
            total_token,
            depth,
            top_k,
            threshold,
            ea_layer_state_dict
        )

        if total_token == -1:
            device = model.base_model.model.layers[0].self_attn.q_proj.weight.device
            cans = [40, 48, 50, 56, 60]
            x = [1, 1.05, 1.07, 1.1, 1.13]
            times = []

            for i in range(len(cans)):
                length = cans[i]
                input_ids = torch.randint(0, model.config.vocab_size - 200, (1, length)).to(device)
                torch.cuda.synchronize()
                start_time = time.time()
                for _ in range(20):
                    torch.cuda.synchronize()
                    with torch.no_grad():
                        outputs = model.base_model(input_ids)
                    torch.cuda.synchronize()
                torch.cuda.synchronize()
                end_time = time.time()
                times.append((end_time - start_time) / x[i])
            total_token = cans[times.index(min(times))]
            model.ea_layer.total_tokens = total_token - 1

        return model

    def forward(
            self,
            input_ids=None,
            attention_mask=None,
            past_key_values=None,
            output_orig=False,
            position_ids=None,
    ):

        with torch.inference_mode():
            # Pass input through the base model
            outputs = self.base_model.model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                past_key_values=past_key_values,
                position_ids=position_ids,
            )
            if output_orig:
                orig = self.base_model.lm_head(outputs[0])
            hidden_states = outputs[0]

        if output_orig:
            return outputs, orig, hidden_states
        else:
            return outputs, hidden_states

    def _log_forensic_step(
            self,
            step,
            token,
            logits,
            best_candidate,
            accept_length,
            sample_p,
            hidden_state_new,
            retrieve_indices,
            candidates,
            position,
            logits_processor,
                draft_stats=None,
            log_metadata=None,
    ):
        try:
            token_id = int(token[0, 0].item())
            token_str = self.tokenizer.decode([token_id], clean_up_tokenization_spaces=False).strip()
            think_flag = (
                token_id == self._think_start_token_id
                or ("<think>" in token_str)
            )
            is_inside_think = self._inside_think or think_flag

            if token_id == self._think_start_token_id or "<think>" in token_str:
                self._inside_think = True
            if token_id == self._think_end_token_id or "</think>" in token_str:
                self._inside_think = False

            retrieve_hidden_state_new = hidden_state_new[:, retrieve_indices]
            retrieve_hidden_state_new = retrieve_hidden_state_new[0]
            accept_hidden_state_new = retrieve_hidden_state_new[best_candidate, : accept_length + 1]
            target_hidden = retrieve_hidden_state_new[best_candidate, accept_length].detach().cpu().tolist()
            draft_hidden = accept_hidden_state_new[-1].detach().cpu().tolist()

            tree_depth = int((retrieve_indices[best_candidate] >= 0).sum().item())
            if tree_depth == 0:
                tree_depth = int(accept_length)

            logits_row = logits[best_candidate, accept_length].float()
            target_probs = torch.softmax(torch.nan_to_num(logits_row, nan=-1e9, posinf=1e9, neginf=-1e9), dim=-1)
            target_probs = torch.nan_to_num(target_probs, nan=0.0, posinf=0.0, neginf=0.0)
            target_mass = target_probs.sum()
            if float(target_mass.item()) > 0.0:
                target_probs = target_probs / target_mass
            target_entropy = float(
                (-(target_probs * torch.log2(target_probs.clamp_min(torch.finfo(target_probs.dtype).tiny)))).sum().item()
            )

            if logits_processor is not None:
                proc_logits = logits_processor(None, logits_row[None, :])[0]
            else:
                proc_logits = logits_row
            top1_p = float(torch.softmax(proc_logits, dim=-1).max().item())

            topk = []
            k = min(32, logits_row.shape[-1])
            topk_values, topk_indices = torch.topk(logits_row, k)
            for top_id, top_val in zip(topk_indices.tolist(), topk_values.tolist()):
                topk.append({
                    "id": int(top_id),
                    "token": self.tokenizer.decode([top_id], clean_up_tokenization_spaces=False).strip(),
                    "logit": float(top_val),
                })

            draft_entropy = None
            draft_top1_prob = None
            draft_topk_probs = []

            if isinstance(draft_stats, dict):
                draft_entropy = float(draft_stats.get("draft_entropy")) if draft_stats.get("draft_entropy") is not None else None
                draft_top1_prob = float(draft_stats.get("draft_top1_prob")) if draft_stats.get("draft_top1_prob") is not None else None
                for item in draft_stats.get("draft_topk_probs", []) or []:
                    if not isinstance(item, dict) or item.get("id") is None:
                        continue
                    tid = int(item["id"])
                    draft_topk_probs.append({
                        "id": tid,
                        "token": self.tokenizer.decode([tid], clean_up_tokenization_spaces=False).strip(),
                        "prob": float(item.get("prob")) if item.get("prob") is not None else None,
                    })
            elif isinstance(sample_p, torch.Tensor):
                sample_p_tensor = sample_p.squeeze().float()
                if sample_p_tensor.ndim == 2 and sample_p_tensor.shape[0] == 1:
                    sample_p_tensor = sample_p_tensor[0]
                sample_p_tensor = torch.nan_to_num(sample_p_tensor, nan=0.0, posinf=0.0, neginf=0.0)
                if torch.is_floating_point(sample_p_tensor) and torch.all(sample_p_tensor >= 0) and abs(float(sample_p_tensor.sum().item()) - 1.0) < 1e-3:
                    draft_probs = sample_p_tensor
                else:
                    draft_probs = torch.softmax(sample_p_tensor, dim=-1)
                draft_probs = torch.nan_to_num(draft_probs.float(), nan=0.0, posinf=0.0, neginf=0.0)
                draft_mass = draft_probs.sum()
                if float(draft_mass.item()) > 0.0:
                    draft_probs = draft_probs / draft_mass
                draft_top1_prob = float(draft_probs.max().item())
                draft_entropy = float(
                    (-(draft_probs * torch.log2(draft_probs.clamp_min(torch.finfo(draft_probs.dtype).tiny)))).sum().item()
                )
                d_k = min(32, draft_probs.shape[-1])
                d_values, d_indices = torch.topk(draft_probs, d_k)
                for top_id, top_prob in zip(d_indices.tolist(), d_values.tolist()):
                    draft_topk_probs.append({
                        "id": int(top_id),
                        "token": self.tokenizer.decode([top_id], clean_up_tokenization_spaces=False).strip(),
                        "prob": float(top_prob),
                    })

            metadata = {
                "run_id": None,
                "problem_id": None,
                "model_name": None,
                "drafter_name": None,
                "temperature": None,
            }
            if isinstance(log_metadata, dict):
                metadata.update(log_metadata)

            forensic = {
                "step": int(step),
                "position": int(position),
                "tree_depth_at_accept": int(tree_depth),
                "accepted": bool(accept_length > 0),
                "accept_length": int(accept_length),
                "token_id": token_id,
                "token_str": token_str,
                "target_entropy": target_entropy,
                "draft_entropy": draft_entropy,
                "draft_top1_prob": draft_top1_prob,
                "draft_topk_probs": draft_topk_probs,
                "run_id": metadata.get("run_id"),
                "problem_id": metadata.get("problem_id"),
                "model_name": metadata.get("model_name") or self.base_model_name_or_path,
                "drafter_name": metadata.get("drafter_name"),
                "temperature": float(metadata.get("temperature")) if metadata.get("temperature") is not None else float(0.0),
                "is_inside_think": bool(is_inside_think),
                "phase_label_hmm": None,
                "tree_depth": int(tree_depth),
            }
            print(json.dumps(forensic))
        except Exception as exc:
            warning = {
                "step": int(step),
                "position": int(position),
                "accepted": bool(accept_length > 0),
                "accept_length": int(accept_length),
                "best_candidate": int(best_candidate) if isinstance(best_candidate, torch.Tensor) else int(best_candidate),
                "error": str(exc),
                "retrieve_indices_shape": list(retrieve_indices.shape) if hasattr(retrieve_indices, 'shape') else None,
                "candidates_shape": list(candidates.shape) if hasattr(candidates, 'shape') else None,
                "hidden_state_new_shape": list(hidden_state_new.shape) if hasattr(hidden_state_new, 'shape') else None,
                "logits_shape": list(logits.shape) if hasattr(logits, 'shape') else None,
            }
            print(json.dumps(warning))

    @torch.no_grad()
    def eagenerate(
            self,
            input_ids,
            temperature=0.0,
            top_p=0.0,
            top_k=0.0,
            max_new_tokens=512,
            max_length=2048,
            log=False,
            is_llama3=False,
            log_metadata=None,

    ):
        if is_llama3:
            stop_token_id = self.tokenizer.convert_tokens_to_ids("<|eot_id|>")


        if temperature > 1e-5:
            logits_processor = prepare_logits_processor(temperature=temperature, top_p=top_p, top_k=top_k)
        else:
            logits_processor = None
        # assert input_ids.shape[0] == 1, "Only support batch size 1 for now!!"
        # Avoid modifying the input_ids in-place

        padding = (torch.zeros(1, 1, dtype=torch.long) - 1).to(input_ids.device)
        input_ids = input_ids.clone()
        self.ea_layer.reset_kv()

        # Initialize the past key and value states
        if hasattr(self, "past_key_values"):
            past_key_values = self.past_key_values
            past_key_values_data = self.past_key_values_data
            current_length_data = self.current_length_data
            # Reset the past key and value states
            current_length_data.zero_()
        else:
            (
                past_key_values,
                past_key_values_data,
                current_length_data,
            ) = initialize_past_key_values(self.base_model,max_length=max_length)
            self.past_key_values = past_key_values
            self.past_key_values_data = past_key_values_data
            self.current_length_data = current_length_data

        input_len = input_ids.shape[1]
        reset_tree_mode(self)
        # prefill
        draft_tokens, retrieve_indices, tree_mask, tree_position_ids, logits, hidden_state, sample_token, draft_stats = initialize_tree(
            input_ids, self, past_key_values, logits_processor
        )
        new_token = 0
        max_length = max_length - self.ea_layer.total_tokens - 10
        for idx in range(max_length):
            # with Timer("all"):
            self.base_model.model.tree_mask = tree_mask

            draft_tokens = draft_tokens.to(input_ids.device)
            # Target model forward, get logits
            logits, hidden_state_new, outputs = tree_decoding(
                self,
                draft_tokens,
                past_key_values,
                tree_position_ids,
                input_ids,
                retrieve_indices,
            )
            # retrieve_indices=tree_buffers["retrieve_indices"]
            # logits = logits[0, retrieve_indices]
            draft_tokens = torch.cat((draft_tokens, padding), dim=1)
            candidates = draft_tokens[0, retrieve_indices]
            # verification
            best_candidate, accept_length, sample_p = evaluate_posterior(
                logits, candidates, logits_processor
            )
            log_retrieve_indices = retrieve_indices
            # print(accept_length)
            prev_input_len = input_ids.shape[1]
            # Adjusting the input sequence, draft model forward
            current_draft_stats = draft_stats
            input_ids, draft_tokens, retrieve_indices, tree_mask, tree_position_ids, new_token, hidden_state, sample_token, draft_stats = update_inference_inputs(
                input_ids,
                candidates,
                best_candidate,
                accept_length,
                retrieve_indices,
                logits_processor,
                new_token,
                past_key_values_data,
                current_length_data,
                self,
                hidden_state_new,
                sample_p
            )
            if log:
                self._log_forensic_step(
                    idx,
                    sample_token,
                    logits,
                    best_candidate,
                    accept_length,
                    sample_p,
                    hidden_state_new,
                    log_retrieve_indices,
                    candidates,
                    prev_input_len,
                    logits_processor,
                    draft_stats=current_draft_stats,
                    log_metadata=log_metadata,
                )

            if is_llama3:
                if stop_token_id in input_ids[0, input_len:].tolist():
                    break

            if self.tokenizer.eos_token_id in input_ids[0, input_len:].tolist():
                break
            if new_token > max_new_tokens:
                break
            if input_ids.shape[1] > max_length:
                break
        if not log:
            return input_ids
        else:
            return input_ids, new_token, idx

    @torch.no_grad()
    def naivegenerate(
            self,
            input_ids,
            temperature=0.0,
            top_p=0.0,
            top_k=0.0,
            max_new_tokens=512,
            max_length=2048,
            log=False,
            is_llama3=False,

    ):
        if is_llama3:
            stop_token_id = self.tokenizer.convert_tokens_to_ids("<|eot_id|>")


        if temperature > 1e-5:
            logits_processor = prepare_logits_processor(temperature=temperature, top_p=top_p, top_k=top_k)
        else:
            logits_processor = None
        # assert input_ids.shape[0] == 1, "Only support batch size 1 for now!!"
        # Avoid modifying the input_ids in-place

        padding = (torch.zeros(1, 1, dtype=torch.long) - 1).to(input_ids.device)
        input_ids = input_ids.clone()
        self.ea_layer.reset_kv()

        # Initialize the past key and value states
        if hasattr(self, "past_key_values"):
            past_key_values = self.past_key_values
            past_key_values_data = self.past_key_values_data
            current_length_data = self.current_length_data
            # Reset the past key and value states
            current_length_data.zero_()
        else:
            (
                past_key_values,
                past_key_values_data,
                current_length_data,
            ) = initialize_past_key_values(self.base_model,max_length=max_length)
            self.past_key_values = past_key_values
            self.past_key_values_data = past_key_values_data
            self.current_length_data = current_length_data

        input_len = input_ids.shape[1]
        reset_tree_mode(self)
        outputs = self.base_model(input_ids, past_key_values=past_key_values, use_cache=True)
        new_token = 0
        max_length = max_length - self.ea_layer.total_tokens - 10
        for idx in range(max_length):
            if logits_processor is not None:
                logits = outputs.logits[:, -1]
                logits = logits_processor(None, logits)
                probabilities = torch.nn.functional.softmax(logits, dim=-1)
                input_id = torch.multinomial(probabilities, 1)
            else:
                input_id = outputs.logits[:, -1:].argmax(dim=-1)
            outputs = self.base_model(input_id, use_cache=True, past_key_values=past_key_values)
            input_ids = torch.cat([input_ids, input_id], dim=-1)
            new_token += 1

            if is_llama3:
                if stop_token_id in input_ids[0, input_len:].tolist():
                    break

            if self.tokenizer.eos_token_id in input_ids[0, input_len:].tolist():
                break
            if new_token > max_new_tokens:
                break
            if input_ids.shape[1] > max_length:
                break
        if not log:
            return input_ids
        else:
            return input_ids, new_token, idx

    @torch.no_grad()
    def ea_generate(
            self,
            input_ids,
            temperature=0.0,
            top_p=0.0,
            top_k=0.0,
            max_new_tokens=512,
            max_length=2048,
            log=False,
            is_llama3=False,

    ):
        if is_llama3:
            stop_token_id = self.tokenizer.convert_tokens_to_ids("<|eot_id|>")


        if temperature > 1e-5:
            logits_processor = prepare_logits_processor(temperature=temperature, top_p=top_p, top_k=top_k)
        else:
            logits_processor = None
        # assert input_ids.shape[0] == 1, "Only support batch size 1 for now!!"
        # Avoid modifying the input_ids in-place

        padding = (torch.zeros(1, 1, dtype=torch.long) - 1).to(input_ids.device)
        input_ids = input_ids.clone()
        self.ea_layer.reset_kv()

        # Initialize the past key and value states
        if hasattr(self, "past_key_values"):
            past_key_values = self.past_key_values
            past_key_values_data = self.past_key_values_data
            current_length_data = self.current_length_data
            # Reset the past key and value states
            current_length_data.zero_()
        else:
            (
                past_key_values,
                past_key_values_data,
                current_length_data,
            ) = initialize_past_key_values(self.base_model,max_length=max_length)
            self.past_key_values = past_key_values
            self.past_key_values_data = past_key_values_data
            self.current_length_data = current_length_data

        input_len = input_ids.shape[1]
        reset_tree_mode(self)
        draft_tokens, retrieve_indices, tree_mask, tree_position_ids, logits, hidden_state, sample_token, draft_stats = initialize_tree(
            input_ids, self, past_key_values, logits_processor
        )
        new_token = 0
        max_length = max_length - self.ea_layer.total_tokens - 10
        for idx in range(max_length):
            # with Timer("all"):
            self.base_model.model.tree_mask = tree_mask

            draft_tokens = draft_tokens.to(input_ids.device)
            # with Timer("tree_decoding"):
            logits, hidden_state_new, outputs = tree_decoding(
                self,
                draft_tokens,
                past_key_values,
                tree_position_ids,
                input_ids,
                retrieve_indices,
            )
            # retrieve_indices=tree_buffers["retrieve_indices"]
            # logits = logits[0, retrieve_indices]
            draft_tokens = torch.cat((draft_tokens, padding), dim=1)
            candidates = draft_tokens[0, retrieve_indices]
            best_candidate, accept_length, sample_p = evaluate_posterior(
                logits, candidates, logits_processor
            )
            # print(accept_length)
            prev_input_len = input_ids.shape[1]
            # with Timer("update_inference_inputs"):
            current_draft_stats = draft_stats
            input_ids, draft_tokens, retrieve_indices, tree_mask, tree_position_ids, new_token, hidden_state, sample_token, draft_stats = update_inference_inputs(
                input_ids,
                candidates,
                best_candidate,
                accept_length,
                retrieve_indices,
                logits_processor,
                new_token,
                past_key_values_data,
                current_length_data,
                self,
                hidden_state_new,
                sample_p
            )
            if log:
                self._log_forensic_step(
                    idx,
                    sample_token,
                    logits,
                    best_candidate,
                    accept_length,
                    sample_p,
                    hidden_state_new,
                    retrieve_indices,
                    candidates,
                    prev_input_len,
                    logits_processor,
                    draft_stats=current_draft_stats,
                )

            yield input_ids

            if is_llama3:
                if stop_token_id in input_ids[0, input_len:].tolist():
                    break

            if self.tokenizer.eos_token_id in input_ids[0, input_len:].tolist():
                break
            if new_token > max_new_tokens:
                break
            if input_ids.shape[1] > max_length:
                break

    @torch.no_grad()
    def naive_generate(
            self,
            input_ids,
            temperature=0.0,
            top_p=0.0,
            top_k=0.0,
            max_new_tokens=512,
            max_length=2048,
            log=False,
            is_llama3=False,

    ):
        if is_llama3:
            stop_token_id = self.tokenizer.convert_tokens_to_ids("<|eot_id|>")


        if temperature > 1e-5:
            logits_processor = prepare_logits_processor(temperature=temperature, top_p=top_p, top_k=top_k)
        else:
            logits_processor = None
        # assert input_ids.shape[0] == 1, "Only support batch size 1 for now!!"
        # Avoid modifying the input_ids in-place

        padding = (torch.zeros(1, 1, dtype=torch.long) - 1).to(input_ids.device)
        input_ids = input_ids.clone()
        self.ea_layer.reset_kv()

        # Initialize the past key and value states
        if hasattr(self, "past_key_values"):
            past_key_values = self.past_key_values
            past_key_values_data = self.past_key_values_data
            current_length_data = self.current_length_data
            # Reset the past key and value states
            current_length_data.zero_()
        else:
            (
                past_key_values,
                past_key_values_data,
                current_length_data,
            ) = initialize_past_key_values(self.base_model,max_length=max_length)
            self.past_key_values = past_key_values
            self.past_key_values_data = past_key_values_data
            self.current_length_data = current_length_data

        input_len = input_ids.shape[1]
        reset_tree_mode(self)
        outputs = self.base_model(input_ids, past_key_values=past_key_values, use_cache=True)
        new_token = 0
        max_length = max_length - self.ea_layer.total_tokens - 10
        for idx in range(max_length):
            if logits_processor is not None:
                logits = outputs.logits[:, -1]
                logits = logits_processor(None, logits)
                probabilities = torch.nn.functional.softmax(logits, dim=-1)
                input_id = torch.multinomial(probabilities, 1)
            else:
                input_id = outputs.logits[:, -1:].argmax(dim=-1)

            outputs = self.base_model(input_id, use_cache=True, past_key_values=past_key_values)
            input_ids = torch.cat([input_ids, input_id], dim=-1)
            new_token += 1

            yield input_ids

            if is_llama3:
                if stop_token_id in input_ids[0, input_len:].tolist():
                    break

            if self.tokenizer.eos_token_id in input_ids[0, input_len:].tolist():
                break
            if new_token > max_new_tokens:
                break
            if input_ids.shape[1] > max_length:
                break