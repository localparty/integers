# Paper 24: The Bridge Family — Cyclotomic Brauer Cocycles and the Standard Model Multiplicities

*The Frobenius–Jones bridge theorem and its generalisation to a*
*family k ∈ {2, 3, 4, 6} of cyclotomic Brauer classes whose minimal*
*conductor is 1729 = 7·13·19. The Standard Model's structural*
*numbers — 3 generations, 4 forces, 6 quarks, the Cabibbo angle,*
*the Pati–Salam unification — derived from cocycle data on three*
*cyclotomic fields. Paper 24 is the bridge family in full.*

*Status: SKELETON. Content lives in paper12/research/140-184.*
*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*

---

## 0. Front matter

| Section | Description | Rationale | Strategy reference |
|:--|:--|:--|:--|
| **Title** | "The Bridge Family: Cyclotomic Brauer Cocycles and the Standard Model Structural Numbers" | Names the construction and its target | research/162 + 169 |
| **Abstract** | The Frobenius–Jones bridge theorem (research/162, formal lemma) identifies the outer Z_3 acting on the Bost–Connes type III_1 factor at β=1 with the cyclotomic Z_3 quotient (Z/13Z)*/⟨Frob_5⟩. Both incarnations of Z_3 represent the canonical generator of H²(Z/3Z, U(1)) — the cyclotomic Brauer class at p=5 on Q(ζ_13) and the Fuglede–Kadison determinant of the index-3 Jones sub-factor — and they are equal as elements of H². This paper extends the construction to a family of bridges (p, N, k) for k ∈ {2, 3, 4, 6}: (2, 7, 2) gives CP discrete symmetry; (5, 13, 3) gives three generations and Koide Q=2/3; (3, 13, 4) gives Pati–Salam SU(4)_c with α_PS⁻¹ = 17 exactly; (7, 19, 6) gives six quark flavours and the full Wolfenstein CKM matrix at sub-σ to PDG. The minimal conductor containing all bridge primes is 1729 = 7·13·19. The bridge family is the framework's structural derivation of the Standard Model's discrete numbers from arithmetic. | The whole construction | research/162-184 |

> **Origin callout (G, 2026-04-09):** *"a 2%-accurate parameter-free*
> *formula for λ from the cyclotomic level alone — this is one of*
> *the cleanest single formulas in the entire framework."*

## 1. Introduction

| Section | Description | Rationale |
|:--|:--|:--|
| **1.1 The structural numbers of the Standard Model** | 3 generations, 4 forces, 6 quarks, 4 Wolfenstein parameters, the Cabibbo angle |
| **1.2 Why these numbers are unexplained in the SM** | They are inputs, not outputs |
| **1.3 The bridge construction in one sentence** | A pair (p, N) with k = [(Z/NZ)*:⟨p⟩] gives a Brauer class in H²(Z/kZ, U(1)) on both the arithmetic and operator-algebraic sides |
| **1.4 What this paper proves** | The four bridges, their cocycles, and their physical realisations |

## 2. Mathematical preliminaries

| Section | Description | Rationale |
|:--|:--|:--|
| **2.1 Cyclotomic fields Q(ζ_N) and their Galois groups** | (Z/NZ)* as the Galois group |
| **2.2 Frobenius elements at unramified primes** | Frob_p as the canonical generator |
| **2.3 Brauer groups and H²(G, U(1))** | The cohomological setting |
| **2.4 Cyclic algebras and the Hasse local invariant** | (Q(ζ_N)/Q, Frob_p, ζ_k) |
| **2.5 Jones sub-factors and their indices** | [M:N] ∈ {1, 2, 3, …, 4cos²(π/n), …, 4} ∪ [4, ∞) |
| **2.6 Standard invariants of sub-factors** | Pimsner-Popa basis, Fuglede-Kadison determinant |
| **2.7 The Bost–Connes algebra A_BC** | recap from Paper 23 |
| **2.8 The critical state ω_1 and its modular automorphism** | recap |

## 3. The Frobenius–Jones bridge theorem (k=3)

