# 233 — RH Cycle 2, Path 3 (Stone) — Adversarial

*Cycle: 2. Date: 2026-04-09. Agent: Adversarial.*

---

## Attacks attempted

### Attack 1: Does the anti-fine-tuning refinement add anything?

The construction agent refines the bound from P < 10^{-34} to
"P < 10^{-50} or lower" by considering correlations between
formulas. But this is still an anti-fine-tuning argument, not a
proof. Going from 10^{-34} to 10^{-50} does not change the
logical status: the step remains BLOCKED.

**Result: SURVIVED.** The construction agent correctly marked the
step as BLOCKED and the sub-computation as insufficient for proof.
The refinement is informative (it shows the bound is robust) but
does not advance the path.

### Attack 2: Is the dependency classification correct?

The construction agent says Path 3 is blocked on Path 5. Is this
accurate? Path 3 (Stone self-adjointness => real spectrum) requires:

1. T_BC is self-adjoint (Stone's theorem applies to the modular
   flow sigma_t, giving self-adjointness of the generator).
2. spec(T_BC) = {gamma_n} (spectral realisation).

Step 1 is proved (modular flow is a strongly continuous
one-parameter group, Stone's theorem gives self-adjointness of
the generator — but the generator is distributional per Meyer).

**Wait:** The Stone self-adjointness argument gives self-adjointness
of the GENERATOR of sigma_t. But Meyer's point is that this
generator, when restricted to H_R and identified with T_BC, is
distributional. So even Step 1 has a subtlety: self-adjointness
in what sense?

**Result: WEAKENED.** Path 3 has its own distributional subtlety,
independent of the dependency on Path 5. Even if Path 5 closes
(proving RH via Weil positivity), Path 3 does not automatically
become rigorous because its starting point (T_BC is self-adjoint
as a genuine operator) is questionable.

### Attack 3: Is the anti-fine-tuning argument valid?

The argument assumes that an extra eigenvalue lambda_extra would
perturb ALL 33 formulas. But the operator dictionary formulas
involve matrix elements <gamma_m | f(L-hat) | gamma_n> for
specific m, n. An extra eigenvalue would contribute to the
COMPLETENESS RELATION (sum over all eigenstates = 1) but would
not necessarily enter specific matrix elements unless the
corresponding eigenstate has nonzero overlap with the operators
used in the formulas.

**Result: WEAKENED.** The anti-fine-tuning argument assumes every
formula is sensitive to lambda_extra. This is true only if
<lambda_extra | f(L-hat) | lambda_extra> contributes to the
formulas, which requires the extra eigenstate to couple to the
physical operators. If the extra eigenstate is "dark" (zero
coupling to all operators in the dictionary), it would be
invisible to the anti-fine-tuning bound.

---

## Overall verdict: INTACT (weakened on dependency and dark-state)

Path 3 remains INTACT in the sense that its logical chain is
valid (self-adjointness => real spectrum), but it is weakened by:

1. The distributional subtlety applies to Path 3 itself, not just
   to downstream paths.
2. The anti-fine-tuning bound has a "dark state" loophole.

These weakenings do not break the path but reinforce its
classification as a DEPENDENT/COMPLETION path.
