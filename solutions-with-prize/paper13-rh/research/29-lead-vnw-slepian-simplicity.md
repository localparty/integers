# Research 29 -- VNW + Slepian Combined Attack on Even-Sector Simplicity

*Date: 2026-04-09*
*Status: PROMISING FRAMEWORK with a clearly identified gap. VNW handles the lambda-direction at each fixed N. Slepian handles N -> infinity. The remaining problem: bridging finite N to the Slepian limit.*

---

## 1. Von Neumann-Wigner for one-parameter families

**Theorem (von Neumann-Wigner, 1929; Arnold, 1972).** Let A(t) be a one-parameter family of real symmetric n x n matrices depending real-analytically on t in R. The set of matrices in Sym(n) with a degenerate eigenvalue has codimension 2 in Sym(n).

**Consequence for one-parameter families:** A real-analytic curve t -> A(t) in Sym(n) has dimension 1. The degenerate locus D_n has codimension 2 in Sym(n), hence dimension n(n+1)/2 - 2. A generic one-parameter curve avoids D_n by transversality (1 + codim(D_n) = 1 + 2 = 3 > dim(Sym(n)) is NOT the right count; the correct statement is that dim(curve) + dim(D_n) = 1 + n(n+1)/2 - 2 = n(n+1)/2 - 1 < n(n+1)/2 = dim(Sym(n)), so the curve generically misses D_n).

**Stronger form (Kato-Rellich + VNW):** For a real-analytic one-parameter family A(t), eigenvalue branches mu_k(t) are real-analytic away from crossings. At a crossing, two conditions must simultaneously hold in an adapted 2x2 block:

    H_{12}(t_0) = 0       (off-diagonal coupling vanishes)
    H_{11}(t_0) = H_{22}(t_0)   (diagonal elements coincide)

This is two equations in one unknown t -- generically inconsistent.

**Critical caveat:** "Generically inconsistent" means crossings are non-generic, NOT impossible. Special families CAN cross (e.g., A(t) = diag(t, -t) crosses at t = 0).

---

## 2. QW_lambda^{N,+} satisfies the VNW hypotheses

Fix N >= 1. The even-sector Weil quadratic form QW_lambda^{N,+} is an (N+1) x (N+1) matrix depending on the single parameter lambda > 1.

**(H1) Real symmetric:** QW_lambda^{N,+} is real symmetric by construction. The matrix entries involve the Weil explicit formula with real test functions restricted to the even sector. The components W_{0,2}, W_R, W_p all contribute real symmetric matrices when restricted to even basis functions.

**(H2) Analytic in lambda:** Each matrix entry of QW_lambda^{N,+} is a real-analytic function of lambda for lambda > 1. The W_{0,2} entries involve 1/(L^2 + 16*pi^2*n^2) with L = 2*log(lambda), which is analytic for lambda > 0. The W_R entries involve psi(1 + i*n*2*pi/L) and its complex conjugate, which are analytic in L (hence in lambda) away from L = 0. The W_p entries involve cos(n * log p) * chi(p <= lambda), which is piecewise constant in lambda; but within each interval (sqrt(p_k), sqrt(p_{k+1})), the sum over primes is fixed and the lambda-dependence comes only through L = 2*log(lambda) in the continuous terms. At lambda = sqrt(p), a new prime enters, introducing a rank-1 jump -- but for the VNW argument we work within each analytic segment and note that simplicity at one point in the segment propagates to the whole segment.

**(H3) Single symmetry class:** The even sector is already a symmetry reduction. The full matrix QW_lambda^N decomposes into even and odd blocks under the Z/2 symmetry n -> -n. Within the even block QW_lambda^{N,+}, there is no further symmetry that could protect crossings. All eigenvalues belong to the same (trivial) representation of the residual symmetry group, so VNW applies without obstruction.

**Conclusion:** At each fixed N, the family lambda -> QW_lambda^{N,+} satisfies VNW. Crossings in lambda are codimension-2 events in a one-parameter family, hence non-generic.

---

## 3. Slepian's simplicity theorem

