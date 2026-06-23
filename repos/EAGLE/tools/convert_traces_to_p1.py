import os, json, math
from glob import glob
import math

PILOT_DIR = os.path.join(os.path.dirname(__file__), '..', 'pilot_traces')
PILOT_DIR = os.path.abspath(PILOT_DIR)

def softmax(xs):
    exps = [math.exp(x) for x in xs]
    s = sum(exps)
    return [e / s for e in exps]

files = glob(os.path.join(PILOT_DIR, '*.jsonl'))
for p in files:
    out_lines = []
    changed = False
    with open(p, 'r') as fh:
        for line in fh:
            try:
                row = json.loads(line)
            except Exception:
                out_lines.append(line)
                continue
            # token -> token_str; drop legacy token field
            if 'token' in row:
                if 'token_str' not in row:
                    row['token_str'] = row.get('token')
                row.pop('token', None)
                changed = True
            # top1_p -> draft_top1_prob
            if 'top1_p' in row:
                if 'draft_top1_prob' not in row:
                    row['draft_top1_prob'] = row.get('top1_p')
                row.pop('top1_p', None)
                changed = True
            # topk -> draft_topk_probs (convert logits->prob if needed)
            if 'topk' in row:
                topk = row.get('topk', [])
                probs = None
                # check if logit present
                if topk and all(('logit' in t) for t in topk):
                    logits = [t['logit'] for t in topk]
                    probs = softmax(logits)
                draft_topk = []
                for i,t in enumerate(topk):
                    prob = None
                    if 'prob' in t:
                        prob = t.get('prob')
                    elif probs is not None and i < len(probs):
                        prob = probs[i]
                    draft_topk.append({
                        'id': t.get('id'),
                        'token': t.get('token'),
                        'prob': prob,
                    })
                if 'draft_topk_probs' not in row:
                    row['draft_topk_probs'] = draft_topk
                row.pop('topk', None)
                changed = True
            # think_flag -> is_inside_think
            if 'think_flag' in row:
                if 'is_inside_think' not in row:
                    row['is_inside_think'] = bool(row.get('think_flag'))
                row.pop('think_flag', None)
                changed = True
            # ensure phase_label_hmm
            if 'phase_label_hmm' not in row:
                row['phase_label_hmm'] = None
                changed = True
            # remove accepted_sequence to match P1 (but keep backup)
            if 'accepted_sequence' in row:
                row['_legacy_accepted_sequence'] = row.pop('accepted_sequence')
                changed = True
            out_lines.append(json.dumps(row))
    if changed:
        with open(p, 'w') as fh:
            fh.write('\n'.join(out_lines) + '\n')
        print('Converted', p)
    else:
        print('No change', p)
print('Done')
