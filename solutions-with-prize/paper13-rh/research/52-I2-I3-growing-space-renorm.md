# Research 52 -- I2 + I3: Growing-Space Limit and Renormalized Kernel

*Date: 2026-04-09. Structure: DEVELOPMENT (A) then ADVERSARIAL (B).*
*Depends on: ledger (I2, I3), research/50 (finite-N context), research/16 (CCM paper)*

---

## PART A: Development

### I2: Growing-space limit

### 1. CCM's construction

D(lambda,N) acts on L^2([lambda^{-1}, lambda]) with N ~ pi(lambda^2). As lambda grows, the Hilbert space GROWS: each new space strictly contains the previous one. The operator adds primes p <= lambda^2, so both the domain and the number of prime contributions increase together. This is NOT the usual "fixed space, growing rank" setup -- it is an inductive system of operators on an inductive system of spaces.

### 2. Hilbert-Schmidt norm estimate

The kernel K_N(x,y) = sum_{p<=lambda^2} (log p / sqrt{p}) cos((x-y) log p) on [lambda^{-1}, lambda]^2. Its HS norm:

||K_N||_HS^2 = int int |K_N(x,y)|^2 dx dy on [lambda^{-1}, lambda]^2.

Cross terms oscillate and contribute lower order. Diagonal terms: each prime p gives ~ (log p)^2 / p times the integration volume ~ lambda^2. Total:

||K_N||_HS^2 ~ lambda^2 sum_{p<=lambda^2} (log p)^2 / p ~ lambda^2 (log lambda)^2

by Mertens' theorem. So ||K_N||_HS ~ lambda log(lambda). This GROWS, but only polynomially in lambda.

### 3. Eigenvalue shrinkage

The eigenvalues of K_N are bounded by ||K_N||_HS / sqrt{rank}. Weyl's law on [lambda^{-1}, lambda] gives rank ~ lambda (number of eigenvalues below a cutoff scales with interval length). Therefore:

|eigenvalue_j| <= ||K_N||_HS / sqrt{lambda} ~ (lambda log lambda) / sqrt{lambda} = sqrt{lambda} log lambda / sqrt{lambda}... 

More carefully: the j-th eigenvalue satisfies sum_j |mu_j|^2 <= ||K||_HS^2. With ~ lambda eigenvalues, the average |mu_j|^2 ~ lambda (log lambda)^2 / lambda = (log lambda)^2. So typical |mu_j| ~ log lambda. Individual eigenvalues are O(log lambda), not shrinking.

Correction to the prompt estimate: eigenvalues do NOT shrink to zero. They stabilize at O(log lambda), consistent with gamma_n ~ log(n) growth of Riemann zeros.

### 4. Eigenvalue gaps vs magnitudes

The gaps between consecutive eigenvalues (Weyl spacing) ~ 1/lambda (from the interval length). Individual eigenvalues ~ log(lambda). So gap/eigenvalue ~ 1/(lambda log lambda) -> 0. This ratio vanishing means that distinguishing individual eigenvalues becomes HARDER as lambda grows, even though the eigenvalues themselves are well-separated in absolute terms.

For GUE repulsion: gap ~ eigenvalue^{-1} (in the bulk), so gap/eigenvalue ~ eigenvalue^{-2}. For Poisson: gap ~ mean spacing ~ 1/lambda, independent of eigenvalue size. The CCM eigenvalues, if they track Riemann zeros, should exhibit GUE statistics (Montgomery-Odlyzko). This makes the gap control HARDER, not easier.

### 5. CCM numerical evidence

CCM verify eigenvalue agreement to 10^{-55} precision for moderate lambda. This is evidence for convergence, not proof. The 10^{-55} precision at finite lambda does not constrain the rate at which errors accumulate as lambda -> infinity.

### 6. Inductive limit framework

Define spaces V_lambda = L^2([lambda^{-1}, lambda]) with inclusion maps i_{lambda_1, lambda_2}: V_{lambda_1} -> V_{lambda_2} (extend by zero). The inductive limit V_inf = colim V_lambda is a locally convex space (NOT a Hilbert space). The operators D(lambda, N) form a compatible family: i_{lambda_1,lambda_2} D(lambda_1, N_1) is "close to" D(lambda_2, N_2) restricted to the image of i. Spectral convergence in the inductive limit topology is the precise formulation of CCM's open gap.

The key subtlety: the inductive limit topology is WEAKER than any Hilbert space topology. Convergence of operators in this topology does not imply convergence of spectra.

---

### I3: Renormalized kernel

### 7. The divergent sum

The QW^inf kernel involves sum_p (log p / sqrt{p}) cos((x-y) log p). Writing t = x-y:

