## Part D, Point 2: Stability of Boltzmann Deviation Order

**Weight:** HEAVY
**Verdict:** SOUND

This is the single most important technical innovation in the paper. I scrutinize each sub-question with maximum skepticism.

**Finding:**

**(a) The definition of Boltzmann deviation order.**

Definition D.2 defines $\mathrm{dev}(\mathcal{O}) \geq p$ in terms of a factorization of the spectral weight: the total weight $W_\alpha^{(m)}(\mathbf{n}) e^{-E(\mathbf{n})}$ must contain $\geq p$ factors of the form $(e^{E_m - E_{n_j}} - 1)$ with bounded residual.

This definition IS equivalent to the intuitive notion "the connected matrix element is bounded by $C\hat{\Delta}^p$." The spectral lemma (Section 5.5.3) proves the implication: $\mathrm{dev} \geq p \implies |\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$.

The converse is also essentially true: if the connected matrix element is $O(\hat{\Delta}^p)$ for structural reasons (not coincidental cancellation), then the weight function admits the required factorization. The definition captures the structural property, not just the numerical bound.

Could an operator satisfy Definition D.2 but fail to give the $\hat{\Delta}^p$ bound? No — the spectral lemma is a theorem, not a heuristic. Could an operator give the $\hat{\Delta}^p$ bound without satisfying Definition D.2? In principle yes (via coincidental cancellation), but the paper does not rely on this direction. The proof uses $\mathrm{dev} \geq 2 \implies$ bound, not the converse.

**(b) The linear combination lemma.**

The lemma states: if each $\mathcal{O}_i$ has $\mathrm{dev} \geq p$ and $\sum |c_i| \|\mathcal{O}_i\| < \infty$, then $\sum c_i \mathcal{O}_i$ has $\mathrm{dev} \geq p$.

The concern about operators with different temporal supports is valid. If $\mathcal{O}_i$ has temporal extent $R_i$ and the sum has temporal extent $R = \max_i R_i$, then shorter operators must be embedded in the maximal representation by "zero-padding" (inserting identity time slices).

