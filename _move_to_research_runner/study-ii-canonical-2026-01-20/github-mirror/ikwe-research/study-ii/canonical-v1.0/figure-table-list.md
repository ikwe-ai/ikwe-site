# Figure & Table List: Study II

**Version:** 1.0 (CANONICAL)  
**Status:** 🔒 LOCKED  
**Lock Date:** 2026-01-20  
**Edit Policy:** No edits permitted during data collection

---

## Purpose

This document specifies all planned figures and tables for Study II results reporting. Placeholders indicate where visualizations will be generated following data collection and analysis.

---

## Figures

### Figure 1: CF Prevalence by Model

**Type:** Bar chart with error bars  
**X-axis:** Model (categorical)  
**Y-axis:** CF Rate (%)  
**Error bars:** 95% CI  
**Notes:** Models sorted by CF rate descending; include n for each model

**Placeholder:**
```
┌────────────────────────────────────────┐
│                                        │
│    █████                               │
│    █████  ████                         │
│    █████  ████  ███                    │
│    █████  ████  ███   ██               │
│    █████  ████  ███   ██   █           │
│  ──────────────────────────────        │
│   Model A  B    C    D   E             │
│                                        │
│         CF Prevalence by Model         │
└────────────────────────────────────────┘
```

---

### Figure 2: CF Prevalence by Scenario Type

**Type:** Grouped bar chart  
**X-axis:** Scenario Type (Acute, Chronic, Transitional)  
**Y-axis:** CF Rate (%)  
**Grouping:** Optional model comparison  
**Error bars:** 95% CI

**Placeholder:**
```
┌────────────────────────────────────────┐
│                                        │
│     ████                               │
│     ████   ████                        │
│     ████   ████   ████                 │
│     ████   ████   ████                 │
│  ────────────────────────              │
│    Acute  Chronic Trans                │
│                                        │
│       CF by Scenario Type              │
└────────────────────────────────────────┘
```

---

### Figure 3: Pathway Distribution

**Type:** Pie chart or stacked bar  
**Segments:** Pathway A, B, C, Other  
**Labels:** Count and percentage  
**Notes:** Only CF=1 responses included

**Placeholder:**
```
┌────────────────────────────────────────┐
│                                        │
│           ╭───────────╮                │
│         ╱   A: XX%     ╲               │
│        │    Premature   │              │
│        │    Closure     │              │
│         ╲   ──────────╱                │
│          ╲ B: XX%    ╱                 │
│           ╲ Harmful ╱                  │
│            ╲Refram ╱                   │
│             ╲────╱  C: XX%             │
│              ────   Authority          │
│                                        │
│         Pathway Distribution           │
└────────────────────────────────────────┘
```

---

### Figure 4: Pathway Behavioral Signatures

**Type:** Heatmap or radar chart  
**Rows/Spokes:** SSF types (1-7)  
**Columns/Axes:** Pathways (A, B, C)  
**Values:** Proportion of pathway exhibiting each SSF

**Placeholder:**
```
┌────────────────────────────────────────┐
│                                        │
│              SSF Distribution          │
│         ┌────┬────┬────┬────┐          │
│         │ A  │ B  │ C  │Oth │          │
│    SSF1 │████│░░░░│░░░░│░░░░│          │
│    SSF2 │░░░░│████│░░░░│░░░░│          │
│    SSF3 │░░░░│████│░░░░│░░░░│          │
│    SSF4 │░░░░│░░░░│████│░░░░│          │
│    SSF5 │░░░░│░░░░│░░░░│░░░░│          │
│    SSF6 │░░░░│░░░░│████│░░░░│          │
│    SSF7 │████│░░░░│░░░░│░░░░│          │
│         └────┴────┴────┴────┘          │
│                                        │
└────────────────────────────────────────┘
```

---

### Figure 5: Emotional Articulation vs. CF Rate

**Type:** Scatterplot with regression line  
**X-axis:** Emotional Articulation Score  
**Y-axis:** CF Rate (%)  
**Points:** Individual models  
**Annotations:** Model labels, r value, p value

**Placeholder:**
```
┌────────────────────────────────────────┐
│                                        │
│  CF%│                                  │
│     │    ●B                            │
│     │        ●A                        │
│     │  ●C        ●D                    │
│     │                  ●E              │
│     │──────────────────────            │
│     └────────────────────── Artic.     │
│                                        │
│   r = [TBD], p = [TBD]                 │
│                                        │
│     Articulation vs. CF Rate           │
└────────────────────────────────────────┘
```

---

### Figure 6: Classification Confusion Matrix

**Type:** Confusion matrix heatmap  
**Rows:** Actual Pathway  
**Columns:** Predicted Pathway  
**Values:** Count and percentage

**Placeholder:**
```
┌────────────────────────────────────────┐
│                                        │
│           Predicted                    │
│         ┌────┬────┬────┐               │
│         │ A  │ B  │ C  │               │
│    ┌────┼────┼────┼────┤               │
│  A │████│░░░░│░░░░│                    │
│    ├────┼────┼────┼────┤               │
│  B │░░░░│████│░░░░│ Actual             │
│    ├────┼────┼────┼────┤               │
│  C │░░░░│░░░░│████│                    │
│    └────┴────┴────┴────┘               │
│                                        │
│   Overall Accuracy: XX%                │
└────────────────────────────────────────┘
```

---

### Figure 7: Turn-by-Turn Escalation Patterns

**Type:** Line chart (small multiples by pathway)  
**X-axis:** Turn number  
**Y-axis:** Distress level or cumulative harm  
**Lines:** Individual CF responses  
**Overlay:** Average trajectory

