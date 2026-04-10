# Strategy 22 — Attacking the Three Wounds

*The Cartwright core survives. Three wounds remain. Each has*
*a concrete attack angle.*

*Date: 2026-04-10*

---

## Wound 1 (Step 9): Induction exception accumulation

**The problem:** At each step K, Cartwright gives finitely many
bad primes. But the bound depends on the eigenvector (hence K).
Could bad sets accumulate to cover all primes?

**Attack: The ZERO BOUND for cosine sums.**

g_k(ξ) = Σ_{i=1}^N φ_k[i] cos(x_i ξ) is a sum of N cosines
with frequencies x_i ∈ [0, L]. By the generalization of the
trigonometric polynomial zero bound:

A sum of N exponentials (or cosines) with distinct real frequencies
has at most 2N−1 zeros on any interval of length T, provided
the frequencies are contained in [−Ω, Ω] (this is a consequence
of the Chebyshev system property — {cos(x_i ξ)} form a Chebyshev
system on any interval if the x_i are distinct).

Actually, the stronger result: a linear combination of N functions
from a Chebyshev system has at most N−1 zeros (Chebyshev's
theorem). {1, cos(x_1 ξ), cos(x_2 ξ), ..., cos(x_N ξ)} with
distinct x_i ≥ 0 form a Chebyshev system on [0, ∞) (this is a
theorem for cosines with distinct frequencies).

So g_k has at most N−1 zeros on [0, ∞). Since g_k ≠ 0
(Step 4), it has at most N−1 zeros TOTAL on [0, ∞).

**The key:** This bound is N−1 regardless of the eigenvector φ_k
and regardless of K. It depends only on the grid size N. The bound
is UNIFORM in K.

For the first N primes: at most N−1 of them can be zeros of g_k.
But there are N primes. So at least ONE prime gives a nonzero
overlap. Actually we need ALL primes to give nonzero overlaps for
the induction — but at most N−1 can be bad. So for primes
beyond the N-th, the overlap is automatically nonzero.

Wait — this doesn't quite close it. We need p_{K+1} specifically
to be nonzero. But the bound says at most N−1 zeros among ALL
{log p}. If K+1 > N−1, then p_{K+1} is automatically good.

For the first N−1 primes: numerical verification (already done).
For all subsequent primes: the Chebyshev bound gives it FOR FREE.

**This closes Wound 1 completely IF {cos(x_i ξ)} is a Chebyshev
system on [0, ∞) for distinct x_i ≥ 0.**

## Wound 2 (Step 12): Discrete ↔ CCM bridge

**The problem:** B is a matrix on R^N. CCM's operators act on
L²([λ⁻¹, λ]). The identification is asserted.

**Attack:** The CCM construction discretizes the Weil explicit
formula on a grid. Our B IS that discretization. The identification
is: B = the matrix of CCM's quadratic form restricted to the
N-dimensional subspace spanned by the grid basis functions.

This is a STANDARD relationship between a continuous operator and
its Galerkin discretization. As N → ∞, the discrete eigenvalues
converge to the continuous ones (standard finite element theory).

The rigorous argument: CCM's Theorem 5.10 gives spectral
convergence for the continuous operators. Our Cartwright argument
gives simplicity for the discrete matrices. The bridge is:
simplicity of the discretization implies simplicity of the
continuous operator (by spectral convergence + gap preservation).

This needs: the discrete eigenvalue gaps don't close faster than
the discretization error. The exponential gap decay (~10⁻¹·⁷ᴺ)
is concerning, but the discretization error also decays
exponentially for Chebyshev grids (spectral methods).

## Wound 3 (Step 10): K → ∞ passage

**The problem:** Strict interlacing at finite K might not survive
K → ∞. Gaps could close.

**Attack:** If the Chebyshev system bound (Wound 1 fix) gives at
most N−1 zeros TOTAL, and the grid has N points, then for K ≥ N
the overlap is automatically nonzero. The induction only runs
to K = π(P_max), the number of primes up to the cutoff. For the
CCM construction, the cutoff is P = λ². The limit is λ → ∞
(equivalently P → ∞), not K → ∞ at fixed N.

