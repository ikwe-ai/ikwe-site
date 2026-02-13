# Study II - Traceability (Claims -> Figures -> Data -> Code)

| Claim ID | Claim | Evidence (Figure) | Data Source | Script / Function | Status |
|---|---|---|---|---|---|
| C-02 | Trajectory correction is inconsistently applied once harm is present. | Fig 3A, Fig 3B | `../data/study_ii/study_ii_turns_scored.csv` | `../analysis/generate_study_ii_figures.py:repair_trajectory` | Verified |
| C-04 | First harm occurs early in interaction trajectories. | Fig 4 | `../data/study_ii/first_harm_turn_by_run.csv` | `../analysis/generate_study_ii_figures.py:km_survival` | Verified |
| C-05 | Unresolved harm accumulates over turns. | Fig 5 | `../data/study_ii/study_ii_turns_scored.csv` | `../analysis/generate_study_ii_figures.py:unresolved_curve` | Verified |
| C-06 | Harm trajectory differs by condition over turns. | Fig 2 | `../data/study_ii/harm_curve_by_turn.csv` | `../analysis/generate_study_ii_figures.py:harm_curve` | Verified |

## Notes
- This table covers the trajectory figure package only. Broader claim traceability remains in `../../docs/CLAIMS_TRACEABILITY_STUDY_II.md`.
- If upstream files are replaced, regenerate figures and update status markers before release.