**Placeholder:**
```
┌────────────────────────────────────────┐
│  Pathway A    Pathway B    Pathway C   │
│  ┌──────┐     ┌──────┐     ┌──────┐    │
│  │ ╱──  │     │  ──╲ │     │ ──── │    │
│  │╱     │     │     ╲│     │      │    │
│  └──────┘     └──────┘     └──────┘    │
│   T1 T2 T3     T1 T2 T3     T1 T2 T3   │
│                                        │
│        Escalation by Pathway           │
└────────────────────────────────────────┘
```

---

### Figure 8: Branching Point Analysis

**Type:** Decision tree or flow diagram  
**Content:** Key moments where repair could have occurred  
**Annotations:** Frequency of each branch

**Placeholder:**
```
┌────────────────────────────────────────┐
│                                        │
│         Initial Response               │
│              │                         │
│     ┌────────┴────────┐                │
│     │                 │                │
│   SSF=0            SSF=1               │
│   (XX%)            (XX%)               │
│                       │                │
│              ┌────────┴────────┐       │
│              │                 │       │
│           Repair           No Repair   │
│           (XX%)              (XX%)     │
│              │                 │       │
│           CF=0              CF=1       │
│                                        │
└────────────────────────────────────────┘
```

---

## Tables

### Table 1: Sample Characteristics

| Characteristic | n | % |
|---------------|---|---|
| **Total responses** | [TBD] | 100% |
| **By vulnerability type** | | |
| - Acute | [TBD] | [TBD] |
| - Chronic | [TBD] | [TBD] |
| - Transitional | [TBD] | [TBD] |
| **By model** | | |
| - Model A | [TBD] | [TBD] |
| - Model B | [TBD] | [TBD] |
| ... | ... | ... |

---

### Table 2: SSF Prevalence by Type

| SSF Type | n | % | Most Common Co-occurrence |
|----------|---|---|--------------------------|
| SSF-1: Premature Solution | [TBD] | [TBD] | [TBD] |
| SSF-2: Minimization | [TBD] | [TBD] | [TBD] |
| SSF-3: Toxic Positivity | [TBD] | [TBD] | [TBD] |
| SSF-4: Premature Referral | [TBD] | [TBD] | [TBD] |
| SSF-5: Interrogation | [TBD] | [TBD] | [TBD] |
| SSF-6: Experience Hijacking | [TBD] | [TBD] | [TBD] |
| SSF-7: Dismissive Closure | [TBD] | [TBD] | [TBD] |

---

### Table 3: CF Rates by Model and Scenario Type

| Model | Acute CF% | Chronic CF% | Trans. CF% | Overall CF% |
|-------|-----------|-------------|------------|-------------|
| A | [TBD] | [TBD] | [TBD] | [TBD] |
| B | [TBD] | [TBD] | [TBD] | [TBD] |
| C | [TBD] | [TBD] | [TBD] | [TBD] |
| **Overall** | [TBD] | [TBD] | [TBD] | [TBD] |

---

### Table 4: Pathway Characteristics Summary

| Characteristic | Pathway A | Pathway B | Pathway C |
|---------------|-----------|-----------|-----------|
| **Primary SSF types** | SSF-1, SSF-7 | SSF-2, SSF-3 | SSF-4, SSF-6 |
| **Mean turns to CF** | [TBD] | [TBD] | [TBD] |
| **Typical escalation** | [TBD] | [TBD] | [TBD] |
| **% of total CF** | [TBD] | [TBD] | [TBD] |

---

### Table 5: Logistic Regression Results - Pathway Prediction

| Predictor | Pathway A OR (95% CI) | Pathway B OR (95% CI) | Pathway C OR (95% CI) |
|-----------|----------------------|----------------------|----------------------|
| Vulnerability (ref: Acute) | | | |
| - Chronic | [TBD] | [TBD] | [TBD] |
| - Transitional | [TBD] | [TBD] | [TBD] |
| Intensity Level | [TBD] | [TBD] | [TBD] |
| Explicit Distress | [TBD] | [TBD] | [TBD] |
| Support-Seeking | [TBD] | [TBD] | [TBD] |

---

### Table 6: Inter-Rater Reliability

| Measure | Cohen's κ | % Agreement | 95% CI |
|---------|-----------|-------------|--------|
| CF (binary) | [TBD] | [TBD] | [TBD] |
| SSF-1 | [TBD] | [TBD] | [TBD] |
| SSF-2 | [TBD] | [TBD] | [TBD] |
| SSF-3 | [TBD] | [TBD] | [TBD] |
| SSF-4 | [TBD] | [TBD] | [TBD] |
| SSF-5 | [TBD] | [TBD] | [TBD] |
| SSF-6 | [TBD] | [TBD] | [TBD] |
| SSF-7 | [TBD] | [TBD] | [TBD] |
| Repair Level | [TBD] | [TBD] | [TBD] |
| Pathway | [TBD] | [TBD] | [TBD] |

---

## Supplementary Materials

### Supplementary Figure S1: Full SSF Co-occurrence Matrix

### Supplementary Table S1: Complete Response-Level Data (anonymized)

### Supplementary Table S2: Model Identification Key (post-analysis)

### Supplementary Table S3: Excluded Responses and Reasons

---

> 🔒 **CANONICAL — DO NOT EDIT**  
> Locked on 2026-01-20. Changes require new version and changelog entry.  
> See documentation/changelog.md for version control policy.
