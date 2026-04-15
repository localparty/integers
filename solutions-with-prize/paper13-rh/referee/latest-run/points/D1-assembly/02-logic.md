# D1.02: The Logical Structure

The proof argues by contradiction: IF an off-line zero existed at s = 1/2 + delta + i*gamma with delta != 0, THEN the bridge cocycles would shift by a non-integer amount, THEN the topological invariant would not be in Z/kZ, contradiction.

**Is this a valid proof by contradiction?**

The logical structure is valid IF:
1. An off-line zero produces a genuine eigenstate in H_R (requires Axiom 1)
2. This eigenstate couples to the bridge projectors (proved for H_R eigenstates)
3. The coupling produces a cocycle shift of exactly Delta_c(delta) (derived from KMS evaluation)
4. The shift must be in (1/k)Z for the cocycle to remain well-defined (NOT PROVED -- see B1.02)
5. The Gelfond-Schneider theorem prevents this for delta != 0 (proved)

The argument is valid modulo assumptions 1 and 4.

**Verdict: VALID in structure, CONDITIONAL in content.**
