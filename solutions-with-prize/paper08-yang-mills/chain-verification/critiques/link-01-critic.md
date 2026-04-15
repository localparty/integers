# Link 1 Critic verdict

**Target:** KK spectral gap Δ₀^KK > 0 (Thm 4)
**Source:** preprint/sections/04-lattice-proof-part1.md §4 (Theorems 1–4)
**Verdict:** WEAKENED
**Confidence:** 7/10

---

## Attacks attempted

1. **Weitzenböck-Bochner hypothesis (positive Ricci on KK fiber) actually satisfied?**
   Result: *bounced.* The fiber is CP^{N-1} with Fubini-Study metric, which is Einstein
   with Ric = (2N/r₃²)g > 0 for all N ≥ 2. The computation is standard and correct.
   No issue here.

2. **Gap Δ₀^KK quantitative vs. qualitative only — does it survive metric perturbations?**
   Result: *exposes gap.* Theorem 1 establishes the Weitzenböck lower bound
   μ₁ ≥ 2N/r₃² at the Fubini-Study metric. The proof is pointwise at A = 0 (the flat
   connection) and exploits the fixed, unperturbed fiber metric. The paper does not
   prove that the spectral gap is *stable under perturbations of the fiber metric* away
   from the round Fubini-Study metric. If the radius r₃ is treated as a dynamical
   modulus (there is a volume zero mode noted in Appendix A) rather than a fixed
   parameter, the gap 2N/r₃² is not invariant — r₃ → ∞ drives μ₁ → 0. The paper
   freezes r₃ at a fixed value by fiat (§1.5), but no stabilization mechanism for r₃
   is proved within the chain; it is an assumption. This is not fully fatal (the proof
   works for any fixed r₃ > 0) but constitutes an unacknowledged assumption that r₃
   does not relax to ∞ in the quantum theory.

3. **Cluster expansion convergence relies silently on small coupling / UV stability not
   yet established at this step?**
   Result: *exposes gap (moderate).* Theorem 2 (bond activity bound) uses the Gaussian
   approximation (free-field propagator) around A = 0 in the k = 0 sector. The
   derivation invokes the inequality |e^{-t}−1| ≤ |t| for |t| ≤ 1 "under the integral,"
   with the claim that V^{bond} is small in the k=0 sector. No explicit bound on
   ‖V^{bond}‖_∞ or its L¹-norm under the free Gaussian measure is given before
   invoking the inequality; the argument is implicitly relying on m₁a ≫ 1 (which holds
   at the physical hierarchy) but this is a regime assumption, not a proved bound at
   this step. For a/r₃ close to √(3/(4N)) (the stated threshold in Theorem 4), the
   argument becomes thin. The constant C₀ in the bond activity bound is stated to
   depend on N but its explicit value is never computed; the KP criterion is therefore
   not checkable numerically without knowing C₀. This is a presentational gap rather
   than a logical hole, but it weakens the claim from "proved" to "proved modulo an
   unspecified N-dependent constant."

4. **Scalar Laplacian conflated with vector (gauge-field) Laplacian?**
   Result: *bounced.* The paper is careful on this point. Theorem 1 and Appendix G both
   explicitly work with the Hodge Laplacian Δ_Hodge on 1-forms (gauge potentials), not
   the scalar Laplacian. Appendix A (scalar spectrum) is used only for the zero-mode
   counting and is not conflated with the 1-form spectrum. The Weitzenböck identity
   Δ_Hodge a = ∇*∇a + Ric(a) is correctly stated for 1-forms. No conflation detected.

5. **N=2 edge case — does the result hold?**
   Result: *bounced.* The paper explicitly states the bound holds for all N ≥ 2.
   For N = 2, Ric = (4/r₃²)g > 0, H¹(CP¹) = 0, and the first eigenvalue of
   Δ_Hodge on 1-forms on CP¹ is 4N/r₃² = 8/r₃² > 0. The adjoint Casimir for SU(2)
   is not zero (C₂(adj) = 2), so no special degeneracy breaks the gap. The argument
   is uniform in N ≥ 2.

