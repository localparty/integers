# Research 55 -- N3: Inverse Littlewood-Offord for the Eigenvalue Gap

*Date: 2026-04-09. Structure: DEVELOPMENT (A) then ADVERSARIAL (B).*
*Depends on: ledger (Step 10 wall), research/54 (N2 pseudo-random gaps), research/48 (fatal gap at Step 10)*

---

## PART A: Development

### 1. The inverse Littlewood-Offord theorem (Tao-Vu 2009)

Let v_1, ..., v_n be real numbers and xi_1, ..., xi_n be iid Rademacher (+/-1) random variables. If there exists a ball B of radius 1 such that P(v_1 xi_1 + ... + v_n xi_n in B) >= n^{-C}, then at least n - n^{1-eps} of the v_i are contained in a *generalized arithmetic progression* (GAP) of rank r <= C' and volume at most n^{C'}, where C', eps depend only on C. A GAP of rank r is a set {a_0 + k_1 g_1 + ... + k_r g_r : 0 <= k_j <= N_j} with generators g_1,...,g_r and dimensions N_1,...,N_r. The volume is prod N_j. The contrapositive: if the v_i CANNOT be captured by any bounded-rank, bounded-volume GAP, then the sum v_1 xi_1 + ... + v_n xi_n has strong anti-concentration: P(sum in B) <= n^{-C} for any unit ball B. Anti-concentration of linear forms in eigenvector components directly controls eigenvalue repulsion in the random matrix literature (Tao-Vu, Annals 2009; Nguyen-Vu, Ann. Prob. 2017).

### 2. Application to QW^N eigenvectors

For the k-th eigenvector phi_k of the even-sector matrix QW^N (Fourier truncation at level N), the components are phi_k[i] for i = 0,...,N. These are determined by the Galerkin matrix, whose entries involve cos(2*pi*n*log(p)/L) for primes p <= lambda^2. The eigenvector components inherit the arithmetic structure of the primes through the spectral decomposition. If phi_k[i] were to cluster in a GAP of rank r and volume V, then by inverse L-O, a random linear combination sum phi_k[i] xi_i would concentrate in a ball -- equivalently, the eigenvalue lambda_k would be poorly separated from its neighbors. If the components DON'T cluster, the eigenvalue gap is polynomial: |lambda_k - lambda_{k+1}| >= n^{-C}.

### 3. Why the components should not cluster

The matrix entries of QW^N involve cos(x_i * log p_j) where x_i are the Fourier modes and p_j are primes. The eigenvalues of such structured matrices are determined by transcendental quantities. The set {cos(2*pi*n*log 2 / L), cos(2*pi*n*log 3 / L), ...} involves logarithms of primes, which are Q-linearly independent (by the fundamental theorem of arithmetic). These values are equidistributed by Weyl's theorem and cannot be captured by a GAP of bounded rank because a GAP has rational algebraic structure while log-prime values are transcendental and multiplicatively independent.

### 4. What is actually needed

The formal requirement: for each eigenvector phi_k of QW^N, show that the component vector (phi_k[0], ..., phi_k[N]) does not lie in a GAP of rank r <= C and volume <= N^C for any absolute constant C. This is a statement about the EIGENVECTORS, not just the matrix entries. The matrix entries have explicit transcendental structure, but eigenvectors are implicit nonlinear functions of those entries. Controlling eigenvector components requires more than controlling matrix entries.

### 5. Numerical evidence (r55_inverse_lo_gap_test.py)

Tested at lambda = sqrt(14), N_fourier in {4, 8, 12, 16}. Rank-1 GAP capture of eigenvector components ranges from 41% to 100%. The middle eigenvectors (k ~ N/2) show the least GAP capture (41-55%), while ground-state and top eigenvectors show more (60-82%). This is consistent with anti-structure for bulk eigenvectors but not universal. The eigenvalue gaps decay catastrophically: min gap ~ 10^{-1.5*N}, confirming the Step 10 wall is real numerically. Even at N=16, gaps are at 10^{-30}.

---

## PART B: Adversarial

### 6. Attack: inverse L-O requires randomness, not determinism

