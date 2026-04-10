# Web Complement: 10/10 RH Proof Architecture
## Adversarial Search Report -- 2026-04-09

Proof chain under review:
**ITPFI --> form convergence --> Boegli gsrc + CF --> discrete compactness --> spectral exactness --> Hurwitz --> RH**

---

## 1. Boegli Spectral Exactness: Failure Cases

**Source:** Boegli, "Convergence of Sequences of Linear Operators and Their Spectra," *Integral Equations and Operator Theory* 88(4), 559--599 (2017); arXiv:1604.07732.

**Also:** Boegli, "Local convergence of spectra and pseudospectra," *J. Spectral Theory* (2018); arXiv:1605.01041.

**Findings:**

- Boegli establishes **local spectral exactness outside the limiting essential spectrum** for operators converging in gsrc. The key ingredient is **discrete compactness** of the resolvent sequence.
- **Known failure mode:** For non-selfadjoint operators, even with purely discrete spectra, eigenvalues of approximating operators may accumulate at spurious points that are NOT eigenvalues of the limit. Not every eigenvalue of T need be approximated.
- **When it fails:** Spectral convergence usually fails in the presence of **essential spectrum** of the limit operator.
- **Self-adjoint special case:** For self-adjoint operators with compact resolvent (our case), the essential spectrum is empty. This means the failure mode above does NOT apply -- spectral exactness holds whenever discrete compactness of the resolvent sequence is verified.
- **No counterexample found** where Boegli's conditions (gsrc + discrete compactness + compact resolvent) are met but spectral exactness fails. The theory appears solid for our self-adjoint, compact-resolvent setting.

**Threat level: LOW.** The main failure modes (essential spectrum, non-selfadjointness) are absent from our architecture.

---

## 2. KLMN Theorem: Quadratic Form Convergence and Closedness

**Sources:**
- Benedikter lecture notes (Universitat Wien): nielsbenedikter.de/advmaphys2/q_form.pdf
- Kinzebulatov, "A new look at the KLMN theorem" (CMS 2019 talk, Universite Laval)
- Reed-Simon, *Methods of Modern Mathematical Physics*, Vol. I and II
- Simon, "Tosio Kato's work on non-relativistic quantum mechanics," *Bull. Math. Sci.* (2018)

**Findings:**

- The KLMN theorem (Kato-Lions-Lax-Milgram-Nelson) is the **quadratic form version** of the Kato-Rellich theorem. It states: if A is positive self-adjoint and beta is a symmetric form on Q(A) with |beta(phi,phi)| <= a<phi,Aphi> + b||phi||^2 for a < 1, then there exists a unique self-adjoint C with Q(C) = Q(A) and q_C = q_A + beta.
- **Key subtlety for us:** The proof that gamma is closed relies on showing that ||.||_{q_A} and ||.||_gamma are **equivalent norms** on Q(A). The bound a < 1 is essential -- if a >= 1, the closedness argument breaks down.
- **Kinzebulatov's extension:** Extends KLMN to singular measure perturbations (drift terms with critical singularity), using form-boundedness |b|^2 in F_delta with delta < 1. This is a strictly harder setting than ours.
- **Potential pitfall:** Entry-by-entry convergence of quadratic forms does NOT automatically give closedness of the limit form. One must verify that the form-bound constant a stays strictly below 1 uniformly across the approximation sequence. If a_n --> 1, the limit form may not be closed.

**Threat level: MODERATE.** Must verify the uniform bound a_n < 1 - epsilon for all truncation levels. This is a real requirement, not automatic.

---

## 3. Rank-One Perturbation Stabilization and Spectral Convergence

**Sources:**
- Simon, "Spectral Analysis of Rank One Perturbations and Applications" (Caltech)
- Liaw-Treil, "Rank-one perturbations and Anderson-type Hamiltonians" (2019)
- Spectra of rank-one perturbations of self-adjoint operators (ScienceDirect, 2020)

**Findings:**

