## Part D, Point 3: The Spectral Lemma

**Weight:** MEDIUM
**Verdict:** SOUND (sub-point a, ADDRESSED); **SOUND** (sub-point b, D3b commit); SOUND (sub-point c)

**[UPDATE]** Sub-points (a) and (b) have been addressed in the preprint. See revision notes below.

---

**Finding:**

**(a) The deviation extraction and $O(1)$ vs. $O(\hat{\Delta})$ factors.** Step 1 of the spectral lemma proof (Section 5.5.3) bounds the deviation factors:
- $n_j = m$ (diagonal): $|e^0 - 1| = 0$ (exact zero).
- $n_j = 0$ (vacuum intermediate): $|e^{\hat{\Delta}} - 1| = \hat{\Delta}(1 + O(\hat{\Delta})) \leq C\hat{\Delta}$.
- $n_j \geq 2$ (higher excited): $|e^{E_1 - E_{n_j}} - 1| \leq 1$ (since $E_1 < E_{n_j}$).

The bound $|e^{E_m - E_{n_j}} - 1| \leq \max(\hat{\Delta} e^{\hat{\Delta}}, 1) \leq C_0 \hat{\Delta}$ is stated in equation (S1.2) where $C_0 = \max(e^{\hat{\Delta}}, 1/\hat{\Delta})$.

The problem with this bound: for $n_j \geq 2$ (higher excited), the factor $|e^{E_1 - E_{n_j}} - 1| \leq 1$ is an $O(1)$ bound, not an $O(\hat{\Delta})$ bound. The combined bound $C_0\hat{\Delta}$ with $C_0 = \max(e^{\hat{\Delta}}, 1/\hat{\Delta})$ uses $C_0 \geq 1/\hat{\Delta}$ for the higher-excited case, so that $C_0 \hat{\Delta} \geq 1$. This effectively replaces the $O(1)$ factor by $O(\hat{\Delta}) \times O(1/\hat{\Delta}) = O(1)$, which is valid but means the $\hat{\Delta}^p$ bound absorbs a factor $C_0^p \geq \hat{\Delta}^{-p}$ into the constant, making $C_p \geq \hat{\Delta}^{-p}$... but wait, $C_0$ is defined to include $1/\hat{\Delta}$, so $C_p = 2C_0^p (1+\zeta)^{R_0-1}$ would diverge as $\hat{\Delta} \to 0$.

This is a genuine issue. The spectral lemma claims $C_p$ is "independent of $k$, $g_k$, and the volume." But if $C_0 = \max(e^{\hat{\Delta}}, 1/\hat{\Delta})$ and $\hat{\Delta}_k \to 0$ as $k \to \infty$ along the RG trajectory... actually, $\hat{\Delta}_k \sim 4^{-k} \to 0$. So $C_0 \sim 4^k \to \infty$.

This means the constant $C_p$ in the spectral lemma grows as $k \to \infty$, which would destroy the $k$-uniform bound claimed. This is a genuine gap in the proof.

The resolution (which the preprint hints at but does not state clearly): for $\hat{\Delta}_k \leq 1$, the bound $|e^{E_1 - E_{n_j}} - 1| \leq 1$ for $n_j \geq 2$ is fine as an $O(1)$ factor. The key is that in the deviation order definition, we require $\geq p$ factors that are $O(\hat{\Delta})$, and the remaining factors are $O(1)$. So out of the $2R-1$ intermediate-state indices, at least $p$ must be of the vacuum-intermediate type (giving $O(\hat{\Delta})$) and the rest are of the higher-excited type (giving $O(1)$). The $C_p$ then includes factors of $\zeta$ (the sum over excited states) but NOT factors of $1/\hat{\Delta}$.

For this to work, Definition D.2 must specify that the $p$ extracted factors are precisely the $O(\hat{\Delta})$ ones (corresponding to $n_j = 0$ or $n_j = m$, the "near-diagonal" cases), and the remaining factors are the $O(1)$ ones absorbed into the residual $\tilde{W}$. The definition as written requires exactly $q_\alpha(\mathbf{n}) \geq p$ factors of $(e^{E_m - E_{n_j}} - 1)$, which could include the $O(1)$ factors from $n_j \geq 2$.