So the correct limiting process is:
- Fix N (grid size)
- Run induction K = 0, 1, ..., K_max where K_max ~ π(λ²)
- For K > N−1: automatic (Chebyshev bound)
- For K ≤ N−1: numerical verification (done)
- Then take N → ∞ with λ → ∞

The K → ∞ limit is actually K → K_max(λ) → ∞ as λ → ∞, but
at each stage, the Chebyshev bound (which grows with N) handles
all but the first N−1 primes. Since N also grows with λ, the
number of numerically verified primes grows but remains finite.

---

## The revised chain (if Wound 1 closes via Chebyshev systems)

The entire argument simplifies dramatically:

1. g_k(ξ) = Σ_i φ_k[i] cos(x_i ξ) has at most N−1 zeros on
   [0, ∞) (Chebyshev system bound — UNIFORM in K)
2. There are infinitely many primes
3. Therefore g_k(log p) ≠ 0 for all but at most N−1 primes
4. For K > N−1: the induction step is automatic
5. For K ≤ N−1: verify numerically (already done to 120 digits)
6. The induction closes for all K → Arithmetic Theorem → RH

No Cartwright theorem needed! The Chebyshev system bound is
STRONGER and SIMPLER. It gives a UNIFORM bound (N−1) that
doesn't depend on the eigenvector at all.

---

## The one thing to verify

> **Are {cos(x_1 ξ), ..., cos(x_N ξ)} a Chebyshev system on
> [0, ∞) for distinct x_i > 0?**

A Chebyshev system (T-system) on an interval I is a set of
functions {f_1, ..., f_N} such that any nontrivial linear
combination has at most N−1 zeros on I.

For {cos(a_k x)} with distinct a_k > 0: this is known to be
a Chebyshev system on [0, π/max(a_k)] but NOT necessarily on
larger intervals (cosines are periodic/quasi-periodic and can
have additional zeros).

WAIT — this is the critical check. On a HALF-LINE [0, ∞),
cosines are NOT a Chebyshev system because they oscillate.
The zero count can exceed N−1.

On a SMALL interval [0, δ], they ARE a Chebyshev system (by the
Vandermonde argument: near 0, cos(a_k x) ≈ 1 − a_k²x²/2, and
the polynomials {1 − a_k²x²/2} form a Chebyshev system).

The {log p} are distributed on [0, ∞), not on a small interval.
So the Chebyshev system argument might NOT work on the full range.

HOWEVER: we don't need a Chebyshev system on [0, ∞). We need a
FINITE zero count. And Cartwright ALREADY gives that. The issue
was uniformity in K.

**Revised approach:** Use the Chebyshev system property on a
FINITE interval [0, T] containing the first M primes. On [0, T],
{cos(x_i ξ)} IS a Chebyshev system IF T < π/max(x_i) = π/L.
The first few log p values are: log 2 ≈ 0.69, log 3 ≈ 1.10,
log 5 ≈ 1.61, log 7 ≈ 1.95, ... For L = 10: π/L ≈ 0.314.
But log 2 = 0.69 > 0.314. So even the FIRST prime is outside
the Chebyshev interval.

This means the Chebyshev system approach on [0, ∞) doesn't
directly work. We're back to Cartwright.

**The actual fix for Wound 1:** Show the Levin constant C in the
zero bound n(T) ≤ σT/π + C is bounded uniformly in K. C depends
on log|g_k(0)| and the integral of log|g_k|. For normalized
eigenvectors (||φ_k|| = 1): |g_k(0)| = |Σ φ_k[i]| ≤ √N
(Cauchy-Schwarz). The integral of log|g_k| over R is bounded by
log(√N) (since |g_k| ≤ √N on R). So C ≤ C(N) — depends on N
but NOT on K. For fixed N, the bound is uniform in K.

**THAT'S the fix.** C depends on N (the grid size) but not on K
(the number of primes). Since N is fixed in the induction (we add
primes to a fixed grid), C is fixed. The Levin bound gives at
most σT/π + C(N) zeros of g_k in [0, T]. This is uniform in K.

---

> *Chebyshev systems: too small an interval. Killed on [0,∞).*
> *Cartwright + uniform Levin constant: ALIVE.*
> *C depends on N (grid) not K (primes). Uniform in K.*
> *Wound 1 closes via explicit Levin bounds.*
