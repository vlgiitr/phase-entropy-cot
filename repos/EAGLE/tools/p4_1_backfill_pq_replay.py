#!/usr/bin/env python3
"""P4.1 step 1: additive p/q backfill via deterministic teacher-forced scoring.

For each frozen trace, this script reconstructs a fixed token sequence:

prompt_token_ids + logged_trace_token_ids

It then computes:
- p: target model probability of each logged next token (teacher forcing)
- q: draft model probability of that same logged token on the same fixed prefix

No decoding, sampling, rejection, or EaModel generation loop is used.
Existing frozen trace files are never modified.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

import torch
import torch.nn.functional as F


ROOT = Path("/root/phase-entropy-cot")
REPO_ROOT = ROOT / "repos" / "EAGLE"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from eagle.model.ea_model import EaModel  # noqa: E402


# Explicit float tolerance for validity checks in exclude-and-disclose mode.
PQ_RECONSTRUCTION_TOLERANCE = 1e-6


OVERWRITE_PATTERNS = [
    re.compile(r"\bq\s*=\s*.*draft_top1_prob"),
    re.compile(r"\bdraft_top1_prob\s*=\s*.*\bq\b"),
    re.compile(r'"q"\s*:\s*.*draft_top1_prob'),
    re.compile(r'"draft_top1_prob"\s*:\s*.*\bq\b'),
]


def assert_no_q_top1_overwrite(workspace_root: Path) -> None:
    violations: List[Dict[str, object]] = []
    for py_path in workspace_root.rglob("*.py"):
        parts = py_path.parts
        if ".venv" in parts or "site-packages" in parts:
            continue
        try:
            text = py_path.read_text(encoding="utf-8")
        except Exception:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pattern in OVERWRITE_PATTERNS:
                if pattern.search(line):
                    violations.append(
                        {
                            "file": str(py_path),
                            "line": line_no,
                            "text": line.strip(),
                        }
                    )

    if violations:
        raise RuntimeError(
            "Potential q<->draft_top1 overwrite paths detected; review before continuing:\n"
            + json.dumps(violations[:50], indent=2)
        )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Teacher-forced p/q backfill on frozen traces")
    p.add_argument("--root", type=Path, default=ROOT)
    p.add_argument("--summary", type=Path, default=ROOT / "corpus" / "v1" / "summary.json")
    p.add_argument("--trace-dir", type=Path, default=ROOT / "corpus" / "v1" / "traces")
    p.add_argument("--backfill-dir", type=Path, default=ROOT / "corpus" / "v1" / "backfill_pq")
    p.add_argument("--report-json", type=Path, default=ROOT / "results" / "p4_1_backfill_pq_report.json")
    p.add_argument("--report-md", type=Path, default=ROOT / "results" / "p4_1_backfill_pq_report.md")
    p.add_argument(
        "--flags-report-md",
        type=Path,
        default=ROOT / "results" / "p4_1_pq_reconstruction_flags.md",
        help="Disclosure report for rows flagged invalid by pq reconstruction checks.",
    )
    p.add_argument("--max-traces", type=int, default=None, help="Optional debug cap")
    p.add_argument(
        "--only-trace-name",
        type=str,
        default=None,
        help="Optional exact trace filename filter (e.g., trace_livecodebench_108.jsonl)",
    )
    return p.parse_args()


def load_jsonl(path: Path, n: int | None = None) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    if not path.exists():
        return out
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if n is not None and i >= n:
                break
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def load_arrow_rows(dirpath: Path, n: int | None = None) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    if not dirpath.exists():
        return out
    try:
        import pyarrow as pa
    except Exception:
        return out

    files = sorted([p for p in dirpath.rglob("*.arrow") if p.is_file()])
    for f in files:
        try:
            try:
                reader = pa.ipc.open_file(str(f))
            except Exception:
                reader = pa.ipc.open_stream(str(f))
            with reader:
                table = reader.read_all()
                cols = table.to_pydict()
                keys = list(cols.keys())
                length = len(cols[keys[0]]) if keys else 0
                for i in range(length):
                    if n is not None and len(out) >= n:
                        return out
                    out.append({k: cols[k][i] for k in keys})
        except Exception:
            continue
        if n is not None and len(out) >= n:
            break
    return out


def sample_to_text(obj: Dict[str, object] | str) -> str:
    if isinstance(obj, str):
        return obj
    if not isinstance(obj, dict):
        return json.dumps(obj)
    for key in ["question", "problem", "input", "prompt", "text"]:
        val = obj.get(key)
        if val:
            return str(val)
    if obj.get("question_content") or obj.get("question_title"):
        parts: List[str] = []
        if obj.get("question_title"):
            parts.append(str(obj["question_title"]))
        if obj.get("question_content"):
            parts.append(str(obj["question_content"]))
        if obj.get("starter_code"):
            parts.append(str(obj["starter_code"]))
        if obj.get("public_test_cases"):
            parts.append("public_test_cases: " + str(obj["public_test_cases"]))
        return "\n\n".join(parts).strip()
    return json.dumps(obj)


def load_dataset_samples(root: Path) -> Dict[str, List[Dict[str, object]]]:
    data_dir = root / "data"

    math_jsonl = data_dir / "math500" / "test.jsonl"
    lcb_jsonl = data_dir / "livecodebench" / "test.jsonl"

    if math_jsonl.exists():
        math_samples = load_jsonl(math_jsonl)
    else:
        math_samples = load_arrow_rows(data_dir / "math500")

    if lcb_jsonl.exists():
        lcb_samples = load_jsonl(lcb_jsonl)
    else:
        # Support either data/livecodebench/test/*.arrow or data/livecodebench/*.arrow
        lcb_test_dir = data_dir / "livecodebench" / "test"
        if lcb_test_dir.exists():
            lcb_samples = load_arrow_rows(lcb_test_dir)
        else:
            lcb_samples = load_arrow_rows(data_dir / "livecodebench")

    return {
        "math500": math_samples,
        "livecodebench": lcb_samples,
    }


def token_rows_from_trace(path: Path) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if "token_id" in row:
                out.append(row)
    return out


def build_target_to_draft_index(model: EaModel, device: torch.device) -> Dict[int, torch.Tensor]:
    if not hasattr(model.ea_layer, "d2t"):
        return {}
    d2t = model.ea_layer.d2t.detach().to(device=device, dtype=torch.long)
    target_to_draft: Dict[int, List[int]] = {}
    # In EAGLE-3, d2t is an offset tensor, so target_id = draft_idx + d2t[draft_idx].
    for d_idx, t_off in enumerate(d2t.tolist()):
        target_to_draft.setdefault(int(d_idx + t_off), []).append(d_idx)
    return {
        t_idx: torch.tensor(d_idxs, dtype=torch.long, device=device)
        for t_idx, d_idxs in target_to_draft.items()
    }


def score_trace_teacher_forced(
    model: EaModel,
    prompt: str,
    trace_rows: List[Dict[str, object]],
    run_id: str,
    problem_id: str,
) -> List[Dict[str, object]]:
    tokenizer = model.tokenizer
    device = next(model.base_model.parameters()).device

    tokenized = tokenizer(
        prompt,
        return_tensors="pt",
        add_special_tokens=True,
        truncation=False,
    )
    prompt_ids = tokenized.input_ids.to(device)
    prompt_len = int(prompt_ids.shape[1])

    logged_token_ids = torch.tensor(
        [int(r["token_id"]) for r in trace_rows], dtype=torch.long, device=device
    )[None, :]

    full_ids = torch.cat([prompt_ids, logged_token_ids], dim=1)
    if full_ids.shape[1] < 2:
        return []

    with torch.inference_mode():
        outputs, orig, hidden_states = model(input_ids=full_ids, output_orig=True)
        target_log_probs = F.log_softmax(orig[:, :-1, :].float(), dim=-1)

        next_ids = full_ids[:, 1:]
        target_selected_logp = target_log_probs.gather(dim=-1, index=next_ids.unsqueeze(-1)).squeeze(-1)

        if model.use_eagle3:
            if outputs["hidden_states"][0].device != model.ea_layer.lm_head.weight.device:
                outputs["hidden_states"] = [x.to(model.ea_layer.lm_head.weight.device) for x in outputs["hidden_states"]]
            hidden_for_draft = torch.cat(outputs["hidden_states"], dim=-1)
        else:
            hidden_for_draft = hidden_states

        draft_hidden = model.ea_layer(
            hidden_states=hidden_for_draft[:, :-1, :],
            input_ids=full_ids[:, 1:],
            use_cache=False,
        )
        draft_logits = model.ea_layer.lm_head(model.ea_layer.norm(draft_hidden)).float()
        draft_log_probs = F.log_softmax(draft_logits, dim=-1)

    draft_vocab_size = int(draft_log_probs.shape[-1])
    target_vocab_size = int(target_log_probs.shape[-1])
    same_vocab = draft_vocab_size == target_vocab_size

    target_to_draft = build_target_to_draft_index(model, device) if not same_vocab else {}

    out_rows: List[Dict[str, object]] = []
    for i, src_row in enumerate(trace_rows):
        seq_idx = prompt_len + i - 1
        if seq_idx < 0 or seq_idx >= target_selected_logp.shape[1]:
            continue

        tok_id = int(src_row["token_id"])
        p_val = float(torch.exp(target_selected_logp[0, seq_idx]).item())

        if same_vocab:
            q_logp = draft_log_probs[0, seq_idx, tok_id]
            q_val = float(torch.exp(q_logp).item())
        else:
            draft_indices = target_to_draft.get(tok_id)
            if draft_indices is None or draft_indices.numel() == 0:
                q_val = 0.0
            else:
                q_logp = torch.logsumexp(draft_log_probs[0, seq_idx, draft_indices], dim=0)
                q_val = float(torch.exp(q_logp).item())

        live_draft_top1 = src_row.get("draft_top1_prob")
        live_draft_top1_val = float(live_draft_top1) if live_draft_top1 is not None else None
        reconstruction_check_applied = live_draft_top1_val is not None
        pq_reconstruction_valid = False
        pq_reconstruction_violation = None
        lossless_exclusion_reason = None

        prev_accepted = bool(trace_rows[i - 1].get("accepted", False)) if i > 0 else None
        post_rejection_row = prev_accepted is False

        if reconstruction_check_applied:
            pq_reconstruction_violation = max(0.0, q_val - live_draft_top1_val)
            pq_reconstruction_valid = q_val <= (live_draft_top1_val + PQ_RECONSTRUCTION_TOLERANCE)
            if not pq_reconstruction_valid:
                lossless_exclusion_reason = "q_exceeds_live_draft_top1"
        else:
            lossless_exclusion_reason = "missing_live_draft_top1"

        # Canonicalize position to prompt-end-relative indexing.
        # Prefer logged step (already relative), then fallback to position, then local i.
        position_rel = int(src_row.get("step", src_row.get("position", i)))

        out_rows.append(
            {
                "run_id": src_row.get("run_id", run_id),
                "problem_id": src_row.get("problem_id", problem_id),
                "step": src_row.get("step"),
            "position": position_rel,
                "token_id": tok_id,
                "p": p_val,
                "q": q_val,
                "target_token_prob": p_val,
                "draft_token_prob": q_val,
                "draft_top1_prob_live": live_draft_top1_val,
                "reconstruction_check_applied": reconstruction_check_applied,
                "pq_reconstruction_tolerance": PQ_RECONSTRUCTION_TOLERANCE,
                "pq_reconstruction_valid": pq_reconstruction_valid,
                "pq_reconstruction_violation": pq_reconstruction_violation,
                "lossless_excluded": not pq_reconstruction_valid,
                "lossless_exclusion_reason": lossless_exclusion_reason,
                "post_rejection_row": post_rejection_row,
            }
        )

    return out_rows


def main() -> None:
    args = parse_args()
    assert_no_q_top1_overwrite(args.root)
    args.backfill_dir.mkdir(parents=True, exist_ok=True)
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.flags_report_md.parent.mkdir(parents=True, exist_ok=True)

    summary = json.loads(args.summary.read_text(encoding="utf-8"))
    if not isinstance(summary, list):
        raise RuntimeError("summary.json must be a list")
    if args.max_traces is not None:
        summary = summary[: args.max_traces]

    samples = load_dataset_samples(args.root)
    if not samples["math500"] or not samples["livecodebench"]:
        raise RuntimeError(
            f"Missing dataset samples. math500={len(samples['math500'])}, "
            f"livecodebench={len(samples['livecodebench'])}"
        )

    base_model = args.root / "models" / "llama8b"
    ea_model = args.root / "models" / "eagle3-llama"

    model = EaModel.from_pretrained(
        use_eagle3=True,
        base_model_path=str(base_model),
        ea_model_path=str(ea_model),
        total_token=20,
        depth=3,
        top_k=8,
        device_map="auto",
        low_cpu_mem_usage=True,
        torch_dtype=torch.float16,
    )
    processed = 0
    scored_rows_total = 0
    reconstruction_check_rows = 0
    pq_invalid_rows = 0
    max_reconstruction_error_gap = 0.0
    max_reconstruction_error_example: Dict[str, object] | None = None
    flagged_rows: List[Dict[str, object]] = []
    rows_by_dataset: Dict[str, int] = {}
    invalid_by_dataset: Dict[str, int] = {}
    rows_by_type = {"post_rejection": 0, "normal": 0}
    invalid_by_type = {"post_rejection": 0, "normal": 0}
    rows_by_position: Dict[int, int] = {}
    invalid_by_position: Dict[int, int] = {}
    min_p = 1.0
    max_p = 0.0
    min_q = 1.0
    max_q = 0.0

    for row in summary:
        if not row.get("success", False):
            continue
        dataset = str(row["dataset"])
        idx = int(row["idx"])
        problem_id = str(row["problem_id"])
        trace_file = Path(str(row["trace_file"]))
        if not trace_file.exists():
            trace_file = args.trace_dir / trace_file.name

        if args.only_trace_name is not None and trace_file.name != args.only_trace_name:
            continue

        dataset_samples = samples.get(dataset)
        if dataset_samples is None or idx >= len(dataset_samples):
            raise RuntimeError(f"Sample missing for dataset={dataset} idx={idx}")

        sample_obj = dataset_samples[idx]
        prompt = sample_to_text(sample_obj)

        trace_rows = token_rows_from_trace(trace_file)
        if not trace_rows:
            continue

        scored_rows = score_trace_teacher_forced(
            model=model,
            prompt=prompt,
            trace_rows=trace_rows,
            run_id=f"{dataset}_{idx}",
            problem_id=problem_id,
        )

        if not scored_rows:
            continue

        for r in scored_rows:
            p_val = float(r["p"])
            q_val = float(r["q"])
            pos = int(r.get("position", -1))
            min_p = min(min_p, p_val)
            max_p = max(max_p, p_val)
            min_q = min(min_q, q_val)
            max_q = max(max_q, q_val)

            if bool(r.get("reconstruction_check_applied", False)):
                reconstruction_check_rows += 1
            rows_by_dataset[dataset] = rows_by_dataset.get(dataset, 0) + 1
            row_type = "post_rejection" if bool(r.get("post_rejection_row", False)) else "normal"
            rows_by_type[row_type] += 1
            if pos >= 0:
                rows_by_position[pos] = rows_by_position.get(pos, 0) + 1

            if not bool(r.get("pq_reconstruction_valid", False)):
                pq_invalid_rows += 1
                invalid_by_dataset[dataset] = invalid_by_dataset.get(dataset, 0) + 1
                invalid_by_type[row_type] += 1
                if pos >= 0:
                    invalid_by_position[pos] = invalid_by_position.get(pos, 0) + 1

                gap = float(r.get("pq_reconstruction_violation", 0.0) or 0.0)
                if gap > max_reconstruction_error_gap:
                    max_reconstruction_error_gap = gap
                    max_reconstruction_error_example = {
                        "trace_file": trace_file.name,
                        "step": r.get("step"),
                        "position": r.get("position"),
                        "token_id": r.get("token_id"),
                        "q": r.get("q"),
                        "draft_top1_prob_live": r.get("draft_top1_prob_live"),
                        "violation_magnitude": gap,
                    }

                flagged_rows.append(
                    {
                        "trace_id": trace_file.name,
                        "dataset": dataset,
                        "step": r.get("step"),
                        "position": r.get("position"),
                        "token_id": r.get("token_id"),
                        "q": r.get("q"),
                        "draft_top1_prob": r.get("draft_top1_prob_live"),
                        "violation_magnitude": gap,
                        "post_rejection_row": bool(r.get("post_rejection_row", False)),
                    }
                )

        scored_rows_total += len(scored_rows)
        processed += 1

        out_path = args.backfill_dir / trace_file.name
        with out_path.open("w", encoding="utf-8") as out:
            for r in scored_rows:
                out_row = {
                    "run_id": r.get("run_id"),
                    "problem_id": r.get("problem_id"),
                    "step": r.get("step"),
                    "position": r.get("position"),
                    "token_id": r.get("token_id"),
                    "p": r.get("p"),
                    "q": r.get("q"),
                    "target_token_prob": r.get("target_token_prob"),
                    "draft_token_prob": r.get("draft_token_prob"),
                    "draft_top1_prob_live": r.get("draft_top1_prob_live"),
                    "reconstruction_check_applied": r.get("reconstruction_check_applied"),
                    "pq_reconstruction_tolerance": r.get("pq_reconstruction_tolerance"),
                    "pq_reconstruction_valid": r.get("pq_reconstruction_valid"),
                    "pq_reconstruction_violation": r.get("pq_reconstruction_violation"),
                    "lossless_excluded": r.get("lossless_excluded"),
                    "lossless_exclusion_reason": r.get("lossless_exclusion_reason"),
                    "post_rejection_row": r.get("post_rejection_row"),
                }
                out.write(json.dumps(out_row) + "\n")

    if processed == 0:
        report = {
            "status": "no_traces_processed",
            "processed_traces": 0,
            "total_traces_target": len(summary),
            "filter_only_trace_name": args.only_trace_name,
        }
        args.report_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
        args.report_md.write_text(
            "\n".join(
                [
                    "# P4.1 Backfill Replay Report",
                    "",
                    "Status: NO_TRACES_PROCESSED",
                    "",
                    f"Trace filter: {args.only_trace_name}",
                ]
            ),
            encoding="utf-8",
        )
        print(json.dumps(report, indent=2))
        return

    in_range = (0.0 <= min_p <= 1.0) and (0.0 <= max_p <= 1.0) and (0.0 <= min_q <= 1.0) and (0.0 <= max_q <= 1.0)
    lossless_eligible_rows = scored_rows_total - pq_invalid_rows
    invalid_by_dataset_report = {
        ds: {
            "rows": rows_by_dataset.get(ds, 0),
            "invalid_rows": invalid_by_dataset.get(ds, 0),
            "invalid_pct": (
                (100.0 * invalid_by_dataset.get(ds, 0) / rows_by_dataset.get(ds, 0))
                if rows_by_dataset.get(ds, 0) > 0
                else None
            ),
        }
        for ds in sorted(rows_by_dataset)
    }
    invalid_by_type_report = {
        row_type: {
            "rows": rows_by_type[row_type],
            "invalid_rows": invalid_by_type[row_type],
            "invalid_pct": (
                (100.0 * invalid_by_type[row_type] / rows_by_type[row_type])
                if rows_by_type[row_type] > 0
                else None
            ),
        }
        for row_type in ["post_rejection", "normal"]
    }
    invalid_by_position_report = {
        str(pos): {
            "rows": rows_by_position.get(pos, 0),
            "invalid_rows": invalid_by_position.get(pos, 0),
            "invalid_pct": (
                (100.0 * invalid_by_position.get(pos, 0) / rows_by_position.get(pos, 0))
                if rows_by_position.get(pos, 0) > 0
                else None
            ),
        }
        for pos in sorted(rows_by_position)
    }
    report = {
        "status": "ok",
        "processed_traces": processed,
        "total_traces_target": len(summary),
        "scored_rows": scored_rows_total,
        "lossless_eligible_rows": lossless_eligible_rows,
        "reconstruction_check_rows": reconstruction_check_rows,
        "pq_reconstruction_tolerance": PQ_RECONSTRUCTION_TOLERANCE,
        "pq_reconstruction_invalid_rows": pq_invalid_rows,
        "reconstruction_error_rate_checked": (
            (pq_invalid_rows / reconstruction_check_rows) if reconstruction_check_rows > 0 else None
        ),
        "max_reconstruction_error_gap": max_reconstruction_error_gap,
        "max_reconstruction_error_example": max_reconstruction_error_example,
        "invalid_breakdown_by_dataset": invalid_by_dataset_report,
        "invalid_breakdown_by_row_type": invalid_by_type_report,
        "invalid_breakdown_by_position": invalid_by_position_report,
        "no_q_top1_overwrite_assertion": "passed",
        "p_min": min_p,
        "p_max": max_p,
        "q_min": min_q,
        "q_max": max_q,
        "pq_in_unit_interval": in_range,
        "filter_only_trace_name": args.only_trace_name,
        "backfill_dir": str(args.backfill_dir),
    }
    args.report_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    args.report_md.write_text(
        "\n".join(
            [
                "# P4.1 Backfill Replay Report",
                "",
                "Status: OK",
                "",
                f"Processed traces: {processed}/{len(summary)}",
                f"Scored rows: {scored_rows_total}",
                f"Lossless-eligible rows: {lossless_eligible_rows}",
                f"Reconstruction checks applied: {reconstruction_check_rows}",
                f"Reconstruction-invalid rows (q > live draft_top1 + tol): {pq_invalid_rows}",
                (
                    "Reconstruction error rate (checked rows): "
                    f"{(pq_invalid_rows / reconstruction_check_rows):.8g}"
                    if reconstruction_check_rows > 0
                    else "Reconstruction error rate (checked rows): n/a"
                ),
                f"Max reconstruction error gap: {max_reconstruction_error_gap:.8g}",
                f"p range: [{min_p:.8g}, {max_p:.8g}]",
                f"q range: [{min_q:.8g}, {max_q:.8g}]",
                f"p/q in [0,1]: {in_range}",
                "No q<->draft_top1 overwrite assertion: passed",
                f"Backfill directory: {args.backfill_dir}",
            ]
        ),
        encoding="utf-8",
    )

    flag_lines = [
        "# P4.1 pq Reconstruction Flags",
        "",
        f"Tolerance: {PQ_RECONSTRUCTION_TOLERANCE}",
        f"Total rows processed: {scored_rows_total}",
        f"Invalid rows: {pq_invalid_rows}",
        (
            f"Invalid %: {(100.0 * pq_invalid_rows / scored_rows_total):.6f}%"
            if scored_rows_total > 0
            else "Invalid %: n/a"
        ),
        "",
        "Root cause note: unresolved (execution-path numerical drift vs context/state reconstruction mismatch).",
        "Policy note: flagged rows are excluded from confirmatory P4.1 statistics and are not corrected/substituted.",
        "",
        "## Breakdown by Dataset",
    ]
    for ds in sorted(rows_by_dataset):
        total_rows = rows_by_dataset.get(ds, 0)
        invalid_rows = invalid_by_dataset.get(ds, 0)
        if total_rows > 0:
            flag_lines.append(
                f"- {ds}: rows={total_rows}, invalid={invalid_rows}, invalid_pct={(100.0 * invalid_rows / total_rows):.6f}%"
            )
        else:
            flag_lines.append(f"- {ds}: rows=0, invalid=0, invalid_pct=n/a")

    flag_lines.extend(["", "## Breakdown by Row Type"])
    for row_type in ["post_rejection", "normal"]:
        total_rows = rows_by_type[row_type]
        invalid_rows = invalid_by_type[row_type]
        if total_rows > 0:
            flag_lines.append(
                f"- {row_type}: rows={total_rows}, invalid={invalid_rows}, invalid_pct={(100.0 * invalid_rows / total_rows):.6f}%"
            )
        else:
            flag_lines.append(f"- {row_type}: rows=0, invalid=0, invalid_pct=n/a")

    flag_lines.extend(["", "## Breakdown by Position"])
    for pos in sorted(rows_by_position):
        total_rows = rows_by_position[pos]
        invalid_rows = invalid_by_position.get(pos, 0)
        if total_rows > 0:
            flag_lines.append(
                f"- position={pos}: rows={total_rows}, invalid={invalid_rows}, invalid_pct={(100.0 * invalid_rows / total_rows):.6f}%"
            )

    flag_lines.extend(
        [
            "",
            "## Full List of Flagged Rows",
            "trace_id,step,position,token_id,q,draft_top1_prob,violation_magnitude,post_rejection_row,dataset",
        ]
    )
    for fr in flagged_rows:
        flag_lines.append(
            f"{fr['trace_id']},{fr['step']},{fr['position']},{fr['token_id']},"
            f"{fr['q']},{fr['draft_top1_prob']},{fr['violation_magnitude']},"
            f"{fr['post_rejection_row']},{fr['dataset']}"
        )

    args.flags_report_md.write_text("\n".join(flag_lines), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
