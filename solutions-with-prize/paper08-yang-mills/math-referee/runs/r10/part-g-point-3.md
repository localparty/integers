## Part G, Point 3: $N$-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) $N$-dependent constants.**

Appendix I.3 provides systematic tracking of $N$-dependent constants through the proof chain. The key constants and their $N$-scaling:

| Constant | $N$-scaling | Effect |
|:---------|:-----------|:-------|
| Spectral gap $\mu_1$ | $2N/r_3^2 \sim N$ | **FAVORABLE** (larger gap at larger $N$) |
| KK mass $m_1$ | $\sqrt{2(N+1)}/r_3 \sim \sqrt{N}$ | **FAVORABLE** |
| Bond constant $C_0$ | $O(N^{N-1})$ (Weyl sum) | Absorbed by $e^{-m_1 a}$ |
| Analyticity radius $\rho$ | $O(1/N^2)$ (from $r_{\mathrm{proj}}, C_D$) | Positive for each $N$ |
| $\beta$-function $b_0$ | $11N/(48\pi^2) \sim N$ | **FAVORABLE** (faster AF) |
| Spectral lemma $C_p$ | $\leq \exp(C_1 R_0^3 N^2)$ | Enter as prefactors only |
| Gronwall exponent $\gamma$ | $O(1/N)$ | **FAVORABLE** |

No constant grows so fast with $N$ that the proof fails for large $N$. The critical convergence mechanism is the $4^{-k}$ geometric contraction from lattice coarsening, which is $N$-independent. All $N$-dependent constants enter as multiplicative prefactors in the convergent sum $\sum C_k g_k^4 \hat{\Delta}_k^2$, modifying the numerical value of $\Delta_\infty$ but not the convergence.

The worst case is $C_p(N) \sim \exp(C_1 R_0^4 N^2)$ from the Combes-Thomas estimate. This enters the spectral lemma bound as $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p(N) M \hat{\Delta}^2$. The exponential-in-$N^2$ growth of $C_p$ is a large but finite constant for each fixed $N$, and it does not affect the convergence of the RG recursion.

**(b) SU(2) special properties.**

For $N = 2$:
- Cubic Casimir $d^{abc} = 0$: all dimension-6 non-derivative operators vanish identically. This simplifies the proof but is NOT used for general $N$ — the $\mathcal{C}$-elimination argument works for all $N \geq 2$ (it eliminates $\mathrm{Tr}(F^3)$ as $\mathcal{C}$-odd, regardless of whether $d^{abc} = 0$).
- $\mathbb{CP}^1 = S^2$: simpler geometry, but the proof uses only the Weitzenböck bound and spectral gap, which work for any $\mathbb{CP}^{N-1}$.
- Exact area law $\sigma = 3g^2/8$: provides an independent check for SU(2) but is not used in the general proof. The general proof uses the cluster expansion for the area law, which applies to all $N$.

No SU(2)-specific property is used in the general proof that fails for $N \geq 3$. The SU(2) case serves as a consistency check, not a logical dependency.

**(c) Error compounding.**

The proof chain has $\sim 14$ steps, each with bounds containing $N$-dependent constants. If each constant has a factor of $N^2$ (from the Lie algebra), the accumulated error could grow as $N^{28}$ in the worst case.

However, the proof works for each fixed $N$ separately — large-$N$ asymptotics are not required. For each fixed $N$:

1. Every constant $C(N)$ is a finite number.
2. The RG recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}}(N) + O(g_k^2 C_k)$ converges to a fixed point $C_*(N) = 4C_{\mathrm{new}}(N)/3$ regardless of the magnitude of $C_{\mathrm{new}}(N)$.
3. The convergence rate $4^{-k}$ is $N$-independent.
4. The sum $\sum C_k g_k^4 \hat{\Delta}_k^2$ converges for any finite $C_*(N)$.

The $N$-dependence is NOT absorbed into uncontrolled constants: Appendix I.3 provides explicit tracking with the table above. The accumulated $N$-dependence produces a finite (possibly large) value of $\Delta_\infty(N)$ for each $N$, which is all that's needed.

For the Clay prize: the proof must work for each fixed $N \geq 2$ (and for each compact simple group). It does. The $N$-dependence of the mass gap value $\Delta_\infty(N)$ is a physical prediction, not a mathematical weakness.

**Impact on the claimed result:**

None. The $N$-dependence is systematically tracked (Appendix I.3). All constants are finite for each fixed $N$, the convergence mechanism ($4^{-k}$ contraction) is $N$-independent, and no SU(2)-specific property is required for the general proof. The proof works uniformly in the sense that the same argument applies to every $N$, with $N$-dependent constants that are finite for each $N$.
