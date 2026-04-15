## Part E, Point 2: Convergence of the Sum

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

(a) The doubly exponential convergence is verified. With $C_k \sim k^\gamma$, $g_k^4 \sim 1/(b_0 k \ln 2)^2$, and $\hat{\Delta}_k^2 \sim 4^{-k}(1 + O(g_k^4))^k$: the accumulated $O(g_k^4)$ correction in $\hat{\Delta}_k$ gives $(1 + O(g_k^4))^k = (1 + O(1/k^2))^k \to e^{O(1/k)} \to 1$ as $k \to \infty$. More precisely, $\prod_{j=0}^{k-1}(1 + c g_j^4) \leq \exp(\sum c g_j^4) \leq \exp(\pi^2 c/(6(b_0 \ln 2)^2))$, a finite constant independent of $k$. So $\hat{\Delta}_k^2 \sim C_{scale} \cdot 4^{-k}$ with $C_{scale}$ a finite constant. The sum becomes $\sum_k k^{\gamma-2} C_{scale} 4^{-k} = C_{scale} \sum_k k^{\gamma-2} 4^{-k} < \infty$ for all $\gamma$.

The numerical estimate from the preprint: for SU(3) with $s = 2$ (the weaker bound), the total correction to $C = \Delta/\Lambda$ is ~1.2%, leaving $C_\infty \geq 0.98 C_0 > 0$. For $s = 4$ (the stronger bound), the correction is ~0.01%.

(b) The starting constant $C_0$ comes from the cluster expansion of Section 4. At $k = 0$: $\hat{\Delta}_0 = a_0 \Delta_0$ where $\Delta_0 > 0$ is the lattice mass gap (Theorem 4). The bound $|\langle 1|E_0(0)|1\rangle_c| \leq C_0 g_0^4 \hat{\Delta}_0^2$ is trivially satisfied at the starting scale because: (i) $\hat{\Delta}_0 \sim O(1)$ in lattice units, so $\hat{\Delta}_0^2 \sim O(1)$; (ii) $\|E_0\| \leq C g_0^4$ gives $|\langle 1|E_0(0)|1\rangle_c| \leq \|E_0\| \leq C g_0^4 = C g_0^4 \cdot 1 \leq C g_0^4 \hat{\Delta}_0^2$ when $\hat{\Delta}_0^2 \geq 1$ (or with an adjusted constant $C_0$ absorbing $1/\hat{\Delta}_0^2$ when $\hat{\Delta}_0 < 1$). The fixed-point convergence $C_k = C_* + (C_0 - C_*) \cdot 4^{-k}$ requires $C_0 < \infty$, which is established by the cluster expansion bounds of Section 4. This is stated in Section 5.4 and confirmed by the r06 referee.

**Impact on the claimed result:** None. The sum converges absolutely with enormous margin, and the starting constant is finite by construction.
