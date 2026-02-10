# Ikwe.ai — Design System Deployment Guide

**Last updated:** 2026-02-09  
**Status:** Ready for implementation  

---

## What's in this package

| File | Purpose | Where it goes |
|------|---------|---------------|
| `ikwe-tokens-final.css` | Single source of truth for all colors, typography, spacing | Import first in every page's `<style>` or link as external stylesheet |
| `index-final.html` | Homepage (conversion-first architecture) | Replaces `index.html` in repo root |
| `audit-final.html` | Audit page (restructured for conversion) | Replaces `audit.html` in repo root |
| `scorecard-embed-final.html` | Scorecard component (warm dark) | Copy the `<style>` + `<div class="sc-card">` block into any dark-bg page |
| `scorecard-pdf-export.html` | Scorecard for PNG/PDF export | Open in browser → screenshot at 2x → canonical `scorecard_image.png` |
| `ikwe_site_full_audit.md` | Full repo audit with all findings | Reference doc for cleanup |

---

## Color rules (non-negotiable)

### Data viz colors — ONLY appear in:
- Scorecard bars and dimension dots
- Status badges (HIGH / MOD / LOW)
- Key statistics (like the 54.7% finding)
- Chart elements on any future data pages

### Data viz colors — NEVER appear on:
- Page backgrounds or section fills
- Body text or paragraph text
- Navigation elements
- CTA buttons
- Borders or dividers
- Hero glows or decorative gradients

### UI accent color:
- Dusty rose `#C4A69A` for kicker labels, active nav state, tier highlights, citation links
- This replaces the previous teal used for those elements