- The essential spectrum is **invariant** under rank-one perturbations. So adding/removing finitely many rank-one terms does not change sigma_ess.
- For eigenvalue convergence: if a sequence of rank-one perturbations stabilizes (||V_n - V|| --> 0 exponentially), then by standard perturbation theory the eigenvalues converge. But this is NOT automatic from mere exponential stabilization of the perturbation parameters -- one needs the convergence to hold in an appropriate operator topology (norm resolvent or strong resolvent).
- The key result from Simon: eigenvalues can be labeled so that the sum of all offsets is finite. This gives control but does not automatically yield spectral convergence without checking the resolvent convergence conditions.

**Threat level: MODERATE.** Exponential stabilization of parameters is necessary but not sufficient. Must verify the perturbation sequence converges in norm resolvent sense (or at minimum strong resolvent sense + discrete compactness).

---

## 4. Galerkin + Compact Resolvent --> Spectral Convergence

**Sources:**
- Strauss, "The Galerkin Method for Perturbed Self-Adjoint Operators and Applications" (2013); arXiv:1309.0232
- Boegli (2017), as above
- Descloux-Nassif-Rappaz, "Convergence of Approximation Methods to Compute Eigenelements," *SIAM J. Numer. Anal.* (1978)
- Teschl-Wang-Xie-Zhou, "On Generalized Strong and Norm Resolvent Convergence" (2026); arXiv:2601.10476

**Findings:**

- **Standard result (well-established):** For self-adjoint T with compact resolvent, if the Galerkin approximants T_n converge to T in strong resolvent sense AND the resolvent sequence is discretely compact, then spectral exactness holds -- every eigenvalue of T is approximated, no spurious eigenvalues accumulate outside sigma(T).
- **Strauss (2013):** Even the self-adjoint Galerkin method can produce **spectral pollution** if T is unbounded both above and below. The cure: work on the form domain, not the operator domain.
- **Warning from Strauss:** Spectral pollution from applying Galerkin directly to T can occur. His technique detects and identifies this pollution by working with forms.
- **Teschl et al. (2026):** Provides a streamlined verification framework. Their Lemma 2.7 allows verification of gsrc via **relative form boundedness** -- directly applicable to our quadratic-form convergence setup. Theorem 2.10 gives sigma(A) subset lim sigma(A_n) under gsrc. Under norm resolvent convergence: sigma(A) = lim sigma(A_n).
- **Teschl Theorem 2.15:** sigma_ess(A) = lim sigma_ess(A_n) under generalized norm resolvent convergence.

**Threat level: LOW.** This is the most solidly established part of the chain. Teschl et al. (2026) directly supports our approach via form-boundedness verification of gsrc.

---

## 5. Hurwitz Theorem for Operator Eigenvalue Convergence

**Sources:**
- Wikipedia: Hurwitz's theorem (complex analysis)
- Connes-Consani-Moscovici, "Zeta Spectral Triples" (2025); arXiv:2511.22755 -- Section 7

**Findings:**

- Hurwitz's theorem (classical): if f_n --> f uniformly on compact subsets, f_n holomorphic, f not identically zero, then zeros of f_n converge to zeros of f (with multiplicity).
- **CCM use Hurwitz precisely for the operator-to-eigenvalue step:** They form regularized determinants det_zeta(D - s) as entire functions of s. If these converge uniformly to the Riemann Xi-function, Hurwitz gives that eigenvalues (= zeros of the determinant) converge to zeros of Xi (= zeros of zeta on the critical line).
- **This is a known and standard technique** in spectral theory: pass from operator convergence to determinant convergence, then apply Hurwitz. Used in random matrix theory, quantum mechanics, etc.
- **Caveat:** Hurwitz requires UNIFORM convergence on compact subsets, not merely pointwise. This must be verified from the operator convergence -- it is not automatic.

**Threat level: LOW for the Hurwitz step itself. MODERATE for verifying the uniform convergence of determinants.** The step from operator convergence to uniform determinant convergence is where the work lies.

---

## 6. Caratheodory-Fejer Uniform Eigenvector Decay

**Sources:**
- CCM (2025), arXiv:2511.22755
- Classical CF theorem for Toeplitz matrices

