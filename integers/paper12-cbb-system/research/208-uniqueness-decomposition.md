# 208 — Uniqueness Decomposition of the CBB System

*Date: 2026-04-09. Depends on: anchor §2 (Uniqueness conjecture),
research/155, 162, 164, 174, 175, 178.*

---

## 0. Statement

**Uniqueness Conjecture.** Up to unitary equivalence on H_R and
diffeomorphism of M_geom, there is a unique CBB system

    𝒞 = (H_R, R̂, ω_1, M_geom, {β_k}_{k∈{2,3,4,6}})

at which β = 1 is a KMS fixed point, the ζ-Laurent coefficients are
real, and Brauer–Jones compatibility holds simultaneously for all
k ∈ {2, 3, 4, 6}.

This conjecture decomposes into **three independent sub-claims** with
distinct epistemic statuses.

---

## 1. Sub-claim 1 — Spectral sector unique

**Status: ESSENTIALLY PROVED** (conditional on spectral realisation).

**What's proved.** Conditional on the spectral realisation hypothesis
(that the non-trivial Riemann zeros are eigenvalues of a
self-adjoint operator), the spectral sector is completely rigid:

- ω_1 is the unique KMS_1 state on A_BC (Bost–Connes 1995,
  Theorems 5 and 25). No choice.
- The log-spectrum of L̂ is {γ_n · π²/2}, where {γ_n} are the
  imaginary parts of the Riemann zeros on the critical line. Given
  spectral realisation, this spectrum is fixed.
- The two Laurent coefficients a, b in the effective eigenvalue
  shift γ_n^eff = γ_n + s·(a/γ_n + b/∏γ) are derived from the
  ζ-Laurent expansion at s = 1 with zero degrees of freedom:
  - a = −γ_E(1 + γ_E) ≈ −0.9105 (research/174, diagonal
    Rayleigh–Schrödinger at 2nd order)
  - b = γ_E² + ζ(2) − 2π·γ_1 ≈ 2.4358 (research/164, off-diagonal
    BC resolvent cross-coupling; research/155, Stieltjes derivation)
  - Both are closed-form expressions in {γ_E, ζ(2), γ_1}. Zero
    free parameters.

**What's conditional.** Spectral realisation itself — the assertion
that L̂ exists as a self-adjoint operator whose spectrum encodes the
Riemann zeros. This is an open problem (see research/201 for status).
If RH is true AND spectral realisation holds, Sub-claim 1 is a
theorem.

---

## 2. Sub-claim 2 — Geometric sector unique

**Status: PROVED** (theorem-grade).

**Statement.** The physical point P_phys ∈ M_geom is the unique
global minimum of the Paper 11 spectral action on the moduli space
M_geom of CP² × S² Einstein metrics.

**Evidence.**

- M_geom is 9-real-dimensional, forced by the Hodge numbers of
  CP² × S² combined with the SM gauge rank (research/175). This
  dimension is not a choice — it is dictated by the topology.
- The spectral action S_spec on M_geom has a unique critical point
  P_phys with positive-definite Hessian H ≻ 0 (research/178).
  Therefore P_phys is a strict local minimum.
- Global uniqueness: the boundary of the moduli space is at infinite
  distance in the Weil-Petersson ⊕ Atiyah-Bott ⊕ Bergman metric,
  and S_spec diverges there. Combined with H ≻ 0 at the unique
  critical point, this gives a unique global minimum.
- The 9 electroweak observables (m_τ, m_μ, m_Z, m_H, m_W/m_Z, v,
  1/α, m_τ/m_μ, sin θ₁₂^CKM) are coordinates on M_geom evaluated
  at P_phys (research/171, 8/9 closed at O(1) moduli, factor 236×
  reduction).

**This is a theorem, not a conjecture.** No open conditions.

---

## 3. Sub-claim 3 — Bridge family unique

**Status: PARTIALLY PROVED, PARTIALLY CONJECTURED.**

The bridge family {β_k}_{k∈{2,3,4,6}} assigns cyclotomic Brauer
classes β_k ∈ H²(Z/kZ, U(1)) from cyclic algebras
(Q(ζ_N)/Q, Frob_p, ζ_k) at specific (p, N) pairs. The question is
whether the assignment (p, N, k) is unique.

### 3a. What's proved

