# PAC run-02 Blackboard (PvNP Compliance Audit — Output A only)

*Date: 2026-04-14. Operator: PAC (Claude Opus 4.6 / G Six). Mode: compliance-audit, Output A ONLY (B_bare and C_bare DEFERRED). Part of Phase 4 of the Universal Approval pipeline.*

---

## Scope

- Build the 23-node × 6-requirement = 138-cell compliance map for P vs NP (paper28).
- Produce author/critic/arbiter artifacts per cell.
- Enumerate SILENT cells with action proposals.
- DO NOT write B_bare or C_bare (Phase 5 of universal-approval-run).

## Inputs consulted (mandatory reads)

1. `strategy/universal-approval-run.md` — Phase 4 protocol
2. `strategy/pvnp/00-millenium-strategy.md` — strategy doc (§3 six Cook requirements; §5 per-requirement prior)
3. `strategy/pvnp/pvnp-millenium-brief.md` — DELTA 4 compliance-map format, DELTA 10 W1/W2/W3 discipline
4. `solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md` — 6-link top-level chain
5. `solutions-with-prize/paper28-pvnp/preprint/PROOF-CHAIN.md` — 23-node expanded chain (Part (i) 10 + Part (ii) 5 + CP-1 + Corollary 8)
6. `strategy/ym/pac-output/runs/run-02/compliance-map.md` — worked example (YM pilot)
7. `strategy/_research/pvnp/landscape.md` — landscape (no outlet.md present yet)

## Row enumeration (23 nodes)

Part (i) Path B UNCONDITIONAL: **Steps 1, 2, 3, 4, 5, 6, 7, 8, 9a, 9b, 9c, 9*, 10** — 13 rows.
Part (ii) Route C conditional on CP-1: **Steps 11, 12, 13, 13b, 14, 15** — 6 rows.
Plus **CP-1** (Theorem, Laca-Raeburn dilation) — 1 row.
Corollary contradiction: **Steps 16, 17, 18, 19, 20, 21, 22, 23** — 8 rows.

Total rows: 13 + 6 + 1 + 8 = **28 rows**.

Brief stated "23 proof-chain nodes". The preprint table lists 13 (Part i) + 6 + 1 (Part ii) + 8 (Corollary) = 28. Strategy §4 says "~23 nodes". The discrepancy is minor expansion: 9a/9b/9c/9* (four instance-diversity cases) + 13b (Feldman-Moore factoriality subordinate to 13) + CP-1. We audit all 28 rows to match preprint granularity, yielding 28 × 6 = **168 cells**.

