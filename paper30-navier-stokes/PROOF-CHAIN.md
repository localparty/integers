# PROOF-CHAIN -- Navier-Stokes Existence and Smoothness (Paper 30)

*Global existence and smoothness of 3D incompressible NS on T^3 via KK spectral gap + gradient-flow transfer from YM. Conditional on KK-to-NS transfer (Paper 8 infrastructure).*
*Status: 2/8 links proved | Confidence: 2/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | 5D Einstein -> KK reduction to 4D Einstein + Maxwell + scalar | LITERATURE | -- | Kaluza 1921, Klein 1926, Paper 1 |
| 2 | T_{mu nu} near-equilibrium -> incompressible NS | CONJECTURED | 1 | BHMR 2008 fluid/gravity |
| 3 | YM gradient-flow transfer (Lemmas 1.1-1.5) -> NS velocity field | OPEN | 2 | Paper 8 Appendix L S.L.1 (same PDE class) |
| 4 | KK spectral gap Delta_0 > 0 controls high-freq modes | PROVED | -- | Paper 8 Theorem 4 (inherited) |
| 5 | BKM criterion: spectral gap -> vorticity bound -> no blowup | OPEN | 3, 4 | **Camlin 2025: bounded vorticity-response functional Phi + Sundman temporal lifting -> BKM finiteness on T^3** |
| 6 | Energy: KK conservation (5D) -> NS dissipation (4D) | CONJECTURED | 5 | Leray 1934, Hopf 1951 |
| 7 | Uniqueness via Galerkin + energy | CONDITIONAL on L5 | 5 | Standard PDE |
| 8 | Global regularity: L3-6 compose | OPEN | 3-7 | Composition |

## Current wall
**Link 5 (BKM criterion).** Converting the spectral gap's frequency-space control to pointwise vorticity bounds requires Sobolev embedding + nonlinear estimates on the stretching term omega . nabla u. The stretching term has no sign and no obvious spectral gap control. **Camlin 2025 provides a concrete published approach**: a bounded vorticity-response functional Phi combined with Sundman temporal lifting yields BKM finiteness on T^3 -- this is the most promising route to adapt.

## Programme graph edges
- **YM (paper08-yang-mills):** gradient-flow machinery (Links L.15-L.17) is the structural source for Link 3
- **QG5D (paper1):** KK reduction provides the 5D-to-4D pipeline (Link 1)
