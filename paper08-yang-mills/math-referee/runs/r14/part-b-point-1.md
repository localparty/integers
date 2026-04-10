## Part B, Point 1: Cluster Expansion Convergence

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Kotecky-Preiss criterion.** The Kotecky-Preiss criterion (CMP 103, 1986) requires: for all polymers $\gamma_0$, $\sum_{\gamma \sim \gamma_0} |w(\gamma)|\,e^{a(\gamma)} \leq a(\gamma_0)$, where the sum runs over incompatible polymers. The preprint verifies this with:

- Polymer weights bounded by $|\phi(C)| \leq (K\,\max|f_P|\,C_0^{1/6}\,e^{-m_1 a/6})^{|C|}$
- The $e^{-m_1 a/6}$ factor uses $|B_C| \geq |S_C|/6$ on the $d = 4$ hypercubic lattice (each bond is shared by at most 6 plaquettes)
- The Kotecky-Preiss weight function $a(C) = \alpha|C|$ with exponential weight $\alpha > 0$
- Convergence when $2\beta + \alpha < m_1 a/6 - \ln(c_d K C_0^{1/6})$

The lattice animal constant $c_d$ for $d = 4$ is known and finite ($c_4 \approx 6.8$; more precisely, the number of lattice animals of size $n$ containing a fixed site grows as $\lambda^n$ with $\lambda \approx 6.77$ for the 4D hypercubic lattice). The combinatorial bound is correct.

The decay rate $\kappa$ depends on $N$ through $m_1(N) = 2\sqrt{N}/r_3$ and $C_0(N)$. For fixed $N$, $\kappa > 0$. The $\kappa$ in Balaban's polymer expansion (CMP 109, Theorem 1) is $k$-independent, as verified by the r03 referee.

**(b) Physical regime coverage.** In the physical regime ($a/r_3 \sim 10^{15}$), $\beta_{\max} \sim \sqrt{N}\,a/(6r_3) \sim 10^{14}$. The cluster expansion covers all $\beta < \beta_{\max}$. Balaban's RG requires $g_0$ sufficiently small (equivalently, $\beta > \beta_{\min}^{\mathrm{Balaban}}$ with $\beta_{\min}^{\mathrm{Balaban}} = O(1)$). The overlap region $\beta_{\min}^{\mathrm{Balaban}} < \beta < \beta_{\max}$ is enormous — spanning 14 orders of magnitude.

The RG trajectory starts at some $\beta_0$ in the overlap region. For the first few steps ($k = 0, 1, 2$) where $g_k$ may not be small, the cluster expansion bounds provide non-perturbative control (Section 5.7, Remark 1). The transition to Balaban's perturbative regime is seamless because the cluster expansion already establishes $\Delta_0 > 0$ and all the bounds needed as initial conditions for the RG recursion.

**(c) Connected function bounds.** Theorem 2 gives exponential decay of connected correlators: $|\langle O(x) O(y)\rangle_c| \leq C\,e^{-m|x-y|}$. The decay rate $m$ depends on $m_1 a$ and $\beta$, not on the lattice spacing $a$ separately. The cluster expansion constants depend on the combination $m_1 a$ (which is fixed in the physical regime) and $\beta$ (which varies). They are $a$-independent in the sense that they do not depend on the UV cutoff beyond what enters through $m_1 a$.

The starting condition $C_0$ for the RG recursion is derived from the cluster expansion bound on $|\langle 1|E_0(0)|1\rangle_c|$, which is finite and explicitly bounded for each fixed $N$.

**Impact on the claimed result:** None. The cluster expansion convergence is rigorously established via the Kotecky-Preiss criterion with explicit bounds. The overlap with Balaban's RG regime is verified quantitatively.
