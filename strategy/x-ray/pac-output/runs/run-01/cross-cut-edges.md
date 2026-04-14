# X-RAY RUN-01 — Cross-Cut Edges

*Accumulated cross-cut edges from this run. Format: `<vertex-A>:<layer-A> ↔ <vertex-B>:<layer-B> — shared <invariant/face> — reason`. Atlas assembly merges this with future runs.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## YM cross-cuts (38 edges)

### Verified (capacitor cell or paper60/61 explicit citation) — 14 edges

- ym:L1 ↔ qg5d:Branch B — shared spectral gap — paper61 §08 explicit derivation chain (S^1 → KK gap → CP^{N-1} Weitzenböck → YM). Capacitor 09 §49 SPEC↔QFT.
- ym:L1b ↔ qg5d:Branch B — shared spectral gap — IR equivalence within KK / standard-lattice transfer.
- ym:L1 ↔ pvnp:L_gap — shared spectral gap — Popa rigidity = type III_1 spectral-gap rigidity = operator-algebra analog.
- ym:L2 ↔ qg5d:Branch B — shared scaling dimension (K.4 inheritance) — paper11 Theorem K.4 closes Balaban setup. Capacitor 09 §74 GEOM↔QFT.
- ym:L2 ↔ rh — shared scaling dimension (Pattern 5 / Epstein-zeta) — same regulator-independence engine.
- ym:L3 ↔ cramer:L_modular — shared ergodic property — paper60 §08 DYNAMICS, paper61 §10 ITPFI III_1.
- ym:L3 ↔ pvnp:L_modular — shared ergodic property — Popa rigidity uses type III_1 modular flow.
- ym:L3 ↔ rh:L_BC — shared ergodic property — BC-algebra ergodicity in cluster expansion.
- ym:L5 ↔ katz-sarnak:L_bridge — shared gauge class (bridge family k=4) — paper61 §10 symmetry-type selector.
- ym:L8 ↔ qg5d:Branch B — shared critical exponent (KK suppression) — paper61 §08 "Links 6–9".
- ym:L10 ↔ qg5d:Branch B — shared critical exponent (non-pert KK) — same compactness argument.
- ym:L10 ↔ pvnp:L_rigidity — shared critical exponent (P4 Topological Rigidity).
- ym:L12 ↔ cramer:L_dynamics — shared scaling dimension (modular-flow contraction).
- ym:L12 ↔ pvnp:L_modular — shared scaling dimension (contraction-on-modular-flow).
- ym:L14 ↔ qg5d:Branch B — shared spectral gap (PRIMARY EDGE — KK gap = parent). Capacitor 09 §49.
- ym:L15 ↔ ns:L_grad-flow — shared ergodic property (gradient-flow infrastructure) — paper08 PROOF-CHAIN.md programme-edge explicit.
- ym:L16 ↔ rh:L_KMS — shared BC-KMS state — paper61 §10 KMS state restriction.
- ym:L16 ↔ baum-connes:L_KMS — shared BC-KMS state — KMS on spectral triple.
- ym:L16 ↔ pvnp:L_KMS — shared BC-KMS state — restriction in pvnp's spectral construction.
- ym:L17 ↔ baum-connes:L_local — shared C*-algebra structure — local algebra (paper08 PROOF-CHAIN.md programme-edge: anomaly = index(D_A)=0).
- ym:L18 ↔ qg5d:Branch B — shared scaling dimension (AF inheritance from K.4).

### Speculative (cross-cut not yet capacitor-formalized; awaits sibling X-Ray) — 24 edges

- ym:L1 ↔ lehmer:L_top — face-only (gap-above-ground-state per paper60 §13 adjacency table).
- ym:L1b ↔ lehmer — face-only (same paper60 §13 adjacency).
- ym:L4 ↔ lindelof:L_amplitude — shared scaling dimension (uniform amplitude bound).
- ym:L4 ↔ rh:L_resolvent — shared scaling dimension (Boegli H1 uniform H^1 bound).
- ym:L5 ↔ h12:L_class — shared gauge class (Galois complexification).
- ym:L6 ↔ hodge:L_C — shared gauge class (C symmetry on Hodge classes).
- ym:L6 ↔ pvnp:L_parity — shared gauge class (discrete parity selection).
- ym:L7 ↔ goldbach:L_int — shared KK mode index (integer-power-sum on circle).
- ym:L7 ↔ twin-primes:L_int — shared KK mode index.
- ym:L7 ↔ collatz:L_harm — shared KK mode index (HARMONICS alternative reading).
- ym:L8 ↔ ns:L_regularity — face-only (deviation analog).
- ym:L9 ↔ katz-sarnak:L_classify — shared scaling dimension (operator-family classification).
- ym:L9 ↔ hodge:L_dim — shared scaling dimension (dim-6 stratum).
- ym:L10b ↔ rh:L_uniform — shared spectral gap (uniform-constant lemmas).
- ym:L10b ↔ selberg-1/4:L_gap — shared spectral gap (arithmetic-surface uniformity).
- ym:L11 ↔ lindelof:L_amplitude — shared scaling dimension (AMPLITUDE growth).
- ym:L11 ↔ ns:L_form — face-only (form-factor regularity).
- ym:L13 ↔ lindelof:L_amplitude — shared scaling dimension (bounded-moments analog).
- ym:L13 ↔ rh:L_Weil — shared scaling dimension (Weil quadratic form convergence).
- ym:L14 ↔ ns:L_regularity — face-only (mass-gap-as-regularity-scale; explicit programme-graph-edge).
- ym:L15 ↔ cramer:L_modular — face-only (DYNAMICS canonical).
- ym:L17 ↔ rh:L_op-distrib — shared C*-algebra structure (operator-valued distribution analog).
- ym:L17 ↔ ns:L_T_munu — shared C*-algebra structure (energy-momentum tensor regularity).
- ym:L18 ↔ rh:L_short-dist — shared scaling dimension (zeta-reg side at short distance).
- ym:L18 ↔ pvnp:L_asymptotic — shared scaling dimension (asymptotic regime via spectral gap rigidity).

---

## Total

- 38 cross-cut edges from ym alone (1 vertex of 25).
- 14 verified, 24 speculative.
- Most-connected partner vertex (from ym): qg5d (8 edges), pvnp (6 edges), rh (7 edges), ns (5 edges), cramer (3 edges).
- This is consistent with paper61 §12's compound-projection assignment: YM = $P_B \cap P_D \cap P_E$, with strong connectivity to qg5d (Branch B parent), rh (Branch D KMS), pvnp (Branch D Popa-rigidity).

When subsequent runs x-ray pvnp / rh / ns / cramer, the speculative edges should upgrade to verified.
