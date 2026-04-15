## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

(a) The preprint DOES NOT claim uniqueness. Different subsequences $a_{j_1} \to 0$ and $a_{j_2} \to 0$ could give different limiting Schwinger functions. The preprint explicitly states (Section 5.7, Remark on Uniqueness): "We do not claim uniqueness of the continuum limit (universality). What is proved is that every subsequential limit satisfies OS1-OS5 with mass gap $\Delta_\infty > 0$, because the RG telescoping sum converges absolutely (independently of the subsequence)."

(b) Universality (uniqueness of the continuum limit) is a non-trivial property that requires additional arguments beyond existence of subsequential limits. For asymptotically free gauge theories, universality is expected but not rigorously proved. The preprint does not address this. The Jaffe-Witten problem statement uses "a" (indefinite article): "prove that for any compact simple gauge group $G$, a quantum Yang-Mills theory exists..." This suggests existence of one theory suffices. The preprint correctly interprets this.

(c) The mass gap $\Delta_\infty$ could in principle depend on the subsequence. However, the RG analysis shows $\Delta_\infty = C_\infty \cdot \Lambda_\infty$ where $C_\infty = C_0 - \sum \delta C_k$ with the sum converging absolutely. The absolute convergence means $C_\infty$ is determined by the series (which sums to a definite value), independent of the ordering or subsequence. Similarly, $\Lambda_\infty$ is determined by the convergent infinite product $\prod(1 + O(g_j^4))$. So $\Delta_\infty$ is actually subsequence-independent, even though the Schwinger functions may differ. **This is an important observation**: the MASS GAP VALUE $\Delta_\infty > 0$ is unique, even if the full QFT is not.

(d) The Jaffe-Witten statement asks for "a quantum Yang-Mills theory" (indefinite article). The preprint constructs at least one such theory (every subsequential limit). Each such theory satisfies OS1-OS5, has the correct gauge group (SU(N), verified via Ward identities in the continuum limit), is non-trivial (verified by three signatures: $\sigma > 0$, non-zero connected 4-point functions, asymptotic freedom), and has mass gap $\Delta_\infty > 0$. This suffices for the Clay problem as stated.

**Impact on the claimed result:** The lack of uniqueness does NOT affect the main claim $\Delta_\infty > 0$, which is proved for every subsequential limit. The Clay prize eligibility is not affected: the problem asks for existence, not uniqueness. **However, the paper should state more prominently that $\Delta_\infty$ is subsequence-independent (by absolute convergence of the RG sum).** This strengthens the result. Closable with 1 paragraph.
