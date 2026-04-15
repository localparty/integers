# D2.04 — Independence of Layers 2-6

## The claim

Paper 13 Section 13.6 states: "Layers 2-6 are independently at
9-10/10. The floor is Layer 1."

This claims that if CCM is assumed correct, the chain from
ITPFI through Hurwitz is solid. Is that claim accurate?

## Assessment

**Partially.** Let me go layer by layer, assuming CCM holds.

### Layer 2 (ITPFI)

Standalone: the ITPFI factorization of ω_1 is proved and does
not depend on CCM. **Independently 9-10/10.** ✓

### Layer 3 (Estimates)

- Estimate 1 (archimedean): depends on research/20 internal
  notes; the preprint's sketch has inconsistencies. Not fully
  standalone. **7/10 at best.**

- Estimate (b) (eigenvector approximation): uses CCM Lemma 7.2
  (prolate error bound). If CCM holds, Paper 13's Davis-Kahan
  argument gives the rate modulo the gap issue. **6-7/10.**

- Estimate (a) (uniform H¹): Theorem 7.1 has the λ ≤ e^π
  restriction in its proof. At fixed λ = √14 it holds.
  **6-7/10** (at fixed λ).

- CF decay: numerical data at N ≤ 30 supports ρ ≥ 4.27;
  asymptotic uniformity in N is not rigorous. **7/10.**

**Overall Layer 3: 6-7/10**, not 9/10.

### Layer 4 (Teschl-Boegli)

- Teschl Lemma 2.7 application: requires verification that
  Teschl's lemma covers Galerkin sequences on varying Hilbert
  spaces. Not explicitly checked. **6/10.**

- KLMN closability: argument has an incorrect implication
  ("positivity ⇒ closability"). **5-6/10.**

- Bögli Theorem 2.5 application: the self-adjoint specialization
  on varying Hilbert spaces is not explicitly verified against
  Bögli's paper. **6-7/10.**

**Overall Layer 4: 5-6/10**, not 9/10.

### Layer 5 (Hurwitz)

- Uniform convergence ξ̂_N → Ξ on compacts: established via
  CCM Lemma 7.3 + Estimate (b). Depends on CCM; depends on
  Estimate (b). **6-7/10** if CCM holds.

- Hurwitz theorem: classical, correctly stated. **10/10.**

- Final deduction in Sec 10.4: tautological as written. **4/10
  as expressed**; 8-9/10 if rewritten explicitly.

**Overall Layer 5: 5-6/10** as written, 7-8/10 if fixed.

### Layer 6 (Conclusion)

Layer 6 is purely logical: "spec(D_∞) = {γ_n} ⊂ ℝ → γ_n ∈ ℝ".
If the inputs hold, the conclusion follows. **Depends entirely
on the exposition of Section 10.4 being rewritten.**

**Overall Layer 6: depends on Layer 5 being fixed.**

## My conclusion

Paper 13's claim "Layers 2-6 are independently at 9-10/10" is
**overstated**. Layer 2 is solid. Layers 3, 4, 5 each have
concrete rigor and exposition gaps **independent of CCM**. If
CCM is perfectly correct, Paper 13's Layers 2-6 still have
issues that would need resolution.

## The real claim (adjusted)

A more accurate self-assessment of Layers 2-6 independent of
CCM:

| Layer | My rating (assuming CCM holds) |
|:------|:-------------------------------|
| 2 (ITPFI) | 9-10/10 |
| 3 (Estimates) | 6-7/10 |
| 4 (Teschl-Boegli) | 5-6/10 |
| 5 (Hurwitz as written) | 5-6/10 |
| 5 (Hurwitz as intended) | 7-8/10 |
| 6 (Conclusion) | follows from 5 |
| **Independent minimum** | **5-6/10** (Layers 4/5 as written) |

So even assuming CCM is correct, the chain from Layer 2 through
Layer 6 is not 9/10 — it is closer to 6/10.

## What this means

The "CCM preprint is the only real risk" framing in Paper 13
underweights the internal issues. If the authors revise the
preprint to close the Layer 3-5 gaps (which is plausible —
none is definitively fatal), the independent-of-CCM confidence
would rise to 8/10, and the total confidence (including CCM)
would be 7-8/10.

Currently, Paper 13 reads as **Layers 2-6 complete, only CCM
uncertain**. A more accurate reading is **Layers 2-6 have their
own polishing to do, and CCM is on top of that**.
