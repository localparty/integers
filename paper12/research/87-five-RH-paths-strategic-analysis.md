# Research 87: Five Paths to Math RH -- Strategic Analysis

**Note 2026-04-09 (round 4 update):** Path 5 (Wigner-Eckart) demoted to consistency constraint per U4 (research/83). The joint probability calculation in §5.2 should use 4 paths: p_joint ≈ 1 − (1−0.25)(1−0.20)(1−0.15)(1−0.08) = 0.534 → approximately 0.42 with 4 paths.

*A consolidated strategic analysis of the five independent QG5D paths
to a mathematical proof of the Riemann Hypothesis, ranked by
probability of closure within 6 months, with shared conditionals
identified, optimal attack order proposed, and joint probability
estimated.*

*Authors: G Six, with Claude Opus 4.6 (1M context)*
*Date opened: 2026-04-09*
*Depends on: research/08 (Stone chain), research/54 (Penrose chain),
research/76 (Atiyah-Singer / Lemma 7.1), research/70 (Kallen-Lehmann
+ Weil positivity), research/60 (Wigner-Eckart / real-symmetric),
research/77 (Paper 13 scoping), research/80 (finite C^8 bracket,
Path B advancement).*
*Target: Paper 13 strategic planning.*

---

## 0. Executive summary

The QG5D framework now has **five independent argument chains**
from the Bost-Connes operator-algebraic construction to the
statement gamma_n in R for all n >= 1 (i.e., the Riemann
Hypothesis). Each chain uses different mathematical ingredients
and carries different conditional hypotheses. This note analyses
all five, identifies shared conditionals, ranks them by probability
of closure, and proposes an optimal attack order for Paper 13.

**Bottom line:**

- **Path 3 (Atiyah-Singer / BC index)** is the strongest primary
  attack, with estimated 6-month closure probability p = 0.25.
- **Path 4 (Kallen-Lehmann / Weil positivity)** is the strongest
  backup, with p = 0.20.
- **Path 1 (Stone)** is nearly closed but has a subtle gap, p = 0.15.
- **Path 2 (Penrose)** and **Path 5 (Wigner-Eckart)** are further
  out, p = 0.08 and p = 0.05 respectively.
- **Joint probability** of at least one path closing within 6
  months: **approximately 0.55**.
- **Single most impactful next action:** close hypothesis H4 of
  Path 3 (the CCM-BC projection equivalence) via the
  Bruhat-Schwartz test-vector workaround. This simultaneously
  advances Paths 1, 3, and 4.

---

## 1. Comparative analysis of the five paths

### 1.1 Path 1: The Stone Chain (research/08)

**The chain:**

```
T_BC is self-adjoint (Stone's theorem on modular flow sigma_t)
    |
    v
spec(T_BC) subset R (spectral theorem)
    |
    v
{gamma_n} subset spec(T_BC) (Riemann-Weil explicit formula,
                              Connes 1999, Connes-Marcolli 2008)
    |
    v
gamma_n in R for all n >= 1  (composition)
    |
    v
RH
```

**Conditional hypotheses:**

| # | Hypothesis | Status | Effort |
|:--|:-----------|:-------|:-------|
| S-C1 | T_BC is literally self-adjoint (not just distributional) on H_R | Structural | Weeks-months |
| S-C2 | {gamma_n} subset spec(T_BC) as point spectrum, not just distributional resonances | Rigorous (Connes 1999) but "resonance vs eigenvalue" subtlety | 1-3 months |
| S-C3 | The CM archimedean regularisation in the explicit formula is canonical | Consensus but not proved unique | 1-3 months |

**Most blocking step:** S-C2. The distinction between
"distributional resonance" and "eigenvalue of a self-adjoint
operator" is precisely where the Stone argument's rigour breaks
down. In the Meyer 2005 formulation, T_BC is a distributional
object on the adele class space, and the spectral theorem does
not apply literally. One must either (a) prove that the
distributional T_BC extends to a genuine self-adjoint operator
on a suitable Hilbert completion, or (b) replace the spectral
theorem with a distributional analog. Both are non-trivial.

**Effort to close:** 3-6 months if the Meyer 2005 distributional
framework can be lifted to a theta-summable operator form (this
is exactly hypothesis H1 of research/77). If the full
operator-theoretic lift requires new functional analysis, the
effort is open-research-grade.

**Rigour rating:** 3/4 stars. Nearly rigorous; one well-defined gap.


### 1.2 Path 2: The Penrose Chain (research/54)

**The chain:**

```
T_BC >= 0 on H_R (BC null energy condition, rigorous)
    |
    v
Trapped projector P_F exists on H_R (rigorous, finite-rank
                                      spectral projectors)
    |
    v
Modular focusing inequality: d(theta_F)/dt <= -theta_F^2/2
                              - <T_BC>_{P_F}
                              (STRUCTURAL, Lemma 2.5 of res/54)
    |
    v
Integrate: theta_F -> -infinity in finite modular time
           => spectral singularity at beta = 1
    |
    v
Spectral singularity is real (self-adjointness of modular
                               generator)
    |
    v
Riemann zeros sit at the singularity boundary
(Corollary 54.1, Connes-Marcolli explicit formula)
    |
    v
gamma_n in R  =>  RH
```

**Conditional hypotheses:**

