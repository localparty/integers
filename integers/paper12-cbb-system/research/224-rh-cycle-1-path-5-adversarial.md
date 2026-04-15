# 224 — RH Cycle 1, Path 5 (CM-trace) — Adversarial

*Cycle: 1. Date: 2026-04-09. Agent: Adversarial.*

---

## Attacks attempted

### Attack 1: Is "KMS implies Weil positivity" a known result or wishful thinking?

The construction agent's most promising sub-path is: KMS reflection
positivity at beta = 1 implies Weil positivity, therefore RH.

**Attack:** KMS reflection positivity is:
    omega_1(a* . sigma_{i beta/2}(a)) >= 0

Weil positivity is:
    sum_{rho, rho'} h(rho) h(rho') W(rho, rho') >= 0
    for all test functions h

These are DIFFERENT positivity conditions on DIFFERENT objects.
KMS positivity is a condition on the ALGEBRA (states and
automorphisms). Weil positivity is a condition on the ZEROS
(distribution on the critical line).

The connection requires the Connes-Marcolli explicit formula
(Theorems 1-3) which translates between the algebra and the
zeros. But the explicit formula is a distributional identity —
it preserves TRACE (distributional equality) not POSITIVITY.
Positivity is a quadratic condition; trace is linear. There is
no general theorem saying that distributional equality preserves
positivity from one side to the other.

**Result: WEAKENED.** The KMS-implies-Weil sub-path is not as
straightforward as the construction agent suggests. The gap
between KMS positivity and Weil positivity is a genuine
mathematical obstacle, not just a "Wick rotation."

### Attack 2: The "trivial" per-eigenvalue positivity w_n >= 0

The construction agent initially notes that w_n = |<...>|^2 >= 0
trivially, then corrects to note that Weil positivity is a GLOBAL
condition on the matrix W(rho, rho'), not per-eigenvalue.

**Attack:** This self-correction is valid but reveals that the
construction agent initially misunderstood the Weil criterion.
The correction is good. No further attack needed.

**Result: SURVIVED.** The construction agent caught its own error.

### Attack 3: Is the off-diagonal resolvent computation feasible?

The construction agent identifies "compute off-diagonal resolvent
matrix elements W(gamma_m, gamma_n)" as a needed step. But the
BC resolvent (T_BC - z)^{-1} is a distributional object (Meyer's
formulation). Off-diagonal matrix elements of a distributional
resolvent are not well-defined pointwise.

Furthermore, even if regularised, the number of off-diagonal
entries is infinite (all pairs (m, n)). Checking positive
semi-definiteness of an infinite matrix requires functional-
analytic machinery (the matrix must define a bounded operator,
and one must show it is positive in the operator sense).

**Result: WEAKENED.** The "compute W then check PSD" approach is
operationally difficult and may not converge to a proof.

### Attack 4: Could Weil positivity FAIL?

The iff nature of Path 5 means that if Weil positivity fails,
RH is false. Is there any scenario in the CBB framework where
Weil positivity could fail?

If the BC two-point function has negative spectral weights at
some scale, this would disprove RH. The anti-fine-tuning bound
(10^{-34}) makes this extremely unlikely but does not rule it
out.

**Result: SURVIVED.** This is a feature of the path, not a bug.
The iff condition is a double-edged sword — it can both prove
and disprove. The construction agent is aware of this.

---

## Overall verdict: INTACT (with caveats)

The construction agent correctly identified the path as BLOCKED
and proposed the most promising sub-path (KMS => Weil). The
adversarial analysis shows this sub-path is harder than initially
presented (Attack 1), but not impossible. The path remains the
most strategically valuable because:

1. It provides an iff condition (unique among the five paths)
2. Closing it unblocks/supersedes Paths 1 and 3
3. The KMS condition is a PROVED property of omega_1

The main adversarial contribution: the gap between KMS positivity
and Weil positivity is not a simple Wick rotation — it requires
showing that distributional equality (explicit formula) preserves
a quadratic positivity condition. This is a specific, well-posed
mathematical question.
