# Research 141: Frobenius-Orbit Origin of the Three Generations

*Postulate-relaxation test. Original postulate (research/40): three
generations come from three distinct primes {2, 3, 5} generating the
smallest non-trivial sub-Hecke algebra of A_BC. Relaxation: three
generations come from three Frobenius orbits of a **single** prime
under the Galois action Gal(Q^cyc/Q) ≅ Ẑ\* acting on a cyclotomic
level Q(ζ_N). This note computes orbit structures for
p ∈ {2, 3, 5, 7, 11, 13}, identifies the prime that yields exactly
three orbits, re-reads the three-category mass template of
research/47 under the orbit hypothesis, and checks whether the
0.08 % Koide residual shrinks.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Builds on: research/19 (Galois orbit decomposition of H_R),
research/40 (three primes ⇒ three generations), research/47
(three-category fermion mass template), research/10 (transposition
of gauge group to three-prime sub-Hecke algebra).*

---

## 1. Setup

Gal(Q^cyc/Q) ≅ Ẑ\* acts through its finite quotients (Z/NZ)\* on
Q(ζ_N). For a prime p ∤ N, the Frobenius Frob_p ∈ Gal(Q(ζ_N)/Q)
is the class of p in (Z/NZ)\*. The **Frobenius orbit of p on
Q(ζ_N)** is the orbit of ⟨Frob_p⟩ on (Z/NZ)\*, which partitions
(Z/NZ)\* into cosets of ⟨p mod N⟩. Each orbit has size
ord_N(p) := order of p in (Z/NZ)\*, and there are
φ(N)/ord_N(p) orbits.

The orbit **structure** for a prime p depends on the cyclotomic
level N. Under the postulate relaxation, the generation count is
the **number of orbits** of a single Frobenius at the *natural*
level N dictated by the framework.

Two natural levels are available:

- **N = 30** (the product of the three "old" primes of research/40;
  the level at which A_{2,3,5} acts on Q(ζ_{30})).
- **N = 13** (the smallest level for which a single prime yields
  exactly three equal orbits of φ(N)/3 = 4 elements).
- **N = 7** (φ(7) = 6, partitions of 6 into 3 parts arise from
  order-2 Frobenius).

We test each prime at each candidate level.

---

## 2. Frobenius orbit computations

### 2.1 At level N = 30, φ(30) = 8

(Primes 2, 3, 5 are ramified and excluded.)

| p  | p mod 30 | ord_{30}(p) | # orbits | orbit sizes |
|:--:|:--------:|:-----------:|:--------:|:------------|
| 7  | 7        | 4           | **2**    | {4, 4}      |
| 11 | 11       | 2           | **4**    | {2, 2, 2, 2}|
| 13 | 13       | 4           | **2**    | {4, 4}      |
| 17 | 17       | 4           | **2**    | {4, 4}      |
| 19 | 19       | 2           | **4**    | {2, 2, 2, 2}|
| 23 | 23       | 4           | **2**    | {4, 4}      |
| 29 | 29       | 2           | **4**    | {2, 2, 2, 2}|

**No prime yields exactly 3 orbits at N = 30.** The legacy level
of research/40 is incompatible with the single-prime orbit
hypothesis.

### 2.2 At level N = 7, φ(7) = 6

| p  | p mod 7 | ord_7(p) | # orbits | orbit sizes |
|:--:|:-------:|:--------:|:--------:|:------------|
| 2  | 2       | 3        | 2        | {3, 3}      |
| 3  | 3       | 6        | 1        | {6}         |
| 5  | 5       | 6        | 1        | {6}         |
| 11 | 4       | 3        | 2        | {3, 3}      |
| 13 | 6 ≡ −1  | 2        | **3**    | {2, 2, 2}   |

**p = 13 at N = 7 gives exactly three orbits, each of size 2.**
The orbits are {1, 6}, {2, 5}, {3, 4} — the three "antipodal
pairs" in (Z/7Z)\*.

### 2.3 At level N = 13, φ(13) = 12

