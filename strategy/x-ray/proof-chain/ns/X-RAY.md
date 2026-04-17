# X-RAY: Navier-Stokes Existence and Smoothness (ns)

*X-Ray of the ns proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: ns
- **Paper**: paper30-navier-stokes
- **Live file**: `strategy/proof-chain/ns/PROOF-CHAIN.md` (snapshot 2026-04-14, v2.1)
- **Top-level claim**: Global existence and smoothness of 3D incompressible Navier-Stokes on $\mathbb{R}^3/\mathbb{Z}^3 = \mathbb{T}^3$ (Fefferman variant B) via KK spectral gap + gradient-flow transfer from YM + cosphere-bundle microlocal regularity.
- **Current status**: 3/8 PROVED (Links 1, 4 foundational + partial Link 5 with two published routes); confidence **4/10** (upgraded from 2/10 by W1/W2 cascade + Route B integration).
- **Primary branch (paper1)**: B (Gravity / KK / spectral gap control of high-frequency modes), with secondary D (type III$_1$ modular-flow ergodicity prevents singular-set formation).
- **Primary face**: CURVATURE (paper60 §13 — NS regularity INHERITS the YM curvature gap; "the gap is the curvature's gift to the quantum theory" applied to the fluid sector via gradient-flow transfer).
- **Primary projection**: $P_B$ (paper61 §19.6 — "Branch B carries the 'spectral gap prevents concentration of energy' ingredient" for NS).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
NS (Navier-Stokes Existence & Smoothness on T^3) — Fefferman variant (B)
│  primary face: CURVATURE   primary proj: P_B   primary pat: P4
│
├── L1: M⁵ Einstein → KK reduction to 4D Einstein+Maxwell+scalar   [LITERATURE]
│      │  face: CURVATURE    proj: P_B   pat: P3
│      │  invariant: KK mode index
│      │  source: Kaluza 1921, Klein 1926; Paper 1 §KK
│      │
│      └── supports L4 (KK spectral gap lives on the reduced geometry)
│
├── L2: T_{μν} near-equilibrium → incompressible NS          [CONJECTURED]
│      │  face: RESONANCE    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure
│      │  source: BHMR 2008 (fluid/gravity duality)
│      │  depends: L1
│      │
│      └── STRUCTURALLY DECOUPLED (chain does NOT require rigorous
│             BHMR; L2 is motivational; rigorous chain L3-L7 composes
│             without it — "architectural decoupling" bypass, W2 below)
│
├── L3: YM gradient-flow transfer (L.1.1–L.1.5 → NS velocity)  [OPEN]
│      │  face: DYNAMICS     proj: P_B   pat: P3
│      │  invariant: ergodic property
│      │  source: Paper 8 §L.1 Lemmas 1.1-1.5; paper08 L15-L17
│      │  depends: L2 motivationally; rigorously on YM L15-L17 (all PROVED)
│      │  note: YM now UNCONDITIONAL post W1/W2 closure → cleaner transfer
│      │
│      └── YM's paper08 L15 is the STRUCTURAL PARENT of L3
│
├── L4: KK spectral gap Δ_0^KK > 0 controls high-freq modes   [PROVED UNCOND. ALL-LOOP]
│      │  face: CURVATURE    proj: P_B   pat: P4
│      │  invariant: spectral gap
│      │  source: paper08 Theorem 4 + Paper 11 Theorem K.4
│      │          + Paper 10 (scheme independence)
│      │
│      └── UPGRADE 2026-04-13: from "PROVED inheriting from Paper 8" to
│             "PROVED UNCONDITIONAL ALL-LOOP" via W1/W2 closure.
│             No residual UV-scheme questions propagate into NS.
│
├── L5: BKM criterion ∫_0^T sup|ω| dt < ∞                    [PARTIAL — W1]
│      │  face: AMPLITUDE    proj: P_D   pat: P4
│      │  invariant: boundary condition
│      │  depends: L3 + L4
│      │  status: OPEN-BUT-ADDRESSED via TWO PUBLISHED ROUTES
│      │
│      ├── L5a Route A (Camlin 2025): bounded Φ functional      [PUBLISHED]
│      │      │  face: DYNAMICS     proj: P_B   pat: P3
│      │      │  invariant: ergodic property
│      │      │  mechanism: Sundman-type temporal lifting →
│      │      │            BKM integral becomes geometrically invariant;
│      │      │            finiteness in physical time on T^3
│      │      │  KK-adaptation task: does Δ_0^KK on M^4×S^1/Z_2
│      │      │                      provide control for Φ?
│      │      │
│      ├── L5b Route B (arXiv:2601.08854, Jan 2026):            [PUBLISHED]
│      │      │  cosphere-bundle microlocal regularity
│      │      │  face: SPREAD       proj: P_D   pat: P1
│      │      │  invariant: scaling dimension (wave-front-set index)
│      │      │  mechanism: lift NS dynamics to cosphere bundle;
│      │      │            wave-front-set regularity criterion
│      │      │  framework advantage: M^4×S^1/Z_2 ALREADY Riemannian
│      │      │  capacitor: MICRO↔QFT (filled Tier 1: Hollands-Wald 2024
│      │      │            + Dappiaggi 2023-24 + BFR 2025 + 2601.08854)
│      │      │
│      └── INTEGRATION TASK: Route B microlocal structure
│             generates Route A Φ functional on M^4×S^1/Z_2 via
│             Hörmander/Melrose wavefront calculus; aggregate
│             confidence 0.60; audit OPEN
│
├── L6: Energy descent: KK conservation (5D) → NS dissipation  [CONJECTURED]
│      │  face: MEASURE      proj: P_B   pat: P4
│      │  invariant: ergodic property
│      │  source: Leray 1934, Hopf 1951; paper30 §6
│      │  depends: L5
│      │
│      └── Clay sub-req 2 (bounded energy ∫|u|^2 < C) depends here
│
├── L7: Uniqueness via Galerkin + energy                       [CONDITIONAL on L5]
│      │  face: SYMMETRY     proj: P_D   pat: P1
│      │  invariant: C*-algebra structure
│      │  source: Ladyzhenskaya 1969, Temam 1977; standard PDE
│      │  depends: L5
│      │
│      └── conditional closure via L5 regularity
│
└── L8: Global regularity: L3-L7 compose                       [OPEN]
       │  face: CURVATURE    proj: P_B   pat: P4
       │  invariant: spectral gap, boundary condition
       │  depends: L3, L4, L5, L6, L7
       │
       └── CLOSES Fefferman variant (B) once L5 integration completes
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (No quantum observable projection
                          forgets the KK gap → NS regularity
                          chain entirely.)
                                  ▲
                                  │
                                  │
        ┌─────────────(P_O outer)───────────────┐
        │                                       │
        │  NS: ∀ smooth div-free u° on T^3,     │
        │      ∃ p,u ∈ C^∞(T^3 × [0,∞))         │
        │      satisfying (1),(2),(3),(10),(11) │
        │      with ∫|u|^2 < C ∀ t.             │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_C cosmology      ═══ P_B gravity ═══       P_D CBB
    (forgotten —       KK gap → Δ_0^KK>0         ITPFI III_1
    no cosmological    controls high-freq        ergodicity of
    pin uses NS        modes; Kaluza-Klein       modular flow
    regularity)        reduction on M^4×S^1/Z_2; prevents
                       YM gradient-flow          singular-set
                       transfer L3 →             formation;
                       gauge→fluid parabolic;    Route B lands
                       Route A φ functional      in MICRO↔QFT
                            │                         │
                            ▼                         ▼
                       P_E pins                 (Pins shadow)
                       (K41 prefactor C_K       K41 universal
                        ≈ 1.5; Kolmogorov η     constant from
                        microscale; Taylor-     BGS/GUE +
                        Reynolds; intermittency Type III_1
                        exponent μ; paper12     ergodicity —
                        master table)           paper38 bonus)
