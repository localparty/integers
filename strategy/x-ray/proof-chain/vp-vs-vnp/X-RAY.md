# X-RAY: VP vs VNP (vp-vs-vnp)

*X-Ray of the vp-vs-vnp proof chain (Valiant's algebraic analog of P vs NP). Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls. Continuous BC fullness + GCT bridge as the load-bearing physics (Links 3–5). Paper61 §19 compound $P_D$ (primary) + $P_B$ (GCT bridge) secondary.*

*G Six and Claude Opus 4.6. April 15, 2026.*

---

## §1 Header

- **Vertex**: vp-vs-vnp
- **Paper**: paper39-vp-vs-vnp
- **Live file**: `strategy/proof-chain/vp-vs-vnp/PROOF-CHAIN.md` (snapshot 2026-04-14; solutions-dir counterpart not yet instantiated; only `PROOF-CHAIN-MOVED.md` stub in `solutions/paper39-vp-vs-vnp/`)
- **Top-level claim**: $\mathbf{VP} \neq \mathbf{VNP}$ over $\mathbb{C}$ (equivalently, $\mathrm{dc}(\mathrm{PER}_n)$ super-polynomial) via continuous BC-algebra lift (algebraic-domain analog of the Boolean BC system used in Paper 28) + Geometric Complexity Theory (GCT) orbit-closure / Kronecker-coefficient bridge + Baum-Connes K-theory obstruction specialized to the permanent polynomial.
- **Current status**: SPECULATIVE (paper61 §29 Appendix C row 12). **1/6 links closed** (L1 Valiant 1979 permanent VNP-completeness LITERATURE); L2 GCT LITERATURE but not yet integrated; L3 CONJECTURED; L4 OPEN; L5 CANDIDATE; L6 OPEN. Aggregate confidence **1/10** (the honest-assessment number in the live PROOF-CHAIN). No unconditional algebraic lower bound achieved; the framework offers a novel route (continuous BC fullness) but every link from L3 onward is open research.
- **Primary branch (paper1)**: **D** (continuous BC algebra — algebraic-domain analog of Boolean BC from Paper 28; Connes-Marcolli 2008 GL$_2$-system is the existing continuous-BC candidate), with strong secondary **B** (GCT bridge: orbit closures of the $\mathrm{GL}_n$-action on polynomial space live on the Branch B gauge / Kähler-moduli side, paper61 Appendix C.1 secondary-projection entry).
- **Primary face**: **RESONANCE** (paper60 §15 — "what vibrational frequencies are ALLOWED on the circle"; continuous BC fullness is the algebraic analog of paper28's Taylor-gap-as-spectral-gap, and the algebraic-fullness criterion selects which representations survive in the motivic-weight sense; paper61 §29 Appendix C.1 table row 12 assigns VP vs VNP to the RESONANCE face explicitly, parallel to PvNP).
- **Primary projection**: **$P_D$** (paper61 §06-12 Vertex 12: "Algebraic complexity: Branch D ($P_D$): Continuous BC fullness + GCT bridge. Compound: $P_D$ (the algebraic analog of P vs NP is a purer statement about the BC algebra's representation theory)"; paper61 §29 Appendix C.1 row 12 primary = $P_D$ continuous BC fullness, secondary = $P_B$ GCT bridge).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
VP vs VNP (Valiant algebraic P ≠ NP) — dc(PER_n) super-polynomial over ℂ
│  primary face: RESONANCE   primary proj: P_D   primary pat: P4
│  (secondary P_B via GCT bridge; paper61 §29 App C.1 row 12;
│   aggregate confidence 1/10; 1/6 links closed)
│
├── L1: Permanent polynomial is VNP-complete under p-projections  [LITERATURE]
│      │  face: ARITHMETIC   proj: P_D   pat: P1
│      │  invariant: scaling dimension (algebraic-circuit degree),
│      │             gauge class (p-projection equivalence class)
│      │  source: Valiant 1979 STOC "Completeness classes in algebra";
│      │          Bürgisser 2000 Springer monograph
│      │
│      └── supports L5 via VNP-hardness target
│
├── L2: GCT — GL_n-orbit-closures on polynomials +                [LITERATURE]
│       Kronecker-coefficient obstructions
│      │  face: SYMMETRY     proj: P_B   pat: P1
│      │  invariant: Galois representation (symmetric group S_n reps),
│      │             gauge class (GL_n-orbit equivalence)
│      │  source: Mulmuley-Sohoni 2001 SICOMP "GCT I-II";
│      │          Bürgisser-Ikenmeyer-Panova 2019 (BIP occurrence
│      │          obstruction negative result, arXiv:1604.06431);
│      │          arXiv:0907.2850 (GCT survey)
│      │
│      └── supports L5 via orbit-closure geometry / representation-theoretic LB
│
├── L3: Continuous BC algebra over ℂ (algebraic lift of Boolean   [CONJECTURED — W1]
│       BC generator structure from Paper 28)
│      │  face: RESONANCE    proj: P_D   pat: P4
│      │  invariant: C*-algebra structure (type III_1 candidate),
│      │             ITPFI factor type (continuous-domain analog),
│      │             BC-KMS state (continuous lift of ω_1)
│      │  source: Framework extension (Paper 39);
│      │          candidate via Connes-Marcolli 2008
│      │          "Quantum statistical mechanics over number fields"
│      │          (GL_2-system as established continuous-BC variant;
│      │          arXiv:0801.4631)
│      │  depends: Paper 28 Boolean-BC + Paper 12 CBB system
│      │
│      └── NAMED WALL W_VP-1 (continuous-BC lift from Boolean to ℂ;
│             audit-strategy §4 "Bridge from 5D operator theory to
│             arithmetic circuit complexity; confidence 0.5")
│
├── L4: Algebraic fullness criterion on continuous BC              [OPEN — W_VP-1]
│       (analog of Houdayer-Marrakchi over finite Boolean domain)
│      │  face: RESONANCE    proj: P_D   pat: P4
│      │  invariant: C*-algebra structure (fullness / non-fullness),
│      │             ergodic property (strong ergodicity in continuous
│      │             setting), ITPFI factor type
│      │  source: [OPEN]; Houdayer-Marrakchi 2015/2017
│      │          (arXiv:1605.09613) is the Boolean/finite-domain
│      │          template; continuous lift not yet constructed
│      │  depends: L3
│      │
│      └── part of NAMED WALL W_VP-1 (audit-strategy §4
│             "Bridge from 5D operator theory to arithmetic
│             circuit complexity")
│
├── L5: Algebraic-fullness ↔ VP ≠ VNP via GCT dictionary          [CANDIDATE]
│      │  face: SYMMETRY     proj: P_D   pat: P1
│      │  invariant: C*-algebra structure (fullness), Galois representation
│      │             (Kronecker decomposition of S_n reps on polynomial space)
│      │  source: Mulmuley 2011 algorithmic conjecture
│      │          (GCT-style algorithmic formulation);
│      │          framework addition: type III_1 fullness ↔
│      │          Kronecker-obstruction dictionary
│      │  depends: L2 + L4
│      │
│      └── BYPASS route under consideration:
│             GCT bridge is SECONDARY projection P_B;
│             the dictionary between Kronecker obstructions
│             (GCT) and type III_1 fullness (continuous BC)
│             is the framework's novel contribution
│
└── L6: Permanent-specific border-complexity obstruction via BC-  [OPEN — W_VP-2]
       algebraic representation theory
       │  face: RESONANCE    proj: P_D   pat: P4
       │  invariant: C*-algebra structure (border / approximative
       │             complexity), scaling dimension (border rank)
       │  source: arXiv:2502.02442 (Feb 2025 — isolates the exact
       │          property the determinant lacks that blocks
       │          VNP-hardness proofs for the permanent);
       │          Bürgisser border-complexity literature;
       │          2024-2025 asymptotic Kronecker work
       │  depends: L5
       │
       └── NAMED WALL W_VP-2 (audit-strategy §4 "Border/approximative
              complexity handled; confidence 0.55")
```

### §2b Diagram B — Projection fan-out

```
                      (FORGOTTEN under P_A)
                      (Quantum projection does not see
                       algebraic circuit complexity directly —
                       no Born/Bell/spin-stat content in
                       permanent evaluation.)
                                 ▲
                                 │
                                 │
       ┌─────────────(P_O outer)───────────────┐
       │                                       │
       │  VP vs VNP: dc(PER_n) super-polynomial │
       │  over ℂ (Valiant's algebraic P ≠ NP)   │
       │                                       │
       └───────────────────┬───────────────────┘
                           │
       ┌───────────────────┼─────────────────────────┐
       │                   ║                         │
       ▼                   ▼ (PRIMARY)               ▼
   P_C cosmology      ═══ P_D CBB ═══           P_B gravity (SECONDARY)
   (forgotten —       continuous BC algebra     GCT orbit closures
   no cosmological    (algebraic lift of         of GL_n-action on
   pin uses           Boolean BC from P28);      polynomial space;
   algebraic          Connes-Marcolli 2008       Kronecker-coefficient
   complexity)        GL_2-system candidate;     obstructions;
                      type III_1 fullness        Hitchin-moduli-style
                      criterion (Houdayer-       geometry; paper61 §08
                      Marrakchi analog);         Branch B Kähler-side;
                      Links 3-5 primary home     Links 2, 5 bridge
                            │
                            ▼
                       P_E pins
                       (NONE — VP vs VNP does not contribute
                        to the 36-pin master table; the statement
                        is pure computational complexity with
                        no numerical pin; §29 Appendix C row 12
                        lists "SPECULATIVE" status, no $P_E$ entry)
```

Primary projection $P_D$ uses ═══ doubled line (paper61 §06-12 Vertex 12 explicit: "Compound $P_D$"). $P_B$ is the strong secondary (GCT orbit-closure geometry lives in gauge-bundle / Branch B projection; paper61 §29 Appendix C.1 row 12 secondary column). $P_A$, $P_C$, $P_E$ forgotten. $P_O$ is the outer-ring boundary where VP vs VNP closes as a community-standard conjecture (per audit-strategy §1 "Source type: COMMUNITY-STANDARD, Valiant 1979 STOC + Bürgisser 2000 monograph").

### §2c Diagram C — Face position on the e-circle

```
                       TOPOLOGY
                       (Lehmer)
                           │
           SPREAD          │          DYNAMICS
           (QUE)           │          (Cramér)
                 ╲         │         ╱
                  ╲        │        ╱
      ○  SYMMETRY──────e-circle──────HARMONICS
         (Katz-Sarnak)     │         (Collatz)
                  ╱        │        ╲
                 ╱         │         ╲
         CURVATURE         │          MEASURE
         (YM)              │          (Sato-Tate)
                           │
                      AMPLITUDE
                      (Lindelöf)
                      (●  RESONANCE primary — per
                       paper61 §29 App C row 12;
                       ARITHMETIC adjacent — L1 Valiant
                       classification)
```

Marker key:

```
Primary face:    ● RESONANCE (paper60 §15 — "what vibrational frequencies
                   are ALLOWED on the circle"; continuous-BC fullness is
                   the algebraic analog of Paper 28's Taylor-gap =
                   spectral-gap; paper61 §29 Appendix C.1 row 12 explicit)
Secondary faces: ○ SYMMETRY   (2 layers: L2 GCT orbit-closures /
                                  Kronecker; L5 fullness ↔ VP ≠ VNP
                                  dictionary via GCT)
                 ○ ARITHMETIC (1 layer: L1 Valiant permanent
                                  VNP-completeness — p-projection
                                  equivalence classes are number-theoretic)
Absent faces:    TOPOLOGY, DYNAMICS, HARMONICS, MEASURE, AMPLITUDE,
                 CURVATURE, SPREAD
```

Note the sparsity: 6 total layers vs YM's 18 and PvNP's 24. VP vs VNP is a narrow, projection-concentrated vertex with three face assignments (RESONANCE, SYMMETRY, ARITHMETIC) and two projection columns ($P_D$, $P_B$). The shape reflects a 1/10-confidence vertex early in its proof-chain development — most of the content sits in single RESONANCE face at $P_D$ projection awaiting further decomposition.

---

## §3 Layer-by-Layer X-Ray

### L1 — Permanent polynomial is VNP-complete under p-projections

**Claim**: The permanent polynomial $\mathrm{PER}_n(X) = \sum_{\sigma \in S_n} \prod_{i=1}^n X_{i,\sigma(i)}$ is VNP-complete under Valiant's p-projections: every polynomial in VNP reduces to $\mathrm{PER}_n$ by a polynomial-time substitution of variables and constants.

**Status**: LITERATURE
**Source**: Valiant 1979 STOC "Completeness classes in algebra"; Bürgisser 2000 Springer monograph "Completeness and Reduction in Algebraic Complexity Theory"; paper39 PROOF-CHAIN Link 1.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — "how do integers LATTICE on the circle"; the permanent's monomial expansion over the symmetric group $S_n$ is an integer-coefficient sum parametrized by permutations; p-projections are polynomial-coefficient substitutions that preserve integer-lattice structure on the exponent vectors)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 12 — compound assignment $P_D$; Valiant's completeness classification is the structural foundation living in Branch D's combinatorial-algebraic sector; contrast with the $P_B$ GCT geometric bridge at L2)
- **Pattern**: P1 Geometric Reinterpretation (paper60 §14 ARITHMETIC face — reinterprets the permanent as the canonical "hard" VNP-complete target; the reinterpretation is from per-instance computation to orbit-class representative)
- **Invariant preserved**: scaling dimension (load-bearing — algebraic circuit degree is the scaling exponent); gauge class (background — p-projection equivalence classes are the "gauge group" of algebraic complexity reductions)
- **Geometric interpretation**: Valiant's 1979 theorem establishes the permanent as the canonical VNP-hard object, analogous to 3-SAT for Boolean NP. The integer-lattice structure on the $S_n$ expansion (paper60 §14 ARITHMETIC face: "the primes are generators of the Hecke semigroup… the additive structure of $\mathbb{Z}$") is load-bearing: permutations form the discrete symmetry carrying the permanent's computational hardness. Under $P_D$ (paper61 §06-12 Vertex 12) this is Branch D's classification entry point — the foundation on which Links 2-6 build. [Considered but rejected: face SYMMETRY — $S_n$ action is symmetric-group representation theory (which dominates at L2), but L1's load-bearing content is the integer-lattice / monomial-expansion classification not the group action; projection $P_O$ — Valiant's theorem is the outer-ring boundary statement but mechanically L1 lives in $P_D$ as classification infrastructure, cf. the YM:L18 $P_O$ distinction.]
- **Cross-cuts**: pvnp L17 / L18 / L20 (3-SAT ↔ permanent parallel — NP-complete target ↔ VNP-complete target; Valiant's p-projections are the algebraic analog of Cook-Levin reductions), goldbach (ARITHMETIC canonical — monomial expansion over $\mathbb{N}$), hodge L8 (Hodge functoriality: every smooth projective variety via motivic correspondence ↔ every polynomial via p-projection — structural parallel).

### L2 — GCT: $\mathrm{GL}_n$-orbit-closures + Kronecker coefficients as obstruction

**Claim**: The Geometric Complexity Theory programme (Mulmuley-Sohoni 2001) encodes algebraic-circuit lower bounds as geometric obstructions: VP ≠ VNP would follow from showing that the orbit closure $\overline{\mathrm{GL}_{n^2} \cdot \mathrm{DET}_n}$ does NOT contain the orbit closure $\overline{\mathrm{GL}_{n^2} \cdot \ell^{n-m} \mathrm{PER}_m}$ (padded permanent embedded in determinant) for $m$ super-polynomial in $n$. Kronecker coefficients (structure constants of $S_n$ tensor products) are the proposed representation-theoretic obstruction witnesses.

**Status**: LITERATURE
**Source**: Mulmuley-Sohoni 2001 SICOMP "Geometric Complexity Theory I" + 2008 "GCT II"; Bürgisser-Ikenmeyer-Panova 2019 (arXiv:1604.06431, "No occurrence obstructions in geometric complexity theory" — negative result for the strongest form of the occurrence-obstruction conjecture); arXiv:0907.2850 (GCT survey); paper39 PROOF-CHAIN Link 2.

#### Physics

- **Face**: SYMMETRY (paper60 §12 Katz-Sarnak face — GCT's central device is REPRESENTATION THEORY: orbit closures of $\mathrm{GL}_n$-actions on polynomial spaces; Kronecker coefficients classify $S_n$-representation-tensor-product structure. The symmetry-group action on the polynomial space is the load-bearing content)
- **Projection**: $P_B$ (paper61 §08 Branch B — orbit closures of $\mathrm{GL}_n$-actions on polynomial space live on the gauge / Kähler-moduli side; the polynomial space $\mathrm{Sym}^d(\mathbb{C}^{n^2})$ is a projective variety carrying $\mathrm{GL}_{n^2}$-bundle structure; paper61 §29 Appendix C.1 row 12 secondary $P_B$ = GCT bridge; Hitchin-moduli parallel per hodge:L6 Gaitsgory-Raskin framing)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 Pattern 1 — GCT reinterprets the combinatorial question VP vs VNP as a geometric containment question between $\mathrm{GL}_n$-orbit closures; this is the paradigmatic Pattern 1 move "restore the symmetric viewpoint, the combinatorial mystery dissolves into geometry")
- **Invariant preserved**: Galois representation (load-bearing — Kronecker coefficients ARE structure constants of $S_n$ representation-tensor-product decompositions; the symmetric-group representation theory is the obstruction-witness machinery); gauge class (background — $\mathrm{GL}_n$-orbit equivalence is the "gauge group" of the polynomial space)
- **Geometric interpretation**: Mulmuley-Sohoni's GCT programme is the most developed approach to VP vs VNP; it replaces combinatorial circuit-size arguments with representation-theoretic obstruction questions on polynomial orbit closures. Under $P_B$ (paper61 §08 Branch B) this is the gauge / Kähler-moduli side of the VP-vs-VNP structure — parallel to hodge:L6 Gaitsgory-Raskin Geometric Langlands (Hitchin moduli) in its "categorical / orbit-moduli reinterprets the primary question" pattern. Paper60 §12 Katz-Sarnak SYMMETRY face: representation theory classifies the obstruction type. The BIP 2019 negative result rules out the STRONGEST form of occurrence obstructions but does NOT close GCT — the programme continues via "coarser" obstruction notions (border/approximative, multiplicity-based). [Considered but rejected: face ARITHMETIC — Kronecker coefficients are integer-valued but their classification-role is symmetry-canonical; projection $P_D$ — final obstruction statement lands in $P_D$ (via L5 dictionary) but GCT's CONSTRUCTION lives in $P_B$ geometric side; pattern P4 — rigidity of orbit-closure containment implied but reinterpretation dominates.]
- **Cross-cuts**: hodge L6 (Geometric Langlands / Hitchin moduli → categorical equivalence ↔ GCT orbit closures → obstruction; P1 pattern shared across both, $P_B$ projection shared), hodge L2 (Tannakian motivic Galois ↔ representation-theoretic obstruction witness — SYMMETRY canonical at group-from-category level), katz-sarnak (SYMMETRY canonical — representation-type classification), ym:L5 (gauge complexification $\mathrm{SL}(N,\mathbb{C})$ ↔ GL-orbit structure — SYMMETRY-face shared move at group level), pvnp L1 / L11 (clone / polymorphism algebra is the Boolean-domain analog of GCT's symmetric-polynomial algebra).

### L3 — Continuous BC algebra over $\mathbb{C}$ (algebraic lift of Boolean BC)

**Claim**: There exists a continuous-domain BC algebra $\mathcal{A}_{\mathrm{BC}}^{\mathbb{C}}$ that lifts the Boolean BC system $\mathcal{C}_{\mathrm{comp}}$ (Paper 28 §3, Boolean domain with discrete Hecke semigroup action) to the algebraic / $\mathbb{C}$-valued setting required for VP vs VNP. The continuous lift preserves the type III$_1$ factor structure, the modular flow $\sigma_t$, the KMS$_1$ state, and the ITPFI factorization.

**Status**: CONJECTURED (NAMED WALL W_VP-1)
**Source**: paper39 PROOF-CHAIN Link 3 [CONJECTURED]; Framework extension (Paper 39); candidate mechanism via Connes-Marcolli 2008 "Quantum statistical mechanics over number fields" (arXiv:0801.4631; established continuous-BC variant with GL$_2$-system rather than $\mathbb{N}^*$-semigroup, but fullness structure not yet extracted).

#### Physics

- **Face**: RESONANCE (paper60 §15 — "what vibrational frequencies are ALLOWED on the circle"; the BC-algebra's spectrum — discrete in Paper 28's Boolean setting, continuous in Connes-Marcolli's GL$_2$-system — is the resonance data that the fullness criterion will interrogate; lifting from discrete to continuous is a RESONANCE-mode extension)
- **Projection**: $P_D$ (paper61 §10 — Branch D is the BC operator-algebra projection; the continuous BC is the algebraic-domain analog of Branch D's Boolean BC system; paper61 §19.5 "P vs NP as a projection: Branch D (fullness face)" extends to VP vs VNP via paper61 §06-12 Vertex 12 "Branch D: Continuous BC fullness + GCT bridge")
- **Pattern**: P4 Topological Rigidity (paper60 §15 — the BC algebra's rigidity theorem "KMS$_1$ state is unique, type III$_1$ factor is forced" extends to the continuous setting: if the lift exists, its modular structure is rigid by the same Tomita-Takesaki argument as the Boolean case; rigidity guarantees the fullness question is well-posed)
- **Invariant preserved**: C*-algebra structure (load-bearing — continuous BC is the target C*-algebra object); ITPFI factor type (background — expected to lift as type III$_1$ continuous analog); BC-KMS state (background — unique KMS$_1$ state on the continuous algebra, continuous-lift of $\omega_1$)
- **Geometric interpretation**: Paper 28's Boolean BC system lives on the finite-domain Boolean relational algebra $M_{\mathrm{Bool}}^\Gamma$; Paper 28 §3 KL 3.4.3 establishes KMS$_1$ state and type III$_1$ GNS factor there. VP vs VNP requires the algebraic-domain analog — polynomials live over $\mathbb{C}$, not $\{0,1\}$ — so Paper 28's Boolean BC must LIFT to a continuous BC algebra compatible with algebraic-circuit computation. Under $P_D$ (paper61 §10) this is Branch D's continuous-domain extension. The Connes-Marcolli 2008 GL$_2$-system (arXiv:0801.4631) is the established continuous-BC variant in the literature; its fullness structure (analog of Houdayer-Marrakchi) is NOT yet extracted, so L3 is CONJECTURED. Pattern P4 (paper60 §15): the rigidity theorem for KMS states extends naturally to continuous settings — the lift is expected to inherit type III$_1$ rigidity. [Considered but rejected: face SYMMETRY — BC semigroup action is symmetric but the LIFT question is resonance-mode / spectral; pattern P1 — reinterpretation of Boolean BC as continuous BC is fair but the rigidity statement about the lift's uniqueness dominates; projection $P_O$ — the conjectural lift could be argued as outer-ring-boundary, but mechanically it lives in $P_D$ as an extension of Branch D.]
- **Cross-cuts**: pvnp L5 (KMS$_1$ state + type III$_1$ GNS factor on Boolean BC — direct parent whose continuous lift is L3), pvnp L10 / L15 (fullness / non-fullness dichotomy whose continuous analog is L4), rh (BC algebra's modular flow at continuous-spectrum side — paper61 §10 Branch D resolvent), baum-connes (K-theory of continuous BC — paper31 K-theoretic setting for GL$_2$-system assembly map), qg5d Branch D (continuous BC variant for VP/VNP is explicitly flagged in qg5d:X-RAY §7 vertex-12 edge: "B1 spectral (continuous BC algebra variant for VP/VNP)… reason: Paper 61 §25 (candidate): continuous BC → algebraic circuit complexity. qg5d's Axiom 1 gives the operator-algebraic substrate; VP vs VNP is the target"), h12 (continuous class-field-theoretic analog via GL$_2$-system adelic structure).

### L4 — Algebraic fullness criterion on continuous BC

**Claim**: The continuous BC algebra $\mathcal{A}_{\mathrm{BC}}^{\mathbb{C}}$ admits an algebraic-fullness criterion — an analog of Houdayer-Marrakchi's fullness dichotomy for Boolean BC (Paper 28 L10 / L15 + CP-1) — stating that the type III$_1$ factor generated by the algebraic-circuit-computable representations is FULL (resp. non-full) in a quantitative sense tied to VP-resp-VNP membership.

**Status**: OPEN (part of NAMED WALL W_VP-1)
**Source**: paper39 PROOF-CHAIN Link 4 [OPEN]; Houdayer-Marrakchi 2015/2017 arXiv:1605.09613 (Boolean/finite-domain template); Marrakchi 2018 Thm B (used in pvnp L15); paper28 PROOF-CHAIN (the Boolean-domain fullness chain L1-L10 Part (i) UNCONDITIONAL + L11-L15 + CP-1 Part (ii) conditional).

#### Physics

- **Face**: RESONANCE (paper60 §15 — fullness ↔ non-fullness is the RESONANCE-mode dichotomy on the continuous BC spectrum: does the factor's inner-automorphism group close in the appropriate topology? The answer determines whether non-approximate resonance-modes are forced; paper28 pvnp:L10 cross-cut explicit — "fullness vs non-fullness is THE structural dichotomy")
- **Projection**: $P_D$ (paper61 §10 — fullness is an operator-algebra property of the BC factor; Branch D is the native home)
- **Pattern**: P4 Topological Rigidity (paper60 §15 — the fullness dichotomy is a rigidity statement: either the type III$_1$ factor is full with forced consequences, or non-full with opposite forced consequences — no middle ground; the same rigidity that drives pvnp L10 / L15 via Houdayer-Marrakchi)
- **Invariant preserved**: C*-algebra structure (load-bearing — fullness IS a C*-algebra property); ergodic property (load-bearing — in the continuous setting, fullness is expected to correspond to strong ergodicity of the continuous modular flow, analogous to pvnp L14 Jones-Schmidt strong ergodicity over finite domains); ITPFI factor type (background)
- **Geometric interpretation**: L4 lifts Houdayer-Marrakchi's Boolean/finite-domain fullness criterion (pvnp L10 via Inn(M_Bool^L) not closed ⇒ NON-FULL; pvnp L15 via Marrakchi 2018 Thm B for FULL) to the continuous setting. Under $P_D$ (paper61 §10) this is Branch D's internal structural-extension requirement — the same mechanics, different domain. The rigidity pattern (paper60 §15 P4) is inherited. The obstacle is that Houdayer-Marrakchi's proof uses the DISCRETE relational-algebra structure; the continuous analog requires a replacement for the discrete group action $G_L$ (pvnp L11 non-amenable, L12 trivial amenable radical) by a suitable continuous-group-action structure on $\mathcal{A}_{\mathrm{BC}}^{\mathbb{C}}$. This is where Connes-Marcolli 2008's GL$_2$-system potentially supplies the continuous-group-action, but the fullness criterion has not yet been derived in that setting. [Considered but rejected: face DYNAMICS — strong ergodicity is dynamical (pvnp L13b/L14 DYNAMICS assignment) but in L4 the load-bearing move is the static fullness dichotomy rather than the flow; face SYMMETRY — fullness has symmetry-group content via Inn(M) but the dichotomy statement is resonance-canonical; pattern P1 — reinterpretation of VP/VNP as fullness/non-fullness is valid but the rigidity of the dichotomy dominates.]
- **Cross-cuts**: pvnp L10 (non-full side of Boolean BC — DIRECT parent whose continuous analog is L4; paper61 §19.5 "PvNP as a projection: Branch D (fullness face)"), pvnp L15 (full side of Boolean BC via Marrakchi 2018 Thm B — direct parent), pvnp L14 (Jones-Schmidt strong ergodicity — the dynamical partner of fullness in Paper 28, whose continuous analog is needed), pvnp L22 (full ∧ non-full ⇒ ⊥ Houdayer-Marrakchi dichotomy — the contradiction engine whose continuous-domain version would drive VP ≠ VNP), rh (BC-algebra fullness analog on continuous-spectrum side, paper61 §15.4), baum-connes (assembly-map closure under continuous fullness), ym:L14 (mass gap rigidity ↔ fullness-as-gap rigidity analog — both are type-III$_1$-factor rigidity manifestations).

### L5 — Algebraic-fullness ↔ VP ≠ VNP via GCT dictionary

**Claim**: The algebraic-fullness criterion of L4 is EQUIVALENT to (or strictly implies) $\mathrm{VP} \neq \mathrm{VNP}$, via a dictionary that connects the BC-algebraic type III$_1$ fullness structure to the GCT orbit-closure / Kronecker-coefficient obstruction witnesses. In one direction: non-fullness of $\mathcal{A}_{\mathrm{BC}}^{\mathbb{C}}$ restricted to the permanent's representation class yields a Kronecker-coefficient obstruction, which is GCT's proposed witness of VP ≠ VNP.

**Status**: CANDIDATE
**Source**: paper39 PROOF-CHAIN Link 5 [CANDIDATE]; Mulmuley 2011 algorithmic conjecture (GCT-style algorithmic formulation); framework addition: type III$_1$ fullness ↔ Kronecker-obstruction dictionary.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — the dictionary CONNECTS symmetry-group representation theory (GCT / Kronecker coefficients on $S_n$ tensor products) with type III$_1$ fullness (which has symmetry-group content via Inn(M) / Out(M)); the load-bearing move is the BRIDGE between two symmetry-side representations)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 12 — "Compound: $P_D$ (the algebraic analog of P vs NP is a purer statement about the BC algebra's representation theory)"; the DICTIONARY lands in $P_D$ even though GCT (L2) lives in $P_B$ — the L5 statement is the $P_D$-target that the $P_B$ GCT input is being mapped TO)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — L5 reinterprets two frameworks (continuous BC fullness + GCT orbit closures) as expressing the same underlying computational obstruction; this is Pattern 1 in its bridge form: two formalisms are revealed to compute the same obstruction invariant)
- **Invariant preserved**: C*-algebra structure (load-bearing — fullness property of $\mathcal{A}_{\mathrm{BC}}^{\mathbb{C}}$); Galois representation (load-bearing — Kronecker decomposition of $S_n$-representations on polynomial space; the two invariants are being RELATED, not just co-present)
- **Geometric interpretation**: L5 is the framework's NOVEL contribution — a dictionary between the continuous-BC fullness criterion (paper61 §19, Branch D operator-algebra side) and the GCT orbit-closure / Kronecker-coefficient obstructions (paper61 §29 App C row 12 secondary $P_B$ bridge). Mulmuley 2011 formulated the algorithmic version of GCT; the framework adds that type III$_1$ fullness is the operator-algebra witness mechanism for GCT's obstruction witnesses. Under $P_D$ (paper61 §06-12 Vertex 12) this dictionary is Branch D's CLOSURE of the VP vs VNP question — if the dictionary holds, Link 4's fullness determination translates directly to VP ≠ VNP. Pattern 1 (paper08 §36): bridging two apparently-different frameworks (BC fullness, GCT orbit closures) by showing they compute the same obstruction. The status is CANDIDATE because the dictionary's formal construction is open — the Kronecker → fullness direction is the framework's proposal; the reverse direction (fullness → Kronecker obstruction) requires deriving Kronecker-coefficient information from type III$_1$ structure. [Considered but rejected: face RESONANCE — fullness itself is resonance-mode (L4 assignment) but the DICTIONARY move is symmetry-canonical because it relates TWO representation-theoretic frameworks; projection $P_B$ — GCT side lives in $P_B$ but the COMPOSED dictionary lands in $P_D$ (compare hodge:L7 where Routes A + B compose landing in $P_D$); pattern P4 — rigidity of the dictionary implied but reinterpretation is the load-bearing move.]
- **Cross-cuts**: hodge L7 (two-route composition Routes A ($P_D$) + B ($P_B$) → Hodge in $P_D$ — structural parallel to L5's $P_D$ fullness + $P_B$ GCT → VP ≠ VNP in $P_D$; paper61 §19.6 compound projection framework), pvnp L1 / L11 (polymorphism algebra ↔ GCT polynomial representation theory — Boolean analog), katz-sarnak (symmetry-type classification ↔ Kronecker-coefficient classification — SYMMETRY canonical shared move at representation-theoretic level), baum-connes (K-theoretic assembly map translates between operator-algebra and geometric-cohomology frameworks, analogous to L5's BC-fullness ↔ GCT-Kronecker dictionary), ym:L5 (group complexification $\mathrm{SL}(N,\mathbb{C})$ ↔ GL-orbit structure — representation-theoretic shared move, per paper60 §12 bridge $k=4$).

### L6 — Permanent-specific border-complexity obstruction via BC-algebraic representation theory

**Claim**: The border complexity $\underline{\mathrm{dc}}(\mathrm{PER}_n)$ — the limit-complexity allowing approximative algebraic circuits — also satisfies a super-polynomial lower bound, via a BC-algebraic representation-theoretic obstruction specific to the permanent. This addresses the "approximative / border" form of VP ≠ VNP, which is what recent GCT work (2024-2025) has converged on as the accessible target.

**Status**: OPEN (NAMED WALL W_VP-2)
**Source**: paper39 PROOF-CHAIN Link 6 [OPEN]; arXiv:2502.02442 (Feb 2025 — isolates the exact property the determinant lacks that causes VNP-hardness proofs for the permanent to fail; directly relevant to L6); Bürgisser border-complexity literature; 2024-2025 asymptotic Kronecker-coefficient work.

#### Physics

- **Face**: RESONANCE (paper60 §15 — border complexity = approximative resonance-mode analysis: which modes are accessible in the limit-closure of algebraic circuits? The determinant-vs-permanent asymmetry identified in arXiv:2502.02442 is a RESONANCE-structural distinction between the two polynomials; their differing border-mode signatures)
- **Projection**: $P_D$ (paper61 §10 — border complexity is expected to live in the continuous-BC operator-algebra projection; the BC-algebraic representation-theoretic witness is the target mechanism)
- **Pattern**: P4 Topological Rigidity (the border / approximative obstruction is a rigidity statement: even in the limit-closure, the permanent's BC-representation structure is distinguishable from the determinant's; the rigidity protects the distinction across the approximation process — analog of paper28's Bulatov-Zhuk rigidity under CSP closure)
- **Invariant preserved**: C*-algebra structure (load-bearing — BC-algebraic representation theory on the approximative-complexity side); scaling dimension (load-bearing — border rank IS a scaling exponent on the approximative-circuit size)
- **Geometric interpretation**: The 2024-2025 GCT literature (arXiv:2502.02442) has narrowed the VP ≠ VNP attack to the BORDER/APPROXIMATIVE complexity question: under approximation, what property specifically distinguishes the permanent from the determinant? L6 proposes that the BC-algebraic representation theory of the continuous-BC algebra (via the dictionary of L5) supplies this property: the permanent's representation class forces non-fullness / specific Kronecker-obstruction pattern that the determinant's representation class avoids. Under $P_D$ (paper61 §10) this is the BORDER-REFINED version of Link 5, specialized to the permanent. Pattern 4 (paper60 §15): rigidity of the obstruction under approximation. [Considered but rejected: face SYMMETRY — representation-theoretic content is symmetry-side but the LIMIT / border-closure structure is resonance-mode-canonical; pattern P1 — reinterpretation of border complexity as BC-representation property is fair but the rigidity under approximation is load-bearing; pattern P5 — zeta-regularization of approximative sums could apply but is secondary.]
- **Cross-cuts**: pvnp CP-1 (conditional theorem on full-factor isomorphism — analogous conditional structural step; both are operator-algebraic CANDIDATE closures), hodge L8 (motivic functoriality closure extending from BC-motivated to ALL smooth projective ↔ L6 extending from L5 dictionary to permanent-specific border closure — P4 closure-rigidity pattern shared), ym:L18 (AF match at short-distance conditional — analog at the perturbative-nonperturbative interface, structurally the "final mechanical closure" conditional), rh (zeta-regularization at spectral-side boundary — L6 P5 alternative reading cross-cuts here), katz-sarnak (Kronecker-coefficient asymptotic classification ↔ Katz-Sarnak symmetry-type asymptotics on L-function families).

---

## §4 Branch Map

The VP vs VNP proof chain is compact (6 links) with a clear two-track structure that composes at L5 and specializes at L6. Unlike YM's largely-linear 18-layer chain or PvNP's parallel Part (i) + Part (ii) + Corollary architecture, VP vs VNP has TWO INPUTS (continuous BC via L3-L4 + GCT via L2) composing at a DICTIONARY (L5) with a permanent-specific refinement (L6). This mirrors hodge's two-route structure at a higher level of conjecturality.

```
L1 (Valiant permanent VNP-complete, LITERATURE — foundation)
                │
                │  anchors the target (permanent = VNP-hard object)
                │  for all subsequent obstruction arguments
                ▼
        ┌───────┴──────────────────────┐
        │                              │
        │                              │  Route I (GCT): Mulmuley-Sohoni
        │                              │  geometric obstruction
        │                              │
        │                              ▼
        │                      L2 (GCT orbit closures +
        │                          Kronecker, LITERATURE)
        │                          [SYMMETRY | P_B | P1]
        │                              │
        │  Route II (continuous BC):   │
        │  Branch D lift + fullness    │
        │                              │
        ▼                              │
L3 (Continuous BC lift, CONJECTURED)   │
   [RESONANCE | P_D | P4]              │
        │                              │
        ▼                              │
L4 (Algebraic fullness criterion,      │
    OPEN)                              │
   [RESONANCE | P_D | P4]              │
        │                              │
        └───────┬──────────────────────┘
                │
                │  Routes I + II compose
                ▼
       L5 (Fullness ↔ VP ≠ VNP via GCT dictionary, CANDIDATE)
          [SYMMETRY | P_D | P1]
                │
                │  specialize to the permanent's
                │  border / approximative regime
                ▼
       L6 (Permanent-specific border obstruction, OPEN — W_VP-2)
          [RESONANCE | P_D | P4]
                │
                ▼
             VP ≠ VNP over ℂ

Route I (L2)     physics triplet: [SYMMETRY  | P_B | P1]
Route II (L3-L4) physics triplet: [RESONANCE | P_D | P4]
Composition (L5) physics triplet: [SYMMETRY  | P_D | P1]
Refinement (L6)  physics triplet: [RESONANCE | P_D | P4]

The two routes differ in which PROJECTION bears the construction:
- Route I (L2) is P_B-canonical (GCT orbit closures, Kähler-moduli side,
  paper61 §08 Branch B gauge geometry)
- Route II (L3-L4) is P_D-canonical (continuous BC, operator-algebra,
  paper61 §10 Branch D)
- Composition at L5 lands in P_D (the BC-algebraic interpretation
  is the target) while drawing on both inputs
- L6 refines L5 into a permanent-specific border-complexity obstruction,
  staying in P_D

This tells us: VP vs VNP is fundamentally a P_D-problem with P_B auxiliary
(same architecture as hodge). The GCT route is a SECONDARY projection
supplying geometric obstruction witnesses; the continuous BC route is the
PRIMARY projection where the closure statement lives. Mulmuley uses
Kronecker (P_B); the framework uses type III_1 fullness (P_D);
paper39 PROOF-CHAIN: "Same question, different weapons."
```

The chain is NOT yet branched in the sense of alternative proof routes for the SAME link — there is no "Route Standard" / "Route 18' bypass" structure as in YM:L18, and no "Part (i) + Part (ii)" dual-direction structure as in PvNP. It is a DAG with two input sources composing at L5. The conjecturality pattern (L1 LITERATURE, L2 LITERATURE, L3 CONJECTURED, L4 OPEN, L5 CANDIDATE, L6 OPEN) indicates the vertex is early-stage: the foundational inputs (L1, L2) are closed classical results, but every link that requires framework work (L3-L6) is open.

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | VP vs VNP does not interrogate winding / cyclotomic / Pontryagin structure at the layer level. |
| DYNAMICS   |   0   |                       | No modular-flow / gap-distribution / flow-on-circle content at the layer level (though L4's strong-ergodicity invariant is dynamical in spirit — a cross-cut to pvnp L13b/L14, not a primary face). |
| HARMONICS  |   0   |                       | No Fourier / harmonic-mixing content. |
| MEASURE    |   0   |                       | No equidistribution / weak-* content. |
| AMPLITUDE  |   0   |                       | No growth-rate / loudness bounds. |
| SYMMETRY   |   2   | ████████              | L2 GCT orbit-closure / Kronecker-coefficient representation theory; L5 BC-fullness ↔ GCT dictionary via symmetry-group action. Paper60 §12 Katz-Sarnak SYMMETRY face canonical — representation-theoretic classification is the mechanism. |
| CURVATURE  |   0   |                       | No gauge-curvature / mass-gap content directly (cross-cut to ym:L14 exists via fullness-as-gap rigidity, not a primary face here). |
| ARITHMETIC |   1   | ████                  | L1 Valiant VNP-completeness via p-projections — monomial-expansion / integer-coefficient structure on $S_n$ orbits. Paper60 §14 ARITHMETIC face — integers-lattice-on-polynomial-exponents shared structural form. |
| RESONANCE  |   3   | ████████████          | DOMINANT. L3 continuous BC lift, L4 algebraic fullness criterion, L6 permanent-border obstruction — three resonance-mode / BC-algebraic-spectrum layers. The vertex's PRIMARY face per paper61 §29 App C.1 row 12. |
| SPREAD     |   0   |                       | No $L^2$-mass-spreading content. |

**Interpretation**: RESONANCE dominates (3 / 6 layers, 50%) — confirming paper61 §29 Appendix C.1 row 12's RESONANCE assignment for VP vs VNP. This parallels PvNP's RESONANCE dominance (Paper 28's primary face is also RESONANCE). SYMMETRY carries 2 layers (33%) via the GCT route (L2) and the L5 dictionary. ARITHMETIC carries the Valiant foundation (L1, 17%). Seven faces are absent — VP vs VNP is narrowly concentrated on RESONANCE / SYMMETRY / ARITHMETIC, which is structurally consistent with its "algebraic-representation-theoretic pure question" character (paper61 §06-12 Vertex 12: "the algebraic analog of P vs NP is a purer statement about the BC algebra's representation theory"). Compared to YM (6 faces populated, diverse) and PvNP (6 faces populated, diverse), VP vs VNP's three-face concentration reflects both its compactness (6 layers) and its early-stage conjecturality — the face distribution is likely to broaden as the proof chain matures.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No quantum-observable content — VP vs VNP is pure computational complexity, not interpretable in terms of Born rule / Bell / spin-statistics. |
| $P_B$        |   1   | ████                 | L2 GCT orbit-closures on polynomial space (gauge-bundle / Kähler-moduli side, paper61 §08 Branch B). Secondary projection per paper61 §29 Appendix C.1 row 12. |
| $P_C$        |   0   |                      | Cosmological projection forgets algebraic complexity entirely. |
| $P_D$        |   5   | ████████████████████ | DOMINANT. L1 Valiant classification + L3 continuous BC lift + L4 algebraic fullness + L5 dictionary landing + L6 permanent-border obstruction. Paper61 §06-12 Vertex 12: "Compound $P_D$". 83% of layers. |
| $P_E$        |   0   |                      | No pin — VP vs VNP does not contribute to the 36-pin master table (paper61 §29 Appendix C.1 row 12 leaves $P_E$ unlisted). |
| $P_O$        |   0   |                      | No layer assigned to $P_O$. The Clay-equivalent boundary argument could be made for the top-level claim's "Valiant's algebraic P ≠ NP" statement, but mechanically L1 (the Valiant foundation) lives in $P_D$, and the remaining layers live in $P_D$ or $P_B$. Contrast with ym:L18 and pvnp Corollary L16-L23 which have explicit $P_O$ assignments for the Clay-grade boundary. VP vs VNP's "outer-ring closure" is COMMUNITY-STANDARD rather than Clay-Millennium, so the $P_O$ projection is less load-bearing here. |

**Interpretation**: The projection profile is extremely concentrated. $P_D$ dominates (5 / 6 layers, 83%) — VP vs VNP is fundamentally a Branch D / continuous-BC object. $P_B$ carries just L2 (GCT), providing geometric-obstruction auxiliary structure. This matches paper61 §06-12 Vertex 12's "Compound $P_D$" assignment and paper61 §29 App C.1 row 12 primary=$P_D$, secondary=$P_B$. The absence of $P_O$ is structurally characteristic: unlike Clay-Millennium vertices (YM, RH, BSD, PvNP, Hodge), VP vs VNP is a community-standard conjecture whose boundary status doesn't foreground outer-ring projection structure. Compared to hodge's 6 / 0 ($P_D$ / $P_O$) distribution and pvnp's $P_D$-dominant + small-$P_O$ corollary-tail distribution, VP vs VNP is the most $P_D$-pure vertex x-rayed to date. The profile also mirrors the vertex's 1/10 confidence — the projection histogram is narrow because the proof chain is narrow because the framework content at most layers is conjectural.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                         pvnp (paper28)
                         ═══ L3 ↔ pvnp L5 (KMS_1 + type III_1 —
                                DIRECT parent, continuous lift)
                         ═══ L4 ↔ pvnp L10 (non-full side —
                                Boolean parent, continuous analog)
                         ═══ L4 ↔ pvnp L15 (full side via
                                Marrakchi 2018, Boolean parent)
                         ═══ L4 ↔ pvnp L22 (full ∧ non-full ⇒ ⊥
                                dichotomy engine)
                         ═══ L6 ↔ pvnp CP-1 (conditional
                                structural step analog)
                               │
                               │
      hodge (paper29) ═════════│═════════ qg5d (Branch D / hub)
      ═══ L2 ↔ hodge L6         │         ═══ L3 ↔ qg5d Branch D
         (Geometric            │             (continuous BC variant
          Langlands ↔ GCT —    │              for VP/VNP, explicit
          P_B / P1 parallel)   │              edge in qg5d:X-RAY
      ═══ L5 ↔ hodge L7         │              §7 vertex-12)
         (two-route            │         ═══ L3 ↔ qg5d Axiom 1
          composition          │              (B1 spectral
          landing in P_D —     │              operator algebra)
          compound projection) │         ─── L2 ↔ qg5d Branch B
      ─── L2 ↔ hodge L2         │              (P_B geometric side)
         (Tannakian ↔ GCT       │
          representation-      │
          theoretic            │
          classification)      │
      ─── L6 ↔ hodge L8         │
         (P4 closure-rigidity  │
          pattern shared —     │
          "final mechanical    │
          closure")            │
                               │
                    vp-vs-vnp  │
                               │
      baum-connes ═════════════│═════════ katz-sarnak
      (paper31)                │         (paper46 — SYMMETRY
      ═══ L3 ↔ K-theory of     │         canonical)
         continuous BC /       │         ═══ L2 ↔ Kronecker
         GL_2-system           │              ↔ symmetry-type
         assembly map          │              classification
      ═══ L4 ↔ assembly-map    │         ─── L5 ↔ representation-
         closure under         │              type classification
         fullness              │              dictionary
      ─── L5 ↔ K-theoretic     │
         ↔ operator-algebra   │
         translation          │
                              │
                              │
      ym (paper08) ═══════════│═══════════ rh (paper13)
      ═══ L4 ↔ ym:L14         │           ═══ L3 ↔ continuous-
         (mass gap rigidity   │              spectrum BC-algebra
          ↔ fullness-as-gap   │              side, paper61 §10
          rigidity — type    │              Branch D resolvent
          III_1 factor       │           ─── L4 ↔ BC-algebra
          rigidity)          │              fullness analog,
      ─── L2 ↔ ym:L5          │              paper61 §15.4
         (SL(N,C) extension  │           ─── L6 ↔ zeta-regulariz-
          ↔ GL-orbit         │              ation at short-
          structure — P1)    │              distance side (P5 alt)
      ─── L5 ↔ ym:L5          │
         (group complexifi-  │
          cation shared     │
          symmetry move     │
          per paper60 §12   │
          bridge k=4)       │
                            │
                   h12 (paper25)
                   ─── L3 ↔ class-field-theoretic
                       continuous analog via
                       GL_2-system adelic structure
                       (Connes-Marcolli 2008
                       is class-field-theoretic)

      goldbach (paper33)
      ─── L1 ↔ ARITHMETIC canonical
          monomial expansion over ℕ

      bgs (paper32)
      ─── L2 ↔ Kronecker asymptotic statistics
          ↔ GUE spectral statistics
          (both representation-theoretic)
```

### Bullet list (per-edge)

- **L1 ↔ pvnp L17 / L18 / L20** — shared scaling dimension (NP-complete ↔ VNP-complete target).
  - Reason: Valiant's 1979 permanent-is-VNP-complete parallels Cook-Levin's 3-SAT-is-NP-complete; both are the canonical hardness targets in their respective complexity classes; pvnp L17-L20 uses 3-SAT as the hardness witness for the contradiction, L1 uses PER$_n$ as the hardness target for the obstruction.
  - Transposition candidate: YES (capacitor ALG↔COMP parallel hardness reductions).

- **L1 ↔ goldbach:L_int** — shared scaling dimension (ARITHMETIC canonical).
  - Reason: monomial expansion over $\mathbb{N}$ shared structural form; p-projections permute monomials in a way structurally parallel to additive combinations of primes.
  - Transposition candidate: SPECULATIVE.

- **L1 ↔ hodge L8** — shared scaling dimension (motivic functoriality ↔ p-projection functoriality).
  - Reason: both extend from a "motivated / BC-relevant" slice to the full class via a functoriality argument — hodge L8 extends from BC-motivated to all smooth projective, L1 embeds arbitrary VNP polynomials into the permanent via p-projections.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ hodge L6** — shared C*-algebra structure + Galois representation (P_B / P1).
  - Reason: GCT orbit closures (Mulmuley-Sohoni) and Geometric Langlands (Gaitsgory-Raskin) are both "categorical / orbit-moduli-side reinterpretations of a primary question"; both live in $P_B$ (Branch B gauge / Kähler-moduli geometry); both use Pattern 1 (Geometric Reinterpretation); paper60 §15 RESONANCE face secondary for both.
  - Transposition candidate: YES (P_B / P1 shared structural move).

- **L2 ↔ hodge L2** — shared Galois representation (Tannakian ↔ GCT representation-theoretic classification).
  - Reason: Tannakian motivic Galois group for hodge ↔ symmetric group $S_n$ Kronecker decomposition for GCT — both are symmetry-type representation-theoretic classifications, paper60 §12 Katz-Sarnak face.
  - Transposition candidate: YES.

- **L2 ↔ katz-sarnak** — shared Galois representation (SYMMETRY canonical).
  - Reason: Kronecker-coefficient classification ↔ Katz-Sarnak symmetry-type classification — both classify "which representations are accessible" on some canonical family.
  - Transposition candidate: YES.

- **L2 ↔ ym:L5** — shared gauge class (group complexification).
  - Reason: $\mathrm{SL}(N, \mathbb{C})$ extension of compact $SU(N)$ in YM parallels $\mathrm{GL}_n$-orbit structure on the polynomial space; paper60 §12 bridge $k=4$ identifies the shared move; SYMMETRY face at group level.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ bgs** — shared Galois representation (Kronecker asymptotics ↔ GUE statistics).
  - Reason: 2024-2025 asymptotic Kronecker-coefficient literature and GUE spectral statistics of Riemann zeros both are representation-theoretic asymptotic distributions; both live in Branch D's symmetry-type sector.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ pvnp L1 / L11** — shared Galois representation (clone / polymorphism ↔ GCT polynomial representation).
  - Reason: Paper 28's Boolean polymorphism-algebra classification is the finite-domain analog of GCT's symmetric-polynomial-algebra classification; both classify hardness by a group action on a discrete / polynomial structure.
  - Transposition candidate: YES (via paper28's polymorphism-algebra framework explicitly generalized to algebraic setting).

- **L3 ↔ pvnp L5** — shared BC-KMS state + ITPFI factor type (DIRECT parent).
  - Reason: pvnp L5 establishes KMS$_1$ state + type III$_1$ GNS factor on Boolean BC (key lemma 3.4.3); L3 is its continuous lift. This is the vertex's PRIMARY edge to pvnp.
  - Transposition candidate: YES (capacitor SPEC↔QFT continuous BC extension).

- **L3 ↔ qg5d Branch D** — shared C*-algebra structure (explicit edge).
  - Reason: qg5d X-RAY §7 vertex-12 edge explicit: "continuous BC algebra variant for VP/VNP… Paper 61 §25 (candidate): continuous BC → algebraic circuit complexity. qg5d's Axiom 1 gives the operator-algebraic substrate; VP vs VNP is the target." This is the vertex's PRIMARY edge to qg5d.
  - Transposition candidate: YES (capacitor SPEC↔ALG continuous-BC lift).

- **L3 ↔ rh** — shared C*-algebra structure (continuous BC via paper61 §10 Branch D resolvent).
  - Reason: RH's BC-algebra side is continuous-spectrum; L3's lift to continuous BC shares the same spectrum-continuity structure.
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ baum-connes** — shared C*-algebra structure (K-theory of continuous BC).
  - Reason: Baum-Connes K-theory of continuous BC / GL$_2$-system assembly map parallels L3's continuous-BC-lift foundation; both rest on paper31 Baum-Connes K-theoretic infrastructure.
  - Transposition candidate: YES.

- **L3 ↔ h12** — shared C*-algebra structure (class-field-theoretic continuous analog).
  - Reason: Connes-Marcolli 2008 GL$_2$-system is class-field-theoretic; h12's continuous-class-field structure shares the same adelic / GL$_2$-system foundation.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ pvnp L10** — shared C*-algebra structure (non-full side DIRECT parent).
  - Reason: pvnp L10 establishes non-fullness of Inn(M_Bool^L) via Houdayer-Marrakchi; L4 is its continuous analog. paper61 §19.5 explicitly "PvNP as a projection: Branch D (fullness face)".
  - Transposition candidate: YES.

- **L4 ↔ pvnp L15** — shared C*-algebra structure (full side DIRECT parent).
  - Reason: pvnp L15 establishes fullness via Marrakchi 2018 Thm B on Boolean BC; L4 is its continuous analog.
  - Transposition candidate: YES.

- **L4 ↔ pvnp L14** — shared ergodic property (strong ergodicity DYNAMICAL partner).
  - Reason: pvnp L14's Jones-Schmidt strong ergodicity is the dynamical partner of fullness on Boolean BC; L4's continuous-BC fullness requires a continuous-domain strong-ergodicity analog.
  - Transposition candidate: YES.

- **L4 ↔ pvnp L22** — shared C*-algebra structure (fullness dichotomy engine).
  - Reason: pvnp L22's "full ∧ non-full ⇒ ⊥" via Houdayer-Marrakchi dichotomy is the contradiction engine driving pvnp's QED (P ≠ NP by contradiction); L4 provides the continuous-domain version of the same dichotomy, which at L5 would drive VP ≠ VNP analogously.
  - Transposition candidate: YES.

- **L4 ↔ ym:L14** — shared C*-algebra structure (mass gap rigidity ↔ fullness-as-gap rigidity).
  - Reason: both are type III$_1$ factor rigidity manifestations — YM's mass gap is a spectral-gap rigidity, L4's fullness is an operator-algebraic rigidity of the same factor-theoretic character. Cross-cut explicit in pvnp X-RAY L10 bullet.
  - Transposition candidate: YES (capacitor SPEC↔QFT P4 rigidity shared).

- **L4 ↔ rh** — shared C*-algebra structure (BC-algebra fullness analog on continuous-spectrum side).
  - Reason: paper61 §15.4 identifies a BC-algebra fullness analog on RH's continuous-spectrum resolvent side.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ baum-connes** — shared C*-algebra structure (assembly-map closure).
  - Reason: continuous BC fullness should imply assembly-map closure in the Baum-Connes K-theoretic framework; both are type III$_1$ closure properties.
  - Transposition candidate: YES.

- **L5 ↔ hodge L7** — shared Galois representation + C*-algebra structure (two-route composition).
  - Reason: hodge L7 composes Route A ($P_D$ endomotive) + Route B ($P_B$ Langlands) landing in $P_D$; L5 composes Route I ($P_B$ GCT) + Route II ($P_D$ continuous BC) landing in $P_D$. Structurally parallel compound-projection compositions. paper61 §19.6 compound-projection framework.
  - Transposition candidate: YES (capacitor COMP-PROJ compound shared).

- **L5 ↔ pvnp L1 / L11** — shared Galois representation (polymorphism-algebra ↔ polynomial-algebra classification).
  - Reason: L5's BC-fullness ↔ GCT dictionary is the algebraic-domain analog of pvnp's Boolean-BC-fullness ↔ clone-classification dictionary.
  - Transposition candidate: YES.

- **L5 ↔ katz-sarnak** — shared Galois representation (SYMMETRY canonical representation-type dictionary).
  - Reason: Katz-Sarnak symmetry-type-from-functional-equation ↔ L5's fullness-to-Kronecker-obstruction both are representation-type classification dictionaries.
  - Transposition candidate: YES.

- **L5 ↔ baum-connes** — shared C*-algebra structure (K-theoretic / operator-algebra translation dictionary).
  - Reason: Baum-Connes assembly map translates between operator-algebra and geometric-cohomology frameworks — this is the paradigmatic dictionary-between-frameworks move, structurally parallel to L5's BC-fullness ↔ GCT-Kronecker dictionary.
  - Transposition candidate: YES.

- **L5 ↔ ym:L5** — shared gauge class (group complexification P1 shared).
  - Reason: YM's $\mathrm{SL}(N, \mathbb{C})$ complexification is the paradigmatic Pattern 1 "reinterpret via the natural ambient group" move; L5's dictionary operates in the same Pattern 1 framing at the representation-theoretic level.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ pvnp CP-1** — shared C*-algebra structure (conditional structural step).
  - Reason: pvnp CP-1 (M_Bool^L ≅ L(R_L) Feldman-Moore groupoid) is the conditional structural step completing Part (ii); L6 is the analogous conditional structural step for the permanent-border obstruction — both are CANDIDATE / CONDITIONAL operator-algebraic closures at the end of a composition chain.
  - Transposition candidate: YES.

- **L6 ↔ hodge L8** — shared scaling dimension (P4 closure-rigidity pattern).
  - Reason: hodge L8 motivic functoriality extending from BC-motivated to all smooth projective ↔ L6 extending from L5 dictionary to permanent-specific border closure. Both are "final mechanical closure" P4-rigidity statements on a previously-obtained conditional structure.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ ym:L18** — shared scaling dimension (final-mechanical-closure conditional analog).
  - Reason: YM L18's AF-match + leading-OPE is the final conditional at the perturbative-nonperturbative interface; L6 is the final conditional at the permanent's approximative-complexity interface — both are "final-closure-conditional" in structure, though L18 lives in $P_O$ and L6 in $P_D$.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ rh** — shared scaling dimension (zeta-regularization at short-distance side, alternative P5 reading).
  - Reason: 2024-2025 asymptotic Kronecker work uses zeta-regularized spectral sums at the limit; RH's zeta-regularization on the spectral side is structurally parallel.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ katz-sarnak** — shared Galois representation (asymptotic representation-type classification).
  - Reason: Kronecker-coefficient asymptotic classification parallels Katz-Sarnak symmetry-type asymptotics on L-function families — both are "how do representation-types distribute asymptotically" questions.
  - Transposition candidate: SPECULATIVE.

- **qg5d (hub) cross-cuts** — multiple.
  - Reason: qg5d X-RAY §7 vertex-12 edge explicit: L3 ↔ qg5d Branch D (continuous BC variant), L3 ↔ qg5d Axiom 1 (B1 spectral operator algebra); L2 ↔ qg5d Branch B (P_B geometric side, GCT orbit-closure geometry). Hub-spoke structure: every layer ultimately draws on qg5d via Branch D primary + Branch B auxiliary.
  - Transposition candidate: YES (capacitor QG5D-HUB).

**Summary**: **31 cross-cut edges** identified across 6 layers (~5.2 cross-cuts per layer — actually the highest average-per-layer density in the X-Ray atlas so far, because compact proof chains with strong framework-parent dependencies produce densely cross-cut annotations). **7 verified-YES** (L3↔pvnp L5 direct, L3↔qg5d explicit, L4↔pvnp L10/L15/L22/L14 direct + pvnp cross-cut bullets, L5↔hodge L7 compound-projection parallel, L2↔hodge L6 P_B/P1 parallel, L4↔ym:L14 explicit pvnp cross-cut, L5↔pvnp L1/L11). **24 SPECULATIVE/CANDIDATE** (pending continuous-BC L3 construction + L4 fullness criterion + L5 dictionary formalization). The PRIMARY edges are L3 ↔ pvnp L5 (continuous lift of KMS$_1$ + type III$_1$) and L3 ↔ qg5d Branch D (paper61 §25 candidate explicit). The vertex is DENSELY CONNECTED to pvnp (5 direct edges) and to hodge (3 edges) — the three papers form a tight sub-cluster of the RESONANCE / SYMMETRY / operator-algebra cold zone in the programme graph (paper61 §29 Appendix closing notes "cold zone contains the highest-resistance open problems (Hodge, Baum-Connes, P vs NP) and the most uncertain vertices (VP vs VNP, Turbulence)").

---

## §8 Current Walls

- **W_VP-1 — Continuous BC lift + algebraic fullness criterion (Links 3-4)**: Lifting Paper 28's Boolean BC system (discrete Hecke semigroup action, finite-domain fullness via Houdayer-Marrakchi) to a continuous BC algebra over $\mathbb{C}$ compatible with algebraic-circuit computation, and deriving the algebraic-fullness criterion on that continuous algebra. Status: **OPEN as a conditional** (L3 CONJECTURED; L4 OPEN). Confidence per audit-strategy §4: **0.5**. Candidate mechanism: Connes-Marcolli 2008 "Quantum statistical mechanics over number fields" (arXiv:0801.4631) GL$_2$-system as established continuous-BC variant; fullness structure not yet extracted. No capacitor cell yet; decomposition / CCM verification not yet launched.

- **W_VP-2 — Border / approximative complexity obstruction (Link 6)**: Proving the permanent-specific border-complexity obstruction via BC-algebraic representation theory, addressing the "approximative / border" form of VP ≠ VNP — which is what recent GCT work (2024-2025 per arXiv:2502.02442) has converged on as the accessible target. Status: **OPEN** (CANDIDATE — the direction is identified but the construction is not yet attempted). Confidence per audit-strategy §4: **0.55**. Depends on L5 (L5 CANDIDATE status). Bypass route: the 2025 preprint (arXiv:2502.02442) isolates the determinant-vs-permanent distinguishing property; L6 proposes that BC-algebraic representation theory supplies the operator-algebraic version of this property.

- **(Derivative) L5 CANDIDATE — Fullness ↔ VP ≠ VNP via GCT dictionary**: Not a named wall per se, but the CANDIDATE-status dictionary at L5 is the pivot on which W_VP-1 and W_VP-2 hinge. If L5's dictionary can be formally constructed (framework novel contribution), W_VP-1's closure (continuous BC fullness) translates directly to VP ≠ VNP over ℂ via the Kronecker-obstruction bridge.

No other named walls in the live PROOF-CHAIN. Links 1 and 2 are LITERATURE (unconditionally closed). Links 3-6 are all conditional/open, reflecting the 1/10 aggregate confidence.

Compared to ym (1 wall = H4, 1 bypass = Step 18') and hodge (3 walls = W1/W2/W3, multiple partial closures), vp-vs-vnp has 2 named walls (W_VP-1, W_VP-2) consolidating 4 open/conjectural links — the wall structure is MORE UNIFIED (everything routes through the continuous-BC-fullness program) but LESS CLOSED (no partial closure on any named wall yet, vs hodge W1 ab-var-powers partial closure via 2024 arXiv:2510.21562).

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/vp-vs-vnp/` — NOT YET CREATED. Priority targets when launched: W_VP-1 (decompose Link 3 continuous-BC-lift into sub-chains — e.g., Connes-Marcolli 2008 formal adaptation; KMS$_1$ uniqueness in continuous setting; type III$_1$ factor construction); then Link 4 algebraic fullness (sub-chain on Houdayer-Marrakchi's proof steps adapted to continuous domain). Links 1-2 (LITERATURE) need no decomposition. Link 5 (dictionary construction) and Link 6 (border obstruction) both benefit from decomposition once L3-L4 sub-chain is visible.

- **CCM verification**: `strategy/ccm-verification/ledger.md#vp-vs-vnp` — NOT YET CREATED. VP vs VNP does NOT directly depend on CCM 2005 (Connes-Consani-Marcolli arXiv:math/0512138, which is hodge / paper28's literature foundation). The closest CCM dependency is **Connes-Marcolli 2008 arXiv:0801.4631** (different paper: "Quantum statistical mechanics over number fields"), which is the candidate continuous-BC / GL$_2$-system construction for L3. Expected verdict when ledger written: **CCM 2005-INDEPENDENT**; **Connes-Marcolli 2008-DEPENDENT** (L3 — the GL$_2$-system is the starting point for the continuous-BC lift).

- **Inner rings**: NOT APPLICABLE — vp-vs-vnp is a primary outer-ring vertex (community-standard level, paper61 §29 App C.1 row 12, paper39), not an inner-ring object.

- **Millennium bundle**: NOT APPLICABLE — VP vs VNP is COMMUNITY-STANDARD, not Clay-Millennium. Per `strategy/vp-vs-vnp/00-audit-strategy.md` §1: "Source type: COMMUNITY-STANDARD. Source: Valiant (1979) STOC; Bürgisser (2000) Springer monograph. Special provisions: None direct. Not on Clay list." Audit venue per §2: JACM / SICOMP / Annals. No `strategy/vp-vs-vnp/millenium-brief.md` — the closest analog is `strategy/vp-vs-vnp/vp-vs-vnp-audit-brief.md` (BARE MODE audit brief for community-standard).

- **Audit bundle**: `strategy/vp-vs-vnp/` — ACTIVE per `strategy/vp-vs-vnp/vp-vs-vnp-audit-brief.md`. B_bare + C_bare deliverables targeted (M × 6 compliance map, 6 Requirements from §3 audit-strategy). 15-researcher landscape + 6 major-approach §N Related Work section required. This X-RAY.md is the scaffolding annotation that feeds the audit compliance map 6 × 6 (Links × Valiant-Bürgisser requirements) when the audit run fires.

- **Parent vertex (pvnp)**: `strategy/x-ray/proof-chain/pvnp/X-RAY.md` (written 2026-04-15). VP vs VNP inherits the trinity + fullness machinery from pvnp; L3 and L4 are direct continuous-domain lifts of pvnp L5 and L10/L15. Cross-cuts explicit in pvnp X-RAY §7 bullets (L10 ↔ vp-vs-vnp:L_continuous, L15 ↔ vp-vs-vnp).

- **Sibling (hodge)**: `strategy/x-ray/proof-chain/hodge/X-RAY.md` (written 2026-04-15). VP vs VNP shares the two-route + compound-projection architecture with hodge (L5 ↔ hodge L7; L2 ↔ hodge L6). The three papers (pvnp, hodge, vp-vs-vnp) form a tight RESONANCE / SYMMETRY / operator-algebra sub-cluster.

- **qg5d hub edge**: `strategy/x-ray/proof-chain/qg5d/X-RAY.md` §7 vertex-12 — explicit edge with invariant, branch, and source documented. This X-RAY's L3 connects directly to qg5d Axiom 1 (B1 spectral) via the continuous BC algebra variant.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W_VP-1 Part (a): Continuous BC algebra lift (L3)**: Constructing a continuous BC algebra $\mathcal{A}_{\mathrm{BC}}^{\mathbb{C}}$ over $\mathbb{C}$ that lifts Paper 28's Boolean BC system preserving KMS$_1$ + type III$_1$ + ITPFI structure. Face: RESONANCE, projection: $P_D$, pattern: P4. Status: CONJECTURED. Candidate mechanism: formal adaptation of Connes-Marcolli 2008 GL$_2$-system (arXiv:0801.4631) to the VP/VNP-relevant representation class.

- **G2 — W_VP-1 Part (b): Algebraic fullness criterion (L4)**: Deriving a Houdayer-Marrakchi-analog fullness criterion on the continuous BC algebra of G1. Face: RESONANCE, projection: $P_D$, pattern: P4. Status: OPEN. Depends on G1. Candidate route: lift Paper 28 Part (i) Path B proof strategy (Taylor ⇒ non-full, unconditional) to the continuous-domain setting using continuous-group-action instead of discrete $G_L$.

- **G3 — L5 CANDIDATE: BC-fullness ↔ GCT-Kronecker dictionary**: Formally constructing the dictionary between continuous-BC fullness (L4) and GCT Kronecker-coefficient obstructions (L2). Face: SYMMETRY, projection: $P_D$, pattern: P1. Status: CANDIDATE. Mulmuley 2011 algorithmic conjecture is the GCT-side formulation; the BC-side translation is the framework's novel contribution. Compound-projection structural parallel with hodge L7 ($P_D$ + $P_B$ composition landing in $P_D$).

- **G4 — W_VP-2: Permanent-specific border-complexity obstruction (L6)**: Proving the border-rank super-polynomial lower bound for PER$_n$ via BC-algebraic representation theory. Face: RESONANCE, projection: $P_D$, pattern: P4. Status: OPEN. Depends on G3. Candidate: combine L5 dictionary with 2025 preprint (arXiv:2502.02442) determinant-vs-permanent distinguishing property via BC-algebraic operator-theoretic witness.

- **G5 — Mulmuley-framework bridge (structural)**: Beyond the per-link gaps, the overall claim that "Mulmuley uses Kronecker, the framework uses type III$_1$; same question, different weapons" (paper39 PROOF-CHAIN final line) is itself a research-level structural claim. Whether these perspectives give the same obstruction, complementary obstructions, or independent obstructions is an **open structural question** stated explicitly in paper39 "Comparison with Mulmuley-Sohoni GCT programme" section.

**5 OPEN items** (2 named walls W_VP-1 / W_VP-2 + CANDIDATE-status L5 + 2 structural questions G3 dictionary & G5 framework-GCT relation). **1 of 6 links closed** (L1 LITERATURE). **1 of 6 LITERATURE** (L2 — unconditionally closed but not yet integrated into the framework's chain). **4 of 6 OPEN/CONJECTURED/CANDIDATE** (L3-L6). The confidence 1/10 reflects the genuine early-stage conjecturality — the framework has identified a novel route (continuous BC fullness + GCT bridge) but every link requiring framework work is open research.

---

## §11 Methodology

This X-Ray was produced by the PAC operator in annotation mode per `strategy/x-ray/x-ray-brief.md` (DELTA 3 primitives: READ / ANNOTATE / CITE / CROSS-LINK / CRITIC-ATTACK / ARBITER-DECIDE). Vocabulary is fixed (10 faces paper60, 6 projections paper61, 5 patterns ORA v8, 16 invariants per template). No invention. Every physics-block assignment carries a paper60 / paper61 / paper28 / paper29 / paper39 / ORA v8 / audit-strategy citation.

### §11a Inputs read (per priority order)

1. `strategy/x-ray/x-ray-template.md` (canonical structure)
2. `strategy/x-ray/x-ray-brief.md` (annotation-mode discipline)
3. `strategy/x-ray/proof-chain/ym/X-RAY.md` (reference exemplar; 18-layer CURVATURE-canonical $P_B$-dominant)
4. `strategy/x-ray/proof-chain/pvnp/X-RAY.md` (direct parent; cross-cut bullets L10 ↔ vp-vs-vnp:L_continuous and L15 ↔ vp-vs-vnp explicit)
5. `strategy/x-ray/proof-chain/hodge/X-RAY.md` (structural sibling; two-route compound-projection architecture parallel)
6. `strategy/x-ray/proof-chain/qg5d/X-RAY.md` §7 vertex-12 edge (explicit B1 spectral / continuous BC variant citation)
7. `strategy/proof-chain/vp-vs-vnp/PROOF-CHAIN.md` (live 6-link chain; 2026-04-14 snapshot)
8. `strategy/vp-vs-vnp/00-audit-strategy.md` (COMMUNITY-STANDARD audit strategy)
9. `strategy/vp-vs-vnp/vp-vs-vnp-audit-brief.md` (B_bare / C_bare audit brief; 15-researcher landscape)
10. `integers/paper60-geometry-of-circle/15-` (RESONANCE face — referenced via 00-table-of-contents §15; Face 9 Selberg ¼ "what vibrational frequencies are ALLOWED on the circle")
11. `integers/paper60-geometry-of-circle/12-face-6-symmetry-katz-sarnak.md` (SYMMETRY face — representation-type classification)
12. `integers/paper60-geometry-of-circle/14-face-8-arithmetic-goldbach-twin-primes.md` (ARITHMETIC face — how integers lattice on the circle)
13. `integers/paper61-projections-5d/sections/06-12-the-six-projections.md` Vertex 12 (VP vs VNP primary $P_D$ + secondary $P_B$ GCT bridge)
14. `integers/paper61-projections-5d/sections/29-30-closing-and-appendices.md` Appendix C.1 row 12 (SPECULATIVE status; primary $P_D$ continuous BC fullness; secondary $P_B$ GCT bridge; RESONANCE face)
15. `integers/paper61-projections-5d/sections/19-24-what-this-explains.md` §19 (paper61 §19.5 "PvNP as a projection: Branch D (fullness face)" extending to VP vs VNP via paper61 §19 compound projection framework)
16. `strategy/north-star.md` §0.9 (Projection Discipline) + §0.10 (Vocabulary Canon — "4+1 derivable coordinates" / "M⁵" / "Integers" canonical terms)

### §11b Projection-discipline compliance (§0.9 check)

Every layer's claim is proved using invariants in the corresponding projection's preservation class (paper61 §15.1). Spot checks:

- L1 scaling dimension + gauge class (Valiant p-projections) — preserved under $P_D$ (Branch D classification). ✓
- L2 Galois representation + gauge class (GCT orbit closures + Kronecker) — preserved under $P_B$ (Branch B gauge-bundle). ✓
- L3 C*-algebra structure + ITPFI factor type (continuous BC) — preserved under $P_D$ (Branch D operator-algebra). ✓
- L4 C*-algebra structure + ergodic property (fullness) — preserved under $P_D$. ✓
- L5 C*-algebra structure + Galois representation (dictionary) — preserved under $P_D$ (composition lands here); the $P_B$ → $P_D$ lift through $M^5$ is implicit in the dictionary construction, respecting §0.9 cross-domain discipline. ✓
- L6 C*-algebra structure + scaling dimension (border obstruction) — preserved under $P_D$. ✓

Paper61 §06-12 Vertex 12's "Compound $P_D$" assignment and §29 App C.1 row 12's "primary $P_D$ + secondary $P_B$" both respect projection discipline: no layer uses $P_A$ / $P_C$ / $P_E$ invariants (all absent from the histogram); the $P_B$ ingredient at L2 lifts through $M^5$ to combine with $P_D$ at L5 (compound-projection via the lifting framework of paper61 §15.1).

### §11c Vocabulary canon compliance (§0.10 check)

Where quoting programme terms, canonical forms used: "continuous BC algebra" (not "continuous-BC variant") per paper39 PROOF-CHAIN terminology; "Branch D" / "Branch B" / "$P_D$" / "$P_B$" per paper61 §06-12; "VP vs VNP over ℂ" (not "algebraic P vs NP without domain specification") per audit-strategy §1. "We derive" / "forced by" / "lifts from" used where applicable. No "postulate" language — all claims are derivations or literature citations.

### §11d Critic-attack record summary

Notable arbiter wins per §3 considered-but-rejected notes:

- **L1 face**: ARITHMETIC over SYMMETRY ($S_n$ symmetry-group is present but the load-bearing content is the integer-lattice monomial-expansion classification, paper60 §14).
- **L1 projection**: $P_D$ over $P_O$ (Valiant's theorem could be framed as outer-ring boundary but mechanically L1 is classification infrastructure living in $P_D$).
- **L2 face**: SYMMETRY over ARITHMETIC (Kronecker coefficients are integer-valued but their classification-role is symmetry-group-representation-theoretic).
- **L2 projection**: $P_B$ over $P_D$ (GCT orbit closures construction lives in Branch B gauge / Kähler-moduli side; the obstruction output lands in $P_D$ via L5 dictionary, but L2's mechanical home is $P_B$).
- **L3 face**: RESONANCE over SYMMETRY (BC-semigroup action is symmetric but the LIFT question is resonance-mode / spectral extension).
- **L3 projection**: $P_D$ over $P_O$ (conjectural lift could be argued as outer-ring boundary but mechanically it lives in $P_D$ as Branch D extension).
- **L4 face**: RESONANCE over DYNAMICS (strong-ergodicity is dynamical in spirit but fullness dichotomy statement is resonance-canonical).
- **L5 face**: SYMMETRY over RESONANCE (dictionary between two frameworks is representation-theoretic at the level where L2's Kronecker side meets L4's fullness side).
- **L5 projection**: $P_D$ over $P_B$ (composition LANDING is $P_D$ even though Route I (L2) lives in $P_B$; same logic as hodge:L7).
- **L6 face**: RESONANCE over SYMMETRY (approximative-closure content is resonance-mode at the BC-spectrum boundary; P4 rigidity under approximation is the load-bearing move).

Full critic-attack record and arbiter decisions to be logged at `strategy/x-ray/pac-output/runs/run-NN/vertices/vp-vs-vnp/critic-attacks.md` and `arbiter-decisions.md` when that run fires. This X-RAY.md records only the WINNING assignments.

### §11e Methodological limits

- VP vs VNP PROOF-CHAIN has only 6 links (vs YM 18, hodge 8, pvnp 24) — compactness produces a narrower face / projection histogram; the high cross-cut density (~5.2 per layer) compensates by indicating strong framework-parent dependencies (pvnp, qg5d, hodge).
- Confidence is 1/10 — the lowest of any X-rayed vertex to date. This reflects genuine conjecturality: 4 of 6 links are OPEN / CONJECTURED / CANDIDATE. The X-Ray's role is to annotate structure, not to evaluate correctness.
- No prior decomposition or CCM-verification ledger entry exists for vp-vs-vnp — this X-RAY.md is the scaffolding artifact that feeds those sibling bundles when they launch.
- Paper39 live PROOF-CHAIN has a very terse Link 2 entry (GCT as LITERATURE) — the framework's integration of GCT is explicit at the programme level (paper61 §29 App C.1 row 12 secondary $P_B$) but not yet at the per-link level. The X-Ray uses the paper61 framework-level integration as the authoritative source for L2 physics-block assignments.
- The "continuous BC" terminology is used throughout per paper39 PROOF-CHAIN and paper61 §06-12 Vertex 12; the established literature object is Connes-Marcolli 2008's GL$_2$-system (arXiv:0801.4631), which is identified as the candidate but formal-adaptation work is OPEN.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record and arbiter decisions belong to `strategy/x-ray/pac-output/runs/run-NN/vertices/vp-vs-vnp/` when that run fires.

Notable cross-vertex considerations:

- **Paper61 §06-12 Vertex 12 "Compound $P_D$"**: treated as $P_D$-primary + $P_B$-secondary per paper61 §29 App C.1 row 12. No construction layer assigned to $P_A$ / $P_C$ / $P_E$ / $P_O$. Paper61 §19.5's extension of "PvNP as Branch D fullness face" to VP vs VNP provides the justification for treating fullness as the primary load-bearing invariant across the continuous-domain layers.

- **Parent vertex inheritance (pvnp)**: treated as DIRECT parent. L3 lifts pvnp L5. L4 lifts pvnp L10 / L15 / L22. The continuous-domain structure inherits pvnp's trinity (spectral-geometric-information) via the paper28 draft §2.4 + §3.8 trinity functor explicit in the pvnp X-RAY §7 qg5d cross-cut bullet.

- **L5 ↔ hodge L7 compound-projection parallel**: recorded. Both compose two routes (one $P_B$, one $P_D$) landing in $P_D$ — structural parallel in two-route composition architecture. Framework-level compound-projection machinery (paper61 §19.6) is the shared tool.

- **L1 $P_D$ vs $P_O$**: rejected $P_O$ despite Valiant's 1979 theorem being an outer-ring-equivalent foundation. Mechanically L1 is classification infrastructure living in $P_D$. Contrast with ym:L18 H4 (genuinely $P_O$-canonical for Clay-grade conditional) and pvnp Corollary L16-L23 (explicit $P_O$ for Clay-grade conclusion).

- **Community-standard status (not Clay)**: audit-strategy §1 "Source type: COMMUNITY-STANDARD, Valiant 1979 STOC + Bürgisser 2000 monograph" explicitly distinguishes this vertex from Clay-Millennium vertices. Accordingly, $P_O$ projection is less load-bearing here than in the Clay outer-ring vertices. The 0 / 6 $P_O$ projection count is structurally informative.

---

*End of VP vs VNP X-Ray. Snapshot 2026-04-15. 6 layers annotated. RESONANCE-dominant (3 layers), $P_D$-dominant (5 layers), P1/P4 mixed pattern distribution. Two named walls (W_VP-1, W_VP-2); CANDIDATE-status L5 dictionary as pivot. Confidence 1/10 reflects early-stage conjecturality — 1/6 links closed (L1 Valiant LITERATURE), 1/6 LITERATURE (L2 GCT), 4/6 OPEN/CONJECTURED/CANDIDATE (L3-L6). Direct-parent inheritance from pvnp (5 cross-cuts); structural sibling to hodge (two-route compound-projection architecture); primary qg5d edge via Branch D continuous BC variant (paper61 §25 candidate). The framework's novel contribution is the L5 BC-fullness ↔ GCT-Kronecker dictionary — "Mulmuley uses Kronecker; the framework uses type III$_1$; same question, different weapons" (paper39 PROOF-CHAIN).*

*G Six and Claude Opus 4.6. April 15, 2026.*
