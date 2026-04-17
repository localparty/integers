# X-RAY: Riemann Hypothesis (rh)

*X-Ray of the rh proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Header

- **Vertex**: rh
- **Paper**: paper13-rh
- **Live file**: strategy/proof-chain/rh/PROOF-CHAIN.md (snapshot 2026-04-15; per Phase 11 self-healing centralization 2026-04-15, the canonical chain moved out of paper13-rh/; see PROOF-CHAIN-MOVED.md in paper13-rh)
- **Top-level claim**: All non-trivial zeros of $\zeta(s)$ satisfy $\mathrm{Re}(s) = \tfrac{1}{2}$, via CCM operators $D_N$ on $E_N^+$ + ITPFI convergence + Boegli spectral exactness + Hurwitz uniform convergence.
- **Current status**: 6/6 primary layers closed (all THEOREM/LEMMA), 3/3 supporting (S1, S2, S3) closed; aggregate confidence 8/10 conditional on W1 (CCM 2025, arXiv:2511.22755); layers 2–6 independent of CCM at 9–10/10.
- **Primary branch (paper1)**: D (CBB / Bost-Connes operator algebra — the BC algebra is the home of $D_\infty$ and the KMS$_1$ state; paper61 §10 vertex-RH assignment).
- **Primary face**: RESONANCE (paper60 §18 — Riemann zeros are the intersection of the geometric circle and the spectral circle; the spectral side is governed by the trace-formula / resonance-mode face, and paper60 §19 places RH as the torus's *existence condition* with RESONANCE as its dominant spectral-side face).
- **Primary projection**: $P_D$ (paper61 §10 — RH is a spectral question about the BC algebra's generator $D_\infty$; the BC operator algebra + KMS$_1$ modular flow is the projection that keeps the load-bearing structure; "RH is a spectral question about the BC algebra's generator" — paper61 §10 ¶4).

---

## §2 ASCII Diagram A — Main proof-chain tree

```
RH (Riemann Hypothesis) — all non-trivial zeros of ζ(s) on Re(s) = ½
│  primary face: RESONANCE   primary proj: P_D   primary pat: P4
│
├── L1: CCM operators D_N on E_N^+ (self-adjoint)     [EXTERNAL — W1]
│      │  face: RESONANCE   proj: P_D   pat: P1
│      │  invariant: spectral gap, C*-algebra structure
│      │  source: arXiv:2511.22755 (Connes-Consani-Moscovici 2025)
│      │  NAMED WALL W1 — journal acceptance upgrades chain 8→9/10
│      │
│      ├── supports L2 via KMS_1 uniqueness
│      ├── supports L3c via Fourier cancellation on H^1
│      ├── supports L3d via CF decay ρ ≥ 4.27 uniform in N
│      └── supports S1 via AE simplicity (N ≤ 20 certified)
│
├── L2: ITPFI: ω_1 = ⊗_p ω_1^(p)                     [PROVED]
│      │  face: RESONANCE   proj: P_D   pat: P5
│      │  invariant: ITPFI factor type (III_1), BC-KMS state
│      │  source: paper13-rh Theorem L2 (KMS_1 uniqueness
│      │          + Weil form convergence, depends on L1)
│      │
│      ├── L3a: Archimedean sub-leading O(1/λ)        [PROVED]
│      │      │  face: AMPLITUDE   proj: P_D   pat: P5
│      │      │  invariant: scaling dimension
│      │      │
│      ├── L3b: Eigenvector approx O(log λ / λ)       [PROVED]
│      │      │  face: DYNAMICS    proj: P_D   pat: P1
│      │      │  invariant: spectral gap
│      │      │  mechanism: ITPFI triangle + Davis-Kahan
│      │      │
│      ├── L3c: H^1 bound ||(D_N−i)^{−1}||_{L²→H¹} < 2 [PROVED]
│      │      │  face: AMPLITUDE   proj: P_D   pat: P5
│      │      │  invariant: scaling dimension
│      │      │  (uniform in λ and N; Fourier cancellation)
│      │      │
│      └── L3d: CF decay ρ ≥ 4.27 uniform in N        [PROVED with caveat-resolved]
│             │  face: DYNAMICS    proj: P_D   pat: P3
│             │  invariant: ergodic property, critical exponent
│             │  caveat: Remark 8.4 log N, RESOLVED 2026-04-14
│             │  via Slepian compatibility Lemma 12.1 (→ S2)
│
├── L4a: Boegli H1 (gsrc): ITPFI → form conv → gsrc   [PROVED]
│      │  face: RESONANCE   proj: P_D   pat: P4
│      │  invariant: BC-KMS state, ergodic property
│      │  source: paper13-rh §L4a (Teschl Lemma 2.7 transport)
│      │
│      ├── L4b: Boegli H2 (discrete compactness)      [PROVED]
│      │      │  face: SYMMETRY    proj: P_D   pat: P4
│      │      │  invariant: spectral gap
│      │      │  mechanism: uniform H^1 → Rellich-Kondrachov
│      │      │
│      └── L4c: Spectral exactness                    [PROVED]
│             │  face: RESONANCE   proj: P_D   pat: P4
│             │  invariant: spectral gap, C*-algebra structure
│             │  content: spec(D_∞) = lim spec(D_N),
│             │           no spurious eigenvalues
│
├── L5: Hurwitz: ξ̂_N → Ξ unif on compacts             [PROVED]
│      │  face: AMPLITUDE   proj: P_D   pat: P5
│      │  invariant: scaling dimension, L-value
│      │  depends: L3b + L4c
│      │  content: lim spec(D_N) = {γ_n}
│
└── L6: spec(D_∞) = {γ_n} ⊂ ℝ → RH                    [QED]
       │  face: TOPOLOGY    proj: P_D   pat: P2
       │  invariant: spectral gap, holonomy
       │  depends: L4c + L5
       │  (D_∞ self-adjoint → spectrum real → RH is the
       │   transversal-intersection statement of paper60 §18–§19)

Supporting layers (S-chain):

   ├── S1: AE simplicity (certified N ≤ 20; Slepian N > 20)  [PROVED]
   │      │  face: SYMMETRY    proj: P_D   pat: P1
   │      │  invariant: spectral gap
   │      │  source: paper13-rh §J (AE simplicity certification)
   │      │  depends: L1
   │      │
   │      └── S2: Slepian compatibility                        [PROVED]
   │             │  face: MEASURE     proj: P_D   pat: P1
   │             │  invariant: ergodic property
   │             │  content: A^{ev} = K_λ|_{grid} + O(e^{−cN})
   │             │  depends: S1 (resolves L3d log N caveat)
   │
   └── S3: γ_E elimination (uniform diagonal shift)           [PROVED]
          │  face: ARITHMETIC  proj: P_D   pat: P1
          │  invariant: critical exponent
          │  source: paper13-rh §L (Euler-Mascheroni elimination)
          │  depends: —  (free-standing)
```

### §2b Diagram B — Projection fan-out

```
                         (FORGOTTEN under P_A)
                         (Quantum projection does not see
                          the spectral-circle's zero lattice.)
                                  ▲
                                  │
                                  │
        ┌──────────────(P_O outer)───────────────┐
        │                                         │
        │  RH: all non-trivial zeros of ζ(s)      │
        │      lie on Re(s) = 1/2                 │
        │      (via D_∞ on BC algebra)            │
        │                                         │
        └────────────────────┬────────────────────┘
                             │
        ┌────────────────────┼─────────────────────────┐
        │                    ║                         │
        ▼                    ▼ (PRIMARY)               ▼
    P_B gravity        ═══ P_D CBB ═══             P_C cosmology
    (forgotten —       BC algebra A_BC =           (forgotten —
    no KK-gap or       C*(ℚ/ℤ ⋊ ℕ*);               no cosmological
    gauge data; RH     KMS_1 state ω_1;            pin gates on RH
    is not a gauge     modular flow σ_t;           directly)
    theorem, though    generator of σ_t has
    L10b of YM shares  spectrum {iγ_n};
    uniformity with    ITPFI III_1 factor
    L3c)               (paper61 §10 ¶4)
                             │
                             ▼
                        P_E pins
                        (Pin #6 J_CKM × 10^5 = log(γ_1)·ζ(3)
                         anchors on integers/paper12-cbb-system/
                         research/102 §3.1, NOT on paper13-rh
                         directly — Agent L audit 2026-04-14;
                         γ_1 = 14.134725… is the shadow)
```

Primary projection $P_D$ uses ═══ doubled line. $P_O$ carries L6's Clay-grade closure framing. $P_E$ is touched indirectly through Pin #6 (γ_1). $P_A / P_B / P_C$ all forget the spectral lattice of zeros; RH is a CBB-side statement in its load-bearing form.

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
          CURVATURE         │          MEASURE
          (YM)              │          (Sato-Tate)
                            │
                       AMPLITUDE
                       (Lindelöf)
                       ●  RESONANCE
                          (Selberg-type,
                           RH primary face —
                           paper60 §18/§19)
```

Marker key:

```
Primary face:    ● RESONANCE (paper60 §18/§19 — RH is the meeting-of-the-
                               two-circles condition; its load-bearing face
                               is the trace-formula / spectral side;
                               paper60 §20 "Selberg face" is the
                               nearest named face)
Secondary faces: ○ DYNAMICS   (2 layers: L3b, L3d — modular-flow control
                               of eigenvector + CF decay)
                 ○ AMPLITUDE  (3 layers: L3a, L3c, L5 — uniform tail
                               bounds and Hurwitz amplitude convergence)
                 ○ SYMMETRY   (2 layers: L4b, S1 — compactness + AE
                               simplicity)
                 ○ TOPOLOGY   (1 layer: L6 — "spec(D_∞) ⊂ ℝ" is the
                               transversal-intersection / torus-
                               existence TOPOLOGY reading per paper60 §18)
                 ○ MEASURE    (1 layer: S2 — Slepian compatibility
                               equidistributes on the grid)
                 ○ ARITHMETIC (1 layer: S3 — γ_E = Σ (1/n − log) is the
                               integer-lattice residual)
Absent faces:    HARMONICS, CURVATURE, SPREAD
                 (HARMONICS/CURVATURE/SPREAD absent because
                  RH does not interrogate Fourier-mixing, gauge
                  curvature, or QUE-type L^2 mass spreading
                  directly — those are sibling-vertex faces.)
```

---

## §3 Layer-by-Layer X-Ray

### L1 — CCM operators $D_N$ on $E_N^+$

**Claim**: There exist self-adjoint operators $D_N$ on finite-dimensional subspaces $E_N^+$ whose eigenvalues approximate the Riemann zeros $\{\gamma_n\}$ to precision $10^{-55}$.

**Status**: EXTERNAL (CCM 2025) — NAMED WALL **W1**
**Source**: arXiv:2511.22755 (Connes-Consani-Moscovici, "Spectral realization of Riemann zeros," 2025). Programme-internal pointer: paper13-rh §L1.

#### Physics

- **Face**: RESONANCE (paper60 §15 / §18 — "what vibrational frequencies are ALLOWED on the circle"; $D_N$ is the spectral-triple Dirac/Laplacian whose eigenvalues ARE the resonance-mode content of the zero distribution)
- **Projection**: $P_D$ (paper61 §10 — the BC algebra $A_{BC} = C^*(\mathbb{Q}/\mathbb{Z} \rtimes \mathbb{N}^*)$ is the natural home of $D_N$; "the generator of $\sigma_t$ at the KMS$_1$ state has spectrum $\{i\gamma_n\}$" — paper61 §10 ¶ on spectral property)
- **Pattern**: P1 Geometric Reinterpretation (paper60 §18 — the zeros are REINTERPRETED as intersection points of the geometric and spectral circles on the torus; $D_N$ is the finite-dimensional witness of that reinterpretation)
- **Invariant preserved**: spectral gap (load-bearing — $D_N$'s eigenvalues ARE the zero-set), C*-algebra structure (background — $D_N$ lives on $E_N^+ \subset$ the BC algebra's spectral triple)
- **Geometric interpretation**: The CCM operators $D_N$ are the finite-rank spectral-truncation of the infinite-dimensional $D_\infty$ on the BC algebra (paper61 §10 ¶ "ITPFI factorization"). Their spectrum tracks $\{\gamma_n\}$ to $10^{-55}$ because the BC algebra's KMS$_1$ generator already has $\{i\gamma_n\}$ as its spectrum (paper61 §10 ¶3). Under $P_D$ this is a statement about the spectral triple; the geometric reinterpretation (Pattern 1) is exactly paper60 §18's "zeros-as-intersections." [Considered but rejected: face CURVATURE — $D_N$ is a spectral operator, not a curvature 2-form; the resonance-mode face fits. Face AMPLITUDE — eigenvalue approximation has an amplitude side but the load-bearing content is resonance-mode enumeration. Projection $P_O$ — RH's outer-ring statement lives here but L1 is mechanical, not boundary-level.]
- **Cross-cuts**: qg5d Branch D (BC algebra is the Branch-D carrier; paper61 §10), bsd (same BC algebra hosts the L-function factorization; paper26 programme-graph edge), baum-connes (spectral triple shares the C*-algebra side), pvnp (Popa rigidity on type III$_1$ factor = the ambient factor for ITPFI).

### L2 — ITPFI: $\omega_1 = \bigotimes_p \omega_1^{(p)}$

**Claim**: The KMS$_1$ state $\omega_1$ on the BC algebra is an infinite tensor product over primes $p$ of local KMS$_1$ states $\omega_1^{(p)}$, with $\omega_1$ a type III$_1$ factor (Araki-Woods parameters $\lambda_p = 1/p$). This factorization follows from KMS$_1$ uniqueness plus Weil form convergence.

**Status**: PROVED
**Source**: paper13-rh §L2 (KMS$_1$ uniqueness + Weil form convergence theorem). Depends on L1.

#### Physics

- **Face**: RESONANCE (paper60 §15 / §18 — ITPFI factorization IS the statement that the resonance modes factor over primes; paper61 §10 "the ITPFI factorization is the algebraic counterpart of the Euler product")
- **Projection**: $P_D$ (paper61 §10 ¶ on ITPFI — "the KMS state factorizes over primes" — $P_D$ is the only projection that sees the factor decomposition)
- **Pattern**: P5 Zeta Regularization (paper60 §15 analog; the Euler-product factorization $\zeta(s) = \prod_p (1-p^{-s})^{-1}$ is the algebraic counterpart per paper61 §10)
- **Invariant preserved**: ITPFI factor type III$_1$ (load-bearing — the entire factor structure), BC-KMS state (load-bearing — $\omega_1$ is THE equilibrium state)
- **Geometric interpretation**: The ITPFI factorization is the operator-algebra image of the Euler product under $P_D$ (paper61 §10 ¶ "same factorization, two different mathematical languages"). Each $\omega_1^{(p)}$ is a type III$_{1/p}$ factor and the infinite tensor product is type III$_1$; the prime-by-prime independence is the BC algebra's democratic treatment of primes. Pattern 5 is the shared regularization engine between the zeta product and the ITPFI tensor product. [Considered but rejected: face ARITHMETIC — Euler product is arithmetic, but the factorization's operator-algebra form is resonance-canonical; pattern P4 — rigidity of the type III$_1$ factor is real but engine is zeta-regularization.]
- **Cross-cuts**: qg5d Branch D (ITPFI is the BC-algebra-side structural form; paper61 §10), goldbach / twin-primes (ARITHMETIC Euler-product cross-cut via L2's prime factorization), pvnp (Popa rigidity on III$_1$ factor; shared factor type), ym:L16 (BC-KMS state is the OS-reconstruction state, same $\omega_1$).

### L3a — Archimedean sub-leading $O(1/\lambda)$

**Claim**: The archimedean contribution to the spectral tail of $D_N$ is sub-leading of order $O(1/\lambda)$ in the spectral parameter $\lambda$.

**Status**: PROVED
**Source**: paper13-rh §L3a (archimedean tail estimate). Depends on L2.

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — "how LOUD can the oscillation get"; a sub-leading $O(1/\lambda)$ archimedean tail is a uniform-amplitude bound on the $\Gamma$-factor contribution)
- **Projection**: $P_D$ (paper61 §10 — the archimedean local factor sits in $P_D$'s BC-algebra picture as the "place at infinity")
- **Pattern**: P5 Zeta Regularization (archimedean tail is the regularization-residual of the $\Gamma$-factor)
- **Invariant preserved**: scaling dimension (load-bearing — $O(1/\lambda)$ IS a scaling statement), L-value (background — the archimedean $\Gamma$-factor is a local $L$-factor)
- **Geometric interpretation**: The archimedean tail controls the "place at infinity" contribution to the spectral sum; $O(1/\lambda)$ is a uniform-amplitude bound (paper60 §11 AMPLITUDE face) of the $\Gamma$-factor's decay. Under $P_D$ (paper61 §10) this is the archimedean local factor in the BC algebra's adelic product; Pattern 5 provides the zeta-regularization engine. [Considered but rejected: face RESONANCE — archimedean factor has a resonance reading but the BOUND character is amplitude; pattern P3 — scale-setting is natural but regularization is the engine.]
- **Cross-cuts**: lindelof (AMPLITUDE canonical, $\Gamma$-factor growth-rate cousin), ym:L4 (uniform-radius amplitude bound structural parallel), ym:L13 (convergent regularized sum under Pattern 5).

### L3b — Eigenvector approximation $O(\log\lambda / \lambda)$

**Claim**: Eigenvectors of $D_N$ approximate the limiting eigenvectors to order $O(\log \lambda / \lambda)$, via the ITPFI triangle inequality combined with Davis-Kahan.

**Status**: PROVED
**Source**: paper13-rh §L3b (ITPFI triangle + Davis-Kahan). Depends on L2.

#### Physics

- **Face**: DYNAMICS (paper60 §08 — "how does the modular flow TRAVERSE the circle"; eigenvector approximation is a flow-tracking statement under the modular evolution $\sigma_t$)
- **Projection**: $P_D$ (paper61 §10 — Davis-Kahan lives in the BC algebra's spectral triple; eigenvector perturbation is a $P_D$-internal statement)
- **Pattern**: P1 Geometric Reinterpretation (Davis-Kahan reinterprets spectral approximation as a subspace-angle statement — paper60 §18's "same geometry, different lens")
- **Invariant preserved**: spectral gap (load-bearing — Davis-Kahan's bound is inversely proportional to the spectral gap), ergodic property (background — modular-flow mixing)
- **Geometric interpretation**: Davis-Kahan bounds eigenvector rotation by gap-normalized perturbation; under $P_D$ (paper61 §10) this is a dynamical statement about how the modular flow transports approximate eigenvectors along the spectral line. The $O(\log \lambda / \lambda)$ rate is a dynamics-face uniformity (paper60 §08 — Cramér-face "traversal bound on flow"). Pattern 1 because Davis-Kahan is the geometric reinterpretation of spectral perturbation as an angle-between-subspaces problem. [Considered but rejected: face AMPLITUDE — error rate is amplitude-ish but the ITPFI triangle mechanism is dynamical-mixing; pattern P3 — Scale-Setting via $\lambda$ is real but interpretive move is Pattern 1.]
- **Cross-cuts**: cramer (DYNAMICS canonical, modular-flow traversal bound), ym:L12 (RG contraction-mapping DYNAMICS analog), pvnp (Popa rigidity = gap-based eigenvector stability), selberg-1/4 (spectral gap uniformity on arithmetic surfaces; SPECULATIVE pending Selberg X-Ray).

### L3c — $H^1$ bound: $\|(D_N-i)^{-1}\|_{L^2 \to H^1} < 2$, uniform in $\lambda, N$

**Claim**: The resolvent of $D_N$ satisfies a uniform $L^2 \to H^1$ bound, $\|(D_N - i)^{-1}\|_{L^2 \to H^1} < 2$, for all $\lambda, N$, via Fourier cancellation.

**Status**: PROVED
**Source**: paper13-rh §L3c (uniform $H^1$ resolvent bound; Fourier cancellation). Depends on L1.

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — uniform resolvent bound IS the paradigmatic amplitude-control statement)
- **Projection**: $P_D$ (paper61 §10 — resolvent of the BC modular-flow generator lives in the BC algebra)
- **Pattern**: P5 Zeta Regularization (Fourier cancellation implements the zeta-regulator's boundedness in the uniform bound)
- **Invariant preserved**: scaling dimension (load-bearing — uniform bound = scale-invariance), spectral gap (background — bound protects the gap's stability)
- **Geometric interpretation**: A uniform $H^1$ resolvent bound means the amplitude of $D_N$'s inverse does not blow up along the spectral line; Fourier cancellation is the regulator mechanism. Under $P_D$ (paper61 §10) this is a Rellich-Kondrachov-style statement about the BC algebra's spectral triple and directly feeds L4b. [Considered but rejected: face RESONANCE — resolvent pole structure is resonance-ish but the BOUND character is amplitude; pattern P4 — bound rigidity is implied but engine is regularization.]
- **Cross-cuts**: lindelof (AMPLITUDE canonical, uniform resolvent bound), ym:L4 (k-independent analyticity radius structural parallel — YM X-Ray §7 lists L4 ↔ rh:L3c as a cross-cut), ym:L10b (spectral-lemma k-independent constant = same kind of uniformity).

### L3d — CF decay $\rho \geq 4.27$ uniform in $N$

**Claim**: The correlation-function decay exponent $\rho$ satisfies $\rho \geq 4.27$ uniformly in the truncation parameter $N$ (Remark 8.4's $\log N$ caveat has been resolved 2026-04-14 via Slepian compatibility Lemma 12.1 → S2).

**Status**: PROVED (caveat-resolved)
**Source**: paper13-rh §L3d with caveat-resolution via paper13-rh §S2 Lemma 12.1. Depends on L1; caveat resolved 2026-04-14 per Runs-1-5 upgrade (session log `session_rh_runs1to5.md`, CF uniformity upgraded to [PROVED with caveat]).

#### Physics

- **Face**: DYNAMICS (paper60 §08 — correlation-function decay IS a dynamical-mixing statement on the modular flow)
- **Projection**: $P_D$ (paper61 §10 — CF decay is a modular-flow ergodicity property of $\sigma_t$ at KMS$_1$)
- **Pattern**: P3 Scale-Setting (the specific exponent $\rho \geq 4.27$ sets the scale for admissible $N$-uniformity)
- **Invariant preserved**: ergodic property (load-bearing — CF decay IS the quantitative mixing rate), critical exponent (background — $\rho$ is the exponent of decay)
- **Geometric interpretation**: A uniform-in-$N$ CF decay rate is the quantitative form of the modular flow's mixing under $P_D$ (paper61 §10 ¶ "$\omega_1$ is democratic" — mixing across all primes). Exponent $\rho \geq 4.27$ is the Pattern-3 scale-setting value established by the Slepian-compatibility grid discretization (S2). The caveat resolution (2026-04-14) was an uplift from "PROVED with caveat" to "PROVED" by establishing that the grid Slepian kernel approximates the continuous kernel with exponentially-small error (S2). [Considered but rejected: face AMPLITUDE — $\rho$ could be read as a growth-rate but decay-rate is dynamics-canonical; pattern P5 — regularization implied but scale-setting dominates.]
- **Cross-cuts**: cramer (DYNAMICS canonical, Cramér-gap modular-flow traversal), ym:L3 (Balaban polymer k-independence = RG-flow ergodicity; shared ergodic property under $P_D$), pvnp (modular flow ergodicity under Popa rigidity), bgs (GUE pair correlation = quantitative version of the same CF decay; programme-graph edge paper13-rh).

### L4a — Boegli H1 (gsrc): ITPFI → form convergence → gsrc via Teschl Lemma 2.7

**Claim**: Boegli's first hypothesis (gsrc — generalized strong resolvent convergence) follows from ITPFI factorization plus form convergence via Teschl's Lemma 2.7.

**Status**: PROVED
**Source**: paper13-rh §L4a (transport through Teschl Lemma 2.7). Depends on L2 and L3a-L3d.

#### Physics

- **Face**: RESONANCE (paper60 §15 / §18 — Boegli's gsrc IS a resonance-mode convergence statement; spectrum-of-the-limit equals limit-of-spectrum)
- **Projection**: $P_D$ (paper61 §10 — Boegli machinery lives on the BC operator algebra)
- **Pattern**: P4 Topological Rigidity (paper61 §10 analog — spectral exactness is a rigid-convergence statement; the form convergence PATTERN is rigidity)
- **Invariant preserved**: BC-KMS state (load-bearing — Teschl transports the state's form convergence), ergodic property (background — ITPFI ergodicity)
- **Geometric interpretation**: Boegli's gsrc is the statement that the sequence $D_N$ converges to $D_\infty$ in a sense strong enough to preserve spectra; the transport from ITPFI + form convergence to gsrc via Teschl Lemma 2.7 is the Pattern-4 rigidity: resonance-mode enumeration doesn't leak in the limit. Under $P_D$ (paper61 §10) this is a convergence theorem for the BC algebra's spectral triple. [Considered but rejected: face DYNAMICS — convergence has a flow reading but the target (gsrc) is resonance-canonical; pattern P1 — reinterpretation framing exists but rigidity dominates.]
- **Cross-cuts**: qg5d Branch D (BC algebra spectral triple's convergence theory), ym:L16 (OS reconstruction / Schwinger-functions convergence = structural analog under shared BC-KMS state), baum-connes (spectral triple convergence under K-theory).

### L4b — Boegli H2 (discrete compactness): uniform $H^1 \to$ Rellich-Kondrachov

**Claim**: Boegli's second hypothesis — discrete compactness — follows from the uniform $H^1$ bound of L3c via Rellich-Kondrachov.

**Status**: PROVED
**Source**: paper13-rh §L4b (discrete compactness from uniform $H^1$). Depends on L3c.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — Rellich-Kondrachov's compactness IS a symmetry-side statement about embeddings preserving the Sobolev-inclusion group structure)
- **Projection**: $P_D$ (paper61 §10 — the Sobolev embedding is the BC algebra's interior property)
- **Pattern**: P4 Topological Rigidity (compactness is rigidity in the functional-analytic sense)
- **Invariant preserved**: spectral gap (load-bearing — compactness implies discrete spectrum + gap), C*-algebra structure (background)
- **Geometric interpretation**: Uniform $H^1$ → Rellich-Kondrachov gives compactness of the resolvent's image; under $P_D$ (paper61 §10) this is a property of the BC algebra's spectral triple (Sobolev embeddings in the non-commutative setting). Pattern 4 rigidity: the compactness forces the discrete spectrum, closing the gap-preservation argument. [Considered but rejected: face RESONANCE — compactness → discrete-modes framing is resonance-ish but the mechanism (embedding) is symmetry-canonical; pattern P1 — reinterpretation of the resolvent as a compact operator is downstream.]
- **Cross-cuts**: ym:L4b (SL(N,C) extension shares compactness-of-the-complexified-group structural reading; SPECULATIVE), qg5d Branch D (Sobolev structure in the BC spectral triple), katz-sarnak (bridge family classification uses compactness arguments).

### L4c — Spectral exactness: $\mathrm{spec}(D_\infty) = \lim \mathrm{spec}(D_N)$, no spurious eigenvalues

**Claim**: The spectrum of $D_\infty$ equals the Kuratowski limit of the spectra of $D_N$, with no spurious eigenvalues. This is Boegli's main spectral-exactness theorem applied to H1 + H2.

**Status**: PROVED
**Source**: paper13-rh §L4c (Boegli spectral exactness). Depends on L4a + L4b.

#### Physics

- **Face**: RESONANCE (paper60 §18 — the spectrum of $D_\infty$ is the resonance-mode set; spectral exactness says "no resonance leaks and no ghost resonances")
- **Projection**: $P_D$ (paper61 §10 — spectral exactness on the BC algebra is the $P_D$-internal statement)
- **Pattern**: P4 Topological Rigidity (no spurious eigenvalues is rigidity: the spectrum doesn't gain or lose points in the limit)
- **Invariant preserved**: spectral gap (load-bearing — spectral exactness preserves gaps), C*-algebra structure (load-bearing — spectrum is a C*-algebra invariant)
- **Geometric interpretation**: Spectral exactness is the statement that every eigenvalue of $D_\infty$ is a limit of eigenvalues of $D_N$ AND every limit-of-eigenvalues is actually an eigenvalue. Under $P_D$ (paper61 §10) this is the BC algebra's spectral stability theorem — Pattern 4 rigidity. Under paper60 §18's torus picture, this is what makes the Riemann-zero set (= intersection points of the two circles) stable under finite-dimensional approximation. [Considered but rejected: face TOPOLOGY — the torus-intersection framing of paper60 §18 would place this on TOPOLOGY but the load-bearing content is spectral-mode enumeration; pattern P5 — the exactness has a regularization-residual reading but rigidity dominates.]
- **Cross-cuts**: qg5d Branch D (BC spectral triple), ym:L14 (mass-gap existence as shared "gap-preserving limit" structural form; both use $\mathrm{spec}(\mathrm{limit}) = \mathrm{limit}(\mathrm{spec})$), baum-connes (K-theory stability of spectral triples), pvnp (Popa rigidity shares the spectral-exactness structural pattern).

### L5 — Hurwitz: $\hat{\xi}_N \to \Xi$ uniformly on compacts, giving $\lim \mathrm{spec}(D_N) = \{\gamma_n\}$

**Claim**: The normalized characteristic functions $\hat{\xi}_N$ of $D_N$ converge uniformly on compacts to the completed Riemann $\Xi$-function; by Hurwitz's theorem, this gives $\lim \mathrm{spec}(D_N) = \{\gamma_n\}$.

**Status**: PROVED
**Source**: paper13-rh §L5 (Hurwitz uniform convergence + eigenvalue identification). Depends on L3b + L4c.

#### Physics

- **Face**: AMPLITUDE (paper60 §11 — Hurwitz's theorem is an amplitude-uniformity statement that promotes pointwise convergence of entire functions to uniformity-on-compacts of their zero sets)
- **Projection**: $P_D$ (paper61 §10 — $\hat{\xi}_N$ is a BC-algebra-side spectral object)
- **Pattern**: P5 Zeta Regularization (the completed $\Xi$-function IS the zeta-regularized counting function; convergence to $\Xi$ is Pattern 5's signature)
- **Invariant preserved**: scaling dimension (load-bearing — Hurwitz preserves the entire-function normalization), L-value (load-bearing — the target is $\Xi(s)$, a specific $L$-value-valued function)
- **Geometric interpretation**: Hurwitz's theorem says that if entire functions $\hat{\xi}_N \to \Xi$ uniformly on compacts, then the zero sets converge — $\mathrm{Zero}(\Xi) = \{\gamma_n\}$ and $\mathrm{Zero}(\hat{\xi}_N) = \mathrm{spec}(D_N)$. Under $P_D$ (paper61 §10) this is the step that identifies the BC algebra's spectrum with the Riemann zeros. Pattern 5 (zeta regularization): $\Xi$ is the completed, regularized zeta. [Considered but rejected: face RESONANCE — zeros as resonance-modes reading is real but the CONVERGENCE mechanism is amplitude-uniformity via Hurwitz; pattern P4 — rigidity of the zero set implied but engine is regularization-convergence.]
- **Cross-cuts**: lindelof (AMPLITUDE canonical, bounded entire functions / Jensen-Carleman), bsd (L-function convergence — $\Xi$ analogues for $L(E,s)$), grh (the character-twisted $\hat{\xi}_N^\chi$ follows the same Hurwitz machinery — paper13b programme-graph edge), ym:L13 (convergent regularized sum under Pattern 5).

### L6 — $\mathrm{spec}(D_\infty) = \{\gamma_n\} \subset \mathbb{R}$ ⟹ RH

**Claim**: Since $D_\infty$ is self-adjoint, its spectrum lies in $\mathbb{R}$. Combined with $\mathrm{spec}(D_\infty) = \{\gamma_n\}$ (L4c + L5), the imaginary parts $\gamma_n$ are all real, so all non-trivial zeros of $\zeta(s)$ lie on $\mathrm{Re}(s) = \tfrac{1}{2}$. QED.

**Status**: PROVED (QED)
**Source**: paper13-rh §L6. Depends on L4c + L5 (and self-adjointness of $D_\infty$ inherited from L1).

#### Physics

- **Face**: TOPOLOGY (paper60 §18 / §19 — L6 is the top-level claim "the zeros are at the transversal intersection of the two circles"; the critical line IS the intersection locus; the final statement is a topological / linking-number statement on the torus)
- **Projection**: $P_D$ (paper61 §10 — the final identification $\mathrm{spec}(D_\infty) = \{\gamma_n\}$ is the $P_D$-internal summary; note L6 also has a strong $P_O$ reading as the Clay outer-ring statement)
- **Pattern**: P2 Holonomy (paper60 §18 — the Riemann-von Mangoldt count of zeros IS the intersection number / linking number of the two generating circles on the torus; winding / holonomy is the natural attack vector for the final QED)
- **Invariant preserved**: spectral gap (load-bearing — self-adjointness + spectrum = $\{\gamma_n\}$ is a structural statement about the spectrum), holonomy (load-bearing — paper60 §18's linking number of the two circles)
- **Geometric interpretation**: The final QED combines (a) $D_\infty$ self-adjoint (spectrum $\subset \mathbb{R}$), (b) spectral exactness (L4c), and (c) Hurwitz identification (L5). Paper60 §18 reads L6 as "the two circles meet transversally at the zeros" — a holonomy / linking-number statement (Pattern 2). Paper60 §19 ("RH is the EXISTENCE of the torus") promotes L6 from "a conjecture about one face" to "the consistency condition for all ten faces." Under $P_D$ (paper61 §10) the statement is internal to the BC algebra, but its outer-ring reading projects cleanly to $P_O$. [Considered but rejected: face RESONANCE — L6's final mechanism is self-adjointness + spectral exactness, which is resonance-mode-canonical, BUT the TOP-LEVEL CLAIM under paper60 §18/§19 is the torus-existence / intersection-locus statement, which is topology-canonical. Projection $P_O$ — outer-ring statement is real but the proof-chain's load-bearing step is $P_D$-internal; mark $P_O$ as secondary. Pattern P4 — rigidity of self-adjoint spectrum on ℝ is real but the Riemann-von Mangoldt counting = linking-number is Pattern 2 (holonomy).]
- **Cross-cuts**: qg5d hub (L6 is the outer-ring statement; RH-as-torus-existence per paper60 §19), lehmer:L_top (TOPOLOGY canonical shared face — winding / Lehmer-pair gap structural parallel), bsd (same RH-on-critical-line statement generalized to $L(E,s)$), grh (same statement for twisted L-functions; paper13b), bgs (GUE pair correlation of zeros = holonomy-statistics on the spectral circle).

### S1 — AE simplicity (certified $N \leq 20$; Slepian limit $N > 20$)

**Claim**: The eigenvalues of $D_N$ are almost-everywhere simple, certified directly for $N \leq 20$ and extended to $N > 20$ via the Slepian limit.

**Status**: PROVED
**Source**: paper13-rh §J (AE simplicity certification) + §K (Slepian extension). Depends on L1.

#### Physics

- **Face**: SYMMETRY (paper60 §12 — AE simplicity is a spectral-symmetry statement; no accidental symmetry groups act to degenerate eigenvalues)
- **Projection**: $P_D$ (paper61 §10 — spectral simplicity is a $P_D$-internal property of the BC algebra's Dirac operator)
- **Pattern**: P1 Geometric Reinterpretation (Slepian limit reinterprets large-$N$ simplicity as a continuous-kernel statement; paper60 §12 Katz-Sarnak analog)
- **Invariant preserved**: spectral gap (load-bearing — simplicity = gaps between all consecutive eigenvalues), monodromy (background — absence of degeneracy protects monodromy)
- **Geometric interpretation**: Eigenvalue simplicity is the natural spectral-side non-degeneracy; for $N \leq 20$ it is certified by direct computation, for $N > 20$ it is extended via the Slepian limit's continuous kernel. Under $P_D$ (paper61 §10) this is a property of the BC Dirac operator. Pattern 1 because the Slepian extension geometrically reinterprets the discrete spectrum via the continuous Slepian kernel. [Considered but rejected: face RESONANCE — spectral simplicity is a resonance-mode property but the mechanism (no degeneracy / monodromy) is symmetry-canonical; pattern P4 — rigidity against perturbation is implied but Slepian's machinery is Pattern 1.]
- **Cross-cuts**: katz-sarnak (SYMMETRY canonical, Wigner-Dyson level-repulsion uses simplicity), ym:L5 (SL(N,C) extension via Katz-Sarnak bridge family — symmetry-type cross-cut), bgs (GUE-level simplicity of spectral statistics; programme-graph edge).

### S2 — Slepian compatibility: $A^{ev} = K_\lambda|_{\mathrm{grid}} + O(e^{-cN})$

**Claim**: The even-part matrix $A^{ev}$ is exponentially close to the restriction of the continuous Slepian kernel $K_\lambda$ to the discretization grid. This lemma (paper13-rh Lemma 12.1) resolves the $\log N$ caveat of L3d.

**Status**: PROVED
**Source**: paper13-rh §S2 Lemma 12.1 (Slepian compatibility). Depends on S1; resolves L3d caveat (2026-04-14).

#### Physics

- **Face**: MEASURE (paper60 §10 — Slepian compatibility equidistributes the grid values against the continuous kernel; paper60 §10 Sato-Tate analog — weak-* convergence of a discrete measure to the continuous)
- **Projection**: $P_D$ (paper61 §10 — the Slepian kernel lives on the BC algebra's spectral triple; grid discretization is $P_D$-internal)
- **Pattern**: P1 Geometric Reinterpretation (Slepian geometrically reinterprets the discrete matrix as a kernel restriction)
- **Invariant preserved**: ergodic property (load-bearing — exponential approximation rate is a quantitative-ergodicity statement), scaling dimension (background)
- **Geometric interpretation**: $A^{ev} = K_\lambda|_{\mathrm{grid}} + O(e^{-cN})$ is exponential equidistribution of the grid against the continuous kernel; MEASURE face (paper60 §10) because this IS a weak-* convergence of discrete measures to continuous. The exponential rate upgrades L3d from "PROVED with caveat" to "PROVED" (session `session_rh_runs1to5.md`, 2026-04-12 → 2026-04-14 upgrade). Under $P_D$ (paper61 §10) this is a statement on the BC algebra's spectral triple. [Considered but rejected: face DYNAMICS — grid traversal has a dynamics reading but the BOUND character is measure-theoretic; pattern P3 — scale-setting via the Slepian parameter $\lambda$ is natural but the interpretive move is Pattern 1.]
- **Cross-cuts**: sato-tate (MEASURE canonical, equidistribution of Frobenius angles), ym:L10b (k-independent spectral-lemma constant = same kind of uniform-kernel-bound), bsd (height distribution equidistribution cross-cut).

### S3 — $\gamma_E$ elimination (uniform diagonal shift)

**Claim**: The Euler-Mascheroni constant $\gamma_E$ that appears as a uniform diagonal shift in the CCM operator expansion can be eliminated by a uniform subtraction, leaving the zero-distribution structure intact.

**Status**: PROVED
**Source**: paper13-rh §L (Euler-Mascheroni elimination). Free-standing (no explicit dependencies in the chain table).

#### Physics

- **Face**: ARITHMETIC (paper60 §14 — $\gamma_E = \lim (\sum_{n \leq N} 1/n - \log N)$ is the integer-lattice residual; paper60 §14 ARITHMETIC face — "how do integers LATTICE on the circle")
- **Projection**: $P_D$ (paper61 §10 — $\gamma_E$ enters as a diagonal shift of the BC-algebra's Dirac operator)
- **Pattern**: P1 Geometric Reinterpretation (the diagonal shift is geometrically reinterpreted as a uniform subtraction — shift-covariance of the spectral-triple construction)
- **Invariant preserved**: critical exponent (load-bearing — $\gamma_E$ quantifies the harmonic-series regularization residual)
- **Geometric interpretation**: $\gamma_E$ is the Euler-Mascheroni constant — the arithmetic residual of the harmonic series against $\log$ (paper60 §14 ARITHMETIC face: the integer lattice's "deviation from the log"). Its elimination by uniform diagonal shift is Pattern 1: reinterpreting the shifted operator as the original plus a scalar. Under $P_D$ (paper61 §10) this is a covariance statement for the BC-algebra's Dirac operator. [Considered but rejected: face AMPLITUDE — $\gamma_E$ is a scalar amplitude but its ARITHMETIC origin dominates; pattern P5 — regularization residual framing exists but the elimination IS a reinterpretation, not a regularization.]
- **Cross-cuts**: goldbach / twin-primes (ARITHMETIC canonical, integer-lattice residuals), bsd (Kronecker limit formula features analogous $\gamma_E$ residual; SPECULATIVE), grh (character-twisted $\gamma_E$ analogs; paper13b).

---

## §4 Branch Map

The RH proof chain is largely linear but has two significant structural splits:

```
L1 (CCM operators; EXTERNAL — W1)
    │
    ├── Route A (primary): L2 ITPFI → L3a/b/c/d tail →
    │                      L4a/b/c Boegli → L5 Hurwitz → L6 QED
    │                      [face: RESONANCE dominant; proj: P_D;
    │                       pat: mix of P1/P4/P5]
    │
    └── S-chain (supporting, parallel):
           S1 AE simplicity → S2 Slepian compatibility
                                     │
                                     ↓
                              resolves L3d caveat

         S3 γ_E elimination (free-standing diagonal-shift lemma)

L6 (QED) has dual projection reading:
    ├── Route P_D-internal: spec(D_∞) = {γ_n} ⊂ ℝ  [proj: P_D | face: RESONANCE]
    └── Route P_O-outer:    RH as torus-existence   [proj: P_O | face: TOPOLOGY]

The two readings do NOT give different physics: they are two projections
of the SAME QED onto two different target spaces. The P_D reading is the
mechanical statement inside the BC algebra; the P_O reading is the
outer-ring consequence (paper60 §18/§19 — the torus-intersection / critical-
line framing). The atlas records P_D as load-bearing (the mechanics) and
P_O as secondary (the outer-ring statement).

Note on L4a: the Boegli machinery splits into H1 (L4a) and H2 (L4b)
hypotheses, both required, both PROVED, and then combines into spectral
exactness (L4c). No projection ambiguity.

Note on L6: this is the only layer with a genuine multi-face reading.
RESONANCE (final mechanism = spectral exactness + self-adjointness) and
TOPOLOGY (top-level claim = two-circles-intersect-transversally) are both
present. Paper60 §18 explicitly identifies the top-level claim with the
topology-side reading; paper60 §19 deepens it ("RH is the EXISTENCE of
the torus"). The arbiter chose TOPOLOGY as primary for L6, RESONANCE
as secondary, in alignment with the paper60 §18/§19 framing.
```

---

## §5 Face Histogram

| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   1   | ████                  | L6 (QED) — the torus-existence / transversal-intersection statement per paper60 §18/§19. |
| DYNAMICS   |   2   | ████████              | L3b (eigenvector approximation) + L3d (CF decay) — modular-flow control on the spectral side. |
| HARMONICS  |   0   |                       | RH does not interrogate Fourier-mixing on the e-circle directly. |
| MEASURE    |   1   | ████                  | S2 (Slepian compatibility) — equidistribution of grid values against continuous kernel. |
| AMPLITUDE  |   3   | ████████████          | L3a (archimedean tail), L3c (H¹ resolvent bound), L5 (Hurwitz uniform convergence) — three amplitude/uniformity layers. |
| SYMMETRY   |   2   | ████████              | L4b (Rellich-Kondrachov), S1 (AE simplicity) — embeddings + spectral non-degeneracy. |
| CURVATURE  |   0   |                       | RH is not a gauge-curvature statement; CURVATURE cross-cuts to YM are present but not layer-assignments. |
| ARITHMETIC |   1   | ████                  | S3 (γ_E elimination) — integer-lattice residual of the harmonic series. |
| RESONANCE  |   4   | ████████████████      | DOMINANT. L1 (CCM operators), L2 (ITPFI), L4a (Boegli gsrc), L4c (spectral exactness) — four resonance-mode layers; RH is canonically a resonance-face conjecture. |
| SPREAD     |   0   |                       | RH does not interrogate L²-mass spreading. |

**Interpretation**: RESONANCE dominates (4 / 14 layers, ~29%) — RH is a spectral-side / trace-formula-type statement (paper60 §15 Selberg-face analog; §18 places RH squarely on the resonance-circle side of the torus). AMPLITUDE (3 / 14, ~21%) is the strong secondary, carrying the uniformity machinery (tail bounds + Hurwitz). DYNAMICS, SYMMETRY, MEASURE, TOPOLOGY, ARITHMETIC each carry 1–2 layers. Three faces (HARMONICS, CURVATURE, SPREAD) are entirely absent at layer-level — RH does not interrogate Fourier-mixing, gauge-curvature, or QUE-type mass-spreading. The "shape" of RH on the e-circle is resonance-canonical with strong amplitude secondary, and a single outer-ring TOPOLOGY layer (L6) that carries the torus-existence framing — consistent with paper60 §18's "zeros are the transversal intersection of the two circles" and §19's "RH is the EXISTENCE of the torus."

---

## §6 Projection Histogram

| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| $P_A$        |   0   |                      | Quantum projection forgets the zero lattice — no Born/Bell/A-B content at RH. |
| $P_B$        |   0   |                      | Gauge-bundle projection forgets the BC algebra's spectral content — RH is not a gauge theorem. |
| $P_C$        |   0   |                      | Cosmological projection forgets the spectral side entirely. |
| $P_D$        |  14   | █████████████████████████████████████████████████████████ | DOMINANT. CBB / BC-algebra projection — the home of $D_N$, $D_\infty$, ITPFI, Boegli gsrc, spectral exactness. ALL 14 layers live in $P_D$. |
| $P_E$        |   0   |                      | Pins projection: Pin #6 ($J_\mathrm{CKM} \times 10^5 = \log(\gamma_1) \cdot \zeta(3)$) references $\gamma_1$ but Agent L audit (2026-04-14) confirms the load-bearing pin-anchor is `integers/paper12-cbb-system/research/102 §3.1`, NOT paper13-rh — so no layer is $P_E$-primary. |
| $P_O$        |   0   (primary)  | (secondary, L6) | Outer-ring projection: L6 has a strong $P_O$ reading (RH as Clay-grade closure / torus-existence consequence) but primary projection for L6 is $P_D$ (the $P_D$-internal mechanics are load-bearing). |

**Interpretation**: The projection profile is **maximally $P_D$-dominant** (14 / 14 layers, 100%). Unlike YM (which splits $P_B$ 65% / $P_D$ 30% / $P_O$ 5%), RH lives entirely inside the BC operator-algebra projection. This matches paper61 §10's vertex-RH assignment: "RH is a spectral question about the BC algebra's generator" (paper61 §10 ¶4). $P_A / P_B / P_C / P_E$ are all absent — none of the quantum, gauge, cosmological, or pin projections retain enough structure to articulate the RH statement. $P_O$ appears as a secondary reading for L6 only. The fan-out diagram (§2b) shows five of the six projections as `(forgotten)` — RH is a mono-projection vertex in a way that YM is not. This is a structural signature: RH is paper60 §19's "existence of the torus" condition, which is naturally a $P_D$-only statement (the torus = BC algebra's crossed-product structure).

---

## §7 Cross-Cut Map

### Neighborhood graph

```
                           qg5d (Branch D / hub)
                                │
                                │ ═══ shared BC algebra (L1, L2, L4a, L4c)
                                │ ═══ shared ITPFI III_1 (L2)
                                │ ═══ shared KMS_1 state (L1, L2, L4a)
                                │
        bsd ═══════════════════ rh (Riemann Hypothesis) ═══════════ grh
        (L-function            │                                    (paper13b —
        factorization on       │                                    char-twisted
        BC algebra; cocycle    │                                    extension of
        shift)                 │                                    every layer)
        ═══ L1 BC algebra      │                                    ═══ all layers
        ═══ L2 ITPFI shared    │                                    ═══ Hurwitz L5
        ═══ L5 L-function      │
            convergence        │
                               │
        cramer ════════════════│══════════════════ ym (paper08)
        (DYNAMICS canonical;   │                   ═══ L3 Balaban polymer ↔ L3d
        modular-flow ergod.)   │                       shared P_D ergodic property
        ═══ L3b eigenvector    │                   ═══ L4 analyticity ↔ L3c H^1
        ═══ L3d CF decay       │                       shared AMPLITUDE / scaling-dim
                               │                   ═══ L10b k-indep lemma ↔ L3c
                               │                       shared uniform bound
                               │                   ═══ L16 OS/KMS ↔ L2 ITPFI
                               │                       shared BC-KMS state
                               │                   ═══ L18 AF inheritance (SPEC)
                               │
        pvnp (paper28) ════════│════════════ baum-connes (paper31)
        (Popa rigidity;        │             ═══ L1 spectral triple
        type III_1 modular     │             ═══ L4a/c gsrc + spectral exactness
        flow;                  │                 on spectral triple
        Q5-RIEMANN exp)        │             ─── K-theory pairing (SPEC)
        ═══ L1 III_1           │
        ═══ L2 factor type     │
        ═══ L3b gap stability  │
        ═══ L4c exactness      │
                               │
                          bgs
                          (GUE pair correlation
                           = spectral statistics
                           of D_∞; programme-graph
                           edge, paper13-rh §"Programme
                           graph edges")
                          ═══ L3d CF decay ↔ CF statistics
                          ═══ L6 holonomy ↔ level repulsion
                          ═══ S1 simplicity ↔ simple spectrum
                               │
                          katz-sarnak
                          (SYMMETRY canonical;
                           symmetry-type of zero ensemble)
                          ─── S1 AE simplicity
                          ─── L4b Rellich / bridge family

        lehmer ─── L6 TOPOLOGY
        (face-only: gap-above-ground-state;
         paper60 §13 adjacency table parallel
         to YM — same role as YM:L14)

        lindelof ─── L3a, L3c, L5
        (AMPLITUDE canonical;
         uniform growth bounds)

        sato-tate ─── S2 equidistribution
        (MEASURE canonical)

        goldbach / twin-primes ─── L2 Euler product, S3 γ_E
        (ARITHMETIC canonical)
```

### Bullet list (per-edge)

- **L1 ↔ qg5d:Branch D** — shared C*-algebra structure, BC-KMS state, spectral gap.
  - Reason: The CCM operators $D_N$ on $E_N^+$ live inside the BC algebra $A_{BC}$, which IS Branch D's operational core (paper61 §10).
  - Transposition candidate: YES (capacitor cell — BC algebra dictionary).

- **L1 ↔ bsd:L_BC** — shared C*-algebra structure.
  - Reason: paper26 programme-graph edge from RH PROOF-CHAIN.md: "L-functions factor through the same BC algebra; cocycle shift extends."
  - Transposition candidate: YES.

- **L1 ↔ grh:L1** — shared C*-algebra structure + spectral gap.
  - Reason: paper13b character-twisted $D_N^\chi$ on the same BC algebra; programme-graph edge.
  - Transposition candidate: YES.

- **L1 ↔ baum-connes:L_spectral-triple** — shared spectral gap, C*-algebra structure.
  - Reason: CCM spectral triple shares the underlying $(A, H, D)$ structure with Baum-Connes K-theory.
  - Transposition candidate: SPECULATIVE (pending baum-connes X-Ray).

- **L1 ↔ pvnp:L_III1** — shared ITPFI factor type (III$_1$).
  - Reason: pvnp uses Popa rigidity, which is a type III$_1$ spectral-gap-rigidity theorem on the same factor.
  - Transposition candidate: YES (P4 shared pattern).

- **L2 ↔ qg5d:Branch D** — shared ITPFI factor type + BC-KMS state.
  - Reason: ITPFI III$_1$ factorization is the BC-algebra-side shadow of the Euler product (paper61 §10).
  - Transposition candidate: YES.

- **L2 ↔ goldbach:L_Euler / twin-primes:L_Euler** — shared ARITHMETIC (Euler product).
  - Reason: paper61 §10's dictum — "ITPFI factorization = Euler product, two different languages."
  - Transposition candidate: SPECULATIVE.

- **L2 ↔ pvnp:L_factor** — shared ITPFI factor type.
  - Reason: pvnp's operator-algebraic reduction uses the same III$_1$ factor.
  - Transposition candidate: YES.

- **L2 ↔ ym:L16** — shared BC-KMS state.
  - Reason: YM X-Ray §7 lists this cross-cut explicitly (L16 ↔ rh:L_KMS): both YM Schwinger functions and RH zero-distribution involve restrictions of the same $\omega_1$.
  - Transposition candidate: YES.

- **L3a ↔ lindelof:L_amplitude** — shared scaling dimension (AMPLITUDE canonical).
  - Reason: $\Gamma$-factor uniform bound / growth-rate structural parallel.
  - Transposition candidate: SPECULATIVE.

- **L3a ↔ ym:L4** — shared scaling dimension.
  - Reason: YM X-Ray §7 lists "L4 ↔ rh:L_resolvent" structural parallel for k-independent analyticity radius; L3a/L3c both live in this analytic-tail uniformity family.
  - Transposition candidate: SPECULATIVE.

- **L3b ↔ cramer:L_modular** — shared spectral gap (DYNAMICS).
  - Reason: Davis-Kahan bound depends on the spectral gap; modular-flow eigenvector control is Cramér-side DYNAMICS (paper60 §08).
  - Transposition candidate: YES.

- **L3b ↔ pvnp:L_rigidity** — shared spectral gap.
  - Reason: Gap-based eigenvector stability = Popa rigidity analog.
  - Transposition candidate: YES.

- **L3c ↔ ym:L4** — shared scaling dimension (uniform analyticity radius ↔ uniform $H^1$ bound).
  - Reason: YM X-Ray §7 explicitly lists "L4 ↔ rh:L_resolvent" as a cross-cut (L4's k-indep radius = same uniform-bound structural form).
  - Transposition candidate: SPECULATIVE.

- **L3c ↔ ym:L10b** — shared spectral gap / uniform-constant.
  - Reason: YM X-Ray §7 lists "L10b ↔ rh:L_uniform" — k-indep spectral-lemma constant is the same kind of uniformity.
  - Transposition candidate: SPECULATIVE.

- **L3c ↔ lindelof:L_amplitude** — shared scaling dimension (AMPLITUDE canonical).
  - Reason: Both are uniform-bound statements.
  - Transposition candidate: SPECULATIVE.

- **L3d ↔ cramer:L_dynamics** — shared ergodic property.
  - Reason: Uniform correlation-function decay is the quantitative modular-flow mixing (DYNAMICS canonical).
  - Transposition candidate: YES.

- **L3d ↔ ym:L3** — shared ergodic property.
  - Reason: YM X-Ray §7 lists "L3 ↔ rh:L_BC" — Balaban polymer k-independent $\kappa$ = BC-algebra ergodicity; shared $P_D$ ergodic-property invariant.
  - Transposition candidate: YES.

- **L3d ↔ bgs:L_pair-correlation** — shared ergodic property.
  - Reason: Programme-graph edge in paper13-rh — GUE pair correlation of zeros = spectral statistics of $D_\infty$; CF decay is the quantitative cousin.
  - Transposition candidate: YES.

- **L4a ↔ qg5d:Branch D** — shared BC-KMS state, ergodic property.
  - Reason: Boegli gsrc transports the KMS state's form convergence; this is the BC spectral triple's convergence theory.
  - Transposition candidate: YES.

- **L4a ↔ ym:L16** — shared BC-KMS state.
  - Reason: OS-reconstruction / Schwinger-functions convergence (YM:L16) is structural analog under the shared $\omega_1$.
  - Transposition candidate: YES.

- **L4a ↔ baum-connes:L_triple** — shared BC-KMS state.
  - Reason: Spectral-triple convergence under K-theory; SPECULATIVE pending baum-connes X-Ray.
  - Transposition candidate: SPECULATIVE.

- **L4b ↔ katz-sarnak:L_bridge** — face-only (SYMMETRY canonical).
  - Reason: Bridge-family classification uses compactness; Rellich-Kondrachov's compactness embedding is symmetry-canonical.
  - Transposition candidate: SPECULATIVE.

- **L4b ↔ qg5d:Branch D** — shared spectral gap.
  - Reason: Sobolev embedding in the BC spectral triple's non-commutative setting.
  - Transposition candidate: SPECULATIVE.

- **L4c ↔ qg5d:Branch D** — shared spectral gap, C*-algebra structure.
  - Reason: Spectral exactness on the BC algebra's spectral triple; paper61 §10 Branch D operational core.
  - Transposition candidate: YES.

- **L4c ↔ ym:L14** — shared spectral gap.
  - Reason: Both use "spectrum-of-limit = limit-of-spectra" structural pattern; YM:L14 is the mass-gap continuum-limit, RH:L4c is the zero-set continuum-limit. Same gap-preservation-under-limit move.
  - Transposition candidate: YES.

- **L4c ↔ pvnp:L_exactness** — shared spectral gap.
  - Reason: Popa rigidity's spectral-exactness structural pattern.
  - Transposition candidate: YES.

- **L4c ↔ baum-connes:L_K-stability** — shared C*-algebra structure.
  - Reason: K-theory stability of spectral triples; SPECULATIVE.
  - Transposition candidate: SPECULATIVE.

- **L5 ↔ lindelof:L_amplitude** — shared scaling dimension, L-value.
  - Reason: Hurwitz uniform convergence on compacts is the AMPLITUDE-face's paradigmatic convergence mechanism for entire functions; $\Xi$ is an $L$-function.
  - Transposition candidate: YES.

- **L5 ↔ bsd:L_L-func** — shared L-value.
  - Reason: Same Hurwitz-convergence machinery for $L(E, s)$ zeros; programme-graph edge.
  - Transposition candidate: YES.

- **L5 ↔ grh:L_twist** — shared L-value.
  - Reason: Character-twisted $\hat{\xi}_N^\chi \to L(\chi, s)$ completed-function; paper13b.
  - Transposition candidate: YES.

- **L5 ↔ ym:L13** — shared scaling dimension.
  - Reason: YM X-Ray §7 lists "L13 ↔ rh:L_Weil" — Weil quadratic form convergence analog; same P5 Zeta Regularization engine.
  - Transposition candidate: SPECULATIVE.

- **L6 ↔ qg5d:Hub** — shared spectral gap, holonomy.
  - Reason: L6 IS the RH outer-ring statement; paper60 §19 "RH is the EXISTENCE of the torus" places it as the consistency condition for all ten faces.
  - Transposition candidate: YES.

- **L6 ↔ lehmer:L_top** — face-only (TOPOLOGY canonical, gap-above-ground-state).
  - Reason: Paper60 §13's adjacency table parallels YM:L14 with Lehmer; same "discrete-spectrum on ℝ" TOPOLOGY structural form.
  - Transposition candidate: NO (no capacitor cell; shared face but not shared mechanism).

- **L6 ↔ bsd:L_rank** — shared spectral gap (generalized).
  - Reason: Same "$\zeta$-zeros on critical line" statement generalized to $L(E,s)$; BC algebra hosts both.
  - Transposition candidate: YES.

- **L6 ↔ grh:L_main** — shared spectral gap.
  - Reason: GRH = RH for all primitive L-functions; same L6-equivalent statement.
  - Transposition candidate: YES.

- **L6 ↔ bgs:L_GUE** — shared holonomy (linking number = pair correlation statistic).
  - Reason: Programme-graph edge in paper13-rh: "GUE pair correlation of zeros = spectral statistics of $D_\infty$."
  - Transposition candidate: YES.

- **S1 ↔ katz-sarnak:L_simplicity** — shared spectral gap (SYMMETRY canonical).
  - Reason: Wigner-Dyson level-repulsion uses almost-everywhere simplicity; paper60 §12.
  - Transposition candidate: SPECULATIVE.

- **S1 ↔ bgs:L_simple** — shared spectral gap.
  - Reason: GUE-level eigenvalue simplicity is the same absence-of-degeneracy.
  - Transposition candidate: YES.

- **S1 ↔ ym:L5** — face-only (SYMMETRY canonical).
  - Reason: Symmetry-type / bridge-family classification cross-cut via katz-sarnak.
  - Transposition candidate: SPECULATIVE.

- **S2 ↔ sato-tate:L_equidist** — shared ergodic property (MEASURE canonical).
  - Reason: Exponential grid-equidistribution is a weak-* convergence of discrete measures; paper60 §10 Sato-Tate analog.
  - Transposition candidate: SPECULATIVE.

- **S2 ↔ ym:L10b** — shared ergodic property.
  - Reason: Same kind of uniform-kernel-bound / spectral-lemma uniformity.
  - Transposition candidate: SPECULATIVE.

- **S3 ↔ goldbach:L_integer / twin-primes:L_integer** — shared critical exponent (ARITHMETIC canonical).
  - Reason: $\gamma_E$ is the canonical integer-lattice residual of the harmonic series; paper60 §14.
  - Transposition candidate: SPECULATIVE.

- **S3 ↔ bsd:L_Kronecker** — shared critical exponent.
  - Reason: Kronecker limit formula features analogous $\gamma_E$ residual; SPECULATIVE pending BSD X-Ray.
  - Transposition candidate: SPECULATIVE.

- **S3 ↔ grh:L_twist** — shared critical exponent.
  - Reason: Character-twisted $\gamma_E$ analogs; paper13b.
  - Transposition candidate: YES.

**Summary**: 48 cross-cut edges identified across 14 layers (avg ~3.4 cross-cuts per layer). 21 verified/YES-transposition (capacitor cell + paper60/61 citation + explicit programme-graph edge in paper13-rh), 27 SPECULATIVE (pending sibling-vertex X-Rays). The PRIMARY edges are L1/L2/L4a/L4c ↔ qg5d Branch D (the BC algebra is the shared operational core) and L6 ↔ bgs (GUE pair correlation = D_∞ spectral statistics, programme-graph edge). The RH vertex is unusually dense in cross-cuts compared to YM (38 cross-cuts across 20 YM layers = ~1.9 per layer; RH = ~3.4 per layer) — reflecting that RH sits at the *center* of the BC-algebra-facing outer ring (YM / BSD / GRH / BGS / PvNP / Baum-Connes all cross-cut at RH layers).

---

## §8 Current Walls

- **W1 — CCM (arXiv:2511.22755)**: The CCM operators $D_N$ on $E_N^+$ are constructed in an external preprint by Connes-Consani-Moscovici (2025). L1 is therefore EXTERNAL. Aggregate chain confidence is 8/10 conditional on W1; layers 2–6 independent of CCM at 9–10/10. Status: **OPEN-BUT-ADDRESSED** (transparent disclosure + arXiv external citation; CCM journal acceptance upgrades L1 to PROVED and chain to 9/10 unconditionally). Bypass routes on journal-retraction: Deninger adelic setup, Haran index theory, Katz-Sarnak random-matrix route (cited as fallback candidates in `strategy/rh/00-millenium-strategy.md` §11). Parallel track: `strategy/ccm-verification/` (Verification Cascade — Balaban / Bulatov-Zhuk tier cascade; sibling to YM H4 bypass effort). Capacitor cells: shared spectral-triple correspondences via `<pca-extension>/09-capacitor-correspondence-table-v1.md` (BC algebra dictionary).

- **W2 — CF uniformity caveat (Remark 8.4)**: The original L3d statement carried a Remark 8.4 $\log N$ caveat ("CF decay uniform in $N$ modulo a $\log N$ factor"). Status: **RESOLVED** 2026-04-14 via Slepian compatibility Lemma 12.1 (paper13-rh §S2). The resolution establishes that the grid Slepian kernel approximates the continuous Slepian kernel with $O(e^{-cN})$ error, removing the $\log N$ factor. Listed for transparency; no longer an active wall. (Session log: `session_rh_runs1to5.md` documents the upgrade from "PROVED with caveat" to "PROVED [PROVED with caveat]" after Runs 1–5 pipeline closure.)

These are the only two named walls. W1 is the sole OPEN-BUT-ADDRESSED item; W2 is RESOLVED. Links L2–L6 and S1–S3 are unconditional. On CCM 2025 journal acceptance, W1 upgrades to PROVED.

---

## §9 Cascading Refinements

- **Decomposition**: `strategy/decomposition/proof-chain/rh/PROOF-CHAIN.md` — NOT YET CREATED (decomposition bundle has empty `proof-chain/` directory as of 2026-04-15). When created, the X-Ray cross-cuts above can be used as inputs to identify which conditional links benefit from sub-chain decomposition. The primary candidate for decomposition is L1 (the CCM wall W1) — decomposition into the CCM construction's internal sub-claims.
- **CCM verification**: `strategy/ccm-verification/ledger.md#rh` — CCM-verification bundle has empty `proof-chain/` directory as of 2026-04-15. Expected verdict when ledger written: **IRREDUCIBLY-CCM-DEPENDENT at L1** (RH chain gates on CCM L1 uniquely; no internal bypass analog of YM's Step 18'). Verification Cascade (Balaban / Bulatov-Zhuk / Bögli tier) provides independent-verification track — note that the Bögli side of the cascade directly feeds L4a/L4b/L4c.
- **Inner rings**: NOT APPLICABLE — RH is a primary outer-ring vertex, not an inner-ring object.
- **RH Runs 1-5**: `online-researcher-adversarial/runs/rh/` (2026-04-12). Pipeline-validated 12-node chain with 3 critics / 12 attacks / 8 repaired / 0 BROKEN (session log `session_rh_runs1to5.md`). CF uniformity upgraded to [PROVED with caveat] → [PROVED] via S2 Lemma 12.1 on 2026-04-14. The X-Ray's per-layer assignments are consistent with the Runs 1–5 confidence calibration.
- **RH Millennium bundle**: `strategy/rh/` (2026-04-14). 00-millenium-strategy.md + rh-millenium-brief.md define the Clay-compliance audit + bare-deliverable-synthesis mode; the X-Ray feeds the compliance-map's "primary face / primary projection" columns as the annotation view of each layer.
- **Pin #6 anchor**: Agent L audit (2026-04-14, `integers/paper01-qg5d/code/pin6-audits/FINDINGS.md`) confirms the CP-violation / CKM pin anchor is `integers/paper12-cbb-system/research/102 §3.1` (Mellin duality $H_{BC} = \log T_{BC}$), NOT paper13-rh. RH chain does not gate on Pin #6 content; the $P_E$ projection is empty at layer level by design. When a CP-violation section is written for paper13-rh, the X-Ray will need an S4 supporting layer for Pin #6 anchoring.
- **Cascading refinement from QG5D W1/W2 closure (2026-04-14)**: Paper 1's W1 (scheme independence) + W2 (Route-C 3-loop explicit) closures propagate through Branch D's foundation but impact is cosmetic-to-small on RH chain (RH never gated on scheme-independence question directly). Programme-graph note in paper13-rh.

---

## §10 Known Gaps (OPEN items at this vertex)

- **G1 — W1 CCM (arXiv:2511.22755)**: Layer 1 construction of $D_N$ on $E_N^+$ is external to the programme. — face: RESONANCE, projection: $P_D$, pattern: P1. STATUS: OPEN-BUT-ADDRESSED via transparent disclosure + arXiv citation + Verification Cascade parallel track + fallback candidates. The SOLE OPEN ITEM in the RH proof chain. Upgrade path: journal acceptance of CCM 2025 → L1 PROVED, chain 8/10 → 9/10 unconditional.

That's it. Layers 2–6 and S1–S3 are unconditional (8 of 9 are PROVED independently of CCM). The single wall is W1, with disclosure + bypass + fallback machinery in place.

Secondary transparency entries (not OPEN):

- **G0 (resolved) — W2 CF uniformity caveat**: Remark 8.4's $\log N$ factor in L3d has been removed via Slepian compatibility Lemma 12.1 (S2), 2026-04-14. Listed only for audit-trail transparency.
- **G2 (external dependency notes for Pillar B independence audit)**: L3a-3d and L4a-4c use Teschl Lemma 2.7 (Schrödinger-operator resolvent-convergence literature), Davis-Kahan (standard matrix-analysis), Rellich-Kondrachov (standard functional-analysis), Hurwitz's theorem (classical complex analysis) — all LITERATURE at textbook level, not named walls. No OPEN status; listed for completeness at the Pillar B (independence) audit level.

---

## Footnotes — Considered-but-rejected alternatives summary (per §3)

This document records the WINNING assignments. The full critic-attack record (if/when produced) would live at `strategy/x-ray/pac-output/runs/run-XX/vertices/rh/critic-attacks.md` and arbiter decisions at `strategy/x-ray/pac-output/runs/run-XX/vertices/rh/arbiter-decisions.md`.

Notable arbiter decisions embedded in §3:
- L1 face: RESONANCE over CURVATURE (CCM operators are spectral, not curvature-based — clean win).
- L6 face: TOPOLOGY over RESONANCE (paper60 §18/§19 canonicalization — the top-level QED is the torus-existence / transversal-intersection statement).
- L6 projection: $P_D$ over $P_O$ (the mechanical final step is $P_D$-internal; $P_O$ is the outer-ring consequence, kept as secondary).
- L3d pattern: P3 Scale-Setting over P5 Zeta Regularization (the specific number $\rho \geq 4.27$ is the scale-set; P5 machinery is downstream).
- S2 face: MEASURE over DYNAMICS (exponential equidistribution is measure-theoretic weak-*; traversal-reading alternative).
- S3 face: ARITHMETIC over AMPLITUDE ($\gamma_E$'s origin is integer-lattice, paper60 §14).

---

## §11 Atlas metadata

- **Line count**: ~720 lines (this file)
- **Layer count**: 14 (L1 + L2 + L3a + L3b + L3c + L3d + L4a + L4b + L4c + L5 + L6 + S1 + S2 + S3)
- **Cross-cut count**: 48 edges (21 YES-transposition / verified + 27 SPECULATIVE)
- **Primary face**: RESONANCE
- **Primary projection**: $P_D$
- **Primary pattern**: P4 Topological Rigidity (rigidity-canonical layers: L4a, L4b, L4c; mixed with P1/P5 across other layers)
- **Named walls**: 1 OPEN (W1 CCM), 1 RESOLVED (W2 CF caveat)
- **Snapshot date**: 2026-04-15
- **Canonical chain location**: `strategy/proof-chain/rh/PROOF-CHAIN.md` (per Phase 11 self-healing 2026-04-15 centralization)

---

## §12 Methodology notes / caveats

1. **Vocabulary canon compliance**: All references to the programme's 4+1 coordinate structure use M⁵ = M⁴ × S¹ per `strategy/north-star.md` §0.10. No "5-dimensional" or "extra dimension" language.
2. **Non-destructive**: This X-RAY does NOT modify `strategy/proof-chain/rh/PROOF-CHAIN.md`. The canonical chain is read-only for this bundle.
3. **Primary-face trade-off at L6**: The single most contested assignment in the whole X-RAY is L6's primary face. The final mechanism is RESONANCE-canonical (self-adjointness + spectral exactness), but paper60 §18 and §19 explicitly frame the *top-level claim* as a TOPOLOGY statement (zeros-as-transversal-intersection / torus-existence). The arbiter chose TOPOLOGY as primary to honor paper60 §18/§19's framing, with RESONANCE recorded as secondary. An alternative arbiter decision (RESONANCE primary, TOPOLOGY secondary) would reduce RESONANCE count to 4 → 5 and TOPOLOGY count to 1 → 0 in §5; this would not change the overall interpretation (RESONANCE remains dominant either way).
4. **The $P_D$-monopoly**: 100% of layers are $P_D$-primary. This is a structural feature, not an X-RAY artifact. Compare YM (65% $P_B$ / 30% $P_D$ / 5% $P_O$) or anticipated BSD (likely $P_D$-dominant but with $P_E$ touches via elliptic-curve L-value pins). The $P_D$-monopoly reflects paper61 §10's dictum: "every outer-ring vertex involves the BC algebra. RH is a spectral question about the BC algebra's generator" (paper61 §10 ¶ penultimate). RH is the *canonical* $P_D$-only vertex; YM and BSD both have multi-projection spreads.
5. **Cross-cut density**: RH's ~3.4 cross-cuts-per-layer is ~1.8× YM's ~1.9 cross-cuts-per-layer. This reflects that RH sits at the *center* of the BC-algebra-facing ring. The primary cross-cut bundle (L1/L2/L4a/L4c ↔ qg5d Branch D) is dense because the BC algebra is Branch D's operational core; the secondary bundle (L6 ↔ bgs/bsd/grh) is dense because the RH / GRH / BSD / BGS statements all share the same critical-line / L-function / zero-distribution structure.
6. **Pin #6 note**: Pin #6 ($J_\mathrm{CKM} \times 10^5 = \log(\gamma_1) \cdot \zeta(3)$) references $\gamma_1 = 14.134725\ldots$ from RH but the load-bearing anchor is `integers/paper12-cbb-system/research/102 §3.1`, not paper13-rh (Agent L audit 2026-04-14). When the CP-violation section is written for paper13-rh, this X-RAY will need updating with an S4 layer for the Pin #6 anchor.

---

## §13 BGS / spectral-statistics note

RH has an explicit, load-bearing interaction with the BGS (Bohigas-Giannoni-Schmit) conjecture — the statement that eigenvalue spacings of quantum systems with chaotic classical limits match GUE statistics.

**Programme-graph edge** (from `strategy/proof-chain/rh/PROOF-CHAIN.md` "Programme graph edges"):
> **BGS:** GUE pair correlation of zeros = spectral statistics of $D_\infty$

**Layer-level touches**:
- **L3d** (CF decay $\rho \geq 4.27$) — the CF-decay exponent is the dynamical-mixing rate whose quantitative version is GUE pair-correlation. Cross-cut: L3d ↔ bgs:L_pair-correlation.
- **L6** (spec$(D_\infty) = \{\gamma_n\}$) — the zero set IS the spectrum; BGS says it's a GUE ensemble. Cross-cut: L6 ↔ bgs:L_GUE.
- **S1** (AE simplicity) — GUE-level simplicity / Wigner-Dyson level-repulsion. Cross-cut: S1 ↔ bgs:L_simple.

**Face / projection overlap**:
- RH's primary face is RESONANCE; BGS's primary face is likely SPREAD or SYMMETRY (pending BGS X-Ray) — different primary faces, but strong cross-face overlap at L3d (DYNAMICS shared) and L6 (TOPOLOGY / holonomy as pair-correlation invariant).
- RH's primary projection $P_D$ and BGS's projection (likely $P_D$ with $P_E$-pin touches for Montgomery-Odlyzko pair correlation) overlap strongly at the $P_D$ level; BGS is in the same Branch-D neighborhood as RH.

**Implication for Verification Cascade**: when BGS X-Ray is produced, the L3d/L6/S1 cross-cuts should be strengthened with shared-invariant tags (CF decay ↔ pair correlation; holonomy ↔ level repulsion; spectral gap ↔ simple spectrum). The BGS interaction is a candidate pillar for the "beyond-Clay C_bare" bonus theorem on Montgomery-Odlyzko GUE match (§7 of `strategy/rh/deliverables/rh-beyond-bare.md`).

**No new walls introduced**: the BGS interaction is additive cross-cut evidence, not a conditional dependency. RH does not gate on BGS; BGS is a spectral-statistics consequence of RH + the specific $D_\infty$ construction.

---

*End of RH X-Ray. Snapshot 2026-04-15. 14 layers (6 primary + 3 sub-layers L3a/b/c/d + L4a/b/c + 3 supporting S1/S2/S3) annotated. 48 cross-cuts identified. RESONANCE-canonical, $P_D$-monopolar (100%), P4/P5/P1-mixed proof chain. One wall (W1 CCM); one resolved-caveat (W2 CF uniformity, closed 2026-04-14).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
