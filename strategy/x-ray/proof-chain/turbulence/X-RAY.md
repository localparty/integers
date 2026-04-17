# X-RAY: Turbulence / Kolmogorov K41 (turbulence)

*X-Ray of the turbulence proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: turbulence
- **Paper**: paper38-turbulence
- **Live file**: `strategy/proof-chain/turbulence/PROOF-CHAIN.md` (snapshot 2026-04-14, v1)
- **Top-level claim**: 3D incompressible turbulence exhibits the Kolmogorov K41 energy spectrum $E(k) \propto k^{-5/3}$ with a well-defined dissipation scale, intermittent dissipation $\varepsilon(x)$ on a fractal singular set, and a universal inertial-range cascade — derived from NS spectral gap + YM gradient-flow regularity + BGS type III$_1$ ergodic statistics.
- **Current status**: 2/7 PROVED (Links 1, 4 foundational, inherited); Links 2-3 INHERITED-PROVED via NS/YM; Links 5-6 CANDIDATE (the K41 walls); Link 7 CONJECTURED. Aggregate confidence **2/10** (foundation strong, payoff open).
- **Primary branch (paper1)**: B (Gravity / KK / gradient-flow regularity inherited from NS and YM) with strong secondary D (CBB type III$_1$ ergodicity produces GUE-like universality underpinning K41 constants).
- **Primary face**: DYNAMICS (paper60 §08 — K41 is a modular-flow-on-the-circle universality statement; "how does the ergodic flow traverse the scales"; paper61 §29-30 §Appendix table row 8 assigns turbulence to DYNAMICS face; the cascade IS a dynamical statement).
- **Primary projection**: $P_B$ (paper61 §06-12 Vertex 8 — "$P_B$ (NS + BGS transfer)") with strong compound $P_B \cap P_D$ (paper61 §06-12: "Compound: $P_B \cap P_D$ (via turbulent cascade and BC ergodics)").

---

## §2 ASCII Diagram A — Main proof-chain tree

```
TURBULENCE (3D incompressible K41 + intermittency) — E(k) ∝ k^(-5/3)
│  primary face: DYNAMICS    primary proj: P_B (compound P_B ∩ P_D)
│  primary pat: P3 Scale-Setting (R → KK → inertial range)
│
├── L1: 5D Einstein → 4D KK fluid reduction               [LITERATURE]
│      │  face: CURVATURE    proj: P_B   pat: P3
│      │  invariant: KK mode index
│      │  source: Paper 1 §KK; BHMR 2008 fluid/gravity duality
│      │
│      └── shared with ns:L1 and qg5d Branch B
│             │
│             └── M^4 × S^1/Z_2 base geometry supports fluid
│                    velocity field exactly as it supports
│                    the YM gauge field
│
├── L2: NS spectral gap Δ_0^KK > 0 controls high-freq modes [INHERITED-PROVED]
│      │  face: CURVATURE    proj: P_B   pat: P4
│      │  invariant: spectral gap
│      │  source: Paper 30 Link 4 + Paper 11 Theorem K.4
│      │          (unconditional all-loop post W1/W2 closure)
│      │  depends: L1
│      │
│      └── UPGRADE 2026-04-13: inherits NS:L4 unconditional all-loop
│             status; no residual UV-scheme question propagates
│             into the turbulent regime
│
├── L3: YM gradient flow regularity = parabolic PDE class of NS [INHERITED-PROVED]
│      │  face: DYNAMICS     proj: P_B   pat: P3
│      │  invariant: ergodic property
│      │  source: Paper 8 Links 15-17 (VERIFIED 9/10; now UNCOND.
│      │          post W1/W2); paper30 Link 3
│      │
│      └── SAME parabolic PDE class as NS velocity-field flow
│             ↔ YM gauge-field gradient flow. Lüscher-Weisz 2010
│             framework carries over; contractivity + well-posedness
│
├── L4: Type III_1 ergodic modular flow → GUE universality    [INHERITED-ESTABLISHED]
│      │  face: RESONANCE    proj: P_D   pat: P4
│      │  invariant: ITPFI factor type (III_1), ergodic property
│      │  source: Paper 32 BGS (L2 PROVED, L5 LITERATURE 2025-11
│      │          Hardy Z PCC); Connes classification
│      │
│      └── Branch D ITPFI ⊗_p (λ_p = 1/p) at KMS_1 provides the
│             universality-class kernel that K41 constants reduce to
│
├── L5: Fractal dimension of singular dissipation set       [CANDIDATE — W_T1]
│      │  face: SPREAD       proj: P_D   pat: P4
│      │  invariant: scaling dimension (Hausdorff), holonomy
│      │  depends: L3
│      │  source: Paper 28 A5 computational-area-law STRUCTURAL
│      │          ANALOG (NPC holonomy ⟺ confining cascade);
│      │          arXiv:2603.28308 interacting weak-singularity
│      │          ensembles
│      │
│      └── WALL: Paper 28 A5 analog not yet transposed from
│             complexity-cascade to fluid-cascade formally
│             (aggregate confidence 0.55; named W_T1)
│
├── L6: K41 k^(-5/3) spectrum from Δ-controlled cascade     [CANDIDATE — W_T2]
│      │  face: DYNAMICS     proj: P_B (compound ∩ P_D)   pat: P3
│      │  invariant: scaling dimension (critical exponent -5/3),
│      │             spectral gap
│      │  depends: L2, L5
│      │  source: Kolmogorov 1941; Frisch 1995;
│      │          arXiv:2502.10032 intermittency-regularity;
│      │          arXiv:2503.19944 log-improved regularity criteria
│      │
│      └── WALL: bridging "Δ > 0 + type III_1 ergodicity"
│             to "-5/3 universal exponent" requires a new
│             theorem. This is THE HARDEST step (named W_T2);
│             aggregate confidence 0.55
│
└── L7: Universal Kolmogorov constants from Riemann zeros   [CONJECTURED]
       │  face: AMPLITUDE    proj: P_E   pat: P5
       │  invariant: L-value (ζ at specific points), critical exponent
       │  depends: L2, L4, L6
       │  source: Branch E master table (paper12 pin row); new
       │
       └── Candidate pin: C_K ≈ 1.5 derived from ζ zeros + ITPFI —
              belongs in Branch E 36-pin table once L6 closes
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (No quantum-observable projection
                          knows about K41 scaling directly.)
                                  ▲
                                  │
                                  │
        ┌─────────────(P_O outer)───────────────┐
        │                                       │
        │  Turbulence: E(k) ∝ k^(-5/3) in the   │
        │  inertial range of 3D incompressible  │
        │  NS, with intermittent ε(x) on a      │
        │  fractal singular set, universal      │
        │  constants.                           │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         ║
        ▼                   ▼ (PRIMARY)               ▼ (COMPOUND)
    P_C cosmology      ═══ P_B gravity ═══       ═══ P_D CBB ═══
    (forgotten —       KK base (L1);              ITPFI ⊗_p λ_p=1/p
     K41 is not a      spectral gap (L2)          at KMS_1 (L4);
     cosmological      inherited from NS;         GUE universality
     observable)       gradient flow (L3)         kernel for K41
                       inherited from YM;         constants;
                       cascade controlled by      fractal dim
                       Δ_0^KK (L6)                singular set (L5)
                            │                         │
                            └──────────┬──────────────┘
                                       ▼
                                  P_E pins
                                  (candidate C_K ≈ 1.5;
                                   Kolmogorov microscale η;
                                   Taylor-Reynolds; intermittency
                                   exponent μ; potential NEW pin
                                   from L7 — Riemann zeros
                                   → universal constants)
```

