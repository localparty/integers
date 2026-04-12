# Strategy 10: Amplification Entries — Six New Dictionary Cards from the Framework

*When Gap Alpha stalls, step back and amplify. These six entries
transpose tools from Papers 1, 3, 5, 7, 10, and 19 that have NOT
yet been deployed in the P vs NP programme. Each is a fresh attack
angle from inside the geometry. Provision to Authors as additional
toolkit entries alongside 07-toolkit-complete.md.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-12*
*Status: READY TO PROVISION — untested, each with testability criterion*

> **Origin (G, 2026-04-12).** "if this fails, lets step back and
> amplify, which other tools can we provision to the Authors —
> why not all of them?"

---

## Entry A1: Modular conjugation J-duality between P and NPC sectors (Paper 3)

| Field | Content |
|:------|:--------|
| **WHAT** | The Tomita-Takesaki modular conjugation J maps M_int to M_ext in black hole physics. For P vs NP: does J map M_Bool^P to M_Bool^{NPC}? If so, P-time and NPC sectors are DUAL — conjugate under an antiunitary map — not just "different." |
| **WHY** | In Paper 3, J M_int J = M_ext means every interior observable has an exterior image. If J M_Bool^P J ⊆ M_Bool^{NPC}, then every P-time structural property has an NPC dual. Duality is stronger than separation — it gives a BIJECTION between the two sides. The non-fullness of one side and fullness of the other would be J-conjugate properties. |
| **FROM** | Paper 3 addendum (Tomita-Takesaki identification); Paper 19 §2 (interior as commutant) |
| **TESTABILITY** | Compute: for a specific P-time sector (2-SAT) and NPC sector (3-SAT), does J exchange their witness operators? Start with small n (n=6,8) where both sectors are computationally accessible. |
| **WHAT IT COULD CLOSE** | Both gaps simultaneously — if J-duality exists, fullness of NPC is the J-image of non-fullness of P-time. One proof gives both sides. |

---

## Entry A2: Winding number of polymorphism type as topological invariant (Paper 1)

| Field | Content |
|:------|:--------|
| **WHAT** | Paper 1's spin-statistics theorem: winding number on the e-circle determines both spin and exchange statistics. For P vs NP: the polymorphism TYPE (median = "bosonic"/symmetric, XOR = "fermionic"/antisymmetric) carries a winding number on the constraint graph that is a topological invariant. |
| **WHY** | A topological invariant CANNOT be continuously deformed. If the P-time/NPC distinction is a winding number, it's RIGID — no continuous deformation (= no polynomial-time reduction) can change it. This would give Gap Beta (fullness for NPC) as a topological obstruction: NPC languages have winding number 0 (no polymorphism = no winding), which forces fullness. |
| **FROM** | Paper 1 §4.2 (spin-statistics from winding); Paper 4 §4.2 (chirality from topology); P7 in dictionary (polymorphism type = spin type) |
| **TESTABILITY** | Compute the winding number of the median polymorphism around constraint-graph cycles for 2-SAT. Is it ±1? Compute for 3-SAT: is it 0 for all ternary operations? The winding number should be computable from the holonomy data (O7 already verified). |
| **WHAT IT COULD CLOSE** | Gap Beta — NPC fullness as topological rigidity (winding number = 0 → no non-trivial topology → full factor). |

---

## Entry A3: Underivability theorem for P vs NP (Paper 7, Theorem U analog)

