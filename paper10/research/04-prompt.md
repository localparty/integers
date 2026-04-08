# Prompt 04 — Assumption A3: Internal KK Loop Momentum Range on S¹/Z₂

**Issued by:** G (principal investigator)  
**Date:** 2026-04-07  
**Output file:** `04-a3-kk-loop-momentum-range.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/a3-kk-loop-range/`

---

## Context

Paper 10 Theorem 1 (conditional on A2–A3) states C_GS = 0 for 5D linearized gravity
on M⁴ × S¹/Z₂. The proof of Theorem 1 assembles as:

    C_GS = [πR/4]² × J(0) × Σ_n 1 = [πR/4]² × J(0) × S₀

where S₀ = 1 + 2ζ_R(0) = 0 is Paper 1's Theorem K.1.

The factor **Σ_n 1** — the KK level sum that equals S₀ — is where Assumption A3 enters:

> **Assumption A3:** In the Goroff-Sagnotti 2-loop diagram on M⁴ × S¹/Z₂, the internal
> KK momentum runs over all integers n ∈ ℤ (i.e., the full Kaluza-Klein spectrum
> including both positive and negative winding modes), so that the sum is
> Σ_{n=-∞}^{∞} 1 = 1 + 2ζ_R(0) = S₀ = 0.

The concern: on the orbifold S¹/Z₂, the physical KK spectrum is n ≥ 0 (even sector) and
n ≥ 1 (odd sector) — not n ∈ ℤ. If the path integral only sums over non-negative KK
levels, the sum is Σ_{n≥0} 1 or Σ_{n≥1} 1, which are NOT zero under zeta regularization.

## Background to read first

- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/research/01-three-graviton-vertex.md`
  — §"Assembly: proof of C_GS = 0" and §"Gaps and residual assumptions / A3"
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/05-open-problems.md`
  — §5.2c
- `/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/22-appendix-k-higher-loop-epstein.md`
  — How the S₁ = 1 + 2ζ_R(0) = 0 identity arises

## The mathematical question

On a circle S¹ with period 2πR (before orbifolding), the KK momentum runs over all
integers: k^5 = n/R, n ∈ ℤ. The loop sum is Σ_{n∈ℤ} f(n²) and the Poisson structure
gives S₀ = 1 + 2ζ_R(0) = 0.

On the orbifold S¹/Z₂, the physical modes are:
- Even sector: cos(ny/R), n = 0, 1, 2, ... → KK masses m_n = n/R, n ≥ 0
- Odd sector: sin(ny/R), n = 1, 2, ... → KK masses m_n = n/R, n ≥ 1

A naive reading: the path integral sums over these physical modes only (n ≥ 0 for even,
n ≥ 1 for odd), not over n ∈ ℤ. If so, S₀ is replaced by:
- Even only: 1 + ζ_R(0) = 1 + (−1/2) = 1/2 ≠ 0
- Odd only: ζ_R(0) = −1/2 ≠ 0

This is a genuine concern. The orbifold construction is the key to resolving it.

## Your task

### Step 1: The orbifold path integral — method of images

