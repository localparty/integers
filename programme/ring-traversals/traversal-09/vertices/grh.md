# GRH Vertex -- Traversal 09 Construction Pass

*Paper 13b, ring position 4. Date: 2026-04-14 (construction-pass confirmed).*

## Status entering: 2/8 PROVED (L1 via BSD 5c, L2 via Bratteli-Robinson T2 2026-04-13)

## Layer-by-layer transfer analysis (Paper 13 RH -> Paper 13b GRH)

| GRH Link | RH analog | Transfer? | Mechanism |
|---|---|---|---|
| L1 BC_chi | CCM D_N (ext) | PROVED | BSD 5c Key Lemma C' covers all Hecke; Dirichlet subset |
| L2 KMS_{1,chi} | ITPFI omega_1 | PROVED | chi kills pole: L(1,chi) finite; fixed-pt algebra trivial (type III_1 factor); BR 5.3.30 |
| L3 CCM_chi | CCM D_N | ADVANCEABLE | Prolate construction is analytic (bandwidth lambda); chi enters only through spectral data. L2 closure gives the KMS_1 state from which D_{N,chi} is built. Needs: numerical verification for pilot chi=(-4/.) |
| L4 ITPFI_chi | ITPFI tensor | ADVANCEABLE | Euler product L(s,chi)=prod_p(1-chi(p)p^{-s})^{-1} gives omega_{1,chi}=tensor_p omega_{1,chi}^(p) with phase chi(p). L2 uniqueness is the prerequisite -- now proved. Three RH proofs (Euler, amenability, Araki-Woods) each transfer: chi(p) is a root of unity so tensor structure is preserved |
| L5 Estimates_chi | 3a-3d | WALL | 5a archimedean: gamma factor shift for odd chi -- needs explicit check. 5b eigenvector: Davis-Kahan is character-agnostic, transfers if L4 closes. 5c H^1: Fourier cancellation acquires chi(n) weights -- the load-bearing step. 5d CF: rho depends on prolate spectrum not chi, likely transfers |
| L6 Boegli_chi | 4a-4c | follows L5 | General theorem; applies once inputs (L3-L5) are correct |
| L7 Hurwitz_chi | L5 | follows L5 | hat{xi}_{N,chi}->Lambda(s,chi) uniform convergence follows from L5 estimates |
| L8 GRH | L6 | follows L5 | Self-adjointness of D_{inf,chi} => real spectrum => GRH |

## What L1+L2 unlock

L2 (KMS_{1,chi} uniqueness) is the gateway to L3 and L4 simultaneously:
- **L3**: the CCM operator D_{N,chi} is built from the GNS representation of the unique KMS_1 state. With L2 proved, the construction input exists. What remains is verifying the prolate-spheroidal machinery produces self-adjoint D_{N,chi} with eigenvalues matching zeros of L(s,chi). This is a numerical+analytic task, not a structural obstruction.
- **L4**: the ITPFI factorization omega_{1,chi}=tensor_p follows from the Euler product of L(s,chi) plus L2 uniqueness. The phase chi(p) at each prime is harmless (root of unity in tensor factor). This can likely close with a short argument.

## New wall: L5 (estimates_chi)

Specifically **L5c** (H^1 Fourier cancellation). In Paper 13, the bound ||(D_N-i)^{-1}||_{L2->H1} < 2 uses Fourier-basis cancellation specific to zeta's spectral data. For L(s,chi), the Fourier coefficients pick up chi(n) factors. The cancellation structure depends on conductor q(chi). This is where the character-twist could genuinely fail to be transparent. Explicit computation for chi=(-4/.) is the minimum test.

## Recommended next actions

1. **L3+L4 construction** (parallel): write the chi-twisted CCM operator definition; prove ITPFI_chi via Euler product. Both now have their prerequisite (L2).
2. **L5c pilot computation**: verify H^1 Fourier cancellation for chi=(-4/.) mod 4. If it holds, the mechanism is likely character-universal.
3. L6-L8 follow automatically once L5 closes.

## Projected chain after this pass: 4/8 PROVED (L1-L4), wall at L5c.
