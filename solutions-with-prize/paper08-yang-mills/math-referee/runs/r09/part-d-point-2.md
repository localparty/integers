## Part D, Point 2: Stability of Boltzmann Deviation Order

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

This is the single most important technical innovation in the paper. I have scrutinized it with particular care.

**(a) The definition of Boltzmann deviation order.** Definition D.2 (Section 5.5.2) defines dev$(\mathcal{O}) \geq p$ in terms of a factorization of the spectral weight: the weight $W_\alpha^{(m)}(\mathbf{n}) \cdot e^{-E(\mathbf{n})}$ must admit $p$ factors of $(e^{E_m - E_{n_j}} - 1)$ with bounded residual. This is equivalent to the statement that the total weight vanishes to order $\geq p$ at the diagonal $\mathbf{n} = (m, m, \ldots, m)$.

The definition is stronger than the intuitive notion "the connected matrix element vanishes to order $p$ in $\hat{\Delta}$" — it requires the vanishing to hold term-by-term in the spectral sum, not just in the total. This is exactly what the spectral lemma needs: the bound (S1.3) extracts $p$ factors of $C\hat{\Delta}$ from each term individually.

The definition is weaker than requiring $\#(\mathbf{n}) \geq p$ (the excitation number criterion): dev $\geq p$ allows low-excitation channels to be present, provided their weight vanishes to the required order. This is precisely the situation for $\mathrm{Tr}(D_0 F)^2$, where the $n = m$ channel has nonzero spectral weight but the Boltzmann factor $(e^{E_m - E_n} - 1)^2$ provides two vanishing powers.

No pathology: an operator satisfying Definition D.2 with $p$ factors does give the $\hat{\Delta}^p$ bound (this is the content of the spectral lemma, Step 1).

**(b) The linear combination lemma.** The lemma states that dev $\geq p$ is preserved under convergent linear combinations. The proof (Section 5.5.3) is elementary: the combined operator $\mathcal{O} = \sum_i c_i \mathcal{O}_i$ has spectral representation indexed by pairs $(i, \alpha_i)$, and the weight $c_i W_{\alpha_i,i}^{(m)}(\mathbf{n}) e^{-E(\mathbf{n})}$ inherits the factorization from $W_{\alpha_i,i}^{(m)}(\mathbf{n}) e^{-E(\mathbf{n})}$. The total residual bound is $\sum_i |c_i| \|\mathcal{O}_i\| = M < \infty$.

The concern about operators with different temporal supports $R_i$: if $\mathcal{O}_i$ has temporal extent $2R_i$ and $\mathcal{O}_j$ has extent $2R_j$ with $R_i < R_j$, the shorter operator can be embedded in the longer representation by inserting identity time slices. The identity insertion $\hat{T}\hat{T}^{-1} = \mathbf{1}$ at each additional slot does not affect the spectral weight (it multiplies by $\sum_n |n\rangle\langle n| = \mathbf{1}$, distributing the weight over all intermediate states but preserving the deviation structure). The padded weight $W_\alpha^{(m)}(\mathbf{n}_{\mathrm{padded}})$ at the additional slots is $\delta_{n_j, n_{j-1}}$ (identity insertion), which vanishes to order 0 at the diagonal — but the existing $p$ deviation factors from the original slots are preserved.

This is handled implicitly in the proof. An explicit statement would be helpful but is not mathematically necessary.

**(c) The role of (B1) analyticity.** The analyticity with $k$-independent radius $\rho$ (established in Section 5.6, Part I) ensures that $\delta E_k^{d=6}$ has a convergent Taylor expansion in the field variables. This is essential: without convergence, the "dimension-6 part" would be only an asymptotic concept, and the classification argument could not be applied to the non-perturbative object.

The concern about configurations near the boundary of $\Omega_s$: the spectral lemma requires the bound on $\langle 1|\delta E_k^{d=6}|1\rangle_c$, which is a matrix element, not a pointwise bound on configurations. The one-particle state $|1\rangle$ has support on typical configurations in the gapped phase. In the gapped phase, typical configurations have $|F_{\mu\nu}| = O(g_k)$ (fluctuations of order the coupling), which is well within the small-field region $|F_{\mu\nu}| < g_k^{1-\epsilon}$ for $g_k$ small. The atypical configurations near the boundary of $\Omega_s$ contribute to the matrix element at the level $O(e^{-c/g_k^{2\epsilon}})$ (from the large-field suppression), which is negligible.

**(d) The transition from perturbative to non-perturbative.** The r05 referee initially flagged this as a GENUINE GAP, then revised to CLOSABLE after careful re-examination. The key insight, which I verify:

The classification IS exhaustive: every dim-6 $\mathcal{C}$-even operator has dev $\geq 2$ by structure. This is NOT a perturbative identification — it is a structural property of the operator class. The non-perturbative operator $\delta E_k^{d=6}$ is a convergent linear combination (by (B1)) of operators in this class. The linear combination lemma preserves dev $\geq 2$.

The dimension-6 projection IS exact because $S_{\mathrm{YM}}$ is the unique dimension-4 operator. The subtraction $E_k = S_k - (1/g_k^2)S_{\mathrm{YM}} - \mathcal{E}_0 V$ removes all dimension-4 content. What remains is genuinely dimension $\geq 6$ (by the convergent Taylor expansion from (B1)).

I find this argument logically correct.

**(e) Structural zero vs. kinematic zero.** The diagonal vanishing $(e^{E_1 - E_1} - 1)^2 = 0$ for $\mathrm{Tr}(D_0 F)^2$ arises from the squared-derivative structure: the operator is a square of first-order temporal differences, producing $(e^{E_m - E_n} - 1)^2$ as a common factor. This is structural (following from the operator being a sum of squares) rather than kinematic (a numerical coincidence).

The concern about cancellations in the linear combination: can $\mathrm{dev} \geq 2$ for each term but $\mathrm{dev} < 2$ for the sum? No. The linear combination lemma proves this directly: the spectral weight of the sum is the sum of the spectral weights, and if each weight vanishes to order $\geq 2$ at the diagonal, the sum does too. Cancellations between terms can only increase the vanishing order, not decrease it — because the factorization (D.2) holds term-by-term for each $\alpha'$, and the spectral lemma bounds each term individually before summing.

**Impact on the claimed result:** None. The stability of deviation order argument is the genuine innovation of this paper, and it is correct.
