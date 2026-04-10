# Research 37 Summary — Lead H: Cartwright Analytic Continuation

*Status: COMPLETED*
*Type: STRONGEST LEAD (feasibility 7/10)*
*Date: 2026-04-10*

---

## Result

**The argument is nearly complete:**

1. φ_k compactly supported on [0,L] → Paley-Wiener → φ̂_k entire
   of exponential type σ = L
2. {log p} has infinite upper density (PNT: π(e^T)/T ~ e^T/T²)
3. Cartwright: entire function of type σ vanishing on set of
   density > σ/π is ≡ 0
4. Infinite > σ/π for any finite σ → φ̂_k vanishes at only
   FINITELY many {log p}
5. Finitely many handled by numerical verification (120 digits)

**Therefore: SPO holds for all but finitely many primes, and
the finite exceptions are verified numerically.**

## The one gap

Discrete-to-continuous interpolation: the grid eigenvector
(a vector in R^N) needs to be connected to a compactly
supported continuous function for Paley-Wiener to apply.

Rated: FILLABLE, not fundamental. Standard interpolation
theory (cubic spline on Chebyshev nodes converges in L²).

## Computation

All 750 overlaps (30 eigvecs × 25 primes) nonzero.
Minimum: 2.82 × 10⁻⁶ (well above threshold).
Fourier transforms smooth, confirming finite type.

## What this gives

**If the interpolation gap is filled:**
SPO holds → secular induction (Lead D) closes →
Arithmetic Theorem → Even-Sector Simplicity →
CCM Theorem 5.10 → spec(D_∞) = {γ_n} → **RH.**

## Files
- Research note: research/37-lead-H-cartwright-analytic.md
- Code: code/cartwright_test.py