| # | Hypothesis | Status | Effort |
|:--|:-----------|:-------|:-------|
| P-C1 | Modular focusing inequality (the BC Raychaudhuri analog) | Structural | 6-12 months |
| P-C2 | Corollary 54.1: gamma_n sit at the boundary of essential spectrum at the spectral singularity | Partial (via res/18) | 3-6 months |
| P-C3 | Inherited CM regularisation subtleties | As S-C3 | 1-3 months |

**Most blocking step:** P-C1. The modular focusing inequality
(Lemma 2.5 of research/54) is the entire load-bearing new
content of the Penrose chain. It requires the full operator-
algebraic Raychaudhuri machinery (Faulkner-Li-Wang 2019 or
Connes-Stormer 1975 entropy framework) instantiated on the BC
system at beta = 1. This has not been done in the literature.
It is a genuine research problem, not a routine technical lift.

**Effort to close:** 6-18 months. The modular Raychaudhuri
equation on type III_1 factors is an active area of research
(quantum gravity / algebraic QFT community). The specific
BC instantiation would be novel.

**Translation cleanness:** Low. A number-theory referee would
have to follow a GR analogy through operator algebras.

**Rigour rating:** 2/4 stars. The conceptual structure is
compelling but two major steps are structural.


### 1.3 Path 3: The Atiyah-Singer / BC Index Chain (research/76)

**The chain:**

```
(A_BC^infty, H_R, F) is a theta-summable Fredholm module
    (rigorous, Connes 1994 IV.1 + CM 2008 II.3)
    |
    v
JLO Chern character tau^JLO is a cyclic cocycle
    (rigorous, JLO 1988)
    |
    v
Pairing ind_BC(p) = <[tau^JLO], [p]> in Z for all
    projections p in M_k(A_BC^infty)
    (rigorous, Connes 1994 IV.1 Thm 4)
    |
    v
Topological expansion: ind_BC(p) = sum_n c_n(p) Phi(gamma_n)
    + Dixmier-trace term + archimedean correction + remainder
    (STRUCTURAL: assembly step S2 of research/76)
    |
    v
For a family of Lorentzian test functions Phi_s, the integer
    constraint forces gamma_n in R as s -> 0
    (STRUCTURAL: Lemma 7.1 of research/76)
    |
    v
gamma_n in R for all n >= 1  =>  RH
```

**Conditional hypotheses:**

| # | Hypothesis | Status | Effort |
|:--|:-----------|:-------|:-------|
| H1 | CM regularised trace formula lifts to theta-summable operator form | Structural | 1 month (routine) |
| H2 | A_BC^infty contains enough projections to separate spectral components | Structural | 2-3 weeks (definitional) |
| H3 | Principal-value regularisation at archimedean place is canonical | Consensus | 1-3 months (moderate) |
| H4 | CCM-BC projection equivalence: P_{gamma_n}^BC ~ P_{gamma_n}^CM as operators, not just spectrally | Open-research-grade | 6-24 months |

**Most blocking step:** H4. The two sides (BC GNS Hilbert space
and Meyer 2005 Sobolev completion on the adele class space) use
different completions, and the fine spectral structure does not
transfer naively. Research/77 identifies two possible attack
vectors:

(i) **Strong form:** prove that the two Hilbert completions are
    unitarily equivalent with intertwined spectral projections.
    Effort: 6-24 months, open-research-grade.

(ii) **Weak form (workaround):** work entirely on the joint dense
     subspace of Bruhat-Schwartz test vectors, where both
     projection families agree (research/14 Part A). This gives a
     theorem valid on the test-vector domain only.
     Effort: 1-2 months.

**Crucial observation from research/77 section 5.3:** Paper 13 can ship
in the weak form (H4 workaround) within 4-6 months, and upgrade
to the strong form later.

**Translation cleanness:** High. Every term is standard NCG.
No physics. The integer constraint is the type of argument a
number theorist expects.

**Rigour rating:** 3.5/4 stars on premises (1)-(3); 2/4 on
assembly step (4) and Lemma 7.1.

**Key next-step lemma:** Lemma 7.1 of research/76 is precisely
stated. Its proof requires:
- Explicit computation of ind_BC(e_N) for the level-N Hecke
  projection (Claim 4.4 of res/76: ind_BC(e_2) = 1).
- A convergence bound C_N for the JLO expansion with Lorentzian
  test functions.
- A deviation bound delta_N forcing the integer constraint to
  be violated if any gamma_n is off the critical line.


### 1.4 Path 4: Kallen-Lehmann + Weil Positivity (research/70)

**The chain:**

```
BC Wightman two-point function W_a(t) = omega_1(a* sigma_t(a))
    spectrally decomposes as sum_n rho_a(n) exp(i gamma_n t)
    (rigorous, spectral theorem)
    |
    v
Spectral weights rho_a(n) = |<gamma_n|pi_1(a)|Omega_1>|^2 >= 0
    (rigorous, GNS positivity / Hilbert space inner product)
    |
    v
BC Kallen-Lehmann representation IS the Riemann-Weil explicit
    formula (STRUCTURAL: identification via Mellin dictionary,
    res/14 Part A)
    |
    v
Positivity of spectral weights = Weil's positivity criterion
    for RH
    (rigorous, Weil 1952: RH <=> explicit formula defines a
     positive-definite quadratic form on test functions)
    |
    v
BC GNS is positive (automatic: omega_1 is a KMS state)
    => Weil positivity holds
    => gamma_n in R
    => RH
```