6. **Silent conditional assumption inherited from a Balaban reference?**
   Result: *exposes gap (minor).* The bond activity bound in Step 3 of Theorem 2
   cites "Lüscher 1977, Seiler 1982 Ch. 4" for the lattice energy bound
   m_n^{latt} a ≥ m_n a − O(ln(m_n a)), which yields G_n(a) ≤ (C₁/m_n a)e^{−m_n a}.
   The cited Seiler 1982 result is for the scalar field; its extension to adjoint scalars
   (the φ_n fields) on a 4D hypercubic lattice requires gauge-invariance of the
   propagator bound. The paper applies the result without verifying that the adjoint
   group action Ad(U_{xy}) does not spoil the transfer-matrix argument. For SU(N) with
   compact group elements, the adjoint action is unitary and bounded, so the bound
   extends straightforwardly, but this step is not written out. This is a minor gap
   that a diligent referee would flag.

---

## Gap description (WEAKENED)

**Primary gap:** The spectral gap μ₁ ≥ 2N/r₃² is proved for fixed r₃, but the proof
does not establish that r₃ is stabilized dynamically. The volume modulus (the constant
zero mode of the scalar Laplacian, Appendix A, (p,q) = (0,0)) is unfixed. If r₃ is
treated as a quantum degree of freedom, the gap 2N/r₃² has no uniform lower bound
away from zero. The proof implicitly treats r₃ as a classical fixed parameter, which
must be stated as an explicit hypothesis of Theorem 1.

**Secondary gap:** The constant C₀ in Theorem 2 is never computed explicitly. The KP
convergence bound Theorem 3 contains ln(c_d K C₀^{1/6}) as a subleading term; at
moderate a/r₃ (near the threshold √(3/(4N))), the sign and magnitude of this term
affects whether β_max(a) is actually positive. This is resolvable but currently unverified.

**Literature needed:** A moduli stabilization argument for r₃ (e.g., showing the
quantum effective potential for the volume modulus is bounded below, or that the
theory is defined only in the sector where r₃ is pinned), and an explicit computation
or upper bound for C₀.

---

## Repair proposal

1. **Add to Theorem 1** an explicit hypothesis: "r₃ is a fixed positive parameter of
   the model (the fiber radius), not a dynamical field. The spectral gap bound
   μ₁ ≥ 2N/r₃² holds for each fixed r₃ > 0 and is uniform on compact sets
   {r₃ ≥ ε} for any ε > 0."

2. **In Remark 2 after Theorem 1**, add: "The volume modulus of CP^{N-1} is frozen
   because the model is defined by fixing the Fubini-Study metric as part of the
   background data; it is not a quantized degree of freedom in this construction."

3. **In Theorem 2 / Step 4**, provide an explicit upper bound for C₀ in terms of N
   (e.g., C₀ ≤ (2N)^{N-1} · C(Weyl) or cite a specific lemma), or add a remark
   confirming that β_max(a) > 0 for all r₃/a < √(3/(4N)).

4. **In Step 3 of Theorem 2**, add one sentence: "The adjoint action Ad(U) is unitary
   on ℝ^{N²-1} for U ∈ SU(N), so the Seiler 1982 scalar propagator bound extends
   to adjoint-valued fields without modification."

---

## Summary

The Weitzenböck-Bochner argument for the KK spectral gap is mathematically sound for
fixed fiber radius r₃ and is correctly restricted to the scalar (Hodge) Laplacian on
1-forms. The verdict is WEAKENED, not BROKEN, because the core inequality
μ₁ ≥ 2N/r₃² is correct but the proof silently assumes r₃ is fixed (not a dynamical
modulus), the constant C₀ controlling the KP threshold is never computed, and the
extension of the Seiler scalar propagator bound to adjoint fields is asserted without
proof. All three gaps are closable by short additions with no new mathematics.