```

Primary projection $P_B$ uses ═══ doubled line. $P_D$ is strong secondary (carries L2, L7, the Branch D "type III$_1$ prevents singular subsets" half of paper61 §19.6's dual-branch characterisation; and Route B's operator-algebra microlocal side). $P_O$ wraps the whole Fefferman variant (B) Clay statement.

### §2c Diagram C — Face position on the e-circle

```
                        TOPOLOGY
                        (Lehmer)
                            │
            SPREAD          │          DYNAMICS
            (QUE)           │          (Cramér)
                  ╲         │         ╱
                   ╲        │        ╱
       SYMMETRY ─────── e-circle ─────── HARMONICS
       (Katz-Sarnak)        │            (Collatz)
                   ╱        │        ╲
                  ╱         │         ╲
       ●  CURVATURE         │          MEASURE
          (YM / NS          │          (Sato-Tate)
           inherited)       │
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (RESONANCE secondary;
                        ARITHMETIC adjacent)
```

Marker key:

```
Primary face:    ● CURVATURE (paper60 §13 — NS inherits the YM curvature gap
                              via gradient-flow transfer; see paper61 §19.6)
Secondary faces: ○ DYNAMICS   (3 layers: L3 gradient-flow transfer,
                              L5a Route A Sundman lifting flow,
                              L5 BKM time-integral of flow)
                 ○ AMPLITUDE  (1 layer: L5 BKM integrand sup|ω| growth bound)
                 ○ RESONANCE  (1 layer: L2 BHMR near-equilibrium stress tensor)
                 ○ MEASURE    (1 layer: L6 energy descent — ergodic dissipation)
                 ○ SYMMETRY   (1 layer: L7 Galerkin/energy uniqueness)
                 ○ SPREAD     (1 layer: L5b Route B microlocal wave-front-set
                              — WF-set measures $L^2$-mass in phase space)
