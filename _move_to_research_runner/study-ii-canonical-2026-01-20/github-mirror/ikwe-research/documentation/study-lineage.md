# Study Lineage: EQ Safety Benchmark → Study II

**Version:** 1.0 (CANONICAL)  
**Status:** 🔒 LOCKED  
**Lock Date:** 2026-01-20

---

## Purpose

This document traces the evolution of Ikwe.ai's emotional safety research from the original EQ Safety Benchmark through to Study II: Mechanism-Based Analysis. It establishes the intellectual lineage and methodological progression that informs the current research.

---

## Research Timeline

```
2024-2025                           2026
    │                                 │
    ▼                                 ▼
┌─────────────────┐             ┌─────────────────┐
│  EQ Safety      │             │    Study II     │
│  Benchmark      │─────────────│  Mechanism      │
│  (Study I)      │             │  Analysis       │
└─────────────────┘             └─────────────────┘
    │                                 │
    │  Key Finding:                   │  Research Question:
    │  54.7% unsafe                   │  WHY do failures
    │  response rate                  │  happen?
    │                                 │
    │  Core Thesis:                   │  Core Contribution:
    │  Recognition ≠                  │  Catastrophic
    │  Safety                         │  Failure taxonomy
    │                                 │
    ▼                                 ▼
  WHAT fails                      HOW it fails
```

---

## Study I: EQ Safety Benchmark

### Overview

The EQ Safety Benchmark established the foundational methodology for evaluating behavioral emotional safety in AI responses to vulnerable users.

### Key Findings

| Metric | Finding |
|--------|---------|
| Unsafe response rate | 54.7% of baseline AI responses exhibited SSF |
| Repair behavior | 43% showed no repair after causing harm |
| Recognition-safety gap | Models with high emotion recognition ≠ safe responses |

### Core Thesis

> "Recognition ≠ Safety" — AI systems can recognize emotions accurately while still responding unsafely.

### Methodological Contributions

1. **Safety-Sabotaging Features (SSF)** — Taxonomy of harmful response characteristics
2. **Vulnerable user scenarios** — Standardized emotional distress prompts
3. **Repair behavior assessment** — Framework for evaluating corrective action

### Limitations Identified

- **Prevalence focus**: Study I established *how often* failures occur
- **Mechanism gap**: Did not explain *why* or *how* failures develop
- **Binary limitation**: SSF present/absent without pathway analysis

---

## Transition: Study I → Study II

### Motivating Questions

Following Study I, several questions emerged:

1. **Pathway question**: Do failures cluster into identifiable patterns?
2. **Mechanism question**: What triggers different failure types?
3. **Threshold question**: What distinguishes catastrophic from recoverable failures?
4. **Prediction question**: Can we predict failure pathways from scenario characteristics?

### Methodological Evolution

| Aspect | Study I | Study II |
|--------|---------|----------|
| **Primary outcome** | SSF presence (binary) | CF composite (binary) |
| **Analysis level** | Response-level | Mechanism-level |
| **Pathway analysis** | Not included | Primary focus |
| **Repair integration** | Separate measure | Integrated into CF |
| **Prediction modeling** | Descriptive | Predictive |

---

## Study II: Mechanism-Based Analysis

### Research Focus

Study II shifts from "what fails" to "how it fails" by introducing:

1. **Catastrophic Failure (CF)** — Composite measure requiring BOTH SSF AND repair failure
2. **Failure Pathways** — Taxonomy of CF mechanisms (A, B, C)
3. **Triggering Conditions** — Scenario characteristics that predict pathways
4. **Threshold Analysis** — Distinguishing CF from recoverable failures

### Theoretical Framework

```
                    AI Response
                        │
            ┌───────────┴───────────┐
            │                       │
        SSF Absent              SSF Present
        (No failure)                │
                        ┌───────────┴───────────┐
                        │                       │
                    Adequate                Poor/Absent
                    Repair                    Repair
                    (Recoverable)           (CATASTROPHIC
                                             FAILURE)
                                                │
                                    ┌───────────┼───────────┐
                                    │           │           │
                                Pathway A   Pathway B   Pathway C
                                (Premature  (Harmful    (Authority
                                 Closure)   Reframing)  Displacement)
```

### Key Hypotheses

**H1**: CF responses cluster into three primary pathways with distinct behavioral signatures.

**H2**: Models with higher emotional articulation will not demonstrate proportionally lower CF rates (decoupling hypothesis, extending Study I finding).

**H3**: Triggering conditions will predict pathway activation with >70% accuracy.

---

## Conceptual Inheritance

### From Study I to Study II

| Concept | Study I Origin | Study II Extension |
|---------|---------------|-------------------|
| SSF taxonomy | Original 7-category system | Maintained, integrated into CF |
| Repair behavior | Standalone measure | Integrated as CF component |
| Scenario corpus | Initial development | Expanded, abstracted |
| Vulnerable user focus | Core framing | Maintained |
| Recognition ≠ Safety | Core thesis | Extended to mechanism level |

### New in Study II

| Concept | Description |
|---------|-------------|
| Catastrophic Failure | Binary composite: SSF + Repair failure |
| Failure Pathways | A (Closure), B (Reframing), C (Displacement) |
| Branching Points | Moments where repair could have occurred |
| Threshold Criteria | What distinguishes CF from recoverable failure |

---

## Methodological Decisions

### Why Binary CF?

The binary CF measure was chosen over continuous severity because:

1. **Clarity**: Clear threshold for "catastrophic" vs. "not catastrophic"
2. **Actionability**: Binary classification enables clear policy recommendations
3. **Reliability**: Easier to achieve inter-rater agreement on binary decisions
4. **Prevalence**: Enables direct comparison of CF rates across models

### Why Three Pathways?

The three-pathway taxonomy emerged from:

1. **Empirical clustering**: Study I responses naturally grouped into these patterns
2. **Clinical literature**: Aligns with known harmful response patterns in human counseling
3. **Distinct mechanisms**: Each pathway has unique triggering conditions and behavioral signatures
4. **Parsimony**: Three categories balance specificity with usability

### Why Composite Measure?

CF requires BOTH SSF AND repair failure because:

1. **Distinguishes recoverable failures**: SSF alone may be corrected with adequate repair
2. **Captures full harm trajectory**: Single-point assessment misses repair opportunity
3. **Aligns with clinical practice**: Therapists also evaluate response + repair
4. **Avoids over-counting**: Many minor missteps are corrected naturally

---

## Future Directions

### Study III (Proposed)

Potential extensions following Study II:

1. **Intervention testing**: Can pathway-specific prompting reduce CF rates?
2. **Real-world validation**: Do CF responses predict actual user harm?
3. **Cross-cultural analysis**: Do pathways vary across cultural contexts?
4. **Longitudinal tracking**: How do CF rates change across model versions?

### Infrastructure Development

- **Automated CF detection**: ML model for real-time CF flagging
- **Pathway prediction API**: Tools for developers to assess risk
- **Benchmark integration**: CF metrics in standard AI evaluation suites

---

## Citation

When referencing this research lineage:

> Ikwe.ai. (2026). Study II: Mechanism-Based Analysis of Catastrophic Failure in AI Emotional Safety Responses. Building on EQ Safety Benchmark findings. Ikwe.ai Research Repository.

---

> 🔒 **CANONICAL — DO NOT EDIT**  
> Locked on 2026-01-20. Changes require new version and changelog entry.  
> See documentation/changelog.md for version control policy.
