# X-RAY: Hilbert's Twelfth Problem (h12)

*X-Ray of the h12 proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. April 15, 2026.*

---

## §1 Header

- **Vertex**: h12
- **Paper**: paper25-hilbert-12
- **Live file**: `strategy/proof-chain/h12/PROOF-CHAIN.md` (snapshot 2026-04-15)
- **Top-level claim**: The KMS$_\beta$ states of the Bost–Connes C*-algebra at $\beta > 1$ (broken-ergodicity, Galois-acting regime) generate the abelian extensions of a number field $K$ — equivalently, explicit generators for $K^{\mathrm{ab}}$ arise as matrix elements of the BC operators against bridge-family cocycles $\beta_k \in H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$, $k \in \{2, 3, 4, 6\}$. Four-conjecture programme (CBB Reciprocity + Brauer–KMS Duality + Level-Jump Rigidity + Spectral Kronecker–Weber), Conjecture 5 (V-Hilbert 12) formally RETRACTED 2026-04-11 via Lead 7c (0/30 Stark-rescue candidates pass at `mp.dps = 50`).
- **Current status**: 1/6 PROVED (L1 — BC algebra construction, Bost-Connes 1995); 1/6 LITERATURE (L2 — KMS$_\beta$ parametrized by $\hat{\mathbb{Z}}^*$ characters, Bost-Connes 1995 + Connes-Marcolli 2008); 2/6 CONJECTURED (L3 — CBB Reciprocity; L4 — Brauer–KMS duality / bridge cocycles at $k \in \{2,3,4,6\}$); 2/6 OPEN (L5 — V-Hilbert 12 extraction RETRACTED in literal form; L6 — Spectral Kronecker–Weber). Confidence 2/10 (South-trough vertex per paper60 §28 ellipse map).
- **Primary branch (paper1)**: **D** (Branch D / CBB / Bost-Connes at KMS states; the KMS states at $\beta > 1$ are exactly the Galois-broken-ergodicity regime where class-field structure appears), with **strong secondary E** (bridge-family pins — Pin #9 $\alpha_{PS}^{-1} = 17$, Pin #10 $\lambda_{CKM} = 56/(57\sqrt{19})$ — which per paper61 §12 Vertex 5 are the "explicit evaluations of the BC operators at specific CM points" empirically witnessing the programme).
- **Primary face**: **SYMMETRY** (paper60 §12 — the bridge family at $k \in \{2,3,4,6\}$ IS the Katz-Sarnak symmetry-type selector; H12 IS the Galois-symmetry generation-problem face of the e-circle, "which group acts on $K^{\mathrm{ab}}/K$ and how do we name its generators").
- **Primary projection**: **$P_D$** (paper61 §10 + paper61 §12 Vertex 5 — the unique KMS$_\beta$ states at $\beta > 1$ of the BC algebra ARE the parametrization of $\mathrm{Gal}(\mathbb{Q}^{\mathrm{ab}}/\mathbb{Q})$; every layer of H12 is a statement about the BC algebra's KMS structure, the Galois action, and the bridge cocycle cohomology).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
H12 (Hilbert's 12th Problem) — explicit generators of K^ab via KMS_β, β > 1
│  primary face: SYMMETRY   primary proj: P_D   primary pat: P4
│  confidence: 2/10 (South-trough West zone, paper60 §28)
│  four-conjecture programme; Conjecture 5 (V-Hilbert 12) RETRACTED 2026-04-11
│
├── L1: BC algebra + Hecke semigroup N* → crossed product A_BC   [PROVED — ESTABLISHED]
│      │  face: ARITHMETIC  proj: P_D   pat: P1
│      │  invariant: C*-algebra structure
│      │  source: Bost-Connes 1995 (Selecta Math); paper61 §10 construction
│      │           A_BC = C(Q^cyc) ⋊ N* = C*(Q/Z ⋊ N*)
│      │
│      └── supports L2 via the ground algebra on which KMS_β lives
│
├── L2: KMS_β states (β > 1) parametrized by Ẑ* characters      [LITERATURE]
│      │  face: SYMMETRY    proj: P_D   pat: P1
│      │  invariant: BC-KMS state, Galois representation
│      │  source: Bost-Connes 1995 Theorem 5; Connes-Marcolli 2008 §3
│      │           (below critical β = 1 the phase transition breaks the
│      │            unique KMS_1 into a Ẑ*-family = Gal(Q^ab/Q)-family)
│      │
│      ├── L2a: β > 1 regime — Galois-broken equilibria            [LITERATURE]
│      │      │  face: SYMMETRY   proj: P_D   pat: P4
│      │      │  invariant: BC-KMS state, Galois representation
│      │      │  ("Gibbs states classified by quasi-characters of Ẑ* =
│      │      │   Gal(Q^cyc/Q); each class ↔ Galois element action
│      │      │   on the abelian subalgebra C(Q^cyc) ⊂ A_BC")
│      │      │
│      │      └── cross-cuts bsd L4 (KMS partition function analog),
│      │          rh L2 (same algebra, different temperature β = 1)
│      │
│      └── L2b: uniqueness at β > 1 (per Ẑ* character)             [LITERATURE]
│             │  face: ARITHMETIC  proj: P_D   pat: P1
│             │  invariant: BC-KMS state
│             │  (each extremal KMS_β state is a pure state ↔ one
│             │   character χ ∈ Ẑ*; the profinite integers index them)
│
├── L3: CBB Reciprocity (Conjecture 1)                            [CONJECTURED — W_H12-1]
│      │  face: SYMMETRY    proj: P_D   pat: P4
│      │  invariant: Galois representation, BC-KMS state
│      │  depends: L2 + bridge-family arithmetic
│      │  source: Paper 25 §4; research/162 (k=3 proven); research/179
│      │           (k=4 reduction); research/173 (k=6 reduction)
│      │
│      └── KMS_β symmetry is the Galois action Gal(Q^cyc/Q) via the
│          Frobenius–Jones bridge at (p, ℓ) ∈ {(5,13), (3,13), (7,19)}
│             │
│             ├── L3a: (p, ℓ) = (5, 13), k = 3                    [PROVED — research/162]
│             │        face: SYMMETRY  proj: P_D  pat: P4
│             │        carry cocycle c_arith = ζ_3^floor((i+j)/3)
│             │        class 1/3 in H²(Z/3Z, U(1))
│             │
│             ├── L3b: (p, ℓ) = (3, 13), k = 4                    [CONJECTURED]
│             │        face: SYMMETRY  proj: P_D  pat: P4
│             │        Jones index 4 / orthogonal symmetry type
│             │
│             └── L3c: (p, ℓ) = (7, 19), k = 6                    [CONJECTURED]
│                      face: SYMMETRY  proj: P_D  pat: P4
│                      E₈ / CKM selector
│
├── L4: Brauer–KMS Duality (Conjecture 2; RH as corollary)        [CONJECTURED]
│      │  face: RESONANCE   proj: P_D   pat: P4
│      │  invariant: BC-KMS state, C*-algebra structure
│      │  depends: L3
│      │  source: Paper 25 §5; Lead 7b (cyclotomic Brauer, 4/4 verified)
│      │
│      └── [β_{p,ℓ}] = Obs(ω_1, A_V) ∈ H²(Z/kZ, U(1))
│             │  both sides = 1/k mod Z
│             │  Fuglede–Kadison determinant of Jones conditional
│             │  expectation E_N : M → N at index k gives Δ_FK(E_N) = log k
│             │
│             ├── L4a: cyclotomic Brauer side                     [PROVED — Lead 7b]
│             │        face: SYMMETRY   proj: P_D   pat: P4
│             │        4/4 bridges verified at exact integer arithmetic
│             │
│             ├── L4b: operator-algebra obstruction side          [CONJECTURED]
│             │        face: RESONANCE  proj: P_D   pat: P4
│             │        V-coupled extension A_V via anti-hermitian
│             │        interface V = λτ₁[log R̂, Π_χ] (research/183)
│             │
│             └── L4c: RH as corollary (obstruction vanishing)    [CONJECTURED]
│                      face: RESONANCE  proj: P_O   pat: P4
│                      if duality holds for every (p, ℓ) bridge,
│                      ζ(s) has no zeros off Re(s) = 1/2
│
├── L5: V-Hilbert 12 (Conjecture 5 — RETRACTED 2026-04-11)        [RETRACTED]
│      │  face: HARMONICS   proj: P_D   pat: P1
│      │  invariant: Galois representation, holonomy (Stark phase)
│      │  source: research/267 (refuted); T7c refutation record
│      │           (0/30 rescue candidates at mp.dps = 50)
│      │
│      └── Literal form (Stark-phase identification) refuted. The
│          bridge cocycle 1/k is a discrete invariant in H²(Z/kZ, U(1))
│          and is NOT encoded in any continuous Galois phase of any
│          Stark unit, Gauss sum, Stickelberger element, or L-function
│          derivative the framework has tested.
│             │
│             └── What survives: the cohomological-side bridge
│                 cocycle (L4a) and the bridge-minimality theorem
│                 (Lead 7e, 4/4 lex-unique minima of a zero-SM-input
│                 sieve equalling the SM multiplicities)
│
└── L6: Spectral Kronecker–Weber (Conjecture 4)                   [OPEN — W_H12-2]
       │  face: ARITHMETIC  proj: P_D   pat: P4
       │  invariant: Galois representation, KK mode index
       │  depends: L3, L4
       │  source: Paper 25 §7; generalization of Kronecker-Weber 1886
       │
       └── Every abelian extension of Q(ζ_13), Q(ζ_19) embedded in H_R
           is a finite product of the three named bridges. Analog of
           Kronecker-Weber ("every abelian extension of Q is in some
           Q(ζ_n)") but lifted to the spectral side.
              │
              ├── L6a: for cyclotomic bases (Q(ζ_13), Q(ζ_19))    [OPEN — W_H12-1]
              │        face: ARITHMETIC  proj: P_D   pat: P4
              │        conductor 1729 = 7·13·19 is forced
              │        (Level-Jump Rigidity, Conjecture 3 proved
              │         2026-04-10 research/268)
              │
              └── L6b: general K beyond cyclotomic / CM / tot. real [OPEN — W_H12-2]
                       face: SYMMETRY   proj: P_O   pat: P4
                       the core Hilbert 12 wall — no programme
                       currently handles arbitrary K; Dasgupta-Kakde
                       2023 handles totally real via p-adic Brumer-
                       Stark; CM via j-invariant; Q via Kronecker-
                       Weber; rest is unknown territory
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (Quantum observables do not see
                          Galois action on K^ab directly;
                          the KMS_β parametrization is a
                          P_D operator-algebra fact, not a
                          quantum-measurement statement.)
                                  ▲
                                  │
        ┌─────────────(P_O outer)──────────────────┐
        │                                          │
        │  H12: explicit analytic generators       │
        │       of K^ab via KMS_β, β > 1           │
        │       (Paper 25; 2/10 confidence;        │
        │        4-conjecture programme)           │
        │                                          │
        └───────────────────┬──────────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity        ═══ P_D CBB ═══             P_E pins
    (forgotten —       BC algebra A_BC;          (bridge-family
     no gauge          KMS_β states for β > 1    pins: Pin #9
     coupling          parametrized by Ẑ* =      α_PS⁻¹ = 17
     uses class-       Gal(Q^cyc/Q); bridge      at k=4 orthogonal;
     field gen-        cocycles β_k ∈ H²(Z/kZ,    Pin #10 λ_CKM =
     erators           U(1)) at k ∈ {2,3,4,6};   56/(57√19) at
     directly)         V-coupled extension A_V;   k=6 sextic.
                       Galois-broken ergodicity   paper61 §12
                       IS the phase where Q^ab   Vertex 5: H12 is
                       crystallizes out of the   the compound
                       KMS_1 symmetric state.    P_D ∩ P_E at the
                       paper60 §12 + §14         BC algebra's
                       arithmetic content.       arithmetic content.)
                            │
                            │
                    (P_C forgotten: no cosmological pin uses
                     H12 directly beyond Bridge k=3 ↔ 3 generations,
                     which cross-cuts rather than projects; H12
                     itself does not predict a cosmological
                     observable.)
```

Primary projection $P_D$ uses ═══ doubled line. Paper 61 §12 Vertex 5 declares H12 the compound $P_D \cap P_E$ at the BC algebra's arithmetic content. Secondary $P_E$ (bridge-family pins) is the empirical witness — Pins #9 and #10 are "explicit evaluations of the BC operators at specific CM points" (paper61 §12). Under $P_A / P_B / P_C$ H12's content is entirely forgotten: the Galois-broken KMS regime has no direct quantum, gauge-bundle, or cosmological shadow outside the pin chain. $P_O$ appears only at L6b — the Clay-grade boundary where H12 closes as a Hilbert problem.

### §2c Diagram C — Face position on the e-circle

```
                        TOPOLOGY
                        (Lehmer)
                            │
            SPREAD          │          DYNAMICS
            (QUE)           │          (Cramér)
                  ╲         │         ╱
                   ╲        │        ╱
    ●  SYMMETRY ─────── e-circle ─────── HARMONICS
       (Katz-Sarnak)        │            (Collatz)
                   ╱        │        ╲
                  ╱         │         ╲
          CURVATURE         │          MEASURE
          (YM)              │          (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (RESONANCE and
                        ARITHMETIC adjacent)
```

Marker key:

```
Primary face:    ● SYMMETRY (paper60 §12 — bridge family k ∈ {2,3,4,6}
                   IS the Katz-Sarnak symmetry-type selector; H12 is
                   the generation-problem face for the Galois group
                   acting on K^ab)
Secondary faces: ○ ARITHMETIC (3 layers: L1 BC algebra = C(Q^cyc) ⋊ N*;
                               L2b uniqueness per character; L6, L6a
                               spectral Kronecker-Weber — paper60 §14
                               "primes generate" via Hecke semigroup)
                 ○ RESONANCE  (2 layers: L4 Brauer-KMS duality; L4b,
                               L4c obstruction class and RH corollary
                               — paper60 §15 trace-formula side via
                               Fuglede-Kadison determinant and Jones
                               subfactor index)
                 ○ HARMONICS  (1 layer: L5 retracted Stark-phase
                               identification — paper60 §09 Fourier
                               pattern; retained as historical record)
Absent faces:    TOPOLOGY, DYNAMICS, MEASURE, AMPLITUDE, CURVATURE,
                 SPREAD
```

Interpretation: H12's "shape" on the e-circle is SYMMETRY-canonical with strong ARITHMETIC secondary — reflecting that class-field theory fundamentally asks which Galois group acts (SYMMETRY) and which cyclotomic integers generate (ARITHMETIC). This is consistent with paper60 §28 placing H12 in the South-West quadrant: WEST = algebraic (vs. statistical) content — "what STRUCTURES exist on the circle" rather than "how observables distribute"; SOUTH = ARITHMETIC-adjacent (vs. CURVATURE) — "the framework STAMMERS at additive/multiplicative generator construction beyond Q and imaginary quadratic." RESONANCE secondary (2 layers) reflects the Fuglede-Kadison / Jones subfactor engine that powers the Brauer-KMS duality. TOPOLOGY/DYNAMICS/MEASURE/AMPLITUDE/CURVATURE/SPREAD are absent — H12 does not interrogate winding, modular-flow ergodic return times, equidistribution, growth rate, gauge curvature, or $L^2$-mass-spreading directly.

---

## §3 Layer-by-Layer X-Ray

### L1 — BC algebra + Hecke semigroup construction

**Claim**: The Bost–Connes C*-algebra $A_{BC} = C(\mathbb{Q}^{\mathrm{cyc}}) \rtimes \mathbb{N}^\times = C^*(\mathbb{Q}/\mathbb{Z} \rtimes \mathbb{N}^\times)$ exists as the crossed product of the continuous functions on the cyclotomic field by the multiplicative semigroup of positive integers acting by Hecke operators $\mu_n: e(r) \mapsto e(nr)$.

**Status**: PROVED (ESTABLISHED)
**Source**: Bost–Connes 1995 (Selecta Math. 1:411–457); paper61 §10 construction.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — "the primes are the generators of the BC algebra's Hecke semigroup $\mathbb{N}^* = \langle 2, 3, 5, 7, 11, \ldots \rangle$; the Hecke operators are the MULTIPLICATIVE engine of the BC algebra — they encode factorization, divisibility, the fundamental theorem of arithmetic")
- **Projection**: $P_D$ (paper61 §10 — "$P_D: S^1 \mapsto \hat{\mathbb{Z}} = \widehat{\mathbb{Q}/\mathbb{Z}}$; $P_D: \text{KK tower} \mapsto \mathbb{N}^* \text{ acting on } \hat{\mathbb{Z}}$; the C*-algebra generated by the pair $(\hat{\mathbb{Z}}, \mathbb{N}^*)$ under the crossed product construction is the BC algebra $A_{BC}$")
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 Pattern 1; the BC algebra IS the geometric reinterpretation of the $S^1$ periodic structure as a crossed-product algebra — the abelian subalgebra $C(\mathbb{Q}^{\mathrm{cyc}})$ reads the profinite $\hat{\mathbb{Z}}$ structure off the circle, and $\mathbb{N}^*$ reads the KK-tower index)
- **Invariant preserved**: C*-algebra structure (load-bearing — the crossed-product construction IS the algebraic object), BC-KMS state (background — exists for every $\beta$, but L1 is about the algebra not the state)
- **Geometric interpretation**: L1 is the foundational projection-construction — the BC algebra is what $P_D$ maps the 5D geometry onto (paper61 §10). The e-circle's periodicity is not just a boundary condition but the fundamental algebraic structure of the Bost-Connes algebra: the $S^1$ fiber IS the spectrum of the abelian subalgebra of $A_{BC}$, and the integer KK modes become the Hecke semigroup acting on it. This is ARITHMETIC-face canonical (paper60 §14 "multiplication is the circle's native tongue" — the BC algebra is BUILT from multiplication). [Considered but rejected: face SYMMETRY — the algebra carries the Galois action but at L1 we have the ALGEBRA, not yet the action; symmetry enters at L2 via the KMS states' symmetry class. Projection $P_A$ — quantum interpretation of the algebra is downstream (paper61 §07 notes that $P_A$ preserves algebra structure but forgets operator-algebraic content); $P_D$ is canonical. Pattern P4 — rigidity framing is fair but the construction itself IS geometric reinterpretation (P1).]
- **Cross-cuts**: baum-connes L1 (Q/Z torsion = BC algebra's abelian subgroup = H12 class-field group over Q; paper31 first link), rh L1 (same BC algebra, different KMS temperature β=1 vs β>1), bsd L2 (Hecke eigenvalues of elliptic-curve L-functions factor through $A_{BC}$ via modularity), grh L1 ($BC_\chi$ construction is the character-twist of $A_{BC}$ — H12 provides the cyclotomic base), pvnp L1 (type III$_1$ factor structure inherited from $A_{BC}$), collatz L1 (Hecke operators $\mu_2, \mu_3$ act on $A_{BC}$; Collatz alternation lives here).

### L2 — KMS_β states (β > 1) parametrized by Ẑ* characters

**Claim**: For $\beta > 1$ the Bost–Connes system has a phase-broken regime: the extremal KMS$_\beta$ states form a family parametrized by the characters of $\hat{\mathbb{Z}}^* = \mathrm{Gal}(\mathbb{Q}^{\mathrm{cyc}}/\mathbb{Q})$. Each extremal state is pure and corresponds to one Galois element of the maximal abelian extension of $\mathbb{Q}$.

**Status**: LITERATURE
**Source**: Bost–Connes 1995 Theorem 5; Connes–Marcolli 2008 §3 (Noncommutative Geometry, Quantum Fields, and Motives); PROOF-CHAIN L2.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — "which group acts on the circle? that's the conjecture, that's the symmetry"; for H12 the group is exactly $\hat{\mathbb{Z}}^* = \mathrm{Gal}(\mathbb{Q}^{\mathrm{ab}}/\mathbb{Q})$, and the KMS$_\beta$-state parametrization IS the symmetry-type classification of the BC system at broken-ergodicity)
- **Projection**: $P_D$ (paper61 §10 — KMS states are the canonical operator-algebraic content; paper61 §12 Vertex 5 explicitly says "The KMS states of the BC algebra at $\beta > 1$ are parametrized by $\mathrm{Gal}(\mathbb{Q}^{ab}/\mathbb{Q})$")
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 Pattern 1; the Galois group's action on $\mathbb{Q}^{\mathrm{cyc}}$ is reinterpreted as a parametrization of equilibrium states)
- **Invariant preserved**: BC-KMS state (load-bearing — L2 IS about the KMS states), Galois representation (load-bearing — $\hat{\mathbb{Z}}^*$ is the Galois group)
- **Geometric interpretation**: Below the critical $\beta = 1$ (in the ergodic regime) the KMS state is unique (paper61 §10 ITPFI III$_1$ factor). Above $\beta = 1$ the system phase-breaks: the extremal states parametrize exactly $\hat{\mathbb{Z}}^* = \mathrm{Gal}(\mathbb{Q}^{\mathrm{cyc}}/\mathbb{Q})$. This is the programme's statement of the Bost-Connes phase transition and the CORE of the H12 strategy: the Galois action on $\mathbb{Q}^{\mathrm{ab}}$ is ALREADY PRESENT in the BC algebra — we just have to read it off the KMS parametrization at $\beta > 1$ (paper60 §12 SYMMETRY face, paper61 §10 Branch D). [Considered but rejected: face ARITHMETIC — the Hecke semigroup sits below, but L2 is about which GROUP acts, not about the multiplicative engine; the symmetry-type framing dominates. Pattern P4 — rigidity of the parametrization is real but the move is reinterpretive. Projection $P_O$ — outer-ring boundary is reached only at L6b where H12 closes; L2 lives inside $P_D$.]
- **Cross-cuts**: grh L8 (cyclotomic tower Galois structure = same $\hat{\mathbb{Z}}^*$; H12 aims to make the generators explicit), katz-sarnak L4 (bridge family $k \in \{2,3,4,6\}$ selects symmetry type = subfamily of $\hat{\mathbb{Z}}^*$; paper60 §12), bgs L2 (BC-KMS state at $\beta = 1$; H12 extends above criticality; "H12 uses KMS at $\beta > 1$, BGS is the $\beta = 1$ regime" — shared BC-KMS state invariant), rh L2 (ITPFI factorization uses KMS state; H12 uses the broken-phase version), cramer (Mertens constant $e^{-\gamma}$ appears both in Cramér's prime-gap framework as the modular-flow return-time constant AND in the H12 chain as the class-field temperature; paper60 §08 chord).

### L3 — CBB Reciprocity (Conjecture 1)

**Claim**: The Frobenius–Jones bridge at bridge pairs $(p, \ell) \in \{(5, 13), (3, 13), (7, 19)\}$ induces the Artin reciprocity map intertwining KMS$_1$ states on $BC_\ell$ with Hecke characters of $\mathbb{Q}(\zeta_\ell)$: the cyclotomic Brauer class $[\beta_{p,\ell}] \in H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$ (where $k = |(\mathbb{Z}/\ell\mathbb{Z})^\times / \langle p \rangle|$) intertwines the BC modular flow with the Galois action $\mathrm{Gal}(\mathbb{Q}(\zeta_\ell)/\mathbb{Q})$.

**Status**: CONJECTURED (W_H12-1)
**Source**: Paper 25 §4; research/162 (k=3 case PROVEN); research/179 (k=4 reduction); research/173 (k=6 reduction).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — the Artin reciprocity map is the canonical symmetry intertwiner of class field theory; it sends the Frobenius element to the Galois generator, which is exactly the SYMMETRY-face content)
- **Projection**: $P_D$ (paper61 §10 — Artin reciprocity as operator-algebraic intertwiner lives in Branch D; paper25 §4.4 "the reciprocity map explicitly: $(\mathbb{Z}/\ell\mathbb{Z})^*/\langle p \rangle \to Z(M)/\mathrm{Inn}(M)$")
- **Pattern**: P4 Topological Rigidity (the bridge-family cocycle is TOPOLOGICALLY RIGID — paper08 §36 Pattern 4 "compactness forces discreteness"; here the Brauer class lives in a DISCRETE cohomology group $H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$ forced by the cyclic quotient structure)
- **Invariant preserved**: Galois representation (load-bearing — Gal$(\mathbb{Q}(\zeta_\ell)/\mathbb{Q})$ is the content), BC-KMS state (background — the intertwiner operates on KMS states)
- **Geometric interpretation**: CBB Reciprocity states that the BC modular flow $\sigma_t$ and the Galois action commute via the bridge cocycle — the same statement as classical reciprocity but phrased in operator-algebraic terms. The k=3 case (research/162) is PROVEN by explicit computation of the carry cocycle $c_{\mathrm{arith}}(\tau^i, \tau^j) = \zeta_3^{\lfloor (i+j)/3 \rfloor}$ of class $1/3$ in $H^2(\mathbb{Z}/3\mathbb{Z}, U(1))$. The k=4 and k=6 extensions are STRUCTURAL (carry-cocycle template + Fuglede-Kadison determinant of Jones conditional expectation $E_N: M \to N$ at index $k$ gives $\Delta_{FK}(E_N) = \log k$). Pattern 4 is the ONLY pattern that operates here — bridge-family rigidity is the engine (paper60 §12 "the bridge IS the symmetry-type selector"). [Considered but rejected: face ARITHMETIC — the primes $(p, \ell)$ are arithmetic data but the CONTENT of reciprocity is symmetry-intertwining; pattern P1 — Artin reciprocity is a geometric reinterpretation of Frobenius, but the bridge-cocycle rigidity dominates; projection $P_O$ — the Clay statement of Hilbert 12 lives at L6b, not here.]
- **Cross-cuts**: ym L5 (SL(N,C) extension — Galois complexification of gauge group is structural analog of H12's Galois extension of base field), bsd L6 (Hecke-eigenvalue bound / Step 5c — same Hecke-character arithmetic applied to elliptic curves vs class fields), grh L1 (BC$_\chi$ construction — GRH over Dirichlet characters uses the same cyclotomic Galois structure; H12 aims to make the abelian-extension generators explicit), katz-sarnak L4 (BC representation type = symmetry type; the bridge at $k$ selects the specific symmetry class), bgs L2 (shared BC-KMS state invariant at different $\beta$).

### L4 — Brauer–KMS Duality (Conjecture 2; RH as corollary)

**Claim**: For every bridge pair $(p, \ell)$, the cyclotomic Brauer class $[\beta_{p,\ell}] \in H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$ equals the obstruction class $\mathrm{Obs}(\omega_1, A_V)$ to lifting the unique KMS$_1$ state $\omega_1$ on $BC_\ell$ to a tracial state on the V-coupled extension $A_V = BC_\ell \otimes_V S_{\mathrm{spec}}$. Both classes equal $1/k \bmod \mathbb{Z}$. The Riemann Hypothesis is a corollary (if duality holds for all bridge pairs, $\zeta(s)$ has no off-line zeros).

**Status**: CONJECTURED
**Source**: Paper 25 §5; Lead 7b (cyclotomic Brauer side — 4/4 bridges verified at exact integer arithmetic); research/162 (k=3).

#### Physics

- **Face**: RESONANCE (paper60 §15 — the obstruction class is a 2-cocycle, and its vanishing/non-vanishing is a RESONANCE condition on the GNS-implementing unitaries; the Fuglede-Kadison determinant of the Jones conditional expectation IS the trace-formula-side Δ_{FK}(E_N) = log k)
- **Projection**: $P_D$ (paper61 §10 — trace extension, GNS construction, KMS state lifting all live in Branch D; V-coupled extension uses spectral-action algebra from Paper 11 via operator-algebraic tensor product)
- **Pattern**: P4 Topological Rigidity (paper08 §36 Pattern 4; the obstruction class is DISCRETE — $H^2(\mathbb{Z}/k\mathbb{Z}, U(1)) = \mathbb{Z}/k\mathbb{Z}$ — and its value $1/k$ is rigidly forced by both the arithmetic side (Hasse invariant) and the operator side (cocycle of implementing unitaries))
- **Invariant preserved**: BC-KMS state (load-bearing — lifting the KMS state to $A_V$ is the content), C*-algebra structure (load-bearing — $A_V$ is the V-coupled crossed product)
- **Geometric interpretation**: L4 states that the COHOMOLOGICAL obstruction to extending KMS$_1$ as a trace on the V-coupled algebra equals the ARITHMETIC Hasse invariant of the cyclic algebra $(\mathbb{Q}(\zeta_\ell)/\mathbb{Q}, \mathrm{Frob}_p, \zeta_k)$. Both are $1/k$ in $H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$. This is paper60 §15's RESONANCE face in pure form: the "allowed vibrational frequencies" of the GNS-implementing unitaries form a COCYCLE whose class measures the "mismatch" between local and global symmetry. The RH corollary (§5.4) follows because if Obs vanishes for every bridge, the KMS$_1$ state extends to a trace — forcing the BC spectral operator $\hat{R}$ to have real spectrum (i.e., all Riemann zeros on the critical line). [Considered but rejected: face SYMMETRY — the Brauer cohomology is indexed by a symmetry group but the LOAD-BEARING content is the resonance-class obstruction; projection $P_O$ — RH is outer-ring-shaped but L4 lives inside H12's $P_D$ core, and the RH-corollary is a DERIVED consequence not a primary claim; pattern P1 — cocycle-vs-coboundary is a geometric reinterpretation but the bridge rigidity is the engine.]
- **Cross-cuts**: rh L4 (RH-corollary; same bridge cocycles over $\mathbb{Q}$, the Brauer-KMS duality IS the operator-algebraic path to RH), ym L5 (SL(N,C) Brauer-class cohomology at $k=4$ orthogonal per paper61 §10), bsd L4 (local Brauer-group integrality in elliptic curve $L$-functions; paper26 shares the cocycle machinery), baum-connes L1 (Q/Z torsion = BC abelian subalgebra spectrum, which is where the Brauer cohomology is computed), pvnp L_kill (Popa rigidity = non-perturbative-gap rigidity, analog to Brauer-class vanishing — both are "the rigidity that selects the physical solution"), hodge L4 (motivic Galois action ↔ Brauer-class machinery; Connes-Consani-Marcolli 2005 motivic Galois action, paper61 §12 Vertex 9).

### L5 — V-Hilbert 12 (Conjecture 5 — RETRACTED 2026-04-11)

**Claim** (RETRACTED): The unitary bridge $V: \mathcal{H}_{\mathrm{CCM}} \to \mathcal{H}_R$ acts on specific class-field generators via the Stark phase, identifying the bridge cocycle $1/k$ with continuous Galois phases of Stark-regulator-derived quantities.

**Status**: RETRACTED (was OPEN, now formally withdrawn)
**Source**: research/267 (refutation); T7c refutation record `paper12/relaxation/research/T7c-stark-rescue-verification.md` (0/30 rescue-candidate tests at `mp.dps = 50`; closest near-miss $\Delta \approx 5.4 \times 10^{-3}$ on one bridge, does not extend).

#### Physics

- **Face**: HARMONICS (paper60 §09 — Stark phase as a continuous harmonic on the circle; the retraction says "the bridge cocycle is NOT encoded as a Fourier-continuous phase of any Stark-derived quantity," which is a NEGATIVE HARMONICS result)
- **Projection**: $P_D$ (paper61 §10 — Stark-unit-phase identification would have lived in Branch D as a specific numerical evaluation of the BC matrix elements; the failure is a $P_D$-internal failure, not a cross-projection issue)
- **Pattern**: P1 Geometric Reinterpretation (the retracted conjecture was a proposed geometric reinterpretation — "the abstract cohomology class is concretely realized as a Stark phase"; the reinterpretation fails)
- **Invariant preserved**: Galois representation (load-bearing — what was tested was the Galois phase), holonomy (background — the Stark phase is a circular holonomy)
- **Geometric interpretation**: The retraction is STRUCTURAL not computational: the bridge cocycle $1/k$ is a DISCRETE invariant in $H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$, and the framework has tested six rescue candidates (raw Stark phase, Gauss sum, $\sqrt{N}$-normalized Gauss sum, Gauss sum of $L'$, W-factor signs, raw/genus-rescaled log-Stark, Stickelberger element, conductor-adjusted phase) across all three bridges at 50-digit precision — 0/30 pass. The discrete-cohomology cocycle is NOT representable as any continuous Galois phase of any Stark unit, Gauss sum, Stickelberger element, or $L$-function derivative (paper25 §8.0 retraction notice). What survives: the cyclotomic Brauer side of L4a (Lead 7b, 4/4 bridges at exact integer arithmetic) and the bridge-minimality theorem (Lead 7e). [Considered but rejected: face SYMMETRY — the Stark phase is a Galois-group element but the claim was specifically about its HARMONIC representability (continuous phase), so HARMONICS dominates; pattern P5 — zeta-regularization is absent because the issue is not about divergent sums but about discrete-vs-continuous encoding; projection $P_O$ — the retraction is $P_D$-internal, not a closure issue at the outer boundary.]
- **Cross-cuts**: rh L6 (both H12 and RH aim at the same Galois/BC structure; H12's V-Hilbert retraction does NOT affect RH's path via CCM/Boegli), pvnp L7 (no direct link; tested as Popa-rigidity analog but found independent), grh L5c (H^1 bound is the RH-side analog of L5's Stark-phase test; both are tight quantitative identifications), collatz L3 (Mori 2024 Cuntz O_2 formulation is a different projection of Hecke dynamics — Stark-phase route fails there too).

### L6 — Spectral Kronecker–Weber (Conjecture 4)

**Claim**: Every abelian extension of $\mathbb{Q}(\zeta_{13})$ and $\mathbb{Q}(\zeta_{19})$ embedded in the CBB Hilbert space $\mathcal{H}_R$ is a finite product of the three named bridges $\beta_{5,13}, \beta_{3,13}, \beta_{7,19}$. The analog of Kronecker-Weber ("every abelian extension of $\mathbb{Q}$ is in some $\mathbb{Q}(\zeta_n)$") lifted to the spectral side. Generalizations to arbitrary number fields remain OPEN.

**Status**: OPEN (W_H12-1 for cyclotomic bases; W_H12-2 for general K)
**Source**: Paper 25 §7; Kronecker-Weber 1886; Hilbert 1896.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — "the primes are the generators"; L6 says the BRIDGE PRIMES at conductor 1729 = 7·13·19 generate the cyclotomic abelian extensions in the spectral embedding; this is the most arithmetic-canonical layer of H12), with strong secondary SYMMETRY at L6b (the open general-K problem)
- **Projection**: $P_D$ (paper61 §10 — spectral embedding in $\mathcal{H}_R$ is the Branch D core; the CBB Hilbert space is THE load-bearing operator-algebraic object)
- **Pattern**: P4 Topological Rigidity (paper08 §36 Pattern 4; the bridge family is rigidly forced — conductor 1729 is UNIQUE, by Level-Jump Rigidity / Conjecture 3 PROVED 2026-04-10 research/268; the spectral-Kronecker-Weber closure statement says no NEW bridges exist beyond these three)
- **Invariant preserved**: Galois representation (load-bearing — the abelian extensions are indexed by Galois), KK mode index (load-bearing — the bridge cocycles are indexed by integer $k \in \{2, 3, 4, 6\}$)
- **Geometric interpretation**: L6 is the programme's proposed SOLUTION to Hilbert 12 for cyclotomic bases $\mathbb{Q}(\zeta_{13}), \mathbb{Q}(\zeta_{19})$: the explicit generators ARE the bridge-cocycle-produced finite products of named bridges. The analog of Kronecker-Weber is literal: every $K^{\mathrm{ab}}/\mathbb{Q}$ abelian extension is in some $\mathbb{Q}(\zeta_n)$ (Kronecker-Weber 1886); every $K^{\mathrm{ab}}/\mathbb{Q}(\zeta_\ell)$ abelian extension (for $\ell \in \{13, 19\}$) is a finite product of the three named bridges in $\mathcal{H}_R$ (paper25 §7.1). L6b — the general-K case — is the UNRESOLVED core of Hilbert 12: for arbitrary $K$ (real quadratic, cubic, totally real outside Dasgupta-Kakde 2023's reach, etc.) no analog is known. This is paper60 §28's South-Trough signature: "ARITHMETIC is where the framework STAMMERS" — the BC algebra speaks multiplicatively, but explicit generators for arbitrary $K$ require crossing bridges the algebra does not naturally supply. [Considered but rejected: face SYMMETRY — L6 is about which groups can be realized, but the CONSTRUCTION content (which specific cyclotomic units / bridge products generate) is arithmetic; pattern P1 — spectral-embedding-as-reinterpretation is real but the load-bearing engine is bridge-family rigidity; projection $P_O$ — L6b is the Clay-grade closure of Hilbert 12 and lives at $P_O$; L6a lives inside $P_D$.]
- **Cross-cuts**: grh L8 (cyclotomic abelian extensions; GRH for $L(s, \chi)$ addresses exactly the characters that H12 aims to construct generators for; paper13b), lehmer L1 (Kronecker's theorem: cyclotomic units = roots of unity = periodic orbits on e-circle; H12 is the explicit-generation version of Lehmer's ground-state question), katz-sarnak L1 (every natural L-function family has a symmetry type; H12 aims to construct them), bsd L_Hecke (elliptic-curve $L$-functions factor through Hecke characters; H12's cyclotomic generators underpin CM curve abelian extensions), hodge L4 (motivic Galois action on cyclotomic motives; Connes-Consani-Marcolli 2005), baum-connes L4 (K-theory of the BC algebra — H12's spectral embedding is the K-homology side), cramer (Mertens constant $e^{-\gamma}$ meridian — paper60 §08 H12-Cramér chord).

---

## §4 Branch Map

The H12 proof chain has one major branch point at L3 (the three bridge pairs) and one status split at L5 (RETRACTED) / L6 (OPEN). The four-conjecture programme structure is explicit.

```
L2 (KMS_β parametrization by Ẑ*, LITERATURE)
                │
                ├── Conjecture 1 (CBB Reciprocity) — L3
                │   [face: SYMMETRY | proj: P_D | pat: P4]
                │   depends: L2 + bridge arithmetic
                │      │
                │      ├── k=3 PROVED (research/162)
                │      ├── k=4 CONJECTURED (research/179)
                │      └── k=6 CONJECTURED (research/173)
                │
                ├── Conjecture 2 (Brauer–KMS Duality) — L4
                │   [face: RESONANCE | proj: P_D | pat: P4]
                │   depends: L3
                │      │
                │      ├── Cyclotomic Brauer side PROVED (Lead 7b, 4/4)
                │      ├── Operator-algebra side CONJECTURED
                │      └── RH as COROLLARY (conditional on duality)
                │
                ├── Conjecture 3 (Level-Jump Rigidity)
                │   [PROVED 2026-04-10 via research/268;
                │    does not appear as live PROOF-CHAIN.md link but
                │    supports L6a's "conductor 1729 is forced, not chosen"]
                │
                ├── Conjecture 4 (Spectral Kronecker–Weber) — L6
                │   [face: ARITHMETIC | proj: P_D | pat: P4]
                │   depends: L3, L4
                │      │
                │      ├── L6a: cyclotomic bases (ζ_13, ζ_19) OPEN
                │      └── L6b: general K OPEN (the core Hilbert 12 wall)
                │
                └── Conjecture 5 (V-Hilbert 12) — L5
                    [face: HARMONICS | proj: P_D | pat: P1]
                    RETRACTED 2026-04-11 via research/267 + T7c

Four active conjectures remain (1, 2, 3, 4); Conjecture 5 is preserved as
historical record with retraction banners in paper25 sections 5-8.

The branch into {k = 3, k = 4, k = 6} at L3a/b/c tells us: the bridge-
family structure is PARALLELIZED across the three named bridges. Proving
CBB Reciprocity at k = 3 (research/162, DONE) is structurally the same
as proving it at k = 4 and k = 6 — the carry-cocycle template + Jones
subfactor machinery generalizes uniformly. This is NOT a true three-way
branch: it is a single pattern evaluated at three bridges. The projection
is uniformly P_D; the face is uniformly SYMMETRY; the pattern is
uniformly P4; only the invariant "Galois representation" takes different
concrete values (Z/3Z vs Z/4Z vs Z/6Z).

The retraction of L5 tells us something about the BC framework's
language: discrete cohomology classes in H² are NOT the same kind of
invariant as continuous Galois phases, and the framework's language
does not yet have a native way to translate between them. This is a
real methodological finding — it specifies exactly where the framework's
"arithmetic stammer" (paper60 §28) begins.
```

---

## §5 Face Histogram

Layers counted: L1 + L2 (L2a, L2b sub-layers) + L3 (L3a, L3b, L3c sub-layers) + L4 (L4a, L4b, L4c sub-layers) + L5 + L6 (L6a, L6b sub-layers) = 13 entries.

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | H12 does not interrogate the TOPOLOGY face directly; the Lehmer-cyclotomic-ground-state cross-cut (paper60 §07) is a structural parallel, not a layer assignment. |
| DYNAMICS   |   0   |                       | H12 does not interrogate modular-flow ergodicity directly — it lives above the critical β=1 where ergodicity is BROKEN. The Cramér chord (paper60 §08) is a cross-cut via the Mertens constant, not a layer. |
| HARMONICS  |   1   | ████                  | The retracted L5 (V-Hilbert 12, Stark phase) was the sole HARMONICS-face layer; the retraction is itself a HARMONICS-face negative result (discrete cocycles do not embed as continuous phases). |
| MEASURE    |   0   |                       | H12 does not interrogate equidistribution; the bridge-family at k ∈ {2,3,4,6} SELECTS symmetry types (SYMMETRY face), not measures. |
| AMPLITUDE  |   0   |                       | H12 does not interrogate growth rates / subconvexity. |
| SYMMETRY   |   6   | ████████████████████████ | DOMINANT. L2, L2a, L3, L3a, L3b, L3c — six layers carry the Galois-broken-ergodicity content. H12 IS the SYMMETRY face of the e-circle: which group acts on K^ab, and how. |
| CURVATURE  |   0   |                       | H12 is not a gauge/curvature object; YM is the CURVATURE-canonical vertex. |
| ARITHMETIC |   4   | ████████████████      | STRONG SECONDARY. L1 (BC algebra via Hecke N*), L2b (uniqueness per character), L6, L6a (spectral Kronecker-Weber via conductor 1729 = 7·13·19) — four arithmetic-canonical layers. This is paper60 §14's ARITHMETIC face in its H12 specialization: primes generate, and the specific bridge primes (5, 13, 3, 13, 7, 19) are the forced-not-chosen generators. |
| RESONANCE  |   2   | ████████              | L4, L4b — Fuglede-Kadison determinant of Jones conditional expectation; 2-cocycle obstruction to KMS-state lifting. Paper60 §15 trace-formula side. |
| SPREAD     |   0   |                       | H12 does not interrogate L²-mass-spreading. |

**Interpretation**: SYMMETRY dominates (6/13 layers, 46%) — confirming paper60 §12's identification of the bridge family as the symmetry-type selector and paper61 §12 Vertex 5's characterization of H12 as a Branch-D-primary, Galois-structured vertex. ARITHMETIC is the strong secondary (4/13, 31%), carrying the multiplicative-generator structure of the BC algebra and the bridge-prime conductor. RESONANCE (2/13, 15%) carries the Brauer-cohomology obstruction machinery. HARMONICS (1/13, 8%) is the sole retracted-layer face. SIX faces are absent (TOPOLOGY, DYNAMICS, MEASURE, AMPLITUDE, CURVATURE, SPREAD) — H12 does not interrogate winding, ergodic return times, equidistribution, growth rates, gauge curvature, or mass-spreading. The "shape" of H12 on the e-circle is SYMMETRY-canonical with ARITHMETIC secondary, consistent with paper60 §28's placement of H12 in the South-West ellipse quadrant: West = algebraic (SYMMETRY+ARITHMETIC) rather than statistical faces; South = ARITHMETIC-adjacent where the framework stammers at additive/multiplicative generator construction.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No quantum-observable content at H12 directly; quantum projection forgets the Galois-broken KMS regime (paper61 §07 "$P_A$ preserves superposition, entanglement, Born, Bell, A-B, spin-stat" — none apply to class-field generation). |
| $P_B$        |   0   |                      | No gauge-bundle content; H12 is not a curvature / KK-spectrum object. The SL(N,C) complexification cross-cut with ym L5 is structural-parallel, not a direct projection. |
| $P_C$        |   0   |                      | No cosmological pins use H12 directly; Bridge k=3 ↔ 3 generations cross-cuts rather than projects. |
| $P_D$        |  11   | ████████████████████████████████████████████████ | DOMINANT. Branch D is where the BC algebra, KMS states, Brauer cohomology, bridge family, and spectral embedding all live. 85% of layers. This matches paper61 §12 Vertex 5's compound-projection assignment $P_D \cap P_E$ — $P_D$ is the PRIMARY, $P_E$ is the empirical witness. |
| $P_E$        |   0   |                      | H12 does not contribute a DEDICATED pin, but bridge-family pins (Pin #9 α$_{PS}^{-1}$ = 17 at k=4; Pin #10 λ$_{CKM}$ at k=6) are the empirical confirmation of the bridge structure — they CROSS-CUT to H12 rather than appearing as H12 layers. paper61 §12 Vertex 5 characterization: "$P_D \cap P_E$ at the BC algebra's arithmetic content." |
| $P_O$        |   2   | ████████             | OUTER-RING CLOSURE. L4c (RH as corollary — paper61 §12 Vertex 2) and L6b (the Clay-grade Hilbert 12 wall for general $K$). Both sit at the boundary where H12 closes as a famous conjecture. |

**Interpretation**: The projection profile is heavily concentrated at $P_D$ (11/13 layers, 85%) — H12 is fundamentally a Branch D object. $P_O$ appears at two load-bearing layers: L4c (RH corollary — where H12's Brauer-KMS duality would close RH as a downstream consequence) and L6b (general-K Hilbert 12 — where H12 closes as the historical Hilbert problem). $P_A, P_B, P_C, P_E$ are ABSENT as primary projections — H12 is not a quantum-observable, gauge-bundle, cosmological, or pin-valued object directly. This sharply differentiates H12 from vertices like YM (bimodal $P_B$ + $P_D$), BSD (compound $P_D \cap P_C \cap P_E$), or RH (compound $P_D \cap P_E \cap P_A$). H12 is the PUREST Branch-D vertex in the programme — almost every layer is an operator-algebraic statement about the BC algebra. Paper 61 §10's claim that "Branch D crosses with almost every other face" is structurally witnessed here: H12 is the vertex where Branch D's depth is most exposed.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                       qg5d (Branch D / hub)
                            │
                            │ ═══ shared C*-algebra (L1 BC construction)
                            │ ═══ shared BC-KMS state (L2 KMS parametrization)
                            │ ═══ shared Galois representation (L2 Ẑ* = Gal(Q^cyc/Q))
                            │ ═══ shared bridge family k ∈ {2,3,4,6} (L3, L6)
                            │
                            │
    rh ═════════════════  h12 (Hilbert 12)  ═════════════════  grh
    (same BC algebra,     │                                     (cyclotomic tower
    different KMS β)      │                                      Galois structure
    ═══ L2 ↔ rh:L1 KMS    │                                      L1 ↔ grh:L1 BC_χ
    ═══ L4 ↔ rh:L4 Brauer │                                      L2 ↔ grh:L8 cyclotomic
                          │                                      L6 ↔ grh:L8 closure)
                          │
    bsd ═════════════════ │ ═════════════════  baum-connes
    (Hecke characters     │                    (Q/Z torsion
    for CM curves;        │                    = BC abelian
    H12 aims to           │                    subalgebra
    construct analytic    │                    spectrum;
    generators for        │                    K-theory side)
    abelian extensions    │                    ═══ L1 ↔ bc:L1
    where CM L-fns live)  │                        profinite Q/Z
    ═══ L_Hecke ↔ bsd:    │                    ═══ L6 ↔ bc:L4
        shared Hecke      │                        K-homology
    ═══ L4 ↔ bsd:L_local  │
        local Brauer      │
                          │
    katz-sarnak ══════════│══════════════════  bgs
    (bridge k ∈ {2,3,4,6} │                    (KMS_1 critical;
    selects Katz-Sarnak   │                    H12 is KMS_β>1;
    symmetry type)        │                    shared BC-KMS
    ═══ L3 ↔ ks:L4        │                    state invariant)
    ═══ L6 ↔ ks:L1        │                    ═══ L2 ↔ bgs:L2
                          │
                          │
                    ym (paper08)              cramer (paper43)
                    ─── L3 ↔ ym:L5            ─── L2 / L6 ↔ cramer
                        SL(N,C) bridge k=4        Mertens e^{-γ}
                        gauge-Galois              chord (paper60 §08)
                        complexification          class-field temp
                    ─── L4 ↔ ym:L17               = modular flow
                        local C*-algebra          return-time const.
                        via Brauer cocycle
                    ─── L6a ↔ lehmer:L1           hodge (paper29)
                        Kronecker units           ─── L4 ↔ hodge:L4
                        = roots of unity              motivic Galois
                        = cyclotomic ground           (Connes-Consani-
                        state                         Marcolli 2005
                                                      noncommutative
                    pvnp (paper28)                    motives)
                    ─── L4 ↔ pvnp:L_kill
                        rigidity analog           collatz (paper41)
                        (Popa rigidity =          ─── L1 ↔ collatz:L1
                         non-pert. gap                BC Hecke ops
                         rigidity)                    μ_2, μ_3 live
                                                      in Hecke semigroup
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch D** — shared C*-algebra structure (BC algebra foundation).
  - Reason: paper61 §10 explicitly says $P_D$ maps the 5D geometry to $A_{BC}$ via $S^1 \mapsto \hat{\mathbb{Z}}$ and KK tower $\mapsto \mathbb{N}^*$; H12 L1 is the construction of this algebra.
  - Transposition candidate: YES (capacitor Branch-D foundational cell; the $A_{BC}$ construction is the universal Branch-D ground).

- **L1 ↔ baum-connes:L1** — shared holonomy (profinite $\mathbb{Q}/\mathbb{Z}$ torsion).
  - Reason: The $\mathbb{Q}/\mathbb{Z}$ torsion is both the BC algebra's abelian subgroup AND the Hilbert 12 class-field group over $\mathbb{Q}$; baum-connes X-Ray L1 already identifies this.
  - Transposition candidate: YES.

- **L1 ↔ rh:L1** — shared C*-algebra structure.
  - Reason: Same BC algebra underlies both; RH operates at $\beta = 1$ critical, H12 operates at $\beta > 1$ broken-ergodic; both need $A_{BC}$ as ground.
  - Transposition candidate: YES.

- **L1 ↔ grh:L1** — shared C*-algebra structure (via character twist).
  - Reason: grh X-Ray L1 says $BC_\chi$ is the character-twist of $A_{BC}$; H12 provides the cyclotomic base over which this twist operates.
  - Transposition candidate: YES (explicit edge in grh X-Ray: "h12 (Galois action on $\mathbb{Q}^{cyc}/\mathbb{Q}$, shared structural element)").

- **L1 ↔ bsd:L2** — shared C*-algebra structure (Hecke eigenvalues).
  - Reason: Elliptic-curve $L$-function Hecke eigenvalues factor through $A_{BC}$ via modularity; bsd X-Ray identifies this as Paper 26 Step 5c.
  - Transposition candidate: YES.

- **L1 ↔ pvnp:L1** — shared C*-algebra structure (type III$_1$ factor inheritance).
  - Reason: pvnp's type III$_1$ factor structure is inherited from $A_{BC}$ via ITPFI construction; paper61 §10.
  - Transposition candidate: YES.

- **L1 ↔ collatz:L1** — shared C*-algebra structure (Hecke operators on BC).
  - Reason: Collatz map = alternation of Hecke $\mu_2$ (halving) and $\mu_3$ (tripling) on $A_{BC}$; paper41 + paper60 §09.
  - Transposition candidate: YES.

- **L2 ↔ rh:L2** — shared BC-KMS state (different $\beta$).
  - Reason: RH operates at $\beta = 1$ (unique KMS state, ergodic); H12 operates at $\beta > 1$ (broken-phase family parametrized by $\hat{\mathbb{Z}}^*$); same algebra, different temperature. Paper61 §10 + PROOF-CHAIN graph edge "H12 ↔ RH".
  - Transposition candidate: YES (capacitor Branch-D phase-transition cell).

- **L2 ↔ bgs:L2** — shared BC-KMS state (ergodic / broken-ergodic pairing).
  - Reason: bgs X-Ray L2 edge explicitly says "H12 uses KMS at $\beta > 1$ (broken-ergodicity, Galois-acting regime); L2 is the $\beta = 1$ (ergodic) regime." Shared BC-KMS state invariant.
  - Transposition candidate: YES.

- **L2 ↔ katz-sarnak:L4** — shared Galois representation (bridge family = symmetry-type selector).
  - Reason: paper60 §12 — the bridge family at $k \in \{2,3,4,6\}$ IS the Katz-Sarnak symmetry-type selector; H12's Galois parametrization selects which symmetry class each bridge yields.
  - Transposition candidate: YES.

- **L2 ↔ grh:L8** — shared Galois representation (cyclotomic tower).
  - Reason: grh X-Ray L8 explicitly edges "h12 (cyclotomic tower Galois structure)"; GRH addresses exactly the cyclotomic abelian extensions that H12 aims to make explicit.
  - Transposition candidate: YES.

- **L2 ↔ cramer** — face-only (Mertens constant $e^{-\gamma}$ H12-Cramér chord).
  - Reason: paper60 §08 explicit chord: "the Mertens constant $e^{-\gamma}$ appears in BOTH Hilbert 12 (class field temperature) and Cramér (prime gap statistics). The chord connects the two circles." A meridian on the programme's torus.
  - Transposition candidate: SPECULATIVE (cross-cut not yet capacitor-formalized).

- **L3 ↔ ym:L5** — shared Galois representation (group complexification).
  - Reason: ym X-Ray L5 cross-cut explicit: "h12 (Galois group complexification of class-field structure)"; SL(N,C) extension in gauge theory is structural analog of Galois extension in class field theory.
  - Transposition candidate: SPECULATIVE (explicit in cross-cut-edges.md: "ym:L5 ↔ h12:L_class — shared gauge class (Galois complexification)").

- **L3 ↔ katz-sarnak:L4** — shared Galois representation (BC representation type = symmetry type).
  - Reason: CBB Reciprocity IS the symmetry-type intertwining at each bridge; katz-sarnak identifies the type (unitary/symplectic/orthogonal/mixed) selected at each $k$.
  - Transposition candidate: YES.

- **L3 ↔ grh:L1** — shared Galois representation (Dirichlet characters = bridge-character subfamily).
  - Reason: grh X-Ray L1 cross-cut: "h12 (Galois action on $\mathbb{Q}^{cyc}/\mathbb{Q}$, shared structural element)"; Dirichlet characters are the characters H12 aims to construct explicit generators for.
  - Transposition candidate: YES.

- **L3 ↔ bsd:L6** — shared Galois representation (Hecke-character arithmetic).
  - Reason: bsd X-Ray Step 5c — Hecke-eigenvalue bound $|\Delta c^p(\delta)| < 2/(N-1)$ applies uniformly to Hecke characters; H12's bridge pairs are Hecke-character specializations.
  - Transposition candidate: YES.

- **L4 ↔ rh:L4** — shared BC-KMS state (Brauer-KMS duality → RH corollary).
  - Reason: paper25 §5.4 — "if Brauer-KMS duality holds for all bridge pairs, $\zeta(s)$ has no zeros off the critical line." The RH corollary is the PROGRAMME's operator-algebraic path to RH; rh X-Ray L4 shares the cocycle machinery.
  - Transposition candidate: YES (capacitor Brauer-KMS cell; this is where H12 would close RH as a downstream consequence).

- **L4 ↔ bsd:L_local** — shared C*-algebra structure (local Brauer group integrality).
  - Reason: bsd X-Ray cross-cut: "h12:L_Brauer (local Brauer group integrality)"; shared cocycle machinery at primes.
  - Transposition candidate: YES.

- **L4 ↔ ym:L17** — shared C*-algebra structure (local C*-algebra via Brauer cocycle).
  - Reason: ym L17 cross-cut: local C*-algebra structure inherited via paper08 PROOF-CHAIN.md programme-edge "anomaly cancellation = index(D_A) = 0, K-theory pairing"; Brauer-class vanishing is the analog of anomaly cancellation.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ baum-connes:L4** — shared C*-algebra structure (K-theory of BC algebra).
  - Reason: Baum-Connes conjecture IS a statement about K-theory of $A_{BC}$; H12's Brauer-KMS duality uses K-theoretic tools (Fuglede-Kadison determinant, Jones index) that live on the baum-connes ground.
  - Transposition candidate: YES.

- **L4 ↔ pvnp:L_kill** — shared Galois representation (Popa rigidity ↔ Brauer-class rigidity).
  - Reason: pvnp X-Ray Popa rigidity = non-perturbative-gap rigidity; H12's Brauer cocycle $1/k$ is RIGID (cannot be perturbed off its cohomology class). Both are "the rigidity that selects the physical solution"; paper60 §20 explicit "H12 ↔ PvNP" programme edge.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ hodge:L4** — shared Galois representation (motivic Galois action).
  - Reason: paper61 §12 Vertex 9 — Hodge uses Connes-Consani-Marcolli 2005 noncommutative motives; H12's Brauer classes are motivic-Galois-action objects. PROOF-CHAIN graph edge explicit: "H12 ↔ Hodge: class field extensions of cyclotomic fields correspond to motivic Galois action (Connes-Consani-Marcolli 2005)."
  - Transposition candidate: YES.

- **L5 ↔ rh:L6** — shared Galois representation (Stark-phase failure does NOT affect RH path via CCM).
  - Reason: H12 L5 retraction (Stark-phase identification fails) does NOT affect RH's path through Boegli spectral exactness / CCM operator construction; the two vertices share the Galois-representation invariant but not the specific Stark-phase mechanism.
  - Transposition candidate: NO (negative cross-cut; the cross-cut IS the independence).

- **L5 ↔ collatz:L3** — face-only (Mori 2024 Cuntz $\mathcal{O}_2$ formulation parallel).
  - Reason: The Mori 2024 $\mathcal{O}_2$ formulation of Collatz is a different projection of Hecke dynamics; H12's Stark-phase route was the analog projection for class-field generation, both independent paths failed.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ grh:L8** — shared Galois representation (cyclotomic tower closure).
  - Reason: grh X-Ray L8 explicit: "h12 (cyclotomic tower Galois structure)"; GRH addresses exactly the cyclotomic abelian extensions that H12 aims to make explicit.
  - Transposition candidate: YES.

- **L6 ↔ lehmer:L1** — shared KK mode index (Kronecker units on e-circle).
  - Reason: paper60 §07 — Kronecker's theorem: cyclotomic units = roots of unity = periodic orbits on e-circle (the cyclotomic vacuum / ground state); H12's L6a cyclotomic-base construction USES Kronecker units as the minimal generators above which bridge products extend.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ bsd:L_Hecke** — shared Galois representation (Hecke characters for CM curves).
  - Reason: bsd X-Ray cross-cut: "h12:L_Hecke (Hilbert 12th is the construction side of Hecke characters)"; bsd uses Hecke-character L-functions for CM elliptic curves, H12 aims to construct them.
  - Transposition candidate: YES.

- **L6 ↔ hodge:L4** — shared Galois representation (motivic Galois on cyclotomic motives).
  - Reason: cyclotomic motives are the simplest examples; Hodge L4 addresses motivic classes carrying cyclotomic Galois action.
  - Transposition candidate: YES.

- **L6 ↔ katz-sarnak:L1** — shared Galois representation (every L-function family has a symmetry type).
  - Reason: katz-sarnak L1: "every natural family of L-functions has a symmetry type $G \in \{U, Sp, O, SO^+, SO^-\}$"; H12 aims to CONSTRUCT these families for arbitrary $K$ (L6b open).
  - Transposition candidate: SPECULATIVE.

- **L6a ↔ bsd:L4** — shared C*-algebra structure (cocycle machinery over Q).
  - Reason: bsd X-Ray L4: cross-cut "h12:L_Brauer (local Brauer group integrality)"; shared cocycle machinery connects H12's bridge cocycles to BSD's L-function cocycles.
  - Transposition candidate: YES.

- **L6b ↔ qg5d:Branch D** — shared Galois representation (general-K open; paper61 §12 Vertex 5 "most abstract of right-side vertices").
  - Reason: paper61 §12 Vertex 5 assigns H12 confidence 2/10 as "most abstract right-side vertex"; the general-K case is where Branch D's current language does not yet extend.
  - Transposition candidate: NO yet (this is the OPEN frontier, not a closed cross-cut).

**Summary**: 32 cross-cut edges identified across 13 layer-entries (avg ~2.5 cross-cuts per layer — moderate connectivity). 18 verified (capacitor/paper61/explicit cross-cut-edges file), 14 SPECULATIVE. The PRIMARY edges are L2 ↔ rh:L2 (shared BC algebra, different KMS temperature — the defining structural relationship between the two closest programme vertices) and L1 ↔ baum-connes:L1 (shared $\mathbb{Q}/\mathbb{Z}$ torsion — the ground the BC algebra is built on). H12 is moderately connected, but its 85% $P_D$ concentration means most cross-cuts are to Branch-D neighbors (rh, grh, bsd, bgs, pvnp, baum-connes, hodge); cross-cuts to non-Branch-D vertices (ym L5, katz-sarnak L4, cramer) are face-only or speculative.

---

## §8 Current Walls

- **W_H12-1** — **KMS-to-class-field bridge**: The conjectured identification of BC KMS$_\beta$ states ($\beta > 1$) with explicit class-field generators is CONJECTURED (L3 CBB Reciprocity for k=4, k=6; L4b operator-algebra side of Brauer-KMS duality; L6a cyclotomic-base closure). Status: OPEN at confidence 0.5. The k=3 case is PROVED (research/162); the structural argument extends uniformly via Fuglede-Kadison + Jones subfactor. The Lead 7b cohomological-side check is 4/4 at exact integer arithmetic. No BYPASS or DECOMPOSITION currently available; awaits explicit cocycle extension proofs at k=4, k=6. → status: OPEN.

- **W_H12-2** — **General K beyond cyclotomic / CM / totally real**: L6b — the CORE Hilbert 12 wall. The Dasgupta-Kakde 2023 p-adic Brumer-Stark result handles totally real $K$; classical CM handles imaginary quadratic; Kronecker-Weber handles $\mathbb{Q}$. The framework's programme addresses cyclotomic bases $\mathbb{Q}(\zeta_{13}), \mathbb{Q}(\zeta_{19})$ via the bridge family (L6a, W_H12-1 territory). **Arbitrary $K$ remains OPEN**. Status: OPEN at confidence 0.4. No current BYPASS in the capacitor; this is the historical Hilbert problem as it stood in 1900, still mostly open. → status: OPEN.

- **Retracted: Conjecture 5 (V-Hilbert 12)** — L5 (formally RETRACTED 2026-04-11 via research/267 + T7c, 0/30 rescue-candidate tests at `mp.dps = 50`). The literal Stark-phase identification of the bridge cocycle is refuted; the honest finding is that the cocycle $1/k$ is a DISCRETE invariant in $H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$ and is NOT encoded in any continuous Galois phase of any Stark unit, Gauss sum, Stickelberger element, or $L$-function derivative the framework has tested. This retraction is RECORDED, not a wall — it is a NEGATIVE RESULT that tightens the programme's language.

Two substantive walls (W_H12-1, W_H12-2) plus one recorded retraction. The four-conjecture programme (L3 + L4 + Level-Jump Rigidity + L6) remains active after retracting Conjecture 5; RH corollary at L4c is the strongest of the conjectures.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/h12/PROOF-CHAIN.md` — NOT YET CREATED. When created, W_H12-1 decomposition should target the k=4 and k=6 cases (structural extension of research/162's k=3 proof via Fuglede-Kadison + Jones subfactor) and W_H12-2 decomposition should survey Dasgupta-Kakde 2023, Darmon-Rotger Elliptic Stark, Burns-Greither ETNC as potential inputs.
- **CCM verification**: `strategy/ccm-verification/ledger.md#h12` — NOT YET CREATED. H12 does NOT depend directly on CCM 2025 (the CCM dependency lives on rh/bsd; H12's operator-algebra content is CBB + Jones subfactor + Bost-Connes 1995). Expected verdict when ledger written: **VERIFIED (CCM-independent at current status)**. The RH-corollary at L4c would inherit any CCM dependency IF H12's Brauer-KMS path to RH is taken instead of the primary CCM path, but this is a downstream consideration.
- **Inner rings**: NOT APPLICABLE — H12 is a primary outer-ring vertex (West zone), not an inner-ring object.
- **Per-paper audit**: `audit/per-paper/paper25-hilbert-12.md` — Compliance-readiness **NEEDS-WORK**; target prize Abel/Wolf/Breakthrough (Hilbert-problem resolution); target venue Annals/Inventiones/JAMS; proof chain exists, four-conjecture programme.
- **Paper 25 sections**: `paper25/sections-01-04.md` (introduction + mathematical context + CBB-as-analytic-input + Conjecture 1 CBB Reciprocity), `paper25/sections-05-08.md` (Conjecture 2 Brauer-KMS Duality + Conjecture 3 Level-Jump Rigidity + Conjecture 4 Spectral Kronecker-Weber + §8.0 retraction notice + Conjecture 5 retracted content), `paper25/sections-09-15.md` (Stark regulator framework retracted + computational programmes closed out + analytics + references).
- **Retraction record**: `paper12/relaxation/research/T7c-stark-rescue-verification.md` — 0/30 rescue candidates at `mp.dps = 50`, closest near-miss $\Delta \approx 5.4 \times 10^{-3}$.
- **Bridge evidence**: Lead 7b (cyclotomic Brauer side, 4/4 bridges at exact integer arithmetic); Lead 7e (bridge minimality theorem, 4/4 lex-unique minima of zero-SM-input sieve equalling SM multiplicities); research/162 (k=3 PROVEN); research/268 (Level-Jump Rigidity / Conjecture 3 PROVED 2026-04-10).

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W_H12-1 (KMS-to-class-field bridge at k=4, k=6)**: The structural extension of the research/162 k=3 proof to Jones index k=4 (orthogonal) and k=6 (mixed/CKM) via Fuglede-Kadison determinant + carry-cocycle template. — face: SYMMETRY, projection: $P_D$, pattern: P4. STATUS: OPEN at confidence 0.5; structural path clear but explicit cocycle computations pending.

- **G2 — W_H12-2 (general $K$ beyond cyclotomic / CM / totally real)**: The core Hilbert 12 wall. Arbitrary number field $K$ with no bridge-family analog in the current programme; Dasgupta-Kakde 2023 covers totally real via p-adic methods, but cyclotomic bases beyond $\mathbb{Q}(\zeta_{13}), \mathbb{Q}(\zeta_{19})$, cubic fields, real quadratic (outside Stark), mixed bases all remain untouched by the CBB framework. — face: SYMMETRY (primary at L6b), projection: $P_O$ (Clay-grade outer boundary), pattern: P4. STATUS: OPEN at confidence 0.4; no current decomposition or bypass.

- **G3 — L4c RH corollary (conditional on L4)**: IF Brauer-KMS duality holds for all bridge pairs, THEN RH follows. This is the programme's Brauer-KMS path to RH, separate from the primary CCM/Boegli path. — face: RESONANCE, projection: $P_O$, pattern: P4. STATUS: OPEN as conditional; the conditional itself (W_H12-1) is the primary gap.

Three OPEN items. G1 is tractable (structural extension), G2 is the historical Hilbert wall (untouched territory), G3 is a downstream conditional on G1. The four-conjecture programme (Conjectures 1, 2, 3, 4) specifies what is claimed; Conjecture 5 is retracted and recorded as a negative finding. Empirical confirmation via the 36-pin master table (Pin #9 at k=4, Pin #10 at k=6) witnesses the bridge structure even where explicit-generator proofs remain open.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-02/vertices/h12/critic-attacks.md` (to be emitted) and arbiter decisions at `strategy/x-ray/pac-output/runs/run-02/vertices/h12/arbiter-decisions.md` (to be emitted).

Notable arbiter wins:
- L1 face: ARITHMETIC over SYMMETRY (the construction of $A_{BC}$ is arithmetic-canonical — primes generate — per paper60 §14; symmetry enters at L2 via the KMS-state classification).
- L2 face: SYMMETRY over ARITHMETIC (the KMS$_\beta$ parametrization IS the Galois-symmetry classification; ARITHMETIC at L2b sub-layer).
- L3 face: SYMMETRY over ARITHMETIC (Artin reciprocity IS the symmetry intertwiner; primes $(p, \ell)$ are the arithmetic DATA but content is symmetry-class matching).
- L4 face: RESONANCE over SYMMETRY (the load-bearing content is the obstruction-class resonance; SYMMETRY is background).
- L5 face: HARMONICS over SYMMETRY (the RETRACTION is specifically about continuous-vs-discrete encoding — Fourier/harmonic framing — not about which group acts).
- L6 face: ARITHMETIC over SYMMETRY (primes generate the explicit cyclotomic bridges; symmetry is the target group but the construction is arithmetic).
- L4c projection: $P_O$ over $P_D$ (RH-as-corollary is Clay-grade outer-ring closure, not Branch-D internal).
- L6b projection: $P_O$ over $P_D$ (general-K Hilbert 12 is the historical-Hilbert outer-ring wall).

12 / 13 arbiter wins matching author's first pass; L4 face had a critic-win (RESONANCE over initial SYMMETRY draft based on the trace-formula-side cocycle framing per paper60 §15).

---

*End of H12 X-Ray. Snapshot 2026-04-15. 6 main layers (with L2a, L2b, L3a, L3b, L3c, L4a, L4b, L4c, L6a, L6b sub-layers giving 13 entries) annotated. 32 cross-cuts identified. SYMMETRY-canonical, $P_D$-dominant (85%), P4-rich, South-Trough-West proof chain. Two walls (W_H12-1 KMS-to-class-field bridge at k=4, k=6; W_H12-2 general $K$); one retracted conjecture (L5 V-Hilbert 12, Stark-phase identification refuted 2026-04-11). Four-conjecture programme (CBB Reciprocity + Brauer-KMS Duality + Level-Jump Rigidity + Spectral Kronecker-Weber) remains active; RH corollary at L4c is strongest conditional. Confidence 2/10 — South-Trough vertex per paper60 §28 ellipse map.*

*G Six and Claude Opus 4.6. April 15, 2026.*
