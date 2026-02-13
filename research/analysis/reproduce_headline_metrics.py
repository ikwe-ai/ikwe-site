#!/usr/bin/env python3
"""Recompute draft headline metrics for the Ikwe Governance Benchmark v0.3."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
from pathlib import Path

import pandas as pd


def wilson_interval(x: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if n <= 0:
        return (float("nan"), float("nan"))
    p = x / n
    denom = 1 + (z * z) / n
    center = (p + (z * z) / (2 * n)) / denom
    half = z * math.sqrt((p * (1 - p) + (z * z) / (4 * n)) / n) / denom
    return (center - half, center + half)


def delta_ci_newcombe_wilson(
    x1: int,
    n1: int,
    x2: int,
    n2: int,
    z: float = 1.959963984540054,
) -> tuple[float, float, float]:
    if n1 <= 0 or n2 <= 0:
        return (float("nan"), float("nan"), float("nan"))
    p1 = x1 / n1
    p2 = x2 / n2
    l1, u1 = wilson_interval(x1, n1, z=z)
    l2, u2 = wilson_interval(x2, n2, z=z)
    delta = p1 - p2
    low = l1 - u2
    high = u1 - l2
    return (delta, low, high)


def load_scored_turns(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    base_fields = [
        "SSF1",
        "SSF2",
        "SSF3",
        "SSF4",
        "SSF5",
        "SSF6",
        "SSF7",
        "Harm_Indicator",
        "Repair_Level",
        "Pathway",
        "Notes",
    ]

    for base in base_fields:
        alt = f"{base}.1"
        if base in df.columns and alt in df.columns:
            df[base] = df[base].replace("", pd.NA).fillna(df[alt])
        elif base not in df.columns and alt in df.columns:
            df[base] = df[alt]

    drop_cols = [c for c in df.columns if c.endswith(".1")]
    if drop_cols:
        df = df.drop(columns=drop_cols)

    numeric_cols = [
        "SSF1",
        "SSF2",
        "SSF3",
        "SSF4",
        "SSF5",
        "SSF6",
        "SSF7",
        "Harm_Indicator",
        "Repair_Level",
        "Turn_Index",
        "Intensity_Level",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scored", default="research/data/study_ii/study_ii_turns_scored.csv")
    parser.add_argument("--scenarios", default="research/data/study_ii/scenarios.json")
    parser.add_argument("--output", default="research/benchmark/headline_metrics_v0.3.json")
    args = parser.parse_args()

    scored_path = Path(args.scored)
    scenarios_path = Path(args.scenarios)
    output_path = Path(args.output)

    df = load_scored_turns(scored_path)

    harm = df["Harm_Indicator"].dropna()
    x = int((harm == 1).sum())
    n = int(harm.shape[0])
    p = (x / n) if n else float("nan")
    ci_low, ci_high = wilson_interval(x, n)

    by_condition = []
    condition_counts: dict[str, dict[str, int]] = {}
    for condition, sub in df.groupby("Condition"):
        harm_sub = sub["Harm_Indicator"].dropna()
        x_c = int((harm_sub == 1).sum())
        n_c = int(harm_sub.shape[0])
        condition_counts[condition] = {"x": x_c, "n": n_c}
        p_c = (x_c / n_c) if n_c else float("nan")
        lo_c, hi_c = wilson_interval(x_c, n_c)
        by_condition.append(
            {
                "condition": condition,
                "harm_x": x_c,
                "harm_n": n_c,
                "harm_rate": p_c,
                "harm_rate_wilson_95": [lo_c, hi_c],
                "repair_level_mean": float(sub["Repair_Level"].mean()),
            }
        )

    by_scenario_condition = []
    for (scenario_id, condition), sub in df.groupby(["Scenario_ID", "Condition"]):
        harm_sub = sub["Harm_Indicator"].dropna()
        x_sc = int((harm_sub == 1).sum())
        n_sc = int(harm_sub.shape[0])
        p_sc = (x_sc / n_sc) if n_sc else float("nan")
        lo_sc, hi_sc = wilson_interval(x_sc, n_sc)
        by_scenario_condition.append(
            {
                "scenario_id": scenario_id,
                "condition": condition,
                "harm_x": x_sc,
                "harm_n": n_sc,
                "harm_rate": p_sc,
                "harm_rate_wilson_95": [lo_sc, hi_sc],
            }
        )

    scenario_delta_ikwe_minus_baseline = []
    for scenario_id, sub in df.groupby("Scenario_ID"):
        ikwe = sub[sub["Condition"] == "ikwe"]["Harm_Indicator"].dropna()
        baseline = sub[sub["Condition"] == "baseline"]["Harm_Indicator"].dropna()
        if ikwe.empty or baseline.empty:
            continue
        x_i = int((ikwe == 1).sum())
        n_i = int(ikwe.shape[0])
        x_b = int((baseline == 1).sum())
        n_b = int(baseline.shape[0])
        d, d_lo, d_hi = delta_ci_newcombe_wilson(x_i, n_i, x_b, n_b)
        scenario_delta_ikwe_minus_baseline.append(
            {
                "scenario_id": scenario_id,
                "delta": d,
                "delta_newcombe_wilson_95": [d_lo, d_hi],
            }
        )

    ssf_cols = [c for c in ["SSF1", "SSF2", "SSF3", "SSF4", "SSF5", "SSF6", "SSF7"] if c in df.columns]
    ssf_any_by_condition = {}
    if ssf_cols:
        ssf_any = (df[ssf_cols].fillna(0).sum(axis=1) > 0).astype(int)
        ssf_any_by_condition = {
            cond: float(rate)
            for cond, rate in ssf_any.groupby(df["Condition"]).mean().to_dict().items()
        }

    first_harm = (
        df[df["Harm_Indicator"] == 1]
        .groupby(["Run_ID", "Condition"], as_index=False)["Turn_Index"]
        .min()
        .groupby("Condition")["Turn_Index"]
        .mean()
        .to_dict()
    )

    condition_delta_ikwe_minus_baseline = None
    if "ikwe" in condition_counts and "baseline" in condition_counts:
        x_i = condition_counts["ikwe"]["x"]
        n_i = condition_counts["ikwe"]["n"]
        x_b = condition_counts["baseline"]["x"]
        n_b = condition_counts["baseline"]["n"]
        d, d_lo, d_hi = delta_ci_newcombe_wilson(x_i, n_i, x_b, n_b)
        condition_delta_ikwe_minus_baseline = {
            "delta": d,
            "delta_newcombe_wilson_95": [d_lo, d_hi],
        }

    scenario_count_manifest = None
    if scenarios_path.exists():
        try:
            scenario_raw = json.loads(scenarios_path.read_text(encoding="utf-8"))
            if isinstance(scenario_raw, list):
                scenario_count_manifest = len(scenario_raw)
        except json.JSONDecodeError:
            scenario_count_manifest = None

    payload = {
        "benchmark": "Ikwe Governance Benchmark",
        "benchmark_version": "v0.3.0-draft",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_files": {
            "scored_turns": str(scored_path),
            "scenarios": str(scenarios_path),
        },
        "coverage": {
            "scored_rows": int(len(df)),
            "scored_runs": int(df["Run_ID"].nunique()) if "Run_ID" in df.columns else None,
            "scored_scenarios": int(df["Scenario_ID"].nunique()) if "Scenario_ID" in df.columns else None,
            "scored_models": int(df["Model_ID"].nunique()) if "Model_ID" in df.columns else None,
            "manifest_scenarios": scenario_count_manifest,
        },
        "headline": {
            "harm_indicator": {
                "x": x,
                "n": n,
                "rate": p,
                "wilson_95": [ci_low, ci_high],
            }
        },
        "by_condition": by_condition,
        "by_scenario_condition": by_scenario_condition,
        "condition_delta_ikwe_minus_baseline": condition_delta_ikwe_minus_baseline,
        "scenario_delta_ikwe_minus_baseline": scenario_delta_ikwe_minus_baseline,
        "ssf_any_rate_by_condition": ssf_any_by_condition,
        "first_harm_turn_mean_by_condition": {k: float(v) for k, v in first_harm.items()},
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print("Benchmark v0.3 headline metrics recomputed")
    print(f"- Harm indicator: {x}/{n} = {p:.4f}")
    print(f"- Wilson 95% CI: [{ci_low:.4f}, {ci_high:.4f}]")
    print(f"- Conditions: {', '.join(sorted(df['Condition'].dropna().unique().tolist()))}")
    print(f"- Output: {output_path}")


if __name__ == "__main__":
    main()
