# PHASES — Phase-Structured Entropy in CoT



---

## P0 · Setup & reproduction · Wk 1–2

**Goal.** A working environment, the EAGLE/Spec-Bench harness reproducing a
published number to ±5%, and a finalized related-work delta.
**Serves.** Pre-condition for everything downstream.

### P0.1 Environment
- [ ] Create conda env `specdec` with: `pytorch (CUDA 12.x)`, `transformers`,
  `accelerate`, `bitsandbytes` (for AWQ stretch), `pandas`, `pyarrow`,
  `numpy`, `scipy`, `scikit-learn`, `matplotlib`, `seaborn`
- [ ] Stats packages: `diptest` (Hartigan), `hmmlearn` (Gaussian HMM),
  `ruptures` (PELT changepoint), `arch` (block bootstrap),
  `statsmodels` (GLM cloglog, MixedLM, multitest Holm/BH),
  `lifelines` (survival, C-index), `patsy` (splines), `kjohnsson/modality`
  (Silverman bandwidth test — install from GitHub)
- [ ] Slurm templates under `slurm/`: `gpu.sbatch` (cpus=4, mem=16G, gres=gpu:1)
  and `cpu.sbatch` (cpus=2, mem=8G) for analysis jobs
- [ ] Confirm GPU access on vitallab2; `nvidia-smi` from a Slurm job

### P0.2 Repos & models
- [ ] Clone `SafeAILab/EAGLE` into `repos/EAGLE`
- [ ] Clone `hemingkx/Spec-Bench` into `repos/Spec-Bench`
- [ ] (Fallback) Clone `pytorch-labs/gpt-fast` into `repos/gpt-fast`
- [ ] Download into `models/`:
  - `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` (primary target, ~15 GB bf16)
  - `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` (drafter)
  - `AngelSlim/Qwen3-8B_eagle3` (EAGLE-3 head, second drafter)
  - `AngelSlim/Qwen3-1.7B_eagle3` (companion EAGLE head for Qwen3-8B target)
- [ ] Verify memory fit on 1×A6000 (48 GB) with KV budget for **32k-token** CoT
  (R1-distill can stretch this long); document headroom

### P0.3 Reproduction
- [ ] Run vanilla EAGLE-2 or EAGLE-3 on Spec-Bench with their default model;
  reproduce a published τ (acceptance length) within ±5%
- [ ] Repeat on R1-Distill-7B + 1.5B drafter on MATH-500 (20 problems) at T=0;
  log τ baseline for our setting
- [ ] **Gate proof:** reproduction table committed to `results/p0_repro.md`

