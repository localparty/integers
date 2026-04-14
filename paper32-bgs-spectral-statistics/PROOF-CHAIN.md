# PROOF-CHAIN -- Berry-Tabor / BGS Conjecture

*The non-trivial zeros of zeta exhibit GUE pair-correlation statistics, derived from the type III_1 structure of the BC algebra at KMS_1 via ergodic modular flow + unitary symmetry class.*
*Status: 2/7 links closed | Confidence: 2/10*

## Chain table

| Link | Statement | Status | Depends on |
|---|---|---|---|
| 1 | BC at KMS_1 is type III_1 factor (Araki-Woods, lambda_p = 1/p) | KNOWN | -- |
| 2 | Modular flow sigma_t is ergodic on BC algebra | OPEN | 1 |
| 3 | Ergodic flow -> absolutely continuous spectral measure (SNAG theorem) | OPEN | 2 |
| 4 | AC measure + unitary symmetry class (T-reversal broken) -> level repulsion | OPEN | 3 |
| 5 | Level repulsion in unitary class -> GUE pair correlation: 1-(sin(pi s)/(pi s))^2 | OPEN | 4 |
| 6 | spec(D_inf) = {gamma_n} -> GUE for Riemann zeros | CONDITIONAL on Paper 13 | 5 |
| 7 | Montgomery-Odlyzko numerical confirmation (10^22 zeros) | KNOWN | -- |

## Current wall
**Link 2 (ergodicity of modular flow).** Type III_1 gives Sd(M)=R (full Connes spectrum), so the flow of weights is ergodic. Transferring to sigma_t on the BC algebra specifically requires verifying central ergodicity (automatic for type III_1 with separable predual -- need to verify separability of predual for BC at KMS_1).

## Programme graph edges
- **RH (Paper 13):** Link 6 conditional on spectral realization spec(D_inf) = {gamma_n}
- **QG5D (Paper 1):** GUE statistics = quantum chaos of the 5D geometry
- **Twin Primes:** GUE pair correlation at close spacing constrains prime gap distribution
