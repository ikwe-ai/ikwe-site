# Deploy "Under Review" Banners — Ready to Commit

**Status:** ✅ All changes staged and ready for commit
**Date:** February 4, 2026

---

## What Was Done

### ✅ Completed Actions

1. **Added warning banners to 4 research pages:**
   - `eq_safety_dashboard.html` — Banner inserted after `</nav>` (line 1264)
   - `emotional-safety-gap.html` — Banner inserted after `<body>` tag (line 318)
   - `full-report.html` — Banner inserted after `</nav>` (line 759)
   - `research-summary.html` — Banner inserted after `</nav>` (line 854)

2. **Updated `robots.txt`:**
   - Added Disallow rules for all 4 research pages
   - Prevents search engine indexing while data is under review

3. **Created documentation:**
   - `ADD-REVIEW-BANNERS.md` — Full implementation guide for future reference

---

## Banner Content

All pages now display this prominent warning:

```
⚠️ UNDER REVIEW

This page contains research data currently under accuracy review.
Updated findings will be published soon. For current information,
see homepage or audit page.
```

**Visual styling:**
- Orange gradient background (`rgba(251,146,60,0.15)` to `rgba(251,146,60,0.08)`)
- Orange border bottom (`rgba(251,146,60,0.3)`)
- Clear typography with links to safe pages

---

## Git Status

All files are staged and ready for commit:

```bash
$ git status

Changes to be committed:
  new file:   ADD-REVIEW-BANNERS.md
  modified:   emotional-safety-gap.html
  modified:   eq_safety_dashboard.html
  modified:   full-report.html
  modified:   research-summary.html
  modified:   robots.txt
```

---

## How to Complete Deployment

### Step 1: Commit Changes

**Note:** There's currently a `.git/index.lock` file that needs to clear. Wait a minute, then run:

```bash
git commit -m "$(cat <<'EOF'
Add 'Under Review' banners to research pages pending data verification

Protection measures for research pages with unverified data:
- Added warning banners to 4 research pages (eq_safety_dashboard.html, emotional-safety-gap.html, full-report.html, research-summary.html)
- Updated robots.txt to prevent search engine indexing of these pages
- Banners direct visitors to accurate pages (homepage, audit page)
- Added implementation documentation (ADD-REVIEW-BANNERS.md)

This prevents visitor confusion while correct data is being verified.
Once verified data is provided, banners can be removed per guide.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### Step 2: Push to Deploy

```bash
git push
```

### Step 3: Verify Deployment

After Netlify deploys (typically 1-2 minutes):

1. Visit https://ikwe.ai/eq_safety_dashboard.html
2. Confirm orange warning banner appears at top
3. Verify links to homepage and audit page work
4. Check other 3 research pages

---

## What This Achieves

**Immediate Protection:**
- ✅ Anyone landing on research pages sees clear warning
- ✅ Links to safe pages (homepage, audit) provided
- ✅ Prevents confusion/trust damage from incorrect data

**Search Engine Protection:**
- ✅ robots.txt prevents new indexing of these pages
- ✅ Existing indexed pages will show the warning banner

**Flexibility:**
- ✅ Pages still accessible (for your review)
- ✅ Easy to remove banners when data is verified
- ✅ No content loss

**Professionalism:**
- ✅ Shows you're careful about accuracy
- ✅ Better than having wrong data up
- ✅ Investors will respect this approach

---

## When to Remove Banners

**After:**
1. You provide correct dashboard numbers
2. All 4 research pages are updated with verified data
3. We verify accuracy together
4. You approve changes

**Then:**
```bash
# Remove banner HTML from each file (use Edit tool or manually)
# Remove robots.txt disallow rules
git add eq_safety_dashboard.html emotional-safety-gap.html full-report.html research-summary.html robots.txt
git commit -m "Remove 'Under Review' banners - research data verified

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
git push
```

---

## Troubleshooting

### If git lock persists:
```bash
# Wait for any background git processes to complete
# Then check if lock file still exists:
ls -la .git/index.lock

# If it's been more than 5 minutes with no git activity,
# you can manually remove it (requires proper permissions)
```

### If banners don't appear:
- Check browser cache (hard refresh: Cmd+Shift+R or Ctrl+F5)
- Verify Netlify deployment completed successfully
- Check browser console for any CSS/styling errors

### If you need to edit banner text:
- Banner HTML is inline-styled in each file
- Look for `<!-- UNDER REVIEW BANNER -->` comment
- Modify the `<p>` text between the `<strong>` tag and closing `</p>`

---

## Next Steps After This Deploys

### Immediate (Site is now safe to show):
1. ✅ Core site pages are accurate (index, audit, partner, enterprise)
2. ✅ Research pages have protection banners
3. ✅ No incorrect data will mislead visitors

### When Ready (After Data Verification):
1. Provide correct dashboard numbers
2. Update all research pages with verified data
3. Remove banners
4. Full site deployment-ready

---

## Files Protected

| File | Status | Banner Location |
|------|--------|----------------|
| `eq_safety_dashboard.html` | ⚠️ Protected | After `</nav>` line 1264 |
| `emotional-safety-gap.html` | ⚠️ Protected | After `<body>` line 318 |
| `full-report.html` | ⚠️ Protected | After `</nav>` line 759 |
| `research-summary.html` | ⚠️ Protected | After `</nav>` line 854 |
| `robots.txt` | ⚠️ Updated | Lines 8-11 (Disallow rules) |

---

## Summary

**What's staged:** 5 modified files + 1 new documentation file
**What it does:** Adds warning banners + prevents search indexing
**Time to deploy:** < 5 minutes (commit + push + Netlify)
**Risk level:** Minimal (only adds protection, doesn't remove content)
**Reversibility:** 100% (easy to remove banners later)

**Your site is now ready for the investor meetings with accurate core pages and protected research pages.**

---

**Ready to commit and push whenever the git lock clears.** 💙