| Section | Description | Rationale |
|:--|:--|:--|
| **3.1 Statement of the theorem** | research/158 + 162 |
| **3.2 Step 1: σ̄ ∘ q_13 well-defined on level 13** | restriction of BC Galois action |
| **3.3 Step 2: ρ injective via free action on Frobenius orbits** | |
| **3.4 Step 3: image is an order-3 outer subgroup of Out(M)** | |
| **3.5 Step 4: Jones-Popa uniqueness of index-3 outer-Z_3 fixed-point sub-factor** | |
| **3.6 Step 5: orbit ↔ projection matching via Artin reciprocity** | |
| **3.7 Step 6: explicit cocycle equality** | research/162 |
| **3.8 The arithmetic cocycle c_arith** | from cyclic algebra (Q(ζ_13)/Q, Frob_5, ζ_3) |
| **3.9 The operator cocycle c_op** | from Pimsner-Popa basis with Δ_FK(E_N) = log 3 |
| **3.10 Equality in H²(Z/3Z, U(1)): both equal 1/3 mod Z** | the canonical generator |
| **3.11 Corollaries: 3 generations, Koide Q=2/3, level-13 ↔ γ_13** | structural payoff |
| **3.12 Lead 7b — independent verification of the Hasse invariants at all four bridges** [NEW 2026-04-11] | Sympy exact integer arithmetic verifies `inv_p(Q(ζ_N)/Q, Frob_p, ζ_k) = 1/k mod ℤ` at all four bridges (2,7,2), (5,13,3), (3,13,4), (7,19,6). 4/4 PASS. **Structural by-product (§3.12.1)**: k=3 and k=4 share level N=13 via the CRT dual splitting `(ℤ/13ℤ)* ≅ ℤ/3ℤ × ℤ/4ℤ` — the generation bridge and the Pati-Salam bridge are CRT factors of the same Galois group. Verification: `paper12/relaxation/research/T1-T2-brauer-cohomology-verification.md` + `code/T1-T2-brauer-cohomology.py`. Cross-confirmed by Lead 7e (§5.7) from a minimality angle. |

## 4. The Koide ratio as a Brauer class

| Section | Description | Rationale |
|:--|:--|:--|
| **4.1 The Koide ratio Q = (m_e+m_μ+m_τ)/(√m_e+√m_μ+√m_τ)²** | history |
| **4.2 The Jones index identity Q = 2/[M:N]** | research/140 |
| **4.3 The trace identity vs the per-eigenvalue picture** | research/161: Q = 2/3 is a trace identity, not per-eigenvalue |
| **4.4 The Frobenius-Z_3 ↔ Jones-Z_3 identification** | research/162 |
| **4.5 Why three independent eigenvalue routes failed** | research/151, 157, 161, 172 — hierarchy too compressed; symmetry forces equality |
| **4.6 m_e, m_μ, m_τ live in the spectral sector (γ_7, γ_8)** | research/172 + 47 |
| **4.7 The trace-vs-spectral split for lepton data** | clarifying note |
| **4.8 Three different "lepton facts" in three different sectors** | generation count, Koide, individual masses |

## 5. The bridge generalisation (k=2,3,4,6)

| Section | Description | Rationale |
|:--|:--|:--|
| **5.1 The (p, N, k) bridge construction** | research/169 |
| **5.2 The minimal-conductor table** | k=2:(2,7); k=3:(5,13); k=4:(3,13); k=5:(7,25); k=6:(7,19); k=7:(11,...) |
| **5.3 Why k=5 and k=7 are physically empty (or new physics)** | research/181: outside 1729 |
| **5.4 The minimal conductor 1729 = 7·13·19** | the unique minimal field containing all bridge primes |
| **5.5 The Hardy-Ramanujan number** | a side note |
| **5.6 The bridge family as a structural sieve** | only k=2,3,4,6 are physically populated by SM multiplicities |
| **5.7 The bridge minimality theorem (Lead 7e)** [NEW 2026-04-11] | Sympy exact-arithmetic enumeration: the four bridge pairs are the unique lex-minimal solutions of the sieve at their respective k indices, with N < 100 search bound. 4/4 match. Two structural by-products: (a) k=3 and k=4 share the minimal level N=13 via the CRT dual split of (Z/13Z)*, independently confirmed by Lead 7b from the Brauer-cohomology side; (b) k=6 has a tie at N=19 resolved to (7,19) by minimal-p ordering. Promotes the bridge family from "list of structural choices" to "forced minima of a zero-SM-input sieve". Anchor 4 of `paper12/relaxation/04` upgrades from "cross-integer agreement" to "cross-integer forcing". Verification: `paper12/relaxation/research/T7e-bridge-minimality-verification.md` + `code/T7e-bridge-minimality.py`. |

