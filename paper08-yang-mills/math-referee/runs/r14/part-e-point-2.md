## Part E, Point 2: Convergence of the Sum

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Doubly exponential convergence.** The sum $\sum_k C_k\,g_k^4\,\hat{\Delta}_k^2$ is bounded by:

With $C_k \sim C_* + (C_0 - C_*)\,4^{-k}$ (geometric convergence to fixed point $C_* = (4/3)C_{\mathrm{new}}$), including the Gronwall correction $C_k \leq C_*\,k^\gamma$:

$$\sum_k C_k\,g_k^4\,\hat{\Delta}_k^2 \leq C_*\sum_k k^\gamma \cdot \frac{1}{(b_0 k \ln 2)^2} \cdot (\text{contraction factor from recursion})$$

The "contraction factor from recursion" is the key: the $C_k$ recursion absorbs the $\hat{\Delta}_k^2$ growth through the $1/4$ contraction at each step. In the recursion variable $C_k$ itself, the bound on the mass gap change $|\delta C_k|$ involves $g_k^4$ times the RG-scale-dependent factor from the form factor bound.

The convergence is doubly exponential in the sense that:
- The $4^{-k}$ geometric convergence of $C_k$ to $C_*$ provides one exponential factor
- The $g_k^4 \sim 1/k^2$ provides polynomial suppression
- Combined: $\sum k^{\gamma-2}\,4^{-k}$ converges for ALL finite $\gamma$

By the ratio test: $a_{k+1}/a_k = [(k+1)/k]^{\gamma-2} \cdot 1/4 \to 1/4 < 1$. The series converges absolutely with ratio $1/4$.

The accumulated $O(g_k^4)$ correction in $\hat{\Delta}_k$ is controlled: $\hat{\Delta}_k = 2^k\hat{\Delta}_0\prod_{j=0}^{k-1}(1 + O(g_j^4))$. The product converges because $\sum g_j^4 \sim \sum 1/j^2 < \infty$ (Basel series). So $\hat{\Delta}_k = C_\Lambda\,2^k\,\hat{\Delta}_0$ with $0 < C_\Lambda < \infty$. The $4^{-k}$ rate from the recursion is NOT affected by these corrections.

**(b) The starting constant $C_0$.** At $k = 0$, the inductive hypothesis states $|\langle 1|E_0(0)|1\rangle_c| \leq C_0\,g_0^4\,\hat{\Delta}_0^2$. The constant $C_0$ is established from the cluster expansion (Section 4):

1. The cluster expansion gives exponential decay of connected correlators with rate $m = O(m_1)$.
2. The connected matrix element $\langle 1|E_0(0)|1\rangle_c$ is bounded by the cluster expansion constants.
3. Dividing by $g_0^4\hat{\Delta}_0^2$ gives $C_0$, which is finite for each $N$.

The fixed-point convergence $C_k = C_* + (C_0 - C_*)\,4^{-k}$ requires $C_0 < \infty$. This is established at $k = 0$ by the cluster expansion bounds.

The preprint's numerical estimate for SU(3) with $s = 2$: total correction to $C_\infty$ is $\sim 1.2\%$, confirming that $C_\infty \approx C_0 > 0$.

**Impact on the claimed result:** None. The sum converges with exponential rate $1/4$, which dominates any polynomial growth from $N$-dependent exponents. The starting constant $C_0$ is finite from the cluster expansion.
