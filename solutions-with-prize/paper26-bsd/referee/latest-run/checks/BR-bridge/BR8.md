# Check BR8: Integrality is a property of the class, not representative

> **☑ CLOSED 2026-04-10** via `research/cohomology-class-lemma.md`
> (**Key Lemma C**).
>
> The lemma the r01 audit asked for is proved in a form stronger
> than asserted: **for every `δ ≠ 0` in `(−1/2, 1/2)` and every
> `N(𝔭) ≥ k ≥ 2`, `|Δc(δ)| < 1/(k + 1)`**. Since the open interval
> `(−1/(k+1), 1/(k+1))` contains no nonzero multiple of `1/k`, the
> shift is definitely outside `(1/k)ℤ \ {0}`. Equivalently (via
> Hasse–Brauer–Noether): the local Brauer invariant at 𝔭 is
> determined uniquely by the Frobenius action, and any shift of
> the cocycle that does NOT land back in `(1/k)ℤ` simply does not
> correspond to a valid Brauer class of degree `k`. Key Lemma C
> rules out this landing for any `δ ≠ 0`, so the shift is
> incompatible with the cyclic algebra structure.
>
> "**The load-bearing gap**" in the r01 verdict is the gap that
> was closed first this session.
>
> **Final rigor label: [LEMMA].**
>
> Numerical verification: `referee/code/test_projector_P.py` §(d),
> `referee/code/verify_twisted_shift.py`.

---

**Group:** BR
**Source:** BR7 + audit analysis
**Pass criterion:** The shift Δc(δ) produces a change in the
**cohomology class**, not just the cocycle representative.

**Verdict (r01):** **FAIL** — **THE LOAD-BEARING GAP**
**Rigor label (r01):** [KEY LEMMA — OPEN]
**Rigor label (post-closure):** [LEMMA]

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
