# P4.1 Losslessness Proof (T=0 Greedy, EAGLE Tree Verification)

Date: 2026-07-13
Scope: This proof covers the actual regime used in this project's corpus generation: temperature 0 with EAGLE tree-based argmax-prefix verification.

## Claim
At temperature 0, EAGLE verification produces exactly the same output sequence as target-only greedy autoregressive decoding.

More precisely, at each verification step, EAGLE computes:
- a selected candidate path index `best_candidate`, and
- an accepted prefix length `accept_length`,

where `accept_length` is the longest prefix on the selected path for which proposed tokens match target argmax decisions at corresponding positions.

Then the emitted tokens are exactly those target-greedy tokens: matched draft tokens are kept, and at first mismatch the target argmax correction is used. Therefore the final emitted sequence is token-for-token identical to target-only greedy decoding, regardless of draft model quality, tree width/shape, or proposed draft length `L`.

## Proof
Fix any decoding state (current prefix).

1. In T=0 mode, verification compares candidate-path tokens to target argmax decisions position-wise and computes the longest matching prefix (`accept_length`) on a selected path (`best_candidate`).

2. For each position up to `accept_length`, a draft token is accepted only when it equals the target model's own greedy token at that position.

3. At the first mismatch position (or immediately if none match), the correction step emits the target model's own greedy token for continuation.

4. Hence each emitted token at this step is one of two cases:
- accepted draft token that already equals target argmax, or
- correction token equal to target argmax.

So every emitted token equals the token target-only greedy decoding would emit from the same prefix.

5. Induct over steps: if prefixes are identical before a step, emitted next token is identical, so prefixes remain identical after the step. Base case is the same prompt prefix. Therefore the full output sequence is identical.

QED.

## Controller-Specific Corollary (P4.1)
Our controller changes only proposal budget parameters (draft length `L`, tree width/shape) by phase, while keeping the same T=0 verification criterion above. Therefore changing `L` cannot break losslessness: it changes how many candidates are proposed per step, not the acceptance correctness condition.

## What This Proof Does Not Cover
1. Non-zero temperature sampling: that regime is stochastic and requires a different proof route (min(1,p/q)-style argument), not this T=0 argmax-prefix argument.
2. Row-level empirical sampler checks on existing logs: current forensic schema does not include enough tree candidate/path identity to reconstruct strict per-row selected-path membership. That is a separate instrumentation issue, not a contradiction of the T=0 sequence-level equivalence proof.
