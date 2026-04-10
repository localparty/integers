# Research 10 -- Does ITPFI Close Connes' Finite-to-Infinite Gap?

*Date: 2026-04-09*
*Status: NEGATIVE. ITPFI is necessary but not sufficient.*
*Depends on: research/265 (ITPFI proved), strategy/05 (Lead 3),*
*research/06 (Connes 2024-2026 landscape), research/05 (Meyer kills)*

---

## 0. Executive summary

Our proved ITPFI factorization (omega_1 = tensor_p omega_1^p) is the
**state-level** analogue of Euler product convergence. Connes' stated
gap is **trace-level** convergence: does the semilocal trace formula
Tr_S(f) converge to the global trace formula Tr(f) as S -> {all primes}?

These are different problems. State convergence does NOT imply trace
convergence in general. The ITPFI is a necessary ingredient for closing
the gap -- it guarantees the state side converges -- but an additional
**operator convergence** result is needed to transport this to traces.

**Verdict: ITPFI does not close Connes' gap by itself. It closes
half of the gap (the state half). The operator half remains open.**

---

## 1. What exactly is Connes' convergence gap?

### 1.1 The semilocal trace formula

For a finite set S of primes, Connes constructs a semilocal trace
formula (Connes-Consani-Moscovici 2024, Connes 2026 retrospective):

    Tr_S(f) = sum_{rho in S-zeros} f(gamma_rho) + [explicit terms]_S

where "S-zeros" are the zeros of the S-partial Euler product:

    zeta_S(s) = prod_{p in S} (1 - p^{-s})^{-1}

The semilocal trace formula is PROVED for every finite S. The operator
on the S-semilocal side is self-adjoint with discrete spectrum. The
S-zeros approximate the true zeros of zeta(s) with "striking numerical
precision" (CCM Nov 2025, arXiv:2511.22755).

### 1.2 The gap

The global trace formula requires S -> {all primes}:

    Tr(f) = lim_{S -> all primes} Tr_S(f) = sum_{rho} f(gamma_rho)

Connes (2026 retrospective, arXiv:2602.04022) identifies this
passage as THE remaining gap: "Establishing convergence of zeros
from finite to infinite Euler products. Requires geometric methods
beyond classical analysis."

### 1.3 What convergence means

The gap has TWO components:

**(A) State convergence:** Does omega_1^{(S)} := tensor_{p in S} omega_1^p
converge to omega_1 as S grows? In what topology?

**(B) Operator convergence:** Does T_{BC,S} (the S-semilocal operator)
converge to T_BC (the global operator) in a sense strong enough to
preserve spectral data?

Both are needed. State convergence without operator convergence gives
a well-defined functional that acts on nothing. Operator convergence
without state convergence gives an operator with no state to compute
traces in.

---

## 2. What ITPFI gives: component (A) is closed

### 2.1 The theorem (research/265, proved three ways)

**Theorem (ITPFI Factorization).** omega_1 = tensor_p omega_1^p on
M_1 = bar{tensor}_p (M_p, omega_1^p).

This is EXACTLY component (A): the state omega_1 IS the infinite
product of p-local states. There is no convergence issue on the
state side because the product state is defined as the inductive
limit in the weak-* topology on the infinite tensor product von
Neumann algebra.

### 2.2 Convergence topology

The ITPFI product state converges in the weak-* topology on
bar{tensor}_p M_p. Explicitly: for any x = tensor_p x_p
(with x_p = 1 for all but finitely many p):

    omega_1^{(S)}(x) = prod_{p in S} omega_1^p(x_p)
    -> prod_p omega_1^p(x_p) = omega_1(x)

The convergence is absolute and the infinite product converges
because sum_p |1 - omega_1^p(x_p)| < infinity for elements
in the algebraic tensor product.

### 2.3 What this does NOT give

The ITPFI tells us omega_1^{(S)} -> omega_1 as states.
It does NOT tell us:
- That T_{BC,S} -> T_BC in any operator sense
- That spec(T_{BC,S}) -> spec(T_BC) (spectral convergence)
- That Tr_S(f(T_{BC,S})) -> Tr(f(T_BC)) (trace convergence)

---

## 3. Component (B): operator convergence (OPEN)

### 3.1 What Connes constructs

