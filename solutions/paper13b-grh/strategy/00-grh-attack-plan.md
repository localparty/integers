# GRH Attack Plan

*Strategy for Paper 13b: The Generalized Riemann Hypothesis*
*Date: 2026-04-13*

---

## 1. Why GRH is the most tractable extension

GRH is not a new problem. It is the SAME problem with different input.

The Paper 13 RH proof chain has 6 layers (CCM operators, ITPFI, four
estimates, Boegli, Hurwitz, conclusion). Every layer operates on a
specific mathematical object (the BC algebra, the KMS_1 state, the
CCM operators D_N, the spectral data). GRH asks: does the same chain
work when we replace the Riemann zeta function with a Dirichlet
L-function L(s,chi)?

The answer is almost certainly yes, because:

- **The BC algebra already knows about characters.** The Galois action
  on Q^{cyc}/Q factors through (Z/qZ)^* for each modulus q. Dirichlet
  characters chi mod q are precisely the irreducible representations of
  this Galois group. The BC system was DESIGNED to encode this structure
  (Bost-Connes 1995, Theorem 25).

- **The CCM operator construction is analytic, not arithmetic.** The
  operators D_N are built from prolate spheroidal wave functions and
  Caratheodory-Fejer theory. The arithmetic input (which L-function)
  enters through the spectral data, not through the operator framework.
  Changing from zeta to L(s,chi) changes the eigenvalues but not the
  construction method.

- **The convergence machinery is general.** Boegli spectral exactness
  and Hurwitz zero convergence are theorems about operators and
  holomorphic functions, respectively. They do not care which L-function
  is being studied.

- **The estimates are the only place where work is needed.** The four
  estimates (archimedean, eigenvector approximation, H^1 regularity,
  CF decay) use specific properties of the zeta function's spectral
  data. For L(s,chi), these properties change in controlled ways
  determined by the conductor q(chi) and the character values chi(p).

**Comparison with other extensions:**

| Extension | What changes | Difficulty vs RH |
|:----------|:------------|:-----------------|
| GRH (Dirichlet) | Arithmetic input (zeta -> L(s,chi)) | +1 layer (character twist) |
| Dedekind zeta | Number field structure | +2 layers (field extension + ideal theory) |
| Automorphic L-functions | Full Langlands machinery | +4 layers minimum |
| Grand RH | Everything | Open-ended |

GRH is the minimal extension. It is the natural first target after RH.

---

## 2. Character modulation: which bridges produce which characters

The bridge family (Paper 24) provides 4 natural bridge indices
k in {2,3,4,6}, each corresponding to a crystallographic constraint on
the ~~5D geometry~~ 4+1 coordinate structure <!-- legacy 2026-04-15: "5D geometry" → "4+1 coordinate structure" per north-star.md §0.10 Vocabulary Canon, Intervention 8 (Agent B) -->. Each k produces Dirichlet characters of specific orders:

### k = 2: Quadratic characters

Characters chi with chi^2 = chi_0 (trivial). These correspond to:
- Real quadratic fields Q(sqrt(d))
- The Kronecker symbol (d/n)
- Class number formulas: h(d) = -1/d sum_{n=1}^{|d|} (d/n) n (negative d)

**Physical anchor:** The Z_2 orbifold is the simplest compactification.
GRH for quadratic characters ensures that the distribution of primes
in arithmetic progressions mod 4 (and more generally mod q for q with
only quadratic characters) is well-behaved.

**Test case:** chi = (-4/.) (the non-principal character mod 4).
L(s,chi) = beta(s) (Dirichlet beta function). GRH for this single
character is already a substantial result.

### k = 3: Cubic characters

Characters chi with chi^3 = chi_0. These correspond to:
- Cubic residue symbols in Z[omega], omega = e^{2pi i/3}
- Cubic reciprocity (Eisenstein integers)

