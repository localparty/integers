## Part E, Point 2: Convergence of the Sum

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The doubly exponential convergence.**

With $C_k \sim k^\gamma$, $g_k^4 \sim 1/(b_0 k \ln 2)^2$, and $\hat{\Delta}_k^2 \sim 4^{-k}$, the general term of the sum is:

$$C_k g_k^4 \hat{\Delta}_k^2 \sim k^{\gamma - 2} \cdot 4^{-k}$$

The ratio test gives $\lim_{k \to \infty} a_{k+1}/a_k = 1/4 < 1$, so the sum converges absolutely for any $\gamma$.

The estimates $g_k^4 \sim 1/(b_0 k \ln 2)^2$ follow from the AF running: $g_k^2 = 1/(b_0 k \ln 2) + O(1/(k \ln k)^2)$ for large $k$. The correction terms accumulate as $\hat{\Delta}_k^2 = 4^{-k} \prod_{j=0}^{k-1}(1 + O(g_j^4))$. The product $\prod(1 + O(g_j^4)) \leq \exp(\sum g_j^4) \leq \exp(C)$ converges because $\sum g_j^4 \sim \sum 1/(b_0 j \ln 2)^2 = \pi^2/(6(b_0 \ln 2)^2) < \infty$ (Basel series). Therefore $\hat{\Delta}_k^2 = 4^{-k} \cdot \Lambda_\infty^2$ with $\Lambda_\infty \in (0, \infty)$.

The accumulated correction does NOT affect the $4^{-k}$ rate — it merely multiplies by a finite constant $\Lambda_\infty^2$.

**(b) The starting constant $C_0$.**

At $k = 0$, $\hat{\Delta}_0 = a_0 \Delta_0$ where $\Delta_0$ is the lattice mass gap from Theorem 4. The cluster expansion gives $\Delta_0 > 0$ with explicit bounds depending on $\beta$, $a/r_3$, and $N$. The connected matrix element $\langle 1|E_0(0)|1\rangle_c$ is bounded by the cluster expansion: $|\langle 1|E_0(0)|1\rangle_c| \leq C_{\mathrm{clus}} g_0^4$ (from the exponential decay of connected correlators).

Therefore $C_0 = |\langle 1|E_0(0)|1\rangle_c|/(g_0^4 \hat{\Delta}_0^2) \leq C_{\mathrm{clus}}/\hat{\Delta}_0^2$. Since $\hat{\Delta}_0 > 0$ (from the lattice mass gap) and the cluster expansion gives exponential decay with rate $m > 0$, $C_0$ is finite.

The fixed-point convergence $C_k = C_* + (C_0 - C_*) 4^{-k} + O(g_k^2)$ shows that $C_k$ converges geometrically to $C_* = 4C_{\mathrm{new}}/3$ regardless of $C_0$, with the $1/4$ contraction driving convergence.

The positivity of the final mass gap requires $C_\infty = C_0 - \sum_{k=0}^\infty \delta C_k > 0$, where $\delta C_k$ is the mass gap shift at step $k$. The numerical estimates (Section 5.7, Remark) show that for SU(3) with $g_0^2 = 1.0$: the total correction is $\sim 1.2\%$ (for $s = 2$), so $C_\infty \geq 0.98 C_0 > 0$.

**Impact on the claimed result:** None. The convergence of the sum is guaranteed by the exponential factor $4^{-k}$, which is robust against all polynomial corrections.
