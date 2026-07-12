#!/usr/bin/env python3
"""P4.1 sampler invariant check (corrected for T=0 greedy verification).

This replaces the previous mis-specified stochastic min(1, p/q) check.
For T=0 in this EAGLE path, verification is deterministic prefix argmax matching.
We audit row-level agreement between:
  criterion = (draft_argmax_id == target_argmax_id)
and logged row outcome:
  accepted (bool)
on confirmatory rows only (pq_reconstruction_valid == True).
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass
class AuditRow:
    trace_file: str
    row_index: int
    run_id: str
    problem_id: str
    step: int | None
    position: int | None
    accepted: bool
    criterion_argmax_match: bool
    target_top1_id: int | None
    draft_top1_id: int | None


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="P4.1 T=0 greedy sampler invariant audit")
    p.add_argument(
        "--backfill-dir",
        type=Path,
        default=Path("/root/phase-entropy-cot/tmp/p4_1_backfill_full"),
    )
    p.add_argument(
        "--trace-dir",
        type=Path,
        default=Path("/root/phase-entropy-cot/corpus/v1/traces"),
    )
    p.add_argument(
        "--out-md",
        type=Path,
        default=Path("/root/phase-entropy-cot/results/p4_1_sampler_invariant_check.md"),
    )
    p.add_argument("--max-anomalies", type=int, default=200)
    return p.parse_args()


def load_token_rows(path: Path) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if "token_id" in row:
                out.append(row)
    return out


def top1_id_from_draft_topk(row: Dict[str, object]) -> int | None:
    topk = row.get("draft_topk_probs")
    if not isinstance(topk, list) or not topk:
        return None
    first = topk[0]
    if not isinstance(first, dict):
        return None
    tok = first.get("id")
    try:
        return int(tok)
    except Exception:
        return None


def run_audit(backfill_dir: Path, trace_dir: Path) -> Tuple[Dict[str, object], List[AuditRow]]:
    backfill_files = sorted(backfill_dir.glob("*.jsonl"))
    if not backfill_files:
        raise FileNotFoundError(f"No jsonl files found in {backfill_dir}")

    total_rows = 0
    confirmatory_rows = 0
    rows_with_complete_ids = 0
    accepted_true = 0
    accepted_false = 0

    criterion_true = 0
    criterion_false = 0

    agree_rows = 0
    disagree_rows = 0

    missing_trace_row = 0
    missing_target_top1 = 0
    missing_draft_top1 = 0

    anomalies: List[AuditRow] = []

    for bf_path in backfill_files:
        trace_path = trace_dir / bf_path.name
        if not trace_path.exists():
            continue

        trace_rows = load_token_rows(trace_path)

        row_index = 0
        with bf_path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                total_rows += 1
                try:
                    b_row = json.loads(line)
                except json.JSONDecodeError:
                    row_index += 1
                    continue

                if not bool(b_row.get("pq_reconstruction_valid", False)):
                    row_index += 1
                    continue

                confirmatory_rows += 1

                if row_index >= len(trace_rows):
                    missing_trace_row += 1
                    row_index += 1
                    continue

                t_row = trace_rows[row_index]
                row_index += 1

                accepted = bool(t_row.get("accepted", False))
                if accepted:
                    accepted_true += 1
                else:
                    accepted_false += 1

                target_top1_id = None
                tok = t_row.get("token_id")
                try:
                    target_top1_id = int(tok)
                except Exception:
                    missing_target_top1 += 1

                draft_top1_id = top1_id_from_draft_topk(t_row)
                if draft_top1_id is None:
                    missing_draft_top1 += 1

                if target_top1_id is None or draft_top1_id is None:
                    continue

                rows_with_complete_ids += 1

                criterion = draft_top1_id == target_top1_id
                if criterion:
                    criterion_true += 1
                else:
                    criterion_false += 1

                if accepted == criterion:
                    agree_rows += 1
                else:
                    disagree_rows += 1
                    anomalies.append(
                        AuditRow(
                            trace_file=bf_path.name,
                            row_index=row_index - 1,
                            run_id=str(t_row.get("run_id", "")),
                            problem_id=str(t_row.get("problem_id", "")),
                            step=int(t_row.get("step")) if t_row.get("step") is not None else None,
                            position=int(t_row.get("position")) if t_row.get("position") is not None else None,
                            accepted=accepted,
                            criterion_argmax_match=criterion,
                            target_top1_id=target_top1_id,
                            draft_top1_id=draft_top1_id,
                        )
                    )

    agreement_rate = (agree_rows / rows_with_complete_ids) if rows_with_complete_ids > 0 else 0.0

    summary: Dict[str, object] = {
        "backfill_dir": str(backfill_dir),
        "trace_dir": str(trace_dir),
        "total_rows": total_rows,
        "confirmatory_rows": confirmatory_rows,
        "rows_with_complete_ids": rows_with_complete_ids,
        "accepted_true": accepted_true,
        "accepted_false": accepted_false,
        "criterion_argmax_match_true": criterion_true,
        "criterion_argmax_match_false": criterion_false,
        "agreement_rows": agree_rows,
        "disagreement_rows": disagree_rows,
        "agreement_rate": agreement_rate,
        "missing_trace_row": missing_trace_row,
        "missing_target_top1": missing_target_top1,
        "missing_draft_top1": missing_draft_top1,
    }
    return summary, anomalies


def write_markdown(out_md: Path, summary: Dict[str, object], anomalies: List[AuditRow], max_anomalies: int) -> None:
    out_md.parent.mkdir(parents=True, exist_ok=True)

    lines: List[str] = []
    lines.append("# P4.1 Sampler Invariant Check (Corrected T=0 Formulation)")
    lines.append("")
    lines.append("This report replaces the prior mis-specified stochastic check using min(1, p/q).")
    lines.append("For this corpus (T=0), the invariant audited here is deterministic argmax-equivalence:")
    lines.append("- criterion_argmax_match = (draft_argmax_id == target_argmax_id)")
    lines.append("- expected row outcome: accepted == criterion_argmax_match")
    lines.append("")

    verdict = "PASS" if int(summary["disagreement_rows"]) == 0 else "FAIL"
    lines.append(f"Overall verdict: **{verdict}**")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- backfill_dir: {summary['backfill_dir']}")
    lines.append(f"- trace_dir: {summary['trace_dir']}")
    lines.append(f"- total_rows_scanned: {summary['total_rows']}")
    lines.append(f"- confirmatory_rows: {summary['confirmatory_rows']}")
    lines.append(f"- rows_with_complete_argmax_ids: {summary['rows_with_complete_ids']}")
    lines.append(f"- accepted_true: {summary['accepted_true']}")
    lines.append(f"- accepted_false: {summary['accepted_false']}")
    lines.append(f"- criterion_argmax_match_true: {summary['criterion_argmax_match_true']}")
    lines.append(f"- criterion_argmax_match_false: {summary['criterion_argmax_match_false']}")
    lines.append(f"- agreement_rows: {summary['agreement_rows']}")
    lines.append(f"- disagreement_rows: {summary['disagreement_rows']}")
    lines.append(f"- exact_agreement_rate: {float(summary['agreement_rate']):.6f}")
    lines.append(f"- missing_trace_row: {summary['missing_trace_row']}")
    lines.append(f"- missing_target_top1: {summary['missing_target_top1']}")
    lines.append(f"- missing_draft_top1: {summary['missing_draft_top1']}")
    lines.append("")

    lines.append("## Real Anomalies (accepted disagrees with argmax-match criterion)")
    lines.append(f"Showing up to {max_anomalies} rows.")
    lines.append("")
    lines.append("| trace_file | row_index | run_id | problem_id | step | position | accepted | criterion_argmax_match | target_top1_id | draft_top1_id |")
    lines.append("|:--|--:|:--|:--|--:|--:|:--:|:--:|--:|--:|")
    for a in anomalies[:max_anomalies]:
        step_val = "" if a.step is None else str(a.step)
        pos_val = "" if a.position is None else str(a.position)
        tgt_val = "" if a.target_top1_id is None else str(a.target_top1_id)
        dr_val = "" if a.draft_top1_id is None else str(a.draft_top1_id)
        lines.append(
            f"| {a.trace_file} | {a.row_index} | {a.run_id} | {a.problem_id} | {step_val} | {pos_val} | {a.accepted} | {a.criterion_argmax_match} | {tgt_val} | {dr_val} |"
        )

    out_md.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    summary, anomalies = run_audit(args.backfill_dir, args.trace_dir)
    write_markdown(args.out_md, summary, anomalies, args.max_anomalies)
    print(
        json.dumps(
            {
                "status": "ok",
                "out_md": str(args.out_md),
                **summary,
                "anomalies_reported": min(len(anomalies), args.max_anomalies),
                "anomalies_total": len(anomalies),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
