## Part D, Point 2: Stability of Boltzmann Deviation Order

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

This is the single most important technical innovation in the paper. I examined it with maximum skepticism.

**(a) The definition of Boltzmann deviation order.**

Definition D.2 defines $\mathrm{dev}(\mathcal{O}) \geq p$ in terms of the factorization of the spectral weight: for the multi-time-slice representation $\langle m|\mathcal{O}|m\rangle = \sum_\alpha \sum_\mathbf{n} W_\alpha^{(m)}(\mathbf{n}) e^{-E(\mathbf{n})}$, one requires that $W_\alpha^{(m)}(\mathbf{n}) e^{-E(\mathbf{n})}$ can be written as $\tilde{W}_\alpha^{(m)}(\mathbf{n}) \cdot \prod_{j=1}^{q_\alpha(\mathbf{n})} (e^{E_m - E_{n_{\sigma(j)}}} - 1)$ with $q_\alpha(\mathbf{n}) \geq p$ and bounded $\tilde{W}$.

This definition IS equivalent to the intuitive notion "the spectral weight vanishes to order $\geq p$ at the diagonal $E_{n_j} = E_m$ for all $j$." The factors $(e^{E_m - E_{n_j}} - 1)$ vanish when $n_j = m$ (diagonal). Having $\geq p$ such factors means the weight vanishes to order $\geq p$ at the diagonal. The deviation order bound $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$ follows from bounding each factor by $C\hat{\Delta}$ (since $|e^{E_m - E_{n_j}} - 1| \leq C(E_m - E_0) = C\hat{\Delta}$ when the factor is $O(\hat{\Delta})$, and by $O(1)$ otherwise, with at least $p$ factors being $O(\hat{\Delta})$).

An operator could satisfy Definition D.2 but give a bound weaker than $(C\hat{\Delta})^p$ only if the $\tilde{W}$ factors grow — but the definition requires bounded $\tilde{W}$, so the bound is exactly $C_p M \hat{\Delta}^p$. The definition is neither weaker nor stronger than the intuitive notion; it is a precise formalization of it.

**(b) The linear combination lemma.**

The lemma states that if each $\mathcal{O}_i$ has $\mathrm{dev} \geq p$ and $\sum |c_i| \|\mathcal{O}_i\| < \infty$, then $\sum c_i \mathcal{O}_i$ has $\mathrm{dev} \geq p$.

The concern about different temporal supports is addressed as follows: if operators $\mathcal{O}_i$ have temporal extent $R_i$, the sum is embedded in a common representation with $R = \max_i R_i$. Shorter operators are zero-padded by inserting identity time slices: $\hat{A}_\alpha^{(s)} = \delta_{n_s, n_{s-1}} \hat{1}$ for the extra slots. The identity insertion $\langle n | \hat{1} | n'\rangle = \delta_{n,n'}$ introduces no new spectral weight — it simply extends the tuple without changing the deviation structure. The Boltzmann factor $e^{-E_{n_j}}$ at an identity slot contributes $(e^{E_m - E_{n_j}} - 1)$ with $n_j$ inherited from the neighboring slot. Zero-padding preserves $\mathrm{dev} \geq p$ because the extra factors are either $O(\hat{\Delta})$ (adding to the deviation count) or $O(1)$ (bounded).

The proof handles cancellations correctly: the deviation order is a property of each term's spectral weight individually, not of the sum. The sum $\sum c_i W_\alpha^{(i,m)}$ could have cancellations, but $\mathrm{dev} \geq p$ requires only that each term has the factored form, not that the factored parts add constructively. The bound uses $|\sum c_i W^{(i)}| \leq \sum |c_i| |W^{(i)}|$, and each $|W^{(i)}|$ has the deviation structure. This is correct.

**(c) The role of (B1) analyticity.**

The convergent Taylor expansion from (B1) means $\delta E_k^{d=6}$ is a genuine (not formal) linear combination of monomials in the block variables, each of which is a gauge-invariant local operator. The analyticity radius $\rho$ determines the domain of convergence.

