# C2.05: Spectral Completeness

**Claim:** H_R = span{|gamma_n>}, no extra eigenvalues.

**Assessment:** This is Proposition 9.3. The proof: if lambda is an eigenvalue with eigenvector f, expand f = sum <e_n, f> e_n, apply T-bar_BC, compare coefficients, get (lambda - gamma_n)<e_n, f> = 0 for all n. Since f != 0, some <e_{n_0}, f> != 0, hence lambda = gamma_{n_0}.

This proof is CORRECT but TAUTOLOGICAL. If {e_n} is a complete ONB of eigenvectors with eigenvalues {gamma_n}, then OF COURSE there are no other eigenvalues. This is the definition of "complete ONB."

The non-trivial content would be: prove that {e_n} IS a complete ONB WITHOUT assuming Axiom 1. The paper does not do this.

**Verdict: TAUTOLOGICAL.** Correct but content-free -- the conclusion is built into the definitions.
