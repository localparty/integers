## Point C2(b): Properties

**The question:**
Verify algebraically that Delta c(0) = 0 and Delta c(delta) != 0 for delta != 0 in (-1/2, 1/2).

**Finding:**
(i) At delta = 0: numerator = 1 - N(p)^0 = 1 - 1 = 0. So Delta c(0) = 0. Correct.

(ii) For delta > 0: N(p)^{-2delta} < 1, so numerator 1 - N(p)^{-2delta} > 0. Denominator N(p) - N(p)^{-2delta} > 0 (since N(p) >= 2 > 1 > N(p)^{-2delta}). So Delta c(delta) > 0 for delta > 0. By symmetry (or direct computation), Delta c(delta) < 0 for delta < 0. Hence Delta c(delta) = 0 iff delta = 0 on (-1/2, 1/2).

(iii) Pole: the denominator vanishes when N(p) = N(p)^{-2delta}, i.e., N(p)^{1+2delta} = 1, i.e., delta = -1/2. This is the boundary of the critical strip, outside the open interval (-1/2, 1/2). No poles in the relevant region.

(iv) The first-order expansion Delta c(delta) ~ 2 delta log(N)/(N-1) is correct by Taylor expansion of N^{-2delta} = 1 - 2delta log N + O(delta^2).

All properties are verified by elementary calculus.

**Verdict for this sub-question:**
SOUND -- All claimed properties are correct and verified algebraically.
