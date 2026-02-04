# Complete Site Cleanup Plan — Kill/Redirect/Rewrite
**Date:** February 4, 2026
**Purpose:** Remove confusion, fix facts, ensure one clear offer

---

## 🚨 CRITICAL ISSUES FOUND

### Enterprise Page
**File:** `enterprise.html`
**Problem:** OLD FRAMING - Multiple competing offers
- "License the EQ Safety Framework" ❌
- "Framework Licensing" ❌
- Multiple products instead of one audit ❌

**Action:** REWRITE using enterprise wrapper template

---

## 📋 COMPLETE ACTION LIST (32 Pages)

### 🔴 DELETE IMMEDIATELY (11 files)

**Backup/Working Files:**
```bash
rm index-BACKUP-20260204.html
rm index-REWRITE.html
rm partner-BACKUP-20260204.html
rm partner-NEW.html
rm "ikwe_index_with_apps_link (1).html"
```

**Redundant/Template Files:**
```bash
rm partner.redirect.html
rm nav-footer-template.html
rm HIDDEN_FORM_SNIPPET.html
rm ikwe-og-verified.html
rm offer.html  # Replaced by audit.html
rm explorer.html  # Unclear purpose
```

**After deletion:** 21 pages (from 32)

---

### ✅ KEEP AS-IS (5 pages — Already Correct)

1. ✅ `index.html` — Just rewritten, accurate
2. ✅ `audit.html` — Just created, accurate
3. ✅ `partner.html` — Just updated, accurate
4. ✅ `privacy.html` — Legal, no claims
5. ✅ `terms.html` — Legal, no claims

---

### 🔧 REWRITE NOW (1 page — Competing Offer)

6. **`enterprise.html`** — CRITICAL
   - **Problem:** Old framing, "Framework Licensing", multiple offers
   - **Fix:** Rewrite as enterprise wrapper for audit (NOT new product)
   - **Template:** Provided by user
   - **Priority:** HIGH

---

### 📊 FIX DATA ACCURACY (4 pages — Wrong Numbers)

7. **`eq_safety_dashboard.html`** — CRITICAL
   - **Problem:** Incorrect harm introduction data
   - **Needs:** Correct numbers from Stephanie
   - **Priority:** HIGH

8. **`emotional-safety-gap.html`**
   - **Problem:** May have inaccurate statistics
   - **Needs:** Data verification
   - **Priority:** MEDIUM

9. **`full-report.html`**
   - **Problem:** Research claims may be outdated
   - **Needs:** Accuracy review
   - **Priority:** MEDIUM

10. **`research-summary.html`**
    - **Problem:** Findings may not match current messaging
    - **Needs:** Consistency check
    - **Priority:** MEDIUM

---

### 📝 UPDATE MESSAGING (2 pages — Old Content)

11. **`about.html`**
    - **Problem:** Old "emotional intelligence layer" framing
    - **Fix:** Use prepared content from DEPLOYMENT-READY-PACKAGE.md
    - **Priority:** MEDIUM

12. **`research.html`**
    - **Problem:** Old framework-heavy language
    - **Fix:** Use prepared content (Proof, Not Philosophy)
    - **Priority:** MEDIUM

---

### ✓ REVIEW & POLISH (9 pages — Probably OK)

13. `founder.html` — Check for old framing
14. `faq.html` — Ensure answers current
15. `blog.html` — Check blog index
16. `press.html` — Check press kit messaging
17. `support.html` — Check support page
18. `inquiry.html` — Verify form + messaging
19. `thank-you.html` — Check confirmation message
20. `report-requested.html` — Check confirmation
21. `report.html` — Determine if needed

---

## 🔍 GLOBAL SEARCH & DESTROY

### Language to REMOVE everywhere:

**Search for these:**
```bash
grep -r "platform" *.html
grep -r "framework" *.html
grep -r "prototype" *.html
grep -r "license" *.html
grep -r "comprehensive" *.html
grep -r "end-to-end" *.html
grep -r "EQ Safety" *.html (above fold only)
grep -r "two-stage" *.html (above fold only)
```

**Replace with:**
- ❌ "platform" → ✅ "system" or remove
- ❌ "framework" → ✅ "audit" or "methodology" (deep pages only)
- ❌ "license" → ✅ "request audit"
- ❌ "comprehensive system" → ✅ "scoped engagement"
- ❌ "EQ Safety Benchmark" → ✅ "early risk signals" (above fold)

---

## 📐 CONSISTENCY RULES (Print & Follow)

