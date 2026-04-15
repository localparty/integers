# Check GZ2: Heegner hypothesis for y²=x³−x

**Group:** GZ
**Source:** Paper 26 §12.2
**Pass criterion:** Heegner hypothesis resolved explicitly.

**Verdict:** PARTIAL (under-specified)
**Rigor label:** [LEMMA]

**Justification:** For y²=x³−x (conductor 32), prime 2 ramifies
in ℚ(i). The classical Heegner hypothesis FAILS for K = ℚ(i).

Paper §12.2 mentions two resolutions:
(a) Yuan-Zhang-Zhang 2013 generalized Gross-Zagier (removes the
    Heegner hypothesis);
(b) Auxiliary field ℚ(√−7), where 2 splits (−7 ≡ 1 mod 8).

**Paper does not commit to one.** Both resolutions are valid in
principle, but a watertight proof should pick one and verify.

**Fix:** Commit to either YZZ 2013 or the auxiliary ℚ(√−7) path.
For the latter, verify that the Heegner point construction over
ℚ(√−7) descends to the curve with CM by ℚ(i).

**Cross-references:**
- Per-Point: D3
- Internal adversarial: Attack 7 (WEAKENED)
