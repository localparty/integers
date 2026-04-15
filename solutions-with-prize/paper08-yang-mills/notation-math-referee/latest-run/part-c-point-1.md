## Part C, Point 1: UV Stability — Precise Scope

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

The claim is that Balaban's UV stability results (CMP 95–119) are used as a "black box" for: convergent polymer expansion, running coupling, irrelevant operator bounds, for general SU($N$).

**(a) The effective action structure.** The decomposition $S_k = (1/g_k^2) S_{\mathrm{YM}} + \sum_n c_n^{(k)} \mathcal{O}_n + E_k$ with $\|E_k\| \leq C g_k^4$ per unit volume is not stated as a single theorem in Balaban. It is inferred from the polymer expansion structure (CMP 109, Thm 1): the effective action is $S_k = (1/g_k^2) S_{\mathrm{YM}} + \sum_X K_k(X,V)$ where each polymer activity $|K_k(X,V)| \leq e^{-\kappa|X|}$. The translation from polymer activities to local operator coefficients with bounds $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$ is standard RG power counting (Wilson–Kogut 1974; Balaban CMP 119, Section 3) but the preprint correctly notes that "the proof uses only the total remainder bound $\|E_k\| \leq C g_k^4$, not individual coefficients" (Section 5.1.3). This is prudent and avoids reliance on an operator decomposition that Balaban does not explicitly provide.

**(b) The gauge group.** This is the main gap in this point. Balaban's published program (CMP 95–119) is stated primarily for SU(2). The preprint's Section 5.1.2 identifies three group-dependent elements: the covariant Laplacian Lipschitz constant $C_D \sim \dim(\mathrm{adj}) = N^2 - 1$, the polymer expansion constant $\kappa(N)$, and the block-spin projection radius $r_{\mathrm{proj}}(N)$. The paper asserts these are all "polynomial in $N$ and do not degrade with $k$" and refers to Appendix I.3 for systematic $N$-dependence tracking.

The extension argument is plausible: Balaban's construction is group-independent in structure, and the $N$-dependent constants are finite for each fixed $N$. However, the extension from SU(2) to SU($N$) has not been published in the literature as a separate theorem. The preprint makes a new claim — that Balaban's UV stability theorem holds for SU($N$) — which requires either (i) a detailed verification of each step in Balaban's 10 papers for general $N$, or (ii) a structural argument that the $N$-dependence is confined to a finite set of constants. The paper provides (ii) but does not give (i). For a Clay submission, option (ii) is acceptable if the structural argument is rigorous, which it appears to be — but this point deserves scrutiny by a referee familiar with Balaban's original proofs.

**(c) The remainder bound.** The bound $\|E_k\| \leq C g_k^4$ per unit volume is in the $L^\infty$ norm on gauge-invariant functionals (Section 5.1.3). The constant $C$ depends on $N$ (through the Lie algebra structure constants) but the paper tracks this through Appendix I.3. The key point is that $C$ is $k$-independent, which follows from Balaban's inductive structure where the convergence constants are refreshed at each step from $k$-independent inputs ($\kappa$, $m_W$, $C_D$).

**(d) The running coupling.** The perturbative running $g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$ with $b_0 = 11N/(48\pi^2)$ is standard. The accumulated higher-order corrections are controlled by the convergence of the product $\prod(1 + O(g_j^4))$, which converges because $\sum g_j^4 \sim \sum 1/j^2 < \infty$ (Basel series). The non-perturbative $\beta$-function is controlled within Balaban's framework through the polymer expansion remainder, which contributes $O(g_k^6)$ corrections that are summable.

**(e) Balaban's program completeness.** The preprint (Section 5.1.5) clearly states what Balaban does NOT prove: the mass gap, confinement, the continuum limit as a QFT, and the spectral response. The boundary between "what Balaban proved" and "what this paper proves" is explicitly drawn. The mass gap at the starting lattice spacing comes from the KK cluster expansion (new), and the preservation through the RG comes from the deviation order argument (new). No unstated assumptions about Balaban's construction are apparent.

**The closable gap:** The SU(2) → SU($N$) extension of Balaban's UV stability. The paper provides a structural argument (Section 5.1.2, Appendix I.3) that is plausible and identifies the correct $N$-dependent parameters, but a complete verification would require checking Balaban's original proofs step-by-step for $N$-dependence. Estimated difficulty: **1 page** of additional argument, primarily collecting the $N$-dependent bounds from each of Balaban's 10 papers and verifying they remain finite for each fixed $N$.

**Impact on the claimed result:**
Affects (iii) the generality claim (SU($N$) for all $N$), not the core result. For SU(2), Balaban's results apply directly. For SU(3) (the physically relevant case), the extension is very plausible but not fully published in the literature.
