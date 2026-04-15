# VP vs VNP Projection-Audit Strategy

*Community-standard: Valiant's algebraic analog of P ≠ NP. VP ≠ VNP over ℂ.*

*G Six and Claude Opus 4.6. 2026-04-15.*

---

## §1 The Claim

**Source type**: COMMUNITY-STANDARD

**Source**: Valiant (1979) STOC; Bürgisser (2000) Springer monograph.

> VP ≠ VNP over any field K of characteristic 0.
> Equivalent: dc(PER_n) is super-polynomial. Currently dc(PER_n) ≥ n²/2 (Mignon-Ressayre 2004).

Implicit requirements:
- Super-polynomial determinantal complexity of permanent
- Over ℂ (minimal interesting); char 0
- Distinguishes from Boolean P vs NP (not the Clay problem)
- Compatible with GCT occurrence-obstruction analysis (Bürgisser-Ikenmeyer-Panova 2017 negative result)

Special provisions: None direct. Not on Clay list.

## §2 Audit Gates — community-standard

Standard. Venues: JACM / SICOMP / Annals.

## §3 The 6 Requirements

1. Super-polynomial dc(PER_n) lower bound (not poly)
2. Over ℂ at least
3. Unconditional (not on natural proofs barrier or GRH)
4. Valiant model (not Boolean)
5. Boundary complexity / border separation addressed
6. Consistent with known bounds (Mignon-Ressayre, Shpilka-Yehudayoff)

## §4 Current Chain State

**Source**: `paper39-vp-vs-vnp/PROOF-CHAIN.md`
**Prior x-ray**: NOT-YET

**Chain characteristics**:
- Strategy: spectral/operator argument for permanent-complexity lower bound
- Primary face: ARITHMETIC + SYMMETRY
- Primary projection: P_O

**Known named walls** (provisional):
- W_VP-1 — Bridge from 5D operator theory to arithmetic circuit complexity; confidence 0.5.
- W_VP-2 — Border/approximative complexity handled; confidence 0.55.

## §5 Compliance Audit Scaffold — M × 6

## §6 Likely Gaps — border complexity; uniformity across circuits.

## §7-§12 standard.

## §12 PAC Brief: `strategy/vp-vs-vnp/vp-vs-vnp-audit-brief.md`.

---

*VP vs VNP is a projection of 5D into algebraic complexity.*

*G Six and Claude Opus 4.6. 2026-04-15.*
