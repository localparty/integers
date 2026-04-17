# NS run-02 arbiter decisions

*Per-cell arbiter reasoning resolving 8 critic dissents from critic-attacks.md.*
*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Arbiter standard

The arbiter decides between author verdict and critic proposal. Standard:

1. **§5d honesty** dominates: any verdict that overstates is downgraded; any verdict that understates an existing bypass is upgraded.
2. **Bypass-pointer completeness**: SILENT verdicts must carry a bypass to programme-level addressing (ADR-N); if the link actually *does* address the requirement (even partially), Pa > S.
3. **Named-wall hygiene**: if a link is the specific location of a named gap, the verdict should be O (with full DELTA-10 fields), not Pa.
4. **Composition vs. addressing**: links that are PROVED may still be Pa for sub-requirements they *feed* rather than *discharge* (addressing semantics).

---

## A1 — L1 Req 4 (periodic T³): **Pa** (author wins)

- Author: Pa (S¹/Z₂ factor contributes periodic structure)
- Critic: S (base T³ periodicity is not in L1)
- Arbiter: **Pa**

Reasoning: L1 (KK reduction on M⁴ × S¹) materially contributes the compactification framework that, when further restricted to M⁴ × S¹/Z₂ and base-sliced, supplies the T³ base of variant (B). The periodic structure is *in* L1's output, not in a silent downstream. Even if L1 does not CLOSE Req 4 on its own, it is a partial addresser (the 5D compactification is why we can pick a periodic base at all). PARTIAL is the honest verdict.

Citation: p1§KK; p30§13 (periodicity construction).

## A2 — L2 Req 2 (bounded energy): **Pa** (author wins)

- Author: Pa (Landau-frame T_μν → NS energy form at leading order)
- Critic: S (BHMR formal expansion; convergence unknown)
- Arbiter: **Pa**

Reasoning: BHMR 2008 §3 derives the Landau-frame stress-energy expansion with EXPLICIT leading-order energy term matching the NS ∫|u|² form. The *formality* of the gradient series is a separate issue (captured in W4 decorative-decoupling disclosure) from whether the leading-order content is present. The leading-order content IS present; therefore Pa, not S. The convergence question is W4.

Citation: BHMR 2008 arXiv:0712.2456 §3; p30§6 energy map.

## A3 — L2 Req 3 (div u = 0): **Pa** (author wins)

- Author: Pa (incompressibility emerges at leading order)
- Critic: S (incompressibility is ASSUMED in BHMR)
- Arbiter: **Pa**

Reasoning: BHMR 2008 §4 derives the incompressibility constraint from conservation laws in the near-equilibrium Landau frame — it is a *derived* leading-order constraint, not an imposed assumption. The critic's reading conflates the ASSUMPTION of near-equilibrium with the CONSEQUENCE of incompressibility. PARTIAL is correct; full rigor of the derivation is part of W4 (decorative decoupling).

Citation: BHMR 2008 §4.

## A4 — L3 Req 3 (div u = 0): **O** (critic wins)

- Author: Pa (YM gauge → NS div-free via structural parallel)
- Critic: O (functor unconstructed, name as W2)
- Arbiter: **O**

Reasoning: p30§00-proof-skeleton explicitly lists the "gradient-flow transfer functor" as THE third wall ("Link 3 ... rigorous functor is not constructed"). A named gap of this specificity should be disclosed as OPEN-BUT-ADDRESSED at the cell level, not buried in PARTIAL. Elevating to O with bypass citation (p8§L.1 Lemmas + pressure Poisson on T³ direct proof) supplies the §5d disclosure discipline. Name the wall: **W2**.

Citation: p30PC L3; p30§00 §3 "third wall"; p8§L.1 Lemmas L.1.1–L.1.5; p30§13 pressure Poisson.

## A5 — L4 Req 1 (C^∞ smoothness): **Pa** (critic wins)

- Author: P (Δ₀^KK > 0 is PROVED UNCONDITIONAL ALL-LOOP)
- Critic: Pa (L4 is *input*, not *addresser*, of Req 1)
- Arbiter: **Pa**