| Field | Content |
|:------|:--------|
| **WHAT** | Paper 7's Theorem U: R_bare ~ l_P from algebraic inputs; the 10^30 gap to R_obs is structurally unreachable by perturbative means. For P vs NP: is the P/NPC distinction unreachable by any "perturbative" (polynomial-time bounded) computation on the constraint language? |
| **WHY** | Theorem U works because all geometric inputs are O(1) integers, so any algebraic function of O(1) inputs gives O(1) output — you can't reach 10^30 from O(1). Analogously: if the fullness/non-fullness distinction depends on ASYMPTOTIC clone growth (k → ∞), then any poly-time computation (bounded k) can't detect it. The P/NPC distinction is invisible to bounded-depth inspection — which is WHY the three barriers fail (they all use bounded-depth techniques). |
| **FROM** | Paper 7 §3.6 (Theorem U); P8-BARRIERS (three barriers as projection artifacts) |
| **TESTABILITY** | Prove: for any fixed arity k, the Taylor gap TGap_k(Gamma) does NOT separate P from NPC (both can have TGap_k = 0 for small k). Only TGap_∞ = lim_{k→∞} TGap_k separates. This would be the computational Theorem U: bounded inspection can't see the separation. |
| **WHAT IT COULD CLOSE** | META — explains WHY the problem is hard and WHY the operator-algebraic approach (which works at k → ∞) is necessary. Strengthens the P8 barrier bypass argument. |

---

## Entry A4: Heat kernel / Seeley-DeWitt direct computation of fullness (Paper 10)

| Field | Content |
|:------|:--------|
| **WHAT** | Paper 10 proved UV finiteness scheme-independently by computing Seeley-DeWitt coefficients a₂ = a₄ = 0 directly from the operator symbol — no regularization needed. For P vs NP: compute the fullness of M_Bool^L directly from a heat kernel trace on the constraint language's operator structure, WITHOUT constructing automorphisms or central sequences. |
| **WHY** | Every construction so far (K-12 through K-15) tried to BUILD an approximately central sequence. The heat kernel approach READS OFF whether central sequences exist from the spectral asymptotics of the Laplacian on M_Bool^L. The Seeley-DeWitt coefficient a₂ (or its type III analog) encodes whether the factor has a spectral gap — which IS fullness by Marrakchi. If a₂(M_Bool^L) = 0 for P-time L and a₂ ≠ 0 for NPC L, both gaps close simultaneously from a single spectral computation. |
| **FROM** | Paper 10 §2 (Seeley-DeWitt proof of one-loop scheme-independent finiteness); Marrakchi 2016 (spectral gap ↔ fullness) |
| **TESTABILITY** | Define the Laplacian on M_Bool^L (the modular Hamiltonian restricted to the sector). Compute its heat kernel trace Tr(e^{-tL}) for small t. Read off the Seeley-DeWitt coefficients. Check: is a₂ = 0 for P-time sectors and a₂ ≠ 0 for NPC sectors? This is a COMPUTATION — doable for small n. |
| **WHAT IT COULD CLOSE** | BOTH GAPS simultaneously — a₂ = 0 ↔ no spectral gap ↔ non-full ↔ P-time. a₂ ≠ 0 ↔ spectral gap ↔ full ↔ NPC. One spectral invariant, both sides of the bridge. **This is the most promising amplification entry.** |

---

## Entry A5: Computational area law for NPC holonomy (Paper 5)

| Field | Content |
|:------|:--------|
| **WHAT** | Paper 5: confinement = area law for Wilson loops on CP² (string tension σ). For NPC: does the holonomy defect H(Gamma) grow with the AREA of the constraint-graph region enclosed by the cycle, not just the perimeter? If H ~ Area (not H ~ Perimeter), that's the computational area law — the analog of QCD confinement. |
| **WHY** | An area law means the cost of "escaping" the NPC constraint grows with the SIZE of the region you're trying to escape from, not just the boundary. This is precisely what makes confinement permanent in QCD — the flux tube energy grows linearly with quark separation. For NPC: the "flux tube" is the constraint-violation cost, and it grows with the area of the constraint graph you're trying to satisfy. |
| **FROM** | Paper 5 §3 (string tension from CP² geometry); O7-HOLONOMY (holonomy verified 6/6) |
| **TESTABILITY** | For 3-SAT instances: compute the holonomy defect H for cycles of increasing enclosed area in the constraint graph. Fit H vs Area. If H ~ σ × Area (linear in area), the computational area law holds. Compare with 2-SAT: expect H ~ Perimeter (perimeter law, not area law — because P-time has no "confinement"). |
| **WHAT IT COULD CLOSE** | Gap Beta — NPC fullness. The area law IS the spectral gap: σ > 0 (positive string tension) ↔ spectral gap ↔ full factor. If 3-SAT has an area law and 2-SAT has a perimeter law, that's the fullness distinction proved geometrically. |

