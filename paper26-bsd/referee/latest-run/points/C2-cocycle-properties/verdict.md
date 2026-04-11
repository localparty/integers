# Point C2 — Cocycle shift properties: Verdict

**Weight:** MEDIUM
**Location in preprint:** §7.3
**Overall rigor label:** **[THEOREM]** on (i)–(iv); **[KEY LEMMA
— OPEN]** on (v)
**Overall verdict:** PASS on algebraic properties; see B2 for (v)

## Sub-question verdicts

- **(a) Algebraic verification.** [THEOREM] — Δc(0) = 0, Δc(δ) ≠
  0 for δ ∈ (−1/2, 1/2) \ {0}, strict monotonicity. All verified
  algebraically (§7.3 proof) and numerically (audit C2).

- **(b) Pole-free in the critical strip.** [THEOREM] — The
  denominator q − q^{−2δ} vanishes when δ = −1/2, which lies on
  the boundary of the open interval. The formula is analytic on
  (−1/2, 1/2).

- **(c) Field independence.** [LEMMA] — The cocycle shift
  formula depends on p only through p^{-s}, so replacing p with
  N(𝔭) gives the same formula over any field. For ramified primes
  (𝔭 = (1+i) with norm 2), no additional subtlety arises.

- **(d) First-order expansion.** [THEOREM] — §7.3(iv) gives
  Δc(δ) = 2δ log q / (q − 1) + O(δ²). Verified.

- **(e) Integrality constraint in (1/k)ℤ.** See Point B2. **This
  is the [KEY LEMMA — OPEN] item.**

## Combined finding

The algebraic properties of the cocycle shift formula are all
correctly stated and verifiable. The only concern is item (v)
— the integrality claim — which is the B2 concern discussed
elsewhere.

## Impact on the claimed result

At the level of the formula's properties, no concern. The
concern is entirely in B2 (whether the shift moves the
cohomology class).

## Action items

None at this point. See Point B2 for the load-bearing item.
