# Paper 30: Navier-Stokes Attack Plan

*Date: 2026-04-13*
*Status: SCAFFOLD -- furthest from closure among all 7 Millennium vertices*

---

## Executive summary

Navier-Stokes is the hardest vertex in the programme graph. Unlike RH
(8/10, conditional on CCM), BSD (pipeline-validated), or YM (18/18
chain verified), NS has only 2/8 links proved and the critical gap --
routing a spectral gap to pointwise vorticity control -- has no clear
path. This document lays out two attack routes and identifies where
the PCA should strike first.

---

## Route A: Gradient-flow transfer (from YM)

### Strategy

Paper 8 (Yang-Mills) proved gradient-flow well-posedness via
Lemmas 1.1-1.5 and closed the 18-link chain through Balaban RG flow
(Links 15-17). The NS equation shares PDE structure with YM:

| Feature | Yang-Mills | Navier-Stokes |
|---------|-----------|---------------|
| PDE type | Second-order parabolic | Second-order parabolic |
| Constraint | Gauge invariance (d_A * F = 0) | Divergence-free (div u = 0) |
| Nonlinearity | Quadratic (A x F) | Quadratic (u . nabla u) |
| Energy | YM action functional | Kinetic energy (1/2) int |u|^2 |
| Spectral gap | Delta_0^KK > 0 (PROVED) | Same gap (inherited via KK) |
| Blowup criterion | Uhlenbeck compactness | BKM (int ||omega||_inf dt) |

### What transfers

- **Spectral gap:** Direct inheritance. The KK spectral gap is a
  property of the geometry (M^4 x S^1), not the field equations. Any
  field theory on this background sees the same gap. PROVED.

- **Energy estimates:** The 5D energy-momentum conservation (Killing
  symmetry of S^1) descends to 4D for any tensor field. The mechanism
  is the same for YM and NS. STRUCTURAL PARALLEL.

- **Parabolic regularity:** Short-time existence for both equations
  follows from the same Picard iteration / semigroup theory. Both are
  well-posed locally. STANDARD.

### What does NOT transfer

- **Gauge vs divergence-free:** YM gauge invariance lives on a compact
  Lie group (SU(N)); the divergence-free condition on NS is a linear
  constraint on R^3. The Uhlenbeck compactness theorem (gauge fixing
  in YM) has no NS analogue. This is not a minor detail -- it is where
  the YM proof uses the compactness of the gauge group essentially.

- **Vorticity stretching:** YM has no direct analogue of the vorticity
  stretching term omega . nabla u. In YM, the nonlinearity [A, F] is
  controlled by gauge covariance. In NS, the stretching term has no
  sign, no gauge symmetry, and no known spectral gap control. THIS IS
  THE WALL.

- **Balaban RG:** The Balaban renormalization group flow (Paper 8
  Links 15-17) exploits the lattice gauge structure of YM. NS on R^3
  has no lattice gauge structure. The Balaban machinery does not
  transfer.

### Verdict on Route A

Route A gives Link 4 (spectral gap) for free and provides structural
motivation for Links 3 and 6. It does NOT give Link 5 (BKM criterion).
The transfer is a scaffolding, not a proof.

---

## Route B: Fluid/gravity correspondence (from 5D Einstein)

### Strategy

Bhattacharyya-Hubeny-Minwalla-Rangamani (2008, arXiv:0712.2456) showed
that the dynamics of near-equilibrium black branes in AdS_5 maps to
the relativistic Navier-Stokes equations at leading order in the
gradient expansion. The programme's 5D geometry (M^4 x S^1, not AdS_5)
is different, but the structural mechanism is the same: long-wavelength
perturbations of a horizon satisfy the NS equations.

### The gradient expansion

At zeroth order: perfect fluid (Euler equations).
At first order: viscous corrections -> Navier-Stokes.
At second order: Burnett / Israel-Stewart terms.

The question: does the gradient expansion converge? If so, the 5D
Einstein equations rigorously contain the NS equations as a subsector.

### What this route gives

- **Link 2 (fluid/gravity dictionary):** If the BHMR construction can
  be made rigorous for M^4 x S^1, this link is closed. The formal
  expansion is well-established.

