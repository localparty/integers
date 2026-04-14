# PROOF-CHAIN -- Navier-Stokes Existence and Smoothness (Paper 30)

*Global existence and smoothness of 3D incompressible NS via KK spectral gap + gradient-flow transfer from YM. Conditional on KK-to-NS transfer (Paper 8 infrastructure).*
*Status: 2/8 links proved | Confidence: 2/10*

## Chain table

| Link | Statement | Status | Depends on |
|---|---|---|---|
| 1 | KK reduction: 5D Einstein on M^4 x S^1 -> 4D Einstein + Maxwell + scalar | LITERATURE | -- |
| 2 | Fluid/gravity dictionary: T_{mu nu} in Landau frame -> incompressible NS | CONJECTURED | 1 |
| 3 | Gradient-flow transfer: YM well-posedness (Paper 8 L15-17) -> NS velocity field | OPEN | 2 |
| 4 | KK spectral gap Delta_0^KK > 0 (inherits from Paper 8 Thm 4) | PROVED | -- |
| 5 | BKM criterion: spectral gap -> vorticity control -> int_0^T ||omega||_inf < inf | OPEN (THE WALL) | 3, 4 |
| 6 | Energy descent: 5D KK conservation -> 4D NS dissipation -> Leray-Hopf | CONJECTURED | 5 |
| 7 | Uniqueness: Galerkin + energy methods, conditional on regularity | CONDITIONAL | 5 |
| 8 | Global regularity: composition of Links 3-7 | OPEN | 3-7 |

## Current wall
**Link 5 (BKM criterion).** Converting the spectral gap's frequency-space control to pointwise vorticity bounds requires Sobolev embedding + nonlinear estimates on the stretching term omega . nabla u. The stretching term has no sign and no obvious spectral gap control.

## Programme graph edges
- **YM (Paper 8):** gradient-flow machinery (Links 15-17) is the structural source for Link 3
- **QG5D (Paper 1):** KK reduction provides the 5D-to-4D pipeline (Link 1)
