# PAC run-02 Blackboard — RH Compliance Audit (Phase 4, Output A only)

*Date: 2026-04-14. Operator: PAC (Claude Opus 4.6 / G Six). Mode: compliance-audit. Output A (internal artifacts) only — B_bare + C_bare DEFERRED to run-03/run-04.*

---

## Scope

- Build the 14-row × 7-column = **98-cell** compliance map for Riemann Hypothesis (paper13-rh).
- Produce author/critic/arbiter artifacts per cell.
- Enumerate SILENT cells with actions (NEW-NAMED-WALL / NEW-LAYER-SKETCH / BYPASS-VIA-CAPACITOR).
- Disclose named walls (W1 CCM, W2 CF-uniformity-resolved) per DELTA 10.
- DO NOT write B_bare or C_bare this run (Phase 5).

## Inputs consulted

1. `strategy/universal-approval-run.md` — Phase 4 contract
2. `strategy/rh/00-millenium-strategy.md` — §1 Bombieri verbatim, §3 7-requirement list, §4 chain state, §5 audit scaffold
3. `strategy/rh/rh-millenium-brief.md` — DELTA 4 matrix format, DELTA 10 W1/W2 disclosure discipline
4. `solutions-with-prize/paper13-rh/PROOF-CHAIN.md` — live 6-primary-layer + 3-supporting chain (14 rows after sub-layer expansion)
5. `strategy/ym/pac-output/runs/run-02/compliance-map.md` — YM pilot format template
6. `strategy/ym/pac-output/runs/run-02/commit-memo.md` — lock-status template
7. `strategy/ym/pac-output/runs/run-02/silent-cells.md` — SILENT-action template
8. `strategy/_research/rh/landscape.md` — acknowledgments context (CCM + Bombieri + Conrey + Sarnak + Iwaniec–Kowalski)
9. `strategy/rh/rh-millenium-brief.md` §PROCEDURE Step 2-3 — rubric for verdict emission

NOTE: `strategy/_research/riemann/outlet.md` not present; the 7 Bombieri requirements are taken from `strategy/rh/00-millenium-strategy.md §3` which itself cites Bombieri "Problems of the Millennium: The Riemann Hypothesis" (Clay official problem description, §I + §III–§VI). This is the stable source per the brief.

## The 7 Bombieri requirements (columns)

Source: `strategy/rh/00-millenium-strategy.md §3` (Clay official problem description by Bombieri).

**Core (mandatory, §5d-required):**

| # | Name | What it asks |
|---|------|---|
| 1 | RH for ζ(s) on Re(s) = ½ | Minimum statement — all non-trivial zeros on critical line |
| 2 | PNT error π(x) = Li(x) + O(√x log x) | Equivalent PNT-error formulation, sharp bound |
| 3 | Analytic continuation + functional equation | Meromorphic to ℂ, simple pole at s = 1 residue 1, Γ-factor FE Eq. (1) |
| 4 | Trivial vs non-trivial zeros distinction | Trivial at −2, −4, …; non-trivial in 0 < Re(s) < 1 |
| 5 | Consistency with numerical evidence | First 1.5 × 10⁹ zeros (van de Lune et al.); Odlyzko 10²² heights; > 40% on line (Conrey) |

**Optional (§5d-encouraged, strengthen deliverable):**

| # | Name | What it asks |
|---|------|---|
| 6 | GRH for global L-functions | Dirichlet, automorphic/ℚ, elliptic-curve, Maass (Bombieri §II + §IV–§VI) |
| 7 | Weil explicit formula | Zero-sum ↔ prime-sum ↔ archimedean-term consistency (Bombieri §V) |

## The 14 chain rows (expanded from PROOF-CHAIN.md)

Live `solutions-with-prize/paper13-rh/PROOF-CHAIN.md` lists 6 primary layers + 3 supporting:

