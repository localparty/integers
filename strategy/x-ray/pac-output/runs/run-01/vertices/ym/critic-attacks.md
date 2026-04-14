# YM CRITIC ATTACKS — One Alternative per Field per Layer

*The critic's job is attacking ASSIGNMENTS, not claims. For each of 18 main layers, generate at least one competing assignment per field (face, projection, pattern, invariant, interpretation) with a reason. Arbiter resolves.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## L1 — KK Spectral gap

- **Face attack**: Author picked CURVATURE; critic argues TOPOLOGY because the gap is the n=0 vs n=1 winding-number separation, and paper60 §13 itself acknowledges the Lehmer (TOPOLOGY) parallel as adjacent.
- **Projection attack**: Author picked P_B; critic argues P_D because the spectral gap of the Hecke semigroup is the BC-algebra signature, and paper61 §10 says Branch D is "the deepest projection — it touches almost every other face including YM via the KK gap."
- **Pattern attack**: Author picked P4; critic argues P3 because the KK radius R IS the scale-setting parameter (Δ_0^KK = 1/R^2), so this is canonical Scale-Setting before it is Topological Rigidity.
- **Invariant attack**: Author picked spectral gap; critic argues KK mode index is the load-bearing one because the gap is DEFINED as the index-difference between n=0 and n=1.
- **Interpretation attack**: Author cited paper60 §13 + paper61 §08; critic notes the citation to paper60 §13's adjacency table makes Lehmer-cross-cut argument stronger than CURVATURE-only, hand-wave risk.

## L1b — IR Equivalence Δ_0^std > 0

- **Face attack**: Author picked CURVATURE; critic argues SYMMETRY because IR equivalence is a regulator-symmetry statement (the Wilson regulator and KK regulator agree because both share the gauge symmetry).
- **Projection attack**: Author picked P_B; critic argues P_D because the equivalence is a transfer-matrix statement and transfer matrices live in the operator algebra (P_D side).
- **Pattern attack**: Author picked P4; critic argues P1 because transfer-matrix equivalence is a Geometric Reinterpretation (lattice ↔ continuum reading of the same operator).
- **Invariant attack**: Author picked spectral gap; critic argues C*-algebra structure (transfer matrix is bounded self-adjoint trace-class — the load-bearing fact for Lemmas 1–3).
- **Interpretation attack**: Author's interpretation cites paper60 §13 — sound, but should also explicitly cite paper08 Lemmas 1–4 (the IR equivalence proof).

## L2 — UV stability (Balaban polymer)

