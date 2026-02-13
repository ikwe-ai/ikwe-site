# Claims-to-Code Traceability — Study II

Study: Study II — Trajectory Safety & Drift Correction

Owner: Visible Healing Inc. (dba Ikwe.ai)

Version: v1.0

Last Updated: 2026-02-13

---

## 0. Scope
This table maps externally visible Study II claims in this repository to:
- source text surfaces
- generation logic
- integrity checks
- reproducibility status

If computation provenance is not present in this repo, fields are marked **UNSPECIFIED** and paired with the required disclosure artifact.

---

## 1. Traceability Table

| Claim ID | Claim Statement (Public) | Appears In | Computation Artifact | Code Reference (file:function:line) | Data Dependencies | Recompute Method | Verification Status | Notes |
|---|---|---|---|---|---|---|---|---|
| C-01 | Baseline emotional-risk introduction rate is 54.7%. | `research.html:172`, `assets/ikwe-scorecard-visual.svg:52`, `samples/public-preview.html:60` | **UNSPECIFIED** (not in this repo) | `assets/ikwe-scorecard-visual.svg` text nodes; `scripts/study_ii_claims_check.sh` canonical pattern check | **UNSPECIFIED** | `bash scripts/study_ii_claims_check.sh` | Partial | Surface-consistent; underlying computation code absent from this repo |
| C-02 | Baseline no-repair-after-harm rate is 43%. | `samples/public-preview.html:61`, `assets/ikwe-scorecard-visual.svg:57` | **UNSPECIFIED** | `scripts/study_ii_claims_check.sh` canonical pattern check | **UNSPECIFIED** | `bash scripts/study_ii_claims_check.sh` | Partial | Same limitation as C-01 |
| C-03 | Observed post-control score reduction range is 42–67%. | `proof.html:233`, `assets/ikwe-scorecard-visual.svg:69`, `samples/public-preview.html:62`, `print/board-brief-print.html:54` | **UNSPECIFIED** | `scripts/study_ii_claims_check.sh` + deprecated phrase blocklist | **UNSPECIFIED** | `bash scripts/study_ii_claims_check.sh` | Partial | Wording hardened from projected to observed |
| C-04 | Evidence basis is n=948 responses across 79 scenarios. | `downloads.html:140`, `downloads/index.html:116`, `proof.html:233`, `assets/ikwe-scorecard-visual.svg:18` | **UNSPECIFIED** | `scripts/study_ii_claims_check.sh` required pattern check | **UNSPECIFIED** | `bash scripts/study_ii_claims_check.sh` | Partial | Basis phrase enforced cross-surface |
| C-05 | Scoring frame uses five risk dimensions + Safety Gate. | `research.html:191`, `print/public-preview-print.html:43`, `print/board-brief-print.html:61`, `print/audit-report-print.html:43` | **UNSPECIFIED** | Template source checks + render pipeline (`scripts/render_pdfs.sh`) | **UNSPECIFIED** | `bash scripts/render_pdfs.sh` then `bash scripts/study_ii_claims_check.sh` | Partial | Display integrity verified; statistical source absent |
| C-06 | Artifact aliases are content-identical for released sample PDFs. | `downloads/*.pdf` | Rendered PDF outputs | `scripts/render_pdfs.sh` copy-sync + `scripts/study_ii_claims_check.sh` SHA256 alias checks | Generated files only | `bash scripts/render_pdfs.sh && bash scripts/study_ii_claims_check.sh` | Verified | Byte identity enforced for alias pairs |
| C-07 | Published claims are tied to methodology and citation references. | `proof.html`, `downloads.html`, `downloads/index.html`, `samples/*.html`, legal footers | HTML source and footer copy | `check-consistency.sh` legal baseline + `scripts/study_ii_claims_check.sh` anchor checks | N/A | `./check-consistency.sh && bash scripts/study_ii_claims_check.sh` | Verified | Method + citation anchors required in claim files |

---

## 2. Required Claim Metadata (Current State)

### Claim C-01 — Metadata
- Claim Type: Quant
- Construct(s): Emotional-risk introduction
- Primary Metric: Proportion
- Unit of Analysis: **UNSPECIFIED**
- Model Versions: **UNSPECIFIED**
- Prompt Template Hash: **UNSPECIFIED**
- Scoring Rubric Version: **UNSPECIFIED**
- Known Limitations: Computation stack absent from this publication repo
- Threats to Validity: See `research/02_validated/study-ii/Threats_To_Validity.md`
- Replication Path: Surface replication only (`bash scripts/study_ii_claims_check.sh`)

### Claim C-02 — Metadata
- Claim Type: Quant
- Construct(s): Repair-after-harm absence
- Primary Metric: Proportion
- Unit of Analysis: **UNSPECIFIED**
- Model Versions: **UNSPECIFIED**
- Prompt Template Hash: **UNSPECIFIED**
- Scoring Rubric Version: **UNSPECIFIED**
- Known Limitations: Computation stack absent from this publication repo
- Threats to Validity: See `research/02_validated/study-ii/Threats_To_Validity.md`
- Replication Path: Surface replication only (`bash scripts/study_ii_claims_check.sh`)

### Claim C-03 — Metadata
- Claim Type: Quant
- Construct(s): Post-control risk score deltas
- Primary Metric: Range delta
- Unit of Analysis: **UNSPECIFIED**
- Model Versions: **UNSPECIFIED**
- Prompt Template Hash: **UNSPECIFIED**
- Scoring Rubric Version: **UNSPECIFIED**
- Known Limitations: Computation stack absent from this publication repo
- Threats to Validity: See `research/02_validated/study-ii/Threats_To_Validity.md`
- Replication Path: Surface replication only (`bash scripts/study_ii_claims_check.sh`)

---

## 3. Unspecified Marker Policy
If required provenance fields are missing, mark them as:

**UNSPECIFIED — verification requires additional disclosure**

No unspecified field may be silently omitted.

---

## 4. Sign-off
Prepared by: Codex automation pass

Reviewed by: __________________
