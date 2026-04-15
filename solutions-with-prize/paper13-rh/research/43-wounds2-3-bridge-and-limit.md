# Research 43 -- Fixing Wounds 2 and 3

*Date: 2026-04-09*
*Depends on: Research 41 (adversarial review), Research 16 (CCM analysis)*

---

## Wound 2 (Step 12): Discrete matrix B vs CCM's continuous operators

**The identification.** B is the Galerkin matrix of CCM's quadratic
form QW_lambda restricted to {delta(x - x_i) : i = 1,...,N} on the
Chebyshev nodes: B_{ij} = QW_lambda(delta_i, delta_j). CCM
(arXiv:2511.22755) builds QW_lambda from the Weil explicit formula;
our B IS that formula evaluated on the grid. The objects live in
different spaces (R^N vs L^2([lambda^{-1}, lambda])) but are related
by standard Galerkin projection.

**Spectral convergence.** Textbook spectral-method theory: Galerkin
eigenvalues converge to continuous eigenvalues as N -> inf. For
Chebyshev grids and smooth kernels, convergence is exponential:
|beta_k^{(N)} - beta_k^{(cont)}| <= C e^{-alpha N}, alpha > 0
determined by the kernel's analyticity strip width.

**Combining with CCM.** Theorem 5.10 proves spectral convergence of
the continuous operators as the number of primes grows. Steps 1-10
prove simplicity of the discrete matrices. The combination:
simplicity (discrete) + spectral convergence = simplicity of the
continuous limit, provided the gap exceeds the discretization error.

**Rate comparison (critical).** Gap: ~10^{-1.7N}. Chebyshev error:
~e^{-alpha N}. Bridge works when alpha > 1.7 ln 10 = 3.91. For the
Weil kernel (analytic on a strip of half-width d): alpha ~ pi d / L.
If alpha < 3.91 the gap decays faster than the error -- but for any
fixed gap at N_0, increasing N beyond N_0 drives the error below the
gap. Fix: choose N = N(K) adaptively. This avoids the rate comparison
entirely at the cost of a more involved (but standard) argument.

**Feasibility: 7/10.** The Galerkin identification is standard and
verifiable. Spectral convergence is textbook (Trefethen; Canuto et
al.). The rate comparison needs an explicit alpha for the Weil kernel
(analyticity strip estimate), which is feasible but requires
calculation. The adaptive N(K) fallback is always available.

---

## Wound 3 (Step 10): Strict interlacing might not survive K -> inf

**The concern.** beta_k(K) != mu_j(K) for all finite K does not
imply the limits differ. Gaps can close.

**Fix via Wound 1 resolution.** The uniform Levin bound (Wound 1
fix): for K > K_0(N), Cartwright guarantees SPO automatically. The
induction terminates at finite K_0(N); beyond it, all primes are
handled without induction. The limit structure is then N -> inf at
fixed K_0(N), with the tail handled by Cartwright -- a standard
"finite verification + asymptotic theorem" form (cf. Platt-Trudgian
GRH verification up to T_0, then zero-free region for T > T_0).

**Discrete vs continuous gaps.** The ~10^{-1.7N} decay is a discrete
artifact. CCM's 10^{-55} precision for the first several hundred
zeros suggests the continuous gaps are much better behaved. The
shrinkage is from finite-dimensional projection, not intrinsic.

**The structural point.** We never take K -> inf directly:
  (1) Fix N. Induction runs up to K_0(N) (finite, explicit).
  (2) Cartwright handles K > K_0(N): SPO is free.
  (3) Interlacing for ALL K, but only K_0(N) steps by induction.
  (4) Take N -> inf. Wound 2 bridge transfers simplicity to the
      continuous operator.
The K -> inf limit is bypassed by Cartwright at step (2).

**Feasibility: 6/10.** Logically clean but depends on Wounds 1 + 2
being closed. Main risk: K_0(N) growing too fast with N, making
finite verification impractical. Estimating K_0(N) requires the same
explicit Levin constants needed for Wound 1.

---

## Summary

| Wound | Fix strategy | Feasibility |
|:------|:-------------|:------------|
| 2 (bridge) | Galerkin identification + Chebyshev spectral convergence | 7/10 |
| 3 (limit)  | Cartwright termination + Galerkin N -> inf | 6/10 |

Wound 3 reduces to Wounds 1 + 2. If those close, Wound 3 is free.
