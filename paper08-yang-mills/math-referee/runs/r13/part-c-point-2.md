## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: Balaban's construction decomposes configurations into small-field region Omega_s (polymer expansion converges) and large-field region Omega_l (exponentially suppressed).

**(a) The small-field condition.** The cutoff is |F_{mu nu}| < g_k^{3/4}, corresponding to epsilon = 1/4 in the notation p(g_k) = g_k^{1-epsilon}. This epsilon is a FIXED constant, independent of k. The choice epsilon = 1/4 is Balaban's (CMP 109, Section 2) and optimizes the trade-off between the small-field polymer expansion convergence and the large-field suppression.

The polymer expansion converges in Omega_s with the stated bounds. The analyticity properties (B1)-(B2) are established in Omega_s. The dimension-6 operator classification (from the exhaustive analysis of gauge-invariant operators) is valid for ANY analytic operator — it does not depend on the field strength being small. The classification is structural (based on symmetries and dimensional analysis), not dynamical.

In Omega_l: the contribution to the effective action is not decomposed into individual operators. Instead, the entire large-field contribution is bounded by ||delta H_k^{lf}|| <= C' e^{-c/g_k^{1/2}} (from the Boltzmann suppression of large field configurations). This bound enters the spectral lemma as an additive correction to the form factor.

**(b) Large-field suppression.** The large-field contribution O(e^{-c/g_k^{2 epsilon}}) = O(e^{-c/g_k^{1/2}}) is weaker than instanton suppression O(e^{-c/g_k^2}) but is still super-polynomially suppressed in g_k.

On the asymptotically free trajectory, g_k^2 ~ 1/(b_0 k ln 2), so:
- e^{-c/g_k^{1/2}} ~ e^{-c (b_0 k ln 2)^{1/4}} -> 0 super-polynomially in k
- g_k^4 hat{Delta}_k^2 ~ (1/k^2) 4^{-k}

The large-field term decays MUCH faster than g_k^4 hat{Delta}_k^2 (super-polynomial vs. polynomial-times-exponential). Specifically, e^{-c k^{1/4}} << k^{-2} 4^{-k} for all sufficiently large k. The RG recursion is not affected by the large-field contribution.

Quantitatively: for k = 10, e^{-c 10^{1/4}} ~ e^{-1.8c} while 4^{-10} ~ 10^{-6}. For k = 100, e^{-c 100^{1/4}} ~ e^{-3.2c} while 4^{-100} ~ 10^{-60}. The exponential 4^{-k} quickly dominates. For the first few steps where the comparison is tighter, the cluster expansion provides direct non-perturbative control (no reliance on the large-field/small-field split).

**(c) Gauge invariance of the decomposition.** The small-field condition |F_{mu nu}| < g_k^{3/4} is gauge-invariant on the lattice: the plaquette variable s_P = 1 - (1/N) Re Tr U_P is manifestly gauge-invariant (it involves the trace of the holonomy around a closed loop). The decomposition Omega_s vs. Omega_l is performed in terms of gauge-invariant quantities.

Balaban's axial gauge fixing is a computational device used WITHIN the small-field domain to organize the perturbative expansion. The gauge-fixing does not affect the definition of the small-field/large-field split, which is gauge-invariant. The final results (effective action, operator bounds) are gauge-invariant because the polymer expansion sums over all gauge orbits.

No error found. The large-field/small-field decomposition is a standard feature of Balaban's construction, with well-controlled bounds on both regions.

**Impact on the claimed result:** None. The decomposition is technically sound and the large-field contributions are negligible.
