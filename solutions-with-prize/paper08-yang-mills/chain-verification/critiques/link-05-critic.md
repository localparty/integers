# PCA Critic Report — Link 5 (B2): Block-spin kernel complexification / SL(N,ℂ) extension

**Date:** 2026-04-13
**Target:** Chain step 5 of 18, Node 06
**Prior status:** [CONFIRMED] (Run 2/3)
**Critic verdict:** SURVIVED (one WEAKENING noted, no BREAK)

---

## Attack-by-attack assessment

### Attack 1 — Cauchy contour and degenerate spectra near r_proj = 1/2

**Verdict: SOUND.**

The concern is whether spec(A†A) stays inside the contour for all A with ‖A−1‖_op < 1/2. The bound is: σ_min(A) ≥ 1 − ‖A−I‖_op (from inf_{‖x‖=1}‖Ax‖ ≥ 1 − ‖A−I‖_op), so at ‖A−I‖_op < 1/2, σ_min(A) > 1/2, hence λ_min(A†A) > 1/4. The contour at radius 1/8 centred on the positive real axis encloses all of spec(A†A) ⊂ [1/4, ∞) strictly. No degenerate eigenvalue can reach 0 inside this ball. The holomorphic functional calculus applies uniformly over the ball. Attack FAILS.

### Attack 2 — Tightness of r_proj = 1/2

**Verdict: SOUND (non-issue).**

The [CONFIRMED] text explicitly writes r_proj = 1/2 "for instance," making no claim of tightness. The only structural claim is that r_proj depends on N alone, not k. A larger ball (smaller r_proj) would require a different sufficient condition on λ_min, but as an existence statement the argument is correct as written. The slack in the radius does not weaken the chain. Attack FAILS.

### Attack 3 — N-dependence vs. lattice-scale dependence of r_proj

**Verdict: SOUND.**

The bound λ_min(A†A) ≥ (1 − ‖A−I‖_op)² depends only on ‖A−I‖_op < 1/2 and involves no k-dependent quantity. The choice r_proj = 1/2 is purely a statement about operator norms on ℂ^N×N; no lattice spacing, block size, or RG-step parameter enters. The claim "r_proj(N) depends on N only" is upheld. Attack FAILS.

### Attack 4 — det(V) smallness and pole in 1/det(V) on the complexified domain

**Verdict: SOUND.**

On SL(N,ℂ), det(V) = 1 is a defining constraint, not a quantity that can become small. The formula V^{-1} = adj(V)/det(V) therefore reduces to V^{-1} = adj(V), which is a polynomial in the entries of V. There is no pole. The extension of polymer activities to SL(N,ℂ) is genuinely polynomial in the matrix entries, and the analyticity radius is unaffected. The [CONFIRMED] text records this correctly. Attack FAILS.

### Attack 5 — Principal-bundle gauge structure not preserved by algebraic extension

**Verdict: WEAKENING (not a break).**

The [CONFIRMED] argument establishes that polymer activities extend analytically to a neighborhood of 1 ∈ SL(N,ℂ) and that the block-spin projection map A ↦ A(A†A)^{-1/2} is locally analytic there. What is NOT explicitly verified is that the complexified projection respects the principal SU(N)-bundle structure globally, i.e., that the block-spin averaging map from SL(N,ℂ)-valued link configurations to the coarse SU(N) lattice is well-defined as a bundle map (not merely a set map). The polar decomposition A = U·P gives a local diffeomorphism near 1, which is sufficient for the local analyticity claim used in the proof. However, if a referee asks whether the gauge-equivariance of the block-spin map is preserved under complexification — specifically, whether gauge transformations g ∈ SL(N,ℂ) acting on A are compatible with the projection — this is left implicit.

**Severity:** LOW. The proof only requires local analyticity of the kernel near 1, which is established. The global bundle claim is not logically necessary for the chain step. A one-line remark noting that gauge equivariance on SL(N,ℂ) follows from equivariance of the polar decomposition under unitary conjugation (U(A†A)^{-1/2} = (UA†AU^†U)^{-1/2}U is straightforward for unitary U, and for full SL(N,ℂ) gauge transformations the block-spin map is a local construction that does not need global equivariance) would fully close the gap.

**Recommended repair:** Add one sentence to the [CONFIRMED] block: "Gauge equivariance of the projection under SL(N,ℂ) is not required globally; the block-spin average is a local construction at each block, and the polar decomposition commutes with unitary conjugation, which is all that the inductive argument uses."

---

## Overall verdict

**SURVIVED.**

Four of five attacks fail cleanly. Attack 5 identifies a minor implicit assumption (global bundle equivariance) that is not needed for the actual logical step but could attract a referee question. No logical gap in the proof chain is introduced. The node remains [PROVED] with a recommended clarifying remark for the SL(N,ℂ) gauge-equivariance point.

---

## Summary (≤150 words)

All five attacks on Link 5 fail to break the argument. Attack 1 (degenerate spectrum) is neutralised by σ_min(A) ≥ 1 − ‖A−I‖_op, placing λ_min(A†A) ≥ 1/4 safely inside the Cauchy contour. Attack 2 (tightness of r_proj) is a non-issue since the argument makes no tightness claim. Attack 3 (lattice-scale dependence) fails because r_proj = 1/2 involves no k-dependent quantity. Attack 4 (det(V) pole) fails because SL(N,ℂ) fixes det = 1, making V^{-1} = adj(V) polynomial. Attack 5 (principal-bundle structure) is a WEAKENING: the argument is locally correct but does not explicitly state that gauge equivariance of the polar decomposition is the only structure needed. A one-sentence clarification closes this gap. Node 06 is SURVIVED; recommend adding the gauge-equivariance remark.
