## Part G, Point 4: Local Field Operators, Stress Tensor, OPE, and AF Matching

**Weight:** HEAVY
**Verdict:** GENUINE GAP (for Clay compliance)

**Finding:**

This Point bundles four Clay-mandated requirements from Jaffe–Witten §4 that the paper explicitly acknowledges as unresolved (PROOF-CHAIN IV.5, Appendix L).

**(a) Local field operators in correspondence with curvature polynomials.** The preprint constructs Schwinger functions of gauge-invariant observables (Wilson loops, plaquette traces). These are NOT local field operators in the Wightman sense — Wilson loops are non-local (they depend on paths, not points). The Jaffe–Witten requirement is for operator-valued distributions $\mathrm{Tr}\,F_{ij}F_{kl}(x)$ on the reconstructed Hilbert space, in correspondence with classical curvature polynomials.

The paper states this as Conjecture L.1 (Appendix L): the construction of $[\mathrm{Tr}\,F^2]_R(x)$ as limits of multiplicatively renormalized lattice operators is an open problem. The paper is explicit: "A Clay submission cannot honestly claim that any of L.1–L.4 are established by the main body."

**Status: GENUINE GAP.** Without local field operators, the constructed theory is a collection of Schwinger functions satisfying OS axioms with a mass gap — but the Schwinger functions are for Wilson loops, not for local curvature operators. This is a theory of strings (Wilson loops), not a theory of local fields. The Clay problem asks for the latter.

**(b) Short-distance match to perturbative AF.** Jaffe–Witten requires that correlation functions "agree at short distances with the predictions of asymptotic freedom." The preprint does not check the two-point function $\langle \mathrm{Tr}\,F_{\mu\nu}(x)\,\mathrm{Tr}\,F_{\rho\sigma}(y)\rangle$ against the perturbative AF prediction at $|x-y| \to 0$. This is Conjecture L.2, conditional on L.1.

**Status: GENUINE GAP.** Without this check, the constructed QFT could in principle be a different theory that happens to have a mass gap but does not reproduce Yang–Mills at short distances.

**(c) Stress tensor.** Jaffe–Witten explicitly requires the existence of a stress-energy tensor $T_{\mu\nu}(x)$. This is Conjecture L.3, conditional on L.1. The construction of a gauge-invariant, conserved stress tensor as an operator-valued distribution requires renormalized composite operators (the gauge-invariant improved stress tensor involves products of fields at the same point).

**Status: GENUINE GAP.**

**(d) Operator product expansion.** Jaffe–Witten requires an OPE with "prescribed local singularities predicted by asymptotic freedom." This is Conjecture L.4, conditional on L.1 and L.2. An OPE is a strong structural property; the mere existence of Schwinger functions with short-distance bounds is not equivalent.

**Status: GENUINE GAP.**

**(e) The "how far from the proof" assessment.** The paper's Appendix L provides an honest accounting:
- Conjecture L.1 (renormalized composite operators) requires a multiplicative renormalization program for lattice operators — this is a substantial open problem comparable to Glimm–Jaffe's operator construction for $\phi^4_3$.
- Conjectures L.2–L.4 are conditional on L.1.
- The paper notes two pieces of unconditional progress: $H_{\mathrm{OS}} \geq 0$ from OS reconstruction, and coincident-point bounds on $S_n$ via Källén–Lehmann + linked cluster.

Estimated difficulty for closing L.1–L.4: **1 paper** (substantial new work required, comparable to known unsolved problems in 4D constructive QFT). The paper correctly states these as a "separate research programme."

**Impact on Clay eligibility:** A failure on any of (a)–(d) is directly a failure of the Clay statement. The current proof establishes a mass gap for a well-defined object (Schwinger functions of Wilson loops satisfying OS axioms), but that object lacks the local field structure Jaffe–Witten demands. This is the single largest gap between the current proof and full Clay compliance.

However, this gap is **honestly acknowledged** by the authors and clearly separated from the mass gap proof itself. The mass gap proof chain (Steps 1–14 in PROOF-CHAIN) does not claim to address L.1–L.4.
