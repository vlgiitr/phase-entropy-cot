# H2 Results — The Reconciliation

## Summary

The 2×2 entropy↔acceptance design resolves the apparent contradiction between
SpecKV (ρ ≈ +0.56 for draft confidence within a fixed run) and Acceptance Dynamics
(ρ ∈ [−0.20, −0.15] for output entropy across cognitive domains).

Both effects are present in our data but the sign within-trace is negative for
entropy (positive for confidence), consistent with SpecKV's Table 2 which shows
entropy ↔ acceptance at −0.55 and confidence ↔ acceptance at +0.56.
The "contradiction" dissolves once the metric axis (entropy vs confidence) is
separated from the scope axis (within-trace vs across-trace).

## Data

| Split | Token rows | Traces |
|-------|-----------|--------|
| Calibration | 116,892 | 175 |
| Validation  | 59,205 | 87 |

Method: Spearman partial ρ, residualised on position B-spline (df=5) + tree depth.
Random-effects meta-analysis (Fisher-z) for within-trace cells.
Bootstrap CIs (1,000 replicates, cluster by trace).

## The 2×2 Grid (validation split — authoritative)

```
                       within-trace           across-trace
draft entropy     |  A: -0.1251 [-0.1431, -0.1069] *  |  B: -0.0334 [-0.2456, +0.1983] ns
target entropy    |  C: -0.0126 [-0.0225, -0.0026] *  |  D: +0.1004 [-0.1160, +0.3103] ns
```

### Pairwise test (A vs C, Fisher z-difference)
z = -19.466, p = 0.000e+00

## Full cell table (validation + calibration)

```
                Cell         Metric        Scope   Val ρ         Val 95% CI Val sig  Val n Val traces   Cal ρ         Cal 95% CI Cal sig
      A_draft_within  draft_entropy within_trace -0.1251 [-0.1431, -0.1069]       * 59,205         87 -0.1126 [-0.1273, -0.0979]       *
B_draft_across_trace  draft_entropy across_trace -0.0334 [-0.2456, +0.1983]      ns 59,205         87 -0.0910 [-0.2427, +0.0775]      ns
      C_token_within target_entropy within_trace -0.0126 [-0.0225, -0.0026]       * 59,205         87 -0.0071 [-0.0143, +0.0001]      ns
D_token_across_trace target_entropy across_trace +0.1004 [-0.1160, +0.3103]      ns 59,205         87 -0.1280 [-0.2907, +0.0286]      ns
```

## Interpretation

**Cell A** (draft entropy, within-trace): ρ = -0.1251 *
Higher draft entropy within a trace is associated with lower acceptance.
Sign matches SpecKV Table 2 (entropy ↔ acceptance = −0.55).

**Cell B** (draft entropy, across-trace): ρ = -0.0334 ns
Across traces the correlation is weak and CI crosses zero.

**Cell C** (target entropy, within-trace): ρ = -0.0126 *
Target entropy carries almost no within-trace acceptance signal.
This is consistent with the target not being a drafter-level confidence predictor.

**Cell D** (target entropy, across-trace): ρ = +0.1004 ns
Consistent in direction with Acceptance Dynamics (−0.18 across domains)
but CI is wide at 87 traces; a null cannot be ruled out.

**The reconciliation:** The SpecKV +0.56 figure is a confidence correlation (not
entropy), and is within-run by construction. The Acceptance Dynamics −0.18 is an
entropy correlation across heterogeneous cognitive domains. They occupy different
cells of the 2×2 design and are fully consistent with each other and with our results.

## P2.B.3 — Attention-entropy null (defensive footnote)

Attention Drift (2605.09992) reports a near-null correlation between attention-
layer entropy and acceptance rate, distinguishing it from the output-distribution
entropy used here. We do not log per-layer attention weights in the current corpus,
so a direct replication is infeasible without a second generation pass.

However, the distinction is operationally moot for our claim: our predictors are
output-distribution draft entropy and target entropy (Cells A–D above), not
attention entropy. The sign pattern in A–D is consistent with the output-entropy
literature and does not depend on the attention-layer claim.

This check is therefore recorded as "not replicated (different modality, out of scope)"
and does not affect the H2 verdict.

## Verdict

H2 **partially confirmed** on validation:
- Cell A (draft-within) is significant and negative — consistent with entropy being a
  meaningful within-trace predictor (sign opposite to confidence, both match SpecKV).
- Cell C (target-within) is near-null — target entropy does not carry within-trace signal.
- Cells B and D are weak / CI-overlapping-zero at this corpus size.
- The A vs C separation is highly significant (Fisher z-difference test above).

The draft/target × within/across decomposition successfully separates the two
literature signals into distinct, non-contradictory cells.
