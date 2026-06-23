import os
import sys
import json
import random
import torch
from io import StringIO

# minimal path so we can reuse tokenizer
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from transformers import AutoTokenizer

TK_PATH = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'llama8b'))
print('Loading tokenizer from', TK_PATH)
try:
    tokenizer = AutoTokenizer.from_pretrained(TK_PATH, use_fast=False)
except Exception as e:
    print('Failed to load tokenizer:', e)
    tokenizer = None

# replicate forensic logger logic

def log_forensic_step(tokenizer, step, token, logits, best_candidate, accept_length, sample_p, hidden_state_new, retrieve_indices, candidates, position, logits_processor):
    token_id = int(token[0, 0].item())
    token_str = tokenizer.decode([token_id], clean_up_tokenization_spaces=False).strip() if tokenizer is not None else str(token_id)
    think_flag = "<think>" in token_str

    retrieve_hidden_state_new = hidden_state_new[:, retrieve_indices]
    retrieve_hidden_state_new = retrieve_hidden_state_new[0]
    accept_hidden_state_new = retrieve_hidden_state_new[best_candidate, : accept_length + 1]
    target_hidden = retrieve_hidden_state_new[best_candidate, accept_length].detach().cpu().tolist()
    draft_hidden = accept_hidden_state_new[-1].detach().cpu().tolist()

    tree_depth = int((retrieve_indices[best_candidate] >= 0).sum().item())
    if tree_depth == 0:
        tree_depth = int(accept_length)

    logits_row = logits[best_candidate, accept_length]
    if logits_processor is not None:
        proc_logits = logits_processor(None, logits_row[None, :])[0]
    else:
        proc_logits = logits_row
    probs = torch.nn.functional.softmax(proc_logits, dim=-1)
    top1_p = float(probs.max().item())

    topk = []
    k = min(32, logits_row.shape[-1])
    topk_values, topk_indices = torch.topk(logits_row, k)
    for top_id, top_val in zip(topk_indices.tolist(), topk_values.tolist()):
        topk.append({
            "id": int(top_id),
            "token": tokenizer.decode([top_id], clean_up_tokenization_spaces=False).strip() if tokenizer is not None else str(top_id),
            "logit": float(top_val),
        })

    forensic = {
        "step": int(step),
        "position": int(position),
        "tree_depth": int(tree_depth),
        "accepted": bool(accept_length > 0),
        "accept_length": int(accept_length),
        "accepted_sequence": [int(x.item()) for x in candidates[best_candidate, : accept_length + 1]],
        "token_id": token_id,
        "token": token_str,
        "think_flag": think_flag,
        "top1_p": top1_p,
        "topk": topk,
        "target_hidden_len": len(target_hidden),
        "draft_hidden_len": len(draft_hidden),
        "sample_p_top1": float(sample_p.max().item()) if isinstance(sample_p, torch.Tensor) else None,
    }
    print(json.dumps(forensic))


# prepare 5 prompts
sample_texts = [
    "Compute 13 + 29.",
    "What is the derivative of x^2 at x=3?",
    "Solve for x: 2x + 5 = 17.",
    "Integrate 1/x from 1 to e.",
    "Compute 7 * 8 - 15.",
]

OUT_DIR = os.path.join(ROOT, 'sanity_unit_traces')
os.makedirs(OUT_DIR, exist_ok=True)

for i, text in enumerate(sample_texts):
    # tokenize
    if tokenizer is not None:
        toks = tokenizer(text, return_tensors='pt', add_special_tokens=True).input_ids
    else:
        toks = torch.tensor([[1,2,3]])

    # synthetic tensors
    num_candidates = 4
    seq_len = 8
    vocab_size = tokenizer.vocab_size if tokenizer is not None else 20000

    logits = torch.randn(num_candidates, seq_len, vocab_size)
    # ensure some large value at a known token
    logits[0, 0, min(10, vocab_size-1)] = 10.0

    hidden_state_new = torch.randn(1, 200, 128)

    # create retrieve_indices: shape [num_candidates, max_depth]
    max_depth = 5
    retrieve_indices = torch.zeros((num_candidates, max_depth), dtype=torch.long) - 1
    for c in range(num_candidates):
        for d in range(max_depth):
            retrieve_indices[c, d] = random.randint(0, hidden_state_new.shape[1]-1)

    candidates = torch.randint(0, vocab_size, (num_candidates, seq_len), dtype=torch.long)

    # pick token as last token in toks
    token = toks[:, -1:]

    sample_p = torch.softmax(torch.randn(vocab_size), dim=0)

    # capture output
    from io import StringIO
    buf = StringIO()
    old = sys.stdout
    sys.stdout = buf
    # call logger for a few steps
    for step in range(3):
        best_candidate = random.randint(0, num_candidates-1)
        accept_length = random.randint(0, max_depth-1)
        position = step
        log_forensic_step(tokenizer, step, token, logits, best_candidate, accept_length, sample_p, hidden_state_new, retrieve_indices, candidates, position, None)
    sys.stdout = old
    out_text = buf.getvalue()
    out_file = os.path.join(OUT_DIR, f'sample_{i}.jsonl')
    with open(out_file, 'w') as fh:
        fh.write(out_text)
    print('Wrote', out_file)

print('Unit test complete. Files in', OUT_DIR)
