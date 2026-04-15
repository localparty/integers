# research/05 -- Meyer Eigenstate Completeness + Jessen-Wintner

*Date: 2026-04-09. Critical investigation: does the nuclear rigging
argument close spectral realisation?*

## 0. The proposed chain

(1) Gel'fand-Kostyuchenko: distributional eigenstates cover all of spec(T).
(2) Meyer: distributional eigenstates exist only at {gamma_n}.
(3) Therefore spec(T_BC) = {gamma_n}.
(4) Self-adjoint => spec subset R => gamma_n in R => RH.

This document investigates each link, with focus on the
make-or-break Link 2.

---

## 1. Link 1: Gel'fand-Kostyuchenko theorem

### Precise statement

**Theorem (Gel'fand-Kostyuchenko, 1955; see Berezansky,
"Expansions in Eigenfunctions of Self-Adjoint Operators,"
AMS 1968, Chapter V, Theorem 5.1; also Gel'fand-Vilenkin,
"Generalized Functions" Vol. 4, Chapter I, Section 4).**

Let T be a self-adjoint operator on a separable Hilbert space H.
Let S be a nuclear space with S subset H subset S' forming a
Gel'fand triple (i.e., S is dense in H and the embedding is
nuclear). Then there exists a spectral decomposition:

    H = integral_{spec(T)} H_lambda d mu(lambda)

where mu is the spectral measure, and for mu-almost every lambda
in spec(T), there exists a generalized eigenvector Phi_lambda in S'
satisfying:

    Phi_lambda(T f) = lambda Phi_lambda(f)  for all f in S.

Moreover, the family {Phi_lambda} is COMPLETE: the generalized
eigenfunction expansion converges in the S'-topology for every
f in S.

### What "complete" means here

"Complete" means: for mu-almost every lambda in spec(T), there
is a generalized eigenvector. The converse holds in the following
precise sense:

