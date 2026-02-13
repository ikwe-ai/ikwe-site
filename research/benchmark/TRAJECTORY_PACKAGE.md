# Study II - Trajectory Package (Figures 2-5)

This package operationalizes interaction trajectory safety as a time-series problem.

## Figures
- Fig 2: Harm trajectory by turn (mean harm rate vs turn index)
- Fig 3A: Repair adequacy trajectory (`P(R-A | Harm=YES)`) by turn
- Fig 3B: Mean repair score trajectory (numeric coding) by turn
- Fig 4: First-harm survival curve (Kaplan-Meier style)
- Fig 5: Unresolved harm curve (`Harm=YES and Repair!=R-A`) by turn

## Key Interpretation Rule
Harm rate measures rubric flag frequency, not harm creation.

Trajectory safety is evaluated by detection timing (Fig 4) and control response (Fig 3A and Fig 3B), with unresolved harm accumulation (Fig 5) treated as the primary safety risk proxy in this slice.

## Coding Disclosure
Repair coding is numeric in the export and mapped as documented in `METHODOLOGY.md`:
- `2 -> R-A` (adequate)
- `1 -> R-I` (insufficient)
- `0 -> R-0` on harm turns with non-harm `N/A` fallback policy disclosed

## Reproduction
Run:

`python3 ../analysis/generate_study_ii_figures.py`

Outputs:

`../figures/Figure*.png` and `../figures/Figure*.pdf`
