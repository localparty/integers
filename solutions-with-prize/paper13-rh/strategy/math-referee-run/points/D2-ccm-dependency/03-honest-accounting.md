# D2.03 — The 8/10 Honest Accounting

## Paper 13's self-assessment

Section 13.6:

| Layer | Confidence | Limiting factor |
|:------|:-----------|:----------------|
| 1 (CCM operators) | 8/10 | Preprint, not yet refereed |
| 2 (ITPFI) | 10/10 | Proved 3 ways |
| 3 (Estimates) | 9/10 | Closed, verified |
| 4 (Boegli: gsrc + H2) | 9/10 | Teschl fix applied |
| 5 (Hurwitz) | 9/10 | Uniform convergence from (b) + Lemma 7.3 |
| 6 (Conclusion) | follows | From Layers 1-5 |
| **Overall** | **8/10** | **Layer 1 (CCM preprint)** |

## My assessment of this rating

**Layer 1: 8/10.** Paper 13 assigns 8/10 to CCM preprint status.
Independent verification of CCM's 5.10 parts and the
even-sector compatibility would raise this. I would rate it
**7/10** because the even-sector modification is an additional
unverified step, not already in CCM.

**Layer 2: 10/10.** ITPFI factorization is solid. I agree with
9-10/10.

**Layer 3: 9/10.** Paper 13 rates the estimates at 9/10, but I
find several issues:
- Theorem 7.1 proof breaks for λ > e^π (computational check).
- Eigenvector approximation has a wrong PNT-tail estimate.
- Constants are inherited from internal research notes.
I would rate Layer 3 at **6-7/10** as written.

**Layer 4: 9/10.** Paper 13 rates the Boegli-Teschl synthesis at
9/10 with "Teschl fix applied". I find:
- Teschl Lemma 2.7 application to Galerkin sequences is not
  rigorous.
- KLMN closability is argued via an incorrect implication.
- ‖Δ_N‖ ≤ C·ρ^{−N} depends on research/40 Lemma 1 not in paper.
I would rate Layer 4 at **6/10**.

**Layer 5: 9/10.** Paper 13 rates Hurwitz at 9/10. I find:
- The uniform-on-compacts convergence is established in λ, not
  clearly in N.
- The final deduction in Section 10.4 is tautological; the
  correct argument (Hurwitz + real-zero property) is implicit.
I would rate Layer 5 at **5-6/10** as currently expressed.

**Overall:** roughly **6-7/10** as written (the minimum of the
layer ratings), not 8/10.

## Where my rating differs from Paper 13's

Paper 13 rates Layers 2-6 at 9-10/10, meaning the authors
believe these are essentially complete. My assessment is that
Layers 3, 4, and 5 each have specific rigor gaps that the
paper's own rating does not reflect. These are not issues of
"hedging against unknowns"; they are concrete technical and
exposition items I identified in this review.

The paper's 8/10 rating is driven entirely by "CCM preprint"
concerns. I agree that CCM is a real risk, but I think the
other layers also have concrete, fixable issues that the
self-rating underweights.

## Is this a problem?

**Self-rating is always difficult.** Authors are close to their
own work and may not see issues that a fresh reader catches. The
paper's self-rating is not dishonest — it is plausibly what the
authors believe. But it is **optimistic**.

A fair external rating would be closer to:

- **6/10** as written (the current state of the preprint).
- **8/10** if the exposition is fixed and the technical gaps I
  listed (Section 10.4 rewrite, Theorem 7.1 restatement, KLMN
  fix, research/40 Lemma included, Slepian rigorization) are
  all resolved.
- **9/10** if CCM is refereed.
- **10/10** if everything above plus independent third-party
  verification of Layers 2-6.

## Verdict on this subpoint

The paper's "honest 8/10" is **approximately right in spirit**
(there are real gaps, and the gaps are manageable in principle)
but **wrong in specifics** (the gaps are not only about CCM's
status; they include concrete rigor and exposition issues in
Layers 3-5). A more accurate rating is 6-7/10 as written,
rising to 8/10 after focused revision, rising to 9/10 after
CCM is refereed.
