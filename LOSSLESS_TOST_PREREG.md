# P4.1 TOST Pre-Registration (Losslessness)

Date: 2026-07-12
Status: Locked before running P4.1 TOST results

## Scope
This prereg defines confirmatory TOST for losslessness on the validation split only.
The locked test split is excluded at this stage.

## Confirmatory Quantity
For each token position `k`, compare controller vs vanilla AR on the acceptance-related distributional statistic `theta_k` (primary: mean accept probability at position `k`, estimated from logged `(p, q)` via `min(1, p/q)`).

Define difference:

`Delta_k = theta_k(controller) - theta_k(vanilla)`

Null and equivalence hypotheses per position:

- `H0_k`: `Delta_k <= -epsilon` or `Delta_k >= epsilon`
- `H1_k`: `-epsilon < Delta_k < epsilon`

TOST passes at position `k` iff both one-sided tests reject at alpha level adjusted by Holm.

## Pre-Registered Margin epsilon
`epsilon` is pre-registered as the median two-sided Monte Carlo CI width across prompts/positions under `M = 200` resamples per prompt on the validation subset.

Operationally:
1. For each prompt and position, draw `M=200` Bernoulli resamples using the logged acceptance probability from `(p, q)`.
2. Compute a 95% CI width for the position-level statistic.
3. Aggregate widths over included positions/prompts.
4. Set `epsilon` to the median width from Step 3.

No observed controller-vs-vanilla deltas are inspected before locking this rule.

## Validation Subset and Inclusion
1. Use only problem_ids in `splits/validation_locked.json`.
2. Subset selection is deterministic by sorted `problem_id`, first `N` prompts (default `N=40` unless data availability requires lower `N`, which must be logged).
3. Positions are included if both methods have at least `n_min=20` prompt-level observations.
4. Confirmatory inclusion requires `pq_reconstruction_valid == True` from the backfill artifact.
5. `pq_reconstruction_valid` is defined as `q <= draft_top1_prob_live + 1e-6`.
6. Execution order is fixed: apply item 4 first, then evaluate item 3 on the surviving rows only.
7. Rows failing item 4 are excluded from confirmatory statistics (sampler invariant, TOST, Holm/FWER) and are not corrected/substituted.

## Multiplicity
Primary confirmatory family is all included positions.
Holm step-down FWER control at familywise `alpha=0.05`.
BH is reserved for exploratory secondary tests only.

## Outputs
The confirmatory report must include:
1. Locked `epsilon` value and how many prompts/positions contributed.
2. Raw per-position TOST p-values.
3. Holm-adjusted pass/fail per position.
4. Family-level pass/fail statement.
5. Rows before filter, excluded-invalid count, and confirmatory rows after filter.
6. Excluded-invalid counts per position.
7. Reference to `results/p4_1_pq_reconstruction_flags.md`.

## Stop Rule
If required logged `(p, q)` fields are unavailable, confirmatory TOST is marked as failed/unverifiable for P4.1 and no substitution metric is promoted as confirmatory.
