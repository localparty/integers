# Prompt 04 — Poisson Resummation / Dim-Reg Route

**Issued by:** G (principal investigator)  
**Route:** 04 — Poisson resummation + dimensional regularization  
**Output file:** `04-poisson-dimreg.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/poisson-dimreg/`

---

## Context

Paper 1 proves UV finiteness via zeta regularization. The scheme-independence question:
does the same vanishing appear in dimensional regularization?

## Your question

**Can Poisson resummation be used to show that the KK mode sum in dim-reg reduces to
the same Epstein zeta function, with the same vanishing?**

In dimensional regularization, the loop integral with KK tower summed is:

    I = ∑_{n=-∞}^{∞} ∫ d^(4−ε)k / (2π)^(4−ε)  ·  F(k², n²/R²)

where F is the integrand from the GS diagram and m_n = n/R are the KK masses.

Zeta regularization performs the KK sum via analytic continuation of ∑ m_n^{−2s}.
Dimensional regularization continues d = 4 − ε.

**The Poisson resummation lemma:** Under suitable conditions on F, we can interchange
the order of integration and summation:

    ∑_n ∫ dk F(k², n²/R²) = ∫ dk ∑_n F(k², n²/R²)

If this exchange is valid, then the KK sum ∑_n F(k², n²/R²) — performed at fixed k²
— produces the Epstein zeta function structure. The UV divergences (poles in ε) then
inherit the vanishing of the Epstein function.

**The Poisson resummation identity** (Jacobi / Poisson):

    ∑_{n=-∞}^{∞} f(n/R) = R ∑_{m=-∞}^{∞} f̂(mR)

where f̂ is the Fourier transform. For the propagator 1/(k² + n²/R²), this converts the
KK sum into a sum over winding modes — convergent in position space, enabling the
exchange of sum and integral.

## Your task

1. **Read Paper 1 relevant sections** at:
   `/Users/gsix/quantum-geometry-in-5d-latex/paper1/`
   Focus on: `32-appendix-u-goroff-sagnotti-verification.md`,
   `22-appendix-k-higher-loop-epstein.md`

2. **Write down the explicit GS diagram integrand** F(k², n²/R²) for the 2-loop
   diagram in 5D linearized gravity. What are the propagators? What are the vertices?
   What power of k and m_n does the integrand carry?

3. **State and prove the exchange lemma:** Under what conditions on F can the KK sum
   and loop integral be interchanged? The key conditions are:
   - Uniform convergence of the sum in k (or dominated convergence)
   - Sufficient UV decay of F in k at fixed n
   Use the Poisson resummation form: after resummation, the sum over winding modes
   converges exponentially, justifying the exchange.

4. **Show that after the exchange**, the KK sum ∑_n F(k², n²/R²) evaluated at fixed k
   gives the Epstein function, and the Epstein vanishing implies the dim-reg pole
   (coefficient of ε^{−1}) also vanishes.

5. **Identify the residual: finite renormalization.** Even if the poles agree, zeta and
   dim-reg can differ by finite terms. Show that this finite difference does NOT affect
   the conclusion of UV finiteness (finite counterterms are acceptable; zero counterterms
   are not required — only zero divergent counterterms).

6. **Write Python code** in `/Users/gsix/quantum-geometry-in-5d-latex/code/poisson-dimreg/`:
   - Create venv, install `mpmath`, `scipy`, `numpy`, `sympy`
   - Implement the Poisson resummation identity numerically for a sample F
     (use F = (k² + n²/R²)^{−s} as the test case)
   - Verify that ∑_n F(k², n²/R²) agrees with the Epstein zeta function to
     machine precision for a range of k², R, s values
   - Show that the ε → 0 pole of ∫ dk ∑_n F(...) with dim-reg equals the
     zeta-regulated value at the same argument
   - Show the exchange (sum first vs. integrate first) gives the same answer
   Save as `compute.py`, output as `results.txt`.

7. **Write your research memo** to `04-poisson-dimreg.md`:
   - Summary
   - Setup (GS integrand structure)
   - The exchange lemma (statement and proof sketch)
   - Poisson resummation connecting dim-reg to zeta
   - The finite-renormalization residual
   - Numerical verification
   - Gaps (does this extend to all loop orders? non-linearized gravity?)
   - Status verdict
   - Proposed next step

Aim for 400–600 lines.
