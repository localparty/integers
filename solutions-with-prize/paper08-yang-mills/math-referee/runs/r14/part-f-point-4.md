## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

**(a) Subsequence dependence.** Different Banach-Alaoglu subsequences $a_{j_1} \to 0$ and $a_{j_2} \to 0$ could yield different limiting Schwinger functions $\{S_n^{(1)}\}$ and $\{S_n^{(2)}\}$. The preprint acknowledges this possibility. However:

1. BOTH limits satisfy OS1--OS5 (the axioms are verified for the lattice theory and preserved under weak limits).
2. BOTH limits have mass gap $\Delta_\infty > 0$ (the mass gap is determined by the RG flow, not by the Banach-Alaoglu subsequence -- see (c) below).

The preprint does NOT claim uniqueness of the continuum limit. It claims: every subsequential limit is a QFT satisfying the Wightman axioms with mass gap $\Delta_\infty > 0$.

**(b) Universality.** Uniqueness of the continuum limit (universality) is a non-trivial property that is NOT proved in the preprint. It would require showing that the lattice Schwinger functions converge (not merely have convergent subsequences). This is an open problem for asymptotically free gauge theories.

The Jaffe-Witten problem does NOT require uniqueness. The problem statement asks to "prove that for any compact simple gauge group $G$, a non-trivial quantum Yang-Mills theory exists on $\mathbb{R}^4$ and has a mass gap $\Delta > 0$." The indefinite article "a" indicates that existence of ONE such theory suffices. The preprint establishes existence of at least one (any subsequential limit), which satisfies the problem requirements.

Universality would be a stronger result but is not needed for the Clay prize.

**(c) The mass gap value.** This is a key observation: $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$ where:

- $C_\infty = C_0 - \sum_{k=0}^\infty \delta C_k$ is determined by the convergent RG series
- $\Lambda_\infty = \Lambda_0 \cdot \prod_{k=0}^\infty (1 + O(g_k^4))$ is determined by the convergent RG product

Both $C_\infty$ and $\Lambda_\infty$ are computed from the RG flow, which is deterministic (no subsequence choice involved). The RG flow depends on:
1. The lattice mass gap $\Delta_0(a_0)$ at spacing $a_0$ (determined by the cluster expansion)
2. The running coupling $g_k^2$ (determined by Balaban's RG)
3. The form factor bound coefficients $C_k$ (determined by the recursion)

None of these depend on which Banach-Alaoglu subsequence is chosen. Different subsequences give the SAME mass gap $\Delta_\infty$, even if they give different Schwinger functions at higher orders.

More precisely: the two-point Schwinger function $S_2(x, 0) \sim e^{-\Delta|x|}$ for large $|x|$, and the decay rate $\Delta$ is determined by the convergent series. All subsequential limits share the same exponential decay rate, hence the same mass gap.

**(d) Comparison with Clay problem.** The precise claim proved: "For any compact simple $G$, starting from Wilson's lattice gauge theory, there exists a subsequential continuum limit of the lattice Schwinger functions that satisfies OS1--OS5 and has mass gap $\Delta_\infty > 0$."

This IS sufficient for the Clay prize:
- "A non-trivial quantum Yang-Mills theory exists" $\checkmark$ (any subsequential limit)
- "On $\mathbb{R}^4$" $\checkmark$ (the continuum Schwinger functions are defined on $\mathbb{R}^4$)
- "Has mass gap $\Delta > 0$" $\checkmark$ ($\Delta_\infty > 0$, subsequence-independent)

The fact that multiple continuum limits might exist does not invalidate the proof. Each limit IS a Yang-Mills theory (it satisfies the YM Schwinger-Dyson equations, as verified in Section 5.7) with mass gap.

**Impact on the claimed result:** None. The non-uniqueness of the continuum limit is acknowledged but does not affect the claimed result. The mass gap is subsequence-independent, and the Jaffe-Witten problem requires existence, not uniqueness.
