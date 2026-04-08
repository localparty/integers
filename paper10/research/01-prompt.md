# Prompt 01 — Three-Graviton Vertex KK Decomposition: Vertex Mass-Independence

**Issued by:** G (principal investigator)  
**Date:** 2026-04-07  
**Output file:** `01-three-graviton-vertex.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/three-graviton-vertex/`

---

## Why this computation exists

Paper 10 of the QG5D series addresses scheme-independence of UV finiteness for 5D
linearized gravity on M⁴ × S¹/Z₂. Five parallel research routes (see
`/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/`) established that the
one-loop result is scheme-independent (Theorem U.2a, Route 02) and that the Weyl anomaly
argument covers the GS sector conditionally (Theorem 4.3, Route 05).

The one gap identified independently by Routes 01, 04, and 05 is:

> **Vertex mass-independence has not been explicitly computed.** Does the GS three-graviton
> vertex in 5D KK gravity, after KK decomposition and y-integral over [0, πR], produce a
> coupling that is mass-independent at leading UV order?

This is Conjecture 1 in Paper 10 §04. This computation is its attempted proof.

## The mathematical question

The 5D graviton h_{MN}(x, y) decomposes on S¹/Z₂ into KK modes. The relevant fields and
their Z₂ parities are:

    h_{μν}(x,y) = (1/√(πR)) Σ_{n≥0} h_{μν}^{(n)}(x) cos(ny/R)    [Z₂-even]
    h_{μ5}(x,y) = (1/√(πR)) Σ_{n≥1} h_{μ5}^{(n)}(x) sin(ny/R)    [Z₂-odd]
    h_{55}(x,y) = (1/√(πR)) Σ_{n≥0} φ^{(n)}(x)     cos(ny/R)    [Z₂-even]

(The n=0 mode for h_{μ5} is projected out by Z₂.)

The three-graviton vertex in 5D linearized gravity (from the cubic term in the
Einstein-Hilbert expansion around flat background) gives, after KK reduction, a coupling:

    g(n₁, σ₁; n₂, σ₂; n₃, σ₃) ∝ ∫₀^{πR} f_{n₁,σ₁}(y) · f_{n₂,σ₂}(y) · f_{n₃,σ₃}(y) dy

where σ ∈ {+, −} indicates Z₂-even (cos) or Z₂-odd (sin) and:

    f_{n,+}(y) = cos(ny/R)
    f_{n,−}(y) = sin(ny/R)

**The four distinct y-integrals are:**

    I_{+++}(n₁,n₂,n₃) = ∫₀^{πR} cos(n₁y/R) cos(n₂y/R) cos(n₃y/R) dy
    I_{++-}(n₁,n₂,n₃) = ∫₀^{πR} cos(n₁y/R) cos(n₂y/R) sin(n₃y/R) dy
    I_{+--}(n₁,n₂,n₃) = ∫₀^{πR} cos(n₁y/R) sin(n₂y/R) sin(n₃y₃/R) dy
    I_{---}(n₁,n₂,n₃) = ∫₀^{πR} sin(n₁y/R) sin(n₂y/R) sin(n₃y/R) dy

**Vertex mass-independence** means: the coefficient of the GS counterterm
R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} in the 2-loop effective action, computed from KK graviton
loops, is proportional to:

    C_GS ∝ Σ_n [g(n,+; n,+; n,+)]² × J(m_n²)

where J(m_n²) is the momentum-space loop integral (a function of KK mass m_n = n/R).

**The claim to verify:** In the UV limit (loop momentum k >> m_n), J(m_n²) → J(0)
(the massless result). If simultaneously g(n,+; n,+; n,+) is n-independent (or factors
cleanly from the n-sum), then C_GS = [g]² × J(0) × Σ_n 1 = [g]² × J(0) × S₀ = 0,
where S₀ = 1 + 2ζ(0) = 0 is Paper 1's Theorem K.1.

---

## Your task

### Step 1: Read the background

Read these files for context (do not skip — they define the notation and the gap):
- `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/01-number-theoretic-zeta-zeros.md`
  (§ on "Leading S₀ gap" and "orbifold subtlety")
- `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/04-poisson-dimreg.md`
  (§ on "vertex mass-independence gap")
