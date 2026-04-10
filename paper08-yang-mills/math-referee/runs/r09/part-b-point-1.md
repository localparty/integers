## Part B, Point 1: Cluster Expansion Convergence

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Kotecký-Preiss criterion.** The convergence condition is stated precisely (Theorem 3, Section 4.3):

$$2\beta + \alpha < \frac{m_1 a}{6} - \ln(c_d K C_0^{1/6}).$$

The polymer weights are bounded by the product of plaquette activities $|f_P| \leq e^{2\beta}$ and bond activities $|g_b| \leq C_0 e^{-m_1 a}$ (Theorem 2). Every connected cluster on a 4D hypercubic lattice satisfies $|B| \geq |S|/6$ (geometric fact: each plaquette touches at most 6 bonds). Distributing the bond suppression over cluster elements gives the per-element bound $(KC_0^{1/6} e^{2\beta - m_1 a/6})^{|\mathcal{C}|}$.

The combinatorial bound on lattice animals of size $n$ uses $c_d^n$ with $c_d \leq Ce^7$ for $d = 4$ (Klarner-Rivest 1973). The precise value is immaterial: $c_d$ appears only inside a logarithm bounded by $m_1 a/6 \sim 10^{14}$.

The $N$-dependence of $\kappa$ enters through $C_0(N)$ and $K(N)$, both finite for each fixed $N$. Since these appear inside a logarithm dominated by $m_1 a/6$, the convergence condition is satisfied for all $N \geq 2$.

**(b) Physical regime coverage.** The cluster expansion covers $\beta < \beta_{\max}(a) \approx m_1 a/6 \sim 5.8 \times 10^{14}$ at physical lattice spacings. Balaban's RG applies for $g_0$ sufficiently small (i.e., $\beta_0$ sufficiently large). On the asymptotic freedom trajectory $\beta(a) = (2Nb_0)\ln(1/(a\Lambda))$, the value at $a \sim 10^{-16}$ m is $\beta \sim 6$, far below $\beta_{\max}$.

The overlap between the cluster expansion domain ($\beta < 10^{14}$) and the Balaban RG domain (large $\beta$, i.e., small $g_0$) is enormous. The crossover lattice spacing $a_{\mathrm{cross}} \sim 3.5 \times 10^{-29}$ m is where the cluster expansion ceases to apply, and Balaban's RG takes over. There is no gap between the two regimes — Section 5.7, Remark 1 handles the first few RG steps ($k = 0, 1, 2$) non-perturbatively via the cluster expansion.

**(c) The connected function bounds.** Theorem 4(c) gives exponential decay of connected correlators with rate $m \geq \alpha/a > 0$ uniformly in $L$. The cluster expansion constants ($C_0$, $K$, $c_d$) are $a$-independent as claimed: $C_0$ depends on $N$ and $r_3$ but not on $a$ or $\beta$; the lattice animal constant $c_d$ is a combinatorial constant of the hypercubic lattice; $K$ is a measure factor bounded by the compact group volume and Gaussian damping.

The starting condition $C_0$ for the RG recursion (Section 5.4) comes from the cluster expansion bound at $k = 0$: the connected matrix element is bounded by the cluster expansion with rate $\alpha > 0$. This is finite and $a$-independent for $a \gg r_3$.

**Impact on the claimed result:** None. The cluster expansion is correctly established with full coverage of the physical regime.
