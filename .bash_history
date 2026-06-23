    msw2=ssw2/(N2-g2)
    kbar2=np.mean([len(v) for v in trace_vals2])
    icc2=(msb2-msw2)/(msb2+(kbar2-1)*msw2) if (msb2+(kbar2-1)*msw2)!=0 else float('nan')
    print('ICC(1) sample_p_top1', icc2, 'g', g2, 'N', N2, 'kbar', kbar2)
else:
    print('no sample_p_top1 data')
PY

 cd /teamspace/studios/this_studio && python - <<'PY'
import json, os, numpy as np
from collections import defaultdict
import math

trace_dir='repos/EAGLE/pilot_traces'
summary=json.load(open(os.path.join(trace_dir,'summary.json')))
trace_entries=[e for e in summary if e.get('success')]
all_rows=[]
for e in trace_entries:
    path=e['trace_file']
    if not os.path.exists(path):
        continue
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            d=json.loads(line)
            def maybe_float(x):
                if x is None:
                    return np.nan
                return float(x)
            def maybe_int(x):
                return int(x) if x is not None else np.nan
            d2={
                'dataset': e['dataset'],
                'idx': e['idx'],
                'step': maybe_int(d.get('step')),
                'position': maybe_int(d.get('position')),
                'tree_depth': maybe_int(d.get('tree_depth')),
                'accepted': bool(d.get('accepted')),
                'accept_length': maybe_int(d.get('accept_length')),
                'token': d.get('token'),
                'think_flag': bool(d.get('think_flag')),
                'top1_p': maybe_float(d.get('top1_p')),
                'sample_p_top1': maybe_float(d.get('sample_p_top1')),
            }
            all_rows.append(d2)
print('trace entries', len(trace_entries), 'token rows', len(all_rows))
all_top1 = np.array([r['top1_p'] for r in all_rows if not math.isnan(r['top1_p'])])
print('top1_p mean', np.mean(all_top1), 'std', np.std(all_top1), 'min', np.min(all_top1), 'max', np.max(all_top1))
print('accepted rate', np.mean([r['accepted'] for r in all_rows]))
print('think rate', np.mean([r['think_flag'] for r in all_rows]))
print('mean tree depth', np.nanmean([r['tree_depth'] for r in all_rows]))
counts=defaultdict(int)
for r in all_rows:
    counts[(r['dataset'], r['idx'])]+=1
lens=sorted(counts.values())
print('token lengths: min', lens[0], 'max', lens[-1], 'median', np.median(lens))
print('len distribution tail', lens[:10], '...', lens[-10:])
lag_stats={lag:[] for lag in range(1,6)}
by_trace=defaultdict(list)
for r in all_rows:
    by_trace[(r['dataset'], r['idx'])].append(r)
for key, rows in by_trace.items():
    vals=[r['top1_p'] for r in sorted(rows, key=lambda x:x['step']) if not math.isnan(r['top1_p'])]
    n=len(vals)
    if n<6:
        continue
    mean=np.mean(vals)
    denom=np.sum((vals-mean)**2)
    if denom==0:
        continue
    for lag in range(1,6):
        num=np.sum((np.array(vals[:-lag])-mean)*(np.array(vals[lag:])-mean))
        lag_stats[lag].append(num/denom)
print('autocorr:')
for lag in range(1,6):
    arr=np.array(lag_stats[lag])
    print(lag, 'n', len(arr), 'mean', np.mean(arr), 'std', np.std(arr), 'min', np.min(arr), 'max', np.max(arr))
trace_vals=[np.array([r['top1_p'] for r in sorted(rows, key=lambda x:x['step']) if not math.isnan(r['top1_p'])]) for rows in by_trace.values()]
trace_vals=[v for v in trace_vals if len(v)>1]
grand=np.concatenate(trace_vals)
g_mean=np.mean(grand)
g=len(trace_vals)
N=len(grand)
ssb=sum(len(v)*(np.mean(v)-g_mean)**2 for v in trace_vals)
ssw=sum(np.sum((v-np.mean(v))**2) for v in trace_vals)
msb=ssb/(g-1)
msw=ssw/(N-g)
kbar=np.mean([len(v) for v in trace_vals])
icc1=(msb-msw)/(msb+(kbar-1)*msw) if (msb+(kbar-1)*msw)!=0 else np.nan
print('ICC(1) top1_p', icc1, 'g', g, 'N', N, 'kbar', kbar)
all_samp=np.array([r['sample_p_top1'] for r in all_rows if not math.isnan(r['sample_p_top1'])])
print('sample_p_top1 count', len(all_samp), 'mean', np.mean(all_samp), 'std', np.std(all_samp))
PY

 cd /teamspace/studios/this_studio && python repos/EAGLE/tools/pilot_analysis.py
 cd /teamspace/studios/this_studio && python - <<'PY'
