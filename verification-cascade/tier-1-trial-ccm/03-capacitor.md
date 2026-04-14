# CCM Zeta Spectral Triples -- Verification Capacitor v1

*Charged toolkit for the Tier 1 CCM verification run. Contains: domain knowledge, kill list, proof chain, correspondences, patterns, operations, escalation routes, and background toolkit cards. Single file -- no external reads needed at runtime beyond the target paper itself.*

*Generated: 2026-04-13. Target: CCM 2025 (arXiv:2511.22755). Mode: VERIFY (preprint).*
*Charge level: 7 steps, 4 correspondences, 0 target-specific kills (first run), 37 imported kills (36 framework + K-T4-1).*
*Amplification from Tier 4: LESSON-1 (standing hypotheses), TK-6 (Galerkin gnrc), TK-7 (gsr sufficiency), K-T4-1 (Teschl Galerkin failure).*

---

## META -- Capacitor state

| Field | Value |
|---|---|
| Version | v1 (pre-run) |
| Target | CCM 2025, arXiv:2511.22755 (PREPRINT) |
| Also | CCM 2024, arXiv:2310.18423 (published precursor) |
| Also | CvS 2025, arXiv:2511.23257 (alternative realization, published CMP) |
| Mode | VERIFY (Tier A) -- OPEN |
| Steps in target | 7 |
| SURVIVED | 0 |
| WEAKENED | 0 |
| BROKEN | 0 |
| PENDING | 7 |
| Kills (target-specific) | 0 (first run) |
| Kills (imported) | 37 (36 framework + 1 from Tier 4) |
| Escalations triggered | 0 |

---

## LEGEND

Standard abbreviations used throughout this capacitor. Read once, apply everywhere.

```
CCM   := Connes-Consani-Moscovici (arXiv:2511.22755, 2025)
CvS   := Connes-van Suijlekom (arXiv:2511.23257, 2025)
CF    := Caratheodory-Fejer (Toeplitz self-adjointness / rank-one perturbation)
QW    := prolate matrix QW_lambda^N
E_N+  := even sector of Sonin space at truncation level N
D_N   := CCM operator on E_N+ (spectral realization of near-Riemann-zeros)
Xi    := Riemann Xi function (completed zeta, entire, zeros = Riemann zeros)
xi_N  := minimum eigenvector of QW_lambda^N
xi-hat_N := Fourier transform of xi_N (eigenvalues of D_N = zeros of xi-hat_N)
gamma := parity involution (splits Hilbert space into even/odd sectors)
T     := Weil explicit formula operator (defines the T-inner product)
mu_N  := minimum eigenvalue of QW_lambda^N
L     := period parameter, L = 2 log(lambda)
AE    := almost-everywhere (simplicity argument)

gsrc  := generalized strong resolvent convergence (Boegli, VERIFIED Tier 4)
DC    := discrete compactness (Boegli, VERIFIED Tier 4)
SE    := spectral exactness (Boegli Thm 2.6, VERIFIED Tier 4)
KLMN  := Kato-Lions-Lax-Milgram-Nelson (self-adjointness via form bound)
RK    := Rellich-Kondrachov (compact Sobolev embedding)
ITPFI := Infinite Tensor Product of Factors of type I

SP    := Spectral (domain/pillar)
GE    := Geometric (domain/pillar)
AL    := Algebraic (domain/pillar)
IN    := Information-theoretic (domain/pillar)

LB    := Load-Bearing (step whose failure collapses downstream)
RH    := Riemann Hypothesis
PW    := Paley-Wiener (space of entire functions of exponential type)
RKHS  := Reproducing Kernel Hilbert Space
SBF   := Segal-Bargmann-Fock (space, used in CvS alternative)
```

---

## KILLS

### Target-specific kills (CCM)

```
(none yet -- first run)
```

### Imported kills from Tier 4 (Boegli verification)

```
K-T4-1: Direct-Teschl-2.7-invocation-with-Galerkin-projections
  WHAT: Citing Teschl Lemma 2.7 directly with J_n = P_N for gnrc
  WHY:  Standing hypothesis (2.1) requires ||J_n*J_n - I|| -> 0 in operator norm;
        fails for orthogonal projections onto proper subspaces (||P_N - I|| = 1 for all N)
  PATTERN: External-source-inconsistency / Standing-hypothesis-failure
  RE-ENTRY: If Teschl publishes revised version with (2.2) as standing hypothesis,
            or if a gsrc variant of Lemma 2.7 is proved
  REPAIR: Use Chatelin Galerkin gnrc (1983, Ch. 3) instead. Keep Teschl for KLMN closability only.
  LESSON: Always verify standing hypotheses of cited theorems (LESSON-1).
```

