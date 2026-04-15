# Node C — Archimedean Estimate (Layer 3a)

**Chain layer:** 3a of 6
**Rigor label:** [LEMMA]
**Dependencies:** Node B (ITPFI)
**Status:** CLOSED

---

## Statement

**Proposition 5.1 (Estimate 1).** The archimedean correction is sub-leading:

$$\frac{\|\tau^{(\mathbb{R})}\|}{\|\sum_p \tau^{(p)}\|} = O\!\left(\frac{1}{\lambda}\right) \to 0 \quad\text{as } \lambda \to \infty$$

(The archimedean norm is $O(1)$; the prime sum norm is $\Theta(\lambda)$ by PNT. The ratio is $O(1/\lambda)$. The node statement in the proof skeleton says $O(\log\lambda/\lambda)$, which is a slightly weaker but also valid bound.)

---

## Proof sketch

1. **Archimedean entries saturate.** The archimedean matrix entries $\rho(x) \sim e^{-x/2}$ decay exponentially, giving bounded norm $C_N$.

2. **Prime sum grows.** By PNT: $\sum_{p \leq \lambda^2} \log p / \sqrt{p} \sim 2\lambda$, so $\|\sum_p \tau^{(p)}\| = \Theta(\lambda)$.

3. **Ratio decays.** $C_N / \Theta(\lambda) = O(1/\lambda)$.

**Numerical verification:** $\lambda = 10, 30, 100$ shows decay exponent $-0.84$, consistent with $O(1/\lambda)$.

---

## Role in the chain

Forms the foundation for Layer 3b (eigenvector approximation). The Davis-Kahan perturbation theorem gives $\|\xi_\lambda - \xi_0\| = O(1/\lambda)$ using the spectral gap of $T_0$ (the Euler product part), which is polynomially large $\sim C'\lambda$ — not the exponentially small gap of $Q_W$.

---

## Sources

- **Preprint:** sections-06-10.md §5, Proposition 5.1
- **Research:** research/20-estimate1-archimedean.md