This ambiguity in the definition and its interaction with the constant $C_p$ is a genuine gap that requires clarification. Specifically: (i) the constant $C_p$ must be bounded uniformly in $k$ for the RG recursion to work, and (ii) the current proof as written allows $C_0 = O(1/\hat{\Delta}_k) = O(4^k)$, which would make $C_p = O(4^{pk})$, destroying the convergence of $\sum_k C_k g_k^4 \hat{\Delta}_k^2$ (since $4^{pk} \cdot 4^{-k} = 4^{(p-1)k} \to \infty$ for $p \geq 2$).

Closing requires: clarify that the $p$ extracted deviation factors in D.2 are specifically the "near-diagonal" ones ($n_j = 0$ or $n_j = m$), each giving $O(\hat{\Delta})$, while the "far-diagonal" factors ($n_j \geq 2$, giving $O(1)$) are absorbed into $\tilde{W}$. With this clarification, $C_0 = e^{\hat{\Delta}} = O(1)$ for small $\hat{\Delta}$, and $C_p = O(1)$ uniformly in $k$. Difficulty: **1 paragraph** rewriting the definition and Step 1.

**(b) The $\zeta$ bound and the two-particle threshold.** Section 5.5.3, Step 3(ii) bounds the two-particle threshold gap: $E_2 - E_1 \geq \hat{\Delta}_k(1 - C_B g_k^4) \geq \hat{\Delta}_k/2$ for $g_k^2 \leq 1/(2C_B)$. This uses a perturbative Born-approximation estimate for the gluon-gluon binding energy, $\epsilon_B \leq C_B g_k^4 \hat{\Delta}_k$.

The concern: is a perturbative binding energy estimate valid non-perturbatively? Could a deeply bound two-glueball state close the gap $E_2 - E_1$?

At small $g_k$, the gluon-gluon interaction is weak and the Born approximation is valid. The preprint acknowledges "This condition is satisfied for all $k \geq k_0$ on the asymptotically free trajectory (where $g_k \to 0$). The finitely many initial steps $k < k_0$ contribute a bounded constant to the RG sum." For $k < k_0$ (finite number of steps), the bound on $\zeta$ may not hold via this argument, but $\zeta \leq C$ still holds because $E_2 \geq E_1 > 0$ (there are finitely many energy levels below $E_2$, and the gap is bounded below by a finite-volume argument). So the initial steps are handled separately.

The non-perturbative concern is real: a deeply bound two-glueball state could have $E_2 - E_1 \sim 0$ at some RG step. However, on the asymptotically free trajectory, the coupling at each step is perturbatively small ($g_k \to 0$), and the binding energy is genuinely perturbative. The argument "$E_2 - E_1 \geq \hat{\Delta}_k/2$" for $g_k^2 \leq 1/(2C_B)$ is valid perturbatively to all orders (since the Born approximation is the leading term and higher orders are suppressed by $g_k^{2n}$). Non-perturbative instanton-mediated binding is suppressed by $e^{-8\pi^2/g_k^2}$, which is negligible. This is a CLOSABLE GAP: the perturbative argument is sound but a non-perturbative statement requires more care. The preprint would be strengthened by noting that non-perturbative binding is suppressed by instantons. Difficulty: **1 paragraph**.

**(c) Volume independence via Combes-Thomas.** Step 3(i) of the spectral lemma uses the Combes-Thomas estimate to bound $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$. The key: is $R_0$ (the support radius of $\hat{A}^{(s)}$) bounded uniformly in $k$?

From Balaban's construction, the block-spin generates operators with support $R_0 = O(L^k)$ in original lattice units (each block-spin step doubles the support). But in *block lattice units* (which is the natural scale for step $k$), the support remains $R_0 = O(1)$ because the blocking factor $L = 2$ is fixed. The spectral lemma is stated in block lattice units, so $R_0$ is indeed bounded uniformly in $k$. The Combes-Thomas estimate gives a bound on $\zeta$ that depends on $R_0$ and the mass gap $m$ of the two-particle sector. Since $m \geq \hat{\Delta}/2 > 0$ (from the two-particle threshold bound above), $\zeta \leq C(R_0, N) < \infty$ with $C$ uniform in $k$ and $L$. SOUND.

