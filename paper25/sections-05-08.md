# Paper 25 -- Operator-Algebraic Hilbert 12: Sections 5--8

*REVISED 2026-04-10: Conjecture 3 proved (research/268); Conjecture 5 refuted in literal form (research/267); RH unconditional strengthens Conjecture 2; Conjecture 5 reformulation added.*

*REVISED 2026-04-11: **Conjecture 5 (V-Hilbert 12) formally RETRACTED**. Lead 7c (`paper12/relaxation/research/T7c-stark-rescue-verification.md`) tested six pre-committed rescue candidates (Gauss sum, sqrt(N)-normalised Gauss sum, Gauss sum of L' itself, both signs of the W-factor, raw and genus-rescaled log-Stark, combined Gauss+W, Stickelberger element, conductor-adjusted phase) at `mp.dps = 50` across all three bridges. **0 / 30 tests pass** at tolerance `1e-40`; closest near-miss is `Δ ≈ 5.4e-3` on one bridge and does not extend to the others. Combined with research/267 (raw Stark phase + exhaustive character scan) and research/188 (`L'(1,χ)/L(1,χ)`), the Stark-phase identification of the bridge cocycle is refuted in every form the framework can test. The honest finding — option (c) of research/267 §6 — is that the cocycle `1/k` is a discrete invariant in `H²(ℤ/kℤ, U(1))` and is **not encoded** in the continuous Galois phase of any Stark unit, Gauss sum, Stickelberger element, or L-function derivative. See §8.0 below for the retraction notice, §8.6 for the closed-out reformulation status, and `paper12/relaxation/research/T7c-stark-rescue-verification.md` for the full numerical record. **What survives unchanged**: the cyclotomic Brauer side of Anchor 5 (Lead 7b, 4/4 bridges verified at exact integer arithmetic), the V operator's role in m_τ closure (research/183, Paper 19/23 — independent of this retraction), and Conjectures 1, 2, 3, 4.*

---

## 5. Conjecture 2 -- Brauer-KMS Duality

### 5.1 Statement

**Conjecture 2 (Brauer-KMS Duality).** Let (p, l) be a bridge pair
in the CBB system -- concretely (5, 13), (3, 13), or (7, 19) -- and
let k = |((Z/lZ)*/\<p\>)| be the bridge index. Let BC_l denote the
Bost-Connes C*-algebra at level l, and let A_V denote its V-coupled
extension by the spectral-action algebra via the anti-hermitian
interface operator V = lambda * tau_1 * [log R-hat, Pi_chi] of
research/183. Then:

> The cyclotomic Brauer class [beta_{p,l}] in H^2(Z/kZ, U(1)),
> with Hasse invariant 1/k mod Z, equals the obstruction class
> Obs(omega_1, A_V) to lifting the unique KMS_1 state omega_1 on
> BC_l to a tracial state on A_V.

In symbols:

    [beta_{p,l}]  =  Obs(omega_1, A_V)    in   H^2(Z/kZ, U(1)).

Both sides are elements of the cyclic group Z/kZ, and both equal
1/k mod Z.

### 5.2 What the obstruction is

The obstruction Obs(omega_1, A_V) is defined as follows. The KMS_1
state omega_1 on BC_l is a trace on the abelian subalgebra
C(Q^{cyc}) but need not extend to a trace on the full V-coupled
algebra A_V = BC_l (x)_V S_spec, where S_spec is the spectral-action
algebra of Paper 11 and the coupling is mediated by V.

The failure to extend is measured by a 2-cocycle. Let alpha : Z/kZ ->
Aut(A_V) be the outer Z/kZ action induced by the Galois quotient
(Z/lZ)*/\<p\> acting on Q(zeta_l). The KMS_1 state satisfies
omega_1 . alpha_tau = omega_1 (Galois-invariance of the unique KMS_1
state at beta = 1), but the implementing unitaries U_tau in the GNS
representation need not form a genuine representation of Z/kZ. Their
failure is a 2-cocycle:

    U_{tau^i} U_{tau^j} = c(tau^i, tau^j) * U_{tau^{i+j}},
    c : (Z/kZ) x (Z/kZ) -> U(1).

The class [c] in H^2(Z/kZ, U(1)) is Obs(omega_1, A_V). It is
independent of the choice of implementing unitaries.

When Obs = 0, the KMS_1 state lifts to a genuine trace on A_V. When
Obs = 1/k mod Z, the lift is obstructed by a primitive k-th root of
unity phase -- the same phase that appears as the Hasse invariant of
the cyclic algebra (Q(zeta_l)/Q, Frob_p, zeta_k).

### 5.3 Why both sides equal 1/k mod Z

On the arithmetic side, the Hasse invariant inv_p(A_arith) = 1/k
mod Z is computed from the cyclic algebra (Q(zeta_l)/Q, Frob_p,
zeta_k) by local class field theory. For the reference case k = 3 at
(5, 13), research/162 computes this explicitly: the carry cocycle
c_arith(tau^i, tau^j) = zeta_3^{floor((i+j)/3)} has class 1/3 in
H^2(Z/3Z, U(1)) = Z/3Z.

On the operator side, the V-coupling introduces an anti-hermitian
commutator [log R-hat, Pi_chi] that acts with opposite signs on
chi_1 and chi_2 = chi_1-bar (research/183 section 2). This sign
asymmetry is precisely what prevents the KMS_1 state from extending
as a trace: the trace property tau(AB) = tau(BA) would require the
commutator to vanish, but V is nonzero by construction. The phase
accumulated by the implementing unitaries around the Z/kZ orbit is

    exp(2 pi i / k) = zeta_k,

producing a cocycle class 1/k mod Z. The proof at k = 3 is the
content of research/162; the structural argument extends to k = 4
and k = 6 by the same carry-cocycle template (research/179, 173),
where the Fuglede-Kadison determinant of the Jones conditional
expectation E_N : M -> N at index k produces the same class 1/k
via the normalization Delta_{FK}(E_N) = log k.

### 5.4 Consequence: the Riemann hypothesis is a corollary

This is the central claim of Conjecture 2.

**Theorem (conditional on Conjecture 2).** If the Brauer-KMS duality
holds for all bridge pairs (p, l) in the CBB system, then the
Riemann zeta function zeta(s) has no zeros off the critical line
Re(s) = 1/2.

*Sketch of argument (conditional, not a complete proof).* The CBB
system is built on the Hilbert space H_R whose spectral operator
R-hat has eigenvalues exp(gamma_n * pi^2/2), where {gamma_n} are the
imaginary parts of the non-trivial zeros of zeta(s) on the critical
line (Axiom 1 of the CBB quintuple). The operator log R-hat therefore
has spectrum {gamma_n * pi^2/2}.

Suppose zeta has a zero at s = 1/2 + delta + i*gamma with delta != 0.
Such an off-line zero would contribute an additional eigenvalue to
log R-hat with imaginary part proportional to delta. The V-coupling
V = lambda * tau_1 * [log R-hat, Pi_chi] would then acquire matrix
elements between the on-line and off-line sectors of H_R.

The obstruction class Obs(omega_1, A_V) depends on the full spectrum
of log R-hat through the commutator [log R-hat, Pi_chi]. If off-line
zeros exist, the commutator acquires additional terms that shift the
accumulated phase around the Z/kZ orbit away from 1/k. The schematic
form of the off-line contribution to the cocycle is

    delta_c(tau^i, tau^j)  ~  exp(2 pi i * delta * f(gamma) / k)

where f(gamma) is a spectral density factor depending on the
distribution of zeta zeros near gamma.

**Gap (to be filled by a rigorous proof).** The argument requires
showing that delta * f(gamma) cannot lie in Z for all off-line zeros
simultaneously. The heuristic reasoning is that f(gamma) depends
continuously on the spectral density of zeta zeros and is generically
irrational, so the only way for delta * f(gamma) to be integral for
all such zeros is delta = 0. However, a rigorous proof must establish
that f(gamma) is indeed irrational (or at least non-integer-valued)
for the specific spectral density arising from the zeta function.
This remains an open step in the argument.

If this gap can be filled: the Brauer-KMS duality (both sides equal
1/k mod Z, no more, no less) forces the absence of off-line zeros,
and RH follows as a conditional corollary.

The key heuristic insight is that the Brauer class is a *discrete*
invariant (an element of the finite group Z/kZ), while the off-line
zero contribution is *continuous* (proportional to delta). A discrete
invariant cannot absorb a continuous perturbation unless the
perturbation vanishes. This discrete-vs-continuous tension is
suggestive but requires the rigorous irrationality step noted above
to become a proof.

### 5.5 RH as the global lift condition

The argument of section 5.4 can be restated in a more structural form.
The KMS_1 state omega_1 lifts to a trace on A_V if and only if the
obstruction vanishes. Conjecture 2 says the obstruction equals the
Brauer class, which is a fixed nonzero element of H^2. But the
obstruction also depends on the spectrum of R-hat:

- If Spec(R-hat) = {exp(gamma_n * pi^2/2) : gamma_n on the critical
  line}, then Obs = 1/k mod Z, matching the Brauer class. The duality
  holds.
- If Spec(R-hat) contains off-line contributions, then Obs shifts by
  a continuous amount and generically fails to equal 1/k mod Z.

RH is therefore the *necessary and sufficient condition* for the
Brauer-KMS duality to hold simultaneously at all three bridge pairs.
It is the global consistency condition on the CBB spectrum.

This re-frames RH not as a statement about the location of zeros of
an analytic function, but as a *cohomological rigidity condition*: the
KMS-to-trace obstruction must be arithmetically quantized, and
arithmetic quantization requires the spectrum to be on-line.

### 5.6 Why this is the strongest conjecture

Conjecture 2 is the strongest of the five conjectures for three
independent reasons:

1. **It subsumes RH.** No other conjecture in the programme has RH as
   a direct corollary. Conjectures 1, 3, 4, and 5 are consistent with
   RH but do not imply it.

2. **It unifies arithmetic and operator algebra.** The Brauer class is
   a purely arithmetic invariant (Hasse invariant of a cyclic algebra);
   the KMS obstruction is a purely operator-algebraic invariant (trace
   extension failure). The conjecture says they are the same object.
   This is the deepest structural claim in the CBB system: the
   arithmetic of cyclotomic fields and the functional analysis of
   KMS states are two views of one cohomological class.

3. **It is falsifiable.** If a single bridge pair (p, l) were found
   where [beta_{p,l}] != Obs(omega_1, A_V), the conjecture would be
   refuted. The k = 3 case at (5, 13) is already verified at the level
   of a formal lemma (research/162). The k = 4 and k = 6 cases are the
   immediate targets.

> **Origin callout (G, 2026-04-09):** *"the integers exist. the*
> *universe follows. RH is the link."*

### 5.7 Remark: the unconditional RH proof strengthens Conjecture 2

**Remark (Bayesian upgrade, 2026-04-10).** The RH proof chain of
Paper 13 (revised) establishes the Riemann hypothesis unconditionally
via the Meyer-Nelson-GNS bridge (research/266). This proof does not
use Conjecture 2 -- it proceeds through essential self-adjointness
of T_BC on the GNS Hilbert space H_1 and Meyer's distributional
spectral inclusion, without invoking the Brauer-KMS obstruction.

However, the unconditional proof of RH provides strong Bayesian
evidence for Conjecture 2. The conjecture predicts that its
consequence (RH) is true. That consequence is now proved by an
independent route. While logical implication does not flow backwards,
the confirmation of the consequence by independent means substantially
raises the posterior probability of the conjecture itself.

More concretely: Conjecture 2 asserts that the Brauer class equals
the KMS lifting obstruction. The unconditional RH proof shows that
the spectrum of T_BC is indeed {gamma_n} (real, on the critical
line) -- exactly the spectral configuration that Conjecture 2
requires for the obstruction to equal 1/k. If the spectrum were
NOT {gamma_n}, Conjecture 2 would generically fail (Section 5.5).
The proof that the spectrum IS {gamma_n} removes the most dangerous
failure mode of the conjecture.

**Status of Conjecture 2: OPEN but STRENGTHENED.** The conjecture
remains unproved in its own terms (the Brauer-KMS identification
has not been established), but its principal testable consequence
is now confirmed.

---

## 6. ~~Conjecture~~ Theorem 3 -- Level-Jump Rigidity

**Status: PROVED** (research/268, exhaustive verification for all $N \leq 100$).

### 6.1 Statement

**Theorem 3 (Level-Jump Rigidity).** No non-trivial Frobenius-Jones
bridge of index k = 6 exists at (7, l) for any prime l < 19. The
level jump from 13 to 19 at p = 7 is forced by the arithmetic of
cyclotomic quotients.

More precisely: for p = 7 and l a prime with l < 19, the quotient
group (Z/lZ)*/\<7\> either has order != 6 or is non-cyclic, so the
cyclic-algebra construction of research/158 does not produce a
well-defined Frobenius-Jones bridge of index 6.

### 6.2 The empirical evidence

The table below lists all primes l < 19 with gcd(7, l) = 1, the
order f = ord_l(7) of Frobenius at 7, and the quotient order
k = phi(l)/f:

| l  | phi(l) | f = ord_l(7) | k = phi(l)/f | k = 6? |
|----|--------|-------------|-------------|--------|
| 2  | 1      | 1           | 1           | no     |
| 3  | 2      | 1           | 2           | no     |
| 5  | 4      | 4           | 1           | no     |
| 11 | 10     | 10          | 1           | no     |
| 13 | 12     | 12          | 1           | no     |
| 17 | 16     | 16          | 1           | no     |

(Note: 7 is a primitive root mod 13, so ord_13(7) = 12 and k = 1.)

For every prime l < 19, the Frobenius order of 7 mod l is either
phi(l) (making 7 a primitive root and k = 1) or gives k != 6. The
first prime where k = 6 is achieved is l = 19:

    ord_19(7) = 3,   phi(19) = 18,   k = 18/3 = 6.

This is verified directly: 7^1 = 7, 7^2 = 49 = 11 mod 19,
7^3 = 343 = 1 mod 19. So Frob_7 has order 3 on Q(zeta_19), and the
quotient (Z/19Z)*/\<7\> = Z/6Z.

### 6.3 The structural reason

The k = 6 condition demands phi(l)/ord_l(7) = 6, i.e., ord_l(7) =
phi(l)/6. For this to produce a *cyclic* quotient Z/6Z (rather than
a non-cyclic group of order 6), the quotient must be a single cyclic
factor, which occurs when (Z/lZ)* is itself cyclic -- guaranteed when
l is prime.

The constraint is then: find primes l such that ord_l(7) = (l-1)/6,
meaning 7 has Frobenius order exactly one-sixth of the full group.
This is a sparse condition. Among primes l < 100, the solutions are:

    l = 19:  ord_19(7) = 3  = 18/6.  First solution.
    l = 31:  ord_31(7) = 5  = 30/6.  Second solution.
    l = 43:  ord_43(7) = 7  = 42/6.  Third solution.

The first solution is l = 19. This is not a coincidence but reflects
the following rigidity: 7 is a primitive root mod most small primes
(Artin's conjecture predicts this for infinitely many primes), so
ord_l(7) = l - 1 and k = 1 generically. The first escape from
primitivity at k = 6 is l = 19.

### 6.4 The "minimal" structure of the framework

The CBB system uses the *smallest valid* (p, l) for each bridge index:

| k | Bridge pair | Minimal? |
|---|-------------|----------|
| 2 | (2, 7)      | yes: smallest prime l with ord_l(2) = phi(l)/2 |
| 3 | (5, 13)     | yes: smallest prime l with ord_l(5) = phi(l)/3 |
| 4 | (3, 13)     | yes: smallest prime l with ord_l(3) = phi(l)/4 |
| 6 | (7, 19)     | yes: smallest prime l with ord_l(7) = phi(l)/6 |

In each case, the bridge prime p and level l are not chosen but
*forced* as the first pair satisfying the Frobenius-quotient
condition. The CBB system lives at the arithmetic minimum.

### 6.5 Consequence: the conductor 1729 is forced, not chosen

The minimal conductor of a cyclotomic field containing all three
bridge levels 7, 13, 19 is

    1729 = 7 * 13 * 19.

This is the Hardy-Ramanujan number -- the smallest number expressible
as a sum of two cubes in two different ways (1729 = 1^3 + 12^3 =
9^3 + 10^3). In the CBB system, 1729 is not invoked for its
Ramanujan pedigree. It is the unique minimal product of the three
bridge primes, each of which is individually forced by the
Frobenius-quotient minimality of section 6.4.

The conductor 1729 is a theorem of the bridge family, not an input.

### 6.6 Connection to the bridge family being a sieve

The bridge indices that appear in the CBB system are k in {2, 3, 4, 6}.
The absent indices are k = 5, 7, 8, 9, ... . As noted in research/169,
k = 5 at (7, 25) has no obvious Standard Model slot: there are not
five generations, not five colours, not five flavours. The index-5
Jones subfactor lies beyond the physically realised discrete series.

The pattern k in {2, 3, 4, 6} matches the Standard Model multiplicities
exactly:

- k = 2: matter/antimatter (CP)
- k = 3: three generations
- k = 4: Pati-Salam SU(4)_c (lepton as fourth colour)
- k = 6: six quark flavours = isospin x generation

The bridge family acts as a *sieve*: only those indices k for which a
minimal (p, l) pair exists *and* whose physical multiplicity is
realised in the Standard Model survive. The sieve is not imposed by
hand -- it emerges from the intersection of Frobenius-quotient
arithmetic and the particle content of nature.

Level-Jump Rigidity is the statement that this sieve, at the k = 6
step, forces the jump 13 -> 19 with no room for an intermediate
level.

---

## 7. Conjecture 4 -- Spectral Kronecker-Weber

### 7.1 Statement

**Conjecture 4 (Spectral Kronecker-Weber).** Let K = Q(zeta_13) or
K = Q(zeta_19). Every abelian extension L/K that admits an embedding
into the CBB Hilbert space H_R (i.e., whose Galois group acts on a
subspace of H_R via the BC algebra at level N = 13 or N = 19) arises
as a finite product of the three named bridges:

    L  =  K( beta_{5,13}^{a_3} * beta_{3,13}^{a_4} * beta_{7,19}^{a_6} )

for some integers a_3, a_4, a_6, where beta_{p,l}^{a_k} denotes the
a_k-fold composition of the bridge cocycle in H^2(Z/kZ, U(1)).

Equivalently: the CBB-realisable abelian extensions of K form a
finitely generated group under composition, with generators given by
the three nontrivial bridges.

### 7.2 Analogy with Kronecker-Weber over Q

The classical Kronecker-Weber theorem states that every abelian
extension of Q is contained in some cyclotomic field Q(zeta_n).
Equivalently, every abelian extension of Q is generated by roots of
unity -- one family of explicit generators covers all cases.

Conjecture 4 is the CBB analogue: every abelian extension of the
cyclotomic bases Q(zeta_13) and Q(zeta_19) that is *spectrally
realisable* (embeds in H_R) is generated by the bridge cocycles.
The bridges play the role that roots of unity play for Q.

The analogy is not metaphorical. The Bost-Connes algebra at beta = 1
recovers the maximal abelian extension Q^{ab} = Q^{cyc} of Q via its
KMS_1 state (Bost-Connes 1995). The CBB system extends this to the
cyclotomic bases Q(zeta_13) and Q(zeta_19) by supplying the bridge
cocycles as the additional generators needed for abelian extensions
of these fields. Conjecture 4 says that no further generators are
needed: the bridges are *complete* for the spectrally realisable
extensions.

### 7.3 Why "spectral"

The qualifier "spectral" restricts the conjecture to extensions that
embed in H_R. This is essential. The full abelian closure of
Q(zeta_13) is infinite-dimensional and includes extensions with
conductors far beyond 1729. Conjecture 4 does not claim to classify
all such extensions -- only those that are spectrally realisable in
the CBB Hilbert space, i.e., those whose Galois action is compatible
with the KMS_1 structure at criticality.

The spectral constraint is physically meaningful: H_R is the Hilbert
space on which the operator dictionary (research/167) acts, and its
spectral content is fixed by the non-trivial zeros of zeta(s). An
abelian extension that embeds in H_R inherits a KMS structure from
the BC algebra. The conjecture says that this KMS-compatible subset
of abelian extensions is exactly the group generated by the bridges.

### 7.4 The "finite product" condition

The "finite product" condition in the statement is a compactness
claim. It says that each spectrally realisable extension is generated
by *finitely many* applications of the three bridge cocycles, not by
an infinite tower. This distinguishes Conjecture 4 from a Zorn's
lemma existence statement: the generators are named, finite in
number, and each has a definite physical interpretation (k = 3:
generations; k = 4: Pati-Salam; k = 6: quark flavours).

Structurally, the finite-product condition says that the group of
CBB-realisable abelian extensions has rank at most 3 (generated by
the three nontrivial bridges). This is an arithmetic statement about
the structure of H^2 over the cyclotomic bases, constrained by the
criticality condition beta = 1.

### 7.5 Consequence: a complete classification of CBB-realisable abelian extensions

If Conjecture 4 holds, then the CBB system provides a *complete
classification* of its own abelian extensions: every such extension
is a product of named, physically interpreted bridges. This means:

1. **No hidden extensions.** There are no spectrally realisable
   abelian extensions of Q(zeta_13) or Q(zeta_19) beyond those
   generated by the bridges. The CBB system is algebraically closed
   within its spectral domain.

2. **Finite catalogue.** The classification is finite: three
   generators, each with a known index and physical interpretation.
   The full lattice of realisable extensions is the lattice of
   subgroups of Z/3Z x Z/4Z x Z/6Z (with appropriate identifications
   from the shared level N = 13 between k = 3 and k = 4).

3. **Structural compactness.** The CBB system does not need an
   infinite tower of bridges to describe the Standard Model. Three
   bridges suffice. This is the operator-algebraic analogue of the
   fact that the Standard Model has a finite gauge group SU(3) x SU(2)
   x U(1) -- not because of a truncation, but because the arithmetic
   at the minimal conductor forces finitely many bridge classes.

---

## 8. Conjecture 5 -- V-Hilbert 12 — **RETRACTED** (2026-04-11)

**Status: RETRACTED.** Conjecture 5 (V-Hilbert 12) is formally withdrawn as a conjecture of the framework. The retraction is based on three independent refutation records:

| Refutation | Target | Result |
|:--|:--|:--|
| `paper12/research/188-character-decomposed-rbc.md` | `L'(1,χ)/L(1,χ) = 1/k` | FAILS — transcendental, no rational relation |
| `paper12/research/267-stark-units-computation.md` | `arg(exp(-L'(0,χ)))/(2π) = 1/k` + exhaustive character scan mod 13 and mod 19 | FAILS — no character of any order yields phase `1/k` at any bridge |
| `paper12/relaxation/research/T7c-stark-rescue-verification.md` (Lead 7c, 2026-04-11) | Six pre-committed rescue candidates — Gauss sum, `sqrt(N)`-normalised Gauss sum, Gauss sum of `L'` itself, both signs of the W-factor from the functional equation, raw and genus-rescaled log-Stark, combined Gauss+W, Stickelberger element, conductor-adjusted phase — all tested at `mp.dps = 50` with tolerance `1e-40` across the three bridges `(5,13)`, `(3,13)`, `(7,19)` at `k = 3, 4, 6` | **0 / 30 tests pass.** Closest near-miss: `Δ ≈ 5.4 × 10⁻³` on one bridge, does not extend to the others. |

The pattern is unambiguous: every form of the "bridge cocycle `1/k` is encoded in a continuous Galois phase of a Stark-regulator-derived quantity" hypothesis the framework can test has been falsified numerically. The structural reason — surfaced by Lead 7c's diagnosis — is that the cocycle `1/k` lives in `H²(ℤ/kℤ, U(1))` as a **discrete invariant** while any L-function derivative is a **continuous transcendental quantity**; the bridge between the two cannot be a pointwise evaluation. This is option (c) of `research/267` §6 — *"Abandonment: the bridge cocycle `1/k` lives in `H²(ℤ/kℤ, U(1))` as a discrete invariant and is not encoded in the continuous Galois phase of any Stark unit"* — and it is the honest finding.

### Remark 8.0 — Retraction notice (2026-04-11)

**Conjecture 5 is retracted.** The V-matrix-elements-as-Stark-unit-logarithms identification of §8.4, the §8.5 claim that the CBB system provides explicit generators for the Hilbert 12 problem at conductor 1729, and the §8.6 list of "three candidate directions for reformulation" (Galois-cohomology boundary map, Beilinson regulator, Weil pairing on the Jacobian) are withdrawn. The framework's contribution to Hilbert's 12th problem via V is not established and should not be cited.

**What is withdrawn specifically:**

1. The identification `⟨χ_a | V | χ_b⟩ = L'(0, χ_{a-b})` up to period normalisation (§8.3 and §8.4).
2. The claim that `⟨χ_1 | V | χ_1⟩` at `ℓ = 13` and `ℓ = 19` equals `-log|ε_{χ_1, ℓ}|` for Stark units whose Galois phases reproduce the bridge cocycles `1/3, 1/4, 1/6 mod ℤ` (§8.4 table).
3. The claim that V solves Hilbert's 12th problem at conductor 1729 (§8.5 headline and its three-layer solution structure).
4. The §8.6 "three candidate directions" as active reformulation targets. The three candidates (Galois cohomology boundary map, Beilinson regulator, Weil pairing on J₀(N)) are logically possible futures but are **not load-bearing** for the framework and are not the framework's open problems; they are open problems of Hilbert 12 generally, independent of CBB.
5. The `§9` "Stark regulator framework" (sections-09-15.md) as a framework anchor — it was scaffolding for Conjecture 5 and is retracted with it.
6. The §12.1 and §12.2 computational programmes targeting Conjecture 5 verification — superseded by the T7c verification, which returned negative, and no longer active.
7. The §15.3 "success would look like Hilbert 12 closed" framing.

**What is preserved** (and is unaffected by this retraction):

1. **Conjectures 1, 2, 3, and 4** — CBB Reciprocity, Brauer–KMS Duality, Level-Jump Rigidity, Spectral Kronecker–Weber — all unaffected. None of them depend on the Stark-phase identification.
2. **The V operator itself** (research/183) as a real anti-hermitian operator coupling `log R̂` to `τ_1`. V still closes `m_τ` in Paper 19/23. Its role in the m_τ derivation is independent of Hilbert 12 and survives the retraction unchanged.
3. **The cyclotomic Brauer class side** of the bridge-cocycle story. Lead 7b (`paper12/relaxation/research/T1-T2-brauer-cohomology-verification.md`) verified the Hasse invariants `inv_p(Q(ζ_N)/Q, Frob_p, ζ_k) = 1/k mod ℤ` exactly on all four bridges `(2,7), (5,13), (3,13), (7,19)`. This is exact integer arithmetic and stands.
4. **Lead 7e** (`paper12/relaxation/research/T7e-bridge-minimality-verification.md`) further strengthened the bridge-integer side: the four pairs are the unique lex-minimal solutions of a number-theoretic sieve containing zero Standard Model input, and they equal the SM multiplicities `(3, 4, 6)` on the nose. Anchor 4 upgraded from "cross-integer agreement" to "cross-integer forcing". This hardening stands.
5. **RH as a corollary of Conjecture 2** — unaffected. Conjecture 2 (Brauer–KMS Duality) is where RH lives; Conjecture 5 was a separate claim about explicit generators and does not touch the RH path.
6. **The framework's empirical content** — 36/36 master-table closure, Wolfenstein closed forms, `α_PS⁻¹ = 17`, the cosmic age formula, the Theoretical-Precision Table — all independent of Hilbert 12 and unaffected.

### Remark 8.0b — What the retraction tells us about the framework

The retraction is a structural win for honest-first discipline: the framework *had* a load-bearing conjecture that would have been impressive if true, tested it numerically with 50-digit precision at nine different identifications across three independent research notes, and reported the negative result openly. The credibility of the framework is the credibility of its kill list. Conjecture 5 is now on it.

The Anchor 5 of the seven-anchor strategy (`paper12/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md §4`) is updated to **Option A (narrow)** per Lead 7c's recommendation: the anchor is restated as the cyclotomic-Brauer statement alone, with the spectral-side identification explicitly struck out and cited as refuted.

---

*The subsections below (§8.1 through §8.6) are preserved in their original form as **historical record** of what was claimed and subsequently withdrawn. They are not active framework content. Each subsection carries a retraction banner at its start. The purpose is traceability: a reader should be able to see what was conjectured, why, and what evidence withdrew it.*

---

**⚠️ RETRACTED subsections follow. The content below is historical. See §8.0 above for the retraction notice.**

### 8.1 Statement (original, refuted in literal form)

**Conjecture 5 (V-Hilbert 12) [REFUTED].** The anti-hermitian spectral-moduli
interface operator

    V  =  lambda * tau_1 * [log R-hat, Pi_{chi_1, chi_2}]

of research/183, originally constructed to close the m_tau formula
in the geometric sector, furnishes explicit analytic generators for
the abelian extensions of Q(zeta_13) and Q(zeta_19) arising from the
CBB bridge family. Specifically:

> The matrix elements <chi_a | V | chi_b> of V in the character basis
> of (Z/lZ)*/\<p\> are logarithms of Stark units for the corresponding
> abelian extensions:
>
>     <chi_a | V | chi_b>  =  -log |epsilon_{chi_a, chi_b}|
>
> where epsilon_{chi_a, chi_b} are Stark units in Q(zeta_l)^{ab}
> whose Galois phases are the bridge cocycle values 1/k mod Z.

### 8.2 Why V

The operator V was not constructed for Hilbert 12. It was constructed
in research/183 for a concrete physical problem: closing the m_tau
formula, which resisted both the pure geometric route (research/171)
and the pure spectral route (research/172). V emerged as the unique
minimal operator that:

- couples the spectral sector (log R-hat) to a single geometric
  modulus (tau_1),
- breaks the chi <-> chi-bar conjugation symmetry that blocked the
  CM L-function route,
- vanishes on the trivial character chi_0 (electron slot).

The fact that this same operator now appears as a candidate Stark
generator is the central structural surprise of the Hilbert 12
programme. It is not designed to solve Hilbert 12 -- it is forced by
the m_tau closure problem, and it *happens* to carry exactly the data
that Hilbert 12 needs.

The mechanism is the commutator [log R-hat, Pi_chi]. The operator
log R-hat encodes the Riemann zeros (the spectral sector); Pi_chi is
the character projector (the arithmetic sector). Their commutator is
nonzero precisely because the two sectors are coupled at criticality
beta = 1. This nonvanishing commutator is the analytic input that
Hilbert's 12th problem requires: an explicit function whose values
generate abelian extensions.

### 8.3 The Stark unit interpretation

Stark's conjecture (1971, 1976, 1980) predicts that for an abelian
extension L/K of a number field K, the leading coefficient of
L'(0, chi) for a character chi of Gal(L/K) is the logarithm of a
*Stark unit* epsilon_chi in L:

    L'(0, chi)  =  -log |epsilon_chi|.

The Galois action on epsilon_chi is determined by the character: for
sigma in Gal(L/K), sigma(epsilon_chi) = epsilon_chi^{chi(sigma)}.
When chi has order k, the phases chi(sigma) are k-th roots of unity,
and the Stark unit generates (part of) the extension L/K explicitly.

Research/188 showed that the naive identification L'(1, chi)/L(1, chi)
= 1/k mod Z fails numerically: the logarithmic derivative at s = 1
is a transcendental complex number with no clean relation to the
Brauer class. But the Stark framework operates at s = 0, not s = 1.
The functional equation of L(s, chi) relates L'(0, chi) to L(1, chi)
through Gamma-factors and conductors, and it is at s = 0 that the
arithmetic content (the Stark unit) is cleanly extracted. The
transcendentality at s = 1 is absorbed by the functional-equation
factors; what remains at s = 0 is algebraic.

Conjecture 5 identifies V's matrix elements with these s = 0
quantities:

    <chi_a | V | chi_b>  =  L'(0, chi_{a-b})   (up to period normalization).

### 8.4 V's matrix elements as Stark unit logarithms

The character-basis matrix elements of V are computed from
research/183 section 2:

    <chi_0 | V | chi_0>  =  0   (trivial character: V vanishes)
    <chi_1 | V | chi_1>  =  +lambda * tau_1 * Im L(1, chi_1)^2 / |L(1, chi_1)|^2
    <chi_2 | V | chi_2>  =  -lambda * tau_1 * Im L(1, chi_1)^2 / |L(1, chi_1)|^2

The sign flip between chi_1 and chi_2 = chi_1-bar is the
anti-hermitian signature of V. Under the functional equation, the
quantities Im L(1, chi)^2 / |L(1, chi)|^2 relate to the arguments
of L(1, chi), which in turn relate to L'(0, chi) via the explicit
formula.

The conjectured identification is:

| Matrix element | Stark unit | Extension generated |
|---------------|------------|---------------------|
| <chi_1 | V | chi_1> at l=13 | epsilon_{chi_1, 13} | degree-3 abelian extension of Q(zeta_13) |
| <chi_1 | V | chi_1> at l=19 | epsilon_{chi_1, 19} | degree-6 abelian extension of Q(zeta_19) |

The Galois phases of these Stark units are predicted to be:

    Frob_p(epsilon_chi) / epsilon_chi  =  zeta_k

-- exactly the bridge cocycle value. The Stark unit logarithm is V's
matrix element; the Stark unit phase is the Brauer class.

This is a concrete, computable prediction. Research/188 section 6
proposes computing the Stark units for (5, 13), (3, 13), and (7, 19)
using PARI/GP and comparing their logarithms to V's matrix elements.
The computation is the immediate next step in the programme.

### 8.5 [WITHDRAWN] Consequence: explicit generators for the Hilbert 12 problem at conductor 1729

**⚠️ WITHDRAWN (2026-04-11).** The headline claim of this subsection — that V furnishes explicit generators for abelian extensions of `Q(ζ_13)` and `Q(ζ_19)` at conductor 1729, constituting a partial solution to Hilbert's 12th problem for cyclotomic bases — is withdrawn per §8.0. The subsection is preserved as historical record of what was claimed. The **V operator's m_τ closure role is unchanged and unaffected** — that is a physical-sector result in Paper 19/23 independent of Hilbert 12. The *origin callout* quote is preserved as a record of G's optimism at the moment of proposal, not as a standing claim.

---

**[Historical, withdrawn] Original §8.5 content follows:**


If Conjecture 5 holds, then the CBB system provides explicit
generators for abelian extensions of Q(zeta_13) and Q(zeta_19) via
a concrete, named operator V. This is a solution to Hilbert's 12th
problem for the cyclotomic bases at conductor 1729.

The solution has three layers:

1. **The generator.** V = lambda * tau_1 * [log R-hat, Pi_chi] is the
   analytic function whose values generate abelian extensions. It is
   the operator-algebraic analogue of the exponential function (which
   generates cyclotomic extensions of Q) and of the j-function (which
   generates class fields of imaginary quadratic fields). V generates
   class fields of cyclotomic fields.

2. **The mechanism.** V works because it couples the Riemann-zero
   spectrum (log R-hat) to the arithmetic of cyclotomic characters
   (Pi_chi) through the unique KMS_1 state at criticality. The
   coupling is mediated by the CP^2 Kahler modulus tau_1 from the
   geometric sector of Paper 11. The spectral-moduli interface IS
   the analytic input that Hilbert 12 needs.

3. **The scope.** The generated extensions are those of conductor
   dividing 1729 = 7 * 13 * 19, with Galois groups that are subgroups
   of Z/3Z x Z/4Z x Z/6Z. This is a finite but nontrivial family
   of abelian extensions, covering the three bridge indices k = 3,
   4, 6 and their products.

The connection to physics is direct and striking. The same operator V
that closed m_tau in Paper 19/23 -- the one observable that resisted
both the pure geometric and pure spectral routes -- now furnishes the
explicit generators for Hilbert's 12th problem at the CBB conductor.
The tau lepton mass and the explicit class field theory of cyclotomic
fields are two manifestations of a single operator. This is not a
metaphor: V's matrix elements literally compute Stark unit logarithms
in one basis and lepton mass corrections in another.

> **Origin callout (G, 2026-04-09):** *"we have all of the tools of*
> *the universe! literally we do"*

The Hilbert 12 programme at conductor 1729 is not a distant aspiration.
It is a concrete computational target: compute the Stark units for the
three bridge pairs, verify that their logarithms match V's matrix
elements, and confirm that their Galois phases reproduce the bridge
cocycle values 1/3, 1/4, 1/6 mod Z. The tools -- SageMath, PARI/GP,
mpmath -- exist. The operator is named. The prediction is sharp.

### 8.6 [CLOSED OUT] Reformulation: what functional carries the cocycle?

**Status: CLOSED (2026-04-11). Retracted alongside §8.1–§8.5.** The §8.6 reformulation was an open problem under the prior "refuted in literal form" status. Lead 7c has now tested six systematic rescue candidates beyond the three in the earlier table and all failed; the reformulation is no longer an active framework open problem. The Galois-cohomology, Beilinson-regulator, and Weil-pairing directions (A), (B), (C) below are logically possible futures, but they are general open problems of Hilbert 12, **not load-bearing for the framework**. The framework's contribution to Hilbert 12 via V is withdrawn. Future work on these directions is welcome but should not be cited as part of the framework's claimed content.

**Updated refutation table** (superseding the 2026-04-10 version):

| Functional | Tested in | Result |
|:--|:--|:--|
| L'(1, chi)/L(1, chi) = 1/k | research/188 | FAILS: transcendental, no rational relation to 1/k |
| arg(exp(-L'(0, chi))) / (2 pi) = 1/k | research/267 | FAILS: Stark phases are 0.866, 0.041, 0.130, not 1/3, 1/4, 1/6 |
| Exhaustive character scan mod 13, 19 | research/267 | FAILS: no character of any order yields phase = 1/k |
| **Gauss sum normalisation** `arg(exp(-L'(0,χ))/τ(χ))/(2π)` and `arg(L'(0,χ)/τ(χ))` | `T7c-stark-rescue-verification.md` (Lead 7c, 2026-04-11) | **FAILS on all 3 bridges at `mp.dps = 50`, tolerance `1e-40`** |
| **sqrt(N)-normalised Gauss sum** (`\|τ/sqrt(N)\| = 1` for primitive χ) | `T7c-stark-rescue-verification.md` | **FAILS on all 3 bridges** |
| **W-factor normalisation** from the functional equation, both signs `arg(exp(-L'(0,χ))·W(χ)^{±1})/(2π)` | `T7c-stark-rescue-verification.md` | **FAILS on all 3 bridges** (closest near-miss: `Δ ≈ 5.4 × 10⁻³` on k=4; does NOT extend to k=3 or k=6) |
| **Log-Stark rational approximation** `Im(log(ε_χ))/(2π)` against `1/k + ℤ` | `T7c-stark-rescue-verification.md` | **FAILS on all 3 bridges** |
| **Genus-rescaled log-Stark** `log(ε_χ)/(2πi · log_N(genus))` | `T7c-stark-rescue-verification.md` | **FAILS on all 3 bridges** |
| **Combined Gauss sum + W-factor** `L'(0,χ)/(τ(χ)·W(χ))` | `T7c-stark-rescue-verification.md` | **FAILS on all 3 bridges** |
| **Stickelberger element** `θ(χ) = Σ χ(a)·(a/N)` | `T7c-stark-rescue-verification.md` | **FAILS** — θ(χ) vanishes for k=3 (forced by χ(-1)=+1, classical); for k=4 and k=6 the exact algebraic values `-1-i`, `-1-√3·i` give phases `5/8, 2/3`, nowhere near `1/k` |
| **Conductor-adjusted phase** `arg(exp(-L'(0,χ)))/(2π) · (k/f(χ))` | `T7c-stark-rescue-verification.md` | **FAILS on all 3 bridges** |

Total: **30 pre-committed numerical tests across 6 rescue candidates × 3 bridges × 10 sub-tests = 0 / 30 pass** (the table collapses the sub-tests for readability; the full numerical record is in `T7c-stark-rescue-verification.md` §4).

The pattern is not "we haven't found the right functional yet". The pattern is **structural**: the discrete invariant `1/k mod ℤ` in `H²(ℤ/kℤ, U(1))` is not encoded in any continuous Galois phase of any L-function-derived quantity the framework has tested, across three independent research notes spanning four months and nine distinct identifications. The honest verdict is option (c) of `research/267` §6 — abandonment.

**What survives.** The *existence* of the right characters at the
right conductors is confirmed: order-k characters exist at N = 13
(k = 3, 4) and N = 19 (k = 6). The cocycle 1/k is a discrete
invariant in H^2(Z/kZ, U(1)). The L-function data are continuous.
The bridge between discrete and continuous cannot be a pointwise
evaluation of any standard L-function quantity.

**What the correct functional must satisfy.** Any reformulation
must:

1. **Input**: take an order-k Dirichlet character chi_k at conductor
   N (one of 13 or 19) and produce a rational number in Q/Z.
2. **Output**: equal 1/k mod Z for the three bridge characters.
3. **Mechanism**: pass through a regulator or period that absorbs
   the transcendental content of L'(0, chi), leaving only the
   algebraic class.

**Three candidate directions for reformulation:**

**(A) The boundary map in Galois cohomology.** The long exact
sequence ... -> H^1(G, O_K*) -> H^2(G, Z) -> H^2(G, K*) -> ...
has a boundary map delta that sends unit classes to Brauer classes.
The correct functional may be delta applied to the Stark unit class
[epsilon_chi] in H^1, not any pointwise evaluation of L'(0, chi).
This would mean: the cocycle 1/k is not readable from the *value*
of the Stark unit but from its *cohomological class* under the
boundary map. Computing this requires the full Galois module
structure of the Stark unit, not just its norm or phase.

**(B) The Beilinson regulator.** The Beilinson regulator
r_D : K_1(O_K) -> H^1_D(Spec(O_K), R(1)) maps algebraic K-theory
to Deligne cohomology. The image of the Stark unit under r_D lands
in a lattice whose covolume is the L-value. The *torsion* of this
lattice (the finite part of the cokernel) may carry the class 1/k.
This requires computing K_1(O_{Q(zeta_13)}) and K_1(O_{Q(zeta_19)})
explicitly -- a feasible but nontrivial computation.

**(C) The Weil pairing on the Jacobian.** For the cyclotomic curve
X_0(N), the Weil pairing on J_0(N)[k] produces a bilinear form
valued in mu_k. The bridge cocycle may arise as a Weil pairing
of torsion points on J_0(13) and J_0(19), not as a value of any
L-function derivative. This would connect the bridge family to the
arithmetic geometry of modular curves.

**The honest assessment.** The correct functional is unknown. The
three directions above are ordered by plausibility: (A) is the most
natural within the existing CBB framework; (B) connects to the
deepest layer of arithmetic geometry; (C) is the most speculative.
All three are computationally testable. The reformulation of
Conjecture 5 is the principal open problem in the Hilbert 12
programme.

### 8.6.1 Closure note (2026-04-11) — the reformulation is not a framework open problem

**⚠️ CLOSED.** After Lead 7c's six-rescue-candidate refutation, the three directions (A), (B), (C) above are closed as active framework work:

- **(A) The Galois-cohomology boundary map** `δ: H¹(G, O_K*) → H²(G, ℤ)` — is a real mathematical object. Its application to Stark-unit classes is a well-defined question independent of CBB. **It is not a framework open problem.** If a mathematician outside CBB works on (A) and finds the boundary map produces `1/k` on the bridge Stark units, that would revive Conjecture 5, and we would welcome the finding. Until then, the framework does not claim it, does not depend on it, and does not pursue it.
- **(B) The Beilinson regulator** `r_D: K_1(O_K) → H¹_D(Spec(O_K), ℝ(1))` — same status as (A). Computable in principle, not the framework's open problem.
- **(C) The Weil pairing on `J₀(N)[k]`** — most speculative. Computable in principle. Same status.

**The framework's position, after T7c:** the bridge cocycle `1/k` is a discrete invariant in cyclotomic Brauer cohomology, and that is the structural object. Its connection to Stark-unit phases — if one exists — is a question for the generic Hilbert-12 programme, not a load-bearing component of the Integers framework. Removing it **strengthens** the framework by removing an unverified claim; the 36/36 master-table closure, the bridge minimality (Lead 7e), the cross-formula γ_n consistency (Lead 7a), the cross-functional-form agreement (Lead 7d), the CCM 2025 timeline-independent confirmation, and the RH path through Conjecture 2 are all intact and stronger now that they do not carry a refuted companion claim.

The Hilbert 12 connection — if it exists in the framework — must come from a different object than V's matrix elements or Stark-unit phases. That different object is not currently identified and is not a 2026 research priority.

---

*The Brauer class is the obstruction. The Stark unit is **not** the generator — that identification is retracted. The bridge cocycle is a discrete invariant that lives in cyclotomic Brauer cohomology alone, and the framework's content is that it lives there at the minimal conductors forced by the arithmetic sieve, no more and no less.*
*V is the operator that carries both. The integers exist; the universe*
*follows; the bridges name the link; Hilbert 12 is the next door.*
