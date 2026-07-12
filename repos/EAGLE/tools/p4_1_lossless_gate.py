#!/usr/bin/env python3
"""P4.1 losslessness hard-gate runner.

This script executes the five required P4.1 checks and writes a JSON + markdown
report. It intentionally fails closed when required logged fields are missing,
instead of silently approximating confirmatory checks.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
from scipy import stats


PQ_KEYS = {
    "p": ["p", "target_prob", "verifier_prob", "prob_p"],
    "q": ["q", "draft_prob", "proposal_prob", "prob_q"],
}


@dataclass
class CheckResult:
    name: str
    status: str  # pass | fail | blocked
    details: Dict[str, object]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run P4.1 losslessness hard-gate checks")
    parser.add_argument("--workspace-root", type=Path, default=Path("/root/phase-entropy-cot"))
    parser.add_argument("--trace-dir", type=Path, default=Path("/root/phase-entropy-cot/corpus/v1/traces"))
    parser.add_argument("--backfill-dir", type=Path, default=Path("/root/phase-entropy-cot/corpus/v1/backfill_pq"))
    parser.add_argument("--validation-lock", type=Path, default=Path("/root/phase-entropy-cot/splits/validation_locked.json"))
    parser.add_argument("--test-lock", type=Path, default=Path("/root/phase-entropy-cot/splits/test_locked.json"))
    parser.add_argument("--controller-output", type=Path, default=None, help="Optional controller output JSONL for greedy check")
    parser.add_argument("--vanilla-output", type=Path, default=None, help="Optional vanilla AR output JSONL for greedy check")
    parser.add_argument("--batch-audit-jsonl", type=Path, default=None, help="Optional batch>1 audit log for EQSPEC ragged check")
    parser.add_argument("--subset-prompts", type=int, default=40)
    parser.add_argument("--n-min", type=int, default=20)
    parser.add_argument("--require-pq-reconstruction-valid", action="store_true", default=True)
    parser.add_argument("--mc-resamples", type=int, default=200)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--out-json", type=Path, default=Path("/root/phase-entropy-cot/results/p4_1_lossless_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("/root/phase-entropy-cot/results/p4_1_lossless_gate.md"))
    return parser.parse_args()


def load_lock(path: Path) -> List[str]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(obj, dict):
        ids: List[str] = []
        for _, vals in obj.items():
            if isinstance(vals, list):
                ids.extend(str(v) for v in vals)
        return sorted(set(ids))
    if isinstance(obj, list):
        return sorted(set(str(v) for v in obj))
    return []


def iter_rows(trace_paths: Sequence[Path]) -> Iterable[Dict[str, object]]:
    for p in trace_paths:
        with p.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue


def pick_key(row: Dict[str, object], candidates: Sequence[str]) -> Optional[str]:
    for k in candidates:
        if k in row:
            return k
    return None


def safe_float(x: object) -> Optional[float]:
    try:
        v = float(x)
        if math.isfinite(v):
            return v
    except Exception:
        return None
    return None


def holm_adjust(pvals: Dict[int, float], alpha: float) -> Dict[int, Dict[str, object]]:
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    out: Dict[int, Dict[str, object]] = {}
    stop = False
    for i, (pos, p) in enumerate(items, start=1):
        thr = alpha / (m - i + 1)
        passed = (not stop) and (p <= thr)
        if not passed:
            stop = True
        out[pos] = {"p": float(p), "holm_threshold": float(thr), "pass": bool(passed)}
    return out


def tost_equivalence(x: np.ndarray, y: np.ndarray, eps: float, alpha: float) -> Tuple[float, float, bool]:
    d = x - y
    n = d.size
    if n < 2:
        return float("nan"), float("nan"), False
    mean_d = float(np.mean(d))
    sd = float(np.std(d, ddof=1))
    if sd == 0.0:
        left_p = 0.0 if mean_d > -eps else 1.0
        right_p = 0.0 if mean_d < eps else 1.0
        return left_p, right_p, (left_p < alpha and right_p < alpha)
    se = sd / math.sqrt(n)
    t_left = (mean_d + eps) / se
    t_right = (mean_d - eps) / se
    df = n - 1
    left_p = 1.0 - stats.t.cdf(t_left, df=df)
    right_p = stats.t.cdf(t_right, df=df)
    return float(left_p), float(right_p), bool(left_p < alpha and right_p < alpha)


def main() -> None:
    args = parse_args()
    args.out_json.parent.mkdir(parents=True, exist_ok=True)

    val_ids = load_lock(args.validation_lock)
    test_ids = set(load_lock(args.test_lock))

    backfill_paths = sorted(args.backfill_dir.glob("*.jsonl"))
    if not backfill_paths:
        raise FileNotFoundError(f"No jsonl files found in {args.backfill_dir}")

    # Gather rows from validation-only prompt ids.
    val_subset = [pid for pid in val_ids if pid not in test_ids][: args.subset_prompts]
    val_subset_set = set(val_subset)

    rows: List[Dict[str, object]] = []
    for row in iter_rows(backfill_paths):
        pid = str(row.get("problem_id", ""))
        if pid in val_subset_set:
            rows.append(row)

    total_rows_before_filter = len(rows)
    if args.require_pq_reconstruction_valid:
        confirmatory_rows = [r for r in rows if bool(r.get("pq_reconstruction_valid", False))]
        invalid_rows = [r for r in rows if not bool(r.get("pq_reconstruction_valid", False))]
    else:
        confirmatory_rows = list(rows)
        invalid_rows = []

    excluded_invalid_per_position: Dict[int, int] = {}
    confirmatory_per_position: Dict[int, int] = {}
    for r in invalid_rows:
        if "position" in r:
            pos = int(r["position"])
            excluded_invalid_per_position[pos] = excluded_invalid_per_position.get(pos, 0) + 1
    for r in confirmatory_rows:
        if "position" in r:
            pos = int(r["position"])
            confirmatory_per_position[pos] = confirmatory_per_position.get(pos, 0) + 1

    positions_meeting_n_min = {
        int(pos): cnt for pos, cnt in confirmatory_per_position.items() if cnt >= args.n_min
    }

    checks: List[CheckResult] = []

    # Check 2: sampler invariant against logged (p, q) and acceptance.
    p_key = pick_key(confirmatory_rows[0], PQ_KEYS["p"]) if confirmatory_rows else None
    q_key = pick_key(confirmatory_rows[0], PQ_KEYS["q"]) if confirmatory_rows else None

    if not confirmatory_rows:
        checks.append(CheckResult("sampler_invariant", "fail", {"reason": "no validation rows"}))
    elif p_key is None or q_key is None:
        checks.append(
            CheckResult(
                "sampler_invariant",
                "fail",
                {
                    "reason": "missing_logged_pq",
                    "found_keys": sorted(confirmatory_rows[0].keys()),
                    "required_any_p": PQ_KEYS["p"],
                    "required_any_q": PQ_KEYS["q"],
                    "rows_before_filter": total_rows_before_filter,
                    "rows_excluded_invalid": len(invalid_rows),
                    "rows_confirmatory": len(confirmatory_rows),
                },
            )
        )
    else:
        deterministic_violations = 0
        valid = 0
        for r in confirmatory_rows:
            p = safe_float(r.get(p_key))
            q = safe_float(r.get(q_key))
            a = bool(r.get("accepted", False))
            if p is None or q is None or q <= 0:
                continue
            valid += 1
            if p >= q and (not a):
                deterministic_violations += 1
        checks.append(
            CheckResult(
                "sampler_invariant",
                "pass" if deterministic_violations == 0 and valid > 0 else "fail",
                {
                    "rows_checked": valid,
                    "deterministic_region_violations": deterministic_violations,
                    "p_key": p_key,
                    "q_key": q_key,
                    "rows_before_filter": total_rows_before_filter,
                    "rows_excluded_invalid": len(invalid_rows),
                    "rows_confirmatory": len(confirmatory_rows),
                    "n_min": args.n_min,
                    "positions_meeting_n_min_after_filter": len(positions_meeting_n_min),
                },
            )
        )

    # Check 3+4: TOST + Holm across positions.
    # Confirmatory only if both controller and vanilla have p/q.
    tost_status = "fail"
    tost_details: Dict[str, object] = {
        "alpha": args.alpha,
        "mc_resamples": args.mc_resamples,
        "subset_prompts": len(val_subset),
        "preregistered_margin_source": "LOSSLESS_TOST_PREREG.md",
        "rows_before_filter": total_rows_before_filter,
        "rows_excluded_invalid": len(invalid_rows),
        "rows_confirmatory": len(confirmatory_rows),
        "confirmatory_filter": "pq_reconstruction_valid == True",
        "n_min": args.n_min,
        "positions_meeting_n_min_after_filter": len(positions_meeting_n_min),
        "excluded_invalid_per_position": {str(k): v for k, v in sorted(excluded_invalid_per_position.items())},
    }

    if p_key is None or q_key is None:
        tost_details["reason"] = "missing_logged_pq"
        checks.append(CheckResult("tost_distribution_equivalence", tost_status, tost_details))
        checks.append(CheckResult("holm_fwer_positions", "fail", {"reason": "tost_not_runnable"}))
    else:
        # Placeholder path for future use when both methods are available.
        checks.append(CheckResult("tost_distribution_equivalence", "fail", {**tost_details, "reason": "controller_vs_vanilla_pair_not_provided"}))
        checks.append(CheckResult("holm_fwer_positions", "fail", {"reason": "no_per_position_tost_pvalues"}))

    # Check 5: Greedy equality at T=0.
    if args.controller_output is None or args.vanilla_output is None:
        checks.append(
            CheckResult(
                "greedy_token_identity_t0",
                "fail",
                {"reason": "missing_controller_or_vanilla_outputs", "controller_output": str(args.controller_output), "vanilla_output": str(args.vanilla_output)},
            )
        )
    else:
        checks.append(CheckResult("greedy_token_identity_t0", "fail", {"reason": "not_implemented_for_this_artifact_format"}))

    # Check 6: EQSPEC-style ragged desync at batch>1.
    if args.batch_audit_jsonl is None:
        checks.append(CheckResult("eqspec_ragged_desync_batch_gt_1", "fail", {"reason": "missing_batch_audit_jsonl", "target_match_rate": 0.999}))
    else:
        checks.append(CheckResult("eqspec_ragged_desync_batch_gt_1", "fail", {"reason": "not_implemented_for_this_artifact_format"}))

    all_pass = all(c.status == "pass" for c in checks)

    payload = {
        "phase": "P4.1",
        "status": "pass" if all_pass else "fail",
        "notes": [
            "This gate fails closed when confirmatory artifacts are missing.",
            "Validation split only; test split intentionally untouched.",
            "Confirmatory order: pq_reconstruction_valid filter is applied first, then n_min thresholding is evaluated on surviving rows.",
        ],
        "validation_subset_problem_ids": val_subset,
        "rows_before_filter": total_rows_before_filter,
        "rows_excluded_invalid": len(invalid_rows),
        "rows_confirmatory": len(confirmatory_rows),
        "n_min": args.n_min,
        "positions_meeting_n_min_after_filter": len(positions_meeting_n_min),
        "excluded_invalid_per_position": {str(k): v for k, v in sorted(excluded_invalid_per_position.items())},
        "checks": [
            {"name": c.name, "status": c.status, "details": c.details}
            for c in checks
        ],
    }

    args.out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    lines = [
        "# P4.1 Losslessness Gate Report",
        "",
        f"Overall status: **{payload['status'].upper()}**",
        "",
        "## Checks",
    ]
    for c in checks:
        lines.append(f"- {c.name}: {c.status}")
        reason = c.details.get("reason") if isinstance(c.details, dict) else None
        if reason:
            lines.append(f"  - reason: {reason}")
    lines.append("")
    lines.append("Validation-only execution completed; locked test split was not loaded.")
    args.out_md.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({"status": payload["status"], "out_json": str(args.out_json), "out_md": str(args.out_md)}, indent=2))


if __name__ == "__main__":
    main()
