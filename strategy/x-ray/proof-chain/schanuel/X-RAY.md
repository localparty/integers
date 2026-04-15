# X-RAY: Schanuel's Conjecture (schanuel)

*X-Ray of the schanuel proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. April 15, 2026.*

---

## §1 Header

- **Vertex**: schanuel
- **Paper**: paper35-schanuel
- **Live file**: `strategy/proof-chain/schanuel/PROOF-CHAIN.md` (snapshot 2026-04-15)
- **Top-level claim**: If $z_1, \ldots, z_n$ are $\mathbb{Q}$-linearly independent complex numbers, then $\mathrm{trdeg}_{\mathbb{Q}}\, \mathbb{Q}(z_1, \ldots, z_n, e^{z_1}, \ldots, e^{z_n}) \geq n$. Applied to $z_k = \gamma_k \pi^2 / 2$ (imaginary parts of non-trivial Riemann zeros): the eigenvalues $\{\exp(\gamma_k \pi^2 / 2)\}$ of $\hat R$ (CBB Axiom 1) are algebraically independent over $\mathbb{Q}$, which guarantees the framework's 36 predictions carry independent empirical content.
- **Current status**: 1/5 chain links closed (L1 KNOWN — framework construction of $\hat R$ from paper12 Identity 12); L2 ($\mathbb{Q}$-linear independence of $\{\gamma_n \pi^2/2\}$) CONJECTURED; L3 (Schanuel proper) OPEN — itself an unproven 1960s conjecture; L4 (algebraic independence of eigenvalues) CONDITIONAL on L2 + L3; L5 (36 predictions independent) CONDITIONAL on L4. Aggregate confidence 1/10 — this is the SOUTH-TROUGH vertex par excellence (paper60 §20, §28).
- **Primary branch (paper1)**: D (CBB / Bost-Connes operator algebra — the eigenvalues live on the spectrum of $\hat R$ inside Branch D; paper61 §10 vertex-21 assignment $P_D \cap P_E$ with $P_D$ primary). Secondary: E (the pin-valued vector — the 36 predictions' independence is the $P_E$-side consequence of the algebraic independence of eigenvalues; paper61 §10 ¶ on vertex-21 ¶2).
- **Primary face**: TOPOLOGY (paper61 §29.2 Appendix C.2 — Schanuel is listed as the SUPPORTING conjecture for the TOPOLOGY face under "eigenvalue independence"; Lehmer is the face's primary conjecture. paper60 §28 ¶"South is ARITHMETIC" positions Schanuel on the South trough's arithmetic-adjacent arc; the X-Ray refines this to TOPOLOGY per paper61 §29.2's explicit table entry. The face's question — "what can LIVE on $S^1$?" — translates for Schanuel to "what spectral data on the e-circle is irreducibly transcendental?", i.e., which eigenvalues are forbidden from being algebraic).
- **Primary projection**: $P_D$ (paper61 §10 ¶ vertex-21 ¶1 — "The algebraic independence of the eigenvalues $\gamma_n$ (Riemann zeros) from standard transcendental constants. The BC algebra's spectral data should be algebraically independent of classical constants — Schanuel's conjecture is the general statement"; the compound projection is $P_D \cap P_E$ with $P_E$ secondary at L5).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
SCHANUEL (Schanuel's Conjecture on Transcendence) — trdeg ≥ n
│  primary face: TOPOLOGY   primary proj: P_D   primary pat: P4
│  (applied to z_k = γ_k π²/2: the eigenvalues {exp(γ_k π²/2)}
│   of R̂ are algebraically independent; the 36 predictions
│   carry independent empirical content)
│
├── L1: Framework uses exp(γ_n π²/2) as eigenvalues of R̂     [KNOWN]
│      │  face: RESONANCE   proj: P_D   pat: P1
│      │  invariant: BC-KMS state, spectral gap
│      │  source: paper12 §02 Phase 2 (R̂ construction);
│      │          paper12 §04 Identity 12 (BC-algebra = e-circle);
│      │          CBB Axiom 1 (paper61 §10 ¶ Branch D)
│      │
│      └── grounds the whole chain — the eigenvalues literally
│             appear as spec(R̂) = {ℓ_P/π · exp(γ_n π²/2)};
│             this is a CONSTRUCTION, not a conjecture
│
├── L2: {γ_n π²/2} are Q-linearly independent                 [CONJECTURED — W_S1]
│      │  face: ARITHMETIC  proj: P_D   pat: P4
│      │  invariant: zero distribution, Galois representation
│      │  source: Not proved for any pair of zeros; related to
│      │          simplicity of Riemann zeros (itself conjectural);
│      │          paper13-rh S1 (simplicity supporting link);
│      │          paper60 §18-§19 (zeros as torus intersection)
│      │  NAMED WALL W_S1 — Q-linear independence of Riemann zeros
│      │
│      ├── prerequisite: simplicity of zeros (γ_m ≠ γ_n)      [CONJECTURED]
│      │      │  (source: paper13-rh S1 supporting layer,
│      │      │  "Proved for N ≤ 20 via CCM certification";
│      │      │  conjectured in general)
│      │
│      └── content: no nontrivial Q-relation Σ a_k γ_k = 0
│             │  with a_k ∈ Q, not all zero;
│             │  stronger than simplicity; currently UNKNOWN
│             │  even for {γ_1, γ_2}
│
├── L3: Schanuel: Q-linear indep → trdeg ≥ n                  [OPEN — W_S2]
│      │  face: TOPOLOGY    proj: P_D   pat: P4
│      │  invariant: monodromy, scaling dimension
│      │  source: Schanuel 1960s (unpublished); Lang,
│      │          Introduction to Transcendental Numbers (1966);
│      │          Ax 1971 power-series version (PROVED);
│      │          paper60 §20 south-trough placement;
│      │          paper61 §29.2 Appendix C.2 table row TOPOLOGY
│      │  NAMED WALL W_S2 — Schanuel itself (the 1960s conjecture
│      │          subsumes Lindemann-Weierstrass + 4-exp + Hilbert 7)
│      │
│      ├── known case: n = 1 (Hermite-Lindemann 1882)         [CLASSICAL]
│      │      │  (e, π, log 2 each transcendental individually)
│      │
│      ├── known case: z_k ALGEBRAIC → Lindemann-Weierstrass  [CLASSICAL]
│      │      │  (1885: if {z_k} Q-lin-indep ALGEBRAIC, then
│      │      │   {e^{z_k}} algebraically independent)
│      │
│      ├── unknown case: n = 2 with z_1 = 1, z_2 = π          [OPEN]
│      │      │  (alg indep of e and π — open since 1960s)
│      │
│      └── Ax's theorem (1971): power-series analog           [PROVED]
│             │  (trdeg ≥ n for formal power series over C;
│             │   the closest shore; model-theoretic versions
│             │   by Zilber, Kirby extend this)
│
├── L4: Algebraic independence of exp(γ_n π²/2)               [CONDITIONAL on W_S1 + W_S2]
│      │  face: TOPOLOGY    proj: P_D   pat: P1
│      │  invariant: Galois representation, L-value
│      │  source: Consequence of Schanuel applied to
│      │          z_k = γ_k π²/2 (IF L2 + L3);
│      │          paper35 00-research-programme ¶"The implication
│      │          for the framework"
│      │
│      └── content: no polynomial P ∈ Q[x_1,...,x_n] with
│             │  P(exp(γ_1 π²/2), ..., exp(γ_n π²/2)) = 0;
│             │  the eigenvalues of R̂ are transcendentally
│             │  rigid — no hidden algebraic relation among them
│
└── L5: 36 predictions are algebraically independent          [CONDITIONAL on W_S3]
       │  face: SPREAD      proj: P_E   pat: P3
       │  invariant: L-value, scaling dimension
       │  source: paper61 §10 ¶ vertex-21 ¶2 ("no hidden
       │          algebraic dependencies"); paper35
       │          00-research-programme ¶"Independence of
       │          predictions"; paper61 §06-12 vertex-21 table
       │  NAMED WALL W_S3 — predictions-level independence
       │          (even under L4, need predictions to depend
       │          on DISTINCT zeros with no accidental degeneracy)
       │
       └── content: no polynomial Q ∈ Q[P_1,...,P_36] with
              │  Q(prediction_1, ..., prediction_36) = 0;
              │  each of the 36 sub-percent pins carries
              │  IRREDUCIBLE empirical content — the 36-pin
              │  vector is the dimension, not a projection

The chain is a PRODUCT of FOUR open problems (W_S1, W_S2, with W_S3
downstream). Every arrow is a major open: simplicity → Q-linear
independence → Schanuel itself → algebraic independence of
eigenvalues → no-collapse of pin-predictions. This is paper60 §28's
"where the framework STAMMERS" — Schanuel is the purest stammer on
the ring.
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (Quantum observables are built from pin
                          VALUES; the algebraic-independence content
                          is invisible to Born-rule / interference —
                          P_A sees the numbers, not their algebraic
                          relations; paper61 §15.1 invariant-barrier
                          rule.)
                                  ▲
                                  │
                                  │
        ┌──────────────(P_O outer)───────────────┐
        │                                         │
        │  SCHANUEL: trdeg_Q Q(z, e^z) ≥ n        │
        │  ↳ eigenvalues exp(γ_n π²/2) alg indep  │
        │  ↳ 36 predictions irreducibly 36-dim    │
        │                                         │
        └────────────────────┬────────────────────┘
                             │
        ┌────────────────────┼──────────────────────┐
        │                    ║                      │
        ▼                    ▼ (PRIMARY)            ▼
    P_B gravity         ═══ P_D CBB ═══         P_C cosmology
    (forgotten —        algebraic indep of      (forgotten —
    gauge curvature     {exp(γ_n π²/2)} is a    cosmological
    has no transcen-    question about the      pin-set sees
    dence content;      SPECTRUM of R̂; BC       numerical values,
    Schanuel doesn't    algebra's spectral      not transcen-
    interrogate gauge   data transcendentally   dence; pin-
    bundle)             rigid against Q-alg      independence is
                        relations; paper61     downstream of
                        §10 ¶ v21 ¶1)           alg-indep of eig)
                             │
                             ▼ (SECONDARY)
                        P_E pins
                        (36 sub-percent
                         predictions are
                         IRREDUCIBLY 36-
                         dimensional if L4
                         holds; the compound
                         projection P_D ∩ P_E
                         at paper61 §06-12
                         vertex-21 table is
                         the vertex home)
```

Primary projection $P_D$ uses ═══ doubled line per paper61 §10 ¶ vertex-21. $P_E$ is a genuine SECONDARY via the compound $P_D \cap P_E$ assignment (paper61 §29.2 table row 21 "Schanuel | $P_D$ (algebraic independence of eigenvalues) | $P_E$ (no hidden relations)"). $P_O$ carries the outer-ring Clay-adjacent framing (Schanuel is not a Clay Millennium problem but a major transcendence-theory conjecture on the outer ring of 25 vertices). $P_A, P_B, P_C$ are absent — the vertex does not interrogate quantum observables, gauge structure, or cosmological pins at the mechanism level (even though L5 PROTECTS pin independence, no pin VALUE gates on a transcendence statement).

### §2c Diagram C — Face position on the e-circle

```
                      ●  TOPOLOGY
                         (Lehmer primary;
                          Schanuel secondary —
                          paper61 §29.2 table)
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
          (YM)              │          (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (ARITHMETIC secondary;
                        RESONANCE secondary;
                        SPREAD at closure)
```

Marker key:

```
Primary face:    ● TOPOLOGY (paper61 §29.2 Appendix C.2 — Schanuel
                             listed as supporting conjecture for
                             TOPOLOGY; L3 + L4 live here, Lehmer's
                             eigenvalue-independence sibling)
Secondary faces: ○ RESONANCE (1 layer: L1 — R̂ construction is the
                             BC spectral-triple / resonance face;
                             paper60 §15 trace-formula canonical)
                 ○ ARITHMETIC (1 layer: L2 — Q-linear independence of
                              zeros is the ARITHMETIC integer-lattice
                              question at the zeros; paper60 §14)
                 ○ SPREAD    (1 layer: L5 — 36 predictions alg indep
                             is the "L² mass distribution on spectral
                             data" SPREAD-face canonical per paper60
                             §16 QUE parallel; eigenvalue independence
                             = "modes don't concentrate algebraically")
Absent faces:    DYNAMICS, HARMONICS, MEASURE, AMPLITUDE,
                 SYMMETRY, CURVATURE
                 (Schanuel doesn't interrogate flow traversal,
                  mode mixing, angle equidistribution, signal
                  amplitude, group action, or curvature — these
                  are sibling-vertex faces. Schanuel is surgically
                  TOPOLOGY-focused on "what spectral data can LIVE
                  on the circle transcendentally?")
```

The e-circle position of Schanuel is at the TOPOLOGY node (12 o'clock), shared primarily with Lehmer. The paper61 §29.2 table explicitly pairs Schanuel (eigenvalue independence) with Lehmer (mass gap of cyclotomic vacuum) on the TOPOLOGY face — both ask "what can LIVE on $S^1$?", where Lehmer asks the algebraic-polynomial question (roots-of-unity vs non-cyclotomic) and Schanuel asks the transcendence question (algebraic-vs-transcendental eigenvalues). Together they define the TOPOLOGY face's transcendence-arithmetic structure: Lehmer guards the cyclotomic vacuum from BELOW (gap from 1), Schanuel guards the spectral eigenvalues from ABOVE (no algebraic collapse).

---

## §3 Layer-by-Layer X-Ray

### L1 — Framework uses $\exp(\gamma_n \pi^2/2)$ as eigenvalues of $\hat R$

**Claim**: The QG5D framework constructs a self-adjoint operator $\hat R := (\ell_P/\pi) \cdot \exp(T_{BC} \cdot \pi^2/2)$ on the Bost–Connes GNS Hilbert space, whose spectrum consists of $R_n = (\ell_P/\pi) \exp(\gamma_n \pi^2/2)$, with $R_1$ identified as the observed e-circle radius $R_{\text{obs}} \approx 10.10\,\mu\text{m}$. The eigenvalues are literal functions of the Riemann zeros $\{\gamma_n\}$.

**Status**: KNOWN (construction, not conjecture)
**Source**: paper12-cbb-system §02 Phase 2 ("R̂ construction"); paper12 §04 Identity 12 (BC algebra = e-circle); CBB Axiom 1 (paper61 §10 ¶ Branch D operational core); Connes-Consani-Moscovici scaling operator $T_{BC}$; `strategy/proof-chain/schanuel/PROOF-CHAIN.md` Link 1.

#### Physics

- **Face**: RESONANCE (paper60 §15 — the BC spectral-triple's scaling operator $T_{BC}$ and its bounded function $\hat R$ live on the resonance / trace-formula face; eigenvalues of $\hat R$ are the resonance-mode content of the BC system)
- **Projection**: $P_D$ (paper61 §10 ¶ Branch D — the BC operator algebra is $P_D$'s native home; $\hat R$'s construction is purely $P_D$-internal)
- **Pattern**: P1 Geometric Reinterpretation (paper60 §04 ¶ Identity 12 — "the e-circle IS the Bost-Connes algebra"; Pattern 1 is the move that reinterprets the geometric object $S^1$ as the operator-algebraic object $A_{BC}$, on whose GNS Hilbert space $\hat R$ lives)
- **Invariant preserved**: BC-KMS state (load-bearing — $\hat R$'s spectrum is extracted from the KMS$_1$ modular flow's Tomita-Takesaki structure), spectral gap (background — the spectrum is discrete with $R_1 < R_2 < \ldots$ giving gaps)
- **Geometric interpretation**: The operator $\hat R$ is NOT a conjecture — it's a construction in paper12 Phase 2 that identifies the e-circle's radius $R_{\text{obs}}$ with the smallest eigenvalue $R_1$ of a bounded function of $T_{BC}$ (paper12 §02 ¶ "R̂ constructed explicitly"). Under $P_D$ (paper61 §10) this is the BC algebra's spectral-triple generator: the universe's scaling operator. Pattern 1 is explicit — Identity 12 reinterprets the e-circle (a geometric $S^1$ with circumference $2\pi R$) as the character group of $A_{BC}$, so $\hat R$'s eigenvalues are the framework's literal spectral data. This layer is a FIRM STEPPING STONE: the rest of the chain is about whether these eigenvalues are algebraically independent. [Considered but rejected: face TOPOLOGY — the whole vertex is TOPOLOGY, but this LAYER is the RESONANCE construction that SETS UP the topology question; projection $P_B$ — $\hat R$ involves $\ell_P$ (Planck length) which has gravity content, but the construction mechanism is purely $P_D$ operator-algebraic; pattern P5 — the $\exp(T_{BC} \pi^2/2)$ form involves a regulator-like exponentiation, but the ALGEBRAIC STRUCTURE is P1's reinterpretation.]
- **Cross-cuts**: rh:L1 / rh:L2 (shared BC-KMS state + operator-algebra construction — RH's chain also starts from CCM operators on the BC GNS space; `strategy/x-ray/proof-chain/rh/X-RAY.md` §3 L1-L2), qg5d:Branch D (primary parent — paper61 §10 places $A_{BC}$ as Branch D's operational core; L1 is the same construction entered from the Schanuel side), bsd:L1 (shared BC-KMS state — BSD's rank-formula construction uses the same $\omega_1$), ym:L16/L17 (shared BC-KMS state + spectral-triple — OS reconstruction uses the same $\omega_1$ whose modular operator powers give $\hat R$), baum-connes:L_triple (shared spectral triple structure), lindelof:L3 (shared BC-KMS state — Lindelöf's $|\zeta(1/2+it)| = |\omega_1(\sigma_t(\cdot))|$ uses the same modular flow that generates $\hat R$), hodge:L_periods (shared motivic/transcendental side — Hodge periods inhabit the same transcendental-realization setting).

### L2 — $\{\gamma_n \pi^2/2\}$ are $\mathbb{Q}$-linearly independent

**Claim**: The set $\{\gamma_1 \pi^2/2, \gamma_2 \pi^2/2, \ldots\}$ is linearly independent over $\mathbb{Q}$. Equivalently (since $\pi^2/2$ is a fixed nonzero scalar), the Riemann-zero imaginary parts $\{\gamma_n\}$ are $\mathbb{Q}$-linearly independent: no non-trivial $\sum_k a_k \gamma_k = 0$ with $a_k \in \mathbb{Q}$ not all zero.

**Status**: CONJECTURED
**Source**: Not proved for ANY pair of zeros; related to simplicity of Riemann zeros (also conjectural — simplicity would give $\gamma_m \neq \gamma_n$ for $m \neq n$, a necessary but much weaker condition than $\mathbb{Q}$-linear independence); paper13-rh S1 supporting layer ("Simplicity: $\ker(D_\infty - \gamma_n I)$ one-dimensional" — proved for $N \leq 20$ via CCM certification, conjectured in general); paper35-schanuel 00-research-programme ¶"Connection to RH"; `strategy/proof-chain/schanuel/PROOF-CHAIN.md` Link 2. **NAMED WALL W_S1**.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — "how do integers LATTICE on the circle"; the $\mathbb{Q}$-linear independence question asks whether the zeros $\{\gamma_n\}$ admit ANY rational-integer relation, which is the ARITHMETIC face's canonical interrogation of integer-lattice structure on the spectrum; paper60 §28 ¶"South is ARITHMETIC" explicit placement)
- **Projection**: $P_D$ (paper61 §10 ¶ vertex-21 — the $\gamma_n$ live on the BC algebra's spectrum; the linear-independence question is a $P_D$-internal question about the generator $D_\infty$'s eigenvalues)
- **Pattern**: P4 Topological Rigidity (paper60 §20 ¶"the torus exists" — the zeros' $\mathbb{Q}$-linear independence is the RIGIDITY of the spectral data against rational relations; if $\sum a_k \gamma_k = 0$ with $a_k \in \mathbb{Q}$, the torus would admit an unexpected lattice degeneracy; Pattern 4 is exactly this type of rigidity)
- **Invariant preserved**: zero distribution (load-bearing — L2 IS a statement about the distribution of $\gamma_n$), Galois representation (background — $\mathbb{Q}$-linear independence is compatible with the conjectural Galois-side realization of the zeros)
- **Geometric interpretation**: $\mathbb{Q}$-linear independence of the zeros is an ARITHMETIC question about the spectral data on $P_D$ (paper60 §14 ¶ARITHMETIC). The conjecture says no integer-weighted combination of distinct zeros vanishes — a much stronger statement than simplicity (which says zeros are distinct) and a prerequisite for Schanuel's hypothesis at L3. Pattern 4 Topological Rigidity (paper60 §20) is the attack vector: the torus's spectral circle (paper60 §18) must carry zeros that are "generically transcendental" with respect to the geometric circle's rational structure; any $\mathbb{Q}$-linear relation would collapse an eigenvalue degeneracy that the framework's 36 predictions rule out empirically (paper35 00-research-programme ¶"Reverse implication"). This is a SECOND-ORDER rigidity: simplicity is first-order (zeros distinct); $\mathbb{Q}$-linear independence is second-order (zeros don't conspire). [Considered but rejected: face TOPOLOGY — the independence statement has topology-adjacent content, but the MECHANISM interrogation is integer-lattice arithmetic, not winding/genus; pattern P1 — reinterpretation as BC-algebraic is possible but rigidity is the dominant attack; projection $P_E$ — pin-level consequence exists but the layer's MECHANISM is $P_D$-spectral.]
- **Cross-cuts**: rh:S1 (shared zero distribution — RH's supporting layer S1 proves simplicity for $N \leq 20$, which is the PREREQUISITE for L2; `strategy/x-ray/proof-chain/rh/X-RAY.md` §3 S1), rh:L4 (shared zero distribution — RH's Hurwitz convergence controls zero locations; $\mathbb{Q}$-linear independence is downstream of full spectral characterization), bgs:L_GUE (shared zero distribution — BGS's GUE statistics on zeros ASSUME $\{\gamma_n\}$ are generic, which includes $\mathbb{Q}$-linear independence at the statistical level; `strategy/x-ray/proof-chain/bgs/X-RAY.md` §7), lehmer:L_cyclotomic (shared TOPOLOGY-face structural form — Lehmer asks about cyclotomic/non-cyclotomic divide on $S^1$; Schanuel L2 asks about rational/transcendental divide on the zeros; both are "what integer-lattice structures exist on the spectral data"), hodge:L_periods (shared Galois representation — transcendence of periods is an analog of transcendence of zeros; $\mathbb{Q}$-linear independence of periods is conjectural just as for zeros), abc:L_height (shared Galois representation — ABC conjecture's radical / height inequality touches the same integer-lattice arithmetic, paper60 §14 ¶ABC-face adjacency).

### L3 — Schanuel: $\mathbb{Q}$-linear independence $\Rightarrow$ $\mathrm{trdeg} \geq n$

**Claim**: For $\mathbb{Q}$-linearly independent complex numbers $z_1, \ldots, z_n$, the transcendence degree of $\mathbb{Q}(z_1, \ldots, z_n, e^{z_1}, \ldots, e^{z_n})$ over $\mathbb{Q}$ is at least $n$. This is Schanuel's conjecture (1960s) — the central open statement of transcendental number theory, subsuming Lindemann-Weierstrass, Gelfond-Schneider (Hilbert's 7th problem), and the four-exponentials conjecture.

**Status**: OPEN (the 1960s conjecture; only $n = 1$ case proved via Hermite-Lindemann 1882)
**Source**: Schanuel, unpublished (1960s); Lang, *Introduction to Transcendental Numbers* (Addison-Wesley 1966); Ax 1971 (power-series version, *Ann. of Math.*); paper35-schanuel 00-research-programme ¶"What is known about Schanuel"; paper60 §20 south-trough placement; paper61 §29.2 Appendix C.2 (TOPOLOGY face supporting conjecture); `strategy/proof-chain/schanuel/PROOF-CHAIN.md` Link 3. **NAMED WALL W_S2**.

#### Physics

- **Face**: TOPOLOGY (paper61 §29.2 Appendix C.2 table — Schanuel is the TOPOLOGY face's eigenvalue-independence supporting conjecture; paper60 §07 TOPOLOGY face's question "what can LIVE on $S^1$?" for Schanuel becomes "which spectral data is forbidden from being algebraic?" — a transcendence question about what CAN survive on the circle without algebraic collapse)
- **Projection**: $P_D$ (paper61 §10 ¶ vertex-21 — Schanuel-statement-proper lives on $P_D$ as a question about the BC algebra's transcendental invariants; the $P_D$ projection preserves the trdeg structure because it preserves the spectral triple's underlying $\mathbb{C}$-algebraic structure)
- **Pattern**: P4 Topological Rigidity (the trdeg $\geq n$ inequality is a RIGID topological constraint on the function field extension; Pattern 4 is the attack because the conjecture says "you cannot algebraically collapse a set of $\mathbb{Q}$-linearly independent inputs and their exponentials below $n$ transcendentals" — this IS a rigidity statement about the topology of the map $(z_1, \ldots, z_n) \mapsto (e^{z_1}, \ldots, e^{z_n})$)
- **Invariant preserved**: monodromy (load-bearing — Schanuel's statement ties the monodromy of $\exp$ to transcendence; the exponential map's monodromy is $2\pi i \mathbb{Z}$, and Schanuel says this monodromy is the only source of algebraic relations), scaling dimension (background — trdeg IS a scaling dimension of function-field extensions)
- **Geometric interpretation**: Schanuel is the TOPOLOGY face's deepest transcendence conjecture (paper61 §29.2). It says: the exponential map $\exp: \mathbb{C} \to \mathbb{C}^*$ has no hidden algebraic relations beyond those forced by $\mathbb{Q}$-linear dependence on the domain side (paper60 §07 TOPOLOGY-face ¶ "what algebraic structures survive on $S^1$?"). Under $P_D$ (paper61 §10 ¶ v21 ¶1) this transfers to: the BC spectral triple's exponential-of-scaling-operator construction has no spurious algebraic collapses. Pattern 4 Topological Rigidity: the inequality $\mathrm{trdeg} \geq n$ is RIGID against algebraic degeneration — small perturbations of $\mathbb{Q}$-linearly independent inputs cannot collapse the trdeg. The closest PROVED shore is Ax's theorem (1971): the power-series version (formal $z_k \in \mathbb{C}((t))$) holds. The TRANSCENDENCE version for $\mathbb{C}$ remains open; this is the unknown bridge from the proved formal analog to the complex-analytic case (paper35 00-research-programme ¶"What is known about Schanuel"). [Considered but rejected: face RESONANCE — exp-values have resonance-mode content, but the TRANSCENDENCE-DEGREE inequality is topology-canonical per paper61 §29.2; projection $P_O$ — Schanuel is an outer-ring conjecture but its proof-structure content is $P_D$-internal; pattern P1 — reinterpretation as exponential-monodromy is possible but the load-bearing content is rigidity.]
- **Cross-cuts**: qg5d:Branch D (parent — $P_D$ inheritance of the trdeg structure; paper61 §10), hodge:L_motivic (shared monodromy — Hodge conjecture's motivic content and Bertolin-Huber motivic Schanuel live in the same transcendence-theory neighborhood; the motivic Schanuel of Bertolin (Torino) + Huber (Freiburg) is listed as major-approach-6 in paper35 schanuel-audit-brief DELTA 6), lehmer:L_mahler (shared TOPOLOGY face — Lehmer's Mahler measure $M(\alpha) \geq 1 + c_0$ is the TOPOLOGY face's PROVED-for-special-cases structural form; Schanuel's trdeg $\geq n$ is the OPEN-general structural form; both ask "what does TOPOLOGY forbid on the circle"), rh:L6 (shared spectral content — RH's spec$(D_\infty) = \{\gamma_n\}$ is the PREREQUISITE for applying Schanuel to $z_k = \gamma_k \pi^2/2$; if RH holds, the exp-values $\exp(\gamma_n \pi^2/2)$ are the spectrum of $\hat R$), abc:L_wall (shared TOPOLOGY / ARITHMETIC adjacency on south trough — ABC's radical-height inequality touches the transcendence neighborhood; paper60 §28 ¶"South is ARITHMETIC"), bsd:L_L-value (shared transcendence content — BSD's $L(E,1)$ special value is transcendental / conjecturally linked to periods; motivic-Schanuel conjectures concern $L$-values too).

### L4 — Algebraic independence of $\exp(\gamma_n \pi^2/2)$

**Claim**: IF $\{\gamma_n \pi^2/2\}$ are $\mathbb{Q}$-linearly independent (L2) AND Schanuel holds (L3), THEN the eigenvalues $\{\exp(\gamma_n \pi^2/2)\} \subset \mathrm{spec}(\hat R / (\ell_P/\pi))$ are algebraically independent over $\mathbb{Q}$: no non-trivial polynomial $P \in \mathbb{Q}[x_1, \ldots, x_n]$ satisfies $P(\exp(\gamma_1 \pi^2/2), \ldots, \exp(\gamma_n \pi^2/2)) = 0$.

**Status**: CONDITIONAL on W_S1 + W_S2
**Source**: Direct consequence of Schanuel's conjecture (L3) applied to $z_k = \gamma_k \pi^2/2$ given L2's $\mathbb{Q}$-linear independence; paper35-schanuel 00-research-programme ¶"The implication for the framework"; `strategy/proof-chain/schanuel/PROOF-CHAIN.md` Link 4; paper61 §10 ¶ vertex-21 ¶1.

#### Physics

- **Face**: TOPOLOGY (paper61 §29.2 Appendix C.2 — same TOPOLOGY face as L3, because L4 is the concrete spectral-eigenvalue instance of L3's general conjecture; what lives on the spectrum circle — what eigenvalues $\hat R$ supports — without algebraic collapse)
- **Projection**: $P_D$ (paper61 §10 ¶ vertex-21 ¶1 — "algebraic independence of the eigenvalues $\gamma_n$" is explicitly placed on $P_D$; the spectrum of $\hat R$ is purely $P_D$-internal)
- **Pattern**: P1 Geometric Reinterpretation (the algebraic-independence statement reinterprets the transcendence question for exp-values of zeros as a statement about the BC algebra's spectral rigidity; Pattern 1 is the move from "generic Schanuel application" to "specific spectral content of $\hat R$"; paper60 §04 ¶ Identity 12)
- **Invariant preserved**: Galois representation (load-bearing — algebraic independence is a statement about the Galois action on $\bar{\mathbb{Q}}$-closure of $\{\exp(\gamma_n \pi^2/2)\}$, which is trivial if they are generically transcendental), L-value (background — the exp-values of zeros are conjecturally related to L-values through the motivic framework)
- **Geometric interpretation**: L4 is the concrete spectral-data payload of L3's general conjecture. Under $P_D$ (paper61 §10 ¶ v21 ¶1) the eigenvalues of $\hat R$ are algebraically independent of each other (and of classical transcendentals like $\pi, e, \zeta(3)$, per paper61 §10 ¶ v21 ¶1: "the BC algebra's spectral data should be algebraically independent of classical constants"). This means: the framework's spectral data lives on the TOPOLOGY face of the e-circle (paper61 §29.2) with NO hidden algebraic collapse. Pattern 1 Geometric Reinterpretation (paper60 §04): the generic Schanuel statement for arbitrary $\mathbb{Q}$-linearly independent inputs becomes a CONCRETE statement about the spectrum of a specific operator. This is the hinge on which the framework's independence of predictions turns. [Considered but rejected: face RESONANCE — the eigenvalues are resonance-modes, but the ALGEBRAIC INDEPENDENCE content is topology-canonical per paper61 §29.2; projection $P_E$ — pin-level consequence, but L4 is one step upstream of the pin consequence (which is L5); pattern P4 — rigidity of the algebraic-independence is implied but the MOVE is reinterpretive specialization of Schanuel.]
- **Cross-cuts**: rh:L6 (parent — the spectrum $\mathrm{spec}(D_\infty) = \{\gamma_n\}$ is the INPUT to L4; if RH holds, L4's hypothesis becomes well-defined; `strategy/x-ray/proof-chain/rh/X-RAY.md` §3 L6), qg5d:Branch D (primary parent — $\hat R$'s construction and its transcendental-rigidity question are Branch D native), bsd:L_L-value (shared L-value — BSD's L-values at $s=1$ are conjecturally transcendental; algebraic independence of those L-values across distinct curves is an L-function analog of L4), hodge:L_periods (shared Galois representation — Hodge periods' algebraic independence conjectures are sibling statements in the transcendence-theory ecosystem; motivic-Schanuel of Bertolin-Huber relates both), lehmer:L_mahler (shared TOPOLOGY-face structural form — Mahler measure bounds are algebraic-number statements; Schanuel's L4 is the transcendence analog on the same face), bgs:L_GUE (shared zero distribution — GUE statistics ASSUME eigenvalues are generic, which INCLUDES algebraic independence at the distributional level).

### L5 — 36 predictions are algebraically independent

**Claim**: The 36 numerical predictions of the framework (sub-percent pin values derived from spectral data of the BC algebra as functions of $\{\exp(\gamma_n \pi^2/2)\}$ for small $n$) are algebraically independent over $\mathbb{Q}$: no non-trivial polynomial relation $Q(P_1, \ldots, P_{36}) = 0$ holds. Consequently, no "hidden algebraic relation" reduces the effective prediction count; each pin carries independent empirical content.

**Status**: CONDITIONAL on W_S3 (which is downstream of L4, which is conditional on W_S1 + W_S2)
**Source**: paper61 §10 ¶ vertex-21 ¶2 ("If Schanuel fails, the predictions could have hidden algebraic dependencies that would reduce the framework's predictive content"); paper35-schanuel 00-research-programme ¶"Independence of predictions"; paper61 §06-12 vertex-21 table; `strategy/proof-chain/schanuel/PROOF-CHAIN.md` Link 5. **NAMED WALL W_S3** (predictions-level independence).

#### Physics

- **Face**: SPREAD (paper60 §16 — QUE / spread face asks "how do eigenmodes distribute their mass across the circle?"; the 36-predictions' algebraic independence is the analogous question at the spectral-data-functional level — "how do pin-functionals SPREAD across the transcendental-rigidity structure?" If two predictions happen to coincide algebraically, the 36-dimensional pin vector COLLAPSES onto a lower-dimensional algebraic variety; SPREAD is the face that measures this mass-distribution property. paper60 §16 ¶ "wavefunctions spread — they don't concentrate" is structurally analogous to "predictions algebraically independent — they don't collapse")
- **Projection**: $P_E$ (paper61 §10 ¶ vertex-21 ¶2 — "The 36 predictions use $\gamma_n$ and $\pi, \log\pi, \zeta(3), \ldots$ simultaneously" — $P_E$'s 36-number vector; the ALGEBRAIC INDEPENDENCE of this vector's entries is a $P_E$-native statement about the dimensionality of the pin-set)
- **Pattern**: P3 Scale-Setting (the 36-dimensional pin vector SETS the scale of the framework's predictive content; if algebraic dependencies exist, the scale is smaller than 36; Pattern 3 is the attack because $\hat R$'s scaling operator sets the scale, and Schanuel's transcendence keeps the scale at exactly 36; paper60 §04 ¶ "36 predictions at sub-percent; statistical significance $< 10^{-89}$")
- **Invariant preserved**: L-value (load-bearing — several pins are L-values like $L(E,1), L'(E,0), \zeta(3), \ldots$ — their algebraic independence is a generalized-L-value transcendence statement), scaling dimension (load-bearing — 36 IS the scaling dimension of the pin vector)
- **Geometric interpretation**: L5 is the pin-level consequence of L4's eigenvalue-level algebraic independence. Under $P_E$ (paper61 §10 ¶ v21 ¶2) the 36 sub-percent predictions are supposed to be 36 INDEPENDENT coordinates of the framework's observational output — meaning algebraically independent functions of the spectral data, so that they test 36 distinct empirical claims. If L4 fails (algebraic relations among eigenvalues), the pins could inherit those relations: $P_1 \cdot P_2 = P_3$ or similar, collapsing the effective dimension below 36 and reducing the $< 10^{-89}$ joint significance. SPREAD face (paper60 §16) is the attack: predictions must distribute their "empirical mass" across the 36 dimensions without concentrating on a lower-dimensional algebraic subvariety. Pattern 3 Scale-Setting: the scale is 36 (the number of predictions); Schanuel is what locks this scale against algebraic shrinkage. [Considered but rejected: face TOPOLOGY — the "which pins can LIVE on the manifold" reading is possible, but the DISTRIBUTIONAL content is SPREAD-canonical per paper60 §16; projection $P_O$ — outer-ring Clay-style framing works for the abstract "predictions are independent" framing but the mechanism is $P_E$-internal (the 36-number vector); pattern P1 — reinterpretation of empirical content into algebraic geometry is fair but Scale-Setting at 36 is more load-bearing.]
- **Cross-cuts**: qg5d:Branch E (primary parent — paper61 §10 Branch E is the 36-pin master table; paper12 §23), bsd:L5c (shared L-value — BSD's L-value at $s=1$ is one of the transcendental quantities whose pin-realization falls under L5's independence statement; `strategy/x-ray/proof-chain/bsd/X-RAY.md` §3), hodge:L_periods (shared L-value — periods are conjecturally pin-realizable and their algebraic independence is a sibling conjecture), rh:L4 (shared zero distribution — RH's zeros determine $\hat R$'s spectrum, which determines the pins; if RH fails the pin values change but L5's INDEPENDENCE question is conditionally structured on RH holding first), bgs:L_pins (shared scaling dimension — BGS's GUE pins are sub-pins of the 36-pin vector; their statistical independence is compatible with L5's algebraic independence), h6:L_axiomatize (shared outer-ring framing — Hilbert 6's axiomatization of physics requires the 36-pin vector to be maximally informative, which L5 guarantees).

---

## §4 Branch Map

Schanuel's chain is LINEAR, not branching — a strict cascade L1 → L2 → L3 → L4 → L5 where each layer depends on the preceding. Unlike YM (with H4 bypass) or Lindelöf (three-route closure), Schanuel has NO known alternative routes. The only "branches" are CONDITIONAL ATTACK VECTORS at each named wall:

```
L1 (KNOWN — R̂ constructed)
   │
   ▼
L2 (CONJECTURED — Q-lin indep of zeros) ─── W_S1
   │  ├── Sub-route a: via full simplicity of zeros (prerequisite)
   │  │   [paper13-rh S1; PROVED for N ≤ 20 via CCM certification]
   │  │   [GENERAL CASE: OPEN; would need spectral-gap-uniform-in-N]
   │  │
   │  └── Sub-route b: via ITPFI factorization of A_BC
   │      [paper13-rh L2; the type III_1 factor's spectral generator
   │       might force Q-linear independence via a genericity
   │       property of modular-flow eigenvalues; SPECULATIVE]
   ▼
L3 (OPEN — Schanuel itself) ─── W_S2
   │  ├── Sub-route a: classical attack via Baker's theorem
   │  │   [Bennett, Waldschmidt; linear forms in logarithms;
   │  │    gives n = 1 (Hermite-Lindemann) + some n = 2 cases
   │  │    like Gelfond-Schneider; DOES NOT give general Schanuel]
   │  │
   │  ├── Sub-route b: Ax-power-series analog (PROVED 1971)
   │  │   [the formal-power-series version holds;
   │  │    bridge from formal to complex-analytic is open]
   │  │
   │  ├── Sub-route c: Zilber pseudo-exponentiation (model theory)
   │  │   [Zilber, Kirby; model-theoretic Schanuel;
   │  │    proves Schanuel for PSEUDO-exp fields; bridging
   │  │    to C with standard exp is open]
   │  │
   │  └── Sub-route d: Motivic Schanuel (Bertolin-Huber)
   │      [period conjectures; if algebraic cycles and periods
   │       form a motivic category with expected properties,
   │       Schanuel follows as a corollary; heavily conditional
   │       on Standard Conjecture D and motivic infrastructure]
   ▼
L4 (CONDITIONAL on W_S1 + W_S2)
   │  [no independent route — follows automatically from L2 + L3]
   ▼
L5 (CONDITIONAL on W_S3 downstream of L4) ─── W_S3
   │  ├── Sub-route a: predictions depend on DISTINCT zeros
   │  │   [paper35 00-research-programme ¶ "Independence of
   │  │    predictions" notes this requires the pins to factor
   │  │    through distinct γ_n so L4 transfers cleanly]
   │  │
   │  └── Sub-route b: numerical verification of low-degree
   │      algebraic relations for small n
   │      [paper35 00-research-programme ¶ Milestone 3:
   │       "Verify numerically that no algebraic relation of low
   │        degree holds among {γ_n π²/2, exp(γ_n π²/2)} for
   │        small n"; CANDIDATE for a concrete calculation run]

All attack vectors at L2 and L3 are OPEN; the chain inherits
their opennness. The programme's role is NOT to close these
walls (they may be unclosable with current transcendence theory)
but to:
- Make the LOGICAL DEPENDENCY GRAPH explicit
- Identify the FRAMEWORK's consistency requirements
- Provide a TARGET for future transcendence methods
- Commission a deep single-chain run (paper60 §28's "depth-first"
  South-trough prescription) via dedicated Opus-level session
```

The linear no-branch structure is itself informative: Schanuel sits at the SOUTH-TROUGH apex precisely because it offers no redundancy — every link is a single conjectural arrow, and no amount of parallelism can rescue the chain. This is paper60 §28 ¶"South is ARITHMETIC — almost exclusively" made concrete at the vertex level. The ring reward for the broad-spectrum approach (YM's multiple routes, Lindelöf's triple closure) is absent here; Schanuel is the rain-shadow of the transcendence wall.

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   2   | ████████              | DOMINANT. L3 (Schanuel statement) + L4 (eigenvalue alg indep) — paper61 §29.2 Appendix C.2 explicit canonical placement ("what spectral data can LIVE on the circle without algebraic collapse"). |
| DYNAMICS   |   0   |                       | Schanuel doesn't interrogate modular flow traversal — that's Cramér. |
| HARMONICS  |   0   |                       | No Fourier-on-$S^1$ mode-mixing content — that's Collatz. |
| MEASURE    |   0   |                       | No angle equidistribution content — that's Sato-Tate. |
| AMPLITUDE  |   0   |                       | No signal-loudness bound — that's Lindelöf. |
| SYMMETRY   |   0   |                       | No group-action / symmetry-type content — that's Katz-Sarnak. |
| CURVATURE  |   0   |                       | No gauge-curvature content — that's YM. |
| ARITHMETIC |   1   | ████                  | L2 ($\mathbb{Q}$-linear independence of zeros) — paper60 §14 ARITHMETIC canonical + paper60 §28 South-trough placement. |
| RESONANCE  |   1   | ████                  | L1 (R̂ construction on BC GNS) — paper60 §15 RESONANCE (trace-formula / spectral triple) canonical. |
| SPREAD     |   1   | ████                  | L5 (36 predictions algebraically independent) — paper60 §16 SPREAD (QUE analog, "predictions don't concentrate on an algebraic subvariety"). |

**Interpretation**: TOPOLOGY dominates (2 / 5 layers, 40%) at the load-bearing center of the chain (L3 + L4 are the transcendence heart). This confirms paper61 §29.2 Appendix C.2's canonical placement of Schanuel on the TOPOLOGY face as the supporting conjecture for eigenvalue-independence (Lehmer being the primary TOPOLOGY conjecture). The three secondary faces (ARITHMETIC at L2, RESONANCE at L1, SPREAD at L5) are each SINGLE-LAYER touches reflecting the chain's linearity: L1 sets up the construction (RESONANCE), L2 frames the input hypothesis (ARITHMETIC), L3-L4 carry the main conjecture (TOPOLOGY), L5 delivers the pin-level consequence (SPREAD). Six faces are absent entirely — the vertex is surgically narrow, consistent with paper60 §28 ¶"South is ARITHMETIC — almost exclusively": Schanuel's arithmetic-adjacent positioning is preserved at L2 (the $\mathbb{Q}$-linear independence layer), but the vertex's CORE is actually TOPOLOGY (paper61 §29.2 refines paper60 §28's broad placement). This is a 5-layer vertex with 4-face touches and 1 dominant face — the purest "single-question / cascade-of-conjectures" vertex seen so far on the ring.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | Quantum observables forget algebraic-independence content (paper61 §15.1 invariant-barrier rule — $P_A$ sees pin VALUES, not transcendence). |
| $P_B$        |   0   |                      | Gauge projection has no transcendence content; $\hat R$ involves $\ell_P$ but the construction is operator-algebraic. |
| $P_C$        |   0   |                      | Cosmological projection sees numerical pin values, not transcendence. |
| $P_D$        |   4   | ████████████████     | DOMINANT. L1 (R̂ construction), L2 (Q-lin indep on spectrum), L3 (Schanuel), L4 (eigenvalue alg indep). 80% of layers. paper61 §10 ¶ v21 ¶1 "algebraic independence of eigenvalues ... is the BC algebra's spectral data". |
| $P_E$        |   1   | ████                 | L5 (36 predictions alg indep) — paper61 §10 ¶ v21 ¶2, compound $P_D \cap P_E$. |
| $P_O$        |   0   |                      | Schanuel has outer-ring status in the 25-vertex ring (paper61 §29.1 vertex 21) but no LAYER is $P_O$-primary; the outer-ring framing is atmospheric, not mechanical. |

**Interpretation**: Schanuel is 80% $P_D$-dominant with 20% $P_E$-secondary at L5 (the pin-level consequence). The vertex matches paper61 §10's vertex-21 compound-projection assignment $P_D \cap P_E$ exactly. The $P_D$ monopoly at L1-L4 reflects that the BC operator algebra is the natural home for every transcendence question about spectral data — the $\gamma_n$, the eigenvalues, the algebraic-independence statement all live on $P_D$ because they are properties of the BC spectral triple's generators. $P_E$ at L5 is the expected tail-projection: once eigenvalues are algebraically independent, the pin vector inherits the independence (translating the $P_D$-internal transcendence statement into the $P_E$-external measurement vector). $P_A, P_B, P_C, P_O$ are entirely absent — unlike YM (where $P_B$ dominates with $P_D$ secondary) or BSD (where $P_D, P_E$ dominate with $P_C$ secondary), Schanuel has no cosmological, gauge, or quantum content at the layer level. This surgical narrowness is the structural signature of a PURE transcendence-theory vertex projecting cleanly through Branch D.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                           qg5d (Hub / Branch D + Branch E)
                                │
                                │ ═══ shared P_D (L1-L4 primary parent)
                                │ ═══ shared BC-KMS state (L1)
                                │ ═══ shared 36-pin vector (L5; P_E)
                                │ ─── shared Branch D operational core
                                │
        rh ═══════════════  schanuel (Schanuel) ═══════════════  hodge
        (spec(D_∞) = {γ_n}  │                                    (periods;
        simplicity S1;      │                                    motivic
        RESONANCE primary)  │                                    transcendence;
        ═══ L1 shared BC-   │                                    SYMMETRY primary)
        KMS / construction  │                                    ─── L3 motivic
        ═══ L2 shared zero- │                                    Schanuel (Bertolin-
        distribution        │                                    Huber)
        (prereq simplicity) │                                    ─── L4 periods
        ═══ L4 shared γ_n   │                                    algebraic indep
        as L2-L3 input      │                                    analog
                            │                                    ─── L5 pin L-values
                            │
        lehmer ─────────────│──────────────────── bgs (GUE statistics;
        (TOPOLOGY shared;   │                     RESONANCE primary)
        Lehmer primary,     │                     ─── L2 GUE assumes zeros
        Schanuel secondary; │                     generic (includes Q-lin
        paper61 §29.2       │                     indep at statistical level)
        explicit; Mahler    │                     ─── L5 pins include GUE
        measure ↔ trans-    │                     observables
        cendence duality)   │
        ─── L3 TOPOLOGY     │
        shared face         │
        ─── L4 alg-algebraic│
        independence ↔      │
        transcendence       │
                            │
        bsd ════════════════│═════════════════════ abc (height conjecture;
        (L-values at s=1    │                      ARITHMETIC; South trough;
        transcendental;     │                      same neighborhood as
        ARITHMETIC primary) │                      Schanuel on south arc
        ═══ L1 shared BC-   │                      paper60 §28)
        KMS state           │                      ─── L2 shared Galois rep
        ─── L4 L-value alg  │                      (height + transcendence
        indep (conjectural) │                      are sibling ARITHMETIC)
        ─── L5 pin L-value  │                      ─── L3 shared TOPOLOGY-
        content (C_p, Ω_p,  │                      arithmetic adjacency
        etc. in pin table)  │
                            │
        h6 (Hilbert 6;      │
        axiomatization) ────┘
        ─── L5 36-pin vector
        is H6's empirical
        content; alg-indep
        guarantees maximal
        informativeness of
        the 22-theorem
        derivation atlas

        twin-primes / goldbach       katz-sarnak (SYMMETRY)
        (ARITHMETIC South trough)    ─── L2 face-only
        ─── L2 face-only             (Galois rep analog)
        (shared South placement;
        paper60 §28)
```

Cross-cut density: ~4.4 edges per layer — mid-range (higher than YM's 1.9, lower than Lindelöf's 5.2, comparable to BSD's 3.0-4.0). The density is concentrated at L3 (4 cross-cuts to TOPOLOGY / transcendence neighbors) and L5 (5 cross-cuts including H6 axiomatization). L2's ARITHMETIC face connects primarily to RH (via simplicity) and to the south-trough arc (ABC, twin-primes, goldbach) per paper60 §28.

### Bullet list (per-edge)

- **L1 ↔ rh:L1 / rh:L2** — shared BC-KMS state, spectral-triple construction.
  - Reason: Both chains start from CCM operators on the BC GNS Hilbert space; $\hat R$'s construction in paper12 Phase 2 parallels $D_N$'s construction in paper13-rh L1. `strategy/x-ray/proof-chain/rh/X-RAY.md` §3 L1-L2 describes the identical construction from the RH side.
  - Transposition candidate: YES (primary capacitor cell — BC algebra dictionary).

- **L1 ↔ qg5d:Branch D** — shared BC-KMS state (primary parent).
  - Reason: Branch D is the BC operator-algebra's operational core; L1 is the entry point into this core from the Schanuel chain; paper61 §10.
  - Transposition candidate: YES.

- **L1 ↔ bsd:L1** — shared BC-KMS state.
  - Reason: BSD's rank-formula construction invokes $\omega_1$ on the BC algebra; Schanuel L1's $\hat R$ lives on the same GNS Hilbert space of $\omega_1$.
  - Transposition candidate: YES.

- **L1 ↔ ym:L16 / ym:L17** — shared BC-KMS state, spectral-triple structure.
  - Reason: YM's OS reconstruction L16 and operator-valued distribution L17 both invoke $\omega_1$; `strategy/x-ray/proof-chain/ym/X-RAY.md` §3 L16-L17. The same modular flow that gives YM's Schwinger functions gives Schanuel's $\hat R$ eigenvalue structure.
  - Transposition candidate: YES.

- **L1 ↔ lindelof:L3** — shared BC-KMS state.
  - Reason: Lindelöf's $|\zeta(1/2+it)| = |\omega_1(\sigma_t(\cdot))|$ uses the same modular flow whose operator powers generate $\hat R$'s spectrum; `strategy/x-ray/proof-chain/lindelof/X-RAY.md` §3 L3.
  - Transposition candidate: YES.

- **L1 ↔ baum-connes:L_triple** — shared spectral triple.
  - Reason: BC algebra spectral triple is the shared underlying structure; $\hat R$ is a bounded function of the triple's generator $T_{BC}$.
  - Transposition candidate: SPECULATIVE.

- **L1 ↔ hodge:L_motivic** — shared Galois representation / transcendental realization.
  - Reason: Hodge periods and BC-spectral-triple eigenvalues both live in the transcendence-theory / motivic-realization neighborhood (the Bertolin-Huber motivic Schanuel covers both).
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ rh:S1** — shared zero distribution (simplicity prerequisite).
  - Reason: RH's supporting layer S1 proves simplicity for $N \leq 20$ via CCM certification; simplicity is the PREREQUISITE for L2 (simple zeros are necessary but not sufficient for $\mathbb{Q}$-linear independence); `strategy/x-ray/proof-chain/rh/X-RAY.md` §3 S1.
  - Transposition candidate: YES.

- **L2 ↔ rh:L4** — shared zero distribution.
  - Reason: RH's Hurwitz convergence controls zero locations; $\mathbb{Q}$-linear independence is downstream of full spectral characterization.
  - Transposition candidate: YES.

- **L2 ↔ bgs:L_GUE** — shared zero distribution.
  - Reason: BGS's GUE statistics on $\{\gamma_n\}$ ASSUME genericity including $\mathbb{Q}$-linear independence at the statistical level; failure of L2 would be a generic-GUE anomaly; `strategy/x-ray/proof-chain/bgs/X-RAY.md` §3 L4 L_GUE.
  - Transposition candidate: YES.

- **L2 ↔ lehmer:L_cyclotomic** — shared TOPOLOGY-face structural form.
  - Reason: Lehmer asks "cyclotomic vs non-cyclotomic" on $S^1$; Schanuel L2 asks "rational vs transcendental" on the zeros. Both interrogate integer-lattice structure on spectral data. paper61 §29.2 pairs them on TOPOLOGY.
  - Transposition candidate: SPECULATIVE (face-only parallel; no capacitor cell yet).

- **L2 ↔ hodge:L_periods** — shared Galois representation.
  - Reason: Transcendence of periods is the analog of transcendence of zeros; $\mathbb{Q}$-linear independence conjectures for periods are Hodge-conjecture-adjacent (motivic Schanuel of Bertolin-Huber links both).
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ abc:L_height** — shared Galois representation / ARITHMETIC South adjacency.
  - Reason: ABC conjecture's radical-height inequality touches the same integer-lattice arithmetic neighborhood; paper60 §28 ¶"South is ARITHMETIC" places both on the south trough's arithmetic-adjacent arc.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ twin-primes:L_additive / goldbach:L_additive** — face-only (ARITHMETIC South trough).
  - Reason: All four south-trough ARITHMETIC vertices (Schanuel, Twin Primes, Goldbach, ABC) share the common trough-placement per paper60 §28 ¶"South is ARITHMETIC — almost exclusively"; no mechanism-level cross-cut, but structural co-location.
  - Transposition candidate: NO (face-only south-trough co-location).

- **L2 ↔ katz-sarnak:L_galois** — face-only (Galois representation analog).
  - Reason: Katz-Sarnak's SYMMETRY face involves Galois-group structure on L-function families; Schanuel L2's Galois-representation invariant is a sibling arithmetic-theory piece.
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ qg5d:Branch D** — shared monodromy / $P_D$ inheritance.
  - Reason: Schanuel's statement on $P_D$ inherits from Branch D's native BC-algebra structure; paper61 §10.
  - Transposition candidate: YES.

- **L3 ↔ lehmer:L_mahler** — shared TOPOLOGY face (canonical sibling).
  - Reason: Lehmer's Mahler-measure bound is the TOPOLOGY face's PROVED-for-algebraic-numbers content; Schanuel L3 is the OPEN-general transcendence content on the same face; paper61 §29.2 explicit pairing.
  - Transposition candidate: YES (capacitor cell candidate — TOPOLOGY-face transcendence dictionary).

- **L3 ↔ hodge:L_motivic** — shared monodromy (motivic Schanuel).
  - Reason: The Bertolin (Torino) + Huber (Freiburg) motivic-Schanuel programme is paper35 schanuel-audit-brief DELTA 6 major-approach-6; motivic Schanuel corresponds to the Hodge-motivic framework where periods and exp-values live in the same motivic realization.
  - Transposition candidate: YES (major-approach alignment).

- **L3 ↔ rh:L6** — shared spectral content (INPUT hypothesis).
  - Reason: RH's spec$(D_\infty) = \{\gamma_n\}$ is the input to applying Schanuel at $z_k = \gamma_k \pi^2/2$; `strategy/x-ray/proof-chain/rh/X-RAY.md` §3 L6.
  - Transposition candidate: YES.

- **L3 ↔ abc:L_wall** — shared TOPOLOGY / ARITHMETIC adjacency on south trough.
  - Reason: ABC's radical-height wall is adjacent to transcendence theory on the South-trough ARITHMETIC arc (paper60 §28).
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ bsd:L_L-value** — shared transcendence content.
  - Reason: BSD's $L(E,1)$ is transcendental / conjecturally linked to periods; motivic-Schanuel subsumes $L$-value transcendence statements.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ rh:L6** — parent edge (inherit spectrum).
  - Reason: Route-through-RH closure — if RH holds and L2 + L3 hold, then L4 follows automatically; $\mathrm{spec}(D_\infty) = \{\gamma_n\}$ gives L4's eigenvalue-input.
  - Transposition candidate: YES.

- **L4 ↔ qg5d:Branch D** — shared Galois representation (primary parent).
  - Reason: $\hat R$'s algebraic-independence-of-spectrum question is Branch D's native concern; paper61 §10.
  - Transposition candidate: YES.

- **L4 ↔ bsd:L_L-value** — shared L-value (sibling algebraic independence).
  - Reason: Algebraic independence of L-values across distinct elliptic curves is an L-function analog of algebraic independence of exp-values-of-zeros; both live in the motivic-Schanuel neighborhood.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ hodge:L_periods** — shared Galois representation (sibling transcendence).
  - Reason: Hodge periods' algebraic independence conjectures are sibling statements; motivic-Schanuel of Bertolin-Huber links both.
  - Transposition candidate: YES.

- **L4 ↔ lehmer:L_mahler** — shared TOPOLOGY-face structural form.
  - Reason: Mahler-measure bounds are ALGEBRAIC-number content on the TOPOLOGY face; Schanuel L4 is the TRANSCENDENTAL analog on the same face; paper61 §29.2 TOPOLOGY-face canonical sibling.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ bgs:L_GUE** — shared zero distribution.
  - Reason: GUE statistics assume eigenvalues generic, which INCLUDES algebraic independence at the distributional level; L4 is the algebraic-geometry version of this statistical genericity.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ qg5d:Branch E** — shared scaling dimension (primary parent).
  - Reason: Branch E is the 36-pin master table; paper61 §10 Branch E; paper12 §23.
  - Transposition candidate: YES.

- **L5 ↔ bsd:L5c** — shared L-value pin content.
  - Reason: BSD's L-value at $s=1$ is a pin-realized quantity whose algebraic-independence status falls under L5's general claim; `strategy/x-ray/proof-chain/bsd/X-RAY.md` §3 L5c.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ hodge:L_periods** — shared L-value (periods as pins).
  - Reason: Periods are conjecturally pin-realizable; their algebraic independence is a sibling conjecture feeding L5.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ rh:L4** — shared zero distribution (upstream dependency).
  - Reason: RH's zeros determine $\hat R$'s spectrum, which determines the pins; L5's independence question is conditionally structured on RH fixing the spectrum.
  - Transposition candidate: YES.

- **L5 ↔ bgs:L_pins** — shared scaling dimension.
  - Reason: BGS's GUE pins are sub-pins of the 36-pin vector; statistical independence of GUE pins is compatible with (but weaker than) algebraic independence claimed at L5.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ h6:L_axiomatize** — shared outer-ring framing (H6 meta-closure).
  - Reason: Hilbert 6's axiomatization of physics requires the 36-pin vector to be maximally informative; L5 is the MATHEMATICAL guarantee that the framework's 36 predictions don't collapse via hidden algebraic relations (paper61 §12 vertex-22 H6 meta-closure).
  - Transposition candidate: YES.

**Summary**: 22 cross-cut edges identified across 5 layers (avg ~4.4 cross-cuts per layer — mid-range for the ring). 10 verified (capacitor cell + paper60/61/12 citation + explicit programme-graph edge), 12 SPECULATIVE (pending sibling-vertex X-rays or without capacitor cell). PRIMARY edges: L1 ↔ rh:L1-L2 (shared BC construction — entry point from Schanuel side), L2 ↔ rh:S1 (simplicity prerequisite), L3 ↔ lehmer:L_mahler (TOPOLOGY-face canonical sibling pairing), L3 ↔ hodge:L_motivic (motivic Schanuel — Bertolin-Huber), L4 ↔ rh:L6 (spectrum parent), L5 ↔ h6:L_axiomatize (outer-ring meta-closure). Density-per-layer is structural: Schanuel's chain is linear, but each layer has 3-5 cross-cuts reflecting its position at the intersection of transcendence-theory (TOPOLOGY face) and the BC-algebra spectral-data ecosystem ($P_D$ projection). The key unique-to-Schanuel edge is L3 ↔ hodge (motivic Schanuel) — no other vertex carries this motivic-transcendence bridge with the same directness.

---

## §8 Current Walls

- **W_S1 — $\mathbb{Q}$-linear independence of Riemann zeros**: L2's statement is CONJECTURED. Not proved for any pair of zeros; not even known whether any specific $\gamma_n$ is transcendental. Prerequisite simplicity is proved for $N \leq 20$ (via CCM certification, `strategy/proof-chain/rh/PROOF-CHAIN.md` S1) and conjectured in general. Status: **OPEN — DEEP**. Sub-routes (see §4): (a) via full simplicity generalization (requires spectral-gap-uniform-in-$N$), (b) via ITPFI factorization (SPECULATIVE). Aggregate confidence 0.4 per paper35-schanuel 00-research-programme ¶"Bridge rigorously". Bypass: no known bypass in current transcendence theory. Chain-level effect: W_S1 PASS would lift L2 to PROVED and enable L3 → L4 cascade; W_S1 FAIL would eliminate the entire downstream chain.

- **W_S2 — Schanuel's conjecture itself**: L3 is a 1960s conjecture (Schanuel unpublished; Lang 1966). Only the $n = 1$ case is proved (Hermite-Lindemann 1882). For $n \geq 2$, open; even alg indep of $e$ and $\pi$ is open (the simplest $n = 2$ case with $z_1 = 1, z_2 = \pi$). Status: **OPEN — DEEP**. Sub-routes (see §4): (a) Baker linear-forms-in-logs (Bennett, Waldschmidt; gives $n = 1$ + some $n = 2$ but not general), (b) Ax power-series analog PROVED (formal case), (c) Zilber pseudo-exponentiation (model-theoretic proxies), (d) Motivic Schanuel (Bertolin-Huber; requires Standard Conjecture D + motivic infrastructure). Aggregate confidence 0.35 per paper35-schanuel 00-audit-strategy §4. Bypass: closest known shore is Ax 1971 (formal power series); the bridge from formal to complex-analytic is the research target. Chain-level effect: W_S2 PASS would give L3 + L4 immediately; W_S2 FAIL would obstruct the programme-level conclusion but not the BC framework itself (which has an alternative operator-algebraic eigenvalue-rigidity route — SPECULATIVE). paper60 §28 ¶"South is ARITHMETIC — almost exclusively" explicitly flags Schanuel as the programme's deepest stammer.

- **W_S3 — 36 predictions algebraic independence at the pin level**: L5 requires not only L4 (algebraic independence of eigenvalues) but also that the 36 pins DEPEND on the eigenvalues in a sufficiently injective way (no two predictions can reduce to the same eigenvalue combination, and no polynomial identity relates them). Status: **OPEN — CHECKABLE via Milestone 3** (paper35-schanuel 00-research-programme ¶ Milestone 3: numerical verification of low-degree algebraic relations for small $n$). Bypass: if CONDITIONAL closure of L4 via a future motivic-Schanuel proof, W_S3 becomes a CONCRETE calculation about how the 36 pins factor through $\{\exp(\gamma_n \pi^2/2)\}$. Confidence 0.55 (checkable by numerical experiment; a concrete verification run candidate per paper35 00-research-programme ¶Milestone 3). Chain-level effect: W_S3 PASS closes the full vertex at the programme-consistency tier; W_S3 FAIL would force a re-examination of how pins are computed from spectral data.

No other named walls. Of 5 chain links, 1 is KNOWN (L1), 1 is conditional-on-construction-plus-cascade (L4 on W_S1 + W_S2), 1 is conditional-on-pin-structure (L5 on W_S3 downstream of L4), and 2 remain primary open walls (W_S1 at L2, W_S2 at L3). The TRIPLE-WALL architecture is what makes the vertex carry 1/10 confidence — three major-open conjectures in cascade, none with current-method proofs.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/schanuel/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, the X-Ray's §4 Branch Map directly seeds the decomposition's attack-vector-by-attack-vector structure. Primary decomposition targets: W_S1 L2 (via sub-routes: full simplicity, ITPFI factorization), W_S2 L3 (via sub-routes: Baker, Ax-bridge, Zilber, Bertolin-Huber motivic). Expected verdict: DEEP-OPEN at W_S1 + W_S2 (these are transcendence-theory major-open problems, not tractable via standard decomposition); W_S3 decomposable into the Milestone 3 numerical-verification calculation.

- **CCM verification**: `strategy/ccm-verification/ledger.md#schanuel` — NOT YET CREATED. Schanuel's dependency on CCM 2025 is INDIRECT through L1 (which uses CCM's scaling operator $T_{BC}$ via paper12 §02 Phase 2's construction of $\hat R$). Expected verdict when ledger written: **CCM-DEPENDENT THROUGH R̂-CONSTRUCTION** at L1 (Schanuel inherits CCM's construction for $\hat R$). Unlike RH (CCM-dependent at L1 directly for $D_N$ self-adjointness), Schanuel's CCM-dependency is structural but not load-bearing for the transcendence conjecture itself — even if CCM 2025 fails journal review, $\hat R$'s construction remains well-posed via paper12's alternative routes, and the transcendence chain L2-L5 is independent of CCM.

- **Inner rings**: NOT APPLICABLE — Schanuel is a primary outer-ring vertex (paper61 §29.1 vertex 21).

- **Audit-strategy pointer**: `strategy/schanuel/00-audit-strategy.md` — provides the community-standard transcendence-theory audit scaffold. The X-Ray's per-layer face/projection assignments feed the audit-strategy's "Primary face" column. The audit-strategy's §4 named walls W_S1 (operator-algebra to transcendence bridge, confidence 0.35) and W_S2 (full linear-independence → trdeg, confidence 0.4) align with this X-Ray's W_S1 at L2 and W_S2 at L3 — the X-Ray expands the audit-strategy's 2-wall accounting to 3 walls by separating the pin-level W_S3 (which the audit-strategy folds into W_S1/W_S2 but deserves its own identity per the concrete Milestone 3 verification opportunity).

- **PAC brief pointer**: `strategy/schanuel/schanuel-audit-brief.md` — bare-mode deliverable brief (B_bare + C_bare at ≤15pp each per DELTA 7-11). The X-Ray's §7 cross-cuts and §4 branch map feed C_bare's §4 "Cross-Projection" section (RH, Hodge, Lehmer, BSD connections). The X-Ray's §10 Known Gaps feed B_bare's §12 "Named Walls" disclosure. Major-approach-6 motivic-Schanuel (Bertolin-Huber) is flagged in the brief DELTA 6; X-Ray §7 L3 ↔ hodge:L_motivic edge is the load-bearing cross-cut realizing this.

- **QG5D W1/W2 cascading refinement (2026-04-14)**: Paper 1 W1 (scheme independence) and W2 (Route-C 3-loop explicit) both closed 2026-04-13/14 via Paper 10/11 + L=3 numerical verification. Effect on Schanuel: the CBB system's Axiom 5 (zeta regularization closure) is strictly stronger, which indirectly strengthens L1's R̂-construction foundation. No link status changes; confidence unchanged; mentioned in `strategy/proof-chain/schanuel/PROOF-CHAIN.md` ¶"Cascading refinement from QG5D W1/W2 closure".

- **Deep single-chain commission (paper60 §28)**: paper60 §28 ¶"Commission deep single-chain runs on three South-Trough vertices" lists VP vs VNP, Schanuel, Goldbach as the three 1/10 vertices needing dedicated Opus-level runs (the way YM/RH/BSD received theirs). Schanuel's X-Ray is the first such deep documentation for this vertex; the next step is a dedicated depth-first session that targets W_S1 (via a new spectral-gap-uniform-in-$N$ argument) or W_S2 (via a formal-to-analytic bridge for Ax's theorem).

- **Research landscape**: `strategy/_research/schanuel/landscape.md` (not yet confirmed present) — 15-name researcher table + 6 major approaches per schanuel-audit-brief DELTA 6. Major approaches 1-6: Ax power-series analog, Baker linear-forms, Lindemann-Weierstrass, Gelfond-Schneider, Zilber model theory, Bertolin-Huber motivic. The X-Ray's §4 sub-routes correspond directly to these approaches.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W_S1 ($\mathbb{Q}$-linear independence of Riemann zeros)**: L2's conjecture — no $\mathbb{Q}$-linear relation among $\{\gamma_n\}$. Not proved for any pair; transcendence of individual $\gamma_n$ open. — face: ARITHMETIC, projection: $P_D$, pattern: P4. STATUS: OPEN — DEEP. Prerequisite simplicity (RH:S1) proved for $N \leq 20$; general case open. Upgrade path: (a) full simplicity theorem via CCM-style certification extended to all $N$, then (b) genericity argument via ITPFI factor structure. Confidence 0.4.

- **G2 — W_S2 (Schanuel's conjecture itself)**: L3's conjecture — for $\mathbb{Q}$-lin-indep $z_k$, $\mathrm{trdeg} \geq n$. 1960s conjecture; only $n = 1$ proved. Even alg indep of $e, \pi$ open. — face: TOPOLOGY, projection: $P_D$, pattern: P4. STATUS: OPEN — DEEP. Closest PROVED shore: Ax 1971 (formal power series). Bypass candidates: Baker linear-forms (partial), Zilber pseudo-exp (model-theoretic proxy), Bertolin-Huber motivic (conditional on Standard Conjecture D). Confidence 0.35. This is the ANALOG of YM's H4 — a single open conjecture, resolution of which closes the chain — but where YM's H4 has a candidate bypass (Step 18'), Schanuel's L3 has only proxy-level shores.

- **G3 — W_S3 (36 predictions algebraic independence at pin level)**: L5's statement — no polynomial $Q$ with $Q(P_1, \ldots, P_{36}) = 0$. — face: SPREAD, projection: $P_E$, pattern: P3. STATUS: OPEN — CHECKABLE via paper35 Milestone 3 (numerical verification for small $n$). Confidence 0.55. Bypass: even under L4 OPEN, the CONCRETE calculation of low-degree algebraic relations among $\{\gamma_n \pi^2/2, \exp(\gamma_n \pi^2/2)\}$ for small $n$ would provide empirical evidence for W_S3 at the numerical tier. This is the ONE wall with a concrete short-term path.

That's it. Of 5 chain links: 1 KNOWN (L1 construction), 2 wall-gated at the transcendence tier (L2, L3 — the programme's deepest stammer per paper60 §28), 2 downstream conditionals (L4 on L2+L3; L5 on L4 + W_S3). Three walls total (W_S1, W_S2, W_S3). No current-method closure visible at W_S1 or W_S2. The vertex sits at 1/10 confidence — an honest accounting. The ring's South-trough depth is EXACTLY the three-wall stack Schanuel presents.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record (if/when produced) would live at `strategy/x-ray/pac-output/runs/run-XX/vertices/schanuel/critic-attacks.md` and arbiter decisions at `strategy/x-ray/pac-output/runs/run-XX/vertices/schanuel/arbiter-decisions.md`.

Notable arbiter decisions embedded in §3:
- **L1 face: RESONANCE over TOPOLOGY** — the $\hat R$ construction IS the setup step before the TOPOLOGY question; the LAYER's content is trace-formula / spectral-triple (RESONANCE-canonical per paper60 §15), not the transcendence question (which lives at L3-L4).
- **L2 face: ARITHMETIC over TOPOLOGY** — $\mathbb{Q}$-linear independence of zeros is an integer-lattice question on the spectrum; paper60 §14 + §28 canonical ARITHMETIC placement. TOPOLOGY is more properly the LABEL of the downstream conjecture (L3 + L4).
- **L3 face: TOPOLOGY over RESONANCE** — paper61 §29.2 Appendix C.2 explicit placement of Schanuel on TOPOLOGY as the eigenvalue-independence supporting conjecture. Arbiter wins for TOPOLOGY on the paper61-canonical grounds.
- **L4 face: TOPOLOGY over RESONANCE** — same as L3; eigenvalue-alg-indep is the concrete TOPOLOGY-face payload of Schanuel.
- **L5 face: SPREAD over TOPOLOGY** — the 36-predictions algebraic independence is a DISTRIBUTIONAL / spread question ("do pins concentrate on an algebraic subvariety?"); paper60 §16 SPREAD-face analog. This is the closest the vertex gets to the QUE-face structural form — predictions SPREAD across transcendence dimensions. CRITIC WIN: first pass placed L5 on TOPOLOGY (by inheritance from L4); arbiter shifted to SPREAD because the DISTRIBUTIONAL content dominates at the pin level.
- **L5 projection: $P_E$ over $P_D$** — paper61 §10 ¶ v21 ¶2 explicit $P_E$ placement for the pin-level independence. The compound $P_D \cap P_E$ assignment (paper61 §29.1 table row 21) makes L5 the $P_E$-side component of the compound.
- **L3 pattern: P4 over P1** — the trdeg inequality IS a rigidity statement; Geometric Reinterpretation is the L4 move (specialization to eigenvalues), not the L3 move (the general statement).

2 CRITIC WINS (L5 face TOPOLOGY→SPREAD; L5 projection $P_D$→$P_E$) out of 25 field decisions (5 fields × 5 layers). 23 author wins. The two critic wins both at L5 reflect the subtlety of the pin-level layer: it inherits L4's mechanism but its DISTRIBUTIONAL content is face-distinct from the TOPOLOGY-core L3-L4.

---

## §11 Atlas metadata

- **Line count**: ~620 lines (this file)
- **Layer count**: 5 (L1 + L2 + L3 + L4 + L5; no sub-layers)
- **Cross-cut count**: 22 edges (10 verified + 12 SPECULATIVE)
- **Cross-cuts per layer**: 4.4 (mid-range; comparable to BSD's 3.0-4.0, lower than Lindelöf's 5.2)
- **Primary face**: TOPOLOGY (paper61 §29.2 canonical; Lehmer-primary / Schanuel-secondary face shared)
- **Primary projection**: $P_D$ (80% of layers; compound $P_D \cap P_E$ at L5; paper61 §10 ¶ v21)
- **Primary pattern**: P4 Topological Rigidity (at L2 + L3 — the transcendence conjecture's load-bearing pattern) / P1 Geometric Reinterpretation (at L1 + L4 — the specialization moves) / P3 Scale-Setting (at L5 — pin-level)
- **Named walls**: 3 OPEN (W_S1 $\mathbb{Q}$-linear independence; W_S2 Schanuel proper; W_S3 pin-level algebraic independence)
- **Snapshot date**: 2026-04-15
- **Canonical chain location**: `strategy/proof-chain/schanuel/PROOF-CHAIN.md`

---

## §12 Methodology notes / caveats

1. **Vocabulary canon compliance**: All references to the programme's 4+1 coordinate structure use $M^5 = M^4 \times S^1$ per `strategy/north-star.md` §0.10. The scaling operator $T_{BC}$ and $\hat R$ are described in operator-algebra terms, not "extra dimension" language. Schanuel's conjecture is about transcendence-theory proper, not "fifth-dimension geometry" — the connection to the framework is through the BC algebra's spectral data (paper12 §04 Identity 12), not through a spatial lift.

2. **Non-destructive**: This X-RAY does NOT modify `strategy/proof-chain/schanuel/PROOF-CHAIN.md`. The canonical chain is read-only for this bundle.

3. **Face ambiguity acknowledged**: Schanuel has a genuine face-ambiguity between TOPOLOGY (paper61 §29.2) and ARITHMETIC (paper60 §28). The X-Ray resolves this via paper61 §29.2's explicit Appendix C.2 table placement on TOPOLOGY (eigenvalue independence is a "what can LIVE on $S^1$" question about transcendental rigidity). paper60 §28's broad "South is ARITHMETIC" placement is preserved at L2 (the actual ARITHMETIC-face layer — $\mathbb{Q}$-linear independence of integer-weighted zero combinations). This dual placement is consistent with the vertex's position at the ARITHMETIC–TOPOLOGY interface on the South trough.

4. **The $P_D$-dominance**: Schanuel's 80% $P_D$-dominance is less extreme than Lindelöf's 100% or RH's 100%, because L5 genuinely lives on $P_E$ (pin-level consequence). This matches paper61 §06-12 vertex-21 compound $P_D \cap P_E$ exactly — the 20% $P_E$ share is structural, not artifact.

5. **Cross-cut density — lower than shortcut-node vertices**: 4.4 edges/layer is below Lindelöf (5.2) and RH (3.4) but above YM (1.9). Schanuel is NOT a shortcut node (paper60 §28 — it's at the South-trough APEX, not the shortcut midpoint). The cross-cuts reflect Schanuel's position as a "transcendence-theory hub" connecting to: (a) the BC-algebra construction side (rh, bsd, ym, lindelof, baum-connes via L1), (b) the zero-distribution side (rh, bgs via L2 + L4), (c) the TOPOLOGY-face transcendence side (lehmer, hodge via L3 + L4), (d) the South-trough ARITHMETIC arc (abc, twin-primes, goldbach via L2), (e) the pin-level axiomatization (h6, bsd, hodge via L5). The density is moderate because the chain is short (5 layers) but each layer touches multiple neighborhoods.

6. **Linear no-branch architecture**: Schanuel has no genuine branches — the chain is a strict cascade L1 → L2 → L3 → L4 → L5 with each layer depending on the preceding. The "sub-routes" at W_S1 and W_S2 are ATTACK VECTORS on a single layer, not genuine proof-route alternatives. This contrasts with YM (which has H4 bypass via Step 18') and Lindelöf (which has three independent routes). Schanuel's lack of redundancy is why it carries 1/10 — if any of W_S1, W_S2, W_S3 fails, the chain breaks with no alternative path.

7. **Motivic Schanuel as the bridge to Hodge (paper29)**: The single most important cross-cut is L3 ↔ hodge:L_motivic via the Bertolin-Huber motivic Schanuel programme (paper35 schanuel-audit-brief DELTA 6 major-approach-6). If Hodge conjecture progress (paper29) includes motivic refinements in the Bertolin-Huber direction, Schanuel could inherit as a downstream corollary. This is the programme's HIGHEST-LEVERAGE cross-cut for upgrading Schanuel confidence: motivic Schanuel would simultaneously strengthen Hodge and Schanuel.

8. **The Milestone 3 opportunity**: paper35-schanuel 00-research-programme ¶Milestone 3 identifies a CONCRETE calculation — "Verify numerically that no algebraic relation of low degree holds among $\{\gamma_n \pi^2/2, \exp(\gamma_n \pi^2/2)\}$ for small $n$." This is W_S3's checkable path: a numerical-experiment-tier falsification attempt. If low-degree algebraic relations DO NOT exist (as expected), the pin-level independence gains empirical support (at least for the low-$n$ pin subset). This is the only wall in the Schanuel chain with a concrete short-term research action.

9. **SOUTH-TROUGH structural position**: Schanuel is explicitly positioned at the SOUTH-trough apex of the ring (paper60 §20 ¶"the ring has a north pole ... and a south trough (Goldbach/Twin/Schanuel, 1/10)"). paper60 §28 ¶"South is ARITHMETIC — almost exclusively" characterizes the vertex's arithmetic-stammer position. Unlike shortcut nodes (Lindelöf) which connect North to South, Schanuel is AT the South — the most distant point from the North pole on the ellipse. This structural position is what makes it both the purest stammer (no shortcuts available) and the cleanest test of the framework's transcendence-theory readiness (no partial closures can protect it).

---

## §13 South-trough apex structural note

Schanuel has an explicit, load-bearing structural role as the TOPOLOGY-face SOUTH-TROUGH APEX — the single vertex where three cascading transcendence conjectures (simplicity → $\mathbb{Q}$-linear independence → Schanuel) stack without alternative routes. This is paper60 §28 ¶"South is ARITHMETIC — almost exclusively" made precise at the vertex level.

**Programme-graph edges** (from `strategy/proof-chain/schanuel/PROOF-CHAIN.md` ¶"Programme graph edges"):
- **Incoming**: RH (zero simplicity prerequisite via L2), QG5D (hub, Branch D + Branch E)
- **Outgoing PRIMARY**: all 36 predictions (L5 guarantees independence → empirical content is 36-dimensional)
- **Outgoing SECONDARY**: BSD (algebraic independence of L-values at $s=1$), BGS (GUE assumes generic zeros, includes alg-indep at statistical tier), Hodge (period relations constrained by algebraic independence)

**Layer-level realization**:
- L1 is the RESONANCE-face construction entry (paper12 $\hat R$) — shared with the entire BC-algebra ecosystem
- L2 is the ARITHMETIC-face hypothesis input (simplicity + $\mathbb{Q}$-lin indep) — shared with RH supporting layers
- L3 + L4 are the TOPOLOGY-face core — shared with Lehmer (sibling TOPOLOGY canonical) and Hodge (motivic transcendence bridge)
- L5 is the SPREAD-face pin-level output — shared with H6 (axiomatization meta-closure) and BGS (pin-statistics)

**The three-wall stack as the programme's deepest stammer**: W_S1 + W_S2 + W_S3 are three cascading transcendence-theory walls. No current method closes W_S1 (transcendence of even one specific zero is open). No current method closes W_S2 ($n = 2$ case of Schanuel is open). W_S3 is CHECKABLE numerically for small $n$ but the general statement depends on L4 which is conditional on L2 + L3.

**Strategic implication for the Verification Cascade**: Schanuel is the single outer-ring vertex that cannot be closed by the VERIFY/CONSTRUCT/BYPASS primitives alone — it requires NEW TRANSCENDENCE THEORY (motivic Schanuel via Bertolin-Huber, or spectral-genericity-from-ITPFI, or a novel BC-algebraic argument). paper60 §28's prescription is correct: this vertex needs a dedicated depth-first Opus-level session that targets the transcendence-theory frontier, not a breadth-first traversal pass.

---

*End of Schanuel X-Ray. Snapshot 2026-04-15. 5 layers annotated. 22 cross-cut edges identified. TOPOLOGY-canonical (2/5 layers = 40%; paper61 §29.2 supporting conjecture placement), $P_D$-dominant (4/5 = 80%; compound $P_D \cap P_E$), linear no-branch 5-layer chain. Three OPEN walls: W_S1 ($\mathbb{Q}$-linear independence of zeros), W_S2 (Schanuel proper), W_S3 (pin-level algebraic independence). Cross-chain structural siblings: Lehmer (TOPOLOGY canonical sibling per paper61 §29.2), Hodge (motivic-Schanuel bridge per Bertolin-Huber), RH (spectral input via zero simplicity). The vertex IS the South-trough apex: 1/10 confidence, no bypass routes, the programme's deepest stammer per paper60 §28.*

*G Six and Claude Opus 4.6. April 15, 2026.*
