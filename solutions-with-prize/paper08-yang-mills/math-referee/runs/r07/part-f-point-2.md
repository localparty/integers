# Referee Report F2: Reflection Positivity - Full Chain

**Classification:** MEDIUM
**Verdict:** SOUND

---

## Overview

Reflection positivity (RP) must hold at three stages: on the lattice for every
spacing a > 0, through the RG flow at intermediate scales, and in the continuum
limit. The preprint uses the KK-enhanced theory with action S_4D (Wilson) +
S_int, where the internal space is CP^{N-1}. This report verifies the full RP
chain.

---

## Sub-point analysis

### (a) Lattice RP for the KK-enhanced theory

Osterwalder-Seiler reflection positivity is established for the standard Wilson
action via the checkerboard decomposition: the action decomposes into
contributions from even and odd time-slabs, and the Boltzmann weight factorizes
in a way compatible with time-reflection. The question is whether the
KK-enhanced action (Wilson + internal coupling) preserves this structure.

The preprint (Appendix D) argues RP via the product manifold lemma: if the
Euclidean spacetime theory on M_1 satisfies RP and the internal space M_2 =
CP^{N-1} is compact with a positive-definite metric, the product theory on
M_1 x M_2 satisfies RP. The argument has three components:

1. The time-reflection theta acts only on the spacetime factor M_1, leaving the
   internal factor M_2 unchanged. Each time-slab of the KK theory factorizes as
   (spatial lattice sites) x (internal connections on CP^{N-1}).

2. The internal action on CP^{N-1} contributes a positive-definite factor to
   the Boltzmann weight, which does not interfere with the reflection structure
   on spacetime.

3. The coupling V_ell between spacetime and internal degrees of freedom respects
   the checkerboard decomposition because V_ell depends only on the link
   variable U_ell and the internal connections at its two endpoints. Since a
   link connecting sites in different time-halves is a "boundary link" that
   appears in both the reflected and unreflected contributions (this is the
   standard Osterwalder-Seiler treatment of boundary links), the coupling term
   preserves the factorization.

The nearest-neighbor structure of V_ell is essential: a non-local coupling could
break the checkerboard decomposition. The preprint correctly restricts to
nearest-neighbor couplings throughout.

**Finding:** SOUND. The product manifold lemma, combined with the
nearest-neighbor structure of V_ell, ensures the checkerboard decomposition is
preserved. The time-reflection acts only on spacetime, leaving the internal
CP^{N-1} factor invariant.

**Impact on the claimed result:** Lattice RP is the starting point for the
entire reconstruction. If it failed for the KK-enhanced theory, the continuum
Hilbert space would not have a positive-definite inner product.

### (b) RP through the RG flow

A potential concern is whether RP must hold at intermediate RG scales. The
effective action S_k at scale k is obtained by integrating out high-momentum
modes, and this integration could in principle break the reflection structure.

The preprint does NOT claim RP for the effective action S_k at intermediate
scales. This is correct and important: the RG flow generates non-local terms in
the effective action (the "E_k" remainder), and these terms generically violate
the checkerboard decomposition needed for RP. Requiring RP at intermediate
scales would be an unnecessarily strong condition.

Instead, the proof uses RP only at two points:

1. On the lattice (for every a > 0), where the full action (before any RG
   coarse-graining) satisfies RP by sub-point (a).

2. In the continuum limit (a -> 0), where RP is recovered by the weak-limit
   argument of sub-point (c).

The RG flow is used only to establish the mass gap and the convergence of the
Schwinger functions, not to preserve RP scale by scale.

**Finding:** SOUND. The proof correctly avoids requiring RP at intermediate
scales, which would be both unnecessary and likely false.

**Impact on the claimed result:** This clarifies the logical structure: RP is an
input (lattice) and an output (continuum), not an intermediate invariant.

### (c) RP in the continuum limit

The continuum Schwinger functions S_n are obtained as weak limits of the lattice
Schwinger functions S_n^{(a)} along a subsequence a_j -> 0. Reflection
positivity for the continuum theory follows from the lower semicontinuity of the
RP condition under weak limits.

The RP condition states: for all Schwartz-class test functions f supported in the
positive-time half-space,

    sum_{m,n} S_{m+n}(theta f_m x f_n) >= 0

where theta is the time-reflection. This is a condition of the form L(S) >= 0
for a continuous linear functional L on the space of distributions. Since
S_n^{(a_j)} -> S_n in the weak-* topology and L is continuous (because
theta f_m x f_n is Schwartz-class and the lattice fields take values in the
compact group SU(N)), the inequality is preserved in the limit.

More precisely: for each finite collection of test functions {f_m}, the quantity
sum S_{m+n}^{(a)}(theta f_m x f_n) >= 0 for all a > 0 (by lattice RP). Taking
the limit a_j -> 0 gives the same inequality for the continuum Schwinger
functions. This is the standard argument (Glimm-Jaffe, Chapter 6).

**Finding:** SOUND. The weak-limit preservation of RP is a standard consequence
of the continuity of the bilinear form in the distributional topology, combined
with compactness of the gauge group.

**Impact on the claimed result:** This completes the RP chain from lattice to
continuum, ensuring the reconstructed Hilbert space has a positive-definite
inner product.

---

## Summary

The reflection positivity chain is sound at all three stages. On the lattice,
the product manifold lemma ensures the KK-enhanced action preserves the
checkerboard decomposition. Through the RG flow, RP is correctly not required at
intermediate scales. In the continuum limit, the standard weak-limit argument
preserves the RP inequality. No gaps are identified.
