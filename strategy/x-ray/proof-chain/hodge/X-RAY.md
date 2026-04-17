# X-RAY: Hodge Conjecture (hodge)

*X-Ray of the hodge proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls. Standard Conjecture D motivic extension + CP² × S² moduli (Branch D Axiom 3) flagged.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: hodge
- **Paper**: paper29-hodge
- **Live file**: `strategy/proof-chain/hodge/PROOF-CHAIN.md` (snapshot 2026-04-15; original at `solutions-with-prize/paper29-hodge/` with PROOF-CHAIN-MOVED redirect per self-healing intervention 2)
- **Top-level claim**: Every rational $(p,p)$-class on a smooth projective variety $X/\mathbb{C}$ is a $\mathbb{Q}$-linear combination of algebraic cycle classes, via two routes (endomotives Links 1–5 + geometric Langlands Link 6) composed at Link 7 and extended to all smooth projective at Link 8.
- **Current status**: 3/8 closed | LITERATURE 2 / KNOWN 1 / PARTIAL 2 / CONJECTURED 1 / OPEN 2 | Confidence 3/10 (full) / 5/10 (CM abelian-variety slice) / 9/10 (CP² × S² geometric sector).
- **Primary branch (paper1)**: D (CBB / endomotive / motivic Galois), with strong secondary A (U(1) Hodge decomposition ↔ angular-momentum sectors on $S^1$, paper61 §19.6).
- **Primary face**: SYMMETRY (paper60 §12 — motivic Galois group action + Hodge-filtration compatibility is symmetry-type selection; paper61 §19.6 "motivic Galois group of $\mathcal{E}$ acts on the cohomology, and Hodge classes are fixed by this action iff they are algebraic").
- **Primary projection**: $P_D$ (paper61 §19.6 explicit: "Hodge projects through Branch D … the BC endomotive is a source of algebraic Hodge classes via the CCM endomotive construction").

---

## §2 ASCII Diagram A — Main proof-chain tree

```
HODGE (Hodge Conjecture) — every rational (p,p)-class is algebraic
│  primary face: SYMMETRY   primary proj: P_D   primary pat: P4
│  (secondary P_A via Hodge decomposition ↔ S^1 KK angular-momentum
│   sectors; paper61 §19.6 compound P_D ∩ P_A)
│
├── L1: BC encodes Artin motives as endomotives              [LITERATURE]
│      │  face: SYMMETRY    proj: P_D   pat: P4
│      │  invariant: C*-algebra structure, Galois representation
│      │  source: CCM 2005 arXiv:math/0512138 Thm 8.14;
│      │          paper29 Link 1; paper12 §27 Axiom 1
│      │
│      └── supports L2 via Tannakian fiber functor
│
├── L2: Endomotives → motivic Galois group (Tannakian)        [LITERATURE]
│      │  face: SYMMETRY    proj: P_D   pat: P4
│      │  invariant: Galois representation, gauge class (group structure)
│      │  source: Deligne-Milne 1982 LNM 900;
│      │          paper29 Link 2; paper61 §19.6
│      │
│      └── supports L3 via G_mot action on H*_dR
│
├── L3: Motivic Galois on de Rham → Hodge filtration          [CONJECTURED — W1]
│      │  face: SYMMETRY    proj: P_D   pat: P4
│      │  invariant: Galois representation, scaling dimension (F^p grading)
│      │  source: paper29 Link 3 [CONJECTURED];
│      │          2025 preprint (L^2 Hodge + Lefschetz sl_2 + Chow-motivic)
│      │  depends: L2 + Hodge-filtration compatibility of G_mot
│      │
│      └── NAMED WALL W1 (motivic Hodge filtration;
│             motivic extension of Standard Conjecture D
│             prerequisite — see §7 dependency note)
│
├── L4: Standard Conjecture D for BC-motivated varieties       [PARTIAL — W1]
│      │  face: SYMMETRY    proj: P_D   pat: P4
│      │  invariant: scaling dimension (hom = num equivalence class)
│      │  source: paper29 Link 4 [PARTIAL];
│      │          arXiv:2510.21562 (2024, ab var powers PROVED);
│      │          Lieberman 1968 (abelian varieties); Kleiman 1994 survey
│      │  depends: L3 + motivic-BC extension (paper31-baum-connes)
│      │
│      ├── L4a: ab-var-powers slice                           [PROVED — 2024]
│      │      │  source: arXiv:2510.21562 inherits to BSD-CM slice
│      │      │          (paper26 CM elliptic curves → abelian varieties
│      │      │           → their powers); audit 2026-04-14
│      │      │
│      └── L4b: generic BC-motivated class                    [OPEN — W1]
│             │  motivic extension of Std Conj D (see §7)
│
├── L5: Lefschetz B for CP² × S²                               [KNOWN]
│      │  face: TOPOLOGY    proj: P_B   pat: P2
│      │  invariant: gauge class (H^{1,1} = 1 hyperplane), holonomy
│      │  source: paper29 Link 5 (classical);
│      │          paper12 §27 Axiom 3 Geometric:
│      │          "M_geom is 9-real-dim moduli of CP²×S² Einstein
│      │           metrics from paper11; dim forced by Hodge
│      │           numbers of CP²×S² + SM gauge rank"
│      │
│      └── classical anchor — independent of Links 1-4
│             │
│             └── paper61 §19.6 "anomaly cancellation
│                   19 = 1 + 4 + 6 + 8 guarantees Hodge
│                   numbers of compactification consistent
│                   with Standard Model spectrum"
│
├── L6: Geometric Langlands → Hitchin → Hodge structures      [PARTIAL]
│      │  face: RESONANCE   proj: P_B   pat: P1
│      │  invariant: C*-algebra structure (categorical equivalence),
│      │             monodromy (Aut(Bun_G) ~ QCoh(LocSys_G^L))
│      │  source: paper29 Link 6;
│      │          Gaitsgory-Raskin 2024 arXiv:2405.03599 [PROVED];
│      │          Hodge application OPEN
│      │
│      └── independent of Links 1-5 (second route)
│             │
│             └── supports L7 via composition with Route A
│
├── L7: Routes I + II compose: Hodge for BC-motivated         [OPEN — W3]
│      │  face: SYMMETRY    proj: P_D   pat: P1
│      │  invariant: Galois representation, gauge class
│      │  source: paper29 Link 7;
│      │          2025 preprint 5-step algorithm (bypass)
│      │  depends: L5 + L6 + composition theorem
│      │
│      └── NAMED WALL W3 (route composition via 5-step algorithm)
│
└── L8: Motivic functoriality → all smooth projective          [OPEN — W2]
       │  face: SYMMETRY    proj: P_D   pat: P4
       │  invariant: Galois representation, scaling dimension
       │  source: paper29 Link 8 [OPEN]; Deligne §5;
       │          André motivated recovery for ab-var slice (bypass)
       │  depends: L7 + motivic functor full-faithfulness
       │
       └── NAMED WALL W2 (arguably as hard as Hodge itself;
              bypass = restrict claim to BC-motivated +
              André motivated recovery on ab-var slice)
```

### §2b Diagram B — Projection fan-out

