# Paper 25: Operator-Algebraic Hilbert 12 — The Mathematical Programme After the CBB System

*The mathematical sequel to Paper 23 (CBB system) and Paper 24*
*(bridge family). The CBB framework is reframed as the analytic*
*input to Hilbert's twelfth problem (explicit construction of*
*abelian extensions) over cyclotomic bases. Five conjectures, one*
*new branch of mathematics, RH as a corollary, and the entire*
*follow-up programme for number theorists, operator algebraists,*
*and noncommutative geometers.*

*Status: SKELETON. Content lives in paper12/research/191.*
*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*

---

**REVISED 2026-04-11: Conjecture 5 (V-Hilbert 12) formally RETRACTED.** See `sections-05-08.md` §8.0 for the retraction notice and the Lead 7c refutation record (`paper12/relaxation/research/T7c-stark-rescue-verification.md`, 0 / 30 rescue-candidate tests pass at `mp.dps = 50`). **The paper is now a FOUR-conjecture paper** (Conjectures 1, 2, 3, 4); Conjecture 5 is retained in §8 as historical record with retraction banners. Downstream: §9 "Stark regulator framework" is retracted with Conjecture 5 (it was scaffolding); §12.1 + §12.2 computational programmes are closed out as superseded by the T7c verification's negative result; §15.3 "Hilbert 12 closed" success criterion is withdrawn. The V operator's role in m_τ closure (research/183 → Paper 19/23) is a separate physical-sector result and is unaffected.

---

## 0. Front matter

| Section | Description | Rationale | Strategy reference |
|:--|:--|:--|:--|
| **Title** | "Operator-Algebraic Explicit Class Field Theory at Criticality: The CBB System as Analytic Input to Hilbert's Twelfth Problem" | Names the programme | research/191 |
| **Abstract** [REVISED 2026-04-11] | Hilbert's 12th problem asks for the explicit analytic construction of abelian extensions of a number field. For the rationals Q the answer is the Kronecker–Weber theorem (cyclotomic generators); for imaginary quadratic fields the answer is the theory of complex multiplication (j-function generators); for general fields the problem remains open. The Critical Bost–Connes–Brauer system of Paper 23 organises a four-conjecture programme — CBB Reciprocity, Brauer–KMS Duality (from which the Riemann hypothesis follows as a corollary), Level-Jump Rigidity, and Spectral Kronecker–Weber — placing the framework's bridge cocycle data inside the mathematical structures around Hilbert's 12th problem for cyclotomic bases. *A fifth conjecture (V-Hilbert 12) was initially stated and has since been **formally retracted** in light of the Lead 7c refutation — see §8.0 for the retraction notice and `paper12/relaxation/research/T7c-stark-rescue-verification.md` for the numerical record (0 / 30 pre-committed rescue candidates pass at `mp.dps = 50`). The framework's bridge cocycle `1/k mod ℤ` is a discrete invariant in `H²(ℤ/kℤ, U(1))` and is not encoded in any continuous Galois phase of any Stark-regulator-derived quantity the framework has tested. Paper 25 therefore does **not** claim a partial solution to Hilbert's 12th problem for cyclotomic bases; it claims the four conjectures above, the cohomological-side bridge cocycle verification (Lead 7b, 4/4 bridges), and the bridge minimality theorem (Lead 7e, 4/4 lex-unique minima of a zero-SM-input sieve equalling the SM multiplicities).* | The mathematical follow-up programme | research/191 |

> **Origin callout (G, 2026-04-09):** *"Hilbert's 12th — the framework*
> *just acquired a mathematical sequel that mathematicians already*
> *care about, not invented, not bespoke."*

## 1. Introduction

| Section | Description | Rationale |
|:--|:--|:--|
| **1.1 Hilbert's 12th problem** | history: Kronecker, Hilbert, Weber, Stark |
| **1.2 What is known: Q (Kronecker–Weber) and imaginary quadratic (CM)** | the two solved cases |
| **1.3 What is open: cyclotomic and number-field bases beyond CM** | the gap |
| **1.4 What the CBB system contributes** | analytic generators for abelian extensions of Q(ζ_13), Q(ζ_19) via bridge cocycles |
| **1.5 Why this matters** | mathematicians independently care; the framework gets a mathematical home |

