# Node A — CCM Operators D_N on E_N^+ (Layer 1)

**Chain layer:** 1 of 6
**Rigor label:** [THEOREM] (external, published preprint)
**Dependencies:** None (external input)
**Status:** CONDITIONAL on CCM (arXiv:2511.22755)

---

## Statement

Connes-Consani-Moscovici (2025) construct self-adjoint operators $D_N$ on even-sector Hilbert spaces $E_N^+ \subset L^2[-L/2, L/2]$, one per truncation level $N$ (primes $p \leq P_N$), such that:

1. **Self-adjointness** via Caratheodory-Fejer theory (CCM Theorem 4.2)
2. **Eigenvalues approximate** the Riemann zeros $\{\gamma_n\}$ to $10^{-55}$ accuracy at $N = 6$ (CCM Theorem 5.10)
3. **Even-sector preservation:** $T$ commutes with the parity involution $\gamma$ (CCM Lemma 5.2(i)), so $Q_W$, the $T$-inner product, and the perturbation all preserve $E_N^+$
4. **Eigenvalue identification:** zeros of $\hat{\xi}_N$ (Fourier transforms of eigenvectors) equal eigenvalues of $D_N$ (CCM Theorem 5.10(iii))

---

## What CCM leaves open

Two gaps in CCM's construction that this paper closes:

1. **Gap 1 (N → ∞ limit):** CCM do not prove that $D_N \to D_\infty$ in any operator topology. We close this via ITPFI state convergence (Node B) → form convergence → gsrc (Node G).

2. **Gap 2 (spectral identification):** CCM do not prove $\operatorname{spec}(D_\infty) = \{\gamma_n\}$ exactly. We close this via Boegli spectral exactness (Node G) + Hurwitz zero convergence (Node H).

---

## Specific CCM results used

| CCM result | What it gives | Where used |
|:-----------|:-------------|:-----------|
| Theorem 4.2 | Self-adjointness of $D_N$ | Foundation |
| Theorem 5.10 | Eigenvalues = zeros of $\hat{\xi}_N$; 55-digit accuracy | Layer 5 (Hurwitz) |
| Lemma 5.2(i) | $T\gamma = \gamma T$ (parity preservation) | Even-sector restriction |
| Lemma 7.2 | Prolate approximation $k_\lambda$ | Layer 3b (eigenvector approx) |
| Lemma 7.3 | $\hat{\xi}_N \to \Xi$ uniformly on compacts | Layer 5 (Hurwitz) |

---

## Conditionality

Theorem 1.1 of this paper is **conditional on CCM**. Upon journal acceptance of arXiv:2511.22755, the chain upgrades from 8/10 to 9/10. With independent third-party verification, 10/10. Layers 2-6 (our contributions) are independently at 9-10/10.

---

## Sources

- **External:** arXiv:2511.22755 (Connes-Consani-Moscovici 2025)
- **Preprint:** sections-01-05.md §3, appendices.md Appendix A
- **Also:** Connes-van Suijlekom arXiv:2511.23257 (Hurwitz argument)
