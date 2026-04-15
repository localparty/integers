# 14 -- CCM Zeta Spectral Triples + ITPFI: Synthesis Investigation

*Date: 2026-04-09*
*Status: INVESTIGATED -- PROMISING BUT WITH STRUCTURAL OBSTACLES*
*Depends on: research/265 (ITPFI factorization), research/13 (L.5 on H_1),
strategy/10 (18 kills), Connes-Consani-Moscovici arXiv:2511.22755 (Nov 2025)*

---

## 0. The lead

Connes-Consani-Moscovici (CCM, 2025) construct self-adjoint operators
D(lambda,N) on L^2([lambda^{-1}, lambda]) whose spectra approximate the
Riemann zeros gamma_n. The construction uses Euler products truncated to
N primes -- the SAME prime-truncation structure as our ITPFI
factorization omega_1 = bigotimes_p omega_1^p.

**Central question:** Does ITPFI control the convergence D(lambda,N) ->
D_inf as N -> inf, closing CCM's open gap?

---

## 1. The CCM construction (arXiv:2511.22755)

### 1.1 What they build

- **Hilbert space:** L^2([lambda^{-1}, lambda]) (NOT H_1, NOT H_R)
- **Operators:** D(lambda,N) built from rank-one perturbations of a
  scaling spectral triple
- **Euler truncation:** Only primes p <= lambda^2 contribute; N controls
  how many primes are active
- **Self-adjointness:** Guaranteed at each finite stage by the
  Caratheodory-Fejer theorem for Toeplitz matrices
- **Numerical precision:** spec(D(lambda,N)) matches gamma_n to 10^{-55}
  for the first zero using only primes <= 13

### 1.2 What they prove

- Each D(lambda,N) is self-adjoint (CF theorem)
- The spectra numerically match gamma_1 through gamma_50 using 6 primes
- The precision degrades from 10^{-55} (gamma_1) to 10^{-3} (gamma_50)

### 1.3 What they leave open

- **(a)** spec(D(lambda,N)) -> {gamma_n} as lambda, N -> inf
- **(b)** The limiting operator D_inf is self-adjoint
- **(c)** The convergence is in a spectral-preserving topology

---

## 2. The ITPFI connection: structural alignment

### 2.1 Shared prime-truncation structure

| Aspect | ITPFI (our work) | CCM |
|:--|:--|:--|
| Truncation parameter | P (primes p <= P) | N (first N primes) |
| What truncates | omega_1 state | Euler product in D(lambda,N) |
| Infinite limit | omega_1 = bigotimes_p omega_1^p | D_inf = lim D(lambda,N) |
| Convergence proved | YES (research/265) | OPEN |
| Space | H_1 = GNS(omega_1) | L^2([lambda^{-1}, lambda]) |

The structural alignment is genuine: both constructions add primes
one at a time and need the infinite product to converge.

### 2.2 The critical difference: what converges

- **ITPFI:** The STATE omega_1 converges as a product state. This is
  proved because the KMS_1 state is unique (BC Theorem 25) and the
  product of local KMS states is KMS (Bratteli-Robinson 5.3.23).

- **CCM:** The OPERATOR D(lambda,N) changes with N. Adding a prime
  changes the rank-one perturbation, which changes the operator itself.
  State convergence does NOT automatically imply operator convergence.

### 2.3 The gap between state and operator convergence

**This is the key structural obstacle.** ITPFI gives:

    omega_1^{<=P} := bigotimes_{p<=P} omega_1^p  ->  omega_1

in weak-* topology. But D(lambda,N) is not a functional of omega_1^{<=P}
alone. It is constructed from the Euler product of zeta, not from the
KMS state. The Euler product and the product state share the same
prime factorization, but they encode DIFFERENT information:

- omega_1^p encodes the p-adic weights: omega_1^p(mu_p^k mu_p^{*k}) = 1/p^k
- The CCM Euler factor at p encodes the spectral contribution of p to
  the zeros: (1 - p^{-s})^{-1}

These are related (both involve p^{-s}) but not identical. The state
lives on A_BC; the Euler factor lives on the zeta function.

---

## 3. Does ITPFI help with CCM's convergence? Analysis

### 3.1 Scenario A: Direct operator convergence via ITPFI (UNLIKELY)

For ITPFI to directly control D(lambda,N), we would need:

    D(lambda,N) = F(omega_1^{<=P})

for some continuous functional F. Then omega_1^{<=P} -> omega_1 would
give D(lambda,N) -> D_inf = F(omega_1).

