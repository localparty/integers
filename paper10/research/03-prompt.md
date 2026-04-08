# Prompt 03 — Assumption A2: h_{μ5} and φ Sector Contributions to the GS Counterterm

**Issued by:** G (principal investigator)  
**Date:** 2026-04-07  
**Output file:** `03-a2-graviphoton-radion-sector.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/a2-graviphoton-radion/`

---

## Context

Paper 10 Theorem 1 (conditional on A2–A3) states that C_GS = 0 for the KK graviton
tower on M⁴ × S¹/Z₂. The proof is complete for the h_{μν} sector (KK gravitons and
their even-mode KK excitations). Assumption A2 asks:

> **Do the h_{μ5} (graviphoton) and h_{55}/φ (radion/graviscalar) sectors contribute
> to the leading Goroff-Sagnotti counterterm?**

## Background to read first

- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/research/01-three-graviton-vertex.md`
  — §"Selection rules at the GS vertex"
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/05-open-problems.md`
  — §5.2b (the open question statement)
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/03-z2-mechanism.md`
  — §3.1 (field content and Z₂ parities)

## The fields

On S¹/Z₂, the 5D metric fluctuation h_{MN} decomposes as:
- **h_{μν}^{(n)}**: spin-2 KK gravitons (Z₂-even, n = 0,1,2,...) — 5 d.o.f. per level
- **A_μ^{(n)} ≡ h_{μ5}^{(n)}**: spin-1 graviphoton / KK gauge field (Z₂-odd, n = 1,2,...) — 2 d.o.f. per level (massive); zero mode projected out by Z₂
- **φ^{(n)} ≡ h_{55}^{(n)}**: spin-0 radion / graviscalar (Z₂-even, n = 0,1,2,...) — 1 d.o.f. per level; n=0 is the massless radion

The GS operator is R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} — built entirely from the 4D Riemann
tensor with purely 4D spacetime indices.

## Your task

### Step 1: Field content analysis

In the 4D effective theory obtained by KK reduction of 5D linearized gravity:
- What is the spin content of each field? (spin-2 gravitons, spin-1 graviphotons, spin-0 radions)
- Which fields couple to R_{μνρσ} at the linearized level? The linearized Riemann tensor
  is built from h_{μν} only — h_{μ5} and h_{55} do not appear in R^{(1)}_{μνρσ}.
- Does this mean A_μ^{(n)} and φ^{(n)} cannot contribute to R_{μνρσ}³ at tree level?

### Step 2: Loop contributions

Even if A_μ and φ don't appear in R_{μνρσ} at tree level, they can appear inside loops
contributing to the GS counterterm. Analyze:

(a) **One-particle irreducible diagrams**: Can a graviphoton loop generate R_{μνρσ}³?
    The graviphoton A_μ^{(n)} has mass m_n = n/R and couples to the graviton via the
    KK vertex. The GS diagram has three graviton external legs. Can internal graviphoton
    lines generate the same GS counterterm?

(b) **Spin-1 Weyl anomaly**: The 4D Weyl anomaly coefficient for a massive spin-1 field
    is (a, c) = (−13/360, −3/20) (opposite sign to graviton!). If the graviphoton tower
    contributes, the total anomaly gets a correction. Compute:
    a_total^{A_μ} = (−13/360) × Σ_{n≥1} 1 = (−13/360) × (S₀ − 1) where S₀ = 0,
    so a_total^{A_μ} = (−13/360) × (−1) = 13/360.
    Wait — this is non-zero! Investigate whether this is cancelled by the radion.

(c) **Spin-0 radion Weyl anomaly**: The radion φ^{(n)} has (a, c) = (1/360, 1/180)
    for a massless scalar. For the tower of massive radions:
    a_total^φ = (1/360) × Σ_{n≥0} 1 = (1/360) × S₀ ... but does the n=0 massless
    radion need special treatment? Compute both with and without the zero mode.

(d) **Combined total**: h_{μν} + A_μ + φ contribution to Weyl anomaly. Does it sum to
    zero? If not, does the mismatch signal a genuine gap in A2?

### Step 3: Index structure of the GS operator

The GS counterterm R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} requires three insertions of the
linearized Riemann tensor R^{(1)}_{μνρσ} = ∂_μ∂_[ρh_{σ]ν} − ∂_ν∂_[ρh_{σ]μ}.
This is built entirely from h_{μν}. Therefore:
- At the level of the GS operator itself, A_μ and φ do not appear
- The question is whether A_μ and φ loops can *generate* effective h_{μν} vertices
  that then feed into the GS operator

Analyze: what is the lowest-order diagram where an internal A_μ^{(n)} or φ^{(n)} line
contributes to an effective R_{μνρσ}³ operator? What is its superficial degree of
divergence? Is it UV-divergent at 2 loops?

### Step 4: Z₂ selection rules revisited

The GS vertex has a specific Z₂ parity structure (from memo 01: only Z₂-even × Z₂-even
× Z₂-even = + combinations contribute at the leading vertex). Check:
- A_μ^{(n)} is Z₂-odd. For a graviphoton to appear inside the GS sunset loop, it must
  appear in pairs (two odd fields give even product). What diagrams have A_μ appearing
  in pairs internally?
- Does Z₂ parity forbid ALL single-insertion A_μ contributions? If so, what about
  double-insertion (two graviphotons in one loop)?

### Step 5: Write Python code

In `/Users/gsix/quantum-geometry-in-5d-latex/code/a2-graviphoton-radion/`:
- Create venv and install `sympy`, `mpmath`, `numpy`
- Compute the full 5D KK Weyl anomaly sum including all three sectors:
  Σ_n a_n^{h_{μν}} + Σ_n a_n^{A_μ} + Σ_n a_n^{φ}
  Use Vassilevich (2003) formulas: spin-2 (43/360), spin-1 (−13/360), spin-0 (1/360)
- Show whether the combined sum is zero or non-zero
- If non-zero: characterize the discrepancy precisely
- Also compute: using the DOF count (5 per graviton level, 2 per graviphoton, 1 per
  radion, for massive levels; massless graviton has 2 d.o.f., massless radion has 1),
  does the total weighted anomaly cancel?
- Save as `compute.py`, output as `results.txt`

### Step 6: Write research memo

Write `03-a2-graviphoton-radion-sector.md` with:

```
## Summary
## The question: Assumption A2 stated precisely
## Field content: h_{μν}, A_μ, φ on S¹/Z₂ with Z₂ parities
## Tree-level analysis: A_μ and φ absent from R_{μνρσ}
## Loop analysis: can graviphoton/radion loops generate GS operator?
## Index structure argument
## Z₂ selection rules for internal A_μ lines
## Weyl anomaly: full tower computation (all three sectors)
## Numerical results (embedded from code)
## Verdict on A2: Satisfied / Partially satisfied / Failed / Requires further work
## If satisfied: statement of Lemma A2
## Proposed next step
```

Aim for 450–600 lines. Verdict must be honest — if the Weyl anomaly computation
shows a non-zero total from A_μ and φ, report it as a genuine gap.
