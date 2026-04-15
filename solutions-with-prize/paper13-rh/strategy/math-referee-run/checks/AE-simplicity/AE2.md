# AE2 — Overlaps certified nonzero at N = 1, ..., 20

**Claim:** At λ = √14, min_k |⟨φ_k | a⟩| > 0 with ~10^{72} safety margin.

**Pass criterion:** rigorous certification at sufficient precision.

**Finding:**
- Paper 13 Appendix F.3 tabulates at N = 1, ..., 20:
  - gap ranges from 8e-2 (N=1) to 7.87e-35 (N=20).
  - min overlap ranges from 6.2e-1 to 9.4e-4.
  - 120-digit working precision; assembly error ~10^{-110}.
  - Eigenvector perturbation ~10^{-75} at N=20.
  - Safety margin = 9.4e-4 / 10^{-75} ≈ 10^{72}.

Verified arithmetic check (my computation): ratio is consistent
with claim (see computation-log.md C6).

**Status:** PASS. The certification is rigorous at mpmath's
reported precision.

**Concern:** The method scales badly in N because the gap
shrinks exponentially; at some N_max, 120-digit precision is
insufficient. N_max ≈ 35-40 by extrapolation.

**Confidence:** 9/10 for the finite certification.
