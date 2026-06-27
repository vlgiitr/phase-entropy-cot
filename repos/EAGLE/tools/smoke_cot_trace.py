import json
import os
import sys
from io import StringIO

import torch
from datasets import load_from_disk

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from eagle.model.ea_model import EaModel

BASE_MODEL = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'llama8b'))
EA_MODEL = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'eagle3-llama'))
DATA_DIR = os.path.abspath(os.path.join(ROOT, '..', '..', 'data'))


def build_reasoning_prompt(tokenizer, problem_text, dataset_name):
    if dataset_name == 'math500':
        user_text = (
            problem_text
            + "\n\nPlease reason step by step, and put your final answer within \\boxed{}."
        )
    else:
        user_text = (
            problem_text
            + "\n\nPlease reason step by step before giving the final answer."
        )

    messages = [{"role": "user", "content": user_text}]
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    return prompt + "<think>\n"


def sample_to_text(obj):
    if isinstance(obj, str):
        return obj
    if not isinstance(obj, dict):
        return json.dumps(obj)
    for key in ['question', 'problem', 'input', 'prompt', 'text']:
        if obj.get(key):
            return obj[key]
    if obj.get('question_content') or obj.get('question_title'):
        parts = []
        if obj.get('question_title'):
            parts.append(obj['question_title'])
        if obj.get('question_content'):
            parts.append(obj['question_content'])
        if obj.get('starter_code'):
            parts.append(obj['starter_code'])
        if obj.get('public_test_cases'):
            parts.append('public_test_cases: ' + obj['public_test_cases'])
        return '\n\n'.join(parts).strip()
    return json.dumps(obj)


def main():
    dataset_name = os.environ.get('SMOKE_DATASET', 'math500').strip()
    sample_index = int(os.environ.get('SMOKE_INDEX', '0'))
    max_new_tokens = int(os.environ.get('SMOKE_MAX_NEW_TOKENS', '512'))
    max_length = int(os.environ.get('SMOKE_MAX_LENGTH', '2048'))

    dataset = load_from_disk(os.path.join(DATA_DIR, dataset_name))['test']
    sample = dataset[sample_index]
    problem_text = sample_to_text(sample)

    model = EaModel.from_pretrained(
        use_eagle3=True,
        base_model_path=BASE_MODEL,
        ea_model_path=EA_MODEL,
        total_token=20,
        depth=3,
        top_k=8,
        device_map='auto',
        low_cpu_mem_usage=True,
        torch_dtype=torch.float16,
    )

    device = next(model.base_model.parameters()).device
    prompt = build_reasoning_prompt(model.tokenizer, problem_text, dataset_name)
    tokenized = model.tokenizer(
        prompt,
        return_tensors='pt',
        add_special_tokens=True,
        truncation=True,
        max_length=max_length,
    )
    input_ids = tokenized.input_ids.to(device)

    buf = StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf
    try:
        _ = model.eagenerate(
            input_ids.clone(),
            temperature=0.0,
            max_new_tokens=max_new_tokens,
            log=True,
            log_metadata={
                'run_id': f'smoke_{dataset_name}_{sample_index}',
                'problem_id': sample_index,
                'model_name': os.path.basename(BASE_MODEL),
                'drafter_name': 'EAGLE-3',
                'temperature': 0.0,
            },
        )
    finally:
        sys.stdout = old_stdout

    rows = []
    for line in buf.getvalue().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            pass

    think_rows = [
        row for row in rows
        if row.get('token_id') == 128013 or row.get('token_str') == '<think>' or row.get('is_inside_think') is True
    ]
    endthink_rows = [
        row for row in rows
        if row.get('token_id') == 128014 or row.get('token_str') == '</think>'
    ]
    error_rows = [row for row in rows if row.get('error')]

    summary = {
        'dataset': dataset_name,
        'sample_index': sample_index,
        'rows': len(rows),
        'error_rows': len(error_rows),
        'think_rows': len(think_rows),
        'endthink_rows': len(endthink_rows),
        'first_think_row': think_rows[0] if think_rows else None,
        'first_endthink_row': endthink_rows[0] if endthink_rows else None,
        'first_error': error_rows[0] if error_rows else None,
    }
    print(json.dumps(summary, ensure_ascii=True))


if __name__ == '__main__':
    main()
