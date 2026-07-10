#!/usr/bin/env python3
"""
Level-based speculative decoding controller (offline).

This module intentionally avoids phase-state inputs. It builds a controller from
smoothed signal levels (EWMA of entropy/confidence), calibrates on a
calibration split, and evaluates with an offline acceptance-run simulator.

It supports:
- Parquet corpus roots partitioned with Hive-style directories
- JSONL trace directories/files
- Synthetic fallback evaluation for local sanity checks
"""

from __future__ import annotations

import argparse
import json
import math
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

try:
    import pyarrow.dataset as ds
except Exception:  # pragma: no cover
    ds = None


@dataclass
class ControllerConfig:
    alpha_entropy: float = 0.2
    alpha_top1: float = 0.2
    entropy_weight: float = 0.65
    uncertainty_weight: float = 0.35
    max_length: int = 8
    min_length: int = 1
    rejection_budget: float = 0.12
    candidate_lengths: Tuple[int, ...] = (8, 6, 4, 2, 1)


@dataclass
class ControllerParams:
    entropy_mean: float
    entropy_std: float
    risk_bin_edges: List[float]
    bin_lengths: List[int]
    lengths_desc: List[int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Level controller fit + offline evaluation")
    parser.add_argument("--input", default=None, help="Parquet corpus root or JSONL path")
    parser.add_argument(
        "--format",
        default="auto",
        choices=["auto", "parquet", "jsonl", "synthetic"],
        help="Input format",
    )
    parser.add_argument("--dataset", default=None, help="Optional dataset filter")
    parser.add_argument("--split", default=None, help="Optional split filter (if present)")
    parser.add_argument("--seed", type=int, default=7, help="Random seed")
    parser.add_argument("--calibration-frac", type=float, default=0.5, help="Fallback split fraction by problem_id")
    parser.add_argument("--max-traces", type=int, default=None, help="Optional cap on trace count")
    parser.add_argument("--out", default=None, help="Output JSON path")
    parser.add_argument("--rejection-budget", type=float, default=0.12, help="Max rejection rate target")
    parser.add_argument("--max-length", type=int, default=8, help="Maximum draft length")
    parser.add_argument("--alpha-entropy", type=float, default=0.2, help="EWMA alpha for entropy")
    parser.add_argument("--alpha-top1", type=float, default=0.2, help="EWMA alpha for top1 confidence")
    parser.add_argument("--self-test", action="store_true", help="Run synthetic sanity evaluation")
    return parser.parse_args()


def ewma(values: np.ndarray, alpha: float) -> np.ndarray:
    out = np.empty_like(values, dtype=np.float64)
    if values.size == 0:
        return out
    prev = float(values[0])
    out[0] = prev
    for i in range(1, values.size):
        x = float(values[i])
        if not np.isfinite(x):
            x = prev
        prev = alpha * x + (1.0 - alpha) * prev
        out[i] = prev
    return out


def _find_parquet_files(root: Path) -> List[str]:
    files: List[str] = []
    for dirpath, _, names in os.walk(root):
        for name in names:
            if name.endswith(".parquet"):
                files.append(os.path.join(dirpath, name))
    return files


def _read_jsonl_paths(path: Path) -> pd.DataFrame:
    paths: List[Path] = []
    if path.is_file() and path.suffix == ".jsonl":
        paths = [path]
    elif path.is_dir():
        paths = sorted(p for p in path.rglob("*.jsonl") if p.is_file())

    rows: List[Dict[str, object]] = []
    for p in paths:
        run_id = p.stem
        with p.open("r", encoding="utf-8") as handle:
            for i, line in enumerate(handle):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                rows.append(
                    {
                        "run_id": obj.get("run_id") or run_id,
                        "problem_id": obj.get("problem_id") or run_id,
                        "step": obj.get("step", obj.get("position", i)),
                        "position": obj.get("position", obj.get("step", i)),
                        "dataset": obj.get("dataset"),
                        "split": obj.get("split"),
                        "draft_entropy": obj.get("draft_entropy"),
                        "target_entropy": obj.get("target_entropy"),
                        "draft_top1_prob": obj.get("draft_top1_prob", obj.get("top1_p")),
                        "accepted": obj.get("accepted"),
                        "phase_label_hmm": obj.get("phase_label_hmm"),
                    }
                )
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)


