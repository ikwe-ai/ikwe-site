# Methodology

## 1. Evaluation Design
- scenario-based sequential interactions
- benchmarked on version-pinned model runs
- scored using a fixed rubric version

## 2. Inputs
- scenario manifest: `research/scenarios/scenario_manifest_v0.3.json`
- prompt set: `research/prompts/prompt_set_v0.3.md`
- rubric: `research/rubric/rubric_v0.2.md`

## 3. Outputs
- claim-facing aggregates
- benchmark summary metrics
- reproducibility and traceability logs

## 4. Statistical Reporting
- report point estimates with uncertainty intervals
- disclose sample size and scenario count
- include sensitivity notes for threshold changes

## 5. Integrity Controls
- cross-surface claims check: `../../scripts/study_ii_claims_check.sh`
- release manifest: `../study-ii/ARTIFACT_MANIFEST.sha256`
