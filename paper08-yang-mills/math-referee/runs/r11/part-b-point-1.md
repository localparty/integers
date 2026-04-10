## Part B, Point 1: Cluster Expansion Convergence

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Kotecký-Preiss criterion.**

The Kotecký-Preiss theorem (CMP 103, 1986) requires: for each polymer $\gamma$, $\sum_{\gamma' \sim \gamma} |w(\gamma')| e^{a(\gamma') + b(\gamma')} \leq a(\gamma)$, where $\sim$ denotes incompatibility. The polymer weights in the preprint are bounded by $|w(\mathcal{C})| \leq (K C_0^{1/6} e^{2\beta} e^{-m_1 a/6})^{|\mathcal{C}|}$, where the factor $e^{-m_1 a/6}$ comes from each element of a cluster carrying suppression from the KK mass (since $|B_\mathcal{C}| \geq |\mathcal{C}|/6$ on the 4D hypercubic lattice).

The combinatorial bound on the number of lattice animals of size $n$ on the $d = 4$ hypercubic lattice is $\leq c_d^n$ with $c_d \leq Ce^7$ (Klarner's constant). The Kotecký-Preiss criterion then reduces to the convergence condition $2\beta + \alpha < m_1 a/6 - \ln(c_d K C_0^{1/6})$.

Does $\kappa$ depend on $N$? The polymer decay constant $\kappa$ in the KP criterion inherits from the KK mass: the effective $\kappa$ is controlled by $m_1 a/6 = \sqrt{N} a/(3r_3)$, which actually improves with $N$. The combinatorial factors ($c_d$, lattice coordination number) are $N$-independent. The constant $K$ (measure factor) and $C_0$ depend on $N$ but are absorbed into the logarithmic correction. For each fixed $N$, the convergence criterion is satisfied with enormous margin.

**(b) Physical regime coverage.**

At physical parameters: $m_1 a/6 = \sqrt{N} a/(\sqrt{3} r_3) \approx 5.8 \times 10^{14}$ for $N = 3$. The convergence condition requires $\beta < 5.8 \times 10^{14} - O(\ln N)$, which covers all practical couplings ($\beta \lesssim 10^2$ in lattice QCD simulations).

The RG trajectory starts at some $\beta_0$ and Balaban's RG applies for $g_0$ sufficiently small (large $\beta$). The overlap is enormous: the cluster expansion covers $\beta \in [0, \sim 10^{14}]$, and Balaban's weak-coupling analysis covers $\beta \gtrsim 10$ (equivalently $g_0^2 \lesssim 1$). The overlap region $\beta \in [10, 10^{14}]$ is vast. There is no gap between the two regimes.

The preprint (Section 5.7, Remark 1) notes that the first few RG steps ($k = 0, 1, 2$) may have $g_k$ not yet small. These steps are handled non-perturbatively by the cluster expansion, which applies for all $\beta$ up to $\sim 10^{14}$. The transition to the weak-coupling Balaban regime is smooth: once $g_k^2$ becomes small enough (after a few RG steps), the perturbative $\beta$-function controls the flow.

**(c) The connected function bounds.**

Theorem 2 provides $|g_b| \leq C_0 e^{-m_1 a}$ with $C_0$ independent of $a$ and $\beta$ (it depends only on $N$ and the geometry of $\mathbb{CP}^{N-1}$). The cluster expansion constants are $a$-independent because: (i) the KK mass $m_1 = 2\sqrt{N}/r_3$ is independent of $a$; (ii) the bond activity $|g_b| \leq C_0 e^{-m_1 a}$ improves as $a$ increases; (iii) the lattice animal constant $c_d$ depends only on dimension $d = 4$.

The starting condition $C_0$ for the RG recursion comes from the cluster expansion bound on the connected two-point function: $|\langle \mathcal{O}(x) \mathcal{O}(y)\rangle_c| \leq C e^{-m|x-y|}$ with rate $m > 0$ uniform in volume. This is a direct output of the converged cluster expansion and is indeed $a$-independent (for fixed $a/r_3$ ratio).

**Impact on the claimed result:** None. The cluster expansion convergence is established with enormous margin, and the constants have the claimed dependencies.
