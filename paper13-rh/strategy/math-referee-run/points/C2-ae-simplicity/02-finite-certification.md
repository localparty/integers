# C2.02 — The Finite Certification (N = 1, ..., 20)

## What was computed

Paper 13 Appendix F:

- At λ = √14, for N = 1, 2, ..., 20:
- Build the (N+1) × (N+1) even-sector matrix A^{ev}(λ, N) at
  120-digit working precision.
- Diagonalize to get eigenvalues {μ_k} and eigenvectors {φ_k}.
- Compute the archimedean cosine vector a^{ev} (explicit rational
  formula).
- Compute overlaps |⟨φ_k | a⟩| for k = 0, 1, ..., N.
- Verify minimum overlap > numerical perturbation error.

Reported results (Appendix F.3):

| N  | gap(μ_1 − μ_0) | min|⟨φ_k|a⟩| | margin | cert? |
|:---|:---------------|:-------------|:-------|:------|
| 1  | 8.0e-2  | 6.2e-1 | ~108 | YES |
| 5  | 2.2e-12 | 2.9e-1 | ~97  | YES |
| 10 | 9.8e-22 | 1.1e-2 | ~87  | YES |
| 15 | 5.6e-29 | 1.4e-3 | ~79  | YES |
| 20 | 7.9e-35 | 9.4e-4 | ~72  | YES |

## Assessment

### Matrix assembly precision

120-digit working precision is generous for a (N+1) × (N+1)
matrix with hypergeometric and digamma entries. Paper 13's
claimed assembly error of 10^{−110} is plausible given mpmath's
default dps behavior.

### Eigenvector perturbation

δ_v ~ δ_A / gap, with δ_A ~ 10^{−110} and gap ~ 10^{−35} at N =
20, gives δ_v ~ 10^{−75}. Overlap minimum ~ 10^{−3}. Ratio
10^{−3} / 10^{−75} = 10^{72}. Safety margin 10^{72}. **Consistent
with paper's claim.**

So the certification is mathematically valid at the reported
precision.

### What does "certified" mean?

The certification establishes that at λ = √14 and each N ≤ 20,
the overlap f_N(√14) ≠ 0, with a margin far exceeding the
numerical computation's error bar. This is a rigorous numerical
statement (given mpmath's correctness).

Combined with the identity theorem (Paper 13 Section 12.2 Stage
2), it implies that at each N ≤ 20, f_N is not identically zero,
hence its zero set is discrete, hence S_N is discrete for
N ≤ 20.

At the specific point λ = √14, the overlap is non-zero, so
AE simplicity holds at that point for each N ≤ 20. This is
enough to invoke CCM Theorem 5.10 at λ = √14, N ≤ 20.

## Concern: the gap shrinks exponentially

The gap decreases exponentially in N (factor ~ 10^{−1.6} per unit
N). At N = 20, gap ~ 10^{−35}. At N = 30, gap ~ 10^{−52}. At
N = 50, gap ~ 10^{−85}. At N = 100, gap ~ 10^{−165}.

The certification precision (120 digits) is **finite**. At some
N_max, the gap drops below the assembly error, and the
certification becomes impossible at finite working precision.

For the N ≤ 20 range actually certified, the margin is 10^{72}
— very comfortable. But the method does not scale to arbitrary
N without increasing precision linearly in N.

**This is not a flaw of the argument**, because the argument
supplements finite certification with a different tool (the
Slepian limit) for N > 20. See C2.03.

## Verdict on this subpoint

**Pass** on the finite certification. At λ = √14 and N ≤ 20,
the overlap is rigorously non-zero at the reported 120-digit
precision, with a safety margin of ~72 orders of magnitude.

This is a genuine numerical theorem: given mpmath's correctness
and the reported input values, the output is deterministic and
reproducible.

The extension to N > 20 via the Slepian limit is examined in
C2.03.
