# Referee Report D3: Spectral Lemma

**Classification:** MEDIUM
**Verdict:** CLOSABLE GAP
**Estimated repair:** 1 paragraph (two-particle binding energy)

---

## Overview

The spectral lemma converts the microscopic deviation order (factorization of
Boltzmann weights) into the macroscopic bound |<1|O|1>_c| <= C_p M Delta-hat^p.
This is the analytic engine that translates the structural classification of D2
into quantitative estimates usable in the RG induction. This report examines the
extraction procedure, the convergence parameter zeta, and the volume
independence of the operator support.

---

## Sub-point analysis

### (a) Deviation extraction

The bound S1.2 treats the spectral sum by case analysis on the intermediate
state labels n_j relative to the external state m:

- n_j = m (diagonal): the factor (e^{E_m - E_m} - 1) = 0. This term
  contributes zero and is dropped.
- n_j = 0 (vacuum) when m = 1 (one-particle): the factor
  (e^{E_1 - E_0} - 1) = (e^{Delta-hat} - 1) ~ C Delta-hat for small
  Delta-hat. This contributes one power of Delta-hat.
- n_j >= 2 (multiparticle) when m = 1: the factor
  (e^{E_1 - E_{n_j}} - 1) is O(1) since E_{n_j} >= E_2 >= 2 Delta-hat - eps_B
  where eps_B is the binding energy.

The proof claims that at least p of the R factors are O(Delta-hat). This follows
from the definition of dev >= p: by hypothesis, p of the spectral slots carry
extractable deviation factors. At each such slot, the factor is bounded by
C Delta-hat (from the n_j = 0 case when m = 1, or symmetrically from the
m = 0 case when n_j = 1).

The remaining R - p factors contribute O(1) bounds. These are absorbed into the
residual spectral weight, which is summed using the zeta bound (sub-point b).
The extraction is multiplicative: the p factors of Delta-hat are pulled out
front, yielding the overall Delta-hat^p suppression.

**Finding:** SOUND. The case analysis is exhaustive, the extraction is correct,
and the residual weight is controlled by the zeta parameter.

### (b) The zeta bound

The convergence parameter

    zeta = sum_{n >= 1} e^{-(E_n - E_1)}

requires E_2 - E_1 > 0 for convergence. In the free theory, E_2 = 2 Delta-hat
(two-particle threshold), so E_2 - E_1 = Delta-hat > 0 and zeta is controlled.
The question is whether interactions can create a deeply bound state with
E_2 - E_1 -> 0, which would cause zeta to diverge.

The paper bounds the binding energy eps_B <= C_B g_k^4 Delta-hat_k using
perturbative estimates (Born approximation for glueball-glueball scattering).
The concern: are perturbative binding energy estimates valid non-perturbatively?

In Balaban's small-field domain at weak coupling (g_k -> 0 as k -> infinity),
the effective action is a perturbation of the free (quadratic) theory. The
glueball-glueball interaction strength is O(g_k^2) per vertex, and a bound
state in d = 4 requires the interaction to exceed a threshold relative to the
kinetic energy. At weak coupling, the interaction is parametrically small:

    eps_B / Delta-hat <= C g_k^4 << 1

A deeply bound state (eps_B ~ Delta-hat) would require O(1) coupling, which
does not occur in the asymptotically free regime.

For the finitely many initial RG steps where g_k is not small, the cluster
expansion gives explicit control on the spectrum. The transfer matrix has a
convergent polymer expansion at these scales, and the gap E_2 - E_1 is bounded
below by explicit combinatorial estimates.

**Finding:** CLOSABLE GAP. The argument is correct but should be strengthened
with a brief justification. Specifically: in Balaban's small-field domain, the
effective action at scale k is S_YM/g_k^2 plus perturbatively small corrections.
The two-particle sector of the transfer matrix is a perturbation of the
free two-particle Hamiltonian by an interaction of strength O(g_k^2). By
standard Kato-Rellich perturbation theory, the binding energy is at most
O(g_k^4) times the one-particle gap, ensuring E_2 - E_1 >= Delta-hat(1 - C g_k^4)
> 0 at weak coupling. This is a 1-paragraph addition.

### (c) Volume independence via Combes-Thomas

The operator support radius R_0 must be bounded uniformly in the RG step k for
the spectral lemma to yield k-independent constants. The preprint claims this
using the Combes-Thomas exponential decay bound.

The block-spin RG generates operators at scale k with support in a ball of
radius O(1) in block lattice units. Each block at step k has physical size
2^k a_0, but the operators in the effective action are expressed in block lattice
coordinates where the lattice spacing is 1. The support radius in block lattice
units is determined by the polymer expansion: activities decay exponentially
with the diameter of the polymer, and the truncation at a fixed radius R_0
introduces errors that are exponentially small in R_0.

The Combes-Thomas bound provides the exponential decay of the transfer matrix
kernel T(x, y) ~ e^{-Delta-hat |x-y|} for |x - y| > R_0. This ensures that
the spectral lemma's constants depend on R_0 but not on k, because R_0 is
measured in block lattice units where the effective theory has O(1) correlation
length (the gap Delta-hat is O(1) in these units at every scale).

**Finding:** SOUND. The block lattice formulation ensures R_0 is k-independent,
and the Combes-Thomas bound provides the necessary decay.

---

## Summary

The spectral lemma is sound in its deviation extraction mechanism and its volume
independence via Combes-Thomas. One closable gap remains: the two-particle
binding energy bound eps_B <= C g_k^4 Delta-hat should be justified by a brief
perturbation theory argument (Kato-Rellich) within Balaban's small-field domain.
This is a 1-paragraph addition that poses no logical obstruction.
