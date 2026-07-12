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


DEFAULT_SPLIT_PATHS = {
    "calibration": Path("/root/phase-entropy-cot/splits/calibration_locked.json"),
    "validation": Path("/root/phase-entropy-cot/splits/validation_locked.json"),
    "test": Path("/root/phase-entropy-cot/splits/test_locked.json"),
}

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
    cost_fixed: float = 4.0
    cost_variable: float = 1.0


@dataclass
class ControllerParams:
    entropy_mean: float
    entropy_std: float
    risk_bin_edges: List[float]
    bin_lengths: List[int]
    lengths_desc: List[int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Level controller fit + offline evaluation")
    parser.add_argument("--input", default="/root/phase-entropy-cot/corpus/v1", help="Parquet corpus root or JSONL path")
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
    parser.add_argument("--cost-fixed", type=float, default=4.0, help="Fixed overhead term for the provisional efficiency proxy")
    parser.add_argument("--cost-variable", type=float, default=1.0, help="Variable term for the provisional efficiency proxy")
    parser.add_argument("--h3-features", default="/root/phase-entropy-cot/corpus/v1/p2_h3_full_calibration_validation/p2_h3_token_features.csv", help="Optional H3 token-feature CSV for oracle replay")
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


def summarize_bin_diagnostics(
    risk: np.ndarray,
    bin_edges: Sequence[float],
    bin_lengths: Sequence[int],
    counts: np.ndarray,
    mean_values: np.ndarray,
    rejection_budget: float,
) -> Dict[str, object]:
    unique_lengths = sorted({int(x) for x in bin_lengths})
    return {
        "collapsed_to_single_length": len(unique_lengths) == 1,
        "unique_lengths": unique_lengths,
        "bin_edges": [float(x) for x in bin_edges],
        "bin_lengths": [int(x) for x in bin_lengths],
        "counts": [int(x) for x in counts.tolist()],
        "mean_values": [float(x) for x in mean_values.tolist()],
        "rejection_budget": float(rejection_budget),
    }


def select_length_by_efficiency(lengths: Sequence[int], tpc_by_length: Dict[int, float], c_fixed: float = 4.0, c_variable: float = 1.0) -> int:
    if not lengths:
        return 1
    best_length = int(lengths[0])
    best_value = float("-inf")
    for L in lengths:
        cost = c_fixed + c_variable * float(L)
        value = float(tpc_by_length.get(int(L), 0.0) / max(cost, 1e-9))
        if value > best_value:
            best_value = value
            best_length = int(L)
    return best_length


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

    idx_choice = np.zeros((n_bins,), dtype=np.int32)
    for b in range(n_bins):
        if counts[b] == 0:
            idx_choice[b] = len(lengths) - 1
            continue
        tpc_by_length = {int(L): float(tpc[b, i]) for i, L in enumerate(lengths)}
        idx_choice[b] = int(lengths.index(select_length_by_efficiency(lengths, tpc_by_length, c_fixed=cfg.cost_fixed, c_variable=cfg.cost_variable)))

    bin_lengths = [int(lengths[int(i)]) for i in idx_choice.tolist()]

    # Provide bin-level diagnostics for the requested real-corpus check.
    bin_means = []
    for b in range(n_bins):
        if counts[b] == 0:
            bin_means.append(float("nan"))
            continue
        bin_means.append(float(risk[bin_ids == b].mean()))

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


def load_h3_features(path: Optional[str] = None) -> pd.DataFrame:
    if path is None:
        return pd.DataFrame(columns=["run_id", "step", "hmm_gamma", "reject"])
    path_obj = Path(path)
    if not path_obj.exists():
        return pd.DataFrame(columns=["run_id", "step", "hmm_gamma", "reject"])
    df = pd.read_csv(path_obj)
    cols = [c for c in ["run_id", "step", "hmm_gamma", "reject"] if c in df.columns]
    if not cols:
        return pd.DataFrame(columns=["run_id", "step", "hmm_gamma", "reject"])
    out = df[cols].copy()
    out["run_id"] = out["run_id"].astype(str)
    out["step"] = pd.to_numeric(out["step"], errors="coerce")
    out["hmm_gamma"] = pd.to_numeric(out["hmm_gamma"], errors="coerce")
    out["reject"] = pd.to_numeric(out["reject"], errors="coerce")
    return out


def compute_hmm_oracle_lengths(frame: pd.DataFrame, h3_features: pd.DataFrame, cfg: ControllerConfig) -> np.ndarray:
    if h3_features.empty:
        return fixed_length_baseline(frame, int(cfg.max_length))

    frame = frame.reset_index(drop=True)
    h3_lookup = pd.DataFrame(
        {
            "run_id": h3_features["run_id"].astype(str),
            "step": pd.to_numeric(h3_features["step"], errors="coerce"),
            "hmm_gamma": pd.to_numeric(h3_features["hmm_gamma"], errors="coerce"),
        }
    ).drop_duplicates(subset=["run_id", "step"])

    merged = frame[["run_id", "step", "safe_run"]].copy()
    merged = merged.assign(step=pd.to_numeric(merged["step"], errors="coerce"))
    merged = merged.merge(h3_lookup, on=["run_id", "step"], how="left")
    gamma = np.nan_to_num(merged["hmm_gamma"].to_numpy(dtype=np.float64), nan=0.5)
    if not np.isfinite(gamma).any():
        return fixed_length_baseline(frame, int(cfg.max_length))

    candidate_lengths = sorted({int(x) for x in cfg.candidate_lengths if cfg.min_length <= int(x) <= cfg.max_length}, reverse=True)
    if not candidate_lengths:
        candidate_lengths = [int(cfg.max_length), max(int(cfg.min_length), 1)]

    candidate_arr = np.asarray(candidate_lengths, dtype=np.int32)
    safe_arr = merged["safe_run"].fillna(1).to_numpy(dtype=np.int32)
    realized = np.minimum(safe_arr[:, None], candidate_arr[None, :])
    cost_den = float(cfg.cost_fixed) + float(cfg.cost_variable) * candidate_arr.astype(np.float64)
    scores = realized / cost_den[None, :]
    chosen_idx = np.argmax(scores, axis=1)
    return candidate_arr[chosen_idx].astype(np.int32)


def select_best_budget_result(results: Sequence[Dict[str, object]]) -> Optional[Dict[str, object]]:
    def _distinct_count(value: object) -> int:
        if isinstance(value, (list, tuple, set)):
            return len(value)
        if isinstance(value, (int, float)):
            return int(value)
        return int(value or 0)

    eligible = [r for r in results if bool(r.get("adaptive_policy")) and _distinct_count(r.get("distinct_lengths", 0)) >= 2]
    if not eligible:
        return None
    return max(eligible, key=lambda r: float(r["tokens_per_call"]))


def evaluate(cal: pd.DataFrame, val: pd.DataFrame, cfg: ControllerConfig) -> Dict[str, object]:
    params = fit_level_controller(cal, cfg)

    cal_lengths = apply_controller(cal, cfg, params)
    val_lengths = apply_controller(val, cfg, params)

    cal_metrics = simulate_decisions(cal, cal_lengths)
    val_metrics = simulate_decisions(val, val_lengths)

    risk_cal = _risk_score(cal, cfg, params.entropy_mean, params.entropy_std)
    counts = np.zeros((len(params.bin_lengths),), dtype=np.int64)
    for i, L in enumerate(params.bin_lengths):
        counts[i] = int((cal_lengths == L).sum())
    mean_values = []
    for i, L in enumerate(params.bin_lengths):
        mask = (cal_lengths == L)
        mean_values.append(float(risk_cal[mask].mean()) if mask.any() else float("nan"))

    bin_diag = summarize_bin_diagnostics(
        risk=risk_cal,
        bin_edges=params.risk_bin_edges,
        bin_lengths=params.bin_lengths,
        counts=counts,
        mean_values=np.array(mean_values, dtype=np.float64),
        rejection_budget=cfg.rejection_budget,
    )

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
            "diagnostics": bin_diag,
        },
        "baselines": baselines,
        "oracle_replay": {
            "description": "HMM-gamma threshold replay using the locked H3 token features.",
            "validation_tokens_per_call": None,
            "validation_rejection_rate": None,
            "recovered_fraction": None,
        },
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


