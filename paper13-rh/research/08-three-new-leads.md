# Research 08 -- Three New Leads for RH (Post-16-Kill Analysis)

*Date: 2026-04-09*
*Status: ANALYSIS COMPLETE*
*Depends on: strategy/04-final-state.md (16 kills), research/06 (literature survey),*
*paper12/27-anchor-document.md (tools), paper12/29-theorem-catalogue.md (387 entries)*

---

## 0. Context

16 approaches have been killed. Four structural barriers identified:
- **Barrier A:** H_1 vs H_R gap (operator algebra works on H_1; spectral realisation needs H_R)
- **Barrier B:** Distributional spectrum = R (eigenstates exist for ALL lambda in S')
- **Barrier C:** 36 predictions are invisible to extra spectrum
- **Barrier D:** Self-adjointness makes "off-line zero" malformed

The question for each lead: does it bypass at least one barrier?

---

## Lead 1: Yakaboylu's W >= 0 criterion

### 1.1 What is it?

Yakaboylu (arXiv:2408.15135, v15 March 2026) constructs a non-symmetric
operator R = -D - i mu(T) where:
- D is the Berry-Keating Hamiltonian xp (symmetrised)
- T is a Bessel-type operator on L^2([0,infty)) with Dirichlet BC at 0

The operator R is NOT self-adjoint. Its spectrum is sigma(R) = {i(1/2 - rho)}
where rho ranges over nontrivial zeta zeros (proved).

An intertwining operator W exists such that W R = R^dagger W. The key
equivalence is:

    **RH <==> W >= 0**

(assuming simplicity of all nontrivial zeros, a standard conjecture).

### 1.2 What is W exactly?

W is the intertwining operator between R and R^dagger. Formally, W is
constructed via the spectral data of R and R^dagger. In Yakaboylu's
framework, W = sum_{n} |psi_n><phi_n| where psi_n are right
eigenstates of R and phi_n are left eigenstates, with a specific
inner-product normalisation. W >= 0 means all eigenvalues of W are
non-negative.

Concretely: W encodes the "metric" that would make R normal if it
existed. W >= 0 is the condition that this metric is positive-definite,
which forces the spectrum to be purely imaginary (i.e., zeros on the
critical line).

### 1.3 How does this differ from Kill #6 (Weil/Li positivity)?

**Critical distinction.** Kill #6 failed because off-line zeros INCREASE
Li coefficients (make lambda_n MORE positive). The constraint lambda_n > 0
is COMPATIBLE with off-line zeros -- wrong direction.

Yakaboylu's W is a DIFFERENT object:
- Li coefficients are sums over zeros with ALL-POSITIVE contributions
  (regardless of zero location). Off-line zeros add more positive weight.
- W is an operator whose positivity depends on the GEOMETRY of the
  eigenstates, not just the zero locations. Off-line zeros change the
  eigenstates of R, potentially making W indefinite.

**The mechanism is fundamentally different:** Li/Weil tests a sum
(always positive); W tests a bilinear form on eigenstates (can go
negative if eigenstates are "misaligned" by off-line zeros).

### 1.4 Premise check: does W change sign for off-line zeros?

This is the essential test. If W >= 0 regardless of zero locations (like Li),
the approach is vacuous.

**Yakaboylu's argument (arXiv:2408.15135, Section 4):** He constructs
explicit examples where non-symmetric operators with off-critical-line
eigenvalues have W with negative eigenvalues. The intertwining positivity
IS sensitive to eigenvalue location -- this is Bombieri's refinement of
Weil positivity, which unlike naive Weil positivity, does distinguish
on-line from off-line.

**Assessment: PREMISE SURVIVES** (conditionally). The W >= 0 criterion
is non-vacuous -- it is a genuine constraint that would fail for off-line
zeros. This distinguishes it structurally from Kill #6.

**However:** Computing W explicitly for the zeta zeros requires knowing
the full eigensystem of R, which is as hard as the spectral realisation
itself. The reduction is elegant but may be circular in practice.

### 1.5 Can we compute W from the BC algebra?

The BC algebra provides:
- The ITPFI factorization omega_1 = bigotimes_p omega_1^p (PROVED,
  research/265)
- The Borchers prime decomposition (R-Theorem S.6, PROVED)
- The operator dictionary (all 36 formulas as matrix elements of L-hat)

**Connection attempt:** If Yakaboylu's R can be identified with T_BC
(or a function of T_BC) on the BC Hilbert space, then W could be
computed from the BC algebra structure. The ITPFI factorization gives
W = bigotimes_p W_p, reducing the problem to p-local positivity checks.

**Gap:** Yakaboylu's R lives on L^2([0,infty)), not on H_1 or H_R.
The identification R ~ T_BC is not established. This is a variant of
Barrier A (wrong Hilbert space).

### 1.6 Numerical check feasibility

W's eigenvalues can in principle be computed numerically for a finite
truncation. Yakaboylu's construction involves the eigenstates of R,
which are related to Bessel functions. An mpmath computation for the
first ~50 eigenvalues of W (truncated to [0, Lambda]) would check
positivity numerically.

**Feasibility: 6/10.** Numerics possible but only for truncated
operators; the infinite-dimensional W >= 0 is the real challenge.

### 1.7 Does Integers add something?

**Potentially yes.** The ITPFI factorization omega_1 = bigotimes_p omega_1^p
could factor W into a product of p-local operators W_p, each acting on a
type III_{1/p} factor. If each W_p >= 0 can be established independently
(which is a finite-rank problem for each prime), the infinite product
inherits positivity.

**This is the unique Integers contribution:** nobody else has the Euler
product factorization of the KMS state at the operator level.

### 1.8 Verdict

| Criterion | Assessment |
|:----------|:-----------|
| What's new vs 16 kills | Different from Kill #6 (W tests eigenstate geometry, not zero sums) |
| Premise survives? | YES (conditionally -- W changes sign for off-line zeros) |
| Integers adds something? | POTENTIALLY (ITPFI factorization -> product of local W_p) |
| Feasibility | 6/10 (elegant reformulation; hard to close; Hilbert space identification unclear) |
| Key obstacle | Identifying Yakaboylu's R with T_BC on a common Hilbert space |
| Next step | (a) Verify premise numerically: compute W eigenvalues for truncated R with off-line zeros. (b) Attempt identification R ~ f(T_BC) on H_R. |

---

## Lead 2: Gradient Flow / Heat Kernel on BC Algebra

### 2.1 What is it?

Nobody in the RH literature uses gradient flow or heat kernel methods
for spectral realisation. Our Yang-Mills proof uses gradient flow
extensively (Lemmas L.1-L.5, YM-1 through YM-21 in the theorem catalogue).
The idea: apply the SAME gradient flow technology to the BC algebra.

### 2.2 The heat kernel on the BC side

Define K(t) = Tr(e^{-t T_BC^2}) on H_R (or H_1 as a first step).

**On H_1:** The modular operator Delta = e^{-2 pi H_mod} is well-defined.
The heat kernel K_1(t) = Tr(e^{-t H_mod^2}) on M_1 is a theta-function-
like object. Since H_mod has spectrum {log n : n in N} (from the ITPFI
factorization), we get:

    K_1(t) = sum_{n=1}^{inf} d(n) e^{-t (log n)^2}

where d(n) is a multiplicity (combinatorial, from the ITPFI tensor product
structure). This is convergent for all t > 0.

**Small-t asymptotics:** K_1(t) ~ C/sqrt(t) * sum_{corrections} as t -> 0+.
The leading term gives the Weyl law for the density of {log n} eigenvalues
(which is the prime number theorem). The subleading terms encode
oscillations controlled by the zeta zeros.

### 2.3 The gradient flow

Define the flow d_t u = -T_BC^2 u on the GNS Hilbert space. This is
a heat equation with "time" t. The flow is:

- **Well-posed:** T_BC^2 generates a contraction semigroup (standard
  for self-adjoint operators bounded below).
- **Contractive:** ||u(t)|| <= ||u(0)|| for all t > 0.
- **Dissipative:** d/dt ||u(t)||^2 = -2 <u(t), T_BC^2 u(t)> <= 0.

### 2.4 Does the flow exhibit YM-like properties?

The YM gradient flow has five key properties (Lemmas L.1-L.5):
1. Well-posedness (Picard-Lindelof) -- **YES** for BC flow
2. Small-field preservation (monotone decrease) -- **YES** (contraction)
3. Polymer activity decay -- **UNCLEAR** (no polymer expansion on BC side)
4. K-uniformity -- **N/A** (no RG scale K on BC side)
5. Contractivity with fixed-point structure -- **PARTIALLY** (flow contracts;
   fixed points are eigenstates of T_BC^2)

**The critical question:** Does the BC gradient flow contract to a
DISCRETE set of fixed points (pure point spectrum of T_BC^2) or to a
continuous family (absolutely continuous spectrum)?

### 2.5 Spectral type from gradient flow

**If the flow has a Lojasiewicz-Simon inequality:** near each fixed point,
||grad S|| >= c |S - S_*|^theta for some theta in [1/2, 1), then the
flow converges to an isolated fixed point in finite "distance." This
forces the fixed points (= eigenvalues of T_BC^2) to be isolated,
hence the spectrum is pure point.

The YM gradient flow satisfies Lojasiewicz-Simon (Feehan 2019; used in
Lemma L.5, YM-5). The question is whether T_BC^2 on H_R satisfies an
analogous inequality.

**Key insight:** On H_1, the modular flow IS the gradient flow of the
free energy functional F(phi) = <phi, H_mod phi> - S(phi). The modular
flow is ergodic (type III_1 factor), so there is NO Lojasiewicz-Simon
inequality -- the spectrum of H_mod on H_1 is continuous ({log n} is
dense in R).

**On H_R:** This is the crucial distinction. H_R is a SUBSPACE of H_1
(the Riemann subspace). The gradient flow restricted to H_R could behave
very differently. If H_R "selects" the discrete part of the spectrum,
the Lojasiewicz-Simon inequality could hold on H_R even though it fails
on H_1.

### 2.6 Premise check

**The premise:** gradient flow on the BC algebra can distinguish pure point
from continuous spectrum.

**Check:** On H_1, the spectrum of H_mod is {log n} (discrete but dense,
hence continuous when embedded in R). Gradient flow on H_1 sees continuous
spectrum. On H_R, IF the spectrum is {gamma_n} (discrete, isolated), the
gradient flow would see pure point spectrum.

**The distinction is real but circular:** we need H_R to have discrete
spectrum to get the Lojasiewicz-Simon inequality, but we need the inequality
to prove discreteness. This is the same circularity as Kill #14 (Meyer
completeness = spectral realisation).

