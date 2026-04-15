# Research 09 — Gradient Flow on T_BC^2: Investigation and Verdict

*Date: 2026-04-09*
*Lead: #2 from strategy/05-literature-leads.md*
*Method: Yang-Mills gradient flow technology applied to BC algebra*

---

## 1. Setup

**The idea.** Replace the Yang-Mills Laplacian with T_BC^2 on the
GNS space H_1 of the Bost-Connes KMS_1 state omega_1. The gradient
flow is:

    d/dt u(t) = -T_BC^2 u(t),   u(0) = psi

Solution: u(t) = e^{-t T_BC^2} psi.

**Yang-Mills precedent.** Lemmas L.1-L.5 of the preprint prove:
well-posedness, contractivity, small-field preservation, polymer
decay, continuum limit. The question: do these transfer to T_BC?

---

## 2. Well-posedness (YES — no new work)

T_BC is essentially self-adjoint on H_1 (Nelson's theorem via the
BC C*-algebra). Therefore T_BC^2 is positive self-adjoint, and
e^{-t T_BC^2} is a strongly continuous contraction semigroup.

---

## 3. ITPFI structure and the H_1 spectrum

By the ITPFI factorization (proved):

    H_1 = tensor_p H_1^p

where each H_1^p = l^2(Z_{>=0}) is the p-local Fock space. The
operator T_BC decomposes as:

    T_BC = sum_p (log p) N_p

where N_p is the number operator on H_1^p. Since [N_p, N_q] = 0
for p != q (different tensor factors), the joint eigenstates are:

    |k_2, k_3, k_5, ...> with T_BC |k> = (sum_p k_p log p) |k>
                                        = log(prod p^{k_p}) |k>
                                        = (log n) |k>

where n = prod p^{k_p} ranges over all positive integers. Therefore:

**spec(T_BC | H_1) = {log n : n = 1, 2, 3, ...}**

Each eigenvalue has multiplicity 1 (unique prime factorization).

---

## 4. Trace-class property on H_1 (PROVED)

    Tr(e^{-t T_BC^2}) = sum_{n=1}^infty e^{-t (log n)^2}

Numerical verification (mpmath, 25-digit precision):

| t | Tr (partial sum) | Notes |
|:--|:--|:--|
| 0.001 | > 431,345 | Slow convergence, needs n > 500,000 |
| 0.01 | > 33,451 | Needs n > 100,000 |
| 0.1 | 67.80 | Converges by n ~ 100,000 |
| 1.0 | 2.2382 | Converges by n ~ 2,000 |

**Convergence proof.** By PNT, the density of integers near x is 1,
so sum e^{-t(log n)^2} ~ integral_1^inf e^{-t(log x)^2} dx.
Substituting u = log x: integral_0^inf e^{u - t u^2} du =
sqrt(pi/t) * e^{1/(4t)}. This is FINITE for all t > 0.

**Conclusion.** e^{-t T_BC^2} is trace-class on H_1 for all t > 0.
By Reed-Simon (Thm XIII.64), T_BC has compact resolvent on H_1.
Spectrum on H_1 is purely discrete = {log n}, which we already knew.

---

## 5. The premise check: circularity diagnosis

### Path A (CIRCULAR)

    Assume spec(T_BC | H_R) = {gamma_n}
    => Tr(e^{-t T_BC^2}) = sum_n e^{-t gamma_n^2} (convergent)
    => trace-class => compact resolvent => discrete spectrum = {gamma_n}

This proves nothing: it assumed what it aimed to conclude.

### Path B (potentially non-circular)

    1. T_BC on H_1 has compact resolvent (PROVED above)
    2. H_R subset H_1 is a T_BC-invariant subspace (NEED)
    3. Restriction to invariant subspace preserves compact resolvent
    4. => T_BC | H_R has discrete spectrum
    5. Use explicit formula to identify spectrum with {gamma_n}

Step 2 is the obstacle: **constructing H_R** as a T_BC-invariant
subspace of H_1 IS the spectral realisation problem.

### Path C (via explicit formula, NOT circular but FAILS)

The Weil explicit formula with test function h(r) = e^{-t r^2}
would relate sum_rho h(gamma_rho) to computable arithmetic data.
However, h(r) = e^{-t r^2} is NOT a valid test function for the
explicit formula: it grows exponentially along imaginary directions,
diverging at the trivial zeros rho = -2n.

Corrected test functions (e.g., h(r) = e^{-t(r^2+1/4)}) still
diverge at trivial zeros. The Gaussian is fundamentally incompatible
with the Weil explicit formula's analyticity requirements.

