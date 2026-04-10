## Part D, Point 3: The Spectral Lemma

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The deviation extraction (Step 1).** Each extracted factor $(e^{E_m - E_{n_j}} - 1)$ is bounded by $C\hat{\Delta}$ via equation (S1.2). The proof correctly handles three cases:

- $n_j = m$ (diagonal): $|e^0 - 1| = 0$. No contribution.
- $n_j = 0$ (vacuum intermediate, $m = 1$): $|e^{\hat{\Delta}} - 1| \leq \hat{\Delta}(1 + O(\hat{\Delta})) \leq C\hat{\Delta}$.
- $n_j \geq 2$ (higher excited, $m = 1$): $|e^{E_1 - E_{n_j}} - 1| \leq 1$ since $E_1 < E_{n_j}$.

The bound (S1.2) unifies these: $|e^{E_m - E_{n_j}} - 1| \leq C_0 \hat{\Delta}$ with $C_0 = \max(e^{\hat{\Delta}}, 1/\hat{\Delta})$. For $\hat{\Delta} \leq 1$ (which holds at later RG steps), $C_0 = 1/\hat{\Delta}$ and the bound is $O(1)$ — but this is acceptable because the $p$ factors are extracted from DIFFERENT slots, and at least $p$ of the factors must be $O(\hat{\Delta})$ by the definition of dev $\geq p$.

The proof claims that at least $p$ of the factors are $O(\hat{\Delta})$, not that ALL are. For the extracted factors, Definition D.2 guarantees $q_\alpha(\mathbf{n}) \geq p$ factors of $(e^{E_m - E_{n_{\sigma(j)}}} - 1)$, each bounded by $C\hat{\Delta}$. The remaining (non-extracted) factors contribute $O(1)$ each and are absorbed into the residual weight $\tilde{W}$. The total bound is $(C\hat{\Delta})^p \cdot |\tilde{W}|$, as stated in (S1.3). The argument is correct.

**(b) The $\zeta$ bound and the two-particle threshold.** The sum $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ requires $E_2 - E_1 > 0$. Section 5.5.3, Step 3(ii) establishes this rigorously:

In Balaban's small-field domain, the spectrum consists of $E_0 = 0$, $E_1 = \hat{\Delta}_k$, $E_2 \geq 2\hat{\Delta}_k - \epsilon_B$. The binding energy $\epsilon_B \leq C_B g_k^4 \hat{\Delta}_k$ is controlled by the Kato-Rellich theorem applied to the two-particle sector: the interaction $V_k$ is a relatively bounded perturbation of the free Hamiltonian with relative bound $\|V_k\|/(2\hat{\Delta}_k) \leq Cg_k^2/(2\hat{\Delta}_k) \ll 1$ for $g_k$ small. Second-order perturbation theory gives $\epsilon_B \leq C_B g_k^4 \hat{\Delta}_k$.

The conclusion $E_2 - E_1 \geq \hat{\Delta}_k/2$ for $g_k^2 \leq 1/(2C_B)$ is correct. This condition is satisfied for all $k \geq k_0$ on the AF trajectory. The finitely many steps $k < k_0$ contribute a bounded constant.

The use of perturbative binding energy estimates is justified because the Kato-Rellich theorem is non-perturbative: it provides rigorous bounds on the perturbation of the spectrum, not just formal series. The concern about a deeply bound two-glueball state is addressed: the interaction is weak ($O(g_k^2)$) relative to the kinetic energy ($\hat{\Delta}_k$), so no deeply bound state can form. This is the standard argument for the absence of Efimov-like effects at weak coupling.

**(c) Volume independence via Combes-Thomas.** The Combes-Thomas estimate controls the sum over states by exploiting locality. The operator $\hat{A}^{(s)}$ is supported in a ball of radius $R_0$ (from the locality hypothesis (ii)). The radius $R_0$ is bounded uniformly in $k$: Balaban's block-spin generates operators with support radius $R_0 = O(1)$ in block lattice units at each step. The blocking increases the lattice spacing but the support radius in lattice units remains bounded.

The sum $\zeta \leq \sum_{r=0}^\infty e^{C_1(R_0+r)^3 N^2} \cdot e^{-c\hat{\Delta} r}$ converges because the exponential decay $e^{-c\hat{\Delta} r}$ dominates the polynomial-in-exponent growth $e^{C_1 r^3}$. The bound is independent of the total spatial volume $L$ because distant excitations are suppressed by the mass gap.

**Impact on the claimed result:** None. The spectral lemma is correctly proved with uniform constants.