The standard treatment of orbifold field theory uses the method of images. The orbifold
S¹/Z₂ is constructed by identifying y ~ −y on S¹. The propagator on S¹/Z₂ is:

    G_{Z₂}(y, y') = G_{S¹}(y, y') + G_{S¹}(y, −y')

where G_{S¹} is the circle propagator. The full circle propagator sums over n ∈ ℤ.
The orbifold propagator sums over BOTH the direct and image contributions — which
together span all of ℤ (through the n and −n terms in G_{S¹}(y,−y')).

Show: the loop integral on S¹/Z₂ with the method-of-images propagator reduces to a
sum over n ∈ ℤ of the form (even part + image part) = (1/2)Σ_{n∈ℤ} + (1/2)Σ_{n∈ℤ}.
The factor of 2 from "direct + image" exactly restores the full integer sum.

### Step 2: Mode expansion derivation

Alternatively, derive A3 from first principles using the mode expansion:

The complete orthonormal mode functions on [0, πR] with Neumann BCs (Z₂-even) are:
    {1/√(πR), √(2/(πR)) cos(ny/R), n = 1,2,...}

The complete orthonormal mode functions with Dirichlet BCs (Z₂-odd) are:
    {√(2/(πR)) sin(ny/R), n = 1,2,...}

When computing a loop diagram, the internal propagator is expanded in ALL mode functions
of BOTH sectors. Show that the combined sum over even + odd modes:

    Σ_{n=0}^∞ [even contribution] + Σ_{n=1}^∞ [odd contribution]

with appropriate multiplicity factors from the mode normalization, equals the full
integer sum Σ_{n∈ℤ} up to the normalization factor.

Key: the normalization of zero-mode (n=0, even) is 1/√(πR); the normalization of
non-zero modes is √(2/(πR)). The factor of 2 difference for n ≥ 1 modes, combined
with the even + odd sectors, reconstructs the full Σ_{n∈ℤ}.

### Step 3: Horava-Witten / orbifold field theory literature

The loop sum on orbifolds is a standard result in string theory and Horava-Witten M-theory
compactifications. Look at:
- The structure of one-loop vacuum amplitudes on orbifolds (Dixon-Harvey-Vafa-Witten 1985,
  or Polchinski's string theory textbook Chapter 10 on orbifolds)
- The Horava-Witten setup (hep-th/9510209): the 11D SUGRA on S¹/Z₂ compactification
  gives precisely the loop structure we need
- State which result from this literature directly implies A3, and quote it

### Step 4: The even vs odd multiplicity reconciliation

From Route 03 (Z₂ parity, `paper9/research/03-z2-parity-cancellation.md`), the
cancellation between even and odd sectors is:
    c_even(n) + c_odd(n) = (+d₀) + (−d₀) = 0   for each n ≥ 1
    c_zero(0) = d₀    (from the n=0 massless graviton)

Wait — if the n=0 graviton contributes but doesn't cancel, the sum is not zero.
Resolve: how does the n=0 mode enter the S₀ computation? In S₀ = 1 + 2ζ_R(0):
- The "1" comes from the n=0 mode
- The "2ζ_R(0)" comes from n ≥ 1 modes counted with multiplicity 2 (direct + image)
Show that this is exactly what the orbifold path integral gives.

### Step 5: Write Python code

In `/Users/gsix/quantum-geometry-in-5d-latex/code/a3-kk-loop-range/`:
- Create venv and install `sympy`, `mpmath`, `numpy`
- Implement the method-of-images propagator on [0, πR] explicitly
  G_{Z₂}(y,y') = G_{S¹}(y,y') + G_{S¹}(y,−y')
- Expand in mode functions and show the coefficient of each mode
- Show that the loop sum (coincidence limit G_{Z₂}(y,y) integrated over y ∈ [0,πR])
  gives the same result as Σ_{n∈ℤ} [contribution] up to a constant factor
- Numerically verify: the sum using Z₂ propagator agrees with S₀ × constant to
  machine precision
- Show the zero-mode counting: 1 + 2Σ_{n=1}^N 1 → S₀ under zeta reg
- Save as `compute.py`, output as `results.txt`

### Step 6: Write research memo

Write `04-a3-kk-loop-momentum-range.md` with:

```
## Summary
## The question: Assumption A3 stated precisely
## The naive concern: orbifold spectrum is n ≥ 0, not n ∈ ℤ
## Resolution 1: method of images (direct + image = full ℤ sum)
## Resolution 2: mode expansion with normalization factors
## Resolution 3: orbifold literature (Dixon-Harvey-Vafa-Witten / HW)
## The zero-mode reconciliation (how "1" in S₀ = 1 + 2ζ_R(0) arises)
## Numerical verification
## Verdict on A3: Satisfied / Requires clarification / Failed
## If satisfied: statement of Lemma A3
## Proposed next step (if any)
```

Aim for 400–550 lines. If the method-of-images argument fully closes A3, state
Lemma A3 explicitly. If there is a subtlety (e.g., twisted sector contributions
in string theory that don't have a field theory analogue), report it precisely.
