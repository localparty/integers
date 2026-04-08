# Prompt 02 — de Donder Gauge Vertex Numerator: Closing Assumption A1

**Issued by:** G (principal investigator)  
**Date:** 2026-04-07  
**Output file:** `02-de-donder-gauge-vertex.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/de-donder-gauge/`

---

## Why this computation exists

Research memo `01-three-graviton-vertex.md` (same directory) established that the
triangle y-integral coupling I_{+++}(n₁, n₂, n₁+n₂) = πR/4 is a universal constant
independent of KK level, and assembled C_GS = 0 from this. Conjecture 1 of Paper 10
is now conditionally proved, subject to three assumptions. The binding one is:

> **Assumption A1:** The vertex numerator in de Donder gauge does not introduce
> n-dependent terms at O(k²) in the UV, beyond the y-integrals already computed.

The concern: the 5D three-graviton vertex contains derivatives ∂_M. When the index M
is a fifth-dimension index (M=5), the derivative acting on a KK mode function produces
∂_5 cos(ny/R) = −(n/R) sin(ny/R) — explicitly n-dependent. If these ∂_5 terms survive
at leading UV order in the GS diagram, A1 fails and the proof has a gap.

This computation determines whether A1 is satisfied or not.

---

## Background to read first

- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/research/01-three-graviton-vertex.md`
  — read §"Gaps and residual assumptions" and §"Assumption A1" in particular
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/04-poisson-weyl.md`
  — Conjecture 1 statement and §4.6

---

## The de Donder gauge three-graviton vertex

In 5D linearized gravity, expand the Einstein-Hilbert action S = (1/2κ²)∫d⁵x √g R
around flat background g_{MN} = η_{MN} + κ h_{MN} to cubic order. In de Donder gauge
(harmonic gauge: ∂^M h_{MN} = (1/2)∂_N h where h = h^M_M), the cubic action gives the
three-graviton vertex.

The Goroff-Sagnotti diagram uses this vertex at each of its three cubic insertions. The
vertex has the schematic structure (Goroff-Sagnotti 1986, adapted to 5D):

    V_{MN,PQ,RS}(k₁,k₂,k₃) = η^{...} k₁^{...} k₂^{...} k₃^{...} terms

All three momenta k₁,k₂,k₃ satisfy k₁+k₂+k₃ = 0. In the GS 2-loop diagram, these are
linear combinations of the two independent loop momenta ℓ₁, ℓ₂ plus external momenta p.

**The n-dependence concern:** After KK reduction, the 5D loop momentum k^M = (k^μ, k^5)
where k^5 = n/R is the discrete KK momentum. The vertex V involves k^M contracted with
polarization indices. Terms with k^5 = n/R factors give n-dependent vertex numerators.

---

## Your task

### Step 1: Write the 5D de Donder gauge three-graviton vertex explicitly

The cubic term in the 5D EH action in de Donder gauge gives:

    L_cubic = κ h^{MN} [∂_M h^{PQ} ∂_P h_{NQ} − (1/2)∂_M h^{PQ} ∂_N h_{PQ}
              + (1/4)∂_M h ∂_N h − (1/2)∂_P h^{PQ} ∂_Q h_{MN} + ...]

Write the full momentum-space vertex V_{MN,PQ,RS}(k₁,k₂,k₃) by Fourier-transforming
and symmetrizing. Use the Goroff-Sagnotti (1986) 4D vertex as a starting point and
extend to 5D (add M=5 components throughout).

### Step 2: Separate ∂_μ terms from ∂_5 terms

Decompose the vertex into:
    V = V^{(4D)} + V^{(∂_5)}

where V^{(4D)} contains only k^μ (4-momentum components) and V^{(∂_5)} contains at
least one factor of k^5 = n/R.

V^{(4D)} reproduces the 4D Goroff-Sagnotti vertex — n-independent.

V^{(∂_5)} contains factors of n/R — explicitly n-dependent.

### Step 3: Power-count V^{(∂_5)} in the UV limit

In the GS 2-loop diagram, the loop momenta are ℓ₁, ℓ₂ ~ k (UV scale). External momenta
p << k. KK masses m_n = n/R << k (UV limit).