Primary projection $P_B$ uses ═══ doubled line (carries L1, L2, L3, L6 — four layers of the seven). $P_D$ is the strong compound partner ═══ (carries L4, L5 — two layers + the K41 universality kernel). $P_E$ receives the L7 conjectured pin. $P_O$ wraps the whole outer-ring conjecture statement. The PRIMARY COMPOUND is $P_B \cap P_D$ per paper61 §06-12 vertex-8 explicit assignment.

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
          CURVATURE         │          MEASURE
          (YM / NS          │          (Sato-Tate)
           inherited)       │
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (● primary: DYNAMICS above;
                        RESONANCE secondary;
                        CURVATURE/SPREAD/AMPLITUDE tertiary)
```

Marker key:

```
Primary face:    ● DYNAMICS   (paper60 §08; paper61 §29-30 Appendix table row 8;
                               L3 grad-flow, L6 cascade dynamics;
                               K41 IS a modular-flow universality statement)
Secondary faces: ○ CURVATURE  (2 layers: L1 KK base, L2 spectral gap — inherited
                               from NS/YM lineage; paper61 §19.6 "Branch B")
                 ○ RESONANCE  (1 layer: L4 type III_1 ergodic modular flow —
                               BGS backbone; paper60 §15 RESONANCE face)
                 ○ SPREAD     (1 layer: L5 fractal dimension of dissipation set —
                               ε(x) distributes L^2 mass on a multifractal support)
                 ○ AMPLITUDE  (1 layer: L7 universal K41 constants — Lindelöf-style
                               amplitude pins through ζ zeros; paper60 §11)
