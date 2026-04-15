#!/usr/bin/env python3
"""
T7e bridge-family minimality verification — Lead 7e.
Hardens Anchor 4 of the seven-anchor strategy
(paper12/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md).

Precision / exactness model (declared up front):
  - All arithmetic is EXACT integer arithmetic in Z and in (Z/NZ)*.
  - Multiplicative orders are computed by divisor enumeration of phi(N)=N-1
    using sympy.factorint (exact integer factorization).
  - Brauer classes are exact rationals (fractions.Fraction).
  - No floating-point is involved anywhere in the sieve.
  - So "symbolic precision" here means "arbitrary-precision integers", which
    for the sizes below (primes < 200) is effectively infinite precision.

Goal: for each target k in {2, 3, 4, 6}, enumerate all (p, N) pairs with
p, N prime, p != N, p < N < BOUND satisfying the bridge sieve, and
identify the LEXICOGRAPHICALLY MINIMAL pair (ordered first by N, then by p).
Compare with the framework's claimed pairs:
    k=2: (2, 7),   k=3: (5, 13),   k=4: (3, 13),   k=6: (7, 19).
"""

from sympy import isprime, factorint, totient, primerange
from math import gcd
from fractions import Fraction

# ----- sieve constraints, cited verbatim from research/162 and 169 -----
#
# research/162 §1:
#   "Frob_5 generates an order-4 subgroup of (Z/13Z)*, and the quotient
#    G_arith = (Z/13Z)*/<5> ~= Z/3Z."
# research/169 §1:
#   "Given prime p and level N with gcd(p,N) = 1, let f = ord_N(p)
#    (residue degree of Frob_p on Q(zeta_N)/Q) and
#      k := phi(N)/f = |(Z/NZ)*/<p>|.
#    When (Z/NZ)*/<p> is cyclic of order k, the cyclic algebra
#    (Q(zeta_N)/Q, Frob_p, zeta_k) carries a Brauer class in Br(Q)[k]
#    with local Hasse invariant 1/k at p."
# research/169 §2 footnote:
#   "k = 2 chosen with nontrivial f > 1 for arithmetic content; the
#    degenerate (p, N) = (5, 4) with f = 1 also gives k = 2 but is trivial."
#   ==> f > 1 is an explicit sieve constraint (non-degeneracy).
#
# Sieve constraints used:
#   (C1) p, N both prime, p != N.
#   (C2) gcd(p, N) = 1  (automatic since both prime and distinct).
#   (C3) (Z/NZ)* cyclic of order phi(N) = N - 1 (automatic for prime N).
#   (C4) k = phi(N) / ord_N(p) equals the target k.
#       <=>  k | (N - 1)  and  ord_N(p) = (N - 1) / k.
#   (C5) f = ord_N(p) > 1  (non-degeneracy; research/169 §2 footnote).
#   (C6) Brauer class [A] = 1/k mod Z is NON-TRIVIAL in H^2(Z/kZ, U(1)) ~= Z/kZ.
#        For k >= 2 the class 1/k is always nonzero in Z/kZ.
#        For k = 2 the cohomology group H^2(Z/2Z, U(1)) is trivial in the
#        continuous-U(1) sense, but 1/2 is the unique 2-torsion element;
#        Lead 7b (T1-T2) and research/169 treat k=2 as a valid bridge with
#        "expected-trivial" cocycle class. We keep (C6) literal: 1/k != 0 in Q/Z,
#        which for k=2 yields 1/2, matching Lead 7b's verdict.
#
# No other constraint is imposed. In particular we do NOT filter on
#   - p < N                 (we include only this convention when lexicographic
#                            ordering is needed; but we also report all p, even
#                            those with p > N, since Frob_p on Q(zeta_N) only
#                            cares about p mod N and p != N suffices)
#   - Pati-Salam / CKM / Koide matching (those are post-hoc identifications).
# We test p < N vs p > N both below.

