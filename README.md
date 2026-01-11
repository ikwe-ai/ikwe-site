# IKWE.AI Site Update — Complete Package

## Complete Site Map

### HTML Pages (all updated)

| File | Purpose | OG Image |
|------|---------|----------|
| `index.html` | Homepage | ikwe-default.png |
| `emotional-safety-gap.html` | Key findings | ikwe-gap.png |
| `research.html` | Research overview | ikwe-research.png |
| `about.html` | About page | ikwe-about.png |
| `press.html` | Press kit | ikwe-press.png |
| `inquiry.html` | **NEW** - Contact/Access form | ikwe-default.png |
| `explorer.html` | Scenario explorer | ikwe-research.png |
| `privacy.html` | Privacy policy | ikwe-default.png |
| `terms.html` | Terms of service | ikwe-default.png |

### Supporting Files

| File | Purpose |
|------|---------|
| `sitemap.xml` | Updated sitemap with all pages |
| `ikwe-og-verified.html` | Screenshot to generate OG images |

### Assets Needed (verify these exist in your repo)

| File | Purpose |
|------|---------|
| `ikwe_logo_dark.png` | Site logo |
| `ikwe_logo_light.png` | Light logo variant |
| `/og/ikwe-default.png` | Default OG image |
| `/og/ikwe-research.png` | Research page OG |
| `/og/ikwe-gap.png` | Findings page OG |
| `/og/ikwe-press.png` | Press page OG |
| `/og/ikwe-about.png` | About page OG |

---

## Fixes Applied in This Update

### 1. Icon sizing (emotional-safety-gap.html)
Warning triangle icons now constrained to 16×16px

### 2. Email display (all pages)
All emails now show as `research@ikwe.ai` with proper mailto links

### 3. Contact/Access forms (all pages)
- Nav "Contact" links now go to `inquiry.html`
- Access modals use JotForm iframe: `https://form.jotform.com/260067967050055`

### 4. New inquiry.html page
Standalone page with embedded JotForm for access requests

### 5. Language precision (all pages)
- "risk" → "made situations worse" / "harm"
- "patterns" → "behaviors"
- Added defensible framing throughout

---

## Language Constitution

### Prefer these phrases:
- "emotionally vulnerable situations"
- "public datasets"
- "made emotional situations worse"
- "failed to acknowledge or correct"
- "responded unsafely"
- "were observed to increase emotional distress"

### Avoid (unless carefully defined):
- "risk" (too abstract)
- "patterns" (sounds speculative)
- "evaluation" without explanation
- "safety failure" (too accusatory)
- "AI fails" / "AI harms" (intent implied)

---

## To Deploy

1. **Generate OG Images:**
   - Open `ikwe-og-verified.html` in Chrome
   - Screenshot each `.og-image` section
   - Save to `/og/` folder

2. **Replace HTML Files:**
   - Upload all HTML files to your repo
   - Ensure `/og/` folder contains the PNG images

3. **Deploy & Cache Bust:**
   - Push to production
   - Force refresh at validators:
     - https://cards-dev.twitter.com/validator
     - https://www.linkedin.com/post-inspector/
     - https://developers.facebook.com/tools/debug/

4. **Verify:**
   - Test at https://metatags.io
   - Test at https://opengraph.xyz

---

## Verified Statistics

All stats verified against research documentation:

| Stat | Value | Plain-English Version |
|------|-------|----------------------|
| First-contact harm | 54.7% | "made emotional situations worse" |
| No correction | 43% | "failed to correct after distress" |
| Categories | 12 | "vulnerability categories" |
| Datasets | 8 | "public datasets" |
| Systems | 4 | "AI systems evaluated" |
| Regulation score | 1.7/5 | "avg regulation score for baseline models" |
