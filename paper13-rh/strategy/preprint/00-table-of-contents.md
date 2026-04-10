# REVISED 2026-04-10: All 9 referee fixes incorporated

# Paper 13: The Riemann Hypothesis via CCM Operators, ITPFI Convergence, and Boegli Spectral Exactness

## Table of Contents (14 sections)

*Revised 2026-04-10. All 9 referee fixes incorporated.*
*New proof architecture: CCM + ITPFI + Boegli + Hurwitz.*
*The Gelfond-Schneider chain (v1) is killed. This is v2.*
*Theorem 1.1 is conditional on CCM (arXiv:2511.22755).*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*

---

### Front matter

- Title, abstract, MSC codes (11M26, 46L55, 47A10, 58B34)
- Keywords: Riemann hypothesis, Bost-Connes algebra, spectral triples,
  ITPFI factorization, spectral exactness, Hurwitz zero convergence

---

### Section 1. Introduction

*RH (conditional on CCM), the six-layer chain, what's new, notation.*

- 1.1. Statement of the Riemann Hypothesis (Theorem 1.1, conditional on CCM)
- 1.2. Notation and conventions (including lambda disambiguation:
  bandwidth vs spectral parameter vs type III parameter)
- 1.3. The six-layer proof chain (overview diagram)
- 1.4. What CCM did: self-adjoint D_N on E_N^+, eigenvalue approximation,
  the two open steps (N -> infinity limit, eigenvalue identification)
- 1.5. What we add: ITPFI + Boegli + Hurwitz closing CCM's gap
- 1.6. The coboundary lesson: why v1 (Gelfond-Schneider) was killed
- 1.7. Relation to the Integers programme
- 1.8. Organization of the paper

*Key references: CCM arXiv:2511.22755, Boegli arXiv:1604.07732,
Connes-van Suijlekom arXiv:2511.23257, Teschl arXiv:2601.10476*

---

### Section 2. The Integers programme (CBB recap)

*Brief recap of the Critical Bost-Connes-Brauer system. Points to Papers 23-24.*

- 2.1. The Bost-Connes C*-algebra A_BC and the unique KMS_1 state omega_1
- 2.2. The CBB system: quintuple (H_R, R-hat, omega_1, M_geom, {beta_k})
- 2.3. The five axioms (spectral, criticality, geometric, bridge, closure)
- 2.4. The 36 zero-parameter predictions (summary table)
- 2.5. Why RH matters for Integers: spectral axiom consistency

*Key references: Bost-Connes 1995, Papers 23-24, anchor document*

---

### Section 3. CCM zeta spectral triples (Layer 1)

*The CCM construction: operators, self-adjointness, eigenvalues,
even-sector compatibility, the two missing steps we close.*

- 3.1. The prolate wave operator and its Hilbert space
- 3.2. The truncated operators D_N on E_N^+ (even sector)
- 3.3. Self-adjointness via Caratheodory-Fejer (CCM Theorem 4.2)
- 3.4. Even-sector compatibility: T commutes with parity (CCM Lemma 5.2(i))
- 3.5. Eigenvalue identification: spec(D_N) approximates {gamma_n}
  (CCM Theorem 5.10)
- 3.6. The two open steps in CCM:
  - (i) Existence and properties of the limit D_infinity
  - (ii) Exact identification spec(D_infinity) = {gamma_n}
- 3.7. Our strategy: ITPFI for (i), Boegli + Hurwitz for (ii)

*Key references: CCM arXiv:2511.22755 Sections 4-5, Theorem 5.10,
Lemma 5.2(i)*

---

### Section 4. ITPFI factorization (Layer 2)

*The state convergence that drives everything.*

- 4.1. Statement: omega_1 = tensor_p omega_1^p (Theorem 4.1)
- 4.2. Proof 1: Euler product decomposition of KMS_1
- 4.3. Proof 2: BC amenability and product state uniqueness
- 4.4. Proof 3: Araki-Woods ITPFI classification
- 4.5. Consequence: weak-* convergence omega_1^{<=P_N} -> omega_1
- 4.6. Connection to CCM: D_log = modular Hamiltonian of omega_1
- 4.7. The Weil quadratic form and entry-by-entry convergence