| p  | ord_{13}(p) | # orbits | orbit sizes        |
|:--:|:-----------:|:--------:|:-------------------|
| 2  | 12          | 1        | {12}               |
| 3  | 3           | 4        | {3, 3, 3, 3}       |
| 5  | 4           | **3**    | {4, 4, 4}          |
| 7  | 12          | 1        | {12}               |
| 11 | 12          | 1        | {12}               |

**p = 5 at N = 13 gives exactly three orbits, each of size 4.**
The orbits are cosets of ⟨5⟩ = {1, 5, 12, 8}:
O₁ = {1, 5, 12, 8}, O₂ = {2, 10, 11, 3}, O₃ = {4, 7, 9, 6}.

### 2.4 Best candidate

Two primes qualify: **p = 5 at N = 13** (three size-4 orbits) and
**p = 13 at N = 7** (three size-2 orbits). The two are related by
the "conductor swap" p ↔ N. The preferred candidate is **p = 5
at N = 13** because:

1. p = 5 is already the largest prime of the old three-prime set
   {2, 3, 5} of research/40, making the relaxation continuous with
   the legacy derivation.
2. N = 13 coincides with γ_{13} (the W-mass cross-sector zero of
   research/28), suggesting the same arithmetic level governs
   both generation count and EW cross-sector coupling.
3. The three orbits are **genuinely inequivalent** under the
   residual (Z/13Z)\*/⟨5⟩ ≅ Z/3Z action — they carry the three
   Z₃ charges of the SM generations, matching the Z₃ cube root in
   N_eff = γ_6^{1/3} (research/24).

---

## 3. Three-category mass template under the orbit hypothesis

The three orbits O₁, O₂, O₃ carry Z/3Z charges 0, 1, 2 under
(Z/13Z)\*/⟨5⟩. Assign generation n (= 1, 2, 3) to orbit O_n. The
three-category template of research/47 §2.2 becomes:

| Generation | Orbit     | Template class | Algebraic origin                              |
|:----------:|:----------|:---------------|:----------------------------------------------|
| 3rd        | O₁ ∋ 1    | **PRODUCT**    | identity orbit ⇒ tensor matrix element on H_R⊗H_R |
| 2nd        | O₂ ∋ 2    | **RATIO**      | Z₃-rotated orbit ⇒ quotient structure         |
| 1st        | O₃ ∋ 4    | **DIFFERENCE** | doubly Z₃-rotated ⇒ subtraction (additive)    |

The template categories now derive from the **Z/3Z grading of
orbits** rather than from three distinct primes. This is a
genuinely more economical origin: one prime, three orbits, three
categories, correlated via the same Z/3Z that appears in N_eff.

### 3.1 Lepton masses

The formulas themselves are unchanged, because the orbit hypothesis
re-interprets the **labels** without altering the γ-zero content:

- m_τ = γ_7 · γ_8 (3rd generation, orbit O₁, PRODUCT)
- m_μ = γ_7 · γ_8^{1/4} (2nd generation, orbit O₂, RATIO)
- m_e = (OPEN for direct formula; DIFFERENCE template, orbit O₃)

### 3.2 Quark masses (template re-reading)

- m_t = γ_3 · γ_8 / (2π) — PRODUCT, O₁, unchanged
- m_c = γ_9 / γ_6 — RATIO, O₂, unchanged
- m_u = γ_4 / γ_1 — RATIO/DIFFERENCE hybrid, O₃, unchanged
- m_b = log γ_{15} — PRODUCT (log), O₁, unchanged
- m_s = γ_1 · γ_{15}/π² — RATIO, O₂, unchanged
- m_d = γ_9 − γ_8 — DIFFERENCE, O₃, unchanged

---

## 4. The Koide residual