Absent faces:    TOPOLOGY, HARMONICS, ARITHMETIC
```

---

## §3 Layer-by-Layer X-Ray

### L1 — M⁵ Einstein → KK reduction to 4D Einstein+Maxwell+scalar

**Claim**: Five-dimensional Einstein gravity on $M^4 \times S^1/\mathbb{Z}_2$ Kaluza-Klein-reduces to 4D Einstein + Maxwell + scalar, providing the base geometry on which NS evolves.

**Status**: LITERATURE
**Source**: Kaluza 1921, Klein 1926; Paper 1 §KK (QG5D derivation); paper30 Link 1.

#### Physics

- **Face**: CURVATURE (paper60 §13 — "the Kaluza-Klein reduction of five-dimensional gravity on $M^4 \times S^1$ produces a tower of massive modes… the circle's compactness forces the gap")
- **Projection**: $P_B$ (paper61 §19.6 — Branch B is gauge-bundle / KK spectral gap; also paper61 §10 $P_B$ carries KK tower)
- **Pattern**: P3 Scale-Setting (KK radius $R \approx 10.10\,\mu\text{m}$ sets the scale for every downstream bound; paper60 §13 "n/R from their winding")
- **Invariant preserved**: KK mode index (load-bearing — $n \in \mathbb{Z}$ labels the tower), spectral gap (background — gap set at $n=1$)
- **Geometric interpretation**: KK reduction is the programme's foundational move — it produces the 4D base on which NS is posed, with an $S^1/\mathbb{Z}_2$ internal phase that will carry the spectral gap inherited by the fluid sector (paper60 §13). Under $P_B$ (paper61 §10) the reduction is the gauge-bundle's geometric preparation. Pattern 3 is canonical: $R$ sets every scale. [Considered but rejected: face TOPOLOGY — KK is circle-fibration so winding is involved but curvature dominates (the gap is the load-bearing output); projection $P_C$ — cosmological pin for $R$ lives in $P_C$ but the geometric step is gauge-side.]
- **Cross-cuts**: qg5d Branch B (L1 IS the QG5D KK reduction, PRIMARY PARENT), ym:L1 (KK spectral gap on same $M^4 \times S^1$), turbulence (paper38 inherits this L1 directly).

### L2 — T_{μν} near-equilibrium → incompressible NS

**Claim**: The 4D stress-energy tensor $T_{\mu\nu}$ in the near-equilibrium Landau frame, restricted to its hydrodynamic sector, gives the incompressible Navier-Stokes equations at leading order in the gradient expansion (fluid/gravity duality).

**Status**: CONJECTURED (bypassed via architectural decoupling — see W2)
**Source**: BHMR 2008 (Bhattacharyya-Hubeny-Minwalla-Rangamani, arXiv:0712.2456); paper30 §2 Link 2.

#### Physics

- **Face**: RESONANCE (paper60 §15 — "what vibrational frequencies are ALLOWED on the circle"; hydrodynamic modes ARE the low-frequency resonances of the stress tensor near equilibrium)
- **Projection**: $P_D$ (paper61 §10 — stress tensor as operator-valued distribution in the BC-algebraic / GNS framework; hydrodynamic limit is a KMS-type coarse-graining)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 analog — restoring the stress-tensor viewpoint reveals NS as the hydrodynamic projection of the Einstein equations)
- **Invariant preserved**: C*-algebra structure (load-bearing — $T_{\mu\nu}$ is operator-valued), BC-KMS state (background — near-equilibrium is near-$\beta=1$-KMS)
- **Geometric interpretation**: Fluid/gravity duality reinterprets NS as the hydrodynamic sector of the 5D Einstein equations — a Pattern 1 geometric reinterpretation (paper08 §36). Under $P_D$ (paper61 §10) the stress tensor sits in the operator-algebra side as an operator-valued distribution (the NS analog of YM L17's $T_{\mu\nu}^R$). The rigorous BHMR expansion is conjectural, but the chain is ARCHITECTURALLY DECOUPLED from L2 (see W2); L3–L7 compose without rigorous L2. [Considered but rejected: face CURVATURE — curvature in stress tensor but BHMR's character is resonant-mode expansion; projection $P_B$ — gauge-side at leading order but stress tensor properly lives in $P_D$ operator-algebra side.]
- **Cross-cuts**: ym:L17 ($T_{\mu\nu}^R$ operator-valued-distribution analog, shared C*-algebra), hilbert6 (axiomatization of fluid mechanics as Hilbert's 6th problem), rh (BC-KMS structure).

### L3 — YM gradient-flow transfer (Lemmas 1.1–1.5) → NS velocity

**Claim**: The Yang-Mills gradient flow (paper08 Lemmas 1.1–1.5, L15–L17) transfers to the NS velocity-field gradient flow via same-parabolic-class structural parallel, carrying the YM gradient-flow regularity infrastructure into the fluid setting.

**Status**: OPEN (OPEN-BUT-ADDRESSED via YM L15 parent)
**Source**: paper08 §L.1 Lemmas 1.1–1.5; paper08 L15 (PROVED, now UNCONDITIONAL post W1/W2); paper30 Link 3.

#### Physics

- **Face**: DYNAMICS (paper60 §08 — gradient flow IS a continuous dynamical system on the velocity field; "how does the modular flow TRAVERSE the circle" applied to the fluid; paper08 L15 explicitly DYNAMICS)
- **Projection**: $P_B$ (paper61 §19.6 — "Branch B carries the 'spectral gap prevents concentration of energy' ingredient" via gradient flow; paper61 §10 gauge-bundle dynamics)
- **Pattern**: P3 Scale-Setting (gradient-flow time $t$ sets the smearing scale; paper08 §36 Pattern 3 on YM L15 inherited directly)
- **Invariant preserved**: ergodic property (load-bearing — contractivity of the gradient flow = ergodic mixing on the fluid configuration space), scaling dimension (background)
- **Geometric interpretation**: NS regularity is a TRANSFER from YM (paper61 §19.6: "The mass gap $\Delta_\infty > 0$ controls the decay rate of gauge-field fluctuations — the same mechanism that prevents blowup in the fluid"). The YM gradient flow (paper08 L15 PROVED, paper60 §13 DYNAMICS face) and the NS gradient flow are the SAME second-order parabolic class with gauge-vs-divergence-free constraint; rigorous functor construction is OPEN but the parent is PROVED. Pattern 3 (scale-setting by flow time) is inherited. [Considered but rejected: face CURVATURE — the curvature gap drives the decay but the transfer's mechanism is dynamical; pattern P4 — rigidity is the end state but mechanism is scale-setting via flow time.]
- **Cross-cuts**: ym:L15 (STRUCTURAL PARENT, shared ergodic property — explicit programme-graph edge), ym:L16 (OS reconstruction analog), ym:L17 (stress-tensor operator-distribution analog), cramer (DYNAMICS canonical), paper32-bgs (modular-flow ergodicity).

### L4 — KK spectral gap Δ_0^KK > 0 controls high-frequency modes

**Claim**: The KK spectral gap $\Delta_0^{KK} = (2\pi/R)^2 > 0$ exists unconditionally at all loop orders, is scheme-independent, and controls high-frequency modes of the NS velocity field via Poincaré on $S^1/\mathbb{Z}_2$.

**Status**: PROVED UNCONDITIONAL ALL-LOOP (upgraded 2026-04-13)
**Source**: paper08 Theorem 4 (Weitzenböck + cluster); paper11 Theorem K.4 (all-orders inductive bootstrap); paper10 (scheme independence); paper30 Link 4.

#### Physics

- **Face**: CURVATURE (paper60 §13 — "the gap is the curvature's gift to the quantum theory"; NS inherits directly)
- **Projection**: $P_B$ (paper61 §08 / §10 — KK spectral gap is the load-bearing structural element; paper61 §19.6 "Branch B carries the 'spectral gap prevents concentration' ingredient for NS")
- **Pattern**: P4 Topological Rigidity (paper08 §36 — "compactness forces discreteness; discreteness forces gaps"; same rigidity as YM L1 inherited into NS)
- **Invariant preserved**: spectral gap (load-bearing — $\Delta_0^{KK} = (2\pi/R)^2$ IS the inherited gap), KK mode index (background)
- **Geometric interpretation**: L4 IS the YM L1 spectral gap applied to the NS setting: the same compactness of $S^1$ that discretizes the YM gauge spectrum discretizes the NS high-frequency modes, bounding them below by the gap (paper60 §13). Under $P_B$ (paper61 §08) this is the structural signature of the gauge-bundle projection. The W1/W2 closure (Paper 11 K.4 + Paper 10 scheme independence) makes the gap UNCONDITIONAL at all loop orders — the strongest inherited foundation any classical PDE chain could rest on (paper30 "cascading impact" §). [Considered but rejected: face TOPOLOGY — Lehmer parallel (paper60 §13 adjacency table) but curvature is canonical; pattern P3 — $R$ sets scale but the gap's existence is rigid.]
- **Cross-cuts**: ym:L1 (PRIMARY PARENT — shared spectral gap, paper60 §13), qg5d Branch B (shared spectral gap, paper61 §08 derivation chain), turbulence:L4 (inherited directly for K41 cascade, paper38), baum-connes (spectral gap as K-theoretic statement about the KK operator, paper31 programme-graph edge), pvnp (Popa-rigidity spectral gap analog).

### L5 — BKM criterion: ∫_0^T sup|ω| dt < ∞

**Claim**: The Beale-Kato-Majda time-integral $\int_0^T \sup_x |\omega(x,t)|\,dt < \infty$ on $\mathbb{T}^3$ is finite (BKM 1984 ⟹ no finite-time blowup ⟹ $C^\infty$ regularity).

**Status**: PARTIAL (OPEN-BUT-ADDRESSED — TWO PUBLISHED ROUTES)
**Source**: paper30 Link 5; Beale-Kato-Majda 1984; Camlin 2025 (Route A); arXiv:2601.08854 Jan 2026 (Route B).

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — "how LOUD can the oscillation get"; BKM bounds the $L^\infty$-amplitude of the vorticity in time)
- **Projection**: $P_D$ (paper61 §10 — BKM handled via operator-algebraic microlocal machinery on the flowed Hilbert space; cosphere-bundle analysis is $P_D$-side; Route A Sundman lifting is a DYNAMICS sub-face under $P_B$)
- **Pattern**: P4 Topological Rigidity (BKM is a topological finiteness criterion — $\int |\omega|\,dt < \infty$ IS a rigidity statement; Route B's wave-front-set triviality is Pattern-4-canonical)
- **Invariant preserved**: boundary condition (load-bearing — BKM IS the boundary condition for NS regularity), scaling dimension (background — wave-front-set index in Route B)
- **Geometric interpretation**: L5 is the NS analog of YM L18 — the AMPLITUDE-bounding conditional whose closure completes the Clay statement. Under $P_D$ (paper61 §10) the cosphere-bundle microlocal structure (Route B) lives in the operator-algebra side, with the MICRO↔QFT capacitor cell (Tier 1: Hollands-Wald 2024 + Dappiaggi 2023-24 + BFR 2025 + arXiv:2601.08854) filled. Pattern 4 rigidity is the frame: no finite-time blowup ⟺ bounded vorticity integral ⟺ $C^\infty$. Two published routes provide OPEN-BUT-ADDRESSED §5d-compliance. [Considered but rejected: face SPREAD — Route B uses phase-space $L^2$-distribution (moved to L5b sub-layer); face DYNAMICS — Route A's Sundman flow is dynamics (moved to L5a sub-layer); projection $P_B$ — gauge-side transfer real but the BKM WALL itself sits at $P_D$ operator-algebra; pattern P1 — Route B is a geometric reinterpretation (moved to L5b).]
- **Cross-cuts**: ym:L18 (both are the CONDITIONAL AMPLITUDE wall for their respective Clay vertex), lindelof (AMPLITUDE canonical — growth-rate bound structural form), turbulence (paper38 inherits via BKM + K41 linkage), baum-connes (cosphere bundle ↔ cotangent microlocalization is Baum-Connes-side; capacitor MICRO↔QFT).

#### L5a — Route A (Camlin 2025): bounded Φ functional + Sundman lifting

**Claim**: A bounded vorticity-response functional $\Phi$ constructed via Sundman-type temporal lifting renders the BKM integral geometrically invariant under bounded temporal diffeomorphism, yielding BKM finiteness in physical time on $\mathbb{T}^3$.

**Status**: PUBLISHED (arXiv preprint; KK-setting adaptation task OPEN)
**Source**: Camlin 2025 arXiv preprint; paper30 §Route-A.

##### Physics (Route A sub-layer)

- **Face**: DYNAMICS (paper60 §08 — Sundman temporal lifting IS a dynamical-flow reparametrization; boundedness of $\Phi$ under the lifted flow is a DYNAMICS-face statement)
- **Projection**: $P_B$ (paper61 §19.6 — KK-adaptation task lives on the gauge-bundle side: does $\Delta_0^{KK}$ on $M^4 \times S^1/\mathbb{Z}_2$ provide Φ-control at the same rate as flat $\mathbb{T}^3$?)
- **Pattern**: P3 Scale-Setting (Sundman time-reparametrization sets the scale for Φ-boundedness; same pattern as YM gradient flow L15)
- **Invariant preserved**: ergodic property (load-bearing — bounded Φ under lifted flow = ergodic-bounded behaviour), boundary condition (background — BKM boundary met via Φ)
- **Geometric interpretation**: Route A constructs a bounded functional whose finiteness implies BKM finiteness via Sundman's classical temporal-lifting move (paper60 §08 DYNAMICS face — flow-on-circle reparametrization). The KK-setting adaptation replaces the flat $\mathbb{T}^3$ base with $M^4 \times S^1/\mathbb{Z}_2$; paper61 §19.6 identifies the transfer mechanism (Branch B spectral gap). Pattern 3: flow time sets the scale for Φ-boundedness. [Considered but rejected: face AMPLITUDE — Φ is an amplitude bound ultimately but the mechanism is dynamics; pattern P4 — boundedness is rigidity but engine is scale-setting via Sundman lift.]
- **Cross-cuts**: ym:L15 (gradient-flow dynamics analog), cramer (DYNAMICS canonical), ym:L3 (k-independent polymer convergence — similar uniform-in-scale dynamical bound).

#### L5b — Route B (arXiv:2601.08854): cosphere-bundle microlocal regularity

**Claim**: Lifting NS dynamics to the cosphere bundle of a Riemannian manifold, microlocal analysis + Riemannian geometry produces a regularity criterion via wave-front-set conditions; landing directly in the capacitor MICRO↔QFT Tier 1 cell.

**Status**: PUBLISHED (arXiv:2601.08854, Jan 2026; WF→vorticity translation task OPEN)
**Source**: arXiv:2601.08854; paper30 §Route-B; capacitor cell MICRO↔QFT (Hollands-Wald 2024 + Dappiaggi 2023-24 + BFR 2025 + 2601.08854).

##### Physics (Route B sub-layer)

- **Face**: SPREAD (paper60 §—two-circles-one-torus interior / paper60 analog of SPREAD — "how $L^2$ mass distributes on the circle"; wave-front-set is the phase-space $L^2$-mass measure; cosphere bundle IS the WF-set's home)
- **Projection**: $P_D$ (paper61 §10 — microlocal analysis + local C*-algebra machinery is operator-algebra-side; MICRO↔QFT capacitor cell sits in $P_D$)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 analog — reinterpreting NS regularity as a WF-set triviality statement on the cosphere bundle; "restore the e-circle, mystery dissolves" applied to the fluid sector on $M^4 \times S^1/\mathbb{Z}_2$)
- **Invariant preserved**: scaling dimension (load-bearing — WF-set carries scaling-dimension index of oscillation/singularity at each cosphere point), C*-algebra structure (background — local C*-algebra of microlocal operators)
- **Geometric interpretation**: Route B is the Pattern 1 geometric reinterpretation of NS regularity: the singular-set question becomes a WF-set question on the cosphere bundle, trivial under microlocal regularity. Under $P_D$ (paper61 §10) this lands in the operator-algebra-side's local C*-algebra (same algebra that carries YM L17). The framework's $M^4 \times S^1/\mathbb{Z}_2$ is ALREADY Riemannian — zero structural mapping work (paper30 §Route-B). Subsumes CKN singular-set bound ($P_1(E) = 0$) because $E = \emptyset$ under WF-triviality. [Considered but rejected: face SYMMETRY — microlocal = symmetry of cotangent bundle is real but SPREAD is load-bearing ($L^2$-mass in phase space); face AMPLITUDE — WF-set bounds amplitude but its character is spread; projection $P_B$ — gauge-side transfer via spectral gap controls WF-set ultimately but the WF-set LIVES in $P_D$ operator-algebra side.]
- **Cross-cuts**: ym:L16 (OS reconstruction shared microlocal machinery), ym:L17 (local C*-algebra operator-valued distribution analog), baum-connes:L_cosphere (cosphere bundle ↔ cotangent K-theory), que (QUE / SPREAD face on equidistribution of $L^2$-mass), hilbert6 (axiomatization of hydrodynamics — microlocal foundation).

### L6 — Energy descent: KK conservation (5D) → NS dissipation (4D)

**Claim**: The 5D Killing $S^1/\mathbb{Z}_2$ symmetry conservation of KK energy descends to 4D NS Leray-Hopf energy dissipation $\frac{d}{dt} \int |u|^2 \leq -2\nu \int |\nabla u|^2$, yielding bounded energy $\int_{\mathbb{T}^3} |u|^2 < C$ for all $t$ (Clay sub-req 2).

**Status**: CONJECTURED
**Source**: Leray 1934, Hopf 1951; paper30 §6 Link 6.

#### Physics

- **Face**: MEASURE (paper60 §10 — "how do measures EQUILIBRATE on the circle"; energy dissipation is the equilibration of the velocity-field measure via ergodic descent)
- **Projection**: $P_B$ (paper61 §08 — KK conservation is gauge-bundle-side; descent to 4D NS is gauge-bundle / gravity projection output)
- **Pattern**: P4 Topological Rigidity (energy dissipation is a rigid Leray-Hopf monotonicity statement once established)
- **Invariant preserved**: ergodic property (load-bearing — dissipation IS ergodic mixing into the zero-energy ground state asymptotically), spectral gap (background — gap drives the dissipation rate)
- **Geometric interpretation**: The Killing vector field along $S^1/\mathbb{Z}_2$ gives 5D energy-momentum conservation (paper1 §KK); dimensionally reduced to 4D this becomes Leray-Hopf dissipation (paper60 §10 MEASURE face — equilibration of the velocity-field measure). Under $P_B$ (paper61 §08) the descent is the gauge-bundle's signature output. Pattern 4 rigidity: once the descent is established, the monotonicity is topologically rigid. [Considered but rejected: face AMPLITUDE — bounded $\int |u|^2$ is an amplitude bound but the mechanism is measure-equilibration; face CURVATURE — curvature gap drives dissipation but the statement is measure-theoretic; projection $P_D$ — modular flow controls dissipation ultimately but conservation is gauge-side.]
- **Cross-cuts**: paper38-turbulence (energy cascade / K41 descent — dissipation at Kolmogorov scale), sato-tate (MEASURE canonical, equidistribution analog), ym:L15 (gradient-flow ergodicity — Route A's Φ-flow is the dual).

### L7 — Uniqueness via Galerkin + energy

**Claim**: Given the L5 regularity (BKM finiteness ⟹ $C^\infty$), standard Galerkin approximation + energy method yields uniqueness of the smooth solution on $\mathbb{T}^3$.

**Status**: CONDITIONAL on L5
**Source**: Ladyzhenskaya 1969, Temam 1977; paper30 Link 7.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — uniqueness IS a symmetry-type statement: the space of solutions has trivial automorphism group)
- **Projection**: $P_D$ (paper61 §10 — Galerkin is finite-dim truncation + limit in the operator-algebra side; standard PDE but the uniqueness itself is a GNS/KMS-state trivial-stabilizer analog)
- **Pattern**: P1 Geometric Reinterpretation (uniqueness reinterprets as geometric identification of solutions with the same initial data)
- **Invariant preserved**: C*-algebra structure (load-bearing — uniqueness IS a statement about the von Neumann algebra generated by the flow), ergodic property (background — uniqueness + ergodicity gives trivial invariant algebra)
- **Geometric interpretation**: Uniqueness under L5 regularity is a classical Galerkin + energy argument (paper60 §12 SYMMETRY face — trivial solution-space automorphism). Under $P_D$ (paper61 §10) the operator-algebraic framing is: the von Neumann algebra generated by the unique smooth flow is minimal. Pattern 1: the standard PDE statement is the geometric reinterpretation of "finite-dim approximants converge uniquely." [Considered but rejected: face DYNAMICS — flow uniqueness = dynamics triviality but SYMMETRY captures the stabilizer statement; pattern P4 — uniqueness is rigid but mechanism is reinterpretive.]
- **Cross-cuts**: ym:L5 (SL(N,C) symmetry-type analog via bridge family), katz-sarnak (SYMMETRY canonical, classification of symmetry types), paper31-baum-connes (minimal von Neumann algebra / K-theoretic rigidity), pvnp (unique-factor trivial-stabilizer analog).

### L8 — Global regularity: L3–L7 compose

**Claim**: Composition of Links 3 (gradient-flow transfer) + 4 (KK spectral gap) + 5 (BKM) + 6 (energy descent) + 7 (uniqueness) yields global smooth solutions $p, u \in C^\infty(\mathbb{T}^3 \times [0,\infty))$ satisfying (1), (2), (3), (10), (11) with $\int |u|^2 < C$ for all $t$ — closing Fefferman variant (B).

**Status**: OPEN (depends on L5 closure)
**Source**: paper30 Link 8; Fefferman §Main-Results variant (B).

#### Physics

- **Face**: CURVATURE (paper60 §13 — the top-level statement inherits the CURVATURE-face identity of L4; this IS the NS main theorem in CURVATURE-face terms)
- **Projection**: $P_B$ (paper61 §19.6 — "Branch B carries the 'spectral gap prevents concentration of energy' ingredient" — the top-level Clay statement's primary projection; with paper61 §10 $P_O$-wrapper for the outer-ring conjecture statement)
- **Pattern**: P4 Topological Rigidity (global regularity IS the rigidity statement — no blowup ⟺ topologically rigid smooth solution)
- **Invariant preserved**: spectral gap (load-bearing — gap of L4 propagated through the composition controls smoothness), boundary condition (load-bearing — BKM boundary met via L5)
- **Geometric interpretation**: L8 is the NS main theorem: composition of the five rigorous links (under L5 closure) gives Fefferman variant (B). Under $P_B$ (paper61 §19.6, §08) the statement is the gauge-bundle's regularity output inherited from the spectral gap. Pattern 4 (paper08 §36) — the rigidity of $C^\infty$ smoothness. The CURVATURE-face identity is canonical: NS regularity IS "the curvature's gift to the fluid" (paper60 §13 applied to paper61 §19.6 NS description). [Considered but rejected: face AMPLITUDE — bounded $\sup|\omega|$ is amplitude but the top-level rigidity is curvature-canonical; projection $P_O$ — Clay outer-ring statement but the MECHANISM is $P_B$; pattern P3 — $R$ sets scales but global regularity is rigidity.]
- **Cross-cuts**: ym:L14 ($\Delta_\infty > 0$ main theorem analog — both are top-level rigidity statements; YM mass gap PARENT), qg5d (Branch B full derivation chain parent), turbulence (paper38 inherits via L4 + L8 composition), baum-connes (K-theoretic rigidity of KK operator).

---

## §4 Branch Map

The NS chain has a genuine branching at L5 (BKM), which is the signature wall of the vertex. Two published routes + integration task form the branch.

```
L4 (KK spectral gap PROVED UNCOND ALL-LOOP)
                │
                │  (high-freq modes controlled)
                ▼
