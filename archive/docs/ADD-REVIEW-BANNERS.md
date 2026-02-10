# Add "Under Review" Banners — Exact Implementation
**Purpose:** Prevent visitors from seeing incorrect research data
**Action:** Add banner HTML to 4 research pages

---

## Banner HTML (Copy This)

```html
<!-- UNDER REVIEW BANNER -->
<div style="background: linear-gradient(135deg, rgba(251,146,60,0.15), rgba(251,146,60,0.08)); border-bottom: 2px solid rgba(251,146,60,0.3); padding: 16px 24px; text-align: center;">
  <div style="max-width: 1080px; margin: 0 auto; color: rgba(234,234,240,0.95); font-family: 'DM Sans', system-ui, sans-serif;">
    <strong style="color: #fb923c; font-size: 14px; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700;">⚠️ Under Review</strong>
    <p style="margin: 8px 0 0; font-size: 14px; line-height: 1.6;">This page contains research data currently under accuracy review. Updated findings will be published soon. For current information, see <a href="/" style="color: #a78bfa; text-decoration: underline;">homepage</a> or <a href="/audit" style="color: #a78bfa; text-decoration: underline;">audit page</a>.</p>
  </div>
</div>
```

---

## Where to Insert

### 1. `eq_safety_dashboard.html`
**Location:** After line 1264 (after `</nav>`), before line 1266 (before tab bar)

**Insert between:**
```html
</nav>

<!-- INSERT BANNER HERE -->

<!-- Tab Bar - Always Visible -->
```

---

### 2. `emotional-safety-gap.html`
**Location:** Right after opening `<body>` tag or after navigation

**Find:**
```html
<body>
```

**Insert banner immediately after**

---

### 3. `full-report.html`
**Location:** Right after navigation, before main content

**Find:**
```html
</nav>
```

**Insert banner immediately after**

---

### 4. `research-summary.html`
**Location:** Right after navigation, before main content

**Find:**
```html
</nav>
```

**Insert banner immediately after**

---

## Navigation Updates

### Remove Research Links Temporarily

**Files to update:**
- `index.html`
- `audit.html`
- `enterprise.html`
- `partner.html`
- `about.html`

**In navigation, comment out or remove:**
```html
<!-- TEMPORARILY HIDDEN - UNDER REVIEW
<a href="/emotional-safety-gap" class="dropdown-item">
  <span class="dropdown-title">The Emotional Safety Gap</span>
  <span class="dropdown-desc">Interactive research findings</span>
</a>
<a href="/research" class="dropdown-item">
  <span class="dropdown-title">Methodology</span>
  <span class="dropdown-desc">Two-stage evaluation framework</span>
</a>
<a href="/full-report" class="dropdown-item">
  <span class="dropdown-title">Full Report</span>
  <span class="dropdown-desc">Complete research document</span>
</a>
<a href="/research-summary" class="dropdown-item">
  <span class="dropdown-title">Research Summary</span>
  <span class="dropdown-desc">Key findings overview</span>
</a>
-->
```

**Keep in navigation:**
```html
<a href="/research" class="nav-link">Research</a>
```

**(Research page itself will have banner, but general methodology is OK to link to)**

---

## Faster Alternative: robots.txt

**Instead of navigation changes, add to `robots.txt`:**

```
User-agent: *
Disallow: /eq_safety_dashboard.html
Disallow: /emotional-safety-gap.html
Disallow: /full-report.html
Disallow: /research-summary.html
```

**This prevents:**
- Search engine indexing
- But won't stop direct links

**Combine with banners for maximum safety**

---

## Git Commands After Banners Added

```bash
git add eq_safety_dashboard.html
git add emotional-safety-gap.html
git add full-report.html
git add research-summary.html
git add robots.txt  # if using

git commit -m "Add 'Under Review' banners to research pages pending data verification"
git push
```

---

## What This Achieves

**Protection:**
- ✅ Anyone landing on research pages sees clear warning
- ✅ Links to safe pages (homepage, audit) provided
- ✅ Prevents confusion/trust damage from incorrect data

**Flexibility:**
- ✅ Pages still accessible (for your review)
- ✅ Easy to remove banners when data is verified
- ✅ No content loss

**Professional:**
- ✅ Shows you're careful about accuracy
- ✅ Better than having wrong data up
- ✅ Investors will respect this

---

## When to Remove Banners

**After:**
1. You provide correct dashboard numbers
2. I fix all 4 research pages
3. We verify accuracy
4. You approve changes

**Then:**
```bash
# Remove banner HTML from each file
git add [files]
git commit -m "Remove 'Under Review' banners - research data verified"
git push
```

---

## Quick Implementation (5 minutes)

**Option 1: Manual (Recommended)**
1. Open each of the 4 files
2. Find location (after `</nav>`)
3. Paste banner HTML
4. Save
5. Commit + push

**Option 2: Sed (Fast)**
```bash
# FOR EACH FILE, insert banner after </nav>
# (Adjust line numbers based on your actual files)
```

---

## STATUS: READY TO IMPLEMENT

All banner code ready. Just need to paste into files and commit.

After this is done, your core site can deploy with confidence.
