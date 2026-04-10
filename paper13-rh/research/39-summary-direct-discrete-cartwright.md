# Research 39 Summary — Lead L: Direct Discrete Cartwright

*Status: COMPLETED — STRONGEST LEAD (8/10)*
*Type: POTENTIAL PROOF CLOSER*
*Date: 2026-04-10*

---

## The argument

1. g_k(ξ) = Σ_i φ_k[i] cos(x_i ξ) is a finite cosine sum
   → TRIVIALLY entire of exponential type σ = max|x_i|

2. g_k ≢ 0: {cos(x_i ξ)} are linearly independent for distinct
   x_i (standard), and φ_k ≠ 0 (eigenvector) → g_k not identically zero

3. {log p : p prime} has infinite upper density (PNT: π(e^T)/T → ∞)

4. Cartwright's theorem: non-zero entire function of type σ cannot
   vanish on a set of density > σ/π. Since ∞ > σ/π for any
   finite σ → g_k vanishes at FINITELY many {log p}

5. The overlap ⟨φ_k | v_p⟩ = g_k(log p). So SPO holds for all
   but finitely many primes per eigenvector.

6. Finite exceptions: numerical verification at 120 digits
   (0 exceptions found across 1500 tests)

## Computation confirms

- 0 zeros / 1500 tests (30 eigenvectors × 50 primes)
- Minimum overlap: 6.65 × 10⁻²⁷ (nonzero)
- Type σ ≈ 9.97, σ/π = 3.18
- Density of {log p} = +∞ ≫ 3.18

## The interpolation gap: ELIMINATED

No discrete-to-continuous bridge needed. The finite cosine sum
IS already an entire function. The discrete grid eigenvector
defines g_k directly. Paley-Wiener is not needed — the type
bound follows from the finite sum structure alone.

## What remains

1. **Verify g_k ≢ 0 rigorously for ALL eigenvectors** (not just
   numerically). Linear independence of {cos(x_i ξ)} for distinct
   x_i is standard (Chebyshev nodes are distinct). φ_k ≠ 0 by
   definition (eigenvector). So g_k ≢ 0 follows rigorously.

2. **Handle the finite exceptions.** Cartwright gives: at most
   C(σ) values of log p where g_k = 0. Computation found 0.
   For a proof: either show C(σ) = 0 (no exceptions ever),
   or verify the first C(σ) primes numerically.

3. **Connect to the full chain.** SPO → Lead D induction →
   Arithmetic Theorem → Even-Sector Simplicity → CCM → RH.

## The chain to RH

IF this argument is correct:

SPO (Cartwright + computation)
→ secular induction preserves strict interlacing (Lead D)
→ Arithmetic Theorem: spec(B) ∩ spec(M_a) = ∅
→ Even-Sector Simplicity Conjecture proved
→ CCM Theorem 5.10 (modified even sector)
→ spec(D_∞) = {γ_n} ⊂ ℝ
→ **The Riemann Hypothesis.**

## Files
- Research note: research/39-lead-L-direct-discrete-cartwright.md
- Code: code/direct_discrete_cartwright.py (runs clean, 0 zeros)
