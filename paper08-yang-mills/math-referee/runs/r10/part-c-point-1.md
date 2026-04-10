## Part C, Point 1: UV Stability — Precise Scope

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

**(a) The effective action structure.**

The preprint writes $S_k = (1/g_k^2)S_{\mathrm{YM}} + \sum_n c_n^{(k)}\mathcal{O}_n + E_k$. This decomposition is *not* stated as a single theorem in Balaban's papers. Balaban works with polymer activities $K_k(X,V)$ satisfying $|K_k(X,V)| \leq e^{-\kappa|X|}$ (CMP 109, Theorem 1). The translation to local operator coefficients is performed in Appendix I (Lemma I.1, the "extraction lemma"), which decomposes the convergent polymer sum into local operators organized by engineering dimension.

The extraction is rigorous: the convergent polymer expansion is a well-defined bounded function of the gauge field, and standard Taylor expansion in gauge-invariant monomials (justified by analyticity property (B1)) produces the operator decomposition with coefficient bounds $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$. The remainder $R_k$ satisfies $\|R_k\| \leq C g_k^{D_0}$ per unit volume.

This extraction is new to this paper (not in Balaban or Dimock), but it follows from standard functional analysis applied to Balaban's construction. The argument is self-contained and correct.

**(b) The gauge group.**

Balaban's published program is primarily for SU(2). The preprint extends to general SU($N$). Appendix I (Section I.2) identifies three group-dependent elements requiring modification:

1. **Covariant Laplacian $D^2[V]$:** Lipschitz constant $C_D$ scales as $\dim(\mathrm{ad}) = N^2 - 1$. Polynomial in $N$, does not affect convergence structure.

2. **Polymer expansion constant $\kappa(N) > 0$:** Finite for each $N$, from fluctuation mass $m_W$ and blocking geometry ($L = 2$, $d = 4$) — both $N$-independent.

3. **Block-spin projection radius $r_{\mathrm{proj}}(N)$:** Analyticity radius of $A \mapsto A(A^\dagger A)^{-1/2}$ near $\mathbf{1} \in \mathrm{GL}(N,\mathbb{C})$. $r_{\mathrm{proj}} \geq 1/4$ for $\|A - \mathbf{1}\| < 1/2$, depending on $N$ only.

The propagator bounds (CMP 95-96) use the Green's function $G_k(V) = (-D^2[V] + m_W^2)^{-1}$. The Lie algebra structure enters through $D^2[V]$, which is polynomial in $V_\ell$ for any $\mathrm{SU}(N)$. The Neumann series and exponential decay $|G_k(x,y;V)| \leq C e^{-m_W|x-y|}$ generalize immediately because $m_W > 0$ and the lattice Laplacian structure is group-independent. Appendix I.3 tracks the $N$-dependence systematically and confirms all constants are polynomial in $N$.

The extension from SU(2) to SU($N$) is rigorous. No SU(2)-specific property is used that fails for $N \geq 3$.

**(c) The remainder bound.**

The bound $\|E_k\| \leq C g_k^4$ per unit volume is the $L^\infty$ norm on gauge-invariant functionals (the supremum over all gauge field configurations in the small-field region). This follows from the convergent polymer expansion: $|E_k[V]| = |\sum_{X \ni x} K_k(X,V)| \leq \sum_{X \ni x} e^{-\kappa|X|} \leq C_{\mathrm{KP}}(\kappa, d)$, combined with the coupling-dependent normalization from the block-spin structure. The norm is the correct one for bounding spectral shifts (the spectral lemma requires $\|E_k\|_{\mathrm{op}} \leq M$ for the operator norm on the Hilbert space, and $\|\mathcal{O}\|_{\mathrm{op}} \leq \|\mathcal{O}\|_{L^\infty}$ for multiplication operators).

The constant $C$ depends on $N$ through the polymer expansion constants ($\kappa$, $c_d$) and the Lie algebra dimension ($N^2 - 1$). For each fixed $N$, $C$ is a finite constant. Appendix I.3 tracks this dependence explicitly.

**(d) The running coupling.**

The recursion $g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$ with $b_0 = 11N/(48\pi^2)$ is established perturbatively with controlled remainder by Balaban. The $O(g_k^6)$ term at each step accumulates over infinitely many RG steps.

The accumulated correction is controlled by the Gronwall argument (Section 5.4.6): the product $\prod_{j=0}^{k-1}(1 + \alpha g_j^2) \leq \exp(\alpha \sum_j g_j^2)$. Since $g_j^2 \sim 1/(b_0 j \ln 2)$ and $\sum 1/j$ diverges, this grows as $k^{\alpha/(b_0 \ln 2)}$ — a power law. This polynomial growth is overwhelmed by the doubly exponential convergence factor $4^{-k}$ in the mass gap sum. The non-perturbative $\beta$-function is controlled by Balaban's construction: the coupling trajectory stays on the asymptotically free manifold, and the accumulated higher-order corrections produce at most polynomial modifications to the convergence rate.

This analysis is correct. The key insight is that the $4^{-k}$ geometric convergence from the lattice coarsening dominates any polynomial correction from the running coupling.

**(e) Balaban's program completeness.**

The boundary between "what Balaban proved" and "what this paper proves" is precisely drawn in Section 5.1 and PROOF-CHAIN.md (Table IV.2). Balaban proved:
- UV stability (effective action bounded at each step)
- Convergent polymer expansion with $k$-independent $\kappa$
- Running coupling with controlled $\beta$-function
- Irrelevant operator bounds

Balaban did NOT prove:
- Existence of the continuum limit as a QFT
- Mass gap at any lattice spacing
- Confinement
- OS axioms

This paper adds:
- Lattice mass gap $\Delta_0 > 0$ via KK topology + cluster expansion (Theorem 4)
- IR equivalence to standard theory (Theorem 5)
- Stability of deviation order (the key innovation, Section 5.6 Part III)
- Continuum limit with $\Delta_\infty > 0$ (Section 5.7)
- OS axiom verification (Section 5.7(f))

The boundary is explicit, and no unstated assumptions about Balaban's construction are identified. The paper uses Balaban's results as a "black box" at the level of the polymer expansion bounds and effective action structure, which are Balaban's published theorems.

**Impact on the claimed result:**

None. The use of Balaban's RG is within its established scope. The extraction of analyticity properties (B1)-(B2) from Balaban's construction is new but rigorously argued. The boundary between prior results and new contributions is precisely delineated.
