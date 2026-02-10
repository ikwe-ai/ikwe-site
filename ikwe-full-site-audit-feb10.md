# Ikwe.ai — Full Site Audit
## February 10, 2026

---

## 1. REPO HYGIENE — CRITICAL

The repo has **476 commits** and significant bloat that needs cleanup before the next deploy.

### Delete These (not site content):
- `files - 2026-02-09T144057.109/` — timestamped export dump
- `files - 2026-02-09T162859.784/` — timestamped export dump
- `files - 2026-02-09T163850.919/` — timestamped export dump
- `files - 2026-02-09T165108.328/` — timestamped export dump
- `node_modules/` — NEVER commit node_modules
- `ikwe-remotion-video/` — Remotion project with committed node_modules
- `.DS_Store` — Mac system file
- `access-request.js` — unused
- `HIDDEN_FORM_SNIPPET.html` — unused
- `_redirects_addition` — merge into `_redirects`

### Move to `/docs` or Delete (deployment artifacts, not site content):
- `ADD-REVIEW-BANNERS.md`
- `DEPLOY-BANNERS.md`
- `DEPLOYED-CHANGES.md`
- `DEPLOYMENT-READY-PACKAGE.md`
- `FINAL-DEPLOY-READY.md`
- `FINAL-DEPLOYMENT-SUMMARY.md`
- `IKWE_COMPLETE_SITE_CONTENT_GUIDE.md`
- `IKWE_SITE_UPDATE_PROMPT.md`
- `IKWE_SITE_UPDATE_PROMPT_v2.md`
- `NOTION_SETUP.md`
- `READY-TO-DEPLOY-CLEANUP.md`
- `REWRITE-SUMMARY.md`
- `SITE-AUDIT-ACCURACY.md`
- `SITE-CLEANUP-PLAN.md`
- `STRIPE_PRODUCTS.md`

### PDF Consolidation (move to `/downloads`, delete old duplicates):

| Keep (move to /downloads if not there) | Delete (old/duplicate) |
|----------------------------------------|----------------------|
| `ikwe_research_summary_branded.pdf` ✨ NEW | `Ikwe_Full_Report.pdf` |
| `ikwe_full_research_report_branded.pdf` ✨ NEW | `Ikwe_Full_Research_Report.pdf` |
| `ikwe_audit_report.pdf` ✅ branded | `Ikwe_Full_Research_Report_v1_Jan2026.pdf` |
| `ikwe_board_brief.pdf` ✅ branded | `Ikwe_Research_Summary.pdf` |
| `ikwe_public_preview.pdf` ✅ branded | `05_Ikwe_Research_Summary.pdf` |
| `Ikwe_Media_Kit_2026.zip` | `Ikwe_Media_Kit.zip` (old version) |
| Press kit PDFs (01–04) | `Ikwe_Self_Audit_FULL_FINAL.pdf` |
| | `Ikwe_Redacted_Audit_FINAL.pdf` |
| | `Ikwe_Tier0_Public_Preview.pdf` |
| | `Ikwe_Tier1_Preview_Pack.pdf` |
| | `Ikwe_Tier2_Playbook.pdf` |

### Add `.gitignore`:
```
node_modules/
.DS_Store
*.zip.bak
```

---

## 2. PAGES — LIVE vs BUILT vs NEEDED

### Core Pages (8 — all built, ready to deploy)

| Route | Live Status | Our File | Deploy? |
|-------|------------|----------|---------|
| `/` | ✅ Live (hybrid: new design + old dropdown nav) | `index-final.html` | YES — fixes nav + meta |
| `/about` | ✅ Live (old version) | `about-final.html` | YES |
| `/audit` | ✅ Live (old version) | `audit-final.html` | YES |
| `/research` | ✅ Live (old version) | `research-final.html` | YES |
| `/proof` | ✅ Live (old version) | `proof-final.html` | YES |
| `/enterprise` | ✅ Live (old version) | `enterprise-final.html` | YES |
| `/inquiry` | ✅ Live (NEW version deployed) | `inquiry-final.html` | DONE ✓ |
| `/downloads` | ✅ Live (old palette) | `downloads-final.html` | YES |

### Missing Pages (need creation)

| Route | Linked From | Action |
|-------|------------|--------|
| `/press` | Footer on all pages | **Build** — press kit page |
| `/privacy` | Footer on all pages | **Build** — privacy policy |
| `/terms` | Footer on all pages | **Build** — terms of service |
| `/404` | Netlify fallback | **Build** — custom error page |

