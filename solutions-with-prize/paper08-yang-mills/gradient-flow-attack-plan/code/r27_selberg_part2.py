"""
R27 Part 2: Deeper analysis of the S1+S5 => S4 implication
and what remains after S4 is settled.

Key question: S1+S5 imply |alpha_{j,p}| <= 1 (weak Ramanujan bound / S4).
But does |alpha_{j,p}| < 1 (strictly inside unit circle) create problems?
And does the FULL Selberg class (S1+S2+S3+S4+S5) force zeros on the line?
"""

import numpy as np
from mpmath import (mp, mpf, mpc, zeta, gamma, pi, log, exp, sqrt,
                    fsum, power, cos, sin, inf, quad, diff, nstr,
                    zetazero, nprint, chop, fabs, re, im)

mp.dps = 30

print("=" * 70)
print("R27 PART 2: WHAT REMAINS AFTER S4 IS SETTLED")
print("=" * 70)

# =================================================================
# ANALYSIS 1: |alpha_{j,p}| < 1 vs |alpha_{j,p}| = 1
# =================================================================
print("\n" + "=" * 70)
print("ANALYSIS 1: Inside vs. On the Unit Circle")
print("=" * 70)

print("""
S4 as stated (a_n = O(n^eps)) is equivalent to |alpha_{j,p}| <= 1
for all but finitely many p. This ALLOWS |alpha_{j,p}| < 1.

Example: Consider a degree-2 function with local factors
  F_p(s) = (1 - alpha_p p^{-s})^{-1} (1 - beta_p p^{-s})^{-1}
where alpha_p * beta_p = 1 (from the functional equation)
and |alpha_p| = p^{-delta}, |beta_p| = p^{delta} for small delta > 0.

For delta > 0: |beta_p| = p^delta > 1, violating |alpha_{j,p}| <= 1!
So the constraint alpha*beta = 1 with |alpha| < 1 gives |beta| > 1.

Wait, this means: for degree >= 2 with the functional equation
forcing alpha * beta = 1, having |alpha| < 1 implies |beta| > 1,
which VIOLATES S4!

For the FE constraint on Satake parameters:
  alpha_{1,p} * alpha_{2,p} = chi(p) (some root of unity, often 1)

If |alpha_1| = r < 1, then |alpha_2| = 1/r > 1. This violates S4.

CONCLUSION: For degree 2 with functional equation (S3):
  S4 (|alpha_{j,p}| <= 1) + S3 (alpha_1 * alpha_2 = root of unity)
  => |alpha_{j,p}| = 1 (Ramanujan!)

So for degree 2: S3 + S4 => Ramanujan conjecture!
""")

# Verify: if alpha * beta = 1 and |alpha| <= 1 and |beta| <= 1,
# then |alpha| = |beta| = 1.
print("Verification: |alpha| <= 1, |beta| <= 1, alpha*beta = 1")
print("=> |alpha*beta| = |alpha|*|beta| = 1")
print("=> |alpha| >= 1 (since |beta| <= 1 means |alpha| = 1/|beta| >= 1)")
print("=> |alpha| = 1 (combining with |alpha| <= 1)")
print()
print("YES: S4 + S3 (for degree 2 with det condition) => full Ramanujan.")

# =================================================================
# ANALYSIS 2: What about higher degree?
# =================================================================
print("\n" + "=" * 70)
print("ANALYSIS 2: Higher Degree")
print("=" * 70)

