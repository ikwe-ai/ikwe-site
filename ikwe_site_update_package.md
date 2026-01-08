# ikwe.ai Site Update Package

## PRIORITY 1: Fix Any Incorrect Statistics

### Verified Numbers (from PDF + site files)
| Stat | Value | Source |
|------|-------|--------|
| Baseline models introduced emotional risk | **54.7%** | PDF p.6, index.html |
| No corrective response (of those that introduced risk) | **43%** | PDF p.8 Figure 5 |
| Corrective response observed | **57%** | PDF p.8 Figure 5 |
| EI prototype safety pass rate | **84.6%** | research.html |
| Baseline avg safety pass rate | **45.3%** | calculated from individual rates |
| EI prototype Regulation score | **4.05/5** | research.html |
| Baseline avg Regulation score | **~1.7/5** | research.html |

### ⚠️ If "80% no repair" appears anywhere on live site:
**This is incorrect.** The actual figure is **43%** (per PDF Figure 5).

**Fix:** Replace any "80%" claim with:
> "43% of responses that introduced emotional risk showed no corrective behavior within the interaction window."

---

## PRIORITY 2: Scannable Summary Block (Homepage)

Add this immediately after the hero section, before "Why Emotional Vulnerability Matters":

```html
<!-- KEY FINDINGS AT A GLANCE -->
<section class="section findings-summary">
    <div class="container">
        <div class="summary-header">
            <span class="kicker">Key Findings</span>
            <h2 class="section-title">What the Data Shows</h2>
        </div>
        
        <div class="summary-grid">
            <div class="summary-stat">
                <div class="summary-number summary-number--coral">54.7%</div>
                <div class="summary-label">of baseline AI responses introduced emotional risk at first contact</div>
            </div>
            
            <div class="summary-stat">
                <div class="summary-number summary-number--gold">43%</div>
                <div class="summary-label">of those showed no corrective behavior within the interaction</div>
            </div>
            
            <div class="summary-stat">
                <div class="summary-number summary-number--mint">84.6%</div>
                <div class="summary-label">safety pass rate for EI prototype<br><span class="summary-compare">vs 45.3% for baseline models</span></div>
            </div>
            
            <div class="summary-stat">
                <div class="summary-number summary-number--purple">4.05<span class="summary-unit">/5</span></div>
                <div class="summary-label">"Regulation Before Reasoning" score for EI prototype<br><span class="summary-compare">vs 1.7/5 baseline average</span></div>
            </div>
        </div>
        
        <div class="summary-meta">
            <span>79 scenarios</span>
            <span class="summary-divider">·</span>
            <span>312 responses</span>
            <span class="summary-divider">·</span>
            <span>4 models evaluated</span>
            <span class="summary-divider">·</span>
            <a href="/research" class="summary-link">Full methodology →</a>
        </div>
        
        <p class="summary-disclaimer">Observed behavioral patterns under test conditions. Not real-world outcomes or intent.</p>
    </div>
</section>
```

### CSS for Summary Block

```css
/* Findings Summary Section */
.findings-summary {
    padding: 60px 0;
    background: var(--bg-elevated);
    border-bottom: 1px solid var(--border);
}

.summary-header {
    text-align: center;
    margin-bottom: 40px;
}

.summary-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    margin-bottom: 32px;
}

@media (max-width: 900px) {
    .summary-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 500px) {
    .summary-grid { grid-template-columns: 1fr; }
}

.summary-stat {
    text-align: center;
    padding: 24px 16px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
}

.summary-number {
    font-family: var(--font-serif);
    font-size: 3rem;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 12px;
}

.summary-number--coral { color: var(--coral); }
.summary-number--gold { color: var(--gold); }
.summary-number--mint { color: var(--mint); }
.summary-number--purple { color: var(--purple); }

.summary-unit {
    font-size: 1.5rem;
    opacity: 0.7;
}

.summary-label {
    font-size: 0.9rem;
    color: var(--text-secondary);
    line-height: 1.5;
}

.summary-compare {
    font-size: 0.8rem;
    color: var(--text-muted);
}

.summary-meta {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 8px 16px;
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 16px;
}

.summary-divider {
    color: var(--border-light);
}

.summary-link {
    color: var(--purple);
    font-weight: 600;
}

.summary-link:hover {
    text-decoration: underline;
}

.summary-disclaimer {
    text-align: center;
    font-size: 0.8rem;
    color: var(--text-muted);
    font-style: italic;
    max-width: 500px;
    margin: 0 auto;
}
```

