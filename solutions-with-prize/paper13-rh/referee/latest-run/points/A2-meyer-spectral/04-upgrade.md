# A2.04: The Upgrade from Distributional to Genuine

**The question:** Does {gamma_n} subset spec_dist(T_BC) imply {gamma_n} subset spec(T-bar_BC)?

**Answer: Not automatically.**

The paper's argument in Appendix B.5 claims:
- Meyer gives gamma_n in approx-spec(T_BC|_S)
- Approximate spectrum is preserved under closure
- Therefore gamma_n in spec(T-bar_BC)

But Meyer gives distributional eigenstates in S', not approximate eigenvectors in H_1. These are different:

1. **Distributional eigenstate:** phi in S' with phi(Tf) = gamma_n phi(f) for all f in S.
2. **Approximate eigenvector:** f_k in H_1, ||f_k|| = 1, ||(T - gamma_n)f_k|| -> 0.

The connection requires a regularization argument: approximate the distribution phi by a sequence in H_1. This is possible in many settings (e.g., if S is a nuclear space with appropriate properties), but it requires proof, not assertion.

**Moreover:** Even if gamma_n is in spec(T-bar_BC), this does not mean it is an EIGENVALUE. It could be in the continuous spectrum. The paper's Step 8 (spectral completeness) claims pure point spectrum, but this is proved by assuming H_R has {e_n} as a complete ONB -- which is Axiom 1.

**Verdict: CRITICAL GAP.** The upgrade is the weakest link in the entire proof chain.
