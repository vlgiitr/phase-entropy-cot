#!/usr/bin/env python3
"""P4.1 step-level sampler invariant check (T=0).

This check is designed as a substitute for blocked row-level selected-path audits.
It verifies step-level consistency of the logged `accept_length` by independently
recomputing it from step-to-step prompt-end-relative position advances:

    recomputed_accept_length = next_position - current_position - 1

Under the T=0 EAGLE verification semantics used for this corpus, each decode step
advances exactly by (accept_length + 1) emitted tokens.

Confirmatory policy:
- Only steps whose backfill row has pq_reconstruction_valid == True are checked.
- Last step in each trace is excluded because there is no next step position.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


ROOT = Path("/root/phase-entropy-cot")


@dataclass
class StepRecord:
    step: int
    position: int
    accept_length: int


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run P4.1 step-level invariant check")
    p.add_argument(
        "--backfill-report-json",
        type=Path,
        default=ROOT / "results" / "p4_1_backfill_pq_report_full_fixedpos.json",
    )
    p.add_argument(
        "--trace-dir",
        type=Path,
        default=ROOT / "corpus" / "v1" / "traces",
    )
    p.add_argument(
        "--summary-json",
        type=Path,
        default=ROOT / "tmp" / "p4_1_summary_full350.json",
        help="Trace summary used for dataset mapping; falls back to corpus/v1/summary.jsonl if missing.",
    )
    p.add_argument(
        "--out-md",
        type=Path,
        default=ROOT / "results" / "p4_1_step_level_invariant_check.md",
    )
    p.add_argument(
        "--top-n",
        type=int,
        default=20,
        help="How many top mismatch clusters to print per section.",
    )
    return p.parse_args()


def _load_jsonl(path: Path) -> List[dict]:
    out: List[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def _load_summary(summary_json: Path) -> List[dict]:
    if summary_json.exists():
        obj = json.loads(summary_json.read_text(encoding="utf-8"))
        if isinstance(obj, list):
            return obj

    # Fallback path if tmp summary is absent.
    summary_jsonl = ROOT / "corpus" / "v1" / "summary.jsonl"
    rows = _load_jsonl(summary_jsonl)
    dedup: List[dict] = []
    seen = set()
    for r in rows:
        if not bool(r.get("success", False)):
            continue
        key = (str(r.get("dataset")), int(r.get("idx", -1)))
        if key in seen:
            continue
        seen.add(key)
        dedup.append(r)
    return dedup


def _pct(n: int, d: int) -> float:
    return (100.0 * n / d) if d > 0 else 0.0


def main() -> None:
    args = parse_args()

    backfill_report = json.loads(args.backfill_report_json.read_text(encoding="utf-8"))
    backfill_dir = Path(str(backfill_report["backfill_dir"]))

    summary = _load_summary(args.summary_json)
    trace_meta: Dict[str, dict] = {Path(str(r["trace_file"])).name: r for r in summary}

    checked = 0
    matches = 0
    mismatches = 0

    skipped_invalid = 0
    skipped_terminal = 0
    missing_trace_files = 0

    signed_delta = Counter()  # recomputed - logged
    abs_delta = Counter()
    mismatch_by_dataset = Counter()
    mismatch_by_trace = Counter()
    mismatch_by_position = Counter()
    mismatch_examples: List[dict] = []

    trace_files = sorted(backfill_dir.glob("*.jsonl"))
    for bf_path in trace_files:
        trace_path = args.trace_dir / bf_path.name
        if not trace_path.exists():
            missing_trace_files += 1
            continue

        trace_rows_raw = _load_jsonl(trace_path)
        back_rows_raw = _load_jsonl(bf_path)

        trace_rows: List[StepRecord] = []
        for row in trace_rows_raw:
            # Guard against non-token rows in trace logs.
            if "step" not in row or "position" not in row:
                continue
            trace_rows.append(
                StepRecord(
                    step=int(row["step"]),
                    position=int(row["position"]),
                    accept_length=int(row.get("accept_length", 0)),
                )
            )

        # Confirmatory filter comes from backfill validity flag.
        valid_by_step: Dict[int, bool] = {}
        for r in back_rows_raw:
            if "step" not in r:
                continue
            valid_by_step[int(r["step"])] = bool(r.get("pq_reconstruction_valid", False))

        dataset = str(trace_meta.get(bf_path.name, {}).get("dataset", "unknown"))

        for i, row in enumerate(trace_rows):
            if i == len(trace_rows) - 1:
                skipped_terminal += 1
                continue

            if not valid_by_step.get(row.step, False):
                skipped_invalid += 1
                continue

            nxt = trace_rows[i + 1]
            recomputed = max(0, int(nxt.position - row.position - 1))
            logged = row.accept_length

            checked += 1
            if recomputed == logged:
                matches += 1
                continue

            mismatches += 1
            d = int(recomputed - logged)
            signed_delta[d] += 1
            abs_delta[abs(d)] += 1
            mismatch_by_dataset[dataset] += 1
            mismatch_by_trace[bf_path.name] += 1
            mismatch_by_position[row.position] += 1

            if len(mismatch_examples) < 50:
                mismatch_examples.append(
                    {
                        "trace_file": bf_path.name,
                        "dataset": dataset,
                        "step": row.step,
                        "position": row.position,
                        "logged_accept_length": logged,
                        "recomputed_accept_length": recomputed,
                        "signed_delta": d,
                    }
                )

    lines: List[str] = []
    lines.append("# P4.1 Step-Level Sampler Invariant Check")
    lines.append("")
    lines.append("## Definition")
    lines.append("For each checked step:")
    lines.append("- logged_accept_length := value logged in trace row")
    lines.append("- recomputed_accept_length := next_position - current_position - 1")
    lines.append("")
    lines.append("Rationale: in T=0 verification, one decode step advances by exactly (accept_length + 1) tokens.")
    lines.append("")
    lines.append("## Scope")
    lines.append(f"- backfill_report: {args.backfill_report_json}")
    lines.append(f"- backfill_dir: {backfill_dir}")
    lines.append(f"- trace_dir: {args.trace_dir}")
    lines.append(f"- summary_source: {args.summary_json if args.summary_json.exists() else ROOT / 'corpus/v1/summary.jsonl'}")
    lines.append("")
    lines.append("Confirmatory filter:")
    lines.append("- include only steps with pq_reconstruction_valid == True")
    lines.append("- exclude terminal step in each trace (no next_position available)")
    lines.append("")
    lines.append("## Results")
    lines.append(f"- traces_seen: {len(trace_files)}")
    lines.append(f"- steps_checked: {checked}")
    lines.append(f"- exact_matches: {matches} ({_pct(matches, checked):.6f}%)")
    lines.append(f"- mismatches: {mismatches} ({_pct(mismatches, checked):.6f}%)")
    lines.append(f"- skipped_invalid_steps: {skipped_invalid}")
    lines.append(f"- skipped_terminal_steps: {skipped_terminal}")
    lines.append(f"- missing_trace_files: {missing_trace_files}")
    lines.append("")

    if mismatches == 0:
        lines.append("## Mismatch Distribution")
        lines.append("- No mismatches observed.")
        lines.append("")
        lines.append("## Clustering")
        lines.append("- dataset clustering: none")
        lines.append("- trace clustering: none")
        lines.append("- position clustering: none")
        lines.append("")
        lines.append("## Verdict")
        lines.append("PASS (empirical corroboration): recomputed and logged accept_length agree on all confirmatory checked steps.")
    else:
        lines.append("## Mismatch Distribution")
        lines.append("### Signed Delta (recomputed - logged)")
        for d, c in signed_delta.most_common():
            direction = "underlogged" if d > 0 else "overlogged"
            lines.append(f"- {d}: {c} ({_pct(c, mismatches):.6f}%) [{direction}]")
        lines.append("")

        lines.append("### Absolute Delta")
        for d, c in abs_delta.most_common():
            lines.append(f"- |delta|={d}: {c} ({_pct(c, mismatches):.6f}%)")
        lines.append("")

        lines.append("## Clustering")
        lines.append("### By Dataset")
        for ds, c in mismatch_by_dataset.most_common(args.top_n):
            lines.append(f"- {ds}: {c} ({_pct(c, mismatches):.6f}%)")
        lines.append("")

        lines.append("### Top Traces")
        for tr, c in mismatch_by_trace.most_common(args.top_n):
            lines.append(f"- {tr}: {c} ({_pct(c, mismatches):.6f}%)")
        lines.append("")

        lines.append("### Top Positions")
        for pos, c in mismatch_by_position.most_common(args.top_n):
            lines.append(f"- position={pos}: {c} ({_pct(c, mismatches):.6f}%)")
        lines.append("")

        lines.append("## Example Mismatches")
        lines.append("| trace_file | dataset | step | position | logged_accept_length | recomputed_accept_length | signed_delta |")
        lines.append("|:--|:--|--:|--:|--:|--:|--:|")
        for ex in mismatch_examples:
            lines.append(
                "| {trace_file} | {dataset} | {step} | {position} | {logged_accept_length} | {recomputed_accept_length} | {signed_delta} |".format(
                    **ex
                )
            )

        lines.append("")
        lines.append("## Verdict")
        lines.append("FAIL: mismatches are not near-zero; inspect patterns above.")

    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "out_md": str(args.out_md),
                "steps_checked": checked,
                "exact_matches": matches,
                "mismatches": mismatches,
                "exact_match_rate_pct": _pct(matches, checked),
                "skipped_invalid_steps": skipped_invalid,
                "skipped_terminal_steps": skipped_terminal,
                "missing_trace_files": missing_trace_files,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
