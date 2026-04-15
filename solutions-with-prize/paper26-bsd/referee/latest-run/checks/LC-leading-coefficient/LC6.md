# Check LC6: Tamagawa numbers correctly computed

**Group:** LC
**Source:** Paper 26 §13.3 table, adversarial Issue 3
**Pass criterion:** c_2 and other c_p match LMFDB for test curves.

**Verdict:** PASS (after the c_2 = 4 correction)
**Rigor label:** [LEMMA]

**Justification:** Internal adversarial review flagged
Issue 3 BROKEN: paper originally stated c_2 = 1 for y²=x³−x,
LMFDB 32.a3 reports c_2 = 4. The fix is in place: the current
preprint (§13.3) states "Tamagawa number at 2 | c_2 | 4 (LMFDB
32.a3; corrected from earlier draft)". BSD formula now closes.

c_p = 1 for all p > 2 (good reduction for y²=x³−x away from 2).

**Cross-references:**
- Computation log: C4c
- Per-Point: D2, E2