*Key references: research/265, Bost-Connes 1995 Theorem 25,
Araki-Woods 1968, Laca-Raeburn 1996*

---

### Section 5. The archimedean estimate (Layer 3a)

*The sub-leading estimate that controls the archimedean contribution.*

- 5.1. Decomposition: tau = tau^{(R)} + Sigma_p tau^{(p)}
- 5.2. The archimedean ratio: norm(tau^{(R)}) / norm(Sigma_p tau^{(p)}) = O(1/lambda)
  (Proposition 5.1)
- 5.3. Proof: Stirling asymptotics at the archimedean place
- 5.4. Davis-Kahan perturbation: eigenvector approximation
  norm(xi_lambda - c . k_lambda) = O(1/lambda) (Proposition 5.2)
- 5.5. The ITPFI triangle inequality: connecting xi_lambda to k_lambda
  through the product structure

*Key references: research/20, research/37, Davis-Kahan 1970*

---

### Section 6. The eigenvector approximation (Layer 3b)

*Closing the gap between D_N eigenvectors and ITPFI product vectors.*

- 6.1. The ITPFI vectors k_lambda in E_N^+
- 6.2. Davis-Kahan sin(theta) theorem applied to D_N
- 6.3. The O(1/lambda) error bound: proof via Proposition 5.1
- 6.4. Uniformity in N: the ITPFI product structure controls
  the approximation independently of truncation level
- 6.5. Consequence: Fourier transforms hat{xi}_N inherit ITPFI structure

*Key references: research/37, Davis-Kahan 1970, Stewart-Sun 1990*

---

### Section 7. Uniform Sobolev regularity (Layer 3c)

*The H^1 bound that provides discrete compactness. Corrected proof
via Fourier-basis cancellation (research/44).*

- 7.1. Resolvent estimate: norm((D_N - i)^{-1})_{L^2 -> H^1}
  <= 1 + C rho^{-N} < 2 (Theorem 7.1, corrected)
- 7.2. Proof: Fourier-basis cancellation -- H^1 weight
  (1 + (2 pi n/L)^2) cancels resolvent denominator ((2 pi n/L)^2 + 1)
  identically; rank-1 quotient correction is O(rho^{-N})
- 7.3. Uniformity in N and in lambda: the bound holds for ALL lambda,
  ALL N, with NO restriction on L = 2 log(lambda)
- 7.4. Uniformity in eigenvector index: all eigenvectors, not just the first
- 7.5. Alternative: CF-based compactness (approach (c) from research/44)
- 7.6. Application to Boegli H2: Rellich-Kondrachov compactness

*Key references: research/44, Reed-Simon II, Rellich-Kondrachov*

---

### Section 8. CF uniform decay (Layer 3d)

*The Caratheodory-Fejer stabilization uniform in N.*

- 8.1. CF approximation on the Bernstein ellipse (rho >= 4.27)
- 8.2. Rank-one perturbation structure
- 8.3. Decay rate: C ~ O(N), uniform in N (Proposition 8.1)
- 8.4. Numerical verification: N = 5, 10, 15, 20, 25, 30
- 8.5. Role in the proof: CF stabilizes the Galerkin approximation
  for the gsrc verification

*Key references: research/35, Baranov-Yakubovich 2021,
CCM arXiv:2511.22755 Section 4*

---

### Section 9. Teschl form convergence + Boegli spectral exactness (Layer 4)

*The heart of the convergence argument.*

- 9.1. Teschl generalized strong resolvent convergence (gsrc)
  - Lemma 2.7: relative bound a = 0 < 1 suffices
  - ITPFI -> form convergence -> gsrc via Galerkin + CF
- 9.2. The three gsrc lemmas (research/40):
  - Lemma 1: explicit norm(Delta_N) <= C rho^{-N}, rho = 19.54
  - Lemma 2: KLMN verification for D_infinity (dense domain,
    closability, bounded below)
  - Lemma 3: AE simplicity sufficiency (identity theorem + Kato)
