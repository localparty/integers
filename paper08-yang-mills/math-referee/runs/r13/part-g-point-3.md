## Part G, Point 3: N-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: the proof works uniformly for all SU(N), N >= 2.

**(a) N-dependent constants.** The I.3 supplement systematically tracks all N-dependent constants through the proof chain. The critical ones:

| Constant | N-scaling | Direction | Impact |
|----------|-----------|-----------|--------|
| Spectral gap mu_1 | ~ 2N/r_3^2 | Favorable | Increases with N |
| KK mass m_1 | ~ sqrt(2N)/r_3 | Favorable | Increases with N |
| Bond constant C_0 | ~ O(N^{N-1}) | Unfavorable | Absorbed by e^{-m_1 a} |
| Analyticity radius rho | ~ O(1/N^2) | Unfavorable | Positive for each N |
| Spectral lemma C_p | ~ exp(C_1 R_0^3 N^2) | Unfavorable | Finite for each N |
| Gronwall exponent gamma | ~ N | Unfavorable | Absorbed by 4^{-k} |
| Combes-Thomas zeta | ~ exp(C N^2) | Unfavorable | Finite for each N |

All constants are FINITE for each fixed N >= 2. The unfavorable scalings (C_0 ~ N^{N-1}, C_p ~ exp(N^2), etc.) are enormous for large N but are overwhelmed by the doubly exponential convergence factor 4^{-k} in the RG sum.

The convergence of Sum C_k g_k^4 hat{Delta}_k^2 is guaranteed by the ratio test: a_{k+1}/a_k -> 1/4 < 1, independent of N (Lemma I.3.1). The factor 1/4 comes from the kinematic doubling of the lattice spacing, which is universal (N-independent). No N-dependence can spoil this convergence.

**(b) SU(2) special properties.** For N = 2:
  - d^{abc} = 0: the cubic Casimir vanishes, so Tr(F^3) = 0 identically (not just C-odd).
  - CP^1 = S^2: round sphere with simpler geometry.
  - Exact area law sigma = 3g^2/8 from Peter-Weyl theorem.

The paper provides an independent proof for SU(2) using exact solvability of 2D Yang-Mills on S^2. This serves as a consistency check.

The general argument (for N >= 3) does NOT use any SU(2)-specific property:
  - The C-elimination of Tr(F^3) works for all N >= 2 (C-odd for N >= 3, identically zero for N = 2).
  - The Weitzenbock bound mu_1 >= 2N/r_3^2 works for all N >= 2.
  - The cluster expansion convergence works for all N (with N-dependent constants).
  - The Feshbach projection works for all N.
  - The Balaban RG works for all N.

**(c) Error compounding.** The proof chain has ~14 steps (as listed in PROOF-CHAIN IV.1). Each step has bounds with N-dependent constants. The accumulated error:

  Product_{steps} C_step(N) ~ N^{O(N^2)} (very rough upper bound)

This is enormous for large N but FINITE for each fixed N. The Clay prize requires the proof to work for each fixed N — there is no requirement for large-N uniformity or large-N asymptotics.

The I.3 supplement tracks the N-dependence through all 14 steps and confirms finiteness at each step. The critical convergence factor (1/4 per RG step) is N-independent, which ensures the RG sum converges regardless of the N-dependent prefactors.

For the extension to other groups (SO, Sp, exceptional), the same analysis applies with group-specific constants replacing the N-dependent ones. Appendix I.4 verifies that all constants are finite for each group.

No error found. The proof works for each fixed N (and each fixed compact simple group), with N-dependent but finite constants throughout.

**Impact on the claimed result:** None. The N-dependence is tracked systematically and does not affect the validity of the proof for any fixed N.
