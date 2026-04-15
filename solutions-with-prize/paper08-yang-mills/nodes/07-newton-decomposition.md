# Node 7 --- Newton Decomposition

**Chain step:** 7 of 14
**Rigor label:** [PROVED]
**Dependencies:** Step 6 (C-elimination of Tr(F^3))
**Status:** PROVED

---

## Statement

After C-elimination removes all zero-derivative dimension-6 operators (Step 6), the surviving dimension-6 operators in the effective action are two-derivative operators of the form $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$. In the Newton (Lorentz) decomposition over $\rho = 0,1,2,3$, only the $n \geq 2$ deviation terms survive in the connected one-particle matrix element.

---

## Proof sketch

1. **Lorentz decomposition.** $\mathrm{Tr}(D_\rho F_{\mu\nu})^2 = \mathrm{Tr}(D_0 F)^2 + \sum_{j=1}^{3} \mathrm{Tr}(D_j F)^2$.

2. **Spatial derivatives vanish.** For $\rho = j \in \{1,2,3\}$, translation invariance of the zero-momentum one-particle state $|1\rangle$ gives $\langle 1|\mathrm{Tr}(D_j F)^2(0)|1\rangle_c = 0$. The lattice finite difference $\nabla_j \mathcal{M}(0) = \mathcal{M}(\hat{j}) - \mathcal{M}(0)$ has zero connected matrix element because $\langle 1|\mathcal{M}(\vec{x})|1\rangle_c$ is $\vec{x}$-independent at $\vec{p}=0$.

3. **Temporal derivatives survive.** Only $\rho = 0$ contributes. In the transfer-matrix representation, $D_0 F(0) = \hat{T}^{-1}F\hat{T} - F$, producing intermediate-state weights $(e^{E_m - E_n} - 1)$. The $n = m$ (diagonal) channel gives zero; only $n \neq m$ channels survive, i.e., deviation order $n \geq 2$ in the squared operator.

---

## Sources

- **Preprint:** Section 5.3.2 (spatial derivative vanishing, temporal derivative mechanism)
- **Literature:** Transfer matrix formalism; translation invariance at zero momentum
