# C1.04 — Multiplicity

## Question

Hurwitz preserves multiplicity of zeros. Do the zeros of Ξ (the
Riemann zeros) have simplicity, and does the proof need it?

## Facts

- The Riemann zeros are **conjectured** to be simple. This is
  widely believed but **not proved**; a "simple zeros conjecture"
  is slightly stronger than RH itself.

- For RH proper, one does not need simplicity of the zeros.
  RH says Re ρ = 1/2 for all non-trivial zeros, whether simple
  or not.

- Hurwitz theorem preserves multiplicity: if f_n → f uniformly
  on compacts and f is not identically zero, then a zero of f of
  multiplicity m is the limit of m zeros of f_n (counted with
  multiplicity) for n large.

## Does Paper 13 need simple zeros of Ξ?

### The positive direction (reality of zeros)

Paper 13 needs: zeros of Ξ in {|Im z| < 1/2} are real.

The argument: ξ̂_N has only real zeros; ξ̂_N → Ξ uniformly; by
Hurwitz, zeros of Ξ are limits of zeros of ξ̂_N; limits of reals
are real.

This argument does NOT require simplicity of the zeros of Ξ. A
double zero of Ξ at a real point is fine — Hurwitz says it is
the limit of a pair of zeros of ξ̂_N (which are real), and the
limit of two reals is still a real number.

### The negative direction (no missed zeros)

Does Paper 13 need to show all zeros of Ξ are captured? Or only
that the captured ones are real?

For RH, we need all zeros. If there is an off-line zero of ζ at
1/2 + δ + iγ with δ ≠ 0, this produces a zero of Ξ at
z = γ − iδ (with |Im z| = |δ| < 1/2). If the Hurwitz argument
catches this zero (as a limit of zeros of ξ̂_N), then since
zeros of ξ̂_N are real, the limit must be real, so Im z = 0,
contradiction — no off-line zeros.

So we need: every zero of Ξ in {|Im z| < 1/2} is a limit of
zeros of ξ̂_N. This is the "converse" direction of Hurwitz
(every zero of the limit is a limit of zeros of the sequence),
which holds under uniform convergence on compacts to a non-
identically-zero limit. ✓

Multiplicity is not needed for the reality conclusion.

### The CCM eigenvalue simplicity claim

CCM Theorem 5.10(i) asserts that eigenvalues of D_N are real and
**simple** (in the even sector). This simplicity is an assumption
about the finite-dim operator, not about Ξ. It is needed for the
AE-simplicity framework (Section 12) but not for the Hurwitz step.

## Verdict on this subpoint

**Pass.** Simplicity of Riemann zeros is not required by the
Hurwitz step. The argument for reality of zeros of Ξ works
regardless of multiplicity.

Paper 13 does not explicitly address this, but there is no
actual concern here.
