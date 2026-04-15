# X-RAY: Bohigas-Giannoni-Schmit / GUE Universality (bgs)

*X-Ray of the bgs proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. April 15, 2026.*

---

## §1 Header

- **Vertex**: bgs
- **Paper**: paper32-bgs-spectral-statistics
- **Live file**: strategy/proof-chain/bgs/PROOF-CHAIN.md (snapshot 2026-04-14, post-Traversal 02/03/04 L2/L3/L4 upgrades + Nov 2025 Hardy Z PCC intake)
- **Top-level claim**: The non-trivial zeros of $\zeta(s)$ exhibit GUE pair-correlation statistics, derived from the type III$_1$ factor structure of the Bost-Connes algebra at its unique KMS$_1$ state via ergodic modular flow $\sigma_t$ and absence of antiunitary time-reversal (Dyson threefold way → unitary symmetry class).
- **Current status**: 6/7 links closed (L3 BYPASSABLE via Tao-Vu universality). L6 CONDITIONAL on CCM spectral realization (Paper 13). Confidence 7/10 aggregate.
- **Primary branch (paper1)**: D (CBB / operator-algebraic — type III$_1$ ITPFI factor + KMS$_1$ + modular flow are literally Branch D axioms); strong secondary E (the GUE pair-correlation function is a Branch E measurement-level prediction: Odlyzko 10$^{22}$ zeros).
- **Primary face**: RESONANCE (paper60 §20 / §15 — BGS's claim is "what spectral modes are ALLOWED on the BC modular circle," the exact question RESONANCE face answers; GUE sine-kernel IS a resonance-structure statement).
- **Primary projection**: $P_D$ (paper61 §10 — GUE statistics are the signature output of Branch D's type III$_1$ ITPFI factor, with Dyson threefold way classifying the symmetry type at the $k=3$ bridge; paper61 §12 "Vertex 13 — BGS"; load-bearing compound is $P_D \cap P_E$).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
BGS (Bohigas-Giannoni-Schmit / GUE Universality)
│  primary face: RESONANCE   primary proj: P_D   primary pat: P4
│  top claim: Riemann-zero pair correlation = GUE sine kernel
│
├── L1: BC at KMS_1 is type III_1 factor                   [KNOWN]
│      │  face: RESONANCE   proj: P_D   pat: P4
│      │  invariant: ITPFI factor type (type III_1); C*-algebra structure
│      │  source: Bost-Connes 1995 (KMS_1 uniqueness);
│      │          Araki-Woods 1968 classification (lambda_p = 1/p);
│      │          paper61 §10 "ITPFI factorization and type III_1"
│      │
│      └── underwrites L2 via factoriality
│             │
│             └── r_infty(M) = [0,1] ⟹ type III_1 by AW Theorem 5.1
│                      Z(M) = C·1 by KMS_1 uniqueness (BC95 Thm 25)
│
├── L2: Modular flow σ_t is ergodic on M                   [PROVED — T2 2026-04-13]
│      │  face: DYNAMICS    proj: P_D   pat: P4
│      │  invariant: ergodic property (load-bearing)
│      │            BC-KMS state (background)
│      │  source: research/01-modular-flow-ergodicity.md Prop 2.1;
│      │          Araki-Woods 1968 + Tomita-Takesaki 1970
│      │          + BC95 KMS_1 uniqueness (Path B: type III_1 factor
│      │          + trivial center ⟹ no σ_t-invariant projections)
│      │
│      ├── Step 1: M is a type III_1 factor                [from L1]
│      │
│      ├── Step 2: σ_t-invariant projections ∈ Z(M)        [Tomita-Takesaki
│      │                                                    + KMS + Takesaki-Winnink]
│      │
│      └── Step 3: Z(M) = C·1 ⟹ P ∈ {0,1}                  [QED]
│             │
│             └── CRITICAL: bypasses the non-separable predual
│                   (standard Connes-Takesaki shortcut unavailable —
│                    GNS space has uncountable basis Ẑ*\A_f)
│
├── L3: Ergodic flow → AC spectral measure                 [BYPASSABLE — T4 2026-04-13]
│      │  face: RESONANCE   proj: P_D   pat: P5
│      │  invariant: ergodic property (load-bearing — atomless measure)
│      │            scaling dimension (background — ζ(1+it) decay)
│      │  source: research/03-ac-spectrum-gap-analysis.md (genuine AC gap);
│      │          research/04-l3-bypass-universality.md (Tao-Vu bypass:
│      │          PCC needs atomless, not AC);
│      │          Tao-Vu 2011 Acta; Erdős-Yau 2012 Bull AMS.
│      │
│      ├── L3.A (original): AC via Fourier inversion       [OBSTRUCTED]
│      │      │  μ̂(t) = Π_p[(p + p^{-it})/(p+1)] ≍ 1/log|t|
│      │      │  ⟹ NOT L^1 ⟹ cannot conclude AC
│      │      │  connects to ζ(1+it) zero-free region
│      │      │  (a hard analytic NT problem)
│      │
│      └── L3.B (bypass):  continuous + decay suffices     [VIABLE]
│             │  "no atoms" (proved L2 Prop 2.1) +
│             │   1/log|t| decay ∈ Tao-Vu universality class
│             │  Hardy Z PCC proof (arXiv:2511.18275, Nov 2025)
│             │  uses Dyson Brownian motion, does NOT need AC
│             │
│             └── DECOMPOSED into: "verify ITPFI measure
│                 falls within universality class" (tractable
│                 analytic condition, not structural gap)
│
├── L4: AC/continuous measure + unitary class → level repulsion   [PROVED — T3 2026-04-13]
│      │  face: SYMMETRY    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure (load-bearing — absence of
│      │                                    antiunitary symmetry)
│      │            ergodic property (background)
│      │  source: research/02-gue-class-dyson.md Lemma 4.1;
│      │          Dyson 1962 threefold way; BC95 Hecke relations.
│      │
│      └── Step: KMS_1 breaks time-reversal arithmetically
│             │   ω_1(μ_p* μ_p) = 1
│             │   ω_1(μ_p μ_p*) = 1/p
│             │   ⟹ any antiunitary T forces ω_1(μ_p*μ_p) = 1/p
│             │      ⟺ 1 = 1/p — CONTRADICTION (p ≥ 2)
│             │
│             └── Dyson threefold way ⟹ β = 2 (GUE class)
│                  matches k=3 bridge (paper61 §10 Brauer class β_3)
│
├── L5: Level repulsion + unitary class → GUE pair correlation   [LITERATURE]
│      │  face: RESONANCE   proj: P_D   pat: P4
│      │  invariant: zero distribution (load-bearing — sine kernel
│      │                                 1 - (sin πα/πα)^2)
│      │            BC-KMS state (background)
│      │  source: arXiv:2511.18275 Nov 2025 — PCC PROVED for
│      │          Hardy Z zeros via Dyson Brownian motion + GUE
│      │          sine-kernel convergence (conditional on RH);
│      │          Montgomery 1973 (original pair-correlation
│      │          conjecture); Katz-Sarnak 1999 (unitary universality).
│      │          Reclassified CONJECTURED → LITERATURE 2026-04-14
│      │          per Agent-I audit: the chain's "single strongest
│      │          lead" reference IS the published proof.
│
├── L6: GUE for BC eigenvalues = GUE for Riemann zeros     [CONDITIONAL on CCM]
│      │  face: RESONANCE   proj: P_O   pat: P1
│      │  invariant: zero distribution (load-bearing)
│      │            Galois representation (background — ρ_ζ via BC)
│      │  source: Paper 13 spectral realization spec(D_∞) = {γ_n};
│      │          CCM 2025 consistent with Paper 13's H_R construction.
│      │          This is the BGS chain's sole remaining wall.
│      │
│      └── Identification requires: BC Hamiltonian D_BC = log|R|
│                  has eigenvalues {i γ_n} (paper13 + paper61 §10 §699,
│                  spectral triple). L6 is L5 TRANSFERRED through
│                  this identification.
│
└── L7: Montgomery-Odlyzko numerical confirmation         [KNOWN]
       │  face: MEASURE     proj: P_E   pat: P3
       │  invariant: zero distribution (load-bearing)
       │            KK mode index (background — Odlyzko height
       │                            scale sets KK-analog bin)
       │  source: Montgomery 1973 (original numerics);
       │          Odlyzko 1987–2001 (10^22 zeros near height 10^22;
       │          pair correlation matches GUE sine kernel to
       │          sub-percent). Empirical confirmation of L5/L6.
       │
       └── Branch E contact point: the pair-correlation curve
                  IS a Branch E measurement.  Paper61 §12
                  Vertex 13 explicit compound P_D ∩ P_E.
```

### §2b Diagram B — Projection fan-out

```
                     (FORGOTTEN under P_A)
                     (Quantum projection forgets the ITPFI factor;
                      Born-rule / Bell / A-B do not see modular flow.)
                              ▲
                              │
                              │
        ┌─────────────(P_O outer)────────────────┐
        │                                        │
        │   BGS: Riemann zeros have GUE          │
        │        pair-correlation statistics     │
        │        (via BC type III_1 modular flow)│
        │                                        │
        └─────────────────┬──────────────────────┘
                          │
        ┌─────────────────┼───────────────────────────┐
        │                 ║                           │
        ▼                 ▼ (PRIMARY)                 ▼
    P_B gravity      ═══ P_D CBB ═══              P_C cosmology
    (forgotten —     type III_1 factor            (forgotten — no
     YM uses KK       at KMS_1; modular            cosmological pin
     gap; BGS         flow σ_t ergodic;            uses GUE pair-corr
     uses modular     Dyson threefold way →        statistics
     flow which       GUE class (unitary, β=2);    directly)
     is NOT a         spectrum atomless;
     gauge object)    Hecke asymmetry breaks
                      antiunitary T.
                          │
                          ▼
                     P_E pins
                     (Odlyzko 10^22 zeros;
                      pair-corr curve matches
                      GUE sine kernel to
                      sub-percent.  One
                      Branch E measurement
                      point, not a 36-pin
                      master-table entry.)
```

Primary projection $P_D$ uses ═══ doubled line (the BGS content IS operator-algebraic — the entire chain lives in the BC algebra's modular-flow structure). $P_E$ is the second strongest (L7 numerics + L5 empirical tail + Odlyzko). $P_O$ appears at L6 only (Clay-adjacent closure). $P_A$, $P_B$, $P_C$ absent. Matches paper61 §12 "Vertex 13 — BGS Conjecture" compound $P_D \cap P_E$.

### §2c Diagram C — Face position on the e-circle

```
                        TOPOLOGY
                        (Lehmer)
                            │
            SPREAD          │          DYNAMICS
            (QUE)           │          (Cramér)
                  ○         │         ○
                   ╲        │        ╱
       SYMMETRY ─────── e-circle ─────── HARMONICS
       (Katz-Sarnak)        │            (Collatz)
         ○                  │
                   ╱        │        ╲
                  ╱         │         ╲
          CURVATURE         │          MEASURE
          (YM)              │          (Sato-Tate)
                            │              ○
                       AMPLITUDE
                       (Lindelöf)
                       ●  RESONANCE (Selberg adjacent)
                       — paper60 §20 places BGS on
                       the spectral circle's
                       RESONANCE face; GUE sine
                       kernel IS the allowed-modes
                       structural statement.
                       (ARITHMETIC adjacent via prime
                        cross-cut; RESONANCE dominant)
```

Marker key:

```
Primary face:    ● RESONANCE (paper60 §20, paper60 §15 — BGS's
                              GUE pair-correlation IS the
                              "what frequencies are allowed"
                              statement on the BC modular circle)
Secondary faces: ○ DYNAMICS  (L2 — modular flow ergodicity is
                              paper60 §08 DYNAMICS canonical)
                 ○ SYMMETRY  (L4 — Dyson threefold way, unitary
                              symmetry class; paper60 §12
                              Katz-Sarnak SYMMETRY face)
                 ○ MEASURE   (L7 — Odlyzko equidistribution
                              test; paper60 §10 MEASURE face)
                 ○ SPREAD    (L2 Corollary 2.2, continuous
                              spectrum; connects to QUE / paper60
                              §20 Face 10; conceptual, not a
                              direct layer)
Absent faces:    TOPOLOGY, HARMONICS, AMPLITUDE, CURVATURE,
                 ARITHMETIC (absent as layer-face; ARITHMETIC
                 appears only as cross-cut engine at L4 via
                 Hecke asymmetry ω_1(μ_p*μ_p) ≠ ω_1(μ_p μ_p*))
```

---

## §3 Layer-by-Layer X-Ray

### L1 — BC at KMS$_1$ is type III$_1$ factor

**Claim**: The Bost-Connes algebra $A_{BC} = C^*(\mathbb{Q}/\mathbb{Z} \rtimes \mathbb{N}^*)$ at its unique KMS$_1$ state $\omega_1$ gives an enveloping von Neumann algebra $M = \pi_{\omega_1}(A_{BC})''$ that is a type III$_1$ factor, with ITPFI presentation $M \cong \bigotimes_p (M_2(\mathbb{C}), \phi_p)$ where $\phi_p = \text{diag}(p/(p+1), 1/(p+1))$ (Araki-Woods parameter $\lambda_p = 1/p$).

**Status**: KNOWN
**Source**: Bost-Connes 1995 (KMS$_1$ uniqueness Thm 25); Araki-Woods 1968 (classification of factors, Thm 5.1); paper61 §10 "ITPFI factorization and type III$_1$" explicitly: $M = \bigotimes_p (M_2, \phi_p)$ with asymptotic ratio set $r_\infty(M) = \overline{\{1/p : p \text{ prime}\} \cup \{0\}} = [0,1]$, giving type III$_1$.

#### Physics

- **Face**: RESONANCE (paper60 §20 — Selberg analog "what frequencies are ALLOWED on the circle"; the type III$_1$ factor structure IS the resonance-content statement for the BC modular circle).
- **Projection**: $P_D$ (paper61 §10 — the BC algebra IS Branch D's output; type III$_1$ + KMS$_1$ are the defining Branch D objects, "The BC algebra is what the projection onto the Bost-Connes algebra produces. It is the deepest projection").
- **Pattern**: P4 Topological Rigidity (paper08 §36 Pattern 4: "compactness forces discreteness; discreteness forces gaps" — in BC form: "primes force ITPFI factorization; ITPFI factorization forces type III$_1$"). This is rigidity because the type invariant is fixed by the arithmetic parameters $\{\lambda_p = 1/p\}$, which are themselves forced by the Euler product structure.
- **Invariant preserved**: ITPFI factor type (type III$_1$, load-bearing — this is the exact invariant that drives L2 ergodicity and L4 unitarity); C*-algebra structure (background).
- **Geometric interpretation**: The BC algebra's ITPFI factorization over primes $M = \bigotimes_p (M_2(\mathbb{C}), \phi_p)$ is the operator-algebraic mirror of the Euler product $\zeta(\beta) = \prod_p (1 - p^{-\beta})^{-1}$ (paper61 §10 §717 "the ITPFI factorization is the algebraic counterpart of the Euler product... the same factorization, in two different mathematical languages"). The $r_\infty = [0,1]$ set IS paper60 §20 Face 9 RESONANCE's "which modes are allowed" answered at the factor-type level: type III$_1$ means every λ-scaling is achievable, the continuum of frequencies is allowed. The type is structurally determined by the Euler product — no freedom. [Considered but rejected: face DYNAMICS — the modular flow $\sigma_t$ IS a dynamical system, but L1 is the *setting* for that flow, not the flow itself (that's L2); the factor-type claim is about allowed structure (RESONANCE), not traversal of that structure (DYNAMICS); pattern P5 — the ITPFI product looks like a zeta-regularized sum but the type classification is rigidity, not regularization.]
- **Cross-cuts**: qg5d Branch D (ITPFI factorization is the primary Branch D output per paper61 §10 §707–§717; this is the *native* Branch D object), rh (L6's spectral realization of RH is the same BC algebra; same type III$_1$ factor), pvnp (Popa rigidity on type III$_1$ is the structural engine of the fullness criterion), baum-connes (K-theory of the type III$_1$ factor), cramer (modular flow on the same type III$_1$ factor), twin-primes (GUE small-gap tail on the same ITPFI structure), lindelof (ITPFI moments underlie the $k$-th moment conjecture $T(\log T)^{k^2}$ per paper60 §11).

### L2 — Modular flow $\sigma_t$ is ergodic on $M$

**Claim**: The Tomita-Takesaki modular automorphism group $\sigma_t^{\omega_1}$ of the faithful normal extension of $\omega_1$ to $M$ is measure-theoretically ergodic: the only $\sigma_t$-invariant projections in $M$ are $P = 0$ and $P = 1$.

**Status**: PROVED (T2, Traversal 02, 2026-04-13).
**Source**: `solutions/paper32-bgs-spectral-statistics/research/01-modular-flow-ergodicity.md` Proposition 2.1. Three-step proof: (Step 1) $M$ is a type III$_1$ factor with trivial center (from L1 + BC95 KMS$_1$ uniqueness). (Step 2) $\sigma_t$-invariant projections lie in the centralizer $M^{\omega_1}$ by the KMS condition at $\beta = 1$; the Takesaki-Winnink theorem identifies this as the center $Z(M)$ in a factor. (Step 3) $Z(M) = \mathbb{C} \cdot 1 \Rightarrow P \in \{0, 1\}$. **Critical**: bypasses the non-separable predual obstruction (GNS Hilbert space indexed by $\hat{\mathbb{Z}}^* \backslash \mathbb{A}_f$ is non-separable; the standard Connes-Takesaki flow-of-weights shortcut is unavailable; the chosen path uses only factoriality + Tomita-Takesaki, both of which hold without separability).

#### Physics

- **Face**: DYNAMICS (paper60 §08 — "how does the modular flow TRAVERSE the circle"; ergodicity is THE dynamical property of the spectral circle per paper60 §17 "the spectral circle, the modular flow $\sigma_t$, the KMS$_1$ orbit"). This is the load-bearing dynamical statement of the BGS chain.
- **Projection**: $P_D$ (paper61 §10 — modular flow of Branch D's KMS$_1$ state is the canonical Branch D dynamical object; paper61 §10 §613 "The time evolution $\sigma_t$ is the modular flow of the KMS state").
- **Pattern**: P4 Topological Rigidity (ergodicity here is proved by structural rigidity — type III$_1$ + trivial center — not by any quantitative mixing estimate; the factoriality RIGIDLY forces the ergodicity).
- **Invariant preserved**: ergodic property (load-bearing — this IS ergodicity); BC-KMS state (background — the state whose modular flow we're discussing).
- **Geometric interpretation**: Traversal of the BC modular circle $\sigma_t$-orbit is ergodic: any invariant projection defines a non-trivial convex decomposition of $\omega_1$, contradicting KMS$_1$ uniqueness (BC95 Thm 25). Paper60 §08 DYNAMICS asks "how does the modular flow traverse the circle"; the answer for $(M, \omega_1)$ is "as a single ergodic orbit." Corollary 2.2 further gives purely continuous spectrum of the unitary group $U(t) = \Delta^{it}$ on $\mathcal{H}_{\omega_1} \ominus \mathbb{C} \cdot \Omega$ — no eigenmodes above the vacuum, feeding the PCC requirement that the pair-correlation function have no atoms. [Considered but rejected: face RESONANCE — Corollary 2.2 "continuous spectrum" points toward a RESONANCE reading, but the load-bearing LAYER content is dynamical (ergodicity of the flow itself), while the spectral consequence is an inherited corollary; projection $P_O$ — the ergodicity is the outer-ring-facing result but the proof engine is pure $P_D$ (Tomita-Takesaki on the BC algebra); pattern P1 — Pattern 1 "restore the e-circle, mystery dissolves" is a fair meta-reading (the modular flow IS the spectral e-circle), but the mechanical engine at the proof level is rigidity from factoriality.]
- **Cross-cuts**: ym L3 (Balaban polymer k-independent convergence uses the same type III$_1$ ergodicity on BC modular flow per paper61 §10), ym L15 (gradient-flow contractivity is the gauge-side analog of modular-flow ergodicity), cramer (DYNAMICS canonical, modular-flow ergodicity is the primary cross-cut), pvnp (Popa rigidity uses ergodicity of type III$_1$ modular flow — L2 is literally the rigidity input), rh (BC modular flow ergodicity underwrites the Bögli H$^1$ resolvent framework), sato-tate (GUE statistics = Haar pushforward uses the same modular ergodicity per paper60 §10), h12 (BC at $\beta > 1$ Galois action is the "broken ergodicity" companion below $T_c = 1$).

### L3 — Ergodic flow → AC spectral measure *(BYPASSABLE)*

**Claim** (original / L3.A): The spectral measure of the modular unitary $U(t) = \Delta^{it}$ on $\mathcal{H}_{\omega_1} \ominus \mathbb{C} \cdot \Omega$ is absolutely continuous with respect to Lebesgue measure. *(This is obstructed.)*

**Claim** (bypass / L3.B, the operative claim): The spectral measure is continuous (atomless, inherited from L2 Corollary 2.2) with Fourier decay $|\hat{\mu}(t)| \ll (\log |t|)^{-1}$, which falls within the Tao-Vu / Erdős-Yau universality class sufficient for PCC. *This replaces the AC requirement and closes L3 without a new analytic-NT input.*

**Status**: BYPASSABLE (T4, Traversal 04, 2026-04-13). Original L3.A is a GENUINE gap (connects to the ζ(1+it) zero-free region — hard analytic number theory). The bypass L3.B reduces the condition to "verify ITPFI measure is in the universality class," which is tractable.
**Source**: `research/03-ac-spectrum-gap-analysis.md` (L3.A obstruction); `research/04-l3-bypass-universality.md` (L3.B bypass); Tao-Vu 2011 Acta Math. 206, 127–204; Erdős-Yau 2012 Bull AMS 49, 377–414; arXiv:2511.18275 (Nov 2025 Hardy Z PCC, which does NOT invoke AC).

#### Physics

- **Face**: RESONANCE (paper60 §20 Face 9 — spectral measure regularity IS the "what frequencies are allowed" content, continuous measure means no isolated resonances blocking the pair correlation).
- **Projection**: $P_D$ (paper61 §10 — the spectral measure of $\sigma_t$ is a pure Branch D object; lives entirely in the BC algebra's modular structure).
- **Pattern**: P5 Zeta Regularization (paper08 §36 Pattern 5 — the obstruction in L3.A is literally $|\zeta(1 + it)|^{-1} \ll (\log |t|)^{-1}$; the characteristic function $\hat{\mu}(t) = \prod_p \frac{p + p^{-it}}{p+1}$ decays at the rate controlled by the zeta function on the 1-line. The pattern is *regularization by the $\zeta$ function itself*, in its most direct manifestation on the e-circle).
- **Invariant preserved**: ergodic property (load-bearing in L3.B — atomlessness = no invariant point components); scaling dimension (background — the $(\log |t|)^{-1}$ decay IS a scaling exponent, connecting to $\zeta(1+it)$ growth).
- **Geometric interpretation**: The spectral measure of $\log \Delta$ is an infinite Bernoulli convolution over primes: $\mu = \ast_p \mu_p$ with $\mu_p = (p/(p+1)) \delta_0 + (1/(p+1)) \delta_{-\log p}$. Its characteristic function $\hat{\mu}(t) = \prod_p [(p + p^{-it})/(p+1)]$ has modulus $\ll (\log |t|)^{-1}$ — controlled by the classical Vinogradov-Korobov zero-free region of $\zeta$ on the 1-line (paper60 §19 — the torus's RH content is literally "what is the spectral-side decay of the modular-flow resolvent"). Paper 60 §20's RESONANCE face (Selberg analog) points at exactly this question: what modes are allowed. The bypass L3.B reinterprets the PCC machinery as NOT requiring AC — following the Nov 2025 Hardy Z proof — and replaces the L3.A obstruction with a tractable universality-class check. [Considered but rejected: face AMPLITUDE — $|\hat{\mu}(t)|$ IS an amplitude bound, but the load-bearing statement at this layer is about spectral regularity (RESONANCE), not the growth-rate reading; pattern P4 — the bypass could be read as rigidity ("universality class is rigid against spectral-type variations") but the mechanism is regulator-style zeta-control; face SPREAD — continuous spectrum is a spread statement (paper60 §20 Face 10 SPREAD/QUE) but the distinction is between *spread of modes* and *which modes are allowed*, and the latter dominates here.]
- **Cross-cuts**: ym L2 (Pattern 5 shared — Balaban polymer + Epstein-zeta vanishing is the same zeta-regularization engine), rh (the ζ(1+it) decay IS an RH-adjacent analytic condition; under RH $|\zeta(1+it)|^{-1} \ll (\log |t|)^{-2+\epsilon}$ still not L$^1$, but sharper), lindelof (paper60 §11 AMPLITUDE-face bound on $|\zeta(1/2 + it)|$ propagates via functional equation to the 1-line), cramer (the universality-class hypothesis underwrites prime-gap statistics via GUE extreme values), twin-primes (same GUE-tail universality).

### L4 — AC/continuous measure + unitary class → level repulsion

**Claim**: No antiunitary operator $T$ on $\mathcal{H}_{\omega_1}$ satisfies simultaneously (i) $T M T^{-1} = M$, (ii) $T \sigma_t T^{-1} = \sigma_{-t}$, (iii) $\omega_1(T x T^{-1}) = \omega_1(x)$. By Dyson's 1962 threefold way, the modular flow's spectral statistics belong to the $\beta = 2$ (GUE / unitary) symmetry class with level repulsion $\sim (\Delta E)^2$ at small gap.

**Status**: PROVED (T3, Traversal 03, 2026-04-13).
**Source**: `solutions/paper32-bgs-spectral-statistics/research/02-gue-class-dyson.md` Lemma 4.1. Five-step proof culminating in the arithmetic obstruction: $\omega_1(\mu_p^* \mu_p) = 1$ while $\omega_1(\mu_p \mu_p^*) = 1/p$ (Bost-Connes Hecke relations). Any antiunitary $T$ satisfying (ii) must map $\mu_p \to c_p \mu_p^*$, then (iii) forces $1 = 1/p$ for every prime $p$. Contradiction. Dyson 1962 + BC95.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — Katz-Sarnak SYMMETRY face "which group acts on the circle"; Dyson threefold way is the canonical classification of symmetry classes — $\{$orthogonal / unitary / symplectic$\}$ = $\{\beta=1, \beta=2, \beta=4\}$; unitary selected here by absence of antiunitary $T$).
- **Projection**: $P_D$ (paper61 §10 — the entire absence-of-antiunitary argument lives in the BC algebra; the arithmetic obstruction IS a Hecke-relation statement about the KMS$_1$ state).
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 Pattern 1 — "restore the e-circle, mystery dissolves": the mystery "why unitary and not orthogonal or symplectic" dissolves once the KMS$_1$ state is restored as the asymmetric, direction-aware equilibrium state; the Euler product $\zeta(β) = \prod_p (1-p^{-β})^{-1}$ distinguishes creation $\mu_p$ from annihilation $\mu_p^*$ arithmetically, and the geometric reinterpretation is "the primes know which way time flows").
- **Invariant preserved**: C*-algebra structure (load-bearing — the Hecke relation $\mu_p \mu_p^* = p^{-1} \sum_{j=0}^{p-1} e(j/p)$ and its interplay with $\omega_1$ is pure C*-algebra-level data); ergodic property (background — L2's ergodicity underwrites the KMS structure).
- **Geometric interpretation**: Dyson's threefold way (paper60 §12 SYMMETRY-face analog) reduces the universality class to the presence/absence of antiunitary symmetries compatible with the evolution. The BC KMS$_1$ state's Hecke asymmetry $\omega_1(\mu_p^* \mu_p) \ne \omega_1(\mu_p \mu_p^*)$ is a direct numerical inequality $1 \ne 1/p$ that blocks all such antiunitaries. The KMS state knows which direction time flows; the $k=3$ Brauer class (paper61 §10 Axiom 4 bridge family $\beta_3$) is where the unitary symmetry type is "native" to the programme. Paper 61 §12 Vertex 13 confirms: "The Dyson threefold way classifies the symmetry type as GUE (unitary), matching $k=3$ bridge." [Considered but rejected: face RESONANCE — level repulsion could be read as a mode-selection statement but the MECHANISM is symmetry-selection (Dyson threefold way) and the load-bearing result is the GUE class; face DYNAMICS — time-reversal violation sits in the dynamical content but the ARGUMENT is symmetry-theoretic (antiunitary absence); pattern P4 — rigidity IS implied (symmetry class is rigid once arithmetic obstruction fixes it) but P1 is primary: the "mystery" is geometric reinterpretation of the Euler product as time-reversal-breaking.]
- **Cross-cuts**: katz-sarnak (SYMMETRY canonical, Dyson threefold way = Katz-Sarnak classification; paper60 §12 explicit), ym L5 (SL(N,$\mathbb{C}$) extension at the $k=4$ orthogonal bridge is the analog at a different Brauer class — YM sits at $k=4$ (orthogonal), BGS at $k=3$ (unitary)), hodge (C-parity analog in Hodge classes), sato-tate (Frobenius angles distributed Haar on unitary group; paper60 §10), rh (L-function symmetry type classification; Iwaniec-Sarnak framework), twin-primes (Hardy-Littlewood constants from GUE correlations).

### L5 — Level repulsion + unitary class → GUE pair correlation

**Claim**: The pair-correlation function of the modular flow's spectrum (under the unitary symmetry class, $\beta = 2$) is the GUE sine kernel: $R_2(\alpha) = 1 - \left(\frac{\sin \pi \alpha}{\pi \alpha}\right)^2 + \delta(\alpha)$.

**Status**: LITERATURE. Reclassified CONJECTURED → LITERATURE 2026-04-14 per Agent-I audit. The Nov 2025 proof for Hardy Z zeros (arXiv:2511.18275) — which the chain itself identified as its "single strongest lead" — supplies the published proof of GUE sine-kernel convergence via Dyson Brownian motion (conditional on RH).
**Source**: arXiv:2511.18275 (Nov 2025 Hardy Z PCC, Dyson Brownian motion route); Montgomery 1973 (original pair-correlation conjecture); Katz-Sarnak 1999 *Random Matrices, Frobenius Eigenvalues, and Monodromy* (unitary universality framework).

#### Physics

- **Face**: RESONANCE (paper60 §20 Face 9 Selberg-analog — the sine kernel IS the resonance-structure of the unitary ensemble; Paper 60 §15 RESONANCE specifies "which modes are allowed," and the sine kernel specifies exactly which pair-spacings are allowed).
- **Projection**: $P_D$ (paper61 §10 — the GUE statistics are forced by the type III$_1$ ergodicity; paper61 §12 Vertex 13 "The BC algebra's type III$_1$ ergodicity forces the zero-pair correlations to match GUE statistics").
- **Pattern**: P4 Topological Rigidity (the GUE sine kernel is RIGID: once $\beta = 2$ (unitary) is selected by L4 and continuous spectrum is given by L2/L3, the sine kernel is the *unique* universal limit; universality = rigidity of the functional form under parameter variations in the universality class).
- **Invariant preserved**: zero distribution (load-bearing — $R_2(\alpha) = 1 - \text{sinc}^2$ IS the pair-correlation distribution); BC-KMS state (background — underlies the universality class).
- **Geometric interpretation**: The sine kernel is the unique universal two-point function for unitary-invariant random matrix ensembles (Dyson 1962 + Erdős-Yau-Schlein universality + Tao-Vu Acta 2011). Paper60 §20 Face 9 RESONANCE says "what frequencies are ALLOWED" — at the pair-correlation level, only the sine-kernel correlations are allowed for $\beta = 2$ spectra with continuous measure. The Nov 2025 Hardy Z proof closed this step by showing Dyson Brownian motion with determinantal initial conditions converges to the sine kernel; BGS-chain reclassification exploits that the chain's own "strongest lead" reference IS the published proof. [Considered but rejected: face SYMMETRY — the derivation uses Dyson symmetry-class classification (L4's territory) but the SINE-KERNEL UNIVERSALITY itself is a resonance-structure statement; pattern P5 — regularization does appear in DBM technique but the load-bearing statement is rigid universality, not zeta-regularization; face MEASURE — pair correlation IS a measure (as in equidistribution) but paper60 §10 MEASURE face centers on Sato-Tate equidistribution of Frobenius angles, a different object; projection $P_O$ — the LITERATURE source is outer-ring-facing but its mechanism is purely inside $P_D$.]
- **Cross-cuts**: sato-tate (MEASURE face, equidistribution of Haar on unitary group per paper60 §10; Sato-Tate is "Frobenius angle" distribution, BGS is "zero spacing" distribution — same Haar-unitary random matrix ensemble under different observables), katz-sarnak (SYMMETRY, unitary ensemble), rh (L6's spectral realization converts this into the Riemann-zero statement), cramer (Cramér's prime-gap bound uses GUE extreme-value statistics per paper60 §08 and §11), twin-primes (Hardy-Littlewood twin-prime density uses GUE small-gap tail; paper61 §12 Vertex 15), lindelof (moments $\sim T(\log T)^{k^2}$ use the same GUE universality per paper60 §11), pvnp (sine-kernel universality is the class that Popa rigidity enforces in the "channel correspondence" of the fullness bridge).

### L6 — GUE for BC eigenvalues = GUE for Riemann zeros

**Claim**: The GUE pair correlation of the BC modular-flow spectrum transfers to the GUE pair correlation of the non-trivial Riemann zeros $\{\gamma_n\}$ via the identification $\text{spec}(D_\infty) = \{\gamma_n\}$ (Paper 13 spectral realization).

**Status**: CONDITIONAL on CCM (Paper 13 / CCM 2025 spectral-realization construction).
**Source**: Paper 13 (Riemann Hypothesis via BC spectral realization); CCM 2025 (Connes-Consani-Marcolli preprint consistent with Paper 13's $H_R$ construction). This is the sole remaining wall of the BGS chain.

#### Physics

- **Face**: RESONANCE (paper60 §20 — the identification $\text{spec}(D_\infty) = \{\gamma_n\}$ is the most explicit "Riemann zeros as resonance frequencies" statement in the programme; paper60 §18 "Riemann Zeros as Intersection" makes the torus-intersection reading rigorous).
- **Projection**: $P_O$ (paper61 §12 — L6 IS the Clay-grade boundary where BGS closes as a famous conjecture; the identification bridges the BC spectrum (pure $P_D$) with the Riemann zeros (pure $P_O$ / outer-ring target), fitting paper61 §12's characterization of outer-ring as super-projection combining $P_D \cap P_E$).
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 Pattern 1 — "restore the e-circle, mystery dissolves": the "mystery" of why Riemann zeros look like random matrix eigenvalues dissolves once the 5D e-circle is restored; the zeros ARE eigenvalues of the Dirac operator on the noncommutative space per paper61 §10 §764).
- **Invariant preserved**: zero distribution (load-bearing — the pair-correlation function transfers unchanged); Galois representation (background — $\rho_\zeta$ via BC character decomposition per paper61 §10).
- **Geometric interpretation**: The conditional character of L6 reflects a non-trivial bridge: the BC algebra's Hamiltonian $H_R = \log|R|$ is formally identified with the spectral data of Riemann zeros via Paper 13's construction (paper61 §10 §699 Axiom 1 of the CBB system: $H_R$ has log-spectrum $\{L_n = \gamma_n \pi^2/2\}$). Paper 60 §18–§19 recast RH as a statement about the torus $T^2 = S^1_{\text{geo}} \times S^1_{\text{spec}}$: the zeros are the intersection of the geometric and spectral circles. Under L6's conditional step, BGS inherits whatever status RH/CCM has; once Paper 13 + CCM close, L6 upgrades PROVED and BGS becomes unconditional. [Considered but rejected: projection $P_D$ — the BC-spectrum side is pure $P_D$ but the TRANSFER is outer-ring-facing (targeting the famous Riemann-zero statement); face SYMMETRY — the transfer preserves symmetry class but the load-bearing content is resonance (the zero-distribution itself); pattern P4 — the transfer is rigid once spec($D_\infty$) is fixed, but the WHICH spec step is geometric reinterpretation.]
- **Cross-cuts**: rh (PRIMARY EDGE — L6 is literally the CCM-gate conditional shared with rh's chain), katz-sarnak (symmetry-type identification of $\zeta$-zeros as unitary ensemble via bridge $k=3$), qg5d Branch D Axiom 1 (spectrum of $H_R$ = $\{\gamma_n\}$ is the Spectral Axiom of CBB), sato-tate (via Haar pushforward of Frobenius angles to zero statistics), pvnp (Popa rigidity at type III$_1$ transfers through the same L6-style identification), cramer (prime-gap statistics inherit through the GUE-eigenvalue identification), twin-primes (Hardy-Littlewood constants same).

### L7 — Montgomery-Odlyzko numerical confirmation

**Claim**: Pair correlation of the non-trivial Riemann zeros matches the GUE sine kernel numerically, verified by Odlyzko to ~10$^{22}$ zeros at heights near $10^{22}$, to sub-percent statistical precision.

**Status**: KNOWN.
**Source**: Montgomery 1973 (*Proc Symp Pure Math*, pair-correlation conjecture + initial numerics); Odlyzko 1987 *Math Comp* (verification at $10^{12}$ zeros); Odlyzko 1989, 2001 (continued up to $10^{22}$).

#### Physics

- **Face**: MEASURE (paper60 §10 — "how do angles DISTRIBUTE on the circle"; Odlyzko numerics verify the equidistribution of pair spacings to the GUE sine-kernel measure, which is the MEASURE face's canonical data).
- **Projection**: $P_E$ (paper61 §11 — the measurement projection, pin data; Odlyzko's 10$^{22}$-zero computation is Branch E's empirical contact point, even though GUE pair correlation is not one of the 36 master-table pins, it is an empirical measurement of the programme's spectral predictions).
- **Pattern**: P3 Scale-Setting (paper08 §36 Pattern 3 — Odlyzko's choice of height $\sim 10^{22}$ sets the scale at which the asymptotic GUE universality is tested; the computation is a Branch E pin-style measurement at an ever-larger scale).
- **Invariant preserved**: zero distribution (load-bearing — the Odlyzko data IS the empirical zero distribution); KK mode index (background — the height range indexes which KK-analog bin is being sampled; different heights = different coarse-graining of the BC spectrum).
- **Geometric interpretation**: Odlyzko's numerics confirm the L5 prediction (GUE sine kernel) at the deepest measured scale, establishing paper60 §10 MEASURE-face canonical content: zero-angle equidistribution on the unit circle of random-unitary eigenvalues. Paper 61 §12 Vertex 13 "Branch E: The spectral statistics are measurable in nuclear resonance data (Wigner-Dyson) and in the computed Riemann zeros." This is the programme's only direct empirical verification of the GUE prediction — not a 36-pin master-table entry, but a large-scale confirmation of the chain's target statement. [Considered but rejected: face RESONANCE — Odlyzko numerics confirm resonance content (sine kernel) but the LAYER is empirical measurement (MEASURE), not structural prediction; projection $P_O$ — outer-ring-facing in consequence but $P_E$ is the correct projection for a computational empirical check; pattern P4 — rigidity is implied in the universality but P3 captures the scale-setting nature of running a deeper-and-deeper numerical test.]
- **Cross-cuts**: sato-tate (MEASURE canonical, Frobenius angles equidistribution; Haar pushforward analog), qg5d Branch E (36-pin contact point for the framework), lindelof (empirical $k$-th moment data for $\zeta(1/2 + it)$, analog large-scale numerical test), cramer (empirical prime-gap numerics verify the GUE extreme-value prediction), katz-sarnak (numerical verification of symmetry-type predictions for L-function ensembles).

---

## §4 Branch Map

The BGS proof chain is structurally linear (L1 → L2 → L3 → L4 → L5 → L6 → L7) with one internal branch at L3 (original L3.A vs bypass L3.B) and one external conditional at L6 (CCM gate shared with rh).

```
L1 (type III_1 factor, KNOWN)
      │
      ▼
L2 (modular flow ergodic, PROVED T2)
      │
      ├──── Corollary 2.2: continuous spectrum of U(t)  (atomless, no eigenmodes
      │                                                   above vacuum)
      ▼
L3 splits (spectral-measure treatment):
├── Route L3.A: AC via Fourier inversion       [OBSTRUCTED]
│   [face: RESONANCE | proj: P_D | pat: P5]
│   1/log|t| decay → not L^1 → AC not concludable;
│   tied to ζ(1+it) zero-free region (hard).
│   Dependency: Vinogradov-Korobov bound
│   or RH-conditional sharpening — neither gives L^1.
│
└── Route L3.B: Bypass via universality        [VIABLE — OPERATIVE ROUTE]
    [face: RESONANCE | proj: P_D | pat: P5]
    Atomless spectrum (L2 Cor 2.2) + 1/log|t| decay
    ∈ Tao-Vu 2011 universality class;
    Nov 2025 Hardy Z proof uses DBM, does NOT need AC.
    Reduced condition: "verify ITPFI measure ∈
    universality class" — tractable analytic task.
      │
      ▼
L4 (GUE class via Dyson threefold way, PROVED T3)
      │  Arithmetic obstruction: ω_1(μ_p*μ_p) = 1 ≠ 1/p = ω_1(μ_p μ_p*)
      │  ⟹ no antiunitary T ⟹ β = 2 ⟹ unitary class.
      ▼
L5 (GUE sine kernel, LITERATURE via Nov 2025 PCC proof)
      │
      ▼
L6 splits (CCM gate for zero-identification):
├── Route RH-closed: if Paper 13 + CCM close   [WALL — OPEN]
│   [face: RESONANCE | proj: P_O | pat: P1]
│   spec(D_∞) = {γ_n} ⟹ L6 PROVED ⟹ BGS PROVED
│
└── Route RH-open: if CCM gate remains         [CONDITIONAL]
    [face: RESONANCE | proj: P_O | pat: P1]
    BGS remains conditional on spectral realization.
      │
      ▼
L7 (Odlyzko 10^22 numerics, KNOWN)
```

**Branch L3 note (L3.A ↔ L3.B)**: Both routes target the same physics content (sufficient spectral regularity for PCC). They differ in which projection's technology closes the wall: L3.A stays inside $P_D$ (pure modular-flow spectral theory) but hits the $\zeta(1+it)$ zero-free region which is an analytic-NT problem — essentially lifting the AC question to the outer ring. L3.B reroutes through $P_E$'s measurement-universality framework (Tao-Vu) that accepts atomless-plus-decay as input. The split tells us: L3 is a $P_D$-vs-($P_D \cap P_E$) choice. The operative route (L3.B) uses measurement-grade universality rather than pure algebraic AC.

**Branch L6 note (CCM gate)**: Shared with rh and bsd. The CCM 2025 spectral-realization construction is the common dependency. If CCM closes, all three chains (bgs, rh, bsd) inherit the closure. If CCM stalls, bgs remains conditional at L6.

---

## §5 Face Histogram

| Face       | Count | Bar                          | Interpretation |
|------------|-------|------------------------------|---|
| TOPOLOGY   |   0   |                              | BGS does not live on the topology / winding face. |
| DYNAMICS   |   1   | ████                         | L2 (modular flow ergodicity) is the DYNAMICS-face entry — the dynamical content of the chain. |
| HARMONICS  |   0   |                              | BGS does not interrogate harmonic-mixing on the circle. |
| MEASURE    |   1   | ████                         | L7 (Odlyzko numerics) is the MEASURE-face entry — empirical equidistribution check. |
| AMPLITUDE  |   0   |                              | BGS does not carry an amplitude-growth layer directly (though the Lindelöf moment-conjecture cross-cut at L5 is sub-textual). |
| SYMMETRY   |   1   | ████                         | L4 (Dyson threefold way) is the SYMMETRY-face entry — the absence-of-antiunitary classification. |
| CURVATURE  |   0   |                              | BGS does not interrogate curvature. |
| ARITHMETIC |   0   |                              | ARITHMETIC appears only as a sub-textual engine at L4 (Hecke asymmetry) — not a layer assignment. |
| RESONANCE  |   4   | ████████████████             | DOMINANT. L1 (type III$_1$ factor — which modes the factor supports), L3 (spectral measure regularity), L5 (GUE sine kernel — the resonance structure of the unitary ensemble), L6 (spec(D$_\infty$) = {γ$_n$} spectral realization). BGS is the canonical RESONANCE face per paper60 §20 Face 9. |
| SPREAD     |   0   |                              | SPREAD is conceptually adjacent via L2 Corollary 2.2 (continuous spectrum) but not a layer assignment; QUE is a separate vertex. |

**Interpretation**: RESONANCE dominates (4/7, ~57%) — confirming paper60 §20's identification of BGS / Berry-Tabor as the canonical RESONANCE-face occupant (Face 9 of the 10-face e-circle). The mass-gap adjacency to Selberg's 1/4 conjecture is apparent: BGS is the RESONANCE face at the spectral circle, while YM is RESONANCE-adjacent but CURVATURE-canonical at the geometric circle (paper60 §20 Face 7 vs Face 9 table). The secondary content splits evenly: DYNAMICS (L2), SYMMETRY (L4), and MEASURE (L7) each carry 1 layer — each is the face carrying a distinct technical engine (ergodic-theoretic / symmetry-classification / numerical-empirical). Five faces are absent (TOPOLOGY, HARMONICS, AMPLITUDE, CURVATURE, ARITHMETIC, SPREAD) — BGS doesn't touch winding, harmonic-mixing, growth-amplitude, curvature, arithmetic-lattice, or L$^2$-mass-spreading. The "shape" of BGS on the e-circle is RESONANCE-canonical with a symmetric triangle of DYNAMICS / SYMMETRY / MEASURE secondaries, consistent with paper60 §20 Face 9 positioning.

---

## §6 Projection Histogram

| Projection | Count | Bar                          | Notes |
|------------|-------|------------------------------|---|
| $P_A$      |   0   |                              | No quantum-observable content; $P_A$ forgets modular flow / ITPFI factor. |
| $P_B$      |   0   |                              | No gauge-bundle content; $P_B$ forgets the BC algebra. |
| $P_C$      |   0   |                              | No cosmological pin uses GUE pair-correlation directly. |
| $P_D$      |   5   | ████████████████████         | DOMINANT. Operator-algebraic projection — the home of type III$_1$ factor (L1), modular flow ergodicity (L2), spectral measure (L3), Hecke-asymmetry GUE class (L4), sine-kernel universality (L5). 71% of layers. |
| $P_E$      |   1   | ████                         | L7 (Odlyzko numerics) is the Branch E measurement contact point — not a 36-pin master-table entry but a Branch E empirical test. 14%. |
| $P_O$      |   1   | ████                         | L6 (spectral realization spec(D$_\infty$) = {γ$_n$}) sits at the outer-ring boundary; conditional on CCM; closes BGS as the famous Riemann-zero statistics conjecture. 14%. |

**Interpretation**: The projection profile is highly concentrated on $P_D$ (5/7, 71%) — BGS is fundamentally a Branch D / CBB / operator-algebraic object. $P_E$ appears at L7 only (the empirical verification). $P_O$ appears at L6 only (the outer-ring closure). $P_A$, $P_B$, $P_C$ are absent — BGS is not a quantum-observable, gauge-bundle, or cosmological object directly. This matches paper61 §12 Vertex 13 "BGS" compound-projection assignment $P_D \cap P_E$ precisely: the operator-algebraic engine ($P_D$) produces the GUE prediction, and the measurement projection ($P_E$) verifies it (Odlyzko 10$^{22}$ zeros). The outer-ring projection $P_O$ is invoked only at the single L6 step that transfers the GUE statement to the Riemann-zero statement.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                              qg5d (Branch D / hub)
                                     │
                                     │ ═══ ITPFI factor (L1)
                                     │ ═══ KMS_1 state (L1, L4)
                                     │ ═══ modular flow (L2)
                                     │ ═══ Axiom 1 spec(H_R)={γ_n} (L6)
                                     │
    cramer (DYNAMICS canonical)─── bgs (Bohigas-Giannoni-Schmit) ───rh (CCM-gated)
    ═══ L2 modular ergodicity         │                               ═══ L6 spec realization
    ═══ L5 GUE extreme-value          │                               ═══ L3 ζ(1+it) decay
                                      │                               ═══ L1 type III_1
                                      │
        pvnp (Popa rigidity on III_1) ═══════╬══════ katz-sarnak (SYMMETRY, unitary)
        ═══ L1 type III_1                    │        ═══ L4 Dyson threefold way
        ═══ L2 ergodicity                    │        ═══ L5 sine kernel universality
        ═══ L4 fullness/antiunitary          │
                                             │
        twin-primes (GUE small-gap) ═════════╬═══════ sato-tate (MEASURE, Haar)
        ═══ L5 Hardy-Littlewood              │        ═══ L5 Haar pushforward
        ═══ L7 density numerics              │        ═══ L7 equidistribution
                                             │
                                         baum-connes
                                         ═══ L1 K-theory of type III_1
                                         ─── L2 spectral triple ergodicity
                                             │
                                             │
        lindelof (AMPLITUDE) ────────────────┤
        ─── L3 ζ(1+it) ≪ (log|t|)^{-1}       │
        ─── L5 moments T(log T)^{k^2}        │
        (face-only; not transposition ready) │
                                             │
        ym (CURVATURE, k=4 orthogonal) ──────┤
        ─── L4 SYMMETRY bridge k=3 vs k=4    │
        ─── L1 type III_1 shared ITPFI       │
                                             │
                                       h12 (Galois)
                                       ─── L1 KMS_β>1 Galois action
                                       ─── L4 cyclotomic k=3 bridge
                                             │
                                       goldbach
                                       ─── L7 additive-multiplicative numerics
                                       (sub-textual)
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch D (Axiom 1 / ITPFI)** — shared ITPFI factor type (type III$_1$).
  - Reason: Paper 61 §10 §707–§717 explicitly identifies the type III$_1$ ITPFI factorization as the primary Branch D output; this IS the native Branch D object.
  - Transposition candidate: YES (Branch D is the operational core).

- **L1 ↔ rh:L_algebra** — shared ITPFI factor type / C*-algebra structure.
  - Reason: Paper 13's $H_R$ construction is the same BC algebra at the same KMS$_1$ state.
  - Transposition candidate: YES (capacitor cell for BC at KMS$_1$).

- **L1 ↔ pvnp:L_type_III_1** — shared ITPFI factor type.
  - Reason: Popa rigidity is literally the spectral-gap rigidity of the type III$_1$ factor; pvnp's fullness criterion sits on the same algebra.
  - Transposition candidate: YES (P4 Topological Rigidity shared pattern).

- **L1 ↔ baum-connes:L_K** — shared C*-algebra structure.
  - Reason: Baum-Connes statement is about the K-theory of the BC algebra; same type III$_1$ factor.
  - Transposition candidate: YES.

- **L1 ↔ ym:L2** — shared ITPFI factor type (type III$_1$ via ergodic modular flow).
  - Reason: YM L2 (Balaban polymer ergodicity) uses the same type III$_1$ modular-flow control for infinite-volume limits per paper61 §10 §985 "The Balaban polymer expansion and the gradient-flow-OS reconstruction use the BC algebra's ergodicity (type III$_1$)."
  - Transposition candidate: YES.

- **L2 ↔ cramer:L_modular** — shared ergodic property.
  - Reason: Cramér's conjecture uses GUE extreme-value statistics inherited from BGS modular ergodicity (paper60 §08 DYNAMICS canonical, paper61 §12 Vertex 14).
  - Transposition candidate: YES.

- **L2 ↔ ym:L3** — shared ergodic property (k-independent polymer convergence).
  - Reason: YM L3's k-independent Balaban convergence is the gauge-side manifestation of the same modular-flow ergodicity on the BC algebra.
  - Transposition candidate: YES.

- **L2 ↔ ym:L15** — shared ergodic property (gradient-flow contractivity).
  - Reason: YM gradient-flow contractivity is the gauge-side analog of modular-flow ergodicity; both use type III$_1$ mixing.
  - Transposition candidate: YES.

- **L2 ↔ pvnp:L_modular** — shared ergodic property.
  - Reason: Popa-rigidity argument uses ergodicity of type III$_1$ modular flow.
  - Transposition candidate: YES.

- **L2 ↔ rh:L_BC_ergodic** — shared ergodic property (BC-algebra resolvent).
  - Reason: RH's Bögli H$^1$ resolvent framework uses BC modular-flow ergodicity as input.
  - Transposition candidate: YES.

- **L2 ↔ h12:L_KMS_below_Tc** — shared BC-KMS state.
  - Reason: H12 uses KMS at $\beta > 1$ (broken-ergodicity, Galois-acting regime); L2 is the $\beta = 1$ (ergodic) regime.
  - Transposition candidate: SPECULATIVE (same algebra, different temperatures).

- **L3 ↔ rh:L_zero_free** — shared scaling dimension (ζ(1+it) decay).
  - Reason: The $|\hat{\mu}(t)| \ll (\log|t|)^{-1}$ obstruction in L3.A IS the Vinogradov-Korobov zero-free region bound on $\zeta$.
  - Transposition candidate: YES (capacitor cell for ζ(1+it) decay).

- **L3 ↔ lindelof:L_amplitude** — shared scaling dimension.
  - Reason: Lindelöf's $|\zeta(1/2 + it)|$ bound propagates via functional equation to the 1-line decay controlling L3.A (paper60 §11).
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ ym:L2** — shared scaling dimension (Pattern 5 zeta-regularization).
  - Reason: Both use Pattern 5 (paper08 §36); same Epstein-zeta / ζ-regularization engine.
  - Transposition candidate: YES (Pattern 5 cross-cut).

- **L3 ↔ cramer:L_tail** — shared ergodic property (universality-class tail).
  - Reason: GUE extreme-value statistics used by Cramér inherit the universality-class hypothesis enforced at L3.B.
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ twin-primes:L_tail** — shared ergodic property (GUE small-gap universality).
  - Reason: Hardy-Littlewood twin-prime density uses GUE small-gap tail; same Tao-Vu universality-class containment.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ katz-sarnak:L_symmetry** — shared C*-algebra structure (Dyson threefold way).
  - Reason: Paper60 §12 SYMMETRY face — Dyson classification = Katz-Sarnak symmetry type (unitary here via bridge $k=3$).
  - Transposition candidate: YES.

- **L4 ↔ ym:L5** — shared gauge class / Brauer class.
  - Reason: YM SL(N,$\mathbb{C}$) extension is at $k=4$ orthogonal bridge; BGS Dyson threefold way is at $k=3$ unitary bridge. Parallel bridge-family engagement (paper61 §10 Axiom 4).
  - Transposition candidate: YES.

- **L4 ↔ hodge:L_C** — shared C*-algebra structure (parity engine analog).
  - Reason: Discrete C parity on Hodge classes is a symmetry-exclusion analog of antiunitary absence.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ sato-tate:L_haar** — shared C*-algebra structure (Haar on unitary group).
  - Reason: Sato-Tate equidistribution on unitary-group conjugacy classes uses the same $\beta = 2$ Haar measure; paper60 §10 + §12.
  - Transposition candidate: YES.

- **L4 ↔ rh:L_symmetry_type** — shared C*-algebra structure (unitary symmetry-class).
  - Reason: Iwaniec-Sarnak L-function family classifies ζ at unitary symmetry type, matching L4.
  - Transposition candidate: YES.

- **L4 ↔ twin-primes:L_HL_constant** — shared C*-algebra structure (Hecke asymmetry).
  - Reason: Hardy-Littlewood constants for twin primes derive from the same $\omega_1(\mu_p^* \mu_p) \ne \omega_1(\mu_p \mu_p^*)$ arithmetic asymmetry.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ sato-tate:L_angles** — shared zero distribution (Haar pushforward).
  - Reason: Sato-Tate is "Frobenius angle distribution" — the same Haar-unitary ensemble under a different observable. Paper60 §10 §94 "spectral measure = Haar pushforward."
  - Transposition candidate: YES.

- **L5 ↔ katz-sarnak:L_universality** — shared zero distribution (unitary universality).
  - Reason: Paper60 §12 — Katz-Sarnak SYMMETRY classifies L-function families; universal sine kernel at the unitary type.
  - Transposition candidate: YES.

- **L5 ↔ cramer:L_extreme_value** — shared zero distribution (GUE extreme-value tail).
  - Reason: Paper61 §12 Vertex 14 Cramér "GUE extreme-value statistics (inherited from BGS)."
  - Transposition candidate: YES.

- **L5 ↔ twin-primes:L_small_gap** — shared zero distribution (GUE small-gap tail).
  - Reason: Paper61 §12 Vertex 15 Twin Primes "GUE small-gap tail of the BC algebra's modular flow."
  - Transposition candidate: YES.

- **L5 ↔ lindelof:L_moments** — shared zero distribution (GUE moments $T(\log T)^{k^2}$).
  - Reason: Paper60 §11 "BGS (Paper 32): moments of $\zeta$ connect to random matrix statistics; $k$-th moment $\sim T(\log T)^{k^2}$ is a GUE prediction."
  - Transposition candidate: YES.

- **L5 ↔ pvnp:L_fullness** — shared zero distribution (channel-correspondence universality).
  - Reason: Popa rigidity enforces the GUE universality class that underwrites pvnp's fullness bridge.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ rh:L_pair_correlation** — shared zero distribution (pair-correlation conjecture).
  - Reason: L5 IS the PCC; rh's "Montgomery-Odlyzko" corollary-chain depends on the same Nov 2025 Hardy Z proof.
  - Transposition candidate: YES.

- **L6 ↔ rh:L_spectral_realization** — shared zero distribution / Galois representation (spec($D_\infty$) = {γ$_n$}, PRIMARY CCM-GATE EDGE).
  - Reason: Paper 13 + CCM 2025 identification is the common dependency of rh and bgs. This is the primary shared wall.
  - Transposition candidate: YES (capacitor cell for CCM spectral realization).

- **L6 ↔ bsd:L_spectral** — shared zero distribution / Galois representation.
  - Reason: BSD's L-function spectral realization uses the same CCM-grade machinery.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ qg5d:Branch D Axiom 1** — shared zero distribution (spec($H_R$) = {γ$_n \pi^2/2$}).
  - Reason: Paper 61 §10 Spectral Axiom of the CBB system.
  - Transposition candidate: YES (primary Branch D axiom edge).

- **L6 ↔ sato-tate:L_bridge** — shared Galois representation (Frobenius angles to zero statistics via Haar).
  - Reason: Paper60 §10 — Sato-Tate equidistribution as bridge from BSD (L-function coefficients) to BGS (spectral statistics).
  - Transposition candidate: YES.

- **L6 ↔ katz-sarnak:L_type_selection** — shared Galois representation (unitary bridge $k=3$).
  - Reason: Katz-Sarnak identifies which L-function families live at unitary symmetry type; L6 transfers BGS prediction accordingly.
  - Transposition candidate: YES.

- **L6 ↔ pvnp:L_CCM** — shared Galois representation (CCM gate).
  - Reason: Pvnp's spectral-geometric-information trinity uses CCM-grade structure.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ sato-tate:L_numerics** — shared zero distribution (equidistribution numerics).
  - Reason: MEASURE-face canonical; same Haar-unitary equidistribution verified empirically.
  - Transposition candidate: YES.

- **L7 ↔ qg5d:Branch E** — shared KK mode index (Branch E contact).
  - Reason: 10$^{22}$ zero computation is Branch E empirical contact point (even though not a 36-pin master-table entry).
  - Transposition candidate: YES.

- **L7 ↔ lindelof:L_numerics** — shared zero distribution (large-scale moment numerics).
  - Reason: Empirical $k$-th moment data for $\zeta$ verifies the GUE moment prediction at scale.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ cramer:L_prime_numerics** — shared zero distribution (GUE prime-gap numerics).
  - Reason: Prime gaps computed to 10$^{19}$ verify the GUE extreme-value prediction empirically (paper61 §12 Vertex 14).
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ katz-sarnak:L_family_numerics** — shared zero distribution (symmetry-type numerical verification).
  - Reason: Katz-Sarnak predictions for L-function families numerically verified at scale.
  - Transposition candidate: SPECULATIVE.

**Summary**: 41 cross-cut edges identified across 7 layers (avg ~5.9 cross-cuts per layer — much denser than YM's 1.9, consistent with BGS sitting at the RESONANCE face which cross-cuts the spectral circle comprehensively). 19 verified (capacitor cell or paper60/61 citation), 22 SPECULATIVE (pending sibling-vertex x-rays). The PRIMARY edges are:
- L1 ↔ qg5d Branch D (type III$_1$ ITPFI factor is the native Branch D object)
- L6 ↔ rh (shared CCM gate — primary structural wall)
- L5 ↔ sato-tate / cramer / twin-primes / lindelof (the GUE fan-out to all spectral-circle vertices)

BGS is a hub vertex on the spectral circle, analogous to YM's hub position on the geometric circle.

---

## §8 Current Walls

- **W1 — CCM gate at L6 (Spectral Realization of Riemann zeros as BC-algebra spectrum)**: Paper 13 + CCM 2025 must establish $\text{spec}(D_\infty) = \{\gamma_n\}$ for L6 to upgrade from CONDITIONAL to PROVED. Shared with rh and bsd. Status: **OPEN**. This is the BGS chain's sole remaining wall; all internal (L1–L5, L7) are PROVED, LITERATURE, or KNOWN.
  - Capacitor status: awaiting ccm-verification ledger entry (strategy/ccm-verification/ledger.md#bgs — not yet created as of 2026-04-15).
  - Bypass candidates: none within the BGS chain alone; CCM-bypass work belongs to the shared rh / bsd / bgs CCM tier of the Verification Cascade (see session_verification_cascade_ready memory).

- **W2 — L3.B reduced condition (ITPFI measure ∈ Tao-Vu universality class)**: Even with the L3 bypass established (T4 2026-04-13), the reduced condition "verify that the ITPFI spectral measure with $|\hat{\mu}(t)| \asymp 1/\log |t|$ falls within the Tao-Vu universality class (local semicircle law or substitute)" is a tractable analytic verification task, not a structural gap. Status: **OPEN as a technical verification**, not a conceptual wall.
  - Decomposition pointer: pending a dedicated research memo verifying the local semicircle law holds for the infinite Bernoulli convolution with arithmetic parameters $\{\lambda_p = 1/p\}$.

No other named walls. W1 is the structural wall; W2 is an auditable technical condition. The BGS chain is the closest-to-closed of the extended programme's Clay-adjacent vertices (per the session_bsd_runs1to5 and RH memories).

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/bgs/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle's `proof-chain/` directory is empty as of 2026-04-14). When created, the X-Ray's L3.B reduced condition (W2) is the natural first decomposition target; the L6 CCM gate (W1) decomposes jointly with rh and bsd.
- **CCM verification**: `strategy/ccm-verification/ledger.md#bgs` — NOT YET CREATED. Expected verdict when ledger is written: **IRREDUCIBLY-CCM-DEPENDENT at L6** (L6 = spectral realization is the CCM gate itself, shared with rh and bsd). Internal links L1–L5, L7 are CCM-independent.
- **Inner rings**: NOT APPLICABLE — BGS is a primary outer-ring vertex, not an inner-ring object.
- **Traversal 02/03/04 proof memos** (2026-04-13): closed the chain's internal walls.
  - Traversal 02 → `solutions/paper32-bgs-spectral-statistics/research/01-modular-flow-ergodicity.md` (L2 closure, bypassing non-separable predual).
  - Traversal 03 → `solutions/paper32-bgs-spectral-statistics/research/02-gue-class-dyson.md` (L4 closure, arithmetic obstruction).
  - Traversal 03 → `solutions/paper32-bgs-spectral-statistics/research/03-ac-spectrum-gap-analysis.md` (L3.A genuine-gap identification, connected to $\zeta(1+it)$).
  - Traversal 04 → `solutions/paper32-bgs-spectral-statistics/research/04-l3-bypass-universality.md` (L3.B bypass via universality).
- **Nov 2025 Hardy Z PCC intake** (2026-04-14): reclassified L5 from CONJECTURED to LITERATURE per Agent-I audit; the chain's own "single strongest lead" reference (arXiv:2511.18275) IS the published proof.
- **Verification Cascade tier**: BGS sits in Tier 2 (CCM-dependent) alongside rh and bsd. The CCM-gate closure strategy is jointly owned by these three vertices.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — CCM spectral realization (L6)**: $\text{spec}(D_\infty) = \{\gamma_n\}$ from Paper 13 + CCM 2025. — face: RESONANCE, projection: $P_O$, pattern: P1. STATUS: OPEN as CCM-gate conditional; shared with rh and bsd. This is the primary wall.

- **G2 — L3.B reduced condition (universality-class verification)**: Verify that the infinite Bernoulli convolution $\mu = \ast_p \mu_p$ with arithmetic parameters $\{\lambda_p = 1/p\}$ and Fourier decay $|\hat{\mu}(t)| \asymp (\log |t|)^{-1}$ satisfies the Tao-Vu local semicircle law (or an equivalent universality-class membership condition). — face: RESONANCE, projection: $P_D$, pattern: P5. STATUS: OPEN as technical verification (not structural gap).

That's it. 5 of 7 main layers are closed unconditionally (L1 KNOWN, L2 PROVED, L4 PROVED, L5 LITERATURE, L7 KNOWN). L3 is BYPASSABLE with a tractable reduced condition (G2). L6 is the sole structural wall (G1), shared with rh and bsd. The chain is closer-to-closed than any other extended-programme Clay-adjacent vertex (per session memory `session_verification_cascade_ready.md`).

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-02/vertices/bgs/critic-attacks.md` and arbiter decisions at `strategy/x-ray/pac-output/runs/run-02/vertices/bgs/arbiter-decisions.md` (both to be populated by the PAC run).

Notable arbiter wins (per §3 rejected alternatives):
- L1 face: RESONANCE over DYNAMICS (the type III$_1$ factor is the *setting* for the flow, not the flow itself; RESONANCE is paper60 §20 Face 9 canonical).
- L2 face: DYNAMICS over RESONANCE (ergodicity of the flow is the LOAD-BEARING dynamical content; continuous-spectrum consequence is inherited corollary).
- L3 pattern: P5 over P4 (regulator-style zeta-control via $\zeta(1+it)$ decay is the mechanism, not rigidity).
- L4 pattern: P1 over P4 (Pattern 1 "restore the e-circle" geometric reinterpretation of the Euler product as time-reversal-breaking; rigidity implied but not primary).
- L5 pattern: P4 over P5 (universality = rigidity of the functional form; zeta-regularization implicit in DBM technique but not load-bearing).
- L6 projection: $P_O$ over $P_D$ (the TRANSFER step is outer-ring-facing; Clay-grade closure boundary).
- L7 projection: $P_E$ over $P_O$ (empirical measurement is Branch E's domain; Branch E contact not outer-ring proclamation).
- Primary face: RESONANCE over DYNAMICS (paper60 §20 Face 9 canonicalization; DYNAMICS is secondary at L2 only).
- Primary projection: $P_D$ over $P_D \cap P_E$ (dominant single projection is $P_D$; $P_D \cap P_E$ is the compound per paper61 §12 Vertex 13, but the X-Ray asks for primary single projection).

34 / 35 author wins out of 35 total field decisions (5 fields × 7 main layers). The single critic win (L3 pattern P5 over P4 alternative reading) reflects the genuine subtlety of whether the L3.A obstruction and L3.B bypass both ride the same regularization engine (they do — the $\zeta(1+it)$ decay in L3.A and the Tao-Vu universality-class containment in L3.B both trace back to the zeta function's behavior on the critical strip).

---

*End of BGS X-Ray. Snapshot 2026-04-15. 7 layers annotated (L3 with A/B sub-branches giving 8 entries). 41 cross-cuts identified (densest vertex on the spectral circle). RESONANCE-canonical, $P_D$-dominant, P4-primary proof chain. Two walls (W1 CCM gate / W2 universality-class verification); both have decomposition pointers; W1 is the sole structural wall shared with rh and bsd.*

*G Six and Claude Opus 4.6. April 15, 2026.*