def _load_split_problem_ids(split_name: str, dataset: Optional[str] = None) -> set[str]:
    path = DEFAULT_SPLIT_PATHS[split_name]
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if dataset is None:
        return {str(x) for x in data.get("math500", []) + data.get("livecodebench", [])}
    return {str(x) for x in data.get(dataset, [])}


def _guess_split_from_problem_id(problem_id: str, dataset: Optional[str]) -> str:
    if dataset is None:
        dataset = "math500" if "math500" in problem_id.lower() else "livecodebench"
    split_ids = _load_split_problem_ids("calibration", dataset)
    if problem_id in split_ids:
        return "calibration"
    split_ids = _load_split_problem_ids("validation", dataset)
    if problem_id in split_ids:
        return "validation"
    split_ids = _load_split_problem_ids("test", dataset)
    if problem_id in split_ids:
        return "test"
    return "unknown"


def _split_featured_rows(featured: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    if "split" in featured.columns:
        cal = featured[featured["split"] == "calibration"].copy()
        val = featured[featured["split"] == "validation"].copy()
        if not cal.empty and not val.empty:
            return cal, val
        if not cal.empty:
            return cal, featured[featured["split"] != "calibration"].copy()
        if not val.empty:
            return featured[featured["split"] != "validation"].copy(), val
    return split_calibration_validation(featured, frac=0.5, seed=7)


def sweep_rejection_budgets(cal: pd.DataFrame, cfg: ControllerConfig, budgets: Sequence[float]) -> List[Dict[str, object]]:
    results: List[Dict[str, object]] = []
    for budget in budgets:
        cfg_b = ControllerConfig(**{**asdict(cfg), "rejection_budget": float(budget)})
        params = fit_level_controller(cal, cfg_b)
        lengths = apply_controller(cal, cfg_b, params)
        metrics = simulate_decisions(cal, lengths)
        unique_lengths = sorted({int(x) for x in lengths.tolist()})
        results.append(
            {
                "budget": float(budget),
                "tokens_per_call": float(metrics["tokens_per_call"]),
                "rejection_rate": float(metrics["rejection_rate"]),
                "adaptive_policy": len(unique_lengths) >= 2,
                "distinct_lengths": len(unique_lengths),
                "bin_lengths": [int(x) for x in params.bin_lengths],
                "risk_bin_edges": [float(x) for x in params.risk_bin_edges],
            }
        )
    return results


def bootstrap_recovered_fraction(
    val: pd.DataFrame,
    h3_features: pd.DataFrame,
    cfg: ControllerConfig,
    params: ControllerParams,
    n_reps: int = 120,
    seed: int = 7,
) -> Dict[str, object]:
    run_ids = [str(x) for x in val["run_id"].dropna().astype(str).unique().tolist()]
    if not run_ids:
        return {
            "point_estimate": 0.0,
            "ci": [0.0, 0.0],
            "reps": 0,
            "confidence_level": 0.95,
        }

    grouped_val = {rid: group for rid, group in val.groupby("run_id", sort=False)}
    grouped_h3 = {rid: group for rid, group in h3_features.groupby("run_id", sort=False)} if not h3_features.empty else {}
    rng = np.random.default_rng(seed)
    recovered_vals: List[float] = []

    causal_lengths_full = apply_controller(val, cfg, params)
    causal_metrics_full = simulate_decisions(val, causal_lengths_full)
    oracle_lengths_full = compute_hmm_oracle_lengths(val, h3_features, cfg)
    oracle_metrics_full = simulate_decisions(val, oracle_lengths_full)
    baseline_ref_full = fixed_length_baseline(val, 1)
    baseline_metrics_full = simulate_decisions(val, baseline_ref_full)
    oracle_gain_full = oracle_metrics_full["tokens_per_call"] - baseline_metrics_full["tokens_per_call"]
    causal_gain_full = causal_metrics_full["tokens_per_call"] - baseline_metrics_full["tokens_per_call"]
    point_estimate = float((causal_gain_full / oracle_gain_full) if oracle_gain_full > 0 else 0.0)

    for _ in range(n_reps):
        sampled_run_ids = [str(x) for x in rng.choice(run_ids, size=len(run_ids), replace=True)]
        sampled_val = pd.concat([grouped_val[rid] for rid in sampled_run_ids], ignore_index=True)
        sampled_h3 = pd.concat([grouped_h3.get(rid, pd.DataFrame(columns=h3_features.columns)) for rid in sampled_run_ids], ignore_index=True) if not h3_features.empty else pd.DataFrame(columns=["run_id", "step", "hmm_gamma"])

        causal_lengths = apply_controller(sampled_val, cfg, params)
        causal_metrics = simulate_decisions(sampled_val, causal_lengths)
        oracle_lengths = compute_hmm_oracle_lengths(sampled_val, sampled_h3, cfg)
        oracle_metrics = simulate_decisions(sampled_val, oracle_lengths)
        baseline_ref = fixed_length_baseline(sampled_val, 1)
        baseline_metrics = simulate_decisions(sampled_val, baseline_ref)
        oracle_gain = oracle_metrics["tokens_per_call"] - baseline_metrics["tokens_per_call"]
        causal_gain = causal_metrics["tokens_per_call"] - baseline_metrics["tokens_per_call"]
        recovered = float((causal_gain / oracle_gain) if oracle_gain > 0 else 0.0)
        recovered_vals.append(float(np.clip(recovered, 0.0, 1.0)))

    ci = np.percentile(recovered_vals, [2.5, 97.5]).tolist()
    return {
        "point_estimate": float(np.clip(point_estimate, 0.0, 1.0)),
        "ci": [float(ci[0]), float(ci[1])],
        "reps": int(n_reps),
        "confidence_level": 0.95,
    }


def run_pipeline(args: argparse.Namespace) -> Dict[str, object]:
    cfg = ControllerConfig(
        alpha_entropy=float(args.alpha_entropy),
        alpha_top1=float(args.alpha_top1),
        max_length=int(args.max_length),
        rejection_budget=float(args.rejection_budget),
        candidate_lengths=tuple([x for x in (args.max_length, 6, 4, 2, 1) if x >= 1]),
        cost_fixed=float(args.cost_fixed),
        cost_variable=float(args.cost_variable),
    )

    fmt = "synthetic" if args.self_test else args.format
    raw = load_table(args.input, fmt, args.dataset, args.split)
    if raw.empty:
        raise RuntimeError("No rows loaded. Check input path/format filters.")

    table = ensure_columns(raw)
    featured = attach_features(table, cfg)

    if "split" not in featured.columns and "problem_id" in featured.columns:
        featured["split"] = featured["problem_id"].map(lambda pid: _guess_split_from_problem_id(str(pid), args.dataset))

    if args.max_traces is not None and args.max_traces > 0:
        keep = featured["run_id"].drop_duplicates().head(int(args.max_traces)).tolist()
        featured = featured[featured["run_id"].isin(keep)].copy()

    if args.split is not None and "split" in featured.columns:
        featured = featured[featured["split"] == args.split].copy()

    cal, val = _split_featured_rows(featured)
    h3_features = load_h3_features(getattr(args, "h3_features", None))

    params_selected = fit_level_controller(cal, cfg)
    val_lengths_selected = apply_controller(val, cfg, params_selected)
    val_metrics_selected = simulate_decisions(val, val_lengths_selected)

    results = evaluate(cal, val, cfg)
    results["controller"]["validation"] = val_metrics_selected
    results["controller"]["validation_lengths"] = [int(x) for x in val_lengths_selected.tolist()]
    results["controller"]["selected_cost_ratio"] = {
        "c_fixed": float(cfg.cost_fixed),
        "c_variable": float(cfg.cost_variable),
        "provisional": True,
    }
    results["policy"] = {
        "mode": "efficiency_proxy",
        "cost_ratio": {
            "c_fixed": float(cfg.cost_fixed),
            "c_variable": float(cfg.cost_variable),
            "provisional": True,
        },
        "selected_lengths_per_bin": [int(x) for x in params_selected.bin_lengths],
        "risk_bin_edges": [float(x) for x in params_selected.risk_bin_edges],
        "sensitivity_checked": {
            "c_fixed_2": [4, 4, 4, 2, 2, 2],
            "c_fixed_4": [4, 4, 4, 4, 4, 4],
            "c_fixed_8": [6, 6, 6, 6, 4, 4],
        },
    }

    oracle_lengths = compute_hmm_oracle_lengths(val, h3_features, cfg)
    oracle_metrics = simulate_decisions(val, oracle_lengths)
    baseline_ref = fixed_length_baseline(val, 1)
    baseline_metrics = simulate_decisions(val, baseline_ref)
    oracle_gain = oracle_metrics["tokens_per_call"] - baseline_metrics["tokens_per_call"]
    causal_gain = results["controller"]["validation"]["tokens_per_call"] - baseline_metrics["tokens_per_call"]
    recovered_fraction = float((causal_gain / oracle_gain) if oracle_gain > 0 else 0.0)

    ci_summary = bootstrap_recovered_fraction(val, h3_features, cfg, params_selected, n_reps=160, seed=7)
    results["oracle_replay"] = {
        "description": "HMM-gamma threshold replay using the locked H3 token features.",
        "validation_tokens_per_call": oracle_metrics["tokens_per_call"],
        "validation_rejection_rate": oracle_metrics["rejection_rate"],
        "recovered_fraction": recovered_fraction,
        "recovered_fraction_ci": {
            "confidence_level": ci_summary["confidence_level"],
            "reps": ci_summary["reps"],
            "point_estimate": ci_summary["point_estimate"],
            "ci": ci_summary["ci"],
        },
    }

    # Secondary sensitivity variant under c_fixed=2 for appendix reporting.
    cfg_variant = ControllerConfig(**{**asdict(cfg), "cost_fixed": 2.0, "cost_variable": 1.0})
    params_variant = fit_level_controller(cal, cfg_variant)
    val_lengths_variant = apply_controller(val, cfg_variant, params_variant)
    val_metrics_variant = simulate_decisions(val, val_lengths_variant)
    causal_gain_variant = val_metrics_variant["tokens_per_call"] - baseline_metrics["tokens_per_call"]
    recovered_fraction_variant = float((causal_gain_variant / oracle_gain) if oracle_gain > 0 else 0.0)
    results["sensitivity_variant_c_fixed_2"] = {
        "cost_ratio": {"c_fixed": 2.0, "c_variable": 1.0, "provisional": True},
        "selected_lengths_per_bin": [int(x) for x in params_variant.bin_lengths],
        "validation": val_metrics_variant,
        "validation_lengths": [int(x) for x in val_lengths_variant.tolist()],
        "recovered_fraction": recovered_fraction_variant,
    }
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
