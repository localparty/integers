## Part D, Point 3: The Spectral Lemma

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim is that for $\mathrm{dev}(\mathcal{O}) \geq p$: $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$, with $C_p$ independent of $k$, $g_k$, and the volume.

**(a) The deviation extraction (Step 1).** The proof correctly identifies three types of intermediate states: diagonal ($n_j = m$, contributing factor 0), near-diagonal ($n_j = 0$ vacuum, contributing $|e^{\hat{\Delta}} - 1| \leq C_* \hat{\Delta}$), and far-diagonal ($n_j \geq 2$, contributing $O(1)$). The claim is that the $p$ extracted deviation factors come from near-diagonal slots. The bound $(e^{\hat{\Delta}} - 1) \leq \hat{\Delta} \cdot e^{\hat{\Delta}}$ is correct, and the constant $C_* = e^{\hat{\Delta}_{\max}}$ is $k$-independent because $\hat{\Delta}_k$ is bounded above by the UV cutoff scale.

The proof correctly claims that at least $p$ of the factors are near-diagonal (giving $O(\hat{\Delta})$ each), while far-diagonal factors are absorbed into the residual weight $\tilde{W}$. This is precisely the content of Definition D.2: the factorization produces $p$ near-diagonal factors with bounded residual. The bound $(C_* \hat{\Delta})^p$ then follows.

**(b) The $\zeta$ bound and the two-particle threshold.** The sum $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ requires $E_2 - E_1 > 0$. The paper bounds the binding energy $\epsilon_B \leq C_B g_k^4 \hat{\Delta}_k$ via Kato–Rellich perturbation theory in the two-particle sector. The interaction $V_k$ has $\|V_k\|_{\mathrm{op}} \leq C g_k^2$ per unit volume, and the relative bound $\|V_k\|/(2\hat{\Delta}_k) \leq C g_k^2/(2\hat{\Delta}_k) \ll 1$ for $g_k$ small ensures no deeply bound two-glueball state can form.

Non-perturbative contributions to $\epsilon_B$ are controlled by the large-field bound: $\|\delta H_k^{\mathrm{lf}}\| \leq C' e^{-6/g_k^{0.98}}$ (for SU(3)), which is strictly sub-leading relative to $g_k^4$ for all $g_k \leq 0.5$ (verified numerically: ratio $\leq 10^{-4}$ at $g_k = 0.5$, $\sim 10^{-22}$ at $g_k = 0.1$). This eliminates a potential circularity where one would need $\hat{\Delta}_k \geq \hat{\Delta}_\infty > 0$ to control the binding energy.

The condition $g_k^4 \leq 1/(4C_B)$ is satisfied for all $k \geq k_0$ on the AF trajectory (where $g_k \to 0$). The finitely many steps $k < k_0$ contribute a bounded constant. The resulting bound $E_2 - E_1 \geq \hat{\Delta}_k/2$ gives $\zeta \leq C(R_0, N)$, $k$-independent.

**(c) Volume independence via Hastings–Koma.** The paper uses the Hastings–Koma exponential clustering theorem (CMP 265, 2006) instead of Combes–Thomas estimates. This is a significant improvement: Hastings–Koma provides clustering bounds that are:
- Volume-independent (local: excitations at distance $r$ suppressed by $e^{-r/\xi}$)
- $K$-uniform (the Lieb–Robinson velocity $v_{\mathrm{LR}}^{\mathrm{phys}} \leq C'' g_k^2$ is bounded uniformly on the AF trajectory)

The operator $\mathcal{O}$ has physical support of diameter $r_0 = R_0 \cdot a_k$. The connected matrix element is rewritten as a vacuum four-point correlator via LSZ reduction. The Hastings–Koma constant $C_{\mathrm{HK}}$ depends only on $d$, $N$, $v_{\mathrm{LR}}^{\mathrm{phys}}$, and $\Delta_{\mathrm{phys}}$ — all $K$-uniform. The large-field tail contributes $O(e^{-c/g_k^{2\epsilon}})$, negligible.

The Hastings–Koma approach requires a finite-dimensional lattice system with finite-range bounded interactions and spectral gap. Balaban's effective Hamiltonian in the small-field domain satisfies these conditions: effective local dimension $D_{\mathrm{eff}} \leq \exp(C_D N^2/g_k^{3/2})$ per link, nearest-neighbor interactions of strength $\|h_{\mathrm{link}}\| \leq C g_k^2/a_k$, physical range $a_k$, and spectral gap $\Delta_{\mathrm{phys}} > 0$ (inductive hypothesis). This is a legitimate application of Hastings–Koma.

Verified computationally: the spectral lemma exponent $g_k^4 \leq 1/(4C_B)$ is equivalent to $g_k^2 \leq 1/(2\sqrt{C_B})$, consistent with the paper's statement.

**Impact on the claimed result:**
No impact. The spectral lemma is correct, with $k$-independent and volume-independent constants established via Hastings–Koma clustering.
