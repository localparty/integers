## Point B3(b): No Dark States

**The question:**
Confirm that |w^k| < 1 implies every eigenstate couples to every bridge.

**Finding:**
Proposition 6.2 states that the coupling is <psi|P_k^p|psi> = 1 - |w^k(p)|^2 > 0 since |w^k| < 1. This means the bridge projector P_k^p has strictly positive expectation value on every eigenstate psi.

The argument is correct: if the coupling were zero, we would need |w^k| = 1, which requires N(p)^{-k/2} = 1, i.e., N(p) = 1. But N(p) >= 2 for all primes, so this is impossible.

**Verdict for this sub-question:**
SOUND -- The dark-state impossibility follows from |w^k| < 1, which holds for all Gaussian primes.
