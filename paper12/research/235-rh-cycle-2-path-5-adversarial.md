# 235 — RH Cycle 2, Path 5 (CM-trace) — Adversarial

*Cycle: 2. Date: 2026-04-09. Agent: Adversarial.*

---

## Attacks attempted

### Attack 1: Is the KMS =/=> Weil conclusion correct?

The construction agent argues that KMS reflection positivity does
NOT directly imply Weil positivity because KMS constrains the
Laplace transform while Weil constrains a quadratic form in
Fourier space.

**Check:** This is correct. The KMS condition is a one-point
condition on the analytic continuation of the two-point function:

    omega_1(a* sigma_{i/2}(a)) >= 0

This constrains sum_n rho_n * exp(-gamma_n/2), a weighted sum.
Weil positivity requires the MATRIX {W(gamma_m, gamma_n)}_{m,n}
to be positive semi-definite, which is a much stronger condition
(infinitely many constraints vs. one).

The construction agent's analysis is honest and correct. The
KMS => Weil direction fails.

**Result: SURVIVED.** The construction agent's honest negative is
confirmed.

### Attack 2: Is the Li criterion sub-path (c) viable?

The construction agent proposes using Li's criterion as an
alternative: RH iff lambda_n >= 0 for all n, where
lambda_n = sum_rho [1 - (1 - 1/rho)^n].

**Assessment:** Li coefficients can be expressed as:
    lambda_n = sum_rho [1 - (1 - 1/rho)^n]
             = n * (some integral involving zeta'/zeta)

In the BC framework, the distributional trace gives:
    lambda_n^{BC} = Tr(P_n(T_BC))
where P_n is a specific polynomial.

**Problem:** The distributional nature of T_BC means Tr(P_n(T_BC))
must be interpreted as a distributional trace, which requires
regularisation. The regularised trace IS the explicit formula,
which brings us back to computing the Li coefficients from the
explicit formula — and this is exactly what Li (1997) did
WITHOUT the BC algebra. The BC algebra adds no computational
advantage here.

**More specifically:** Li's criterion is EQUIVALENT to Weil
positivity (Li proved this). So if KMS does not imply Weil
positivity (as the construction agent showed), then KMS does
not imply Li's criterion either.

**Result: WEAKENED.** Sub-path (c) is not an independent route.
Li's criterion is equivalent to Weil positivity, so the same gap
(off-diagonal matrix elements) appears. The BC algebra provides
no shortcut.

### Attack 3: Is there any remaining viable sub-path for Path 5?

The construction agent identifies three sub-paths: (a) compute
off-diagonal resolvent, (b) use Hecke equivariance, (c) Li's
criterion. Attack 2 eliminates (c) as equivalent to (a). What
about (b)?

**Assessment of (b):** The Hecke operators T_p act on the BC
algebra and constrain the matrix elements <gamma_m | T_p | gamma_n>.
If the Hecke algebra forces the off-diagonal Weil matrix elements
to have specific signs, this could close the positive
semi-definiteness gap.

**The Hecke constraint:** T_p |gamma_n> = p^{i*gamma_n} |gamma_n>
(the Hecke eigenvalue is a phase). The off-diagonal matrix
element of T_p is:
    <gamma_m | T_p | gamma_n> = 0  (for m != n, since Hecke
    operators are diagonal in the gamma_n basis)

This means the Hecke operators provide NO off-diagonal information
— they are diagonal by construction.

**Result: WEAKENED.** Sub-path (b) is also blocked. The Hecke
operators are diagonal in the eigenbasis and provide no
off-diagonal constraints.

### Attack 4: Is Path 5 effectively dead?

All three sub-paths are blocked or equivalent:
- (a) requires computing off-diagonal resolvent matrix elements
  of T_BC, which is distributional
- (b) Hecke operators are diagonal, no off-diagonal info
- (c) equivalent to (a)

Is Path 5 headed for KILLED?

**Assessment:** No. Unlike Path 4 (category error) and Path 2
(structural impossibility), Path 5 has a WELL-POSED open question:
is the Weil matrix positive semi-definite? The difficulty is
computational (computing the off-diagonal elements), not
structural. The BC algebra provides the RIGHT framework (the
explicit formula IS the distributional trace), and the question
is whether additional algebraic structure (beyond KMS and Hecke)
constrains the answer.

Possible additional structures not yet explored:
- Galois action on the off-diagonal elements
- The multiplicative structure of A_BC (the Hecke ALGEBRA, not
  just individual Hecke operators)
- The Q*-action and its representation theory

**Result: SURVIVED.** Path 5 is blocked but not dead. The question
is well-posed and the framework provides potential tools not yet
deployed.

---

## Overall verdict: DAMAGED

Path 5 is DAMAGED by the failure of the KMS => Weil direction
(the cycle 1 primary target). All three proposed sub-paths have
issues. However, the path is not KILLED because:

1. The Weil positivity question is well-posed
2. The BC algebra is the correct framework
3. Unexplored algebraic structures remain

Path 5 needs a new approach for cycle 3: either a deeper algebraic
argument using the full multiplicative structure of A_BC, or an
indirect approach via a criterion not equivalent to Weil (e.g.,
the Nyman-Beurling completeness criterion, which characterises RH
via density of certain functions in L^2 and may be more accessible
from the BC Hilbert space).
