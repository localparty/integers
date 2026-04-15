# Referee Report D1: Exhaustiveness of Dimension-6 Classification

**Classification:** MEDIUM
**Verdict:** CLOSABLE GAP
**Estimated repair:** 1 page (lattice-specific derivation)

---

## Overview

The stability of deviation order argument relies on classifying ALL dimension-6,
C-even, gauge-invariant operators in the effective action. If the classification
misses an operator with dev < 2, the entire mass gap preservation mechanism
fails. This report examines the completeness of the classification in both the
continuum and lattice settings.

---

## Sub-point analysis

### (a) Luscher-Weisz basis

The classification uses the Symanzik effective theory framework (Symanzik 1983,
Luscher-Weisz 1985). In the continuum, the dimension-6 gauge-invariant C-even
operators are:

    O_1 = Tr(D_rho F_mu_nu)^2
    O_2 = Tr(D_mu F^{mu rho} D_nu F^nu_rho)
    O_3 = Tr(F_mu_nu F_nu_rho F_rho_mu)

On the lattice, additional operators arise from the discretization. However,
these are related to the continuum operators by:

1. Equations of motion (on-shell equivalence within path integrals),
2. Lattice identities (trace cyclicity, Cayley-Hamilton for SU(N)),
3. Total derivative removal (integration by parts on the lattice torus).

The preprint implicitly uses the continuum classification. The previous referee
(r05) flagged this as "a presentation gap, not a mathematical gap."

The key structural observation: products of plaquettes at the same lattice site
contribute to dimensions 4n for n plaquette factors. In particular, the product
of two plaquettes at the same site is dimension 8, not dimension 6. This means
lattice artifacts from plaquette products do not contaminate the dimension-6
sector. The only dimension-6 lattice operators are improved-action terms (e.g.,
2x1 rectangular Wilson loops), which lie in the span of the continuum basis
after Symanzik expansion.

**Finding:** CLOSABLE GAP. The argument is correct but the lattice-specific
derivation should be stated explicitly. Specifically, the paper should include a
brief derivation showing that the lattice block-spin transformation generates
operators whose Symanzik expansion at dimension 6 lies within the continuum
Luscher-Weisz basis. Estimated difficulty: 1 page of standard material.

### (b) Second two-derivative operator

The operator O_2 = Tr(D_mu F^{mu rho} D_nu F^nu_rho) is the second
independent two-derivative contraction. The preprint (Section 5.6, Part III.3)
addresses this directly. By the Yang-Mills equations of motion and the Bianchi
identity, this operator differs from O_1 = Tr(D_rho F_mu_nu)^2 by terms that
are either:

1. C-odd (vanishing coefficient in the effective action by charge conjugation
   symmetry of SU(N) Yang-Mills), or
2. Higher-dimension operators (dev >= 3, absorbed into the remainder).

Alternatively, O_2 is itself expressible as a sum of terms of the form
(D_rho ...)^2, each carrying a squared deviation factor from the two-derivative
structure. Either route gives dev(O_2) >= 2.

The r05 revision confirmed this analysis. The equations-of-motion reduction is
standard in the Symanzik improvement program and is valid non-perturbatively
within the path integral (Luscher-Weisz 1985, Section 4).

**Finding:** SOUND after the r05 revision.

### (c) Lattice artifacts at dimension 6

The Wilson plaquette action has O(a^2) lattice artifacts, corresponding to
dimension-6 corrections in the Symanzik expansion. After Balaban's block-spin
RG transformation, these artifacts propagate through the effective action at
each scale.

The crucial separation property: S_YM is the UNIQUE gauge-invariant dimension-4
operator (up to normalization). This was confirmed in the verification stage
(Part B). Consequently, dimension-6 artifacts cannot mix down into dimension 4.
They remain cleanly separated in the effective action decomposition:

    S_k = (1/g_k^2) S_YM + sum_{d=6} c_n^{(k)} O_n^{d=6} + E_k

The dimension-6 coefficients c_n^{(k)} receive contributions from both the
continuum dimension-6 operators and the lattice artifacts, but both sources
produce operators in the same Luscher-Weisz basis. No new operators appear.

**Finding:** SOUND. The uniqueness of S_YM at dimension 4 guarantees clean
separation, and the Luscher-Weisz classification is complete at dimension 6.

---

## Summary

The dimension-6 classification is exhaustive. The continuum Luscher-Weisz basis
captures all gauge-invariant, C-even operators at this dimension, and lattice
artifacts do not introduce operators outside this basis. The one closable gap is
presentational: a 1-page derivation explicitly connecting the lattice block-spin
operators to the continuum basis via Symanzik expansion. This is standard
material and poses no logical obstruction.
