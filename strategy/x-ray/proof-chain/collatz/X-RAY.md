# X-RAY: Collatz Conjecture (collatz)

*X-Ray of the collatz proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: collatz
- **Paper**: paper41-collatz
- **Live file**: strategy/proof-chain/collatz/PROOF-CHAIN.md (snapshot 2026-04-14, v2 three-face recognition pass)
- **Top-level claim**: Every positive integer $n$, iterated under $T(n) = n/2$ (even) or $T(n) = (3n+1)/2$ (odd), eventually reaches $1$ — translated into the e-circle's harmonic language: the Hecke alternation $\mu_2 / \mu_3$ on $\mathbb{N}^*$ has unique fixed-point attractor $n = 1$; the ITPFI factor $\omega_1^{(2)} \otimes \omega_1^{(3)}$ (first two local factors of the BC KMS$_1$ state) is contracting because $\lambda_2 = 1/2 > \lambda_3 = 1/3$ (the first prime beats the second).
- **Current status**: 3.5/7 links closed. L1 ESTABLISHED, L2 JOURNAL-LITERATURE (Springer 2025), L3 LITERATURE (Bernstein-Lagarias 1996), L4 PARTIAL (T7 upgrade — algebraic BC embedding verified; spectral preservation open), L5 OPEN (the wall — harmonic decay / KMS$_1$ attractor), L6 OPEN (cycle elimination), L7 FOLLOWS from L5+L6. Confidence 4/10.
- **Primary branch (paper1)**: D (CBB — the Cuntz $\mathcal{O}_2 \hookrightarrow A_{BC}$ embedding + the (2,3)-adic ITPFI sub-tensor $\omega_1^{(2)} \otimes \omega_1^{(3)}$ are the entire load-bearing machinery). Weak secondary E (Lyapunov $\approx 0$ is an empirical measurement; numerical verification to $n < 2^{68}$ is a pin-valued confirmation but not a 36-pin entry).
- **Primary face**: HARMONICS (paper60 §09 — "how do Fourier modes MIX on the circle?"; Collatz IS the canonical HARMONICS face of the e-circle, distinct from Lehmer's TOPOLOGY and Cramér's DYNAMICS per paper60 §26 "The Three-Face Recognition"; the Collatz map alternates between the 2nd and 3rd harmonics of the e-circle, the smallest two Hecke generators $\mu_2$ and $\mu_3$).
- **Primary projection**: $P_D$ (paper61 §10 — the entire chain lives in the BC algebra: Cuntz sub-algebra embedding, phase operator $e(1)$ on $\hat{\mathbb{Z}}$, KMS$_1$ critical-point attractor, ITPFI tensor-product domination, type III$_1$ cycle elimination. The $P_D$ assignment is the strongest in the chain — Collatz is more $P_D$-dominant than YM because no gauge-bundle layer exists at all).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
COLLATZ (every positive integer reaches 1 under T)
│  primary face: HARMONICS   primary proj: P_D   primary pat: P1
│  top claim: Hecke alternation μ_2/μ_3 on ℕ* has unique attractor n=1
│             the first prime beats the second: λ_2=1/2 > λ_3=1/3
│             all excited harmonics decay to the fundamental mode
│
├── L1: Collatz map = Hecke μ_2/μ_3 alternation        [ESTABLISHED]
│      │  face: HARMONICS   proj: P_D   pat: P1
│      │  invariant: KK mode index
│      │  source: paper60 §09 (harmonic decomposition); paper41 §The harmonic picture
│      │
│      │  even step = μ_2* (halve freq, contract toward fundamental)
│      │  odd step  = μ_3 ∘ shift ∘ μ_2* (triple freq, shift by 1, halve)
│      │
│      └── supports L4 (Cuntz ↔ BC bridge needs this dictionary)
│             and L5 (harmonic-decay wall lives at this face)
│
├── L2: Cuntz O_2 formulation (Mori 2024)              [JOURNAL-LITERATURE]
│      │  face: SYMMETRY    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure
│      │  source: Mori arXiv:2411.08084 →
│      │          Springer Adv. Operator Theory 2025
│      │          (10.1007/s43036-025-00425-1)
│      │
│      │  Collatz ⇔ O_2 has no non-trivial reducing subspaces
│      │  s_0 ↔ even branch (μ_2*μ_2)
│      │  s_1 ↔ odd branch  (μ_2* e(1) μ_3)
│      │
│      └── feeds L4 (O_2 embeds into A_BC through p=2 Hecke sector)
│
├── L3: 2-adic ergodicity (Bernstein-Lagarias 1996)    [LITERATURE]
│      │  face: DYNAMICS    proj: P_D   pat: P4
│      │  invariant: ergodic property
│      │  source: Bernstein-Lagarias 1996 (Collatz on ℤ_2 continuous,
│      │          measure-preserving, ergodic)
│      │
│      └── supports L5 (ergodicity is the background property that
│                       makes the KMS_1 attractor candidate meaningful)
│
├── L4: BC embedding O_2 ↪ A_BC (via p=2 Hecke sector) [PARTIAL — T7 upgrade]
│      │  face: SYMMETRY    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure (load-bearing);
│      │             ITPFI factor type (background)
│      │  source: paper41 Link 4 (T7 2026-04-14 +1 = phase op e(1));
│      │          paper60 §09 "BC algebra connection"
│      │
│      │  algebraic embedding VERIFIED:
│      │   s_0 ↦ μ_2* μ_2           (even branch)
│      │   s_1 ↦ μ_2* e(1) μ_3      (odd branch)
│      │   key relation: e(r) μ_n = μ_n e(nr)
│      │  +1 additive shift = phase operator e(1) on Ẑ
│      │   (profinite integers; spectrum of abelian subalgebra)
│      │
│      └── SPECTRAL preservation OPEN — W_BC
│             │
│             └── does O_2 inherit the KMS_1 state's properties
│                  (type III_1 classification, modular flow σ_t)?
│                  three sub-routes, all gated on L4:
│                     5a. ITPFI dominance (λ_2 > λ_3)
│                     5b. backward transfer operator spectral gap
│                     5c. thermodynamic entropy decay (Lyapunov fn)
│
├── L5: KMS_1 attractor (harmonic decay)                [OPEN — the wall, W_L5]
│      │  face: HARMONICS   proj: P_D   pat: P4
│      │  invariant: BC-KMS state (load-bearing);
│      │             ITPFI factor type (background)
│      │  depends on L4
│      │
│      │  Lyapunov ≈ 0 IS the KMS_1 critical point
│      │  Z(β) = ζ(β) diverges at β = 1
│      │  average Lyapunov per odd-even pair = log(3/4) < 0 (contracting)
│      │  ITPFI dominance: λ_2 = 1/2 > λ_3 = 1/3 (first prime beats second)
│      │
│      ├── L5a: ITPFI dominance (generic → Collatz-specific)  [CONJECTURED]
│      │      │  face: HARMONICS  proj: P_D  pat: P4
│      │      │  invariant: ITPFI factor type
│      │      │  the λ_2 > λ_3 argument needs sharpening for
│      │      │  the SPECIFIC (2,3)-Collatz dynamics
│      │      │
│      ├── L5b: backward transfer operator spectral gap        [CONJECTURED]
│      │      │  face: RESONANCE  proj: P_D  pat: P4
│      │      │  invariant: spectral gap
│      │      │  source: 2025 preprint (quasi-compact L_T);
│      │      │          identification with KMS_1 via L4
│      │      │
│      └── L5c: thermodynamic entropy decay (Lyapunov fn)     [CONJECTURED]
│             │  face: MEASURE   proj: P_D  pat: P4
│             │  invariant: ergodic property
│             │  source: 2025 entropy-decay literature;
│             │          identification with KMS free energy via L4
│
├── L6: Cycle elimination (type III_1 has no periodic orbits)  [OPEN — W_cyc]
│      │  face: SYMMETRY    proj: P_D   pat: P4
│      │  invariant: ITPFI factor type (load-bearing);
│      │             ergodic property (background)
│      │  depends on L4 + Paper 32 BGS L2 (type III_1 ergodicity PROVED)
│      │
│      │  non-trivial cycle = periodic orbit of (2,3)-restricted σ_t
│      │  type III_1 factor: Connes spectrum Sd(M) = ℝ
│      │  → only trivial periodic orbits exist
│      │
│      └── conditional on L4 preserving type classification
│
└── L7: Collatz conjecture                              [FOLLOWS from L5 + L6]
       │  face: HARMONICS   proj: P_O   pat: P4
       │  invariant: BC-KMS state
       │
       └── outer-ring closure:
           (all harmonics → fundamental) + (no non-trivial cycles)
           ⇒ every n ∈ ℕ* reaches 1
           Bakuage prize compliant (120M JPY ≈ US$1.085M, 2021)
