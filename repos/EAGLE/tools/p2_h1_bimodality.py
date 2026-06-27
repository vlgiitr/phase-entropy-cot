#!/usr/bin/env python3
"""
Phase 2.A H1 analysis.

This script covers the Phase 2.A tests only:
- marginal bimodality: Hartigan dip test, 1-vs-2 component GMM BIC, Silverman test hook, n_eff
- temporal phase structure: 2-state Gaussian HMM, LR test vs 1-state, PELT changepoints, run-length KS test
- autocorrelation-preserving nulls: stationary block bootstrap, AR(p) surrogate, single-state HMM surrogate
- artifact controls: formatting/cue mask, single contiguous <think> span

It is written to be run later; it does not execute anything on import.
"""

from __future__ import annotations

import argparse
import importlib
import json
import math
import os
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyarrow.dataset as ds
from scipy import stats as scipy_stats
from sklearn.mixture import GaussianMixture

try:
	from diptest import diptest
except Exception:  # pragma: no cover - dependency is expected in the analysis env
	diptest = None

try:
	from hmmlearn.hmm import GaussianHMM
except Exception:  # pragma: no cover
	GaussianHMM = None

try:
	import ruptures as rpt
except Exception:  # pragma: no cover
	rpt = None

try:
	from arch.bootstrap import StationaryBootstrap, optimal_block_length
except Exception:  # pragma: no cover
	StationaryBootstrap = None
	optimal_block_length = None

try:
	from statsmodels.tsa.stattools import acf
except Exception:  # pragma: no cover
	acf = None

try:
	from statsmodels.tsa.ar_model import AutoReg
except Exception:  # pragma: no cover
	AutoReg = None


DEFAULT_CORPUS_PATHS = (
	Path("/root/phase-entropy-cot/repos/EAGLE/corpus/v1"),
	Path("/root/phase-entropy-cot/corpus/v1"),
)


@dataclass
class TraceMetric:
	view: str
	run_id: str
	dataset: str
	problem_id: str
	n_tokens: int
	entropy_source: str
	dip_stat: Optional[float]
	dip_pvalue: Optional[float]
	gmm_delta_bic: Optional[float]
	gmm_prefer_2: Optional[bool]
	silverman_status: str
	silverman_pvalue: Optional[float]
	n_eff: Optional[float]
	hmm_ll_1: Optional[float]
	hmm_ll_2: Optional[float]
	hmm_lr_stat: Optional[float]
	hmm_lr_pvalue: Optional[float]
	hmm_states: Optional[List[int]]
	pelt_changepoints: Optional[List[int]]
	pelt_segment_lengths: Optional[List[int]]
	run_length_ks_stat: Optional[float]
	run_length_ks_pvalue: Optional[float]
	block_bootstrap_dip_mean: Optional[float]
	block_bootstrap_dip_pvalue: Optional[float]
	ar_surrogate_dip_mean: Optional[float]
	ar_surrogate_dip_pvalue: Optional[float]
	hmm_surrogate_dip_mean: Optional[float]
	hmm_surrogate_dip_pvalue: Optional[float]


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Phase 2.A H1 analysis on the corpus.")
	parser.add_argument("--corpus-path", default=None, help="Corpus root. Defaults to the first existing known path.")
	parser.add_argument("--out-dir", default="/root/phase-entropy-cot/repos/EAGLE/results/p2_h1", help="Output directory.")
	parser.add_argument("--entropy-col", default="auto", choices=["auto", "draft_entropy", "target_entropy"], help="Entropy column to analyze.")
	parser.add_argument("--dataset", default=None, choices=[None, "math500", "livecodebench"], help="Optional dataset filter.")
	parser.add_argument("--split", default=None, help="Optional split filter.")
	parser.add_argument("--min-trace-len", type=int, default=50, help="Minimum rows per trace after filtering.")
	parser.add_argument("--max-traces", type=int, default=None, help="Optional cap on traces to analyze.")
	parser.add_argument("--random-seed", type=int, default=7, help="Random seed.")
	parser.add_argument("--n-surrogates", type=int, default=200, help="Number of surrogate draws per trace for nulls.")
	parser.add_argument("--bootstrap-reps", type=int, default=200, help="Number of block bootstrap replicates per trace.")
	parser.add_argument("--ar-max-lag", type=int, default=12, help="Maximum lag searched for AR(p).")
	parser.add_argument("--hmm-max-iter", type=int, default=100, help="Max HMM iterations.")
	parser.add_argument("--pelt-penalty", type=float, default=3.0, help="PELT penalty multiplier.")
	return parser.parse_args()


