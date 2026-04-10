## Part A, Point 1: The Weitzenböck Spectral Gap on $\mathbb{CP}^{N-1}$

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The spectral bound.**

The Weitzenböck formula on 1-forms states $\Delta_1^H = \nabla^*\nabla + \mathrm{Ric}$. For $\mathbb{CP}^{N-1}$ with the Fubini-Study metric of curvature radius $r_3$, the Ricci tensor is Einstein: $\mathrm{Ric} = (2N/r_3^2)\,g_{\mathrm{FS}}$. Since $\nabla^*\nabla \geq 0$, this gives the lower bound

$$\mu_1 \geq \frac{2N}{r_3^2}$$

for the first eigenvalue of the Hodge Laplacian on 1-forms. For $N = 3$ (the SU(3) case featured in the body of the paper), this yields $\mu_1 \geq 6/r_3^2$, matching the preprint's claim.

For general $N \geq 2$: the bound $\mu_1 \geq 2N/r_3^2$ *improves* with $N$. Appendix I.3 (N-dependence tracking) confirms this: the spectral gap scales as $\sim N$, which is favorable (larger $N$ gives a larger gap). The bound $\mu_1 \geq 6/r_3^2$ stated in the abstract is the $N = 3$ specialization; for $N = 2$, the Weitzenböck bound gives $\mu_1 \geq 4/r_3^2$, and for $N \geq 3$ the bound exceeds $6/r_3^2$. The proof in Appendix I.4 (other gauge groups) uses the group-specific Einstein constant $\lambda_G = 2N/r_3^2$ for each SU($N$).

The numerical coefficient is correct. Appendix A verifies the explicit eigenvalue computation for $\mathbb{CP}^2$: the actual first eigenvalue is $\lambda_1 = 12/r_3^2$, which exceeds the Weitzenböck lower bound of $6/r_3^2$ by a factor of 2. This is expected for Kähler manifolds, where the Weitzenböck bound is typically not sharp. There is no error.

**(b) The connection to KK mass.**

The preprint derives $m_1 = 2\sqrt{3}/r_3$ from the actual first eigenvalue $\lambda_1^{(1)} = 12/r_3^2$ on $\mathbb{CP}^2$ (not from the Weitzenböck lower bound). The KK mass is $m_1 = \sqrt{\lambda_1^{(1)}} = \sqrt{12}/r_3 = 2\sqrt{3}/r_3$. The factor of $2\sqrt{3} \approx 3.46$ is correct.

There is no additional factor from the gauge field structure vs. scalar Laplacian here because the relevant quantity is the spectral gap of the Hodge Laplacian on 1-forms (which already accounts for the gauge field nature through the Weitzenböck identity). The mass of the lowest KK mode is indeed the square root of the first eigenvalue of the Hodge Laplacian on 1-forms on the internal manifold, as used in standard Kaluza-Klein reduction.

For general SU($N$), Appendix I.3 gives $m_1 = \sqrt{2(N+1)}/r_3$ (using the actual eigenvalue on $\mathbb{CP}^{N-1}$, which exceeds the Weitzenböck lower bound). The proof requires only $m_1 > 0$, and the exact value determines the quantitative convergence of the cluster expansion.

**Impact on the claimed result:**

None. The spectral gap is correctly computed and correctly used. The bound improves with $N$, posing no obstruction for large gauge groups.
