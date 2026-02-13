#!/usr/bin/env python3
"""Study II consistency gate for benchmark docs, metrics, and artifacts."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from reproduce_headline_metrics import delta_ci_newcombe_wilson, load_scored_turns, wilson_interval


@dataclass
class CheckState:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def err(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_files(paths: list[Path], state: CheckState) -> None:
    for path in paths:
        if not path.exists():
            state.err(f"missing file: {path}")


def assert_close(a: float, b: float, label: str, state: CheckState, tol: float = 1e-9) -> None:
    if math.isnan(a) and math.isnan(b):
        return
    if abs(a - b) > tol:
        state.err(f"{label} mismatch: expected {b}, got {a}")


def frame_compare(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    keys: list[str],
    numeric_cols: list[str],
    label: str,
    state: CheckState,
    tol: float = 1e-9,
) -> None:
    a = actual.copy()
    e = expected.copy()
    a = a.sort_values(keys).reset_index(drop=True)
    e = e.sort_values(keys).reset_index(drop=True)

    if a.shape[0] != e.shape[0]:
        state.err(f"{label}: row count mismatch ({a.shape[0]} vs {e.shape[0]})")
        return

    merged = a.merge(e, on=keys, how="outer", indicator=True)
    if not (merged["_merge"] == "both").all():
        missing = merged[merged["_merge"] != "both"][keys + ["_merge"]]
        state.err(f"{label}: key mismatch rows found: {missing.to_dict('records')[:5]}")
        return

    for col in numeric_cols:
        if col not in a.columns or col not in e.columns:
            state.err(f"{label}: missing numeric column {col}")
            continue
        diff = (pd.to_numeric(a[col], errors="coerce") - pd.to_numeric(e[col], errors="coerce")).abs().fillna(0.0)
        if (diff > tol).any():
            idx = int(diff.idxmax())
            key_str = ", ".join(f"{k}={a.loc[idx, k]}" for k in keys)
            state.err(
                f"{label}: column {col} mismatch at {key_str} "
                f"(actual={a.loc[idx, col]}, expected={e.loc[idx, col]})"
            )


def parse_integrity(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if not row:
                continue
            key = row[0].strip()
            value = ",".join(row[1:]).strip()
            out[key] = value
    return out


def parse_results_hashes(results_md: Path) -> list[tuple[str, str]]:
    hashes: list[tuple[str, str]] = []
    pattern = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([a-f0-9]{64})`\s*\|$")
    for line in results_md.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line.strip())
        if match:
            hashes.append((match.group(1), match.group(2)))
    return hashes


def check_results_surface(metrics: dict, results_text: str, state: CheckState) -> None:
    expected_strings = [
        "| baseline    |  21 |  30 |       0.7   | [0.521, 0.833]    |",
        "| ikwe        |  21 |  24 |       0.875 | [0.690, 0.957]    |",
        "| OVERALL       | ikwe - baseline |   0.175 | [-0.143, 0.435]            |",
        "baseline `0.700`, ikwe `0.875`",
        "baseline `0.633`, ikwe `0.833`",
    ]

    for token in expected_strings:
        if token not in results_text:
            state.err(f"RESULTS.md missing expected token: {token}")

    baseline = next((x for x in metrics["by_condition"] if x["condition"] == "baseline"), None)
    ikwe = next((x for x in metrics["by_condition"] if x["condition"] == "ikwe"), None)
    if baseline is None or ikwe is None:
        state.err("headline_metrics_v0.3.json missing baseline or ikwe row")
        return

    if baseline["harm_x"] != 21 or baseline["harm_n"] != 30:
        state.err("headline metrics baseline k/n not equal to expected 21/30")
    if ikwe["harm_x"] != 21 or ikwe["harm_n"] != 24:
        state.err("headline metrics ikwe k/n not equal to expected 21/24")


def check_traceability_functions(traceability_md: Path, figures_py: Path, state: CheckState) -> None:
    trace_text = traceability_md.read_text(encoding="utf-8")
    figure_text = figures_py.read_text(encoding="utf-8")
    funcs = re.findall(r"generate_study_ii_figures\.py:([A-Za-z_][A-Za-z0-9_]*)", trace_text)
    for fn in sorted(set(funcs)):
        if f"def {fn}(" not in figure_text:
            state.err(f"TRACEABILITY references missing function: {fn}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run consistency checks for Study II benchmark artifacts")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root (defaults to ikwe-site root)",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    benchmark_dir = root / "research" / "benchmark"
    analysis_dir = root / "research" / "analysis"
    data_dir = root / "research" / "data" / "study_ii"
    figures_dir = root / "research" / "figures"

    state = CheckState()

    required = [
        benchmark_dir / "RESULTS.md",
        benchmark_dir / "TRACEABILITY.md",
        benchmark_dir / "TRAJECTORY_PACKAGE.md",
        benchmark_dir / "headline_metrics_v0.3.json",
        analysis_dir / "reproduce_headline_metrics.py",
        analysis_dir / "generate_study_ii_figures.py",
        data_dir / "study_ii_turns_scored.csv",
        data_dir / "harm_rate_by_group.csv",
        data_dir / "harm_curve_by_turn.csv",
        data_dir / "first_harm_turn_by_run.csv",
        data_dir / "ssf_rates_by_group.csv",
        data_dir / "repair_mean_by_group.csv",
        data_dir / "harm_rate_condition_comparison.csv",
        data_dir / "integrity_summary.csv",
    ]
    require_files(required, state)
    if state.errors:
        for err in state.errors:
            print(f"ERR: {err}")
        return 1

    scored = load_scored_turns(data_dir / "study_ii_turns_scored.csv")

    expected_harm_rate = (
        scored.groupby(["Scenario_ID", "Model_ID", "Condition"], as_index=False)["Harm_Indicator"]
        .mean()
        .rename(columns={"Harm_Indicator": "Harm_Rate"})
    )
    actual_harm_rate = pd.read_csv(data_dir / "harm_rate_by_group.csv")
    frame_compare(
        actual_harm_rate,
        expected_harm_rate,
        keys=["Scenario_ID", "Model_ID", "Condition"],
        numeric_cols=["Harm_Rate"],
        label="harm_rate_by_group.csv",
        state=state,
    )

    expected_harm_curve = (
        scored.groupby(["Scenario_ID", "Condition", "Turn_Index"], as_index=False)["Harm_Indicator"]
        .mean()
        .rename(columns={"Harm_Indicator": "Harm_Rate"})
    )
    actual_harm_curve = pd.read_csv(data_dir / "harm_curve_by_turn.csv")
    frame_compare(
        actual_harm_curve,
        expected_harm_curve,
        keys=["Scenario_ID", "Condition", "Turn_Index"],
        numeric_cols=["Harm_Rate"],
        label="harm_curve_by_turn.csv",
        state=state,
    )

    expected_first_harm = (
        scored[scored["Harm_Indicator"] == 1]
        .groupby(["Run_ID", "Scenario_ID", "Model_ID", "Condition"], as_index=False)["Turn_Index"]
        .min()
        .rename(columns={"Turn_Index": "First_Harm_Turn"})
    )
    actual_first_harm = pd.read_csv(data_dir / "first_harm_turn_by_run.csv")
    frame_compare(
        actual_first_harm,
        expected_first_harm,
        keys=["Run_ID", "Scenario_ID", "Model_ID", "Condition"],
        numeric_cols=["First_Harm_Turn"],
        label="first_harm_turn_by_run.csv",
        state=state,
    )

    ssf_cols = [f"SSF{i}" for i in range(1, 8)]
    expected_ssf = scored.groupby(["Scenario_ID", "Model_ID", "Condition"], as_index=False)[ssf_cols].mean()
    actual_ssf = pd.read_csv(data_dir / "ssf_rates_by_group.csv")
    frame_compare(
        actual_ssf,
        expected_ssf,
        keys=["Scenario_ID", "Model_ID", "Condition"],
        numeric_cols=ssf_cols,
        label="ssf_rates_by_group.csv",
        state=state,
    )

    expected_repair = (
        scored.groupby(["Scenario_ID", "Model_ID", "Condition"], as_index=False)["Repair_Level"]
        .mean()
        .rename(columns={"Repair_Level": "Mean_Repair"})
    )
    actual_repair = pd.read_csv(data_dir / "repair_mean_by_group.csv")
    frame_compare(
        actual_repair,
        expected_repair,
        keys=["Scenario_ID", "Model_ID", "Condition"],
        numeric_cols=["Mean_Repair"],
        label="repair_mean_by_group.csv",
        state=state,
    )

    expected_cmp = expected_harm_rate.pivot_table(
        index=["Scenario_ID", "Model_ID"], columns="Condition", values="Harm_Rate", aggfunc="mean"
    ).reset_index()
    expected_cmp["Delta_IKWE_minus_Baseline"] = expected_cmp["ikwe"] - expected_cmp["baseline"]
    actual_cmp = pd.read_csv(data_dir / "harm_rate_condition_comparison.csv")
    frame_compare(
        actual_cmp,
        expected_cmp[["Scenario_ID", "Model_ID", "baseline", "ikwe", "Delta_IKWE_minus_Baseline"]],
        keys=["Scenario_ID", "Model_ID"],
        numeric_cols=["baseline", "ikwe", "Delta_IKWE_minus_Baseline"],
        label="harm_rate_condition_comparison.csv",
        state=state,
    )

    integrity = parse_integrity(data_dir / "integrity_summary.csv")
    if integrity.get("rows") != str(len(scored)):
        state.err(f"integrity_summary.csv rows mismatch: {integrity.get('rows')} vs {len(scored)}")
    if integrity.get("runs") != str(scored["Run_ID"].nunique()):
        state.err("integrity_summary.csv runs mismatch")
    if integrity.get("turns_per_run_min") != str(int(scored.groupby("Run_ID")["Turn_Index"].count().min())):
        state.err("integrity_summary.csv turns_per_run_min mismatch")
    if integrity.get("turns_per_run_max") != str(int(scored.groupby("Run_ID")["Turn_Index"].count().max())):
        state.err("integrity_summary.csv turns_per_run_max mismatch")

    for key, values in [
        ("scenarios", sorted(scored["Scenario_ID"].dropna().unique().tolist())),
        ("models", sorted(scored["Model_ID"].dropna().unique().tolist())),
        ("conditions", sorted(scored["Condition"].dropna().unique().tolist())),
    ]:
        raw = integrity.get(key)
        if raw is None:
            state.err(f"integrity_summary.csv missing key: {key}")
            continue
        try:
            parsed = sorted(ast.literal_eval(raw))
        except Exception:
            state.err(f"integrity_summary.csv invalid list for {key}: {raw}")
            continue
        if parsed != values:
            state.err(f"integrity_summary.csv {key} mismatch: {parsed} vs {values}")

    metrics_path = benchmark_dir / "headline_metrics_v0.3.json"
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))

    harm = scored["Harm_Indicator"].dropna()
    x = int((harm == 1).sum())
    n = int(harm.shape[0])
    p = x / n
    lo, hi = wilson_interval(x, n)
    json_h = metrics["headline"]["harm_indicator"]
    if json_h["x"] != x or json_h["n"] != n:
        state.err("headline_metrics_v0.3.json harm x/n mismatch")
    assert_close(float(json_h["rate"]), p, "headline harm rate", state)
    assert_close(float(json_h["wilson_95"][0]), lo, "headline wilson low", state)
    assert_close(float(json_h["wilson_95"][1]), hi, "headline wilson high", state)

    condition_rows = {
        c: {
            "x": int((g["Harm_Indicator"] == 1).sum()),
            "n": int(g["Harm_Indicator"].shape[0]),
            "mean_repair": float(g["Repair_Level"].mean()),
        }
        for c, g in scored.groupby("Condition")
    }
    for row in metrics["by_condition"]:
        condition = row["condition"]
        if condition not in condition_rows:
            state.err(f"headline metrics unexpected condition: {condition}")
            continue
        ex = condition_rows[condition]
        if row["harm_x"] != ex["x"] or row["harm_n"] != ex["n"]:
            state.err(f"headline metrics condition k/n mismatch for {condition}")
        assert_close(float(row["repair_level_mean"]), ex["mean_repair"], f"{condition} repair mean", state)
        c_lo, c_hi = wilson_interval(ex["x"], ex["n"])
        assert_close(float(row["harm_rate_wilson_95"][0]), c_lo, f"{condition} ci low", state)
        assert_close(float(row["harm_rate_wilson_95"][1]), c_hi, f"{condition} ci high", state)

    if "ikwe" in condition_rows and "baseline" in condition_rows:
        d, d_lo, d_hi = delta_ci_newcombe_wilson(
            condition_rows["ikwe"]["x"],
            condition_rows["ikwe"]["n"],
            condition_rows["baseline"]["x"],
            condition_rows["baseline"]["n"],
        )
        delta_json = metrics["condition_delta_ikwe_minus_baseline"]
        assert_close(float(delta_json["delta"]), d, "condition delta", state)
        assert_close(float(delta_json["delta_newcombe_wilson_95"][0]), d_lo, "condition delta low", state)
        assert_close(float(delta_json["delta_newcombe_wilson_95"][1]), d_hi, "condition delta high", state)

    results_md = benchmark_dir / "RESULTS.md"
    results_text = results_md.read_text(encoding="utf-8")
    check_results_surface(metrics, results_text, state)

    for rel_path, recorded_hash in parse_results_hashes(results_md):
        data_file = (benchmark_dir / rel_path).resolve()
        if not data_file.exists():
            state.err(f"RESULTS hash entry points to missing file: {rel_path}")
            continue
        current_hash = sha256_file(data_file)
        if current_hash != recorded_hash:
            state.err(f"RESULTS hash mismatch for {rel_path}: {recorded_hash} != {current_hash}")

    check_traceability_functions(
        benchmark_dir / "TRACEABILITY.md",
        analysis_dir / "generate_study_ii_figures.py",
        state,
    )

    required_figures = [
        "Figure1_HarmRate_ByCondition.png",
        "Figure1_HarmRate_ByCondition.pdf",
        "Figure1B_Delta_HarmRate.png",
        "Figure1B_Delta_HarmRate.pdf",
        "Figure2_HarmTrajectory_ByTurn.png",
        "Figure2_HarmTrajectory_ByTurn.pdf",
        "Figure3A_RepairAdequacy_Trajectory.png",
        "Figure3A_RepairAdequacy_Trajectory.pdf",
        "Figure3B_MeanRepairScore_Trajectory.png",
        "Figure3B_MeanRepairScore_Trajectory.pdf",
        "Figure4_FirstHarm_SurvivalCurve.png",
        "Figure4_FirstHarm_SurvivalCurve.pdf",
        "Figure5_UnresolvedHarm_Curve.png",
        "Figure5_UnresolvedHarm_Curve.pdf",
    ]
    for figure_name in required_figures:
        path = figures_dir / figure_name
        if not path.exists():
            state.err(f"missing figure: {path}")

    if state.errors:
        print("FAIL: consistency check detected issues")
        for err in state.errors:
            print(f"- {err}")
        if state.warnings:
            print("WARNINGS:")
            for warning in state.warnings:
                print(f"- {warning}")
        return 1

    print("PASS: Study II consistency checks passed")
    if state.warnings:
        print("WARNINGS:")
        for warning in state.warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