**Physical anchor:** The 3-generation structure. The orbifold Euler
characteristic chi(M_5) encodes three fermion generations. GRH for cubic
characters constrains the arithmetic distribution of cubic residues,
which in turn constrains the generation-counting topological invariant.

**Test case:** The cubic character mod 7 (smallest conductor for a
primitive cubic character). This would be the first non-quadratic GRH
verification.

### k = 4: Quartic characters

Characters chi with chi^4 = chi_0. These correspond to:
- Quartic residue symbols in Z[i]
- Quartic reciprocity (Gaussian integers)

**Physical anchor:** The Pati-Salam coupling. The SU(4) x SU(2)_L x
SU(2)_R gauge group requires quartic symmetry in the compactification.
GRH for quartic characters constrains the arithmetic of Gaussian primes,
which feeds into the Pati-Salam breaking pattern.

**Test case:** The quartic character mod 5 (smallest conductor for a
primitive quartic character).

### k = 6: Sextic characters

Characters chi with chi^6 = chi_0. These correspond to:
- Sextic residue symbols in Z[omega]
- The E_8 lattice connection via modular forms of level 6

**Physical anchor:** Full bridge family closure. The k = 6 bridge is the
most constrained and connects to the E_8 x E_8 heterotic string. GRH at
k = 6 ensures arithmetic consistency of the full lattice structure.

**Test case:** The sextic character mod 7 (factors through cubic and
quadratic characters mod 7).

### Pilot order

The natural verification order is: k=2, k=3, k=4, k=6. This follows
increasing difficulty. k=2 (quadratic) has the most existing literature
and is the easiest test. k=6 (sextic) is the most constrained but also
the richest, since it subsumes k=2 and k=3.

---

## 3. PCA targeting: what to verify at each link

The Proof-Chain Adversarial (PCA) for Paper 13b should target
character-modulation preservation at each link. Below is the specific
attack surface for each link:

### Link 1 (BC_chi construction)

**PCA target:** Does chi-modulation preserve the algebraic relations of
the BC system?

- Verify: mu_n -> chi(n) mu_n is an algebra homomorphism
- Verify: the sigma_t automorphism group commutes with chi-twisting
- Attack vector: chi(n) = 0 for gcd(n,q) > 1 -- does this introduce
  zero divisors?
- Expected resolution: restrict to (n,q) = 1 sector; the BC algebra
  naturally handles this via the conductor filtration

### Link 2 (KMS_{1,chi} state)

**PCA target:** Is the KMS_1 state unique on BC_chi?

- Verify: KMS condition omega(a sigma_{i}(b)) = omega(b a) transfers
- Attack vector: chi-twisting might break the extremality condition,
  allowing multiple KMS_1 states
- Expected resolution: the Galois action on KMS states (Bost-Connes
  Theorem 25) already parameterizes KMS states by characters; KMS_{1,chi}
  IS the chi-evaluation of the unique KMS_1 state

### Link 3 (CCM_chi operators)

**PCA target:** Does the CCM construction extend to L(s,chi)?

- Verify: prolate Hilbert space construction with period L = 2 log(lambda)
  is unchanged (it depends on lambda, not on chi)
- Verify: Caratheodory-Fejer self-adjointness survives chi-twisting
- Attack vector: the spectral data changes; do the 55-digit eigenvalue
  approximations hold for L(s,chi)?
- Expected resolution: numerical verification for small conductor
  characters (q = 3, 4, 5, 7) would establish the pattern

### Link 4 (ITPFI_chi factorization)

**PCA target:** Does the tensor product factorization respect
character-modulation?

- Verify: omega_{1,chi} = tensor_p omega_{1,chi}^p
- Verify: each of the three ITPFI proofs (Euler product, BC amenability,
  Araki-Woods) transfers
- Attack vector: the Euler product for L(s,chi) has chi(p) factors;
  do these propagate correctly through the tensor product?
- Expected resolution: chi(p) is a root of unity for each p, so the
  tensor product picks up a phase that does not affect the factorization
  structure

