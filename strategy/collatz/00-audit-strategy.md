# Collatz Projection-Audit Strategy

*Community-standard; ACTIVE prize Bakuage 120M JPY ≈ US$1.085M (2021). Every positive integer iterated under T(n)={n/2 even; 3n+1 odd} eventually reaches 1.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 The Claim

**Source type**: COMMUNITY-STANDARD (active prize)

**Source**: Collatz (1937); Lagarias AMS volumes.

> For every positive integer n, iterated Collatz T^k(n) eventually reaches 1.

Implicit requirements:
- Every n (not density-1 almost-all)
- Total stopping time σ(n) < ∞ always
- Consistent with Tao (2019) almost-all orbits attain almost-bounded values
- Compatible with Krasikov-Lagarias density x^0.84

Special provisions: Active prize — Bakuage condition is "publication in reputable journal + committee verification."

## §2 Audit Gates — Bakuage specific:
(a) Reputable journal publication
(b) Bakuage committee verification
(c) General mathematical acceptance (per Annals / Forum Math Pi)
(d) Satisfactorily answers Collatz claim (every n → 1)

## §3 The 5 Requirements
1. Every n ∈ ℤ^+ reaches 1
2. No nontrivial cycle exists
3. No divergent trajectory
4. Stopping time bound (strong form: σ(n) ≤ C log n)
5. Compatible with Tao 2019 almost-all logarithmic density

## §4 Current Chain State

**Source**: `paper41-collatz/PROOF-CHAIN.md`

Strategy: harmonics/ergodic; density of trajectory → 1.

**Named walls**:
- W_CZ-1 — Density → everywhere strengthening; confidence 0.4.
- W_CZ-2 — No nontrivial cycle; confidence 0.6.

## §5 M × 5 Scaffold.
## §6 Gaps — density ≠ everywhere; cycle exclusion.
## §7-§12 standard (publication cascade aims at Forum Math Pi / Annals to satisfy Bakuage).

## §12 PAC Brief: `strategy/collatz/collatz-audit-brief.md`.

---

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
