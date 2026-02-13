# Threats to Validity (Benchmark Layer)

Status: Active benchmark-level validity register for Study II trajectory releases.

## Construct Validity
- Risk: Harm flags may capture sensitivity to rubric markers rather than direct evidence of harm creation.
- Mitigation: Interpret harm trajectories jointly with repair adequacy and unresolved-harm curves.
- Control Artifact: `RESULTS.md` trajectory interpretation guardrails.

## Internal Validity
- Risk: Prompt wording and turn framing can shift measured rates.
- Mitigation: Run prompt sensitivity variants (`P0` to `P3`) under fixed model/version settings.
- Control Artifact: `PROMPT_SENSITIVITY.md`.

## Reliability
- Risk: Scoring may vary by coder and adjudication behavior.
- Mitigation: Dual-coding subset with agreement metrics and adjudication logs.
- Control Artifact: `SCORING_RELIABILITY.md`.

## External Validity
- Risk: Pilot slices with limited scenario families do not generalize to all contexts.
- Mitigation: Mark pilot outputs as descriptive and scale scenario coverage in later releases.
- Control Artifact: `RESULTS.md` limitations and scope language.

## Temporal Validity
- Risk: Model updates and infrastructure drift can change measured trajectories.
- Mitigation: Pin model/version metadata and rerun on version changes.
- Control Artifact: `METHODOLOGY.md` version disclosure requirements.

## Security and Access Validity
- Risk: Artifacts may be inaccessible, altered, or replaced without provenance checks.
- Mitigation: Preserve hash-based audit tables, maintain read-only release artifacts where required, and keep reproducibility scripts in-repo.
- Control Artifact: `RESULTS.md` Inputs and Hashes section plus `REPRODUCIBILITY.md`.
