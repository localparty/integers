# C1.05 — Coverage of All Zeros

## Question

Hurwitz on compact subsets gives convergence of zeros inside each
compact. To get ALL Riemann zeros, we need the argument to cover
every compact subset of the strip. Does Paper 13 do this?

## Finding

The Hurwitz theorem (Paper 13 Section 10.2) is stated for a
*connected open set* U with uniform convergence on compact
subsets. The zeros of the limit inside any compact subset are
approximated. By varying the compact subset, one can cover all
of U.

Paper 13 Section 10.1 establishes uniform convergence on compact
subsets of {|Im z| < 1/2}. This is the full open strip where Ξ
encodes critical-strip zeros of ζ.

**Coverage of Riemann zeros:**
- The real-axis zeros of Ξ correspond to critical-line zeros
  of ζ at s = 1/2 + iz. There are ~T/(2π) · log(T/2π) such
  zeros with |γ| ≤ T (Riemann–von Mangoldt).
- Any hypothetical off-line zeros of ζ at Re s = 1/2 + δ
  correspond to complex zeros of Ξ at z = γ − iδ with
  |Im z| = |δ| < 1/2.

For the argument to exclude off-line zeros, Paper 13 needs
convergence on compact sets containing hypothetical off-line
zeros. Any such zero is at finite |z|, and any fixed |z| lies in
some compact. So the "every compact" requirement is met.

## The uniformity-in-N question (again)

This is the same issue as in C1.01: the uniform convergence on
compacts is in which limit parameter?

- "As λ → ∞" is the Paper 13 phrasing.
- "As N → ∞" is what Bögli's spectral exactness uses.

If these are not the same limit, "coverage" has a different
meaning in each. A clean restatement of Section 10 is needed.

## Sub-concern: the strip boundary

The strip {|Im z| < 1/2} is open. As |Im z| → 1/2, the Paley–
Wiener constant C_α in Corollary 6.6 blows up. This means
convergence on compact subsets is fine (every compact stays
bounded away from the boundary), but convergence **uniformly on
the full strip** is not. For coverage of RH, this is not a
problem — critical-strip zeros are discrete and each lies in
some compact subset away from the boundary.

## Verdict on this subpoint

**Pass.** Every Riemann zero (on-line or hypothetically off-line)
lies in a compact subset of the strip, and Paper 13 claims
uniform convergence on every such compact. The coverage is
complete in principle.

The caveat is again the λ-vs-N ambiguity: the "uniform
convergence on compacts" statement needs to be interpreted in
the same limit as the downstream Bögli application.
