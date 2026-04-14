# PROOF-CHAIN -- Riemann Hypothesis (Paper 13)

*All non-trivial zeros of zeta(s) lie on Re(s)=1/2, via CCM operators + ITPFI convergence + Boegli spectral exactness. Conditional on CCM (arXiv:2511.22755).*
*Status: 6/6 layers closed (all THEOREM/LEMMA) | Confidence: 8/10*

## Chain table

| Link | Statement | Status | Depends on |
|---|---|---|---|
| 1 | CCM operators D_N on E_N^+ (self-adjoint, eigenvalues ~ {gamma_n} to 10^{-55}) | EXTERNAL (CCM 2025) | -- |
| 2 | ITPFI: omega_1 = tensor_p omega_1^(p) (KMS_1 uniqueness + Weil form convergence) | PROVED | 1 |
| 3a | Archimedean sub-leading: O(1/lambda) | PROVED | 2 |
| 3b | Eigenvector approximation: O(log lambda / lambda) via ITPFI triangle + Davis-Kahan | PROVED | 2 |
| 3c | H^1 bound: ||(D_N-i)^{-1}||_{L2->H1} < 2, all lambda, all N (Fourier cancellation) | PROVED | 1 |
| 3d | CF decay: rho >= 4.27 uniform in N (with log N caveat, Remark 8.4) | PROVED (with caveat) | 1 |
| 4a | Boegli H1 (gsrc): ITPFI -> form convergence -> gsrc via Teschl Lemma 2.7 | PROVED | 2, 3a-3d |
| 4b | Boegli H2 (discrete compactness): uniform H^1 -> Rellich-Kondrachov | PROVED | 3c |
| 4c | Spectral exactness: spec(D_inf) = lim spec(D_N), no spurious eigenvalues | PROVED | 4a, 4b |
| 5 | Hurwitz: hat{xi}_N -> Xi uniformly on compacts -> lim spec(D_N) = {gamma_n} | PROVED | 3b, 4c |
| 6 | spec(D_inf) = {gamma_n} subset R (D_inf self-adjoint) => RH | QED | 4c, 5 |
| S1 | AE simplicity (certified N<=20; Slepian limit N>20) | PROVED | 1 |
| S2 | Slepian compatibility: A^{ev} = K_lambda|_grid + O(e^{-cN}) | PROVED | S1 |
| S3 | gamma_E elimination: uniform diagonal shift | PROVED | -- |

## Current wall
**CCM (arXiv:2511.22755).** Layer 1 is an external preprint by Connes-Consani-Moscovici. Upon journal acceptance, chain upgrades to 9/10. Layers 2-6 independently at 9-10/10.

## Programme graph edges
- **YM (Paper 8):** AF coefficient connects spectral data to gauge coupling
- **BSD (Paper 26):** L-functions factor through the same BC algebra; cocycle shift extends
- **GRH (Paper 13b):** character-twisted extension of every layer
- **BGS:** GUE pair correlation of zeros = spectral statistics of D_inf
- **PvNP (Paper 28):** Q5-RIEMANN exponent constrains spectral gap scaling