Count the power of k in each term of V^{(∂_5)} relative to V^{(4D)}:
- V^{(4D)} ~ k² at the vertex (each vertex contributes ~k² to the GS operator)
- V^{(∂_5)} has one factor of n/R replacing one factor of k^μ, so V^{(∂_5)} ~ (n/R) × k

The ratio: V^{(∂_5)} / V^{(4D)} ~ (n/R) / k = m_n / k << 1 in the UV limit.

**If this power counting holds:** the ∂_5 terms are O(m_n/k) suppressed at leading UV
order, A1 is satisfied, and the vertex numerator is effectively n-independent in the UV.

### Step 4: Identify any exceptions

Check whether there are terms in V^{(∂_5)} that are NOT suppressed in the UV — i.e.,
terms where the n/R factor multiplies something that grows faster with k than V^{(4D)}.
For example, if V^{(∂_5)} ~ (n/R) × k² / p (with an inverse external momentum), that
would be unsuppressed. Identify all such terms, if any.

### Step 5: Check the GS diagram structure specifically

The GS diagram has a specific topology: two loops, six propagators, three vertices. The
superficial degree of UV divergence is:
    D = 5×(2 loops) − 2×(6 propagators) + 2×(3 vertices) = 10 − 12 + 6 = 4
    
Wait — in 4D effective theory: D = 4×2 − 2×6 + 2×3 = 8 − 12 + 6 = 2.
The GS operator has dimension 6 (three Riemann tensors), so D = 6 → 2-loop divergent.

Redo the power counting including the ∂_5 vertex terms. Show that V^{(∂_5)} terms
in the GS diagram either:
(a) are suppressed by m_n/k (UV-safe), or
(b) vanish by the Epstein vanishing theorem at the relevant argument, or
(c) are exactly cancelled by the y-integral selection rules (forbidden by Z₂ parity)

### Step 6: Write Python code

In `/Users/gsix/quantum-geometry-in-5d-latex/code/de-donder-gauge/`:
- Create venv and install `sympy`, `mpmath`, `numpy`
- Implement the 5D de Donder vertex V_{MN,PQ,RS}(k₁,k₂,k₃) in sympy
  (use abstract symbolic momenta; don't need full tensor structure — focus on
  the k^5 = n/R dependence)
- Separate into V^{(4D)} and V^{(∂_5)} symbolically
- Power-count each term: substitute k^μ → λk^μ, k^5 → (n/R), and expand in λ → ∞
- Show V^{(∂_5)} / V^{(4D)} → 0 as λ → ∞ (i.e., in the UV limit)
- Numerically verify: for n = 1..20 and k/m_n = 10, 100, 1000, show the ratio
  V^{(∂_5)} / V^{(4D)} scales as 1/(k/m_n)
- Save as `compute.py`, output as `results.txt`

### Step 7: Write your research memo

Write `02-de-donder-gauge-vertex.md` with:

```
## Summary
## The question: Assumption A1 stated precisely
## The 5D de Donder gauge vertex (explicit)
## Decomposition: V^{(4D)} vs V^{(∂_5)}
## Power counting in the UV limit
## Exceptions and edge cases
## GS diagram structure check
## Numerical verification
   ### Code (key snippets)
   ### Results
## Verdict on A1: Satisfied / Partially satisfied / Failed
## If satisfied: statement of the closed theorem
## If failed: precise characterization of the gap
## Proposed next step
```

Aim for 500–650 lines. Be honest — if A1 is not satisfied in all cases, say so
precisely rather than papering over it.

---

## What a positive result looks like

If A1 is satisfied: state **Lemma A1** — "In de Donder gauge, the 5D three-graviton
vertex numerator, after KK decomposition on S¹/Z₂, introduces no n-dependent terms at
leading UV order (O(k²) in the GS diagram). The ∂_5 contributions are O(m_n/k)
suppressed and vanish in the UV limit."

Combined with `01-three-graviton-vertex.md`, this converts Conjecture 1 into
**Theorem 1** of Paper 10, closing the last gap.
