## Part A, Point 3: The Bogomolny Bound on the Lattice

**Weight:** LIGHT
**Verdict:** CLOSABLE GAP (Lüscher topological charge construction is invoked correctly but the small-field/large-field reduction relies on Balaban's framework whose own scope is partially conditional — see Point C1).

**Finding:**

(a) **Lattice instantons.** The preprint correctly recognizes that the Bogomolny bound is a continuum result and that lattice configurations need not have integer second Chern class. The fix is the Lüscher (1982) geometric construction (CMP 85), which assigns an integer topological charge $Q_L[U]$ to lattice configurations satisfying $\|1 - U_P\| < \epsilon_L$, where $\epsilon_L$ is a $G$- and $d$-dependent constant. Section 04.4, "Compatibility with the small-field condition" (lines 826–842) argues that Balaban's small-field condition $|F_{\mu\nu}| < g_k^{1-\epsilon}$ implies $\|1 - U_P\| < C a^2 g_k^{1-\epsilon} < \epsilon_L$ for $g_k$ small enough.

This argument is correct in structure but has two soft spots:

1. **The dependence on Balaban's small-field decomposition.** For the cluster-expansion regime of Theorem 4 (which uses NO Balaban RG, only the KK enhancement), the small-field/large-field decomposition is performed manually and the contribution from "rough" configurations is bounded by $O(e^{-c/g_k^{2\epsilon}})$. This is acceptable but the constant $c$ is N-dependent and needs to be tracked through the cluster expansion estimates. Not done explicitly.

2. **The transition $g_k \to g_0$ at $k = 0$ (the bare lattice).** The bare coupling $g_0$ may not be small, so the small-field condition is not automatic at the starting scale. Section 04.4 line 836 says "for $k < k_0$ by taking $a_0$ small enough" — but $a_0$ is the physical lattice spacing, fixed by the physics, not free. For the cluster expansion regime to cover $\beta < 10^{14}$, the small-field/large-field decomposition must be effective at the *coarse* lattice ($a_0 \gg r_3$) where $g_0$ is *large* (strong coupling). This is exactly the regime where the small-field condition is most fragile.

(b) **The restriction to $c_2 = 0$.** The "Corollary" in Section 04.4 (lines 805–860) addresses tunneling between sectors via the Bogomolny bound and gets the geometric series $1 - C e^{-4\pi^2 \beta/N}$, which is positive for $\beta > 0$. This is fine for $\beta$ large (weak coupling), but the cluster-expansion regime covers $\beta$ down to small values where $e^{-4\pi^2 \beta/N}$ is $O(1)$ and the bound is uninformative. In the strong-coupling regime, the topological-sector contribution should be controlled by the smallness of the Boltzmann factor $e^{-\beta s_P}$, not by the Bogomolny factor — but the preprint does not make this distinction.

**To close:** state explicitly that the small-field/large-field decomposition for the *bare* cluster expansion (Theorem 4) uses the cluster-expansion smallness $\beta < a_0/(2\sqrt{N} r_3)$ rather than Balaban's $g_k^{1-\epsilon}$ condition, and verify that Lüscher's $\epsilon_L$ threshold is satisfied throughout the cluster-expansion convergence window. **Difficulty: 1 page.**

**Impact on the claimed result:** Minor. The Bogomolny suppression is an *additional* contribution beyond the cluster expansion proper, and even if the topological-sector argument has soft spots, the lattice mass gap $\Delta_0 > 0$ in the trivial $c_2 = 0$ sector (which is what Theorem 4 actually proves) is independent of the Bogomolny bound. The Bogomolny argument is needed only to convert "$\sigma_0 > 0$ in the trivial sector" to "$\sigma > 0$ in the full theory". For Clay purposes (which require the *full* theory's mass gap, not the trivial-sector restricted theory), this gap matters but is closable.
