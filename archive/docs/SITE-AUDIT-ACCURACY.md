# Ikwe.ai Complete Site Audit — Accuracy Check
**Date:** February 4, 2026
**Purpose:** Identify inaccurate data, misleading claims, and pages to delete

---

## 🚨 Critical Issues Found

### 1. EQ Safety Dashboard (`eq_safety_dashboard.html`)
**Issue:** Contains incorrect data about harm introduction
- Claims "54% introduced harm at first contact"
- **NEED TO VERIFY:** What's the actual correct number from your research?

**Status:** ⚠️ NEEDS CORRECTION

---

## 📊 All Pages Inventory (32 files)

### ✅ CORE PAGES (Keep & Verify)
1. `index.html` — Homepage (just updated, should be accurate)
2. `audit.html` — Risk & Harm Pattern Audit page (just created, accurate)
3. `about.html` — About page (needs content update)
4. `research.html` — Research/methodology (needs content update)
5. `partner.html` — Partnership page (just updated, accurate)
6. `enterprise.html` — For Teams page (needs review)
7. `inquiry.html` — Contact form (needs review)

### 📈 RESEARCH PAGES (Verify Data Accuracy)
8. `eq_safety_dashboard.html` — ⚠️ HAS INCORRECT DATA
9. `emotional-safety-gap.html` — Interactive findings (needs accuracy check)
10. `full-report.html` — Complete research doc (needs accuracy check)
11. `research-summary.html` — Key findings (needs accuracy check)

### 📰 CONTENT PAGES (Review for Consistency)
12. `blog.html` — Blog index
13. `press.html` — Press kit
14. `founder.html` — Founder page
15. `faq.html` — FAQ page
16. `support.html` — Support the research

### ⚙️ UTILITY PAGES (Keep)
17. `privacy.html` — Privacy policy
18. `terms.html` — Terms of service
19. `thank-you.html` — Form submission confirmation
20. `report-requested.html` — Report request confirmation

### 🗑️ DELETE — Backup/Working Files
21. `index-BACKUP-20260204.html` — Backup file
22. `index-REWRITE.html` — Working copy (now deployed to index.html)
23. `partner-BACKUP-20260204.html` — Backup file
24. `partner-NEW.html` — Working copy (deployed to partner.html)
25. `ikwe_index_with_apps_link (1).html` — Old version

### 🗑️ DELETE — Redundant/Unclear Purpose
26. `partner.redirect.html` — Unclear purpose
27. `nav-footer-template.html` — Template file (not needed in production)
28. `HIDDEN_FORM_SNIPPET.html` — Snippet file (not needed in production)
29. `ikwe-og-verified.html` — Unclear purpose
30. `offer.html` — REPLACED by audit.html
31. `explorer.html` — Unclear purpose
32. `report.html` — Possibly redundant with report-requested.html

---

## 🔍 Pages Requiring Data Accuracy Review

### Priority 1: EQ Safety Dashboard
**File:** `eq_safety_dashboard.html`

**What to check:**
- 54.7% vs 45.3% split
- Which number means "passed safety gate"
- Which number means "introduced risk at first contact"
- Stage 1 vs Stage 2 performance numbers
- Ikwe model performance claims
- Baseline model comparisons

**Action needed:** Provide correct numbers from actual research

---

### Priority 2: Emotional Safety Gap
**File:** `emotional-safety-gap.html`

**What to check:**
- All statistics and percentages
- Research methodology claims
- Findings accuracy
- Model performance data

---

### Priority 3: Full Report & Research Summary
**Files:** `full-report.html`, `research-summary.html`

**What to check:**
- Consistency with actual research findings
- No overstated claims
- Accurate methodology description
- Proper limitations and caveats

---

## 🎯 Consistency Checks Across All Pages

### Value Proposition (Must Match)
**Canonical:** "Ikwe helps AI teams identify harm and risk patterns early enough to change outcomes"

**Check these pages:**
- ✅ index.html (correct)
- ⏳ about.html (needs update)
- ⏳ research.html (needs update)
- ✅ audit.html (correct)
- ✅ partner.html (correct)
- ⏳ enterprise.html (needs check)

### Product Name (Must Match)
**Canonical:** "Risk & Harm Pattern Audit"

