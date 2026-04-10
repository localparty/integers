## Part D, Point 2: Stability of Boltzmann Deviation Order

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

This is the single most important technical innovation in the paper. The claim is that the full non-perturbative operator $\delta E_k^{d=6}$ has $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$, established by (B1) analyticity, the dimension-6 classification, and the linear combination lemma.

**(a) The definition of Boltzmann deviation order.** Definition D.2 (Section 5.5.2) defines $\mathrm{dev}(\mathcal{O}) \geq p$ by requiring that the spectral weight $W_\alpha^{(m)}(\mathbf{n}) \cdot e^{-E(\mathbf{n})}$ admits a factorization of $p$ powers of $(e^{E_m - E_{n_j}} - 1)$ from the weight, with bounded residual. This is equivalent to the weight vanishing to order $\geq p$ at the diagonal configuration $\mathbf{n} = (m, \ldots, m)$.

The definition is stronger than the intuitive notion "the connected matrix element is $O(\hat{\Delta}^p)$": it requires the factorization to hold term-by-term in the spectral sum, not just for the total. The Spectral Lemma (Section 5.5.3) then converts $\mathrm{dev} \geq p$ to the bound $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$. The definition is well-chosen because it is stable under linear combinations (see (b) below) and computable from the operator structure.

**(b) The linear combination lemma.** If each $\mathcal{O}_i$ has $\mathrm{dev} \geq p$ and $\sum |c_i| \|\mathcal{O}_i\| < \infty$, then $\sum c_i \mathcal{O}_i$ has $\mathrm{dev} \geq p$. The proof is straightforward: the combined spectral representation indexed by pairs $(i, \alpha_i)$ inherits the factorization from each term, with total residual bound $M = \sum |c_i| \|\mathcal{O}_i\|$. The concern about different temporal extents $R_i$ is addressed by the paper's Remark on uniform temporal extent: Balaban's polymer expansion generates operators with temporal support bounded by $R_0$ block lattice units (CMP 109, Theorem 1), so $R_i \leq R_0$ uniformly. Zero-padding shorter operators to the maximal extent $R_0$ preserves the deviation structure because inserting identity time slices (diagonal contributions with $e^{E_m - E_m} - 1 = 0$) does not reduce the vanishing order.

Can $\mathrm{dev} \geq 2$ for each term but $\mathrm{dev} < 2$ for the sum via cancellations? No. The linear combination lemma explicitly handles this: deviation order is defined at the level of individual spectral weights, and the absolute convergence $\sum |c_i| \|\mathcal{O}_i\| < \infty$ prevents cancellations from degrading the vanishing order. The triangle inequality applies to the residual bounds, not to the deviation factors themselves. This is correct.

**(c) The role of (B1) analyticity.** (B1) guarantees that $\delta E_k^{d=6}$ is a convergent (not formal) sum of monomials within the analyticity domain of radius $\rho > 0$. The spectral lemma requires the expansion to converge on configurations contributing to the matrix element $\langle 1|\delta E_k^{d=6}|1\rangle_c$. The one-particle state $|1\rangle$ is a zero-momentum state with support on typical configurations in the gapped phase.

In the small-field domain $\Omega_s$, typical configurations satisfy $|F_{\mu\nu}| < g_k^{1-\epsilon}$, which is well within the analyticity domain $\rho > 0$ (since $\rho$ is $k$-independent and $g_k \to 0$). The measure on the one-particle state concentrates on these typical configurations by the exponential clustering (Hastings–Koma) established in Section 5.5.3 Step 3(i). Large-field configurations contribute $O(e^{-c/g_k^{2\epsilon}})$ to any matrix element, which is negligible. So yes, the analyticity domain contains the support of the physically relevant matrix elements.

**(d) The transition from perturbative to non-perturbative.** This is the key insight of the paper. The naive approach (splitting $\mathcal{O} = \mathcal{O}^{\mathrm{pert}} + \delta\mathcal{O}$ with $\|\delta\mathcal{O}\| \leq C g_k^6$) fails because the non-perturbative remainder gives $|\langle 1|\delta\mathcal{O}|1\rangle_c| \leq C g_k^6/\hat{\Delta}^3$, which requires $g_k^2 \leq \hat{\Delta}^5$ — impossible on the AF trajectory.

The correct approach bypasses the split entirely: it classifies ALL $\mathcal{C}$-even dimension-6 operators (perturbative and non-perturbative alike) by their structural properties. Since every such operator is a two-derivative operator (Classes I-II being absent), it carries the squared deviation factor $(e^{E_m - E_n} - 1)^2$ from the temporal derivative structure. This is a property of the **operator class**, not of perturbation theory. The dimension-4 projection is exact because $S_{\mathrm{YM}}$ is unique (PROOF-CHAIN IV.3): any "dimension-4 contamination" in the remainder would contradict this uniqueness.

**(e) Structural zero vs. kinematic zero.** The diagonal vanishing $(e^{E_1 - E_1} - 1)^2 = 0$ is structural: it arises from the squared-derivative structure of dimension-6 operators, which forces the spectral weight to vanish at $n_j = m$ regardless of the specific values of $E_m$. This is verified explicitly for $\mathrm{Tr}(D_0 F)^2$ in Section 5.5.4: the factor $(e^{E_m - E_n} - 1)^2$ appears naturally in the spectral sum $\sum_n (e^{E_m - E_n} - 1)^2 |\langle m|F|n\rangle|^2$.

The concern about cancellations in convergent sums is addressed by the linear combination lemma (part (b) above): absolute convergence prevents the deviation order from degrading. The spectral weights of the non-perturbative sum $\delta E_k^{d=6}$ inherit the $\mathrm{dev} \geq 2$ property term-by-term from the classification.

**Impact on the claimed result:**
This is the central technical innovation. If it is correct (and I find no error), it closes the gap between perturbative and non-perturbative control of irrelevant operators. The argument is elegant: instead of trying to bound non-perturbative corrections directly, it classifies all possible operators by symmetry and dimension, showing that the suppression is universal.