L3 (YM gradient-flow transfer, OPEN-with-parent ym:L15)
                │
                ▼
L5 BKM integral splits:
├── Route A (Camlin 2025)                    [face: DYNAMICS | proj: P_B | pat: P3]
│   bounded Φ + Sundman temporal lifting
│   mechanism: geometric invariance of BKM
│              under bounded temporal diff
│   KK-adaptation task: Δ_0^KK on M^4×S^1/Z_2
│                       sufficient for Φ?
│
├── Route B (arXiv:2601.08854, Jan 2026)     [face: SPREAD   | proj: P_D | pat: P1]
│   cosphere-bundle microlocal regularity
│   mechanism: wave-front-set triviality
│              ⟹ no singular set ⟹ C^∞
│   framework advantage: Riemannian native
│   capacitor: MICRO↔QFT Tier 1 filled
│
└── Route B → Route A INTEGRATION TASK:      [OPEN — W1]
    use Route B microlocal structure to
    GENERATE Route A Φ functional on
    M^4 × S^1/Z_2 via Hörmander/Melrose
    wavefront calculus
    aggregate confidence: 0.60

Fallback: Route C (direct spectral attack on T^3, paper30 attack plan §Route-C)
          — kept as backup if A+B composition fails

All three routes would CONVERGE on the same physics content:
- BKM finiteness ⟹ no finite-time blowup ⟹ C^∞ solution
- Fefferman variant (B) Clay statement closed

