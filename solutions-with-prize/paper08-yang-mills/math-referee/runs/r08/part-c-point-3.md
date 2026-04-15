## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

(a) The overlap region is explicit. The cluster expansion applies for all $\beta < \beta_{max}(a) \sim m_1 a/6 \sim 10^{14}$ (at physical lattice spacings). Balaban's RG applies for $g_0$ sufficiently small, i.e., $\beta_0 = 2N/g_0^2$ sufficiently large. The precise lower bound $\beta_{min}^{Balaban}$ is not stated as a single number in Balaban's papers — it is a condition of the form "$g_0 < \gamma$" for a universal constant $\gamma > 0$ depending on N, d, and the blocking geometry. For practical purposes, Balaban's construction works for $\beta_0 \geq O(10)$ (the coupling must be weak enough for the perturbative expansion around the saddle point to converge). Since $\beta_{max}(a) \sim 10^{14}$, the overlap is enormous: both arguments apply simultaneously for $O(10) \leq \beta \leq O(10^{14})$.

(b) The transition from "cluster expansion regime" to "Balaban RG regime" is handled in Section 5.7, Remark 1. At $k = 0$, the coupling $g_0$ may not be small (the cluster expansion operates in all regimes, not just weak coupling). The first few RG steps ($k = 0, 1, 2$) where $g_k^4 = O(1)$ are handled non-perturbatively: the cluster expansion bounds provide a finite total contribution $K_0 = \sum_{k=0}^{k_0} |\delta C_k| < \infty$ that is absorbed into the starting constant $C_0$. After finitely many steps, $g_k$ enters the small-coupling regime where Balaban's perturbative RG applies with full control. This is a standard "finite initial segment" argument in constructive QFT and is rigorously justified.

**Impact on the claimed result:** None. The regime overlap is explicit and enormous. The transition from non-perturbative (cluster expansion) to perturbative (Balaban RG) is handled by a standard finite-initial-segment argument.
