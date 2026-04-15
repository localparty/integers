# B1.03: Exactness of the Formula

**The claim:** The cocycle shift formula (1 - p^{-2*delta})/(p - p^{-2*delta}) is EXACT, not an approximation.

**Assessment:** As an algebraic formula derived from the ratio of Euler factors, the expression is indeed exact. The derivation (Step 4 to Step 5) involves no approximation. The Taylor expansion in Corollary 5.3 is provided for illustration but is not needed.

**Properties (all correct):**
- Vanishes iff delta = 0 (numerator 1 - p^{-2*delta} = 0 iff delta = 0)
- Strictly monotone increasing (derivative positive)
- Pole at delta = -1/2 (edge of critical strip, no zeros there)
- Analytic in the open critical strip

**Verdict: CORRECT.** The formula is exact and its properties are correctly stated. The concern is not with the formula itself but with its interpretation as a cocycle shift (see B1.01 and B1.02).
