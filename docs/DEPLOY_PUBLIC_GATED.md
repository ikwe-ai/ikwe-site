# Ikwe Public + Gated Deployment Playbook

## Current state
- Public landing pages exist: `/`, `/research`, `/audit`, `/proof`, `/downloads`.
- Release gates now exist in-repo:
  - `python3 research/analysis/consistency_check.py`
  - `bash scripts/release_gate.sh`
  - GitHub Action: `.github/workflows/release-gate.yml`
- A true auth login/dashboard gate is **not** implemented in this repo yet.

## Pre-release (must pass)
Run from repo root:

```bash
npm run release:gate
```

This blocks release if:
- scored-turn aggregations drift from published CSVs
- headline metrics drift from computed values
- Results hash table is stale
- traceability function references are broken
- required figures/files are missing
- live QA and site consistency checks fail

## Public release flow (safe default)
1. Create release branch:
```bash
git checkout -b codex/release-study-ii-v0.3
```
2. Run gate:
```bash
npm run release:gate
```
3. Commit only intended files:
```bash
git add research/analysis/consistency_check.py scripts/release_gate.sh .github/workflows/release-gate.yml package.json research/benchmark/headline_metrics_v0.3.json
git commit -m "Add Study II consistency/release gates"
git push -u origin codex/release-study-ii-v0.3
```
4. Open PR and require green `Release Gate` check before merge.
5. Merge to `main` after review.
6. In Netlify, deploy the latest `main` commit to production.

## Gated access setup (login + dashboard path)
Use Netlify Access Control for immediate gating:

1. Keep public pages open:
- `/`
- `/research`
- `/audit`
- `/proof`
- `/downloads`

2. Create protected paths for institutional access:
- `/research/validated/*`
- `/dashboard/*`

3. In Netlify UI:
- Site settings -> Access control
- Protect the paths above with team/member login or password gate
- Add approved reviewer emails/domains

4. Add a public request path:
- Send unauthorized users to `/research-access-terms`
- Use `/inquiry` for access requests

## Recommended dashboard rollout
Phase 1 (fast): static dashboard pages under `/dashboard/` + Netlify path protection.  
Phase 2 (institutional): SSO + role-based access + audit logs.  
Phase 3 (production): API-backed dashboards with signed data snapshots and per-release version pinning.
