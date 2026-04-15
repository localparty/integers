## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The overlap region.**

The precise coupling ranges:
- **Cluster expansion:** converges for all $\beta < \beta_{\max}(a) = m_1 a / 6 - \ln(c_d K C_0^{1/6})$. In the physical regime, $\beta_{\max} \sim 10^{14}$.
- **Balaban's RG:** applies for $g_0^2$ sufficiently small, i.e., $\beta = 2N/g_0^2$ sufficiently large. The explicit threshold is $g_0^2 \leq g_{\max}^2$ where $g_{\max}$ is determined by Balaban's small-field condition and polymer expansion convergence. For SU(3), this gives $\beta \gtrsim 10$ (i.e., $g_0^2 \lesssim 0.6$).

The overlap region is $10 \lesssim \beta \lesssim 10^{14}$, which is enormous. All physically relevant couplings ($\beta \sim 6$ in typical lattice QCD simulations) lie within the cluster expansion domain, and all perturbatively accessible couplings ($\beta \gg 1$) lie within Balaban's domain.

There is an explicit $\beta_{\min}^{\mathrm{Balaban}}$ below which Balaban's construction does not apply (where $g_0^2$ is too large for the small-field expansion). This is not a problem because:
1. The cluster expansion provides $\Delta_0 > 0$ for all $\beta < 10^{14}$
2. The RG is needed only for the continuum limit (sending $a \to 0$ at fixed physics), which requires $\beta \to \infty$ along the asymptotically free trajectory

**(b) The transition.**

At $k = 0$, the coupling $g_0$ may not be small. The first few RG steps ($k = 0, 1, 2, \ldots$) may have $g_k^4 = O(1)$, where the perturbative operator classification is not directly applicable.

Section 5.7, Remark 1 handles these initial steps explicitly: the cluster expansion (which does not require $g_k$ to be small) provides:
1. $\Delta_k > 0$ at each initial step
2. $C_k < \infty$ (the form factor bound is finite)
3. Connected correlation functions decay exponentially

The mass gap shift at these initial steps is bounded by the cluster expansion without invoking the dimension-6 classification. There are finitely many such steps (say $k < k_0$), and their total contribution to the mass gap sum $\sum_k \delta C_k$ is a finite constant.

For $k \geq k_0$ (where $g_k$ is small enough for Balaban's perturbative analysis), the stability of deviation order argument and the spectral lemma apply. The transition from the "cluster expansion regime" to the "Balaban RG regime" is rigorous: both provide the required inputs (mass gap and form factor bounds) in their respective domains, and the overlap ensures continuity.

**Impact on the claimed result:**

None. The coupling regimes overlap extensively, and the transition between them is explicitly handled. The first few non-perturbative RG steps are controlled by the cluster expansion, which requires no perturbative assumptions.
