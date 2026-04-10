# B3.02 — The Form Difference Δ_N

## What is Δ_N?

Paper 13 Corollary 8.3:

  ‖σ_N |ξ_N⟩⟨ξ_N| − σ_∞ |ξ_∞⟩⟨ξ_∞|‖_op ≤ C_Δ · ρ_Δ^{−N},

with ρ_Δ ≥ 4 (analytically) and ρ_Δ = 19.54 (numerically).

This is the difference of two rank-one operators: the CCM rank-one
correction to D_N at level N, vs its limit at N = ∞. The
exponential decay rate ρ_Δ is claimed to follow from:

  ‖Δ_N‖ ≤ |σ_N| · sin∠(ξ_N, ξ_∞) + |σ_N − σ_∞|,

with the sine controlled by CF decay (Proposition 8.1) and the
scalar difference controlled by ITPFI entry-by-entry convergence.

## Is the rank-one structure exact?

CCM constructs D' as D + rank-one perturbation (Appendix A.3):

  D' = D − |D*ξ⟩⟨η|.

At level N, this is D_N + (rank-one)_N. Both ingredients vary
with N: ξ depends on N (it is the minimum eigenvector of
QW_λ^{N,+}) and η is the Dirichlet kernel on E_N^+, which also
varies with N.

Whether the "difference Δ_N" is exactly rank-one or only
approximately rank-one is a subtle question. If ξ_N and ξ_∞ differ
by a small vector, the difference of the rank-one operators is a
rank-≤ 2 operator:

  |ξ_N⟩⟨ξ_N| − |ξ_∞⟩⟨ξ_∞| = |ξ_N − ξ_∞⟩⟨ξ_N| + |ξ_∞⟩⟨ξ_N − ξ_∞|,

which has rank 2, not rank 1. Its operator norm is bounded by
2·‖ξ_N − ξ_∞‖ (the scalar coefficients are unit, approximately).

Paper 13's writeup conflates "rank-one perturbation" (the
*structure* of the correction at each N) with "rank-one stability"
(the *difference* of corrections across N). The former is exactly
rank-one; the latter is rank-2 at most.

The operator-norm bound

  ‖Δ_N‖ ≤ 2 · ‖ξ_N − ξ_∞‖ + bounded terms

is plausible and is what the paper's Cor 8.3 proof sketch suggests.
The exponential decay then comes from CF decay controlling
‖ξ_N − ξ_∞‖.

## Is ρ_Δ ≥ 4 (analytically) proved?

Paper 13 says ρ_Δ = 19.54 "numerically fitted" and ≥ 4
"analytically". The analytic bound is attributed to research/40
Lemma 1. Without that document I cannot verify.

The paper's hand-wavy analytical argument would be: CF decay
gives ρ_N ≥ 4.27 for the eigenvector tails, and this translates
to an exponential bound on ‖ξ_N − ξ_∞‖, and hence on ‖Δ_N‖.

The subtlety is that ‖ξ_N − ξ_∞‖ is a difference of vectors in
different Hilbert spaces (E_N^+ vs E_∞^+), and the "norm" used in
Cor 8.3 must be the limit space norm with ξ_N viewed as an
embedded vector. The embedded CF decay transfers, but there are
book-keeping details that the paper does not spell out.

## Numerical values

Paper 13 Remark 9.4 tabulates b(N) = C_Δ · ρ_Δ^{−N}:

| N  | b(N)              |
|:---|:------------------|
| 10 | 3.04 × 10^{−26}   |
| 20 | 3.75 × 10^{−39}   |
| 30 | 4.62 × 10^{−52}   |

Extracting ρ_Δ: (3.04e-26 / 3.75e-39)^{1/10} = (8.11e12)^{0.1}
≈ 19.5. Consistent with claimed ρ_Δ = 19.54. So the numerical
pattern is self-consistent.

But **numerical self-consistency at N ≤ 30 is not a uniform
bound for all N**. The pattern could break for larger N. The
analytical ρ_Δ ≥ 4 claim (research/40) would close this if
proved; I cannot verify.

## Verdict on this subpoint

**Conditional pass** on the rank-one structure (understood as
rank-2 difference, not rank-1, but with the same scaling).

**Unverified** for the analytical bound ρ_Δ ≥ 4 — depends on
research/40 Lemma 1, which is not in the preprint.

**Correct numerically** for N = 10, 20, 30 at the reported values.