import json, os, math
from collections import defaultdict
import numpy as np

trace_dir='repos/EAGLE/pilot_traces'
summary=json.load(open(os.path.join(trace_dir,'summary.json')))
rows=[]
for e in summary:
    if not e.get('success'):
        continue
    with open(e['trace_file']) as f:
        for line in f:
            if not line.strip():
                continue
            d=json.loads(line)
            rows.append({'dataset': e['dataset'], 'step': d.get('step'), 'top1_p': d.get('top1_p'), 'accepted': bool(d.get('accepted')), 'think_flag': bool(d.get('think_flag')), 'tree_depth': d.get('tree_depth')})

def stats(rs):
    valid=[float(x['top1_p']) for x in rs if x['top1_p'] is not None]
    return {'count': len(rs), 'top1_mean': np.mean(valid), 'top1_std': np.std(valid), 'accepted_rate': np.mean([x['accepted'] for x in rs]), 'think_rate': np.mean([x['think_flag'] for x in rs]), 'tree_depth_mean': np.mean([x['tree_depth'] for x in rs if x['tree_depth'] is not None])}

all_stats=stats(rows)
print('all', all_stats)
by=defaultdict(list)
for r in rows:
    by[r['dataset']].append(r)
for k,v in by.items():
    print(k, stats(v))
PY

 cd /teamspace/studios/this_studio && python - <<'PY'
import json, os
path = 'data/math500/test.jsonl'
print('math500 exists', os.path.exists(path))
if os.path.exists(path):
    with open(path) as f:
        for i, line in enumerate(f):
            if i >= 5: break
            obj=json.loads(line)
            print(i, {k: obj.get(k) for k in ['problem_id','id','question','input','prompt','text']})

print('--------------------------------')

arrow_dir='data/livecodebench/test'
print('lcb dir exists', os.path.isdir(arrow_dir))
if os.path.isdir(arrow_dir):
    import pyarrow as pa
    files = sorted([os.path.join(arrow_dir,f) for f in os.listdir(arrow_dir) if f.endswith('.arrow')])
    print('arrow files', files[:3])
    if files:
        try:
            reader = pa.ipc.open_file(files[0])
        except Exception:
            reader = pa.ipc.open_stream(files[0])
        tbl = reader.read_all()
        d = tbl.to_pydict()
        print('keys', list(d.keys())[:20])
        print('len', len(next(iter(d.values()))))
        for i in range(min(3, len(next(iter(d.values()))))):
            print(i, {k:d[k][i] for k in list(d.keys())[:10]})
PY

 cd /teamspace/studios/this_studio && python - <<'PY'
import json, os
print('math500 exists', os.path.exists('data/math500/test.jsonl'))
if os.path.exists('data/math500/test.jsonl'):
    with open('data/math500/test.jsonl') as f:
        for i, line in enumerate(f):
            if i >= 3: break
            obj = json.loads(line)
            print('math500', i, {k: obj.get(k) for k in ['problem_id','id','question','input','prompt','text']})
print('---')
arrow_dir='data/livecodebench/test'
print('lcb dir exists', os.path.isdir(arrow_dir))
if os.path.isdir(arrow_dir):
    import pyarrow as pa
    files = sorted([os.path.join(arrow_dir, f) for f in os.listdir(arrow_dir) if f.endswith('.arrow')])
    print('arrow files count', len(files), 'first3', files[:3])
    if files:
        try:
            reader = pa.ipc.open_file(files[0])
        except Exception:
            reader = pa.ipc.open_stream(files[0])
        table = reader.read_all()
        d = table.to_pydict()
        print('keys', list(d.keys())[:20])
        print('rows', len(next(iter(d.values()))))
        for i in range(min(3, len(next(iter(d.values()))))):
            row = {k: d[k][i] for k in list(d.keys())[:10]}
            print('lcb', i, row)
PY

 cd /teamspace/studios/this_studio && python - <<'PY' > /tmp/dataset_ids.txt
