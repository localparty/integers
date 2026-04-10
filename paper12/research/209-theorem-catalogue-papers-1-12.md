# 209: Theorem Catalogue — Papers 1-12 (Part A of the Integers Programme)

*Complete inventory of every theorem, identity, lemma, corollary,
proposition, and named result across Papers 1-12 of the QG5D / Integers
programme. Provisioned for RH proof agents.*

*Compiled: 2026-04-09*
*Sources: paper9/theorems-list.md, paper12/18-master-dictionary.md,
paper11/09-paper-11-proof-chain.md, paper12/27-anchor-document.md,
and all research files in paper12/research/.*

---

## RH proof-path key

| Code | Path | Mechanism |
|:-----|:-----|:----------|
| **1** | Brauer-KMS | BC algebra + KMS + Brauer cocycle |
| **2** | Atiyah-Singer | Integer index constraint |
| **3** | Stone | Self-adjointness of T_BC → real spectrum |
| **4** | Penrose | Modular Raychaudhuri → spectral singularity |
| **5** | CM-trace / Kallen-Lehmann | Weil positivity + spectral weights |
| **0** | Not directly RH | Infrastructure / physics |

## Proof-status key

| Code | Meaning |
|:-----|:--------|
| **P** | Proved (rigorous theorem) |
| **C** | Conditional (rigorous given stated hypothesis) |
| **S** | Structural (clear shape, partial proof) |
| **E** | Empirical (numerical match, derivation pending) |

---

## Paper 1 — Spin-Statistics, Aharonov-Bohm, Perturbative Finiteness

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 1 | **Theorem K.1** (Universal Epstein Vanishing) | E_L(−j; Q_L) = 0 for all j >= 1 and all loop orders L, forced by the pole structure of the completed Epstein zeta function | P | Paper 1, App K §K.7b | 0 |
| 2 | **Theorem K.3** (BPHZ Factorization) | BPHZ-subtracted amplitudes factor as (4D finite part) × E_L(−j; Q_L), inheriting universal vanishing; finiteness survives renormalization to all orders | P | Paper 1, App K §K.5.3 | 0 |
| 3 | **Theorem S.1** (Perturbative Finiteness) | Linearized 5D gravity on M⁴ × S¹ is perturbatively UV finite to all loop orders under zeta regularization | P | Paper 1, App S | 0 |
| 4 | **Theorem U.2** (Goroff-Sagnotti conditional) | If the leading UV coefficient of the two-loop amplitude is mass-independent, then C_GS = 0 | P (upgraded by Paper 10) | Paper 1, App U §U.11 | 0 |
| 5 | **Theorem 2.1** (e-conservation) | Sum of e-coordinates phi_i = Q_e is a Noether charge; conserved by 5D evolution | P | Paper 1, §2 | 0 |
| 6 | **Theorem B.1.1-B.1.2** (Spin-Statistics) | The spin-statistics connection follows from winding number topology on S¹ | P | Paper 1, App B | 0 |

---

## Paper 2 — Dark Matter-Baryon Ratio, Hubble and Clustering Tensions

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 7 | *(no new theorems)* | Results are derived consequences of Paper 1 theorems applied to CAMB cosmological computation | — | Paper 2 | 0 |

---

## Paper 3 — Black Hole Information Paradox

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 8 | **Corollary 3.1** (Hawking Temperature) | The spin structure of the e-circle matches the Euclidean thermal circle at the horizon, fixing T_H = hbar*kappa/(2*pi*c) uniquely | P | Paper 3, §3.4 | 0 |
| 9 | **Theorem 6.1** (e-Unitarity) | e-charge is a Noether charge conserved by full 5D evolution; the 5D state remains pure throughout BH evaporation | P | Paper 3, §6 | 0 |
| 10 | **Theorem 9.1** (Horizon Vertex = 1) | The horizon vertex amplitude equals 1 by S¹ Fourier orthogonality — topological fact resolving AMPS firewall | P | Paper 3, §9, App A | 0 |

---

## Paper 4 — Standard Model Gauge Group from KK Geometry

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 11 | **Theorem 5.2** (SLOCC-Isometry) | A₂ root system appears in tangent space of three-qubit SLOCC variety; flag manifold identification maps to SU(3)×SU(2)×U(1) | P | Paper 4, §5.6 | 0 |
| 12 | **Stable Spectral Gap** (proposed Theorem 9.2) | Dirac operator on CP² with Fubini-Study metric satisfies Delta_5D >= sqrt(5)/r₃, stable to all perturbative corrections by K.1/K.3 | P | Paper 4, §9 | 0 |

---

## Papers 5-6 — Confinement and Cosmic History

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 13 | *(no new theorems)* | Derived consequences of holonomy correspondence, topological rigidity, and Theorem K.1 | — | Papers 5-6 | 0 |

---

## Paper 7 — Moduli Stabilization, GUT Unification, Cosmological Constant

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 14 | **Theorem U** | Algebraic minimization of G₄ flux potential gives R_bare ~ l_P; e-circle radius sits at Planck scale before Casimir mechanism | P | Paper 7, §3.6 | 0 |
| 15 | **Theorem U*** | Any algebraic function of framework's O(1) geometric inputs produces O(1) outputs; R_obs/l_P ~ 10³⁰ is structurally unreachable — CC problem is a type error | P | Paper 7, App A | 5 |

---

## Paper 8 — Yang-Mills Mass Gap