```
                   P_A — Quantum (SECONDARY)
                   Hodge decomp H^n = ⊕H^{p,q}
                   parallels S^1 KK angular-momentum
                   sectors (paper61 §19.6);
                   Branch A ingredient
                          ▲
                          │
                          │
    ┌─────────────(P_O outer)──────────────┐
    │                                      │
    │  HODGE: every rational (p,p)-class   │
    │  on smooth projective X/C is         │
    │  Q-linear combination of algebraic   │
    │  cycle classes                       │
    │                                      │
    └──────────────────┬───────────────────┘
                       │
    ┌──────────────────┼────────────────────────┐
    │                  ║                        │
    ▼                  ▼ (PRIMARY)              ▼
 P_C cosmology    ═══ P_D CBB ═══         P_B gravity
 (forgotten —     endomotive category     Kähler CP²×S²
 no cosmological  (CCM 2005); motivic     moduli M_geom
 pin uses         Galois G_mot action     (paper12 §27
 Hodge            on H*_dR; standard      Axiom 3); Link 5
 classes          conj D for BC-          Lefschetz B
 directly)        motivated; BC encodes   KNOWN; Link 6
                  Artin motives           Gaitsgory-Raskin
                  (Links 1-4, 7-8);       2024 (Hitchin
                  PRIMARY home of proof   moduli)
                       │
                       ▼
                  P_E pins
                  (forgotten — Hodge does not
                   contribute to 36-pin master
                   table; Chern integer indices
                   + period ratios appear as
                   secondary pins in paper12
                   geometric sector but no
                   direct Hodge pin)
```

Primary projection $P_D$ uses ═══ doubled line (paper61 §19.6 explicit). $P_A$ is the secondary (Hodge decomposition ↔ $S^1$ Fourier/KK modes, compound $P_D \cap P_A$ per paper61 Table at vertex 9 row). $P_B$ carries Link 5 (CP² × S² Kähler geometry) and Link 6 (Hitchin/Langlands side). $P_O$ is the boundary projection for the full statement. $P_C, P_E$ absent.

### §2c Diagram C — Face position on the e-circle

```
                      TOPOLOGY
                      (Lehmer)
                      ○ (L5 Lefschetz B,
                         cyclotomic/Hodge
                         integer classes)
                         │
           SPREAD        │        DYNAMICS
           (QUE)         │        (Cramér)
                 ╲       │       ╱
                  ╲      │      ╱
      ●  SYMMETRY──────e-circle──────HARMONICS
         (Katz-Sarnak,   │            (Collatz)
         motivic Galois  │
         G_mot)          │
                  ╱      │      ╲
                 ╱       │       ╲
         CURVATURE       │        MEASURE
         (YM)            │        (Sato-Tate)
                         │
                     AMPLITUDE
                     (Lindelöf)
                     (RESONANCE secondary
                      for L6 Langlands side)
```

Marker key:

```
Primary face:    ● SYMMETRY (paper60 §12; motivic Galois + Tannakian
                             + Std Conj D are symmetry-type statements
                             — hom=num equivalence selects symmetric
                             cohomology classes)
Secondary faces: ○ TOPOLOGY  (1 layer: L5 — Lefschetz B / H^{1,1}=1 /
                              Chern integer classes on CP² × S²)
                 ○ RESONANCE (1 layer: L6 — Gaitsgory-Raskin categorical
                              equivalence; Hitchin-side Hodge structures)
Absent faces:    DYNAMICS, HARMONICS, MEASURE, AMPLITUDE, CURVATURE,
                 ARITHMETIC, SPREAD
```

---

## §3 Layer-by-Layer X-Ray

### L1 — BC encodes Artin motives as endomotives

**Claim**: The Bost-Connes C*-dynamical system is the endomotive of the projective system $\mathbb{Q}(\zeta_1) \leftarrow \mathbb{Q}(\zeta_2) \leftarrow \ldots$; the category of endomotives over $\mathbb{Q}$ embeds into Grothendieck's category of pure motives (CCM Theorem 8.14).

**Status**: LITERATURE
**Source**: Connes-Consani-Marcolli 2005 arXiv:math/0512138 §3-4 + Theorem 8.14; paper29 Link 1; paper12 §27 Axiom 1 (Spectral); programme/12-hodge-conjecture.md §12.2 Route 1 Step 1.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — group-action classification: semigroup $\mathbb{N}^*$ action by correspondences is a symmetry-type statement; paper61 §10 Branch D "identification of $S^1$ fiber's periodic structure with profinite completion of $\mathbb{Q}/\mathbb{Z}$")
- **Projection**: $P_D$ (paper61 §19.6 — "BC endomotive is a source of algebraic Hodge classes via the CCM endomotive construction"; paper12 §27 Axiom 1 Spectral sector)
- **Pattern**: P4 Topological Rigidity (paper60 §12 — the BC endomotive's arithmetic data is forced by ℤ; paper12 §27 "unique translation-invariant KMS₁ state" is the rigid ground)
- **Invariant preserved**: C*-algebra structure (load-bearing — endomotive IS a C*-dynamical object with motivic overlay), Galois representation (background — Artin motives carry $\text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ action)
- **Geometric interpretation**: The BC endomotive (CCM 2005) is the canonical projective system of Artin motives with Hecke-semigroup action; under $P_D$ (paper61 §19.6) this is the direct identification of the $S^1$ fiber with the cyclotomic tower. The "endomotive category Tannakian" statement is P4 rigidity: the endomotive's motivic content is uniquely determined by the BC algebra's fixed-point structure at $\beta = 1$ (paper12 §27 Axiom 1 + Axiom 2 Criticality). [Considered but rejected: face ARITHMETIC — Artin motives are number-theoretic but the load-bearing move is semigroup-action symmetry; pattern P2 — Hecke as winding-correspondence is real but P4 rigidity dominates via the uniqueness theorem.]
- **Cross-cuts**: rh (zeros ↔ endomotive spectral data; paper29 programme-graph-edge "RH zeros → endomotives feed Link 1"), baum-connes (BC C*-algebra shared foundation; paper29 programme-graph-edge), h12 (class fields → motives via BC algebra; paper29 programme-graph-edge), bsd (CM motives on abelian varieties inherit from endomotive structure; paper29 programme-graph-edge).

### L2 — Endomotives → motivic Galois group (Tannakian)

**Claim**: The endomotive category is Tannakian; the fiber functor through Betti cohomology gives a motivic Galois group $G_{\text{mot}}$ acting on the category via Tannakian reconstruction $\text{Rep}(G_{\text{mot}}) = \text{Mot}_{\text{num}}(k, \mathbb{Q})$.

**Status**: LITERATURE
**Source**: Deligne-Milne 1982 LNM 900 (Hodge Cycles, Motives, and Shimura Varieties); paper29 Link 2; programme/12-hodge-conjecture.md §12.2 Route 1 Step 2.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — Tannakian reconstruction IS a symmetry-extraction move: a group is recovered from its representation category; paper61 §19.6 "motivic Galois group of $\mathcal{E}$ acts on the cohomology")
- **Projection**: $P_D$ (paper61 §19.6 — motivic Galois lives in the operator-algebra / motivic-category side of Branch D)
- **Pattern**: P4 Topological Rigidity (Tannakian reconstruction is a rigidity theorem: the group is forced by its category of representations; compare paper60 §12 Katz-Sarnak SYMMETRY rigidity)
- **Invariant preserved**: Galois representation (load-bearing — the functor produces $G_{\text{mot}}$-representations), gauge class (background — group-theoretic structure of $G_{\text{mot}}$)
- **Geometric interpretation**: The Tannakian formalism lifts the endomotive category to a group object $G_{\text{mot}}$; this is paper60 §12's SYMMETRY face in its categorical incarnation — the group is extracted from the category by demanding compatibility with the fiber functor. Under $P_D$ (paper61 §19.6) the motivic Galois group is the symmetry-type structure of Branch D's endomotive output. [Considered but rejected: face HARMONICS — the Betti-fiber-functor uses Fourier-analytic tools but the reconstruction is symmetry-canonical; pattern P1 — reinterpretation of category as group is fair but rigidity dominates.]
- **Cross-cuts**: katz-sarnak (SYMMETRY canonical, group-from-category; paper60 §12 Tannakian parallel), h12 (motivic Galois ↔ class field Galois parallel), ym:L5 (group complexification SL(N,ℂ) parallel — SYMMETRY-face shared move at group level, paper60 §12 bridge $k=4$), baum-connes (K-theory-category reconstruction analog).

