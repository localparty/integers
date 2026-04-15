# Node 04 --- Polymer Convergence

**Chain step:** 3 of 18
**Rigor label:** [LITERATURE]
**Dependencies:** Node 03 (UV stability)
**Status:** ESTABLISHED (Balaban)

---

## Statement

**Balaban, CMP 109, Theorem 1 (detailed: Theorem 3).** At RG step $k$, in the small-field region $\Omega_s$, the effective action admits a convergent polymer expansion:

$$S_k[V] = \frac{1}{g_k^2} S_{\mathrm{YM}}[V] + \sum_{X \in \mathcal{P}_k} K_k(X, V)$$

with polymer activities satisfying $|K_k(X,V)| \leq e^{-\kappa|X|}$ and decay constant $\kappa > 0$ independent of $k$.

---

## Proof sketch

1. **Polymer activities.** Each $K_k(X,V)$ is computed by: background evaluation (polynomial composition), saddle-point via $G_k(V)$ (analytic), Gaussian integration (convergent trace-log), and Mayer resummation (convergent cluster expansion, CMP 109 Sec. 4).

2. **$k$-independent decay.** The controlling parameters ($\kappa$ from CMP 109 Sec. 3, $m_W$ and $C_D$ from CMP 95--96, $r_{\mathrm{proj}}(N)$ from CMP 98 Sec. E) are all $k$-independent by Balaban's inductive hypotheses.

3. **Scalar analogue.** Dimock (arXiv:1108.1335, 2011, Thm 14) provides an explicit statement of the analyticity mechanism in the scalar case; the gauge case follows the same structure.

---

## Sources

- **Literature:** Balaban, CMP 109, Thm 1 and Thm 3; Dimock 2011 (arXiv:1108.1335)
- **Preprint:** Appendix H, Section 3
