# Link 12 Critic — RG Recursion C_{k+1} = C_k/4 + C_new

**Verdict: SURVIVED (with notation flag)**

## Attack Results

**Attack 1 (1/4 factor normalization):** FAILS. The factor 1/4 is purely kinematic: the physical matrix element is unchanged between bare theories K and K+1; it is merely reexpressed in the new dimensionless unit Δ̂²_{K+1} = Δ̂²_K/4. Section 5.4.3b is explicit. No implicit contribution-counting error.

**Attack 2 (transient growth pushing Δ̂_k near zero):** FAILS. Δ̂_k is a kinematic quantity fixed by the bare-scale geometry (Δ̂_K² = (a*Δ_phys)²·4^{-K}), not a dynamical variable driven by C_k. Transient growth affects C_k, not Δ̂_k. The non-perturbative polymer bound covers the finitely many strong-coupling inner steps k < k₀(K), and k₀(K) is non-increasing in K (§5.4.6).

**Attack 3 (K-dependence of C_new):** FAILS. The recursion explicitly allows C_new(K) to be K-dependent. K-uniformity C_new(K) ≤ C_* is claimed resolved via Hastings–Koma + Appendix M Lemmas M.1.1–M.1.2.

**Attack 4 (positivity):** FAILS. C_new is defined as the absolute-value upper bound constant from §5.4.4; it is non-negative by definition. Induction preserves C_K ≥ 0.

**Attack 5 (initial condition direction):** FAILS as a break. The outer index K and inner index k are explicitly disambiguated (§5.4.1). Notation flag: the fixed-point formula C_K = C_{**} + (C_0 − C_{**})·4^{-K} stated in §5.4.6 is inconsistent with the O(g_K^2 C_K) correction in the boxed recursion, which produces polynomial growth C_K ≲ K^γ, not convergence to a fixed point. The paper corrects itself two paragraphs later and shows the outer sum ΣC_K g_K^4 Δ̂_K² converges anyway. The summary table entry "Recursion for C_k has bounded fixed point — Proved" overstates: the result is a bounded orbit with polynomial growth, not a genuine fixed point. This is a presentational inconsistency, not a logical error.

## Summary

All five attack vectors fail to break the link. The 1/4 contraction is correct, positivity and K-uniformity hold, transient growth does not destabilize Δ̂_k, and the flow direction is properly set. The single flag is a notational inconsistency between the fixed-point formula and the O(g_K^2) correction: the table claims convergence to a fixed point, but the actual result is a bounded polynomial orbit whose outer sum converges by the 4^{-K} factor. This weakens the presentation but not the mathematical conclusion. **SURVIVED.**
