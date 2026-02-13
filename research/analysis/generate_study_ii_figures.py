#!/usr/bin/env python3
"""Generate publishable Study II figures from grouped CSV outputs.

Outputs:
- Figure1_HarmRate_ByCondition.{png,pdf}
- Figure1B_Delta_HarmRate.{png,pdf}
- Figure2_Repair_ByCondition.{png,pdf}
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
except ModuleNotFoundError as exc:
    missing = exc.name or "unknown"
    print(f"missing dependency: {missing}")
    print("install with: pip install -r research/environment/requirements.txt")
    sys.exit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Study II paper figures")
    parser.add_argument(
        "--harm-csv",
        default="research/data/study_ii/harm_rate_condition_comparison.csv",
        help="CSV with harm-rate by scenario and condition",
    )
    parser.add_argument(
        "--repair-csv",
        default="research/data/study_ii/repair_mean_by_group.csv",
        help="CSV with repair means by scenario and condition",
    )
    parser.add_argument(
        "--outdir",
        default="research/figures",
        help="Output directory for PNG/PDF figures",
    )
    return parser.parse_args()


def find_col(df: pd.DataFrame, candidates: list[str], label: str) -> str:
    for col in candidates:
        if col in df.columns:
            return col
    raise KeyError(f"Missing {label} column. Tried: {candidates}")


def save_fig(fig: plt.Figure, outdir: Path, stem: str) -> None:
    png = outdir / f"{stem}.png"
    pdf = outdir / f"{stem}.pdf"
    fig.savefig(png, dpi=300, bbox_inches="tight")
    fig.savefig(pdf, bbox_inches="tight")
    print(f"wrote {png}")
    print(f"wrote {pdf}")


def base_style() -> None:
    plt.style.use("default")
    plt.rcParams.update(
        {
            "font.size": 10,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "legend.fontsize": 9,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": "#3d4351",
            "axes.grid": True,
            "grid.color": "#d8dce5",
            "grid.linestyle": "-",
            "grid.linewidth": 0.6,
            "grid.alpha": 0.9,
        }
    )


def normalize_condition(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower()


def prepare_harm(harm_df: pd.DataFrame) -> pd.DataFrame:
    scenario_col = find_col(harm_df, ["Scenario_ID", "scenario_id", "scenario", "Scenario"], "scenario")
    condition_col = find_col(harm_df, ["Condition", "condition"], "condition")

    if any(
        c in harm_df.columns
        for c in ["harm_rate", "Harm_Rate", "harm_rate_turn_level", "rate", "mean_harm"]
    ):
        rate_col = find_col(
            harm_df,
            ["harm_rate", "Harm_Rate", "harm_rate_turn_level", "rate", "mean_harm"],
            "harm rate",
        )
        out = harm_df[[scenario_col, condition_col, rate_col]].copy()
        out.columns = ["scenario", "condition", "harm_rate"]
    else:
        k_col = find_col(
            harm_df,
            ["k", "harm_turns", "harm_k", "Harm_Turns"],
            "harm count (k)",
        )
        n_col = find_col(
            harm_df,
            ["n", "total_turns", "N", "Total_Turns"],
            "total turns (n)",
        )
        out = harm_df[[scenario_col, condition_col, k_col, n_col]].copy()
        out.columns = ["scenario", "condition", "k", "n"]
        out["harm_rate"] = out["k"] / out["n"]
        out = out[["scenario", "condition", "harm_rate"]]

    out["condition"] = normalize_condition(out["condition"])
    return out


def prepare_repair(repair_df: pd.DataFrame) -> pd.DataFrame:
    scenario_col = find_col(repair_df, ["Scenario_ID", "scenario_id", "scenario", "Scenario"], "scenario")
    condition_col = find_col(repair_df, ["Condition", "condition"], "condition")
    repair_col = find_col(
        repair_df,
        [
            "repair_mean",
            "Repair_Mean",
            "mean_repair",
            "Repair_Level_Mean",
            "repair_level_mean",
            "Repair_Level.1",
        ],
        "repair mean",
    )

    out = repair_df[[scenario_col, condition_col, repair_col]].copy()
    out.columns = ["scenario", "condition", "repair_mean"]
    out["condition"] = normalize_condition(out["condition"])
    return out


def grouped_bar(
    df: pd.DataFrame,
    value_col: str,
    ylabel: str,
    title: str,
    baseline_color: str,
    ikwe_color: str,
) -> plt.Figure:
    piv = df.pivot_table(index="scenario", columns="condition", values=value_col, aggfunc="mean")
    scenarios = list(piv.index)

    if "baseline" not in piv.columns or "ikwe" not in piv.columns:
        raise ValueError("Need both baseline and ikwe conditions to plot grouped bars")

    x = np.arange(len(scenarios))
    width = 0.36

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.bar(x - width / 2, piv["baseline"].values, width, label="Baseline", color=baseline_color)
    ax.bar(x + width / 2, piv["ikwe"].values, width, label="Ikwe", color=ikwe_color)

    ax.set_xticks(x)
    ax.set_xticklabels(scenarios)
    ax.set_ylabel(ylabel)
    ax.set_title(title, pad=8)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper left")
    return fig


def delta_bar(harm_df: pd.DataFrame) -> plt.Figure:
    piv = harm_df.pivot_table(index="scenario", columns="condition", values="harm_rate", aggfunc="mean")
    if "baseline" not in piv.columns or "ikwe" not in piv.columns:
        raise ValueError("Need both baseline and ikwe conditions to compute delta")

    delta = (piv["ikwe"] - piv["baseline"]).sort_index()
    x = np.arange(len(delta))

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    colors = ["#bb3e03" if v > 0 else "#1b7f5a" for v in delta.values]
    ax.bar(x, delta.values, color=colors, width=0.55)
    ax.axhline(0, color="#3d4351", linewidth=1.0)
    ax.set_xticks(x)
    ax.set_xticklabels(delta.index.tolist())
    ax.set_ylabel("Delta Harm Rate (Ikwe - Baseline)")
    ax.set_title("Figure 1B. Change in Harm Rate by Scenario", pad=8)
    ax.set_axisbelow(True)
    return fig


def main() -> int:
    args = parse_args()
    harm_path = Path(args.harm_csv)
    repair_path = Path(args.repair_csv)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    base_style()

    if not harm_path.exists():
        print(f"missing harm input: {harm_path}")
        print("add harm_rate_condition_comparison.csv and rerun")
        return 1

    if not repair_path.exists():
        print(f"missing repair input: {repair_path}")
        print("add repair_mean_by_group.csv and rerun")
        return 1

    harm_df = pd.read_csv(harm_path)
    repair_df = pd.read_csv(repair_path)

    harm = prepare_harm(harm_df)
    repair = prepare_repair(repair_df)

    fig1 = grouped_bar(
        harm,
        value_col="harm_rate",
        ylabel="Harm Rate (Proportion of Turns)",
        title="Figure 1. Harm Rate by Condition Across Scenarios",
        baseline_color="#607196",
        ikwe_color="#2a9d8f",
    )
    save_fig(fig1, outdir, "Figure1_HarmRate_ByCondition")
    plt.close(fig1)

    fig1b = delta_bar(harm)
    save_fig(fig1b, outdir, "Figure1B_Delta_HarmRate")
    plt.close(fig1b)

    fig2 = grouped_bar(
        repair,
        value_col="repair_mean",
        ylabel="Mean Repair Level (Raw Coding Scale)",
        title="Figure 2. Repair Mean by Condition Across Scenarios",
        baseline_color="#607196",
        ikwe_color="#2a9d8f",
    )
    save_fig(fig2, outdir, "Figure2_Repair_ByCondition")
    plt.close(fig2)

    print("figure generation complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