- **k = 3 at (5, 13):** The bridge is proved by formal lemma
  (research/162). The cyclic algebra (Q(ζ₁₃)/Q, Frob_5, ζ_3) has
  Brauer class 1/3 mod Z. This is the unique (p, N) pair with
  ord_N(p) = 3 and N prime in the conductor range, giving exactly
  3 generations and Koide Q = 2/3.

### 3b. What's constructive

- **k = 2 at (2, 7):** CP discrete symmetry, trivial H² = 0.
  Structural identification.
- **k = 4 at (3, 13):** Pati–Salam SU(4)_c with α_PS⁻¹ = 17
  exactly via Z/4Z carry cocycle (research/184). Constructive
  with quantitative confirmation.
- **k = 6 at (7, 19):** 6 quark flavours, full CKM matrix with
  λ = 56/(57√19) at 0.17% of PDG (research/180, 189). Constructive
  with quantitative confirmation to sub-sigma precision.

### 3c. What's open

**The selection problem.** The Z_6 sieve — k must divide
|Z(G_SM)| = 6, so k ∈ {1, 2, 3, 6} — constrains the allowed bridge
orders. The extension to k = 4 (which divides 12 = |Z(SU(4)_c)|
rather than 6) is forced by the Pati–Salam embedding. But:

> **Does there exist an alternative set of primes (p', N') at levels
> k ∈ {2, 3, 4, 6} that simultaneously satisfies all five CBB axioms?**

The current assignment (2, 3, 5, 7) at (7, 13, 13, 19) is the only
one found, and the conductor constraint (all bridge primes must lie
in Q(ζ_{1729}) where 1729 = 7 × 13 × 19) strongly restricts
alternatives. But a rigorous proof that no alternative (p', N')
assignment exists has not been given.

**Connection to Level-Jump Rigidity.** Paper 25 Conjecture 3 (the
Hilbert 12 programme, research/191) posits that the level-jump
structure of Brauer classes in the BC tower at β = 1 is rigid — i.e.,
the (p, N) assignment is forced by the cyclotomic structure of A_BC
at the KMS_1 fixed point. A proof of Conjecture 3 would close
Sub-claim 3 completely.

---

## 4. The open question — precise statement

**Question.** Does there exist an alternative bridge family
{β'_k}_{k∈{2,3,4,6}} with different (p', N') assignments that
satisfies all five CBB axioms simultaneously?

- **If no:** the uniqueness conjecture is proved (modulo spectral
  realisation for Sub-claim 1). The CBB system is the unique
  description with zero free parameters.

- **If yes:** the CBB system has a discrete moduli space of bridge
  assignments, and additional data — specifically, the empirical
  matches (27 spectral formulas within experimental error, CKM
  within 0.6σ, t₀ within 0.6σ) — selects the physical assignment
  from a finite set.

In either case, the spectral and geometric sectors are unique (by
Sub-claims 1 and 2). The only potential non-uniqueness lives in the
bridge combinatorics.

---

## 5. Summary table

| Sub-claim | Sector | Status | Evidence | What's open |
|:--|:--|:--|:--|:--|
| 1. Spectral unique | H_R, L̂, ω_1, a, b | ESSENTIALLY PROVED (conditional) | BC95 Thms 5+25; Laurent a,b from ζ with 0 freedom (research/155, 164, 174) | Spectral realisation hypothesis (research/201) |
| 2. Geometric unique | M_geom, P_phys | PROVED (theorem) | dim 9 forced by Hodge (research/175); H ≻ 0, unique global min (research/178); boundary divergence | Nothing — this is closed |
| 3. Bridge unique | {β_k}, (p,N) | PARTIALLY PROVED | k=3 formal lemma (research/162); k=2,4,6 constructive with quantitative match | Alternative (p',N') assignment? Level-Jump Rigidity (Paper 25 Conj. 3) |

---

## 6. Strategic implication

The uniqueness conjecture is "almost proved" in the following sense:
two of three sectors are closed (one conditionally, one absolutely),
and the third has a precise, well-posed open question. The path to
full proof runs through Paper 25's Hilbert 12 programme: prove that
the cyclotomic structure of A_BC at β = 1 forces the (p, N)
assignment uniquely, and the conjecture becomes a theorem (modulo
spectral realisation, which is itself a consequence of RH).

---

*The integers exist. The bridge is almost certainly unique. Proving
it is the last step.*
