## Part G, Point 3: $N$-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** SOUND (with a minor presentation inconsistency to reconcile)

**Finding:**

**(a) $N$-dependent constants.** Appendix I.3 systematically tracks $N$-dependence through the entire proof chain. The complete catalog (14 items):

| Constant | $N$-scaling | Direction |
|----------|-----------|-----------|
| Spectral gap $\mu_1$ | $\geq 2N/r_3^2$ | FAVORABLE |
| KK mass $m_1$ | $2\sqrt{N}/r_3$ | FAVORABLE |
| Bond constant $C_0$ | $O(N^{N-1})$ (crude) | Unfavorable but absorbed |
| Cluster threshold $\beta_{\max}$ | $\sim \sqrt{N}\,a/(6r_3)$ | FAVORABLE |
| Polymer decay $\kappa$ | $> 0$, decreasing in $N$ | Finite for fixed $N$ |
| Analyticity radius $\rho$ | $O(1/N^2)$ | Finite for fixed $N$ |
| $\beta$-function $b_0$ | $11N/(48\pi^2)$ | FAVORABLE |
| Gronwall exponent $\gamma$ | $\sim N$ (see below) | Finite for fixed $N$ |
| Spectral lemma $C_p$ | $\leq \exp(C_1 R_0^3 N^2)$ | Worst-case but finite |
| Operator norm $C$ | poly($N$) | Finite for fixed $N$ |
| $C_{\mathrm{new}}$ | $\leq \exp(C_1 R_0^4 N^2)$ | Finite for fixed $N$ |
| Fixed point $C_*$ | $(4/3)C_{\mathrm{new}}(N)$ | Finite for fixed $N$ |
| RG sum | converges for each $N$ | $\checkmark$ |

The critical observation: the $1/4$ contraction factor in the RG recursion is N-INDEPENDENT (it's a geometric property of $L = 2$ blocking in $d = 4$). This $N$-independent exponential factor dominates all $N$-dependent polynomial or sub-exponential growth.

**(b) SU(2) special properties.** For $N = 2$:
- $d^{abc} = 0$ (no cubic Casimir): all dim-6 non-derivative operators vanish identically. This is a simplification, not a requirement.
- $\mathbb{CP}^1 = S^2$ (round sphere): simpler geometry with additional exact results.
- Exact area law $\sigma = 3g^2/8$: from 2D YM on $S^2$ (exact solution).

The proof for general $N$ does NOT use these SU(2)-specific properties. The dim-6 non-derivative operators are eliminated by $\mathcal{C}$-symmetry for ALL $N \geq 2$ (not by the vanishing of $d^{abc}$). The cluster expansion and RG recursion use only properties available for general SU($N$).

**(c) Error compounding -- the $\gamma$ discrepancy.** The proof chain has $\sim 14$ steps. If each constant has an $N$-dependent factor, the accumulated error grows polynomially in $N$. The key question: does this growth overwhelm the $4^{-k}$ convergence?

The answer is NO, because $4^{-k}$ is EXPONENTIAL in $k$, while $N$-dependent growth is at most polynomial in $k$ (through $k^\gamma$). For any finite $\gamma$, $k^\gamma \cdot 4^{-k} \to 0$ exponentially.

**The discrepancy to reconcile:** Appendix I.3 (full version) derives $\gamma \sim N$ (from $\alpha \sim N^2$ and $b_0 \sim N$, giving $\gamma = \alpha/(b_0 \ln 2) \sim N$). The compressed I.3 in the umbrella file Appendix I lists $\gamma \sim 1/N$ (apparently using $\alpha \sim N$). The more conservative value $\gamma \sim N$ should be used.

This discrepancy is a PRESENTATION ISSUE, not a mathematical error:
- With $\gamma = N$: $\sum k^{N-2} 4^{-k}$ converges for every finite $N$ (ratio test gives limit $1/4$)
- With $\gamma = 1/N$: $\sum k^{1/N - 2} 4^{-k}$ converges even faster

Neither value affects the proof's validity. But the preprint should reconcile the two stated values.

**Overall $N$-dependence assessment:** The proof establishes, for each fixed $N \geq 2$:
1. Every constant is finite (tracked in Appendix I.3)
2. The RG sum converges (dominated by $4^{-k}$)
3. $\Delta_\infty(N) > 0$ (positive, $N$-dependent)

The Clay prize requires each fixed $N$, not large-$N$ asymptotics. The proof satisfies this requirement.

**Impact on the claimed result:** None. All constants are finite for fixed $N$, the $4^{-k}$ convergence dominates any $N$-dependent polynomial growth, and the mass gap is positive for each $N$. The $\gamma$ discrepancy between the full and compressed I.3 should be reconciled for clarity but does not affect any mathematical conclusion.