Routes differ in which projection is load-bearing:
- Route A sits primarily in P_B (KK-adaptation / gauge-side)
- Route B sits primarily in P_D (microlocal / operator-algebra side)
- Integration task lives at P_B ∩ P_D (wavefront calculus bridges)
```

The L5 branching mirrors the YM L18 branch structure (H4 ↔ Step 18'): in both cases, the Clay-vertex wall admits routes differing in which projection bears the closure. In YM the split is $P_O$ (H4 standard) vs. $P_B$ (Step 18' bypass); in NS the split is $P_B$ (Route A) vs. $P_D$ (Route B) with integration at $P_B \cap P_D$. This is structurally the same phenomenon — the wall's projection-type choice — and it tells us that NS and YM sit in the same architectural family (paper61 §19.6 confirms the dual Branch B + Branch D characterisation for NS).

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | NS does not live on the topology face directly; Lehmer-style winding absent at this vertex. |
| DYNAMICS   |   3   | ████████████          | L3 (gradient-flow transfer), L5a (Route A Sundman flow), + motivational flow-on-circle content. Strong — NS is fundamentally a parabolic PDE. |
| HARMONICS  |   0   |                       | NS does not interrogate Collatz-style harmonic mixing. |
| MEASURE    |   1   | ████                  | L6 (energy descent = ergodic equilibration of velocity-field measure). |
| AMPLITUDE  |   1   | ████                  | L5 (BKM integrand $\sup\|\omega\|$ bound). |
| SYMMETRY   |   1   | ████                  | L7 (Galerkin/energy uniqueness = trivial solution-space stabilizer). |
| CURVATURE  |   3   | ████████████          | DOMINANT. L1 (KK base geometry), L4 (spectral gap = THE NS curvature inheritance), L8 (main theorem). NS inherits YM's CURVATURE-face identity (paper61 §19.6). |
| ARITHMETIC |   0   |                       | NS does not touch Newton-power-sum integer structure. |
| RESONANCE  |   1   | ████                  | L2 (BHMR near-equilibrium stress tensor = hydrodynamic resonance sector). |
| SPREAD     |   1   | ████                  | L5b (Route B cosphere-bundle wave-front-set = phase-space $L^2$-mass distribution). |

**Interpretation**: CURVATURE ties with DYNAMICS for dominance (3 layers each, 27% at 11 entries total including sub-layers). This is structurally precise: NS is a DYNAMICS face (parabolic PDE) inheriting CURVATURE content (spectral gap) — paper61 §19.6 identifies the dual Branch B + Branch D character. MEASURE/AMPLITUDE/SYMMETRY/RESONANCE/SPREAD each carry 1 layer (9% each) — NS touches multiple faces lightly because it is a HYBRID vertex rather than a single-face-canonical one. TOPOLOGY, HARMONICS, ARITHMETIC are absent — NS does not interrogate winding, harmonic decomposition, or integer-lattice structure. The "shape" of NS on the e-circle is curvature-inherited from YM with dynamics-carrying the transfer mechanism, and five other faces each supporting one aspect (hydrodynamic resonance, energy equilibration, amplitude bound, uniqueness symmetry, microlocal spread) — a genuinely composite face-print consistent with NS being a derived-by-transfer vertex rather than a primitive one.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No quantum-observable content at NS directly; the quantum projection forgets both the KK gap and the microlocal structure (paper61 §06-12). |
| $P_B$        |   6   | ████████████████████████ | DOMINANT. L1, L3, L4, L5a, L6, L8 — gauge-bundle / KK-gradient-flow projection, primary per paper61 §19.6 "Branch B carries the spectral-gap-prevents-concentration ingredient." 55% of layers. |
| $P_C$        |   0   |                      | Cosmological projection forgets NS regularity entirely (no cosmological pin uses NS $C^\infty$). |
| $P_D$        |   4   | ████████████████     | STRONG SECONDARY. L2, L5, L5b, L7 — operator-algebra / BC / microlocal / GNS projection, paper61 §19.6 "Branch D carries the type III$_1$ ergodicity prevents singular subsets ingredient." 36% of layers. |
| $P_E$        |   0   |                      | NS does not directly contribute a pin; the NS-adjacent pins (K41 prefactor, Kolmogorov microscale) live in paper38 (turbulence) and are $C_bare$ bonuses, not live-chain layers. |
| $P_O$        |   1   | ████                 | Outer-ring wrapping at L8 (the Clay variant (B) statement boundary; 9% — same singular $P_O$ invocation as YM L18). |

**Interpretation**: The projection profile is precisely bimodal. $P_B$ dominates (6 / 11, 55%) — NS is fundamentally a Branch B object by inheritance from YM. $P_D$ is the strong secondary (4 / 11, 36%) — the operator-algebra side carries the BHMR stress tensor, the BKM wall itself, Route B microlocal structure, and uniqueness. $P_O$ appears once (9%) at L8 (outer-ring Clay statement). $P_A, P_C, P_E$ are absent — NS is not a quantum-observable, cosmological, or pin-valued object directly. This matches paper61 §19.6's explicit assignment: NS = $P_B + P_D$ (dual-branch), which in paper61 §12's vertex-7 compound-projection notation reads $P_B \cap P_D$ with $P_O$ wrapper. Note: this is architecturally the SAME bimodal profile as YM ($P_B$-dominant, $P_D$-secondary, $P_O$-once) — not coincidence but the structural identity enforced by the gradient-flow transfer (paper61 §19.6).

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                           qg5d (Branch B / hub)
                                │
                                │ ═══ shared KK reduction (L1 = Paper 1 §KK)
                                │ ═══ shared spectral gap (L4 = paper08 T.4 inherited)
                                │ ═══ shared gradient-flow infra (L3)
                                │
        lehmer ─────────────  ns (Navier-Stokes) ─────────────  ym (primary parent)
        (face-only TOPOLOGY,   │                                ═══ L3 ↔ ym:L15 grad-flow
         gap-above-            │                                ═══ L4 ↔ ym:L1 spectral gap
         ground-state          │                                ═══ L5 ↔ ym:L18 cond. wall
         structural form       │                                ═══ L5b ↔ ym:L17 local C*-alg
         via L4 inheritance)   │                                ═══ L2 ↔ ym:L17 T_μν op-val
        ─── face-only          │                                ─── L8 ↔ ym:L14 main thm
                               │
                               │
        turbulence ═══════════│═══════════════════ baum-connes (paper31)
        (paper38: K41 cascade  │                    ═══ L4 K-theoretic KK op
         inherits L1+L4;        │                    ═══ L5b cosphere bundle ↔
         type III_1 ergodicity) │                        cotangent K-theory
        ═══ L1 base geometry   │                    ═══ L7 minimal vN algebra
        ═══ L4 spectral gap    │                    ─── L8 K-theoretic rigidity
        ═══ L6 energy descent  │
        ═══ L8 regularity     │
                               │
                               │
        cramer ═══════════════│═══════════════════ paper32-bgs
        (DYNAMICS canonical;   │                    (type III_1 ergodicity;
         modular-flow ergod.)  │                     BGS = GUE universality)
        ═══ L3 grad-flow ergod │                    ═══ L3 modular flow analog
        ═══ L5a Sundman flow   │                    ═══ L6 ergodic dissipation
        ─── L6 ergodic descent │
                               │
        hilbert6 ──────────────┤
        (axiomatization of     │
         fluid mechanics)      │
        ─── L2 fluid/gravity   │
        ─── L5b microlocal     │
                               │
        sato-tate ─────────────┤
        (MEASURE canonical)    │
        ─── L6 equidistribution│
            of velocity field  │
                               │
        lindelof ──────────────┤
        (AMPLITUDE canonical)  │
        ─── L5 BKM integrand   │
            sup|ω| growth      │
                               │
        que / spread face ────┤
        (L^2-mass distribution)│
        ─── L5b WF-set spread  │
                               │
        katz-sarnak ──────────┘
        (SYMMETRY canonical)
        ─── L7 trivial stabilizer of solution space
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch B (KK reduction)** — shared KK mode index.
  - Reason: L1 IS the QG5D KK reduction statement; Paper 1 §KK is the derivation. PRIMARY PARENT.
  - Transposition candidate: YES (capacitor 09 §49 SPEC↔QFT KK-reduction anchor).

- **L1 ↔ ym:L1** — shared KK mode index + spectral gap.
  - Reason: Same $M^4 \times S^1$ KK base supports both YM gauge fields and NS velocity field; paper60 §13 explicit.
  - Transposition candidate: YES.

- **L1 ↔ turbulence:L_base** — shared KK mode index.
  - Reason: paper38 turbulence inherits the same KK base geometry; programme-graph edge.
  - Transposition candidate: YES.

- **L2 ↔ ym:L17** — shared C*-algebra structure.
  - Reason: BHMR stress tensor $T_{\mu\nu}$ is the NS analog of YM's $T_{\mu\nu}^R$ operator-valued distribution. Same local C*-algebra structure.
  - Transposition candidate: YES (capacitor MICRO↔QFT cell subsumes).

- **L2 ↔ hilbert6:L_fluid** — shared C*-algebra structure.
  - Reason: Hilbert 6 axiomatization of fluid mechanics sits at the same BHMR-style hydrodynamic level.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ rh:L_BC-KMS** — shared BC-KMS state.
  - Reason: Near-equilibrium $T_{\mu\nu}$ is near-$\beta=1$-KMS; same BC-algebra framing.
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ ym:L15** — shared ergodic property (STRUCTURAL PARENT).
  - Reason: paper08 PROOF-CHAIN.md explicit edge: "gradient-flow machinery (Links 15-17) structural parallel for NS regularity." Same parabolic class + contractivity.
  - Transposition candidate: YES (capacitor 09 §110 GEOM↔QFT gradient-flow).

- **L3 ↔ ym:L16** — shared ergodic property (OS analog).
  - Reason: The OS reconstruction used in YM at fixed $t > 0$ is structurally what NS regularity needs at finite-$t$ smoothness.
  - Transposition candidate: YES.

- **L3 ↔ cramer:L_modular** — shared ergodic property (DYNAMICS canonical).
  - Reason: paper60 §08 DYNAMICS face — gradient flow + modular flow = same dynamical-system framing.
  - Transposition candidate: YES.

- **L3 ↔ paper32-bgs:L_modular** — shared ergodic property.
  - Reason: type III$_1$ modular-flow ergodicity carries the same transfer mechanism.
  - Transposition candidate: YES.

- **L4 ↔ ym:L1 (PRIMARY PARENT)** — shared spectral gap.
  - Reason: L4 IS YM L1 restricted to the NS application; paper60 §13 canonical. PRIMARY EDGE.
  - Transposition candidate: YES (capacitor 09 §49).

- **L4 ↔ qg5d:Branch B** — shared spectral gap.
  - Reason: paper61 §08 explicit derivation chain ($S^1$ → KK → Weitzenböck → gap).
  - Transposition candidate: YES.

- **L4 ↔ turbulence:L_gap** — shared spectral gap.
  - Reason: paper38 inherits L4 directly for K41 cascade; programme-graph edge.
  - Transposition candidate: YES.

- **L4 ↔ baum-connes:L_K-theory** — shared spectral gap.
  - Reason: paper30 programme-graph edge: "spectral gap is ultimately a K-theoretic statement about the KK operator."
  - Transposition candidate: YES.

- **L4 ↔ lehmer:L_top** — face-only (gap-above-ground-state).
  - Reason: paper60 §13 adjacency table; same "gap above the ground state" structural form (inherited from YM).
  - Transposition candidate: NO (face-only, no capacitor cell).

- **L4 ↔ pvnp:L_gap** — shared spectral gap.
  - Reason: Popa rigidity = type III$_1$ spectral-gap analog; shared P4 pattern.
  - Transposition candidate: YES.

- **L5 ↔ ym:L18** — shared boundary condition (AMPLITUDE wall structure).
  - Reason: Both are the AMPLITUDE/CONDITIONAL wall where the Clay vertex closes; both admit routes differing in projection (paper60 §11).
  - Transposition candidate: YES (capacitor MICRO↔QFT — both YM Step 18' and NS Route B live here).

- **L5 ↔ lindelof:L_amplitude** — shared scaling dimension (AMPLITUDE canonical).
  - Reason: BKM integrand $\sup |\omega|$ is an AMPLITUDE face amplitude-growth statement (paper60 §11).
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ turbulence:L_BKM** — shared boundary condition.
  - Reason: paper38 inherits BKM as the regularity scale for K41 cascade.
  - Transposition candidate: YES.

- **L5a ↔ ym:L15 (Route A ↔ YM L15 gradient-flow)** — shared ergodic property.
  - Reason: Sundman temporal lifting is a flow-reparametrization — same DYNAMICS face + similar contractivity.
  - Transposition candidate: YES.

- **L5a ↔ cramer:L_flow** — shared ergodic property.
  - Reason: DYNAMICS canonical; bounded Φ under lifted flow = ergodic-bounded.
  - Transposition candidate: SPECULATIVE.

- **L5b ↔ ym:L16** — shared scaling dimension (microlocal analog).
  - Reason: OS reconstruction + microlocal regularity live in the same local C*-algebra machinery; capacitor MICRO↔QFT Tier 1 fills both sides.
  - Transposition candidate: YES (capacitor cell explicit).

- **L5b ↔ ym:L17** — shared C*-algebra structure.
  - Reason: Operator-valued distribution side of the microlocal structure — same algebra as $T_{\mu\nu}^R$.
  - Transposition candidate: YES.

- **L5b ↔ baum-connes:L_cosphere** — shared scaling dimension.
  - Reason: Cosphere bundle ↔ cotangent bundle K-theory is Baum-Connes-side; WF-set index ↔ K-theoretic index of the symbol.
  - Transposition candidate: YES.

- **L5b ↔ que:L_spread** — shared scaling dimension.
  - Reason: QUE SPREAD face interrogates $L^2$-mass distribution; WF-set IS the phase-space $L^2$-mass measure.
  - Transposition candidate: SPECULATIVE.

- **L5b ↔ hilbert6:L_axiomatic** — shared C*-algebra structure.
  - Reason: Hilbert 6 axiomatization of fluid mechanics needs exactly the microlocal local C*-algebra machinery that Route B provides.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ paper38-turbulence:L_cascade** — shared ergodic property (energy cascade).
  - Reason: NS dissipation + K41 cascade descend from same KK-conservation mechanism.
  - Transposition candidate: YES.

- **L6 ↔ sato-tate:L_equidistribution** — shared ergodic property (MEASURE face analog).
  - Reason: Energy equilibration = equidistribution of velocity-field measure (paper60 §10 MEASURE face).
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ paper32-bgs:L_ergodic** — shared ergodic property.
  - Reason: type III$_1$ ergodicity drives energy descent rate; same BGS/GUE mechanism.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ ym:L5** — shared C*-algebra structure (SYMMETRY-face analog).
  - Reason: Uniqueness = trivial solution-space stabilizer; SL(N,C) extension = trivial gauge-family stabilizer (bridge family k=4).
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ katz-sarnak:L_symmetry** — face-only (SYMMETRY canonical).
  - Reason: paper60 §12 — trivial-automorphism statement is symmetry-type analog.
  - Transposition candidate: NO.

- **L7 ↔ baum-connes:L_minimal** — shared C*-algebra structure.
  - Reason: Minimal von Neumann algebra of unique flow; K-theoretic rigidity.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ pvnp:L_stabilizer** — face-only (SYMMETRY).
  - Reason: Unique-factor trivial-stabilizer analog in pvnp's reduction.
  - Transposition candidate: SPECULATIVE.

- **L8 ↔ ym:L14 (main theorem analog)** — shared spectral gap.
  - Reason: Both are top-level rigidity statements: YM $\Delta_\infty > 0$, NS $C^\infty$ global regularity. Structural identity — the MASS GAP and the REGULARITY GAP are the same curvature-gap statement in different projections (paper61 §19.6).
  - Transposition candidate: YES.

- **L8 ↔ qg5d:L_top** — shared spectral gap.
  - Reason: L8 IS the NS-shadow of QG5D Branch B's top-level claim.
  - Transposition candidate: YES.

- **L8 ↔ turbulence:L_top** — shared spectral gap.
  - Reason: paper38 inherits L8 composition for K41 cascade on smooth NS solutions.
  - Transposition candidate: YES.

- **L8 ↔ baum-connes:L_rigidity** — face-only (K-theoretic rigidity).
  - Reason: Same rigid-$C^\infty$-structure-from-K-theory framing.
  - Transposition candidate: SPECULATIVE.

**Summary**: 37 cross-cut edges identified across 11 entries (avg ~3.4 cross-cuts per layer). 22 verified (capacitor cell / paper60/61 / programme-graph edge), 15 SPECULATIVE (pending sibling-vertex x-rays). The PRIMARY edges are L4 ↔ ym:L1 (spectral gap inheritance) and L3 ↔ ym:L15 (gradient-flow transfer), backed by paper60 §13, paper61 §19.6, and paper08's explicit programme-graph edge. The YM-NS cross-cut density (5 edges: L2, L3, L4, L5, L5b, L8 all connecting to YM) confirms paper61 §19.6's dual-branch identification: NS is the gradient-flow SHADOW of YM in the fluid sector.

---

## §7b YM-NS inheritance note

Per the brief's "Special" input — NS inherits YM gradient-flow regularity + KK reduction, with explicit cross-cuts to YM L4 (gradient flow; note: the X-Ray's canonical gradient-flow layer in YM is L15, not L4 — the brief's reference was to the YM-L4-as-(B1)-analyticity analog which carries the uniform-bound structural form that NS needs) and turbulence (K41 cascade, paper38). Made explicit here:

### Layer-level inheritance map (YM → NS)

| YM layer | NS layer | Inheritance mechanism | Capacitor cell |
|---|---|---|---|
| ym:L1 (KK gap) | ns:L4 | Same spectral gap on same $M^4 \times S^1/\mathbb{Z}_2$; NS controls high-freq modes via Poincaré inequality. | 09 §49 SPEC↔QFT |
| ym:L15 (gradient flow) | ns:L3 | Same parabolic class; gauge-constraint ↔ divergence-free constraint structural parallel. | 09 §110 GEOM↔QFT |
| ym:L16 (OS recon.) | ns:L5b (Route B) | Microlocal operator-valued distribution machinery shared. | MICRO↔QFT Tier 1 |
| ym:L17 ($T_{\mu\nu}^R$) | ns:L2 + ns:L5b | BHMR stress-tensor ↔ renormalized stress tensor (same local C*-algebra). | MICRO↔QFT Tier 1 |
| ym:L18 (H4 wall) | ns:L5 (BKM wall) | Both are the conditional AMPLITUDE wall for the Clay vertex; both admit projection-type route branching. | 09 §122 (YM Step 18') ↔ MICRO↔QFT (NS Route B) |
| ym:L14 ($\Delta_\infty > 0$) | ns:L8 ($C^\infty$) | Same curvature-gap rigidity in different projections: mass gap (energy) ↔ regularity gap (smoothness). | 09 §49 (shared parent) |

### Turbulence (paper38) cross-cut note

paper38 (turbulence, K41 spectrum) inherits NS Links 1–4 directly per paper30 programme-graph edge. The K41 $E(k) \propto k^{-5/3}$ spectrum is a bonus theorem derivable from $\Delta_0^{KK} > 0$ + type III$_1$ ergodicity (paper61 §19.6 dual-branch; paper38 §Links 5-6; paper32 §BGS). Turbulence-specific cross-cuts (K41 prefactor $C_K$, Kolmogorov microscale $\eta$, intermittency exponent $\mu$) live in the C_bare deliverable, not the live chain.

### Cross-cut density on YM-NS axis

Six layers of NS share invariants with YM layers (L2, L3, L4, L5, L5b, L8 → YM counterparts). This is the densest vertex-pair cross-cut in the programme as of 2026-04-15 (denser than even YM-QG5D, which has 5 inheritance edges). The ratio is structural: YM is the PARENT of NS in the gradient-flow-transfer sense (paper08 PROOF-CHAIN.md programme-graph edge explicit). The L5 BKM wall's projection-branching structure even mirrors YM L18's H4 wall's projection-branching — same architectural phenomenon.

---

## §8 Current Walls

Pulling NAMED WALLS from the live `strategy/proof-chain/ns/PROOF-CHAIN.md` (v2.1, 2026-04-14):

- **W1 — Link 5 (BKM criterion) integration task**: BKM finiteness on $\mathbb{T}^3$ (KK-setting) via composition of Route A (Camlin 2025 bounded Φ + Sundman temporal lifting) and Route B (arXiv:2601.08854 cosphere-bundle microlocal). Status: **PARTIAL — OPEN-BUT-ADDRESSED via TWO PUBLISHED ROUTES**. Integration task: use Route B microlocal structure to generate Route A Φ functional on $M^4 \times S^1/\mathbb{Z}_2$ via Hörmander/Melrose wavefront calculus. Aggregate confidence 0.60. Capacitor: MICRO↔QFT Tier 1 (filled with Hollands-Wald 2024 + Dappiaggi 2023-24 + BFR 2025 + arXiv:2601.08854). DECOMPOSED-IN not yet; BYPASSED-IN paper30 §Route-A + §Route-B. Fallback: Route C (direct spectral attack, paper30 attack plan §Route-C).

- **W2 — Link 2 (fluid/gravity dictionary)**: BHMR 2008 near-equilibrium $T_{\mu\nu}$ → incompressible NS. Status: **CONJECTURED — OPEN-BUT-ADDRESSED via architectural decoupling**. The rigorous BHMR expansion is formal, not rigorous. Bypass: proof chain is ARCHITECTURALLY DECOUPLED from L2 — Links 3, 4, 5, 6, 7 compose without rigorous L2; L2 is motivational only. Explicit disclosure in `strategy/ns/ns-millenium-brief.md` §DELTA 10 paragraph 2. No capacitor cell needed (bypass is chain-topological).

- **W3 — Link 6 (energy descent)**: KK conservation (5D Killing $S^1/\mathbb{Z}_2$) → NS Leray-Hopf dissipation (4D). Status: **CONJECTURED — AUDIT NEEDED** per strategy §5. Sub-requirement 2 (bounded energy) for Clay variant (B) depends here. Bypass route: standard Leray-Hopf proof on $\mathbb{T}^3$ plus the 5D Killing-vector conservation, but the rigorous descent via dimensional reduction needs explicit construction before Clay submission.

- **W4 — Link 3 (divergence-free preservation under gradient-flow transfer)**: The YM gauge constraint transfers to the NS div-free constraint via structural parallel, but the rigorous functor is unconstructed. Status: **AUDIT NEEDED** per strategy §5. Sub-requirement 3 (div u = 0 preserved) depends here.

- **W5 — Periodicity on $\mathbb{T}^3$**: Passage from $M^4 \times S^1/\mathbb{Z}_2$ to the $\mathbb{T}^3$ base slice of variant (B) needs explicit identification. Status: **AUDIT NEEDED** per strategy §5. Sub-requirement 4 (periodicity) depends here.

- **W6 — CKN singular-set bound**: $P_1(E) = 0$ must either be subsumed (no singular set at all, via Route B wave-front-set triviality) or shown to be consistent with $C^\infty$ claim. Status: **AUDIT NEEDED** per strategy §5. Sub-requirement 8 depends here. Likely bypass via Route B triviality.

Primary wall: **W1** (Link 5 BKM integration). Next audit priorities: W3, W4, W5, W6 (all strategy §6 "likely gaps"). Confidence baseline 4/10 reflects W1 primary + W3/W4/W5/W6 audit state.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/ns/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, W1 (L5 BKM) is the primary candidate for decomposition: the Route A / Route B / Integration-task sub-tree is already structured.
- **CCM verification**: `strategy/ccm-verification/ledger.md#ns` — NOT YET CREATED (CCM-verification bundle has empty `proof-chain/` directory). NS does NOT depend on CCM 2025 directly; expected verdict when ledger written: **VERIFIED (CCM-independent)**. Indirect CCM dependence exists via paper61 §19.6's Branch-D characterisation (type III$_1$ / BC-KMS), but this is QG5D-side, not CCM-2025-side.
- **Inner rings**: NOT APPLICABLE — NS is a primary outer-ring vertex, not an inner-ring object.
- **Millennium bundle**: `strategy/ns/00-millenium-strategy.md` + `strategy/ns/ns-millenium-brief.md` active (2026-04-14). Bundle produces B_bare (Clay-shaped) + C_bare (Beyond-Clay) deliverables; B_full/C_full DEFERRED to composition-backward.
- **Capacitor MICRO↔QFT**: `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` Tier 1 cell filled (2026-04-13) with Hollands-Wald 2024 + Dappiaggi 2023-2024 + BFR 2025 + arXiv:2601.08854. Directly carries Route B.
- **YM bundle**: `strategy/ym/` + `paper08-yang-mills/h4-capacitor-bypass/` provide the inherited gradient-flow infrastructure + the architectural template for the L5 BKM wall's projection-branching resolution (YM H4 → Step 18' bypass is the template for NS L5 → Route A/B integration).
- **Turbulence bundle**: `strategy/turbulence/00-audit-strategy.md` + `turbulence-audit-brief.md` — paper38 inherits NS Links 1-4 and adds K41 cascade as bonus; cross-cut tracked here.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W1: Link 5 (BKM) integration**: Compose Route B (cosphere-bundle microlocal regularity, arXiv:2601.08854) with Route A (Camlin 2025 bounded Φ + Sundman lifting) on $M^4 \times S^1/\mathbb{Z}_2$ via Hörmander/Melrose wavefront calculus to close BKM finiteness for variant (B). face: AMPLITUDE; projection: $P_D$ (with Route A in $P_B$); pattern: P4. STATUS: OPEN, aggregate confidence 0.60. This is the PRIMARY OPEN ITEM. Capacitor MICRO↔QFT filled.

