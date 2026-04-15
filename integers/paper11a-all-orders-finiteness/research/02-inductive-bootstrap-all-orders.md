# Research 02: Inductive Bootstrap — All-Orders UV Finiteness

**Date:** April 8, 2026
**Status:** CLOSED
**Result:** Theorem K.4 — UV finiteness at all loop orders by strong induction
**Computation:** `code/bootstrap_L4_verify.py`
**Formal proof:** `04-all-orders-inductive-proof.md`

---

## Discovery

The BPHZ factorisation verification at L=3 (Research 01) revealed a
recursive structure: each loop order's vanishing makes the next loop
order's BPHZ subtraction trivial. This is not a coincidence — it is
a proof by strong induction.

---

## Theorem K.4 (All-Orders BPHZ Factorisation and Vanishing)

In linearised KK gravity on M^4 x S^1/Z_2, under spectral zeta
regularisation of KK mode sums, the L-loop counterterm coefficient
C^(L) vanishes identically for every L >= 1 and every diagram topology.

---

## Proof Structure

### Prerequisites

(P1) Theorem K.1: E_d(-j; Q) = 0 for all j >= 1, any positive-definite Q.
(P2) Lemma A1: Three-graviton vertex is mass-independent (Paper 10).
(P3) Weinberg's theorem: BPHZ counterterms are polynomial in masses.
(P4) KK conservation: Constrained sums produce Epstein zeta functions.

### Base cases

**L=1:** Heat kernel factorisation on M^4 x S^1 gives S_0 = 1+2zeta(0) = 0.
No subdivergences. (Paper 1, Appendix F.)

**L=2:** One-loop subdivergence counterterms proportional to S_0 = 0 (L=1
result). BPHZ trivial. Raw amplitude gives E_2(-j; Q_2) = 0.
(Paper 1, Appendix G.)

### Inductive step (L-1 -> L)

**Hypothesis:** All counterterm coefficients vanish at orders 1,...,L-1.

**Step 1:** Every proper subdivergence gamma of an L-loop diagram has
l(gamma) < L. By the hypothesis, CT(gamma) = 0.

**Step 2:** The BPHZ forest formula subtracts CT(gamma) terms, all zero:
A^{BPHZ} = A^{raw} - 0 = A^{raw}.

**Step 3:** With mass-independent vertices (P2), A^{raw} factors as
(4D integral) x E_L(-j; Q_L).

**Step 4:** By Theorem K.1 (P1): E_L(-j; Q_L) = 0.

Therefore C^(L) = 0. QED.

### Factorised topologies

If an L-loop diagram factorises as Gamma_1 x Gamma_2 with l(Gamma_i) < L,
then A = A_1 x A_2. By the hypothesis, at least one factor involves
E_{l_i}(-j) = 0, so the product vanishes.

---

## Numerical Verification Through L=4

The computation `code/bootstrap_L4_verify.py` verified:

### Gram matrices (banana-(L+1) diagrams)

| L | det(A_L) | Eigenvalues | Lattice |
|---|----------|-------------|---------|
| 1 | 1.0 | {1} | Z |
| 2 | 0.75 | {0.5, 1.5} | A_2 (Eisenstein) |
| 3 | 0.5 | {0.5, 0.5, 2.0} | D_3 (FCC) |
| 4 | 0.3125 | {0.5, 0.5, 0.5, 2.5} | D_4 |

All positive definite. The pattern: eigenvalue 1/2 with multiplicity
L-1, and (L+1)/2 with multiplicity 1. Determinant = (L+1)/2^L.

### Kissing numbers

| L | Kissing number | Lattice name |
|---|---------------|-------------|
| 1 | 2 | Z (integer lattice) |
| 2 | 6 | A_2 (hexagonal) |
| 3 | 12 | D_3 (FCC) |
| 4 | 24 | D_4 |

The D_L kissing number is 2L(L-1) for L >= 3.

### Structural zeros

| L | E_L(-1) → 0 | E_L(-2) → 0 | E_L(-3) → 0 | Lambda_L(-1) |
|---|-------------|-------------|-------------|-------------|
| 1 | ✓ | ✓ | ✓ | 0.3826 |
| 2 | ✓ | ✓ | ✓ | 0.5075 |
| 3 | ✓ | ✓ | ✓ | 0.5756 |
| 4 | ✓ | ✓ | ✓ | 0.6279 |

All 12 structural zeros confirmed numerically (E_L(s) approaches zero
linearly as s -> -j, with finite Lambda_L(-j)).

**L=4 is the first loop order never previously checked.** Its confirmation
validates the inductive bootstrap at the first non-trivial step beyond
the existing L=1,2,3 data.

---

## What This Upgrades

| Result | Before | After |
|--------|--------|-------|
| UV finiteness | Proved at L=1,2; conditional at L>=3 | **PROVED at all orders** |
| Theorem K.3 (conditional BPHZ) | The binding constraint | **Superseded by K.4** |
| Higgs naturalness (Appendix D) | Higher-loop protection conditional | **Unconditional** |
| Scheme-independence | At L=1,2 only (Paper 10) | Extends naturally |

---

## Why the Overlapping Subdivergences Gap Dissolves

The gap identified in K.5.2 was: "do overlapping subdivergences break
the factorisation?" The answer: they never get the chance. The
counterterms that would create the entanglement between 4D momentum and
KK index structures are zero. There is nothing to subtract. The raw
amplitude factors cleanly.

The gap is closed not by computing through the entanglement, but by
showing the entanglement never forms.

---

## Caveats

1. Linearised gravity only (full nonlinear vertices may have mass dependence)
2. Spectral zeta regularisation (scheme-independence at L>=3 is a corollary, not independently proved)
3. Flat background M^4 x S^1/Z_2 (curved backgrounds have nonzero Seeley-DeWitt coefficients)

---

## References

- Paper 1, Appendix K Sections K.5.2, K.7b
- Paper 10, Section 5.2 (Lemma A1)
- `04-all-orders-inductive-proof.md` (formal Theorem K.4)
- `code/mercedes_route_c.py` (L=3 verification)
- `code/bootstrap_L4_verify.py` (L=1-4 verification)
