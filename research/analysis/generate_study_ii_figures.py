#!/usr/bin/env python3
"""Generate publishable Study II figures from grouped CSV outputs.

Outputs:
- Figure1_HarmRate_ByCondition.{png,pdf}
- Figure1B_Delta_HarmRate.{png,pdf}
- Figure2_HarmTrajectory_ByTurn.{png,pdf}
- Figure3_FirstHarmTurn_Distribution.{png,pdf}
- Figure4_Repair_ByCondition.{png,pdf}
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

plt = None
np = None
pd = None


def load_deps() -> None:
    global plt, np, pd  # noqa: PLW0603
    try:
        import matplotlib.pyplot as _plt
        import numpy as _np
        import pandas as _pd
    except ModuleNotFoundError as exc:
        missing = exc.name or "unknown"
        print(f"missing dependency: {missing}")
        print("install with: python3 -m pip install -r research/environment/requirements.txt")
        sys.exit(1)

    plt = _plt
    np = _np
    pd = _pd


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
        "--curve-csv",
        default="research/data/study_ii/harm_curve_by_turn.csv",
        help="CSV with turn-level harm trajectory by scenario and condition",
    )
    parser.add_argument(
        "--first-harm-csv",
        default="research/data/study_ii/first_harm_turn_by_run.csv",
        help="CSV with first-harm turn per run",
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


def prepare_curve(curve_df: pd.DataFrame) -> pd.DataFrame:
    condition_col = find_col(curve_df, ["Condition", "condition"], "condition")
    turn_col = find_col(curve_df, ["Turn_Index", "turn_index", "turn", "Turn"], "turn index")
    rate_col = find_col(
        curve_df,
        ["harm_rate", "Harm_Rate", "mean_harm", "harm_rate_turn_level", "rate"],
        "harm rate",
    )
    out = curve_df[[condition_col, turn_col, rate_col]].copy()
    out.columns = ["condition", "turn_index", "harm_rate"]
    out["condition"] = normalize_condition(out["condition"])
    out["turn_index"] = pd.to_numeric(out["turn_index"], errors="coerce")
    out["harm_rate"] = pd.to_numeric(out["harm_rate"], errors="coerce")
    out = out.dropna(subset=["turn_index", "harm_rate"])
    return (
        out.groupby(["condition", "turn_index"], as_index=False)["harm_rate"]
        .mean()
        .sort_values(["condition", "turn_index"])
    )


def prepare_first_harm(first_harm_df: pd.DataFrame) -> pd.DataFrame:
    condition_col = find_col(first_harm_df, ["Condition", "condition"], "condition")
    turn_col = find_col(
        first_harm_df,
        ["first_harm_turn", "First_Harm_Turn", "first_turn", "First_Turn"],
        "first harm turn",
    )
    out = first_harm_df[[condition_col, turn_col]].copy()
    out.columns = ["condition", "first_harm_turn"]
    out["condition"] = normalize_condition(out["condition"])
    out["first_harm_turn"] = pd.to_numeric(out["first_harm_turn"], errors="coerce")
    out = out.dropna(subset=["first_harm_turn"])
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


def trajectory_line(curve_df: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    colors = {"baseline": "#607196", "ikwe": "#2a9d8f"}

    for condition in sorted(curve_df["condition"].unique()):
        subset = curve_df[curve_df["condition"] == condition].sort_values("turn_index")
        ax.plot(
            subset["turn_index"],
            subset["harm_rate"],
            marker="o",
            linewidth=2.0,
            label=condition,
            color=colors.get(condition, "#444444"),
        )

    ax.set_xlabel("Turn Index")
    ax.set_ylabel("Mean Harm Rate (Proportion Flagged)")
    ax.set_title("Figure 2. Harm Trajectory Across Turns by Condition", pad=8)
    ax.set_ylim(0.0, 1.05)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper left")
    return fig


def first_harm_distribution(first_harm_df: pd.DataFrame) -> plt.Figure:
    max_turn = int(first_harm_df["first_harm_turn"].max())
    x = np.arange(1, max_turn + 1)
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    colors = {"baseline": "#607196", "ikwe": "#2a9d8f"}

    for condition in sorted(first_harm_df["condition"].unique()):
        subset = first_harm_df[first_harm_df["condition"] == condition]["first_harm_turn"].to_numpy()
        y = np.array([(subset <= t).mean() for t in x], dtype=float)
        ax.step(x, y, where="post", linewidth=2.0, label=condition, color=colors.get(condition, "#444444"))
        ax.plot(x, y, marker="o", linewidth=0, color=colors.get(condition, "#444444"))

    ax.set_xlabel("Turn Index")
    ax.set_ylabel("Cumulative Proportion of Runs With First Harm")
    ax.set_title("Figure 3. First Harm Turn Distribution by Condition", pad=8)
    ax.set_ylim(0.0, 1.05)
    ax.set_xticks(x)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower right")
    return fig


def main() -> int:
    args = parse_args()
    load_deps()
    harm_path = Path(args.harm_csv)
    repair_path = Path(args.repair_csv)
    curve_path = Path(args.curve_csv)
    first_harm_path = Path(args.first_harm_csv)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    base_style()

    if not harm_path.exists():
        print(f"missing harm input: {harm_path}")
        print("add harm_rate_condition_comparison.csv and rerun")
        return 1

    harm_df = pd.read_csv(harm_path)
    harm = prepare_harm(harm_df)

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

    if curve_path.exists():
        curve_df = pd.read_csv(curve_path)
        curve = prepare_curve(curve_df)
        fig2 = trajectory_line(curve)
        save_fig(fig2, outdir, "Figure2_HarmTrajectory_ByTurn")
        plt.close(fig2)
    else:
        print(f"skipped Figure 2 (missing input): {curve_path}")

    if first_harm_path.exists():
        first_harm_df = pd.read_csv(first_harm_path)
        first_harm = prepare_first_harm(first_harm_df)
        fig3 = first_harm_distribution(first_harm)
        save_fig(fig3, outdir, "Figure3_FirstHarmTurn_Distribution")
        plt.close(fig3)
    else:
        print(f"skipped Figure 3 (missing input): {first_harm_path}")

    if repair_path.exists():
        repair_df = pd.read_csv(repair_path)
        repair = prepare_repair(repair_df)
        fig4 = grouped_bar(
            repair,
            value_col="repair_mean",
            ylabel="Mean Repair Level (Raw Coding Scale)",
            title="Figure 4. Repair Mean by Condition Across Scenarios",
            baseline_color="#607196",
            ikwe_color="#2a9d8f",
        )
        save_fig(fig4, outdir, "Figure4_Repair_ByCondition")
        plt.close(fig4)
    else:
        print(f"skipped Figure 4 (missing input): {repair_path}")

    print("figure generation complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
