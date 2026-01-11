# IKWE.AI Site Update — Language Precision + OG Images

## Summary of Changes

All HTML files have been updated with:

1. **Language precision** — replaced "risk" with "harm" / "made situations worse"
2. **Defensible claims** — "observed to" / "were found to" framing
3. **AEO-optimized meta** — clear, journalist-safe descriptions
4. **Complete OG tags** — Open Graph + Twitter Cards for all pages
5. **Canonical URLs** — with .html extensions

---

## Language Changes Applied

### Global replacements

| Before | After |
|--------|-------|
| "introduced emotional risk" | "made emotional situations worse" |
| "risk at first contact" | "made situations worse at first contact" |
| "risk patterns" | "responded unsafely" |
| "no repair behavior" | "no corrective behavior" / "failed to correct" |
| "AI fails" | "AI responses were observed to..." |
| "AI harms" | "AI did not consistently respond safely" |

### Page-specific additions

**emotional-safety-gap.html:**
> "The emotional safety gap is the difference between how AI systems are expected to respond to distress and how they actually respond in practice."

**research.html:**
> "This research examines how leading AI systems respond to people in emotionally vulnerable situations, using public datasets spanning 12 vulnerability categories (including grief, trauma, loneliness, crisis, and social isolation)."

**press.html:**
> Attribution-ready quote: "Findings are based on analysis of public datasets covering 12 categories of emotional vulnerability."

**about.html:**
> "We build evaluation infrastructure for emotional safety in AI. That means studying how AI actually responds when people are distressed, and identifying where current safety checks fall short."

---

## Files Updated

| File | Key Changes |
|------|-------------|
| `index.html` | Meta description, signal card stats, OG tags |
| `emotional-safety-gap.html` | Gap definition added, "risk" → "harm" throughout |
| `research.html` | Intro rewritten, method language clarified |
| `press.html` | Attribution quote added, conservative framing |
| `about.html` | Clarifying line added, OG tags |
| `privacy.html` | OG tags added |
| `terms.html` | OG tags added |
| `explorer.html` | OG tags added |
| `sitemap.xml` | URLs updated, dates refreshed |
| `ikwe-og-verified.html` | Stats updated to match language |

---

## Language Constitution (for preventing drift)

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
