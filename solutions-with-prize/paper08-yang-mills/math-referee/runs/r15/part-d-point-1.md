## Part D, Point 1: Exhaustiveness of the Dimension-6 Classification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim under scrutiny: every C-even, gauge-invariant, local operator of engineering dimension 6 on the d=4 hypercubic lattice falls into one of four classes (I-IV), all with dev >= 2. This is formalized in Section 5.6 Part III.3 and given a self-contained lattice derivation in Appendix J (Theorem J.1).

**(a) Lattice-specific derivation vs. continuum citation.**

The r05 referee flagged that the preprint "implicitly uses the continuum classification" and called this "a presentation gap, not a mathematical gap." The current preprint has closed this gap. Appendix J provides a lattice-specific derivation that does NOT merely cite Luscher-Weisz or Symanzik. The argument proceeds from first principles:

- Step 1 identifies zero-derivative dimension-6 candidates as Tr(F^3) and d^{abc}F^3, eliminates both by C-oddness.
- Step 2 eliminates one-derivative (dimension-5) operators by C-parity.
- Step 3 constructs two-derivative operators directly from lattice building blocks (lattice finite differences of s_P), arriving at two independent structures.
- Step 5 addresses the critical question of lattice-specific operators explicitly: "Operators that exist on the lattice but not in the continuum --- for example, O(4)-breaking contractions such as sum_mu Tr(D_mu F_{mu nu})^2 with no sum over the repeated mu index --- are included in the Symanzik classification as separate operators. However, they share the same two-derivative structure as the O(4)-invariant operators and therefore carry the same deviation order (dev >= 2)."
- Step 6 handles redundant operators (equations of motion) following Luscher-Weisz Section 3.

The key insight of Step 5 is correct: O(4)-breaking lattice artifacts at dimension 6 necessarily involve two lattice derivatives of a dimension-4 building block (because dimension 6 cannot be reached from products of plaquettes at a single vertex, as explained in J.2). Since all two-derivative structures produce dev >= 2 by the spectral mechanism, the O(4)-breaking variants are automatically covered.

The argument in Appendix J is self-contained and correct. The statement in Theorem J.1 that the classification "coincides with the continuum Luscher-Weisz basis up to O(4)-breaking terms that share the same derivative structure" is the right characterization.

**(b) The second two-derivative operator O_EOM = Tr(D_mu F^{mu rho} D_nu F^nu_rho).**

The r05 referee identified that dev >= 2 was verified explicitly only for Tr(D_0 F)^2, not for O_EOM. The current preprint has addressed this directly in Section 5.6 Part III.3, item (III), with a two-pronged argument:

First, the equations-of-motion reduction: O_EOM = Tr(D_rho F_{mu nu})^2 + commutator terms. The commutator terms Tr(F_{mu nu}[F^{mu rho}, F^nu_rho]) are C-odd (three factors of F under F -> -F^T) and have zero coefficient. The remainder differs from Tr(D_rho F)^2 by dimension-8 terms (dev >= 4).

Second, and importantly, an independent explicit spectral verification: O_EOM is decomposed over Lorentz indices, spatial components vanish at zero momentum by translation invariance, and the temporal component produces (e^{E_m - E_n} - 1)^2 from the two D insertions. This confirms dev(O_EOM) >= 2 by direct spectral computation, independent of the equations-of-motion reduction.

This closes the gap identified by r05 completely and with adequate rigor.

**(c) Operator mixing: dimension-4 contamination from lattice artifacts.**

The Wilson action O(a^2) artifacts propagate through the block-spin integration. The question is whether they can produce a dimension-4 component through operator mixing, contaminating the dimension-6 remainder.

The preprint's argument (Section 5.6 Part III, [CONFIRMED] item on dimension-6 projection; PROOF-CHAIN.md IV.3) rests on the uniqueness of S_YM as the sole dimension-4, C-even, parity-even, gauge-invariant operator. The coupling renormalization g_{k+1} is defined as the coefficient of S_YM (Balaban CMP 109, Sec. 2), and the remainder is everything else. Since S_YM is unique at dimension 4, the subtraction is exact: there is no dimension-4 operator for the artifacts to "mix into" other than S_YM itself, which is already absorbed.

The argument is: s_P^2 has dimension 8, Tr(F tilde{F}) is parity-odd and absent, and no other dimension-4 gauge-invariant local operator exists on the hypercubic lattice. The O(a^2) artifacts of the Wilson action contribute to dimension 6 and higher in the remainder, where the classification applies. This is correct.

One technical point deserves mention: the "dimension-6 projection" requires that the Taylor expansion of the effective action in powers of a converges (otherwise "dimension-6 part" is only asymptotic). This is guaranteed by (B1) -- the analyticity with k-independent radius ensures the Taylor expansion converges in a fixed neighborhood. The preprint states this explicitly in Section 5.6, Part III.4: "Without (B1), the 'dimension-6 part' of the effective action might be only an asymptotic concept." With (B1), the projection is exact.

**Impact on the claimed result:**

No impact. The classification is exhaustive, the lattice-specific derivation is provided, all basis operators have dev >= 2, and the dimension-4/dimension-6 separation is exact. This point is sound.
