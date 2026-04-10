# AE4 — AE sufficient for the chain (identity theorem)

**Claim:** Analytic function nonzero at infinitely many points is nonzero a.e.; suffices because chain only needs simplicity at generic λ.

**Pass criterion:** identity theorem correctly applied; sufficiency argument valid.

**Finding:**
- Identity theorem: correctly gives discreteness of the zero set
  {f_N = 0} for real-analytic f_N. At N ≤ 20, verified at
  λ = √14, hence S_N is discrete at each N ≤ 20.
- For N > 20: Paper 13's Slepian-limit extension is a
  **heuristic**, not a theorem. It argues that the limiting
  overlap is positive in the Slepian limit and "by continuity"
  the overlap remains positive for large N. The convergence
  argument is not stated rigorously.
- "AE suffices because we need simplicity at one λ per N":
  reasonable but see C2.04 — the proof actually uses a **fixed**
  λ = √14 for all N, so we need simplicity at that specific λ
  at every N (not just "some λ per N").

**Status:** WEAKENED at N > 20. Rigorous at N ≤ 20; heuristic
above.

**Confidence:** 6/10. See points/C2-ae-simplicity/03-prolate-
extension.md.