import json, os
print('math500 exists', os.path.exists('data/math500/test.jsonl'))
if os.path.exists('data/math500/test.jsonl'):
    with open('data/math500/test.jsonl') as f:
        for i, line in enumerate(f):
            if i >= 3: break
            obj = json.loads(line)
            print('math500', i, {k: obj.get(k) for k in ['problem_id','id','question','input','prompt','text']})
print('---')
arrow_dir='data/livecodebench/test'
print('lcb dir exists', os.path.isdir(arrow_dir))
if os.path.isdir(arrow_dir):
    import pyarrow as pa
    files = sorted([os.path.join(arrow_dir, f) for f in os.listdir(arrow_dir) if f.endswith('.arrow')])
    print('arrow files count', len(files), 'first', files[:3])
    if files:
        try:
            reader = pa.ipc.open_file(files[0])
        except Exception:
            reader = pa.ipc.open_stream(files[0])
        table = reader.read_all()
        d = table.to_pydict()
        keys = list(d.keys())
        print('keys', keys[:20])
        print('rows', len(next(iter(d.values()))))
        for i in range(min(3, len(next(iter(d.values()))))):
            print('lcb', i, {k: d[k][i] for k in keys[:10]})
PY

 cd /teamspace/studios/this_studio && if [ -f /tmp/dataset_ids.txt ]; then sed -n '1,200p' /tmp/dataset_ids.txt; else echo 'no file'; fi
 cd /teamspace/studios/this_studio && python - <<'PY'
import json, os

print('math500 exists', os.path.exists('data/math500/test.jsonl'))
if os.path.exists('data/math500/test.jsonl'):
    with open('data/math500/test.jsonl') as f:
        for i, line in enumerate(f):
            if i >= 3: break
            obj = json.loads(line)
            print('math500', i, {k: obj.get(k) for k in ['problem_id','id','question','input','prompt','text']})

arrow_dir = 'data/livecodebench/test'
print('lcb dir exists', os.path.isdir(arrow_dir))
if os.path.isdir(arrow_dir):
    import pyarrow as pa
    files = sorted([os.path.join(arrow_dir, f) for f in os.listdir(arrow_dir) if f.endswith('.arrow')])
    print('arrow files count', len(files), 'first', files[:3])
    if files:
        reader = pa.ipc.open_file(files[0]) if pa.ipc.is_stream_reader(pa.memory_map(files[0])) else pa.ipc.open_file(files[0])
        table = reader.read_all()
        d = table.to_pydict()
        keys = list(d.keys())
        print('keys', keys[:20])
        print('rows', len(next(iter(d.values()))))
        for i in range(min(3, len(next(iter(d.values()))))):
            print('lcb', i, {k: d[k][i] for k in keys[:10]})
PY

 cd /teamspace/studios/this_studio && echo '--- math head ---' && head -n 3 data/math500/test.jsonl | sed -n '1,3p' && echo '--- lcb arrow metadata ---' && python - <<'PY'
import pyarrow as pa, os
arrow_dir = 'data/livecodebench/test'
files = sorted([os.path.join(arrow_dir, f) for f in os.listdir(arrow_dir) if f.endswith('.arrow')])
print('files', files[:3])
reader = pa.ipc.open_file(files[0])
table = reader.read_all()
print('keys', list(table.schema.names)[:20])
print('len', len(table))
print('first', table.slice(0,3).to_pydict())
PY

 cd /teamspace/studios/this_studio && python - <<'PY'
import os, pyarrow as pa
arrow_dir = 'data/livecodebench/test'
files = sorted([os.path.join(arrow_dir,f) for f in os.listdir(arrow_dir) if f.endswith('.arrow')])
print('files count', len(files))
if files:
    reader = pa.ipc.open_stream(files[0])
    table = reader.read_all()
    print('schema names', table.schema.names)
    print('rows', len(table))
PY

 cd /teamspace/studios/this_studio && python - <<'PY'
import os, json
p='data/math500/dataset_dict.json'
print('path', os.path.exists(p))
if os.path.exists(p):
    with open(p) as f:
        d=json.load(f)
    print('keys', list(d.keys())[:20])
    print('sample keys', {k: type(v) for k,v in d.items() if k in ['test']})
    if 'test' in d:
        print('test count', len(d['test']))
        print('test first', d['test'][:3])
PY

 cd /teamspace/studios/this_studio && python - <<'PY'
import os, json
math_path='data/math500/test.jsonl'
count=0
uids=[]
with open(math_path) as f:
    for line in f:
        obj=json.loads(line)
        count +=1
        uid=obj.get('unique_id') or obj.get('problem_id') or obj.get('id') or f'math500_{count}'
        uids.append(uid)