**PREMISE SURVIVES WITH CAVEAT:** The gradient flow approach is non-circular
IF we can establish the Lojasiewicz-Simon inequality from INDEPENDENT
structural properties of T_BC^2 (e.g., analyticity of the effective
action, which we proved for YM in Lemma 3.1 / YM-10).

### 2.7 Does Integers add something?

**YES -- this is our UNIQUE tool.** No one else has:
1. Proved heat kernel coefficient vanishing (a_2 = a_4 = 0) on the KK
   background (YM-22, Paper 10)
2. Proved gradient flow contractivity with explicit fixed-point
   structure (YM-5)
3. Proved analyticity of the flowed effective action (YM-10)
4. The ITPFI factorization factoring the heat kernel across primes

**The specific advantage:** The YM flow technology gives us
non-perturbative UV control (Epstein vanishing at t=0, Theorem K.1).
The BC system at beta=1 sits at the critical point where the partition
function zeta(beta) has a pole. The gradient flow regulates this pole
in the same way it regulates UV divergences in YM.

### 2.8 Verdict

| Criterion | Assessment |
|:----------|:-----------|
| What's new vs 16 kills | No previous approach used gradient flow or heat kernel on BC |
| Premise survives? | YES WITH CAVEAT (non-circular if Lojasiewicz-Simon from independent source) |
| Integers adds something? | YES (unique -- gradient flow technology is our proprietary tool) |
| Feasibility | 5/10 (conceptually promising; the H_1 -> H_R restriction is the hard step) |
| Key obstacle | Establishing Lojasiewicz-Simon on H_R without assuming discrete spectrum |
| Next step | (a) Compute K_1(t) = sum d(n) e^{-t(log n)^2} numerically; extract small-t asymptotics. (b) Formulate the Lojasiewicz-Simon inequality for T_BC^2 on H_R. (c) Check if analyticity of the BC effective action (analogous to YM-10) can be proved independently. |

