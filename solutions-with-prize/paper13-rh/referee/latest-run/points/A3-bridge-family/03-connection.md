# A3.03: Connection to T_BC

**The critical question:** How do the bridge cocycles interact with the spectral operator? Why does an off-line zero shift the cocycle?

The paper's answer (Section 5): The cocycle c(i,j) = omega_1(u_i u_j u_{i+j mod k}^{-1}) is evaluated using the KMS_1 state. The unitaries u_j are constructed from mu_p^j. An off-line zero at s = 1/2 + delta + i*gamma changes the Hecke eigenvalue norm from p^{-1/2} to p^{-(1/2+delta)}, which changes the p-local partition function, which changes the KMS evaluation, which shifts the cocycle value.

**Assessment:** This connection relies on the Hecke eigenvalue formula mu_p |gamma_n> = p^{-s} |gamma_n>. This formula is the DEFINITION of the Hecke action on the spectral basis. It requires that {|gamma_n>} are genuine eigenstates in some Hilbert space where both T_BC and mu_p act. This brings us back to Axiom 1.

If we grant Axiom 1, the connection is well-motivated: the KMS_1 state evaluates Hecke operator products, and these evaluations depend on the zero locations through the eigenvalue formula. The cocycle shift formula follows from this dependence.

**Verdict: The connection is logically sound WITHIN the axiom system, but depends on Axiom 1 for the existence of the spectral basis.**
