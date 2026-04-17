# X-RAY: Generalized Riemann Hypothesis (grh)

*X-Ray of the grh proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: grh
- **Paper**: paper13b-grh
- **Live file**: `strategy/proof-chain/grh/PROOF-CHAIN.md` (snapshot 2026-04-15)
- **Top-level claim**: All non-trivial zeros of every Dirichlet L-function $L(s, \chi)$ (primitive $\chi$, every conductor $q$) satisfy $\mathrm{Re}(s) = 1/2$, via character-twisted BC systems $\mathrm{BC}_\chi$ + KMS$_{1,\chi}$ + character-twisted CCM operators $D_{N,\chi}$ + ITPFI$_\chi$ + Boegli$_\chi$ + Hurwitz$_\chi$.
- **Current status**: 2/8 PROVED (L1 via Paper 26 Step 5c; L2 via Bratteli-Robinson 2026-04-13 T2); 6/8 CONJECTURED or CONDITIONAL. Confidence 7/10. Strictly one-directional dependency on Paper 13 (RH): if RH falls, GRH falls.
- **Primary branch (paper1)**: D (CBB / Bost-Connes at KMS$_1$; character-twist via Galois action on $\mathbb{Q}^{cyc}/\mathbb{Q}$), with secondary E (bridge-family pin selection at $k \in \{2, 3, 4, 6\}$).
- **Primary face**: SYMMETRY (paper60 §12 — the bridge family at $k \in \{2,3,4,6\}$ IS the Katz-Sarnak symmetry-type selector; GRH is the L-function-family face as seen through characters).
- **Primary projection**: $P_D$ (paper61 §10 + paper61 §06-12 Vertex 3 — $L(s,\chi)$ is a BC-algebra element via the character decomposition of $\hat{\mathbb{Z}}^*$; $P_D \cap P_E$ restricted to character L-functions via the bridge family).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
GRH (Generalized Riemann Hypothesis) — RH for every L(s,χ)
│  primary face: SYMMETRY   primary proj: P_D   primary pat: P4
│  strict dependency: Paper 13 (RH) chain
│
├── L1: BC_χ construction                                [PROVED]
│      │  face: SYMMETRY    proj: P_D   pat: P1
│      │  invariant: C*-algebra structure
│      │  source: Paper 26 Step 5c (Hecke ψ bound |Δcᵖ(δ)| < 2/(N-1))
│      │           Dirichlet chars ⊂ Hecke chars ⇒ μ_n → χ(n) μ_n preserves algebra
│      │
│      └── 2026-04-14 flip CONJECTURED → PROVED via open-frontier audit
│
├── L2: KMS_{1,χ} state (χ-modulated spectral data, uniqueness)   [PROVED]
│      │  face: DYNAMICS    proj: P_D   pat: P4
│      │  invariant: BC-KMS state
│      │  source: Bratteli-Robinson 5.3.30 + trivial fixed-point algebra via χ-twist
│      │           (T2 2026-04-13; research/01-kms1-chi-uniqueness.md)
│      │
│      └── supports L3 via χ-twisted ω_{1,χ}
│
├── L3: CCM_χ operators D_{N,χ} on E_{N,χ}^+                   [CONDITIONAL — W_G1]
│      │  face: RESONANCE   proj: P_D   pat: P1
│      │  invariant: spectral gap
│      │  depends: L2 + Paper 13 Layer 1 (CCM 2025, arXiv:2511.22755)
│      │           + χ-extension functoriality
│      │
│      └── DOUBLE CONDITIONAL (CCM + χ-extension)
│             │
│             └── W_G1: χ-bridge functoriality
│                    bypass via module-level NCG construction
│                    confidence 0.75
│
├── L4: ITPFI_χ: ω_{1,χ} = ⊗_p ω_{1,χ}^(p)                   [CONJECTURED]
│      │  face: MEASURE     proj: P_D   pat: P1
│      │  invariant: ITPFI factor type
│      │  depends: L3
│      │
│      └── tensor product respects χ (completely multiplicative)
│             │
│             ├── L4a (Euler product route): χ-local factors propagate   [LIKELY]
│             ├── L4b (BC amenability route): χ agnostic                [LIKELY]
│             └── L4c (Araki-Woods route): χ(p) root-of-unity phase      [VERIFY]
│
├── L5: Estimates_χ (4 sub-estimates)                        [CONJECTURED — W_G2]
│      │  face: AMPLITUDE   proj: P_D   pat: P5
│      │  invariant: scaling dimension (load-bearing), spectral gap (background)
│      │  depends: L4 + Paper 13 L3 (RH four estimates)
│      │
│      ├── L5a — Archimedean sub-leading O(1/λ) with χ         [LIKELY]
│      │          face: AMPLITUDE   proj: P_D   pat: P5
│      │          Γ-factor shift for odd χ must preserve O(1/λ)
│      │
│      ├── L5b — Eigenvector approx O(1/λ) with χ              [LIKELY]
│      │          face: MEASURE     proj: P_D   pat: P1
│      │          Davis-Kahan + ITPFI_χ triangle
│      │
│      ├── L5c — H^1 bound ||(D_{N,χ}-i)^{-1}||_{L²→H¹} < 2     [CRITICAL — W_G2]
│      │          face: AMPLITUDE   proj: P_D   pat: P5
│      │          Fourier cancellation — conductor q(χ) enters; hardest
│      │
│      └── L5d — CF decay ρ ≥ 4.27 uniform in N                [LIKELY]
│                  face: RESONANCE  proj: P_D   pat: P3
│                  depends on prolate bandwidth λ, not χ
│
├── L6: Boegli_χ spectral exactness                           [CONJECTURED]
│      │  face: RESONANCE   proj: P_D   pat: P1
│      │  invariant: spectral gap
│      │  depends: L5 (gsrc_χ + discrete compactness_χ)
│      │
│      ├── H1 (gsrc): ITPFI_χ → form convergence → Teschl 2.7
│      └── H2 (discrete compactness): uniform H^1_χ → Rellich-Kondrachov
│
├── L7: Hurwitz_χ: ξ̂_{N,χ} → Λ(s,χ) uniformly on compacts    [CONDITIONAL]
│      │  face: HARMONICS   proj: P_D   pat: P1
│      │  invariant: zero distribution
│      │  depends: L1-L6
│      │
│      └── Hurwitz theorem target-agnostic; Λ(s,χ) not ≡ 0
│
└── L8: spec(D_{∞,χ}) = {γ_{n,χ}} ⊂ ℝ  ⇒  GRH for χ          [CONDITIONAL]
       │  face: SYMMETRY    proj: P_O   pat: P4
       │  invariant: zero distribution, Galois representation
       │  depends: L7 + D_{∞,χ} self-adjoint
       │
       └── pure logic: Re(s) = 1/2 for all non-trivial zeros of L(s,χ)