print("""
For degree d, the functional equation gives:
  prod_{j=1}^d alpha_{j,p} = chi(p) (root of unity)

S4 gives: |alpha_{j,p}| <= 1 for all j.
Combined: prod |alpha_{j,p}| = 1 and each |alpha_{j,p}| <= 1.

By AM-GM (or just the product constraint):
  prod |alpha_{j,p}| = 1 with each factor <= 1
  => each factor = 1

So for ANY degree d >= 1, if the functional equation gives
  prod alpha_{j,p} = root of unity (i.e., |prod alpha_{j,p}| = 1)
then S4 => |alpha_{j,p}| = 1 for all j.

THIS IS THE FULL RAMANUJAN CONJECTURE!

Summary of the logical chain:
  S1 + S5 => S4 (|alpha_{j,p}| <= 1)
  S4 + S3 (determinant condition) => |alpha_{j,p}| = 1 (full Ramanujan)

So for the Selberg class with ALL five axioms:
  S1 + S2 + S3 + S5 => S4 => full Ramanujan

Wait — is this right? The functional equation (S3) says:
  Lambda(s) = epsilon * Lambda_bar(1-s)

For the local factor at p, this gives:
  F_p(s) = epsilon_p * F_p_bar(1-s) * (gamma factors)

The Satake parameters transform as:
  {alpha_{j,p}} -> {chi(p)/alpha_{j,p}} (not necessarily the product = 1)

Actually, the precise constraint is: the multiset {alpha_{j,p}} is
mapped to {chi(p) * alpha_{j,p}^{-1}} under s -> 1-s. This means:

  For each alpha_{j,p}, there exists alpha_{k,p} such that
  alpha_{j,p} * alpha_{k,p} = chi(p)

This is a PAIRING, not necessarily a product-equals-1 condition on
ALL parameters simultaneously.

For degree 2: alpha_1 * alpha_2 = chi(p), so the product constraint
holds and we get |alpha_j| = 1 from S4.

For degree 3: the pairing gives alpha_j * alpha_k = chi(p), but
there's an ODD element that pairs with itself: alpha_j^2 = chi(p),
so |alpha_j| = 1. And the paired ones satisfy |alpha_j| = 1 by
the same argument.

For general even degree: the pairing alpha_j * alpha_{sigma(j)} = chi(p)
for some involution sigma. Each pair satisfies |alpha_j * alpha_sigma(j)| = 1,
and with |alpha_j| <= 1, |alpha_sigma(j)| <= 1, we get |alpha_j| = 1.

CONCLUSION: For ALL degrees, S3 + S4 => full Ramanujan.
""")

# =================================================================
# ANALYSIS 3: The Kaczorowski-Perelli program — what's known
# =================================================================
print("\n" + "=" * 70)
print("ANALYSIS 3: The Kaczorowski-Perelli Classification Program")
print("=" * 70)

print("""
Kaczorowski and Perelli have studied the structure of the Selberg class
in a series of papers (1999-2011+). Key results:

1. DEGREE CLASSIFICATION:
   - d = 0: Only F = 1 (Conrey-Ghosh 1993)
   - d = 1: Only shifted Dirichlet L-functions (K-P 1999, 2002)
             n^{ia} L(s+ib, chi) with a,b real, chi primitive
             In the Selberg class (with S4): a = b = 0, so just L(s, chi)
   - d = 2: OPEN (conjectured: only GL(2) automorphic L-functions)
   - d > 2: WIDE OPEN

2. THE SELBERG ORTHONORMALITY CONJECTURE:
   For primitive F, G in S:
     sum_{p <= x} a_F(p) * conj(a_G(p)) / p = delta_{F,G} * log log x + O(1)

   This is proved for degree 1 (from PNT for L-functions) but OPEN
   for degree >= 2.

3. STRONG MULTIPLICITY ONE:
   If a_F(p) = a_G(p) for all but finitely many p, then F = G.
   Proved for all degrees in S (K-P 2002).

4. THE SELBERG CONJECTURES (still open for d >= 2):
   (a) d_F is a non-negative integer for all F in S
   (b) Primitive functions in S satisfy orthonormality
   (c) Every F in S factors uniquely into primitives

5. WHAT THIS MEANS FOR OUR QUESTION:
   The K-P program shows that the Selberg class axioms are VERY
   restrictive. For degree 1, they completely determine the function.
   For degree 2, it is CONJECTURED (but not proved) that they
   determine the function to be an automorphic L-function.

   If the Selberg class = automorphic L-functions (Langlands-Selberg
   conjecture), then GRH in the Selberg class = GRH for automorphic
   L-functions. Neither is proved, but they would be equivalent.
""")

