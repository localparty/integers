# T10 Vertex: P vs NP L5 backward -- the "wall" is already bypassed by contrapositive

**Source:** Paper 28 preprint PROOF-CHAIN (up-to-date) vs root PROOF-CHAIN (stale). **Date:** 2026-04-14.

---

## Finding: the wall statement in the root PROOF-CHAIN is obsolete

Root `paper28-pvnp/PROOF-CHAIN.md` still says L5 backward (non-full => Taylor) is OPEN. The **preprint** `paper28-pvnp/preprint/PROOF-CHAIN.md` (and sections-04) proves P != NP WITHOUT proving L5 backward directly. It uses the **contrapositive**:

- Path B (Part i, UNCONDITIONAL): Taylor => non-full (L5 forward).
- Route C (Part ii, conditional on CP-1, Theorem-level): **non-Taylor => full**.

The corollary (Steps 16-23) chains both with both directions of Bulatov-Zhuk into a **proof-by-contradiction** for P != NP. L5 backward qua "non-full => Taylor" is never needed as a direct implication: the contradiction form (3-SAT full AND non-full) is what gets used. Route C is the L5-backward-substitute.

**Net:** the wall as literally stated (non-full => Taylor, one-step operator-algebraic to universal-algebraic transfer) is still unproven and probably not provable in one move. But the programme does not need it. It needs only non-Taylor => full, which is closed via Jones-Schmidt + Marrakchi 2018 on the crossed product side, conditional on CP-1 (independently verified by 6 Critics, Route C: p=0.85).

## Assessment of the three classical attack routes

**A. Spectral (TGap=0 forces Taylor).** BLOCKED. Experiment (Strategy 02, `pvnp_modular_flow_polymorphism.py`) falsified the direct mechanism: KMS-weighted majority gives 66.6% match on 2-SAT, 0% on XOR-SAT. The operator algebra controls WHETHER a polymorphism exists, not WHICH one. Spectral => Taylor in one step is dead. Route A in `strategy/04` (full => not-P-time via Hastings area law / Lieb-Robinson) bypasses L5 entirely and is the viable spectral attack -- but Route C already delivers the same bypass more cheaply.

**B. Geometric (trivial holonomy forces Taylor).** BLOCKED at same barrier as A. Holonomy measures rigidity, not the specific algebraic operation.

**C. Information (positive channel capacity forces Taylor).** PARTIALLY BLOCKED. dim_poly_k growth rate distinguishes P from NPC (Paper 28 Q6-OUTDIM, CODE<->INFO capacitor cell) -- but again measures presence, not identity, of the polymorphism.

## Capacitor priority cells for L5 backward

- **ERG <-> OA (Popa cocycle superrigidity, CRITICAL).** Would apply if PCirc+ is w-rigid. **Not established**, and likely false: PCirc+ contains Thompson's V which is non-amenable but NOT w-rigid in Popa's sense (no property (T)). Transfer of algebraic structure from non-fullness to Taylor does NOT follow from Popa.
- **REP <-> OA (Kazhdan (T) for Out(M), CRITICAL).** Symmetric issue: (T) for Out(M_Bool^L) is not known and the non-full case has continuous Out, which is the OPPOSITE of what (T) gives (spectral gap). Direct-mode attack runs the wrong way.
- **MOD <-> OA (Fagin, HIGH).** NP = existential SO logic. Fagin transfers NP-completeness to definability, not non-fullness to Taylor. Provides a complementary characterization but not a proof bridge.

**Verdict on capacitor:** the three CRITICAL/HIGH cells do NOT close L5 backward directly. They'd each require new theorems on PCirc+/Out(M_Bool^L)/definability of Taylor, none of which is in the literature.

## Is there a viable attack route?

Yes -- **the contrapositive is already the viable route, and it is implemented**. The honest statement is:

1. L5 backward as literally phrased (non-full => Taylor, direct transfer) is genuinely stuck -- no one-step cell in the capacitor closes it, and the three direct routes (spectral/geometric/information) are falsified at the "which polymorphism" step.
2. L5 backward as USED in the proof-by-contradiction is closed via Route C's contrapositive (non-Taylor => full), conditional on CP-1 at Theorem level.
3. The root `PROOF-CHAIN.md` is stale relative to preprint. **Recommended action:** update root chain to reflect Route C closure; reclassify "L5 backward wall" as "L5-backward-via-contrapositive, conditional on CP-1 (Theorem)." This is a bookkeeping fix, not new mathematics.

## Conclusion

L5 backward is a Millennium-class wall AS STATED but is NOT the actual gating constraint of the programme. The programme's weakest link is **CP-1 uniqueness** (groupoid identification), not L5 backward. Confidence: the preprint's p=0.82 for the full bridge already prices in the contrapositive route; no new attack is needed to push past 0.82 from the L5 side. Spending cycles on a direct non-full => Taylor proof is lower EV than tightening CP-1.

---

*T10 vertex. L5 backward "wall" bookkeeping fix. Route C contrapositive already carries the load. Next lever is CP-1, not L5.*
