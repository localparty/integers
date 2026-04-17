# X-RAY: ABC Conjecture (abc)

*X-Ray of the abc proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: abc
- **Paper**: paper37-abc
- **Live file**: `strategy/proof-chain/abc/PROOF-CHAIN.md` (snapshot 2026-04-15; carries 2026-04-14 W1/W2 cascading refinement note from QG5D)
- **Top-level claim**: For every $\varepsilon > 0$, there exist only finitely many coprime triples $(a, b, c)$ with $a + b = c$ and $c > \operatorname{rad}(abc)^{1+\varepsilon}$. Equivalently: there exists $K_\varepsilon$ with $c \leq K_\varepsilon \cdot \operatorname{rad}(abc)^{1+\varepsilon}$ for every coprime $a + b = c$. The framework's route: BC Mellin bridge carries $\operatorname{rad}(abc)$ as a multiplicative norm controlled by ITPFI factor weights $\lambda_p = 1/p$ (paper61 §12 vertex 18).
- **Current status**: **1/6 links closed**; confidence **1/10**. L1 KNOWN (Bost-Connes 1995); L2 ESTABLISHED (Paper 12 Mellin transposition); **L3 CONJECTURED — THE WALL W_A1** (BC-partition height function on multiplicative structure; no candidate in the literature); **L4 CONJECTURED** ($\operatorname{rad}(abc)$ as multiplicative norm under $\{\mu_p\}$); **L5 OPEN** (ABC inequality from BC height bound); **L6 OPEN** (explicit $\varepsilon$-dependence via Riemann-zero spacing; conditional on RH Layer 1). NOT IUT; independent operator-algebraic route.
- **Primary branch (paper1)**: D (CBB modular-flow / Bost-Connes operational core — paper61 §12 vertex 18 explicitly assigns $P_D$ compound; the Mellin bridge converts $\operatorname{rad}(n) = \prod_{p \mid n} p$ into an ITPFI weight identity $\lambda_p = 1/p$ from Branch D's KMS$_1$ state); with secondary outer-ring $P_O$ boundary at L6 (the quantitative $\varepsilon$-dependence closing statement as Oesterlé-Masser Clay-adjacent formulation).
- **Primary face**: ARITHMETIC (paper60 §14 — Goldbach/Twin Primes/ABC sit on the single ARITHMETIC face; paper60 §20 "Ellipse and Missing Faces" map places ABC explicitly on the SOUTH trough's ARITHMETIC spine; paper60 §28 "The South Trough Needs Lifting" lists ABC alongside Goldbach/Twin Primes/Schanuel as the ARITHMETIC-canonical south vertices).
- **Primary projection**: $P_D$ (paper61 §12 vertex 18 "ABC Conjecture": "The BC Mellin bridge relates the radical $\operatorname{rad}(n) = \prod_{p|n} p$ to the ITPFI factors $\lambda_p = 1/p$. The ABC inequality is a statement about the concentration of ITPFI weight in the radical"; paper61 §14 projection table assigns $P_D: M^5 \to A_{BC}$ as the natural home for every Hecke-semigroup-valued question).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
ABC CONJECTURE — c ≤ K_ε · rad(abc)^{1+ε} for every ε > 0
│  primary face: ARITHMETIC   primary proj: P_D   primary pat: P4
│  top claim: Oesterlé 1988 / Masser 1985
│  route: BC Mellin bridge for rad(abc); no IUT claim
│  status: 1/6 closed; confidence 1/10; south-trough vertex
│
├── L1: Primes ↔ μ_p Hecke operators generate N^*        [KNOWN]
│      │  face: ARITHMETIC    proj: P_D   pat: P4
│      │  invariant: C*-algebra structure, BC-KMS state
│      │  source: Bost-Connes 1995 (CMP 172, 381–446);
│      │          paper61 §10 (Branch D Axiom 5 "primes-
│      │          as-operators"); paper60 §14 (the Hecke
│      │          semigroup is the multiplicative engine)
│      │
│      └── supports L2 via multiplicative generation of N^⋊
│             │
│             └── this is the entry point SHARED with goldbach,
│                    twin-primes, rh, bsd, pvnp, baum-connes —
│                    the BC algebra IS built from the primes
│                    (paper61 §10 table)
│
├── L2: Mellin transform = canonical additive ↔           [ESTABLISHED]
│      │  multiplicative bridge in the framework
│      │  face: HARMONICS     proj: P_D   pat: P5
│      │  invariant: spectral gap, scaling dimension
│      │  source: Paper 12 research/14 transposition
│      │          dictionary; Mellin 1890s; Perron 1908;
│      │          Riemann 1859 (explicit formula); paper60 §14
│      │          "the Mellin bridge IS the explicit formula"
│      │  depends: L1
│      │
│      └── supports L3 via multiplicative-side height candidate
│             │
│             └── SHARED with goldbach:L3, twin-primes:L1/L2
│                    (same bridge; same narrowness at POINTWISE
│                    level — the narrowness is structural,
│                    paper60 §14)
│
├── L3: Height function h(·) on multiplicative struct.   [CONJECTURED — THE WALL W_A1]
│      │  via BC partition
│      │  face: ARITHMETIC    proj: P_D   pat: P4
│      │  invariant: BC-KMS state, C*-algebra structure
│      │  source: framework original (no candidate in
│      │          literature); analogous to Szpiro 1981
│      │          conductor-discriminant bound on elliptic
│      │          curves; paper37-abc programme §2
│      │  depends: L2
│      │  confidence on the wall itself: 0.4
│      │
│      ├── proposed form: h_BC(n) = − log ω_1(μ_n^* μ_n)
│      │     = log n (trivial case); non-trivial height
│      │     must fold in the RADICAL structure via
│      │     ITPFI weights {λ_p = 1/p}
│      │     (paper61 §12 vertex 18 "concentration of
│      │      ITPFI weight in the radical")
│      │
│      └── NOT YET DECOMPOSED in strategy/decomposition/…
│             decomposition candidate three sub-links:
│             ├── L3.a: operator-theoretic height on
│             │         N^⋊ from BC partition             [OPEN]
│             ├── L3.b: Szpiro-analog inequality between
│             │         BC-height and rad-height           [OPEN]
│             └── L3.c: the height extends to coprime
│                       additive triples (a,b,c)           [OPEN]
│
├── L4: rad(abc) as multiplicative norm under μ_p         [CONJECTURED]
│      │  face: ARITHMETIC    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure, ITPFI factor type
│      │  source: paper61 §12 vertex 18 "rad(n) ↔ ITPFI
│      │          factors λ_p = 1/p"; framework original
│      │  depends: L1, L3
│      │
│      ├── proposed identity: − log rad(n) = Σ_{p | n} log(1/p)
│      │                                  = Σ_{p | n} log λ_p
│      │   interprets rad(n) as the reduction of the
│      │   ITPFI weight to SQUARE-FREE support
│      │
│      └── ITPFI factorization ω_1 = ⊗_p ω_1^{(p)} at each
│             prime; rad(n) picks up p with multiplicity 1,
│             not p^{a_p} (paper61 §10)
│
├── L5: ABC inequality c < K(ε) · rad(abc)^{1+ε}          [OPEN]
│      │  from BC height bound
│      │  face: ARITHMETIC    proj: P_D   pat: P5
│      │  invariant: L-value, C*-algebra structure
│      │  source: Oesterlé 1988 / Masser 1985 target;
│      │          Stewart-Tijdeman 1986 (κ = 3 unconditional,
│      │          baseline for comparison); Stewart-Yu 2001
│      │          (refined exponential bound)
│      │  depends: L3, L4
│      │
│      ├── sub-requirements (paper37-abc programme §2):
│      │     ├── L5.a: lift BC height from N^* to the
│      │     │         coprime-triple set {(a,b,c): a+b=c}  [OPEN]
│      │     ├── L5.b: convert BC height bound into polynomial
│      │     │         rad(abc)^{1+ε} form                   [OPEN]
│      │     └── L5.c: move from "sufficiently large" to
│      │               "all but finitely many" triples      [OPEN]
│      │
│      └── the non-IUT route: if L5 closes via L3+L4, we
│             obtain an ABC proof independent of Mochizuki's
│             Inter-Universal Teichmüller Theory (paper37
│             programme §3; Scholze-Stix 2018 critique
│             of IUT Cor. 3.12 is NOT our concern — we
│             neither endorse nor refute)
│
└── L6: Explicit ε-dependence via Riemann-zero spacing    [OPEN]
       │  (explicit formula)
       │  face: RESONANCE    proj: P_O   pat: P5
       │  invariant: zero distribution, spectral gap
       │  source: RH (paper13) Layer 1 — spectral prime
       │          density; Montgomery 1973 (PCC); Hardy Z
       │          PCC arXiv:2511.18275 Nov 2025 (GUE sine-
       │          kernel PROVED conditional on RH); paper60
       │          §14 "the explicit formula IS the bridge"
       │  depends: L5 + RH Layer 1 (cross-paper transport,
       │           not independent RH assumption)
       │
       ├── proposed form: K_ε = C · exp(F(γ_n, ε))
       │     for an explicit F depending on Riemann zero
       │     spacings {γ_n} and ε; the GUE sine-kernel
       │     bulk regime (PROVED Nov 2025) delivers the
       │     spacing data
       │
       └── closes abc as the outer-ring Clay-adjacent vertex
              (paper61 §12 vertex 18); the Baker-style
              explicit K_ε refinement is the PRIZE form
              (Annals-grade closure); the non-effective
              existence form is the minimum COMPLY deliverable

───────────────────────────────────────────────────────────
COMPARISON INPUT — IUT vs framework (paper37 §3)
───────────────────────────────────────────────────────────

The framework's route STANDS INDEPENDENT of:

  Mochizuki IUT 2012/2021 — Hodge theaters, Frobenioids,
     log-links; Scholze-Stix 2018 flagged gap in Cor. 3.12;
     published in PRIMS (Mochizuki editor-in-chief) —
     mainstream non-acceptance as of 2026
  Joshi 2021+ — alternative formalization of IUT ideas;
     ongoing Scholze-Joshi dialogue
  Vojta's conjecture — ABC as special case; Vojta deeper
     and also open
  Stewart-Tijdeman / Stewart-Yu — unconditional exponential
     bounds in rad; baseline for comparison

The BC-Mellin route is a fundamentally different machine:
operator algebras + Mellin bridge + Riemann zero spectral
data. The two routes could both succeed (they would agree
at the ABC inequality value), both fail, or one succeed —
they are ORTHOGONAL proof strategies (paper37 §3).

───────────────────────────────────────────────────────────
GUE three-tail cross-chain input (paper60 §14)
───────────────────────────────────────────────────────────

ABC lives in the BULK-REGIME of the GUE sine-kernel
distribution, via the Mellin bridge + explicit formula:

     small-gap tail  ←  Twin Primes (gap = 2)
     ────────────────────────────────────────
     BULK            ←  GOLDBACH (sine-kernel bulk;
                        prime density in short intervals)
                        ABC's L6 ε-dependence consumes
                        the SAME bulk data
     ────────────────────────────────────────
     large-gap tail  ←  Cramér (max gap ~ log² x)

ABC is not a pure bulk-regime object: L6 consumes
spacing DATA from the bulk, but the ABC inequality's
POINTWISE content (specific triples (a,b,c)) asks a
question sharper than Goldbach's or Twin Primes' tail
statistics. It sits on the ARITHMETIC face but requires
the spectral bulk + a NEW HEIGHT structure (L3). The
height is the novel conjecture; without it, ABC
retreats to the classical Szpiro analog + Vojta.
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (Quantum observables do not see
                          the radical rad(abc) directly —
                          radical is a multiplicative
                          operation on integers, invisible
                          to quantum-observable projection.)
                                  ▲
                                  │
                                  │
        ┌──────────────(P_O outer)──────────────────┐
        │                                            │
        │  ABC: c ≤ K_ε · rad(abc)^{1+ε} for every   │
        │       ε > 0, coprime a + b = c             │
        │  (Oesterlé-Masser; non-IUT route)          │
        │                                            │
        └───────────────────┬────────────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity      ═══ P_D CBB ═══           P_C cosmology
    (forgotten —     Bost-Connes algebra        (forgotten —
    no gauge-        A_{BC}; Hecke semigroup    ABC does not
    bundle struct    N^⋊ = ⟨μ_p⟩; KMS_1 state;  contribute
    carries rad      Mellin bridge to rad(abc); any cosmological
    directly;        ITPFI factors λ_p = 1/p;   pin — it is
    primes have      BC-partition height        a pure number-
    no KK tower      h_BC(·) on N^⋊ candidate;  theory statement
    interpretation)  paper61 §12 vertex 18      unrelated to the
                     explicit assignment        36-pin master table)
                            │
                            ▼
                       P_E pins
                       (forgotten — ABC is NOT a
                        sub-percent numerical pin;
                        it is a QUALITATIVE statement
                        about the finitely-many-
                        exceptions structure; ABC
                        is Chen-compatible but not
                        pin-valued)
```

Primary projection $P_D$ uses ═══ doubled line. $P_O$ is the second-strongest projection: the top-level conjecture statement is the outer-ring Oesterlé-Masser formulation (paper61 §12 vertex 18) and L6 (explicit $\varepsilon$-dependence) is the Clay-adjacent closure statement. $P_A, P_B, P_C, P_E$ all FORGET ABC entirely — ABC is neither a quantum observable, nor a gauge-bundle object, nor a cosmological pin, nor a numerical pin. It lives in the $P_D \cap P_O$ compound projection (paper61 §12 vertex 18: "$P_D$ — pure BC/Mellin"). The Mellin bridge (L2) is the SOLE layer that moves off pure $P_D$-operator content onto $P_D$'s Fourier-dual side ($C^*(\mathbb{Q}/\mathbb{Z})$ characters dual to the multiplicative $\mu_p$), giving L2 a HARMONICS face assignment while staying within $P_D$'s preservation class.

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
         (YM)               │          (Sato-Tate)
                            │
                       ● ARITHMETIC  ← ABC
                         (Goldbach +      (south-trough sibling
                          Twin Primes +    of Goldbach, Twin
                          ABC + …)         Primes; paper60 §28
                            │              "The South Trough
                       AMPLITUDE            Needs Lifting")
                       (Lindelöf)
                                           (RESONANCE secondary
                                            at L6 via explicit
                                            formula; HARMONICS
                                            secondary at L2 via
                                            Mellin bridge)
```

Marker key:

```
Primary face:    ● ARITHMETIC (paper60 §14 — ABC is a canonical
                  ARITHMETIC-face vertex; paper60 §20/§28 map it
                  onto the south trough's arithmetic spine)
Secondary faces: ○ HARMONICS (1 layer: L2 — Mellin bridge is the
                              dual-Fourier side of the arithmetic
                              lattice; paper60 §09 Collatz analog)
                 ○ RESONANCE (1 layer: L6 — explicit-formula-
                              delivered ε-dependence via Riemann
                              zeros; paper60 §15 Selberg analog)
Absent faces:    TOPOLOGY, DYNAMICS, AMPLITUDE, SYMMETRY,
                 CURVATURE, MEASURE, SPREAD
```

The face profile is ARITHMETIC-dominant (4 of 6 layers) with thin HARMONICS (L2) and RESONANCE (L6) footprints and zero presence on the other seven. This is paper60 §14/§20/§28's thesis made concrete: ABC lives primarily on the arithmetic face because the question "does $\operatorname{rad}(abc)$ control $c$?" is an ARITHMETIC-LATTICE question about the multiplicative-to-additive interface. The cross-tails to HARMONICS (Mellin bridge) and RESONANCE (explicit formula) are the two bridges out of the arithmetic face — they are NARROW (paper60 §14), and the chain stops at them.

---

## §3 Layer-by-Layer X-Ray

### L1 — Primes generate BC algebra via $\mu_p$

**Claim**: The Bost-Connes algebra $A_{BC}$ has its multiplicative Hecke semigroup $\mathbb{N}^\rtimes$ generated by a family of isometries $\{\mu_p\}_{p \text{ prime}}$, one per rational prime; these $\mu_p$ are the primes seen as operators on the BC Hilbert space. This is the SAME L1 as goldbach, twin-primes, rh (at the generator level), bsd, pvnp, baum-connes: a shared foundational entry point.

**Status**: KNOWN
**Source**: Bost-Connes 1995 (CMP 172, 381–446); paper61 §10 "BC algebra / the operator-algebra dictionary"; Branch D Axiom 5 "zeta regularization closure"; paper01-qg5d appendix Z/BC dictionary; paper60 §14 canonical ARITHMETIC-face entry.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — "the primes are the generators of the Bost-Connes algebra's Hecke semigroup $\mathbb{N}^* = \langle 2, 3, 5, 7, \ldots \rangle$. Each prime $p$ defines a Hecke operator $\mu_p$. The Hecke operators are the MULTIPLICATIVE engine of the BC algebra." ABC asks a multiplicative-over-additive question about these generators.)
- **Projection**: $P_D$ (paper61 §10 — "$A_{BC}$ (Bost-Connes at KMS$_1$) is the target of $P_D$; Hecke semigroup on $S^1$"; paper61 §12 vertex 18 "BC Mellin bridge" explicitly places ABC's L1 inside $P_D$)
- **Pattern**: P4 Topological Rigidity (paper61 §10 — the prime generators are topologically rigid in the BC system: they are fixed by the semigroup structure, not chosen; this is the $P_D$ signature of Branch D Axiom 5)
- **Invariant preserved**: C*-algebra structure (load-bearing — $A_{BC}$ is a specific C*-algebra generated by $\{\mu_p\}$), BC-KMS state (background — the $\mu_p$ carry the KMS$_1$ state by definition)
- **Geometric interpretation**: The $\mu_p$ are the primes as isometries on the BC Hilbert space; each $\mu_p$ implements multiplication by $p$ on the frequency side. This is paper60 §14's "frequency multiplication" interpretation: the primes are the IRREDUCIBLE frequency multipliers on the e-circle. Under $P_D$ (paper61 §10) this is the foundational layer — every other $P_D$-layer of every ARITHMETIC-face vertex rests on this generation property. For ABC specifically, the Hecke semigroup provides the multiplicative norm that the radical will probe in L4. [Considered but rejected: face RESONANCE — the $\mu_p$ are resonance-mode generators in a loose sense, but paper60 §14 canonicalizes ARITHMETIC for ABC because the question asks about additive-combination $(a + b = c)$ of multiplicative objects; projection $P_O$ — the BC algebra has outer-ring facets but the generator property is strictly $P_D$ internal.]
- **Cross-cuts**: goldbach:L1 (same $\mu_p$ generator entry point), twin-primes:L1 (same), rh:L2 ($\mu_p$ generate ITPFI Euler product for $\zeta$), bsd:L1 (BC over imaginary quadratic $K$ — extension of $\mathbb{N}^\rtimes$ to number-field primes), baum-connes:L1 (Cuntz-Li semigroup $\mathbb{N}^\rtimes$ at K-theory target), pvnp:L_BC (BC-algebra spectral-gap rigidity), bgs:L1 (BC at KMS$_1$ → type III$_1$).

### L2 — Mellin transform as the canonical additive ↔ multiplicative bridge

**Claim**: The Mellin transform $f(s) = \int_0^\infty F(x) x^{s-1} dx$ connects the additive Fourier analysis on $\mathbb{Z}$ with the multiplicative Dirichlet series on $\mathbb{N}^\rtimes$; within the framework, the bridge lives inside $C^*(\mathbb{Q}/\mathbb{Z}) \subset A_{BC}$ (the maximal abelian subalgebra of the BC algebra carrying the additive characters dual to the multiplicative $\mu_p$). The Riemann-von Mangoldt explicit formula IS the instantiation of this bridge.

**Status**: ESTABLISHED
**Source**: Paper 12 research/14 transposition dictionary (BC algebra Mellin construction); Mellin 1890s; Perron 1908; Riemann 1859; paper60 §14 "the Mellin bridge IS the explicit formula; it translates the multiplicative information (zeros of $\zeta$) into additive information (prime-counting)"; paper37-abc programme §2.

#### Physics

- **Face**: HARMONICS (paper60 §09 — Collatz face; the Mellin bridge is the canonical FOURIER/ORBIT-AVERAGING face, connecting additive orbits on $\mathbb{Z}$ to multiplicative Dirichlet series — paper60 §14 explicitly identifies the Mellin bridge as the FACE-8-to-FACE-3 connection ARITHMETIC ↔ HARMONICS)
- **Projection**: $P_D$ (paper61 §10 — the bridge lives inside the BC algebra via $C^*(\mathbb{Q}/\mathbb{Z})$; paper61 §12 vertex 18 "BC Mellin bridge" places ABC's L2 inside $P_D$)
- **Pattern**: P5 Zeta Regularization (paper60 §14 explicit formula is the zeta-regularized translation between sum-over-primes and sum-over-zeros; Mellin transform is the canonical zeta regularization move)
- **Invariant preserved**: spectral gap (load-bearing — the bridge's information-carrying capacity depends on the zero-free region of $\zeta$), scaling dimension (background — Mellin pairs $s \leftrightarrow x^s$ is a scaling duality)
- **Geometric interpretation**: The Mellin bridge is the one narrow tube connecting the multiplicative side (Dirichlet series, Euler product, BC algebra) to the additive side (exponential sums, $\mathbb{Z}$-lattice). Under $P_D$ (paper61 §10) the bridge lives inside the BC algebra's abelian subalgebra $C^*(\mathbb{Q}/\mathbb{Z})$; Pattern 5 (paper60 §14): the bridge's core mechanism IS zeta regularization — the explicit formula trades $\sum_p \log p$ for $\sum_\rho x^\rho/\rho$. The bridge is NARROW in a precise sense (paper60 §14): it converts average multiplicative information to average additive information efficiently, but POINTWISE information poorly — this narrowness is exactly what makes L3 (height on triples) the wall. [Considered but rejected: face ARITHMETIC — the Mellin bridge lives on the arithmetic face structurally but paper60 §09 names HARMONICS for Fourier/dual-side content and §14 explicitly identifies the Mellin bridge as the ARITHMETIC ↔ HARMONICS edge; projection $P_A$ — the Fourier duality has quantum-side overtones but the bridge mechanism is operator-algebraic.]
- **Cross-cuts**: goldbach:L3 (same Mellin bridge, same narrowness framing, SHARED across all ARITHMETIC-south-trough vertices), twin-primes:L1/L2 (same explicit formula), rh:L2/L3 (RH zeros are the bridge's multiplicative-side data), collatz:L_Mellin (paper60 §09 HARMONICS canonical), bgs:L4 (sine-kernel universality is the bulk of the bridge's spectral output), schanuel (prospective — algebraic independence of L-values is the transcendence side of the bridge; no x-ray yet, face-only speculative cross-cut).

### L3 — Height function $h_{BC}(\cdot)$ on multiplicative structure via BC partition — **W_A1 — the wall**

**Claim**: There exists a height function $h_{BC}: \mathbb{N}^\rtimes \to \mathbb{R}_{\geq 0}$ constructed from the BC partition function $Z(\beta) = \zeta(\beta)$ (or a natural derivative thereof) that satisfies a Szpiro-analog inequality controlling $\operatorname{rad}(n)$ in terms of $n$; extended to coprime triples $(a, b, c)$ with $a + b = c$, this height bounds $c$ in terms of $\operatorname{rad}(abc)$.

**Status**: **CONJECTURED — THE WALL W_A1** (primary named wall of the abc proof chain). Confidence on the wall itself: 0.4 (ring confidence 1/10 per landscape.md). No candidate in the literature.
**Source**: paper37-abc programme §2 "Current wall"; Szpiro 1981 conductor-discriminant inequality on elliptic curves (classical height analog the framework emulates); framework original proposal; paper61 §12 vertex 18 "The ABC inequality is a statement about the concentration of ITPFI weight in the radical"; paper60 §28 "The South Trough Needs Lifting" ABC entry "height function from BC partition (no candidate in the literature)."

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the height function on $\mathbb{N}^\rtimes$ is an arithmetic-lattice object; paper60 §28 explicitly places ABC's height on the ARITHMETIC face of the south trough)
- **Projection**: $P_D$ (paper61 §10 — the BC partition function is the canonical $P_D$ object; paper61 §12 vertex 18 "BC Mellin bridge" places the height construction inside $P_D$)
- **Pattern**: P4 Topological Rigidity (if the height exists, it is a rigidity of the BC partition structure: the multiplicative-norm statement is forced by the Euler-product decomposition, not chosen — the analogy to Szpiro 1981 is structural: the conductor-discriminant bound is a RIGIDITY of the elliptic curve's reduction type)
- **Invariant preserved**: BC-KMS state (load-bearing — the height is literally evaluating a partition-derived functional on the Hecke operators), C*-algebra structure (background — the height's domain $\mathbb{N}^\rtimes$ is the semigroup inside $A_{BC}$)
- **Geometric interpretation**: The proposed height is a novel construction: $h_{BC}(n)$ should distinguish $n$-values with the same multiplicative norm but different radical structure. The KMS$_1$ state at equilibrium gives $\omega_1(\mu_n^* \mu_n) = 1/n$; the trivial height $h_{\text{triv}}(n) = -\log \omega_1(\mu_n^* \mu_n) = \log n$ is insensitive to the radical. A non-trivial height must fold the RADICAL structure into the construction — candidate: some spectral-derivative of $Z(\beta)$ at $\beta = 1$ that picks up $\operatorname{rad}(n)$ via the ITPFI factorization $\omega_1 = \otimes_p \omega_1^{(p)}$ (paper61 §12 vertex 18: "concentration of ITPFI weight in the radical"). Under $P_D$ (paper61 §10) this is an operational-core object; if the construction succeeds, Pattern 4 says it is RIGID — forced by the BC partition's structure, not a free parameter. The wall is genuine: paper37 programme §2 is explicit that "there is no candidate in the literature"; paper60 §28 lists the height construction as a framework original problem. [Considered but rejected: face RESONANCE — the BC partition function has resonance-mode content but the HEIGHT construction is an arithmetic-lattice move (paper60 §14); projection $P_O$ — the wall is Clay-adjacent but the proposed construction lives operationally in $P_D$; pattern P1 — Geometric Reinterpretation of the Szpiro bound in BC language is a fair alternative but the load-bearing content is the rigidity of the height's existence.]
- **Cross-cuts**: bsd:L3 (height on elliptic-curve Mordell-Weil group via BC at number-field Hecke characters — same "BC partition derives a height" structural move), rh:L_partition (shared BC-partition machinery; the height candidate leverages $Z(\beta)$ at or near $\beta = 1$), goldbach:L6 (analogous novel conjecture: KMS$_1$-derived kernel $f$ delivering additive conclusions — same P4 structural form), twin-primes:L4 (analogous: $C_2$ from arithmetic fine structure of BC Hecke — same novel-height-from-BC construction), schanuel (prospective — the height's transcendence over $\mathbb{Q}$ could tie to algebraic independence of $L$-values; speculative, no x-ray yet).

### L4 — $\operatorname{rad}(abc)$ as multiplicative norm under $\mu_p$

**Claim**: The radical $\operatorname{rad}(n) = \prod_{p \mid n} p$ is a natural multiplicative norm under the BC Hecke semigroup's action, given explicitly by the ITPFI-factor-truncation identity $-\log \operatorname{rad}(n) = \sum_{p \mid n} \log \lambda_p = \sum_{p \mid n} \log(1/p)$, where $\lambda_p = 1/p$ is the ITPFI factor weight at prime $p$ (paper61 §10). The radical is the reduction of the ITPFI weight to SQUARE-FREE support (multiplicity 1 per prime, regardless of $a_p$).

**Status**: CONJECTURED
**Source**: paper61 §12 vertex 18 "rad(n) ↔ ITPFI factors $\lambda_p = 1/p$"; paper37-abc programme §2 Link 4; paper61 §10 ITPFI factorization $\omega_1 = \otimes_p \omega_1^{(p)}$; depends on L1, L3.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the radical is a canonical arithmetic-lattice invariant; it counts the SUPPORT of the multiplicative structure of $n$ on the prime lattice)
- **Projection**: $P_D$ (paper61 §10 — ITPFI-factor decomposition is the $P_D$ target; paper61 §12 vertex 18 explicit)
- **Pattern**: P1 Geometric Reinterpretation (reinterpreting $\operatorname{rad}(n)$ as the square-free projection of the ITPFI weight; the CLASSICAL $\operatorname{rad}(n)$ is the reduction of multiplicity information; the BC reinterpretation says this reduction is the natural operator-algebraic content)
- **Invariant preserved**: C*-algebra structure (load-bearing — the statement is about the structure of $A_{BC}$ restricted to square-free integers), ITPFI factor type (background — type III$_{1/p}$ at each prime factor)
- **Geometric interpretation**: The radical is the arithmetic invariant that ABC constrains. The proposed reinterpretation (paper61 §12 vertex 18) says $-\log \operatorname{rad}(n) = \sum_{p \mid n} \log \lambda_p$ — the radical is the ITPFI factor weight truncated to the SET of primes dividing $n$, ignoring multiplicities. This is Pattern 1 (paper60's Geometric Reinterpretation pattern): the familiar $\operatorname{rad}(n)$ becomes a natural projection of the BC-algebra's ITPFI weight onto square-free support. Under $P_D$ (paper61 §10) this reinterpretation is operational — it connects the arithmetic question (what is $\operatorname{rad}(abc)$?) to the BC-algebra's tensor-product structure. The reinterpretation is modest (not a theorem yet; a structural identification), but it is the BRIDGE between L1/L3 (BC machinery) and L5 (the ABC inequality). [Considered but rejected: face HARMONICS — the Mellin-dual framing of the radical is a fair alternative but paper60 §14 canonicalizes ARITHMETIC for the radical as an arithmetic-lattice invariant; pattern P4 — the ITPFI truncation is rigid, but the move from classical $\operatorname{rad}$ to BC $\operatorname{rad}$ is reinterpretive (P1); projection $P_O$ — the radical itself sits at the outer-ring framing but the ITPFI reinterpretation is internal-$P_D$.]
- **Cross-cuts**: bsd:L1/L4 (number-field-extended ITPFI weight — BC over imaginary quadratic $K$ gives an analogous truncation to square-free ideals in $\mathcal{O}_K$), baum-connes:L2 (Cuntz-Li semigroup's K-theory encoding carries the radical-structure information in its cohomology), rh:L_Euler (Euler-product decomposition directly into ITPFI factors is the dual picture), goldbach:L2 (shared ITPFI factorization at the unique-factorization level), twin-primes:L4 (shared ITPFI-derived arithmetic factors; $C_2 = \prod_{p>2}(1 - 1/(p-1)^2)$ is an ITPFI-truncated product).

### L5 — ABC inequality $c < K(\varepsilon) \cdot \operatorname{rad}(abc)^{1+\varepsilon}$ from BC height bound

**Claim**: Combining the BC height function $h_{BC}$ (L3) with the radical-as-ITPFI-norm identity (L4), for every $\varepsilon > 0$ there exists $K(\varepsilon)$ such that $c \leq K(\varepsilon) \cdot \operatorname{rad}(abc)^{1+\varepsilon}$ for all coprime $a + b = c$. Equivalently: only finitely many coprime triples satisfy $c > \operatorname{rad}(abc)^{1+\varepsilon}$ for each fixed $\varepsilon > 0$.

**Status**: **OPEN**
**Source**: Oesterlé 1988 / Masser 1985 (target statement); paper37-abc programme §2 Link 5; Stewart-Tijdeman 1986 (baseline $c \leq \exp(K_1 \cdot \operatorname{rad}(abc)^{15})$); Stewart-Yu 2001 (refined exponential bound); paper37-abc §3 comparison with Mochizuki IUT (independent route).

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the ABC inequality IS the canonical arithmetic-face statement; paper60 §20 "Ellipse and Missing Faces" places ABC at the south trough's arithmetic spine)
- **Projection**: $P_D$ (paper61 §12 vertex 18 — "$P_D$ — pure BC/Mellin"; the inequality lives inside $P_D$'s preservation class because both $h_{BC}$ (L3) and the ITPFI-norm interpretation of $\operatorname{rad}(abc)$ (L4) are $P_D$-operational)
- **Pattern**: P5 Zeta Regularization (the passage from the height bound to the polynomial $\operatorname{rad}(abc)^{1+\varepsilon}$ form is via a zeta-regularized estimate of the partition-function derivative; Pattern 5 is the signature pattern for any proof that converts a BC-partition-valued quantity into a polynomial number-theoretic bound)
- **Invariant preserved**: L-value (load-bearing — $K(\varepsilon)$ in refined forms is an L-value at specific arguments; Baker 1990s effective ABC refinements explicitly involve $L$-values), C*-algebra structure (background — the inequality's domain is the BC-algebra's Hecke semigroup)
- **Geometric interpretation**: The ABC inequality is the arithmetic output of the $h_{BC}$ construction (L3) through the ITPFI-norm reinterpretation (L4). Under $P_D$ (paper61 §12 vertex 18) the inequality is a statement about the concentration of ITPFI weight in the radical — for coprime $a + b = c$, the additive constraint forces the radical to carry a definite share of the multiplicative weight. Pattern 5 (paper60 §14, paper08 §36): the regularization that converts $h_{BC}(c)$ into $\log \operatorname{rad}(abc)^{1+\varepsilon}$ is zeta-regularized. The wall is GENUINE: without L3 and L4, the inequality has no operator-algebraic derivation; the BC route is ORTHOGONAL to Mochizuki IUT — neither endorses nor refutes (paper37 §3). The baseline for comparison is Stewart-Tijdeman 1986 $c \leq \exp(K_1 \cdot \operatorname{rad}(abc)^{15})$ (exponential in rad; unconditional). Moving to polynomial $\operatorname{rad}(abc)^{1+\varepsilon}$ requires either Vojta's conjecture (also open) or the BC height (L3). [Considered but rejected: face MEASURE — the "all but finitely many" statement has equidistribution/density overtones but paper60 §14 canonicalizes ARITHMETIC for ABC; projection $P_O$ — the ABC inequality IS the outer-ring Clay-adjacent statement, and $P_O$ is a reasonable reading; the arbiter preference for $P_D$ rests on paper61 §12 vertex 18's explicit "$P_D$ — pure BC/Mellin" assignment and the fact that the OPERATIONAL content (height bound + ITPFI truncation) lives in $P_D$; $P_O$ is reserved for L6 (the Clay-boundary closure); pattern P4 — rigidity of the inequality once L3/L4 hold is real but the CONVERSION mechanism is zeta-regularization.]
- **Cross-cuts**: bsd:L5 (analogous inequality on elliptic curves — Szpiro's conjecture is equivalent to ABC, providing a structural parallel; the BC-K height would give both), goldbach:L5 (shared ARITHMETIC-south-trough wall: both need BC machinery to produce quantitative arithmetic bounds; shared additive-multiplicative wall framing, paper60 §14), twin-primes:L5 (shared: $C_2 \cdot x / (\log x)^2$ asymptotic is the analog of $K(\varepsilon)$ form), rh:L_short-dist (ζ zero-free region controls the $\varepsilon$-dependence structurally; cross-paper transport), schanuel (prospective — $K(\varepsilon)$ in explicit Baker-style form involves transcendental $L$-values; speculative), vp-vs-vnp:L_counting (prospective — effective ABC gives uniform bounds that feed into effective algebraic complexity; speculative).

### L6 — Explicit $\varepsilon$-dependence via Riemann-zero spacing (explicit formula)

**Claim**: The constant $K(\varepsilon)$ in the ABC inequality admits an explicit form $K(\varepsilon) = C \cdot \exp(F(\{\gamma_n\}, \varepsilon))$ where $\{\gamma_n\}$ is the sequence of Riemann-zero imaginary parts and $F$ is derived from the explicit formula; the Baker-style REFINED ABC with effective $K(\varepsilon)$ is the Annals-grade closure of the conjecture.

**Status**: **OPEN**
**Source**: Riemann-von Mangoldt explicit formula; paper13-rh PROOF-CHAIN.md Layer 1 (spectral prime density, 8/10 conditional on CCM 2025; cross-paper transport for abc's L6); Montgomery 1973 PCC; Hardy Z PCC arXiv:2511.18275 Nov 2025 (GUE sine-kernel PROVED conditional on RH); Baker 1990s (effective ABC style); paper37-abc programme §2 Link 6.

#### Physics

- **Face**: RESONANCE (paper60 §15 — the explicit formula IS the trace-formula-side resonance content; the Riemann-zero spectral data delivering $K(\varepsilon)$ is a resonance-mode quantity)
- **Projection**: $P_O$ (paper61 §17 — L6 is the Clay-adjacent closure boundary; the explicit $\varepsilon$-dependence is the prize-form Oesterlé-Masser statement, sitting at the outer-ring boundary where abc closes as a famous conjecture)
- **Pattern**: P5 Zeta Regularization (the explicit formula IS zeta regularization; the $K(\varepsilon)$ extraction is a zeta-regularized sum over zeros)
- **Invariant preserved**: zero distribution (load-bearing — Riemann zeros $\{\gamma_n\}$ are the explicit-formula input), spectral gap (background — RH zero-free region bounds the $K(\varepsilon)$ dependence)
- **Geometric interpretation**: L6 consumes the spectral prime density from RH Layer 1 (cross-paper, not independent RH assumption) and delivers the explicit $K(\varepsilon)$. Under $P_O$ (paper61 §17) this is where abc closes as the outer-ring Clay-adjacent vertex: the REFINED $K(\varepsilon)$ form is the Baker-style effective ABC, which is the Annals-grade target; the non-effective existence form is the minimum COMPLY deliverable. Pattern 5: the conversion from zero-spacing data to $K(\varepsilon)$ is zeta-regularized via the explicit formula. The GUE sine-kernel bulk (PROVED Nov 2025, arXiv:2511.18275) delivers the spacing data; the ARITHMETIC side extraction of $K(\varepsilon)$ from that data is still OPEN — same structural form as goldbach:L6 (KMS$_1$ kernel novel conjecture) and twin-primes:L5 ($C_2$ from GUE fine structure). [Considered but rejected: face ARITHMETIC — the $K(\varepsilon)$ form is arithmetic content but the EXTRACTION mechanism (zero-spacing → $K$) is resonance-mode (paper60 §15); projection $P_D$ — the cross-paper input IS $P_D$-operational (RH's KMS$_1$ state), but L6 itself is the outer-ring closure statement ($P_O$); pattern P4 — rigidity of the zero distribution under GUE universality is real but the MECHANISM delivering $K(\varepsilon)$ is regularization.]
- **Cross-cuts**: rh:L_explicit-formula (primary cross-paper transport; abc's L6 CONSUMES rh's Layer 1 as input; same explicit formula, same zero distribution; rh is the upstream vertex), grh:L4/L5 (generalized zeros for multi-modulus ABC variants; Dirichlet L-function zeros control Dirichlet-ABC forms), bgs:L4/L5 (GUE sine-kernel bulk delivers the spacing data), twin-primes:L4 (same GUE fine-structure extraction structural form), goldbach:L6 (same novel-KMS-derived-closure structural form), cramer:L_large-gap (GUE three-tail: large-gap tail shares the same Fredholm determinant machinery as abc's L6 bulk input; paper60 §14), schanuel (prospective — transcendence of $L$-value arguments in $K(\varepsilon)$; no x-ray yet), lindelof:L_amplitude (prospective — bounded ζ moments feed the same explicit-formula apparatus; face-only speculative).

---

## §4 Branch Map

The abc chain is largely linear but has one notable structural fork at L5/L6: the **non-effective closure** (minimum COMPLY — existence of $K_\varepsilon$) vs. the **effective Baker-style refined closure** (Annals-grade prize form with explicit $K(\varepsilon)$). Additionally, the entire chain STANDS INDEPENDENT of Mochizuki IUT (paper37 §3 explicit programme position).

```
L4 (rad(abc) as ITPFI norm, CONJECTURED)
                │
                ├── Route Non-Effective: L5 → existence of K_ε
                │   [face: ARITHMETIC | proj: P_D | pat: P5]
                │   minimum COMPLY form; Oesterlé 1988 target
                │   "for every ε > 0, only finitely many triples"
                │   does NOT require explicit K(ε)
                │
                └── Route Effective: L5 + L6 → explicit K(ε)
                    [face: RESONANCE | proj: P_O | pat: P5]
                    Baker-style refined ABC; Annals-grade closure
                    consumes RH Layer 1 explicit-formula output
                    K(ε) = C · exp(F({γ_n}, ε)) explicit form

Both routes target: c ≤ K_ε · rad(abc)^{1+ε} for coprime a+b=c
(with effective form delivering explicit constant).

Routes differ in which projection is load-bearing:
- Route Non-Effective sits at P_D (operational BC-algebra
  content: h_BC height + ITPFI truncation of rad) with L5's
  existence statement satisfying minimum community-standard
- Route Effective sits at P_O (the Clay-adjacent closure
  statement with effective constant is the outer-ring prize
  form) with P_D machinery (BC height + Mellin bridge +
  explicit formula) supplying the internal content

Framework position (paper37 §3):
 - NOT Mochizuki IUT: we neither endorse nor refute the
   Mochizuki-Scholze-Stix-Joshi debate
 - NOT Vojta route: Vojta's conjecture is deeper and also
   open; ABC is a special case
 - Our route: BC Mellin bridge + operator-algebraic height +
   explicit formula; ORTHOGONAL to IUT

Structural note: If L3 (the wall W_A1) resolves, L4 is
a modest structural identification (paper61 §12 vertex 18),
L5 is a moderate downstream calculation, and L6 is a
quantitative refinement using cross-paper transport from
RH. The chain's SOLE substantive wall is L3 — the height
function from BC partition.
```

**Cross-chain structural input — the GUE three-tail (paper60 §14)**: ABC's L6 consumes the bulk-regime spacing data via RH's explicit formula. Twin Primes lives in the small-gap tail (gap = 2); Goldbach lives in the bulk (prime density); Cramér lives in the large-gap tail (max gap). All four are views of the Fredholm determinant $\det(1 - K_{\sin})$; ABC's L6 is the ARITHMETIC-face consumer of the bulk that DIFFERS from Goldbach's consumer — Goldbach asks "does every even $N \geq 4$ equal $p + q$?" (a pointwise additive question), while ABC asks "is $c$ bounded by $\operatorname{rad}(abc)^{1+\varepsilon}$?" (a pointwise multiplicative-over-additive question). Both pass through the same bulk, with different arithmetic factors on the other side of the bridge.

---

## §5 Face Histogram

| Face       | Count | Bar                        | Interpretation |
|------------|-------|----------------------------|---|
| TOPOLOGY   |   0   |                            | ABC does not live on the topology face; no winding/genus content (contrast Lehmer). |
| DYNAMICS   |   0   |                            | ABC does not interrogate the modular-flow dynamics directly (the GUE bulk feeds L6 as cross-chain structural input, not as a layer; contrast Cramér). |
| HARMONICS  |   1   | ████                       | L2 (Mellin bridge) is the canonical Fourier/dual-side layer — the bridge between additive (circle-method) and multiplicative (Euler-product) forms. |
| MEASURE    |   0   |                            | ABC does not directly interrogate equidistribution (contrast Sato-Tate, Goldbach L4). |
| AMPLITUDE  |   0   |                            | ABC does not interrogate growth-rate/subconvexity (contrast Lindelöf). |
| SYMMETRY   |   0   |                            | ABC has no explicit Galois/symmetry-type content (contrast Katz-Sarnak, h12). |
| CURVATURE  |   0   |                            | ABC is not a gauge-curvature object (contrast YM). |
| ARITHMETIC |   4   | ████████████████           | DOMINANT (67%). L1 (primes generate BC), L3 (BC-partition height — THE WALL), L4 (rad as ITPFI norm), L5 (ABC inequality). Four of six layers are arithmetic-face canonical. ABC is a canonical ARITHMETIC vertex alongside Goldbach and Twin Primes (paper60 §14/§20/§28). |
| RESONANCE  |   1   | ████                       | L6 (explicit $\varepsilon$-dependence via Riemann-zero spacing) is the trace-formula-side resonance content — the explicit formula is the canonical RESONANCE-face layer (paper60 §15). |
| SPREAD     |   0   |                            | ABC does not interrogate $L^2$-mass-spreading. |

**Interpretation**: ARITHMETIC dominates (4 / 6 layers = 67%) — confirming paper60 §14/§20/§28's identification of ABC as a canonical ARITHMETIC vertex on the south trough. HARMONICS carries 1 layer (L2 Mellin bridge, 17%); RESONANCE carries 1 layer (L6 explicit formula, 17%). All seven other faces are absent. This concentrated ARITHMETIC signature is the structural signal that the chain's depth is shallow (6 links, 1 closed) while its face-pureness is maximal — ABC asks one question, and that question lives on one face, and the face's own difficulty (paper60 §28 "the south trough needs lifting") is what makes the chain short and the wall (L3) hard. The "shape" of ABC on the e-circle is a single point at ARITHMETIC with thin rays to HARMONICS (via Mellin) and RESONANCE (via explicit formula) — the two bridges out of the arithmetic face. This shape mirrors Goldbach's shape exactly (both are ARITHMETIC-4 / HARMONICS-1 / MEASURE-1 vs. ARITHMETIC-4 / HARMONICS-1 / RESONANCE-1), differing only in which neighboring face L6 reaches — Goldbach reaches MEASURE (equidistribution-via-density), ABC reaches RESONANCE (explicit-formula-via-zero-spacing).

---

## §6 Projection Histogram

| Projection | Count | Bar                        | Notes |
|------------|-------|----------------------------|---|
| $P_A$        |   0   |                            | ABC has no quantum-observable content; $P_A$ forgets it entirely (radical is invisible to quantum observables). |
| $P_B$        |   0   |                            | ABC has no gauge-bundle content; $P_B$ forgets it (primes have no KK-tower interpretation). |
| $P_C$        |   0   |                            | ABC contributes no cosmological pin; $P_C$ forgets it. |
| $P_D$        |   5   | ████████████████████       | DOMINANT (83%). L1, L2, L3, L4, L5 all live inside $P_D$'s preservation class — the BC algebra, Mellin bridge, BC-partition height, ITPFI-norm radical, and ABC inequality are all operational BC-algebra content. paper61 §12 vertex 18 explicit: "$P_D$ — pure BC/Mellin." |
| $P_E$        |   0   |                            | ABC is not pin-valued; it is a qualitative statement about finitely-many-exceptions, not a sub-percent numerical pin. |
| $P_O$        |   1   | ████                       | L6 (explicit $\varepsilon$-dependence — the Clay-adjacent closure statement with effective $K(\varepsilon)$). |

**Interpretation**: The projection profile is $P_D$-dominant (5 / 6 = 83%) with a single $P_O$ entry at L6. This is paper61 §12 vertex 18's compound-projection assignment for ABC made concrete: $P_D$ for the internal BC-algebraic machinery (Mellin bridge, height construction, ITPFI-norm reinterpretation, inequality derivation), $P_O$ for the outer-ring effective closure statement. $P_A, P_B, P_C, P_E$ are all absent — ABC is neither a quantum observable, nor a gauge bundle, nor a cosmological pin, nor a sub-percent numerical prediction. The $P_D$ dominance is the structural signal that ABC's natural home is Branch D (Bost-Connes, operator-algebra side) — matching paper61 §12 vertex 18's explicit "$P_D$ — pure BC/Mellin" assignment. This profile mirrors Goldbach's profile almost exactly (5 $P_D$ / 1 $P_O$) and matches Twin Primes' $P_D$-dominance (5 $P_D$ / 1 $P_D \cap P_E$) — the three ARITHMETIC-south-trough vertices share a common projection fingerprint, confirming their shared structural position on the framework's bouquet. The absence of $P_E$ (pin-valued) distinguishes ABC from Twin Primes: ABC has no numerical pin content, while Twin Primes' $C_2 \approx 0.6601618$ has mesoscopic numerical framing (Odlyzko-style).

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                           qg5d Branch D
                           (Axiom 5; N^⋊ = ⟨μ_p⟩;
                            primes-as-operators;
                            BC algebra, KMS_1;
                            ITPFI factorization)
                                  │
                                  │ ═══ shared C*-algebra structure (L1)
                                  │ ═══ shared Mellin bridge (L2)
                                  │ ═══ shared BC-KMS state (L1, L3)
                                  │ ═══ shared ITPFI factors λ_p=1/p (L4)
                                  │
       goldbach ═══════════════   abc   ══════════════   twin-primes
       (ARITHMETIC sibling;      │                     (ARITHMETIC sibling;
        additive-multiplicative  │                      small-gap tail;
        wall;                    │                      C_2 from GUE fine
        Goldbach: N = p + q      │                      structure)
        ABC:      c ≤ rad^{1+ε}) │                     ═══ L1/L2 shared μ_p
       ═══ L1/L2 shared μ_p,     │                     ═══ L3 novel height
           Mellin                │                         vs. novel C_2
       ═══ L3 shared novel       │                         (parallel
           height-from-BC        │                          structural form)
       ═══ L5/L6 shared wall     │                     ═══ L6 shared GUE
           (south-trough         │                         bulk + explicit
           arithmetic)           │                         formula
                                 │
       rh ═══════════════════════│═══════════════════  bsd
       (RESONANCE; CCM           │                    (ARITHMETIC; BC over
        resolvent; explicit      │                    imaginary quadratic K;
        formula)                 │                    Hecke characters)
       ═══ L2 Mellin bridge      │                    ═══ L1 shared μ_p;
           (same)                │                        N^⋊ extension to K
       ═══ L6 explicit formula   │                    ═══ L3 parallel
           cross-paper transport │                        height-from-BC
           (L6 CONSUMES rh       │                        (BSD uses Tate
           Layer 1)              │                         height; ABC
       ─── L3 BC-partition       │                         uses BC height)
           shared machinery      │                    ─── L5 shared Szpiro-
                                 │                        analog structure
                                 │                        (Szpiro ≡ ABC)
                                 │
       bgs ══════════════════════│═══════════════════  baum-connes
       (RESONANCE; GUE three-    │                    (RESONANCE; K-theory;
        tail; sine-kernel        │                    Cuntz-Li semigroup)
        PROVED Nov 2025)         │                    ═══ L1 shared N^⋊
       ═══ L6 bulk-regime        │                    ─── L4 K-theory of
           sine-kernel           │                        square-free support
           universality          │
                                 │
                           collatz (HARMONICS)
                           (additive-multiplicative
                            interface; paper60 §09)
                           ─── L2 Mellin-dual framing
                           ─── L3/L5 shared south-trough
                               arithmetic difficulty

                           pvnp (RESONANCE)
                           (BC algebra spectral-gap
                            rigidity)
                           ─── L1/L3 shared BC
                               operational content

                           schanuel (prospective)
                           (transcendence; algebraic
                            independence of L-values)
                           ─── L2/L6 face-only
                               (L-value transcendence
                               at explicit formula
                               arguments; speculative,
                               no x-ray yet)

                           ─── GUE three-tail structural
                               input (paper60 §14):
                               Twin Primes ↔ Goldbach ↔
                               ABC ↔ Cramer — four
                               ARITHMETIC-face consumers
                               of one Fredholm determinant
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch-D-Axiom-5** — shared C*-algebra structure + BC-KMS state.
  - Reason: Branch D Axiom 5 literally names $\{\mu_p\}$ (the primes as operators) as the generators of $\mathbb{N}^\rtimes$; paper61 §10 table places this as the $P_D$ target. ABC L1 IS Axiom 5 read through the ABC question (what do the generators know about $\operatorname{rad}$?).
  - Transposition candidate: YES (foundational; shared with every ARITHMETIC/RESONANCE south-trough vertex).

- **L1 ↔ goldbach:L1** — shared C*-algebra structure.
  - Reason: same $\mu_p$ entry point; both vertices rest on Bost-Connes 1995.
  - Transposition candidate: YES (identical content at this layer; paper60 §14 canonical).

- **L1 ↔ twin-primes:L1** — shared C*-algebra structure.
  - Reason: same $\mu_p$ entry point; ARITHMETIC-south-trough sibling.
  - Transposition candidate: YES.

- **L1 ↔ rh:L2** — shared C*-algebra structure (BC-algebra Hecke generation).
  - Reason: RH's L2 uses $\{\mu_p\}$ to generate the Euler product for $\zeta$; ABC's L1 uses the same generators for a different question.
  - Transposition candidate: YES.

- **L1 ↔ bsd:L1** — shared C*-algebra structure (BC over $K$ extension).
  - Reason: BSD extends the BC algebra to imaginary quadratic fields; ABC's L1 is the rational-field case.
  - Transposition candidate: YES (both factor through paper61 §10 $P_D$ target).

- **L1 ↔ baum-connes:L1** — shared C*-algebra structure (Cuntz-Li semigroup).
  - Reason: Cuntz-Li semigroup IS $\mathbb{N}^\rtimes$ in K-theory language; paper31 PROOF-CHAIN.md names the same $\mathbb{N}^*$.
  - Transposition candidate: YES.

- **L1 ↔ pvnp:L_BC** — shared C*-algebra structure.
  - Reason: pvnp uses BC algebra's spectral-gap rigidity; ABC uses the same algebra for a different question.
  - Transposition candidate: YES.

- **L1 ↔ bgs:L1** — shared C*-algebra structure (BC at KMS$_1$ → type III$_1$).
  - Reason: BGS's ITPFI-factor framework shares the BC $\mu_p$ generators.
  - Transposition candidate: YES.

- **L2 ↔ goldbach:L3** — shared spectral gap / scaling dimension (Mellin bridge).
  - Reason: same Mellin bridge; same narrowness framing (paper60 §14 "the bridge is narrow — converts average multiplicative to average additive efficiently, pointwise poorly"). Both ABC and Goldbach hit the bridge's pointwise limit.
  - Transposition candidate: YES.

- **L2 ↔ twin-primes:L1/L2** — shared spectral gap (explicit formula as Mellin bridge).
  - Reason: same explicit formula; twin-primes uses it for zero-pair correlation, abc uses it for height extraction.
  - Transposition candidate: YES.

- **L2 ↔ rh:L2/L3** — shared spectral gap (explicit formula).
  - Reason: RH provides the bridge's multiplicative-side data; ABC consumes the bridge's output.
  - Transposition candidate: YES.

- **L2 ↔ collatz:L_Mellin** — shared scaling dimension (HARMONICS canonical).
  - Reason: paper60 §09 HARMONICS canonical — same Fourier/dual-side framing.
  - Transposition candidate: SPECULATIVE (Collatz x-ray not yet written).

- **L2 ↔ bgs:L4** — shared spectral gap (sine-kernel universality output).
  - Reason: the bulk of the Mellin bridge's spectral output IS the sine-kernel universality (PROVED Nov 2025).
  - Transposition candidate: YES.

- **L2 ↔ schanuel** — face-only speculative (transcendence of $L$-value at bridge arguments).
  - Reason: Schanuel asks about algebraic independence of values; the Mellin bridge evaluates the Dirichlet series at integer points where transcendence comes in.
  - Transposition candidate: NO (no Schanuel x-ray yet).

- **L3 ↔ bsd:L3** — shared BC-KMS state (parallel BC-partition-derived height).
  - Reason: BSD uses a Tate-height analog derived from BC over $K$; ABC uses a BC-partition-derived height on $\mathbb{N}^\rtimes$. Same structural move: "BC partition derives a height."
  - Transposition candidate: YES (this is the PRIMARY cross-cut for the wall W_A1 — a capacitor cell connecting abc L3 to bsd L3 could BYPASS W_A1 via transposition; see §9).

- **L3 ↔ goldbach:L6** — shared BC-KMS state (parallel novel KMS$_1$-derived conjecture).
  - Reason: both are framework-original conjectures positing a BC-KMS-derived arithmetic closure. Same P4 structural form (rigidity from BC partition's structure).
  - Transposition candidate: YES (parallel structural novelty; both are south-trough walls).

- **L3 ↔ twin-primes:L4** — shared BC-KMS state (parallel arithmetic-fine-structure conjecture).
  - Reason: Twin Primes' $C_2$-extraction wall is an analog of ABC's height-extraction wall — both extract an ARITHMETIC constant from BC machinery.
  - Transposition candidate: YES.

- **L3 ↔ rh:L_partition** — shared BC-KMS state.
  - Reason: the proposed height uses $Z(\beta) = \zeta(\beta)$ or its derivatives at $\beta = 1$; RH's analysis of $\zeta$ near $\beta = 1$ is structural input.
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ schanuel** — face-only speculative (transcendence of height values).
  - Reason: algebraic independence of height values over $\mathbb{Q}$ could tie to Schanuel's conjecture.
  - Transposition candidate: NO.

- **L4 ↔ bsd:L1/L4** — shared C*-algebra structure (number-field ITPFI extension).
  - Reason: BC over imaginary quadratic $K$ has an analogous truncation to square-free ideals in $\mathcal{O}_K$; the radical of $abc$ generalizes to the ideal-theoretic radical.
  - Transposition candidate: YES.

- **L4 ↔ baum-connes:L2** — shared ITPFI factor type.
  - Reason: K-theory of the Cuntz-Li semigroup encodes the square-free-support information; same ITPFI-truncation move.
  - Transposition candidate: YES.

- **L4 ↔ rh:L_Euler** — shared C*-algebra structure (Euler product as ITPFI).
  - Reason: the Euler product $\prod_p (1 - p^{-\beta})^{-1}$ IS the ITPFI-factor product; truncating to square-free support is dual to the radical construction.
  - Transposition candidate: YES.

- **L4 ↔ goldbach:L2** — shared ITPFI factor type (unique factorization).
  - Reason: both rest on the ITPFI factorization $\omega_1 = \otimes_p \omega_1^{(p)}$; ABC's radical picks one-per-prime, Goldbach's unique-factorization picks all-with-multiplicity.
  - Transposition candidate: YES.

- **L4 ↔ twin-primes:L4** — shared ITPFI factor type (arithmetic factor from BC).
  - Reason: both use ITPFI-truncated-product structure; Twin Primes' $C_2 = \prod_{p>2}(1 - 1/(p-1)^2)$ is an ITPFI-derived arithmetic factor.
  - Transposition candidate: YES.

- **L5 ↔ bsd:L5** — shared L-value / C*-algebra structure (Szpiro ≡ ABC).
  - Reason: Szpiro's conjecture (on elliptic-curve discriminants) is EQUIVALENT to ABC; both are consequences of an analogous BC-height construction.
  - Transposition candidate: YES (capacitor-cell candidate: BC-height → both Szpiro and ABC in parallel).

- **L5 ↔ goldbach:L5** — shared scaling dimension (south-trough wall).
  - Reason: both need BC machinery to produce quantitative arithmetic bounds; shared additive-multiplicative wall framing (paper60 §14).
  - Transposition candidate: YES.

- **L5 ↔ twin-primes:L5** — shared L-value (asymptotic constant).
  - Reason: $K(\varepsilon)$ form is analogous to $C_2 \cdot x / (\log x)^2$ asymptotic form; both are south-trough quantitative closure statements.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ rh:L_short-dist** — shared L-value (zero-free region bounds).
  - Reason: $\varepsilon$-dependence in $K(\varepsilon)$ is structurally controlled by the RH zero-free region.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ schanuel** — face-only (transcendence of $K(\varepsilon)$).
  - Reason: explicit Baker-style $K(\varepsilon)$ involves transcendental $L$-values.
  - Transposition candidate: NO (no Schanuel x-ray yet).

- **L5 ↔ vp-vs-vnp:L_counting** — face-only speculative (effective counting bounds).
  - Reason: effective ABC uniform bounds could feed algebraic complexity; speculative.
  - Transposition candidate: NO.

- **L6 ↔ rh:L_explicit-formula** — shared zero distribution (PRIMARY EDGE).
  - Reason: abc's L6 CONSUMES rh's Layer 1 as input; same explicit formula; same zero distribution. This is the cross-paper transport declared in paper37 programme §2.
  - Transposition candidate: YES (this is the structural backbone of L6; no capacitor bypass because RH is upstream).

- **L6 ↔ grh:L4/L5** — shared zero distribution (generalized zeros for multi-modulus ABC).
  - Reason: GRH controls Dirichlet L-function zeros; Dirichlet-ABC variants consume GRH the way rational-ABC consumes RH.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ bgs:L4/L5** — shared zero distribution (GUE sine-kernel).
  - Reason: the bulk-regime spacing data (PROVED Nov 2025) feeds L6's $K(\varepsilon)$ extraction.
  - Transposition candidate: YES.

- **L6 ↔ twin-primes:L4** — shared zero distribution (GUE fine structure).
  - Reason: both extract arithmetic constants from GUE fine-structure data; Twin Primes extracts $C_2$, ABC extracts $K(\varepsilon)$.
  - Transposition candidate: YES.

- **L6 ↔ goldbach:L6** — shared BC-KMS state (novel KMS$_1$-derived closure).
  - Reason: parallel structural form — both are outer-ring closure statements deriving from BC-KMS machinery.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ cramer:L_large-gap** — shared zero distribution (GUE three-tail).
  - Reason: Cramér lives in the large-gap tail; ABC's L6 uses the bulk; both are views of the same Fredholm determinant $\det(1 - K_{\sin})$ (paper60 §14).
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ schanuel** — face-only (transcendence of $L$-value arguments in $K(\varepsilon)$).
  - Reason: explicit formula evaluates at specific points where transcendence appears.
  - Transposition candidate: NO.

- **L6 ↔ lindelof:L_amplitude** — face-only (bounded ζ moments).
  - Reason: bounded $\zeta$ moments on the critical line feed the same explicit-formula apparatus.
  - Transposition candidate: SPECULATIVE.

**Summary**: 32 cross-cut edges identified across 6 layers (avg ~5.3 cross-cuts per layer — high connectivity because ABC's $P_D$ dominance places it adjacent to every other $P_D$ vertex). 15 verified (paper60 §14 + paper61 §10/§12 + proof-chain cross-references), 17 SPECULATIVE or FACE-ONLY (pending sibling-vertex x-rays for Schanuel, Collatz, Cramér, etc.). The PRIMARY edge is **L6 ↔ rh:L_explicit-formula** (cross-paper transport of spectral prime density), backed by paper37-abc programme §2's explicit declaration. The STRUCTURAL KEY edge is **L3 ↔ bsd:L3** (shared BC-partition-derived height construction) — this is the capacitor-cell candidate that could BYPASS the W_A1 wall via transposition between ABC and BSD.

---

## §8 Current Walls

- **W_A1 — BC-Mellin-to-rad bridge / BC-partition height function**: The central technical gap of the abc chain. Does the BC algebra's partition function $Z(\beta) = \zeta(\beta)$ (or a natural derivative thereof) define a height function $h_{BC}: \mathbb{N}^\rtimes \to \mathbb{R}_{\geq 0}$ that controls $\operatorname{rad}(abc)$ in the ABC inequality form? The analogy to Szpiro's 1981 conductor-discriminant inequality on elliptic curves is STRUCTURAL (paper37 programme §2) but not proven. Status: **OPEN as a conjecture**, NOT YET DECOMPOSED in `strategy/decomposition/…`. Confidence on the wall: 0.4 (ring confidence 1/10). Audit-strategy.md §4 declares W_A1 as the single primary wall. If W_A1 closes via construction, L4 is a modest structural identification, L5 a moderate calculation, and L6 a quantitative refinement using cross-paper transport from RH — the chain's ONLY substantive wall is L3. Capacitor-cell candidate: **transposition from bsd:L3** (shared BC-partition-derived height construction; BSD uses Tate-height analog in BC over $K$). Paper60 §28 "The South Trough Needs Lifting" lists this wall alongside Goldbach's novel KMS decomposition and Twin Primes' $C_2$-extraction as the three framework-original south-trough conjectures.

Additional structural notes (NOT named walls — these are open sub-items downstream of W_A1):
- L5 (ABC inequality closure): depends on W_A1; if W_A1 closes, L5 is downstream calculation not a separate wall.
- L6 (explicit $\varepsilon$-dependence): depends on RH Layer 1 (cross-paper transport); not an independent RH assumption (paper37 §2); RH is upstream and NOT a wall of abc's chain.
- Comparison with Mochizuki IUT: NOT a wall. The framework route is ORTHOGONAL to IUT (paper37 §3). We neither endorse nor refute. If Mochizuki's IUT is ever validated, the two routes must agree at the ABC inequality value; the framework can be tested against any Mochizuki corollary.

No other named walls. The chain has one primary wall (L3/W_A1) and five OPEN-but-derivative-if-W_A1-closes items.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/abc/PROOF-CHAIN.md` — **NOT YET CREATED** (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, the candidate decomposition of L3/W_A1 into three sub-links (L3.a operator-theoretic height construction; L3.b Szpiro-analog inequality; L3.c extension to coprime triples) should be the first deliverable. The L5 sub-requirements (L5.a-c) are downstream and decompose after L3.
- **CCM verification**: `strategy/ccm-verification/ledger.md#abc` — **NOT YET CREATED** (CCM-verification bundle has empty `proof-chain/` directory as of 2026-04-15). ABC's L6 inherits RH's CCM 2025 conditionality through cross-paper transport. Expected verdict when ledger written: **CCM-DEPENDENT AT L6 via RH transport** (the dependency is inherited, not independent; see paper37 §2 cascading-impact note on W1/W2 closure).
- **Inner rings**: NOT APPLICABLE — ABC is a primary outer-ring vertex, not an inner-ring object.
- **Capacitor-cell candidate for W_A1 bypass**: the **transposition from bsd:L3** (shared BC-partition-derived height) is the most promising cross-cut-to-capacitor conversion in the abc chain. If a capacitor cell is constructed for "BC-K height → rad-type bound on number-field objects," the cell TRANSPOSES between BSD (L-function height) and ABC (radical height); this would bypass W_A1 by proving it as a corollary of a shared structural theorem. Cell candidate cite: capacitor 09 (BSD/ABC parallel height) — currently DRAFT, not yet written.
- **Comparison to Joshi framework**: Joshi 2021+ is an alternative formalization of IUT ideas; not aligned with our BC-Mellin route. Per paper37 §3 we CITE Joshi alongside Mochizuki and Scholze-Stix as acknowledgment; no cascading input from Joshi to our chain.
- **No prior ORA v8 runs on abc**: unlike ym/rh/bsd/pvnp (which have documented Runs 1-5 pipelines), abc has not yet entered the ORA pipeline. This X-Ray is the FIRST adversarial-grade annotation of the abc chain. Next step: `strategy/abc/` bundle per abc-audit-brief.md INVOCATION STYLE B.
- **Paper60/§28 South Trough Lifting**: abc is one of the four framework-original south-trough conjectures awaiting construction of its novel height/decomposition. The broader strategic context is paper60 §28 "The South Trough Needs Lifting" — concentrated excision/bypass/repair energy targeting Turb, H12, ABC, Goldbach, Twin Primes, Schanuel, VP.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W_A1: BC-partition height function on $\mathbb{N}^\rtimes$** (from L3, primary named wall). No candidate in the literature exists. Proposed form: some spectral-derivative of $Z(\beta)$ at $\beta = 1$ that picks up radical structure via ITPFI truncation. — face: ARITHMETIC, projection: $P_D$, pattern: P4. STATUS: **OPEN as a conjecture**; confidence 0.4; BYPASS candidate via capacitor transposition with bsd:L3 is unfilled. This is the DOMINANT open item in the abc proof chain.
- **G2 — L4 $\operatorname{rad}(n)$-as-ITPFI-norm structural identification** (from L4). Status: CONJECTURED in paper61 §12 vertex 18 but not proved as a theorem. Downstream of L3. — face: ARITHMETIC, projection: $P_D$, pattern: P1.
- **G3 — L5 ABC inequality derivation from L3+L4** (from L5). Status: OPEN; downstream of L3 and L4. Requires the BC-height → rad-bound passage and the "sufficiently large" → "all" closure. — face: ARITHMETIC, projection: $P_D$, pattern: P5.
- **G4 — L5 sub-items (L5.a/b/c)** decomposition of the inequality closure: (a) lift BC height from $\mathbb{N}^\rtimes$ to coprime triples; (b) convert height bound into $\operatorname{rad}(abc)^{1+\varepsilon}$ form; (c) "sufficiently large" → "all but finitely many" closure. All downstream of L3. — face: ARITHMETIC, projection: $P_D$, pattern: P5.
- **G5 — L6 explicit $K(\varepsilon)$ form** (from L6). Status: OPEN; depends on L5 + RH Layer 1 cross-paper transport. The Baker-style effective refinement is the Annals-grade target; the non-effective form is the minimum community-standard deliverable. — face: RESONANCE, projection: $P_O$, pattern: P5.
- **G6 — IUT comparison** (framework-bonus): if Mochizuki IUT is ever validated or definitively refuted, the framework route must be tested against it. NOT a wall of our chain, but an open disposition question for publication positioning. — face: (framework-meta), projection: (framework-meta), pattern: (framework-meta).

That's six open items, cascading from W_A1 (G1). The chain's SOLE substantive wall is G1; G2-G5 become downstream calculations once G1 resolves; G6 is a framework-positioning item.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record would be at `strategy/x-ray/pac-output/runs/run-XX/vertices/abc/critic-attacks.md` (pending first ORA run on abc).

Notable arbiter decisions:
- **L3 projection**: $P_D$ over $P_O$ — the height CONSTRUCTION is $P_D$-operational (BC partition is a Branch D object), even though the wall W_A1 is Clay-adjacent. $P_O$ is reserved for L6 closure.
- **L4 pattern**: P1 over P4 — the reinterpretation of $\operatorname{rad}(n)$ as ITPFI-truncated weight is a GEOMETRIC REINTERPRETATION move (P1), even though the resulting identity is rigid (P4).
- **L5 projection**: $P_D$ over $P_O$ (per arbiter on L3) — the operational content lives inside $P_D$; $P_O$ is L6's dedicated projection.
- **L6 face**: RESONANCE over ARITHMETIC — the EXTRACTION mechanism (zero-spacing → $K(\varepsilon)$) is resonance-mode (paper60 §15), not arithmetic-lattice.
- **L6 projection**: $P_O$ over $P_D$ — the explicit $\varepsilon$-dependence IS the outer-ring Clay-adjacent closure statement; paper61 §17 outer-ring boundary.

Author wins on 28 / 30 field decisions (5 fields × 6 layers = 30). The two CRITIC WINS are on L3 projection and L6 face; both are documented above.

---

*End of ABC X-Ray. Snapshot 2026-04-15. 6 layers annotated. 32 cross-cuts identified. ARITHMETIC-canonical, $P_D$-dominant, P4/P5-mixed proof chain. One primary wall (W_A1 at L3); non-IUT route; capacitor-bypass candidate via transposition with bsd:L3. Paper60 §28 south-trough vertex, confidence 1/10.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