### Rule 1: One Product Only
**Only page that sells:** `/audit`
- Product name: "Risk & Harm Pattern Audit"
- Never "framework licensing"
- Never "platform"
- Never "comprehensive solution"

### Rule 2: No New Offers
Pages that must NOT introduce new products:
- `/enterprise` → Routes to audit
- `/partner` → Routes to audit (after qualification)
- `/research` → Routes to audit
- `/about` → Routes to audit
- All others → Route to audit

### Rule 3: Terminology Lock
**Above the fold (homepage, audit, enterprise):**
- ✅ "Early risk signals"
- ✅ "Trajectory analysis"
- ✅ "Intervention windows"
- ❌ "EQ Safety Benchmark"
- ❌ "Two-stage framework"
- ❌ "Emotional intelligence layer"

**Deep pages (research, full report) - OK to use:**
- "Two-stage evaluation framework"
- "EQ Safety Benchmark"
- Technical methodology terms

### Rule 4: Safety Check
Before publishing any page, ask:
> "If someone reads this page, can they answer 'What do I buy?' in one sentence?"

**Correct answer:** "A Risk & Harm Pattern Audit"

**If unclear:** Page needs rewrite.

---

## 🎯 PRIORITY EXECUTION ORDER

### TODAY (Critical Path)
1. ✅ Delete 11 backup/redundant files
2. ✅ Rewrite `enterprise.html` (template provided)
3. ✅ Search & destroy problematic language
4. ⏳ Get correct data for `eq_safety_dashboard.html`

### THIS WEEK (Before Deploy)
5. Fix `eq_safety_dashboard.html` with correct data
6. Update `about.html` with new content
7. Update `research.html` with new content
8. Verify `emotional-safety-gap.html` accuracy

### NEXT WEEK (Polish)
9. Review remaining 9 pages for consistency
10. Final accuracy check on research pages
11. Peer review entire site
12. Deploy

---

## 🔧 ENTERPRISE.HTML REWRITE (Exact Template)

**Status:** Ready to execute (see separate file)

**Key changes:**
- ❌ Remove: "License the framework"
- ❌ Remove: "Framework Licensing" section
- ❌ Remove: Multiple competing offers
- ✅ Add: Clear audit focus
- ✅ Add: Scale/coordination context
- ✅ Add: Same four deliverables as audit page
- ✅ Add: Single CTA → Request audit

---

## 📊 PROBLEMATIC LANGUAGE SEARCH RESULTS

**Files with "framework" (need fixing):**
- enterprise.html ❌ (multiple instances)
- research.html ⚠️ (OK on deep page, check above fold)
- eq_safety_dashboard.html ⚠️ (check context)

**Files with "license/licensing":**
- enterprise.html ❌ (MUST remove)

**Files with "platform":**
- enterprise.html ❌ (check context)
- [Need to search others]

**Files with "prototype" (already fixed):**
- ✅ research.html (fixed)
- ✅ eq_safety_dashboard.html (fixed)
- founder.html ✅ (OK in historical context)

---

## ✅ SUCCESS CRITERIA

After cleanup, verify:

**Homepage test:**
- [ ] Can explain Ikwe in 60 seconds
- [ ] Clear what you buy (audit)
- [ ] No competing offers
- [ ] Timeline visual shows timing value

**Audit page test:**
- [ ] Four concrete deliverables listed
- [ ] No new capabilities introduced
- [ ] Clear "no long-term commitment"
- [ ] Single CTA

**Enterprise page test:**
- [ ] Wraps audit for scale (doesn't replace it)
- [ ] Same deliverables as audit page
- [ ] No "framework licensing"
- [ ] Routes to audit CTA

**Site-wide test:**
- [ ] No "platform" language above fold
- [ ] No "license" language anywhere
- [ ] Consistent terminology
- [ ] All CTAs point to audit or inquiry

---

## 🚀 DEPLOYMENT READINESS

**After these fixes:**
- ✅ One clear product (audit)
- ✅ No competing offers
- ✅ No misleading data
- ✅ Enterprise page supports (not competes)
- ✅ Conversion path clear
- ✅ Peer-review ready

---

## 📞 IMMEDIATE NEXT STEPS

1. **Execute deletions** (5 min)
2. **Rewrite enterprise.html** (15 min)
3. **Search & fix language** (20 min)
4. **Get correct dashboard data** (waiting on Stephanie)
5. **Deploy clean site** (1 day after data correction)

---

**Ready to proceed?** Let's execute the deletions and enterprise rewrite now.
