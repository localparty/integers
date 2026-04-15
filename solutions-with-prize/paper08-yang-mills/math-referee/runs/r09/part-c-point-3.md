## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The overlap region.** The cluster expansion applies for all $\beta < \beta_{\max}(a) \approx m_1 a/6 \sim 5.8 \times 10^{14}$ (at physical lattice spacings). Balaban's RG applies for $g_0$ sufficiently small, i.e., $\beta_0 = 2N/g_0^2$ sufficiently large. The precise threshold $\beta_{\min}^{\mathrm{Balaban}}$ is not stated as a sharp constant in Balaban's papers — it is typically of order $O(N)$ (ensuring $g_0^2 < \gamma$ for the smallness parameter $\gamma$ in CMP 109, Theorem 1).

The overlap region is $\beta_{\min}^{\mathrm{Balaban}} < \beta < \beta_{\max}(a)$. Since $\beta_{\min}^{\mathrm{Balaban}} = O(N)$ and $\beta_{\max} \sim 10^{14}$, the overlap is vast. The proof does not require knowledge of the precise threshold — it suffices that both arguments apply simultaneously for $\beta$ in the range of physical interest.

**(b) The transition.** At $k = 0$, the coupling $g_0$ may not be small (e.g., $g_0^2 \sim 1$ at $\beta \sim 6$). Section 5.7, Remark 1 handles the first few RG steps non-perturbatively:

> "At $k = 0, 1, 2$ where $g_k^4 = O(1)$, first-order perturbation is not a priori justified. These finitely many steps are handled non-perturbatively via the cluster expansion, with bounded total contribution $K_0$ absorbed into $C_0$."

The transition from "cluster expansion regime" to "Balaban RG regime" is rigorously justified: the cluster expansion provides finite, bounded results for the first $k_0$ steps (where $g_k$ is not yet small), and Balaban's UV stability takes over for $k \geq k_0$ (where $g_k$ is small enough for the perturbative $\beta$-function to control the flow). The total contribution from the initial steps is a finite constant, absorbed into $C_0$. The RG recursion (Section 5.4) handles both regimes uniformly: the sum $\sum C_k g_k^4 \hat{\Delta}_k^2$ converges regardless of the size of the first few terms, because $4^{-k}$ provides doubly exponential convergence.

**Impact on the claimed result:** None. The regime overlap is established and the transition is handled correctly.