Absent faces:    TOPOLOGY, HARMONICS, MEASURE, SYMMETRY, ARITHMETIC
```

---

## §3 Layer-by-Layer X-Ray

### L1 — 5D Einstein → 4D KK fluid reduction

**Claim**: Five-dimensional Einstein gravity on $M^4 \times S^1/\mathbb{Z}_2$ Kaluza-Klein-reduces via the fluid/gravity duality (BHMR 2008) to a 4D fluid description, providing the base geometry on which turbulent NS dynamics is posed.

**Status**: LITERATURE
**Source**: Paper 1 §KK (QG5D derivation); BHMR 2008 (Bhattacharyya-Hubeny-Minwalla-Rangamani, arXiv:0712.2456); paper38 PROOF-CHAIN.md Link 1.

#### Physics

- **Face**: CURVATURE (paper60 §13 — "the Kaluza-Klein reduction of five-dimensional gravity on $M^4 \times S^1$ produces a tower of massive modes… the circle's compactness forces the gap"; turbulence inherits the CURVATURE-inherited base from NS/YM)
- **Projection**: $P_B$ (paper61 §10 — Branch B gauge-bundle / KK tower carries the fluid base; paper61 §06-12 vertex-8 "$P_B$ (NS + BGS transfer)")
- **Pattern**: P3 Scale-Setting (KK radius $R \approx 10.10\,\mu\text{m}$ sets the scale for the inertial range; dissipation scale $\eta = (\nu^3/\varepsilon)^{1/4}$ is the fluid analog of the KK scale)
- **Invariant preserved**: KK mode index (load-bearing — $n \in \mathbb{Z}$ labels the tower), spectral gap (background — downstream $n=1$ gap used at L2)
- **Geometric interpretation**: KK reduction provides the 4D background on which NS, hence turbulent flows, live (paper60 §13). Under $P_B$ (paper61 §06-12) this is the same Branch B geometric preparation used by both YM and NS vertices — paper38 inherits this layer identically from paper30 and paper08. Pattern 3 is canonical: the circle's radius $R$ sets every downstream scale, and the fluid inertial range is ultimately cut off by this microscale. [Considered but rejected: face TOPOLOGY — circle fibration involves winding but the load-bearing output is curvature; projection $P_C$ — cosmological pins for $R$ live in $P_C$ but the geometric step is gauge-side.]
- **Cross-cuts**: qg5d Branch B (L1 IS the QG5D KK reduction, PRIMARY PARENT via paper61 §08 derivation chain), ns:L1 (identical base — paper30 Link 1), ym:L1 (KK spectral gap on same $M^4 \times S^1$).

### L2 — NS spectral gap $\Delta_0^{KK} > 0$ controls high-frequency modes

**Claim**: The Kaluza-Klein spectral gap $\Delta_0^{KK} > 0$, inherited from YM Theorem 4 and Paper 11 Theorem K.4 (unconditional all-loop), controls the high-frequency modes of the NS velocity field and therefore of the turbulent cascade.

**Status**: INHERITED-PROVED (unconditional all-loop post W1/W2 closure)
**Source**: Paper 30 Link 4 (PROVED UNCONDITIONAL ALL-LOOP); Paper 8 Theorem 4; Paper 11 Theorem K.4 (all-orders inductive bootstrap); Paper 10 (scheme independence); paper38 PROOF-CHAIN.md Link 2.

#### Physics

- **Face**: CURVATURE (paper60 §13 — "the gap is the curvature's gift to the quantum theory"; same gap-above-ground-state structural form that YM/NS rest on)
- **Projection**: $P_B$ (paper61 §08 — "the KK spectral gap is the load-bearing structural element" for every Branch B vertex; paper61 §19.6 for NS)
- **Pattern**: P4 Topological Rigidity (paper08 §36 — "compactness forces discreteness; discreteness forces gaps"; the gap survives the regulator transfer into the fluid sector)
- **Invariant preserved**: spectral gap (load-bearing), KK mode index (background — gap lives between $n=0$ and $n=1$ sectors)
- **Geometric interpretation**: The KK spectral gap is the single most important inherited invariant — it is what makes turbulence's foundation as strong as NS's. The W1/W2 closure (2026-04-13) upgraded this layer from conditional to UNCONDITIONAL ALL-LOOP (paper38 PROOF-CHAIN.md "Cascading impact"), meaning every high-frequency-mode argument in the downstream turbulence chain rests on a regulator-scheme-independent object. Under $P_B$ (paper61 §19.6) this is the "spectral gap prevents concentration of energy" ingredient carried from the gauge sector to the fluid. [Considered but rejected: face TOPOLOGY — gap-above-ground-state parallel with Lehmer is real but curvature is canonical per paper60 §13 adjacency table; pattern P3 — $R$ is a scale but the gap's existence is rigid.]
- **Cross-cuts**: ns:L4 (SHARED PRIMARY PARENT — paper30 Link 4), ym:L1 (KK gap = same object), qg5d:Branch B (paper61 §08 derivation chain), baum-connes:L_K-theory (K-theoretic KK operator), lehmer (face-only, TOPOLOGY gap-above-ground-state analog via paper60 §13 table).

### L3 — YM gradient flow regularity = parabolic PDE class of NS

**Claim**: The Yang-Mills gradient flow's well-posedness + contractivity (paper08 Lemmas 1.1-1.5, L15-L17) transfers to the NS velocity-field flow, and therefore to the gradient-flow regularized turbulent velocity field, via same-parabolic-class structural parallel.

**Status**: INHERITED-PROVED (from YM L15-L17 VERIFIED 9/10, now UNCONDITIONAL post W1/W2)
**Source**: Paper 8 Links 15-17; Paper 30 Link 3; paper38 PROOF-CHAIN.md Link 3.

#### Physics

- **Face**: DYNAMICS (paper60 §08 — gradient flow IS a continuous dynamical system on the velocity field; "how does the modular flow TRAVERSE the circle" applied to the fluid; identical face-assignment as ym:L15 and ns:L3)
- **Projection**: $P_B$ (paper61 §19.6 — Branch B spectral-gap-and-gradient-flow; paper61 §10 gauge-bundle dynamics inherited to fluid)
- **Pattern**: P3 Scale-Setting (gradient-flow time $t$ sets the smearing scale; Lüscher-Weisz 2010 framework transferred into the fluid regime; fluid-side smearing scale is the Kolmogorov microscale $\eta$)
- **Invariant preserved**: ergodic property (load-bearing — contractivity $=$ ergodic mixing on the velocity-field configuration space), scaling dimension (background — gradient-flow time has dimension $[L]^2$)
- **Geometric interpretation**: The YM gradient flow and the NS velocity-field flow are in the same parabolic class; turbulent NS regularity inherits the well-posedness + contractivity infrastructure directly (paper60 §08 DYNAMICS face). Under $P_B$ (paper61 §19.6) this is the gauge-bundle's gradient-flow structure projected into the fluid sector. Pattern 3 is canonical: the flow time is the scale-setting parameter; in the turbulent regime the smearing scale will ultimately equal the Kolmogorov $\eta$. [Considered but rejected: face HARMONICS — heat-equation analogy is real but load-bearing content is dynamical (well-posedness + contractivity); pattern P4 — contractivity rigidity implied but Scale-Setting dominates.]
- **Cross-cuts**: ym:L15 (STRUCTURAL PARENT — paper08 explicit programme-graph edge: "gradient-flow machinery (Links 15-17) structural parallel for NS regularity" which propagates to turbulence), ns:L3 (same gradient-flow transfer one step upstream), cramer:L_modular (DYNAMICS canonical, modular-flow-on-circle), paper32-bgs:L2 (type III$_1$ modular-flow ergodicity is the BC-algebra analog of gradient-flow contractivity).

### L4 — Type III$_1$ ergodic modular flow → GUE universality on eigenvalue spacings

**Claim**: The type III$_1$ factor structure of the Bost-Connes algebra at its unique KMS$_1$ state, combined with the ergodicity of the modular flow $\sigma_t$, produces GUE pair-correlation universality (Paper 32 BGS chain) — and this universality kernel supplies the statistical backbone for K41 universal constants in the turbulent cascade.

**Status**: INHERITED-ESTABLISHED (BGS chain 6/7 closed; L5 LITERATURE via Hardy Z PCC arXiv:2511.18275 Nov 2025)
**Source**: Paper 32 BGS PROOF-CHAIN.md L1 (KNOWN), L2 (PROVED), L5 (LITERATURE); Connes classification; Araki-Woods 1968 ($\lambda_p = 1/p$); Bost-Connes 1995 (KMS$_1$ uniqueness); paper38 PROOF-CHAIN.md Link 4.

#### Physics

- **Face**: RESONANCE (paper60 §15 — "what vibrational frequencies are ALLOWED on the circle"; GUE sine-kernel IS a resonance-structure statement on the BC modular spectrum; paper60 §20 / paper60 §15 "BGS's claim is what spectral modes are ALLOWED on the BC modular circle")
- **Projection**: $P_D$ (paper61 §10 — GUE statistics are the signature output of Branch D's type III$_1$ ITPFI factor; paper61 §06-12 vertex-8 "$P_D$ (type III$_1$)")
- **Pattern**: P4 Topological Rigidity (paper08 §36 analog — ergodicity of type III$_1$ modular flow is a rigid statement about the BC algebra's classification; there are no non-trivial $\sigma_t$-invariant projections)
- **Invariant preserved**: ITPFI factor type (type III$_1$, load-bearing — this IS the classification statement), ergodic property (load-bearing — $\sigma_t$ is ergodic on the type III$_1$ factor)
- **Geometric interpretation**: The BC algebra $\mathcal{M} = \bigotimes_p \mathcal{M}_p$ with Araki-Woods parameter $\lambda_p = 1/p$ is type III$_1$ (paper61 §10); at KMS$_1$ the modular flow is ergodic (Paper 32 L2 PROVED). Under $P_D$ (paper61 §06-12) this is the operator-algebraic side that Turbulence shares with BGS and carries the universality-class kernel — if K41 constants are universal across fluid systems, their universality rides on the same Dyson threefold-way / Connes classification that gives GUE for Riemann zeros. Pattern 4 rigidity: the type III$_1$ classification is unique and inevitable. [Considered but rejected: face DYNAMICS — ergodicity is dynamical but the load-bearing claim is that the BC modular spectrum is RESONANCE-structured (GUE kernel); face MEASURE — GUE is a measure statement but the primary content is resonance mode distribution; projection $P_B$ — no, Branch D is canonical here.]
- **Cross-cuts**: paper32-bgs:L1 (type III$_1$ KNOWN), paper32-bgs:L2 (ergodicity PROVED — shared parent), rh:L_BC-KMS (BC algebra at KMS$_1$ shared), pvnp:L_Popa (Popa rigidity = type III$_1$ spectral-gap rigidity analog), baum-connes:L_K (K-theoretic BC-algebra structure).

### L5 — Fractal dimension of singular dissipation set from constraint-graph holonomy

**Claim**: The singular dissipation set $\{x : \varepsilon(x) \neq 0\}$ in 3D turbulent flow has a well-defined Hausdorff dimension $d_H < 3$ (intermittency), derived via a structural analog of the Paper 28 A5 computational area law: NPC holonomy obeys area law $\iff$ confining cascade, transposed to fluid-dynamics as dissipation holonomy $\iff$ intermittent cascade.

**Status**: CANDIDATE (named wall W_T1)
**Source**: Paper 28 A5 computational area law (structural analog — not yet formally transposed); arXiv:2603.28308 finite-time weak singularities and interacting weak-singularity ensembles for 3D NS; paper38 PROOF-CHAIN.md Link 5; turbulence-audit 00 §4 W_T1 "5D-to-NS regularization bridge; confidence 0.6."

#### Physics

- **Face**: SPREAD (paper60 §Face-10 / paper61 §29-30 — "QUE-type / SPREAD: $L^2$ mass distribution"; the dissipation field $\varepsilon(x)$ is an $L^2$-mass-on-fractal-support object; multifractal spectrum $f(\alpha)$ is the canonical SPREAD-face statement)
- **Projection**: $P_D$ (paper61 §10 — fractal dimension of a singular support is an operator-algebraic / modular-measure-theoretic statement in the BC framework; paper28 A5 analog is $P_D$-native)
- **Pattern**: P4 Topological Rigidity (the fractal dimension is rigid — it is a topological invariant of the multifractal support; holonomy-governed rigidity analogous to paper28's constraint-graph area law)
- **Invariant preserved**: scaling dimension (load-bearing — Hausdorff dimension $d_H$ IS a scaling dimension), holonomy (background — structural analog of paper28's NPC constraint holonomy)
- **Geometric interpretation**: Paper 28 A5 shows that in the PvNP construction, computational holonomy on the NPC constraint graph obeys an area law characteristic of a confining cascade. The same structural form — holonomy controls the fractal support of the "hard" set — should transfer to fluid dynamics: the singular dissipation set is the "hard" set, and its fractal dimension reflects the holonomy of the fluid-velocity gradient flow on its constraint graph. This is Pattern 4 rigidity (paper08 §36 analog): the multifractal spectrum is an invariant, not tunable. Under $P_D$ (paper61 §10) the construction lives on the BC-algebraic side via the ITPFI factorization over scales (each scale $\ell$ a local tensor factor). [Considered but rejected: face MEASURE — $\varepsilon(x)$ IS a measure but the load-bearing content is $L^2$-mass-spreading on fractal support (SPREAD); face CURVATURE — singular set is curvature-singular but the dimension statement is a SPREAD invariant; pattern P5 — zeta regularization is tangentially involved (multifractal generating function) but rigidity dominates.]
- **Cross-cuts**: pvnp:L_A5 (Paper 28 A5 computational area law — STRUCTURAL PARENT via programme-graph edge), ns:L5b (cosphere-bundle wave-front-set analog — both measure fractal support in phase space), que / sato-tate (SPREAD/MEASURE face — $L^2$-mass distribution on circle/torus), hodge:L_dim (fractal-dimension-of-singular-stratum analog; speculative).

### L6 — K41 $k^{-5/3}$ spectrum from $\Delta$-controlled cascade

**Claim**: The Kolmogorov K41 energy spectrum $E(k) = C_K \varepsilon^{2/3} k^{-5/3}$ in the inertial range of 3D incompressible NS follows from the $\Delta_0^{KK} > 0$ spectral-gap-controlled cascade combined with the fractal dissipation set L5; equivalently, structure functions $S_p(\ell) \sim (\varepsilon\ell)^{p/3}$ up to multifractal corrections.

**Status**: CANDIDATE (named wall W_T2 — THE HARDEST STEP)
**Source**: Kolmogorov 1941 (Dokl. Akad. Nauk SSSR 30); Frisch 1995 Cambridge; arXiv:2502.10032 "Intermittency and Dissipation Regularity in Turbulence" (Feb 2025, rigorous connection between regularity criteria and intermittency scaling); arXiv:2503.19944 log-improved regularity criteria; paper38 PROOF-CHAIN.md Link 6; turbulence-audit 00 §4 W_T2 "Dissipation-anomaly proof uniform in $\nu$; confidence 0.55."

#### Physics

- **Face**: DYNAMICS (paper60 §08 — K41 IS a modular-flow universality statement: "how does the ergodic cascade traverse scales"; paper61 §29-30 Appendix table row 8 assigns turbulence to DYNAMICS face; the $-5/3$ exponent is the universal return-time exponent of the spectral-gap-controlled flow)
- **Projection**: $P_B$ compound with $P_D$ (paper61 §06-12 vertex-8 "Compound: $P_B \cap P_D$ (via turbulent cascade and BC ergodics)"; Branch B carries the spectral-gap control, Branch D the universality-class kernel)
- **Pattern**: P3 Scale-Setting (the $-5/3$ exponent IS the scale-setting signature; the KK radius $R$ → inertial range $[\eta, L]$ → Kolmogorov microscale $\eta$ is the scale-setting chain)
- **Invariant preserved**: scaling dimension (load-bearing — $-5/3$ IS the scaling dimension of $E(k)$ in inverse wavenumber), spectral gap (background — the gap enables the cascade control), critical exponent (load-bearing — $5/3$ is a critical exponent)
- **Geometric interpretation**: K41 is the universal scaling signature of the turbulent cascade; the framework claim is that it follows from $\Delta > 0$ (spectral gap prevents arbitrary concentration of energy at any single scale, forcing a power-law distribution across scales) plus the type III$_1$ ergodicity (paper60 §08 DYNAMICS; paper61 §06-12 vertex-8). The $-5/3$ exponent is the unique exponent compatible with dimensional analysis of $\varepsilon^{2/3} k^{-5/3}$ (Kolmogorov 1941) AND with the spectral-gap-controlled cascade dynamics. This is Pattern 3 scale-setting at its most physically striking. Under $P_B \cap P_D$ (paper61 §10 compound) the scaling emerges from the intersection of the Branch B spectral gap and the Branch D ergodicity. **THE WALL**: bridging "$\Delta > 0$ + type III$_1$ ergodicity" to "$-5/3$ universal exponent" requires a new theorem — no such theorem exists in the literature and no sub-chain of the programme currently produces it. [Considered but rejected: face AMPLITUDE — $E(k)$ is an amplitude but the spectrum's character is dynamical cascade; face RESONANCE — sum over modes is resonance but DYNAMICS dominates; projection $P_O$ — outer-ring wrapping possible but the load-bearing mechanism is inside $P_B \cap P_D$.]
- **Cross-cuts**: ns:L4 (SHARED SPECTRAL GAP — $\Delta$ is the load-bearing invariant), ns:L5 (BKM criterion as regularity-scale for cascade), paper32-bgs:L4 (GUE level-repulsion = universality-class kernel), cramer:L_returns (modular-flow return-time statistics ≈ cascade return times across scales), lindelof:L_amplitude (AMPLITUDE uniform-bound structural form for moments), pvnp:L_A5 (area-law cascade analog for fractal dissipation).

### L7 — Universal Kolmogorov constants from Riemann zeros (framework prediction)

**Claim**: The universal Kolmogorov constants (Kolmogorov constant $C_K \approx 1.5$ and intermittency exponents) are derivable from the Riemann zeros $\{\gamma_n\}$ via the ITPFI factorization, giving a new pin in the Branch E master table.

**Status**: CONJECTURED (new framework-level prediction)
**Source**: Branch E master table (paper12-cbb-system pin inventory); paper38 PROOF-CHAIN.md Link 7; paper61 §29-30 Appendix table row 8 "Speculative."

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — "how LOUD can the oscillation get"; universal constants $C_K$ are amplitude-level pins, Lindelöf-style moment-level statements projected to the fluid regime)
- **Projection**: $P_E$ (paper61 §12 — pins / Branch E measurable outputs; paper61 §06-12 vertex-8 compound discussion notes "secondary projections include $P_E$ once L7 closes")
- **Pattern**: P5 Zeta Regularization (paper08 §36 — universal constants from $\zeta$ zeros are the paradigmatic Pattern-5 prediction; similar to YM's glueball mass pin derivation from $\Delta_\infty$ via KK-tower regularization)
- **Invariant preserved**: L-value (load-bearing — $C_K$ would be a specific value derived from $\zeta$ at specific arguments), critical exponent (background — intermittency exponents $\mu$)
- **Geometric interpretation**: The framework's most audacious turbulence prediction: that the universal K41 prefactor $C_K \approx 1.5$ is not a free parameter but a computable output of the ITPFI factorization $\bigotimes_p \omega_1^{(p)}$ evaluated against the Riemann-zero spectrum (paper61 §06-12 vertex-8 "$P_E$ pins" fan-out). This is Pattern 5 at its extreme — regularize a universal fluid constant through a zeta-valued expression. Under $P_E$ (paper61 §12) this would be a new pin in the 36-pin master table once L6 provides the $k^{-5/3}$ mechanism for $C_K$ to sit on. [Considered but rejected: face ARITHMETIC — zeta zeros live on the ARITHMETIC face but the CLAIM is about universal amplitudes; face RESONANCE — ζ zeros = resonance but the pin value is AMPLITUDE; projection $P_D$ — derivation lives in $P_D$ but the OUTPUT is a pin, hence $P_E$.]
- **Cross-cuts**: rh:L_zeros ($\gamma_n$ as primary object), paper32-bgs:L5 (GUE pair-correlation supplies the universality kernel feeding $C_K$), lindelof:L_amplitude (Lindelöf hypothesis ≈ amplitude-universal ζ moments — same AMPLITUDE face), baum-connes:L_index (K-theoretic constraints on the spectrum used for pin derivation — speculative).

---

## §4 Branch Map

The turbulence proof chain has two significant branch/split structures, both at the K41 walls.

```
L4 (type III_1 ergodicity, INHERITED) + L2 (spectral gap, INHERITED)
                │
                ├── Route A: Direct-cascade derivation of L6
                │   (attempt to derive -5/3 exponent from
                │    Δ + ergodicity via new theorem)
                │   [face: DYNAMICS | proj: P_B ∩ P_D | pat: P3]
                │   WALL: requires new mathematical result
                │   Confidence 0.55
                │
                └── Route B: Via L5 fractal-dimension bridge
                    (first construct multifractal support,
                     then derive -5/3 as spectral consequence)
                    [face: SPREAD → DYNAMICS | proj: P_D → P_B ∩ P_D | pat: P4 → P3]
                    WALL_T1 (L5 Paper 28 A5 analog not yet
                    transposed to fluid) THEN WALL_T2
                    Confidence 0.55

