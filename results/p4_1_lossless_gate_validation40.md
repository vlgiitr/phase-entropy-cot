# P4.1 Losslessness Gate Report

Overall status: **FAIL**

## Checks
- sampler_invariant: fail
- tost_distribution_equivalence: fail
  - reason: controller_vs_vanilla_pair_not_provided
- holm_fwer_positions: fail
  - reason: no_per_position_tost_pvalues
- greedy_token_identity_t0: fail
  - reason: missing_controller_or_vanilla_outputs
- eqspec_ragged_desync_batch_gt_1: fail
  - reason: missing_batch_audit_jsonl

Validation-only execution completed; locked test split was not loaded.