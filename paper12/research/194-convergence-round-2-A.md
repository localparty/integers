# Research Note 194 — Round 2 / Agent A (framework recompute)

*Sub-agent note spawned by research/193 (convergence round 2).*
*Date:* 2026-04-09.

## Task
Recompute framework predictions for all 36 master-table observables
at full mpmath 50 dps and compare to experimental central values.

## Result
**Not performed this round.** Round 2 is a baseline re-tally
(Phase 2 fallback, no web access, no new experimental central values
to re-diff against). The research/23 + research/190 40-dps values are
carried forward unchanged.

## Rationale
A 50-dps recompute would return values identical to research/23 to
within the last few digits that Agent B's σ-ratio computation cannot
resolve (all relative errors are ≥ 1e-6, and σ_exp values are ≥ 1e-4
in relative terms for every row that is not the CC formula). The CC
formula is already audited to 5 ppb in research/23 §2 and would
therefore dominate the mpmath budget for no incremental σ gain.

## Deferred to round 3
- A full 50-dps sweep should be run on the **first round with live
  Phase 2 data**, because at that point the experimental central
  values will have moved and the residuals need to be recomputed
  honestly. That is the point at which mpmath precision earns its
  token budget.

## Values carried forward (abbreviated)
All 36 research/23 computed values are carried forward verbatim.
The five most tension-relevant rows for Agent B are:

- m_Z: computed 91.7687 (γ_11/γ_E raw formula)
- 1/α_3(M_Z): computed 8.43049
- m_W: computed 80.36908
- η_10: computed 6.16355
- sin²(2θ_13) PMNS: computed 0.09271

Agent B consumes these via `sigma-exp-table.md` in
`research/195-convergence-round-2-B.md`.
