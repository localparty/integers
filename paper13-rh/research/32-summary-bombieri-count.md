# Research 32 Summary — Lead C: Bombieri Eigenvalue Count

*Status: COMPLETED (evidence, not a proof path)*
*Type: Diagnostic / evidence*
*Date: 2026-04-10*

---

## Result

Li coefficients λ₁...λ₆₂ all positive (consistent with RH).
Hankel matrix H[i,j] = λ_{i+j+2} is NOT PSD (expected — Hankel
PSD is strictly stronger than Li positivity). Bombieri's actual
theorem applies to the Weil form QW^{N,+}, not the Hankel matrix.

## Why it's not a proof path

Weil positivity (QW ≥ 0) ⟺ RH. So "prove QW has no negative
eigenvalues" IS proving RH directly. No shortcut.

## What it provides

- Numerical confirmation: all tested eigenvalues positive
- Structural insight: Hankel PSD ≠ Li positivity (different objects)
- Consistency check on existing computations

## Caution re kill #6

Kill #6 showed off-line zeros make Li coefficients MORE positive
(wrong direction). Bombieri's theorem is about MATRIX eigenvalues
of the truncated Weil form, not individual Li coefficients. These
are different quantities. Lead C does not contradict kill #6 but
also cannot circumvent it — both reflect the fact that Weil
positivity is equivalent to RH.

## Files
- Research note: research/32-lead-C-bombieri-eigenvalue-count.md
- Code: code/bombieri_eigenvalue_count.py