def load_table(input_path: Optional[str], fmt: str, dataset: Optional[str], split: Optional[str]) -> pd.DataFrame:
    if fmt == "synthetic":
        return make_synthetic_dataset(seed=7, n_traces=48, trace_len=120)

    if input_path is None:
        raise ValueError("--input is required unless --format synthetic")

    path = Path(input_path)
    if fmt == "auto":
        if path.is_dir() and _find_parquet_files(path):
            fmt = "parquet"
        elif path.is_file() and path.suffix == ".jsonl":
            fmt = "jsonl"
        elif path.is_dir() and list(path.rglob("*.jsonl")):
            fmt = "jsonl"
        else:
            raise FileNotFoundError(f"Could not infer format for input path: {path}")

    if fmt == "parquet":
        if ds is None:
            raise RuntimeError("pyarrow is required to read parquet input")
        parquet_files = _find_parquet_files(path)
        if not parquet_files:
            raise FileNotFoundError(f"No parquet files found under {path}")
        table = ds.dataset(parquet_files, format="parquet", partitioning="hive", partition_base_dir=str(path)).to_table()
        df = table.to_pandas()
    elif fmt == "jsonl":
        df = _read_jsonl_paths(path)
    else:
        raise ValueError(f"Unsupported format: {fmt}")

    if df.empty:
        return df

    if dataset is not None and "dataset" in df.columns:
        df = df[df["dataset"] == dataset]
    if split is not None and "split" in df.columns:
        df = df[df["split"] == split]

    return df.reset_index(drop=True)


def ensure_columns(df: pd.DataFrame) -> pd.DataFrame:
    required = ["run_id", "problem_id", "step", "position", "accepted"]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    out = df.copy()
    out["run_id"] = out["run_id"].astype(str)
    out["problem_id"] = out["problem_id"].astype(str)
    out["step"] = pd.to_numeric(out["step"], errors="coerce")
    out["position"] = pd.to_numeric(out["position"], errors="coerce")
    out["accepted"] = out["accepted"].astype(bool)

    if "draft_entropy" in out.columns:
        out["draft_entropy"] = pd.to_numeric(out["draft_entropy"], errors="coerce")
    else:
        out["draft_entropy"] = np.nan

    if "target_entropy" in out.columns:
        out["target_entropy"] = pd.to_numeric(out["target_entropy"], errors="coerce")
    else:
        out["target_entropy"] = np.nan

    if "draft_top1_prob" in out.columns:
        out["draft_top1_prob"] = pd.to_numeric(out["draft_top1_prob"], errors="coerce")
    else:
        out["draft_top1_prob"] = np.nan

    entropy_fallback = out["target_entropy"]
    out["entropy"] = out["draft_entropy"].where(out["draft_entropy"].notna(), entropy_fallback)
    out["entropy"] = out["entropy"].fillna(float(np.nanmedian(out["entropy"].to_numpy(dtype=np.float64))))

    p = out["draft_top1_prob"].to_numpy(dtype=np.float64)
    valid = np.isfinite(p)
    if valid.any():
        fill = float(np.nanmedian(p[valid]))
    else:
        fill = 0.5
    p = np.where(valid, p, fill)
    p = np.clip(p, 1e-6, 1.0 - 1e-6)
    out["draft_top1_prob"] = p

    return out


def compute_safe_acceptance_run(accepted: np.ndarray) -> np.ndarray:
    """safe[i] = max contiguous accepted tokens starting at i."""
    n = accepted.size
    safe = np.zeros(n, dtype=np.int32)
    run = 0
    for i in range(n - 1, -1, -1):
        if bool(accepted[i]):
            run += 1
        else:
            run = 0
        safe[i] = run
    return safe


