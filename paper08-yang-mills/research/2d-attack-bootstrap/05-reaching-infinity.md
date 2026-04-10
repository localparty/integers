# 05. Reaching L = infinity

## 5.1 The bootstrap trajectory

Starting from L_0 (the semiclassical boundary), the bootstrap generates
a sequence:

  L_0 < L_1 < L_2 < ... < L_n < ...

where L_{n+1} = L_n + delta_n, and at each step m(L_n) >= mu_n > 0.

**The question:** Does L_n -> infinity, or does it converge to some
finite L* = sup_n L_n < infinity?

**Equivalently:** Does sum_{n=0}^{infinity} delta_n = infinity?


## 5.2 The geometric growth scenario

**If** the step size satisfies delta_n >= c_3 L_n (as argued in
Section 04), then:

  L_{n+1} >= (1 + c_3) L_n

  L_n >= L_0 (1 + c_3)^n

  sum_{n=0}^{N} delta_n >= c_3 L_0 sum_{n=0}^{N} (1 + c_3)^n
                         = c_3 L_0 ((1+c_3)^{N+1} - 1) / c_3
                         = L_0 ((1+c_3)^{N+1} - 1) -> infinity

So the bootstrap reaches L = infinity in "infinite steps" but
L_n -> infinity EXPONENTIALLY fast. After n steps, L_n ~ L_0 e^{c_3 n}.

**Reaching any target L_target:** The number of steps needed is:

  n(L_target) = ln(L_target/L_0) / ln(1 + c_3) = O(ln(L_target/L_0))

This is LOGARITHMIC in the target — extremely efficient.


## 5.3 The lower bound trajectory

Alongside L_n -> infinity, the lower bound mu_n evolves as:

  mu_n >= mu_0 (1 - c_4)^n

After n(L) = ln(L/L_0)/ln(1+c_3) steps to reach circumference L:

  mu(L) >= mu_0 exp( -|ln(1-c_4)| ln(L/L_0) / ln(1+c_3) )
         = mu_0 (L/L_0)^{-alpha}

where:

  alpha = |ln(1 - c_4)| / ln(1 + c_3)

**The behavior of mu(L):**

- If alpha < 0: mu(L) GROWS with L. Impossible (would contradict
  monotone decrease from the step bounds).