- **L1** — CCM operators D_N on E_N^+ (EXTERNAL — arXiv:2511.22755)
- **L2** — ITPFI: ω_1 = ⊗_p ω_1^(p) (KMS_1 uniqueness + Weil form convergence) (PROVED)
- **L3a** — Archimedean sub-leading: O(1/λ) (PROVED)
- **L3b** — Eigenvector approximation: O(log λ / λ) (PROVED)
- **L3c** — H¹ bound: ‖(D_N − i)^{−1}‖_{L²→H¹} < 2 (PROVED)
- **L3d** — CF decay: ρ ≥ 4.27 uniform in N (PROVED; Remark 8.4 caveat resolved by S2 Lemma 12.1, 2026-04-14)
- **L4a** — Boegli H1 (gsrc) (PROVED)
- **L4b** — Boegli H2 (discrete compactness) (PROVED)
- **L4c** — Spectral exactness: spec(D_∞) = lim spec(D_N) (PROVED)
- **L5** — Hurwitz: ξ̂_N → Ξ uniformly on compacts (PROVED)
- **L6** — spec(D_∞) = {γ_n} ⊂ ℝ ⇒ RH (QED)
- **S1** — AE simplicity (PROVED)
- **S2** — Slepian compatibility: A^{ev} = K_λ|_grid + O(e^{−cN}) (PROVED) — resolves W2 CF uniformity caveat
- **S3** — γ_E elimination: uniform diagonal shift (PROVED)

14 rows × 7 columns = **98 cells**.

## Plan (execution order)

1. Draft author-verdicts for all 98 cells — walk L1→L6 + S1→S3 by Bombieri requirement.
2. Critic passes: propose alternative verdict per cell (must propose at least one; agreement acceptable).
3. Arbiter: decide per cell; record rejected alternatives.
4. Assemble `compliance-map.md` with matrix + verdict distribution + §5d compliance check + SILENT enumeration.
5. Enumerate SILENT cells with action proposals.
6. Write `vertices/rh/audit-draft.md` + `critic-attacks.md` + `arbiter-decisions.md`.
7. Write `kills.md` (claims weakened during audit), `silent-cells.md`.
8. Write `commit-memo.md` with verdict distributions, SILENT count, LOCKED / NOT-LOCKED status, next-run recommendation.

## Verdict rubric

- **PROVED** (P): layer's own content fully establishes the requirement (with direct programme citation).
- **PARTIAL** (Pa): layer partially addresses — requires bootstrap from another layer / supporting lemma.
- **OPEN-BUT-ADDRESSED** (O): layer explicitly names the requirement as a wall with bypass route documented (W1 CCM at L1).
- **SILENT** (S): layer does not address the requirement at all — triggers action (NEW-NAMED-WALL / NEW-LAYER-SKETCH / BYPASS-VIA-CAPACITOR or BYPASS-VIA-PROGRAMME-ADDRESSING).

Default: if a layer's statement is on one axis (e.g., L3c is about H¹ bound on resolvent) and says nothing about another (e.g., Req 2 PNT error), verdict is SILENT unless the content inherently carries the requirement. Silence is not a defect per se — the question is whether ADDRESSED somewhere in the chain. If yes, propose BYPASS-VIA-PROGRAMME-ADDRESSING (ADR-N) pointing to the addressing layer.

## Verdict priors (before per-cell audit)

Global programme picture (before per-cell audit):

- **Req 1 (RH on ½)**: **OPEN-BUT-ADDRESSED** at L6 QED; conditional on W1 (CCM L1). Upstream PARTIAL per contribution. Supporting S1–S3 SILENT on RH itself (infrastructure).
- **Req 2 (PNT error)**: **ADDRESSED via classical equivalence** — RH ⟺ π(x) = Li(x) + O(√x log x) is a downstream corollary (Bombieri §I, Riemann–von Mangoldt). Only L6 can anchor this directly; upstream layers SILENT → BYPASS to programme addressing at L6 (and to classical Bombieri §I citation for the equivalence direction).
- **Req 3 (analytic continuation + FE)**: **CLASSICAL PREREQUISITE** — ζ(s) meromorphic extension + Eq. (1) is used implicitly throughout (L2 ξ-function convergence relies on FE). Needs explicit citation at L2 (where ξ̂_N / Weil form appears) and in B_bare §5 standalone section. Upstream L1 construction inherits ξ(s) structure; L3–L5 all use FE via Ξ / ξ̂. Expected PARTIAL at L2 and PROVED via CITATION at the programme-entry node (B_bare §5). Other layers SILENT → BYPASS to §5.
- **Req 4 (trivial vs non-trivial)**: **IMPLICIT IN L1–L6** — the CCM construction E_N^+ restricts to the even ξ-entire-function spectrum, yielding only non-trivial zeros {γ_n}; trivial zeros at −2, −4, … are excluded by the Γ(s/2)-pole structure of ξ(t). Expected PROVED at L1 (construction) and L6 (QED match); SILENT at L2–L5 except where ξ̂_N uses the even-function restriction (→ PARTIAL at L5 Hurwitz).
- **Req 5 (numerical evidence)**: **CONSISTENCY AT L6 and S1** — 10²²-height Odlyzko comparison + first-1.5 × 10⁹-zeros match validates D_∞ spectrum match. Expected PROVED at L6 (side-check); PARTIAL at S1 (AE simplicity cert N ≤ 20 + Slepian limit consistent with simple-zeros cluster). L2–L5 SILENT → BYPASS.
- **Req 6 (GRH)**: **BONUS via paper13b character twist** (not required by §5d core). Expected SILENT at paper13-rh layers; ADDRESSED via paper13b-grh as programme extension. Optional per §5d — every SILENT is allowed here unless we choose to strengthen (we do — paper13b-grh references in B_bare §14 and C_bare §5).
- **Req 7 (Weil explicit formula)**: **L2 carries "Weil form convergence"** as an ingredient → promote to PROVED or PARTIAL at L2 via explicit citation to integers/paper12-cbb-system/research/102 §3.1 (Mellin duality H_BC = log T_BC) + Bombieri §V. Other layers SILENT → BYPASS to L2.

