## Part D, Point 1: Exhaustiveness of the Dimension-6 Classification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: every C-even, gauge-invariant, local operator of engineering dimension 6 on the d = 4 hypercubic lattice falls into one of four classes, all with dev >= 2.

**(a) The Luscher-Weisz basis.** The classification in Appendix J (Theorem J.1) establishes the complete lattice operator basis at dimension 6. The argument proceeds by exhaustive enumeration:

**Step 1 (Zero-derivative, dim-6):** The operators Tr(F^3) and d^{abc} F^3 are C-odd (under C: F -> -F^T, so Tr(F^3) -> -Tr(F^3)). They are eliminated exactly from the C-invariant effective action.

**Step 2 (One-derivative, dim-5):** All gauge-invariant operators with one derivative and odd powers of F are C-odd.

**Step 3 (Two-derivative, dim-6):** The surviving operators are Tr(D_rho F_{mu nu})^2 and related contractions. These have dev >= 2 by the two-derivative structure.

**Step 4 (Three-or-more derivatives):** These produce dimension >= 7, not dimension 6.

**Step 5 (Lattice-specific operators):** O(4)-breaking contractions (e.g., Sum_mu Tr(D_mu F_{mu nu})^2 without the O(4)-covariant sum) share the two-derivative structure and have dev >= 2. These vanish in the continuum limit but contribute at finite lattice spacing.

The argument that lattice operators beyond the continuum Symanzik basis are redundant by equations of motion is stated and justified in Appendix J, Step 6. The key point: on the lattice, additional operators can arise from the lattice discretization, but they either (i) reduce to the continuum operators plus higher-dimension corrections, or (ii) vanish by the lattice equations of motion. The Symanzik (1983) argument is applied explicitly to the Wilson action.

This coincidence with the continuum Luscher-Weisz basis is expected (the Symanzik effective theory predicts it) and is confirmed by the explicit lattice enumeration.

**(b) The second two-derivative operator.** The operator Tr(D_mu F^{mu rho} D_nu F^nu_rho) is related to Tr(D_rho F_{mu nu})^2 by equations of motion. The preprint handles this in Section 5.6, Part III.3:

  O_EOM = Tr(D_rho F_{mu nu})^2 + commutator terms

The commutator terms involve [F, F] contractions, which are C-odd and vanish in the effective action. The remaining contribution has the two-derivative structure and hence dev >= 2.

The r05 referee flagged that dev >= 2 was verified explicitly only for Tr(D_0 F)^2, not for the second operator. The current preprint addresses this by showing that the EOM-related operator reduces to Tr(D_rho F)^2 modulo C-odd terms. This closure is adequate.

**(c) Lattice artifacts at dimension 6.** The Wilson action has O(a^2) lattice artifacts. Through the block-spin integration, these generate dimension-6 operators in the effective action. The question is whether they could contribute a dimension-4 component through operator mixing.

The answer is no: the uniqueness of S_YM as the dimension-4 gauge-invariant operator (established in PROOF-CHAIN IV.3) means that any dimension-4 contribution is already absorbed into the coupling renormalization g_k -> g_{k+1}. The extraction is exact (not approximate): since S_YM is the UNIQUE dim-4 operator, subtracting (1/g_k^2) S_YM from S_k leaves a remainder that is purely dimension >= 6. No mixing occurs.

No error found. The classification is exhaustive, the EOM reduction is handled, and the lattice artifacts are properly accounted for.

**Impact on the claimed result:** None. The dimension-6 classification is a rigorous combinatorial/algebraic result.
