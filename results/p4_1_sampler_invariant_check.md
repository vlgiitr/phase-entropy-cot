# P4.1 Sampler Invariant Check (Corrected T=0 Formulation)

This report replaces the prior mis-specified stochastic check using min(1, p/q).
For this corpus (T=0), the invariant audited here is deterministic argmax-equivalence:
- criterion_argmax_match = (draft_argmax_id == target_argmax_id)
- expected row outcome: accepted == criterion_argmax_match

Overall verdict: **FAIL**

## Summary
- backfill_dir: /root/phase-entropy-cot/tmp/p4_1_backfill_full
- trace_dir: /root/phase-entropy-cot/corpus/v1/traces
- total_rows_scanned: 236235
- confirmatory_rows: 235274
- rows_with_complete_argmax_ids: 235274
- accepted_true: 153655
- accepted_false: 81619
- criterion_argmax_match_true: 50
- criterion_argmax_match_false: 235224
- agreement_rows: 81655
- disagreement_rows: 153619
- exact_agreement_rate: 0.347063
- missing_trace_row: 0
- missing_target_top1: 0
- missing_draft_top1: 0

## Real Anomalies (accepted disagrees with argmax-match criterion)
Showing up to 200 rows.

| trace_file | row_index | run_id | problem_id | step | position | accepted | criterion_argmax_match | target_top1_id | draft_top1_id |
|:--|--:|:--|:--|--:|--:|:--:|:--:|--:|--:|
| trace_livecodebench_0.jsonl | 1 | livecodebench_0 | 1873_A | 1 | 462 | True | False | 358 | 0 |
| trace_livecodebench_0.jsonl | 3 | livecodebench_0 | 1873_A | 3 | 465 | True | False | 11886 | 545 |
| trace_livecodebench_0.jsonl | 5 | livecodebench_0 | 1873_A | 5 | 468 | True | False | 13 | 4745 |
| trace_livecodebench_0.jsonl | 6 | livecodebench_0 | 1873_A | 6 | 471 | True | False | 596 | 1379 |
| trace_livecodebench_0.jsonl | 7 | livecodebench_0 | 1873_A | 7 | 473 | True | False | 3575 | 125 |
| trace_livecodebench_0.jsonl | 8 | livecodebench_0 | 1873_A | 8 | 476 | True | False | 382 | 903 |
| trace_livecodebench_0.jsonl | 10 | livecodebench_0 | 1873_A | 10 | 479 | True | False | 2380 | 545 |
| trace_livecodebench_0.jsonl | 11 | livecodebench_0 | 1873_A | 11 | 483 | True | False | 449 | 1576 |
| trace_livecodebench_0.jsonl | 12 | livecodebench_0 | 1873_A | 12 | 485 | True | False | 264 | 1308 |
| trace_livecodebench_0.jsonl | 13 | livecodebench_0 | 1873_A | 13 | 487 | True | False | 11 | 0 |
| trace_livecodebench_0.jsonl | 14 | livecodebench_0 | 1873_A | 14 | 490 | True | False | 13 | 94 |
| trace_livecodebench_0.jsonl | 15 | livecodebench_0 | 1873_A | 15 | 492 | True | False | 9277 | 95 |
| trace_livecodebench_0.jsonl | 16 | livecodebench_0 | 1873_A | 16 | 495 | True | False | 264 | 95 |
| trace_livecodebench_0.jsonl | 17 | livecodebench_0 | 1873_A | 17 | 497 | True | False | 1063 | 412 |
| trace_livecodebench_0.jsonl | 18 | livecodebench_0 | 1873_A | 18 | 500 | True | False | 649 | 253 |
| trace_livecodebench_0.jsonl | 19 | livecodebench_0 | 1873_A | 19 | 504 | True | False | 520 | 482 |
| trace_livecodebench_0.jsonl | 20 | livecodebench_0 | 1873_A | 20 | 506 | True | False | 5784 | 187 |
| trace_livecodebench_0.jsonl | 22 | livecodebench_0 | 1873_A | 22 | 511 | True | False | 8417 | 108 |
| trace_livecodebench_0.jsonl | 26 | livecodebench_0 | 1873_A | 26 | 518 | True | False | 279 | 482 |
| trace_livecodebench_0.jsonl | 27 | livecodebench_0 | 1873_A | 27 | 521 | True | False | 9221 | 412 |
| trace_livecodebench_0.jsonl | 28 | livecodebench_0 | 1873_A | 28 | 523 | True | False | 13997 | 801 |
| trace_livecodebench_0.jsonl | 29 | livecodebench_0 | 1873_A | 29 | 525 | True | False | 11 | 499 |
| trace_livecodebench_0.jsonl | 32 | livecodebench_0 | 1873_A | 32 | 531 | True | False | 5782 | 0 |
| trace_livecodebench_0.jsonl | 33 | livecodebench_0 | 1873_A | 33 | 534 | True | False | 81122 | 239 |
| trace_livecodebench_0.jsonl | 35 | livecodebench_0 | 1873_A | 35 | 537 | True | False | 279 | 121 |
| trace_livecodebench_0.jsonl | 39 | livecodebench_0 | 1873_A | 39 | 542 | True | False | 2380 | 482 |
| trace_livecodebench_0.jsonl | 44 | livecodebench_0 | 1873_A | 44 | 549 | True | False | 293 | 482 |
| trace_livecodebench_0.jsonl | 45 | livecodebench_0 | 1873_A | 45 | 552 | True | False | 477 | 0 |
| trace_livecodebench_0.jsonl | 46 | livecodebench_0 | 1873_A | 46 | 554 | True | False | 11 | 96 |
| trace_livecodebench_0.jsonl | 48 | livecodebench_0 | 1873_A | 48 | 557 | True | False | 1855 | 467 |
| trace_livecodebench_0.jsonl | 49 | livecodebench_0 | 1873_A | 49 | 561 | True | False | 358 | 379 |
| trace_livecodebench_0.jsonl | 52 | livecodebench_0 | 1873_A | 52 | 567 | True | False | 422 | 118 |
| trace_livecodebench_0.jsonl | 53 | livecodebench_0 | 1873_A | 53 | 569 | True | False | 311 | 100 |
| trace_livecodebench_0.jsonl | 55 | livecodebench_0 | 1873_A | 55 | 574 | True | False | 7315 | 96 |
| trace_livecodebench_0.jsonl | 57 | livecodebench_0 | 1873_A | 57 | 580 | True | False | 382 | 482 |
| trace_livecodebench_0.jsonl | 58 | livecodebench_0 | 1873_A | 58 | 583 | True | False | 1781 | 726 |
| trace_livecodebench_0.jsonl | 61 | livecodebench_0 | 1873_A | 61 | 588 | True | False | 26350 | 487 |
| trace_livecodebench_0.jsonl | 63 | livecodebench_0 | 1873_A | 63 | 591 | True | False | 11 | 0 |
| trace_livecodebench_0.jsonl | 65 | livecodebench_0 | 1873_A | 65 | 594 | True | False | 374 | 801 |
| trace_livecodebench_0.jsonl | 67 | livecodebench_0 | 1873_A | 67 | 598 | True | False | 498 | 96 |
| trace_livecodebench_0.jsonl | 73 | livecodebench_0 | 1873_A | 73 | 606 | True | False | 1541 | 0 |
| trace_livecodebench_0.jsonl | 74 | livecodebench_0 | 1873_A | 74 | 609 | True | False | 1205 | 104 |
| trace_livecodebench_0.jsonl | 76 | livecodebench_0 | 1873_A | 76 | 612 | True | False | 81556 | 115 |
| trace_livecodebench_0.jsonl | 78 | livecodebench_0 | 1873_A | 78 | 617 | True | False | 2804 | 482 |
| trace_livecodebench_0.jsonl | 80 | livecodebench_0 | 1873_A | 80 | 621 | True | False | 13 | 125 |
| trace_livecodebench_0.jsonl | 81 | livecodebench_0 | 1873_A | 81 | 624 | True | False | 369 | 4181 |
| trace_livecodebench_0.jsonl | 82 | livecodebench_0 | 1873_A | 82 | 627 | True | False | 925 | 125 |
| trace_livecodebench_0.jsonl | 83 | livecodebench_0 | 1873_A | 83 | 629 | True | False | 596 | 99 |
| trace_livecodebench_0.jsonl | 84 | livecodebench_0 | 1873_A | 84 | 631 | True | False | 330 | 96 |
| trace_livecodebench_0.jsonl | 85 | livecodebench_0 | 1873_A | 85 | 633 | True | False | 358 | 3904 |
| trace_livecodebench_0.jsonl | 87 | livecodebench_0 | 1873_A | 87 | 637 | True | False | 422 | 95 |
| trace_livecodebench_0.jsonl | 91 | livecodebench_0 | 1873_A | 91 | 643 | True | False | 6857 | 125 |
| trace_livecodebench_0.jsonl | 92 | livecodebench_0 | 1873_A | 92 | 645 | True | False | 5885 | 95 |
| trace_livecodebench_0.jsonl | 96 | livecodebench_0 | 1873_A | 96 | 650 | True | False | 11 | 95 |
| trace_livecodebench_0.jsonl | 97 | livecodebench_0 | 1873_A | 97 | 653 | True | False | 64819 | 482 |
| trace_livecodebench_0.jsonl | 99 | livecodebench_0 | 1873_A | 99 | 656 | True | False | 330 | 145 |
| trace_livecodebench_0.jsonl | 100 | livecodebench_0 | 1873_A | 100 | 660 | True | False | 11690 | 801 |
| trace_livecodebench_0.jsonl | 101 | livecodebench_0 | 1873_A | 101 | 662 | True | False | 1268 | 4132 |
| trace_livecodebench_0.jsonl | 105 | livecodebench_0 | 1873_A | 105 | 669 | True | False | 1980 | 99 |
| trace_livecodebench_0.jsonl | 106 | livecodebench_0 | 1873_A | 106 | 671 | True | False | 1781 | 2469 |
| trace_livecodebench_0.jsonl | 108 | livecodebench_0 | 1873_A | 108 | 675 | True | False | 2218 | 94 |
| trace_livecodebench_0.jsonl | 109 | livecodebench_0 | 1873_A | 109 | 677 | True | False | 330 | 33323 |
| trace_livecodebench_0.jsonl | 110 | livecodebench_0 | 1873_A | 110 | 679 | True | False | 9062 | 3904 |
| trace_livecodebench_0.jsonl | 111 | livecodebench_0 | 1873_A | 111 | 682 | True | False | 1288 | 317 |
| trace_livecodebench_0.jsonl | 114 | livecodebench_0 | 1873_A | 114 | 686 | True | False | 382 | 481 |
| trace_livecodebench_0.jsonl | 115 | livecodebench_0 | 1873_A | 115 | 689 | True | False | 11 | 347 |
| trace_livecodebench_0.jsonl | 116 | livecodebench_0 | 1873_A | 116 | 691 | True | False | 1855 | 96 |
| trace_livecodebench_0.jsonl | 118 | livecodebench_0 | 1873_A | 118 | 694 | True | False | 358 | 151 |
| trace_livecodebench_0.jsonl | 119 | livecodebench_0 | 1873_A | 119 | 697 | True | False | 279 | 115 |
| trace_livecodebench_0.jsonl | 120 | livecodebench_0 | 1873_A | 120 | 700 | True | False | 449 | 130 |
| trace_livecodebench_0.jsonl | 122 | livecodebench_0 | 1873_A | 122 | 704 | True | False | 1 | 96 |
| trace_livecodebench_0.jsonl | 123 | livecodebench_0 | 1873_A | 123 | 706 | True | False | 279 | 96 |
| trace_livecodebench_0.jsonl | 127 | livecodebench_0 | 1873_A | 127 | 713 | True | False | 220 | 96 |
| trace_livecodebench_0.jsonl | 128 | livecodebench_0 | 1873_A | 128 | 716 | True | False | 25 | 0 |
| trace_livecodebench_0.jsonl | 130 | livecodebench_0 | 1873_A | 130 | 719 | True | False | 13997 | 130 |
| trace_livecodebench_0.jsonl | 131 | livecodebench_0 | 1873_A | 131 | 724 | True | False | 11651 | 94 |
| trace_livecodebench_0.jsonl | 133 | livecodebench_0 | 1873_A | 133 | 727 | True | False | 17 | 96 |
| trace_livecodebench_0.jsonl | 136 | livecodebench_0 | 1873_A | 136 | 733 | True | False | 7041 | 96 |
| trace_livecodebench_0.jsonl | 137 | livecodebench_0 | 1873_A | 137 | 735 | True | False | 2361 | 125 |
| trace_livecodebench_0.jsonl | 138 | livecodebench_0 | 1873_A | 138 | 737 | True | False | 3250 | 180 |
| trace_livecodebench_0.jsonl | 139 | livecodebench_0 | 1873_A | 139 | 741 | True | False | 2489 | 96 |
| trace_livecodebench_0.jsonl | 141 | livecodebench_0 | 1873_A | 141 | 744 | True | False | 3868 | 228 |
| trace_livecodebench_0.jsonl | 142 | livecodebench_0 | 1873_A | 142 | 746 | True | False | 2533 | 0 |
| trace_livecodebench_0.jsonl | 145 | livecodebench_0 | 1873_A | 145 | 750 | True | False | 5885 | 125 |
| trace_livecodebench_0.jsonl | 146 | livecodebench_0 | 1873_A | 146 | 752 | True | False | 422 | 0 |
| trace_livecodebench_0.jsonl | 148 | livecodebench_0 | 1873_A | 148 | 755 | True | False | 374 | 125 |
| trace_livecodebench_0.jsonl | 149 | livecodebench_0 | 1873_A | 149 | 757 | True | False | 719 | 115 |
| trace_livecodebench_0.jsonl | 152 | livecodebench_0 | 1873_A | 152 | 762 | True | False | 527 | 125 |
| trace_livecodebench_0.jsonl | 153 | livecodebench_0 | 1873_A | 153 | 764 | True | False | 64819 | 723 |
| trace_livecodebench_0.jsonl | 156 | livecodebench_0 | 1873_A | 156 | 770 | True | False | 449 | 100 |
| trace_livecodebench_0.jsonl | 158 | livecodebench_0 | 1873_A | 158 | 773 | True | False | 832 | 834 |
| trace_livecodebench_0.jsonl | 160 | livecodebench_0 | 1873_A | 160 | 776 | True | False | 2361 | 96 |
| trace_livecodebench_0.jsonl | 162 | livecodebench_0 | 1873_A | 162 | 780 | True | False | 433 | 482 |
| trace_livecodebench_0.jsonl | 163 | livecodebench_0 | 1873_A | 163 | 782 | True | False | 11 | 0 |
| trace_livecodebench_0.jsonl | 167 | livecodebench_0 | 1873_A | 167 | 789 | True | False | 422 | 487 |
| trace_livecodebench_0.jsonl | 170 | livecodebench_0 | 1873_A | 170 | 793 | True | False | 264 | 482 |
| trace_livecodebench_0.jsonl | 171 | livecodebench_0 | 1873_A | 171 | 797 | True | False | 1405 | 482 |
| trace_livecodebench_0.jsonl | 173 | livecodebench_0 | 1873_A | 173 | 800 | True | False | 3752 | 723 |
| trace_livecodebench_0.jsonl | 174 | livecodebench_0 | 1873_A | 174 | 802 | True | False | 304 | 96 |
| trace_livecodebench_0.jsonl | 176 | livecodebench_0 | 1873_A | 176 | 805 | True | False | 382 | 282 |
| trace_livecodebench_0.jsonl | 177 | livecodebench_0 | 1873_A | 177 | 807 | True | False | 7344 | 4132 |
| trace_livecodebench_0.jsonl | 178 | livecodebench_0 | 1873_A | 178 | 810 | True | False | 596 | 105 |
| trace_livecodebench_0.jsonl | 179 | livecodebench_0 | 1873_A | 179 | 812 | True | False | 311 | 125 |
| trace_livecodebench_0.jsonl | 180 | livecodebench_0 | 1873_A | 180 | 814 | True | False | 304 | 1001 |
| trace_livecodebench_0.jsonl | 181 | livecodebench_0 | 1873_A | 181 | 816 | True | False | 315 | 164 |
| trace_livecodebench_0.jsonl | 184 | livecodebench_0 | 1873_A | 184 | 820 | True | False | 67514 | 95 |
| trace_livecodebench_0.jsonl | 185 | livecodebench_0 | 1873_A | 185 | 822 | True | False | 369 | 2140 |
| trace_livecodebench_0.jsonl | 186 | livecodebench_0 | 1873_A | 186 | 827 | True | False | 11 | 323 |
| trace_livecodebench_0.jsonl | 189 | livecodebench_0 | 1873_A | 189 | 831 | True | False | 98571 | 130 |
| trace_livecodebench_0.jsonl | 190 | livecodebench_0 | 1873_A | 190 | 835 | True | False | 1243 | 94 |
| trace_livecodebench_0.jsonl | 192 | livecodebench_0 | 1873_A | 192 | 838 | True | False | 52518 | 95 |
| trace_livecodebench_0.jsonl | 194 | livecodebench_0 | 1873_A | 194 | 843 | True | False | 15 | 153 |
| trace_livecodebench_0.jsonl | 195 | livecodebench_0 | 1873_A | 195 | 845 | True | False | 264 | 0 |
| trace_livecodebench_0.jsonl | 200 | livecodebench_0 | 1873_A | 200 | 851 | True | False | 25 | 72 |
| trace_livecodebench_0.jsonl | 201 | livecodebench_0 | 1873_A | 201 | 856 | True | False | 15465 | 94 |
| trace_livecodebench_0.jsonl | 203 | livecodebench_0 | 1873_A | 203 | 862 | True | False | 293 | 606 |
| trace_livecodebench_0.jsonl | 205 | livecodebench_0 | 1873_A | 205 | 869 | True | False | 382 | 2967 |
| trace_livecodebench_0.jsonl | 206 | livecodebench_0 | 1873_A | 206 | 872 | True | False | 11 | 726 |
| trace_livecodebench_0.jsonl | 207 | livecodebench_0 | 1873_A | 207 | 874 | True | False | 67514 | 409 |
| trace_livecodebench_0.jsonl | 208 | livecodebench_0 | 1873_A | 208 | 876 | True | False | 64819 | 2140 |
| trace_livecodebench_0.jsonl | 210 | livecodebench_0 | 1873_A | 210 | 881 | True | False | 323 | 95 |
| trace_livecodebench_0.jsonl | 211 | livecodebench_0 | 1873_A | 211 | 884 | True | False | 1053 | 93 |
| trace_livecodebench_0.jsonl | 213 | livecodebench_0 | 1873_A | 213 | 888 | True | False | 2100 | 100 |
| trace_livecodebench_0.jsonl | 214 | livecodebench_0 | 1873_A | 214 | 891 | True | False | 420 | 0 |
| trace_livecodebench_0.jsonl | 215 | livecodebench_0 | 1873_A | 215 | 893 | True | False | 279 | 151 |
| trace_livecodebench_0.jsonl | 216 | livecodebench_0 | 1873_A | 216 | 896 | True | False | 14410 | 693 |
| trace_livecodebench_0.jsonl | 217 | livecodebench_0 | 1873_A | 217 | 899 | True | False | 14364 | 545 |
| trace_livecodebench_0.jsonl | 218 | livecodebench_0 | 1873_A | 218 | 901 | True | False | 56977 | 477 |
| trace_livecodebench_0.jsonl | 219 | livecodebench_0 | 1873_A | 219 | 905 | True | False | 28474 | 99 |
| trace_livecodebench_0.jsonl | 220 | livecodebench_0 | 1873_A | 220 | 907 | True | False | 52518 | 95 |
| trace_livecodebench_0.jsonl | 222 | livecodebench_0 | 1873_A | 222 | 912 | True | False | 293 | 93 |
| trace_livecodebench_0.jsonl | 223 | livecodebench_0 | 1873_A | 223 | 916 | True | False | 264 | 1195 |
| trace_livecodebench_0.jsonl | 224 | livecodebench_0 | 1873_A | 224 | 918 | True | False | 15465 | 801 |
| trace_livecodebench_0.jsonl | 225 | livecodebench_0 | 1873_A | 225 | 920 | True | False | 16 | 97 |
| trace_livecodebench_0.jsonl | 226 | livecodebench_0 | 1873_A | 226 | 924 | True | False | 264 | 99 |
| trace_livecodebench_0.jsonl | 227 | livecodebench_0 | 1873_A | 227 | 926 | True | False | 11651 | 1195 |
| trace_livecodebench_0.jsonl | 228 | livecodebench_0 | 1873_A | 228 | 929 | True | False | 382 | 723 |
| trace_livecodebench_0.jsonl | 229 | livecodebench_0 | 1873_A | 229 | 931 | True | False | 272 | 606 |
| trace_livecodebench_0.jsonl | 230 | livecodebench_0 | 1873_A | 230 | 936 | True | False | 272 | 94 |
| trace_livecodebench_0.jsonl | 231 | livecodebench_0 | 1873_A | 231 | 938 | True | False | 1403 | 2967 |
| trace_livecodebench_0.jsonl | 233 | livecodebench_0 | 1873_A | 233 | 944 | True | False | 4593 | 100 |
| trace_livecodebench_0.jsonl | 234 | livecodebench_0 | 1873_A | 234 | 947 | True | False | 15 | 576 |
| trace_livecodebench_0.jsonl | 235 | livecodebench_0 | 1873_A | 235 | 951 | True | False | 220 | 96 |
| trace_livecodebench_0.jsonl | 236 | livecodebench_0 | 1873_A | 236 | 953 | True | False | 5155 | 0 |
| trace_livecodebench_0.jsonl | 238 | livecodebench_0 | 1873_A | 238 | 957 | True | False | 4320 | 0 |
| trace_livecodebench_0.jsonl | 239 | livecodebench_0 | 1873_A | 239 | 960 | True | False | 14410 | 2384 |
| trace_livecodebench_0.jsonl | 240 | livecodebench_0 | 1873_A | 240 | 962 | True | False | 14364 | 128 |
| trace_livecodebench_0.jsonl | 241 | livecodebench_0 | 1873_A | 241 | 964 | True | False | 65 | 477 |
| trace_livecodebench_0.jsonl | 242 | livecodebench_0 | 1873_A | 242 | 968 | True | False | 28474 | 132 |
| trace_livecodebench_0.jsonl | 243 | livecodebench_0 | 1873_A | 243 | 971 | True | False | 52518 | 95 |
| trace_livecodebench_0.jsonl | 244 | livecodebench_0 | 1873_A | 244 | 975 | True | False | 293 | 3353 |
| trace_livecodebench_0.jsonl | 247 | livecodebench_0 | 1873_A | 247 | 982 | True | False | 15465 | 2967 |
| trace_livecodebench_0.jsonl | 248 | livecodebench_0 | 1873_A | 248 | 984 | True | False | 25 | 97 |
| trace_livecodebench_0.jsonl | 249 | livecodebench_0 | 1873_A | 249 | 989 | True | False | 15465 | 94 |
| trace_livecodebench_0.jsonl | 251 | livecodebench_0 | 1873_A | 251 | 995 | True | False | 264 | 606 |
| trace_livecodebench_0.jsonl | 252 | livecodebench_0 | 1873_A | 252 | 1000 | True | False | 272 | 801 |
| trace_livecodebench_0.jsonl | 253 | livecodebench_0 | 1873_A | 253 | 1002 | True | False | 682 | 2967 |
| trace_livecodebench_0.jsonl | 254 | livecodebench_0 | 1873_A | 254 | 1007 | True | False | 15465 | 323 |
| trace_livecodebench_0.jsonl | 255 | livecodebench_0 | 1873_A | 255 | 1011 | True | False | 2100 | 0 |
| trace_livecodebench_0.jsonl | 256 | livecodebench_0 | 1873_A | 256 | 1013 | True | False | 904 | 125 |
| trace_livecodebench_0.jsonl | 257 | livecodebench_0 | 1873_A | 257 | 1015 | True | False | 1053 | 180 |
| trace_livecodebench_0.jsonl | 258 | livecodebench_0 | 1873_A | 258 | 1017 | True | False | 682 | 315 |
| trace_livecodebench_0.jsonl | 259 | livecodebench_0 | 1873_A | 259 | 1020 | True | False | 13 | 323 |
| trace_livecodebench_0.jsonl | 260 | livecodebench_0 | 1873_A | 260 | 1022 | True | False | 4320 | 265 |
| trace_livecodebench_0.jsonl | 262 | livecodebench_0 | 1873_A | 262 | 1025 | True | False | 719 | 317 |
| trace_livecodebench_0.jsonl | 265 | livecodebench_0 | 1873_A | 265 | 1032 | True | False | 25 | 1379 |
| trace_livecodebench_0.jsonl | 266 | livecodebench_0 | 1873_A | 266 | 1036 | True | False | 65 | 96 |
| trace_livecodebench_0.jsonl | 267 | livecodebench_0 | 1873_A | 267 | 1038 | True | False | 1 | 94 |
| trace_livecodebench_0.jsonl | 268 | livecodebench_0 | 1873_A | 268 | 1040 | True | False | 422 | 96 |
| trace_livecodebench_0.jsonl | 269 | livecodebench_0 | 1873_A | 269 | 1042 | True | False | 279 | 96 |
| trace_livecodebench_0.jsonl | 270 | livecodebench_0 | 1873_A | 270 | 1045 | True | False | 323 | 482 |
| trace_livecodebench_0.jsonl | 271 | livecodebench_0 | 1873_A | 271 | 1047 | True | False | 5885 | 834 |
| trace_livecodebench_0.jsonl | 272 | livecodebench_0 | 1873_A | 272 | 1049 | True | False | 433 | 99 |
| trace_livecodebench_0.jsonl | 274 | livecodebench_0 | 1873_A | 274 | 1052 | True | False | 98571 | 96 |
| trace_livecodebench_0.jsonl | 276 | livecodebench_0 | 1873_A | 276 | 1055 | True | False | 374 | 99 |
| trace_livecodebench_0.jsonl | 277 | livecodebench_0 | 1873_A | 277 | 1057 | True | False | 330 | 96 |
| trace_livecodebench_0.jsonl | 278 | livecodebench_0 | 1873_A | 278 | 1059 | True | False | 1442 | 3904 |
| trace_livecodebench_0.jsonl | 279 | livecodebench_0 | 1873_A | 279 | 1062 | True | False | 323 | 96 |
| trace_livecodebench_0.jsonl | 280 | livecodebench_0 | 1873_A | 280 | 1067 | True | False | 11 | 834 |
| trace_livecodebench_0.jsonl | 281 | livecodebench_0 | 1873_A | 281 | 1069 | True | False | 94929 | 99 |
| trace_livecodebench_0.jsonl | 282 | livecodebench_0 | 1873_A | 282 | 1073 | True | False | 902 | 103 |
| trace_livecodebench_0.jsonl | 284 | livecodebench_0 | 1873_A | 284 | 1076 | True | False | 1442 | 96 |
| trace_livecodebench_0.jsonl | 286 | livecodebench_0 | 1873_A | 286 | 1082 | True | False | 279 | 4181 |
| trace_livecodebench_0.jsonl | 287 | livecodebench_0 | 1873_A | 287 | 1084 | True | False | 11 | 270 |
| trace_livecodebench_0.jsonl | 288 | livecodebench_0 | 1873_A | 288 | 1088 | True | False | 9221 | 96 |
| trace_livecodebench_0.jsonl | 289 | livecodebench_0 | 1873_A | 289 | 1090 | True | False | 56977 | 96 |
| trace_livecodebench_0.jsonl | 290 | livecodebench_0 | 1873_A | 290 | 1092 | True | False | 374 | 103 |
| trace_livecodebench_0.jsonl | 291 | livecodebench_0 | 1873_A | 291 | 1095 | True | False | 3343 | 96 |
| trace_livecodebench_0.jsonl | 292 | livecodebench_0 | 1873_A | 292 | 1099 | True | False | 1648 | 265 |
| trace_livecodebench_0.jsonl | 294 | livecodebench_0 | 1873_A | 294 | 1103 | True | False | 330 | 482 |
| trace_livecodebench_0.jsonl | 295 | livecodebench_0 | 1873_A | 295 | 1106 | True | False | 449 | 3904 |
| trace_livecodebench_0.jsonl | 296 | livecodebench_0 | 1873_A | 296 | 1109 | True | False | 13 | 125 |
| trace_livecodebench_0.jsonl | 297 | livecodebench_0 | 1873_A | 297 | 1112 | True | False | 4320 | 265 |
| trace_livecodebench_0.jsonl | 298 | livecodebench_0 | 1873_A | 298 | 1114 | True | False | 279 | 96 |
| trace_livecodebench_0.jsonl | 299 | livecodebench_0 | 1873_A | 299 | 1119 | True | False | 374 | 975 |
| trace_livecodebench_0.jsonl | 300 | livecodebench_0 | 1873_A | 300 | 1121 | True | False | 3508 | 0 |
| trace_livecodebench_0.jsonl | 303 | livecodebench_0 | 1873_A | 303 | 1126 | True | False | 1139 | 130 |
| trace_livecodebench_0.jsonl | 304 | livecodebench_0 | 1873_A | 304 | 1131 | True | False | 13997 | 96 |
| trace_livecodebench_0.jsonl | 305 | livecodebench_0 | 1873_A | 305 | 1133 | True | False | 7041 | 0 |
| trace_livecodebench_0.jsonl | 306 | livecodebench_0 | 1873_A | 306 | 1136 | True | False | 382 | 125 |