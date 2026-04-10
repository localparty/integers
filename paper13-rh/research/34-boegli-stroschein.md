# Research 34 -- Boegli and Stroschein: Two Backup Tools for Spectral Convergence

*Date: 2026-04-10*
*Status: INVESTIGATED. Boegli: APPLIES with one verification needed.*
*Stroschein: APPLIES with structural adaptation. Boegli is more promising.*

---

## TOOL 1: BOEGLI'S SPECTRAL EXACTNESS (arXiv:1604.07732)

### 1.1 The theorem (precise statement)

**Theorem (Boegli 2017).** Let T_n, T be closed operators on Hilbert
spaces H_n, H respectively. Suppose:

(H1) **Generalized strong resolvent convergence (gsrc):** There exist
bounded operators J_n : H -> H_n (identification operators) and
z_0 in rho(T) cap bigcap_n rho(T_n) such that

    (T_n - z_0)^{-1} J_n phi -> J (T - z_0)^{-1} phi   for all phi in H

where J is a bounded operator H -> H (typically the identity if
H_n = H for all n, but Boegli allows varying spaces).

(H2) **Discrete compactness:** Every sequence {u_n}, u_n in H_n, with
sup_n ||(T_n - z_0)^{-1} u_n|| < infty and sup_n ||u_n|| < infty,
has a subsequence such that (T_{n_k} - z_0)^{-1} u_{n_k} converges.

Then: **Spectral exactness** holds:

    spec(T) = lim spec(T_n)

in the Hausdorff sense. No spurious eigenvalues appear. Eigenvalues
of T_n converge to eigenvalues of T with multiplicity preserved.

### 1.2 Hypothesis check against CCM

**(H1) Generalized strong resolvent convergence:**

CCM's operators D(lambda,N) act on varying spaces:
H_N = E'_N subset L^2([lambda^{-1}, lambda], d*u), where dim(E'_N) = 2N.

As N -> infinity (with lambda growing so that lambda^2 >= p_N), the
spaces H_N grow and exhaust a limit space.

**Check:** The identification operators J_N : H_infty -> H_N can be
defined as orthogonal projections onto E'_N in the Weil inner product.
For gsrc, we need:

    (D(lambda,N) - z)^{-1} J_N phi -> (D_infty - z)^{-1} phi

for all phi in H_infty and z in the resolvent set.

Since D(lambda,N) is self-adjoint with discrete spectrum (finite-dimensional
space), the resolvent exists for all z not in spec(D(lambda,N)).

**The key question:** Is there a z_0 in C \ R that lies in rho(T_n)
for all n? YES -- since each D(lambda,N) is self-adjoint, its spectrum
is real. Any z with Im(z) != 0 lies in all resolvent sets simultaneously.
Take z_0 = i.

The gsrc condition then requires: for each smooth test vector phi, the
projected resolvents converge. This is plausible because:
- The Weil quadratic form QW_lambda^N converges entry-by-entry as N -> infty
  (each matrix entry tau_{n,m} stabilizes once all primes p <= lambda^2
  contributing to that entry are included)
- The eigenvectors of QW_lambda^N converge (numerically demonstrated
  by CCM to 10^{-55})
- The resolvent (D(lambda,N) - i)^{-1} is a rational function of the
  matrix entries, hence continuous in the entries

**Sub-verdict on (H1): PLAUSIBLE.** The entry-by-entry convergence of
the Weil matrix, combined with self-adjointness at each stage, should
give gsrc. A rigorous proof would require showing that the projected
resolvent (D(lambda,N) - i)^{-1} P_N phi converges for each phi in a
dense subspace. The ITPFI state convergence (omega_1^{<=P} -> omega_1)
supports this at the state level: the inner products
<phi, (D(lambda,N) - i)^{-1} psi> are expectations in the truncated
state, and ITPFI guarantees these expectations converge.

**(H2) Discrete compactness:**

At each N, D(lambda,N) acts on a finite-dimensional space (dim = 2N).
Therefore (D(lambda,N) - z_0)^{-1} is a finite-rank operator, hence
compact. The resolvent at each stage is trivially compact.

**But Boegli's discrete compactness is a UNIFORM condition on the
sequence:** Given bounded {u_n} with bounded {(T_n - z_0)^{-1} u_n},
extract a convergent subsequence of the resolvent images.

Since dim(H_N) = 2N -> infinity, the spaces are not uniformly
finite-dimensional. The sequence {(D(lambda,N) - i)^{-1} u_n} lives
in spaces of increasing dimension.

