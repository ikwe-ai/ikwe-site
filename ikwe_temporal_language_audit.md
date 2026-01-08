# ikwe.ai Temporal Language Audit

## The Problem

The site currently uses "over time" language that implies longitudinal tracking across sessions or days. What you're actually measuring is behavioral stability **within the interaction window**—how the AI responds as emotional vulnerability deepens within a single conversation or exchange.

Your methodology confirms:
- Single-turn evaluation (multi-turn planned for future)
- Safety Gate applied at first contact  
- Corrective behavior measured within the interaction window
- Current limitation listed: "Single-turn evaluation (multi-turn planned)"

---

## Findings by File

### index.html (6 issues)

| Line | Current Text | Issue | Suggested Fix |
|------|--------------|-------|---------------|
| 561 | "whether responses stabilize or risk increases **over time**" | Implies longitudinal | "whether responses stabilize users or introduce risk **as vulnerability deepens**" |
| 660 | "sustained emotional safety **over time**" | Implies longitudinal | "sustained emotional safety **within the interaction**" |
| 721 | "as vulnerability deepens" | ✅ GOOD | Keep as-is |
| 806 | "behavioral stability" | ✅ GOOD | Keep as-is |
| 912 | "Boundary Integrity **Over Time**" | Misleading card title | "Boundary Integrity **Under Pressure**" |
| 914 | "as conversations extended" | Implies multi-turn | "as emotional intensity increased" |
| 926 | "in **extended interactions**" | Implies multi-turn | "in **high-vulnerability moments**" |

### research.html (3 issues)

| Line | Current Text | Issue | Suggested Fix |
|------|--------------|-------|---------------|
| 370 | "risk trajectories **over time**" | Implies longitudinal | "risk trajectories **within interactions**" |
| 399 | "consistency and stability **over time**" | Implies longitudinal | "consistency and stability **as vulnerability deepens**" |
| 692 | "Multi-turn trajectory evaluation" | ✅ GOOD - this is in "Planned Improvements" | Keep as-is (correctly positioned as future work) |

### about.html (3 issues)

| Line | Current Text | Issue | Suggested Fix |
|------|--------------|-------|---------------|
| 356 | "made things worse **over time**" | Implies longitudinal | "made things worse **as the interaction progressed**" |
| 390 | "Does safety hold **over time**, or degrade?" | Implies longitudinal | "Does safety hold **as vulnerability increases**, or degrade?" |
| 413 | "How behavior changes **over time** as vulnerability deepens" | Redundant + misleading | "How behavior shifts **as vulnerability deepens**" |

### press.html (2 issues)

| Line | Current Text | Issue | Suggested Fix |
|------|--------------|-------|---------------|
| 480 | "whether it remains safe **over time**" | Implies longitudinal | "whether it remains safe **as vulnerability deepens**" |
| 508 | "stabilize users or introduce risk **over time**" | Implies longitudinal | "stabilize users or introduce risk **within the interaction**" |

---

## Summary of Changes

**Total issues found:** 14  
**Issues to fix:** 11  
**Already correct:** 3 (lines that use "as vulnerability deepens" or correctly position multi-turn as future work)

---

## Recommended Replacement Patterns

| Avoid | Use Instead |
|-------|-------------|
| "over time" | "as vulnerability deepens" / "within the interaction" / "as emotional intensity increases" |
| "extended interactions" | "high-vulnerability moments" / "emotionally charged exchanges" |
| "as conversations extended" | "as emotional intensity increased" / "as vulnerability became apparent" |
| "longitudinal" | (remove or reframe as future work) |
| "trajectories over time" | "behavioral trajectories within interactions" |

---

## Key Framing Principle

**What you measure:** How AI behavior shifts *within a single interaction window* as emotional vulnerability becomes apparent or intensifies.

**What you don't (yet) measure:** How AI behavior changes across multiple sessions, days, or longitudinal user relationships.

The distinction matters because:
1. Your 54.7% stat is about **first contact**
2. Your 43% no-correction stat is about **immediate follow-through**
3. Your methodology explicitly lists "single-turn evaluation" as current scope
4. Multi-turn is correctly positioned as planned future work

The risk pattern isn't slow accumulation over days—it's that harm-adjacent behavior shows up **immediately** and then persists within that same exchange.
