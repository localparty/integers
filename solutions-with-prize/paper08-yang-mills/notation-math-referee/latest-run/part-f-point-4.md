## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

The preprint obtains the continuum theory as a subsequential Banach–Alaoglu limit. The Jaffe–Witten footnote (§6.6, fn. 2) requires properties of the limit to be established, not merely that a weak limit exists.

**(a) Subsequence dependence.** Different subsequences could give different limiting Schwinger functions, hence different QFTs. The paper explicitly states: "We do not claim uniqueness of the continuum limit (universality). What is proved is that every subsequential limit satisfies OS1–OS5 with mass gap $\Delta_\infty > 0$." This is honest and correct.

**(b) Universality.** Universality (uniqueness of the continuum limit) is a non-trivial property in statistical mechanics that requires additional arguments. For asymptotically free gauge theories, universality is supported by perturbative arguments but not rigorously proved. The paper does not address universality. The Jaffe–Witten problem does not explicitly require uniqueness.

**(c) The mass gap value.** The mass gap $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$ is proved positive for every subsequential limit. The value $C_\infty = C_0 - \sum \delta C_K$ and $\Lambda_\infty = \lim \Lambda_K$ are determined by the convergent sums, which depend on the specific subsequence only through the starting data. On the AF trajectory, the running coupling $g_K$ and the dimensionless gap $\hat{\Delta}_K$ are determined by the bare coupling and the one-loop + remainder corrections, which are universal (independent of the subsequence). So $\Delta_\infty > 0$ holds for every subsequence, and the value is in fact subsequence-independent (up to the $O(g_K^6)$ corrections in the running coupling, which are bounded and convergent).

**(d) Comparison with the Clay problem.** The Jaffe–Witten statement asks to prove "a quantum Yang–Mills theory exists ... and has a mass gap." The indefinite article "a" suggests existence of one such theory suffices. The paper proves: for every subsequential limit of the Wilson lattice gauge theory, the limit satisfies OS1–OS5 with $\Delta_\infty > 0$. This gives existence of at least one (in fact, every limit has the property).

**Does this satisfy the Jaffe–Witten footnote?** The footnote excludes "weak-existence (compactness) as the solution ... unless one also uses other techniques to establish properties of the limit." The paper does use other techniques: the mass gap is propagated through the RG (not merely asserted for a hypothetical limit), and the OS axioms are verified by explicit bounds that survive the limit. The mass gap and axioms are established for **the** limit (whichever subsequence is chosen), not merely asserted.

**Gap:** The paper could strengthen its position by showing that the mass gap value $\Delta_\infty$ is actually subsequence-independent (which appears to be the case from the argument, since $C_\infty$ and $\Lambda_\infty$ are determined by convergent series). This would establish that all subsequential limits are the same QFT, at least in terms of their mass spectrum.

Closable in **1 page**: show that $C_\infty$ and $\Lambda_\infty$ are independent of the extraction subsequence by verifying that the Schwinger functions $S_n^{(a)}$ converge (not just subsequentially) for all $n$ and all Schwartz test functions. This would follow if the bounds on $|S_n^{(a)} - S_n^{(a')}|$ are Cauchy in $a, a'$.

**Impact on the claimed result:**
Affects (iii) Clay prize eligibility. The footnote requires "properties of the limit" to be established, which the paper does (mass gap and OS axioms are propagated). Uniqueness is not required by the problem statement. The paper's approach satisfies the footnote's requirement.