### Imported framework kills (relevant subset)

**Directly relevant to the CCM/RH domain:**

```
K-RH-1: Coboundary-gap-v1-proof
  WHAT: Original v1 RH proof via cohomological approach
  WHY:  Gap in archimedean estimate (original proof incomplete)
  NOTE: Resolved via CCM + Boegli bypass (Layer 3+4 of RH chain).
        THIS is why CCM is load-bearing -- it was the bypass route for K-RH-1.

K-RH-2: Direct-Hilbert-space-RH-proof
  WHAT: Attempt to prove RH directly in Hilbert space without spectral realization
  WHY:  Circular (assumes spectral realization without proving it)
  NOTE: Shows why CCM operators (external spectral realization) are needed.
```

**Pattern-relevant kills (standing hypothesis failures in other domains):**

```
K-YM-3: Osterwalder-Schrader-direct-application
  WHAT: Directly citing OS axioms without checking domain compatibility
  WHY:  OS requires Euclidean field theory axioms; lattice theory satisfies
        discretized versions that require separate verification
  PATTERN: Standing-hypothesis-failure (same pattern as K-T4-1)
  RELEVANCE: CCM may have analogous standing-hypothesis issues with cited results
```

**Other framework kills (for agent context, not directly relevant):**
- K-YM-1 through K-YM-8: Yang-Mills domain (irrelevant to CCM verification)
- K-PvNP-1 through K-PvNP-20: P vs NP domain (irrelevant)
- K-BSD-1 through K-BSD-7: BSD domain (irrelevant)

**The full 36-kill list is in the compiled ORA generator (03-ora-generator-compiled.md section 1).** Agents should reference it if pattern-matching is needed but should not spend tokens re-reading irrelevant kills.

---

## CHAIN -- 7 steps with dependencies and status

```
chain[7]{step,type,statement,deps,LB,risk,status}:
  1*,Foundation,"T-inner-prod-well-defined-and-positive-definite-on-E_N+(Weil-explicit-formula)",--,*,Medium,PENDING
  2*,Spectral,"QW_lambda^N-minimum-eigenvalue-simple-and-even(prolate-matrix)",1,*,Medium,PENDING
  3*,Self-adj,"CF-rank-one-perturbation-preserves-self-adjointness-of-D_N(Thm4.2)",1;2,*,Low-Medium,PENDING
  4*,Symmetry,"T-commutes-with-gamma(Lemma5.2i):Tgamma=gammaT-so-E_N+-invariant",1,*,Low,PENDING
  5*,Core,"Eigenvalues-of-D_N=zeros-of-xi-hat_N(Thm5.10:THE-CORE-CLAIM)",1;2;3;4,*,High,PENDING
  6*,Convergence,"xi-hat_N->Xi-uniformly-on-compact-subsets(Lemma7.3)",1;2,*,Medium,PENDING
  7,Numerical,"Eigenvalues-match-gamma_n-to-10^{-55}-at-N=6",5,,Low,PENDING
```

Dependency adjacency:
```
1 -> 2 -> 3 -> 5
1 -> 4 -> 5
1 -> 2 -> 6
5 -> 7
5 + 6 -> RH.Layer5 (Hurwitz zero convergence)
ALL -> RH.Layer1 (CCM IS Layer 1)
```

Critical path: 1 -> 2 -> 3 -> 5. If Step 5 SURVIVES, the core spectral identification is verified.
Convergence path: 1 -> 2 -> 6. If Step 6 SURVIVES, the Hurwitz argument is enabled.
Both paths required for the full RH proof.

Risk-ordered priority: Step 5 (High) > Steps 1, 2, 6 (Medium) > Step 3 (Low-Medium) > Step 4 (Low) > Step 7 (Low).

---

## CORRESPONDENCES -- CCM concepts mapped to 4 pillars

### Concept: T-inner product (Weil explicit formula form)

| Domain | Image | Key property | Reference |
|---|---|---|---|
| SP | Weil quadratic form: <f, g>_T = sum over primes of Lambda(p)-weighted correlations | Positivity encodes prime distribution | CCM 2025 Section 2 |
| GE | Period integral: <f, g>_T as integration of f * g over a period domain with von Mangoldt measure | Geometric measure on primes | Weil 1952 |
| AL | Hecke pairing: <f, g>_T factors through Hecke operators T_p, one per prime | Algebraic structure of prime decomposition | Hecke 1937 |
| IN | Mutual information of BC states: <f, g>_T = mutual information I(f; g) in the Bost-Connes KMS state | Information-theoretic interpretation of prime correlations | Paper 13 Layer 2 |

### Concept: D_N operator (spectral realization of near-zeros)