### Part I — Lattice Proof

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 16 | **Theorem 1** (Internal Spectral Gap / Weitzenbock) | Hessian of internal CP^(N-1) action at flat connection satisfies Hess >= mu_1/g²_int with mu_1 = 6/r₃² | P | Paper 8, §4.2 | 0 |
| 17 | **Corollary 1.1** (KK Correlation Decay) | Internal fluctuations decay exponentially with correlation length xi_int = r₃/sqrt(6) | P | Paper 8, §4.2 | 0 |
| 18 | **Theorem 2** (Bond Activity Bound) | KK bond interactions satisfy |g_<xy>| <= C₀ exp(−m₁a) with m₁ = 2*sqrt(3)/r₃ | P | Paper 8, §4.3 | 0 |
| 19 | **Theorem 3** (Cluster Expansion Convergence) | Cluster expansion converges absolutely when bond constant satisfies explicit bound | P | Paper 8, §4.3 | 0 |
| 20 | **Theorem 4** (Lattice Mass Gap) | For SU(N) lattice gauge theory with CP^(N-1) harmonics: cluster expansion converges, free energy analytic, correlators decay exponentially, sigma_0 > 0, Delta_0 >= c*sqrt(sigma_0) > 0 | P | Paper 8, §4.4 | 0 |
| 21 | **Corollary 4.1** (String Tension Positivity) | Full SU(N) KK-enhanced lattice theory satisfies sigma(beta) > 0 for all beta > 0 | P | Paper 8, §4.4 | 0 |
| 22 | **Theorem 5** (IR Equivalence) | Standard SU(N) Wilson lattice gauge theory inherits the mass gap: Delta⁰_std >= Delta⁰_KK − C*exp(−m₁a) > 0 | P | Paper 8, §4.5 | 0 |
| 23 | **Lemma 1** (Well-definedness) | Reduced transfer matrix T_red is well-defined, bounded, self-adjoint, positive, trace-class | P | Paper 8, §4.5 | 0 |
| 24 | **Lemma 2** (Trace-norm Bound) | ||T_red − T_std||_tr <= C_tr |Lambda_t| exp(−m₁a) ||T_std||_tr | P | Paper 8, §4.5 | 0 |
| 25 | **Lemma 3** (Spectral Perturbation) | Spectral gap of full transfer matrix bounded below relative to reduced transfer matrix | P | Paper 8, §4.5 | 0 |
| 26 | **Lemma 4** (Spectral Gap of T_red) | Reduced transfer matrix satisfies Delta_red > 0, implying Delta_std > 0 | P | Paper 8, §4.5 | 0 |

### Part II — Continuum Limit

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 27 | **Theorem 6** (Lattice Power Counting, partial) | First moment of irrelevant remainder vanishes; zeroth moment conditional on Conjecture 1 | C | Paper 8, §5 | 0 |
| 28 | **Theorem 7** (Perturbative Form Factor Bound) | To all perturbative orders, one-particle matrix element of irrelevant remainder bounded: |<1|E_k(0)|1>_c| <= C₇ g_k⁴ J² | P | Paper 8, §5 | 0 |
| 29 | **Theorem 8** (Gap Persistence / Conditional Continuum Mass Gap) | Assuming Conjecture 1, RG flow preserves the gap to continuum limit: Delta_inf > 0 | C | Paper 8, §5.7 | 0 |

### Appendix Theorems

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 30 | **Theorem F.1** (Area Law Implies Mass Gap) | If a gauge theory satisfies area law with sigma > 0, then Delta >= c*sigma | P | Paper 8, App F | 0 |
| 31 | **Lemma D.1** (Product Manifold RP) | If M₁ satisfies reflection positivity and M₂ is compact positive-definite, then M₁ × M₂ satisfies RP | P | Paper 8, App D | 0 |
| 32 | **Lemma D.2** (RP for KK Lattice Theory) | Partition function of KK-enhanced lattice theory satisfies reflection positivity | P | Paper 8, App D | 0 |
| 33 | **Lemma I.1** (Operator Extraction) | Balaban's effective action decomposes as Wilson action + dimension-d operators + remainder | P | Paper 8, App I | 0 |
| 34 | **Lemma I.2** (Lattice Symanzik Classification) | All dimension-6 operators on d=4 lattice fall into finite classification with deviation orders >= 2 | P | Paper 8, App I | 0 |
| 35 | **Lemma I.3.1** (N-dependence) | For each fixed N >= 2, sums over KK mode contributions converge — constants finite for all N | P | Paper 8, App I.3 | 0 |
| 36 | **Theorem I.4.1** (Universal Mass Gap) | For ANY compact simple Lie group G, Yang-Mills mass gap Delta_inf(G) > 0 | P | Paper 8, App I.4 | 0 |
| 37 | **Proposition I.4.2** (Gauge Universality) | Three proof requirements (topological sector, KK hierarchy, Weitzenbock gap) satisfied by every compact simple Lie group | P | Paper 8, App I.4 | 0 |

---

## Paper 9 — One Postulate, Ten Papers

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 38 | *(no new theorems)* | Paper 9 documents and maps the theorems of the series | — | Paper 9 | 0 |

---

