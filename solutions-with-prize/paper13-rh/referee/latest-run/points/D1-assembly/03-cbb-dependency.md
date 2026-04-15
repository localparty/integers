# D1.03: CBB Dependency

The paper claims (Section 10.4) that the proof is "FROM the CBB axioms" and that Axiom 1 is "proved, not assumed" (Steps 1-6 derive it).

**Assessment:** This is the paper's most problematic claim. Let me trace the logic carefully:

Steps 1-6 allegedly prove that all zeros are on the critical line. But what do Steps 1-6 assume?

- Step 1 assumes Axiom 4 (bridge family exists with the stated properties)
- Step 2 uses published results (KMS uniqueness) -- no CBB axiom needed
- Step 3 uses the Hecke eigenvalue formula mu_p |gamma_n> = p^{-s} |gamma_n>. This requires that {|gamma_n>} are eigenstates in some Hilbert space. This is Axiom 1.
- Step 4 uses Gelfond-Schneider -- no axiom needed, but relies on Step 3
- Step 5 uses the bridge projector formula -- requires Axiom 1 (for the eigenstates)

So Steps 1-6 use Axiom 1 (through the existence of eigenstates) and Axiom 4 (bridge family). The claim that Axiom 1 is "derived" is circular: Steps 1-6 use the eigenstates from Axiom 1 to prove a property of the eigenstates.

The non-circular reading: Steps 1-6 prove that IF eigenstates exist (in any Hilbert space), THEN they must have real eigenvalues. This is a valid conditional statement. Axiom 1 then provides the existence.

**Verdict: The proof is CONDITIONAL on Axiom 1 and Axiom 4.** The paper's claim that it is unconditional (revised version) is not supported.
