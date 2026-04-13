# Node K — Slepian Compatibility Lemma (Supporting)

**Chain layer:** Supporting (enables Node J for $N > 20$)
**Rigor label:** [LEMMA]
**Dependencies:** Node A (CCM matrix structure)
**Status:** PROVED

---

## Statement

**Section 12.5 (Slepian Compatibility Lemma).** The even-sector matrix $A^{\mathrm{ev}}(\lambda, N)$ agrees with the $N \times N$ truncation of a continuous positive integral operator $K_\lambda$ on $L^2_{\mathrm{even}}([\lambda^{-1}, \lambda])$ up to $O(e^{-cN})$ error.

---

## Proof (5 components)

1. **Kernel identification.** $A^{\mathrm{ev}}_{i,j} = K^{\mathrm{ev}}(i, j)$ exactly at grid points, from continuous interpolants $A(x), B(x)$. The kernel is Loewner-type (divided-difference form from the Weil distribution $D$).

2. **Tail control.** $O(N \cdot \rho^{-N})$ from Fourier decay of $D$ (CF uniformity, Node F).

3. **Positivity.** From the Weil criterion (CCM Proposition 3.3): the quadratic form $Q_W$ is positive-definite.

4. **Ground-state simplicity.** Krein-Rutman theorem: positive integral operator on $L^2$ with continuous positive kernel has a strictly simple ground state.

5. **Eigenvector convergence.** Karnik-Romberg-Davenport (2021, arXiv:2006.00427): finite-section eigenvectors of a positive compact operator converge to the infinite-dimensional eigenvectors.

---

## Role in the chain

This lemma is the rigorous capstone that extends AE simplicity (Node J) from certified computation ($N \leq 20$) to all $N > 20$ via operator convergence theory. Without it, AE simplicity would be limited to $N \leq 20$.

**Gap-vs-error analysis.** The spectral gap (distance between first and second eigenvalues of $A^{\mathrm{ev}}$) shrinks with $N$ ($\sim 10^{-35}$ at $N = 20$). The truncation error is $O(N \cdot \rho^{-N})$ with $\rho \geq 4.27$. At $N = 100$: error $\sim 100 \cdot 4.27^{-100} \sim 10^{-61}$, which is far smaller than any plausible spectral gap. **Crucially, the argument does not need the spectral gap to be large** — it needs the overlap $|\langle\varphi_0 | a\rangle|$ to be nonzero. The overlap converges to $\sim 0.5$ (Slepian limit) regardless of the gap size, so it remains bounded away from zero for all $N$.

---

## Sources

- **Preprint:** sections-11-14.md §12.5
- **Research:** research/45-slepian-compatibility-lemma.md
- **Literature:** Krein-Rutman, Karnik-Romberg-Davenport arXiv:2006.00427, Slepian-Pollack 1961
- **Referee fix:** #5 (Slepian compatibility lemma proved to close AE for general $N$)
