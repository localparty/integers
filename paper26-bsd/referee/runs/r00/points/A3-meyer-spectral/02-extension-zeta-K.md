## Point A3(b): Extension to zeta_K(s)

**The question:**
The extension from zeta(s) to zeta_K(s) over Q(i) requires replacing the rational BC system with the Ha-Paugam system. Is the spectral inclusion theorem proved for this extension, or is it assumed by analogy?

**Finding:**
The preprint (Proposition 3.6) proves the extension by appeal to the explicit formula for zeta_K:

    sum_rho x^rho = x - sum_a Lambda_K(a) * 1_{N(a) <= x} + O(1)

where Lambda_K is the von Mangoldt function for K and rho runs over non-trivial zeros of zeta_K(s). The proof states: "The distributional eigenstates are constructed exactly as in Meyer's original argument, with the rational von Mangoldt function replaced by Lambda_K."

This is a sketch, not a complete proof. The claim that "the structure of the argument depends only on the existence of an Euler product and a functional equation for zeta_K(s), both of which hold" is correct in spirit but would benefit from explicit verification of each step.

Key steps that need verification:
1. The explicit formula for zeta_K is standard (Neukirch, VII).
2. The distributional eigenstate construction uses the explicit formula to create functionals on the BC algebra whose eigenvalue is determined by a zero rho.
3. The Ha-Paugam algebra admits the same distributional framework as the classical BC algebra.

Points 1 and 2 are standard. Point 3 is where the work lies: one needs to verify that the Ha-Paugam algebra over Q(i) supports the same distributional construction as the classical BC algebra. For h_K = 1 fields (where the algebra has the same structural features as the classical case), this is expected to work.

**Verdict for this sub-question:**
CLOSABLE GAP -- The extension is structurally sound but the proof is sketched rather than written in full detail. Closable with approximately 2-3 pages of careful argument verifying the distributional construction in the Ha-Paugam setting.
