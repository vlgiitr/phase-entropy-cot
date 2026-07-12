# P4.1 Status (2026-07-13)

## What Is Proven
- Regime: T=0 greedy verification used by this project's corpus generation.
- Result: sequence-level losslessness is proven for EAGLE tree verification under argmax-prefix acceptance/correction.
- Interpretation: output tokens are identical to target-only greedy decoding, step by step.
- Controller impact: varying proposal budget (L, tree width/shape) does not change correctness criterion, so losslessness is preserved for any controller-chosen L in this T=0 regime.

## What Is Empirically Blocked Right Now
- The original row-level sampler invariant check based on min(1,p/q) is mis-specified for this T=0 corpus.
- A strict row-level replacement is also blocked by logging schema limits:
  - forensic rows do not include tree candidate/node identity, selected-path membership, or best_candidate path indices,
  - so row-to-selected-path mapping cannot be reconstructed from the existing 350-trace corpus alone.
- Consequence: strict per-row sampler-invariant validation cannot be completed without additional instrumentation.

## What Is Not Applicable
- TOST-style distributional equivalence tests designed for stochastic sampling are not the primary proof path for T=0 greedy verification.
- In this regime, the relevant obligation is deterministic sequence-level equivalence, already addressed by the T=0 proof.

## Practical Next Step (if empirical corroboration is required)
- Add instrumentation to log candidate/path identity at verification time (best_candidate, retrieve_indices path slice, per-node depth/parent ids, and on-selected-path flag).
- Then run a path-aware invariant audit aligned to the actual tree selection semantics.
