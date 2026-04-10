# 03. The Cluster Expansion on R x S^1_L

## 3.1 Overview of the strategy

The cluster expansion is a tool from constructive QFT that converts a
mass gap into analytic control over the theory. The logic is:

  m(L) > 0
    => correlations decay exponentially at rate m(L)
    => cluster expansion converges
    => free energy and correlators are analytic in the parameters
    => m(L) is an analytic function of L (in some neighborhood)
    => m(L + delta) can be computed from m(L) by Taylor expansion

This is the engine of the bootstrap: each step extends the domain of
analyticity of m(L) from [0, L] to [0, L + delta].


## 3.2 The lattice regularization

To make the cluster expansion rigorous, we discretize.

**Lattice setup.** Place the Z_3-twisted CP^2 model on a lattice:

  Lambda = a Z_t x (a Z / (N_s a) Z)

where a is the lattice spacing (temporal and spatial), and N_s = L/a is
the number of spatial sites (so the spatial circle has circumference
L = N_s a).

At each site x, the field is z(x) in S^5 subset C^3 (with |z|^2 = 1),
modulo the U(1) gauge equivalence z ~ e^{i alpha} z.

The lattice action is:

  S_lat = -(1/g^2) sum_{<xy>} |z(x)-bar . z(y)|^2

   = -(1/g^2) sum_{<xy>} ( |z-bar_x . z_y|^2 - 1 )  +  const

using the standard CP^{N-1} lattice action (the quartic formulation).

**The twist.** The Z_3 twist is implemented as:

  z(t, x + L) = Omega . z(t, x)

on the lattice. This modifies the spatial links that wrap around S^1_L:
the link from x = (N_s - 1)a to x = 0 includes an Omega insertion.


## 3.3 The transfer matrix

**Definition.** The transfer matrix T_L is the operator on
L^2(Maps(S^1_L -> CP^2)_{Z_3-twisted}) defined by:

  (T_L psi)(phi_1) = integral D phi_0  exp(-S_link(phi_0, phi_1))  psi(phi_0)

where S_link(phi_0, phi_1) is the lattice action for one temporal link
(connecting the spatial configuration phi_0 at time t to phi_1 at time
t + a).

**Properties** [PROVED]:

(a) T_L is a bounded, positive, self-adjoint operator (from the
    Osterwalder-Schrader reflection positivity of the lattice action).

(b) T_L is trace-class (because the target space CP^2 is compact
    and the action is bounded below).

(c) The spectrum of T_L is discrete: eigenvalues lambda_0 > lambda_1
    >= lambda_2 >= ... > 0, with lambda_0 the Perron-Frobenius
    eigenvalue.

**The mass gap and the transfer matrix.**

  m(L) = -ln(lambda_1 / lambda_0) / a

or in the continuum limit:

  m(L) = lim_{a -> 0} [ -ln(lambda_1/lambda_0) / a ]

The condition m(L) > 0 is equivalent to lambda_1/lambda_0 < 1, i.e.,
the transfer matrix has a spectral gap.


## 3.4 The cluster expansion: polymer formulation

We use the polymer (Kotecky-Preiss) formulation of the cluster
expansion. This is the standard tool in constructive QFT for converting
exponential decay into convergent expansions.

**Setup.** Consider the partition function on R_t x S^1_L (after
discretizing time: N_t temporal sites with N_t -> infinity).

Decompose the lattice into temporal slices:

  Lambda = bigcup_{t=0}^{N_t - 1} Sigma_t

where Sigma_t = {t} x S^1_L is the spatial lattice at time t.

**Polymers.** A polymer gamma is a connected subset of the spacetime
lattice Lambda. The polymer activity is:

  rho(gamma) = integral D phi_gamma  prod_{<xy> in gamma}
               (exp(-(1/g^2)|z_x-bar . z_y|^2) - 1)
               x prod_{x in gamma} d mu_{FS}(z_x)

where the product is over links internal to gamma, and d mu_{FS} is the
Fubini-Study measure (Haar measure on CP^2).

Two polymers gamma_1, gamma_2 are INCOMPATIBLE (gamma_1 ~ gamma_2)
if they share a site or are connected by a link.

**The partition function as a polymer gas:**

  Z = sum_{n >= 0} (1/n!) sum_{gamma_1, ..., gamma_n}
      prod_{i<j} (1 - delta(gamma_i ~ gamma_j))
      prod_i rho(gamma_i)