| Domain | Image | Key property | Reference |
|---|---|---|---|
| SP | Self-adjoint generator: D_N generates a one-parameter group on E_N^+ | Eigenvalues real, spectral theorem applies | CCM 2025 Theorem 4.2 |
| GE | Derivative on Sonin space: D_N = d/dx modified by CF rank-one correction | Geometric flow on reproducing kernel space | CCM 2025 Section 4 |
| AL | CCM spectral triple: (A_N, H_N, D_N) is a spectral triple in Connes' NCG sense | Algebraic framework for noncommutative geometry | Connes 1994 |
| IN | Fisher information operator: D_N encodes the Fisher information of the spectral distribution | Information geometry of eigenvalue distribution | Amari-Nagaoka 2000 |

### Concept: Even sector E_N^+

| Domain | Image | Key property | Reference |
|---|---|---|---|
| SP | Spectral projection: E_N^+ = (1+gamma)/2 applied to the full space | Reduces to parity-even functions | CCM 2025 Section 5 |
| GE | Parity-invariant subspace: functions f with f(-x) = f(x) in the Sonin space | Geometric symmetry reduction | Standard |
| AL | Z/2-grading: the parity involution gamma gives a Z/2-graded Hilbert space | Algebraic grading | Connes 1994 |
| IN | Symmetric channel: the even sector corresponds to symmetric quantum channels (invariant under bit flip) | Information-theoretic symmetry | Wilde 2013 |

### Concept: Eigenvalue identification (Theorem 5.10)

| Domain | Image | Key property | Reference |
|---|---|---|---|
| SP | Point spectrum = zeros: eigenvalues of D_N are exactly the zeros of xi-hat_N | Spectral identification via Fourier transform | CCM 2025 Theorem 5.10 |
| GE | Nodal sets of eigenfunctions: zeros of xi-hat_N are nodal points of the eigenfunction in frequency space | Geometric interpretation of zeros | Courant-Hilbert |
| AL | Characteristic polynomial roots: in the finite-dimensional case, eigenvalues of D_N are roots of det(D_N - lambda I) = 0 | Algebraic eigenvalue theory | Standard linear algebra |
| IN | Capacity of spectral channel: eigenvalues encode the channel capacity at each frequency | Information capacity at spectral points | Shannon 1948 |

### Concept: Uniform convergence (Lemma 7.3)

| Domain | Image | Key property | Reference |
|---|---|---|---|
| SP | Spectral convergence: eigenvector Fourier transforms converge to Xi | Spectral stability under approximation | CCM 2025 Lemma 7.3 |
| GE | Compact-open topology: xi-hat_N -> Xi in the compact-open topology on holomorphic functions | Geometric convergence on compact sets | Montel's theorem |
| AL | Algebraic approximation: the prolate expansion approximates the zeta function algebraically | Polynomial-like approximation | Slepian 1961-83 |
| IN | Channel fidelity: the approximate channel xi-hat_N has fidelity -> 1 with the true channel Xi | Information fidelity convergence | Quantum info |

---

## PATTERNS -- Six Patterns analysis per load-bearing step

### Step 1* (T-inner product): P4 (Topological Rigidity)

Weil positivity IS a topological rigidity: the positivity of the T-inner product is **protected by the functional equation** of the Riemann zeta function. The functional equation ensures that the Weil distribution W satisfies W(f * f~) >= 0 for all test functions f (where f~ is the Fourier dual). This is a topological constraint -- it cannot be perturbed away.

**Attack angle**: is the functional equation used explicitly or implicitly in the positivity proof? If implicitly, flag the assumption. Check: does the positivity hold term-by-term (for each prime p), or only as a sum over all primes? If the latter, the proof must handle the summation carefully.

### Step 2* (minimum eigenvalue simplicity): P3 (Analytic Continuation)

The simplicity of the minimum eigenvalue may depend on analytic continuation in the bandwidth parameter lambda. If QW_lambda^N depends analytically on lambda, eigenvalue crossings occur on a codimension-1 set, so simplicity is generic. But **the specific lambda used by CCM must be checked**.

**Attack angle**: does CCM prove simplicity for a specific lambda, or for generic lambda? If generic, how is the specific lambda verified to be generic?

### Step 3* (CF self-adjointness): P4 (Topological Rigidity)

Rank-one perturbation preserves self-adjointness by a **discrete index argument**: the Fredholm index of D_N - D is 0 (rank-one perturbation), so D_N has the same deficiency indices as D. If D is self-adjoint (deficiency indices (0,0)), so is D_N. This is topological -- small perturbations cannot change deficiency indices.

**Attack angle**: does the rank-one perturbation actually have Fredholm index 0? The perturbation is |D*xi_N><eta_N|, which maps any vector to a multiple of D*xi_N. Is D*xi_N in the Hilbert space? Is eta_N? If either is outside the space, the perturbation is not well-defined.

