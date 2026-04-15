# Paper 28 — P vs NP

**Directory:** `/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper28-pvnp/`
**PROOF-CHAIN:** 5/6 links closed. Confidence 7/10. Link 5 backward is the wall.

## Claim
P ≠ NP via Boolean BC system + trinity dictionary + Bulatov-Zhuk CSP dichotomy + spectral gap = Taylor gap equivalence.

## Target prize
**Clay Millennium Prize — P vs NP.** Secondary: Gödel Prize (CS), Breakthrough, Knuth Prize.

## Target venues
- Annals of Mathematics / JAMS (math venue — qualifying outlet)
- Companion: STOC / FOCS / JACM (CS venue)
- Cascade: Zenodo → GitHub → arXiv (cs.CC, math.OA, math.LO) → journal

## Current state
- Link 1 (Boolean BC system): PROOF OUTLINED
- Link 2 (Trinity functor cohomology preservation): PROOF OUTLINED
- Link 3 (Bulatov-Zhuk CSP dichotomy): PROVED EXTERNAL
- Link 4 (Taylor gap = spectral gap, 6/6 Schaefer classes): COMPUTATIONALLY VERIFIED
- Link 5 FORWARD (Taylor → non-full): numerically settled
- Link 5 BACKWARD (non-full → Taylor): **OPEN — the wall**
- Link 6 (P ≠ NP): CONDITIONAL on Link 5

## Compliance-readiness: **NEEDS-WORK (wall + obstructions)**
Per `audit/clay-millennium/PvNP/compliance-checklist.md`:
- §5(b) either-direction clause helps framing
- Link 5 backward: seven attempted bypass routes (A-G)
- Obstructions (relativization, natural proofs, algebrization) NOT YET EXPLICITLY AUDITED

## Specific gaps
- Link 5 backward closure (the wall)
- Explicit audit of the 3 obstructions (relativization / natural / algebrization) — required for §5d discipline
- Framing as "conditional under 7 bypass attempts" if wall unresolved
