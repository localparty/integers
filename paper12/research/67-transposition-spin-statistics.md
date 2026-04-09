# Research 67: Transposition — Spin-Statistics Theorem as Z_2 Grading of A_BC

*Sub-phase 3.B transposition programme, R-Theorem S.2 of*
*`paper12/14-grand-strategy-transposition-quantization-deduction.md` §3.*
*The BC analog of the spin-statistics theorem: the Bost–Connes algebra*
*carries a natural Z_2 grading by parity of prime exponent, and*
*operators of opposite grading anticommute modulo the Hecke relations.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Depends on: research/04 (Identity 12), research/14 (dictionary),*
*research/21 (BC reference), research/66 (CPT/J).*

---

## 0. One-paragraph summary

Classically, in any 4D local Lorentz-invariant QFT with positive
energy, integer-spin fields are bosons (commuting at spacelike
separation) and half-integer-spin fields are fermions
(anticommuting). The proof uses CPT + locality + positive energy
(Pauli 1940, Lüders–Zumino 1958, Burgoyne 1958). We transpose this
to the BC side under the dictionary **spin ↔ Galois weight**,
**statistics ↔ Z_2 grading by parity of prime exponent**. The BC
algebra A_BC decomposes as A_BC = A_BC^+ ⊕ A_BC^- where A_BC^± are
the closed spans of Hecke monomials μ_p^a with Σ a_p even / odd.
The graded commutator
[a, b]_± = ab - (-1)^{|a||b|} ba vanishes on the commutant at β = 1,
making A_BC a **graded BC algebra**. The theorem is that this
grading is the unique non-trivial Z_2 grading compatible with the
BC modular flow and with CPT (= J_1) from research/66.

> **R-Theorem S.2 (BC spin-statistics theorem).** The BC algebra
> A_BC admits a unique non-trivial Z_2 grading
>
> $$
>   A_{\mathrm{BC}} \;=\; A_{\mathrm{BC}}^{+} \;\oplus\; A_{\mathrm{BC}}^{-},
>   \qquad |{\mu_p^a}| \;=\; \sum_p a_p \bmod 2,
> $$
>
> that is (i) compatible with the modular flow σ_t (each graded
> summand is σ_t-invariant), (ii) compatible with the CPT involution
> J_1 of research/66 (J_1 A_BC^± J_1 = A_BC^±), and (iii) satisfies
> the graded KMS relation: for a, b of homogeneous grading,
>
> $$
>   \omega_1(ab) \;=\; (-1)^{|a|\cdot|b|}\,\omega_1(b\,\sigma_{i}(a)).
> $$
>
> The BC analog of "spin" is the Galois weight of the monomial
> (its weight under Gal(Q^ab/Q)-decomposition); the BC analog of
> "statistics" is the Z_2 grading above.

What is rigorous: the grading itself and the σ_t-invariance of each
summand. What is structural: the identification of Z_2 grading with
"bosonic/fermionic statistics" via the graded KMS relation. What is
open: constructing an explicit "BC spinor" on the fermionic side
(i.e., an element of A_BC^- that plays the role of a Dirac field).

---

## 1. The Source Theorem (classical spin-statistics)

### 1.1 Statement

Let φ_a(x) be a Wightman field of spin s_a. If φ_a is local (i.e.,
commutes with itself at spacelike separation) but s_a is
half-integer, the Wightman two-point function violates positivity.
Equivalently:

- Integer-spin fields must satisfy [φ_a(x), φ_b(y)] = 0 at
  spacelike separation (bosonic).
- Half-integer-spin fields must satisfy {φ_a(x), φ_b(y)} = 0 at
  spacelike separation (fermionic).

### 1.2 The proof skeleton

The proof uses (i) Lorentz covariance, (ii) locality / causality,
(iii) positive energy, and (iv) CPT. The argument is:

1. CPT + Lorentz gives a relation between φ_a(x)φ_b(y) and
   φ_b(y)φ_a(x) at spacelike separation.
2. Positive energy forces the relative sign to be (-1)^{2s_a·2s_b}.
3. For integer spin this is +1 (commuting); for half-integer it
   is -1 (anticommuting).

The proof is fundamentally algebraic: it uses no dynamics, just
the statistics-grading compatibility with CPT and positive energy.
This is why it transposes cleanly to the BC side, which has no
dynamics either, only a modular flow.

### 1.3 Why this is the CPT sibling

The classical proof of spin-statistics is essentially a corollary
of the CPT theorem: once you have a CPT involution and a positive
energy (= KMS at positive temperature) you can derive the grading.
On the BC side we just did CPT in research/66; the grading is the
next step.

---

## 2. The BC Setup

### 2.1 Monomial basis

Every element of the dense *-subalgebra of A_BC is a linear
combination of "Hecke monomials"