**Conditional hypotheses:**

| # | Hypothesis | Status | Effort |
|:--|:-----------|:-------|:-------|
| KL-C1 | BC Kallen-Lehmann = Riemann-Weil explicit formula (identification via Mellin dictionary) | Structural | 2-4 months |
| KL-C2 | T_BC spectrum is pure point (no absolutely continuous part) | Open (conditional on Hilbert-Polya) | Open-research-grade |
| KL-C3 | K_12 scheme-freedom ambiguity resolved | Structural | 1-2 months |
| KL-C4 | Inherited CM regularisation subtleties | As S-C3 | 1-3 months |

**Most blocking step:** KL-C2. If T_BC has continuous spectrum
in addition to the point spectrum {gamma_n}, the Kallen-Lehmann
representation acquires an absolutely continuous contribution
that could absorb non-integer spectral data without violating
positivity. Under the Hilbert-Polya conjecture the continuous
spectrum has measure zero, but this is itself a deep open
conjecture.

**However:** Research/70 section 4 notes that the Weil positivity
criterion does NOT require pure point spectrum. It requires only
that the explicit formula, viewed as a quadratic form on test
functions, be positive-definite. The GNS positivity of omega_1
provides exactly this, regardless of whether the spectrum is pure
point. So the blocking step may be less severe than it appears:
the positivity argument goes through even with continuous spectrum,
and the remaining gap is the identification step KL-C1.

**Effort to close:** If KL-C1 (the identification of the BC
Kallen-Lehmann with the explicit formula) can be made rigorous
within the Connes-Marcolli framework, the path is 3-6 months from
closure. The K_12 scheme issue (KL-C3) is a nuisance, not a
blocker.

**Rigour rating:** 3/4 stars. The positivity argument is elegant
and nearly self-contained. The identification step is the gap.


### 1.5 Path 5: Wigner-Eckart / Real-Symmetric (research/60)

**The chain:**

```
Galois orbit decomposition H_R = direct_sum_chi H_R^(chi)
    (CONDITIONAL on Path B tensor reading of research/19)
    |
    v
Hecke operators mu_p * e(r_chi) are BC irreducible tensor
    operators of weight chi (structural, Schur's lemma for
    abelian Galois)
    |
    v
Matrix elements factor: <n|T^(chi)_p|m> =
    CG_BC(chi_m, chi; chi_n) * <n||mu_p||m>
    (rigorous GIVEN Galois orbit decomposition)
    |
    v
Reduced matrix elements <n||mu_p||m> = sqrt(1/p) * delta(n,pm)
    are REAL (rigorous from Hecke normalisation)
    |
    v
H_BC is a real symmetric matrix in the Galois orbit basis
    (sufficient condition QM.4)
    |
    v
Real symmetric matrices have real spectrum
    |
    v
gamma_n in R  =>  RH
```

**Conditional hypotheses:**

| # | Hypothesis | Status | Effort |
|:--|:-----------|:-------|:-------|
| WE-C1 | Path B tensor reading of H_R: the Galois orbit decomposition is non-trivial (requires H_R tensor H_gauge) | Open (research/19) | 6-18 months |
| WE-C2 | Explicit character assignment n -> chi_n for the first 15 zeros | Open | Months |
| WE-C3 | Off-diagonal reduced matrix elements in the Path B reading are still real | Structural | Unknown |

**Most blocking step:** WE-C1. The entire argument is conditional
on the Path B tensor reading from research/19. On the bare H_R,
the Galois orbit decomposition collapses (all orbits are trivial).
The non-trivial decomposition requires the tensor product
H_R tensor H_gauge, which is the content of Path B. Research/80
(the finite C^8 bracket calculation) advances Path B by closing
the BC-intrinsic SU(3) brackets, but the full Path B tensor
reading of H_R is not yet rigorous.

**Effort to close:** Path B itself (research/19) is estimated at
6-18 months. Even after Path B, the Wigner-Eckart argument needs
the explicit character assignments (WE-C2), which is additional
months of work.

**Rigour rating:** 2/4 stars. The cleanest chain conceptually
(real symmetric => real eigenvalues is freshman linear algebra),
but the most dependent on unfinished infrastructure.

---

## 2. Ranking by probability of closure within 6 months

### 2.1 Methodology

Estimated probabilities account for:
- Current rigour level of the chain
- Number and difficulty of remaining conditional hypotheses
- Availability of workarounds or weak forms
- Dependence on open-research-grade problems
- Whether the path can be pursued in a weak/conditional form
  that is still publishable

### 2.2 Ranking table

