# research/01 -- Premise Check: Path A (Chern Character)

*Date: 2026-04-10. Status: PREMISE FAILED (vacuous constraint).*

## 1. The premise

Path A claims: the JLO Chern character ch_n(T_BC) changes when an
off-line zero at delta != 0 is introduced, and the Connes pairing
<ch_n, [e]> = integer forces delta = 0.

## 2. Check 1: Does ch_0 change?

ch_0 = Tr_s(exp(-T^2)) = sum_n sign(gamma_n) * exp(-gamma_n^2).

For on-line zeros, gamma_n come in pairs (gamma, -gamma). Each pair
contributes (+1)*exp(-g^2) + (-1)*exp(-g^2) = 0. Therefore ch_0 = 0
identically by the functional equation symmetry.

An off-line zero at rho = 1/2 + delta + i*t would contribute a
spectral value gamma_* = (rho - 1/2)/i = t - i*delta, which is
COMPLEX. But T_BC is self-adjoint (Stone's theorem), so its spectrum
is real. Adding a complex spectral value destroys self-adjointness.
There is no well-defined "T_BC with off-line zero" in which to
evaluate ch_0.

## 3. Check 2: Is ind_BC(e_N) nonzero for any Hecke projection?

Research/90 proves: ind_BC(e_N) = 0 for ALL Hecke projections e_N.

The mechanism: the supertrace Tr_s(e_N * exp(-t*T^2)) is purely
imaginary at every finite t (because <gamma_n|e_N|gamma_n> and
<-gamma_n|e_N|-gamma_n> are complex conjugates, and the grading
sign flips one). The imaginary part decays exponentially as
t -> infinity. The real part is identically zero.

Numerical verification (30 zeros, 50-digit precision):
- Tr_s at t=0.01: Re=0, Im=-0.057
- Tr_s at t=0.1:  Re=0, Im=-1.08e-9
- Tr_s at t=1.0:  Re=0, Im=-8.79e-88

## 4. Check 3: Are there non-Hecke projections with nonzero index?

Research/48 Section 6.3 (O1) identifies this as an open problem:
finding a projection e in K_0(A_BC) with ind_BC(e) != 0 that is
not a Hecke projection. The rank-one projection P_1 = |gamma_1><gamma_1|
is in the von Neumann completion, not in A_BC^infty.

Without such a projection, the Connes pairing constraint is 0 = integer,
which is trivially satisfied for all delta.

## 5. Verdict

**PREMISE IS VACUOUS.** This is a coboundary-type error:

1. The invariant (ind_BC = 0) does not change under the perturbation
   because it is already zero.
2. The perturbation itself (adding complex spectral values to a
   self-adjoint operator) is ill-defined.
3. The constraint 0 = integer is trivially satisfied.

Path A is BLOCKED unless a non-Hecke projection with nonzero index
is found. This is an open problem in the Connes programme and is
unlikely to be resolved within this cycle.

## 6. Coboundary lesson check

This is structurally identical to the v1 coboundary error:
- v1: H^2(Z/kZ, U(1)) is discrete -> class doesn't change -> vacuous
- v2 Path A: ind_BC = 0 for all known projections -> doesn't change -> vacuous

The mechanism differs (topological vs K-theoretic) but the failure mode
is the same: the invariant is too stable to detect the perturbation.
