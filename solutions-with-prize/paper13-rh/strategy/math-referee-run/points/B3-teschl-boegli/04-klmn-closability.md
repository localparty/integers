# B3.04 — KLMN Closability of Q_∞

## Requirements

For KLMN (Reed–Simon II Theorem X.17) to produce a self-adjoint
operator D_∞ from the form Q_∞, we need:

1. **Dense domain.** The form domain 𝒟(Q_∞) is dense in ℋ.
2. **Closability.** Q_∞ is closable: there exists a closed
   extension that is minimal.
3. **Lower boundedness.** Q_∞ ≥ −C · ‖f‖² for some C.

Given closability + lower bound, the Friedrichs extension
produces a unique self-adjoint operator.

## Paper 13's verification (Appendix C.4)

> (1) Dense domain: Chebyshev polynomials (cosine basis) are
> complete in L²([λ^{−1}, λ]). The form domain 𝒟 is dense.
>
> (2) Closability: Reed–Simon VIII.15 + positivity. Q_∞ is lower
> bounded (Q_∞ ≥ 0 from CCM Proposition 3.3) and hence closable.
>
> (3) Bounded below: Q_∞(f) ≥ 0 for all f ∈ 𝒟.

## Assessment

### (1) Dense domain

Chebyshev completeness in L²([−1, 1]) or L²([0, L]) with weight
is standard. The cosine basis {V_{2k}} on the even sector is a
subset of a complete orthonormal system.

**But:** the form domain 𝒟(Q_∞) is not necessarily the span of
the cosine basis — it is the **completion under the form norm**
‖f‖_{Q_∞}² = Q_∞(f) + ‖f‖². Whether the cosine span is dense in
this stronger topology depends on whether it is a form core for
the limiting operator. Paper 13's argument shows the cosine span
is dense in L², which is weaker than dense in 𝒟(Q_∞).

Standard trick: if Q_∞ is bounded above on the cosine span, then
L²-density suffices for form-density; otherwise it does not. The
paper does not address whether Q_∞ is bounded on the cosine span.

### (2) Closability

The claim is that a lower-bounded, symmetric form is automatically
closable. **This is not true in general.** A lower-bounded
symmetric form admits a lower-bounded closed extension (the
Friedrichs extension), but "closable" requires that the minimal
closed extension is also bounded below with the same constant —
equivalently, that the form does not "collapse" under closure.

The standard result (Reed–Simon II X.23, or similar): a
lower-semi-bounded symmetric form is closable **iff** its
lower-semi-continuous regularization agrees with the form on a
dense set. Equivalently, the Friedrichs extension is canonical
under weak additional hypotheses.

Paper 13's invocation of "Reed–Simon VIII.15 + positivity" is not
precise. VIII.15 (I would need to check exact numbering) is
either about closability of symmetric operators or about form
theory; the correct citation would be Reed–Simon II, Chapter X
(specifically X.3 and X.23 for form closability).

**A stronger concern:** lower-bounded symmetric forms on a
Hilbert space are **not always closable**. Reed–Simon II, Example
X.3.1 exhibits a positive symmetric form that is not closable.
The standard situation where closability holds is when the form
comes from a symmetric operator (via ⟨f, Tg⟩); in general forms,
one needs more care.

Paper 13 does not rule out the non-closable case. The assertion
"positivity implies closability" is false as stated.

### (3) Lower boundedness

CCM Proposition 3.3 (cited by Paper 13) says QW_λ is bounded
below. This is a finite-N statement. Its extension to Q_∞ requires
the lower bound to survive the limit, which is a separate matter.
The entry-by-entry convergence of matrix elements does not
automatically preserve lower-bounds.

A standard result: if Q_N is uniformly lower-bounded (with the
same constant) and converges pointwise on a dense set to Q_∞,
then Q_∞ is lower-bounded with the same constant. Paper 13
implicitly assumes uniform lower boundedness but does not state
it.

## Net assessment

Paper 13's Appendix C.4 is a **sketch** of KLMN closability that
is not rigorous. Specifically:

- Density in 𝒟(Q_∞) (not L²) is not established.
- Closability is claimed as a consequence of lower-boundedness,
  which is **not generally true**.
- Uniform lower boundedness across N is assumed, not proved.

The overall statement (Q_∞ produces a unique self-adjoint D_∞ via
Friedrichs) is *plausible* and probably correct, but the argument
as written has holes.

## Verdict on this subpoint

**Weakened.** KLMN closability is a load-bearing item in Layer 4.
Paper 13's verification is a sketch that contains at least one
incorrect implication ("positivity ⇒ closability"). A rigorous
proof would cite specific Reed–Simon results with correct numbers
and verify each of the three conditions (dense domain in the
form norm, minimal closed extension agrees with the form,
uniform lower boundedness) explicitly.

This is a standard-rigor gap, fixable but currently open.