print('math500 count', count)
print('sample unique_ids', uids[:5])

import pyarrow as pa
arrow_dir='data/livecodebench/test'
files=sorted([os.path.join(arrow_dir,f) for f in os.listdir(arrow_dir) if f.endswith('.arrow')])
print('lcb arrow files', len(files))
total=0
qids=[]
for f in files:
    reader=pa.ipc.open_stream(f)
    tbl=reader.read_all()
    d=tbl.to_pydict()
    ids=d.get('question_id') or d.get('unique_id') or []
    n=len(next(iter(d.values()))) if d else 0
    total += n
    if len(qids)<5:
        qids.extend(ids[:5])
print('lcb count', total)
print('sample question_ids', qids[:5])
PY

 cd /teamspace/studios/this_studio && python - <<'PY'
import os, json, random
random.seed(0)
math_ids=[]
with open('data/math500/test.jsonl') as f:
    for line in f:
        obj=json.loads(line)
        uid=obj.get('unique_id') or obj.get('problem_id') or obj.get('id')
        if uid is None:
            continue
        math_ids.append(uid)

# create a 25% locked test split from math500 by problem id
k = len(math_ids) // 4
locked = sorted(math_ids[:k])
with open('splits/test_locked.json', 'w') as f:
    json.dump({'math500': locked, 'livecodebench': []}, f, indent=2)
print('locked math500 count', len(locked))
print('sample locked ids', locked[:5])
PY

 cd /teamspace/studios/this_studio && ps -ef | grep -E 'python .*sanity_check_math500.py' | grep -v grep || true
 cd /teamspace/studios/this_studio && ps -p 16667 -o pid,etime,cmd
 cd /teamspace/studios/this_studio && python repos/EAGLE/tools/sanity_check_math500.py
 cd /teamspace/studios/this_studio && ps -ef | grep -E 'sanity_check_math500.py|EaModel.from_pretrained' | grep -v grep || true
 cd /teamspace/studios/this_studio && python - <<'PY'
import time, os, signal
pid=16667
for _ in range(6):
    try:
        os.kill(pid, 0)
        print('alive')
    except OSError:
        print('dead')
        break
    time.sleep(10)
PY

 cd /teamspace/studios/this_studio && ls -1 repos/EAGLE/sanity_traces && python - <<'PY'
import json, os
summary_path='repos/EAGLE/sanity_traces/summary.json'
if os.path.exists(summary_path):
    with open(summary_path) as f:
        summary=json.load(f)
    print('summary_count', len(summary))
    print('first_summary', summary[0])
else:
    print('summary missing')
trace_file='repos/EAGLE/sanity_traces/trace_sample_0.jsonl'
if os.path.exists(trace_file):
    with open(trace_file) as f:
        lines=f.readlines()
    print('trace_lines', len(lines))
    if lines:
        print('trace0', lines[0].strip())
else:
    print('trace missing')
PY

 cd /teamspace/studios/this_studio && python repos/EAGLE/tools/sanity_check_math500.py
 cd /teamspace/studios/this_studio && ps -ef | grep -E 'python .*sanity_check_math500.py' | grep -v grep || true
 cd /teamspace/studios/this_studio && python - <<'PY'
import os, time
pid=None
for proc in os.popen("ps -ef | grep '[p]ython repos/EAGLE/tools/sanity_check_math500.py'").read().strip().splitlines():
    parts=proc.split()
    if parts:
        pid=int(parts[1])
        break
print('pid', pid)
for _ in range(12):
    if pid is None:
        print('process not found')
        break
    try:
        os.kill(pid,0)
        print('alive')
    except OSError:
        print('dead')
        break
    time.sleep(10)
PY

 cd /teamspace/studios/this_studio && python - <<'PY'
import os, time
pid=18616
for _ in range(6):
    try:
        os.kill(pid,0)
        print('alive')
    except OSError:
        print('dead')
        break
    time.sleep(10)
PY

 cd /teamspace/studios/this_studio && ps -ef | grep -E 'python .*sanity_check_math500.py' | grep -v grep || true && echo '---' && ls -l repos/EAGLE/sanity_traces/summary.json repos/EAGLE/sanity_traces/trace_sample_0.jsonl 2>/dev/null || true
