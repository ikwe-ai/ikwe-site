# Ikwe.ai — Full Site Audit & Cleanup Report
**Date:** February 9, 2026  
**Auditor:** Claude (for Stephanie Stranko)  
**Scope:** GitHub repo (ikwe-ai/ikwe-site), live site (ikwe.ai), uploaded files, placement rules

---

## Executive Summary

The site has strong content and a cohesive visual identity, but the repo is cluttered with artifacts from multiple build iterations, and there are several consistency issues between the live pages, the placement rules doc, and the product pages. This audit covers **5 areas**: repo hygiene, nav/footer consistency, product/PDF alignment, branding issues, and a prioritized action plan.

---

## 1. REPO HYGIENE — Critical Cleanup Needed

### 1A. Files That Should Be Removed from the Repo

The repo contains **development artifacts, zip archives, backups, and node_modules** that should never be in a production repo. This is the #1 cleanup priority.

**Zip archives (should be in releases or removed entirely):**
- `files - 2026-02-09T141456.481.zip`
- `files - 2026-02-09T144057.109.zip`
- `files - 2026-02-09T161033.971.zip`
- `files - 2026-02-09T163850.919.zip`
- `files - 2026-02-09T165108.328.zip`
- `ikwe-site-corrected-v2.1.zip`
- `Ikwe_Media_Kit.zip`
- `Ikwe_Media_Kit_2026.zip`

**Timestamp folders (extracted zips left in repo):**
- `files - 2026-02-09T144057.109/`
- `files - 2026-02-09T162859.784/`
- `files - 2026-02-09T163850.919/`
- `files - 2026-02-09T165108.328/`

**node_modules committed to repo:**
- `node_modules/` — **never commit this**; add to `.gitignore`
- `ikwe-remotion-video/node_modules/` — same

**OS files:**
- `.DS_Store` — add to `.gitignore`

**Backup/draft files:**
- `enterprise-BACKUP-20260204.html`
- `enterprise-NEW.html`
- `ikwe_index_with_apps_link (1).html` (parenthetical copy)

**Superseded deployment docs:**
- `ADD-REVIEW-BANNERS.md`
- `DEPLOY-BANNERS.md`
- `DEPLOYED-CHANGES.md`
- `DEPLOYMENT-READY-PACKAGE.md`
- `FINAL-DEPLOY-READY.md`
- `FINAL-DEPLOYMENT-SUMMARY.md`
- `READY-TO-DEPLOY-CLEANUP.md`
- `REWRITE-SUMMARY.md`
- `SITE-AUDIT-ACCURACY.md`
- `SITE-CLEANUP-PLAN.md`
- `IKWE_SITE_UPDATE_PROMPT.md`
- `IKWE_SITE_UPDATE_PROMPT_v2.md`
- `NOTION_SETUP.md`
- `_redirects_addition` (should be merged into `_redirects` or removed)

**Raw data files (should not be public):**
- `ei_analysis_report_2025-12-19__1_.json`
- `ei_responses_full.json`

### 1B. Duplicate/Overlapping PDF Files

The repo has multiple PDF naming conventions. Reconcile with placement rules:

| In Repo | Placement Rules Expects | Status |
|---------|------------------------|--------|
| `Ikwe_Tier0_Public_Preview.pdf` | `ikwe_public_preview.pdf` | **Name mismatch** |
| `Ikwe_Tier1_Preview_Pack.pdf` | (not in placement rules) | Unclear purpose |
| `Ikwe_Tier2_Playbook.pdf` | (not in placement rules) | Unclear purpose |
| `Ikwe_Full_Report.pdf` | (full report) | OK |
| `Ikwe_Full_Research_Report.pdf` | (duplicate?) | **Possible duplicate** |
| `Ikwe_Full_Research_Report_v1_Jan2026.pdf` | (versioned duplicate?) | **Possible duplicate** |
| `Ikwe_Research_Summary.pdf` | (research summary) | OK |
| `05_Ikwe_Research_Summary.pdf` | (press kit version) | **Duplicate of above?** |
| `Ikwe_Redacted_Audit_FINAL.pdf` | `ikwe_audit_report.pdf` | **Name mismatch** |
| `Ikwe_Self_Audit_FULL_FINAL.pdf` | (not in placement rules) | Unclear purpose |

**Action needed:** Confirm canonical filenames and move them to `/downloads/` per placement rules. Remove or archive duplicates.

### 1C. Duplicate HTML Pages

Several pages appear to exist in multiple versions:

| Current files | Likely canonical | Notes |
|---------------|-----------------|-------|
| `audit.html` + `ikwe_audit_page.html` + `ikwe_audit_landing_page.html` + `ikwe_audit_branded.html` | `audit.html` | 4 versions of audit page |
| `ikwe_playbook_page.html` + `ikwe_playbook_branded.html` | One of these → `playbook.html` | 2 versions |
| `ikwe_preview_page.html` + `ikwe_preview_branded.html` | One of these → `preview.html` | 2 versions |
| `ikwe_proof_page.html` + `ikwe_proof_branded.html` | One of these → `proof.html` | 2 versions |
| `ikwe_public_preview.html` + `ikwe_preview_branded.html` | Unclear overlap | Need to verify |
| `ikwe_board_brief.html` | Canonical | OK |
| `ikwe_audit_report.html` + `audit-report.html` | Pick one | 2 versions |
| `board-brief.html` + `ikwe_board_brief.html` | Pick one | 2 versions |
| `ikwe_scorecard_visual.html` + `ikwe_scorecard_branded.html` | Pick one | 2 versions |
| `ikwe_og_branded.html` + `ikwe-og-verified.html` | Utility pages | May both be needed |
| `enterprise.html` + `enterprise-NEW.html` + `enterprise-BACKUP-20260204.html` | `enterprise.html` | Remove backups |

**Action needed:** Identify which version of each page is canonical, ensure `_redirects` maps clean URLs to them, and remove the rest.

### 1D. Missing .gitignore

The repo needs a `.gitignore` at minimum containing:
```
node_modules/
.DS_Store
*.zip
```

---

## 2. NAVIGATION & FOOTER CONSISTENCY

### 2A. Homepage Navigation (live site)

**Main nav links:**
- Research dropdown: Emotional Safety Gap, Methodology, Full Report, Case Studies, Research & Evidence, Trust & Governance
- About (link)
- For Teams (→ `/enterprise`)
- Request Audit (→ `/inquiry`)

**Footer links:**
- Research: Emotional Safety Gap, Methodology, Full Report
- Company: About, Founder, FAQ, Blog, Press Kit
- Support: Support the Research, Enterprise
- Connect: Contact, Privacy, Terms

### 2B. Research Page Navigation (live site)

**Main nav links — DIFFERENT from homepage:**
- Research dropdown adds: **Research Summary** (not on homepage dropdown)
- About dropdown: About Ikwe.ai, Founder, **FAQ, Blog, Press Kit** (homepage has no About dropdown)
- Adds: Audit, Proof, **Partner**, Support
- "For Teams" → removed, replaced by individual links

**Footer links — DIFFERENT from homepage:**
- Adds: **Research Summary** under Research
- Adds: **Products section** (Preview Pack, Playbook, Full Audit, Enterprise)
- Adds: `stephanie@ikwe.ai` under Connect

### 2C. Press Page Navigation (live site)

**Main nav — DIFFERENT from both above:**
- Research dropdown: **Missing** Research & Evidence, Trust & Governance, Research Summary
- About dropdown: **Missing** FAQ, Blog, Press Kit
- Rest similar to research page

### 2D. Thanks Pages Navigation (uploaded files)

**Main nav — DIFFERENT from all above:**
- No dropdown menus at all
- Just: brand + "Request an AI Risk Audit" button

**Footer links — DIFFERENT from all above:**
- Research: Emotional Safety Gap, Methodology, Full Report
- Company: About, **Audit, Proof, Support** (no Founder, FAQ, Blog, Press)
- Connect: Request an AI Risk Audit, Privacy, Terms
- **Missing:** Products section, stephanie@ikwe.ai, Research Summary

### Summary of Nav/Footer Inconsistencies

| Element | Homepage | Research | Press | Thanks pages |
|---------|----------|----------|-------|-------------|
| Research Summary in nav | ❌ | ✅ | ❌ | ❌ |
| About as dropdown | ❌ | ✅ | ✅ | ❌ |
| Partner link in nav | ❌ | ✅ | ✅ | ❌ |
| Products in footer | ❌ | ✅ | ✅ | ❌ |
| Research & Evidence in nav | ✅ | ✅ | ❌ | ❌ |
| Trust & Governance in nav | ✅ | ✅ | ❌ | ❌ |
| stephanie@ikwe.ai in footer | ❌ | ✅ | ✅ | ❌ |
| Founder/FAQ/Blog in footer | ✅ | ✅ | ✅ | ❌ |

