# Retroactive Verification Summary

*Date: 2026-04-12*

---

## Overview

10 dictionary entries were subjected to independent re-verification. Results:

| Outcome | Count | Entries |
|---------|-------|---------|
| CONFIRMED (same or stronger) | 4 | PATB-DIAGONAL, RULE9-GATE, P8-BARRIERS, O7-HOLONOMY |
| CONFIRMED with softening | 1 | Q7-CASIMIR |
| WEAKENED (claim reduced) | 1 | Q5-RIEMANN |
| PARTIALLY VERIFIED | 1 | Q6-OUTDIM |
| CORRECTED (score changed) | 1 | PATD-CONDEXP (4/5 to 3/5) |
| DOWNGRADED | 1 | O8-PARTITION (2/5 to 1/5) |
| Meta-entry | 1 | TRINITY (see proof_trinity.md) |

**Bottom line:** 5 of 10 entries confirmed or stronger. 1 weakened but still
useful. 2 corrected with lower scores. 1 partially verified with significant
false-positive removal. 1 meta-entry assessed separately.

---

## Entries that got STRONGER

### PATB-DIAGONAL
Extended from original coverage to include Dual-Horn and NAE explicitly.
100% closure across all six Schaefer classes. The foundation is more solid
than before.

### P8-BARRIERS
2000 random functions tested (up from the original run). Zero had TGap = 0.
The barrier-clearance claim is robust. The finite-size caveat (accidental
polymorphisms at high clause ratios) is noted but does not affect the
asymptotic argument.

### O7-HOLONOMY
The NAE correction -- properly classifying negated projections as essentially
unary -- actually removes an ambiguity in the original. The 6/6 separation
is now cleaner because the NAE case no longer relies on a debatable
polymorphism classification.

---

## Entries with corrections

### Q5-RIEMANN (WEAKENED)
The formula 2/(gamma_6 - gamma_5) is uniquely best among 3780 candidates, so
the mathematical content survives. But the "verified at 0.001%" precision claim
is misleading: alpha cannot be independently measured at n <= 16, and the match
is against published values. The binary TGap separation (RULE9-GATE) does not
depend on this formula.

### RULE9-GATE (clarification)
TGap must be treated as binary (0 or 1), not as a continuous exponent. The
language-level separation is clean. The continuous value is
discretisation-sensitive and should not be over-interpreted.

### Q6-OUTDIM (PARTIALLY VERIFIED -- most significant correction)
The original 6/6 claim at k=5 was based on 5k-tuple constraint checking.
Rigorous 50k-tuple checking reveals that Horn, Dual-Horn, and XOR-SAT all
yield 0 polymorphisms at k=5 -- the original nonzero counts were false
positives. Only 2-SAT shows confirmed exponential growth. The NPC collapse
(0 polymorphisms for 3-SAT and NAE) is robust.

### Q7-CASIMIR (softened)
"Exactly 2 inflection points" is discretisation-sensitive at n=12. Replaced
with "three qualitative regimes." The P/NPC decay distinction itself holds.

### O8-PARTITION (DOWNGRADED, 2/5 to 1/5)
V2 (Lee-Yang spacing signature) does not reproduce. This was a statistical
fluctuation in the original run. Only V1 (entropy gap) is confirmed. All three
kills still hold, but the entry's positive content is minimal.

### PATD-CONDEXP (CORRECTED, 4/5 to 3/5)
Horn-SAT is also Hamming-1 disconnected at n >= 12. The original scored it as
walk-connected, giving 4/5. Correct score is 3/5. The polymorphism-closure
version gives 5/5 but is not independent of TGap.

---

## The most important correction

**Q6-OUTDIM** is the most valuable finding of the re-verification.

The original claimed clean 6/6 separation of dim_poly_k at k=5 across all
Schaefer classes. This was the information column of the trinity, and it
appeared to independently confirm the spectral and geometric columns.

The correction: increasing constraint-checking rigour from 5k-tuples to
50k-tuples eliminates all Horn, Dual-Horn, and XOR-SAT polymorphisms at k=5.
The original nonzero counts were false positives -- relations that appeared
to be preserved under 5k random constraint checks but failed under more
thorough testing.

This matters for three reasons:

1. It removes a false positive that could have undermined credibility if
   discovered by an adversary.
2. It correctly identifies the information column as the weakest of the three
   trinity columns, focusing future work.
3. It demonstrates that retroactive verification works -- the whole point of
   this exercise was to catch exactly this kind of error.

The NPC collapse side of Q6 is unaffected and remains one of the strongest
results in the dictionary.

---

## Overall confidence

After re-verification, the dictionary's reliability is structured as follows:

**High confidence (can be cited without caveat):**
- PATB-DIAGONAL: algebraic foundation, fully confirmed.
- RULE9-GATE: binary TGap separation, fully confirmed.
- P8-BARRIERS: barrier clearance, fully confirmed.
- O7-HOLONOMY: geometric separation, fully confirmed with NAE correction.

**Medium confidence (cite with noted limitations):**
- Q5-RIEMANN: formula is uniquely best, but precision claim needs qualification.
- Q7-CASIMIR: qualitative regimes confirmed, exact inflection count dropped.
- PATD-CONDEXP: 3/5 walk gap confirmed; polymorphism-closure version is 5/5
  but not independent.

**Low confidence (needs further work):**
- Q6-OUTDIM: NPC side robust, P-time side unconfirmed beyond 2-SAT at k=5.
- O8-PARTITION: only 1 of 5 signatures confirmed.

**The core programme is solid.** The spectral (TGap) and geometric (holonomy)
columns both achieve clean 6/6 separation with no false positives detected.
These are the two load-bearing pillars of the P vs NP transposition dictionary.
The information column and the supplementary entries need further development,
but they are secondary to the main argument.

The re-verification removed 3 false positives (Q6 Horn/Dual-Horn/XOR at k=5),
1 non-reproducing signature (O8 Lee-Yang), and 1 misclassification (PATD
Horn-SAT connectivity). None of these affect the core spectral or geometric
results. The dictionary is more honest and therefore more credible than before
the re-verification.