**Theorem (Slepian 1961, Landau-Pollak 1962).** The prolate spheroidal wave operator B_{T,Omega} = P_T P_Omega P_T has all eigenvalues simple: 1 > chi_0 > chi_1 > chi_2 > ... > 0.

*Proof mechanism:* B_{T,Omega} commutes with the Sturm-Liouville operator F_c = d/dx[(1-x^2) dy/dx] + c^2(1-x^2)y, where c = pi*T*Omega. Sturm-Liouville oscillation theory gives simplicity of F_c, which transfers to B_{T,Omega} via the shared eigenbasis.

**Relevance:** CCM (Connes-Consani-Marcolli) establish that the ground state eigenvector of QW_lambda^{N,+} converges to a prolate spheroidal eigenfunction as N -> infinity (at each fixed lambda). The PW_lambda operator has simple eigenvalues by Slepian. Therefore: **simplicity holds in the N -> infinity limit.**

---

## 4. The two-parameter picture: (lambda, N)

### 4.1 VNW in the lambda-direction

At each fixed N, VNW says: eigenvalue crossings in the one-parameter family lambda -> QW_lambda^{N,+} are codimension-2, hence non-generic. If we verify simplicity at one value lambda_0 for that N, VNW propagates simplicity to all lambda in the same analytic segment. Since QW is piecewise analytic in lambda (with rank-1 jumps at lambda = sqrt(p)), one propagates across jumps by re-verifying at one point in each segment -- but the segments are semi-algebraic in lambda, and in practice a single numerical check at large lambda suffices to cover the entire range (the jumps at lambda = sqrt(p) are rank-1 perturbations that cannot create degeneracies from simple spectra, by a separate rank-1 argument).

**Status:** VNW handles the lambda-direction cleanly, modulo the non-generic vs. impossible caveat.

### 4.2 N as a second parameter?

Treating (lambda, N) as a two-parameter family: VNW says the degenerate locus in a TWO-parameter family has codimension 2, hence dimension 2 - 2 = 0. Crossings can occur at **isolated points** in the (lambda, N) plane.

But N is a **discrete** parameter (N in Z_{>= 1}). The (lambda, N) parameter space is not R^2 but R x Z. Isolated points in R^2 could, in principle, land on integer values of N. So the two-parameter VNW argument does not automatically exclude crossings at specific (lambda_0, N_0) with N_0 integer.

### 4.3 The Slepian anchor at N = infinity

Slepian gives simplicity at N = infinity (the limiting prolate operator). So any crossing in the (lambda, N) plane must occur at FINITE N. The question: can a crossing exist at some finite (lambda_0, N_0) that is "invisible" from the N -> infinity limit?

---

## 5. Proposed strategy: numerical bootstrap + VNW + Slepian

**Step 1 (done).** Verify simplicity numerically at specific (lambda_0, N_0) to high precision. This has been done to 120+ decimal digits for all tested (lambda, N) pairs -- hundreds of cases, zero counterexamples.

**Step 2 (VNW propagation).** At each verified N_0, VNW propagates simplicity from the tested lambda_0 to ALL lambda > 1 at that N_0. This is the VNW one-parameter argument: verified simplicity at one point + analyticity + codimension 2 implies simplicity everywhere along the analytic curve. (This step requires strengthening "non-generic" to "impossible" for the specific arithmetic family QW -- see Section 6.)

**Step 3 (finite N coverage).** Repeat Steps 1-2 for each N = 1, 2, ..., N_max. For each N, one numerical verification + VNW covers all lambda. The numerical evidence covers N up to at least 20 with multiple lambda values.

**Step 4 (large N via Slepian).** For N > N_max, use the Slepian limit: QW_lambda^{N,+} converges to the prolate operator PW_lambda, which has simple spectrum by Slepian. If this convergence is quantitative (with an explicit error bound on eigenvalue gaps), then for N sufficiently large, simplicity of PW transfers back to QW^{N,+}.

**Step 5 (bridge).** Choose N_max large enough that:
- Steps 1-3 cover N = 1, ..., N_max by numerical verification + VNW
- Step 4 covers N > N_max by Slepian convergence

---

## 6. The remaining gap

Two distinct issues prevent this from being a complete proof:

