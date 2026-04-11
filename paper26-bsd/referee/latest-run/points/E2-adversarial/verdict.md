# Point E2 — Adversarial review cross-check: Verdict

**Weight:** MEDIUM
**Location in preprint:** §17 + `01-adversarial-proof-review.md`
(internal)
**Overall rigor label:** N/A (meta-check)
**Overall verdict:** Internal review honest; external audit finds
additional issues

## Sub-question verdicts

- **(a) Have the 2 BROKEN items been fixed in the release candidate?**

  **Issue 1 (Conditionality inheritance):**
  - Internal review flagged: paper claimed "unconditional" but
    inherited CBB axiom conditionality.
  - Status in current preprint: **FIXED** — Theorem 9.1 and
    Theorem 13.1 now explicitly state "conditional on the CBB
    axioms (Paper 23)". §9.4 "Gap audit" reframed as conditional.
    See preprint lines 74-79, 360-373, 553-559, 693-696.

  **Issue 3 (Heegner hypothesis + c_2 numerical error):**
  - Internal review flagged: paper claimed c_2 = 1 for y²=x³−x,
    LMFDB says c_2 = 4. Also Heegner hypothesis fails at 2 for
    K = ℚ(i).
  - Status in current preprint: **PARTIALLY FIXED**. c_2 = 4 is
    now stated (preprint line 438: "Tamagawa number at 2 | c_2 |
    4 (LMFDB 32.a3; corrected from earlier draft)"). The BSD
    formula closure is now correct. But the Heegner hypothesis
    resolution is still under-specified: paper mentions both
    Yuan-Zhang-Zhang 2013 AND auxiliary field ℚ(√−7) but does
    not commit. See D3 verdict.

- **(b) Are the 5 WEAKENED items still weak?**

  **Weakened 1 (CM factorization notation):** Still sloppy. Paper
  writes L(E,s) = L(s,χ_K)·L(s,ψ) rather than the standard
  Deuring L(E,s) = L(s,ψ)·L(s,ψ̄). See Point D1.

  **Weakened 2 (Ha-Paugam citation):** Still incomplete. Paper
  should also cite Laca-Larsen-Neshveyev 2015. See Point A1.

  **Weakened 3 (Meyer over Q(i)):** Not strengthened. Paper 3.6
  is still a sketch. See Point A3.

  **Weakened 4 (Twist for L(s,ψ)):** Strengthened via §3.6.1
  (added in the 2026-04-09 revision), which references Connes-
  Marcolli 2008 §4.3 and works through a first-order argument
  for twist insensitivity. But the extension from CM 2008 (stated
  for ℚ) to K is still asserted, not carried out. See Point A3.

  **Weakened 5 (h_K > 1 scope):** Honestly scoped as open in
  §15.4. Not a rigor issue for the stated scope.

- **(c) What did the internal review miss?**

  The external audit (this run) adds the following that were NOT
  in the internal adversarial review's 15 attacks:

  **New Gap G1 — Proposition 4.3 bridge table broken.** The
  internal review did not computationally verify the specific
  Frobenius orders in the worked-example table. The audit's C5
  direct computation finds 3 of 4 rows wrong:
  - k=4 row is mathematically invalid (prime not coprime to
    conductor)
  - k=6 row has wrong Frobenius order
  - (k=2 row was already flagged by the paper's own ERRATUM)

  **New Editorial E1 — Table 8.1 numerical values.** The
  internal review did not check the 30-digit log-ratios in
  Table 8.1. The audit's C3 finds 4 of 5 are wrong (only
  log(5)/log(2) is correct).

  **New Editorial E2 — Ω formula in §13.3.** The formula
  "Ω_E = Γ(1/4)²/(2π)^{3/2}" is off by a factor of π. Correct
  formula: Γ(1/4)²/(2√(2π)).

  **New Concern C — Cohomology class vs representative.** The
  internal review did not scrutinize Proposition 7.3(v)'s
  integrality claim at the level of "does the shift move the
  cohomology class?" This is the single most important missing
  lemma in the audit (Point B2).

  **New Concern D — Inert-prime edge case in Baker Step 5.** The
  internal review did not catch that for inert Gaussian primes
  (norm p²), the exact-promotion argument in §8.3 Step 5 allows
  δ_0 ∈ {−1/4, 0, 1/4}, not just δ_0 = 0. The paper's Step 5
  handles only rational-prime norms.

  **New Observation — Remark 12.6 rank-1 vacuity.** The internal
  review did not emphasize that the paper's own Remark 12.6 makes
  the rank-1 case vacuous within scope. This should be more
  prominent in the paper's framing.

- **(d) Honesty of reported adversarial review outcomes.**
  PASS — the internal review report (research/05) is honest and
  well-structured. The "15 attacks: 8 survived, 5 weakened, 2
  broken" accounting is consistent with what the preprint
  reflects. The fixes to the 2 broken items are in place
  (partially for Issue 3).

## Combined finding

**The internal adversarial review is honest and substantive.**
It caught the two most obvious bugs (conditionality framing and
c_2 numerical error) and flagged the five areas that needed
work.

**But the external audit finds additional issues the internal
review missed**:
1. Proposition 4.3 computational errors (the worked examples
   are broken).
2. Table 8.1 numerical errors (4 of 5 wrong).
3. Ω formula editorial error.
4. The cohomology-class vs representative concern (the most
   important missing lemma).
5. The inert-prime edge case in Baker's Step 5.

The first four are editorial or computational and are bounded
fixes. The fifth (cohomology class) is the load-bearing
mathematical concern.

## Impact on the claimed result

**Moderate.** The internal review's 8/10 conditional confidence
is approximately right in spirit, but the external audit
suggests it may be closer to 6-7/10 as written (similar to
Paper 13's pre-fix state). With focused fixes, it could
return to 8/10.

## Action items

All listed in the relevant point verdicts:
- A1 for Ha-Paugam citation
- A3 for Meyer-Nelson and twist
- B1 for Proposition 4.3
- B2 for cohomology class (the load-bearing one)
- C1 for Table 8.1 and inert-prime edge case
- D1 for §10.2 notation
- D2 for Ω formula
- D3 for Heegner field commitment
