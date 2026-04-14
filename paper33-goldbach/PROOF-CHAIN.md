# PROOF-CHAIN -- Goldbach Conjecture (Paper 33)

*Every even integer >= 4 is the sum of two primes.*
*The BC algebra provides a natural home via prime Hecke operators*
*and the Mellin bridge between additive and multiplicative structure.*

*Status: 2/6 links closed | Confidence: 1/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | Primes generate BC algebra via mu_p | KNOWN | -- | Bost-Connes 1995 |
| 2 | Hecke semigroup N* encodes multiplicative structure | KNOWN | -- | BC construction |
| 3 | Mellin bridge: additive <-> multiplicative | ESTABLISHED | 1, 2 | Paper 12 transposition |
| 4 | Spectral prime density from explicit formula | CONDITIONAL (cross-paper transport from Paper 13 RH; equivalently CONDITIONAL on CCM 2025, not an independent RH assumption) | 3 | Riemann-von Mangoldt explicit formula; see Paper 13 PROOF-CHAIN.md (RH at 8/10 conditional on CCM 2025). Tagged cross-paper 2026-04-14 per Agent-I audit item 6. |
| 5 | Circle method in BC/adelic setting | OPEN | 4 | Hardy-Littlewood-Vinogradov + adelic reformulation |
| 6 | Even-indexed KMS_1 decomposition as prime convolution | OPEN | 5 | Novel -- the core conjecture |

## Current wall

**Link 5 (circle method transfer).** Reformulating the Hardy-Littlewood
circle method within the BC/adelic framework requires:

1. Expressing the circle method's major/minor arc decomposition via
   Q/Z characters within C*(Q/Z)
2. Translating Vinogradov's exponential sum estimates into the
   BC algebraic setting
3. Closing the gap between "sufficiently large" and "all even integers"

**What is known classically:**
- Under RH: binary Goldbach holds for sufficiently large N (Montgomery-Vaughan 1975)
- Helfgott 2013: ternary Goldbach proved (every odd >= 7 is sum of 3 primes)
- Binary (even) case remains fully open

The BC framework provides a natural language (KMS_1 states decompose over
primes) but no obvious new analytic tools beyond the classical circle method.
Link 6 (even-indexed KMS_1 decomposition as prime convolution) is the novel
conjecture that would need to yield new estimates.

## Programme graph edges

- **RH (paper13-rh):** explicit formula gives prime density; RH -> asymptotic Goldbach
- **GRH (paper13b-grh):** Dirichlet GRH -> primes in progressions -> additive structure
- **QG5D (paper1):** Hecke semigroup N* is the multiplicative engine
- **BGS (paper32-bgs-spectral-statistics):** spectral prime density feeds Link 4
- **Twin Primes (paper34-twin-primes):** shared additive prime structure

**GUE three-tail structure.** Goldbach IS the bulk regime of the GUE distribution. The sine-kernel universality (Tao-Vu 2011) controls prime density in intervals. Inherits from BGS (7/10) via the GUE three-tail structure: small-gap tail (Twin Primes, gap=2), bulk (Goldbach, sine-kernel density), large-gap tail (Cramer, max gap ~ log^2 x). The bulk regime provides the prime density guarantees that the circle method (L5) requires.

## Cascading refinement from QG5D W1/W2 closure (2026-04-14)

Paper 1 PROOF-CHAIN.md W1 (scheme independence) and W2 (Route-C 3-loop explicit) both closed 2026-04-13/14 via Paper 10 (Theorem 1 two-loop scheme-independence + Theorem U.2a one-loop Seeley-DeWitt) + Paper 11 (Theorem K.4 all-orders inductive bootstrap) + explicit L=3 numerical verification at 50-digit precision (`paper1/code/K-5-2-route-c-3loop.py`). Cascading impact on this chain: the CBB system's Axiom 5 (zeta regularization closure) no longer has a lingering regulator-scheme question. Effect is cosmetic-to-small — this chain never gated on the scheme question directly, but the underlying foundation is now strictly stronger. No link status changes required; confidence unchanged; mention included for completeness of the programme graph.