### Step 4* (T gamma = gamma T): P0 (Direct Computation)

This should be a direct computation. The parity involution gamma acts by f(x) -> f(-x) (or its Sonin space analogue). The Weil operator T acts by convolution with the von Mangoldt function. Commutativity should follow from the fact that the von Mangoldt function is even (Lambda(n) depends on |n|, not on the sign of n).

**Attack angle**: is the von Mangoldt-weighted kernel in the T-inner product actually symmetric under the parity involution? Check for factors of (-1)^k that might break commutativity.

### Step 5* (eigenvalue identification): P5 (Strategic Inversion)

The identification goes through **zeta regularization of the prolate expansion**: D_N is constructed so that its eigenvalue equation D_N f = lambda f is equivalent to xi-hat_N(lambda) = 0. This is an inversion: instead of computing eigenvalues from the operator, the operator is designed to make its eigenvalues equal to specified zeros.

**Attack angle**: the inversion is the core claim. Verify that the design actually works: does D_N f = lambda f really force xi-hat_N(lambda) = 0? Or does the converse also need to be checked (every zero of xi-hat_N is an eigenvalue)?

### Step 6* (uniform convergence): P1 (Geometric Reinterpretation)

Convergence in the RKHS norm (Sonin space) implies convergence in the PW space (Paley-Wiener, via Fourier transform), which implies uniform convergence on compacts (via the RKHS property: point evaluation is continuous). This is P1: convergence in a larger/stronger space implies convergence in the smaller/weaker one.

**Attack angle**: is the Fourier transform an isometry from the Sonin space (with T-inner product) to the PW space? If not an isometry, what is the norm distortion? Is the distortion bounded uniformly in N?

---

## OPERATIONS -- Key operations in CCM's construction

| Operation | Spectral | Geometric | Algebraic | Information |
|---|---|---|---|---|
| T-inner product <f,g>_T | Spectral weight by primes | Period integral with von Mangoldt measure | Hecke operator pairing | Mutual information in BC state |
| Prolate matrix QW_lambda^N | Finite-rank spectral approximation | Truncated period matrix | N x N matrix of prime interactions | Channel capacity matrix |
| Min eigenvector xi_N | Ground state of QW | Minimizer of Rayleigh quotient | Perron-Frobenius vector | Minimum entropy state |
| CF perturbation D - rank1 | Rank-one spectral modification | Geometric flow + correction | Algebraic completion to spectral triple | Channel correction |
| Parity projection (1+gamma)/2 | Spectral projection onto even sector | Symmetry reduction | Z/2-grading projection | Symmetric channel selection |
| Fourier transform xi_N -> xi-hat_N | Spectral to frequency domain | Point evaluation in RKHS | Algebra homomorphism PW -> C | Channel output measurement |
| Limit N -> infinity | Spectral convergence D_N -> D_inf | Geometric limit of Sonin spaces | Algebraic direct limit | Channel capacity limit |
| Hurwitz (downstream, Layer 5) | Zero convergence | Argument principle limit | Root convergence of polynomials | Capacity convergence |

---

## FRAMEWORK INTERFACE

### CCM -> RH proof chain

| CCM step | RH layer | What it provides |
|---|---|---|
| Step 1 (T-inner product) | **Layer 1 foundation** | The Hilbert space on which everything is defined |
| Step 2 (min eigenvalue) | **Layer 1 setup** | The eigenvector that defines the spectral realization |
| Step 3 (self-adjointness) | **Layer 1 guarantee** | D_N is self-adjoint -> eigenvalues are real -> zeros are on the critical line |
| Step 4 (parity symmetry) | **Layer 1 symmetry** | Even sector is well-defined -> reduction to E_N^+ is valid |
| Step 5 (eigenvalue identification) | **Layer 1 core** | eigenvalues = zeros of xi-hat_N: the spectral identification that IS the RH approach |
| Step 6 (uniform convergence) | **Layer 1 -> Layer 5 bridge** | xi-hat_N -> Xi enables Hurwitz zero convergence |
| Step 7 (numerical) | Layer 1 confirmation | Empirical check, not load-bearing for the proof |

**Combined**: ALL steps close RH Layer 1. Steps 5 + 6 together bridge to Layer 5 (Hurwitz).

### RH proof chain -> CCM (what Paper 13 feeds INTO CCM)