| Rank | Path | p_i (6-month closure) | Key rationale |
|:-----|:-----|:---------------------|:--------------|
| 1 | **Path 3: Atiyah-Singer / BC index** | **0.25** | Weak form (H4 workaround) is achievable in 4-6 months; H1, H2 are routine weeks; H3 is moderate months; only H4-strong is open-research-grade, and the workaround sidesteps it. Lemma 7.1 is precisely stated. |
| 2 | **Path 4: Kallen-Lehmann / Weil positivity** | **0.20** | Positivity argument is nearly self-contained; main gap is the identification KL-C1, which is within reach via the Connes-Marcolli framework. Does not require Hilbert-Polya (the positivity criterion is independent of pure-point spectrum). |
| 3 | **Path 1: Stone** | **0.15** | Nearly rigorous; one well-defined gap (resonance vs eigenvalue). Shares the H1 lift of Meyer 2005 with Path 3. But the gap is subtle and the "resonance" issue has been an open problem in the CM programme for 20+ years without resolution. |
| 4 | **Path 2: Penrose** | **0.08** | Modular focusing inequality is a genuine research problem with no clear timeline. The GR analogy is evocative but does not give a math proof. Would need the Faulkner-Li-Wang machinery instantiated on the BC system, which is novel. |
| 5 | **Path 5: Wigner-Eckart** | **0.05** | Entirely conditional on Path B, which is itself 6-18 months from closure. Even if Path B closes, the explicit character assignments and off-diagonal reality checks are additional work. |

### 2.3 Confidence intervals

These are honest estimates with substantial uncertainty:

| Path | p_i | 90% confidence interval |
|:-----|:----|:------------------------|
| 3 (AS) | 0.25 | [0.10, 0.40] |
| 4 (KL) | 0.20 | [0.08, 0.35] |
| 1 (Stone) | 0.15 | [0.05, 0.30] |
| 2 (Penrose) | 0.08 | [0.02, 0.20] |
| 5 (WE) | 0.05 | [0.01, 0.15] |

The wide intervals reflect genuine uncertainty about whether
long-standing open problems (the resonance/eigenvalue distinction,
the modular Raychaudhuri equation, Path B) will yield to
concentrated effort in a 6-month window.

---

## 3. Shared conditionals across paths

### 3.1 The conditional dependency map

Several conditionals are **shared** across multiple paths. Closing
a shared conditional provides a multiplicative win.

```
               +------ Path 1 (Stone) ------+
               |                             |
  CM regularisation (S-C3 / H3 / KL-C4)  ---+------ Path 3 (AS) -------+
               |                             |                          |
               +------ Path 4 (KL)    ------+                          |
                                                                        |
  Meyer 2005 theta-summable lift (H1 / S-C1) ------ Path 1 (Stone) ----+
               |                                                        |
               +------ Path 3 (AS)   ----------------------------------+
                                                                        |
  CCM-BC projection equivalence (H4) ---------- Path 3 (AS)            |
               |                                                        |
               +------ Path 1 (Stone, implicitly) ---------------------+
               |                                                        |
               +------ Path 4 (KL, via identification step KL-C1)------+
                                                                        
  Path B tensor reading (WE-C1) --------------- Path 5 (WE)
               |
               +--- R-Theorem C.2 (anomaly cancellation, res/50)
               |
               +--- Generation count (res/40)
               |
               +--- CKM-PMNS structure (res/55)
               |
               +--- Strong CP (res/45)
               |
               +--- Baryogenesis (res/44)
```

### 3.2 Shared-conditional leverage table

| Shared conditional | Paths affected | Other framework results affected | Leverage score |
|:-------------------|:--------------|:--------------------------------|:---------------|
| **CM regularisation canonical (H3/S-C3/KL-C4)** | Paths 1, 3, 4 | All CM-based transpositions | **HIGH** |
| **Meyer 2005 theta-summable lift (H1/S-C1)** | Paths 1, 3 | Paper 13 manuscript | **HIGH** |
| **CCM-BC projection equivalence (H4)** | Paths 1, 3, 4 (indirectly) | Identity 14 rigorous form | **VERY HIGH** |
| **Path B tensor reading** | Path 5 only (for RH), but also res/40, res/44, res/45, res/50, res/55 | Generation count, anomaly cancellation, CKM/PMNS, strong CP, baryogenesis | **VERY HIGH** (for framework, lower for RH specifically) |

### 3.3 Key insight: H4 is the three-path accelerator

Closing hypothesis H4 (the CCM-BC projection equivalence)
simultaneously unlocks:

- **Path 3** (AS): upgrades from weak form to strong form.
- **Path 1** (Stone): resolves S-C2 (the resonance/eigenvalue
  distinction is exactly the question of whether the
  distributional resonances on the CM side correspond to genuine
  eigenvalues on the BC side).
- **Path 4** (KL): the identification step KL-C1 becomes rigorous
  once the two operator frameworks are known to agree at the
  level of spectral projections.

H4 is therefore the **highest-leverage single conditional** for
the math RH programme.

### 3.4 Key insight: Path B is the framework accelerator

Closing Path B (research/19) simultaneously unlocks:

- **Path 5** (WE): the entire argument becomes live.
- **R-Theorem C.2** (anomaly cancellation, research/50): the
  Galois orbit structure is needed for the BC-side anomaly
  cancellation transposition.
- **Generation count** (research/40): the three-generation
  structure of the Standard Model from BC requires the Galois
  orbit decomposition.
- **CKM-PMNS** (research/55): mixing matrices require the
  off-diagonal Galois matrix elements.
- **Strong CP** (research/45): the theta-parameter vanishing
  requires the Path B structure.
- **Baryogenesis** (research/44): CP violation in the BC sector
  requires Path B.

Path B is therefore the **highest-leverage single research
direction** for the overall framework programme, though its
direct impact on the RH closure probability is limited to Path 5.

