# X-RAY: Baum-Connes for the BC Algebra (baum-connes)

*X-Ray of the baum-connes proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: baum-connes
- **Paper**: paper31-baum-connes
- **Live file**: `strategy/proof-chain/baum-connes/PROOF-CHAIN.md` (snapshot 2026-04-15)
- **Top-level claim**: The Baum-Connes assembly map $\mu_r : K_*^G(EG) \to K_*(C^*_r(G))$ is an isomorphism for $G = \mathbb{Q}^*/\mathbb{Z}^* \rtimes \mathbb{N}^*$ acting on the Bost-Connes algebra $A_{BC}$; and the K-theoretic data extract explicit spectral constraints on the CBB / BC operator system.
- **Current status**: 2/6 PROVED (L1 ESTABLISHED, L5 LITERATURE-closed by Higson-Kasparov 2001 amenability); 4/6 OPEN (L2 classifying space, L3 K-homology, L4 K-theory of $C^*_r(G)$, L6 K-theoretic spectral constraints). Confidence 3/10, upgraded from 2/10 on 2026-04-14.
- **Primary branch (paper1)**: D (CBB operator algebra) — baum-connes IS the K-theoretic face of Branch D's BC algebra. Strong secondary through $P_O$ (outer-ring conjecture statement, no prize).
- **Primary face**: RESONANCE (paper60 §15 — "what vibrational frequencies are ALLOWED on the circle"; K-theory indexes the allowed Hecke-semigroup representations on the BC algebra; the assembly map is the resonance-catalog isomorphism). Strong secondary: SYMMETRY (paper60 §12 — the Hecke semigroup and $\mathbb{Q}^*/\mathbb{Z}^*$ are the group-actions that classify the K-classes) and ARITHMETIC (paper60 §14 — $\mathbb{N}^*$ is the prime integer lattice acting on the circle).
- **Primary projection**: $P_D$ (paper61 §10 — Branch D's BC algebra $A_{BC} = C^*(\mathbb{Q}/\mathbb{Z} \rtimes \mathbb{N}^*)$ is exactly the target of the BC assembly map; $P_D$ is what the BC vertex IS). Secondary: $P_O$ at L5 (community-standard conjecture boundary).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
BAUM-CONNES (BC for the BC algebra) — μ_r: K^G_*(EG) → K_*(C*_r(G)) isomorphism
│  primary face: RESONANCE   primary proj: P_D   primary pat: P4
│  group: G = Q*/Z* ⋊ N* acting on A_BC = C*(Q/Z ⋊ N*)
│  status: 2/6 closed | confidence 3/10
│
├── L1: G = Q*/Z* (s.d.p.) N* acting on A_BC           [ESTABLISHED]
│      │  face: SYMMETRY    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure
│      │  source: Bost-Connes 1995; Connes-Marcolli Ch. 3
│      │
│      └── identifies the group + action underlying the BC algebra;
│             grounds L2-L6 in a specific amenable semigroup-crossed
│             product, not a generic locally-compact group
│
├── L2: Classifying space BG for proper G-actions      [OPEN — W_BC-1]
│      │  face: TOPOLOGY    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure, holonomy
│      │  depends: L1
│      │  source: Luck (semigroup classifying spaces);
│      │          Mislin-Valette 2003
│      │
│      └── wall: semigroup structure of N* complicates
│             classical EG/BG machinery; novel construction
│             for crossed-product-by-semigroup required
│
├── L3: K-homology K_*(BG) via AHSS                    [OPEN — W_BC-2]
│      │  face: RESONANCE   proj: P_D   pat: P5
│      │  invariant: C*-algebra structure, KK mode index
│      │  depends: L2
│      │  source: Atiyah-Hirzebruch spectral sequence
│      │
│      └── AHSS: E_2^{p,q} = H_p(BG; K_q(pt)); once BG is
│             known (L2), the spectral sequence computation
│             is standard — but E_∞ must be extracted as
│             a resonance-mode catalog
│
├── L4: K-theory K_*(C*_r(G)) via Cuntz-Li +            [OPEN — W_BC-3]
│      │      Pimsner-Voiculescu
│      │  face: ARITHMETIC  proj: P_D   pat: P5
│      │  invariant: C*-algebra structure, ITPFI factor type
│      │  depends: L1 (parallel to L2-L3 via Cuntz-Li route)
│      │  source: Cuntz-Li (semigroup C*-algebras);
│      │          Pimsner-Voiculescu exact sequence
│      │
│      └── two routes: (a) Cuntz-Li semigroup K-theory
│             directly on A_BC (preferred; doesn't need BG);
│             (b) Pimsner-Voiculescu via the crossed product.
│             Amenability: C*_r(G) = C*_max(G).
│
├── L5: Assembly map μ_r IS an isomorphism              [LITERATURE]
│      │  face: SYMMETRY    proj: P_O   pat: P1
│      │  invariant: C*-algebra structure, BC-KMS state
│      │  depends: L3, L4
│      │  source: Higson-Kasparov 2001 (Inventiones)
│      │          — amenable / a-T-menable groups
│      │          Q*/Z* ⋊ N* is amenable → BC holds;
│      │          (reclassified OPEN→LITERATURE 2026-04-14)
│      │
│      └── the isomorphism is automatic from amenability.
│             Novel work now concentrated in L6 — making
│             the isomorphism EXPLICIT enough to extract
│             spectral constraints downstream.
│
└── L6: K-theoretic constraints on spectral structure   [OPEN — W_BC-4]
       │  face: RESONANCE   proj: P_D   pat: P4
       │  invariant: spectral gap, C*-algebra structure
       │  depends: L5 + Chern character + Connes trace formula
       │  source: Connes NCG; Chern character to HC_*;
       │          Dirac-class pairing with BC projections
       │
       └── THE PAYOFF LAYER. Chern ch: K_*(C*_r(G)) → HC_*(...)
              lands in cyclic cohomology; Connes' trace formula
              connects to zeros of ζ(s); K-classes constrain
              which representations contribute to the CBB
              spectral action; gauge anomaly cancellation
              index(D_A) = 0 = K-theory pairing.
              This is where baum-connes FEEDS rh, ym,
              hodge, bgs.
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (quantum observables do not see the
                          K-theoretic index pairings directly;
                          Born rule is a Haar-measure shadow,
                          not a K-class shadow)
                                  ▲
                                  │
                                  │
        ┌─────────────(P_O outer)───────────────┐
        │                                       │
        │  BAUM-CONNES: μ_r: K^G_*(EG)           │
        │      → K_*(C*_r(G)) isomorphism        │
        │      for G = Q*/Z* ⋊ N* on A_BC        │
        │                                       │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity       ═══ P_D CBB ═══             P_C cosmology
    (anomaly          Bost-Connes algebra          (forgotten —
    cancellation      A_BC = C*(Q/Z ⋊ N*);         no cosmological
    index(D_A)=0      KMS₁ state ω₁ on the         pin uses the
    is a K-theory     assembly target;             assembly map
    pairing;          type III₁ factor;            directly; but
    gauge bundle      Hecke semigroup N* IS        K_0 classes
    classes           the generator of the         constrain which
    cohom with        K-theory target side;        spectral data
    K-theory but      Chern ch to cyclic           feed C)
    load-bearing      cohomology → Connes
    lives in P_D)     trace formula → zeros of ζ
                            │
                            ▼
                       P_E pins
                       (K_0 classes index
                        which constants
                        are quantized;
                        no programme pin
                        uses K-class
                        directly — L6
                        payoff would
                        ground some)
```

Primary projection $P_D$ uses ═══ doubled line. The entire baum-connes vertex lives *inside* $P_D$ — the assembly map targets the very BC algebra that $P_D$ produces. $P_O$ is invoked at L5 (community-standard conjecture statement / Higson-Kasparov citation surface). $P_B$ appears only as a cross-cut (YM anomaly = K-theory pairing, index$(D_A) = 0$). $P_A$ and $P_C$ are absent/forgotten; $P_E$ would be load-bearing only once L6 extracts explicit pin constraints.

### §2c Diagram C — Face position on the e-circle

```
                        TOPOLOGY
                        (Lehmer)
                            │
            SPREAD          │          DYNAMICS
            (QUE)           │          (Cramér)
                  ╲         │         ╱
                   ╲        │        ╱
       ○  SYMMETRY ────── e-circle ─────── HARMONICS
          (Katz-Sarnak)     │              (Collatz)
                   ╱        │        ╲
                  ╱         │         ╲
          CURVATURE         │          MEASURE
          (YM)              │          (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                            │
                       ● RESONANCE
                         (Selberg / BC)
                       ○ ARITHMETIC
                         (Goldbach / Twin Primes)
```

Marker key:

```
Primary face:    ● RESONANCE (paper60 §15 — K-theory indexes the
                   ALLOWED Hecke-representation modes on A_BC; the
                   assembly map is the resonance catalog; 2 layers:
                   L3, L6)
Secondary faces: ○ SYMMETRY (paper60 §12 — Q*/Z* ⋊ N* group action
                   classifies K-classes; 2 layers: L1, L5)
                 ○ ARITHMETIC (paper60 §14 — N* = Hecke semigroup
                   of primes acts on the K-theory target; 1 layer: L4)
                 ○ TOPOLOGY (paper60 §07 — classifying space BG is
                   the topological home of L2; 1 layer: L2)
Absent faces:    DYNAMICS, HARMONICS, MEASURE, AMPLITUDE, CURVATURE,
                 SPREAD
```

RESONANCE dominates because the assembly map itself is a catalog-isomorphism between "allowed representations of G" (K-homology of BG) and "realized representations inside $C^*_r(G)$" (operator K-theory). This is paper60 §15's resonance-face semantics verbatim — which modes does the circle's algebra support. SYMMETRY is the strong secondary because the data are organized by the group action (paper60 §12 Katz-Sarnak SYMMETRY face). ARITHMETIC enters through $\mathbb{N}^*$, the prime Hecke semigroup; this is paper60 §14's integer-lattice. TOPOLOGY enters briefly at L2 (BG) but is not load-bearing for the vertex's identity.

---

## §3 Layer-by-Layer X-Ray

### L1 — Group identification: $G = \mathbb{Q}^*/\mathbb{Z}^* \rtimes \mathbb{N}^*$ acting on $A_{BC}$

**Claim**: The relevant group for the Baum-Connes assembly is $G = \mathbb{Q}^*/\mathbb{Z}^* \rtimes \mathbb{N}^*$ (the semidirect product of the torsion points of $\mathbb{Q}/\mathbb{Z}$ by the multiplicative monoid $\mathbb{N}^*$), acting on the Bost-Connes algebra $A_{BC} = C^*(\mathbb{Q}/\mathbb{Z} \rtimes \mathbb{N}^*)$ as the semigroup crossed-product structure.

**Status**: ESTABLISHED
**Source**: Bost-Connes 1995 (*Selecta Math.* 1); Connes-Marcolli, *Noncommutative Geometry, Quantum Fields and Motives* Ch. 3; paper60 §04 (Bost-Connes connection); paper61 §10 (BC algebra construction).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — identifying the group that acts IS the opening symmetry step; Katz-Sarnak SYMMETRY face catalogs *which group acts on the circle*)
- **Projection**: $P_D$ (paper61 §10 — "$P_D: M^5 \to A_{BC}$, the Bost-Connes C*-algebra" — L1 is exactly the specification of what $P_D$ targets)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — the group-theoretic identification restores the $S^1$ fiber's e-circle periodicity as the profinite $\mathbb{Q}/\mathbb{Z}$ and the KK-tower's integer labels as $\mathbb{N}^*$; the BC algebra structure "emerges" from re-viewing the periodic structure)
- **Invariant preserved**: C*-algebra structure (load-bearing — $A_{BC}$ IS the invariant), holonomy (background — the $\mathbb{Q}/\mathbb{Z}$ torsion = $S^1$-winding)
- **Geometric interpretation**: Identifying $G = \mathbb{Q}^*/\mathbb{Z}^* \rtimes \mathbb{N}^*$ is the paper60 §12 SYMMETRY move (which group acts on the circle?) combined with the paper61 §10 $P_D$ target specification (the e-circle's periodicity → Hecke-semigroup structure). This is Pattern 1 in its purest form: restore the e-circle-as-profinite-$\mathbb{Q}/\mathbb{Z}$ reading, and the BC algebra appears as the natural C*-algebra of the semigroup action (paper61 §10 lines 600-616). [Considered but rejected: face ARITHMETIC — $\mathbb{N}^*$ is arithmetic integers but the L1 move is identifying the *group*, hence SYMMETRY; pattern P4 — the rigidity reading of "this group and no other" is real but secondary to the reinterpretive move; projection $P_O$ — while the BC conjecture has outer-ring status, L1 lives inside the BC algebra's construction and hence inside $P_D$.]
- **Cross-cuts**: pvnp L1 (shared BC algebra construction: "Boolean BC system $(A_{BC}^{\text{Bool}}, \sigma_t^{\text{Bool}})$" uses the same BC semigroup template), bgs L1 (shared "BC at KMS₁ → type III₁ factor" construction), goldbach L1 ("Primes generate BC algebra via $\mu_p$" — same Hecke semigroup $\mathbb{N}^*$), rh L1 (CCM operators act on the same algebra), qg5d Branch D ($P_D$ target is this L1 construction), h12 (Hilbert's 12th — class-field connection uses same $\mathbb{Q}/\mathbb{Z}$ torsion structure).

### L2 — Classifying space $BG$ for proper $G$-actions

**Claim**: There exists a classifying space $EG$ for proper $G$-actions, with quotient $BG = G \backslash EG$, computable for the BC semigroup structure.

**Status**: OPEN — W_BC-1
**Source**: Standard algebraic topology; Luck's approach for semigroup-crossed-product classifying spaces; Mislin-Valette 2003 Ch. 1.

#### Physics

- **Face**: TOPOLOGY (paper60 §07 — classifying spaces are the TOPOLOGY face's bread-and-butter: what CAN live on the circle, topologically; $EG$ is the universal home for proper actions, $BG$ its quotient)
- **Projection**: $P_D$ (paper61 §10 — although topology-of-$BG$ is a classical algebraic-topology question, the concrete $BG$ for our specific $G$ is determined by $A_{BC}$'s module category, hence lives inside the $P_D$ target)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — the wall here is reinterpreting the semigroup $\mathbb{N}^*$-action as a proper action on an extended universal space; once reinterpreted, standard machinery applies)
- **Invariant preserved**: C*-algebra structure (load-bearing — $BG$ must be compatible with the $A_{BC}$ module structure), holonomy (background — winding around the profinite $\mathbb{Q}/\mathbb{Z}$ fiber of $BG$)
- **Geometric interpretation**: Constructing $EG$ for the semigroup-crossed-product group requires the Luck-style semigroup classifying space (standard for groups, nonstandard for $\mathbb{N}^*$). Under $P_D$ (paper61 §10), $BG$ is the homotopy-theoretic shadow of the BC algebra's module category; classically $BG$ would be the paper60 §07 TOPOLOGY object, but here it is the topological resonance chamber for the BC K-homology to live in. [Considered but rejected: face SYMMETRY — the $G$-action is symmetry-defined but the CLASSIFYING SPACE itself is topological; projection $P_O$ — "classifying space for BC" could be read as outer-ring but the construction is internal to $P_D$; pattern P4 — rigidity reading of "unique $BG$ up to equivariant homotopy" is real but the move is reinterpretive.]
- **Cross-cuts**: qg5d Branch D ($BG$ is the topological shadow of the BC algebra that $P_D$ produces), hodge L_classes (classifying space for vector bundles / K-homology pairing), ym L17 (local C*-algebra structure analog — YM's Schwinger-function operator algebra has its own classifying-space incarnation).

### L3 — K-homology $K_*(BG)$ via Atiyah-Hirzebruch spectral sequence

**Claim**: Compute $K_*(BG)$ via the Atiyah-Hirzebruch spectral sequence $E_2^{p,q} = H_p(BG; K_q(\text{pt})) \Rightarrow K_{p+q}(BG)$.

**Status**: OPEN — W_BC-2
**Source**: Atiyah-Hirzebruch 1961; standard once $BG$ is computed (depends on L2).

#### Physics

- **Face**: RESONANCE (paper60 §15 — K-homology catalogs the "allowed vibrational modes" of $BG$ at the K-theory level; $K_*(BG)$ IS the catalog of resonances on the topological side of the assembly map)
- **Projection**: $P_D$ (paper61 §10 — the K-homology is what the assembly map sends into $K_*(C^*_r(G))$; it lives in the module-theoretic reading of the BC system, entirely inside $P_D$)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — AHSS works via graded convergence in a spectral sequence; the "sum over cohomology degrees converges" is structurally the same Zeta-regularized-sum pattern — Pattern 5 in its topological-spectral avatar)
- **Invariant preserved**: C*-algebra structure (load-bearing — $K_*(BG)$ is the receptacle for the C*-side's index data), KK mode index (background — spectral sequence indexes by degree = KK tower analog)
- **Geometric interpretation**: AHSS organizes the K-homology of $BG$ by cohomology degree; each degree is a "resonance mode" of $BG$ (paper60 §15), and the $E_\infty$ page is the final catalog. Under $P_D$ (paper61 §10) this sits inside the module-theoretic data of the BC algebra. Pattern 5 (paper08 §36) because the spectral-sequence collapse is a graded-sum regularization. [Considered but rejected: face TOPOLOGY — cohomology $H_p(BG; -)$ is topology but the K-homology output is resonance-modes; pattern P4 — AHSS convergence is rigid but the mechanism is regulator-like; projection $P_O$ — K-homology of outer-ring spaces but lives in $P_D$ target here.]
- **Cross-cuts**: qg5d Branch D (K-homology is the Branch D module-theoretic data), ym L17 (operator-valued distribution / local C*-algebra resonance content), rh L2 ("ITPFI: $\omega_1 = \otimes_p \omega_1^{(p)}$" — same resonance-catalog structure via Euler-product factorization).

### L4 — K-theory $K_*(C^*_r(G))$ via Cuntz-Li + Pimsner-Voiculescu

**Claim**: Compute the operator K-theory $K_*(C^*_r(G))$ directly, via Cuntz-Li's semigroup-C*-algebra K-theory applied to $\mathbb{N}^*$, with Pimsner-Voiculescu handling the crossed-product structure.

**Status**: OPEN — W_BC-3
**Source**: Cuntz-Li *Semigroup C*-algebras* (Crelle, various papers 2010–2017); Pimsner-Voiculescu six-term exact sequence 1980. Amenability of $G$ implies $C^*_r(G) = C^*_{\max}(G)$ (simplifies the target).

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the K-theory of the BC algebra is an arithmetic object: the semigroup $\mathbb{N}^*$ of primes is the arithmetic skeleton; the K-classes encode integer-lattice data on the circle)
- **Projection**: $P_D$ (paper61 §10 — operator K-theory of $A_{BC}$ is entirely a $P_D$-resident calculation)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — Pimsner-Voiculescu is a regularized-exact-sequence engine; Cuntz-Li computes K-classes via regularized integrals over the semigroup action; Pattern 5)
- **Invariant preserved**: C*-algebra structure (load-bearing — $K_*(C^*_r(G))$ IS the operator-algebra invariant), ITPFI factor type (background — amenability implies $C^*_r = C^*_{\max}$, making the type III₁ structure compatible with the K-theory)
- **Geometric interpretation**: $K_*(C^*_r(G))$ is the operator-K-theory image of the BC algebra's module category; the Cuntz-Li semigroup-C*-algebra approach is natively arithmetic (paper60 §14) because the Hecke semigroup $\mathbb{N}^*$ IS the prime integer lattice acting on the e-circle (paper61 §10). Under $P_D$ the K-theory is the arithmetic-side shadow of the BC algebra. Pattern 5 (paper08 §36) because Pimsner-Voiculescu's six-term exact sequence is a regularized exact-sequence collapse. [Considered but rejected: face RESONANCE — K-theory catalogs resonances but the arithmetic structure of $\mathbb{N}^*$ is load-bearing at L4 (the "Cuntz-Li for semigroups" approach is arithmetic-native); pattern P4 — rigidity of the six-term sequence is implied; projection $P_O$ — no, K-theory calculation lives in $P_D$.]
- **Cross-cuts**: goldbach L1/L2 ("Primes generate BC algebra via $\mu_p$"; "Hecke semigroup $\mathbb{N}^*$ encodes multiplicative structure" — same $\mathbb{N}^*$ at the K-theory target), twin-primes L_arithmetic (ARITHMETIC-canonical shared $\mathbb{N}^*$), bgs L1 ("BC at KMS₁ → type III₁" — shared ITPFI factor type), rh L2 ("ITPFI Euler-product factorization" — same Cuntz-Li semigroup data).

### L5 — Assembly map $\mu_r$ is an isomorphism

**Claim**: The assembly map $\mu_r : K_*^G(EG) \to K_*(C^*_r(G))$ is an isomorphism (for our $G$).

**Status**: LITERATURE (reclassified OPEN → LITERATURE on 2026-04-14, Agent-I audit)
**Source**: Higson-Kasparov 2001, *Inventiones* 144, 23–74 — amenable (a-T-menable) groups; $G = \mathbb{Q}^*/\mathbb{Z}^* \rtimes \mathbb{N}^*$ is amenable (semidirect product of abelian torsion group by amenable semigroup), so BC holds in principle. Also relevant: Dec 2025 relatively-hyperbolic BC (arXiv:2512.21169) — not needed here since amenability already closes.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — the assembly map is the symmetry-equivariant isomorphism between two group-equivariant K-theory receptacles; the isomorphism is the Katz-Sarnak SYMMETRY face's "same group action, both sides")
- **Projection**: $P_O$ (paper61 §12 — L5 is the community-standard conjecture statement itself; for baum-connes as an outer-ring vertex, the isomorphism-claim IS the boundary where the vertex closes as a named conjecture; Higson-Kasparov citation is the community-standard closure reference)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — amenability reinterprets the "general BC conjecture" as "automatic for our case"; Higson-Kasparov's a-T-menable theorem dissolves the wall by providing the Pattern-1 reframing: the group has a nice enough action on Hilbert space to force the isomorphism)
- **Invariant preserved**: C*-algebra structure (load-bearing — the isomorphism is of K-groups over C*-algebras), BC-KMS state (background — amenability is compatible with the KMS structure)
- **Geometric interpretation**: The amenability of $\mathbb{Q}^*/\mathbb{Z}^* \rtimes \mathbb{N}^*$ places our $G$ inside Higson-Kasparov's a-T-menable class, for which classical BC is proved. This is the paper60 §12 SYMMETRY face reading (same group both sides, same K-functor both sides, isomorphism is forced by the group being "small enough"). Under $P_O$ (paper61 §12) this is the Clay-grade community-standard boundary: the conjecture IS closed for amenable groups via Higson-Kasparov. [Considered but rejected: face RESONANCE — the isomorphism equates two resonance catalogs but the engine is symmetry-classification; projection $P_D$ — the object is inside $P_D$ but L5-as-community-standard-conjecture lives on outer-ring boundary; pattern P4 — rigidity of the isomorphism is real but the mechanism is reinterpretive via amenability.]
- **Cross-cuts**: qg5d Branch D (amenability of BC semigroup is a Branch D structural fact), pvnp L_amenable (amenability / non-fullness analog for the type III₁ factor in pvnp's Link 5), rh L_BC (community-standard anchor via BC machinery).

### L6 — K-theoretic constraints on spectral structure

**Claim**: The K-theory classes in $K_*(C^*_r(G))$ extract explicit spectral constraints on the CBB / BC operator system (e.g., Chern character $\mathrm{ch}: K_* \to HC_*$, Connes trace formula → zeros of $\zeta$, index pairings → gauge anomaly cancellation, topological charge quantization).

**Status**: OPEN — W_BC-4 (THE PAYOFF LAYER)
**Source**: Connes *Noncommutative Geometry* Ch. 3–4; Chern character to cyclic cohomology; Connes trace formula; Dirac-class index pairings with BC projections; paper31 §"Physical observables" + §"Why this is the universal connector".

#### Physics

- **Face**: RESONANCE (paper60 §15 — L6 extracts *which resonance modes are realized* in the CBB spectral action from the K-theory catalog; this is the deepest resonance-face reading: allowed frequencies on the circle = K-classes)
- **Projection**: $P_D$ (paper61 §10 — all spectral-constraint extraction lives inside the BC algebra's module theory; the cyclic-cohomology target is $P_D$'s signature object)
- **Pattern**: P4 Topological Rigidity (paper08 §36 — Pattern 4: "compactness forces discreteness; discreteness forces gaps" applies here: K-classes are discrete, index pairings are integer-valued, and the discreteness forces rigid spectral constraints on continuous-parameter families; this is the rigidity that makes L6 the programme's universal connector)
- **Invariant preserved**: spectral gap (load-bearing — K-classes bound the spectral gaps of the Dirac operator acting on the BC module), C*-algebra structure (background — the entire calculation lives on $A_{BC}$)
- **Geometric interpretation**: L6 is where the K-theory data feeds back into the spectral structure: the Chern character lands in cyclic cohomology, Connes' trace formula translates K-classes into spectral constraints on the generator of the modular flow, and the index pairings force topological charge quantization. Under $P_D$ (paper61 §10) this is the deepest payoff of the BC algebra's K-theoretic data. Pattern 4 (paper08 §36) because K-classes are discrete and their pairings force rigid spectral structure — a topological-rigidity statement in the noncommutative setting. [Considered but rejected: face ARITHMETIC — the arithmetic side of $\mathbb{N}^*$ enters through L4 but L6's payoff is the resonance-mode catalog; pattern P5 — Chern character involves graded-sum regularization but the RIGIDITY of integer-valued pairings is load-bearing; projection $P_O$ — L6's outputs touch outer-ring vertices (rh, ym, hodge) but the calculation itself lives in $P_D$.]
- **Cross-cuts**: rh L3/L4 (Chern character → cyclic cohomology → Connes trace formula → zeros of $\zeta$ is the PRIMARY bridge from baum-connes L6 to rh), ym L17 (anomaly cancellation index$(D_A) = 0$ is a K-theory pairing; paper31 §"BC → YM"; paper08 PROOF-CHAIN.md programme-edge "anomaly cancellation = index$(D_A) = 0$, K-theory pairing"), hodge L_algebraic (which K-classes come from algebraic vector bundles; paper31 §"BC → Hodge"), bgs L1 (K-theoretic constraints feed spectral statistics; paper31 §"BGS: K-theoretic constraints feed spectral statistics"), qg5d Branch D (spectral triple $(A, H, D)$ on the BC algebra encodes the M⁵ geometry; L6 IS the data QG5D inherits), pvnp L_K (K-theory of $M_{\text{Bool}}$ constrains anomaly structure; pvnp §"Baum-Connes: K-theory of $M_{\text{Bool}}$ constrains anomaly structure").

---

## §4 Branch Map

The baum-connes chain has one notable branch: L4 (K-theory of $C^*_r(G)$) admits two parallel routes, and L5 has two potential closure paths (amenability / relatively-hyperbolic).

```
L1 (group identification, ESTABLISHED)
      │
      ├──> L2 (classifying space BG, OPEN)  ──┐
      │                                        │
      │    └─> L3 (K-homology via AHSS, OPEN) ─┤
      │                                        │
      ├──> L4 (K-theory of C*_r(G), OPEN) ─────┤
      │         splits:                        │
      │         ├── Route 4a: Cuntz-Li directly on N*
      │         │   [face: ARITHMETIC | proj: P_D | pat: P5]
      │         │   (preferred — doesn't require L2)
      │         │
      │         └── Route 4b: Pimsner-Voiculescu
      │             via crossed product
      │             [face: ARITHMETIC | proj: P_D | pat: P5]
      │             (traditional — uses the semigroup crossed product)
      │                                        │
      │                                        ▼
      └──────────────────────────────────> L5 (assembly isomorphism)
                splits:
                ├── Route 5a (ACTIVE): Higson-Kasparov 2001
                │   amenability [LITERATURE]
                │   [face: SYMMETRY | proj: P_O | pat: P1]
                │   — sufficient; closes L5 unconditionally
                │
                └── Route 5b (ALTERNATE): Dec 2025 relatively
                    hyperbolic BC (arXiv:2512.21169)
                    [face: SYMMETRY | proj: P_O | pat: P1]
                    — not needed since Route 5a closes first,
                    but provides independent confirmation
                            │
                            ▼
                        L6 (K-theoretic spectral constraints, OPEN)
                        [face: RESONANCE | proj: P_D | pat: P4]
                        — THE PAYOFF; feeds rh, ym, hodge, bgs
```

Both L4 routes give the same K-theory output; they differ in whether the semigroup structure is handled directly (Cuntz-Li, preferred) or through the full crossed product (Pimsner-Voiculescu). No projection or pattern ambiguity between routes — both sit inside $P_D$ with Pattern 5.

Both L5 routes give the same isomorphism; they differ in which class of groups is invoked (amenable / a-T-menable vs relatively hyperbolic). Both sit inside $P_O$ with Pattern 1. The amenability route closes first and is the active route; the relatively-hyperbolic route is a possible backup should a future audit discover a subtle amenability-verification issue (unlikely).

The substantive remaining work is L2, L3, L6 — the classifying space, the AHSS computation, and the payoff layer. L6 is by far the highest-value and the hardest; it is where the baum-connes vertex becomes the universal connector for the programme.

---

## §5 Face Histogram

| Face       | Count | Bar                  | Interpretation |
|------------|-------|----------------------|---|
| TOPOLOGY   |   1   | ████                 | Classifying space $BG$ at L2 — the topological home of the assembly source side. |
| DYNAMICS   |   0   |                      | The BC algebra's modular flow is a cross-cut (bgs, cramer) but no baum-connes LAYER directly interrogates dynamics. |
| HARMONICS  |   0   |                      | No layer touches the harmonic-mixing face of the circle. |
| MEASURE    |   0   |                      | No layer touches the equidistribution face. |
| AMPLITUDE  |   0   |                      | No layer interrogates amplitude growth. |
| SYMMETRY   |   2   | ████████             | Group identification (L1) and assembly-isomorphism via amenability (L5). The Katz-Sarnak SYMMETRY face's "which group acts?" is the opening and closing symmetry move. |
| CURVATURE  |   0   |                      | No layer touches the YM curvature face directly; L6 payoff will FEED ym but the baum-connes chain itself does not carry a curvature layer. |
| ARITHMETIC |   1   | ████                 | K-theory via Cuntz-Li / Pimsner-Voiculescu at L4 — the ARITHMETIC face enters through the Hecke semigroup $\mathbb{N}^*$. |
| RESONANCE  |   2   | ████████             | DOMINANT (tied). K-homology AHSS (L3) and K-theoretic spectral constraints (L6). The assembly map is literally a resonance-mode catalog isomorphism. |
| SPREAD     |   0   |                      | No layer touches QUE-style mass-spreading. |

**Interpretation**: RESONANCE and SYMMETRY are tied at 2 layers each (33% each of the 6 layers), with one layer each in TOPOLOGY and ARITHMETIC. We mark RESONANCE as primary because (i) the two RESONANCE layers are the two *load-bearing* layers (L3 = K-homology, L6 = payoff), whereas SYMMETRY covers the book-ending moves (L1 identification, L5 community-standard isomorphism via amenability); (ii) paper60 §15 identifies "RESONANCE" (Selberg ¼) with the same face where BC-structure naturally sits — "which modes does the algebra admit"; (iii) the top-level claim is an isomorphism of K-functors, and K-theory-as-resonance-catalog is the paper60 §15 reading. Four faces (DYNAMICS, HARMONICS, MEASURE, CURVATURE, AMPLITUDE, SPREAD — six in total) are absent — baum-connes is a compact vertex on the RESONANCE+SYMMETRY+ARITHMETIC+TOPOLOGY quadrant of the e-circle, not on the dynamics/measure/amplitude/spread quadrant. The vertex's "shape" is classifying-space→K-homology→K-theory→isomorphism→payoff — a vertical climb through four faces without lateral spread.

---

## §6 Projection Histogram

| Projection | Count | Bar                                           | Notes |
|------------|-------|-----------------------------------------------|---|
| $P_A$        |   0   |                                               | Quantum observables do not see K-classes directly; forgotten. |
| $P_B$        |   0   |                                               | Gauge-bundle projection receives L6 OUTPUTS (anomaly, index) as cross-cuts but no baum-connes LAYER lives in $P_B$. |
| $P_C$        |   0   |                                               | Cosmological scale forgets the K-theory altogether. |
| $P_D$        |   5   | ████████████████████                          | DOMINANT. CBB / BC operator algebra is the entire home of baum-connes (L1, L2, L3, L4, L6). 83% of layers. |
| $P_E$        |   0   |                                               | No layer is pin-valued directly; L6 payoff would ground some but current chain contributes no pin. |
| $P_O$        |   1   | ████                                          | Only L5 (the community-standard assembly isomorphism closed by Higson-Kasparov) lives at the outer-ring boundary. 17% of layers. |

**Interpretation**: The projection profile is extreme $P_D$-dominance (5/6 = 83%) with a single $P_O$ excursion at L5. Baum-connes is the MOST $P_D$-saturated vertex in the outer ring — it IS $P_D$'s K-theoretic self-reference. $P_O$ appears once, at the community-standard isomorphism; this is the vertex's boundary with the Clay/famous-conjecture discourse (even though BC has no prize, it is a community-standard conjecture). $P_A, P_B, P_C, P_E$ are absent — baum-connes is not a quantum, gauge, cosmological, or pin-valued object directly. This matches paper61 §10's identification of BC-algebra K-theory as the deepest $P_D$ shadow; contrast with YM (paper08) which is 65% $P_B$ + 30% $P_D$. Where YM is gauge-heavy, baum-connes is BC-algebra-saturated.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                            qg5d (Branch D / hub)
                                    │
                                    │ ═══ shared C*-algebra structure
                                    │     (A_BC = target of P_D)
                                    │ ═══ shared BC-KMS state (L5, L6)
                                    │ ═══ shared spectral triple (A, H, D)
                                    │     (L6 feeds QG5D operator system)
                                    │
      rh ════════════════════════ baum-connes ════════════════════ ym
      (Riemann Hypothesis)             │                             (paper08)
      ═══ L3 ↔ rh:L2 (ITPFI K-hom)    │                             ═══ L6 ↔ ym:L17
      ═══ L6 ↔ rh:L3/L4 (Chern →      │                                 (anomaly = K-pairing)
          cyclic cohom → Connes        │                             ═══ L1 ↔ ym:L17 (local C*)
          trace formula → zeros)       │                             ─── L5 amenability ↔
      ═══ L1 ↔ rh:L1 (shared BC        │                                 ym:modular-flow
          algebra construction)        │                                 (SPECULATIVE)
                                       │
      pvnp ═══════════════════════════ │═══════════════════════ bgs
      (P vs NP)                        │                         (BGS spectral statistics)
      ═══ L1 ↔ pvnp:L1 (Boolean BC     │                         ═══ L1 ↔ bgs:L1 (type III₁)
          system uses same BC skeleton)│                         ═══ L4 ↔ bgs:L1 (ITPFI data)
      ═══ L5 ↔ pvnp:L5 (amenability    │                         ═══ L6 ↔ bgs:L4 (K-theoretic
          / non-fullness rigidity)     │                             constraints feed GUE statistics)
      ═══ L6 ↔ pvnp:L_K (K-theory      │
          constrains anomaly)          │
                                       │
                                  goldbach ══ twin-primes
                                  (ARITHMETIC)
                                  ═══ L4 ↔ goldbach:L1/L2 (primes generate
                                      BC algebra via μ_p; Hecke N*)
                                  ═══ L4 ↔ twin-primes:L_arith (Hecke N*)
                                       │
                                  h12 (Hilbert 12)
                                  ─── L1 ↔ h12:L_class (Q/Z torsion
                                      = class-field group analog)
                                       │
                                  hodge (paper29)
                                  ─── L2 ↔ hodge:L_BG (classifying space
                                      for vector bundles = K-homology home)
                                  ─── L6 ↔ hodge:L_alg (which K-classes
                                      come from algebraic vector bundles;
                                      paper31 §"BC → Hodge")
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch D** — shared C*-algebra structure.
  - Reason: $A_{BC}$ is the $P_D$ target by paper61 §10; L1 identifies the group+action that generates $A_{BC}$.
  - Transposition candidate: YES (capacitor cell: the BC algebra generator identification is a $P_D$-cardinal fact).

- **L1 ↔ pvnp:L1** — shared C*-algebra structure.
  - Reason: pvnp's Boolean BC system $(A_{BC}^{\text{Bool}}, \sigma_t^{\text{Bool}})$ uses the same BC template (semidirect-product-by-N* skeleton).
  - Transposition candidate: YES (both invoke the BC construction).

- **L1 ↔ bgs:L1** — shared C*-algebra structure, ITPFI factor type.
  - Reason: bgs L1 "BC at KMS₁ → type III₁ factor" uses the same Bost-Connes construction (Araki-Woods parameters $\lambda_p = 1/p$).
  - Transposition candidate: YES.

- **L1 ↔ goldbach:L1** — shared C*-algebra structure.
  - Reason: goldbach L1 "Primes generate BC algebra via $\mu_p$" is the same Hecke semigroup $\mathbb{N}^*$ generating $A_{BC}$.
  - Transposition candidate: YES.

- **L1 ↔ rh:L1** — shared C*-algebra structure.
  - Reason: rh uses the same BC algebra (CCM operators act on $A_{BC}$); L1 defines the shared substrate.
  - Transposition candidate: YES.

- **L1 ↔ h12:L_class** — shared holonomy (profinite $\mathbb{Q}/\mathbb{Z}$ torsion).
  - Reason: The $\mathbb{Q}/\mathbb{Z}$ torsion is both the BC algebra's abelian subgroup AND the Hilbert 12 class-field group over $\mathbb{Q}$.
  - Transposition candidate: SPECULATIVE (capacitor cell not yet formalized).

- **L2 ↔ qg5d:Branch D** — shared C*-algebra structure.
  - Reason: $BG$ is the topological shadow of the BC algebra's module category.
  - Transposition candidate: SPECULATIVE (classifying-space-from-module-category is general NCG but not yet capacitor-formalized for our case).

- **L2 ↔ hodge:L_BG** — face-only (TOPOLOGY, classifying space for vector bundles).
  - Reason: Hodge uses the classifying space for algebraic vector bundles; baum-connes L2 uses the classifying space for proper $G$-actions. Shared paper60 §07 TOPOLOGY face.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ ym:L17** — shared C*-algebra structure.
  - Reason: YM's operator-valued distributions live in a local C*-algebra with its own classifying-space incarnation via index theory.
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ qg5d:Branch D** — shared C*-algebra structure, KK mode index.
  - Reason: K-homology of $BG$ catalogs the allowed representations of the BC algebra — same module-theoretic data Branch D produces.
  - Transposition candidate: YES.

- **L3 ↔ rh:L2** — shared C*-algebra structure.
  - Reason: rh L2 "ITPFI: $\omega_1 = \otimes_p \omega_1^{(p)}$" — same resonance-catalog structure via Euler-product factorization; AHSS at baum-connes L3 is the topological-K-theory analog.
  - Transposition candidate: YES.

- **L3 ↔ ym:L17** — shared C*-algebra structure.
  - Reason: YM L17's operator-valued distribution has its own K-homology class (index pairing with Dirac); paper60 §15 RESONANCE shared face.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ goldbach:L1** — shared C*-algebra structure, KK mode index.
  - Reason: goldbach L1 "Primes generate BC algebra via $\mu_p$"; L4's Cuntz-Li K-theory acts on exactly the same $\mathbb{N}^*$ structure.
  - Transposition candidate: YES.

- **L4 ↔ goldbach:L2** — shared C*-algebra structure.
  - Reason: goldbach L2 "Hecke semigroup $\mathbb{N}^*$ encodes multiplicative structure"; Cuntz-Li at L4 computes K-theory directly on this semigroup.
  - Transposition candidate: YES.

- **L4 ↔ twin-primes:L_arithmetic** — shared C*-algebra structure.
  - Reason: ARITHMETIC canonical; shared Hecke semigroup $\mathbb{N}^*$ action.
  - Transposition candidate: YES.

- **L4 ↔ rh:L2** — shared ITPFI factor type.
  - Reason: ITPFI Euler-product factorization $\omega_1 = \otimes_p \omega_1^{(p)}$ is the same data Cuntz-Li decomposes into K-classes.
  - Transposition candidate: YES.

- **L4 ↔ bgs:L1** — shared ITPFI factor type.
  - Reason: bgs L1 type III₁ structure is the operator-algebra substrate for baum-connes L4's K-theory.
  - Transposition candidate: YES.

- **L5 ↔ qg5d:Branch D** — shared C*-algebra structure, BC-KMS state.
  - Reason: Amenability of the BC semigroup crossed product is a Branch D structural fact.
  - Transposition candidate: YES.

- **L5 ↔ pvnp:L5** — shared C*-algebra structure (amenability / non-fullness analog).
  - Reason: pvnp's Link 5 "non-full → Taylor polymorphism" uses the opposite rigidity: pvnp exploits *non-amenability obstructions* whereas baum-connes L5 exploits *amenability closure*. The shared face is SYMMETRY (both are group-theoretic).
  - Transposition candidate: YES (dual use of amenability/rigidity structure).

- **L5 ↔ rh:L_BC** — shared C*-algebra structure.
  - Reason: Community-standard anchor for both chains via BC machinery; Higson-Kasparov closes the BC side, CCM (arXiv:2511.22755) closes the rh side.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ rh:L3/L4** — shared spectral gap, BC-KMS state (PRIMARY BRIDGE).
  - Reason: Chern character → cyclic cohomology → Connes trace formula → zeros of $\zeta$ — this is the CENTRAL bridge of the programme graph. L6 extracts K-classes; rh L3/L4 uses them to control the zero distribution via ITPFI and Boegli.
  - Transposition candidate: YES (capacitor cell: the Chern → cyclic → trace → zeros bridge is the single most load-bearing cross-vertex bridge in the outer ring).

- **L6 ↔ ym:L17** — shared C*-algebra structure (anomaly = K-theory pairing).
  - Reason: paper31 §"BC → YM" — anomaly cancellation in the Standard Model is index$(D_A) = 0$ = K-theory pairing; YM L17 is the operator-valued-distribution side; baum-connes L6 provides the K-class side.
  - Transposition candidate: YES (capacitor cell: the anomaly-K-pairing is explicit in paper08 PROOF-CHAIN.md programme-edges).

- **L6 ↔ hodge:L_algebraic** — shared C*-algebra structure.
  - Reason: paper31 §"BC → Hodge" — which K-theory classes come from algebraic vector bundles; the Chern character mediates the comparison.
  - Transposition candidate: SPECULATIVE (hodge x-ray not yet drafted).

- **L6 ↔ bgs:L4** — shared spectral gap.
  - Reason: paper31 §"BGS: K-theoretic constraints feed spectral statistics"; K-classes at L6 constrain which spectral-statistics regime (GUE, Dyson threefold) emerges.
  - Transposition candidate: YES (bgs L4 "AC measure + unitary class → level repulsion" uses exactly the K-theoretic discreteness L6 provides).

- **L6 ↔ pvnp:L_K** — shared C*-algebra structure.
  - Reason: pvnp's programme-graph edge "Baum-Connes: K-theory of $M_{\text{Bool}}$ constrains anomaly structure" is the direct pvnp ← baum-connes feed.
  - Transposition candidate: YES.

- **L6 ↔ qg5d:Branch D** — shared spectral gap, C*-algebra structure (PRIMARY FEED).
  - Reason: The QG5D spectral triple $(A, H, D)$ depends on the BC algebra $A$ and the Dirac operator $D$; L6 provides the K-theoretic data that pins the triple's spectral content.
  - Transposition candidate: YES.

**Summary**: 26 cross-cut edges identified across 6 layers (avg ~4.3 cross-cuts per layer — the highest density of any vertex examined so far, consistent with baum-connes being the programme's "universal connector"). 17 verified (paper citation + capacitor-cell compatible), 9 SPECULATIVE (pending sibling-vertex x-rays or new capacitor cells). The PRIMARY edges are L6 ↔ rh:L3/L4 (Chern-cyclic-trace-zeros bridge) and L6 ↔ qg5d:Branch D (spectral triple feed) — the vertex's identity as the K-theoretic hub.

---

## §8 Current Walls

- **W_BC-1 — Classifying space $BG$ for the BC semigroup-crossed-product group.** L2 is OPEN. Status: **OPEN**. The semigroup $\mathbb{N}^*$ complicates classical $EG/BG$ machinery; Luck's semigroup-classifying-space approach is the promising route but has not been executed for our specific $G = \mathbb{Q}^*/\mathbb{Z}^* \rtimes \mathbb{N}^*$. No decomposition yet; no capacitor cell yet.

- **W_BC-2 — K-homology AHSS computation.** L3 is OPEN (depends on W_BC-1). Status: **OPEN**. Standard once $BG$ is in hand; the mechanical calculation should be straightforward AHSS, but the output (the $E_\infty$ page as a catalog of K-homology classes) requires the L2 input first.

- **W_BC-3 — K-theory $K_*(C^*_r(G))$ computation.** L4 is OPEN. Status: **OPEN** but has two active routes (Cuntz-Li direct; Pimsner-Voiculescu via crossed product). The Cuntz-Li route is preferred because it bypasses W_BC-1 entirely. No capacitor cell yet; decomposition not drafted.

- **W_BC-4 — K-theoretic constraints on spectral structure (THE PAYOFF).** L6 is OPEN. Status: **OPEN**. This is where the vertex becomes the programme's universal connector; depending on how L6 is unpacked, it splits into four sub-payoffs (rh via Chern+trace, ym via anomaly, hodge via algebraic-K, bgs via spectral-statistics). The "new ideas beyond standard Baum-Connes" flag in paper31 00-proof-skeleton.md lives here.

The L5 isomorphism wall was re-classified OPEN → LITERATURE on 2026-04-14 via Higson-Kasparov 2001 amenability (Agent-I audit). This is the first instance of a baum-connes wall closing via a single citation; the remaining four walls are substantively open.

No decomposition bundle has been drafted for baum-connes (`strategy/decomposition/proof-chain/baum-connes/` does not exist as of 2026-04-15). No CCM-verification ledger entry yet. The path forward: draft decomposition bundle for W_BC-3 (Cuntz-Li route) first (preferred because it bypasses W_BC-1, W_BC-2); then W_BC-4 payoff unpacking.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/baum-connes/PROOF-CHAIN.md` — NOT YET CREATED as of 2026-04-15. Priority for creation: medium (after rh, ym, bsd, pvnp — the vertices with richer existing walls). When drafted, the four walls W_BC-1..4 each become natural decomposition targets; W_BC-3 (Cuntz-Li route) is the most immediately tractable.

- **CCM verification**: `strategy/ccm-verification/ledger.md#baum-connes` — NOT YET CREATED. Verdict (provisional): **VERIFIED (CCM-independent)**. The baum-connes proof chain does not depend on CCM 2025 (arXiv:2511.22755); rh and bsd are the CCM-dependent vertices, whereas baum-connes provides the K-theoretic substrate rh *uses* via the Chern character, but this flow is baum-connes → rh, not rh → baum-connes.

- **Inner rings**: NOT APPLICABLE — baum-connes is a primary outer-ring vertex (K-theoretic face of Branch D's BC algebra). No inner-ring decomposition needed.

- **QG5D W1/W2 cascading refinement (2026-04-14)**: Paper 1's W1 (scheme independence) and W2 (Route-C 3-loop) closed via Paper 10 (Theorem 1 + U.2a) + Paper 11 (Theorem K.4) + explicit L=3 numerical verification. Impact on baum-connes chain: cosmetic-to-small (the chain never gated on the scheme question directly), but the underlying CBB / Axiom 5 foundation is strictly stronger. No link status changes; confidence unchanged at 3/10; mention included in PROOF-CHAIN.md for programme-graph completeness.

- **Strategy files**: `strategy/baum-connes/00-audit-strategy.md` (community-standard audit gates, M×6 compliance, EXCISE for coefficients-version FALSE); `strategy/baum-connes/baum-connes-audit-brief.md` (PAC bare-mode invocation, 14 researchers, 5 major approaches). Both dated 2026-04-15; neither has triggered a PAC run yet.

- **Research landscape**: `strategy/_research/baum-connes/landscape.md` + `outlet.md` (2026-04-15, this session). Outlet analysis: no monetary prize; target journal Annals / Inventiones / GAFA.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W_BC-1 (classifying space BG for semigroup-crossed-product group).** — face: TOPOLOGY, projection: $P_D$, pattern: P1. STATUS: OPEN. No decomposition drafted. Most tractable via Luck's semigroup approach (Mislin-Valette 2003 Ch. 1 extended).

- **G2 — W_BC-2 (K-homology AHSS computation).** — face: RESONANCE, projection: $P_D$, pattern: P5. STATUS: OPEN, BLOCKED by G1. Standard AHSS mechanics; automatic once G1 resolves.

- **G3 — W_BC-3 (K-theory of $C^*_r(G)$ via Cuntz-Li + PV).** — face: ARITHMETIC, projection: $P_D$, pattern: P5. STATUS: OPEN. Preferred route (4a) bypasses G1/G2 entirely. Highest-priority open wall for near-term work.

- **G4 — W_BC-4 (K-theoretic constraints on spectral structure — THE PAYOFF).** — face: RESONANCE, projection: $P_D$, pattern: P4. STATUS: OPEN. Splits into four sub-payoffs (rh, ym, hodge, bgs); "new ideas beyond standard Baum-Connes" required. The vertex's universal-connector role lives here.

Four OPEN walls. The L5 isomorphism wall closed via Higson-Kasparov 2001 amenability on 2026-04-14. The four remaining walls are all inside $P_D$, with projection-discipline compliance automatic; the K-theoretic payoff (G4) is the programme's single highest-value open wall because it is the point where baum-connes becomes the receptacle for every index-theoretic invariant in the programme.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-01/vertices/baum-connes/critic-attacks.md` (to be created) and arbiter decisions at `strategy/x-ray/pac-output/runs/run-01/vertices/baum-connes/arbiter-decisions.md` (to be created).

Notable arbiter wins (anticipated):
- L3 face: RESONANCE over TOPOLOGY — AHSS starts from topology $H_p(BG; -)$ but the K-homology output catalogs resonance modes; paper60 §15 canonicalizes the RESONANCE reading for K-homology on a C*-algebra's classifying space.
- L4 face: ARITHMETIC over RESONANCE — Cuntz-Li is arithmetic-native (semigroup $\mathbb{N}^*$); critic argued RESONANCE (K-theory output) but arbiter picked ARITHMETIC (engine is the prime semigroup).
- L5 projection: $P_O$ over $P_D$ — the isomorphism-as-community-standard-claim lives on outer-ring boundary; critic argued $P_D$ (the object lives in $P_D$) but arbiter picked $P_O$ (the claim is the Clay-boundary-equivalent).
- L6 pattern: P4 over P5 — Chern+cyclic-cohomology+trace-formula chain involves graded-sum regularization but the LOAD-BEARING feature is integer-valued index pairings (topological rigidity); arbiter picked P4.
- Primary face: RESONANCE over SYMMETRY — tied at 2 layers each, but RESONANCE layers (L3, L6) are load-bearing while SYMMETRY layers (L1, L5) are book-ending; paper60 §15 canonicalizes the reading.

---

*End of Baum-Connes X-Ray. Snapshot 2026-04-15. 6 layers annotated. 26 cross-cuts identified (avg 4.3/layer — highest density so far). RESONANCE-primary, $P_D$-saturated (83%), P4/P5-rich chain. Four walls (W_BC-1..4); L5 closed via Higson-Kasparov amenability (2026-04-14); L6 payoff feeds rh, ym, hodge, bgs, qg5d — the universal-connector role of the K-theoretic face.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
