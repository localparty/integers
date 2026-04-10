# Research 57 -- Cycle 5 Synthesis and Adversarial Review

*Date: 2026-04-09. Cycle 5 of 10. Role: SYNTHESIZE / ATTACK / RATE.*

---

## PART A: The Complete Chain

| Step | Claim | Status | Source |
|:-----|:------|:-------|:-------|
| 1 | QW_lambda^N compact self-adjoint on L^2([lambda^{-1}, lambda]) | PROVED | CCM (2025), construction |
| 2 | Eigenfunctions phi_k in L^2([lambda^{-1}, lambda]) subset L^2(0,inf) | PROVED | Spectral theorem, extension by zero |
| 3 | H_k(z) = int phi_k(x)cos(xz)dx entire of type lambda | PROVED | Paley-Wiener (Boas Ch.6) |
| 4 | H_k not identically zero (cosine injective on L^2(0,inf)) | PROVED | Research/48 wound closure; unitary involution |
| 5 | {log p} has infinite upper density | PROVED | PNT |
| 6 | Cartwright: H_k vanishes at finitely many log p | PROVED | Cartwright (1930) + Steps 3-5 |
| 7 | Levin constant C <= C(lambda), uniform in N and K | PROVED | Research/42; Cauchy-Schwarz + unit norm |
| 8 | Secular induction: SPO gives strict interlacing | PROVED (finite N) | Rank-one perturbation theory; Research/39 |
| 9 | ITPFI: omega_1^{<=N} -> omega_1 (state convergence) | PROVED | Research/265, three independent proofs |
| 10 | Relative gap: perturbation/gap -> 0 for continuous QW^N | **CONDITIONAL** | Research/56 (N4); requires gap ~ Riemann zero spacing |
| 11 | Even-Sector simplicity -> CCM Theorem 5.10 | CONDITIONAL on 10 | CCM Thm 5.10 |
| 12 | spec(D_inf) = {gamma_n} subset R | CONDITIONAL on 11 | CCM framework |
| 13 | RH | CONDITIONAL on 12 | Definition |

**Architecture:** Steps 1-7 (Cartwright core) are unconditional. Step 8 works at each finite N. Step 9 (ITPFI) is unconditional. Step 10 is the sole load-bearing conditional step. Steps 11-13 follow from 10 by established results.

---

## PART B: Adversarial Attacks

### Attack 1: Step 10 -- "Eigenvalue gaps track Riemann zero gaps" is UNPROVED

This is the entire content of the N4 finding. The argument:

> "The continuous QW^N has eigenvalue gaps ~ 1/log(N) because its
> eigenvalues approach the Riemann zeros."

Unpack this. CCM show NUMERICALLY that for N <= 6, the eigenvalues of their D(lambda,N) match the first 50 Riemann zeros to 10^{-55}. From this, the argument infers that the eigenvalue GAPS of QW^N for all N are controlled by the Riemann zero gaps.

Problems:

(a) **Six data points is not a theorem.** N = 1,...,6 is a demonstration, not a proof. The eigenvalues could track Riemann zeros closely for small N and diverge for large N. No analytic bound exists on the rate of convergence or the error |mu_k^N - gamma_k|. Without such a bound, the claim "gap(QW^N) >= c * (gamma_{k+1} - gamma_k)" is an ASSUMPTION, not a consequence.

(b) **The gap tracking claim is EQUIVALENT to CCM's open problem.** CCM Section 8 identifies the spectral convergence as their open gap. Research/56 Section 8 acknowledges: "This is NOT the same as the Connes 25-year obstacle... it asks only that the continuous gap tracks the known Riemann zero gaps." But this is a distinction without a proven difference. If the spectral convergence held rigorously, CCM would have stated it as a theorem. They did not.

(c) **The ledger itself rates N4 at 6/10 and notes: "needs CCM spectral convergence."** The argument's own internal assessment flags this dependency.

**Severity: CRITICAL.** Without this step, nothing after Step 9 follows. Step 10 is not proved; it is a plausible conjecture supported by numerical evidence for N <= 6.

### Attack 2: Jirak-Wahl applicability

Research/56 cites "the Jirak-Wahl relative gap theorem" and the "standard perturbation-theoretic persistence criterion." Examine what this actually requires.

