# Check SHA3: Strong BSD p-part for all primes

**Group:** SHA
**Source:** Paper 26 §11.3 remark, Rubin 1991
**Pass criterion:** Full p-part analysis.

**Verdict:** PARTIAL
**Rigor label:** [LEMMA]

**Justification:** Rubin 1991 gives p > 7 for CM curves. Small
primes (p = 2, 3, 5, 7) need additional treatment (Perrin-Riou,
Kobayashi, or case-by-case). The paper mentions this briefly but
does not fully resolve. For the weak-form BSD (rank equality),
not an issue; for the strong form (leading coefficient), there's
a small gap at small primes.

**Cross-references:**
- SHA2, LC1