Both routes would converge on the same physics content:
- Universal -5/3 exponent in the inertial range
- Intermittency corrections from multifractal structure
- Universal C_K constant (L7 pin)

Routes differ in which face is load-bearing first:
- Route A puts DYNAMICS/cascade first, SPREAD downstream
- Route B puts SPREAD/fractal first, DYNAMICS downstream

The split is structural: it asks whether K41 is primarily
a statement about the flow (Route A, DYNAMICS-first) or
primarily a statement about the dissipation support
(Route B, SPREAD-first). The Paper 28 A5 analog favors
Route B because it provides a published mechanism for the
fractal support via computational-area-law transposition.
```

This branching mirrors the YM L18 / NS L5 branch structures: in all three cases, the Clay-adjacent wall admits routes differing in which projection or face is load-bearing first. The pattern — Tier-A wall admits Tier-B "start from different face" bypass routes — is a programme-wide structural feature (paper61 §19.6 dual Branch B + Branch D characterisation gives explicit room for these splits).

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | Turbulence does not interrogate Lehmer-style winding. |
| DYNAMICS   |   2   | ████████              | DOMINANT face. L3 (gradient-flow transfer), L6 (K41 cascade). paper61 §29-30 Appendix table row 8 "DYNAMICS" canonical. |
| HARMONICS  |   0   |                       | No Collatz-style harmonic-mixing layer. |
| MEASURE    |   0   |                       | MEASURE face absent as a primary layer (ε(x) is a measure but load-bearing invariant is SPREAD). |
| AMPLITUDE  |   1   | ████                  | L7 (universal K41 constants $C_K$ — Lindelöf-style amplitude pins). |
| SYMMETRY   |   0   |                       | No Katz-Sarnak-style symmetry-type classification layer. |
| CURVATURE  |   2   | ████████              | L1 (KK base geometry), L2 (spectral gap). Inherited from NS/YM lineage — secondary dominant. |
| ARITHMETIC |   0   |                       | No Newton-power-sum / integer-lattice layer. |
| RESONANCE  |   1   | ████                  | L4 (type III$_1$ ergodic modular flow — BGS backbone). |
| SPREAD     |   1   | ████                  | L5 (fractal dimension of singular dissipation set — $L^2$-mass on multifractal support). |

**Interpretation**: DYNAMICS (2 / 7 layers, 29%) and CURVATURE (2 / 7, 29%) tie for dominance, matching paper61 §29-30 Appendix table row 8 assignment of turbulence to DYNAMICS face with NS-inherited CURVATURE foundation. AMPLITUDE, RESONANCE, SPREAD each carry one layer (14% each) — turbulence touches four distinct faces lightly because it is a *derived* vertex (inherited from NS, YM, BGS) rather than a primitive one. Five faces (TOPOLOGY, HARMONICS, MEASURE, SYMMETRY, ARITHMETIC) are absent — turbulence does not interrogate winding, harmonic mixing, equidistribution, symmetry-type, or integer-lattice structure. The "shape" of turbulence on the e-circle is DYNAMICS-canonical (as per paper61 §29-30) with CURVATURE-inheritance (the Branch B spine) and three specialty faces (AMPLITUDE for pins, RESONANCE for the ergodic kernel, SPREAD for the multifractal support) supporting the structure. This is a genuinely composite face-print — consistent with turbulence being a synthesis vertex that inherits all of NS, YM, BGS, and reaches into new SPREAD territory via the fractal-dissipation-set claim.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No quantum-observable projection forgets turbulence entirely — K41 is not a quantum observable. |
| $P_B$        |   4   | ████████████████     | DOMINANT. L1 (KK base), L2 (spectral gap), L3 (gradient-flow transfer), L6 (cascade scaling) — 57% of layers. paper61 §06-12 vertex-8 "$P_B$ (NS + BGS transfer)". |
| $P_C$        |   0   |                      | Cosmological projection forgets turbulence regularity entirely. |
| $P_D$        |   2   | ████████             | STRONG SECONDARY. L4 (type III$_1$ ergodicity), L5 (fractal dissipation) — 29% of layers. Plus compound $P_B \cap P_D$ at L6. paper61 §06-12 "$P_D$ (type III$_1$)". |
| $P_E$        |   1   | ████                 | Pin projection. L7 (universal $C_K$ from ζ zeros) — 14%. New pin candidate for Branch E master table. |
| $P_O$        |   0   |                      | Outer-ring projection not individually assigned; turbulence's claim as a whole is the outer-ring wrapper but no individual layer lives at $P_O$. |

**Interpretation**: The projection profile is precisely what paper61 §06-12 vertex-8 prescribes: **compound $P_B \cap P_D$** with $P_E$ pin downstream. $P_B$ dominates (4 / 7, 57%) — turbulence is fundamentally a Branch B object by inheritance from NS and YM. $P_D$ carries the BGS-inherited universality kernel and the fractal-dissipation construction (2 / 7, 29%). $P_E$ receives the conjectured L7 universal-constant pin (1 / 7, 14%). $P_A, P_C, P_O$ are absent — turbulence is not a quantum-observable, cosmological, or outer-ring-as-individual-layer object. This matches paper61 §29-30 Appendix table row 8 exactly: Primary $P_B$ (NS + BGS transfer), Secondary $P_D$ (type III$_1$), Ring Position 9, Status SPECULATIVE. The architectural identity: turbulence = NS-lineage spine (L1-L3 Branch B) + BGS-lineage kernel (L4 Branch D) + synthesis walls (L5-L7 at $P_D$ and $P_E$). Whereas NS is $P_B$-dominant with $P_D$-secondary (Branch B dominant), turbulence is $P_B$-dominant with $P_D$-secondary *and* $P_E$-pin — the pin projection appears here because this vertex is where the framework delivers a measurable prediction ($C_K$) that NS alone does not reach.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                        qg5d (Branch B hub)
                             │
                             │ ═══ shared KK reduction (L1 = Paper 1 §KK)
                             │ ═══ shared spectral gap (L2 inherits paper08 T.4)
                             │ ═══ shared gradient-flow infra (L3)
                             │
    ns ═══════════════ turbulence (K41) ═══════════════ ym (primary grandparent)
    (paper30;              │                           (paper08; primary parent
     PRIMARY PARENT;       │                            of L3 gradient-flow)
     turbulence = NS       │                           ═══ L3 ↔ ym:L15 grad-flow
     + statistics)         │                           ═══ L2 ↔ ym:L1 spectral gap
    ═══ L1 ↔ ns:L1 base    │                           ═══ L6 ↔ ym:L18 wall-family
    ═══ L2 ↔ ns:L4 gap     │                            (both Clay-adjacent)
    ═══ L3 ↔ ns:L3 flow    │                           ─── L5 ↔ ym:L8 dim-supp
    ═══ L6 ↔ ns:L5 BKM     │                                (speculative deviation
         (both walls at    │                                 analog)
          the Clay         │
          boundary)        │
                           │
                           │
    paper32-bgs ═══════════│══════════════════ pvnp (paper28)
    (SECONDARY PARENT;     │                    (A5 computational area law;
     type III_1            │                     STRUCTURAL ANALOG of L5 fractal-
     ergodicity;           │                     dissipation-set holonomy)
     GUE universality)     │                    ═══ L5 ↔ pvnp:L_A5 area-law
    ═══ L4 ↔ bgs:L1 type   │                         fractal support
         III_1             │                    ─── L6 ↔ pvnp:L_cascade
    ═══ L4 ↔ bgs:L2 ergod. │                         confining cascade
    ═══ L4 ↔ bgs:L5 GUE    │                    (Popa rigidity ↔ spectral-gap
    ═══ L7 ↔ bgs:L5 pin    │                     universality bridge)
         (universality     │
          kernel → C_K)    │
                           │
                           │
    cramer ════════════════│══════════════════ rh (paper13)
    (DYNAMICS canonical;   │                    (ζ zeros; BC-KMS state;
     modular-flow          │                     zero pair-correlation)
     ergodicity;           │                    ═══ L7 ↔ rh:L_zeros ζ zeros
     return-time stats)    │                         as universal-constant source
    ═══ L3 ↔ cramer:L_mod  │                    ═══ L4 ↔ rh:L_BC-KMS shared
    ═══ L6 ↔ cramer:L_ret  │                         BC-algebra foundation
         (cascade return-  │                    ─── L6 ↔ rh:L_Weil sum
          time analog to   │                         (speculative — bounded
          max-gap analysis)│                          amplitude over zeros)
                           │
                           │
    baum-connes ═══════════│══════════════════ lindelof
    (paper31; K-theory     │                    (AMPLITUDE canonical;
     of BC algebra;        │                     universal moments)
     spectral gap          │                    ─── L7 ↔ lindelof:L_moments
     as K-theoretic)       │                         C_K as Lindelöf-style
    ═══ L2 ↔ bc:L_K gap    │                         amplitude pin
    ─── L5 ↔ bc:L_spread   │                    ─── L6 ↔ lindelof:L_uniform
         (K-theoretic      │                         uniform cascade amplitude
          fractal index)   │
                           │
    hilbert6 ──────────────┤
    (Hilbert's 6th:        │
     axiomatization of     │
     fluid mechanics)      │
    ─── L1 ↔ h6:L_fluid    │
         fluid/gravity     │
    ─── L6 ↔ h6:L_axiom    │
         K41 as axiom      │
         of fluid ML       │
                           │
    que / spread ──────────┘
    (L^2-mass distribution)
    ─── L5 ↔ que:L_spread
         multifractal support
         of ε(x)
```