| Paper 13 component | CCM hypothesis used |
|---|---|
| ITPFI structure (Layer 2) | Provides the tensor product structure for the operator construction |
| Archimedean estimates (Layer 3.1) | Strengthens the convergence rates for Step 6 |
| Eigenvector estimates (Layer 3.2) | Provides uniform bounds on xi_N for Step 2 |
| H^1 norm bound (Layer 3.3) | Provides DC verification via Rellich-Kondrachov |
| CF uniformity (Layer 3.4) | Provides resolvent convergence for Boegli (Layer 4, VERIFIED) |
| Boegli spectral exactness (Layer 4, VERIFIED) | Provides spec(D_inf) = lim spec(D_N) -- no spurious zeros |

---

## ESCALATION ROUTES (pre-identified, per step)

### Step 1 (T-inner product positivity)

| Tier | Route | Source |
|---|---|---|
| B | Li's positivity criterion: <f,f>_T >= 0 iff Li's coefficients lambda_n >= 0 for all n. Check whether CCM's positivity follows from Li's criterion. | Li 1997, Bombieri-Lagarias 1999 |
| B | Connes-van Suijlekom: CvS uses standard L^2 inner product on Segal-Bargmann-Fock space, bypassing the T-inner product entirely. | CvS 2025 |
| C | Construct positivity from ITPFI: the tensor product structure of omega_1 provides a natural positive form. Prove it equals the T-inner product. | Paper 13 Layer 2 |

### Step 2 (eigenvalue simplicity)

| Tier | Route | Source |
|---|---|---|
| B | Analytic perturbation theory (Kato Ch. II): eigenvalues analytic in lambda -> simplicity generic. | Kato 1966 |
| B | Perron-Frobenius: if QW_lambda^N has positive entries, minimum eigenvalue of inverse is simple. | Classical |
| C | Handle multiplicity directly: modify RH argument for non-simple eigenvalues. | Paper 13 modified Layer 1 |

### Step 3 (CF self-adjointness)

| Tier | Route | Source |
|---|---|---|
| B | Kato-Rellich: rank-one perturbation with relative bound < 1. | Reed-Simon II, Thm X.12 |
| B | KLMN form-bounded perturbation: form bound < 1 -> self-adjoint. | Reed-Simon II, Thm X.17 |
| C | Friedrichs extension: construct D_N as self-adjoint ab initio. | Friedrichs extension theorem |

### Step 4 (T gamma = gamma T)

| Tier | Route | Source |
|---|---|---|
| B | Direct Fourier-side verification. | Standard |
| C | If fails: restructure CCM to avoid parity decomposition (would be major). | -- |

### Step 5 (eigenvalue identification)

| Tier | Route | Source |
|---|---|---|
| B | Paley-Wiener + characteristic function identification. | Koosis 1988 |
| B | Connes-van Suijlekom alternative spectral identification. | CvS 2025 |
| C | Direct ITPFI spectral identification: read eigenvalues from tensor factors. | Paper 13 Layer 2 |

### Step 6 (uniform convergence)

| Tier | Route | Source |
|---|---|---|
| B | Slepian prolate function estimates. | Slepian 1961-83 |
| B | Sobolev embedding: H^1 convergence -> uniform convergence. | Adams-Fournier 2003 |
| C | Bypass via Boegli spectral exactness (VERIFIED): spec convergence without needing function convergence. | Boegli Thm 2.6 (Tier 4 VERIFIED) |

### Step 7 (numerical)

| Tier | Route | Source |
|---|---|---|
| B | Independent computation in PARI/GP or SageMath. | -- |
| C | Not needed (confirmatory, not LB). | -- |

---

## BACKGROUND TOOLKIT -- Five-field cards

### TK-1: Weil explicit formula

| Field | Content |
|---|---|
| **WHAT** | For a suitable test function f, the Weil explicit formula relates sums over primes to sums over Riemann zeros: sum_{rho} f-hat(rho) = f-hat(0) + f-hat(1) - sum_p sum_k (log p / p^{k/2}) [f(k log p) + f(-k log p)] + integral term. |
| **WHY** | The T-inner product is derived from this formula. Positivity of the T-inner product is equivalent to the non-negativity of the Weil distribution. |
| **DATA** | Weil 1952, "Sur les 'formules explicites' de la theorie des nombres premiers." Bombieri 2000, Clay Millennium lecture. |
| **USE** | Foundation for Step 1 verification. Check that CCM's T-inner product correctly implements the Weil formula. |
| **STATUS** | CLASSICAL (Weil 1952, widely verified) |

### TK-2: Prolate spheroidal wave functions

