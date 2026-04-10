# Point 1: The Stability of Excitation Number Lemma

**Location:** Section 5.6, Part III.3

**Verdict:** SOUND

**Finding:**

The paper claims that every $\mathcal{C}$-even, gauge-invariant, local operator of engineering dimension 6 on the $d=4$ hypercubic lattice has $\mathrm{dev} \geq 2$ (Boltzmann deviation order, the revised notion replacing the earlier "excitation number"). The classification into four classes (I--IV) is examined sub-point by sub-point.

---

## (a) Exhaustiveness of the classification

**Claim under attack:** The four-class decomposition is exhaustive for dimension-6 operators on the lattice.

**Finding: SOUND.**

The specific concern is whether lattice-discretization artifacts produce dimension-6 operators missed by the continuum counting. The example given is $(\mathrm{Re}\,\mathrm{Tr}\,U_P)^3$.

This operator does NOT contaminate the dimension-6 sector. Expanding in the lattice spacing:

$$(\mathrm{Re}\,\mathrm{Tr}\,U_P)^3 = \left(N - \frac{a^4}{2}\mathrm{Tr}\,F^2 + O(a^6)\right)^3$$

$$= N^3 - \frac{3N^2 a^4}{2}\mathrm{Tr}\,F^2 + \frac{3N a^8}{4}(\mathrm{Tr}\,F^2)^2 + O(a^{12}).$$

The expansion proceeds in powers of $a^4$ (each plaquette contributes dimension 4 in leading order). The terms have engineering dimensions 0, 4, 8, 12, ... but **never 6**. Dimension-6 operators require covariant derivatives acting between different lattice sites, which products of plaquettes at the same vertex do not produce.

More generally, any product of $k$ plaquette variables at the same vertex generates operators of dimension $4k$ (leading) with subleading corrections at dimensions $4k+2, 4k+4, \ldots$, but these subleading terms come from expanding individual plaquettes $U_P = 1 - a^4 F^2/(2N) + O(a^6)$ and involve $O(a^2)$ lattice artifacts within each plaquette -- these are dimension-6 corrections to a single plaquette, i.e., they reduce to the same $\mathrm{Tr}(DF)^2$-type operators already classified.

The exhaustiveness of the dimension-6 operator classification on the hypercubic lattice is standard: it coincides with the Luscher--Weisz operator basis (Luscher--Weisz, CMP 97, 1985). The lattice-specific operators at dimension 6 include $O(4)$-breaking variants (e.g., $\sum_\mu \mathrm{Tr}(D_\mu F_{\mu\nu})^2$ with no sum on $\mu$), but these are still two-derivative operators with $\mathrm{dev} \geq 2$ by the same spectral mechanism.

---

## (b) Ghost fields and gauge fixing

**Claim under attack:** The classification applies to the full effective action, not just the gauge-invariant part.

**Finding: SOUND.**

Balaban uses axial gauge, not the Faddeev--Popov method. In axial gauge, the gauge is completely fixed and **no ghost fields appear**. The fluctuation integration is over physical (gauge-fixed) degrees of freedom only. The resulting effective action $S_k[V]$ is expressed entirely in terms of block link variables $V_\ell$, which are gauge-invariant by construction (CMP 98, Section 2: the block-averaging preserves gauge equivariance).

The gauge-fixing artifacts (the axial gauge condition itself) affect the parameterization of the fluctuation integral but not the form of the output. The effective action at each RG step is a gauge-invariant functional of the block variables. There are no Faddeev--Popov ghosts, no BRST-exact terms, and no gauge-fixing artifacts in $\delta E_k^{d=6}$.

---

## (c) Lattice artifacts: dimension-6 operators from the Wilson action

**Claim under attack:** Wilson action artifacts at $O(a^2)$ could mix with $S_\mathrm{YM}$ through renormalization.

**Finding: SOUND.**

The Wilson action differs from the continuum action by $O(a^2)$ corrections, which are genuine dimension-6 operators. These artifacts are present from the start and propagate through the RG. But they are properly handled:

1. **They are part of $\delta E_k^{d=6}$**, not a separate source of contamination. The coupling renormalization at each step absorbs the unique dimension-4 operator $S_\mathrm{YM}$, and everything else (including lattice artifacts) goes into the remainder.

2. **They cannot mix with $S_\mathrm{YM}$** because $S_\mathrm{YM}$ is the unique dimension-4 gauge-invariant $\mathcal{C}$-even parity-even operator on the lattice (Section 5.6, Part III, [CONFIRMED] item 3). The coupling renormalization extraction is exact by uniqueness.

3. **Their deviation order is $\geq 2$** because they are $\mathcal{C}$-even dimension-6 operators and fall into the same classification (Class III or IV).

---

## (d) The transition from perturbative to non-perturbative

**Claim under attack:** The diagonal vanishing $(e^{E_1 - E_1} - 1)^2 = 0$ is a kinematic identity, not a symmetry, and might be lifted by non-perturbative corrections.

**Finding: SOUND.** This is the most subtle sub-point, and the paper handles it correctly through a structural argument that does not depend on the diagonal vanishing of a specific operator.

The concern conflates two things:

**(i) The diagonal vanishing for a specific operator.** For $\mathrm{Tr}(D_0 F)^2$, the factor $(e^{E_m - E_n} - 1)^2$ evaluated at $n = m$ gives $(e^0 - 1)^2 = 0$. This is indeed a kinematic identity, not a symmetry. But the paper does NOT claim this identity is preserved under non-perturbative deformation of the operator.

**(ii) The deviation order of the non-perturbative operator.** The paper's argument (Section 5.6, Part III.3--III.4) establishes $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ through a completely different route:

- By (B1), $\delta E_k^{d=6}$ has a convergent expansion in gauge-invariant monomials.
- Each monomial is a $\mathcal{C}$-even dimension-6 operator.
- By the classification, each such operator falls into Class III (two derivatives, $\mathrm{dev} \geq 2$) or Class IV (three+ derivatives, $\mathrm{dev} \geq 3$).
- By the linear combination lemma (Section 5.5.3), the convergent sum has $\mathrm{dev} \geq 2$.

The key insight is that **the deviation order is a property of the operator class, not of a specific perturbative identification**. Every $\mathcal{C}$-even dimension-6 gauge-invariant operator has the two-derivative structure that forces $\mathrm{dev} \geq 2$, regardless of whether it is "close" to $\mathrm{Tr}(DF)^2$ or not.

The concern about "the one-particle state itself shifts" is irrelevant: the deviation order is defined in terms of the actual spectral decomposition of the transfer matrix (whatever the eigenstates are), and the spectral mechanism produces the factor $(e^{E_m - E_n} - 1)^2$ from the algebraic structure of the covariant derivative, not from a perturbative identification of states.

---

**Impact on the claimed result:** None. This point is sound.