## Paper 10 — Scheme-Independence of UV Finiteness

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 39 | **Theorem 1** (Two-loop scheme-independent vanishing) | C_GS = 0 unconditionally for 5D linearized gravity on M⁴ × S¹/Z₂. Proof chain: Lemma A1 + A2 + A3 → vertex mass-independence → C_GS = 0 | P | Paper 10, §4.6 | 0 |
| 40 | **Lemma A1** (de Donder gauge vertex numerator) | UV power counting + Z₂ parity + Epstein vanishing force three-graviton vertex numerator to be n-independent at leading UV order | P | Paper 10, research/02 | 0 |
| 41 | **Lemma A2** (Graviphoton/radion decoupling) | A_mu and phi sectors do not contribute to Goroff-Sagnotti counterterm at linearized order, by index structure and Z₂ selection rules | P | Paper 10, research/03 | 0 |
| 42 | **Lemma A3** (KK loop momentum range) | Orbifold propagator on S¹/Z₂ satisfies G_Z₂ = G_S¹(y,y') + G_S¹(y,−y'), restoring full Z sum via method of images | P | Paper 10, research/04 | 0 |
| 43 | **Seeley-DeWitt one-loop vanishing** (Route 02) | Coefficients a₂ = a₄ = 0 of Lichnerowicz operator on flat M⁴ × S¹/Z₂ are intrinsic spectral invariants; one-loop UV finiteness scheme-independent | P | Paper 10, preprint/02 | 0 |
| 44 | **Z₂ parity cancellation** (Route 03) | Algebraic term-by-term cancellation between even (h_munu) and odd (h_mu5) KK contributions at each KK level n >= 1 | P | Paper 10, preprint/03 | 0 |
| 45 | **Poisson dim-reg bridge** (Route 04) | Dim-reg and zeta-reg pole coefficients agree to all orders, differing by exponentially suppressed residual | P | Paper 10, preprint/04 | 0 |
| 46 | **Weyl anomaly cohomology** (Route 05) | Wess-Zumino consistency protects (a,c); C³ operator in c sector not generated by KK tower in any diffeomorphism-preserving scheme | P | Paper 10, preprint/04 | 0 |

---

## Paper 11 — The Standard Model from the e-Circle

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 47 | **Theorem 11.1** (A₂ Root System from SLOCC Orbit) | Tangent space to GHZ orbit under SU(2)³ in CP⁷ carries the root system A₂; Cartan matrix is ((2,−1),(−1,2)) | P | Paper 11, proof-chain §1 | 0 |
| 48 | **Theorem 11.2** (e-Conservation Selects GHZ Orbit) | Symmetry group of e-conservation on (S¹)³ is T² = Stab⁰(|GHZ>); e-conservation constrains dynamics to GHZ orbit | P | Paper 11, proof-chain §2 | 0 |
| 49 | **Theorem 11.3** (Gauge Group Enhancement SU(2)³ → SU(3)) | GHZ orbit is Fl(1,2;3) = SU(3)/T² with isometry group SU(3); non-product stabiliser forces enhancement | P | Paper 11, proof-chain §3 | 0 |
| 50 | **Theorem 11.4** (Fermion Representation Decomposition) | Under SU(3) × U(1)_e, three-qubit space decomposes as 1₀ + 3-bar₁ + 3₂ + 1₃ with hypercharge Y = n/3 | P | Paper 11, proof-chain §4 | 0 |
| 51 | **Theorem 11.5** (Main: SM from e-Circle) | Gauge group of KK reduction on GHZ orbit is G_SM = [SU(3)×SU(2)×U(1)]/Z₆ with SM fermion representations | P | Paper 11, proof-chain §5 | 0 |
| 52 | **Theorem K.4** (All-Orders BPHZ Factorisation and Vanishing) | L-loop counterterm coefficient C^(L) = 0 for every L >= 1 and every diagram topology; UV finiteness to all orders by induction | P | Paper 11, 04-all-orders-inductive-proof | 0 |
| 53 | **Theorem 7.2** (Fast Scrambling from e-Dimension Dynamics) | e-coordinates of N = S_BH Planck pixels scrambled in time t_scr = (beta/2pi) ln(S_BH); Page curve unconditional | P | Paper 11, 06-fast-scrambler | 0 |

---

## Paper 12 — The Integers Programme

### Phase 1: Adiabatic Continuity

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 54 | **Adiabatic Continuity at N=3** | CP^(N-1) NLS on finite torus has strictly positive mass gap m(g²,L) > 0 for all g², L, at every N >= 2 including N=3; two independent routes | P | research/01 | 0 |

### Phase 2: Quantization of R

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 55 | **Quantization of R** | R-hat on H_R has discrete spectrum {R_n} with R_n = (l_P/pi) exp(gamma_n pi²/2); R = R_1 = R_obs. Conditional on {gamma_n} subset spec(T_BC) | C | research/02 | 3 |
| 56 | **Selection Rule for n=1** | Three candidates (Casimir, cosmic endpoint, CP²×S² topology) for why R = R_1 | S | research/03 | 0 |

