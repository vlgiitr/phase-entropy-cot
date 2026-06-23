import os
import sys
import json
import time
from io import StringIO
import torch
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from eagle.model.ea_model import EaModel

MATH_JSONL = os.path.abspath(os.path.join(ROOT, '..', '..', 'data', 'math500', 'test.jsonl'))
LCB_JSONL = os.path.abspath(os.path.join(ROOT, '..', '..', 'data', 'livecodebench', 'test.jsonl'))
LCB_ARROW_DIR = os.path.abspath(os.path.join(ROOT, '..', '..', 'data', 'livecodebench', 'test'))
BASE_MODEL = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'llama8b'))
EA_MODEL = os.path.abspath(os.path.join(ROOT, '..', '..', 'models', 'eagle3-llama'))

OUT_DIR = os.path.join(ROOT, 'pilot_traces')
os.makedirs(OUT_DIR, exist_ok=True)

def load_samples(path, n):
    out = []
    if not os.path.exists(path):
        return out
    with open(path) as fh:
        for i,line in enumerate(fh):
            if i>=n: break
            try:
                obj=json.loads(line)
            except Exception:
                obj={'text': line.strip()}
            out.append(obj)
    return out


def sample_to_text(obj):
    if isinstance(obj, str):
        return obj
    if not isinstance(obj, dict):
        return json.dumps(obj)
    for key in ['question', 'problem', 'input', 'prompt', 'text']:
        if obj.get(key):
            return obj[key]
    # LiveCodeBench-style object
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


def get_problem_id(obj, idx):
    for k in ['problem_id', 'unique_id', 'id', 'question_id', 'sample_id', 'idx']:
        if isinstance(obj, dict) and obj.get(k) is not None:
            return obj.get(k)
    return idx


def load_samples_from_arrow_dir(dirpath, n):
    # Read arrow shard files until we have n samples
    out = []
    try:
        import pyarrow as pa
    except Exception:
        return out
    if not os.path.isdir(dirpath):
        return out
    files = sorted([os.path.join(dirpath, f) for f in os.listdir(dirpath) if f.endswith('.arrow')])
    for f in files:
        try:
            try:
                reader = pa.ipc.open_file(f)
            except Exception:
                reader = pa.ipc.open_stream(f)
            with reader:
                table = reader.read_all()
                rows = table.to_pydict()
                keys = list(rows.keys())
                length = len(rows[keys[0]]) if keys else 0
                for i in range(length):
                    if len(out) >= n:
                        break
                    obj = {k: rows[k][i] for k in keys}
                    out.append(obj)
        except Exception:
            continue
        if len(out) >= n:
            break
    return out

math_samples = load_samples(MATH_JSONL, 30)
if os.path.exists(LCB_JSONL):
    lcb_samples = load_samples(LCB_JSONL, 20)
else:
    lcb_samples = load_samples_from_arrow_dir(LCB_ARROW_DIR, 20)
print('pilot: math=', len(math_samples), 'lcb=', len(lcb_samples), 'arrow_dir=', LCB_ARROW_DIR)

samples = []
for i,s in enumerate(math_samples):
    samples.append({'dataset':'math500','idx':i,'obj':s})
for i,s in enumerate(lcb_samples):
    samples.append({'dataset':'livecodebench','idx':i,'obj':s})

if not samples:
    print('No samples found; aborting')
    sys.exit(1)

print('Loading model...')
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
print('Model loaded on', device)

summary = []
all_trace_rows = []
for s in samples:
    ds = s['dataset']
    idx = s['idx']
    obj = s['obj']
    # find text
    text = obj.get('question') or obj.get('input') or obj.get('prompt') or obj.get('text') or json.dumps(obj)
    print('Running', ds, idx)
    try:
        text = sample_to_text(obj)
        tokenized = model.tokenizer(
            text,
            return_tensors='pt',
            add_special_tokens=True,
            truncation=True,
            max_length=2048,
        )
        input_ids = tokenized.input_ids.to(device)
        if input_ids.shape[1] == 2048:
            print('  [WARN] input truncated to 2048 tokens')
        try:
            torch.cuda.empty_cache()
        except Exception:
            pass
        t0=time.time()
        _ = model.eagenerate(input_ids.clone(), temperature=0.0, max_new_tokens=1024, log=False)
        t_no_log = time.time()-t0

        buf = StringIO()
        old_stdout = sys.stdout
        sys.stdout = buf
        t0=time.time()
        problem_id = get_problem_id(obj, idx)
        _ = model.eagenerate(
            input_ids.clone(),
            temperature=0.0,
            max_new_tokens=1024,
            log=True,
            log_metadata={
                'run_id': f'{ds}_{idx}',
                'problem_id': problem_id,
                'model_name': os.path.basename(BASE_MODEL),
                'drafter_name': 'EAGLE-3',
                'temperature': 0.0,
            },
        )
        t_log = time.time()-t0
        sys.stdout = old_stdout

        trace_out = buf.getvalue().strip()
        trace_rows = []
        for line in trace_out.splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            row['dataset'] = ds
            row['idx'] = idx
            row['problem_id'] = problem_id
            all_trace_rows.append(row)
            trace_rows.append(row)
        trace_file = os.path.join(OUT_DIR, f'trace_{ds}_{idx}.jsonl')
        with open(trace_file,'w') as fh:
            fh.write(trace_out + '\n')
        summary.append({'dataset':ds,'idx':idx,'t_no_log':t_no_log,'t_log':t_log,'trace_file':trace_file,'success':True})
        print('Done', ds, idx, f't_no_log={t_no_log:.3f}s t_log={t_log:.3f}s')
    except Exception as e:
        print('ERROR', ds, idx, e)
        summary.append({'dataset':ds,'idx':idx,'success':False,'error':str(e)})

with open(os.path.join(OUT_DIR,'summary.json'),'w') as fh:
    json.dump(summary, fh, indent=2)

if all_trace_rows:
    df = pd.DataFrame(all_trace_rows)
    df.to_parquet(os.path.join(OUT_DIR, 'pilot_corpus.parquet'), index=False)

print('Pilot finished. summary written to', os.path.join(OUT_DIR,'summary.json'))