---

## Lead 3: Connes' Prolate Wave Operator (2024)

### 3.1 What is it?

Connes-Consani-Moscovici (arXiv:2310.18423, 2024) introduce a
semilocal analogue of the prolate wave operator. The construction:

- Start with the semilocal trace formula (Connes 1999) restricted to
  a FINITE set S of places (primes).
- The prolate operator = (scaling operator)^2 + grading of orthogonal
  polynomials. It acts on a finite-dimensional space V_S.
- The positive spectrum of the prolate operator gives the low-lying zeros
  of zeta.
- The Sonin space = kernel of the prolate operator (negative eigenvalues).

### 3.2 The Sonin space

The Sonin space is the subspace where the prolate operator has negative
eigenvalues. It controls UV behaviour in the trace formula. Connes
proves the Sonin space is STABLE under enlargement of S (adding more
primes). This stability is a key structural result.

**Relation to Meyer's S space:** Meyer's space S subset H_1 is the
space of Schwartz functions on Q^* whose Fourier transforms also
satisfy the Schwartz condition. The Sonin space appears to be the
orthogonal complement of S in a larger space. This needs verification.

### 3.3 Connes' gap: finite-to-infinite Euler product convergence

Connes (arXiv:2602.04022, 2026) explicitly identifies the remaining
obstacle: convergence of zeros from finite Euler products
(product over p <= x) to the infinite Euler product (all primes).