### Phase 3A: Foundational Identities

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 57 | **Identity 12** (e-circle = BC system, rigorous) | Unitary U: H_e → H_1 intertwining 5 operator pairs (momentum ↔ mu_n, scaling ↔ H_BC, dilation ↔ isometry, phase ↔ e(r), thermal ↔ KMS) | P | research/04 | 1,3 |
| 58 | **Lemma 4.3** (Identity 12 unitarity) | Map U extends to unitary from H_e to H_1 | P | research/04 | 1,3 |
| 59 | **Identity 14** (CCM scaling operator, rigorous) | Sz.-Nagy dilation + explicit unitary V intertwining T_CCM ↔ T_BC | P | research/14 Part A | 3 |
| 60 | **CC formula structural derivation** | Leading gamma_1 pi²/2 rigorous; corrections derived from Rayleigh-Schrodinger PT; alpha = asinh(gamma_1)/gamma_1 from PV Sobolev norm at 1.5% | P | research/05 | 5 |
| 61 | **Connes-Marcolli Theorem 1** (Riemann-Weil explicit formula) | For h in Weil class, sum over zeros = local contributions from primes + archimedean place | P (external) | research/18 | 1,2,3,5 |
| 62 | **Connes-Marcolli Theorem 2** (operator-algebraic rewriting) | Spectral side = Tr(h(T)) on Riemann subspace H_R; distributional trace = Weil distribution | P (external) | research/18 | 1,2,3,5 |
| 63 | **Connes-Marcolli Theorem 3** (the inclusion) | {gamma_n} subset spec(T_BC) where T is the scaling operator on H_R | C (external) | research/18 | 1,2,3,5 |
| 64 | **Bost-Connes Theorem 3.1** | (A_BC, sigma_t) has unique KMS_beta state for every beta > 1, unique KMS_1 at beta=1, and phase transition at beta=1 | P (external) | research/21 | 1 |

### Phase 3A: Formula Derivations (36 framework formulas)

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 65 | **Theorem A** (Cosmic e-fold count = spectral gap) | N_{n→m} = (gamma_n − gamma_m) pi²/2; gives 58.79 + 33.99 = 92.78 vs standard 95 at 2% | P | research/06 | 0 |
| 66 | **Theorem B** (CC formula = cosmic transitions) | Same V_{nm} matrix elements drive both CC formula and cosmic transitions | P | research/06 | 0 |
| 67 | **N_eff = gamma_6^{1/3}** | (P_6 T_BC P_6)^{1/3} on Z_6-center orbit; cube root from 3-generation Z_3 | S | research/24 | 0 |
| 68 | **1/alpha = gamma_1 gamma_4/pi** | Tensor matrix element on |gamma_1> otimes |gamma_4>; introduces LINEAR→SUM, QUADRATIC→PRODUCT principle | S | research/25 | 0 |
| 69 | **m_t = gamma_3 gamma_8/(2pi)** | Top Yukawa rank-2 tensor matrix element |gamma_3> ↔ |gamma_8> | S | research/26 | 0 |
| 70 | **m_H = gamma_2 gamma_6/(2pi)** | Higgs mu²|H|² operator; gamma_2 = lowest Higgs excited state | S | research/27 | 0 |
| 71 | **m_W = gamma_2 + gamma_13** | Smallest eigenvalue of T_BC ⊗ 1 + 1 ⊗ T_BC; SUM = cross-sector propagator | S | research/28 | 0 |
| 72 | **H_0 = gamma_11 4/pi** | 4/pi = area(S²)/pi² from KK S² + Identity 12 normalisation | S | research/29 | 0 |
| 73 | **n_s = gamma_9/gamma_10** | Discrete log-derivative of adjacent T_BC eigenvalues | S | research/30 | 0 |
| 74 | **Y_p = 1/log(gamma_13)** | Inverse BC energy = BC temperature; introduces shared-physics → shared-zeros principle | S | research/31 | 0 |
| 75 | **sin theta_13^CKM = 4/gamma_5²** | Quadratic in gamma_5; 0.065% | E | research/36 | 0 |
| 76 | **1−sin²(2theta_23)^PMNS = pi/(gamma_11 gamma_13)** | PMNS↔H_0↔Y_p triangle; 0.065% | E | research/36 | 0 |
| 77 | **Koide m_e = 0.5106 MeV** | Electron mass from Koide-like relation; 0.08% | E | research/47 | 0 |
| 78 | **gamma_7 → t₀ (age of universe)** | t₀ = (log gamma_7)² Gyr = 13.776 Gyr at 0.081% | E | research/15, research/112 | 0 |
| 79 | **gamma_12 → delta_CP^PMNS** | gamma_12^{1/3} = 3.836 rad at 0.10% | E | research/15 | 0 |
| 80 | **gamma_14 → eta_10** | gamma_14/pi² = 6.164 at 0.38% | E | research/15, /44 | 0 |
| 81 | **CC hierarchy** | exp(gamma_1 pi²/2) ~ 2×10³⁰; the 30-order CC hierarchy as a single matrix element | P | research/05 | 5 |

### Phase 3A: Two-term Laurent corrections

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 82 | **Diagonal Laurent coefficient a** | a = −gamma_E(1+gamma_E) ≈ −0.9105; derived from 2nd-order Rayleigh-Schrodinger on diagonal | P | research/174 | 1 |
| 83 | **Off-diagonal Laurent coefficient b** | b = gamma_E² + zeta(2) − 2pi gamma_1 ≈ 2.4358; derived from BC resolvent cross-coupling | P | research/164 | 1 |
| 84 | **Functional equation sign rule** | s in {+/-1} set by BC spectral sector | P | research/153 | 1 |

