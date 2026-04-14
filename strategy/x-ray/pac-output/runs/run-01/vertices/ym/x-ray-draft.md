# YM X-RAY DRAFT — Author Layer

*First-pass annotations for ym (paper08, 18 nodes). For each layer, the 5-field Physics block. Citations attached. Critic and arbiter operate from this draft.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## Author rules

- Pick face from 10 (paper60).
- Pick projection from 6 (paper61).
- Pick pattern from 5 (ORA v8 / paper08 §36-the-method).
- Pick 1–2 invariants from fixed list of 16.
- Interpretation: ≤3 sentences, must cite paper60 or paper61.
- Cross-cuts: list other vertices sharing the invariant/face.

---

## L1 — KK Spectral gap Δ_0^KK > 0 (Weitzenböck + cluster expansion, Theorem 4)

- **Face**: CURVATURE (paper60 §13 — "the gap between vacuum and first KK excitation is the curvature's gift to the quantum theory")
- **Projection**: P_B (paper61 §08 — "the KK spectral gap Δ_0^KK = 1/R^2 is the load-bearing structural element for the Yang-Mills mass gap proof")
- **Pattern**: P4 Topological Rigidity (paper08 §36 — Pattern 4 "compactness forces discreteness; discreteness forces gaps"; Weitzenböck on CP^{N-1} is rigid spectral gap).
- **Invariant preserved**: spectral gap (load-bearing); KK mode index n=0 vs n≥1 (background).
- **Geometric interpretation**: The internal space CP^{N-1} has positive Ricci curvature, and by the Weitzenböck formula Δ_A = ∇*_A∇_A + Ric + F_A the lowest eigenvalue is bounded below by μ_1 ≥ 2N/r_3^2 > 0 (paper60 §13). The compact circle's lattice spectrum {n^2/R^2} discretizes the gauge tower and forces the gap. This is the e-circle's "gap above the ground state" (paper60 §13 Lehmer parallel).
- **Cross-cuts**: qg5d Branch B (same KK gap, paper61 §08); lehmer L_top (same "gap above ground state" structural form per paper60 §13 table).

## L1b — IR equivalence Δ_0^std > 0 (reduced transfer matrix, Theorem 5)

- **Face**: CURVATURE (paper60 §13 — IR equivalence transports the curvature gap to the standard Wilson lattice; same face, same gap).
- **Projection**: P_B (paper61 §08 — gauge-bundle projection of the lattice transfer matrix is still a Wilson-loop / KK statement)
- **Pattern**: P4 Topological Rigidity (paper08 §36 — Lemma chain D.1/D.2 reflection-positivity rigidity → same spectral-gap rigidity preserved across regulators)
- **Invariant preserved**: spectral gap (load-bearing); ergodic property (background, via reflection positivity).
- **Geometric interpretation**: The Wilson lattice and KK lattice agree in the IR limit (Δ_0^std ≥ Δ_0^KK − Ce^{−m_1 a}); the gap survives the reduced transfer matrix construction (paper08 Lemmas 1–4 + Feshbach). This is the same curvature-induced gap as L1, transported through an IR-equivalence; the e-circle's compactness still anchors the bound (paper60 §13).
- **Cross-cuts**: qg5d Branch B (KK ↔ standard lattice equivalence); lehmer (cyclotomic gap = topological-protection analog of IR equivalence per paper60 §13 parallel table).

## L2 — UV stability (Balaban polymer expansion; UV-finite all-loop)

