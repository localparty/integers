# BG4 — Bögli spectral exactness applied

**Claim:** Bögli's theorem gives spec(D_∞) = lim spec(D_N).

**Pass criterion:** Theorem applied correctly; self-adjoint specialization used; varying Hilbert space case handled.

**Finding:**
- Bögli 2017 is a result for closed operators on **a single**
  Hilbert space H. Paper 13's operators D_N live on **different**
  Hilbert spaces E_N^+ (growing dimension).
- The extension to varying Hilbert spaces (via Galerkin
  embeddings P_N) is standard in principle but is **not
  explicitly verified** against Bögli's paper.
- The self-adjoint specialization is standard; Bögli's full
  theorem is non-self-adjoint.
- "gsrc" vs ordinary "strong resolvent convergence": Bögli's
  H1 is ordinary srg (at least as paraphrased in Paper 13
  Appendix D.2); Teschl gives gsrc. Whether gsrc suffices for
  Bögli's H1 is not checked.

**Status:** CONDITIONALLY PASS — Bögli's theorem applies to the
setup in principle, but the specific version (gsrc + varying
Hilbert spaces) is not cited precisely.

**Confidence:** 7/10.
