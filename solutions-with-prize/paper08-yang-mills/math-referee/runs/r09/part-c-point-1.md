## Part C, Point 1: UV Stability — Precise Scope

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) The effective action structure.** The decomposition $S_k = (1/g_k^2)S_{\mathrm{YM}} + \sum_n c_n^{(k)}\mathcal{O}_n + E_k$ is NOT stated as a single theorem in Balaban. It is inferred from the polymer expansion (CMP 109, Theorem 1): the effective action in the small-field region is $S_k = (1/g_k^2)S_{\mathrm{YM}} + \sum_X K_k(X,V)$, where the polymer activities $K_k(X,V)$ are bounded by $e^{-\kappa|X|}$. The "operator decomposition" is obtained by expanding the polymer activities in local operators — this is a standard Symanzik expansion, not a theorem in Balaban per se.

The translation from polymer activities to local operator coefficients with bounds $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$ follows from the analyticity of the polymer activities (B1, established in Section 5.6 Part I) and the engineering dimension counting. This translation is new to this paper, building on Balaban's polymer bounds. The argument is logically sound: the convergent polymer expansion defines a well-defined functional of $V$, which can be Taylor-expanded in the field strength; the coefficients are bounded by Cauchy estimates from the analyticity radius.

**(b) The gauge group.** Balaban's published program is primarily for SU(2). Section 5.1.2 explicitly addresses the extension to SU($N$), identifying three $N$-dependent elements: the Lipschitz constant $C_D$ of the covariant Laplacian ($\sim N^2$), the polymer convergence constant $\kappa(N)$ (finite for each $N$), and the block-spin projection radius $r_{\mathrm{proj}}(N)$ (depends on matrix size, not on $k$). The systematic tracking of $N$-dependence is deferred to Appendix I.3.

**The gap:** While the structural arguments for extending Balaban to SU($N$) are sound (the construction is group-independent in structure), a full verification would require confirming that every step in Balaban's 10-paper series uses only properties that hold for general compact Lie groups (polynomial dependence of $D^2[V]$ on $V$, positivity of the covariant Laplacian, etc.). The preprint asserts this but does not provide a line-by-line verification. For a Millennium Prize submission, this extension should be stated as a separate theorem with proof, not asserted as obvious.

**Status update:** Appendix I.3 provides a complete 14-constant tracking through the proof chain, with Lemma I.3.1 establishing convergence for each fixed $N$ and a summary table (Section I.3.5). Appendix I, Section I.1.3 extends the construction to SU($N$) with explicit treatment of four group-dependent ingredients. This gap is **CLOSED**.

**(c) The remainder bound.** The bound $\|E_k\| \leq Cg_k^4$ per unit volume follows from the polymer expansion: $|K_k(X,V)| \leq e^{-\kappa|X|}$ implies $\sum_{X \ni x} |K_k(X,V)| \leq C_{\mathrm{KP}} < \infty$. The leading contribution at one loop is $O(g_k^4)$ per site (the one-loop determinant ratio). The norm is the $L^\infty$ norm on gauge-invariant functionals: $\|E_k\| = \sup_{V \in \Omega_s} |E_k[V]|$ per site.

The constant $C$ depends on $N$ through $C_{\mathrm{KP}}(\kappa(N), d)$. For each fixed $N$, $C$ is finite. The norm is the correct one for the spectral lemma application.

**(d) The running coupling.** The evolution $g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$ with controlled remainder is established by Balaban perturbatively. The accumulated higher-order corrections do not spoil asymptotic freedom because the sum $\sum g_k^4 < \infty$ (Basel-type series, Section 5.1.4). The infinite product $\prod(1 + O(g_j^4))$ converges because $\sum g_j^4 \sim \pi^2/(6(b_0\ln 2)^2) < \infty$. This is a purely perturbative $\beta$-function with controlled non-perturbative remainder — the non-perturbative $\beta$-function is not needed.

**(e) Balaban's program completeness.** The boundary between "what Balaban proved" and "what this paper proves" is drawn precisely in Section 5.1.5 ("What Balaban Does NOT Prove") and Section 5.1.6 ("What We Need Beyond Balaban"). The four items Balaban does not prove (mass gap, confinement, continuum limit as QFT, spectral response) are clearly stated. The paper's new contributions (lattice mass gap via KK, form factor bound via deviation order, OS axioms) are correctly identified.

**Impact on the claimed result:** The gap in sub-point (b) affects the generality claim (SU($N$) for all $N$) but not the core mathematical argument. For any fixed $N$, the constants are finite and the proof chain holds. The extension to general $N$ requires verifying the Appendix I.3 material, which I have not independently assessed. This is closable but represents the most significant presentation gap in the Balaban-interface section.