| Field | Content |
|---|---|
| **WHAT** | The prolate spheroidal wave functions (PSWFs) are eigenfunctions of the time-frequency concentration operator: restrict to interval [-L/2, L/2], Fourier transform, restrict to bandwidth [-W, W], Fourier transform back. The operator QW is this composition. |
| **WHY** | CCM's prolate matrix QW_lambda^N is a finite-rank version of the PSWF concentration operator, where the "bandwidth" is determined by the primes up to p_N. |
| **DATA** | Slepian-Pollak 1961, Landau-Pollak 1961-62, Slepian 1964-83. Modern: Osipov-Rokhlin-Xiao, "Prolate Spheroidal Wave Functions of Order Zero" (2013). |
| **USE** | Background for Steps 2 and 6. The prolate approximation (Lemma 7.2) and convergence (Lemma 7.3) rely on PSWF theory. |
| **STATUS** | CLASSICAL (60+ years of development) |

### TK-3: Caratheodory-Fejer theory

| Field | Content |
|---|---|
| **WHAT** | The CF theory provides conditions under which Toeplitz-type operators are self-adjoint. In the rank-one perturbation context: if D is self-adjoint and V = |u><v| is a rank-one operator with u, v in dom(D), then D + V is self-adjoint on dom(D). |
| **WHY** | CCM's D_N is constructed as D plus a rank-one perturbation. CF theory (or Kato-Rellich) ensures self-adjointness is preserved. |
| **DATA** | Classical: Grenander-Szego, "Toeplitz Forms and Their Applications" (1958). Bottcher-Silbermann, "Toeplitz Matrices" (1999). For unbounded perturbations: Kato, Perturbation Theory, Ch. V. |
| **USE** | Foundation for Step 3 verification. Check that the CF conditions hold for CCM's specific construction. |
| **STATUS** | CLASSICAL (bounded case) / REQUIRES CHECKING (unbounded D case) |

### TK-4: Paley-Wiener space

| Field | Content |
|---|---|
| **WHAT** | The Paley-Wiener space PW_sigma is the space of entire functions of exponential type at most sigma that are L^2-restricted to the real line. The Fourier transform is an isometry from L^2([-sigma, sigma]) to PW_sigma. |
| **WHY** | The Fourier transform of xi_N lives in a Paley-Wiener-type space. The eigenvalue identification (Step 5) interprets eigenvalues as zeros of an entire function in this space. |
| **DATA** | Paley-Wiener 1934. Koosis, "The Logarithmic Integral" (1988). Young, "An Introduction to Nonharmonic Fourier Series" (2001). |
| **USE** | Background for Step 5. The spectral identification requires xi-hat_N to be in a PW space. |
| **STATUS** | CLASSICAL |

### TK-5: Hurwitz's theorem (downstream, for context)

| Field | Content |
|---|---|
| **WHAT** | If f_n -> f uniformly on compacts, f is not identically zero, and f_n have zeros z_n^(k), then zeros of f are limits of zeros of f_n (and conversely, every limit of zeros is a zero of f). |
| **WHY** | This is RH Layer 5, downstream of CCM. The connection: CCM Step 6 gives xi-hat_N -> Xi uniformly on compacts; Hurwitz gives eigenvalues of D_N -> zeros of Xi. |
| **DATA** | Hurwitz 1893. Conway, Functions of One Complex Variable II, Thm 2.5. |
| **USE** | Context only. Not a verification target in THIS run (verified at Layer 5). |
| **STATUS** | CLASSICAL (130+ years old) |

### TK-6: Galerkin norm resolvent convergence (from Tier 4)

| Field | Content |
|---|---|
| **WHAT** | For operators with compact resolvent and Galerkin projections P_N with P_N -> I strongly, the Galerkin resolvents converge in norm: ||(P_N T P_N - z)^{-1} P_N - (T-z)^{-1}|| -> 0. |
| **WHY** | Provides gnrc for CCM operators WITHOUT needing Teschl's condition (2.1). Classical route that was the REPAIR for K-T4-1 in Tier 4. |
| **DATA** | Chatelin, Spectral Approximation of Linear Operators, 1983, Ch. 3. Also Stummel 1970-73, Vainikko 1976. |
| **USE** | If CCM uses Galerkin-type projections with compact resolvent, this provides gnrc directly. Also relevant if CCM cites results that require gsrc. |
| **STATUS** | CLASSICAL (textbook-level, Tier 4 VERIFIED) |

### TK-7: gsr suffices for spectral inclusion (from Tier 4)

| Field | Content |
|---|---|
| **WHAT** | Boegli's Theorem 2.3 (spectral inclusion) requires only gsr (strong resolvent convergence), not gnr (norm). |
| **WHY** | Discovered during Tier 4. If CCM's spectral convergence route needs only spectral inclusion (not spectral exactness), gsr is an easier fallback. |
| **DATA** | Boegli 2017, Thm 2.3 proof uses dominated convergence, not norm estimates. |
| **USE** | Amplification: if gnrc is hard to verify for CCM operators, gsr may suffice. |
| **STATUS** | ESTABLISHED (Tier 4 finding) |

