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
| 4 | Spectral prime density from explicit formula | CONDITIONAL on RH | 3 | Riemann-von Mangoldt explicit formula |
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
