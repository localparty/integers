# CCM5 — No hidden RH assumption in CCM construction

**Claim:** CCM's operators are built without assuming RH; the
eigenvalue match at N = 6 is a computation, not an assumption.

**Pass criterion:** RH-free construction verified.

**Finding:** On Paper 13's account of CCM:
- The Weil distribution D(y) is built from the von Mangoldt
  function and gamma factor (primes, not zeros).
- E_N is defined by Fourier truncation on an interval.
- QW_λ^N is a matrix with hypergeometric/digamma entries.
- Eigenvalue-to-γ_n matching is a *result* of computation.

**No RH input in the construction.**

**Subtle concern:** the O(ρ^{−N}) rate in CCM Theorem 5.10(ii)
must be derived a priori (from CF theory), not a posteriori
(from fitting to {γ_n}). Paper 13 accepts this is a priori on
CCM's authority; a careful referee of the CCM paper would need
to verify.

**Status:** PASS (RH-free as far as Paper 13 can tell).

**Confidence:** 9/10.
