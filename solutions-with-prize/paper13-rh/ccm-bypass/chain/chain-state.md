# Chain State — RH Layer 1 CCM Bypass (FINAL)

*Updated after Wave 1 completion. Programme exiting at Tier 2.*

| Link | Statement | Domain | Status | Confidence | Blocker | Last wave |
|---|---|---|---|---|---|---|
| L1 | Self-adjoint D_N on E_N^+ with eigenvalues → {γ_n}, H¹ bounds, KMS₁ compatible | SPEC / OA | CONDITIONAL (CCM) | 8/10 | CCM 2025 not peer-reviewed | W1 |
| L1-bypass | Alternative Layer 1 delivering items (1)-(4) to Layer 2 without CCM | ALL | **HONEST-STALL** | 2/10 | Hilbert-Pólya: no known spectral realization independent of CCM | W1 |
| L2 | ITPFI factorization ω₁ = ⊗_p ω₁^(p) | OA | VERIFIED | 9/10 | — | Prior |
| L3 | Four estimates (archimedean, eigenvector, H¹, CF) | SPEC | VERIFIED | 9/10 | — | Prior |
| L4 | Teschl gsrc + Bögli spectral exactness | SPEC | VERIFIED | 9/10 | — | Prior |
| L5 | Hurwitz zero convergence | ANT | VERIFIED | 9/10 | — | Prior |
| L6 | spec(D_∞) = {γ_n} ⊂ ℝ → RH | SPEC | VERIFIED | 9/10 | Conditional on L1 | Prior |

## L1-bypass decomposition (Wave 1 results)

| Item | Requirement | Best result | Cell | Status |
|---|---|---|---|---|
| L1.1 | Self-adjoint D_N on E_N^+ → D_∞ in gsrc | Berry-Keating xp: SA on L²(ℝ₊), strong resolvent convergence | W1-MI | PARTIAL (different Hilbert space than E_N^+) |
| L1.2 | Eigenvalues → {γ_n} | No construction achieves this without CCM or assuming RH | ALL 5 | **BLOCKED** (Hilbert-Pólya wall) |
| L1.3 | Uniform H¹ bounds | Berry-Keating xp: graph-norm H¹ bounds, uniform in N | W1-MI | PARTIAL (graph norm, not Sobolev H¹) |
| L1.4 | KMS₁ state structure on BC algebra | BC 1995 → GNS → type III₁ → ITPFI | W1-OA | **VIABLE** (independent of CCM) |

## Named wall

**The Hilbert-Pólya wall.** Every attempt to identify Riemann zeros as eigenvalues of a self-adjoint operator on a Hilbert space either:
(a) Uses CCM's prolate-operator/CF construction (the only one producing a family D_N),
(b) Is conditional on RH (Yakaboylu W≥0, Berry-Keating with Weil positivity),
(c) Is circular (LeClair: S-matrix defined from ξ-function),
(d) Works in the wrong space (Meyer: nuclear Fréchet, not Hilbert), or
(e) Produces a twisted spectral triple incompatible with Bögli (type III sigma).

## Verdict: CHAIN CONDITIONAL (CCM load-bearing)

The chain remains conditional on CCM 2025. Phase 2 proceeds with CCM verification as mandatory critical path.