## 2. Mathematical context

| Section | Description | Rationale |
|:--|:--|:--|
| **2.1 Class field theory in one paragraph** | abelian extensions ↔ idele class group |
| **2.2 The Artin reciprocity map** | the central tool |
| **2.3 Stark's conjecture and Stark units** | analytic generators for abelian extensions |
| **2.4 The Bost–Connes phase transition revisited** | from operator algebra to class field theory |
| **2.5 Connes–Marcolli's quantum statistical mechanics of class field theory** | the existing programme |
| **2.6 Where the CBB system fits in** | criticality + explicit Brauer witnesses |

## 3. The CBB system as analytic input

| Section | Description | Rationale |
|:--|:--|:--|
| **3.1 The bridge family as Brauer cohomological data** | Paper 24 recap |
| **3.2 The five primes 2, 3, 5, 7, 11 and the three levels 7, 13, 19** | the bridge primes and conductors |
| **3.3 The minimal conductor 1729 = 7·13·19** | the minimal cyclotomic field containing all bridge data |
| **3.4 Why criticality (β=1) is essential for explicit generators** | the unique fixed-point structure |
| **3.5 The CBB system as a finite-conductor completion of BC** | structural |

## 4. Conjecture 1 — CBB Reciprocity

| Section | Description | Rationale |
|:--|:--|:--|
| **4.1 Statement** | The Frobenius–Jones bridge at (p, ℓ) ∈ {(5,13), (3,13), (7,19)} induces the Artin reciprocity map intertwining KMS_1 states on BC_ℓ with Hecke characters of Q(ζ_ℓ) |
| **4.2 Evidence: research/162 (k=3 case proven)** | sketch + proof outline |
| **4.3 Reduction to k=4 and k=6** | research/179 + 173 |
| **4.4 The reciprocity map explicitly** | (Z/ℓZ)*/⟨p⟩ → Z(M)/Inn(M) |
| **4.5 Consequences if true** | full Artin map for cyclotomic abelian extensions of degree dividing 6 |

## 5. Conjecture 2 — Brauer–KMS Duality

| Section | Description | Rationale |
|:--|:--|:--|
| **5.1 Statement** | [β_{p,ℓ}] equals the obstruction to lifting the KMS_1 state on BC_ℓ to a trace on the V-coupled spectral-action algebra |
| **5.2 What the obstruction is** | a class in H²(out, U(1)) |
| **5.3 Why both sides equal 1/k mod Z** | research/162 + structural extension |
| **5.4 Consequence: the Riemann hypothesis is a corollary** | the obstruction vanishes ⇒ ζ has no off-line zeros |
| **5.5 RH as the global lift condition** | sketch |
| **5.6 Why this is the strongest conjecture** | RH is on the right side |

## 6. Conjecture 3 — Level-Jump Rigidity

| Section | Description | Rationale |
|:--|:--|:--|
| **6.1 Statement** | No non-trivial Frobenius–Jones bridge exists for (7, ℓ < 19); the 13 → 19 jump is forced |
| **6.2 The empirical evidence** | research/169 minimal conductors table |
| **6.3 The structural reason** | (Z/ℓZ)*/⟨7⟩ has order ≠ 6 for ℓ < 19 |
| **6.4 The "minimal" structure of the framework** | each k uses the smallest valid (p, N) |
| **6.5 Consequence: the conductor 1729 is forced, not chosen** | structural |
| **6.6 Connection to the bridge family being a sieve** | only k = 2, 3, 4, 6 populated by SM multiplicities |

## 7. Conjecture 4 — Spectral Kronecker–Weber

| Section | Description | Rationale |
|:--|:--|:--|
| **7.1 Statement** | Every abelian extension of Q(ζ_13) and Q(ζ_19) embedded in the CBB Hilbert space is a finite product of the three named bridges |
| **7.2 Analogy with Kronecker–Weber over Q** | every abelian extension of Q is in some Q(ζ_n) |
| **7.3 Why "spectral"** | the embedding lives in H_R |
| **7.4 The "finite product" condition** | structural compactness |
| **7.5 Consequence: a complete classification of CBB-realisable abelian extensions** | |

