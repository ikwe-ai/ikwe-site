# Ikwe Governance Benchmark Versioning Policy

## 1. Versioning Structure
The benchmark follows semantic versioning:

`MAJOR.MINOR.PATCH`

### MAJOR (`vX.0.0`)
Increment when core construct definitions, scoring methodology, aggregation logic, or scenario inclusion criteria materially change.

Major versions are not backward-comparable without explicit migration documentation.

### MINOR (`v0.X.0`)
Increment when thresholds are recalibrated, metrics are added, or reporting/robustness is expanded without changing core construct definitions.

Minor versions maintain conceptual compatibility with the same major version.

### PATCH (`v0.0.X`)
Increment for bug fixes, documentation corrections, and non-structural reproducibility improvements.

Patch changes do not substantively alter benchmark outputs.

## 2. Version Disclosure Requirements
Each benchmark result release must disclose:
- benchmark version
- scenario set version
- prompt template version
- rubric version
- model version
- environment version

Missing disclosure invalidates cross-version comparability claims.

## 3. Deprecation Policy
When a construct or metric is deprecated:
- retain documentation in version history
- publish migration guidance
- keep archived versions accessible

## 4. Stability Commitment
Major benchmark versions are frozen for at least 90 days after release to support independent replication, public review, and stability validation.