- 9.3. Boegli hypothesis H1: gsrc (PROVED, Theorem 9.1)
- 9.4. Boegli hypothesis H2: discrete compactness
  (uniform H^1 + Rellich, CLOSED)
- 9.5. Boegli spectral exactness theorem:
  H1 + H2 -> spec(D_infinity) = lim spec(D_N), no spurious eigenvalues

*Key references: Teschl arXiv:2601.10476, Boegli arXiv:1604.07732,
research/38, 40, 41*

---

### Section 10. Hurwitz eigenvalue convergence (Layer 5)

*Identifying the limit spectrum with the Riemann zeros.*

- 10.1. Fourier transforms of eigenvectors: hat{xi}_N
- 10.2. Uniform convergence: hat{xi}_N -> Xi on compact subsets
  (Lemma 7.3 + Estimate b)
- 10.3. Hurwitz's theorem: uniform convergence of holomorphic
  functions -> convergence of zeros (with multiplicity).
  Note: Xi(0) = 0.4971... (not 1/2); the non-vanishing condition
  for Hurwitz is satisfied.
- 10.4. The identification chain:
  - Step 1: each hat{xi}_N has only real zeros (CCM Theorem 5.10(iii)
    + explicit sine-times-rational formula)
  - Step 2: hat{xi}_N -> Xi uniformly on compacts in {|Im z| < 1/2}
    (Estimate (b) + CCM Lemma 7.3)
  - Step 3: Xi(0) = 0.4971... != 0 (non-vanishing at origin)
  - Step 4: By Hurwitz, every zero of Xi in {|Im z| < 1/2} is a limit
    of zeros of hat{xi}_N; since each hat{xi}_N has only real zeros,
    such limits are real
  - Step 5: Zeros of Xi in {|Im z| < 1/2} correspond via s = 1/2 + iz
    to non-trivial zeros of zeta in 0 < Re s < 1
  - Step 6: Therefore every non-trivial zero of zeta is on Re s = 1/2. RH.

*Key references: Hurwitz 1893, Connes-van Suijlekom arXiv:2511.23257
(CMP), CCM Theorem 5.10(iii)*

---

### Section 11. The complete proof (Layer 6 -- Theorem + QED)

*Assembly of all six layers into the final argument.*

- 11.1. Theorem 11.1 (Riemann Hypothesis, conditional on CCM): statement
- 11.2. Proof:
  - Layer 4 (Boegli): spec(D_infinity) = lim spec(D_N)
  - Layer 5 (Hurwitz): lim spec(D_N) = {gamma_n}
  - Combining: spec(D_infinity) = {gamma_n}
  - D_infinity is self-adjoint (from Layer 1 + Layer 4)
  - Therefore: spec(D_infinity) subset R
  - Therefore: gamma_n in R for all n
  - Therefore: all non-trivial zeros of zeta lie on Re(s) = 1/2
  - QED
- 11.3. Remarks on the logical structure

---

### Section 12. AE simplicity and the even-sector modification

*Technical refinement: why the even sector suffices.*

- 12.1. AE simplicity of eigenvalues (Proposition 12.1, research/29)
- 12.2. The parity constraint: CCM Theorem 5.10 requires evenness + simplicity
- 12.3. Even-sector restriction: E_N^+ automatically gives even eigenfunctions
- 12.4. Simplicity in the even sector: AE from Kato perturbation theory
- 12.5. Slepian Compatibility Lemma (NEW, research/45):
  - 12.5.1. Statement: A^{ev}(lambda, N) agrees with N x N
    finite-section of continuous positive integral operator K_lambda
    up to O(e^{-cN})
  - 12.5.2. Kernel identification: Loewner-type kernel from Weil
    distribution Fourier coefficients
  - 12.5.3. Positivity: Krein-Rutman gives strictly simple positive
    ground state
  - 12.5.4. Eigenvector convergence: Karnik-Romberg-Davenport (2021)
    quantitative bounds
  - 12.5.5. Consequence: AE simplicity holds for ALL N, closing the
    Slepian gap for N > 20
