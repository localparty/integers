# OPN Route 6a: CLOSED-NEGATIVE (Kill)

*The odd Robin inequality cannot prove OPN nonexistence.*

## The direction error

The T6 E₂ work proposed: "the halved Mertens constant e^γ/2 ≈ 0.891 gives an odd Robin bound σ(n)/n < (e^γ/2)·ln(ln n) < 2 for all odd n > ~12,847, proving no OPN exists above that threshold."

**This reasoning is backwards.** The bound (e^γ/2)·ln(ln n) is BELOW 2 only for n < ~12,687. For n > 12,687, the bound EXCEEDS 2 — which is true but vacuous for the OPN question.

## The fatal fact

σ(n)/n > 2 for infinitely many odd n. Explicitly:
- σ(1155)/1155 = 1.995 (just below 2)
- σ(15015)/15015 = 2.148 (above 2)
- σ(45045)/45045 = 2.327 (well above 2)
- The odd primorial sequence diverges: lim sup = e^γ/2 · ln(ln n) → ∞

**There is no inequality-based route to OPN nonexistence.** The question is about EXACT equality σ(n)/n = 2, not whether σ(n)/n can exceed 2 (it can, easily).

## What Route 6a DID establish (productive content)

1. The odd Gronwall constant lim sup_{n odd} σ(n)/(n·ln(ln n)) = e^γ/2 — rigorously derived via two independent methods (Mertens for odd primes; Dirichlet series residue).
2. The Dirichlet series zero at s=1 from factor (1-2^{1-s}) is a genuine spectral signature of the "missing 2."
3. For the finite range (N₀, 12687), odd Robin gives σ(n)/n < 2 — complementing the computational bound N > 10^{1500}.

## Route status update

| Route | Status | Reason |
|---|---|---|
| 6a (odd Robin) | **CLOSED-NEGATIVE** | σ(n)/n > 2 for infinitely many odd n; inequality cannot prove exact-equality impossibility |
| 6b (E₂ quasi-modular) | BLOCKED-DECOMPOSED | Odd restriction destroys quasi-modularity; productive output absorbed into 6a (now killed) |
| 6c (ABC auxiliary) | CONDITIONAL on ABC | Viable but imports unproved ABC |
| **6d (ITPFI resonance)** | **OPEN — new priority** | The ITPFI joint constraint on the product ∏ h(p^v) = 2 is the remaining framework-native route. The question is algebraic: can the ITPFI tensor product structure obstruct exact resonance at h = 2 for odd compositions? |

## The honest lesson

The OPN question is harder than any inequality can reach. It asks for a RESONANCE obstruction — why can't local abundancy factors at odd primes conspire to produce exactly 2? This is a Hasse-principle question (local solutions exist but global assembly fails), not an asymptotic bound question. The BSD template (local-global obstruction via Brauer class) remains the structurally correct analogy. Route 6d (ITPFI resonance) inherits this framing.

*Kill recorded. The honest negative refines: OPN is about resonance, not bounds.*
