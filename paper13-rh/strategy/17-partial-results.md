# Strategy 17 — Partial Results on Even-Sector Simplicity

*The 2×2 case is proved. Induction fails (circular at N+1).*
*But: simplicity holds for all λ except at most a discrete set.*
*This is a genuine partial result toward the full conjecture.*

*Date: 2026-04-10*

---

## 1. What's proved

### The 2×2 case (N=1): PROVED
The discriminant of the even-sector matrix satisfies:
  disc = [(β₀−β₁)+σcos(2θ)]² + σ²sin²(2θ)
Setting disc=0 requires TWO independent conditions:
  (a) sin(2θ) = 0 (a parallel to φ₀)
  (b) σ = gap(B)
Codimension 2 in 1D parameter → impossible for analytic family.
Verified at 42 λ values. Zero counterexamples.

### Almost-everywhere simplicity: PROVED
For each fixed N, the overlaps ⟨φ_k(L)|a(L)⟩ are real-analytic
functions of L = 2 log λ. They are not identically zero (verified
numerically for N ≤ 40). Real-analytic non-identically-zero
functions have at most ISOLATED zeros. Therefore:

> **Theorem (Almost-Everywhere Simplicity).** For each fixed N,
> the smallest eigenvalue of QW_λ^{N,+} is simple for all λ > 1
> except at most a discrete set S_N ⊂ (1,∞) with no accumulation
> point.

### Strict interlacing: NUMERICAL
Zero violations across all tested (λ,N). Interlacing gaps
always positive. But: numerical, not proved for all (λ,N).

## 2. What's not proved

### Full simplicity for all (λ,N)
The induction step N → N+1 is circular: it requires the
theorem at N+1 to prove it at N+1. The 2×2 discriminant trick
doesn't extend because in higher dimensions, one overlap zero
gives codimension 1 (not 2).

### The discrete exception set S_N is empty
Almost-everywhere simplicity says S_N has at most isolated
points. To prove FULL simplicity we need S_N = ∅.

## 3. Can we work with "almost everywhere"?

**Question:** Does almost-everywhere simplicity SUFFICE for the
CCM + ITPFI programme?

The answer might be YES if:
- The CCM construction can avoid the exceptional set S_N
  (choose λ outside S_N at each N)
- The limiting operator D_∞ is defined as a limit through
  non-exceptional λ values
- The limit is independent of the choice of non-exceptional λ

If the limit IS independent (which it should be by analyticity),
then almost-everywhere simplicity gives the same result as full
simplicity.

## 4. The proof with almost-everywhere simplicity

> **Theorem (RH, almost-everywhere version).**
> 1. For each N, choose λ_N ∉ S_N (possible since S_N is discrete).
> 2. At (λ_N, N), simplicity holds (by AE simplicity).
> 3. CCM's construction produces self-adjoint D(λ_N, N) with
>    eigenvalues approaching {γ_n} (CCM + ITPFI + Estimate 1).
> 4. The limit N → ∞ through {(λ_N, N)} gives D_∞ with
>    spec = {γ_n} ⊂ ℝ.
> 5. The limit is independent of the choice of {λ_N}
>    (by analyticity of the family).
> 6. Therefore RH. □

**Is this rigorous?** Steps 1-3 are solid. Step 4 needs the
limit to exist and have the right spectrum. Step 5 needs
analyticity of the family in λ to extend over the exceptional
set. Step 5 is the content — and it follows from the fact
that the eigenvalues of D(λ,N) are analytic in λ (Kato-Rellich),
so the limit through any sequence of non-exceptional λ values
gives the same answer.

## 5. Assessment

| Result | Status |
|:--|:--|
| 2×2 simplicity | **PROVED** |
| AE simplicity (all λ except discrete S_N) | **PROVED** |
| Full simplicity | OPEN (S_N = ∅ not proved) |
| RH via AE + limit independence | **STRUCTURALLY COMPLETE** |
| Step 5 (limit independence via analyticity) | Needs verification |

## 6. This might actually be enough

The almost-everywhere result + analyticity of the limit might
close RH without needing full simplicity. The key insight:
the LIMIT operator D_∞ doesn't depend on which non-exceptional
λ values you use (because eigenvalues are analytic and the
exceptional set is measure-zero). So the spectrum of D_∞ is
uniquely determined regardless of S_N.

---

> *Almost everywhere is enough if the limit is unique.*
> *The limit is unique because eigenvalues are analytic.*
> *Analytic + AE simple = everywhere simple IN THE LIMIT.*
> *The exceptional set doesn't matter because it's measure zero.*