- **Face attack**: Author picked RESONANCE; critic argues CURVATURE because Balaban polymer IS the RG of the curvature 2-form, and the UV-finiteness inherits from the curvature-side Theorem K.1.
- **Projection attack**: Author picked P_B; critic argues P_D because Balaban's polymer expansion is operator-algebraic in nature (uses cluster expansion and ITPFI factor properties).
- **Pattern attack**: Author picked P5; critic argues P4 because the Balaban convergence is a topological-rigidity statement (the cluster expansion's convergence radius is rigid against all loop orders).
- **Invariant attack**: Author picked scaling dimension; critic argues spectral gap (the UV-finiteness preserves the L1 gap, not just the dimension).
- **Interpretation attack**: Critic's strongest objection: "you cited paper61 §08's K.4 but didn't cite paper08's actual Balaban implementation." Author should add paper08 §43 (balaban-framework).

## L3 — Polymer convergence κ k-independent

- **Face attack**: Author picked DYNAMICS; critic argues RESONANCE because k-independent κ is a uniformity-of-modes statement (resonance-mode invariance across RG steps).
- **Projection attack**: Author picked P_D; critic argues P_B because the polymer convergence acts on the lattice gauge field (gauge bundle), not directly on the operator algebra.
- **Pattern attack**: Author picked P5; critic argues P3 because k-independence is precisely Scale-Setting (the convergence rate doesn't run with the RG step).
- **Invariant attack**: Author picked ergodic property; critic argues scaling dimension (k-independence IS a scaling-invariance statement).
- **Interpretation attack**: Sound, but the modular-flow analogy is somewhat speculative — should cite paper61 §10 ITPFI ergodicity more carefully.

## L4 — (B1) analyticity, k-independent radius

- **Face attack**: Author picked AMPLITUDE; critic argues RESONANCE because analyticity of free energy is precisely a "what frequencies are allowed" statement (poles/zeros of the resolvent).
- **Projection attack**: Author picked P_D; critic argues P_B because (B1) is part of the Balaban framework which is gauge-side.
- **Pattern attack**: Author picked P5; critic argues P3 because the k-independence is Scale-Setting.
- **Invariant attack**: Author picked scaling dimension; critic argues spectral gap (analyticity radius is set by the gap).
- **Interpretation attack**: Cross-cut to lindelof is suggestive but speculative — needs the actual face-table reference from paper60 §11 to back the AMPLITUDE claim more solidly.

## L5 — (B2) SL(N,C) extension

- **Face attack**: Author picked SYMMETRY; critic argues TOPOLOGY because SL(N,C) extension is a topological deformation of the gauge bundle (Pontryagin class lifts).
- **Projection attack**: Author picked P_D; critic argues P_B because SL(N,C) is the natural complexification at the gauge-bundle level (P_B's domain).
- **Pattern attack**: Author picked P1; critic argues P2 (Holonomy Correspondence) because SL(N,C) is precisely the extension that makes Wilson loops well-defined as holonomies.
- **Invariant attack**: Author picked gauge class; critic argues monodromy (SL(N,C) controls the monodromy representation).
- **Interpretation attack**: The bridge-family k=4 link is interesting but should cite paper61 §10's specific bridge-family derivation more explicitly.

## L6 — C-elimination of Tr(F^3)

- **Face attack**: Author picked SYMMETRY; critic argues CURVATURE because Tr(F^3) IS a curvature invariant (Pontryagin density's analog), so this is curvature classification.
- **Projection attack**: Author picked P_B; critic argues P_A (Quantum) because charge conjugation C is a discrete quantum symmetry, P_A's domain.
- **Pattern attack**: Author picked P1; critic argues P4 because the C-elimination is rigid (no perturbation breaks it).
- **Invariant attack**: Author picked gauge class; critic argues critical exponent (C-elimination changes the dimension counting).
- **Interpretation attack**: The "discrete-symmetry selection rule" framing is right but should cite paper60 more explicitly than the §12 SYMMETRY face citation.

## L7 — Newton decomposition: n ≥ 2 survives

- **Face attack**: Author picked ARITHMETIC; critic argues HARMONICS because Newton's symmetric functions ARE harmonic decomposition of the gauge eigenvalue spectrum.
- **Projection attack**: Author picked P_B; critic argues P_D because Newton sums act on operator spectra (P_D's algebra side).
- **Pattern attack**: Author picked P1; critic argues P2 because Newton sums = trace of holonomy powers (Wilson loops winding).
- **Invariant attack**: Author picked KK mode index; critic argues holonomy (Newton sum = Wilson loop wind-count).
- **Interpretation attack**: The integer-lattice framing is good; should also reference paper60 §09 (Collatz HARMONICS) for the harmonic alternative.

## L8 — dev(Tr(DF)^2) ≥ 2

- **Face attack**: Author picked CURVATURE; critic argues AMPLITUDE because dev=2 is a growth-rate bound (the operator's amplitude scales with R^2).
- **Projection attack**: Author picked P_B; critic argues P_D (the deviation index is operator-algebraic in spirit, used in the BC framework's classification).
- **Pattern attack**: Author picked P4; critic argues P3 because dev=2 is exactly Scale-Setting (R^2 is the scale).
- **Invariant attack**: Author picked critical exponent; critic argues scaling dimension (dev=2 IS the scaling dimension excess).
- **Interpretation attack**: The Weitzenböck citation is solid; cross-cut to NS could be tighter.

## L9 — Dim-6 classification

- **Face attack**: Author picked SYMMETRY; critic argues CURVATURE because dim-6 operators ARE higher-curvature corrections.
- **Projection attack**: Author picked P_B; critic argues P_D because operator classification is canonical operator-algebra (P_D side).
- **Pattern attack**: Author picked P1; critic argues P4 because the classification's closure is a rigid (topological) statement.
- **Invariant attack**: Author picked scaling dimension; critic argues critical exponent.
- **Interpretation attack**: SYMMETRY framing relies on Katz-Sarnak analogy; should cite paper60 §12 more directly.

## L10 — dev(δE_k^{d=6}) ≥ 2 non-perturbatively

- **Face attack**: Author picked CURVATURE; critic argues RESONANCE because non-perturbative δE_k is precisely the resonance-energy (mode amplitudes) at scale k.
- **Projection attack**: Author picked P_B; critic argues P_D because non-perturbative bounds invoke the operator-algebra (Balaban polymer's ergodic ITPFI structure).
- **Pattern attack**: Author picked P4; critic argues P5 (the non-perturbative bound is regularization-invariant, Pattern 5).
- **Invariant attack**: Author picked critical exponent; critic argues spectral gap (the non-perturbative bound is what protects the gap).
- **Interpretation attack**: Sound; the propagation-through-RG framing is correct.

## L10b — Spectral lemma constant C_p k-independent

- **Face attack**: Author picked RESONANCE; critic argues AMPLITUDE because C_p is precisely an amplitude prefactor.
- **Projection attack**: Author picked P_D; critic argues P_B (spectral lemma in the gauge-bundle context).
- **Pattern attack**: Author picked P3; critic argues P5 (k-independence is the regulator-independence of zeta-reg).
- **Invariant attack**: Author picked spectral gap; critic argues scaling dimension.
- **Interpretation attack**: Solid; Pattern 3 framing is the right call.

## L11 — C_new g_k^4 Δ̂² bound

- **Face attack**: Author picked AMPLITUDE; critic argues CURVATURE because the form factor is a curvature-derived quantity at each RG step.
- **Projection attack**: Author picked P_B; critic argues P_D (form factors live in the operator algebra of fields).
- **Pattern attack**: Author picked P3; critic argues P4 (the bound's rigidity).
- **Invariant attack**: Author picked scaling dimension; critic argues critical exponent (g_k^4 power).
- **Interpretation attack**: Cross-cut to NS via "form-factor regularity for fluid" is speculative — needs actual NS reference.

## L12 — RG recursion C_{k+1} = C_k/4 + C_new

- **Face attack**: Author picked DYNAMICS; critic argues CURVATURE because the recursion preserves the curvature-induced gap structure.
- **Projection attack**: Author picked P_B; critic argues P_D (recursion is operator-algebraic dynamics).
- **Pattern attack**: Author picked P3; critic argues P4 (fixed-point of the recursion is rigid).
- **Invariant attack**: Author picked scaling dimension; critic argues ergodic property (contraction = mixing).
- **Interpretation attack**: DYNAMICS face is right; the contraction-mapping framing is on point.

## L13 — Σ C_k g_k^4 Δ̂_k² < ∞

- **Face attack**: Author picked AMPLITUDE; critic argues RESONANCE (the convergent sum is a sum over resonance modes).
- **Projection attack**: Author picked P_B; critic argues P_D (the sum is over operator contributions across RG steps).
- **Pattern attack**: Author picked P5; critic argues P4 (the convergence is a topological-rigidity statement).
- **Invariant attack**: Author picked scaling dimension; critic argues spectral gap (sum convergence is what sustains the gap).
- **Interpretation attack**: AMPLITUDE framing is good; cross-cut to Lindelöf could be tighter.

## L14 — Δ_∞ > 0

- **Face attack**: Author picked CURVATURE; critic argues TOPOLOGY (the gap is topological in the Lehmer sense per paper60 §13's adjacency table).
- **Projection attack**: Author picked P_B; critic argues P_D (the BC-algebra spectrum carries the gap as Branch D pin).
- **Pattern attack**: Author picked P4; critic argues P3 (the gap = 1/R^2 is a scale).
- **Invariant attack**: Author picked spectral gap; critic argues KK mode index.
- **Interpretation attack**: Solid; this is the canonical CURVATURE statement.

## L15 — Gradient flow well-posedness, contractivity

- **Face attack**: Author picked DYNAMICS; critic argues HARMONICS (gradient flow = heat equation = harmonic dissipation).
- **Projection attack**: Author picked P_B; critic argues P_D (gradient flow induces a modular-flow analog on the field-operator algebra).
- **Pattern attack**: Author picked P3; critic argues P4 (the contractivity is rigid).
- **Invariant attack**: Author picked ergodic property; critic argues spectral gap (contractivity rate = gap).
- **Interpretation attack**: Solid; the cross-cut to NS is explicit in the YM PROOF-CHAIN.md.

## L16 — Continuum Schwinger functions OS0–OS4

- **Face attack**: Author picked RESONANCE; critic argues SYMMETRY (OS axioms = symmetry constraints on correlators).
- **Projection attack**: Author picked P_D; critic argues P_A (Schwinger functions can be Wick-rotated to physical / quantum observables, P_A's side).
- **Pattern attack**: Author picked P1; critic argues P4 (OS axioms are rigid).
- **Invariant attack**: Author picked BC-KMS state; critic argues C*-algebra structure.
- **Interpretation attack**: Sound; P_D / RESONANCE framing is the right call.

## L17 — [Tr F²]_R as operator-valued distribution; T_μν^R

- **Face attack**: Author picked RESONANCE; critic argues CURVATURE (Tr F² IS the Yang-Mills Lagrangian density, the curvature norm).
- **Projection attack**: Author picked P_D; critic argues P_B (T_μν is the gauge-side stress tensor).
- **Pattern attack**: Author picked P1; critic argues P4 (the operator-valued distribution is rigidly defined modulo the renormalization choice).
- **Invariant attack**: Author picked C*-algebra structure; critic argues BC-KMS state.
- **Interpretation attack**: The Pattern 1 framing is correct (renormalization = geometric reinterpretation of formal symbol).

## L18 — AF match (CONDITIONAL on H4)

- **Face attack**: Author picked RESONANCE; critic argues CURVATURE (AF is the running of the gauge coupling = curvature-side flow).
- **Projection attack**: Author picked P_O; critic argues P_B (H4 lives in the gauge-bundle / perturbative-matching framework, P_B side).
- **Pattern attack**: Author picked P5; critic argues P1 (the H4 bypass via Step 18' is a Geometric Reinterpretation: read AF directly from the non-perturbative construction, not from BARE PT).
- **Invariant attack**: Author picked scaling dimension; critic argues critical exponent.
- **Interpretation attack**: The Step 18' / H4 Bypass framing is correct and well-cited; the P_O framing is justified by L18 being the boundary where YM as a Clay outer-ring problem closes.

---

## Critic summary

- 18 layers × 5 fields = 90 attacks logged.
- Strongest disputes (where critic and author genuinely diverge):
  - L1 face: CURVATURE vs TOPOLOGY (the gap-above-ground-state is shared by both faces per paper60 §13 table)
  - L1 pattern: P4 vs P3 (Topological Rigidity vs Scale-Setting)
  - L2 face: RESONANCE vs CURVATURE (Balaban as RG of curvature)
  - L18 projection: P_O vs P_B (outer Clay vs gauge-side conditional)
- The critic finds NO assignment that the author got CLEARLY WRONG — the disputes are between two defensible alternatives, not author errors. This is consistent with the X-Ray brief expectation: a vertex's primary face/projection are usually well-determined; secondaries are negotiable.

Hand off to arbiter.