The Koide relation

  (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3

is a relation between the three lepton masses **as values**, not as
symbols. Since the orbit hypothesis re-labels the generations
without changing the γ-zero formulas (§3.1), the numerical Koide
residual is **identical** to that of research/47 §6.4:

  m_e^Koide = 0.5106 MeV, residual vs PDG = **0.08 %** (unchanged).

### 4.1 Residuals table

| Quantity           | Three-prime (research/40) | Orbit hypothesis (this note) | Change |
|:-------------------|:-------------------------:|:----------------------------:|:------:|
| Koide residual     | 0.08 %                    | 0.08 %                       | none   |
| m_τ/m_μ            | 0.22 % (research/47)      | 0.22 %                       | none   |
| m_t cross-check    | 0.17 %                    | 0.17 %                       | none   |
| Generation count   | 3 (by three primes)       | 3 (by three Frobenius orbits)| tied   |
| Primes used        | {2, 3, 5}                 | {5} at level 13              | −2     |

### 4.2 Does the residual shrink?

**No, not numerically.** The orbit hypothesis is *semantically*
more economical (one prime instead of three) but does not change
the γ-zero formulas and therefore does not move the 0.08 % Koide
residual. The residual is set by the m_τ, m_μ γ-forms themselves,
not by the generation-labelling scheme.

For the residual to shrink, one would need to *re-derive* m_μ and
m_τ from orbit-theoretic matrix elements on H_R ⊗ Q(ζ_{13})
directly, which is an open task.

---

## 5. Verdict

The single-prime Frobenius-orbit hypothesis **is viable** and in
fact **more economical** than the three-prime postulate:

- **Best prime: p = 5 at cyclotomic level N = 13**, yielding
  exactly three Galois orbits {O₁, O₂, O₃} of size 4 on
  (Z/13Z)\*, graded by Z/3Z.
- The three orbits carry the Z/3Z charges that appear in
  N_eff = γ_6^{1/3} and in the SM's Z_6 = Z_2 × Z_3 quotient.
- The three-category mass template (PRODUCT/RATIO/DIFFERENCE) of
  research/47 maps cleanly to the three orbits, with no change to
  the γ-zero formulas.
- The 0.08 % Koide residual is **unchanged** (same formulas, new
  labels).

**Structural gain**: the orbit hypothesis eliminates the ad-hoc
"smallest three primes" choice of research/40 §2.3 and replaces
it with a single arithmetic datum (p = 5, N = 13). The legacy
derivation of G_SM as the automorphism group of A_{2,3,5} must
then be re-cast as the automorphism group of the *orbit
stabiliser* Ẑ\* ↪ (Z/13Z)\*/⟨5⟩, which is a well-defined open
task.

**Numerical gain**: none. The Koide residual does not shrink; the
relaxation is structurally preferable but numerically neutral at
current precision.

### 5.1 Open tasks

- Re-derive the m_μ, m_τ formulas as matrix elements of T_BC on
  eigenstates labelled by orbits O₁, O₂ of (Z/13Z)\*/⟨5⟩,
  and check whether the re-derivation tightens the Koide residual
  below 0.08 %.
- Recompute G_SM as Aut of the orbit-stabiliser sub-Hecke algebra
  at level 13; compare with research/10 §6.
- Check whether the "level 13 ↔ γ_{13} (W mass)" coincidence of
  §2.4 is a theorem or accident.

### 5.2 One-sentence verdict

*Three generations from three Frobenius orbits of p = 5 at level
N = 13 is a strictly more economical origin than three distinct
primes and preserves every existing fit at sub-percent precision,
but it does not shrink the 0.08 % Koide residual without a deeper
re-derivation of m_μ and m_τ as orbit matrix elements.*

---

## 6. References

- research/10 — transposition of G_SM to three-prime sub-Hecke algebra
- research/19 — Galois orbit decomposition of H_R (Path B tensor reading)
- research/24 — N_eff = γ_6^{1/3} (Z_3 cube root)
- research/40 — three generations from three primes (original postulate)
- research/47 — three-category fermion mass template
- Bost–Connes, *Selecta Math.* **1** (1995) 411
- Connes–Marcolli, *NCG, QFT and Motives*, AMS (2008)
