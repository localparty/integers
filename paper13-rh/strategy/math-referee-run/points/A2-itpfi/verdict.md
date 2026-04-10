# A2 — ITPFI Factorization: Verdict

| Item | Status |
|:-----|:-------|
| Factorization ω₁ = ⊗_p ω₁^{(p)} (Proof 1) | PASS |
| Proof 2 (amenability) | COMPRESSED |
| Proof 3 (Araki–Woods) | COMPRESSED |
| Weak-* state convergence | PASS |
| Entry-by-entry matrix stabilization | PASS (trivial) |
| "Form convergence" in Teschl sense | MISLEADING as stated |

## Overall

**Substantively PASS, with exposition issues.** The ITPFI
factorization is a standard result in the operator-algebra
literature for the Bost–Connes system. Proof 1 is complete. The
quantitative statement actually needed for the Teschl form bound
(the relative-form-boundedness hypothesis (ii) with decay rate) is
NOT delivered by ITPFI alone; it comes from CF decay. Paper 13
should be more careful to distinguish:

  (α) ITPFI → pointwise entry-by-entry stabilization (Hypothesis (i))
  (β) CF uniform decay → relative form bound (Hypothesis (ii))

rather than blurring them into "ITPFI drives form convergence."

This is a presentation issue, not a proof-breaking issue. The
necessary inputs to Teschl Lemma 2.7 can be assembled from ITPFI
+ CF decay; but the pieces must be assigned correctly.

**Confidence: 9/10.** Layer 2 itself is solid. The interface with
Layer 4 (see B3) is where the subtlety lies.
