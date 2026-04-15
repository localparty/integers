## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

**(a) Subsequence dependence.** The preprint explicitly addresses this (Section 5.7(f), Remark on uniqueness):

> "We do NOT claim uniqueness of the continuum limit (universality). What is proved is that every subsequential limit satisfies OS1-OS5 with mass gap $\Delta_\infty > 0$."

Different subsequences $a_{j_1} \to 0$ and $a_{j_2} \to 0$ could yield different limiting Schwinger functions. The preprint acknowledges this as a separate question not addressed in the paper. The claim is existence of A theory with mass gap, not uniqueness.

**(b) Universality.** Universality (uniqueness of the continuum limit) is a deep open problem in constructive QFT. It is expected for asymptotically free gauge theories (supported by perturbative arguments and lattice simulations) but has not been rigorously proved for any non-trivial 4D theory. The preprint correctly identifies this as outside the scope:

> "The Jaffe-Witten problem statement requires the existence of 'a' quantum Yang-Mills theory with mass gap (indefinite article); uniqueness is a separate question not required for the prize."

I agree with this reading of the Jaffe-Witten problem statement. The word "a" (indefinite article) in "prove that for any compact simple gauge group $G$, a quantum Yang-Mills theory exists" suggests existence suffices.

**(c) The mass gap value.** The preprint makes the important claim that $\Delta_\infty$ is subsequence-independent:

> "The RG analysis gives $\Delta_\infty = C_\infty \cdot \Lambda_\infty$ where $C_\infty = C_0 - \sum \delta C_k$ with the series converging absolutely, and $\Lambda_\infty = \lim_{k\to\infty} \Lambda_k$ is determined by the convergent infinite product."

Both $C_\infty$ and $\Lambda_\infty$ are defined as limits of sequences determined entirely by the RG flow, not by the Banach-Alaoglu subsequence. The RG flow is a fixed dynamical system: $g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$, $\hat{\Delta}_{k+1} = 2\hat{\Delta}_k(1 + O(g_k^4))$. These sequences converge independently of the subsequence chosen for the Schwinger functions.

This argument is correct: the mass gap value depends on the RG flow, which is unique, not on the subsequential extraction, which may not be unique.

**(d) Comparison with the Clay problem.** The Jaffe-Witten statement asks to prove that "a quantum Yang-Mills theory exists on $\mathbb{R}^4$ and has a mass gap $\Delta > 0$." The word "a" (indefinite article) is critical. If multiple continuum limits exist, each one is a quantum Yang-Mills theory (derived from the same lattice action via different subsequences). Each satisfies OS1-OS5 with the same mass gap $\Delta_\infty > 0$. The existence of one such theory suffices for the prize.

The concern about whether all subsequential limits are "Yang-Mills theories" is addressed by the Ward identities (Section 5.7(f), Remark on Ward identities): the lattice Ward identities converge to continuum Ward identities, confirming that the limiting theory is a gauge theory with gauge group SU($N$). Different subsequences may yield different detailed Schwinger functions but all satisfy the same Ward identities and have the same mass gap.

**Impact on the claimed result:** None. The treatment of uniqueness is honest and correct. The proof establishes existence of a theory with mass gap, which is what the Clay problem requires.
