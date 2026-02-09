# IKWE.AI SITE UPDATE — IMPLEMENTATION PROMPT

Use this prompt to update ikwe.ai. It is based on the current live site structure (fetched February 9, 2026) and specifies exact changes.

---

## CRITICAL CHANGES — SITE IDENTITY SHIFT

The site currently reads as a **research organization explaining emotional safety theory**.
It needs to read as a **risk infrastructure company selling a product**.

### What to REMOVE from the homepage:

- The entire "AI Safety Pyramid" section (Policy/Compliance/Crisis framework graphic)
- The "ΔT" interaction timeline visualization
- The "Concrete capabilities teams can deploy" section
- The "Deployment Model" section
- The "Trust & Governance" overview section
- The Origin/founder narrative section
- Excessive navigation links (Research dropdown with 6+ items)

### What to KEEP (edited):

- Hero section (rewritten — see below)
- "Who This Is For" (tightened — see below)
- "How Ikwe Works" (restructured as deliverables — see below)
- CTA (simplified)

---

## NEW HOMEPAGE STRUCTURE (5 sections max)

### Section 1 — Hero

```
IKWE.AI

AI risk scales faster than you can see it.
Ikwe catches it before it costs you.

Board-ready AI risk audits for companies scaling
conversational AI, agents, and decision systems.

[Request an AI Risk Audit]
```