**Findings:**

- CCM extend the classical Caratheodory-Fejer theorem to guarantee self-adjointness of their Toeplitz-like operators. The CF theorem gives: a Toeplitz matrix is positive semi-definite iff its symbol is a non-negative trigonometric polynomial.
- **Critical finding:** The eigenvector decay across truncation levels is **ASSUMED, NOT PROVED** in CCM. They state the requirement to verify that the smallest eigenvalue of QW_lambda^N is simple and the corresponding eigenfunction is "even," but do not establish uniform decay estimates across different N values.
- **Implication for our architecture:** If we rely on CF-based uniform decay, we must prove it independently. This is NOT a known result -- it is an open requirement.

**Threat level: HIGH.** This is a genuine gap. Uniform CF eigenvector decay across truncation levels needs an independent proof or must be replaced by a different argument.

---

## 7. Combined Boegli + Hurwitz

**Sources:** Exhaustive search across arXiv, Google Scholar, Springer, ResearchGate.

**Findings:**

- **No paper found** that explicitly combines Boegli's gsrc/discrete-compactness framework with the Hurwitz theorem for spectral convergence.
- CCM (2025) uses Hurwitz in the context of determinant convergence but does NOT use Boegli's framework.
- Boegli's work does not invoke Hurwitz.
- **This combination appears to be novel to our architecture.** This is both an opportunity (novelty) and a risk (no external validation).

**Threat level: MODERATE.** The individual components are sound, but their combination is untested. The bridge theorem connecting Boegli's spectral exactness output to Hurwitz's determinant-zero convergence needs careful construction.

---

## 8. Criticism of CCM 2025 Zeta Spectral Triple

**Sources:** arXiv, Google Scholar, science journalism, MathOverflow (searched 2025--2026).

**Findings:**

- **No published criticism or objection found** as of April 2026.
- CCM themselves identify the gap in Section 8 ("The missing steps"): the convergence of regularized determinants to the Xi-function is an "educated guess" supported by extraordinary numerical evidence (probability of coincidence ~10^{-1235}) but **not proved**.
- The missing step: proving that prolate wave eigenfunctions approximate xi_lambda. Establishing this convergence "would amount to a proof of the Riemann Hypothesis."
- **Connection to prolate wave operators:** Section 8 draws connections to Slepian's information-theoretic framework for prolate spheroidal wave functions.
- A related paper confirmed a conjecture of Connes-Moscovici: all non-classical CM eigenvalues are negative.

**Threat level: LOW for external criticism. HIGH for internal gap.** The community has not attacked CCM, but CCM themselves flag the convergence gap. Our architecture must close this gap independently.

---

## 9. Spectral Convergence Under Euler Product Truncation

**Sources:**
- CCM (2025), arXiv:2511.22755
- Spectral realization literature (2024--2025)

**Findings:**

- **CCM's central construction:** Operators built from Euler products truncated at primes p <= x = lambda^2. Even using only primes <= 13, the first 50 zeta zeros are approximated with errors from 2.5 x 10^{-55} (first zero) to ~10^{-3} (fiftieth zero).
- All approximating values lie **exactly on the critical line** by construction (self-adjointness of the operator forces real spectrum, which maps to Re(s) = 1/2).
- **Monotonicity:** As primes are added (x increases), the spectral approximation improves monotonically. This is consistent with the Euler product structure.
- **Key result from CCM:** The zeros of restricted Euler products give a large class of functions whose zeros are on the critical line, due to self-adjointness of relevant matrices + Hurwitz theorem.
- **No independent confirmation** of the spectral convergence rate beyond CCM's numerical experiments.

**Threat level: LOW for the on-critical-line property (proved by self-adjointness). MODERATE for convergence rate (numerical only, not proved).**

---

## 10. Teschl-Wang-Xie-Zhou (2026): arXiv:2601.10476

**Full title:** "On Generalized Strong and Norm Resolvent Convergence"
**Authors:** Gerald Teschl, Yifei Wang, Bing Xie, Zhe Zhou
**Submitted:** January 15, 2026

