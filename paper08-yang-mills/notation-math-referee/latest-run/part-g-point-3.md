## Part G, Point 3: $N$-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

The claim is that the proof works uniformly for all SU($N$), $N \geq 2$.

**(a) $N$-dependent constants.** The paper tracks $N$-dependence through Appendix I.3. The key constants and their $N$-scaling:

| Constant | $N$-dependence | Source |
|:---------|:---------------|:-------|
| Spectral gap $\mu_1$ | $2N/r_3^2$ (grows with $N$) | Theorem 1 |
| KK mass $m_1$ | $2\sqrt{N}/r_3$ (grows) | Theorem 2 |
| Propagator constant $C_0$ | $O(\mathrm{poly}(N))$ | Weyl asymptotics |
| KP convergence threshold | Improves with $N$ (larger $m_1$) | Theorem 3 |
| Analyticity radius $\rho$ | $O(1/\mathrm{poly}(N))$ | CMP 98, $r_{\mathrm{proj}}(N)$ |
| Lie algebra $C_D$ | $N^2 - 1$ | Adjoint dimension |
| Spectral lemma $C_p$ | $O(\mathrm{poly}(N))$ | Hastings–Koma |
| Gronwall exponent $\gamma$ | $O(\mathrm{poly}(N)/N)$ | $\alpha/(b_0 \ln 2)$ |
| $b_0$ | $11N/(48\pi^2)$ | One-loop |

Verified computationally: $b_0 = 11N/(48\pi^2)$ matches the standard result. Dual Coxeter numbers: SU(2)→2, SU(3)→3, SU(4)→4, SU(5)→5. Lie algebra dimensions: A2→8, A3→15, A4→24. These are consistent with the paper.

**(b) SU(2) special properties.** For $N=2$: $d^{abc} = 0$ (all cubic-Casimir operators vanish identically), $\mathbb{CP}^1 = S^2$ (round sphere), and the exact area law $\sigma = 3g^2/8$ provides an independent check. The paper gives a self-contained SU(2) proof (Section 4.6 / Appendix H) using the exact solvability of 2D Yang–Mills on $S^2$. For $N \geq 3$, the cubic operators exist but are eliminated by $\mathcal{C}$-symmetry (Section 5.3.1). This $\mathcal{C}$-elimination works for all $N \geq 3$ uniformly.

The Haar integral $\int (\mathrm{Re}\,\mathrm{Tr}\,U)^2 dU = 1/2$ for $N \geq 3$ and $= 1$ for $N = 2$ was verified computationally by Schur orthogonality. The paper does not use this integral directly, but it enters the plaquette activity bound.

**(c) Error compounding.** The proof chain has ~14 steps, each with $N$-dependent constants. If each constant has a factor of $N^2$ (from Lie algebra), the accumulated error could grow as $N^{28}$. However, the proof only claims a mass gap for each **fixed** $N$ — large-$N$ asymptotics are not required. For each fixed $N$, all constants are finite, and the doubly exponential convergence $4^{-K}$ in the outer sum overwhelms any polynomial $N$-dependent prefactor.

**Gap:** The systematic tracking in Appendix I.3 should explicitly state the polynomial degree of $N$-dependence for the final constant $C_\infty$, showing it is bounded for each fixed $N$. The current treatment tracks individual constants but does not give the total accumulated $N$-dependence as a closed-form bound. Closable in **1 paragraph** by collecting the polynomial bounds.

For the Clay prize, which requires the result for "any compact simple gauge group $G$," the proof must work for each fixed $G$ (not uniformly in $N$). The paper's approach satisfies this requirement: for each fixed $N$, the constants are finite and the proof goes through.

**Impact on the claimed result:**
Minor impact on the generality claim. The proof is valid for each fixed $N$, but the explicit $N$-dependence of the final constant could be stated more sharply.
