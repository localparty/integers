## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The small-field condition.** In Balaban's construction, the small-field cutoff is $p(g_k) = g_k^{1-\epsilon}$ for a fixed constant $\epsilon > 0$ (typically $\epsilon = 1/10$ or similar; the exact value is specified in Balaban's papers). The parameter $\epsilon$ is $k$-independent -- it is chosen once at the start of the construction.

The small-field region is $\Omega_s = \{V : |F_{\mu\nu}(V)| < p(g_k)\}$. All the key properties hold in $\Omega_s$:
- Polymer expansion converges (CMP 109, Theorem 1)
- Analyticity of $S_k[V]$ with $k$-independent radius (property (B1))
- Operator decomposition via the extraction lemma (Appendix I.1)
- Dimension-6 classification (Appendix J)

The dimension-6 classification is valid in $\Omega_s$ because the operators are classified by their algebraic structure (gauge invariance, $\mathcal{C}$-symmetry, engineering dimension), which does not depend on the field strength magnitude. The classification holds for ALL configurations, not just small-field ones. The role of $\Omega_s$ is to ensure the COEFFICIENTS of the operators are controlled (via analyticity), not the classification itself.

**(b) Large-field suppression.** The large-field contribution is bounded by $O(e^{-c/g_k^{2\epsilon}})$ (Section 5.6, Part III.5). On the asymptotically free trajectory $g_k^2 \approx 1/(b_0 k \ln 2)$:

$$e^{-c/g_k^{2\epsilon}} = e^{-c(b_0 k \ln 2)^{\epsilon}}$$

For any $\epsilon > 0$, this decays faster than any power of $k$. Meanwhile, the small-field contribution $g_k^4\,\hat{\Delta}_k^2$ involves $g_k^4 \sim 1/k^2$. The large-field contribution is negligible:

$$\frac{e^{-c(b_0 k)^{\epsilon}}}{1/k^2} = k^2\,e^{-c(b_0 k)^{\epsilon}} \to 0$$

for any $\epsilon > 0$. For the RG recursion, the large-field contribution to $C_{k+1}$ is $O(e^{-c(b_0 k)^{\epsilon}})$, which is summable:

$$\sum_{k=0}^{\infty} e^{-c(b_0 k)^{\epsilon}} < \infty$$

This is weaker than instanton suppression $O(e^{-c/g_k^2}) = O(e^{-cb_0 k \ln 2})$ but more than sufficient.

**(c) Gauge invariance of the decomposition.** The field strength $F_{\mu\nu}$ transforms in the adjoint representation: $F_{\mu\nu} \to g\,F_{\mu\nu}\,g^{-1}$. The norm $|F_{\mu\nu}|^2 = \mathrm{Tr}(F_{\mu\nu}^\dagger F_{\mu\nu})$ is gauge-invariant. Therefore the condition $|F_{\mu\nu}| < p(g_k)$ is gauge-invariant, and the small-field/large-field decomposition respects gauge invariance.

Balaban's construction uses axial gauge as a computational device within $\Omega_s$, but the BOUNDARIES of the regions are gauge-invariant. The effective action at each step is gauge-invariant (this is proved by Balaban and is a structural property of the block-spin transformation). The gauge-fixing does not interact with the small-field/large-field split.

**Impact on the claimed result:** None. The small-field/large-field decomposition is a standard technique in constructive QFT. The large-field contributions are exponentially suppressed and negligible compared to the small-field contributions. The decomposition is gauge-invariant.
