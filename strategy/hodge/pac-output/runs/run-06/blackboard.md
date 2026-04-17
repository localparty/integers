# Hodge Run-06 Blackboard — PAC Phase 5C HARDEN Synthesis

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
*Date: 2026-04-14.*
*Task: produce `strategy/hodge/deliverables/hodge-harden-bare.md` (Pillar C) — 7-section bare theorem skeleton.*

---

## Plan (pre-execution)

1. Read `strategy/universal-approval-run.md` §5C HARDEN → identify required deliverable structure + discipline.
2. Read `strategy/hodge/00-millenium-strategy.md` + `hodge-millenium-brief.md` → identify Hodge-specific parameters + 6 Deligne requirements context.
3. Read `strategy/hodge/deliverables/hodge-independence-bare.md` → enumerate the 6 retained externals + 3 residual walls.
4. Read `strategy/_research/hodge/landscape.md` → competitive-context for "no contender has done this" narrative.
5. Map 7-section structure.
6. Write `hodge-harden-bare.md` with zero prose, ≤ 15 pages, citations per claim, NOT-Kähler + rational-not-integral discipline preserved.
7. Write `commit-memo.md` + this `blackboard.md`.

## Derived 7-section structure (per universal-approval-run.md §5C + Pillar-A/B parallel)

§1 Retained externals (inventory — Pillar-C scope)
§2 Harden Theorem (main claim)
§3 Per-external X-ray + compliance weak-link table
§4 Per-external hardening work (routes produced)
§5 Double-kill narrative
§6 Pillar-C worklist + long-horizon flag
§7 References

## Retained externals enumeration (from brief + Pillar-B §1)

From task brief:
- FMS24 (ab-var-powers) — recent preprint
- GR24 (geometric Langlands) — recent
- L²-25 (2025 five-step algorithm) — recent preprint, audit target
- CCM05 (Connes-Marcolli 2005 BC algebra) — foundational
- Del[1] (Deligne motivated motives) — literature
- Atiyah-Hirzebruch (integral obstruction) — classical

All 6 enumerated + cross-checked against Pillar-B §8.4 classical-literature entries.

## Pillar-B residual walls (routed to Pillar-C)

- $W_1^{\mathrm{B}}$ = generic-$\mathcal{M}_\mathrm{BC}$-extension-audit → `motivic-Hodge-filtration/`
- $W_2^{\mathrm{B}}$ = generic $p\geq 2$ outside $\mathcal{M}_\mathrm{BC}$ (IRREDUCIBLE at Pillar B; flagged long-horizon at Pillar C) → `hodge-W2-irreducible/`
- $W_3^{\mathrm{B}}$ = L²-25 audit → `L2-25-five-step/`

## Primitive-per-weak-link assignments (drafted in §3 + §4)

| External | Layers | Primitives |
|----------|--------|------------|
| E1 FMS24 | 6 layers | VERIFY + CONSTRUCT (CM-corollary) |
| E2 GR24 | 5 layers | VERIFY + DECOMPOSE + CONSTRUCT (interface-lemma) + BYPASS |
| E3 L²-25 | 5 steps | VERIFY per-step + potential CONSTRUCT S5 |
| E4 CCM05 | 5 layers | VERIFY + CONSTRUCT ($F^p$-lemma) + EXCISE L5 |
| E5 André | 4 layers | VERIFY archival + EXCISE L4 |
| E6 AH 1962 | 3 layers | VERIFY archival |

## New lemmas CONSTRUCTed (Pillar-C output)

1. **E1.L5 CM-abelian corollary** (FMS24 extension): paper26-bsd CM module as FMS24-implied-corollary; reciprocal-value to FMS authors.
2. **E2.L3 interface-lemma**: Simpson nonabelian Hodge → GR24 spectral decomposition bridge (not in GR24 directly); $F^p$-transport on Hitchin-dual Shimura sub-slice.
3. **E4.L4 $F^p$-compatibility lemma**: zero-dim de Rham ⇒ $F^p$-trivial at weight 0; $G_\mathrm{mot}^\mathrm{end}$-compatibility vacuous on Artin-motive sub-slice.

## $W_2^{\mathrm{B}}$ long-horizon disposition

Four candidate research directions published as open invitation:
- (c1) K-theory closure via cap§ATOP-D6
- (c2) Langlands functoriality via cap§LANG-D13
- (c3) period-domain rigidity (Griffiths transcendental)
- (c4) Voisin codim-2 cycle methods

Not gated on this run. Published as audit-of-weak-links + open-invitation artifact. §5d-compliant transparent disclosure.

## §5C.3 gate check

"No external is cited without at least one VERIFY pass completed."

6/6 externals have VERIFY pass at publication. PASS.

## Discipline checklist

- [x] Zero prose paragraphs
- [x] ≤ 15 pages (~14 est)
- [x] Every claim cited
- [x] NOT-Kähler preserved (§1 abstract; §5.5)
- [x] Rational-not-integral preserved (E6 AH hardening; §4.6; §5.5)
- [x] All 3 residual walls routed
- [x] $W_2^{\mathrm{B}}$ long-horizon flag explicit
- [x] Double-kill narrative per §5C position statement
- [x] Per-external reciprocity (§5.3)
- [x] "No contender has done this" (§5.4; landscape-sourced)

## Notes / decisions

- **Fixed-width bare-mode**: all content in table-form or theorem-statement-with-citation. No prose paragraphs except abstract-italic-leaders at top/bottom per programme convention (not prose-body-of-sections).
- **Weighing E5 André and E6 AH**: these are standing/classical literature with minimal hardening value. Included as baseline archival VERIFY to maintain completeness-of-retained-externals discipline. Labeled "baseline hardening" throughout.
- **Programme-internal motivic BC**: not in Pillar-C scope (programme-internal; separate `strategy/baum-connes/` bundle responsibility).
- **$W_2^{\mathrm{B}}$ long-horizon**: explicitly NOT closed. Publishing as open-invitation is §5d-compliant.
- **8 folders under `strategy/externals-hardening/`**: 6 externals + 2 wall-routed (motivic-Hodge-filtration + hodge-W2-irreducible). L2-25 subsumes $W_3^{\mathrm{B}}$.
- **Cross-reference to CCM verification**: `strategy/ccm-verification/` is the exemplar Pillar-C instance (CCM 2025 arXiv:2511.22755); CCM05 in Pillar-C scope here is the foundational 2005 work, different from CCM 2025.

## Outcome

`strategy/hodge/deliverables/hodge-harden-bare.md` — DRAFTED, 7 sections, bare mode, PUBLISH-READY target.

`strategy/hodge/pac-output/runs/run-06/commit-memo.md` — LOCKED recommendation.

Ready for Zenodo companion-release alongside Pillar A + Pillar B bare skeletons.
