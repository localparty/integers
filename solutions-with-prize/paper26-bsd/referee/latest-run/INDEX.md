# INDEX — BSD Math Referee Run r01

*Paper 26 rigor audit, 2026-04-10.*

## Primary deliverables

- **`rigorous-proof.md`** — the yang-mills-standard reformulation
  with every step labeled [THEOREM] / [LEMMA] / [KEY LEMMA — OPEN]
  / [GAP]. **Read this first.**
- **`summary.md`** — overall rigor verdict, closing statements.
- **`rigor-checklist.md`** — master roll-up table of ~35 checks.
- **`computation-log.md`** — every venv check performed, with
  results and verdicts.

## Supporting files

- **`points/`** — per-point analyses (A1–E2):
  - A1 Ha-Paugam BC over K
  - A2 Nelson self-adjointness
  - A3 Meyer spectral inclusion — **HEAVY**
  - B1 Bridge family over Q(i)
  - B2 Cocycle shift formula — **HEAVY**
  - B3 ITPFI over K
  - C1 Baker theorem application — **HEAVY**
  - C2 Cocycle shift properties
  - D1 CM L-function factorization
  - D2 Kolyvagin rank 0
  - D3 Gross-Zagier + Kolyvagin rank 1 — **HEAVY**
  - E1 Assembly — **HEAVY**
  - E2 Adversarial check

- **`checks/`** — per-check files in 13 groups:
  - R (rank equality)
  - LC (leading coefficient)
  - AC (analytic continuation)
  - BC (Bost-Connes foundation)
  - MY (Meyer spectral inclusion)
  - BR (bridge family)
  - IT (ITPFI factorization)
  - TR (transcendence / Baker)
  - DS (dark states)
  - CM (CM L-function factorization)
  - KV (Kolyvagin)
  - GZ (Gross-Zagier)
  - SHA (Tate-Shafarevich)

## Headline finding

**Rigor scorecard for the 11-step proof chain:**
- [THEOREM] or [LEMMA]: 7/11
- [KEY LEMMA — OPEN]: 3/11
- [GAP]: 1/11

**The three [KEY LEMMA — OPEN] items:**
1. Meyer distributional → point spectrum upgrade (Key Lemma A)
2. Twisted spectral inclusion for L(s, ψ) over K (Key Lemma B)
3. Cohomology-class integrality premise (Key Lemma C)

**The [GAP]:** Proposition 4.3's bridge table has 3 of 4 rows
broken (direct computational check).

**The most critical item:** Key Lemma C (cohomology class vs
cocycle representative). The entire bridge kill mechanism rests
on this premise, which Paper 26 asserts but does not prove.

## Coordination

When the Clay compliance referee (`02-clay-referee.md`) runs next,
it should consult `summary.md` and `rigorous-proof.md` for the
rigor verdict (per its Point CA10). The two audits are designed to
coexist in this `latest-run/` directory without conflict.
