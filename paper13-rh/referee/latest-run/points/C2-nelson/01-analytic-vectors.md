# C2.01: Analytic Vectors

**Claim:** The eigenvectors e_n are entire analytic vectors for T_BC because sum_{k=0}^infty ||T_BC^k e_n||^2 t^{2k}/(2k)! = cosh(gamma_n t) < infty for all real t.

**Assessment:** CORRECT. If T_BC e_n = gamma_n e_n with gamma_n real, then ||T_BC^k e_n|| = |gamma_n|^k, and the series is exactly cosh(gamma_n t), which converges for all t.

**But:** This computation assumes gamma_n is real (so that ||T_BC^k e_n|| = |gamma_n|^k). The reality of gamma_n is the CONCLUSION of Steps 1-6. So the Nelson argument depends on the prior establishment that delta = 0. This is not circularity -- it is sequential logic -- but it means Nelson does not independently force the zeros onto the line.

**Verdict: CORRECT, given that gamma_n is real (from Steps 1-6).**
