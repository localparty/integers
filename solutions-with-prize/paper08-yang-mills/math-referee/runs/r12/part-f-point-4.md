## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** GENUINE GAP (for Clay Prize purposes; existential result is sound for subsequential limits)

---

**Finding:**

**(a) Subsequence dependence.** The continuum limit is constructed via the Banach-Alaoglu theorem, which yields a *subsequential* limit: there exists a subsequence $a_j \to 0$ such that $S_n^{(a_j)} \to S_n$ for all $n$. Different subsequences could in principle give different limiting Schwinger functions $\{S_n^{(1)}\}$ and $\{S_n^{(2)}\}$, both satisfying OS1–OS5 and having $\Delta_\infty > 0$.

The preprint does not claim uniqueness of the continuum limit. Section 5.7 establishes existence of *a* subsequential limit with the desired properties. The abstract says "there exists a continuum limit" (existential), not "the continuum limit is unique." This is an honest and correct statement of what is proved.

**(b) Universality.** Universality (independence of the continuum limit from the lattice regularization and from the subsequence choice) is not addressed in the preprint. Section 5.7 does not discuss whether the subsequential limit is independent of the subsequence. Universality is expected from the renormalization group fixed-point structure (Wilson), but proving it rigorously requires showing that all subsequential limits define the same Wightman theory.

For the Clay Prize, the Jaffe-Witten problem statement uses the indefinite article: "prove that... a quantum Yang-Mills theory exists on $\mathbb{R}^4$ and has a mass gap $\Delta > 0$." This suggests existence of *one* such theory is sufficient. The preprint proves this: there exists at least one subsequential limit of the lattice theory (as $a \to 0$ along some sequence) that satisfies OS1–OS5 with $\Delta_\infty > 0$, hence gives a Wightman QFT via OS reconstruction.

However, the Clay Prize problem also implicitly requires that the constructed theory is a *Yang-Mills theory* — i.e., that it satisfies the Yang-Mills equations of motion in some sense. This is related to sub-point (d) in F5.

**(c) Mass gap value.** Even for different subsequences, $\Delta_\infty > 0$ is guaranteed for each: the proof that $\Delta_\infty = C_\infty \Lambda_\infty > 0$ uses $C_\infty = C_0 - \sum \delta C_k > 0$ and $\Lambda_\infty > 0$. The value of $C_\infty$ may depend on $C_0$ (the starting mass gap ratio, fixed by the cluster expansion at $a = a_0$), and $\Lambda_\infty$ (the accumulated scale factor, determined by $\int_0^\infty \beta(g) dg/g^2$). Both are determined by the universal asymptotic freedom trajectory, not by the specific subsequence (which only determines the initial lattice spacing $a_0$). The mass gap in physical units $\Delta_\infty \Lambda^{-1}$ is universal (a pure number independent of the lattice), so different subsequences give the same $\Delta_\infty/\Lambda$.

This suggests the continuum limit *is* unique up to overall scale (the definition of $\Lambda$ in terms of the microscopic coupling $g_0$). But this is not proved in the preprint. CLOSABLE GAP: add a remark that the mass gap ratio $\Delta_\infty/\Lambda_{\text{QCD}}$ is subsequence-independent because it is determined by the universal RG flow, even if the limiting Schwinger functions are potentially different. Difficulty: **1 paragraph**.

**(d) Clay problem interpretation.** The Clay problem requires "a quantum Yang-Mills theory." The preprint constructs a Wightman QFT via OS reconstruction from Schwinger functions built from Wilson loops (gauge-invariant observables). The question is whether this theory is the Yang-Mills theory in the sense that the dynamics are governed by the Yang-Mills equations.

On the lattice, the dynamics are governed by the Wilson action (which approximates the Yang-Mills action up to $O(a^2)$ corrections). In the continuum limit, the $O(a^2)$ corrections vanish (Section 5.7(f), OS2: O(4)-breaking corrections go to zero). The limiting theory has $\mathrm{O}(4)$ invariance and gauge invariance. But whether it satisfies the Yang-Mills equations of motion as operator equations is a separate question.

For gauge theories, the Ward identities (associated with gauge invariance) play the role of equations of motion. The Schwinger functions constructed from gauge-invariant Wilson loops automatically satisfy the gauge Ward identities (they are built from gauge-invariant quantities). But whether the limiting theory has the correct off-shell structure (e.g., correct relation between the gauge field propagator and the interaction vertices at tree level) is not addressed.

For the Clay Prize, the minimal requirement is existence of a mass-gapped QFT with the gauge symmetry SU($N$), which the preprint establishes. Whether additional requirements (specific equation of motion satisfaction, non-triviality of the $S$-matrix) are needed is a matter of interpretation of the Jaffe-Witten problem.

**Summary.** The preprint proves: for each fixed $N \geq 2$, there exists a subsequential continuum limit of $\mathrm{SU}(N)$ lattice Yang-Mills theory (Wilson action) satisfying OS1–OS5 with $\Delta_\infty > 0$, which by OS reconstruction gives a Wightman QFT with mass gap. This is an existential result, not a uniqueness result. For the Clay Prize's "a quantum Yang-Mills theory exists," the existential result is sufficient in interpretation, but uniqueness (universality) would make the result stronger and more convincing.

**Impact on the claimed result:** The GENUINE GAP here is not in the proof of $\Delta_\infty > 0$ — that is established. The gap is in the Clay Prize context: the preprint establishes *a* continuum QFT with mass gap, but not that this is the *unique* Yang-Mills theory. For the Clay Scientific Advisory Board, a full solution would require addressing universality. As stated, the preprint provides an existential proof of a mass-gapped QFT associated with $\mathrm{SU}(N)$ lattice Yang-Mills, which may or may not be accepted as a full solution to the Clay problem depending on the Board's interpretation.
