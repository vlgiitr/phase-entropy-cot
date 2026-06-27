#!/usr/bin/env python3
"""
Compute Silverman test results only for existing P2 H1 outputs.

This script updates `silverman_status` and `silverman_pvalue` columns in
`raw_trace_metrics.csv` and `masked_trace_metrics.csv` without recomputing the
other H1 tests.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
import pandas as pd

# Reuse corpus loading, entropy materialization, and view builders from H1 script.
from p2_h1_bimodality import (  # type: ignore
    build_view_trace,
    load_corpus,
    materialize_entropy_series,
    resolve_corpus_path,
    try_silverman_test,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Compute Silverman-only outputs for existing H1 metrics.")
    p.add_argument("--corpus-path", default="corpus/v1", help="Corpus root used by H1.")
    p.add_argument("--out-dir", required=True, help="Existing H1 output directory to update.")
    p.add_argument("--entropy-col", default="auto", choices=["auto", "draft_entropy", "target_entropy"])
    p.add_argument("--dataset", default=None, choices=[None, "math500", "livecodebench"], help="Optional dataset filter.")
    p.add_argument("--split", default=None, help="Optional split filter.")
    p.add_argument("--min-trace-len", type=int, default=50, help="Minimum rows per trace after view filters.")
    return p.parse_args()


def _compute_for_run(df: pd.DataFrame, run_id: str, view: str, min_trace_len: int) -> Tuple[str, Optional[float]]:
    group = df[df["run_id"] == run_id].copy()
    if group.empty:
        return "missing_run", None
    trace_view = build_view_trace(group, view)
    if len(trace_view) < min_trace_len:
        return "too_short", None
    series = pd.to_numeric(trace_view["analysis_entropy"], errors="coerce").to_numpy(dtype=np.float64)
    series = series[np.isfinite(series)]
    if series.shape[0] < min_trace_len:
        return "too_short", None
    status, pvalue = try_silverman_test(series)
    return status, pvalue


def update_view_metrics(df_all: pd.DataFrame, csv_path: Path, view: str, min_trace_len: int) -> None:
    metrics = pd.read_csv(csv_path)
    statuses = []
    pvalues = []
    for run_id in metrics["run_id"].astype(str).tolist():
        status, pvalue = _compute_for_run(df_all, run_id, view, min_trace_len)
        statuses.append(status)
        pvalues.append(pvalue)
    metrics["silverman_status"] = statuses
    metrics["silverman_pvalue"] = pvalues
    metrics.to_csv(csv_path, index=False)



def main() -> None:
    args = parse_args()
    corpus_path = resolve_corpus_path(args.corpus_path)
    out_dir = Path(args.out_dir)

    df = load_corpus(corpus_path, args.dataset, args.split)
    df, _ = materialize_entropy_series(df, args.entropy_col)
    df = df[df["analysis_entropy"].notna()].copy()

    for view in ("raw", "masked"):
        csv_path = out_dir / f"{view}_trace_metrics.csv"
        if csv_path.exists():
            update_view_metrics(df, csv_path, view, args.min_trace_len)


if __name__ == "__main__":
    main()