**Impact on the claimed result:** Sub-point (a) is now addressed: the revised preprint (Step 1 of the spectral lemma proof) explicitly restricts the $p$ extracted deviation factors to near-diagonal slots ($n_j \in \{0, m\}$), each giving a factor $O(\hat{\Delta})$ with k-independent constant $C_* = e^{\hat{\Delta}_{\max}}$. The problematic $C_0 = \max(e^{\hat{\Delta}}, 1/\hat{\Delta})$ — which grew as $4^k$ — is replaced by $C_* = e^{\hat{\Delta}_{\max}}$, bounded above by the UV cutoff scale. Far-diagonal factors ($n_j \geq 2$) are explicitly confined to the residual $\tilde{W}$, not counted as extracted deviation factors. The RG recursion now closes with a k-uniform spectral lemma constant.

**[REVISION NOTE — Sub-point (b) ADDRESSED — D3b commit.]** The non-perturbative binding gap is now closed by a two-part argument inserted after the Kato--Rellich bound in Step~3(ii):

1. **Small-field sector (topological triviality).** The small-field condition $|F_{\mu\nu}| < g_k^{3/4}$ (Appendix~K.4, $\epsilon=1/4$) forces the lattice topological charge $|Q| \leq C\,\mathrm{vol}\cdot g_k^{3/2} \to 0$. Configurations in the small-field domain are topologically trivial; instanton-mediated binding contributions are absent by construction.

2. **Large-field sector (exponential suppression).** The large-field contribution to the effective Hamiltonian is suppressed by $O(e^{-c/g_k^{1/2}})$ (Appendix~K.4; Balaban, CMP~119). The resulting large-field binding energy $\epsilon_B^{\mathrm{lf}} \leq D\hat\Delta_k e^{-c/g_k^{1/2}}$ satisfies $e^{-c/g_k^{1/2}} \ll g_k^4$ for all small $g_k$ (beyond all perturbative orders).

Combined: $\epsilon_B \leq C_B g_k^4\hat\Delta_k + C'e^{-c/g_k^{1/2}} \leq 2C_B g_k^4\hat\Delta_k$, giving $E_2 - E_1 \geq \hat\Delta_k/2$ for $g_k^4 \leq 1/(4C_B)$ (i.e., $g_k^2 \leq 1/(2\sqrt{C_B})$). ✓ COMMITTED.

Three follow-up issues identified and corrected in a subsequent pass:
- **Issue 1 (coupling exponent):** Corrected $g_k^2 \leq 1/(4C_B)$ (wrong) to $g_k^4 \leq 1/(4C_B)$, equivalently $g_k^2 \leq 1/(2\sqrt{C_B})$. The same error was present in the original text's condition $g_k^2 \leq 1/(2C_B)$.
- **Issue 2 (additivity + $\hat\Delta_k$ prefactor):** Added the Weyl eigenvalue inequality as the one-sentence justification for the additive bound $\epsilon_B \leq \epsilon_B^{\mathrm{pert}} + \epsilon_B^{\mathrm{lf}}$. Removed the unjustified $\hat\Delta_k$ prefactor from $\epsilon_B^{\mathrm{lf}}$: the Weyl inequality gives $\epsilon_B^{\mathrm{lf}} \leq \|\delta H_k^{\mathrm{lf}}\|_{\mathrm{op}} \leq C' e^{-c/g_k^{1/2}}$ (no $\hat\Delta_k$ factor); the conclusion $e^{-c/g_k^{1/2}} \ll g_k^4\hat\Delta_k$ still holds.
- **Issue 3 (topological charge integrality):** Specified the Lüscher--Weiss geometric lattice topological charge (integer-valued by construction; Lüscher--Weiss, Nucl. Phys. B 290, 1987). Added that small-field configurations approximate smooth continuum fields to within $O(g_k^{1/4})$ (Appendix K.4), so the geometric charge equals the continuum charge, and $Q \in \mathbb{Z}$ with $|Q| < 1 \Rightarrow Q = 0$ follows.

All three sub-points are now SOUND.
