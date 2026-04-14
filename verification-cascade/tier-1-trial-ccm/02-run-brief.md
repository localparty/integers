# Tier 1 Run Brief: CCM Zeta Spectral Triples

*The verification target, the proof chain, the attack surface, and the framework interface. Everything an ORA runner needs to know about WHAT to verify.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-13.*

---

## Target

**Connes, Consani, Moscovici 2025**, "Zeta spectral triples"
arXiv: [2511.22755](https://arxiv.org/abs/2511.22755)

Also relevant (precursor):
**Connes-Consani 2024**, "Zeta zeros and prolate wave operators"
Annals of Functional Analysis (2024). arXiv: [2310.18423](https://arxiv.org/abs/2310.18423)

Also relevant (alternative realization):
**Connes-van Suijlekom 2025**, arXiv: [2511.23257](https://arxiv.org/abs/2511.23257)
Communications in Mathematical Physics (published).

---

## Mode

**VERIFY** (Tier A). Escalate to Tier B/C if WEAKENED/BROKEN found. **PREPRINT** -- apply preprint-specific scrutiny (section 11 of runner instructions).

---

## Why this target

The RH proof chain (Paper 13, "Spectral realization of Riemann zeros via the critical Bost-Connes system") depends on CCM 2025 at **Layer 1** -- the foundation of the entire chain. The chain structure:

```
Layer 1: CCM operators D_N on E_N^+ (self-adjoint, eigenvalues ~ Riemann zeros)  <-- THIS
Layer 2: ITPFI structure of omega_1 (tensor factorization, 3 independent proofs)
Layer 3: Estimates (archimedean, eigenvector, H^1 norm, CF uniformity)
Layer 4: Boegli spectral exactness (gsrc + DC -> no spurious eigenvalues)  [VERIFIED: Tier 4]
Layer 5: Hurwitz zero convergence (xi-hat_N -> Xi uniformly on compacts)
Layer 6: spec(D_infinity) = {gamma_n} subset R -> RH
```

**If CCM has a gap, Layer 1 collapses. The entire RH proof collapses.** CCM provides the operators, the spectral identification, and the convergence of eigenvectors to the Riemann Xi function. Without CCM, there is no spectral realization.

**CCM is a PREPRINT.** It has not been peer-reviewed. Nobody in the world has independently verified it. This verification is the first independent check.

**The Tier 4 pilot (Boegli) validated the verification architecture.** We now apply the same architecture to the highest-value target. The architecture found a real issue in Tier 4 (K-T4-1: standing hypothesis failure in Teschl). We expect CCM to have a higher probability of issues (preprint status).

---

## What CCM's paper constructs

### The Sonin space
A reproducing kernel Hilbert space (RKHS) of entire functions on (0, infinity) equipped with a non-standard inner product: the **T-inner product** derived from Weil's explicit formula. The T-inner product encodes the distribution of prime numbers through the von Mangoldt function Lambda(n).

### The prolate matrix
A finite-rank operator QW_lambda^N (N = number of primes included, lambda = bandwidth parameter, L = 2 log lambda = period). The **minimum eigenvalue** mu_N and corresponding **eigenvector** xi_N of QW_lambda^N are the core objects. The minimum eigenvalue controls positivity; the eigenvector converges to the Riemann Xi function.

### The Caratheodory-Fejer (CF) perturbation
D_N is constructed as D - |D*xi_N><eta_N| where D is the derivative operator, xi_N is the minimum eigenvector, and eta_N is a related vector. The CF theory ensures that this rank-one perturbation of an unbounded operator preserves self-adjointness.

### The even sector
The parity involution gamma splits the Hilbert space into even (E_N^+) and odd (E_N^-) sectors. CCM work in E_N^+ where the minimum eigenvalue is simple and the eigenvector is even. This simplification is essential -- without it, the eigenvector is not unique.

### The spectral identification
The eigenvalues of D_N (restricted to E_N^+) are exactly the zeros of xi-hat_N (the Fourier transform of the eigenvector). As N -> infinity, xi-hat_N -> Xi (the Riemann Xi function) uniformly on compact subsets. By Hurwitz's theorem, the eigenvalues converge to the zeros of Xi, which are the Riemann zeros.

---

## Proof chain to verify (7 load-bearing steps)

| Step | Type | Statement | Depends on | LB? | Risk | Status |
|---:|---|---|---|---|---|---|
| 1* | Foundation | T-inner product is well-defined and positive-definite on E_N^+ | -- | * | Medium | PENDING |
| 2* | Spectral | QW_lambda^N has a minimum eigenvalue that is simple and even | 1 | * | Medium | PENDING |
| 3* | Self-adjointness | CF rank-one perturbation preserves self-adjointness of D_N | 1, 2 | * | Low-Medium | PENDING |
| 4* | Symmetry | T commutes with parity involution gamma (Lemma 5.2(i)): T gamma = gamma T, so E_N^+ is invariant | 1 | * | Low | PENDING |
| 5* | Core claim | Eigenvalues of D_N = zeros of xi-hat_N (Theorem 5.10) | 1, 2, 3, 4 | * | High | PENDING |
| 6* | Convergence | xi-hat_N -> Xi uniformly on compact subsets (Lemma 7.3) | 1, 2 | * | Medium | PENDING |
| 7 | Numerical | Eigenvalues match gamma_n (Riemann zeros) to 10^{-55} at N = 6 | 5 | | Low | PENDING |

Dependencies:
```
1 -> 2 -> 3 -> 5
1 -> 4 -> 5
1 -> 2 -> 6
5 + 6 -> RH.Layer5 (Hurwitz) -> RH.Layer6 (conclusion)
ALL -> RH.Layer1
```

Critical path: 1 -> 2 -> 3 -> 5. If Step 5 SURVIVES, the core spectral identification is verified.
Convergence path: 1 -> 2 -> 6. If Step 6 SURVIVES, the Hurwitz argument is enabled.
Both paths required for the RH proof.

---

## Verification protocol per step

For each of the 7 steps, the Verifier executes:

1. **READ** the relevant CCM paper section (download via WebFetch from arXiv:2511.22755). Cross-reference with CCM 2024 (arXiv:2310.18423) where cited.
2. **RESTATE** the claim in your own words. Do not parrot the paper.
3. **IDENTIFY** all assumptions:
   - Explicit: stated hypotheses
   - Implicit: domain assumptions, topological requirements, convergence conditions
   - Standing/ambient: hypotheses at section headers that apply to all results in the section (LESSON-1)
   - External citations: for each cited result, list its own hypotheses and verify they hold in CCM's context
4. **CHECK** the proof step by step. For each deduction:
   - Is the step justified? By what prior result?
   - Is the step reversible?
   - Are there edge cases?
5. **RE-DERIVE** independently if possible
6. **SELF-SUSPECT** (Signature 2): "Am I reading this wrong? Am I filling in a gap the paper does not actually bridge? Am I trusting the Fields Medal instead of trusting the proof?"

---

## Attack surface -- what to look for

### On Step 1 (T-inner product, positive-definite)
- Is the T-inner product actually positive definite, or only positive semi-definite? If semi-definite, the quotient construction is needed and must be checked.
- Positive-definiteness depends on Weil's explicit formula and the distribution of primes. Does the positivity hold for ALL test functions in E_N^+, or only for a dense subset?
- Is there a standing hypothesis about the class of test functions (Schwartz class, compactly supported, etc.) that is used but not always restated?
- Does the T-inner product depend on N (the truncation level)? If so, are the inner product spaces for different N compatible?
- **Weil positivity**: the positivity criterion ultimately relies on the fact that the Weil distribution is positive on E_N^+. This is the deepest claim -- if it fails, everything fails.

### On Step 2 (minimum eigenvalue, simple and even)
- Is simplicity of the minimum eigenvalue proved for all N, or only for generic N? If generic, is there a concrete N where simplicity fails?
- Does the "almost-everywhere" (AE) argument in Paper 13 Section 12 apply here, or is CCM's own argument self-contained?
- Is the parity of the eigenvector (even) a consequence of the operator structure, or does it require an additional argument?
- Does the simplicity depend on the bandwidth parameter lambda? If lambda is poorly chosen, could the minimum eigenvalue have multiplicity > 1?
- **Analytic perturbation theory**: if the eigenvalues of QW_lambda^N are analytic functions of lambda, simplicity is generic. But is analyticity proved?

### On Step 3 (CF self-adjointness)
- Does CF theory (Caratheodory-Fejer) apply when the base operator D is unbounded? The classical CF theory is for bounded operators / finite matrices.
- Is the perturbation |D*xi_N><eta_N| a bounded operator? If D is unbounded and xi_N is in dom(D), then D*xi_N is a fixed vector and the perturbation IS bounded (rank-one with fixed vectors). But is xi_N actually in dom(D)?
- Does the rank-one perturbation preserve the domain of D? (Self-adjointness requires same domain.)
- Is there a subtlety with the unboundedness of D that the CF analogy misses?
- **Kato-Rellich**: if the perturbation is relatively bounded with bound < 1, self-adjointness follows from Kato-Rellich. Check whether CCM uses this route or a different one.

### On Step 4 (T gamma = gamma T)
- Is this a direct computation, or does it depend on structural properties of the T-inner product?
- Check on explicit basis elements: if f(x) is in the Sonin space, is T(gamma f) = gamma(Tf)? Write out both sides.
- Does the commutativity extend to the completion of the Sonin space, or only to a dense subspace?
- Are there domain issues? (T and gamma must be defined on compatible domains.)

### On Step 5 (eigenvalue identification -- THE CORE CLAIM)
- This is the most important step. The eigenvalues of D_N must be EXACTLY the zeros of xi-hat_N.
- Does the identification require analytic continuation? (D_N is defined on L^2; xi-hat_N is an entire function of exponential type. The connection between operator eigenvalues and zeros of an entire function may require going outside the Hilbert space.)
- Is the spectral identification a consequence of the construction (D_N is designed so its eigenvalues are the zeros), or does it require a separate proof?
- Does the identification hold for ALL eigenvalues, or only for simple eigenvalues?
- **Paley-Wiener**: the Fourier transform maps the Sonin space to a space of entire functions of exponential type (Paley-Wiener space). Is this identification rigorous for the T-inner product (non-standard)?
- **Multiplicity**: if xi-hat_N has a double zero at some point, does D_N have a double eigenvalue? Or does the rank-one perturbation split multiplicities?

### On Step 6 (uniform convergence, xi-hat_N -> Xi)
- What is the rate of convergence? Is it polynomial or exponential in N?
- Is "uniform on compact subsets" strong enough for Hurwitz's theorem? (Hurwitz requires uniform convergence on compact subsets -- so yes, IF the convergence is truly uniform and not just pointwise.)
- Does the convergence of xi-hat_N to Xi follow from the convergence of xi_N (the eigenvector) in the Sonin space? If so, which norm controls the convergence?
- **Prolate approximation quality** (Lemma 7.2): the eigenvector xi_N approximates the CCM prolate function. Is the approximation in L^2 norm, Sobolev norm, or pointwise? The strength of the approximation determines the strength of the convergence of xi-hat_N.
- Does the uniform convergence extend to vertical strips of bounded width, or only to bounded rectangles? (The Riemann zeros extend to infinity along the critical line.)

### On Step 7 (numerical verification)
- The claimed accuracy is 10^{-55}. Is this with interval arithmetic / rigorous error bounds, or floating-point only?
- At N = 6 (primes 2, 3, 5, 7, 11, 13), how many Riemann zeros are captured?
- Can the computation be independently reproduced?

---

## Framework interface

### If CCM SURVIVES (expected outcome given author caliber)
- RH Layer 1 is **secure**
- RH confidence: 8/10 -> 9/10
- The verification cascade proceeds to Tier 2 (Balaban verification for YM)
- The SURVIVED verdict is documented for the Clay submission
- This is the first independent verification of CCM -- itself a publishable result

### If CCM is WEAKENED
- Classify as CLOSABLE or GENUINE
- If CLOSABLE:
  - Identify the fix. Note it for the CCM authors.
  - RH confidence stays at 8/10 (the fix is standard)
  - Paper 13 adds a note: "We independently verified CCM 2025 and found [N] presentation-level issues, all closable."
- If GENUINE:
  - Escalate to **Tier B**: Connes-van Suijlekom (arXiv:2511.23257) provides an alternative spectral realization via Segal-Bargmann-Fock space. If CvS has the same spectral identification without the gap, the RH proof can route through CvS instead.
  - Escalate to **Tier C**: construct D_infinity directly from ITPFI + Boegli without CCM. This is harder but would make the RH proof fully self-contained.
  - RH confidence drops to 6/10 pending escalation

### If CCM is BROKEN
- This is a significant finding. A fundamental gap in a Connes preprint.
- Escalate to **Tier C immediately**: construct spectral realization of Riemann zeros without CCM
  - Route 1: ITPFI structure + Boegli spectral exactness + direct operator construction on Bost-Connes KMS states
  - Route 2: Connes-van Suijlekom alternative realization (if the gap is specific to CCM, not to the general approach)
  - Route 3: entirely new spectral realization using the framework's own tools (QG5D geometric operators)
- RH confidence drops to 4/10 pending bypass construction
- The finding itself should be communicated to the authors

---

## Escalation routes per step

### Step 1 (T-inner product)

| Tier | Route | Source |
|---|---|---|
| B | Verify Weil positivity via alternative formulation: the T-inner product is positive iff the Weil distribution W is positive on the relevant test function space. Check against Li's positivity criterion (Li 1997, Bombieri-Lagarias 1999). | Li, "The positivity of a sequence..." (1997) |
| B | Use Connes-van Suijlekom's Segal-Bargmann-Fock realization, which has a different (standard L^2) inner product. If CvS avoids the T-inner product entirely, the positivity issue is bypassed. | CvS 2025, arXiv:2511.23257 |
| C | Construct the inner product from the framework's quantum information pillar: mutual information of BC states provides a natural positive-definite form. Prove equivalence with the T-inner product. | Paper 13 Layer 2 (ITPFI) |

### Step 2 (minimum eigenvalue simplicity)

| Tier | Route | Source |
|---|---|---|
| B | Use analytic perturbation theory (Kato Ch. II) to prove that eigenvalues of QW_lambda^N are analytic in lambda, hence simple for generic lambda. Then verify that the specific lambda used in CCM is generic. | Kato, Perturbation Theory, Ch. II |
| B | Prove simplicity from the structure of the prolate matrix: QW_lambda^N has positive entries (Perron-Frobenius), so the minimum eigenvalue of the INVERSE is simple. Check if this argument applies. | Perron-Frobenius theorem |
| C | Accept multiplicity > 1 as possible and modify the RH argument to handle non-simple eigenvalues. The spectral identification (Step 5) may still work with degenerate eigenvalues if the eigenspace is well-behaved. | Paper 13, modified Layer 1 |

### Step 3 (CF self-adjointness)

| Tier | Route | Source |
|---|---|---|
| B | Use Kato-Rellich perturbation theory: if the rank-one perturbation is D-bounded with relative bound < 1, self-adjointness follows from Kato-Rellich (Reed-Simon II, Thm X.12). This is independent of CF theory. | Reed-Simon II |
| B | Use KLMN (form-bounded perturbation): if the perturbation is form-bounded with bound < 1, self-adjointness follows from KLMN. Check if this applies to CCM's rank-one perturbation. | Reed-Simon II, Thm X.17 |
| C | Construct D_N as a self-adjoint operator ab initio, without routing through "base operator + perturbation". Use the Friedrichs extension of the quadratic form associated to D_N. | Friedrichs extension theorem |

### Step 4 (T gamma = gamma T)

| Tier | Route | Source |
|---|---|---|
| B | Verify by direct computation on the Fourier side: gamma corresponds to complex conjugation of the Fourier transform. T is the Weil explicit formula operator. Check commutativity on the Fourier side. | Standard Fourier analysis |
| C | Not needed -- if T gamma != gamma T, the even sector is not invariant, and the entire CCM construction needs restructuring. This would be BROKEN, not WEAKENED. | -- |

### Step 5 (eigenvalue identification)

| Tier | Route | Source |
|---|---|---|
| B | Independent derivation via the Paley-Wiener theorem: eigenvalues of D_N correspond to zeros of the characteristic function of D_N in the Paley-Wiener space. If xi-hat_N IS the characteristic function, the identification follows. | Paley-Wiener, Koosis (1988) |
| B | Use Connes-van Suijlekom's alternative spectral identification (if CvS has the same theorem via a different route). | CvS 2025 |
| C | Construct the spectral identification directly from the ITPFI structure: the eigenvalues of D_N can be read off from the ITPFI factors, each factor contributing log(p) for prime p. The spectral identification is then a direct consequence of the tensor product structure. | Paper 13 Layer 2 |

### Step 6 (uniform convergence)

| Tier | Route | Source |
|---|---|---|
| B | Prove uniform convergence via Slepian's prolate function theory: the prolate spheroidal wave functions converge to the sinc function uniformly on compacts. If xi_N is a prolate function, convergence to Xi may follow from Slepian's estimates. | Slepian (1961-1983) |
| B | Prove convergence in a stronger topology (e.g., H^1 norm) and deduce uniform convergence via Sobolev embedding. | Sobolev embedding + Morrey inequality |
| C | Bypass uniform convergence entirely: if spectral exactness (Boegli, Tier 4 VERIFIED) gives spec(D_infinity) = lim spec(D_N), then eigenvalue convergence follows without needing xi-hat_N -> Xi. | Boegli Thm 2.6 (VERIFIED) |

### Step 7 (numerical)

| Tier | Route | Source |
|---|---|---|
| B | Independent numerical computation using PARI/GP or SageMath. | Computational verification |
| C | Not needed -- numerical step is confirmatory, not load-bearing. | -- |

---

## Honest assessment

CCM is authored by Alain Connes (Fields Medal 1982, foundational work in noncommutative geometry and operator algebras), Caterina Consani (expert in arithmetic geometry and NCG), and Henri Moscovici (expert in cyclic cohomology and index theory). This is a top-tier author team.

**Probability of a fundamental gap: LOW (~5-10%).** Despite preprint status, the authors are among the most careful mathematicians alive. The spectral realization approach has been developed over 20+ years (Connes' programme on RH via NCG). The current paper builds on the published CCM 2024 paper.

**Probability of a presentation/precision gap: MEDIUM (~20-30%).** Preprints often have notation inconsistencies, implicit assumptions, and steps that are "clear to the authors" but not fully written out. These are CLOSABLE issues.

**Probability of a standing-hypothesis issue: MEDIUM-HIGH (~30-40%).** LESSON-1 from Tier 4: standing hypotheses are the #1 risk. CCM likely cites results from functional analysis, prolate function theory, and number theory. Each citation is an attack surface where the cited theorem's hypotheses may not hold in CCM's non-standard context (T-inner product instead of L^2, Sonin space instead of Schwartz space, etc.).

**The preprint paradox:** the authors' caliber REDUCES the probability of fundamental gaps but DOES NOT reduce the probability of standing-hypothesis issues or presentation gaps. Standing hypotheses are easy to miss regardless of expertise -- they are a formatting issue, not a competence issue.

**Verify as if expecting BROKEN. Report as if expecting SURVIVED. The discipline is the product.**