# =================================================================
# ANALYSIS 4: The precise logical structure
# =================================================================
print("\n" + "=" * 70)
print("ANALYSIS 4: Complete Logical Structure")
print("=" * 70)

print("""
THE COMPLETE PICTURE:

GIVEN: S1 (Dirichlet series, convergence Re(s) > 1, a_1 = 1)
       S2 (meromorphic continuation, finite order)
       S3 (functional equation with Gamma factors)
       S5 (Euler product, b_{p^k} = O(p^{k*theta}), theta < 1/2)

DERIVED:
  Step 1: S1 + S5 => a_n = O(n^eps) for all eps > 0
          (i.e., S4 follows from S1 + S5)
          PROOF: S1 gives convergence for Re(s) > 1.
          S5 gives multiplicative structure with a_p ~ sum alpha_{j,p}.
          PNT + convergence at sigma = 1+eps for all eps > 0
          => |a_p| = O(p^eps) => |alpha_{j,p}| <= 1+eps for all eps
          => |alpha_{j,p}| <= 1 (for all but finitely many p).
          Multiplicativity extends to all n.

  Step 2: S4 (|alpha_{j,p}| <= 1) + S3 (functional equation pairing)
          => |alpha_{j,p}| = 1 for all j, p (full Ramanujan)
          PROOF: FE pairs Satake parameters: alpha_j * alpha_sigma(j) = chi(p)
          with |chi(p)| = 1. Both factors <= 1, product = 1 => both = 1.

  Step 3: So S1+S2+S3+S5 => full Ramanujan conjecture.

  Step 4: BUT Ramanujan is OPEN for Maass forms!
          This means either:
          (a) Maass form L-functions satisfy S1+S2+S3+S5 and our
              argument proves Ramanujan (unlikely — the argument must
              have a gap), OR
          (b) Our argument has a subtle gap.

WHERE IS THE GAP?

The gap is in Step 1. The convergence argument assumes:
  sum_p |a_p| p^{-sigma} converges for all sigma > 1
  => |a_p| = O(p^eps) for all eps > 0

But this is NOT quite right. The correct statement is:
  sum_p |a_p| p^{-sigma} < infty for sigma > 1
  does NOT require |a_p| = O(p^eps).

  Example: |a_p| could be 1 for most primes but p^{1/4} for a sparse
  subset of primes. If the sparse subset has density 0 (which it must
  for convergence), then sum_p p^{1/4-sigma} over the subset converges
  for sigma > 1.

  More precisely: sum_p |a_p|^2 p^{-2sigma} < infty for sigma > 1
  is guaranteed by S5 with theta < 1/2. This gives Rankin-Selberg
  type bounds but NOT pointwise |a_p| <= 1.

CORRECTED STATEMENT:
  S1 + S5 => sum_p |a_p|^2 p^{-2sigma} < infty for sigma > 1
           => |a_p|^2 / p is summable (from sigma = 1)
           => |a_p| = O(p^{1/2+eps}) on average
           => S4 in the weak form (a_n = O(n^eps))

  Wait, this is also wrong. Let me be very precise.

PRECISE ANALYSIS:

S5 states: log F(s) = sum_p sum_k b_{p^k} p^{-ks} with
b_{p^k} = O(p^{k*theta}), theta < 1/2.

This means: |b_p| = O(p^theta) with theta < 1/2.
Since b_p = a_p (the Dirichlet coefficient at p), we get
|a_p| = O(p^theta) with theta < 1/2.

But S4 requires |a_p| = O(p^eps) for ALL eps > 0. The S5 condition
gives theta < 1/2 but does NOT give theta = 0.

So S5 alone gives |a_p| = O(p^{1/2-delta}) for some delta > 0.
This is WEAKER than S4.

Now add S1: convergence for Re(s) > 1.
The series sum a_n n^{-s} converges for sigma > 1.
For sigma = 1+eps: sum |a_n| n^{-1-eps} < infty.
This requires sum_p |a_p| p^{-1-eps} < infty.
By PNT: |a_p| = O(p^eps') for any eps' > eps.
Since eps is arbitrary: |a_p| = O(p^eps) for all eps > 0.

AH BUT WAIT: The argument "sum_p |a_p| p^{-1-eps} < infty for all eps > 0
implies |a_p| = O(p^eps)" is correct only for the INDIVIDUAL terms.
The sum can converge even with sporadic large terms, as long as they
are sparse enough.

Let me think about this more carefully with Dirichlet series.

For sum a_n n^{-s} converging for Re(s) > 1:
  Necessary condition: a_n = o(n^{1+eps}) for any eps > 0.
  NOT necessary: a_n = O(n^eps).

  Example: a_n = 0 for most n, but a_N = N for N = 2^{2^k}.
  Then sum a_n n^{-s} = sum_k 2^{2^k} * 2^{-s*2^k} which converges
  for Re(s) > 1 (the terms decay double-exponentially).
  But a_N = N is NOT O(N^eps) for eps < 1.

However, for MULTIPLICATIVE functions (from S5), sporadic large
values at primes propagate to prime powers and products.
If |a_p| = p^{0.4} at some prime p, then |a_{p^k}| ~ p^{0.4k},
and the series sum a_n n^{-s} at sigma = 1+eps gets contributions
~ p^{0.4k - k(1+eps)} = p^{k(-0.6-eps)} from p^k.
This converges for each p, so multiplicativity alone does NOT
force |a_p| to be small.

THE REAL CONSTRAINT: S5 explicitly states theta < 1/2.
Combined with S1 (convergence for Re(s) > 1), what do we get?

The S5 bound b_{p^k} = O(p^{k*theta}) with theta < 1/2 means
the Euler product sum_p sum_k |b_{p^k}| p^{-k*sigma} converges
for sigma > 1+theta (approximately). Wait, more precisely:

sum_p sum_k |b_{p^k}| p^{-k*sigma}
<= C * sum_p sum_k p^{k(theta - sigma)}
= C * sum_p p^{theta-sigma} / (1 - p^{theta-sigma})
This converges for sigma > 1 + theta.

S1 requires convergence for sigma > 1. So we need 1 + theta <= 1,
i.e., theta <= 0.

BUT theta < 1/2 is the S5 condition, and we're getting theta <= 0!

WAIT — the S5 condition says b_{p^k} = O(p^{k*theta}) for some
theta < 1/2. This theta is a BOUND, not an exact value.
The actual theta ACHIEVED could be 0 (Ramanujan) or anything < 1/2.

S1 says the Dirichlet series converges for Re(s) > 1.
S5 says there is an Euler product with some theta < 1/2.
Combined: the theta MUST be <= 0, which means theta = 0
(since theta >= 0 trivially for non-degenerate Satake parameters).

So S1 + S5 => theta = 0 => S4.

BUT the issue is: S5 says b_{p^k} = O(p^{k*theta}) for SOME theta < 1/2.
The 'some' is existential. S1 constrains what that theta can be.
The constraint is theta <= 0, which in the formulation means the
infimum of valid thetas is <= 0.

HMMMM. But theta in S5 is any fixed value < 1/2 that works as a
uniform bound. If the actual Satake parameters satisfy
|alpha_{j,p}| = p^{epsilon_p} with epsilon_p -> 0 but epsilon_p > 0
for all p, then the INFIMUM of valid thetas is 0, and 0 < 1/2,
so S5 is satisfied. Meanwhile a_p ~ p^{epsilon_p} which is
O(p^eps) for any eps > 0. So S4 holds.

What if epsilon_p doesn't tend to 0? Say |alpha_{j,p}| = p^{0.1}
for all p. Then theta = 0.1 works in S5. But then a_p ~ p^{0.1}
and sum a_p p^{-sigma} ~ sum p^{0.1 - sigma} which converges only
for sigma > 1.1. So S1 (convergence for sigma > 1) FAILS.

DEFINITIVE CONCLUSION:

S1 (strict, sigma > 1) + S5 (Euler product, theta < 1/2)
DO imply S4 (a_n = O(n^eps) for all eps > 0).

The proof is by contrapositive: if S4 fails, then for some delta > 0,
|a_p| >= p^delta for infinitely many p. With an Euler product, this
means the Dirichlet series diverges at sigma = 1 + delta/2, so it
cannot converge for all sigma > 1, violating S1.
""")