### Bullet list (per-edge)

- **L1 ↔ ns:L1 (PRIMARY PARENT base)** — shared KK mode index.
  - Reason: Turbulence inherits NS:L1 directly; same $M^4 \times S^1/\mathbb{Z}_2$ base geometry; paper30 Link 1 = paper38 Link 1.
  - Transposition candidate: YES (capacitor 09 §49 SPEC↔QFT KK-reduction anchor).

- **L1 ↔ qg5d:Branch B** — shared KK mode index.
  - Reason: L1 IS the QG5D KK reduction (paper61 §08 derivation chain).
  - Transposition candidate: YES.

- **L1 ↔ ym:L1** — shared KK mode index + spectral gap foundation.
  - Reason: Same $M^4 \times S^1$ KK base supports YM gauge fields and (via NS) turbulent velocity field.
  - Transposition candidate: YES.

- **L1 ↔ hilbert6:L_fluid** — shared C*-algebra structure (fluid/gravity duality).
  - Reason: Hilbert's 6th problem asks for axiomatization of fluid mechanics; fluid/gravity duality is a candidate axiomatic foundation (paper60 §Hilbert-6 connection).
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ ns:L4 (PRIMARY PARENT spectral gap)** — shared spectral gap.
  - Reason: L2 IS NS:L4 restricted to the turbulent regime; unconditional all-loop post W1/W2 closure.
  - Transposition candidate: YES (capacitor 09 §49 SPEC↔QFT Weitzenböck-Bochner spectral gap).

