# Node 8 --- Deviation Bound for Tr(DF)^2

**Chain step:** 8 of 14
**Rigor label:** [PROVED]
**Dependencies:** Step 7 (Newton decomposition)
**Status:** PROVED

---

## Statement

The operator $\mathrm{Tr}(D_0 F_{\mu\nu})^2$ has Boltzmann deviation order $\mathrm{dev} \geq 2$.

---

## Proof sketch

1. **Spectral representation.** Writing $(D_0 F)(0) = \hat{T}^{-1}F(0)\hat{T} - F(0)$ and inserting a complete set:

$$\langle m|(D_0 F)^2|m\rangle = \sum_n (e^{E_m - E_n} - 1)^2 \, |\langle m|F|n\rangle|^2$$

2. **Structural zero at diagonal.** The factor $(e^{E_m - E_n} - 1)^2$ vanishes identically at $n = m$. This is a structural zero (the deviation factor is exactly zero), not a numerical cancellation.

3. **Two powers of $\hat{\Delta}$.** For $m=1$, the dominant off-diagonal channel $n=0$ contributes $(e^{\hat{\Delta}} - 1)^2 = \hat{\Delta}^2(1 + O(\hat{\Delta}))$. The squared structure arises because the operator is a square of first-order temporal differences.

4. **Deviation order.** The weight $W^{(m)}(n) \cdot e^{-E_n}$ admits factoring out two powers of $(e^{E_m - E_n} - 1)$ with bounded residual, confirming $\mathrm{dev}(\mathrm{Tr}(D_0 F)^2) \geq 2$.

---

## Sources

- **Preprint:** Section 5.5.4 (explicit spectral verification)
- **Definition:** Section 5.5.2 (Boltzmann deviation order)