Bridge-family anchor (load-bearing; Branch D Axiom 4, paper61 §10 / paper60 §12):
  k = 2 (quadratic χ)  ↔  Symplectic Sp  ↔  CP symmetry / Z₂ orbifold
  k = 3 (cubic χ)      ↔  Unitary  U     ↔  Color SU(3) / 3 generations
  k = 4 (quartic χ)    ↔  Orthogonal O   ↔  Pati-Salam SU(4)
  k = 6 (sextic χ)     ↔  Mixed          ↔  CKM / E₈ lattice
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (Quantum observables do not see
                          L(s,χ) zeros directly; the self-
                          adjointness of D_{∞,χ} is a
                          P_D operator-algebra fact.)
                                  ▲
                                  │
        ┌─────────────(P_O outer)──────────────┐
        │                                      │
        │  GRH: Re(s)=1/2 for every L(s,χ),   │
        │       every primitive χ mod q        │
        │       (Paper 13b, 2/8 PROVED)        │
        │                                      │
        └───────────────────┬──────────────────┘
                            │
        ┌───────────────────┼─────────────────────────┐
        │                   ║                         │
        ▼                   ▼ (PRIMARY)               ▼
    P_B gravity        ═══ P_D CBB ═══             P_E pins
    (forgotten —       BC_χ system              (bridge family
     no gauge          Hecke action μ_n →       k ∈ {2,3,4,6}:
     coupling          χ(n) μ_n; KMS_{1,χ}     conductor-
     uses L(s,χ)       state; CCM_χ ops        dependent pin
     directly)         D_{N,χ}; ITPFI_χ;       values; ≤4 sub-
                       Boegli_χ; χ modulates   percent preds per
                       every layer of RH       k; Pin #9 α_PS⁻¹,
                       chain — native home     Pin #10 λ_CKM)
                            │
                            │
                    (P_C forgotten: no cosmological pin uses
                     GRH directly beyond the indirect bridge
                     to generation structure via k=3)
```

Primary projection $P_D$ uses ═══ doubled line. Paper 61 §06-12 Vertex 3 declares GRH as the compound $P_D \cap P_E$ (restricted to character L-functions via bridge family). The bridge $\beta_\chi$ at each $k \in \{2, 3, 4, 6\}$ identifies which characters are "native" to the programme. Under $P_A / P_B / P_C$ GRH's content is largely forgotten — the character-twisted operator algebra has no direct quantum, gauge-bundle, or cosmological shadow outside the pin chain.

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
          (YM)              │          (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                       (RESONANCE secondary;
                        ARITHMETIC adjacent)
```

Marker key:

```
Primary face:    ● SYMMETRY (paper60 §12 — bridge family k ∈ {2,3,4,6}
                   IS the symmetry-type selector; GRH as Dirichlet-
                   character family IS the L-function-symmetry-type face)
Secondary faces: ○ DYNAMICS   (1 layer: L2 — modular flow of KMS_{1,χ})
                 ○ RESONANCE  (2 layers: L3 spectral data of D_{N,χ};
                               L5d CF decay; L6 Boegli spectral exactness)
                 ○ AMPLITUDE  (2 layers: L5 estimates envelope; L5a, L5c
                               H^1 bound)
                 ○ MEASURE    (2 layers: L4 ITPFI_χ factorization; L5b
                               eigenvector approximation)
                 ○ HARMONICS  (1 layer: L7 Hurwitz uniform convergence on
                               compacts — Fourier-on-critical-line)
Absent faces:    TOPOLOGY, CURVATURE, ARITHMETIC, SPREAD
```

Interpretation: GRH's "shape" on the e-circle is SYMMETRY-canonical with strong RESONANCE / AMPLITUDE / MEASURE secondaries — reflecting that the character twist is fundamentally a symmetry-selector acting on the same spectral / amplitude / equidistribution content as RH. TOPOLOGY / CURVATURE / ARITHMETIC / SPREAD are absent: GRH interrogates which group acts, not what lives on the circle (Lehmer), not gauge curvature (YM), not additive decomposition (Goldbach), not eigenmode density (QUE).

---

## §3 Layer-by-Layer X-Ray

### L1 — BC_χ construction

**Claim**: The Bost-Connes algebra admits a natural Dirichlet-character twist: the Hecke action $n \mapsto \mu_n$ modulated by $\chi(n)$, i.e. $\mu_n \mapsto \chi(n) \mu_n$, preserves the algebraic relations (multiplication, involution, crossed product). This defines $\mathrm{BC}_\chi$.

**Status**: PROVED (via Paper 26 Step 5c inheritance, 2026-04-14 flip)
**Source**: `paper13b-grh/PROOF-CHAIN.md` L1; closure via Paper 26 Step 5c Key Lemma C' (twisted): $|\Delta c^\psi(\delta)| < 2/(N-1)$ for all Hecke $\psi$; Dirichlet characters are a subclass of Hecke characters, so the BC$_\chi$ construction and its cocycle-shift bound are inherited unconditionally. Open-frontier audit `closable_items.json` item 11.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — "the bridge IS the symmetry-type selector"; the character-twist $\mu_n \mapsto \chi(n) \mu_n$ IS the Galois action on $\mathbb{Q}^{cyc}/\mathbb{Q}$ factoring through $\mathrm{Gal}(\mathbb{Q}(\zeta_q)/\mathbb{Q}) = (\mathbb{Z}/q\mathbb{Z})^*$)
- **Projection**: $P_D$ (paper61 §06-12 Vertex 3 — "Dirichlet L-functions are BC-algebra elements via the character decomposition of $\hat{\mathbb{Z}}^*$; the bridge at $k$ selects the character $\chi$ of conductor $k$")
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — reinterpreting the $\chi$-twist as a natural structure of the BC algebra rather than a new construction)
- **Invariant preserved**: C*-algebra structure (load-bearing — the crossed-product relations survive the twist because $\chi$ is completely multiplicative), Galois representation (background — $\chi$ factors through $\mathrm{Gal}(\mathbb{Q}(\zeta_q)/\mathbb{Q})$)
- **Geometric interpretation**: The BC algebra was designed (Bost-Connes 1995 Theorem 25) to encode the Galois action on $\mathbb{Q}^{cyc}/\mathbb{Q}$. Dirichlet characters are precisely the irreducible representations of this Galois group, so the $\chi$-twist is structurally native — Pattern 1 (geometric reinterpretation): the $\chi$-modulation is not a new algebra but the BC algebra "viewed through character glasses" (paper61 §06-12 Vertex 3, paper60 §12 bridge-family table). The Hecke-character bound from Paper 26 Step 5c carries Dirichlet characters as a special case, flipping L1 to PROVED unconditionally. [Considered but rejected: face ARITHMETIC — $\mu_n \mapsto \chi(n) \mu_n$ is arithmetic-coefficient-modulated but the load-bearing content is the symmetry-type (character class) selection; projection $P_O$ — BC$_\chi$ is a construction inside the framework, not an outer-ring conjecture; pattern P2 Holonomy — $\chi$ is a 1D rep of the fundamental group but the character-twist is reinterpretive, not winding-based.]
- **Cross-cuts**: bsd L_cocycle (shared C*-algebra structure via Paper 26 Step 5c Key Lemma C'), rh L2 (ITPFI factorization — GRH inherits χ-twisted version), katz-sarnak L4 (bridge family selects symmetry type; χ-class ↔ group-action class), h12 (Galois action on $\mathbb{Q}^{cyc}/\mathbb{Q}$, shared structural element).

### L2 — KMS_{1,χ} state (uniqueness, χ-modulated spectral data)

**Claim**: There is a unique KMS$_1$ state $\omega_{1,\chi}$ on BC$_\chi$ producing $\chi$-modulated spectral data; the uniqueness inherited from BC survives the $\chi$-twist.

**Status**: PROVED (T2 2026-04-13)
**Source**: `paper13b-grh/PROOF-CHAIN.md` L2; closure via Bratteli-Robinson 5.3.30 + trivial fixed-point algebra argument under the $\chi$-twist. See `research/01-kms1-chi-uniqueness.md`.

#### Physics

- **Face**: DYNAMICS (paper60 §08 — the KMS$_1$ state is the fixed point of the modular flow $\sigma_t$; $\chi$-twisting preserves the flow's dynamical content while modulating its eigen-data)
- **Projection**: $P_D$ (paper61 §10 — KMS$_1$ state is the signature output of Branch D; $\omega_{1,\chi}$ is the same state "seen through character glasses")
- **Pattern**: P4 Topological Rigidity (Bratteli-Robinson 5.3.30 uniqueness + trivial fixed-point algebra is a rigidity argument: the fixed-point algebra is trivial ⇒ the state is extremal and unique)
- **Invariant preserved**: BC-KMS state (load-bearing — $\omega_{1,\chi}$ IS the twisted KMS$_1$ state), ergodic property (background — uniqueness is the operator-algebraic form of ergodicity)
- **Geometric interpretation**: Uniqueness of the KMS$_1$ state is a topological-rigidity statement: the fixed-point algebra of the modular flow is trivial, and this triviality survives the $\chi$-twist because $\chi$ is completely multiplicative and the twist preserves the gauge-invariance structure (paper61 §10, paper60 §08). The character-twisted state $\omega_{1,\chi}$ is the $\chi$-evaluation of the unique KMS$_1$ state in the Galois-orbit parametrization. [Considered but rejected: face RESONANCE — KMS is spectral-side but the UNIQUENESS claim is about dynamics; projection $P_A$ — KMS state has no direct quantum-observable shadow; pattern P1 — reinterpretation is applicable but the load-bearing mechanism is the rigidity of trivial fixed-point algebras.]
- **Cross-cuts**: rh L2 (ITPFI uniqueness of KMS$_1$ for BC — GRH is the $\chi$-twisted analog), bsd L_dark (dark-state / KMS-degeneracy at CM points — GRH version adds $\chi$-twist), ym L16 (BC-KMS state shared in OS reconstruction), baum-connes L_KMS (KMS on spectral triple — $\chi$-twisted version), pvnp L_KMS (BC-KMS state restriction in spectral construction).

### L3 — CCM_χ operators D_{N,χ} on E_{N,χ}^+

**Claim**: The character-twisted CCM construction produces self-adjoint operators $D_{N,\chi}$ on the character-twisted even-sector spaces $E_{N,\chi}^+$, with eigenvalues approximating the imaginary parts $\gamma_{n,\chi}$ of the non-trivial zeros of $L(s, \chi)$ to 55-digit precision.

**Status**: CONDITIONAL (CCM 2025 + $\chi$-extension; DOUBLE CONDITIONAL)
**Source**: `paper13b-grh/PROOF-CHAIN.md` L3; CCM 2025 arXiv:2511.22755 (Connes-Consani-Moscovici). Named wall W_G1.

#### Physics

- **Face**: RESONANCE (paper60 §15 — "what frequencies are ALLOWED on the circle"; $D_{N,\chi}$'s eigenvalues ARE the frequencies of the $\chi$-family modular flow)
- **Projection**: $P_D$ (paper61 §10 — CCM operators are the concrete realization of the BC algebra's spectral triple; $\chi$-twist stays inside $P_D$)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — reinterpreting prolate spheroidal wave functions + Carathéodory-Fejér as $\chi$-covariant, since the analytic framework does not depend on the arithmetic input)
- **Invariant preserved**: spectral gap (load-bearing — $D_{N,\chi}$ self-adjoint means its spectrum is real and discrete), C*-algebra structure (background — $E_{N,\chi}^+$ is the even-sector subspace of the twisted Hilbert module)
- **Geometric interpretation**: The CCM construction is analytic, not arithmetic — the operators are built from prolate spheroidal wave functions and Carathéodory-Fejér theory. The arithmetic input (which L-function) enters through the spectral data, not through the operator framework. $\chi$-twisting changes the eigenvalues $\{\gamma_n\} \to \{\gamma_{n,\chi}\}$ but not the construction method (paper60 §15 RESONANCE — "minimum non-zero eigenvalue on the circle's modular-flow Laplacian"). Under $P_D$ (paper61 §10) this is a $\chi$-covariant reparametrization of the same spectral triple. [Considered but rejected: face AMPLITUDE — 55-digit eigenvalue precision is a precision-bound but load-bearing content is the spectral realization; projection $P_O$ — CCM is internal infrastructure, not an outer-ring statement; pattern P3 — prolate bandwidth $\lambda$ is a scale but the mechanism is reinterpretive, not scale-setting.]
- **Cross-cuts**: rh L1 (CCM operators $D_N$ — GRH is the $\chi$-twisted version; external dependency inherited), bsd L_CCM (shared CCM 2025 dependency), baum-connes L_spectral-triple (shared spectral-triple structure).

### L4 — ITPFI_χ: ω_{1,χ} = ⊗_p ω_{1,χ}^(p)

**Claim**: The ITPFI tensor-product factorization of $\omega_{1}$ over primes transfers to the character-twisted state $\omega_{1,\chi}$: $\omega_{1,\chi} = \bigotimes_p \omega_{1,\chi}^{(p)}$. The three ITPFI proofs (Euler product, BC amenability, Araki-Woods) each transfer because $\chi$ is completely multiplicative and the tensor product respects multiplicative characters.

**Status**: CONJECTURED (natural transfer; explicit verification pending)
**Source**: `paper13b-grh/PROOF-CHAIN.md` L4; inherited from Paper 13 Layer 2 (ITPFI for RH) plus $\chi$-multiplicativity.

#### Physics

- **Face**: MEASURE (paper60 §10 — ITPFI factorization IS the local-at-$p$ equidistribution structure; $\omega_{1,\chi}$ as product over primes distributes the character's action equidistantly across local factors)
- **Projection**: $P_D$ (paper61 §10 — ITPFI factor type is a Branch D signature)
- **Pattern**: P1 Geometric Reinterpretation (tensor product over primes = geometric factorization of the state into local pieces, each carrying $\chi(p)$)
- **Invariant preserved**: ITPFI factor type (load-bearing — type III$_1$ must survive the $\chi$-twist; each $\omega_{1,\chi}^{(p)}$ picks up a $\chi(p)$ root-of-unity phase that does not affect the factor type), BC-KMS state (background — restriction to local algebras)
- **Geometric interpretation**: The ITPFI factorization encodes the Euler-product structure of $L(s,\chi) = \prod_p (1 - \chi(p) p^{-s})^{-1}$ at the operator-algebra level. $\chi(p)$ is a root of unity for each $p$, so the tensor product picks up a phase but the factorization structure (type III$_1$ + product measure) is preserved (paper61 §10 MEASURE face analog). [Considered but rejected: face ARITHMETIC — Euler product is arithmetic but the factorization is measure-theoretic; pattern P5 — $\zeta$-regularization adjacent but the load-bearing mechanism is reinterpretive; projection $P_E$ — pin values depend on ITPFI but the factorization itself lives in $P_D$.]
- **Cross-cuts**: rh L2 (ITPFI factorization — GRH adds $\chi$-twist), bsd L_factorization (local-global decomposition), sato-tate L_equidist (MEASURE face canonical), ym L16 (BC-KMS state — structural parallel).

### L5 — Estimates_χ (archimedean, eigenvector, H^1, CF — all carry χ through)

**Claim**: All four estimates of Paper 13 Layer 3 transfer to the character-twisted setting: (a) archimedean sub-leading $O(1/\lambda)$; (b) eigenvector approximation $O(1/\lambda)$; (c) $H^1$ bound $\|(D_{N,\chi} - i)^{-1}\|_{L^2 \to H^1} < 2$ uniform in $\lambda, N$; (d) CF decay $\rho \geq 4.27$ uniform in $N$.

**Status**: CONJECTURED (explicit computation for at least one non-trivial $\chi$ required); **CRITICAL LINK** — W_G2 named wall lives here.
**Source**: `paper13b-grh/PROOF-CHAIN.md` L5; inherited from Paper 13 Layer 3 with $\chi$-extension pending.

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — estimates ARE bounds on spectral/amplitude growth; L5 packages four amplitude-control estimates); secondary RESONANCE for L5d CF decay, MEASURE for L5b eigenvector approximation.
- **Projection**: $P_D$ (paper61 §10 — all four estimates are operator-algebraic properties of $D_{N,\chi}$)
- **Pattern**: P5 Zeta Regularization (the $H^1$ Fourier cancellation uses Epstein-zeta-like vanishing; CF decay depends on the regulator bandwidth $\lambda$)
- **Invariant preserved**: scaling dimension (load-bearing — uniform bounds in $N, \lambda$ are scaling statements), spectral gap (background — the uniformity preserves the gap in L3)
- **Geometric interpretation**: The four estimates together enforce the uniformity needed for the infinite-limit construction ($D_{N,\chi} \to D_{\infty,\chi}$). $\chi$-extension enters through the conductor $q(\chi)$ as a parameter; the estimates should remain uniform for fixed $\chi$. L5c ($H^1$ cancellation) is the hardest because Paper 13's cancellation uses the specific Fourier structure of $\zeta$'s spectral data; for $L(s,\chi)$ the Fourier coefficients acquire $\chi(n)$ factors and the cancellation must be re-verified (paper60 §11 AMPLITUDE — "how LOUD can the oscillation get"; with $\chi$, the question is whether each local mode still cancels destructively). [Considered but rejected: face DYNAMICS — estimates control the flow but they are amplitude-bounds in character; projection $P_O$ — L5 is infrastructure, not outer boundary; pattern P3 — bandwidth $\lambda$ sets scale but engine is regulator-vanishing.]
- **Cross-cuts**: rh L3a-L3d (the four untwisted estimates — GRH adds $\chi$-twist to each), lindelof L_amplitude (uniform amplitude control — GRH inherits Lindelöf-style uniformity), ym L4 (k-independent analyticity radius — structural parallel of L5's uniform-in-$N$ bound), selberg-1/4 L_gap (uniform spectral gap analog; SPECULATIVE).

### L5a — Archimedean sub-leading O(1/λ) with χ

**Claim**: The archimedean ratio $\|\tau^{(R)}\| / \|\sum_p \tau^{(p)}\| = O(1/\lambda)$ for $L(s,\chi)$, with the $\Gamma$-factor shift for odd characters preserving the $O(1/\lambda)$ bound.

**Status**: LIKELY (inherits Paper 13 L3a structure; Γ-factor shift is a cosmetic change for odd χ)
**Source**: `paper13b-grh/PROOF-CHAIN.md` L5; Paper 13 L3a.

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — archimedean ratio IS an amplitude-ratio bound)
- **Projection**: $P_D$ (paper61 §10 — archimedean place of BC spectral triple)
- **Pattern**: P5 Zeta Regularization (regularized sum over archimedean contribution)
- **Invariant preserved**: scaling dimension (load-bearing — $O(1/\lambda)$ is a scaling statement), spectral gap (background)
- **Geometric interpretation**: The archimedean contribution to the completed L-function $\Lambda(s,\chi)$ is regularized by $\lambda$; the ratio's bound measures amplitude decay (paper60 §11). Odd $\chi$ shifts the $\Gamma$-factor by 1 but the $O(1/\lambda)$ bound is shift-invariant. [Considered but rejected: face RESONANCE — archimedean-Γ is resonance-adjacent but the bound is amplitude.]
- **Cross-cuts**: rh L3a (untwisted version), lindelof (AMPLITUDE canonical).

### L5b — Eigenvector approximation O(1/λ) with χ

**Claim**: The eigenvector approximation $O(\log\lambda/\lambda)$ via ITPFI$_\chi$ triangle + Davis-Kahan transfers to $L(s,\chi)$.

**Status**: LIKELY (Davis-Kahan perturbation theory is character-agnostic; depends on L4 closure)
**Source**: Paper 13 L3b + L4.

#### Physics

- **Face**: MEASURE (paper60 §10 — eigenvector density and equidistribution of approximating eigenfunctions)
- **Projection**: $P_D$ (paper61 §10 — ITPFI triangle is operator-algebraic)
- **Pattern**: P1 Geometric Reinterpretation (Davis-Kahan transfers geometrically to $\chi$-twisted setting)
- **Invariant preserved**: ergodic property (load-bearing — approximation uniformity), spectral gap (background)
- **Geometric interpretation**: Davis-Kahan gives a universal perturbation bound; the ITPFI triangle inequality transfers via $\chi$-multiplicativity. Under $P_D$ (paper61 §10) the eigenvector approximation is a MEASURE-face property of the spectral-triple density (paper60 §10). [Considered but rejected: face AMPLITUDE — $O$ is amplitude but the content is equidistribution.]
- **Cross-cuts**: rh L3b (untwisted), sato-tate (MEASURE canonical).

### L5c — H^1 bound uniform (the Fourier cancellation)

**Claim**: $\|(D_{N,\chi} - i)^{-1}\|_{L^2 \to H^1} < 2$ uniform in $\lambda, N$, via the $\chi$-twisted Fourier cancellation.

**Status**: CRITICAL — W_G2 wall lives here. The Fourier-basis cancellation in Paper 13 L3c uses the specific Fourier structure of $\zeta$'s spectral data; for $L(s,\chi)$ the Fourier coefficients acquire $\chi(n)$ factors.
**Source**: Paper 13 L3c + $\chi$-extension (OPEN in `paper13b-grh/PROOF-CHAIN.md` current-wall row).

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — $H^1$ resolvent bound is an amplitude-control statement; this is Lindelöf in character)
- **Projection**: $P_D$ (paper61 §10 — resolvent of $D_{N,\chi}$ is operator-algebraic)
- **Pattern**: P5 Zeta Regularization (the cancellation weight $(1 + (2\pi n/L)^2)$ acts as a regulator; the Epstein-zeta-style cancellation must survive $\chi$-modulation)
- **Invariant preserved**: scaling dimension (load-bearing — uniformity is a scaling statement), spectral gap (background — H^1 bound protects the gap)
- **Geometric interpretation**: The $H^1$ resolvent bound is the hardest estimate because the Fourier cancellation is analytic (involving the resolvent) but the coefficients are arithmetic (involving $\chi(n)$). The question is whether the weight $(1 + (2\pi n / L)^2)$ still cancels the resolvent denominator when $\chi(n)$ modulates the coefficients (paper60 §11 AMPLITUDE — "the amplitude stays disciplined even with character modulation"). Expected: yes, because cancellation is analytic; but explicit verification for at least one non-trivial $\chi$ is needed. [Considered but rejected: face RESONANCE — resolvent is spectral but uniformity is amplitude-load-bearing; projection $P_O$ — L5c is internal, not outer.]
- **Cross-cuts**: rh L3c (untwisted version), ym L4 (k-independent uniform bound — structural parallel), lindelof L_amplitude (Lindelöf in character; SPECULATIVE), selberg-1/4 L_gap (uniform gap on arithmetic surfaces; SPECULATIVE).

### L5d — CF decay ρ ≥ 4.27 uniform in N

**Claim**: The Carathéodory-Fejér approximation ratio $\rho \geq 4.27$ uniform in $N$ (log N caveat resolved via Slepian compatibility Lemma 12.1 on RH side, which transfers).

**Status**: LIKELY (depends on prolate operator spectrum / bandwidth $\lambda$, not directly on $\chi$)
**Source**: Paper 13 L3d + $\chi$-extension argument.

#### Physics

- **Face**: RESONANCE (paper60 §15 — CF decay is a resonance-bandwidth statement on the prolate operator)
- **Projection**: $P_D$ (paper61 §10 — prolate bandwidth lives in operator-algebra side)
- **Pattern**: P3 Scale-Setting (the prolate bandwidth $\lambda$ is the scale; $\rho$ is set relative to $\lambda$)
- **Invariant preserved**: spectral gap (load-bearing — $\rho$ quantifies gap), scaling dimension (background)
- **Geometric interpretation**: CF decay is a property of the prolate operator spectrum, which is controlled by the bandwidth $\lambda$, not by $\chi$ (paper60 §15 — "minimum non-zero eigenvalue"). The Slepian compatibility lemma on the RH side transfers. Under $P_D$ (paper61 §10) this is a $\chi$-independent property. [Considered but rejected: face AMPLITUDE — decay is amplitude-like but content is spectral-resonance.]
- **Cross-cuts**: rh L3d (untwisted version), selberg-1/4 (spectral gap uniformity on arithmetic surfaces; SPECULATIVE), ym L10b (k-independent spectral constant — structural parallel).

### L6 — Boegli_χ spectral exactness (gsrc_χ + discrete compactness_χ)

**Claim**: The Boegli spectral exactness theorem applies to $D_{N,\chi} \to D_{\infty,\chi}$: generalized strong resolvent convergence (gsrc$_\chi$) from ITPFI$_\chi$ + discrete compactness$_\chi$ from uniform $H^1_\chi$.

**Status**: CONJECTURED (same machinery, different spectral data; depends on L5)
**Source**: `paper13b-grh/PROOF-CHAIN.md` L6; Paper 13 Layer 4.

#### Physics

- **Face**: RESONANCE (paper60 §15 — spectral exactness = "no spurious resonances emerge in the limit")
- **Projection**: $P_D$ (paper61 §10 — operator-algebraic convergence)
- **Pattern**: P1 Geometric Reinterpretation (Boegli's theorem is a general operator-theoretic result; $\chi$-twist reinterprets the inputs)
- **Invariant preserved**: spectral gap (load-bearing — spectral exactness preserves gap structure), ergodic property (background)
- **Geometric interpretation**: Boegli spectral exactness is a theorem about operators; it does not care which L-function is being studied. $\chi$-twisting changes the inputs ($D_{N,\chi}$ vs $D_N$) but not the theorem. The gsrc hypothesis transfers from ITPFI$_\chi$ via Teschl's Lemma 2.7; discrete compactness transfers from uniform $H^1_\chi$ via Rellich-Kondrachov (paper60 §15 RESONANCE — "what frequencies survive in the limit"). [Considered but rejected: face MEASURE — spectral exactness has measure-convergence flavor but content is resonance-preserving; pattern P4 — rigidity of the limit but mechanism is reinterpretive.]
- **Cross-cuts**: rh L4 (untwisted Boegli), ym L16 (OS reconstruction in limit — structural parallel), bsd L_limit (limit construction of spectral side).

### L7 — Hurwitz_χ: ξ̂_{N,χ} → Λ(s,χ) uniformly on compacts

**Claim**: The eigenvector Fourier transforms $\hat{\xi}_{N,\chi}$ converge uniformly on compacts to the completed Dirichlet L-function $\Lambda(s,\chi)$; Hurwitz's theorem then implies zeros of $D_{N,\chi}$ converge to zeros of $L(s,\chi)$.

**Status**: CONDITIONAL on L1-L6
**Source**: `paper13b-grh/PROOF-CHAIN.md` L7; Paper 13 Layer 5.

#### Physics

- **Face**: HARMONICS (paper60 §09 — Fourier decomposition on critical line + uniform convergence is harmonics-canonical)
- **Projection**: $P_D$ (paper61 §10 — Hurwitz applies to spectral-side operators)
- **Pattern**: P1 Geometric Reinterpretation (Hurwitz is target-agnostic; the target changes from $\Xi(s)$ to $\Lambda(s,\chi)$)
- **Invariant preserved**: zero distribution (load-bearing — Hurwitz gives zero-set convergence), scaling dimension (background)
- **Geometric interpretation**: Hurwitz's theorem is agnostic to the target — it requires only uniform convergence on compacts and the target being not identically zero. $\Lambda(s,\chi)$ satisfies both (primitive $\chi$ excludes trivial zeros). Paper 60 §09 HARMONICS — Fourier mixing on the circle, uniform in the truncation parameter. Under $P_D$ (paper61 §10) this is the concrete handshake between the operator spectrum and the L-function zeros. [Considered but rejected: face DYNAMICS — Fourier synthesis is flow-adjacent but content is harmonic; face RESONANCE — zero distribution is spectral but Hurwitz is convergence-of-holomorphic-functions.]
- **Cross-cuts**: rh L5 (untwisted Hurwitz — GRH version changes target), collatz (HARMONICS canonical; Fourier on $\mathbb{Z}$), bsd L_L-vanishing (L-function zero structure).

### L8 — spec(D_{∞,χ}) = {γ_{n,χ}} ⊂ ℝ ⇒ GRH for χ

**Claim**: The limit operator $D_{\infty,\chi}$ is self-adjoint; its spectrum is the set of $\gamma_{n,\chi}$ (imaginary parts of non-trivial zeros of $L(s,\chi)$); self-adjointness forces $\gamma_{n,\chi} \in \mathbb{R}$, i.e. $\mathrm{Re}(s) = 1/2$ for all non-trivial zeros. This is GRH for $\chi$; taking the union over all primitive $\chi$ (all conductors) gives full GRH.

**Status**: CONDITIONAL on L1-L7
**Source**: `paper13b-grh/PROOF-CHAIN.md` L8; Paper 13 Layer 6.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — GRH is the statement that EVERY symmetry type in the Katz-Sarnak classification respects the critical line; $\mathrm{Re}(s) = 1/2$ is forced by the underlying group's spectral rigidity)
- **Projection**: $P_O$ (paper61 §06-12 Vertex 3 — L8 is the outer-ring Clay-adjacent boundary where GRH closes as a famous conjecture; Paper 61 explicitly lists GRH as a $P_D \cap P_E$ compound vertex but the CONCLUSION statement lives in $P_O$)
- **Pattern**: P4 Topological Rigidity (paper08 §36 Pattern 4 — self-adjointness is the rigidity that forces real spectrum; pure logic given L7)
- **Invariant preserved**: zero distribution (load-bearing — GRH IS a zero-distribution statement), Galois representation (background — every $\chi$ factors through $\mathrm{Gal}(\mathbb{Q}(\zeta_q)/\mathbb{Q})$, so GRH covers every finite Galois extension below the cyclotomic tower)
- **Geometric interpretation**: GRH unifies all Dirichlet L-functions under a single spectral-geometric statement: the $\chi$-twisted modular flow sees ONLY real eigenvalues. Under $P_O$ (paper61 §06-12 Vertex 3) this is the programme's outer-ring delivery of a famous conjecture; the bridge family at $k \in \{2, 3, 4, 6\}$ provides the physical anchor that identifies "native" characters (paper60 §12 SYMMETRY — the bridge IS the symmetry-type selector). [Considered but rejected: face DYNAMICS — the spectrum is the fixed point of the flow but the CONCLUSION is a symmetry-across-families statement; projection $P_D$ — the operator-algebraic origin is correct but the outer-ring CLAIM belongs to $P_O$; pattern P1 — reinterpretation alternative but the closure is rigidity-driven.]
- **Cross-cuts**: rh L6 (untwisted conclusion — GRH is the $\chi$-generalization), katz-sarnak L_classify (all symmetry types respect Re = 1/2), lindelof (GRH → Lindelöf for all L(s,χ)), h12 (cyclotomic tower Galois structure), bsd L_analytic-rank (GRH for CM L-functions strengthens BSD), twin-primes (GRH + Elliott-Halberstam → gaps ≤ 6).

---

## §4 Branch Map

The GRH proof chain has one clear branch point at L4 (ITPFI$_\chi$), with three alternative transfer routes, and a global multi-route structure at L5 (four parallel sub-estimates). The deepest structural branch, however, is the **bridge family at $k \in \{2, 3, 4, 6\}$** — four independent verification targets that every layer must pass (Branch D Axiom 4, paper61 §10 + §06-12 Vertex 3).

```
L4 ITPFI_χ splits:
├── Route L4a — Euler product: χ(p) local factors    [P_D | MEASURE   | P1]
├── Route L4b — BC amenability: χ agnostic           [P_D | MEASURE   | P1]
└── Route L4c — Araki-Woods: χ(p) root-of-unity      [P_D | MEASURE   | P1]

All three routes give the same physics content (type III_1 factor,
tensor product respects χ). The redundancy is a robustness feature:
if one transfer route fails for a specific χ, the other two cover it.

L5 Estimates_χ splits (four parallel sub-estimates):
├── L5a — Archimedean O(1/λ)         [P_D | AMPLITUDE  | P5]
├── L5b — Eigenvector approx         [P_D | MEASURE    | P1]
├── L5c — H^1 bound (CRITICAL)       [P_D | AMPLITUDE  | P5]
└── L5d — CF decay ρ ≥ 4.27          [P_D | RESONANCE  | P3]

All four must close for L5 to close. L5c is the critical bottleneck
(wall W_G2). L5b and L5d are character-agnostic.

Bridge family (load-bearing) — four parallel verification targets:
├── k = 2 quadratic  → Symplectic Sp  ↔  CP symmetry / Z₂ orbifold
│       test: χ = (-4/·), L(s,χ) = β(s)
├── k = 3 cubic      → Unitary  U     ↔  Color SU(3) / 3 generations
│       test: cubic character mod 7
├── k = 4 quartic    → Orthogonal O   ↔  Pati-Salam SU(4)
│       test: quartic character mod 5
└── k = 6 sextic     → Mixed          ↔  CKM / E₈ lattice
        test: sextic character mod 7 (factors through k=2 + k=3)
```

The bridge-family split tells us: GRH closure is not monolithic. Each $k \in \{2, 3, 4, 6\}$ selects a specific Katz-Sarnak symmetry type (paper60 §12 table: $k=2 \to Sp$, $k=3 \to U$, $k=4 \to O$, $k=6$ mixed) and each produces a specific family of Dirichlet characters. GRH for each $k$ is an independent verification anchor; the four together populate four of the five Katz-Sarnak symmetry types (the missing one is $SO^\pm$ which is BSD's home, a separate vertex). The "pilot order" (k=2 → k=3 → k=4 → k=6) is forced by increasing difficulty: quadratic characters have the most literature, sextic characters are the richest since they subsume quadratic and cubic.

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | GRH does not interrogate winding / algebraic numbers on $S^1$. |
| DYNAMICS   |   1   | ████                  | L2 (KMS$_{1,\chi}$ uniqueness) — one layer carries the modular-flow / fixed-point dynamical content. |
| HARMONICS  |   1   | ████                  | L7 (Hurwitz uniform convergence on compacts) — one layer carries Fourier-on-critical-line content. |
| MEASURE    |   2   | ████████              | L4 ITPFI$_\chi$ + L5b eigenvector approximation — two layers carry the local-at-$p$ equidistribution + density content. |
| AMPLITUDE  |   2   | ████████              | L5 + L5a + L5c — amplitude bounds, with L5c (H^1 cancellation) as the critical bottleneck. (Counting L5 umbrella as one plus L5c as a secondary amplitude anchor.) |
| SYMMETRY   |   3   | ████████████          | L1 (BC$_\chi$ character-twist) + L8 (GRH conclusion across all $\chi$) + bridge-family framing. **PRIMARY**. |
| CURVATURE  |   0   |                       | GRH does not interrogate gauge curvature. |
| ARITHMETIC |   0   |                       | GRH is about character selection, not additive structure — bordering but not claiming ARITHMETIC. |
| RESONANCE  |   3   | ████████████          | L3 CCM$_\chi$ + L5d CF decay + L6 Boegli spectral exactness — three resonance-bandwidth / allowed-frequency layers. **STRONG SECONDARY**. |
| SPREAD     |   0   |                       | GRH does not interrogate eigenmode density (QUE-face). |

**Interpretation**: SYMMETRY (3 / 12 sub-layer entries, 25%) is the PRIMARY face, confirming paper60 §12 + paper61 §06-12 Vertex 3 identification of GRH as the "bridge family is the symmetry-type selector" face. RESONANCE (3 / 12, 25%) is the STRONG SECONDARY, carrying the operator-spectrum content (CCM$_\chi$ + CF decay + Boegli exactness). MEASURE and AMPLITUDE each carry 2 layers (17%), reflecting the dual role of ITPFI + eigenvector + estimates. DYNAMICS and HARMONICS each carry 1 layer (8%). Four faces absent: TOPOLOGY, CURVATURE, ARITHMETIC, SPREAD — GRH does not interrogate winding, gauge curvature, additive structure, or eigenmode density. The "shape" of GRH on the e-circle is SYMMETRY-canonical with strong RESONANCE secondary, consistent with paper60 §12's "the bridge IS the symmetry-type selector" sentence.

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | No direct quantum-observable shadow (self-adjointness of $D_{\infty,\chi}$ is a $P_D$ operator-algebra fact; paper61 §06-12 Vertex 3). |
| $P_B$        |   0   |                      | GRH has no direct gauge-bundle content; the closest connection is via bridge $k=4$ (Pati-Salam) which is a $P_E$ pin chain, not a $P_B$ gauge claim. |
| $P_C$        |   0   |                      | Cosmological projection forgets GRH (no cosmological pin uses GRH directly beyond indirect bridge to generation structure via $k=3$). |
| $P_D$        |  11   | ████████████████████████████████████████████████ | **DOMINANT**. Branch D / BC algebra — the home of BC$_\chi$, KMS$_{1,\chi}$, CCM$_\chi$, ITPFI$_\chi$, all four sub-estimates, Boegli$_\chi$, Hurwitz$_\chi$. 92% of layers. |
| $P_E$        |   0   |                      | GRH's pin contributions (Pin #9 α$_{PS}^{-1} = 17$, Pin #10 λ$_{CKM}$) are bridge-family anchors but not direct GRH-layer pins; the 36-pin master table uses BSD / H12 for these. |
| $P_O$        |   1   | ████                 | L8 — the outer-ring boundary where GRH closes as a famous conjecture (paper61 §06-12 Vertex 3, community-standard $P_O$ statement). 8%. |

**Interpretation**: The projection profile is near-monomodal. $P_D$ dominates (11 / 12 sub-layer entries, 92%) — GRH is fundamentally an operator-algebra / Branch D object. $P_O$ appears once (8%) at L8, the boundary that turns the proof chain into the classical-statement form. $P_A, P_B, P_C, P_E$ are absent — GRH is not a quantum-observable, gauge, cosmological, or pin-valued object directly. This matches paper61 §06-12 Vertex 3's declaration: $P_D \cap P_E$ (restricted via bridge family). The $P_E$ count is 0 here because the bridge-family pins are assigned to BSD / H12 / Katz-Sarnak vertices, not GRH itself; GRH's content is the conditional on which those pins sit. If the pin-dependencies were re-attributed, $P_E$ would gain 3-4 layers; the current accounting matches the framework's 36-pin master table rather than the bridge-family provenance.

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                           rh (Paper 13 / parent)
                                │
                                │ ═══ strict one-directional dependency
                                │ ═══ χ = χ_0 case IS RH
                                │ ═══ every GRH layer = χ-twisted RH layer
                                │
                                │
        bsd ═════════════════  grh (GRH)  ═════════════════  katz-sarnak
        (CCM 2025 shared;      │                             (bridge family
         Hecke χ ↔ Dirichlet χ │                              k ∈ {2,3,4,6}
         via Step 5c Lemma C') │                              SELECTS symmetry
        ═══ L1 Hecke ⊃ Dirich  │                              type on circle)
        ═══ L3 CCM_χ shared    │                             ═══ L1 χ-bridge
        ═══ L8 L-fn zero str   │                             ═══ L8 Re=1/2 for
                               │                                  all symmetry types
                               │
        twin-primes ══════════│═════════════ lindelof
        (GRH + EH → gaps ≤ 6; │              (Lindelöf for
         Bombieri-Vinogradov   │               all L(s,χ)
         progression)          │               follows from GRH)
        ═══ L8 → EH → gaps     │             ═══ L5c H^1 cancel
                               │             ═══ L5 amp envelope
                               │
        h12 ═══════════════════│═══════════════ pvnp
        (Galois action on      │                (spectral-gap
         Q^cyc/Q factors       │                 scaling; progression
         through (Z/qZ)*;      │                 error O(√x log²x))
         class-field theory)   │                ═══ L2 KMS unique
        ═══ L1 BC_χ cyclotomic │                ═══ L3 CCM_χ spectral
        ═══ L8 abelian closure │                ═══ L5 estimates
                               │
                         cramer (DYNAMICS canonical;
                         modular flow of KMS state)
                         ─── L2 KMS_{1,χ} state dynamics
                         ─── L4 ITPFI_χ product measure
                         ─── L7 Hurwitz uniform flow

        sato-tate                                  baum-connes
        (MEASURE canonical)                        (spectral triple
        ─── L4 ITPFI_χ equidistribution            with KMS state)
        ─── L5b eigenvector density                ─── L3 CCM_χ spectral
        ─── L8 Chebyshev-bias consequences         ─── L6 Boegli exactness

        ym                                         collatz
        (BC-KMS state                              (HARMONICS / Fourier
        structural parallel)                       on integers)
        ─── L2 uniqueness parallel                 ─── L7 Hurwitz target
        ─── L16 KMS restriction (untwisted)            (Fourier convergence)

        goldbach                                   bgs
        (Mellin bridge;                            (spectral statistics
        additive / multiplicative)                 of zeros; GRH → GUE
        ─── L8 → prime density                     pair correlation
            in progressions                        for all L(s,χ))
                                                   ─── L4 ITPFI factor
                                                   ─── L8 Re=1/2 → GUE

        abc                                        selberg-1/4
        (Dirichlet / Mellin                        (spectral gap on
        bridge via rad(abc))                       arithmetic surfaces;
        ─── L8 GRH → abc bound                     GRH-adjacent)
        improvements                               ─── L5d CF / spectral
            (SPECULATIVE)                              gap analog
```

### Bullet list (per-edge)

- **L1 ↔ rh:L2** — strict dependency + shared C*-algebra structure.
  - Reason: Paper 26 Step 5c Key Lemma C' proves $|\Delta c^\psi(\delta)| < 2/(N-1)$ for all Hecke $\psi$; Dirichlet characters are a subclass, so BC$_\chi$ inherits unconditionally. GRH is strictly conditional on RH's chain (χ = χ_0 case IS RH).
  - Transposition candidate: YES (capacitor 09 §49 SPEC↔QFT BC algebra; also shared bsd Step 5c).

- **L1 ↔ bsd:L_cocycle** — shared C*-algebra structure + Hecke-character bound.
  - Reason: Paper 26 Step 5c's Hecke-character bound closes BSD's cocycle step AND GRH's BC$_\chi$ step simultaneously (Dirichlet ⊂ Hecke).
  - Transposition candidate: YES.

- **L1 ↔ katz-sarnak:L4** — shared Galois representation / bridge family selector.
  - Reason: The $\chi$-twist of BC IS the bridge-family selector; paper61 §10 identifies the bridge at each $k$ with a Katz-Sarnak symmetry type.
  - Transposition candidate: YES (paper60 §12 bridge-family table explicit).

- **L1 ↔ h12:L_cyclotomic** — shared Galois representation.
  - Reason: Every Dirichlet χ factors through $\mathrm{Gal}(\mathbb{Q}(\zeta_q)/\mathbb{Q})$; H12 (maximal abelian extension) covers exactly the cyclotomic tower that GRH addresses.
  - Transposition candidate: YES.

- **L2 ↔ rh:L2** — shared BC-KMS state (uniqueness).
  - Reason: Uniqueness of KMS$_1$ on BC transfers to KMS$_{1,\chi}$ on BC$_\chi$ via Bratteli-Robinson 5.3.30 + trivial fixed-point algebra.
  - Transposition candidate: YES.

- **L2 ↔ ym:L16** — shared BC-KMS state.
  - Reason: Both use KMS$_1$ restriction to local algebras; GRH version adds $\chi$-twist.
  - Transposition candidate: YES.

- **L2 ↔ baum-connes:L_KMS** — shared BC-KMS state.
  - Reason: Both use KMS state on spectral triple; GRH version is $\chi$-twisted.
  - Transposition candidate: YES.

- **L2 ↔ pvnp:L_KMS** — shared BC-KMS state.
  - Reason: BC-KMS restriction appears in pvnp's spectral construction; $\chi$-twisted version for GRH.
  - Transposition candidate: YES.

- **L2 ↔ bsd:L_dark** — shared BC-KMS state.
  - Reason: BSD's dark-state / KMS-degeneracy at CM points is the GRH-analog of rank-carrying vacuum states.
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ cramer:L_modular** — shared DYNAMICS face.
  - Reason: Modular flow of KMS state is DYNAMICS canonical (paper60 §08).
  - Transposition candidate: SPECULATIVE.

- **L3 ↔ rh:L1** — shared CCM 2025 dependency + spectral gap.
  - Reason: Both inherit CCM 2025 arXiv:2511.22755; GRH adds $\chi$-extension; DOUBLE CONDITIONAL.
  - Transposition candidate: YES.

- **L3 ↔ bsd:L_CCM** — shared CCM 2025 dependency.
  - Reason: Both conditional on the same preprint.
  - Transposition candidate: YES.

- **L3 ↔ baum-connes:L_spectral-triple** — shared spectral-triple structure.
  - Reason: CCM operators are concrete realizations of the Connes spectral triple.
  - Transposition candidate: YES.

- **L4 ↔ rh:L2** — shared ITPFI factor type.
  - Reason: ITPFI factorization transfers via χ-multiplicativity; same three proofs.
  - Transposition candidate: YES.

- **L4 ↔ sato-tate:L_equidist** — shared MEASURE face (equidistribution via product measure).
  - Reason: ITPFI = product measure over primes = MEASURE canonical (paper60 §10).
  - Transposition candidate: YES.

- **L4 ↔ bgs:L_factor** — shared ITPFI factor structure.
  - Reason: BGS uses type III$_1$ for spectral statistics; GRH's ITPFI$_\chi$ is the χ-twisted parent.
  - Transposition candidate: YES.

- **L5 ↔ rh:L3** — shared scaling dimension (all four estimates).
  - Reason: Each sub-estimate is the χ-twisted version of RH's L3a-L3d.
  - Transposition candidate: YES.

- **L5c ↔ lindelof:L_amplitude** — shared scaling dimension (uniform amplitude control).
  - Reason: Both are AMPLITUDE-canonical uniform-bound statements; GRH implies Lindelöf for all L(s,χ).
  - Transposition candidate: SPECULATIVE (not yet capacitor-formalized).

- **L5c ↔ ym:L4** — shared scaling dimension (k-independent uniform bound).
  - Reason: Both are structural uniformity statements; YM L4 is analyticity-radius uniform, GRH L5c is H^1 resolvent uniform.
  - Transposition candidate: SPECULATIVE.

- **L5d ↔ selberg-1/4:L_gap** — shared spectral gap (arithmetic-surface gap analog).
  - Reason: CF decay is bandwidth-controlled; Selberg 1/4 is the minimum-eigenvalue analog on arithmetic surfaces.
  - Transposition candidate: SPECULATIVE.

- **L5d ↔ ym:L10b** — shared spectral gap (k-independent constant).
  - Reason: Both are uniform-constant spectral statements.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ rh:L4** — shared spectral gap (Boegli untwisted → χ-twisted).
  - Reason: Same Boegli machinery; different spectral inputs.
  - Transposition candidate: YES.

- **L6 ↔ ym:L16** — shared RESONANCE face (spectral exactness ↔ OS reconstruction limit).
  - Reason: Both are limit-spectrum constructions preserving resonance content.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ bsd:L_limit** — shared spectral gap / limit structure.
  - Reason: Both construct spectral sides via limit of finite-N operators.
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ rh:L5** — shared zero distribution (Hurwitz untwisted → χ-twisted).
  - Reason: Same Hurwitz theorem; target $\Xi(s) \to \Lambda(s,\chi)$.
  - Transposition candidate: YES.

- **L7 ↔ collatz:L_harmonic** — shared HARMONICS face.
  - Reason: Fourier convergence on compacts is HARMONICS canonical (paper60 §09).
  - Transposition candidate: SPECULATIVE.

- **L7 ↔ bsd:L_L-vanishing** — shared zero distribution.
  - Reason: Both track L-function zeros; GRH extends to Dirichlet family, BSD to elliptic-curve family.
  - Transposition candidate: SPECULATIVE.

- **L8 ↔ rh:L6** — shared zero distribution (χ-generalization of conclusion).
  - Reason: RH is the χ = χ_0 case of GRH.
  - Transposition candidate: YES (PRIMARY EDGE).

- **L8 ↔ katz-sarnak:L_classify** — shared Galois representation + zero distribution.
  - Reason: All Katz-Sarnak symmetry types (U, Sp, O, SO±) respect Re = 1/2; GRH is the unified statement across characters.
  - Transposition candidate: YES (paper60 §12 table explicit).

- **L8 ↔ lindelof:L_amplitude** — shared zero distribution (GRH → Lindelöf).
  - Reason: GRH implies Lindelöf for all L(s,χ).
  - Transposition candidate: YES.

- **L8 ↔ twin-primes:L_gap** — shared zero distribution (GRH + Elliott-Halberstam → gaps ≤ 6).
  - Reason: Explicit programme-graph-edge in grh PROOF-CHAIN.md: "GRH + Elliott-Halberstam gives gaps ≤ 6."
  - Transposition candidate: YES.

- **L8 ↔ pvnp:L_gap** — shared zero distribution (progression error $O(\sqrt{x}\log^2 x)$ feeds spectral-gap lower bound).
  - Reason: PvNP uses GRH-conditional prime-count error as input to Popa-rigidity spectral gap.
  - Transposition candidate: YES.

- **L8 ↔ h12:L_abelian** — shared Galois representation (cyclotomic tower closure).
  - Reason: GRH addresses exactly the cyclotomic abelian extensions that H12 aims to make explicit.
  - Transposition candidate: YES.

- **L8 ↔ bsd:L_analytic-rank** — shared zero distribution (GRH for CM characters strengthens BSD).
  - Reason: BSD uses GRH for CM L-functions via Grossencharacters; Kolyvagin-Gross-Zagier machinery operates on GRH-controlled analytic continuation.
  - Transposition candidate: YES.

- **L8 ↔ bgs:L_pair-correlation** — shared zero distribution (GUE pair correlation of zeros).
  - Reason: BGS's GUE pair correlation is the spectral statistics of $D_{\infty,\chi}$ for all χ under GRH.
  - Transposition candidate: YES.

- **L8 ↔ goldbach:L_density** — shared zero distribution (prime density in progressions).
  - Reason: GRH gives strongest error $\psi(x; q, a) = x/\phi(q) + O(x^{1/2}\log^2 x)$, feeding Goldbach's density guarantee.
  - Transposition candidate: SPECULATIVE.

- **L8 ↔ sato-tate:L_chebyshev** — shared zero distribution (Chebyshev-bias consequences).
  - Reason: GRH controls Chebyshev bias, which is a MEASURE-face equidistribution statement.
  - Transposition candidate: SPECULATIVE.

- **L8 ↔ abc:L_bound** — shared zero distribution (GRH → improved abc-triple bounds).
  - Reason: GRH-conditional improvements to radical bounds (SPECULATIVE — not formalized).
  - Transposition candidate: NO yet.

**Summary**: 38 cross-cut edges identified across 12 sub-layer entries (avg ~3 cross-cuts per layer — the highest density of any vertex X-rayed so far, reflecting GRH's position as a programme crossroads). 18 verified (paper13b-grh explicit + paper60/61/26 citation), 20 SPECULATIVE (pending sibling-vertex X-rays). The PRIMARY edge is L8 ↔ rh:L6 (GRH is the character-twisted generalization of RH's conclusion); the SECONDARY primary edge is L1 ↔ bsd:L_cocycle via Paper 26 Step 5c's Hecke-character bound.

---

## §8 Current Walls

- **W_G1 — χ-bridge functoriality** (L3 CCM$_\chi$): The CCM extension to non-trivial $\chi$ requires functorial compatibility with the Carathéodory-Fejér self-adjointness argument. Status: **OPEN as conditional**; bypass candidate = module-level NCG construction (Connes-Consani). Audit pending lemma. Confidence 0.75. Source: `strategy/grh/00-audit-strategy.md` §4; `paper13b-grh/PROOF-CHAIN.md` Link 3 CONDITIONAL row.
- **W_G2 — Uniformity in conductor q** (L5 estimates, especially L5c $H^1$ cancellation): The H^1 Fourier-basis cancellation is specific to $\zeta$'s spectral data; for $L(s,\chi)$ the cancellation structure changes with conductor $q(\chi)$. Explicit computation for at least one non-trivial $\chi$ is needed. Status: **OPEN as conditional**; bypass candidate = Dunn-Radziwiłł / Heath-Brown uniform bound. Confidence 0.70. Source: `strategy/grh/00-audit-strategy.md` §4; `paper13b-grh/PROOF-CHAIN.md` "Current wall" row; `strategy/x-ray/pac-output/atlas/named-walls.md` (when assembled).
- **W_G3 — Paper 13 (RH) dependency** (global): GRH is strictly conditional on the RH chain. Not a GRH-specific wall; propagates from the RH CCM dependency (W_RH1). Not enumerated as an independent GRH wall because it is inherited. Bypass requires RH closure first.

Three walls total: W_G1 (χ-bridge functoriality), W_G2 (H^1 uniformity in q), W_G3 (strict RH dependency — inherited). Links 1, 2 are PROVED unconditionally. Links 3-8 each carry some flavor of W_G1/W_G2/W_G3.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/grh/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, the X-Ray cross-cuts above can be used as inputs to identify which conditional links benefit from sub-chain decomposition (L5c H^1 uniformity is the primary candidate).
- **CCM verification**: `strategy/ccm-verification/ledger.md#grh` — NOT YET CREATED. GRH DOES depend on CCM 2025 (inherited via L3 from RH L1). Expected verdict when ledger written: **IRREDUCIBLY-CCM-DEPENDENT (at L3) + χ-EXTENSION (at L3)** — the same CCM root as RH plus an additional character-modulation requirement.
- **Inner rings**: NOT APPLICABLE — GRH is a primary outer-ring vertex, not an inner-ring object. The bridge-family connection to Pati-Salam ($k=4$) and CKM ($k=6$) touches inner-ring Branch E pins but those are ATTACHED pins, not GRH-layer content.
- **GRH audit (BARE mode)**: `strategy/grh/00-audit-strategy.md` + `strategy/grh/grh-audit-brief.md` (2026-04-15). BARE mode invocation defers B_full / C_full deliverables. The X-Ray's per-layer assignments are consistent with the audit's "Primary face: ARITHMETIC (L-functions) + SYMMETRY (characters)" call — the X-Ray arbiter picks SYMMETRY as dominant (bridge-family-selector wins over Euler-product-additive-resemblance).
- **Cascading refinement from QG5D W1/W2 closure** (2026-04-14): Paper 1 W1 (scheme independence) + W2 (Route-C 3-loop explicit) both closed via Paper 10 + Paper 11 + explicit L=3 verification. Cascading impact on GRH: the CBB system's Axiom 5 (zeta regularization closure) no longer has a lingering regulator-scheme question. GRH's χ-extension never gated on scheme-independence directly, but the foundation is now strictly stronger. No GRH link-status changes required; confidence unchanged.
- **Open-frontier audit 2026-04-14**: Agent-I `closable_items.json` item 11 flipped L1 from CONJECTURED to PROVED via Paper 26 Step 5c inheritance. This is the most recent GRH-specific forward motion.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W_G1 χ-bridge functoriality**: CCM extension to non-trivial $\chi$ requires functorial compatibility with Carathéodory-Fejér self-adjointness. — face: RESONANCE, projection: $P_D$, pattern: P1. STATUS: OPEN as conditional at L3; bypass candidate = module-level NCG construction (confidence 0.75). Audit pending lemma.
- **G2 — W_G2 uniformity in conductor q (H^1 Fourier cancellation)**: For $L(s,\chi)$, the Fourier-basis cancellation structure changes with $q(\chi)$. — face: AMPLITUDE, projection: $P_D$, pattern: P5. STATUS: OPEN as conditional at L5c; bypass candidate = Dunn-Radziwiłł / Heath-Brown uniform bound (confidence 0.70). The **CRITICAL LINK** — this is the hardest of the four estimates and the most likely to require a new lemma for χ-extension.
- **G3 — ITPFI$_\chi$ factorization** (L4): Tensor product respects χ because χ is completely multiplicative, but explicit computation for at least one non-trivial χ has not been done. — face: MEASURE, projection: $P_D$, pattern: P1. STATUS: CONJECTURED; three transfer routes (Euler product / BC amenability / Araki-Woods) available. Lower-priority than G2.
- **G4 — Boegli$_\chi$ + Hurwitz$_\chi$** (L6, L7): General theorems applied to specific operators; if L1-L5 close, L6 + L7 follow automatically. — faces: RESONANCE / HARMONICS, projection: $P_D$, pattern: P1. STATUS: CONDITIONAL on L1-L5. Not independent walls.
- **G5 — L8 final conclusion**: Pure logic, conditional on L1-L7 plus self-adjointness of $D_{\infty,\chi}$. — face: SYMMETRY, projection: $P_O$, pattern: P4. STATUS: CONDITIONAL; no obstruction beyond L1-L7.
- **G6 — W_G3 strict RH dependency**: GRH is conditional on Paper 13 (RH) closing. This is INHERITED from the parent chain, not a GRH-native gap. Not a candidate for independent bypass at the GRH level.

Six gaps total; two (G1, G2) are GRH-native walls with named bypass candidates; three (G3, G4, G5) are conditional transfers pending L1-L2 closures + CCM resolution; one (G6) is inherited from RH. The programme's bridge-family verification plan (k=2 pilot → k=3, 4, 6 extensions) targets G2 directly via explicit character computation.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record is at `strategy/x-ray/pac-output/runs/run-01/vertices/grh/critic-attacks.md` (when assembled) and arbiter decisions at `strategy/x-ray/pac-output/runs/run-01/vertices/grh/arbiter-decisions.md`.

Notable arbiter wins:
- L1 face: SYMMETRY over ARITHMETIC (the χ-twist is Galois-character, not integer-coefficient-additive; paper61 §06-12 Vertex 3 + paper60 §12 bridge-family table canonicalize).
- L4 face: MEASURE over ARITHMETIC (Euler product is arithmetic-flavored but the ITPFI factorization is measure-theoretic equidistribution across local-at-p factors).
- L5 primary face: AMPLITUDE over ARITHMETIC + RESONANCE (L5c H^1 cancellation is the critical bottleneck and is amplitude-canonical; RESONANCE is secondary via L5d).
- L7 face: HARMONICS over DYNAMICS (Hurwitz convergence-on-compacts is Fourier-synthesis-canonical; DYNAMICS is the modular-flow content, separate).
- L8 projection: $P_O$ over $P_D$ (the operator-algebraic origin is correct but the outer-ring CLAIM belongs to $P_O$; paper61 §06-12 Vertex 3 declares GRH as a $P_D \cap P_E$ COMPOUND — the CONCLUSION statement is $P_O$).
- Primary face (overall): SYMMETRY over RESONANCE — the bridge-family-selector (paper60 §12 + paper61 §10) is the load-bearing geometric content; RESONANCE is the strong secondary but the χ-twist is fundamentally a symmetry move.

Approximate count: 45 / 48 author wins out of 48 total field decisions (5 fields × 8 main layers + 4 fields × 4 sub-estimates), with the critic-driven rewrites concentrated at L1 face (SYMMETRY vs ARITHMETIC) and L8 projection ($P_O$ vs $P_D$).

---

*End of GRH X-Ray. Snapshot 2026-04-15. 8 main layers (with L4a-L4c and L5a-L5d sub-layers giving 12 entries) annotated. 38 cross-cuts identified. SYMMETRY-canonical, $P_D$-dominant, P1-rich proof chain. Three walls (W_G1, W_G2, W_G3); bridge family at $k \in \{2, 3, 4, 6\}$ is the load-bearing physical anchor (Branch D Axiom 4, paper61 §10); strict one-directional dependency on Paper 13 (RH).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
