 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python -m unittest test_level_controller.py
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python level_controller.py --self-test --max-traces 24 --out /teamspace/studios/this_studio/repos/EAGLE/tools/level_controller_selftest.json
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python -m unittest -v test_level_controller.py
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python level_controller.py --self-test --max-traces 24 --out /teamspace/studios/this_studio/repos/EAGLE/tools/level_controller_selftest.json | head -n 80
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python -m unittest -v test_level_controller.LevelControllerTests.test_pipeline_runs_synthetic
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python -m unittest -v test_level_controller.py
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python -m unittest test_level_controller.py -q
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python level_controller.py --self-test --max-traces 24 --out /teamspace/studios/this_studio/repos/EAGLE/tools/level_controller_selftest.json
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python -m unittest -v test_level_controller.LevelControllerTests.test_pipeline_runs_synthetic
 cd /teamspace/studios/this_studio/repos/EAGLE/tools && python level_controller.py --self-test --max-traces 24 --out /teamspace/studios/this_studio/repos/EAGLE/tools/level_controller_selftest.json && python - <<'PY'
import json
p='/teamspace/studios/this_studio/repos/EAGLE/tools/level_controller_selftest.json'
obj=json.load(open(p))
print('controller_tpc',obj['controller']['validation']['tokens_per_call'])
print('controller_rej',obj['controller']['validation']['rejection_rate'])
print('fixed_L2_rej',obj['baselines']['fixed_L2']['rejection_rate'])
print('policy_bins',obj['controller']['params']['bin_lengths'])
PY

 cd /teamspace/studios/this_studio && command -v soffice || command -v libreoffice || python - <<'PY'
import importlib.util
print('python-docx' if importlib.util.find_spec('docx') else 'no-python-docx')
PY

 cd /teamspace/studios/this_studio && python -m pip install --user python-docx
 cd /teamspace/studios/this_studio && python - <<'PY'
import re
from pathlib import Path
from docx import Document

rtf_path = Path('Implementation_Log_Current_Stage.rtf')
out_path = Path('Implementation_Log_Current_Stage.docx')

raw = rtf_path.read_text(encoding='utf-8', errors='ignore')

# Basic RTF to plain text cleanup for this simple document.
text = raw
text = text.replace('\\par', '\n')
text = re.sub(r'\\u-?\d+\??', ' ', text)
text = re.sub(r'\\[a-zA-Z]+-?\d* ?', '', text)
text = text.replace('{', '').replace('}', '')
text = text.replace('  ', ' ')
lines = [ln.strip() for ln in text.splitlines()]
lines = [ln for ln in lines if ln]

# Rebuild DOCX with simple heading detection.
doc = Document()
for line in lines:
    if line.startswith('Implementation Log'):
        doc.add_heading(line, level=1)
    elif re.match(r'^\d+\)', line):
        doc.add_heading(line, level=2)
    else:
        doc.add_paragraph(line)

doc.save(out_path)
print(out_path)
PY

 head -n 20 repos/EAGLE/pilot_traces/summary.json
 python3 -c '
import json, numpy as np

with open("repos/EAGLE/pilot_traces/summary.json", "r") as f:
    data = json.load(f)

total_rows = len(data)
success_count = sum(1 for x in data if x.get("success") is True)
fail_count = sum(1 for x in data if x.get("success") is False)

dataset_counts = {}
for x in data:
    ds = x.get("dataset")
    dataset_counts[ds] = dataset_counts.get(ds, 0) + 1

t_no_logs = [x["t_no_log"] for x in data if "t_no_log" in x]
t_logs = [x["t_log"] for x in data if "t_log" in x]

overhead_ratios = [x["t_log"] / x["t_no_log"] for x in data if "t_log" in x and "t_no_log" in x and x["t_no_log"] > 0]
absolute_overheads = [x["t_log"] - x["t_no_log"] for x in data if "t_log" in x and "t_no_log" in x]

print(f"Total rows: {total_rows}")
print(f"Success/Fail counts: Success: {success_count}, Fail: {fail_count}")
print(f"Per-dataset counts: {dataset_counts}")

if t_no_logs:
    print(f"t_no_log: mean={np.mean(t_no_logs):.4f}, median={np.median(t_no_logs):.4f}, min={np.min(t_no_logs):.4f}, max={np.max(t_no_logs):.4f}")
if t_logs:
    print(f"t_log: mean={np.mean(t_logs):.4f}, median={np.median(t_logs):.4f}, min={np.min(t_logs):.4f}, max={np.max(t_logs):.4f}")
if overhead_ratios:
    print(f"Mean overhead ratio (t_log/t_no_log): {np.mean(overhead_ratios):.4f}")
if absolute_overheads:
    print(f"Mean absolute overhead seconds (t_log - t_no_log): {np.mean(absolute_overheads):.4f}")
'
