# 267. Stark Unit Computation for Conjecture 5 (V-Hilbert 12)

*Authors: G Six with Claude Opus 4.6. Date: 2026-04-09.*

> **Goal.** Compute Stark units epsilon_chi = exp(-L'(0, chi)) for
> the three CBB bridge characters and check whether their Galois
> phases equal the cocycle values 1/k mod Z, as predicted by
> Conjecture 5 of Paper 25 section 8.

## 1. Method

For each bridge (p, l) with index k, construct the primitive
Dirichlet character chi of order k on (Z/lZ)* using generator
g = 2. Compute L'(0, chi) numerically via central difference on
the Hurwitz-zeta representation

    L(s, chi) = N^{-s} sum_{a=1}^{N-1} chi(a) zeta(s, a/N)

at s = 0 with h = 10^{-12}, using mpmath at 50-digit precision.
The Stark unit is epsilon_chi = exp(-L'(0, chi)). The Galois phase
is arg(epsilon_chi) / (2 pi) mod 1 = -Im(L'(0, chi)) / (2 pi) mod 1.

## 2. Results

### Bridge (5, 13), k = 3: chi of order 3 on (Z/13Z)*

    L(0, chi_3) = -B_{1,chi_3} ~ 0   (numerically < 10^{-50})
    L'(0, chi_3) = 0.80754... + 0.84435...i

    epsilon_chi = exp(-L'(0, chi_3)) = 0.29621... - 0.33337...i
    |epsilon| = 0.44595...

    Phase = arg(epsilon) / (2 pi) mod 1 = 0.86562
    Target: 1/3 = 0.33333
    Match: **NO** (difference 0.468)

### Bridge (3, 13), k = 4: chi of order 4 on (Z/13Z)*

    L(0, chi_4) = -B_{1,chi_4} = 1 + i
    L'(0, chi_4) = 0.30176... - 0.26034...i

    epsilon_chi = exp(-L'(0, chi_4)) = 0.71460... + 0.19036...i
    |epsilon| = 0.73952...

    Phase = arg(epsilon) / (2 pi) mod 1 = 0.04143
    Target: 1/4 = 0.25000
    Match: **NO** (difference 0.209)

### Bridge (7, 19), k = 6: chi of order 6 on (Z/19Z)*

    L(0, chi_6) = -B_{1,chi_6} = 1 + sqrt(3)i
    L'(0, chi_6) = 0.45670... - 0.81697...i

    epsilon_chi = exp(-L'(0, chi_6)) = 0.43350... + 0.46178...i
    |epsilon| = 0.63337...

    Phase = arg(epsilon) / (2 pi) mod 1 = 0.13003
    Target: 1/6 = 0.16667
    Match: **NO** (difference 0.037)

## 3. Exhaustive character scan

All nontrivial characters mod 13 (m = 1..11) and mod 19 (m = 1..17)
were scanned. No character of any order yields a phase exactly equal
to 1/k for k in {2, 3, 4, 6}.

Closest near-misses (tolerance < 0.02):

    mod 13, m=2 (order 6):  phase 0.9252 ~ 11/12 (d=0.0085)
    mod 13, m=10 (order 6): phase 0.0748 ~ 1/12  (d=0.0085)

    mod 19, m=2 (order 9):  phase 0.8341 ~ 5/6   (d=0.0008)
    mod 19, m=16 (order 9): phase 0.1659 ~ 1/6   (d=0.0008)
    mod 19, m=8 (order 9):  phase 0.0538 ~ 1/18  (d=0.0018)
    mod 19, m=10 (order 9): phase 0.9462 ~ 17/18 (d=0.0018)

The m=16 character mod 19 (order 9, not order 6) comes closest
to the 1/6 target with d = 0.0008, but this is still not an exact
match and has the wrong character order.

## 4. Diagnosis

The Stark unit epsilon_chi = exp(-L'(0, chi)) for a Dirichlet
character chi mod N is an algebraic unit in Q(zeta_N)^{ab} only
when Stark's conjecture holds (proven for abelian extensions of Q,
i.e., for Dirichlet characters, by the analytic class number
formula). However, the *phase* of the Stark unit is determined by
Im(L'(0, chi)), which is a transcendental quantity with no reason
to equal 1/k.

The conjecture as stated in Paper 25 section 8 identifies:

    V's matrix elements = L'(0, chi)   (up to period normalization)

The "up to period normalization" qualifier is doing essential work.
The raw L'(0, chi) values do NOT produce Galois phases equal to
1/k. If the conjecture is to survive, the period normalization
must be specified explicitly — it cannot be a simple scalar.

## 5. Comparison with research/188

Research/188 tested L'(1, chi)/L(1, chi) = 1/k and found it fails.
The present computation tests the Stark-unit version at s = 0:
arg(exp(-L'(0, chi))) / (2 pi) = 1/k. This also fails.

The two failures are related by the functional equation but are
logically independent tests. Both refute the naive reading of
Conjecture 5.

## 6. Verdict

**Conjecture 5 (V-Hilbert 12) is REFUTED in its literal form.**

The Galois phases of exp(-L'(0, chi)) do not equal 1/k mod Z for
any of the three bridges, nor for any other character mod 13 or
mod 19. The conjecture requires either:

(a) A non-trivial "period normalization" that rotates the phases
    to 1/k — but this would need to be specified to be testable.

(b) A different identification between V's matrix elements and
    L-function values — perhaps involving Gauss sums, conductors,
    or the W-factor of the functional equation.

(c) Abandonment: the bridge cocycle 1/k lives in H^2(Z/kZ, U(1))
    as a discrete invariant and is not encoded in the continuous
    Galois phase of any Stark unit.

The structural observation from research/188 remains: the
order-k characters exist at the right conductors, aligning with
the k = 3, 4, 6 bridges. The *existence* of the right characters
is confirmed; their *values* do not carry the cocycle.
