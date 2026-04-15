# Point B1 — Bridge family over Q(i): Verdict

> **☑ CLOSED 2026-04-10** — Proposition 4.3 rebuilt in
> `research/corrected-bridge-table.md` with four new rows using
> Gaussian primes of norms {13, 29, 41}, all split. Conductor
> product `3 × 5 × 7 = 105` preserved; all four rows verified
> computationally in `referee/code/`. Bonus: the choice of split
> primes avoids the TR5 inert-prime edge case.
>
> The "355 triples" claim (r01 item (b)) is an editorial /
> bibliographic matter, not load-bearing for the proof chain — two
> valid triples with distinct prime norms suffice, and the
> corrected table supplies four.
>
> **Overall rigor label (post-closure): [LEMMA].**
> **Overall verdict (post-closure): PASS.**
>
> *r01 verdict preserved below.*

---

**Weight:** MEDIUM
**Location in preprint:** §4
**Overall rigor label (r01):** **[GAP]** on Proposition 4.3; **[LEMMA]** on the rest
**Overall rigor label (post-closure):** **[LEMMA]** throughout
**Overall verdict (r01):** FAIL on the worked example table; PASS on the structural claims
**Overall verdict (post-closure):** PASS

## Sub-question verdicts

- **(a) Brauer cocycles β_k.** [THEOREM] — H²(ℤ/kℤ, U(1)) ≅ ℤ/kℤ
  is standard. Definition 4.1 and Proposition 4.1 state the Brauer
  class correctly.

- **(b) Bridge triples (Prop 4.2's 355 count).** NOT VERIFIED — the
  paper cites research/02 for the computation. The claim of 355
  triples for N(𝔑) ≤ 50 was not independently reproduced in this
  run. Given the errors in Prop 4.3 (below), the 355 count should
  be independently reproduced in a future run.

- **(c) Minimal conductors (Prop 4.3).** **[GAP]** — direct
  computational check (audit C5) finds **3 of 4 rows broken**:
  - k=2: flagged by paper's own [ERRATUM] as "not a valid bridge"
  - k=3: CORRECT — ord_{(ℤ/7ℤ)^×}(13) = 2, giving k = φ(7)/2 = 3
  - k=4: **INVALID** — bridge prime (2+i) has norm 5, which
    divides the conductor (5), so (2+i) is NOT coprime to (5),
    so the Frobenius is not defined. The triple ((2+i), (5), k=4)
    does not exist.
  - k=6: **WRONG** — paper claims ord_{(ℤ/7ℤ)^×}(2) = 1, but the
    correct order is 3 (2, 4, 1 — period 3). This would give
    k = φ(7)/3 = 2, NOT 6 as the paper claims.

  The "minimal conductor product 105" claim is thus unsupported
  by the stated table. See audit C5 for detail.

- **(d) Connection to T_{BC,K}.** [KEY LEMMA — OPEN] — How do the
  bridge cocycles interact with the spectral operator over K? The
  interaction is the same as over Q (the shift formula in B2 is
  derived from the local Euler factor, which is common to both
  fields). But the interaction's correctness depends on the
  Meyer-Nelson compatibility (Point A3) and the cohomology-class
  lemma (Point B2).

## Combined finding

**The bridge family is structurally plausible but the worked
example table in Proposition 4.3 is broken.** Three of four
"minimal conductor" rows have errors or are invalid. Only the
k=3 triple at ((3+2i), (7)) is correct.

**For the core proof chain**, only **two valid bridges with
distinct norms** are needed (for Baker's argument). The k=3
triple provides one valid example. At least one more valid
example must exist; this audit did not verify the 355-triple
enumeration of Proposition 4.2, so we cannot confirm. **The
paper's own worked examples of "minimal conductors" provide
only ONE valid triple.**

## Impact on the claimed result

**Moderate to high.** If only the k=3 triple is verified, the
argument of Baker-kills-δ = 0 has no second bridge to operate on
— at least not one that the paper explicitly exhibits. The
structural claim that "bridges exist" is plausible (Prop. 4.2),
but the minimum requirement of "two explicit bridges with
distinct norms" is not met in the preprint.

## Action items

1. **Recompute Proposition 4.3** with correct Frobenius orders:
   - Find the actual minimal conductor and Gaussian prime for
     each k ∈ {2, 3, 4, 6}.
   - Verify each computation explicitly.

2. **Independently verify Proposition 4.2** (the 355-triple
   enumeration).

3. **Exhibit at least TWO valid bridge triples with distinct
   prime norms** explicitly in the paper. The k=3 triple at
   ((3+2i), (7)) gives norm 13. A second triple with a different
   norm (e.g., 2, 5, 17, 29, ...) should be verified and
   presented.

**Estimated effort:** One to two days of careful computation.
This is "editorial math" — computationally concrete and
boundedly hard.
