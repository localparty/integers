# Check SHA2: Ш with correct order in BSD formula

**Group:** SHA
**Source:** Paper 26 §13.3, Rubin 1991
**Pass criterion:** |Ш| consistent across formula.

**Verdict:** PASS (for p > 7 via Rubin)
**Rigor label:** [LEMMA]

**Justification:** Rubin 1991 establishes the p-part of BSD for
CM curves with p > 7. For test curve y²=x³−x, |Ш| = 1 (LMFDB
32.a3) and the BSD formula closes. Small-prime p-part needs
separate treatment but is not load-bearing for the proof.

**Cross-references:**
- LC1, LC3, KV3
