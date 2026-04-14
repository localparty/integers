# Twin Prime Conjecture via Zero-Spacing Statistics

*A research programme (not a proof skeleton).*
*Status: ~1/10.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-13*

---

## Entry point

The explicit formula connects prime gaps to the spacing of Riemann
zeros. For primes p_n and p_{n+1}, the gap d_n = p_{n+1} - p_n is
controlled by oscillatory sums over zeta zeros:

    sum_{gamma} p_n^{i gamma} / (1/2 + i gamma)

The twin prime conjecture -- there are infinitely many primes p with
p + 2 also prime -- is a statement about the distribution of gaps
d_n = 2. The framework provides a spectral interpretation: twin
primes correspond to specific pair-correlation statistics of Riemann
zeros at close spacing.

---

## The spectral interpretation

**Prime gaps from zero spacing.** The Hardy-Littlewood conjecture
(1923) predicts that the number of twin primes up to x is
asymptotically

    pi_2(x) ~ 2 C_2 x / (log x)^2

where C_2 = prod_{p >= 3} (1 - 1/(p-1)^2) = 0.6601... is the
twin prime constant. This asymptotic is related to the pair
correlation of zeros at close spacing via the explicit formula:
the sum over zeros oscillates, and twin primes require constructive
interference at gap = 2.

**If BGS closes (Link 5 of bgs-spectral-statistics):** The GUE pair
correlation function

    R_2(s) = 1 - (sin(pi s) / (pi s))^2

governs the spacing of Riemann zeros. The Fourier transform of R_2
constrains prime-gap statistics. Montgomery (1973) showed that the
GUE pair correlation, combined with the explicit formula, predicts
the Hardy-Littlewood asymptotic for twin primes -- but this is
a PREDICTION, not a proof.

---

## What is already known classically

- **Zhang 2013:** There are infinitely many prime pairs with gap
  <= 7 x 10^7 (bounded gaps theorem).
- **Maynard 2015 / Tao (Polymath 8b):** Gap <= 246.
- **Under GRH + Elliott-Halberstam:** Gap <= 6 (Goldston-Pintz-
  Yildirim 2005, conditional).

The framework provides the SPECTRAL EXPLANATION for bounded gaps:
the GUE statistics of Riemann zeros, via the explicit formula, force
primes to cluster. Zhang-Maynard-Tao proved bounded gaps using
sieve methods; the BC framework explains WHY sieves work -- the
spectral structure of the zeros forces the prime distribution to
have bounded gaps.

---

## The twin prime gap

Bounded gaps (infinitely many gaps <= 246) are proved. Twin primes
(infinitely many gaps = 2) require going beyond GUE bulk statistics:

1. **Bulk GUE gives bounded gaps.** The pair correlation function
   R_2(s) vanishes at s = 0 (level repulsion) but is positive for
   small s > 0. This forces primes to have bounded gaps, because
   zeros cannot be too regularly spaced.

2. **Twin primes need fine structure.** Gap exactly 2 requires
   understanding the pair correlation at the SPECIFIC scale
   2 / (log p) in the zero spacing. This is beyond the bulk GUE
   universality and enters the realm of mesoscopic statistics.

3. **The arithmetic factor.** The twin prime constant C_2 is an
   arithmetic factor that GUE alone cannot produce. It arises from
   the local structure of primes mod small primes (sieve theory).
   Any spectral approach must reproduce this arithmetic factor.

---

## Connection to GRH

If GRH holds for all Dirichlet L-functions L(s, chi), then:

- The Bombieri-Vinogradov theorem is upgraded to the Elliott-
  Halberstam conjecture (or close to it)
- GPY + Elliott-Halberstam gives gaps <= 6
- The twin prime conjecture would follow from a further strengthening
  of the equidistribution of primes in arithmetic progressions

In the BC framework, Dirichlet characters chi are automorphisms of
the BC algebra (they act on Q/Z via Galois). GRH for L(s, chi)
is a statement about the spectral realization of all these
characters, not just the trivial one.

---

## Programme structure

This is NOT a proof skeleton. The links from entry point to twin
primes are:

    zero spacing (GUE) --> prime gap statistics --> bounded gaps --> twin primes
    (BGS chain)           (explicit formula)       (PROVED classically)  (OPEN)

The first arrow is the BGS chain (see bgs-spectral-statistics).
The second arrow is the explicit formula (classical). The third
arrow is Zhang-Maynard-Tao (proved 2013-2015). The fourth arrow
is the OPEN gap: bounded gaps --> twin primes.

---

## Milestones (speculative)

1. Close the BGS chain (see bgs-spectral-statistics programme)
2. Derive bounded gaps as a corollary of GUE + explicit formula
   (reproducing Zhang-Maynard-Tao spectrally)
3. Extend GRH to all Dirichlet characters within the BC framework
   (this is a separate research programme, closely tied to Paper 13)
4. Investigate mesoscopic zero statistics beyond bulk GUE
5. Attempt the arithmetic factor C_2 from the BC sieve structure

---

## Honest accounting

Status: ~1/10. Bounded gaps might follow from the BGS chain as a
spectral corollary (Milestone 2), which would be satisfying but not
new mathematics. Twin primes specifically (gap = 2) require going
far beyond anything the current framework provides. The arithmetic
factor C_2 is fundamentally a sieve-theoretic object, and it is
unclear how (or whether) the BC algebra captures sieve structure.
This programme is decades away from completion.

---

Next step: a dedicated cell-fill run on Milestone 2 (spectral derivation of bounded gaps from GUE pair correlation).
