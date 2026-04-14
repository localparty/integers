# PROOF-CHAIN -- Twin Prime Conjecture (Paper 34)

*Infinitely many primes p with p+2 also prime.*
*The spectral route: GUE pair-correlation statistics of Riemann zeros*
*(via BGS chain) predict the Hardy-Littlewood twin prime asymptotic*
*pi_2(x) ~ 2 C_2 x/(log x)^2.*

*Status: 1/5 links closed | Confidence: 1/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | Explicit formula: prime gaps <-> zero spacing | KNOWN | -- | Riemann-Weil explicit formula |
| 2 | Zero pair correlation -> gap statistics | CONDITIONAL on BGS | 1 | Montgomery 1973 |
| 3 | GUE small-gap tail -> bounded prime gaps | ESTABLISHED | -- | Zhang 2013, Maynard-Tao 2014 (gap<=246) |
| 4 | GUE -> Hardy-Littlewood twin prime constant C_2 | CONJECTURED | 2, 3 | **Nov 2025 Hardy Z PCC (arXiv:2511.18275): GUE sine-kernel proved** |
| 5 | C_2 > 0 -> infinitely many twin primes | CONDITIONAL on L4 | 4 | Hardy-Littlewood conjecture |

## Current wall

**Link 4 (arithmetic correction factor C_2 from GUE fine structure).**

The Nov 2025 Hardy Z-function PCC proof establishes GUE sine-kernel
convergence, but extracting the arithmetic constant
C_2 = prod_{p>2} (1 - 1/(p-1)^2) requires:

1. Going beyond bulk GUE into mesoscopic zero statistics
2. Incorporating sieve-theoretic arithmetic correction factors
3. Relating the spectral (zero) pair correlation to the arithmetic
   (prime) pair correlation with the correct local factors

**What is known classically:**
- Zhang 2013: infinitely many gaps <= 7 x 10^7
- Maynard 2015 / Polymath 8b: gap <= 246
- Under GRH + Elliott-Halberstam: gap <= 6 (GPY 2005)
- Gap = 2 requires the full C_2 computation, which is beyond current methods

The Nov 2025 result provides the GUE side; the missing piece is the
arithmetic-to-spectral dictionary at the level of individual local factors.

## Programme graph edges

- **BGS (paper32-bgs-spectral-statistics):** GUE pair correlation feeds Link 2
- **RH (paper13-rh):** zero spacing via explicit formula controls gap statistics
- **GRH (paper13b-grh):** GRH + Elliott-Halberstam -> gaps <= 6
- **Goldbach (paper33-goldbach):** shared additive prime structure
