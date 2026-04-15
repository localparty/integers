# BG1 — Teschl form-boundedness with a = 0 < 1

**Claim:** The relative form bound a = 0 holds (form-small in the strongest sense).

**Pass criterion:** Teschl Lemma 2.7 correctly applied; a = 0 means the perturbation is form-bounded with relative bound zero.

**Finding:**
- Paper 13 Theorem 9.3 gives |δ_N[f]| ≤ ‖Δ_N‖_op · ‖f‖², which
  matches Teschl's (ii) with a = 0, b = ‖Δ_N‖_op.
- **But**: δ_N is defined as Q_N − P_N Q_0 P_N (the Galerkin
  residual), **not** Q_N − Q_∞. Teschl Lemma 2.7 asks for the
  bound on the common form domain, where Q_N − Q_∞ is the
  natural difference.
- On range(P_N), the two definitions coincide.
- Outside range(P_N), Paper 13's "Δ_N" is effectively zero
  (the Galerkin residual doesn't see vectors orthogonal to
  range(P_N)), whereas the true Q_N − Q_∞ is not.
- Paper 13 relies on the common form domain being exhausted by
  the growing range(P_N), which is true in the limit but
  requires the form domain to be identified with the direct
  limit.

**Additional concern:** Whether Teschl Lemma 2.7 applies to
Galerkin sequences on varying Hilbert spaces is **not explicitly
checked** against Teschl's actual paper.

**Status:** CONDITIONAL — the form bound is established on
range(P_N) (where it equals zero by definition), but the
translation to Teschl's "common form domain" hypothesis is
informal.

**Confidence:** 6/10. See points/B3-teschl-boegli/01-gsrc-verification.md.
