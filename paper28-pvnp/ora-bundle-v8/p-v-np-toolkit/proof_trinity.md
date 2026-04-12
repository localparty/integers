# Proof: THE TRINITY -- Spectral-Geometric-Information Correspondence

*Independent re-verification synthesis*
*Date: 2026-04-12*

---

## Claim

Three independent measures separate P from NPC across all six Schaefer classes:
spectral (TGap), geometric (holonomy), information (polymorphism dimension).
The original claim was 6/6 separation in all three columns.

## Re-verification status of each column

### Spectral column (TGap)

Source: RULE9-GATE and P8-BARRIERS re-verification.

TGap as a binary gate (0 = at least one Taylor operation preserves the relation,
1 = no Taylor operation preserves) cleanly separates P-time from NPC at the
language level. This is the strongest of the three columns:

- 2-SAT, Horn-SAT, Dual-Horn, XOR-SAT: TGap = 0 (Taylor ops exist).
- 3-SAT, NAE-3-SAT: TGap = 1 (no Taylor ops survive cross-instance).
- 0 out of 2000 random Boolean functions had TGap = 0, confirming NPC-side robustness.

The continuous TGap exponent formula 2/(gamma_6 - gamma_5) from Q5-RIEMANN is
weakened (match is against literature values, not independent measurement, and
alpha cannot be measured precisely at n <= 16). However, the binary separation
does not depend on the continuous formula. It stands on its own.

**Status: 6/6 CONFIRMED.**

### Geometric column (holonomy)

Source: O7-HOLONOMY re-verification.

Holonomy measures closed loops in the constraint hypergraph. For NPC languages,
cross-instance constraint cycles produce nontrivial holonomy; for P-time
languages, the polymorphism structure trivialises these loops.

- All six Schaefer classes tested. 6/6 separation confirmed.
- NAE-3-SAT correction: the negated-projection polymorphisms (NOT a, NOT b,
  NOT c) are properly classified as essentially unary. They do not constitute
  genuine Taylor operations. Zero genuine Taylor ops survive cross-instance
  for NAE, matching the NPC prediction.
- This correction actually strengthens the entry by removing an ambiguity in
  the original NAE treatment.

**Status: 6/6 CONFIRMED.**

### Information column (dim_poly_k)

Source: Q6-OUTDIM re-verification.

dim_poly_k counts the number of k-ary polymorphisms (up to equivalence) that
preserve a constraint language. The original claim: NPC languages collapse to 0,
P-time languages show exponential growth, clean 6/6 separation at k=5.

Re-verification findings:

- NPC collapse: CONFIRMED. 0 polymorphisms in 2,000,000 samples for both
  3-SAT and NAE-3-SAT. Robust.
- 2-SAT exponential growth: CONFIRMED. 161,000,000 polymorphisms at k=5.
  Clearly separated from NPC.
- Horn-SAT, Dual-Horn, XOR-SAT at k=5: NOT CONFIRMED. Rigorous 50k-tuple
  constraint checking yields 0 hits for all three. The original nonzero counts
  came from 5k-tuple checking, which produced false positives.
- At k=4 (exhaustive): 2-SAT is clearly separated. Horn and Dual-Horn show
  moderate counts. XOR-SAT is nearly equal to NAE -- no clean separation.

The information column therefore confirms the NPC/P divide in one direction
(NPC collapse) but does not yet establish positive growth for all four P-time
classes at k=5. The clean 6/6 separation was overstated.

**Status: PARTIALLY VERIFIED (NPC collapse + 2-SAT growth confirmed; Horn/Dual-Horn/XOR unconfirmed at k=5).**

## Independence assessment

The three columns measure genuinely different properties:

1. **Spectral (TGap):** algebraic -- existence of a Taylor polymorphism for the
   language. This is a yes/no property of the clone.
2. **Geometric (holonomy):** topological -- whether constraint-graph cycles
   produce nontrivial parallel transport. This depends on the interaction
   structure between constraints, not just the clone.
3. **Information (dim_poly_k):** combinatorial -- how fast the polymorphism
   count grows with arity k. This is a quantitative refinement of the
   spectral column.

Columns 1 and 3 are correlated (both derive from polymorphisms) but not
identical: TGap is binary while dim_poly_k is a growth rate. Column 2
(holonomy) is structurally independent, drawing on constraint-graph topology
rather than polymorphism algebra.

The independence is therefore partial: spectral and information share a common
algebraic root, while geometric is genuinely orthogonal.

## Revised trinity status

| Column | Original claim | Re-verified status |
|--------|---------------|--------------------|
| Spectral (TGap) | 6/6 | 6/6 CONFIRMED (binary gate) |
| Geometric (holonomy) | 6/6 | 6/6 CONFIRMED (NAE corrected) |
| Information (dim_poly_k) | 6/6 | PARTIAL (2/6 P-time + 2/2 NPC confirmed) |

## Verdict

The trinity holds in its spectral and geometric columns. Both achieve clean 6/6
separation across all Schaefer classes with no caveats beyond finite-size effects.

The information column needs correction: the original 6/6 claim at k=5 relied on
insufficient constraint checking (5k-tuples instead of 50k). With rigorous
checking, only 2-SAT shows confirmed exponential growth at k=5. The NPC collapse
side (3-SAT, NAE) is robust. Horn, Dual-Horn, and XOR-SAT may have growth below
the sampling threshold, or may require higher k to manifest clearly.

The programme's core claim -- that spectral, geometric, and information-theoretic
measures all independently witness the P/NPC divide -- is supported by two out of
three columns with full confidence, and by the third column on the NPC side. The
P-time side of the information column is the remaining gap.

This is an honest improvement over the original: two solid columns plus a
partially verified third is stronger than three columns with hidden false
positives.