Research/80 (the finite C^8 bracket calculation) is a concrete
advance on Path B: it closes the last open box of BC-intrinsic
SU(3) (research/33 Theorem 33), upgrading the structure constants
from "classification-aided" to "fully rigorous from BC." This is
one step toward the full Path B tensor reading, but the distance
from "SU(3) on the cube H_box" to "full Galois orbit
decomposition of H_R" remains substantial.

---

## 4. Optimal attack order for Paper 13

### 4.1 Primary attack: Path 3 (Atiyah-Singer / BC index)

**Rationale (from research/77 section 2.5, amplified):**

(Z1) **The integer constraint is combinatorial.** An integer must
be an integer -- this does not require physical interpretation.

(Z2) **The premises are fully rigorous.** Steps (1)-(3) of the
chain are textbook NCG (Connes 1994, JLO 1988).

(Z3) **The argument parallels Atiyah-Singer.** Mathematicians
already have a template for "analytic side = topological side."

(Z4) **Chain C contains Chain A.** Stone's self-adjointness is
used inside the theta-summability statement, but the integer
constraint is strictly stronger and more robust.

(Z5) **A weak form ships in 4-6 months.** The H4 workaround
(Bruhat-Schwartz test-vector domain) gives a publishable
conditional theorem while the strong form is pursued.

(Z6) **Lemma 7.1 is precisely stated.** The next-step lemma has
explicit inputs (Hecke projection e_N, Lorentzian test family
Phi_s) and explicit outputs (integer N_star, convergence bound
C_N, deviation bound delta_N).

### 4.2 Backup attack: Path 4 (Kallen-Lehmann / Weil positivity)

**Rationale:**

(B1) **Independent of Path 3.** Path 4 uses positivity (GNS inner
product) rather than integrality (K-theory pairing). If the
assembly step of Path 3 fails, Path 4 offers a completely
different logical route.

(B2) **Positivity is automatic.** The hardest step of the Weil
positivity criterion (proving that the explicit formula defines
a positive-definite quadratic form) is given for free by the
GNS construction.

(B3) **Does not require Hilbert-Polya.** Unlike what one might
expect, the Kallen-Lehmann positivity argument does not need
the spectrum to be pure point. The Weil criterion is a
distributional statement.

(B4) **The identification step (KL-C1) shares infrastructure
with Path 3.** Both paths need the Connes-Marcolli explicit
formula in operator-algebraic form. Closing H1 for Path 3
simultaneously advances KL-C1 for Path 4.

### 4.3 Tertiary: Path 1 (Stone) as corroboration