### Routes That Need Redirects (not pages)

| Route | Redirect To | Reason |
|-------|------------|--------|
| `/full-report` | `/downloads/ikwe_full_research_report.pdf` | Footer link |
| `/case-studies` | `/proof` | Footer link |
| `/emotional-safety-gap` | `/research` | Footer link |
| `/support` | `/inquiry` | Footer link |
| `/founder` | `/about` | Footer link |
| `/faq` | `/about` | Footer link |
| `/partner` | `/enterprise` | Legacy |
| `/blog` | `/` | Legacy |
| `/playbook` | `/audit` | Product link (tier) |
| `/preview` | `/audit` | Product link (tier) |

### Legacy Pages (in repo, can keep or redirect)

| Route | Status | Recommendation |
|-------|--------|---------------|
| `/board-brief` | Live, old design | Redirect to `/downloads/ikwe_board_brief.pdf` |
| `/audit-report` | Live, old design | Redirect to `/downloads/ikwe_audit_report.pdf` |
| `/audit-report-print` | Live, print layout | Keep for now |
| `/board-brief-print` | Live, print layout | Keep for now |
| `/blog` | Live, old design | Redirect to `/` |
| `/scorecard` | Component, not a page | Keep for embeds |

---

## 3. INCONSISTENCIES FOUND

### A. Navigation
**Problem:** Live homepage uses dropdown menus (Research▾, Pricing▾, About▾). Our 8 rebuilt pages use flat nav links (Research, Audit, Proof, About). The inquiry page (already deployed) uses the flat nav.

**Fix:** Deploy all 8 core pages → flat nav becomes the standard everywhere. Dropdowns were adding complexity without helping conversion.

### B. Footer Links Point to Non-Existent Routes
**Problem:** Footer on rebuilt pages links to `/emotional-safety-gap`, `/full-report`, `/case-studies`, `/founder`, `/faq` — none of which exist as pages.

**Fix:** Add redirects in `_redirects` file (see section above). This is cheaper and safer than creating new pages.

### C. PDF File Naming Chaos
**Problem:** Same PDFs exist at multiple paths with different names. Root dir has 15+ PDFs that belong in `/downloads/`.

**Fix:** Consolidate all PDFs to `/downloads/` with clean lowercase names. Add redirects for old paths.

### D. Search Engine Meta Description
**Problem:** Google shows the old description: *"Experience emotionally intelligent AI that truly understands. Built by a Lady. Powered by Love."*

**Fix:** Deploy `index-final.html` which has: *"Board-ready AI risk audits for companies scaling conversational AI, agents, and decision systems."* It will take Google 1-4 weeks to re-index.

### E. Stripe Links
**Problem:** Audit page links to specific Stripe buy URLs that need verification.

**Fix:** Test all Stripe links after deploy. Current links in audit page:
- System Blueprint: `https://buy.stripe.com/14AeVe1AEetHg7QamR9sk06`
- Preview Pack: `https://buy.stripe.com/fZudRa6UY85jaNw2Up9sk04`
- DIY Playbook: `https://buy.stripe.com/28E8wQ2EI2L18Fo59a9sk05`

---

## 4. DEPLOY ORDER

### Phase 1: Core Pages (do all at once)
1. Replace `index.html` ← `index-final.html`
2. Replace `about.html` ← `about-final.html`
3. Replace `audit.html` ← `audit-final.html`
4. Replace `research.html` ← `research-final.html`
5. Replace `proof.html` ← `proof-final.html`
6. Replace `enterprise.html` ← `enterprise-final.html`
7. Replace `downloads/index.html` ← `downloads-final.html`
8. Verify `inquiry.html` ← already deployed ✓

### Phase 2: Missing Pages + Redirects
9. Add `press.html`
10. Add `privacy.html`
11. Add `terms.html`
12. Add `404.html`
13. Replace `_redirects` with comprehensive version
14. Add `.gitignore`

### Phase 3: PDF Cleanup
15. Replace research PDFs with branded versions
16. Move root PDFs to `/downloads/`
17. Add PDF redirect rules

### Phase 4: Repo Cleanup
18. Delete junk folders
19. Delete deployment docs (or move to /docs)
20. Delete duplicate PDFs
21. Delete committed node_modules
