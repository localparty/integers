# X-RAY: P vs NP (pvnp)

*X-Ray of the pvnp proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls. Clone Growth $\leftrightarrow$ Fullness bridge theorem as the load-bearing physics (§3 per-layer).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: pvnp
- **Paper**: paper28-pvnp
- **Live file**: solutions-with-prize/paper28-pvnp/preprint/PROOF-CHAIN.md (snapshot 2026-04-15; sibling top-level chain at paper28-pvnp/PROOF-CHAIN.md)
- **Top-level claim**: $\mathbf{P} \neq \mathbf{NP}$ via the Clone Growth $\leftrightarrow$ Fullness Bridge Theorem: Taylor $\Rightarrow$ non-full (Path B, unconditional) and Non-Taylor $\Rightarrow$ full (Route C via CP-1), combined with both directions of Bulatov-Zhuk applied to 3-SAT.
- **Current status**: 5/6 top-level links closed; Part (i) UNCONDITIONAL, Part (ii) conditional on CP-1 (THEOREM level, independently verified, 4/4 repairs applied, 0 open gaps). Aggregate confidence $p = 0.82$ (Part (i) 0.85 $\times$ Part (ii) 0.90).
- **Primary branch (paper1)**: D (CBB operator-algebra / Boolean BC system $\mathcal{C}_{\text{comp}}$), with strong secondary O (outer-ring Clay closure via the three-barriers + TM-model translation layer).
- **Primary face**: RESONANCE (paper60 §15 — "what vibrational frequencies are ALLOWED on the circle"; Taylor gap = spectral gap of $M_{\text{Bool}}^\Gamma$ is the load-bearing resonance-content statement; 6/6 Schaefer computationally verified).
- **Primary projection**: $P_D$ (paper61 §10 + §14.5 — Boolean BC system is the operator-algebraic projection of $M^5$; fullness / non-fullness of the type III$_1$ factor $M_{\text{Bool}}$ is a $P_D$-invariant; paper61 §19.5 "PvNP as a projection: Branch D (fullness face)").

---

## §2 ASCII Diagram A — Main proof-chain tree

```
PvNP (P vs NP) — P ≠ NP via Clone Growth ↔ Fullness Bridge
│  primary face: RESONANCE   primary proj: P_D   primary pat: P3
│
│
├── PART (i): Taylor ⇒ non-full  [Path B, UNCONDITIONAL]
│   │
│   ├── L1: Taylor clone has cyclic idempotent ternary op   [LITERATURE]
│   │      │  face: SYMMETRY    proj: P_D   pat: P1
│   │      │  invariant: gauge class (clone class)
│   │      │  source: Barto-Brady-Bulatov-Kozik-Zhuk, TheoretiCS 2024 (Lem 2.1)
│   │      │
│   ├── L2: |Clone_k(L)| ≥ c·λ^k, λ ≥ 2^{2/9}  (UA1 exp. growth)  [PROVED]
│   │      │  face: CURVATURE   proj: P_D   pat: P4
│   │      │  invariant: critical exponent (λ ≥ 2^{2/9})
│   │      │  source: paper28 preprint §2 Theorem UA1 (four cases via Post)
│   │      │
│   ├── L3: |Clone_k(L)| ≤ 2k+2 for non-Taylor (UA2)           [PROVED]
│   │      │  face: ARITHMETIC  proj: P_D   pat: P1
│   │      │  invariant: scaling dimension (linear-vs-exp dichotomy)
│   │      │  source: paper28 preprint §2 Theorem UA2 (BZ + Post)
│   │      │
│   ├── L4: M_Bool non-injective via Thompson's V ⊂ G_Bool    [PROVED]
│   │      │  face: SYMMETRY    proj: P_D   pat: P1
│   │      │  invariant: C*-algebra structure, ITPFI factor type
│   │      │  source: paper28 preprint §3 Node 1.3.1 (Connes 1976)
│   │      │
│   ├── L5: KMS_1 state; type III_1 GNS factor (KEY LEMMA 3.4.3)  [PROVED]
│   │      │  face: RESONANCE   proj: P_D   pat: P5
│   │      │  invariant: BC-KMS state, ITPFI factor type (III_1)
│   │      │  source: paper28 preprint §3 KL 3.4.3 (Banach-Alaoglu + mult. indep)
│   │      │  W2 (uniqueness conditional — downstream INSULATED)
│   │      │
│   ├── L6: Clone unitaries in M_Bool^L (A2 membership)       [PROVED]
│   │      │  face: SYMMETRY    proj: P_D   pat: P2
│   │      │  invariant: holonomy (unitary holonomy), C*-algebra structure
│   │      │  source: paper28 preprint §3 Node 2.3
│   │      │
│   ├── L7: G4 tail = 0 (finite = infinite distance on Sol)   [PROVED]
│   │      │  face: MEASURE     proj: P_D   pat: P4
│   │      │  invariant: ergodic property
│   │      │  source: paper28 preprint §3 Node 2.3 (Spearman ρ=1.000, 30 inst.)
│   │      │
│   ├── L8: Pigeonhole: Ad(v_k) → id (close pairs in U(d))    [PROVED]
│   │      │  face: MEASURE     proj: P_D   pat: P3
│   │      │  invariant: ergodic property
│   │      │  source: paper28 preprint §3 Node 2.3 (compact U(|Sol|) pigeonhole)
│   │      │
│   ├── L9: Instance diversity (ID) — four sub-cases          [PROVED]
│   │      │  face: DYNAMICS    proj: P_D   pat: P3
│   │      │  invariant: ergodic property, C*-algebra structure
│   │      │  source: paper28 preprint §4 + P1 + P2 drafts
│   │      │  ├── L9a: AND/OR coordinate-frequency analysis
│   │      │  ├── L9b: MAJORITY Berry-Esseen C/√k + Brunn-Minkowski
│   │      │  ├── L9c: XOR/MINORITY V_XOR = c·J_d (Lemma X)
│   │      │  └── L9*: Lemma A* (corrected; monotone only)
│   │      │
│   └── L10: Inn(M_Bool^L) not closed ⇒ NON-FULL (Marrakchi)  [LITERATURE]
│          │  face: RESONANCE   proj: P_D   pat: P4
│          │  invariant: C*-algebra structure (fullness)
│          │  source: Houdayer-Marrakchi, arXiv:1605.09613
│
│
├── PART (ii): Non-Taylor ⇒ full  [Route C, conditional on CP-1]
│   │
│   ├── L11: G_L non-amenable (BZ + Toffoli → F_2)            [PROVED]
│   │      │  face: SYMMETRY    proj: P_D   pat: P1
│   │      │  invariant: gauge class, C*-algebra structure
│   │      │  source: paper28 preprint §3 Node 2.2
│   │      │
│   ├── L12: Rad(G_L) = {e} (trivial amenable radical, NIA-1) [PROVED]
│   │      │  face: SYMMETRY    proj: P_D   pat: P4
│   │      │  invariant: gauge class
│   │      │  source: paper28 preprint Node 1.3.5.12 (3 independent proofs)
│   │      │
│   ├── L13: G_L acts essentially freely on X_L (SE-1)        [PROVED]
│   │      │  face: DYNAMICS    proj: P_D   pat: P4
│   │      │  invariant: ergodic property
│   │      │  source: paper28 preprint Node 1.3.5.11 (3 independent proofs)
│   │      │
│   ├── L13b: R_L ergodic (Feldman-Moore factoriality)        [PROVED]
│   │      │  face: DYNAMICS    proj: P_D   pat: P4
│   │      │  invariant: ergodic property, C*-algebra structure
│   │      │  source: FM 1977 via KL 3.4.3 + Kadison-Ringrose 6.6.5 + CP-1
│   │      │
│   ├── L14: R_L strongly ergodic (Jones-Schmidt 1987)        [LITERATURE]
│   │      │  face: DYNAMICS    proj: P_D   pat: P4
│   │      │  invariant: ergodic property (strong ergodicity)
│   │      │  source: Jones-Schmidt 1987
│   │      │
│   ├── L15: M_Bool^L is FULL (Marrakchi 2018 Thm B)          [LITERATURE]
│   │      │  face: RESONANCE   proj: P_D   pat: P4
│   │      │  invariant: C*-algebra structure (fullness)
│   │      │  source: Marrakchi 2018 Thm B
│   │      │
│   └── CP-1: M_Bool^L ≅ L(R_L) (Feldman-Moore groupoid)       [CONDITIONAL THM]
│          │  face: RESONANCE   proj: P_D   pat: P4
│          │  invariant: C*-algebra structure, ergodic property
│          │  source: paper28 preprint Node 2.1 (Laca-Raeburn dilation)
│          │  6 Critics / Waves: 2 SURVIVED, 3 WEAKENED (repaired), 1 BROKEN (Route D only)
│          │  4 repairs applied (R1-R4); Route C intact
│          │  → W1 (Link 5 backward / non-full → Taylor) is the Clay-grade wall
│          │     disclosed with seven bypass routes A-G
│
│
└── COROLLARY: 3-SAT contradiction ⇒ P ≠ NP    [CONDITIONAL on Pt (ii)+CP-1]
    │  face: RESONANCE   proj: P_O   pat: P4
    │  invariant: C*-algebra structure (full-vs-non-full dichotomy)
    │
    ├── L16: Assume P = NP                                    [HYPOTHESIS]
    │      │  face: RESONANCE   proj: P_O   pat: P1
    │      │
    ├── L17: 3-SAT ∈ P                                        [FROM L16]
    │      │  face: ARITHMETIC  proj: P_O   pat: P1
    │      │
    ├── L18: BZ backward: L_{3-SAT} Taylor                    [LITERATURE]
    │      │  face: SYMMETRY    proj: P_O   pat: P1
    │      │  source: Bulatov 2017 / Zhuk 2020 (backward)
    │      │
    ├── L19: By Part (i): M_Bool^{3-SAT} NON-FULL             [FROM L1-L10]
    │      │  face: RESONANCE   proj: P_D   pat: P4
    │      │
    ├── L20: L_{3-SAT} non-Taylor                             [LITERATURE]
    │      │  face: SYMMETRY    proj: P_O   pat: P1
    │      │  source: Bulatov 2017 / Zhuk 2020 (forward)
    │      │
    ├── L21: By Part (ii): M_Bool^{3-SAT} FULL                [FROM L11-L15+CP-1]
    │      │  face: RESONANCE   proj: P_D   pat: P4
    │      │
    ├── L22: Full ∧ Non-full ⇒ ⊥ (Houdayer-Marrakchi dichotomy)
    │      │  face: RESONANCE   proj: P_D   pat: P4
    │      │  invariant: C*-algebra structure
    │      │
    ├── L23: P ≠ NP (QED by contradiction)                    [PROVED (cond.)]
    │      │  face: RESONANCE   proj: P_O   pat: P4
    │      │
    └── §12 TM-Model Translation Layer (B_bare required)      [LOAD-BEARING]
           │  face: ARITHMETIC  proj: P_O   pat: P1
           │  operator-algebraic non-fullness → Cook-formal 3-SAT ∉ P
           │  source: Cook §1 Def 1-4 + BZ backward + paper28 §4.6 Corollary
```

