# IKWE.AI — COMPREHENSIVE SITE AUDIT REPORT
**Date:** February 12, 2026
**Scope:** Full repo audit — content, messaging, data accuracy, assets, theme, navigation, investor-readiness
**Site:** ikwe.ai (hosted on Netlify/Cloudflare, GitHub Pages)
**Domain:** ikwe.ai (CNAME confirmed)

---

## EXECUTIVE SUMMARY

The site is **visually impressive** and has **real substance** behind it — genuine research data (948 responses, 79 scenarios), a legitimate research report with methodology, and a product with clear pricing tiers. The core thesis ("Recognition ≠ Safety") is powerful and differentiated.

**However, there are credibility-breaking issues that must be fixed before putting this in front of investors, VCs, or enterprise buyers.** The founder name inconsistency alone would kill a deal. The mobile navigation being completely absent means half your traffic can't navigate your site. And several data inconsistencies signal lack of attention to detail — exactly the opposite of what a safety/audit company needs to project.

**Bottom line:** The bones are strong. The positioning is ahead of the market. But the polish isn't there yet, and the site has specific issues that undermine trust. Fix the critical items below and you have a pitch-ready platform.

---

## 🔴 CRITICAL — Fix Before Any Outreach

### 1. FOUNDER NAME INCONSISTENCY
- **about.html** says: "Stephanie Stranko"
- **press.html** says: "Stephanie Jirón"
- **research/before-the-violation** metadata says: "Stephanie Stranko"
- **Content guide** says: "Stephanie Stranko"
- **Impact:** An investor doing 30 seconds of due diligence sees two different names on the same site. This reads as either sloppy, fraudulent, or abandoned. It kills trust instantly.
- **Fix:** Choose one name. Update everywhere. Search entire repo for both variants.

### 2. MOBILE NAVIGATION IS COMPLETELY BROKEN
- On every page, at screen width <860px: `@media(max-width:860px){.nav-links{display:none;}}`
- **There is no hamburger menu, no mobile menu, no alternative.** The entire navigation disappears.
- On mobile, users see only the logo. They cannot reach Research, Audit, Proof, About, or the CTA.
- **Impact:** ~60% of web traffic is mobile. Your site is effectively unusable for the majority of visitors. An investor checking on their phone sees a dead end.
- **Fix:** Add a hamburger menu component to every page.

### 3. RISK DIMENSION COUNT INCONSISTENCY
- **research.html stats** say: "6 behavioral safety dimensions scored per response"
- **research.html body** lists only **5** dimensions (Escalation, Dependency, Authority, Scale, Governance)
- **Scorecard everywhere** shows **5** dimensions
- **audit.html outcomes** mentions "six behavioral dimensions — safety gate, escalation, dependency, authority, scale, and governance"
- **The full research report PDF** uses a 2-stage model (Safety Gate binary + quality dimensions)
- **Impact:** Which is it — 5 or 6? An academic, regulator, or technical investor will catch this. For an audit company, data inconsistency is the worst possible signal.
- **Fix:** Standardize. If Safety Gate is counted as the 6th dimension, state that consistently. If it's a separate binary gate (as the research report describes), use "5 risk dimensions + binary Safety Gate" everywhere.

### 4. MISSING MEDIA KIT ZIP
- **press.html** links to `/Ikwe_Media_Kit_2026.zip`
- **This file does not exist.** It's a 404.
- **Impact:** Any journalist or media contact hitting this gets a dead download. Signals the press kit is aspirational, not real.
- **Fix:** Either create the zip file bundling all press PDFs, or remove the link.

### 5. EMAIL OBFUSCATION BROKEN ON KEY PAGES
- **research.html** and **proof.html** footers show `[email protected]` instead of the actual email address
- This is Cloudflare email protection (`data-cfemail`) that renders incorrectly
- **about.html** and **enterprise.html** have the actual email visible
- **Impact:** Two of your most important pages (Research and Proof — the pages investors read) have broken contact info in the footer.
- **Fix:** Either ensure Cloudflare email obfuscation works consistently, or use `mailto:stephanie@ikwe.ai` directly as other pages do.

---

## 🟠 HIGH — Fix This Week

