# Check BR3: Minimal conductor product 105

> **☑ CLOSED 2026-04-10** via `research/corrected-bridge-table.md`.
> Proposition 4.3 rebuilt with correct Frobenius orders. New table:
>
> | k | N_cond | Bridge prime 𝔭 | N(𝔭) | ord | k |
> |:-:|:-:|:-:|:-:|:-:|:-:|
> | 2 | 3 | (2+3i) | 13 | 1 | 2 |
> | 3 | 7 | (2+3i) | 13 | 2 | 3 |
> | 4 | 5 | (4+5i) | 41 | 1 | 4 |
> | 6 | 7 | (2+5i) | 29 | 1 | 6 |
>
> All four rows verified computationally. Conductor product
> `3 × 5 × 7 = 105` preserved. **Bonus:** all four primes are
> split Gaussian (norms 13, 29, 41 — rational primes), so the TR5
> inert-prime edge case `δ ∈ {−1/4, 0, 1/4}` does not arise.
>
> **Final rigor label: [LEMMA] (straightforward computational
> verification).**

---

**Group:** BR
**Source:** Paper 26 §4.3, Proposition 4.3
**Pass criterion:** Minimal conductors {3, 5, 7} verified
computationally.

**Verdict (r01):** **FAIL** — 3 of 4 rows broken
**Rigor label (r01):** [GAP]
**Rigor label (post-closure):** [LEMMA]

**Justification:** Audit C5 directly computed the Frobenius
orders in the "minimal conductor" Table 4.3 and found:

- **k=2**: flagged by paper's own [ERRATUM] as "not a valid bridge"
- **k=3**: CORRECT (ord(13) = 2 in (ℤ/7ℤ)^×, giving k = 6/2 = 3)
- **k=4**: **INVALID** — bridge prime (2+i) has norm 5, which
  divides conductor (5). (2+i) is NOT coprime to (5), so the
  Frobenius is undefined. The triple does not exist.
- **k=6**: **WRONG** — paper claims ord(2) = 1 in (ℤ/7ℤ)^×,
  but the correct order is 3 (2, 4, 1 — period 3). Would give
  k = 6/3 = 2, not 6.

**Only the k=3 row survives.** The "minimal conductor product
105" claim is unsupported by the stated table.

**Effect on proof:** The core argument needs only two valid
bridges with distinct norms. The k=3 triple at ((3+2i), (7))
is verified. A second valid triple must exist; none is explicitly
verified in the preprint.

**Cross-references:**
- Per-Point: B1
- Computation log: C5
- Editorial: this must be recomputed from scratch