**Recommendation:** Create a shared `includes/nav.html` and `includes/footer.html` (the repo already has an `includes/` directory) and use a build step or JS include to keep all pages synced. Choose the research page version as the canonical template — it's the most complete.

---

## 3. PRODUCT & PDF ALIGNMENT

### 3A. Placement Rules vs. Live Site

Per the `ikwe_site_placement_rules.md`, the homepage hero should have a "View a Completed Audit (Redacted)" button that downloads `ikwe_public_preview.pdf`.

**What the homepage actually has:**
- "See How Ikwe Works" → `#how-it-works` (anchor)
- "View Evidence & Case Studies" → `/case-studies`
- **No direct PDF download on homepage** ❌

The homepage has shifted to an enterprise/infrastructure pitch and dropped the direct PDF lead magnet CTA. This is a **strategic decision** that may be intentional, but it contradicts the placement rules.

### 3B. Research Page Download Links

The research page has:
- "Download Summary (PDF)" → `/Ikwe_Research_Summary.pdf` (root-level file)
- "View Sample Audit Output" → `/downloads/#public-preview` (hash anchor)

**Issues:**
- The PDF is served from the root (`/Ikwe_Research_Summary.pdf`) instead of `/downloads/` — inconsistent with placement rules
- `/downloads/#public-preview` is a hash anchor, not a direct PDF link — is there a downloads page with anchored sections?

### 3C. Thanks Pages Download Links

- thanks-playbook: links to `/downloads/#board-brief` and `/downloads/#audit-report`
- thanks-preview: links to `/downloads/#public-preview` and `/downloads/#board-brief`

**These hash anchors suggest a `/downloads/` page exists with anchored sections.** This is fine as a pattern, but the placement rules say PDFs should be at direct paths like `/downloads/ikwe_public_preview.pdf`.

**Questions to resolve:**
1. Does a `/downloads/index.html` page exist with password-gated sections?
2. Are the direct PDF paths (`/downloads/ikwe_public_preview.pdf`, etc.) also working?
3. Do the PDF filenames in the repo match what the download page expects?

### 3D. Press Page Statistics

The press page reports:
- **312 total responses** across **79 scenarios** and **4 AI systems**

But your core research tested **948 responses** across **79 scenarios**. The 312 number may represent a specific subset (79 × 4 = 316, close to 312). Verify this is intentionally the public-facing number.

### 3E. Product Tier Mapping

From the footer "Products" section on research/press pages:
- Preview Pack → `/preview`
- Playbook → `/playbook`
- Full Audit → `/audit`
- Enterprise → `/enterprise`

From the placement rules CTA routing:
- Preview Pack ($250) → Stripe checkout
- Playbook ($5,000) → Stripe checkout
- Full Audit ($25,000) → `/inquiry.html`
- Implementation ($50K+) → `stephanie@ikwe.ai`

**Verify:** Are the Stripe checkout links configured and working on the product pages?

---

## 4. BRANDING & ENCODING ISSUES

### 4A. Character Encoding

Both `thanks-playbook.html` and `thanks-preview.html` have:
```
Â© 2026 Visible Healing Inc. Â· Des Moines, Iowa
```
Should be:
```
© 2026 Visible Healing Inc. · Des Moines, Iowa
```
This is a UTF-8 double-encoding issue. The `Â` characters appear when UTF-8 bytes are decoded as Latin-1 then re-encoded.

**Fix:** Replace `Â©` with `©` and `Â·` with `·` (or use HTML entities `&copy;` and `&middot;`).

### 4B. OG Image Inconsistency

- Thanks pages reference: `/og_image.png`
- Repo has: `ikwe-og.png` and `ikwe-press-og.png`
- Homepage meta likely references one of these

**Verify:** Does `/og_image.png` resolve, or should it be `ikwe-og.png`?

### 4C. Logo Reference

All pages reference `/ikwe_logo_dark.png` — this file exists in the repo ✅

### 4D. Email Inconsistency

- Thanks pages: `stephanie@ikwe.ai`
- Press page contact: `press@ikwe.ai`
- Research page footer: `stephanie@ikwe.ai`

Both are fine — just confirm both email addresses are active.

### 4E. Tagline Variations

- Homepage: "Emotional safety infrastructure for AI systems"
- Homepage footer: "Early risk detection for AI teams"
- Research page: "Ikwe builds behavioral emotional safety infrastructure for AI — the EQ that allows IQ to scale without breaking trust"
- Thanks pages: "Behavioral emotional safety infrastructure for AI"
- Press page: Same as research

