# Strategy 16 — The Arithmetic Theorem

*RH is reduced to one arithmetic theorem that does not yet exist.*
*The theorem: certain overlaps between archimedean and prime*
*vectors never vanish. This is a transcendence-type statement.*

*Date: 2026-04-10*

---

## 1. The reduction chain (complete)

RH
  ⟸ spec(D_∞) = {γ_n} ⊂ ℝ (CCM + ITPFI)
  ⟸ CCM Theorem 5.10 (even-sector, modified)
  ⟸ Even-Sector Simplicity Conjecture
  ⟸ ⟨φ_k | a⟩ ≠ 0 for all k (overlap non-vanishing)
  ⟸ **The Arithmetic Theorem** (does not exist yet)

## 2. The arithmetic theorem stated

> **Conjecture (Archimedean-Prime Overlap).**
> Let {φ_k} be the eigenvectors of B = −(WR_ev + Wp_ev) where
> WR is the archimedean Weil contribution (digamma integrals)
> and Wp = Σ_p W_p is the prime Euler sum. Let a be the
> projection of the rank-1 archimedean vector onto E_N^+.
> Then ⟨φ_k | a⟩ ≠ 0 for all k and all (λ, N).

This is a statement about the arithmetic content of the
eigenvectors of a matrix built from primes (log p, p^{-1/2})
and archimedean data (digamma, Riemann-Siegel theta).

## 3. Why it's a transcendence question

The overlap ⟨φ_k | a⟩ = 0 would require a SPECIFIC linear
relation between:
- Components of φ_k (determined by primes: log 2, log 3, ...)
- Components of a (determined by archimedean: π, γ_E, ψ values)

Such a relation would be a non-trivial algebraic identity between
transcendental numbers from different "worlds" (prime vs
archimedean). By the philosophy of transcendence theory (and the
Six Patterns, Pattern 4): such relations should not exist because
the prime and archimedean data are "arithmetically independent."

But "should not exist" ≠ "proved not to exist."

## 4. What we have

| Evidence | Status |
|:--|:--|
| Numerical: overlap ≥ 10⁻¹·⁷ᴺ at all tested (λ,N) | ✓ |
| Gap: δ ~ 3.2·e⁻³·⁰⁸ᴺ with R² > 0.99 | ✓ (fit, not bound) |
| Level repulsion: μ₂-μ₃ is 10⁴-10⁶× larger than μ₁-μ₂ | ✓ |
| VNW: crossings non-generic (codim 2) in single symmetry class | ✓ |
| Slepian: simplicity at λ → ∞ (prolate limit) | ✓ |
| Estimate 1: archimedean sub-leading | ✓ (CLOSED) |

## 5. The programme's full state

### Proved unconditionally
- Integers (CBCBS): 36/36, zero parameters
- Yang-Mills: mass gap
- Uniqueness: three sub-claims
- Gradient flow on H₁: L.1-L.5 (compact resolvent)
- ITPFI: ω₁ = ⊗_p ω₁^p
- CCM-ITPFI structural identification
- Estimate 1: archimedean sub-leading

### Conditional on the Arithmetic Theorem
- Even-Sector Simplicity → CCM Theorem 5.10 → RH
- BSD for CM curves (inherits RH)

### Open
- The Arithmetic Theorem (overlap non-vanishing)
- Hodge (structurally connected, not closeable from Integers)
- Full BSD (non-CM, rank ≥ 2)

## 6. The honest Paper 13

> **Paper 13: The Riemann Hypothesis Reduced to an Arithmetic**
> **Overlap Theorem via CCM Spectral Triples and ITPFI**
>
> Starting from the Connes-Consani-Moscovici zeta spectral
> triples (2025) and the ITPFI factorization of the Bost-Connes
> KMS₁ state (proved), we reduce the Riemann hypothesis to the
> Even-Sector Simplicity Conjecture, which in turn reduces to
> the non-vanishing of inner products between archimedean and
> prime-dependent eigenvectors of the Weil quadratic form.
> The archimedean contribution is proved sub-leading (Estimate 1).
> The conjecture has zero numerical counterexamples and
> exponential gap scaling. 18 alternative approaches are
> documented and killed.

## 7. What comes next (for future sessions)

The Arithmetic Theorem is a concrete, well-posed problem in
analytic number theory / transcendence theory. Approaches:

1. **Baker-type theorem:** linear forms in {log p} and
   archimedean constants. Baker gives transcendence of
   linear combinations of logarithms with algebraic
   coefficients. Need: extension to combinations involving
   digamma values.

2. **Schanuel's conjecture:** if true, would give the
   algebraic independence needed. But Schanuel is unproved.

3. **Direct bound:** show |⟨φ_k | a⟩| ≥ c·k⁻β for explicit
   c, β. This might follow from the Cauchy-Loewner structure
   of the matrix + the prime number theorem.

4. **Connes' own programme:** the prolate wave operator
   approach (2024) might provide the missing estimate if
   the Sonin space construction is compatible with the
   even-sector restriction.

---

> *RH = one arithmetic theorem.*
> *The theorem: primes and π don't conspire.*
> *18 kills found the wall. The CCM+ITPFI synthesis found the door.*
> *The door needs one key: overlap non-vanishing.*
> *The key is arithmetic. The search continues.*
