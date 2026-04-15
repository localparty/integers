# Check BR7: Integrality constraint rigorously established

> **☑ CLOSED 2026-04-10** via `research/cohomology-class-lemma.md`
> (**Key Lemma C**). Elementary bound:
>
> ```
> |Δc(δ)| < 1/(k + 1) < 1/k    for δ ∈ (−1/2, 1/2) \ {0}, N ≥ k.
> ```
>
> Therefore `Δc(δ) ∈ (0, 1/k) ∪ (−1/k, 0)`, which contains no
> nonzero multiples of `1/k`. The integrality premise holds
> unconditionally. Combined with Hasse–Brauer–Noether
> local-global reciprocity, this rules out `δ ≠ 0` at the level
> of the local Brauer invariant.
>
> Verified numerically on all four corrected bridge rows in
> `referee/code/test_projector_P.py` and
> `referee/code/verify_twisted_shift.py` (twisted case with
> Hecke character).
>
> **Final rigor label: [LEMMA].**

---

**Group:** BR
**Source:** Paper 26 §7.3(v)
**Pass criterion:** Δc(δ) ∈ (1/k)ℤ rigorously derived.

**Verdict (r01):** **FAIL** — asserted, not proved
**Rigor label (r01):** [KEY LEMMA — OPEN]
**Rigor label (post-closure):** [LEMMA]

**Justification:** See BR8 for the critical concern. Proposition
7.3(v) says: "The Hasse invariant ... takes values in (1/k)ℤ/ℤ.
The bridge cocycle c_k(δ) = c_k(0) + Δc(δ) must remain in
(1/k)ℤ for the bridge to be well-defined." This conflates the
cocycle representative with the cohomology class. The statement
is about the class; the justification is about the
representative.

**Cross-references:**
- Per-Point: B2
- BR8 (the load-bearing sub-issue)
