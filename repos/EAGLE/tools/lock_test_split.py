#!/usr/bin/env python3
"""
P1.4: Split corpus by problem_id and lock test set.
Splits unique problem_ids into 50:25:25 (calibration:validation:test) ratio.
Writes test set problem_ids to splits/test_locked.json.
"""
import json
from pathlib import Path
import pandas as pd
import pyarrow.dataset as ds
import numpy as np

CORPUS_PATH = Path("/root/phase-entropy-cot/corpus/v1")
SPLITS_DIR = Path("/root/phase-entropy-cot/splits")
OUTPUT_FILE = SPLITS_DIR / "test_locked.json"

print("=" * 60)
print("P1.4: Lock Test Set by Problem ID")
print("=" * 60)

# Read the corpus
print("\nReading corpus...")
model_dir = CORPUS_PATH / "model=llama8b"
dataset = ds.dataset(str(model_dir), format='parquet')
table = dataset.to_table()
corpus_df = table.to_pandas()

print(f"Total corpus rows: {len(corpus_df)}")

# Add dataset column from summary
summary_file = CORPUS_PATH / 'summary.json'
with open(summary_file) as f:
    summary_data = json.load(f)

problem_to_dataset = {}
for entry in summary_data:
    problem_to_dataset[entry['problem_id']] = entry['dataset']

corpus_df['dataset'] = corpus_df['problem_id'].map(problem_to_dataset)

# Process each dataset separately
results = {}

for dataset_name in ['math500', 'livecodebench']:
    print(f"\n{'='*60}")
    print(f"Processing {dataset_name}...")
    print(f"{'='*60}")
    
    dataset_df = corpus_df[corpus_df['dataset'] == dataset_name]
    unique_problems = sorted(dataset_df['problem_id'].unique())
    
    print(f"Unique problems in {dataset_name}: {len(unique_problems)}")
    
    if len(unique_problems) == 0:
        print(f"WARNING: No problems found for {dataset_name}")
        results[dataset_name] = []
        continue
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Shuffle problem IDs
    shuffled_problems = np.random.permutation(unique_problems)
    
    # Compute split indices (50:25:25)
    n_total = len(shuffled_problems)
    n_calib = int(n_total * 0.50)
    n_val = int(n_total * 0.25)
    # n_test = n_total - n_calib - n_val
    
    calib_problems = shuffled_problems[:n_calib]
    val_problems = shuffled_problems[n_calib:n_calib+n_val]
    test_problems = shuffled_problems[n_calib+n_val:]
    
    print(f"Split: {len(calib_problems)} calib, {len(val_problems)} val, {len(test_problems)} test")
    print(f"Ratios: {len(calib_problems)/n_total:.1%} / {len(val_problems)/n_total:.1%} / {len(test_problems)/n_total:.1%}")
    
    # Add split column to corpus (for reference, though we only lock test)
    corpus_df.loc[corpus_df['problem_id'].isin(calib_problems), 'split'] = 'calibration'
    corpus_df.loc[corpus_df['problem_id'].isin(val_problems), 'split'] = 'validation'
    corpus_df.loc[corpus_df['problem_id'].isin(test_problems), 'split'] = 'test'
    
    # Store test problems
    results[dataset_name] = sorted([str(p) for p in test_problems])

# Write to splits/test_locked.json
print(f"\nWriting test set lock to {OUTPUT_FILE}...")
SPLITS_DIR.mkdir(exist_ok=True)

with open(OUTPUT_FILE, 'w') as f:
    json.dump(results, f, indent=2)

print(f"✓ Test set locked: {len(results['math500'])} math500 + {len(results['livecodebench'])} livecodebench problems")
print(f"✓ Output written to: {OUTPUT_FILE}")

# Print summary
print("\n" + "=" * 60)
print("SPLIT LOCKING SUMMARY")
print("=" * 60)
for dataset_name, test_ids in results.items():
    print(f"\n{dataset_name}:")
    print(f"  Test set size: {len(test_ids)} problems")
    if test_ids:
        print(f"  Sample test problems: {test_ids[:3]}")

print("\n✓ P1.4 COMPLETE: Test set is now LOCKED")
print("  Do not load these problems again until P4")
