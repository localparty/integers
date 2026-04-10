# Research 34 Summary — Lead F: Parametric τ-Tracking

*Status: COMPLETED (research note + computation)*
*Type: Diagnostic (strong numerics, weak as proof)*
*Feasibility: 3/10 proof, 9/10 diagnostic*
*Date: 2026-04-10*

---

## Result

B(τ) = B_arch + τ·B_prime swept from τ=0 to τ=1.

- Gap monotonically decreases from 10⁻³ (τ=0) to 10⁻²³ (τ=1)
- Minimum is at τ=1 (the target), not intermediate
- Zero sign changes in det(C(τ)) — no spectral coincidence
- Numerically clean: the Arithmetic Theorem holds at every τ

## Critical theoretical finding

VNW does NOT apply to two-matrix coincidences. Eigenvalues of
B(τ) and M_a(τ) are eigenvalues of DIFFERENT matrices.
Codimension of coincidence = 1 (not 2). Crossings CAN occur
as isolated points in one-parameter families. Continuity alone
cannot exclude them.

## What it provides

- The gap decreases monotonically: τ=0 is easiest, τ=1 is hardest
- No intermediate instability — the difficulty comes from the
  full arithmetic content, not from partial content
- Supports Lead D's finding: primes don't create coincidences,
  they approach but never reach them

## Files
- Research note: research/34-lead-F-parametric-tau-tracking.md
- Code: code/parametric_tau_test.py
