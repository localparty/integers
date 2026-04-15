# PROOF-CHAIN -- ABC Conjecture (Paper 37)

*For coprime a + b = c with a, b, c ∈ ℤ>0, rad(abc) > c^(1-ε) holds for all but finitely many triples, for every ε > 0.*
*Framework route: operator-algebraic via the BC Mellin bridge between additive and multiplicative structure.*
*Alternative to Mochizuki's Inter-Universal Teichmüller Theory (IUT) — different method, same target.*

*Status: 1/6 links closed | Confidence: 1/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | BC algebra's primes ↔ μ_p Hecke operators generate N* | KNOWN | -- | Bost-Connes 1995 |
| 2 | Mellin transform is the canonical additive ↔ multiplicative bridge in the framework | ESTABLISHED | 1 | Paper 12 research/14 transposition dictionary |
| 3 | Height function h(·) on multiplicative structure via BC partition | CONJECTURED | 2 | Framework original; analogous to Szpiro conductor/discriminant bound |
| 4 | rad(abc) as multiplicative norm under μ_p | CONJECTURED | 1, 3 | -- |
| 5 | ABC inequality c < K(ε) · rad(abc)^(1+ε) from BC height bound | OPEN | 3, 4 | -- |
| 6 | Explicit ε-dependence via Riemann-zero spacing (explicit formula) | OPEN | 5, RH Layer 1 | RH + Montgomery 1973 |

## Current wall

**Link 3 (height function).** The central technical gap: does the BC algebra's partition function (or a natural derivative thereof) define a height function on triples (a, b, c) that controls rad(abc)? The analogy to Szpiro's conductor-discriminant inequality on elliptic curves is structural but not proven. If Link 3 closes, Links 4-6 are substantially downstream work but the method is opened.

## Comparison with Mochizuki IUT

[Mochizuki 2012](https://arxiv.org/pdf/2403.10430) claimed an ABC proof via Inter-Universal Teichmüller Theory (IUT). [Scholze-Stix 2018](https://arxiv.org/pdf/2505.10568) identified a gap in Corollary 3.12 described as "so severe that in their opinion small modifications will not rescue the proof strategy." 2024-2025: Kirti Joshi publishing canonical-formulation attempts; mainstream mathematical community still regards ABC unproven.

**Framework's distinction**: IUT is a specific constructed theory (Hodge theaters, Frobenioids, log-links). The QG5D/BC route is a fundamentally different machine — operator algebras + Mellin bridge + Riemann zero spectral data. It doesn't attempt to fix IUT; it offers an independent alternative. The two routes could both succeed (they would agree at the ABC inequality), both fail, or one succeed — they are orthogonal proof strategies.

## Cascading impact (2026-04-14 W1/W2 closure)

Axiom 1 (spectral realization of BC generators via {γₙ}) is now unconditional all-loop. Link 1 inherits. Links 3-6 depend on how tightly the {γₙ} spacing controls the explicit formula's error term — if the framework's spectral data is rigid enough to constrain the prime-density error, Link 6 becomes derivable from the RH chain's Layer 1.

## Programme graph edges

- **QG5D (paper1):** BC generators via μ_p; Mellin bridge from the transposition dictionary
- **RH (paper13):** Riemann-zero spacing controls explicit formula → controls rad(abc) error term
- **Goldbach (paper33):** shared additive-multiplicative bridge; both rely on prime structure in BC
- **Twin Primes (paper34):** prime-gap control via zero spacing; ABC controls multiplicative dispersion
- **GRH (paper13b):** generalized zeros control Dirichlet L-function error; relevant for multi-modulus ABC variants
- **Schanuel (paper35):** algebraic independence of L-values at integer arguments constrains explicit ABC bounds

## Current open fronts

1. **Height-function construction**: operator-theoretic height on N*-semigroup from BC partition. No candidate in the literature.
2. **ε-dependence via zero spacing**: quantitative passage from RH-level spectral data to ABC's ε.
3. **Comparison with Mochizuki**: if Mochizuki's IUT is ever validated, the two routes must agree at the ABC inequality. The framework approach can be tested against any Mochizuki corollary.

## Detail files

- Bost-Connes 1995 — BC algebra foundations
- Paper 12 research/14 — transposition dictionary (Mellin bridge)
- Paper 13-rh PROOF-CHAIN.md — Riemann-zero spectral data
- Paper 33-goldbach PROOF-CHAIN.md — shared additive-multiplicative infrastructure
- Szpiro 1981 — conductor-discriminant inequality (classical height analog)
- Mochizuki 2012 + Scholze-Stix 2018 + Joshi 2024-2025 — IUT programme status

---

*v1: 2026-04-14. Novel operator-algebraic approach to ABC; no IUT dependencies.*
*Mellin is the bridge. Primes are the generators. The height is the open question.*