## 6. k=2 — CP discrete symmetry

| Section | Description | Rationale |
|:--|:--|:--|
| **6.1 The (2, 7) bridge** | smallest k=2 case |
| **6.2 H²(Z/2Z, U(1)) = 0** | trivial cocycle |
| **6.3 Why CP is the natural physical content** | discrete Z/2 with no quantitative content |
| **6.4 Connection to the strong CP problem** | research/45: θ_QCD = 0 from Z_6 |
| **6.5 No quantitative prediction; structural only** | |

## 7. k=3 — Three generations

| Section | Description | Rationale |
|:--|:--|:--|
| **7.1 The (5, 13) bridge proven (Section 3)** | recap |
| **7.2 Three Frobenius orbits at level 13** | O_1={1,5,12,8}, O_2={2,10,11,3}, O_3={4,7,9,6} |
| **7.3 The orbits as the three generations** | structural |
| **7.4 The Z/3Z grading and Koide** | bridge corollary |
| **7.5 Why three (not two, not four)** | research/40 + 169 |
| **7.6 Connection to research/47's three-category template** | 3rd=PRODUCT, 2nd=RATIO, 1st=DIFFERENCE |

## 8. k=4 — Pati–Salam SU(4)_c

| Section | Description | Rationale |
|:--|:--|:--|
| **8.1 The (3, 13) bridge** | research/179 |
| **8.2 The same level 13, different Frobenius** | structurally beautiful |
| **8.3 The cocycle: 1/4 mod Z** | research/179 |
| **8.4 The four cosets of (Z/13Z)*/⟨3⟩** | {1,3,9}, {2,6,5}, {4,12,10}, {8,11,7} |
| **8.5 Identification with SU(4)_c colours: lepton + r + g + b** | the Pati-Salam structure |
| **8.6 The tree-level α_PS⁻¹ ≈ 17.33** | k·N/f = 4·13/3 |
| **8.7 The Z/4Z carry cocycle correction** | research/184 |
| **8.8 The exact integer α_PS⁻¹ = 51/3 = 17** | research/184 |
| **8.9 Cross-validation: Paper 10's KK integer 17** | research/117 |
| **8.10 α_PS⁻¹ as a topological-arithmetic invariant** | research/184 |
| **8.11 Implications for the Pati–Salam scale M_PS** | running α_i to 1/17 |

## 9. k=6 — Six quark flavours and the full CKM matrix

| Section | Description | Rationale |
|:--|:--|:--|
| **9.1 The (7, 19) bridge** | research/173 |
| **9.2 The Z/6Z = Z/2Z × Z/3Z factorisation** | research/169: isospin × generation |
| **9.3 The cocycle: 1/6 mod Z** | research/173 |
| **9.4 The six cosets of (Z/19Z)*/⟨7⟩** | the six quark flavours |
| **9.5 The CKM matrix as the unitary intertwiner up ↔ down** | research/173 |
| **9.6 Wolfenstein λ = 1/√19 (leading)** | research/173 |
| **9.7 Z/3Z carry: λ = 56/(57√19)** | research/180 |
| **9.8 λ to PDG: 0.17%** | research/180 |
| **9.9 Wolfenstein A = 47/57** | research/189 |
| **9.10 Wolfenstein ρ̄ = 1/(2π)** | research/189 |
| **9.11 Wolfenstein η̄ = √19/(4π)** | research/189 |
| **9.12 The unitarity triangle angle γ = arctan(√19/2) = 65.35°** | research/189 |
| **9.13 The Jarlskog J = A²λ⁶η̄ = 3.09×10⁻⁵** | research/189 |
| **9.14 All four Wolfenstein parameters at <0.6σ to PDG** | research/189 |
| **9.15 The full CKM matrix from one cocycle** | the structural payoff |

