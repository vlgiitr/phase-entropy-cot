#!/usr/bin/env python3
"""
Repartition corpus to include 'split' in the partition columns.
Reads the current corpus and writes it back with split='none' in the partition structure.
"""
import shutil
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.dataset as ds
from pathlib import Path

CORPUS_PATH = Path("/root/phase-entropy-cot/corpus/v1")

print("Reading corpus from current partitioning...")
# Read only the partitioned parquet directories, excluding non-parquet files
# The actual partitions start with model= 
model_dir = CORPUS_PATH / "model=llama8b"

# If it doesn't exist (already deleted), restore from backup
if not model_dir.exists():
    backup_path = CORPUS_PATH.with_stem("v1_backup_original_partition")
    if backup_path.exists():
        print(f"model=llama8b directory not found, restoring from backup...")
        model_dir_backup = backup_path / "model=llama8b"
        shutil.copytree(model_dir_backup, model_dir)
        print(f"Restored to: {model_dir}")
    else:
        print("ERROR: Neither model=llama8b nor backup found!")
        exit(1)

print(f"Reading partition from: {model_dir}")
dataset = ds.dataset(str(model_dir), format='parquet')

# Read with partitions included in the table
table = dataset.to_table()
corpus_df = table.to_pandas()

print(f"Loaded {len(corpus_df)} rows with {len(corpus_df.columns)} columns")

# Add partition columns
# model and drafter are constant for this corpus
corpus_df['model'] = 'llama8b'
corpus_df['drafter'] = 'EAGLE-3'
corpus_df['temperature'] = 0

# Read dataset from summary.json using problem_id as key
print("Reading dataset information from summary.json...")
import json
summary_file = CORPUS_PATH / 'summary.json'
if summary_file.exists():
    with open(summary_file) as f:
        summary_data = json.load(f)
    
    # Create a mapping from problem_id to dataset
    problem_to_dataset = {}
    for entry in summary_data:
        problem_to_dataset[entry['problem_id']] = entry['dataset']
    
    # Apply the mapping to corpus_df
    corpus_df['dataset'] = corpus_df['problem_id'].map(problem_to_dataset)
    
    unmapped = corpus_df['dataset'].isna().sum()
    if unmapped > 0:
        print(f"WARNING: {unmapped} rows could not be mapped to a dataset")
else:
    print("ERROR: summary.json not found!")
    corpus_df['dataset'] = 'unknown'

print(f"Loaded {len(corpus_df)} rows")
print(f"Columns: {list(corpus_df.columns)}")

# Verify split column exists and has correct value
if "split" not in corpus_df.columns:
    print("ERROR: 'split' column not found in corpus!")
    exit(1)

print(f"Split values: {corpus_df['split'].unique()}")

# Backup the current corpus
backup_path = CORPUS_PATH.with_stem("v1_backup_original_partition")
if backup_path.exists():
    shutil.rmtree(backup_path)
shutil.copytree(CORPUS_PATH, backup_path)
print(f"Backed up original corpus to {backup_path}")

# Remove old partition directories (keep only traces and summary.json)
for item in CORPUS_PATH.iterdir():
    if item.is_dir() and item.name not in ["traces"]:
        print(f"Removing {item.name}")
        shutil.rmtree(item)

# Write corpus with new partition columns including split
print("Writing corpus with new partitioning (model, drafter, dataset, temperature, split)...")
table = pa.Table.from_pandas(corpus_df)
pq.write_to_dataset(
    table,
    root_path=str(CORPUS_PATH),
    partition_cols=["model", "drafter", "dataset", "temperature", "split"],
    existing_data_behavior="delete_matching"
)

print(f"Corpus repartitioned successfully!")
print(f"New structure at {CORPUS_PATH}")

# Verify the new structure
new_dirs = [d.name for d in CORPUS_PATH.iterdir() if d.is_dir() and d.name.startswith("model=")]
print(f"New partition directories: {new_dirs}")