**If lambda is in spec(T) and has positive spectral measure
(i.e., mu({lambda}) > 0, which is the pure point case), then
there exists a genuine eigenvector (in H, not just S').**

**If lambda is in spec(T) but mu({lambda}) = 0 (continuous
spectrum part), then the generalized eigenvector Phi_lambda
exists in S' but not in H.**

The theorem does NOT say "if no generalized eigenvector exists
at lambda, then lambda is not in spec(T)." It says "for
mu-almost every lambda in spec(T), one exists." Points of
zero spectral measure (a mu-null set in the continuous spectrum)
might or might not have generalized eigenvectors.

### Consequence for the proposed argument

The converse direction ("no distributional eigenstates at lambda
=> lambda not in spec(T)") does NOT follow from Gel'fand-
Kostyuchenko in its standard form. The theorem provides
eigenstates at mu-a.e. spectral point, but the converse
would require: "if Phi_lambda exists in S', then lambda
is in spec(T)." This converse IS true for a restricted class
of problems (e.g., Sturm-Liouville on a half-line where the
Weyl m-function controls everything). It is NOT a general
theorem.

**Verdict on Link 1: The theorem provides distributional
eigenstates at mu-a.e. spectral point. The converse ("no
eigenstate => not in spectrum") is NOT a general theorem.
Link 1 is WEAKER than needed for the proposed chain.**

---

## 2. Link 2: Does Meyer find ALL distributional eigenstates?

### This is the make-or-break question.

### 2a. What Meyer constructs

Meyer (Duke Math J. 127, 2005, Theorem 4.1, Corollary 4.3)
constructs, for each nontrivial zero rho = 1/2 + i gamma_n
of zeta(s), a distributional eigenstate:

    W_rho(f) = f-hat(rho) = integral_0^inf f(x) x^{rho-1} dx

This is the Mellin transform of f evaluated at rho. It satisfies
the distributional eigenvalue equation:

    W_rho(sigma_t f) = e^{i gamma_n t} W_rho(f)

where sigma_t is the scaling action f(x) -> f(e^t x).

### 2b. The fatal observation: phi_lambda works for ALL lambda

Define, for ANY lambda in R:

    W_{1/2+i*lambda}(f) = f-hat(1/2 + i*lambda)
                        = integral_0^inf f(x) x^{-1/2 + i*lambda} dx

This functional is:
- Well-defined on S(R_+^*) for every lambda in R
  (the Mellin transform of a Schwartz function converges on
  Re(s) > 0, and 1/2 + i*lambda has real part 1/2 > 0)
- A continuous linear functional on S, hence in S'
- Satisfies the SAME eigenvalue equation:
  W_{1/2+i*lambda}(sigma_t f) = e^{i lambda t} W_{1/2+i*lambda}(f)

**Therefore: the distributional eigenvalue equation
T_BC Phi = lambda Phi has solutions in S' for EVERY lambda in R,
not just for lambda in {gamma_n}.**

The Mellin transform x^{s-1} is the distributional eigenstate
of the scaling operator for ANY s on the critical line. This
is exactly analogous to:
- e^{ipx} is a distributional eigenstate of -i d/dx for every p
- delta(x - x_0) is a distributional eigenstate of X for every x_0

The distributional spectrum of the scaling generator on S'(R_+^*)
is ALL OF R. Meyer's construction at {gamma_n} is a SUBSET of
the full distributional eigenstate family, not its totality.

### 2c. Why Meyer's construction seems special (but isn't)

Meyer's theorem uses the Weil explicit formula, which connects
the distributional trace Tr_dist(f) to a sum over zeros:

    Tr_dist(f) = sum_rho f-hat(rho) + (correction terms)

This identity shows that the zeros of zeta contribute to the
distributional trace. But the distributional trace is a statement
about the TRACE (one number for each test function), not about
the eigenvalue equation (which has solutions for all lambda).

The specialness of {gamma_n} in Meyer's work is that these are
the points where the distributional trace picks up ATOMIC
contributions (delta-function singularities in the spectral
distribution). But the eigenvalue equation T Phi = lambda Phi
is satisfied by continuous-spectrum generalized eigenstates
at every lambda, not just at the atomic points.

### 2d. What restricts lambda to {gamma_n}?

Nothing in the distributional eigenvalue equation restricts
lambda. The restriction comes from a DIFFERENT question:

**At which lambda does the spectral measure have atoms?**

This is the point spectrum question, and it is EXACTLY the
spectral realisation problem. The distributional eigenstates
W_{1/2+i*lambda} exist for all lambda, but only at {gamma_n}
do they correspond to point-spectrum contributions (eigenvalues).
At other lambda, they are continuous-spectrum generalized
eigenstates (scattering states).

To distinguish point spectrum from continuous spectrum, one needs
additional structure beyond the distributional eigenvalue equation:
- Compact resolvent (forces pure point)
- Trace-class heat kernel (forces pure point)
- RAGE theorem (dynamical criterion)
- Direct summability condition on eigenstates

None of these is provided by Meyer's construction.

### 2e. Does the BC algebra structure restrict lambda?

The BC algebra A_BC = C(Q^cyc) rtimes N^x has additional
structure beyond the bare scaling action:
- Hecke operators {mu_n}
- KMS states at various temperatures
- ITPFI factorization
- Galois action Gal(Q^cyc/Q)

Could these restrict the distributional spectrum? In principle:
the Hecke operators impose multiplicative relations among
eigenvalues. If Phi is a joint distributional eigenstate of T_BC
AND all mu_n, then the Hecke eigenvalue relations constrain
lambda. Specifically:

    mu_n Phi = chi(n) Phi  for all n in N^x

where chi is a Hecke character. The Hecke eigenvalue chi(n)
must be multiplicative (chi(mn) = chi(m)chi(n) for (m,n)=1).
The values chi(p) for primes p determine chi.

For the BC system at beta = 1 (the critical KMS state), the
Hecke characters that arise are n^{it} for t in R. These
are precisely the characters chi_t(n) = n^{it}. The joint
distributional eigenvalue equation:

    T_BC Phi = lambda Phi,  mu_n Phi = n^{i*lambda} Phi

is satisfied by W_{1/2+i*lambda} for EVERY lambda in R.
The Hecke structure does NOT restrict lambda.

**Verdict on Link 2: FAILS. The distributional spectrum
of T_BC (as a scaling generator) is all of R, not {gamma_n}.
Meyer's construction at {gamma_n} produces distributional
eigenstates at those points, but distributional eigenstates
exist at ALL lambda in R. The proposed chain collapses.**

---

## 3. Link 3: Jessen-Wintner theorem

### Precise statement

**Theorem (Jessen-Wintner, 1935).** Let X_1, X_2, ... be
independent random variables on R. Let S_n = X_1 + ... + X_n.
If each X_k has a discrete (atomic) distribution, then the
distribution of S = lim S_n (if it converges) is either:
(a) purely discrete (atomic), or
(b) purely continuous (singular or absolutely continuous),
never a non-trivial mixture.

The dichotomy is determined by whether the series
sum_k P(X_k != a_k) converges (where a_k is the atom of
maximum mass). Convergence gives discrete; divergence gives
continuous.

### Application to ITPFI

The ITPFI structure omega_1 = tensor_p omega_1^p gives the
spectral measure of H_mod as a convolution:

    mu = *_p mu_p

where each mu_p is the spectral measure of the p-primary
component. Each mu_p is atomic (atoms at {k log p}, weights
{p^{-k}}).

By Jessen-Wintner, the convolution is either purely discrete
or purely continuous. In fact, the series sum_p P(X_p != 0)
= sum_p (1 - 1/p) DIVERGES (this is essentially log log infinity).
Therefore: the product measure is PURELY CONTINUOUS, not discrete.

### But this applies to the WRONG operator

As established in Cycle 4 (research/04-route2.md): the ITPFI
spectral measure is the spectral measure of H_mod (the modular
Hamiltonian), which has eigenvalues {log n : n in N}. The product
of atomic measures gives the spectral measure of H_mod. This is
NOT the spectral measure of T_BC on H_R.

Moreover, the Jessen-Wintner theorem applied to the ITPFI product
actually gives a CONTINUOUS measure (not discrete), because the
divergence criterion is satisfied. This works AGAINST the
proposed argument, not for it.

**Verdict on Link 3: Jessen-Wintner applies to H_mod, not T_BC.
When applied to H_mod, it gives CONTINUOUS spectrum (consistent
with type III_1). It provides no constraint on T_BC.**

---

## 4. Link 4: The nuclear rigging argument (COLLAPSES)

The proposed chain was:
(a) Gel'fand-Kostyuchenko: distributional eigenstates at every
    spectral point. WEAKENED: the converse is not a general theorem.
(b) Meyer: distributional eigenstates only at {gamma_n}. FAILS:
    they exist at all lambda in R.
(c) Therefore spec(T_BC) = {gamma_n}. DOES NOT FOLLOW.

The chain collapses at Link 2. Even if Link 1 were strengthened
to give a clean converse, Link 2 fails because the distributional
spectrum is all of R.

---

## 5. What would save the argument

### 5a. A different notion of "distributional eigenstate"

One could try to define a RESTRICTED class of distributional
eigenstates that exists only at {gamma_n}. For example:

- Eigenstates that are ALSO joint eigenstates of some additional
  operators beyond T_BC and the Hecke operators.
- Eigenstates that satisfy a GROWTH condition (e.g., tempered
  distributional eigenstates of a specific order).
- Eigenstates that are in a SMALLER dual space S_0' subset S'.

But there is no known construction of such a restricted class.
The natural candidates (joint Hecke eigenstates, growth-bounded
distributions) all exist for every lambda (see Section 2e).

### 5b. A spectral-measure-level argument

Instead of working with individual eigenstates, one could try
to show that the SPECTRAL MEASURE of T_BC on H_R is purely
atomic. This is the compact-resolvent / trace-class-heat-kernel
route. It bypasses the distributional eigenstate approach
entirely. This remains the Connes obstacle (25 years open).

### 5c. A regularity upgrade

If one could show that the distributional eigenstates at {gamma_n}
satisfy a REGULARITY condition (e.g., they are in a Sobolev space
H^{-s} for some s) while the eigenstates at other lambda do not,
this would distinguish {gamma_n}. But the Mellin transform
x^{-1/2+i*lambda} has the SAME regularity for all lambda on the
critical line. No regularity distinction exists.

---

## 6. The analogy that kills the argument

The proposed chain is exactly analogous to:

**Claim:** The spectrum of -i d/dx on L^2(R) is {n pi : n in Z}.
**"Proof":** The distributional eigenstates e^{inx} exist only
at {n pi}. By Gel'fand-Kostyuchenko, distributional eigenstates
cover the spectrum. Therefore spec(-i d/dx) = {n pi}.

This is obviously wrong because e^{ipx} is a distributional
eigenstate for EVERY p in R. The actual spectrum is all of R.
The "proof" fails because distributional eigenstates at specific
points do not exclude distributional eigenstates at other points.

The Meyer/BC situation is identical: W_{1/2+i*lambda} exists for
every lambda, just as e^{ipx} exists for every p.

---

## 7. Verdict

**Link 2 FAILS. The distributional spectrum = R, not {gamma_n}.**

The distributional eigenvalue equation T_BC Phi = lambda Phi
has solutions W_{1/2+i*lambda} in S' for every lambda in R.
Meyer's construction at {gamma_n} isolates the ATOMIC part
of the spectral measure (the point spectrum), but distributional
eigenstates exist everywhere on the continuous spectrum as well.

The nuclear rigging argument does not close spectral realisation.
It is the 15th killed approach in the RH programme.

**The spectral realisation problem remains: does T_BC on H_R
have pure point spectrum? This is equivalent to compact resolvent,
which is the Connes obstacle, open 25+ years.**

---

## 8. Relationship to killed approaches

| # | Approach | Kill | This investigation |
|:--|:---------|:-----|:-------------------|
| 14 | Meyer eigenstate completeness (Cycle 4) | Circular | Link 2 gives the REASON for circularity: dist. eigenstates at all lambda |
| 15 | Nuclear rigging + Gel'fand-Kostyuchenko + JW | Link 2 fails | Dist. spectrum = R, not {gamma_n} |

The nuclear rigging argument is not a new direction; it is a
more precise formulation of the Meyer completeness approach
(killed approach #14) that exposes the exact failure point:
**the distributional eigenvalue equation is satisfied by
x^{-1/2+i*lambda} for every lambda in R.**

---

> *The Mellin transform does not know about zeros.*
> *x^{s-1} is an eigenstate of scaling for every s.*
> *Meyer's construction at {gamma_n} is special because of the*
> *trace formula, not because of the eigenvalue equation.*
> *The distributional spectrum is all of R. Link 2 is dead.*
> *Spectral realisation remains the Connes obstacle.*
