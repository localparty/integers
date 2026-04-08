# Prompt 02 — Heat Kernel / Seeley-DeWitt Route

**Issued by:** G (principal investigator)  
**Route:** 02 — Heat kernel / Seeley-DeWitt coefficients  
**Output file:** `02-heat-kernel-seeley-dewitt.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/seeley-dewitt/`

---

## Context

Paper 1 of the QG5D series proves UV finiteness via zeta regularization of KK mode sums.
The open honesty (Paper 1 Appendix U §U.2c): scheme-independence is not proved.

## Your question

**Do the Seeley-DeWitt (heat kernel) coefficients vanish for linearized 5D gravity on
M⁴ × S¹/Z₂?**

The Seeley-DeWitt coefficients a_{2k} appear in the small-t expansion of the heat kernel:

    Tr(e^{−tD}) ~ ∑_k a_{2k}(D) · t^{k − d/2}    as t → 0⁺

These coefficients are **intrinsically geometric invariants** — they depend only on the
background geometry and the symbol of the kinetic operator D. They are scheme-independent
by construction: they can be computed from the operator's symbol without reference to any
regularization.

The connection to UV finiteness: the poles of the spectral zeta function ζ_D(s) are
residues of the Mellin transform of Tr(e^{−tD}), and they equal the Seeley-DeWitt
coefficients. If a_{2k}(D) = 0 for all relevant k, then ζ_D(s) has no poles at the
corresponding points — UV finiteness is scheme-independent.

For the orbifold S¹/Z₂, the heat kernel has two contributions:
1. Bulk contribution: standard Seeley-DeWitt series for the interior
2. Fixed-point (brane) contributions: localized at the two Z₂ fixed points y = 0, πR

The fixed-point contributions are given by Cheeger's cone formula and the
Branson-Gilkey orbifold heat kernel results.

## Your task

1. **Read Paper 1 relevant sections** at:
   `/Users/gsix/quantum-geometry-in-5d-latex/paper1/`
   Focus on: `32-appendix-u-goroff-sagnotti-verification.md`,
   `22-appendix-k-higher-loop-epstein.md`, `30-appendix-s-finiteness-theorem.md`

2. **Identify the kinetic operator D** for linearized gravity on M⁴ × S¹/Z₂.
   This is the Lichnerowicz operator acting on spin-2 fluctuations h_{μν}.
   Write its symbol and the relevant background geometry.

3. **Compute the Seeley-DeWitt coefficients a₂ and a₄** for this operator using
   the Vassilevich (2003) formulas (hep-th/0306138 — the standard reference).
   The coefficients are expressed as integrals of local curvature invariants.
   On flat M⁴ × S¹/Z₂ background (linearized gravity = flat background), the
   M⁴ curvature invariants vanish. Focus on the S¹/Z₂ contributions.

4. **Include the fixed-point corrections.** The Z₂ orbifold has fixed points at
   y = 0 and y = πR. The heat kernel on an orbifold receives boundary contributions
   proportional to the eta invariant and extrinsic curvature of the fixed-point set.
   For S¹/Z₂, these are known explicitly.

5. **Write Python code** in `/Users/gsix/quantum-geometry-in-5d-latex/code/seeley-dewitt/`:
   - Create venv and install `sympy`, `mpmath`, `numpy`
   - Implement the Vassilevich a₂ and a₄ formulas symbolically in sympy
   - Compute the bulk and fixed-point contributions separately
   - Verify whether the total (bulk + fixed-point) vanishes
   - Cross-check: does the numerical heat kernel trace (computed by truncating the
     KK spectrum to n ≤ 500) agree with the analytic Seeley-DeWitt prediction?
   Save as `compute.py`, output as `results.txt`.

6. **Write your research memo** to `02-heat-kernel-seeley-dewitt.md`:
   - Summary
   - Setup (Vassilevich formulas, orbifold heat kernel)
   - Main computation (a₂, a₄ — show the algebra)
   - Numerical cross-check results
   - Gaps (higher-loop = higher a_{2k}; generating function argument needed)
   - Status verdict
   - Proposed next step if promising

Aim for 400–600 lines including embedded code and output.
