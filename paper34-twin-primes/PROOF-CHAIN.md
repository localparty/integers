# PROOF-CHAIN -- Twin Prime Conjecture

*Research programme (not a proof chain). Infinitely many primes p with p+2 also prime. The spectral interpretation: twin primes correspond to specific pair-correlation statistics of Riemann zeros at close spacing.*
*Status: programme only (~1/10) | Confidence: 1/10*

## Entry point
The explicit formula connects prime gaps to zero spacing. Twin primes (gap=2) require constructive interference at gap=2 in the oscillatory sum over zeta zeros. The BGS chain (if closed) would give GUE pair correlation, which predicts the Hardy-Littlewood asymptotic pi_2(x) ~ 2 C_2 x/(log x)^2.

## Key question
Can GUE bulk statistics + explicit formula + mesoscopic refinements close the gap from bounded gaps (Zhang-Maynard-Tao, gap <= 246) to twin primes (gap = 2)?

## Open steps

| Step | Description | Status |
|---|---|---|
| 1 | Close the BGS chain (see bgs-spectral-statistics) | OPEN |
| 2 | Derive bounded gaps as corollary of GUE + explicit formula | OPEN |
| 3 | Extend GRH to all Dirichlet characters in BC framework | OPEN |
| 4 | Investigate mesoscopic zero statistics beyond bulk GUE | OPEN |
| 5 | Reproduce arithmetic factor C_2 from BC sieve structure | OPEN |

## What is known
- Zhang 2013: infinitely many gaps <= 7x10^7
- Maynard 2015 / Polymath 8b: gap <= 246
- Under GRH + Elliott-Halberstam: gap <= 6 (GPY 2005)
- Gap=2 requires going beyond bulk GUE into mesoscopic statistics + arithmetic factor C_2

## Programme graph edges
- **BGS:** GUE pair correlation (Link 5) constrains prime gap distribution
- **RH (Paper 13):** zero spacing via explicit formula controls gap statistics
- **GRH (Paper 13b):** GRH + Elliott-Halberstam -> gaps <= 6
