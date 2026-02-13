# Ikwe Governance Benchmark — Statistical Reporting Standards (Study II)

**Generated:** 2026-02-12 (America/Chicago)  
**Applies to:** Study II slice results generated from `study_ii_turns_scored.csv`

---

## 1. Proportion Estimates (Wilson Score Interval)

For any proportion (e.g., harm rate, violation rate):

- Observed count: `k`
- Total trials: `n`
- Point estimate: \( \hat{p} = k/n \)

Wilson interval (95%):

\[
CI = \frac{\hat{p} + \frac{z^2}{2n} \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}
\]

Where \( z = 1.96 \) for 95%.

### Worked examples (from this slice)

**Baseline (overall):** k=21, n=30, \(\hat{p}=0.700\), CI=[0.521, 0.833]

**Ikwe (overall):** k=21, n=24, \(\hat{p}=0.875\), CI=[0.690, 0.957]

---

## 2. Difference in Proportions (Newcombe–Wilson)

For two independent proportions:

- Group 1: \(k_1, n_1\)
- Group 2: \(k_2, n_2\)
- Difference: \( \Delta = \hat{p}_1 - \hat{p}_2 \)

We use Newcombe’s method based on Wilson intervals:

\[
CI_\Delta = [L_1 - U_2,\; U_1 - L_2]
\]

Where \([L_i, U_i]\) are Wilson bounds for each group.

### Worked example (Ikwe − Baseline, overall)

- Ikwe: k1=21, n1=24
- Baseline: k2=21, n2=30
- \(\Delta=0.175\)
- 95% CI (Newcombe–Wilson): [-0.143, 0.435]

---

## 3. Reporting Requirements

Every reported proportion MUST include:

- k and n
- point estimate
- 95% CI method (Wilson unless otherwise specified)

Every reported difference MUST include:

- definition of groups
- point estimate \(\Delta\)
- uncertainty interval (Newcombe–Wilson unless otherwise specified)

---

## 4. Notes on Small Sample Sizes

This slice has small *n* by design (pilot scale). Therefore:

- CIs will be wide
- Apparent deltas should be described as **descriptive** unless replicated at larger scale
- Any claims of “improvement” should be phrased as “observed under this protocol”

---
