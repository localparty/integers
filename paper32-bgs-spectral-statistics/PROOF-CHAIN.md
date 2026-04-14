# PROOF-CHAIN -- Berry-Tabor / BGS Conjecture (Paper 32)

*The non-trivial zeros of zeta exhibit GUE pair-correlation statistics, derived from the type III_1 structure of the BC algebra at KMS_1 via ergodic modular flow + unitary symmetry class.*
*Status: 2/7 links closed | Confidence: 3/10 (upgraded from 2/10 due to Nov 2025 Hardy Z result)*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | BC at KMS_1 -> type III_1 factor | KNOWN | -- | Connes classification (Araki-Woods, lambda_p = 1/p) |
| 2 | Modular flow sigma_t is ergodic on BC algebra | OPEN | 1 | **2024: dynamical systems analysis bridges Montgomery PCC to quantum chaos (arXiv:2406.12852)** |
| 3 | Ergodic flow -> absolutely continuous spectral measure | CONJECTURED | 2 | Standard ergodic theory (SNAG theorem) |
| 4 | AC measure + unitary class -> level repulsion | CONJECTURED | 3 | Random matrix theory (T-reversal broken) |
| 5 | Level repulsion -> GUE pair correlation | CONJECTURED | 4 | **Nov 2025: Montgomery PCC PROVED for Hardy Z-function zeros (arXiv:2511.18275) -- Dyson Brownian motion equivalence + GUE sine-kernel convergence PROVED assuming RH** |
| 6 | GUE for BC eigenvalues = GUE for Riemann zeros | CONDITIONAL on Paper 13 | 5 | Spectral realization spec(D_inf) = {gamma_n} |
| 7 | Montgomery-Odlyzko numerical confirmation (10^22 zeros) | KNOWN | -- | Odlyzko 1987 |

## Current wall
**Link 2 (ergodicity of modular flow).** Type III_1 gives Sd(M) = R (full Connes spectrum), so flow of weights is ergodic. Transferring to sigma_t on the BC algebra specifically requires verifying central ergodicity (automatic for type III_1 with separable predual -- need to verify separability for BC at KMS_1).

**CRITICAL UPGRADE (Nov 2025):** The Hardy Z-function PCC proof (arXiv:2511.18275) combined with the March 2025 result (100% of zeros simple AND on critical line, conditional on PCC NOT on RH) means: if we prove Link 2 (ergodicity) -> Link 5 now has a concrete published proof -> Link 6 connects to Paper 13 -> the BGS chain is closer to closing than any other extended vertex. The Nov 2025 Hardy Z result is the single strongest lead in the extended programme.

## Programme graph edges
- **RH (paper13-rh):** Link 6 conditional on spectral realization spec(D_inf) = {gamma_n}
- **QG5D (paper1):** GUE statistics = quantum chaos of the 5D geometry
- **Twin Primes (paper34-twin-primes):** GUE pair correlation at close spacing constrains prime gap distribution
- **PvNP (paper28-pvnp):** spectral statistics of modular flow feed computational complexity bounds
- **Baum-Connes (paper31-baum-connes):** K-theoretic constraints on the type III_1 factor
