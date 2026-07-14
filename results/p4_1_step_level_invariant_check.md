# P4.1 Step-Level Sampler Invariant Check (Reassessment)

## What the previous “100% pass” actually tested

The earlier implementation recomputed:
- recomputed_accept_length = next_position - current_position - 1

That check is tautological by construction. The logged `position` values in the trace are themselves derived from the same generation bookkeeping that advances the sequence by `accept_length + 1` tokens per step.

### Evidence from the generation code
- In [repos/EAGLE/eagle/model/ea_model.py](repos/EAGLE/eagle/model/ea_model.py), the logged `position` is the prompt-relative position at the time of logging.
- In [repos/EAGLE/eagle/model/utils.py](repos/EAGLE/eagle/model/utils.py), the next generation state advances by `accept_length + 1` tokens.

Because of that implementation, the identity
- next_position - current_position - 1 == accept_length
holds by design and does not independently verify the sampler behavior.

## Artifact audit for a genuine independent step-level check

I inspected the current artifacts:
- [results/p4_1_backfill_pq_report_full_fixedpos.json](results/p4_1_backfill_pq_report_full_fixedpos.json)
- [tmp/p4_1_backfill_full/trace_math500_0.jsonl](tmp/p4_1_backfill_full/trace_math500_0.jsonl)
- [corpus/v1/traces/trace_math500_0.jsonl](corpus/v1/traces/trace_math500_0.jsonl)

### What exists in the current schema
Backfill rows contain fields such as:
- `step`, `position`, `token_id`, `p`, `q`, `target_token_prob`, `draft_token_prob`, `pq_reconstruction_valid`

Trace rows contain fields such as:
- `step`, `position`, `token_id`, `accept_length`, `accepted`, `draft_topk_probs`, `draft_top1_prob`

### What does not exist
I did not find any field in the current artifacts that records, per step:
- the draft model’s argmax token at each prefix position along the accepted path,
- the target model’s argmax token at each prefix position along that same path,
- or any list of per-position argmax-equality outcomes from which `accept_length` could be recomputed as the longest prefix match.

The relevant argmax-style fields are absent, including names such as:
- `target_argmax_id`, `draft_argmax_id`
- `target_argmaxes`, `draft_argmaxes`
- `accepted_path_argmaxes`

## Result
A genuine step-level check that recomputes `accept_length` from the actual draft/target argmax agreement sequence is not possible from the current artifacts alone.

## Conclusion
The prior 100% pass rate only demonstrates that the logged position deltas are internally consistent with the logged `accept_length` under the same logging convention. It does not demonstrate an independent sampler invariant.

This is the same category of limitation as the earlier row-level check: it is documented, but it cannot be fixed from the current artifacts without re-running generation with additional per-position argmax logging.
