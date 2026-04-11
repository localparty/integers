# Check LC1: BSD leading coefficient at rank 0

**Group:** LC
**Source:** Paper 26 §11.3, §13.1
**Pass criterion:** L(E,1) = Ω · |Ш| · ∏ c_p / |E_tors|² with
all terms defined and computed.

**Verdict:** PASS with one editorial issue
**Rigor label:** [LEMMA]

**Justification:** The formula is correctly stated. For the test
curve y² = x³ − x:
- Ω_E ≈ 2.62205755 (correct numerical value, though the formula
  "Γ(1/4)²/(2π)^{3/2}" stated in §13.3 is off by π; see LC4)
- |Ш| = 1 (Kolyvagin, matches LMFDB 32.a3)
- c_2 = 4 (corrected from earlier c_2 = 1; matches LMFDB)
- c_p = 1 for p > 2 (good reduction)
- |E_tors|² = 16 (E_tors = Z/2 × Z/2)

BSD formula: L(E,1) = (1 × 2.622 × 1 × 4) / 16 = 0.6555
Paper's L(E,1) = Ω/4 = 0.6555 ✓

The formula closes correctly. The c_2 = 4 correction per LMFDB
is in place (this was Issue 3 BROKEN in the internal adversarial
review).

**Cross-references:**
- Per-Point: points/D2-kolyvagin-rank0/verdict.md
- Computation log: C4
- LC4 (Ω formula editorial error)