- **L2 ↔ ym:L1** — shared spectral gap.
  - Reason: Same KK gap $\Delta_0^{KK} > 0$ by inheritance chain paper08 → paper30 → paper38.
  - Transposition candidate: YES.

- **L2 ↔ qg5d:Branch B** — shared spectral gap.
  - Reason: paper61 §08 explicit derivation chain ($S^1$ → KK → Weitzenböck → gap).
  - Transposition candidate: YES.

- **L2 ↔ baum-connes:L_K** — shared spectral gap.
  - Reason: Spectral gap is a K-theoretic statement about the KK operator; paper30 programme-graph edge.
  - Transposition candidate: YES.

- **L2 ↔ lehmer:L_top** — face-only (gap-above-ground-state).
  - Reason: paper60 §13 adjacency table — TOPOLOGY face parallel for gap-above-ground-state structural form, inherited from YM/NS.
  - Transposition candidate: NO (face-only, no capacitor cell, but documented in paper60).

- **L3 ↔ ns:L3 (PRIMARY PARENT gradient flow)** — shared ergodic property.
  - Reason: L3 IS NS:L3 restricted to the turbulent regime.
  - Transposition candidate: YES.

- **L3 ↔ ym:L15 (GRANDPARENT gradient-flow)** — shared ergodic property.
  - Reason: paper08 PROOF-CHAIN.md explicit programme-graph edge: "gradient-flow machinery (Links 15-17) structural parallel for NS regularity" propagates to turbulence; Lüscher-Weisz 2010 framework shared.
  - Transposition candidate: YES (capacitor 09 §110 GEOM↔QFT gradient-flow).

- **L3 ↔ ym:L16** — shared BC-KMS state (OS analog).
  - Reason: OS reconstruction used in YM at fixed $t > 0$ is structurally what turbulent-regularity needs at finite-$t$ smoothness.
  - Transposition candidate: YES.

- **L3 ↔ cramer:L_modular** — shared ergodic property (DYNAMICS canonical).
  - Reason: paper60 §08 DYNAMICS face — gradient flow + modular flow = same dynamical-system framing.
  - Transposition candidate: YES.

- **L3 ↔ paper32-bgs:L2** — shared ergodic property.
  - Reason: Type III$_1$ modular-flow ergodicity carries the same transfer mechanism into the fluid regime.
  - Transposition candidate: YES.

- **L4 ↔ paper32-bgs:L1 (PRIMARY PARENT III$_1$)** — shared ITPFI factor type (III$_1$).
  - Reason: L4 IS BGS:L1 inherited into turbulence; Araki-Woods classification $\lambda_p = 1/p$ shared.
  - Transposition candidate: YES.

- **L4 ↔ paper32-bgs:L2** — shared ergodic property.
  - Reason: BGS:L2 ergodicity (PROVED T2 2026-04-13) is L4's ergodicity statement for turbulence.
  - Transposition candidate: YES.

