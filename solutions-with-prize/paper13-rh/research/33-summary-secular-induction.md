# Research 33 Summary — Lead D: Secular Equation + Induction

*Status: COMPLETED (research note + computation)*
*Type: STRONGEST LEAD (feasibility 5/10)*
*Date: 2026-04-10*

---

## Result

The inductive argument is clean and numerically verified:

1. Base case (K=0): Cauchy matrix is STP → all overlaps nonzero
   (Gantmacher-Krein). PROVED.

2. Inductive step: adding prime p_{K+1} preserves strict interlacing
   IFF ⟨φ_k^K | v_p⟩ ≠ 0 (single-prime overlap, SPO_K).

3. SPO_K verified numerically for all K=0..19 and N=8..30.
   ALL overlaps nonzero. Overlaps NOT decaying (slope ≥ 0).

## Key numerical findings

- Single-prime overlaps: always nonzero, not shrinking
- Spectral gap (B vs M_a): GROWS with primes added
- Simplicity: holds at every step
- Large N (25-30): overlaps ~10⁻⁶ to 10⁻⁷ (Cauchy conditioning),
  but still nonzero

## The remaining gap

Prove SPO_K: ⟨φ_k^K | v_p⟩ ≠ 0 for transcendental eigenvectors.

At K=0: eigenvectors are algebraic functions of {x_i} (Cauchy).
Baker's theorem applies → SPO_0 follows.

At K≥1: eigenvectors become transcendental (depend on all
previously added primes). Baker doesn't directly apply.
Need: extension of Baker to polynomial (not linear) forms
in {log p, π, γ_E}, or a structural argument.

## Why this is the best lead

- Reduces FULL Arithmetic Theorem to single-prime question
- Single-prime is simpler (one log p at a time)
- Numerics show overlaps DON'T decay → structural reason exists
- The non-decay suggests a monotonicity or positivity argument

## Files
- Research note: research/33-lead-D-secular-induction.md
- Code: code/secular_induction_test.py
