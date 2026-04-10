## Point A3(a): Meyer's Original Result

**The question:**
Meyer's theorem for Q states that distributional eigenstates of the BC operator include zeros of zeta(s). What is the precise statement? Does Meyer prove this for zeta(s) or for a broader class of L-functions?

**Finding:**
The preprint cites "Meyer 1997" for the spectral inclusion. Meyer's work (specifically in the framework of Connes' 1999 trace formula approach) constructs distributional eigenstates of the BC Hamiltonian whose eigenvalues are the imaginary parts of the non-trivial zeros of zeta(s). This uses the explicit formula (Weil's version) which relates sums over zeros to sums over primes.

Meyer's original result is specifically for the Riemann zeta function zeta(s) and the original Bost-Connes system over Q. It does not directly address Hecke L-functions or Dedekind zeta functions of number fields. The construction relies on:
1. The explicit formula for zeta(s)
2. The Euler product structure
3. The distributional framework on the BC algebra

The preprint (Proposition 3.6) claims the extension to zeta_K is "direct" because zeta_K also has an explicit formula, an Euler product, and a functional equation. This is the right structural argument -- Meyer's proof depends on these general properties, not on specifics of Q.

However, the published record of Meyer's theorem for general Dedekind zeta functions is thin. The extension is "expected" but the referee should note that a fully detailed proof for zeta_K in the Ha-Paugam setting, while structurally clear, may not be written down in the literature in the required generality.

**Verdict for this sub-question:**
CLOSABLE GAP -- Meyer's original result is for zeta(s) over Q. The extension to zeta_K(s) over Q(i) follows the same structural argument (explicit formula + Euler product), but the detailed proof in the Ha-Paugam setting should be written out explicitly. The gap is closable with approximately 1 page of careful argument.