def resolve_corpus_path(candidate: Optional[str]) -> Path:
	if candidate:
		path = Path(candidate)
		if not path.exists():
			raise FileNotFoundError(f"Corpus path not found: {path}")
		return path
	for path in DEFAULT_CORPUS_PATHS:
		if path.exists():
			return path
	raise FileNotFoundError("No corpus path found. Checked known default locations.")


def load_corpus(corpus_path: Path, dataset: Optional[str], split: Optional[str]) -> pd.DataFrame:
	parquet_files: List[str] = []
	for root, _, files in os.walk(corpus_path):
		for name in files:
			if name.endswith(".parquet"):
				parquet_files.append(os.path.join(root, name))
	if not parquet_files:
		raise FileNotFoundError(f"No parquet files found under {corpus_path}")

	dataset_obj = ds.dataset(parquet_files, format="parquet", partitioning="hive", partition_base_dir=str(corpus_path))
	columns = [
		"run_id",
		"problem_id",
		"position",
		"step",
		"dataset",
		"split",
		"draft_entropy",
		"target_entropy",
		"draft_topk_probs",
		"token_str",
		"is_inside_think",
	]
	df = dataset_obj.to_table(columns=columns).to_pandas()
	if dataset is not None:
		df = df[df["dataset"] == dataset]
	if split is not None:
		df = df[df["split"] == split]
	return df


def _safe_entropy_from_probs(probs: np.ndarray) -> float:
	probs = probs[np.isfinite(probs)]
	probs = probs[(probs >= 0.0) & (probs <= 1.0)]
	total = float(probs.sum())
	if total <= 0.0:
		return float("nan")
	probs = probs / total
	tiny = np.finfo(np.float32).tiny
	probs = np.clip(probs, tiny, 1.0)
	return float(-(probs * np.log2(probs)).sum())


def topk_proxy_entropy(row: pd.Series) -> float:
	topk = row.get("draft_topk_probs", None)
	if isinstance(topk, list) and topk:
		probs = []
		for item in topk:
			if isinstance(item, dict) and item.get("prob") is not None:
				probs.append(float(item["prob"]))
		if probs:
			probs_arr = np.asarray(probs, dtype=np.float64)
			mass = float(np.sum(probs_arr[np.isfinite(probs_arr)]))
			if mass > 0.0:
				probs_arr = probs_arr / mass if mass > 1.0 else probs_arr
				entropy = _safe_entropy_from_probs(probs_arr)
				tail_mass = max(0.0, 1.0 - min(mass, 1.0))
				if tail_mass > 0.0:
					entropy += float(-tail_mass * math.log2(tail_mass))
				return entropy
	return float("nan")


def materialize_entropy_series(df: pd.DataFrame, requested_col: str) -> Tuple[pd.DataFrame, str]:
	out = df.copy()
	out["draft_entropy"] = pd.to_numeric(out.get("draft_entropy"), errors="coerce")
	out["target_entropy"] = pd.to_numeric(out.get("target_entropy"), errors="coerce")

	if requested_col in ("draft_entropy", "target_entropy"):
		if out[requested_col].notna().any():
			out["analysis_entropy"] = out[requested_col]
			return out, requested_col
	else:
		if out["draft_entropy"].notna().any():
			out["analysis_entropy"] = out["draft_entropy"]
			return out, "draft_entropy"
		if out["target_entropy"].notna().any():
			out["analysis_entropy"] = out["target_entropy"]
			return out, "target_entropy"

	out["analysis_entropy"] = out.apply(topk_proxy_entropy, axis=1)
	return out, "draft_topk_proxy_entropy"


def contiguous_runs(values: Sequence[int]) -> List[int]:
	if not values:
		return []
	runs: List[int] = []
	last = values[0]
	length = 1
	for value in values[1:]:
		if value == last:
			length += 1
		else:
			runs.append(length)
			last = value
			length = 1
	runs.append(length)
	return runs


def run_lengths_from_states(states: Sequence[int]) -> List[int]:
	return contiguous_runs(list(states))