## 8. Conjecture 5 — V-Hilbert 12 — **RETRACTED 2026-04-11**

*Retained as historical record with retraction banners on every subsection. See `sections-05-08.md` §8.0 for the retraction notice and T7c refutation table.*

| Section | Description | Rationale |
|:--|:--|:--|
| **8.0 Retraction notice** [NEW 2026-04-11] | Formal retraction of Conjecture 5; refutation record (188 + 267 + T7c, 0/30 rescue candidates pass); list of withdrawn claims; list of preserved framework content | Honest-first discipline |
| **8.1 Statement** [WITHDRAWN] | Original conjecture — that V furnishes analytic generators for abelian extensions of Q(ζ_13), Q(ζ_19) | Historical record |
| **8.2 Why V** [Historical] | V's construction for m_τ closure — separate from Hilbert 12 claim, unaffected | Preserved |
| **8.3 The Stark unit interpretation** [WITHDRAWN] | The L'(0,χ) = −log|ε_χ| → bridge phase rationale | Historical record |
| **8.4 V's matrix elements as Stark unit logarithms** [WITHDRAWN] | The conjectured identification | Historical record |
| **8.5 Consequence: explicit generators for Hilbert 12 at conductor 1729** [WITHDRAWN] | The original headline result — withdrawn | Historical record |
| **8.6 [CLOSED OUT] Reformulation: what functional carries the cocycle?** | Three candidate directions (A) Galois-cohomology boundary map, (B) Beilinson regulator, (C) Weil pairing — all closed as **NOT** load-bearing framework open problems after T7c. General Hilbert-12 open questions, independent of CBB. | Closure |

## 9. The Stark regulator framework — **RETRACTED 2026-04-11**

*§9 was scaffolding for Conjecture 5 and is retracted alongside it. Retained as historical record. The subsections below are preserved with banners but are not active framework content. §9.4 (*"Why Stark regulators are right"*) is explicitly withdrawn — T7c's refutation record shows Stark regulators are **not** right for the bridge cocycle identification at any of the rescue candidates tested.*

| Section | Description | Rationale |
|:--|:--|:--|
| **9.1 Stark's conjecture in one paragraph** [Historical] | L-function leading coefficients = Stark unit regulators — still a real mathematical conjecture; not a framework claim | Preserved |
| **9.2 Stark units and their Galois phases** [Historical] | General number-theoretic content; framework claim on their identification with the bridge cocycle is withdrawn | Preserved |
| **9.3 Why the naive RBC was wrong (research/182)** [Historical] | Recap of prior refutation | Historical |
| **9.4 Why Stark regulators are right** [WITHDRAWN] | This claim is refuted by T7c. Stark regulators do not carry the bridge cocycle in any form the framework has tested. | Historical |
| **9.5 The character-decomposed picture (research/188)** [Historical] | Research/188's analysis is preserved as a refutation record | Historical |
| **9.6 Computing Stark units for (5,13), (3,13), (7,19)** [CLOSED] | Executed in research/267 and T7c; negative result for the naive identification and for all 6 rescue candidates | Historical |
| **9.7 Comparing to the bridge cocycle values** [CLOSED — negative result] | See T7c for the full comparison table; 0 / 30 match at `mp.dps = 50` | Historical |

## 10. The Riemann hypothesis as a corollary

| Section | Description | Rationale |
|:--|:--|:--|
| **10.1 RH in one paragraph** | non-trivial zeros of ζ on Re(s) = 1/2 |
| **10.2 Why RH appears in the CBB system** | the spectrum of log R̂ is {γ_n·π²/2} |
| **10.3 The Brauer–KMS duality interpretation of RH** | obstruction-vanishing |
| **10.4 The 37 R-Theorems and the LOCK** | recap from Paper 12 |
| **10.5 Path to a proof: Conjecture 2 ⇒ RH** | sketch |
| **10.6 Why the CBB framing is the right route** | criticality + explicit witnesses |
| **10.7 Connection to the Connes–Marcolli explicit formula** | research/18 |

