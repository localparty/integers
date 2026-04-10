## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

(a) The small-field condition $|F_{\mu\nu}| < p(g_k) = g_k^{1-\epsilon}$ uses a fixed $\epsilon > 0$ (typically small, e.g., $\epsilon = 1/10$; the precise value is chosen in Balaban CMP 109 to optimize the polymer expansion convergence while maintaining the large-field suppression). The parameter $\epsilon$ is fixed once and does not depend on $k$. The polymer expansion and analyticity properties (B1)-(B2) are established only in $\Omega_s$. The dimension-6 operator classification is valid only in $\Omega_s$, as the Taylor expansion of the effective action (which defines the "dimension-6 part") requires analyticity. Outside $\Omega_s$ (in $\Omega_l$), the effective action is not controlled term-by-term but contributes only a total exponentially suppressed correction.

(b) The large-field contribution is bounded by $O(e^{-c/g_k^{2\epsilon}})$ (Section 5.6, Part III.5). On the asymptotically free trajectory, $g_k^2 \sim 1/(b_0 k \ln 2)$, so $e^{-c/g_k^{2\epsilon}} = e^{-c(b_0 k \ln 2)^\epsilon}$, which decreases faster than any power $g_k^n$ or polynomial $k^{-n}$. The target bound is $g_k^4 \hat{\Delta}_k^2 \sim 4^{-k}/k^2$, which decreases exponentially but only as $4^{-k}$. Since $e^{-c k^\epsilon}$ decreases faster than $4^{-k}$ for all $\epsilon > 0$ (stretched exponential dominates geometric), the large-field suppression is sufficient for the RG recursion. The specific comparison: $e^{-c/g_k^{2\epsilon}} / (g_k^4 \hat{\Delta}_k^2) \to 0$ as $k \to \infty$, so the large-field contribution is negligible relative to the small-field form factor bound at each step.

(c) The condition $|F_{\mu\nu}| < p(g_k)$ IS gauge-invariant: $F_{\mu\nu}$ is defined via the plaquette variable $U_P$, and $|F_{\mu\nu}|$ is the norm of the anti-Hermitian lattice field strength, which transforms under the adjoint representation. The Hilbert-Schmidt norm $|F_{\mu\nu}|_{HS} = \sqrt{Tr(F_{\mu\nu}^2)}$ is gauge-invariant. Balaban's axial gauge fixing is a computational device used within the small-field region to define the propagator and saddle-point expansion; it does not affect the gauge-invariance of the small-field/large-field classification.

**Impact on the claimed result:** None. The decomposition is standard (Balaban CMP 109, 119) and correctly implemented.
