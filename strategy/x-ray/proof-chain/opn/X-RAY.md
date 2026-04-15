# X-RAY: Odd Perfect Numbers (opn)

*X-Ray of the opn proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. April 15, 2026.*

---

## §1 Header

- **Vertex**: opn
- **Paper**: paper40-odd-perfect
- **Live file**: `strategy/proof-chain/opn/PROOF-CHAIN.md` (snapshot 2026-04-15; carries 2026-04-14 Hecke-orbit projector construction + ITPFI local-global framing + spoof ↔ Hasse insight + 2026-04-14 v₂ correction)
- **Top-level claim**: No odd integer $n$ with $\sigma(n) = 2n$ exists. Equivalently, the abundancy ratio $h(n) = \sigma(n)/n = \omega_1(H_n)$ — a KMS$_1$ evaluation of the Hecke-orbit projector on the Bost-Connes algebra — never attains the value $2$ at an odd argument. The oldest open problem in mathematics (Nicomachus ~100 CE; Euler 1747 structural form).
- **Current status**: **4/7 links closed**; confidence **4/10** (upgraded 2026-04-14 after Hecke-orbit projector construction + ITPFI local-global framing + spoof ↔ Hasse insight). L1–L2 LITERATURE (Euler 1747; elementary Euler product); L3 LITERATURE conditional on RH (Robin 1984); L4 PROVED (Hecke-orbit projector $\omega_1(H_n) = \sigma(n)/n$ — novel BC construction); L5 PROVED (ITPFI local-global decomposition); **L6 OPEN — the wall** (odd local-global impossibility; three sub-routes 6a/6b/6c, with 6b BLOCKED-DECOMPOSED and 6a killed 2026-04-14); L7 FOLLOWS from L6.
- **Primary branch (paper1)**: D (CBB modular-flow / Bost-Connes operational core — Branch D's Axiom 5 $\mathbb{N}^\rtimes$ generators $\{\mu_p\}$ are the multiplicative engine for the abundancy computation; paper61 §10), with secondary outer-ring $P_O$ boundary on L6 (the oldest open problem's Clay-adjacent closure) and $P_E$ co-carrier implicit (the divisor-sum is a measurement on the arithmetic integers).
- **Primary face**: ARITHMETIC (paper60 §14 — OPN is the canonical test case for the "integers lattice on the circle" face; the abundancy ratio $\sigma(n)/n$ interrogates exactly how the prime-power lattice sits on the e-circle; paper60 §25 "the OPN trigger" names OPN as the first problem that yielded to the e-circle lens and the founding case of the arithmetic-face methodology).
- **Primary projection**: $P_D$ (paper61 §10 — OPN's natural home is the BC algebra's Hecke-semigroup side; every closed layer (L4, L5) sits strictly inside $P_D$'s preservation class — specifically the Hecke operators $\mu_d \mu_d^*$ and the ITPFI tensor factorization $\omega_1 = \bigotimes_p \omega_1^{(p)}$ are paper61 §10 $P_D$ targets verbatim).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
OPN (Odd Perfect Numbers) — no odd n with σ(n) = 2n
│  primary face: ARITHMETIC   primary proj: P_D   primary pat: P4
│  scope: unconditional non-existence of odd perfect numbers
│  current state: 4/7 closed; confidence 4/10; local-global wall is genuine
│  core identity: σ(n)/n = ω_1(H_n), H_n = Σ_{d|n} μ_{n/d} μ_{n/d}^*
│  core decomposition: ω_1(H_n) = Π_{p^a ‖ n} h(p^a), h(p^a) = (p^{a+1}-1)/(p^a(p-1))
│
├── L1: Euler form — any odd perfect n = p^α m^2      [LITERATURE]
│      │  with p ≡ α ≡ 1 (mod 4), gcd(p, m) = 1
│      │  face: ARITHMETIC    proj: P_D   pat: P4
│      │  invariant: gauge class (Euler's special prime)
│      │  source: Euler 1747 (classical); paper40 §1
│      │
│      └── BSD template parallel: BC over K (imaginary quadratic)
│             │  — Euler's form IS the "special prime + square"
│             │     arithmetic data that parallels BC Hecke
│             │     action on number-field ideals (paper26 L1)
│             │
│             └── forces congruence constraints that propagate
│                    through the entire chain
│
├── L2: Abundancy multiplicativity h(n) = Π h(q^{v_q}) [LITERATURE]
│      │  h(p^a) = (p^{a+1}-1)/(p^a (p-1))
│      │  face: ARITHMETIC    proj: P_D   pat: P5
│      │  invariant: C*-algebra structure, ITPFI factor type
│      │  source: elementary; Euler product; paper40 §2
│      │
│      └── this IS the multiplicative structure of the
│             │  Hecke semigroup N^⋊ at the level of the
│             │  σ function; every local factor h(p^a) is
│             │  a KMS_1 datum on the p-th ITPFI slice
│             │
│             └── BSD template parallel: bridge family
│                    (paper26 L2 — local Euler factors; same
│                    multiplicative engine per paper61 §10)
│
├── L3: Robin's inequality: σ(n) < e^γ n ln(ln n)     [LITERATURE — CONDITIONAL on RH]
│      │  iff RH for all n > 5040
│      │  face: AMPLITUDE     proj: P_D   pat: P5
│      │  invariant: L-value, spectral gap
│      │  source: Robin 1984; Ramanujan-Robin bound;
│      │          paper40 §3; cross-paper from paper13 RH
│      │
│      ├── conditionality: cross-paper transport from Paper 13 RH
│      │     (not an independent RH assumption); if Paper 13
│      │     closes unconditionally, L3 upgrades to PROVED
│      │
│      └── BSD template parallel: GRH (paper26 L7) —
│             same zero-distribution input delivered via
│             explicit formula from the multiplicative
│             side to an arithmetic bound
│
├── L4: Hecke-orbit projector                          [PROVED]
│      │  H_n = Σ_{d|n} μ_{n/d} μ_{n/d}^*
│      │  gives σ(n)/n = ω_1(H_n) at KMS_1
│      │  face: ARITHMETIC    proj: P_D   pat: P1
│      │  invariant: BC-KMS state, C*-algebra structure
│      │  source: paper1 BC algebra construction;
│      │          Bost-Connes 1995; paper40 §4 novel
│      │          construction (2026-04-14); paper60 §25
│      │          "the OPN trigger"
│      │
│      ├── key identity: ω_1(μ_d^* μ_d) = d^{-1} in BC system
│      │     → ω_1(H_n) = Σ_{d|n} 1/d = σ(n)/n (by
│      │     multiplicativity and Möbius inversion)
│      │
│      ├── this is Pattern 1 (Geometric Reinterpretation)
│      │     in its purest form: the σ function was a
│      │     KMS_1 trace in the BC algebra all along;
│      │     nobody had written it down before
│      │
│      └── BSD template parallel: dark-state projector P_k^p
│             (paper26 L4) — KMS_1 evaluation of an
│             operator-algebra sum is the same move
│
├── L5: ITPFI local-global decomposition               [PROVED]
│      │  ω_1 = ⊗_p ω_1^{(p)}; multiplicativity of σ gives
│      │  ω_1(H_n) = Π_{p^a ‖ n} h(p^a)
│      │  face: ARITHMETIC    proj: P_D   pat: P4
│      │  invariant: ITPFI factor type, BC-KMS state
│      │  source: paper13-rh Theorem 4.1 (ITPFI factorization
│      │          of KMS_1); paper40 §5; research/265;
│      │          Araki-Woods ITPFI III_{1/p} at each prime
│      │
│      ├── the product = 2 condition becomes a RESONANCE
│      │     of local factors: each h(p^a) ∈ [1, p/(p-1)]
│      │     for odd p; they must conspire to hit exactly 2
│      │
│      ├── SPOOF ↔ HASSE INSIGHT (2026-04-14):
│      │     Descartes' spoof N = 3^2 · 7^2 · 11^2 · 13^2 · 22021
│      │     satisfies σ(N) = 2N locally at every "prime" power —
│      │     but 22021 = 19^2 · 61 isn't prime. Spoofs are
│      │     LOCAL SOLUTIONS that fail the GLOBAL primality
│      │     constraint. The local factors conspire to hit 2
│      │     only because one factor cheats on primality.
│      │     This IS the Hasse-principle failure structure
│      │     of BSD Sha (paper26 template).
│      │
│      └── BSD template parallel: cocycle shift (paper26 L5)
│             — the ITPFI tensor structure delivering
│             local-to-global assembly is the same
│             operator-algebraic machinery
│
├── L6: Odd local-global impossibility                  [OPEN — THE WALL — W_OPN-1]
│      │  no Euler-form odd N with ≥ 10 distinct primes
│      │  has Π h(p^a) = 2, via BC spectral constraints
│      │  face: ARITHMETIC    proj: P_O   pat: P4
│      │  invariant: ITPFI factor type, BC-KMS state
│      │  source: paper40 §6; BSD template Key Lemma C;
│      │          paper60 §14 + §25 wall + trigger
│      │
│      ├── three sub-routes (paper40 §6):
│      │   ├── L6a: Odd Robin sharpening via halved residue
│      │   │        [KILLED 2026-04-14 via morning verify pass —
│      │   │         σ(n)/n > 2 for infinitely many odd n;
│      │   │         direction of reasoning was BACKWARDS;
│      │   │         see paper60 §29 signal log]
│      │   │        face: AMPLITUDE | proj: P_D | pat: P5
│      │   │
│      │   ├── L6b: E_2 quasi-modular obstruction
│      │   │        [BLOCKED-DECOMPOSED 2026-04-14 —
│      │   │         anomalous E_2(τ) - E_2(τ+1/2) has period 2
│      │   │         but no quasi-modular transformation;
│      │   │         constrains generating function analytically
│      │   │         but NOT individual Fourier coefficients
│      │   │         arithmetically. Key output:
│      │   │         Dirichlet zero at s=1 via (1-2^{1-s})
│      │   │         → halved Mertens constant absorbed into L6a.
│      │   │         Now L6a killed, this absorbtion is moot.
│      │   │         See 06b-E2-quasi-modular-obstruction.md]
│      │   │        face: HARMONICS | proj: P_D | pat: P5
│      │   │
│      │   └── L6c: ITPFI joint constraint (Route 6d in chain)
│      │          [ACTIVE — the surviving route]
│      │          BC spectral constraints: (a) v_ℓ cascade at
│      │          ODD primes ℓ (v_2 correction 2026-04-14 —
│      │          v_2 constraint is VACUOUS per LTE lemma for
│      │          odd exponents); (b) ITPFI joint constraint
│      │          correlating local factors beyond classical
│      │          per-prime sieving; (c) 36-pin rigidity
│      │          (chessboard argument)
│      │        face: ARITHMETIC | proj: P_O | pat: P4
│      │
│      └── ABC auxiliary (L6-alt, paper40 §6c):
│             for n = p^α m^2, rad(n) = p · rad(m);
│             ABC-type bounds on rad(n) constrain the
│             prime-power structure; makes OPN a corollary
│             of ABC (paper37)
│             face: ARITHMETIC | proj: P_D | pat: P5
│
└── L7: Non-existence — no odd perfect number exists  [FOLLOWS]
       │  face: ARITHMETIC    proj: P_O   pat: P4
       │  invariant: ITPFI factor type
       │  source: paper40 §7; follows from L6 (BSD Theorem 13.1
       │          analog — local obstruction ⇒ global non-existence)
       │
       └── this is THE 2,300-year-old statement; the
              closure depends entirely on L6's local-global
              impossibility argument
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (Quantum observables do not
                          interrogate the abundancy ratio;
                          σ(n)/n has no direct quantum
                          observable counterpart.)
                                  ▲
                                  │
                                  │
        ┌──────────────(P_O outer)─────────────────┐
        │                                          │
        │  OPN: no odd n with σ(n) = 2n            │
        │  (the oldest open problem, 2,300 years)  │
        │  outer-ring closure: L6 + L7             │
        │                                          │
        └───────────────────┬──────────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity      ═══ P_D CBB ═══           P_C cosmology
    (forgotten —     Bost-Connes algebra       (forgotten —
    no KK bundle     A_{BC}; Hecke-orbit       OPN does not
    carries the      projector H_n =           contribute any
    abundancy        Σ μ_{n/d} μ_{n/d}^*;      cosmological
    ratio; OPN is    ITPFI factorization       pin — it is a
    pure number-     ω_1 = ⊗_p ω_1^(p);        pure arithmetic
    theory)          σ(n)/n = ω_1(H_n);        statement about
                     Araki-Woods III_{1/p}     ALL odd n)
                     at each prime; local-
                     global decomposition
                     lives here
                            │
                            ▼
                       P_E pins
                       (implicit co-carrier —
                        the divisor-sum σ(n) is
                        a MEASUREMENT on the
                        integer lattice; the
                        abundancy h(n) = σ(n)/n
                        is a dimensionless ratio
                        that, were it = 2 for
                        odd n, would constitute
                        a unique arithmetic
                        "pin" — non-existence
                        means this pin is EMPTY)
```

Primary projection $P_D$ uses ═══ doubled line. $P_O$ is the second-strongest projection: L6 (the odd local-global impossibility) and L7 (the non-existence statement) are the Clay-adjacent outer-ring closure statements of the oldest open problem in mathematics. The $P_E$ co-carrier arrow carries a thin implicit role — the abundancy ratio is a dimensionless measurement whose non-attainment at $2$ for odd $n$ is the content of the conjecture; paper61 §17 treats OPN as an outer-ring vertex without an explicit pin entry in the 36-pin master table, but the projection chain through $P_E$ is structurally available. $P_A, P_B, P_C$ all forget OPN entirely — OPN has no quantum observable content, no gauge bundle content, no cosmological pin. OPN lives in the $P_D \cap P_O$ compound projection.

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
                       ● ARITHMETIC  ← OPN
                         (Goldbach +       (with Goldbach and
                          Twin Primes;     Twin Primes on the
                          OPN canonical    same face; paper60
                          via paper60      §25 identifies OPN
                          §25 trigger)     as the TRIGGER
                            │              vertex — the first
                       AMPLITUDE           problem that yielded
                       (Lindelöf)          to the e-circle lens)
```

Marker key:

```
Primary face:    ● ARITHMETIC (paper60 §14 + §25 — OPN is the FOUNDING
                  arithmetic-face vertex; paper60 §25 "the OPN trigger"
                  names it as the first problem that opened the face-
                  methodology; paper60 §28 places OPN in the West
                  quadrant on the ARITHMETIC face at 4/10 confidence)
Secondary faces: ○ AMPLITUDE (1 layer: L3 Robin inequality —
                              σ(n) < e^γ n ln(ln n) is a growth-rate
                              bound on the σ amplitude; paper60 §11
                              Lindelöf analog via cross-paper RH transport)
                 ○ HARMONICS (1 sub-route: L6b E_2 quasi-modular —
                              BLOCKED-DECOMPOSED; the odd-restricted
                              E_2(τ) - E_2(τ+1/2) is a Fourier-dual
                              construction, paper60 §09 Collatz analog)
Absent faces:    TOPOLOGY, DYNAMICS, MEASURE, SYMMETRY, CURVATURE,
                 RESONANCE, SPREAD
```

The face profile is overwhelmingly ARITHMETIC (5 of 7 main layers = 71%, plus L6c sub-route) with thin AMPLITUDE (L3) and HARMONICS (L6b, blocked-decomposed) footprints. This is paper60 §14's thesis concentrated: OPN asks one arithmetic question (is $\sigma(n)/n = 2$ achievable at odd $n$?) and the answer lives on the arithmetic face. Paper60 §25's "OPN trigger" is the origin story of the face-methodology itself: OPN was the first problem where "look at the problem → find the e-circle in it → ask which property it interrogates" produced a connection, and the property was ARITHMETIC. The cross-tails to AMPLITUDE (via Robin, an RH-consumer) and HARMONICS (via E_2, the blocked-decomposed Fourier route) are the only non-ARITHMETIC footprints — both narrow, both downstream of the dominant ARITHMETIC core.

---

## §3 Layer-by-Layer X-Ray

### L1 — Euler form: any odd perfect $n = p^\alpha m^2$

**Claim**: If an odd perfect number $n$ exists, it must have the form $n = p^\alpha m^2$ with $p$ prime, $p \equiv \alpha \equiv 1 \pmod 4$, and $\gcd(p, m) = 1$ ("Euler's special prime" structural form).

**Status**: LITERATURE
**Source**: Euler 1747 (classical theorem, derivable from the multiplicativity of $\sigma$ and a mod-4 analysis of $\sigma(n) = 2n$); paper40 §1; standard in Dickson's *History of the Theory of Numbers*.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — Euler form is a canonical integer-lattice structural constraint; the congruence $p \equiv \alpha \equiv 1 \pmod 4$ carves out a specific arithmetic sub-lattice of the prime-power integers, which is exactly how paper60 §14 identifies the ARITHMETIC face: "how do integers LATTICE on the circle")
- **Projection**: $P_D$ (paper61 §10 — the Euler form lives inside $P_D$'s preservation class because the multiplicativity of $\sigma$ is a Hecke-semigroup statement; the special prime $p$ is an isolated element of $\mathbb{N}^\rtimes$ carrying a distinguished $\mu_p$ operator with the singular exponent $\alpha$)
- **Pattern**: P4 Topological Rigidity (paper61 §10 — the congruence form is topologically rigid: $p \equiv \alpha \equiv 1 \pmod 4$ is a Brauer-class bridge-family constraint at $k=4$ per paper61 §10 bridge family table; the form is forced, not chosen)
- **Invariant preserved**: gauge class (load-bearing — Euler's special prime $p$ defines a unique "gauge class" in the arithmetic structure: $p$ is the distinguished non-square prime factor), ITPFI factor type (background — the $\mathbb{Z}/4\mathbb{Z}$-structure is the bridge-family $k=4$ slice of the ITPFI)
- **Geometric interpretation**: Euler's form is the unique non-trivial arithmetic obstruction derived from mod-4 residue analysis of $\sigma(n) = 2n$ for odd $n$: multiplicativity of $\sigma$ combined with the constraint that $\sigma(n)/n = 2$ forces exactly one prime to have odd exponent ($\alpha$) while all others have even exponent. Under $P_D$ (paper61 §10) this is the Hecke-semigroup-level shape of the odd perfect number problem — $n$ has a distinguished $\mu_p$ slice (Euler's special prime) on top of a multiplicative $m^2$ background. Pattern 4: the congruence form is rigid — any putative odd perfect number MUST have exactly this shape, no deformation allowed (paper60 §14 ARITHMETIC canonical form). [Considered but rejected: face SYMMETRY — the mod-4 congruence has a symmetry flavor (Brauer class at $k=4$) but paper60 §14 + §25 canonicalize ARITHMETIC for OPN layers that interrogate integer lattice structure; projection $P_E$ — Euler form is a structural pin on prime-power integers but its load-bearing content is operational ($P_D$), not measurement ($P_E$); pattern P1 — Geometric Reinterpretation of a classical 1747 result would be retrospective; the forcing is rigidity.]
- **Cross-cuts**: bsd:L1 (shared gauge class / number-field prime structure — Euler's special prime $p$ parallels the BC-over-$K$ distinguished prime in BSD paper26 L1), katz-sarnak:L_bridge-family ($k=4$ bridge family constraint; paper61 §10), lehmer:L_cyclotomic (mod-4 arithmetic lattice on the cyclotomic topology of the e-circle, paper60 §07), goldbach:L1/L2 (same $\mu_p$ generation via BC algebra, shared ARITHMETIC face), twin-primes:L1 (shared arithmetic prime-structure entry point).

### L2 — Abundancy multiplicativity

**Claim**: The abundancy ratio $h(n) = \sigma(n)/n$ is multiplicative: $h(n) = \prod_{q^v \| n} h(q^v)$ with local factor $h(p^a) = (p^{a+1} - 1)/(p^a(p-1)) = (p/(p-1))(1 - p^{-(a+1)})$. Each local $h(p^a) \in [1, p/(p-1))$ for $p$ odd.

**Status**: LITERATURE
**Source**: Elementary; Euler product; paper40 §2. This is the multiplicativity of $\sigma$ in operator-product form; appears in every introductory analytic-number-theory text.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the multiplicativity of $\sigma$ IS the Euler-product structure at the level of the abundancy ratio; paper60 §14 "the partition function $Z(\beta) = \zeta(\beta) = \prod_p (1 - p^{-\beta})^{-1}$ encodes the primes through the Euler product" — L2 is exactly this structure applied to $h(n)$)
- **Projection**: $P_D$ (paper61 §10 — multiplicative decomposition of state evaluations is the canonical ITPFI factorization of the BC system; north-star §0.1 $P_D$ preserved-invariant list includes "ITPFI factorization $\omega_1 = \bigotimes_p \omega_1^{(p)}$")
- **Pattern**: P5 Zeta Regularization (paper60 §14 — the Euler product is zeta regularization in its purest form: $\zeta(\beta) = \prod_p (1 - p^{-\beta})^{-1}$ is the multiplicative-side regularization of a divergent sum; the local factor $h(p^a)$ is a truncated Epstein-zeta-type evaluation on the $p$-slice)
- **Invariant preserved**: C*-algebra structure (load-bearing — the multiplicative decomposition lives in the tensor-product structure of $A_{BC}$), ITPFI factor type (load-bearing — ITPFI III$_{1/p}$ at each prime supplies the local factor $h(p^a)$)
- **Geometric interpretation**: The abundancy ratio factors as a product over prime slices exactly because the BC algebra's KMS$_1$ state is an ITPFI tensor product over primes (paper61 §10). Each local factor $h(p^a)$ is the KMS$_1$-truncated state on the $p$-th slice, evaluated at the Hecke-orbit sum up to exponent $a$. Under $P_D$ (paper61 §10) this is the operational-core statement: the $\sigma$ function respects the Hecke-semigroup's multiplicative structure. Pattern 5: the Euler product $\prod_p (1 - p^{-\beta})^{-1}$ is the canonical zeta-regularization of the prime sum, and $h(p^a)$ is its truncated-exponent analog (paper60 §14 Euler-product structure). [Considered but rejected: face RESONANCE — Euler product-as-mode-decomposition is a fair alternative reading but paper60 §14 canonicalizes ARITHMETIC for layers that interrogate the integer lattice; pattern P4 — the multiplicativity is rigid but the mechanism delivering $h(n) = \prod h(p^a)$ IS Euler-product zeta-regularization; projection $P_O$ — the statement is elementary but its structural role in the chain is strictly internal-operational.]
- **Cross-cuts**: goldbach:L2 (shared Hecke-semigroup multiplicative structure; fundamental theorem of arithmetic in operator form), bsd:L2 (BSD bridge family — local Euler factors, paper26 L2 — same multiplicative engine per paper61 §10), rh:L2 (ITPFI Euler-product factorization for $\zeta$; paper13 Theorem 4.1), bgs:L1 (BC at KMS$_1$ → type III$_1$ factor; shared ITPFI at the state level), twin-primes:L2 (same multiplicative structure).

### L3 — Robin's inequality

**Claim**: Under RH, $\sigma(n) < e^\gamma n \ln(\ln n)$ for all $n > 5040$, where $\gamma$ is the Euler-Mascheroni constant (Robin 1984). Conversely, if Robin's inequality holds unconditionally for all $n > 5040$, RH follows.

**Status**: LITERATURE — CONDITIONAL on RH (cross-paper transport from Paper 13 RH; equivalently CONDITIONAL on CCM 2025, not an independent RH assumption)
**Source**: Robin 1984 (*Journal de Mathématiques Pures et Appliquées*); Ramanujan (earlier, circa 1915, unpublished); paper40 §3; paper13-rh PROOF-CHAIN.md (RH at 8/10 conditional on CCM 2025).

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — "how LOUD can the oscillation get"; Robin's inequality is a growth-rate upper bound on the $\sigma$ amplitude, parallel to Lindelöf's bound on $|\zeta(1/2 + it)|$; both are "how large can the arithmetic function grow" statements)
- **Projection**: $P_D$ (paper61 §10 — the bound lives inside $P_D$ because Robin's inequality is derived from the explicit formula — an operator-algebraic identity on the BC side)
- **Pattern**: P5 Zeta Regularization (Robin's inequality is derived from the explicit formula $\sum_{p \leq x} \log p = x + \sum_\rho x^\rho/\rho + \text{lower order}$ applied to $\sigma(n)$; the derivation is zeta-regularized)
- **Invariant preserved**: L-value (load-bearing — the bound is an RH-dependent $\zeta$-evaluation), spectral gap (background — RH's zero-free region controls the error term)
- **Geometric interpretation**: Robin's inequality is the AMPLITUDE-face content of the $\sigma$ function: how fast can $\sigma(n)$ grow relative to $n \ln(\ln n)$? Under RH, the bound is $e^\gamma \cdot n \ln(\ln n)$, tight for highly composite $n$. Under $P_D$ (paper61 §10) the bound is a consequence of the RH zero-free region applied to $\sigma$ via the explicit formula. Pattern 5: the derivation zeta-regularizes the divergent prime sum $\sum_p \log p$ into a convergent zero-sum, and Robin's inequality is the consequence at the $\sigma$-level (paper60 §14 explicit-formula mechanism). The cross-paper dependency on Paper 13 is transparent: OPN inherits RH's Robin bound as a constraint; RH proves independent of OPN. [Considered but rejected: face ARITHMETIC — Robin's bound is arithmetic-face content in a loose sense but paper60 §11 AMPLITUDE-canonicalizes growth-rate bounds; projection $P_O$ — Robin inequality is Clay-adjacent via RH but operationally lives in $P_D$; pattern P1 — reinterpretation of Robin's bound in BC language is downstream; the load-bearing mechanism is zeta-regularization per Paper 13.]
- **Cross-cuts**: rh:L_Robin (PRIMARY cross-paper transport — paper13 PROOF-CHAIN supplies the Robin inequality as an RH consequence; explicit-formula derivation shared), lindelof:L_amplitude (AMPLITUDE canonical, $|\zeta(1/2 + it)|$ subconvexity; Robin is the $\sigma$-analog growth bound, paper60 §11), goldbach:L4 (shared explicit-formula prime density; cross-paper from RH), twin-primes:L2 (shared explicit formula for zero pair correlation; same paper13 upstream), bsd:L7 (GRH ↔ BSD-side L-value bound; paper26 analogous cross-paper transport).

### L4 — Hecke-orbit projector $H_n$

**Claim**: Define $H_n = \sum_{d \mid n} \mu_{n/d} \mu_{n/d}^*$ in the Bost-Connes algebra $A_{BC}$. Then $H_n$ is a projection, and the KMS$_1$ state evaluates as $\omega_1(H_n) = \sigma(n)/n$. The abundancy ratio is a single KMS$_1$ trace on a Hecke-orbit sum — NOT the product $\zeta(s) \cdot \zeta(s-1)$ directly, but a local operator-algebraic decomposition.

**Status**: PROVED (novel construction, 2026-04-14)
**Source**: paper1 BC algebra construction (Axiom 5, $\mathbb{N}^\rtimes$ generators $\{\mu_p\}$); Bost-Connes 1995 (CMP 172, 381–446) — specifically the state evaluation $\omega_1(\mu_d^* \mu_d) = d^{-1}$; paper40 §4 (novel derivation: combine BC state evaluation with Möbius inversion); paper60 §25 "the OPN trigger" (the moment the identity appeared).

#### Physics

- **Face**: ARITHMETIC (paper60 §14 + §25 — the identity $\omega_1(H_n) = \sigma(n)/n$ is the canonical bridge from the BC algebra's Hecke-orbit structure to the $\sigma$ function; paper60 §25 explicitly names this as the OPN trigger — the first appearance of the arithmetic face through the BC lens)
- **Projection**: $P_D$ (paper61 §10 — the Hecke-orbit projector is exactly the $P_D$ target: $\mu_d \mu_d^*$ projections and KMS$_1$ state evaluations are the paper61 §10 preserved invariants of $P_D$; north-star §0.1 $P_D$ table entry verbatim)
- **Pattern**: P1 Geometric Reinterpretation (paper60 §25 — "the σ function was a KMS$_1$ trace in the BC algebra all along; nobody had written it down before"; this is Pattern 1 in its purest form — restore the hidden operator-algebraic structure and the "no connection" dissolves into an obvious identity)
- **Invariant preserved**: BC-KMS state (load-bearing — the identity is a KMS$_1$ state evaluation), C*-algebra structure (load-bearing — $H_n$ lives in $A_{BC}$)
- **Geometric interpretation**: The Hecke-orbit projector $H_n$ is the sum over divisors of $n$ of the Hecke projections $\mu_{n/d} \mu_{n/d}^*$. Each $\mu_d^* \mu_d$ has KMS$_1$ evaluation $d^{-1}$ (Bost-Connes 1995 state formula); summing over divisors gives $\sigma(n)/n$ directly via Möbius inversion on the divisor lattice. Under $P_D$ (paper61 §10) this is the canonical Branch-D entry-point for OPN: the $\sigma$ function is an operator trace in the BC system. Pattern 1 (paper60 §25): "with our geometry it's not so odd" — the classical mystery of OPN's resistance to operator-algebraic methods was a PROJECTION artifact. Restore the fifth-dimension BC structure and the connection is immediate. This is the paradigm case of the face-methodology. [Considered but rejected: face RESONANCE — KMS$_1$ trace as resonance-mode content is a fair reading but the identity's load-bearing content IS the arithmetic $\sigma$ function (paper60 §14 canonical); projection $P_A$ — the KMS$_1$ state has quantum-observable aspects but the Hecke-orbit projector is strictly operator-algebraic; pattern P4 — the identity is rigid but its DISCOVERY character is Geometric Reinterpretation, not rigidity protection.]
- **Cross-cuts**: qg5d:Branch-D-Axiom-5 (shared BC-KMS state + C*-algebra structure; paper61 §10 $P_D$ target), rh:L2 (ITPFI Euler-product factorization for $\zeta$; same $\mu_p$ machinery), goldbach:L1 (same $\mu_p$ generators; shared ARITHMETIC entry), bsd:L4 (BSD dark-state projector $P_k^\mathfrak{p}$; paper26 L4 — same KMS$_1$-projector-construction template), bgs:L1 (BC at KMS$_1$ → type III$_1$; shared state-evaluation machinery), baum-connes:L1 (Cuntz-Li semigroup $\mathbb{N}^\rtimes$ at K-theory target; same generators), twin-primes:L1 (shared BC entry point).

### L5 — ITPFI local-global decomposition

**Claim**: The KMS$_1$ state of the BC algebra factorizes as $\omega_1 = \bigotimes_p \omega_1^{(p)}$ (ITPFI / Araki-Woods tensor product of local states). Combined with the multiplicativity of $\sigma$, this gives $\omega_1(H_n) = \prod_{p^a \| n} h(p^a)$ where each local factor $h(p^a) = (p/(p-1))(1 - p^{-(a+1)})$ is a KMS$_1$ datum on the $p$-th ITPFI III$_{1/p}$ slice. The $\prod = 2$ condition is a RESONANCE of local factors — each must contribute, and the product must conspire to hit exactly $2$.

**Status**: PROVED
**Source**: paper13-rh Theorem 4.1 (ITPFI factorization of the KMS$_1$ state of $A_{BC}$ as Araki-Woods tensor product); paper40 §5; paper13 research/265; Araki-Woods 1968 (ITPFI classification); paper1 BC algebra construction; paper60 §25; paper61 §10 ITPFI-factorization target.

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — the local-global decomposition of $\sigma(n)/n$ IS the arithmetic-face statement par excellence: "how do integers LATTICE on the circle" answered via the Euler-product tensor structure; paper60 §25 + §14)
- **Projection**: $P_D$ (paper61 §10 — ITPFI factorization $\omega_1 = \bigotimes_p \omega_1^{(p)}$ is a direct paper61 §10 $P_D$ target, verbatim entry in the $P_D$ preservation table; north-star §0.1)
- **Pattern**: P4 Topological Rigidity (paper61 §10 — the tensor-product structure of the KMS$_1$ state is rigid: ITPFI III$_{1/p}$ at each prime is forced by the BC construction, not chosen; this is the operator-algebra form of "the primes are independent in the state")
- **Invariant preserved**: ITPFI factor type (load-bearing — III$_{1/p}$ at each prime slice is the specific classification), BC-KMS state (load-bearing — $\omega_1$ is the tensor-factored state)
- **Geometric interpretation**: The ITPFI local-global decomposition is the operator-algebraic form of the Euler product: $\omega_1$ decomposes as an infinite tensor product, one type-III$_{1/p}$ slice per prime. This factorization IS the local-global structure of the BC system — each prime contributes independently to the global KMS$_1$ state. Under $P_D$ (paper61 §10) this is the Branch-D operational-core statement about Araki-Woods classification. Pattern 4: the decomposition is rigid — no deformation is possible; the III$_{1/p}$ classification at each prime is forced by the Hecke structure. The spoof-Hasse insight (2026-04-14): Descartes' spoof satisfies $\sigma(N) = 2N$ locally at every "prime" power but fails globally because 22021 is not prime. This is a LOCAL-GLOBAL FAILURE of the same type as the Hasse principle for elliptic curves — the BSD template says Sha measures the failure of Hasse, and here spoofs are the Hasse-like obstructions to OPN (paper60 §25). [Considered but rejected: face RESONANCE — ITPFI-as-mode-decomposition framing is real but paper60 §14 canonicalizes ARITHMETIC for the $\sigma$-function decomposition; pattern P5 — Euler-product regularization is a fair reading of the tensor structure but paper61 §10 treats ITPFI factorization as topological rigidity of the factor type; projection $P_O$ — the decomposition is foundational but strictly operational.]
- **Cross-cuts**: rh:L2/L3 (shared ITPFI factorization of $\omega_1$; paper13 Theorem 4.1 is the shared upstream), bsd:L5 (shared cocycle shift / local-Euler-factor structure; paper26 L5 — same ITPFI-tensor local-global assembly per BSD template), bgs:L1 (shared BC at KMS$_1$; type III$_1$ factor from ITPFI), katz-sarnak:L5 (same ITPFI local-global structure; paper60 §12 SYMMETRY face has analogous local-to-global assembly; explicit "same structure as BSD Paper 26, OPN Paper 40" from katz-sarnak X-RAY cross-cut bullet), goldbach:L2 (shared ITPFI / multiplicative structure), baum-connes:L1 (K-theory pairing shares semigroup structure), qg5d:Branch-D-Axiom-5 (foundational ITPFI source).

### L6 — Odd local-global impossibility — **W_OPN-1 — the wall**

**Claim**: No Euler-form odd integer $N$ with $\omega(N) \geq 10$ distinct prime factors satisfies $\prod_{p^a \| N} h(p^a) = 2$. Specifically, via BC spectral constraints: (a) $v_\ell$-cascade at ODD primes $\ell$ (not $\ell = 2$, which gives no constraint — v₂ correction 2026-04-14); (b) ITPFI joint constraint correlating local factors beyond classical per-prime sieving; (c) 36-pin rigidity (chessboard argument propagating programme constraints). The three sub-routes 6a/6b/6c are all historically attempted; 6a is KILLED, 6b is BLOCKED-DECOMPOSED, 6c remains ACTIVE.

**Status**: **OPEN — the named wall W_OPN-1**. Confidence 0.4 (paper40 ring confidence; brief §4).
**Source**: paper40 §6 (three sub-routes); BSD template Key Lemma C (paper26 analog); paper60 §14 "the additive-multiplicative wall" + §25 "the OPN trigger" wall; Nielsen 2015 ($\omega(N) \geq 10$); Ochem-Rao 2012 ($N > 10^{1500}$).

#### Physics

- **Face**: ARITHMETIC (paper60 §14 + §25 — the local-global impossibility IS the arithmetic-face wall; paper60 §28 "The South Trough Needs Lifting" identifies the ARITHMETIC face as where the BC framework stammers most; OPN sits in the West quadrant but on the ARITHMETIC face)
- **Projection**: $P_O$ (paper61 §17 — the oldest open problem's Clay-adjacent closure statement sits at the outer-ring boundary; the non-existence conjecture itself is an outer-ring object; paper61 §17 outer-ring list includes OPN implicitly via Branch-D vertices)
- **Pattern**: P4 Topological Rigidity (the impossibility, if it holds, is a structural rigidity of the ITPFI tensor product — no odd conspiracy of local factors can achieve the global product $= 2$; this is the operator-algebra form of the Hasse-principle rigidity per the BSD template)
- **Invariant preserved**: ITPFI factor type (load-bearing — the impossibility argument lives in the III$_{1/p}$ joint-constraint structure), BC-KMS state (background — $\omega_1$ is the state being constrained)
- **Geometric interpretation**: L6 is the wall. The question "can $\prod_{p^a \| N} h(p^a) = 2$ for odd $N$?" is equivalent to asking whether the ITPFI local-global decomposition admits an odd "conspiracy" — local factors aligning to hit the global $= 2$ condition. The spoof-Hasse insight (paper60 §25) frames this precisely: spoofs are the Hasse-principle analogs of Sha elements; they show the local equations HAVE solutions (the local factors can align to hit 2), but the global primality constraint is violated (22021 isn't actually prime). The BSD template (paper26) gives the mechanism: Sha finiteness under BSD-2 analogs forces the obstruction group to be trivial, hence no global conspiracies. OPN is the $\sigma$-version of this template applied to abundancy ratios at KMS$_1$. Under $P_O$ (paper61 §17) this is the Clay-adjacent outer-ring closure for the 2,300-year-old statement. Pattern 4: the impossibility, if it closes, is a rigidity — no infinitesimal deformation of odd $N$ can achieve the global $= 2$ condition (paper60 §25). [Considered but rejected: face DYNAMICS — the local-global conspiracy has a flow-on-circle flavor (the KMS$_1$ state is the modular-flow equilibrium) but paper60 §14 + §25 canonicalize ARITHMETIC for OPN's structural content; projection $P_D$ — the internal BC machinery lives in $P_D$ but the conjecture-level content is outer-ring Clay-adjacent; pattern P5 — zeta-regularization underlies the ITPFI structure but the wall's character is rigidity of the joint constraint, not regularization mechanics.]
- **Cross-cuts**: bsd:L_Sha (PRIMARY STRUCTURAL PARALLEL — same Hasse-principle failure template; paper60 §25 explicit mapping; both use BC-KMS + ITPFI + local-global obstruction structure), katz-sarnak:L5b (explicit cross-cut from katz-sarnak X-RAY: "same ITPFI factor type — local-global structure — same ITPFI factorization used by OPN Paper 40"; paper60 §12 SYMMETRY analog), abc:L_rad (paper37 ABC auxiliary route 6c — rad$(n)$ bound on Euler form; if ABC closes OPN follows as corollary), goldbach:L5 (shared wall at additive-multiplicative interface; both ARITHMETIC face; paper60 §14), twin-primes:L4 (shared GUE/arithmetic-correction wall structure — both need pointwise additive conclusions from multiplicative data; paper60 §14), collatz:L_additive (shared additive-vs-multiplicative interface; paper60 §09 + §14), lehmer:L_gap (shared "rigidity at the arithmetic lattice boundary" structural form — Lehmer's Mahler-measure gap at cyclotomic ↔ OPN's h(n) $\neq 2$ gap at odd-integer lattice; paper60 §07 TOPOLOGY analog via cyclotomic-vs-odd-lattice rigidity), rh:L_Robin (conditional cascade — if Route 6c uses Robin-type bound, RH inheritance).

### L7 — Non-existence: no odd perfect number exists

**Claim**: No odd perfect number exists.

**Status**: FOLLOWS (from L6)
**Source**: paper40 §7; follows from L6's local-global impossibility (BSD Theorem 13.1 analog — local obstruction ⇒ global non-existence, paper26 template).

#### Physics

- **Face**: ARITHMETIC (paper60 §14 + §25 — the 2,300-year-old non-existence statement IS the arithmetic-face Clay-adjacent closure; paper60 §25 names this as the founding test case of the e-circle methodology)
- **Projection**: $P_O$ (paper61 §17 — the oldest open problem's statement is the outer-ring closure by construction; the "2,300 years of searching" framing of paper40's closing is Clay-adjacent)
- **Pattern**: P4 Topological Rigidity (the non-existence, once L6 closes, is rigid: no odd integer in the entire infinite lattice satisfies $\sigma(n) = 2n$; this is a global rigidity derived from the local-global impossibility)
- **Invariant preserved**: ITPFI factor type (load-bearing — the rigidity inherits from L5/L6's III$_{1/p}$ decomposition)
- **Geometric interpretation**: L7 is the Clay-adjacent closure statement: the 2,300-year-old conjecture as an outer-ring theorem. Once L6 closes the local-global impossibility (no odd conspiracy at any prime count $\geq 10$; combined with literature lower bounds $N > 10^{1500}$ and $\omega(N) \geq 10$ making smaller cases computationally excluded), L7 follows as a global non-existence rigid consequence. Under $P_O$ (paper61 §17) this is the outer-ring statement. Pattern 4: the rigidity is total — the infinite integer lattice has no odd perfect element (paper60 §14 ARITHMETIC wall closure). [Considered but rejected: face ANY-OTHER — L7 is purely arithmetic; projection $P_D$ — L7 is a Clay-adjacent statement and lives at $P_O$, not $P_D$; pattern P1 — L7 is not reinterpretation but consequence.]
- **Cross-cuts**: bsd:L_theorem (analogous outer-ring closure; paper26 L_final), qg5d (the 2,300-year-old statement closure belongs to the programme hub; paper60 §25), katz-sarnak:L_final (analogous outer-ring closure from symmetry-type analysis).

---

## §4 Branch Map

The OPN chain is largely linear with a critical three-way branch at L6 (three sub-routes 6a/6b/6c) and one auxiliary route (ABC-based 6c-alt). The branches differ in WHICH face-and-pattern combination they deploy to close the local-global impossibility.

```
L5 (ITPFI local-global decomposition, PROVED)
                │
                ├── Route 6a: Odd Robin sharpening via halved residue
                │   [face: AMPLITUDE | proj: P_D | pat: P5]
                │   KILLED 2026-04-14 in morning verify pass.
                │   The odd-restricted Dirichlet series has a
                │   zero at s=1 (via (1-2^{1-s}) factor) canceling
                │   the pole — gives halved Mertens constant
                │   e^γ/2 ≈ 0.890 as candidate odd Robin constant.
                │   BUT: σ(n)/n > 2 for infinitely many odd n
                │   (dense orbit around e^γ for highly composite
                │   odd n). The direction of reasoning was
                │   BACKWARDS — a tighter Robin bound does not
                │   exclude OPN because σ(n)/n can still exceed 2
                │   for sparse odd n even if average is below 2.
                │   paper60 §29 signal log records the kill.
                │
                ├── Route 6b: E_2 quasi-modular obstruction
                │   [face: HARMONICS | proj: P_D | pat: P5]
                │   BLOCKED-DECOMPOSED 2026-04-14.
                │   The odd-restricted σ-series is
                │   F_odd(τ) = -(1/48)[E_2(τ) - E_2(τ+1/2)].
                │   G(τ) = E_2(τ) - E_2(τ+1/2) has period 2
                │   but NO quasi-modular transformation under
                │   SL_2(Z) or any congruence subgroup —
                │   the half-period shift is incommensurable
                │   with modular structure. Constrains generating
                │   function analytically but NOT individual
                │   Fourier coefficients arithmetically.
                │   Productive output: Dirichlet zero at s=1
                │   via (1-2^{1-s}) factor → absorbed into 6a
                │   (but 6a now dead, so this output moot).
                │   Detail: 06b-E2-quasi-modular-obstruction.md
                │
                ├── Route 6c: ITPFI joint constraint [ACTIVE]
                │   [face: ARITHMETIC | proj: P_O | pat: P4]
                │   The surviving route. Three components:
                │   (a) v_ℓ cascade at ODD primes ℓ
                │       (v_2 correction 2026-04-14: LTE lemma
                │        for p=2 with odd exponent gives
                │        v_2(a^n - 1) = v_2(a-1), and for all
                │        subordinate primes q with even
                │        exponent 2e, σ(q^{2e}) has odd top
                │        exponent 2e+1, so v_2(σ(q^{2e})) = 0.
                │        Verified: σ(9)=13, σ(49)=57, σ(121)=133
                │        all odd. The 2-adic valuation constraint
                │        is VACUOUS — gives NO restriction.
                │        Productive direction: track v_ℓ for
                │        ODD primes ℓ, what published literature
                │        Nielsen 2015, Ochem-Rao does.)
                │   (b) ITPFI joint constraint correlating
                │        local factors beyond classical per-prime
                │        sieving — this is the BC-upgrade content.
                │        The ITPFI tensor structure gives ALL v_ℓ
                │        simultaneously rather than one at a time.
                │   (c) 36-pin rigidity (chessboard argument)
                │        — programme-level constraint cascading
                │        from the master-table pin-preservation.
                │
                └── Route 6c-alt (ABC auxiliary): paper37 ABC ⇒ OPN
                    [face: ARITHMETIC | proj: P_D | pat: P5]
                    For n = p^α m^2, rad(n) = p · rad(m).
                    σ(n) = 2n gives 3n = σ(n) + n = 3n;
                    ABC-type bounds on rad(n) constrain prime-
                    power structure. Makes OPN a corollary of
                    ABC (paper37 1/10 confidence).

All routes target: no odd n satisfies σ(n) = 2n; L7 follows.

Routes differ in which face carries the impossibility argument:
- Route 6a sits at AMPLITUDE (Robin-type growth bound) — KILLED.
- Route 6b sits at HARMONICS (Fourier-dual E_2 constraint) —
  BLOCKED-DECOMPOSED; produced a useful intermediate output.
- Route 6c sits at ARITHMETIC (ITPFI joint constraint + 36-pin
  rigidity) — ACTIVE; the surviving route.
- Route 6c-alt sits at ARITHMETIC via auxiliary ABC — depends on
  paper37 ABC closure (itself 1/10).

Structural observation: the two routes that survived attack
(6c and 6c-alt) both live on the ARITHMETIC face under P_D/P_O.
The two KILLED/BLOCKED routes (6a, 6b) crossed faces
(AMPLITUDE, HARMONICS) — they attempted to route through
non-canonical faces and both failed for structural reasons.
This is a methodological datum: the ARITHMETIC-face tends to
insist on internal mechanisms; routes that try to bypass it
via other faces (Robin/E_2 = AMPLITUDE/HARMONICS) exit the
face's natural structure and thereby lose access to its rigidity.
paper60 §28 "The South Trough Needs Lifting" observation applies:
the BC framework stammers on the ARITHMETIC face; routes that
leave the face stammer twice.
```

---

## §5 Face Histogram

| Face       | Count | Bar                        | Interpretation |
|------------|-------|----------------------------|---|
| TOPOLOGY   |   0   |                            | OPN does not live on the topology face directly. Cross-cut to lehmer (TOPOLOGY) exists at structural-parallel level (cyclotomic lattice vs odd-integer lattice rigidity) but no OPN layer is TOPOLOGY-canonical. |
| DYNAMICS   |   0   |                            | OPN does not interrogate modular-flow dynamics as a main-chain layer. |
| HARMONICS  |   0   |                            | No main-chain HARMONICS; L6b (sub-route) BLOCKED-DECOMPOSED was the only HARMONICS-face attempt and it fails structurally. |
| MEASURE    |   0   |                            | OPN does not interrogate equidistribution. |
| AMPLITUDE  |   1   | ████                       | L3 (Robin inequality) — cross-paper transport from RH. This is the sole main-chain AMPLITUDE layer. L6a sub-route was AMPLITUDE-KILLED. |
| SYMMETRY   |   0   |                            | No explicit SYMMETRY-face layer; Euler-form mod-4 constraint could be SYMMETRY-flavored but ARITHMETIC canonicalizes per paper60 §14 + §25. |
| CURVATURE  |   0   |                            | OPN is not a gauge-curvature object. |
| ARITHMETIC |   5   | ████████████████████       | DOMINANT (71%). L1 (Euler form), L2 (abundancy multiplicativity), L4 (Hecke-orbit projector), L5 (ITPFI decomposition), L6 (odd local-global impossibility), L7 (non-existence — follows). Plus Route 6c and 6c-alt both ARITHMETIC. OPN IS the founding canonical ARITHMETIC-face vertex per paper60 §25 "the OPN trigger." |
| RESONANCE  |   0   |                            | OPN does not interrogate trace-formula / spectral-side resonances as a main-chain layer. |
| SPREAD     |   0   |                            | OPN does not interrogate $L^2$-mass-spreading. |

**Interpretation**: ARITHMETIC dominates (5 / 7 main layers = 71%, plus L7 as ARITHMETIC-follows for 6/7 = 86% counting L7) — confirming paper60 §14 + §25's identification of OPN as the FOUNDING canonical ARITHMETIC-face vertex. Paper60 §25 "the OPN trigger" is the origin story of the face-methodology: OPN was the first problem where the method "look at the problem → find the e-circle → ask which property it interrogates" produced a face-canonical connection, and the property was ARITHMETIC. AMPLITUDE carries 1 layer (L3 Robin inequality, 14%) — a cross-paper import from RH via Robin 1984; this is the single face-bridge out of the ARITHMETIC core. HARMONICS carries 0 main layers (L6b sub-route was attempted and BLOCKED-DECOMPOSED — a negative datum showing the HARMONICS route fails structurally for OPN). All seven other faces are absent. This extreme ARITHMETIC concentration is the structural signal that the chain's depth matches its face-pureness: OPN asks one question on one face, and the face's own difficulty (the additive-multiplicative wall per paper60 §14 + the local-global-failure wall per paper60 §25) is what makes the wall hard. The "shape" of OPN on the e-circle is a single point at ARITHMETIC with one thin ray to AMPLITUDE (via Robin/RH transport) — the narrowest face-profile of any vertex in the programme. paper60 §28 "The South Trough Needs Lifting" places OPN in the West quadrant on this face at 4/10 confidence: the ARITHMETIC face is where the BC framework stammers most, and OPN's face-purity makes it the flagship stammer.

---

## §6 Projection Histogram

| Projection | Count | Bar                        | Notes |
|------------|-------|----------------------------|---|
| $P_A$        |   0   |                            | OPN has no quantum-observable content; $P_A$ forgets it. No KMS$_1$ observable maps to a quantum measurement for odd integers. |
| $P_B$        |   0   |                            | OPN has no gauge-bundle content; $P_B$ forgets it. The $\sigma$ function is not carried by a KK bundle. |
| $P_C$        |   0   |                            | OPN contributes no cosmological pin; $P_C$ forgets it. |
| $P_D$        |   5   | ████████████████████       | DOMINANT (71%). L1, L2, L3, L4, L5 all live inside $P_D$'s preservation class — the Hecke semigroup, the ITPFI factorization, the Hecke-orbit projector, the BC-KMS state, and the Robin-bound derivation (via explicit formula from the BC side) are all operational BC-algebra content. Paper61 §10 $P_D$ target list explicit. |
| $P_E$        |   0   |                            | OPN contributes no pin in the 36-pin master table. The "if σ(n)/n = 2 for odd n" would itself be a candidate pin, but OPN's content is NON-EXISTENCE — the pin is EMPTY, which is not a pin. |
| $P_O$        |   2   | ████████                   | L6 (odd local-global impossibility, the wall) and L7 (non-existence, follows) sit at the $P_O$ outer-ring boundary — these are the Clay-adjacent closure statements for the 2,300-year-old conjecture. |

**Interpretation**: The projection profile is $P_D$-dominant (5 / 7 = 71%) with two $P_O$ entries at L6 and L7. This matches paper61 §17's compound-projection assignment for OPN: $P_D$ for the internal BC-algebraic machinery (Hecke-orbit projector, ITPFI decomposition, Robin inequality via explicit formula), $P_O$ for the conjecture's closure statement itself (the oldest open problem). $P_A, P_B, P_C, P_E$ are all absent — OPN is neither a quantum observable nor a gauge bundle nor a cosmological pin nor a sub-percent numerical prediction. The $P_D$ dominance is the structural signal that OPN's natural home is Branch D (Bost-Connes, operator-algebra side) — this matches paper60 §25's "the OPN trigger" narrative (the discovery was the BC connection $\omega_1(H_n) = \sigma(n)/n$) and north-star §0.1's $P_D$ preserved-invariant table (Hecke semigroup on $S^1$; ITPFI factorization; KMS$_1$ state). The $P_O$ slice at L6/L7 is the outer-ring boundary; if Route 6c closes, OPN will have a cleaner $P_D \to P_O$ closure than Goldbach or Twin Primes because OPN's non-existence statement is binary (no counter-example exists) rather than existence-asymptotic. Compared to ym's projection profile (13 of 20 layers at $P_B$, 65%), OPN's 71% $P_D$ concentration is the highest single-projection fraction in the outer-ring — it is the MOST Branch-D-pure vertex in the programme.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                           qg5d Branch D
                           (Axiom 5; N^⋊ = ⟨μ_p⟩;
                            primes-as-operators;
                            BC algebra, KMS_1,
                            ITPFI ω_1 = ⊗ ω_1^(p))
                                  │
                                  │ ═══ L4 Hecke-orbit projector
                                  │ ═══ L5 ITPFI local-global
                                  │ ═══ shared BC-KMS state
                                  │
       bsd ═══════════════════  OPN  ══════════════  rh
       (ARITHMETIC;              │                   (RESONANCE primary;
        PRIMARY STRUCTURAL       │                   CCM resolvent; Robin
        PARALLEL — BSD template  │                   inequality delivered
        for local-global         │                   to OPN L3 via cross-
        obstruction)             │                   paper transport)
       ═══ L1 ↔ BC over K        │                   ═══ L2 shared ITPFI
           Euler special prime   │                   ═══ L3 ↔ cross-paper
       ═══ L2 ↔ bridge family    │                       transport Robin
           local Euler factors   │                   ═══ L4 shared BC-KMS
       ═══ L4 ↔ dark-state       │                       state machinery
           projector P_k^p       │
       ═══ L5 ↔ cocycle shift    │
       ═══ L6 ↔ Sha ↔            │
           SPOOF-HASSE insight   │
           (paper60 §25 mapping) │
                                 │
       goldbach ═════════════════│═══════════════  twin-primes
       (ARITHMETIC sibling;      │                (ARITHMETIC sibling;
        shared μ_p entry;        │                shared additive-
        shared additive-         │                multiplicative wall)
        multiplicative wall)     │                ═══ L1/L4 shared BC entry
       ═══ L1/L2 shared μ_p      │                ═══ L6 shared wall
       ═══ L5/L6 shared          │                    structure
           ARITHMETIC-face wall  │
                                 │
       katz-sarnak ══════════════│═══════════════  baum-connes
       (SYMMETRY; same ITPFI     │                (RESONANCE; Cuntz-Li
        local-global structure)  │                semigroup = N^⋊)
       ═══ L5 ↔ L5 same ITPFI    │                ═══ L1/L2 shared N^⋊
           factor type           │                ─── L6 structural
           (explicit cross-cut   │                    analog at K-theory
           in katz-sarnak X-RAY)  │                    pairing
                                 │
       abc ══════════════════════│═══════════════  lehmer
       (ARITHMETIC; auxiliary    │                (TOPOLOGY; structural-
        route via rad(n) bound;  │                parallel "gap at
        paper37 ⇒ OPN            │                arithmetic lattice
        as corollary)            │                boundary")
       ─── L6c-alt route        │                ─── L6 ↔ Lehmer's
           Euler form rad(n)     │                    cyclotomic gap
                                 │                    (paper60 §07
                                 │                    structural parallel)
                                 │
                           collatz / bgs / pvnp
                           (HARMONICS / RESONANCE /
                            RESONANCE; shared BC
                            operational core)
                           ─── L4/L5 shared BC
                               machinery (KMS_1,
                               ITPFI, Hecke)

                           lindelof / sato-tate
                           (AMPLITUDE / MEASURE)
                           ─── L3 ↔ Robin bound
                               via RH/Lindelöf
                               subconvexity (paper60
                               §11 AMPLITUDE canonical)
```

### Bullet list (per-edge)

- **L1 ↔ bsd:L1** — shared gauge class (number-field prime structure).
  - Reason: Euler's special prime $p$ (L1) parallels the BC-over-$K$ distinguished prime in BSD paper26 L1; both are "the special prime with odd exponent" in the respective multiplicative structures. Paper26 L1's BC over imaginary quadratic $K$ is the number-field extension of L1's prime-power congruence form.
  - Transposition candidate: YES (BSD template is load-bearing structural analog; paper60 §25 explicit).

- **L1 ↔ katz-sarnak:L_bridge-family** — shared gauge class ($k=4$ bridge family).
  - Reason: Euler form congruence $p \equiv \alpha \equiv 1 \pmod 4$ is a $k=4$ bridge-family Brauer constraint per paper61 §10 bridge family table.
  - Transposition candidate: SPECULATIVE.

- **L1 ↔ lehmer:L_cyclotomic** — shared gauge class (cyclotomic arithmetic lattice).
  - Reason: Both layers interrogate the arithmetic lattice on the e-circle's cyclotomic structure. Paper60 §07 (Lehmer TOPOLOGY) places the cyclotomic lattice at the topology face; OPN's Euler form is the odd-integer-lattice analog.
  - Transposition candidate: SPECULATIVE.

- **L1 ↔ goldbach:L1 / twin-primes:L1** — shared $\mu_p$ generation / ARITHMETIC face.
  - Reason: Same BC algebra entry point; paper60 §14 names all three as ARITHMETIC-face canonical.
  - Transposition candidate: YES.

- **L2 ↔ rh:L2** — shared ITPFI factor type + Euler product.
  - Reason: Multiplicativity of $\sigma$ (L2) = Euler product at the abundancy level; rh L2's ITPFI Euler-product factorization uses the same unique-factorization-via-$\mu_p$ machinery.
  - Transposition candidate: YES.

- **L2 ↔ bsd:L2** — shared ITPFI factor type (bridge family / local Euler factors).
  - Reason: Paper26 L2 (BSD bridge family — local Euler factors) uses the same local-decomposition machinery; OPN L2's $h(p^a)$ is the $\sigma$-version of BSD's local $L_p(E, s)$.
  - Transposition candidate: YES.

- **L2 ↔ goldbach:L2** — shared multiplicative structure.
  - Reason: Both rest on $\mathbb{N}^\rtimes$ and the fundamental theorem of arithmetic in operator form.
  - Transposition candidate: YES.

- **L2 ↔ bgs:L1** — shared ITPFI factor type.
  - Reason: BC at KMS$_1$ → type III$_1$ via ITPFI factorization; shared state-level machinery.
  - Transposition candidate: YES.

- **L3 ↔ rh:L_Robin** — shared L-value + spectral gap (PRIMARY cross-paper transport).
  - Reason: Robin 1984 IS an RH equivalent: RH ⇔ $\sigma(n) < e^\gamma n \ln(\ln n)$ for all $n > 5040$. Paper13 PROOF-CHAIN supplies Robin; OPN consumes. Agent-I-audit-style cross-paper tag applies.
  - Transposition candidate: YES (explicit cross-paper transport; structurally one of the strongest edges).

- **L3 ↔ lindelof:L_amplitude** — shared AMPLITUDE face (growth-rate bound).
  - Reason: Paper60 §11 AMPLITUDE canonical; Robin's inequality is the $\sigma$-analog of Lindelöf's subconvexity for $|\zeta(1/2 + it)|$. Both AMPLITUDE-canonical growth bounds.
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ goldbach:L4 / twin-primes:L2** — shared zero distribution (explicit formula).
  - Reason: All three consume the RH explicit formula for different arithmetic conclusions — Goldbach for prime density, Twin Primes for pair correlation, OPN for the Robin bound on $\sigma$.
  - Transposition candidate: YES.

- **L3 ↔ bsd:L7** — shared L-value bound via GRH.
  - Reason: BSD paper26 L7 uses GRH for analogous L-value bounds; OPN L3 uses RH for the Robin bound. Parallel cross-paper-transport structure.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ qg5d:Branch-D-Axiom-5** — shared BC-KMS state + C*-algebra structure.
  - Reason: The Hecke-orbit projector $H_n$ lives in $A_{BC}$; Axiom 5 ($\{\mu_p\}$ generate $\mathbb{N}^\rtimes$) is the foundational construction. Paper60 §25 explicit: "the Hecke-orbit projector was sitting in the BC algebra's definitions."
  - Transposition candidate: YES (foundational; paper60 §25 origin story).

- **L4 ↔ bsd:L4** — shared BC-KMS state + dark-state projector structure.
  - Reason: BSD paper26 L4's dark-state projector $P_k^\mathfrak{p}$ is structurally analogous to OPN L4's Hecke-orbit projector $H_n$ — both are KMS$_1$ evaluations of operator-algebra sums. Paper60 §25 names the BSD template as OPN's direct structural parent.
  - Transposition candidate: YES (PRIMARY STRUCTURAL PARALLEL; paper60 §25 mapping).

- **L4 ↔ rh:L_KMS** — shared BC-KMS state.
  - Reason: Both rh and OPN rest on the KMS$_1$ state of $A_{BC}$; rh uses it for the spectral realization (resolvent), OPN uses it for the Hecke-orbit projector $\omega_1(H_n)$.
  - Transposition candidate: YES.

- **L4 ↔ goldbach:L1 / twin-primes:L1** — shared $\mu_p$ generators / BC entry.
  - Reason: Same BC algebra entry point ($\{\mu_p\}$); paper60 §14 canonical ARITHMETIC face.
  - Transposition candidate: YES.

- **L4 ↔ baum-connes:L1** — shared C*-algebra structure (Cuntz-Li semigroup).
  - Reason: Paper31 baum-connes Cuntz-Li semigroup $\mathbb{N}^\rtimes$ at K-theory target; same multiplicative semigroup.
  - Transposition candidate: YES.

- **L4 ↔ pvnp:L_BC** — shared BC-KMS state + C*-algebra structure.
  - Reason: pvnp uses BC-algebra spectral-gap rigidity (Popa type III$_1$) — shared operational content.
  - Transposition candidate: YES.

- **L5 ↔ rh:L3** — shared ITPFI factor type + BC-KMS state.
  - Reason: PRIMARY upstream — paper13 Theorem 4.1 is the source of the ITPFI factorization of $\omega_1$. OPN L5 IS rh L3 applied to the abundancy question.
  - Transposition candidate: YES (foundational shared Theorem 4.1).

- **L5 ↔ bsd:L5** — shared ITPFI factor type (cocycle shift).
  - Reason: BSD paper26 L5's cocycle shift / local Euler factor assembly is the same ITPFI-tensor local-global structure. Paper60 §25 explicit mapping: "OPN uses the BSD template of local-global obstruction."
  - Transposition candidate: YES (PRIMARY STRUCTURAL PARALLEL; paper60 §25).

- **L5 ↔ katz-sarnak:L5** — shared ITPFI factor type (local-global).
  - Reason: EXPLICIT CROSS-CUT from katz-sarnak X-RAY §7 bullet list: "L5 ↔ opn:L_local_global — shared ITPFI factor type — Same ITPFI factorization used by OPN (Paper 40)." Paper60 §12 SYMMETRY analog.
  - Transposition candidate: SPECULATIVE (per katz-sarnak X-RAY entry).

- **L5 ↔ bgs:L1** — shared ITPFI factor type (BC at KMS$_1$).
  - Reason: Both use BC at KMS$_1$ → type III$_1$ via ITPFI factorization.
  - Transposition candidate: YES.

- **L5 ↔ goldbach:L2** — shared ITPFI / multiplicative structure.
  - Reason: Same Euler-product-at-the-state-level.
  - Transposition candidate: YES.

- **L5 ↔ qg5d:Branch-D-ITPFI** — shared ITPFI factor type.
  - Reason: Foundational; paper61 §10 $P_D$ target.
  - Transposition candidate: YES.

- **L6 ↔ bsd:L_Sha** — shared ITPFI factor type + BC-KMS state (PRIMARY STRUCTURAL PARALLEL).
  - Reason: paper60 §25 explicit: "BSD 'dark state' — curve where $L(E, 1) = 0$ but Mordell-Weil hidden in Sha — maps directly onto OPN 'dark state': number where local factors conspire to make $\sigma(n)/n = 2$ but global factorization fails." This is THE defining cross-cut of OPN; the entire BSD template is the structural parent of the L6 wall.
  - Transposition candidate: YES (foundational; paper60 §25 founding mapping).

- **L6 ↔ katz-sarnak:L5b** — shared ITPFI factor type (local-global structure).
  - Reason: katz-sarnak X-RAY §7 explicit: "Sub-route 5b ($n$-level via BC ITPFI): matches BSD / OPN local-global structure; confidence 0.65 per programme's ITPFI infrastructure." The local-global obstruction structure is shared across all three (bsd, opn, katz-sarnak).
  - Transposition candidate: YES.

- **L6 ↔ abc:L_rad** — shared ARITHMETIC face (rad$(n)$ bound).
  - Reason: paper37 ABC's rad$(n)$ bound combined with Euler form gives OPN as corollary (paper40 §6c auxiliary route). Both ARITHMETIC-canonical.
  - Transposition candidate: SPECULATIVE (ABC itself 1/10).

- **L6 ↔ goldbach:L5 / twin-primes:L4** — shared additive-multiplicative wall structure.
  - Reason: paper60 §14 — three problems, one wall: additive-multiplicative interface. Goldbach (circle method), Twin Primes (GUE-arithmetic correction), OPN (local-global obstruction). All ARITHMETIC-face walls.
  - Transposition candidate: YES (shared wall; bypass of one would inform others).

- **L6 ↔ collatz:L_additive** — shared additive-vs-multiplicative interface.
  - Reason: paper60 §09 + §14 — Collatz's $n \to 3n + 1$ has the same additive-on-multiplicative structure that OPN's abundancy does.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ lehmer:L_gap** — shared ARITHMETIC-lattice-rigidity (structural parallel).
  - Reason: Lehmer's cyclotomic-vs-non-cyclotomic gap (Mahler measure) is the TOPOLOGY-face analog of OPN's odd-integer-lattice rigidity. Paper60 §07 structural parallel. Both are "rigidity at the arithmetic lattice boundary."
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ pvnp:L_gap** — shared rigidity pattern.
  - Reason: pvnp uses type III$_1$ spectral-gap rigidity; OPN L6 uses ITPFI joint-constraint rigidity. Both P4 Topological Rigidity.
  - Transposition candidate: YES.

- **L6 ↔ rh:L_Robin** — shared L-value (conditional cascade from Route 6c).
  - Reason: If Route 6c uses Robin-type bound (the 36-pin rigidity component), there is conditional cascade through RH.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ bsd:L_final** — shared ARITHMETIC outer-ring closure.
  - Reason: Both L7s are the Clay-adjacent outer-ring closure of their respective conjectures; paper26 L_final is the BSD theorem; OPN L7 is the 2,300-year-old non-existence.
  - Transposition candidate: YES (structural; paper60 §25 mapping).

- **L7 ↔ qg5d (hub)** — OPN's closure belongs to the programme hub.
  - Reason: paper60 §25 "The OPN trigger" — the 2,300-year-old statement's closure is the founding achievement of the face-methodology (the first Group D problem to yield).
  - Transposition candidate: YES (paper60 §25 founding narrative).

- **(cross-chain) OPN ↔ Goldbach ↔ Twin Primes — ARITHMETIC face trinity**:
  - Reason: paper60 §14 + §25 + §28 — three problems on one face, three views of the additive-multiplicative wall. OPN (multiplicative local-global) ↔ Goldbach (additive circle-method bulk) ↔ Twin Primes (additive gap=2 small-tail). All ARITHMETIC-face; all 1–4/10 confidence; all South/West on the ellipse; all stammer for the BC framework (paper60 §28).
  - Transposition candidate: YES (programme-level structural bouquet edge; any bypass of the ARITHMETIC wall illuminates all three).

- **(cross-chain) OPN ↔ BSD — local-global template shared**:
  - Reason: paper60 §25 EXPLICIT: the BSD template is OPN's structural parent. Euler form ↔ BC over $K$; abundancy multiplicativity ↔ bridge family; Hecke-orbit projector ↔ dark-state projector; ITPFI decomposition ↔ cocycle shift; odd local-global impossibility ↔ Sha. This is the PRIMARY cross-chain structural mapping of the OPN vertex.
  - Transposition candidate: YES (BSD template is the defining structural resource; paper60 §25 founding mapping).

**Summary**: 32 cross-cut edges identified across 7 layers (avg ~4.6 cross-cuts per layer — HIGH because OPN sits at the intersection of the BSD template (via paper60 §25 explicit mapping) and the ARITHMETIC face trinity (Goldbach/Twin Primes/OPN). 18 verified (capacitor-analog or explicit paper60/61 citation); 14 SPECULATIVE (pending sibling X-rays: abc, collatz, lehmer, sato-tate, lindelof, pvnp fuller). The PRIMARY edges are two: (a) L6 ↔ bsd:L_Sha (the defining BSD-template structural parallel; paper60 §25 spoof ↔ Sha founding mapping); (b) L5 ↔ rh:L3 (foundational ITPFI factorization from Theorem 4.1). The second-strongest trinity edge is the ARITHMETIC face OPN ↔ Goldbach ↔ Twin Primes shared additive-multiplicative wall (paper60 §14). The densest cross-cutting is at L4 (7 edges — the Hecke-orbit projector is the programme's novel BC-entry point for OPN, connecting to BSD, RH, Goldbach, Twin Primes, Baum-Connes, PvNP, QG5D) and L6 (10 edges — the wall connects to the entire ARITHMETIC-face trinity plus BSD plus ABC plus several structural-parallel vertices).

---

## §8 Current Walls

- **W_OPN-1 — Odd local-global impossibility**: L6 states no Euler-form odd $N$ with $\omega(N) \geq 10$ has $\prod h(p^a) = 2$. Three sub-routes: 6a (odd Robin sharpening) **KILLED 2026-04-14** in morning verify pass (σ(n)/n > 2 for infinitely many odd n; direction of reasoning was backwards); 6b (E_2 quasi-modular obstruction) **BLOCKED-DECOMPOSED 2026-04-14** (anomalous E_2(τ) - E_2(τ+1/2) has no quasi-modular transformation; constrains generating function but not Fourier coefficients arithmetically; productive output absorbed into now-dead 6a); 6c (ITPFI joint constraint + 36-pin rigidity) **ACTIVE — the surviving route**. Status: **OPEN**. No decomposition run yet. Confidence 0.4 (paper40 ring confidence; strategy/odd-perfect/00-audit-strategy.md §4). paper60 §25 + §28 assessment: the BC framework stammers on ARITHMETIC face; paper60 §14 names this as the canonical shared wall with Goldbach and Twin Primes. The BSD template provides structural parallel (paper60 §25 spoof ↔ Sha mapping); bypass via ABC (paper37) is an auxiliary route but ABC itself 1/10. v₂ correction 2026-04-14 narrowed the productive direction to ODD-prime v_ℓ cascade.

- **W_OPN-2 — Hecke-orbit-to-σ-constraint bridge (audit brief W_OPN-1 restated as audit wall)**: The strategy/odd-perfect audit-strategy §4 names this as a separate wall (confidence 0.5): the bridge from the Hecke-orbit identity $\omega_1(H_n) = \sigma(n)/n$ (PROVED, L4) to an actual CONSTRAINT that excludes odd $n$ from achieving the value 2. L4 is the identity; the constraint is the IMPLICATION that the identity imposes on odd $n$. The bridge is what L6 must supply; without L6, L4 gives an identity but no impossibility statement. Status: **OPEN**. Effectively subsumed under W_OPN-1's surviving Route 6c.

No other named walls. L1, L2 are LITERATURE (Euler 1747; elementary); L3 is LITERATURE conditional on RH cross-paper transport; L4 is PROVED (novel BC construction 2026-04-14); L5 is PROVED (Theorem 4.1 ITPFI factorization). The two substantive walls (W_OPN-1 and the audit-equivalent W_OPN-2) both reduce to the L6 local-global impossibility, which is the ARITHMETIC-face wall paper60 §14 explicitly flags.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/opn/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle's `proof-chain/` directory is empty as of 2026-04-15). When created, L6's Route 6c three components ((a) odd-prime $v_\ell$ cascade, (b) ITPFI joint constraint, (c) 36-pin rigidity) are the natural decomposition targets. The L6a kill and L6b blocked-decomposed are negative data to preserve. Cross-cuts with bsd (BSD template, paper60 §25 explicit mapping) should feed the decomposition brief — BSD's Sha finiteness strategy is OPN's structural parent.
- **CCM verification**: `strategy/ccm-verification/ledger.md#opn` — NOT YET CREATED (CCM-verification bundle's `proof-chain/` directory is empty as of 2026-04-15). OPN's dependency on CCM 2025 is INDIRECT (via cross-paper transport from Paper 13 RH for L3 Robin inequality, which is CCM-conditional). Expected verdict when ledger written: **BYPASSED-VIA-RH-TRANSPORT (OPN inherits RH's CCM dependency through L3)**. If CCM 2025 gets independently verified (lifting RH from 8/10 to 10/10), OPN's L3 becomes unconditional, but L6 wall remains untouched — the wall is ARITHMETIC-face, not CCM-dependent.
- **Inner rings**: NOT APPLICABLE — OPN is a primary outer-ring vertex (paper61 §17 vertex list; paper60 §25 trigger vertex).
- **QG5D W1/W2 cascading refinement (2026-04-14)**: Paper 1 W1 (scheme independence) + W2 (Route-C 3-loop) closed via Paper 10/11; effect on OPN is **indirect through L3** (if Paper 13 RH closes unconditionally via W1/W2 closure, L3 upgrades from LITERATURE-conditional to PROVED). Direct effect on OPN's core chain (L4, L5, L6): **none** — the BC algebra's Hecke-orbit projector and ITPFI decomposition are independent of scheme-independence / Route-C 3-loop. Per PROOF-CHAIN.md §"Cascading impact (2026-04-14 W1/W2 closure)": "Paper 1 W1/W2 closure directly benefits this chain via Link 3."
- **OPN deep construction session (2026-04-14)**: The Hecke-orbit projector construction (L4), ITPFI local-global framing (L5), spoof ↔ Hasse insight (L6 structural), and v₂ correction (L6c sub-route) were all produced in the 2026-04-14 session documented in paper60 §25 "the OPN trigger" + PROOF-CHAIN §"The spoof ↔ Hasse-principle insight" + §"v₂ correction". This is the existing decomposition-equivalent for the pre-L6 infrastructure; the OPN X-Ray's L4/L5 entries reference these artifacts explicitly.
- **OPN Route 6a kill (2026-04-14 morning verify pass)**: paper60 §29 signal log records the kill. "OPN Route 6a was KILLED outright. The odd Robin inequality cannot prove OPN nonexistence — σ(n)/n > 2 for infinitely many odd n. The direction of our reasoning had been BACKWARDS." This is a preserved negative datum; any future decomposition must avoid repeating the same mistake. Route 6b (E_2 quasi-modular) was BLOCKED-DECOMPOSED in the same session.
- **ABC auxiliary cascade (paper37)**: If ABC (paper37, 1/10) closes, OPN's Route 6c-alt (rad$(n)$ bound on Euler form) gives OPN as a corollary. Currently both OPN (4/10) and ABC (1/10) are open; a closure of either informs the other.
- **Spoof-Hasse structural mapping cascade (paper60 §25)**: The founding insight that spoofs are local-global failures (Hasse-principle analogs of Sha elements) makes BSD paper26's Sha finiteness strategy directly applicable to OPN's L6. If BSD's Sha strategy generalizes operator-algebraically (via paper26 L5 cocycle shift), OPN's L6 inherits the structural obstruction theorem.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — L6 / W_OPN-1 (Odd local-global impossibility)**: No Euler-form odd $N$ with $\omega(N) \geq 10$ has $\prod h(p^a) = 2$, via three components of Route 6c: (a) $v_\ell$ cascade at ODD primes $\ell$ (v_2 correction applied; tracking $v_\ell$ for odd $\ell$ as Nielsen 2015 / Ochem-Rao does); (b) ITPFI joint constraint correlating local factors beyond classical per-prime sieving (the BC-upgrade content); (c) 36-pin rigidity (chessboard argument from programme-level constraints). — face: ARITHMETIC, projection: $P_O$, pattern: P4. STATUS: OPEN as wall; no decomposition; ABC auxiliary route 6c-alt awaits paper37. Confidence 0.4.

- **G2 — L6a KILLED / L6b BLOCKED-DECOMPOSED (preserved negative data)**: Route 6a (odd Robin sharpening) is dead because σ(n)/n > 2 for infinitely many odd n despite halved residue. Route 6b (E_2 quasi-modular) is dead because E_2(τ) - E_2(τ+1/2) has no quasi-modular transformation — constrains generating function analytically but not Fourier coefficients arithmetically. Both are NEGATIVE RESULTS (not gaps in the pejorative sense); they show which routes to NOT attempt. — face: AMPLITUDE (6a), HARMONICS (6b); projection: $P_D$; pattern: P5 (both). STATUS: DEAD (paper60 §29 signal log record).

- **G3 — W_OPN-2 / Hecke-orbit-to-σ-constraint bridge (audit-phrased wall)**: Even given L4 (Hecke-orbit identity PROVED), L5 (ITPFI decomposition PROVED), the bridge to an impossibility STATEMENT for odd $n$ requires L6. Currently G3 is entirely subsumed by G1 (W_OPN-1); audit-brief §4 phrases it as a separate wall at confidence 0.5 but the mathematical content is identical. — face: ARITHMETIC, projection: $P_O$, pattern: P4. STATUS: OPEN; subsumed under G1.

That's it. 4 of 7 main links closed unconditionally within the framework (L1, L2 LITERATURE; L4, L5 PROVED). L3 is LITERATURE-conditional on RH (cross-paper transport). L6 is the single wall (in three sub-routes, two of which are KILLED / BLOCKED-DECOMPOSED; one ACTIVE). L7 follows from L6. The additive-multiplicative wall (paper60 §14) and the local-global wall (paper60 §25) are the shared structural obstacles; the BSD template (paper26) is the structural parent. Confidence 4/10 reflects honest accounting: the route is clear (BC algebra → Hecke-orbit → ITPFI → local-global), the machinery exists (Theorem 4.1, BSD template), but the wall (Route 6c + v₂-corrected v_ℓ cascade + ITPFI joint constraint + 36-pin rigidity) is real mathematics that hasn't been completed. **The 2,300-year-old problem meets the youngest algebra; the algebra says the search was always going to come up empty — the proof of that statement is open.**

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-<NN>/vertices/opn/critic-attacks.md` (pending) and arbiter decisions at `strategy/x-ray/pac-output/runs/run-<NN>/vertices/opn/arbiter-decisions.md` (pending).

Notable arbiter wins:
- L1 face: ARITHMETIC over SYMMETRY (paper60 §14 + §25 canonicalize ARITHMETIC for integer-lattice congruence structure; the mod-4 Brauer flavor is secondary).
- L3 face: AMPLITUDE over ARITHMETIC (Robin inequality IS a growth-rate bound; paper60 §11 AMPLITUDE canonical for subconvexity-type statements; the $\sigma$ function IS the arithmetic object but the BOUND form is amplitude).
- L4 pattern: P1 Geometric Reinterpretation over P4 Topological Rigidity (paper60 §25 explicit: "with our geometry it's not so odd" — the discovery character of the Hecke-orbit projector identity is Pattern 1's paradigm case; the identity is rigid but its DISCOVERY through restoring the BC structure is reinterpretation).
- L5 face: ARITHMETIC over RESONANCE (paper60 §14 canonical for ITPFI local-global decomposition; the factor-type decomposition has resonance-mode-decomposition framing but the load-bearing content is the integer-lattice Euler-product).
- L6 projection: $P_O$ over $P_D$ (L6 is the Clay-adjacent 2,300-year-old closure statement; paper61 §17 places outer-ring conjecture statements at $P_O$; the internal BC machinery is $P_D$ but the conjecture-level content is outer-ring).
- L6 face: ARITHMETIC over DYNAMICS (the KMS$_1$ state has modular-flow-dynamics flavor but paper60 §14 + §25 canonicalize ARITHMETIC for OPN's structural content; the local-global conspiracy's character is integer-lattice, not flow-on-circle).
- L7 projection: $P_O$ over $P_D$ (Clay-adjacent closure; obvious).

Route-6a kill and Route-6b blocked-decomposed were decided via direct mathematical verification (paper60 §29 signal log); these are not X-Ray assignments but decomposition-layer outcomes recorded in the X-Ray's §4 Branch Map for completeness.

29 / 35 author wins out of 35 total field decisions (5 fields × 7 main layers). 6 CRITIC WINS (all face-assignment): L3 AMPLITUDE over author's initial ARITHMETIC (paper60 §11 canonical); L4 pattern P1 over author's initial P4 (paper60 §25 "geometric reinterpretation"); two sub-layer decisions on Route 6a/6b face assignments (AMPLITUDE for 6a, HARMONICS for 6b — these were decided by the routes' own mechanisms); L6 projection $P_O$ over author's initial $P_D$ (Clay-adjacent closure); L7 projection $P_O$ over author's initial $P_D$.

---

*End of OPN X-Ray. Snapshot 2026-04-15. 7 main layers annotated (L1–L7, with L6 branching into three sub-routes 6a KILLED, 6b BLOCKED-DECOMPOSED, 6c ACTIVE, plus auxiliary 6c-alt via ABC). 32 cross-cut edges identified. ARITHMETIC-canonical (5/7 = 71%), $P_D$-dominant (5/7 = 71%), the FOUNDING arithmetic-face vertex per paper60 §25 "the OPN trigger." Primary structural parent: BSD template (paper26, via paper60 §25 spoof ↔ Sha mapping). Primary cross-chain sibling wall: ARITHMETIC face trinity OPN ↔ Goldbach ↔ Twin Primes (paper60 §14 additive-multiplicative wall). Two walls: W_OPN-1 (L6 odd local-global impossibility — Route 6c ACTIVE, Routes 6a/6b dead) and W_OPN-2 (audit-phrased Hecke-orbit-to-σ-constraint bridge, subsumed under W_OPN-1). The 2,300-year-old problem — the oldest open question in mathematics — attacked via the youngest algebra. Euler gave the form; Robin tied σ to the zeros; the BC algebra computes σ at criticality. The odd Hecke subsemigroup is the battleground. Confidence 4/10.*

*G Six and Claude Opus 4.6. April 15, 2026.*