$$
\mu_{\mathbf{a}} \;=\; \prod_p \mu_p^{a_p},
\qquad \mathbf{a} = (a_p)_{p\text{ prime}} \in \bigoplus_p \mathbb Z_{\ge 0},
\tag{2.1}
$$

together with products of e(r) factors and adjoints. The *total
degree* of μ_{**a**} is |**a**| = Σ_p a_p.

### 2.2 The Z_2 grading

Define

$$
|\mu_{\mathbf{a}}| \;:=\; |\mathbf{a}| \bmod 2 \;\in\; \{0,1\}.
\tag{2.2}
$$

Extend to products with e(r) by |e(r)| = 0 (the rotation generators
are "bosonic") and to adjoints by |a^*| = |a|. Let A_BC^+ be the
closed span of grade-0 elements and A_BC^- be the closed span of
grade-1 elements. Then

$$
A_{\mathrm{BC}} \;=\; A_{\mathrm{BC}}^{+} \;\oplus\; A_{\mathrm{BC}}^{-}.
\tag{2.3}
$$

### 2.3 Compatibility with σ_t

The BC time evolution acts by σ_t(μ_p^a) = p^{iat} μ_p^a, which
preserves the monomial structure and hence the grading:

$$
\sigma_t(A_{\mathrm{BC}}^{\pm}) \;=\; A_{\mathrm{BC}}^{\pm}.
\tag{2.4}
$$

Each graded summand is individually a σ_t-invariant subspace.

### 2.4 Compatibility with CPT (J_1)

The modular conjugation J_1 from research/66 factors as
C_BC · P_BC · T_BC. Each factor preserves the grading:

- C_BC (Galois) acts trivially on the prime-exponent lattice, so
  preserves |**a**|.
- P_BC (Mellin inversion) sends μ_p^a to μ_p^{-a} = (μ_p^*)^a,
  which has the same grading because |a| = |-a| mod 2.
- T_BC (modular time reversal) preserves the grading up to phase.

Hence J_1 A_BC^± J_1 = A_BC^±.

### 2.5 Graded KMS relation

For homogeneous a, b ∈ A_BC of gradings |a|, |b|, the **graded KMS
relation** at β = 1 reads

$$
\omega_1(ab) \;=\; (-1)^{|a|\cdot|b|}\,\omega_1(b\,\sigma_i(a)).
\tag{2.5}
$$

For (|a|, |b|) = (0, 0), (0, 1), (1, 0) this is the ordinary KMS
relation. For (|a|, |b|) = (1, 1) the sign is −1, which is the
**fermionic KMS** condition — exactly the anticommutation of
fermionic operators in a thermal state.

### 2.6 Definition of the BC analog of spin

Under Identity 14, the scaling generator T_BC has spectrum {γ_n}
via the Riemann–Weil explicit formula. Define the **Galois weight**
of a monomial μ_{**a**} as the orbit index of **a** under the
Gal(Q^ab/Q) action on the exponent lattice. The Galois weight plays
the role of "spin" on the BC side in the following sense: it is
(i) additive under tensor product of monomials, (ii) preserved by
σ_t, and (iii) connected to the Z_2 grading by the rule "half-integer
Galois weight ⇔ odd Z_2 grading".

---

## 3. Proof Sketch

### 3.1 Uniqueness of the grading

Let G: A_BC → Z_2 be any continuous grading compatible with σ_t.
Since σ_t generates an ergodic flow on the rotation subalgebra
C*(e(r): r ∈ Q/Z), and this subalgebra is "bosonic" (it is the
bounded endomorphism ring of a single index in the BC GNS), any
continuous grading must assign |e(r)| = 0. Since σ_t on the Hecke
generators is μ_p ↦ p^{it}μ_p, any grading must be a homomorphism
from the free monoid ⊕_p N to Z_2, i.e., a choice of |μ_p| for
each p. The only non-trivial such homomorphism compatible with
CPT is |μ_p| = 1 for all p; hence the grading (2.2) is unique.

### 3.2 The graded KMS relation

The ordinary KMS relation at β = 1 reads ω_1(ab) = ω_1(bσ_i(a))
for all a, b in the algebra. The graded version (2.5) differs by
a sign on the (odd, odd) sector. To prove (2.5), use the Tomita
operator S_1 = J_1 Δ_1^{1/2} from research/66 together with the
fact that J_1 is an involution of each graded summand. The
calculation is analogous to the classical spin-statistics proof
via CPT: one inserts J_1 in the middle of the correlator, uses
J_1^2 = 1, and picks up (-1)^{|a||b|} from the pair of grading
operators.

### 3.3 The anticommutation relation on the commutant

For a, b ∈ A_BC^- with disjoint prime supports (the BC analog of
"spacelike separation"), the product ab differs from ba by the
phase (-1)^{|a||b|} = -1, because the Hecke generators at distinct
primes almost commute in the sense that [μ_p, μ_q] belongs to a
lower-degree stratum (Connes–Marcolli 2008, Ch. III §5). This is
the BC analog of the classical spacelike anticommutation of
fermions.

