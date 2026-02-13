# Study II Hostile Peer Review Stress Test

Owner: Visible Healing Inc. (dba Ikwe.ai)

Version: v1.0

Last Updated: 2026-02-13

## Purpose
This protocol pressure-tests Study II publication integrity against adversarial review focused on contradiction hunting, unverifiable claims, and reproducibility gaps.

## Threat Model
Adversarial reviewers are expected to challenge:
- Numeric drift between pages, visuals, PDFs, and PNG exports
- Ambiguous claim wording (for example, `projected` vs `observed`)
- Missing methods/citation references near quantitative claims
- Inconsistent artifact aliases
- Link and route failures
- Missing legal/IP boundaries for gated research

## Stress-Test Matrix
| Test ID | Failure Pattern | Test Method | Pass Criteria |
|---|---|---|---|
| HPR-01 | Contradictory claim wording | `bash scripts/study_ii_claims_check.sh` | No deprecated phrasing detected |
| HPR-02 | Missing canonical benchmark basis | `bash scripts/study_ii_claims_check.sh` | Canonical benchmark basis statement present |
| HPR-03 | Broken cross-surface consistency | `rg -n "54\.7%|43%|42–67%|n=948"` on tracked sources | All canonical claims are present only in approved wording |
| HPR-04 | PDF alias drift | `bash scripts/study_ii_claims_check.sh` | Alias pairs are byte-identical |
| HPR-05 | Routing/link inconsistency | `./check-consistency.sh` | No missing local links or routes |
| HPR-06 | Pricing or offer drift | `bash scripts/live_qa_scan.sh` | No old-pricing strings; expected pricing present |
| HPR-07 | Missing legal/citation boundary | `./check-consistency.sh` | Legal baseline checks pass |
| HPR-08 | Non-deterministic artifact output | Rebuild + compare manifest | Manifest regenerated and reviewed for expected delta |

## Hostile Questions and Required Evidence
| Reviewer Question | Required Evidence |
|---|---|
| "Where is this number sourced?" | Claim ID from `CLAIMS_TO_CODE_MAP.md` + source file path + line search output |
| "How do we know exports match source copy?" | Build scripts + checksum manifest + alias byte-equality checks |
| "Are statements observational or projected?" | Canonical wording checks in `scripts/study_ii_claims_check.sh` |
| "Can another team verify your surface claims?" | Public methodology page, citation guide, and deterministic verification command set |

## Runbook
```bash
bash scripts/render_pdfs.sh
node scripts/render_samples.mjs
bash scripts/generate_study_ii_manifest.sh
bash scripts/study_ii_claims_check.sh
bash scripts/live_qa_scan.sh
./check-consistency.sh
```

## Acceptance Criteria
- All commands pass with exit code 0.
- No deprecated/non-verifiable claim phrasing remains.
- Canonical basis statement and methodology/citation references are present on all tracked surfaces.
- Manifest file updated and reviewed.

## Incident Response (If Any Test Fails)
1. Freeze release branch.
2. Record failing command and output in release notes.
3. Patch source templates first, then regenerate artifacts.
4. Regenerate manifest.
5. Re-run full runbook.
6. Require second-person review before publish.

## Governance Notes
- This protocol is a publication-integrity gate, not a substitute for raw-data disclosure.
- If computation code is moved into this repo later, add function-level claim mappings and environment pinning immediately.
