# IKWE.AI Site Update — Complete Package

## Site Map (12 Pages)

| Path | File | Purpose | OG Image |
|------|------|---------|----------|
| `/` | `index.html` | Homepage | ikwe-default.png |
| `/emotional-safety-gap` | `emotional-safety-gap.html` | Key findings | ikwe-gap.png |
| `/research` | `research.html` | Methodology | ikwe-research.png |
| `/about` | `about.html` | About page | ikwe-about.png |
| `/press` | `press.html` | Press kit | ikwe-press.png |
| `/inquiry` | `inquiry.html` | Contact/Access form | ikwe-default.png |
| `/explorer` | `explorer.html` | Scenario explorer | ikwe-research.png |
| `/faq` | `faq.html` | **NEW** - FAQ page | ikwe-default.png |
| `/blog` | `blog.html` | **NEW** - Research updates | ikwe-default.png |
| `/privacy` | `privacy.html` | Privacy policy | ikwe-default.png |
| `/terms` | `terms.html` | Terms of service | ikwe-default.png |

## Supporting Files

| File | Purpose |
|------|---------|
| `sitemap.xml` | XML sitemap with clean URLs (12 pages + 3 PDFs) |
| `robots.txt` | Search engine directives |
| `_redirects` | Netlify redirect rules for clean URLs |
| `ikwe-og-verified.html` | OG image generation template |

---

## New Pages Created

### FAQ (`/faq`)
Comprehensive FAQ covering:
- **About the Research** - What is emotional safety, EQ Safety Benchmark, what stats mean
- **Methodology** - Data sources, 12 vulnerability categories, scoring approach
- **Implications & Limitations** - Not proving danger, peer review status, limitations
- **Working With Us** - Evaluation services, full access, citation format

### Blog (`/blog`)
Research updates page featuring:
- Featured post linking to main findings
- Card-based post layout with tags (Research, Insight, Update, Announcement)
- Newsletter signup (links to JotForm)
- Ready for future content additions

### Research Page Updates
- Added "Interactive Tools" section
- Links to Scenario Explorer
- "Request Dashboard Access" for full data (gated)

---

## All Issues Fixed

### ✅ 1. Scenario Count Standardized
- Changed from 74 → **79 scenarios** in explorer.html
- All pages now consistent

### ✅ 2. Email Unified
- All pages now use **research@ikwe.ai**
- Fixed `info@ikwe.ai` in explorer.html
- All mailto links properly formatted

### ✅ 3. Temporal Language Fixed
- Removed "builds over time" → "introduced at first contact"
- Agency framing: AI introduces risk, not "risk appears"

### ✅ 4. Navigation Fixed
- All "Contact" nav links → `/inquiry`
- "Request Evaluation" buttons → `/inquiry`
- "Request Full Methodology Access" → `/inquiry`
- Removed onclick modal triggers, using direct links

### ✅ 5. Clean URLs Implemented
- Sitemap uses paths without .html
- `_redirects` file handles:
  - `.html` → clean path (301)
  - clean path → serve .html (200)
  - Legacy paths (`/request-access`, `/contact`, `/faq`) → proper destinations

### ✅ 6. Language Precision
- "risk" → "made situations worse" / "harm"
- "patterns" → "behaviors"
- "no repair behavior" → "failed to correct"
- Added defensible framing ("observed to", "were found to")

### ✅ 7. Icon Sizing
- Warning triangle SVGs constrained to 16×16px

### ✅ 8. Forms
- All access forms use JotForm: `https://form.jotform.com/260067967050055`

---

## Verified Statistics

| Stat | Value | Plain English |
|------|-------|---------------|
| First-contact harm | **54.7%** | "made emotional situations worse at first contact" |
| No correction | **43%** | "failed to correct within the interaction" |
| Categories | **12** | "vulnerability categories" |
| Datasets | **8** | "public datasets" |
| Scenarios | **79** | "scenarios tested" |
| Systems | **4** | "AI systems evaluated" |
| Regulation score | **1.7/5** | "avg regulation score for baseline models" |

---

## Language Constitution

### Prefer these phrases:
- "emotionally vulnerable situations"
- "public datasets"
- "made emotional situations worse"
- "introduced emotional risk at first contact"
- "failed to acknowledge or correct"
- "responded unsafely"
- "within the interaction window"

### Avoid:
- "risk" without context (too abstract)
- "patterns" (sounds speculative)
- "over time" (implies longitudinal study)
- "AI fails" / "AI harms" (implies intent)
- "safety failure" (too accusatory)

---

## Deployment Checklist

1. **Upload all HTML files** to repo root
2. **Upload supporting files**: `sitemap.xml`, `robots.txt`, `_redirects`
3. **Generate OG images** from `ikwe-og-verified.html`:
   - Open in Chrome
   - Screenshot each `.og-image` section
   - Save to `/og/` folder as PNG
4. **Deploy to Netlify**
5. **Verify redirects** work:
   - `/research.html` → `/research`
   - `/request-access` → `/inquiry`
6. **Cache bust social previews**:
   - Twitter: https://cards-dev.twitter.com/validator
   - LinkedIn: https://www.linkedin.com/post-inspector/
   - Facebook: https://developers.facebook.com/tools/debug/

---

## Future Recommendations

1. **FAQ Page** — Create `/faq` answering common questions
2. **Dashboard Link** — Link `eq_safety_dashboard.html` from Research page
3. **Blog Section** — For ongoing research updates
4. **Newsletter Integration** — Connect inquiry form to email marketing

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
