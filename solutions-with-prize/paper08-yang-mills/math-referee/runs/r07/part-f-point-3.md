# Referee Report F3: Thermodynamic Limit

**Classification:** MEDIUM
**Verdict:** CLOSABLE GAP
**Estimated repair:** 1 paragraph (volume cancellation lemma)

---

## Overview

The mass gap is first established on a finite torus (Z/LZ)^4 and then extended
to infinite volume L -> infinity. The critical issue is whether the bounds
obtained on the finite torus are uniform in L, so that the mass gap survives the
thermodynamic limit. This report examines the volume-independence of the RG
bounds, the infinite-volume mass gap, and exponential clustering.

---

## Sub-point analysis

### (a) Uniformity in L of the RG step bound

The RG recursion bound |C_{k+1}(L) - C_k(L)| must be independent of the
spatial volume L^3 for the inductive argument to extend to infinite volume. The
preprint uses the connected matrix element <1|E_k(0)|1>_c to control each RG
step, where |1> is the first excited state at momentum p = 0.

The volume-independence of the connected matrix element arises from a standard
cancellation in lattice field theory. The state |1> at zero spatial momentum is
delocalized over the entire spatial volume with normalization factor 1/L^{3/2}.
The operator E_k(0) = sum_x E_k(x) involves a sum over all spatial sites. The
matrix element therefore contains:

    <1|E_k(0)|1>_c = (1/L^3) sum_{x,y} <1_x|E_k(0)|1_y>_c

The connected part of the correlator <1_x|E_k(0)|1_y>_c decays exponentially
in |x - y| (by the mass gap), so the double spatial sum produces a factor of
L^3 from the diagonal and near-diagonal terms, which exactly cancels the
1/L^3 prefactor from the delocalization. Off-diagonal terms contribute
exponentially small corrections O(e^{-Delta L}).

This cancellation is the statement that the connected matrix element is an
intensive quantity: it measures the per-site contribution after vacuum
subtraction. This is standard in lattice field theory, but the preprint does not
state it as a lemma or provide the cancellation argument.

**Finding:** CLOSABLE GAP. The volume cancellation is standard and correct, but
should be stated explicitly as a lemma with the cancellation argument above.
Estimated difficulty: 1 paragraph.

**Impact on the claimed result:** Without uniformity in L, the RG recursion
bounds could degrade with volume, potentially allowing the mass gap to vanish in
the thermodynamic limit. The cancellation ensures volume-independence and is
essential for the argument.

### (b) Infinite-volume mass gap

For fixed lattice spacing a, the finite-volume mass gap Delta(a, L) converges
to the infinite-volume mass gap Delta(a, infinity) as L -> infinity. The rate
of convergence is exponentially fast:

    |Delta(a, L) - Delta(a, infinity)| = O(e^{-Delta L})

This exponential convergence follows from the exponential decay of correlators
in a gapped theory: the finite-volume corrections to the spectral gap come from
"wrapping" contributions where correlations propagate around the torus, and
these are suppressed by e^{-Delta L}.

The convergence is uniform in a because the mass gap Delta is bounded below
uniformly in a (this is the content of the RG argument in the preceding
sections). Specifically, Delta(a) >= Delta_min > 0 for all a in (0, a_0], so
the exponential convergence rate e^{-Delta_min L} is uniform.

**Finding:** SOUND. The exponential convergence in L and its uniformity in a
follow from standard estimates in gapped lattice systems.

**Impact on the claimed result:** This establishes that the mass gap persists in
infinite volume for each fixed a, which is a necessary input for the subsequent
continuum limit a -> 0.

### (c) Exponential clustering in finite volume

Exponential clustering (exponential decay of connected correlators) in finite
volume on (Z/LZ)^4 is the input needed for sub-point (b). The cluster expansion
from Part B provides this: for L sufficiently large (L >= L_0 where L_0 depends
on the mass gap scale but not on a), the connected correlators satisfy

    |<O(x) O(y)>_c| <= C exp(-Delta |x - y|)

where the distance |x - y| is the torus distance (minimum over periodic images).

The spectral gap between the ground state energy E_0 and the first excited state
energy E_1 is bounded below uniformly in L for L >= L_0. This is a standard
consequence of the cluster expansion: the expansion provides control over the
transfer matrix, and the gap between E_0 and E_1 is determined by the decay
rate of the connected two-point function, which is L-independent (up to
exponentially small corrections from the periodic boundary conditions).

For L < L_0, the finite-volume system has finitely many degrees of freedom
(for fixed a) and the spectral gap is trivially positive (it is a finite
matrix). The uniformity in a again follows from the RG bounds.

**Finding:** SOUND. The cluster expansion provides the exponential clustering
needed for the thermodynamic limit, with bounds that are uniform in L for
L >= L_0.

**Impact on the claimed result:** Exponential clustering is the bridge between
the finite-volume spectral gap and the infinite-volume mass gap. Without it,
the finite-volume gap could close as L -> infinity.

---

## Summary

The thermodynamic limit argument has one closable gap: the volume cancellation
in the connected matrix element <1|E_k(0)|1>_c should be stated as an explicit
lemma showing that the delocalization factor 1/L^{3/2} cancels with the spatial
sum to produce a volume-independent bound. This is standard material requiring
1 paragraph. The infinite-volume mass gap convergence and finite-volume
exponential clustering are both sound.
