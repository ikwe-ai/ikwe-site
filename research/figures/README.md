# Study II Figures

This directory stores publishable figure exports for Study II benchmark reporting.

## Expected Outputs
- `Figure1_HarmRate_ByCondition.png`
- `Figure1_HarmRate_ByCondition.pdf`
- `Figure1B_Delta_HarmRate.png`
- `Figure1B_Delta_HarmRate.pdf`
- `Figure2_HarmTrajectory_ByTurn.png`
- `Figure2_HarmTrajectory_ByTurn.pdf`
- `Figure3A_RepairAdequacy_Trajectory.png`
- `Figure3A_RepairAdequacy_Trajectory.pdf`
- `Figure3B_MeanRepairScore_Trajectory.png`
- `Figure3B_MeanRepairScore_Trajectory.pdf`
- `Figure4_FirstHarm_SurvivalCurve.png`
- `Figure4_FirstHarm_SurvivalCurve.pdf`
- `Figure5_UnresolvedHarm_Curve.png`
- `Figure5_UnresolvedHarm_Curve.pdf`

## Inputs
Place canonical grouped CSVs at:
- `research/data/study_ii/harm_rate_condition_comparison.csv`
- `research/data/study_ii/harm_curve_by_turn.csv` (for Figure 2)
- `research/data/study_ii/first_harm_turn_by_run.csv` (for Figure 4)
- `research/data/study_ii/study_ii_turns_scored.csv` (for Figures 3A, 3B, 5)

## Generate
```bash
python3 research/analysis/generate_study_ii_figures.py
```

Or with explicit paths:
```bash
python3 research/analysis/generate_study_ii_figures.py \
  --harm-csv /path/to/harm_rate_condition_comparison.csv \
  --curve-csv /path/to/harm_curve_by_turn.csv \
  --first-harm-csv /path/to/first_harm_turn_by_run.csv \
  --turns-csv /path/to/study_ii_turns_scored.csv \
  --outdir research/figures
```

## Caption Copy
Figure 1: Harm rate by condition across Study II scenarios. Bars show the proportion of turns flagged as harm within each scenario under baseline vs Ikwe condition.

Figure 1B: Change in harm rate under Ikwe condition (Delta = Ikwe - Baseline). Positive values indicate higher flagged harm rate under Ikwe; negative values indicate reduction.

Figure 2: Harm trajectory across turns by condition. Higher values reflect higher detection frequency (`Harm_Indicator = YES`) and do not independently imply harm creation.

Figure 3A: Repair adequacy trajectory by turn conditional on harm, reported as `P(R-A | Harm=YES)`.

Figure 3B: Mean repair score trajectory by turn conditional on harm, using numeric repair coding.

Figure 4: First-harm survival curve (`P(no harm detected yet)`), Kaplan-Meier style over turns.

Figure 5: Unresolved harm curve by turn, reported as `P(Harm=YES and Repair!=R-A)`.

## Guardrails
- Harm rate definition: proportion of turns with `Harm_Indicator = YES`.
- Scenario abstraction and inclusion criteria: `research/scenarios/scenario_manifest_v0.3.json`.
- Rubric and repair coding interpretation constraints: `research/rubric/rubric_v0.2.md`.
- Current trajectory figures use this operational repair mapping for numeric exports: `2 -> R-A`, `1 -> R-I`, `0 -> R-0` on harm turns and `N/A` fallback on non-harm turns.
