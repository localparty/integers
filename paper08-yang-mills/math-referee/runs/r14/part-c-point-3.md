## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The overlap region.** The two regimes are:

- **Cluster expansion (Section 4):** Valid for $\beta < \beta_{\max}(a) = m_1 a/6 - \ln(c_d K C_0^{1/6})$. At physical parameters ($a/r_3 \sim 10^{15}$): $\beta_{\max} \sim 10^{14}$.
- **Balaban's RG (Section 5):** Valid for $g_0$ sufficiently small, i.e., $\beta > \beta_{\min}^{\mathrm{Balaban}}$ with $\beta_{\min}^{\mathrm{Balaban}} = O(1)$ (a specific finite number depending on $N$, but not on $a$).

The overlap is the enormous range $\beta_{\min}^{\mathrm{Balaban}} < \beta < \beta_{\max} \sim 10^{14}$. There is no gap between the two regimes: the cluster expansion extends to extremely large $\beta$ (due to the KK mass enhancement), while Balaban's RG begins at moderate $\beta$.

In the r05/r06 referee reviews, the regime overlap was verified as consistent: $\beta_{\mathrm{crit}} < \beta_0 < 10^{14}$ (r07 summary).

**(b) The transition from cluster expansion to RG regime.** At $k = 0$ (the starting lattice), the coupling $g_0 = \sqrt{2N/\beta_0}$ may be moderate (not necessarily small). The first few RG steps ($k = 0, 1, 2, \ldots$) may have $g_k^4 = O(1)$.

The preprint handles this in Section 5.7, Remark 1: the cluster expansion provides non-perturbative control for the initial steps. The key inputs from the cluster expansion are:

1. $\Delta_0 > 0$ (lattice mass gap from Theorem 4-5)
2. Exponential decay of connected correlators (initial condition for the RG)
3. Finite $C_0$ (starting constant for the recursion)

These are established for ALL $\beta$ in the cluster expansion domain, including moderate coupling. The transition to Balaban's perturbative RG regime happens when $g_k$ becomes sufficiently small (after several blocking steps, the effective coupling decreases due to asymptotic freedom). The number of non-perturbative steps is finite (typically $\sim 3$-$5$ steps), and the cluster expansion controls each one.

The transition is rigorously justified because: (i) the RG recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}} + O(g_k^2 C_k)$ holds for ALL $k$ (not just large $k$), and (ii) the cluster expansion provides the initial data ($C_0$, $\hat{\Delta}_0$) at $k = 0$.

**Impact on the claimed result:** None. The two regimes overlap massively, and the transition from cluster expansion control to Balaban's RG is seamless.