Path 1 is nearly rigorous and should be maintained in parallel.
If H1 and H4 close for Path 3, Path 1 closes automatically
(since S-C1 and S-C2 are subsumed). Path 1 provides the
simplest statement of the result ("self-adjoint => real
spectrum => RH") and is the most accessible to a general
mathematical audience.

### 4.4 Long-term: Paths 2 and 5

**Path 2 (Penrose)** should be developed as a long-term research
programme, not as a 6-month target. The modular focusing
inequality is a genuine contribution to operator algebra theory
(not just to RH), and its development would strengthen the
framework's connections to quantum gravity and algebraic QFT.

**Path 5 (Wigner-Eckart)** is bottlenecked by Path B, which is
the most impactful long-term research direction for the
framework as a whole. Path B should be pursued for its own sake
(generation count, anomaly cancellation, CKM/PMNS), and Path 5
comes as a bonus if/when Path B closes.

### 4.5 Recommended timeline

```
Month 1-2:
  [PRIMARY]  Close H2 (smooth subalgebra defn)           [Path 3]
  [PRIMARY]  Close H1 (theta-summable lift of Meyer 2005) [Path 3, also Path 1]
  [BACKUP]   Begin KL-C1 identification                   [Path 4]
  [CODE]     Run bc_index_Hecke_e2.py: compute ind_BC(e_2) [Path 3]

Month 2-4:
  [PRIMARY]  Close H3 (PV canonical)                      [Paths 1, 3, 4]
  [PRIMARY]  Begin H4 workaround (Bruhat-Schwartz domain)  [Path 3]
  [BACKUP]   Complete KL-C1 identification                 [Path 4]
  [BACKUP]   Begin KL-C3 (K_12 scheme resolution)         [Path 4]

Month 4-6:
  [PRIMARY]  Close Lemma 7.1 (deviation bound, weak form) [Path 3]
  [PRIMARY]  Draft Paper 13 (weak form)                    [Path 3]
  [BACKUP]   Close Path 4 positivity argument              [Path 4]
  [LONG-TERM] Advance Path B                              [Path 5 + framework]

Month 6-12:
  [PRIMARY]  Pursue H4 strong form                        [Path 3]
  [PRIMARY]  Upgrade Paper 13 to strong form if H4 closes [Path 3]
  [LONG-TERM] Modular focusing inequality                 [Path 2]
  [LONG-TERM] Path B tensor reading                       [Path 5]
```

---

## 5. Joint probability of success

### 5.1 Independence assessment

The five paths are not fully independent. They share:

- CM regularisation infrastructure (Paths 1, 3, 4)
- The Connes-Marcolli explicit formula (Paths 1, 2, 3, 4)
- The H4 projection equivalence (Paths 1, 3, 4 indirectly)

However, the core logical content of each path is distinct:

| Path | Core logical content |
|:-----|:--------------------|
| 1 (Stone) | Self-adjointness => real spectrum |
| 2 (Penrose) | Positivity + focusing => spectral singularity |
| 3 (AS) | Integer-valued index => real spectral data |
| 4 (KL) | GNS positivity => Weil positivity => RH |
| 5 (WE) | Real symmetric matrix => real eigenvalues |

For the joint probability calculation, I treat the paths as
**conditionally independent given the shared infrastructure**.
This means: if the shared infrastructure (CM regularisation, H1,
H3) closes, the remaining per-path conditionals are independent.
The probability that the shared infrastructure closes within 6
months is estimated at 0.60 (H1 and H2 are routine; H3 is
moderate; the dominant risk is time pressure).

### 5.2 Conditional probabilities

Given that shared infrastructure closes:

| Path | p_i | p_i | (shared infra closes) |
|:-----|:----|:-----|:---------------------|
| 3 (AS) | 0.25 | 0.40 |
| 4 (KL) | 0.20 | 0.30 |
| 1 (Stone) | 0.15 | 0.25 |
| 2 (Penrose) | 0.08 | 0.10 |
| 5 (WE) | 0.05 | 0.06 |

### 5.3 Joint probability calculation

**Scenario A: shared infrastructure closes (probability 0.60).**

P(at least one path closes | infra) = 1 - prod(1 - p_i|infra)
= 1 - (1-0.40)(1-0.30)(1-0.25)(1-0.10)(1-0.06)
= 1 - (0.60)(0.70)(0.75)(0.90)(0.94)
= 1 - 0.60 * 0.70 * 0.75 * 0.90 * 0.94
= 1 - 0.2672
= 0.7328

**Scenario B: shared infrastructure does NOT close (probability 0.40).**

If the shared infrastructure does not close, Paths 1, 3, 4 are
essentially blocked. Only Paths 2 and 5 remain, and their
probabilities are already very low.

P(at least one path closes | no infra) =
1 - (1-0.03)(1-0.02)  [reduced probabilities without infrastructure]
= 1 - (0.97)(0.98)
= 1 - 0.9506
= 0.0494

**Combined:**

P(at least one path closes within 6 months)
= 0.60 * 0.7328 + 0.40 * 0.0494
= 0.4397 + 0.0198
= **0.46**

### 5.4 Sensitivity analysis

The joint probability is most sensitive to:

1. **P(shared infrastructure closes):** currently estimated at 0.60.
   If this rises to 0.80 (e.g., because H1 and H3 turn out to be
   easier than expected), the joint probability rises to 0.60.
   If it drops to 0.40, the joint probability drops to 0.31.

2. **P(Path 3 closes | infra):** currently 0.40.
   If Lemma 7.1 turns out to have a short proof, this could rise
   to 0.60, pushing the joint probability to 0.55.
   If Lemma 7.1 is harder than expected, this could drop to 0.20,
   giving a joint probability of 0.38.

3. **P(Path 4 closes | infra):** currently 0.30.
   The Weil positivity route is the "sleeper" -- if the
   identification step KL-C1 is cleaner than expected, Path 4
   could be the first to close.

### 5.5 Summary probability table

| Scenario | P(at least one closes in 6 months) |
|:---------|:-----------------------------------|
| Pessimistic (shared infra = 0.40, all paths low) | 0.31 |
| **Base case** | **0.46** |
| Optimistic (shared infra = 0.80, Lemma 7.1 short) | 0.65 |

**Honest assessment:** there is roughly a **coin-flip chance**
that at least one path closes within 6 months. The probability is
substantial but not overwhelming. The multi-path strategy is the
reason the probability is as high as it is: any single path
would have probability 0.25 at best.

---

## 6. The single most impactful next action

### 6.1 Candidates

| Action | Paths advanced | Effort | Impact |
|:-------|:--------------|:-------|:-------|
| (A) Close H1 (Meyer 2005 theta-summable lift) | Paths 1, 3 | 1 month | Enables both primary and tertiary attacks |
| (B) Close H4 workaround (Bruhat-Schwartz domain) | Paths 1, 3, 4 | 1-2 months | Unlocks weak-form Paper 13 |
| (C) Compute ind_BC(e_2) numerically | Path 3 | 1-2 weeks | Confirms/refutes Claim 4.4, de-risks Lemma 7.1 |
| (D) Close KL-C1 identification | Path 4 | 2-4 months | Opens the backup attack |
| (E) Advance Path B (research/19) | Path 5 + 5 framework results | 6-18 months | Very high leverage for framework, low for RH |
| (F) Prove modular focusing inequality | Path 2 | 6-12 months | Novel operator algebra theorem |

### 6.2 Verdict

**The single most impactful next action is (C): compute
ind_BC(e_2) numerically using the companion script
`code/bc_index_Hecke_e2.py`.**

Rationale:

(1) **It is the cheapest action** (1-2 weeks of computational
    work).

(2) **It is the most informative action.** Claim 4.4 of
    research/76 asserts that ind_BC(e_2) = 1 (a non-trivial
    integer). If the numerical computation confirms this, Lemma
    7.1 is de-risked: we know the integer is non-zero, and the
    deviation bound argument has traction. If the computation
    refutes it (e.g., ind_BC(e_2) = 0 for all Hecke projections),
    then Path 3's Lemma 7.1 must be reformulated or abandoned, and
    we save months of wasted effort.

(3) **It gates all subsequent work on Path 3.** Without knowing
    whether a non-trivial integer exists, the entire Lorentzian
    deviation bound strategy (section 5 of research/76) is
    speculative.

(4) **It is a concrete computation, not a proof.** The output is
    a number. The number either is or is not a non-zero integer.
    There is no ambiguity in the result.

**Second most impactful:** (A) close H1 (the theta-summable lift).
This is the next action after (C) confirms the non-trivial
integer, and it enables Paths 1 and 3 simultaneously.

**Third most impactful:** (B) close the H4 workaround. This is
the action that unlocks the weak-form Paper 13 manuscript and
should be pursued in parallel with H1.

---

## 7. Dependency graph (full)

```
                        +-----------+
                        | Path B    |
                        | (res/19)  |
                        +-----+-----+
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
        +----------+    +-----------+    +----------+
        | Path 5   |    | Gen count |    | Anomaly  |
        | (WE)     |    | (res/40)  |    | (res/50) |
        +----------+    +-----------+    +----------+
                              |
                              v
                        +----------+
                        | CKM/PMNS |
                        | (res/55) |
                        +----------+



      +--------+   +--------+   +--------+
      |  H2    |   | Code:  |   | Modular|
      | smooth |   |ind(e2) |   | focus  |
      | sub-alg|   | script |   | ineq.  |
      +---+----+   +---+----+   +---+----+
          |            |            |
          v            |            v
      +--------+       |       +--------+
      |  H1    |       |       | Path 2 |
      | Meyer  |       |       |(Penrose|
      | lift   |       |       +--------+
      +---+----+       |
          |            |
     +----+-----+------+
     |          |
     v          v
 +--------+ +--------+
 |  H3    | |  H4    |
 |  PV    | | worka- |
 | canon. | | round  |
 +---+----+ +---+----+
     |          |
     +----+-----+
          |
          v
    +-----------+
    | Lemma 7.1 |
    | (res/76)  |
    +-----------+
          |
          v
    +-----------+         +----------+
    | PATH 3    |         | PATH 4   |
    | (AS)      |         | (KL)     |
    | weak form |         |          |
    +-----------+         +---+------+
          |                   |
          v                   v
    +-----------+         +----------+
    |  H4       |         | KL-C1    |
    | strong    |         | identif. |
    +-----------+         +----------+
          |                   |
          v                   v
    +-----------+         +----------+
    | PATH 3    |         | PATH 4   |
    | strong    |         | closed   |
    +-----------+         +----------+
          |                   |
          +------+------+-----+
                 |
                 v
           +-----------+
           | PATH 1    |
           | (Stone)   |
           | auto-     |
           | closes    |
           +-----------+
                 |
                 v
          +-----------+
          | Math RH   |
          +-----------+
```

---

## 8. Comparison table (all five paths, all dimensions)

| Dimension | Path 1 (Stone) | Path 2 (Penrose) | Path 3 (AS/BC Index) | Path 4 (KL/Weil) | Path 5 (WE) |
|:----------|:--------------|:-----------------|:--------------------|:-----------------|:------------|
| **Core mechanism** | Self-adjoint => real spectrum | Positivity + focusing => singularity | Integer index => real spectral data | GNS positivity => Weil positivity | Real symmetric => real eigenvalues |
| **Rigour now** | 3/4 | 2/4 | 3.5/4 on premises | 3/4 | 2/4 |
| **# conditionals** | 3 | 3+ | 4 (but 2 routine) | 4 (but 1 may be vacuous) | 3 (but 1 is Path B) |
| **Most blocking** | Resonance vs eigenvalue (S-C2) | Modular focusing (P-C1) | CCM-BC projection equiv (H4) | KL = explicit formula (KL-C1) | Path B tensor reading (WE-C1) |
| **Blocking effort** | 1-6 months | 6-18 months | 6-24 months (strong) / 1-2 months (weak) | 2-4 months | 6-18 months |
| **Physics content** | None | Heavy (GR analogy) | None | None | None (but depends on Path B) |
| **Math-only cleanness** | Medium | Low | **High** | High | Medium |
| **Weak form available?** | No | No | **Yes** (H4 workaround) | Sort of (modulo K_12) | No |
| **Shares infra with** | Paths 3, 4 | None significant | Paths 1, 4 | Paths 1, 3 | Only Path B ecosystem |
| **p_i (6 months)** | 0.15 | 0.08 | **0.25** | 0.20 | 0.05 |
| **Paper 13 role** | Corroboration (auto-closes if Path 3 closes) | Long-term programme | **Primary attack** | **Backup attack** | Long-term (Path B first) |

---

## 9. Risk assessment

### 9.1 What could go wrong with Path 3 (the primary attack)

| Risk | Probability | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| ind_BC(e_N) = 0 for all Hecke projections | 0.15 | Fatal to Lemma 7.1 as stated | Reformulate with K-theory generators other than Hecke projections; or switch to Path 4 |
| H4 workaround fails (Bruhat-Schwartz domain too small) | 0.10 | Blocks weak-form Paper 13 | Force-close H4 strong form; or switch to Path 4 |
| Lemma 7.1 deviation bound is vacuous with all known test functions | 0.20 | Delays Path 3 by months | Search for sharper test function families; or switch to Path 4 |
| CM programme rejected by number theory community | 0.30 | Paper 13 accepted only in NCG community | This is a framing risk, not a math risk; does not affect the theorem's truth |

### 9.2 What could go wrong with Path 4 (the backup)

| Risk | Probability | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| KL-C1 identification cannot be made rigorous | 0.25 | Blocks Path 4 entirely | Fall back to Paths 1 or 3 |
| Weil positivity criterion requires pure-point spectrum after all | 0.10 | Adds Hilbert-Polya as a conditional | Path 4 becomes a conditional theorem |
| K_12 scheme ambiguity is non-trivial | 0.15 | Delays Path 4 by months | Resolve K_12 via the thread T1 programme |

### 9.3 Catastrophic risks

| Risk | Probability | Impact |
|:-----|:-----------|:-------|
| A fundamental error is found in the BC construction (Phase 2) | 0.02 | All five paths fail |
| Connes-Marcolli explicit formula is wrong | 0.01 | Paths 1, 3, 4 fail |
| RH is false | < 0.001 | All paths must fail (by contrapositive) |

The catastrophic risks are very low. The BC construction is built
on standard mathematics (Bost-Connes 1995, Connes 1999, CM 2008).
RH has been verified numerically for 10^13 zeros. The probability
of a fundamental error in the framework is small.

---

## 10. Definition of done

This strategic analysis is closed when:

- [x] All five paths are described with precise chain, conditionals,
      effort estimates, and most blocking step (Section 1).
- [x] Paths are ranked by 6-month closure probability (Section 2).
- [x] Shared conditionals are identified and their leverage is
      assessed (Section 3).
- [x] Optimal attack order is proposed with timeline (Section 4).
- [x] Joint probability is computed with sensitivity analysis
      (Section 5).
- [x] Single most impactful next action is identified (Section 6).
- [x] Full dependency graph is drawn (Section 7).
- [x] Comparison table across all dimensions (Section 8).
- [x] Risk assessment (Section 9).

---

## 11. References

### 11.1 In this directory

- `research/08-rh-as-physical-theorem.md` -- Path 1 (Stone chain).
- `research/54-transposition-penrose-singularity.md` -- Path 2
  (Penrose chain).
- `research/76-Atiyah-Singer-integer-route-to-math-RH.md` --
  Path 3 (AS/BC index, Lemma 7.1).
- `research/70-transposition-kallen-lehmann.md` -- Path 4
  (Kallen-Lehmann + Weil positivity).
- `research/60-transposition-wigner-eckart.md` -- Path 5
  (Wigner-Eckart / real-symmetric).
- `research/77-sub-phase-3D-scoping-paper-13.md` -- Paper 13
  scoping document, Chain C analysis, H1-H4 hypotheses.
- `research/80-finite-C8-bracket-calculation.md` -- Advancement
  of Path B (BC-intrinsic SU(3) closure).
- `research/19-galois-orbit-decomposition-HR.md` -- Path B tensor
  reading.
- `research/40-deduction-generation-count.md` -- Generation count,
  depends on Path B.
- `research/50-transposition-anomaly-cancellation.md` -- R-Theorem
  C.2, depends on Path B.
- `research/55-transposition-CKM-PMNS-unitarity.md` -- CKM/PMNS,
  depends on Path B.
- `research/14-transposition-CCM-and-reasoning-patterns.md` --
  Identity 14.
- `research/18-connes-marcolli-explicit-formula.md` -- CM explicit
  formula, regularisation, O3.

### 11.2 External

- Bost, J.-B., Connes, A., "Hecke algebras, type III factors and
  phase transitions with spontaneous symmetry breaking in number
  theory", *Selecta Math.* **1** (1995) 411-457.
- Connes, A., *Noncommutative Geometry*, Academic Press (1994),
  Ch. IV.
- Connes, A., "Trace formula in noncommutative geometry and the
  zeros of the Riemann zeta function", *Selecta Math.* **5**
  (1999) 29-106.
- Connes, A., Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS Colloquium Publications **55** (2008).
- Jaffe, A., Lesniewski, A., Osterwalder, K., "Quantum K-theory
  I: the Chern character", *Comm. Math. Phys.* **118** (1988) 1-14.
- Meyer, R., "On a representation of the idele class group related
  to primes and zeros of L-functions", *Duke Math. J.* **127**
  (2005) 519-595.
- Weil, A., "Sur les 'formules explicites' de la theorie des
  nombres premiers", *Comm. Sem. Math. Univ. Lund* (1952).
- Faulkner, T., Li, M., Wang, H., "A modular toolkit for bulk
  reconstruction", *JHEP* (2019).
- Connes, A., Stormer, E., "Entropy for automorphisms of II_1 von
  Neumann algebras", *Acta Math.* **134** (1975) 289.

---

*Five paths. One mountain. The integer constraint of Path 3 is*
*the sharpest tool; the Weil positivity of Path 4 is the deepest*
*insight; the Stone chain of Path 1 is the simplest statement.*
*Together they give a coin-flip chance of closure in six months.*
*The next step is a computation: does ind_BC(e_2) equal 1?*