**Problem:** CCM's D(lambda,N) is NOT a functional of omega_1. It is
built from a DIFFERENT use of the prime factorization (the Euler product
of zeta as a function of s, not the partition function of the BC system).
The connection between these two objects IS the explicit formula -- but
the explicit formula is not a continuous map in operator norm.

**Verdict: DOES NOT WORK as stated.**

### 3.2 Scenario B: ITPFI provides norm control for resolvent convergence (PLAUSIBLE)

Strong resolvent convergence of D(lambda,N) requires:

    ||(D(lambda,N) - z)^{-1} phi - (D_inf - z)^{-1} phi|| -> 0

for all phi and z not in the spectrum. This can be established if:

(i) The perturbation from adding prime p_{N+1} is bounded:
    ||D(lambda,N+1) - D(lambda,N)|| <= C/p_{N+1}

(ii) The sum sum_{N} ||D(lambda,N+1) - D(lambda,N)|| converges
    (or the squared sum converges, for Hilbert-Schmidt perturbations)

From research/11 sec. 6: the perturbation from adding prime p to the
BC system satisfies |1 - Z_p(t)| ~ 1/p. If CCM's perturbation has
similar 1/p behavior, then:

- sum 1/p diverges (Mertens) -- rank-one perturbation theory needs care
- sum 1/p^2 converges -- Hilbert-Schmidt perturbations would converge
- The CCM rank-one perturbation structure might give ||delta D_N|| ~ 1/p^2
  (because rank-one perturbations in L^2 have squared-norm scaling)

**The ITPFI product convergence (sum |1-Z_p|^2 < inf) could provide
exactly the right estimates.** The key question: do CCM's rank-one
perturbations have Hilbert-Schmidt norms that track our |1 - Z_p|?

**Verdict: PLAUSIBLE but requires detailed calculation within the
CCM framework.**

### 3.3 Scenario C: Caratheodory-Fejer + ITPFI (INTERESTING)

CCM use the CF theorem for Toeplitz matrices to establish
self-adjointness at finite N. The Toeplitz structure comes from
convolution on the multiplicative group.

The ITPFI factorization IS the infinite multiplicative convolution:
omega_1 = bigotimes_p omega_1^p is the product measure on N^x,
which is multiplicative convolution of the p-local measures.

**If the CF theorem at finite N uses the truncated product measure
omega_1^{<=P} as input, then ITPFI convergence (omega_1^{<=P} -> omega_1)
would provide CF inputs for all N, and the limiting Toeplitz matrix
would inherit self-adjointness.**

**Verdict: REQUIRES checking whether CCM's CF application uses the
product state or something else. If it does, this is the strongest
connection.**

### 3.4 Scenario D: Spectral convergence theorem (THE RIGHT FRAMEWORK)

**Theorem (Kato-Rellich for self-adjoint perturbations):** If A_N
are self-adjoint, A_N -> A in strong resolvent sense, and A is
self-adjoint, then spec(A) subset lim inf spec(A_N).

**Theorem (spectral mapping + numerical convergence):** If additionally
spec(A_N) converges numerically (i.e., for each n, lambda_n(A_N) -> mu_n),
then spec(A) = {mu_n}.

CCM have: each A_N = D(lambda,N) is self-adjoint, and spec(A_N) converges
numerically to {gamma_n} with extraordinary precision.

What's missing: A_N -> A in strong resolvent sense. This IS the
convergence gap.

**Can ITPFI provide strong resolvent convergence?** Not directly (wrong
space), but the ITPFI estimates on perturbation sizes (|1 - Z_p| ~ 1/p)
suggest the CCM perturbations have similar scaling. If so, the resolvent
convergence follows from Kato's perturbation theory applied to
rank-one perturbations with decaying norms.

**Verdict: THE MOST PROMISING PATH. Requires proving ||D(N+1) - D(N)||
decays and combining with existing spectral mapping theorems.**

---

## 4. Does this avoid the H_1 vs H_R wall?

### 4.1 The wall (from kills 9, 11, 13, 17, 18)

H_1 has spectrum {log n}. H_R has spectrum {gamma_n}.
No bridge exists without assuming the answer.
ITPFI factors H_1 but H_R has no prime factorization.

### 4.2 CCM's bypass

CCM work on L^2([lambda^{-1}, lambda]) -- NEITHER H_1 NOR H_R.
Their operators are CONSTRUCTED to have spectra at {gamma_n}.
The construction does not pass through the BC GNS representation.