This is an exact rewriting (no approximation).


## 3.5 Convergence of the cluster expansion

**Theorem 3.1 (Kotecky-Preiss criterion).** The cluster expansion
converges absolutely if there exists a function a: Polymers -> [0, inf)
such that for every polymer gamma_0:

  sum_{gamma ~ gamma_0} |rho(gamma)| exp(a(gamma)) <= a(gamma_0)

When this condition holds:
(i)   ln Z is given by a convergent series.
(ii)  All truncated correlation functions are given by convergent series.
(iii) The free energy and correlators are analytic in the parameters
      (coupling g^2, circumference L).

**Proof:** Standard. See Kotecky-Preiss (1986), Friedli-Velenik (2017)
Chapter 5.


## 3.6 Verifying the Kotecky-Preiss criterion

**The key bound: polymer activities are exponentially suppressed by
their size.**

**Lemma 3.2 (Activity bound).** For the Z_3-twisted CP^2 model on
R x S^1_L with mass gap m > 0:

  |rho(gamma)| <= exp( -m |gamma|_t )  x  C^{|gamma|}

where:
- |gamma|_t is the temporal extent of gamma (number of temporal links
  in gamma)
- |gamma| is the number of sites in gamma
- C = C(g^2, L) is a constant depending on the coupling and the
  circumference
- m = m(L) is the mass gap

**Proof sketch.** The activity rho(gamma) involves integrating the
Boltzmann weight over the field configurations on gamma, with the
surrounding fields traced out. The exponential decay in |gamma|_t
comes from the transfer matrix: the contribution of a polymer of
temporal extent T is suppressed by (lambda_1/lambda_0)^T = exp(-m T).

More precisely, insert a complete set of transfer matrix eigenstates
between each temporal slice. The polymer gamma creates an excitation
above the vacuum; this excitation propagates for |gamma|_t time steps,
acquiring a suppression factor exp(-m |gamma|_t). The spatial
integration over the polymer's internal structure gives the factor
C^{|gamma|}.

The constant C depends on the model:

  C = O(1/g^2) x Vol(CP^2) = O(1/g^2) x (pi^2/2)

where Vol(CP^2) = pi^2/2 is the volume of CP^2 with unit Fubini-Study
metric.

[This step is ARGUED, not fully PROVED. Making it rigorous requires
detailed bounds on the transfer matrix spectral decomposition. The
analogous bound IS proved for the CP^1 model by Affleck and others.]


**Lemma 3.3 (Counting bound).** The number of polymers gamma with
|gamma| = n that are incompatible with a fixed polymer gamma_0 is
bounded by:

  #{gamma : |gamma| = n, gamma ~ gamma_0} <= |gamma_0| x (2d)^n x n!

where d = 2 is the spacetime dimension.

In our case (d = 2), the coordination number of the lattice is 2d = 4
(each site has 4 neighbors). The factor |gamma_0| accounts for the
number of sites in gamma_0 where gamma can attach.

**Actually, a tighter bound.** The number of connected lattice animals
of size n containing a fixed site is bounded by (2d e)^n / n in d
dimensions. Using d = 2:

  #{connected gamma containing fixed site, |gamma| = n} <= (4e)^n / n

So:

  #{gamma ~ gamma_0, |gamma| = n} <= |gamma_0| x (4e)^n


**Combining the bounds.** Choose a(gamma) = alpha |gamma| for a
constant alpha > 0 to be determined. The Kotecky-Preiss criterion
requires:

  sum_{gamma ~ gamma_0} |rho(gamma)| exp(alpha |gamma|)
    <= sum_{n >= 1} |gamma_0| (4e)^n exp(-m n_t(n)) C^n exp(alpha n)
    <= alpha |gamma_0|

The critical question is: what is n_t(n), the minimum temporal extent
of a polymer of size n?

**In our geometry R x S^1_L:** A polymer of n sites on the lattice
(Z x Z_{N_s}) has temporal extent n_t >= n / N_s (at minimum, it is a
horizontal strip). But more usefully:

For any polymer gamma, |gamma|_t >= 1 whenever gamma extends in the
temporal direction. The suppression from the mass gap acts on the
temporal extent. For polymers that are purely spatial (a single time
slice), the suppression comes from the spatial mass gap (which equals
the temporal mass gap by the Euclidean symmetry of the action).