The homepage footer ("Early risk detection for AI teams") is the most different — it sounds more like a product tagline than the institutional "behavioral emotional safety infrastructure" language used elsewhere.

**Recommendation:** Standardize to one primary tagline across all pages. "Behavioral emotional safety infrastructure for AI" or "Emotional safety infrastructure for AI systems" are both strong.

### 4F. Copyright/Location

- Homepage: "© 2026 Visible Healing Inc. Des Moines, Iowa" ✅
- Research/Press: Same ✅
- Thanks pages: Encoding issue (see 4A) but content correct

---

## 5. PAGE INVENTORY — What Exists vs. What's Linked

### Pages Confirmed Live (fetched successfully)
- `/` (index.html) ✅
- `/research` ✅
- `/press` ✅

### Pages Linked from Nav/Footer (not yet verified live)
- `/emotional-safety-gap`
- `/full-report`
- `/case-studies`
- `/research-and-evidence`
- `/trust-and-governance`
- `/research-summary`
- `/about`
- `/founder`
- `/faq`
- `/blog`
- `/enterprise`
- `/audit`
- `/proof`
- `/partner`
- `/support`
- `/inquiry`
- `/preview`
- `/playbook`
- `/privacy`
- `/terms`

### Pages in Repo with No Clear Nav Link
- `explorer.html`
- `eq_safety_dashboard.html`
- `ikwe_risk_audit_dashboard.jsx`
- `audit-report-print.html`
- `board-brief-print.html`
- `ikwe_og_branded.html`
- `ikwe-og-verified.html`
- `ikwe_content_distribution_v2.md`
- `access-request.js`
- `check-consistency.sh`
- `HIDDEN_FORM_SNIPPET.html`

**Action needed:** Verify all linked pages resolve. Any that 404 need either a redirect or the page needs to be created/renamed.

---

## 6. PRIORITIZED ACTION PLAN

### Phase 1: Repo Cleanup (Do First)

1. **Create `.gitignore`** — add `node_modules/`, `.DS_Store`, `*.zip`
2. **Delete zip archives** from repo (5 timestamped + 2 media kit + 1 corrected)
3. **Delete timestamp folders** (4 extracted zip folders)
4. **Delete backup/draft HTML** (`enterprise-BACKUP`, `enterprise-NEW`, `ikwe_index_with_apps_link (1)`)
5. **Delete superseded docs** (all the deployment/cleanup markdown files listed in 1A)
6. **Move raw JSON data** (`ei_analysis_report...json`, `ei_responses_full.json`) to a private repo or remove
7. **Consolidate PDFs** — pick canonical names, move to `/downloads/`, remove duplicates
8. **Remove `node_modules/`** from repo history (requires `git filter-branch` or BFG)

### Phase 2: Navigation & Footer Sync

9. **Pick canonical nav/footer template** — use the research page version (most complete)
10. **Apply to all pages** — either via includes or manual sync
11. **Fix encoding** on thanks-playbook.html and thanks-preview.html (`Â©` → `©`)

### Phase 3: Product Pages & PDFs

12. **Verify all product pages** (`/preview`, `/playbook`, `/audit`) are live and have correct Stripe links
13. **Verify `/downloads/` page** exists and hash anchors work
14. **Verify PDF paths** match between download links and actual files
15. **Verify OG image** path (`/og_image.png` vs `ikwe-og.png`)
16. **Standardize tagline** across all pages

### Phase 4: Link Verification

17. **Test all 20+ internal links** from nav/footer — identify any 404s
18. **Verify `_redirects`** file maps clean URLs (e.g., `/audit` → `audit.html`) correctly
19. **Check Stripe product links** are functional

### Phase 5: Final Polish

20. **Decide on duplicate HTML pages** — which is canonical for audit, playbook, preview, proof, scorecard
21. **Archive or remove non-canonical versions**
22. **Update `README.txt`** to reflect current site structure (it currently shows the media kit README, not a site README)

---

## Quick Wins (Can Do Right Now)

- [ ] Fix `Â©` encoding in both thanks pages
- [ ] Create `.gitignore`
- [ ] Delete `.DS_Store` from repo
- [ ] Standardize footer tagline
- [ ] Verify OG image filename

---

*This audit covers what was accessible. A full link-by-link test of all 20+ pages would complete the picture. Recommend running a crawler (like `wget --spider`) against the live site to catch any 404s.*