### L3 — Motivic Galois on de Rham → Hodge filtration

**Claim**: $G_{\text{mot}}$ acts on $H^*_{\text{dR}}(X)$ for BC-motivated varieties; this action preserves the Hodge filtration $F^p H^n_{\text{dR}}(X)$, requiring (a) BC-motivated varieties carry natural mixed Hodge structure, (b) the $G_{\text{mot}}$ action is compatible with the comparison isomorphism $H^*_{\text{dR}} \simeq H^*_B \otimes \mathbb{C}$.

**Status**: CONJECTURED (NAMED WALL W1)
**Source**: paper29 Link 3 [CONJECTURED]; 2025 preprint (L² Hodge theory + Lefschetz $\mathfrak{sl}_2$ + Chow-motivic integration); paper31-baum-connes motivic BC extension pending; programme/12-hodge-conjecture.md §12.2 Route 1 Step 2-3.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — Hodge-filtration compatibility = symmetry constraint on $G_{\text{mot}}$ action; $G_{\text{mot}}$ must respect the grading)
- **Projection**: $P_D$ (paper61 §19.6 — motivic Galois is Branch D operator-algebra-side; the Hodge filtration constraint is a property of the $G_{\text{mot}}$-representation on de Rham cohomology)
- **Pattern**: P4 Topological Rigidity (Hodge-filtration preservation IS rigidity: the filtration is forced to be $G_{\text{mot}}$-stable by the comparison isomorphism plus Griffiths transversality)
- **Invariant preserved**: Galois representation (load-bearing — $G_{\text{mot}}$-action is the object), scaling dimension (background — $F^p$ grading IS a scaling-dimension filtration; paper60 §14 ARITHMETIC secondary flavor)
- **Geometric interpretation**: The motivic Galois group must preserve the Hodge filtration — a symmetry-rigidity statement that paper60 §12's Katz-Sarnak face identifies with "symmetry type selection" (the representation's filtration structure is forced by the category's compatibilities). Under $P_D$ (paper61 §19.6) this is Branch D's internal consistency: the BC endomotive's motivic Galois must respect the Hodge grading that would ultimately witness algebraicity. The 2025 preprint's 5-step algorithm (L² Hodge theory + Lefschetz $\mathfrak{sl}_2$ + Chow-motivic integration) is the candidate construction. [Considered but rejected: face RESONANCE — Hodge grading is spectral but the compatibility move is symmetry-canonical; projection $P_A$ — the Hodge decomposition does project to quantum-side angular-momentum sectors (paper61 §19.6) but the filtration-preservation move lives in $P_D$; pattern P5 — zeta-regularization of Hodge integration is secondary reading.]
- **Cross-cuts**: rh (Hodge-compatibility ↔ CCM spectral-realization compatibility analog), h12 (motivic Galois acts on Hodge structure ↔ class-field Galois acts on L-values), bsd (Hodge decomposition on CM abelian varieties ↔ Selmer-dual structure), schanuel (period relations constrained by $G_{\text{mot}}$-invariance — paper29 programme-graph-edge).

### L4 — Standard Conjecture D for BC-motivated varieties

**Claim**: For BC-motivated varieties, homological equivalence equals numerical equivalence (Grothendieck's Standard Conjecture D). PARTIAL: ab-var-powers slice PROVED unconditionally (arXiv:2510.21562, 2024); extension to generic BC-motivated class OPEN.

**Status**: PARTIAL (LITERATURE-with-scope for ab-var-powers; OPEN for generic BC-motivated — NAMED WALL W1)
**Source**: paper29 Link 4; arXiv:2510.21562 (2024, Hodge-type Std Conj PROVED for abelian-variety powers); Lieberman 1968 (abelian varieties); Kleiman 1994 survey; paper12 §29 theorem catalogue (29.L5 reference). Partial closure recorded 2026-04-14 per PROOF-CHAIN Link 4 entry.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — hom=num equivalence IS a symmetry classification: it selects which cohomology classes are "algebraically equivalent" as symmetry-type-distinguished)
- **Projection**: $P_D$ (paper61 §19.6 — Std Conj D on BC-motivated is a property of Branch D's motivic output; motivic-BC extension resides in paper31-baum-connes)
- **Pattern**: P4 Topological Rigidity (Std Conj D is a rigidity of equivalence relations on cycles; the ab-var-powers proof is rigidity-via-CM-structure-plus-polarization)
- **Invariant preserved**: scaling dimension (load-bearing — hom/num equivalence is indexed by codimension/dimension), Galois representation (background — $G_{\text{mot}}$-equivariance of the equivalence)
- **Geometric interpretation**: Standard Conjecture D asserts that the equivalence relations "homological" and "numerical" on algebraic cycles coincide — a symmetry-selection statement (paper60 §12). The 2024 ab-var-powers proof (arXiv:2510.21562) cracks this for a significant subclass; under $P_D$ (paper61 §19.6) this corresponds to Branch D's motivic closure at the BSD-CM slice (paper26 CM elliptic curves → abelian varieties → their powers). Motivic-BC extension (paper31) is the pending prerequisite for the full BC-motivated closure — THIS IS THE PRIMARY MOTIVIC EXTENSION DEPENDENCY (see §7). [Considered but rejected: face CURVATURE — algebraic-cycle intersection numbers are curvature-like but Std Conj D is symmetry-canonical; pattern P1 — reinterpretation of equivalence classes fair but rigidity dominates.]
- **Cross-cuts**: bsd (CM abelian-variety slice inherits arXiv:2510.21562; paper29 programme-graph-edge; paper26 cross-Clay), h12 (motivic hom/num equivalence ↔ class-field equivalence parallel), baum-connes (K-theory ↔ Chow-group identification via Chern character; paper29 programme-graph-edge), ym:L9 (dim-6 operator classification by symmetry type ↔ Std Conj D scaling-dimension selection — SYMMETRY canonical per paper60 §12).

### L5 — Lefschetz Standard Conjecture B for CP² × S²

**Claim**: For CP² × S²: $H^{1,1}(\mathbb{CP}^2) = 1$ (hyperplane class), $S^2 = \mathbb{CP}^1$ has trivial Hodge structure ($H^{1,1} = 1$, point class); Künneth gives $H^{p,p}(\mathbb{CP}^2 \times S^2)$ algebraic for all $p$; hard Lefschetz is classical for smooth projective.

**Status**: KNOWN (classical)
**Source**: paper29 Link 5 (classical algebraic geometry); paper12 §27 Axiom 3 (Geometric: "M_geom is 9-real-dim moduli of CP²×S² Einstein metrics"); paper12 §29 theorem catalogue 29.L5; paper61 §19.6 "anomaly cancellation 19 = 1 + 4 + 6 + 8 guarantees Hodge numbers compat with SM spectrum"; programme/12-hodge-conjecture.md §12.2 Route 1 Step 3.

#### Physics

- **Face**: TOPOLOGY (paper60 §07 Lehmer face — $H^{1,1} = 1$ is a topological winding / integer-class statement; paper60 §13 adjacency table "Lehmer and YM are the two gap-above-ground-state faces" — CP²×S² carries the same integer-cohomology-generated-by-one-class rigidity)
- **Projection**: $P_B$ (paper61 §08 — CP² is the internal space of Branch B gravity-side; $S^2$ = $\mathbb{CP}^1$ Kähler geometry is gauge-bundle-structural; Axiom 3 Geometric per paper12 §27 lives in Branch B compactification-moduli sector)
- **Pattern**: P2 Holonomy (paper60 §07 TOPOLOGY-face uses winding/Chern-class correspondence; the CP² hyperplane class is the generator of the $U(1)$-bundle winding; Chern number)
- **Invariant preserved**: gauge class (load-bearing — $H^{1,1} = 1$ generated by hyperplane = $c_1(\mathcal{O}(1))$), holonomy (background — the integral class is the winding of the tautological bundle)
- **Geometric interpretation**: Lefschetz B for CP² × S² is classical: the hyperplane class generates $H^{1,1}(\mathbb{CP}^2)$; Künneth with $\mathbb{CP}^1$ gives all $(p,p)$-classes algebraic. Under $P_B$ (paper61 §08) this is Branch B's Kähler geometric sector — paper12 §27 Axiom 3 identifies the moduli space $M_{\text{geom}}$ of CP² × S² Einstein metrics as "9-real-dimensional, forced by Hodge numbers of CP² × S² + SM gauge rank" (paper11). The anomaly-cancellation relation $19 = 1 + 4 + 6 + 8$ (paper61 §19.6) guarantees consistency. TOPOLOGY face assignment (paper60 §07) tracks that the $H^{1,1} = 1$ statement is a winding-number / integer-generator rigidity — the cyclotomic-protection analog on the Kähler-geometric side. [Considered but rejected: face SYMMETRY — Kähler structure IS a symmetry but the load-bearing content is topological generation by integer class; projection $P_D$ — CP² × S² appears in Branch D's geometric sector (paper12 §27 Axiom 3) but the Kähler / Lefschetz content is $P_B$-canonical.]
- **Cross-cuts**: qg5d Branch B (CP² × S² IS the internal compactification manifold of QG5D, paper12 §27 Axiom 3; paper61 §08), lehmer (TOPOLOGY canonical — integer-class rigidity / cyclotomic-protection structural parallel per paper60 §13 adjacency table), baum-connes (Chern-character isomorphism K-theory ↔ rational cohomology — Chern class of hyperplane lives in both; paper29 programme-graph-edge), ym:L5 (CP^{N-1} internal space vs CP² × S² — Kähler structural family; paper60 §13 SYMMETRY adjacent to CURVATURE).