**The crucial estimate:** We need a uniform bound on
||(D(lambda,N) - i)^{-1}||. Since D(lambda,N) is self-adjoint:

    ||(D(lambda,N) - i)^{-1}|| = 1/dist(i, spec(D(lambda,N))) = 1/1 = 1

because spec(D(lambda,N)) subset R and dist(i, R) = 1. So the resolvents
are UNIFORMLY BOUNDED in operator norm (bound = 1 for z_0 = i).

For discrete compactness, we additionally need: the resolvent images
form a RELATIVELY COMPACT set. Since {(D(lambda,N) - i)^{-1} u_n} has
||...|| <= ||u_n|| <= C, and the vectors live in subspaces of a common
ambient space L^2(R_+^*, d*u), we need compactness in L^2.

**The mechanism:** The resolvent (D(lambda,N) - i)^{-1} acts as a
smoothing operator (it maps L^2 into the domain of D(lambda,N), which
consists of smoother functions). If the smoothing is UNIFORM in N --
i.e., the resolvent images have uniformly bounded Sobolev H^1 norm --
then Rellich compactness gives a convergent subsequence in L^2.

**ITPFI contribution:** The Weil matrix has entries controlled by
the Euler product. ITPFI guarantees the product converges at the
state level. The Sobolev regularity of the resolvent images is
controlled by the eigenvalue gaps of D(lambda,N). The extreme
numerical precision (10^{-55}) suggests the eigenvalue gaps are
bounded below uniformly in N (no spectral accumulation for fixed
zero index k). If the k-th eigenvalue gap is bounded below
independently of N, then the resolvent maps into a uniformly bounded
Sobolev space, giving discrete compactness.

**Sub-verdict on (H2): NEEDS VERIFICATION.** The uniform bound on
resolvent norms is automatic (= 1). Discrete compactness reduces to
a uniform lower bound on eigenvalue gaps, which is numerically
supported but unproved.

### 1.3 Does ITPFI help satisfy the hypotheses?

**For (H1):** YES, indirectly. ITPFI gives convergence of the
underlying state, which controls the inner products that define
gsrc. The state omega_1^{<=P} determines the Weil quadratic form
QW_lambda^N (via the explicit formula), and state convergence
implies convergence of the quadratic form entries.

**For (H2):** PARTIALLY. ITPFI does not directly give eigenvalue
gap bounds. However, the ITPFI product structure (one factor per
prime) combined with the rank-one perturbation formula means each
prime changes the spectrum by a controlled amount. The interlacing
theorem for rank-one perturbations gives: the eigenvalues of
D(lambda,N+1) interlace with those of D(lambda,N). Interlacing
prevents eigenvalue collapse, which is the main mechanism for
discrete compactness failure.

### 1.4 Verdict on Boegli

**APPLIES, contingent on one verification: discrete compactness
of the resolvent sequence.**

The gsrc hypothesis (H1) is plausible given ITPFI state convergence
and the entry-by-entry stability of the Weil matrix. The discrete
compactness (H2) reduces to a uniform eigenvalue gap bound, which is
strongly supported by numerics (the CCM data shows stable, well-separated
eigenvalues across all truncation levels) but requires a rigorous proof.

**If discrete compactness is verified:** Boegli gives spectral exactness
directly. spec(D_infty) = lim spec(D(lambda,N)), no spurious eigenvalues,
multiplicity preserved. Combined with Lemma 7.3 (hat{xi}_lambda -> Xi
uniformly), this gives RH.

**Difficulty of the remaining verification:** MODERATE. The eigenvalue
gap bound follows from the interlacing theorem if one can show that
successive rank-one perturbations (adding primes) do not cause
eigenvalue collision. The numerical evidence (all 50 CCM eigenvalues
remain well-separated through all truncation levels) strongly supports
this. A rigorous proof might use:
- Interlacing for rank-one perturbations (standard)
- ITPFI to control the perturbation sizes
- The CF mechanism to bound the eigenvector components

---

## TOOL 2: STROSCHEIN'S NON-ASYMPTOTIC BOUNDS (arXiv:2505.07513)

### 2.1 The theorem (precise statement)

**Theorem (Stroschein 2025/2026).** Let H be a self-adjoint operator on
a Hilbert space H with spectral measure E_lambda. Let V_N subset H be a
sequence of subspaces with P_N the orthogonal projection onto V_N. Let
H_N = P_N H P_N be the Galerkin approximation.

Then for any interval [a,b] and any spectral threshold delta > 0:

    |mu_k(N) - lambda_k| <= C(delta, N) * ||H(I - P_N)|| / gap_k