**Check these pages:**
- ✅ index.html (correct)
- ✅ audit.html (correct)
- ⏳ enterprise.html (needs check)
- ⏳ inquiry.html (needs check)

### Terminology Consistency
**Use:** "Early risk signals" NOT "EQ Safety Benchmark" (above fold)
**Use:** "Trajectory analysis" NOT "Two-stage framework" (above fold)
**Use:** "Model" NOT "Prototype" (✅ already fixed)

---

## 📝 Recommended Actions

### IMMEDIATE (Before Deploy)

1. **Delete backup/working files:**
   ```bash
   rm index-BACKUP-20260204.html
   rm index-REWRITE.html
   rm partner-BACKUP-20260204.html
   rm partner-NEW.html
   rm ikwe_index_with_apps_link\ \(1\).html
   rm partner.redirect.html
   rm nav-footer-template.html
   rm HIDDEN_FORM_SNIPPET.html
   rm ikwe-og-verified.html
   rm offer.html
   ```

2. **Fix EQ Safety Dashboard:**
   - Get correct data from you
   - Update all numbers
   - Verify claims

3. **Verify research pages:**
   - emotional-safety-gap.html
   - full-report.html
   - research-summary.html

### NEXT (After Deploy)

4. **Update content pages:**
   - about.html (use prepared content)
   - research.html (use prepared content)
   - enterprise.html (check messaging)
   - faq.html (ensure accuracy)

5. **Review utility pages:**
   - inquiry.html (ensure form works)
   - thank-you.html (clear messaging)
   - support.html (current)

---

## 🚫 Pages to DELETE (11 files)

**Backup/Working Files (5):**
- index-BACKUP-20260204.html
- index-REWRITE.html
- partner-BACKUP-20260204.html
- partner-NEW.html
- ikwe_index_with_apps_link (1).html

**Redundant/Unclear (6):**
- partner.redirect.html
- nav-footer-template.html
- HIDDEN_FORM_SNIPPET.html
- ikwe-og-verified.html
- offer.html (replaced by audit.html)
- explorer.html (unclear purpose)

**After deletion:** 21 pages remaining (from 32)

---

## ✅ Pages Confirmed Accurate

1. ✅ index.html (just rewritten)
2. ✅ audit.html (just created with exact content)
3. ✅ partner.html (just updated with exact content)
4. ✅ privacy.html (legal, no data claims)
5. ✅ terms.html (legal, no data claims)

---

## ⚠️ Pages Needing Data Verification

**CRITICAL:**
1. eq_safety_dashboard.html — Incorrect harm introduction data
2. emotional-safety-gap.html — All statistics need verification
3. full-report.html — Research claims need verification
4. research-summary.html — Findings need verification

**IMPORTANT:**
5. about.html — Update with new messaging
6. research.html — Update with new messaging
7. enterprise.html — Check value prop consistency
8. founder.html — Check for accuracy
9. faq.html — Ensure answers are current
10. blog.html — Check all blog post claims

---

## 📊 What I Need From You

To fix the data accuracy issues, please provide:

### 1. EQ Safety Dashboard Correct Numbers
- What % passed Stage 1 (safety gate)?
- What % introduced risk at first contact?
- What's Ikwe model's Stage 2 performance?
- What are baseline model Stage 2 numbers?

### 2. Core Research Findings (Accurate)
- What are the key findings you want to highlight?
- What are the limitations/caveats?
- What should NOT be claimed?

### 3. Pages to Keep or Delete
- Should explorer.html be kept or deleted?
- Should report.html be kept or deleted?
- Are there other pages I missed that should go?

---

## 🎯 Goal: Clean, Accurate, Conversion-Ready Site

**After this cleanup:**
- All data accurate and verifiable
- No misleading claims
- No redundant pages
- Clear conversion path
- Peer-review ready
- Investor-grade polish

---

## 📋 Next Steps

1. **YOU:** Provide correct data for EQ Safety Dashboard
2. **ME:** Fix all inaccurate numbers
3. **ME:** Delete unnecessary files
4. **ME:** Update remaining pages for consistency
5. **BOTH:** Final review before deploy

---

**Ready to proceed?** Let me know the correct data and I'll fix everything.
