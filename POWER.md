# POWER Justification for Full Corpus (P1)

## Scope

This document records the pilot-derived quantities used to size the full corpus for speculative decoding analysis under H3.

- Pilot configuration: P1.2 pilot run via `tools/pilot_run.py`
- Target model: DeepSeek-R1-Distill-LLaMA-8B
- Drafter: EAGLE-3 head (`yuhuili/EAGLE3-DeepSeek-R1-Distill-LLaMA-8B`)
- Temperature: 0.0 (greedy)
- Datasets: MATH-500 and LiveCodeBench
- Pilot traces: 50 total (30 MATH-500, 20 LiveCodeBench)
- Pilot success: 50/50 traces

## 1) ICC of Per-Token Signal and Acceptance

Goal: estimate within-trace vs across-trace dependence to inform effective sample size.

Method:
- Unit of analysis: token-row
- Grouping factor: trace/run
- Pilot implementation proxy: ICC on draft top-1 probability (`icc1_top1_p`) from pilot analysis artifact
- Acceptance dependence handled through design-effect adjustment in power calculation

Results from pilot (`repos/EAGLE/pilot_traces/analysis.json`):
- ICC proxy (top1 probability): 0.07138360215402388
- Groups (traces): 50
- N token rows used for ICC proxy: 20264
- Mean rows/trace (`kbar`): 405.28

Notes:
- This POWER sizing pass used the pilot ICC proxy together with empirical autocorrelation and cluster design effect.
- A full mixed-effects ICC table for target entropy and binary acceptance can be added as a follow-on, but corpus sizing already had sufficient margin with the pilot proxy approach.

## 2) Per-Trace Autocorrelation of Entropy Series

Goal: characterize serial dependence in per-token entropy process.

Method:
- Per trace, compute autocorrelation at lags 1..5
- Aggregate summaries across traces

Results from pilot (`repos/EAGLE/pilot_traces/analysis.json`):
- Lag set used: L = 5
- Mean lag-1 autocorr: 0.18650242452823812
- Mean lag-2 autocorr: 0.12841127486608875
- Mean lag-3 autocorr: 0.09080058573760769
- Mean lag-4 autocorr: 0.08642956171882432
- Mean lag-5 autocorr: 0.06774243222140193

Distribution summary (min/max/std by lag):
- Lag 1: min -0.012243074350792577, max 0.3809998495843796, std 0.08369287654449889
- Lag 2: min -0.011917621789382084, max 0.345942936885833, std 0.06673123789987631
- Lag 3: min -0.03471907525855084, max 0.2272824623026456, std 0.06116978840390785
- Lag 4: min -0.12115343421015591, max 0.25003904552986056, std 0.0659371329312051
- Lag 5: min -0.11360880703860121, max 0.23967110484323945, std 0.06731001468651605

## 3) Power Analysis for H3

Hypothesis target:
- Detect +0.02 absolute incremental C-index over EWMA baseline
- Significance: alpha = 0.05
- Target power: 0.8

Inputs from pilot (`repos/EAGLE/pilot_traces/analysis.json`):
- Observed ICC proxy: 0.07138360215402388
- Observed autocorrelation profile: positive short-lag dependence (means: 0.1865, 0.1284, 0.0908, 0.0864, 0.0677)
- Mean trace length: 405.28 token rows/trace
- Design effect (dependence-adjusted): 29.858962678828775

Computed power output (pilot artifact):
- Required effective token rows (independent-equivalent): 1135.0634821655417
- Estimated required traces: 84

Allocation decision for full corpus:
- MATH-500 target: 200 traces
- LiveCodeBench target: 150 traces
- Total target: 350 traces

Rationale:
- Planned N (350 traces) is well above pilot-estimated requirement (84 traces), providing headroom for split integrity, exclusions, heterogeneity, and uncertainty in effect transport from pilot to full corpus.

## 4) Corpus Size Decision

Final approved corpus size:
- 200 MATH-500 traces
- 150 LiveCodeBench traces
- 350 traces total

Observed final corpus (for confirmation):
- 350 traces generated
- 236,235 token rows
- Split by problem_id locked at calibration/validation/test = 175/87/88 traces

Final statement:
- Approved corpus size for P1: 350 traces (200 MATH-500 + 150 LiveCodeBench)
- Date locked: 2026-07-10
- Owner: phase-structured entropy implementation track