### P0.4 Reading + delta
Tier-1 (read in full, write 3-line digest each: mechanism / what's new / our delta):
- [ ] **SpecKV** 2605.02888 (ρ≈+0.56 within-trace draft entropy) — H2 anchor
- [ ] **Acceptance Dynamics** 2604.14682 (ρ≈−0.18 across domains, "chat paradox") — H2 anchor
- [ ] **HeteroSpec** 2505.13254 (~5.36×, closest memoryless joint controller) — primary baseline
- [ ] **AdaEDL** 2410.18351 (`1−√(γ·H)` rule) — secondary baseline
- [ ] **SVIP** 2411.18462 (Pinsker bound on reasoning, +22% on QwQ@8K) — secondary baseline
- [ ] **Beyond 80/20** 2506.01939 (forking tokens) — empirical basis for C1
- [ ] **PEAR** 2510.08026 + **EDRM** 2605.22873 (named phase entropy / regime transition) — phase concept
- [ ] **EAGLE-2** 2406.16858 + **EAGLE-3** 2503.01840 — drafter base
- [ ] **AdaEAGLE** 2412.18910 (~29% adaptive-length oracle gap) — net-of-length-oracle benchmark
- [ ] **EQSPEC** 2510.22876 (lossless audit, ~95% equivalence) — losslessness bar
- [ ] **SemanticSpec / Beyond Tokens** 2602.03708 — analysis-only hidden-state probe precedent
- [ ] Tier-2 skim (Attention Drift 2605.09992, DSDE 2509.01083, TALON 2601.07353,
  SAGE 2602.00523, GOOSE 2604.02047)
- [ ] Write `RELATED_WORK.md` — 2-page extended related work; also paper-§related-work draft

### P0 Exit gate
1. Reproduction within ±5%
2. Tier-1 reading digests committed
3. 1-paragraph novelty statement vs each Tier-1 paper

---

## P1 · Instrumentation, corpus & power · Wk 2–3

**Goal.** Patched decoder that logs per-token forensics; corpus sized by a
pilot ICC power analysis; calibration/validation/test split locked before any
analysis runs.
**Serves.** H1–H4 (the corpus is the empirical foundation).

### P1.1 Decoder patch
- [ ] Identify the per-token logging point in `EAGLE/eagle/model/ea_model.py`
  inside the verify/draft loop
- [ ] Patch to append, per accepted-or-rejected position:
  - `run_id, problem_id, model_name, drafter_name, temperature`
  - `position` (global token index from prompt end)
  - `token_id, token_str`
  - `target_entropy` (Shannon, in bits, on full softmax)
  - `draft_entropy` (same on drafter logits)
  - `draft_top1_prob`
  - `draft_topk_probs` (k=32; controlled via flag for top-k sensitivity)
  - `accepted` (bool)
  - `tree_depth_at_accept` (int)
  - `is_inside_think` (bool — flips on `<think>` / `</think>` token ids)
  - `phase_label_hmm` (filled later in P2, left null at logging)
- [ ] Sanity-test on 5 sample MATH-500 traces; eyeball entropy time series
- [ ] Confirm logging adds ≤10% overhead (we don't need this to be production-fast,
  but the same code generates the analysis dataset *and* later runs the controller)

### P1.2 Pilot run + power
- [ ] Generate **pilot corpus**: 30 MATH-500 + 20 LiveCodeBench traces on
  R1-Distill-7B at T=0 (≈50 traces, ~100–300k token-rows)
- [ ] Compute **ICC** of per-token entropy and acceptance: variance-within-trace
  vs variance-across-trace (via `statsmodels` MixedLM null model)
- [ ] **Power analysis** for H3: simulate target effect size = +0.02 absolute
  incremental C-index over EWMA at α=0.05 with the observed ICC and per-trace
  autocorrelation; solve for `n_traces` (likely 150–300 per dataset)
- [ ] Commit `POWER.md` justifying the corpus size

### P1.3 Full corpus
- [ ] Generate frozen-core corpus: **~200 MATH-500 + ~150 LiveCodeBench** at T=0
  on R1-Distill-7B + R1-Distill-1.5B drafter (one combination; EAGLE-3 head
  variant logged separately as a second drafter, per H2's drafter-dependence)
- [ ] Persist as Parquet partitioned by `(model, drafter, dataset, temperature, split)`
  under `corpus/v1/`
- [ ] Commit `CORPUS_SCHEMA.md` with column dtypes

### P1.4 Split (pre-registration)
- [ ] Split **by `problem_id`, not by token** (avoid trace-level leakage)
- [ ] Calibration : Validation : Test = 50 : 25 : 25 (proportions on problems)
- [ ] **Lock the test set**: write its problem_ids to `splits/test_locked.json`
  and **do not load it again until P4**

### P1 Exit gate
1. Schema-correct Parquet corpus
2. Power justification committed (`POWER.md`)
3. Test set locked
4. Entropy-vs-position sanity plots for 10 traces match expected spike-on-floor pattern

---

## P2 · The science · Wk 3–7 (hard gate at Wk 7)

**Goal.** Definitive verdicts on **H1** (structure), **H2** (reconciliation),
**H3** (state-vs-level) on the frozen-core corpus.
**Serves.** C1, C2, C3 — the heart of the paper.
**Bank.** AAAI-27 Student Abstract on H1 + H2 (+ H3 verdict, either sign).

### P2.A · H1 — phase structure, tested correctly · Wk 3–4

Two sub-hypotheses run independently, both must be reported.

#### P2.A.1 Marginal bimodality (the shape)
- [ ] Per-trace **Hartigan dip test** (`diptest`); report dip statistic distribution
  + fraction of traces rejecting unimodality
- [ ] **GMM 1- vs 2-component BIC** (`sklearn.mixture.GaussianMixture`) per trace;
  report ΔBIC distribution + fraction preferring 2-component
- [ ] **Silverman bandwidth test** via `kjohnsson/modality` on pooled and per-trace
- [ ] Compute **n_eff** per trace (effective sample size given autocorrelation
  via `acf` from `statsmodels.tsa`)

#### P2.A.2 Temporal phase structure
- [ ] Fit **2-state Gaussian HMM** (`hmmlearn.hmm.GaussianHMM`) per trace
- [ ] Compare log-likelihood vs 1-state (memoryless mixture) — LR test
- [ ] **PELT changepoint** detection (`ruptures.Pelt`) on entropy series;
  characterize segment lengths
- [ ] Run-length distribution vs **geometric null** (KS test, `scipy.stats`)

#### P2.A.3 Autocorrelation-preserving null (R8 mitigation)
- [ ] Compute autocorrelation function of entropy series per trace
- [ ] Choose **Politis–White block length** (`arch.bootstrap.optimal_block_length`)
- [ ] **Stationary block bootstrap** (`arch.bootstrap.StationaryBootstrap`):
  resample blocks → compute dip stat distribution under null
- [ ] **AR(p) surrogate** (via `statsmodels.tsa.AR` with order=p chosen by AIC)
  matching empirical autocorrelation; same null distribution
- [ ] Single-state-HMM surrogate (Gaussian, no transitions): compare
- [ ] Report: observed dip stat vs each of three null distributions

#### P2.A.4 Artifact controls
- [ ] Build formatting/cue mask: regex over tokens like `\n`, ` `, `=`, `$`,
  numbers; rerun H1 with masked positions removed
- [ ] Restrict to a single contiguous `<think>` span per trace; rerun H1

#### P2.A.5 Output
- [ ] Figure: per-trace dip statistic histogram + null bands
- [ ] Figure: entropy trace + HMM-posterior overlay for 3 example traces
- [ ] Table: H1 verdict summary
- [ ] Write `H1_results.md` — verdict (bimodal/not; phase-structured/not) with stats

### P2.B · H2 — the reconciliation · Wk 4–5 (sign-robust headline)

#### P2.B.1 2×2 design
Under **a single fixed (L, B) configuration** (the phase-agnostic baseline),
estimate entropy↔acceptance relationship in:

```
                       within-trace        across-domain
draft entropy     |   cell A (expect +)  |   cell B (we measure)
target entropy    |   cell C (we measure) |   cell D (expect −)
```

- [ ] Compute partial correlations controlling for **position** (spline) and
  **tree depth** — via residualized variables
- [ ] **Cell A** (draft-within): per-trace ρ; aggregate via random-effects
  meta-analysis (Fisher z transform); expect ≈ +0.56 (SpecKV)
- [ ] **Cell B** (draft-across): aggregate across MATH-500 vs LiveCodeBench
  domain means
- [ ] **Cell C** (target-within): per-trace ρ on target entropy
- [ ] **Cell D** (target-across): expect ≈ −0.18 (Acceptance Dynamics)
- [ ] CIs by bootstrap; pairwise cell comparisons via Fisher z difference test

#### P2.B.2 Drafter robustness
- [ ] Repeat all four cells with the second drafter (EAGLE-3 head) → show
  signs persist (drafter-dependence noted, signs robust)

#### P2.B.3 Attention-entropy null distinction (R8)
- [ ] Briefly verify: if we use **attention-entropy** instead of output-entropy,
  do we replicate Attention Drift's (2605.09992) null? — defensive footnote

#### P2.B.4 Output
- [ ] Figure: 2×2 grid with CIs
- [ ] Table: cell ρ + CI + sample size + p
- [ ] Write `H2_results.md` — the reconciliation explained in one figure

### P2.C · H3 — state vs level · Wk 5–7 (THE core test)

#### P2.C.1 The latent state (acausal)
- [ ] Fit 2-state Gaussian HMM on draft entropy (and parallel on target entropy)
  per trace; `hmmlearn` forward–backward
- [ ] Get **posterior phase probability** γ_t = P(Z_t=1 | full trajectory)
- [ ] Define `phase_label_hmm` ∈ {0, 1}: argmax posterior; also retain γ_t as continuous covariate
- [ ] Write back into the corpus (one extra column)
- [ ] Train HMM on calibration, get posteriors on validation; **do not touch test**

#### P2.C.2 The bandwidth-matched causal smoothing (the rival)
- [ ] Compute draft-entropy **EWMA** at α ∈ {0.1, 0.2, 0.3, 0.5}
- [ ] For each, compute the **effective bandwidth** (≈ 1/α)
- [ ] Match to the HMM's effective phase persistence (mean run length under
  the 2-state HMM); pick the α with the closest bandwidth
- [ ] Document the matching in `BANDWIDTH_MATCH.md` (pre-registered)

#### P2.C.3 The conditional survival model
This is the central statistical test of the paper. Run in this exact order.

- [ ] Define event: **rejection** of the proposed draft token at the verifier
- [ ] Define censoring: **L-cap** — when the drafter reached its full length
  without rejection (the accepted run was right-censored)
- [ ] **Discrete-time survival** via `statsmodels` GLM with **cloglog** link
  (one row per token-at-risk; outcome = rejected?; offset = log-hazard baseline)
- [ ] Per-trace **random effect** (use `statsmodels.regression.mixed_linear_model`
  for the random-intercept structure, or `pymer4`/`rpy2` to `lme4::glmer` if
  needed)
- [ ] Covariates: **spline in position** (`patsy.dmatrix("bs(position, df=5)")`)
  + **tree depth at accept**

- [ ] **Nested predictor sets**:
  - `M_a` : instantaneous draft confidence + draft entropy + AdaEDL bound term
    `1 − √(γ·H)`
  - `M_b` : `M_a` + bandwidth-matched causal EWMA of draft entropy
  - `M_c` : `M_b` + HMM phase state (the acausal latent)

- [ ] **Likelihood-ratio tests**: `M_b` vs `M_a`, `M_c` vs `M_b`
  (`M_c` vs `M_b` is the H3 test)
- [ ] **Multiplicity correction**: Holm/FWER across the (M_c vs M_b) test
  family — confirmatory uses Holm; exploratory secondary tests use BH

#### P2.C.4 Time-dependent C-index
- [ ] Compute time-dependent **C-index** for `M_a`, `M_b`, `M_c` on validation
  (`lifelines.utils.concordance_index` adapted to discrete-time, or roll our own)
- [ ] **Bootstrap CIs** (cluster bootstrap by trace) for each C-index
- [ ] Report **incremental C-index** = C(M_c) − C(M_b) with CI

#### P2.C.5 Drafter-blind confirmation
The proposal **earns the word "state"** only if a drafter-blind label also predicts.

- [ ] **Lexical-cue detector** (training-free): regex/keyword match over
  cue tokens `{however, thus, wait, therefore, let me reconsider, instead,
  actually, but, so}`; binary cue indicator → does it predict acceptance (AUC)?
  Does it co-occur with HMM-state transitions above chance?
- [ ] **Analysis-only hidden-state probe** (SemanticSpec precedent — R3 mitigation):
  train a small linear/MLP probe on target hidden states (penultimate layer or
  selected via best probe) to predict the HMM-state on held-out tokens; report
  probe AUC. **Explicitly analysis-only — not deployed in any controller.**

#### P2.C.6 Output
- [ ] Figure: incremental C-index forest plot (M_a → M_b → M_c) with CIs
- [ ] Figure: example trace with overlay of (raw entropy, EWMA, HMM state,
  acceptance outcomes)
- [ ] Table: LR test results (M_c vs M_b) per dataset
- [ ] Write `H3_results.md` — verdict (state / level) with stats

### P2 Exit gate (Wk 7 hard)
1. H1, H2, H3 verdicts with statistical confidence on validation
2. All artifact controls run, all nulls reported
3. Drafter-blind confirmation result reported
4. **Pre-register the H3 verdict** (whichever direction) before any P3 work begins
5. Draft AAAI-27 Student Abstract (2 pg) on H1 + H2 + H3 verdict — submit-ready

---

## P3 · Controller + oracle headroom · Wk 7–9

**Goal.** Build the deployed training-free EWMA-hysteresis detector and measure
the **oracle-vs-online gap** — how much of the H3 oracle (HMM-state) value the
causal detector recovers.
**Serves.** C4 (bounded demonstration).
**Conditional.** If H3 returned "level, not state", this phase is reduced to a
short measurement of the oracle-vs-online gap and we move on to P4. We do not
force a controller win.

### P3.1 Detector
- [ ] Implement **EWMA-hysteresis** detector: two thresholds (upper to enter
  "decision" phase, lower to return to "execution"); α from P2.C.2 matching
- [ ] Calibrate the two thresholds on **calibration split only** via a simple
  grid (objective: maximize predicted τ on a small offline simulation)
- [ ] **Freeze the thresholds** before validation/test
- [ ] Comparators (for the H4-A3 ablation): single-threshold (≈SVIP), lexical-cue,
  oracle HMM state

### P3.2 Policy
- [ ] Phase → (draft length L, tree budget B-width split) under fixed total node
  budget
- [ ] Two configurations to evaluate:
  - "deep" (execution): L=8, single chain, width 1
  - "shallow-wide" (decision): L=3, width 3–4 (HeteroSpec-comparable budget)
- [ ] Budget total node count matched to HeteroSpec defaults for the matched-FLOPs
  comparison in P4
- [ ] Freeze policy spec in `POLICY.md`

### P3.3 Oracle simulation
- [ ] On validation: replay the corpus with the **acausal HMM phase** as the
  controller input (oracle gets the future); measure τ and predicted speedup
- [ ] On validation: replay with the **causal EWMA detector**; same metrics
- [ ] Compute **recovered fraction** = (causal_gain − no_phase) / (oracle_gain − no_phase)

### P3 Exit gate
1. Frozen detector + policy spec
2. Oracle-vs-online gap on validation, with CI
3. Decision: (a) controller is worth running in P4 lossless eval, or (b) we
   instead lead with the oracle-headroom result and a smaller, honest controller table

---

## P4 · Lossless eval → workshop result · Wk 9–11 (hard gate)

**Goal.** Final speedup numbers at **matched FLOPs and matched wall-clock**,
with the lossless guarantee verified to a high empirical bar.
**Serves.** C4 + clears the workshop-paper bar.

### P4.1 Losslessness verification (proof obligation, R9)
- [ ] **Mathematical proof** that dynamic (L, B) leaves the accept/resample rule
  `min(1, p/q)` and resample-from-`(p−q)₊` unchanged; commit to `LOSSLESS_PROOF.md`
- [ ] **Sampler invariant check**: for the corpus's logged `(p, q)` pairs and
  acceptance decisions, verify the rule was applied correctly
- [ ] **TOST equivalence test** at the distribution level: equivalence margin
  ε = the Monte-Carlo CI width at M = 200 resamples per prompt (subset of test);
  pre-register ε via `LOSSLESS_TOST_PREREG.md`
- [ ] **Holm/FWER** multiplicity correction across positions for TOST
  (BH only for any exploratory secondary tests)
- [ ] **Greedy behavioral equality**: at T=0, token-for-token identity between
  our controller's output and vanilla AR (the senior reviewer's sanity check)
