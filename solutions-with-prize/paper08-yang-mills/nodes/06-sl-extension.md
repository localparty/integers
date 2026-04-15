# Node 06 --- SL(N,C) Extension (B2)

**Chain step:** 5 of 18
**Rigor label:** [PROVED] (Part II, standard complex analysis)
**Dependencies:** Node 05 (analyticity)
**Status:** PROVED

---

## Statement

**(B2).** The analyticity domain of $S_k[V]$ extends to a neighborhood of $\mathbf{1} \in \mathrm{SL}(N,\mathbb{C})$, with $k$-independent radius.

---

## Proof sketch

1. **Algebraic extension.** Polymer activities $K_k(X,V)$ depend algebraically on $(V_\ell)_{ij}$. On $\mathrm{SU}(N)$, $V^{-1} = V^\dagger = \mathrm{adj}(V)$ (since $\det V = 1$). On $\mathrm{SL}(N,\mathbb{C})$, $\det V = 1$ still holds, so $V^{-1} = \mathrm{adj}(V)$ remains polynomial.

2. **Block-spin kernel.** The projection $A \mapsto A(A^\dagger A)^{-1/2}$ is analytic near $\mathbf{1} \in \mathrm{GL}(N,\mathbb{C})$ via holomorphic functional calculus: $(A^\dagger A)^{1/2}$ is a Cauchy integral over a contour in $\{\mathrm{Re}(z) > 0\}$. For $\|A - \mathbf{1}\| < 1/2$, $\lambda_{\min}(A^\dagger A) \geq 1/4$, giving radius $r_{\mathrm{proj}} = 1/2$ depending only on $N$.

3. **Cauchy estimates.** The bounds $|K_k(X,V)| \leq e^{-\kappa|X|}$ on $\mathrm{SU}(N)$ extend to complex $V$ with $\|V_\ell - \mathbf{1}\|_{\mathrm{HS}} < \rho'$ by Cauchy estimates. The radius $\rho'$ depends on $\rho$ and polynomial degree but not on $k$.

4. **Purpose.** (B1)--(B2) together promote the perturbative identification $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ to a non-perturbative statement (Claim 5.2.1), which feeds the spectral lemma.

---

## Sources

- **Preprint:** Appendix H, Section 3 Step (d); Section 5.2 (Claim 5.2.1)
- **Literature:** Holomorphic functional calculus (standard), CMP 98 Sec. E
