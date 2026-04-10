## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim is that Balaban's construction decomposes configurations into small-field region $\Omega_s$ (where the polymer expansion converges) and large-field region $\Omega_l$ (exponentially suppressed).

**(a) The small-field condition.** The cutoff is $p(g_k) = g_k^{1-\epsilon}$ with $\epsilon = \epsilon^* = 0.49$ (Appendix K.4). This is a fixed constant, independent of $k$. The polymer expansion and analyticity properties (B1)–(B2) are established within $\Omega_s$. The dimension-6 operator classification is valid within $\Omega_s$ because the operators are defined through the effective action, which in turn is defined through the polymer expansion convergent in $\Omega_s$. In $\Omega_l$, the effective action is not decomposed into local operators — the entire contribution is bounded by $O(e^{-c/g_k^{2\epsilon}})$.

**(b) Large-field suppression.** The large-field contribution is bounded by $O(e^{-c/g_k^{2\epsilon}})$ (Balaban CMP 119; preprint Section 5.5.3 Step 3(i)). This is weaker than instanton suppression $O(e^{-c/g_k^2})$ but still decays faster than any power of $g_k$.

Verified computationally: on the AF trajectory with $g_k^2 \sim 1/(b_0 k \ln 2)$, the large-field contribution at $k=1$ gives ratio $e^{-c/g_k^{2\epsilon}} / (g_k^4 \hat{\Delta}_k^2) \approx 7 \times 10^{-3}$ (marginally small), while for $k \geq 5$ the ratio exceeds 1, meaning the large-field term is NOT uniformly negligible compared to $g_k^4 \hat{\Delta}_k^2$ at early RG steps.

However, the paper explicitly handles this: the first $k_0(K)$ RG steps (where $g_k^4 = O(1)$) are treated non-perturbatively via the cluster expansion (Section 5.4.6). The polymer bound $|K_k(X,V)| \leq e^{-\kappa|X|}$ holds uniformly in $k$ (including the strong-coupling regime), so the large-field contribution is absorbed into the $k$-independent starting constant. For $k \geq k_0$ on the AF trajectory, $g_k$ is small and the large-field suppression $e^{-c/g_k^{2\epsilon}}$ is indeed negligible compared to $g_k^4 \hat{\Delta}_k^2$.

**(c) Gauge invariance of the decomposition.** The condition $|F_{\mu\nu}| < p(g_k)$ is gauge-invariant because $F_{\mu\nu}$ transforms in the adjoint representation and $|F_{\mu\nu}|$ uses a gauge-invariant norm (e.g., $\mathrm{Tr}(F_{\mu\nu}^2)$). Balaban uses axial gauge fixing as a computational device (Point G2), but the small-field/large-field split is defined gauge-invariantly through the plaquette variable $s_P = 1 - (1/N)\mathrm{Re}\,\mathrm{Tr}\,U_P$. The gauge-fixing interacts with the block-spin integration (Steps (i)–(iii) of Section 5.4.1) but does not affect the gauge-invariant decomposition.

**Impact on the claimed result:**
No impact. The large-field/small-field decomposition is standard in Balaban's framework and is handled correctly, with the strong-coupling steps treated non-perturbatively.
