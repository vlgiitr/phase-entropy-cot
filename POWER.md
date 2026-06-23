# POWER Justification for Full Corpus (P1)

## Scope

This document records the pilot-derived quantities required to size the full corpus for speculative decoding analysis under H3.

- Pilot configuration: [FILL IN]
- Model: [FILL IN]
- Drafter: [FILL IN]
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
- ICC (entropy): [FILL IN]
- ICC (acceptance): [FILL IN]
- Notes on model family / link function: [FILL IN]

## 2) Per-Trace Autocorrelation of Entropy Series

Goal: characterize serial dependence in per-token entropy.

Method:
- For each trace, compute autocorrelation of `target_entropy` at lags 1..L
- Aggregate across traces by dataset and globally

Record results:
- Lag set used (L): [FILL IN]
- Mean lag-1 autocorr: [FILL IN]
- Mean lag-2 autocorr: [FILL IN]
- Mean lag-3 autocorr: [FILL IN]
- Distribution summary (min/max/std): [FILL IN]

## 3) Power Analysis for H3

Hypothesis target:
- Detect +0.02 absolute incremental C-index over EWMA
- Significance: alpha = 0.05
- Target power: [FILL IN, e.g. 0.8 or 0.9]

Inputs from pilot:
- Observed ICC: [FILL IN]
- Observed autocorrelation profile: [FILL IN]
- Mean trace length / token-rows per trace: [FILL IN]
- Outcome variability assumptions: [FILL IN]

Procedure:
- Use observed ICC and autocorrelation to account for dependence
- Solve for required `n_traces` to detect +0.02 C-index gain

Output:
- Required traces for MATH-500: [FILL IN]
- Required traces for LiveCodeBench: [FILL IN]
- Sensitivity range under alternate dependence assumptions: [FILL IN]

## 4) Corpus Size Decision

Planned full corpus:
- ~200 MATH-500 traces
- ~150 LiveCodeBench traces

Justification:
- This target is selected to satisfy the dependence-adjusted power requirement from Section 3 while preserving per-problem split hygiene and headroom for exclusions.
- Fill in final rationale after pilot numbers are finalized.

Final statement:
- Approved corpus size for P1: [FILL IN]
- Date locked: [FILL IN]
- Owner: [FILL IN]
