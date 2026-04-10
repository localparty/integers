# Lead 3: Rigorous perturbation bound ‖D(λ,N+1) − D(λ,N)‖ from ITPFI

## Direction (written by Strategist, Cycle 1)
Status: OPEN
Pattern: SP2 (transpose the R-theorem family into operator bounds) + Pattern 5 (zeta regularization of the rank-one perturbation)
Feasibility: 7/10
Rationale: Strategy/11 §3 step 3 identified ‖D(λ,N+1) − D(λ,N)‖ ~ 1/p_{N+1}^α with α > 1/2 as the key computation. Strategy 1 (this cycle) reframes it as a SECOND independent convergence control behind lead 2's Teschl transfer, but the bound is still the cleanest number to extract for a paper. Quick feasibility check (mpmath, done during strategy writing): from CCM's published data, the empirical exponent α ranges from ≈2.69 (worst, high zeros) to ≈49.4 (best, low zeros), both vastly above 1/2. That is a strong signal the bound exists; this lead makes it formal.
Toolkit connection: R265 (ITPFI, ω₁ = ⊗_p ω₁^p) — the state-level prime factorization whose norm bounds at each p give the required exponent. R28 (archimedean estimate O(1/λ)) for the archimedean contribution to the rank-one perturbation. code/ccm_perturbation_bound.py (if present in code/) or new mpmath script.
Investigate:
1. Read CCM 2025 (sources/ccm-zeta-spectral-triples-2025.pdf) §3 in detail and write down EXPLICITLY: D(λ,N+1) − D(λ,N) = α_{p_{N+1}} · |v⟩⟨w| with α_p, v, w as explicit functions of the Euler factor E_p(s).
2. Compute ‖D(λ,N+1) − D(λ,N)‖ as a rank-one operator norm: |α_p| · ‖v‖ · ‖w‖. Bound each factor using R265's p-local KMS data and the archimedean R28 bound.
3. Show Σ_N ‖D(λ,N+1) − D(λ,N)‖ < ∞ as a series indexed by primes. (If lead 1 gives finite-stage criticality and this series converges, the limit exists in operator norm — the strongest possible convergence.)
4. Run an mpmath script that numerically verifies the bound against CCM's actual operators for N=1,..,6 (the primes p ≤ 13) and one higher N if feasible. PASTE THE OUTPUT in the research section. "Would compute" is not acceptable.
5. Check: is the bound uniform in λ, or does it degrade as λ → ∞? If it degrades, what is the dependence? (This affects whether lead 2's limit can be taken before or after λ → ∞.)
Would close if: a rigorous bound Σ_N ‖D(λ,N+1) − D(λ,N)‖ ≤ C(λ) < ∞ with C locally bounded in λ, together with numerical corroboration on N ≤ 10.
Would kill if: the bound provably diverges (α ≤ 1/2 asymptotically), OR the bound only holds for a subsequence of primes, OR it depends on λ in a way that forbids the joint limit.
Source: strategy/11 §3, CCM 2025 (arXiv:2511.22755), research/265 (ITPFI three proofs), research/28 (R28 archimedean estimate).
Premise check: The relevant invariant is ‖D(λ,N+1) − D(λ,N)‖ as a real number, which DOES shift continuously under the addition of each prime (each rank-one perturbation has a nontrivial norm, and norms add continuously). So the constraint Σ < ∞ is non-vacuous: it is a real inequality whose LHS depends continuously on the primes included. Kill #1 (coboundary) does NOT apply because norms are not topological invariants. The cognate warning is kill #6 (Weil positivity subtlety): a positivity-from-above bound must not be swapped with a positivity-from-below bound. Here we want ‖·‖ small, not some bilinear form positive — cleaner, and not entangled with kill #6.

---

## Research (appended by Executor, Cycle 1)
[placeholder — executor fills in]

---

## Adversarial (appended by Adversary, Cycle 1)
[placeholder — adversary fills in]
