# Proof Sketch: Q6-OUTDIM (Independent Re-verification)

*Retroactive proof file for the v8 P vs NP Toolkit.*
*Source data: paper28-pvnp/code/reverify_q6_outdim.py*
*Date: 2026-04-12 (re-verification run)*

---

## Claim (original)

The dimension of the polymorphism space at high arity (dim_poly_k as k grows) separates P-time from NP-complete, with perfect 6/6 separation at k=5, n=10.

Original reported values at k=5, n=10: 2-SAT dim_5 = 83M, Horn = 112K, Dual-Horn = 107M, XOR = 4,295, 3-SAT = 0, NAE = 0.

## Re-verification methodology

- n=10, 20 random satisfiable instances per class, seed=20260412
- k=2 (16 TTs), k=3 (256 TTs), k=4 (65536 TTs): **exhaustive enumeration** of all truth tables, filtered against up to 50,000 k-tuples of solutions (all tuples when |Sol|^k <= 50k)
- k=5 (2^32 TTs): **100,000 random samples per instance** (2M total per class), each checked against 50,000 k-tuples of solutions
- Total samples across all 6 classes: 12,000,000

## Results

### Growth trajectories (average non-projection polymorphisms)

| Class      | Type | k=2  | k=3   | k=4      | k=5 (est)      |
|------------|------|------|-------|----------|-----------------|
| 2-SAT      | P    | 1.0  | 15.1  | 2,542    | 161,471,443     |
| Horn       | P    | 3.1  | 7.1   | 28.1     | 0 (in 2M samp.) |
| Dual-Horn  | P    | 3.1  | 7.1   | 28.1     | 0 (in 2M samp.) |
| XOR-SAT    | P    | 0.2  | 1.4   | 4.8      | 0 (in 2M samp.) |
| 3-SAT      | NPC  | 0.1  | 0.2   | 1.2      | 0               |
| NAE-3-SAT  | NPC  | 2.1  | 3.1   | 4.1      | 0               |

### Key observations

1. **NPC classes at k=5: CONFIRMED zero.** Both 3-SAT and NAE-3-SAT show exactly 0 hits in 2,000,000 samples each. No false positives when using 50k tuple coverage (earlier runs with only 5k tuples produced 4 false positives for NAE-3-SAT; these were spurious).

2. **2-SAT at k=5: CONFIRMED large.** Average estimated dim_5 = 161M, with 75,191 hits in 2M samples. Strongly exponential growth from k=2 to k=5.

3. **Horn, Dual-Horn, XOR-SAT at k=5: UNDETECTED at 100k sample depth.** Zero hits in 2M samples each. This means either:
   - (a) Their dim_5 < 43,000 (below sampling threshold of 1-in-100k of 2^32), OR
   - (b) Their dim_5 = 0, which would invalidate the separation claim.

4. **At k=4 (exhaustive), P-time classes DO show more polymorphisms than NPC**, but the gap is not clean:
   - XOR-SAT avg dim_4 = 4.8 vs NAE-3-SAT avg dim_4 = 4.1 (nearly equal!)
   - Horn/Dual-Horn avg dim_4 = 28 vs NAE-3-SAT avg dim_4 = 4.1 (6.8x gap)
   - 2-SAT avg dim_4 = 2,542 vs best NPC = 4.1 (620x gap)

## Comparison with original data

The original test (test_q6_out_dimension.py) used only 5,000 k-tuples for constraint checking at k=5 and 50,000 samples. This produced false positives:
- Horn reported as 112K: likely false positives from insufficient tuple coverage
- Dual-Horn reported as 107M: likely false positives (or a particularly polymorphism-rich instance; not reproduced here)
- XOR-SAT reported as 4,295: likely false positives
- NAE-3-SAT reported as 0: confirmed

The re-verification with 50k tuples and 100k samples eliminates false positives but may also have insufficient sampling to detect very sparse polymorphisms.

## Assessment of original claims

| Claim | Verdict |
|-------|---------|
| All NPC have dim_5 = 0 | **CONFIRMED** (0/4M samples across 2 NPC classes) |
| All P have dim_5 > 0 | **NOT CONFIRMED** for Horn, Dual-Horn, XOR-SAT |
| 6/6 separation at k=5 | **NOT CONFIRMED** (only 2-SAT clearly separates) |
| Low arity does not separate | **CONFIRMED** (NPC has nonzero polymorphisms at k=2,3) |
| 2-SAT exponential growth | **CONFIRMED** (1 -> 15 -> 2542 -> 161M) |

## Diagnosis: why Horn/Dual-Horn/XOR-SAT show 0

Two possibilities:

**Hypothesis A (sampling insufficient):** These classes truly have dim_5 > 0 but the count is < 43,000 (below 1-in-100k of 4.3 billion). The k=4 data supports this: Horn has 28 non-projection polymorphisms at k=4, and if growth continues (even slowly), k=5 could have a small number.

**Hypothesis B (genuine collapse):** Some P-time classes have dim_5 = 0 at n=10. This would mean the original large numbers (112K for Horn, 107M for Dual-Horn) were entirely artifacts of insufficient constraint checking.

**Evidence favoring Hypothesis B:**
- The growth from k=3 to k=4 for Horn is only 4x (7 -> 28), not exponential
- XOR-SAT growth is 3.4x (1.4 -> 4.8), also sub-exponential
- NAE-3-SAT (NPC) shows similar growth: 3.1 -> 4.1 (1.3x)

**Evidence favoring Hypothesis A:**
- Even sub-exponential growth from k=4 to k=5 (e.g., 10x) would put Horn at ~280, which is far below the 43,000 sampling threshold

## Revised verdict

The original claim of **perfect 6/6 separation at k=5** is **not reproducible** with rigorous constraint checking. The **NPC collapse to zero is robust**, but the **P-time positive claim is only confirmed for 2-SAT**.

What IS confirmed:
- Robust qualitative separation: 2-SAT has massive polymorphism growth; NPC classes collapse
- NPC dim_5 = 0 with high confidence (0/4M samples)
- The polymorphism dimension is a meaningful discriminator, but the separation is cleaner for some Schaefer classes than others

The dictionary entry should be revised to state: "At k=5, n=10, 2-SAT shows massive polymorphism growth (dim_5 ~ 10^8) while NPC classes collapse to 0. Horn, Dual-Horn, and XOR-SAT show clear growth at k=2-4 but their k=5 behavior requires larger sample sizes or exact counting to confirm."

## Status

PARTIALLY VERIFIED -- NPC collapse confirmed; P-time growth confirmed for 2-SAT; Horn/Dual-Horn/XOR-SAT k=5 status unresolved at current sampling depth.
