# Link 6 Critic Verdict: C-Elimination of Tr(F³)

**Result: SURVIVED — with one annotated weakness**

---

## Attack-by-Attack Assessment

### AV1: Is C a lattice symmetry of the Balaban block-spin action?
**Does not break the link.** The paper asserts (§5.3.1, lines 503–506) that "the Yang-Mills action and the block-spin averaging both respect charge conjugation." The C-action is defined on link variables as U_ℓ → U_ℓ* (complex conjugation), which is a manifest symmetry of the Wilson plaquette action (Re Tr U_P is real and symmetric under complex conjugation) and of any block-spin averaging kernel built from Re Tr of products of links. No derivation or citation is given for the kernel's C-invariance, but the claim is structurally sound: Balaban's block-spin map averages U_ℓ → (coarse link) using a heat-kernel-type measure that depends only on |U_ℓ|-type real quantities invariant under U → U*.

**Annotated weakness:** The assertion "block-spin averaging respects C" is stated without proof or Balaban citation. A referee could demand a one-line argument or pointer to Balaban CMP 109 §2 where the averaging kernel is defined.

### AV2: Tr(F³) vs Tr(F̃ F F) — are ALL cubic operators eliminated?
**Does not break the link.** The paper explicitly treats both zero-derivative cubic operators: O₂ = Tr(F_μν F^νρ F_ρ^μ) and O₃ = d^{abc} F^a F^b F^c (§5.3.1, lines 397–501; Appendix J, Step 1). The operator Tr(F̃ F F) with Hodge dual is parity-odd (F̃_μν = ½ε_μνρσ F^ρσ flips parity), so it is excluded by the separate parity-even constraint invoked throughout (Appendix J header, Theorem J.1). The argument covers the complete zero-derivative dimension-6 basis.

### AV3: SU(2) triviality — is "exact elimination" vacuous for N=2?
**Does not break the link; correctly noted.** The paper explicitly acknowledges (lines 459–462, 501): for SU(2), Tr(F³) and d^{abc}F³ vanish identically because d^{abc} = 0. The "elimination" for N=2 is vacuous — the operators do not exist — but the paper is transparent about this and the non-trivial statement is made only for N ≥ 3. The link is not broken; the scope is correctly restricted.

### AV4: Is C-invariance preserved under the Balaban RG step?
**Does not break the link.** The argument does not need C-invariance of each intermediate RG kernel step-by-step; it needs only that the *accumulated* effective action S_{k+1}[V] is C-invariant. Since (a) S_YM is C-invariant, (b) the block-spin integration measure is C-invariant (by the same structural argument as AV1), and (c) C is a global symmetry not broken by any local lattice regulator, S_{k+1} inherits C-invariance exactly. The concern about higher-dimensional terms in the kernel breaking C does not arise: C is a Z₂ internal symmetry of the lattice action, not an approximate continuum symmetry, so it cannot be "broken at finite lattice spacing" in the way chiral symmetry can.

### AV5: Does "exact" include non-perturbative instanton contributions?
**Does not break the link.** The elimination is not a statement about the coefficient of Tr(F³) being small — it is a statement that C-odd operators have *exactly zero* matrix elements in C-even states, by the selection rule ⟨C-even | C-odd | C-even⟩ = 0. This is an exact algebraic consequence of C-symmetry and holds non-perturbatively, including for instanton backgrounds, provided the vacuum and mass-gap state are C-even. Instantons do not contribute to C-odd expectation values because instantons come in ±Q pairs and the vacuum is C-symmetric (no θ-term is included in the real Euclidean action). The paper states this explicitly (lines 471–472): "This is exact and non-perturbative: C-odd operators have vanishing diagonal matrix elements in C-even states."

---

## Summary (≤150 words)

Link 6 SURVIVED all five attacks. The C-odd character of both O₂ = Tr(F³) and O₃ = d^{abc}F³ is correctly derived from U_ℓ → U_ℓ* on the lattice. The block-spin action inherits C-invariance structurally (C is an exact Z₂ lattice symmetry, not an approximate continuum one). The Tr(F̃FF) operator is independently excluded by parity. The SU(2) case is acknowledged as trivially vanishing (d^{abc}=0); the non-trivial claim applies only to N≥3. The "exact" qualifier is correct: it is an algebraic selection rule, not a perturbative statement, so instantons do not generate C-odd contributions in a C-symmetric vacuum. One annotated weakness: the claim "block-spin averaging respects C" is asserted without a citation or one-line proof — a reviewer could request a pointer to Balaban CMP 109 §2 for completeness, but this does not constitute a gap that breaks the link.

**Verdict: SURVIVED**
