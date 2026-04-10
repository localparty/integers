## Part D, Point 1: Exhaustiveness of the Dimension-6 Classification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Lüscher-Weisz basis.**

The preprint's classification of dimension-6 operators coincides with the Lüscher-Weisz (1985) operator basis. The standard Symanzik effective theory argument (Symanzik 1983) establishes that lattice operators not present in the continuum are redundant by equations of motion (EOM). Appendix J (Theorem J.1) provides the lattice-specific derivation, which does not merely cite the continuum result but derives the basis directly on the $d = 4$ hypercubic lattice.

The derivation proceeds in four steps:
1. **Zero-derivative operators** (Tr($F^3$), $d^{abc}F^3$): Both $\mathcal{C}$-odd, eliminated exactly by charge conjugation symmetry of the effective action.
2. **One-derivative operators** (dimension 5): Empty in the $\mathcal{C}$-even sector — all odd-power traces are $\mathcal{C}$-odd.
3. **Two-derivative operators** (dimension 6): $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$, plus $\mathrm{O}(4)$-breaking variants sharing the same two-derivative structure.
4. **Three-or-more-derivative operators** (dimension $\geq 7$): Not dimension 6.

This exhaustive classification is established for the specific lattice action used (Wilson plaquette action). The block-spin integration in Balaban's construction does not create new operator structures beyond the Symanzik classification because block-spin integration is a linear operation on gauge-invariant functionals. This point is explicitly stated in Appendix J.

**(b) The second two-derivative operator.**

The operator $\mathcal{O}_{\mathrm{EOM}} = \mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ is related to $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ by the Yang-Mills equations of motion and the Bianchi identity. Section 5.6 Part III.3 provides an explicit spectral verification of $\mathrm{dev}(\mathcal{O}_{\mathrm{EOM}}) \geq 2$:

Using the Bianchi identity $D_{[\mu}F_{\nu\rho]} = 0$ and commutator $[D_\mu, D_\nu] = F_{\mu\nu}$:
$$\mathcal{O}_{\mathrm{EOM}} = \mathrm{Tr}(D_\rho F_{\mu\nu})^2 + \text{terms involving } [F,F] \text{ contractions}$$

The commutator terms $\mathrm{Tr}(F_{\mu\nu}[F^{\mu\rho}, F^\nu{}_\rho])$ involve three $F$-factors with no covariant derivatives. These are $\mathcal{C}$-odd (odd power of $F$) and vanish in the $\mathcal{C}$-invariant effective action. The remaining contribution is $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ plus dimension-8 lattice artifacts.

Additionally, an explicit spectral computation confirms $\mathrm{dev}(\mathcal{O}_{\mathrm{EOM}}) \geq 2$: each factor $\sum_\mu D_\mu F^{\mu\rho}$ decomposes over Lorentz indices. Spatial components vanish at $\vec{p} = 0$ by translation invariance. The temporal component $D_0 F^{0\rho}$ produces a factor $(e^{E_m - E_n} - 1)$ in the transfer matrix. The product of two such factors gives $(e^{E_m - E_n} - 1)^2$, vanishing at $n = m$ (diagonal). This confirms $\mathrm{dev} \geq 2$ by direct spectral computation, independent of the EOM reduction.

The r05 referee flagged this as a CLOSABLE GAP; the current preprint closes it.

**(c) Lattice artifacts at dimension 6.**

The Wilson action contains $O(a^2)$ lattice artifacts. Under Balaban's block-spin integration, these propagate into the effective action. Appendix J addresses this explicitly: the $O(4)$-breaking lattice operators (e.g., $\sum_\mu \mathrm{Tr}(D_\mu F_{\mu\nu})^2$ without sum on the second $\mu$) share the same two-derivative structure as the $O(4)$-invariant operators and therefore carry the same deviation order $\mathrm{dev} \geq 2$.

The key point: there is no dimension-4 contamination from lattice artifacts because $S_{\mathrm{YM}}$ is the unique dimension-4 gauge-invariant, $\mathcal{C}$-even, parity-even operator (PROOF-CHAIN.md IV.3). Operator mixing between dimension 6 and dimension 4 would require a dimension-4 operator other than $S_{\mathrm{YM}}$, which does not exist. The subtraction of $(1/g_k^2)S_{\mathrm{YM}}$ is exact, leaving a remainder that is genuinely dimension $\geq 6$.

**Impact on the claimed result:**

None. The dimension-6 classification is exhaustive, correctly derived for the lattice action, and accounts for all lattice artifacts. The second two-derivative operator has $\mathrm{dev} \geq 2$ by both the EOM reduction and direct spectral computation.