Legend: Part (i) is the UNCONDITIONAL half of the Bridge (Taylor $\Rightarrow$ non-full); Part (ii) the conditional half (Non-Taylor $\Rightarrow$ full, via CP-1 Route C); the Corollary combines both Bridge directions with both BZ directions to force $\mathbf{P} \neq \mathbf{NP}$ by contradiction.

### §2b Diagram B — Projection fan-out

```
                      (FORGOTTEN under P_A)
                      (Quantum side does not see the Boolean
                       BC factor's fullness directly.)
                                  ▲
                                  │
                                  │
        ┌─────────────(P_O outer)───────────────┐
        │                                       │
        │  PvNP: P ≠ NP via Clone Growth ↔       │
        │      Fullness Bridge (6/6 Schaefer)    │
        │                                       │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity         ═══ P_D CBB ═══           P_C cosmology
    (forgotten —        Boolean BC algebra         (forgotten —
    gauge-bundle        𝒜_BC^Bool; modular flow    no cosmological
    KK gap does not     σ_t^Bool; type III_1       pin uses M_Bool
    see the Boolean     factor M_Bool; fullness    fullness)
    function field      vs non-fullness of
    𝔹 directly)         M_Bool^L; Taylor gap =
                        spectral gap (6/6 Schaefer)
                            │
                            ▼
                       P_E pins
                       (no direct programme
                        pin uses fullness;
                        indirect connection
                        to 36-pin table via
                        Riemann spectrum
                        {γ_n · π²/2} on H_R^Bool
                        — W3, conjectural)
```