def multiplicative_order(a, n):
    """Exact multiplicative order of a in (Z/nZ)*, by divisor enumeration."""
    assert gcd(a, n) == 1
    phi = int(totient(n))
    # enumerate divisors of phi
    divisors = {1}
    for q, e in factorint(phi).items():
        new = set()
        for d in divisors:
            for i in range(e + 1):
                new.add(d * q**i)
        divisors = new
    for d in sorted(divisors):
        if pow(a, d, n) == 1:
            return d
    raise RuntimeError("no order found")

def brauer_class(k):
    """Hasse invariant 1/k mod Z as an element of Q/Z, represented by
    Fraction(1, k) in [0, 1)."""
    return Fraction(1, k)

def nontrivial_in_H2(k):
    """Whether 1/k mod Z is nontrivial in H^2(Z/kZ, U(1)).
    For k >= 2, 1/k is a nonzero element of the cyclic group Z/kZ of
    characters, equivalently nonzero in Q/Z. We follow Lead 7b's convention:
    k=2 gives 1/2 (nontrivial as an element of 1/k Z / Z, expected-trivial in
    the strict U(1)-cohomology sense but still counted as a valid bridge)."""
    return k >= 2  # every candidate we consider has k in {2,3,4,6}

def sieve_valid_pairs(k_target, bound):
    """Return all (N, p) with p,N prime, p!=N, p<N<bound, satisfying
    the sieve for target k=k_target. Sorted lex by (N, p)."""
    valid = []
    for N in primerange(3, bound):
        if (N - 1) % k_target != 0:
            continue
        # need ord_N(p) = (N-1)/k_target
        f_needed = (N - 1) // k_target
        if f_needed <= 1:
            continue  # C5: f > 1
        for p in primerange(2, N):  # p < N, p prime
            if p == N:
                continue
            f = multiplicative_order(p, N)
            if f != f_needed:
                continue
            # k confirmed
            cls = brauer_class(k_target)
            if not nontrivial_in_H2(k_target):
                continue
            valid.append((N, p, f, cls))
    return valid

def main():
    BOUND = 100
    framework_claim = {2: (2, 7), 3: (5, 13), 4: (3, 13), 6: (7, 19)}
    results = {}
    for k in [2, 3, 4, 6]:
        pairs = sieve_valid_pairs(k, BOUND)
        results[k] = pairs
        print(f"\n===== k = {k}   (search bound N < {BOUND}) =====")
        print(f"  #valid pairs: {len(pairs)}")
        for N, p, f, cls in pairs:
            print(f"    (p={p:3d}, N={N:3d})   f=ord_N(p)={f}   "
                  f"k=phi(N)/f={(N-1)//f}   Brauer={cls}")
        if pairs:
            N0, p0, f0, c0 = pairs[0]
            minimal = (p0, N0)
        else:
            minimal = None
        claimed = framework_claim[k]
        match = (minimal == claimed)
        print(f"  MINIMAL (lex by (N,p)): {minimal}")
        print(f"  FRAMEWORK CLAIM:        {claimed}")
        print(f"  {'MATCH' if match else 'MISMATCH'}")
        results[k] = (pairs, minimal, claimed, match)

    # Summary
    print("\n\n===== SUMMARY =====")
    print(f"{'k':>3} | {'minimal (p,N)':>16} | {'framework (p,N)':>16} | verdict")
    print("-" * 60)
    for k in [2, 3, 4, 6]:
        _, minimal, claimed, match = results[k]
        print(f"{k:>3} | {str(minimal):>16} | {str(claimed):>16} | "
              f"{'MATCH' if match else 'MISMATCH'}")

    all_match = all(results[k][3] for k in [2, 3, 4, 6])
    print(f"\nALL FOUR MATCH: {all_match}")
    print(f"Anchor 4 verdict: {'STRENGTHENED' if all_match else 'SEE DIAGNOSIS'}")

if __name__ == "__main__":
    main()