python3 repos/EAGLE/tools/convert_traces_to_p1.py
# Run analysis (writes `repos/EAGLE/pilot_traces/analysis.json`)
python3 repos/EAGLE/tools/pilot_analysis.py
# Pretty-print analysis.json (full)
python3 -c "import json,sys;print(json.dumps(json.load(open('repos/EAGLE/pilot_traces/analysis.json')),indent=2))"
# Print ICC and autocorrelation sections specifically
python3 - <<'PY'
import json
a=json.load(open('repos/EAGLE/pilot_traces/analysis.json'))
print('ICC:')
print(json.dumps(a.get('icc'), indent=2))
print('\\nAutocorrelation:')
print(json.dumps(a.get('autocorr'), indent=2))
PY

# Quick check of a sample trace to confirm P1 fields (token_str, draft_top1_prob, is_inside_think)
head -n1 repos/EAGLE/pilot_traces/trace_math500_0.jsonl | python3 -m json.tool
rm -rf repos/EAGLE/pilot_traces
mkdir -p repos/EAGLE/pilot_traces
# Run the pilot harness (generates 30 Math500 + 20 LCB traces)
python3 repos/EAGLE/tools/pilot_run.py
# Convert legacy fields to P1 (safe no-op if already P1)
python3 repos/EAGLE/tools/convert_traces_to_p1.py
# Run analysis (writes repos/EAGLE/pilot_traces/analysis.json)
python3 repos/EAGLE/tools/pilot_analysis.py
# Print ICC and autocorrelation sections for quick copy/paste
python3 - <<'PY'
import json
a=json.load(open('repos/EAGLE/pilot_traces/analysis.json'))
print('ICC:')
print(json.dumps(a.get('icc'), indent=2))

cd /teamspace/studios/this_studio
python3 repos/EAGLE/tools/pilot_analysis.py
cd /teamspace/studios/this_studio
python3 repos/EAGLE/tools/pilot_analysis.py
python3 - <<'PY'
import json
a=json.load(open('repos/EAGLE/pilot_traces/analysis.json'))
print('ICC:')
print(json.dumps(a.get('icc'), indent=2))
print('\\nAutocorrelation:')
print(json.dumps(a.get('autocorr'), indent=2))
PY

 cd /teamspace/studios/this_studio && if ps -p 18616 > /dev/null 2>&1; then echo alive; else echo dead; fi && echo '---' && if [ ! -f repos/EAGLE/sanity_traces/trace_sample_0.jsonl ]; then echo missing; else python - <<'PY'
import json
for path in ['repos/EAGLE/sanity_traces/summary.json','repos/EAGLE/sanity_traces/trace_sample_0.jsonl']:
    print('FILE', path)
    try:
        with open(path) as f:
            if path.endswith('.json'):
                print(json.load(f)[0])
            else:
                print(f.readline().strip())
    except Exception as e:
        print('ERROR', e)
PY; fi
 cd /teamspace/studios/this_studio && if ps -p 18616 > /dev/null 2>&1; then echo alive; else echo dead; fi && echo '---' && python - <<'PY'
import json
for path in ['repos/EAGLE/sanity_traces/summary.json', 'repos/EAGLE/sanity_traces/trace_sample_0.jsonl']:
    print('FILE', path)
    try:
        with open(path) as f:
            if path.endswith('.json'):
                print(json.load(f)[0])
            else:
                print(f.readline().strip())
    except Exception as e:
        print('ERROR', e)
PY
  cd /teamspace/studios/this_studio && if ps -p 18616 > /dev/null 2>&1; then echo alive; else echo dead; fi; echo '---'; echo 'summary:'; head -n 1 repos/EAGLE/sanity_traces/summary.json; echo '---'; echo 'trace0:'; head -n 1 repos/EAGLE/sanity_traces/trace_sample_0.jsonl;  cd /teamspace/studios/this_studio && echo TEST;  cd /teamspace/studios/this_studio && python repos/EAGLE/tools/pilot_run.py;  cd /teamspace/studios/this_studio && ps -ef | grep -E 'python .*pilot_run.py' | grep -v grep || true && echo '---' && ls -1 repos/EAGLE/pilot_traces 2>/dev/null | head -n 20;  cd /teamspace/studios/this_studio && echo OK;  cd /teamspace/studios/this_studio && pwd && ls -1 | head;  pwd;  cd /teamspace/studios/this_studio && python -c "import os, time; p='repos/EAGLE/pilot_traces/analysis.json'; print(os.path.exists(p)); print(time.ctime(os.path.getmtime(p)) if os.path.exists(p) else 'missing')"
 cd /teamspace/studios/this_studio && python - <<'PY'