### TK-8: Boegli spectral exactness (VERIFIED at Tier 4)

| Field | Content |
|---|---|
| **WHAT** | gsrc + DC -> spectral exactness: spec(T) = lim spec(T_n), no spurious eigenvalues, no missing eigenvalues. |
| **WHY** | Boegli Thm 2.6 is VERIFIED (Tier 4, all 5 steps SURVIVED + LOCK). CCM's eigenvalue convergence ultimately routes through Boegli at RH Layer 4. |
| **DATA** | Boegli 2017, Thm 2.6. Tier 4 verification: 5/5 SURVIVED, 5/5 LOCKED, 1 kill (K-T4-1), 0 broken. |
| **USE** | Step 6 escalation route (Tier C): if xi-hat_N -> Xi fails, Boegli can provide eigenvalue convergence directly from operator convergence, bypassing the function-level convergence entirely. |
| **STATUS** | VERIFIED (Tier 4, independently checked) |

### TK-9: Spectral triples in NCG

| Field | Content |
|---|---|
| **WHAT** | A spectral triple (A, H, D) consists of a *-algebra A represented on a Hilbert space H, and a self-adjoint operator D (the Dirac operator) such that [D, a] is bounded for all a in A. The spectral triple encodes the geometry of a noncommutative space. |
| **WHY** | CCM's construction produces spectral triples (A_N, E_N^+, D_N). The self-adjointness of D_N (Step 3) and the boundedness of commutators are part of the spectral triple axioms. |
| **DATA** | Connes, "Noncommutative Geometry" (1994). Connes-Marcolli, "Noncommutative Geometry, Quantum Fields and Motives" (2008). |
| **USE** | Background context. Agents should know what a spectral triple is to understand why D_N is constructed the way it is. |
| **STATUS** | CLASSICAL (30+ years, Connes' foundational framework) |

### TK-10: Bost-Connes system

| Field | Content |
|---|---|
| **WHAT** | The Bost-Connes system is a quantum statistical mechanical system whose partition function is the Riemann zeta function. It has a unique KMS state omega_beta for each inverse temperature beta > 1. At beta = 1, the KMS state omega_1 is the critical state. |
| **WHY** | Paper 13's RH proof works through the Bost-Connes KMS state omega_1. CCM's construction interfaces with Paper 13 through this state. The ITPFI structure of omega_1 (Layer 2) provides the tensor product decomposition. |
| **DATA** | Bost-Connes 1995, Selecta Mathematica. Connes-Marcolli 2006, JAMS. Laca-Larsen-Neshveyev 2015. |
| **USE** | Interface context. Agents should understand HOW CCM connects to Paper 13. |
| **STATUS** | CLASSICAL (published, well-established) |

---

## AUTHORS' HONEST STATEMENTS

### From CCM 2025

Key self-identified issues and limitations from the paper:

1. **Section 7 Outlook (p.28)**: The authors identify the "main remaining obstacle" as rigorous UV asymptotics matching. This is a SELF-FLAGGED gap. **Verifiers must determine whether any of the 7 load-bearing steps depend on material the authors themselves consider unresolved.**

2. **Prolate approximation**: The authors note that the convergence xi_N -> prolate function (Lemma 7.2) is proved under specific conditions on the bandwidth parameter lambda. **Check whether these conditions are always satisfied or only for large N.**

3. **Numerical evidence**: The authors emphasize the numerical match to 10^{-55} as strong evidence. **This is evidence, not proof. Do not let numerical agreement substitute for logical verification.**

### From CCM 2024 (precursor)

The precursor paper (arXiv:2310.18423) is PUBLISHED in Annals of Functional Analysis. This provides a foundation that has been peer-reviewed. **Verifiers should distinguish between results that originate in the published 2024 paper and results that are new in the 2025 preprint.** New results in the 2025 preprint deserve higher scrutiny.

### From Connes-van Suijlekom 2025

CvS provides an alternative approach via the Segal-Bargmann-Fock space. CvS is PUBLISHED in Communications in Mathematical Physics. **If CCM's approach has a gap that CvS's approach does not, the RH proof can potentially route through CvS.** This is a pre-identified Tier B escalation.

---

## LESSON AMPLIFICATION (from Tier 4)

### LESSON-1: Always verify standing hypotheses of cited theorems

**Source**: Tier 4 pilot (Boegli verification), Step 5, K-T4-1.

**What happened**: Teschl's Lemma 2.7 requires standing hypothesis (2.1): ||J_n*J_n - I|| -> 0 in operator norm. This appears once at the section header, not at the theorem statement. The hypothesis fails for Galerkin projections (||P_N - I|| = 1 for all N). The theorem itself is correct, but it cannot be cited in the RH proof's context.

**Amplification to CCM**: CCM cites results from multiple domains:
- Prolate function theory (Slepian et al.)
- Operator theory (Kato, Reed-Simon)
- Number theory (Weil explicit formula)
- Spectral geometry (Connes' NCG)

Each citation is an attack surface for standing-hypothesis failure. The cited theorem may be correct but its hypotheses may not hold in CCM's non-standard context (T-inner product instead of L^2, Sonin space instead of Schwartz space, etc.).

**Standing instruction for all agents**: When any step cites an external result, the agent MUST:
1. Identify the cited result's complete hypotheses (including standing/ambient)
2. Verify that each hypothesis holds in CCM's specific context
3. If a hypothesis fails: WEAKENED with "standing-hypothesis-failure" pattern

---

## INDEX -- Source access pointers

```
@FETCH-1: arXiv:2511.22755 (CCM 2025, target paper)
  URL: https://arxiv.org/abs/2511.22755
  Key sections: Sec 2 (Sonin space), Sec 4 (Thm 4.2, self-adjointness),
    Sec 5 (Lemma 5.2, Thm 5.10), Sec 7 (Lemmas 7.2-7.3, Outlook)
  Download via: WebFetch https://arxiv.org/pdf/2511.22755

@FETCH-2: arXiv:2310.18423 (CCM 2024, published precursor)
  URL: https://arxiv.org/abs/2310.18423
  Key sections: Foundation results cited by CCM 2025
  Download via: WebFetch https://arxiv.org/pdf/2310.18423

@FETCH-3: arXiv:2511.23257 (CvS 2025, alternative realization)
  URL: https://arxiv.org/abs/2511.23257
  Key sections: Segal-Bargmann-Fock realization, Tier B escalation
  Download via: WebFetch https://arxiv.org/pdf/2511.23257

@FETCH-4: Paper 13 RH proof chain (for framework interface)
  Path: paper13-rh/preprint/00-proof-skeleton.md
  Key sections: Layer 1 description, CCM dependency

@FETCH-5: Paper 13 Sections 8-9 (where CCM is applied)
  Path: paper13-rh/preprint/sections-06-10.md
  Key sections: Section 8 (spectral realization), Section 9 (Hurwitz)

@FETCH-6: Boegli verification (Tier 4, COMPLETED)
  Path: verification-cascade/tier-4-trial-boegli/output/blackboard.md
  Key sections: LESSON-1, K-T4-1, TK-6, TK-7

@FETCH-7: Framework kills and corrections
  Path: paper13-rh/preprint/sections-11-14.md
  Key sections: Sections 11-14 (honest negatives, corrections, verification)
```

---

## HONEST ASSESSMENT

This is a preprint by Alain Connes (Fields Medal), Caterina Consani, and Henri Moscovici -- a top-tier author team with decades of experience in operator algebras, noncommutative geometry, and spectral theory. Connes has been working on the RH via NCG for 20+ years. This paper represents the latest iteration of that programme.

**Expect most steps to SURVIVE.** The authors' track record and the depth of the underlying programme strongly suggest that the core mathematical ideas are correct. The spectral realization approach has been refined over multiple papers.

**Watch for three things:**

1. **Standing-hypothesis issues (LESSON-1)**: The #1 risk, especially for a preprint. CCM cites results from multiple domains; each citation's hypotheses must hold in CCM's non-standard spaces. This is the pattern that caught K-T4-1 in Tier 4.

2. **Presentation gaps**: Preprints often have steps that are "clear to the authors" but not fully written out. These are CLOSABLE but must be flagged -- a Clay referee will flag them too.

3. **The Outlook gap (p.28, section 7)**: The authors themselves identify an unresolved issue. Determine whether any load-bearing step depends on this unresolved material.

**What we do NOT expect to find**: a fundamental mathematical error in a paper by Connes, Consani, and Moscovici. The probability is LOW (~5-10%). But verification is the point. We verify what we depend on, not what we doubt.

**The preprint paradox**: the authors' caliber reduces P(fundamental gap) but does NOT reduce P(standing-hypothesis gap) or P(presentation gap). Those are format issues, not competence issues. Apply LESSON-1 everywhere.

**The discipline is the product. The discovery, if any, is a bonus.**

---

## MERGE LOG

| Date | Run | Cards added | Cards updated | Kills added | Escalations | Notes |
|---|---|---|---|---|---|---|
| 2026-04-13 | v1 build | 10 TK cards | 0 | 0 target-specific, 37 imported | 0 | Initial capacitor build. Amplified from Tier 4 (LESSON-1, TK-6, TK-7, K-T4-1). |