### CTA buttons:
- Primary: warm cream (#E8E4DF) fill, dark (#141218) text
- Secondary: ghost (transparent bg, border)
- NOT teal fill

---

## Audit page section order (canonical, locked)

1. **Hero** — urgency framing + primary CTA + preview download
2. **What You Get** — 3 outcome cards (Scorecard, Report, Action Plan)
3. **Sample Outputs** — 3 PDF download links (minimal row)
4. **Scorecard** — full interactive component
5. **Pricing Tiers** — 4 columns with Stripe links wired
6. **What Happens Next** — 4-week timeline (Week 1–4)
7. **Trust Strip** — single credibility line
8. **Final CTA** — catches scrollers

### Stripe payment links (wired in tier CTAs)

- Preview Pack ($250): `https://buy.stripe.com/fZudRa6UY85jaNw2Up9sk04`
- Playbook ($5,000): `https://buy.stripe.com/14A5kEbbeetH1cW66B9sk05`
- Full Audit ($25K): → `/inquiry` (high-touch, not self-serve)
- Enterprise ($50K+): → `/inquiry`

---

## CTA copy rules (non-negotiable)

| Context | Copy | Link |
|---------|------|------|
| Primary CTA (buttons) | Request an AI Risk Audit | `/inquiry` |
| Nav CTA | Request an Audit | `/inquiry` |
| Tier: Preview | Get Preview Pack | Stripe link |
| Tier: Playbook | Get Playbook | Stripe link |
| Tier: Full Audit | Request an AI Risk Audit | `/inquiry` |
| Tier: Enterprise | Request an AI Risk Audit | `/inquiry` |

**Do not rotate CTA language.** Consistency = trust.

---

## Homepage section order (canonical, locked)

1. **Hero** — consequence framing + 3 intent-matched CTAs
2. **Proof** — mini scorecard + bullets + "View full case study"
3. **Start Where You Are** — 4 router cards (Preview / Playbook / Audit / Research)
4. **Credibility Strip** — one line + methodology link
5. **Final CTA** — "If your AI interacts with people, you're carrying risk."

---

### Phase 1: Core files (30 min)

1. **Add `ikwe-tokens-final.css`** to your repo (e.g., `/css/tokens.css` or inline in each page)
2. **Replace `index.html`** with `index-final.html` (rename to `index.html`)
3. **Replace `audit.html`** with `audit-final.html` (rename to `audit.html`)
4. Test both pages locally

### Phase 2: Apply to remaining pages (1-2 hrs)

For each page (proof, research, about, enterprise, case-studies, etc.):

1. Copy the `<nav>` block from index-v2 (identical on all pages)
2. Copy the `<footer>` block from index-v2 (identical on all pages)
3. Update the page's CSS variables to match tokens:
   - `--bg: #141218` (was `#09090b`)
   - `--bg-2: #1a171f` (was `#0f1014`)
   - `--bg-card: #1e1b23` (was `#16181d`)
   - `--text: #E8E4DF` (was `#eaeaf0`)
   - All other values from tokens file
4. Change any teal kicker labels to `color: #C4A69A` (rose)
5. Change any teal CTA buttons to `background: #E8E4DF; color: #141218`
6. Set active nav link for current page: `class="active"` uses rose color

### Phase 3: Scorecard alignment (30 min)

Every page that shows the scorecard should use the same component:

1. **Site pages** (proof, audit): Use `scorecard-embed-final.html` markup
2. **PDFs**: Screenshot `scorecard-pdf-export.html` at 2x → replace all table/screenshot combos
3. **OG image**: Use the PDF export version cropped to 1200×630

This eliminates the drift where scorecard appears differently across contexts.

### Phase 4: PDF updates (1 hr)

For each PDF (Public Preview, Board Brief, Audit Report):

1. Replace any HTML-table scorecards with the canonical PNG
2. Replace any screenshot scorecards with the canonical PNG
3. Ensure headers use Fraunces, body uses DM Sans
4. Pull quotes: left border in muted teal (20-30% opacity), NOT solid neon
5. Page backgrounds: white or `#F8FAFC`, NOT dark

### Phase 5: Repo cleanup (from audit doc)

See `ikwe_site_full_audit.md` for the full list. Priority order:

1. Add `.gitignore` (node_modules, .DS_Store, *.zip)
2. Delete 8 zip archives from root
3. Delete timestamp folders
4. Consolidate PDFs to canonical names in `/downloads/`
5. Remove duplicate HTML pages (keep only canonical versions)
6. Remove superseded deployment docs

---

## Nav structure (canonical, all pages)

```
Research | Audit | Proof | About | [Request Audit]
```

- "Research" links to `/research`
- "Audit" links to `/audit`
- "Proof" links to `/proof`
- "About" links to `/about`
- CTA button links to `/inquiry`

Active state: `class="active"` on current page's link → displays in rose

---

## Footer structure (canonical, all pages)

```
[Brand + tagline + copyright]  |  Research col  |  Company col  |  Connect col
                               |  ─────────────────────────────────────────────
                               |  Citation line (full width)
```

Research: Emotional Safety Gap, Methodology, Full Report, Research Summary  
Company: About, Founder, Audit, Proof, Press Kit  
Connect: Request an Audit, Enterprise, stephanie@ikwe.ai, Privacy, Terms

Tagline: "Behavioral emotional safety infrastructure for AI."  
Copyright: © 2026 Visible Healing Inc. / Des Moines, Iowa

---

## Typography rules

| Context | Font | Weight | Size |
|---------|------|--------|------|
| Page title (h1) | Fraunces | 600 | clamp(2.1rem, 4.2vw, 3.2rem) |
| Section title (h2) | Fraunces | 600 | clamp(1.25rem, 2.4vw, 1.65rem) |
| Kicker label | Space Mono | 700 | 11px, uppercase, 0.1em tracking |
| Body text | DM Sans | 400 | 1.05rem, line-height 1.75 |
| Nav links | DM Sans | 500 | .875rem |
| Scorecard data | Space Mono | 700 | 12.5px |
| Badge pills | DM Sans | 700 | 10px, uppercase |

---

## What NOT to change

- The scorecard data values (these come from actual research)
- The five risk dimensions and their assigned colors
- The status thresholds (High ≥60, Mod 30-59, Low <30)
- The quadrant mark (conic gradient of coral/lilac/navy/teal)
- The Fraunces + DM Sans + Space Mono font stack
- The research content on any page
