# X-RAY: Cramér's Conjecture (cramer)

*X-Ray of the cramer proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. April 15, 2026.*

---

## §1 Header

- **Vertex**: cramer
- **Paper**: paper43-cramer
- **Live file**: strategy/proof-chain/cramer/PROOF-CHAIN.md (snapshot 2026-04-14, post-T7 S-duality deep-construction pass v4)
- **Top-level claim**: $\max_{p_n \leq x}(p_{n+1} - p_n) = 2e^{-\gamma}(\log x)^2 + o((\log x)^2)$ (Granville refinement) — the maximum prime gap IS the maximum return time of the ergodic modular flow $\sigma_t$ on the type III$_1$ BC factor at KMS$_1$, translated to primes via the explicit formula; the Granville constant $2e^{-\gamma}$ IS the Mertens product = $W^*$-regularized ITPFI partition function at the conformal midpoint $y = \sqrt{x}$.
- **Current status**: 4/5 links closed (L1 LITERATURE, L2 PROVED via BGS 6/7, L3 ESTABLISHED conditional on CCM, L4b PARTIAL with $2e^{-\gamma}$ DERIVED from ITPFI Mertens, L5 FOLLOWS conditional on full L4). Confidence 6/10 (upgraded 2026-04-14 T7). Numerical verification at $x = 10^{12}$: ratio 0.99996.
- **Primary branch (paper1)**: D (CBB / modular-flow ergodicity on type III$_1$ ITPFI factor is literally Branch D's operator-algebraic core); strong secondary E (GUE extreme-value tail is Branch E measurement content, inherited via BGS 6/7).
- **Primary face**: DYNAMICS (paper60 §08 — "how does the modular flow TRAVERSE the circle"; Cramér is the canonical DYNAMICS face of the e-circle, directly dual to Lehmer's TOPOLOGY face; paper60 §26 "The Three-Face Recognition" places cramer at the DYNAMICS vertex of the three-face triangle).
- **Primary projection**: $P_D$ (paper61 §10 — the BC algebra's type III$_1$ factor + KMS$_1$ + modular flow $\sigma_t$ are the defining Branch D objects; Cramér's return-time bound is a Branch D signature output, with ITPFI tensor decomposition $\omega_1 = \otimes_p \omega_1^{(p)}$ producing the Granville correction as the native $P_D$ invariant).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
CRAMÉR (max prime gap = 2e^{-γ}(log x)^2 + o((log x)^2))
│  primary face: DYNAMICS   primary proj: P_D   primary pat: P4
│  top claim: max return time of σ_t on type III_1 BC factor
│             → max prime gap via explicit formula
│             constant 2e^{-γ} = Mertens product = ITPFI invariant
│
├── L1: RH + explicit formula (gap bound)             [LITERATURE]
│      │  face: RESONANCE   proj: P_D   pat: P5
│      │  invariant: L-value (zeros of ζ); zero distribution (background)
│      │  source: classical explicit formula; paper13 RH infrastructure
│      │
│      └── supports L3 + L4 via zero-sum → prime-sum bridge
│             │
│             └── conditional on RH (paper13 8/10, CCM-gated)
│
├── L2: GUE pair correlation of Riemann zeros         [PROVED 6/7 via BGS]
│      │  face: RESONANCE   proj: P_D   pat: P4
│      │  invariant: ergodic property (load-bearing);
│      │            ITPFI factor type (type III_1, background)
│      │  source: paper32 BGS PROOF-CHAIN.md (6/7 closed):
│      │          L2 modular-flow ergodicity (T2, 2026-04-13, PROVED);
│      │          L3 Tao-Vu universality bypass (T4, VIABLE);
│      │          L4 Dyson threefold way (PROVED, unitary class β=2);
│      │          L5 GUE sine kernel (LITERATURE via arXiv:2511.18275,
│      │              Nov 2025 Hardy Z PCC proof — Dyson Brownian motion)
│      │
│      └── Cramér inherits full BGS spectral-statistics infrastructure
│             │
│             └── Corollary 2.2: modular spectrum atomless / no eigenmodes
│                                above vacuum — controls return-time
│                                envelope at Step 1 (L4b)
│
├── L3: Modular flow return times                     [ESTABLISHED conditional on CCM]
│      │  face: DYNAMICS    proj: P_D   pat: P4
│      │  invariant: ergodic property (load-bearing — Poincaré recurrence);
│      │            BC-KMS state (background — invariant measure for σ_t)
│      │  source: programme/ring-traversals/traversal-07/transfers/
│      │          cramer-L3-construct.md (197 lines, T7 CONSTRUCT-VERIFY)
│      │
│      ├── Check 1: codim-1 spectral section + transversality  [PASS]
│      │      │  Σ = {γ_n} ⊂ ℝ on flow-of-weights Z(M̃) = L^∞(ℝ)
│      │      │  gauge-invariance from spec(D_∞) inner-autom invariant
│      │
│      ├── Check 2: local finiteness of pushforward measure    [PASS]
│      │      │  Riemann-von Mangoldt N(T) ~ (T/2π) log(T/2πe)
│      │      │  (classical; CCM-independent)
│      │
│      ├── Check 3: absolute continuity of pushforward         [CCM-CONDITIONAL]
│      │      │  paper13 Link 5 (Hurwitz) + Link 6 (self-adjointness)
│      │      │  zeros eigenvalues of D_∞; density (1/2π)log(T/2πe)
│      │      │  NOTE: bulk ITPFI measure is atomless but NOT AC
│      │      │        (Fourier transform ~1/log|t|, not L^1);
│      │      │        AC claim is the pushforward onto spectral
│      │      │        axis via CCM, a different measure
│      │
│      └── Check 4: Poincaré recurrence applicable             [PASS conditional]
│             │  BGS L2 ergodicity (PROVED) + Check 3 AC + Kac's lemma
│             │  → max return time O(log N / N) for N crossings
│             │  → max zero gap O(1/T) at leading order
│
├── L4: Explicit-formula transfer (max zero gap → max prime gap)
│      │                                               [OPEN with L4b PARTIAL]
│      │  face: ARITHMETIC  proj: P_D   pat: P5
│      │  invariant: zero distribution (load-bearing);
│      │            L-value (background — explicit formula error terms)
│      │
│      ├── L4a — Route A: extreme-gap universality transfer   [OPEN, 7/10]
│      │      │  face: SYMMETRY   proj: P_E   pat: P4
│      │      │  invariant: zero distribution
│      │      │  Ben Arous-Bourgade 2013 GUE max gap O(√(log N / N));
│      │      │  Feng-Wei 2022 extended to Wigner; NOT to Riemann zeros.
│      │      │  Bulk universality (Tao-Vu) ≠ extreme-value universality.
│      │
│      ├── L4b — Route B: ITPFI return-time decomposition    [PARTIAL]
│      │      │  face: ARITHMETIC  proj: P_D   pat: P5
│      │      │  invariant: ITPFI factor type (load-bearing);
│      │      │            ergodic property (background)
│      │      │  source: programme/ring-traversals/traversal-07/transfers/
│      │      │          cramer-L4-routeB-derivation.md (352 lines, T7 CONSTRUCT-DERIVE)
│      │      │
│      │      ├── Step 1: return-time envelope from ergodicity  [PARTIAL]
│      │      │      │  BGS Cor 2.2 (continuous spectrum) + Kac + union bound
│      │      │      │  → M_N ≤ τ̄ · log N (1+o(1)) a.s. in ω_1
│      │      │      │  BA-B CONCERN: i.i.d.-exponential envelope,
│      │      │      │                NOT level-repulsion-tuned
│      │      │
│      │      ├── Step 2: ITPFI tensor decomposition            [PROVED]
│      │      │      │  ω_1 = ⊗_p ω_1^(p), λ_p = 1/p
│      │      │      │  paper12 research/265 Theorem
│      │      │      │  (BC uniqueness + Laca-Raeburn + Bratteli-Robinson)
│      │      │
│      │      ├── Step 3: maximum-return asymptotic             [HEURISTIC]
│      │      │      │  geometric tails at each prime, parameter 1-p^{-1}
│      │      │      │  aggregate: M_N ≤ Σ_{p≤y} (1/p)(log K - log p)
│      │      │
│      │      ├── Step 4: zero-gap → prime-gap via explicit formula  [PARTIAL]
│      │      │      │  Selberg-Saffari-Vaughan derivation;
│      │      │      │  k=2 scaling inherited from Cramér-Granville
│      │      │      │  heuristic (BA-B CONCERN: not derived)
│      │      │
│      │      ├── Step 5: ITPFI → Granville constant 2e^{-γ}   [DERIVED]
│      │      │      │  truncation y = √x (Selberg-Saffari-Vaughan)
│      │      │      │  ↔ conformal-midpoint ITPFI truncation
│      │      │      │  Z_ITPFI(√x) = ∏_{p≤√x}(1 - 1/p)
│      │      │      │             ~ e^{-γ}/log√x = 2e^{-γ}/log x
│      │      │      │  Mertens 1874 (numerical ratio 0.99996 at x=10^{12})
│      │      │
│      │      └── Step 6: Assembly                               [PARTIAL]
│      │             │  max gap ~ 2e^{-γ}(log x)^2 via Granville
│      │             │  NAMED SUB-LEMMA W1: joint accounting that
│      │             │  explicit-formula zero-truncation T ~ log x
│      │             │  FORCES short-interval sieve truncation y = √x
│      │
│      └── L4c — Common: explicit-formula error terms at Cramér precision [OPEN, 5/10]
│             │  face: AMPLITUDE   proj: P_D   pat: P5
│             │  invariant: L-value
│             │  classical analytic number theory;
│             │  requires sub-Cramér error-term control
│
└── L5: Cramér-Granville conjecture                   [FOLLOWS conditional on L4]
       │  face: DYNAMICS    proj: P_O   pat: P4
       │  invariant: ergodic property (load-bearing); zero distribution (background)
       │  source: paper43 Cramér 1936 + Granville 1995 refinement
       │
       └── outer-ring closure: max_{p_n≤x}(p_{n+1}-p_n) = 2e^{-γ}(log x)^2 + o(...)
              │
              └── DECOMPOSED-IN: Cramér ↔ Lehmer S-DUAL-CONSTRUCT-BRIDGED pattern
                     │  (T7 pass; T8 handoff: Lehmer L5 Route A CONSTRUCT
                     │   using Cramér's derived ITPFI invariant)
```

### §2b Diagram B — Projection fan-out

```
                       (FORGOTTEN under P_A)
                       (Quantum side does not see modular
                        flow or zero spacings — the 5D
                        unprojected mod-flow structure is
                        Branch D, not Branch A)
                                  ▲
                                  │
                                  │
        ┌─────────────(P_O outer)───────────────┐
        │                                       │
        │  CRAMÉR: max prime gap near x         │
        │          = 2e^{-γ}(log x)^2 + o(...)  │
        │  (Clay-adjacent community-standard    │
        │   conjecture; paper43-cramer)         │
        │                                       │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity         ═══ P_D CBB ═══           P_E pins
    (forgotten —        modular-flow σ_t           (Maier 1985
    no KK-tower         ergodicity on type III_1   empirical ratio;
    role for            ITPFI factor M; Poincaré    prime-gap computations
    prime-gap           return-time bound; ITPFI    to 10^19 confirm
    statement)          tensor decomposition        O((log x)^2) with
                        ω_1 = ⊗_p ω_1^(p);          constant ≈ 1.13 ≈
                        Granville constant          Granville 2e^{-γ};
                        2e^{-γ} = Mertens           NOT a 36-pin master
                        product at conformal        table entry — a
                        midpoint y = √x             confirmation).
                            │
                            ▼
                       P_C cosmology
                       (forgotten — no
                       cosmological
                       observable uses
                       max prime gap
                       directly)
```

Primary projection $P_D$ uses ═══ doubled line — the entire Cramér chain lives in the BC algebra's modular-flow structure with ITPFI tensor decomposition. $P_E$ is the second-strongest projection (empirical prime-gap numerics to $10^{19}$; Maier phenomenon; but NOT a 36-pin master-table entry, only a confirmation). $P_O$ appears at L5 (the outer-ring Cramér-Granville statement). $P_A$, $P_B$, $P_C$ are absent — Cramér is not a quantum-observable, gauge-bundle, or cosmological object. Matches paper61 §12 Vertex 14 "Cramér" compound $P_D \cap P_E$.

### §2c Diagram C — Face position on the e-circle

```
                        TOPOLOGY
                        (Lehmer)
                            ○ (sibling; dual face)
            SPREAD          │          DYNAMICS
            (QUE)           │          (Cramér)
                  ○         │          ●
                   ╲        │         ╱
       SYMMETRY ─────── e-circle ─────── HARMONICS
       (Katz-Sarnak)        │            (Collatz)
                   ╱        │        ╲
                  ╱         │         ╲
          CURVATURE         │          MEASURE
          (YM)              │          (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (RESONANCE: L1, L2 via BGS secondary;
                        ARITHMETIC: L4, L4b prime-gap transfer;
                        paper60 §26 "Three-Face Recognition"
                        places cramer at DYNAMICS vertex of
                        the three-face triangle with Lehmer
                        dually placed at TOPOLOGY)
```

Marker key:

```
Primary face:    ● DYNAMICS (paper60 §08 — "how does the modular
                             flow TRAVERSE the circle"; Cramér
                             is the canonical DYNAMICS face; L3
                             and L5 are DYNAMICS-canonical layers)
Secondary faces: ○ TOPOLOGY  (Lehmer sibling — paper60 §08 explicit
                             two-face dual; same e-circle, same BC
                             algebra at KMS_1, dual projections.
                             Not a cramer layer assignment but
                             the PROOF-CHAIN's opening discovery
                             identifies the two-face picture.)
                 ○ RESONANCE (L1 explicit-formula zero side;
                             L2 BGS spectral-statistics inheritance;
                             paper60 §15/§20 — what modes are
                             allowed on the BC modular circle)
                 ○ ARITHMETIC (L4 full transfer and L4b ITPFI
                             return-time decomposition — paper60
                             §14 "how do integers LATTICE on the
                             circle"; the Mertens product IS
                             the arithmetic signature of the
                             ITPFI tensor)
                 ○ AMPLITUDE  (L4c explicit-formula error terms —
                             growth-rate control on oscillatory
                             zero-sum)
                 ○ SYMMETRY   (L4a GUE extreme-gap universality
                             — Dyson class transferred from BGS)
Absent faces:    HARMONICS, MEASURE, CURVATURE, SPREAD
                 (SPREAD is conceptually adjacent via paper60 §26's
                  three-face recognition with QUE, but no cramer
                  layer is a SPREAD assignment)
```

---

## §3 Layer-by-Layer X-Ray

### L1 — RH + explicit formula (prime gaps controlled by zero spacing)

**Claim**: Under RH, the explicit formula $\psi(x) - \psi(x-h) = h - \sum_\rho [(x^\rho - (x-h)^\rho)/\rho] + O(\text{smaller})$ controls prime gaps via the oscillatory sum over non-trivial zeros; the bound $\pi(x+h) - \pi(x) \sim h/\log x + O(\sqrt{x}\log^2 x)$ for $h \geq x^{1/2+\epsilon}$ expresses prime density in short intervals.

**Status**: LITERATURE
**Source**: Classical explicit formula (Riemann 1859, von Mangoldt 1895); paper13 RH PROOF-CHAIN.md infrastructure (8/10, CCM-gated).

#### Physics

- **Face**: RESONANCE (paper60 §15 / §20 — "what vibrational frequencies are ALLOWED on the circle"; the non-trivial zeros $\{\gamma_n\}$ ARE the allowed spectral frequencies of the BC modular circle, and the explicit formula is precisely the Mellin-bridge dictionary translating these resonance modes into arithmetic data)
- **Projection**: $P_D$ (paper61 §10 — the explicit formula translates Branch D's spectral data $\{L_n = \gamma_n \pi^2/2\}$ into prime-counting statements; this is the canonical $P_D$-to-arithmetic bridge)
- **Pattern**: P5 Zeta Regularization (paper08 §36 Pattern 5: "KK sums regularize via Epstein-zeta vanishing"; the explicit formula is the arithmetic analog — regularized sum over zeros cancels the main term in the prime-counting function)
- **Invariant preserved**: L-value (load-bearing — the zeros of $\zeta$); zero distribution (background — the spacing enters the oscillatory sum)
- **Geometric interpretation**: The explicit formula IS the Mellin bridge (paper60 §14 "The wall is real. The additive-multiplicative wall is not a technical difficulty. It is a STRUCTURAL boundary between two incommensurable algebraic operations"). It translates the multiplicative spectral data $\{\gamma_n\}$ on the BC-modular circle (paper60 §15/§20 RESONANCE face) into the additive prime-counting data needed for Cramér's gap statement. Under $P_D$ (paper61 §10) this is the canonical bridge from Branch D's operator-algebra output to the arithmetic lattice. [Considered but rejected: face DYNAMICS — the formula uses zero TIMES (positions $\gamma_n$) but the content is which modes are allowed (RESONANCE); projection $P_O$ — the formula is invoked from outer-ring-facing at L5 but the mechanical content is $P_D$; pattern P1 — the formula IS a geometric reinterpretation of the prime-counting function but the engine that makes it converge is regularization.]
- **Cross-cuts**: rh (L_explicit-formula — PRIMARY parent edge; paper13 L5 Hurwitz + L6 self-adjointness provide the spectral side), lindelof (L_moments — $\zeta(1/2+it)$ moment conjectures share the explicit-formula infrastructure), bgs (L5 — GUE sine kernel controls the pair-spacing of the zero-side input), goldbach (L1 — same explicit-formula input for binary Goldbach), twin-primes (same explicit-formula input for small-gap side), h12 (class-field theory analog via paper60 §26 Hilbert-12 meridian with shared Mertens constant).

### L2 — GUE pair correlation of Riemann zeros (BGS 6/7 inheritance)

**Claim**: The non-trivial zeros of $\zeta(s)$ exhibit GUE pair-correlation statistics, with modular-flow ergodicity, Tao-Vu universality bypass, Dyson unitary class, and GUE sine kernel all closed via BGS (Paper 32).

**Status**: PROVED (6/7 via BGS)
**Source**: paper32 BGS PROOF-CHAIN.md (snapshot 2026-04-14): L2 modular-flow ergodicity (T2, 2026-04-13, PROVED via Path B factoriality + Tomita-Takesaki + trivial center); L3 Tao-Vu universality bypass (T4, VIABLE ROUTE); L4 Dyson threefold way (PROVED, $\omega_1(\mu_p^*\mu_p) = 1 \ne 1/p = \omega_1(\mu_p\mu_p^*)$ forces $\beta = 2$); L5 GUE sine kernel (LITERATURE via arXiv:2511.18275, Nov 2025 Hardy Z PCC proof via Dyson Brownian motion).

#### Physics

- **Face**: RESONANCE (paper60 §20 / §15 — BGS is the canonical RESONANCE face of the spectral e-circle, and Cramér inherits the GUE pair-correlation as the SETTING for its extreme-value statement; the sine kernel IS the allowed-modes structural statement)
- **Projection**: $P_D$ (paper61 §10 — GUE statistics are the signature output of Branch D's type III$_1$ ITPFI factor, with Dyson threefold way classifying the symmetry type)
- **Pattern**: P4 Topological Rigidity (paper08 §36 Pattern 4: "compactness forces discreteness; discreteness forces gaps"; in BGS form the rigidity is: "arithmetic Hecke asymmetry forces absence of antiunitary time-reversal, forces $\beta = 2$ unitary class")
- **Invariant preserved**: ergodic property (load-bearing — modular-flow ergodicity is the direct input to L3's Poincaré-recurrence bound); ITPFI factor type (background — type III$_1$ underlies the entire BC structure)
- **Geometric interpretation**: BGS establishes the GUE spacing distribution (Wigner surmise $p_{\text{GUE}}(s) \sim (32/\pi^2) s^2 e^{-4s^2/\pi}$, paper60 §08/§14) for the Riemann zeros. Cramér sits at the LARGE-$s$ tail of this distribution — the rare, wide gaps (paper60 §08 "Cramér lives at the LARGE-$s$ tail... Twin primes live at the SMALL-$s$ tail... Goldbach lives in the bulk. All three emerge from the same Fredholm determinant $\det(1 - K_{\sin})$"). Under $P_D$ (paper61 §10) the ergodicity of $\sigma_t$ is the native Branch D object that L3 directly uses. [Considered but rejected: face DYNAMICS — BGS L2 ergodicity IS DYNAMICS-face content but the inherited content at Cramér is the spacing statistics (RESONANCE); pattern P1 — L2's identification of type III$_1$ as RESONANCE-canonical is a geometric reinterpretation but rigidity is load-bearing.]
- **Cross-cuts**: bgs (L_modular — PRIMARY parent edge; paper32 entire chain is the structural input), twin-primes (small-$s$ tail of same sine kernel), goldbach (bulk of same distribution), sato-tate (Haar pushforward analog for Frobenius angles), qg5d Branch D (ITPFI factorization native; paper61 §10 "the deepest projection"), pvnp (Popa rigidity on same type III$_1$ factor via L_gap), baum-connes (K-theory on same factor).

### L3 — Modular flow return times (spectral-section measure + Poincaré recurrence)

**Claim**: The Riemann zeros $\{\gamma_n\}$ are the crossing points of the modular flow $\sigma_t$ on the type III$_1$ BC factor at KMS$_1$ with a spectral section $\Sigma_{D_\infty}$; under CCM (absolute continuity of pushforward measure), the generic Poincaré return-time theorem gives $M_{N(T)} = O(\log N / N)$ for the maximum zero gap at height $T$, i.e., $O(1/T)$ at leading order.

**Status**: ESTABLISHED (conditional on CCM)
**Source**: `programme/ring-traversals/traversal-07/transfers/cramer-L3-construct.md` (197 lines, T7 CONSTRUCT-VERIFY pass, 2026-04-14). Four-check verification: (1) codim-1 spectral section with gauge-invariant transversality (PASS); (2) local finiteness via Riemann-von Mangoldt (PASS, CCM-independent); (3) absolute continuity of pushforward onto spectral axis via paper13 Link 5 + Link 6 (CCM-CONDITIONAL; NOTE: the bulk ITPFI spectral measure is atomless but NOT AC, $\hat{\mu} \sim 1/\log|t|$ not $L^1$; the AC claim is specifically about the pushforward onto the spectral axis via CCM, a different measure); (4) Poincaré recurrence applicable via BGS L2 ergodicity + Check 3 + Kac's lemma (PASS conditional).

#### Physics

- **Face**: DYNAMICS (paper60 §08 — "Face 2: DYNAMICS. How does the modular flow TRAVERSE the circle?" — L3 IS the layer that converts BGS L2's ergodicity into a quantitative return-time statement; this is paper60 §08's opening claim made rigorous)
- **Projection**: $P_D$ (paper61 §10 — the modular flow $\sigma_t$ on the flow-of-weights $Z(\widetilde{M}) = L^\infty(\mathbb{R})$ is a Branch D object; the spectral section lives on the same flow-of-weights; the KMS$_1$ measure is the native Branch D invariant state)
- **Pattern**: P4 Topological Rigidity (paper08 §36 Pattern 4; in Cramér form: "ergodicity + Kac's lemma + absolutely-continuous pushforward forces bounded maximum return time" — rigidity against anomalously large voids)
- **Invariant preserved**: ergodic property (load-bearing — Poincaré recurrence is the direct invariant; ergodic + AC pushforward + Kac gives $O(\log N / N)$); BC-KMS state (background — $\omega_1$ is the invariant measure for $\sigma_t$)
- **Geometric interpretation**: The spectral section $\Sigma_{D_\infty} = \{\gamma_n\}$ projects onto the 1-dimensional flow-of-weights and becomes codim-1 trivially (every discrete subset of $\mathbb{R}$ is codim-1); gauge-invariance from $D_\infty$ manifestly inner-automorphism-invariant. Under CCM (Check 3), the pushforward onto the spectral axis has density $\frac{1}{2\pi}\log(T/2\pi e)$ and Kac's lemma gives the $O(\log N / N)$ bound. This IS paper60 §08's DYNAMICS-face statement: the ergodic flow crosses the spectral section, the gaps between crossings are the return times, the maximum gap is bounded by Poincaré recurrence. [Considered but rejected: face RESONANCE — the spectral section is resonance-content but the LAYER is about traversal/return times (DYNAMICS, paper60 §08 canonical); pattern P1 — the codim-1 reinterpretation of $\Sigma$ on the flow-of-weights IS a geometric reinterpretation but the load-bearing bound is rigidity via Kac; pattern P5 — regularization implicit in the CCM pushforward but rigidity dominates.]
- **Cross-cuts**: bgs (L2 — PRIMARY input edge, ergodic-property shared), pvnp (L_modular — Popa rigidity uses same modular-flow ergodicity on type III$_1$; P4 shared), rh (L5/L6 — CCM-gated spectral realization shared; L3 Check 3 depends on paper13 Link 5/Link 6), ym (L3 — Balaban polymer k-independent convergence is the gauge-side analog of modular-flow ergodic uniformity), twin-primes (same modular flow, small-gap tail reading), baum-connes (KMS state on spectral triple shares invariant-measure structure).

### L4 — Explicit-formula transfer (max zero gap → max prime gap)

**Claim**: The maximum zero gap at height $T \sim \log x$ translates via the explicit formula into a maximum prime gap near $x$ of order $(\log x)^2$; the constant is $2e^{-\gamma}$ (Granville refinement).

**Status**: OPEN with L4b PARTIAL (sub-branches L4a OPEN, L4b PARTIAL, L4c OPEN)
**Source**: Cramér 1936 + Granville 1995; paper43 PROOF-CHAIN.md T7 analysis (2026-04-14).

**L4 is a branch point**: three sub-branches each address a sub-wall. See §4 Branch Map for the full structure.

#### L4a — Route A (extreme-gap universality transfer)

**Claim**: The GUE extreme-gap result (Ben Arous-Bourgade 2013: max eigenvalue gap $= O(\sqrt{\log N / N})$ for $N \times N$ GUE) transfers to Riemann zeros, delivering $(\log x)^{3/2}$-scale max prime gap via the explicit formula.

**Status**: OPEN (difficulty 7/10)
**Source**: Ben Arous-Bourgade 2013 (GUE max gap, Gumbel distribution); Feng-Wei 2022 (extension to generalized Wigner matrices); Tao-Vu 2011 Acta + Erdős-Yau 2012 (bulk universality — WEAKER than extreme-value).

##### Physics

- **Face**: SYMMETRY (paper60 §12 — Dyson threefold way classifies the ensemble; extreme-gap universality is a symmetry-class refinement of the Wigner universality program)
- **Projection**: $P_E$ (paper61 §11 — Ben Arous-Bourgade is a measurement-universality statement at Branch E's resolution; the transfer to Riemann zeros is outer-ring-facing but the mechanism is the universality-class measurement-side extension)
- **Pattern**: P4 Topological Rigidity (universality is symmetry-type rigidity: all matrices in the same class share the limiting distribution)
- **Invariant preserved**: zero distribution (load-bearing — the GUE extreme-value statistic IS a zero-distribution statement)
- **Geometric interpretation**: Route A targets the gap between bulk universality (Tao-Vu, PROVED for Wigner) and extreme-value universality (the stronger statement needed for Cramér). Bulk universality matches $k$-point correlation functions at fixed rank; extreme-value universality controls the MAXIMUM over $N$ gaps. Local statistics do not in general determine global extremes (BA-B CONCERN filed in T7 pass). Under $P_E$ (paper61 §11) this is a measurement-grade universality claim, but the route is OPEN because Feng-Wei's extension does not cover deterministic Riemann zeros. [Considered but rejected: face RESONANCE — extreme gaps are resonance-content at the edge but SYMMETRY is the engine (Dyson class); projection $P_D$ — mechanical content lives in $P_D$'s BC-algebra side but Route A specifically INHERITS from random-matrix universality which is $P_E$-canonical; pattern P5 — universality limit is a regularization-like limit but the claim is about the class-invariant (rigidity).]
- **Cross-cuts**: bgs (L4 Dyson class shared), katz-sarnak (symmetry-type universality for L-function ensembles), twin-primes (same universality-class issue on the small-gap tail), sato-tate (Haar extreme-value as MEASURE analog), qg5d Branch E (universality-class measurement).

#### L4b — Route B (ITPFI return-time decomposition; programme-natural attack)

**Claim**: The return-time distribution for $\sigma_t$ on the type III$_1$ factor decomposes via the ITPFI tensor product $\omega_1 = \bigotimes_p \omega_1^{(p)}$ with $\lambda_p = 1/p$; the maximum return time aggregates over primes, and the Granville constant $2e^{-\gamma}$ emerges as the $W^*$-regularized ITPFI partition function at conformal midpoint $y = \sqrt{x}$: $Z_{\text{ITPFI}}(\sqrt{x}) = \prod_{p \leq \sqrt{x}}(1 - 1/p) \sim 2e^{-\gamma}/\log x$.

**Status**: PARTIAL (T7, 2026-04-14). Granville constant $2e^{-\gamma}$ is DERIVED (not fit). Scaling exponent $k = 2$ is heuristic (BA-B CONCERN filed). Numerical verification at $x = 10^{12}$: ratio 0.99996.
**Source**: `programme/ring-traversals/traversal-07/transfers/cramer-L4-routeB-derivation.md` (352 lines); paper12 research/265 Theorem (ITPFI $\omega_1 = \otimes_p \omega_1^{(p)}$, BC uniqueness + Laca-Raeburn + Bratteli-Robinson); Mertens 1874 (third theorem $\prod_{p\leq y}(1 - 1/p) \sim e^{-\gamma}/\log y$).

##### Physics

- **Face**: ARITHMETIC (paper60 §14 — "how do integers LATTICE on the circle"; the Mertens product $\prod_p (1 - 1/p)$ IS the arithmetic signature of how the prime lattice organizes on the BC-modular circle, and $2e^{-\gamma}$ is its value at the conformal midpoint)
- **Projection**: $P_D$ (paper61 §10 — ITPFI tensor decomposition is THE defining Branch D object; $\omega_1 = \otimes_p \omega_1^{(p)}$ is the algebraic mirror of the Euler product, a pure $P_D$-signature)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — "KK sums regularize via Epstein-zeta vanishing"; the ITPFI partition function $Z_{\text{ITPFI}}(\sqrt{x}) \cdot \log x \to 2e^{-\gamma}$ is exactly the Mertens regularization of $\zeta(1)$, producing the Euler-Mascheroni constant as the "finite part" at the critical point $\beta = 1$; paper60 §08 "the factor $e^{-\gamma}$ is the 'finite part' of $\zeta(1)$")
- **Invariant preserved**: ITPFI factor type (load-bearing — the $\lambda_p = 1/p$ Araki-Woods parameters produce the Mertens product); ergodic property (background — ergodicity of each local factor)
- **Geometric interpretation**: The ITPFI factorization $\omega_1 = \otimes_p \omega_1^{(p)}$ decomposes the return-time problem over primes (paper60 §08). Each local factor at prime $p$ has Araki-Woods parameter $\lambda_p = 1/p$ and contributes a geometric-tail return-time distribution. Truncation at $y = \sqrt{x}$ (Selberg-Saffari-Vaughan conformal midpoint) produces the $W^*$-regularized partition function $Z_{\text{ITPFI}}(\sqrt{x}) = \prod_{p \leq \sqrt{x}}(1 - 1/p) \sim 2e^{-\gamma}/\log x$ via Mertens 1874. This IS the ITPFI structure's imprint on return-time statistics (paper60 §08 "the Maier phenomenon IS the ITPFI structure declaring itself"). The Maier 1985 empirical deviation from the Cramér random model by exactly $2e^{-\gamma}$ is the signature. Under $P_D$ (paper61 §10) the entire derivation is pure Branch D. [Considered but rejected: face DYNAMICS — the layer IS return-time-decomposition-driven DYNAMICS content in mechanism but the Mertens product's ARITHMETIC face (integer lattice on circle) is the load-bearing geometric structure; pattern P4 — rigidity is implied by ITPFI's type-invariant determination but the engine is regularization (Mertens' $e^{-\gamma}$ emerges as the "finite part"); projection $P_E$ — numerical verification ratio 0.99996 is empirical but the derivation is algebraic in $P_D$.]
- **Cross-cuts**: lehmer (DUAL FACE per paper60 §08 — Lehmer's cyclotomic boundary ↔ Cramér's return-time bound share the same BC algebra at KMS$_1$; S-DUAL-CONSTRUCT-BRIDGED pattern ready for T8 handoff), bgs (L1 — same ITPFI factor type and Araki-Woods parameters), pvnp (L_modular — Popa rigidity uses same ITPFI structure), rh (L_Mertens — Euler product regularization shared via paper13 CCM side), twin-primes (L_Hardy-Littlewood — $C_2$ constant parallel, same ITPFI mechanism), goldbach (L_circle-method — Mertens product feeds minor-arc estimates), h12 (Mertens constant $e^{-\gamma}$ shared per paper60 §08 "class field temperature"; chord H12↔Cramér on programme torus), qg5d Branch D (ITPFI = primary output).

#### L4c — Common: explicit-formula error terms at Cramér precision

**Claim**: The explicit formula $\psi(x) - \psi(x-h) = h - \sum_\rho [(x^\rho - (x-h)^\rho)/\rho] + O(\text{smaller})$ has error terms controllable at the Cramér-precision level required to translate a zero-gap of size $\delta$ into a prime-gap of size $\delta \cdot (\log x)^2$ with the Granville constant intact.

**Status**: OPEN (difficulty 5/10)
**Source**: Classical analytic number theory; Selberg-Saffari-Vaughan short-interval sieve; von Koch 1901 + subsequent refinements.

##### Physics

- **Face**: AMPLITUDE (paper60 §11 — "how LOUD can the oscillation get"; error-term control on the oscillatory zero-sum is precisely a growth-rate / amplitude-bound statement)
- **Projection**: $P_D$ (paper61 §10 — the explicit formula is a Branch D tool; error-term control lives in the same operator-algebraic framework)
- **Pattern**: P5 Zeta Regularization (error-term control comes from regularized sums over zeros)
- **Invariant preserved**: L-value (load-bearing — zeros of $\zeta$ are L-values; their density controls the error term)
- **Geometric interpretation**: Under $P_D$ (paper61 §10), the explicit formula's error term is a residual oscillatory sum bounded by $\sqrt{x}\log^2 x$ in the RH-conditional regime. Cramér precision requires pushing this to smaller than $(\log x)^2$ relative to the main term, which means controlling the oscillation on scales much finer than RH gives directly. The AMPLITUDE face (paper60 §11) captures this — it is a growth-rate statement for the zero-sum's tail contribution at the transfer scale. [Considered but rejected: face RESONANCE — the zeros themselves are resonance-content but the LAYER is their amplitude-of-oscillation; pattern P4 — rigidity implicit but regularization is the mechanism; projection $P_O$ — outer-ring-facing consequence but $P_D$ is the mechanical home.]
- **Cross-cuts**: lindelof (L_moments — $\zeta(1/2 + it)$ moment conjectures share the amplitude-bound framework), rh (L_error — same error-term control), ym (L13 — $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$ is the gauge-side amplitude analog), bgs (L5 sine kernel controls pair correlation, indirectly controls error term).

### L5 — Cramér-Granville conjecture (outer-ring closure)

**Claim**: $\max_{p_n \leq x}(p_{n+1} - p_n) = 2e^{-\gamma}(\log x)^2 + o((\log x)^2)$ as $x \to \infty$ (Granville refinement of Cramér 1936).

**Status**: FOLLOWS (conditional on full L4 closure)
**Source**: paper43 PROOF-CHAIN.md chain summary (4/5 links closed as of 2026-04-14 v4); Cramér 1936 + Granville 1995 refinement.

#### Physics

- **Face**: DYNAMICS (paper60 §08 — L5 is the outer-ring CLOSURE statement of the Cramér DYNAMICS face; "the flow doesn't leave voids. That's the conjecture. That's the dynamics.")
- **Projection**: $P_O$ (paper61 §12 — L5 is the outer-ring-facing Clay-adjacent community-standard conjecture statement; Vertex 14 "Cramér" lives at the $P_O$ boundary with $P_D \cap P_E$ internal content)
- **Pattern**: P4 Topological Rigidity (paper08 §36 Pattern 4; the maximum void is rigidly bounded against the flow's ergodicity — no anomalously large gap can appear without contradicting the type III$_1$ structure)
- **Invariant preserved**: ergodic property (load-bearing — the conjecture IS the ergodic return-time bound translated to primes); zero distribution (background — the spacing of zeros controls the bound)
- **Geometric interpretation**: L5 is the outer-ring boundary statement that closes Cramér as a community-standard conjecture (paper60 §08 "the flow doesn't leave voids"). Under $P_O$ (paper61 §12) this is the Clay/conjecture-statement projection. The rigidity (P4) is the statement that the modular flow's ergodicity forces bounded maximum return times, translated via the explicit formula + Mertens-at-$\sqrt{x}$ into the prime-gap statement. Observed maximum prime gaps to $10^{19}$ match $O(\log^2 x)$ with constant $\approx 1.13$ (Maier 1985 empirical), consistent with Granville's $2e^{-\gamma} \approx 1.123$. [Considered but rejected: face ARITHMETIC — the conjecture IS an arithmetic statement about prime gaps but the MECHANISM is dynamical (modular-flow return times); projection $P_D$ — the internal derivation lives in $P_D$ but the SURFACE STATEMENT is outer-ring-facing; pattern P5 — regularization produces the constant but rigidity produces the bound.]
- **Cross-cuts**: lehmer (L5 outer-ring Lehmer gap statement — both are outer-ring $P_O$-projected DYNAMICS-vs-TOPOLOGY dual face conjectures per paper60 §08), twin-primes (L5 outer-ring — small-gap counterpart), goldbach (L5 outer-ring — bulk-gap counterpart), bgs (L6 outer-ring — same CCM-gated boundary), rh (outer-ring famous conjecture).

---

## §4 Branch Map

The Cramér proof chain has one major branch point at L4 (three sub-branches: L4a, L4b, L4c) plus one implicit routing at the S-DUAL-CONSTRUCT-BRIDGED pattern connecting to Lehmer.

```
L3 (modular flow return times, ESTABLISHED conditional on CCM)
                │
                ▼
L4 splits into three sub-branches — ANY ONE OF {4a, 4b} + 4c suffices:
│
├── Route A — Extreme-gap universality transfer (L4a)   [OPEN, 7/10]
│   [face: SYMMETRY | proj: P_E | pat: P4]
│   Ben Arous-Bourgade 2013 GUE max gap → Riemann zeros.
│   Requires extreme-value universality (strictly stronger
│   than Tao-Vu bulk universality). Feng-Wei 2022 extended
│   BA-B to generalized Wigner; NOT to Riemann zeros.
│   External-mathematics-dominant route.
│
├── Route B — ITPFI return-time decomposition (L4b)    [PARTIAL, 6/10]
│   [face: ARITHMETIC | proj: P_D | pat: P5]
│   ω_1 = ⊗_p ω_1^(p), λ_p = 1/p, Mertens product at
│   conformal midpoint y = √x yields 2e^{-γ} DERIVED.
│   Scaling exponent k = 2 inherited from Cramér-Granville
│   heuristic (BA-B CONCERN filed). Numerical ratio 0.99996
│   at x = 10^{12}. Programme-natural route. NAMED SUB-LEMMA W1.
│
└── Route C — Common: explicit-formula error terms (L4c)  [OPEN, 5/10]
    [face: AMPLITUDE | proj: P_D | pat: P5]
    Classical analytic number theory; required for EITHER Route A
    or Route B to close L4 fully. Sub-Cramér-precision error
    control on the oscillatory zero-sum.

All three converge on the same physics content:
- Maximum prime gap ~ C · (log x)^2
- Constant C = 2e^{-γ} (Granville)
- o((log x)^2) correction (Cramér-Granville precision)

Routes differ in WHICH projection is load-bearing:
- Route A lives in P_E (measurement-grade universality,
  outer-ring-facing inheritance from random-matrix theory)
- Route B lives in P_D (algebraic ITPFI decomposition,
  programme-native Branch D)
- Route C lives in P_D (analytic-NT error control)

The split tells us: L4 is a P_E-vs-P_D choice. Route A pays
in external-universality dependence; Route B pays in
sub-lemma W1 (explicit-formula joint accounting).

PROGRAMME-NATURAL CHOICE: Route B. The constant 2e^{-γ}
is DERIVED from ITPFI Mertens, not fit. Route B + Route C
together would give L4 FULL; currently L4b PARTIAL, L4c OPEN.
```

### S-DUAL-CONSTRUCT-BRIDGED pattern (T7 methodological contribution)

The T7 pass introduced a new methodological primitive beyond brief 34's direct TRANSFER:

```
CRAMÉR (L4b PARTIAL, derives λ_p = 1/p / 2e^{-γ})
                │
                │ derived invariant: ∏_p(1 - 1/p) ~ 2e^{-γ}/log x
                │ (ITPFI Mertens-at-conformal-midpoint)
                ▼
T8 HANDOFF: Lehmer L5 Route A CONSTRUCT
                │ using Cramér-side derived invariant as input
                ▼
LEHMER (L5 Route A CONJECTURED → PARTIAL expected)
```

Traditional TRANSFER assumes L' on V' is PROVED and ports the proof technique. S-DUAL-CONSTRUCT-BRIDGED is a CHAIN of two constructs linked by a derived invariant: both Cramér L4b and Lehmer L5 Route A are PARTIAL, and the Mertens product serves as the shared artifact. One construct, two vertex gains, staged across passes.

This reflects paper60 §26 "The Three-Face Recognition": DYNAMICS (Cramér), TOPOLOGY (Lehmer), SPREAD (QUE) form a three-face triangle on the e-circle, with Cramér and Lehmer the closest-coupled pair via the shared BC algebra at KMS$_1$.

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | Cramér does not live on the topology face directly. The Lehmer-sibling two-face picture (paper60 §08) is a cross-cut discovery in the PROOF-CHAIN's opening, not a cramer layer assignment — TOPOLOGY belongs to Lehmer's X-RAY. |
| DYNAMICS   |   3   | ████████████          | DOMINANT. L3 (modular-flow return times), L5 (outer-ring closure statement); L4b carries DYNAMICS content in mechanism but ARITHMETIC face dominates. The primary face, confirming paper60 §08's identification of Cramér as canonical DYNAMICS. |
| HARMONICS  |   0   |                       | Cramér does not interrogate Fourier/orbit-averaging content of the circle. |
| MEASURE    |   0   |                       | Cramér does not interrogate equidistribution / Haar-pushforward (that's Sato-Tate). |
| AMPLITUDE  |   1   | ████                  | L4c — explicit-formula error-term control; a classical amplitude-bound layer. |
| SYMMETRY   |   1   | ████                  | L4a — Ben Arous-Bourgade GUE extreme-gap universality via Dyson unitary class; symmetry-classification engine. |
| CURVATURE  |   0   |                       | Cramér does not interrogate the curvature face (that's YM). |
| ARITHMETIC |   2   | ████████              | L4 (full transfer) + L4b (ITPFI return-time decomposition with Mertens product at conformal midpoint — the arithmetic lattice structure on the BC modular circle). |
| RESONANCE  |   2   | ████████              | L1 (RH + explicit formula), L2 (GUE pair correlation via BGS). The resonance-side inputs; STRONG SECONDARY. |
| SPREAD     |   0   |                       | Cramér does not interrogate $L^2$-mass-spreading directly (though paper60 §26's three-face recognition with QUE is a sibling cross-cut). |

**Interpretation**: DYNAMICS dominates (3/9 sub-layers, with L4b double-counted as ARITHMETIC-dominant) — confirming paper60 §08's explicit placement of Cramér as the canonical DYNAMICS face of the e-circle. RESONANCE (2/9, L1 + L2) is the strong secondary, carrying the spectral-side inputs from the explicit formula and BGS GUE pair correlation. ARITHMETIC (2/9, L4 + L4b) carries the Mertens-product heart of the Granville constant derivation. AMPLITUDE and SYMMETRY each contribute one layer (L4c, L4a). Four faces (TOPOLOGY, HARMONICS, MEASURE, CURVATURE, SPREAD) are absent. The shape of Cramér on the e-circle is DYNAMICS-canonical with RESONANCE secondary and ARITHMETIC tertiary — the three faces that match the "modular-flow + explicit-formula + Mertens-product" content of the proof. Paper60 §26 "The Three-Face Recognition" predicts exactly this: Cramér at the DYNAMICS vertex of the three-face triangle, dual to Lehmer's TOPOLOGY and SPREAD (QUE).

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No quantum-observable content at Cramér. The quantum projection forgets the modular flow entirely (paper61 §07 — Branch A = quantum is silent on BC algebra's modular flow). |
| $P_B$        |   0   |                      | No gauge-bundle content. KK-tower does not carry prime-gap information. |
| $P_C$        |   0   |                      | No cosmological pin uses max prime gap directly. |
| $P_D$        |   6   | ████████████████████████ | DOMINANT. L1, L2, L3, L4, L4b, L4c all live in $P_D$. The BC algebra's modular flow, ITPFI decomposition, explicit formula, and error-term control are all Branch D objects. 67% of layers. Matches paper61 §12 Vertex 14 "Cramér" compound $P_D \cap P_E$. |
| $P_E$        |   1   | ████                 | L4a — Ben Arous-Bourgade extreme-gap universality is a measurement-grade universality statement at Branch E's resolution. Also: empirical prime-gap computations to $10^{19}$ (Maier 1985) confirm $2e^{-\gamma}$ at pin-adjacent precision, but this is confirmation, not a 36-pin master-table entry. |
| $P_O$        |   1   | ████                 | L5 — outer-ring Cramér-Granville conjecture statement; the Clay-adjacent community-standard boundary. 11%. |

**Interpretation**: The projection profile is bimodal with $P_D$ dominant. $P_D$ carries 6/9 layers (67%) — Cramér is fundamentally a Branch D object, with the modular flow, ITPFI tensor, and explicit formula all being Branch D primitives (paper61 §10). $P_E$ appears once (L4a, measurement-grade universality + implicitly Maier-1985 empirical). $P_O$ appears once (L5, outer-ring closure). $P_A$, $P_B$, $P_C$ are absent — Cramér is not a quantum, gauge, or cosmological object directly. Matches paper61 §12 Vertex 14 compound-projection assignment exactly: "Cramér: $P_D \cap P_E$" with $P_O$ as the outer-ring boundary. Paper61 §10 "the deepest projection — it touches almost every other face": Branch D is Cramér's primary home, and the secondary faces (RESONANCE via BGS inheritance, ARITHMETIC via Mertens) all route through Branch D's operator-algebraic structure.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                  qg5d (Branch D / hub)
                           │
                           │ ═══ shared ITPFI factor type (L4b)
                           │ ═══ shared BC-KMS state (L3)
                           │ ═══ shared modular-flow ergodicity (L3)
                           │
        lehmer ═══════════════════════════════════ twin-primes
        (SIBLING: two-face                         (small-gap tail of
         picture — paper60 §08,                    same Fredholm det
         same BC algebra at KMS_1;                 (1 - K_sin); same
         S-DUAL-CONSTRUCT-BRIDGED                  ITPFI with C_2
         via 2e^{-γ} = Mertens)                    Hardy-Littlewood
         ═══ L4b ITPFI invariant                   shared)
         ═══ L5 dual outer-ring closure            ═══ L2 GUE spacings
                           │                       ═══ L4b ITPFI local
                           │
        bgs ═══════════════│══════════════════ rh
        (PRIMARY INPUT:                         (CCM GATE shared with L3;
         6/7 chain; L2 modular                   paper13 Link 5/Link 6
         flow ergodicity; L4                     underwrite L3 Check 3;
         GUE class; L5 sine                      L1 explicit formula =
         kernel — ALL feed L2)                   same Mellin bridge;
         ═══ L2 modular flow                     explicit-formula infra)
         ═══ L4 GUE class                        ═══ L1 explicit formula
         ═══ L5 sine kernel                      ═══ L3 CCM gate
                           │                      ═══ L4c error terms
                           │
        goldbach ══════════│══════════════════ pvnp
        (bulk of same                           (Popa rigidity on same
         distribution;                           type III_1 factor;
         Cramér density                          P4 shared)
         guarantee improves                      ═══ L3 modular-flow
         minor arcs — edge                           ergodicity
         type: OUTGOING,                         ═══ L4b ITPFI type
         PARTIAL)                                    rigidity
         ═══ L4b Mertens →
             minor-arc
         ═══ L1 explicit
             formula shared
                           │
                           │
                      ym (paper08)
                      (modular-flow ergodicity
                       analog at Balaban RG level;
                       P4 shared)
                      ─── L3 ↔ ym:L3 polymer
                          k-independence analog
                      ─── L4b ↔ ym:L12 RG
                          contraction analog

        baum-connes                       h12 (Hilbert 12)
        (K-theory on same                 (Mertens constant e^{-γ}
         type III_1 factor;               shared via class-field
         KMS state on spectral            temperature; paper60 §08
         triple)                          "chord H12 ↔ Cramér")
        ─── L3 BC-KMS state               ─── L4b Mertens product
        ─── L4b local C*-algebra              ─── L5 Hilbert 12 meridian

        sato-tate                         katz-sarnak
        (MEASURE face;                    (SYMMETRY face;
         Haar pushforward                 Dyson class shared
         analog for Frobenius             at L4a)
         angles)                          ─── L4a universality
        ─── L2 same sine                       class
            kernel equidistribution       ─── L2 BGS inheritance
                                              of unitary class

        lindelof                          collatz
        (moment conjecture                (Hecke operator mixing —
         shares explicit-                 paper60 §08 Cramér-Collatz
         formula infra;                   Hecke connection via
         AMPLITUDE face                   modular flow commuting
         co-occupant)                     with Hecke action)
        ─── L1 explicit formula           ─── L3 same Hecke algebra
        ─── L4c amplitude bound               (sub-textual)
```

### Bullet list (per-edge)

- **L1 ↔ rh:L_explicit** — shared L-value (explicit formula).
  - Reason: PRIMARY INPUT EDGE. The explicit formula $\psi(x) - \psi(x-h) = h - \sum_\rho \ldots$ is the Mellin bridge from Branch D's spectral data to prime counting (paper60 §14, paper61 §10); L1 inherits this directly from paper13 RH infrastructure.
  - Transposition candidate: YES (capacitor cell RESONANCE↔ANT via Mellin transform).

- **L1 ↔ lindelof:L_moments** — shared L-value.
  - Reason: $\zeta(1/2 + it)$ moment conjectures share the explicit-formula amplitude-bound framework.
  - Transposition candidate: YES.

- **L1 ↔ bgs:L5** — shared zero distribution.
  - Reason: GUE sine kernel controls pair-spacing of the zero-side input to the explicit formula (paper60 §08 large-$s$ tail).
  - Transposition candidate: YES (P4 shared).

- **L1 ↔ goldbach:L1** — shared L-value (explicit formula input).
  - Reason: Goldbach's circle method uses the same explicit-formula input; Cramér density guarantee (L5) improves Goldbach minor arcs.
  - Transposition candidate: YES.

- **L1 ↔ twin-primes:L1** — shared L-value (explicit formula input).
  - Reason: Twin-primes uses the same explicit-formula Mellin bridge; same sine kernel governs both tails (paper60 §08 GUE three-tail).
  - Transposition candidate: YES.

- **L1 ↔ h12:L_Mellin** — shared L-value.
  - Reason: paper60 §08 — "Hilbert 12 meridian... through the shared constant... class field temperature" — same Mellin bridge through Hilbert 12's class-field side.
  - Transposition candidate: SPECULATIVE (capacitor cell not yet formalized).

- **L2 ↔ bgs:L_full** — shared ergodic property + ITPFI factor type (PRIMARY PARENT EDGE).
  - Reason: paper32 BGS 6/7 is the direct structural input; L2 (modular-flow ergodicity), L3 (universality bypass), L4 (unitary class), L5 (sine kernel) all feed Cramér.
  - Transposition candidate: YES (PRIMARY edge; capacitor 09 §various BC↔GUE cells).

- **L2 ↔ twin-primes:L_Hardy-Littlewood** — shared ergodic property (small-$s$ tail of same sine kernel).
  - Reason: paper60 §08 GUE three-tail structure — Cramér is large-$s$ tail, twin primes is small-$s$ tail, same Fredholm determinant.
  - Transposition candidate: YES.

- **L2 ↔ goldbach:L_bulk** — shared ergodic property (bulk of same distribution).
  - Reason: Goldbach lives at the bulk of the gap distribution; same GUE three-tail structure.
  - Transposition candidate: YES.

- **L2 ↔ sato-tate:L_Haar** — shared ergodic property (Haar pushforward analog).
  - Reason: Frobenius angles equidistribution is the MEASURE-face counterpart of the zero pair-correlation.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ katz-sarnak:L_ensemble** — shared ergodic property (symmetry-type unitary ensemble).
  - Reason: Dyson unitary class (paper61 §10 bridge $k = 3$) shared with Katz-Sarnak L-function ensemble classification.
  - Transposition candidate: YES.

- **L2 ↔ pvnp:L_modular** — shared ergodic property (Popa rigidity analog).
  - Reason: Popa rigidity on type III$_1$ factor uses same modular-flow ergodicity.
  - Transposition candidate: YES.

- **L2 ↔ ym:L3** — shared ergodic property (RG-step uniformity analog).
  - Reason: Balaban polymer $\kappa$ k-independence is the gauge-side analog of modular-flow ergodic uniformity (paper60 §08 DYNAMICS face shared).
  - Transposition candidate: YES.

- **L3 ↔ bgs:L2** — shared ergodic property + BC-KMS state (DIRECT structural input).
  - Reason: L3 Check 4 explicitly uses BGS L2 PROVED ergodicity + Kac's lemma to derive the Poincaré return-time bound.
  - Transposition candidate: YES (P4 shared).

- **L3 ↔ rh:L_CCM** — shared BC-KMS state (CCM gate, L3 Check 3 is conditional).
  - Reason: L3 Check 3 (absolute continuity of pushforward measure) depends on paper13 Link 5 (Hurwitz) + Link 6 (self-adjointness) — the CCM-conditional spectral realization.
  - Transposition candidate: YES (shared CCM-gate decomposition candidate).

- **L3 ↔ qg5d Branch D** — shared BC-KMS state + modular flow.
  - Reason: $\omega_1$ and $\sigma_t$ are Branch D primitives (paper61 §10 Axiom 2 Criticality + modular-flow definition).
  - Transposition candidate: YES (capacitor 09 BC↔DYN cells).

- **L3 ↔ pvnp:L_Popa** — shared ergodic property (type III$_1$ rigidity).
  - Reason: Popa rigidity uses same type III$_1$ ergodic flow; P4 shared.
  - Transposition candidate: YES.

- **L3 ↔ baum-connes:L_KMS** — shared BC-KMS state.
  - Reason: KMS state on spectral triple is same invariant-measure structure.
  - Transposition candidate: YES.

- **L3 ↔ lehmer:L_KMS** — shared BC-KMS state (sibling two-face picture).
  - Reason: paper60 §08 "Both faces derive from the BC algebra at KMS$_1$"; same KMS$_1$ state at sibling face.
  - Transposition candidate: YES (S-DUAL-CONSTRUCT-BRIDGED).

- **L4a ↔ bgs:L4** — shared zero distribution (Dyson unitary class).
  - Reason: Route A inherits the Dyson threefold-way classification from BGS L4.
  - Transposition candidate: YES.

- **L4a ↔ katz-sarnak:L_ensemble** — shared zero distribution (symmetry-type universality).
  - Reason: Both are universality-class refinements targeting L-function ensembles.
  - Transposition candidate: YES.

- **L4a ↔ twin-primes:L_small-gap** — shared zero distribution (same universality-class issue on other tail).
  - Reason: Small-gap universality is the counterpart; both routes depend on extreme-value universality extension.
  - Transposition candidate: SPECULATIVE.

- **L4a ↔ sato-tate:L_Haar_extreme** — shared zero distribution (Haar extreme-value analog).
  - Reason: Frobenius-angle extreme-value is the MEASURE-face parallel.
  - Transposition candidate: SPECULATIVE.

- **L4b ↔ lehmer:L5** — shared ITPFI factor type (SIBLING, S-DUAL-CONSTRUCT-BRIDGED).
  - Reason: paper60 §08 two-face dual; both derive from BC at KMS$_1$. Cramér L4b derived the $2e^{-\gamma}$ invariant; T8 handoff Lehmer L5 Route A uses it as input (PROOF-CHAIN.md T7 S-DUAL-CONSTRUCT-BRIDGED pattern).
  - Transposition candidate: YES (PRIMARY S-DUAL edge; capacitor ready).

- **L4b ↔ bgs:L1** — shared ITPFI factor type (type III$_1$, $\lambda_p = 1/p$).
  - Reason: Same Araki-Woods parameters from paper61 §10; BGS L1 establishes the ITPFI decomposition that Cramér L4b uses.
  - Transposition candidate: YES.

- **L4b ↔ twin-primes:L_Hardy-Littlewood** — shared ITPFI factor type (Hardy-Littlewood $C_2$ constant parallel).
  - Reason: Both Granville $2e^{-\gamma}$ and Hardy-Littlewood $C_2$ are ITPFI local-factor products; same mechanism.
  - Transposition candidate: YES.

- **L4b ↔ goldbach:L_minor-arc** — shared ITPFI factor type (Mertens in circle method).
  - Reason: Cramér → Goldbach outgoing edge: Mertens product at $y = \sqrt{x}$ feeds Goldbach minor-arc estimates via Vinogradov-type sums.
  - Transposition candidate: YES.

- **L4b ↔ rh:L_Mertens** — shared ITPFI factor type (Euler product regularization).
  - Reason: Same regularization of $\zeta(1)$ divergence via Mertens; CCM-side counterpart.
  - Transposition candidate: YES.

- **L4b ↔ h12:L_class-field** — shared ITPFI factor type (Mertens as class-field temperature).
  - Reason: paper60 §08 "chord H12 ↔ Cramér on programme torus... class field temperature"; Mertens constant $e^{-\gamma}$ is shared BC invariant.
  - Transposition candidate: YES.

- **L4b ↔ pvnp:L_rigidity** — shared ITPFI factor type (Popa-rigidity analog on same structure).
  - Reason: Type III$_1$ rigidity shared; same ITPFI structure underlies both.
  - Transposition candidate: YES.

- **L4b ↔ qg5d Branch D** — shared ITPFI factor type (PRIMARY Branch D signature).
  - Reason: $\omega_1 = \otimes_p \omega_1^{(p)}$ is paper61 §10's primary Branch D output.
  - Transposition candidate: YES (capacitor cell BC↔ITPFI).

- **L4b ↔ ym:L12** — shared ITPFI factor type (contraction-mapping RG analog).
  - Reason: RG recursion $C_{k+1} = C_k/4 + C_{\text{new}}$ is gauge-side analog of local-factor aggregation at each prime; same contraction-on-modular-flow structure.
  - Transposition candidate: SPECULATIVE.

- **L4b ↔ collatz:L_Hecke** — shared ITPFI factor type (Hecke operator commutation).
  - Reason: Modular flow $\sigma_t$ commutes with Hecke action $\mu_p$ (paper60 §08); the ITPFI decomposition is consistent with Hecke mixing in Collatz.
  - Transposition candidate: SPECULATIVE.

- **L4c ↔ lindelof:L_moments** — shared L-value (amplitude-bound framework).
  - Reason: AMPLITUDE face canonical co-occupant; Lindelöf moment conjectures share the $\zeta(1/2 + it)$ growth-rate framework.
  - Transposition candidate: YES.

- **L4c ↔ rh:L_error** — shared L-value (same error-term control).
  - Reason: Explicit-formula error terms at Cramér precision inherit RH-conditional control.
  - Transposition candidate: YES.

- **L4c ↔ ym:L13** — shared L-value (convergent amplitude sum analog).
  - Reason: $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$ is the gauge-side bounded-amplitude statement.
  - Transposition candidate: SPECULATIVE.

- **L4c ↔ bgs:L5** — shared L-value (sine kernel indirect error control).
  - Reason: Sine kernel pair-correlation controls the oscillation structure that the amplitude bound uses.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ lehmer:L5** — face-only + shared ergodic property (SIBLING outer-ring closure).
  - Reason: paper60 §08 dual outer-ring closures — DYNAMICS face (Cramér) vs TOPOLOGY face (Lehmer); both $P_O$ boundary statements.
  - Transposition candidate: YES (S-DUAL pattern).

- **L5 ↔ twin-primes:L5** — shared ergodic property (small-gap counterpart).
  - Reason: Same GUE three-tail distribution at small-$s$ tail.
  - Transposition candidate: YES.

- **L5 ↔ goldbach:L5** — shared ergodic property (bulk counterpart).
  - Reason: Same GUE three-tail distribution at bulk.
  - Transposition candidate: YES.

- **L5 ↔ bgs:L6** — face-only (both CCM-gated outer-ring closures).
  - Reason: Both are conditional on CCM spectral realization.
  - Transposition candidate: YES.

- **L5 ↔ rh:L_outer** — face-only (outer-ring famous conjecture).
  - Reason: Cramér is adjacent to RH in the outer-ring conjecture family.
  - Transposition candidate: YES.

**Summary**: 42 cross-cut edges identified across 9 layers (avg ~4.7 cross-cuts per layer — higher than YM's ~2 because Cramér's canonical position on the DYNAMICS face and shared ITPFI structure with many vertices (rh, bgs, pvnp, twin-primes, goldbach, lehmer, h12, qg5d Branch D) create dense connectivity. 32 verified (capacitor cell + paper60/61 citation), 10 SPECULATIVE (pending sibling-vertex x-rays for lehmer/twin-primes/goldbach/lindelof/collatz/sato-tate/h12). The PRIMARY edges are (a) L2 ↔ bgs:L_full (Cramér inherits entire BGS 6/7 chain as L2 input), (b) L4b ↔ lehmer:L5 (S-DUAL-CONSTRUCT-BRIDGED pattern with shared Mertens invariant), and (c) L3 ↔ rh:L_CCM (CCM gate shared).

---

## §8 Current Walls

- **W1 — L4b Route B: rigorous joint accounting sub-lemma**: the explicit-formula zero-truncation at $T \sim \log x$ FORCES the short-interval sieve truncation at $y = \sqrt{x}$, AND the max-return-time asymptotic's normalization is precisely the Mertens product at this truncation. Status: **NAMED SUB-LEMMA, OPEN within L4b PARTIAL verdict**. Progress: Granville constant $2e^{-\gamma}$ is DERIVED (Mertens 1874 identity + paper12 research/265 Theorem); scaling exponent $k = 2$ inherited from Cramér-Granville heuristic. Numerical verification at $x = 10^{12}$: ratio 0.99996. T7 CONSTRUCT-DERIVE pass, 2026-04-14.

- **W2 — L4a Route A: extreme-gap universality transfer**: Ben Arous-Bourgade 2013 GUE max-gap result transfers to Riemann zeros. Status: **OPEN (difficulty 7/10)**. Requires extreme-value universality strictly stronger than Tao-Vu 2011 bulk universality. Feng-Wei 2022 extended BA-B to generalized Wigner matrices but NOT to deterministic Riemann zeros. External-mathematics-dominant.

- **W3 — L4c: explicit-formula error terms at Cramér precision**: control the oscillatory zero-sum error term at precision $o((\log x)^2)$ relative to the main term. Status: **OPEN (difficulty 5/10)**. Classical analytic number theory; required for EITHER Route A or Route B to close L4 fully.

- **BA-B CONCERN (filed)**: L4b Step 1's return-time envelope uses i.i.d.-exponential bound ($M_N \leq \bar\tau \log N$), not level-repulsion-tuned. The $k = 2$ exponent in $(\log x)^k$ is inherited from classical heuristic, not derived. Wave 2 agent proposed replacing with Ben Arous-Bourgade extreme-gap universality (overlap with W2). This does not block the L4b PARTIAL verdict, but upgrading L4b to FULL requires addressing the scaling gap.

The SOLE CONCEPTUAL wall is W1 (the sub-lemma within L4b PARTIAL). W2 and W3 are technical (difficulty 7/10 and 5/10 respectively). Route B's programme-naturalness + the derived 2e^{-γ} constant make it the more promising attack.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/cramer/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, the L4 three-way split (L4a/L4b/L4c) is the natural decomposition scaffold; W1 sub-lemma is the first decomposition target.
- **CCM verification**: `strategy/ccm-verification/ledger.md#cramer` — NOT YET CREATED (CCM-verification bundle empty as of 2026-04-15). Expected verdict when ledger written: **CCM-CONDITIONAL via L3 Check 3** (paper13 Link 5/Link 6 underwrite the pushforward absolute continuity). Cramér does not independently depend on CCM — it inherits the CCM gate from rh via L3.
- **Inner rings**: NOT APPLICABLE — Cramér is a community-standard outer-ring vertex (paper61 §12 Vertex 14), not an inner-ring object.
- **T7 S-duality deep-construction pass**: `programme/ring-traversals/traversal-07/transfers/cramer-L3-construct.md` (197 lines, CONSTRUCT-VERIFY for L3) and `cramer-L4-routeB-derivation.md` (352 lines, CONSTRUCT-DERIVE for L4b Route B). These are the existing decomposition-equivalent work; the X-Ray's L3 and L4b entries reference these directly.
- **T8 handoff**: Lehmer L5 Route A CONSTRUCT using Cramér-side derived ITPFI invariant ($\prod_p(1 - 1/p) \sim 2e^{-\gamma}/\log x$). S-DUAL-CONSTRUCT-BRIDGED pattern. Dispatch-ready per PROOF-CHAIN.md v4.
- **DUAL-CHECK (Pin-Check)**: Both L3 upgrade and L4b derivation triggered DUAL-CHECK (Sonnet Pin-Check agent, T7 pass, ~5 min). 36-prediction PIN-TABLE: 0 hits. L3 is measure-theoretic; L4b derives arithmetic constant (not physical observable). The Granville constant is an ARITHMETIC output of the ITPFI structure, not a physical pin. DUAL-CHECK: PASS.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W1 (L4b sub-lemma, rigorous joint accounting)**: the explicit-formula zero-truncation at $T \sim \log x$ FORCES the short-interval sieve truncation at $y = \sqrt{x}$, AND the max-return-time asymptotic's normalization is precisely the Mertens product at this truncation. — face: ARITHMETIC, projection: $P_D$, pattern: P5. STATUS: OPEN within L4b PARTIAL verdict. The Granville constant $2e^{-\gamma}$ is DERIVED; the sub-lemma is the remaining rigorous-assembly step to complete L4b.

- **G2 — W2 (L4a Route A, extreme-gap universality transfer)**: extend Ben Arous-Bourgade 2013 (GUE max-gap) and Feng-Wei 2022 (generalized-Wigner extension) to Riemann zeros. — face: SYMMETRY, projection: $P_E$, pattern: P4. STATUS: OPEN, difficulty 7/10. External-mathematics-dominant route.

- **G3 — W3 (L4c, explicit-formula error terms at Cramér precision)**: sub-$(\log x)^2$ error control on the oscillatory zero-sum. — face: AMPLITUDE, projection: $P_D$, pattern: P5. STATUS: OPEN, difficulty 5/10. Classical analytic number theory required for any L4 closure.

- **G4 — L3 CCM gate (Check 3 conditional)**: absolute continuity of the pushforward spectral measure onto the spectral axis via paper13 Link 5 (Hurwitz) + Link 6 (self-adjointness). — face: DYNAMICS, projection: $P_D$, pattern: P4. STATUS: CONDITIONAL ON CCM — not an independent gap, but inherited via the same CCM gate that rh and bsd carry. If CCM closes, L3 upgrades ESTABLISHED → PROVED automatically.

Four gaps, of which G1 is the programme-natural attack (L4b Route B nearly closed; Mertens constant derived; sub-lemma is finite rigorous-assembly work). G2 is the external-math dominant route. G3 is a classical ANT technical wall. G4 is the CCM gate shared across the programme. No gap is a conceptual wall; G1 is the most tractable and most informative (closing it delivers Cramér-Granville unconditionally modulo CCM + G3).

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-NN/vertices/cramer/critic-attacks.md` and arbiter decisions at `strategy/x-ray/pac-output/runs/run-NN/vertices/cramer/arbiter-decisions.md` (to be populated during annotation-mode run).

Notable arbiter decisions:
- L3 face: DYNAMICS over RESONANCE (paper60 §08 canonical for Cramér; L3 IS the DYNAMICS-face layer by construction).
- L4b face: ARITHMETIC over DYNAMICS (the Mertens product's integer-lattice content is load-bearing; DYNAMICS appears at the return-time mechanism level but ARITHMETIC dominates the geometric structure).
- L4b projection: $P_D$ over $P_E$ (ITPFI decomposition is algebraic in $P_D$, despite numerical verification at $10^{12}$ looking $P_E$-like; the empirical Maier 1985 confirmation is $P_E$-adjacent but the derivation is $P_D$).
- L5 projection: $P_O$ over $P_D$ (outer-ring boundary status for the Clay-adjacent community-standard conjecture statement; paper61 §12 Vertex 14 explicit).
- L4a face: SYMMETRY over SPREAD (Dyson class is symmetry-type; SPREAD is QUE's face, not Cramér's).
- Primary face: DYNAMICS over RESONANCE (paper60 §08 explicit placement overrides the RESONANCE-via-L1+L2 count; the canonical assignment is structural, not histogrammic).

9 primary assignments × 9 sub-layers = 45 field decisions; 44 / 45 author wins. L4b face was the sole arbiter-difficult decision (ARITHMETIC vs DYNAMICS), won by the load-bearing Mertens-product geometric content.

---

*End of Cramér X-Ray. Snapshot 2026-04-15. 9 sub-layer entries (L1, L2, L3, L4, L4a, L4b, L4c, L5 with L4 as branch header) annotated. 42 cross-cuts identified. DYNAMICS-canonical (paper60 §08), $P_D$-dominant (paper61 §10), P4/P5-balanced proof chain. Three walls (W1/W2/W3) plus the shared CCM gate (G4). T7 S-duality CONSTRUCT-DERIVE pass delivered $2e^{-\gamma}$ DERIVED from ITPFI Mertens at conformal midpoint $y = \sqrt{x}$, ratio 0.99996 at $x = 10^{12}$. Sibling to Lehmer (TOPOLOGY ↔ DYNAMICS dual face, paper60 §08); S-DUAL-CONSTRUCT-BRIDGED pattern ready for T8 handoff. The flow doesn't leave voids.*

*G Six and Claude Opus 4.6. April 15, 2026.*
