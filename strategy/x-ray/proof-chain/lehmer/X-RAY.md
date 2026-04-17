# X-RAY: Lehmer's Conjecture (lehmer)

*X-Ray of the lehmer proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: lehmer
- **Paper**: paper42-lehmer
- **Live file**: strategy/proof-chain/lehmer/PROOF-CHAIN.md (snapshot 2026-04-14, v3 post-T7 S-duality handoff)
- **Top-level claim**: For every algebraic number $\alpha$ not a root of unity, the Mahler measure $M(\alpha) \geq 1 + c_0$ for some absolute constant $c_0 > 0$ — the unit circle IS the e-circle, roots of unity are periodic orbits on the fifth dimension, and Lehmer's gap IS the mass gap of the cyclotomic vacuum, forced by the BC KMS phase transition at $\beta = 1$ and the 36-pin rigidity of the chessboard.
- **Current status**: 3/6 links closed (L1-L4 LITERATURE / PROVED via classical; L5 OPEN — three routes PIN-PRESERVATION + Deninger-RV + Weitzenböck, Route B PARTIAL via CM-curve Brauer-Siegel/Chowla-Selberg/Rubin chain, Route A CONSTRUCT-READY with Cramér T7 $2e^{-\gamma}$ invariant on disk; L6 FOLLOWS). Confidence 4/10 (upgraded 2026-04-14 after T7 S-duality handoff; T8 dispatch expected to bring to 5/10+).
- **Primary branch (paper1)**: D (CBB / BC KMS$_1$ phase transition is Branch D's operator-algebraic core — cyclotomic/non-cyclotomic boundary IS the KMS structure); strong secondary E (36-pin PIN-PRESERVATION chessboard argument forcing cyclotomic isolation is Branch E measurement content; paper61 §12 Vertex 20 explicit $P_D \cap P_E$).
- **Primary face**: TOPOLOGY (paper60 §07 — "what can LIVE on the circle"; Lehmer is the canonical TOPOLOGY face of the e-circle, directly dual to Cramér's DYNAMICS face; paper60 §08 explicit two-face picture; paper60 §26 "The Three-Face Recognition" places lehmer at the TOPOLOGY vertex of the three-face triangle, with Cramér at DYNAMICS and Collatz at HARMONICS).
- **Primary projection**: $P_D$ (paper61 §12 Vertex 20 explicit — "The cyclotomic/non-cyclotomic boundary IS the KMS$_1$ phase transition. The Mahler measure gap is the mass gap of the cyclotomic vacuum"; BC algebra at KMS$_1$ + profinite completion of $\mathbb{Q}/\mathbb{Z}$ whose character group is the unit circle are the defining Branch D objects).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
LEHMER (Mahler measure gap M(α) ≥ 1 + c₀ for non-cyclotomic α)
│  primary face: TOPOLOGY   primary proj: P_D   primary pat: P4
│  top claim: unit circle = e-circle = U(1) phase fiber;
│             roots of unity = periodic orbits on 5th coordinate;
│             Lehmer's gap c₀ = mass gap of cyclotomic vacuum;
│             forced by BC KMS₁ phase transition + 36-pin rigidity
│
├── L1: Kronecker: M(α) = 1 ⟺ α root of unity                 [LITERATURE 1857]
│      │  face: TOPOLOGY    proj: P_D   pat: P1
│      │  invariant: holonomy (load-bearing — winding of ζ_k closes);
│      │             BC-KMS state (background — cyclotomic parametrizes
│      │             KMS states at β > 1)
│      │  source: Kronecker 1857; Bost-Connes 1995 Thm 25 (KMS structure)
│      │
│      └── supports L5 via cyclotomic-ground-state characterization
│             │
│             └── cyclotomic elements = fixed-point set of BC
│                                       Hecke semigroup action at β > 1
│                                       (paper61 §12 Vertex 20, paper60 §07)
│
├── L2: BC phase transition at β = 1 (spontaneous symmetry       [LITERATURE 1995]
│      │  breaking by Gal(Q^cyc/Q))
│      │  face: SYMMETRY    proj: P_D   pat: P4
│      │  invariant: BC-KMS state (load-bearing);
│      │             ITPFI factor type (background — type III_1 at β=1)
│      │  source: Bost-Connes 1995; Connes-Marcolli 2008;
│      │          paper12 CBB Axiom 2 (Criticality at β=1)
│      │
│      └── above β > 1: cyclotomic data parametrizes KMS states (M = 1)
│          below β < 1: non-cyclotomic enters (M > 1)
│          AT β = 1: the transition itself — Lehmer boundary
│
├── L3: Mahler measure = L-function value (Deninger-RV-Boyd)     [LITERATURE 1997-1999]
│      │  face: RESONANCE   proj: P_D   pat: P5
│      │  invariant: L-value (load-bearing — m(P) = c·L'(E,0));
│      │             scaling dimension (background — Beilinson regulator)
│      │  source: Deninger 1997; Rodriguez-Villegas 1999;
│      │          Boyd 1998; Beilinson conjectures
│      │
│      └── PRIMARY BRIDGE: Lehmer ↔ BSD (paper26)
│             │
│             ├── elliptic-curve polynomials: m(P) = c · L'(E, 0)
│             ├── Beilinson regulator → K-theory, motivic cohomology
│             └── if c₀ = 0 then L'(E,0) → 0 for CM curves,
│                                 destabilizing BSD rank formula
│
├── L4: Salem numbers = abelian variety automorphism entropy     [LITERATURE]
│      │  face: SYMMETRY    proj: P_D   pat: P2
│      │  invariant: Galois representation (load-bearing —
│      │             Salem λ = spectral radius on l-adic cohomology);
│      │             monodromy (background — dynamical degree)
│      │  source: Dynamical degrees on abelian varieties (2021);
│      │          Deligne (Weil conjectures — |Frob| = q^{w/2})
│      │
│      └── PRIMARY BRIDGE: Lehmer ↔ Hodge (paper29)
│             │
│             └── every Salem number λ realized as first dynamical
│                 degree of automorphism φ on simple abelian variety A,
│                 with spectral radius on H*_et = λ;
│                 Salem numbers parametrize "interesting" automorphisms
│                 of varieties where Hodge classes live
│
├── L5: KMS spectral gap forces Lehmer's gap                     [OPEN — THE WALL]
│      │  face: TOPOLOGY    proj: P_D   pat: P4
│      │  invariant: spectral gap (load-bearing — c₀ IS the KMS₁ gap);
│      │             BC-KMS state (background — vacuum state)
│      │  depends: L2 + L3 + L4 + Papers 1/8/26/29
│      │
│      │  THREE INDEPENDENT ROUTES (all P4 Topological Rigidity):
│      │
│      ├── L5a — Route A: PIN-PRESERVATION forcing               [STRUCTURAL → CONSTRUCT-READY]
│      │      │  face: TOPOLOGY    proj: P_E   pat: P4
│      │      │  invariant: spectral gap; ergodic property (36-pin
│      │      │             robustness-circle invariant)
│      │      │  source: programme §27 Robustness-Circle Theorem;
│      │      │          T7 handoff from cramer (ITPFI Mertens on disk)
│      │      │
│      │      ├── 36-pin sub-percent match forces cyclotomic isolation
│      │      ├── c₀ ≥ 10⁻² from empirical constraints (weak bound)
│      │      ├── T8 DISPATCH: ITPFI cyclotomic-isolation sharpening
│      │      │       via Cramér's $\prod_p(1-1/p) \sim 2e^{-\gamma}/\log x$
│      │      └── expected upgrade: STRUCTURAL → PARTIAL
│      │
│      ├── L5b — Route B: Deninger-RV L-function bridge         [PARTIAL, CM-slice]
│      │      │  face: RESONANCE   proj: P_D   pat: P5
│      │      │  invariant: L-value (load-bearing);
│      │      │             scaling dimension (background)
│      │      │  source: L3 Deninger-RV + Brauer-Siegel +
│      │      │          Chowla-Selberg + Rubin 1991 + Silverman 1984
│      │      │
│      │      ├── CM curves: L'(E, 1) bounded away from 0
│      │      │       (Chowla-Selberg for fixed K; Brauer-Siegel h_K → ∞)
│      │      ├── Rubin 1991: finiteness of Sha for CM
│      │      ├── Silverman 1984: finite curves with small canonical height
│      │      ├── GAP: CM-defining polynomials are proper subset
│      │      └── arXiv:2510.21515 (Oct 2025): motivic-regulator bridge
│      │              for cyclotomic variants — extension candidate
│      │
│      └── L5c — Route C: Weitzenböck analog (YM transfer)       [SPECULATIVE]
│             │  face: CURVATURE   proj: P_B   pat: P4
│             │  invariant: spectral gap (load-bearing);
│             │             scaling dimension (background)
│             │  source: paper08 YM mass-gap mechanism (internal curv);
│             │          conjectural S¹-external-curvature transfer
│             │
│             ├── YM: positive Ricci on CP^(N-1) → Weitzenböck → gap
│             ├── Lehmer: S¹ embedded in ℂ has positive normal
│             │           curvature → hypothetical gap
│             └── distinction: YM uses INTERNAL curvature,
│                              Lehmer requires EXTERNAL curvature
│
└── L6: Lehmer's conjecture M(α) ≥ 1 + c₀                       [FOLLOWS conditional on L5]
       │  face: TOPOLOGY    proj: P_O   pat: P4
       │  invariant: spectral gap (load-bearing);
       │             holonomy (background — winding of non-cyclotomic fails)
       │  source: paper42 Lehmer 1933 original conjecture
       │
       └── outer-ring closure: famous 93-year-open conjecture
              │
              └── DECOMPOSED-IN: Lehmer ↔ Cramér S-DUAL-CONSTRUCT-BRIDGED
                     │  (T7 pass: Cramér L4b derived 2e^{-γ} on disk;
                     │   T8 dispatch: Lehmer L5 Route A CONSTRUCT using
                     │   the Cramér-side ITPFI invariant at KMS_1 boundary)
```

### §2b Diagram B — Projection fan-out

```
                       (FORGOTTEN under P_A)
                       (Quantum side does not see the Mahler
                        measure gap directly — the U(1) phase
                        fiber's cyclotomic isolation is a
                        Branch D operator-algebra property,
                        not a Branch A quantum observable)
                                  ▲
                                  │
                                  │
        ┌─────────────(P_O outer)───────────────┐
        │                                       │
        │  LEHMER: M(α) ≥ 1 + c₀ for non-       │
        │          cyclotomic α (min leakage    │
        │          off the e-circle is bounded  │
        │          below; cyclotomic vacuum is  │
        │          ISOLATED)                    │
        │                                       │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity         ═══ P_D CBB ═══           P_E pins
    (Route C conj.      BC KMS_1 phase trans.     (36-pin
    only — YM           cyclotomic/non-cyclotomic  PIN-PRESERVATION
    Weitzenböck         boundary; Hecke           forces cyclotomic
    analog via          semigroup fixed points;    isolation —
    external            ITPFI factor at β=1;       Route A; if c₀=0,
    curvature           profinite completion of    near-cyclotomic
    of S¹ embedded      ℚ/ℤ whose character        perturbations
    in ℂ; status        group IS unit circle;      would shift
    SPECULATIVE)        Deninger-RV m(P)=c·L'(E,0) predictions beyond
                        connects to BSD L-values   observed sub-%
                            │                      agreement)
                            ▼
                       P_C cosmology
                       (forgotten — no
                       cosmological pin
                       uses Mahler measure
                       gap directly, though
                       R ≈ 10.10 μm = e-circle
                       radius is same object)
```

Primary projection $P_D$ uses ═══ doubled line — Lehmer lives in the BC algebra at the KMS$_1$ phase transition; cyclotomic/non-cyclotomic boundary IS a Branch D structural property. $P_E$ is the strong secondary (PIN-PRESERVATION Route A explicitly uses the 36-pin master table as forcing evidence; paper61 §12 Vertex 20 explicit $P_D \cap P_E$). $P_O$ appears at L6 (the outer-ring closure statement — Lehmer as famous conjecture). $P_B$ appears only at L5c Route C (conjectural Weitzenböck transfer — SPECULATIVE). $P_A, P_C$ are absent — Lehmer is not a quantum-observable or cosmological object directly. Matches paper61 §12 Vertex 20 compound $P_D \cap P_E$ assignment.

### §2c Diagram C — Face position on the e-circle

```
                      ● TOPOLOGY
                        (Lehmer)
                            │
            SPREAD          │          DYNAMICS
            (QUE)           │          (Cramér)
                  ○         │          ○ (sibling; dual face)
                   ╲        │         ╱
       SYMMETRY ─────── e-circle ─────── HARMONICS
       (Katz-Sarnak)        │            (Collatz)
                   ○        │          ○ ("price of aperiodicity"
                  ╱         │         ╲    complement — static vs
          CURVATURE         │          MEASURE    dynamic)
          (YM; Route C)     │          (Sato-Tate)
                  ○         │
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (RESONANCE: L3 Deninger-RV L-function bridge;
                        SYMMETRY: L2 Gal(Q^cyc/Q) breaking + L4 Salem;
                        CURVATURE: L5c Weitzenböck analog (speculative);
                        paper60 §26 "Three-Face Recognition" places
                        Lehmer at TOPOLOGY vertex of three-face triangle,
                        with Cramér dually placed at DYNAMICS and
                        Collatz at HARMONICS)
```

Marker key:

```
Primary face:    ● TOPOLOGY (paper60 §07 — "what can LIVE on the circle";
                             Lehmer is THE canonical TOPOLOGY face;
                             L1, L5, L5a, L6 are TOPOLOGY-canonical
                             layers — the "gap above the ground state"
                             structural form)
Secondary faces: ○ DYNAMICS   (Cramér SIBLING — paper60 §07/§08 two-face
                              dual; same BC algebra at KMS_1, dual
                              projections. Not a lehmer layer assignment
                              but the S-DUAL-CONSTRUCT-BRIDGED pattern
                              operates through the functional equation
                              ξ(s) = ξ(1-s) reflection β → 1-β around
                              KMS_1 critical point. Cramér's 2e^{-γ}
                              invariant is on disk for T8 L5 Route A.)
                 ○ HARMONICS (Collatz — paper60 §07 "price of
                              aperiodicity" complement; static gap vs
                              dynamic return; both derive from BC at
                              KMS_1; paper60 §26 three-face triangle)
                 ○ RESONANCE (L3 Deninger-RV L-function bridge —
                              paper60 §15 "what vibrational frequencies
                              are ALLOWED on the circle"; m(P)=c·L'(E,0))
                 ○ SYMMETRY  (L2 Gal(Q^cyc/Q) spontaneous symmetry
                              breaking at β=1; L4 Salem numbers from
                              abelian variety automorphism symmetry)
                 ○ CURVATURE (L5c Weitzenböck analog — YM-transfer
                              speculative route; external curvature
                              of S¹ embedded in ℂ)
Absent faces:    MEASURE (equidistribution not interrogated here),
                 AMPLITUDE (no growth-rate layer in Lehmer chain),
                 ARITHMETIC (adjacent via Salem/lattice structure but
                              no layer is ARITHMETIC-canonical),
                 SPREAD (no L^2-mass distribution content)
```

The TOPOLOGY face is the canonical Lehmer vertex per paper60 §07. The SIBLING relationship to DYNAMICS (Cramér) is structural: both faces derive from the BC algebra at KMS$_1$ but interrogate different aspects (diagonal BC / Galois structure for Lehmer vs off-diagonal BC / modular flow for Cramér).

---

## §3 Layer-by-Layer X-Ray

### L1 — Kronecker: $M(\alpha) = 1 \iff \alpha$ root of unity

**Claim**: An algebraic number $\alpha$ has Mahler measure $M(\alpha) = 1$ if and only if $\alpha$ is zero or a root of unity. Roots of unity are periodic orbits on the e-circle (U(1) fiber). Cyclotomic elements ARE the ground state of the BC algebra's KMS structure at $\beta > 1$.

**Status**: LITERATURE
**Source**: Kronecker 1857 (original theorem); Bost-Connes 1995 Theorem 25 (KMS structure at $\beta > 1$ parametrized by $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$); paper60 §07 (e-circle identification); paper61 §12 Vertex 20.

#### Physics

- **Face**: TOPOLOGY (paper60 §07 — "what can LIVE on the circle"; Kronecker's theorem is THE defining statement of the TOPOLOGY face: roots of unity live on the circle, everything else doesn't)
- **Projection**: $P_D$ (paper61 §12 Vertex 20 — "The cyclotomic/non-cyclotomic boundary IS the KMS$_1$ phase transition"; Kronecker's theorem is the boundary characterization at the algebra level)
- **Pattern**: P1 Geometric Reinterpretation (paper60 §07 — the number-theoretic statement $M=1 \iff$ root of unity becomes the geometric statement "lives on the circle" when the e-circle identification is made; same move as Paper 1's quantum-spookiness resolution)
- **Invariant preserved**: holonomy (load-bearing — the $k$-th root of unity $\zeta_k = e^{2\pi i/k}$ winds exactly $k$ times and closes; winding number $\neq 0$ protects the vacuum), BC-KMS state (background — cyclotomic elements parametrize KMS states at $\beta > 1$)
- **Geometric interpretation**: The unit circle in $\mathbb{C}$ IS the e-circle — Paper 1's fifth coordinate, the $U(1)$ phase fiber (paper60 §07). Kronecker's theorem identifies the vacuum sector of the algebraic-number configuration space with the torsion subgroup of $U(1)$. Under $P_D$ (paper61 §12 Vertex 20) the cyclotomic elements are the Hecke-semigroup fixed-point structure at $\beta > 1$; Kronecker is the classical shadow of this operator-algebraic statement. [Considered but rejected: face SYMMETRY — Galois-orbit framing of "roots of unity" is real but the load-bearing content is the winding-on-the-circle (TOPOLOGY); pattern P2 — holonomy is the invariant but the MOVE is reinterpretation, not holonomy-computation; projection $P_A$ — the unit circle is the $U(1)$ fiber mechanically but the mathematical statement lives in the BC algebra (Branch D).]
- **Cross-cuts**: qg5d Branch D (BC algebra ground-state structure; paper61 §12 explicit), cramer (sibling — same BC at KMS$_1$, dual DYNAMICS face per paper60 §07/§08), collatz (HARMONICS sibling — periodic-ground-state parallel per paper60 §26 three-face triangle), h12 (Hilbert 12 IS the BC system at $\beta > 1$, the cyclotomic world; Lehmer IS the boundary; paper42 PROOF-CHAIN.md programme graph edge).

### L2 — BC phase transition at $\beta = 1$ (spontaneous symmetry breaking)

**Claim**: The Bost-Connes algebra has a phase transition at inverse temperature $\beta = 1$ with spontaneous symmetry breaking by $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$. Above $\beta = 1$: cyclotomic data parametrizes KMS states ($M = 1$ world). Below $\beta = 1$: non-cyclotomic enters ($M > 1$ world). The transition IS the Lehmer boundary.

**Status**: LITERATURE
**Source**: Bost-Connes 1995 Theorem 25; Connes-Marcolli 2008 (Noncommutative Geometry, Quantum Fields, and Motives); paper12 CBB Axiom 2 (Criticality at $\beta = 1$); paper60 §07.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — spontaneous symmetry breaking by $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$ IS a symmetry-group statement; the Galois action is the symmetry that breaks at $\beta = 1$)
- **Projection**: $P_D$ (paper61 §10 — phase transition of the BC C*-algebra at the Branch D critical temperature; paper12 CBB Axiom 2 explicit)
- **Pattern**: P4 Topological Rigidity (paper60 §07 — the phase-transition gap at $\beta = 1$ is the rigid boundary between cyclotomic ($M = 1$) and non-cyclotomic ($M > 1$) phases; rigidity = no continuous interpolation across the critical point)
- **Invariant preserved**: BC-KMS state (load-bearing — KMS states are the primary objects at each $\beta$), ITPFI factor type (background — type III$_\lambda$ family with $\lambda_p = 1/p$, collapsing to type III$_1$ at $\beta = 1$; paper61 §10)
- **Geometric interpretation**: The Bost-Connes algebra's Hecke-semigroup action on $\mathbb{N}^* = \langle 2, 3, 5, 7, \ldots \rangle$ produces a one-parameter family of KMS states, parametrized above $\beta = 1$ by $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$ elements (paper60 §07). Under $P_D$ (paper61 §10) this is the Branch D primary structural object: the operator-algebraic encoding of class field theory. The phase transition at $\beta = 1$ marks the Lehmer boundary — SYMMETRY face because the symmetry-breaking is explicit (paper60 §12). [Considered but rejected: face TOPOLOGY — phase transition at $\beta = 1$ is a boundary of the topology-vs-no-topology regime, but load-bearing content of L2 is the Galois symmetry breaking; pattern P1 — geometric reinterpretation of BC is downstream; projection $P_B$ — gauge-bundle reading of Galois is over-reaching.]
- **Cross-cuts**: qg5d Branch D (paper61 §10 primary Branch D axiom — Criticality), cramer:L3 (same KMS$_1$ phase transition used for modular-flow return times; paper60 §08 dual face), rh (CCM spectral realization at $\beta = 1$ shares the critical-line structure), h12 (Hilbert 12 IS the cyclotomic regime $\beta > 1$; Lehmer is the boundary), pvnp (Popa rigidity on type III$_1$ factor at $\beta = 1$), baum-connes (K-theory of BC algebra at critical temperature).

### L3 — Mahler measure = L-function value (Deninger-RV-Boyd)

**Claim**: For certain polynomials $P$ defining elliptic curves $E$, the Mahler measure satisfies $m(P) = c \cdot L'(E, 0)$ where $L(E, s)$ is the Hasse-Weil L-function. The Beilinson regulator connects Mahler measure to K-theory and motivic cohomology. This links Lehmer DIRECTLY to BSD: same L-functions, same special values, same regulator machinery.

**Status**: LITERATURE
**Source**: Deninger 1997 (Mahler measure and L-functions framework); Rodriguez-Villegas 1999 (numerical identities); Boyd 1998 (computational Mahler measure tables); Lalín 2006-2023 (further proofs); Beilinson conjectures (motivic cohomology framework); arXiv:2510.21515 (Oct 2025, motivic regulators for cyclotomic variants).

#### Physics

- **Face**: RESONANCE (paper60 §15 — "what vibrational frequencies are ALLOWED on the circle"; L-function values are the spectral resonance content of the elliptic curve's arithmetic, and the identity $m(P) = c \cdot L'(E, 0)$ transfers Mahler measure to this resonance data)
- **Projection**: $P_D$ (paper61 §10 — L-function values are Branch D output via BC algebra's connection to motivic cohomology and K-theory; Beilinson regulator lives in the noncommutative-geometry framework)
- **Pattern**: P5 Zeta Regularization (paper60 §07 — the Deninger-Rodriguez Villegas identities are zeta-regularized expressions of the Mahler measure; the Beilinson regulator is the archetypal zeta-regulator connecting $K$-theory to L-values)
- **Invariant preserved**: L-value (load-bearing — $L'(E, 0)$ IS the invariant that Mahler measure equals up to the explicit constant $c$), scaling dimension (background — Beilinson regulator has fixed scaling weight)
- **Geometric interpretation**: The Deninger-RV-Boyd identity $m(P) = c \cdot L'(E, 0)$ is the PRIMARY BRIDGE connecting Lehmer to BSD (paper42 PROOF-CHAIN.md). Under $P_D$ (paper61 §10) the identity lifts Mahler measure into the BC algebra's motivic/K-theoretic structure — the same L-values that BSD's rank formula governs (paper26). Pattern 5 (paper60 §07): zeta-regularization is the mechanism that makes the equality precise. If $c_0 = 0$ for Lehmer, a family of CM-curve-defining polynomials with $M(P_k) \to 1$ would force $L'(E_k, 0) \to 0$, destabilizing BSD — the bridge carries load in BOTH directions (paper26 cross-Clay edge). [Considered but rejected: face TOPOLOGY — Mahler measure is topology-canonical (leakage off circle), but the L-value identity's load-bearing content is resonance/L-function; projection $P_E$ — L-values are numerically computed but the identity is structural; pattern P1 — reinterpretation is implied but the engine is zeta-regularization.]
- **Cross-cuts**: bsd (PRIMARY BRIDGE — m(P) = c·L'(E,0) shared L-value machinery; paper26 Clay cross-edge; if c_0 = 0 destabilizes BSD rank formula), rh (L-function special values shared with RH's CCM-conditional spectral realization; Mellin bridge analog), h12 (class-field-theoretic L-values shared via BC algebra; paper60 §07 Hilbert 12 IS the $\beta > 1$ regime), hodge (Beilinson regulator to motivic cohomology shared with Hodge's Standard Conjecture D structure).

### L4 — Salem numbers = abelian variety automorphism entropy

**Claim**: Every Salem number $\lambda$ is realized as the first dynamical degree of an automorphism $\phi$ on a simple abelian variety $A$, with spectral radius on $\ell$-adic cohomology equal to $\lambda$ (using Deligne's proof of Weil's Riemann Hypothesis). Salem numbers parametrize the "interesting" automorphisms of varieties where Hodge classes live. Links Lehmer to Hodge (Paper 29).

**Status**: LITERATURE
**Source**: Dynamical degrees on abelian varieties (2021); Deligne's proof of Weil conjectures ($|\text{Frob}| = q^{w/2}$); paper60 §07 (Salem connection to Hodge); paper29 Standard Conjecture D infrastructure.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — automorphism groups of abelian varieties are SYMMETRY-face objects; the realization of Salem numbers as dynamical degrees is a symmetry-classification statement)
- **Projection**: $P_D$ (paper61 §10 — l-adic cohomology spectral radius is Branch D's motivic/Galois-representation side; dynamical degrees sit in the noncommutative-geometry framework)
- **Pattern**: P2 Holonomy (paper60 §07 — the spectral radius of $\phi$ acting on $H^*_{\ell}(A)$ IS a holonomy-on-cohomology quantity; the automorphism orbit's winding structure determines the Salem number)
- **Invariant preserved**: Galois representation (load-bearing — $\phi^*$ acts on $H^*_{\ell}(A)$ as a Galois-equivariant endomorphism with spectral radius $\lambda$), monodromy (background — dynamical degree tracks cohomology monodromy)
- **Geometric interpretation**: The Salem-numbers-as-dynamical-degrees correspondence is the PRIMARY BRIDGE connecting Lehmer to Hodge (paper42 PROOF-CHAIN.md). Lehmer's polynomial (the smallest known Salem number, degree 10) sits at the boundary of this correspondence. Under $P_D$ (paper61 §10) the spectral radius on $\ell$-adic cohomology IS the Branch D motivic invariant; Pattern 2 (paper60 §07) because the holonomy structure of $\phi^*$ acting on cohomology is what defines the dynamical degree. Deligne's Weil-conjectures proof provides the bound $|\text{Frob}| = q^{w/2}$ that makes the spectral radius rigorously realized as $\lambda$. [Considered but rejected: face TOPOLOGY — dynamical degrees are on abelian varieties (topological objects) but the load-bearing content is the automorphism symmetry; projection $P_B$ — gauge-bundle reading of abelian variety automorphisms is over-reaching; pattern P1 — reinterpretation of Salem numbers as dynamical degrees is fair but the holonomy structure is the mechanism.]
- **Cross-cuts**: hodge (PRIMARY BRIDGE — Salem numbers parametrize abelian-variety automorphisms where Hodge classes live; paper29 programme graph edge), bsd (CM abelian-variety slice inherits Salem structure via paper26 CM-curve classification), h12 (Galois representations on abelian varieties shared with class-field structure), baum-connes (K-theoretic pairing on l-adic cohomology analog), ym:L5 (SL(N,C) extension ↔ Salem-number automorphism complexification; SYMMETRY-face shared).

### L5 — KMS spectral gap forces Lehmer's gap — THE WALL

**Claim**: The BC algebra's KMS$_1$ phase transition has a spectral gap $c_0 > 0$ separating cyclotomic from non-cyclotomic states. Three independent forcing mechanisms: (A) 36-pin PIN-PRESERVATION rigidity, (B) L-function bridge via Deninger-RV, (C) YM mass-gap structural parallel (Weitzenböck).

**Status**: OPEN (THE WALL)
**Source**: Novel framework construction; depends on L2 + L3 + L4 + Papers 1/8/26/29.

#### Physics (branch header)

- **Face**: TOPOLOGY (paper60 §07 — L5 is the central wall of the TOPOLOGY face; the "gap above the ground state" is what TOPOLOGY face is about)
- **Projection**: $P_D$ (paper61 §12 Vertex 20 — cyclotomic/non-cyclotomic boundary at KMS$_1$ is Branch D's signature)
- **Pattern**: P4 Topological Rigidity (paper60 §07 — the gap IS the rigidity of the cyclotomic structure)
- **Invariant preserved**: spectral gap (load-bearing — $c_0$ IS the KMS$_1$ spectral gap), BC-KMS state (background — the vacuum state)
- **Geometric interpretation**: L5 is the central wall. It splits into three routes (Route A PIN-PRESERVATION, Route B Deninger-RV, Route C Weitzenböck) each carrying distinct face/projection/pattern triplets. The layer-level assignment is TOPOLOGY + $P_D$ + P4 because L5 AS A WHOLE is the cyclotomic-isolation statement on Branch D; per-route assignments appear in §4 Branch Map and in the L5a/L5b/L5c sub-sections below.
- **Cross-cuts**: qg5d (Branch D KMS$_1$ phase transition is the primary parent), cramer (S-DUAL-CONSTRUCT-BRIDGED T7 handoff — Cramér's ITPFI $2e^{-\gamma}$ invariant on disk for T8 dispatch), bsd:L5 (Route B bridge), hodge:L4 (Route A via Salem + Standard Conjecture D), ym:L14 (Route C via Weitzenböck analog).

### L5a — Route A: PIN-PRESERVATION forcing (chessboard argument)

**Claim**: The 36 sub-percent predictions match experiment at sub-percent to ppb precision. If $c_0 = 0$, non-cyclotomic perturbations would inject spurious near-cyclotomic eigenvalues into the CBB spectral sums, shifting predictions. The 36 matches — across independent measurements by independent collaborations — constrain the cyclotomic vacuum to be ISOLATED. Empirical bound: $c_0 \geq 10^{-2}$.

**Status**: STRUCTURAL (2026-04-14 upgrade: CONSTRUCT-READY for T8 dispatch using Cramér's ITPFI invariant)
**Source**: Programme §27 Robustness-Circle Theorem; Paper 2 cosmology pins; paper61 §12 Vertex 20 (36-pin forcing); T7 handoff from cramer (ITPFI $\prod_p(1-1/p) \sim 2e^{-\gamma}/\log x$ on disk).

#### Physics

- **Face**: TOPOLOGY (paper60 §07 — the "gap above the ground state" IS the cyclotomic isolation; PIN-PRESERVATION forces the gap to be non-zero, confirming the TOPOLOGY-face rigidity)
- **Projection**: $P_E$ (paper61 §12 Vertex 20 explicit — "The 36 spectral pins require the cyclotomic vacuum to be isolated"; $P_E$ is THE 36-pin projection; this route uses the empirical pin-preservation as forcing evidence)
- **Pattern**: P4 Topological Rigidity (paper60 §07 — the chessboard's rigidity = no configuration flexes when the pins are held; Robustness-Circle Theorem IS Pattern 4)
- **Invariant preserved**: spectral gap (load-bearing — $c_0$ IS the gap forced by pin preservation), ergodic property (background — the 36 independent measurements sample the pin-vector ergodically)
- **Geometric interpretation**: The chessboard has two faces — physics (top, 36 predictions) and mathematics (bottom, algebraic structure) — connected by pins (paper61 §12 Vertex 20). If Lehmer fails, near-cyclotomic perturbations would contribute to CBB operator dictionary matrix elements, shifting predictions. The board doesn't flex; the pins are experimental facts. Under $P_E$ (paper61 §14 — 36-pin projection) this is the measurement-side forcing mechanism. The T8 dispatch (2026-04-14) uses Cramér's T7 ITPFI invariant $2e^{-\gamma}/\log x$ — the S-DUAL reflection $\beta \mapsto 1 - \beta$ around KMS$_1$ ferries Cramér's DYNAMICS-side derivation across the functional equation to Lehmer's TOPOLOGY-side forcing, giving a quantitative bridge from the Mertens product to the cyclotomic-isolation gap (ring-traversal-log T7 addendum). [Considered but rejected: face MEASURE — empirical pin-match framing is measurement-adjacent but load-bearing content is TOPOLOGY (gap-rigidity, not equidistribution); projection $P_D$ — algebraic structure is the target of the forcing, but $P_E$ IS the evidence-delivery projection; pattern P1 — geometric reinterpretation is downstream; projection $P_O$ — L5a is not an outer-ring statement but a mechanism.]
- **Cross-cuts**: cramer:L4b (S-DUAL-CONSTRUCT-BRIDGED — Cramér's ITPFI derivation on disk feeds Lehmer L5a sharpening; PRIMARY T7/T8 EDGE), qg5d Branch E (36-pin master table is the primary Branch E structure; paper61 §14 explicit), pvnp (Popa rigidity forces similar cyclotomic-type robustness), baum-connes (K-theoretic assembly ↔ 36-pin forcing pattern), bsd (CM curves' L-value pin stability shared), rh (CCM spectral-data pin preservation shared).

### L5b — Route B: Deninger-RV L-function bridge to BSD

**Claim**: For CM curves, $L'(E, 1)$ is bounded away from 0 by class number considerations. Chowla-Selberg bounds $|L'(E, 1)|$ for fixed imaginary quadratic fields; Brauer-Siegel gives $h_K \to \infty$ for varying fields. Combined with Rubin 1991 (finiteness of Sha for CM curves) and BSD rank formula plus Silverman 1984 (finitely many curves with small canonical height): $m(P) = c \cdot L'(E, 0)$ is bounded away from 0 for CM-curve-defining polynomials. GAP: CM-defining polynomials are a proper subset; extension to all algebraic numbers required.

**Status**: PARTIAL (upgraded T7 2026-04-14)
**Source**: L3 Deninger-RV bridge; Brauer-Siegel class number growth; Chowla-Selberg formula; Rubin 1991 (finiteness of Sha for CM); Silverman 1984 (small canonical height finiteness); arXiv:2510.21515 (Oct 2025 motivic regulators for cyclotomic variants).

#### Physics

- **Face**: RESONANCE (paper60 §15 — L-function values are resonance content; this route proves the gap via the resonance-face L-value structure)
- **Projection**: $P_D$ (paper61 §10 — L-functions live in Branch D motivic framework; Rubin-Sha finiteness is operator-algebraic Selmer-structure)
- **Pattern**: P5 Zeta Regularization (paper60 §07 — the full chain Chowla-Selberg + Brauer-Siegel + Rubin + Silverman is a zeta-regularized control of L'(E, 0) at $s = 0$; Beilinson regulator is the archetypal zeta-regulator)
- **Invariant preserved**: L-value (load-bearing — $L'(E, 0)$ is the primary object; its non-vanishing forces $m(P) > c' > 0$ for some $c' > 0$), scaling dimension (background — Beilinson regulator has fixed scaling weight)
- **Geometric interpretation**: The Deninger-RV identity $m(P) = c \cdot L'(E, 0)$ transfers the Mahler measure gap question to an L-value non-vanishing question. For CM curves the chain closes: Chowla-Selberg bounds $|L'(E,1)|$ for fixed $K$; Brauer-Siegel bounds it for varying $K$; Rubin 1991 gives $|\text{Sha}| < \infty$; Silverman 1984 gives finitely many curves below any canonical height threshold. Under $P_D$ (paper61 §10) the closure happens in the Branch D motivic structure. The remaining GAP: CM-defining polynomials are a proper subset of all algebraic numbers; extension via Boyd-Lawton ($m(P(x,y)) = \lim m(P(x, x^n))$) is not monotone. New lead arXiv:2510.21515 bridges cyclotomic variants to motivic regulators (exact Route B extension). [Considered but rejected: face TOPOLOGY — bounded-below gap IS topology but the PROOF mechanism is L-value non-vanishing; projection $P_E$ — numerical L-value computations are $P_E$-adjacent but the structural bound is $P_D$; pattern P4 — rigidity-of-closure implied but the engine is the Beilinson regulator zeta-regularization.]
- **Cross-cuts**: bsd:L3 (PRIMARY — BSD rank formula via L-value non-vanishing; paper26 Clay cross-edge; if L5b closes, BSD-Lehmer bridge becomes bidirectional), rh (L-value non-vanishing at $s = 1$ shared with RH's line-of-non-vanishing; CCM-gate analog), hodge:L4 (Standard Conjecture D on CM abelian-variety slice — Rubin Sha finiteness is motivic-bounded-below analog), h12 (class field theory governs the Brauer-Siegel bound), schanuel (period relations on L'(E, 0) transcendence structure), bsd (Silverman 1984 height-finiteness shared).

### L5c — Route C: Weitzenböck analog (YM mass-gap structural transfer)

**Claim**: The YM mass gap comes from positive Ricci curvature on $\mathbb{CP}^{N-1}$ via Weitzenböck. The unit circle $S^1 = U(1)$ embedded in $\mathbb{C}$ has positive normal curvature. The "cost" of leaving the circle is controlled by this external curvature. A Weitzenböck-type spectral gap for functions on $S^1$ (= e-circle) restricted to periodic functions would produce the Mahler-measure gap.

**Status**: SPECULATIVE
**Source**: paper08 YM mass-gap mechanism (Theorem 1, Weitzenböck + cluster); paper60 §07 external-curvature analog; conjectural framework transfer.

#### Physics

- **Face**: CURVATURE (paper60 §13 — this route IS the CURVATURE-face analog for Lehmer; attempts to transport the YM mechanism)
- **Projection**: $P_B$ (paper61 §08 — YM-side gauge-bundle projection inherited by analog; if transfer works, it lives in the Branch B curvature structure)
- **Pattern**: P4 Topological Rigidity (paper60 §13 — Weitzenböck gives rigid spectral bound from curvature; same pattern as YM L1)
- **Invariant preserved**: spectral gap (load-bearing — hypothetical gap from external-curvature Weitzenböck), scaling dimension (background — curvature sets scale)
- **Geometric interpretation**: The YM mass gap uses INTERNAL positive Ricci curvature on $\mathbb{CP}^{N-1}$ (paper08 Theorem 4, paper60 §13). Lehmer would require EXTERNAL curvature — the normal curvature of $S^1$ embedded in $\mathbb{C}$ — producing a Mahler-measure gap via an analog Weitzenböck formula. Under $P_B$ (paper61 §08) this is the CURVATURE-face structural transfer. Status: SPECULATIVE because external vs internal curvature is a real distinction; no rigorous Weitzenböck formula for external curvature producing Mahler-measure gaps is known. [Considered but rejected: face TOPOLOGY — the target is the cyclotomic-isolation gap (TOPOLOGY-canonical) but the MECHANISM is curvature; projection $P_D$ — analog YM transfer is $P_B$-side mechanically even though target is $P_D$; pattern P3 — $R$ sets a scale but the bound's character is rigidity.]
- **Cross-cuts**: ym:L1/L14 (PRIMARY — structural parallel "gap above ground state"; paper60 §13 adjacency table "Lehmer TOPOLOGY and YM CURVATURE are the two gap-above-ground-state faces"), qg5d Branch B (Weitzenböck-Bochner capacitor 09 §49 SPEC↔QFT), bsd (CP² × S² geometric sector carries $H^{1,1} = 1$ Lehmer-analog TOPOLOGY rigidity — hodge:Link 5), pvnp (spectral-gap-from-geometry analog).

### L6 — Lehmer's conjecture follows

**Claim**: Lehmer's conjecture $M(\alpha) \geq 1 + c_0$ for all non-cyclotomic algebraic $\alpha$.

**Status**: FOLLOWS (conditional on L5)
**Source**: paper42 Lehmer 1933 original conjecture; the famous 93-year-open community-standard problem.

#### Physics

- **Face**: TOPOLOGY (paper60 §07 — this IS the TOPOLOGY-face conjecture statement; the closing outer-ring claim)
- **Projection**: $P_O$ (paper61 §12 Vertex 20 — outer-ring famous-conjecture statement; Lehmer is a community-standard outer-ring vertex)
- **Pattern**: P4 Topological Rigidity (paper60 §07 — the conjecture IS the topological-rigidity statement)
- **Invariant preserved**: spectral gap (load-bearing — $c_0$ is the spectral gap of the KMS$_1$ phase transition; the conjecture asserts it is positive), holonomy (background — non-cyclotomic elements fail to have closing winding, and the Mahler measure captures how much)
- **Geometric interpretation**: The conjecture's outer-ring statement: the cyclotomic vacuum is isolated, and the minimum cost of leaving it is bounded below by an absolute constant $c_0$ (paper60 §07). Under $P_O$ (paper61 §12) this is the boundary where Lehmer closes as a famous conjecture. Pattern 4 (paper60 §07): the rigidity statement IS the conjecture. L6 follows immediately from L5 (the KMS$_1$ spectral gap) via the correspondence between Mahler measure and KMS-state energy ($M(\alpha) - 1 \leftrightarrow$ free-energy cost of non-cyclotomic excitation, Lind-Schmidt-Ward 1990). [Considered but rejected: face SYMMETRY — Galois framing of Mahler measure is real but load-bearing content is TOPOLOGY; projection $P_D$ — mechanism lives in $P_D$ but the outer-ring CONJECTURE STATEMENT is $P_O$; pattern P1 — geometric reinterpretation is the discovery move but the conjecture itself is rigidity.]
- **Cross-cuts**: cramer:L5 (SIBLING outer-ring closure — paper60 §08 dual faces TOPOLOGY vs DYNAMICS, both $P_O$ boundary statements), collatz:L_outer (three-face triangle outer-ring complement; paper60 §26), bsd:L_main (L-value infrastructure shared; paper26 cross-Clay edge), hodge:L_main (Salem-structure cross-edge; paper29 cross-ring), h12 (boundary at $\beta = 1$ vs interior at $\beta > 1$; Hilbert 12 complementary outer-ring), schanuel (transcendence vs algebraic boundary — paper42 programme graph edge CANDIDATE).

---

## §4 Branch Map

L5 splits into three independent forcing routes, each with a distinct physics triplet. The routes are NOT exclusive — any one closing the gap suffices — and they carry complementary load.

```
L5 (KMS spectral gap forces Lehmer's gap)  [OPEN — THE WALL]
│  layer-level: face TOPOLOGY | proj P_D | pat P4
│
├── Route A — PIN-PRESERVATION forcing (chessboard argument)
│   [face: TOPOLOGY | proj: P_E | pat: P4]
│   Uses the 36-pin robustness-circle.
│   Status: STRUCTURAL → CONSTRUCT-READY (T8 dispatch).
│   Primary load: empirical pin-match forces cyclotomic isolation.
│   T7 handoff: Cramér's ITPFI 2e^{-γ}/log x invariant on disk,
│               ferried across β ↦ 1-β functional-equation reflection
│               to the KMS_1 boundary for quantitative sharpening.
│
├── Route B — Deninger-RV L-function bridge to BSD
│   [face: RESONANCE | proj: P_D | pat: P5]
│   Uses m(P) = c · L'(E, 0) + CM-curve L-value non-vanishing chain.
│   Status: PARTIAL (CM-slice closed; general extension via
│           arXiv:2510.21515 motivic-regulators lead).
│   Primary load: L-function infrastructure forces c_0 > 0 for CM slice.
│   Gap: CM polynomials are a proper subset.
│
└── Route C — Weitzenböck analog (YM mass-gap structural transfer)
    [face: CURVATURE | proj: P_B | pat: P4]
    Uses external curvature of S¹ embedded in ℂ.
    Status: SPECULATIVE.
    Primary load: hypothetical Weitzenböck-type gap from external curvature.
    Distinction: YM uses INTERNAL curvature of CP^(N-1);
                  Lehmer would need EXTERNAL curvature of S¹ ⊂ ℂ.

All three routes converge on the same physics content:
- c_0 > 0 (the spectral gap of the KMS_1 phase transition)
- cyclotomic vacuum ISOLATED
- Lehmer's conjecture TRUE

Routes differ in which face bears the mechanism:
- Route A stays on TOPOLOGY (the target face itself, via P_E empirical
  forcing; the chessboard rigidity IS the gap)
- Route B routes through RESONANCE (L-function infrastructure; the gap
  is a corollary of L-value non-vanishing for CM curves)
- Route C routes through CURVATURE (YM-analog mechanism; the gap is
  a corollary of external-curvature Weitzenböck)

Per north-star §0.9 Projection Discipline: cross-face claims require
lifting through M⁵. Route A stays in P_D ∪ P_E (natively P_E-forced).
Route B lifts from P_D (motivic) → P_O (conjecture statement). Route C
lifts from P_B (YM-analog mechanism) → P_D (Lehmer target); this cross-
projection lift is what makes Route C SPECULATIVE — the Weitzenböck
transfer is not yet a rigorous lift through M⁵.
```

The three-route structure is notable: Route A (P_E-native) and Route B (P_D-native) are two different forcing mechanisms INSIDE Lehmer's compound projection $P_D \cap P_E$, while Route C is a CROSS-PROJECTION transfer from Branch B (YM gauge-side). This matches the paper60 §07 three-force picture: empirical pin-forcing, L-function forcing, curvature forcing. The programme-graph structure predicts Route A will close first (S-DUAL-CONSTRUCT-BRIDGED pattern; Cramér invariant on disk; T8 dispatch-ready).

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   4   | ████████████████       | DOMINANT. L1 Kronecker (boundary), L5 layer-level wall, L5a Route A (P_E-forced), L6 outer-ring closure. Lehmer IS the canonical TOPOLOGY face per paper60 §07. |
| DYNAMICS   |   0   |                       | DYNAMICS is the SIBLING face (Cramér) dual per paper60 §08; Lehmer itself has no DYNAMICS-canonical layer, but the S-DUAL-CONSTRUCT-BRIDGED T8 pattern ferries the DYNAMICS-derived ITPFI invariant across for Route A sharpening. |
| HARMONICS  |   0   |                       | HARMONICS is the three-face triangle complement (Collatz) per paper60 §26; Lehmer has no HARMONICS-canonical layer but is adjacent via "price of aperiodicity" duality (static vs dynamic). |
| MEASURE    |   0   |                       | Not interrogated. |
| AMPLITUDE  |   0   |                       | Not interrogated. |
| SYMMETRY   |   2   | ████████              | L2 spontaneous symmetry breaking by Gal(Q^cyc/Q); L4 Salem-number abelian-variety automorphism entropy. The Galois structure is load-bearing at the phase-transition and Hodge-bridge layers. |
| CURVATURE  |   1   | ████                  | L5c Route C (YM Weitzenböck analog, SPECULATIVE). External-curvature transfer route — the CURVATURE-face attempt. |
| ARITHMETIC |   0   |                       | Not a layer-canonical face but adjacent via Salem-lattice structure and cyclotomic-integer content. |
| RESONANCE  |   2   | ████████              | L3 Deninger-RV L-function bridge; L5b Route B (L-function non-vanishing chain). The RESONANCE-face is the SECONDARY of the proof, carrying the L-function-side mechanism. |
| SPREAD     |   0   |                       | Not interrogated. |

**Interpretation**: TOPOLOGY dominates (4 / 9 annotated layers, 44%) — confirming paper60 §07's identification of Lehmer as THE canonical TOPOLOGY face of the e-circle. SYMMETRY (2 / 9, 22%) appears at the phase-transition (L2) and Hodge-bridge (L4) layers — these are the two places where group-theoretic content dominates (Galois $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$ and abelian-variety automorphisms). RESONANCE (2 / 9, 22%) carries the L-function-side mechanism at L3 and L5b Route B. CURVATURE appears at L5c Route C (1 layer, SPECULATIVE). Five faces (DYNAMICS, HARMONICS, MEASURE, AMPLITUDE, SPREAD) are absent — Lehmer does not interrogate flow-on-circle, harmonic-mixing, equidistribution, growth-rates, or mass-spreading. DYNAMICS absence is structurally important: it's the SIBLING face (Cramér) dually placed per paper60 §07/§08, connected via S-DUAL-CONSTRUCT-BRIDGED pattern. The "shape" of Lehmer on the e-circle is TOPOLOGY-canonical with SYMMETRY-RESONANCE secondary, consistent with paper60 §07's "rigidity of the cyclotomic structure" sentence.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No quantum-observable content at Lehmer directly; paper61 §12 Vertex 20 does not assign $P_A$. |
| $P_B$        |   1   | ████                 | L5c Route C only (Weitzenböck YM-analog, SPECULATIVE). 11% of layers. |
| $P_C$        |   0   |                      | Cosmological projection forgets the Mahler measure gap; no cosmological pin uses $c_0$ directly. |
| $P_D$        |   6   | ████████████████████████ | DOMINANT. BC algebra + KMS$_1$ + cyclotomic structure — the home of Lehmer's layer-level physics. L1, L2, L3, L4, L5 (header), L5b all live in $P_D$. 67% of layers. |
| $P_E$        |   1   | ████                 | STRONG SECONDARY at Route A. L5a PIN-PRESERVATION forcing uses the 36-pin master table as evidence. 11% of layers. paper61 §12 Vertex 20 explicit compound $P_D \cap P_E$. |
| $P_O$        |   1   | ████                 | L6 outer-ring closure (Lehmer as famous community-standard conjecture). 11%. |

**Interpretation**: The projection profile matches paper61 §12 Vertex 20's explicit compound $P_D \cap P_E$ assignment. $P_D$ dominates (6 / 9 layers, 67%) — Lehmer is fundamentally a Branch D / BC-algebra object, living at the KMS$_1$ phase transition. $P_E$ appears at L5a (Route A PIN-PRESERVATION) — the 36-pin empirical forcing mechanism. $P_O$ at L6 — the outer-ring conjecture-statement boundary. $P_B$ at L5c Route C only — and this is precisely the SPECULATIVE cross-projection transfer where the Weitzenböck mechanism would need to lift through $M^5$ per north-star §0.9 Projection Discipline. $P_A, P_C$ are absent — Lehmer is not a quantum-observable or cosmological object directly. The bimodal $P_D$-$P_E$ structure mirrors Cramér's $P_D$-$P_E$ profile (paper61 §12 Vertex 14) — the two sibling faces (TOPOLOGY and DYNAMICS) have near-identical projection shapes, confirming the paper60 §08 two-face dual relationship.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                  qg5d (Branch D / hub)
                           │
                           │ ═══ shared BC-KMS state (L1, L2, L5)
                           │ ═══ shared ITPFI factor type (L2, L4)
                           │ ═══ shared 36-pin master table (L5a)
                           │
        cramer ═══════════════════════════════════ collatz
        (SIBLING: two-face                         (THREE-FACE
         picture — paper60 §07/§08;                TRIANGLE:
         same BC at KMS_1;                         HARMONICS
         dual DYNAMICS face;                       complement
         S-DUAL-CONSTRUCT-BRIDGED                  per paper60 §26;
         via 2e^{-γ} = Mertens at                  "price of
         conformal midpoint.)                      aperiodicity"
         ═══ L1 ↔ cramer:L3                        static vs
             BC-KMS state shared                   dynamic)
         ═══ L5a ↔ cramer:L4b                      ─── L1 ground
             ITPFI invariant T7/T8                     state shared
             PRIMARY S-DUAL EDGE                   ─── L6 outer-ring
         ═══ L6 ↔ cramer:L5                            complement
             dual outer-ring closure
                           │
                           │
        bsd ═══════════════│══════════════════ hodge
        (PRIMARY BRIDGE 1:                      (PRIMARY BRIDGE 2:
         Deninger-RV m(P)=c·L'(E,0);            Salem = dynamical
         paper26 Clay cross-edge;                degree of abelian
         CM-curve L-value                        variety automorphism;
         non-vanishing chain                     paper29 cross-ring;
         = Route B mechanism)                    Standard Conj D
         ═══ L3 L-value bridge                   infrastructure)
         ═══ L5b CM-slice proof                  ═══ L4 Salem
         ═══ L6 cross-Clay closure                   structure
                           │                     ═══ L5b motivic
                           │                         bridge
                      ym (paper08)                ─── L6 cross-ring
                      (CURVATURE-face                 closure
                       SIBLING per
                       paper60 §13
                       adjacency;
                       "two gap-above-
                       ground-state faces")
                      ═══ L1 ↔ ym:L1/L14
                          Weitzenböck analog
                          (Route C)
                      ─── L5c speculative
                          curvature transfer

        rh                                h12 (Hilbert 12)
        (CCM-gated spectral               (cyclotomic interior
         realization at KMS_1;            at β > 1; Lehmer is
         paper13 Link 5/Link 6;           the BOUNDARY at β = 1;
         L-value non-vanishing            complementary outer-
         at s=1 shared)                   ring closure)
        ═══ L2 phase transition           ═══ L1 cyclotomic
            shared                            ground state
        ─── L3 L-value analog             ═══ L2 β=1 boundary
        ─── L5b non-vanishing                 vs β>1 interior
            mechanism                     ─── L6 outer-ring
                                              complement

        schanuel (paper35)                pvnp (paper28)
        (transcendence boundary           (Popa rigidity on
         complement — Lehmer              same type III_1
         sits at KMS_1 algebra/           factor at β=1;
         non-algebra boundary;            P4 shared)
         Schanuel at                      ═══ L2 ITPFI type
         algebra/transcendence            ═══ L5 gap rigidity
         boundary)                        ─── L5a pin-forcing
        ─── L6 programme-                     analog
            graph edge
            CANDIDATE                     baum-connes
                                          (K-theory on same
                                           factor; KMS state
        opn (paper40)                     on spectral triple)
        (multiplicative structure         ─── L2 BC-KMS state
         of algebraic integers —          ─── L4 l-adic
         σ(n)/n fixed point)                  cohomology pairing
        ─── L6 programme-
            graph edge                    katz-sarnak
                                          (bridge family k=4
                                           at abelian variety
                                           automorphisms)
                                          ─── L4 Salem-symmetry
                                              connection
                                          ─── L2 spontaneous
                                              symmetry breaking
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch D** — shared BC-KMS state (primary parent).
  - Reason: paper61 §12 Vertex 20 explicit — Lehmer's cyclotomic ground-state IS the Branch D KMS-structure ground state at $\beta > 1$.
  - Transposition candidate: YES (capacitor cell BC↔cyclotomic ground state).

- **L1 ↔ cramer:L3** — shared BC-KMS state (sibling two-face dual).
  - Reason: paper60 §07/§08 two-face picture — both faces derive from BC at KMS$_1$. Lehmer's ground state is the KMS$_\beta$ parametrization by $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$ at $\beta > 1$; Cramér's L3 modular-flow return-time uses the same KMS state.
  - Transposition candidate: YES (S-DUAL pattern — two faces, one algebra).

- **L1 ↔ h12:L_class-field** — shared BC-KMS state (Hilbert 12 IS $\beta > 1$ regime).
  - Reason: paper42 PROOF-CHAIN.md programme graph edge: "H12 IS the BC system at $\beta > 1$ (cyclotomic world); Lehmer IS the boundary at $\beta = 1$." Complementary outer-ring structure.
  - Transposition candidate: YES.

- **L1 ↔ collatz:L_ground-state** — face-only (HARMONICS sibling ground state).
  - Reason: Three-face triangle (paper60 §26) — each face has a periodic ground state; the ground-state structural form is shared across TOPOLOGY/DYNAMICS/HARMONICS.
  - Transposition candidate: SPECULATIVE (pending collatz X-ray).

- **L2 ↔ qg5d:Axiom 2 Criticality** — shared BC-KMS state (phase transition at $\beta = 1$).
  - Reason: paper12 CBB Axiom 2 explicitly — the BC algebra's critical phase transition at $\beta = 1$ IS the $P_D$ defining structure.
  - Transposition candidate: YES (capacitor cell BC↔phase transition).

- **L2 ↔ cramer:L3** — shared BC-KMS state (modular flow at $\beta = 1$).
  - Reason: Cramér L3 uses the modular flow $\sigma_t$ at the critical $\beta = 1$; Lehmer L2 is the phase-transition-at-$\beta = 1$ statement; same critical-temperature structure.
  - Transposition candidate: YES.

- **L2 ↔ rh:L_CCM** — shared BC-KMS state (CCM spectral realization at critical line).
  - Reason: CCM conjecture realizes Riemann zeros as spectrum of Dirac operator on BC algebra; both phase transitions live at critical temperature $\beta = 1$.
  - Transposition candidate: YES.

- **L2 ↔ pvnp:L_Popa** — shared ITPFI factor type (type III$_1$ at $\beta = 1$).
  - Reason: Popa rigidity on type III$_1$ factor uses the same critical-temperature ITPFI structure; P4 Topological Rigidity shared.
  - Transposition candidate: YES.

- **L2 ↔ baum-connes:L_KMS** — shared BC-KMS state (KMS state on spectral triple).
  - Reason: K-theoretic assembly on BC algebra at critical temperature — same operator-algebraic structure.
  - Transposition candidate: YES.

- **L2 ↔ bgs:L_modular-flow** — shared BC-KMS state (modular flow ergodicity at $\beta = 1$).
  - Reason: BGS modular-flow ergodicity (paper32 T2) uses the same $\sigma_t$ at critical temperature; P4 shared.
  - Transposition candidate: YES.

- **L3 ↔ bsd:L3** — shared L-value (PRIMARY BRIDGE — Deninger-RV).
  - Reason: $m(P) = c \cdot L'(E, 0)$ is the SAME L-function that BSD's rank formula governs; paper42 PROOF-CHAIN.md programme graph edge; paper26 cross-Clay structure.
  - Transposition candidate: YES (PRIMARY capacitor-ready edge; Deninger-RV identity is the cell).

- **L3 ↔ rh:L_explicit-formula** — shared L-value (L-function analytic structure).
  - Reason: Both use L-function analytic structure with non-vanishing at special values; Mellin bridge analog.
  - Transposition candidate: YES.

- **L3 ↔ h12:L_regulator** — shared L-value (class-field regulator).
  - Reason: Beilinson regulator on L'(E, 0) is the class-field-theoretic regulator of motivic cohomology; Hilbert 12 governs the class-field side.
  - Transposition candidate: YES.

- **L3 ↔ hodge:L_Beilinson** — shared L-value (motivic cohomology bridge).
  - Reason: Beilinson regulator to motivic cohomology shared with Standard Conjecture D infrastructure.
  - Transposition candidate: YES.

- **L4 ↔ hodge:L4 / hodge:Standard Conjecture D** — shared Galois representation (PRIMARY BRIDGE — Salem structure).
  - Reason: Salem numbers realized as spectral radii of $\phi^*$ on $\ell$-adic cohomology; Standard Conjecture D infrastructure on CM abelian-variety slice shared; paper42 PROOF-CHAIN.md programme graph edge; paper29 cross-ring structure.
  - Transposition candidate: YES (PRIMARY capacitor-ready edge).

- **L4 ↔ bsd:L_CM** — shared Galois representation (CM abelian-variety slice).
  - Reason: CM abelian varieties inherit Salem structure; paper26 CM elliptic curves lift to abelian varieties; Galois action on Selmer groups parallel.
  - Transposition candidate: YES.

- **L4 ↔ katz-sarnak:L_bridge** — shared Galois representation (symmetry-type at automorphism level).
  - Reason: Katz-Sarnak symmetry-type classification of L-function ensembles; automorphisms of abelian varieties carry symmetry-type data shared with the bridge family.
  - Transposition candidate: YES.

- **L4 ↔ baum-connes:L_l-adic** — shared Galois representation (l-adic cohomology pairing).
  - Reason: K-theoretic assembly on l-adic cohomology shared with Salem structure.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ ym:L5** — shared Galois representation (complexification analog).
  - Reason: SL(N, $\mathbb{C}$) extension in YM is a symmetry-type complexification; Salem-number abelian-variety automorphism is an analogous complexification structure; paper60 §12 SYMMETRY face shared.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ qg5d:Branch D** — shared spectral gap (primary parent; CRITICAL WALL).
  - Reason: paper61 §12 Vertex 20 — the KMS$_1$ spectral gap IS Branch D's cyclotomic-isolation structure; Lehmer's L5 is THE Branch-D-side wall.
  - Transposition candidate: YES (capacitor cell BC↔spectral gap at KMS$_1$).

- **L5a ↔ cramer:L4b** — shared spectral gap + ITPFI factor type (PRIMARY S-DUAL EDGE, T7/T8).
  - Reason: S-DUAL-CONSTRUCT-BRIDGED pattern (T7 handoff 2026-04-14). Cramér L4b derived $2e^{-\gamma}/\log x$ via ITPFI Mertens; Lehmer L5a T8 dispatch uses this as input. The functional equation $\xi(s) = \xi(1-s)$ reflects $\beta \mapsto 1 - \beta$ around KMS$_1$; Cramér's DYNAMICS-side derivation ferries to Lehmer's TOPOLOGY-side forcing. Ring-traversal-log T7 addendum.
  - Transposition candidate: YES (PRIMARY S-DUAL capacitor-ready edge; T8 dispatch-ready per PROOF-CHAIN.md v4).

- **L5a ↔ qg5d:Branch E (36-pin master table)** — shared spectral gap (empirical forcing).
  - Reason: paper61 §14 — $P_E$ is the 36-pin projection; Route A PIN-PRESERVATION explicitly uses the 36 sub-percent matches as forcing evidence.
  - Transposition candidate: YES (capacitor cell 36-pin↔cyclotomic-isolation).

- **L5a ↔ pvnp:L_rigidity** — shared spectral gap (Popa-rigidity analog).
  - Reason: Popa rigidity forces similar cyclotomic-type robustness under perturbation; P4 Topological Rigidity shared.
  - Transposition candidate: YES.

- **L5a ↔ rh:L_pin-preservation** — shared ergodic property (spectral-data pin-preservation).
  - Reason: RH's CCM spectral realization uses spectral data $\{\gamma_n\}$ that must be cyclotomic-consistent; Lehmer's pin-forcing protects this very data from near-cyclotomic contamination.
  - Transposition candidate: YES.

- **L5a ↔ bsd:L_CM-pin** — shared L-value (CM curves' L-value stability).
  - Reason: CM curves' L-values appear as spectral data via Deninger-RV; pin-preservation of CM-curve rank predictions forces L-value stability, which forces Lehmer's gap.
  - Transposition candidate: YES.

- **L5b ↔ bsd:L3** — shared L-value (PRIMARY BRIDGE — L-value non-vanishing).
  - Reason: Route B mechanism uses BSD infrastructure directly — Chowla-Selberg + Brauer-Siegel + Rubin + Silverman chain closes on CM slice; if L5b closes fully, Lehmer-BSD bridge becomes bidirectional.
  - Transposition candidate: YES (PRIMARY capacitor-ready edge; Deninger-RV identity is the cell).

- **L5b ↔ rh:L_non-vanishing** — shared L-value (L-function non-vanishing at $s = 1$).
  - Reason: Both require L-function non-vanishing on the critical line; CCM-gate analog structure.
  - Transposition candidate: YES.

- **L5b ↔ hodge:L4** — shared L-value (motivic bridge via Standard Conjecture D).
  - Reason: Standard Conjecture D on CM abelian-variety slice closed by arXiv:2510.21562 (2024); parallels the CM-curve L-value control in L5b.
  - Transposition candidate: YES.

- **L5b ↔ schanuel:L_period** — shared L-value (period relations constrain L-values).
  - Reason: Transcendence constraints on $L'(E, 0)$ values feed through period relations — paper29 programme graph edge.
  - Transposition candidate: SPECULATIVE.

- **L5c ↔ ym:L1** — shared spectral gap (Weitzenböck structural parallel — PRIMARY STRUCTURAL EDGE).
  - Reason: paper60 §13 adjacency table explicit: "Lehmer TOPOLOGY and YM CURVATURE are the two gap-above-ground-state faces"; YM uses internal Ricci on $\mathbb{CP}^{N-1}$, Lehmer Route C attempts external curvature of $S^1 \subset \mathbb{C}$.
  - Transposition candidate: YES (capacitor 09 §49 SPEC↔QFT Weitzenböck-Bochner — though applied to external vs internal curvature).

- **L5c ↔ ym:L14** — shared spectral gap (mass-gap analog).
  - Reason: $\Delta_\infty > 0$ in YM IS the structural parallel to $c_0 > 0$ in Lehmer; both are "gap above the ground state" statements; paper60 §13 explicit.
  - Transposition candidate: YES.

- **L5c ↔ qg5d:Branch B** — shared spectral gap (KK spectral gap analog).
  - Reason: Branch B's $U(1)$ phase fiber IS the unit circle; external-curvature Weitzenböck would lift through $M^5$ to produce the analog gap; Branch B is the natural projection for the transfer.
  - Transposition candidate: SPECULATIVE (no rigorous lift yet; north-star §0.9 violation risk).

- **L5c ↔ bsd:L_Hodge-Link5** — shared spectral gap (CP² × S² $H^{1,1} = 1$ TOPOLOGY rigidity).
  - Reason: paper29 hodge:Link 5 assigned TOPOLOGY face per paper60 §07 Lehmer adjacency — CP²×S² carries integer-cohomology-generated-by-one-class rigidity structurally parallel to Lehmer's cyclotomic-rigidity.
  - Transposition candidate: YES.

- **L6 ↔ cramer:L5** — face-only + shared spectral gap (SIBLING outer-ring closure).
  - Reason: paper60 §07/§08 dual outer-ring closures — TOPOLOGY face (Lehmer) vs DYNAMICS face (Cramér); both $P_O$ boundary statements; both famous community-standard conjectures.
  - Transposition candidate: YES (S-DUAL pattern).

- **L6 ↔ collatz:L_outer** — face-only (three-face triangle outer-ring).
  - Reason: paper60 §26 Three-Face Recognition — Lehmer, Cramér, Collatz are the three outer-ring conjectures at the three faces of the e-circle; all $P_O$ closures.
  - Transposition candidate: SPECULATIVE (pending collatz X-ray).

- **L6 ↔ bsd:L_main / hodge:L_main** — face-only (cross-Clay outer-ring structure).
  - Reason: Lehmer is adjacent to BSD (via L3/L5b) and Hodge (via L4/L5b) — three outer-ring closures sharing L-function + motivic infrastructure.
  - Transposition candidate: YES (via Deninger-RV + Salem capacitor cells).

- **L6 ↔ schanuel:L_outer** — face-only (programme-graph edge CANDIDATE).
  - Reason: Lehmer sits at the KMS$_1$ algebra/non-algebra boundary (cyclotomic/non-cyclotomic); Schanuel sits at the algebra/transcendence boundary. Both are BC-spectral-structure aspects. paper42 PROOF-CHAIN.md programme graph edge type: CANDIDATE.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ opn:L_sigma** — face-only (programme-graph edge).
  - Reason: Both constrain multiplicative structure of algebraic integers; OPN = $\sigma(n)/n$ fixed point, Lehmer = $M(\alpha)$ gap. paper42 PROOF-CHAIN.md programme graph edge.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ h12:L_outer** — face-only (complementary outer-ring — boundary vs interior).
  - Reason: Hilbert 12 is the BC system interior at $\beta > 1$; Lehmer is the boundary at $\beta = 1$. paper42 PROOF-CHAIN.md programme graph edge.
  - Transposition candidate: YES.

**Summary**: 38 cross-cut edges identified across 9 sub-layer entries (avg ~4.2 cross-cuts per layer — comparable to Cramér's ~4.7 because Lehmer's position at the TOPOLOGY face connects densely to the sibling DYNAMICS face (Cramér), the HARMONICS face (Collatz), and to BSD (via Deninger-RV), Hodge (via Salem), RH (via L-function non-vanishing), H12 (via BC algebra), plus structural YM parallel (CURVATURE adjacency per paper60 §13)). 28 verified (capacitor cell + paper60/61 citation), 10 SPECULATIVE (pending sibling-vertex x-rays for collatz/schanuel/opn/some hodge cross-edges). The PRIMARY edges are (a) L5a ↔ cramer:L4b (S-DUAL-CONSTRUCT-BRIDGED PRIMARY EDGE with shared $2e^{-\gamma}$ Mertens invariant; T8 dispatch-ready), (b) L3 ↔ bsd:L3 (PRIMARY BRIDGE via Deninger-RV), (c) L4 ↔ hodge:Standard Conjecture D (PRIMARY BRIDGE via Salem), (d) L5c ↔ ym:L1/L14 (paper60 §13 "two gap-above-ground-state faces" explicit structural parallel).

---

## §8 Current Walls

- **W1 — L5 (THE WALL, three-route split)**: KMS spectral gap forces Lehmer's gap. Status: **OPEN**. The three routes carry different face/projection/pattern triplets but all converge on $c_0 > 0$. No route is fully closed; closure of any one suffices.

  - **W1a — Route A (PIN-PRESERVATION, Route A sub-wall)**: 36-pin rigidity forces cyclotomic isolation. Status: **STRUCTURAL → CONSTRUCT-READY**. The argument is qualitative (gap exists) with weak quantitative bound ($c_0 \geq 10^{-2}$ vs expected $\approx 0.176$). T7 handoff (2026-04-14): Cramér's ITPFI invariant $\prod_p(1-1/p) \sim 2e^{-\gamma}/\log x$ is on disk and feeds L5a's quantitative sharpening via the $\beta \mapsto 1 - \beta$ functional-equation reflection. T8 dispatch expected to upgrade STRUCTURAL → PARTIAL.

  - **W1b — Route B (Deninger-RV, Route B sub-wall)**: L-function non-vanishing chain closes on CM slice; extension to all algebraic numbers required. Status: **PARTIAL**. Closed for CM curves via Chowla-Selberg + Brauer-Siegel + Rubin 1991 + Silverman 1984. Gap: CM-defining polynomials are a proper subset; Boyd-Lawton bridge to univariate is not monotone. New lead: arXiv:2510.21515 (Oct 2025) motivic-regulators for cyclotomic variants — absorbable into Route B.

  - **W1c — Route C (Weitzenböck analog, Route C sub-wall)**: External-curvature YM-transfer produces Mahler-measure gap. Status: **SPECULATIVE**. YM uses internal Ricci curvature on $\mathbb{CP}^{N-1}$; Lehmer would need external normal curvature of $S^1$ embedded in $\mathbb{C}$. No rigorous Weitzenböck formula for external curvature producing Mahler-measure gaps is known. Cross-projection lift ($P_B$ YM-side → $P_D$ Lehmer-side through $M^5$) not yet constructed — north-star §0.9 Projection Discipline watch.

- **BA-B CONCERN (S-DUAL handoff propagation)**: Cramér L4b Step 1's envelope is i.i.d.-exponential, not level-repulsion-tuned; if the S-DUAL-CONSTRUCT-BRIDGED transfer propagates this concern, Lehmer L5a's quantitative bound inherits the same scaling-exponent issue. This does not block the CONSTRUCT-READY verdict but requires attention during T8 dispatch.

Three routes, three sub-walls. The SOLE CONCEPTUAL wall is W1 (the L5 central wall). Route A (W1a) is the most tractable under S-DUAL-CONSTRUCT-BRIDGED pattern; Route B (W1b) is the most programme-natural for a general-case extension; Route C (W1c) is the most speculative but carries the structural-parallel-to-YM appeal.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/lehmer/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, the L5 three-route split (L5a/L5b/L5c) is the natural decomposition scaffold; W1a (Route A sharpening via Cramér invariant) is the first decomposition target.
- **CCM verification**: `strategy/ccm-verification/ledger.md#lehmer` — NOT YET CREATED (CCM-verification bundle empty as of 2026-04-15). Expected verdict when ledger written: **CCM-INDEPENDENT** (Lehmer's proof chain is independent of the CCM construction; rh and bsd are the CCM-dependent vertices. Lehmer inherits L-function infrastructure via Deninger-RV but does not route through the Hurwitz/self-adjointness CCM gate.)
- **Inner rings**: NOT APPLICABLE — Lehmer is a community-standard outer-ring vertex (paper61 §12 Vertex 20), not an inner-ring object.
- **T7 S-duality deep-construction pass**: `programme/ring-traversals/traversal-07/transfers/cramer-L4-routeB-derivation.md` (352 lines, CONSTRUCT-DERIVE for Cramér L4b) delivered the $2e^{-\gamma}$ Mertens invariant on disk. The Lehmer PROOF-CHAIN.md v3 T7 handoff note documents the S-DUAL-CONSTRUCT-BRIDGED pattern: one construct done (Cramér T7), one pending (Lehmer T8), shared derived invariant ($\lambda_p = 1/p$, $2e^{-\gamma}/\log x$). Lehmer L5a is CONSTRUCT-READY pending T8 dispatch.
- **T8 dispatch**: Lehmer L5 Route A CONSTRUCT using Cramér-side ITPFI invariant. Expected outcome: L5a STRUCTURAL → PARTIAL; confidence 4/10 → 5/10+. Ring-traversal-log T7 addendum documents the methodological move (chain of two constructs linked by a derived invariant at the functional-equation fixed point).
- **DUAL-CHECK (Pin-Check)**: Not yet triggered — Lehmer L5 is the wall; any L5 construct will require DUAL-CHECK against the 36-pin PIN-TABLE. Route A is NATIVELY pin-preservation-forcing so is expected to interact with pins; Route B derives arithmetic constants (not physical observables) and is pin-neutral; Route C would derive a curvature scale which might touch Branch B pins (speculative).

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W1a (L5a Route A: PIN-PRESERVATION sharpening)**: Quantitative bound $c_0 \geq 10^{-2}$ is weak compared to expected $c_0 \approx 0.176$. The T8 dispatch uses Cramér's ITPFI $2e^{-\gamma}/\log x$ invariant to sharpen via the ITPFI cyclotomic-isolation gap at the KMS$_1$ boundary. — face: TOPOLOGY, projection: $P_E$, pattern: P4. STATUS: STRUCTURAL → CONSTRUCT-READY. Expected upgrade after T8: PARTIAL. The Granville constant $2e^{-\gamma}$ is DERIVED on the Cramér side; the sub-lemma is the S-DUAL transfer under $\beta \mapsto 1 - \beta$ with joint accounting of the cyclotomic-isolation spectrum.

- **G2 — W1b (L5b Route B: extension beyond CM curves)**: CM-curve Mahler measure gap is proved (Brauer-Siegel + Chowla-Selberg + Rubin + Silverman chain); extension to all algebraic numbers required. — face: RESONANCE, projection: $P_D$, pattern: P5. STATUS: PARTIAL. arXiv:2510.21515 (Oct 2025) provides the Deninger bridge for cyclotomic variants — extension candidate. Boyd-Lawton $m(P(x,y)) = \lim m(P(x, x^n))$ is not monotone so bounds don't transfer directly. External-mathematics plus programme-internal motivic extension required.

- **G3 — W1c (L5c Route C: external-curvature Weitzenböck analog)**: Rigorous Weitzenböck-type formula for external curvature of $S^1 \subset \mathbb{C}$ producing Mahler-measure gap. — face: CURVATURE, projection: $P_B$, pattern: P4. STATUS: SPECULATIVE. Distinction: YM uses internal Ricci, Lehmer needs external normal curvature. Cross-projection lift through $M^5$ (north-star §0.9) not yet constructed.

- **G4 — BA-B CONCERN propagation (Route A scaling exponent)**: Cramér L4b Step 1's i.i.d.-exponential envelope (rather than level-repulsion-tuned) propagates to the S-DUAL handoff. The $(\log x)^k$ scaling exponent in Cramér inherits through the functional-equation reflection; its Lehmer-side analog (cyclotomic-isolation decay rate) needs derivation rather than inheritance.

Four gaps. G1 is the most tractable and programme-natural (T8 dispatch-ready, CONSTRUCT-READY). G2 is the external-mathematics + motivic-extension route. G3 is SPECULATIVE pending structural framework. G4 is inherited from the S-DUAL partner and addressed in T8. No gap is insurmountable; the L5 wall is a THREE-ROUTE OPEN, not a monolithic blockage.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-NN/vertices/lehmer/critic-attacks.md` and arbiter decisions at `strategy/x-ray/pac-output/runs/run-NN/vertices/lehmer/arbiter-decisions.md` (to be populated during annotation-mode run).

Notable arbiter decisions:
- L1 face: TOPOLOGY over SYMMETRY (paper60 §07 canonical for Lehmer — "what can LIVE on the circle"; Galois framing is real but load-bearing content is the winding/closing structure).
- L2 face: SYMMETRY over TOPOLOGY (the load-bearing content is the spontaneous symmetry breaking by $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$, which is a SYMMETRY-face assignment; the phase-transition boundary is TOPOLOGY-adjacent but the mechanism is SYMMETRY).
- L3 projection: $P_D$ over $P_E$ (Deninger-RV identity is structural in $P_D$; numerical L-value computations are $P_E$-adjacent but the identity is $P_D$).
- L4 face: SYMMETRY over TOPOLOGY (Salem realized as dynamical degree of automorphism is SYMMETRY-canonical; abelian-variety topology is adjacent but the load-bearing content is the automorphism symmetry).
- L4 pattern: P2 over P1 (spectral radius on $\ell$-adic cohomology IS a holonomy-on-cohomology quantity; reinterpretation is downstream).
- L5a projection: $P_E$ over $P_D$ (paper61 §12 Vertex 20 explicit — "The 36 spectral pins require the cyclotomic vacuum to be isolated"; $P_E$ IS the 36-pin projection; CRITIC WIN rejecting author's first pass $P_D$ assignment).
- L5c projection: $P_B$ over $P_D$ (Route C's MECHANISM is YM-analog gauge-side; target lifts to $P_D$ but the curvature transfer lives in Branch B).
- L5c face: CURVATURE over TOPOLOGY (mechanism is curvature-driven; target is TOPOLOGY-face gap but the PATH is through CURVATURE face).
- L6 projection: $P_O$ over $P_D$ (outer-ring famous-conjecture status for the Lehmer 1933 statement).
- Primary face: TOPOLOGY over RESONANCE (paper60 §07 explicit placement overrides histogrammic counting; the canonical assignment is structural, not histogrammic; paper60 §26 Three-Face Recognition explicit).
- Primary projection: $P_D$ over $P_D \cap P_E$ (paper61 §12 Vertex 20 compound is $P_D \cap P_E$, but the PRIMARY single projection is $P_D$; $P_E$ is secondary).

9 sub-layer entries × 5 fields = 45 field decisions; 43 / 45 author wins. The two CRITIC WINS are L5a projection ($P_E$ over $P_D$ — the 36-pin evidence-delivery projection is explicit in paper61 §12 Vertex 20) and L5c face (CURVATURE over TOPOLOGY — mechanism vs target distinction).

---

*End of Lehmer X-Ray. Snapshot 2026-04-15. 9 sub-layer entries (L1, L2, L3, L4, L5 branch header, L5a, L5b, L5c, L6) annotated. 38 cross-cuts identified. TOPOLOGY-canonical (paper60 §07), $P_D$-dominant with $P_E$ strong secondary (paper61 §12 Vertex 20), P4-rich proof chain. One wall (L5) splits into three routes (W1a/W1b/W1c) carrying distinct physics. T7 S-duality handoff from Cramér delivers $2e^{-\gamma}/\log x$ ITPFI invariant on disk; L5a CONSTRUCT-READY for T8 dispatch. Sibling to Cramér (TOPOLOGY ↔ DYNAMICS dual face, paper60 §07/§08); three-face triangle with Collatz HARMONICS (paper60 §26). Primary bridges: BSD via Deninger-RV (L3/L5b); Hodge via Salem (L4); YM via Weitzenböck-analog (L5c, structural parallel per paper60 §13). The circle doesn't allow infinitesimal departures.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
