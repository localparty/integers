# B2.04 — Dependence on N

## Question

Is the eigenvector approximation uniform in N, or does it degrade?
Does the ITPFI product vector k_λ depend on N?

## Finding

Paper 13 Section 6 notation: k_λ = ⊗_{p ≤ P_N} k_λ^{(p)}, the
tensor product of p-local eigenvectors over primes up to P_N. So
k_λ explicitly depends on N.

Theorem 6.4 gives ‖ξ_λ − c · k_λ‖ = O(1/λ) "as λ → ∞". At
*fixed* N. The paper does not claim that the constant in the O is
independent of N.

For the chain to work downstream, we need one of:

**(A) The estimate uniform in N, for fixed λ**: ‖ξ_λ^{(N)} − c_N · k_λ^{(N)}‖ ≤ C(λ)
uniformly in N, vanishing as N → ∞.

**(B) The estimate uniform in N, for growing λ = λ(N)**: ‖ξ_{λ(N)} − c_N · k_{λ(N)}‖ = O(1/λ(N))
as N → ∞.

Paper 13 gives **neither**. Instead it gives:

**(C)** At each fixed N, ‖ξ_λ − c · k_λ‖ = O(1/λ) as λ → ∞.

(C) is fundamentally a different statement. Without further work,
(C) does not imply (A) or (B).

## The gap(T_0) ≥ C''·λ problem resurfaces

Recall from B2.01 that the eigenvector approximation relies on
gap(T_0) ≥ C'' · λ with C'' depending on "truncation geometry"
— very possibly C'' = C''(N). If C''(N) → 0 as N → ∞, the
estimate degrades badly.

The paper's numerical table (Sec 8.1 / Appendix G) shows
‖ξ_N‖_{H¹} values at N = 5, 10, 15, 20, 30 that are bounded
(∼ 1.7). If the H¹ norm is bounded uniformly, and CF decay is
uniform in N, the Euler-product eigenvector ξ_0 itself is
"well-behaved" in a uniform sense. But this is about ξ_0, not
the approximation ‖ξ_λ − c · k_λ‖.

## What the paper could say (but doesn't)

A charitable reconstruction: perhaps the O(1/λ) estimate is
*actually* uniform in N, because the constants 5.5 and C'' in
Lemma 6.1 do not depend on N. This is possible, but the paper
does not state or prove it. The phrase "depending only on the
truncation geometry" strongly suggests N-dependence.

## Verdict on this subpoint

**Not established.** The uniformity of Theorem 6.4's O(1/λ)
estimate in N is neither stated nor proved. Without it, the
downstream Hurwitz argument cannot use the estimate as the
N → ∞ Fourier transform convergence input.

**Required fix:** Either prove joint uniformity, or state
explicitly that λ = λ(N) grows with N in some specific way and
repeat the estimate for this coupled regime. Without one of
these, the Section 6 → Section 10 bridge is broken.