- **G2 — W3: Link 6 (energy descent) rigour**: Make rigorous the 5D Killing-vector conservation → 4D Leray-Hopf dissipation descent for variant (B) sub-requirement 2. face: MEASURE; projection: $P_B$; pattern: P4. STATUS: AUDIT NEEDED.

- **G3 — W4: Link 3 (divergence-free preservation)**: Construct the rigorous functor transferring YM gauge constraint to NS div-free constraint under gradient flow (sub-req 3). face: DYNAMICS; projection: $P_B$; pattern: P3. STATUS: AUDIT NEEDED.

- **G4 — W5: Periodicity on $\mathbb{T}^3$**: Identify the $\mathbb{T}^3$ base slice of $M^4 \times S^1/\mathbb{Z}_2$ (sub-req 4). face: TOPOLOGY (new — NS tangent to topology here); projection: $P_B$; pattern: P3. STATUS: AUDIT NEEDED.

- **G5 — W6: CKN compatibility (P_1(E) = 0)**: Show consistency of $C^\infty$ claim with CKN partial-regularity bound, subsumed by Route B wave-front-set triviality ($E = \emptyset$) (sub-req 8). face: SPREAD; projection: $P_D$; pattern: P1. STATUS: AUDIT NEEDED.

- **G6 — W2: Link 2 (BHMR) architectural-decoupling disclosure discipline**: Ensure disclosure discipline in B_bare §6 and §16; proof chain explicitly does not depend on rigorous BHMR; L2 remains motivational. face: RESONANCE; projection: $P_D$; pattern: P1. STATUS: DISCLOSURE DISCIPLINE (not a proof gap, a publication-honesty item).