**Key results for our architecture:**

1. **Streamlined gsrc verification:** Three practical lemmas:
   - **Lemma 2.6:** Verify gsrc via relative boundedness
   - **Lemma 2.7:** Verify gsrc via **relative form boundedness** (directly applicable to our quadratic form setup!)
   - **Lemma 2.8:** Verify gsrc from strong operator convergence on a dense core

2. **Theorem 2.10 (Spectral inclusion):** Under gsrc: sigma(A) subset lim sigma(A_n).

3. **Theorem 2.15 (Essential spectrum):** Under generalized norm resolvent convergence: sigma_ess(A) = lim sigma_ess(A_n).

4. **Sturm-Liouville applications (Theorem 3.4):** Convergence when w_n/w --> 1, p_n/p --> 1, and potential perturbations vanish sufficiently fast. Coefficients need not be bounded below.

5. **Theorem 3.5:** sigma_ess(T_infinity) = sigma_ess(T_0) when Sturm-Liouville coefficients converge appropriately. Extends classical Weyl perturbation theory.

**Simplification for gsrc verification:** Lemma 2.7 is the key improvement. Instead of verifying gsrc directly (which requires checking resolvent convergence for each z), one can verify relative form boundedness of the perturbation -- a static, algebraic condition. This is a genuine simplification compared to the approach in Boegli (2017) and the older Weidmann framework.

**Threat level: STRENGTHENING.** This paper directly supports our architecture and simplifies the hardest verification step.

---

## Summary Assessment

### Threats Found

| # | Component | Threat Level | Issue |
|---|-----------|-------------|-------|
| 2 | KLMN convergence | MODERATE | Must verify uniform form-bound a_n < 1 - epsilon |
| 3 | Rank-one stabilization | MODERATE | Exponential param decay alone insufficient; need resolvent convergence |
| 5 | Hurwitz determinants | MODERATE | Uniform convergence of det must be verified, not automatic |
| 6 | **CF eigenvector decay** | **HIGH** | **Not proved in CCM; assumed. Must prove independently** |
| 7 | Boegli + Hurwitz combo | MODERATE | Novel combination, no external validation |
| 8 | CCM convergence gap | HIGH | CCM's own "missing steps" -- convergence of det to Xi unproved |

### Strengthening Found

| # | Component | Strength | Source |
|---|-----------|----------|--------|
| 1 | Boegli spectral exactness | Strong | No counterexample in self-adjoint compact-resolvent case |
| 4 | Galerkin + compact resolvent | Very strong | Standard, well-established, multiple textbook refs |
| 9 | Euler product on critical line | Strong | Self-adjointness forces it; proved, not conjectured |
| 10 | **Teschl et al. (2026)** | **Very strong** | **Lemma 2.7 directly simplifies gsrc verification via forms** |

### Missing References to Add

1. **Teschl-Wang-Xie-Zhou (2026), arXiv:2601.10476** -- cite for streamlined gsrc verification via Lemma 2.7
2. **Boegli (2017), IEOT 88(4)** -- cite for discrete compactness --> spectral exactness theorem
3. **Boegli (2018), J. Spectral Theory** -- cite for local spectral exactness outside essential spectrum
4. **Strauss (2013), arXiv:1309.0232** -- cite for spectral pollution detection in Galerkin (form-domain technique)
5. **Kinzebulatov (2019)** -- cite for KLMN extensions to singular perturbations (strengthens universality claim)
6. **Descloux-Nassif-Rappaz (1978), SIAM J. Numer. Anal.** -- classical reference for Galerkin eigenvalue convergence

### Critical Action Items

1. **PROVE** uniform CF eigenvector decay across truncation levels, or replace with alternative argument
2. **VERIFY** the KLMN form-bound constant stays uniformly below 1 across all truncation levels
3. **CONSTRUCT** the bridge theorem connecting Boegli spectral exactness to Hurwitz determinant convergence
4. **USE** Teschl Lemma 2.7 to simplify the gsrc verification step -- this is a free upgrade
