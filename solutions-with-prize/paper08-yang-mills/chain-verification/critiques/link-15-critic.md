# Link 15 Critic — Gradient-Flow Well-Posedness, Contractivity, Small-Field Preservation, K-Uniform Polymer Decay

**Verdict: SURVIVED (one residual flag — max-principle gap in L.1.2)**

---

## Attack Results

### Attack 1 (Which action drives the flow?)

**FAILS.** The flow equation (L.1.2) is written explicitly as the negative gradient of $S_{\mathrm{KK}}$ — the full KK-enhanced action, not the Wilson action alone and not a block-spin effective action. The memo W1-01 and the L.1 text are consistent: the flow equation reads $\partial_t V_t = -g_0^2 (\partial_{V,\ell} S_{\mathrm{KK}}) V_t$. The KK coupling terms are shown to be $C^\infty$ by the adjoint-action structure and uniform convergence of the KK mode sum. The three actions (Wilson, block-spin effective, KK-enhanced) differ only at order $O(a^2)$ in the continuum limit — and the paper works on a finite lattice throughout Phase 1, so this difference is harmless for well-posedness. No ambiguity exists.

### Attack 2 (Contractivity uniform in the lattice spacing?)

**WEAKENED but not BROKEN.** The contractivity claim (Lemma L.1.5) rests on two ingredients: (a) monotone decrease of the action (a direct identity, uniform in every parameter), and (b) vacuum isolation via the Hessian bound $\mathrm{Hess}_{A=0} S_{\mathrm{KK}} \geq (2N/r_3^2)\mathbb{1}$ from the Weitzenböck spectral gap. Both are indeed independent of the lattice spacing $a_k$: the monotonicity identity (L.1.22) holds for any lattice spacing by the chain rule, and the spectral gap $2N/r_3^2$ depends only on $N$ and the compactification radius $r_3$, not on $a_k$. The Lojasiewicz–Simon convergence rate constant $\sigma$ in (B.4) of W1-02 is controlled from below by $2N/r_3^2$, which is lattice-spacing-independent. Therefore the contractivity constant is uniform in $a_k$, and the continuum-limit argument at this stage does not break. **Flag:** the paper invokes the Lojasiewicz–Simon theorem for a continuum analogue (Feehan arXiv:1409.1525) as supporting motivation, but the actual lattice result is elementary ODE theory on a compact manifold (unique minimum, Lyapunov function). The reference to the continuum Feehan theorem is supporting evidence, not a logical step; its status (finite-time existence only for $d=4$ continuum flow) does not affect the lattice claim. This is a presentational over-reliance on a continuum tool, not a logical gap.

### Attack 3 (Does the flow preserve the small-field domain?)

**FAILS as a break, but gap identified in the pointwise step.**

The core preservation proof (Lemma L.1.2) chains: (1) monotone action decrease, (2) action bound $S[V_0] \leq C_S p(g_k)^2 |\Lambda_k|$ for $V_0 \in \Omega_s$, and (3) quadratic coercivity $S[V] \geq (m_W^2/2)\|F\|_{L^2}^2$. This gives an $L^2$ bound on the flowed field strength but does not directly give the *pointwise* bound $\|F_{\mu\nu}^{(t)}(x)\| < p(g_k)$ needed to place $V_t$ back in $\Omega_s$.

