## Part C, Point 1: UV Stability — Precise Scope of Balaban's Input

**Weight:** HEAVY
**Verdict:** SOUND WITH CAVEATS (sub-points a, b, c, e); CLOSABLE GAP (sub-point d)

---

**Finding:**

**(a) Operator decomposition from polymer activities.** The preprint writes $S_k = (1/g_k^2) S_{\text{YM}} + \sum_n c_n^{(k)} \mathcal{O}_n + E_k$. This decomposition is not stated as a single theorem in Balaban but is inferred from the structure of his construction.

Balaban's polymer expansion gives $S_k[V] = (1/g_k^2) S_{\text{YM}}[V] + \sum_{X \in \mathcal{P}_k} K_k(X, V)$ with $|K_k(X,V)| \leq e^{-\kappa|X|}$. The translation from polymer activities to local operator coefficients proceeds via the Taylor expansion of $K_k(X, V)$ in $V - \mathbf{1}$ (the block field deviation from the identity), which gives $K_k(X,V) = \sum_n c_n^{(k)}(X) \mathcal{O}_n(X) + \ldots$ where $c_n^{(k)}(X) \sim g_k^{d_n-4}$ from dimensional analysis.

The preprint acknowledges: "Balaban works with polymer activities $K_k(X,V)$, not with an explicit operator decomposition. The translation from polymer activities to local operator coefficients with bounds $|c_n^{(k)}| \leq C_n g_k^{d_n-4}$ — is in CMP 109, Section 2 (which defines $g_{k+1}$ as the coefficient of $S_{\text{YM}}$) and CMP 119. The systematic operator identification is new to this paper (Appendix J)." Section 5.1.3 cites CMP 109 for the effective action structure and CMP 109 Sec. 2 for the coupling renormalization, but the explicit translation to operator form is done in this paper via Appendix J and the PROOF-CHAIN.md [CONFIRMED] items. This attribution is clear and honest. SOUND (with the caveat that the translation is the preprint's work, not Balaban's).

**(b) Extension to SU($N$).** Section 5.1.2 explicitly identifies the three group-dependent elements and argues they are all finite and computable for each fixed $N$: covariant Laplacian ($C_D \sim N^2-1$), polymer convergence $\kappa(N)$, and block-spin projection radius $r_{\text{proj}}(N)$. The statement "All three constants are polynomial in $N$ and do not degrade with $k$" is defended by explicit formulas. The propagator bound (CMP 95, Prop. 1.2) is stated for general compact Lie groups in Balaban's paper (the specific SU(2) case is the primary example, but the proof is group-independent). SOUND.

**(c) The remainder bound norm.** The bound $\|E_k\| \leq C g_k^4$ per unit volume uses the $L^\infty$ norm on gauge-invariant functionals of the block-averaged fields — this is Balaban's natural norm in the small-field region (CMP 109, Sec. 3). Section 5.1.3 states this norm explicitly. The constant $C$ is identified as depending on $N$, $d$, and the blocking geometry $L=2$ but not on $k$. This is stated consistently throughout. SOUND.

**(d) Running coupling and accumulated corrections.** The preprint states $g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$. This is Balaban's perturbative renormalization group equation (CMP 109, Sec. 2). The concern: accumulated higher-order corrections $O(g_k^6)$ over infinitely many steps. The preprint establishes in Section 5.1.4 that the accumulated scale factor $\Lambda_\infty = \prod_{j \geq 0}(1 + O(g_j^4))$ converges since $\sum g_j^4 \sim \sum 1/(j \ln 2)^2 < \infty$.

However, the accumulated $O(g_k^6)$ correction to the *coupling* (not the gap) is:
$$g_k^2 = g_0^2 - b_0 g_0^4 k \ln 2 + O\Bigl(\sum_{j=0}^{k-1} g_j^6\Bigr)$$
Since $g_j^6 \sim 1/(b_0 j \ln 2)^3$ and $\sum_{j=1}^k 1/j^3$ converges, the accumulated correction to $g_k^2$ is $O(g_0^6)$, bounded uniformly in $k$. So the one-loop running coupling formula $g_k^2 \approx g_0^2/(1 + b_0 g_0^2 k \ln 2)$ is accurate up to a bounded error. The non-perturbative $\beta$-function is controlled in the sense that the running coupling remains on the one-loop trajectory with bounded corrections. This is standard (Balaban, CMP 119; Dimock 2011). SOUND.

However, there is a subtlety: Balaban's construction requires $g_0$ small, i.e., $g_0 \leq g_*$ for some threshold $g_*$ that is not quantified in the published papers. The preprint handles this by taking the cluster expansion (valid for all $\beta < 10^{14}$) to provide the starting condition for the Balaban RG at some $g_0 \leq g_*$, with the Remark 1 argument for the finitely many initial steps. This transition argument is informal (Section 5.7, Remark 1) but standard. CLOSABLE GAP for this specific point: the threshold $g_*$ below which Balaban's construction applies is not explicitly given in the preprint. Closing requires citing the explicit smallness condition from Balaban's papers or giving a quantitative bound on $g_*$. Difficulty: **1 paragraph**.

**(e) Completeness of Balaban's program.** Section 5.1.5 explicitly and honestly states what Balaban proves and does not prove: UV stability is proved; mass gap, confinement, continuum limit as QFT, and spectral response are not. The boundary between Balaban's results and this paper's contributions is clearly drawn. The three former [VERIFY] items (analyticity of polymer activities, block-spin kernel complexification, dimension-6 projection exactness) are confirmed in PROOF-CHAIN.md [CONFIRMED] items with self-contained arguments. SOUND.

**Impact on the claimed result:** Sub-point (d) (threshold $g_*$ for Balaban's construction) is a minor closable gap that does not affect the existence of a mass gap but should be made explicit for Clay Prize eligibility. All other sub-points are sound. The attribution of what is Balaban's result vs. this paper's contribution is transparent.
