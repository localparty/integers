# Yang-Mills H4 Excision Brief — Tier B

*For use with ORA v8 in `execute` mode (excision).*

---

## Objective

Find an independent proof that the non-perturbative Schwinger functions agree with perturbation theory at short distances — WITHOUT assuming H4. Produce a self-contained argument that eliminates the H4 dependency from Step 18 of the YM proof chain.

## Target

Step 18 of `paper08-yang-mills/preprint/PROOF-CHAIN.md`:

> AF match (L.2), leading-order OPE (L.4): C^1 = C_N|x|^{-8}(log)^{-2} — CONDITIONAL ON H4

H4 states: non-perturbative Schwinger functions agree with perturbation theory at short distances (the standard hypothesis from Jaffe-Witten Section 4).

## Mode

**EXCISE** — Tier B. The goal is independent re-derivation, not verification. We are trying to PROVE H4, not test it.

## The four routes to explore (IN PARALLEL)

### Route 1: Analyticity + Identity Theorem
The gradient-flow Schwinger functions F(t) are analytic in flow-time t. If the Taylor coefficients at t=0 can be identified with the perturbative coefficients, the identity theorem for analytic functions gives agreement to all orders.

**Status:** BLOCKED at Taylor-coefficient identification (Route A from H4 closure programme).
**What to try:** The capacitor notes that Step 17 constructs T_{mu nu}^R via the Suzuki formula. Can the Suzuki formula's small-t expansion be matched term-by-term to perturbative Feynman diagrams? The gradient-flow regularization (Luscher 2010, arXiv:1006.4518) has an explicit perturbative expansion — can this be leveraged?

### Route 2: Borel Summability + Watson's Theorem
If the perturbative series for the Schwinger functions is Borel summable, Watson's theorem gives agreement between the Borel sum and the non-perturbative answer in a sector of the complex coupling plane. Combined with the gradient-flow analyticity, this may close H4.

**What to try:** The Balaban construction gives analyticity of the effective action in the coupling. Is the analyticity domain large enough to apply Watson's theorem? Key reference: Rivasseau's constructive QFT results on Borel summability of phi^4_4.

### Route 3: Instanton Gas
In the semi-classical regime, instantons are the leading non-perturbative corrections. If the instanton contributions are exponentially suppressed (exp(-8pi^2/g^2)), and the gradient-flow construction controls all non-perturbative effects, H4 follows from the instanton gas being sub-leading.

**What to try:** The KK geometry (CP^2 x S^2) has explicit instanton solutions. Can the instanton action be bounded below using the Bogomolny bound (already established in Step 1*)? If instanton contributions are O(exp(-const/g_k^2)) and g_k -> 0 by AF, they vanish in the continuum limit.

### Route 4: Large-N then Finite-N
At N=infinity (planar limit), the theory simplifies dramatically. Prove H4 at large N using planar dominance, then extend to finite N via 1/N expansion with explicit error bounds.

**What to try:** The Balaban construction works for all N. The 1/N expansion has been made rigorous in simpler models (Rivasseau, Gurau). Can the N-dependence tracking in Appendix I.3 provide the error bounds needed?

## Kill list (DO NOT repeat these)

- **K-1:** CCM 2025 port to YM — KILLED. CCM addresses rank-one perturbation of spectral triple, NOT QFT perturbation theory. Wrong space.
- **K-2:** Spectral action approach — KILLED. Produces bare action at Lambda, not running coupling. Cannot close H4.
- **K-meta:** RH and H4 require incompatible NCG machinery (theta-summable vs finitely-summable). Do not attempt unified NCG approach.

## Structural insight from verification

Step 18 is the ONLY load-bearing step lacking P4 (topological rigidity) protection. The highest-leverage pattern is P6: H4 is literally asking whether the perturbative projection faithfully captures the full theory. The difficulty IS the projection — perturbation theory projects out non-perturbative structure (instantons, renormalons). To close H4, you must show the projected-out structure is sub-leading.

## Success criterion

Produce a SELF-CONTAINED argument (not depending on H4 as an assumption) that establishes:
- The non-perturbative Schwinger functions constructed in Steps 15-17 agree with perturbation theory at short distances, OR
- The OPE C^1 = C_N|x|^{-8}(log)^{-2} follows from the gradient-flow construction without H4

If ANY route produces a complete argument, Step 18 is EXCISED. The chain becomes 18/18 unconditional.

If ALL routes fail, produce HONEST-STALL with: (a) what specifically blocks each route, (b) new kills to add to the capacitor, (c) whether any route is CLOSE enough that a targeted push could close it.

## Output structure

Write to `verification-cascade/ora-generator/yang-mills-proof-chain/h4-excision-run/`:

```
00-blackboard.md          — running state, route status, dispatches
01-route-1-analyticity.md — identity theorem attempt
02-route-2-borel.md       — Borel summability attempt
03-route-3-instanton.md   — instanton gas attempt
04-route-4-large-N.md     — large-N attempt
05-excision-verdict.md    — EXCISED (with proof) or HONEST-STALL (with blockers)
06-capacitor-patch.md     — new kills, new cards, corrections for capacitor v3
```

## Key references on disk

- `paper08-yang-mills/closing-H4/blackboard.md` — 165KB H4 closure blackboard (routes A-D, all prior work)
- `paper08-yang-mills/closing-H4/closure/` — closure corrections
- `paper08-yang-mills/closing-H4/nodes/` — 9 node files from prior attempts
- `paper08-yang-mills/preprint/` — the full preprint (Appendix L for gradient-flow, Appendix M for continuum limit)
- Capacitor H.8 escalation routes for Step 18

Execute autonomously. Dispatch all four routes in parallel. Do not ask questions.
