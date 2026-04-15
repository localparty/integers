## Part A, Point 1: The Weitzenboeck Spectral Gap on $\mathbb{CP}^{N-1}$

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The spectral bound.** The Weitzenboeck formula $\Delta_1^H = \nabla^*\nabla + \mathrm{Ric}$ on 1-forms is correctly applied. For $(\mathbb{CP}^{N-1}, g_{\mathrm{FS}})$ with holomorphic sectional curvature $4/r_3^2$, the Ricci tensor is $\mathrm{Ric}_{ab} = (2N/r_3^2)\,g_{ab}$ (Einstein manifold). Since $\nabla^*\nabla \geq 0$, every eigenvalue of $\Delta_1^H$ satisfies $\mu \geq 2N/r_3^2$.

For $N = 3$ ($\mathbb{CP}^2$): $\mu_1 \geq 6/r_3^2$. This is the specific claim in Theorem 1. For general $N \geq 3$: $\mu_1 \geq 2N/r_3^2 \geq 6/r_3^2$. For $N = 2$ ($\mathbb{CP}^1 = S^2$): $\mu_1 \geq 4/r_3^2$, and the paper provides a separate self-contained SU(2) proof (Section 4.6). So the bound $\mu_1 \geq 6/r_3^2$ holds for $N \geq 3$, with $N = 2$ handled independently.

The actual first eigenvalue on 1-forms on $\mathbb{CP}^{N-1}$ is $\mu_{\min}^{(1)} = 4N/r_3^2$ (Ikeda-Taniguchi 1978), which exceeds the Weitzenboeck lower bound by a factor of 2. For $N = 3$: $\mu_{\min}^{(1)} = 12/r_3^2$. The bound used in the proof ($6/r_3^2$) has a safety factor of 2 built in.

The coefficient $2N/(N-1)$ mentioned in the referee instructions corresponds to the Lichnerowicz bound for scalar functions, not 1-forms. For 1-forms the Weitzenboeck formula directly gives $\mathrm{Ric} = 2N/r_3^2$, not $2N/(N-1)\cdot r_3^{-2}$. The paper correctly uses $2N/r_3^2$.

I verified: $H^1(\mathbb{CP}^{N-1}; \mathbb{R}) = 0$ for $N \geq 2$, confirming no harmonic 1-forms exist. This excludes zero modes from the Hodge Laplacian spectrum on 1-forms.

**(b) Connection to KK mass.** The KK mass is $m_1 = \sqrt{\mu_{\min}^{(1)}}/r_3$. For $N = 3$, using the actual eigenvalue $\mu_{\min}^{(1)} = 12/r_3^2$: $m_1 = \sqrt{12}/r_3 = 2\sqrt{3}/r_3$. This is the square root of the spectral gap. No additional factor from gauge field structure is needed: the 1-form Laplacian IS the relevant operator for gauge field KK modes. For general $N$: $m_1 = 2\sqrt{N}/r_3$ (from $\mu_{\min}^{(1)} = 4N/r_3^2$, tracked systematically in Appendix I.3).

The factor $2\sqrt{3}$ is correct for $N = 3$. It comes from the actual spectrum, not from the Weitzenboeck lower bound (which would give $m_1 \geq \sqrt{6}/r_3 \approx 2.45/r_3$; the actual value $2\sqrt{3}/r_3 \approx 3.46/r_3$ is larger).

**Impact on the claimed result:** None. The spectral bound is correct and conservative. The KK mass derivation is standard Kaluza-Klein theory applied to the well-known spectrum of $\mathbb{CP}^{N-1}$.
