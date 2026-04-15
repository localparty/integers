## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

The claim: Delta_infinity > 0 for the continuum theory, obtained as a subsequential limit via Banach-Alaoglu.

**(a) Subsequence dependence.** The paper extracts a subsequential limit a_j -> 0 such that S_n^{(a_j)} -> S_n for all n simultaneously. Different subsequences could in principle give different limiting Schwinger functions. The paper does NOT claim uniqueness of the continuum limit. This is correct — uniqueness is a much harder problem.

However, the MASS GAP is subsequence-independent. The mass gap ratio C_k = Delta_k/Lambda_k satisfies the recursion C_{k+1} = C_k - delta C_k with |delta C_k| <= C' g_k^4 (a_k Lambda)^s. The sum Sum delta C_k converges absolutely (Section 5.4.6), so C_infinity = C_0 - Sum delta C_k is uniquely determined by the RG flow. Since the RG flow depends only on the bare parameters (g_0, a_0) and the gauge group, C_infinity is independent of the subsequence used for the Schwinger function extraction.

Similarly, Lambda_infinity = lim Lambda_k is uniquely determined by the product formula Lambda_k = Pi(1 + O(g_j^4)), which converges absolutely.

Therefore Delta_infinity = C_infinity * Lambda_infinity is UNIQUELY DETERMINED, even though the full Schwinger functions may not be.

**(b) Universality.** The paper does not prove universality (that different regularizations give the same continuum limit). This is expected — universality for asymptotically free gauge theories is supported by perturbative arguments but not rigorously proved. It is NOT required by the Jaffe-Witten problem statement.

**(c) The mass gap value.** As argued in (a), C_infinity and Lambda_infinity are subsequence-independent. The positivity Delta_infinity > 0 is guaranteed for every subsequence:

  Delta_infinity = (C_0 - Sum delta C_k) * Lambda_infinity > 0

since |Sum delta C_k| <= Sum C' g_k^4 (a_k Lambda)^s ~ 2% of C_0 (for s = 2), so C_infinity >= 0.98 C_0 > 0.

**(d) Comparison with Clay problem.** The Jaffe-Witten statement: "prove that for any compact simple gauge group G, a quantum Yang-Mills theory exists on R^4 and has a mass gap Delta > 0." The indefinite article "a" means existence of AT LEAST ONE such theory suffices.

The paper proves: there exists a subsequential continuum limit satisfying OS1-OS5 with mass gap Delta_infinity > 0. Moreover, every subsequential limit has the same mass gap. This is sufficient for the Clay prize.

The preprint explicitly addresses all of these points in a dedicated "Remark (Uniqueness and subsequence-independence of the mass gap)" (Section 5.7, lines 2382-2425). It states:

(i) "Different subsequences ... could in principle yield different limiting Schwinger functions. We do **not** claim uniqueness of the continuum limit (universality)."

(ii) "The mass gap value Delta_infinity is subsequence-independent" — proved via the RG telescoping sum, which converges absolutely independently of the subsequence.

(iii) "The Jaffe-Witten problem statement requires the existence of 'a' quantum Yang-Mills theory with mass gap (indefinite article); uniqueness is a separate question not required for the prize."

The remark also addresses the Jaffe-Witten caution on compactness arguments: the mass gap is NOT inferred from the lattice by compactness, but established through the quantitative RG convergence argument.

No error found. The subsequence analysis is thorough and correctly handles the uniqueness question.

**Impact on the claimed result:** None. The mass gap is uniquely determined and positive for every subsequential continuum limit.
