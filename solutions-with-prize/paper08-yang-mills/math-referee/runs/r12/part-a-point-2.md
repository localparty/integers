## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND (sub-point a, ADDRESSED); SOUND (sub-point b)

**[UPDATE]** Sub-point (a) addressed in the preprint. See revision note below.

---

**Finding:**

**(a) Transfer matrix estimate and the free-field approximation.** Theorem 2 (Section 4, Steps 1–4) derives the bond activity bound $|g_b| \leq C_0 e^{-m_1 a}$ via the following chain: (Step 1) expand the internal gauge field in Hodge eigenmodes; (Step 2) compute the Gaussian free-field propagator $G_n(a)$ for mode $n$ in the $k=0$ topological sector; (Step 3) establish $G_n(a) \leq (C_1/m_n a) e^{-m_n a}$ via the transfer matrix representation; (Step 4) sum over modes to bound $\langle |V^{\text{bond}}| \rangle_{k=0} \leq C_4 e^{-m_1 a}$, then conclude $|g_{\langle xy\rangle}| \leq C_0 e^{-m_1 a}$.

The gap is in the final step. Step 4 bounds the *free-field expectation* $\langle |V^{\text{bond}}| \rangle$ using Gaussian statistics for the internal modes. The cluster expansion requires a bound on the *actual bond activity* $g_\ell = e^{-V_\ell^{\text{bond}}} - 1$ for every field configuration in the support of the measure, not just its expectation. The estimate $|e^{-V} - 1| \leq |V|$ (valid for $|V| \leq 1$) requires $|V_\ell^{\text{bond}}|$ to be small pointwise, not merely its expectation to be small.

The gap closes as follows: in the small-field region $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$, the internal connection amplitude is bounded, so $V_\ell^{\text{bond}}$ is pointwise bounded. Outside $\Omega_s$, configurations are exponentially suppressed (Balaban, CMP 119) and contribute negligibly to the cluster expansion. Within $\Omega_s$, the internal connections have $|A_x| \leq C p(g_k)/r_3$, so $|V_n^{\text{bond}}| \leq 2\|A_x\|\|A_{x+\hat\mu}\| \leq C'' p(g_k)^2 G_n(0)/r_3^2$, and the KK mode sum reproduces the $e^{-m_1 a}$ bound via the spectral gap. This argument is not written in the preprint but is standard in the constructive QFT literature (Seiler 1982, Ch. 4). Closing requires: one paragraph specifying that the bond activity bound holds in $\Omega_s$ using the pointwise small-field bound on $|A_x|$, not just the free-field expectation. Difficulty: **1 paragraph**.

The transfer matrix on $\mathbb{CP}^{N-1}$ is trace-class (it is a compact manifold, so the Laplacian has discrete spectrum and the heat kernel is trace-class; the propagator bound follows from standard spectral estimates). Boundary corrections from the compact geometry are absorbed into the spectral decomposition; there are no finite-volume corrections beyond the discrete spectrum, which is fully accounted for in the eigenmode expansion.

**(b) The constant $C_0$ and its $N$-dependence.** Section 4, Step 4 states: "$C_0 = C_4$ depends on $N$ (through the Weyl asymptotics and the dimension of the adjoint representation) but not on $\beta$ or $a/r_3$." The Weyl asymptotics on $\mathbb{CP}^{N-1}$ give $d_n \sim n^{N-2}$ and $m_n \sim n/r_3$, so the remaining sum $\sum_{n\geq1} d_n e^{-(m_n-m_1)a}$ converges to a constant that grows with $N$ (roughly as a Bessel function of order $N-2$). For large $N$, $C_0 = C_0(N)$ grows, but only polynomially in $N$ for fixed $a/r_3$.

The cluster expansion convergence condition is $2\beta < (m_1 a/6) - \ln(c_d K C_0^{1/6})$. With $m_1 a/6 \sim 10^{14}$ at physical scales, even $C_0 \sim N^{100}$ would reduce the convergence threshold by only $100 \ln N / 6$, which is negligible compared to $10^{14}$. The $N$-dependent constant cannot compromise the expansion in the physical regime. SOUND.

**[REVISION NOTE — Sub-point (a) ADDRESSED.]** The revised preprint clarifies that $|g_b|$ in Theorem 2 and the KP criterion refers to the **integrated bond activity** (after integrating the internal fields $A_x$ against the free Gaussian measure), not the pointwise value of $e^{-V^{\mathrm{bond}}}-1$ for a specific field configuration. The cluster weight $\phi(\mathcal{C})$ already includes the integration $\int \prod_x dA_x\,e^{-S_{\mathrm{int}}(x)}$, so the bound $\langle|e^{-V}-1|\rangle_{k=0} \leq \langle|V|\rangle_{k=0} \leq C_4 e^{-m_1 a}$ is the correct quantity for the KP criterion. The free-field expectation is exactly what appears in the cluster weight, not a surrogate for a missing pointwise bound. The Step 4 exposition now makes this explicit, and the boxed bound is labeled "integrated." Additionally, the eigenvalue and mass formula are corrected to $m_1 = 2\sqrt{N}/r_3$ from $\lambda_1^{(1)} = 4N/r_3^2$ (consistent with the A1 commit fix).

**Impact on the claimed result:** Gap is now closed. No remaining gap in Theorem 2 sub-point (a).
