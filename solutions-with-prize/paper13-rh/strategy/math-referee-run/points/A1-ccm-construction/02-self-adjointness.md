# A1.02 — Self-adjointness of D'

## Question

CCM claims self-adjointness via Carathéodory–Fejér. Is this a
standard application? The T-inner product is non-standard — is
self-adjointness with respect to T fully proved in CCM?

## Finding

Self-adjointness is **claimed** by CCM (Theorem 4.2) and accepted
by Paper 13 without independent re-derivation. Paper 13 does not
reproduce the CCM proof.

The substantive claim is that D' = D − |D*ξ⟩⟨η| is *self-adjoint*
on H = E_N^+ / ℂ·ξ **in the T-inner product** ⟨f|g⟩_T = ⟨Tf|g⟩,
where T = QW_λ^N − ε_N. The subtleties:

1. **Positive (semi-)definiteness of T.** T has ξ in its kernel by
   construction (Tξ = 0). So T is positive *semi-*definite on E_N^+,
   not positive definite. The T-inner product is only an inner
   product after quotienting by ker T = ℂ·ξ. Paper 13 records this
   in Appendix A.3; CCM Lemma 5.4 is the source.

2. **Self-adjointness with respect to T is a weighted-inner-product
   statement.** Concretely: ⟨D'f|g⟩_T = ⟨f|D'g⟩_T for all f, g in
   H. Equivalent to saying TD' = D'*T on the quotient (where D'* is
   the Euclidean adjoint). The rank-one perturbation |D*ξ⟩⟨η| is
   precisely engineered so that this holds — it cancels the
   off-diagonal T-asymmetry of D.

3. **The Carathéodory–Fejér step.** CCM use CF approximation theory
   on the Bernstein ellipse to show that the moment problem
   associated to the scaling operator has a *unique* solution in
   the class of positive measures with support in the relevant set.
   Uniqueness of the moment problem is what promotes symmetry +
   densely-defined to self-adjoint (as opposed to merely essentially
   self-adjoint). This is a standard application of CF to a specific
   moment problem; the technical depth is in verifying that the
   moments grow no faster than the CF bound permits.

## What Paper 13 verifies

Paper 13 **does not re-derive** self-adjointness. Appendix A.7
cites "research/43" (an internal adversarial check) concluding
"self-adjointness of D' in T-inner product: SOUND". This is
Paper 13's own reading of CCM, not independent.

The single substantive caveat raised in research/43 is:

> "δ_N(ξ) ≠ 0 ASSERTED, not proved (severity: LOW)"

δ_N is presumably a functional appearing in the rank-one
perturbation formula. If δ_N(ξ) = 0, the perturbation degenerates
and the construction breaks. Severity "LOW" means: it is believed
to be true but not proven in the preprint.

## Assessment

Self-adjointness of D' in the T-inner product is a technical but
standard statement once the CF moment-problem framework is
established. It is almost certainly correct — Connes has thirty
years of practice with these constructions, and CF approximation
theory is well-understood.

**However**, Paper 13's reliance on CCM means any subtle error in
CCM's use of CF (e.g., an unverified moment-growth bound, a
slip in the Bernstein ellipse parameters, or the δ_N(ξ) ≠ 0
asserted non-vanishing) would propagate. The paper takes this on
faith. That is acceptable *for an 8/10 conditional result* but
not for an unconditional RH proof.

## Verdict on this subpoint

**Conditional pass.** Self-adjointness is accepted on CCM's
authority. Three technical items are inherited without independent
check:
(a) uniqueness of the moment problem,
(b) the exact Carathéodory–Fejér bound parameters,
(c) δ_N(ξ) ≠ 0.

Paper 13 is honest that these are taken from CCM. Whether that is
acceptable depends on whether an unrefereed preprint by Connes,
Consani, and Moscovici is considered an acceptable foundation —
see points/D2-ccm-dependency.