Zero-padding preserves deviation structure: inserting $\hat{T}$-insertions at identity produces intermediate sums $\sum_n |n\rangle e^{-E_n}\langle n|$, which is the transfer matrix itself. The additional factors in the weight function are $1 \cdot e^{-E_n}$ (the identity operator contributes $\delta_{n,n'}$ matrix elements). The deviation factors $(e^{E_m - E_n} - 1)$ at the padded slots are not extracted — they contribute to the residual weight. Since $|e^{E_m - E_n} - 1| \leq C$ (bounded), the residual weight bound $\tilde{W}_\alpha$ is multiplied by at most $C^{R-R_i}$ per padded slot. This is bounded because $R$ is bounded (operators have finite temporal extent in lattice units) and $C$ is a finite constant.

Section 5.5.3 handles this implicitly by working with a common temporal extent $R$ for all operators in the sum. The proof is correct.

**(c) The role of (B1) analyticity.**

The convergent Taylor expansion (from analyticity with $k$-independent radius $\rho$) ensures $\delta E_k^{d=6}$ is a genuine convergent sum of gauge-invariant monomials, not a formal asymptotic series. The analyticity radius $\rho$ determines the domain of convergence.

The concern: do typical configurations in the gapped phase lie within the analyticity domain? In the small-field region $\Omega_s$, the Taylor expansion converges by construction (B1). The matrix element $\langle 1|\delta E_k^{d=6}|1\rangle_c$ receives contributions from all configurations, but:

1. Configurations in $\Omega_s$ contribute within the convergence domain — the Taylor expansion applies.
2. Configurations in $\Omega_l$ (near or beyond the boundary of $\Omega_s$) contribute at level $O(e^{-c/g_k^{2\epsilon}})$ by Balaban's large-field bounds.

The one-particle state $|1\rangle$ in the gapped phase has support dominated by typical (small-field) configurations. The probability of atypical (large-field) configurations is exponentially suppressed. Therefore the matrix element is dominated by the small-field contribution, where the Taylor expansion converges.

The spectral lemma applies to the operator on $\Omega_s$ (where (B1) guarantees convergent expansion), and the $\Omega_l$ contribution is separately bounded by $O(e^{-c/g_k^{2\epsilon}})$, which is negligible. This two-part structure is correct.

**(d) The transition from perturbative to non-perturbative.**

The r05 referee initially flagged this as a GENUINE GAP, then revised to CLOSABLE. The key insight — which I concur with — is that the classification is *exhaustive*: every dimension-6 $\mathcal{C}$-even operator has $\mathrm{dev} \geq 2$ by its structural properties (two covariant derivatives producing two factors of $e^{E_m - E_n} - 1$ in the transfer matrix), not by perturbative identification of specific operators.

The "dimension-6 part" of the effective action is defined by projecting out the dimension-4 component $(S_{\mathrm{YM}}/g_k^2)$. This projection requires $S_{\mathrm{YM}}$ to be the unique dimension-4 operator, which is confirmed in PROOF-CHAIN.md IV.3. The uniqueness argument is non-perturbative: on the hypercubic lattice, $s_P^2$ has dimension 8, $\mathrm{Tr}(F\tilde{F})$ is parity-odd, and redundant operators (vanishing by EOM) are not generated by the block-spin. The subtraction is exact.

The projection is well-defined non-perturbatively because the analyticity (B1) provides a convergent expansion from which the dimension-4 component (the coefficient of $S_{\mathrm{YM}}$) can be unambiguously extracted. The remainder is a convergent sum of operators of dimension $\geq 6$, with the dimension-8+ contributions separately bounded by $g_k^4 \hat{\Delta}_k^4$ (even stronger suppression). The "dimension-6 part" is the dominant remainder after subtracting dimension-4 and bounding dimension-8+.

**(e) Structural zero vs. kinematic zero.**

The diagonal vanishing $(e^{E_1 - E_1} - 1)^2 = 0$ is structural: it arises from the squared-derivative structure of dimension-6 operators, not from a specific numerical coincidence.

The deviation order involves the spectral weight $W_\alpha^{(m)}(\mathbf{n})$, which depends on the specific operator through its multi-time-slice decomposition. For the non-perturbative $\delta E_k^{d=6}$, the spectral weights are not computed explicitly. Instead, they are inferred from the classification: $\delta E_k^{d=6}$ is a convergent sum of operators, each with $\mathrm{dev} \geq 2$.

The concern about cancellations: can $\mathrm{dev} \geq 2$ for each term but $\mathrm{dev} < 2$ for the sum? The linear combination lemma (Section 5.5.3) proves this CANNOT happen. The proof: deviation order is defined at the level of the spectral weight factorization. For each term $c_i \mathcal{O}_i$ with $\mathrm{dev}(\mathcal{O}_i) \geq 2$, the weight admits $\geq 2$ factors of $(e^{E_m - E_n} - 1)$ with bounded residual. The sum's weight at each $(\alpha, \mathbf{n})$ is $\sum_i c_i W_{\alpha_i}^{(m)}(\mathbf{n})$. Each term has the required factorization. Cancellations between terms can reduce the total weight but CANNOT remove the zero at $n_j = m$ (structural zeros cannot be cancelled by adding more zeros). The total weight still vanishes at the diagonal to order $\geq 2$.

More precisely: if $W_i(\mathbf{n}) = \tilde{W}_i(\mathbf{n}) \cdot \prod_{j=1}^{p_i} (e^{E_m - E_{n_{\sigma_i(j)}}} - 1)$ with $p_i \geq 2$, then cancellation between different $W_i$ at the diagonal (where $\prod = 0$) gives $0 - 0 = 0$. Away from the diagonal, cancellations can reduce magnitude but do not affect the vanishing structure.

I verify the proof handles cancellations correctly. It does.

**Impact on the claimed result:**

None. The stability of deviation order argument is the central innovation. After careful examination of all five sub-questions, I find the argument correct. The key elements — (B1) analyticity ensuring convergent expansion, exhaustive dimension-6 classification, linear combination lemma preserving deviation order, and unique dimension-4 projection — fit together without gaps. The structural nature of the vanishing (not kinematic coincidence) is correctly established.