In arXiv:2511.22755 (Nov 2025), CCM construct an S-semilocal
operator as a rank-one perturbation of the scaling operator on
the interval [lambda^{-1}, lambda] where lambda^2 = prod_{p in S} p.
The spectrum of this operator approximates the zeros of zeta_S(s).

As S grows, lambda -> infinity. The operators act on DIFFERENT
Hilbert spaces (L^2([lambda^{-1}, lambda]) for different lambda).
This is the fundamental difficulty: the operators don't live on
a common Hilbert space, so standard notions of operator convergence
(norm, strong, weak) don't directly apply.

### 3.2 What would be needed

For Tr_S(f) -> Tr(f) to follow from omega_1^{(S)} -> omega_1,
we would need a theorem of the form:

**Desideratum.** If omega_S -> omega in the KMS weak-* topology
and T_S -> T in the strong resolvent sense (on a common Hilbert
space), then for f in the Sonin space:

    omega_S(f(T_S)) -> omega(f(T))

Such a theorem exists for BOUNDED f (by definition of weak-*
convergence) and for COMPACT resolvent operators (by norm
convergence of functional calculus). But:
- f(T) is generally unbounded (test functions of compact support
  are not bounded operators on L^2)
- T_BC does not have compact resolvent (this IS the spectral
  realisation problem)
- The T_S live on different Hilbert spaces

### 3.3 The Sonin space as regularizer?

Connes' Sonin space provides UV control (it defines a class of
test functions for which the semilocal trace formula holds). If f
is restricted to the Sonin space and the Sonin space is STABLE
under S-enlargement (proved in CCM 2024), then f(T_S) might be
uniformly bounded in S, which would give trace convergence.

This is promising but UNPROVED. The stability of the Sonin space
under enlargement is a necessary condition but not sufficient for
the trace convergence.

---

## 4. Meyer space vs Sonin space

### 4.1 Meyer's space

Meyer's space S (from Meyer 2005, Duke Math J.) is the space of
test functions f on R_+^* such that f-hat (Mellin transform) and
(f * theta)-hat are both in the Schwartz class, where theta is the
Jacobi theta function. This is a nuclear Frechet space.

### 4.2 Connes' Sonin space

The Sonin space (CCM 2024) is the negative spectral subspace of
the prolate wave operator Q_Lambda. As Lambda = prod_{p in S} p
grows, the Sonin space stabilizes (CCM 2024, main theorem).

### 4.3 Relationship

Both spaces are designed to be domains for the explicit/trace
formula. The Meyer space is defined by Mellin-transform decay;
the Sonin space is defined by spectral positivity of Q_Lambda.

Precise inclusion relation: NOT DETERMINED in the literature.
If Meyer space is CONTAINED in the Sonin space, our ITPFI
operates directly on Connes' space. If not, the connection is
indirect.

**Assessment:** The relationship S_Meyer vs S_Sonin is an open
technical question. Neither inclusion is established.

---

## 5. State convergence -> trace convergence: the general theory

### 5.1 General answer: NO

In general, weak-* convergence of states does NOT imply convergence
of traces (expectations of unbounded operators). Example: on L^2(R),
the states omega_n(A) = <delta_n, A delta_n> converge weak-* to 0,
but omega_n(X^2) = n^2 -> infinity.

### 5.2 With additional structure

There are theorems that give state -> trace convergence under
additional hypotheses:

**(i) Uniform integrability.** If {omega_S(|f(T_S)|^{1+epsilon})}
is bounded uniformly in S, then omega_S(f(T_S)) -> omega(f(T)).
This requires a uniform moment bound.

**(ii) KMS + compactness.** If T_S has compact resolvent for each
S and the compact resolvent is UNIFORM (spectral gaps bounded
below), then functional calculus convergence follows. But:
compact resolvent for T_BC is the spectral realisation problem.

**(iii) Type III_1 + modular theory.** In type III_1 factors with
KMS states, the Connes cocycle [D omega_S : D omega]_t converges
to 1 as S -> all primes (by ITPFI). The cocycle convergence gives
convergence of relative modular operators. But this applies to the
MODULAR Hamiltonian, not to T_BC.