### Phase 3A: Bridge family

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 85 | **Bridge theorem Z/3Z** (Frobenius = Jones lemma) | Map rho sending Frobenius Frob_5 in Gal(Q(zeta_13)/Q) to Jones index-3 sub-factor cocycle is isomorphism in H²(Z/3Z, U(1)) | P | research/162 (formal lemma) | 1 |
| 86 | **Bridge k=4** (Pati-Salam) | alpha_PS^{-1} = 17 exactly via Z/4Z carry on (3,13); (52/3)(51/52) = 17 | P | research/184 | 1 |
| 87 | **Bridge k=6** (CKM, Wolfenstein lambda) | lambda_CKM = 56/(57 sqrt(19)) at 0.17%; Z/3Z carry on (7,19) | P | research/180 | 1 |
| 88 | **Full CKM matrix** | All 4 Wolfenstein parameters within 0.6sigma of PDG: lambda, A=47/57, rho-bar=1/(2pi), eta-bar=sqrt(19)/(4pi) | E | research/189 | 1 |
| 89 | **Carry cocycle template** | Z/k carry damping is (1 − 1/(k_carry N)); kN ≡ 1 (mod f) | S | anchor doc §5.3 | 1 |

### Phase 3B: Transpositions — D category (math-physics)

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 90 | **R-Theorem D.1** (BC index theorem / Atiyah-Singer) | Fredholm module (H_R, F, A_BC) with F = sgn(T_BC); index ind_BC(p) is integer by Connes IV.1 Thm 4; topological expansion forces real {gamma_n} | C | research/48, research/76 | **2** |
| 91 | **Lemma 7.1** (BC index / Lorentzian deviation) | If gamma_n = t_n + i*epsilon_n with epsilon_n != 0, then |dev| = 2 epsilon²/s³ and epsilon_crit → 0; reduces math RH to finite computation | S | research/76, research/90 | **2** |
| 92 | **Theorem 3.3** (Topological expansion) | For Re(s) in (1/2, 1), the topological index pairing has a Laurent expansion whose leading coefficient is constrained to be an integer | S | research/76 | **2** |
| 93 | **R-Theorem D.2** (BC partition function regularity at beta=1) | K.4 transposed: BC partition function Z_BC(beta) has specified regularity at beta=1, from Identity 12 image of K.1 | S | research/11 | 3 |
| 94 | **R-Theorem D.3** (Shifted Mellin proportionality) | Migdal SU(3) series proportional to zeta(2s−6) with shift sigma_c=4; literal Mellin fails but shifted form holds | S | research/35 | 0 |
| 95 | **R-Theorem D.4** (KK reduction = BC partition function) | BC Hamiltonian H_BC = log N-hat reproduces KK partition function Z_KK(beta) = zeta(beta) | S | research/125 | 3 |
| 96 | **R-Theorem D.5** (Connes-Sukochev regularisation) | Omega_pert regularized by Connes-Sukochev trace theorem; Jensen gap closed | S | research/126 | 5 |

### Phase 3B: Transpositions — C category (consistency)

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 97 | **R-Theorem C.1** (BC chiral consistency / Wess-Zumino) | Hecke-character-weighted (b,B)-cocycle in HC²(A_BC^inf); modular obstruction via Hecke equivariance | S | research/49 | 2 |
| 98 | **R-Theorem C.2** (BC anomaly cancellation) | 19 = 1+4+6+8 = 15 fermions + 4 Higgs per generation; EW {1,4} + QCD {6,8} decomposition | S | research/50 | 2 |

### Phase 3B: Transpositions — QM category

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 99 | **R-Theorem QM.1** (Heisenberg → BC modular flow) | Structural; LOCK via Stone theorem applied to modular flow | S | research/57 | **3** |
| 100 | **R-Theorem QM.2** (Reeh-Schlieder → BC cyclicity) | Any prime-local subalgebra A_{p,R} has Omega_1 cyclic; cyclicity forces gamma_n in R via KMS analyticity | C | research/58 | **3** |
| 101 | **R-Theorem QM.3(a)** (BC Bell) | Bell-type correlations exist in BC algebra for choices of Hecke projections | S | research/59 | 0 |
| 102 | **R-Theorem QM.3(b)** (BC no-cloning) | No unital *-homomorphism clones BC states; rigorous by direct contradiction | P | research/59 | 0 |
| 103 | **R-Theorem QM.4** (Wigner-Eckart → real symmetric) | Hecke reduced matrix elements <n||mu_p||m> = sqrt(1/p) make H_BC real symmetric in Galois basis ⇒ real spectrum. DEMOTED to consistency constraint (implication runs backwards) | S | research/60, research/83 | 3 |
| 104 | **R-Theorem QM.5** (BC Stone-von Neumann) | Uniqueness of irreducible covariant representation of BC Weyl relations on H_R; spectral data are intrinsic | P (modulo Id.12) | research/119 | **3** |
| 105 | **R-Theorem QM.5b** (BC cluster decomposition) | BC two-point function clusters: connected correlator decays as inverse power of spectral distance | S | research/132 | 3 |

