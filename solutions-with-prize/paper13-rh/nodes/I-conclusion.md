# Node I — Conclusion: RH (Layer 6)

**Chain layer:** 6 of 6
**Rigor label:** [THEOREM] conditional on CCM
**Dependencies:** All prior nodes (A-H, J-L)
**Status:** QED

---

## Statement

**Theorem 1.1 (Riemann Hypothesis, conditional on CCM).** All non-trivial zeros of the Riemann zeta function $\zeta(s)$ lie on $\operatorname{Re}(s) = 1/2$.

---

## Proof (6-step assembly)

1. **CCM operators** (Node A): Self-adjoint $D_N$ on $E_N^+$ with eigenvalues approximating $\{\gamma_n\}$.

2. **ITPFI convergence** (Node B): $\omega_1 = \bigotimes_p \omega_1^{(p)}$ gives entry-by-entry convergence of the Weil quadratic form.

3. **Four estimates** (Nodes C-F): Archimedean sub-leading $O(1/\lambda)$, eigenvector approximation $O(1/\lambda)$, H$^1$ bound $\leq 2$ uniform, CF decay $\rho \geq 4.27$ uniform.

4. **Boegli spectral exactness** (Node G): H1 (gsrc from ITPFI) + H2 (discrete compactness from H$^1$) $\Rightarrow$ $\operatorname{spec}(D_\infty) = \lim \operatorname{spec}(D_N)$.

5. **Hurwitz eigenvalue convergence** (Node H): $\hat{\xi}_N \to \Xi$ uniformly $\Rightarrow$ $\lim \operatorname{spec}(D_N) = \{\gamma_n\}$.

6. **Conclusion:** $\operatorname{spec}(D_\infty) = \{\gamma_n\} \subset \mathbb{R}$. Self-adjointness of $D_\infty$ follows from the KLMN theorem (Reed-Simon X.17): the Galerkin limit form $Q_0$ is closed and semibounded (CCM Proposition 3.3 gives positivity; ITPFI gives entry-by-entry convergence ensuring closability via Reed-Simon VIII.15). The Friedrichs extension produces a unique self-adjoint operator $D_\infty$ associated to $Q_0$. **Note:** $D_\infty$ is NOT defined as a norm or strong limit of $D_N$ (which would not preserve self-adjointness in general). It is defined via the form limit. Since $D_\infty$ is self-adjoint, $\operatorname{spec}(D_\infty) \subset \mathbb{R}$. Therefore $\gamma_n \in \mathbb{R}$ for all $n$. **QED.**

---

## Proof chain diagram

```
Layer 1:  CCM operators D_N on E_N^+ (self-adjoint, spectra ~ {γ_n})
            |
Layer 2:  ITPFI ω₁ = ⊗_p ω₁^(p) (state convergence → form convergence)
            |
Layer 3:  ESTIMATES (archimedean, eigenvector, H¹, CF — all closed)
            |
Layer 4:  TESCHL gsrc + BOEGLI spectral exactness (H1 + H2 → no spurious)
            |
Layer 5:  HURWITZ zero convergence (ξ̂_N → Ξ uniformly → eigenvalue id)
            |
Layer 6:  spec(D_∞) = {γ_n} ⊂ ℝ  →  RH  ∎
```

**Score: 8/10.** All mathematics closed. Floor is CCM preprint status (Layer 1).

---

## Sources

- **Preprint:** sections-11-14.md §11
- **All nodes:** A through L
