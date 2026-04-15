# B1.03 — The Implied Constant

## Question

Is the implied constant in O(1/λ) effective? Does it depend on N?

## Finding

Paper 13 Section 6.2 gives an explicit constant:

  ‖τ^{(ℝ)}‖_op ≤ 5.5,  gap(T_0) ≥ C'' · λ.

The "5.5" is cited to Estimate 1 (research/20, "closed"). The
paper offers no derivation of this specific value in the
preprint itself; it is taken from an internal note.

The constant C'' in the gap bound is described as "an explicit
constant C'' > 0 depending only on the truncation geometry"
(Section 6.2, after Eq 6.6). "Depending only on the truncation
geometry" is **not an effective statement**. It doesn't give a
numerical value and doesn't make the N-dependence explicit.

The paper further cites "research/24, verified at all tested
truncation levels" for the claim that the relative gap μ_1/μ_2 is
stable in N. "Verified at all tested truncation levels" is
numerics, not a proof.

## Assessment

- **‖τ^{(ℝ)}‖_op ≤ 5.5**: plausible but inherited from research/20.
  No derivation in the paper.

- **gap(T_0) ≥ C'' · λ**: plausible shape but C'' is not numerical
  and its N-dependence is not tracked.

- **μ_1/μ_2 ≈ 10^{−6} stable in N**: numerical observation; not a
  theorem.

All three items are characterized as "closed" in the paper's
internal grading system, but "closed" seems to mean "verified in
internal research notes" rather than "proved rigorously in a form
a referee can independently check".

## Verdict on this subpoint

**Not effective.** The constant is opaque to external verification.
The proof relies on internal research notes (20, 24, 37) whose
status is not clear from the preprint.

**Required fix:** state the constants numerically, with a one-line
derivation, and track their N-dependence explicitly. This is
standard analytic-estimate hygiene.