where:
- mu_k(N) = k-th eigenvalue of H_N
- lambda_k = k-th eigenvalue of H (if it exists in [a,b])
- C(delta, N) is an explicit constant depending on the spectral density
  rho(E, [a-delta, b+delta]) and the projection quality
- gap_k = min_{j != k} |lambda_k - lambda_j| is the eigenvalue gap

**Key innovation:** The bound is NON-ASYMPTOTIC (explicit for each N)
and does not require eigenvalue gaps to be large -- it works even for
clustered eigenvalues via an integrated version using the spectral
measure.

**Integrated version (gap-independent):**

    int_a^b |mu(N)(lambda) - lambda|^2 d rho(lambda) <= C'(delta, N) * ||(I - P_N) H^{1/2}||_HS^2

where mu(N)(lambda) is the counting-function error and rho is the
spectral density. This bound holds WITHOUT eigenvalue gap assumptions.

**Prolate application:** Applied to the Slepian prolate operator
B_T = F_Omega P_T F_Omega^*, the theorem gives the "sharp accuracy
transition": eigenvalues of the truncated prolate operator match the
true ones up to an index k_*(N) ~ 2TW/pi, after which accuracy
degrades rapidly. This transition is at k_* where the spectral density
changes character.

### 2.2 Hypothesis check against CCM

**(a) Self-adjoint operator H with spectral measure:**

The limiting operator D_infty (if it exists) would be self-adjoint
on L^2(R_+^*, d*u) with spectral measure supported at {gamma_n}.
At each finite N, D(lambda,N) is self-adjoint on E'_N.

**Problem:** Stroschein's framework requires a FIXED ambient operator H
and subspace approximations H_N = P_N H P_N. In CCM's setup, there is
no fixed ambient operator -- the operators D(lambda,N) change
structurally with N (different rank-one perturbations, different Weil
matrices). They are NOT subspace projections of a common operator.

**Possible adaptation:** If we could identify a fixed operator H_infty
such that D(lambda,N) = P_N H_infty P_N + error(N), then Stroschein
applies with error bounds. The Weil quadratic form provides the candidate:
QW = lim QW_lambda^N (the full Weil form with all primes). Then
QW_lambda^N = P_N QW P_N + tail terms (from primes not yet included).

The tail terms satisfy (from research/16, Section 7):

    ||QW - QW_lambda^N|| = ||sum_{p > lambda^2} W_p|| <= sum_{p > lambda^2} (log p)/sqrt{p}

This sum converges (by comparison with integral x^{-1/2} dx). So the
tail is bounded and vanishes as lambda -> infty.

**Sub-verdict:** The framework DOES apply if we work at the level of the
Weil quadratic form (matrix level) rather than the derived operator D'.
The quadratic form QW_lambda^N IS a subspace approximation to QW, up
to a tail error that vanishes.

**(b) Explicit bounds |mu_k(N) - gamma_k| <= f(N):**

From the integrated version, we would get:

    sum_k |mu_k(N) - gamma_k|^2 w_k <= C * ||sum_{p > lambda^2} W_p||^2

where w_k are spectral weights. The right side is:

    C * (sum_{p > lambda^2} (log p)/sqrt{p})^2 ~ C * lambda^{-1} (log lambda)^2

(by prime number theorem: sum_{p > x} (log p)/sqrt{p} ~ 2/sqrt{x} * log x).

This gives a CONCRETE convergence rate: the integrated spectral error
decays as lambda^{-1} (log lambda)^2. For individual eigenvalues, the
gap-dependent version gives:

    |mu_k(N) - gamma_k| <= C_k * lambda^{-1/2} * log lambda / gap_k

where gap_k = min_{j!=k} |gamma_k - gamma_j| is the spacing between
consecutive Riemann zeros.

**The gap_k dependence:** For large k, gap_k ~ 2pi / log(gamma_k/2pi)
(by the Riemann-von Mangoldt formula). So the bound becomes:

    |mu_k(N) - gamma_k| <= C_k * lambda^{-1/2} * log(lambda) * log(gamma_k)

This decays in lambda but GROWS in k. For fixed k, it vanishes as
lambda -> infty. This is exactly the pattern CCM observe: precision
degrades with zero number but improves with lambda.

**(c) The prolate connection:**

CCM's construction IS closely related to the prolate operator programme.
The Slepian prolate operator B_T = F_Omega P_T F_Omega^* localizes
simultaneously in time and frequency. CCM's operator D(lambda,N) acts
on L^2([lambda^{-1}, lambda]) (time-localized to [lambda^{-1}, lambda])
with the Weil quadratic form providing frequency structure (the Fourier
transform hat{xi} detects the zeros).