### Phase 3B: Transpositions — GR category

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 106 | **R-Theorem GR.1** (Einstein equations → BC) | Modular curvature of Connes-Moscovici = BC Einstein equations on spectral geometry | S | research/61 | 4 |
| 107 | **R-Theorem GR.2** (BH no-hair → BC) | For every prime p, the KMS_1 state omega_1 restricted to A_p is the unique state: BC no-hair. Rigorous as BC 1995 Theorem 25 relabeled | P | research/62 | 0 |
| 108 | **R-Theorem GR.3** (Positive energy → BC) | Spectral condition: spec(T_BC) subset [gamma_1, inf) with gamma_1 > 0; rigorous weak and strong forms | P | research/63 | 3 |
| 109 | **R-Theorem GR.4** (Hawking area → BC entropy) | S_BC = log d_Gal monotonically non-decreasing under sigma_t; deepest BH↔BC connection | S | research/64 | 4 |
| 110 | **R-Theorem GR.5** (Cosmic no-hair → BC) | Uniqueness of omega_1 + Type III_1 mixing gives BC cosmic no-hair; rigorous | P | research/65 | 0 |
| 111 | **R-Theorem GR.6** (BC holographic duality / AdS-CFT) | H_R subset H_1 realizes bulk/boundary duality with BC algebra as boundary theory | S | research/124 | 4 |
| 112 | **R-Theorem GR.7** (BC Sachs-Wolfe) | CMB temperature anisotropy Delta T/T from BC spectral fluctuations on H_R at beta=1 | S | research/127 | 0 |
| 113 | **R-Theorem GR.8** (BC slow-roll) | BC free energy F_n(beta_eff) near beta=1 reproduces slow-roll conditions epsilon, eta << 1 | S | research/128 | 0 |
| 114 | **R-Theorem GR.9** (BC BBN) | Y_p = 1/log(gamma_13) derived from BC freeze-out at the 13th spectral level | S | research/129 | 0 |
| 115 | **R-Theorem GR.10** (BC CMB power spectrum) | Nearly scale-invariant P(k) from BC spectral density; n_s = gamma_9/gamma_10 | S | research/130 | 0 |