- If alpha = 0: mu(L) = mu_0. Perfect case (mass gap doesn't decrease).

- If 0 < alpha < 1: mu(L) decreases as a power law, slowly.
  m(L) >= mu_0 (L_0/L)^alpha with alpha < 1.

- If alpha = 1: mu(L) ~ mu_0 L_0/L. The lower bound decreases as 1/L.
  This is MARGINAL: the condition m > K/L from cluster expansion
  convergence requires mu_0 L_0 > K, which holds at the starting point
  but is not guaranteed to hold forever.

- If alpha > 1: mu(L) decreases FASTER than 1/L. The condition m > K/L
  is eventually violated, and the bootstrap stalls.


## 5.4 What determines alpha

Recall alpha = |ln(1-c_4)| / ln(1+c_3).

The constants c_3 and c_4 come from:
- c_3: the fractional step size (delta/L)
- c_4: the fractional loss in the mass gap bound per step

Both are determined by the cluster expansion at each L. The question is
whether they remain bounded as L varies.

**The three regimes:**

**(A) Small L (semiclassical, L << 1/Lambda):**
c_3 and c_4 are computable from the instanton expansion.
The mass gap is dominated by fractional instantons:
m ~ L Lambda^2. As L increases, m increases, so c_4 is small
(the gap is GROWING). alpha ~ 0 in this regime.

**(B) Crossover (L ~ 1/Lambda):**
This is where the semiclassical description breaks down and
the theory transitions to the strongly-coupled regime.
c_3 and c_4 depend on the full non-perturbative dynamics.
This is the HARDEST regime to control.

**(C) Large L (L >> 1/Lambda):**
The mass gap approaches m(infinity) > 0 (the infinite-volume
value). The theory is essentially the decompactified 2D CP^2
model, with finite-L corrections of order exp(-m L).
c_3 ~ 1 (large steps are possible since m is nearly constant).
c_4 ~ exp(-m L) << 1 (the mass gap barely changes).
alpha ~ 0 in this regime.

**The crossover regime (B) is the bottleneck.** If the bootstrap can
get through the crossover from L ~ 1/Lambda (semiclassical) to
L ~ several/Lambda (strongly-coupled but with m ~ Lambda), then the
rest is easy: in regime (C), the steps are large and the mass gap is
nearly constant.


## 5.5 Estimate of alpha in the crossover regime

In the crossover regime, we need to estimate how much the mass gap
can change per step.

**Upper bound on |dm/dL| from the spectral representation.**

Using the spectral decomposition of the transfer matrix:

  m(L) = E_1(L) - E_0(L)

and the Hellmann-Feynman theorem:

  dm/dL = <1|dH/dL|1> - <0|dH/dL|0>

The operator dH/dL can be bounded by the energy density of the theory.
In a massive theory, the vacuum energy density is:

  e_vac = -(1/(2pi)) integral_0^{infinity} p ln(1 - exp(-beta sqrt(p^2 + m^2))) dp

(for a free massive boson on S^1_{beta=L}). For a general interacting
theory:

  |dE_n/dL| <= (energy density at level n) x (spatial volume = L)

Wait — the spatial volume IS L (we're in 1+1 dimensions with spatial
S^1_L). So:

  |dE_n/dL| <= rho_n

where rho_n is the energy density in state n. For a massive theory:

  |rho_1 - rho_0| ~ m^2 / (4pi)  (the vacuum energy difference for a
                                    particle of mass m)

Therefore:

  |dm/dL| = |rho_1 - rho_0| ~ m^2 / (4pi)

This gives:

  |dm/dL| / m ~ m / (4pi)

and the fractional change over one step of size delta = c_3 L:

  c_4 ~ c_3 L m / (4pi)

At the crossover L ~ 1/Lambda, m ~ Lambda, so:

  c_4 ~ c_3 / (4pi) ~ c_3 / 12

Since c_3 < 1 (the step is a fraction of L), we get c_4 < 1/12.

**Result.** alpha ~ |ln(1 - 1/12)| / ln(1 + c_3) ~ (1/12) / c_3.

If c_3 ~ 1/2 (step size is half the current L), then alpha ~ 1/6.

**This is LESS than 1, which means the bootstrap works!**

The mass gap lower bound decreases as:

  mu(L) >= mu_0 (L_0/L)^{1/6}

which is positive for all finite L.


## 5.6 The infinite-volume limit

Even if m(L) > 0 for all finite L, we need m(infinity) > 0 for the
physical mass gap. The bootstrap gives:

  m(L) >= mu_0 (L_0/L)^{alpha}

which goes to 0 as L -> infinity. So the bootstrap alone does NOT
prove m(infinity) > 0.

**However:** We KNOW from lattice simulations that m(infinity) > 0.
The bootstrap proves that m(L) > 0 for all finite L, which means
there is no phase transition at any finite L. Combined with the
lattice result m(infinity) > 0, this gives:

  m(L) > 0  for ALL L in (0, infinity]

**Can we do better?** Yes, if we can show that m(L) is MONOTONICALLY
related to some controlled quantity as L -> infinity.

**Approach: the monotonicity theorem.** [ARGUED]

In the Z_3-twisted CP^2 model, the mass gap m(L) satisfies:

  m(L) >= m(infinity) - C exp(-m(infinity) L)

for L large enough (L >> 1/Lambda). This follows from the fact that
finite-L corrections to the mass gap are exponentially small in mL
(cluster expansion at large L, where mL >> 1).

If this bound holds, then m(L) > 0 for all L > 0 follows from
m(infinity) > 0 alone — no bootstrap needed for large L. The bootstrap
is only needed to cross the interval [L_0, L_1] where L_1 is the first
value where m L > C for some constant C (so the large-L asymptotics
kicks in).


## 5.7 The gap in the argument

**The honest problem.** The bootstrap argument has a gap at the
crossover regime L ~ 1/Lambda. Specifically:

**(Gap 1) The cluster expansion convergence condition.**
We need m(L) > K/L for the cluster expansion to converge. If K is
too large (K >> 1), this requires mL >> 1, which may not hold at
the crossover.

At the crossover: m ~ Lambda, L ~ 1/Lambda, so mL ~ 1. Whether
mL > K depends on the constant K, which depends on the combinatorics
of the polymer expansion (specifically, on the constant C in the
activity bound |rho(gamma)| <= C^{|gamma|} exp(-m |gamma|_t)).

For the CP^2 model, C includes a factor of Vol(CP^2) = pi^2/2 ~ 5
from the target space integration. If C ~ 5, then K ~ ln(5 x 4e) ~ 4.
The condition mL > 4 at the crossover is NOT satisfied (mL ~ 1).

**This is the critical gap.** The cluster expansion may not converge
at the crossover.

**(Gap 2) The derivative bound.**
The bound |dm/dL| <= C_2 m/L is based on dimensional analysis and the
cluster expansion. But at the crossover, where the cluster expansion is
marginally convergent, the bound may not hold quantitatively.

**(Gap 3) Large-N extrapolation.**
At N = infinity, there is no crossover problem: m(L) = Lambda for all L
(Witten 1979). At N = 2 (CP^1), adiabatic continuity is proved. But
N = 3 is in between, and neither the N = infinity simplification nor
the CP^1 integrability applies.


## 5.8 Possible resolutions

**Resolution A: Improved cluster expansion.** Use a MULTI-SCALE cluster
expansion (Brydges-Kennedy, Abdesselam-Rivasseau) instead of a
single-scale one. The multi-scale expansion has better convergence
properties because it separates the contributions at different length
scales. The convergence condition may weaken to m > 0 (not m > K/L).

Status: the multi-scale cluster expansion technology EXISTS (developed
by Brydges, Kennedy, Abdesselam, Rivasseau in the 1990s-2000s for
various constructive QFT problems). Adapting it to the CP^2 model
on R x S^1 is a concrete technical project. [OPEN]

**Resolution B: Use the large-N expansion.** At N = infinity, m(L) > 0
for all L (proved). At finite N, write:

  m(L; N) = m(L; infinity) + (1/N) m_1(L) + (1/N^2) m_2(L) + ...

If the 1/N expansion converges (or is Borel summable) for N = 3, then
m(L; 3) > 0 follows from m(L; infinity) > 0 provided the corrections
are small enough.

Status: the 1/N expansion for the CP^{N-1} mass gap is asymptotic, not
convergent. Borel summability is conjectured but not proved. For N = 3,
the correction terms are O(1/3) ~ 0.33, which is not parametrically
small. [OPEN]

**Resolution C: Direct lattice computation.** For the specific question
"is m(L) > 0 for all L in [L_0, L_1]?", one can in principle compute
m(L) on a lattice for finitely many values of L in [L_0, L_1] and
interpolate.

Status: this is a computational problem, not a theoretical one. Lattice
simulations of the 2D CP^2 model with Z_3 twist are feasible and
have been done (by Bietenholz, de Forcrand, and others). The results
show no phase transition. But lattice results are numerical, not
mathematical proofs. [NUMERICAL EVIDENCE, not proof]

**Resolution D: Anomaly matching.** Use the mixed anomaly between the
Z_3 center symmetry and CP symmetry to constrain m(L). The anomaly
matching condition requires that the vacuum is nontrivial at every L.
If one can show that the ONLY way to match the anomaly with m > 0 is
through Z_3 breaking, and the Z_3 twist already breaks the symmetry,
then m(L) > 0 follows.

Status: the anomaly matching argument constrains but does not determine
the mass gap. It says the vacuum is nontrivial, but "nontrivial" could
mean either gapped (m > 0) or gapless (m = 0 with a CFT). Ruling out
the gapless option at every L is equivalent to the original problem.
[OPEN]


## 5.9 Summary: steps to L = infinity

**What works:**

1. Bootstrap from L_0 (semiclassical) to L ~ 1/Lambda: likely works,
   with O(ln(1/(L_0 Lambda))) steps. The mass gap is growing in this
   regime (from m ~ L Lambda^2 to m ~ Lambda).

2. Bootstrap from L ~ several/Lambda to L = infinity: works easily.
   The mass gap is nearly constant (m ~ Lambda), the steps are large
   (delta ~ L), and finite-L corrections are exponentially small.

**What is hard:**

3. Bootstrap through the crossover L ~ 1/Lambda: the cluster expansion
   may not converge (mL ~ 1), the derivative bounds are uncertain, and
   the constants are not computable analytically.

**The size of the gap:** The interval [c_1/Lambda, c_2/Lambda] for
some constants c_1, c_2 ~ O(1). This is a FINITE interval in L.

**What would close the gap:** A proof that m(L) >= c/L for all L,
with c > K. This is a finite-dimensional inequality (it can be checked
at finitely many values of L by continuity), but proving it analytically
requires non-perturbative control in the crossover regime.