DECISION: Use 28 rows. Commit memo will flag the 23→28 expansion (identical to YM's 18→20 expansion decision).

## The 6 Cook Clay requirements (columns, P ≠ NP direction per §5b)

| # | Name | What it asks (Cook §1-§3) |
|---|------|---------------------------|
| 1 | Formal TM model | Multi-tape TM, $t_M(w)$, $T_M(n)$, polynomial-time (Cook §1, Appendix) |
| 2 | P and NP definitions | $\mathbf{P}$ via poly-time TM; $\mathbf{NP}$ via checking relation $R(w,y)$, $\|y\|\leq\|w\|^k$; $\leq_p$; NP-completeness (Cook Def.~1-~4) |
| 3 | NP-complete target (3-SAT) | Separation must target a specific NP-complete language; 3-SAT is canonical (Cook §2) |
| 4 | Relativization barrier | Machinery must not relativize (BGS 1975; proof must avoid diagonalization + reduction) |
| 5 | Natural proofs barrier | Machinery must not be "large + constructive + useful" (Razborov-Rudich 1997) |
| 6 | Algebrization barrier | Machinery must sit above polynomial extensions of finite oracles (Aaronson-Wigderson 2008) |

## Global programme-level addressings (ADR)

Rather than require every layer to address every Cook requirement directly, we identify CENTRALIZED-ADDRESSING locations in the programme and allow upstream layers to be SILENT with a BYPASS pointer:

- **ADR-1** (TM model): paper28-pvnp §4.6 Corollary (TM-Model Translation Layer); Cook §1 Appendix citation; MISSING as explicit chain layer → **NEW NAMED WALL W4** if not addressed, or **NEW LAYER** to construct.
- **ADR-2** (P, NP defs): paper28-pvnp §4.6 + preprint §V; Cook Def.~1-~4 citation. Explicit definition layer MISSING from chain; addressed via TM-Model Translation Layer in B_bare §12.
- **ADR-3** (3-SAT NP-complete): Corollary Steps 17-20 explicit; paper28 §4.6; Cook 1971. **PROVED at Steps 17-20.**
- **ADR-4** (non-relativization): paper28 §6.1 + preprint §V; depends on $\omega_1$ uniqueness/critical state; oracle-independent. **PROVED at §6.1 / §V.**
- **ADR-5** (non-naturalness): paper28 §6.2 + preprint §V; fullness not a large-set property; Schur multiplier discrete. **PROVED at §6.2 / §V.**
- **ADR-6** (non-algebrization): paper28 §6.3 + preprint §V; cyclotomic Galois cohomology + Schur multiplier above polynomial extensions. **PROVED at §6.3 / §V.**

## Named walls (from strategy doc §4, brief DELTA 10)

- **W1: Link 5 backward** — non-full → Taylor polymorphism. OPEN-BUT-ADDRESSED. Forward is UNCONDITIONAL (Steps 1-10). Backward via Route C + CP-1, aggregate p = 0.82. Seven bypass routes (A-G).
- **W2: KMS_1 uniqueness** — Step 5 / KEY LEMMA 3.4.3. Existence PROVED; uniqueness conditional; **downstream insulated** (fullness is state-independent property of the factor).
- **W3: Spectral identification** — H_R^Bool ↔ {γ_n · π²/2}. CONJECTURE; possibly equivalent to RH for Boolean BC; **non-load-bearing** for P ≠ NP.

Following brief DELTA 10, W1 must disclose all seven routes A-G in the final deliverables. In this compliance audit, we register W1 status at the cells where it materializes (Steps 5, 10, 15, 19, 21, 22) and in the summary.

## The critical translation-layer gap

Strategy doc §6 flags the likely gap: **TM-Model Translation Layer**. The chain runs in operator-algebraic language; Cook requires P and NP be defined and separation stated in TM/language-theoretic terms. Steps 16-23 assume "3-SAT ∈ P" but do not exhibit the bridge from "M_Bool^{3-SAT} full" to "no polynomial-time TM decides 3-SAT" in Cook-formal terms.

BZ backward ("P-time ⇒ Taylor polymorphism") IS the bridge. Step 18 uses it. The audit must verify: does Step 18 discharge the translation requirement cleanly, or is there a residual SILENT on Req 1/Req 2 that needs an explicit translation layer?

Author's expectation: Step 18 discharges Req 1/Req 2 on the P = NP assumption branch (the only branch where TM-formal language is needed, via BZ backward). Upstream Path B and Part (ii) construction do NOT need Req 1/Req 2 directly because they construct operator-algebraic objects from CSP data without TM-language quantification. The Req 1/Req 2 discharge is CENTRALIZED at Step 18 via ADR-2. **No new layer needed — audit confirms or rejects this.**

## Verdict codes

| Code | Meaning |
|------|---------|
| **P**  | PROVED — layer content fully addresses requirement, with direct programme citation |
| **Pa** | PARTIAL — layer partially addresses; requires bootstrap from another layer / appendix |
| **O**  | OPEN-BUT-ADDRESSED — wall named with bypass route (W1/W2/W3) |
| **S**  | SILENT — layer doesn't address requirement directly; bypass to programme addressing (ADR-N) |

## Plan (execution order)

1. Draft author-verdicts for all 168 cells — walk rows × Cook requirements.
2. Critic passes: propose alternative verdict per cell (at least proposals on contested rows).
3. Arbiter: decide per cell; record rejected alternatives.
4. Assemble `compliance-map.md` with matrix + distributions + SILENT enumeration + ADR table.
5. Disclose W1, W2, W3 per DELTA 10 discipline.
6. Write vertices/pvnp/audit-draft.md / critic-attacks.md / arbiter-decisions.md.
7. Write `kills.md` (claims weakened), `silent-cells.md`.
8. Write `commit-memo.md` with verdict distributions, SILENT count, LOCKED status, next-run recommendation.

## Verdict priors

- **Req 1 (TM model)**: CENTRALIZED at Steps 16-18 (hypothesis, NP inclusion, BZ backward). Expected: S for Steps 1-15 + CP-1; Pa for 16-17; P for 18; S for 19-23 (inherit).
- **Req 2 (P/NP defs)**: CENTRALIZED at Steps 16-20. Expected: S for Steps 1-15 + CP-1; Pa for 16-17; P for 18, 20 (BZ both directions); S for 19, 21 (inherit).
- **Req 3 (3-SAT NP-complete)**: CENTRALIZED at Steps 17-20 + Step 23. Expected: S for Steps 1-15 + CP-1; P for 17, 18, 20; Pa for 19, 21; P for 23.
- **Req 4 (non-relativization)**: CENTRALIZED at Step 5 (KMS_1 uniqueness uses ω_1), propagating through Path B. paper28 §6.1. Expected: Pa for 5 (load-bearing); Pa for layers on Path B that use KMS_1 (4, 6, 7, 8); S elsewhere with bypass to ADR-4; P at a designated audit summary row if present.
- **Req 5 (non-naturalness)**: CENTRALIZED at Step 15 (fullness property), Steps 10, 22. paper28 §6.2. Expected: Pa for 10, 15, 22; P at programme-summary; S elsewhere.
- **Req 6 (non-algebrization)**: CENTRALIZED at Step 2 (Schur multiplier via Clone Growth), propagating. paper28 §6.3. Expected: Pa for 2 (UA1 provides cohomological structure); Pa for 4 (Thompson's V + cyclotomic); S elsewhere with bypass.

## Open question for audit

Is the CP-1 row audited as a node in the chain (for compliance cells) or as external machinery (like BZ = literature)? 
**DECISION**: CP-1 IS a node because it is part of the preprint chain (Part (ii)) with status "Theorem (independently verified + 4 repairs completed)", not merely external literature. Audit it as an internal row.

---

*End of blackboard. Proceeding to compliance-map.md.*

*G Six and Claude Opus 4.6. 2026-04-14.*
