# Node 03 --- UV Stability

**Chain step:** 2 of 18
**Rigor label:** [LITERATURE]
**Dependencies:** None (independent input)
**Status:** ESTABLISHED (Balaban)

---

## Statement

The small-field/large-field decomposition of the lattice gauge theory functional integral is UV-stable: at each RG step $k$, the effective action in the small-field region $\Omega_s$ (where $|F_{\mu\nu}| < p(g_k) = g_k^{1-\epsilon}$) admits a well-defined polymer expansion with controlled remainders, uniformly in the UV cutoff.

---

## Proof sketch

1. **Small-field region.** Balaban decomposes configurations into small-field ($|F| < g_k^{1-\epsilon}$) and large-field ($|F| \geq g_k^{1-\epsilon}$) regions. Large-field contributions are suppressed by $e^{-c/g_k^2}$.

2. **Propagator control.** The fluctuation propagator $G_k(V) = (-D^2[V] + m_W^2)^{-1}$ satisfies $\|G_k\| \leq C/m_W^2$ with exponential decay $|G_k(x,y)| \leq Ce^{-m_W|x-y|}$ (CMP 95, Prop. 1.2).

3. **$d=3$ completion.** CMP 102 (1985) establishes the full program in $d=3$.

4. **$d=4$ extension.** CMP 119 (1988) extends the convergent polymer expansion to $d=4$: effective actions at each step have exponentially decaying activities, uniformly in $k$.

---

## Sources

- **Literature:** Balaban, CMP 102 (1985), CMP 109 (1987), CMP 119 (1988)
- **Preprint:** Appendix H, Section 2.1--2.4