- **Link 6 (energy descent):** The 5D geometry has a Killing vector
  (S^1 translation). The associated conserved quantity descends to the
  4D energy. Energy dissipation (viscosity) arises from the horizon
  area theorem (entropy increase). This is the most physical route to
  the Leray-Hopf upgrade.

### What this route does NOT give

- **Link 5 (BKM criterion):** The fluid/gravity correspondence is a
  long-wavelength expansion. The BKM criterion requires pointwise
  control of vorticity at ALL scales, including UV. The gradient
  expansion breaks down precisely where BKM matters most. This route
  does not help with the wall.

- **Rigorous control:** The BHMR expansion is formal. Making it
  rigorous (controlling error terms, proving convergence) is itself an
  open problem. This is Link 2's gap.

### Verdict on Route B

Route B is the most physically motivated but mathematically weakest
route. It gives strong intuition (turbulence is gravitational in
origin) but does not touch the hard analysis.

---

## Route C (speculative): Direct spectral attack

### The idea

Bypass both YM transfer and fluid/gravity. Work directly with the
NS equations on R^3 and use the KK spectral gap as an external input.

Specifically: decompose the velocity field u into KK modes on S^1.
The zero mode is the 3D NS velocity. The massive modes (n >= 1) have
mass m_n = 2 pi n / R. The spectral gap is m_1 = 2 pi / R.

Claim: the massive modes provide a natural UV regularization. Integrating
them out gives an effective 3D theory with a UV cutoff at scale
Lambda ~ 1/R. The cutoff theory is globally regular (finite degrees of
freedom). Taking R -> 0 (decompactification) recovers 3D NS.

Problem: the limit R -> 0 is singular. The spectral gap goes to
infinity, but so does the number of modes below any fixed cutoff. This
is a renormalization problem, not a regularity problem. No clear path.

### Verdict on Route C

Speculative. Would require new ideas about the R -> 0 limit. Not
currently viable but worth recording.

---

## PCA target priority

If the Proof-Chain Adversarial system is deployed on Paper 30, it
should attack in this order:

### Priority 1: Link 5 (BKM criterion) -- THE WALL

This is the single bottleneck. Everything downstream is standard or
conditional once Link 5 is closed. The PCA should:

1. **Verify the spectral gap is insufficient alone.** Construct an
   explicit counterexample: a divergence-free vector field on T^3 with
   spectral gap Delta > 0 but unbounded vorticity stretching. If such
   an example exists, Route A is dead and the paper needs a fundamentally
   different approach.

2. **Search for additional structure.** What property of the KK
   embedding (beyond the spectral gap) could control vorticity
   stretching? Candidates: the KK constraint equations, the Bianchi
   identity in 5D, the dilaton equation of motion.

3. **Test the BHMR bound.** In the fluid/gravity framework, is there a
   geometric bound on vorticity? The dual statement would be: black
   brane horizons cannot develop arbitrarily sharp features. This is
   related to cosmic censorship.

### Priority 2: Link 3 (gradient-flow transfer) -- THE MAIN GAP

If Link 5 has a path, Link 3 becomes the next target:

1. **Formalize the PDE category.** Define the category of second-order
   parabolic systems with divergence-free constraint. Construct the
   functor from YM (on principal G-bundle) to NS (on R^3) explicitly.
   Identify what properties are preserved.

2. **Find the obstruction.** What breaks in the transfer? Is it the
   noncompactness of R^3 vs the compact gauge group? Is it the absence
   of gauge covariance? Identify the precise obstruction.

### Priority 3: Link 2 (fluid/gravity rigour) -- HARD BUT KNOWN

The rigorous fluid/gravity dictionary is a known open problem in
mathematical general relativity. This is not specific to the programme.

1. **Literature search.** Has anyone proved convergence of the BHMR
   gradient expansion? Check Hubeny-Rangamani reviews, Romatschke
   resurgence programme, Heller-Spalinski attractors.

2. **Error bounds.** Can the BHMR expansion be bounded at finite order?
   Even a rigorous first-order result (5D Einstein -> NS + bounded
   error) would close Link 2.

---

## Programme graph connections

### Edges to other vertices