- `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/05-weyl-anomaly-kk-tower.md`
  (§ on "Conjecture 1" and what needs to be verified)
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/04-poisson-weyl.md`
  (Conjecture 1 full statement and computation roadmap)

### Step 2: Compute the y-integrals analytically

Use product-to-sum identities:
    cos(A)cos(B) = [cos(A−B) + cos(A+B)] / 2
    sin(A)sin(B) = [cos(A−B) − cos(A+B)] / 2
    sin(A)cos(B) = [sin(A+B) + sin(A−B)] / 2

Then ∫₀^{πR} cos(ny/R) dy = πR·δ_{n,0} and ∫₀^{πR} sin(ny/R) dy = 0 for all n.

Compute I_{+++}, I_{++-}, I_{+--}, I_{---} in closed form as functions of (n₁,n₂,n₃).
Characterize all cases: (a) diagonal n₁=n₂=n₃=n, (b) two equal n₁=n₂≠n₃,
(c) all distinct n₁≠n₂≠n₃, (d) zero modes (any nᵢ=0).

### Step 3: Identify which vertex topologies contribute to the GS diagram

The GS diagram (2-loop, three internal graviton lines) has specific topology. Identify:
- Which combinations (σ₁,σ₂,σ₃) of Z₂ parities appear
- Which KK levels (n₁,n₂,n₃) are summed over
- What the selection rules are (parity conservation at each vertex: must have even
  number of Z₂-odd fields at each cubic vertex — verify this)

### Step 4: Analyze UV behavior of the loop integral J(m²)

For the GS diagram, the momentum-space loop integral at each KK level n is:
    J(m_n²) = ∫ d⁴k₁ d⁴k₂ / (2π)⁸  ·  [propagators with mass m_n] × [vertices ~ k²]

In the UV (k >> m_n):
    J(m_n²) = J(0) + m_n² × J'(0) + O(m_n⁴)

The leading UV divergence comes from J(0). Show that the correction terms m_n² × J'(0)
are less UV-divergent (lower superficial degree of divergence), so the GS coefficient
at leading order is m_n-independent.

### Step 5: Assemble the proof of vertex mass-independence

Combine Steps 2–4:
- Write C_GS as a sum over KK levels with the y-integral couplings × momentum integral
- Separate into a leading term (J(0), mass-independent) × Σ_n [coupling]² and
  subleading terms (J'(0), suppressed)
- Show the leading term: [coupling]² × Σ_n 1 = [coupling]² × S₀ = 0
- Show the subleading terms: [coupling]² × m_n² × Σ_n m_n^{2k} = Epstein at higher s,
  vanishing by the Universal Epstein Vanishing theorem (Paper 1, Theorem K.1)
- Conclude: C_GS = 0 to all orders in m_n/k, scheme-independently

### Step 6: Write Python code

In `/Users/gsix/quantum-geometry-in-5d-latex/code/three-graviton-vertex/`:
- Create venv and install `sympy`, `mpmath`, `numpy`, `scipy`
- Compute I_{+++}(n₁,n₂,n₃) symbolically using sympy for general n₁,n₂,n₃
- Verify closed-form results numerically for n = 1..20
- Compute the diagonal coupling g(n,n,n) = I_{+++}(n,n,n) and confirm it is
  n-independent (or find exactly how it scales with n)
- Compute g(n,n,n)² × Σ_{n=1}^{N} 1 for N = 10, 100, 1000 and show convergence
  to zero under zeta regularization (S₀ = 1 + 2ζ(0) = 0)
- Compute the first subleading correction: Σ_n (n/R)² = ζ_R(−2) = 0 (trivial zero)
  and Σ_n (n/R)⁴ = ζ_R(−4) = 0 — show these vanish too
- Save as `compute.py`, output as `results.txt`

### Step 7: Write your research memo

Write `01-three-graviton-vertex.md` with:

```
## Summary
## Background and gap being addressed
## The y-integrals: closed-form results
   ### I_{+++}: table of cases
   ### I_{++-}, I_{+--}, I_{---}: selection rules
## Selection rules at the GS vertex
## UV behavior: mass-independence of J(m²)
## Assembly: proof of C_GS = 0
## Numerical verification
   ### Code snippets (key parts)
   ### Results table
## Gaps and residual assumptions
## Status: Proved / Partial / Requires further work
## Connection to Paper 10 Conjecture 1
## Proposed next step
```

**Aim for 500–700 lines.** This is the key computation for Paper 10 — it should be
complete enough to convert Conjecture 1 into Theorem 1.

---

## Honesty requirements

- If the y-integrals are NOT n-independent for the diagonal case, say so explicitly
  and characterize the n-dependence precisely
- If the UV behavior argument has gaps, label them clearly as Assumptions
- If the full proof goes through: state it as a theorem with a clear proof boundary
  (what is assumed, what is derived)
- Do not claim more than what the computation actually establishes