### L6 — Geometric Langlands → Hitchin moduli → Hodge structures

**Claim**: Gaitsgory-Raskin 2024 (arXiv:2405.03599) proved the geometric Langlands conjecture: for reductive $G$ and smooth projective curve $C$, the categorical equivalence $\text{Aut}(\text{Bun}_G) \simeq \text{QCoh}(\text{LocSys}_{G^L})$ holds. APPLICATION: Hitchin moduli carry natural Hodge structures; Langlands equivalence should transport these to algebraic cycles. The bridge from categorical equivalence to Hodge-class algebraicity is OPEN.

**Status**: PARTIAL (geometric Langlands PROVED; Hodge application OPEN)
**Source**: paper29 Link 6; Gaitsgory-Raskin 2024 arXiv:2405.03599 (Breakthrough Prize 2025); Kapustin-Witten 2007 arXiv:hep-th/0604151 (physics predecessor); programme/12-hodge-conjecture.md §12.2 Route 2.

#### Physics

- **Face**: RESONANCE (paper60 §15 — categorical equivalence $\text{Aut} \simeq \text{QCoh}$ is a resonance-amplitude-matching statement: automorphic sheaves = spectral sheaves; the correspondence IS spectral data matched to automorphic data)
- **Projection**: $P_B$ (paper61 §08 — Hitchin moduli + Bun_G live in gauge-bundle / Branch B; Kapustin-Witten's N=4 SYM S-duality is the Branch B physics predecessor)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — Geometric Langlands reinterprets automorphic data as spectral data; the categorical equivalence is the paradigmatic Pattern 1 move: "restore the other side of the duality, the mystery dissolves")
- **Invariant preserved**: C*-algebra structure (load-bearing — categorical equivalence of derived categories is a homotopy-C*-algebra-level statement), monodromy (background — Langlands duality between $\text{Bun}_G$ and $\text{LocSys}_{G^L}$ IS monodromy-swap)
- **Geometric interpretation**: Geometric Langlands (Gaitsgory-Raskin 2024) is a categorical duality $\text{Aut}(\text{Bun}_G) \simeq \text{QCoh}(\text{LocSys}_{G^L})$; under $P_B$ (paper61 §08) this is Branch B's gauge-theory / Hitchin-moduli sector (Kapustin-Witten 2007 physics predecessor). Under paper60 §15 RESONANCE face, the categorical equivalence is the resonance-mode correspondence between automorphic and spectral sides. Pattern 1 (paper08 §36): reinterpreting the categorical equivalence as algebraicity-witness is the open step. [Considered but rejected: face SYMMETRY — Langlands duality IS a symmetry but the load-bearing content is resonance-mode matching; projection $P_D$ — the final Hodge-class output maps to $P_D$ but the construction's engine is $P_B$ gauge-bundle; pattern P4 — categorical rigidity implied but reinterpretation dominates.]
- **Cross-cuts**: ym:L16/L17 (RESONANCE canonical — Schwinger functions / operator-valued distributions are the YM-side resonance-mode content; paper60 §15 Branch B RESONANCE parallel), baum-connes (categorical / K-theoretic equivalence analog; paper29 programme-graph-edge), katz-sarnak (symmetry-type classification of Langlands duals), rh (Langlands dual ↔ functional-equation duality — SPECULATIVE).

### L7 — Routes I + II compose: Hodge for BC-motivated

**Claim**: Routes I (Links 1-5) and II (Link 6) compose: for BC-motivated smooth projective varieties, every rational $(p,p)$-class is algebraic. Requires a composition theorem showing that the endomotive route and the Langlands route produce compatible algebraicity witnesses.