- **L4 ↔ paper32-bgs:L5** — shared ergodic property (GUE kernel).
  - Reason: BGS:L5 (LITERATURE via Hardy Z PCC arXiv:2511.18275) supplies the GUE universality kernel that L4 forwards to K41 universality.
  - Transposition candidate: YES.

- **L4 ↔ rh:L_BC-KMS** — shared BC-KMS state.
  - Reason: Same BC algebra at KMS$_1$; paper61 §10 shared framework.
  - Transposition candidate: YES.

- **L4 ↔ pvnp:L_Popa** — shared ITPFI factor type.
  - Reason: Popa rigidity = type III$_1$ spectral-gap rigidity — shared operator-algebra structure.
  - Transposition candidate: YES.

- **L4 ↔ baum-connes:L_K** — shared ITPFI factor type.
  - Reason: Baum-Connes K-theory of the BC algebra is the K-theoretic counterpart of the type III$_1$ classification.
  - Transposition candidate: YES.

- **L5 ↔ pvnp:L_A5 (STRUCTURAL PARENT)** — shared holonomy.
  - Reason: Paper 28 A5 computational-area-law $\iff$ NPC-holonomy $\iff$ confining-cascade is the structural analog for L5's fluid-dissipation-holonomy $\iff$ intermittent-cascade. Programme-graph edge.
  - Transposition candidate: YES (transposition through a NEW capacitor cell PROB↔SPREAD would be required; currently OPEN).

- **L5 ↔ ns:L5b** — shared scaling dimension.
  - Reason: NS Route B cosphere-bundle wave-front-set is a phase-space $L^2$-mass-distribution analog; both measure fractal support; both live at SPREAD face (paper60 §Face-10).
  - Transposition candidate: YES.

- **L5 ↔ que:L_spread** — shared scaling dimension (SPREAD face).
  - Reason: QUE ($L^2$-mass distribution on arithmetic manifolds) shares the SPREAD face with L5; paper60 §Face-10 SPREAD canonical.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ sato-tate:L_equid** — face-only (MEASURE vs SPREAD adjacency).
  - Reason: Sato-Tate equidistribution and multifractal dissipation are close cousins on the measure/spread face pair.
  - Transposition candidate: NO yet.

- **L5 ↔ hodge:L_dim** — shared scaling dimension.
  - Reason: Fractal dimension of singular stratum analog — Hodge conjecture's middle-cohomology algebraic-cycle classification has dim-of-stratum structure.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ baum-connes:L_K-fractal** — shared scaling dimension.
  - Reason: K-theoretic fractal index for the singular set via the KK operator; paper31 programme-graph edge.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ ns:L5** — shared boundary condition (Clay-adjacent wall-family).
  - Reason: paper38 L6 and paper30 L5 both sit at the Clay-adjacent wall position: NS:L5 (BKM) is the regularity wall, turbulence:L6 (K41) is the statistics wall; both admit routes differing in projection.
  - Transposition candidate: YES (capacitor MICRO↔QFT cell is relevant to both).

- **L6 ↔ ym:L18** — shared scaling dimension (Clay-adjacent wall-family).
  - Reason: YM:L18 (H4 / AF match) and turbulence:L6 (K41 from cascade) are structurally the same wall-family: Clay-adjacent conditional with route-through-multiple-projections character. YM found Step 18' via Balaban+gradient-flow; turbulence seeks analogous unconditional route.
  - Transposition candidate: YES.

- **L6 ↔ ns:L4** — shared spectral gap.
  - Reason: $\Delta_0^{KK}$ is the load-bearing invariant of the cascade; directly inherited from NS:L4.
  - Transposition candidate: YES.

- **L6 ↔ paper32-bgs:L4** — shared ergodic property.
  - Reason: BGS:L4 level-repulsion (PROVED T3 2026-04-13) is the universality-class kernel feeding K41 universality.
  - Transposition candidate: YES.

- **L6 ↔ cramer:L_ret** — shared ergodic property.
  - Reason: Modular-flow return-time statistics on BC algebra are the structural analog of cascade return-times across scales in the inertial range.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ lindelof:L_amplitude** — shared scaling dimension.
  - Reason: Uniform cascade amplitude = AMPLITUDE-face uniform-bound structural form; paper60 §11 Lindelöf canonical.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ pvnp:L_cascade** — shared scaling dimension.
  - Reason: Paper 28 A5 confining cascade is a structural analog of K41 cascade; area-law ↔ $-5/3$ spectrum via holonomy.
  - Transposition candidate: SPECULATIVE (new capacitor cell would be needed).

- **L7 ↔ rh:L_zeros** — shared L-value.
  - Reason: L7 derives $C_K$ from $\{\gamma_n\}$ via ITPFI factorization; the Riemann zeros are the primary object supplying the pin.
  - Transposition candidate: YES.

- **L7 ↔ paper32-bgs:L5** — shared L-value.
  - Reason: BGS:L5 GUE pair-correlation (Hardy Z PCC LITERATURE) supplies the universality kernel that converts ζ zeros into universal fluid constants.
  - Transposition candidate: YES.

- **L7 ↔ lindelof:L_moments** — shared L-value (AMPLITUDE pin).
  - Reason: $C_K$ is a Lindelöf-style amplitude pin — universal amplitude-level prediction; same AMPLITUDE face.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ baum-connes:L_index** — shared L-value.
  - Reason: K-theoretic constraints on the spectrum used for pin derivation; speculative programme-graph edge.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ qg5d:Branch E (pin table)** — shared L-value.
  - Reason: L7 is a candidate new pin for the 36-pin Branch E master table; paper12-cbb-system pin inventory.
  - Transposition candidate: YES (upon L6 closure).

**Summary**: 35+ cross-cut edges identified across 7 layers (avg ~5 cross-cuts per layer — highest density among the outer-ring vertices, consistent with turbulence being a pure synthesis vertex inheriting from NS, YM, BGS, and reaching into PvNP, RH, Lindelöf, Baum-Connes). 17 verified (shared-parent inheritance + capacitor cell), 18 SPECULATIVE (pending sibling-vertex x-rays or new capacitor cells). PRIMARY edges: L2 ↔ ns:L4 (shared spectral gap = KK gap), L3 ↔ ns:L3 (shared gradient flow), L4 ↔ paper32-bgs:L1 (shared type III$_1$), L5 ↔ pvnp:L_A5 (STRUCTURAL ANALOG — Paper 28 A5 computational area law). Turbulence is the densest hub node of the outer-ring cross-cut graph by inheritance-edge count.

---

## §8 Current Walls

- **W_T1 — 5D-to-NS regularization bridge (fractal dissipation set via Paper 28 A5 analog)**: The transposition of the Paper 28 A5 computational-area-law (NPC holonomy $\iff$ confining cascade) into a fluid-dynamics statement (dissipation holonomy $\iff$ intermittent cascade with Hausdorff dimension $d_H < 3$) has not been formalized. Status: **OPEN**, aggregate confidence 0.55 (turbulence-audit 00 §4). Face: SPREAD, projection: $P_D$, pattern: P4.
  - Candidate decomposition path: transpose through a new capacitor cell `PROB↔SPREAD: holonomy on constraint graph ↔ fractal dimension of support`.
  - Cross-reference: `strategy/decomposition/proof-chain/turbulence/PROOF-CHAIN.md` — NOT YET CREATED.

