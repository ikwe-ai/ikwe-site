# Threats to Validity — Study II

Study: Study II — Trajectory Safety & Drift Correction

Owner: Visible Healing Inc. (dba Ikwe.ai)

Version: v1.0

Last Updated: 2026-02-13

## Construct Validity
- Risk: Drift markers may conflate tone quality with authority signaling.
- Mitigation: Maintain explicit marker definitions, positive/negative examples, and edge-case counterexamples in rubric notes.
- Current Gap: Full rubric artifact not in this publication repo.

## Internal Validity
- Risk: Prompt framing and order effects may influence behavior.
- Mitigation: Use prompt sensitivity suite (P0–P3), randomized ordering where feasible, and explicit prompt template tracking.
- Current Gap: Prompt hash registry is not yet published in this repo.

## External Validity
- Risk: Scenario families may not generalize to all deployment contexts.
- Mitigation: Publish scenario taxonomy coverage, inclusion rationale, and out-of-scope notes.
- Current Gap: Scenario index source currently unspecified in this repo.

## Reliability
- Risk: Scoring may be subjective without coder agreement controls.
- Mitigation: Dual-code at least 20% of turns, report agreement, and log adjudication decisions.
- Current Gap: Inter-rater report is not yet published in this repo.

## Temporal Validity
- Risk: Model updates alter observed behavior over time.
- Mitigation: Pin model versions per run, timestamp runs, and define rerun cadence.
- Current Gap: Model version/run ledger not yet published in this repo.

## Publication Integrity Controls Present in This Repo
- Canonical cross-surface claim checks: `scripts/study_ii_claims_check.sh`
- Legal/citation baseline checks: `check-consistency.sh`
- Pricing/link drift checks: `scripts/live_qa_scan.sh`
- Deterministic sample artifact generation paths: `scripts/render_pdfs.sh`, `scripts/render_samples.mjs`