**Design notes:**
- Dark background (use existing #1A1A2E)
- One sentence tagline, not a paragraph
- Single CTA button → links to /inquiry or mailto
- NO secondary CTA. No "View Evidence Pack."

---

### Section 2 — Proof (The Scorecard Visual)

Place the Before/After scorecard image here. One image. No scrolling.

Below it:

```
Before we audit anyone else's AI, we audited our own.

Across three production AI systems and 948 evaluated responses:

• 54.7% of baseline responses introduced emotional risk
• 43% showed no repair after causing harm
• Risk scores dropped 42–67% after applying Ikwe

The fixes were structural, not intuitive — they transfer to any team.
```

**Design notes:**
- White background
- Image should be the scorecard visual (ikwe_scorecard_visual.html screenshot)
- Three bullet points only
- End with the transfer line — it sells the audit

---

### Section 3 — What You Get

Replace the current "Three layers of safety infrastructure" with:

```
What the $25,000 AI Risk Audit Delivers

1. Board-Ready Risk Report
   Defensible documentation for boards, investors, and regulators.

2. AI Safety Scorecard
   Red/Yellow/Green across five core risk dimensions.

3. Failure Mode Map
   Evidence-backed risk events with triggers, scale effects, and consequences.

4. Audit Trail
   What was reviewed, how conclusions were reached, proof of diligence.

5. Priority Action Plan
   NOW / NEXT / LATER — clear guidance, no ambiguity.

Delivered in 4 weeks. No disruption. No slowdown.

[Request an AI Risk Audit]
```

**Design notes:**
- Clean numbered list, not framework diagrams
- Each item: bold title + one-line description
- This IS the sales page content, condensed for the homepage

---

### Section 4 — Who This Is For

Tighten the current list to:

```
Built for AI companies scaling faster than their safeguards.

→ Post-seed / post-YC / pre-Series B startups
→ Teams shipping conversational AI, agents, therapy, or education systems
→ Companies preparing for diligence, platform review, or regulatory scrutiny
→ Anyone whose AI influences human decisions, emotions, or behavior at scale
```

Remove: Insurance & risk partners, Policy & research institutions (those are enterprise — not homepage)

---

### Section 5 — CTA (Bottom)

```
Fast AI companies don't fail because they move quickly.
They fail because risk scales faster than control.

[Request an AI Risk Audit]

Limited engagements per quarter.

Healthcare · Policy & Gov · LLM & Agents · Workplace & HR · Consumer
```

---

## NAVIGATION — SIMPLIFY

### Current nav (too many items):
- Research (dropdown with 6 links)
- About
- For Teams
- Request Audit

### New nav:
- Audit (→ /audit sales page)
- Proof (→ /proof case study)
- About (→ /about, rewritten)
- Request Audit (→ /inquiry, primary CTA button style)

Remove the Research dropdown entirely from main nav. Research pages can still exist but are not primary navigation.

---

## PAGE: /audit (Sales Page)

Replace current /enterprise page content with the full $25K audit sales page.
Use the HTML from `ikwe_25k_audit_sales_page.html` as the content source.

Key copy points to preserve exactly:
- "Scale your AI — without scaling the risk that can take you down."
- "Founders are structurally constrained by proximity, incentives, and cognitive load."
- The 54.7% / 43% stats
- The before/after table
- The pricing: $25,000
- Timeline: 4 weeks
- CTA: "Request an AI Risk Audit (Limited engagements per quarter)"

---

## PAGE: /proof (Case Study)

New page. Contains:
- The redacted self-audit summary
- The scorecard visual
- The before/after table
- Download link for the redacted PDF
- Brief methodology note

Tone: quiet, factual, board-adjacent. Not a blog post. Not thought leadership.

---

## PAGE: /about (Rewritten)

Current about page is too narrative/personal. Replace with:

```
About Ikwe

Ikwe.ai builds behavioral emotional safety infrastructure for conversational AI.

We evaluate how AI systems behave when interacting with emotionally vulnerable
users — not what they say, but what they do when it matters.

Our research across 948 AI responses found that 54.7% introduced emotional risk
despite appearing supportive. Recognition is not safety.

Ikwe exists to close the gap between what AI systems recognize and how they behave.

---

Founded by Stephanie Stranko
Iowa-based researcher and technologist working at the intersection of emotional
intelligence, AI systems, and human safety. Background in product development,
operations, and behavioral analysis. Built Ikwe from direct exposure to system
failure in emotionally sensitive AI contexts.

Visible Healing Inc. · Des Moines, Iowa
```

6-8 lines for founder bio. Professional. No life story.

---

## PAGE: /inquiry (Contact/Request)

Keep simple. Form or mailto. Fields:
- Name
- Company
- AI system type (dropdown: Conversational AI / Agent / Decision System / Other)
- Brief description
- Submit → "Request Audit"

---

## PAGES TO KEEP BUT DEPRIORITIZE

These pages can still exist but should NOT be in primary navigation:
- /research (methodology)
- /full-report
- /emotional-safety-gap
- /case-studies
- /research-and-evidence
- /trust-and-governance

They serve SEO and deep-link purposes. They are not sales pages.

---

## FOOTER — SIMPLIFY

### Current footer (too many links):
Research (3 links), Company (5 links), Support (2 links), Connect (3 links)

### New footer:
```
ikwe.ai
Behavioral emotional safety infrastructure for AI.
© 2026 Visible Healing Inc. · Des Moines, Iowa

Audit  ·  Proof  ·  About  ·  Research  ·  Contact  ·  Privacy  ·  Terms
```

One line of links. That's it.

---

## VISUAL SYSTEM NOTES

### Keep:
- Current dark color palette (#1A1A2E primary)
- Teal accent (#16697A)
- Current logo treatment
- Clean sans-serif typography

### Change:
- Remove all abstract framework diagrams
- Remove the ΔT timeline visualization
- Remove the safety pyramid graphic
- Only show visuals that represent paid output (the scorecard)

### Rule: If it's not something a client receives, it doesn't go on the site.

---

## STRIPE PRODUCTS TO CREATE

### Product 1: Ikwe AI Risk Audit
- Price: $25,000 (one-time)
- Description: Board-ready AI risk audit including safety scorecard, failure mode map, observed risk events, audit trail, and priority action plan. Delivered in 4 weeks.
- Metadata: tier=standard, delivery=4weeks

### Product 2: Ikwe Enterprise AI Risk Audit
- Price: Custom ($50,000-$75,000)
- Description: Multi-system, cross-sector AI risk audit for enterprise environments. Includes all standard deliverables plus cross-system risk correlation and regulatory mapping.
- DO NOT publish price. Inquiry only.
- Metadata: tier=enterprise, delivery=6-8weeks

### Product 3: Ikwe Quarterly Re-Audit
- Price: $15,000/quarter
- Description: Quarterly risk reassessment with updated scorecard, delta analysis, and remediation tracking. Available after initial audit.
- Sold as upsell only. Not on public pricing page.
- Metadata: tier=recurring, delivery=2weeks

### What NOT to create in Stripe yet:
- Template downloads
- Framework licenses
- Subscription products
- Tool access

Clarity beats leverage right now.

---

## IMPLEMENTATION ORDER

1. Update homepage (hero + proof + deliverables + who + CTA)
2. Create /audit page with sales page content
3. Create /proof page with redacted case study
4. Rewrite /about
5. Simplify navigation
6. Simplify footer
7. Create Stripe products
8. Connect /inquiry form to email
9. Screenshot scorecard visual and place on homepage
10. Remove framework graphics

---

## THE TEST

When someone lands on ikwe.ai, within 5 seconds they should know:
1. What Ikwe does (AI risk audits)
2. That it's real (scorecard visual with actual numbers)
3. What to do next (Request an Audit)

Everything else is secondary.
