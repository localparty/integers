# D1 — The Assembly: Verdict

## Overall judgment

**The proof chain is structurally complete** in the sense that
each layer is labeled and each tool is identified. The six-layer
architecture is coherent and the tools (ITPFI, CCM, Teschl,
Bögli, Hurwitz) are each applied in a plausibly correct way.

**The proof is not yet a proof**, however, because:

1. The final deduction (Section 10.4 Step 4) is tautological as
   written.
2. Layer 4 has interface gaps that need technical fixes.
3. Several estimates rely on internal research notes not
   included in the preprint.
4. Theorem 7.1's proof only holds for λ ≤ e^π, a restriction not
   discussed in the paper.
5. AE simplicity for N > 20 is heuristic, not theorem.
6. Xi(0) value is stated wrongly (cosmetic but telling).
7. Notational conflation of λ (bandwidth vs spectral parameter)
   obscures uniformity claims.

These are **fixable**. The architecture is right. The execution
is incomplete.

## The single most critical issue

**Section 10.4 Step 4**, where the final deduction is made. It
currently reads as a tautology (concluding that γ_n ∈ ℝ, when
γ_n are defined as imaginary parts of critical-line zeros and
hence trivially real). The correct argument — Hurwitz in the
complex plane applied to ξ̂_N → Ξ, using the real-zero property
of ξ̂_N to force reality of limits — is implicit but never
explicit. This must be rewritten.

## Is it 8/10, as the paper claims?

**The 8/10 rating is slightly generous.** The paper itself
attributes the 2-point gap to CCM preprint status. That accounts
for about 1 point. The other 1 point includes:

- Interface gaps in Layer 4 (worth 0.5-1 point),
- AE simplicity for N > 20 (worth 0.3 point),
- Notational issues (worth 0.2 point).

Additional deductions not accounted for in the 8/10:

- Tautological final deduction (worth 0.5-1 point),
- Broken proof of Theorem 7.1 at λ > e^π (worth 0.3 point),
- KLMN closability misargument (worth 0.2 point),
- Multiple internal-research-note dependencies (worth 0.3 point).

My assessment: **about 6-7/10 as written**, rising to 8/10 if
the most critical exposition fixes are made, and to 9/10 if
CCM is refereed.

## What would close all the gaps

A complete, rigorous, self-contained version would need:

1. **Rewrite Section 10.4 Step 4** with explicit Hurwitz-in-ℂ +
   real-zero-property argument.
2. **State and prove the real-zero property of ξ̂_N** as a
   named lemma.
3. **Include research/40 Lemma 1** (‖Δ_N‖ ≤ C·ρ^{−N}) in the
   paper.
4. **Correct Theorem 7.1's proof** to either restrict to λ ≤ e^π
   explicitly or use a different argument.
5. **Correct the KLMN closability argument** to cite the right
   Reed-Simon result.
6. **Rigorize the Slepian-limit extension** for AE simplicity at
   N > 20.
7. **Disambiguate λ** throughout Sections 5-10 (bandwidth vs
   spectral parameter).
8. **Fix cosmetic Xi(0) errors** in Sec 10.3 and App E.4.
9. **Prove the even-sector restriction compatibility** with CCM
   Theorem 5.10.
10. **Either include research/20, 24, 37 estimates** or replace
    them with proofs in the preprint.

Given the scope of these fixes, the paper is **not refereeable
as-is**. It is in the state of "a promising architecture with
multiple gaps that can likely be closed with further work".

This matches Paper 13's own description of 8/10 confidence,
adjusted downward for the exposition problems that the
internal rating did not catch.
