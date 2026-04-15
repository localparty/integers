# B3.08 — Novelty of the Synthesis

## The claim

Paper 13 explicitly emphasizes that the combination ITPFI →
Teschl gsrc → Bögli spectral exactness → Hurwitz has not been
done before. Section 10.7:

> "The synthesis … is the technically novel contribution. No
> prior work has combined these four ingredients. Each ingredient
> is established (ITPFI proved, Teschl published, Bögli published,
> Hurwitz classical); the combination is new and closes the gap
> left open in CCM Section 8."

## Why novelty matters for refereeing

Novel syntheses of established tools sometimes have **interface
gaps** that none of the component papers addresses because none
has exactly this usage in mind:

- **Teschl Lemma 2.7** is a result about a sequence of closed
  semibounded forms on a **common** Hilbert space converging to
  a limit form. Galerkin sequences (varying Hilbert spaces) are
  a generalization that may or may not be covered.

- **Bögli 2017** is a result about non-selfadjoint operators on a
  common Hilbert space. The self-adjoint case is a specialization;
  Galerkin-sequence generalization is another step.

- **Hurwitz** is classical complex analysis, not adapted to
  Fourier transforms of eigenvectors on varying spaces.

At each interface, there is a risk of incompatibility that no
single source addresses.

## Specific interfaces I see

1. **ITPFI (Layer 2) → Teschl (Layer 4).** ITPFI gives entry-by-
   entry matrix convergence on the algebraic direct limit;
   Teschl wants pointwise form convergence on a common form
   domain. The translation involves:
   - upgrading from algebraic direct limit to form domain,
   - verifying uniform relative form bound (separate from ITPFI,
     comes from CF decay),
   - handling the rank-one correction that distinguishes Q_N from
     the base form.

   Paper 13's Appendix C makes this translation implicitly. It is
   not rigorous.

2. **CF decay (Estimate d) → Teschl form bound.** CF decay gives
   Σ |ξ_j| ρ^{−|j|} < ∞, not a form bound. The operator-norm
   bound ‖Δ_N‖ ≤ C ρ^{−N} is an additional step that Paper 13
   attributes to research/40 Lemma 1, not included in the preprint.

3. **Teschl → Bögli.** gsrc from Teschl is used as Bögli's H1.
   Whether Bögli's theorem covers gsrc (as opposed to ordinary
   srg) on varying Hilbert spaces is not verified.

4. **Bögli → Hurwitz.** Bögli gives Hausdorff convergence of
   spectra in compact windows. Hurwitz uses pointwise convergence
   of functions (the Fourier transforms) and conclusions about
   their zeros. The bridge between "Hausdorff-close spectra" and
   "zero set of a function" is CCM Theorem 5.10(iii), which in
   turn is on CCM's preprint authority.

5. **Hurwitz uniform convergence vs Bögli spectral convergence.**
   Hurwitz requires uniform-on-compacts convergence of *the
   Fourier transforms themselves*, not just their zero sets. The
   former is a stronger requirement. Paper 13 claims both, using
   different arguments (Lemma 7.3 for k̂_λ and Estimate (b) for
   ξ̂_λ − k̂_λ).

## Verdict on this subpoint

**Novelty is real, and so is the risk.** Each interface is a
potential gap, and Paper 13 does not close all of them at the
level of rigor that a Clay-millennium proof requires.

The strongest interface concerns (in order):
1. Teschl Lemma 2.7 applied to Galerkin sequences on varying
   Hilbert spaces without explicitly checking Teschl's hypotheses
   in that generality.
2. "Form convergence" conflated with "entry-by-entry matrix
   convergence".
3. The CF-decay → form-bound translation (research/40 Lemma 1)
   not in the preprint.

None of these is definitively fatal, but collectively they
represent about 2–3 points of the 8/10 honest confidence rating.
