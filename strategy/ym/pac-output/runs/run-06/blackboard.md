# run-06 Blackboard — PAC Pillar-C HARDEN synthesis for YM

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Mode
Pillar C HARDEN — double-kill theorem skeleton. BARE MODE. Companion to `ym-clay-bare.md` (Pillar A) and `ym-independence-bare.md` (Pillar B).

## Inputs read
- `strategy/universal-approval-run.md` §5C
- `strategy/ym/00-millenium-strategy.md`
- `strategy/ym/ym-millenium-brief.md`
- `strategy/ym/deliverables/ym-independence-bare.md` (entire file)
- `strategy/ym/deliverables/ym-clay-bare.md` (§1–§15 headers)
- `strategy/_research/yang-mills/landscape.md`

## Externals inventory (from §8.4 of ym-independence-bare and §2 of clay-bare + landscape.md §Acknowledgments)
Pillar-B retained externals (non-QG5D, non-paper1-hub, non-programme-internal):

### Classical literature leaves (E1–E9)
- E1 Balaban CMP 95–119 (1982–89) — block-spin RG
- E2 Osterwalder–Schrader CMP 31 (1973) / CMP 42 (1975) — OS reconstruction
- E3 Glimm–Jaffe 1987 — Ch. 6 reconstruction
- E4 Feshbach 1958 — projection technique (L1b)
- E5 Harlander–Lüscher–Suzuki arXiv:2111.14376 — gradient-flow coefficients (L17)
- E6 Reisz CMP 116–117 (1988) — lattice power counting (Step 18')
- E7 Lüscher 2010 — gradient flow (L15, Step 18')
- E8 Osterwalder–Seiler 1978 — Wilson-action RP (L16)
- E9 Magnen–Rivasseau–Seneor 1993 — φ⁴₃ independent standing of H4-type assumption
- E10 Seiler LNP 159 (1982) — constructive gauge theory baseline
- E11 Jaffe–Witten 2000 — Clay target (problem source, not a dep)
- E12 Hairer regularity structures 2014 — parallel route reference (not used as dep; acknowledged)

### Internal self-harden
- I1 L.3.7-audit (paper08 Appendix L §L.3 Lemma L.3.7) — this is the only Pillar-B residual. YM's special case: the "external" for HARDEN purposes is our own programme's sub-lemma.

## Classification per §5C §5C.1 discipline
"non-QG5D, non-paper1, non-literature-that's-already-peer-reviewed, non-classical"

- E1 Balaban: peer-reviewed, classical (1980s-era constructive QFT). Per §5C.1 strict reading would exclude from HARDEN worklist since it's peer-reviewed literature. BUT: paper08 Step 18' uses Balaban in a novel block-spin continuation (all nine compact simple G — Balaban only covered SU(N) in 4D publicly). Paper08 Appendix K §K.1–K.9 itself generalized Balaban's RG. The HARDEN story here is: we EXTENDED Balaban's classical 4D-SU(N) + 3D-all-G results to 4D-all-compact-simple-G via the universal K.9 Summary table. That is genuine hardening.
- E2–E9: classical literature used as leaves. Per §5C.1, NOT Pillar-C worklist. But per §5C.3 "every external cited without VERIFY pass → not permitted" we do VERIFY each citation is used faithfully.
- E10 Seiler LNP 159: classical reference used for framework.
- E11 Jaffe–Witten: target, not dep.
- E12 Hairer: parallel programme, not dep; acknowledged.
- I1 L.3.7: INTERNAL, the Pillar-C SELF-HARDEN target per brief §4.

## HARDEN strategy per external
Dispatch table in deliverable §3 per external; full folder stubs scheduled under `strategy/externals-hardening/<name>/`.

Hardening types applied:
- **VERIFY**: confirm citation is used faithfully (all E-externals)
- **EXTEND**: generalize a result (E1 Balaban → all G via K.9; E5 Harlander → gradient-flow coefficients non-perturbatively; E6 Reisz → our power-counting matching)
- **CONSTRUCT**: build new sub-claim supporting the external (I1 L.3.7: paper08 §L.3 alternate proof)
- **BYPASS**: route around a specific assumption (L.3.7 alternates (i)–(iv) per Pillar B §5.1)

## Double-kill narrative template (per §5C protocol)
Per-external prose: *"We depend on X AND we strengthened X by applying PAC primitive Z, yielding [specific improvement]."* Fair attribution — X's authors benefit; our proof benefits.

## Internal self-harden structure (I1)
The L.3.7 audit is an ORA-v8 verify-and-repair wave scheduled for the 2-year Clay window. The HARDEN artifact is the stub brief + acceptance criteria + fallback alternates.

## Output files
- `strategy/ym/deliverables/ym-harden-bare.md` (primary)
- `strategy/ym/pac-output/runs/run-06/blackboard.md` (this)
- `strategy/ym/pac-output/runs/run-06/commit-memo.md`
- `strategy/ym/pac-output/runs/run-06/primitive-log.md` (critic attacks / arbiter)

## Discipline
- BARE MODE: zero prose paragraphs; tables + theorem statements + citations only
- ≤ 15 pages; target ~400–500 lines
- Fair attribution per Universal Approval
- Every claim cites programme paper + specific § OR external paper + specific §

## Arbiter
PUBLISH-READY verdict target.