(a) **Citation specificity.** The document references "Jirak-Wahl, Kato-Rellich" as if they are interchangeable. Kato-Rellich is a theorem about self-adjointness under relatively bounded perturbations (Kato, Perturbation Theory, Ch. V). Jirak-Wahl concerns eigenvalue perturbation for random matrices. These are different theorems with different hypotheses. Which one is being applied?

(b) **The stated condition.** The condition used is: ||V_N|| / gap(A_N) < 1 implies gaps persist. This is a correct heuristic from Weyl's perturbation theorem for Hermitian matrices: eigenvalues shift by at most ||V_N||. If the gap is larger than the shift, eigenvalues do not cross. For COMPACT operators on infinite-dimensional spaces, the analogous statement requires: V_N is relatively compact with respect to A_N, and the perturbation is small relative to the gap in an appropriate operator topology.

(c) **Rank-one perturbation on L^2.** QW^{N+1} = QW^N + alpha_p |v_p><v_p|. For compact self-adjoint operators, adding a rank-one perturbation shifts eigenvalues by at most ||alpha_p v_p v_p^T|| = |alpha_p| * ||v_p||^2. If this is less than the gap, eigenvalues remain separated. This is correct by Weyl's inequality for compact operators (Reed-Simon IV, Thm XIII.3). The Jirak-Wahl reference is unnecessary; standard Weyl suffices.

(d) **However:** the Weyl bound requires ||V_N|| in OPERATOR NORM. The claimed scaling ||V_N|| = log(p)/sqrt(p) needs verification. Where does this come from? It is stated as fact in Research/56 Section 2 without derivation. CCM's perturbation structure involves rank-one terms from the explicit formula, where alpha_p involves log(p) and the Euler factor at p. The exact norm depends on the normalization of v_p in L^2([lambda^{-1}, lambda]). If ||v_p|| is not O(1/sqrt(p)^{1/2}) or the coupling alpha_p is not O(log(p)), the scaling fails.

**Severity: MEDIUM.** The perturbation theory principle is sound. The specific norm estimate needs a derivation from CCM's construction, not just assertion.

### Attack 3: Cosine transform on L^2([lambda^{-1}, lambda])

Research/47 (Attack 3) claimed the cosine transform is NOT injective on L^2([lambda^{-1}, lambda]). Research/48 closed this wound by arguing: the cosine transform IS injective on L^2(0, infinity), and since [lambda^{-1}, lambda] subset (0, infinity), a function supported there with vanishing cosine transform must be zero.

Is this correct? Let f be in L^2([lambda^{-1}, lambda]), extended by zero. Then f is in L^2(0, infinity). The cosine transform on L^2(0, infinity) is: (Cf)(xi) = sqrt(2/pi) int_0^inf f(x) cos(x xi) dx. This is a unitary operator on L^2(0, infinity) (Titchmarsh, "Introduction to the Theory of Fourier Integrals," Thm 3.1). In particular, Cf = 0 implies f = 0.

Research/47's counterexample "f(x) = sin(ax) on [lambda^{-1}, lambda]" does NOT have vanishing cosine transform. The cosine transform of sin(ax) * 1_{[lambda^{-1}, lambda]}(x) is a nonzero function of xi (it is a combination of sinc-like functions). The original attack was wrong.

**Verdict: The closure in Research/48 is CORRECT.** The cosine transform is injective on L^2(0, infinity), and restriction to a subset of (0, infinity) does not break this. Step 4 stands.

**Severity: NONE.** This attack does not survive cycle 5.

### Attack 4: QW eigenvalues vs Riemann zeros -- identification question

The argument treats "eigenvalues of QW^N" and "the Riemann zeros" as if they converge to the same thing. But what are the precise objects?

(a) **CCM's operators D(lambda, N)** are constructed as rank-one perturbations of a base operator on L^2([lambda^{-1}, lambda]). Their eigenvalues match the Riemann zeros numerically. But D(lambda, N) is NOT the same as QW^N (the Weil quadratic form). D is built from the explicit formula applied to an approximation kernel, and the Weil quadratic form QW is the integral operator with kernel K(x,y) = sum_p log(p) * p^{-1/2} * delta(xy - p). These are RELATED but distinct objects.