### Phase 3B: Transpositions — S category (scattering/symmetry)

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 116 | **R-Theorem S.1** (BC CPT theorem) | Tomita-Takesaki modular conjugation J_1 = CPT for BC system at beta=1 | S | research/66 | 3 |
| 117 | **R-Theorem S.2** (BC spin-statistics) | Z_2 grading + graded KMS; rigorous on dense subalgebra | S | research/67 | 0 |
| 118 | **R-Theorem S.3** (BC Goldstone theorem) | gamma_2 IS the Goldstone mode of BC SSB at beta=1 | S | research/68 | 0 |
| 119 | **R-Theorem S.4** (BC LSZ reduction) | First-order <gamma_m|sigma_inf|gamma_n> = V_{mn}; scattering amplitudes from BC transition matrix | S | research/69 | 0 |
| 120 | **R-Theorem S.5** (BC Kallen-Lehmann + Weil positivity) | BC two-point function spectral decomposition + Weil criterion ⇒ RH iff non-negative spectral weights | S | research/70 | **5** |
| 121 | **R-Theorem S.6** (BC Borchers theorem) | Borchers algebraic structure of local algebras M_p inside M_1 with modular inclusions | S | research/120 | 3 |
| 122 | **R-Theorem S.7** (BC Tomita-Takesaki, explicit) | Delta_1 = exp(−2pi T_BC), J_1 explicit on H_1; modular flow = sigma_t at beta=1 | P | research/121 | **3** |
| 123 | **R-Theorem S.8** (BC DHR superselection) | Hecke projections as superselection sectors with parastatistics from Galois orbits | S | research/122 | 1 |
| 124 | **R-Theorem S.9** (Coleman's theorem on BC side) | On BC spectral line (1+1d), no SSB of continuous symmetry; but discrete SSB at beta=1 survives | S | research/123 | 0 |
| 125 | **R-Theorem S.10** (BC Noether theorem) | Every one-parameter automorphism of A_BC commuting with sigma_t has a conserved charge in H_R | S | research/131 | 0 |
| 126 | **R-Theorem S.11** (BC PCT-spin-statistics, combined) | Combined PCT + spin-statistics from J_1 grading + Z_2 on A_BC | S | research/133 | 3 |
| 127 | **R-Theorem S.12** (BC crossing symmetry) | KMS condition at beta=1 is the BC analog of crossing symmetry; analytic continuation s → 1−s | S | research/134 | 5 |

### Phase 3B: Transpositions — Numbered

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 128 | **R-Theorem 10** (Gauge group from 3 primes) | g_SM as smallest non-trivial Hecke subalgebra symmetry; SU(3) from BC-intrinsic Kirillov construction | C | research/10 | 0 |
| 129 | **R-Theorem L.0** (YM mass gap = BC mass gap) | gamma_1 IS the BC mass gap unconditionally; YM gap transposed | P | research/12 Part B | 0 |
| 130 | **R-Theorem 51** (Coleman-Mandula on BC side) | g = R T_BC + g_int with g_int = g_SM; second independent g_SM derivation | S | research/51 | 0 |
| 131 | **Lemma 51.1-51.3** (BC analogs of CM lemmas) | BC versions of the three key steps of Coleman-Mandula | S | research/51 | 0 |
| 132 | **R-Theorem 51-HLS** (Haag-Lopuszanski-Sohnius on BC side) | Z_2-graded extension of CM: g = g_0 + g_1 with g_1 = Galois-sector fermionic generators | S | research/51 | 0 |
| 133 | **R-Theorem 52** (Higgs mechanism = BC SSB) | The Higgs mechanism IS BC spontaneous symmetry breaking at beta=1; closes "gamma_2 = Higgs" | C | research/52 | 0 |
| 134 | **R-Theorem 53** (Asymptotic freedom = pole of zeta) | alpha_BC(beta) = 4pi/(b_BC(beta−1)) ↔ alpha_s(mu); CC log correction + alpha_s(mu) are the SAME BC fact | S | research/53 | 0 |
| 135 | **R-Theorem 54** (Penrose singularity on BC side) | Trapped projector + modular Raychaudhuri ⇒ spectral singularity at beta=1 ⇒ {gamma_n} subset R | S | research/54 | **4** |
| 136 | **Lemma 2.5** (Modular focusing) | For any rank-finite projector P on H_R, the modular expansion theta(t) of P under sigma_t is monotonically non-decreasing | S | research/54 | 4 |
| 137 | **R-Theorem 55** (BC three-generation unitarity) | O_CKM and O_PMNS unitary on H_3gen; sin theta_23^CKM * sin theta_23^PMNS = pi/(2 sqrt(2) gamma_6) at 0.07% | S | research/55 | 0 |
| 138 | **Theorem 55b** (First-Generation Difference) | sin²theta_12^PMNS − sin²theta_12^CKM = sqrt(2/gamma_4) at 0.0067%; confirms gamma_4 as 1st-gen zero | E | research/79 | 0 |
| 139 | **Theorem U*_BC** (Transposition of Theorem U*) | In perturbative KMS state omega_pert, algebraic functions of O(1) inputs give O(1) outputs; CC hierarchy unreachable algebraically | S | research/13 | 5 |

### Phase 3C: RH as Physical Theorem (5 paths)

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 140 | **RH physical form** (Stone chain — Path 1) | T_BC self-adjoint (Stone) → spec subset R → {gamma_n} subset spec → gamma_n in R. Simplest machinery | C | research/08 §2 | **3** |
| 141 | **RH physical form** (Penrose chain — Path 2) | Trapped projector + modular Raychaudhuri ⇒ spectral singularity at beta=1 ⇒ gamma_n in R | S | research/54 | **4** |
| 142 | **RH physical form** (Atiyah-Singer chain — Path 3) | ind_BC(p) integer ⇒ topological expansion forces real {gamma_n}; strongest because combinatorial | C | research/48, /76 | **2** |
| 143 | **RH physical form** (Kallen-Lehmann + Weil — Path 4) | BC spectral decomposition + Weil criterion ⇒ RH iff non-negative spectral weights; provides iff | S | research/70 | **5** |
| 144 | **RH physical form** (Wigner-Eckart — Path 5, demoted) | Real symmetric in Galois basis ⇒ real spectrum; demoted to consistency constraint | S | research/60 | 3 |
| 145 | **Empirical chain** | Reality of 36 predictions forces reality of gamma_n at precision of each match (5×10⁻⁹ for gamma_1) | E | research/08 §3 | 1,2,3,4,5 |

### Phase 3: Deduction Programme

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 146 | **Dark matter as gamma_5** | Omega_DM/Omega_b = gamma_5/(2pi) at 2.2%; 5 GeV SM-singlet relic | S | research/38 | 0 |
| 147 | **Hierarchy problem is BC-natural** | Delta_BC = 2 vs SM Delta_BG ~ 10³⁴; m_H/M_Pl = exp(−gamma_6)(2pi/gamma_5) at 2% | S | research/39 | 0 |
| 148 | **Three generations from 3-prime Hecke** | Sufficiency from Paper 11 + necessity from 3-prime sub-Hecke; 2 primes → no SU(3); 4 primes → W'/Z' | S | research/40 | 0 |
| 149 | **Dark energy w=−1 from KMS** | Type III_1 forbids quintessence; w(z) is STEP function not smooth | S | research/41 | 0 |
| 150 | **Cosmological coincidence** | "Now" = gamma_2 → gamma_1 level-crossing; rho_Lambda(z>>1) ~ 10⁻⁵⁹ of present | S | research/42 | 0 |
| 151 | **Inflation initial conditions** | Three constraints select gamma_5; r ~ 5×10⁻³ at LiteBIRD/CMB-S4 | S | research/43 | 0 |
| 152 | **Baryogenesis = gamma_5 → gamma_2 transition** | eta_10 = gamma_14/pi² rigorous; inflation and baryogenesis same physics | S | research/44 | 0 |
| 153 | **Strong CP solved by Z_6** | theta_QCD = 0 forced by omega_1 KMS_1 uniqueness; no axion; d_n null at 10⁻³⁰ | P | research/45 | 0 |
| 154 | **Neutrino mass scale** | Sigma m_nu = log(gamma_10)/gamma_15 = 0.06001 eV at 0.019%; normal ordering, Majorana | E | research/46 | 0 |
| 155 | **Fermion mass template** | 3rd gen=PRODUCT, 2nd=RATIO, 1st=DIFFERENCE; universal across masses AND mixing angles | S | research/47 | 0 |

### Phase 3: Operator Dictionary and Uniqueness

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 156 | **Operator dictionary closure** | All 36 formulas are matrix elements of L-hat = log R-hat in spectral basis; dictionary closed under sum/product/ratio/power/log/exp | P | research/167 | 1,3 |
| 157 | **EW sector = moduli space** | 9 EW observables are coordinates on M_geom, a 9-real-dim moduli space of CP²×S² Einstein metrics | S | research/168 | 0 |
| 158 | **dim M_geom = 9** | Forced by Hodge numbers of CP²×S² + SM gauge rank | S | research/175 | 0 |
| 159 | **P_phys = unique vacuum** | Spectral-action minimum P_phys has positive-definite Hessian; unique global minimum | S | research/178 | 0 |
| 160 | **CBB uniqueness conjecture** | Up to unitary equivalence, unique CBB system at beta=1 with real zeta-Laurent coefficients and Brauer-Jones compatibility for k in {2,3,4,6} | S | research/176 | 1 |

### OTOC and Scrambling

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 161 | **Theorem 7.1** (lambda = 0 on all A_BC at beta=1) | OTOC Lyapunov exponent lambda = 0 for entire abelian A_BC at beta=1 (honest negative) | P | research/75 | 0 |
| 162 | **Lemma 1.1** (Bigrading of sigma_t on A_BC) | Every element X of A_BC decomposes by bigrading (Hecke degree, KK mode) | P | research/75 | 0 |

### Meyer Spectral Realisation

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 163 | **Meyer's Theorem** (2005) | {gamma_n} subset spec(T_BC) unconditionally in the distributional sense; no hypothesis on RH required | P (external) | research/201 | 1,2,3,5 |

### Additional Research Results

| # | Name | Statement | Status | Source | RH |
|:--|:-----|:----------|:-------|:-------|:---|
| 164 | **m_tau interface operator** | m_tau closed by anti-hermitian V = lambda tau_1 [log R-hat, Pi_chi]; lambda = 2.695×10⁻³ from spectral action | S | research/183, /187 | 0 |
| 165 | **Six absolute time scale** | t₀ = (log gamma_7)² Gyr; first absolute time scale in physics | E | research/112 | 0 |
| 166 | **Minimal conductor 1729** | 1729 = 7×13×19 = unique minimal field containing all three bridge primes; Hardy-Ramanujan number | S | research/181 | 1 |
| 167 | **ind_BC(e_2) = 0** (honest negative) | Previously claimed ind = 1; proved ind = 0 by three methods; deviation mechanism works with ind = 0 | P | research/90 | 2 |
| 168 | **Supertrace purity** | Functional equation forces Re(Tr_s) = 0 for all Hecke projections, trivialising K_0(A_BC) on Hecke subspace | S | research/90 | 2 |
| 169 | **Shifted Lorentzian deviation** | |dev| = 2 epsilon²/s³, epsilon_crit → 0 | S | research/82 | 2 |

---

## Summary Statistics

| Paper | Entries | Key results |
|:------|:--------|:------------|
| Paper 1 | 6 | Thm K.1, K.3, S.1 (UV finiteness engine) |
| Paper 2 | 0 | (derived consequences only) |
| Paper 3 | 3 | Thm 6.1 (e-Unitarity), Thm 9.1 (Firewall) |
| Paper 4 | 2 | Thm 5.2 (SLOCC), Spectral Gap |
| Papers 5-6 | 0 | (derived consequences only) |
| Paper 7 | 2 | Thm U, Thm U* (CC problem) |
| Paper 8 | 22 | Full YM mass gap chain (Thms 1-8, F.1, I.4.1) |
| Paper 9 | 0 | (mapping paper) |
| Paper 10 | 8 | Scheme-independence (Thm 1, Lemmas A1-A3, 4 routes) |
| Paper 11 | 7 | SM gauge group (Thms 11.1-11.5), K.4, Thm 7.2 |
| Paper 12 | 119 | Identity 12, CC formula, 37 R-Theorems, 5 RH paths, bridges, formulas |
| **Total** | **169** | |

## Most RH-Relevant Entries (by proof path)

### Path 1 (Brauer-KMS): 12 entries
- Identity 12 (#57), BC Theorem 3.1 (#64), Bridge Z/3Z (#85), Bridge k=4/k=6 (#86-87), Laurent coefficients (#82-84), Operator dictionary (#156), CBB uniqueness (#160), Meyer (#163), 1729 (#166)

### Path 2 (Atiyah-Singer): 9 entries
- R-Theorem D.1 (#90), Lemma 7.1 (#91), Theorem 3.3 (#92), R-Theorem C.1 (#97), R-Theorem C.2 (#98), ind_BC(e_2)=0 (#167), Supertrace purity (#168), Shifted Lorentzian (#169)

### Path 3 (Stone): 14 entries
- Quantization of R (#55), Identity 12 (#57), Identity 14 (#59), R-Theorem QM.1-QM.5 (#99-105), R-Theorem S.1/S.6/S.7 (#116,121,122), R-Theorem GR.3 (#108), RH physical form (#140)

### Path 4 (Penrose): 5 entries
- R-Theorem 54 (#135), Lemma 2.5 modular focusing (#136), R-Theorem GR.1 (#106), R-Theorem GR.4 (#109), RH physical form (#141)

### Path 5 (CM-trace / Kallen-Lehmann): 7 entries
- R-Theorem S.5 (#120), R-Theorem S.12 (#127), CC formula (#60), CC hierarchy (#81), Theorem U* (#15,#139), R-Theorem D.5 (#96)

---

*169 total entries across 12 papers. Paper 8 dominates on theorem count*
*(22 entries for the YM mass gap). Paper 12 dominates on total results*
*(119 entries spanning all phases). 47 entries have direct RH relevance*
*(paths 1-5). The Atiyah-Singer path (Path 2) has the strongest*
*combinatorial constraint via Lemma 7.1; the Stone path (Path 3) has*
*the most supporting infrastructure (14 entries).*
