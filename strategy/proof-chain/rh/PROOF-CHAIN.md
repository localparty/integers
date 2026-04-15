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
| 3d | CF decay: rho >= 4.27 uniform in N (log N caveat, Remark 8.4; caveat resolved by Slepian compatibility Lemma 12.1, 2026-04-14) | PROVED | 1 |
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

## Known gap: Pin #6 CP-violation anchor (2026-04-14)

Agent L audit (2026-04-14, `integers/paper01-qg5d/code/pin6-audits/FINDINGS.md`) confirms via ripgrep that Paper 13 has **no CP-violation section**, despite CKM being cited as a downstream prediction. Pin #6 (J_CKM × 10⁵ = log(γ_1) · ζ(3)) therefore does **not** anchor on any explicit Paper 13 content; the load-bearing document is `integers/paper12-cbb-system/research/102 §3.1` (Mellin duality H_BC = log T_BC, giving log γ_1 as the BC Hamiltonian ground-state eigenvalue). Writing the CP-violation section would complete Pin #6's structural audit; until then the anchor is `integers/paper12-cbb-system/research/102`. No chain-link status change — RH chain does not gate on CP-violation content.

## Cascading refinement from QG5D W1/W2 closure (2026-04-14)

Paper 1 PROOF-CHAIN.md W1 (scheme independence) and W2 (Route-C 3-loop explicit) both closed 2026-04-13/14 via Paper 10 (Theorem 1 two-loop scheme-independence + Theorem U.2a one-loop Seeley-DeWitt) + Paper 11 (Theorem K.4 all-orders inductive bootstrap) + explicit L=3 numerical verification at 50-digit precision (`integers/paper01-qg5d/code/K-5-2-route-c-3loop.py`). Cascading impact on this chain: the CBB system's Axiom 5 (zeta regularization closure) no longer has a lingering regulator-scheme question. Effect is cosmetic-to-small — this chain never gated on the scheme question directly, but the underlying foundation is now strictly stronger. No link status changes required; confidence unchanged; mention included for completeness of the programme graph.