The concern is whether typical configurations contributing to $\langle 1|\delta E_k^{d=6}|1\rangle_c$ lie within the analyticity domain. In the gapped phase, the one-particle state $|1\rangle$ is dominated by configurations near the vacuum (small field). In Balaban's small-field region $\Omega_s$, the field strength satisfies $|F_{\mu\nu}| < g_k^{1-\epsilon}$, which is well within the analyticity radius for $g_k$ small. The typical configurations of $|1\rangle$ are concentrated in $\Omega_s$ because: (i) the Boltzmann weight $e^{-S}$ suppresses large fields exponentially; (ii) the mass gap ensures the one-particle state has finite energy, restricting field amplitudes.

The matrix element $\langle 1|\delta E_k^{d=6}|1\rangle_c$ receives contributions only from configurations in $\Omega_s$ (where the Taylor expansion converges) plus large-field contributions from $\Omega_l$ (exponentially suppressed). The (B1) analyticity ensures the expansion converges on all configurations that contribute non-negligibly.

**(d) The transition from perturbative to non-perturbative.**

This is the crux of the argument. The key insight: the $\mathrm{dev} \geq 2$ property is NOT established by perturbative identification (matching to one-loop operators) but by exhaustive classification of the operator space. The argument is:

1. By (B1), $\delta E_k^{d=6}$ is a convergent sum of gauge-invariant local operators of dimension 6.
2. By the dimension-6 classification (Section 5.3.1, Appendix J), every $\mathcal{C}$-even, gauge-invariant dimension-6 operator falls into one of four classes.
3. Classes (I)-(II) (zero-derivative and one-derivative operators) are absent: $\mathcal{C}$-odd operators have coefficient exactly zero.
4. Classes (III)-(IV) (two-or-more-derivative operators) all have $\mathrm{dev} \geq 2$ by the spectral mechanism.
5. By the linear combination lemma, $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$.

The projection separating dimension-4 from dimension-6 IS well-defined non-perturbatively because $S_{\mathrm{YM}}$ is the unique dimension-4 operator (PROOF-CHAIN.md, IV.3). The coupling renormalization $g_{k+1}$ is defined as the coefficient of $S_{\mathrm{YM}}$ in the effective action. The remainder after subtracting $(1/g_k^2) S_{\mathrm{YM}}$ is the sum of dimension-$\geq 6$ operators. The analyticity from (B1) ensures this is a convergent (not formal) decomposition.

The dimension-8, dimension-10, etc. contributions have $\mathrm{dev} \geq 4, 6, \ldots$ (more derivatives mean more deviation factors). They are handled by the same classification argument at higher dimensions.

**(e) Structural zero vs. kinematic zero.**

The diagonal vanishing $(e^{E_1 - E_1} - 1)^2 = 0$ for $\mathrm{Tr}(D_0 F)^2$ is structural: it arises from the squared-derivative structure of the operator, not from a numerical coincidence. The factor $(e^{E_m - E_n} - 1)$ vanishes identically when $n = m$ regardless of the specific values of $E_m$. This is a property of the operator class (two covariant derivatives), not of a specific matrix element.

For the non-perturbative $\delta E_k^{d=6}$, the spectral weights are inferred from the classification: since $\delta E_k^{d=6}$ is a convergent linear combination of operators each having $\mathrm{dev} \geq 2$, and deviation order is preserved under convergent linear combinations (the linear combination lemma), the sum has $\mathrm{dev} \geq 2$.

Can cancellations change the deviation structure? The linear combination lemma addresses this: $\mathrm{dev} \geq 2$ for the sum follows from $\mathrm{dev} \geq 2$ for each term, regardless of cancellations in the spectral weights. The proof uses triangle inequality: $|W_{\mathrm{total}}| \leq \sum |c_i| |W_i|$, and each $|W_i|$ has the factored form with $\geq 2$ deviation factors. The absolute value prevents cancellations from reducing the deviation order. Cancellations can make the bound tighter (smaller $M$), but cannot reduce $p$.

**Impact on the claimed result:** None. The stability of deviation order argument is the genuine innovation of this paper, and it is correct. The classification-based approach avoids the pitfalls of perturbative identification. The linear combination lemma, combined with the exhaustive dimension-6 classification and the (B1) analyticity, establishes $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ non-perturbatively.
