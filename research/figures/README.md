# Study II Figures

This directory stores publishable figure exports for Study II benchmark reporting.

## Expected Outputs
- `Figure1_HarmRate_ByCondition.png`
- `Figure1_HarmRate_ByCondition.pdf`
- `Figure1B_Delta_HarmRate.png`
- `Figure1B_Delta_HarmRate.pdf`
- `Figure2_Repair_ByCondition.png`
- `Figure2_Repair_ByCondition.pdf`

## Inputs
Place canonical grouped CSVs at:
- `research/data/study_ii/harm_rate_condition_comparison.csv`
- `research/data/study_ii/repair_mean_by_group.csv`

## Generate
```bash
python research/analysis/generate_study_ii_figures.py
```

Or with explicit paths:
```bash
python research/analysis/generate_study_ii_figures.py \
  --harm-csv /path/to/harm_rate_condition_comparison.csv \
  --repair-csv /path/to/repair_mean_by_group.csv \
  --outdir research/figures
```

## Caption Copy
Figure 1: Harm rate by condition across Study II scenarios. Bars show the proportion of turns flagged as harm within each scenario under baseline vs Ikwe condition.

Figure 1B: Change in harm rate under Ikwe condition (Delta = Ikwe - Baseline). Positive values indicate higher flagged harm rate under Ikwe; negative values indicate reduction.

Figure 2: Mean repair score by condition across Study II scenarios. Bars show group means from `Repair_Level` coding and should be interpreted with rubric mapping and N/A handling disclosures.

## Guardrails
- Harm rate definition: proportion of turns with `Harm_Indicator = YES`.
- Scenario abstraction and inclusion criteria: `research/scenarios/scenario_manifest_v0.3.json`.
- Rubric and repair coding interpretation constraints: `research/rubric/rubric_v0.2.md`.
