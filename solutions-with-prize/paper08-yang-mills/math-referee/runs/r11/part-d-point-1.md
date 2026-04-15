## Part D, Point 1: Exhaustiveness of the Dimension-6 Classification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Lüscher-Weisz basis.**

The Lüscher-Weisz classification (CMP 97, 1985) identifies the continuum dimension-6 operators in the Symanzik effective theory. For pure gauge theory, the off-shell basis consists of three operators: $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$, $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$, and $\mathrm{Tr}(F_{\mu\nu} F^{\nu\rho} F_\rho{}^\mu)$. On-shell (using $D_\mu F^{\mu\nu} = 0$), the second is related to the first, leaving two independent operators.

The lattice-specific analysis (Appendix J, Theorem J.1) extends this to the hypercubic lattice. The key additional concern is whether lattice artifacts — operators present on the lattice but absent in the continuum — could contribute at dimension 6. Theorem J.1 proves that no such operators exist: gauge-invariant, $\mathcal{C}$-even lattice operators of dimension 6 are precisely the discretizations of the continuum operators, plus $\mathrm{O}(4)$-breaking variants that share the two-derivative structure.

The argument is: (i) single-plaquette operators $s_P = \mathrm{Re}\,\mathrm{Tr}(\mathbf{1} - U_P)/N$ have dimension 4; (ii) products $s_P^n$ have dimension $4n \geq 8$; (iii) reaching dimension 6 from dimension-4 building blocks requires exactly one lattice finite difference (covariant derivative); (iv) $\mathcal{C}$-even operators with an odd number of field strengths under the trace are $\mathcal{C}$-odd and eliminated.

This is stated and proved in Appendix J with explicit verification. The classification is exhaustive for the lattice action used (Wilson plaquette action processed by Balaban's block-spin).

**(b) The second two-derivative operator.**

The operator $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ involves the Yang-Mills equation of motion $D_\mu F^{\mu\nu}$. The r05 referee flagged that $\mathrm{dev} \geq 2$ was verified explicitly only for $\mathrm{Tr}(D_0 F)^2$, not for this operator.

The current preprint closes this gap in Section 5.6, Part III.3, item (III). The argument: each factor $D_\mu F^{\mu\rho} = \sum_\mu D_\mu F^{\mu\rho}$ decomposes over Lorentz index. Spatial components ($\mu = j$) give zero connected matrix elements at zero momentum by translation invariance. The temporal component ($\mu = 0$) gives $D_0 F^{0\rho} = \hat{T}^{-1} F^{0\rho} \hat{T} - F^{0\rho}$ with matrix element factor $(e^{E_m - E_n} - 1)$. The product of two such factors gives $(e^{E_m - E_n} - 1)^2$, confirming $\mathrm{dev} \geq 2$ by direct spectral computation.

Additionally, the equation-of-motion relation $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho) = \mathrm{Tr}(D_\rho F_{\mu\nu})^2 + \text{$\mathcal{C}$-odd terms} + \text{dim-8 terms}$ means the $\mathcal{C}$-even part of the second operator equals $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ up to dimension-8 corrections (which have $\mathrm{dev} \geq 4$). Either route establishes $\mathrm{dev} \geq 2$.

**(c) Lattice artifacts at dimension 6.**

The Wilson action contains $O(a^2)$ lattice artifacts. Under Balaban's block-spin, these propagate into the effective action. However, operator mixing between dimension 4 and dimension 6 is forbidden by the uniqueness of $S_{\mathrm{YM}}$ as the sole dimension-4 gauge-invariant operator (PROOF-CHAIN.md, IV.3). The dimension-4 component is exactly absorbed into coupling renormalization. The remainder is genuinely dimension $\geq 6$.

The lattice artifacts (dimension-6 operators breaking $\mathrm{O}(4)$ to the hypercubic group) are included in the classification of Theorem J.1. They share the two-derivative structure of the continuum operators and have $\mathrm{dev} \geq 2$ for the same spectral reason. They vanish in the continuum limit at rate $O(g_k^4 (a_k\Lambda)^2)$.

**Impact on the claimed result:** None. The dimension-6 classification is exhaustive, both operators have $\mathrm{dev} \geq 2$, and lattice artifacts are properly controlled.