## Expected SILENT count

Per the priors, ~50–60 of 98 cells expected SILENT. No cell expected to require NEW-NAMED-WALL or NEW-LAYER-SKETCH: the chain is structurally complete for §5d. All SILENT cells should take BYPASS-VIA-PROGRAMME-ADDRESSING actions (ADR-N pointing to the addressing layer in the existing chain or to a classical citation).

**Exception watch**: if Req 4 (trivial vs non-trivial) cannot be anchored explicitly in L1 or L6, then NEW-LAYER-SKETCH may be triggered. The brief §6 flags this as one of four "likely gaps". Audit must verify.

## Verdict assignment discipline

For each (row, requirement) cell, apply the rubric and cite:
- Programme paper (paper13-rh PROOF-CHAIN row + specific source section/lemma)
- External citation only for arXiv:2511.22755 (W1) at L1
- Bombieri §X for classical-prerequisite citations
- integers/paper12-cbb-system/research/102 for Mellin duality / Weil form anchor (Req 7)
- solutions/paper13b-grh/... for GRH extension (Req 6)

## Named walls (expected)

- **W1** — CCM Layer 1 operators (arXiv:2511.22755). Primary. Full DELTA 10 disclosure in compliance-map.md.
- **W2** — CF uniformity caveat (Remark 8.4). RESOLVED 2026-04-14 via S2 Slepian compatibility Lemma 12.1. Full DELTA 10 disclosure in compliance-map.md with status = RESOLVED. Retained in list for transparency.

No new named walls expected. Audit must verify.

## Decisions

- **Row count**: 14 (L1, L2, L3a–L3d, L4a–L4c, L5, L6, S1, S2, S3). Matches PROOF-CHAIN.md enumeration exactly. No collapsing of sublayers — each has a distinct verdict profile.
- **Column count**: 7 (Core 1–5 + Optional 6, 7). All seven audited because DELTA 4 requires it for transparency.
- **SILENT-on-optional is OK**: Req 6 (GRH) and Req 7 (Weil EF) are strengtheners. Core 1–5 must have ≥ 1 non-SILENT cell each for §5d LOCK.
- **LOCK criterion**: all 98 cells have verdict + citation + arbiter decision; zero SILENT cells WITHOUT an action; every Core 1–5 requirement has ≥ 1 non-SILENT cell.

## Open questions (watchlist during audit)

1. Is Req 4 (trivial vs non-trivial) explicitly addressed in the chain, or silent-only-with-bypass? Verify at L1 (E_N^+ construction) and L6 (QED match).
2. Does L2 "Weil form convergence" cite Weil explicit formula with sufficient §-level precision, or is it a promotable PARTIAL?
3. Is Req 3 (analytic continuation + FE) cited explicitly in paper13-rh or only implicit? Audit pointer expected at §L5 Hurwitz (ξ̂_N → Ξ) and §L6 (ξ entire).
4. Is Req 5 (numerical evidence) anchored in a side-check section, or only in the strategy document? Compliance with §5d requires explicit inclusion in B_bare §14 (future run); audit flags PARTIAL if only strategy-level.

---

*End of blackboard. Proceeding to per-cell author-draft.*