### 6. COLOR ACCENT INCONSISTENCY ACROSS PAGES
- **Homepage, audit.html, enterprise.html** use **lilac/purple** (#A78BFA) as primary accent
- **research.html, proof.html, inquiry.html, press.html** use **rose** (#C4A69A) as primary accent
- Nav CTA button is **lilac** on some pages, **white** on others
- **Impact:** The site feels like two different brands stitched together. An investor clicking from homepage → research → proof notices the shift. It undermines the sense of a unified, professional product.
- **Fix:** Choose one accent system. The lilac is more modern and distinctive. Migrate all pages to the lilac system or create a deliberate dual-accent design language with clear rationale.

### 7. NAV POSITION INCONSISTENCY
- **Homepage, audit.html, enterprise.html** use `position: fixed` (content scrolls behind nav)
- **research.html, proof.html, inquiry.html, press.html** use `position: sticky`
- The fixed-nav pages have proper hero padding (140px). The sticky-nav pages have less (110px).
- **Impact:** Visual inconsistency when navigating between pages. Some pages' content starts lower than others.
- **Fix:** Standardize to `position: fixed` on all pages with matching hero padding.

### 8. BLOG CONTENT ORPHANED
- Three substantive blog posts exist: `the-day-we-stopped-checking.html`, `the-world-fell-once.html`, `blog-wikibear.html`
- The `_redirects` file sends `/blog` to homepage (`/blog → / 301`)
- These posts are not linked from any navigation or page
- **Impact:** Content you created is invisible. Blog posts could be valuable for SEO, thought leadership, and investor due diligence (shows sustained commitment).
- **Fix:** Either create a proper /blog index page and add it to nav, or remove the redirect and link to individual posts from the Research page.

### 9. PLAUSIBLE ANALYTICS INCONSISTENT
- **Present on:** index.html, enterprise.html, press.html
- **Missing from:** research.html, proof.html, inquiry.html, about.html, audit.html
- **Impact:** You're not tracking visits to your most critical pages — Audit (where people buy), Inquiry (where people convert), and Proof (where people evaluate you).
- **Fix:** Add `<script defer data-domain="ikwe.ai" src="https://plausible.io/js/script.js"></script>` to every page's `<head>`.

### 10. DOWNLOADS PORTAL ACCESS CODE IN SOURCE
- `downloads/index.html` contains a hardcoded access code: `IKWE-ACCESS`
- Anyone viewing source can see it
- **Impact:** If gated content is part of the business model, the gate is meaningless. For free previews, the gate creates friction with no security.
- **Fix:** Either remove the access code gate (if the previews are free), or move authentication server-side.

### 11. HOMEPAGE vs. AUDIT TIER MISMATCH
- **Homepage** shows 3 tiers: $2,500 / $5,000 / $25,000+
- **audit.html** shows 4 tiers: $2,500 / $5,000 / $25,000+ / $50,000+
- **enterprise.html** shows only $25,000+
- **Impact:** A visitor going homepage → audit sees a different product lineup. The $50K tier appearing only on the audit page is disorienting.
- **Fix:** Decide: is the $50K tier a standalone product or an upsell? If it belongs in the funnel, show it everywhere. If it's enterprise-only, put it only on /enterprise.

---

## 🟡 MEDIUM — Fix Before Investor Outreach

### 12. CONTENT GUIDE NOT FULLY IMPLEMENTED
The IKWE_COMPLETE_SITE_CONTENT_GUIDE.md describes a restructured homepage with these sections:
- Hero → Problem → Proof/Scorecard → Product Tiers → Who This Is For → CTA
- **Current homepage** uses a slide-based design that doesn't match this flow
- The content guide says to REMOVE: Safety Pyramid, ΔT visualization, Deployment Model, Trust & Governance, Origin sections
- **Some of these may already be removed**, but the current homepage doesn't follow the guide's recommended structure
- **Impact:** The content guide represents the clearest, most sales-focused version of the site. The homepage's slide-based approach is more atmospheric but less conversion-oriented.
- **Fix:** Consider whether the slide-based homepage or the guide's Problem→Proof→Product flow better serves conversion. For investor outreach, the guide's structure is likely stronger.

### 13. SITEMAP REFERENCES NON-EXISTENT PAGES
- sitemap.xml lists `/preview` and `/playbook` as pages
- These actually redirect to `/audit` (302 redirects)
- **Impact:** Search engines see a redirect loop signal. Not catastrophic, but unprofessional.
- **Fix:** Either build the dedicated /preview and /playbook pages (as the content guide calls for) or remove them from sitemap.

### 14. PRESS PDFs ARE DATED
- Press Overview, Visual Sheet, Quotes, and Citation Guide are all from January 9, 2026
- The founder name in press materials is "Jirón" while the rest of the site says "Stranko"
- **Impact:** Press kit may not reflect current positioning
- **Fix:** Update press PDFs to match current site copy and standardized founder name.

### 15. ABOUT PAGE UNDERPLAYS THE FOUNDER
- Current about.html hero: "Most AI safety failures are not technical problems."
- The content guide suggests: "Founded in Iowa. Built for the real world."
- The founder section is present but brief
- For investor readiness: the founder bio needs to sell harder. Over a year of dedicated work, 244,000+ words of testing data, the insight that higher articulation = lower safety — these are differentiators.
- **Fix:** Strengthen the founder section. Add concrete credentials, the journey narrative, and why this person is uniquely positioned. Investors bet on founders.

### 16. .DS_Store AND BACKUP FILES IN REPO
- Multiple `.DS_Store` files (macOS artifacts) committed
- `research/before-the-violation/` has `index.backup.html` and `indexbackup2.html`
- `archive/` directory with old backups
- **Impact:** Minor, but signals lack of engineering hygiene. An investor or technical partner cloning the repo sees this.
- **Fix:** Add `.DS_Store` to `.gitignore`. Remove backup files from the main branch.

---

## 🟢 LOW — Nice to Have / Polish

### 17. NO STRUCTURED DATA (Schema.org)
- No JSON-LD or microdata on any page
- Adding Organization, Product, and Article schema would improve SEO and Google rich results

### 18. FAVICON IS 18KB PNG
- Using `/ikwe_logo_dark.png` (18KB) as favicon
- Should be a proper `.ico` or small `.png` (typically <5KB)

### 19. NO OG:TYPE META TAG
- Most pages have og:title, og:description, og:image but not og:type
- Should add `<meta property="og:type" content="website">` (or "product" for audit page)

### 20. RESEARCH SUBPAGE CLEANUP
- `/research/before-the-violation/` has 3 versions of the same page (index.html, index.backup.html, indexbackup2.html)
- Clean up to single canonical version

### 21. FORM CONFIRMATION
- The inquiry form submits to Netlify but there's no visible confirmation page or success state referenced
- Users may not know if their submission went through
- Consider adding a thank-you redirect or inline confirmation

---

## DATA & CITATION ACCURACY CHECK

### Consistent Data Points (✅ Verified Across Pages)
- **54.7%** of baseline AI responses introduce emotional risk — consistent across homepage, research, proof, audit, press materials, and full research report PDF
- **948 responses** evaluated — consistent everywhere
- **79 scenarios** — consistent everywhere
- **Risk reduction percentages**: −50% Escalation, −58% Dependency, −50% Authority, −42% Scale, −67% Governance — consistent across homepage gauges, proof page, audit scorecard
- **Scorecard scores**: Baseline 80/48/36/48/24, Post-mitigation 40/20/18/28/8 — consistent everywhere
- **Ikwe EI Prototype**: 84.6% conditional performance — matches full research report
- **43%** showed no repair/correction — consistent
- **1.7/5** average regulation score — in research report
- **"Recognition ≠ Safety"** thesis — consistent

### Inconsistencies Found (⚠️)
- **Dimension count**: "6" in research stats vs "5" listed → needs standardization
- **Founder name**: Stranko vs Jirón → needs standardization
- **Tier count**: 3 on homepage vs 4 on audit page → needs decision

### Citation Format (✅)
- Footer citation is consistent: `Ikwe.ai (2026). Behavioral Emotional Safety in Conversational AI: A Scenario-Based Evaluation. Visible Healing Inc.`
- Full research report follows academic convention
- Press overview includes proper disclaimers about what the research does NOT claim

---

## INVESTOR-READINESS ASSESSMENT

### What's Working
1. **Clear product with pricing** — $2.5K / $5K / $25K tiers. Investors see revenue model immediately.
2. **Real data, not vaporware** — 948 responses, 79 scenarios, actual scorecards with before/after
3. **Self-audit credibility** — "We audited ourselves first" is a strong trust signal
4. **Board-ready language** — The audit page speaks directly to the enterprise buyer
5. **Market timing** — EU AI Act, regulatory pressure, AI safety concerns are all converging
6. **Unique positioning** — "Behavioral emotional safety" is a category Ikwe is creating. No direct competitors doing exactly this.

### What's NOT Working for Investors
1. **The mobile experience is broken** (Critical #2 above)
2. **Founder name inconsistency** signals lack of attention to detail (Critical #1)
3. **No team page** — A solo founder is fine, but investors want to see advisors, research partners, or domain experts. Even listing advisory board or academic collaborators would help.
4. **No traction metrics visible** — How many audits completed? Any testimonials? Any logos? Even "3 audits completed" is better than silence.
5. **No competitive landscape framing** — The site doesn't address "why not just use Anthropic's safety tools?" or "how is this different from AI safety labs?"
6. **Revenue model clarity** — Are the $2.5K and $5K products PDFs or live services? The content guide suggests PDF delivery. If so, the margin story is very different than consulting.
7. **The homepage hero is atmospheric, not conversion-focused** — An investor has 15 seconds. The current "You're willing to scale AI fast. Are you willing to scale risk just as fast?" is provocative but doesn't say what Ikwe IS until paragraph 2.

### What Would Make This Investor-Ready
1. Fix all Critical issues
2. Add a one-line clear value prop above the fold: "Ikwe audits AI systems for behavioral safety risk. Board-ready reports in 4 weeks."
3. Add a "Traction" or "Proof Points" section: audits completed, data points analyzed, risk reductions achieved
4. Add team/advisors section on /about
5. Add a comparison section: "Traditional AI safety tests for X. Ikwe tests for Y."
6. Consider a dedicated /investors page with pitch deck download

---

## ASSET INVENTORY

### PDFs (All Verified Present) ✅
| File | Size | Status |
|------|------|--------|
| ikwe_public_preview.pdf | 69KB | Real content |
| ikwe_board_brief.pdf | 50KB | Real content |
| ikwe_audit_report.pdf | 81KB | Real content |
| ikwe_full_research_report.pdf | 13KB | Real content (6-page report) |
| ikwe_research_summary.pdf | 9KB | Real content |
| ikwe_scorecard_sample.pdf | 69KB | Real content |
| ikwe_report_sample.pdf | 81KB | Real content |
| ikwe_action_plan_sample.pdf | 50KB | Real content |
| 01_Ikwe_Press_Overview.pdf | 3.9KB | Real content |
| 02_Ikwe_Press_Visual_Sheet.pdf | 39KB | Real content |
| 03_Ikwe_Approved_Quotes.pdf | 3KB | Real content |
| 04_Ikwe_Citation_Guide.pdf | 4.1KB | Real content |

### Missing Files ❌
| File | Referenced From | Status |
|------|----------------|--------|
| Ikwe_Media_Kit_2026.zip | press.html | MISSING |

### Images (All Verified Present) ✅
- ikwe_logo_dark.png, ikwe-og.png, ikwe-scorecard-visual.svg
- stat-card-1/2/3/4.png, ikwe-logo.png, ikwe-support-banner.png, ikwe-two-stage.png
- downloads/images/ — 3 PNGs for sample previews

### Forms ✅
- inquiry.html — Netlify form (`ikwe-audit`), properly configured with honeypot spam protection
- downloads/index.html — Netlify form (`downloads-access`), access code gated

---

## PRIORITY ACTION PLAN

### NOW (Before any outreach)
1. ~~[ ]~~ Standardize founder name across all pages and PDFs
2. ~~[ ]~~ Add mobile hamburger menu to all pages
3. ~~[ ]~~ Fix dimension count (5 vs 6) — standardize language
4. ~~[ ]~~ Create Ikwe_Media_Kit_2026.zip or remove press link
5. ~~[ ]~~ Fix email display on research.html and proof.html footers

### NEXT (This week)
6. ~~[ ]~~ Standardize color accent to lilac system across all pages
7. ~~[ ]~~ Standardize nav position (fixed vs sticky) across all pages
8. ~~[ ]~~ Add Plausible analytics to all pages
9. ~~[ ]~~ Decide on homepage structure: slide-based vs. content guide's conversion flow
10. ~~[ ]~~ Remove hardcoded access code from downloads portal or remove gate
11. ~~[ ]~~ Standardize tier count (3 vs 4) across homepage and audit page

### LATER (Before investor meetings)
12. ~~[ ]~~ Add traction/proof points section
13. ~~[ ]~~ Strengthen founder bio for investor audience
14. ~~[ ]~~ Add team/advisors section
15. ~~[ ]~~ Build /blog index page and link existing posts
16. ~~[ ]~~ Clean up repo (.DS_Store, backups, archive)
17. ~~[ ]~~ Add structured data markup
18. ~~[ ]~~ Fix sitemap (remove redirect pages or build them)
19. ~~[ ]~~ Consider dedicated /investors page

---

*This audit was conducted against the full repo contents as of February 12, 2026.*
