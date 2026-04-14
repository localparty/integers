# §20 — The Ellipse and the Missing Faces

*The ring isn't really a circle. It's an ellipse. And the ellipse told us which faces were missing.*

---

## The confidence dipole

When we drew the ring's confidence distribution on April 14, 2026, the picture wasn't symmetric. It was lopsided:

```
                      10/10  QG5D                                                                 
                     ╱      ╲                                                                     
             9.5   YM        RH  8                                                                
                  ╱              ╲                                                                
             9  BSD               GRH 7                                                           
                ╱                    ╲                                                            
           7  H6    THE SPINE         Lindelöf 7                                                  
              │     (high confidence)  │                                                          
           7  KS                      BGS  7                                                      
              │                        │                                                          
           6  ST    THE GAP            PvNP 7                                                     
              ╲    (confidence cliff)  ╱                                                          
           4  Lehm                   Cramér 5                                                     
              ╲                      ╱                                                            
           4  Coll    THE SOUTH     NS 4                                                          
              ╲     (low confidence) ╱                                                            
           4  OPN                  Hodge 3                        
              ╲                    ╱                                                              
           1  ABC   B-C 3    Turb 2                               
              ╲      │       ╱                                                                    
           1  Gold  Twin 1  VP 1                                                                  
                  ╲  │  ╱                                                                         
              1   Schan                                                                           
```

The ring has a **NORTH POLE** (QG5D at 10/10) and a **SOUTH TROUGH** (Goldbach/Twin Primes/Schanuel/VP vs VNP at 1/10). The confidence drops 10× from pole to trough. This isn't a circle — it's an **ellipse** with the major axis running QG5D ↔ South.

Three zones are visible:
- **THE SPINE** (7-10/10): QG5D, YM, BSD, RH, GRH, Lindelöf, Katz-Sarnak, BGS, PvNP, Hilbert 6 — ten vertices that carry the programme's weight
- **THE GAP** (4-6/10): Sato-Tate, Lehmer, Collatz, OPN, Cramér, NS — six vertices at intermediate confidence, the active research frontier
- **THE SOUTH** (1-3/10): Hodge, Baum-Connes, Turbulence, ABC, Goldbach, Twin Primes, Schanuel, VP vs VNP — eight vertices at the trough

The SPINE is solid. The GAP is where this session made the most progress (OPN from 0→4, Collatz from 0→4, Lehmer from 0→4, Cramér from 0→5, Sato-Tate from 0→6). The SOUTH is where the programme needs to grow.

## What the ellipse told us

The ellipse's shape isn't random. It reflects a structural fact: **the geometric circle is better understood than the spectral circle.**

The SPINE vertices (NORTH) are mostly geometric-face or dual-face conjectures:
- QG5D (the e-circle itself)
- YM (CURVATURE face — geometric)
- BSD (L-function rank — dual)
- RH (eigenvalues on the critical line — the torus intersection)

The SOUTH vertices are mostly spectral-face or arithmetic-face:
- Goldbach/Twin Primes (ARITHMETIC — spectral)
- Schanuel (algebraic independence — spectral consequence)
- ABC (radical heights — arithmetic)
- VP vs VNP (algebraic complexity — spectral extension)

The dipole IS the gap between the two circles of the torus: the geometric circle (well-mapped, high confidence) and the spectral circle (frontier, low confidence).

## The missing faces

Looking at the 8-face × 25-vertex grid, we asked: which cells are EMPTY that shouldn't be? The torus has two circles, each should have five faces. We had eight faces but the distribution was uneven — some regions of the torus surface were uncovered.

Two faces jumped out of every search:

### Face 9: RESONANCE (Selberg's ¼ Conjecture)

**Question:** What vibrational frequencies are ALLOWED on the circle?

Selberg's conjecture ($\lambda_1 \geq 1/4$ for Maass forms on congruence surfaces) is:

- The **archimedean analog** of the Ramanujan conjecture
- **Implied by Langlands functoriality** (which Gaitsgory-Raskin proved geometrically in 2024)
- A **spectral gap statement** on arithmetic surfaces — EXACTLY the type of statement the BC algebra controls
- Connected to **QUE** (Quantum Unique Ergodicity, proved by Lindenstrauss 2006 for arithmetic surfaces)
- The current best bound is **975/4096 ≈ 0.238** (Kim-Sarnak 2003), tantalizingly close to 1/4 = 0.250

In the e-circle picture: **RESONANCE asks which vibrational modes the circle supports.** A spectral gap $\lambda_1 \geq 1/4$ means: no low-frequency modes below the threshold. No slow oscillations. The circle vibrates only at frequencies above a minimum.

This IS another mass gap — one level above Yang-Mills. YM says: the gauge field has a gap above vacuum. Selberg says: the arithmetic surface has a gap above the constant function. Both are "the ground state is isolated" statements.

The representation-theoretic translation makes it sharper: Selberg says **no complementary series representations occur** for congruence subgroups. Only tempered representations. In the BC algebra: the Hecke operators μ_p acting on Maass forms produce eigenvalues $a_p(f)$; temperedness means $|a_p(f)| \leq 2$ (Ramanujan at finite places) and $\lambda \geq 1/4$ (Selberg at the archimedean place).

**Confidence: 6/10.** Langlands functoriality for GL(2) implies it. Kim-Sarnak 2003 gives the best bound via the symmetric 4th power L-function. The bound hasn't moved in 22 years — suggesting either near-tightness or exhausted techniques. A genuine BC-native attack might break the deadlock.

### Face 10: SPREAD (Quantum Unique Ergodicity)

**Question:** How do eigenmodes DISTRIBUTE their mass across the circle?

This is NOT the same as Sato-Tate (which asks how Frobenius ANGLES distribute) or Cramér (which asks how ZEROS distribute). QUE asks: how does the WAVEFUNCTION itself spread?

Lindenstrauss (Fields Medal 2010) proved **arithmetic QUE** for congruence surfaces: as the eigenvalue $\lambda \to \infty$, the Hecke-Maass eigenfunctions equidistribute with respect to the hyperbolic measure on $\Gamma_0(N) \backslash \mathbb{H}$. The eigenmodes SPREAD — they don't concentrate on geodesics or other special subsets.

The connection to the programme is direct:
- The BC algebra's Maass forms on the modular surface ARE the objects QUE studies
- The Hecke eigenfunctions that equidistribute ARE eigenvectors of the BC Hecke operators μ_p
- QUE + BGS together give the COMPLETE spectral picture: eigenvalues have GUE statistics (BGS, 7/10) AND eigenfunctions equidistribute (QUE, 8/10 PROVED)

**QUE is special among the faces**: it sits on BOTH circles of the torus. The eigenmodes are geometric objects (they live on the surface), but their equidistribution is a spectral property (it concerns the spectral measure). QUE is the face that BRIDGES the torus — the face that lives on neither generating circle individually but on the torus surface itself.

