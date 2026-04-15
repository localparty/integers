# Point C1 — Baker's theorem application: Verdict

**Weight:** HEAVY
**Location in preprint:** §8
**Overall rigor label:** **[LEMMA]** (conditional on integrality
premise B2)
**Overall verdict:** PASS at the transcendence level, **DEPENDENT
on Point B2** for the premise, plus editorial concerns

## Sub-question verdicts

- **(a) Baker's theorem statement.** [THEOREM] — Baker 1966 is
  correctly stated (Theorem 8.1) and correctly applied (log α
  irrational / transcendental for distinct algebraic α, β ≠ 0).

- **(b) Linear independence of logarithms.** [THEOREM] — For
  distinct positive integer prime norms N_1 ≠ N_2, the ratio
  log N_1 / log N_2 is irrational (by unique factorization,
  elementary). Baker upgrades this to transcendence.

- **(c) Is Baker actually needed?** EDITORIAL — the paper's own
  §8.5 admits: "The upgrade from Gelfond–Schneider to Baker is a
  convenience (cleaner statement over number fields), not a
  necessity. The proof would go through with Gelfond–Schneider
  alone." Baker is used for rhetorical symmetry with the RH case,
  not for genuine mathematical need. Not a concern at the rigor
  level.

- **(d) The formal kill — rigorous version.** **[LEMMA]**
  (conditional on B2) — the paper's argument:
  (i) If δ ≠ 0, the integrality constraints at two distinct
      prime norms impose m_1 log N_1 = m_2 log N_2 for some
      nonzero integers m_1, m_2.
  (ii) Baker/unique factorization forces m_1 = m_2 = 0.
  (iii) The only way is δ = 0.
  This chain is rigorous given (i) — but (i) depends on the
  integrality constraint being valid, which is Point B2's
  cohomology-class lemma. If B2 is [KEY LEMMA — OPEN] / GAP,
  then C1's "formal kill" operates on an unproven premise.

- **(e) Exact vs first-order.** [LEMMA] (mostly) — §8.3 Step 5
  extends the first-order argument to exact. The reasoning:
  N_j^{−2δ_0} must be rational, which forces −2δ_0 ∈ ℤ (for
  rational prime norm), hence δ_0 = 0.
  **Concern:** For inert Gaussian primes, the norm is p² (a
  SQUARE of a rational prime). Then N_j^{−2δ_0} = p^{−4δ_0} ∈ ℚ
  forces 4δ_0 ∈ ℤ, i.e., δ_0 ∈ (1/4)ℤ. Combined with
  |δ_0| < 1/2: δ_0 ∈ {−1/4, 0, 1/4}. The paper's Step 5 doesn't
  address this edge case. For split primes (norm p, a rational
  prime), the paper's argument is correct and gives δ_0 = 0.

- **(f) Numerical verification (Table 8.1).** **FAIL at editorial
  level** — audit C3 shows 4 of 5 entries are wrong. Paper's
  log(5)/log(13) = 0.626812... is incorrect (actual: 0.627473...).
  Only log(5)/log(2) is correct. Does not affect the proof
  conclusion (the ratios are still irrational/transcendental),
  but the stated numerical values in the table are wrong.

## Combined finding

Baker's theorem is correctly invoked. The transcendence conclusion
(log N_1 / log N_2 is transcendental) is correct for distinct
positive integer prime norms. The **formal kill** argument is
rigorous at the level of transcendence theory.

**BUT:** the entire mechanism is contingent on the integrality
premise from Point B2, which is [KEY LEMMA — OPEN]. Baker is
firing on a premise that the paper does not establish.

**Separately:** Table 8.1 has numerical errors in 4 of 5 entries.
Editorial fix.

**Separately:** Step 5's exact-promotion has a technical edge case
for inert primes (norm p²) that the paper does not address.

## Impact on the claimed result

**High severity, but the concern is inherited from B2.** If B2's
cohomology-class lemma is proved, C1's Baker kill closes
rigorously. If B2 is not proved, C1 is vacuous.

**The inert-prime edge case** (norm p² gives δ_0 ∈ (1/4)ℤ) is a
genuine concern that the paper should address separately.
Resolution: use only split primes (norm p, rational prime) or
the ramified prime (norm 2), avoiding inert primes with norm p².

## Action items

1. **Fix Table 8.1** numerical values (5 of them; 4 are wrong).
2. **Address the inert-prime edge case** in §8.3 Step 5. Either
   restrict to split/ramified primes only, or handle norm p² as
   a separate case.
3. **After B2 is closed**, re-verify that Baker's kill operates
   on the cohomology-class integrality (not just the cocycle
   representative).
4. **Optional:** replace Baker with Gelfond-Schneider throughout,
   per the paper's own §8.5 admission that GS suffices.
