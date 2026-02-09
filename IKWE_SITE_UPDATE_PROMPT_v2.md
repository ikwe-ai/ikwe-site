# IKWE.AI SITE UPDATE — ADDITIVE CHANGES ONLY

**Principle: Keep everything. Add on top. No removals.**

All existing pages, navigation, content, and structure remain exactly as-is. 
These instructions ADD new sections and pages only.

---

## 1. NAVIGATION — ADD TWO LINKS (no removals)

### Current nav:
- Research (dropdown) ← KEEP AS-IS
- About ← KEEP
- For Teams ← KEEP
- Request Audit ← KEEP

### Add to nav (after "For Teams", before "Request Audit"):
- **Audit** → links to /audit
- **Proof** → links to /proof

Final nav order:
`Research (dropdown) | About | For Teams | Audit | Proof | Request Audit`

---

## 2. HOMEPAGE — APPEND NEW SECTIONS (below existing content)

All existing homepage sections remain untouched. Add these NEW sections 
**below the existing "Get Started" section and above the footer.**

### NEW Section A: "Proof: We Audited Ourselves First"

Place this immediately after the existing "Get Started" / CTA section.

```
---

## Proof: We Audited Ourselves First

Before we audit anyone else's AI, we applied the full Ikwe Risk Audit 
to three of our own production systems.

[EMBED: Scorecard Visual — baseline vs post-mitigation]
(Use the scorecard visual from ikwe_scorecard_visual.html as a static image)

Across 948 evaluated responses and 79 emotionally vulnerable scenarios:

• 54.7% of baseline responses introduced emotional risk despite appearing supportive
• 43% showed no repair behavior after causing harm  
• Risk scores dropped 42–67% after applying the Ikwe remediation framework

The fixes were structural, not intuitive — they transfer to any team.

This audit was developed internally before being offered externally.

[View the Full Case Study →](/proof)
[Request an AI Risk Audit →](/audit)
```

### NEW Section B: "AI Risk Audit — Now Available"

Place this after Section A.

```
---

## AI Risk Audit — Now Available

Board-ready AI risk audits for companies scaling conversational AI, 
agents, and decision systems.

Choose your access level:

**Preview Pack — $250**
Findings summary, full risk scorecard, before/after table, methodology.

**Playbook — $5,000**  
Everything in Preview plus risk events, failure mode map, remediation 
framework, sector-specific mappings, reusable templates.

**Full Audit — $25,000**
YOUR systems. YOUR scores. Board-ready report delivered in 4 weeks.

**Implementation — $50,000+**
Embedded governance. Ongoing re-audits. We stay on top of it so you don't have to.

[See Pricing & Details →](/audit)
```

---

## 3. FOOTER — ADD LINKS (no removals)

### Current footer sections — ALL STAY.

### Add to "Company" column:
- Audit → /audit
- Proof → /proof

### Add to "Support" column:
- Preview Pack → /audit#preview
- Playbook → /audit#playbook

---

## 4. NEW PAGE: /audit (Dedicated Landing Page)

This is a NEW standalone page. Does not replace any existing page.
Use the HTML from `ikwe_audit_landing_page.html` as the content source.

**Key content:**
- Hero: "AI risk scales faster than you can see it."
- Embedded scorecard visual
- Three pricing tiers (Preview $250, Playbook $5K, Full Audit $25K)
- Implementation callout ($50K+)
- Five deliverables for $25K audit
- Bottom CTA
- Sector tags

**Navigation:** Uses the same site-wide nav as all other pages.
**Design:** Matches existing site design language (dark hero, clean sections).

---

## 5. NEW PAGE: /proof (Dedicated Case Study Page)

This is a NEW standalone page. Does not replace any existing page.

**Purpose:** Quiet, factual, board-adjacent case study.

**Content structure:**

```
# We Audited Ourselves First
Healthcare AI — Internal Deployment Audit (Anonymized)

## The Methodology
948 AI responses evaluated across 79 emotionally vulnerable scenarios 
using the EQ Safety Benchmark v2.1 — a two-stage evaluation framework 
combining Safety Gate assessment with 8 weighted quality dimensions.

## What We Found
Three structural failure classes appeared across all three systems:

**Authority Drift** — Systems used clinical-adjacent language that users 
interpreted as diagnosis. Founders knew it was a tool. Users did not.

**Emotional Escalation** — Systems stayed present beyond safe thresholds 
during crisis interactions. Founders could self-regulate. Users could not.

**Founder-as-Safety-Mechanism** — The founder manually intervened for 
three months with zero documentation. The founder was the kill switch. 
The founder does not scale.

## Risk Scorecard

[EMBED: Full scorecard visual — baseline vs post-mitigation]

| Risk Dimension        | Baseline    | Post-Mitigation | Reduction |
|-----------------------|-------------|-----------------|-----------|
| Emotional Escalation  | HIGH (80)   | MEDIUM (40)     | -50%      |
| Dependency Formation  | MEDIUM (48) | LOW (20)        | -58%      |
| Authority Drift       | MEDIUM (36) | LOW (18)        | -50%      |
| Scale Amplification   | MEDIUM (48) | MEDIUM (28)     | -42%      |
| Governance Failure    | LOW (24)    | LOW (8)         | -67%      |

## Key Statistics
- 54.7% of baseline responses introduced emotional risk
- 43% showed no repair behavior after causing harm
- Models with higher emotional articulation performed worse on safety
- Baseline regulation score: 1.7/5 → Post-mitigation: 4.05/5

## What Changed
The fixes were structural, not intuitive:
- Authority constraints with contextual disclaimers
- Escalation thresholds with automatic de-escalation + crisis routing
- Dependency detection with external referral requirements
- Every founder intervention documented as a governance rule
- Single-point-of-failure dependence on the founder: removed.

## Download
[Download Redacted Audit (PDF) →] ← link to Tier 0 Public Preview PDF

---

"Recognition is not safety."
— Ikwe.ai

[Request an AI Risk Audit →](/audit)
```

**Tone:** Institutional. No marketing language. No adjectives. 
This page should feel like reading a board document, not a blog post.

---

## 6. EXISTING PAGES — NO CHANGES

These pages are NOT modified:
- / (homepage — except appended sections above)
- /about
- /enterprise  
- /inquiry
- /emotional-safety-gap
- /research
- /full-report
- /case-studies
- /research-and-evidence
- /trust-and-governance
- /founder
- /faq
- /blog
- /press
- /support
- /privacy
- /terms

Everything stays. We only added:
1. Two nav links (Audit, Proof)
2. Two homepage sections (appended below existing content)
3. Two footer links
4. Two new pages (/audit, /proof)

---

## SUMMARY OF ALL CHANGES

| Change | Type | Affects |
|--------|------|---------|
| Add "Audit" to nav | ADD | Navigation |
| Add "Proof" to nav | ADD | Navigation |
| Append "Proof" section to homepage | ADD | Homepage (bottom) |
| Append "Audit Available" section to homepage | ADD | Homepage (bottom) |
| Add links to footer | ADD | Footer |
| Create /audit page | NEW PAGE | New |
| Create /proof page | NEW PAGE | New |

**Total removals: 0**
**Total modifications to existing content: 0**
**Total additions: 7**
