## Part G, Point 3: $N$-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP (Gronwall direction discrepancy); SOUND (proof works for each fixed $N$)

---

**Finding:**

**(a) $N$-dependent constants through the proof chain.** The $N$-dependent quantities and their behavior:

| Quantity | $N$-dependence | Source |
|:---------|:---------------|:-------|
| $\mu_1$ on $\mathbb{CP}^{N-1}$ | $4N/r_3^2$ (exact) | Appendix E, Ikeda-Taniguchi |
| $m_1 = 2\sqrt{N}/r_3$ | $\sim\sqrt{N}$ | Exact eigenvalue |
| $C_0$ (bond activity constant) | $\sim N^{2N-4}$ (Weyl asymptotics) | Theorem 2, Step 4 |
| $\kappa(N)$ (polymer convergence) | $\sim 1/N^2$ (from $C_D \sim N^2$) | Section 5.1.2 |
| $r_{\text{proj}}(N)$ (block-spin radius) | $O(1/\sqrt{N})$ | Section 5.1.2 |
| $C_D \sim N^2-1$ | $\sim N^2$ | Section 5.1.2 |
| $b_0 = 11N/(48\pi^2)$ | $\sim N$ | One-loop $\beta$-function |
| $\gamma = \alpha/(b_0 \ln 2)$ | disputed (see below) | Section 5.4.6 |
| $C_p$ (spectral lemma constant) | $O(N^?)$ | Section 5.5.3 |

For each fixed $N$, all these constants are finite. The proof establishes $\Delta_\infty > 0$ for each fixed $N$. No constant grows to infinity as $N$ is fixed, and the accumulation of $N^2$ factors through 14 proof steps gives at most $N^{28}$ for the accumulated constant — which is finite for each fixed $N$. For large $N$, the constants are large but not infinite.

The proof does not claim uniformity in $N$ (the bound $\Delta_\infty \geq C_N > 0$ is not uniform in $N$). For the Clay Prize, each fixed $N$ is separate, and the proof works for each. SOUND.

**(b) SU(2) special properties.** For $N=2$:
- $d^{abc} = 0$: the $d$-symbol operator $\mathcal{O}_3$ vanishes identically. The classification is simpler (only $\mathrm{Tr}(D_\rho F)^2$ survives at dimension 6).
- $\mathbb{CP}^1 = S^2$: the internal space is a round sphere, which is simpler than $\mathbb{CP}^{N-1}$ for $N \geq 3$. The spectral gap $\mu_1(S^2) = 2/r^2$ (from $4N/r^2 = 8/r^2$ for $N=2$... wait, $4 \times 2/r^2 = 8/r^2$ for $N=2$). The SU(2) case has all the same structural features.

Does the proof use any SU(2)-specific property that fails for $N \geq 3$? No: the $\mathcal{C}$-elimination argument works for all $N$ (the $\mathrm{Tr}(F^3)$ operator exists for $N \geq 3$ but is $\mathcal{C}$-odd, so it's eliminated regardless; for $N=2$ it vanishes identically). The Weitzenböck formula holds for all $N$. The cluster expansion holds for all $N$. The spectral lemma and deviation order arguments are $N$-independent in structure. No SU(2)-special property is used. SOUND.

**(c) Gronwall exponent discrepancy — CLOSABLE GAP.** Two appendices of the same paper give contradictory $N$-dependence for $\gamma = \alpha/(b_0 \ln 2)$:

- **I-gap-closures.md, Section I.3.2**: $\gamma \sim 1/N$. This appears to follow from the incorrect eigenvalue formula $\mu_{\min}^{(1)} = 2(N+1)/r_3^2$ (wrong; should be $4N/r_3^2$) and an error in the coefficient $\alpha$.

- **I3-N-dependence-tracking.md**: $\gamma \sim N$, because $\alpha \sim N^2$ (adjoint representation Casimir $C_A = N$ for SU($N$), but the *dimension* of the adjoint representation is $N^2-1 \sim N^2$, which enters $\alpha$) and $b_0 \sim N$, giving $\gamma \sim N^2/N = N$.

The correct direction is $\gamma \sim N$: the $O(g_k^2)$ correction coefficient $\alpha$ comes from the block-spin change to the operator coefficients, which scales as the dimension of the adjoint representation ($N^2-1$). The one-loop beta function coefficient $b_0 = 11N/(48\pi^2) \sim N$. So $\gamma = \alpha/(b_0 \ln 2) \sim (N^2)/(N) = N$.

This means $C_k \sim k^N$, and the accumulated constant in the RG sum is $C_* \sim N$ (independent of $k$ at the fixed point). For large $N$, $C_k \sim k^N$ grows faster with $k$ for large $N$, but the sum $\sum_k k^N g_k^4 (a_k\Lambda)^2 \sim \sum_k k^{N-2} 4^{-k}$ converges for all $N$ (the doubly exponential $4^{-k}$ dominates any polynomial $k^{N-2}$). The proof works for all fixed $N$.

The discrepancy between I.3 ($\gamma \sim 1/N$) and I-gap-closures.md ($\gamma \sim 1/N$, same direction but different formula origin) vs. I3-N-dependence-tracking.md ($\gamma \sim N$) is:
- I-gap-closures.md: appears to use the wrong eigenvalue formula, cascading to wrong $\gamma$.
- I3-N-dependence-tracking.md: appears correct in direction.
- The preprint's Section 5.4.6 says "$C_k \sim k^\gamma$" without specifying $\gamma$'s $N$-dependence.

Closing requires: (1) fix the eigenvalue formula in I-gap-closures.md from $2(N+1)/r_3^2$ to $4N/r_3^2$; (2) recompute $\gamma$ in I-gap-closures.md; (3) verify consistency with I3-N-dependence-tracking.md. Difficulty: **1 paragraph** in each appendix.

**(d) Error compounding through 14 steps.** The proof has approximately 14 steps in the PROOF-CHAIN.md. Each step introduces constants that may have factors of $N$. With $N^2$ per step from Lie algebra dimension, the accumulated constant is at most $N^{28}$ for the 14-step chain. For each fixed $N$, this is finite. The Clay Prize requires the proof to work for each fixed $N$, not uniformly in $N$, so this is acceptable.

The preprint does not provide a systematic $N$-dependent bound on the accumulated constant. Appendix I.3 attempts to track $N$-dependence but has errors (see point A1 and the discrepancy above). For a complete Clay Prize proof, a systematic $N$-dependence tracking is needed to guarantee that each constant is finite for each fixed $N$. The preprint's claim that "all three constants are polynomial in $N$" (Section 5.1.2) partially addresses this, but the tracking is incomplete.

**Impact on the claimed result:** For each fixed $N$, the proof establishes $\Delta_\infty > 0$. The Gronwall exponent discrepancy ($\gamma \sim N$ vs. $\gamma \sim 1/N$) does not affect this qualitative conclusion (any finite $\gamma$ works), but it is an inconsistency in the quantitative appendices. For Clay Prize purposes, the $N$-dependence tracking must be internally consistent. The current state (two appendices contradicting each other) is not acceptable.
