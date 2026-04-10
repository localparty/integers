# 217 — RH Cycle 1, Path 3 (Stone) — Construction

*Cycle: 1. Date: 2026-04-09. Agent: Construction.*

---

## Step attempted

**Spectral realisation — reverse inclusion:** Path 3 uses
Stone's theorem (self-adjointness of T_BC implies real spectrum)
combined with spectral realisation (spec(T_BC) = {gamma_n}) to
conclude gamma_n in R. Meyer's theorem [#163] gives inclusion
{gamma_n} subset spec(T_BC). The open step is the reverse:
spec(T_BC) subset {gamma_n}, i.e., no extraneous spectrum.

## Result: BLOCKED

## Analysis

The Stone chain (research/08, #140) is the simplest of the five
paths:

1. **PROVED.** Stone's theorem: if T_BC is self-adjoint on H_R,
   then spec(T_BC) subset R.

2. **PROVED (external).** Meyer 2005 [#163]: the non-trivial
   Riemann zeros are in the spectrum of T_BC.

3. **OPEN.** Reverse inclusion: no extraneous spectrum. This IS
   the spectral realisation conjecture [25.C1, Critical 2].

### The state of the art

The anti-fine-tuning argument (research/201, CV-20) shows:
- P(extra eigenvalue hiding below all 33 error bars) < 10^{-34}
- This is evidence, not proof

The Connes-Marcolli explicit formula (research/201 §5.1) gives:
- Tr_dist(e^{itT_BC}) = sum_rho e^{i gamma_n t} + (smooth terms)
- A proof requires showing the smooth terms contribute no point
  spectrum — i.e., the resolvent (T_BC - z)^{-1} has poles only
  at z = gamma_n

### Why this step is blocked

The reverse inclusion requires proving that T_BC, restricted to
H_R, has pure point spectrum equal to {gamma_n}. The obstacles:

1. **T_BC is distributional** in the Meyer formulation. The
   spectral theorem for unbounded self-adjoint operators requires
   a genuine operator, not a distribution.

2. **The smooth terms** in the explicit formula are not understood
   well enough to rule out additional point spectrum. They include
   contributions from the archimedean place and the trivial zeros.

3. **No uniqueness argument** currently rules out additional
   eigenvalues. The anti-fine-tuning bound (10^{-34}) is
   probabilistic, not deterministic.

### What the catalogue provides

- R-Theorem QM.5 (Stone-von Neumann) [#104]: unique irreducible
  representation of BC Weyl relations at beta = 1. This gives
  uniqueness of the representation, but does not directly
  constrain the spectrum of T_BC within that representation.

- R-Theorem S.7 (Tomita-Takesaki explicit) [#122]: modular
  positivity Delta > 0. The modular operator is related to but
  not identical with T_BC.

- The CM-trace path (Path 5) provides an iff condition [S.5]:
  RH iff non-negative spectral weights. If Path 5 closes, it
  would simultaneously close this step.

### What's needed

Either:
(a) A direct construction of T_BC as a genuine self-adjoint
    operator (not distributional) with the spectral theorem
    applicable, followed by a completeness argument for the
    eigenfunctions, OR
(b) Closing Path 5 (CM-trace / Weil positivity), which would
    give spectral realisation as a consequence.

## Next step

This path is BLOCKED pending spectral realisation. The
recommended attack is via Path 5 (CM-trace), which provides
the iff condition. Cycle 2 should focus on Path 5 first, as
closing it would unblock both Path 3 and Path 1.
