# Prompt Sensitivity Protocol (Benchmark Layer)

Status: Planned benchmark protocol for hostile-review hardening.

## Objective
Test whether headline trajectory claims remain directionally stable across prompt variants.

## Planned Variants
- `P0`: Baseline prompt
- `P1`: Semantically equivalent paraphrase
- `P2`: De-intensified framing
- `P3`: Neutralized framing

## Planned Criteria
- Recompute Figures 2-5 for each variant.
- Preserve model/version pinning across variants.
- Report directional stability for:
  - early first-harm timing
  - repair adequacy levels
  - unresolved harm accumulation

## Output Contract
- Variant registry with prompt hashes.
- Delta table versus `P0`.
- Stability verdict per claim (`Stable`, `Mixed`, `Unstable`).

## Related Detailed Protocol
- `../02_validated/study-ii/Prompt_Sensitivity.md`
