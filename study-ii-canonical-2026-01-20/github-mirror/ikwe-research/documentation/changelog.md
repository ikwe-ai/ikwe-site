# Changelog: Study II

All notable changes to Study II research infrastructure are documented in this file.

---

## Version Control Policy

### Change Categories

| Category | Symbol | Description |
|----------|--------|-------------|
| **MAJOR** | 🔴 | Changes that would invalidate collected data |
| **MINOR** | 🟡 | Changes that affect interpretation but not data |
| **PATCH** | 🟢 | Clarifications, typo fixes, no impact on study |

### Change Process

1. Document proposed change in this changelog
2. Assess impact category
3. If MAJOR during data collection: STOP and evaluate
4. Increment version number appropriately
5. Update all affected documents
6. Create new GitHub commit with clear message

---

## [Unreleased]

*No unreleased changes*

---

## [1.0.0] - 2026-01-20

### Status: 🔒 LOCKED — Canonical Infrastructure

### Added

- **Abstract** — Study II abstract with research questions and hypotheses
- **Methods** — Complete methodological framework
  - Research questions and hypotheses
  - Sample selection criteria
  - Measures specification
  - Analysis plan
- **Results Scaffolding** — Pre-registered results structure with placeholders
- **CF Definition** — Binary composite measure specification
  - SSF component definitions (7 types)
  - Repair behavior assessment (3 levels)
  - Truth table and decision logic
  - Worked examples
- **Scoring Codebook** — Decision-tree coding reference
  - Scenario characteristics coding
  - SSF detection decision trees
  - Repair assessment protocol
  - Pathway classification criteria
  - Reliability procedures
- **Spreadsheet Schema** — Formula-enforced scoring system
  - Column specifications
  - Validation rules
  - CF computation formulas
  - Quality flags
- **Validation Dataset** — 5 exemplar cases for spreadsheet testing
  - Pathway A validation case
  - Pathway B validation case
  - Pathway C validation case
  - No-failure validation case
  - Recoverable failure validation case
- **Figure & Table List** — Pre-specified visualizations and tables
- **Study Lineage** — Evolution from EQ Benchmark to Study II
- **This Changelog** — Version control documentation

### Locked Components

The following are locked as of 2026-01-20 and cannot be modified during data collection:

- [ ] abstract.md
- [ ] methods.md
- [ ] results-scaffolding.md
- [ ] cf-definition.md
- [ ] scoring-codebook.md
- [ ] spreadsheet-schema.md
- [ ] validation-dataset.csv
- [ ] figure-table-list.md
- [ ] study-lineage.md

### Notes

- This represents the canonical research infrastructure prior to data collection
- All methodological decisions are final for Study II v1.0
- Any changes during data collection would require new version increment

---

## Change Log Template

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Category: 🔴/🟡/🟢

### Changed
- [File affected] — Description of change

### Rationale
- Why this change was necessary

### Impact Assessment
- Effect on collected data: [None/Partial/Full invalidation]
- Effect on interpretation: [None/Minor/Major]
- Required actions: [List any follow-up needed]
```

---

## Anticipated Changes (Post Data Collection)

The following changes are expected after data collection completes:

- [ ] Results scaffolding populated with actual data
- [ ] Figure files generated
- [ ] Discussion section added
- [ ] Limitations section completed
- [ ] Supplementary materials added

These will be documented as version 1.1.0 (MINOR — post-collection population).

---

> 🔒 **CANONICAL — DO NOT EDIT**  
> This changelog structure is locked as of 2026-01-20.  
> New entries may be added below the [1.0.0] section following change process.
