## Part A, Point 1: The Weitzenböck Spectral Gap on $\mathbb{CP}^{N-1}$

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The spectral bound.**

The Weitzenböck formula on 1-forms states $\Delta_1^H = \nabla^*\nabla + \mathrm{Ric}$. For $\mathbb{CP}^{N-1}$ with the Fubini-Study metric of holomorphic sectional curvature $4/r_3^2$, the Einstein constant is $\mathrm{Ric}_{ab} = \frac{2N}{r_3^2} g_{ab}$. Since $\nabla^*\nabla \geq 0$ and $H^1(\mathbb{CP}^{N-1}) = 0$ for all $N \geq 2$ (no harmonic 1-forms), every eigenvalue of $\Delta_1^H$ satisfies $\mu_n \geq 2N/r_3^2$.

The preprint states $\mu_1 \geq 6/r_3^2$ in the abstract, which is the specialization to $N = 3$ (i.e., $\mathbb{CP}^2$). Theorem 1 in Section 4 correctly gives the general formula $\mu_1 = 2N/r_3^2$ for arbitrary $N$. This is verified by independent computation: the Ikeda-Taniguchi classification (1978) gives the exact first eigenvalue of $\Delta_1^H$ on $\mathbb{CP}^n$ as $\mu_{\min}^{(1)} = 4(n+1)/r^2 = 4N/r_3^2$ (with the standard normalization where holomorphic sectional curvature is $4/r_3^2$). This exceeds the Weitzenböck lower bound $2N/r_3^2$ by a factor of 2, providing a safety margin.

The bound is correct for all $N \geq 2$. It improves with $N$ (larger spectral gap), which is favorable for the proof.

**(b) The connection to KK mass.**

The KK mass is $m_1 = \sqrt{\mu_{\min}^{(1)}}/r_3$. Using the exact first eigenvalue $\mu_{\min}^{(1)} = 4N/r_3^2$, one obtains $m_1 = 2\sqrt{N}/r_3$. For $N = 3$: $m_1 = 2\sqrt{3}/r_3 \approx 3.46/r_3$. The factor $2\sqrt{3}$ is the square root of $12 = 4 \times 3$, coming from $\sqrt{4N/r_3^2} \cdot r_3 = 2\sqrt{N}$, specialized to $N = 3$.

This is correct. The KK mass is indeed the square root of the eigenvalue (since the Klein-Gordon equation on the product manifold gives $m_n^2 = \lambda_n^{(1)}/r_3^2$, so $m_n = \sqrt{\lambda_n^{(1)}}/r_3$). No additional factor arises from gauge field structure vs. scalar Laplacian because the relevant operator is the Hodge Laplacian on $\mathfrak{su}(N)$-valued 1-forms, which on a flat connection reduces to the scalar Hodge Laplacian tensored with the identity on the Lie algebra.

**Impact on the claimed result:** None. The spectral gap computation is standard Riemannian geometry and is correct as stated.
