#!/usr/bin/env python3

import unittest

import numpy as np
import pandas as pd

import level_controller as lc


class LevelControllerTests(unittest.TestCase):
    def test_safe_acceptance_run(self):
        accepted = np.array([True, True, False, True, True, True, False], dtype=bool)
        safe = lc.compute_safe_acceptance_run(accepted)
        self.assertEqual(safe.tolist(), [2, 1, 0, 3, 2, 1, 0])

    def test_ewma_shape_and_stability(self):
        x = np.array([1.0, np.nan, 3.0, 5.0], dtype=np.float64)
        y = lc.ewma(x, alpha=0.5)
        self.assertEqual(y.shape, x.shape)
        self.assertTrue(np.isfinite(y).all())
        self.assertAlmostEqual(float(y[0]), 1.0, places=6)

    def test_controller_shortens_when_risk_high(self):
        cfg = lc.ControllerConfig(max_length=8, candidate_lengths=(8, 6, 4, 2, 1))
        df = lc.make_synthetic_dataset(seed=11, n_traces=8, trace_len=80)
        df = lc.ensure_columns(df)
        df = lc.attach_features(df, cfg)
        cal, val = lc.split_calibration_validation(df, frac=0.5, seed=11)
        params = lc.fit_level_controller(cal, cfg)

        low = val.copy()
        low["entropy_ewma"] = np.nanpercentile(val["entropy_ewma"].to_numpy(), 10)
        low["top1_ewma"] = np.nanpercentile(val["top1_ewma"].to_numpy(), 90)

        high = val.copy()
        high["entropy_ewma"] = np.nanpercentile(val["entropy_ewma"].to_numpy(), 90)
        high["top1_ewma"] = np.nanpercentile(val["top1_ewma"].to_numpy(), 10)

        low_lengths = lc.apply_controller(low, cfg, params)
        high_lengths = lc.apply_controller(high, cfg, params)

        self.assertTrue(np.array_equal(np.unique(low_lengths), np.unique(high_lengths)) or np.mean(low_lengths) <= np.mean(high_lengths))

    def test_pipeline_runs_synthetic(self):
        class Args:
            input = None
            format = "synthetic"
            dataset = None
            split = None
            seed = 7
            calibration_frac = 0.5
            max_traces = 20
            out = None
            rejection_budget = 0.18
            max_length = 8
            alpha_entropy = 0.2
            alpha_top1 = 0.2
            cost_fixed = 4.0
            cost_variable = 1.0
            self_test = True

        results = lc.run_pipeline(Args())
        self.assertIn("controller", results)
        self.assertIn("baselines", results)
        self.assertIn("comparison", results)

        controller_rej = results["controller"]["validation"]["rejection_rate"]
        baseline_keys = sorted(results["baselines"].keys())
        self.assertGreater(len(baseline_keys), 0)
        self.assertTrue(0.0 <= controller_rej <= 1.0)

    def test_bin_collapse_detection_flags_single_length(self):
        diagnostic = lc.summarize_bin_diagnostics(
            risk=np.array([0.1, 0.2, 0.3, 0.4]),
            bin_edges=[0.0, 0.25, 0.5, 0.75, 1.0],
            bin_lengths=[1, 1, 1, 1],
            counts=np.array([1, 1, 1, 1]),
            mean_values=np.array([0.1, 0.2, 0.3, 0.4]),
            rejection_budget=0.12,
        )
        self.assertTrue(diagnostic["collapsed_to_single_length"])
        self.assertEqual(diagnostic["unique_lengths"], [1])

    def test_select_best_budget_prefers_adaptive_policy(self):
        rows = [
            {"budget": 0.12, "tokens_per_call": 0.90, "adaptive_policy": False, "distinct_lengths": [1]},
            {"budget": 0.30, "tokens_per_call": 0.88, "adaptive_policy": True, "distinct_lengths": [1, 2]},
            {"budget": 0.45, "tokens_per_call": 0.80, "adaptive_policy": True, "distinct_lengths": [1, 4]},
        ]
        selected = lc.select_best_budget_result(rows)
        self.assertIsNotNone(selected)
        self.assertEqual(selected["budget"], 0.30)

    def test_select_length_by_efficiency_prefers_normalized_throughput(self):
        tpc_by_length = {8: 4.0, 6: 3.6, 4: 2.8, 2: 2.0, 1: 0.9}
        selected = lc.select_length_by_efficiency((8, 6, 4, 2, 1), tpc_by_length, c_fixed=4.0, c_variable=1.0)
        self.assertEqual(selected, 6)

    def test_hmm_oracle_uses_efficiency_proxy_candidate_set(self):
        frame = pd.DataFrame(
            {
                "run_id": ["r0", "r1", "r2", "r3"],
                "step": [0, 1, 0, 1],
                "safe_run": [2, 2, 8, 8],
            }
        )
        h3 = pd.DataFrame(
            {
                "run_id": ["r0", "r1", "r2", "r3"],
                "step": [0, 1, 0, 1],
                "hmm_gamma": [0.2, 0.2, 0.8, 0.8],
            }
        )
        cfg = lc.ControllerConfig(max_length=8, candidate_lengths=(8, 6, 4, 2, 1), cost_fixed=4.0, cost_variable=1.0)
        lengths = lc.compute_hmm_oracle_lengths(frame, h3, cfg)
        self.assertEqual(lengths.tolist(), [2, 2, 8, 8])

    def test_split_frames_keep_calibration_and_validation_separate(self):
        df = lc.make_synthetic_dataset(seed=3, n_traces=6, trace_len=40)
        df = lc.ensure_columns(df)
        df["split"] = ["calibration"] * 120 + ["validation"] * 120
        df["problem_id"] = [f"p{i % 6}" for i in range(len(df))]
        featured = lc.attach_features(df, lc.ControllerConfig(max_length=8, candidate_lengths=(8, 6, 4, 2, 1)))
        cal, val = lc._split_featured_rows(featured)
        self.assertTrue(not cal.empty)
        self.assertTrue(not val.empty)
        self.assertEqual(set(cal["split"].unique()), {"calibration"})
        self.assertEqual(set(val["split"].unique()), {"validation"})

    def test_bootstrap_recovered_fraction_returns_ci(self):
        cfg = lc.ControllerConfig(max_length=8, candidate_lengths=(8, 6, 4, 2, 1), cost_fixed=4.0, cost_variable=1.0)
        df = lc.make_synthetic_dataset(seed=9, n_traces=6, trace_len=40)
        df = lc.ensure_columns(df)
        df = lc.attach_features(df, cfg)
        cal, val = lc.split_calibration_validation(df, frac=0.5, seed=9)
        params = lc.fit_level_controller(cal, cfg)
        h3 = pd.DataFrame(
            {
                "run_id": val["run_id"].astype(str),
                "step": val["step"],
                "hmm_gamma": 0.5,
            }
        )
        bootstrap = lc.bootstrap_recovered_fraction(val, h3, cfg, params, n_reps=20, seed=3)
        self.assertEqual(bootstrap["reps"], 20)
        self.assertEqual(len(bootstrap["ci"]), 2)
        self.assertGreaterEqual(bootstrap["ci"][0], 0.0)
        self.assertLessEqual(bootstrap["ci"][1], 1.0)


if __name__ == "__main__":
    unittest.main()
