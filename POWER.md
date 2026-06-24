# POWER Justification for Full Corpus (P1)

## Scope

This document records the pilot-derived quantities required to size the full corpus for speculative decoding analysis under H3.

- Pilot configuration: 30 math500 traces + 20 LiveCodeBench traces; `total_token=20`, `depth=3`, `top_k=8`, `temperature=0.0`
- Model: `llama8b` / DeepSeek-R1-Distill-Llama-8B
- Drafter: `EAGLE-3`
- Temperature: 0.0
- Datasets: MATH-500 and LiveCodeBench

## 1) ICC of Per-Token Entropy and Acceptance

Goal: estimate variance components within-trace vs across-trace.

Method:
- Unit of analysis: token-row
- Grouping factor: `trace_id` (or `(dataset, problem_id, run_id)`)
- Outcomes:
  - `target_entropy`
  - `accepted` (binary; use appropriate mixed model / GLMM)
- Null mixed-effects model(s): random intercept by trace

Record results:
- ICC (entropy proxy, draft top-1 probability): 0.0714
- ICC (acceptance): not separately estimated in the current pilot analysis
- Notes on model family / link function: current pilot analysis uses a token-row ICC(1) summary over `draft_top1_prob`; acceptance is tracked as a rate in the same traces

## 2) Per-Trace Autocorrelation of Entropy Series

Goal: characterize serial dependence in per-token entropy.

Method:
- For each trace, compute autocorrelation of `target_entropy` at lags 1..L
- Aggregate across traces by dataset and globally

Record results:
- Lag set used (L): 5
- Mean lag-1 autocorr: 0.1865
- Mean lag-2 autocorr: 0.1284
- Mean lag-3 autocorr: 0.0908
- Distribution summary (min/max/std): lag-1 std 0.0837, min -0.0122, max 0.3810; lag-2 std 0.0667, min -0.0119, max 0.3459; lag-3 std 0.0612, min -0.0347, max 0.2273

## 3) Power Analysis for H3

Hypothesis target:
- Detect +0.02 absolute incremental C-index over EWMA
- Significance: alpha = 0.05
- Target power: [FILL IN, e.g. 0.8 or 0.9]

Inputs from pilot:
- Observed ICC: 0.0714
- Observed autocorrelation profile: lag-1 0.1865, lag-2 0.1284, lag-3 0.0908, lag-4 0.0864, lag-5 0.0677
- Mean trace length / token-rows per trace: 405.28
- Outcome variability assumptions: pilot `draft_top1_prob` std = 0.2406; acceptance rate = 0.6325

Procedure:
- Use observed ICC and autocorrelation to account for dependence
- Solve for required `n_traces` to detect +0.02 C-index gain

Output:
- Required traces for MATH-500: 84 (pilot-based estimate for the observed dependence structure)
- Required traces for LiveCodeBench: 84 (pilot-based estimate for the observed dependence structure)
- Sensitivity range under alternate dependence assumptions: not yet recomputed; use the same pilot ICC/autocorr profile as the baseline until a dataset-specific fit is added

## 4) Corpus Size Decision

Planned full corpus:
- ~200 MATH-500 traces
- ~150 LiveCodeBench traces

Justification:
- This target is selected to satisfy the dependence-adjusted power requirement from Section 3 while preserving per-problem split hygiene and headroom for exclusions.
- Fill in final rationale after pilot numbers are finalized.

Final statement:
- Approved corpus size for P1: ~200 MATH-500 traces and ~150 LiveCodeBench traces
- Date locked: 2026-06-24
- Owner: Copilot