```
Paper 1 (QG5D)  ---[KK geometry]--->  Paper 30 (NS)
                                        ^
Paper 8 (YM)    ---[spectral gap]------/
                ---[GF transfer]------/
                ---[Appendix L]------/
```

- **Paper 1 -> Paper 30:** The 5D geometry (M^4 x S^1, metric ansatz,
  dilaton dynamics) is the foundation. NS lives on the 4D slice.

- **Paper 8 -> Paper 30 (strong):** Three edges. (1) Spectral gap
  (PROVED, transfers directly). (2) Gradient-flow machinery (structural
  parallel, transfer OPEN). (3) Appendix L (the NS structural parallel
  section, written explicitly to lay groundwork for Paper 30).

- **Paper 30 -> Paper 8 (weak):** If NS regularity is proved via KK
  spectral gap, it provides independent evidence for the physical
  relevance of the KK framework. Soft edge.

### No direct edges to

- Paper 13 (RH): No structural connection. RH is number-theoretic;
  NS is PDE/geometry. The only shared infrastructure is the programme
  framework itself.

- Paper 26 (BSD): No structural connection.

- Paper 28 (P vs NP): No structural connection.

---

## Honest assessment

### Where NS stands among the 7 Millennium vertices

| Vertex | Paper | Links proved | Confidence | Status |
|--------|-------|-------------|------------|--------|
| RH | 13 | 6/6 | 8/10 | Conditional on CCM |
| YM | 8 | 18/18 | 9/10 | Chain verified |
| BSD | 26 | 11/11 | 8/10 | Pipeline validated |
| P vs NP | 28 | TBD | 6/10 | Spectral-geometric-information trinity |
| Hodge | TBD | TBD | TBD | Not started |
| Poincare | -- | -- | 10/10 | Solved (Perelman 2003) |
| **NS** | **30** | **2/8** | **2/10** | **Scaffold only** |

NS is the furthest from closure. The gap is not incremental -- it is
structural. The spectral gap (the programme's main weapon) is
necessary but not sufficient for NS regularity. The vorticity
stretching term has no known spectral gap control. This is not a
detail to be fixed; it is the essence of the Navier-Stokes problem.

### What would change the assessment

1. **A spectral gap -> BKM theorem** (Link 5 closed): Jumps to 6/10.
   All downstream links become standard.

2. **Rigorous fluid/gravity** (Link 2 closed): Jumps to 4/10.
   Provides the embedding but still needs Link 5.

3. **Both Link 2 and Link 5** closed: Jumps to 8/10.
   Comparable to RH and BSD.

4. **A counterexample to Link 5** (spectral gap does not control BKM):
   The current architecture is dead. Would need Route C or a
   fundamentally new idea.

### Timeline estimate

- Links 1, 4: DONE (inherited).
- Link 2: 6-12 months (literature review + rigorous error bounds).
- Link 3: 6-12 months (PDE category theory, functor construction).
- Link 5: UNKNOWN. This is a hard open problem. Could be 1 year or
  never. No honest estimate possible.
- Links 6, 7: 1-3 months each (standard once Link 5 is closed).
- Link 8: Immediate (composition).

### Bottom line

Paper 30 is a bet that the KK spectral gap, which proved sufficient
for Yang-Mills, extends to Navier-Stokes. The structural parallels
are real but the critical link (spectral gap -> vorticity control)
is genuinely open. This paper should be written honestly as a
conditional result: "NS regularity follows IF the gradient-flow
transfer is rigorous AND the spectral gap controls BKM." The
programme's contribution is the architecture and the spectral gap
infrastructure from Paper 8. The hard analysis is future work.

---

## Next actions

1. Write Paper 30 Appendix A: detailed comparison of YM and NS
   PDE structure (what transfers, what doesn't).
2. Literature review: rigorous fluid/gravity results post-BHMR 2008.
3. Construct explicit test: spectral gap + BKM on T^3 (toy model).
4. Draft Link 5 attack: try Sobolev embedding + spectral gap +
   Gronwall to bound ||omega||_inf. Identify where it fails.
5. PCA brief: write the Verification Cascade brief for NS
   (following YM/RH/BSD template).

---

## Revision history

- 2026-04-13: Initial attack plan. Two routes analyzed. PCA priorities set.