The inverse Littlewood-Offord theorem is a statement about RANDOM variables xi_i. The conclusion "P(sum in B) <= n^{-C}" is a probability over the random choice of signs xi_i. For the eigenvector problem, there is no randomness: the eigenvector components are completely determined by the matrix QW^N. There is no probability space. The "anti-concentration" of a deterministic vector is not defined in the L-O framework. One cannot assert "phi_k has anti-concentration" because phi_k is a fixed vector. The L-O machinery applies to the random variable sum v_i xi_i where v_i = phi_k[i], telling us about random PROJECTIONS of phi_k. But eigenvalue gaps depend on the specific inner product <phi_k, delta_perturbation>, not a random projection. The theorem says "if the components avoid GAPs, random projections anti-concentrate" -- it does NOT say "eigenvalue gaps are large."

**Severity: FATAL for direct application.** The theorem answers a different question than the one Step 10 requires.

### 7. Attack: transcendentality does not prevent GAP membership

A GAP is a set {a_0 + k_1 g_1 + ... + k_r g_r : 0 <= k_j <= N_j}. The generators g_j can be ANY real numbers, including transcendental ones. Example: {pi + k*sqrt(2) : k = 0,...,100} is a rank-1 GAP containing transcendental elements. The set {cos(n*log 2) : n = 0,...,N} for N = 20 has all entries transcendental, but they CAN be approximately captured by a GAP if the cosine values happen to cluster near an arithmetic progression. The Q-linear independence of {log p} controls the MATRIX ENTRIES, not the EIGENVECTOR COMPONENTS. Eigenvector components are nonlinear functions (solutions of the eigenvalue equation) of transcendental quantities -- being nonlinear images of transcendentals says nothing about GAP avoidance. A simple counterexample: let M be a matrix with transcendental entries but with eigenvector (1/sqrt(n), ..., 1/sqrt(n)) -- this flat vector lies in a rank-1 GAP of volume 1 despite the matrix having transcendental entries.

**Severity: HIGH.** The argument "transcendental inputs imply non-GAP outputs" is a non sequitur.

### 8. Can inverse L-O be adapted to deterministic sequences?

There is no published "deterministic inverse Littlewood-Offord" theorem. The closest results: (a) Tao-Vu's work on Waring's problem uses additive combinatorics for deterministic sets, but targets a different conclusion (representation counts, not anti-concentration). (b) The Balog-Szemeredi-Gowers lemma gives structural control over sets with large additive energy, which is related but requires the set to have large self-sumset -- not directly applicable to eigenvector components. (c) Bourgain's discretized sum-product estimates give anti-concentration for convolutions of deterministic measures under Diophantine conditions, but apply to measures, not individual vectors. No existing tool bridges from "eigenvector components of a matrix with arithmetic structure" to "eigenvalue gaps are polynomial."

**Severity: HIGH.** Adapting L-O to the deterministic setting would be a new theorem in additive combinatorics, not an application of known results.

---

## VERDICT

**Feasibility: 3/10.** The inverse Littlewood-Offord direction is a creative reframing of the Step 10 wall, but the central mechanism fails on inspection. The theorem requires randomness (Attack 6, FATAL); transcendentality of matrix entries does not propagate to eigenvector anti-structure (Attack 7, HIGH); and no deterministic analogue exists (Attack 8, HIGH).

The numerical test confirms the problem is real: eigenvector components show 41-100% rank-1 GAP capture (not the clean "anti-structure" the argument needs), and eigenvalue gaps decay as 10^{-1.5N} (the Step 10 wall in raw numbers).

**Confidence: 3/10** that this direction can close Step 10.

- 8/10 that the inverse L-O theorem is correctly stated and the GAP framework is relevant conceptual vocabulary.
- 2/10 that the randomness barrier (Attack 6) can be overcome with existing tools.
- 1/10 that "transcendental components avoid GAPs" is formally provable (Attack 7).

**What would change the assessment:** A deterministic anti-concentration theorem: "if the coefficients v_i satisfy a quantitative Diophantine condition (e.g., no n^{-C} of them lie in a GAP of rank r <= C), then the eigenvalue gaps of a matrix with those entries as eigenvector components are polynomial." No such theorem exists. Building one would require merging additive combinatorics with spectral perturbation theory in a way that has not been done.

**Recommendation:** Log as N3 at 3/10. Lower than N2 (4/10) because this note identifies a specific FATAL obstacle (Attack 6: no probability space) that N2's pseudo-random direction does not share -- N2 at least proposes a mechanism (equidistribution as proxy for randomness) even if the bridge is missing. N3 proposes applying a theorem whose hypotheses are categorically unmet.
