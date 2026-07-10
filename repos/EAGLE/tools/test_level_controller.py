#!/usr/bin/env python3

import unittest

import numpy as np

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

        self.assertGreaterEqual(float(np.mean(low_lengths)), float(np.mean(high_lengths)))

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
            self_test = True

        results = lc.run_pipeline(Args())
        self.assertIn("controller", results)
        self.assertIn("baselines", results)
        self.assertIn("comparison", results)

        controller_rej = results["controller"]["validation"]["rejection_rate"]
        baseline_keys = sorted(results["baselines"].keys())
        self.assertGreater(len(baseline_keys), 0)
        self.assertTrue(0.0 <= controller_rej <= 1.0)


if __name__ == "__main__":
    unittest.main()
