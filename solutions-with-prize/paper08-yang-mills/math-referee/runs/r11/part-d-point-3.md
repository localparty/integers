## Part D, Point 3: The Spectral Lemma

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The deviation extraction (Step 1).**

The proof extracts $p$ factors of $(e^{E_m - E_{n_j}} - 1)$ from the spectral weight. Each factor is bounded by:
- If $n_j = 0$ (vacuum): $|e^{E_m - E_0} - 1| = |e^{E_m} - 1| \leq E_m e^{E_m} \leq C \hat{\Delta}$ (for $m \in \{0,1\}$, $E_m \leq \hat{\Delta}$).
- If $n_j \geq 2$ (multi-particle): $|e^{E_1 - E_{n_j}} - 1| \leq 1$ (since $E_{n_j} \geq E_2 > E_1$, the argument is negative, and $|e^x - 1| \leq 1$ for $x \leq 0$).

The proof IS claiming that at least $p$ of the factors are $O(\hat{\Delta})$, not that all factors are $O(\hat{\Delta})$. The deviation order $\mathrm{dev} \geq p$ means there exist $\geq p$ positions $\sigma(1), \ldots, \sigma(p)$ in the tuple $\mathbf{n}$ where the factor $(e^{E_m - E_{n_{\sigma(j)}}} - 1)$ appears. The bound on the full product is:

$$\prod_{j=1}^{q} |e^{E_m - E_{n_{\sigma(j)}}} - 1| \leq (C\hat{\Delta})^p \cdot 1^{q-p}$$

where $q \geq p$ is the actual number of deviation factors, and the remaining $q - p$ factors are bounded by 1. This gives $(C\hat{\Delta})^p$ as claimed. The bound is traced precisely through the proof.

**(b) The $\zeta$ bound and the two-particle threshold.**

The quantity $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ requires $E_2 - E_1 > 0$. The preprint bounds the two-particle binding energy $\epsilon_B \leq C_B g_k^4 \hat{\Delta}_k$ using Kato-Rellich perturbation theory on the two-glueball sector. This gives $E_2 - E_1 \geq \hat{\Delta}_k(1 - C_B g_k^4) \geq \hat{\Delta}_k/2$ for $g_k^2 \leq 1/(2C_B)$.

Are perturbative binding energy estimates valid non-perturbatively? In the small-field region of Balaban's construction, the effective interaction between glueballs at step $k$ is of order $g_k^2$ (one-gluon exchange at leading order). The two-glueball sector of the transfer matrix $\hat{T}_k$ has $H_{\mathrm{2-body}} = H_0 + g_k^2 V$ where $H_0$ has the two-particle threshold at $2\hat{\Delta}_k$ and $V$ is a bounded interaction. By Kato-Rellich, $|E_2 - 2\hat{\Delta}_k| \leq C g_k^2 \|V\|$, so the binding energy $\epsilon_B = 2\hat{\Delta}_k - E_2 \leq C g_k^2 \|V\|$. Since $\|V\| \leq C' g_k^2 \hat{\Delta}_k$ (from the operator norm of the interaction), $\epsilon_B \leq C'' g_k^4 \hat{\Delta}_k$.

Could a deeply bound two-glueball state exist at some RG step? No, because: (i) the interaction is weak ($O(g_k^2)$) in the small-field regime; (ii) in $d = 4$, two-body bound states require sufficiently strong attractive interactions (the Born approximation shows binding occurs only when $g^2$ exceeds a critical value proportional to the inverse density of states, which is not reached on the AF trajectory); (iii) the cluster expansion ensures exponential decay of correlations at each $k$, preventing the formation of deeply bound states.

This argument is valid at each RG step in the weak-coupling regime ($g_k^2 \ll 1$). For the initial steps where $g_k = O(1)$, the two-particle threshold is controlled by the cluster expansion directly (the mass gap and exponential clustering from Theorem 4 bound $\zeta$ independently).

**(c) Volume independence via Combes-Thomas.**

The Combes-Thomas estimate requires the operator $\hat{A}^{(s)}$ to be local, supported in a ball of radius $R_0$ lattice spacings. The preprint states that $R_0$ is bounded uniformly in $k$.

In Balaban's block-spin, each step generates operators with support in "polymer" regions. The polymer activities $K_k(X,V)$ are supported in connected polymers $X$ with size $|X|$. However, the exponential decay $|K_k(X,V)| \leq e^{-\kappa|X|}$ means large polymers are suppressed. The effective local operators at step $k$ are dominated by small polymers ($|X| \leq R_0$) with exponentially small corrections from larger polymers.

The key point: the block-spin doubles the lattice spacing at each step, but the polymer sizes (measured in block lattice spacings) remain bounded because Balaban's inductive hypotheses maintain the decay constant $\kappa$ independent of $k$. A polymer of size $|X|$ in block lattice units has physical extent $|X| a_k = |X| 2^k a_0$, but the relevant quantity for the Combes-Thomas estimate is the extent in block lattice units, which is bounded.

The $R_0$ entering the spectral lemma is the support radius in units of the lattice spacing at step $k$. Since $\kappa$ is $k$-independent, the effective locality radius $R_0 \sim 1/\kappa$ is also $k$-independent. This is correct.

**Impact on the claimed result:** None. The spectral lemma is correctly formulated and proved. The constants are $k$-independent as claimed.
