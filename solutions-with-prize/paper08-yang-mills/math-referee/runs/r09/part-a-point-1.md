## Part A, Point 1: The Weitzenböck Spectral Gap on $\mathbb{CP}^{N-1}$

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The spectral bound.** The Weitzenböck formula $\Delta_1^H = \nabla^*\nabla + \mathrm{Ric}$ on 1-forms is correctly applied. For the Fubini-Study metric on $\mathbb{CP}^{N-1}$ with holomorphic sectional curvature $4/r_3^2$, the Einstein condition gives:

$$R_{ab} = \frac{2N}{r_3^2}\,g_{ab}.$$

This is stated in Section 4.2, Step 2, and is standard (see e.g. Besse, *Einstein Manifolds*, Chapter 8). Since $\nabla^*\nabla \geq 0$:

$$\Delta_1^H \geq \frac{2N}{r_3^2}\,\mathrm{Id}.$$

For $N = 3$ (SU(3)): $\mu_1 \geq 6/r_3^2$. For general $N \geq 2$: $\mu_1 \geq 2N/r_3^2 \geq 4/r_3^2$. The numerical coefficient is correct for all $N$. The proof uses the $N = 3$ value as the stated bound but correctly notes (Remark 3, Section 4.2) that the bound improves with $N$.

The absence of harmonic 1-forms follows from $H^1(\mathbb{CP}^{N-1};\mathbb{R}) = 0$ for all $N \geq 2$, which is standard algebraic topology.

The actual first eigenvalue $\mu_{\min}^{(1)} = 12/r_3^2$ (Ikeda-Taniguchi 1978, also derivable from the symmetric space structure, see Appendix A) exceeds the Weitzenböck bound by a factor of 2. The proof uses the actual eigenvalue for the KK mass (Theorem 2) while citing only the lower bound for the spectral gap claim (Theorem 1). This is conservative and correct.

**(b) The connection to KK mass.** The paper derives $m_1 = \sqrt{\lambda_1^{(1)}}/r_3 = \sqrt{12}/r_3 = 2\sqrt{3}/r_3$ from $\lambda_1^{(1)} = 12/r_3^2$. This is the actual first eigenvalue, not the Weitzenböck bound. The factor $2\sqrt{3}$ is verified: $\sqrt{12} = 2\sqrt{3} \approx 3.46$.

The KK mass IS the square root of the spectral gap divided by $r_3$, coming from the mode decomposition $m_n = \sqrt{\lambda_n^{(1)}}/r_3$. There is no additional factor from the gauge field structure vs. scalar Laplacian, because the adjoint representation acts only on the color indices and does not modify the eigenvalues of the Hodge Laplacian on $\mathbb{CP}^{N-1}$.

**Impact on the claimed result:** None. The spectral gap estimate is correct and conservative.
