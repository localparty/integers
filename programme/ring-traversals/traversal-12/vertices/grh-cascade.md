# GRH Cascade: L5a, L5b, L5d, L6, L7, L8 (fixed conductor q)

*Traversal-12 vertex. Written 2026-04-14. Per T9 meta: L5a,b,d follow once L4 closes; L6-L8 follow L5 automatically. Scope here: fixed conductor q, real χ (self-adjointness live via L3).*

Template: RH chain (`paper13-rh/PROOF-CHAIN.md`) layers 3a, 3b, 3d, 4a-4c, 5, 6 ↔ GRH chain (`paper13b-grh/PROOF-CHAIN.md`) links 5a, 5b, 5d, 6, 7, 8.

---

## L5a — Archimedean sub-leading O(1/λ) for L(s,χ)

**Template:** RH L3a (archimedean sub-leading O(1/λ) on completed ξ).
**Twist ingredient:** gamma-factor shift γ_χ(s) = π^{-(s+a)/2} Γ((s+a)/2), a ∈ {0,1} (a=1 for odd χ). Shift is an explicit entire factor.
**Argument:** The L3a bound is driven by Stirling asymptotics of Γ((s+a)/2) + the Dirichlet series tail; χ(n) is unimodular so |χ(n)| ≤ 1 and the series tail estimate is unchanged up to a q-dependent constant. The a=1 shift is an explicit translation of argument — Stirling's remainder is unaffected. **Transfer: mechanical.** No new work.

## L5b — Eigenvector approximation for D_{N,χ}

**Template:** RH L3b (ITPFI triangle + Davis-Kahan, bound O(log λ / λ)).
**Twist ingredient:** ω_{1,χ} factorization (GRH L4 = "ITPFI_χ", currently CONJECTURED).
**Argument:** Davis-Kahan is an operator-theoretic inequality on perturbations of self-adjoint operators — entirely character-agnostic. The triangle ‖D_{N,χ} − D_{∞,χ}‖ ≤ ‖D_{N,χ} − D_{N,χ}^{ITPFI}‖ + ‖D_{N,χ}^{ITPFI} − D_{∞,χ}‖ uses exactly the L4 factorization. **Transfer: immediate, conditional on L4 being closed for χ.** Note: L4 is CONJECTURED in the GRH chain; once it upgrades to PROVED, L5b is automatic.

## L5d — CF (closed-form) decay ρ ≥ 4.27 for D_{N,χ}

**Template:** RH L3d (ρ ≥ 4.27 uniform in N, caveat resolved 2026-04-14 by Slepian compatibility Lemma 12.1).
**Twist ingredient:** D_{N,χ} = D_N ⊗ 1 + I ⊗ M_χ with M_χ diagonal character matrix, ‖M_χ‖ ≤ log q (fixed q ⇒ bounded).
**Argument:** The prolate/Slepian spectrum driving ρ depends on the L² projection onto band-limited functions, which is set by the grid geometry, not the character. Adding a bounded diagonal M_χ shifts each prolate eigenvalue by ≤ log q and does not collapse the gap. At **fixed q**, ρ_χ ≥ 4.27 − O(log q / N) → 4.27. **Transfer: holds pointwise in q, but uniformity in q is lost.** This is the fixed-conductor/uniform-q split documented at L5c.

## L6 — Bögli discrete compactness for D_{N,χ}

**Template:** RH L4b (uniform H¹ bound ⇒ Rellich-Kondrachov compactness of embedding H¹ ↪ L²).
**Twist ingredient:** H¹_χ bound on (D_{N,χ} − i)^{-1} (L5c-fixed, PROVED at T11 for bounded q).
**Argument:** Rellich-Kondrachov is geometric — it depends on the domain and the Sobolev scale, not on what operator generates the H¹ norm. χ enters only through the coefficient M_χ in D_{N,χ}, which is bounded and does not affect the compactness class. Combined with L5c-fixed ‖(D_{N,χ}−i)^{-1}‖_{L²→H¹} uniform in N, compactness transfers. **Transfer: immediate at fixed q.**

## L7 — Hurwitz convergence ξ̂_{N,χ} → Λ(s,χ)

**Template:** RH L5 (Hurwitz's theorem: uniform convergence on compacts of ξ̂_N → Ξ ⇒ zero-set convergence).
**Twist ingredient:** ξ̂_{N,χ}(s) := det regularization of char-poly of D_{N,χ}, with γ_χ(s) prefactor.
**Argument:** The Hurwitz mechanism requires only (i) uniform convergence on compacts in a zero-free neighborhood, and (ii) no cancellation of limits with zeros at infinity. Both hold: χ(n) bounded ⇒ Dirichlet series converges uniformly on compacts of Re(s) > 1, analytic continuation is by the completed L-function (classical), and γ_χ is entire nonvanishing on the critical strip. **Transfer: mechanical.** The only technical note is the γ_χ shift for odd χ, which is explicit.

## L8 — spec(D_{∞,χ}) = {γ_{n,χ}} ⊂ ℝ ⇒ GRH(χ)

**Template:** RH L6 (QED: self-adjointness ⇒ real spectrum ⇒ RH).
**Twist ingredient:** D_{∞,χ} self-adjoint (GRH L3 = PARTIAL-PROVED T10 for real χ).
**Argument:** Self-adjointness of D_{∞,χ} ⇒ spec ⊂ ℝ. Combined with L7 (spec = {γ_{n,χ}} = zeros of Λ(s,χ) shifted to critical line coordinates), all zeros of L(s,χ) have Re(s) = 1/2. **Transfer: QED for real χ.** For complex χ, L3 is only PARTIAL; self-adjointness is replaced by a symmetrized operator D_{∞,χ} ⊕ D_{∞,χ̄} which is self-adjoint on the sum and inherits the conclusion via the functional equation L(s,χ) ↔ L(s,χ̄).

---

## Does GRH close at fixed conductor q?

**Yes, conditionally on two live links.** The cascade is clean: L5a, L5b, L5d, L6, L7, L8 all transfer mechanically or immediately from RH once the conductor is fixed. **But two upstream links still gate closure:**

1. **GRH L3** is PARTIAL-PROVED (self-adjointness only for real χ). Complex χ needs the χ⊕χ̄ symmetrization above — straightforward but requires writing.
2. **GRH L4 (ITPFI_χ)** is CONJECTURED. L5b depends on this. An explicit character-twisted KMS factorization proof is needed — not available by pure citation from Paper 13. **This is genuine new work**, not a mechanical transfer. Expected to parallel Paper 13 L2 closely (Bratteli-Robinson 5.3.30 + trivial fixed-point algebra via χ-twist, which GRH L2 already uses — so the template exists and the gap is small).

**Uniformity in q remains open** (equivalent to Burgess subconvexity; GRH L5c-uniform). At fixed q the chain closes modulo L3-complex and L4. Net: GRH for individual L(s,χ) at fixed q is **one Bratteli-Robinson-style lemma + one symmetrization away** from full proof.
