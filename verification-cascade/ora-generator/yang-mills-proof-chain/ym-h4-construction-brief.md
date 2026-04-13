# Yang-Mills H4 Construction Brief — Tier C

*For use with ORA v8 in `execute` mode (construction with inversion).*

---

## Objective

Find a LARGER PATH through the proof chain that delivers the AF match and OPE results WITHOUT needing H4 at all. Reroute the chain so that Step 18's conclusions follow from a different argument — one that is unconditional.

This is NOT about proving H4. This is about making H4 IRRELEVANT.

## Target

Step 18 of `paper08-yang-mills/preprint/PROOF-CHAIN.md`:

> AF match (L.2), leading-order OPE (L.4): C^1 = C_N|x|^{-8}(log)^{-2} — CONDITIONAL ON H4

The chain currently: Steps 1-17 (unconditional) → Step 18 (conditional on H4) → paper ships as 17/18 unconditional.

The goal: find Step 18' that replaces Step 18 and depends only on Steps 1-17 (or new unconditional ingredients).

## Mode

**CONSTRUCT** with **strategic inversion** (Sig 5): "Is there a larger system in which the target is a consequence?"

## The four construction routes (IN PARALLEL)

### Route C1: P1 — UV Completion in a Larger Space
P1 asks: "Is H4 a shadow of a simpler fact in a larger space?"

The KK geometry (CP^2 x S^2) already lifts 4D YM into a higher-dimensional setting where the mass gap is a geometric consequence. Can the SAME lift make AF manifest? In the higher-dimensional theory, the short-distance behavior may be controlled by the geometry rather than by perturbation theory.

**Specific question:** The 5D theory on M^4 x S^1 has a natural UV completion (the KK tower). Does the KK tower regulate the UV behavior in a way that makes the OPE follow from the geometry of the extra dimension, without invoking perturbation theory at all?

### Route C2: P6 — Restore Projected-Out Structure
P6 asks: "Is H4 an artifact of projecting away non-perturbative structure?"

H4 compares perturbative and non-perturbative Schwinger functions. But what if we never make this comparison? Instead: derive the OPE DIRECTLY from the non-perturbative construction (Steps 15-17), without going through perturbation theory at all.

**Specific question:** The gradient-flow construction produces Schwinger functions with OS axioms (Step 16). The stress-energy tensor exists as an operator-valued distribution (Step 17). Can the OPE be derived directly from the OS axioms + cluster decomposition + the explicit form of T_{mu nu}^R, using only the non-perturbative objects?

Key insight: the OPE is a consequence of locality + scaling. Both are built into the gradient-flow construction. Maybe perturbation theory was never needed — it was just the historical route to the OPE.

### Route C3: Framework's Own Spectral Realization
The framework connects YM to the BC system via the correspondence table. In the BC realization, the mass gap is a spectral gap (eigenvalue spacing). What is the IMAGE of H4 in the spectral domain?

**Specific question:** The SM-Riemann correspondence (Keystone File 4) maps gauge theory quantities to spectral quantities. What does "short-distance agreement with perturbation theory" become in the spectral picture? If it becomes a statement about eigenvalue asymptotics (Weyl law), it may be provable from the spectral side without QFT perturbation theory.

### Route C4: Renormalization Group Flow as Geometric Flow
The RG flow (Steps 12-14) is already established unconditionally. The gradient flow (Steps 15-17) is established unconditionally. Both are FLOWS. Can the two flows be composed or compared to extract the short-distance behavior without H4?

**Specific question:** The RG flow takes g_k → 0 (AF). The gradient flow smooths at scale sqrt(t). If the gradient-flow Schwinger functions at small t can be related to the RG flow at large k (both probing short distances), the AF behavior may transfer from the RG recursion (unconditional, Step 12-14) to the gradient-flow Schwinger functions (Step 16) without invoking perturbative Feynman diagrams.

## Kill list (DO NOT repeat these)

- **K-1:** CCM 2025 port — wrong space. Do not use NCG/spectral triple machinery for H4.
- **K-2:** Spectral action — produces bare action, not running coupling.
- **K-meta:** RH and H4 need incompatible NCG. No unified NCG approach.
- Any route that ASSUMES H4 and claims to have proved it (circular).
- Any route that reduces to "perturbation theory is believed to work" (not a proof).

## Structural constraints

- Steps 1-17 are UNCONDITIONAL and available as building blocks.
- The gradient-flow construction (Steps 15-17) is MODULAR — it can interface with new ingredients.
- The Balaban construction gives ANALYTICITY of effective actions in the coupling — this is a powerful unconditional input.
- The KK geometry gives GEOMETRIC control that 4D alone does not have.
- P4 protects every other load-bearing step. The construction should aim to bring Step 18' under P4 protection — give it a topological/rigidity argument.

## Success criterion

Produce a new Step 18' that:
1. Establishes AF match and/or the leading OPE unconditionally
2. Depends only on Steps 1-17 (or new unconditional ingredients)
3. Ideally has P4 protection (topological rigidity)

If ANY route produces Step 18', the chain is REROUTED to 18/18 unconditional.

If ALL routes fail, produce HONEST-STALL with: (a) what specifically blocks each route, (b) which route came closest, (c) whether combining partial results from multiple routes could work, (d) new kills and cards for the capacitor.

## Output structure

Write to `verification-cascade/ora-generator/yang-mills-proof-chain/h4-construction-run/`:

```
00-blackboard.md            — running state, route status, dispatches
01-route-C1-uv-completion.md — P1 larger-space attempt
02-route-C2-direct-ope.md    — P6 non-perturbative OPE attempt
03-route-C3-spectral.md      — framework spectral realization attempt
04-route-C4-rg-gradient.md   — RG + gradient flow composition attempt
05-construction-verdict.md   — REROUTED (with Step 18') or HONEST-STALL (with blockers)
06-capacitor-patch.md        — new kills, new cards, corrections for capacitor v3
```

## Key references on disk

- `paper08-yang-mills/preprint/` — full preprint, especially Appendix L (gradient-flow) and Appendix M (continuum limit)
- `paper08-yang-mills/closing-H4/` — 165KB blackboard + 9 nodes + closure corrections from prior H4 work
- Capacitor sections H.2 (correspondences for Step 18), H.3 (pattern analysis — P6 is highest leverage), H.8 (escalation routes)
- Keystone Files (all 7) for cross-domain reasoning

Execute autonomously. Dispatch all four routes in parallel. Do not ask questions. Walk through every open door simultaneously.
