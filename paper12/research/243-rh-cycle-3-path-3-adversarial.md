# 243 — RH Cycle 3, Path 3 (Stone) — Adversarial

*Cycle: 3 (LIVE). Date: 2026-04-09. Agent: Adversarial.*

---

## Attacks attempted

### Attack 1: The dark-state closure is tautological.

**Analysis.** The construction argues: H_R = span{|gamma_n>}, so any eigenvector must be some |gamma_m>. This is true by construction — it follows directly from the definition of H_R. It does NOT prove that T_BC on a LARGER space (e.g., Meyer's nuclear space, or the full GNS space of A_BC) has no extra eigenvalues.

The real spectral realisation question is: does T_BC on the FULL representation space have spectrum {gamma_n} and nothing else? The dark-state argument only addresses H_R, which is DEFINED as the span of {|gamma_n>}.

**Result: WEAKENED.** The argument is valid on H_R but tautological — H_R is defined to have basis {|gamma_n>}. The interesting question is about the larger space. The construction should have addressed this.

### Attack 2: Is the conditional chain RH-dependent?

**Analysis.** The chain is: Axiom 1 (H_R exists with basis {|gamma_n>}) => Nelson (T_BC ess. self-adjoint) => Stone (spectrum real) => gamma_n real => RH.

But Axiom 1 ASSUMES gamma_n are the eigenvalues. If gamma_n were complex (off-line zeros), they wouldn't be eigenvalues of a self-adjoint operator. Axiom 1 implicitly assumes RH by restricting to zeros on the critical line.

**Result: WEAKENED.** The argument proves: "If all zeros are on the critical line, then all zeros are on the critical line." The non-trivial content is the self-adjointness step (Path 6), which shows that the assumption is self-consistent.

### Attack 3: Resolvent computation is numerical, not rigorous.

**Analysis.** The resolvent sum_{n=1}^{100} 1/(gamma_n - z) at test points between gamma_1 and gamma_2 shows no poles. But this is a truncation to 100 zeros. A pole at z = lambda_extra in the FULL resolvent (all zeros) could be masked by truncation effects.

**Result: SURVIVED.** The resolvent computation is presented as numerical evidence, not a proof. The dark-state argument provides the proof (on H_R). The resolvent data is supplementary.

## Overall verdict: INTACT (conditional, weakened)

Path 3's result is logically valid but conditional on Axiom 1 in a way that makes it near-tautological. The real content comes from Path 6 (essential self-adjointness) rather than from Path 3 itself. Path 3 should be reclassified as a COMPLETION path that assembles the results of Paths 6 and 5 into a final argument, rather than an independent proof route.
