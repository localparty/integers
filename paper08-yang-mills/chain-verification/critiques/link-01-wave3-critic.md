# Link 1 Wave 3 Adversarial Critic

**Target:** KK spectral gap Δ₀^KK > 0 (Thm 4) — Wave 2 Author repair
**Wave:** 3 (adversarial Critic — different instance from Author; no trust of Author quotes without independent verification)
**Verdict:** **WEAKENED** (repair partially successful; one critical sub-claim falsified)
**Confidence:** 9/10

---

## Independent Preprint Verification

All Author quotes were independently verified against
`preprint/sections/04-lattice-proof-part1.md`. Findings below
cite line offsets in that file.

---

## Attack Vector A — r₃-stabilization hypothesis

**Finding: PASSES. The repair is correct in kind, though inert in force.**

Independent verification confirms §1.5 (lines 114–141) already lists
`r₃` as a model parameter in the five-parameter table, and states
explicitly "the limit `a → 0` is taken with `r₃` fixed" (line 140).
Theorem 1 (lines 182–193) carries the hypothesis "the Fubini–Study
metric with radius `r₃`" and nowhere treats `r₃` as a quantized field.
The Author's proposed Standing Hypothesis block adds explicitness; it
is an honest scope declaration, not a logical gap.

**Residual issue (minor).** The Author's Remark 2 references "the
`(p,q) = (0,0)` mode of Appendix A." Appendix A is titled "The
Laplacian Spectrum on CP²" and is explicitly N=3 specific (A.2 table
uses (p,q) Dynkin labels of SU(3)). For general CP^{N-1} the zero
mode is simply the constant function; the (p,q) notation is undefined
for N ≠ 3. The Remark should read "the constant zero mode of the
scalar Laplacian" rather than citing Appendix A by N=3 notation. This
is a presentational inaccuracy, not a logical error — the modulus
exists for all N — but it weakens the cross-reference.

**Backward check — cross-node impact.** Fixing r₃ as background data
does not conflict with any downstream link. Links 2–17 all operate at
fixed background geometry; r₃ appears only as a parameter (not a
dynamical variable) in every subsequent step. No damage propagated.

**Sub-verdict: PASSES (presentational fix accepted; Appendix A
cross-reference should be corrected to be N-general).**

---

## Attack Vector B — C₀(N) formula and β_max > 0

**Finding: BROKEN at the stated threshold. This is the primary failure
of the Wave 2 repair.**

### B1. Integral formula — verified correct

The Author's Gamma-function integral identity is independently
confirmed:

$$\int_0^\infty t^{N-2} e^{-\gamma t^{1/(2(N-1))}} dt
  = 2(N-1)\,\gamma^{-2(N-1)^2}\,\Gamma(2(N-1)^2)$$

This follows from the substitution u = γ t^s with s = 1/(2(N-1)),
p = N-2, giving (1/s) γ^{-(p+1)/s} Γ((p+1)/s) = 2(N-1) γ^{-2(N-1)^2}
Γ(2(N-1)^2). The formula is correct. The Γ-function values are:

| N | 2(N-1)² | Γ(2(N-1)²) |
|---|---------|------------|
| 2 | 2 | 1.0 |
| 3 | 8 | 5040 |
| 4 | 18 | ≈ 3.6 × 10¹⁵ |

### B2. The β_max > 0 claim is FALSE at the stated threshold

**This is the decisive failure.** The Author asserts (Remark 3):

> "m₁a/6 ≥ 4/(3√3) ≈ 0.77 at the threshold boundary, which exceeds
> ln(c_d K C₀^{1/6}) for all N ≥ 2 at the stated physical regime
> r₃/a ≪ 1."

Two independent errors compound here:

**Error 1: Conflation of physical regime with threshold boundary.**
The preprint itself (lines 629–631) states:
> "c_d appears only inside a logarithm bounded by m₁a/6 ∼ 10¹⁴"

This is true in the **physical** regime r₃/a ∼ 10⁻¹⁵. But the
threshold r₃/a < √(3/(4N)) is NOT the physical regime. At the
threshold boundary r₃/a = √(3/(4N)):

| N | r₃/a | m₁a | m₁a/6 |
|---|------|-----|-------|
| 2 | 0.612 | 4.62 | **0.770** |
| 3 | 0.500 | 6.93 | **1.155** |
| 4 | 0.433 | 9.24 | **1.540** |

These are O(1) numbers, not 10¹⁴. The preprint's "bounded by 10¹⁴"
argument does not apply here.

**Error 2: c_d is not O(1).**
The KP convergence criterion contains ln(c_d K C₀^{1/6}). The
preprint (line 628) states: "c_d ≤ Ce^7 (Klarner-Rivest 1973)."
So ln(c_d) ≥ 7 at the Klarner-Rivest bound. Even with the
Gaunt-Sykes numerical estimate c_d ≈ 6.75 for d=4, ln(c_d) ≈ 1.91.