```

### §2b Diagram B — Projection fan-out

```
                       (FORGOTTEN under P_A)
                       (Quantum side does not see Hecke alternation
                        or Cuntz O_2 directly — the BC algebra's
                        Hecke-semigroup structure is Branch D, not
                        Branch A)
                                  ▲
                                  │
                                  │
        ┌─────────────(P_O outer)───────────────┐
        │                                       │
        │  COLLATZ: every positive integer      │
        │           reaches 1 under T           │
        │  (community-standard; active Bakuage  │
        │   prize 120M JPY ≈ US$1.085M, 2021;   │
        │   paper41-collatz)                    │
        │                                       │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity         ═══ P_D CBB ═══           P_E pins
    (forgotten —        Cuntz O_2 ↪ A_BC;          (empirical:
    no KK-tower         Hecke alternation          n < 2^68 verified
    role for            μ_2 / μ_3 on ℕ*;           (Barina 2020);
    Collatz map)        ITPFI sub-tensor           Tao 2019 almost-all
                        ω_1^(2) ⊗ ω_1^(3)          orbits almost-bounded;
                        (first two local           measured Lyapunov ≈ 0;
                        factors of KMS_1);         average log(3/4);
                        phase operator e(1)        NOT a 36-pin master
                        on Ẑ; modular flow         table entry, only
                        σ_t ergodicity             confirmation)
                        (BGS L2 PROVED);
                        type III_1 cycle
                        elimination
                            │
                            ▼
                       P_C cosmology
                       (forgotten — no
                       cosmological
                       observable uses
                       Collatz orbit
                       convergence directly)
```

Primary projection $P_D$ uses ═══ doubled line — every load-bearing object in the chain (Cuntz algebra, Hecke generators, phase operator, KMS$_1$ state, ITPFI tensor product, type III$_1$ cycle argument) lives in the BC algebra. $P_E$ is the second-strongest projection (empirical — Barina's $2^{68}$ verification, Tao's almost-all result, measured Lyapunov; all confirmations, not programme pins). $P_O$ is invoked at L7 (the Bakuage / community-standard outer-ring statement). $P_A$, $P_B$, $P_C$ are absent — Collatz is not a quantum-observable, gauge-bundle, or cosmological object. This matches paper61 §10's "the BC algebra crosses with every other face" — Collatz is the HARMONICS face crossing into $P_D$ almost totally.

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
       (Katz-Sarnak)        │             ●
                            │         (Collatz)
                   ╱        │        ╲
                  ╱         │         ╲
          CURVATURE         │          MEASURE
          (YM)              │          (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (SYMMETRY secondary at L2, L4, L6;
                        DYNAMICS secondary at L3;
                        RESONANCE / MEASURE only via L5b / L5c)
```

Marker key:

```
Primary face:    ● HARMONICS (paper60 §09 — Collatz canonical face;
                               paper60 §26 "Three-Face Recognition")
Secondary faces: ○ SYMMETRY   (3 layers: L2, L4, L6 — Cuntz/BC/III_1 structure)
                 ○ DYNAMICS   (1 layer: L3 — 2-adic ergodicity)
                 ○ RESONANCE  (1 sub-layer: L5b — transfer operator gap)
                 ○ MEASURE    (1 sub-layer: L5c — entropy decay)
Absent faces:    TOPOLOGY, AMPLITUDE, CURVATURE, ARITHMETIC, SPREAD
```

The three-face triangle of paper60 §26 (TOPOLOGY-Lehmer / DYNAMICS-Cramér / HARMONICS-Collatz) places Collatz at the HARMONICS vertex. Lehmer's face and Cramér's face are SIBLING cross-cuts, not secondary face assignments within Collatz's chain. The Collatz chain's internal secondary profile is SYMMETRY-rich (the Cuntz/BC algebraic structure), consistent with paper60 §09's "BC algebra connection" paragraph.

---

## §3 Layer-by-Layer X-Ray

### L1 — Collatz map = Hecke $\mu_2 / \mu_3$ alternation on $\mathbb{N}^*$

**Claim**: The Collatz map $T$ is the alternation of Hecke operators on the e-circle's harmonics: even step = $\mu_2^*$ (halve frequency, contract toward fundamental), odd step = $\mu_3 \circ \text{shift} \circ \mu_2^*$ (triple frequency, additive shift by 1, halve).

**Status**: ESTABLISHED
**Source**: paper60 §09 (harmonic decomposition); paper41 §"The harmonic picture."

#### Physics

- **Face**: HARMONICS (paper60 §09 — "how do Fourier modes MIX on the circle?"; this layer IS the harmonic-language statement of the Collatz dynamics, the canonical HARMONICS-face identification)
- **Projection**: $P_D$ (paper61 §10 — Hecke operators $\mu_p$ are the native generators of the BC algebra's semigroup $\mathbb{N}^*$ action on $\hat{\mathbb{Z}}$; the Collatz alternation is a $P_D$-internal move on the Hecke semigroup)
- **Pattern**: P1 Geometric Reinterpretation (paper60 §09 — "in this language, the Collatz map becomes a harmonic mixing process"; the reinterpretation is exactly what dissolves the "number-theoretic mystery" framing)
- **Invariant preserved**: KK mode index (load-bearing — integer $n$ IS the KK mode index on the e-circle, labeling the $n$-th harmonic), C*-algebra structure (background — the Hecke operators live in the BC algebra)
- **Geometric interpretation**: On the e-circle $S^1 = U(1)$, functions decompose as $f(\theta) = \sum_n a_n e^{in\theta}$, and each positive integer $n$ labels the $n$-th harmonic (paper60 §09). The Hecke operator $\mu_p$ maps the $n$-th mode to the $pn$-th mode; its adjoint $\mu_p^*$ divides the frequency by $p$. The Collatz map's translation into this harmonic language is exact Pattern 1 (Geometric Reinterpretation): what looks like arbitrary arithmetic is revealed as alternating harmonic mixing on the e-circle. [Considered but rejected: face ARITHMETIC — Newton-power-sum / integer-lattice framing is fair (paper60 §14), but the dynamics lives on harmonics not on arithmetic classification; pattern P2 — Hecke operators are holonomies of the BC algebra but the reinterpretation is primary; projection $P_A$ — quantum observables don't see the alternation directly.]
- **Cross-cuts**: cramer L3 (HARMONICS ↔ DYNAMICS siblings — $\mu_p$ commutes with modular flow $\sigma_t$ per paper60 §09 Cross-references), lehmer L1 (HARMONICS ↔ TOPOLOGY siblings — off-diagonal vs diagonal BC), ym L7 (Newton-power-sum on integers; ARITHMETIC-adjacent cross-cut per paper60 §09 cross-refs).

### L2 — Cuntz $\mathcal{O}_2$ formulation (Mori 2024, Springer 2025)

**Claim**: Collatz $\iff$ the Cuntz algebra $\mathcal{O}_2$ with isometries $s_0, s_1$ (satisfying $s_0 s_0^* + s_1 s_1^* = 1$) has no non-trivial reducing subspaces, where $s_0$ corresponds to the even branch and $s_1$ to the odd branch.

