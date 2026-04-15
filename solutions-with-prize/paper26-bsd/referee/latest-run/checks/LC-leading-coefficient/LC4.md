# Check LC4: Ω_E formula correctly stated

**Group:** LC
**Source:** Paper 26 §13.3 table
**Pass criterion:** Formula for the real period of y²=x³−x is
correct.

**Verdict:** **FAIL** (editorial error)
**Rigor label:** (editorial)

**Justification:** The paper writes:
> "Ω_E = Γ(1/4)²/(2π)^{3/2} ≈ 2.62205755..."

This formula is **WRONG**. Compute directly:
- Γ(1/4)²/(2π)^{3/2} = 0.8346...  (NOT 2.622)
- Γ(1/4)²/(2·√(2π)) = 2.62205755... (the correct formula)
- These differ by a factor of exactly π (0.8346 × π = 2.622).

The paper's **numerical value** (2.62205755) is correct, but the
formula **as written** yields 0.8346, not 2.622. This means
there's a typo or copy-paste error in the preprint's formula.

**Effect on proof:** ZERO. The numerical value is correct, and
the BSD formula closure with Ω = 2.622 works (see LC1). But the
formula as printed is mathematically wrong.

**Fix:** Replace `Γ(1/4)²/(2π)^{3/2}` with `Γ(1/4)²/(2·√(2π))`
or equivalently `Γ(1/4)²/√(8π)`.

**Cross-references:**
- Computation log: C4a
- Per-Point: D2
