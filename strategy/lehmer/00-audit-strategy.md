# Lehmer Totient Projection-Audit Strategy

*Community-standard: Lehmer's totient problem (1932). Does composite n exist with φ(n) | n-1? Conjecture: NO. (Distinct from Lehmer-Mahler measure conjecture.)*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 The Claim

**Source type**: COMMUNITY-STANDARD

**Source**: Lehmer (1932).

> If φ(n) | n - 1 for composite n, then n does not exist. Equivalent: φ(n) | n-1 ⇒ n prime.

Implicit requirements:
- Every composite n: φ(n) does not divide n-1
- Unconditional
- Consistent with Cohen-Hagis (≥ 14 prime factors), Pinch bounds, Banks bounds

Special provisions: Note — Lehmer ALSO has a conjecture about Mahler measure (Smyth 1971 handled non-reciprocal case) — the landscape refers to that; our audit covers Lehmer's totient problem per the outlet, with a potential sibling audit for Mahler-measure Lehmer.

## §2 Audit Gates — community-standard.

## §3 The 4 Requirements
1. No composite Lehmer number (totient sense)
2. Unconditional
3. Compatible with component/size bounds
4. Structural obstruction mechanism

## §4 Current Chain State

**Source**: `paper42-lehmer/PROOF-CHAIN.md`

Strategy: gap = BC KMS phase transition between cyclotomic and non-cyclotomic (landscape suggests Mahler-measure framing; totient framing per outlet is the primary target).

**Named walls**:
- W_L1 — Totient → prime proof; confidence 0.45 (ring confidence 3/10).

## §5 M × 4 Scaffold.
## §6 Gaps — structural proof; possible Mahler-measure bridge.
## §7-§12 standard.

## §12 PAC Brief: `strategy/lehmer/lehmer-audit-brief.md`.

---

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
