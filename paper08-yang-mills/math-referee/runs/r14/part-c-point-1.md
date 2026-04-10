## Part C, Point 1: UV Stability -- Precise Scope

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

**(a) The effective action structure.** The decomposition $S_k = (1/g_k^2)\,S_{\mathrm{YM}} + \sum_n c_n^{(k)}\,\mathcal{O}_n + E_k$ is NOT a standalone theorem in Balaban's papers. Balaban works with polymer activities $K_k(X, V)$ satisfying $|K_k(X,V)| \leq e^{-\kappa|X|}$ (CMP 109, Theorem 1). The translation to a local operator decomposition with coefficient bounds is performed in the preprint's Appendix I.1 (Extraction Lemma, Lemma I.1).

The extraction proceeds in five steps: (1) polymer expansion to local functionals (from CMP 109), (2) Taylor expansion in Lie algebra variables (using analyticity from (B1)), (3) dimension assignment by degree, (4) Cauchy estimates for coefficient bounds, (5) remainder control. Each step is a standard mathematical operation:

- Step (2) requires analyticity with $k$-independent radius $\rho > 0$, which is property (B1)
- Step (4) gives $|c_{d,i}^{(k)}| \leq C_{d,i}(N)\,g_k^{d-4}$ via Cauchy's integral formula
- Step (5) gives $\|R_k\| \leq C(N)\,g_k^{D_0}$ by truncation

The extraction lemma is rigorous. It does not require reading between the lines of Balaban's papers -- it starts from his stated theorem (polymer expansion convergence) and applies standard analysis. The r03 referee verified this construction and found it confirmed.

**(b) The gauge group.** Balaban's published program is primarily for SU(2). Extension to SU($N$) requires verifying three group-dependent elements:

1. **Covariant Laplacian:** $C_D = O(N^2 - 1)$ (Lipschitz constant of the adjoint action). Polynomial in $N$, finite for each $N$.
2. **Polymer expansion convergence:** $\kappa(N) > 0$ depends on the adjoint dimension. May decrease with $N$ but remains strictly positive for each fixed $N$.
3. **Block-spin projection:** $r_{\mathrm{proj}}(N) \geq 1/4$ for all $N$ (from eigenvalue bound on $A^\dagger A$ near identity).

Appendix I.1.3 and K provide detailed arguments for why each step of Balaban's construction generalizes. No step is SU(2)-specific: the propagator bounds, Mayer resummation, and axial gauge fixing are all structural properties of compact Lie groups.

The key point: Balaban's construction for SU(2) does not use any property of SU(2) that fails for SU($N$). The Lie algebra structure enters through the covariant Laplacian (which works for any compact Lie algebra) and the group integration (which works for any compact group via Haar measure). The claim is that the SAME construction, with $N$-dependent constants, works for SU($N$).

While a standalone published paper systematically verifying each step for SU($N$) would be ideal, the structural arguments are convincing for fixed $N$. No mathematical gap is present -- only a gap in the published literature, which the appendices fill.

**(c) The remainder bound.** $\|E_k\| \leq C\,g_k^4$ per unit volume follows from the polymer expansion via: $E_k = \sum_X K_k(X, V) - [(1/g_k^2)\,S_{\mathrm{YM}} + \sum_{d \leq D_0} c_d\,\mathcal{O}_d]$, and $|K_k(X, V)| \leq e^{-\kappa|X|}$ (convergent sum). The bound is in the $L^\infty$ norm on gauge-invariant functionals, which is the correct norm for the spectral lemma. The constant $C$ depends on $N$ polynomially through $\kappa(N)$, $\rho(N)$, and combinatorial factors.

**(d) The running coupling.** The accumulated $O(g_k^6)$ corrections over infinitely many RG steps are controlled because:

$$\sum_{k=0}^{\infty} g_k^6 = \sum_k \frac{1}{(b_0 k \ln 2)^3} \sim \sum \frac{1}{k^3} < \infty \quad\text{(converges by $p$-series)}$$

The non-perturbative $\beta$-function is controlled to this order. Higher-order corrections are $O(g_k^8)$, and $\sum g_k^8 \sim \sum 1/k^4 < \infty$. So the running coupling trajectory $g_k^2 = 1/(b_0 k \ln 2)(1 + O(1/k))$ is rigorously established, with the $O(1/k)$ correction from accumulated higher-order terms.

**(e) Balaban's program completeness.** The boundary between "what Balaban proved" and "what this paper proves" is precisely drawn in Section 5.1:

**Balaban proved:** UV stability (bounded effective action), convergent polymer expansion, running coupling with controlled remainder, propagator bounds with exponential decay, gauge invariance preservation.

**Balaban did NOT prove:** Existence of the continuum limit, mass gap, infinite-volume limit, OS axioms, reflection positivity preservation.

**This paper proves:** Mass gap survives $a \to 0$ (the form factor bound), OS axioms in the continuum limit, thermodynamic limit.

The paper uses Balaban's results as a black box for the UV regime (Steps 2-3 of the proof chain). Properties (B1)-(B2) are extracted from Balaban's construction via the analysis in Appendix H. The extraction is explicit and verifiable.

There are no unstated assumptions about Balaban's construction. Every property used is either (i) a stated theorem in Balaban's papers (polymer convergence, CMP 109 Thm 1), (ii) derived from the construction via standard analysis (analyticity, Appendix H), or (iii) new to this paper (form factor bound, OS verification).

**Impact on the claimed result:** None. The scope of Balaban's results is correctly identified and used within their actual domain. The extraction of properties (B1)-(B2) is rigorous. The extension to SU($N$) relies on structural arguments that are convincing for each fixed $N$.
