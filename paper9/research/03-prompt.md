# Prompt 03 — Z₂ Parity Cancellation Route

**Issued by:** G (principal investigator)  
**Route:** 03 — Z₂ even/odd mode parity cancellation  
**Output file:** `03-z2-parity-cancellation.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/z2-parity/`

---

## Context

Paper 1 of the QG5D series proves UV finiteness of 5D linearized gravity on M⁴ × S¹/Z₂
via zeta regularization. The open question: is the vanishing scheme-independent?

## Your question

**Is the Epstein vanishing a consequence of Z₂ parity, forcing even/odd KK mode
contributions to cancel — in any Z₂-preserving regularization scheme?**

On the orbifold S¹/Z₂, the fifth dimension coordinate y is identified under y → −y.
KK modes decompose into:
- Z₂-even: cos(ny/R), n = 0, 1, 2, ... (survive on both branes)
- Z₂-odd: sin(ny/R), n = 1, 2, ... (vanish at fixed points)

The graviton fluctuation h_{MN} on the orbifold has definite Z₂ parities determined by
the index structure: h_{μν} (4D graviton and KK gravitons) is Z₂-even; h_{μ5} (KK
graviphoton) is Z₂-odd; h_{55} (radion) is Z₂-even.

The Goroff-Sagnotti vertex R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} is a cubic in the Riemann tensor.
The question is: what is the net Z₂ parity of the three-vertex when two or three external
legs carry KK indices?

**If the vertex has odd Z₂ parity for the dominant diagram topology**, then:
- Even-mode contributions and odd-mode contributions enter with opposite signs
- They cancel pairwise for each KK level n
- The cancellation is a consequence of Z₂ symmetry — it holds in ANY regulator
  that preserves Z₂ (dim-reg does, cutoff reg does if imposed symmetrically, Pauli-Villars does)

## Your task

1. **Read Paper 1 relevant sections** at:
   `/Users/gsix/quantum-geometry-in-5d-latex/paper1/`
   Focus on: `34-appendix-w-orbifold-dark-sector.md` (orbifold structure),
   `32-appendix-u-goroff-sagnotti-verification.md`

2. **Analyze the Z₂ parity of the GS vertex.** 
   - Write the 5D linearized graviton vertex for h_{MN}h_{PQ}h_{RS} → R...R...R
   - Track the Z₂ transformation of each field component under y → −y
   - Determine: for the 2-loop GS diagram, what is the net Z₂ parity of the integrand?
   
3. **Show the mode-by-mode cancellation** if the argument holds:
   - For each KK level n, show that contribution from Z₂-even mode n cancels
     contribution from Z₂-odd mode n to the GS coefficient
   - Write the cancellation formula explicitly

4. **Identify which regulators preserve Z₂.** Dimensional regularization (continue d)
   preserves all discrete symmetries. Cutoff regularization preserves Z₂ if the cutoff
   is imposed on |p| not on individual mode numbers. Pauli-Villars preserves Z₂ if PV
   fields come in Z₂ partners. Zeta regularization manifestly preserves Z₂.

5. **Write Python code** in `/Users/gsix/quantum-geometry-in-5d-latex/code/z2-parity/`:
   - Create venv, install `sympy`, `numpy`, `mpmath`
   - Implement the KK mode sum for the GS coefficient symbolically
   - Separate into even and odd contributions
   - Verify numerically (sum over n = 1..1000) that even and odd contributions cancel
     to machine precision
   - Show this holds for multiple truncations (n=10, 100, 1000) to demonstrate
     it's not a finite-truncation accident
   Save as `compute.py`, output as `results.txt`.

6. **Write your research memo** to `03-z2-parity-cancellation.md`:
   - Summary
   - Setup (orbifold parity, mode decomposition)
   - Parity analysis of the GS vertex
   - Cancellation proof (algebraic)
   - Numerical verification
   - Which regulators this argument covers (and which it misses)
   - Gaps and obstacles
   - Status verdict
   - Proposed next step

Aim for 400–600 lines.
