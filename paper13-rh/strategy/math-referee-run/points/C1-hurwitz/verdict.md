# C1 — Hurwitz Application: Verdict

| Item | Status |
|:-----|:-------|
| Hurwitz theorem correctly stated | PASS |
| ξ̂_N holomorphic | PASS (entire / meromorphic with real zeros) |
| Ξ not identically zero | PASS (Ξ(0) ≠ 0, cosmetic value error) |
| Uniform convergence on compacts | CONDITIONAL (λ vs N conflation) |
| Real-zero property of ξ̂_N | IMPLICIT — needed, not stated |
| Coverage of all zeros in the strip | PASS |
| Multiplicity preservation (not needed for RH) | PASS |
| The final deduction as written in Section 10.4 | **TAUTOLOGICAL / WEAK** |

## Overall

The Hurwitz application is structurally correct and is the right
way to close this kind of argument. The mathematical content —
uniform convergence of ξ̂_N to Ξ on compacts, with ξ̂_N having
only real zeros, giving reality of all zeros of Ξ in the strip,
hence RH — is sound.

**But the paper does not say this.** Paper 13 Section 10.4 Step 4
concludes "γ_n ∈ ℝ" and invokes a (circular) assertion that only
critical-line zeros contribute to spec(D_∞). The stronger, correct
argument via Hurwitz in the complex plane plus the real-zero
property of ξ̂_N is never explicitly made.

**Required fix:** Rewrite Section 10.4 to explicitly state:

1. **Lemma (real-zero property):** For each N, every complex zero
   of ξ̂_N is real. [Proof: CCM Theorem 5.10(iii) + explicit
   formula for ξ̂_N.]

2. **Main argument:** ξ̂_N → Ξ uniformly on compact subsets of
   {|Im z| < 1/2}. By Hurwitz, every zero of Ξ in the strip is
   a limit of zeros of ξ̂_N. Since each ξ̂_N has only real zeros,
   limits of such zeros are real. Hence every zero of Ξ in the
   strip is real. Translating back via s = 1/2 + iz: every
   non-trivial zero of ζ satisfies Re s = 1/2.

As currently written, the final argument is not a proof. As
reconstructed, it is a proof, conditional on the ingredients
(CCM, Teschl–Bögli, ITPFI, Estimate (b)) being correct.

**Confidence on the Hurwitz step itself: 8/10.**
**Confidence on the exposition as written: 4/10** — the actual
argument is not spelled out; a reader cannot reconstruct it
without doing the work I did here.