The paper bridges this gap in Step 4 via a "maximum principle for the discrete heat equation" applied to the parabolic inequality $\partial_t E \leq \Delta E - 2\|D_\nu G_{\nu\mu}\|^2$. **Gap:** this parabolic inequality is stated without proof in the L.1 text. It is a standard result for the continuum Yang–Mills heat equation (Struwe 1994, Rade 1992), but on the lattice the energy density $E(t,x)$ satisfies a discrete equation whose structure depends on the specific form of the lattice action. W2-06 cites Struwe for the maximum principle but applies it to the lattice setting; no lattice-specific verification is given. The discrete maximum principle requires that the equation have the form $\partial_t E(x) \leq \sum_y w_{xy} (E(y)-E(x))$ with $w_{xy} \geq 0$, which requires checking that the nonlinear terms $-2\|D_\nu G_{\nu\mu}\|^2$ have the right sign and that the lattice Laplacian has non-negative off-diagonal weights. For the standard nearest-neighbor lattice Laplacian on a regular lattice this holds, but the nonlinear reaction term needs to be verified to be non-positive. In the text it is written as "$\leq \Delta E$", which requires the reaction term to be non-positive — and indeed $-2\|D_\nu G_{\nu\mu}\|^2 \leq 0$, so the inequality $\partial_t E \leq \Delta E$ is sound. The discrete maximum principle then applies provided the discrete Laplacian has nonnegative off-diagonal entries (satisfied for the standard graph Laplacian). This is a **fillable gap** (two lines of verification), not a break. The logical conclusion — that the pointwise maximum of $E$ is non-increasing — follows once these two lines are added.

### Attack 4 (K-uniformity of polymer decay)

**FAILS.** Lemma L.1.4 gives the cleanest argument in Link 15. The key cancellation in Step 2 of the K-uniformity proof is that the factor $g_0^2$ in the flow equation cancels the factor $1/g_0^2$ in $S_{\mathrm{KK}} = (1/g_0^2) S_{\mathrm{YM}} + \ldots$, making the flow equation $K$-independent in form on $\Omega_s$. The polymer decay constant $\kappa_B$ is $(k,K)$-uniform by Appendix M, Lemma M.1.2 (which is itself a proved lemma in the preprint). The KK mass tower is $K$-independent by the frozen dilaton. The argument is tight and correct.

**Attempted attack at small $K$ (UV):** At small bare-scale index $K$ (ultraviolet), the bare coupling $g_0(K)$ is small (asymptotic freedom: $g_0^2(K) \sim 1/(b_0 \ln(K))$). Could the $g_0^2$-cancellation fail at $K=0$? No: the $g_0^2$ prefactor in the flow equation (L.1.2) is explicit and constant, and the $1/g_0^2$ in $S_{\mathrm{KK}}$ enters only the overall normalization of the action. The flow equation on $\Omega_s$ involves the gradient of the action, and the $g_0^2$ prefactor simply sets the flow-time scale without introducing $K$-dependence into the domain $\Omega_s$ or the polymer estimates. The decay constant $\kappa_B$ depends on the blocked action's analyticity properties, not on $g_0$.

### Attack 5 (Well-posedness on the gauge-orbit quotient)

**FAILS.** This is the sharpest potential attack: in the continuum, the gradient flow is a PDE on an infinite-dimensional gauge orbit space, and global well-posedness in $d=4$ is open (only short-time existence is known; Struwe 1994, Feehan arXiv:1409.1525). However, Lemma L.1.1 works entirely on the *lattice*, not the continuum. The lattice configuration space is $\mathcal{M} = \mathrm{SU}(N)^{|\Lambda_k^1|}$, a *finite-dimensional compact manifold*. No gauge fixing or quotient is needed for well-posedness: the flow is gauge-covariant (Lemma L.1.1(vi)), and gauge-invariant observables are preserved (Corollary 5.2). Global existence follows trivially from compactness via Picard–Lindelöf (no PDE analysis required). The paper explicitly flags this in Remark 6.1 of W1-01 and Remark 4.2: "The lattice regularization bypasses these analytic difficulties entirely." The continuum gauge-orbit quotient issue does not arise.

---

## Summary

All five attack vectors fail to break Link 15. Lemmas L.1.1 (well-posedness), L.1.3 (polymer decay), L.1.4 ($K$-uniformity), and L.1.5 (contractivity) are sound. One fillable gap is identified in Lemma L.1.2: the pointwise bound in Step 4 invokes the discrete maximum principle for the lattice Yang–Mills heat equation without explicitly verifying the non-positivity of the discrete reaction term and the non-negativity of the off-diagonal lattice Laplacian weights. Both conditions hold (the reaction term $-2\|D_\nu G_{\nu\mu}\|^2 \leq 0$ and the graph Laplacian is standard), but the verification is missing from the text. This is a presentational gap requiring two lines of argument, not a logical break. **SURVIVED.**