def compute_n_eff(series: np.ndarray) -> Optional[float]:
	if acf is None:
		return None
	n = int(series.shape[0])
	if n < 3:
		return float(n)
	nlags = min(200, max(1, n // 4))
	rho = acf(series, nlags=nlags, fft=True, missing="drop")
	if rho.shape[0] <= 1:
		return float(n)
	positive = []
	for value in rho[1:]:
		if not np.isfinite(value) or value <= 0:
			break
		positive.append(float(value))
	denom = 1.0 + 2.0 * sum(positive)
	return float(n / denom) if denom > 0 else float(n)


def fit_gmm_bic(series: np.ndarray, seed: int) -> Tuple[float, float, float, bool]:
	x = series.reshape(-1, 1)
	gmm1 = GaussianMixture(n_components=1, covariance_type="full", n_init=5, random_state=seed)
	gmm2 = GaussianMixture(n_components=2, covariance_type="full", n_init=5, random_state=seed)
	gmm1.fit(x)
	gmm2.fit(x)
	bic1 = float(gmm1.bic(x))
	bic2 = float(gmm2.bic(x))
	delta = bic1 - bic2
	return bic1, bic2, delta, bool(delta > 0.0)


def try_silverman_test(series: np.ndarray) -> Tuple[str, Optional[float]]:
	module_names = ["modality", "kjohnsson.modality", "silverman"]
	for module_name in module_names:
		try:
			module = importlib.import_module(module_name)
		except Exception:
			continue
		for attr in (
			"silverman_bwtest",
			"silverman_test",
			"silverman",
			"test",
			"run",
			"bandwidth_test",
		):
			func = getattr(module, attr, None)
			if callable(func):
				try:
					# The modality package requires alpha and can be very expensive with
					# adaptive resampling defaults. Use bounded non-adaptive settings.
					if attr == "silverman_bwtest":
						result = func(np.asarray(series), 0.05, adaptive_resampling=False, N_non_adaptive=200)
					else:
						result = func(series)
				except TypeError:
					try:
						if attr == "silverman_bwtest":
							result = func(np.asarray(series), 0.05, adaptive_resampling=False, N_non_adaptive=200)
						else:
							result = func(np.asarray(series))
					except Exception:
						continue
				except Exception:
					continue
				if isinstance(result, dict):
					pvalue = result.get("pvalue") or result.get("p_value") or result.get("pv")
					if pvalue is not None:
						return f"{module_name}.{attr}", float(pvalue)
				if hasattr(result, "pvalue"):
					return f"{module_name}.{attr}", float(result.pvalue)
				if isinstance(result, (tuple, list)) and len(result) >= 2:
					return f"{module_name}.{attr}", float(result[1])
				if isinstance(result, (int, float)):
					return f"{module_name}.{attr}", float(result)
				return f"{module_name}.{attr}", None
	return "skipped", None


def hmm_num_params(n_states: int, n_features: int = 1, covariance_type: str = "diag") -> int:
	startprob = n_states - 1
	transmat = n_states * (n_states - 1)
	means = n_states * n_features
	if covariance_type == "diag":
		covars = n_states * n_features
	else:
		covars = n_states * int(n_features * (n_features + 1) / 2)
	return startprob + transmat + means + covars


def fit_hmm(series: np.ndarray, n_states: int, seed: int, max_iter: int) -> Optional["GaussianHMM"]:
	if GaussianHMM is None:
		return None
	model = GaussianHMM(
		n_components=n_states,
		covariance_type="diag",
		n_iter=max_iter,
		random_state=seed,
		verbose=False,
	)
	model.fit(series.reshape(-1, 1))
	return model


def hmm_lr_test(series: np.ndarray, seed: int, max_iter: int) -> Tuple[Optional[float], Optional[float], Optional[float], Optional[List[int]]]:
	if GaussianHMM is None:
		return None, None, None, None
	m1 = fit_hmm(series, 1, seed, max_iter)
	m2 = fit_hmm(series, 2, seed, max_iter)
	if m1 is None or m2 is None:
		return None, None, None, None
	ll1 = float(m1.score(series.reshape(-1, 1)))
	ll2 = float(m2.score(series.reshape(-1, 1)))
	lr = 2.0 * (ll2 - ll1)
	df = max(1, hmm_num_params(2) - hmm_num_params(1))
	pvalue = float(scipy_stats.chi2.sf(lr, df))
	states = m2.predict(series.reshape(-1, 1)).astype(int).tolist()
	return ll1, ll2, pvalue, states


def pelt_changepoints(series: np.ndarray, penalty: float) -> Tuple[Optional[List[int]], Optional[List[int]]]:
	if rpt is None or len(series) < 3:
		return None, None
	algo = rpt.Pelt(model="rbf").fit(series)
	cps = algo.predict(pen=penalty)
	if not cps:
		return None, None
	seg_lengths: List[int] = []
	start = 0
	for cp in cps:
		seg_lengths.append(int(cp - start))
		start = cp
	return [int(cp) for cp in cps], seg_lengths


def run_length_ks_test(states: Sequence[int]) -> Tuple[Optional[float], Optional[float]]:
	run_lengths = run_lengths_from_states(states)
	if len(run_lengths) < 2:
		return None, None
	mean_len = float(np.mean(run_lengths))
	if mean_len <= 1.0:
		return None, None
	p = min(max(1.0 / mean_len, 1e-6), 1.0 - 1e-6)
	sample = np.asarray(run_lengths, dtype=np.float64)
	ks = scipy_stats.kstest(sample, scipy_stats.geom(p).cdf)
	return float(ks.statistic), float(ks.pvalue)


def choose_block_length(series: np.ndarray) -> float:
	if optimal_block_length is None:
		return max(2.0, math.sqrt(len(series)))
	try:
		tbl = optimal_block_length(series)
		for key in ("stationary", "circular"):
			if key in tbl.columns:
				value = float(tbl[key].iloc[0])
				if np.isfinite(value) and value > 0:
					return value
		first = float(tbl.iloc[0, 0])
		if np.isfinite(first) and first > 0:
			return first
	except Exception:
		pass
	return max(2.0, math.sqrt(len(series)))


def simulate_ar_surrogate(series: np.ndarray, seed: int, max_lag: int) -> Optional[np.ndarray]:
	if AutoReg is None or len(series) < 5:
		return None
	rng = np.random.default_rng(seed)
	best_fit = None
	best_aic = float("inf")
	best_lag = 1
	upper = min(max_lag, max(1, len(series) // 5))
	for lag in range(1, upper + 1):
		try:
			fit = AutoReg(series, lags=lag, old_names=False).fit()
		except Exception:
			continue
		if fit.aic < best_aic:
			best_aic = float(fit.aic)
			best_fit = fit
			best_lag = lag
	if best_fit is None:
		return None

	params = np.asarray(best_fit.params, dtype=np.float64)
	intercept = float(params[0]) if params.size else 0.0
	phi = np.asarray(params[1:], dtype=np.float64)
	sigma = float(np.sqrt(getattr(best_fit, "sigma2", np.var(best_fit.resid, ddof=1))))
	sigma = max(sigma, 1e-8)

	values = list(np.asarray(series[:best_lag], dtype=np.float64))
	while len(values) < len(series):
		lagged = values[-best_lag:][::-1]
		if len(lagged) < best_lag:
			lagged = [values[0]] * (best_lag - len(lagged)) + lagged
		pred = intercept + float(np.dot(phi[:best_lag], np.asarray(lagged, dtype=np.float64)))
		values.append(float(pred + rng.normal(0.0, sigma)))
	return np.asarray(values[: len(series)], dtype=np.float64)


def simulate_hmm_surrogate(series: np.ndarray, seed: int, max_iter: int) -> Optional[np.ndarray]:
	if GaussianHMM is None:
		return None
	model = fit_hmm(series, 1, seed, max_iter)
	if model is None:
		return None
	try:
		samples, _ = model.sample(len(series), random_state=seed)
		return samples[:, 0].astype(np.float64)
	except Exception:
		return None


def dip_stat(series: np.ndarray) -> Optional[Tuple[float, float]]:
	if diptest is None or len(series) < 2:
		return None
	try:
		stat, pvalue = diptest(np.asarray(series, dtype=np.float64))
		return float(stat), float(pvalue)
	except Exception:
		return None


def stationary_bootstrap_dip(series: np.ndarray, seed: int, reps: int) -> Tuple[Optional[float], Optional[float]]:
	if StationaryBootstrap is None or diptest is None or len(series) < 4:
		return None, None
	block_len = choose_block_length(series)
	rng = np.random.default_rng(seed)
	values = []
	try:
		bs = StationaryBootstrap(block_len, series)
		for idx, data in enumerate(bs.bootstrap(reps)):
			if idx >= reps:
				break
			sample = np.asarray(data[0][0], dtype=np.float64)
			if len(sample) < 2:
				continue
			stat = diptest(sample)[0]
			values.append(float(stat))
	except Exception:
		# fallback to a basic i.i.d. resample if bootstrap internals differ
		for _ in range(reps):
			sample = rng.choice(series, size=len(series), replace=True)
			values.append(float(diptest(sample)[0]))
	if not values:
		return None, None
	observed = diptest(series)[0]
	values_arr = np.asarray(values, dtype=np.float64)
	pvalue = float((np.sum(values_arr >= observed) + 1.0) / (len(values_arr) + 1.0))
	return float(values_arr.mean()), pvalue


def ar_surrogate_dip(series: np.ndarray, seed: int, reps: int, max_lag: int) -> Tuple[Optional[float], Optional[float]]:
	if diptest is None:
		return None, None
	values = []
	for rep in range(reps):
		surrogate = simulate_ar_surrogate(series, seed + rep + 1, max_lag)
		if surrogate is None or len(surrogate) < 2:
			continue
		values.append(float(diptest(surrogate)[0]))
	if not values:
		return None, None
	observed = diptest(series)[0]
	values_arr = np.asarray(values, dtype=np.float64)
	pvalue = float((np.sum(values_arr >= observed) + 1.0) / (len(values_arr) + 1.0))
	return float(values_arr.mean()), pvalue


def hmm_surrogate_dip(series: np.ndarray, seed: int, reps: int, max_iter: int) -> Tuple[Optional[float], Optional[float]]:
	if diptest is None:
		return None, None
	values = []
	for rep in range(reps):
		surrogate = simulate_hmm_surrogate(series, seed + rep + 1, max_iter)
		if surrogate is None or len(surrogate) < 2:
			continue
		values.append(float(diptest(surrogate)[0]))
	if not values:
		return None, None
	observed = diptest(series)[0]
	values_arr = np.asarray(values, dtype=np.float64)
	pvalue = float((np.sum(values_arr >= observed) + 1.0) / (len(values_arr) + 1.0))
	return float(values_arr.mean()), pvalue


def is_cue_token(token: str) -> bool:
	if token is None:
		return False
	return bool(re.fullmatch(r"\s+", token) or re.fullmatch(r"[\n\t\r]+", token) or re.fullmatch(r"[=\$\,\.\:\;\(\)\[\]\{\}<>\-\+\*/\\]+", token) or re.fullmatch(r"\d+(?:\.\d+)?", token))


def longest_think_span(group: pd.DataFrame) -> pd.DataFrame:
	if "is_inside_think" not in group.columns:
		return group
	mask = group["is_inside_think"].fillna(False).astype(bool).to_numpy()
	best_start = best_end = None
	current_start = None
	for idx, flag in enumerate(mask):
		if flag and current_start is None:
			current_start = idx
		elif not flag and current_start is not None:
			if best_start is None or (idx - current_start) > (best_end - best_start):
				best_start, best_end = current_start, idx
			current_start = None
	if current_start is not None:
		if best_start is None or (len(mask) - current_start) > (best_end - best_start):
			best_start, best_end = current_start, len(mask)
	if best_start is None:
		return group.iloc[0:0].copy()
	return group.iloc[best_start:best_end].copy()


def build_view_trace(group: pd.DataFrame, view: str) -> pd.DataFrame:
	trace = group.sort_values(["position", "step"], kind="stable").copy()
	if view == "raw":
		return trace
	if view == "masked":
		if "token_str" in trace.columns:
			trace = trace[~trace["token_str"].fillna("").map(is_cue_token)]
		return trace
	if view == "think_only":
		return longest_think_span(trace)
	raise ValueError(f"Unknown view: {view}")


def plot_dip_histograms(all_metrics: pd.DataFrame, out_path: Path) -> None:
	if all_metrics.empty:
		return
	views = list(all_metrics["view"].dropna().unique())
	fig, axes = plt.subplots(len(views), 1, figsize=(10, 4 * len(views)), squeeze=False)
	for row_idx, view in enumerate(views):
		ax = axes[row_idx][0]
		subset = all_metrics[(all_metrics["view"] == view) & all_metrics["dip_stat"].notna()]
		if subset.empty:
			ax.set_title(f"{view}: no dip stats")
			continue
		ax.hist(subset["dip_stat"], bins=20, alpha=0.75, color="#4477aa")
		ax.axvline(subset["dip_stat"].median(), color="black", linestyle="--", linewidth=1, label="median dip")
		ax.set_title(f"{view}: per-trace dip statistics")
		ax.set_xlabel("dip statistic")
		ax.set_ylabel("count")
		ax.legend(loc="best")
	fig.tight_layout()
	fig.savefig(out_path, dpi=160)
	plt.close(fig)


def plot_example_traces(example_rows: List[Dict[str, object]], out_path: Path) -> None:
	if not example_rows:
		return
	fig, axes = plt.subplots(len(example_rows), 1, figsize=(12, 4 * len(example_rows)), squeeze=False)
	for idx, row in enumerate(example_rows):
		ax = axes[idx][0]
		series = np.asarray(row["series"], dtype=np.float64)
		probs = np.asarray(row["hmm_posteriors"], dtype=np.float64) if row.get("hmm_posteriors") is not None else None
		ax.plot(series, label="entropy", color="#4477aa")
		if probs is not None and probs.ndim == 2 and probs.shape[1] >= 2:
			ax2 = ax.twinx()
			ax2.plot(probs[:, 1], label="HMM phase posterior", color="#cc6677", alpha=0.8)
			ax2.set_ylim(0, 1)
			ax2.set_ylabel("phase posterior")
			handles2, labels2 = ax2.get_legend_handles_labels()
		else:
			handles2, labels2 = ([], [])
		if row.get("changepoints"):
			for cp in row["changepoints"]:
				ax.axvline(int(cp) - 0.5, color="#ddcc77", linestyle=":", linewidth=1)
		ax.set_title(f"{row['view']} | {row['run_id']} | {row['dataset']} | {row['problem_id']}")
		ax.set_xlabel("position")
		ax.set_ylabel("entropy")
		handles, labels = ax.get_legend_handles_labels()
		ax.legend(handles + handles2, labels + labels2, loc="best")
	fig.tight_layout()
	fig.savefig(out_path, dpi=160)
	plt.close(fig)


def analyze_trace(
	trace_df: pd.DataFrame,
	view: str,
	seed: int,
	n_surrogates: int,
	bootstrap_reps: int,
	ar_max_lag: int,
	hmm_max_iter: int,
	pelt_penalty: float,
) -> Tuple[Optional[TraceMetric], Optional[Dict[str, object]]]:
	if trace_df.empty:
		return None, None

	trace_df = trace_df.sort_values(["position", "step"], kind="stable")
	series = pd.to_numeric(trace_df["analysis_entropy"], errors="coerce").to_numpy(dtype=np.float64)
	series = series[np.isfinite(series)]
	if len(series) < 2:
		return None, None

	dip = dip_stat(series)
	if dip is None:
		dip_stat_value = dip_pvalue = None
	else:
		dip_stat_value, dip_pvalue = dip

	try:
		gmm1_bic, gmm2_bic, delta_bic, prefer_2 = fit_gmm_bic(series, seed)
	except Exception:
		gmm1_bic = gmm2_bic = delta_bic = None
		prefer_2 = None

	silverman_status, silverman_pvalue = try_silverman_test(series)
	n_eff = compute_n_eff(series)

	hmm_ll1 = hmm_ll2 = hmm_lr_pvalue = None
	hmm_states = None
	if len(series) >= 5:
		try:
			hmm_ll1, hmm_ll2, hmm_lr_pvalue, hmm_states = hmm_lr_test(series, seed, hmm_max_iter)
		except Exception:
			hmm_ll1 = hmm_ll2 = hmm_lr_pvalue = None
			hmm_states = None

	changepoints, seg_lengths = pelt_changepoints(series, pelt_penalty) if len(series) >= 3 else (None, None)
	run_ks_stat = run_ks_pvalue = None
	if hmm_states is not None:
		try:
			run_ks_stat, run_ks_pvalue = run_length_ks_test(hmm_states)
		except Exception:
			run_ks_stat = run_ks_pvalue = None

	block_mean = block_pvalue = None
	ar_mean = ar_pvalue = None
	hmm_sur_mean = hmm_sur_pvalue = None

	if dip_stat is not None:
		try:
			block_mean, block_pvalue = stationary_bootstrap_dip(series, seed, bootstrap_reps)
		except Exception:
			block_mean = block_pvalue = None
		try:
			ar_mean, ar_pvalue = ar_surrogate_dip(series, seed, n_surrogates, ar_max_lag)
		except Exception:
			ar_mean = ar_pvalue = None
		try:
			hmm_sur_mean, hmm_sur_pvalue = hmm_surrogate_dip(series, seed, n_surrogates, hmm_max_iter)
		except Exception:
			hmm_sur_mean = hmm_sur_pvalue = None

	metric = TraceMetric(
		view=view,
		run_id=str(trace_df["run_id"].iloc[0]),
		dataset=str(trace_df["dataset"].iloc[0]),
		problem_id=str(trace_df["problem_id"].iloc[0]),
		n_tokens=int(len(series)),
		entropy_source=str(trace_df.attrs.get("entropy_source", "unknown")),
		dip_stat=float(dip_stat_value) if dip_stat_value is not None else None,
		dip_pvalue=float(dip_pvalue) if dip_pvalue is not None else None,
		gmm_delta_bic=float(delta_bic) if delta_bic is not None else None,
		gmm_prefer_2=bool(prefer_2) if prefer_2 is not None else None,
		silverman_status=silverman_status,
		silverman_pvalue=float(silverman_pvalue) if silverman_pvalue is not None else None,
		n_eff=float(n_eff) if n_eff is not None else None,
		hmm_ll_1=float(hmm_ll1) if hmm_ll1 is not None else None,
		hmm_ll_2=float(hmm_ll2) if hmm_ll2 is not None else None,
		hmm_lr_stat=float(2.0 * (hmm_ll2 - hmm_ll1)) if hmm_ll1 is not None and hmm_ll2 is not None else None,
		hmm_lr_pvalue=float(hmm_lr_pvalue) if hmm_lr_pvalue is not None else None,
		hmm_states=hmm_states,
		pelt_changepoints=changepoints,
		pelt_segment_lengths=seg_lengths,
		run_length_ks_stat=float(run_ks_stat) if run_ks_stat is not None else None,
		run_length_ks_pvalue=float(run_ks_pvalue) if run_ks_pvalue is not None else None,
		block_bootstrap_dip_mean=float(block_mean) if block_mean is not None else None,
		block_bootstrap_dip_pvalue=float(block_pvalue) if block_pvalue is not None else None,
		ar_surrogate_dip_mean=float(ar_mean) if ar_mean is not None else None,
		ar_surrogate_dip_pvalue=float(ar_pvalue) if ar_pvalue is not None else None,
		hmm_surrogate_dip_mean=float(hmm_sur_mean) if hmm_sur_mean is not None else None,
		hmm_surrogate_dip_pvalue=float(hmm_sur_pvalue) if hmm_sur_pvalue is not None else None,
	)

	extra = {
		"series": series.tolist(),
		"hmm_posteriors": None,
		"changepoints": changepoints,
		"view": view,
		"run_id": metric.run_id,
		"dataset": metric.dataset,
		"problem_id": metric.problem_id,
	}
	if hmm_states is not None and GaussianHMM is not None:
		try:
			hmm_model = fit_hmm_from_series(series, seed, hmm_max_iter)
			if hmm_model is not None:
				extra["hmm_posteriors"] = hmm_model.predict_proba(series.reshape(-1, 1)).tolist()
		except Exception:
			extra["hmm_posteriors"] = None

	return metric, extra


def fit_hmm_from_series(series: np.ndarray, seed: int, hmm_max_iter: int) -> Optional["GaussianHMM"]:
	if GaussianHMM is None:
		return None
	model = GaussianHMM(
		n_components=2,
		covariance_type="diag",
		n_iter=hmm_max_iter,
		random_state=seed,
		verbose=False,
	)
	model.fit(series.reshape(-1, 1))
	return model


def summarize_view(metrics: pd.DataFrame) -> Dict[str, object]:
	if metrics.empty:
		return {"n_traces": 0}
	summary = {
		"n_traces": int(len(metrics)),
		"dip_reject_fraction": float((metrics["dip_pvalue"].notna() & (metrics["dip_pvalue"] < 0.05)).mean()) if metrics["dip_pvalue"].notna().any() else None,
		"gmm_prefer_2_fraction": float(metrics["gmm_prefer_2"].mean()) if metrics["gmm_prefer_2"].notna().any() else None,
		"dip_stat_median": float(metrics["dip_stat"].median()) if metrics["dip_stat"].notna().any() else None,
		"delta_bic_median": float(metrics["gmm_delta_bic"].median()) if metrics["gmm_delta_bic"].notna().any() else None,
		"n_eff_median": float(metrics["n_eff"].median()) if metrics["n_eff"].notna().any() else None,
		"hmm_lr_reject_fraction": float((metrics["hmm_lr_pvalue"].notna() & (metrics["hmm_lr_pvalue"] < 0.05)).mean()) if metrics["hmm_lr_pvalue"].notna().any() else None,
	}
	return summary


def write_markdown_report(
	out_dir: Path,
	corpus_path: Path,
	entropy_source: str,
	view_summaries: Dict[str, Dict[str, object]],
	args: argparse.Namespace,
) -> None:
	lines: List[str] = []
	lines.append("# H1 Results")
	lines.append("")
	lines.append("## Config")
	lines.append("")
	lines.append(f"- corpus_path: {corpus_path}")
	lines.append(f"- entropy_source: {entropy_source}")
	lines.append(f"- dataset_filter: {args.dataset}")
	lines.append(f"- split_filter: {args.split}")
	lines.append(f"- min_trace_len: {args.min_trace_len}")
	lines.append(f"- n_surrogates: {args.n_surrogates}")
	lines.append(f"- bootstrap_reps: {args.bootstrap_reps}")
	lines.append(f"- ar_max_lag: {args.ar_max_lag}")
	lines.append(f"- pelt_penalty: {args.pelt_penalty}")
	lines.append("")
	lines.append("## View Summary")
	lines.append("")
	lines.append("| view | n_traces | dip_reject_fraction | gmm_prefer_2_fraction | dip_stat_median | delta_bic_median | n_eff_median | hmm_lr_reject_fraction |")
	lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
	for view, summary in view_summaries.items():
		lines.append(
			f"| {view} | {summary.get('n_traces', 0)} | {summary.get('dip_reject_fraction')} | {summary.get('gmm_prefer_2_fraction')} | "
			f"{summary.get('dip_stat_median')} | {summary.get('delta_bic_median')} | {summary.get('n_eff_median')} | {summary.get('hmm_lr_reject_fraction')} |"
		)
	lines.append("")
	lines.append("## Interpretation")
	lines.append("")
	lines.append("- `raw` is the primary H1 analysis view.")
	lines.append("- `masked` reruns H1 after removing formatting/cue tokens.")
	lines.append("- `think_only` reruns H1 on the longest contiguous `<think>` span.")
	lines.append("- Silverman testing is included as a hook and will be marked skipped if the package API is unavailable.")
	lines.append("")

	with open(out_dir / "H1_results.md", "w", encoding="utf-8") as fh:
		fh.write("\n".join(lines) + "\n")


def main() -> None:
	args = parse_args()
	np.random.seed(args.random_seed)

	corpus_path = resolve_corpus_path(args.corpus_path)
	out_dir = Path(args.out_dir)
	out_dir.mkdir(parents=True, exist_ok=True)

	df = load_corpus(corpus_path, args.dataset, args.split)
	df, entropy_source = materialize_entropy_series(df, args.entropy_col)
	df = df[df["analysis_entropy"].notna()].copy()
	df["entropy_source"] = entropy_source

	trace_groups = list(df.groupby("run_id", sort=False))
	if args.max_traces is not None:
		trace_groups = trace_groups[: args.max_traces]

	view_names = ["raw", "masked", "think_only"]
	all_metrics: List[TraceMetric] = []
	view_summaries: Dict[str, Dict[str, object]] = {}
	example_traces: List[Dict[str, object]] = []

	for view in view_names:
		view_metrics: List[Dict[str, object]] = []
		for run_id, group in trace_groups:
			group = group.copy()
			group.attrs["entropy_source"] = entropy_source
			trace_view = build_view_trace(group, view)
			if len(trace_view) < args.min_trace_len:
				continue
			trace_view = trace_view.copy()
			trace_view.attrs["entropy_source"] = entropy_source
			metric, extra = analyze_trace(
				trace_view,
				view=view,
				seed=args.random_seed,
				n_surrogates=args.n_surrogates,
				bootstrap_reps=args.bootstrap_reps,
				ar_max_lag=args.ar_max_lag,
				hmm_max_iter=args.hmm_max_iter,
				pelt_penalty=args.pelt_penalty,
			)
			if metric is None:
				continue
			all_metrics.append(metric)
			row = asdict(metric)
			row["hmm_states"] = json.dumps(metric.hmm_states) if metric.hmm_states is not None else None
			row["pelt_changepoints"] = json.dumps(metric.pelt_changepoints) if metric.pelt_changepoints is not None else None
			row["pelt_segment_lengths"] = json.dumps(metric.pelt_segment_lengths) if metric.pelt_segment_lengths is not None else None
			view_metrics.append(row)
			if view == "raw" and len(example_traces) < 3 and extra is not None:
				example_traces.append(extra)

		view_df = pd.DataFrame(view_metrics)
		view_df.to_csv(out_dir / f"{view}_trace_metrics.csv", index=False)
		view_summaries[view] = summarize_view(view_df)

	metrics_df = pd.DataFrame([{
		**asdict(metric),
		"hmm_states": json.dumps(metric.hmm_states) if metric.hmm_states is not None else None,
		"pelt_changepoints": json.dumps(metric.pelt_changepoints) if metric.pelt_changepoints is not None else None,
		"pelt_segment_lengths": json.dumps(metric.pelt_segment_lengths) if metric.pelt_segment_lengths is not None else None,
	} for metric in all_metrics])
	metrics_df.to_csv(out_dir / "all_trace_metrics.csv", index=False)

	with open(out_dir / "view_summaries.json", "w", encoding="utf-8") as fh:
		json.dump(view_summaries, fh, indent=2)

	write_markdown_report(out_dir, corpus_path, entropy_source, view_summaries, args)
	plot_dip_histograms(metrics_df, out_dir / "dip_histograms.png")
	plot_example_traces(example_traces, out_dir / "example_traces.png")


if __name__ == "__main__":
	main()
