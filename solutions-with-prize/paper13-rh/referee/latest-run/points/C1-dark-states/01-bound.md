# C1.01: The Bound

The bridge projector diagonal element is c_n^{(k)} = (1/k)(1 - w^k)/(1 - w) where w = exp(-2*pi*i/k) * p^{-(1/2+i*gamma_n)}.

|w| = p^{-1/2} < 1 for all primes p >= 2.
|w^k| = p^{-k/2} < 1.
Therefore 1 - w^k != 0 and 1 - w != 0, so c_n^{(k)} != 0.

**Assessment:** This is elementary and correct. The bound is trivially satisfied.

For off-line zeros at s = 1/2 + delta + i*gamma with delta > 0, |w| = p^{-(1/2+delta)} < p^{-1/2}, giving an even tighter bound. For -1/2 < delta < 0, |w| = p^{-(1/2+delta)} < 1 since 1/2 + delta > 0.

**Verdict: CORRECT.** The bound is elementary and covers the entire critical strip.
