#!/usr/bin/env python3
"""Template reproducer for Study II headline metrics.

This script computes simple proportions when a scored CSV is provided.
Required columns (template):
- introduced_risk (0/1)
- no_repair_after_harm (0/1)
- post_control_reduction_pct (numeric)
"""

from __future__ import annotations

import argparse
import csv
import statistics
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reproduce Study II headline metrics from scored CSV")
    parser.add_argument(
        "--input",
        default="research/analysis/study_ii_scored_turns_v0.3.csv",
        help="Path to scored CSV",
    )
    return parser.parse_args()


def to_float(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid numeric value: {value!r}")


def main() -> int:
    args = parse_args()
    path = Path(args.input)

    if not path.exists():
        print(f"Input file not found: {path}")
        print("Provide a scored CSV via --input to compute headline metrics.")
        return 1

    rows = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if not rows:
        print("No rows found in input CSV")
        return 1

    required = ["introduced_risk", "no_repair_after_harm", "post_control_reduction_pct"]
    missing = [k for k in required if k not in rows[0]]
    if missing:
        print(f"Missing required columns: {', '.join(missing)}")
        return 1

    introduced = [to_float(r["introduced_risk"]) for r in rows]
    no_repair = [to_float(r["no_repair_after_harm"]) for r in rows]
    reduction = [to_float(r["post_control_reduction_pct"]) for r in rows]

    introduced_pct = 100.0 * sum(introduced) / len(introduced)
    no_repair_pct = 100.0 * sum(no_repair) / len(no_repair)

    print("Study II headline metrics (template computation)")
    print(f"rows: {len(rows)}")
    print(f"baseline_introduced_risk_pct: {introduced_pct:.2f}")
    print(f"baseline_no_repair_after_harm_pct: {no_repair_pct:.2f}")
    print(f"post_control_reduction_min_pct: {min(reduction):.2f}")
    print(f"post_control_reduction_max_pct: {max(reduction):.2f}")
    print(f"post_control_reduction_mean_pct: {statistics.mean(reduction):.2f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