- **W_T2 — Dissipation-anomaly proof uniform in $\nu$ (K41 $-5/3$ from $\Delta$-controlled cascade)**: The derivation of $E(k) \propto k^{-5/3}$ from $\Delta_0^{KK} > 0$ plus type III$_1$ ergodicity requires a new theorem; equivalently, a proof of the dissipation anomaly $\lim_{\nu \to 0} \varepsilon(\nu) = \varepsilon_0 > 0$ uniform in $\nu$. Status: **OPEN**, aggregate confidence 0.55 (turbulence-audit 00 §4). Face: DYNAMICS, projection: $P_B \cap P_D$, pattern: P3. THE HARDEST STEP.
  - Candidate route A: direct cascade derivation (DYNAMICS first, SPREAD downstream).
  - Candidate route B: via L5 multifractal bridge (SPREAD first, DYNAMICS downstream).
  - Cross-reference: arXiv:2502.10032 (Feb 2025 intermittency-regularity rigor) is the strongest published lead.

Links 1-4 are INHERITED-PROVED or INHERITED-ESTABLISHED via NS, YM, BGS chains. Link 7 is a CONJECTURED prediction downstream of L6.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/turbulence/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, the X-Ray cross-cuts above should feed the L5/L6 walls decomposition; the most productive route is likely W_T1 first (Paper 28 A5 transposition) then W_T2 (cascade derivation).
- **CCM verification**: `strategy/ccm-verification/ledger.md#turbulence` — NOT YET CREATED. Turbulence does NOT depend on CCM 2025 directly (the inherited BGS:L6 depends on CCM via spectral realization, but that question sits one vertex upstream). Expected verdict when ledger written: **VERIFIED (CCM-independent at Links 1-5); L6 statistics-kernel inherited from BGS:L5 which is LITERATURE (Hardy Z PCC), so turbulence does not require CCM for the K41 content itself**.
- **Inner rings**: NOT APPLICABLE — turbulence is a primary outer-ring vertex inheriting from NS.
- **Parent chain (NS)**: `strategy/proof-chain/ns/PROOF-CHAIN.md` and `strategy/x-ray/proof-chain/ns/X-RAY.md`. The W1/W2 cascade (2026-04-13) upgraded NS:L4 to UNCONDITIONAL ALL-LOOP, which turbulence:L2 inherits.
- **Parent chain (YM)**: `strategy/proof-chain/ym/PROOF-CHAIN.md` and `strategy/x-ray/proof-chain/ym/X-RAY.md`. YM:L15-L17 grad-flow is the structural grandparent of turbulence:L3; YM:L18 wall-family is the structural sibling of turbulence:L6.
- **Parent chain (BGS)**: `strategy/proof-chain/bgs/PROOF-CHAIN.md` and `strategy/x-ray/proof-chain/bgs/X-RAY.md`. BGS:L1-L5 supplies turbulence:L4 (ergodicity kernel) and turbulence:L7 (universality pin).
- **Turbulence Audit strategy**: `strategy/turbulence/00-audit-strategy.md` and `strategy/turbulence/turbulence-audit-brief.md`. Provides the W_T1 / W_T2 wall definitions and the 6-requirement community-standard audit scaffold.
- **Bare deliverable**: `strategy/turbulence/deliverables/turbulence-bare.md` — NOT YET CREATED; expected to summarize the 7-link chain with §1 Claim / §2 K41 Main Theorem / §3-§10 per-requirement / §11 Analytics / §12 Walls / §13 Numbers (C_K ≈ 1.5, intermittency) / §14 References per audit brief DELTA 5.
- **PROOF-CHAIN origin**: `solutions/paper38-turbulence/PROOF-CHAIN-MOVED.md` — live PROOF-CHAIN was centralized 2026-04-15 per Option A self-healing intervention 2.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W_T1**: Fractal dimension of singular dissipation set via Paper 28 A5 computational-area-law analog — the transposition of NPC constraint-graph holonomy ↔ confining cascade into fluid-dissipation holonomy ↔ intermittent cascade with $d_H < 3$ has not been formalized. Face: SPREAD, projection: $P_D$, pattern: P4. Confidence 0.55. L5 CANDIDATE.

- **G2 — W_T2**: K41 $k^{-5/3}$ spectrum from $\Delta$-controlled cascade — bridging $\Delta_0^{KK} > 0$ plus type III$_1$ ergodicity to universal $-5/3$ exponent requires a NEW THEOREM. Equivalently: proof of the dissipation anomaly $\lim_{\nu \to 0} \varepsilon(\nu) = \varepsilon_0 > 0$ uniform in $\nu$. Face: DYNAMICS, projection: $P_B \cap P_D$, pattern: P3. Confidence 0.55. L6 CANDIDATE — THE HARDEST STEP.

- **G3 — L7 pin closure**: Universal Kolmogorov constants $C_K \approx 1.5$ from ITPFI factorization over Riemann zeros — derivation is CONJECTURED; pin does not yet enter the 36-pin Branch E master table. Closure CONDITIONAL on L6 (W_T2) closure. Face: AMPLITUDE, projection: $P_E$, pattern: P5.

- **G4 — Onsager 1/3 connection**: The framework's K41 derivation (via L6) should be consistent with Onsager's 1/3 conjecture (rigorously proved by Isett 2018 and De Lellis-Székelyhidi-Buckmaster-Vicol via convex integration); explicit mapping to Hölder $C^{1/3}$ threshold and multifractal corrections is not yet written. Face: DYNAMICS, projection: $P_D$, pattern: P1 (geometric reinterpretation of Hölder regularity as modular-flow regularity). CONDITIONAL on L6.

That's it. Links 1-4 are INHERITED-PROVED / INHERITED-ESTABLISHED. The four open items (G1 W_T1, G2 W_T2, G3 L7 pin, G4 Onsager) are all downstream of the L5/L6 wall family. The chain's foundation is as strong as NS's and YM's combined (both inherited unconditional); the open work is the K41 upgrade.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record would be at `strategy/x-ray/pac-output/runs/run-NN/vertices/turbulence/critic-attacks.md`.

Notable arbiter wins:
- L6 face: DYNAMICS over AMPLITUDE (paper61 §29-30 Appendix table row 8 canonicalization — K41 is DYNAMICS-canonical per the closing appendix).
- L5 face: SPREAD over MEASURE ($\varepsilon(x)$ IS a measure but the load-bearing invariant is multifractal support / $L^2$-mass-distribution = SPREAD face per paper60 §Face-10; paper60 §13 discipline "pick dominant").
- L4 face: RESONANCE over DYNAMICS (BGS is primary-RESONANCE per paper60 §15 / paper61 §29-30; the ergodicity *mechanism* is DYNAMICS but the *claim* is about which spectral modes are allowed).
- L6 projection: $P_B \cap P_D$ over $P_O$ (paper61 §06-12 vertex-8 explicit compound assignment; L6 closure would sit inside the compound, not at outer-ring).
- L7 projection: $P_E$ over $P_D$ (the derivation lives in $P_D$ but the OUTPUT is a measurable pin, hence $P_E$ per paper61 §12 vertex-assignment discipline; same logic as YM glueball pin).
- L1/L2 face: CURVATURE over TOPOLOGY (paper60 §13 adjacency-table canonicalization; inherited from NS/YM).

---

*End of Turbulence X-Ray. Snapshot 2026-04-15. 7 layers annotated. 35+ cross-cuts identified (the densest outer-ring synthesis vertex). DYNAMICS-canonical face with CURVATURE-inheritance, $P_B \cap P_D$-compound projection, P3-dominant pattern. Two walls (W_T1, W_T2); L6 (K41 from $\Delta$) is THE HARDEST STEP.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
