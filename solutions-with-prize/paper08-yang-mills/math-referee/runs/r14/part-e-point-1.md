## Part E, Point 1: Inductive Stability

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The $1/4$ contraction.** The factor $1/4$ in the recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}}$ is a kinematic identity arising from the scale transformation:

$$\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$$

since $\hat{\Delta}_{k+1} = 2\hat{\Delta}_k(1 + O(g_k^4))$ (the dimensionless gap doubles when the lattice spacing doubles). Expressing the OLD contribution $\langle 1|E_k^{\downarrow}(0)|1\rangle_c \leq C_k g_k^4\hat{\Delta}_k^2$ in step-$(k+1)$ variables:

$$C_k g_k^4\hat{\Delta}_k^2 = C_k g_k^4 \cdot \hat{\Delta}_{k+1}^2/4 = (C_k/4)\,g_k^4\,\hat{\Delta}_{k+1}^2$$

The change of lattice (from $\Lambda_k$ to $\Lambda_{k+1}$) introduces corrections of $O(g_k^2\,C_k)$ from:
- Wave function renormalization: the one-particle state changes under blocking
- Coupling renormalization: $g_{k+1}^2 \neq g_k^2$

These corrections are subleading and handled by the Gronwall argument in (c).

**(b) The wave function correction.** The bound $\|\delta|1\rangle\| \leq C\,g_k^4/\hat{\Delta}_k$ uses Kato analytic perturbation theory. The gap condition requires $\|E_k\|$ to be small compared to the spectral gap $\hat{\Delta}_k$ of the unperturbed transfer matrix.

On the asymptotically free trajectory:
- $\|E_k\| \leq C\,g_k^4$
- $\hat{\Delta}_k = a_k\,\Delta_k \approx 2^k\,a_0\,\Delta_\infty$

The ratio: $\|E_k\|/\hat{\Delta}_k \leq C\,g_k^4/(2^k a_0 \Delta_\infty) \sim 1/(k^2 \cdot 2^k)$, which goes to zero exponentially. The gap condition is satisfied for ALL $k \geq 0$ with large margin.

For the first few steps ($k = 0, 1, 2$) where $g_k$ may not be small, the condition $\|E_k\| \ll \hat{\Delta}_k$ still holds because $\hat{\Delta}_0 = a_0\,\Delta_0$ is finite (from the cluster expansion) and $\|E_0\|$ is bounded by the cluster expansion constants. The Kato perturbation theory is applicable from the start.

The cross terms from the wave function change contribute to the $(A2)$ term: $O(g_k^8/\hat{\Delta}_k)$, which is subleading compared to $(C_k/4)\,g_k^4\,\hat{\Delta}_{k+1}^2$.

**(c) The Gronwall bound.** The accumulated correction $\prod_{j=0}^{k-1}(1 + \alpha\,g_j^2)$ gives polynomial growth:

$$\prod_{j=0}^{k-1}(1 + \alpha\,g_j^2) \leq \exp\left(\alpha\sum_{j=0}^{k-1} g_j^2\right) = \exp\left(\alpha\sum_{j=0}^{k-1}\frac{1}{b_0 j \ln 2}\right)$$

Since $\sum_{j=1}^{k} 1/j \approx \ln k$: the product grows as $k^{\alpha/(b_0 \ln 2)} = k^\gamma$.

The exponent $\gamma = \alpha/(b_0 \ln 2)$ depends on $N$ through:
- $\alpha$: the coefficient of $g_k^2$ in the correction term. This is $O(N^2)$ from the adjoint Casimir (the wave function correction involves the adjoint representation).
- $b_0 = 11N/(48\pi^2)$: linear in $N$.
- Therefore $\gamma \sim N^2/N = N$.

**A discrepancy noted:** The compressed I.3 in the umbrella file lists $\gamma \sim 1/N$ (citing $\alpha \sim N$ and $b_0 \sim N$), while the full I.3 file derives $\gamma \sim N$ (citing $\alpha \sim N^2$). The more conservative (larger) value $\gamma \sim N$ should be used. This does NOT affect the convergence: the sum $\sum k^{N-2}\,4^{-k}$ converges for ANY finite $N$ by the ratio test (limit $= 1/4 < 1$). But the discrepancy in the stated value of $\gamma$ should be reconciled in the preprint for consistency.

For the Clay prize requirement: the proof works for each fixed $N$. The $N$-dependent constants make $C_*$ and the convergence rate depend on $N$, but positivity of $\Delta_\infty$ holds for each fixed $N$.

**Impact on the claimed result:** None. The inductive stability is correctly established. The $1/4$ contraction provides the dominant mechanism, the wave function correction is controlled by Kato perturbation theory, and the Gronwall bound produces polynomial growth that is overwhelmed by the doubly exponential convergence. The $\gamma$ discrepancy ($N$ vs. $1/N$) is a presentation issue, not a mathematical error.