**The H_1 vs H_R wall does not directly apply.** CCM's space is a
third space, purpose-built for the zeros. The wall says: you cannot
get from H_1 to H_R. CCM never try to. They start fresh.

### 4.3 But a NEW wall appears

CCM bypass our wall, but face their own: proving convergence.
The convergence gap for D(lambda,N) -> D_inf is THEIR version of
the H_1 vs H_R problem. At finite N, they have approximations.
At N = inf, they need the exact zeros. The gap between finite
approximation and infinite limit is the SAME fundamental difficulty,
just in a different guise.

### 4.4 Does ITPFI help with the new wall?

**Partially.** ITPFI controls the infinite product of LOCAL factors.
CCM's construction also uses an infinite product of local factors.
The structural parallel is real. But ITPFI works on H_1 (where the
product state converges), not on L^2([lambda^{-1}, lambda]).

To make ITPFI useful for CCM, we need a MAP between:
- The state space: omega_1^{<=P} on H_1
- The operator space: D(lambda,N) on L^2([lambda^{-1}, lambda])

This map would be a form of the explicit formula, made operator-valued.
This is essentially Connes' original programme -- and it remains open.

---

## 5. Premise check: does this avoid all 18 kills?

| Kill | Mechanism | Avoided? | Why |
|:--|:--|:--|:--|
| 1-2 | Topology | YES | Not topological |
| 3, 5 | Index theory | YES | No index computation |
| 4 | Geometry | YES | No Lorentzian argument |
| 6 | Li positivity | YES | Not positivity-based |
| 7 | Spectral flow | YES | Self-adjointness built in |
| 8 | KMS uniqueness | YES | Not claiming compactness from KMS |
| 9 | H_1 spectrum | YES | Not on H_1 |
| 10 | Predictions | YES | Not using matrix elements |
| 11 | Algebraic measure | YES | Not on H_1 |
| 12 | RAGE | YES | Different operator |
| 13 | ITPFI atomicity | YES | Not claiming {log n} = {gamma_n} |
| 14 | Meyer completeness | YES | Not circular |
| 15 | Nuclear rigging | YES | Not distributional |
| 16 | Hamburger | YES | Not moment-based |
| 17 | Gradient flow H_1 | YES | Not on H_1 |
| 18 | Combined L.5 | YES | Not on H_1 |

**All 18 kills avoided.** The approach operates on a different space
with a different construction. The only question is convergence.

---

## 6. What would the proof look like?

### 6.1 The theorem (hypothetical)

**Theorem (RH via CCM + ITPFI).** Let D(lambda,N) be the CCM zeta
spectral triples (arXiv:2511.22755). Let omega_1 = bigotimes_p omega_1^p
be the ITPFI factorization of the BC KMS_1 state. Then:

(a) The rank-one perturbations ||D(lambda,N+1) - D(lambda,N)||
    satisfy ||delta D_N|| <= C/p_{N+1}^alpha for some alpha > 1/2.

(b) By Kato's perturbation theory, D(lambda,N) converges in strong
    resolvent sense to a self-adjoint operator D_inf.

(c) The spectral convergence theorem (strong resolvent + numerical
    convergence) gives spec(D_inf) = {gamma_n} subset R.

(d) Therefore all non-trivial zeros of zeta lie on Re(s) = 1/2.

### 6.2 What needs to be proved

- **(a)** is the key technical step. It requires analyzing CCM's
  rank-one perturbation structure and bounding the norms. The ITPFI
  estimate |1 - Z_p| ~ 1/p suggests this should be true with
  alpha = 1, but the relationship between Z_p and the CCM perturbation
  norm is not established.

- **(b)** follows from (a) by standard Kato theory if alpha > 1/2.

- **(c)** requires the spectral mapping theorem + strong resolvent
  convergence. Standard if (b) holds.

- **(d)** is definitional: spec(D_inf) subset R means all zeros are
  on the critical line.

### 6.3 The hard step

Step (a) is the entire proof. Everything else is standard. And step (a)
requires understanding CCM's construction in enough detail to bound
the perturbation norms -- which requires reading and digesting the
full CCM paper (not just the abstract).

---

## 7. Honest assessment

### 7.1 What is genuinely promising

1. **CCM avoids all 18 kills.** This is not a minor point. Every previous
   approach hit at least one kill. CCM's construction is on a fresh
   space with operators that HAVE the right spectra by construction.

