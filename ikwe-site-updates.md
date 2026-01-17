# Ikwe.ai Site Updates: PDF Access Structure

## Summary of Current State

**Files reviewed:**
- `index.html` — Homepage
- `research.html` — Research/methodology page
- `emotional-safety-gap.html` — Main findings page
- `inquiry.html` — Contact/inquiry form
- `inquiry.js` & `access-request.js` — Netlify functions for form handling

**Current PDF references found:**
1. `emotional-safety-gap.html` line 581: "Full Report PDF" links to `/inquiry` (already gated via form)
2. `research.html` line 137: "Request Full Methodology Access" button
3. No direct public links to either PDF currently exist on the site

**Good news:** The site doesn't currently expose direct PDF links. The structure is already partially gated.

---

## Recommended Architecture

```
/05_Ikwe_Research_Summary.pdf     → PUBLIC (direct download)
/Ikwe_Full_Research_Report_v1_Jan2026.pdf → GATED (via /report page)
```

**Flow:**
1. Public summary PDF: Direct links from research pages
2. Full report: `/report` landing page → Email capture → Thank-you/confirmation page

---

## Checklist of Changes

### 1. Files to Add

| File | Purpose |
|------|---------|
| `/report.html` | Landing page describing full report + access request form |
| `/report-requested.html` | Confirmation page after form submission |

### 2. Files to Edit

| File | Change |
|------|--------|
| `emotional-safety-gap.html` | Update "Full Report PDF" resource link to go to `/report` |
| `research.html` | Add public summary download button; update full methodology link |
| `index.html` | Add download button in CTA section (optional) |

### 3. Netlify Function Updates

The existing `access-request.js` can handle report requests. No changes needed unless you want a separate database for report requests.

---

## Exact HTML Changes

### Change 1: emotional-safety-gap.html (line ~581)

**Current:**
```html
<a href="/inquiry" class="resource-item locked" id="pdf-resource"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg><span>Full Report PDF</span></a>
```

**Replace with:**
```html
<a href="/report" class="resource-item locked" id="pdf-resource"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg><span>Full Report PDF</span></a>
```

Also add a new public summary download link. Find the resources-grid section (~line 578-583) and update to:

```html
<div class="resources-grid">
  <a href="/explorer" class="resource-item"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path></svg><span>Scenario Explorer</span></a>
  <a href="/press" class="resource-item"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"></path></svg><span>Press Kit</span></a>
  <a href="/05_Ikwe_Research_Summary.pdf" class="resource-item" download><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg><span>Research Summary (PDF)</span></a>
  <a href="/report" class="resource-item locked" id="pdf-resource"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg><span>Full Report Access</span></a>
</div>
```

---

### Change 2: research.html (line ~135-139)

**Current:**
```html
<div class="cta">
  <a class="btn" href="/emotional-safety-gap">Explore the Findings <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg></a>
  <a class="btn secondary" href="/inquiry">Request Full Methodology Access</a>
</div>
```

**Replace with:**
```html
<div class="cta">
  <a class="btn" href="/emotional-safety-gap">Explore the Findings <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg></a>
  <a class="btn secondary" href="/05_Ikwe_Research_Summary.pdf" download>Download Summary (PDF) <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg></a>
</div>
<div class="note" style="margin-top:12px;"><a href="/report" style="color:var(--purple);">Request full report access →</a></div>
```

---

### Change 3: index.html (line ~308-311) — Optional

**Current:**
```html
<div class="cta-btns">
  <a class="btn primary" href="/emotional-safety-gap">Explore the Research</a>
  <a class="btn" href="/inquiry">Start a Conversation</a>
</div>
```

**Replace with (optional — adds summary download):**
```html
<div class="cta-btns">
  <a class="btn primary" href="/emotional-safety-gap">Explore the Research</a>
  <a class="btn" href="/05_Ikwe_Research_Summary.pdf" download>Download Summary (PDF)</a>
  <a class="btn" href="/inquiry">Start a Conversation</a>
</div>
```

---

## New Pages to Create

See the following files (created separately):
- `report.html` — Full report landing page
- `report-requested.html` — Confirmation page

---

## Gating Flow (Static Site Compatible)

**Option A: Simple Email Capture (Recommended)**

1. User lands on `/report`
2. User fills out email + intended use
3. Form submits to Netlify Forms or existing Notion function
4. User is redirected to `/report-requested`
5. You manually review and send PDF via email

**Option B: Instant Access (Less Secure)**

1. Same flow, but `/report-requested` includes a temporary download link
2. Link is not indexed, but technically accessible if someone guesses URL

**Recommendation:** Use Option A. It creates a touchpoint for press/partnership conversations and keeps the full report genuinely gated.

---

## Files to Upload to Site Root

Ensure these files are in your site's root directory:

```
/05_Ikwe_Research_Summary.pdf          ← Public download
/Ikwe_Full_Research_Report_v1_Jan2026.pdf  ← Keep but don't link publicly
```

The full report filename should NOT appear in any public HTML. You'll send it manually after reviewing access requests.

---

## Verification Checklist

After deploying:

- [ ] `/05_Ikwe_Research_Summary.pdf` downloads directly
- [ ] `/report` shows landing page with form
- [ ] Form submission creates entry in Notion (or Netlify Forms)
- [ ] `/report-requested` shows confirmation
- [ ] "Full Report PDF" link on `/emotional-safety-gap` goes to `/report`
- [ ] Research summary download works from `/research`
- [ ] No public link to `Ikwe_Full_Research_Report_v1_Jan2026.pdf` exists
