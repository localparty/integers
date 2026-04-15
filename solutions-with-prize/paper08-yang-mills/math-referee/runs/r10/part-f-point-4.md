## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

**(a) Subsequence dependence.**

The continuum limit is obtained via Banach-Alaoglu: different subsequences $a_{j_1} \to 0$ and $a_{j_2} \to 0$ could yield different limiting Schwinger functions $\{S_n^{(1)}\}$ and $\{S_n^{(2)}\}$. Both would satisfy OS1-OS5. Both would have $\Delta_\infty > 0$ (same value — see (c) below).

The preprint does NOT claim uniqueness of the continuum limit. Section 5.7 states explicitly: "We do not claim uniqueness. What is proved: every subsequential limit satisfies OS1-OS5 with mass gap $\Delta_\infty > 0$."

This is an honest acknowledgment, not a gap. The Jaffe-Witten problem does not require uniqueness (see (d) below).

**(b) Universality.**

Universality (uniqueness of the continuum limit up to field rescaling) is a fundamental property expected for asymptotically free gauge theories on physical grounds. It is supported by perturbative arguments (the $\beta$-function is universal to two loops) but not rigorously proved in the non-perturbative setting.

The preprint does not address universality. This is a significant open problem in constructive QFT, but it is NOT required for the Jaffe-Witten problem, which asks for the *existence* of a quantum Yang-Mills theory with mass gap, not for its uniqueness.

If uniqueness were required, it would demand additional arguments: convergence (not just precompactness) of the lattice Schwinger functions in the continuum limit. This would be a substantial extension (likely requiring a separate paper-length argument), but it is not needed for the Clay prize.

**(c) The mass gap value.**

The mass gap $\Delta_\infty = C_\infty \cdot \Lambda_\infty$ is subsequence-independent. Both $C_\infty$ and $\Lambda_\infty$ are determined entirely by the RG flow:

- $C_\infty = C_0 - \sum_{k=0}^\infty \delta C_k$: the series converges absolutely, and each term $\delta C_k$ is determined by the RG flow at step $k$ (the running coupling $g_k$, the operator norm bound, and the spectral lemma constant). These are properties of the lattice theory at scale $a_k$, not of any limiting Schwinger functions.

- $\Lambda_\infty = \lim_k \Lambda_k$: determined by the convergent infinite product $\prod_j(1 + O(g_j^4))$ from the $\beta$-function.

Neither $C_\infty$ nor $\Lambda_\infty$ depends on which subsequence of lattice spacings is used for the Banach-Alaoglu extraction. Therefore $\Delta_\infty > 0$ is a uniquely determined physical quantity: the same for every subsequential limit.

This is a significant strength of the proof: even without uniqueness of the full theory, the mass gap value is uniquely determined.

**(d) Comparison with the Clay problem.**

The Jaffe-Witten statement asks to "prove that for any compact simple gauge group $G$, *a* quantum Yang-Mills theory exists on $\mathbb{R}^4$ and has a mass gap $\Delta > 0$." The indefinite article "a" indicates that existence of one such theory suffices. Multiple continuum limits (if they exist) would all be Yang-Mills theories in the sense of being derived from the Yang-Mills Lagrangian on the lattice via the Wilson action. They would all share the same mass gap value $\Delta_\infty > 0$.

The preprint's result — that every subsequential limit is a Wightman QFT with mass gap $\Delta_\infty > 0$ — is sufficient for the Clay prize. The existence of at least one such limit is guaranteed by Banach-Alaoglu compactness.

**Impact on the claimed result:**

None. The preprint correctly handles the uniqueness question (Section 5.7, Remark on Uniqueness and Subsequence-Independence):

(i) It explicitly acknowledges that uniqueness (universality) is not proved and is not claimed.

(ii) It proves that the mass gap value $\Delta_\infty > 0$ IS subsequence-independent — both $C_\infty$ and $\Lambda_\infty$ are determined by the RG flow, not by the Banach-Alaoglu extraction.

(iii) It correctly cites the Jaffe-Witten indefinite article: "a" quantum Yang-Mills theory, not "the" unique one.

Uniqueness of the continuum limit is a separate open problem in constructive QFT, not a gap in this paper. The paper does not need to solve it for the Clay prize.
