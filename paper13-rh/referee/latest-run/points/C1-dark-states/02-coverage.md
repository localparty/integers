# C1.02: Coverage

**The concern:** Does this cover ALL eigenstates, including distributional ones?

**Assessment:** The argument as stated covers eigenstates |gamma_n> that are in the Hilbert space H_R. For distributional eigenstates in S', the bridge projector diagonal element may not be well-defined (you cannot compute <phi, Pi phi> for a distribution phi not in H).

However, the paper's proof chain does not need the dark-state argument for distributional eigenstates separately. The argument by contradiction is: IF an off-line zero exists, THEN there is an eigenstate at that zero (by Axiom 1 or Meyer's inclusion), AND that eigenstate couples to the bridges, AND the cocycle shift is non-integer, contradiction. The dark-state argument ensures the coupling is nonzero.

**The real issue:** If the "eigenstate" is distributional (in S' but not H_1), the coupling computation may not apply. The paper implicitly assumes genuine eigenstates in H_1, which requires Axiom 1.

**Verdict: CORRECT within the axiom system.** The coverage extends to all hypothetical eigenstates in the critical strip, provided they are genuine Hilbert space vectors.
