# Check BR3: Minimal conductor product 105

**Group:** BR
**Source:** Paper 26 §4.3, Proposition 4.3
**Pass criterion:** Minimal conductors {3, 5, 7} verified
computationally.

**Verdict:** **FAIL** — 3 of 4 rows broken
**Rigor label:** [GAP]

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