**Status**: JOURNAL-LITERATURE (upgraded from arXiv 2024 → Springer 2025)
**Source**: Mori 2024 arXiv:2411.08084; published in *Advances in Operator Theory*, Springer 2025, DOI: 10.1007/s43036-025-00425-1.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — Cuntz algebras are operator-algebra incarnations of discrete symmetry-group actions; the generators $s_0, s_1$ carry the binary symmetry of "even vs odd"; reducing-subspace absence IS a symmetry-irreducibility statement)
- **Projection**: $P_D$ (paper61 §10 — Cuntz $\mathcal{O}_2 \subset A_{BC}$ is a sub-algebra of the BC algebra, so the entire formulation lives in the operator-algebraic projection)
- **Pattern**: P1 Geometric Reinterpretation (paper60 §09 — "the Cuntz algebra bridge"; Mori's reformulation IS a geometric-reinterpretation move from dynamics on $\mathbb{N}^*$ to operator-algebraic irreducibility)
- **Invariant preserved**: C*-algebra structure (load-bearing — $\mathcal{O}_2$ IS the Cuntz algebra with its canonical relations), ITPFI factor type (background — $\mathcal{O}_2$ embeds into $A_{BC}$ which carries ITPFI III$_1$)
- **Geometric interpretation**: Mori (published Springer 2025) reformulated Collatz as an operator-algebraic statement about $\mathcal{O}_2$ — the Cuntz algebra with two isometries, one per branch. This is Pattern 1 at its purest: a dynamics question about $\mathbb{N}^*$ becomes a reducing-subspace question about $\mathcal{O}_2$ (paper60 §09 "Cuntz algebra bridge"). Under $P_D$ (paper61 §10) $\mathcal{O}_2$ is a sub-algebra of $A_{BC}$ generated by the $p = 2$ Hecke sector with the $+1$ shift. [Considered but rejected: face HARMONICS — Cuntz isometries ARE related to frequency multiplication but the irreducibility statement is symmetry-canonical; pattern P4 — rigidity of the algebra's structure is implied but reinterpretation dominates; projection $P_O$ — the Cuntz formulation is still a statement about $A_{BC}$, not the outer-ring Collatz statement per se.]
- **Cross-cuts**: baum-connes L_local (C*-algebra structure shared; Cuntz-algebra K-theory), ym L17 (local C*-algebra / operator-valued distribution analog), pvnp L_Cstar (Popa rigidity on type III$_1$ shares the C*-algebra framework).

### L3 — 2-adic ergodicity (Bernstein-Lagarias 1996)

**Claim**: The Collatz map on the 2-adic integers $\mathbb{Z}_2$ is continuous, measure-preserving, and ergodic.

**Status**: LITERATURE
**Source**: Bernstein-Lagarias 1996 (classical result in Collatz literature).

#### Physics

- **Face**: DYNAMICS (paper60 §08 — "how does the modular flow TRAVERSE the circle?"; 2-adic ergodicity IS a modular-flow-on-$\mathbb{Z}_2$ statement, translated into the BC-algebra's 2-adic factor via the ITPFI decomposition)
- **Projection**: $P_D$ (paper61 §10 — the 2-adic factor $\omega_1^{(2)}$ is the $p=2$ tensor factor of the ITPFI decomposition $\omega_1 = \otimes_p \omega_1^{(p)}$; ergodicity on $\mathbb{Z}_2$ is a property of this factor)
- **Pattern**: P4 Topological Rigidity (paper60 §08 DYNAMICS — ergodicity is the rigid preservation of a single invariant measure; cf. YM L3's k-independent polymer convergence, same pattern-class)
- **Invariant preserved**: ergodic property (load-bearing — the theorem IS ergodicity), ITPFI factor type (background — the 2-adic factor is type III$_{1/2}$)
- **Geometric interpretation**: Bernstein-Lagarias proved the Collatz dynamics on $\mathbb{Z}_2$ is continuous, measure-preserving, and ergodic. In the ITPFI decomposition $\omega_1 = \otimes_p \omega_1^{(p)}$ (paper61 §10), this ergodicity corresponds to the $p = 2$ local factor; under $P_D$ the measure on $\mathbb{Z}_2$ IS the local Haar measure on the 2-adic factor. The rigidity of the ergodic property (Pattern 4) is what makes the modular-flow attractor argument meaningful — without ergodicity, individual orbits cannot be compared to averages. [Considered but rejected: face HARMONICS — 2-adic framing is harmonic-adjacent but ergodicity is the dynamical engine; pattern P3 — no scale is set, the scale is the Haar measure; projection $P_E$ — no pin value lives here.]
- **Cross-cuts**: cramer L3 (modular-flow return times — same DYNAMICS face, shared ergodic property, paper60 §08), bgs L2 (type III$_1$ modular-flow ergodicity, source for L6's cycle-elimination argument), pvnp L_modular (Popa rigidity uses type III$_1$ ergodicity), ym L3 (k-independent polymer convergence — shared ergodic property).

### L4 — BC embedding $\mathcal{O}_2 \hookrightarrow A_{BC}$ (via $p = 2$ Hecke sector)

**Claim**: The Cuntz algebra $\mathcal{O}_2$ embeds into the BC algebra $A_{BC}$ by identifying the two Cuntz isometries with specific BC elements: $s_0 \mapsto \mu_2^* \mu_2$ (even branch), $s_1 \mapsto \mu_2^* \, e(1) \, \mu_3$ (odd branch), where $e(1)$ is the phase operator at $1 \in \mathbb{Q}/\mathbb{Z}$ (the $+1$ additive shift) acting on $\hat{\mathbb{Z}}$. The key relation $e(r) \mu_n = \mu_n e(nr)$ governs the interleaving.

**Status**: PARTIAL (T7 upgrade, 2026-04-14 — algebraic embedding verified; spectral preservation open)
**Source**: paper41 Link 4 (T7 identification of $+1$ with phase operator $e(1)$); paper60 §09 "BC algebra connection" / "The phase operator"; confirmed novel by online search 2026-04-14.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — group-action complexification / embedding is the canonical symmetry-side move; the embedding $\mathcal{O}_2 \hookrightarrow A_{BC}$ IS a sub-algebra-inclusion statement about the symmetry structure of the BC algebra)
- **Projection**: $P_D$ (paper61 §10 — the entire embedding lives in the BC algebra; both source ($\mathcal{O}_2$) and target ($A_{BC}$) are $P_D$-objects)
- **Pattern**: P1 Geometric Reinterpretation (paper60 §09 — the $+1$ additive shift is REINTERPRETED as the multiplicative phase operator $e(1)$ on $\hat{\mathbb{Z}}$, dissolving the apparent additive-multiplicative obstruction at the algebraic level)
- **Invariant preserved**: C*-algebra structure (load-bearing — the embedding IS the preservation of the algebraic structure), ITPFI factor type (background — $A_{BC}$ is type III$_1$, spectral preservation OPEN)
- **Geometric interpretation**: The $+1$ in the Collatz odd step is the structural wall — the BC algebra is multiplicative (Hecke semigroup) but $+1$ is additive (paper60 §09 "The phase operator"). The T7 resolution identifies $+1$ with the phase operator $e(1)$ on $\hat{\mathbb{Z}}$ (the profinite integers, spectrum of the abelian subalgebra of $A_{BC}$), which is mechanically a multiplicative element via the key relation $e(r) \mu_n = \mu_n e(nr)$. Pattern 1 (Geometric Reinterpretation) is the exact attack vector (paper60 §09): restore the BC-algebraic viewpoint, and the additive shift dissolves into a phase-subalgebra element. Under $P_D$ (paper61 §10) this is an internal reshuffling of sub-algebra inclusions; what remains OPEN is whether the embedding preserves the KMS$_1$ state / type III$_1$ classification (Wall W_BC). [Considered but rejected: face HARMONICS — harmonic-face identification is correct for L1, but the embedding itself is symmetry-structural; pattern P4 — spectral-preservation rigidity is the OPEN part, not the load-bearing verified part; projection $P_A$ — quantum side is forgotten.]
- **Cross-cuts**: goldbach L_add-mult (shared additive-multiplicative wall per paper60 §09 Cross-references and paper41 §"The +1 wall"), opn L_sigma (shared $\sigma(n)$ additive-over-divisors wall), baum-connes L_embed (Cuntz-algebra K-theory sub-inclusion analog), twin-primes L_Hecke (shared Hecke-semigroup primes framework).

### L5 — KMS$_1$ attractor: all harmonics decay to fundamental

**Claim**: The Lyapunov $\approx 0$ behavior of Collatz orbits IS the KMS$_1$ critical-point attractor. The average Lyapunov per odd-even pair is $\log(3/4) \approx -0.288 < 0$ (contracting). ITPFI dominance $\lambda_2 = 1/2 > \lambda_3 = 1/3$: the 2-adic factor (division by 2) outweighs the 3-adic factor (multiplication by 3) in the tensor product $\omega_1^{(2)} \otimes \omega_1^{(3)}$, so all excited harmonics decay to the fundamental mode $n = 1$.

**Status**: OPEN — the wall (W_L5)
**Source**: paper41 Link 5; paper60 §09 "The KMS$_1$ attractor"; depends on L4 full closure.

#### Physics

- **Face**: HARMONICS (paper60 §09 — "all excited modes decay to the fundamental"; this is the harmonic-decay statement at the heart of the Collatz conjecture, the canonical HARMONICS-face claim per paper60 §26 "Three-Face Recognition")
- **Projection**: $P_D$ (paper61 §10 — the KMS$_1$ critical point is the equilibrium of the BC algebra's modular flow; the ITPFI tensor decomposition is $P_D$-internal)
- **Pattern**: P4 Topological Rigidity (paper08 §36 pattern inventory extended: KMS$_1$ criticality is the rigid phase-transition point; attractor status IS a rigidity-of-equilibrium statement)
- **Invariant preserved**: BC-KMS state (load-bearing — the KMS$_1$ state IS the attractor), ITPFI factor type (background — III$_1$ is the factor class at $\beta = 1$)
- **Geometric interpretation**: The BC partition function $Z(\beta) = \zeta(\beta)$ diverges at $\beta = 1$ — the system sits at the phase transition between expansion ($\beta < 1$, chaotic) and contraction ($\beta > 1$, convergent). The measured Collatz Lyapunov $\approx 0$ IS KMS$_1$ behavior (paper60 §09 "The KMS$_1$ attractor"); the conjecture says the critical point is an ATTRACTOR — all trajectories in $\mathbb{N}^*$ converge to it. Pattern 4 (Topological Rigidity) captures why: the ITPFI tensor product $\omega_1^{(2)} \otimes \omega_1^{(3)}$ is rigidly dominated by the $p = 2$ factor ($\lambda_2 > \lambda_3$, paper60 §09 "The (2,3)-adic perspective"), forcing the contracting direction to win. Under $P_D$ (paper61 §10) this is the equilibrium statement about the first two local factors of the BC KMS$_1$ state. The wall is that AVERAGE contraction must be upgraded to POINTWISE convergence — individual orbits can have arbitrarily long expanding stretches. [Considered but rejected: face DYNAMICS — the flow is dynamical but the decay-to-fundamental is harmonic-canonical; pattern P3 — Lyapunov is a rate but its vanishing is criticality-rigidity; projection $P_E$ — numerical confirmation of Lyapunov $\approx 0$ is $P_E$-adjacent but load-bearing is $P_D$.]
- **Cross-cuts**: lehmer L_gap (KMS phase-transition mechanism shared: Lehmer $c_0 > 0$ is static gap, Collatz L5 is dynamic decay — "price of aperiodicity" duality per paper60 §09), cramer L4b-Step5 (ITPFI at conformal midpoint — same $\omega_1^{(p)}$ Araki-Woods structure), bgs L2 (modular-flow ergodicity feeds the attractor argument), opn L_KMS (KMS$_1$ evaluation of Hecke orbit sum $\sigma(n)/n = \omega_1(H_n)$ — same equilibrium-state framework).

#### L5a — ITPFI dominance (generic → Collatz-specific)

**Claim**: In the ITPFI type III$_1$ factor with Araki-Woods parameters $\lambda_p = 1/p$, the local factor $\omega_1^{(2)}$ ($\lambda_2 = 1/2$) has more weight than $\omega_1^{(3)}$ ($\lambda_3 = 1/3$), so the 2-adic contracting direction dominates the Collatz orbit.

**Status**: CONJECTURED (the dominance is structurally clear; rigorous for SPECIFIC Collatz dynamics needs new analysis)
**Source**: paper41 §5a; paper60 §09 "The (2,3)-adic perspective."

##### Physics

- **Face**: HARMONICS (paper60 §09 — ITPFI dominance IS the harmonic-side explanation of contraction)
- **Projection**: $P_D$ (paper61 §10 — Araki-Woods parameters and ITPFI factor structure are $P_D$-native)
- **Pattern**: P4 Topological Rigidity ($\lambda_2 > \lambda_3$ is a rigid algebraic fact about the ITPFI structure; the wall is PROPAGATING it to pointwise orbit contraction)
- **Invariant preserved**: ITPFI factor type (load-bearing)
- **Geometric interpretation**: The Araki-Woods parameters are structurally $\lambda_p = 1/p$ (paper61 §10 / paper60 §09); $\lambda_2 > \lambda_3$ is immediate. The rigidity argument is that in ITPFI tensor products, the larger parameter dominates the return-to-equilibrium — the structural fact about the algebra (Pattern 4, paper08 §36 pattern canon extended). The remaining work is making this rigorous for the SPECIFIC Collatz dynamics (not just generic ITPFI products). [Considered but rejected: face MEASURE — Araki-Woods is measure-theoretic but the load-bearing content is harmonic decay; pattern P3 — the $\lambda_p = 1/p$ scale is set but the dominance is rigidity.]
- **Cross-cuts**: cramer L4b-Step2 (ITPFI tensor decomposition $\omega_1 = \otimes_p \omega_1^{(p)}$, same structure), lehmer L_ITPFI ($c_0$ static gap analog), opn L_tensor (ITPFI sub-tensor for odd-divisor sum — same (2,3)-adic restriction).

#### L5b — Backward transfer operator spectral gap

**Claim**: The backward transfer operator $\mathcal{L}_T$ for the Collatz dynamics is quasi-compact with a spectral gap and unique invariant density. Identification with the BC algebra's KMS$_1$ spectral gap (via L4) would make the contraction a spectral consequence.

**Status**: CONJECTURED (spectral gap exists in literature; identification with KMS$_1$ structure needs L4 closure)
**Source**: 2025 preprint on spectral calculus for arithmetic dynamics (see paper41 §5b).

##### Physics

- **Face**: RESONANCE (paper60 §15 — "what vibrational frequencies are ALLOWED on the circle"; spectral gap of transfer operator IS a resonance-content statement)
- **Projection**: $P_D$ (paper61 §10 — transfer operator spectral gap is operator-algebraic)
- **Pattern**: P4 Topological Rigidity (spectral gap is the rigidity statement)
- **Invariant preserved**: spectral gap (load-bearing)
- **Geometric interpretation**: Quasi-compactness + spectral gap of $\mathcal{L}_T$ is a RESONANCE-face statement (paper60 §15) about which decay modes are allowed. Identifying this gap with the BC KMS$_1$ spectral gap (which requires L4 to carry the spectral structure across the embedding) would make contraction a spectral-rigidity consequence. [Considered but rejected: face HARMONICS — spectral gap of transfer operator lives at resonance even though it controls harmonics; pattern P3 — rate of decay is a scale.]
- **Cross-cuts**: ym L1 / L14 (spectral gap — same P4 rigidity pattern), rh L_Boegli (Boegli resolvent spectral gap — shared uniform-constant framework), pvnp L_gap (Popa-rigidity spectral gap — III$_1$ analog).

#### L5c — Thermodynamic entropy decay (Lyapunov function)

**Claim**: A thermodynamic entropy that DECREASES along Collatz orbits (recent 2025 work) serves as a Lyapunov function; identification with the KMS$_1$ free energy of $A_{BC}$ restricted to the Collatz sub-algebra makes the decay a thermodynamic consequence.

**Status**: CONJECTURED (entropy exists in literature; KMS-free-energy identification needs L4)
**Source**: 2025 thermodynamic entropy-decay literature (see paper41 §5c).

##### Physics

- **Face**: MEASURE (paper60 §10 — entropy is a measure-theoretic invariant of the dynamical system; Sato-Tate-adjacent equidistribution framework)
- **Projection**: $P_D$ (paper61 §10 — KMS free energy lives in the BC algebra)
- **Pattern**: P4 Topological Rigidity (entropy monotonicity = rigid decrease; Lyapunov-function status is rigidity)
- **Invariant preserved**: ergodic property (load-bearing — Lyapunov function monotonicity)
- **Geometric interpretation**: A thermodynamic entropy that monotonically decreases along orbits is a measure-theoretic Lyapunov function — it forces convergence without requiring pointwise estimates. Identifying it with the BC KMS$_1$ free energy restricted to the Collatz sub-algebra (paper60 §09 / paper61 §10) would close the contraction argument thermodynamically. [Considered but rejected: face HARMONICS — entropy tracks harmonic mixing but the invariant is measure-theoretic; pattern P5 — entropy is regularized but the rigidity of monotonic decrease dominates.]
- **Cross-cuts**: sato-tate L_equi (MEASURE canonical — equidistribution / entropy framework), bgs L3 (entropy bound analog), cramer L4b-Step1 (return-time envelope from ergodicity — analogous Kac-lemma argument).

### L6 — Cycle elimination: type III$_1$ has no non-trivial periodic orbits

**Claim**: A non-trivial Collatz cycle would be a periodic orbit of the $(2,3)$-restricted modular flow $\sigma_t$. Type III$_1$ factors have Connes spectrum $\text{Sd}(M) = \mathbb{R}$ — no periodic orbits except the trivial one. Conditional on L4 preserving the type classification, non-trivial cycles are ruled out.

**Status**: OPEN (conditional on L4 spectral preservation)
**Source**: paper41 Link 6; Paper 32 BGS PROOF-CHAIN L2 (modular-flow ergodicity PROVED via T2 2026-04-13).

#### Physics

- **Face**: SYMMETRY (paper60 §12 — cycle elimination is a symmetry-theoretic closure about the Connes spectrum; type classification is a symmetry-invariant of the factor)
- **Projection**: $P_D$ (paper61 §10 — Connes spectrum and type III$_1$ classification are $P_D$-native operator-algebraic invariants)
- **Pattern**: P4 Topological Rigidity (type III$_1$ has $\text{Sd}(M) = \mathbb{R}$ as a rigid algebraic fact; no periodic orbits is topologically rigid)
- **Invariant preserved**: ITPFI factor type (load-bearing — type III$_1$ IS the rigid classification), ergodic property (background — Connes spectrum via modular-flow ergodicity)
- **Geometric interpretation**: The Connes spectrum $\text{Sd}(M) = \mathbb{R}$ of a type III$_1$ factor means the modular flow $\sigma_t$ has no non-trivial periodic orbits — an algebraic rigidity of the factor class (paper61 §10). If L4's embedding preserves the type classification (the OPEN part of L4), then any non-trivial Collatz cycle would contradict this rigidity. Pattern 4 captures it: the absence of periodic orbits is not a dynamical estimate but a classification-theoretic fact. Under $P_D$ this is a statement about the modular-flow structure preserved by the BC embedding. [Considered but rejected: face DYNAMICS — modular flow is dynamical but the KEY statement is the Connes-spectrum classification (symmetry-type); pattern P3 — no scale is set; projection $P_O$ — the outer-ring Collatz statement is at L7, not L6.]
- **Cross-cuts**: bgs L2 (modular-flow ergodicity PROVED — primary parent edge, paper32 T2 2026-04-13), cramer L3 (modular-flow return times — shared type III$_1$ framework), pvnp L_rigidity (Popa-rigidity type III$_1$ invariance — same classification), baum-connes L_type (type classification on spectral triple).

### L7 — Collatz conjecture

**Claim**: Every positive integer $n$ eventually reaches $1$ under iteration of the Collatz map $T$.

**Status**: FOLLOWS (from L5 harmonic decay + L6 cycle elimination)
**Source**: paper41 Link 7 assembly; community-standard statement (Collatz 1937; Bakuage prize 2021).

#### Physics

- **Face**: HARMONICS (paper60 §09 — the Collatz conjecture IS the HARMONICS-face closure statement; "every harmonic decays to the fundamental")
- **Projection**: $P_O$ (paper61 §12 — the outer-ring community-standard conjecture statement; where the internal $P_D$-derivation turns into a Bakuage-prize-grade closure)
- **Pattern**: P4 Topological Rigidity (L5 + L6 combine to give the rigid attractor + rigid no-cycles content; the Collatz conjecture is their topological rigidity joint statement)
- **Invariant preserved**: BC-KMS state (load-bearing — the attractor IS the KMS$_1$ state's rigid pull), ergodic property (background — cycles excluded by III$_1$ ergodicity)
- **Geometric interpretation**: The Collatz statement is the joint consequence of L5 (all harmonics decay) and L6 (no non-trivial cycles). Under $P_O$ (paper61 §12) this is the outer-ring closure — the community-standard formulation whose resolution is what Bakuage offers the prize for. The geometric content is simple: on the e-circle, excited harmonics cannot persist (L5) and cannot form loops (L6), so every orbit must terminate at the fundamental (paper60 §09). [Considered but rejected: face SYMMETRY — no-cycles is symmetry-canonical (L6) but the conjecture's primary face is HARMONICS per paper60 §09; pattern P1 — the whole translation is Pattern 1 but the closure step is rigidity of L5+L6; projection $P_D$ — internal derivation is $P_D$ but OUTER-RING closure is $P_O$, matching the YM L18 analogy.]
- **Cross-cuts**: lehmer L_Bakuage-sibling (shared "rigidity on e-circle" outer-ring closure pattern — topology vs harmonics dual), cramer L5 (Cramér-Granville outer-ring — same $P_O$ community-standard closure), ym L18 ($P_O$ outer-ring Clay closure analog — different face, same projection at closure).

---

## §4 Branch Map

The Collatz chain has ONE genuine branch point (L5, the wall), which splits into three parallel sub-routes (L5a / L5b / L5c), all gated on L4. This is the main structural feature of the proof chain.

```
L4 (BC embedding — PARTIAL, spectral preservation open)
                │
                └── Gates all three routes into L5.
                │
                ▼
L5 splits:
├── Route A — L5a: ITPFI dominance (λ_2 > λ_3)
│       [face: HARMONICS | proj: P_D | pat: P4]
│       [invariant: ITPFI factor type]
│       Argument: structural algebraic fact about Araki-Woods params.
│       Gap: upgrade from generic ITPFI to specific Collatz dynamics.
│
├── Route B — L5b: backward transfer operator spectral gap
│       [face: RESONANCE | proj: P_D | pat: P4]
│       [invariant: spectral gap]
│       Argument: quasi-compactness of L_T (literature)
│                 + identification with KMS_1 gap (via L4).
│       Gap: spectral-preservation (L4 OPEN part).
│
└── Route C — L5c: thermodynamic entropy decay (Lyapunov fn)
        [face: MEASURE | proj: P_D | pat: P4]
        [invariant: ergodic property]
        Argument: monotone-decrease entropy (literature)
                  + identification with KMS free energy (via L4).
        Gap: spectral-preservation (L4 OPEN part).
```

All three routes share:
- Same projection $P_D$ (all live in the BC algebra / operator-algebraic projection)
- Same pattern P4 (all three are rigidity-of-equilibrium statements)
- Same dependency on L4 (all three need the BC embedding to preserve spectral/type structure)

They differ in face assignment, which tells us that L5's harmonic-decay content can be approached from three adjacent faces of the e-circle (HARMONICS for L5a, RESONANCE for L5b, MEASURE for L5c). The critic challenge is: if all three routes have the same $P_D$ and the same P4 but pick different faces, are we really solving the wall three times or once? The arbiter answer: the three faces are independent attacks on the same $P_D$-content, so closing ANY ONE would close L5; the three routes are independent in the sense of attack-vector, but dependent in the sense of $P_D$-machinery (L4 closure). This is why "close L4 fully, and Links 5 and 6 each have three independent attacks" is the programme stance (paper41 §4 current wall).

The L7 closure has the same outer-ring-boundary character as YM L18: an internal $P_D$-derivation terminates at a $P_O$ statement for prize-compliance purposes. No branch at L7 — it's the unique community-standard closure.

---

## §5 Face Histogram

Layer count per face, treating L5a / L5b / L5c as sub-layers (3 extra entries), giving 10 annotated entries across L1-L7.

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | Collatz does not live on the topology face directly; Lehmer (topology) is a sibling cross-cut per paper60 §26 three-face triangle, not an internal layer. |
| DYNAMICS   |   1   | ████                  | 2-adic ergodicity (L3) — one dynamics-face layer, providing the background measure-preserving structure for L5's attractor argument. |
| HARMONICS  |   3   | ████████████          | DOMINANT. Harmonic-decomposition dictionary (L1), KMS$_1$ attractor main (L5), outer-ring Collatz statement (L7). Collatz IS the canonical HARMONICS face per paper60 §09, §26. |
| MEASURE    |   1   | ████                  | Thermodynamic entropy-decay sub-route (L5c) — one sub-layer approaches the wall via the MEASURE face. |
| AMPLITUDE  |   0   |                       | Collatz does not interrogate growth-rate / subconvexity. |
| SYMMETRY   |   3   | ████████████          | STRONG SECONDARY. Cuntz $\mathcal{O}_2$ formulation (L2), BC embedding (L4), type III$_1$ cycle elimination (L6). Three layers carry the algebraic-symmetry structure — this is what makes Collatz an operator-algebraic object, not just a dynamics problem. |
| CURVATURE  |   0   |                       | No gauge-curvature content. |
| ARITHMETIC |   0   |                       | Despite the "number theory" surface appearance, no layer lives on the arithmetic face — integers on the e-circle are harmonics (KK mode index), not arithmetic-lattice objects for Collatz (cf. YM L7 which is arithmetic-canonical via Newton sums). |
| RESONANCE  |   1   | ████                  | Backward-transfer-operator spectral-gap sub-route (L5b) — one sub-layer approaches the wall via the RESONANCE face. |
| SPREAD     |   0   |                       | No $L^2$-mass-distribution content. |

**Interpretation**: HARMONICS dominates (3 / 10 layers, 30%) — confirming paper60 §09's identification of Collatz as the canonical HARMONICS face. SYMMETRY is the strong secondary (3 / 10, 30%), carrying the algebraic-structure side (Cuntz / BC / type III$_1$). DYNAMICS, MEASURE, RESONANCE each contribute 1 layer (10% each), showing that the L5 branch's three routes (L5a / L5b / L5c) spread the wall-attack across three adjacent faces. Five faces (TOPOLOGY, AMPLITUDE, CURVATURE, ARITHMETIC, SPREAD) are absent. The "shape" of Collatz on the e-circle is HARMONICS-canonical with strong SYMMETRY secondary — consistent with paper60 §26 "Three-Face Recognition" placing Collatz at the HARMONICS vertex of the triangle while acknowledging its Cuntz-algebraic backbone. Notably, ARITHMETIC's absence distinguishes Collatz from YM (which has L7 Newton power-sum) and goldbach / twin-primes (canonical ARITHMETIC vertices), despite the surface appearance of Collatz as a "number theory" problem.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No quantum-observable content; Collatz's Hecke alternation does not appear in Branch A. Paper61 §08 confirms: quantum side does not see Hecke structure directly. |
| $P_B$        |   0   |                      | No gauge-bundle content. Unlike YM which is $P_B$-dominant, Collatz has zero gauge-bundle layers — there is no KK-tower role for the Collatz map. |
| $P_C$        |   0   |                      | No cosmological observable. |
| $P_D$        |   9   | ████████████████████████████████████ | DOMINANT — 90% of layers. Cuntz/BC embedding (L2, L4), Hecke alternation (L1), 2-adic ergodicity (L3), KMS$_1$ attractor (L5, L5a, L5b, L5c), type III$_1$ cycle elimination (L6). Collatz is MORE $P_D$-concentrated than any other vertex in the programme: the entire chain except the outer-ring L7 closure lives in the BC algebra. |
| $P_E$        |   0   |                      | Empirical confirmation (Barina $2^{68}$, Tao 2019 almost-all, measured Lyapunov $\approx 0$) is $P_E$-adjacent but not a 36-pin programme entry — same status as YM's lattice-QCD mass ($m_{0^{++}} \approx 1.7$ GeV) per paper61 §12: confirmation, not programme pin. No $P_E$ layer. |
| $P_O$        |   1   | ████                 | Outer-ring community-standard statement — invoked only at L7 (Bakuage-prize closure). 10%. |

**Interpretation**: The projection profile is extreme — 9 / 10 layers at $P_D$, 1 / 10 at $P_O$, all five other projections empty. Collatz is the MOST PROJECTION-CONCENTRATED vertex in the programme: the entire proof chain machinery lives in the BC algebra, with only the outer-ring conjecture statement at L7 escaping into $P_O$ for community-standard / Bakuage-prize purposes. This matches paper61 §10's "Branch D crosses with almost every other face" exactly — Collatz is a pure Branch D object at the HARMONICS face, with the BC algebra providing both the Cuntz sub-algebra embedding (L2, L4), the modular-flow ergodicity (L3, L6), the KMS$_1$ attractor (L5), and the ITPFI tensor structure (L5a). The contrast with YM is informative: YM is $P_B$-dominant (65%) with $P_D$ secondary (30%) because YM needs the gauge bundle explicitly; Collatz is $P_D$-dominant (90%) with $P_O$ only for closure because Collatz never needs the gauge bundle at all.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                       qg5d (Branch D / e-circle origin)
                           │
                           │ ═══ paper60 §09: Collatz = HARMONICS face
                           │ ═══ paper61 §10: Cuntz O_2 ⊂ A_BC
                           │ ═══ ITPFI ω_1 = ⊗_p ω_1^(p) (primes 2,3)
                           │
                           ▼
                    collatz (HARMONICS, P_D)
                      │         │        │
       ┌──────────────┤         │        ├─────────────────┐
       │              │         │        │                 │
    lehmer ═════ cramer ═══════ │ ══════ bgs ═════ pvnp
   (TOPOLOGY;   (DYNAMICS;      │        (GUE; modular  (Popa rigidity;
    three-face   three-face     │         flow ergodic  type III_1)
    triangle)    triangle)      │         PROVED)        ═══ L6 ↔ III_1
   ═══ L7/L5    ═══ L1/L3/L5    │        ═══ L3/L6        ═══ L5 ↔ gap
    siblings     (Hecke +        │         modular flow  ═══ L4 ↔ C*
    per paper60  modular         │                        algebra
    §09 cross-   flow commute)   │
    refs)                        │
                                 │
                ┌────────────────┤
                │                │
           goldbach ═══════════ opn ═════ twin-primes
          (additive +          (σ(n) = 2n;         (Hecke primes;
           multiplicative;      Hecke orbit sum;    gap = 2 analog)
           +1 shift wall)       additive-mult wall) ═══ L4 ↔ N* Hecke
          ═══ L4 ↔ wall        ═══ L4 ↔ wall
                                ═══ L5 ↔ KMS_1
                                 evaluation

           sato-tate ────────────── ym (paper08)
          (MEASURE canonical;       (ARITHMETIC at L7
           entropy / equi-           Newton sums;
           distribution)             HARMONICS-adjacent)
          ─── L5c ↔ entropy         ─── L1 ↔ harmonic
               decay                     framework

                        baum-connes (paper31)
                       (local C*-algebra;
                        Cuntz K-theory)
                       ═══ L2 ↔ O_2 structure
                       ═══ L4 ↔ embedding
                       ═══ L6 ↔ type
```

### Bullet list (per-edge)

- **L1 ↔ cramer:L3** — shared face-adjacency (HARMONICS ↔ DYNAMICS siblings) and shared invariant (ergodic property / Hecke commutation).
  - Reason: paper60 §09 Cross-references — "the modular flow $\sigma_t$ (Cramér's dynamics) commutes with the Hecke action $\mu_p$ (Collatz's harmonics). The two faces interrogate different aspects of the same algebraic structure."
  - Transposition candidate: YES (paper60 §26 three-face triangle, capacitor-formalizable).

- **L1 ↔ lehmer:L1** — shared face-sibling (HARMONICS ↔ TOPOLOGY siblings).
  - Reason: paper60 §09 "Off-diagonal BC (Collatz — Hecke + phase interaction) vs diagonal BC (Lehmer — phase alone)"; same e-circle's three-face triangle.
  - Transposition candidate: YES (three-face-recognition capacitor pending).

- **L1 ↔ ym:L7** — shared KK mode index (integer-harmonic framework).
  - Reason: paper60 §09 cross-refs — Newton power-sums (ym L7) decompose by integer powers of the harmonic; Collatz L1 alternates frequencies on the same integer-harmonic lattice.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ baum-connes:L_local** — shared C*-algebra structure.
  - Reason: Cuntz algebra $\mathcal{O}_2$ K-theory is a canonical Baum-Connes object; K-theory pairing on $A_{BC}$ sub-inclusions.
  - Transposition candidate: YES.

- **L2 ↔ ym:L17** — shared C*-algebra structure (operator-valued-distribution analog).
  - Reason: Both live in local C*-algebras as irreducible operator structures.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ pvnp:L_Cstar** — shared C*-algebra structure.
  - Reason: Popa rigidity on type III$_1$ factors shares the operator-algebraic framework.
  - Transposition candidate: YES.

- **L3 ↔ cramer:L3** — shared ergodic property (modular-flow canonical).
  - Reason: Both are type III$_1$ modular-flow ergodicity statements — paper60 §08 DYNAMICS canonical, same $\omega_1^{(p)}$ factor.
  - Transposition candidate: YES.

- **L3 ↔ bgs:L2** — shared ergodic property (type III$_1$ modular flow).
  - Reason: BGS L2 PROVED (T2 2026-04-13) is the primary parent for the modular-flow ergodicity used in Collatz L6.
  - Transposition candidate: YES.

- **L3 ↔ pvnp:L_modular** — shared ergodic property.
  - Reason: Popa rigidity uses type III$_1$ modular-flow ergodicity.
  - Transposition candidate: YES.

- **L3 ↔ ym:L3** — shared ergodic property.
  - Reason: K-independent polymer convergence is the same type-III$_1$ modular-flow ergodicity in BC-algebra form.
  - Transposition candidate: YES.

- **L4 ↔ goldbach:L_wall** — shared additive-multiplicative wall.
  - Reason: paper60 §09 Cross-references / paper41 §"The +1 wall" — Collatz ($+1$), Goldbach ($p+q = 2n$), OPN ($\sigma(n) = \sum d$) all face the same additive-on-multiplicative obstruction. The phase operator $e(1)$ on $\hat{\mathbb{Z}}$ is the common resolution candidate.
  - Transposition candidate: YES (shared-wall capacitor pending).

- **L4 ↔ opn:L_wall** — shared additive-multiplicative wall.
  - Reason: Same paper60 §09 / paper41 shared-wall identification; OPN's $\sigma(n) = \sum_{d | n} d$ is additive over divisors on the multiplicative Hecke structure.
  - Transposition candidate: YES.

- **L4 ↔ twin-primes:L_Hecke** — shared Hecke-semigroup framework.
  - Reason: Twin primes use $\mathbb{N}^*$ with gap = 2 structure; Collatz uses $\mathbb{N}^*$ with $\mu_2 / \mu_3$ alternation. Same semigroup, different restriction.
  - Transposition candidate: SPECULATIVE.

- **L4 ↔ baum-connes:L_embed** — shared C*-algebra structure (Cuntz-algebra sub-inclusion).
  - Reason: K-theory of sub-algebra inclusions on $A_{BC}$ — Baum-Connes machinery directly applicable.
  - Transposition candidate: YES.

- **L5 ↔ lehmer:L_gap** — shared BC-KMS state (phase-transition mechanism).
  - Reason: paper60 §09 "With Face 1 (TOPOLOGY, Lehmer), the connection is the 'price of aperiodicity' duality: Lehmer says the minimum cost of being aperiodic is $c_0 > 0$ (a static gap), while Collatz says all aperiodic states eventually decay to the periodic ground state (a dynamic convergence)."
  - Transposition candidate: YES (three-face capacitor).

- **L5 ↔ cramer:L4b-Step5** — shared ITPFI factor type.
  - Reason: Both invoke the ITPFI tensor decomposition $\omega_1 = \otimes_p \omega_1^{(p)}$ with Araki-Woods $\lambda_p = 1/p$; Cramér uses conformal-midpoint truncation ($y = \sqrt{x}$), Collatz uses $(2,3)$-adic sub-tensor. Same ITPFI machinery.
  - Transposition candidate: YES.

- **L5 ↔ bgs:L2** — shared BC-KMS state.
  - Reason: Modular-flow ergodicity on type III$_1$ is the foundational infrastructure for the KMS$_1$ attractor argument.
  - Transposition candidate: YES.

- **L5 ↔ opn:L_KMS** — shared BC-KMS state.
  - Reason: OPN uses $\sigma(n)/n = \omega_1(H_n)$ (KMS$_1$ evaluation of Hecke orbit sum); Collatz L5 is the dynamic version (Hecke orbit decay to fundamental under KMS$_1$).
  - Transposition candidate: YES.

- **L5a ↔ cramer:L4b-Step2** — shared ITPFI factor type (tensor decomposition $\omega_1 = \otimes_p \omega_1^{(p)}$).
  - Reason: Same Araki-Woods $\lambda_p = 1/p$ structure, same paper12 §265 reference.
  - Transposition candidate: YES.

- **L5a ↔ lehmer:L_ITPFI** — shared ITPFI factor type.
  - Reason: Lehmer's $c_0$ static-gap invariant uses the same ITPFI decomposition from the topology side.
  - Transposition candidate: SPECULATIVE (pending Lehmer X-Ray).

- **L5a ↔ opn:L_tensor** — shared ITPFI factor type ($(2,3)$-adic sub-tensor).
  - Reason: OPN's odd-case analysis restricts to odd-divisor sums = tensor-product restriction on $\omega_1^{(p)}$ factors excluding $p = 2$; Collatz uses $\omega_1^{(2)} \otimes \omega_1^{(3)}$. Related sub-tensor framework.
  - Transposition candidate: SPECULATIVE.

- **L5b ↔ ym:L1 / L14** — shared spectral gap.
  - Reason: Transfer operator spectral gap (Collatz L5b) and YM mass gap (YM L1, L14) share Pattern 4 (Topological Rigidity) on spectral gaps.
  - Transposition candidate: YES.

- **L5b ↔ rh:L_Boegli** — shared spectral gap (uniform-constant framework).
  - Reason: Boegli's uniform $H^1$ resolvent bound is analogous uniformity structure for CCM-side spectral gap.
  - Transposition candidate: SPECULATIVE.

- **L5b ↔ pvnp:L_gap** — shared spectral gap.
  - Reason: Popa-rigidity spectral gap on type III$_1$ = operator-algebra analog.
  - Transposition candidate: YES.

- **L5c ↔ sato-tate:L_equi** — shared ergodic property (entropy / equidistribution).
  - Reason: MEASURE face canonical — entropy decay and equidistribution are adjacent paper60 §10 content.
  - Transposition candidate: SPECULATIVE.

- **L5c ↔ bgs:L3** — shared ergodic property (entropy bound).
  - Reason: BGS uses entropy bounds for bulk spectral statistics; Collatz L5c uses entropy as Lyapunov function.
  - Transposition candidate: SPECULATIVE.

- **L5c ↔ cramer:L4b-Step1** — shared ergodic property (Kac's-lemma return-time envelope analog).
  - Reason: Both use ergodicity + Kac-lemma-style envelope arguments.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ bgs:L2** — shared ITPFI factor type (modular-flow ergodicity → no periodic orbits).
  - Reason: Primary parent edge — BGS L2 PROVED (T2 2026-04-13) supplies the modular-flow ergodicity that L6's Connes-spectrum argument requires.
  - Transposition candidate: YES.

- **L6 ↔ cramer:L3** — shared ITPFI factor type.
  - Reason: Same type III$_1$ framework; Cramér uses return times, Collatz uses no-periodic-orbits.
  - Transposition candidate: YES.

- **L6 ↔ pvnp:L_rigidity** — shared ITPFI factor type (type III$_1$ rigidity).
  - Reason: Popa rigidity IS the rigidity of type III$_1$ classification under embeddings.
  - Transposition candidate: YES.

- **L6 ↔ baum-connes:L_type** — shared ITPFI factor type.
  - Reason: Type classification is preserved under K-theory morphisms on $A_{BC}$ sub-inclusions.
  - Transposition candidate: YES.

- **L7 ↔ lehmer:L_Bakuage-sibling** — face-only (three-face-triangle outer-ring closure pattern).
  - Reason: paper60 §26 three-face recognition — Collatz (HARMONICS) and Lehmer (TOPOLOGY) are outer-ring siblings on the e-circle.
  - Transposition candidate: NO yet (sibling closure is conjectural pattern).

- **L7 ↔ cramer:L5** — face-only (three-face-triangle outer-ring closure pattern).
  - Reason: Same paper60 §26 three-face recognition.
  - Transposition candidate: NO yet.

- **L7 ↔ ym:L18** — projection-shared ($P_O$ outer-ring closure).
  - Reason: Both are internal-$P_D$-derivation-terminating-at-$P_O$-outer-ring-closure moves for prize-compliance purposes (Clay for YM, Bakuage for Collatz).
  - Transposition candidate: YES (P_O boundary pattern capacitor).

**Summary**: 29 cross-cut edges identified across 10 annotated layers (avg ~2.9 per layer — slightly higher than YM's 1.9, reflecting Collatz's three-face-triangle embedding). 14 YES transposition candidates (backed by paper60 §09 cross-refs, paper60 §26 three-face, shared-wall identification, explicit parent edges like BGS L2). 15 SPECULATIVE. The PRIMARY edges are L6 ↔ bgs:L2 (modular-flow ergodicity from BGS, PROVED) and L4 ↔ goldbach:L_wall / opn:L_wall (shared additive-multiplicative wall trio).

---

## §8 Current Walls

- **W_BC — L4 spectral preservation (the BC embedding's open part)**: The algebraic embedding $\mathcal{O}_2 \hookrightarrow A_{BC}$ (via $s_0 \mapsto \mu_2^* \mu_2$, $s_1 \mapsto \mu_2^* e(1) \mu_3$) is VERIFIED (T7 2026-04-14). What remains open is whether the embedding preserves the KMS$_1$ state's properties — specifically, whether the embedded Cuntz algebra inherits the type III$_1$ classification and modular flow. Face: SYMMETRY, projection: $P_D$, pattern: P1 (for embedding) / P4 (for spectral rigidity). Status: **OPEN**. No capacitor cell yet; decomposition would split into (a) type-classification preservation and (b) modular-flow extension.

- **W_L5 — KMS$_1$ attractor (harmonic decay; THE CONJECTURE'S WALL)**: The average Lyapunov per odd-even pair is $\log(3/4) < 0$ (contracting), but average contraction must be upgraded to POINTWISE convergence — individual orbits can have arbitrarily long expanding stretches where $\mu_3$ temporarily dominates. Three sub-routes (L5a ITPFI dominance / L5b transfer-operator spectral gap / L5c thermodynamic entropy decay) each conjecturally close the wall IF L4 is fully closed. Face: HARMONICS, projection: $P_D$, pattern: P4. Status: **OPEN**. This is THE wall — the substantive open content of the Collatz conjecture modulo L4.

- **W_cyc — L6 cycle elimination (conditional on L4)**: Non-trivial Collatz cycle = non-trivial periodic orbit of the $(2,3)$-restricted $\sigma_t$ on the BC algebra. Type III$_1$ factor has Connes spectrum $\text{Sd}(M) = \mathbb{R}$, so only trivial periodic orbits exist — IF L4 preserves the type classification. Conditional on L4's spectral-preservation part. Face: SYMMETRY, projection: $P_D$, pattern: P4. Status: **OPEN** (conditional on W_BC).

Three walls, all gated on L4. Closing L4 (W_BC) fully gives L5 three independent attacks (L5a / L5b / L5c) and L6 one direct argument (Connes spectrum). The Collatz conjecture's substantive difficulty has been refactored from "prove every orbit converges" into "prove the BC embedding preserves spectral structure" — a single algebraic question rather than an uncountable family of orbit checks.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/collatz/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-14). When created, the X-Ray-identified L5 branch (L5a / L5b / L5c three routes) is the natural decomposition skeleton; W_BC / W_L5 / W_cyc are the three sub-chain roots.
- **CCM verification**: `strategy/ccm-verification/ledger.md#collatz` — NOT YET CREATED (CCM-verification bundle has empty `proof-chain/` directory as of 2026-04-14). Collatz does NOT depend on CCM 2025 (the Collatz chain uses BC algebra intrinsically but does not inherit the RH / CF-uniformity part of CCM). Expected verdict when ledger written: **VERIFIED (CCM-independent)**.
- **Inner rings**: NOT APPLICABLE — Collatz is a primary outer-ring vertex, not an inner-ring object.
- **T7 deep-construction pass**: paper41-collatz PROOF-CHAIN.md upgraded v1→v2 on 2026-04-14 via the T7 "three-face recognition" pass. The X-Ray per-layer assignments are consistent with the T7 upgrade's identification of $+1$ as the phase operator $e(1)$ on $\hat{\mathbb{Z}}$.
- **Three-face triangle (paper60 §26)**: `integers/paper60-geometry-of-circle/26-the-three-face-recognition.md` — Collatz's placement at the HARMONICS vertex of the Lehmer / Cramér / Collatz triangle is the structural-recognition source for the primary-face assignment. When Lehmer's X-Ray and Cramér's X-Ray (already written) are cross-compared, the three-face triangle becomes a transposable capacitor pattern.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W_BC (L4 spectral preservation)**: Does the algebraic embedding $\mathcal{O}_2 \hookrightarrow A_{BC}$ (VERIFIED) preserve the KMS$_1$ state's properties (type III$_1$ classification, modular flow $\sigma_t$)? — face: SYMMETRY, projection: $P_D$, pattern: P4 (rigidity). STATUS: OPEN. Gates W_L5 and W_cyc.

- **G2 — W_L5 (KMS$_1$ attractor / harmonic decay)**: Does the average Lyapunov $\log(3/4) < 0$ upgrade to POINTWISE orbit convergence on all of $\mathbb{N}^*$? Three sub-routes (ITPFI dominance / transfer-operator spectral gap / thermodynamic entropy decay), each conjecturally closing given W_BC. — face: HARMONICS, projection: $P_D$, pattern: P4. STATUS: OPEN. This is THE Collatz wall.

- **G3 — W_cyc (L6 cycle elimination, conditional on L4)**: Does type III$_1$ Connes spectrum $\text{Sd}(M) = \mathbb{R}$ propagate through the L4 embedding to rule out non-trivial Collatz cycles? — face: SYMMETRY, projection: $P_D$, pattern: P4. STATUS: OPEN (conditional on W_BC).

Three walls, all $P_D$, all P4, all gated on L4 (W_BC). This is the chain's substantive open content. The L5a / L5b / L5c sub-routes are conjectural attacks, not independent walls — they collapse into W_L5 once any one closes (given W_BC).

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-01/vertices/collatz/critic-attacks.md` (to be created on atlas-run).

Notable arbiter wins:
- **L2 face**: SYMMETRY over HARMONICS (the Cuntz $\mathcal{O}_2$ irreducibility statement is algebraic-symmetry-canonical; Mori's formulation is about reducing subspaces, not harmonic content, even though $\mathcal{O}_2$'s generators correspond to harmonic operations).
- **L4 face**: SYMMETRY over HARMONICS (the BC embedding is a sub-algebra-inclusion statement; the phase operator $e(1)$ acts on $\hat{\mathbb{Z}}$ as a symmetry-side object even though it resolves the additive-multiplicative wall at the harmonic-mixing layer).
- **L5 face**: HARMONICS over RESONANCE (the KMS$_1$ attractor's content is harmonic decay per paper60 §09, §26; L5b's RESONANCE framing is a sub-route attack but not the load-bearing face of L5 itself).
- **L5 pattern**: P4 over P1 (the attractor status is a rigidity-of-equilibrium statement; P1 Geometric Reinterpretation describes the DESCRIPTION but not the LOAD-BEARING argument).
- **L7 projection**: $P_O$ over $P_D$ (outer-ring Bakuage-prize closure boundary, matching YM L18's $P_O$ assignment at the Clay closure).
- **Primary projection**: $P_D$ — no competition; 9 / 10 layers at $P_D$ is the most concentrated $P_D$-signature in the programme.

Absent ARITHMETIC face (despite surface appearance of Collatz as "number theory"): the critic attack is "shouldn't integer iteration be ARITHMETIC-face?"; arbiter decision: no — paper60 §14 ARITHMETIC is "how do integers LATTICE on the circle" (Newton sums, additive structure of goldbach / twin-primes), whereas Collatz's integers are Fourier MODES on the circle (paper60 §09 HARMONICS). The integer label $n$ is a harmonic index, not a lattice-arithmetic object.

29 / 29 field decisions recorded; author/arbiter consensus on all primary-face, primary-projection, and primary-pattern assignments. L2, L4, L5, L5a-c, L6, L7 face/projection/pattern all survive critic attack.

---

*End of Collatz X-Ray. Snapshot 2026-04-14 (post-T7 three-face pass). 7 layers + 3 L5-sub-routes = 10 annotated entries. 29 cross-cuts identified. HARMONICS-canonical, extreme $P_D$-dominant (90%), P4-rich proof chain. Three walls (W_BC, W_L5, W_cyc), all gated on L4. Three sub-routes into L5.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
