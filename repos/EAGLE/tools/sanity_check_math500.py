import sys
import os
import json
import time
from io import StringIO
from transformers import BitsAndBytesConfig

# Ensure repo root is on path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from eagle.model.ea_model import EaModel


def find_jsonl_files(base_dir):
    out = []
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.jsonl'):
                out.append(os.path.join(root, f))
    return sorted(out)


def load_samples(jsonl_path, n=5):
    samples = []
    with open(jsonl_path, 'r') as fh:
        for i, line in enumerate(fh):
            if i >= n:
                break
            try:
                obj = json.loads(line)
            except Exception:
                obj = {'text': line.strip()}
            samples.append(obj)
    return samples


def get_problem_id(obj, idx):
    for k in ['problem_id', 'unique_id', 'id', 'question_id', 'sample_id', 'idx']:
        if isinstance(obj, dict) and obj.get(k) is not None:
            return obj.get(k)
    return idx

BASE_MODEL = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'llama8b'))
EA_MODEL = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'eagle3-llama'))
DATA_DIR = os.path.abspath(os.path.join(ROOT, '..', '..', 'data', 'math500'))

print('ROOT', ROOT)
print('BASE_MODEL', BASE_MODEL)
print('EA_MODEL', EA_MODEL)
print('DATA_DIR', DATA_DIR)

# locate a jsonl
jsonl_candidates = find_jsonl_files(DATA_DIR)
if not jsonl_candidates:
    print('No jsonl found under data/math500 --- falling back to built-in sample prompts')
    sample_texts = [
        "Compute 13 + 29.",
        "What is the derivative of x^2 at x=3?",
        "Solve for x: 2x + 5 = 17.",
        "Integrate 1/x from 1 to e.",
        "Compute 7 * 8 - 15.",
    ]
    samples = [{'question': t} for t in sample_texts]
else:
    jsonl_path = jsonl_candidates[0]
    print('Using', jsonl_path)
    samples = load_samples(jsonl_path, n=5)

print('Loaded', len(samples), 'samples')
# debug previews controlled by SANITY_DEBUG env var
DEBUG = os.environ.get('SANITY_DEBUG', '0') == '1'
if DEBUG:
    for idx, sample in enumerate(samples):
            sample_text = sample.get('question') or sample.get('problem') or sample.get('input') or sample.get('prompt') or sample.get('text')
# instantiate model (may be heavy)
print('Loading EaModel.from_pretrained (this may take a while)')
quantization_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_threshold=6.0,
    llm_int8_has_fp16_weight=False,
)
model = EaModel.from_pretrained(
    use_eagle3=True,
    base_model_path=BASE_MODEL,
    ea_model_path=EA_MODEL,
    total_token=20,
    depth=3,
    top_k=8,
    quantization_config=quantization_config,
    device_map='auto',
    low_cpu_mem_usage=True,
    torch_dtype='auto',
)

device = next(model.base_model.parameters()).device
print('Model loaded on', device)

out_dir = os.path.join(ROOT, 'sanity_traces')
os.makedirs(out_dir, exist_ok=True)
summary = []

for i, sample in enumerate(samples):
    if DEBUG:
        print('---')
        print(f'Beginning sample {i}')
    # find text field
    text = None
    for k in ['question', 'input', 'prompt', 'text']:
        if k in sample:
            text = sample[k]
            break
    if text is None:
        text = json.dumps(sample)
    if DEBUG:
        print(f'sample {i} text preview:', repr(text)[:200])

    try:
        input_ids = model.tokenizer(text, return_tensors='pt', add_special_tokens=True).input_ids.to(device)

        # run once baseline without logging
        t0 = time.time()
        _ = model.eagenerate(input_ids.clone(), temperature=0.0, max_new_tokens=16, log=False)
        t_no_log = time.time() - t0

        # capture stdout for logging run
        buf = StringIO()
        old_stdout = sys.stdout
        sys.stdout = buf
        t0 = time.time()
        problem_id = get_problem_id(sample, i)
        res = model.eagenerate(
            input_ids.clone(),
            temperature=0.0,
            max_new_tokens=16,
            log=True,
            log_metadata={
                'run_id': f'sanity_{i}',
                'problem_id': problem_id,
                'model_name': os.path.basename(BASE_MODEL),
                'drafter_name': 'EAGLE-3',
                'temperature': 0.0,
            },
        )
        t_log = time.time() - t0
        sys.stdout = old_stdout

        trace_out = buf.getvalue().strip()
        trace_file = os.path.join(out_dir, f'trace_sample_{i}.jsonl')
        with open(trace_file, 'w') as fh:
            fh.write(trace_out + '\n')

        print(f'Completed sample {i} t_no_log={t_no_log:.4f}s t_log={t_log:.4f}s trace_file={trace_file}')
        summary.append({'sample': i, 't_no_log': t_no_log, 't_log': t_log, 'trace_file': trace_file, 'success': True})
    except Exception as exc:
        print(f'ERROR on sample {i}:', repr(exc))
        summary.append({'sample': i, 'success': False, 'error': str(exc)})
        continue

# write summary
with open(os.path.join(out_dir, 'summary.json'), 'w') as fh:
    json.dump(summary, fh, indent=2)

print('Done. Summary:')
print(json.dumps(summary, indent=2))