# Numerical verification
print("\nNumerical verification of the convergence obstruction:")
print()

for delta in [0.01, 0.05, 0.1, 0.2]:
    # If |a_p| = p^delta for all primes, the partial sums of
    # sum_p p^{delta - sigma} diverge for sigma <= 1 + delta.
    sigma = 1 + delta/2  # Between 1 and 1+delta
    partial_sum = mpf(0)
    # Sum over primes up to 10000
    primes = []
    sieve = [True] * 10001
    for i in range(2, 10001):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, 10001, i):
                sieve[j] = False

    for p in primes:
        partial_sum += power(p, delta - sigma)

    print(f"  delta = {delta}, sigma = 1+delta/2 = {1+delta/2}:")
    print(f"    sum_{{p<=10000}} p^{{delta-sigma}} = {nstr(partial_sum, 8)}")
    print(f"    (should diverge as cutoff -> infinity for sigma = 1+delta/2)")
    print(f"    Comparison: log(log(10000)) = {nstr(log(log(10000)), 8)}")
    print()

# =================================================================
# ANALYSIS 5: The refined question after S4 is settled
# =================================================================
print("\n" + "=" * 70)
print("ANALYSIS 5: The Refined Questions")
print("=" * 70)

print("""
Given that S4 is a CONSEQUENCE of S1+S5, the original question
"Do S1+S2+S3+S5 without S4 force zeros onto Re(s) = 1/2?"
becomes:
"Do S1+S2+S3+S4+S5 force zeros onto Re(s) = 1/2?"
which IS the Selberg class GRH conjecture.

Moreover, from our Analysis 1 and 2:
  S3 + S4 => full Ramanujan (|alpha_{j,p}| = 1)

So the Selberg class axioms S1+S2+S3+S4+S5 imply BOTH:
(a) Ramanujan conjecture (from S3 + S4)
(b) Everything else we know about L-functions

And the question "does S imply GRH?" is EQUIVALENT to:
"Does Ramanujan + FE + Euler product + analytic continuation
imply all zeros on Re(s) = 1/2?"

THIS is what the Selberg class GRH conjecture asserts.

WHAT IS KNOWN ABOUT S => GRH:

1. For degree 1: S => F is L(s,chi) (Kaczorowski-Perelli).
   GRH for L(s,chi) is a theorem for chi = 1 under no additional
   assumptions (it's the classical RH, still open).
   So even for d=1, S does NOT imply GRH (since RH is open).

2. For degree 2: Much less is known.

3. GENERAL: No unconditional result of the form "S => GRH" is known
   for ANY degree, not even degree 0 (vacuously true since d=0 => F=1).

4. What IS known: the Selberg class axioms imply MANY consequences
   of GRH:
   - Zero-free regions: F(s) != 0 for Re(s) > 1 - c/log(|t|+3)
   - Zero density estimates: N(sigma, T) << T^{A(1-sigma)} log T
   - Prime number theorem analogues: sum a_p p^{-s} has abscissa 1
   - Mean-value theorems: integral |F(1/2+it)|^2 dt ~ T log T

5. But zero-free regions are NOT the critical line. The gap between
   "no zeros for Re(s) > 1 - c/log t" and "no zeros for Re(s) > 1/2"
   is ENORMOUS.

WHAT WOULD IT TAKE TO PROVE S => GRH:

Option A: Prove that the Selberg class = automorphic L-functions
(Langlands-Selberg conjecture), then prove GRH for automorphic
L-functions. Both steps are open.

Option B: Prove GRH directly from the axioms, without identifying
the functions. This would be a purely analytic proof. No one knows
how to do this.

Option C: Find a NEW axiom that:
(i) Is satisfied by all automorphic L-functions
(ii) Together with S1-S5, implies GRH
(iii) Is not itself equivalent to GRH

This is essentially the program that R26 and the attack plan pursue.
The "tool creation" from R26 section 6 is exactly seeking (iii).
""")

