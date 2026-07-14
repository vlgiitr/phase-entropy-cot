import argparse
import json
import os
import sys
from io import StringIO
from pathlib import Path

import torch
from datasets import load_from_disk

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from eagle.model.ea_model import EaModel

BASE_MODEL = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'llama8b'))
EA_MODEL = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'eagle3-llama'))
DATA_DIR = os.path.abspath(os.path.join(ROOT, '..', '..', 'data'))
SPLIT_CHOICES = ('calibration', 'validation', 'test')


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


def _load_split_ids(dataset_name, split_name, split_locks_dir=None):
    split_locks_dir = Path(split_locks_dir or os.path.join(ROOT, '..', '..', 'splits'))
    lock_path = Path(split_locks_dir) / f'{split_name}_locked.json'
    if not lock_path.exists():
        return None
    payload = json.loads(lock_path.read_text(encoding='utf-8'))
    ids = payload.get(dataset_name)
    if isinstance(ids, list):
        return {str(item) for item in ids}
    return None


def _row_matches_split_id(row, split_ids):
    if not split_ids:
        return False
    if isinstance(row, dict):
        row_dict = row
    else:
        row_dict = dict(row)
    for key in ('unique_id', 'problem_id', 'question_id', 'id', 'contest_id', 'question_title', 'problem', 'input', 'prompt', 'text'):
        value = row_dict.get(key)
        if value is None:
            continue
        if isinstance(value, (list, tuple, dict)):
            continue
        if str(value) in split_ids:
            return True
    return False


def select_dataset_rows(dataset_name, dataset_store, split_name, split_locks_dir=None, allow_test_split=True, confirm_fn=None):
    split_name = (split_name or 'validation').strip().lower()
    if split_name not in SPLIT_CHOICES:
        raise ValueError(f'Unsupported split {split_name!r}; expected one of {SPLIT_CHOICES}')

    if split_name == 'test':
        if not allow_test_split:
            raise RuntimeError('The test split is not available by default. Pass --confirm-test-split to opt in.')
        if confirm_fn is None:
            def confirm_fn(prompt_text):
                if not sys.stdin.isatty():
                    raise RuntimeError('The test split requires an explicit confirmation. Re-run with --confirm-test-split.')
                print(prompt_text, end='', flush=True)
                response = input().strip().lower()
                return response in {'y', 'yes'}
        if not confirm_fn('You are about to run smoke tests on the test split. Continue? [y/N] '):
            raise RuntimeError('Test split selection aborted.')

    split_ids = _load_split_ids(dataset_name, split_name, split_locks_dir=split_locks_dir)
    if split_ids is not None:
        if isinstance(dataset_store, dict):
            if split_name in dataset_store:
                rows = dataset_store[split_name]
                if isinstance(rows, (list, tuple)):
                    return list(rows)
        rows = [row for row in dataset_store if _row_matches_split_id(row, split_ids)]
        if rows:
            return rows

    if isinstance(dataset_store, dict):
        if split_name in dataset_store:
            rows = dataset_store[split_name]
            return list(rows)

    raise RuntimeError(f'No rows matched the {split_name} split for dataset {dataset_name!r}.')


def parse_args():
    parser = argparse.ArgumentParser(description='Run a small EAGLE smoke generation pass.')
    parser.add_argument('--dataset', default=os.environ.get('SMOKE_DATASET', 'math500').strip(), help='Dataset name to sample from')
    parser.add_argument('--index', type=int, default=int(os.environ.get('SMOKE_INDEX', '0')), help='Sample index within the selected split')
    parser.add_argument('--max-new-tokens', type=int, default=int(os.environ.get('SMOKE_MAX_NEW_TOKENS', '512')), help='Maximum new tokens to generate')
    parser.add_argument('--max-length', type=int, default=int(os.environ.get('SMOKE_MAX_LENGTH', '2048')), help='Maximum sequence length')
    parser.add_argument('--mode', choices=['ar', 'fixed', 'controller'], default=os.environ.get('SMOKE_MODE', 'fixed'), help='Generation mode to use')
    parser.add_argument('--fixed-draft-length', type=int, default=int(os.environ.get('SMOKE_FIXED_DRAFT_LENGTH', '4')), help='Draft length to use in fixed mode')
    parser.add_argument('--controller-policy', default=os.environ.get('SMOKE_CONTROLLER_POLICY', os.path.join(ROOT, '..', '..', 'results', 'controller_real_corpus_eval_v3_frozen.json')), help='Path to the frozen controller JSON policy')
    parser.add_argument('--split', choices=SPLIT_CHOICES, default=os.environ.get('SMOKE_SPLIT', 'validation').strip() or 'validation', help='Dataset split to sample from (default: validation)')
    parser.add_argument('--confirm-test-split', action='store_true', help='Explicitly confirm that the test split should be used')
    return parser.parse_args()


def main():
    args = parse_args()
    dataset_name = args.dataset
    sample_index = args.index
    max_new_tokens = args.max_new_tokens
    max_length = args.max_length

    dataset_store = load_from_disk(os.path.join(DATA_DIR, dataset_name))
    dataset = select_dataset_rows(
        dataset_name,
        dataset_store,
        args.split,
        split_locks_dir=os.path.join(ROOT, '..', '..', 'splits'),
        allow_test_split=args.confirm_test_split,
    )
    if sample_index >= len(dataset):
        raise IndexError(f'Sample index {sample_index} is out of range for split {args.split} with {len(dataset)} rows')
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
        mode = args.mode
        controller_policy_path = args.controller_policy if mode == 'controller' else None
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
            mode=mode,
            fixed_draft_length=args.fixed_draft_length,
            controller_policy_path=controller_policy_path,
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
        'split': args.split,
        'sample_index': sample_index,
        'selected_rows': len(dataset),
        'rows': len(rows),
        'error_rows': len(error_rows),
        'think_rows': len(think_rows),
        'endthink_rows': len(endthink_rows),
        'first_think_row': think_rows[0] if think_rows else None,
        'first_endthink_row': endthink_rows[0] if endthink_rows else None,
        'first_error': error_rows[0] if error_rows else None,
        'mode': args.mode,
        'fixed_draft_length': args.fixed_draft_length,
    }
    print(json.dumps(summary, ensure_ascii=True))


if __name__ == '__main__':
    main()
