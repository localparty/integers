# Research 01: Mercedes Route C — BPHZ Factorisation at L=3

**Date:** April 8, 2026
**Status:** CLOSED
**Result:** BPHZ factorisation holds at L=3 by trivial subtraction
**Computation:** `code/mercedes_route_c.py`

---

## Problem Statement

Paper 1 Appendix K Section K.5.2 identified the overlapping subdivergences
gap: at L >= 3, does the BPHZ-subtracted amplitude factorise as
(4D integral) x E_L(-j; Q_L)?

At L=1 and L=2, this was verified by explicit computation (Appendices F
and G). At L >= 3, the factorisation was conditional on Theorem K.3 —
specifically, on whether BPHZ subtraction preserves polynomial KK-mass
dependence in the presence of overlapping subdivergences.

---

## What Was Known Before

1. **Theorem K.1 (Universal Epstein Vanishing):** E_d(-j; Q) = 0 for all
   j >= 1 and any positive-definite Q. Proved in K.7b via 1/Gamma(-j) = 0.

2. **The Mercedes quadratic form:** Q_3(n_1,n_2,n_3) = n_1^2 + n_2^2 + n_3^2
   + n_1 n_2 + n_2 n_3 + n_1 n_3, identified as the D_3 (FCC) lattice.
   Numerically verified: E_3(-j; Q_3) = 0 for j = 1,...,6.
   (File: `etc/12a-three-loop-mercedes-calculation.md`)

3. **Lemma A1 (Paper 10):** The three-graviton vertex on M^4 x S^1/Z_2
   is mass-independent at leading UV order. Three mechanisms:
   (a) UV power counting: V^{d_5}/V^{4D} = O(m_n/k) -> 0
   (b) Z_2 parity: least-suppressed terms projected out
   (c) Epstein backstop: surviving terms have KK sums = 0

4. **L=2 sunset result:** E_2(-j; Q_2) = 6 zeta(-j) L(-j, chi_{-3}) = 0
   for all j >= 1 by complementary zeros.

---

## The Key Insight

The Mercedes diagram at L=3 has three sunset (L=2) subdivergences. Each
sunset subdivergence produces a BPHZ counterterm proportional to
E_2(-j; Q_2). But E_2(-j; Q_2) = 0 by the already-proved L=2 result.

Therefore: **the BPHZ counterterms are zero. Subtraction is trivial.**

    A^{BPHZ}_{Mercedes} = A^{raw} - Sum CT_sunset = A^{raw} - 0 = A^{raw}

The raw amplitude, with mass-independent vertices (Lemma A1), factors as:

    A^{raw} = (4D integral) x E_3(-j; Q_3) = (4D integral) x 0 = 0

---

## Detailed Derivation

### Step 1: Identify subdivergences

The Mercedes diagram at L=3 has the banana-4 topology: 4 propagators
connecting 2 vertices, with 3 loops. The proper subdivergences are:

- Three sunset (L=2) sub-diagrams, obtained by removing one propagator
- Three one-loop sub-diagrams (self-energy insertions)

Each sunset subdivergence gamma has loop order l(gamma) = 2.

### Step 2: Compute subdivergence counterterms

By the BPHZ forest formula, the counterterm for a sunset subdivergence
is the pole part of the L=2 sunset amplitude. This pole part is
proportional to E_2(-j; Q_2) where Q_2 is the Eisenstein lattice form.

From Paper 1, Appendix G:
    E_2(-j; Q_2) = 6 zeta(-j) L(-j, chi_{-3}) = 0 for all j >= 1.

(The complementary zeros of zeta and L cover all negative integers.)

Therefore: CT(gamma) = 0 for each sunset subdivergence gamma.

The one-loop subdivergences contribute counterterms proportional to
S_0 = 1 + 2 zeta(0) = 0 (the L=1 result). These also vanish.

### Step 3: BPHZ subtraction is trivial

The BPHZ forest formula:
    A^{BPHZ} = A^{raw} + Sum_{forests} Product_{gamma} (-CT(gamma))

Since CT(gamma) = 0 for every subdivergence:
    A^{BPHZ} = A^{raw}

### Step 4: Raw amplitude factorisation

With mass-independent vertices (Lemma A1), the Mercedes amplitude is:

    A^{raw} = C^3 x I_{4D}(epsilon) x Sigma'_{n_1+n_2+n_3+n_4=0} f(Q_3(n))

where C = piR/4 (the universal vertex coupling) and I_{4D} is the 4D
momentum integral in dim-reg.

The mass expansion of f gives:
    Sigma'_n Q_3(n)^{-j} = E_3(-j; Q_3)

### Step 5: Epstein vanishing

By Theorem K.1: E_3(-j; Q_3) = 0 for all j >= 1.

Therefore: A^{BPHZ} = 0. The three-loop counterterm coefficient vanishes.

---

## Numerical Verification

The computation `code/mercedes_route_c.py` verified:

1. **Gram matrix:** det(A_3) = 0.5, eigenvalues {0.5, 0.5, 2.0}, positive
   definite. Confirmed.

2. **FCC lattice:** Kissing number r(1) = 12. Representation numbers match
   D_3 sequence: {1, 12, 6, 24, 12, 24, 8, 48}.

3. **Structural zeros:** E_3(s; Q_3) approaches zero linearly as s -> -j
   for j = 1,...,6, with finite residues Lambda_3(-j) matching the values
   from `etc/12a`.

4. **KK conservation identity:** For n_1+n_2+n_3+n_4 = 0:
   n_1^2+n_2^2+n_3^2+n_4^2 = 2Q_3(n_1,n_2,n_3). Verified for five test
   configurations.

5. **Complementary zeros (L=2):** All 10 negative integers checked —
   each has zeta(-j) = 0 (even j) or L(-j, chi_{-3}) = 0 (odd j).

---

## The Bootstrap Discovery

The argument reveals a recursive structure:

    L=1: No subdivergences -> heat kernel factorisation -> S_0 = 0
    L=2: L=1 CTs = 0 -> BPHZ trivial -> E_2(-j) = 0
    L=3: L<=2 CTs = 0 -> BPHZ trivial -> E_3(-j) = 0
    L=k: L<=k-1 CTs = 0 -> BPHZ trivial -> E_k(-j) = 0

This is an induction. See Research 02 for the formal proof.

---

## References

- Paper 1, Appendix F (one-loop computation)
- Paper 1, Appendix G (two-loop computation)
- Paper 1, Appendix K Section K.2 (Mercedes quadratic form)
- Paper 1, Appendix K Section K.5.2 (overlapping subdivergences gap)
- Paper 1, Appendix K Section K.7b (Theorem K.1)
- Paper 10, Section 5.2 (Lemma A1, vertex mass-independence)
- `etc/12a-three-loop-mercedes-calculation.md` (lattice identification)
- `etc/sunset_compute.py` (two-loop code template)