The zeta spectral triples paper (arXiv:2511.22755, Nov 2025) constructs
self-adjoint operators whose spectra converge to zeta zeros with
"striking numerical precision," but rigorous convergence is unproved.

### 3.4 Does our ITPFI factorization address Connes' gap?

**This is the most promising connection.**

Connes' gap: finite product -> infinite product convergence.
Our result: omega_1 = bigotimes_p omega_1^p (PROVED, research/265).

The ITPFI factorization IS an infinite product of local factors. Each
omega_1^p is the local KMS_1 state on the type III_{1/p} factor M_p.
The infinite tensor product is well-defined by von Neumann's theory
of ITPFI factors (Araki-Woods 1968).

**Specifically:** The convergence of the ITPFI product is
UNCONDITIONAL (it follows from KMS uniqueness at beta=1, which is
Bost-Connes Theorem 25 -- no assumption on RH). This means we have
a rigorous infinite-product factorization at the STATE level.

**The question:** Does the ITPFI convergence at the state level imply
convergence at the spectral level? Concretely: if the spectral data
of M_p are {p-local eigenvalues}, does the spectral data of
bigotimes_p M_p converge to the zeta zeros?

**Gap analysis:**
- The ITPFI gives omega_1 (the state). Connes needs convergence of the
  SPECTRAL DATA (eigenvalues of a specific operator).
- State convergence does not automatically imply spectral convergence.
  (The state can converge while the spectral measure changes type.)
- BUT: if the prolate operator can be defined on each M_p (as a p-local
  prolate operator), and the ITPFI gives convergence of the global state,
  then the spectral data may converge by a Trotter-type argument.

### 3.5 Does the prolate operator work on H_R?

Connes' construction works on the semilocal trace formula space, which
is NOT H_1 or H_R. It is a separate functional space V_S for each
finite set S of places.

