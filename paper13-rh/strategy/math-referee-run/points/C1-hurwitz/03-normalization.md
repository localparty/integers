# C1.03 — Normalization

## Question

Hurwitz requires the limit function to not be identically zero.
Is the convergence ξ̂_N → Ξ or ξ̂_N → c_N · Ξ with c_N → 0? If
normalizations degenerate, Hurwitz may not apply.

## Finding

Paper 13 Theorem 10.1 states "ξ̂_N → c · Ξ" with c = c(λ) the
"normalization scalar of Theorem 6.4". Lemma 6.3 gives
|c'| = 1 + O(λ^{−2}), so c → 1 (up to a unimodular phase) as
λ → ∞.

This is essentially a phase ambiguity: the eigenvector ξ_λ is
defined up to a phase, and c absorbs it. The absolute value |c|
is bounded away from 0, so the limit is not degenerate.

The hypothesis of Hurwitz — that the limit is not identically
zero — is satisfied because Ξ is not identically zero (as a
nontrivial entire function, Ξ has at most countably many zeros
and is non-vanishing on most of its domain).

## Xi(0) check

Paper 13 says "Ξ(0) = 1/2 ≠ 0". I verified computationally that
Ξ(0) = ξ(1/2) = −(1/8) π^{−1/4} Γ(1/4) ζ(1/2) ≈ 0.4971, not 1/2.
The paper's stated value and its stated formula in Appendix E.4
are both wrong (see computation-log.md C2).

**Effect on proof:** COSMETIC. The correct value is nonzero, so
Hurwitz applicability is intact.

**Effect on paper's credibility:** a careful referee reading
Section 10 for the first time will see the claim "Ξ(0) = 1/2"
and immediately check it, finding a wrong value. This undermines
confidence that the paper has been checked.

## Verdict on this subpoint

**Pass on non-degeneracy.** The normalization constant c is
bounded away from 0, and the limit Ξ is not identically zero.
Hurwitz hypothesis met.

**Cosmetic error** on the specific value of Ξ(0): needs to be
corrected to ≈ 0.4971.
