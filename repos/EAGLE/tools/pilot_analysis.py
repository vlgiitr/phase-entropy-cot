import json
import os
import math
from collections import defaultdict

import numpy as np


def load_summary(trace_dir):
    path = os.path.join(trace_dir, 'summary.json')
    with open(path) as f:
        return json.load(f)


def parse_trace_row(row):
    def maybe_float(x):
        if x is None:
            return np.nan
        return float(x)

    def maybe_int(x):
        return int(x) if x is not None else np.nan

    return {
            'step': maybe_int(row.get('step')),
            'position': maybe_int(row.get('position')),
            'tree_depth': maybe_int(row.get('tree_depth')),
            'accepted': bool(row.get('accepted')),
            'accept_length': maybe_int(row.get('accept_length')),
            'token_str': row.get('token_str') or row.get('token'),
            'is_inside_think': bool(row.get('is_inside_think') if row.get('is_inside_think') is not None else row.get('think_flag')),
            'draft_top1_prob': maybe_float(row.get('draft_top1_prob') if row.get('draft_top1_prob') is not None else row.get('top1_p')),
            'sample_p_top1': maybe_float(row.get('sample_p_top1')),
        }


def load_trace_rows(trace_dir, summary):
    rows = []
    for entry in summary:
        # skip malformed or missing entries
        if not isinstance(entry, dict):
            continue
        if not entry.get('success'):
            continue
        trace_path = entry.get('trace_file')
        if not trace_path:
            continue
        if not os.path.exists(trace_path):
            # skip missing trace files rather than crash
            print('Warning: missing trace file', trace_path)
            continue
        with open(trace_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                row = parse_trace_row(obj)
                # attach dataset/idx if available
                row['dataset'] = entry.get('dataset') if isinstance(entry.get('dataset'), str) or entry.get('dataset') is not None else None
                row['idx'] = entry.get('idx') if entry.get('idx') is not None else None
                rows.append(row)
    return rows


def compute_stats(rows):
    valid_top1 = [r['draft_top1_prob'] for r in rows if not math.isnan(r['draft_top1_prob'])]
    accepted = [r['accepted'] for r in rows]
    think = [r['is_inside_think'] for r in rows]
    tree_depth = [r['tree_depth'] for r in rows if not math.isnan(r['tree_depth'])]

    details = {
        'token_rows': len(rows),
        'valid_top1_rows': len(valid_top1),
        'draft_top1_prob_mean': float(np.mean(valid_top1)) if valid_top1 else None,
        'draft_top1_prob_std': float(np.std(valid_top1)) if valid_top1 else None,
        'draft_top1_prob_min': float(np.min(valid_top1)) if valid_top1 else None,
        'draft_top1_prob_max': float(np.max(valid_top1)) if valid_top1 else None,
        'accepted_rate': float(np.mean(accepted)),
        'think_rate': float(np.mean(think)),
        'mean_tree_depth': float(np.nanmean(tree_depth)) if tree_depth else None,
    }
    return details


def compute_token_lengths(rows):
    lengths = defaultdict(int)
    for r in rows:
        lengths[(r['dataset'], r['idx'])] += 1
    values = sorted(lengths.values())
    return {
        'min': int(values[0]),
        'max': int(values[-1]),
        'median': float(np.median(values)),
        'count': len(values),
        'tail_low': values[:10],
        'tail_high': values[-10:],
    }


def compute_autocorr(rows, max_lag=5):
    by_trace = defaultdict(list)
    for r in rows:
        by_trace[(r['dataset'], r['idx'])].append(r)

    result = {}
    for lag in range(1, max_lag + 1):
        values = []
        for trace_rows in by_trace.values():
            trace_rows = sorted(trace_rows, key=lambda x: x['step'])
            series = np.array([r['draft_top1_prob'] for r in trace_rows if not math.isnan(r['draft_top1_prob'])])
            if len(series) <= lag:
                continue
            mean = np.mean(series)
            denom = np.sum((series - mean) ** 2)
            if denom == 0:
                continue
            num = np.sum((series[:-lag] - mean) * (series[lag:] - mean))
            values.append(num / denom)
        values = np.array(values)
        result[lag] = {
            'traces': int(len(values)),
            'mean': float(np.mean(values)) if len(values) else None,
            'std': float(np.std(values)) if len(values) else None,
            'min': float(np.min(values)) if len(values) else None,
            'max': float(np.max(values)) if len(values) else None,
        }
    return result


def compute_icc(rows):
    by_trace = defaultdict(list)
    for r in rows:
        by_trace[(r['dataset'], r['idx'])].append(r['draft_top1_prob'])
    groups = [np.array([v for v in vals if not math.isnan(v)]) for vals in by_trace.values()]
    groups = [g for g in groups if len(g) > 1]
    grand = np.concatenate(groups)
    g = len(groups)
    N = len(grand)
    kbar = float(np.mean([len(gp) for gp in groups]))
    mean_grand = np.mean(grand)
    ssb = sum(len(gp) * (np.mean(gp) - mean_grand) ** 2 for gp in groups)
    ssw = sum(np.sum((gp - np.mean(gp)) ** 2) for gp in groups)
    msb = ssb / (g - 1)
    msw = ssw / (N - g)
    icc = (msb - msw) / (msb + (kbar - 1) * msw) if (msb + (kbar - 1) * msw) != 0 else float('nan')
    return {
        'icc1_top1_p': float(icc),
        'groups': int(g),
        'N': int(N),
        'kbar': float(kbar),
    }


def compute_power_estimate(stats, icc, effect_size=0.02, alpha=0.05, target_power=0.8):
    sd = stats.get('draft_top1_prob_std') or stats.get('top1_p_std')
    if sd is None or math.isnan(sd) or sd <= 0:
        return {
            'error': 'invalid_stddev',
            'effect_size': effect_size,
            'alpha': alpha,
            'target_power': target_power,
        }
    z_alpha = 1.96
    z_beta = 0.84
    required_tokens = ((z_alpha + z_beta) * sd / effect_size) ** 2
    kbar = icc.get('kbar', 1.0)
    design_effect = max(1.0, 1.0 + (kbar - 1.0) * icc.get('icc1_top1_p', 0.0))
    estimated_traces = math.ceil(required_tokens / kbar * design_effect) if kbar > 0 else None
    return {
        'effect_size': effect_size,
        'alpha': alpha,
        'target_power': target_power,
        'required_token_rows': float(required_tokens),
        'mean_trace_length': float(kbar),
        'design_effect': float(design_effect),
        'estimated_traces': int(estimated_traces) if estimated_traces is not None else None,
    }


def main():
    trace_dir = os.path.join(os.path.dirname(__file__), '..', 'pilot_traces')
    summary = load_summary(trace_dir)
    rows = load_trace_rows(trace_dir, summary)
    stats = compute_stats(rows)
    lengths = compute_token_lengths(rows)
    autocorr = compute_autocorr(rows)
    icc = compute_icc(rows)
    power_estimate = compute_power_estimate(stats, icc)
    analysis = {
        'trace_count': len([e for e in summary if e.get('success')]),
        'summary_success': sum(1 for e in summary if e.get('success')),
        'summary_fail': sum(1 for e in summary if not e.get('success')),
        'stats': stats,
        'lengths': lengths,
        'autocorr': autocorr,
        'icc': icc,
        'power_estimate': power_estimate,
    }
    out_path = os.path.join(trace_dir, 'analysis.json')
    with open(out_path, 'w') as f:
        json.dump(analysis, f, indent=2)
    print(json.dumps(analysis, indent=2))


if __name__ == '__main__':
    main()
