# Ikwe Governance Benchmark - Draft v0.3

Status: Active

Last Updated: 2026-02-13

Reproducibility Status: Partial

## 1. Purpose
The Ikwe Governance Benchmark defines a reproducible framework for measuring trajectory-level risk instability in AI systems under specified evaluation protocols.

This benchmark does not certify safety and does not guarantee harm prevention.

## 2. Core Objects
### 2.1 Scenario Set
- versioned
- inclusion criteria documented
- manifest maintained

### 2.2 Evaluation Protocol
- model version pinned
- prompt template versioned
- decoding parameters documented

### 2.3 Scoring Rubric
- construct definitions documented
- severity scale documented
- adjudication policy documented

## 3. Scope Boundaries
- benchmark outputs are bounded to disclosed scenario families
- cross-version comparisons require full version tuple disclosure
- claims without provenance are marked UNSPECIFIED

## 4. Governance Alignment
- claims traceability: `../../docs/CLAIMS_TRACEABILITY_STUDY_II.md`
- hostile review hardening: `../02_validated/study-ii/`