### Link 5 (Estimates_chi)

**PCA target:** Do all four estimates survive chi-twisting?

This is the CRITICAL link. Each estimate must be individually verified:

- **5a (Archimedean):** The ratio norm(tau^(R)) / norm(Sigma_p tau^(p))
  should be O(1/lambda) regardless of chi. Attack vector: the gamma
  factor for L(s,chi) includes a shift for odd characters; does this
  break the O(1/lambda) bound?

- **5b (Eigenvector approximation):** Davis-Kahan perturbation theory is
  character-agnostic. The ITPFI triangle inequality transfers if Link 4
  closes. Lower risk.

- **5c (H^1 regularity):** THIS IS THE HARDEST. The Fourier-basis
  cancellation in Paper 13 uses the specific structure of the zeta
  function's spectral data. For L(s,chi), the Fourier coefficients
  acquire chi(n) factors. Attack vector: does the weight (1 + (2pi n/L)^2)
  still cancel the resolvent denominator when chi(n) modulates the
  coefficients? Expected: yes, because the cancellation is analytic
  (involving the resolvent) not arithmetic (involving the coefficients).
  But this MUST be verified explicitly.

- **5d (CF decay):** The CF approximation rho >= 4.27 may depend on the
  specific spectral data. For L(s,chi), the spectral data changes.
  Attack vector: does rho degrade for large conductor? Expected: rho
  depends on the prolate operator spectrum, which is controlled by the
  bandwidth lambda, not by chi.

### Links 6-7 (Boegli_chi, Hurwitz_chi)

**PCA target:** Minimal. These are general theorems applied to specific
inputs. If Links 1-5 provide correct inputs, Links 6-7 follow.

- Verify: Lambda(s,chi) is not identically zero (trivially true for
  primitive chi)
- Verify: uniform convergence of hat{xi}_{N,chi} on compacts (follows
  from Link 5 estimates)

### Link 8 (GRH conclusion)

**PCA target:** Pure logic check. Self-adjointness of D_{infinity,chi}
implies real spectrum implies GRH for chi.

---

## 4. Programme graph connections

Paper 13b (GRH) connects to the broader programme as follows:

```
                    Paper 13 (RH)
                        |
                    [depends on]
                        |
                    Paper 13b (GRH) ----[enables]----> Paper 26 (BSD)
                        |                                  |
                        |                             [L-functions of
                        |                              elliptic curves]
                        |
                    [constrains]
                        |
                 +------+------+
                 |             |
            Paper 28       Paper 12
            (PvNP)         (H12: Gauge
                            hierarchy)
```

### Edge: Paper 13b -> Paper 26 (BSD)

BSD requires the analytic rank of an elliptic curve E to equal its
algebraic rank. The analytic rank is defined via the L-function L(s,E),
which for CM curves factors through Hecke L-functions -- which are
Dirichlet L-functions twisted by Grossencharacters. GRH for these
characters constrains the zero distribution of L(s,E), strengthening
the BSD approach.

Specifically: if GRH holds for all characters arising from the CM type
of E, then the analytic continuation and functional equation of L(s,E)
are well-controlled, and the Kolyvagin-Gross-Zagier machinery (used
in Paper 26) operates on solid ground.

### Edge: Paper 13b -> Paper 28 (PvNP)

The PvNP proof (Paper 28) uses spectral gap arguments that connect to
the distribution of primes in arithmetic progressions. GRH gives the
strongest known error term for prime counting in progressions:

  psi(x; q, a) = x/phi(q) + O(x^{1/2} log^2 x)

This error term, conditional on GRH, provides the arithmetic input for
the spectral gap lower bounds in the Popa rigidity framework.

### Edge: Paper 13b -> Paper 12 (H12: Gauge hierarchy)

