## Part C, Point 1: UV Stability — Precise Scope

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) The effective action structure.**

The decomposition $S_k = (1/g_k^2) S_{\mathrm{YM}} + \sum_n c_n^{(k)} \mathcal{O}_n + E_k$ is NOT stated as a single theorem in Balaban's papers. Balaban works with polymer activities $K_k(X,V)$ satisfying $|K_k(X,V)| \leq e^{-\kappa|X|}$ (CMP 109, Theorem 1/3). The effective action is the sum $S_k = (1/g_k^2) S_{\mathrm{YM}} + \sum_X K_k(X,V)$.

The translation from polymer activities to local operator coefficients with bounds $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$ is performed in the preprint's Appendix I, Lemma I.1 ("Operator extraction lemma"). This is new to this paper: it Taylor-expands each polymer activity (using analyticity from (B1)) and groups monomials by engineering dimension. The bounds on coefficients then follow from Cauchy estimates and the convergent polymer expansion.

This extraction lemma is a straightforward consequence of the analyticity established in (B1) and the convergence of the polymer expansion. It does not require new mathematics beyond what Balaban proved plus standard complex analysis. However, it is not a citation of an existing result — it is a new (short) argument. This should be acknowledged more clearly.

**(b) The gauge group.**

Balaban's published program is primarily for SU(2). The preprint claims results for general SU($N$). This is the most significant scope extension.

The propagator bounds (CMP 95-96) use properties of the covariant Laplacian $-D^2[V] + m_W^2$, where $D$ is the covariant derivative in the adjoint representation. The key properties — exponential decay $|G_k(x,y;V)| \leq C e^{-m_W|x-y|}$ and analyticity in $V$ — depend on: (i) the spectral gap $m_W^2 > 0$ (universal), (ii) the Lipschitz constant $C_D$ of $D^2$ as a function of $V$ (scales as $N^2 - 1$), (iii) the radius of convergence of the Neumann series for $G_k$.

These generalize to SU($N$) with $N$-dependent constants. The Lipschitz constant grows as $C_D \sim N^2$, which reduces the analyticity radius by $O(1/N^2)$ but does not invalidate the construction for any fixed $N$. The polymer expansion convergence constant $\kappa$ may decrease with $N$ (due to more Lie algebra generators contributing to fluctuations), but remains positive for each fixed $N$.

Appendix I.3 tracks $N$-dependence systematically through all 14 steps. The critical observation is that all $N$-dependent constants are polynomial (or sub-exponential) in $N$, while the convergence factor $4^{-k}$ in the RG sum is $N$-independent.

The gap: Balaban's proofs would need to be checked line-by-line for SU($N$) generality. The preprint asserts this generalization is "standard" and provides the tracking in I.3, but does not reproduce Balaban's proofs for general $N$. For a Clay-level proof, this gap should be closed explicitly.

**(c) The remainder bound.**

The bound $\|E_k\| \leq C g_k^4$ per unit volume follows from: (i) the polymer expansion $\sum_X |K_k(X,V)| e^{\kappa|X|} \leq C_{\mathrm{KP}}$ (from Kotecký-Preiss); (ii) subtracting $(1/g_k^2) S_{\mathrm{YM}}$; (iii) using $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$ with $d_n \geq 6$ giving $|c_n^{(k)}| \leq C_n g_k^2$; (iv) summing over operators.

The norm is the $L^\infty$ norm on gauge-invariant functionals: $\|E_k\| = \sup_{V \in \Omega_s} |E_k(0)[V]|$ where $\Omega_s$ is the small-field region. This is the correct norm for the spectral lemma application, which requires $\|\mathcal{O}\| \leq M$.

The constant $C$ depends on $N$ (through Lie algebra dimensions and combinatorial factors). For each fixed $N$, $C(N)$ is finite. This is verified in I.3.

**(d) The running coupling.**

The perturbative $\beta$-function $g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$ with $b_0 = 11N/(48\pi^2)$ is established by Balaban with controlled remainder. The accumulation of $O(g_k^6)$ corrections over infinitely many steps is controlled by Balaban's inductive hypotheses: at each step, the coupling is defined as the coefficient of $S_{\mathrm{YM}}$ in the effective action, and the deviation from the perturbative trajectory satisfies $|g_k^2 - g_k^{2,\mathrm{pert}}| \leq C g_k^6$.

The non-perturbative $\beta$-function is controlled in Balaban's framework: the polymer expansion provides uniform bounds on the effective action at each step, and the coupling renormalization is exact (since $S_{\mathrm{YM}}$ is the unique dimension-4 operator). The accumulated higher-order corrections satisfy $\sum_{j=0}^{k-1} O(g_j^6) \leq C \sum_j 1/(b_0 j \ln 2)^3 < \infty$ (convergent Basel-type series), so the trajectory stays close to the perturbative one for all $k$.

**(e) Balaban's program completeness.**

The boundary between "what Balaban proved" and "what this paper proves" IS precisely drawn in Section 5.1 and PROOF-CHAIN.md. Balaban proved: UV stability, convergent polymer expansion, running coupling with controlled remainder, propagator bounds. This paper proves: lattice mass gap (Theorems 1-5), the operator extraction (I.1), the analyticity properties (B1)-(B2) as consequences of Balaban's construction, the dimension-6 classification and deviation order argument, and the continuum limit.

The preprint does not claim that Balaban proved the continuum limit or the mass gap. It uses Balaban's results as input for the RG analysis and proves the new results (spectral lemma, deviation order stability, RG recursion convergence).

**Closing the gap:** The main closable item is (b): the extension of Balaban's results to SU($N$). This requires either (i) a detailed verification that Balaban's proofs generalize (estimated: 1 paper, but the paper need only verify, not re-derive), or (ii) a statement that the proof is carried out for each fixed $N$ with the understanding that Balaban's construction generalizes with $N$-dependent constants (which the preprint already provides in I.3). For a Clay submission, option (i) would be stronger. Difficulty: 1 page for the statement, ~10 pages for the verification.

**Impact on the claimed result:** (iii) Potentially affects Clay prize eligibility. The extension to SU($N$) relies on asserting that Balaban's construction generalizes, which is mathematically plausible but not published in the literature. A referee for the Clay prize would likely request explicit verification.