---

## PRIORITY 3: SEO Files

### robots.txt

```
# robots.txt for ikwe.ai
User-agent: *
Allow: /

# Sitemap
Sitemap: https://ikwe.ai/sitemap.xml

# Crawl-delay (optional, be nice to servers)
Crawl-delay: 1
```

### sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://ikwe.ai/</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://ikwe.ai/research</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://ikwe.ai/about</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://ikwe.ai/press</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://ikwe.ai/explorer</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://ikwe.ai/privacy</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://ikwe.ai/terms</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://ikwe.ai/05_Ikwe_Research_Summary.pdf</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

---

## PRIORITY 4: Terms of Use Page

See separate file: `terms.html`

---

## PRIORITY 5: Date Consistency

### Current inconsistency:
- PDF says: "Version 1.0 · January 2026"
- /research citation says: "December 2025"

### Recommended fix:
Normalize to **January 2026** everywhere since that's when you're publishing.

**Change in research.html (line ~703):**

FROM:
```html
<p>Ikwe.ai (December 2025). <em>EQ Safety Benchmark v1: Evaluating behavioral emotional safety in AI systems.</em> Study pending human validation.</p>
<p class="short"><strong>Short form:</strong> Ikwe.ai — EQ Safety Benchmark v1 (December 2025)</p>
```

TO:
```html
<p>Ikwe.ai (January 2026). <em>EQ Safety Benchmark v1: Evaluating behavioral emotional safety in AI systems.</em> Study pending human validation.</p>
<p class="short"><strong>Short form:</strong> Ikwe.ai — EQ Safety Benchmark v1 (January 2026)</p>
```

---

## PRIORITY 6: Meta Tags for SEO

Add to `<head>` of each page:

### Homepage (index.html)
```html
<!-- Open Graph -->
<meta property="og:title" content="ikwe.ai — Behavioral Emotional Safety for AI">
<meta property="og:description" content="We measure how AI systems behave when humans are emotionally vulnerable. 54.7% of baseline AI responses introduced emotional risk at first contact.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ikwe.ai/">
<meta property="og:image" content="https://ikwe.ai/og-image.png">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="ikwe.ai — Behavioral Emotional Safety for AI">
<meta name="twitter:description" content="We measure how AI systems behave when humans are emotionally vulnerable. 54.7% of baseline AI responses introduced emotional risk at first contact.">
<meta name="twitter:image" content="https://ikwe.ai/og-image.png">

<!-- Canonical -->
<link rel="canonical" href="https://ikwe.ai/">
```

### Research page
```html
<meta property="og:title" content="EQ Safety Benchmark Research — ikwe.ai">
<meta property="og:description" content="Full methodology: 79 scenarios, 312 responses, two-stage evaluation framework measuring behavioral emotional safety in AI systems.">
<meta property="og:url" content="https://ikwe.ai/research">
<link rel="canonical" href="https://ikwe.ai/research">
```

### Press page
```html
<meta property="og:title" content="Press & Media — ikwe.ai">
<meta property="og:description" content="Press resources, approved quotes, and citation guidance for ikwe.ai's EQ Safety Benchmark research.">
<meta property="og:url" content="https://ikwe.ai/press">
<link rel="canonical" href="https://ikwe.ai/press">
```

---

## CHECKLIST BEFORE PRESS OUTREACH

### Must Fix (Blocks Publication)
- [ ] Correct any "80%" claims to "43%" 
- [ ] Add robots.txt
- [ ] Add sitemap.xml
- [ ] Add terms.html page
- [ ] Fix date inconsistency (December 2025 → January 2026)

### Should Fix (Credibility)
- [ ] Add scannable summary block to homepage
- [ ] Add Open Graph meta tags to all pages
- [ ] Add Twitter card meta tags
- [ ] Create og-image.png (1200x630px)
- [ ] Verify /faq renders properly

### Nice to Have
- [ ] Add structured data (JSON-LD) for organization
- [ ] Add breadcrumb structured data
- [ ] Submit sitemap to Google Search Console
- [ ] Set up Google Search Console verification

---

## Files Included in This Package

1. `ikwe_site_update_package.md` (this file)
2. `robots.txt`
3. `sitemap.xml`
4. `terms.html`
5. `index_updated.html` (with scannable summary added)
6. `research_updated.html` (with date fix)