The gauge hierarchy problem (Paper 12) requires fine-tuning cancellations
in the ~~5D compactification~~ 4+1 coordinate structure (S¹ internal phase fiber) <!-- legacy 2026-04-15: "5D compactification" → "4+1 coordinate structure (S¹ internal phase fiber)" per north-star.md §0.10 Vocabulary Canon, Intervention 8 (Agent B) -->. GRH for characters associated with the
bridge family (k = 2,3,4,6) constrains the arithmetic of the
compactification manifold, providing number-theoretic bounds on the
hierarchy ratio m_W/m_Pl.

### Edge: Paper 13 -> Paper 13b (dependency)

This is the critical edge. Paper 13b CANNOT stand without Paper 13.
If any layer of the RH chain fails, the corresponding link of the GRH
chain fails. The dependency is strict, non-negotiable, and acknowledged.

---

## 5. Honest assessment and timeline

### If Paper 13 RH closes unconditionally

GRH becomes a systematic verification programme. The proof machinery
exists; the task is to verify that character-modulation preserves it
at each of the 8 links.

**Estimated timeline: 6 months of focused work.**

Breakdown:
- Month 1: BC_chi construction and KMS_{1,chi} uniqueness (Links 1-2).
  This is mostly formal algebraic verification, drawing on the extensive
  Bost-Connes literature.
- Month 2: CCM_chi operator construction and numerical verification
  (Link 3). Run CCM's code with L(s,chi) spectral data for the 4 pilot
  characters. Verify 55-digit eigenvalue agreement.
- Months 3-4: Estimate verification (Link 5). This is the bulk of the
  work. Each of the four estimates must be individually verified with
  chi-modulation. The H^1 Fourier-basis cancellation (Estimate 5c) is
  the hardest and may require a new lemma.
- Month 5: ITPFI_chi factorization (Link 4). Verify the three proofs
  transfer. This may reveal a new proof route specific to L-functions.
- Month 6: Assembly (Links 6-8). Apply Boegli and Hurwitz to the
  character-twisted operators. Write the paper.

### If Paper 13 RH remains conditional on CCM

GRH inherits the CCM conditionality at Link 3. The paper would be
stated as:

  "GRH conditional on CCM (arXiv:2511.22755) and Paper 13 (RH)."

This is still valuable: it demonstrates that the CCM framework, if
correct, implies not just RH but the full GRH for Dirichlet characters.
The philosophical impact is substantial even without unconditional proof.

### Risk assessment

| Risk | Probability | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Character-twist breaks KMS uniqueness | 5% | Fatal for Link 2 | Literature search: character-twisted KMS states are known (Laca-Larsen-Neshveyev) |
| H^1 Fourier cancellation fails for L(s,chi) | 15% | Blocks Link 5c | Explicit computation for chi mod 3; find alternative cancellation mechanism |
| CCM construction does not extend | 10% | Blocks Link 3 | Numerical verification before attempting proof |
| ITPFI tensor product incompatible with chi | 10% | Blocks Link 4 | Euler product proof transfers most naturally; focus there first |
| Paper 13 RH itself fails | See Paper 13 accounting | Fatal for all links | Independent risk; not mitigatable from Paper 13b |

### Overall confidence

**~5/8 if Paper 13 RH is correct.** This reflects:
- High confidence (8/10) that the framework transfers
- Moderate confidence (5/10) that the estimates carry through without
  surprises
- The 5/8 is a floor, not a ceiling: each verified link raises
  confidence for the remaining links, since the character-modulation
  either works systematically or fails early

### Pilot strategy

Before attempting the full GRH, run the chain for ONE character:

  **chi = (-4/.), the non-principal character mod 4.**

This is the simplest non-trivial Dirichlet character. L(s,chi) = beta(s)
(the Dirichlet beta function) has well-understood zeros. If the 8-link
chain closes for this single character, the pattern for general chi
should be clear.

After the pilot, extend to the 4 bridge family characters
(k = 2,3,4,6) before attempting the general case.