2. **The Euler product truncation is shared.** ITPFI and CCM both add
   primes one at a time. The structural parallel is not superficial.

3. **The numerical evidence is extraordinary.** 10^{-55} precision with
   6 primes suggests the convergence rate is exponential in N (or
   faster). If the rate can be proved to be exponential, the sum in
   step (a) converges trivially.

4. **The spectral convergence theorem is ready.** Strong resolvent
   convergence + numerical convergence is a KNOWN sufficient condition
   for spectral convergence. The theorem exists; we just need to verify
   its hypotheses.

### 7.2 What remains difficult

1. **The map between ITPFI and CCM is missing.** omega_1^{<=P} lives on
   H_1; D(lambda,N) lives on L^2([lambda^{-1}, lambda]). These are
   different spaces. The prime truncation is structurally similar but
   not formally the same object.

2. **CCM's convergence gap IS the hard part.** They left it open
   because it IS hard. Our ITPFI does not trivially close it.

3. **We have not read the full CCM paper.** The analysis above is based
   on the abstract/summary. The actual rank-one perturbation structure
   might reveal additional obstacles.

4. **A new wall replaces the old wall.** We avoid H_1 vs H_R, but face
   "D(lambda,N) convergence" instead. This might be easier (CCM already
   have numerical convergence), or it might be equally hard (proving
   RIGOROUS convergence of spectral approximations is a notoriously
   difficult problem).

### 7.3 Feasibility rating

**6/10 for ITPFI directly closing CCM's gap.**
The structural parallel is real but the formal connection is missing.
ITPFI controls state convergence on H_1; CCM need operator convergence
on L^2([lambda^{-1}, lambda]). These are different problems.

**8/10 for CCM as a path to RH (independent of ITPFI).**
The construction avoids all known obstacles. The convergence gap is
their only open problem. The numerical evidence strongly suggests
convergence. This is probably the strongest current approach to RH.

**7/10 for ITPFI providing USEFUL ESTIMATES for CCM's convergence.**
Even if ITPFI doesn't directly close the gap, the estimates from
research/11 (perturbation sizes ~1/p, squared sums converging, polymer
decay) might transfer to CCM's setting by analogy, suggesting the right
bounds to prove.

---

## 8. Recommended next steps

1. **Obtain and study arXiv:2511.22755 in full.** The detailed
   construction of D(lambda,N) -- especially the rank-one perturbation
   structure -- is essential for assessing whether ITPFI estimates
   apply.

2. **Identify the map (if any) between omega_1^p and CCM's p-local
   Euler factor.** If D(lambda,N) can be expressed as a functional of
   the truncated product state, ITPFI applies directly.

3. **Bound ||D(lambda,N+1) - D(lambda,N)|| as a function of p_{N+1}.**
   This is the key technical calculation. If it scales as 1/p^alpha
   with alpha > 1/2, the convergence follows.

4. **Check whether the CF theorem at finite N uses the product measure
   omega_1^{<=P} as input.** If so, the ITPFI -> CF -> self-adjointness
   chain might extend to N = inf.

5. **Investigate the lambda -> inf limit independently of the N -> inf
   limit.** CCM have TWO parameters (lambda and N). The interplay between
   them might be crucial.

---

## 9. Comparison with remaining angles from strategy/10

| Angle | Strategy 10 description | CCM connection |
|:--|:--|:--|
| A. Explicit formula | Connes' approach | CCM may implement this |
| B. Sonin space | Connes-Consani-Moscovici 2024 | Precursor to CCM 2025 |
| C. Scattering | Yakaboylu | Different approach |
| D. Zeta spectral triple | Connes-Consani 2025 | THIS IS IT |
| E. New Hilbert space | H_new with both properties | CCM's L^2 IS H_new |

CCM's construction IS angle D from strategy/10. Their L^2([lambda^{-1}, lambda])
IS the "third space" hypothesized in angle E: it has Euler product structure
(so ITPFI-like technology might apply) AND has spectra at {gamma_n}
(so the right spectrum). It is neither H_1 nor H_R.

**The most promising of all remaining angles after 18 kills.**

---

*CCM bypass the H_1 vs H_R wall by building a third space.*
*Their operators have the right spectra by construction.*
*The convergence gap is the only obstacle.*
*ITPFI provides structural motivation but not a direct proof.*
*The numerical evidence (10^{-55}) screams that convergence holds.*
*This is the lead to pursue.*