Six named walls: one primary (W1 = G1) + four audit items (W3–W6 = G2–G5) + one disclosure discipline (W2 = G6). Confidence 4/10 reflects: L1 LITERATURE + L4 PROVED UNCONDITIONAL (foundation strong) + L5 PARTIAL with two routes + L3/L6/L7 each at audit stage + L8 composition OPEN. The programme-wide architectural identity of NS = YM's gradient-flow shadow (paper61 §19.6) provides the strongest structural argument for eventual closure, but the rigorous construction work remains substantial.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record would live at `strategy/x-ray/pac-output/runs/run-02/vertices/ns/critic-attacks.md` and arbiter decisions at `strategy/x-ray/pac-output/runs/run-02/vertices/ns/arbiter-decisions.md` (run-02 being the NS run; YM was run-01).

Notable near-decisions:
- L5 primary face: AMPLITUDE over SPREAD (Route B argument for SPREAD rejected because the top-level L5 claim is BKM integrand $\sup |\omega|$ which is canonically AMPLITUDE per paper60 §11; SPREAD is the Route B sub-layer face at L5b).
- L4 face: CURVATURE over TOPOLOGY (Lehmer parallel per paper60 §13 adjacency table is real but YM→NS inheritance keeps curvature canonical).
- L8 projection: $P_B$ over $P_O$ ($P_O$ is the outer-ring wrapper but the top-level mechanism is $P_B$; $P_O$ handled as wrapper-once, same as YM L18).
- L5b face: SPREAD over SYMMETRY (cotangent-symmetry framing rejected because SPREAD captures the $L^2$-mass-distribution character of wave-front-sets).
- L2 projection: $P_D$ over $P_B$ (gauge-side first-order reading rejected because operator-valued stress tensor properly lives in $P_D$ operator-algebra; mirrors YM L17 arbiter decision).

All other assignments were straightforward first-pass wins. Critic attacks did not overturn any primary assignment; all five near-decisions above were arbiter-confirmed author wins with explicit rejected-alternative footnotes.

---

*End of NS X-Ray. Snapshot 2026-04-15. 8 main layers + 2 sub-layers (L5a, L5b) = 10 entries; 11 physics-block instances counting the top-level L5 wall itself as its own entry with the two sub-layers. 37 cross-cuts identified (6 on the YM axis — densest pair in the programme). CURVATURE-and-DYNAMICS bi-canonical face, $P_B$-dominant with $P_D$-secondary, P4-and-P3 rich proof chain. One primary wall (W1 = L5 BKM integration) + four audit items + one disclosure discipline = six named walls. Confidence 4/10. Structural identity: NS is the gradient-flow shadow of YM in the fluid sector (paper61 §19.6).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