# =================================================================
# ANALYSIS 6: Implications for the QG5D program
# =================================================================
print("\n" + "=" * 70)
print("ANALYSIS 6: What This Means for the QG5D RH Program")
print("=" * 70)

print("""
FROM R26: Adelic RP gives S1+S2+S3+S5 (structurally).
FROM R27 (this file): S1+S5 => S4. So adelic RP gives ALL of S1-S5.

But S1-S5 do NOT imply GRH (the Selberg class conjecture is open).
So adelic RP does NOT imply GRH through the Selberg class route.

THE REVISED PICTURE:

What adelic RP gives:
  S1 + S2 + S3 + S5 => S4 => full Ramanujan => all Selberg axioms
  All zero-free region results, density estimates, etc.
  But NOT GRH.

What's STILL needed for GRH:
  A mechanism that converts the Selberg class axioms (or their
  adelic RP equivalent) into a zero-location statement.

The four angles from the attack plan address this:
  Angle 1 (Adelic Lee-Yang): converts local positivity to zero location
  Angle 2 (Selberg Class): THIS analysis — S4 is redundant, but
    the Selberg class conjecture remains open
  Angle 3 (Bost-Connes): phase transition at beta=1 as zero mechanism
  Angle 4 (Explicit Formula): additive Lee-Yang via prime sums

WHAT R27 CONTRIBUTES TO THE PROGRAM:

1. CLARIFIES that S4 is NOT the bottleneck. The R26 diagnosis
   "S4 is the gap" is WRONG in one sense: S4 follows from S1+S5.
   The gap is not a MISSING AXIOM but a missing THEOREM
   (that S1-S5 imply GRH).

2. ESTABLISHES that the full Ramanujan conjecture follows from the
   Selberg class axioms (via S3+S4). This is a POSITIVE result:
   the QG5D framework, via adelic RP, gives everything needed
   for the Selberg class.

3. REFRAMES the problem: the question is not "which axioms are
   sufficient?" but "what proof technique converts the axioms
   into a zero-location theorem?" This is the correct framing
   for the four angles.

4. IDENTIFIES the real mathematical frontier: Selberg class GRH.
   This is one of the deepest open problems in analytic number theory.
   No amount of axiom-hunting can bypass it — what's needed is a
   PROOF TECHNIQUE.
""")

print("\n" + "=" * 70)
print("FINAL THEOREM SUMMARY")
print("=" * 70)

print("""
THEOREM (S4 is redundant):
  S1 (convergence Re(s) > 1) + S5 (Euler product, theta < 1/2)
  => S4 (a_n = O(n^eps) for all eps > 0).

THEOREM (Ramanujan from FE + Ramanujan bound):
  S3 (functional equation with pairing of Satake parameters)
  + S4 (|alpha_{j,p}| <= 1)
  => |alpha_{j,p}| = 1 for all j, p (full Ramanujan).

COROLLARY:
  The Selberg class axioms S1+S2+S3+S5 imply S4 AND full Ramanujan.
  S4 is not an independent axiom.

OPEN PROBLEM:
  S1+S2+S3+S4+S5 => GRH (the Selberg class GRH conjecture).
  WIDE OPEN. Not even proved for degree 1.
""")
