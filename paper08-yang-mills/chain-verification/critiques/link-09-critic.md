# Link 09 Critic Report — Dim-6 Classification: all ops have dev ≥ 2

**Verdict: SURVIVED**

---

## Attack-by-attack findings

### Attack 1 — Completeness of the H(4) classification
Appendix J proceeds from first principles: it enumerates all gauge-invariant building blocks on the hypercubic lattice (plaquettes, products, finite differences), rules out zero-derivative operators by the dimension-counting argument ($n = 3/2$ plaquettes impossible), rules out one-derivative operators by C-parity, and identifies the two-derivative class as the only survivor. The enumeration explicitly covers O(4)-breaking contractions (§J.3 Step 5) as a *separate subcase*, not a gap. **No independent operator is missing.**

### Attack 2 — Lattice Laplacian / discrete derivatives
The lattice Laplacian $\nabla_\mu \nabla_\mu s_P$ is a specific instance of the two-derivative structure $\nabla_\rho \nabla_\sigma s_P$ with $\rho = \sigma$. Appendix J Step 3 handles the full tensor $\nabla_\rho \nabla_\sigma s_P$ (both off-diagonal and diagonal), so the Laplacian is a special case within the classified basis. No operator involving the lattice Laplacian escapes the classification. **Attack fails.**

### Attack 3 — EOM-redundant operators and block-spin kernel dependence
Section 5.6 Part III.3 does *not* invoke the claim that EOM operators are "not generated." Instead it gives an independent spectral argument: the second operator $\mathcal{O}_{\mathrm{EOM}} = \mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ is verified to have dev ≥ 2 directly via transfer-matrix computation (§III.3 bullet 3, explicit spectral verification). The field-redefinition / EOM equivalence is mentioned only as supplementary motivation; the bound does not depend on it. The EOM commutator terms are C-odd and drop out exactly. **No kernel-dependence vulnerability.**

### Attack 4 — Ghost / auxiliary fields in the effective action
The paper works in the pure-glue lattice Wilson action, where Balaban's block-spin RG integrates only over link variables $U_\ell \in \mathrm{SU}(N)$. There are no ghost or auxiliary fields in the effective action $S_k[V]$ (these appear only in the BRST gauge-fixed continuum formulation, which is not the setting here). The classification in §5.3 and Appendix J is explicitly for gauge-invariant operators in link variables; the absence of ghosts is not an oversight but a consequence of the lattice framework. **Attack inapplicable.**

### Attack 5 — Counterexample: $\mathrm{Tr}(F^2)^2$ index contractions
$\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})^2$ has engineering dimension 8, not 6 (each $F$ is dimension 2, four factors = dimension 8). Appendix J Step 1 explicitly records $(\mathrm{Re}\,\mathrm{Tr}\,U_P)^2 \sim \mathrm{Tr}(F^2)^2$ as dimension 8. No Fierz-type identity reduces this to dimension 6. Different index contractions (e.g., $\mathrm{Tr}(F_{\mu\nu}F^{\nu\rho}F_{\rho\sigma}F^{\sigma\mu})$) are likewise dimension 8. **No dim-6 counterexample exists here.**

### Attack 6 — Single operator with dev = 1 overlooked
For dev = 1 to occur one would need a gauge-invariant, C-even, dim-6 operator whose spectral weight contains exactly one factor of $(e^{E_m - E_n} - 1)$. The only candidates are (i) zero-derivative: eliminated by C-parity; (ii) one-derivative: absent in C-even sector; (iii) two-derivative: both surviving operators produce the factor $(e^{E_m-E_n}-1)^2$ (two derivative insertions, each bringing one factor), giving dev ≥ 2, not 1. The spatial-derivative components contribute zero by translation invariance, so no operator in class (iii) can reduce to a single $(e^{E_m-E_n}-1)$ factor. **No dev = 1 operator exists.**

---

## Summary (≤150 words)

All six attack vectors fail. Appendix J's enumeration is exhaustive: the dimension-counting argument (no half-integer plaquette products) eliminates zero-derivative candidates; C-parity kills the remaining cubic operators exactly; the lattice Laplacian is a special case of the two-derivative tensor already classified; O(4)-breaking operators are explicitly covered as a subcase in §J.3 Step 5; no ghost or auxiliary fields appear in Balaban's pure-glue framework; and $\mathrm{Tr}(F^2)^2$ is dimension 8, not 6. The dev = 1 gap is structurally closed: two-derivative operators bring $(e^{E_m-E_n}-1)^2$ in the spectral weight, forcing dev ≥ 2. The EOM operator receives an independent spectral verification, removing any block-spin kernel dependence. Link 9 is sound.

**SURVIVED**
