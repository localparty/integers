# X-RAY RUN-01 BLACKBOARD — PAC PILOT (YM)

*Master scratchpad. Run-01 is the X-Ray pipeline pilot. Vertex: ym (Yang-Mills, paper08, 18 nodes). Annotation mode. Fixed vocabulary.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Run plan

1. READ the four mandatory inputs (DONE: README, x-ray-brief, x-ray-template, paper08 PROOF-CHAIN).
2. READ paper60 §13 (CURVATURE face) and paper61 §08–§12 (P_B, P_D, P_E, P_O) for citation anchors.
3. ANNOTATE all 18 layers (L1, L1b, L2, L3, L4, L5, L6, L7, L8, L9, L10, L10b, L11, L12, L13, L14, L15, L16, L17, L18) with the 5-field Physics block.
4. CRITIC-ATTACK every layer's 5 fields (one alternative each, minimum).
5. ARBITER-DECIDE.
6. ASSEMBLE X-RAY.md (all 10 sections, three mandatory ASCII diagrams).
7. UPDATE INDEX.md.
8. EMIT cross-cuts.
9. Write commit-memo.

## YM pre-pilot decisions

- **Top-level claim**: $\Delta_\infty > 0$ for 4D SU(N) Yang-Mills via KK spectral gap + Balaban RG + gradient-flow OS reconstruction.
- **Status**: 17/18 PROVED, 1 CONDITIONAL on H4. Confidence 9.5/10.
- **Primary branch (paper1)**: B (Gravity / KK / gauge). Secondary D (CBB through Balaban operator-algebra control).
- **Primary face**: CURVATURE (paper60 §13 — explicit canonical face for YM).
- **Primary projection**: P_B (paper61 §08 — KK gap is the gauge-bundle projection's signature). Secondary P_D (Balaban via type III_1 ergodicity).
- **Primary pattern**: P4 Topological Rigidity (CBB-style spectral gap rigidity) for the gap-bearing chain. Secondary P2 Holonomy (Wilson-loop / CP^{N-1} layers) and P5 Zeta Regularization (KK sum / Balaban polymer).

## Layer count: 18+1 = the chain table is 18 numbered links + L1b sub-link
- L1, L1b, L2, L3, L4, L5, L6, L7, L8, L9, L10, L10b, L11, L12, L13, L14, L15, L16, L17, L18
- Total 20 entries. We will treat as 18 main layers with L1b and L10b as sub-layers.

## Per-layer first-pass face/projection/pattern (DRAFT — author layer)

| Layer | Claim | Face | Projection | Pattern |
|---|---|---|---|---|
| L1  | Δ_0^KK > 0 (Weitzenböck + cluster) | CURVATURE | P_B | P4 |
| L1b | Δ_0^std > 0 (IR equiv via reduced T-matrix) | CURVATURE | P_B | P4 |
| L2  | UV stability (Balaban polymer; UV-finite all-loop via P10/P11) | RESONANCE | P_B | P5 |
| L3  | Polymer convergence κ k-independent | DYNAMICS | P_D | P5 |
| L4  | (B1) analyticity, k-independent radius | AMPLITUDE | P_D | P5 |
| L5  | (B2) SL(N,C) extension | SYMMETRY | P_D | P1 |
| L6  | C-elimination of Tr(F^3) | SYMMETRY | P_B | P1 |
| L7  | Newton decomposition: n ≥ 2 survives | ARITHMETIC | P_B | P1 |
| L8  | dev(Tr(DF)^2) ≥ 2 | CURVATURE | P_B | P4 |
| L9  | Dim-6 classification: all dev ≥ 2 | SYMMETRY | P_B | P1 |
| L10 | dev(δE_k^{d=6}) ≥ 2 non-perturbatively | CURVATURE | P_B | P4 |
| L10b | Spectral lemma constant C_p k-independent | RESONANCE | P_D | P3 |
| L11 | C_new g_k^4 Δ̂² bound | AMPLITUDE | P_B | P3 |
| L12 | RG recursion C_{k+1} = C_k/4 + C_new | DYNAMICS | P_B | P3 |
| L13 | Σ C_k g_k^4 Δ̂_k² < ∞ | AMPLITUDE | P_B | P5 |
| L14 | Δ_∞ > 0 | CURVATURE | P_B | P4 |
| L15 | Gradient-flow well-posedness, contractivity | DYNAMICS | P_B | P3 |
| L16 | Continuum Schwinger functions OS0–OS4 | RESONANCE | P_D | P1 |
| L17 | [TrF²]_R operator-valued distrib; T_μν^R | RESONANCE | P_D | P1 |
| L18 | AF match (L.2), leading-order OPE (L.4) — CONDITIONAL on H4 | RESONANCE | P_O | P5 |

## Histogram summary (preliminary)

| Face | Count |
|---|---|
| CURVATURE | 6 (L1, L1b, L8, L10, L14 + others by tilt) |
| RESONANCE | 5 (L2, L10b, L16, L17, L18) |
| DYNAMICS | 3 (L3, L12, L15) |
| AMPLITUDE | 3 (L4, L11, L13) |
| SYMMETRY | 3 (L5, L6, L9) |
| ARITHMETIC | 1 (L7) |

| Projection | Count |
|---|---|
| P_B | 13 |
| P_D | 6 |
| P_O | 1 (L18 conditional/conjecture statement) |

| Pattern | Count |
|---|---|
| P4 | 5 (L1, L1b, L8, L10, L14) |
| P5 | 4 (L2, L3, L4, L13, L18) |
| P3 | 4 (L10b, L11, L12, L15) |
| P1 | 5 (L5, L6, L7, L9, L16, L17) |
| P2 | 0 (Wilson-loop layer is sub-textual; called out in interpretations only) |

## NEEDS-CITATION flags

- None at this draft pass (all citations to paper60 §13, paper61 §08/§10, paper08, paper11, paper12 are present).

## Critic attack plan

Each layer receives one-of-each attack (face/projection/pattern/invariant/interpretation). The strongest contention will be:
- L1 vs L1b face (CURVATURE both, but L1b is also TOPOLOGY — Wilson loop transfer matrix lives on the lattice topology).
- L2 (Balaban): RESONANCE vs CURVATURE (Balaban is RG flow of curvature).
- L18 (H4): P_O outer ring vs P_B (gauge-side conditional).

## Cross-cuts (preliminary)

1. ym L1 (KK gap) ↔ qg5d Branch B (KK reduction). Same invariant: spectral gap.
2. ym L1 (KK gap) ↔ pvnp (spectral gap on Popa-rigidity construction). Same invariant: spectral gap.
3. ym L2 (Balaban UV) ↔ qg5d W1/W2 (paper10/11 unconditional UV-finite). Same invariant: scaling dimension / KK mode.
4. ym L4 (analyticity radius) ↔ rh L1 (CCM analyticity) — conjectural cross-cut: shared analyticity-of-resolvent property.
5. ym L13 (Σ C_k g_k^4 < ∞) ↔ rh (Weil quadratic form decomposition). Conjectural.
6. ym L15-L17 (gradient-flow OS) ↔ ns (paper30) — gradient-flow as NS regularity machinery (shared dynamics).
7. ym anomaly cancellation (sub-textual) ↔ hodge / baum-connes (K-theory pairing).
8. ym L1b (IR equivalence) ↔ lehmer (TOPOLOGY canonical, same gap-above-ground-state structural parallel).

## OPEN questions

- Is there a layer I should treat as having P_E (pin) primary projection? L14 produces Δ_∞, which lattice QCD pins at 1.7 GeV — but YM does not list this as a programme pin in the 36 master table. So P_E is not primary for any YM layer; mention in interpretation only.
- L18 conditional on H4: does H4 belong to the Wall section as W1 (yes) and to the Known Gaps section as G1 (yes).

## Status

- 2026-04-14, 12:00 — blackboard initial version. Author draft starts now.