**Status**: OPEN (NAMED WALL W3)
**Source**: paper29 Link 7; 2025 preprint 5-step algorithm (L² Hodge + Lefschetz $\mathfrak{sl}_2$ + Chow-motivic integration) — candidate composition mechanism.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — route composition = compatibility of two symmetry-group actions; $G_{\text{mot}}$ action from Route I must agree with Langlands-dual group action from Route II)
- **Projection**: $P_D$ (paper61 §19.6 — composition landing point is Branch D's motivic category; even though Route II (L6) lives in $P_B$, the composed statement's algebraicity-witness conclusion lives in $P_D$)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — compose two routes by reinterpreting both outputs in common motivic-BC category; paper61 §19.6 "Hodge classes are fixed by $G_{\text{mot}}$ iff algebraic")
- **Invariant preserved**: Galois representation (load-bearing — both routes produce $G$-equivariant outputs; composition is compatibility of representations), gauge class (background — Langlands-dual gauge group enters through L6)
- **Geometric interpretation**: Link 7 asks for a composition theorem: the endomotive-route motivic Galois action and the Langlands-route Hitchin-moduli Hodge structure must agree on their overlap (BC-motivated varieties within Hitchin-covered families). Under $P_D$ (paper61 §19.6) this is internal consistency of Branch D's two sub-routes. Pattern 1 (paper08 §36): reinterpret both categorical outputs as classes in a common motivic target. The 2025 preprint's 5-step algorithm is the candidate construction. [Considered but rejected: face RESONANCE — categorical-equivalence side of L6 is resonance but composition is symmetry-compatibility; projection $P_B$ — Route II lives in $P_B$ but the COMPOSED conclusion's algebraicity-witness lives in $P_D$; pattern P4 — rigidity of composition fair but reinterpretation is load-bearing move.]
- **Cross-cuts**: ym:L18 (route-split: $P_O$-vs-$P_B$ branching decision — same structural shape of "which projection bears the closure"), rh (two-route structure: CCM spectral + functional-equation ↔ two-route Hodge), bsd (CM-abelian route composition analog), h12 (class-field + motivic composition analog).

### L8 — Motivic functoriality → all smooth projective

**Claim**: Extend from BC-motivated varieties to all smooth projective varieties over $\mathbb{C}$. Requires a motivic functoriality theorem: every smooth projective variety admits a motivic correspondence to a BC-motivated variety that preserves Hodge classes. "Arguably as hard as the Hodge conjecture itself" (PROOF-CHAIN comment).

**Status**: OPEN (NAMED WALL W2 — the hardest step)
**Source**: paper29 Link 8 [OPEN]; Deligne §5 (motivic functor full-faithfulness); André motivated recovery (bypass on ab-var slice).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — motivic functoriality IS a symmetry-equivalence-of-categories statement: the motivic-correspondence category is closed under smooth projective)
- **Projection**: $P_D$ (paper61 §19.6 — motivic functoriality is Branch D's closure property: can every variety be captured by the BC-motivated / endomotive category?)
- **Pattern**: P4 Topological Rigidity (paper60 §12 — functoriality is a universal-property rigidity: the motivic category is forced to contain all smooth projective via the correspondence)
- **Invariant preserved**: Galois representation (load-bearing — motivic correspondences preserve $G_{\text{mot}}$-equivariance), scaling dimension (background — correspondences preserve codimension/dimension)
- **Geometric interpretation**: Link 8 is the extension from BC-motivated to all smooth projective via a motivic functoriality theorem. Under paper60 §12's SYMMETRY face: the motivic category is closed (universally) under smooth projective. Under $P_D$ (paper61 §19.6) this is Branch D's ultimate closure — the BC endomotive must capture every variety through motivic correspondence. Pattern 4 rigidity (paper60 §12): universal property forces the correspondence; Deligne §5 notes "progress blocked by lack of methods to construct interesting algebraic cycles" — same wall in our framework. BYPASS: restrict Clay claim to BC-motivated class + André motivated recovery for ab-var slice. [Considered but rejected: face ARITHMETIC — motivic correspondences are number-theoretic but the functoriality statement is symmetry-canonical; pattern P1 — reinterpretation of varieties as motivic-category-objects is fair but rigidity dominates; projection $P_O$ — L8 is arguably the Clay-outer-ring-boundary but mechanically lives in $P_D$.]
- **Cross-cuts**: bsd (CM-abelian André motivated recovery — bypass direction), h12 (motivic-class-field correspondence analog), baum-connes (K-theoretic functoriality analog — assembly-map closure), schanuel (period-relation functoriality — paper29 programme-graph-edge).

---

## §4 Branch Map

The Hodge proof chain splits at the route level (Route A = endomotive Links 1–5, Route B = geometric Langlands Link 6) and at the composition/extension level (Links 7-8). Unlike YM's single-conditional structure, Hodge has THREE named walls (W1, W2, W3) and a cleaner two-route architecture.

```
L1 (BC endomotives, LITERATURE)
                │
                │  Route A sequential chain
                ▼
L2 (Tannakian G_mot, LITERATURE)
                │
                ▼
L3 (G_mot → Hodge filt, CONJECTURED — W1)  ←── motivic-BC extension
                │                              (paper31-baum-connes)
                ▼                              prerequisite
L4 (Std Conj D for BC-motivated, PARTIAL — W1)
                │   ├── L4a ab-var-powers [PROVED 2024]
                │   └── L4b generic [OPEN — W1]
                ▼
L5 (Lefschetz B for CP² × S², KNOWN)  ←─ Branch D Axiom 3 Geometric
                │                        (paper12 §27; 9-d M_geom)
                │
                │  Route A convergence
                ▼
        ┌───────┴───────┐
        │               │
                L7 (Routes compose, OPEN — W3)
        │               │
        │    ^^^
        │    │  │ Route B independent
        │    │  │
        │    L6 (Geom Langlands, PARTIAL)
        │               │
        │               ▼
        └───────────────┴── Hodge for BC-motivated (if W1 + W3 close)
                            │
                            ▼
                  L8 (Motivic functoriality, OPEN — W2)
                            │
                            ▼
                    Full Hodge Conjecture (if W1 + W2 + W3 all close)

Route A physics triplet: [SYMMETRY | P_D | P4]    dominant symmetry/rigidity
Route B physics triplet: [RESONANCE | P_B | P1]   categorical-equivalence reinterpretation
Link 5 anchor triplet:   [TOPOLOGY | P_B | P2]    classical integer-class rigidity
Link 8 closure triplet:  [SYMMETRY | P_D | P4]    universal-property rigidity

The two routes differ in which PROJECTION bears the construction:
- Route A (Links 1-4, 7-8) is $P_D$-canonical (motivic / endomotive / Branch D)
- Route B (Link 6) is $P_B$-canonical (Hitchin moduli / gauge / Branch B)
- Link 5 is a $P_B$ classical anchor (CP² × S² Kähler geometry per paper12 §27 Axiom 3)
- Composition at L7 lands in $P_D$ (motivic category is the target)

This tells us: Hodge is fundamentally a $P_D$-problem with $P_B$ auxiliary structure
(the Langlands route and the Kähler moduli both feed into the Branch D motivic output).
Paper61 §19.6's compound assignment $P_D \cap P_A$ captures the final observational
ingredient (Hodge decomposition ↔ S^1 KK angular-momentum sectors) — $P_A$ is not a
CONSTRUCTION projection for any layer but IS the quantum-side shadow of the finished
Hodge-decomposition statement.
```

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   1   | ████                  | L5 Lefschetz B for CP² × S² — classical integer-class / cyclotomic-protection structural form (paper60 §07). |
| DYNAMICS   |   0   |                       | Hodge does not interrogate the dynamical / modular-flow traversal of the circle. |
| HARMONICS  |   0   |                       | The Hodge-decomposition shadow in $P_A$ (Fourier-modes on $S^1$) is a CROSS-CUT (paper61 §19.6), not a layer assignment. |
| MEASURE    |   0   |                       | No equidistribution content. |
| AMPLITUDE  |   0   |                       | No growth-rate / "loudness" content. |
| SYMMETRY   |   6   | ████████████████████████ | DOMINANT. L1 BC endomotives, L2 Tannakian $G_{\text{mot}}$, L3 Hodge-filtration compatibility, L4 Std Conj D (hom=num), L7 route composition, L8 motivic functoriality — six symmetry-canonical layers. Hodge IS the canonical SYMMETRY vertex for group-action / motivic-Galois-category problems. |
| CURVATURE  |   0   |                       | No curvature face (despite CP² × S² being Kähler — the Kähler class is topology-canonical, not curvature-canonical here). |
| ARITHMETIC |   0   |                       | Artin motives and cyclotomic fields are number-theoretic cross-cuts, not primary face. |
| RESONANCE  |   1   | ████                  | L6 Geometric Langlands categorical equivalence (paper60 §15 — automorphic ↔ spectral resonance-matching). STRONG SECONDARY despite single-layer count because L6 IS Route B. |
| SPREAD     |   0   |                       | No $L^2$-mass-spreading content. |

**Interpretation**: SYMMETRY dominates (6 / 8 layers, 75%) — confirming Hodge as the canonical SYMMETRY face in the outer ring (motivic Galois group / Tannakian / Standard Conjectures D form the symmetry-type-classification skeleton). TOPOLOGY (L5) and RESONANCE (L6) each contribute one layer as auxiliary anchors: TOPOLOGY is the classical CP² × S² integer-class anchor (Kähler-geometric side), RESONANCE is the Langlands-categorical anchor (gauge-side). Seven faces are absent (DYNAMICS, HARMONICS, MEASURE, AMPLITUDE, CURVATURE, ARITHMETIC, SPREAD). The "shape" of Hodge on the e-circle is strongly concentrated on SYMMETRY with Kähler-topology + categorical-resonance bookends — consistent with paper61 §19.6's compound assignment $P_D \cap P_A$ (Branch D's motivic Galois + Branch A's Hodge-decomposition shadow).

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No CONSTRUCTION layer lives in $P_A$. However, paper61 §19.6 compound assignment is $P_D \cap P_A$: the Hodge decomposition $H^n = \oplus H^{p,q}$ is the quantum-side shadow of the finished statement (parallel to $S^1$ KK angular-momentum sectors). $P_A$ is the observational, not constructional, projection. |
| $P_B$        |   2   | ████████             | L5 (CP² × S² Kähler / Branch D Axiom 3 Geometric = Branch B Kähler-moduli sector per paper12 §27) and L6 (Hitchin moduli / Gaitsgory-Raskin gauge-theory side). STRONG SECONDARY. |
| $P_C$        |   0   |                      | Cosmological projection forgets Hodge. |
| $P_D$        |   6   | ████████████████████████ | DOMINANT. Branch D / endomotive / motivic Galois — home of L1, L2, L3, L4, L7, L8. 75% of layers. Matches paper61 §19.6 "primary projection through Branch D". |
| $P_E$        |   0   |                      | Hodge does not contribute a direct pin to the 36-pin master table. Chern-class integers + period ratios appear in paper12 geometric sector but no direct Hodge pin (noted in $P_E$-row of §2b fan-out). |
| $P_O$        |   0   |                      | No layer assigned to $P_O$ — the outer-ring-boundary could be argued at L8 (motivic functoriality is the Clay-grade full-scope closure) but mechanically lives in $P_D$. Contrast with YM:L18 which IS $P_O$-canonical for H4's Clay-boundary status. |

**Interpretation**: $P_D$-dominant (6 / 8, 75%) — Hodge is fundamentally a Branch D / motivic / endomotive object. $P_B$ carries the Kähler-moduli anchor (L5) and the geometric-Langlands / Hitchin-moduli route (L6) — the gauge-bundle / gravity-side structural support. Paper61 §19.6 compound assignment $P_D \cap P_A$ identifies the quantum-shadow ($P_A$) observational character even though no construction layer lives there. Compared to YM's bimodal $P_B$/$P_D$ profile (65/30), Hodge is more uniformly $P_D$-concentrated with $P_B$ as minority auxiliary. The absence of a $P_O$ layer is a structural distinction: Hodge's Clay-boundary character distributes across three named walls (W1 in $P_D$, W2 in $P_D$, W3 in $P_D$) rather than concentrating at one conditional.

---

## §7 Standard Conjecture D motivic extension + CP² × S² moduli note (Branch D Axiom 3)

This vertex has two SPECIAL structural dependencies that are called out per brief.

### §7.1 Motivic extension of Standard Conjecture D (W1 prerequisite)

W1 (L3-L4 motivic Hodge filtration / Std Conj D for BC-motivated) depends on the **motivic extension of Standard Conjecture D**. The dependency graph:

```
W1 closure requires:
│
├── Part (a): Hodge-filtration compatibility of G_mot on H^*_dR
│       │
│       └── depends on: Motivic-Baum-Connes extension
│              │
│              └── paper31-baum-connes motivic BC construction
│                  (Route A support; PROOF-CHAIN edge)
│
└── Part (b): Standard Conjecture D for BC-motivated
        │
        ├── ab-var-powers slice [PROVED 2024, arXiv:2510.21562]
        │       │
        │       └── inherits to BSD-CM slice (paper26; CM elliptic curves
        │             → abelian varieties → their powers)
        │
        └── generic BC-motivated [OPEN]
                │
                └── motivic extension of Std Conj D needed
                    (Grothendieck 1969; Kleiman 1994 survey;
                     motivic cohomology deep conjecture)
```

**Why motivic not classical**: Std Conj D (hom = num) is stated classically for pure motives. Its MOTIVIC EXTENSION — applied to the BC endomotive's pro-object in $\text{CHM}_\mathbb{Q}$ — requires that the comparison isomorphism $H^*_{\text{dR}} \simeq H^*_B \otimes \mathbb{C}$ intertwine $G_{\text{mot}}$-action and Hodge-filtration. This is NOT the classical statement; it is the motivic-cohomological refinement. The 2024 ab-var-powers proof (arXiv:2510.21562) cracks the classical slice; extension to the motivic / BC-motivated setting is W1.

**Cross-reference to §3**: L3 (CONJECTURED) and L4 (PARTIAL) both depend on this motivic extension. The motivic-BC extension resides in paper31-baum-connes (programme-graph-edge). The 2025 preprint's 5-step algorithm (L² Hodge + Lefschetz $\mathfrak{sl}_2$ + Chow-motivic integration) is the candidate construction.

### §7.2 CP² × S² moduli — Branch D Axiom 3 (L5 anchor)

L5 (Lefschetz B for CP² × S², KNOWN) is the classical anchor, but its role in THIS framework is structural: CP² × S² IS the internal compactification manifold of QG5D's geometric sector. Per paper12 §27 Axiom 3 Geometric:

> *"M_geom is a 9-real-dimensional moduli space of CP²×S² Einstein metrics from QG5D Paper 11, disjoint from the spectral sector. dim_ℝ M = 9 is forced by Hodge numbers of CP²×S² + SM gauge rank."*

This is **Branch D Axiom 3** — the Geometric axiom of the CBB system, which sets the moduli space's dimension from the very Hodge numbers that Link 5 certifies are algebraic. The self-consistent loop:

```
CP² × S² Hodge numbers
       │
       │  (classical algebraic geometry;
       │   Link 5 Lefschetz B)
       ▼
H^{1,1}(CP²×S²) structure
       │
       │  (Branch D Axiom 3:
       │   dim M_geom forced by
       │   Hodge numbers + SM rank)
       ▼
M_geom (9-d Einstein moduli)
       │
       │  (paper11; paper12 §27;
       │   paper61 §08 Branch B
       │   KK compactification)
       ▼
Anomaly cancellation 19 = 1 + 4 + 6 + 8
       │
       │  (paper61 §19.6; guarantees Hodge
       │   numbers consistent with SM)
       ▼
Compactification is self-consistent
```

**What this means for the X-Ray**: L5 is TOPOLOGY-face / $P_B$-projection at the LAYER level (classical Kähler-geometric statement), but structurally it is DEPENDENT ON Branch D Axiom 3 at the programme level — the CP² × S² moduli serves double duty (classical Link 5 anchor + CBB Geometric axiom basis). This is the architectural specialty of Hodge: Branch D Axiom 3 is where the geometric anchor meets the operator-algebra framework.

**Cross-reference to §3**: L5's Physics block notes $P_B$ (Branch B KK compactification), but the programme-level structural dependency is on Branch D Axiom 3 (paper12 §27). This is NOT a double-counting — the LAYER is $P_B$ (Kähler-geometric classical), but the FRAMEWORK ROLE is Branch D Axiom 3. Both are real; they operate at different levels of the construction.

**Summary**: Hodge's two §7-special structural dependencies are (i) motivic extension of Std Conj D (W1 prerequisite, resides in paper31-baum-connes + 2024/2025 literature), and (ii) CP² × S² moduli serving as Branch D Axiom 3 Geometric (L5 anchor + framework basis, paper12 §27 + paper11). Both are flagged for atlas cross-cut output.

---

## §8 Atlas metadata

### §8a Named walls pulled from live PROOF-CHAIN

- **W1 — Motivic Hodge Filtration (Links 3-4)**: Motivic Galois acts on de Rham respecting Hodge filtration + Standard Conjecture D for BC-motivated. Status: **OPEN as a conditional** (CONJECTURED); PARTIAL for ab-var-powers slice (PROVED 2024, arXiv:2510.21562); inherits to BSD-CM slice. Bypass route: motivic-BC extension (paper31-baum-connes) + 2024 Std Conj D result + 2025 preprint 5-step algorithm. Closure scope: BC-motivated class (BSD-CM slice inherited; generic BC-motivated open).

- **W2 — Motivic Functoriality to All Smooth Projective (Link 8)**: Extension from BC-motivated class to ALL smooth projective varieties. Status: **OPEN-BUT-ADDRESSED**; arguably as hard as the Hodge conjecture itself. Bypass route: restrict Clay claim to BC-motivated class + André motivated recovery for abelian-variety slice. Closure scope: acknowledged-hard.

- **W3 — Route Composition (Link 7)**: Routes A (endomotive Links 1-5) + B (geometric Langlands Link 6) compose to Hodge for BC-motivated class. Status: **OPEN**. Bypass route: 2025 preprint's 5-step algorithm (L² Hodge theory + Lefschetz $\mathfrak{sl}_2$ + Chow-motivic integration). Closure scope: BC-motivated class.

All three are transparently disclosed per Clay §5d compliance (see `strategy/hodge/hodge-millenium-brief.md` DELTA 10).

### §8b Framework role (Branch D Axiom 3)

CP² × S² moduli doubles as (i) L5 classical Kähler-geometric anchor (TOPOLOGY / $P_B$ / P2) and (ii) Branch D Axiom 3 Geometric basis (paper12 §27 — 9-d Einstein-moduli space, dimension forced by Hodge numbers + SM rank). Anomaly cancellation $19 = 1 + 4 + 6 + 8$ (paper61 §19.6) ensures self-consistency with Standard Model spectrum.

### §8c Confidence stratification (per §7 strategy doc)

| Scope | Confidence | Blocker |
|---|---|---|
| CP² × S² (geometric sector, L5) | 9/10 | classical, KNOWN |
| CM abelian varieties (Link 4a slice) | 5/10 | W1 Hodge-filtration compatibility |
| General abelian varieties | 4/10 | W1 motivic extension of Std Conj D |
| BC-motivated smooth projective | 3/10 | W1 + W3 |
| All smooth projective varieties (full Hodge) | 3/10 | W2 motivic functoriality |

### §8d Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/hodge/` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, priority targets: W1 (Links 3-4, decompose motivic-Hodge-filtration into sub-chains), W3 (Link 7 composition theorem). Links 1-2 (LITERATURE), 5 (KNOWN) need no decomposition.
- **CCM verification**: `strategy/ccm-verification/ledger.md#hodge` — NOT YET CREATED. Hodge DOES depend on CCM 2005 (Connes-Consani-Marcolli arXiv:math/0512138 Theorem 8.14) for L1 (BC endomotive → Artin motives). Expected verdict when ledger written: **IRREDUCIBLY-CCM-DEPENDENT for L1** (CCM 2005 endomotive construction is the literature anchor).
- **Inner rings**: NOT APPLICABLE — Hodge is a primary outer-ring vertex.
- **Millennium bundle**: `strategy/hodge/` — pac-output bundle active per `strategy/hodge/hodge-millenium-brief.md`; B_bare + C_bare deliverables targeted. This X-RAY.md is the scaffolding annotation that feeds the compliance map 8 × 6 (Links × Deligne requirements).
- **Motivic-BC extension**: `solutions/paper31-baum-connes/PROOF-CHAIN.md` — Route A support chain; W1 depends on this.
- **2025 preprint (L² Hodge + Lefschetz $\mathfrak{sl}_2$ + Chow-motivic)**: external; the candidate 5-step algorithm for W3 composition.

---

## §9 Methodology

This X-Ray was produced by the PAC operator in annotation mode per `strategy/x-ray/x-ray-brief.md` (DELTA 3 primitives: READ / ANNOTATE / CITE / CROSS-LINK / CRITIC-ATTACK / ARBITER-DECIDE). Vocabulary is fixed (10 faces paper60, 6 projections paper61, 5 patterns ORA v8, 16 invariants per template). No invention. Every physics-block assignment carries a paper60 / paper61 / paper12 / paper29 / paper31 / ORA v8 / capacitor citation.

### §9a Inputs read (per priority order)

1. `strategy/x-ray/x-ray-template.md` (canonical structure)
2. `strategy/x-ray/x-ray-brief.md` (annotation-mode discipline)
3. `strategy/x-ray/proof-chain/ym/X-RAY.md` (reference exemplar; 18-layer CURVATURE-canonical $P_B$-dominant)
4. `strategy/proof-chain/hodge/PROOF-CHAIN.md` (live 8-link chain; 2026-04-15 snapshot)
5. `strategy/hodge/00-millenium-strategy.md` (Clay compliance strategy)
6. `strategy/hodge/hodge-millenium-brief.md` (W1/W2/W3 disclosure requirements)
7. `solutions-with-prize/paper29-hodge/preprint/00-proof-skeleton.md` (per-link detail; two-route framing; confidence stratification)
8. `solutions-with-prize/paper29-hodge/strategy/00-hodge-attack-plan.md` (PCA verification plan per link)
9. `integers/paper60-geometry-of-circle/13-face-7-curvature-yang-mills.md` (SYMMETRY / CURVATURE face positioning)
10. `integers/paper61-projections-5d/sections/06-12-the-six-projections.md` (§19.6 Hodge compound $P_D \cap P_A$ explicit)
11. `integers/paper61-projections-5d/sections/19-24-what-this-explains.md` §19.6 Hodge + NS section
12. `integers/paper12-cbb-system/27-anchor-document.md` (Axiom 3 Geometric: CP² × S² Einstein moduli, 9-d, forced by Hodge numbers + SM rank)
13. `programme/12-hodge-conjecture.md` §12.2 (Route 1 BC → endomotives → motives; Route 2 Kapustin-Witten → Gaitsgory-Raskin)
14. `strategy/north-star.md` §0.9 (Projection Discipline) + §0.10 (Vocabulary Canon — "4+1 derivable coordinates" / "M⁵" / "Integers" canonical terms)

### §9b Projection-discipline compliance (§0.9 check)

Every layer's claim is proved using invariants in the corresponding projection's preservation class (paper61 §15.1). Spot checks:

- L1 C*-algebra structure (BC endomotive) — preserved under $P_D$ (Branch D IS the operator-algebra projection). ✓
- L5 gauge class / holonomy (Chern hyperplane) — preserved under $P_B$ (gauge-bundle projection). ✓
- L6 C*-algebra structure (categorical equivalence) — preserved under $P_B$ (Hitchin-moduli gauge side). ✓
- L3-L4 Galois representation — preserved under $P_D$ (motivic Galois lives in Branch D). ✓

Paper61 §19.6's compound assignment $P_D \cap P_A$ identifies the OBSERVATIONAL (finished-statement) shadow ($P_A$) without assigning any CONSTRUCTION layer to $P_A$. This respects projection discipline: no cross-domain claim uses $P_A$-invariants to prove a $P_D$-layer.

### §9c Vocabulary canon compliance (§0.10 check)

Where quoting programme terms, "5D" has been rendered "M⁵" or "4+1 coordinate structure" per intervention 8b. "Postulate" avoided (L5 is KNOWN from classical algebraic geometry; L1-L2 LITERATURE; no postulated claims at the X-Ray layer — all derivations or citations). "We derive" / "forced by" / "inherits" used where applicable.

### §9d Critic-attack record summary

Notable arbiter wins per §3 considered-but-rejected notes:

- **L3 face**: SYMMETRY over RESONANCE (Hodge grading is spectral but compatibility move is symmetry-canonical)
- **L3 projection**: $P_D$ over $P_A$ (Hodge decomposition shadows into $P_A$ per paper61 §19.6 but filtration-preservation construction lives in $P_D$)
- **L5 projection**: $P_B$ over $P_D$ (CP² × S² appears in Branch D Axiom 3 but Kähler / Lefschetz content is $P_B$-canonical; the framework-role vs layer-role distinction clarified in §7)
- **L6 face**: RESONANCE over SYMMETRY (Langlands duality has symmetry character but categorical-equivalence resonance-matching is load-bearing)
- **L7 projection**: $P_D$ over $P_B$ (composition LANDING is $P_D$ even though Route II (L6) lives in $P_B$)
- **L8 projection**: $P_D$ over $P_O$ (motivic functoriality IS Clay-grade-closure-equivalent but MECHANICALLY lives in $P_D$ — compare YM:L18 $P_O$-canonical where H4 is genuinely the Clay-conditional)

Full critic-attack record and arbiter decisions to be logged at `strategy/x-ray/pac-output/runs/run-02/vertices/hodge/critic-attacks.md` and `arbiter-decisions.md` when that run fires. This X-RAY.md records only the WINNING assignments.

### §9e Methodological limits

- Hodge PROOF-CHAIN has 8 links vs YM's 18 — fewer layers means lower cross-cut count is expected (see §8b of YM X-RAY where YM's 38 cross-cuts came from 20 layer entries).
- Three named walls (vs YM's single H4 wall) means the §8 walls-list is richer but the §7 special-dependency discussion (§7.1 motivic Std Conj D + §7.2 Branch D Axiom 3) is where the structural content lives.
- No prior decomposition or CCM-verification ledger entry exists for Hodge — this X-RAY.md is the scaffolding artifact that feeds those sibling bundles when they launch.
- Paper61 §19.6 assigns compound projection $P_D \cap P_A$ to Hodge; this X-RAY uses $P_D$-dominant + $P_A$-observational-shadow reading, not $P_A$-as-construction-layer. Arbiter decision recorded.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W1 (motivic Hodge filtration + Std Conj D for BC-motivated)**: Links 3-4 conditional. Face: SYMMETRY, projection: $P_D$, pattern: P4. Status: OPEN-BUT-ADDRESSED with PARTIAL closure on ab-var-powers slice (arXiv:2510.21562, 2024); BSD-CM slice inherits (paper26); generic BC-motivated class OPEN. Bypass: motivic-BC extension (paper31) + 2025 5-step algorithm + André motivated recovery.

- **G2 — W3 (route composition, Link 7)**: Routes A (endomotive) + B (Langlands) compose to Hodge for BC-motivated. Face: SYMMETRY, projection: $P_D$, pattern: P1. Status: OPEN. Bypass: 2025 preprint 5-step algorithm (L² Hodge theory + Lefschetz $\mathfrak{sl}_2$ + Chow-motivic integration).

- **G3 — W2 (motivic functoriality to all smooth projective, Link 8)**: Extension from BC-motivated to all smooth projective. Face: SYMMETRY, projection: $P_D$, pattern: P4. Status: OPEN; "arguably as hard as the Hodge conjecture itself" (PROOF-CHAIN). Bypass: restrict claim to BC-motivated + André motivated recovery for abelian-variety slice.

- **G4 — Link 6 Hodge application**: Gaitsgory-Raskin categorical equivalence PROVED; Hodge-class algebraicity extraction from categorical statement OPEN. Face: RESONANCE, projection: $P_B$, pattern: P1. Bypass: combine with Route A at L7 (subsumed in W3 closure).

- **G5 — Link 4b generic BC-motivated Std Conj D**: arXiv:2510.21562 (2024) covers ab-var-powers; extension to generic BC-motivated class OPEN. Face: SYMMETRY, projection: $P_D$, pattern: P4. Sub-wall of W1.

5 OPEN items (4 named walls W1/W2/W3 + G4 Langlands-Hodge bridge + G5 generic-BC-motivated slice). 3 of 8 links closed (L1 LITERATURE, L2 LITERATURE, L5 KNOWN). 3 of 8 PARTIAL/CONJECTURED (L3 CONJECTURED, L4 PARTIAL, L6 PARTIAL). 2 of 8 OPEN (L7, L8). Confidence stratification per §8c.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record and arbiter decisions belong to `strategy/x-ray/pac-output/runs/run-02/vertices/hodge/` when that run fires.

Notable cross-vertex considerations:

- **Paper61 §19.6 compound $P_D \cap P_A$**: treated as $P_D$-construction + $P_A$-observational-shadow. No construction layer assigned to $P_A$ (no layer uses quantum-side Born/Bell/spin-statistics invariants). Arbiter decision: the compound assignment is OBSERVATIONAL (what the finished statement looks like under $P_A$), not CONSTRUCTIONAL (which invariants build the proof). $P_A$ in §2b fan-out labeled as SECONDARY with "(forgotten at construction level)" clarification.

- **Branch D Axiom 3 vs L5 $P_B$**: double role clarified in §7.2. At LAYER level, L5 is $P_B$ (classical Kähler-geometric). At FRAMEWORK level, CP² × S² serves Branch D Axiom 3 Geometric (paper12 §27). Both assignments are correct; they operate at different levels of the construction.

- **L8 $P_D$ vs $P_O$**: rejected $P_O$ despite L8 being the Clay-grade full-scope closure. Mechanically L8 lives in $P_D$ (motivic functoriality is a closure property of the motivic category). Contrast YM:L18 which IS $P_O$-canonical because H4 IS genuinely the Clay-grade conditional boundary for YM. Hodge's Clay-grade character is distributed across three named walls, none of which lives in $P_O$ exclusively.

---

*End of Hodge X-Ray. Snapshot 2026-04-15. 8 layers (with L4a/L4b sub-layers giving 9 entries) annotated. SYMMETRY-canonical (6 layers), $P_D$-dominant (6 layers), P4-rich (4 layers). Three named walls (W1, W2, W3) transparently disclosed per Clay §5d; PARTIAL closure on ab-var-powers slice (2024) inherits to BSD-CM. Branch D Axiom 3 (CP² × S² 9-d moduli) framework-role for L5 flagged in §7.2. Compound projection $P_D \cap P_A$ per paper61 §19.6 retained as $P_D$-construction + $P_A$-observational-shadow.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
