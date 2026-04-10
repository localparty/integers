## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) Subsequence dependence.**

The continuum limit is obtained by Banach-Alaoglu: the family $\{S_n^{(a)}\}_{a > 0}$ lies in a weak-$*$ precompact set of tempered distributions, so a convergent subsequence $a_j \to 0$ exists. Different subsequences could yield different limiting Schwinger functions.

The preprint claims (Section 5.7, Remark 1) that every subsequential limit has mass gap $\Delta_\infty > 0$ because the RG telescoping sum converges absolutely, independently of the subsequence. The argument: $\Delta_\infty = C_\infty \cdot \Lambda_\infty$ where both $C_\infty = C_0 - \sum \delta C_k$ and $\Lambda_\infty = \lim \Lambda_k$ are defined as limits of sequences determined entirely by the RG flow. These sequences do not depend on which subsequence of lattice spacings is chosen — the RG steps and their bounds are properties of the lattice theory at each fixed $a$, not of the limiting procedure.

This argument is correct: $C_\infty$ and $\Lambda_\infty$ are determined by the coupling trajectory $g_k$ and the mass gap shifts $\delta C_k$, which are computed on the lattice and are $a$-independent (after expressing everything in lattice units). The positivity $\Delta_\infty > 0$ follows from $C_\infty > 0$ and $\Lambda_\infty > 0$, both of which are subsequence-independent.

**(b) Universality.**

Universality (uniqueness of the continuum limit) is NOT proved by the preprint. This is a non-trivial property that goes beyond the existence of subsequential limits. For asymptotically free theories, universality is expected on physical grounds and supported by perturbative universality (the $\beta$-function coefficients $b_0, b_1$ are scheme-independent). However, non-perturbative universality — the statement that ALL subsequential limits are the same — is a much stronger claim.

The preprint does not claim universality. It claims: for every subsequential limit, OS1-OS5 hold and $\Delta_\infty > 0$. This is sufficient for the Jaffe-Witten problem.

Does the Jaffe-Witten problem require uniqueness? The problem statement says "prove that a non-trivial quantum Yang-Mills theory exists on $\mathbb{R}^4$ and has a mass gap." The indefinite article "a" suggests existence of one such theory suffices. The statement does not require uniqueness of the construction. A subsequential limit satisfying OS1-OS5 with $\Delta_\infty > 0$ IS "a non-trivial quantum Yang-Mills theory with a mass gap."

**(c) The mass gap value.**

$C_\infty$ and $\Lambda_\infty$ are subsequence-independent (as argued in (a)). Therefore $\Delta_\infty = C_\infty \Lambda_\infty$ is unique — every subsequential limit has the SAME mass gap value. This is because the mass gap is determined by the RG flow, not by the subsequence.

Different subsequences could yield different Schwinger functions (different $n$-point functions) but with the same spectrum. This is analogous to different constructions of the same theory (e.g., different lattice actions giving the same continuum theory). The mass gap is a spectral quantity, determined by the transfer matrix eigenvalues, which converge along the RG flow.

**(d) Comparison with the Clay problem.**

The Jaffe-Witten problem statement asks for "a quantum Yang-Mills theory" satisfying axioms "at least as strong as" Wightman or OS. The preprint constructs such a theory (via a subsequential limit) and proves $\Delta_\infty > 0$.

**The gap:** The Jaffe-Witten problem description (in the extended version) explicitly cautions about compactness/subsequential limit constructions, noting that "properties of the limiting theory must be verified." The preprint does verify the properties (OS1-OS5 and $\Delta_\infty > 0$) for the limiting theory, not merely for the approximants. This addresses the Jaffe-Witten concern.

However, the preprint does not establish that all subsequential limits are the same theory. If different subsequences give different $n$-point functions (even with the same mass gap), the "theory" is not uniquely defined. The Clay problem asks for "a theory," so existence of one is sufficient, but the Scientific Advisory Board might view non-uniqueness as a conceptual weakness.

**Closing the gap:** Full universality would require: (i) showing that the Schwinger functions converge (not just subsequentially) as $a \to 0$, or (ii) showing that any two subsequential limits are equivalent (same $n$-point functions). This is a substantial open problem, estimated at 1 paper of additional work.

However, for the mass gap claim $\Delta_\infty > 0$, universality is NOT required. The mass gap is the same for every subsequential limit, and every limit satisfies OS1-OS5. The claim "there exists a QFT with mass gap $\Delta_\infty > 0$" is proved.

**Impact on the claimed result:** (iii) Potentially affects Clay prize eligibility, but the gap is philosophical rather than mathematical. The mass gap IS proved for every subsequential limit. The lack of uniqueness means the "theory" may not be uniquely specified, but the existence statement is rigorous. A Clay referee would likely request a discussion of universality but would not reject the proof on these grounds, given that the mass gap value is subsequence-independent.