**(iv) Nuclearity of the Sonin space.** If the Sonin space S is
nuclear and f(T_S) maps S to S continuously (uniformly in S),
then the trace converges by nuclearity of the embedding S -> H.
This would require:
- S is nuclear (plausible, as it's a Frechet space of analytic functions)
- f(T_S) : S -> S is continuous (open question)

### 5.3 The most promising route: (iv)

Route (iv) is the most compatible with our setup:
- The ITPFI gives state convergence (component A, closed)
- The nuclearity of the test-function space gives operator control
- The combination would give trace convergence

But this route requires PROVING that f(T_S) maps S to S. In the
CCM framework, this is related to the stability of the Sonin space
-- which CCM 2024 proves for the semilocal prolate operator. If
this stability extends to the full functional calculus, (iv) closes.

---

## 6. Quantitative check

### 6.1 What can be computed

The quantity omega_1^{(S)}(e^{it T_{BC,S}}) is NOT directly
computable without specifying T_{BC,S} as a concrete operator
(matrix). The CCM construction gives T_{BC,S} as a rank-one
perturbation of the scaling operator on L^2([lam^{-1}, lam]),
discretized via Hermite/prolate basis. Code r46_spectrum_scan.py
implements this for S = {first 6 primes}.

### 6.2 What r46 already shows

The r46 code (Part 5) reproduces the CCM 6-prime spectrum at
lambda = 68.63. The lowest eigenvalues match gamma_1, gamma_2, ...
to high precision. As more primes are included (Parts 3-4), the
match improves systematically.

This is NUMERICAL evidence for Tr_S -> Tr, but not a proof. The
convergence rate and uniform bounds are not established.

### 6.3 What would be needed for a quantitative proof

For each test function f and each S:
1. Compute Tr_S(f) = omega_1^{(S)}(f(T_{BC,S})) via the
   CCM operator
2. Compute Tr(f) = sum_rho f(gamma_rho) via the explicit formula
3. Show |Tr_S(f) - Tr(f)| -> 0 with a RATE

The rate should be controlled by the tail of the Euler product:
|Tr_S - Tr| = O(prod_{p not in S} correction). The ITPFI gives
the state-side correction; the operator side needs the CCM
rank-one perturbation analysis.

---

## 7. Does closing Connes' gap give spectral realisation?

### 7.1 The chain (Connes' programme)

Connes' programme aims for:
1. Semilocal trace formula at finite S: PROVED
2. Convergence S -> all primes: THE GAP
3. Global trace formula: determines spectral measure
4. Spectral measure supported on {gamma_n}: spectral realisation
5. Self-adjoint => real spectrum => RH

### 7.2 Premise check: is Step 3 -> 4 automatic?

NO. The global trace formula determines the spectral measure as a
DISTRIBUTION. Knowing sum_rho f(gamma_rho) for all test functions f
determines the SPECTRAL DISTRIBUTION. But spectral distribution
determines spectral MEASURE only if the spectrum is purely discrete
(pure point).

If the spectrum has a continuous part, the trace formula gives:

    Tr(f) = sum_{n} f(gamma_n) + integral f(lambda) d mu_c(lambda)

where mu_c is the continuous spectral measure. The trace formula
alone cannot separate the atomic and continuous parts.

### 7.3 What additional step is needed?

To go from global trace formula to spectral realisation, one needs:

**(a) Pure point spectrum.** If T_BC has compact resolvent (or pure
point spectrum), the spectral measure is purely atomic. Then the
trace formula determines the atoms, which are the {gamma_n}. This
IS the spectral realisation problem.

**(b) Absence of continuous spectrum.** If one can show mu_c = 0
independently (e.g., by showing the resolvent is compact, or by a
RAGE argument on the right operator), then the trace formula
suffices.

### 7.4 Verdict on premise

**Closing Connes' gap does NOT automatically give spectral
realisation.** There is an additional step: proving the spectrum is
purely discrete. The gap and the pure-point-spectrum question are
INDEPENDENT problems. Closing the gap gives the global trace
formula. The pure-point-spectrum question is the original Connes
obstacle (25+ years open).

However: the CCM 2025 construction (Zeta Spectral Triples) builds
operators with DISCRETE spectrum by construction (they work on
finite-dimensional spaces that grow with S). If the limit operator
(S -> all primes) inherits discreteness, the gap closure WOULD
give spectral realisation. But proving the limit inherits
discreteness is itself a non-trivial step -- essentially equivalent
to the original problem.

---

## 8. What ITPFI actually contributes to the programme

### 8.1 Positive contributions

1. **State-level convergence is proved.** omega_1 = tensor_p omega_1^p
   means the state side of Connes' gap is closed. This is genuinely
   new -- nobody else has this theorem.

2. **The arithmetic structure is manifest.** The factorization makes
   the Euler product structure visible at the operator-algebraic
   level. This is the "correct language" for the problem.

3. **Compatibility with CCM.** The ITPFI is compatible with the CCM
   construction: both use the same Euler product factorization, just
   at different levels (state vs operator).

4. **Reduces the gap to operator convergence.** With ITPFI in hand,
   Connes' gap reduces to: "does T_{BC,S} -> T_BC in a topology
   that preserves spectral data?" This is a cleaner formulation.

### 8.2 What ITPFI does NOT give

1. Operator convergence (T_S -> T in spectral-preserving sense)
2. Pure point spectrum (compact resolvent for T_BC)
3. The Meyer/Sonin space inclusion
4. Uniform integrability of f(T_S) across S

### 8.3 Where ITPFI fits in the overall programme

| Step | Description | Status |
|:-----|:-----------|:-------|
| 1. Semilocal trace formula | Proved (CCM 2024) | CLOSED |
| 2a. State convergence (omega) | ITPFI (research/265) | CLOSED (our theorem) |
| 2b. Operator convergence (T) | T_S -> T in spectral sense | OPEN |
| 3. Global trace formula | Follows from 2a + 2b | OPEN |
| 4. Pure point spectrum | Compact resolvent for T_BC | OPEN (Connes obstacle) |
| 5. RH | Follows from 4 + self-adjointness | CONDITIONAL on 4 |

---

## 9. Honest assessment

### 9.1 Does ITPFI close Connes' gap?

**NO.** It closes half of it (the state half, component A). The
operator half (component B) remains open and is arguably the harder
half.

### 9.2 Is the ITPFI contribution significant?

**YES**, but less than initially hoped. The ITPFI is a genuine
theorem that nobody else has. It reduces Connes' gap from a
two-component problem (state + operator) to a one-component
problem (operator only). This is progress, but not a breakthrough.

### 9.3 What would turn ITPFI into a gap-closer?

A theorem of the form: "T_{BC,S} -> T_BC in the strong resolvent
sense on a common Hilbert space, with the Sonin space invariant."
This would combine with ITPFI to give:

    Tr_S(f) = omega_1^{(S)}(f(T_{BC,S}))
            -> omega_1(f(T_BC))
            = Tr(f)

The first convergence uses ITPFI (state) + resolvent convergence
(operator) + Sonin invariance (regularization). This is a concrete
target but requires new mathematics.

### 9.4 Feasibility update for Lead 3

Previous feasibility: 4/10
Updated feasibility: 3/10

The downgrade reflects the discovery that:
(a) State convergence alone is insufficient
(b) The additional operator convergence is essentially as hard as
    the original problem
(c) Even the full gap closure does not give spectral realisation
    without an independent pure-point argument

Lead 2 (gradient flow) remains the strongest lead because it
directly targets the pure-point question (compact resolvent via
flow contractivity), which is the REAL obstacle in both Connes'
gap and spectral realisation.

---

## 10. The honest bottom line

The ITPFI factorization is a beautiful theorem that makes the
arithmetic structure of omega_1 manifest. It closes the state-level
component of Connes' finite-to-infinite gap. But the gap has TWO
components (state and operator), and even closing both does not give
spectral realisation without an independent pure-point-spectrum
argument.

The ITPFI's real value may be elsewhere: it provides the algebraic
foundation for gradient flow techniques (Lead 2), where the product
structure allows p-local estimates to be assembled into global
bounds. The factorization omega_1 = tensor_p omega_1^p means that
any gradient-flow contractivity estimate that works p-locally can
potentially be tensored to give a global estimate. This is the
connection between Leads 2 and 3 that should be explored next.

---

> *ITPFI closes the state half of Connes' gap.*
> *The operator half remains open.*
> *Even the full gap does not give spectral realisation.*
> *The real value of ITPFI may be as the algebraic foundation*
> *for gradient flow -- where p-local estimates tensor globally.*