sum_p (log p / sqrt{p}) cos(t log p) = Re[sum_p (log p) p^{-1/2 + it}] = -Re[P'(1/2 + it)]

where P(s) = sum_p p^{-s} is the prime zeta function.

### 8. Analytic properties of P(s)

P(s) converges for Re(s) > 1. It has a logarithmic singularity at s = 1: P(s) ~ -log(s-1) as s -> 1. For Re(s) = 1/2: P(1/2 + it) does not converge, even conditionally. The Mobius inversion P(s) = sum_{n>=1} mu(n)/n log(zeta(ns)) shows that P has a natural boundary on Re(s) = 0 (dense singularities from zeros of zeta(ns)), but the line Re(s) = 1/2 is in the "gap" between convergence (Re > 1) and the natural boundary (Re = 0). No standard regularization makes P(1/2+it) finite.

### 9. Weil explicit formula as renormalization

The Weil explicit formula for a test function h:

sum_rho h(gamma_rho) = h-hat(0) log(pi) + integral terms - sum_p sum_k (log p / p^{k/2}) [h-hat(k log p) + h-hat(-k log p)]

The prime side (RHS) diverges term by term at k=1 when evaluated on the "kernel function." But the zero side (LHS) converges for h in Schwartz class. The explicit formula IS the renormalization: it reorganizes the divergent prime sum into the convergent zero sum plus computable archimedean terms.

The renormalized kernel: define K^{ren}(x,y) via the ZERO side, K^{ren}(x,y) = sum_rho f(gamma_rho, x, y), where f encodes the eigenfunction structure. This converges (for Schwartz test functions) and avoids the divergent prime sum entirely.

### 10. Zero-side operator

QW^{ren} defined via the zero sum: <phi, QW^{ren} psi> = sum_rho <phi, e_rho><e_rho, psi> where e_rho are eigenfunctions. This converges for phi, psi in Schwartz class. The operator is well-defined on S(R) and extends to a distribution on S'(R).

### 11. Circularity question

The zero sum involves {gamma_rho} -- the very quantities whose reality (RH) we want to prove. Using them to define the operator that should prove RH appears circular.

But: the zeros are INPUTS to the operator definition. The OUTPUT is that the operator's eigenvalues are simple and its spectral measure has specific properties. The simplicity then constrains the zero locations. This is self-consistency, not circularity -- the same logical structure as Connes' trace formula approach, where the zeros parametrize a spectral geometry and RH is equivalent to a positivity property of that geometry.

### 12. Connes' programme and the distributional trace

Connes defines a distribution D(f) = sum_rho f-hat(gamma_rho) + (explicit terms). RH is equivalent to D being positive on a specific convex cone. The renormalized kernel I3 is essentially the integral kernel of Connes' distribution restricted to the multiplicative group. This is NOT new -- it is Connes' spectral realisation problem in kernel form.

---

## PART B: Adversarial

### 13. Attack I2: inductive limits do not preserve spectral type

Standard spectral theory (compact operators, self-adjoint operators, trace class perturbations) assumes a FIXED Hilbert space. The inductive limit V_inf is not a Hilbert space. There is no general theorem that says: "if T_n on V_n has spectrum S_n, and T_n -> T on colim V_n, then spec(T) = lim S_n." Counterexamples exist: sequences of compact operators on growing spaces whose inductive limit is not compact (or not even bounded).

The spectral convergence of D(lambda,N) on V_lambda requires BESPOKE analysis of this particular family. No off-the-shelf inductive-limit result applies. This is not a gap that can be closed by citing a theorem -- it requires new estimates specific to CCM's kernel.

**Severity: HIGH.** The framework is correct but empty until filled with CCM-specific bounds.

### 14. Attack I3: Schwartz restriction loses point evaluation

The renormalized kernel K^{ren} is a distribution, not a function. It acts on Schwartz test functions, not on point evaluations. Eigenvalue simplicity requires that eigenfunctions be distinguishable at individual points -- i.e., point evaluation must be meaningful. In the distributional setting, "eigenfunction" means a tempered distribution solving QW^{ren} u = lambda u in S'(R). Such distributional eigenfunctions are not functions and do not have pointwise values.

To recover simplicity: need a regularity theorem showing distributional eigenfunctions are actually smooth (or at least continuous). This is plausible (elliptic regularity for the underlying differential structure) but unproved for QW^{ren}.

**Severity: HIGH.** The distributional framework is well-defined but the simplicity argument requires regularity results that do not yet exist.

### 15. Attack both: reformulation, not resolution

I2 reformulates CCM's convergence gap as inductive-limit spectral convergence. I3 reformulates it as distributional operator theory on the zero side of the explicit formula. Neither introduces a NEW mathematical tool. Both land squarely inside Connes' 25-year spectral realisation programme:

- I2 is the "absorption spectral" approach (add primes, hope spectrum stabilizes).
- I3 is the "trace formula" approach (define operator via zeros, prove positivity).

Connes, Consani, and Marcolli have explored both for decades. The specific new ingredient we bring (Cartwright simplicity at finite N) helps I2 marginally (prevents collisions during induction) but does not address the analytic estimates that are the actual bottleneck.

**Severity: MODERATE-HIGH.** Not fatal (reformulations can still lead to proofs), but the user should not expect these to bypass Connes' obstacles.

---

## VERDICT

**I2 (Growing-space limit): 5/10.**
Mathematically sound framework. The inductive limit formulation is the correct way to state CCM's construction rigorously. The eigenvalue estimates (Section 3-4) show that individual eigenvalues stabilize at O(log lambda) while gaps shrink as O(1/lambda), making the gap-control problem concrete. But no new tool for proving the spectral convergence. Value: clarifies what needs to be proved. Does not prove it.

**I3 (Renormalized kernel): 3/10.**
The Weil explicit formula as renormalization is elegant and correct. But the resulting operator is Connes' distributional trace in disguise (Section 12). The circularity concern (Section 11) is resolvable in principle (self-consistency, not circularity), but the distributional regularity gap (Section 14) is serious. Value: connects CCM's kernel divergence to a known framework. Does not advance beyond that framework.

**Combined assessment:** Both leads are legitimate mathematical reformulations that clarify the structure of the wall (Step 10). Neither provides a new proof technique. They are worth recording as context for future work, but neither should be promoted to active pursuit.

**Recommendation:** Update ledger: I2 to 5/10 (confirmed), I3 to 3/10 (confirmed). Neither warrants dedicated research cycles. Monitor for external progress on inductive-limit spectral theory (I2) or distributional regularity for explicit-formula operators (I3).
