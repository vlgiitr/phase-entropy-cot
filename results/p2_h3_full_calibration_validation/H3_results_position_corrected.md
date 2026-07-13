# P2.C H3 Results (Position-Corrected Re-Verification)

## Re-Verification Note
This is a re-verification run of the locked H3 confirmatory ladder after the position-indexing bug was identified.

- Bug context: prior run used absolute sequence-length `position` in the spline term.
- Correction applied here: position-dependent terms now use prompt-relative indexing (canonicalized via `step`, starting at 0 per trace).
- Intent: hold everything else fixed and change only position indexing.

## Fixed Configuration (unchanged from locked run)
- corpus: `corpus/v1`
- train/eval traces: 175 / 87
- train/eval rows: 116,892 / 59,205
- matched EWMA alpha: 0.40502282239836346
- HMM source/settings: same locked `p2_h3_token_features.csv` artifact
- bootstrap reps for delta c-index: 120 (cluster bootstrap by run_id, refit=True)

## Side-by-Side Comparison (Locked vs Position-Corrected)

| Metric | Locked (absolute position) | Position-corrected (prompt-relative step) |
|---|---:|---:|
| M_a c-index | 0.8503221418 | 0.8409574994 |
| M_b c-index | 0.8492750572 | 0.8411176217 |
| M_c c-index | 0.8489274259 | 0.8417854887 |
| Delta c-index (M_c - M_b) | -0.0003476313 | +0.0006678671 |
| Delta 95% CI | [-0.0021113223, +0.0015309244] | [-0.0011855764, +0.0020423226] |
| LR M_b vs M_a | 32.2367914526 | 21.0572190921 |
| p-value M_b vs M_a | 1.364817e-08 | 4.457702e-06 |
| LR M_c vs M_b | 0.1766644513 | 40.7300220747 |
| p-value M_c vs M_b | 0.6742555689 | 1.747812e-10 |
| corr(draft_entropy, hmm_gamma) | 0.9333332475 | 0.9333332475 |
| condition number (M_c) | 201.3939477690 | 172.8523992916 |

## Plain-Language Outcome
- The corrected-position refit changes the numeric fit substantially for the absolute c-index levels and LR(M_c vs M_b).
- The primary incremental discrimination metric remains small and uncertain: delta(M_c - M_b)=+0.0006678671 with 95% CI crossing 0.
- On that basis, the original H3 conclusion remains unchanged: **H3 is still not confirmed for incremental state-over-level gain**.

## Artifacts
- Locked reference summary: `results/p2_h3_full_calibration_validation/p2_h3_summary.json`
- Position-corrected refit JSON: `results/p2_h3_full_calibration_validation/H3_confirmatory_reconstruction_position_corrected.json`
- Locked report preserved unchanged: `results/p2_h3_full_calibration_validation/H3_results.md`
