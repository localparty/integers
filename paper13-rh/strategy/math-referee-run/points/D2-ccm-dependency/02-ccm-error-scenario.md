# D2.02 — What If CCM Has an Error?

## Scenarios

### Scenario A: CCM Theorem 5.10(iii) is wrong in full generality

If the identification "zeros of ξ̂_N = eigenvalues of D_N" fails
as stated, the Hurwitz link fails at its most fundamental step.
Layer 5 is unusable.

**Effect on Paper 13:** complete collapse. Layers 2-4 (our
contributions) give us convergence of some sequence of
operators to some limit operator, but we no longer know that
the limit's spectrum corresponds to Riemann zeros.

### Scenario B: CCM Theorem 5.10 holds only on the full (even+odd) Sonin space, not the even-sector E_N^+

Paper 13's even-sector restriction loses CCM's identification.
The D_N on E_N^+ is now an operator whose spectrum is *not*
identified with {γ_n} via ξ̂_N.

**Effect on Paper 13:** Layer 1 compromised; the Hurwitz argument
cannot start.

**Mitigation:** Paper 13 could abandon the even-sector restriction
and find a different way to satisfy the "even-simple hypothesis".
Currently the paper's AE mechanism requires the even sector, so
this is a significant refactoring.

### Scenario C: CCM Theorem 4.2 fails ("δ_N(ξ) ≠ 0" does not hold)

D' is not self-adjoint at some (λ, N). The T-inner-product
construction degenerates. CCM Theorem 5.10 does not apply.

**Effect on Paper 13:** for the specific (λ, N) where this fails,
the chain is interrupted. If it fails at countably many (λ, N),
the Hurwitz limit can still be taken along a subsequence. If it
fails at a dense set, the limit is undefined.

**Paper 13's acknowledgment:** research/43 labels "δ_N(ξ) ≠ 0" as
"ASSERTED, not proved (severity: LOW)". If the severity is truly
LOW (i.e., it is always nonzero by a simple but unwritten
argument), no effect. If it can fail, the scenario matters.

### Scenario D: CCM Lemma 7.3 holds only on a narrower substrip than stated

The Hurwitz uniform convergence of k̂_λ → Ξ is restricted to
|Im z| < α for some α < 1/2. The Hurwitz argument can still
exclude complex zeros of Ξ in |Im z| < α, but not those with
α ≤ |Im z| < 1/2.

**Effect on Paper 13:** RH is excluded in a strict subset of the
critical strip. This is a partial RH (which is what various
existing "zero-density" theorems already prove).

### Scenario E: CCM's numerical 10^{−55} claim is wrong

This is embarrassing but not proof-breaking. The numerical claim
is motivational; the actual proof uses the a priori O(ρ^{−N})
rate from CCM, not the specific numerical value.

**Effect on Paper 13:** credibility hit. No effect on the
argument.

## Layers 2-6 as a conditional result

Paper 13 Strategy 26 notes "Layers 2-6 are independently at
9-10/10". This would be the standalone statement: "IF operators
D_N with the claimed CCM properties exist, THEN our convergence
argument closes to give spec(D_∞) = {γ_n} and hence RH."

This conditional statement **is** of mathematical interest. Even
if CCM is found to be wrong, Paper 13's Layers 2-6 would
constitute a template for how to close a CCM-like construction.
That is a genuine contribution, separable from Layer 1.

But for the paper to claim RH, Layer 1 must actually hold.

## Verdict on this subpoint

**Paper 13's fate is tied to CCM's fate.** If CCM has any of
scenarios A-D in full severity, Paper 13's proof fails or
degrades. Scenario E is cosmetic.

**Honest mitigation:** Paper 13 should explicitly frame its
theorem as "assuming CCM's construction is correct in the
stated form, the conclusion is RH". This gives credit for the
Layers 2-6 contribution independent of CCM's fate.

As currently written, Paper 13 stakes the unconditional RH
claim on an unrefereed preprint. This is a significant risk
concentration.
