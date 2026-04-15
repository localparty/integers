## Point E1(d): Numerical Verification

**The question:**
Section 13.3 claims BSD formula verification to 50 digits. Is numerical verification used as a substitute for proof?

**Finding:**
The preprint is careful to distinguish proof from verification. Section 13.3 states: "This is the simplest instance of Theorem 13.1, and it confirms that the abstract chain -- bridge family -> GRH -> Kolyvagin -> BSD -- produces correct numerical output on the canonical test case."

The numerical verification is presented as evidence supporting the theorem, not as a substitute for the proof. The proof itself is the chain in Sections 3-12. The verification in Section 13.3 is a sanity check.

The numerical values (L(E, 1) = Omega/4, Sha = 1, c_2 = 4, |E_tors| = 4) are all standard and can be verified against LMFDB/Cremona tables.

One concern: the preprint could benefit from numerical verification for a SECOND curve (not just y^2 = x^3 - x). Section 14.2 provides partial data for y^2 = x^3 - 1 but does not give the same level of detail.

**Verdict for this sub-question:**
SOUND -- Numerical verification is used as evidence, not as proof. The distinction is clearly maintained.
