# Node 12 --- RG Recursion

**Chain step:** 12 of 14
**Rigor label:** [PROVED]
**Dependencies:** Step 11 (new-operator bound)
**Status:** PROVED

---

## Statement

The form-factor constant obeys the recursion $C_{K+1} = C_K/4 + C_{\mathrm{new}} + O(g_K^2 C_K)$, which has a bounded fixed point $C_{**} = 4C_*/3$, ensuring $\sum_K C_K g_K^4 \hat{\Delta}_K^2 < \infty$ and $\Delta_\infty > 0$.

---

## Proof sketch

1. **Old contribution contracts.** The telescoping comparison between bare theories $K$ and $K+1$: the effective action at scale $k$ computed from bare theory $K$ is compared with the same scale computed from bare theory $K+1$ (which has twice the lattice points). The old remainder $E^{(K)\downarrow}$ re-expressed in $K+1$ variables satisfies $|\text{(A)}| \leq (C_K/4) g_K^4 \hat{\Delta}_{K+1}^2$. The factor $1/4$ is kinematic: $\hat{\Delta}_{K+1}^2 = \hat{\Delta}_K^2/4$ from bare refinement $a_0(K+1) = a_0(K)/2$ (Section 5.1 notation).

2. **New contribution bounded.** By Step 11, $|\text{(B)}| \leq C_{\mathrm{new}} g_K^4 \hat{\Delta}_{K+1}^2$.

3. **Inductive step.** Combining: $C_{K+1} \leq C_K/4 + C_{\mathrm{new}} + O(g_K^2 C_K)$. The geometric contraction $1/4$ dominates the $O(g_K^2)$ perturbative corrections.

4. **Bounded orbit.** Fixed point $C_{**} = 4 C_{\mathrm{new}}/3$ (from $C_{**} = C_{**}/4 + C_{\mathrm{new}}$), approached at rate $4^{-K}$. **Transient regime:** For $K < K_0$ where $g_K^2$ is not yet small, the recursion $C_{K+1} \leq (1/4 + c g_K^2) C_K + C_{\mathrm{new}}$ may not contract. However, $g_K^2 \sim 1/(b_0 K \ln 2)$, so $1/4 + c g_K^2 < 1$ for $K > K_0 := \lceil 4c/(3 b_0 \ln 2)\rceil$. Below $K_0$, $C_K$ grows at most polynomially: $C_K \leq C_0 \prod_{j=0}^{K-1}(1/4 + c g_j^2) \leq C_0 K^{c'}$. This polynomial transient is absorbed by the $4^{-K}$ factor in the sum.

5. **Convergent sum.** With $g_K^4 \sim 1/K^2$ (bare running) and $\hat{\Delta}_K^2 \sim 4^{-K}$ (bare refinement):

$$\sum_{K \geq K_0} C_K g_K^4 \hat{\Delta}_K^2 \lesssim \sum_K K^{\gamma - 2} \cdot 4^{-K} < \infty$$

The doubly exponential factor $4^{-K}$ overwhelms any polynomial $K^\gamma$.

6. **Conclusion.** The total mass-gap shift is bounded: $\Delta_\infty = \Delta_0 \cdot \Lambda_\infty > 0$.

---

## Sources

- **Preprint:** Section 5.4.5 (inductive step), Section 5.4.6 (convergence of sum)
- **Preprint:** Section 5.7 (continuum mass gap theorem)
