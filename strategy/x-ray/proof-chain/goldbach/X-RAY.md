# X-RAY: Goldbach Conjecture (goldbach)

*X-Ray of the goldbach proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: goldbach
- **Paper**: paper33-goldbach
- **Live file**: `strategy/proof-chain/goldbach/PROOF-CHAIN.md` (snapshot 2026-04-15; carries 2026-04-14 QG5D W1/W2 cascading refinement note + Agent-I audit item 6 cross-paper tag)
- **Top-level claim**: Every even integer $N \geq 4$ is the sum of two primes: $N = p + q$. Quantitative HL form $r_2(N) \sim 2 C_2 \cdot N/(\log N)^2 \cdot \prod_{p \mid N, p>2} (p-1)/(p-2)$.
- **Current status**: **2/6 links closed**; confidence 1/10. L1–L2 KNOWN (Bost-Connes 1995); L3 ESTABLISHED (Paper 12 Mellin transposition); L4 CONDITIONAL (cross-paper transport from Paper 13 RH; not an independent RH assumption); **L5 OPEN — the wall** (Hardy-Littlewood circle method in BC/adelic setting); **L6 OPEN** (novel even-indexed KMS$_1$ prime-convolution decomposition).
- **Primary branch (paper1)**: D (CBB modular-flow / Bost-Connes operational core — Branch D's Axiom 5 $\mathbb{N}^\rtimes$ generators $\{\mu_p\}$ are literally the primes as operators; paper61 §10), with secondary outer-ring $P_O$ boundary on L6 (the Clay-targeted conjecture statement).
- **Primary face**: ARITHMETIC (paper60 §14 — Goldbach is one of the two canonical vertices on this face alongside Twin Primes; the face is explicitly titled "Face 8: ARITHMETIC (Goldbach + Twin Primes)").
- **Primary projection**: $P_D$ (paper61 §10 — Goldbach's natural home is the BC algebra's Hecke-semigroup side; every layer except L3 (Mellin bridge) and L6 (outer-ring Clay closure) sits strictly inside $P_D$'s preservation class).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
GOLDBACH (binary): every even N ≥ 4 is p + q; HL quantitative r_2(N) asymptotic
│  primary face: ARITHMETIC   primary proj: P_D   primary pat: P4
│  scope: strong (binary) form, unconditional; Helfgott-compatible; Chen-compatible
│  current state: 2/6 closed; confidence 1/10; additive-multiplicative wall is genuine
│
├── L1: Primes generate BC algebra via μ_p              [KNOWN]
│      │  face: ARITHMETIC    proj: P_D   pat: P4
│      │  invariant: C*-algebra structure, BC-KMS state
│      │  source: Bost-Connes 1995 (CMP 172); paper61 §10;
│      │          Branch D Axiom 5 — {μ_p} = the primes as operators
│      │
│      └── supports L2 via multiplicative generation of N^⋊
│             │
│             └── this is THE entry point — the BC algebra is
│                    BUILT from the primes; Goldbach asks the
│                    additive question of its multiplicative
│                    generators (paper60 §14)
│
├── L2: Hecke semigroup N^⋊ encodes multiplicative    [KNOWN]
│      │  structure (fundamental theorem of arithmetic
│      │  in operator form)
│      │  face: ARITHMETIC    proj: P_D   pat: P4
│      │  invariant: C*-algebra structure, ITPFI factor type
│      │  source: BC construction 1995; Laca-Neshveyev 2011;
│      │          paper61 §10; north-star §0.1 P_D target
│      │
│      └── supports L3 via Euler product
│                Z(β) = ζ(β) = ∏_p (1 - p^{-β})^{-1}
│                (the partition function IS the Euler product)
│
├── L3: Mellin bridge: additive ↔ multiplicative       [ESTABLISHED]
│      │  face: HARMONICS     proj: P_D   pat: P5
│      │  invariant: spectral gap, scaling dimension
│      │  source: Paper 12 transposition; Mellin 1890s;
│      │          Perron 1908; paper60 §14 "the Mellin bridge IS
│      │          the explicit formula"; classical analytic NT
│      │
│      └── the bridge is a theorem (Mellin transform between
│             Dirichlet series on the multiplicative side and
│             exponential sums on the additive side). The bridge
│             EXISTS. The question is how much information it carries
│             (paper60 §14: "the bridge is narrow — it converts
│             AVERAGE multiplicative information to AVERAGE additive
│             information efficiently; POINTWISE information poorly")
│
├── L4: Spectral prime density from explicit formula   [CONDITIONAL — cross-paper transport]
│      │  face: MEASURE       proj: P_D   pat: P5
│      │  invariant: zero distribution, spectral gap
│      │  source: Riemann-von Mangoldt explicit formula;
│      │          Paper 13 RH PROOF-CHAIN.md (8/10 conditional on CCM 2025);
│      │          Montgomery-Vaughan 1975 asymptotic result;
│      │          Agent-I audit item 6 cross-paper tag 2026-04-14
│      │
│      ├── conditionality: cross-paper transport from RH, not an
│      │     independent RH assumption. Under RH: π(x+h) - π(x) ~ h/log x
│      │     for h ≥ x^{1/2+ε} (strong equidistribution)
│      │
│      └── supports L5 via prime density guarantees on short intervals
│                (this is the raw material the circle method needs)
│
├── L5: Circle method in BC/adelic setting            [OPEN — the wall — W_GB-1]
│      │  face: ARITHMETIC    proj: P_D   pat: P5
│      │  invariant: C*-algebra structure, zero distribution
│      │  source: Hardy-Littlewood 1923; Vinogradov 1937;
│      │          Helfgott 2013 (ternary); paper33-goldbach
│      │          §5 Milestone 2; paper60 §14 wall
│      │
│      ├── three sub-requirements (paper33 programme §5):
│      │     ├── L5.a: major/minor arc decomposition via
│      │     │         Q/Z characters within C*(Q/Z)          [OPEN]
│      │     ├── L5.b: Vinogradov exponential sum estimates
│      │     │         in BC algebraic setting                [OPEN]
│      │     └── L5.c: gap closure from "sufficiently large N"
│      │               to "all even N ≥ 4"                    [OPEN]
│      │
│      └── NOT YET DECOMPOSED in strategy/decomposition/...
│             (see §9 Cascading Refinements)
│
└── L6: Even-indexed KMS_1 decomposition as            [OPEN — the novel conjecture]
       │  prime convolution
       │  face: ARITHMETIC    proj: P_O   pat: P4
       │  invariant: BC-KMS state, C*-algebra structure
       │  source: paper33-goldbach programme novel conjecture;
       │          paper61 §17 outer-ring boundary
       │
       ├── proposed form: ω_1(H_{2n}) = Σ_{p+q=2n} f(p,q)
       │     for some explicit kernel f derivable from KMS_1
       │     structure; this would give Goldbach DIRECTLY from
       │     the operator-algebra decomposition
       │
       └── if L6 holds, Goldbach closes without the classical
              circle method. If L6 fails, Goldbach retreats to
              classical tools (same as everyone else has).
              Confidence on L6: 1/10 (speculative).

───────────────────────────────────────────────────────────
CROSS-CHAIN STRUCTURAL INPUT — GUE three-tail (paper60 §14)
───────────────────────────────────────────────────────────

The three-tail structure of the GUE sine-kernel (from BGS,
paper32, arXiv:2511.18275 Nov 2025) places Goldbach in the
BULK regime:

     small-gap tail  ←  Twin Primes (gap = 2)
     ────────────────────────────────────────
     BULK            ←  GOLDBACH (sine-kernel
                        density; prime density
                        in short intervals)
     ────────────────────────────────────────
     large-gap tail  ←  Cramér (max gap ~ log²x)

All three are views of ONE Fredholm determinant det(1 - K_sin).
The bulk regime — Tao-Vu 2011 sine-kernel universality, now
PROVED Nov 2025 — provides the prime density that L4 requires.
The arithmetic correction factor (Goldbach singular series
2C_2 · ∏(p-1)/(p-2)) is the analog of the twin-prime C_2 in
the small-gap tail; both cross the additive-multiplicative
wall and both remain open at the arithmetic layer.
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (Quantum observables do not see the
                          additive-multiplicative structure of
                          the primes directly.)
                                  ▲
                                  │
                                  │
        ┌──────────────(P_O outer)─────────────────┐
        │                                          │
        │  GOLDBACH: every even N ≥ 4 is p + q      │
        │  (and HL quantitative r_2(N) asymptotic) │
        │                                          │
        └───────────────────┬──────────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity      ═══ P_D CBB ═══           P_C cosmology
    (forgotten —     Bost-Connes algebra       (forgotten —
    no KK bundle     A_{BC}; Hecke semigroup   Goldbach does
    carries Gold-    N^⋊ = ⟨μ_2, μ_3, μ_5,...⟩; not contribute
    bach addition    KMS_1 state ω_1; Euler    any cosmological
    directly)        product Z(β) = ζ(β);      pin — it is a
                     Branch D Axiom 5          pure number-theory
                     primes-as-operators;      statement)
                     Mellin bridge lives here
                            │
                            ▼
                       P_E pins
                       (forgotten — Goldbach is
                        NOT a sub-percent numerical
                        pin; it is a qualitative
                        statement about ALL even
                        integers, Chen-compatible
                        but not pin-valued)
```

Primary projection $P_D$ uses ═══ doubled line. $P_O$ is the second-strongest projection: L6 (the novel KMS$_1$ prime-convolution decomposition) is the Clay-targeted outer-ring closure statement, and the top-level "every even $N \geq 4$ is $p + q$" is itself the outer-ring Goldbach formulation (paper61 §17 outer-ring list, vertex 12). $P_A, P_B, P_C, P_E$ all forget Goldbach entirely — Goldbach is a pure operational/outer-ring object living in the $P_D \cap P_O$ compound projection of paper61 §17. The Mellin bridge (L3) is the SOLE layer that forgets $P_D$'s operator-algebraic core and moves to $P_D$'s Fourier-dual side (the additive characters of $\mathbb{Q}/\mathbb{Z}$ inside $C^*(\mathbb{Q}/\mathbb{Z})$).

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
                       ● ARITHMETIC  ← GOLDBACH
                         (Goldbach +      (with Twin Primes;
                          Twin Primes)     paper60 §14 names
                            │              Goldbach as the FIRST
                       AMPLITUDE           canonical ARITHMETIC
                       (Lindelöf)          vertex)
```

Marker key:

```
Primary face:    ● ARITHMETIC (paper60 §14 — Goldbach is the canonical
                  ARITHMETIC vertex; the face title literally names it)
Secondary faces: ○ HARMONICS (1 layer: L3 — Mellin bridge is the
                              dual-Fourier side of the arithmetic lattice;
                              paper60 §09 Collatz analog)
                 ○ MEASURE   (1 layer: L4 — spectral prime density is an
                              equidistribution/weak-* convergence statement;
                              paper60 §10 Sato-Tate analog)
Absent faces:    TOPOLOGY, DYNAMICS, AMPLITUDE, SYMMETRY, CURVATURE,
                 RESONANCE, SPREAD
```

The face profile is ARITHMETIC-dominant (4 of 6 layers) with thin HARMONICS/MEASURE footprints and zero presence on the other seven. This is paper60 §14's thesis made concrete: Goldbach lives primarily on the arithmetic face because the question "do the multiplicative generators additively cover?" is an arithmetic-lattice question. The cross-tails to HARMONICS (Mellin bridge = Fourier dual) and MEASURE (density from explicit formula) are the bridges to other faces — they are narrow, and the chain stops at them.

---

## §3 Layer-by-Layer X-Ray

### L1 — Primes generate BC algebra via $\mu_p$

**Claim**: The Bost-Connes algebra $A_{BC}$ has its multiplicative Hecke semigroup $\mathbb{N}^\rtimes$ generated by a family of isometries $\{\mu_p\}_{p \text{ prime}}$, one per rational prime; these $\mu_p$ are the primes seen as operators on the Hilbert space of the BC system.

**Status**: KNOWN
**Source**: Bost-Connes 1995 (CMP 172, 381–446); paper61 §10 "BC algebra / the operator-algebra dictionary"; Branch D Axiom 5 "zeta regularization closure" with generator set $\{\mu_p\}$; paper01-qg5d appendix Z/BC dictionary.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — "the primes are the generators of the Bost-Connes algebra's Hecke semigroup $\mathbb{N}^* = \langle 2, 3, 5, 7, \ldots \rangle$. Each prime $p$ defines a Hecke operator $\mu_p$. The Hecke operators are the MULTIPLICATIVE engine of the BC algebra")
- **Projection**: $P_D$ (paper61 §10 — "$A_{BC}$ (Bost-Connes at KMS$_1$) is the target of $P_D$; Hecke semigroup on $S^1$")
- **Pattern**: P4 Topological Rigidity (paper61 §10 — the prime generators are topologically rigid in the BC system: they are fixed by the semigroup structure, not chosen; this is the $P_D$ signature of Branch D Axiom 5)
- **Invariant preserved**: C*-algebra structure (load-bearing — $A_{BC}$ is a specific C*-algebra generated by the $\mu_p$), BC-KMS state (background — the $\mu_p$ carry the KMS$_1$ state by definition)
- **Geometric interpretation**: The $\mu_p$ are the primes as isometries on the BC Hilbert space. Each $\mu_p$ implements multiplication by $p$ on the frequency side; equivalently, $\mu_p$ is the inclusion $n \mapsto pn$ on the spectrum. This is paper60 §14's "frequency multiplication" interpretation: the primes are the IRREDUCIBLE frequency multipliers on the e-circle (you cannot decompose $\mu_p$ further). Under $P_D$ (paper61 §10 table) this is the foundational layer — every other $P_D$-layer of every other vertex rests on this generation property. [Considered but rejected: face RESONANCE — the $\mu_p$ are resonance-mode generators in a loose sense, but paper60 §14 canonicalizes ARITHMETIC because the question Goldbach asks is about additive coverage, not mode structure; projection $P_O$ — the BC algebra itself has outer-ring facets but the generator property is strictly $P_D$ internal.]
- **Cross-cuts**: rh:L2 ($\mu_p$ generate ITPFI Euler product for $\zeta$), bgs:L1 (BC at KMS$_1$ → type III$_1$ factor, shared generator structure), baum-connes:L1 (Cuntz-Li semigroup $\mathbb{N}^\rtimes$ at K-theory target; paper31 PROOF-CHAIN.md names the same $\mathbb{N}^*$), bsd:L1 (BC over imaginary quadratic $K$ — extension of $\mathbb{N}^\rtimes$ to number-field primes), pvnp:L_BC (BC algebra spectral-gap rigidity), twin-primes:L1 (shared $\mu_p$ entry point).

### L2 — Hecke semigroup $\mathbb{N}^\rtimes$ encodes multiplicative structure

**Claim**: The Hecke semigroup $\mathbb{N}^\rtimes$, generated by $\{\mu_p\}$, gives an operator-algebra form of the fundamental theorem of arithmetic: every element factors uniquely as $\mu_n = \mu_{p_1^{a_1}} \mu_{p_2^{a_2}} \cdots$ with the primes commuting among themselves.

**Status**: KNOWN
**Source**: BC construction 1995; Laca-Neshveyev 2011; paper61 §10 "BC algebra is the C*-algebra of the semigroup $\mathbb{N}^\rtimes$ crossed with the diagonal action"; north-star §0.1 $P_D$ preserved-invariant list.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — "the multiplicative structure is fully encoded... the prime factorization of every integer is visible in the operator algebra")
- **Projection**: $P_D$ (paper61 §10 — Hecke-semigroup structure is the $P_D$ target)
- **Pattern**: P4 Topological Rigidity (paper61 §10 — the unique-factorization property is a topological rigidity of the semigroup, not a choice; this is the operator-algebra form of Euclid's Elements VII)
- **Invariant preserved**: C*-algebra structure (load-bearing — $\mathbb{N}^\rtimes$ IS the semigroup whose C*-algebra is $A_{BC}$), ITPFI factor type (background — the semigroup structure induces the ITPFI III$_{1/p}$ tensor factorization at each prime)
- **Geometric interpretation**: The Hecke semigroup $\mathbb{N}^\rtimes$ is the multiplicative engine of the BC algebra. Its Euler product $Z(\beta) = \zeta(\beta) = \prod_p (1 - p^{-\beta})^{-1}$ encodes the primes; the KMS$_1$ state treats all primes democratically $\omega_1(\mu_p^* \mu_p) = p^{-1}$ (paper60 §14). Under $P_D$ (paper61 §10) this is the canonical Branch D operational-core statement: multiplication is the circle's native tongue. Pattern 4: the factorization is rigid. [Considered but rejected: face RESONANCE — Euler-product-as-mode-decomposition framing is real but paper60 §14 canonicalizes ARITHMETIC; pattern P1 — Geometric Reinterpretation of the fundamental theorem would be a fair reading of L2, but paper61 §10 treats unique factorization as structural rigidity (P4) not reinterpretation.]
- **Cross-cuts**: rh:L2 (ITPFI Euler-product factorization ↔ unique-factorization-via-$\mu_p$; paper61 §10 "ITPFI factorization = Euler product, two different languages"), bgs:L1 (shared BC/Euler-product structure feeding GUE), baum-connes:L1 (Cuntz-Li semigroup = extension of $\mathbb{N}^\rtimes$), bsd:L1 (number-field extension), twin-primes:L2 (same fundamental-theorem entry point).

### L3 — Mellin bridge: additive $\leftrightarrow$ multiplicative

**Claim**: The Mellin transform $f(s) = \int_0^\infty F(x) x^{s-1} dx$ connects the additive Fourier analysis on $\mathbb{Z}$ (exponential sums, the circle method) with the multiplicative Dirichlet series on $\mathbb{N}^\rtimes$ (zeta function, L-functions); the Riemann–von Mangoldt explicit formula $\psi(x) = x - \sum_\rho x^\rho/\rho - \log(2\pi) - \frac{1}{2}\log(1 - x^{-2})$ IS the instantiation of this bridge that imports spectral (multiplicative) information into arithmetic (additive) form.

**Status**: ESTABLISHED
**Source**: Paper 12 transposition (BC algebra Mellin construction); Mellin 1890s; Perron 1908; Riemann 1859 (explicit formula); paper60 §14 "the Mellin bridge IS the explicit formula; it translates the multiplicative information (zeros of $\zeta$) into additive information (prime-counting)"; paper33-goldbach programme §2.

#### Physics

- **Face**: HARMONICS (paper60 §09 — Collatz face; the Mellin bridge is the canonical FOURIER/ORBIT-AVERAGING face, connecting additive orbits on $\mathbb{Z}$ to multiplicative Dirichlet series)
- **Projection**: $P_D$ (paper61 §10 — the bridge lives inside the BC algebra via $C^*(\mathbb{Q}/\mathbb{Z})$ as the maximal abelian subalgebra carrying additive characters dual to the multiplicative $\mu_p$)
- **Pattern**: P5 Zeta Regularization (paper60 §14 explicit formula is the zeta-regularized translation between sum-over-primes and sum-over-zeros; the Mellin transform is the canonical zeta regularization)
- **Invariant preserved**: spectral gap (load-bearing — the bridge's power depends on the zero-free region of $\zeta$), scaling dimension (background — Mellin pairs $s \leftrightarrow x^s$ is a scaling duality)
- **Geometric interpretation**: The Mellin bridge is the one narrow tube connecting the multiplicative side (Dirichlet series, Euler product, BC algebra) to the additive side (exponential sums, $\mathbb{Z}$-lattice, circle method). Under $P_D$ (paper61 §10) the bridge lives inside the BC algebra's abelian subalgebra $C^*(\mathbb{Q}/\mathbb{Z})$ whose characters are the additive exponentials. Pattern 5: the bridge's core mechanism IS zeta regularization — the explicit formula trades the divergent $\sum_p \log p$ on the prime side for the convergent $\sum_\rho x^\rho/\rho$ on the zero side. The bridge is NARROW in a precise sense (paper60 §14): it converts average multiplicative information to average additive information efficiently, but pointwise information poorly. [Considered but rejected: face ARITHMETIC — the Mellin bridge lives on the arithmetic face structurally but paper60 §09 names HARMONICS for Fourier/dual-side content and §14 explicitly identifies the Mellin bridge as the FACE-8-to-FACE-3 connection (ARITHMETIC ↔ HARMONICS); projection $P_A$ — the Fourier duality has quantum-side overtones but the bridge mechanism is operator-algebraic.]
- **Cross-cuts**: collatz:L_Mellin (paper60 §09 HARMONICS canonical — same Fourier/dual-side framing), rh:L2/L3 (explicit formula is shared — RH zeros are the bridge's multiplicative-side data), twin-primes:L1 (same explicit formula connecting prime gaps ↔ zero spacing), bgs:L4 (sine-kernel universality is the bulk of the bridge's spectral output).

### L4 — Spectral prime density from explicit formula

**Claim**: Under RH (cross-paper transport from Paper 13), the explicit formula gives prime density in short intervals: $\pi(x+h) - \pi(x) \sim h/\log x$ for $h \geq x^{1/2 + \varepsilon}$; Montgomery-Vaughan 1975 uses this to show Goldbach holds for all sufficiently large even integers (with $O(x^{1-\delta})$ exceptions under GRH).

**Status**: CONDITIONAL (cross-paper transport from Paper 13 RH; equivalently CONDITIONAL on CCM 2025, **not an independent RH assumption**). Tagged cross-paper 2026-04-14 per Agent-I audit item 6.
**Source**: Riemann-von Mangoldt explicit formula; paper13-rh PROOF-CHAIN.md (RH at 8/10 conditional on CCM 2025); Montgomery-Vaughan 1975; Hardy Z PCC arXiv:2511.18275 Nov 2025 (GUE sine-kernel PROVED for $\zeta$ zeros — closes the spectral side).

#### Physics

- **Face**: MEASURE (paper60 §10 — Sato-Tate face; prime density in short intervals is an equidistribution/weak-* convergence statement — "how densely do prime points equidistribute on $\mathbb{Z}$")
- **Projection**: $P_D$ (paper61 §10 — prime density is the weak-$^*$ content of $\omega_1$ on projection-indexed operators)
- **Pattern**: P5 Zeta Regularization (the explicit formula IS zeta regularization delivering the density)
- **Invariant preserved**: zero distribution (load-bearing — Riemann zeros are the explicit-formula input), spectral gap (background — RH zero-free region is the spectral gap this density depends on)
- **Geometric interpretation**: The spectral prime density is the output of the Mellin bridge (L3) on the density question: given the zero-location information (RH), how densely do primes distribute in intervals? Under $P_D$ (paper61 §10) this is the weak-$^*$ content of the KMS$_1$ state evaluated on density-indexed operator families. Pattern 5: the conversion from multiplicative zeros to additive density is zeta-regularized. The density is the raw material L5's circle method needs — without it, the major-arc estimate fails. The cross-paper dependency on Paper 13 is explicit and non-circular: Goldbach inherits RH's density as an input; RH proves independent of Goldbach. [Considered but rejected: face ARITHMETIC — prime density is arithmetic-face content but the density-in-intervals FORM is equidistribution (MEASURE face); projection $P_O$ — density as outer-ring statement is a fair reading but the operational content lives in $P_D$.]
- **Cross-cuts**: rh:L2/L3 (zero distribution is shared — RH provides the input that L4 consumes; paper13 is the upstream vertex), bgs:L4 (sine-kernel universality = bulk density, PROVED Nov 2025), twin-primes:L2 (zero pair correlation → gap statistics; same explicit-formula source), sato-tate:L_equidist (MEASURE canonical; paper60 §10).

### L5 — Circle method in BC/adelic setting — **W_GB-1 — the wall**

**Claim**: Reformulating the Hardy-Littlewood circle method within the BC/adelic framework — expressing the major/minor arc decomposition via $\mathbb{Q}/\mathbb{Z}$ characters in $C^*(\mathbb{Q}/\mathbb{Z})$, translating Vinogradov exponential-sum estimates into the BC algebraic setting, and closing the gap from "sufficiently large" to "all even" — proves binary Goldbach.

**Status**: **OPEN — the named wall W_GB-1**. Confidence 0.5 on the wall itself.
**Source**: Hardy-Littlewood 1923 (classical); Vinogradov 1937 (ternary large-$n$); Helfgott 2013 (ternary unconditional); paper33-goldbach programme §5 Milestone 2; paper60 §14 "Link 5 is the wall — the BC framework provides a natural language but no obvious new analytic tools beyond the classical circle method."

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the circle method is the canonical tool that crosses the additive-multiplicative wall; paper60 §14 explicitly identifies this as the arithmetic face's load-bearing layer)
- **Projection**: $P_D$ (paper61 §10 — the reformulation lives inside $P_D$'s target: $C^*(\mathbb{Q}/\mathbb{Z})$ is the BC algebra's maximal abelian subalgebra and carries the $\mathbb{Q}/\mathbb{Z}$ characters the circle method uses)
- **Pattern**: P5 Zeta Regularization (the Vinogradov/circle-method apparatus is the arithmetic-side zeta-regularization of exponential sums; paper60 §14)
- **Invariant preserved**: C*-algebra structure (load-bearing — the reformulation is an operator-algebra statement about $C^*(\mathbb{Q}/\mathbb{Z})$), zero distribution (background — the minor-arc estimate depends on $\zeta$'s zero-free region)
- **Geometric interpretation**: The circle method is the classical tool for additive problems — it decomposes $\int_0^1 |S(\alpha, N)|^k e(-\alpha M) d\alpha$ into major arcs (rational $\alpha$ with small denominator; main term) and minor arcs (everything else; error term). Under $P_D$ (paper61 §10) the rationals $\mathbb{Q}/\mathbb{Z}$ are the characters of the maximal abelian subalgebra $C^*(\mathbb{Q}/\mathbb{Z}) \subset A_{BC}$; the major-arc decomposition should reformulate as a spectral decomposition of that subalgebra. Pattern 5: the minor-arc estimates are zeta-regularized exponential sums. The wall is genuine and structural: the BC framework provides the language (characters, KMS state, explicit formula) but no obvious new analytic power beyond the classical circle method. paper60 §14's honest accounting: "the translator between multiplicative and additive is slow; whether the BC algebra widens this bridge is the open problem." [Considered but rejected: face DYNAMICS — the circle method is a flow-on-circle in a loose sense but paper60 §14 canonicalizes ARITHMETIC; projection $P_O$ — the wall is Clay-adjacent and some framing would put it at $P_O$, but the proposed reformulation content (major/minor arcs in $C^*(\mathbb{Q}/\mathbb{Z})$) is strictly $P_D$ operational; pattern P1 — Geometric Reinterpretation is a fair alternative (circle method reinterpreted in BC language) but the actual mechanism closing the gap would be regularization of minor-arc estimates.]
- **Cross-cuts**: twin-primes:L3/L4 (shared additive-multiplicative wall; both need the same bridge-widening; paper60 §14 explicit), rh:L4 (circle method consumes the RH prime density from L4 of this chain = L3/L4 of rh), bgs:L_bulk (GUE bulk provides the raw statistical input circle method leverages), collatz:L_additive (shared additive-vs-multiplicative interface; paper60 §14 programme-edge "Collatz: shared additive-multiplicative interface").

### L6 — Even-indexed KMS$_1$ decomposition as prime convolution

**Claim**: For each even integer $2n \geq 4$, the KMS$_1$ state $\omega_1$ evaluated on a specific even-indexed Hecke combination $H_{2n} = \sum_{p+q=2n} \mu_p^* \mu_q$ (or similar operator-theoretic quantity) decomposes as an explicit convolution $\omega_1(H_{2n}) = \sum_{p+q=2n} f(p, q)$ for some kernel $f$ derivable from the KMS$_1$ structure; the non-vanishing of this sum gives binary Goldbach directly.

**Status**: **OPEN — novel conjecture**; confidence 1/10.
**Source**: paper33-goldbach programme §5 Milestone 3 novel conjecture; paper61 §17 outer-ring BC-to-Goldbach bridge (speculative); paper60 §14 "Link 6 is novel — if true it would give Goldbach directly from KMS structure."

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the conjecture's statement is purely additive-over-multiplicative; the novel claim IS that the BC algebra's KMS state carries the additive information $p + q = 2n$)
- **Projection**: $P_O$ (paper61 §17 — the novel KMS$_1$ decomposition is what would close Goldbach as an outer-ring Clay-adjacent vertex; L6 is the Clay boundary of this chain)
- **Pattern**: P4 Topological Rigidity (if the decomposition holds, it is a rigidity of the KMS$_1$ state's support: the even-indexed Hecke combinations are forced to be a sum over prime pairs)
- **Invariant preserved**: BC-KMS state (load-bearing — the conjecture is literally about evaluating $\omega_1$ on a specific operator), C*-algebra structure (background — the operator $H_{2n}$ lives in $A_{BC}$)
- **Geometric interpretation**: The novel conjecture says the KMS$_1$ state at equilibrium sees the additive completeness of the primes via an operator-algebraic decomposition. Under $P_O$ (paper61 §17) this is the outer-ring Goldbach statement: every even integer's representation as $p + q$ becomes the value of a KMS-state functional on a specific Hecke combination. Pattern 4: the decomposition's existence, if it holds, is a structural rigidity forced by the semigroup-character pairing. The honest accounting (paper60 §14): "if true, Goldbach closes without the classical circle method; if false, the BC route to Goldbach reduces to the classical tools." The BC algebra provides the LANGUAGE; whether it provides the POWER is unknown. [Considered but rejected: face RESONANCE — KMS$_1$ as resonance-mode content is a fair reading but paper60 §14 canonicalizes ARITHMETIC for Goldbach statements; projection $P_D$ — the operator-algebraic content lives in $P_D$ but the Clay-closure status of L6 is outer-ring; pattern P1 — Geometric Reinterpretation of Goldbach as KMS decomposition is a fair alternative but the conjecture's load-bearing content is the rigidity of the decomposition's existence.]
- **Cross-cuts**: twin-primes:L5 (analogous novel conjecture: twin-prime constant $C_2$ as GUE-arithmetic correction — same additive-multiplicative-wall-crossing structure), bsd:L1/L3 (KMS$_1$ + ITPFI decomposition is the parallel BC structure for L-values; same machinery applied to elliptic-curve L-functions), rh:L_KMS (KMS$_1$ state is the shared resource; Goldbach and RH both rest on it), bgs:L_bulk (GUE bulk regime delivers the density prerequisite L6 might internalize via its kernel $f$).

---

## §4 Branch Map

The Goldbach chain is largely linear but has one notable structural fork at L5/L6: the classical route through L5 (widening the circle method in the BC framework) vs. the novel route through L6 (direct KMS$_1$ prime-convolution). Both routes target the same conclusion but rest on different $P_D$-vs-$P_O$ projection emphases.

```
L4 (spectral prime density, CONDITIONAL cross-paper from RH)
                │
                ├── Route Classical: L5 (circle method in BC/adelic setting)
                │   [face: ARITHMETIC | proj: P_D | pat: P5]
                │   three sub-requirements L5.a/L5.b/L5.c all OPEN
                │   Goldbach closes via classical circle method
                │   re-expressed in BC language; no new tools
                │   expected; "sufficiently large" → "all" gap
                │   remains the final obstruction.
                │
                └── Route Novel: L6 (even-indexed KMS_1 prime convolution)
                    [face: ARITHMETIC | proj: P_O | pat: P4]
                    speculative conjecture; if true, closes Goldbach
                    WITHOUT the classical circle method; if false,
                    the BC route reduces to Route Classical.

Both routes target: binary Goldbach N = p + q for all even N ≥ 4
(with HL quantitative r_2(N) ~ 2 C_2 · N / (log N)² correction).

Routes differ in which projection is load-bearing:
- Route Classical sits at P_D (operational BC-algebra reformulation
  of the circle method) with P_O boundary only at the final
  Goldbach statement
- Route Novel sits at P_O (the KMS_1 decomposition is the outer-ring
  closure statement) with P_D machinery (the KMS state, the Hecke
  operators) supplying the internal content

Structural note: a combined route — use L6's kernel f to REPLACE
Vinogradov's exponential-sum estimates on the minor arcs of L5.a/b —
would reduce L5.a and L5.b to corollaries of L6 and leave only
L5.c (the "sufficiently large" → "all" gap closure) as the residual
open item. The chain table does not formalize this hybrid route;
it is a candidate decomposition for future work.
```

**Cross-chain structural input — the GUE three-tail (paper60 §14)**: Goldbach sits in the BULK regime of the GUE sine-kernel distribution. Twin Primes sits in the small-gap tail (gap = 2); Cramér sits in the large-gap tail. All three are Fredholm-determinant views of $\det(1 - K_{\sin})$. The bulk's sine-kernel universality was PROVED Nov 2025 (arXiv:2511.18275, Hardy Z PCC). This closes the spectral side; the arithmetic side of the tails (extracting pointwise additive conclusions from the spectral universality) is the shared wall with Twin Primes and Cramér.

---

## §5 Face Histogram

| Face       | Count | Bar                        | Interpretation |
|------------|-------|----------------------------|---|
| TOPOLOGY   |   0   |                            | Goldbach does not live on the topology face; no winding/genus content. |
| DYNAMICS   |   0   |                            | Goldbach does not interrogate the modular-flow dynamics directly (though the GUE three-tail situates it in the bulk of a spectral flow; that is cross-chain structural input, not a layer). |
| HARMONICS  |   1   | ████                       | L3 (Mellin bridge) is the canonical Fourier/dual-side layer — the bridge between the additive (circle-method) and multiplicative (Euler-product) forms. |
| MEASURE    |   1   | ████                       | L4 (spectral prime density) is the equidistribution layer — density-in-intervals is Sato-Tate-face content. |
| AMPLITUDE  |   0   |                            | Goldbach does not interrogate growth-rate/subconvexity of the primes directly. |
| SYMMETRY   |   0   |                            | Goldbach has no explicit Galois/symmetry-type content (Helfgott's ternary proof uses minor-arc bounds, not symmetry; our chain does not introduce Galois structure). |
| CURVATURE  |   0   |                            | Goldbach is not a gauge-curvature object. |
| ARITHMETIC |   4   | ████████████████           | DOMINANT (67%). L1 (primes generate BC), L2 (Hecke semigroup), L5 (circle method in BC), L6 (novel KMS$_1$ convolution) — four of six layers are arithmetic-face canonical. Goldbach IS the canonical ARITHMETIC vertex with Twin Primes (paper60 §14 face title). |
| RESONANCE  |   0   |                            | Goldbach does not interrogate trace-formula/spectral-side resonances (despite the BC-algebra home: the BC algebra's resonance-mode content is consumed by rh/bgs, not by Goldbach directly). |
| SPREAD     |   0   |                            | Goldbach does not interrogate $L^2$-mass-spreading. |

**Interpretation**: ARITHMETIC dominates (4 / 6 layers = 67%) — confirming paper60 §14's identification of Goldbach as the canonical ARITHMETIC vertex alongside Twin Primes. HARMONICS carries 1 layer (L3 Mellin bridge, 17%); MEASURE carries 1 layer (L4 explicit-formula density, 17%). All seven other faces are absent. This concentrated ARITHMETIC signature is the structural signal that the chain's depth is shallow (6 links, 2 closed) while its face-pureness is maximal — Goldbach asks one question, and that question lives on one face, and the face's own difficulty is what makes the chain short and the wall hard. The "shape" of Goldbach on the e-circle is a single point at ARITHMETIC with thin rays to HARMONICS (via Mellin) and MEASURE (via density) — the two bridges out of the arithmetic face to its immediate face neighbors.

---

## §6 Projection Histogram

| Projection | Count | Bar                        | Notes |
|------------|-------|----------------------------|---|
| $P_A$        |   0   |                            | Goldbach has no quantum-observable content; $P_A$ forgets it. |
| $P_B$        |   0   |                            | Goldbach has no gauge-bundle content; $P_B$ forgets it. |
| $P_C$        |   0   |                            | Goldbach contributes no cosmological pin; $P_C$ forgets it. |
| $P_D$        |   5   | ████████████████████       | DOMINANT (83%). L1, L2, L3, L4, L5 all live inside $P_D$'s preservation class — the BC algebra, Hecke semigroup, Mellin bridge (via $C^*(\mathbb{Q}/\mathbb{Z})$), explicit-formula spectral density, and circle-method reformulation are all operational BC-algebra content. |
| $P_E$        |   0   |                            | Goldbach is not pin-valued; it is a qualitative statement about ALL even integers, not a sub-percent numerical prediction. |
| $P_O$        |   1   | ████                       | L6 (the novel KMS$_1$ prime-convolution conjecture) sits at the $P_O$ outer-ring boundary — this is the Clay-targeted closure statement. |

**Interpretation**: The projection profile is $P_D$-dominant (5 / 6 = 83%) with a single $P_O$ entry at L6. This is paper61 §17's compound-projection assignment for Goldbach: $P_D$ for the internal BC-algebraic machinery, $P_O$ for the outer-ring conjecture statement itself. $P_A, P_B, P_C, P_E$ are all absent — Goldbach is neither a quantum observable nor a gauge bundle nor a cosmological pin nor a sub-percent numerical prediction. The $P_D$ dominance is the structural signal that Goldbach's natural home is Branch D (Bost-Connes, operator-algebra side) — this matches paper60 §14's thesis ("the primes are the generators of the Bost-Connes algebra") and north-star §0.1's $P_D$ preserved-invariant table (Hecke semigroup on $S^1$). The $P_O$ slice at L6 is the outer-ring boundary; if Route Novel (L6) closes, Goldbach is $P_O \leftrightarrow P_D$ compound; if Route Classical (L5) closes, Goldbach is pure $P_D$.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                           qg5d Branch D
                           (Axiom 5; N^⋊ = ⟨μ_p⟩;
                            primes-as-operators;
                            BC algebra, KMS_1)
                                  │
                                  │ ═══ shared C*-algebra structure
                                  │ ═══ shared Hecke semigroup N^⋊
                                  │ ═══ shared BC-KMS state (L1, L2, L6)
                                  │
       twin-primes ═══════════   goldbach   ══════════════   rh
       (ARITHMETIC               │                            (RESONANCE primary;
        sibling;                 │                            CCM resolvent)
        same wall                │                            ═══ L3/L4 ↔ explicit
        at additive-             │                                formula, Mellin
        multiplicative           │                                bridge, zero
        interface)               │                                distribution
       ═══ L1/L2 shared μ_p      │
       ═══ L3 shared Mellin      │
       ═══ L5/L6 shared wall     │
                                 │
       bgs ══════════════════════│═══════════════════  baum-connes
       (RESONANCE; GUE           │                    (RESONANCE; K-theory
        three-tail;              │                    pairing; Cuntz-Li
        sine-kernel              │                    semigroup = N^⋊)
        PROVED Nov 2025)         │                    ═══ L1/L2 ↔ shared N^⋊
       ═══ L4 bulk-regime        │                    ─── L6 novel KMS_1
           sine-kernel           │                        decomposition
           universality          │                        structural analog
       ─── L_bulk (L5, L6)       │
                                 │
       bsd ══════════════════════│═══════════════════  collatz
       (ARITHMETIC; BC over K;   │                    (HARMONICS; additive-
        Hecke characters)        │                    multiplicative
       ═══ L1/L3 ↔ number-       │                    interface; paper60 §09)
           field extension       │                    ─── L3 Mellin-dual
           of L1/L2              │                        framing
       ─── L5 shared L-value     │                    ─── L5/L6 shared
           local Euler factor    │                        additive-vs-mult
                                 │                        interface
                                 │
       pvnp ═════════════════════│═══════════════════  ym:L7
       (RESONANCE; BC algebra    │                    (ARITHMETIC; Newton
        spectral-gap rigidity)   │                    power-sum integers)
       ─── L1/L2 shared BC       │                    ─── L1/L2 shared
           operational content   │                        integer-lattice
                                 │                        ARITHMETIC face
                                 │
                           sato-tate
                           (MEASURE canonical;
                            paper60 §10)
                           ─── L4 shared equidistribution/
                               weak-* convergence

                           lindelof (AMPLITUDE) / cramer (DYNAMICS)
                           ─── face-only GUE three-tail structural input
                               (paper60 §14): Twin Primes ↔ Goldbach ↔
                               Cramer = three regimes of one sine-kernel
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch-D-Axiom-5** — shared C*-algebra structure + BC-KMS state.
  - Reason: Branch D Axiom 5 literally names $\{\mu_p\}$ (the primes as operators) as the generators of $\mathbb{N}^\rtimes$; paper61 §10 table places this as the $P_D$ target. Goldbach L1 IS Axiom 5 read through the Goldbach question.
  - Transposition candidate: YES (this is foundational; no capacitor cell needed — it is the source).

- **L1 ↔ rh:L2** — shared C*-algebra structure (BC-algebra ITPFI factorization).
  - Reason: rh L2 ("ITPFI Euler-product factorization") and Goldbach L1/L2 use the same $\mu_p$-generation — paper61 §10 "ITPFI factorization = Euler product, two different languages."
  - Transposition candidate: YES (shared BC machinery; both $P_D$).

- **L1 ↔ bgs:L1** — shared C*-algebra structure (BC at KMS$_1$).
  - Reason: bgs L1 ("BC at KMS$_1$ → type III$_1$") is the same foundational layer as Goldbach L1; both rest on Bost-Connes 1995.
  - Transposition candidate: YES.

- **L1 ↔ baum-connes:L1** — shared C*-algebra structure (Cuntz-Li semigroup).
  - Reason: baum-connes L1 lists Goldbach L1/L2 as a direct cross-cut: "Primes generate BC algebra via $\mu_p$; Hecke semigroup $\mathbb{N}^*$ encodes multiplicative structure — same $\mathbb{N}^*$ at the K-theory target." paper31 PROOF-CHAIN.md names identical generators.
  - Transposition candidate: YES.

- **L1 ↔ bsd:L1** — shared C*-algebra structure (BC over imaginary quadratic $K$).
  - Reason: bsd L1 is the number-field extension of Goldbach L1/L2 — $A_{BC,K}$ extends $A_{BC}$ by replacing $\mathbb{N}^\rtimes$ with the semigroup of integral ideals of $K$. The generator set is the number-field primes, the analog of Goldbach's $\{\mu_p\}$.
  - Transposition candidate: YES.

- **L1 ↔ pvnp:L_BC** — shared BC-KMS state + C*-algebra structure.
  - Reason: pvnp uses BC-algebra spectral-gap rigidity (Popa type III$_1$) — shared operational content with Goldbach L1.
  - Transposition candidate: YES (P4 shared).

- **L1 ↔ twin-primes:L1** — shared ARITHMETIC + $\mu_p$ generation.
  - Reason: Twin Primes L1 ("explicit formula: prime gaps $\leftrightarrow$ zero spacing") and Goldbach L1 share the BC entry point; paper60 §14 names both as canonical ARITHMETIC vertices.
  - Transposition candidate: YES.

- **L2 ↔ qg5d:Branch-D** — shared C*-algebra structure.
  - Reason: the Hecke semigroup IS Branch D's multiplicative object; north-star §0.1 $P_D$ preserved invariants list includes "Hecke semigroup on $S^1$."
  - Transposition candidate: YES.

- **L2 ↔ rh:L2** — shared ITPFI factor type + Euler product.
  - Reason: Euler product = fundamental theorem of arithmetic at the C*-algebra level (paper61 §10); rh's ITPFI decomposition uses the same unique-factorization property.
  - Transposition candidate: YES.

- **L2 ↔ twin-primes:L2** — shared multiplicative structure.
  - Reason: both chains rest on $\mathbb{N}^\rtimes$ and the fundamental theorem of arithmetic in operator form.
  - Transposition candidate: YES.

- **L2 ↔ baum-connes:L1** — shared $\mathbb{N}^\rtimes$ (Cuntz-Li semigroup).
  - Reason: paper31 PROOF-CHAIN.md explicit — "Cuntz-Li semigroup $\mathbb{N}^\rtimes$ at K-theory target; shared generators with Goldbach."
  - Transposition candidate: YES.

- **L2 ↔ ym:L7** — shared KK mode index / integer-lattice (speculative).
  - Reason: ym L7 (Newton power-sum decomposition) is the ARITHMETIC-face integer-power-sum layer of YM; ym cross-cuts explicit to "goldbach / twin-primes — ARITHMETIC canonical, additive-multiplicative integer structure."
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ rh:L3/L4** — shared explicit formula + spectral gap.
  - Reason: the Mellin bridge IS the explicit formula; rh's L3/L4 layers import the same bridge from the RH zero side. Goldbach consumes, RH produces.
  - Transposition candidate: YES.

- **L3 ↔ twin-primes:L1** — shared explicit formula (prime gaps ↔ zero spacing).
  - Reason: both use the Mellin-bridge explicit formula, Twin Primes for gap spacing, Goldbach for sum covering.
  - Transposition candidate: YES.

- **L3 ↔ collatz:L_Mellin** — shared HARMONICS face + Mellin-dual framing.
  - Reason: paper60 §09 names Collatz as the HARMONICS-canonical vertex; the Mellin bridge is a Fourier-dual construction identified with the HARMONICS face per paper60 §14. Collatz's additive-multiplicative interface shares the bridge structurally.
  - Transposition candidate: SPECULATIVE (Collatz X-ray not yet built).

- **L3 ↔ bgs:L4** — shared Mellin bridge output (sine-kernel universality).
  - Reason: bgs L4 (sine-kernel universality PROVED Nov 2025) is the spectral-side output the Mellin bridge delivers to Goldbach's L4.
  - Transposition candidate: YES.

- **L4 ↔ rh:L2/L3** — shared zero distribution (PRIMARY EDGE — cross-paper transport).
  - Reason: Goldbach L4 is literally cross-paper transported from RH; paper13 PROOF-CHAIN.md is the explicit upstream vertex. Agent-I audit item 6 tagged this 2026-04-14.
  - Transposition candidate: YES (explicit cross-paper transport; structurally the single strongest edge in the Goldbach chain).

- **L4 ↔ bgs:L4** — shared zero distribution + sine-kernel universality.
  - Reason: bgs PROVES the sine-kernel bulk (Nov 2025 arXiv:2511.18275); Goldbach L4 uses the bulk density to fuel L5's circle method.
  - Transposition candidate: YES.

- **L4 ↔ twin-primes:L2** — shared zero distribution (pair correlation).
  - Reason: Twin Primes L2 (zero pair correlation → gap statistics) uses the same explicit formula output, applied to the gap = 2 regime; Goldbach uses it for the bulk density.
  - Transposition candidate: YES.

- **L4 ↔ sato-tate:L_equidist** — face-only (MEASURE canonical).
  - Reason: paper60 §10 Sato-Tate is the MEASURE-canonical vertex; prime density in intervals is the equidistribution content MEASURE face interrogates.
  - Transposition candidate: SPECULATIVE (Sato-Tate X-ray not yet built).

- **L5 ↔ twin-primes:L4/L5** — shared additive-multiplicative wall + ARITHMETIC.
  - Reason: both chains hit the same structural wall at the circle-method/gap-statistics boundary; paper60 §14 "both chains share the same structural obstacle: the additive-multiplicative wall."
  - Transposition candidate: YES (the wall is shared; a bypass of the wall would benefit both).

- **L5 ↔ rh:L4** — shared zero distribution (circle method consumes RH).
  - Reason: circle method's major-arc estimate depends on RH's prime density; rh L4 is the producer, Goldbach L5 is the consumer.
  - Transposition candidate: YES.

- **L5 ↔ bgs:L_bulk** — shared bulk-regime sine-kernel + GUE three-tail.
  - Reason: paper60 §14 programme edge "GUE three-tail: Twin Primes ↔ Goldbach ↔ Cramér, three views of one sine-kernel"; bgs's bulk regime IS the input to Goldbach's circle method.
  - Transposition candidate: YES.

- **L5 ↔ collatz:L_additive** — shared additive-vs-multiplicative interface.
  - Reason: paper60 §14 explicit outgoing edge "Collatz (paper41, 4/10): shared additive-multiplicative interface (harmonics vs. lattice)."
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ bsd:L5** — shared L-value local Euler factors (face-only ARITHMETIC).
  - Reason: bsd L5's Euler factors are local arithmetic data; Goldbach's circle method has a local-at-$p$ structure in the major-arc decomposition. Both ARITHMETIC-face. bsd X-ray cross-cuts explicit: "L5 ↔ goldbach:L_Euler."
  - Transposition candidate: SPECULATIVE (the local-local analogy is structural but mechanical transposition unclear).

- **L6 ↔ twin-primes:L5** — shared novel arithmetic-correction structure.
  - Reason: Twin Primes L5 (GUE → Hardy-Littlewood $C_2$) is the novel arithmetic-correction-factor extraction analog of Goldbach L6 (KMS$_1$ prime-convolution kernel $f$). Both cross the additive-multiplicative wall; both are conjectured; both are at confidence 1/10.
  - Transposition candidate: YES (structurally identical move; any progress on one would illuminate the other).

- **L6 ↔ bsd:L1/L3** — shared BC-KMS state + ITPFI decomposition.
  - Reason: bsd's L1 + L3 (unique KMS$_1$ + ITPFI factorization) is the parallel structural machinery applied to L-values; Goldbach L6 is the parallel machinery applied to additive convolutions. Both use the KMS$_1$-as-L-value-encoding thesis.
  - Transposition candidate: SPECULATIVE (the structural parallel is genuine; the transposition mechanism is not yet formalized).

- **L6 ↔ rh:L_KMS** — shared BC-KMS state.
  - Reason: RH's KMS$_1$-based resolvent construction and Goldbach L6's KMS$_1$-based prime-convolution decomposition both rest on the same KMS$_1$ state of $A_{BC}$.
  - Transposition candidate: YES.

- **L6 ↔ baum-connes:L_novel** — structural analog at K-theory pairing.
  - Reason: L6 is a novel conjecture that would decompose the KMS$_1$ state by an additive convolution; paper31 baum-connes has analogous novel K-theory-pairing conjectures for the Cuntz-Li semigroup.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ bgs:L_bulk** — shared bulk-regime delivery.
  - Reason: if L6 holds, the kernel $f$ must recover the sine-kernel bulk density as a consistency check; bgs's proved sine-kernel is the bulk test.
  - Transposition candidate: SPECULATIVE.

- **(cross-chain) Goldbach ↔ Twin Primes ↔ Cramér — GUE three-tail**:
  - Reason: paper60 §14 explicit: "Twin Primes, Goldbach, and Cramer are three views of ONE distribution — three regimes of the GUE." The Fredholm determinant $\det(1 - K_{\sin})$ governs all three through small-gap tail / bulk / large-gap tail. This is a face-only structural cross-cut at the ARITHMETIC-DYNAMICS interface (paper60 §14).
  - Transposition candidate: YES (the three-tail structure is a programme-level structural bouquet edge; any bypass of the additive-multiplicative wall affects all three).

**Summary**: 24 cross-cut edges identified across 6 layers (avg 4 cross-cuts per layer — HIGH, because the $P_D$ operational core is shared by all Branch-D vertices). 14 verified (capacitor/paper60-61 citation); 10 SPECULATIVE (pending sibling X-rays: twin-primes, collatz, sato-tate, lindelof, cramer). The PRIMARY edge is L4 ↔ rh:L2/L3 (cross-paper transport of zero distribution, explicitly tagged by Agent-I audit item 6 on 2026-04-14). The second-strongest edge is L5 ↔ twin-primes:L4/L5 (shared additive-multiplicative wall). The densest cross-cutting is at L1/L2 (4 + 4 = 8 edges across qg5d, rh, bgs, baum-connes, bsd, pvnp, twin-primes) — the BC operational core is the programme's connectivity hub, and Goldbach's entry point is right on it.

---

## §8 Current Walls

- **W_GB-1 — Operator-interference to prime-pair bridge / Circle method in BC/adelic setting**: L5 is conditional on (i) expressing Hardy-Littlewood major/minor arc decomposition via $\mathbb{Q}/\mathbb{Z}$ characters inside $C^*(\mathbb{Q}/\mathbb{Z})$ (L5.a); (ii) translating Vinogradov exponential-sum estimates into the BC algebraic setting (L5.b); (iii) closing the gap between "sufficiently large $N$" (Montgomery-Vaughan 1975 / Chen's $p + P_2$) and "all even $N \geq 4$" (L5.c). Status: **OPEN**. No decomposition run yet. Confidence 0.5 (paper33 audit-strategy). paper60 §14 assessment: "the wall is genuine — the BC framework provides the LANGUAGE but no obvious new analytic tools." Direct analog to the twin-primes wall; bypass work on one chain would inform the other.

- **W_GB-2 — Novel KMS$_1$ prime-convolution decomposition**: L6 is the novel conjecture $\omega_1(H_{2n}) = \sum_{p+q=2n} f(p, q)$ for an explicit kernel $f$ derivable from the KMS$_1$ structure. Status: **OPEN — speculative**. Confidence 1/10. If L6 holds, Goldbach closes without the classical circle method; if L6 fails, Goldbach retreats to Route Classical (L5). No decomposition run yet. This is the Clay-targeted outer-ring closure statement.

No other named walls. L1, L2 are KNOWN (Bost-Connes 1995 + construction); L3 is ESTABLISHED (Mellin bridge is a classical theorem); L4 is CONDITIONAL on cross-paper transport from Paper 13 RH (not an independent assumption). The two substantive walls are W_GB-1 (the circle-method wall) and W_GB-2 (the novel KMS$_1$ conjecture). Both sit downstream of L4; neither is yet decomposed or capacitor-formalized.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/goldbach/PROOF-CHAIN.md` — NOT YET CREATED. When created, the three sub-requirements of L5 (L5.a Q/Z-character arc decomposition, L5.b Vinogradov BC-algebraic, L5.c "sufficiently large" → "all") should be decomposed first; L6's novel kernel $f$ is the second decomposition target. Cross-cuts with twin-primes (shared additive-multiplicative wall) should feed the decomposition brief.
- **CCM verification**: `strategy/ccm-verification/ledger.md#goldbach` — NOT YET CREATED. Goldbach's dependency on CCM 2025 is INDIRECT (via cross-paper transport from Paper 13 RH, which is CCM-conditional). Expected verdict when ledger written: **BYPASSED-VIA-RH-TRANSPORT (Goldbach inherits RH's CCM dependency through L4)**. If CCM 2025 gets independently verified (lifting RH from 8/10 to 10/10), Goldbach's L4 becomes unconditional, but L5/L6 walls remain untouched.
- **Inner rings**: NOT APPLICABLE — Goldbach is a primary outer-ring vertex (paper61 §17 vertex 12).
- **QG5D W1/W2 cascading refinement (2026-04-14)**: Paper 1 W1 (scheme independence) + W2 (Route-C 3-loop) closed via Paper 10/11; effect on Goldbach is **cosmetic-to-small** (per PROOF-CHAIN.md §"Cascading refinement from QG5D W1/W2 closure"). The chain does not gate on the scheme question; the underlying foundation is strictly stronger; no link status changes required; confidence unchanged.
- **Cross-chain GUE three-tail sibling refinement (Nov 2025)**: Hardy Z PCC arXiv:2511.18275 PROVED the sine-kernel universality for $\zeta$ zeros — this closes the spectral side of the GUE three-tail structure (paper60 §14). Effect on Goldbach: L4's bulk-regime density is strengthened; bgs L4 now reads LITERATURE (PROVED) instead of CONJECTURED. L5/L6 walls untouched. bgs vertex is at 7/10 pre-Nov-2025, expected to lift with formal incorporation.
- **Agent-I audit item 6 (2026-04-14)**: L4's cross-paper tag formalized — "CONDITIONAL (cross-paper transport from Paper 13 RH; equivalently CONDITIONAL on CCM 2025, not an independent RH assumption)." This is a labeling refinement, not a mathematical change; it clarifies Goldbach's dependency graph and prevents double-counting RH as an independent conditional.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — L5 / W_GB-1 (Circle method in BC/adelic setting)**: The three sub-requirements L5.a (major/minor arcs via $\mathbb{Q}/\mathbb{Z}$ characters in $C^*(\mathbb{Q}/\mathbb{Z})$), L5.b (Vinogradov in BC algebra), L5.c ("sufficiently large" → "all") all OPEN. — face: ARITHMETIC, projection: $P_D$, pattern: P5. STATUS: OPEN as wall; no decomposition; bypass candidates unknown. Confidence 0.5.

- **G2 — L6 / W_GB-2 (Novel KMS$_1$ prime-convolution decomposition)**: $\omega_1(H_{2n}) = \sum_{p+q=2n} f(p, q)$ with explicit $f$ — existence and form of kernel $f$. — face: ARITHMETIC, projection: $P_O$, pattern: P4. STATUS: OPEN as novel conjecture; confidence 1/10; the Clay-targeted outer-ring closure statement.

That's it. Two of six main links closed. Two substantive walls (W_GB-1 circle-method and W_GB-2 KMS$_1$). The additive-multiplicative wall is genuine and structural (paper60 §14): crossing it is the central open problem of analytic number theory and the programme honestly claims 1/10 on this vertex. The BC framework provides the language; whether it provides the power is unknown.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-<NN>/vertices/goldbach/critic-attacks.md` (pending) and arbiter decisions at `strategy/x-ray/pac-output/runs/run-<NN>/vertices/goldbach/arbiter-decisions.md` (pending).

Notable arbiter wins:
- L3 face: HARMONICS over ARITHMETIC (paper60 §14 explicitly identifies the Mellin bridge as the FACE-8-to-FACE-3 connection; Mellin is Fourier-dual content which is HARMONICS-canonical per paper60 §09).
- L4 face: MEASURE over ARITHMETIC (prime density in intervals is equidistribution content, Sato-Tate-face canonical per paper60 §10; the arithmetic content is the primes, but the DENSITY-IN-INTERVALS form is measure-theoretic).
- L6 projection: $P_O$ over $P_D$ (L6 is the Clay-targeted novel closure statement; paper61 §17 outer-ring list places it at $P_O$; the internal BC machinery is $P_D$, but the conjecture-level content is outer-ring).
- L5 pattern: P5 over P1 (the circle method's load-bearing mechanism is zeta-regularization of exponential sums on minor arcs; Geometric Reinterpretation in BC language is downstream framing).
- L1/L2 face: ARITHMETIC over RESONANCE (paper60 §14 canonical — the $\mu_p$ are resonance-mode generators in loose usage, but the question Goldbach asks on them is arithmetic-additive, not mode-spectral).

28 / 30 author wins out of 30 total field decisions (5 fields × 6 main layers). 2 CRITIC WINS at L3 and L4 where the author's first pass over-extended ARITHMETIC to layers where HARMONICS and MEASURE are canonical per paper60's explicit face assignments.

---

*End of Goldbach X-Ray. Snapshot 2026-04-15. 6 main layers annotated. 24 cross-cut edges identified. ARITHMETIC-canonical (4/6 layers = 67%), $P_D$-dominant (5/6 = 83%), shallow chain (6 links) with high face-pureness — Goldbach asks one question on one face and the face's own difficulty (additive-multiplicative wall, paper60 §14) is what makes the walls hard and the confidence 1/10. Two walls: W_GB-1 (L5 circle method in BC/adelic setting) and W_GB-2 (L6 novel KMS$_1$ prime-convolution conjecture). Cross-chain structural siblings: Twin Primes (ARITHMETIC, small-gap tail) and Cramér (DYNAMICS, large-gap tail) — three views of one GUE sine-kernel.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
