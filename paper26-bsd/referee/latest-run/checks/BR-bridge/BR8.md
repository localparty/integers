# Check BR8: Integrality is a property of the class, not representative

**Group:** BR
**Source:** BR7 + audit analysis
**Pass criterion:** The shift Δc(δ) produces a change in the
**cohomology class**, not just the cocycle representative.

**Verdict:** **FAIL** — **THE LOAD-BEARING GAP**
**Rigor label:** [KEY LEMMA — OPEN]

**Justification:** This is the single most important missing
lemma in the audit. The precise required statement is:

> *Let β(δ) ∈ Z²(ℤ/kℤ, U(1)) be the cocycle representative
> obtained from the spectral shift at parameter δ. Define the
> class map [·] : Z²(ℤ/kℤ, U(1)) → H²(ℤ/kℤ, U(1)) ≅ ℤ/kℤ.
> Then [β(δ)] ≠ [β(0)] for δ ∈ (−1/2, 1/2) \ {0}.*

Paper 26 does NOT state, prove, or acknowledge this lemma. Without
it, Baker's kill argument (§8.3) operates on a premise that may
not hold: a continuous shift of the cocycle representative may
be absorbable by a coboundary, leaving the class unchanged, and
the integrality constraint trivially satisfied.

**If the lemma is true**: the paper should prove it explicitly,
probably via a concrete H² calculation.

**If the lemma is false**: the entire bridge mechanism collapses
and the paper needs a different invariant.

**Effect on proof chain:** **Maximum**. This is the single item
whose resolution determines whether the BSD proof chain is
rigorously complete.

**Cross-references:**
- Per-Point: B2
- rigorous-proof.md §XIII Key Lemma C