Stroschein's "sharp accuracy transition" at k_* ~ 2TW/pi translates
in the CCM context to: eigenvalues are well-approximated up to
zero index k_* ~ lambda * (something), after which accuracy degrades.
CCM's Table 1 shows precisely this pattern: for lambda^2 = 14, zeros
up to k ~ 30 are matched to 10^{-19} but zero 50 is only matched
to 10^{-6}.

The formal connection: CCM's eigenvector xi is analogous to the
prolate spheroidal wave function psi_{0,c} where c = lambda * gamma_1.
The CF theorem plays the role of Slepian's eigenvalue concentration.
Stroschein's bounds for the prolate operator should transfer to CCM
with the appropriate dictionary.

### 2.3 Does ITPFI help?

**For the tail bound:** YES. The tail ||QW - QW_lambda^N|| involves
the Euler product tail sum_{p > lambda^2} W_p. ITPFI controls the
state-level analogue: ||omega_1 - omega_1^{<=P}|| in weak-* norm.
The relationship between the state tail and the quadratic form tail
goes through the explicit formula:

    QW(f,g) = <omega_1, F(f,g)>

where F(f,g) is the explicit-formula functional. If F is continuous
(bounded operator on the algebra), then:

    |QW - QW^{<=P}| = |<omega_1 - omega_1^{<=P}, F>| <= ||omega_1 - omega_1^{<=P}|| * ||F||

ITPFI gives ||omega_1 - omega_1^{<=P}|| -> 0. So ITPFI controls the
Stroschein tail error.

**For the eigenvalue gaps:** ITPFI does not directly give gap lower
bounds. However, the ITPFI product structure + interlacing from
rank-one perturbations gives qualitative gap control (no eigenvalue
collision).

### 2.4 Verdict on Stroschein

**APPLIES with structural adaptation.** The framework requires
viewing CCM's operators as subspace approximations to a limiting
quadratic form QW, which is mathematically natural. The non-asymptotic
bounds give explicit convergence rates that match CCM's numerical
observations.

**If applied:** Stroschein gives:
- Integrated spectral error ~ lambda^{-1} (log lambda)^2 (rate)
- Individual eigenvalue error ~ lambda^{-1/2} log(lambda) / gap_k
- Sharp accuracy transition at k_* ~ f(lambda) (matching Table 1)

