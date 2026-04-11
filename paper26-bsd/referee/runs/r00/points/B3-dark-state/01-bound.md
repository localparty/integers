## Point B3(a): The Bound

**The question:**
Verify |w^k| for specific Gaussian primes.

**Finding:**
For (1+i) with norm 2: |w^k| = 2^{-k/2}. At k=2: 2^{-1} = 0.5. At k=6: 2^{-3} = 0.125. All < 1.
For (2+i) with norm 5: |w^k| = 5^{-k/2}. At k=2: 5^{-1} = 0.2. All < 1.
For inert prime (3) with norm 9: |w^k| = 9^{-k/2}. At k=2: 9^{-1} = 0.111. All < 1.

The minimum norm among Gaussian primes is N(1+i) = 2, the ramified prime above 2. Since all k >= 1 and N(p) >= 2, we have N(p)^{-k/2} <= 2^{-1/2} = 0.707 < 1.

The numerical table in Proposition 6.1 is consistent with these calculations.

**Verdict for this sub-question:**
SOUND -- Elementary arithmetic confirms the bound for all Gaussian primes.