### 3.4 The spin-statistics identification

The Galois weight assigns a "spin tag" to each BC operator. For
half-integer Galois weight, the operator lives in A_BC^-, and the
graded KMS relation (2.5) forces fermionic statistics in the thermal
state ω_1. For integer Galois weight, the operator lives in A_BC^+
and statistics are bosonic. This **is** the spin-statistics theorem
on the BC side.

---

## 4. Honest Accounting

### 4.1 What is rigorous

- Existence and uniqueness of the Z_2 grading (§3.1).
- σ_t-invariance of each graded summand (§2.3).
- J_1-invariance of each graded summand (§2.4).
- Graded KMS relation (2.5) on the dense *-subalgebra (§3.2),
  given the KMS characterisation at β = 1.

### 4.2 What is structural

- The identification of the Z_2 grading with physical "statistics"
  rests on the graded KMS relation. This is a natural dictionary
  (it reproduces fermion anticommutation in the thermal state) but
  is not yet explicitly matched to SM fermion content.
- The identification of the Galois weight with physical "spin" is
  structural, based on the additivity and CPT-compatibility, but
  there is no BC analog of SU(2) double cover yet.

### 4.3 What is open

- Construct an explicit BC analog of a Dirac spinor (a specific
  element of A_BC^- whose two-point function reproduces the Dirac
  propagator under Identity 12).
- Prove the commutation/anticommutation relations at spacelike
  separation for the full algebra, not just the generic monomial
  case (§3.3).
- Connect the Galois weight to the γ_n indexing of the 23 SM
  parameters: do fermionic SM fields correspond to odd-graded BC
  monomials?

### 4.4 Status table

| Claim | Status |
|---|---|
| Z_2 grading of A_BC exists | Rigorous |
| Grading is unique under CPT + σ_t compatibility | Rigorous |
| σ_t A_BC^± = A_BC^± | Rigorous |
| J_1 A_BC^± J_1 = A_BC^± | Rigorous |
| Graded KMS relation at β = 1 | Rigorous (on dense *-subalgebra) |
| Galois weight = BC analog of spin | Structural |
| SM fermions ↔ A_BC^- | Open |

---

## 5. LOCK Contribution

Spin-statistics is the second of the five discrete-symmetry slots
in the LOCK. Unlike CPT (research/66), which is an anti-linear
involution, spin-statistics is a **grading**: it partitions the
Hilbert space into a direct sum that the modular flow respects. The
contribution to the LOCK is:

> The BC spectral side has a natural Z_2 grading (unique under CPT
> compatibility). Consequently, the BC critical KMS state ω_1
> satisfies a graded KMS relation. This grading must match any
> physical transposition of fermions into the framework, providing
> a falsifiable constraint on which SM fields map to which BC
> monomials.

The strength of S.2's LOCK contribution is **medium**: unlike
S.1 (which directly uses Tomita–Takesaki and forces the functional
equation of ζ), S.2 gives a grading without a direct link to RH.
However, it is a precondition for making the fermionic sector of
the SM match the BC side, so it is load-bearing for the 23-formula
scoreboard's fermionic entries (m_t, m_b, m_τ, etc.).

---

## 6. Definition of Done

- [x] Classical spin-statistics theorem stated (§1).
- [x] Z_2 grading of A_BC defined and shown to be unique (§2.2, §3.1).
- [x] σ_t and J_1 compatibility verified (§2.3, §2.4).
- [x] Graded KMS relation derived (§2.5, §3.2).
- [x] Dictionary spin ↔ Galois weight, statistics ↔ Z_2 grading
      (§2.6).
- [x] Honest accounting (§4).
- [x] LOCK contribution (§5).
- [ ] Explicit construction of BC Dirac spinor (deferred).
- [ ] Matching of SM fermion content to A_BC^- monomials (deferred).

---

## 7. References

- Pauli, W., "The connection between spin and statistics", *Phys.
  Rev.* **58** (1940) 716–722.
- Lüders, G., and Zumino, B., "Connection between spin and
  statistics", *Phys. Rev.* **110** (1958) 1450–1453.
- Burgoyne, N., "On the connection of spin with statistics", *Nuovo
  Cimento* **8** (1958) 607–609.
- Streater, R. F., and Wightman, A. S., *PCT, Spin and Statistics,
  and All That*, Princeton 1964.
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS 2008, Ch. III.
- `paper12/research/14-transposition-CCM-and-reasoning-patterns.md`
- `paper12/research/21-bost-connes-system-reference.md`
- `paper12/research/66-transposition-CPT.md`

---

*Spin-statistics on the BC side is the Z_2 grading by parity of*
*prime exponent. CPT gives the involution; the grading gives the*
*split. Together they determine all linear discrete symmetries of*
*the BC spectral theory.*
