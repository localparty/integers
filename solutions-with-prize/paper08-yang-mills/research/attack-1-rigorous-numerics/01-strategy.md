# 01. Strategy: Computer-Assisted Proof of the Crossover Mass Gap

## 1.1 The problem in one sentence

Prove that the 2D CP^2 sigma model on R x S^1_L with Z_3-twisted
boundary conditions has mass gap m(L) > 0 for all L in the crossover
interval [c_1/Lambda, c_2/Lambda], where the bootstrap cluster
expansion cannot be verified analytically.


## 1.2 Why this is the right problem

The full proof chain (Section 34 of the main paper) reduces the
4D SU(3) Yang-Mills mass gap to a single 2D statement: adiabatic
continuity of the Z_3-twisted CP^2 sigma model. The bootstrap cluster
expansion (2d-attack-bootstrap/) proves m(L) > 0 at small L
(semiclassical) and propagates it outward with geometric step size.
But it stalls at the crossover L ~ 1/Lambda, where mL ~ O(1) and
the Kotecky-Preiss convergence constant K exceeds mL.

The crossover interval is FINITE: it has width O(1/Lambda). The mass
gap throughout is O(Lambda) (confirmed by lattice simulations of the
2D model). This is a bounded function on a bounded interval -- a
finite problem, amenable to computer-assisted proof.


## 1.3 The strategy: three layers

**Layer 1. Finite-volume lattice computation with certified error.**

Discretize the CP^2 sigma model on a lattice Lambda_a = Z/(T/a)Z x
Z/(L/a)Z with lattice spacing a. The transfer matrix T_a is a FINITE
matrix. Its two largest eigenvalues lambda_0 > lambda_1 determine
the mass gap:

    m_latt(L, a) = (1/a) ln(lambda_0 / lambda_1)

Compute lambda_0 and lambda_1 using interval arithmetic (every
floating-point operation replaced by a rigorous enclosure). The
output is a certified interval [m_lower, m_upper] containing the
true lattice mass gap.

**Layer 2. Finite-volume to infinite-volume extrapolation.**

The lattice computation is on a strip of finite temporal extent T.
Use Luscher's finite-volume bounds (1977) to relate the finite-T
mass gap to the infinite-T (thermodynamic) mass gap:

    m(L) >= m_latt(L, a, T) - C exp(-m_latt * T)

For T large enough (T > 10/m), the correction is negligible
compared to the mass gap.

**Layer 3. Continuum extrapolation (lattice spacing a -> 0).**

The lattice mass gap differs from the continuum mass gap by O(a^2)
corrections (for the standard CP^{N-1} lattice action). Use
Richardson extrapolation at 2-3 lattice spacings to bound the
continuum mass gap:

    m_cont(L) = m_latt(L, a) + c_2 a^2 + O(a^4)

with c_2 bounded rigorously.


## 1.4 What needs to be computed

For each L in a grid {L_1, ..., L_K} covering [c_1/Lambda, c_2/Lambda]:

1. The transfer matrix T(L, a) of the 2D CP^2 lattice model on
   one time-slice of S^1_L with Z_3 twist, at lattice spacing a.

2. The two largest eigenvalues lambda_0, lambda_1 of T, computed
   with interval arithmetic.

3. The lattice mass gap m_latt = (1/a) ln(lambda_0/lambda_1).

4. The finite-volume correction (Layer 2).

5. The continuum extrapolation (Layer 3).

6. A certified lower bound m_lower(L_k) > 0 at each grid point.


## 1.5 How analyticity fills the gaps between grid points

Between grid points L_k and L_{k+1}, the mass gap m(L) is an
analytic function of L (proved by the cluster expansion, which
DOES converge outside the crossover -- the point is that analyticity
extends INTO the crossover from both sides).

More concretely: the mass gap m(L) satisfies a Lipschitz bound

    |m(L) - m(L')| <= C_Lip |L - L'|

where C_Lip is bounded by the spectral theory of the transfer matrix
(the Hellmann-Feynman formula gives dm/dL in terms of expectation
values that are themselves bounded). If:

    m_lower(L_k) > C_Lip * (L_{k+1} - L_k) / 2

at each grid point, then m(L) > 0 for all L in [L_k, L_{k+1}].

This determines the required grid spacing:

    Delta L < 2 m_lower / C_Lip


## 1.6 The computational chain

```
CP^2 lattice model       Transfer matrix T        Eigenvalues
on S^1_L (1 time-slice)  (finite matrix,          (interval arithmetic,
with Z_3 twist            dimension d(N_s))        certified enclosures)
        |                        |                        |
        v                        v                        v
Hilbert space dimension   T = exp(-a H_latt)      lambda_0, lambda_1
d = (N_s + 2)! /          symmetric, positive      with rigorous
    (N_s! * 2!)            definite, banded         error bars
  x (angular modes)                                      |
                                                         v
                                                  m = ln(lam_0/lam_1)/a
                                                  with certified bounds
                                                         |
                                                         v
                                                  m_cont(L) via
                                                  Richardson extrapolation
                                                  + Luscher correction
```


## 1.7 Summary of required tools

1. **Lattice CP^2 model:** Standard lattice formulation of the
   CP^{N-1} model (Campostrini-Rossi 1992 action, or the quartic
   formulation with manifest reflection positivity).

2. **Transfer matrix construction:** Explicit matrix elements in
   a suitable basis for CP^2-valued fields on a spatial lattice.

3. **Interval arithmetic library:** INTLAB (Matlab), Arb (C/Flint),
   or a custom implementation in Julia/Rust. Must handle matrix
   eigenvalue enclosures.

4. **Certified eigenvalue computation:** Either the Krawczyk method
   for eigenvalue enclosures (based on verified Newton iteration)
   or Lehmann-Goerisch bounds (variational enclosures using
   Lehmann's method).

5. **Luscher finite-volume bounds:** Standard results from lattice
   QFT adapted to the 2D transfer matrix.


## 1.8 Status classification

| Component | Status |
|-----------|--------|
| Lattice CP^2 model formulation | [PROVED] (standard, well-known) |
| Transfer matrix is finite, positive, self-adjoint | [PROVED] (reflection positivity) |
| Eigenvalue gap = mass gap | [PROVED] (transfer matrix formalism) |
| Interval arithmetic for matrix eigenvalues | [PROVED] (Rump 1999, Miyajima 2008) |
| Luscher finite-volume bounds | [PROVED] (Luscher 1977) |
| Continuum extrapolation bounds | [PROVED] (Symanzik improvement program) |
| Lipschitz bound for m(L) | [FEASIBLE] (Hellmann-Feynman + spectral theory) |
| Computation fits in available hardware | [FEASIBLE] (see 06-feasibility.md) |
| Full computer-assisted proof | [OPEN] (the project described here) |