Reasoning: The distinction: *this link is proved* ≠ *this link discharges this requirement*. L4 (KK spectral gap) is indeed PROVED as a theorem about frequency-space control. But Req 1 (C^∞ of u, p on T³) is discharged by composition L5 + L6 + L7 + L8, where L4 feeds L5 as an input. The column should read "how does THIS link contribute to discharging THIS requirement" — L4 contributes as high-frequency-mode control (PARTIAL contribution), not as final discharger.

This is the same pattern as YM: L14 was P for "uniform gap" (which L14 directly proves) but S/Pa for other requirements where L14 is input. Consistency maintained.

Citation: p8T4 + p11K.4 + p10.

## A6 — L5 Req 5 (Leray→smooth): **O** (critic wins)

- Author: Pa (composition with conditional-on-L5 qualifier)
- Critic: O (Leray→smooth passage IS the discharge of Req 5 and IS conditional on W1)
- Arbiter: **O**

Reasoning: Req 5 (Leray→smooth passage) is ONE of the two things L5 centrally addresses (the other is Req 6 BKM). The conditionality of Req 5 on W1 resolution is exactly what OPEN-BUT-ADDRESSED was designed to disclose. Pa hides the conditionality; O with "bypass via W1 Routes A⊕B" discloses it. §5d-honest.

Citation: Leray 1934; Hopf 1951; Camlin 2025; arXiv:2601.08854; p30PC L5.

## A7 — L5b Req 8 (CKN P₁(E) = 0): **Pa** (critic wins)

- Author: P (WF-set triviality ⇒ E = ∅)
- Critic: Pa (needs explicit Hörmander-calculus cross-reference)
- Arbiter: **Pa**

Reasoning: The chain "WF(u) = 0 ⇒ u ∈ C^∞ ⇒ E = ∅ ⇒ P₁(E) = 0" is textbook microlocal (Hörmander IV §8). However, for a Clay-grade compliance artifact, the cross-reference from arXiv:2601.08854's wave-front-set regularity statement to the Hörmander-equivalent pointwise smoothness consequence is a non-trivial inheritance — worth an explicit proof in B_bare §14. Until that inheritance is explicitly laid out, Pa > P. Future upgrade to P after WF→CKN audit in run-03 B_bare synthesis.

Citation: arXiv:2601.08854; Hörmander IV §8 (pending explicit cross-reference); CKN 1982; Lin 1998.

## A8 — L6 Req 2 (bounded energy): **O** (critic wins)

- Author: Pa (5D Killing → 4D viscous dissipation)
- Critic: O (L6 is CONJECTURED — that is a named gap, not a partial success)
- Arbiter: **O**

Reasoning: L6 per PROOF-CHAIN v2.1 is CONJECTURED. The strategy §6 explicitly lists "Energy descent (Link 6) — currently CONJECTURED; the 5D Killing-symmetry argument needs a rigorous Leray-Hopf descent proof before Clay submission" as a priority audit gap. That is the textbook profile of a NAMED WALL. Elevating to O with bypass citation + scheduled proof + confidence 0.50 + effect-if-resolved disclosure is §5d-mandatory. Name the wall: **W3**.

Citation: p30PC L6; Leray 1934; Hopf 1951; strategy §6 priority.

---

## Meta-decision: no new named walls introduced

Although the arbiter elevated three cells to OPEN-BUT-ADDRESSED (A4 → W2, A6 → W1 instance, A8 → W3), ALL THREE walls were ALREADY IDENTIFIED in strategy §6 / §11 and brief DELTA 10:

- W1 (BKM) — strategy §11 + brief DELTA 10 (primary)
- W2 (GF functor) — strategy §6 + p30§00 §3 (third wall)
- W3 (energy descent) — strategy §6 (priority)
- W4 (BHMR decorative) — brief DELTA 10 (secondary)

The arbiter's elevations moved these walls from implicit in the narrative to explicit at the cell level. No new walls introduced at this run.

---

## Lock gate

- 8 dissents raised and resolved.
- 3 verdicts sharpened to OPEN-BUT-ADDRESSED (A4, A6, A8).
- 2 verdicts downgraded from P to Pa for accuracy (A5, A7).
- 3 verdicts held at author's Pa against critic's S (A1, A2, A3).
- 0 bare SILENTs remaining.
- 4 named walls disclosed with full DELTA-10 fields.

**Arbiter pass complete. Matrix locked.**

---

*End of arbiter-decisions.md. 2026-04-14.*
