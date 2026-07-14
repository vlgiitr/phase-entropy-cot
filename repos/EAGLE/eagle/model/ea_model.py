import copy
import json
import os
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer
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


class RuntimeLevelController:
    def __init__(self, policy_path: str | None = None):
        self.policy_path = policy_path or self._default_policy_path()
        self.params = None
        self.config = None
        self._entropy_ewma = None
        self._top1_ewma = None
        self._load_policy()

    @staticmethod
    def _default_policy_path() -> str:
        return str(Path(__file__).resolve().parents[2] / "results" / "controller_real_corpus_eval_v3_frozen.json")

    def _load_policy(self) -> None:
        policy_path = Path(self.policy_path)
        if not policy_path.exists():
            return
        try:
            payload = json.loads(policy_path.read_text(encoding="utf-8"))
        except Exception:
            return
        controller = payload.get("controller", {})
        self.params = controller.get("params", {})
        self.config = controller.get("config", {})
        if self.params:
            self._entropy_ewma = float(self.params.get("entropy_mean", 0.0))
            self._top1_ewma = 0.5

    def reset(self) -> None:
        self._entropy_ewma = None
        self._top1_ewma = None
        if self.params:
            self._entropy_ewma = float(self.params.get("entropy_mean", 0.0))
            self._top1_ewma = 0.5

    def select_length(self, draft_entropy=None, draft_top1_prob=None, fallback_length: int = 4) -> int:
        if not self.params:
            return int(max(1, fallback_length))
        if self._entropy_ewma is None:
            self.reset()

        alpha_entropy = float(self.config.get("alpha_entropy", 0.2)) if self.config else 0.2
        alpha_top1 = float(self.config.get("alpha_top1", 0.2)) if self.config else 0.2

        current_entropy = float(self._entropy_ewma)
        current_top1 = float(self._top1_ewma)
        if draft_entropy is not None and np.isfinite(float(draft_entropy)):
            current_entropy = float(draft_entropy)
            self._entropy_ewma = alpha_entropy * float(draft_entropy) + (1.0 - alpha_entropy) * self._entropy_ewma
        if draft_top1_prob is not None and np.isfinite(float(draft_top1_prob)):
            current_top1 = float(draft_top1_prob)
            self._top1_ewma = alpha_top1 * float(draft_top1_prob) + (1.0 - alpha_top1) * self._top1_ewma

        entropy_mean = float(self.params.get("entropy_mean", 0.0))
        entropy_std = float(self.params.get("entropy_std", 1.0))
        if entropy_std < 1e-6:
            entropy_std = 1.0
        risk = current_entropy - entropy_mean
        risk = risk / entropy_std
        uncertainty = 1.0 - current_top1
        score = uncertainty + 0.1 * risk

        edges = [float(x) for x in self.params.get("risk_bin_edges", [])]
        lengths = [int(x) for x in self.params.get("bin_lengths", [])]
        if not edges or not lengths:
            return int(max(1, fallback_length))
        if score <= 0.40:
            return int(max(1, lengths[0]))
        if score <= 0.85:
            return int(max(1, lengths[1]))
        return int(max(1, lengths[-1]))


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
        self._default_total_tokens = int(getattr(self.ea_layer, "total_tokens", 1))
        self.runtime_controller = RuntimeLevelController()

    def get_tokenizer(self):
        """Get the tokenizer of the base model.

        Returns:
            Tokenizer: The tokenizer of the base model.
        """
        return self.tokenizer

    def _set_runtime_draft_length(self, draft_length: int) -> None:
        draft_length = max(1, int(draft_length))
        self.ea_layer.total_tokens = max(1, draft_length - 1)

    def _get_runtime_draft_length(
            self,
            mode: str,
            draft_length: int | None = None,
            draft_entropy: float | None = None,
            draft_top1_prob: float | None = None,
            fallback_length: int = 4,
    ) -> int:
        mode = (mode or "speculative").lower()
        if mode == "ar" or mode == "autoregressive":
            return 1
        if mode == "fixed":
            return int(max(1, draft_length or fallback_length))
        if mode == "controller":
            return self.runtime_controller.select_length(
                draft_entropy=draft_entropy,
                draft_top1_prob=draft_top1_prob,
                fallback_length=fallback_length,
            )
        return int(max(1, draft_length or fallback_length))

    def _restore_runtime_draft_length(self) -> None:
        self.ea_layer.total_tokens = max(1, int(self._default_total_tokens))

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
            draft_stats,
            hidden_state_new,
            retrieve_indices,
            candidates,
            position,
            logits_processor,
            log_metadata=None,
            mode: str = "speculative",
            draft_length: int | None = None,
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
            if best_candidate < retrieve_hidden_state_new.shape[0]:
                accept_hidden_state_new = retrieve_hidden_state_new[best_candidate, : accept_length + 1]
                target_hidden = retrieve_hidden_state_new[best_candidate, accept_length].detach().cpu().tolist()
                draft_hidden = accept_hidden_state_new[-1].detach().cpu().tolist()
            else:
                accept_hidden_state_new = retrieve_hidden_state_new[0, : accept_length + 1]
                target_hidden = retrieve_hidden_state_new[0, accept_length].detach().cpu().tolist()
                draft_hidden = accept_hidden_state_new[-1].detach().cpu().tolist()

            tree_depth = int((retrieve_indices[best_candidate] >= 0).sum().item()) if best_candidate < retrieve_indices.shape[0] else int(accept_length)
            if tree_depth == 0:
                tree_depth = int(accept_length)

            if best_candidate < logits.shape[0] and accept_length < logits.shape[1]:
                logits_row = logits[best_candidate, accept_length]
            else:
                logits_row = logits[0, 0]
            target_probs = torch.softmax(logits_row, dim=-1)
            target_entropy = float((-(target_probs * torch.log2(target_probs.clamp(min=1e-12))).sum()).item())

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

            if isinstance(sample_p, torch.Tensor):
                sample_p_tensor = sample_p.squeeze()
                if sample_p_tensor.ndim == 2 and sample_p_tensor.shape[0] == 1:
                    sample_p_tensor = sample_p_tensor[0]
                if torch.is_floating_point(sample_p_tensor) and torch.all(sample_p_tensor >= 0) and abs(float(sample_p_tensor.sum().item()) - 1.0) < 1e-3:
                    draft_probs = sample_p_tensor
                else:
                    draft_probs = torch.softmax(sample_p_tensor, dim=-1)
            else:
                draft_probs = None

            draft_top1_prob = float(draft_probs.max().item()) if draft_probs is not None else None
            draft_entropy = float((-(draft_probs * torch.log2(draft_probs.clamp(min=1e-12))).sum()).item()) if draft_probs is not None else None

            draft_topk_probs = []
            if draft_probs is not None:
                d_k = min(32, draft_probs.shape[-1])
                d_values, d_indices = torch.topk(draft_probs, d_k)
                for top_id, top_prob in zip(d_indices.tolist(), d_values.tolist()):
                    draft_topk_probs.append({
                        "id": int(top_id),
                        "token": self.tokenizer.decode([top_id], clean_up_tokenization_spaces=False).strip(),
                        "prob": float(top_prob),
                    })

            # Prefer drafter stats emitted from the draft tree expansion when available.
            # This keeps legacy fields unchanged while enabling additive p/q backfill.
            if isinstance(draft_stats, dict):
                if draft_stats.get("draft_entropy") is not None:
                    draft_entropy = float(draft_stats.get("draft_entropy"))
                if draft_stats.get("draft_top1_prob") is not None:
                    draft_top1_prob = float(draft_stats.get("draft_top1_prob"))
                if draft_stats.get("draft_topk_probs") is not None:
                    draft_topk_probs = draft_stats.get("draft_topk_probs")

            target_token_prob = float(target_probs[token_id].item()) if token_id < target_probs.shape[-1] else None
            draft_token_prob = None
            if draft_probs is not None and token_id < draft_probs.shape[-1]:
                draft_token_prob = float(draft_probs[token_id].item())
            if isinstance(draft_stats, dict):
                topk_probs = draft_stats.get("draft_topk_probs")
                if isinstance(topk_probs, list):
                    for item in topk_probs:
                        if int(item.get("id", -1)) == token_id:
                            draft_token_prob = float(item.get("prob"))
                            break

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
                "p": target_token_prob,
                "q": draft_token_prob,
                "target_token_prob": target_token_prob,
                "draft_token_prob": draft_token_prob,
                "run_id": metadata.get("run_id"),
                "problem_id": metadata.get("problem_id"),
                "model_name": metadata.get("model_name") or self.base_model_name_or_path,
                "drafter_name": metadata.get("drafter_name"),
                "temperature": float(metadata.get("temperature")) if metadata.get("temperature") is not None else float(0.0),
                "is_inside_think": bool(is_inside_think),
                "phase_label_hmm": None,
                "tree_depth": int(tree_depth),
                "run_mode": mode,
                "draft_length": int(draft_length) if draft_length is not None else None,
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
            mode: str = "speculative",
            fixed_draft_length: int = 4,
            controller_policy_path: str | None = None,

    ):
        if mode in {"ar", "autoregressive"}:
            return self.naivegenerate(
                input_ids=input_ids,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                max_new_tokens=max_new_tokens,
                max_length=max_length,
                log=log,
                is_llama3=is_llama3,
                mode=mode,
                fixed_draft_length=fixed_draft_length,
                controller_policy_path=controller_policy_path,
            )

        if controller_policy_path is not None:
            self.runtime_controller = RuntimeLevelController(policy_path=controller_policy_path)
        elif not hasattr(self, "runtime_controller") or self.runtime_controller is None:
            self.runtime_controller = RuntimeLevelController()

        if is_llama3:
            stop_token_id = self.tokenizer.convert_tokens_to_ids("<|eot_id|>")

        if temperature > 1e-5:
            logits_processor = prepare_logits_processor(temperature=temperature, top_p=top_p, top_k=top_k)
        else:
            logits_processor = None

        padding = (torch.zeros(1, 1, dtype=torch.long) - 1).to(input_ids.device)
        input_ids = input_ids.clone()
        self.ea_layer.reset_kv()

        if hasattr(self, "past_key_values"):
            past_key_values = self.past_key_values
            past_key_values_data = self.past_key_values_data
            current_length_data = self.current_length_data
            current_length_data.zero_()
        else:
            # Allocate KV cache with a safe margin: allow room for the prompt,
            # the planned new tokens, and the EA draft tokens to avoid overflow
            # during tree decoding. This prevents writes that exceed the
            # preallocated dimension (seen as: start + length > dimension).
            alloc_max = int(max_length + max_new_tokens + getattr(self.ea_layer, 'total_tokens', 0) + 16)
            (
                past_key_values,
                past_key_values_data,
                current_length_data,
            ) = initialize_past_key_values(self.base_model, max_length=alloc_max)
            self.past_key_values = past_key_values
            self.past_key_values_data = past_key_values_data
            self.current_length_data = current_length_data

        input_len = input_ids.shape[1]
        reset_tree_mode(self)
        self.runtime_controller.reset()
        current_draft_length = self._get_runtime_draft_length(
            mode=mode,
            draft_length=fixed_draft_length,
            fallback_length=fixed_draft_length,
        )
        self._set_runtime_draft_length(current_draft_length)
        draft_tokens, retrieve_indices, tree_mask, tree_position_ids, logits, hidden_state, sample_token, draft_stats = initialize_tree(
            input_ids, self, past_key_values, logits_processor
        )
        new_token = 0
        max_length = max_length - self.ea_layer.total_tokens - 10
        for idx in range(max_length):
            self.base_model.model.tree_mask = tree_mask
            draft_tokens = draft_tokens.to(input_ids.device)
            logits, hidden_state_new, outputs = tree_decoding(
                self,
                draft_tokens,
                past_key_values,
                tree_position_ids,
                input_ids,
                retrieve_indices,
            )
            draft_tokens = torch.cat((draft_tokens, padding), dim=1)
            candidates = draft_tokens[0, retrieve_indices]
            best_candidate, accept_length, sample_p = evaluate_posterior(
                logits, candidates, logits_processor
            )
            prev_input_len = input_ids.shape[1]
            position_from_prompt_end = max(0, prev_input_len - input_len)
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
                sample_p,
            )
            current_draft_length = self._get_runtime_draft_length(
                mode=mode,
                draft_length=fixed_draft_length,
                draft_entropy=draft_stats.get("draft_entropy") if isinstance(draft_stats, dict) else None,
                draft_top1_prob=draft_stats.get("draft_top1_prob") if isinstance(draft_stats, dict) else None,
                fallback_length=fixed_draft_length,
            )
            self._set_runtime_draft_length(current_draft_length)
            if log:
                self._log_forensic_step(
                    idx,
                    sample_token,
                    logits,
                    best_candidate,
                    accept_length,
                    sample_p,
                    draft_stats,
                    hidden_state_new,
                    retrieve_indices,
                    candidates,
                    position_from_prompt_end,
                    logits_processor,
                    log_metadata=log_metadata,
                    mode=mode,
                    draft_length=current_draft_length,
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

        self._restore_runtime_draft_length()
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
            mode: str = "ar",
            fixed_draft_length: int = 4,
            controller_policy_path: str | None = None,

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
            alloc_max = int(max_length + max_new_tokens + getattr(self.ea_layer, 'total_tokens', 0) + 16)
            (
                past_key_values,
                past_key_values_data,
                current_length_data,
            ) = initialize_past_key_values(self.base_model, max_length=alloc_max)
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
            mode: str = "speculative",
            fixed_draft_length: int = 4,
            controller_policy_path: str | None = None,

    ):
        if mode in {"ar", "autoregressive"}:
            return self.naive_generate(
                input_ids=input_ids,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                max_new_tokens=max_new_tokens,
                max_length=max_length,
                log=log,
                is_llama3=is_llama3,
                mode=mode,
                fixed_draft_length=fixed_draft_length,
                controller_policy_path=controller_policy_path,
            )

        if controller_policy_path is not None:
            self.runtime_controller = RuntimeLevelController(policy_path=controller_policy_path)
        elif not hasattr(self, "runtime_controller") or self.runtime_controller is None:
            self.runtime_controller = RuntimeLevelController()

        if is_llama3:
            stop_token_id = self.tokenizer.convert_tokens_to_ids("<|eot_id|>")

        if temperature > 1e-5:
            logits_processor = prepare_logits_processor(temperature=temperature, top_p=top_p, top_k=top_k)
        else:
            logits_processor = None

        padding = (torch.zeros(1, 1, dtype=torch.long) - 1).to(input_ids.device)
        input_ids = input_ids.clone()
        self.ea_layer.reset_kv()

        if hasattr(self, "past_key_values"):
            past_key_values = self.past_key_values
            past_key_values_data = self.past_key_values_data
            current_length_data = self.current_length_data
            current_length_data.zero_()
        else:
            alloc_max = int(max_length + max_new_tokens + getattr(self.ea_layer, 'total_tokens', 0) + 16)
            (
                past_key_values,
                past_key_values_data,
                current_length_data,
            ) = initialize_past_key_values(self.base_model, max_length=alloc_max)
            self.past_key_values = past_key_values
            self.past_key_values_data = past_key_values_data
            self.current_length_data = current_length_data

        input_len = input_ids.shape[1]
        reset_tree_mode(self)
        self.runtime_controller.reset()
        current_draft_length = self._get_runtime_draft_length(
            mode=mode,
            draft_length=fixed_draft_length,
            fallback_length=fixed_draft_length,
        )
        self._set_runtime_draft_length(current_draft_length)
        draft_tokens, retrieve_indices, tree_mask, tree_position_ids, logits, hidden_state, sample_token, draft_stats = initialize_tree(
            input_ids, self, past_key_values, logits_processor
        )
        new_token = 0
        max_length = max_length - self.ea_layer.total_tokens - 10
        for idx in range(max_length):
            self.base_model.model.tree_mask = tree_mask
            draft_tokens = draft_tokens.to(input_ids.device)
            logits, hidden_state_new, outputs = tree_decoding(
                self,
                draft_tokens,
                past_key_values,
                tree_position_ids,
                input_ids,
                retrieve_indices,
            )
            draft_tokens = torch.cat((draft_tokens, padding), dim=1)
            candidates = draft_tokens[0, retrieve_indices]
            best_candidate, accept_length, sample_p = evaluate_posterior(
                logits, candidates, logits_processor
            )
            prev_input_len = input_ids.shape[1]
            position_from_prompt_end = max(0, prev_input_len - input_len)
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
                sample_p,
            )
            current_draft_length = self._get_runtime_draft_length(
                mode=mode,
                draft_length=fixed_draft_length,
                draft_entropy=draft_stats.get("draft_entropy") if isinstance(draft_stats, dict) else None,
                draft_top1_prob=draft_stats.get("draft_top1_prob") if isinstance(draft_stats, dict) else None,
                fallback_length=fixed_draft_length,
            )
            self._set_runtime_draft_length(current_draft_length)
            if log:
                self._log_forensic_step(
                    idx,
                    sample_token,
                    logits,
                    best_candidate,
                    accept_length,
                    sample_p,
                    draft_stats,
                    hidden_state_new,
                    retrieve_indices,
                    candidates,
                    position_from_prompt_end,
                    logits_processor,
                    mode=mode,
                    draft_length=current_draft_length,
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

        self._restore_runtime_draft_length()

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
            mode: str = "ar",
            fixed_draft_length: int = 4,
            controller_policy_path: str | None = None,

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
            alloc_max = int(max_length + max_new_tokens + getattr(self.ea_layer, 'total_tokens', 0) + 16)
            (
                past_key_values,
                past_key_values_data,
                current_length_data,
            ) = initialize_past_key_values(self.base_model, max_length=alloc_max)
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