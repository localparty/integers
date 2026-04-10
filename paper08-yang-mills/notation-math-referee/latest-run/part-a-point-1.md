## Part A, Point 1: The Weitzenböck Spectral Gap on $\mathbb{CP}^{N-1}$

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim is that the Hodge Laplacian on 1-forms on $(\mathbb{CP}^{N-1}, g_{\mathrm{FS}})$ has spectral gap $\mu_1 \geq 2N/r_3^2$, driving the KK mass $m_1 = 2\sqrt{N}/r_3$.

**(a) The spectral bound.** The Weitzenböck formula $\Delta_{\mathrm{Hodge}} = \nabla^*\nabla + \mathrm{Ric}$ on 1-forms is standard differential geometry. The Fubini–Study metric on $\mathbb{CP}^{N-1}$ is Einstein with $\mathrm{Ric}_{ab} = (2N/r_3^2) g_{ab}$. Since $\nabla^*\nabla \geq 0$, every eigenvalue of $\Delta_{\mathrm{Hodge}}$ on 1-forms satisfies $\mu_n \geq 2N/r_3^2$. The coefficient $2N/r_3^2$ is correct for general $N \geq 2$. Note: the referee prompt asks about $2N/(N-1) \cdot r_3^{-2}$; the preprint uses $2N/r_3^2$, which is the correct Einstein constant for $\mathbb{CP}^{N-1}$. (The Lichnerowicz bound involves $n/(n-1) \cdot R_{\min}$ for scalar eigenvalues, not for 1-forms; the Weitzenböck bound on 1-forms directly uses the Ricci tensor.) The bound holds for all $N \geq 2$ and improves linearly with $N$.

Verified computationally in `code/`-venv (sympy): $\mathrm{Ric} = 2N/r_3^2 \cdot g$ for $N = 2,3,4,5$. The actual first eigenvalue is $4N/r_3^2$ (Ikeda–Taniguchi 1978), exceeding the Weitzenböck bound by a factor of 2.

No harmonic 1-forms exist on $\mathbb{CP}^{N-1}$ since $H^1(\mathbb{CP}^{N-1}; \mathbb{R}) = 0$ for $N \geq 2$, confirming strict positivity.

**(b) The connection to KK mass.** The preprint derives $m_1 = 2\sqrt{N}/r_3$ from the **actual** first eigenvalue $\lambda_1^{(1)} = 4N/r_3^2$ (Ikeda–Taniguchi), not from the Weitzenböck lower bound $2N/r_3^2$. The KK mass is $m_n = \sqrt{\lambda_n^{(1)}}/r_3$ by the standard KK reduction (Section 4.1, equation for $m_n$), so $m_1 = \sqrt{4N}/r_3 = 2\sqrt{N}/r_3$.

Verified computationally: $\sqrt{4 \cdot 3} = 2\sqrt{3} \approx 3.464$. For $N=3$, $m_1 = 2\sqrt{3}/r_3$. The Weitzenböck bound alone would give $m_1 \geq \sqrt{2N}/r_3 = \sqrt{6}/r_3 \approx 2.449/r_3$, which is weaker but sufficient for all subsequent bounds.

There is no additional factor from gauge field structure vs. scalar Laplacian: the KK mass is simply $\sqrt{\lambda_1^{(1)}}$ because the internal modes are expanded in eigenfunctions of the Hodge Laplacian on 1-forms (not the scalar Laplacian). The paper is consistent in using the 1-form Laplacian throughout.

**Impact on the claimed result:**
No impact. The spectral bound is correct and forms a solid foundation for the cluster expansion.
