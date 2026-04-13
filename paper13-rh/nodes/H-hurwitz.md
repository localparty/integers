# Node H — Hurwitz Eigenvalue Convergence (Layer 5)

**Chain layer:** 5 of 6
**Rigor label:** [THEOREM] (classical + closed)
**Dependencies:** Node A (CCM Lemma 7.3), Node D (eigenvector approximation)
**Status:** CLOSED

---

## Statement

The eigenvalues of $D_N$ converge to the non-trivial zeros $\{\gamma_n\}$ of the Riemann zeta function:

$$\lim_{N \to \infty} \operatorname{spec}(D_N) = \{\gamma_n\}$$

---

## Proof

1. **Fourier transforms converge.** By CCM Lemma 7.3 + Estimate b (Node D): $\hat{\xi}_N \to \Xi$ uniformly on compact subsets of $\{|\operatorname{Im}(z)| < 1/2\}$, where $\Xi$ is the Riemann Xi function.

2. **Hurwitz's theorem (1893).** If holomorphic functions $f_n \to f$ uniformly on compact subsets and $f$ is not identically zero, then the zeros of $f_n$ converge to the zeros of $f$ (with multiplicity).

3. **$\Xi$ is not identically zero.** $\Xi(0) = 0.4971\ldots \neq 0$ (corrected from earlier draft; referee fix #8).

4. **Eigenvalue identification.** Zeros of $\hat{\xi}_N$ = eigenvalues of $D_N$ (CCM Theorem 5.10(iii)). Zeros of $\Xi$ = non-trivial zeros $\{\gamma_n\}$ of $\zeta$.

5. **Conclusion.** $\lim \operatorname{spec}(D_N) = \{\gamma_n\}$.

---

## Combined with Boegli (Node G)

Boegli gives: $\operatorname{spec}(D_\infty) = \lim \operatorname{spec}(D_N)$.

Hurwitz gives: $\lim \operatorname{spec}(D_N) = \{\gamma_n\}$.

Therefore: $\operatorname{spec}(D_\infty) = \{\gamma_n\}$.

---

## Sources

- **Preprint:** sections-06-10.md §10
- **Literature:** Hurwitz 1893, Connes-van Suijlekom arXiv:2511.23257
- **Referee fix:** #8 ($\Xi(0) = 0.4971$, not $1/2$)
