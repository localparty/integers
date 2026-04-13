# Node G — Form Convergence + Boegli Spectral Exactness (Layer 4)

**Chain layer:** 4 of 6
**Rigor label:** [THEOREM]
**Dependencies:** Node B (ITPFI), Node E (H$^1$ bound), Node F (CF decay)
**Status:** CLOSED

---

## Statement

**Theorem 9.1 (Spectral exactness).** $\operatorname{spec}(D_\infty) = \lim_{N \to \infty} \operatorname{spec}(D_N)$ with no spurious eigenvalues.

This follows from Boegli's spectral exactness theorem (arXiv:1604.07732, Theorem 2.6), applied in the self-adjoint specialization, once two hypotheses are verified:

- **(H1) Generalized strong resolvent convergence (gsrc):** $D_N \to D_\infty$ in gsrc.
- **(H2) Discrete compactness:** The resolvent family $\{(D_N - i)^{-1}\}$ is precompact.

---

## Proof of H1 (gsrc)

Three steps, using ITPFI (Node B) as the engine:

1. $J_N^* J_N \to I$ where $J_N$ are orthogonal projections onto exhausting Chebyshev basis (standard, textbook).

2. $D_N = P_N D_\infty P_N + \Delta_N$ where $\Delta_N = Q_N - P_N Q_0 P_N$ is the difference between the finite-$N$ form and the Galerkin projection of the limit form $Q_0$ (defined via ITPFI entry-by-entry convergence, independently of $D_\infty$'s eigenvectors). The perturbation $\|\Delta_N\| \to 0$ exponentially by CF decay (Node F): $\|\Delta_N\| \leq C_\Delta \cdot \rho^{-N}$. **Note:** $Q_0$ exists as a closed semibounded quadratic form (Reed-Simon I, Theorem VIII.7) independently of the KLMN construction of $D_\infty$ in Section 9, avoiding any circularity.

3. Second resolvent identity: gsrc follows from $\|\Delta_N\| \to 0$ + $J_N^* J_N \to I$.

**Alternative verification:** Teschl-Wang-Xie-Zhou (arXiv:2601.10476) Lemma 2.7 gives gsrc from the KLMN relative bound $a = 0 < 1$. This is immediate since the perturbation $\Delta_N$ is rank-1 with $\|\Delta_N\| \to 0$.

## Proof of H2 (discrete compactness)

Uniform H$^1$ bound (Node E): $\|(D_N - i)^{-1}\|_{L^2 \to H^1} \leq 2$ for all $N$. By Rellich-Kondrachov, $H^1 \hookrightarrow L^2$ compactly on bounded domains $[-L/2, L/2]$. Therefore the resolvent family is precompact in $L^2$.

**Independent backup:** CF decay (Node F) gives Arzela-Ascoli compactness directly.

---

## Boegli's theorem applied

With H1 + H2 verified, Boegli (Theorem 2.6, self-adjoint case) gives:

$$\operatorname{spec}(D_\infty) = \lim_{N \to \infty} \operatorname{spec}(D_N)$$

No spurious eigenvalues. No eigenvalue loss. The finite-$N$ spectra converge exactly to the infinite limit.

---

## Sources

- **Preprint:** sections-06-10.md §§9-10, Theorem 9.1
- **Research:** research/38-boegli-h1-gsrc.md, research/40-gsrc-ten-out-of-ten.md, research/41-teschl-klmn-gsrc.md
- **Literature:** Boegli arXiv:1604.07732, Teschl et al. arXiv:2601.10476, Reed-Simon II (KLMN)
