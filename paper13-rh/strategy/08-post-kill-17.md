# Strategy 08 — After Kill #17: The Invariant Subspace Question

*Gradient flow works on H₁ (compact resolvent proved). But H₁*
*has spectrum {log n}, not {γ_n}. Kill #17.*

*The surviving lemma: if H_R is a T_BC-invariant subspace of H₁,*
*its heat kernel inherits trace-class → pure point → RH.*

*The question collapses to: does such a subspace exist?*

*Date: 2026-04-10*

---

## 1. Kill #17 summary

The gradient flow e^{-tT_BC²} on H₁ gives:
- Compact resolvent: PROVED (heat trace converges)
- Spectrum on H₁: {log n} (not {γ_n})
- Five orders of magnitude between the two spectra
- The explicit formula can't bridge them (Gaussian test function invalid)

## 2. The surviving lemma

**Lemma (gradient flow inheritance).** If H_R ⊂ H₁ is a closed
T_BC-invariant subspace, then T_BC|_{H_R} inherits compact
resolvent from T_BC on H₁. Therefore T_BC|_{H_R} has purely
discrete spectrum.

*Proof sketch.* The heat semigroup e^{-tT²} restricted to an
invariant subspace is still trace-class (restriction of a
trace-class operator to an invariant subspace is trace-class).
Trace-class heat kernel → compact resolvent → discrete spectrum. □

## 3. The new question

> **Does there exist a closed, T_BC-invariant subspace H_R ⊂ H₁
> such that spec(T_BC|_{H_R}) = {γ_n}?**

This is a WEAKER question than general spectral realisation:
- General: construct H_R and T_BC from scratch
- This version: find H_R as a SUBSPACE of H₁ (which we have)

The advantage: H₁ exists, T_BC on H₁ is well-understood, and
compact resolvent is already proved on H₁. The only question is
whether the right subspace exists.

## 4. Known constraints on H_R

If H_R ⊂ H₁ exists with spec = {γ_n}:
- dim H_R = countably infinite (one eigenvector per γ_n)
- H_R is orthogonal to the {log n} eigenvectors of T_BC on H₁
  (since {γ_n} ∩ {log n} = ∅ — disjoint spectra)
- H_R lives in the ORTHOGONAL COMPLEMENT of the point spectrum
  subspace of H₁

Wait — T_BC on H₁ has POINT spectrum {log n}. If T_BC also has
eigenvectors at {γ_n} in H₁, they'd be in the orthogonal complement.
But Reed-Simon says: a self-adjoint operator's eigenvectors for
distinct eigenvalues are orthogonal. So {γ_n}-eigenvectors ⊥ {log n}-
eigenvectors. The question: does T_BC have eigenvectors at {γ_n}
in H₁ at all?

Meyer says: distributional eigenstates exist in S' at {γ_n}.
But S' ⊃ H₁ — they might not be IN H₁.

This is EXACTLY the spectral realisation problem restated as:
"are Meyer's distributional eigenstates in H₁ or only in S'?"

## 5. The 17 kills and where we are

| Kill # | Route | What it taught us |
|:--|:--|:--|
| 1-2 | Coboundary | Topology can't detect continuous perturbation |
| 3-4 | Index/Penrose | Category errors |
| 5-7 | Chern/Weil/flow | Self-adjoint → real; zero index; wrong direction |
| 8-11 | KMS/Weyl/predictions/measure | H₁ ≠ H_R; predictions invisible to extras |
| 12-14 | RAGE/ITPFI/Meyer | Wrong operator; circularity |
| 15-16 | Nuclear rigging/moments | Distributional spectrum = ℝ; tautological |
| **17** | **Gradient flow** | **Compact resolvent on H₁ (proved!), but wrong spectrum** |

## 6. What remains

The problem is precisely:

> **Are the Riemann zeros eigenvalues of T_BC IN H₁,**
> **or only distributional eigenvalues in S' \ H₁?**

If in H₁ → they span a T_BC-invariant subspace H_R → compact
resolvent inherited → pure point → RH.

If only in S' → Meyer's result is the best we can do → spectral
realisation remains open.

This is the Connes programme in its sharpest possible formulation.

---

> *17 kills. Each one sharpened the question.*
> *The question is now one sentence:*
> *Are Meyer's eigenstates in H₁ or only in S'?*