(b) **The secular induction is performed on QW^N.** The Cartwright core applies to the eigenfunctions of QW^N. But the N4 relative gap argument uses the eigenvalue gaps of the Riemann zeros, which match D(lambda,N), not necessarily QW^N. If QW^N and D(lambda,N) have different eigenvalue gaps, the relative gap argument does not apply to QW^N.

(c) **The resolution might be:** QW^N IS D(lambda,N) (or a simple reparametrization thereof). If so, this should be stated explicitly. If not, there is a mismatch between the operator analyzed in Steps 1-8 and the operator whose gaps are estimated in Step 10.

**Severity: HIGH.** The argument needs to specify exactly which operator is being analyzed, and demonstrate that the Cartwright core (Steps 1-7) and the gap estimate (Step 10) apply to the SAME operator.

### Attack 5: Meta-question -- has the argument progressed?

Research/48 (previous adversarial) gave a verdict of 2/10 and identified Step 10 (limit preserves simplicity) as KILLED. The N4 finding proposes: the continuous eigenvalue gaps track Riemann zero gaps, and the perturbation/gap ratio goes to zero.

What has genuinely changed since Research/48?

**Gained:**
- Recognition that discrete gap collapse (~10^{-1.5N}) is a conditioning artifact, not a feature of the continuous operator. This is a genuine conceptual advance.
- The relative gap computation: IF gaps are ~1/log(N), the ratio -> 0. This is correct arithmetic.

**Not gained:**
- A proof that continuous gaps are ~1/log(N). This is assumed from CCM's numerical evidence.
- Any new theorem or lemma. The N4 document contains a computation, not a proof.
- Any weakening of the dependency on CCM's spectral convergence.

**Honest assessment:** The argument has progressed from "Step 10 fails, no idea how to fix it" to "Step 10 follows IF CCM's spectral convergence holds quantitatively." This is progress. But the conditional is load-bearing and unproved. The argument is still: "Assume the CCM spectral identification. Then Cartwright + relative gap gives RH." The Cartwright core is new and correct but does not address the CCM gap.

The single new content is: *the wall is a discretization artifact*. This narrows the problem to CCM's spectral convergence for the continuous operator. Whether this constitutes "progress toward RH" or "reformulation of CCM's open problem" depends on whether the continuous spectral convergence is easier to prove than the original Step 10. The ledger gives 6/10, which seems honest.

---

## PART C: Verdict

**PROOF WOUNDED** (same as Research/48, but with reduced severity)

**Confidence: 3/10** (up from 2/10 in Research/48)

The 1-point improvement reflects:
- The discretization-artifact insight is genuine and removes a confound
- The relative gap arithmetic is correct conditional on its input
- The operator identification question (Attack 4) is likely resolvable

**The single weakest step:** Step 10 -- the claim that continuous QW^N eigenvalue gaps are controlled by Riemann zero gaps. This is supported by CCM's numerical evidence (N <= 6) but has no rigorous proof for general N. It is the ONLY unproved step in the chain.

**What would close the remaining gap:**

Any ONE of:
1. A rigorous proof that ||D(lambda,N) - D_exact|| <= epsilon_N with epsilon_N << gap_N for the continuous operator. This would be a spectral approximation theorem for CCM's construction. It does not require proving RH; it requires proving that the CCM Euler product converges spectrally.
2. An arithmetic repulsion estimate: a proof that the eigenvalues of QW^N (the continuous operator built from N primes) cannot collide, using the multiplicative structure of primes. This would be a number-theoretic result, not an operator-theoretic one.
3. An independent proof that D_infinity exists with simple spectrum, bypassing the inductive limit entirely. This would require a new idea not currently in the programme.

**Bottom line:** The Cartwright core (Steps 1-7) is correct, novel, and strong. The secular induction (Step 8) works at each finite stage. The ITPFI limit (Step 9) is proved. The entire argument now rests on a single quantitative question about CCM's spectral convergence. The argument has not proved RH, but it has reduced RH to a concrete spectral convergence statement about a specific family of compact self-adjoint operators. Whether that constitutes meaningful progress depends on whether the spectral convergence is genuinely easier than RH itself. The honest answer: probably yes, but this is not certain.