**The effective suppression.** For a polymer of size n:

  |rho(gamma)| <= exp(-m x diam(gamma)) x C^n

where diam(gamma) is the diameter of gamma in any direction. Since
diam(gamma) >= c sqrt(n) for a connected polymer in 2D (by the
isoperimetric inequality):

  |rho(gamma)| <= exp(-m c sqrt(n)) x C^n

This is SUPER-exponentially suppressed for large n when m > 0.

**Convergence criterion.** The Kotecky-Preiss criterion is satisfied
when:

  sum_{n >= 1} (4e)^n exp(-m c sqrt(n) + alpha n) C^n < alpha

This converges for any alpha > 0 provided m > 0 (the exp(-m c sqrt(n))
kills the exponential growth of the other factors for large n).

More precisely, convergence holds when:

  m > (1/c) (ln(4e C) + alpha)^2 / (some constant)

i.e., the mass gap must be large enough relative to the coupling
strength.


## 3.7 The key inequality: convergence condition

**Theorem 3.4 (Cluster expansion convergence).** [ARGUED]

The cluster expansion for the Z_3-twisted CP^2 model on R x S^1_L
converges provided:

  m(L) > K / L

where K = K(g^2(1/L)) is a constant that depends on the effective
coupling. In the semiclassical regime:

  K = O(ln(1/g^2))

Specifically:

  K = c_0 ln(C(g^2, L))  where c_0 is a geometric constant.

**Why the condition m > K/L?** The circumference L sets the spatial
extent of the lattice S^1_L. A polymer wrapping around S^1_L has
spatial extent L, so its activity is suppressed by exp(-m L). For the
cluster expansion to converge, we need this suppression to overcome
the entropic factor from counting polymers that wrap:

  exp(-m L) x (# wrapping polymers) < 1

The number of wrapping polymers of temporal extent T is O(exp(const x L))
(since the polymer must extend across L sites). So we need:

  m L > const x L,  i.e.,  m > const

But more carefully, the "const" depends on the coupling through C(g^2, L).

**In the semiclassical regime (small L):**

  m(L) ~ L Lambda^2  (from fractional instantons)
  K/L ~ ln(1/g^2) / L

The condition m(L) > K/L becomes:

  L Lambda^2 > ln(1/g^2) / L
  L^2 > ln(1/g^2) / Lambda^2

Since g^2 ~ 1/ln(1/(L Lambda)), this is:

  L^2 > ln(ln(1/(L Lambda))) / Lambda^2

which is satisfied for L >> (sqrt(ln(ln)) / Lambda, i.e., for L not
too small. At very small L, the KK gap m_KK = 2pi/(3L) >> K/L saves us.

So the convergence condition is satisfied in the semiclassical regime:
m(L) > K/L for all L in (0, L_0]. [ARGUED]


## 3.8 What convergence gives us

When the cluster expansion converges at circumference L:

(1) **Analyticity.** The free energy f(L, g^2) and all connected
    correlators are real-analytic functions of L in a neighborhood of L.

(2) **Mass gap analyticity.** m(L) is a real-analytic function of L
    in a neighborhood of L (because m is determined by the exponential
    decay rate of the two-point function, which is analytic).

(3) **Quantitative control.** The cluster expansion gives explicit
    upper and lower bounds on m(L + delta) in terms of m(L):

      m(L + delta) = m(L) + m'(L) delta + O(delta^2)

    with m'(L) computable from the cluster expansion.

(4) **Absence of phase transitions.** A convergent cluster expansion
    EXCLUDES phase transitions. Since m(L) is analytic, it cannot
    jump discontinuously or touch zero (unless it is identically zero
    in a neighborhood).


## 3.9 The connection to the bootstrap

The cluster expansion gives us a MACHINE:

  INPUT:  m(L) > 0 at some value L
  OUTPUT: m(L') > 0 for L' in (L - delta, L + delta)

with delta determined by the radius of convergence of the analytic
continuation. The bootstrap iterates this machine:

  m(L_0) > 0  =>  m(L_1) > 0  =>  m(L_2) > 0  =>  ...

where L_{n+1} = L_n + delta_n.

The question is: does sum_n delta_n = infinity (reaching L = infinity)?
Or does sum_n delta_n < infinity (getting stuck at some finite L*)?

This is analyzed in Sections 04 and 05.