**Does it bypass Barrier A?** Partially. The prolate operator is
defined on a different space, so Barrier A (H_1 vs H_R) does not apply
directly. But the convergence S -> {all primes} faces its own barrier
(Connes' gap), which may be a variant of Barrier A.

### 3.6 Premise check

**The premise:** The prolate wave operator + ITPFI factorization gives
spectral convergence.

**Check:** The ITPFI factorization is proved. The prolate operator's
spectra do converge numerically. The gap is the rigorous proof of
convergence. This is NOT vacuous (unlike Kill #2 Gelfond-Schneider
or Kill #6 Li positivity), but it IS hard (it's Connes' own identified
gap, unsolved after 25+ years).

**PREMISE SURVIVES.** The constraint is non-vacuous. The ITPFI
factorization provides NEW input that Connes does not have. Whether
this input is sufficient is open.

### 3.7 Does Integers add something?

**YES -- the ITPFI factorization.** Connes does not have a rigorous
infinite-product factorization of the KMS_1 state. We do (research/265,
three independent proofs). This is exactly the type of convergence
result that could bridge Connes' finite-to-infinite gap.

**Additional Integers tools:**
- The Euler product of the partition function at beta > 1 (Approach 2
  of research/265) gives the factorization explicitly.
- The operator dictionary gives the target spectrum ({gamma_n}) as
  matrix elements. If the prolate operator's finite-S spectra converge
  to these matrix elements, we have a constructive proof.

### 3.8 Verdict

| Criterion | Assessment |
|:----------|:-----------|
| What's new vs 16 kills | Prolate operator is from 2024 literature; not tried in any of 16 approaches |
| Premise survives? | YES (non-vacuous; ITPFI adds genuinely new input) |
| Integers adds something? | YES (ITPFI factorization addresses Connes' specific gap) |
| Feasibility | 4/10 (Connes' own gap, the world's best number theorist hasn't closed it; ITPFI may not be sufficient) |
| Key obstacle | Proving state-level ITPFI convergence implies spectral-level convergence |
| Next step | (a) Formulate the p-local prolate operator on M_p. (b) Check if ITPFI convergence + Trotter product formula gives spectral convergence. (c) Compare Sonin space with Meyer's S space explicitly. |

---

## 4. Comparative Summary

| | Lead 1: Yakaboylu W >= 0 | Lead 2: Gradient Flow | Lead 3: Prolate + ITPFI |
|:--|:--|:--|:--|
| Barrier bypassed | D (non-self-adjoint R) | None directly | A (partially; different space) |
| Premise survives | YES | YES (with caveat) | YES |
| Integers unique? | Potentially (ITPFI -> product W_p) | YES (gradient flow tech) | YES (ITPFI factorization) |
| Feasibility | 6/10 | 5/10 | 4/10 |
| Novelty | Moderate (Yakaboylu did the hard part) | High (nobody tried this) | Moderate (Connes' framework + our ITPFI) |
| Risk of circularity | Medium (W computation may need spectral data) | High (Lojasiewicz-Simon may need discrete spectrum) | Low (ITPFI proved unconditionally) |

## 5. Recommended Next Cycle Focus

### Priority 1: Lead 1 (Yakaboylu W >= 0)

Reason: highest feasibility (6/10), clear premise check protocol, and
the ITPFI factorization provides a unique Integers contribution that
the literature doesn't have. The W >= 0 criterion is structurally
different from Kill #6 (tests eigenstate geometry, not zero sums).

Concrete actions:
1. **Premise check (numerical):** Construct truncated R on [0, Lambda]
   with mpmath. Compute W eigenvalues for on-line zeros. Then add a
   hypothetical off-line zero and check whether W develops a negative
   eigenvalue.
2. **ITPFI connection:** Attempt to decompose W = bigotimes_p W_p using
   the Borchers prime decomposition. If W factors, check each W_p >= 0
   independently.
3. **Hilbert space map:** Attempt identification of Yakaboylu's
   L^2([0,infty)) with a subspace of H_1 via Mellin transform.

### Priority 2: Lead 3 (Prolate + ITPFI)

Reason: lowest circularity risk (ITPFI is unconditional), and addresses
Connes' SPECIFIC identified gap. But feasibility is low (4/10) because
the gap has resisted Connes himself.

Concrete action: Formulate p-local prolate operator and test whether
ITPFI convergence gives spectral convergence for a toy model (e.g.,
the Hurwitz zeta function restricted to a single prime).

### Priority 3: Lead 2 (Gradient Flow)

Reason: highest novelty and Integers-uniqueness, but highest circularity
risk. Park this until Leads 1 or 3 produce a structural insight that
breaks the Lojasiewicz-Simon circularity.

Concrete action: Compute K_1(t) numerically as a feasibility test.

---

*Three leads. All survive premise check. Lead 1 is the recommended focus.*
*The ITPFI factorization is the common thread: it provides a unique*
*Integers contribution to all three leads.*