## 11. The mathematical follow-up programme

| Section | Description | Rationale |
|:--|:--|:--|
| **11.1 Audience: number theorists** | CFT, Iwasawa, Langlands, Stark conjecture |
| **11.2 Audience: operator algebraists** | BC/CM school, Connes' programme |
| **11.3 Audience: noncommutative geometers** | spectral action, Connes–Marcolli |
| **11.4 Audience: mathematical physicists at criticality** | KMS, type III_1 factors |
| **11.5 Audience: TQFT and category theorists** | Frobenius–Jones as functors |
| **11.6 The five conjectures as the next ~5-10 years of work** | research timeline |

## 12. Computational programmes

| Section | Description | Rationale |
|:--|:--|:--|
| **12.1 Compute Stark units for (5, 13), (3, 13), (7, 19)** [CLOSED — executed in research/267 + T7c, negative for the Conjecture 5 identification] | superseded by the T7c verification | Historical |
| **12.2 Verify Conjecture 5 (V-Hilbert 12) on level 13** [CLOSED — negative result, Conjecture 5 retracted] | Retracted alongside Conjecture 5 | Historical |
| **12.3 Compute the higher-k bridges (k=5, 7, 8, ...)** | concrete task — still open, but these bridges are exploratory, not load-bearing |
| **12.4 The (Z/1729Z)* character lattice** | full character-decomposition test |
| **12.5 Tooling: SageMath, PARI/GP, mpmath** | available |

## 13. Connections to other open problems

| Section | Description | Rationale |
|:--|:--|:--|
| **13.1 The Stark–Tate conjecture** | first-order generalisation |
| **13.2 The Brumer–Stark conjecture** | proved for Q in 2023, open for cyclotomic |
| **13.3 The equivariant Tamagawa number conjecture (eTNC)** | related |
| **13.4 The Gross–Stark conjecture** | p-adic version |
| **13.5 Where CBB fits in this constellation** | criticality completion |

## 14. Open problems generated by the framework

| Section | Description | Rationale |
|:--|:--|:--|
| **14.1 Does every cyclotomic Brauer class arise from a bridge?** | converse to the bridge construction |
| **14.2 What is the full functor Frob → Jones?** | categorical |
| **14.3 Is the CBB system unique among critical KMS_1 systems?** | uniqueness within a category |
| **14.4 Can the conductor 1729 be derived from a meta-rule?** | first-principles |
| **14.5 What is the spectrum of V on H_R?** | open question |
| **14.6 Higher-rank generalisation: GL_2 instead of GL_1** | open |
| **14.7 The connection to L-functions of motives** | open |

## 15. Conclusion

| Section | Description | Rationale |
|:--|:--|:--|
| **15.1 What this paper does** | five conjectures, one programme |
| **15.2 What it doesn't do** | prove anything beyond research/162 |
| **15.3 What success would look like** [REVISED 2026-04-11] | RH proved via Conjecture 2 (Brauer–KMS Duality); Conjectures 1, 2, 3, 4 established; the cyclotomic-Brauer side of the bridge cocycle family hardened at all four bridges with the minimality theorem (Lead 7e) intact. *Hilbert 12 for cyclotomic bases is **no longer** a framework success criterion after the Conjecture 5 retraction; see §8.0.* |
| **15.4 Timeline: 5-10 years if conjectures hold** | the mathematical sequel |
| **15.5 What G said** | *"the framework just earned a mathematical home"* |
| **15.6 The integers exist; the universe follows; the bridges name the link; Hilbert 12 is the next door** | the closing line |

---

## Status

SKELETON. Content lives in paper12/research/191. This paper is the
mathematical follow-up programme: the CBB system reframed as the
analytic input to Hilbert's 12th problem over cyclotomic bases.
~15 sections, ~80+ subsections.

---

*The CBB system is a quintuple. The bridge family is its data.*
*Hilbert's 12th is its mathematical home. RH is its corollary.*
*The integers exist. The universe follows. The bridges name the link.*
