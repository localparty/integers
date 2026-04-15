## Part B, Point 1: Cluster Expansion Convergence

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Kotecký-Preiss criterion.**

The polymer weights are bounded by:
$$|\phi(\mathcal{C})| \leq (K C_0^{1/6} e^{2\beta} e^{-m_1 a/6})^{|\mathcal{C}|}$$

The per-element suppression incorporates: plaquette activity $|f_P| = |e^{-\beta s_P} - 1| \leq e^{2\beta}$, bond activity $|g_b| \leq C_0 e^{-m_1 a}$ (Theorem 2), and the geometric constraint $|B_{\mathcal{C}}| \geq |S_{\mathcal{C}}|/6$ (each plaquette touches at most 6 bonds on a 4D lattice).

The Kotecký-Preiss criterion requires, for exponential weight $a(\mathcal{C}) = \alpha|\mathcal{C}|$:
$$\sum_{\mathcal{C} \ni x} |\phi(\mathcal{C})|\,e^{\alpha|\mathcal{C}|} \leq \alpha$$

This is satisfied when:
$$2\beta + \alpha < \frac{m_1 a}{6} - \ln(c_d K C_0^{1/6})$$

where $c_d$ is the lattice animal constant for $d = 4$ (the number of connected subgraphs of size $n$ containing a given vertex grows as $c_d^n$ — this is a rigorous combinatorial bound).

The decay constant $\kappa$ for the polymer weights: effective $\kappa_{\mathrm{eff}} = m_1/6 - 2\beta/|\mathcal{C}| - \ln(c_d K C_0^{1/6})/|\mathcal{C}|$. For the convergence regime, $\kappa_{\mathrm{eff}} > 0$.

$N$-dependence: $K = K(N)$ is a finite $N$-dependent constant (from Haar measure normalization and Gaussian damping from $S_{\mathrm{int}}$). $C_0 = C_0(N)$ depends on $N$ through Weyl asymptotics. The lattice animal constant $c_d$ depends only on $d = 4$, not on $N$ or the gauge group. The combinatorial bound on the number of connected subgraphs of size $|X|$ on the 4D hypercubic lattice is standard ($c_4 \approx 18.1$ from rigorous bounds, or $c_4 \leq 4 \cdot (2d-1) = 28$ from cruder estimates).

The convergence criterion is correctly stated and correctly derived from the Kotecký-Preiss theorem.

**(b) Physical regime coverage.**

The convergence bound $\beta < \beta_{\max}(a) = m_1 a/6 - \ln(c_d K C_0^{1/6})$ covers $\beta_{\max} \sim m_1 a/6 \approx 5.8 \times 10^{14}$ in the physical regime ($a/r_3 \sim 10^{15}$).

The RG trajectory starts at some $\beta_0$ and proceeds to larger $\beta$ (weaker coupling). Balaban's construction applies for $g_0$ sufficiently small, i.e., $\beta = 2N/g_0^2$ sufficiently large. The overlap is explicit (r05 Point 7(c)): the cluster expansion requires $\beta < 10^{14}$, and Balaban requires $\beta \gtrsim 10$ (i.e., $g_0^2 \lesssim 0.6$ for SU(3)). The overlap region is $10 \lesssim \beta \lesssim 10^{14}$, which covers all physically relevant couplings.

There is no gap between the cluster expansion domain and the weak-coupling domain. The cluster expansion provides the starting mass gap $\Delta_0 > 0$; Balaban's RG then controls the continuum limit from any starting coupling in the overlap region. Section 5.7 Remark 1 handles the first few RG steps ($k = 0, 1, 2$) non-perturbatively via the cluster expansion when $g_k^4 = O(1)$. This is rigorous: the cluster expansion provides $\Delta_k > 0$ and $C_k < \infty$ at each initial step without requiring $g_k$ to be small.

**(c) The connected function bounds.**

Theorem 2 provides exponential decay of connected correlation functions: $|\langle \mathcal{O}(x)\mathcal{O}(y)\rangle_c| \leq C e^{-m|x-y|}$ with rate $m \geq \alpha/a > 0$ uniform in $L$ (lattice size). These bounds feed into:

1. **OS1 temperedness:** The bound $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ uses the cluster expansion constants, which are $a$-independent (they depend on $m_1 a/6 - 2\beta$, which is $O(10^{14})$ in the physical regime).

2. **The starting condition $C_0$ for the RG recursion:** At $k = 0$, $C_0$ is the form factor bound $|\langle 1|E_0(0)|1\rangle_c| \leq C_0 g_0^4 \hat{\Delta}_0^2$, obtained from the cluster expansion. This is finite and explicitly bounded (r05 Point 7(b) confirms this).

The cluster expansion constants are $a$-independent as claimed: they depend on the dimensionless ratio $m_1 a / (6\beta)$, and in the physical regime this ratio is $\sim 10^{14}/\beta \gg 1$.

**Impact on the claimed result:**

None. The cluster expansion is correctly applied with rigorous bounds. The physical regime coverage is complete, and the overlap with Balaban's domain is explicit.
