
# run-03 Blackboard — B_bare synthesis

*PAC run-03. MODE: bare-deliverable-synthesis. Output B_bare only (Clay-shaped X-ray). Output A LOCKED (run-02). Output C_bare parallel (run-04, sibling agent). B_full DEFERRED.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Plan

1. Read inputs (§1-§6 in brief) — DONE.
2. Plan section-by-section strategy per B_bare 17-section template.
3. Author first-pass draft at `vertices/ym/b-bare-draft.md`.
4. Critic attacks per-section bare-discipline violations → `vertices/ym/critic-attacks.md`.
5. Arbiter decisions w/ rejected footnotes → `vertices/ym/arbiter-decisions.md`.
6. Final B_bare at `deliverables/ym-clay-bare.md`.
7. Commit memo.

## Sources of truth

- Compliance map LOCKED at run-02 → ground truth for §3 Requirements Map verdicts.
- paper08-yang-mills preprint sections → ground truth for theorem statements (K, I4, L, §05).
- solutions-with-prize/paper08-yang-mills/research/51-infinite-volume.md → ground truth for ℝ⁴ limit (ADR-2).
- solutions-with-prize/paper08-yang-mills/h4-capacitor-bypass/closure/closure-digest.md → ground truth for H4 named-wall fields.
- X-RAY.md run-01 → ground truth for face/projection/pattern histograms (§14).

## Citation conventions (adopt from run-02)

- `p8§NN` = preprint/sections filename stem
- `p8R§NN` = research/NN-filename stem
- `p8L.X.Y` = Appendix L Lemma L.X.Y
- `p8K.N` = Appendix K §K.N
- `p8I4.N` = Appendix I.4 §I.4.N
- `p8F.N` = Appendix F §F.N
- `h4CB/cyc5` = h4-capacitor-bypass/cycle-5 (via closure-digest; synthesis/wave1 artifact)
- `cap§N` = millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md §N

## §3 Requirements Map — verdicts from run-02 compliance map

Authoritative (LOCKED run-02):

| Req | J-W requirement | Verdict | Layers (highest) | Citations |
|-----|-----------------|---------|------------------|-----------|
| 1 | Any compact simple G | PROVED | L2-L7, L14 (P-cells pervasive) | p8I4 Thm I.4.1; p8K.9 Summary table |
| 2 | On ℝ⁴ (infinite volume) | PROVED | L14, L16, L17 | p8R§51 III + IV; §51 V |
| 3 | Mass gap uniform in V | PROVED | L1b, L10, L10b, L11, L12, L13, L14, L16 (8 P-cells) | p8R§51 II; p8F.5 Remark |
| 4 | Wightman/OS axioms | PROVED | L16, L17 | p8§05.6 Proof of (f) OS1-OS5; p8§05 Wightman correspondence table |
| 5 | AF match at short dist | OPEN-BUT-ADDRESSED | L18 (H4 named wall) | p8L.7; h4CB closure-digest 2026-04-13 Step 18' |
| 6 | Stress tensor + OPE | PROVED | L17 | p8L.0(c) Lemma L.4.1; L.0(d) Lemma L.4.3 |
| 7 | Non-triviality | PROVED | L14, L18 | p8§05 Proposition Non-triv (three signatures) |

## Bare-discipline discipline

Per DELTA 3: ONLY theorem statements, definitions, equations, figures (ASCII/TikZ-skeleton), numbers (tabulated with citations), compliance analytics, citations. NO prose paragraphs. Delete any "we show", "note that", "in this section".

Per DELTA 8: Every claim cites programme paper + §-level location.

Per DELTA 10: H4 in §10 + §15 with all 7 required fields.

## Per-section brief

- **§1 Problem**: verbatim J-W quote (strategy §1). No commentary.
- **§2 Main Theorem**: YM Existence and Mass Gap statement. Cite §§5-13 for proof via paper08 Appendix I.4 Theorem I.4.1.
- **§3 Requirements Map**: 7-row verdict table (LOCKED from run-02).
- **§4 Definitions**: gauge field A, curvature F, Euclidean measure dμ, reflection positivity, mass gap Δ.
- **§5 Measure Construction**: Thm 5.1 existence of dμ on S'(ℝ⁴,g). Cite p8R§51 III, paper08 Appendix H (Balaban analyticity setup) — Thm 1 in preprint body.
- **§6 OS Reflection Positivity**: Thm 6.1 OS0-OS5. Cite p8§05.6 Proof of (f). Also Appendix D (reflection positivity).
- **§7 OS→Wightman**: Thm 7.1 W0-W5. Cite p8§05 Wightman correspondence table.
- **§8 Mass Gap Uniform in V**: Thm 8.1 Δ uniform as V→ℝ⁴. Cite p8R§51 II.1-II.3 + p8F.5 Rem. Numerical bound Δ ≥ 0.999·δ₀.
- **§9 Infinite Volume Limit**: Thm 9.1 Moore-Osgood limit. Cite p8R§51 III + IV.
- **§10 AF Match (H4 disclosure)**: Thm 10.1 + NAMED WALL W1 per DELTA 10 (7 fields).
- **§11 Stress+OPE**: Thm 11.1 T_μν Suzuki + Thm 11.2 OPE. Cite p8L.4.1 + p8L.4.3.
- **§12 Group Generality**: Thm 12.1 any compact simple G. Cite p8I4.1 Thm I.4.1 + p8K.9 Summary.
- **§13 Non-triviality**: Thm 13.1. Cite p8§05 Prop Non-triv (three signatures).
- **§14 Proof-Chain Analytics**: 20-node ASCII DAG; RIGIDITY (P4 count); SYMMETRY face+projection histograms; pointer to run-02 compliance map.
- **§15 Named Walls**: W1 (H4) expanded. Zero additional (run-02 confirmed).
- **§16 Numbers Table**: Δ_∞, δ₀, b_0(G), R=10.10μm, c_N, C_p, etc.
- **§17 References**: AMS format, programme papers with §-level entries.

## Target

≤ 15 pages ≈ 400-600 lines md. Each section kept as short as the bare theorem statement + citation requires. Strict.

## Blockers / NEEDS flags (to monitor)

- NONE expected at outset. All citations validated in run-02 compliance map.
- If any theorem needs NEEDS-CONSTRUCTION flag, log here + placeholder in draft. Do not invent.

## Execution order

(a) Write B_bare draft in single pass, section by section.
(b) Critic reads for bare-discipline violations (prose, uncited claims, page count).
(c) Arbiter ships.

---

*End of blackboard. Execution begins.*
