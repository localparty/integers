# B1.02 — Uniformity in λ and N

## Question

Does O(1/λ) hold for ALL eigenvalues λ, including the first few?
Or only for λ > λ_0? If the latter, how are the first eigenvalues
handled? Is the implied constant uniform in N?

## Finding

Paper 13 Proposition 5.1 states the bound "for λ = γ_n with n ≥ 2".
So it explicitly excludes the smallest zero γ_1 = 14.13... at
n = 1. The paper does not say how γ_1 is handled.

For the Hurwitz argument in Section 10, the uniform convergence
of ξ̂_λ → Ξ on compact subsets of |Im z| < 1/2 is needed. Any
compact subset containing γ_1 requires the estimate to hold at
λ = γ_1. Paper 13 does not address this.

Further, Section 6.2 Lemma 6.1 says "At fixed truncation level
N, for λ sufficiently large". The bound is:
- at fixed N,
- for λ sufficiently large (no explicit threshold),
- with a constant depending on the "truncation geometry" (Eq 6.6:
  gap(T_0) ≥ C'' · λ "for an explicit constant C'' > 0 depending
  only on the truncation geometry").

**"Truncation geometry" suggests C'' depends on N.** If C'' = C''(N)
and C''(N) → 0 as N → ∞ (for example), then the bound
‖ξ_λ − ξ_0‖ ≤ 5.5/(C''(N)·λ) degrades in N. The Hurwitz chain
(Section 10) requires joint uniform control in both λ and N (see
B2 and C1), which the paper does not establish.

## The λ-vs-N confusion

Paper 13 uses "λ" in at least two distinct senses:

1. **The CCM bandwidth parameter** (fixed in Appendices at
   √14 ≈ 3.742, controlling L = 2 log λ ≈ 2.64).

2. **A spectral parameter** used as a shorthand for "at eigenvalue
   λ = γ_n" in Section 5–6.

These are different meanings. Proposition 5.1 uses "λ" in sense 2
(it ranges over the Riemann zeros). Lemma 6.1 uses "λ" in sense 2
as well. But Section 6.1 writes "At fixed truncation level N, for
λ sufficiently large", which reads like sense 1 (bandwidth).

This is a notational bug, not just a cosmetic one. Without clear
distinction:
- We cannot say whether C'' depends on N or on the bandwidth λ.
- We cannot state the needed uniformity.
- The jump from Section 6 ("at fixed N, large λ") to Section 9
  ("the limit N → ∞") is incoherent as written.

## What the paper needs and does not have

For the chain to work, we need an estimate of the form:

  ‖ξ_λ − ξ_0‖ ≤ C / λ, uniform in N,

for λ = γ_n with n ≥ 1 and for all N sufficiently large (or for
all N). Paper 13 states:

  ‖ξ_λ − ξ_0‖ ≤ 5.5 / (C''(·) · λ),

with C'' depending on "truncation geometry" (possibly on N), for
λ sufficiently large (no explicit threshold), at fixed N. This is
strictly weaker than what is needed.

## Verdict on this subpoint

**Weakened.** The uniformity (joint in λ and N) that the downstream
Hurwitz argument needs is not explicitly established. The paper
conflates two distinct uses of "λ" and does not track the
dependence of the implicit constants on N.

**Required fix:** State Proposition 5.1 with explicit bounds
uniform in N and covering all λ = γ_n (including n = 1). If the
bound degrades at small n, explain how the Hurwitz argument
survives.
