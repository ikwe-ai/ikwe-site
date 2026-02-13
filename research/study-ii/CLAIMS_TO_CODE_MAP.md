# Study II Claims-to-Code Map

Owner: Visible Healing Inc. (dba Ikwe.ai)

Version: v1.0

Last Updated: 2026-02-13

Status: Active

## Scope
This map covers externally visible Study II benchmark claims surfaced in the ikwe.ai site, sample pages, scorecard visuals, and generated PDFs/PNGs in this repository.

## Canonical Evidence Basis
- Benchmark basis statement: `n=948 responses across 79 scenarios`
- Core metrics:
  - `54.7%` baseline emotional-risk introduction rate
  - `43%` baseline no-repair-after-harm rate
  - `42–67%` observed post-control score reduction range
- Scoring frame: five risk dimensions plus Safety Gate

## Claims Map
| Claim ID | Canonical Claim | Value | Display Surfaces | Source Artifacts / Templates | Generation / Enforcement Code | Third-Party Verification |
|---|---|---:|---|---|---|---|
| C-01 | Baseline emotional-risk introduction rate | 54.7% | `research.html`, `proof.html`, `samples/public-preview.html`, `assets/ikwe-scorecard-visual.svg`, generated PDFs/PNGs | `assets/ikwe-scorecard-visual.svg`, `samples/public-preview.html`, `print/board-brief-print.html` | `scripts/study_ii_claims_check.sh`, `scripts/live_qa_scan.sh`, `scripts/render_pdfs.sh`, `scripts/render_samples.mjs` | Run `bash scripts/study_ii_claims_check.sh` and inspect occurrences with `rg -n "54\.7%"` |
| C-02 | Baseline no-repair-after-harm rate | 43% | `samples/public-preview.html`, `assets/ikwe-scorecard-visual.svg` | `assets/ikwe-scorecard-visual.svg`, `samples/public-preview.html` | `scripts/study_ii_claims_check.sh` | Run `rg -n "43%" assets/ikwe-scorecard-visual.svg samples/public-preview.html` |
| C-03 | Observed post-control reduction range | 42–67% | `proof.html`, `assets/ikwe-scorecard-visual.svg`, `samples/public-preview.html`, board brief PDF | `assets/ikwe-scorecard-visual.svg`, `samples/public-preview.html`, `print/board-brief-print.html` | `scripts/study_ii_claims_check.sh`, `scripts/render_pdfs.sh` | Run `rg -n "42[–-]67%|42–67%" proof.html assets/ikwe-scorecard-visual.svg samples/public-preview.html print/board-brief-print.html` |
| C-04 | Benchmark sample size and scenario count | n=948, 79 scenarios | `research.html`, `downloads.html`, `downloads/index.html`, `proof.html`, `assets/ikwe-scorecard-visual.svg`, `research-access-terms.html` | `assets/ikwe-scorecard-visual.svg` plus page copy | `scripts/study_ii_claims_check.sh` | Run `rg -n "n=948 responses across 79 scenarios|948 responses, 79 scenarios"` across tracked files |
| C-05 | Scoring dimensions + Safety Gate frame | 5+1 | `research.html`, `audit.html`, scorecard visuals/PDFs | `research.html`, `audit.html`, print templates | `scripts/study_ii_claims_check.sh`, `scripts/render_pdfs.sh` | Run `rg -n "five risk dimensions \+ Safety Gate|5\+1" research.html audit.html print/*.html` |
| C-06 | Artifact status and redaction boundary | Redacted sample, not full production disclosure | `proof.html`, `downloads.html`, `samples/*.html`, `print/*.html`, PDF outputs | `samples/*.html`, `print/*.html` | `scripts/study_ii_claims_check.sh`, `scripts/render_pdfs.sh` | Confirm redaction/rights/citation text is present in sample pages and PDF templates |
| C-07 | Rights/citation/legal baseline | All rights reserved + citation/method references | Live pages + sample pages + `research-access-terms.html` | Footer/legal text in HTML templates | `check-consistency.sh`, `scripts/study_ii_claims_check.sh` | Run `./check-consistency.sh` and review legal baseline pass |

## Data/Code Provenance Notes
- This repository is a publication and artifact-delivery surface.
- Primary statistical computation code for Study II is not currently checked into this repo.
- Therefore, reproducibility in this repo is enforced via:
  - canonical claim text constraints
  - deterministic artifact generation pipelines
  - artifact checksum manifest
- If computation code is later added, map each claim to exact script/function/line and pin environment details.

## Artifact Build Graph
1. Canonical source copy lives in:
   - `assets/ikwe-scorecard-visual.svg`
   - `samples/*.html`
   - `print/*.html`
2. PDF generation:
   - `scripts/render_pdfs.sh` -> `downloads/*.pdf`
3. PNG generation:
   - `scripts/render_samples.mjs` -> `downloads/images/*.png`
4. Consistency gates:
   - `scripts/study_ii_claims_check.sh`
   - `scripts/live_qa_scan.sh`
   - `check-consistency.sh`

## Required Release Commands
```bash
bash scripts/render_pdfs.sh
node scripts/render_samples.mjs
bash scripts/generate_study_ii_manifest.sh
bash scripts/study_ii_claims_check.sh
bash scripts/live_qa_scan.sh
./check-consistency.sh
```

## Release Gate
A Study II release is valid only if every command above exits with code 0 and `research/study-ii/ARTIFACT_MANIFEST.sha256` is regenerated in the same release commit.
