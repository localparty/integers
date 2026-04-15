# Yang-Mills Mass Gap: Submission-Ready Preprint

This directory contains the submission-ready preprint for the Yang-Mills
mass gap proof. All sections are final and self-contained.

The `research/` directory (at the repository root) contains the research
history: exploratory files, superseded drafts, and working documents
that led to the results presented here.


## Reading Order

1. Abstract
2. Introduction (Section 1)
3. Geometric Framework (Section 2)
4. Quantitative Predictions (Section 3)
5. Section 4 -- Lattice Proof
6. Section 5 -- Continuum Limit
7. Section 6 -- Referee Objections
8. Section 7 -- Previous Approaches
9. Conclusion
10. Appendices A--H


## Verification Status

Three analyticity properties of Balaban's construction (formerly marked
[VERIFY]) have been confirmed by explicit argument in the verification
report (`preprint-verification/verify-balaban-items.md`). No new
mathematics is required; each follows from Balaban's published results
(CMP 95--109) by standard functional analysis.

1. **Analyticity of individual polymer activities** -- confirmed: each
   of the four block-spin operations (background evaluation, saddle
   point, Gaussian integration, Mayer resummation) preserves analyticity
   by standard arguments (CMP 95--96, 98, 109; Dimock 2013, Thm 14 for
   the scalar analogue).

2. **k-independence of analyticity radius** -- confirmed: the controlling
   constants ($\kappa$, $m_W$, $C_D$, $r_\mathrm{proj}(N)$) are all
   independent of the RG step $k$ by Balaban's stated inductive
   hypotheses (CMP 109, Section 3).

3. **Exactness of dimension-6 projection** -- confirmed: $S_\mathrm{YM}$
   is the unique local, gauge-invariant, C-even, parity-even dimension-4
   operator on the hypercubic lattice, so Balaban's coupling
   renormalization leaves no dimension-4 contamination in the remainder
   (CMP 109, Section 2).

A referee wishing to verify these points should consult the self-
contained arguments in Appendix H and the verification report, then
check the specific Balaban section references against the published
journal text.