def attach_features(df: pd.DataFrame, cfg: ControllerConfig) -> pd.DataFrame:
    parts: List[pd.DataFrame] = []
    for _, g in df.groupby("run_id", sort=False):
        h = g.sort_values(["step", "position"]).copy()
        e = h["entropy"].to_numpy(dtype=np.float64)
        p = h["draft_top1_prob"].to_numpy(dtype=np.float64)
        h["entropy_ewma"] = ewma(e, cfg.alpha_entropy)
        h["top1_ewma"] = ewma(p, cfg.alpha_top1)
        h["safe_run"] = compute_safe_acceptance_run(h["accepted"].to_numpy(dtype=bool))
        parts.append(h)
    return pd.concat(parts, ignore_index=True)


def split_calibration_validation(df: pd.DataFrame, frac: float, seed: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    probs = sorted(df["problem_id"].dropna().astype(str).unique().tolist())
    if not probs:
        return df.copy(), df.copy()
    rng = np.random.default_rng(seed)
    shuffled = probs.copy()
    rng.shuffle(shuffled)
    k = max(1, min(len(shuffled) - 1, int(round(len(shuffled) * frac))))
    cal_set = set(shuffled[:k])
    cal = df[df["problem_id"].astype(str).isin(cal_set)].copy()
    val = df[~df["problem_id"].astype(str).isin(cal_set)].copy()
    if val.empty:
        val = cal.copy()
    return cal, val


def _risk_score(frame: pd.DataFrame, cfg: ControllerConfig, mean: float, std: float) -> np.ndarray:
    z = (frame["entropy_ewma"].to_numpy(dtype=np.float64) - mean) / std
    uncertainty = 1.0 - frame["top1_ewma"].to_numpy(dtype=np.float64)
    return cfg.entropy_weight * z + cfg.uncertainty_weight * uncertainty


def _lengths_from_bins(risk: np.ndarray, edges: Sequence[float], bin_lengths: Sequence[int]) -> np.ndarray:
    # bin id in [0, n_bins-1] where n_bins == len(bin_lengths)
    bins = np.digitize(risk, np.asarray(edges, dtype=np.float64), right=False)
    bins = np.clip(bins, 0, len(bin_lengths) - 1)
    return np.asarray([int(bin_lengths[b]) for b in bins], dtype=np.int32)


def simulate_decisions(frame: pd.DataFrame, lengths: np.ndarray) -> Dict[str, float]:
    safe = frame["safe_run"].to_numpy(dtype=np.int32)
    chosen = lengths.astype(np.int32)
    realized = np.minimum(chosen, safe)
    reject = (chosen > safe).astype(np.int32)

    total_tokens = int(realized.sum())
    total_calls = int(len(chosen))
    tokens_per_call = float(total_tokens / total_calls) if total_calls else 0.0
    rejection_rate = float(reject.mean()) if total_calls else 0.0

    return {
        "rows": total_calls,
        "mean_chosen_length": float(chosen.mean()) if total_calls else 0.0,
        "tokens_per_call": tokens_per_call,
        "rejection_rate": rejection_rate,
    }


def fit_level_controller(cal: pd.DataFrame, cfg: ControllerConfig) -> ControllerParams:
    e = cal["entropy_ewma"].to_numpy(dtype=np.float64)
    mean = float(np.nanmean(e))
    std = float(np.nanstd(e))
    if not np.isfinite(std) or std < 1e-6:
        std = 1.0

    lengths = sorted({int(x) for x in cfg.candidate_lengths if cfg.min_length <= int(x) <= cfg.max_length}, reverse=True)
    if not lengths:
        lengths = [cfg.max_length, max(cfg.min_length, 1)]

    risk = _risk_score(cal, cfg, mean, std)
    safe = cal["safe_run"].to_numpy(dtype=np.int32)

    # Build monotonic risk bins and learn one draft length per bin.
    n_bins = min(10, max(4, len(lengths) + 1))
    quantiles = np.linspace(0.0, 1.0, n_bins + 1)
    edge_values = np.quantile(risk, quantiles)

    # Ensure strict monotonic internal edges for np.digitize behavior.
    internal = []
    prev = -float("inf")
    for x in edge_values[1:-1]:
        x = float(x)
        if x <= prev:
            x = prev + 1e-8
        internal.append(x)
        prev = x

    bin_ids = np.digitize(risk, np.asarray(internal, dtype=np.float64), right=False)
    bin_ids = np.clip(bin_ids, 0, n_bins - 1)

    counts = np.zeros((n_bins,), dtype=np.int64)
    rej = np.zeros((n_bins, len(lengths)), dtype=np.float64)
    tpc = np.zeros((n_bins, len(lengths)), dtype=np.float64)

    for b in range(n_bins):
        mask = bin_ids == b
        counts[b] = int(mask.sum())
        if counts[b] == 0:
            continue
        safe_b = safe[mask]
        for i, L in enumerate(lengths):
            chosen = np.full(shape=(counts[b],), fill_value=int(L), dtype=np.int32)
            sim_b = simulate_decisions(pd.DataFrame({"safe_run": safe_b}), chosen)
            rej[b, i] = sim_b["rejection_rate"]
            tpc[b, i] = sim_b["tokens_per_call"]

    # Start each bin at best local throughput under budget if possible, else conservative.
    idx_choice = np.zeros((n_bins,), dtype=np.int32)
    for b in range(n_bins):
        if counts[b] == 0:
            idx_choice[b] = len(lengths) - 1
            continue
        valid = [i for i in range(len(lengths)) if rej[b, i] <= cfg.rejection_budget]
        if valid:
            idx_choice[b] = int(max(valid, key=lambda i: tpc[b, i]))
        else:
            idx_choice[b] = len(lengths) - 1

    def aggregate_metrics(choice: np.ndarray) -> Tuple[float, float]:
        total = max(1, int(counts.sum()))
        rej_sum = 0.0
        tpc_sum = 0.0
        for b in range(n_bins):
            if counts[b] == 0:
                continue
            i = int(choice[b])
            w = float(counts[b]) / float(total)
            rej_sum += w * rej[b, i]
            tpc_sum += w * tpc[b, i]
        return rej_sum, tpc_sum

    # Enforce global budget with greedy step-down when needed.
    current_rej, _ = aggregate_metrics(idx_choice)
    while current_rej > cfg.rejection_budget:
        best_bin = None
        best_ratio = -float("inf")
        for b in range(n_bins):
            i = int(idx_choice[b])
            if counts[b] == 0 or i >= len(lengths) - 1:
                continue
            dr = rej[b, i] - rej[b, i + 1]
            dt = tpc[b, i] - tpc[b, i + 1]
            if dr <= 0:
                continue
            ratio = dr / max(dt, 1e-9)
            if ratio > best_ratio:
                best_ratio = ratio
                best_bin = b
        if best_bin is None:
            break
        idx_choice[best_bin] += 1
        current_rej, _ = aggregate_metrics(idx_choice)

    bin_lengths = [int(lengths[int(i)]) for i in idx_choice.tolist()]

    return ControllerParams(
        entropy_mean=mean,
        entropy_std=std,
        risk_bin_edges=[float(x) for x in internal],
        bin_lengths=bin_lengths,
        lengths_desc=[int(x) for x in lengths],
    )


def apply_controller(frame: pd.DataFrame, cfg: ControllerConfig, params: ControllerParams) -> np.ndarray:
    risk = _risk_score(frame, cfg, params.entropy_mean, params.entropy_std)
    return _lengths_from_bins(risk, params.risk_bin_edges, params.bin_lengths)


def fixed_length_baseline(frame: pd.DataFrame, length: int) -> np.ndarray:
    return np.full(shape=(len(frame),), fill_value=int(length), dtype=np.int32)


def evaluate(cal: pd.DataFrame, val: pd.DataFrame, cfg: ControllerConfig) -> Dict[str, object]:
    params = fit_level_controller(cal, cfg)

    cal_lengths = apply_controller(cal, cfg, params)
    val_lengths = apply_controller(val, cfg, params)

    cal_metrics = simulate_decisions(cal, cal_lengths)
    val_metrics = simulate_decisions(val, val_lengths)

    baselines: Dict[str, Dict[str, float]] = {}
    for length in sorted(set(cfg.candidate_lengths), reverse=True):
        baselines[f"fixed_L{int(length)}"] = simulate_decisions(val, fixed_length_baseline(val, int(length)))

    best_baseline_key = sorted(baselines.keys(), key=lambda k: baselines[k]["tokens_per_call"], reverse=True)[0]
    best_baseline = baselines[best_baseline_key]

    summary = {
        "controller": {
            "calibration": cal_metrics,
            "validation": val_metrics,
            "params": asdict(params),
            "config": asdict(cfg),
        },
        "baselines": baselines,
        "comparison": {
            "best_tokens_per_call_baseline": best_baseline_key,
            "controller_tokens_per_call": val_metrics["tokens_per_call"],
            "baseline_tokens_per_call": best_baseline["tokens_per_call"],
            "controller_rejection_rate": val_metrics["rejection_rate"],
            "baseline_rejection_rate": best_baseline["rejection_rate"],
            "tokens_per_call_delta": val_metrics["tokens_per_call"] - best_baseline["tokens_per_call"],
        },
    }
    return summary


def make_synthetic_dataset(seed: int, n_traces: int = 60, trace_len: int = 140) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows: List[Dict[str, object]] = []
    for t in range(n_traces):
        run_id = f"synthetic-{t}"
        problem_id = f"prob-{t // 2}"
        phase = 0
        for step in range(trace_len):
            if rng.uniform() < 0.07:
                phase = 1 - phase
            # Hidden regime drives entropy/confidence.
            if phase == 0:
                entropy = float(rng.normal(1.6, 0.25))
                top1 = float(np.clip(rng.normal(0.84, 0.05), 0.01, 0.99))
                p_accept = 0.90
            else:
                entropy = float(rng.normal(3.0, 0.35))
                top1 = float(np.clip(rng.normal(0.58, 0.07), 0.01, 0.99))
                p_accept = 0.63

            accepted = bool(rng.uniform() < p_accept)
            rows.append(
                {
                    "run_id": run_id,
                    "problem_id": problem_id,
                    "dataset": "synthetic",
                    "split": "none",
                    "step": step,
                    "position": step,
                    "draft_entropy": entropy,
                    "target_entropy": np.nan,
                    "draft_top1_prob": top1,
                    "accepted": accepted,
                    "phase_label_hmm": np.nan,
                }
            )
    return pd.DataFrame(rows)


def run_pipeline(args: argparse.Namespace) -> Dict[str, object]:
    cfg = ControllerConfig(
        alpha_entropy=float(args.alpha_entropy),
        alpha_top1=float(args.alpha_top1),
        max_length=int(args.max_length),
        rejection_budget=float(args.rejection_budget),
        candidate_lengths=tuple([x for x in (args.max_length, 6, 4, 2, 1) if x >= 1]),
    )

    fmt = "synthetic" if args.self_test else args.format
    raw = load_table(args.input, fmt, args.dataset, args.split)
    if raw.empty:
        raise RuntimeError("No rows loaded. Check input path/format filters.")

    table = ensure_columns(raw)
    featured = attach_features(table, cfg)

    if args.max_traces is not None and args.max_traces > 0:
        keep = featured["run_id"].drop_duplicates().head(int(args.max_traces)).tolist()
        featured = featured[featured["run_id"].isin(keep)].copy()

    cal, val = split_calibration_validation(featured, frac=float(args.calibration_frac), seed=int(args.seed))
    results = evaluate(cal, val, cfg)
    results["meta"] = {
        "rows_total": int(len(featured)),
        "rows_calibration": int(len(cal)),
        "rows_validation": int(len(val)),
        "traces_total": int(featured["run_id"].nunique()),
        "problems_total": int(featured["problem_id"].nunique()),
        "format": fmt,
    }
    return results


def main() -> None:
    args = parse_args()
    results = run_pipeline(args)
    text = json.dumps(results, indent=2)
    print(text)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