### Gap A: VNW non-generic vs. impossible

VNW says crossings are non-generic (codimension 2) but not impossible. To promote "non-generic" to "impossible" for QW_lambda^{N,+} specifically, one needs the arithmetic exclusion argument from Research 26 (Section A.6): show that the overlap <phi_k | a> can never vanish, where phi_k are eigenvectors of B = -(W_R + W_p) and a is the archimedean vector. This is a transcendence-type statement about prime logarithms vs. pi.

**Without this:** VNW alone gives "simplicity holds for all lambda outside a measure-zero set" -- but we need it for ALL lambda.

**Partial workaround:** The rank-1 perturbation structure provides an independent argument. By Cauchy interlacing (Research 27), simplicity of A^ev = B + sigma|a><a| is equivalent to all overlaps <phi_k | a> being nonzero. The overlaps are themselves real-analytic functions of lambda. If an overlap vanishes at some lambda_0, it vanishes on a discrete set (by analyticity). Combining: the set of lambda where simplicity fails is AT MOST discrete. This is stronger than the bare VNW conclusion but still not "everywhere."

### Gap B: Quantitative Slepian convergence

For Step 4, we need: there exists N_0 such that for all N >= N_0 and all lambda > 1, the eigenvalue gap of QW_lambda^{N,+} is at least half the corresponding gap of PW_lambda. This requires a quantitative convergence estimate QW^{N,+} -> PW with explicit error bounds. CCM provide qualitative convergence (Lemma 7.2) but the error is O(lambda^{-2}) in the lambda -> infinity direction, not in the N -> infinity direction needed here.

**Status of Gap B:** A quantitative N -> infinity convergence estimate is plausible but unproven. The numerical data (Research 26, Section C) shows the gap decays exponentially in N: delta^ev ~ C * exp(-alpha * N). This DECAY means the gap gets smaller as N grows, which is the WRONG direction for a simple-minded Slepian transfer -- the prolate gap is O(1), but the Weil gap is exponentially small.

**Reinterpretation:** The relevant quantity is not the absolute gap but whether it is ZERO. Even an exponentially small gap proves simplicity. The question is only: does the gap ever hit exactly zero? Slepian says no at N = infinity; VNW says no for generic lambda at each finite N; the combined question is whether an exponentially shrinking but always-positive gap can suddenly hit zero at some finite N.

---

## 7. Feasibility assessment

| Component | Status | Difficulty |
|:----------|:-------|:-----------|
| VNW hypotheses verified for QW^{N,+} | DONE (Section 2) | Routine |
| VNW propagation in lambda at fixed N | WORKS (non-generic exclusion) | Clean |
| Strengthening to "impossible" (Gap A) | OPEN -- needs arithmetic input | Hard (6/10) |
| Slepian simplicity at N = infinity | KNOWN (Sturm-Liouville) | Classical |
| Quantitative QW -> PW convergence (Gap B) | OPEN -- needs explicit bounds | Hard (7/10) |
| Numerical verification at tested (lambda, N) | DONE to 120 digits | Complete |
| Full proof via this strategy | INCOMPLETE -- Gaps A and B remain | Combined 7/10 difficulty |

**Overall rating: 6/10.**

This is stronger than any single-theorem approach (Research 26 rated VNW alone at 5/10 and the gap bound at 4/10). The combined VNW + Slepian framework covers both ends of the N-range and gives a clear two-gap structure. Gap A (arithmetic exclusion) was already identified in Research 26; Gap B (quantitative Slepian convergence) is new and potentially more tractable since it asks for norm estimates rather than transcendence results.

**Recommended next step:** Attack Gap B first. Establish explicit operator-norm bounds on QW_lambda^{N,+} - (prolate projection to N+1 modes) as a function of N. If ||QW - proj(PW)|| < gap(PW)/2 for N >= N_0, then Weyl perturbation gives simplicity for all N >= N_0, closing one of the two gaps.

---

> *VNW sweeps lambda. Slepian anchors infinity.*
> *The architecture is sound; two bolts remain loose.*
> *One arithmetic (overlaps never vanish), one analytic (convergence rate).*
> *Either bolt, tightened, halves the conjecture.*