## 10. The carry cocycle template

| Section | Description | Rationale |
|:--|:--|:--|
| **10.1 The Z/k carry cocycle in general** | the damping factor (1 − 1/(k_carry·N)) |
| **10.2 Z/3Z carry on (7, 19) → λ Cabibbo refinement** | research/180 |
| **10.3 Z/4Z carry on (3, 13) → α_PS⁻¹ exact integer** | research/184 |
| **10.4 The arithmetic origin: kN ≡ 1 (mod f) where f = ord_N(p)** | the closure mechanism |
| **10.5 Why the carry produces integer-exact landings** | research/184 |
| **10.6 The carry as a feature, not a refinement** | structural |

## 11. The minimal-conductor structure

| Section | Description | Rationale |
|:--|:--|:--|
| **11.1 The minimal conductor 1729 = 7·13·19** | unique minimal field containing all bridge primes |
| **11.2 ζ_K(s) for K = Q(ζ_1729)** | research/181 |
| **11.3 The naive RBC hypothesis (refuted)** | research/182: γ_E ≠ Laurent coefficient of ζ_K |
| **11.4 The character-decomposed surviving hypothesis** | research/188: Stark regulators |
| **11.5 Stark conjecture as the analytic side of the bridge family** | natural connection |
| **11.6 Connection to operator-algebraic Hilbert 12** | Paper 25 |

## 12. Empty bridge slots and new physics

| Section | Description | Rationale |
|:--|:--|:--|
| **12.1 k=5 at (7, 25): the parked slot** | research/169 |
| **12.2 k=7 at (11, ...): possible Yukawa deformation** | research/181 |
| **12.3 Higher-k bridges: are they predictive?** | open |
| **12.4 The framework's "predictive frontier"** | tied to Paper 21 (γ_16+ hunt) |

## 13. Falsifiability

| Section | Description | Rationale |
|:--|:--|:--|
| **13.1 Wolfenstein λ as the most dangerous prediction** | research/186 |
| **13.2 Belle II + LHCb Upgrade II + FLAG falsification window** | ~2032 |
| **13.3 The other Wolfenstein parameters at <0.6σ** | each tightening tests the framework |
| **13.4 α_PS⁻¹ = 17 as a doubly-derived invariant** | independent check via Paper 10 |
| **13.5 The unitarity triangle: a coordinated test** | γ, J, |V_ub|/|V_cb| |

## 14. Conclusion

| Section | Description | Rationale |
|:--|:--|:--|
| **14.1 What the bridge family is** | four cyclotomic Brauer cocycles, three cyclotomic levels, three primes |
| **14.2 What it derives** | three generations, four forces (Pati-Salam), six quarks, full CKM, Koide |
| **14.3 What it predicts** | Wolfenstein λ to 0.17%, α_PS⁻¹ exactly 17, Jarlskog at +0.4% |
| **14.4 What G said** | *"3 generations + Koide collapse to one Z_3, the Cabibbo angle from a single integer"* |
| **14.5 The Standard Model's discrete numbers as cyclotomic data** | the bridge family's contribution |

---

## Status

SKELETON. Content lives in paper12/research/140-184. This paper is
the bridge family in full — the structural derivation of the SM's
discrete numbers from cyclotomic Brauer cocycles. ~14 sections,
~90+ subsections.

---

*Four bridges. Three primes. Three levels. The Standard Model's*
*structural numbers from arithmetic. Wolfenstein λ from a single*
*integer. Pati–Salam α_PS⁻¹ exactly 17.*