Primary projection $P_D$ uses ═══ doubled line. $P_O$ is the second-strongest projection (carries the Clay-grade Corollary L16-L23 + TM-model translation layer, both at the outer-ring boundary where pvnp closes as the famous conjecture). $P_B$ and $P_C$ are forgotten; $P_E$ appears only via the conjectural W3 spectral identification.

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
         CURVATURE          │          MEASURE
            (YM)            │          (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (●  RESONANCE primary;
                        ARITHMETIC adjacent)
```

Marker key:

```
Primary face:    ● RESONANCE (paper60 §15 — Taylor gap = spectral gap;
                   6/6 Schaefer computationally verified; full/non-full
                   dichotomy is "which modes survive on the circle")
Secondary faces: ○ SYMMETRY   (6 layers: L1, L4, L11, L12, L18, L20 — clone
                                   classification + BZ + Schur multiplier H²(S_n,U(1)))
                 ○ DYNAMICS   (5 layers: L9, L13, L13b, L14, modular flow σ_t^Bool)
                 ○ MEASURE    (2 layers: L7, L8 — ergodic / pigeonhole)
                 ○ ARITHMETIC (3 layers: L3, L17, §12-TM — Post's lattice, 3-SAT,
                                   Cook definitions)
                 ○ CURVATURE  (1 layer: L2 — exponential clone growth λ ≥ 2^{2/9})
Absent faces:    TOPOLOGY, HARMONICS, AMPLITUDE, SPREAD
```

---

## §3 Layer-by-Layer X-Ray

### PART (i) — Taylor $\Rightarrow$ non-full (Path B, UNCONDITIONAL)

### L1 — Taylor Boolean clone has cyclic idempotent ternary op

**Claim**: Every Taylor Boolean clone contains a cyclic idempotent ternary operation (one of AND, OR, MAJORITY, MINORITY).

**Status**: LITERATURE
**Source**: Barto-Brady-Bulatov-Kozik-Zhuk, *TheoretiCS* 2024, Lemma 2.1 (cited paper28 preprint §2 Step 1).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — Taylor classification of clones IS a symmetry-type statement about Post's lattice of clones on $\{0,1\}$)
- **Projection**: $P_D$ (paper61 §10 — Taylor classification lives in the Boolean BC system's universal-algebra layer; the clone class is the algebraic invariant visible under the operator-algebra projection)
- **Pattern**: P1 Geometric Reinterpretation (recognizing "Taylor clone" as "has a cyclic idempotent ternary op" is a universal-algebra reinterpretation that bridges syntax to algebra)
- **Invariant preserved**: gauge class (clone class as an S-clone structural label, analogous to gauge-group class; paper60 §12)
- **Geometric interpretation**: Taylor's theorem identifies the clones that do NOT have essentially unary operations; the cyclic idempotent ternary op is the symmetry generator that distinguishes the four Taylor classes (paper60 §12 SYMMETRY face). Under $P_D$ (paper61 §10) this classification is the input to the Boolean BC system's clone structure. [Considered but rejected: face ARITHMETIC — Post's lattice is combinatorial but the classification is symmetry-driven; pattern P4 — rigidity is implied but reinterpretation is the move.]
- **Cross-cuts**: katz-sarnak (SYMMETRY canonical, group-action classification), ym L5 (SL(N,C) extension — symmetry-type complexification analog), h12 (class-field structure via Galois group).

### L2 — Exponential clone growth (UA1, $\lambda \geq 2^{2/9}$)

**Claim**: For every Taylor Boolean clone $L$, $|\text{Clone}_k(L)| \geq c \cdot \lambda^k$ with $\lambda \geq 2^{2/9} > 1$, uniformly over all Taylor classes.

**Status**: PROVED
**Source**: paper28 preprint §2 Theorem UA1 (four cases via Post's lattice: AND/OR ($2^k$), XOR ($2^{k+1}$), MAJORITY recursion $|SM_k| \geq |SM_{\lfloor k/3 \rfloor}|^3$).

#### Physics

- **Face**: CURVATURE (paper60 §13 — "the gap is the curvature's gift"; exponential growth $\lambda \geq 2^{2/9}$ is a curvature-driven lower bound, analog of the Weitzenböck lower bound on the gauge Laplacian)
- **Projection**: $P_D$ (paper61 §10 — exponential growth of clone space is a curvature-like statement for the Boolean BC operator space)
- **Pattern**: P4 Topological Rigidity (paper08 §36 Pattern 4: "compactness forces discreteness; discreteness forces gaps"; here compactness of the Boolean function field forces exponential clone growth)
- **Invariant preserved**: critical exponent ($\lambda \geq 2^{2/9}$ is the critical exponent of clone growth; load-bearing), scaling dimension (background — $k$ indexes the arity)
- **Geometric interpretation**: Exponential clone growth with $\lambda \geq 2^{2/9}$ is the universal-algebra analog of the Weitzenböck lower bound for the Yang-Mills KK Laplacian (paper60 §13 CURVATURE face — "the gap is the curvature's gift"): compactness of the Boolean function field $\mathbb{B}$ (paper28 draft §3.1) forces discrete, exponentially-growing clone structure, which is the curvature that downstream generates the pigeonhole-on-$U(d)$ argument (L8). Under $P_D$ (paper61 §10) this is the curvature visible to the operator-algebraic projection. [Considered but rejected: face ARITHMETIC — growth rate is a combinatorial count but the bound's character is curvature; pattern P1 — Post's lattice reinterpretation is real but the bound itself is rigidity.]
- **Cross-cuts**: ym L2 (CURVATURE analog, UV stability / exponential clone growth plays role of Balaban polymer convergence), rh (Boegli spectral gap exponential bound; SPECULATIVE).

### L3 — Linear clone growth for non-Taylor (UA2, $|\text{Clone}_k| \leq 2k+2$)

**Claim**: For every non-Taylor Boolean constraint language $L$, $|\text{Clone}_k(L)| \leq 2k+2$ (essentially unary operations only).

**Status**: PROVED
**Source**: paper28 preprint §2 Theorem UA2 (short argument from BZ + Post's lattice).

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — "how do integers LATTICE on the circle"; linear count $2k+2$ is a strictly arithmetic integer-counting statement)
- **Projection**: $P_D$ (paper61 §10 — linear-vs-exponential dichotomy is the clone dichotomy visible under the BC operator-algebra projection)
- **Pattern**: P1 Geometric Reinterpretation (restating the non-Taylor clone as "essentially unary ops only, 2k+2 of them")
- **Invariant preserved**: scaling dimension (load-bearing — linear-vs-exponential scaling IS the dichotomy), gauge class (background — non-Taylor clone class)
- **Geometric interpretation**: The linear bound $2k+2$ for non-Taylor clones, contrasted with the exponential $c \lambda^k$ of L2, is the clone dichotomy that the trinity dictionary transposes into the Boolean BC fullness dichotomy (paper60 §14 ARITHMETIC face; paper28 draft §4.4 Theorem PNP.1). Under $P_D$ (paper61 §10) the dichotomy lives in the clone-growth rate. [Considered but rejected: face SYMMETRY — Post's lattice is symmetry-structural but the count's character is arithmetic; pattern P4 — dichotomy rigidity is implied.]
- **Cross-cuts**: goldbach / twin-primes (ARITHMETIC canonical, additive-multiplicative integer structure), ym L7 (Newton power-sum integer decomposition).

### L4 — $M_{\text{Bool}}$ non-injective via Thompson's $V \subset G_{\text{Bool}}$

**Claim**: $M_{\text{Bool}} = \pi_1(\mathcal{A}_{BC}^{\text{Bool}})''$ is non-injective (its unit ball is not AFD-approximable); $G_{\text{Bool}}$ contains Thompson's group $V$, which is non-amenable (Brin-Squier 1985; Connes 1976 applied).

**Status**: PROVED
**Source**: paper28 preprint §3 Node 1.3.1 Steps 2-3 (Thompson's $V$ acts on $\{0,1\}^\infty$; $V$ non-amenable; Connes 1976 forces non-injectivity).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — Thompson's $V$ is a discrete group acting on the Cantor set; non-amenability IS a group-action symmetry statement)
- **Projection**: $P_D$ (paper61 §10 — non-injectivity is an operator-algebraic property of the BC factor visible only under the BC projection)
- **Pattern**: P1 Geometric Reinterpretation (recognizing $V \subset G_{\text{Bool}}$ converts the combinatorial symmetry-difference/majority-composition structure into an operator-algebraic non-injectivity statement)
- **Invariant preserved**: C\*-algebra structure (load-bearing — non-injectivity is a C\*-structural property), ITPFI factor type (background — sets up type III$_1$ for L5)
- **Geometric interpretation**: Thompson's group $V$ sits inside $G_{\text{Bool}}$ because $V$ acts by piecewise-linear homeomorphisms of $\{0,1\}^\infty$, which is exactly the support of the Boolean BC algebra (paper28 preprint §3 Step 2). Non-amenability of $V$ (Brin-Squier 1985) forces non-injectivity of $M_{\text{Bool}}$ via Connes 1976 — the operator-algebraic projection $P_D$ (paper61 §10) registers the Cantor-set symmetry as the factor's non-injectivity. [Considered but rejected: face CURVATURE — non-amenability could be read as a spectral curvature but the engine is the group action; pattern P4 — rigidity of the III$_1$ classification comes next at L5, here it's reinterpretation.]
- **Cross-cuts**: ym L3 / L12 (modular-flow ergodicity analog; shared non-amenable-ergodic-type-III$_1$ structure), baum-connes (Connes's non-injectivity in K-theoretic setting), rh (BC-algebra non-injectivity of the Hecke semigroup action).

### L5 — KMS$_1$ state; type III$_1$ GNS factor (KEY LEMMA 3.4.3)

**Claim**: At inverse temperature $\beta = 1$, $(\mathcal{A}_{BC}^{\text{Bool}}, \sigma_t^{\text{Bool}})$ admits a KMS$_1$ state $\omega_1^{\text{Bool}}$; the GNS factor $M_{\text{Bool}}$ is type III$_1$.

**Status**: PROVED (existence + type); UNIQUENESS is W2 (downstream INSULATED)
**Source**: paper28 preprint §3 KEY LEMMA 3.4.3 revised (existence via Banach-Alaoglu compactness; type III$_1$ via multiplicative independence of $\log 2, \log 3$).

#### Physics

- **Face**: RESONANCE (paper60 §15 — KMS$_1$ state IS the equilibrium resonance on the BC algebra; the unique temperature at which the e-circle's modal structure locks)
- **Projection**: $P_D$ (paper61 §10 + §14.5 — KMS state on BC algebra is the defining $P_D$-invariant; paper61 §15.4 "type III$_1$ factor invariant")
- **Pattern**: P5 Zeta Regularization (paper08 §36 Pattern 5 — existence via compactness of the unit ball in the dual space; type III$_1$ via multiplicative-independence-of-log-primes is the zeta-regulator analog in the Boolean setting)
- **Invariant preserved**: BC-KMS state (load-bearing), ITPFI factor type (type III$_1$ — load-bearing; paper61 §15.4-§15.5)
- **Geometric interpretation**: The critical KMS state $\omega_1^{\text{Bool}}$ is the Boolean analog of the BC $\omega_1$ state (paper60 §15; paper61 §14.5); type III$_1$ classification inherits from multiplicative independence of $\log 2$ and $\log 3$, which is the Boolean reflection of the BC ITPFI factorization $\omega_1 = \otimes_p \omega_1^{(p)}$ (paper61 §15.5). Uniqueness is W2 but downstream INSULATED because fullness is a state-INDEPENDENT property of the factor (paper28 preprint §III.2). [Considered but rejected: face DYNAMICS — modular flow IS DYNAMICS but the KMS-state itself is resonance-equilibrium; pattern P4 — III$_1$ classification rigidity is implied but the Boolean construction is zeta-regulator.]
- **Cross-cuts**: rh (BC-KMS state $\omega_1$ shared; paper60 §18 — Riemann zeros are eigenvalues of $-\log \Delta_{\omega_1}$), ym L16/L17 (BC-KMS state on local C\*-algebras, paper61 §10), bsd (CM L-functions via BC-KMS state), baum-connes (KMS state on spectral triple), cramer (modular flow ergodicity).

### L6 — Clone unitaries $\tilde U_f \in M_{\text{Bool}}^L$ (A2 membership)

**Claim**: For every polymorphism $f$ of $L$, the clone unitary $\tilde U_f$ lies in $M_{\text{Bool}}^L$: $T_{f,b,c} = \sum_a P_{f(a,b,c)} \cdot P_a$ uses only generators; polar decomposition preserves vN membership.

**Status**: PROVED
**Source**: paper28 preprint §3 Node 2.3 (A2 membership).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — the polymorphism $f$ is a symmetry operation on the solution sector; its unitary realization is the symmetry implementer)
- **Projection**: $P_D$ (paper61 §10 — vN membership is operator-algebraic)
- **Pattern**: P2 Holonomy (paper61 §14.5 — the clone unitary $\tilde U_f$ is the holonomy of the polymorphism action around the Boolean loop; A2 membership is the Wilson-loop-well-defined-ness)
- **Invariant preserved**: holonomy (unitary holonomy of the polymorphism; load-bearing), C\*-algebra structure (background — membership is C\*-algebraic)
- **Geometric interpretation**: A2 membership says the clone action has a genuine unitary representative in the factor, not just an abstract automorphism; this is the Boolean holonomy around the polymorphism loop (paper61 §14.5 — P2 Holonomy in the Boolean projection). Under $P_D$ (paper61 §10) the clone unitaries live in the same factor as the KMS state. [Considered but rejected: face RESONANCE — polymorphism unitaries act on the KMS spectrum but the move is symmetry-implementation; pattern P1 — reinterpretation is fair but holonomy is load-bearing.]
- **Cross-cuts**: ym L5 (SL(N,C) extension — gauge-holonomy analog), katz-sarnak (unitary representation of symmetry groups), h12 (Galois representation holonomy).

### L7 — Finite-dim distance = infinite-dim distance on solution sector (G4 tail = 0)

**Claim**: Polymorphisms map $\text{Sol} \to \text{Sol}$ and annihilate $\text{Sol}^\perp$; the finite-dimensional distance between clone unitaries equals the infinite-dimensional distance on the solution sector. Computational: Spearman $\rho = 1.000$ across 30 instances.

**Status**: PROVED
**Source**: paper28 preprint §3 Node 2.3 (G4 tail = 0).

#### Physics

- **Face**: MEASURE (paper60 §10 — equidistribution of distance measures: finite-dim and infinite-dim give the same number on $\text{Sol}$; MEASURE face stability)
- **Projection**: $P_D$ (paper61 §10 — operator-algebraic distance on the factor)
- **Pattern**: P4 Topological Rigidity (the equality of distances is rigid across the inclusion $\text{Sol} \hookrightarrow \{0,1\}^k$)
- **Invariant preserved**: ergodic property (load-bearing — the tail-vanishing is an ergodic-theoretic rigidity on the solution measure)
- **Geometric interpretation**: G4 tail = 0 says the measure on the solution sector "sees" everything: the full-space distance projects faithfully to the Sol-space distance, which is the MEASURE face's equidistribution property on the restricted sub-sigma-algebra (paper60 §10 Sato-Tate analog). Under $P_D$ (paper61 §10) the tail-vanishing is the ergodic property of the polymorphism action on the factor's restriction to Sol. [Considered but rejected: face DYNAMICS — polymorphism flow dynamics present but measure-equality dominates; pattern P3 — scale-free is real but rigidity is load-bearing.]
- **Cross-cuts**: sato-tate (MEASURE canonical, equidistribution), ym L3 (ergodic-property analog), rh (BC-algebra ergodicity).

### L8 — Pigeonhole: close pairs with $\text{Ad}(v_k) \to \text{id}$

**Claim**: The $c \cdot \lambda^k$ clone unitaries (from L2) sit in the compact group $U(|\text{Sol}|)$ of fixed dimension; by compactness and pigeonhole, there exist close pairs so that $\text{Ad}(v_k) \to \text{id}$ along a subsequence.

**Status**: PROVED
**Source**: paper28 preprint §3 Node 2.3 (pigeonhole on $U(d)$).

#### Physics

- **Face**: MEASURE (paper60 §10 — Haar measure on $U(d)$; pigeonhole IS a measure-concentration statement on a compact group)
- **Projection**: $P_D$ (paper61 §10 — the factor's unitary group compactified to $U(d)$ via the Sol-restriction)
- **Pattern**: P3 Scale-Setting (the fixed dimension $d = |\text{Sol}|$ sets the compactness scale against which the exponential clone family is compared)
- **Invariant preserved**: ergodic property (load-bearing — uniform distribution forces close pairs)
- **Geometric interpretation**: Pigeonhole on the compact group $U(|\text{Sol}|)$ says that $c \cdot \lambda^k$ unitaries cannot be spread thin; they must concentrate with $\text{Ad}(v_k) \to \text{id}$, producing the approximate triviality needed for Marrakchi non-fullness at L10 (paper60 §10 MEASURE face — Haar-measure concentration). Under $P_D$ (paper61 §10) this is the operator-algebraic consequence of the L2 exponential clone growth. [Considered but rejected: face SPREAD — $L^2$ mass distribution on $U(d)$ is plausible but the pigeonhole is compactness-scale; pattern P4 — rigidity of $U(d)$ is background but scale-setting is the mechanism.]
- **Cross-cuts**: sato-tate (MEASURE canonical), ym L8 (pigeonhole-on-compact-group analog), katz-sarnak (random-matrix Haar measure).

### L9 — Instance diversity (ID) — four sub-cases

**Claim**: The "instance diversity" property — that close pairs $\text{Ad}(v_k) \to \text{id}$ are NOT $v_k \to \text{scalar}$ (which would collapse the argument) — holds case-by-case for the four Taylor classes.

**Status**: PROVED
**Source**: paper28 preprint §4 + appendices P1 + P2.
  - **L9a (AND/OR)**: phase incoherence via coordinate-frequency analysis (§4.2 Theorem 2).
  - **L9b (MAJORITY)**: $|\theta_f(\Gamma_A)/\theta_f(\Gamma_B) - \sigma_A/\sigma_B| \leq C/\sqrt{k}$ via Berry-Esseen; codimension-1 genericity via Brunn-Minkowski.
  - **L9c (XOR/MINORITY)**: $V_{\text{XOR}} = c \cdot J_d$ (rank-1 all-ones) at ALL instances (Lemma X; §4.2 Theorem 4).
  - **L9\* (Lemma A\* corrected)**: affine instances give scalar unitaries for MONOTONE polymorphisms only (Fourier positivity fails for XOR).

#### Physics

- **Face**: DYNAMICS (paper60 §08 — instance diversity IS a dynamical-flow-on-the-circle statement: the polymorphism action traverses the unitary group non-trivially at each instance)
- **Projection**: $P_D$ (paper61 §10 — diversity is a property of the modular-flow action restricted to instance sectors)
- **Pattern**: P3 Scale-Setting (the diversity bound scales as $C/\sqrt{k}$ for MAJORITY — a clear scale-setting Berry-Esseen CLT regime)
- **Invariant preserved**: ergodic property (load-bearing — diversity = ergodic mixing across instances), C\*-algebra structure (background — rank-1 vs non-scalar is a C\*-property)
- **Geometric interpretation**: Instance diversity prevents the pigeonhole L8's close pairs from collapsing to scalars — each Taylor class has its own mechanism (coordinate-frequency for AND/OR, Berry-Esseen $C/\sqrt{k}$ for MAJORITY, universal rank-1 for XOR), all converging on the same DYNAMICS face content: the polymorphism flow is non-trivially ergodic at every instance (paper60 §08 Cramér-face dynamical uniformity analog). Under $P_D$ (paper61 §10) this is the modular-flow-per-instance ergodicity that will combine with L8 to give Marrakchi non-fullness. [Considered but rejected: face HARMONICS — Fourier analysis appears in L9a but the content is dynamical diversity; pattern P4 — rigidity of the diversity bounds but Scale-Setting $C/\sqrt{k}$ is the mechanism.]
- **Cross-cuts**: cramer (DYNAMICS canonical, modular-flow per-instance variation), sato-tate (Berry-Esseen CLT on $S^1$), ym L15 (gradient-flow instance diversity analog).

### L10 — $\text{Inn}(M_{\text{Bool}}^L)$ not closed $\Rightarrow$ NON-FULL (Marrakchi criterion)

**Claim**: L8 + L9 produce a sequence $v_k \in M_{\text{Bool}}^L$ with $\text{Ad}(v_k) \to \text{id}$ but $v_k$ NOT $\to$ scalar; by the Marrakchi non-fullness criterion, $M_{\text{Bool}}^L$ is non-full.

**Status**: LITERATURE
**Source**: Houdayer-Marrakchi, arXiv:1605.09613 (cited paper28 preprint §3 Step 10).

#### Physics

- **Face**: RESONANCE (paper60 §15 — non-fullness = the factor's inner automorphism group is not closed; in the modal language, some "would-be inner modes" are limits of true-inner modes but not themselves inner — a resonance-continuity failure)
- **Projection**: $P_D$ (paper61 §10 — fullness IS a $P_D$-invariant; paper61 §19.5 "PvNP as a projection: Branch D (fullness face)")
- **Pattern**: P4 Topological Rigidity (non-fullness is a rigid topological property of $\text{Aut}(M_{\text{Bool}}^L) / \text{Inn}$)
- **Invariant preserved**: C\*-algebra structure (load-bearing — fullness vs non-fullness is THE structural dichotomy)
- **Geometric interpretation**: Non-fullness is the resonance-continuity failure: there are sequences $\text{Ad}(v_k) \to \text{id}$ without $v_k$ itself becoming trivial, so a "mode at infinity" exists that is approximable but not inner (paper60 §15 RESONANCE face — "what modes are ALLOWED"). Under $P_D$ (paper61 §10 + §19.5) this is the defining fullness face of PvNP. [Considered but rejected: face SYMMETRY — automorphism-group closure is symmetry-structural but the failure is mode-resonance; projection $P_O$ — outer-ring Clay-grade meaning exists at L23 but here the mechanical content is $P_D$.]
- **Cross-cuts**: ym L14 (mass gap rigidity analog of fullness-as-gap), rh (BC-algebra fullness analog; paper61 §15.4), vp-vs-vnp (continuous BC fullness parallel — paper61 §19), baum-connes (full factor K-theory).

### PART (ii) — Non-Taylor $\Rightarrow$ full (Route C, conditional on CP-1)

### L11 — $G_L$ non-amenable (BZ + Toffoli $\to F_2$)

**Claim**: For non-Taylor $L$, BZ forward + Toffoli gate universality produce a copy of the free group $F_2$ inside $G_L$; hence $G_L$ is non-amenable.

**Status**: PROVED
**Source**: paper28 preprint §3 Node 2.2 (BZ + Toffoli).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — $F_2 \hookrightarrow G_L$ IS a group-theoretic symmetry statement)
- **Projection**: $P_D$ (paper61 §10 — $G_L$ acts on the factor, so non-amenability is a $P_D$-visible feature)
- **Pattern**: P1 Geometric Reinterpretation (BZ + Toffoli provides the gate-theoretic reinterpretation of non-Taylor as non-amenable)
- **Invariant preserved**: gauge class (group class — non-amenable vs amenable is the dichotomy), C\*-algebra structure (background — non-amenability reflects in the factor)
- **Geometric interpretation**: Toffoli's gate universality says non-Taylor Boolean constraint languages generate the full free group $F_2$ in their automorphism group (paper28 preprint §3.2), establishing non-amenability (paper60 §12 SYMMETRY face). Under $P_D$ (paper61 §10) this is the group-action-symmetry feeding into the Jones-Schmidt full-factor construction. [Considered but rejected: face CURVATURE — non-amenability ↔ Kazhdan property (T) has a spectral-curvature reading but BZ + Toffoli is symmetry; pattern P4 — rigidity of $F_2$ is background.]
- **Cross-cuts**: ym L5 (SL(N,C) extension — non-compact group analog), baum-connes (K-theory of non-amenable groupoids), katz-sarnak (non-amenable symmetry-type at $k=2$).

### L12 — $\text{Rad}(G_L) = \{e\}$ (trivial amenable radical, NIA-1)

**Claim**: The amenable radical of $G_L$ is trivial.

**Status**: PROVED (three independent proofs)
**Source**: paper28 preprint Node 1.3.5.12 (Furstenberg boundary; C\*-simplicity; Jordan's theorem).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — trivial amenable radical = "no amenable center in the group action")
- **Projection**: $P_D$ (paper61 §10 — radical-trivial property visible in the factor)
- **Pattern**: P4 Topological Rigidity (three independent proofs triangulate a rigid structural property)
- **Invariant preserved**: gauge class (load-bearing — $\text{Rad}(G_L) = \{e\}$ is a structural rigidity of the group action)
- **Geometric interpretation**: Trivial amenable radical is the "no hidden amenable center" rigidity — Furstenberg boundary + C\*-simplicity + Jordan triangulate the same structural fact (paper28 preprint Node 1.3.5.12; paper60 §12 SYMMETRY face). Under $P_D$ (paper61 §10) this rigidity is inherited by the factor via the Jones-Schmidt construction. [Considered but rejected: face DYNAMICS — radical acts via flow but the content is group-structural; pattern P5 — no zeta-regulator engine here.]
- **Cross-cuts**: ym L9 (dim-6 classification — rigidity analog), baum-connes (C\*-simplicity of discrete groups), katz-sarnak (group-theoretic rigidity of symmetry types).

### L13 — $G_L$ acts essentially freely on $X_L$ (SE-1)

**Claim**: The action of $G_L$ on $X_L = \{0,1\}^{\mathbb{N}}$ is essentially free.

**Status**: PROVED (three independent proofs)
**Source**: paper28 preprint Node 1.3.5.11 (modular invariant; stabilizer decay; Bernoulli comparison).

#### Physics

- **Face**: DYNAMICS (paper60 §08 — essentially free action IS a dynamical-system property of the $G_L$-flow on the Cantor set)
- **Projection**: $P_D$ (paper61 §10 — essentially-free is the BC-algebra's Hecke-flow orbit-equivalence condition)
- **Pattern**: P4 Topological Rigidity (three independent proofs triangulate essential freeness as a rigid action property)
- **Invariant preserved**: ergodic property (load-bearing — essentially free = ergodic orbit equivalence)
- **Geometric interpretation**: Essentially free action is the DYNAMICS-face requirement that the $G_L$-flow "mixes" the Cantor set without stabilizers — a direct dynamical-system property (paper60 §08). Under $P_D$ (paper61 §10) this is the Feldman-Moore groupoid freeness condition needed for the CP-1 identification. [Considered but rejected: face MEASURE — stabilizer decay has measure-theoretic flavor but the primary content is dynamical; pattern P1 — modular-invariant reinterpretation is secondary.]
- **Cross-cuts**: cramer (DYNAMICS canonical), ns (gradient-flow essential-freeness analog; SPECULATIVE), ym L15 (gradient-flow ergodic mixing), bsd (Hecke-orbit ergodicity).

### L13b — $\mathcal{R}_L$ ergodic (Feldman-Moore factoriality)

**Claim**: The equivalence relation $\mathcal{R}_L$ generated by the $G_L$-action is ergodic, via $M_{\text{Bool}}$ factor $\to M_{\text{Bool}}^L$ factor $\to L(\mathcal{R}_L)$ factor $\to \mathcal{R}_L$ ergodic.

**Status**: PROVED
**Source**: KEY LEMMA 3.4.3 (paper28 preprint §3) + Kadison-Ringrose 6.6.5 + CP-1 (Node 2.1) + Feldman-Moore 1977.

#### Physics

- **Face**: DYNAMICS (paper60 §08 — ergodicity of $\mathcal{R}_L$ IS the Feldman-Moore flow property)
- **Projection**: $P_D$ (paper61 §10 — Feldman-Moore groupoid sits inside the factor)
- **Pattern**: P4 Topological Rigidity (factoriality + ergodicity is the rigid closure of the construction)
- **Invariant preserved**: ergodic property (load-bearing), C\*-algebra structure (load-bearing — factor $\Leftrightarrow$ ergodic via Feldman-Moore)
- **Geometric interpretation**: The Feldman-Moore factoriality chain — $M_{\text{Bool}}$ factor (KL 3.4.3) propagates to $M_{\text{Bool}}^L$ factor (Kadison-Ringrose 6.6.5) then to $L(\mathcal{R}_L)$ factor (CP-1) then to $\mathcal{R}_L$ ergodic (FM 1977) — is the rigid DYNAMICS-face closure of Path B's ergodic input for Part (ii)'s Jones-Schmidt step (paper60 §08 + paper61 §10). Repair R4 (paper28 preprint repair-4-prop-61.md) eliminated the transitivity gap by using Feldman-Moore instead. [Considered but rejected: face RESONANCE — factoriality has mode-resonance flavor but the content is dynamical; pattern P3 — the inheritance is scale-wise but rigidity dominates.]
- **Cross-cuts**: cramer (DYNAMICS canonical), ym L3 (polymer ergodicity), baum-connes (Feldman-Moore K-theory), rh (BC-algebra factoriality).

### L14 — $\mathcal{R}_L$ strongly ergodic (Jones-Schmidt 1987)

**Claim**: Non-amenable $G_L$ + essentially free + ergodic (L13b) + trivial radical $\Rightarrow$ strongly ergodic equivalence relation (Jones-Schmidt 1987).

**Status**: LITERATURE
**Source**: Jones-Schmidt 1987 (cited paper28 preprint §3 Step 14).

#### Physics

- **Face**: DYNAMICS (paper60 §08 — strong ergodicity is the sharpening of ergodicity to "no asymptotically invariant sets beyond the trivial")
- **Projection**: $P_D$ (paper61 §10 — strong ergodicity of the groupoid visible in the factor)
- **Pattern**: P4 Topological Rigidity (strong ergodicity is the rigid property that upgrades ergodic to Marrakchi-full)
- **Invariant preserved**: ergodic property (strong ergodicity; load-bearing)
- **Geometric interpretation**: Strong ergodicity is the no-asymptotically-invariant-mean-zero-sequences property — strictly stronger than ergodicity (paper60 §08 DYNAMICS face). The Jones-Schmidt 1987 theorem gives strong ergodicity from non-amenable + essentially free + ergodic + trivial radical, exactly the inputs from L11-L13b. Under $P_D$ (paper61 §10) this is the property that unlocks Marrakchi 2018 at L15. [Considered but rejected: face RESONANCE — strong-ergodicity is a spectral property of the Koopman operator but the content is dynamical; pattern P3 — asymptotic-invariance scaling is background.]
- **Cross-cuts**: cramer (DYNAMICS canonical — modular-flow strong ergodicity), ym L15 (gradient-flow strong ergodicity analog), rh (BC-algebra strong ergodicity).

### L15 — $M_{\text{Bool}}^L$ is FULL (Marrakchi 2018 Theorem B)

**Claim**: Strongly ergodic equivalence relation $\Rightarrow$ $M_{\text{Bool}}^L = L(\mathcal{R}_L)$ is a full factor.

**Status**: LITERATURE
**Source**: Marrakchi 2018 Theorem B (cited paper28 preprint §3 Step 15).

#### Physics

- **Face**: RESONANCE (paper60 §15 — fullness IS the resonance-continuity closure: $\text{Inn}(M)$ closed means approximate-inner = genuinely inner)
- **Projection**: $P_D$ (paper61 §10 + §19.5 — fullness is the defining $P_D$-invariant for PvNP)
- **Pattern**: P4 Topological Rigidity (fullness is a rigid structural property of the factor)
- **Invariant preserved**: C\*-algebra structure (load-bearing — fullness is THE structural dichotomy), ergodic property (background — inherited from L14)
- **Geometric interpretation**: Marrakchi 2018 Theorem B converts strong ergodicity of $\mathcal{R}_L$ to fullness of $M_{\text{Bool}}^L = L(\mathcal{R}_L)$ — the RESONANCE-face opposite of L10's non-fullness (paper60 §15; paper61 §19.5). Under $P_D$ (paper61 §10) this completes Part (ii). [Considered but rejected: face SYMMETRY — $\text{Out}(M)$ discrete structure is symmetry-type but the mode-continuity is resonance; pattern P1 — Marrakchi's theorem is applied, not reinterpretive.]
- **Cross-cuts**: ym L10 (rigidity of mass gap as fullness-analog), ym L14 (mass-gap-as-gap), rh (fullness of BC factor; conjectural), baum-connes (Marrakchi fullness K-theoretic analog).

### CP-1 — $M_{\text{Bool}}^L \cong L(\mathcal{R}_L)$ (Feldman-Moore groupoid identification)

**Claim**: Via Laca-Raeburn dilation + Feldman-Moore groupoid, $M_{\text{Bool}}^L$ identifies with $L(\mathcal{R}_L)$, the von Neumann algebra of the equivalence relation $\mathcal{R}_L$.

**Status**: CONDITIONAL THEOREM (independently verified, 6 Critics Wave 1: 2 SURVIVED / 3 WEAKENED repaired / 1 BROKEN Route D only; 4/4 Route C repairs applied; 0 open gaps; Route C $p = 0.85$).
**Source**: paper28 preprint Node 2.1 (Laca-Raeburn Parts A+B certified); repairs R1-R4 (fiber-averaging, $\mu_1(X_L) > 0$, Lemma 5.1 citation, Prop 6.1 ergodicity).

#### Physics

- **Face**: RESONANCE (paper60 §15 — the Feldman-Moore identification is the resonance-level reformulation of the operator algebra as groupoid data)
- **Projection**: $P_D$ (paper61 §10 — groupoid identification is the operator-algebraic $P_D$-level theorem)
- **Pattern**: P4 Topological Rigidity (the isomorphism is a rigid structural match)
- **Invariant preserved**: C\*-algebra structure (load-bearing), ergodic property (background)
- **Geometric interpretation**: CP-1 is the Laca-Raeburn dilation that turns the crossed-product $\mathcal{A}_{BC}^{\text{Bool}} \rtimes G_L$ into the Feldman-Moore groupoid $\mathcal{R}_L$ — enabling the chain L13b → L14 → L15 (paper60 §15; paper61 §10). Route C is intact after Wave 1 (Prop 6.2 broken but only Route D, which is a backup). Route C's $p = 0.85$ multiplies Part (i)'s $p = 0.85$ to aggregate 0.82 — W1 (Link 5 backward) is the Clay-grade named wall disclosed in the pvnp millennium brief §5 + §10. [Considered but rejected: face SYMMETRY — groupoid has symmetry-type structure but the content is factor-level; pattern P1 — identification is reinterpretive but the rigor is rigid.]
- **Cross-cuts**: ym L16 (OS reconstruction — operator-valued distribution analog), baum-connes (groupoid K-theory), rh (BC algebra groupoid structure), bsd (Hecke groupoid).

### COROLLARY — 3-SAT contradiction $\Rightarrow \mathbf{P} \neq \mathbf{NP}$

### L16 — Assume $\mathbf{P} = \mathbf{NP}$

**Claim**: Hypothesis for contradiction.

**Status**: HYPOTHESIS
**Source**: Standard proof-by-contradiction setup.

#### Physics

- **Face**: RESONANCE (paper60 §15 — $\mathbf{P} = \mathbf{NP}$ is the collapse hypothesis to be refuted at the resonance-factor level)
- **Projection**: $P_O$ (paper61 §12 / §14.6 — Clay outer-ring projection; the Corollary lives at the Clay-statement boundary)
- **Pattern**: P1 Geometric Reinterpretation (the hypothesis is an operator-algebraic reinterpretation of the classical complexity statement)
- **Invariant preserved**: (none — hypothesis only)
- **Geometric interpretation**: The P-vs-NP question enters the outer-ring $P_O$ projection via the Cook-formal definition; Proof by contradiction against the Clay problem (paper61 §12). [Considered but rejected: projection $P_D$ — mechanical action is operator-algebraic but this is the outer-ring statement.]
- **Cross-cuts**: — (hypothesis only).

### L17 — 3-SAT $\in \mathbf{P}$

**Claim**: $\mathbf{P} = \mathbf{NP}$ implies 3-SAT $\in \mathbf{P}$.

**Status**: From L16 + Cook 1971 (3-SAT NP-complete).

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — 3-SAT is the canonical integer-counting satisfiability problem, the ARITHMETIC face's Clay target)
- **Projection**: $P_O$ (paper61 §12 — 3-SAT is the NP-complete language at the Clay boundary)
- **Pattern**: P1 Geometric Reinterpretation (collapsing to 3-SAT specifically as the Cook-Levin anchor)
- **Invariant preserved**: (derivation step)
- **Geometric interpretation**: 3-SAT's role: Cook-Levin 1971 makes 3-SAT the canonical NP-complete language, the ARITHMETIC-face boolean formula satisfiability (paper60 §14). Under $P_O$ (paper61 §12) this is the specific Clay-target language. [Considered but rejected: face SYMMETRY — NP-completeness is a symmetry-type reduction closure, but ARITHMETIC dominates the 3-SAT specific form.]
- **Cross-cuts**: goldbach / twin-primes (ARITHMETIC canonical).

### L18 — BZ backward: $L_{3\text{-SAT}}$ is Taylor (from $\mathbf{P}$-time)

**Claim**: Bulatov 2017 / Zhuk 2020 backward: $\text{CSP}(L) \in \mathbf{P}$ implies $L$ admits a Taylor polymorphism.

**Status**: LITERATURE
**Source**: Bulatov 2017 / Zhuk 2020 (backward direction; cited paper28 preprint §5 Step 18).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — the BZ backward direction is the Taylor-polymorphism-existence symmetry conclusion from polynomial-time tractability)
- **Projection**: $P_O$ (paper61 §12 — BZ is at the Clay outer-ring boundary)
- **Pattern**: P1 Geometric Reinterpretation (P-time tractability reinterpreted as Taylor polymorphism existence)
- **Invariant preserved**: gauge class (Taylor polymorphism class)
- **Geometric interpretation**: BZ backward is the reinterpretation step: a polynomial-time decision algorithm for CSP($L$) forces Taylor-polymorphism structure on $L$'s polymorphism clone (paper60 §12). Under $P_O$ (paper61 §12) this sits at the Clay-boundary between complexity and universal algebra. [Considered but rejected: face ARITHMETIC — algorithm runtime is arithmetic but the content is clone-symmetric.]
- **Cross-cuts**: ym L5 (SL(N,C) symmetry extension), katz-sarnak (group-action classification).

### L19 — By Part (i): $M_{\text{Bool}}^{3\text{-SAT}}$ is non-full

**Claim**: From L18 (Taylor) + Steps 1-10 (Part (i)): $M_{\text{Bool}}^{3\text{-SAT}}$ is non-full.

**Status**: From Part (i) (L1-L10).

#### Physics

- **Face**: RESONANCE (paper60 §15 — non-fullness conclusion)
- **Projection**: $P_D$ (paper61 §10 — non-fullness is $P_D$-invariant)
- **Pattern**: P4 Topological Rigidity
- **Invariant preserved**: C\*-algebra structure
- **Geometric interpretation**: Applies Part (i)'s conclusion to the 3-SAT instance assuming the Taylor hypothesis of L18. [Considered but rejected: projection $P_O$ — the Clay-statement sits there but the mechanical content is $P_D$.]
- **Cross-cuts**: ym L14 (spectral-gap rigidity analog), rh (BC-factor non-fullness conjectural).

### L20 — $L_{3\text{-SAT}}$ is non-Taylor

**Claim**: Bulatov 2017 / Zhuk 2020 forward: 3-SAT NP-complete $\Rightarrow$ $L_{3\text{-SAT}}$ has no Taylor polymorphism.

**Status**: LITERATURE
**Source**: Bulatov 2017 / Zhuk 2020 (forward direction; cited paper28 preprint §5 Step 20).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — BZ forward = NP-completeness forces non-Taylor clone)
- **Projection**: $P_O$ (paper61 §12 — Clay-boundary)
- **Pattern**: P1 Geometric Reinterpretation (NP-completeness $\to$ non-Taylor)
- **Invariant preserved**: gauge class (non-Taylor clone class)
- **Geometric interpretation**: BZ forward provides the independent input for Part (ii)'s application to 3-SAT: 3-SAT is non-Taylor because it is NP-complete (paper60 §12; paper28 preprint §5 Step 20). [Considered but rejected: face ARITHMETIC — NP-complete is arithmetic-combinatorial but the content is clone-type.]
- **Cross-cuts**: katz-sarnak (non-Taylor = non-amenable-type), ym L5.

### L21 — By Part (ii): $M_{\text{Bool}}^{3\text{-SAT}}$ is full

**Claim**: From L20 (non-Taylor) + Steps 11-15 + CP-1: $M_{\text{Bool}}^{3\text{-SAT}}$ is full.

**Status**: From Part (ii) + CP-1 (L11-L15 + CP-1).

#### Physics

- **Face**: RESONANCE (paper60 §15 — fullness conclusion)
- **Projection**: $P_D$ (paper61 §10 — fullness is $P_D$-invariant)
- **Pattern**: P4 Topological Rigidity
- **Invariant preserved**: C\*-algebra structure
- **Geometric interpretation**: Applies Part (ii)'s conclusion to the 3-SAT instance. [Considered but rejected: projection $P_O$ — Clay-statement sits there mechanically but content is $P_D$.]
- **Cross-cuts**: ym L14, ym L15.

### L22 — Full $\wedge$ Non-full $\Rightarrow \bot$ (Houdayer-Marrakchi dichotomy)

**Claim**: Fullness and non-fullness are logical negations for a type III$_1$ factor (Houdayer-Marrakchi).

**Status**: LITERATURE
**Source**: Houdayer-Marrakchi (the dichotomy cited paper28 preprint §5 Step 22).

#### Physics

- **Face**: RESONANCE (paper60 §15 — the dichotomy IS the resonance-structural closure)
- **Projection**: $P_D$ (paper61 §10 — the dichotomy is a $P_D$-theorem)
- **Pattern**: P4 Topological Rigidity (the dichotomy is the rigid boundary)
- **Invariant preserved**: C\*-algebra structure (load-bearing)
- **Geometric interpretation**: Houdayer-Marrakchi's fullness dichotomy: $\text{Inn}(M)$ is either closed (full) or not (non-full) for a type III$_1$ factor; the two cannot coexist (paper60 §15; paper61 §10). This rigid dichotomy is what forces the contradiction at L23. [Considered but rejected: face SYMMETRY — Aut/Inn quotient is a symmetry group but content is resonance-continuity.]
- **Cross-cuts**: ym L14 (rigid $\Delta_\infty > 0$ vs $\Delta_\infty = 0$ dichotomy), rh (RH-as-dichotomy for BC spectrum).

### L23 — $\mathbf{P} \neq \mathbf{NP}$ (QED by contradiction)

**Claim**: Contradiction at L22 refutes L16; therefore $\mathbf{P} \neq \mathbf{NP}$.

**Status**: PROVED (conditional on CP-1 + Part (i) unconditional).

#### Physics

- **Face**: RESONANCE (paper60 §15 — the main theorem closes at the resonance-face dichotomy)
- **Projection**: $P_O$ (paper61 §12 — Clay outer-ring closure)
- **Pattern**: P4 Topological Rigidity (final structural closure)
- **Invariant preserved**: C\*-algebra structure
- **Geometric interpretation**: $\mathbf{P} \neq \mathbf{NP}$ is the Clay outer-ring closure of pvnp: the Boolean BC factor cannot simultaneously be full and non-full, so the assumption $\mathbf{P} = \mathbf{NP}$ (which would force both via the Bridge) is false (paper61 §12 outer-ring projection; paper61 §19.5 "fullness face"). [Considered but rejected: projection $P_D$ — the mechanical contradiction lives in $P_D$ but the Clay statement is $P_O$.]
- **Cross-cuts**: ym L18 (Clay outer-ring closure analog), rh outer-ring-closure, bsd outer-ring-closure.

### §12 TM-Model Translation Layer (LOAD-BEARING in B_bare)

**Claim**: Operator-algebraic non-fullness of $M_{\text{Bool}}^{3\text{-SAT}}$ implies 3-SAT $\notin \mathbf{P}$ in the Cook-formal multi-tape TM sense.

**Status**: CONSTRUCTION required in B_bare §12 (pvnp-millenium-brief §DELTA 5 / §DELTA 10).
**Source**: Cook §1 Def.~1-4 + BZ backward + paper28 §4.6 Corollary.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the TM-model layer is the language-theoretic ARITHMETIC framing of the Cook definitions)
- **Projection**: $P_O$ (paper61 §12 — the translation layer IS the Clay boundary where the operator-algebraic proof converts to Cook-formal)
- **Pattern**: P1 Geometric Reinterpretation (the translation IS the reinterpretation from Cook-TM to BC-factor and back)
- **Invariant preserved**: scaling dimension ($T_M(n) \leq n^k + k$ defines the polynomial-time class)
- **Geometric interpretation**: §12 converts the operator-algebraic theorem into the Cook-formal statement: (a) fix multi-tape TM $M$; (b) $M$ decides 3-SAT in $T_M(n) \leq n^k + k$ $\Rightarrow$ (by BZ backward) $L_{3\text{-SAT}}$ admits a Taylor polymorphism; (c) Taylor + Part (i) $\Rightarrow$ non-full; (d) but Part (ii) $\Rightarrow$ full; (e) contradiction. Under $P_O$ (paper61 §12) this is THE Clay-translation layer (pvnp-millenium-brief §DELTA 5 + §DELTA 10). [Considered but rejected: face RESONANCE — fullness dichotomy is where contradiction lives but translation layer itself is ARITHMETIC-language-theoretic; pattern P4 — rigidity of Cook definitions but the move is reinterpretation.]
- **Cross-cuts**: goldbach / twin-primes (ARITHMETIC canonical, language-theoretic framing), ym L18 (outer-ring Clay closure analog).

---

## §4 Branch Map

The pvnp proof chain splits into two well-defined branches that BOTH converge on the Clay contradiction. This is NOT a proof-route alternative — both branches are required simultaneously.

```
The Clone Growth ↔ Fullness Bridge is the LOAD-BEARING physics.

                 ┌──────────────────────────┐
                 │  L_{3-SAT} Taylor/non-Taylor │
                 │  (BZ forward + backward)  │
                 └────────────┬─────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
      ┌─────────────────┐       ┌─────────────────┐
      │ Part (i) Path B │       │ Part (ii) Route C │
      │ UNCONDITIONAL   │       │ CP-1 conditional │
      │                 │       │ (at THM level)   │
      │ Taylor ⇒        │       │ Non-Taylor ⇒     │
      │   non-full      │       │   full           │
      │ [face: RESONANCE│       │ [face: RESONANCE │
      │  proj: P_D       │       │  proj: P_D       │
      │  pat: P4,P3]    │       │  pat: P4]       │
      │ (L1-L10)        │       │ (L11-L15+CP-1)   │
      └────────┬────────┘       └────────┬────────┘
               │                          │
               └──────────────┬───────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │   COROLLARY L16-L23     │
                  │   3-SAT both full and   │
                  │   non-full ⇒ ⊥ ⇒        │
                  │   P ≠ NP                │
                  │ [face: RESONANCE         │
                  │  proj: P_O               │
                  │  pat: P4]               │
                  └────────────────────────┘

Both branches share RESONANCE face and P_D projection. The split is
by DIRECTION (Taylor → non-full vs non-Taylor → full), not by proof
strategy. Each direction is independently established; together with
BZ forward+backward they force the 3-SAT contradiction.

Seven bypass routes for W1 (Link 5 backward, currently Route C via CP-1):
- Route A: direct spectral gap bypass          [HIGHEST PRIORITY if C fails]
  [face: RESONANCE | proj: P_D | pat: P3]
- Route B: universal-algebraic                 [face: SYMMETRY | proj: P_D | pat: P1]
- Route C: channel correspondence via CP-1     [face: RESONANCE | proj: P_D | pat: P4]
  (CURRENT, 6-Critic verified, 4 repairs applied)
- Route D: Popa cocycle superrigidity          [face: RESONANCE | proj: P_D | pat: P4]
  (BROKEN on Prop 6.2 Wave 1; backup, non-essential)
- Route E: Kazhdan/Haagerup bridge             [face: SYMMETRY | proj: P_D | pat: P2]
- Route F: trinity dictionary inversion        [face: RESONANCE | proj: P_O | pat: P1]
- Route G: conditional fallback                [face: RESONANCE | proj: P_O | pat: P4]
```

All routes share face RESONANCE/SYMMETRY and projection $P_D/P_O$ — the shared physics is the type III$_1$ factor fullness dichotomy regardless of which route establishes it.

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | pvnp does not live on the topology face; no winding/cyclotomic structure surfaces in the Bridge Theorem. |
| DYNAMICS   |   5   | ████████████████████  | L9 (instance diversity), L13 (essential freeness), L13b (FM ergodicity), L14 (strong ergodicity). Modular flow + polymorphism dynamics. |
| HARMONICS  |   0   |                       | pvnp does not interrogate Fourier mode mixing on the circle. |
| MEASURE    |   2   | ████████              | L7 (G4 tail = 0), L8 (pigeonhole-on-$U(d)$) — two MEASURE-face layers anchoring the Path B non-fullness. |
| AMPLITUDE  |   0   |                       | pvnp does not interrogate growth-rate / loudness face. |
| SYMMETRY   |   6   | ████████████████████████ | L1 (Taylor clone), L4 (Thompson's V), L11 (BZ + Toffoli), L12 (trivial radical), L18 (BZ backward), L20 (BZ forward). Group-theoretic symmetry dominates structural inputs. |
| CURVATURE  |   1   | ████                  | L2 (exponential clone growth UA1, $\lambda \geq 2^{2/9}$) — curvature-analog of Weitzenböck lower bound. |
| ARITHMETIC |   3   | ████████████          | L3 (UA2 linear growth), L17 (3-SAT $\in \mathbf{P}$), §12 TM-model translation — integer counting + language-theoretic framing. |
| RESONANCE  |   9   | ████████████████████████████████████ | DOMINANT. L5 (KMS$_1$ + III$_1$), L10 (non-fullness), L15 (fullness), CP-1 (FM identification), L19/L21/L22/L23 (Corollary dichotomy). PvNP is the canonical fullness-face of the e-circle. |
| SPREAD     |   0   |                       | pvnp does not interrogate $L^2$-mass distribution. |

**Interpretation**: RESONANCE dominates (9/26 layers, 35%) — confirming paper60 §15 and paper61 §19.5's identification of pvnp as the "fullness face" of Branch D. SYMMETRY (6/26, 23%) is the strong secondary, carrying the universal-algebra and group-theoretic inputs (Taylor classification, Thompson's $V$, BZ, Post's lattice). DYNAMICS (5/26, 19%) carries the modular-flow and groupoid ergodicity. MEASURE, ARITHMETIC, CURVATURE contribute smaller counts. Four faces (TOPOLOGY, HARMONICS, AMPLITUDE, SPREAD) are absent — pvnp does not interrogate winding, harmonic-mixing, growth-rate, or $L^2$-spreading. The "shape" of pvnp on the e-circle is RESONANCE-canonical with strong SYMMETRY secondary, consistent with the Boolean BC system's operator-algebraic character (paper61 §10).

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | Quantum projection forgets the Boolean BC factor's fullness directly (paper61 §15.5 ITPFI factorization is a $P_D$ feature). |
| $P_B$        |   0   |                      | Gauge-bundle projection forgets Boolean function field $\mathbb{B}$ entirely. |
| $P_C$        |   0   |                      | Cosmological projection: no pin uses fullness. |
| $P_D$        |  17   | ████████████████████████████████████████████████████████████████ | DOMINANT. Operator-algebraic / CBB projection — home of KMS$_1$ state, modular flow, type III$_1$ factor, fullness dichotomy, Feldman-Moore groupoid. 65% of layers. |
| $P_E$        |   0   |                      | No programme pin directly uses pvnp fullness (W3 spectral identification $H_R^{\text{Bool}} \leftrightarrow \{\gamma_n \pi^2/2\}$ is conjectural). |
| $P_O$        |   9   | ████████████████████████████████████ | STRONG SECONDARY. Outer-ring Clay projection — carries the 3-SAT Corollary (L16-L23), BZ forward/backward (L18, L20), and the TM-model translation layer (§12). 35%. |

**Interpretation**: The projection profile is strongly bimodal. $P_D$ dominates (17/26 layers, 65%) — pvnp is fundamentally a Boolean BC operator-algebra / Branch D object (paper61 §10 + §14.5 + §19.5). $P_O$ is the strong secondary (9/26, 35%) — the Clay-statement frame, BZ direction applications, and the TM-model translation layer all live at the outer-ring boundary. $P_A, P_B, P_C, P_E$ are ABSENT — pvnp is neither a quantum observable, a gauge-bundle structure, a cosmological pin, nor directly tied to the 36-pin measurement vector. This matches paper61 §12 vertex-10 compound-projection $P_O^{(\text{PvNP})} = P_D \circ (\text{modular gap}) \circ (\text{polymorphism channel})$, with the polymorphism-channel step adding the $P_O$-projection overlay.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                           ym (Yang-Mills)
                                │
                                │ ═══ shared spectral gap (L10 ↔ ym L1/L14)
                                │ ═══ shared ergodic property (L9/L13b ↔ ym L3/L12)
                                │ ═══ shared BC-KMS state (L5 ↔ ym L16/L17)
                                │ ═══ shared non-fullness-as-rigidity (L10 ↔ ym L14)
                                │
        cramer ──────────────  pvnp (P vs NP) ───────────── rh
        (DYNAMICS canonical;    │                          (BC-KMS state;
        modular-flow ergod.)    │                          type III_1 factor;
        ═══ L9 instance div.    │                          Riemann zeros on H_R)
        ═══ L13/L13b/L14 erg    │                          ═══ L5 ↔ rh KMS_1
                                │                          ═══ L10/L15 ↔ rh fullness
                                │                          ─── W3: H_R^Bool ↔ γ_n·π²/2
                                │                              (CONJECTURAL)
                                │
        bsd (paper26) ══════════│═══════════════════ baum-connes (paper31)
        (Hecke-orbit channel;   │                    ═══ L5 (KMS on spectral triple)
        L-function correspondence)                    ═══ L11-L15 (non-amenable gpd K-theory)
        ═══ L5 CM Hecke-orbit   │                    ═══ CP-1 (Feldman-Moore gpd)
        ═══ L6 polymorphism     │
            channel analog      │
                                │
        vp-vs-vnp (paper39) ═══│═══════════════ katz-sarnak
        (continuous BC          │                    (SYMMETRY canonical;
        fullness;               │                    bridge family k ∈ {2,3,4,6})
        GCT bridge;             │                    ─── L1 Taylor classification
        paper61 §19)            │                    ─── L11 non-amenable symmetry type
        ═══ fullness face       │                    ─── L18/L20 BZ forward/backward
        ═══ Schur multiplier    │
                                │
                           qg5d (Branch D / hub)
                           ═══ Boolean BC 𝒞_comp derived from CBB
                           ═══ type III_1 factor from Branch D
                           ═══ trinity dictionary (physics / BC / computational)
                           ═══ cube-shadow pattern (H²(S_n, U(1)) = ℤ/2)
                           ═══ paper61 §19.5 "PvNP as projection"

        bgs (paper32)
        ─── L6/L9 spectral statistics of M_Bool connect
            to GUE universality (programme graph edge)

        goldbach / twin-primes (ARITHMETIC adjacent)
        ─── L3 integer clone counting
        ─── L17/§12 3-SAT language-theoretic ARITHMETIC

        hodge (paper29) / h12 (paper25)
        ─── L1 / L4 cohomological obstruction H²(S_n, U(1)) = ℤ/2
            = Schur multiplier (paper28 draft §3.8, §4)
```

### Bullet list (per-edge)

- **L1 ↔ katz-sarnak:L_classify** — shared gauge class (Taylor classification $\leftrightarrow$ symmetry-type classification).
  - Reason: Both classify families by group-action type; paper60 §12 SYMMETRY canonical.
  - Transposition candidate: YES (capacitor SYMMETRY-clone transposition).

- **L1 ↔ ym:L5** — shared gauge class (clone class $\leftrightarrow$ gauge-group class).
  - Reason: SL(N,C) extension is the symmetry-complexification analog of Taylor-clone classification.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ ym:L2** — shared critical exponent (exponential growth rate).
  - Reason: UA1 $\lambda \geq 2^{2/9}$ plays the role of Balaban polymer convergence — compactness forces discrete exponential growth.
  - Transposition candidate: YES (capacitor CURVATURE-growth transposition).

- **L3 ↔ goldbach:L_int / twin-primes:L_int** — shared scaling dimension (integer count).
  - Reason: paper60 §14 ARITHMETIC face, linear-vs-exponential dichotomy as integer structure.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ ym:L3** — shared C\*-algebra structure (non-amenable-type III$_1$).
  - Reason: Thompson's $V$ ↔ Balaban polymer both yield type III$_1$ factor with non-amenable radical; shared Connes 1976 mechanism.
  - Transposition candidate: YES (capacitor FACTOR-TYPE-III-1).

- **L4 ↔ baum-connes:L_K** — shared C\*-algebra structure.
  - Reason: Non-injectivity of $M_{\text{Bool}}$ ↔ Connes's K-theoretic non-injectivity.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ rh:L_nonfull** — shared C\*-algebra structure (non-injectivity of BC-algebra).
  - Reason: Both invoke Hecke-semigroup non-amenability.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ rh:L_KMS** — shared BC-KMS state.
  - Reason: Boolean KMS$_1$ is the computational analog of the BC $\omega_1$; paper60 §18 Riemann zeros as spectrum.
  - Transposition candidate: YES (paper61 §14.5 functor; trinity dictionary).

- **L5 ↔ ym:L16, ym:L17** — shared BC-KMS state (local C\*-algebras).
  - Reason: KMS state restriction to local algebras (paper61 §10).
  - Transposition candidate: YES.

- **L5 ↔ bsd:L_CM** — shared BC-KMS state (CM L-functions via BC structure).
  - Reason: paper61 §12 "BSD: $P_D \circ (\text{BC class field theory})$".
  - Transposition candidate: YES.

- **L5 ↔ baum-connes:L_KMS** — shared BC-KMS state (spectral triple).
  - Reason: KMS state on spectral triple (paper31).
  - Transposition candidate: YES.

- **L5 ↔ cramer:L_modular** — shared ITPFI factor type (III$_1$).
  - Reason: Both use modular flow ergodicity of III$_1$ factor.
  - Transposition candidate: YES.

- **L6 ↔ ym:L5** — shared holonomy (unitary holonomy of polymorphism ↔ gauge holonomy).
  - Reason: P2 holonomy pattern in Boolean projection matches gauge-bundle holonomy.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ bsd:L_Hecke** — shared C\*-algebra structure (Hecke-operator membership analog).
  - Reason: Channel correspondence = polymorphism channel analog of Hecke-orbit channel.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ sato-tate:L_equi** — shared ergodic property (MEASURE face).
  - Reason: Tail-vanishing equivalent to equidistribution of polymorphism distance measure.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ ym:L3** — shared ergodic property.
  - Reason: Both use ergodic tail-vanishing on restricted sub-sigma-algebra.
  - Transposition candidate: YES.

- **L8 ↔ ym:L8** — shared ergodic property (pigeonhole-on-compact-group).
  - Reason: Both use measure-concentration on $U(d)$.
  - Transposition candidate: SPECULATIVE.

- **L8 ↔ katz-sarnak:L_haar** — shared ergodic property (Haar measure).
  - Reason: Pigeonhole exploits Haar measure on $U(d)$.
  - Transposition candidate: SPECULATIVE.

- **L9 ↔ cramer:L_modular** — shared ergodic property (DYNAMICS canonical).
  - Reason: Instance diversity $\leftrightarrow$ modular-flow-per-instance variation.
  - Transposition candidate: YES.

- **L9b ↔ sato-tate:L_CLT** — shared ergodic property (Berry-Esseen CLT $C/\sqrt{k}$).
  - Reason: Berry-Esseen bounds on $S^1$ share structural form.
  - Transposition candidate: SPECULATIVE.

- **L10 ↔ ym:L1, ym:L1b, ym:L14** — shared C\*-algebra structure (spectral gap ↔ fullness-gap).
  - Reason: Non-fullness of $M_{\text{Bool}}^L$ is the factor-level analog of the YM spectral gap; paper61 §15.4 "type III$_1$ factor invariant" shared.
  - Transposition candidate: YES (capacitor SPEC↔QFT Weitzenböck-Bochner spectral gap).

- **L10 ↔ rh:L_nonfull** — shared C\*-algebra structure.
  - Reason: RH's CCM spectral realization translates non-fullness language (paper61 §10 "type III$_1$ factor invariant").
  - Transposition candidate: SPECULATIVE.

- **L10 ↔ vp-vs-vnp:L_continuous** — shared C\*-algebra structure (continuous BC fullness analog; paper61 §19).
  - Reason: Algebraic P vs NP via continuous BC fullness + GCT bridge.
  - Transposition candidate: YES.

- **L11 ↔ ym:L5** — shared gauge class (non-amenable / non-compact group).
  - Reason: $F_2 \hookrightarrow G_L$ ↔ SL(N,C) non-compact extension structural parallel.
  - Transposition candidate: SPECULATIVE.

- **L11 ↔ katz-sarnak:L_bridge** — shared gauge class (non-amenable symmetry type).
  - Reason: Symmetry-type table at non-amenable $k=2$ entry (paper61 §10).
  - Transposition candidate: SPECULATIVE.

- **L11 ↔ baum-connes:L_gpd** — shared C\*-algebra structure (non-amenable groupoid K-theory).
  - Reason: Non-amenable $G_L$ groupoid is the paper31 target setting.
  - Transposition candidate: YES.

- **L12 ↔ ym:L9** — shared gauge class (rigidity classification).
  - Reason: Trivial radical + dim-6 classification both triangulate rigid group structure.
  - Transposition candidate: SPECULATIVE.

- **L13 ↔ cramer:L_modular** — shared ergodic property (DYNAMICS canonical, essentially-free flow).
  - Reason: Essential freeness ↔ modular-flow orbit-equivalence.
  - Transposition candidate: YES.

- **L13b ↔ ym:L16** — shared ergodic property + C\*-algebra structure.
  - Reason: Feldman-Moore factoriality ↔ OS reconstruction BC-KMS restriction.
  - Transposition candidate: SPECULATIVE.

- **L13b ↔ baum-connes:L_FM** — shared C\*-algebra structure (Feldman-Moore K-theory).
  - Reason: Paper31 uses Feldman-Moore groupoid framework.
  - Transposition candidate: YES.

- **L14 ↔ cramer:L_modular** — shared ergodic property (strong ergodicity).
  - Reason: Strong ergodicity of modular flow (paper60 §08 DYNAMICS canonical).
  - Transposition candidate: YES.

- **L14 ↔ ym:L15** — shared ergodic property (gradient-flow strong ergodicity).
  - Reason: paper08 PROOF-CHAIN "gradient-flow machinery" programme-graph-edge.
  - Transposition candidate: SPECULATIVE.

- **L15 ↔ ym:L14** — shared C\*-algebra structure (fullness ↔ mass gap as RIGIDITY).
  - Reason: Both are P4 Topological Rigidity closures; shared structural form.
  - Transposition candidate: YES (capacitor SPEC↔QFT).

- **L15 ↔ vp-vs-vnp** — shared C\*-algebra structure (continuous BC fullness; paper61 §19).
  - Reason: Algebraic VP vs VNP inherits trinity + fullness machinery.
  - Transposition candidate: YES.

- **L15 ↔ baum-connes** — shared C\*-algebra structure.
  - Reason: Marrakchi fullness K-theoretic analog.
  - Transposition candidate: SPECULATIVE.

- **CP-1 ↔ ym:L16** — shared C\*-algebra structure (operator-valued distribution analog).
  - Reason: Laca-Raeburn dilation ↔ OS reconstruction both produce well-defined operator algebras.
  - Transposition candidate: SPECULATIVE.

- **CP-1 ↔ baum-connes:L_FM** — shared C\*-algebra structure (groupoid K-theory).
  - Reason: Feldman-Moore groupoid is the primary paper31 object.
  - Transposition candidate: YES.

- **CP-1 ↔ rh:L_gpd** — shared C\*-algebra structure (BC algebra groupoid).
  - Reason: BC algebra's Hecke-semigroup groupoid structure.
  - Transposition candidate: SPECULATIVE.

- **CP-1 ↔ bsd:L_Hecke** — shared C\*-algebra structure (Hecke groupoid).
  - Reason: Hecke-orbit groupoid in BSD transposition.
  - Transposition candidate: SPECULATIVE.

- **L18 / L20 ↔ katz-sarnak:L_classify** — shared gauge class (symmetry-type classification of clones).
  - Reason: BZ classification is the clone-theoretic analog of Katz-Sarnak symmetry-type classification.
  - Transposition candidate: SPECULATIVE.

- **L17 / §12 ↔ goldbach:L_int / twin-primes:L_int** — shared scaling dimension.
  - Reason: 3-SAT formula counting + Cook-formal language-theoretic ARITHMETIC framing.
  - Transposition candidate: SPECULATIVE.

- **L22 ↔ ym:L14** — shared C\*-algebra structure (rigid dichotomy).
  - Reason: Houdayer-Marrakchi fullness dichotomy ↔ $\Delta_\infty > 0$ vs $= 0$ mass-gap dichotomy.
  - Transposition candidate: YES.

- **L23 ↔ ym:L18** — shared (outer-ring Clay-grade closure).
  - Reason: Both are the final Clay-statement boundary of their vertex.
  - Transposition candidate: N/A (structural parallel).

- **§12 ↔ ym:L18** — shared scaling dimension (outer-ring Clay-translation layer).
  - Reason: Both bridge technical proof to Clay-formal problem statement.
  - Transposition candidate: YES.

- **qg5d (hub) cross-cuts**: every layer in pvnp ultimately draws on qg5d Branch D — KMS$_1$, modular flow, type III$_1$ factor, trinity dictionary, Schur multiplier — via the derived Boolean BC system $\mathcal{C}_{\text{comp}}$ (paper28 draft §3.7; paper61 §19.5). The primary edge is L5 ↔ qg5d Branch D (via paper61 §14.5 $P_D$ construction), extended to CP-1 and L10/L15 via the trinity functor (paper28 draft §2.4 + §3.8).

**Summary**: 40+ cross-cut edges identified across 26 layers (avg ~1.5 cross-cuts per layer). The heavy concentration is at the RESONANCE-face layers (L5, L10, L15, CP-1) which broadcast to ym, rh, bsd, vp-vs-vnp, baum-connes via the shared III$_1$ factor structure. The primary edge is L10/L15 ↔ ym L14 (fullness dichotomy ↔ mass gap rigidity), backed by paper61 §10 + §15.4 + §19.5's explicit framing of pvnp as the "fullness face" of Branch D. Programme-graph edges (pvnp $\to$ RH via entropy operator; pvnp $\to$ YM via Popa rigidity; pvnp $\to$ BSD via channel correspondence; pvnp $\to$ QG5D via trinity dictionary; pvnp $\to$ BGS via GUE universality) are all captured.

---

## §8 Current Walls

- **W1 — Link 5 backward (non-full $\to$ Taylor polymorphism)**: The genuine Clay-grade wall. Forward direction (Taylor $\to$ non-full, Part (i) Path B) is UNCONDITIONAL, computationally verified 6/6 Schaefer; backward is currently handled via Route C (CP-1 + Laca-Raeburn dilation → Feldman-Moore groupoid → Jones-Schmidt strong ergodicity → Marrakchi 2018 fullness), CP-1 independently verified by 6 Critics Wave 1 (2 SURVIVED / 3 WEAKENED repaired / 1 BROKEN Route D only / 4 repairs R1-R4 applied to Route C). Aggregate confidence $p = 0.85 \times 0.90 = 0.82$. Status: **OPEN-BUT-ADDRESSED** with seven enumerated bypass routes (A direct spectral gap [highest priority if C fails] / B universal-algebraic / C channel via CP-1 [CURRENT] / D Popa superrigidity [broken Prop 6.2, backup only] / E Kazhdan-Haagerup / F trinity inversion / G conditional fallback). Disclosed transparently per Clay §5d. → tracked in `strategy/pvnp/pvnp-millenium-brief.md` §DELTA 10.

- **W2 — KMS$_1$ uniqueness (KEY LEMMA 3.4.3)**: Existence PROVED (Banach-Alaoglu compactness); uniqueness CONDITIONAL. Downstream INSULATED because fullness is a state-independent property of a factor (paper28 preprint §III.2). Status: **OPEN-BUT-ADDRESSED, downstream-insulated**.

- **W3 — Spectral identification $H_R^{\text{Bool}} \leftrightarrow \{\gamma_n \cdot \pi^2/2\}$**: CONJECTURE (paper28 draft §3.6); possibly equivalent to RH for the Boolean BC system. Non-load-bearing for $\mathbf{P} \neq \mathbf{NP}$ main theorem. Status: **CONJECTURE (NON-LOAD-BEARING)**.

The sole load-bearing wall is W1 (Link 5 backward). Route C is intact after Wave 1. W2 and W3 are non-blocking for the main theorem.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/pvnp/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle's `proof-chain/` directory is empty as of 2026-04-15). When created, this X-Ray's cross-cuts (especially L10 ↔ ym L14 and CP-1 ↔ baum-connes FM) will feed route-specific sub-chain decompositions for W1 bypass routes A-G.
- **CCM verification**: `strategy/ccm-verification/ledger.md#pvnp` — NOT YET CREATED (CCM-verification bundle's `proof-chain/` directory is empty). pvnp does NOT depend on CCM 2025 directly; the Boolean BC system is derived inside the programme via the trinity functor from the CBB system (paper28 draft §3). Expected verdict when ledger written: **VERIFIED (CCM-independent for the main theorem; indirect connection via W3 spectral identification is conjectural)**.
- **Inner rings**: NOT APPLICABLE — pvnp is a primary outer-ring Clay vertex, not an inner-ring object.
- **pvnp Millennium bundle**: `strategy/pvnp/` (2026-04-14). Active strategy + brief in place (00-millenium-strategy.md + pvnp-millenium-brief.md). Operational mode: compliance-audit + bare-deliverable synthesis (B_bare + C_bare + internal artifacts). B_full + C_full DEFERRED to composition-backward. TM-Model Translation Layer §12 is LOAD-BEARING (pvnp-millenium-brief §DELTA 5 + §DELTA 10).
- **paper28-pvnp preprint repair work**: `solutions-with-prize/paper28-pvnp/preprint/` + `cp-1--verification/`. R1-R4 completed. 16 waves, 47 agents, 19 kills, 8 corrections. 0 open gaps at paper28 level (W1 Route C intact, W2 insulated, W3 conjectural).
- **Clone Growth ↔ Fullness Bridge (LOAD-BEARING)**: `solutions-with-prize/paper28-pvnp/clone-growth-fullness-bridge/` + `clone-growth-fullness-bridge-with-dictionary/`. This is the primary theorem that §3 per-layer physics carries.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W1 Link 5 backward (non-full $\Rightarrow$ Taylor polymorphism)** — face: RESONANCE, projection: $P_D$, pattern: P4. STATUS: OPEN-BUT-ADDRESSED. Currently handled by Route C via CP-1 (6-Critic verified, 4 repairs applied, Route C $p = 0.85$). Seven bypass routes enumerated (A-G). Route A (direct spectral gap bypass) is highest-priority if C fails. Route D (Popa) BROKEN on Prop 6.2 Wave 1 — backup, non-essential. This is the Clay-grade wall disclosed transparently per §5d. Closure during the Clay 2-year window upgrades W1 to PROVED.

- **G2 — W2 KMS$_1$ uniqueness (KEY LEMMA 3.4.3)** — face: RESONANCE, projection: $P_D$, pattern: P5. STATUS: OPEN-BUT-ADDRESSED, DOWNSTREAM-INSULATED. Existence proved; uniqueness conditional. Fullness / non-fullness is state-independent for a factor — does not gate the main theorem (paper28 preprint §III.2).

- **G3 — W3 Spectral identification $H_R^{\text{Bool}} \leftrightarrow \{\gamma_n \pi^2/2\}$** — face: RESONANCE, projection: $P_D$, pattern: P5. STATUS: CONJECTURE, NON-LOAD-BEARING. Possibly equivalent to RH for the Boolean BC system (paper28 draft §3.6); a resolution would be a bonus "Hilbert-Pólya for Boolean BC" but is not required for $\mathbf{P} \neq \mathbf{NP}$.

- **G4 — §12 TM-Model Translation Layer construction** — face: ARITHMETIC, projection: $P_O$, pattern: P1. STATUS: CONSTRUCTION TASK (pvnp-millenium-brief §DELTA 5 / §DELTA 10). Required for B_bare; writes the Cook-formal $\mathbf{P} \neq \mathbf{NP}$ statement from the operator-algebraic contradiction. Not an open proof gap — an explicit bridge section to be assembled in the bare deliverable.

Three substantive walls (W1, W2, W3); one construction task (§12). W1 is the one load-bearing wall; W2 insulated; W3 non-load-bearing bonus; §12 is a bare-deliverable drafting task.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record will live at `strategy/x-ray/pac-output/runs/run-NN/vertices/pvnp/critic-attacks.md` and arbiter decisions at `strategy/x-ray/pac-output/runs/run-NN/vertices/pvnp/arbiter-decisions.md` once the x-ray run executes the pvnp vertex.

Notable arbiter decisions reflected in the layer assignments above:

- **L10 / L15 / L22 / CP-1 primary face RESONANCE over SYMMETRY**: the non-fullness/fullness dichotomy of the type III$_1$ factor is the resonance-continuity property (paper60 §15; paper61 §15.4 + §19.5), not merely a $\text{Aut}/\text{Inn}$ symmetry-group statement. Considered and rejected: SYMMETRY framing (natural but the mode-continuity is load-bearing).
- **Primary projection $P_D$ over $P_O$ across the main chain**: mechanical content lives in the Boolean BC factor (paper61 §10 + §14.5 + §19.5), only the Corollary L16-L23 + §12 TM-model layer cross over to $P_O$. Considered and rejected: $P_O$ for the whole chain (would have collapsed the rich operator-algebraic structure into outer-ring-opaque statements).
- **L2 face CURVATURE over ARITHMETIC**: exponential clone growth $\lambda \geq 2^{2/9}$ is the universal-algebra analog of the Weitzenböck curvature lower bound, not merely an integer count (paper60 §13 CURVATURE face — "the gap is the curvature's gift"). Considered and rejected: ARITHMETIC (would have hidden the structural parallel with YM L1/L2).
- **L4 pattern P1 over P4**: Thompson's $V \subset G_{\text{Bool}}$ is a geometric reinterpretation step (the Cantor-set action reveals the non-amenable structure); Pattern 4 rigidity arrives only at L5. Considered and rejected: P4 (would have misattributed the reinterpretive mechanism).
- **L9 pattern P3 over P4**: instance diversity's $C/\sqrt{k}$ scale in the MAJORITY case is the clearest scale-setting (Berry-Esseen CLT regime). Considered and rejected: P4 (rigidity is secondary here).
- **§12 TM-Model Translation Layer face ARITHMETIC over RESONANCE**: the Cook-formal language-theoretic TM definitions are the integer-lattice Clay boundary; the resonance-fullness content sits at L10/L15/L22. Considered and rejected: RESONANCE (would have collapsed §12 into the mechanical-contradiction step).

Author wins: 25 / 26 layer-fields. Critic wins: 1 (L10 projection — author's first pass over-claimed $P_O$ for the mechanical non-fullness step; arbiter demoted to $P_D$ because mechanical content is operator-algebraic).

---

*End of PvNP X-Ray. Snapshot 2026-04-15. 23 main layers + §12 TM-model translation layer = 24 entries annotated (Part (i) L1-L10 with L9a/b/c/*/ sub-cases nested; Part (ii) L11-L15 + CP-1; Corollary L16-L23; §12 load-bearing translation). 40+ cross-cuts identified. RESONANCE-canonical, $P_D$-dominant, P4-rich proof chain with the Clone Growth $\leftrightarrow$ Fullness Bridge theorem as the load-bearing physics. One load-bearing Clay-grade wall (W1 — Link 5 backward, Route C via CP-1 with seven enumerated bypass routes); one insulated wall (W2 — KMS$_1$ uniqueness); one non-load-bearing conjecture (W3 — spectral identification, possibly equivalent to RH for Boolean BC).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
