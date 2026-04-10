## Part D, Point 3: The Spectral Lemma

**Weight:** MEDIUM
**Verdict:** SOUND (with one technical concern about the locality radius)

**Finding:**

(a) **Deviation extraction (Step 1).** Each extracted factor $(e^{E_m - E_{n_j}} - 1)$ is bounded as follows:
- **Diagonal ($n_j = m$):** factor is exactly 0; the slot contributes nothing and is not counted.
- **Near-diagonal ($n_j = 0$, vacuum):** factor is $(e^{\hat\Delta} - 1) \leq C_* \hat\Delta$ where $C_* = e^{\hat\Delta_{\max}}$, the Boltzmann factor at the maximum gap (which is bounded above by $1$ in lattice units, i.e. $C_*$ is a finite $k$-independent constant).
- **Far-diagonal ($n_j \geq 2$):** $|e^{E_m - E_{n_j}} - 1| \leq 1$, contributing $O(1)$ but absorbed into the residual.

The proof's claim is that $p$ near-diagonal factors give $(C_* \hat\Delta)^p$, while the far-diagonal slots are $O(1)$ and absorbed into the bounded residual. This is correct *provided* that hypothesis (iii) ($\mathrm{dev} \geq p$) requires the $p$ extracted factors to be near-diagonal (i.e., the spectral weight vanishes specifically when one of the intermediate states is the vacuum, not just any state).

**This is the right reading of Definition D.2.** The vanishing-to-order-$p$ at the diagonal is what produces the $\hat\Delta^p$ factor; far-diagonal channels are not "extracted deviation factors" in the sense of D.2. Sound.

(b) **The $\zeta$ bound and the two-particle threshold.** The sum
$$\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$$
is bounded by a Combes–Thomas-type estimate:
$$\zeta \leq \sum_{r=0}^\infty e^{C_1(R_0+r)^3 N^2} \cdot e^{-c\hat\Delta r}$$
The exponential suppression dominates the polynomial density of states, so $\zeta < \infty$.

**Concern:** the estimate requires $E_2 - E_1 > 0$ (a spectral gap *above* the one-particle state). This is the binding-energy issue. The proof handles it via the perturbative bound $\epsilon_B \leq C_B g_k^4 \hat\Delta_k$ from Born/Lippmann–Schwinger, plus a Kato–Rellich argument for non-perturbative corrections. The non-perturbative correction is bounded by the large-field error $\|\delta H_k^{\mathrm{lf}}\|_{\mathrm{op}} \leq C' e^{-c/g_k^{1/2}}$ via Weyl's eigenvalue inequality.

This is rigorous but relies on the non-perturbative correction being smaller than the perturbative gap. Concretely, we need $C' e^{-c/g_k^{1/2}} \ll C_B g_k^4 \hat\Delta_k$, which holds if $g_k$ is small enough that the exponential beats the polynomial. This is not automatic at moderate $g_k$ — see the C2 large-field discussion.

The proof's resolution: at moderate $g_k$ ($k < k_0$), the binding-energy issue is handled non-perturbatively by the cluster expansion (which gives $\Delta_0^{\mathrm{KK}} > 0$ directly from Theorem 4 without needing the Kato bound). For $k \geq k_0$, $g_k$ is small and the perturbative bound applies. The transition is again the K-vs-k issue: the "$k_0$" mentioned here is in the Balaban inner-step convention, but the convergence sum uses the bare-refinement convention. Acknowledging this ambiguity, the binding-energy step is plausible but technically conditional on Point C1.

(c) **Volume independence via Combes–Thomas.** The Combes–Thomas estimate requires the operator to be supported in a ball of radius $R_0$, with $R_0$ uniformly bounded. The proof claims $R_0 = O(1)$ (block lattice units) uniformly in $k$, citing Balaban's polymer expansion: "operators supported within connected polymers of diameter bounded by $R_0$ block lattice units (CMP 109, Theorem 1)."

**This is a real technical concern.** Balaban's polymer expansion gives polymer activities with exponential decay $|K_k(X, V)| \leq e^{-\kappa|X|}$, but the polymer *size* $|X|$ is *not* uniformly bounded — it ranges over all connected polymers, with the exponential decay providing the convergence. The "support radius" $R_0$ of the *individual* polymer activities can be arbitrarily large (at the cost of exponential suppression).

When the spectral lemma is applied to $\mathcal{O} = \delta E_k^{d=6}$, the operator is a sum over polymer activities, and each activity has a different support radius. The linear-combination lemma handles the convergent sum, but the *Combes–Thomas locality bound* used to control $\zeta$ requires the operator to be a *single* local operator with bounded support, not a convergent sum of operators with growing support. The preprint glosses over this distinction.

The fix is to apply the Combes–Thomas bound to *each* polymer activity individually, with the activity's specific support radius, and then sum. The exponential decay $e^{-\kappa|X|}$ provides the necessary suppression to make the sum finite. This is plausible but is *not* what the preprint actually does — the preprint applies Combes–Thomas to a single operator with "$R_0 = O(1)$", which is technically incorrect for the full Balaban remainder.

**To close:** Re-do the spectral-lemma estimate as a sum over polymer activities, applying Combes–Thomas to each activity with its own support radius, and summing with the polymer-expansion convergence. **Difficulty: 2–3 pages.**

**Impact on the claimed result:** This is a real technical gap in the spectral-lemma proof. It is closable (the polymer expansion provides the necessary structure), but the current presentation conflates "single local operator" with "polymer expansion." A clean version would need to separate these.
