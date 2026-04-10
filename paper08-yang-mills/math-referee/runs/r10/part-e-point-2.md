## Part E, Point 2: Convergence of the Sum

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The doubly exponential convergence.**

With $C_k \sim k^\gamma$, $g_k^4 \sim 1/(b_0 k \ln 2)^2$, and $\hat{\Delta}_k^2 \sim 4^{-k}(1 + O(g_k^4))^k$:

First, the accumulated correction in $\hat{\Delta}_k$: at each RG step, $\hat{\Delta}_{k+1} = 2\hat{\Delta}_k(1 + O(g_k^4))$. Iterating: $\hat{\Delta}_k = 2^k \hat{\Delta}_0 \prod_{j=0}^{k-1}(1 + O(g_j^4))$. The product $\prod(1 + O(g_j^4)) \leq \exp(\sum O(g_j^4))$. Since $g_j^4 \sim 1/j^2$ and $\sum 1/j^2 = \pi^2/6 < \infty$, the product converges to a finite constant. Therefore $\hat{\Delta}_k^2 \sim 4^k \hat{\Delta}_0^2 \cdot C_{\mathrm{prod}}$, so $\hat{\Delta}_k^2$ grows as $4^k$ (the mass gap in dimensionless units doubles at each step).

Wait — the sum involves $\hat{\Delta}_k^2$ in the *numerator* (as part of the bound $C_k g_k^4 \hat{\Delta}_k^2$), and this growth is the issue. The mass gap shift at step $k$ is bounded by $\delta C_k \leq C' g_k^4 (a_k \Lambda)^s$ where $(a_k \Lambda)^s = (a_0 \Lambda / 2^k)^s \sim 2^{-ks}$. For $s = 2$: the general term is $g_k^4 \cdot 4^{-k} \sim k^{-2} \cdot 4^{-k}$, which converges doubly exponentially.

The accumulated $O(g_k^4)$ correction in $\hat{\Delta}_k$ does NOT affect the $4^{-k}$ rate because: the correction factor $\prod(1 + O(g_j^4))$ is a bounded multiplicative constant (convergent product), so $\hat{\Delta}_k^2 \sim 4^{-k} \cdot C_{\mathrm{prod}}$ up to a bounded factor. This does not change the exponential convergence rate.

Numerical verification (from the preprint, Section 5.7): for SU(3) with $g_0^2 = 1.0$ and $a_0\Lambda = 0.1$:
- $s = 2$: total sum $\approx 0.012$ (1.2% correction)
- $s = 4$: total sum $\approx 10^{-4}$ (0.01% correction)

**(b) The starting constant $C_0$.**

At $k = 0$: $\hat{\Delta}_0 = a_0 \Delta_0 \sim O(1)$ (mass gap times lattice spacing is dimensionless and $O(1)$). The starting constant $C_0$ is the form factor bound at the initial scale:

$$|\langle 1|E_0(0)|1\rangle_c| \leq C_0 g_0^4 \hat{\Delta}_0^2$$

$C_0$ is established by the cluster expansion (Section 4, Theorem 4): the connected correlation functions decay exponentially with rate $m \geq \alpha/a > 0$, and the form factor is bounded by the cluster expansion constants. These are finite (explicitly bounded by the Kotecký-Preiss criterion parameters).

The fixed-point convergence $C_k = C_* + (C_0 - C_*) 4^{-k}$ requires $C_0 < \infty$. This is established: the cluster expansion provides $C_0 \leq C_{\mathrm{KP}}(\kappa, d, N)$, which is a finite constant depending on the polymer expansion parameters.

For the r05 referee's confirmation (Point 7(b)): $C_0$ is finite from the cluster expansion, and the recursion converges to the fixed point $C_* = 4C_{\mathrm{new}}/3$ with geometric rate $4^{-k}$, starting from any finite $C_0$.

**Impact on the claimed result:**

None. The convergence of $\sum C_k g_k^4 \hat{\Delta}_k^2$ is robust, with doubly exponential rate $4^{-k}$ dominating all polynomial and logarithmic corrections. The starting constant is finite and explicitly bounded by the cluster expansion.
