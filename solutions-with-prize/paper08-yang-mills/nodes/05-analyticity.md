# Node 05 --- Analyticity (B1)

**Chain step:** 4 of 18
**Rigor label:** [PROVED] (Part I, extraction from CMP 95--109)
**Dependencies:** Node 03 (UV stability), Node 04 (polymer convergence)
**Status:** PROVED

---

## Statement

**(B1).** The small-field effective action $S_k[V]$ is analytic in the block link variables $V_\ell$, with $k$-independent radius of analyticity $\rho > 0$.

---

## Proof sketch

1. **Propagator analyticity.** $G_k(V) = (-D^2[V] + m_W^2)^{-1}$ is analytic in $V$ because $D^2[V]$ depends polynomially on $V_\ell$ and the inverse is analytic wherever $S_k^{(2)}$ is invertible (CMP 95--96).

2. **Activity analyticity.** Each polymer activity $K_k(X,V)$ is a composition of four analytic operations: polynomial background evaluation (radius $\infty$), analytic saddle-point via $G_k(V)$ (radius $\geq r_G$ from invertibility of $S_k^{(2)}$), Gaussian integration (convergent trace-log, radius $\geq r_{\text{tl}}$ from cluster expansion), and Mayer resummation (Weierstrass on convergent cluster expansion, radius $\geq r_M$ from $\kappa$ bound). **Domain tracking:** The image of each operation at radius $r_n$ lies within the domain of the next operation at radius $r_{n+1}$: the saddle-point output $\|G_k(V) - G_k(V_0)\| \leq C\|V - V_0\|$ contracts, and the trace-log input is bounded by $\|K_k\| \leq e^{-\kappa|X|}$ (polymer decay). The composition radius is $\geq \min(r_G, r_{\text{tl}}, r_M) > 0$, with each factor $k$-independent.

3. **$k$-independent radius.** The radius is determined by: (i) invertibility of $S_k^{(2)}[V]$ (controlled by $m_W^2 \sim 1/a_k^2$, $k$-independent condition); (ii) Mayer expansion convergence (controlled by $\kappa$, $k$-independent); (iii) averaging kernel radius (fixed by geometry). The minimum $\rho > 0$ is independent of $k$.

4. **Convergent series.** By (B1), $\delta E_k^{d=6}$ has a convergent (not merely asymptotic) perturbative expansion with controlled remainder $\|R_{N+1}\| \leq C^{N+1} g_k^{2(N+1)}$.

---

## Sources

- **Preprint:** Appendix H, Sections 2--3 (extraction and verification)
- **Literature:** Balaban, CMP 95--96, 98, 109; Dimock 2013
