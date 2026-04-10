## Point D2(c): The BSD Formula at Rank 0

**The question:**
Once rank = 0 and Sha is finite, are all terms of the BSD formula computed and verified?

**Finding:**
The BSD formula at rank 0 is:
L(E, 1) = (|Sha| * Omega_E * prod c_p) / |E(Q)_tors|^2

Section 13.3 verifies this for E: y^2 = x^3 - x:
- |Sha| = 1
- Omega_E = Gamma(1/4)^2 / (2pi)^{3/2} ~ 2.62206
- c_2 = 4 (corrected from earlier draft per research/06)
- |E(Q)_tors| = 4
- RHS = 1 * 2.62206 * 4 / 16 = 0.65551
- L(E, 1) = 0.65551

The numerical match is exact. The Tamagawa number correction (c_2 = 4, not 1) was identified and fixed in the adversarial review (research/06).

The preprint also invokes Rubin (1991) for the general BSD formula at rank 0 for CM curves. Rubin's result establishes the p-part of BSD for CM curves at rank 0 (for p sufficiently large), which combined with explicit computations for small primes closes the formula.

**Verdict for this sub-question:**
SOUND -- All terms computed correctly. The numerical verification matches. The Tamagawa number correction was appropriately identified and fixed.