Combining at the threshold boundary with c_d from Gaunt-Sykes (6.75),
K = 1 (normalized Haar), and C₀ computed via the Author's own formula
with γ = c′_N · a/r₃ at threshold:

| N | m₁a/6 | ln(c_d K C₀^{1/6}) | β_max |
|---|-------|---------------------|-------|
| 2 | 0.770 | 2.35 (c_d=6.75) | **−1.58** |
| 3 | 1.155 | 2.99 (c_d=6.75) | **−1.83** |

β_max < 0 for all N ≥ 2 at the stated threshold, with **any**
rigorous or numerical value of c_d. The KP criterion fails at
r₃/a = √(3/(4N)).

**Root cause: the threshold r₃/a < √(3/(4N)) does not ensure
β_max > 0. The threshold is too permissive by a factor of ∼6–9.**

For β_max > 0 with c_d ≈ 6.75, one requires m₁a/6 > ln(c_d) ≈ 1.91,
i.e., m₁a > 11.5, i.e., a/r₃ > 11.5/(2√N). For N=2 this is
a/r₃ > 8.1, i.e., r₃/a < 0.124 — a factor of ~5 tighter than
√(3/8) ≈ 0.612.

### B3. C₀(N) formula — a further inconsistency

The Author writes C₀(N) with γ = c′_N (the spectral gap eigenvalue
difference, an O(1) constant), yielding:

$$C_0(N) \leq 2C_1\bigl[1 + 2(N-1)(c'_N)^{-2(N-1)^2}\Gamma(2(N-1)^2)\bigr]$$

But the actual γ in the mode sum (Step 4 of Thm 2, lines 531–535) is
γ = c · a/r₃, not just c′_N. The Author has dropped the (a/r₃)
suppression factor from the C₀ formula. Specifically:

$$C(N) \leq 1 + 2(N-1)(c'_N \cdot a/r_3)^{-2(N-1)^2}\Gamma(2(N-1)^2)$$

At fixed a/r₃, C(N) grows with decreasing a/r₃ (as (a/r₃)^{-2(N-1)²}).
At the threshold, a/r₃ ∼ 2 and this factor is not negligible. The
preprint's claim (line 564–566) that "C₀ depends on N but not on
β or a/r₃" is technically correct (C₀ is defined as a supremum over
the allowed range), but the Author's explicit formula omitting the
(a/r₃)^{-2(N-1)²} factor is the largest-possible (worst-case) bound,
achieved only as a/r₃ → 1⁺. This is not wrong in principle but
produces a formula that is inconsistently applied: the Author uses
the worst-case C₀ (no a/r₃ suppression) but then claims the small
m₁a/6 ∼ 0.77 is sufficient to dominate it — these two choices are
incompatible.

**Sub-verdict: BROKEN on the β_max > 0 claim. The stated threshold
r₃/a < √(3/(4N)) does not guarantee convergence of the KP expansion.
The threshold condition must be significantly tightened, or the proof
must carry an additional condition (e.g., r₃/a < 1/(6√N)) that ensures
m₁a/6 > ln(c_d).**

---

## Attack Vector C — Seiler adjoint-extension sentence

**Finding: PASSES (the sentence is mathematically correct; the citation
gap remains open but is not a logical hole).**

The Author's argument: Ad(U) : su(N) → su(N) is an isometry (‖Ad(U)φ‖
= ‖φ‖), so the hopping term ‖Ad(U_{⟨xy⟩})φ_n(y) - φ_n(x)‖² equals
‖φ_n(y) - Ad(U)⁻¹φ_n(x)‖² — a scalar kinetic term after a U-dependent
rotation. This is independently verified: Ad(U) ∈ SO(N²-1) by
compactness, so it is an isometry of (su(N), Killing form). The
transfer-matrix equivalence follows because the rotation is measurable
and bounded uniformly in U (compact group), so dominated convergence
applies when integrating over Haar measure.

The Seiler 1982 LNP 159 proposition number remains unverified (the
Author flags this). The fallback citations (Glimm-Jaffe 1987 Ch. 18,
or Lüscher 1977 eq. (2.5)) are appropriate alternatives. This is a
bibliographic gap, not a mathematical one.

**Sub-verdict: PASSES (minor bibliographic gap, acceptable for
WEAKENED → REPAIRED on this item alone).**

---

## Attack Vector D — Cross-node consistency

**Finding: NO CONFLICT with L11 C_new or L13.**

L11's C_new is the Balaban RG constant controlling g_k^4 Δ̂² bounds
(§5.5.5); it does not reference L1's C₀ or m₁. L13's summability uses
a different cluster-expansion constant C_0^{cl} from §5.4.6, not the
KK bond-activity C₀ from Theorem 2. The two constants share notation
only superficially; they enter different parts of the proof. No
cross-contamination detected.

**Sub-verdict: PASSES.**

---

## Attack Vector E — Bonus grep: r₃ usage consistency

All 37 occurrences of r₃ in `04-lattice-proof-part1.md` (verified by
independent grep) treat r₃ as a fixed positive parameter: it appears
as a metric scale in the Fubini-Study metric definition, in the KK
mass formula m_n = √λ_n / r₃, in the physical regime table (§1.5),
and in the threshold condition r₃/a < √(3/(4N)). No occurrence
treats r₃ as a dynamical variable or a quantized field. The repair's
Standing Hypothesis is consistent with all 37 usages.

**Sub-verdict: PASSES.**

---

## Primary Gap Summary

The Wave 2 repair correctly handles:
- r₃-stabilization (scope declaration, consistent with all preprint usages)
- Seiler adjoint-extension (mathematically valid; bibliographic gap minor)
- C₀(N) formula (Gamma-function integral identity is correct)

The Wave 2 repair FAILS on the one claim it explicitly defers:

**The threshold condition r₃/a < √(3/(4N)) does NOT imply β_max > 0.**

At the threshold boundary m₁a/6 ∼ 0.77 – 1.54 (N=2 to 4), while
ln(c_d K C₀^{1/6}) ≥ 1.91 (using numerical c_d ≈ 6.75) for all N.
β_max is negative at the stated boundary — the KP series diverges
there. The Author's own "self-suspicion" §1 flags this check as
"resolvable by short computation," and the computation (performed
independently above) resolves it negatively.

This is not a presentational gap. It is a structural error in Theorem 4:
the stated range r₃/a < √(3/(4N)) is too large. The correct threshold
requires m₁a/6 > ln(c_d K C₀^{1/6}), which in the worst case (Klarner-
Rivest c_d ≤ Ce^7) demands m₁a ≫ 42, i.e., r₃/a ≪ 1/(21√N).

**Theorem 4's scope statement (line 751: "with r₃/a < √(3/(4N))")
must be replaced by a tighter condition, or the proof must establish
that r₃/a ≪ 1 (not merely < O(1)) within the theorem hypothesis.**

Note that the proof's conclusions remain valid in the physical regime
r₃/a ∼ 10⁻¹⁵, where m₁a/6 ∼ 10¹⁴. The physical-regime application
is sound. The fault is in the stated mathematical boundary.

---

## Repair Required

The Wave 3 repair must:

1. **Replace the threshold in Theorem 4** from r₃/a < √(3/(4N)) to
   an explicit condition ensuring β_max > 0. Candidates:
   - Option (a): r₃/a < 1/(3·ln(c_d)·√N) (derived from the bound,
     using c_d ≤ Ce^7 → r₃/a < 1/(21√N))
   - Option (b): State the theorem only for r₃/a ≤ ε₀(N) where
     ε₀(N) is defined implicitly by β_max(ε₀) = 0, computed
     numerically for each N.
   - Option (c): Add "r₃/a ≪ 1" as a hypothesis (valid for the
     physical application, honest about the limitation).

2. **Correct the C₀(N) formula in Remark 3** to include the (a/r₃)
   suppression factor, or state clearly that the formula is the
   worst-case bound (a/r₃ → 1) and that the threshold must be chosen
   to make the formula self-consistent.

3. **Correct the Appendix A cross-reference in Remark 2** from the
   N=3-specific (p,q) = (0,0) notation to "the constant zero mode of
   the scalar Laplacian" (language valid for all N ≥ 2).

Items 1 and 2 are REQUIRED for the verdict to advance from WEAKENED
to VERIFIED. Item 3 is presentational.

---

## Summary (≤150 words)

THE FRAMEWORK SURFACED A REAL GAP. Three repairs were attempted; two
succeed (r₃ scope declaration, Seiler adjoint-extension sentence), one
fails decisively. The Author's β_max > 0 argument conflates the
physical regime (r₃/a ∼ 10⁻¹⁵, m₁a/6 ∼ 10¹⁴) with the mathematical
threshold boundary (r₃/a = √(3/(4N)), m₁a/6 ∼ 0.77). At the stated
threshold, β_max < 0 for all N ≥ 2 with any rigorous value of the
lattice-animal constant c_d. The threshold in Theorem 4 is too
permissive by a factor of ~6–9 in r₃/a. The physical application
(r₃ ∼ 10⁻³¹ m) remains sound; only the stated mathematical boundary
is wrong. Link 1 remains **WEAKENED** pending replacement of the
threshold condition and correction of the C₀(N) formula's (a/r₃)
dependence.

---

*Verdict: WEAKENED. The core Weitzenböck gap is sound; the KP
convergence boundary is structurally mis-stated. Wave 3 repair:
tighten Theorem 4 threshold or add r₃/a ≪ 1 as explicit hypothesis.*
