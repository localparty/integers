## Part G, Point 3: $N$-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) $N$-dependent constants.**

Appendix I.3 tracks $N$-dependence through all 14 steps of the proof chain. The key constants and their $N$-scaling:

| Constant | $N$-scaling | Direction |
|:---------|:-----------|:----------|
| Spectral gap $\mu_1 = 2N/r_3^2$ | $\sim N$ | Favorable (larger gap) |
| KK mass $m_1 = 2\sqrt{N}/r_3$ | $\sim \sqrt{N}$ | Favorable (stronger suppression) |
| Bond constant $C_0$ | $O(N^{N-1})$ | Unfavorable (but absorbed by $e^{-m_1 a}$) |
| Cluster threshold $\beta_{\max}$ | $\sim \sqrt{N}$ | Favorable (wider window) |
| Analyticity radius $\rho$ | $O(1/N^2)$ | Unfavorable (but positive for each $N$) |
| $\beta$-function $b_0 = 11N/(48\pi^2)$ | $\sim N$ | Favorable (faster AF) |
| Gronwall exponent $\gamma$ | $\sim N$ | Unfavorable (polynomial growth) |
| Spectral lemma $C_p$ | $\leq \exp(C N^2)$ | Unfavorable (but finite for each $N$) |
| Combes-Thomas $\zeta$ | $\leq \exp(C' N^2)$ | Unfavorable (but finite for each $N$) |

Does any constant grow so fast with $N$ that the proof fails for large $N$? No. The doubly exponential convergence factor $4^{-k}$ is $N$-independent and dominates all polynomial or sub-exponential growth in $N$. The sum $\sum_k C_k g_k^4 \hat{\Delta}_k^2$ converges for each fixed $N$ because $4^{-k}$ provides geometric convergence with ratio $1/4 < 1$, independent of $N$.

The mass gap value $\Delta_\infty(N)$ may decrease with $N$ (because the constants $C_\infty(N)$ and $\Lambda_\infty(N)$ have worse bounds for larger $N$), but positivity is guaranteed.

**(b) SU(2) special properties.**

For $N = 2$: the cubic Casimir $d^{abc} = 0$, so all dimension-6 non-derivative operators vanish identically (not just by $\mathcal{C}$-symmetry). The internal space $\mathbb{CP}^1 = S^2$ is the round 2-sphere, with simpler geometry (isomorphic to SU(2)/U(1)). The exact area law $\sigma = 3g^2/8$ provides an independent consistency check.

Does the proof use any SU(2)-specific property that doesn't generalize? No. The proof chain works for general SU($N$):
- The $\mathcal{C}$-elimination of $\mathrm{Tr}(F^3)$ works for all $N$ (it is $\mathcal{C}$-odd for all $N \geq 3$, and identically zero for $N = 2$).
- The cluster expansion uses $\mu_1 = 2N/r_3^2$ (valid for all $N$).
- The Feshbach projection uses $m_1 = 2\sqrt{N}/r_3$ (valid for all $N$).
- The deviation order argument uses the dimension-6 classification (valid for all $N$).

The SU(2) exact area law is used as an independent check, not as an input to the proof.

**(c) Error compounding.**

The proof chain has $\sim 14$ steps. If each constant $C$ has a factor of $N^2$ from the Lie algebra, the accumulated error could grow as $N^{28}$. This is a large number for large $N$, but for each FIXED $N$, it is finite.

The systematic tracking in I.3 (Lemma I.3.1) proves: "For each fixed $N \geq 2$, the sum $\sum_{k=0}^\infty C_k g_k^4 \hat{\Delta}_k^2$ converges." The proof uses the ratio test: $a_{k+1}/a_k \to 1/4 < 1$. The factor $1/4$ is universal ($N$-independent). The ratio test is insensitive to the prefactor — even if $C_k$ grows as $N^{28} k^\gamma$, the ratio $(k+1)^\gamma/(4k^\gamma) \to 1/4$ for large $k$.

For the Clay prize, the proof must work for each fixed $N$ — large-$N$ asymptotics are not required. The preprint correctly states this (I.3, Section I.3.1): "We do not claim or require large-$N$ asymptotics."

The proof is uniform in $N$ in the following sense: the STRUCTURE of the argument (cluster expansion, deviation order, RG recursion) is the same for all $N$. The CONSTANTS depend on $N$ but are finite for each $N$. This is sufficient for the Jaffe-Witten problem, which asks for a proof "for any compact simple gauge group" — meaning for each group separately, not uniformly in the group.

**Impact on the claimed result:** None. The $N$-dependence is systematically tracked, all constants are finite for fixed $N$, and the convergence factor $4^{-k}$ is universal.