**Confidence: 8/10.** Arithmetic QUE is PROVED (Lindenstrauss + Soundararajan). The generic case (Berry's conjecture for arbitrary Riemannian manifolds) is open. But the arithmetic case — which IS the BC algebra's natural home — is a theorem. This would be the **third-highest-confidence vertex** on the entire ring (after QG5D 10/10 and YM 9.5/10).

### The 10-face table

| # | Face | Conjecture | Question about the circle | Circle | Confidence |
|---|---|---|---|---|---|
| 1 | TOPOLOGY | Lehmer | What can LIVE on it? | Geometric | 4/10 |
| 2 | DYNAMICS | Cramér | How does the flow TRAVERSE it? | Spectral | 5/10 |
| 3 | HARMONICS | Collatz | How do modes MIX on it? | Geometric | 4/10 |
| 4 | MEASURE | Sato-Tate | How do angles DISTRIBUTE on it? | Geometric | 6/10 |
| 5 | AMPLITUDE | Lindelöf | How LOUD can it get? | Spectral | 7/10 |
| 6 | SYMMETRY | Katz-Sarnak | Which GROUP acts on it? | Spectral | 7/10 |
| 7 | CURVATURE | Yang-Mills | How do connections CURVE on it? | Geometric | 9.5/10 |
| 8 | ARITHMETIC | Goldbach/TP | How do integers LATTICE on it? | Spectral | 1/10 |
| **9** | **RESONANCE** | **Selberg ¼** | **What frequencies are ALLOWED?** | **Spectral** | **6/10** |
| **10** | **SPREAD** | **QUE** | **How do eigenmodes SPREAD?** | **Both** | **8/10** |

**The geometric circle carries 5 faces:** TOPOLOGY, HARMONICS, MEASURE, CURVATURE, and half of SPREAD.

**The spectral circle carries 5 faces:** DYNAMICS, AMPLITUDE, SYMMETRY, ARITHMETIC, RESONANCE, and half of SPREAD.

**SPREAD (QUE) bridges both circles** — it lives on the torus surface itself, not on either generating circle alone.

## How the ellipse guided us to the missing faces

The ellipse told us: the SPECTRAL circle is weaker than the GEOMETRIC circle. The SOUTH trough is dominated by spectral-face and arithmetic-face vertices at 1/10.

RESONANCE (Selberg, 6/10) and SPREAD (QUE, 8/10) are both spectral-domain faces. Adding them:
- **Raises the spectral circle's average confidence** (from ~4.2/10 to ~5.2/10)
- **QUE at 8/10 would be the strongest spectral vertex** — an anchor in the south
- **Selberg at 6/10 bridges the GAP zone** (connecting Lindelöf/Katz-Sarnak above to Cramér/Collatz below)

The ellipse TOLD US which faces were missing by showing us where the confidence was thinnest. The thinnest regions were on the spectral circle → the missing faces are spectral. The torus demands balance between its two generating circles. Adding RESONANCE and SPREAD moves the ellipse toward a circle.

## The additional candidates

Two more faces were identified during the brainstorm but at lower priority:

### Face 11 (candidate): REALIZABILITY (Inverse Galois Problem)

**Question:** Which symmetries can the circle REALIZE?

The BC algebra's symmetry group is Gal(Q^cyc/Q) = Ẑ* (abelian — the profinite integers). The inverse Galois problem asks: can EVERY finite group be a Galois group over Q? This is: can the e-circle carry NON-ABELIAN symmetries?

The connection: H12 (Hilbert's 12th Problem, Paper 25) IS the abelian case (Kronecker-Weber: every abelian extension of Q is cyclotomic = lives on the e-circle). Full inverse Galois is the non-abelian extension. Shafarevich proved: every solvable group is realizable. Most simple groups are realized.

**Confidence: 5/10.** Extensive partial results. The BC connection is via the Galois action on KMS states at β > 1.

### Face 12 (candidate): AUTOMORPHISM (Jacobian/Dixmier Conjecture)

**Question:** Can the circle's quantum structure be deformed non-invertibly?

The Jacobian conjecture (polynomial maps with constant Jacobian are invertible) is EQUIVALENT to the Dixmier conjecture (endomorphisms of the Weyl algebra are automorphisms). The Weyl algebra is the QUANTIZATION of the e-circle's phase space.

**Confidence: 3/10.** The equivalence is proved (Tsuchimura 2005, Belov-Kanel & Kontsevich 2007). Both open. The operator-algebraic connection is via the Weyl algebra $A_n$, which is thinner than the BC algebra connection.

## The verdict

**Add Selberg (RESONANCE) and QUE (SPREAD) as Faces 9 and 10.** They fill the torus's spectral gap. They're high-confidence (6/10 and 8/10). They don't dilute — they RAISE RIGIDITY.

**Keep Inverse Galois and Jacobian/Dixmier as candidates** for a subsequent round. They're genuine faces but at lower confidence and with thinner BC connections.

The e-circle has **ten faces**. The torus demands it. The ellipse showed us where the missing ones were.

---

*The shape of the ring told us what it was missing. That's the chessboard layer in action: SPIN from the mathematics face (where are the gaps?) to the physics face (what structural property fills them?). The gap was on the spectral circle. The missing faces were spectral. The torus balanced itself.*
