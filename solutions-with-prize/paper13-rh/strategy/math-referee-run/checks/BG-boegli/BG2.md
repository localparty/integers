# BG2 — KLMN closability of the limit form

**Claim:** Q_∞ is closable; KLMN gives a unique self-adjoint operator.

**Pass criterion:** dense domain (Chebyshev completeness proved), closability, bounded below.

**Finding (CRITICAL):** Paper 13 Appendix C.4 argues:

> "(2) Closability: Reed-Simon VIII.15 + positivity. Q_∞ is
> lower bounded (Q_∞ ≥ 0 from CCM Proposition 3.3) and hence
> closable."

**This implication is false in general.** A lower-bounded
symmetric form is **not automatically closable**. Reed-Simon II
Example X.3.1 exhibits a positive symmetric form that is **not
closable**. The correct statement is that a lower-bounded form
admits a Friedrichs extension (a closed, lower-bounded extension),
but this is not the same as the form itself being closable.

Additional concerns:
- "Dense domain": Paper 13 argues via Chebyshev completeness in
  L². But the form domain 𝒟(Q_∞) is the completion in the
  form norm, which is strictly smaller. L²-density of the
  cosine basis is not L²-density of 𝒟(Q_∞).
- Uniform lower-boundedness across N: assumed but not proved.

**Status:** WEAKENED — the argument as written contains an
incorrect implication. A rigorous version would correctly
distinguish "closable" from "has a Friedrichs extension" and
cite specific Reed-Simon results (likely from Chapter X).

**Confidence:** 5/10.
