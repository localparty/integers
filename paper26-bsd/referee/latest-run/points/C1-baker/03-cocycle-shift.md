## Point C1(c): The Cocycle Shift Formula and Integrality

**The question:**
The formula Delta c(delta) = (1 - N(p)^{-2delta}) / (N(p) - N(p)^{-2delta}) must vanish for delta != 0 only if certain integrality conditions are met. Walk through the argument.

**Finding:**
The integrality constraint (Proposition 7.3(v)) requires Delta c(delta) in (1/k)Z for the bridge of index k. This is because the Hasse invariant of the Brauer class takes values in (1/k)Z/Z.

For delta != 0, the shift Delta c(delta) is a continuous function that is strictly positive for delta > 0 and strictly negative for delta < 0 (Proposition 7.3(ii)). The first non-zero value in (1/k)Z is +/- 1/k.

At two bridge primes with norms N1, N2 and indices k1, k2, the simultaneous constraints are:
- Delta c_{k1}(delta) = m1/k1 for some non-zero integer m1
- Delta c_{k2}(delta) = m2/k2 for some non-zero integer m2

Taking the ratio and using the first-order approximation Delta c ~ (2 delta log N)/(N-1):

m1 k2 / (m2 k1) ~ (log N1 / log N2) * (N2 - 1)/(N1 - 1)

The left side is rational. The right side contains the transcendental factor log N1 / log N2. A transcendental number cannot equal a rational number. Contradiction.

The promotion from first-order to exact (Steps 5-6 of Proposition 8.6) uses the real-analyticity of the ratio Delta c_1/Delta c_2 and the Baker-theoretic constraint on the relationship between N1^{-2delta} and N2^{-2delta}. This is the most technical part of the argument.

**Assessment:** The first-order argument is clean and convincing. The promotion to the exact case in Steps 5-6 is more hand-wavy: it appeals to "the nonlinearity of the exact formula amplifies the transcendence obstruction" without giving a rigorous bound. However, the structure is correct: for the exact formula, one would need N1^{-2delta} and N2^{-2delta} to simultaneously satisfy polynomial equations with rational coefficients, which Baker's theorem prevents (since log N1 and log N2 are linearly independent over Q-bar).

**Verdict for this sub-question:**
CLOSABLE GAP -- The first-order argument is rigorous. The promotion to the exact case is correct in structure but would benefit from a more careful treatment. Closable with approximately 1 page of explicit Baker-theoretic bound.