import os, glob, time
paths = glob.glob('repos/EAGLE/pilot_traces/*.jsonl') + ['repos/EAGLE/pilot_traces/analysis.json']
for p in sorted(paths):
    if os.path.exists(p):
        print(p, os.path.getmtime(p), time.ctime(os.path.getmtime(p)))
PY
  cd /teamspace/studios/this_studio && echo hello && pwd;  cd /teamspace/studios/this_studio && echo READY;  cd /teamspace/studios/this_studio && rm -rf repos/EAGLE/pilot_traces/* && python repos/EAGLE/tools/pilot_run.py;  cd /teamspace/studios/this_studio && python repos/EAGLE/tools/convert_traces_to_p1.py;  cd /teamspace/studios/this_studio && python3 repos/EAGLE/tools/convert_traces_to_p1.py;  cd /teamspace/studios/this_studio && python3 repos/EAGLE/tools/convert_traces_to_p1.py && python3 repos/EAGLE/tools/pilot_analysis.py repos/EAGLE/pilot_traces && git add repos/EAGLE/pilot_traces && git commit -m "Update pilot traces to P1 schema and refreshed analysis" || true;  cd /teamspace/studios/this_studio && python3 repos/EAGLE/tools/convert_traces_to_p1.py && python3 repos/EAGLE/tools/pilot_analysis.py repos/EAGLE/pilot_traces && git add repos/EAGLE/pilot_traces repos/EAGLE/tools/convert_traces_to_p1.py && git commit -m "Convert pilot traces to P1 schema and refresh analysis" || true;  cd /teamspace/studios/this_studio && echo START_CONVERT && python3 -u repos/EAGLE/tools/convert_traces_to_p1.py && echo DONE_CONVERT && echo START_ANALYSIS && python3 -u repos/EAGLE/tools/pilot_analysis.py repos/EAGLE/pilot_traces && echo DONE_ANALYSIS && git add repos/EAGLE/pilot_traces repos/EAGLE/tools/convert_traces_to_p1.py && git commit -m "Convert pilot traces to P1 schema and refresh analysis" || echo NO_COMMIT
 cd /teamspace/studios/this_studio && python3 - <<'PY'
print('PING')
PY
  cd /teamspace/studios/this_studio && echo test-terminal > /tmp/studio_terminal_test.txt;  cd /teamspace/studios/this_studio && python3 repos/EAGLE/tools/convert_traces_to_p1.py && python3 repos/EAGLE/tools/pilot_analysis.py;  cd /teamspace/studios/this_studio && python3 repos/EAGLE/tools/convert_traces_to_p1.py > /tmp/conv.log 2>&1; echo CONV_EXIT:$?; tail -n 20 /tmp/conv.log; echo '---'; python3 repos/EAGLE/tools/pilot_analysis.py > /tmp/anl.log 2>&1; echo ANAL_EXIT:$?; tail -n 20 /tmp/anl.log;  ls -l /tmp/conv.log /tmp/anl.log 2>/dev/null; echo '---'; if [ -s /tmp/conv.log ]; then echo CONV_CONTENT; tail -n 20 /tmp/conv.log; fi; echo '---'; if [ -s /tmp/anl.log ]; then echo ANAL_CONTENT; tail -n 20 /tmp/anl.log; fi;  pwd && whoami && ls /tmp | head;  echo hi;  cd /teamspace/studios/this_studio && python3 repos/EAGLE/tools/convert_traces_to_p1.py && python3 repos/EAGLE/tools/pilot_analysis.py;  cd /teamspace/studios/this_studio && python3 repos/EAGLE/tools/pilot_run.py > /tmp/pilot_run.log 2>&1; echo PILOT_EXIT:$?; tail -n 120 /tmp/pilot_run.log; python3 repos/EAGLE/tools/convert_traces_to_p1.py > /tmp/conv.log 2>&1; echo CONV_EXIT:$?; tail -n 120 /tmp/conv.log; python3 repos/EAGLE/tools/pilot_analysis.py > /tmp/anl.log 2>&1; echo ANAL_EXIT:$?; tail -n 200 /tmp/anl.log;  cd /teamspace/studios/this_studio && python3 repos/EAGLE/tools/pilot_analysis.py > /tmp/anl.log 2>&1; echo ANAL_EXIT:$?; tail -n 200 /tmp/anl.log
ssh root@164.52.193.242