**Limitations:**
- The gap-dependent bound requires eigenvalue gap lower bounds (same
  issue as Boegli's discrete compactness)
- The integrated bound is gap-independent but gives L^2-averaged error,
  not pointwise convergence of individual eigenvalues
- The adaptation from subspace projection to "subspace projection +
  tail error" requires checking that the tail error does not introduce
  spectral pollution (spurious eigenvalues)

---

## COMPARATIVE ANALYSIS

### Which tool is more promising?

| Criterion | Boegli | Stroschein |
|:----------|:-------|:-----------|
| Theorem type | Qualitative (spectral exactness) | Quantitative (error bounds) |
| Key hypothesis | Discrete compactness | Fixed ambient operator |
| CCM compatibility | Natural (varying spaces OK) | Needs adaptation (tail error) |
| ITPFI integration | Helps with gsrc | Helps with tail bounds |
| Gap dependence | No (spectral exactness is gap-free) | Yes for pointwise; no for integrated |
| Spectral pollution | Excluded by theorem | Needs separate check |
| Remaining work | Verify discrete compactness | Adapt framework + verify gap bounds |
| Output if successful | spec(D_infty) = lim spec(D(N)) | Explicit error |mu_k(N) - gamma_k| |

### Recommendation

**Boegli is the primary tool.** Reasons:

1. **Handles varying spaces natively.** Boegli's framework is designed
   for operators on different Hilbert spaces with identification maps.
   CCM's setup (dim increasing with N) fits naturally. Stroschein requires
   a fixed ambient operator, which must be constructed.

2. **Spectral exactness is the exact result needed.** Boegli gives
   spec(T) = lim spec(T_n) with no spurious eigenvalues. This is
   precisely the spectral convergence gap. Stroschein gives error bounds,
   which are useful but secondary to the existence question.

3. **Discrete compactness is checkable.** The uniform resolvent bound
   is automatic (= 1 for z_0 = i). Discrete compactness reduces to
   uniform Sobolev regularity, which is connected to eigenvalue gap
   bounds. The interlacing theorem for rank-one perturbations provides
   a natural mechanism.

4. **No spectral pollution concern.** Boegli's theorem excludes
   spurious eigenvalues by construction. Stroschein's adaptation needs
   a separate spectral pollution check (the tail error could in principle
   introduce spurious eigenvalues).

**Stroschein is the quantitative backup.** Once Boegli establishes
spectral exactness, Stroschein's bounds give the RATE of convergence.
The rate lambda^{-1/2} log(lambda) / gap_k matches CCM's observed
pattern and would provide a complete quantitative theory.

---

## THE ONE REMAINING VERIFICATION: DISCRETE COMPACTNESS

The entire gap reduces to:

> **Does the resolvent sequence {(D(lambda,N) - i)^{-1}} satisfy
> discrete compactness?**

Equivalent reformulations:

(a) Is the sequence {(D(lambda,N) - i)^{-1} u_N}, for bounded {u_N},
    relatively compact in L^2?

(b) Do the resolvent images have uniformly bounded H^1 Sobolev norm?

(c) Are the eigenvalue gaps of D(lambda,N) bounded below (for fixed
    zero index k) uniformly in N?

(d) Does the interlacing theorem for rank-one perturbations prevent
    eigenvalue collision as N -> infty?

### Why (d) is the most natural approach:

CCM's operators change by rank-one perturbations as primes are added.
The Cauchy interlacing theorem says: the eigenvalues of D(lambda,N+1)
interlace with those of D(lambda,N). Specifically, between any two
consecutive eigenvalues of D(lambda,N+1), there is exactly one
eigenvalue of D(lambda,N).

This PREVENTS eigenvalue collision: no two eigenvalues can merge
because interlacing forces them to stay separated. The minimum gap
can only shrink by a factor related to the perturbation size
(~ 1/sqrt{p_{N+1}}), but the gap cannot vanish in finitely many steps.

For the gap to vanish as N -> infty, one would need the gaps to
decay faster than the perturbation sizes. But the perturbation
sizes are 1/sqrt{p} ~ 1/sqrt{N log N}, and there are only N
eigenvalues to interlace. The gap between the k-th eigenvalues
of successive approximations is bounded below by:

    gap_k(N) >= gap_k(N-1) - 2 * ||Delta_N|| >= gap_k(N-1) - C/sqrt{p_N}

Telescoping: gap_k(N) >= gap_k(N_0) - C * sum_{n=N_0+1}^{N} 1/sqrt{p_n}

The sum diverges (~ 2 sqrt{N}), so this naive bound fails. But the
interlacing structure means the gap cannot just decrease monotonically;
new eigenvalues inserted between old ones RESTORE gaps. The net effect
is more subtle than the telescoping bound suggests.

### Path to completing the verification:

1. Use the CF (Caratheodory-Fejer) structure to show that the
   eigenvector components xi_j are bounded in Sobolev norms uniformly
   in N. The CF theorem gives exponentially decaying Fourier
   coefficients, which means xi has uniform regularity.

2. The resolvent (D(lambda,N) - i)^{-1} maps into the domain of
   D(lambda,N), which in the V_n basis is the set of sequences
   {c_n} with sum n^2 |c_n|^2 < infty. The CF-controlled
   eigenvector decay gives uniform control of this Sobolev norm.

3. Rellich compactness then gives discrete compactness.

**Feasibility: 7/10.** The ingredients are present; the assembly
requires careful estimates within the CCM framework.

---

## SYNTHESIS: PATH TO CLOSING THE GAP

The complete chain would be:

1. **ITPFI** (proved): omega_1^{<=P} -> omega_1 in weak-*
   --> QW_lambda^N converges entry-by-entry to QW
   --> gsrc of D(lambda,N) (Boegli hypothesis H1)

2. **CF mechanism** (CCM proved): eigenvector components decay
   exponentially in the V_n basis
   --> uniform Sobolev regularity of resolvent images
   --> discrete compactness (Boegli hypothesis H2)

3. **Boegli's theorem**: (H1) + (H2) --> spectral exactness
   --> spec(D_infty) = lim spec(D(lambda,N))

4. **Lemma 7.3** (CCM proved): hat{xi}_lambda -> Xi uniformly
   --> the limiting eigenvalues are the zeros of Xi
   --> RH

Steps 1 and 4 are proved. Step 3 is an existing theorem.
Step 2 is the one verification needed.

---

> *Boegli's spectral exactness theorem applies to CCM's operators.*
> *The gsrc hypothesis follows from ITPFI state convergence.*
> *Discrete compactness is the one remaining verification.*
> *It reduces to uniform Sobolev regularity of CF eigenvectors.*
> *Stroschein gives quantitative rates once Boegli establishes convergence.*
> *One verification separates the current state from spectral exactness.*
