## Part C, Point 1: UV Stability — Precise Scope

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

The claim: Section 5.1 uses Balaban's results as a "black box": UV stability, convergent polymer expansion, running coupling, irrelevant operator bounds.

**(a) The effective action structure.** The decomposition S_k = (1/g_k^2) S_YM + Sum c_n O_n + E_k is NOT a theorem in Balaban's papers. Balaban works with polymer activities K_k(X,V), not with an explicit operator decomposition. The translation is new to this paper and is performed in the Extraction Lemma (Appendix I, Section I.1).

The Extraction Lemma proceeds by Taylor-expanding each analytic polymer activity K_k(X,V) around V = 1 (the identity configuration). The analyticity (B1) ensures convergence. Each order in the expansion corresponds to operators of a specific engineering dimension. The dimension-4 part is uniquely S_YM (by the uniqueness argument in PROOF-CHAIN IV.3). The remainder at dimension 6 satisfies |c_n^{(k)}| <= C_n g_k^{d_n - 4}.

This extraction is rigorous given the analyticity of the polymer activities and the absolute convergence of the polymer expansion. The Taylor expansion of a convergent sum of analytic functions is itself convergent, with coefficients bounded by Cauchy estimates. The operator dimensions are well-defined on the lattice (determined by the number of link variables in each Taylor monomial).

The Extraction Lemma is a genuine new contribution. It is straightforward functional analysis, not deep mathematics, but it fills an important gap between Balaban's polymer formalism and the operator language needed for the spectral argument.

**(b) The gauge group.** Balaban's published program treats SU(2) explicitly. The extension to SU(N) is argued in Section 5.1 and Appendix I.4. The three group-dependent elements are:

(i) The covariant Laplacian: D^2[V] depends polynomially on V through the adjoint representation. The Lipschitz constant C_D scales as dim(adj) = N^2 - 1.

(ii) The propagator bounds: G_k(V) = (-D^2[V] + m_W^2)^{-1} is analytic with radius depending on C_D and m_W (both k-independent). For SU(N), the radius is r ~ 1/C_D ~ 1/N^2 (from I.3).

(iii) The polar decomposition: A -> A(A^dagger A)^{-1/2} has radius r_proj(N) = 1/2 (independent of N, as verified in PROOF-CHAIN IV.3).

Balaban's construction is structurally group-independent: every step (background evaluation, saddle point, Gaussian integration, Mayer resummation) is algebraic in nature and applies to any compact Lie group. The group enters only through specific constants. For each fixed N, these constants are finite and the construction goes through.

This is not a gap — Balaban himself notes the group-independence of the structure (CMP 109, Section 1). The explicit N-tracking in I.3 confirms that all constants are finite for each N.

**(c) The remainder bound.** ||E_k|| <= C g_k^4 per unit volume. This follows from the polymer expansion: the sum Sum_X |K_k(X)| e^{-kappa|X|} converges to give the total remainder bounded by C g_k^4 (since each polymer activity has dimension >= 6 and coefficient <= C g_k^{d-4}, the dominant contribution is dimension 6 with coefficient ~ g_k^2, squared to give g_k^4 in the norm).

The norm is the L^infty norm on gauge-invariant functionals in the small-field domain Omega_s. This is the correct norm for the spectral lemma application (the operator norm M in the spectral lemma). The constant C depends on N (through the number of operators and their coefficients) but is finite for each fixed N.

**(d) The running coupling.** g_{k+1}^2 = g_k^2 - b_0 g_k^4 ln 2 + O(g_k^6) with b_0 = 11N/(48 pi^2). Balaban establishes this with controlled O(g_k^6) remainder. The accumulated correction over K steps:

  Sum_{k=0}^K O(g_k^6) ~ Sum 1/k^3 (on the AF trajectory)

This sum converges (p-series with p = 3 > 1). So the accumulated higher-order corrections are bounded by a finite constant. The non-perturbative beta-function is controlled through the polymer expansion at each step — the coupling g_k is defined as the coefficient of S_YM in the effective action, and the polymer expansion gives the next-step coupling with controlled remainder.

**(e) Balaban's program completeness.** The boundary between Balaban's results and the paper's new results is clearly drawn:

**Balaban provides:** UV stability (effective action bounded), polymer convergence (kappa k-independent), running coupling control (O(g_k^6) remainder), propagator bounds (exponential decay with k-independent parameters).

**The paper provides:** (i) Mass gap at starting scale (KK mechanism, Section 4); (ii) Stability of deviation order (Section 5.5-5.6, the key innovation); (iii) RG recursion and convergence (Section 5.4); (iv) Continuum limit construction (Section 5.7).

The paper does not claim that Balaban proved the continuum limit — it explicitly acknowledges (Section 5.1.5) that Balaban proved UV stability but not the existence of the continuum limit. The gap between "UV stability" and "mass gap in the continuum" is bridged by the paper's new arguments.

Are there unstated assumptions about Balaban's construction? The three [VERIFY] items (polymer analyticity, k-independent radius, complexification) have been confirmed by explicit argument in PROOF-CHAIN IV.3. The arguments are self-contained and have been validated by the r03 and r06 referee reports.

No error found. The use of Balaban's results is within their stated scope, the extension to SU(N) is properly argued, and the boundary with new results is clearly delineated.

**Impact on the claimed result:** None. The Balaban inputs are used correctly, and the translation to the operator language (Extraction Lemma) is a valid new contribution.