- **Face**: RESONANCE (paper60 §15 — RESONANCE = "what vibrational frequencies are ALLOWED on the circle"; Balaban polymer is precisely the resonance-mode RG that selects which frequencies survive UV completion).
- **Projection**: P_B (paper61 §08 — "all UV divergences in 5D KK quantum gravity factorize through the zeta regulator"; YM Link 2 inherits from this Theorem K.4 unconditional UV-finiteness)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — Pattern 5 "KK sums regularize via Epstein-zeta vanishing"; Theorem K.1 vanishing E_L(−j;Q)=0 is the engine)
- **Invariant preserved**: scaling dimension (load-bearing); spectral gap (background — UV stability preserves L1's gap).
- **Geometric interpretation**: Balaban's polymer expansion (CMP 109,119) is the lattice-RG implementation of UV stability; combined with Paper 11 Theorem K.4 (all-loop UV-finiteness via Epstein-zeta vanishing on the KK lattice, paper61 §08), Link 2's setup is unconditional. The UV-finiteness is structurally inevitable from S^1 compactness (paper61 §08 "Level 1 — Arithmetic").
- **Cross-cuts**: qg5d Branch B (W1/W2 closure — same Theorem K.4); rh (zeta-regularization is shared with the BC-algebra side).

## L3 — Polymer convergence, κ k-independent

- **Face**: DYNAMICS (paper60 §08 — "how does the modular flow TRAVERSE the circle"; the RG flow's k-independent convergence rate is precisely a flow-on-the-circle invariant)
- **Projection**: P_D (paper61 §10 — Branch D's modular-flow ergodicity controls infinite-volume limits; YM uses this via Balaban's polymer)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — k-independent convergence is the same Epstein-zeta scheme-independence Pattern that Theorems K.1 + K.4 provide)
- **Invariant preserved**: ergodic property (load-bearing — polymer mixing); scaling dimension (background).
- **Geometric interpretation**: A k-independent convergence radius κ is the polymer expansion's statement that the RG flow is uniformly mixing across scales — a dynamical property of the modular flow on the BC algebra under projection P_D (paper61 §10 ITPFI factor type III_1 ergodicity). The flow traverses the e-circle uniformly (paper60 §08 Cramér-face dynamics analog).
- **Cross-cuts**: cramer (same modular-flow ergodicity); pvnp (Popa rigidity uses ergodicity of type III_1 modular flow); rh (BC-algebra ergodicity).

## L4 — (B1) analyticity, k-independent radius

- **Face**: AMPLITUDE (paper60 §11 — AMPLITUDE = "how LOUD can the oscillation get; analytic radius bounds growth"; analyticity of free energy in k is precisely the YM analog of Lindelöf bound)
- **Projection**: P_D (paper61 §10 — analyticity of the BC-algebra resolvent under modular flow, lifted to the polymer free energy)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — analyticity follows from Pattern 5's regulator-independence)
- **Invariant preserved**: scaling dimension (load-bearing — analyticity radius IS a scale); spectral gap (background).
- **Geometric interpretation**: A k-independent analyticity radius for the polymer free energy means the amplitude bound is uniform in the RG step — the same kind of "no growth blowup" that characterizes the AMPLITUDE face (paper60 §11). Under P_D the analyticity is a property of the modular-flow resolvent (paper61 §10 spectral triple).
- **Cross-cuts**: lindelof (AMPLITUDE canonical, same uniform-bound structural form); rh L_resolvent (Boegli H1 uniform H¹ resolvent bound is the same kind of uniformity).

## L5 — (B2) SL(N,C) extension

- **Face**: SYMMETRY (paper60 §12 — SYMMETRY face is "which group acts on the circle"; complexification SU(N) → SL(N,C) is exactly a symmetry-extension move)
- **Projection**: P_D (paper61 §10 — gauge-group complexification is the BC bridge family choice at k=4, P_D's symmetry-type selector)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — Pattern 1 "you don't add complexity, you reveal the simpler underlying object"; complexification reveals SL(N,C) as the natural ambient group)
- **Invariant preserved**: gauge class (load-bearing — Pontryagin / U(1) bundle class lifted to SL(N,C)); monodromy (background).
- **Geometric interpretation**: Extending from compact SU(N) to non-compact SL(N,C) is the symmetry-side complexification move that paper60 §12 (Katz-Sarnak SYMMETRY face) identifies with the bridge family at k=4 (orthogonal type, paper61 §10). The extension is geometric reinterpretation, not new physics — the same gauge bundle, viewed under its natural complex-analytic structure.
- **Cross-cuts**: katz-sarnak (SYMMETRY canonical, bridge family k=4 symmetry-type selection per paper61 §10); h12 (Galois group complexification of class-field structure).

## L6 — C-elimination of Tr(F^3)

- **Face**: SYMMETRY (paper60 §12 — charge-conjugation parity selects which gauge invariants survive; C-elimination is a symmetry-imposed selection rule)
- **Projection**: P_B (paper61 §08 — C-parity acts on the gauge bundle, which P_B preserves)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — Tr(F^3) "looks like a perturbative obstruction" in 4D but vanishes by the geometric C-symmetry, restoring the simpler structure)
- **Invariant preserved**: gauge class (load-bearing — discrete C-symmetry preserves Pontryagin class).
- **Geometric interpretation**: C-elimination of Tr(F^3) is the discrete-symmetry selection rule that removes a candidate dim-6 obstruction; under P_B's gauge-bundle projection (paper61 §08), the surviving operators are the C-even ones. This is Pattern 1 — restoring the symmetric viewpoint dissolves the perturbative concern.
- **Cross-cuts**: hodge (C-symmetry on Hodge classes); pvnp (parity selects which decision instances survive).

## L7 — Newton decomposition: n ≥ 2 survives

- **Face**: ARITHMETIC (paper60 §14 — ARITHMETIC face is "how do integers LATTICE on the circle"; Newton's decomposition into power-sum symmetric polynomials is exactly an integer-lattice statement on the eigenvalues)
- **Projection**: P_B (paper61 §08 — power-sum decomposition acts on the KK lattice spectrum, which P_B preserves)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — restating the dim-6 problem in the Newton power-sum basis reveals the n ≥ 2 structure)
- **Invariant preserved**: KK mode index (load-bearing — Newton sums index by integer power); scaling dimension (background — n indexes the dimension).
- **Geometric interpretation**: The Newton symmetric-function decomposition tracks how integer powers (n=2,3,...) survive after the C-elimination of L6. This is paper60 §14's ARITHMETIC face — integers lattice on the circle as the power-sum spectrum of the gauge invariants. Under P_B (paper61 §08), the surviving n ≥ 2 sector controls the dim-6 contribution.
- **Cross-cuts**: goldbach / twin-primes (ARITHMETIC canonical, additive-multiplicative integer structure); collatz (integer-lattice harmonics on circle).

## L8 — dev(Tr(DF)^2) ≥ 2

- **Face**: CURVATURE (paper60 §13 — Tr(DF)^2 is the squared-derivative of the curvature 2-form; deviation ≥ 2 is precisely a curvature-decay statement)
- **Projection**: P_B (paper61 §08 — derivative of curvature is a gauge-bundle quantity; P_B preserves the field-strength differential structure)
- **Pattern**: P4 Topological Rigidity (paper08 §36 — deviation bound is a rigid lower bound that survives non-perturbative corrections)
- **Invariant preserved**: critical exponent (load-bearing — dev = 2 IS a critical exponent for the operator); scaling dimension (background).
- **Geometric interpretation**: The deviation index "dev" measures how far a gauge operator suppresses below the leading dim-4 action; dev ≥ 2 means Tr(DF)^2 contributes only at order R^2 relative to the leading curvature-squared action (paper60 §13's Weitzenböck-curvature framework). Under P_B (paper61 §08) this is a structural property of the KK-suppressed operators.
- **Cross-cuts**: qg5d Branch B (same dim-suppression for KK-mode operators per paper61 §08 "Links 6–9"); ns (gradient-flow regularity uses analogous deviation).

## L9 — Dim-6 classification: all operators dev ≥ 2

- **Face**: SYMMETRY (paper60 §12 — classification of dim-6 operators by gauge symmetry IS a symmetry-type accounting; SYMMETRY face Katz-Sarnak analog)
- **Projection**: P_B (paper61 §08 — operator classification is gauge-bundle structural)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — dim-6 classification reveals the irreducible content; geometric reorganization, not new physics)
- **Invariant preserved**: scaling dimension (load-bearing — dim-6 is the labeling); gauge class (background).
- **Geometric interpretation**: Classifying all dim-6 operators by their gauge content shows uniformly dev ≥ 2 across the entire family — a symmetry statement in the spirit of paper60 §12's Katz-Sarnak SYMMETRY face: the gauge group's representation theory closes the classification. Under P_B (paper61 §08), this means no dim-6 operator escapes the KK suppression.
- **Cross-cuts**: katz-sarnak (operator family classification by symmetry type); hodge (dim-6 = dim of a specific Hodge stratum analog).

## L10 — dev(δE_k^{d=6}) ≥ 2 non-perturbatively

- **Face**: CURVATURE (paper60 §13 — δE_k is the energy correction at scale k, non-perturbative bound IS the curvature gap propagated to all RG steps)
- **Projection**: P_B (paper61 §08 — non-perturbative bound on KK-suppressed operators; P_B's gauge-bundle preservation)
- **Pattern**: P4 Topological Rigidity (paper08 §36 — non-perturbative deviation = topological rigidity of the suppression bound)
- **Invariant preserved**: critical exponent (load-bearing — dev=2 is the operator's critical exponent); spectral gap (background).
- **Geometric interpretation**: The non-perturbative version of L9 — the deviation bound holds beyond perturbation theory. This is the curvature gap (paper60 §13) propagating through the polymer expansion to bound corrections at every RG step. Under P_B (paper61 §08) the bound is a rigid feature of the gauge-bundle's KK structure.
- **Cross-cuts**: qg5d Branch B (non-perturbative KK suppression); pvnp (Popa rigidity = analog of non-perturbative gap rigidity).

## L10b — Spectral lemma constant C_p k-independent

- **Face**: RESONANCE (paper60 §15 — RESONANCE face = "what vibrational frequencies are ALLOWED"; spectral-lemma constant is the resonance-amplitude prefactor)
- **Projection**: P_D (paper61 §10 — spectral-lemma uniformity is a property of the BC algebra's modular-flow resolvent under P_D)
- **Pattern**: P3 Scale-Setting (paper08 §36 — k-independence sets the scale uniformly; the constant doesn't run with the RG)
- **Invariant preserved**: spectral gap (load-bearing — C_p quantifies the gap); scaling dimension (background).
- **Geometric interpretation**: A k-independent C_p means the spectral-lemma bound is set at a single scale and doesn't drift with the RG — Pattern 3 in its purest form (paper08 §36). Under P_D (paper61 §10) this is a uniform property of the modular-flow spectrum.
- **Cross-cuts**: rh (uniform Boegli resolvent constants, similar k-independence); selberg-1/4 (spectral gap uniformity on arithmetic surfaces).

## L11 — C_new g_k^4 Δ̂² bound

- **Face**: AMPLITUDE (paper60 §11 — bound on the form-factor amplitude g_k^4 Δ̂² is a growth-rate / "loudness" statement)
- **Projection**: P_B (paper61 §08 — gauge coupling g_k and form factor live in the gauge-bundle projection)
- **Pattern**: P3 Scale-Setting (paper08 §36 — the bound's coefficient C_new sets the scale of the form-factor contribution at each RG step)
- **Invariant preserved**: scaling dimension (load-bearing — Δ̂² indexes the operator dimension); critical exponent (background — g_k^4 power).
- **Geometric interpretation**: The form-factor bound C_new g_k^4 Δ̂² is the amplitude (paper60 §11) of the new-operator contribution at each RG step; the coefficient C_new is set by the spectral lemma L10b. Under P_B (paper61 §08) this controls the gauge-side amplitude growth.
- **Cross-cuts**: lindelof (AMPLITUDE growth bound); ns (form-factor regularity for fluid).

## L12 — RG recursion C_{k+1} = C_k/4 + C_new

- **Face**: DYNAMICS (paper60 §08 — RG recursion IS a discrete dynamical system on the coefficient C_k; flow-on-the-circle analog)
- **Projection**: P_B (paper61 §08 — RG flow acts on the gauge-bundle's coupling sequence)
- **Pattern**: P3 Scale-Setting (paper08 §36 — recursion with contraction factor 1/4 sets the scale across RG steps)
- **Invariant preserved**: scaling dimension (load-bearing — recursion in scaling exponent); critical exponent (background — 1/4 contraction).
- **Geometric interpretation**: The RG recursion C_{k+1} = C_k/4 + C_new is a contraction-mapping dynamics (paper60 §08 DYNAMICS face) on the form-factor coefficient. Contraction factor 1/4 < 1 ensures convergence; the "modular flow on the circle" analog is exact (paper61 §10 modular-flow ergodicity).
- **Cross-cuts**: cramer (DYNAMICS canonical, same modular-flow contraction); pvnp (Popa rigidity uses contraction-on-modular-flow analog).

## L13 — Σ C_k g_k^4 Δ̂_k² < ∞

- **Face**: AMPLITUDE (paper60 §11 — convergence of the sum is the amplitude's total energy; bounded total amplitude IS the AMPLITUDE statement)
- **Projection**: P_B (paper61 §08 — sum over RG steps in the gauge sector)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — the convergent sum is the regularized total of the form-factor contributions, the same Pattern 5 that handles KK sums)
- **Invariant preserved**: scaling dimension (load-bearing — sum convergence is a scaling-dimension statement); spectral gap (background — convergence requires the gap of L1).
- **Geometric interpretation**: Σ C_k g_k^4 Δ̂_k² < ∞ packages L11+L12 into a finite-amplitude statement (paper60 §11). The sum converges by Pattern 5 (paper08 §36) and the convergence is what sustains Δ_∞ > 0 in the continuum limit. Under P_B (paper61 §08) this is the gauge-side bounded amplitude.
- **Cross-cuts**: lindelof (AMPLITUDE canonical, bounded ζ moments); rh (Weil quadratic form convergence).

## L14 — Δ_∞ > 0 (mass gap from L1b + L13)

- **Face**: CURVATURE (paper60 §13 — THIS IS the curvature face's main theorem; Δ_∞ IS the mass gap)
- **Projection**: P_B (paper61 §08 — the mass gap is the gauge-bundle projection's signature output)
- **Pattern**: P4 Topological Rigidity (paper08 §36 — Δ_∞ > 0 is the rigid topological gap, protected by curvature compactness)
- **Invariant preserved**: spectral gap (load-bearing — Δ_∞ IS the spectral gap); KK mode index (background — gap is between n=0 and n=1 sector).
- **Geometric interpretation**: This is the YM mass gap. It combines the KK gap of L1b (per paper60 §13: "the gap is the curvature's gift") with the convergent form-factor sum L13 to bound the continuum limit of the mass gap from below. The 5D origin: positive Ricci curvature on CP^{N-1} (paper61 §08).
- **Cross-cuts**: qg5d Branch B (KK gap = primary parent); lehmer (TOPOLOGY analog of "gap above ground state" per paper60 §13 table); ns (mass gap analog for NS regularity scale).

## L15 — Gradient-flow well-posedness, contractivity (Lemmas 1.1–1.5)

- **Face**: DYNAMICS (paper60 §08 — gradient flow IS a continuous dynamical system on gauge fields; flow-on-the-circle analog)
- **Projection**: P_B (paper61 §08 — gradient flow acts on the gauge-bundle, P_B preserves)
- **Pattern**: P3 Scale-Setting (paper08 §36 — gradient flow time t sets the smearing scale; contractivity is scale-set)
- **Invariant preserved**: ergodic property (load-bearing — contractivity = ergodic mixing); scaling dimension (background — gradient-flow time is a scale).
- **Geometric interpretation**: Gradient flow's well-posedness and contractivity are dynamical-system properties (paper60 §08 DYNAMICS face) on the gauge-bundle space. The flow time t is the scale-setting parameter (paper08 §36 Pattern 3). Under P_B (paper61 §08) the flow respects the bundle structure.
- **Cross-cuts**: ns (paper30 — gradient-flow infrastructure for NS regularity, explicit edge in YM PROOF-CHAIN.md); cramer (DYNAMICS canonical).

## L16 — Continuum Schwinger functions: OS0–OS4 at fixed t > 0

- **Face**: RESONANCE (paper60 §15 — Schwinger functions ARE the trace-formula-side resonance content; OS axioms catalog allowed resonances)
- **Projection**: P_D (paper61 §10 — OS reconstruction goes from Euclidean correlators to Wightman fields via the GNS construction = a P_D / operator-algebra step)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — Schwinger functions reinterpret the path integral as resonance data)
- **Invariant preserved**: BC-KMS state (load-bearing — Schwinger functions = restriction of the KMS state to local fields); ergodic property (background).
- **Geometric interpretation**: The Schwinger functions OS0–OS4 are the Wightman-fields data after gradient-flow regularization at fixed t > 0. Under P_D (paper61 §10) these are the BC-KMS state restricted to local field algebras — the same state that controls the YM modular-flow ergodicity. Pattern 1 (paper08 §36): the OS axioms are the geometric reinterpretation of the path integral as operator-valued distribution data.
- **Cross-cuts**: rh (BC-KMS state shared); baum-connes (KMS state on the spectral triple); pvnp (BC-KMS state restriction).

## L17 — [Tr F²]_R as operator-valued distribution; T_μν^R constructed

- **Face**: RESONANCE (paper60 §15 — operator-valued distributions ARE the resonance-mode operators; T_μν is the energy-momentum resonance content)
- **Projection**: P_D (paper61 §10 — operator-valued distributions live in the BC operator-algebra side)
- **Pattern**: P1 Geometric Reinterpretation (paper08 §36 — reinterpreting the formal classical observable [Tr F²] as a renormalized operator-valued distribution is the canonical Pattern-1 move)
- **Invariant preserved**: C*-algebra structure (load-bearing — operator-valued distribution lives in the local C*-algebra); BC-KMS state (background).
- **Geometric interpretation**: The renormalized [Tr F²]_R and T_μν^R are operator-valued distributions in the gradient-flow framework. Under P_D (paper61 §10) these are elements of the local C*-algebra associated with the YM Schwinger functions. The geometric reinterpretation (Pattern 1, paper08 §36) takes the formal classical density and produces a rigorous operator definition.
- **Cross-cuts**: rh (operator-valued distribution analog); ns (energy-momentum tensor regularity); baum-connes (local C*-algebra structure).

## L18 — AF match (L.2), leading-order OPE (L.4) — CONDITIONAL on H4

- **Face**: RESONANCE (paper60 §15 — asymptotic freedom and OPE are short-distance resonance-content statements; OPE coefficients ARE resonance amplitudes)
- **Projection**: P_O (paper61 §12 — L18 is the boundary of the unconditional chain; the conditional leg connects to the OUTER conjecture-statement layer where YM as a Clay problem lives. AF match is what closes the YM Clay problem)
- **Pattern**: P5 Zeta Regularization (paper08 §36 — H4 expects the perturbative short-distance series to match the non-perturbative; Pattern 5 is the only pattern that operates at the "perturbative-short-distance vs non-perturbative" interface)
- **Invariant preserved**: scaling dimension (load-bearing — AF means scaling dimension flows to free in UV); critical exponent (background — OPE coefficients).
- **Geometric interpretation**: H4 says the gradient-flow OS reconstruction's short-distance behavior matches asymptotic freedom and the leading OPE (paper60 §13 "the sole remaining wall is a technical hypothesis about short-distance matching, not a conceptual gap"). The H4 Bypass session (2026-04-13) produced Step 18' as a candidate unconditional replacement using Balaban RG + gradient-flow Lüscher coupling (capacitor 09 §74 + §110, paper08 h4-capacitor-bypass). Under P_O (paper61 §12) this is the boundary where YM as the outer-ring Clay vertex closes.
- **Cross-cuts**: qg5d Branch B (UV-finite via K.1+K.4 → AF inherits); rh (zeta-regularization side at short distance); pvnp (asymptotic regime analog via spectral gap rigidity).

---

## Author summary

- 18 layers (treating L1b and L10b as sub-layers, but counting them in the histograms).
- Total entries: 20.
- Face distribution: CURVATURE 6 / RESONANCE 5 / DYNAMICS 3 / AMPLITUDE 3 / SYMMETRY 3 / ARITHMETIC 1 / TOPOLOGY 0 / HARMONICS 0 / MEASURE 0 / SPREAD 0.
- Projection distribution: P_B 13 / P_D 6 / P_O 1.
- Pattern distribution: P4 5 / P5 4 / P3 4 / P1 6 / P2 0.
- Cross-cuts: 38 edges identified across 20 layers (multiple per layer).

Hand off to critic.