- [ ] **EQSPEC check at batch>1**: ragged-tensor desync test (the 2510.22876
  audit found 95% match in some impls; we target ≥99.9%)

### P4.2 Core sweep
- [ ] Target × dataset × T grid (frozen core only):
  `{R1-Distill-Qwen-7B} × {MATH-500, LiveCodeBench} × {T=0}`
- [ ] Drafter combinations: R1-Distill-1.5B (draft-model SD) **and** EAGLE-3 head
  stacked variant
- [ ] **Baselines on identical setup**:
  - Vanilla AR
  - Vanilla SD (fixed γ=5, no tree)
  - **AdaEDL** (our reimpl, simple rule; commit `baselines/adaedl.py`)
  - **SVIP** (our reimpl)
  - **HeteroSpec** (the to-beat — re-impl or use authors' code if available)
  - EAGLE-2 dynamic tree (off-the-shelf)
- [ ] Our controller (stacked on EAGLE-3 drafter)
- [ ] Metrics: τ overall, **τ per phase**, speedup vs AR, speedup vs **HeteroSpec**
  (the number that matters), tokens/s wall-clock, memory overhead
- [ ] **Matched FLOPs**: same target-call budget per request
- [ ] **Matched wall-clock**: rerun the comparison on a wall-clock-time budget
  (a slower controller wastes its predicted speedup; this is the honesty check)

### P4.3 Core ablations
- [ ] **A1** (the make-or-break): phase-state vs best-tuned per-token entropy
  length (calibrated AdaEDL λ) at matched width and FLOPs
- [ ] **A2**: length-only phase control vs SVIP
- [ ] **A3**: detector variants — EWMA-hysteresis vs single-threshold (≈SVIP) vs
  lexical-cue vs oracle HMM state (already from P3, formalized for the paper)
- [ ] **A4**: hysteresis on/off, **boundary-resolved** — does persistence help
  *at* execution→decision boundaries, or does it lag them? (per-boundary τ)

### P4.4 Headline framing (R5 mitigation)
- [ ] Report controller speedup **net of an adaptive-length oracle** (subtract
  AdaEAGLE's ~29% adaptive-length headroom from the comparison)
- [ ] Report the controller stacked on **EAGLE-3 AND HeteroSpec** specifically,
  not just vanilla SD
- [ ] If marginal gain < ~5% over HeteroSpec at matched compute: **do not headline
  it** — lead with H2 + the H3 verdict (R5 contingency)

### P4 Exit gate (hard)
1. All five losslessness checks pass (proof, invariant, TOST/Holm, greedy, EQSPEC)
2. Speedup table with CIs for the frozen core
3. Honest H4 verdict (positive / null / contingent)
4. Workshop-result decision: (i) controller-positive paper, or (ii) measurement-
   paper headlining C1+C2+C3 with C4 as a one-figure honesty result

---

## P5 · Extended tier · Wk 11–12 (optional)

**Goal.** Replicate and stress the result. Explicitly optional — the paper does
not depend on this completing.
**Serves.** Robustness; appendix.

### P5.1 Scale replication
- [ ] Add **R1-Distill-Qwen-14B** as a second scale (or in the proposal's
  "specificity check" slot)
- [ ] Add **Qwen3-8B-thinking** as a cross-family replication

### P5.2 Temperature sweep
- [ ] T=0.6 (R1's recommended temperature) on MATH-500 + LiveCodeBench
- [ ] Verify H1/H2/H3 verdicts hold under sampling

### P5.3 Extended baselines (reimplementations)
- [ ] **TALON** 2601.07353
- [ ] **SAGE** 2602.00523 (if applicable to text)
- [ ] **DSDE** 2509.01083 (the temporal-aggregation closest comparison)

### P5.4 Lossy Pareto (the "additional things")
- [ ] Relaxed verification at high-confidence low-entropy phases (e.g., accept
  draft top-1 if target's top-1 mass > τ_lossy, without strict `p/q` check)
- [ ] **pass@1 on MATH / AIME** for the lossy variant
- [ ] Speedup-vs-accuracy Pareto curve; compare to Fuzzy SD, EARS

### P5.5 Additional datasets (chat negative control)
- [ ] GSM8K, AIME-24/25, HumanEval, MBPP (extra reasoning/code coverage)
- [ ] **MT-Bench** as the **negative control** — phases should be weak here
  (if they aren't, our specificity claim is in trouble — this is the R-style stress)

---

## P6 · Writing & submission · Wk 12–14

**Goal.** Two submissions: workshop paper + Student Abstract. Code/corpus release.

### P6.1 Workshop paper (4 pg, target: NeurIPS ENLSP 2026 ~mid-Sept)
- [ ] Structure decision based on P2/P4 outcome:
  - If H3 positive + H4 positive → lead with C3 + C4, C2 in §4
  - If H3 positive + H4 null → lead with C3, C2 in §4, C4 as honest one-figure
  - If H3 null → **lead with C2 (sign-robust)**, frame H3 as "level, not state — the
    field can stop adding hysteresis" — a useful negative
- [ ] ≥60% of body on H1+H2+H3; C4 = one figure + one table max
- [ ] Lossless verification gets its own §
- [ ] Lossy / extended tier results → appendix

### P6.2 Student Abstract (AAAI-27, 2 pg, ~mid-Sept)
- [ ] H1 + H2 + H3 verdict only (no controller; matches the "floor" framing)
- [ ] Submit-ready by Wk 12 (Student Abstract already drafted at P2 gate)

### P6.3 Polish + release
- [ ] Run `humanizer` skill on prose
- [ ] Staff-engineer-bar internal review (the "would they sign off?" pass)
- [ ] **Code release**: GitHub repo with controller, baselines, analysis scripts
- [ ] **Corpus release**: Parquet + schema doc; Zenodo DOI
- [ ] `REPRODUCIBILITY.md` with exact seeds + Slurm scripts

### P6 Exit gate
1. Workshop paper submitted
2. Student Abstract submitted
3. Code + corpus released with DOI

---

## Per-phase pitfalls (cross-referenced to proposal risks)

| Phase | Pitfall | Tied to | Where mitigated |
|---|---|---|---|
| P1 | Token-level split → trace leakage | — | **P1.4** problem_id split, test locked |
| P2.A | Eyeballing bimodality instead of testing it | R8 | **P2.A.3** autocorrelation-preserving null |
| P2.A | Reading bimodality off cue/formatting tokens | — | **P2.A.4** masking + within-`<think>` |
| P2.B | Conflating draft/target or within/across | — | **P2.B.1** 2×2 design with position+depth controls |
| P2.C | "Phase" = thresholded EWMA → tautology | **R1** | **P2.C.1** acausal HMM, not causal smoothing |
| P2.C | Random effects ignored → inflated p | **R10** | **P2.C.3** per-trace random effect + cluster bootstrap |
| P2.C | Multiplicity hacking | **R10** | **P2.C.3** Holm/FWER pre-registered |
| P2.C | Hidden-state probe contradicts "training-free" | **R3** | **P2.C.5** probe is **analysis-only**, lexical-cue is the training-free check |
| P3 | Calibrating thresholds on test | — | **P3.1** freeze before validation/test |
| P3 | Differential censoring at L-cap | **R6** | **P3.3 / P2.C.3** multi-L + cap as censoring in survival |
| P4 | "Wins on FLOPs, loses on wall-clock" | — | **P4.2** matched-wall-clock comparison |
| P4 | Claiming losslessness without testing | **R9** | **P4.1** five checks incl. EQSPEC + TOST |
| P4 | Double-counting adaptive-length headroom | **R5** | **P4.4** report net of AdaEAGLE 29% |
| P5 | Lossy adds without accuracy story | — | **P5.4** pass@1 Pareto + chat negative control |
| P6 | Spinning a null H3 as positive | **R2** | **P6.1** "level, not state" lead-with framing |

## Single-source / provisional citations to recheck before camera-ready
(Flagged by the proposal as 2026 single-source.)

- SpecKV 2605.02888 — ρ≈+0.56 figure
- Acceptance Dynamics 2604.14682 — ρ≈−0.18 figure
- Attention Drift 2605.09992
- HeteroSpec 2505.13254 — 5.36× figure
- TALON / SAGE / GOOSE (2026 wave) — speedup figures
- AdaEAGLE 2412.18910 — 29% oracle gap

These power the related-work positioning; verify against the primary
source again before the paper goes out.
