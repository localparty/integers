## Part E, Point 2: Convergence of the Sum

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim is $\sum_K C_K g_K^4 \hat{\Delta}_K^2 < \infty$.

**(a) The doubly exponential convergence.** With $C_K \sim K^\gamma$, $g_K^4 \sim 1/(b_0 K \ln 2)^2 \sim 1/K^2$, and $\hat{\Delta}_K^2 = (a^* \Delta_{\mathrm{phys}})^2 \cdot 4^{-K}$: the sum is $\sum K^{\gamma-2} 4^{-K}$. This converges for all finite $\gamma$ because the exponential $4^{-K}$ dominates any polynomial $K^{\gamma-2}$.

Verified computationally (mpmath, 50-digit precision): for $\gamma = 0, 1, 2, 5, 10$, the sums are $0.268, 0.288, 0.333, 1.630, 2132.2$ respectively — all finite.

The estimate $g_K^4 \sim 1/(b_0 K \ln 2)^2$ uses one-loop running. Corrections from higher loops and non-perturbative effects modify this by multiplicative factors $(1 + O(g_K^2))^K$, which grow polynomially (absorbed into $K^\gamma$). The accumulated $O(g_K^4)$ correction in $\hat{\Delta}_K$ is bounded: $\hat{\Delta}_K^2 = (a^* \Delta_{\mathrm{phys}})^2 \cdot 4^{-K} \cdot (1 + O(g_K^4))^K$, and $(1 + O(1/K^2))^K \to 1$ as $K \to \infty$. So the $4^{-K}$ rate is not affected.

**(b) The starting constant $C_0$.** At $K = 0$, $\hat{\Delta}_0 = a^* \Delta_{\mathrm{phys}} \sim O(1)$ (since $a^*$ is the reference scale where the cluster expansion converges and $\Delta_{\mathrm{phys}}$ is the physical mass gap). The bound $C_0$ comes from the cluster expansion: $|\langle 1|E_0(0)|1\rangle_c| \leq \|E_0\| \leq C g_0^4$ from the cluster expansion convergence, so $C_0 \leq C g_0^4 / (g_0^4 \hat{\Delta}_0^2) = C/\hat{\Delta}_0^2 < \infty$. This is established in the Cluster–Balaban Handoff Lemma (Section 5.4.5): $C_K(k=0) \leq C_0^{\mathrm{cl}}$ uniformly in $K$ (conditional on (H1)–(H2)).

The fixed-point convergence $C_K = C_* + (C_0 - C_*) 4^{-K}$ requires $C_0 < \infty$, which is satisfied.

**Impact on the claimed result:**
No impact. The convergence is robust — the doubly exponential decay $4^{-K}$ overwhelms any polynomial growth.
