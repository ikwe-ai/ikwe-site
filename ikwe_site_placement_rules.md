# Ikwe.ai — PDF Download Placement Rules
## Where Each Document Lives, Links, and Shows Up

---

## Three Public PDFs

| PDF | Pages | Purpose | Filename |
|-----|-------|---------|----------|
| **System Blueprint Preview** | 4 | Free lead magnet — shows findings + tiered paywall | `ikwe_public_preview.pdf` |
| **Board Brief** | 3 | Sales sample — condensed scorecard + CTA | `ikwe_board_brief.pdf` |
| **Audit Report** | 7 | Full sample output — complete redacted audit | `ikwe_audit_report.pdf` |

---

## Site Placement Map

### 1. Homepage (`/` or `/index.html`)

**System Blueprint Preview PDF** — primary download
- Hero section: "View a Completed Audit (Redacted)" button → downloads `ikwe_public_preview.pdf`
- This is the free lead magnet. No gate. Immediate download.
- Also shown: OG hero image (`og_image.png`) in the hero/social preview

**Board Brief PDF** — secondary reference
- NOT directly linked from homepage
- Used in OG meta tags if sharing the audit page specifically

### 2. Audit Page (`/audit` or `/ikwe_audit_page.html`)

**All three PDFs** — tiered access display

| Section | PDF | Action |
|---------|-----|--------|
| "See What an Audit Looks Like" | System Blueprint Preview | Direct download button |
| "Sample Board Brief" | Board Brief | Direct download button |
| "Full Sample Report (Redacted)" | Audit Report | Direct download button |
| Tier pricing table | — | Links to Stripe checkout |

Layout:
```
[Download System Blueprint Preview — Free]     ← ikwe_public_preview.pdf
[Download Board Brief — Free]        ← ikwe_board_brief.pdf  
[Download Full Sample Report — Free] ← ikwe_audit_report.pdf
[Request YOUR Audit — $2,500+]         ← Stripe / inquiry form
```

### 3. Proof Page (`/proof` or `/ikwe_proof_page.html`)

**Audit Report PDF** — evidence artifact
- "View the Full Sample Audit" → downloads `ikwe_audit_report.pdf`
- Scorecard visual (`scorecard_image.png`) displayed inline
- This page is about proving the methodology works

### 4. Research Page (`/research` or `/research.html`)

**System Blueprint Preview PDF** — methodology reference
- "View Sample Audit Output" link in methodology section → `ikwe_public_preview.pdf`
- The emotional-safety-gap research content lives here as HTML, not as a PDF download

### 5. Playbook Page (`/playbook` or `/ikwe_playbook_page.html`)

**Board Brief PDF** — quick reference
- "See a Sample Board Brief" → downloads `ikwe_board_brief.pdf`
- This is the consulting/implementation pitch page

### 6. Preview Page (`/preview` or `/ikwe_preview_page.html`)

**System Blueprint Preview PDF** — the main artifact
- This page IS the preview, so the PDF is the primary download
- "Download This Preview" → `ikwe_public_preview.pdf`
- Tier upgrade CTAs link to `/audit` page

---

## Download Path Rules

```
/downloads/ikwe_public_preview.pdf    ← Free, ungated
/downloads/ikwe_board_brief.pdf       ← Free, ungated  
/downloads/ikwe_audit_report.pdf      ← Free, ungated (sample)
```

All three are public sample/redacted outputs. No gate required.
The paywall is on the REAL audit, not the samples.

---

## CTA Routing Rules

| User sees... | They click... | They go to... |
|---|---|---|
| Free preview PDF | "Download Preview" | `/downloads/ikwe_public_preview.pdf` |
| Free board brief | "Download Brief" | `/downloads/ikwe_board_brief.pdf` |
| Free full sample | "Download Sample Report" | `/downloads/ikwe_audit_report.pdf` |
| System Blueprint ($2,500) | "Get System Blueprint" | Stripe checkout or `/audit` inquiry |
| Playbook ($5,000) | "Get Playbook" | Stripe checkout or `/audit` inquiry |
| Full Audit ($25,000) | "Request Audit" | `/inquiry.html` or Stripe |
| Implementation ($50K+) | "Contact Us" | `stephanie@ikwe.ai` or `/inquiry.html` |

---

## Image Placement

| Image | Where it goes |
|-------|--------------|
| `og_image.png` | Homepage hero, social OG tags, LinkedIn preview |
| `scorecard_image.png` | Proof page inline, Audit page inline, social proof |
| `ikwe-logo.png` | All PDF covers, site header (already in place) |

---

## Classification Rules

- **No PDF should say "Board Confidential"** — all public documents use "Sample — Redacted" or "System Blueprint Preview"
- Internal-only documents (actual client audits) use "Board Confidential" — these are never on the site
- The distinction: sample/demo = public, real client work = confidential

---

## Quick Reference: Which PDF for Which Audience

| Audience | Give them... | PDF |
|----------|-------------|-----|
| Cold lead (LinkedIn, X, email) | System Blueprint Preview | `ikwe_public_preview.pdf` |
| Warm lead (after first call) | Board Brief | `ikwe_board_brief.pdf` |
| Evaluating purchase | Full Sample Report | `ikwe_audit_report.pdf` |
| Board member / decision maker | Board Brief | `ikwe_board_brief.pdf` |
| Technical evaluator | Full Sample Report | `ikwe_audit_report.pdf` |
| Investor / advisor | Board Brief + Preview | Both |
