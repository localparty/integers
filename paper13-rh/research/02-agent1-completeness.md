# research/02 -- Agent 1: Completeness of Meyer's Eigenstates

*Date: 2026-04-10. Spectral Realisation Cycle 2.*

## 1. The question

Does Meyer 2005 produce a distributional eigenstate for EVERY zero
gamma_n, and do these eigenstates span a dense subspace of H_1?

## 2. Meyer 2005 — what it actually proves

**Reference:** R. Meyer, "On a representation of the idele class group
related to primes and zeros of L-functions," Duke Math. J. **127**
(2005), no. 3, 519--595.

### 2.1 Meyer's construction (Theorem 4.1, Corollary 4.3)

Meyer constructs a representation of the idele class group C_Q =
A_Q^x / Q^x on a nuclear Frechet space S(C_Q) of Schwartz-Bruhat
functions. The key results:

**(a) Theorem 4.1.** The distributional trace of the representation,
acting on S(C_Q), reproduces the Weil explicit formula:

    Tr_dist(f | S(C_Q)) = sum_rho f-hat(rho) + (smooth terms)

where the sum is over ALL non-trivial zeros rho of zeta(s), counted
with multiplicity.

**(b) Corollary 4.3.** For each non-trivial zero rho = 1/2 + i*gamma_n,
there exists a distributional eigenstate phi_n in S'(C_Q) such that
the time evolution acts as:

    sigma_t(phi_n) = e^{i*gamma_n*t} * phi_n

This holds for EVERY non-trivial zero, not just finitely many.

### 2.2 Answer to question (a): ALL zeros

YES. Meyer's construction produces an eigenstate for every zero.
The distributional trace formula sums over ALL non-trivial zeros
rho (Theorem 4.1). Each zero contributes a distributional
eigenfunction (Corollary 4.3). There is no finite truncation.

### 2.3 Answer to question (b): Do {phi_n} span S?

This is where the gap lies. Meyer proves:

1. Each phi_n is in S'(C_Q) (the topological dual of the Schwartz
   space).
2. The distributional trace involves ALL phi_n.
3. S(C_Q) is a nuclear Frechet space, and the Gel'fand triple
   S(C_Q) subset H_1 subset S'(C_Q) gives S dense in H_1.

**BUT Meyer does NOT prove that {phi_n} span S or even a dense
subspace of S.** His theorem is about the TRACE (a single linear
functional on test functions), not about SPANNING.

### 2.4 The spanning gap

The difference is crucial:

- **Trace completeness:** For every test function f in S, the trace
  Tr(f) = sum_n f-hat(gamma_n) + (smooth). This determines the
  Fourier transform of f at the gamma_n, but a function is not
  determined by its values at a discrete set of points unless those
  points are dense (which {gamma_n} is NOT in R).

- **Eigenstate completeness:** {phi_n} span a dense subspace of H_1
  iff every vector in H_1 can be approximated by finite linear
  combinations of phi_n. This is a statement about the COMPLETENESS
  of the eigenfunction system, not just the trace.

For a self-adjoint operator with pure point spectrum, the
eigenstates automatically form a complete orthonormal system.
But we are trying to PROVE pure point spectrum, not assume it.

## 3. The Gel'fand triple argument (attempted)

### 3.1 Setup

The Gel'fand triple is S subset H_1 subset S'. If {phi_n} span S
(in the Frechet topology), then they automatically span a dense
subspace of H_1 (since S is dense in H_1).

### 3.2 Does the nuclear spectral theorem help?

The nuclear spectral theorem (Gel'fand-Vilenkin) says: for a
self-adjoint operator A on H with a nuclear rigging S subset H
subset S', there exists a COMPLETE system of generalised
eigenfunctions {phi_lambda} in S' that diagonalises A.

**Key:** The theorem guarantees completeness of the generalised
eigenfunctions. But it applies to the FULL spectral decomposition,
including any continuous spectrum. If A has continuous spectrum, the
generalised eigenfunctions include non-normalisable ones
(scattering states).

### 3.3 The distinction

- If T_BC has pure point spectrum: the nuclear spectral theorem
  gives {phi_n}_{n=1}^infty as a complete system in S', and
  these are exactly Meyer's eigenstates. Completeness is automatic.

- If T_BC has continuous spectrum alongside {gamma_n}: the nuclear
  spectral theorem gives {phi_n} PLUS additional generalised
  eigenfunctions from the continuous part. Meyer's {phi_n} would
  NOT be complete.

**This is circular:** completeness of Meyer's eigenstates is
equivalent to pure point spectrum, which is equivalent to spectral
realisation, which is equivalent to RH.

## 4. What WOULD close the gap

### 4.1 Route 1: Prove T_BC has compact resolvent

If (T_BC - z)^{-1} is compact for some z not in spec(T_BC), then
T_BC has purely discrete spectrum (all eigenvalues, no continuous
part). Meyer's eigenstates would then automatically be complete.

Status: Connes' programme has NOT proved compact resolvent for T_BC
on the adele class space. The difficulty: the adele class space is
non-compact, and compact resolvent requires the operator to "see"
the compactness of the geometry.

### 4.2 Route 2: Prove trace-class heat kernel

If exp(-t*T_BC^2) is trace-class for some t > 0, the spectrum is
discrete. The theta-summability of T_BC (Connes 1999) suggests this
might hold, but it is not proved.

### 4.3 Route 3: Weyl law with error control

If the eigenvalue counting function of T_BC matches the
Riemann-von Mangoldt formula with error O(log T), and the total
spectral counting function (including continuous spectrum) must
also match, there is no room for macroscopic continuous spectrum.
But O(log T) extra eigenvalues could still hide (see Agent 4).

## 5. Premise check

**Does this argument distinguish spec = {gamma_n} from
spec = {gamma_n} ∪ {extra}?**

The completeness argument, IF it could be closed, would distinguish:
complete eigenstates mean no room for extra spectrum. But the
argument is circular at present: completeness = pure point spectrum
= spectral realisation = RH.

## 6. Verdict

**ANGLE 1 OUTCOME: Structural insight, but circular at the core.**

Meyer produces eigenstates for ALL zeros (not finitely many). The
Gel'fand triple S subset H_1 subset S' means S is dense in H_1.
But Meyer does NOT prove that {phi_n} span S. Proving that would
require showing T_BC has no continuous spectrum, which IS spectral
realisation.

The angle is not vacuous -- it correctly identifies the gap. But
it does not close it. The gap reduces to: does T_BC have compact
resolvent (or equivalently, trace-class heat kernel)?

**Status: OPEN. The right question, but no new progress.**