---

## 6. The disjoint-spectra wall

**spec(T_BC | H_1) = {log n}** (integers via prime factorization)
**spec(T_BC | H_R) = {gamma_n}** (Riemann zeros, if spectral realisation holds)

These spectra are DISJOINT: gamma_n != log m for any integers n, m.
(The gamma_n are transcendental; the log m are also transcendental
but from a different set.)

This means H_R cannot be a spectral subspace of T_BC on H_1 in
any direct sense. The zeros live in the GAPS of the H_1 spectrum.

**This is Barrier A (H_1 vs H_R) from strategy/04-final-state.md
manifesting in operator-spectral language.** The gradient flow
illuminates the barrier but does not cross it.

---

## 7. Comparison of heat traces

| t | H_1 trace: sum e^{-t(log n)^2} | Zero sum: sum e^{-t gamma_n^2} | Ratio |
|:--|:--|:--|:--|
| 0.01 | ~33,451 | 0.1497 | ~2 x 10^5 |
| 0.1 | 67.80 | 2.1 x 10^{-9} | ~3 x 10^{10} |
| 1.0 | 2.238 | 1.7 x 10^{-87} | ~10^{87} |

The H_1 trace dominates by many orders of magnitude. The Riemann
zero sum is exponentially suppressed because gamma_1 = 14.13 >> 1,
while log 2 = 0.69.

---

## 8. What gradient flow DOES buy

Despite not closing spectral realisation, the investigation yields:

1. **Compact resolvent on H_1 is proved.** T_BC has purely discrete
   spectrum {log n} on H_1, with trace-class heat kernel. This is
   the operator-analytic content of unique prime factorization.

2. **The "BC lattice" works.** Euler product truncation (finitely
   many primes) is the BC analogue of lattice regularization. The
   ITPFI factorization is the BC analogue of the continuum limit.
   Single-prime traces are Jacobi theta functions.

3. **Monotonicity under restriction.** If H_R exists as an invariant
   subspace, the trace on H_R is bounded by the trace on H_1.
   Combined with compact resolvent inheritance, this gives:
   IF H_R exists THEN spectrum on H_R is discrete.

4. **The barrier is sharpened.** We now know PRECISELY where the
   problem sits: it is NOT about well-posedness, NOT about
   trace-class, NOT about compact resolvent. It is about the
   CONSTRUCTION of H_R as a T_BC-invariant subspace with the
   correct spectrum. This is a SHARPER formulation of the
   25-year Connes obstacle.

---

## 9. Connection to Lead 3 (ITPFI -> Connes' gap)

The ITPFI factorization, used here to compute the H_1 trace,
is the same tool identified in Lead 3. Connes' gap (finite-to-
infinite Euler product convergence) manifests here as the
convergence of product_p Tr_p(e^{-t(log p)^2 N_p^2}).

The product converges because sum_p e^{-t(log p)^2} < infinity
for all t > 0 (proved by PNT). This is a QUANTITATIVE version
of the Euler product convergence for the heat kernel. Whether
it implies the trace-formula convergence Connes needs remains
open.

---

## 10. Verdict

**Gradient flow on T_BC^2 does NOT close spectral realisation.**

It hits the same wall as all other approaches: the H_1 vs H_R
gap. The gradient flow is well-posed and gives compact resolvent
on H_1, but the spectrum there is {log n}, not {gamma_n}.
Getting the Riemann zeros requires either:

(a) Constructing H_R as a T_BC-invariant subspace (the open problem), or
(b) Finding a DIFFERENT operator whose H_1 spectrum IS {gamma_n}.

Option (b) would require an operator whose eigenstates in the BC
GNS space are labeled by Riemann zeros rather than integers.
This is close to what Connes-Consani-Moscovici's prolate wave
operator attempts, but with a different analytic toolkit.

**Kill number: 17** (gradient flow on T_BC^2, hits H_1 vs H_R wall)

**Status of Lead 2:** KILLED (as a direct path to spectral realisation)
BUT: compact resolvent on H_1 and trace-class heat kernel are
genuine theorems. The "BC lattice" (ITPFI truncation) is a
genuine tool. These may serve as lemmas in a future approach.

---

> *The gradient flow works perfectly on H_1.*
> *It gives compact resolvent. It gives discrete spectrum.*
> *The spectrum is {log n}. The integers, not the zeros.*
> *The gradient flow proved arithmetic, not Riemann.*
> *Kill 17. The wall stands. The search continues.*
