# 168 — EW Sector as Moduli Space (not Spectrum)

**Status:** HYPOTHESIS (structurally supported, awaiting numerical test in Cycle 6)
**Parent:** Cycle 4 straggler isolation (9 PDG-precision observables)
**Sibling:** 156 (KK–Frobenius stragglers), 160 (conductor lift)

## 1. The partition

Cycle 4 left exactly 9 observables uncloseable by any multiplicative envelope on the Bost–Connes spectral coefficients γ_n:

| # | Observable | Sector role |
|---|---|---|
| 1 | m_τ | charged lepton Yukawa |
| 2 | m_μ | charged lepton Yukawa |
| 3 | m_Z | EW gauge boson |
| 4 | m_H | Higgs pole |
| 5 | m_W/m_Z | ρ-parameter / custodial SU(2) |
| 6 | v | Higgs VEV |
| 7 | 1/α | fine-structure / U(1)_Y × SU(2)_L mixing |
| 8 | m_τ/m_μ | Yukawa ratio |
| 9 | sin θ_12 (CKM) | quark-sector mixing from Higgs Yukawas |

Verification against research/23 formulas: every straggler is either (a) a Higgs-sector mass, (b) a gauge boson mass (= gv/2 type), (c) a Yukawa ratio (= y_f v/√2), or (d) a CKM angle (= overlap of Yukawa eigenbases). **All 9 involve the Higgs VEV v or gauge couplings directly.** No neutrino mass, no QCD scale, no cosmological constant, no dark-matter mass appears.

The BC spectral sector — which *does* close under γ_n envelopes (Cycles 1–3) — contains: Λ_QCD, m_p, m_n, m_π, Ω_Λ, H_0, m_ν sums, θ_13, sin²θ_W *at the Z-pole after running*, θ_QCD bound, dark-matter candidate mass. These are pure arithmetic: eigenvalues of a Dirac/Laplacian-type operator on the BC system.

**The partition is sharp: spectrum = everything except EWSB; moduli = EWSB.**

## 2. Structural argument: why spectrum cannot close EWSB

The Bost–Connes sector delivers *eigenvalues*. An eigenvalue is an invariant of an operator: it does not know about the background geometry, only about the operator's symbol. In Paper 11 language, γ_n are spectral data of the KK Laplacian on CP²×S²×S¹ at **fixed** metric.

The Higgs VEV v is categorically different. In any geometric Higgs mechanism (Connes–Chamseddine spectral action, KK reduction with Wilson lines, flux compactification), v is the **location of the minimum** of an effective potential on the moduli space of the internal metric. It is not an eigenvalue of a fixed operator — it is the *value of the modulus at which an operator family is evaluated*. Likewise:

- m_W, m_Z = gv/2, √(g²+g'²)v/2 — depend on v and on gauge couplings, which in KK reduction are **volume moduli** of the gauge factor (g² ∝ 1/Vol(CP²) type).
- m_H² = 2λv² where λ is the quartic, itself a **curvature modulus** of the Higgs potential (= sectional curvature of the vacuum submanifold).
- 1/α depends on the ratio of volume moduli of the U(1)_Y and SU(2)_L factors.
- Charged lepton Yukawas y_f = √2 m_f/v are **overlap integrals** of wavefunctions on CP²×S² — i.e. functions of the metric moduli.
- CKM angles are rotation angles between Yukawa eigenbases; they too are overlap integrals depending on the CP² metric.

A multiplicative envelope E_n on γ_n can shift eigenvalues but cannot move the minimum of a potential. **The moduli sector is topologically disjoint from the spectral sector:** it lives on the tangent space to metric deformations, not on the spectrum of a fixed operator. No function of {γ_n} can reach it.

This is why Cycle 4 failed — and the failure is a *theorem*, not a numerical accident.

## 3. The creative hypothesis

> **EW-Moduli Hypothesis.** The residuals of the 9 stragglers, taken as a 9-vector in log-space, form coordinates on the moduli space M = { metrics on CP²×S² compatible with Paper 11's topological data } modulo isometry. Fitting the 9 residuals simultaneously is equivalent to **solving for the physical point in M** at which our universe sits.

More precisely:

- dim M ≥ 9 (CP² has 2 Kähler moduli + 2 complex-structure; S² has 1 radius; gauge-factor volumes contribute ≥ 2; Wilson-line phases contribute ≥ 2). The dimension matches.
- The 9 observables are (conjecturally) **independent coordinate functions** on M, not redundant combinations — consistent with Cycle 4 finding that no single-parameter correction closes more than one.
- The Higgs potential V(v) = (λ/4)(v²−v₀²)² is the pullback to M of the spectral action of Paper 11 after integrating out the BC spectrum. Its minimum v₀ is where M intersects the physical slice.

Predictions:
1. The 9-dim fit should have a **unique** minimum (generic moduli space, no continuous degeneracy after Wilson-line gauge fixing).
2. The fitted metric on CP²×S² should satisfy an **Einstein-like equation** sourced by the BC spectral stress-energy (this would be the Cycle-6 consistency check).
3. Residuals *within* the EW sector should correlate via the moduli-space metric — e.g. ∂(m_H)/∂(CP²-Kähler modulus) and ∂(v)/∂(same modulus) should give a predicted ratio.
4. Observables *outside* the EW sector should be **insensitive to 1st-order moduli deformations** (justifying their closure by γ_n alone).

## 4. One-line statement

**EW sector lives in moduli space, not spectrum.** The BC spectral γ_n close the arithmetic sector; the 9 stragglers are coordinates on the Kähler–volume–Wilson-line moduli of CP²×S², and fitting them *is* fitting the metric of the internal geometry.

## 5. Verdict

**HYPOTHESIS — structurally supported.** Three converging lines of evidence:

1. **Sharp empirical partition** (Cycle 4): all 9 stragglers are EWSB observables; no EWSB observable closes under γ_n.
2. **No-go argument** (§2): eigenvalues of a fixed operator cannot encode the location of a potential minimum; the two sectors are functorially disjoint.
3. **Dimension count** (§3): dim M matches the straggler count, and the moduli are exactly the geometric DoF that an EWSB observable depends on in a KK/spectral-action construction.

Not yet proven — requires Cycle 6 to (a) write down M explicitly from Paper 11's topological data, (b) derive the 9 observables as functions on M from the spectral action, and (c) verify the fit has a unique, stable minimum matching PDG values. If all three pass, this reclassifies Cycles 1–3 as "spectral closure" and Cycle 6 as "moduli closure," and the two together constitute the full Paper-12 mass-gap-to-SM-parameters map.

## 6. Next action (Cycle 6 opener)

Enumerate moduli on CP²×S² from Paper 11 §4 (topological data), compute dim M with Wilson lines, and write the 9 observables as explicit functions of those moduli. The KK Frobenius analysis of 156 is the right scaffold — it already sees the non-spectral part; Cycle 6 should name it "moduli" and proceed.
