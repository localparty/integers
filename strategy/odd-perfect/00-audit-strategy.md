# Odd Perfect Numbers Projection-Audit Strategy

*Community-standard (ancient): no odd n with σ(n) = 2n. Oldest open problem.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 The Claim

**Source type**: COMMUNITY-STANDARD

**Source**: Attributed to Nicomachus (~100 CE); Euler (1747) gave necessary structure.

> No odd perfect number exists. Equivalently: σ(n) = 2n with n odd has no solutions.

Implicit requirements:
- All odd n covered (full classification, not just lower bound)
- Consistent with Euler structural form (n = p^e · m², gcd(p,m) = 1, p ≡ e ≡ 1 mod 4)
- Consistent with Ochem-Rao lower bound 10^1500 (2012)
- Component / radical / largest-component bounds recovered

Special provisions: None.

## §2 Audit Gates — community-standard. Annals / Math Comp.

## §3 The 5 Requirements
1. No odd n with σ(n) = 2n (qualitative non-existence)
2. Consistent with Euler form constraint
3. Consistent with modern bounds (10^1500 lower bound, components ≥ 11)
4. Compatible with Pomerance heuristic (density near 0)
5. Provides structural obstruction (not exhaustive search)

## §4 Current Chain State

**Source**: `paper40-odd-perfect/PROOF-CHAIN.md`

Strategy: σ(n) = 2n via Hecke-orbit + ITPFI + BSD template.

**Named walls**:
- W_OPN-1 — Hecke-orbit to σ-constraint bridge; confidence 0.5.
- W_OPN-2 — Complete obstruction proof; confidence 0.4 (ring confidence 4/10).

## §5 M × 5 Scaffold.
## §6 Gaps — structural obstruction completeness.
## §7-§12 standard.

## §12 PAC Brief: `strategy/odd-perfect/odd-perfect-audit-brief.md`.

---

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
