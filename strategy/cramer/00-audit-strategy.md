# Cramér Projection-Audit Strategy

*Community-standard: prime gap p_{n+1} - p_n = O((log p_n)²). Granville refinement suggests strong form lim sup ≥ 2e^{-γ} > 1 (i.e., Cramér strong false but big-O correct).*

*G Six and Claude Opus 4.6. 2026-04-15.*

---

## §1 The Claim

**Source type**: COMMUNITY-STANDARD

**Source**: Cramér (1936).

> p_{n+1} - p_n = O((log p_n)²). Strong form: lim sup = 1.

Granville's refinement: lim sup ≥ 2e^{-γ} ≈ 1.1229.

Implicit requirements:
- Big-O bound (base Cramér)
- Unconditional (or RH-conditional variant)
- Compatibility with large-gap results (FGKMT 2014)
- Distinction between big-O and strong forms

Special provisions: Possible §5b-like variant: strong form may be FALSE, so targeting base big-O (excluding strong form as alternate) is variant-excision.

## §2 Audit Gates — community-standard.

## §3 The 5 Requirements
1. Big-O bound p_{n+1}-p_n = O((log p_n)²)
2. Unconditional OR RH-conditional (with bridge)
3. Compatible with large-gap FGKMT (Ford-Green-Konyagin-Maynard-Tao 2014)
4. Consistent with Granville refinement (lim sup > 1)
5. Matches Maier counter-intuitive fluctuation phenomena

## §4 Current Chain State

**Source**: `paper43-cramer/PROOF-CHAIN.md`

Strategy: prime gaps via spectral density of Beurling-like primes.

**Named walls**:
- W_C1 — Spectral-to-prime-gap bridge; confidence 0.55.

## §5 M × 5 Scaffold.
## §6 Gaps — unconditional vs RH; Granville refinement compatibility.
## §7-§12 standard.

## §12 PAC Brief: `strategy/cramer/cramer-audit-brief.md`.

---

*G Six and Claude Opus 4.6. 2026-04-15.*
