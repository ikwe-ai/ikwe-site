#!/usr/bin/env python3
"""Generate publishable Study II figures from grouped CSV outputs.

Outputs:
- Figure1_HarmRate_ByCondition.{png,pdf}
- Figure1B_Delta_HarmRate.{png,pdf}
- Figure2_HarmTrajectory_ByTurn.{png,pdf}
- Figure3A_RepairAdequacy_Trajectory.{png,pdf}
- Figure3B_MeanRepairScore_Trajectory.{png,pdf}
- Figure4_FirstHarm_SurvivalCurve.{png,pdf}
- Figure5_UnresolvedHarm_Curve.{png,pdf}
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
        "--turns-csv",
        default="research/data/study_ii/study_ii_turns_scored.csv",
        help="CSV with turn-level scored records used for Figures 3A/3B/5",
    )
    parser.add_argument(
        "--repair-ra-value",
        type=float,
        default=2.0,
        help="Numeric repair code representing R-A (adequate repair)",
    )
    parser.add_argument(
        "--repair-ri-value",
        type=float,
        default=1.0,
        help="Numeric repair code representing R-I",
    )
    parser.add_argument(
        "--repair-r0-value",
        type=float,
        default=0.0,
        help="Numeric repair code representing R-0 or N/A fallback",
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


def parse_harm_indicator(series: pd.Series) -> pd.Series:
    normalized = series.astype(str).str.strip().str.lower()
    true_set = {"1", "true", "yes", "y", "harm", "high"}
    false_set = {"0", "false", "no", "n", "", "nan", "none", "safe"}
    out = pd.Series(index=series.index, dtype=bool)
    out.loc[normalized.isin(true_set)] = True
    out.loc[normalized.isin(false_set)] = False

    unknown_mask = ~(normalized.isin(true_set | false_set))
    if unknown_mask.any():
        numeric = pd.to_numeric(series[unknown_mask], errors="coerce")
        out.loc[unknown_mask] = numeric.fillna(0) > 0

    return out.fillna(False)


def parse_repair_score(series: pd.Series, ra_value: float, ri_value: float, r0_value: float) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    if numeric.notna().any():
        return numeric

    normalized = series.astype(str).str.strip().str.lower()
    mapping = {
        "r-a": ra_value,
        "ra": ra_value,
        "adequate": ra_value,
        "r-i": ri_value,
        "ri": ri_value,
        "r-0": r0_value,
        "r0": r0_value,
        "n/a": np.nan,
        "na": np.nan,
        "none": np.nan,
        "": np.nan,
    }
    return normalized.map(mapping)


def prepare_turns(turns_df: pd.DataFrame, args: argparse.Namespace) -> pd.DataFrame:
    condition_col = find_col(turns_df, ["Condition", "condition"], "condition")
    turn_col = find_col(turns_df, ["Turn_Index", "turn_index", "turn", "Turn"], "turn index")
    harm_col = find_col(
        turns_df,
        ["Harm_Indicator.1", "Harm_Indicator", "harm_indicator", "Harm"],
        "harm indicator",
    )
    repair_col = find_col(
        turns_df,
        ["Repair_Level.1", "Repair_Level", "repair_level", "Repair"],
        "repair level",
    )

    out = turns_df[[condition_col, turn_col, harm_col, repair_col]].copy()
    out.columns = ["condition", "turn_index", "harm", "repair_raw"]
    out["condition"] = normalize_condition(out["condition"])
    out["turn_index"] = pd.to_numeric(out["turn_index"], errors="coerce")
    out["harm"] = parse_harm_indicator(out["harm"])
    out["repair_score"] = parse_repair_score(
        out["repair_raw"],
        args.repair_ra_value,
        args.repair_ri_value,
        args.repair_r0_value,
    )
    out["is_ra"] = (out["repair_score"] == args.repair_ra_value).fillna(False)
    out = out.dropna(subset=["turn_index"]).copy()
    return out


def grouped_bar(harm_df: pd.DataFrame) -> plt.Figure:
    piv = harm_df.pivot_table(index="scenario", columns="condition", values="harm_rate", aggfunc="mean")
    if "baseline" not in piv.columns or "ikwe" not in piv.columns:
        raise ValueError("Need both baseline and ikwe conditions to plot Figure 1")

    x = np.arange(len(piv.index))
    width = 0.36

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.bar(x - width / 2, piv["baseline"].values, width, label="baseline", color="#1f77b4")
    ax.bar(x + width / 2, piv["ikwe"].values, width, label="ikwe", color="#ff7f0e")
    ax.set_xticks(x)
    ax.set_xticklabels(piv.index.tolist())
    ax.set_ylabel("Harm Rate (proportion of turns flagged)")
    ax.set_xlabel("Scenario")
    ax.set_title("Figure 1. Harm Rate by Condition (Baseline vs Ikwe)", pad=8)
    ax.set_ylim(0.0, 1.05)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right")
    return fig


def delta_bar(harm_df: pd.DataFrame) -> plt.Figure:
    piv = harm_df.pivot_table(index="scenario", columns="condition", values="harm_rate", aggfunc="mean")
    if "baseline" not in piv.columns or "ikwe" not in piv.columns:
        raise ValueError("Need both baseline and ikwe conditions to compute delta")

    delta = (piv["ikwe"] - piv["baseline"]).sort_index()
    x = np.arange(len(delta))

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    colors = ["#1f77b4" if v > 0 else "#2ca02c" for v in delta.values]
    ax.bar(x, delta.values, color=colors, width=0.55)
    ax.axhline(0, color="#3d4351", linewidth=1.0)
    ax.set_xticks(x)
    ax.set_xticklabels(delta.index.tolist())
    ax.set_ylabel("Delta Harm Rate (Ikwe - Baseline)")
    ax.set_xlabel("Scenario")
    ax.set_title("Figure 1B. Change in Harm Rate Under Ikwe Condition", pad=8)
    ax.set_axisbelow(True)
    return fig


def trajectory_line(curve_df: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    colors = {"baseline": "#1f77b4", "ikwe": "#ff7f0e"}

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
    ax.set_ylabel("Mean Harm Rate (proportion flagged)")
    ax.set_title("Figure 2. Harm Trajectory Across Turns by Condition", pad=8)
    ax.set_ylim(0.0, 1.05)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper left")
    return fig


def first_harm_survival(first_harm_df: pd.DataFrame) -> plt.Figure:
    if first_harm_df.empty:
        raise ValueError("first_harm_turn_by_run.csv has no numeric first-harm rows")

    max_turn = int(first_harm_df["first_harm_turn"].max())
    x = np.arange(0, max_turn + 1)
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    colors = {"baseline": "#1f77b4", "ikwe": "#ff7f0e"}

    for condition in sorted(first_harm_df["condition"].unique()):
        subset = first_harm_df[first_harm_df["condition"] == condition]["first_harm_turn"].to_numpy()
        y = np.array([(subset > t).mean() for t in x], dtype=float)
        ax.step(x, y, where="post", linewidth=2.0, label=condition, color=colors.get(condition, "#444444"))

    ax.set_xlabel("Turn Index")
    ax.set_ylabel("Survival (P(no harm detected yet))")
    ax.set_title("Figure 4. First-Harm Survival Curve (Kaplan-Meier style)", pad=8)
    ax.set_ylim(0.0, 1.05)
    ax.set_xticks(x)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right")
    return fig


def aggregate_turn_metric(turns_df: pd.DataFrame, value_col: str, harm_only: bool = False) -> pd.DataFrame:
    frame = turns_df.copy()
    if harm_only:
        frame = frame[frame["harm"]].copy()
    grouped = (
        frame.groupby(["condition", "turn_index"], as_index=False)[value_col]
        .mean()
        .sort_values(["condition", "turn_index"])
    )

    # Fill missing condition/turn pairs with 0.0 for stable trajectory plotting.
    if grouped.empty:
        return grouped

    conditions = sorted(grouped["condition"].unique().tolist())
    turns = sorted(turns_df["turn_index"].dropna().unique().tolist())
    grid = pd.MultiIndex.from_product([conditions, turns], names=["condition", "turn_index"]).to_frame(index=False)
    merged = grid.merge(grouped, on=["condition", "turn_index"], how="left")
    merged[value_col] = merged[value_col].fillna(0.0)
    return merged


def two_line_trajectory(df: pd.DataFrame, value_col: str, title: str, ylabel: str, stem: str, outdir: Path) -> None:
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    colors = {"baseline": "#1f77b4", "ikwe": "#ff7f0e"}
    for condition in ["baseline", "ikwe"]:
        subset = df[df["condition"] == condition].sort_values("turn_index")
        if subset.empty:
            continue
        ax.plot(
            subset["turn_index"],
            subset[value_col],
            marker="o",
            linewidth=2.0,
            label=condition,
            color=colors[condition],
        )
    ax.set_xlabel("Turn Index")
    ax.set_ylabel(ylabel)
    ax.set_title(title, pad=8)
    ax.set_ylim(0.0, max(1.05, float(df[value_col].max()) + 0.05))
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right")
    save_fig(fig, outdir, stem)
    plt.close(fig)


def main() -> int:
    args = parse_args()
    load_deps()
    harm_path = Path(args.harm_csv)
    curve_path = Path(args.curve_csv)
    first_harm_path = Path(args.first_harm_csv)
    turns_path = Path(args.turns_csv)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    base_style()

    if not harm_path.exists():
        print(f"missing harm input: {harm_path}")
        print("add harm_rate_condition_comparison.csv and rerun")
        return 1

    harm_df = pd.read_csv(harm_path)
    harm = prepare_harm(harm_df)

    fig1 = grouped_bar(harm)
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
        fig4 = first_harm_survival(first_harm)
        save_fig(fig4, outdir, "Figure4_FirstHarm_SurvivalCurve")
        plt.close(fig4)
    else:
        print(f"skipped Figure 4 (missing input): {first_harm_path}")

    if turns_path.exists():
        turns_df = pd.read_csv(turns_path)
        turns = prepare_turns(turns_df, args)

        harm_turns_adequacy = aggregate_turn_metric(turns.assign(repair_adequacy=turns["is_ra"].astype(float)), "repair_adequacy", harm_only=True)
        two_line_trajectory(
            harm_turns_adequacy,
            value_col="repair_adequacy",
            title="Figure 3A. Repair Adequacy Trajectory by Turn (Conditional on Harm)",
            ylabel="Repair Adequacy Rate (P(R-A) | Harm=YES)",
            stem="Figure3A_RepairAdequacy_Trajectory",
            outdir=outdir,
        )

        harm_turns_repair = aggregate_turn_metric(turns, "repair_score", harm_only=True)
        two_line_trajectory(
            harm_turns_repair,
            value_col="repair_score",
            title="Figure 3B. Mean Repair Score Trajectory by Turn (Conditional on Harm)",
            ylabel="Mean Repair Score (numeric coding)",
            stem="Figure3B_MeanRepairScore_Trajectory",
            outdir=outdir,
        )

        unresolved = turns.assign(unresolved=((turns["harm"]) & (~turns["is_ra"])).astype(float))
        unresolved_turn = aggregate_turn_metric(unresolved, "unresolved", harm_only=False)
        two_line_trajectory(
            unresolved_turn,
            value_col="unresolved",
            title="Figure 5. Unresolved Harm Accumulation by Turn",
            ylabel="Unresolved Harm Rate (Harm=YES & Repair!=R-A)",
            stem="Figure5_UnresolvedHarm_Curve",
            outdir=outdir,
        )
    else:
        print(f"skipped Figures 3A/3B/5 (missing input): {turns_path}")

    print("figure generation complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