- 12.6. Euler-Mascheroni elimination (Lemma 12.2, research/28)
- 12.7. The non-exceptional set: identity theorem guarantees density

*Key references: research/22, 28, 29, 42, 45; Kato perturbation theory;
Slepian-Pollack 1961; Karnik-Romberg-Davenport arXiv:2006.00427*

---

### Section 13. Adversarial review + killed approaches

*Honest accounting: what was tried, what was killed, what survives.*

- 13.1. The 18 killed approaches (summary table from Strategy 10)
- 13.2. The coboundary kill: why Gelfond-Schneider failed
  - H^2 invariants not preserved under continuous delta-deformation
  - Coboundary corrections absorb the shift
  - Lesson: topological invariants need discrete parameters, not continuous
- 13.3. Adversarial review cycles (Strategies 24-26)
  - Initial score: 7/10
  - After three fixes: 8/10
  - Layer-by-layer confidence assessment
- 13.4. The nine referee fixes applied:
  - Fix 1: Final deduction rewritten (explicit Hurwitz + real-zero)
  - Fix 2: Teschl-Boegli interface verified (Thm 2.6, gnrc)
  - Fix 3: H^1 bound corrected (Fourier cancellation, ALL lambda)
  - Fix 4: KLMN closability fixed (Reed-Simon X, three conditions)
  - Fix 5: Slepian compatibility lemma proved (research/45)
  - Fix 6: Theorem 1.1 conditional on CCM
  - Fix 7: Lambda disambiguated throughout
  - Fix 8: Xi(0) = 0.4971 (corrected from 1/2)
  - Fix 9: Even-sector compatibility (CCM Lemma 5.2(i))
- 13.5. What would upgrade to 9/10: CCM journal acceptance
- 13.6. What would upgrade to 10/10: independent third-party verification

*Key references: Strategies 10, 24, 25, 26, 28; research/41, 42, 43, 44, 45*

---

### Section 14. Conclusion

- 14.1. Summary: the six-layer chain and the theorem
- 14.2. What is new: ITPFI + Boegli + Hurwitz closing the CCM gap
- 14.3. The Integers programme: RH as spectral axiom consistency
- 14.4. The coboundary lesson and its methodological implications
- 14.5. Acknowledgments and the role of G's strategic vision
- 14.6. The sentence: "The integers exist. The zeros are on the line."

---

## Appendices (planned)

- A. ITPFI: the three proofs in full (from research/265)
- B. The four estimates: complete epsilon-delta arguments
- C. gsrc lemmas: explicit bounds (from research/40)
- D. Numerical verification tables (CCM eigenvalues vs. Riemann zeros)
- E. The 18 killed approaches: complete list with kill reasons

---

## Section-to-file mapping

| Sections | File |
|:---------|:-----|
| 1-5 | sections-01-05.md |
| 6-10 | sections-06-10.md |
| 11-14 | sections-11-14.md |
| Appendices | appendices.md |

---

## Citation plan (essential)

| Ref | Citation |
|:----|:---------|
| CCM | Connes-Consani-Moscovici 2025, arXiv:2511.22755 |
| Boegli | Boegli 2017, arXiv:1604.07732 |
| CvS | Connes-van Suijlekom 2025, arXiv:2511.23257 (CMP) |
| Teschl | Teschl-Wang-Xie-Zhou 2026, arXiv:2601.10476 |
| BC | Bost-Connes 1995, Selecta Math. |
| Hurwitz | Hurwitz 1893, Math. Ann. |
| RS | Reed-Simon, Methods of Modern Mathematical Physics II |
| AW | Araki-Woods 1968, RIMS |
| LR | Laca-Raeburn 1996, J. Operator Theory |
| BY | Baranov-Yakubovich 2021, rank-one perturbation theory |
| DK | Davis-Kahan 1970, sin(theta) theorem |
| KRD | Karnik-Romberg-Davenport 2021, arXiv:2006.00427 |
| SP | Slepian-Pollack 1961, BSTJ |
