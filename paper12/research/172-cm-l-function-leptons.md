# Research 172: Connes–Marcolli L-Function Matrix Elements and the Charged Leptons

*Cycle 7. Authors: G Six, with Claude Opus 4.6. Date: 2026-04-09.*
*Builds on: research/140 (index-3 sub-factor), research/158 (Frobenius Z/3Z
= Jones Z/3Z bridge theorem), research/161 (standard-invariant ansätze
fail), research/162 (bridge cocycle closed).*

---

## 1. Goal

Execute research/161 §5's recommended next step: test whether the
**matrix elements** of T_BC on the level-13 CM tower, restricted to
the index-3 sub-factor N, reproduce (m_e, m_μ, m_τ) via the L-function
values L(1, χ) for χ a character of (Z/13Z)* of order dividing 3.

The three characters in question factor through
(Z/13Z)* / ⟨Frob_5⟩ ≅ Z/3Z, identified by research/158's bridge
theorem with the outer Z/3Z of the Jones sub-factor. Taking 2 as a
primitive root mod 13, they are

    χ_k(2^a) = exp(2π i k a / 3),   k = 0, 1, 2.

## 2. Computation of L(1, χ_k)

Using the Hurwitz representation
L(1, χ) = −(1/13) Σ_{n=1}^{12} χ(n) ψ(n/13), mpmath at 40 digits:

| k | L(1, χ_k)                                | |L(1, χ_k)|² |
|:-:|:-----------------------------------------|:--------------|
| 0 | 3.09776 (finite-sum regularization)      | 9.59614       |
| 1 | 0.56633 + 0.31510 i                      | 0.420015      |
| 2 | 0.56633 − 0.31510 i                      | 0.420015      |

(For k = 0 the genuine L(1, χ_0) diverges like ζ(1)(1 − 1/13); the
finite Hurwitz sum is used as the regularized value, equivalently the
constant term of the Laurent expansion.)

## 3. Structural obstruction

**χ_2 = χ̄_1.** The two nontrivial order-3 characters of (Z/13Z)* are
complex conjugates, so

    |L(1, χ_1)| = |L(1, χ_2)|   exactly.

Any ansatz of the form m_i ∝ |L(1, χ_i)|² (or any even function of
L(1, χ_i)) therefore assigns **equal masses to m_μ and m_τ**. This is
a symmetry obstruction, not a tuning failure: complex conjugation on
(Z/13Z)* / ⟨5⟩ ≅ Z/3Z acts by τ ↔ τ⁻¹, and |·|² is invariant.

## 4. Numerical test (best-effort assignment)

Pinning m_e := PDG 0.5109989 MeV against |L(1, χ_0)|² and propagating:

| quantity | value            | PDG           |
|:---------|:-----------------|:--------------|
| m_e      | 0.5110 MeV (pin) | 0.5110 MeV    |
| m_μ      | 0.02237 MeV      | 105.6584 MeV  |
| m_τ      | 0.02237 MeV      | 1776.86 MeV   |

Wrong by **four orders of magnitude** in the heavy leptons and
degenerate between μ and τ by construction. Koide:

    Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 0.54055,

residual vs 2/3: **−18.92 %** — essentially identical to research/161
§3.1's principal-graph eigenvalue ansatz (0.5359, −19.6 %), and
~240× worse than the γ-template 0.08 % floor.

## 5. Does the 0.08 % close? **No.**

The failure is sharper than research/161's: there, the A_5 spectrum
had insufficient multiplicative spread. Here the obstruction is a
**symmetry theorem**: any ℓ²-type matrix element of T_BC built from
characters of the Z/3Z quotient is invariant under τ ↔ τ⁻¹, forcing
m_μ = m_τ. The three-generation hierarchy breaks this Z/2
automorphism, so no pure order-3-character L-value scheme can ever
reproduce it. One would need either

(a) characters of higher order (killing the Z/3Z grading that
    research/158 identifies with the generation index), or

(b) non-invariant matrix elements — e.g. L(1, χ) itself (not |·|²),
    using real and imaginary parts as separate observables; but these
    are basis-dependent and not gauge-invariant under change of
    primitive root.

Neither route is compatible with research/158's bridge theorem.

## 6. Verdict

- **Filename**: `paper12/research/172-cm-l-function-leptons.md`
- **Masses (pinned to m_e)**: m_e = 0.5110 MeV, m_μ = m_τ = 0.02237 MeV.
- **Koide Q**: 0.54055.
- **Residual**: −18.92 % vs 2/3; 0.08 % γ-template floor does **not**
  close — it blows up by ~240×.
- **Verdict**: **Fails, and fails structurally.** The CM L-function
  route is excluded not by numerical mismatch but by a symmetry
  theorem: complex conjugation of characters of (Z/13Z)*/⟨5⟩ forces
  m_μ = m_τ in any modulus-squared matrix element.
- **Consequence**: the 0.08 % Koide residual lives in the γ_7·γ_8
  γ-template itself (research/47 §6.4), not in any Z/3Z /
  sub-factor / Bost–Connes layer. Four independent routes have now
  been closed: direct Frobenius orbit periods (research/151), mixed
  Fourier/power scheme (research/157), A_5 principal-graph
  eigenvalues (research/161), and CM L-function matrix elements
  (this note). The individual charged-lepton masses are **not**
  Z/13Z-arithmetic data; they are Riemann-zero data, and Koide Q
  = 2/3 is the only statement about them that the Jones index
  controls (research/140 as upgraded by research/162).

## 7. References

- research/140, 158, 161, 162 (as cited)
- research/47 §6.4 — γ-template Koide, 0.08 % floor
- Connes–Marcolli, *Noncommutative Geometry, Quantum Fields and
  Motives*, AMS Colloquium **55** (2008), Ch. 3 — CM L-functions
- Bost–Connes, *Selecta Math.* **1** (1995) 411 — A_BC

---

*The three characters of (Z/13Z)*/⟨Frob_5⟩ ≅ Z/3Z split as χ_0 and a
conjugate pair χ_1, χ̄_1. Any |L(1, χ)|² scheme is therefore Z/2-
symmetric and cannot distinguish m_μ from m_τ: the resulting Koide Q
is 0.541 (−18.9 %), ~240× worse than the γ-template. The 0.08 %
residual does not close via CM L-values; the charged-lepton hierarchy
is Riemann-zero data, not Z/13Z-arithmetic data.*
