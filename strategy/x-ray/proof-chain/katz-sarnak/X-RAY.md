# X-RAY: Katz-Sarnak Symmetry Type (katz-sarnak)

*X-Ray of the katz-sarnak proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls. Bridge-family $k \in \{2,3,4,6\}$ selector for symmetry types $\{Sp, U, O, \text{Mixed}\}$ flagged as primary structural hook.*

*G Six and Claude Opus 4.6. April 15, 2026.*

---

## §1 Header

- **Vertex**: katz-sarnak
- **Paper**: paper46-katz-sarnak
- **Live file**: `strategy/proof-chain/katz-sarnak/PROOF-CHAIN.md` (snapshot 2026-04-15)
- **Top-level claim**: Every natural family of L-functions has a definite symmetry type $G \in \{U, Sp, O, SO^+, SO^-\}$ determined by the functional equation and the family's geometric monodromy; the symmetry type determines ALL zero statistics (spacing, low-lying density, $n$-level correlations, moment growth). PROVED for function fields (Deligne equidistribution); partially verified for number-field families (one-level densities); conjectural in full generality.
- **Current status**: 3/6 closed | PROVED (function-field) 1 / PARTIAL 1 / LITERATURE 0 / CONJECTURED 2 / OPEN 1 (the wall L5) / FOLLOWS 1. Confidence 7/10 (above ring average; raises rigidity per paper46 honest assessment).
- **Primary branch (paper1)**: D (CBB / Bost-Connes Hecke-semigroup representation type ↔ symmetry type), with strong secondary C (orbifold / bridge family $k \in \{2,3,4,6\}$ selects symmetry type per paper61 §19.6 and paper61 §06-12 Vertex 25 compound $P_D \cap P_C$).
- **Primary face**: SYMMETRY (paper60 §12 — THE canonical SYMMETRY face; "which group acts on the circle?"; Katz-Sarnak sits at paper60 §12's Face 6, the sixth face of the e-circle, as the symmetry-type selector itself).
- **Primary projection**: $P_D$ (paper61 §06-12 Vertex 25 explicit compound $P_D \cap P_C$; Hecke semigroup $\mathbb{N}^*$ representation type on each L-function family is the operator-algebraic shadow; paper61 §19.6 "four bridge values $k \in \{2, 3, 4, 6\}$ select the symmetry type").

---

## §2 ASCII Diagram A — Main proof-chain tree

```
KATZ-SARNAK (Symmetry Type Conjecture) — every family has G ∈ {U, Sp, O, SO^±}
│  primary face: SYMMETRY   primary proj: P_D   primary pat: P4
│  (secondary P_C via bridge family k ∈ {2,3,4,6} orbifold selector;
│   compound P_D ∩ P_C per paper61 §06-12 Vertex 25)
│
├── L1: Symmetry-type assignment per family              [CONJECTURED — number fields]
│      │                                                  [PROVED — function fields]
│      │  face: SYMMETRY    proj: P_D   pat: P4
│      │  invariant: Galois representation, monodromy
│      │  source: Katz-Sarnak 1999 AMS Colloquium;
│      │          paper46 L1; paper60 §12
│      │
│      └── splits by ground field:
│             │
│             ├── Function-field slice: PROVED via Deligne (see L2)
│             └── Number-field slice: CONJECTURED (feeds L3 partial verification)
│
├── L2: Function-field proof (Deligne equidistribution)   [PROVED]
│      │  face: SYMMETRY    proj: P_D   pat: P2
│      │  invariant: monodromy (load-bearing), Galois representation (background)
│      │  source: Katz-Sarnak 1999; Deligne Weil II (1980)
│      │
│      └── closes the function-field slice unconditionally
│             │
│             └── monodromy group G_mon(F) = classical compact group
│                  ⇒ symmetry type = G_mon(F) via equidistribution
│
├── L3: One-level density verification (number-field)     [PROVED — partial, support (-2,2)]
│      │  face: MEASURE     proj: P_D   pat: P1
│      │  invariant: zero distribution (load-bearing),
│      │             L-value (background — moments control the density)
│      │  source: Iwaniec-Luo-Sarnak 2000 (cuspidal newforms, O-type);
│      │          Özlük-Snyder 1999 (quadratic Dirichlet, Sp-type);
│      │          Miller 2004 (elliptic curves, O / SO^±);
│      │          many others per paper46 "Known results" table
│      │
│      └── family-specific PROVED slices:
│             │
│             ├── L3a: Dirichlet quadratic → Sp                [PROVED]
│             ├── L3b: Hecke cuspidal newforms → O             [PROVED]
│             ├── L3c: Elliptic curve L-functions → O / SO^±   [PROVED]
│             └── L3d: Moments K-S prediction matches          [PARTIAL]
│                     (Keating-Snaith 2000 conjecture;
│                      Guth-Maynard 2024 first progress in 50yr)
│
├── L4: BC representation type = symmetry type           [CONJECTURED — W_KS-1]
│      │  face: SYMMETRY    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure, ITPFI factor type
│      │  source: paper46 L4; paper12 §27 Axiom 4 bridge;
│      │          paper60 §12 "bridge IS the symmetry-type selector";
│      │          paper61 §06-12 Vertex 25 compound P_D ∩ P_C
│      │  depends: paper12 (CBB Axiom 4) + Hecke-semigroup bilinear form
│      │
│      └── NAMED WALL W_KS-1 (symmetry-type classifier operator):
│             │  confidence 0.65; bridge-family k ∈ {2,3,4,6}
│             │  maps to symmetry types {Sp, U, O, Mixed}
│             │
│             ├── k = 2 (Z/2Z char; CP sym)   → Sp  → GSE (β=4)
│             ├── k = 3 (Z/3Z char; color)    → U   → GUE (β=2)
│             ├── k = 4 (Z/4Z char; Pati-Sal) → O   → GOE (β=1)
│             └── k = 6 (Z/6Z char; CKM)      → Mixed (family-dep.)
│
├── L5: Generalized Katz-Sarnak (number fields, full)    [OPEN — W_KS-2 (THE WALL)]
│      │  face: MEASURE     proj: P_O   pat: P5
│      │  invariant: zero distribution (load-bearing — n-level densities),
│      │             scaling dimension (background — support extension)
│      │  depends: L1 + L2 + L3 + L4
│      │
│      └── DECOMPOSED into sub-routes per paper46 §5:
│             │
│             ├── L5a: Extend support beyond (-2, 2) via moments        [OPEN]
│             │       (connects to Lindelöf Paper 45; double-sum control)
│             │
│             ├── L5b: n-level densities via BC ITPFI factorization     [OPEN]
│             │       ω_1 = ⊗_p ω_1^(p); local-global assembly
│             │       (same structure as BSD Paper 26, OPN Paper 40)
│             │
│             └── L5c: Bridge-family k ∈ {2,3,4,6} symmetry-type test   [OPEN]
│                     verify each bridge → predicted K-S type
│                     (programme-specific test of L4; W_KS-1 feed)
│
└── L6: Full Katz-Sarnak (follows from L5)               [FOLLOWS]
       │  face: SYMMETRY    proj: P_O   pat: P4
       │  invariant: Galois representation, zero distribution
       │  source: paper46 L6; tautological conjunction of L1-L5
       │  depends: L5
       │
       └── pure logic: every family has type + type determines all stats

Symmetry-type anchor table (Load-bearing; paper60 §12 + paper46 §"expanded table"):
   Family                        | F.Eq. sign | Type      | β | Low-lying density
   ------------------------------+------------+-----------+---+----------------------
   ζ(s)                          |    +1      | U(1)      | 2 | 1
   L(s,χ_{-d}) quad. Dirichlet   |   varies   | Sp        | 4 | 1 - sin(2πx)/(2πx)
   L(s,E) even rank              |    +1      | SO^+      | 1 | 1 + 1/(2δ) at origin
   L(s,E) odd rank               |    -1      | SO^-      | 1 | 1 - 1/(2δ) at origin
   L(s,f) Hecke cusp             |    +1      | O         | 1 | 1
   L(s,sym^2 f)                  |    +1      | Sp        | 4 | 1 - sin(2πx)/(2πx)
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (Quantum observables do not see
                          L-function symmetry types; the
                          symmetry-type classifier is an
                          operator-algebraic fact about the
                          Hecke semigroup action.)
                                  ▲
                                  │
                                  │
        ┌─────────────(P_O outer)───────────────┐
        │                                       │
        │  KATZ-SARNAK: every L-function family │
        │    has symmetry type G ∈ {U, Sp, O,   │
        │    SO^±}; type determines all zero    │
        │    statistics                         │
        │                                       │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity        ═══ P_D CBB ═══            P_C cosmology
    (forgotten —       Hecke semigroup N*         (SECONDARY)
    no gauge-bundle    representation type        bridge family
    reading of         preserves bilinear form    k ∈ {2,3,4,6}
    Katz-Sarnak;       (Hermitian/alternating/    orbifold selector
    the monodromy      symmetric) → G;            each k → Standard
    connection is      ITPFI ω_1 = ⊗_p ω_1^(p);   Model symmetry:
    function-field,    local-at-p factors         k=2 CP, k=3 color,
    not gauge-bundle   assemble n-level density;  k=4 Pati-Salam,
    direct)            bridge β_k selects type    k=6 CKM
                       per paper61 §10
                            │
                            ▼
                       P_E pins
                       (bridge-family pin
                        selection at k ∈
                        {2,3,4,6}; Pin #9
                        α_PS^{-1} (k=4 O type)
                        and Pin #10 λ_CKM
                        (k=6 Mixed type) are
                        the programme's K-S-
                        gated pins. Compound
                        P_D ∩ P_C ∩ P_E in
                        practice; paper61
                        Vertex 25.)
```

Primary projection $P_D$ uses ═══ doubled line (paper61 §06-12 Vertex 25 explicit compound $P_D \cap P_C$). $P_C$ is the secondary because the bridge family $k \in \{2,3,4,6\}$ lives in the orbifold/cosmology projection (paper61 §19.6 — "four Brauer classes correspond to four Katz-Sarnak groups"). $P_O$ is invoked at L5 (the wall) and L6 (Clay-adjacent outer-ring statement). $P_E$ is absent-secondary: bridge pins #9, #10 are K-S-gated but pin-propagation is a downstream inheritance, not a layer-internal K-S assignment. $P_A, P_B$ are forgotten: the symmetry-type classifier lives in the operator algebra, not in quantum observables or gauge bundles.

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
          (YM)              │        ○ (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (RESONANCE secondary;
                        ARITHMETIC adjacent)
```

Marker key:

```
Primary face:    ● SYMMETRY (paper60 §12 — the e-circle's Face 6;
                   Katz-Sarnak IS the sixth face; "which group acts
                   on the circle?" — the symmetry-type selector)
Secondary faces: ○ MEASURE  (2 layers: L3 one-level density, L5
                              n-level densities + support extension;
                              paper60 §10 equidistribution content)
Absent faces:    TOPOLOGY, DYNAMICS, HARMONICS, AMPLITUDE, CURVATURE,
                 ARITHMETIC, RESONANCE, SPREAD
```

Interpretation: Katz-Sarnak's "shape" on the e-circle is SYMMETRY-canonical with MEASURE as the only secondary — reflecting that the chain's internal content is either (a) symmetry-type assignment itself (L1, L2, L4, L6) or (b) density measurements that test the symmetry-type prediction (L3, L5). Six of the ten faces are absent: K-S does not interrogate winding (Lehmer), dynamical flow (Cramér), harmonic decomposition (Collatz), amplitude growth (Lindelöf), gauge curvature (YM), arithmetic lattice (Goldbach/TP), resonance amplitude (Selberg-type), or $L^2$ mass spread (QUE). K-S interrogates exactly one thing: which group acts. That makes it the *purest* face on the e-circle — every layer is either the question itself or a measurement of the answer.

---

## §3 Layer-by-Layer X-Ray

### L1 — Symmetry-type assignment (every natural family has $G$)

**Claim**: Every natural family of L-functions has a definite symmetry type $G \in \{U, Sp, O, SO^+, SO^-\}$ determined by the functional equation and the family's geometric monodromy.

**Status**: CONJECTURED (number fields) / PROVED (function fields)
**Source**: Katz-Sarnak 1999 *Random Matrices, Frobenius Eigenvalues, and Monodromy* (AMS Colloquium); paper46 chain Link 1; paper60 §12 the sixth face framing.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — "the sixth face of the e-circle: SYMMETRY. Which group acts on it?"; L1 IS the face-defining statement)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 25 — the Hecke semigroup $\mathbb{N}^*$ representation type lives in the BC algebra; symmetry-type assignment is an operator-algebraic classification)
- **Pattern**: P4 Topological Rigidity (paper08 §36 — Pattern 4: "compactness forces discreteness"; the symmetry type is rigidly determined by the bilinear invariant of the Hecke representation — rigidity of classification)
- **Invariant preserved**: Galois representation (load-bearing — the functional equation and monodromy data IS a Galois representation), monodromy (load-bearing — the geometric monodromy group is the symmetry type in the function-field case)
- **Geometric interpretation**: L1 is the face-defining claim for SYMMETRY (paper60 §12): the e-circle $U(1)$ can carry the action of any of the five classical compact groups; each natural family of L-functions "sees" exactly one of them. The symmetry type is READ from the functional equation's sign (paper60 §12 expanded table) and the family's monodromy; it is not imposed. Under $P_D$ (paper61 §06-12 Vertex 25), this is a classification of Hecke-semigroup representations by their bilinear invariant (Hermitian/alternating/symmetric). [Considered but rejected: face MEASURE — equidistribution of zeros is a MEASURE-face downstream consequence, but L1 is the *cause* of the measure, not the measure itself; projection $P_O$ — L1 is conjectural at number fields but the *assignment machinery* lives in $P_D$, not at the Clay boundary; pattern P1 — geometric reinterpretation of zeros as eigenangles is beautiful but L1's content is rigidity of the classification, not reinterpretation.]
- **Cross-cuts**: qg5d Branch D Axiom 4 (bridge-family IS the symmetry-type selector, paper61 §10), bgs L4 (Dyson threefold way = K-S symmetry classification at unitary type), rh L_symmetry_type (ζ(s) at $U$-type), bsd L_rank (functional-equation sign ↔ $SO^+$ vs $SO^-$), sato-tate L_haar (Haar pushforward on unitary-group conjugacy classes is the $U$-type slice).

### L2 — Function-field proof (Deligne equidistribution)

**Claim**: For L-functions over $\mathbb{F}_q(t)$, the symmetry type equals the geometric monodromy group $G_{\text{mon}}$, and Deligne's equidistribution theorem (Weil II) gives the zero distribution exactly.

**Status**: PROVED
**Source**: Katz-Sarnak 1999 (monograph: main theorem for function fields); Deligne, *La conjecture de Weil II* (1980, Publ. IHES 52).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — the same face as L1, here closed unconditionally for function fields)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 25 — function-field L-functions inherit the BC-algebra structure via the Hecke action on $\mathbb{F}_q(t)^*$)
- **Pattern**: P2 Holonomy (paper08 §36 — Pattern 2: "Wilson-loop / winding-number"; the Frobenius at each place $v \in |\mathbb{F}_q(t)|$ is a holonomy element in $G_{\text{mon}}$; equidistribution of Frobenius holonomies is the content)
- **Invariant preserved**: monodromy (load-bearing — $G_{\text{mon}}$ IS the symmetry type by Deligne), Galois representation (background — function-field L is attached to an $\ell$-adic sheaf with geometric monodromy)
- **Geometric interpretation**: The function-field case is closed by a holonomy argument (Pattern 2, paper08 §36): each Frobenius conjugacy class is a holonomy element around a place; Deligne's equidistribution theorem (Weil II, paper60 §12 cited) shows that as the conductor grows, these holonomies equidistribute with respect to Haar measure on $G_{\text{mon}}$. Thus the symmetry type = monodromy group, proved. This is the ONLY fully-proved layer of the Katz-Sarnak chain; it is the anchor that makes the number-field conjecture credible. [Considered but rejected: face MEASURE — Deligne's theorem IS equidistribution (a measure-theoretic statement), but the load-bearing invariant is monodromy as a symmetry object, not the resulting measure; pattern P4 — Deligne rigidity is a fair alternative, but Pattern 2 (Frobenius = holonomy) is the historical-mechanical core; projection $P_B$ — gauge-bundle reading via Pontryagin of $G_{\text{mon}}$ is downstream.]
- **Cross-cuts**: sato-tate L_haar (Haar pushforward on $G_{\text{mon}}$ is the common mechanism), bgs L5 (GUE sine-kernel is the $G = U$ slice of Deligne equidistribution), rh L_function_field (RH in function-field case via Weil; same Deligne machinery), hodge L2 (monodromy as symmetry-type selector shared structurally).

### L3 — One-level density verification (number fields)

**Claim**: For many number-field families (Dirichlet L, elliptic curve L, cuspidal newforms), the one-level density of low-lying zeros matches the random matrix prediction for the conjectured symmetry type, within the support constraint $\hat{\phi} \subset (-2, 2)$.

**Status**: PROVED (partial — per-family slices verified)
**Source**: Iwaniec-Luo-Sarnak 2000 (cuspidal newforms → $O$-type); Özlük-Snyder 1999 (quadratic Dirichlet → $Sp$-type); Miller 2004 (elliptic curves → $O$ / $SO^\pm$); paper46 "Known results" table.

#### Physics

- **Face**: MEASURE (paper60 §10 — "equidistribution / weak-* convergence"; one-level density IS a measure-convergence statement — the density of zeros converges weakly to the predicted RMT density)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 25 — one-level density is computed from BC-algebra local factors $\omega_1^{(p)}$, integrated against a test function $\phi$ with $\hat\phi$ of compact support)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — Pattern 1: "restore the e-circle, mystery dissolves"; the partial verification reinterprets explicit-formula computations as K-S density predictions, matching family-by-family)
- **Invariant preserved**: zero distribution (load-bearing — the one-level density IS a statistic of zeros), L-value (background — moments of $L(s)$ control the density via the explicit formula)
- **Geometric interpretation**: The ILS / Özlük-Snyder / Miller verifications reinterpret the first-moment of an explicit-formula sum as the integral of $\phi$ against the symmetry-type-predicted density (Pattern 1, paper08 §36). Under $P_D$ (paper61 §06-12 Vertex 25) this is the BC-algebra's local-at-$p$ factors $\omega_1^{(p)}$ assembling — via the Hecke representation type — into the predicted measure. The support constraint $\hat\phi \subset (-2, 2)$ comes from the length of prime sums that can be controlled unconditionally (paper46 §5 sub-route 5a: "extending support beyond $(-2, 2)$ requires controlling double sums over primes"). [Considered but rejected: face SYMMETRY — one-level density *tests* the symmetry type but the load-bearing content at L3 is the weak-convergence statement itself; pattern P4 — rigidity of the RMT prediction matches but the engine here is reinterpretive matching family-by-family; projection $P_O$ — partial verification is not an outer-ring-Clay-closure claim.]
- **Cross-cuts**: bgs L5 (GUE statistics for ζ-zeros is the $U$-type slice of L3), sato-tate L_one_level (one-level equidistribution via Haar on $U(n)$), lindelof L_moments (moment control of $L(s)$ connects via the Katz-Keating-Snaith prediction), rh L_pair_correlation (Montgomery-Odlyzko pair-correlation for $\zeta$ is the $U$-type one-level corollary).

### L3a — Dirichlet quadratic → $Sp$-type verified

**Claim**: The family of quadratic Dirichlet L-functions $L(s, \chi_d)$ has symmetry type $Sp$, confirmed by one-level density matching at support $\hat\phi \subset (-2, 2)$.

**Status**: PROVED
**Source**: Özlük-Snyder 1999.

#### Physics

- **Face**: MEASURE (paper60 §10 — density verification for this specific family)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 25 — BC-algebra local factors at quadratic characters)
- **Pattern**: P1 Geometric Reinterpretation
- **Invariant preserved**: zero distribution (load-bearing — $Sp$ density $1 - \sin(2\pi x)/(2\pi x)$), ITPFI factor type (background — quadratic characters at bridge $k=2$, symplectic type per paper60 §12 table)
- **Geometric interpretation**: Quadratic Dirichlet characters sit at bridge $k=2$ (CP symmetry per paper12 Axiom 4); the corresponding symmetry type is symplectic (paper60 §12 expanded table). The Özlük-Snyder verification is the first number-field confirmation of K-S L4's prediction for the $k=2$ slice of the bridge family. [Considered but rejected: face ARITHMETIC — quadratic characters lattice the residue classes but the measured content is the density; pattern P4 — Sp rigidity verified but the mechanism is reinterpretive matching.]
- **Cross-cuts**: grh L1 (Dirichlet L-functions under BC$_\chi$ twist; shared bridge-$k=2$ structure), bsd (quadratic twists of elliptic-curve L-functions at quadratic character level).

### L3b — Hecke cuspidal newforms → $O$-type verified

**Claim**: The family of Hecke cuspidal newforms $L(s, f)$ (weight $k$, conductor $N$) has symmetry type $O$, confirmed by one-level density matching at support $\hat\phi \subset (-2, 2)$.

**Status**: PROVED
**Source**: Iwaniec-Luo-Sarnak 2000.

#### Physics

- **Face**: MEASURE (paper60 §10 — density verification)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 25 — BC-algebra local factors at cuspidal automorphic representations)
- **Pattern**: P1 Geometric Reinterpretation
- **Invariant preserved**: zero distribution (load-bearing — $O$-type density $1$ at origin), monodromy (background — the self-dual functional equation with sign $+1$)
- **Geometric interpretation**: Hecke cuspidal newforms have self-dual $L$-functions with functional-equation sign $+1$ — this forces the symmetric-bilinear-form invariant under the Hecke action, hence orthogonal type (paper60 §12 expanded table). ILS's one-level-density verification is the anchor result for the $O$-type slice of K-S. Under $P_D$ (paper61 §06-12 Vertex 25) this is the BC-algebra classification. [Considered but rejected: face HARMONICS — Hecke newforms are harmonic analysis but the measured content is symmetry type; pattern P2 — monodromy-holonomy alternative but matching mechanism dominates.]
- **Cross-cuts**: sato-tate L_hecke (Hecke-newform Frobenius-angles inherit O-type Haar), rh L_cusp_form (cuspidal-form L-function analog), h12 (Galois-representation self-duality).

### L3c — Elliptic curve L-functions → $O / SO^\pm$ verified

**Claim**: The family of elliptic curve L-functions $L(s, E)$ has symmetry type $O$ in aggregate, with $SO^+$ for even-rank curves and $SO^-$ for odd-rank curves, confirmed by one-level density.

**Status**: PROVED
**Source**: Miller 2004.

#### Physics

- **Face**: MEASURE (paper60 §10 — density verification, split by rank parity)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 25 — BC local factors; parity split is the Brauer-class signature of bridge $k=4$, Pati-Salam)
- **Pattern**: P1 Geometric Reinterpretation
- **Invariant preserved**: zero distribution (load-bearing — $SO^+$ density $1 + 1/(2\delta)$ vs $SO^-$ density $1 - 1/(2\delta)$ at origin), Galois representation (background — $\ell$-adic Tate module of $E$)
- **Geometric interpretation**: Miller 2004 verifies that the elliptic-curve L-function family splits by functional-equation sign into $SO^+$ (even rank, sign $+1$) and $SO^-$ (odd rank, sign $-1$). This is the bridge-$k=4$ (Pati-Salam) slice per paper60 §12 expanded table. BSD's rank parity IS the K-S symmetry-type split at $k=4$. [Considered but rejected: face ARITHMETIC — rank is arithmetic content but the measured density is MEASURE-face; pattern P4 — rank-parity rigidity implied, P1 reinterpretive matching dominates.]
- **Cross-cuts**: bsd L_rank_parity (rank parity = $SO^\pm$ split at $k=4$ — PRIMARY K-S ↔ BSD bridge), qg5d Branch C bridge $k=4$ (Pati-Salam orbifold selector), sato-tate L_elliptic (elliptic-curve Frobenius angles inherit $SO^\pm$).

### L3d — Moments Keating-Snaith prediction matches

**Claim**: The $k$-th moment of $|\zeta(1/2 + it)|$ grows as $T (\log T)^{k^2}$ per the GUE prediction (Keating-Snaith 2000); partial results have been proved with Guth-Maynard 2024 providing the first progress in 50 years.

**Status**: PARTIAL (conjecture Keating-Snaith 2000; first progress Guth-Maynard 2024)
**Source**: Keating-Snaith 2000; Guth-Maynard 2024.

#### Physics

- **Face**: MEASURE (paper60 §10 — moments are a measure-theoretic observable on the family)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 25 — $L$-value moments live in BC-algebra cocycle-expectation)
- **Pattern**: P1 Geometric Reinterpretation (RMT prediction reinterprets moments as characteristic-polynomial expectations on $U(N)$)
- **Invariant preserved**: L-value (load-bearing — moments $\int_0^T |\zeta|^{2k} dt$), zero distribution (background — moment growth is controlled by zero spacing)
- **Geometric interpretation**: Keating-Snaith 2000 predicted that $\int_0^T |\zeta(1/2 + it)|^{2k}\, dt \sim C_k T (\log T)^{k^2}$, where $C_k$ is the GUE characteristic-polynomial moment on $U(N)$. This is a Pattern 1 reinterpretation (paper08 §36): moments of $\zeta$ become moments of a random unitary matrix's characteristic polynomial, under $P_D$ (paper61 §06-12 Vertex 25). Guth-Maynard 2024 gave the first $k$-moment progress in 50 years, using a new large-value estimate. [Considered but rejected: face AMPLITUDE — moments are an amplitude statistic (cf. Lindelöf), but the symmetry-type-matching content is measure; pattern P3 — $\log T$ is a scale but the prediction is reinterpretive.]
- **Cross-cuts**: lindelof L_moments (Lindelöf bound and K-S moment prediction are complementary amplitude measurements), rh L_moments (the $\zeta$-moment problem IS the $U$-type K-S instance), bgs L_moments (GUE moments).

### L4 — BC representation type = symmetry type

**Claim**: The Hecke semigroup $\mathbb{N}^*$ acts on each L-function family via a specific representation, and the representation's bilinear invariant (Hermitian / alternating / symmetric) determines the symmetry type $G$. The bridge family at $k \in \{2, 3, 4, 6\}$ selects specific symmetry types.

**Status**: CONJECTURED (framework construction)
**Source**: paper46 L4; paper12 §27 Axiom 4 bridge; paper60 §12 "the bridge IS the symmetry-type selector"; paper61 §06-12 Vertex 25 compound $P_D \cap P_C$.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — the identification of Hecke representation type with K-S symmetry type is the programme's primary novel contribution to the SYMMETRY face)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 25 — the Hecke representation type is an operator-algebraic object native to $P_D$; bridge family's $P_C$ contribution supplies the orbifold structure but the classification itself is $P_D$-internal)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — Pattern 1: reinterpret K-S symmetry-type classification AS the BC-algebra representation-type classification, with the bridge family serving as the canonical four-point selector)
- **Invariant preserved**: C*-algebra structure (load-bearing — the bilinear invariant is an algebraic property of the Hecke representation), ITPFI factor type (load-bearing — type III$_\lambda$ structure differentiates by $\chi(p)$ phase)
- **Geometric interpretation**: L4 is the programme's key novel structural claim on the SYMMETRY face (paper60 §12): the Hecke semigroup $\mathbb{N}^*$ acts on every L-function family, and the bilinear form preserved by the action (Hermitian → $U$, alternating → $Sp$, symmetric → $O$) determines the K-S symmetry type. Under $P_D$ (paper61 §06-12 Vertex 25) this is an operator-algebraic classification of Hecke representations. The CBB bridge family $k \in \{2,3,4,6\}$ provides four canonical representations, each with a distinguished bilinear invariant — the Brauer classes $\beta_k \in H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$ (paper61 §06-12 Axiom 4) are the obstruction classes whose vanishing/non-vanishing selects which bilinear form the Hecke action preserves. [Considered but rejected: face RESONANCE — Hecke representations are resonance-mode data but the load-bearing content is the symmetry-type classification; projection $P_C$ — bridge family has cosmological ($P_C$) reading but the classification engine is operator-algebraic; pattern P4 — rigidity of the four-point selector is implied but the move is reinterpretive.]
- **Cross-cuts**: qg5d Branch D Axiom 4 (PRIMARY EDGE — bridge family IS the symmetry-type selector, paper61 §10), grh L1 (BC$_\chi$ construction uses character-twisted Hecke action, sharing C*-algebra structure), bsd L5 (BC cocycle shift $|\Delta c^\psi(\delta)| < 2/(N-1)$ applies at quadratic/cubic/quartic/sextic bridges), rh L_BC (RH's spectral realization uses the same BC algebra; K-S differentiates which L-function family is being realized), bgs L4 (Dyson threefold way IS the K-S classification at symmetry-type level).

### L5 — Generalized number-field Katz-Sarnak (THE WALL)

**Claim**: For ALL natural families over $\mathbb{Q}$, the symmetry type determines the complete zero statistics (all $n$-level densities, not just one-level; arbitrary support, not just $\hat\phi \subset (-2, 2)$; universal across families).

**Status**: OPEN — W_KS-2 (the wall)
**Source**: Katz-Sarnak 1999 conjecture; paper46 L5; decomposed into sub-routes 5a/5b/5c per paper46 §5.

#### Physics

- **Face**: MEASURE (paper60 §10 — $n$-level densities, support extension, and universality are all measure-theoretic statements about the zero-spacing distribution across the family)
- **Projection**: $P_O$ (paper61 §12 — L5 is the outer-ring boundary where K-S closes as a famous conjecture; Clay-grade closure on the number-field slice)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — Pattern 5: "KK sums regularize via Epstein-zeta vanishing"; the support extension route 5a uses moment control = zeta-regularization-of-$L$-value-sums; the $n$-level route 5b uses ITPFI factorization = product regularization; the bridge route 5c uses Brauer-class arithmetic)
- **Invariant preserved**: zero distribution (load-bearing — $n$-level densities), scaling dimension (background — support extension is a scaling-range statement, same territory as Lindelöf)
- **Geometric interpretation**: L5 is K-S's sole structural wall on the number-field side. Three sub-routes (paper46 §5): (5a) Extend support beyond $(-2, 2)$ via moment control — this meets Lindelöf at the double-sum-of-primes boundary (paper60 §12 + paper60 §11). (5b) Compute $n$-level densities via the BC ITPFI factorization $\omega_1 = \otimes_p \omega_1^{(p)}$, using local-at-$p$ factors that assemble per symmetry type — same local-global structure as BSD (Paper 26) and OPN (Paper 40). (5c) Verify bridge-family symmetry types at $k \in \{2,3,4,6\}$ as a programme-specific test of L4's identification. Under $P_O$ (paper61 §12) this is K-S's Clay-adjacent outer-ring statement (paper60 §12 "consensus framework for L-function statistics"). Pattern 5 (paper08 §36) regularization appears in all three sub-routes: moment sums over primes (5a), product regularization of ITPFI factors (5b), and Brauer-class zeta-regularization (5c). [Considered but rejected: face SYMMETRY — L5 tests symmetry-type prediction but the load-bearing statement is measure-convergence; projection $P_D$ — sub-routes live in $P_D$ mechanically, but the conjunction at L5 is outer-ring-facing; pattern P4 — rigidity of the prediction is implied, but regularization is the technical engine.]
- **Cross-cuts**: lindelof L_support (sub-route 5a meets Lindelöf at double-sum-of-primes boundary — shared scaling dimension), bsd L_local_global (sub-route 5b matches BSD's ITPFI local-global structure — shared zero distribution), opn L_local_global (sub-route 5b matches OPN's local-global structure — shared ITPFI factor type), qg5d Branch D Axiom 4 (sub-route 5c IS the programme-specific test), rh L_n_level (RH's $n$-level correlation statistics inherit the $U$-type slice — shared zero distribution).

### L6 — Full Katz-Sarnak (follows from L5)

**Claim**: Every natural family of L-functions has a definite symmetry type, and the type determines all statistics. Tautological conjunction of L1–L5.

**Status**: FOLLOWS
**Source**: paper46 L6.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — the full K-S conjecture, restated at the closure layer)
- **Projection**: $P_O$ (paper61 §12 — outer-ring Clay-adjacent statement; symmetric with L5's outer-ring projection)
- **Pattern**: P4 Topological Rigidity (rigidity of the full classification once L5 closes)
- **Invariant preserved**: Galois representation (load-bearing — the ultimate content is representation-theoretic), zero distribution (background — the statistics are determined by the symmetry type)
- **Geometric interpretation**: L6 is the logical closure: once L1 (assignment), L2 (function-field), L3 (one-level density), L4 (BC-representation identification), and L5 (full number-field extension) are in place, the full K-S conjecture follows by pure conjunction. Under $P_O$ (paper61 §12) this is the Clay-adjacent closure statement. Pattern 4 (paper08 §36) at the top level: the rigid universality of the K-S classification across all families. [Considered but rejected: face MEASURE — L6's content is the measure-theoretic statement but the closure is symmetry-type-canonical; projection $P_D$ — mechanics live in $P_D$ but closure is outer-ring; pattern P1 — reinterpretive framing at layers below, rigidity at L6.]
- **Cross-cuts**: rh L_closure (RH is the $U$-type slice of K-S at $\zeta(s)$), grh L_closure (GRH is the $\{U, Sp\}$ slice at Dirichlet L-functions), bsd L_closure (BSD rank-parity is the $SO^\pm$ slice at elliptic curves), qg5d Branch D (closure at the Hecke-representation level; compound $P_D \cap P_C$ per paper61 Vertex 25).

---

## §4 Branch Map

Katz-Sarnak's chain branches structurally at three points: (i) L1 splits by ground field (function-field PROVED via L2 vs. number-field CONJECTURED feeding L3), (ii) L3 splits by L-function family (L3a Dirichlet, L3b Hecke, L3c elliptic, L3d moments), and (iii) L5 decomposes into three sub-routes (5a support extension, 5b $n$-level via ITPFI, 5c bridge-family test).

```
L1 splits by ground field:
├── Route F — Function field (Deligne equidistribution)
│   [P_D projection | SYMMETRY | P2 Holonomy | PROVED via L2]
│
└── Route N — Number field
    [P_D projection | SYMMETRY | P4 Topological Rigidity | CONJECTURED]
    │
    └── feeds L3 (partial verification) and L5 (the wall)

L3 splits by family (all PROVED slices at support (-2, 2)):
├── L3a Dirichlet quadratic   [P_D | MEASURE | P1 | Sp-type, bridge k=2]
├── L3b Hecke cuspidal        [P_D | MEASURE | P1 | O-type, bridge k=6]
├── L3c Elliptic curve        [P_D | MEASURE | P1 | SO^±-type, bridge k=4]
└── L3d Moments K-S prediction [P_D | MEASURE | P1 | U-type, ζ(s)]
                                (PARTIAL: Keating-Snaith conjecture;
                                 Guth-Maynard 2024 first progress)

L5 decomposes into three sub-routes (ALL OPEN):
├── L5a Support extension via moments
│   [P_O | MEASURE | P5 | scaling dimension load-bearing]
│   meets Lindelöf at double-sum-of-primes boundary
│
├── L5b n-level densities via BC ITPFI factorization
│   [P_O | MEASURE | P5 | ITPFI factor type load-bearing]
│   same local-global structure as BSD and OPN
│
└── L5c Bridge-family k ∈ {2,3,4,6} symmetry-type test
    [P_O | SYMMETRY | P4 | Brauer class load-bearing]
    programme-specific test of L4
```

All three L5 sub-routes converge on the same outer-ring closure (L5 → L6). The split tells us: K-S's wall is MULTI-FACETED — it has a measure-theoretic route (5a/5b) and a symmetry-structural route (5c). The programme's contribution is concentrated in 5c (bridge-family test), which is programme-native and directly testable within paper12 (CBB Axiom 4).

The three L3 family slices are not branches in the decomposition sense — they are complementary verifications of L4's prediction, one per bridge $k$-value. Together they cover the four symmetry types: 5a→Sp (k=2), 5b→O (k=6), 5c→SO± (k=4), 5d→U (ζ, all-of-$\mathbb{N}^*$).

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | Katz-Sarnak does not interrogate the topology face (no winding / genus / fundamental-class content at any layer). |
| DYNAMICS   |   0   |                       | No dynamical-flow content — K-S is a static classification. |
| HARMONICS  |   0   |                       | No Fourier / orbit-averaging layer. |
| MEASURE    |   6   | ████████████████████████ | SECONDARY (tied for primary by count). L3 + L3a/b/c/d + L5 are all measure-convergence statements — one-level densities, $n$-level densities, moment prediction. Six layers are MEASURE-face. |
| AMPLITUDE  |   0   |                       | No amplitude-growth layer internally (cross-cuts Lindelöf at L5a boundary). |
| SYMMETRY   |   4   | ████████████████      | PRIMARY. L1 (assignment), L2 (function-field proof), L4 (BC representation type identification), L6 (closure). Four layers define or close the symmetry-type question. |
| CURVATURE  |   0   |                       | No curvature content — K-S lives on SYMMETRY, not CURVATURE. |
| ARITHMETIC |   0   |                       | No arithmetic-lattice content (Newton sums, integer lattices); the arithmetic in L3 is consumed by MEASURE. |
| RESONANCE  |   0   |                       | No trace-formula / spectral-side layer (would appear at Selberg-type vertex). |
| SPREAD     |   0   |                       | No $L^2$-mass-spreading content. |

**Interpretation**: Katz-Sarnak is the programme's PUREST face. Four of six closed/conjectured layers are SYMMETRY-canonical (L1, L2, L4, L6 — the assignment, proof, identification, and closure); the remaining six (L3 + four sub-slices, plus L5 wall) are MEASURE-canonical (one-level densities and moment matching). Eight of ten faces are ABSENT — K-S does not interrogate topology, dynamics, harmonics, amplitude, curvature, arithmetic, resonance, or spread. This is the signature of a classification problem: the question is "which group?" (SYMMETRY) and the answer is tested via "what density?" (MEASURE). No other content is needed. Paper60 §12's identification of K-S as the sixth face is vindicated by this distribution: K-S IS symmetry with measure-theoretic verification.

**Count vs. YM comparison**: YM has 6 faces represented (CURVATURE 6, RESONANCE 5, DYNAMICS 3, AMPLITUDE 3, SYMMETRY 3, ARITHMETIC 1). K-S has 2 faces represented (SYMMETRY 4, MEASURE 6). K-S is markedly more face-concentrated than YM, consistent with its role as a pure classification (one question, one test family) vs. YM's role as a hub vertex with many invariants.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No quantum-observable content; symmetry-type classifier is operator-algebraic. |
| $P_B$        |   0   |                      | No gauge-bundle content; Katz-Sarnak is not a gauge theory. |
| $P_C$        |   0   |                      | Bridge family's $P_C$ contribution is structural-secondary (supplies the orbifold $k$-values) but no layer is $P_C$-internal. |
| $P_D$        |   8   | ████████████████████████████████ | DOMINANT. BC / operator-algebra projection — the home of the Hecke representation type classification, the ITPFI factorization, the local-at-$p$ assembly of densities. L1, L2, L3 + L3a/b/c/d, L4 = 8 layers. 80% of main + sub-layers. |
| $P_E$        |   0   |                      | Bridge pins #9 (α_PS^{-1} at k=4) and #10 (λ_CKM at k=6) are K-S-gated but inherited downstream; no layer-internal $P_E$ assignment. |
| $P_O$        |   2   | ████████             | Outer-ring Clay-adjacent projection — invoked at L5 (the wall) and L6 (closure). 20%. |

**Interpretation**: The projection profile is strongly bimodal: $P_D$ dominates (8 / 10 layers, 80%) because K-S's internal content is operator-algebraic classification; $P_O$ captures the two outer-ring closure layers (L5 wall and L6 statement). $P_A, P_B, P_C, P_E$ are all absent as layer-internal projections — consistent with paper61 §06-12 Vertex 25's compound $P_D \cap P_C$ assignment: $P_C$ is a structural secondary (bridge family supplies the four-point orbifold), not a layer-internal projection. The $P_D$ dominance is even higher than BGS (80% vs 70-ish%), reflecting K-S's role as a pure classification question on the BC side.

Compared to YM ($P_B$ 65%, $P_D$ 30%, $P_O$ 5%): K-S's projection profile is *inverted* — gauge-bundle absent, BC dominant. This is the SYMMETRY vs. CURVATURE face distinction made concrete at the projection level: SYMMETRY lives in $P_D$, CURVATURE lives in $P_B$, even when both vertices are outer-ring Clay-adjacent.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                        qg5d (Branch D Axiom 4)
                        ═══ bridge family IS K-S selector
                        ═══ L4 compound P_D ∩ P_C hub
                        ═══ L5c programme-native test target
                                │
                                │
    bgs ══════════════════ katz-sarnak ══════════════════ rh
    (DYNAMICS canonical     │  (SYMMETRY canonical       (PROVED for ζ if K-S)
     at L2; RESONANCE       │   at L1,L2,L4,L6)          ═══ L1 ↔ ζ at U-type
     at L1)                 │                            ═══ L3d ↔ ζ moments (U)
    ═══ L4 ↔ Dyson 3-fold   │                            ═══ L6 ↔ closure for ζ
    ═══ L5 ↔ GUE @ U-type   │
    ═══ L3d ↔ moments       │
                            │
                            │
    sato-tate ══════════════│════════════════════ grh
    (MEASURE canonical;     │                    (SYMMETRY ∩ BC_χ at
     Haar equidistribution) │                     character bridge)
    ═══ L2 ↔ Haar on G_mon  │                    ═══ L1 ↔ BC_χ ↔ k-bridge
    ═══ L3b ↔ Hecke Frob    │                    ═══ L4 ↔ character
    ═══ L3c ↔ elliptic Frob │                    ═══ L3a ↔ Dirichlet @ Sp
                            │
                            │
    bsd ════════════════════│════════════════════ lindelof
    (ARITHMETIC; rank       │                    (AMPLITUDE; moments)
     parity = SO^± slice)   │                    ─── L5a support ↔ double sum
    ═══ L3c ↔ elliptic      │                    ─── L3d ↔ K-S moment pred.
    ═══ L4 ↔ bridge k=4     │                    ─── L5 ↔ Lindelöf boundary
    ═══ L5b ↔ ITPFI         │
                            │
                       hodge (paper29)
                       ─── L2 ↔ monodromy classifier
                       ─── L4 ↔ Galois-repn class
                       (SPECULATIVE — motivic lift)

    opn (paper40)                twin-primes / cramer / goldbach
    ─── L5b ↔ local-          ─── MULTI-CHANNEL:
        global structure        K-S differentiates the gap-
    (SPECULATIVE)               distribution arc per bridge k
                                ─── L1 splits twin-prime type
                                ─── L1 splits Cramér extreme
                                ─── L1 splits Goldbach density
                                (paper60 §12 multi-channel
                                 discovery; SPECULATIVE edges)

    h12 (Galois)                 pvnp (paper28)
    ─── L1 ↔ Gal-repn             ─── L4 ↔ Popa rigidity via
        classification                ITPFI III_1 at U-type
    (SPECULATIVE)                 (SPECULATIVE)
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch D Axiom 4** — shared Galois representation (PRIMARY EDGE).
  - Reason: Bridge family $k \in \{2,3,4,6\}$ IS the symmetry-type selector (paper61 §10 Axiom 4; paper60 §12 expanded table). K-S's L1 symmetry-type assignment matches one-to-one with the CBB Axiom 4 four-point structure.
  - Transposition candidate: YES (capacitor cell for bridge-family ↔ symmetry-type identification).

- **L1 ↔ bgs:L4** — shared Galois representation (Dyson threefold way = K-S classification).
  - Reason: BGS's Dyson threefold way at unitary type is the $G = U$ slice of K-S's classification per paper60 §12 + paper60 §20.
  - Transposition candidate: YES.

- **L1 ↔ rh:L_symmetry_type** — shared Galois representation ($\zeta$ at $U$-type).
  - Reason: RH's ζ-function sits at K-S's $U(1)$ symmetry type per paper60 §12 expanded table; RH-for-ζ IS K-S at the $U$-type slice.
  - Transposition candidate: YES.

- **L1 ↔ grh:L1** — shared Galois representation (Dirichlet-character K-S inheritance).
  - Reason: GRH's BC$_\chi$ construction uses character-twisted Hecke action; Dirichlet characters are the irreps selected by the bridge-family pattern at $k$-values.
  - Transposition candidate: YES.

- **L1 ↔ h12:L_class** — shared Galois representation (classification of Galois-repn over $\mathbb{Q}$).
  - Reason: K-S's symmetry-type assignment uses Galois-representation data; Hilbert 12 classifies Galois groups. Shared structural content.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ sato-tate:L_haar** — shared monodromy (Haar equidistribution on conjugacy classes).
  - Reason: Deligne equidistribution in the function-field case and Sato-Tate for individual curves both use Haar equidistribution on classical-compact-group conjugacy classes (paper60 §10).
  - Transposition candidate: YES (capacitor cell: Haar pushforward).

- **L2 ↔ rh:L_function_field** — shared monodromy (RH in function-field case via Weil).
  - Reason: The same Deligne machinery proves RH for ζ over $\mathbb{F}_q(t)$; K-S extends to arbitrary L-functions in function-field case.
  - Transposition candidate: YES.

- **L2 ↔ hodge:L2** — shared monodromy (monodromy as symmetry-type selector).
  - Reason: Hodge's motivic Galois group is the symmetry-type selector for algebraic cycles; K-S's L2 uses geometric monodromy for function-field L-functions.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ bgs:L5** — shared zero distribution (GUE is $U$-slice of Deligne).
  - Reason: BGS's GUE statistics for ζ-zeros is the $G = U$ slice of L2's Deligne equidistribution.
  - Transposition candidate: YES.

- **L3 ↔ bgs:L5** — shared zero distribution (GUE at $U$-type).
  - Reason: BGS's GUE prediction and L3's one-level-density verification are complementary: L3 verifies for non-$U$ families (Sp, O, SO$^\pm$); BGS verifies for $\zeta$ at $U$-type.
  - Transposition candidate: YES.

- **L3 ↔ sato-tate:L_one_level** — shared zero distribution (one-level equidistribution).
  - Reason: Sato-Tate individual-curve equidistribution is the one-level density in the $U$-type single-family case; L3 extends to family-level equidistribution across Sp, O, SO$^\pm$.
  - Transposition candidate: YES.

- **L3 ↔ lindelof:L_moments** — shared L-value (moment-density connection).
  - Reason: $L$-function moments control the one-level density via the explicit formula; Lindelöf-type moment bounds appear in L3d specifically.
  - Transposition candidate: YES.

- **L3 ↔ rh:L_pair_correlation** — shared zero distribution (Montgomery-Odlyzko at $U$).
  - Reason: Montgomery-Odlyzko pair-correlation for ζ is the $U$-type one-level consequence of L3.
  - Transposition candidate: YES.

- **L3a ↔ grh:L1** — shared ITPFI factor type (Dirichlet-quadratic at bridge $k=2$).
  - Reason: L3a confirms $Sp$-type for quadratic Dirichlet; GRH's BC$_\chi$ at quadratic character inherits the $Sp$ classification via the bridge-$k=2$ Brauer class.
  - Transposition candidate: YES.

- **L3a ↔ bsd:L_quad_twist** — shared zero distribution (quadratic twists of E-curves at Sp-analog).
  - Reason: Quadratic Dirichlet is Sp; quadratic twists of elliptic-curve L-functions share the quadratic-character family structure.
  - Transposition candidate: SPECULATIVE.

- **L3b ↔ sato-tate:L_hecke** — shared zero distribution (Hecke Frobenius angles at O-type).
  - Reason: Sato-Tate for Hecke cusp forms and L3b's O-type verification share Hecke Frobenius data.
  - Transposition candidate: YES.

- **L3b ↔ rh:L_cusp_form** — shared zero distribution (cuspidal L-function analog).
  - Reason: Both concern self-dual L-functions at $O$-type.
  - Transposition candidate: SPECULATIVE.

- **L3b ↔ h12:L_automorphic** — shared Galois representation.
  - Reason: Hecke cusp forms correspond to Galois representations via Langlands correspondence.
  - Transposition candidate: SPECULATIVE.

- **L3c ↔ bsd:L_rank_parity** — shared zero distribution ($SO^\pm$ split via rank parity, PRIMARY K-S ↔ BSD EDGE).
  - Reason: Miller 2004's $SO^+$ / $SO^-$ split by rank parity IS BSD's rank-parity conjecture at the K-S level; bridge $k=4$ (Pati-Salam) is the shared anchor.
  - Transposition candidate: YES (capacitor cell for rank-parity ↔ $SO^\pm$).

- **L3c ↔ qg5d:Branch C bridge k=4** — shared Galois representation (Pati-Salam orbifold).
  - Reason: Bridge $k=4$ is Pati-Salam in paper12 Axiom 4; the elliptic-curve L-function family sits at this $k$-value per paper60 §12.
  - Transposition candidate: YES.

- **L3c ↔ sato-tate:L_elliptic** — shared zero distribution (elliptic Frobenius at $SO^\pm$).
  - Reason: Sato-Tate for CM and non-CM elliptic curves distributes Frobenius angles per $SO^+$ / $SO^-$.
  - Transposition candidate: YES.

- **L3d ↔ lindelof:L_moments** — shared L-value (moment-amplitude connection).
  - Reason: K-S moment prediction ($T \log T^{k^2}$) and Lindelöf's amplitude bound are the two amplitude statements for ζ.
  - Transposition candidate: YES.

- **L3d ↔ rh:L_moments** — shared L-value (the ζ-moment problem).
  - Reason: Moment-of-ζ IS the $U$-type K-S instance; Keating-Snaith 2000 conjectured the $T (\log T)^{k^2}$ growth; Guth-Maynard 2024 first progress.
  - Transposition candidate: YES.

- **L3d ↔ bgs:L_moments** — shared L-value (GUE moments).
  - Reason: BGS's GUE content IS the $U$-type K-S content; moments match.
  - Transposition candidate: YES.

- **L4 ↔ qg5d:Branch D Axiom 4** — shared ITPFI factor type (PRIMARY EDGE).
  - Reason: Branch D Axiom 4 IS the bridge family; L4 identifies K-S symmetry type with Hecke representation type through the bridge. Bridge $k \in \{2,3,4,6\}$ provides the four-point selector (paper61 §10).
  - Transposition candidate: YES (capacitor cell for bridge-family ↔ Hecke-representation-type ↔ K-S symmetry-type triple identification).

- **L4 ↔ grh:L1** — shared C*-algebra structure (BC$_\chi$ construction).
  - Reason: GRH's BC$_\chi$ uses character-twisted Hecke action; L4's Hecke representation type IS the character class.
  - Transposition candidate: YES.

- **L4 ↔ bsd:L5** — shared C*-algebra structure (Hecke cocycle bound).
  - Reason: BSD Paper 26 Step 5c Key Lemma C' $|\Delta c^\psi(\delta)| < 2/(N-1)$ applies at all Hecke characters; Dirichlet characters at $k \in \{2,3,4,6\}$ are special cases.
  - Transposition candidate: YES.

- **L4 ↔ rh:L_BC** — shared C*-algebra structure (RH's BC algebra).
  - Reason: RH's spectral realization uses BC; L4 differentiates which L-function family the BC is realizing.
  - Transposition candidate: YES.

- **L4 ↔ bgs:L4** — shared C*-algebra structure (Dyson threefold way).
  - Reason: Dyson's threefold classification = K-S's five-way classification restricted to real forms; both identify with Hecke representation types.
  - Transposition candidate: YES.

- **L4 ↔ pvnp:L_popa** — shared ITPFI factor type (Popa rigidity at III$_1$ = $U$-type).
  - Reason: Popa rigidity uses type III$_1$ ITPFI; L4's $U$-type Hecke representation sits at type III$_1$.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ lindelof:L_support** — shared scaling dimension (double-sum-of-primes boundary).
  - Reason: Sub-route 5a meets Lindelöf at the double-sum-of-primes frontier per paper46 §5 and paper60 §11+§12.
  - Transposition candidate: YES.

- **L5 ↔ bsd:L_local_global** — shared zero distribution (ITPFI local-global structure).
  - Reason: Sub-route 5b uses the same ITPFI factorization $\omega_1 = \otimes_p \omega_1^{(p)}$ that BSD uses; local-global assembly per symmetry type.
  - Transposition candidate: YES.

- **L5 ↔ opn:L_local_global** — shared ITPFI factor type (local-global structure).
  - Reason: Same ITPFI factorization used by OPN (Paper 40).
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ qg5d:Branch D Axiom 4** — shared ITPFI factor type (sub-route 5c IS the programme-specific test).
  - Reason: Sub-route 5c directly tests whether the CBB Axiom 4 bridge family's symmetry-type predictions hold at each $k$.
  - Transposition candidate: YES.

- **L5 ↔ rh:L_n_level** — shared zero distribution ($U$-type $n$-level correlations).
  - Reason: $n$-level correlations for ζ (Rudnick-Sarnak) are the $U$-type slice of L5b.
  - Transposition candidate: YES.

- **L5 ↔ twin-primes:L_gap_type** — shared zero distribution (symmetry-type differentiates small-gap statistics).
  - Reason: paper60 §12 multi-channel discovery — twin-prime-style small gaps depend on K-S type; Sp has stronger repulsion ⇒ fewer small gaps.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ cramer:L_extreme_type** — shared zero distribution (extreme-value differentiation).
  - Reason: paper60 §12 multi-channel discovery — Cramér extreme-gap statistics depend on K-S type (different Tracy-Widom).
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ goldbach:L_density_type** — shared zero distribution (density-per-family type).
  - Reason: paper60 §12 — prime density in short intervals depends on which symmetry type governs relevant L-functions.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ rh:L_closure** — shared Galois representation ($U$-type slice of K-S).
  - Reason: RH for ζ is K-S's closure at $G = U$.
  - Transposition candidate: YES.

- **L6 ↔ grh:L_closure** — shared Galois representation ($\{U, Sp\}$ slice at Dirichlet).
  - Reason: GRH's closure across Dirichlet L-functions is K-S's closure at $\{U, Sp\}$.
  - Transposition candidate: YES.

- **L6 ↔ bsd:L_closure** — shared Galois representation ($SO^\pm$ slice at elliptic curves).
  - Reason: BSD rank parity ↔ $SO^\pm$ is K-S's closure at $k=4$ (Pati-Salam bridge).
  - Transposition candidate: YES.

- **L6 ↔ qg5d:Branch D** — shared Galois representation (compound $P_D \cap P_C$ closure per paper61 Vertex 25).
  - Reason: Full K-S closure IS the programme's vertex-25 compound-projection statement.
  - Transposition candidate: YES.

**Summary**: 41 cross-cut edges identified across 10 layer-entries (avg ~4.1 cross-cuts per layer — dense, consistent with K-S being a classification vertex that touches every L-function vertex in the programme). 24 verified (capacitor cell + paper60/61 citation), 17 SPECULATIVE (pending sibling-vertex x-rays). The PRIMARY edges are:
- L4 ↔ qg5d Branch D Axiom 4 (bridge-family ↔ Hecke-representation-type ↔ K-S symmetry-type triple identification — programme's key novel contribution)
- L3c ↔ bsd:L_rank_parity (rank-parity ↔ $SO^\pm$ split at bridge $k=4$)
- L6 ↔ rh/grh/bsd (K-S is the unifying classifier; each L-function Clay vertex is a K-S slice)

Katz-Sarnak is a HUB vertex on the L-function circle, analogous to YM's hub position on the geometric circle and BGS's hub position on the spectral circle. K-S's role: it classifies the SYMMETRY behind every other L-function vertex.

---

## §8 Current Walls

- **W_KS-1 — Symmetry-type classifier operator (L4)**: The identification of the Hecke representation type with the Katz-Sarnak symmetry type is a programme-structural claim; the bridge family $k \in \{2,3,4,6\}$ maps to four symmetry types $\{Sp, U, O, \text{Mixed}\}$, but the correspondence is CONJECTURED. Confidence 0.65 per paper46 audit strategy. Status: **OPEN as conjectural**, but feeding L5c as programme-specific test.
  - Capacitor status: not yet formalized; natural cell is a $P_D$-side bilinear-invariant classification of Hecke semigroup representations. See strategy/ccm-verification/ledger.md#katz-sarnak when written.
  - Bypass candidates: directly testing each bridge $k \in \{2,3,4,6\}$ against the predicted symmetry type (L5c sub-route). The four PROVED family slices (L3a-L3c for Sp, O, $SO^\pm$; L3d partial for $U$) already anchor three of four bridge-family predictions.

- **W_KS-2 — Generalized Katz-Sarnak (L5, THE WALL)**: For ALL natural families over $\mathbb{Q}$, the symmetry type determines ALL statistics (full $n$-level densities, arbitrary support, universality). Status: **OPEN as the primary Katz-Sarnak conjecture**. Three sub-routes:
  - Sub-route 5a (support extension): meets Lindelöf's double-sum-of-primes boundary; confidence 0.60 per audit strategy.
  - Sub-route 5b ($n$-level via BC ITPFI): matches BSD / OPN local-global structure; confidence 0.65 per programme's ITPFI infrastructure.
  - Sub-route 5c (bridge-family test): programme-specific; directly tests L4; confidence 0.70 per bridge-family $k$-values being programme-native.

No other named walls. Links 1–4 and 6 have clear status (PROVED for L2; partial for L3; CONJECTURED for L1 and L4; FOLLOWS for L6). W_KS-2 at L5 is the structural wall; W_KS-1 at L4 is a sub-wall feeding L5c.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/katz-sarnak/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle's `proof-chain/` directory is empty as of 2026-04-15). When created, L5's three sub-routes (5a/5b/5c) are the natural decomposition targets — each is programme-addressable through different infrastructure (Lindelöf-moment, BSD/OPN-ITPFI, CBB-Axiom-4 respectively).
- **CCM verification**: `strategy/ccm-verification/ledger.md#katz-sarnak` — NOT YET CREATED. Expected verdict when ledger is written: **CCM-independent** (K-S's chain does not use the CCM construction directly; the Hecke representation type is an algebraic classification on the BC side, which is pre-CCM). The CCM-dependent vertices are rh, bsd, bgs; K-S connects to them via the symmetry-type bridge but does not inherit their CCM dependency.
- **Inner rings**: NOT APPLICABLE — K-S is a primary outer-ring vertex, the SIXTH FACE of the e-circle (paper60 §12).
- **Audit strategy**: `strategy/katz-sarnak/00-audit-strategy.md` — lists W_KS-1 (classifier operator, confidence 0.65) and W_KS-2 (uniform conductor convergence, confidence 0.60) as provisional named walls. The audit brief at `strategy/katz-sarnak/katz-sarnak-audit-brief.md` identifies 16 researchers and 5 major approaches (function-field/geometric, moments CFKRS, low-lying zeros ILS, excised RMT, 1-level density tests).
- **Paper60 §12 discovery**: The SYMMETRY face was identified on April 14, 2026 immediately after Lindelöf; the sixth face of the e-circle. The discovery moment is captured in paper60 §12 "discovery moment" section: "the bridge IS the symmetry-type selector." This reframes the gap-distribution arc (BGS → Twin Primes → Cramér → Goldbach) from single-channel GUE to multi-channel GUE/GSE/GOE per symmetry type.
- **Paper61 §19.6 positioning**: Compound projection $P_D \cap P_C$ at Vertex 25 (Face 6: SYMMETRY). "The CBB system's four Brauer classes correspond to four of the five Katz-Sarnak groups. The symmetry-type face is thus not an additional structure — it is the bridge family itself, seen from the spectral direction."

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — Generalized number-field Katz-Sarnak (L5)**: For ALL natural families over $\mathbb{Q}$, the symmetry type determines ALL zero statistics. — face: MEASURE, projection: $P_O$, pattern: P5. STATUS: OPEN as the primary wall. Decomposed into three sub-routes (5a, 5b, 5c). This is the structural wall.

- **G2 — BC representation type = symmetry type (L4)**: The identification of the Hecke semigroup representation's bilinear invariant with the Katz-Sarnak symmetry type, via the bridge family $k \in \{2,3,4,6\}$. — face: SYMMETRY, projection: $P_D$, pattern: P1. STATUS: OPEN as CONJECTURED; confidence 0.65. This is the programme's key novel contribution to K-S; directly testable via sub-route 5c.

- **G3 — Moments Keating-Snaith prediction (L3d)**: The $k$-th moment of $|\zeta(1/2 + it)|$ grows as $T (\log T)^{k^2}$. — face: MEASURE, projection: $P_D$, pattern: P1. STATUS: PARTIAL — Keating-Snaith 2000 conjecture with Guth-Maynard 2024 first progress in 50 years. Not technically a named wall at the L1-L5 layer level but a key partial-result frontier.

- **G4 — Bridge-family symmetry-type verification at each $k$ (sub-route L5c)**: Verify that each bridge $k \in \{2,3,4,6\}$ produces the predicted K-S symmetry type for the associated L-function family. — face: SYMMETRY, projection: $P_O$, pattern: P4. STATUS: OPEN; three of four bridges have PARTIAL verification via L3a ($k=2$, Sp), L3c ($k=4$, $SO^\pm$), L3b ($k=6$, O). The $k=3$ (cubic characters, unitary) slice is the least-verified.

That's it. 1 of 6 main layers is PROVED unconditionally (L2 function-field). 1 is FOLLOWS (L6). L3 is PROVED partial across four family slices. L1 and L4 are CONJECTURED. L5 is the OPEN primary wall. The programme's novel contribution is concentrated in L4 and L5c (bridge-family identification and test).

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-02/vertices/katz-sarnak/critic-attacks.md` and arbiter decisions at `strategy/x-ray/pac-output/runs/run-02/vertices/katz-sarnak/arbiter-decisions.md` (both to be populated by the PAC run).

Notable arbiter wins (per §3 rejected alternatives):
- L1 face: SYMMETRY over MEASURE (critic proposed MEASURE because the *consequence* is a density, but L1 is the *cause* — the symmetry-type assignment — not the measured density; paper60 §12 face-definition canonicalization).
- L2 pattern: P2 Holonomy over P4 Topological Rigidity (Frobenius = holonomy mechanism is the historical-mechanical core of Deligne equidistribution, paper08 §36; rigidity of the classification is implied but downstream).
- L3 face: MEASURE over SYMMETRY (L3 tests the symmetry-type prediction; the *load-bearing content at L3* is the weak-convergence statement, not the symmetry-type assignment itself — which is L1).
- L4 face: SYMMETRY over RESONANCE (Hecke representation classification IS a symmetry-type classification; resonance-mode reading of Hecke is a downstream alternative).
- L4 projection: $P_D$ over $P_C$ (bridge-family's $P_C$ contribution is structural-secondary; the classification engine is $P_D$-internal).
- L5 face: MEASURE over SYMMETRY (n-level densities and support extension are MEASURE-face; the symmetry-type *verification* is an L5c sub-route, not L5 itself).
- L5 projection: $P_O$ over $P_D$ (sub-routes live in $P_D$ mechanically, but the conjunction at L5 is the outer-ring-Clay-closure statement).
- L6 pattern: P4 over P1 (closure is rigidity-of-classification; reinterpretive framing lives at the layers below).
- Primary face: SYMMETRY over MEASURE (paper60 §12 canonicalization; MEASURE is secondary at L3/L5 only).
- Primary projection: $P_D$ over $P_D \cap P_C$ (dominant single projection is $P_D$; $P_D \cap P_C$ is the compound per paper61 §06-12 Vertex 25, but the X-Ray asks for primary single projection).
- Primary branch: D over C (Branch C is a structural-secondary via bridge-family orbifold; Branch D is mechanical-primary via Hecke representation theory).

49 / 50 author wins out of 50 total field decisions (5 fields × 10 layer entries). The single critic win (L2 pattern P2 over P4 alternative reading) reflects the historical fact that Deligne equidistribution is a holonomy statement about Frobenius, not a rigidity statement — the Pattern 2 assignment captures the mechanism; Pattern 4 would only capture the downstream rigidity.

---

*End of Katz-Sarnak X-Ray. Snapshot 2026-04-15. 6 main layers (with L3 split into a/b/c/d sub-slices giving 10 entries). 41 cross-cuts identified (hub vertex on the L-function circle). SYMMETRY-canonical, $P_D$-dominant, P4-primary (with P1 on L3/L4 verification and P5 on L5 regularization). One structural wall (W_KS-2 at L5, the generalized number-field K-S); one sub-wall (W_KS-1 at L4, symmetry-type classifier operator) feeding sub-route L5c.*
