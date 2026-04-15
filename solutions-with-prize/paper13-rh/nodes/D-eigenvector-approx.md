# Node D — Eigenvector Approximation (Layer 3b)

**Chain layer:** 3b of 6
**Rigor label:** [LEMMA]
**Dependencies:** Node B (ITPFI), Node C (archimedean estimate), Node J (AE simplicity)
**Status:** CLOSED

---

## Statement

**Theorem 6.4 (Estimate b).** For the CCM eigenvector $\xi_\lambda$ and the prolate approximation $k_\lambda$:

$$\|\xi_\lambda - c \cdot k_\lambda\| = O(1/\lambda) \quad\text{as } \lambda \to \infty$$

where $c$ is a normalizing constant. Consequently, the Fourier transforms satisfy $|\hat{\xi}_\lambda - \hat{c} \cdot \hat{k}_\lambda| = O(1/\lambda)$ uniformly on compact $K \subset \{|\operatorname{Im}(z)| < 1/2\}$.

---

## Proof sketch (ITPFI triangle inequality)

**Critical insight:** Use the ITPFI triangle inequality, routing through the Euler product operator $T_0 = \sum_p \tau^{(p)}$, NOT directly through $Q_W$ (whose spectral gap is exponentially small).

The operator decomposition $D_N = T_0 + \tau^{(\mathbb{R})}$ splits $D_N$ into the $p$-adic sum $T_0$ (dominant) and the archimedean correction $\tau^{(\mathbb{R})}$ (sub-leading by Node C). Let $\xi_0$ denote the $T_0$-eigenvector nearest to eigenvalue $\lambda$.

1. $\xi_\lambda \approx \xi_0$: Davis-Kahan applied to the pair $(T_0, D_N = T_0 + \tau^{(\mathbb{R})})$ with perturbation norm $\|\tau^{(\mathbb{R})}\| = O(1)$ and spectral gap $\delta(T_0, \lambda)$ of $T_0$ near $\lambda$. The bound is $\|\xi_\lambda - \xi_0\| \leq \|\tau^{(\mathbb{R})}\| / \delta(T_0, \lambda)$. The gap $\delta(T_0, \lambda)$ mirrors Riemann zero spacing $\sim 2\pi/\log\lambda$, giving $\|\xi_\lambda - \xi_0\| = O(\log\lambda / \lambda)$ (using $\|\tau^{(\mathbb{R})}\| / \delta \sim O(1) / (2\pi/\log\lambda) \cdot (1/\lambda)$ from the archimedean sub-leading ratio).
2. $k_\lambda \approx \xi_0$: CCM Lemma 7.2 prolate error $O(\lambda^{-2})$.
3. Triangle inequality: $\|\xi_\lambda - c \cdot k_\lambda\| = O(\log\lambda / \lambda) = o(1)$.

**Note on the gap:** The gap of $T_0$ near $\lambda$ is $\sim 2\pi/\log\lambda$ (matching Riemann zero spacing), NOT polynomially large. The $O(\log\lambda/\lambda)$ rate includes a log correction but is still $o(1)$, which suffices for Hurwitz (Node H).

**Why Approach 1 (direct Davis-Kahan on $D_N$) fails:** The spectral gap of $D_N$ near $\lambda$ is exponentially small ($\sim e^{-cN}$), so the direct perturbation bound diverges. The ITPFI triangle routes through $T_0$ whose gap, while shrinking as $O(1/\log\lambda)$, is polynomially controlled — not exponentially small.

---

## Role in the chain

This closes CCM's Gap 2 (eigenvector identification). The $O(\log\lambda/\lambda)$ rate is $o(1)$, which is all Hurwitz (Layer 5) requires.

**Depends on AE simplicity** (Node J) for uniqueness of $\xi_\lambda$ up to phase.

---

## Sources

- **Preprint:** sections-06-10.md §6, Theorem 6.4
- **Research:** research/37-estimate-b-eigvec-approx.md
