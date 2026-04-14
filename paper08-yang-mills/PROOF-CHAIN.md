# PROOF-CHAIN -- Yang-Mills Mass Gap (Paper 8)

*Delta_infinity > 0 for 4D SU(N) YM via KK spectral gap + Balaban RG + gradient-flow OS reconstruction. Unconditional through Link 17; Link 18 conditional on H4.*
*Status: 17/18 PROVED, 1 CONDITIONAL | Confidence: 9/10*

## Chain table

| Link | Statement | Status | Depends on |
|---|---|---|---|
| 1 | Delta_0^KK > 0 (Thm 4, Weitzenbock + cluster expansion) | PROVED | -- |
| 1b | Delta_0^std > 0 (IR equivalence via reduced transfer matrix, Thm 5) | PROVED | 1 |
| 2 | UV stability | LITERATURE (CMP 109, 119) | -- |
| 3 | Polymer convergence, kappa k-independent | LITERATURE (CMP 109) | -- |
| 4 | (B1): analyticity, k-independent radius | PROVED | 2, 3 |
| 5 | (B2): SL(N,C) extension | PROVED | 4 |
| 6 | C-elimination of Tr(F^3) | PROVED | -- |
| 7 | Newton decomposition: n >= 2 survives | PROVED | 6 |
| 8 | dev(Tr(DF)^2) >= 2 | PROVED | 7 |
| 9 | Dim-6 classification: all ops have dev >= 2 | PROVED | 8 |
| 10 | dev(delta E_k^{d=6}) >= 2 non-perturbatively | PROVED | 4, 5, 9 |
| 10b | Spectral lemma constant C_p k-independent | PROVED | 10 |
| 11 | C_new g_k^4 Delta-hat^2 bound | PROVED | 10, 10b |
| 12 | RG recursion: C_{k+1} = C_k/4 + C_new | PROVED | 11 |
| 13 | Sum C_k g_k^4 Delta-hat_k^2 < infinity | PROVED | 12 |
| 14 | Delta_infinity > 0 | PROVED | 1b, 13 |
| 15 | Gradient-flow: well-posedness, contractivity (Lemmas 1.1-1.5) | PROVED | 14 |
| 16 | Continuum Schwinger functions: OS0-OS4 at fixed t>0 | PROVED | 15 |
| 17 | [Tr F^2]_R as operator-valued distribution; T_{mu nu}^R constructed | PROVED | 16 |
| 18 | AF match (L.2), leading-order OPE (L.4) | CONDITIONAL on H4 | 17 |

## Current wall
**H4** (Hypothesis 4): non-perturbative Schwinger functions agree with perturbation theory at short distances. Link 18 (AF match + OPE) is conditional on H4. Links 1-17 are unconditional.

## Programme graph edges
- **QG5D (Paper 1):** KK spectral gap (Link 1) inherits from e-circle compactification
- **RH (Paper 13):** AF coefficient connects to zeta spectral data
- **NS (Paper 30):** gradient-flow machinery (Links 15-17) structural parallel for NS regularity
- **Hodge (Paper 29):** gauge anomaly cancellation is a K-theoretic / Hodge-class statement
- **Baum-Connes:** anomaly cancellation = index(D_A) = 0, a K-theory pairing
