# Reproducibility

## Current Status
| Artifact | Public | Versioned | Status |
|---|---|---|---|
| Scenario Manifest | Yes | Yes | Draft Published |
| Prompt Archive | Yes | Yes | Draft Published |
| Rubric | Yes | Yes | Draft Published |
| Recompute Script | Yes | Yes | Template Published |
| Claims Integrity Gate | Yes | Yes | Active |
| Artifact Manifest | Yes | Yes | Active |

## Reproduction Instructions
1. Regenerate PDFs: `bash scripts/render_pdfs.sh`
2. Regenerate PNGs: `node scripts/render_samples.mjs`
3. Rebuild manifest: `bash scripts/generate_study_ii_manifest.sh`
4. Run claims checks: `bash scripts/study_ii_claims_check.sh`
5. Run QA checks: `bash scripts/live_qa_scan.sh && ./check-consistency.sh`

## Integrity Caveat
This reproduces publication artifacts and claim-surface consistency. It does not yet reproduce full raw statistical computation in-repo.
