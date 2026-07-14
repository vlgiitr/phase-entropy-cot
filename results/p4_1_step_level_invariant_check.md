# P4.1 Step-Level Sampler Invariant Check

## Definition
For each checked step:
- logged_accept_length := value logged in trace row
- recomputed_accept_length := next_position - current_position - 1

Rationale: in T=0 verification, one decode step advances by exactly (accept_length + 1) tokens.

## Scope
- backfill_report: /root/phase-entropy-cot/results/p4_1_backfill_pq_report_full_fixedpos.json
- backfill_dir: /root/phase-entropy-cot/tmp/p4_1_backfill_full
- trace_dir: /root/phase-entropy-cot/corpus/v1/traces
- summary_source: /root/phase-entropy-cot/tmp/p4_1_summary_full350.json

Confirmatory filter:
- include only steps with pq_reconstruction_valid == True
- exclude terminal step in each trace (no next_position available)

## Results
- traces_seen: 350
- steps_checked: 234924
- exact_matches: 234924 (100.000000%)
- mismatches: 0 (0.000000%)
- skipped_invalid_steps: 961
- skipped_terminal_steps: 350
- missing_trace_files: 0

## Mismatch Distribution
- No mismatches observed.

## Clustering
- dataset clustering: none
- trace clustering: none
- position clustering: none

## Verdict
PASS (empirical corroboration): recomputed and logged accept_length agree on all confirmatory checked steps.