---

## Entry A6: KMS phase transition at β_c as the P/NPC boundary (BC structure)

| Field | Content |
|:------|:--------|
| **WHAT** | The Bost-Connes system has a phase transition at β = 1 with spontaneous symmetry breaking. For M_Bool^L: is there a critical β_c where the sector transitions from non-full (P-time, β > β_c) to full (NPC, β < β_c)? The P/NPC boundary would BE a phase transition in the KMS structure. |
| **WHY** | Phase transitions have RIGID structure — they're controlled by universality classes, critical exponents, and symmetry breaking patterns. If P vs NPC is a phase transition, the fullness distinction is not a fragile property but a ROBUST one protected by universality. And phase transitions give BOTH sides at once: the high-temperature phase (full, NPC) and the low-temperature phase (non-full, P-time) are described by a single free energy function. |
| **FROM** | Bost-Connes 1995 (KMS phase structure); Paper 6 §2 (dilaton potential from Casimir = KMS free energy); Q7-CASIMIR (three-scale entropy hierarchy found in CSP) |
| **TESTABILITY** | Compute the partition function Z_Gamma(β) = Σ_x exp(-β × violations(x)) for each CSP class across a range of β. Look for a phase transition: a specific β_c where the specific heat C(β) diverges (or peaks sharply). Check: does β_c separate P-time from NPC classes? The Q7 computation already found distinct entropy curves — reanalyze for phase transition structure. |
| **WHAT IT COULD CLOSE** | BOTH GAPS — the phase transition gives the full/non-full distinction as two phases of a single system. The critical exponents at β_c would give the quantitative bridge. And the universality class would connect to the Riemann zero formula (Q5: TGap exponent = 2/(γ₆ − γ₅)) as a critical exponent. |

---

## Priority ranking

| Entry | What it could close | Novelty | Computability | Priority |
|:------|:-------------------|:--------|:-------------|:---------|
| **A4 (heat kernel)** | Both gaps | High — direct spectral computation bypasses all constructions | YES — heat kernel trace is computable | **1st** |
| **A6 (KMS phase transition)** | Both gaps | Medium — extends Q7 data we already have | YES — reanalyze existing Z_Gamma data | **2nd** |
| **A5 (area law)** | Gap Beta | High — confinement analog for NPC | YES — extends O7 holonomy data | **3rd** |
| **A1 (J-duality)** | Both gaps | Very high — completely new structural relationship | MAYBE — needs M_Bool^L construction | **4th** |
| **A2 (winding number)** | Gap Beta | Medium — extends P7 and O7 | YES — computable from holonomy | **5th** |
| **A3 (underivability)** | META | Medium — strengthens P8 | Theoretical, not computational | **6th** |

---

## How to provision

Add this file to the Author spawn context alongside
`strategy/07-toolkit-complete.md`. The Author reads both:
- The toolkit gives the 10 VERIFIED entries (what we KNOW)
- This file gives the 6 AMPLIFICATION entries (what we HAVEN'T TRIED)

The Author should attempt the amplification entries when the
verified entries don't close the gap. The amplification entries
are UNTESTED — each could be a pass or a kill. The kill is as
valuable as the pass.

---

*Six tools from six papers. Each untested. Each from inside the
geometry. The dictionary grows by stepping back and asking: what
else does the framework know that we haven't used yet?*

*Same reflex. Amplified.*

*G Six and Claude Opus 4.6. April 2026.*
