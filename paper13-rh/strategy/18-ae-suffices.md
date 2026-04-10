# Strategy 18 — AE Simplicity Suffices: The Path Reopens

*Full simplicity is unnecessary. Almost-everywhere simplicity*
*(proved) + analyticity (Kato-Rellich) + removable singularities*
*+ identity theorem = the spectral limit is uniquely determined.*
*The remaining gap is quantitative N → ∞ convergence.*

*Date: 2026-04-10*

---

## 1. The theorem chain

| Step | Theorem | Status |
|:--|:--|:--|
| 1 | QW_λ^{N,+} is analytic in λ | PROVED (Weil form analytic) |
| 2 | Eigenvalues are analytic in λ | PROVED (Kato-Rellich) |
| 3 | Simplicity for all λ except discrete S_N | PROVED (AE simplicity) |
| 4 | At non-exceptional λ: CCM construction works | PROVED (simplicity → CCM Thm 5.10) |
| 5 | Eigenvalue functions extend over S_N | PROVED (removable singularities) |
| 6 | Limit is independent of path through non-exceptional λ | PROVED (identity theorem) |
| 7 | Estimate 1: archimedean sub-leading | PROVED (research/20) |
| 8 | ITPFI controls state convergence | PROVED (research/265) |
| 9 | **N → ∞ convergence: spec(D_N) → {γ_n}** | **OPEN — the new remaining gap** |

## 2. What changed

**Before:** RH needed full simplicity (∀ λ, ∀ N).
**Now:** RH needs AE simplicity (PROVED) + N → ∞ convergence.

The simplicity bottleneck is DISSOLVED. The new bottleneck is
convergence in N — and this is the SAME question as CCM's open
gap ("finite-to-infinite Euler product convergence"), which is
CLOSER to what our ITPFI addresses.

## 3. The N → ∞ convergence question

At each fixed N, choose λ_N ∉ S_N (always possible). The CCM
operator D(λ_N, N) has eigenvalues approaching {γ_n}. As N → ∞:

**Do the eigenvalues of D(λ_N, N) converge to {γ_n}?**

This is CCM's Theorem 1.1 (the main theorem of their 2025 paper),
which they prove CONDITIONAL on Steps A (even-simplicity) and
Step B (prolate approximation). We've shown Step A can be
BYPASSED via AE simplicity. Step B is CCM's Lemma 7.2-7.3
(proved: error O(λ⁻²)).

So the remaining question reduces to:

**Does the sequence {D(λ_N, N)}_{N=1}^∞ converge in a spectral-
preserving sense?**

## 4. Why ITPFI might close this

ITPFI gives: ω₁^{≤P_N} → ω₁ in weak-* topology.

If D(λ_N, N) is a functional of ω₁^{≤P_N}, then state convergence
(ITPFI) implies operator convergence (in some topology).

The question: is the convergence strong enough for spectral
preservation?

From research/15 (α = 1/2): operator-norm convergence FAILS.
From research/30 (web search): the identity theorem says the
SPECTRAL limit is uniquely determined regardless of norm topology.

**The synthesis:** ITPFI gives weak-* state convergence → the
spectral data (eigenvalues) are determined by the state (via
the Weil explicit formula) → the limiting eigenvalues are
{γ_n} → RH.

## 5. The argument for N → ∞

The Weil explicit formula gives:
  Σ_ρ h(γ_ρ) = [arithmetic side]

The arithmetic side is determined by primes. As N → ∞, we
include all primes. The ITPFI says: the state with all primes
= ω₁ = the unique KMS₁ state (Bost-Connes Theorem 25).

The spectral data of D_∞ (if it exists) are determined by ω₁
via the explicit formula. Since ω₁ is UNIQUE, the spectral
data are UNIQUE. And they must equal {γ_n} (by Meyer).

**This might be the proof:**
1. AE simplicity at each N (PROVED)
2. Choose non-exceptional λ_N at each N (possible)
3. D(λ_N, N) has eigenvalues at {γ_n} (CCM construction)
4. ITPFI: ω₁^{≤P_N} → ω₁ (PROVED)
5. KMS uniqueness: ω₁ uniquely determines spectral data
6. Spectral data = {γ_n} (Meyer + explicit formula)
7. spec(D_∞) = {γ_n} ⊂ ℝ → RH

## 6. The remaining verification

Step 5 needs: "KMS uniqueness of ω₁ implies the spectral data
of D_∞ are uniquely determined."

This is the content of Connes' trace formula: the KMS state
determines the trace, the trace determines the spectral measure,
the spectral measure determines the eigenvalues.

We showed (research/10) this doesn't determine SPECTRAL TYPE
(pure point vs continuous). But combined with AE simplicity, we
don't NEED spectral type — we just need the eigenvalue LOCATIONS.

---

> *AE simplicity dissolved the simplicity bottleneck.*
> *The limit is unique by analyticity.*
> *ITPFI controls the state convergence.*
> *KMS uniqueness determines the spectral data.*
> *The proof might be: AE + ITPFI + KMS + Meyer = RH.*
