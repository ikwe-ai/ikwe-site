# Study Release Checklist (Ikwe Canonical)

## Structure
- [ ] `README.md` present
- [ ] `Claims_Inventory.md` present
- [ ] `Methodology.md` present
- [ ] `Results_Summary.md` present
- [ ] `Reproducibility_Appendix.md` present
- [ ] `Version_Log.md` present

## Hostile Review Hardening
- [ ] `Threats_To_Validity.md` present
- [ ] `Prompt_Sensitivity.md` present
- [ ] `Scoring_Reliability.md` present
- [ ] `Negative_Controls.md` present
- [ ] Claims-to-code mapping complete (`docs/CLAIMS_TRACEABILITY_STUDY_II.md`)
- [ ] Core claims avoid UNSPECIFIED only when upstream computation artifacts are published

## Reproducibility
- [ ] Scenario index versioned and discoverable
- [ ] Model version pinned/recorded
- [ ] Prompt template hashed
- [ ] Recompute script exists for each quantitative claim

## Publication Integrity Gates
- [ ] `bash scripts/render_pdfs.sh`
- [ ] `node scripts/render_samples.mjs`
- [ ] `bash scripts/generate_study_ii_manifest.sh`
- [ ] `bash scripts/study_ii_claims_check.sh`
- [ ] `bash scripts/live_qa_scan.sh`
- [ ] `./check-consistency.sh`

## Sign-off
- [ ] Prepared by
- [ ] Reviewed by
- [ ] Release approved
