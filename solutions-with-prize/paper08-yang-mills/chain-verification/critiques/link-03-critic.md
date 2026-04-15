# PCA Critique: Link 3 — Polymer convergence with κ k-independent

**Run:** YM Verification Cascade  
**Date:** 2026-04-13  
**Critic role:** Adversarial (attempt to BREAK)  
**Target:** Link 3 — Balaban CMP 109, Theorem 1 (detailed Theorem 3): polymer activities satisfy |K_k(X,V)| ≤ e^{−κ|X|} with κ > 0 independent of k.  
**Primary sources read:** H-balaban-analyticity.md, K-balaban-general-groups.md, PROOF-CHAIN.md IV.1/IV.3

---

## Attack 1: κ conflation (polymer convergence radius vs. block-spin compression factor)

**Vector:** If the same symbol κ is used for both the block-spin compression factor (from the block-averaging step, fixed by lattice geometry L=2) and the polymer cluster convergence rate (from the Kotecky–Preiss criterion), conflating them would make the k-independence claim circular or false.

**Finding:** Appendix K.5 explicitly separates these. The polymer decay constant κ(G) is derived from a non-circular formula:

$$\kappa(G) = \kappa_0 - C_1 \cdot d_G \cdot \ln\!\bigl(\max(4d\,d_G/m_W^2,\, 2)\bigr)$$

where ρ₀(G) = min(m_W²/4dd_G, 1/2) is defined entirely without reference to κ (using only the propagator radius from K.2 and the projection radius from K.3). The block-spin compression geometry (L=2, axial gauge, K.7) is a separate construction with no κ dependence. No conflation occurs.

**Verdict on Attack 1:** FAILS TO BREAK. The two quantities are cleanly separated and the formula for κ(G) is non-circular.

---

## Attack 2: Mayer resummation — uniform convergence in k

**Vector:** The Weierstrass-convergence step in the Mayer expansion might require k-dependent damping (e.g., a factor growing with k to suppress large polymers), invalidating uniform convergence.

**Finding:** K.5 step (iii) gives the inductive net decay rate after one RG step:

$$\kappa_{k+1} = \kappa_k - c_1 d_G - c_2 d_G e^{-2\delta_0} - c_3 d_G e^{-\kappa_0}$$

Every degradation term (c₁d_G, c₂d_G e^{−2δ₀}, c₃d_G e^{−κ₀}) depends only on d_G, δ₀, and κ₀ — none of which change with k. Balaban's construction chooses m_W large enough that the total degradation δκ < κ₀/2, so κ(G) = κ₀ − δκ > κ₀/2 > 0 at every step. The Kotecky–Preiss criterion is satisfied uniformly in k with no k-dependent damping required.

**Verdict on Attack 2:** FAILS TO BREAK. The degradation per step is a k-independent constant, and the decay rate stabilizes above κ₀/2.

---

## Attack 3: g* k-independence — does the convergence radius shrink with scale?

**Vector:** If the convergence threshold g* for |g| < g* were scale-dependent (e.g., g* ~ 1/k), the polymer expansion would fail at sufficiently large k.

**Finding:** The small-field condition is p(g_k) = g_k^{1−ε} with fixed ε ∈ (0, 1/2). Since g_k → 0 under asymptotic freedom (K.6, b₀(G) > 0 for all compact simple G), the threshold p(g_k) → 0, meaning the small-field region Ω_s *expands* at later RG steps, making polymer convergence easier rather than harder. The convergence parameter κ(G) is set at the outset by the choice of m_W (K.5, explicit lower bound m_W² > 4dd_G e^{κ₀/(C₁d_G)}) and does not depend on k or g_k. The preprint uses ε* = 0.49, confirmed to be strictly inside the convergence window ε < 1/2 of CMP 119 Sec. 2.

**Verdict on Attack 3:** FAILS TO BREAK. g* is effectively m_W-dependent and k-independent; the small-field region expands rather than contracts.

---

## Attack 4: Minimum of controlling parameters (κ, m_W, C_D, r_proj) — could one shrink?

**Vector:** PROOF-CHAIN IV.3 item 1 lists four controlling parameters. If any one degrades with k, the minimum ρ(G) = min(...) could approach zero.

**Finding:** K.8 gives the explicit formula:

$$\rho(G) = \min\!\left(\frac{\kappa(G)}{2d},\; \frac{m_W^2}{4d\,d_G},\; r_{\mathrm{proj}}(G)\right)$$

Each component is verified k-independent:
- κ(G)/(2d): polymer decay constant, k-independent by K.5 induction proof.
- m_W²/(4dd_G): propagator analyticity radius (K.2), k-independent because m_W·a_k is held fixed through the RG (the lattice spacing a_k scales with the RG step, keeping the dimensionless product constant).
- r_proj(G) ≥ 1/2: projection analyticity (K.3), defined geometrically as nearest point on G, carries no k dependence whatsoever.

C_D = d_G/m_W² from K.2 enters the inductive step but not the final radius formula; it appears in the degradation δκ and is bounded by a k-independent constant. The minimum of three k-independent positive quantities is positive and k-independent.

**One residual concern (WEAKENED, not BROKEN):** The formula m_W·a_k = const requires that the physical fluctuation mass m_W tracks the lattice scale exactly through all RG steps. This is Balaban's inductive hypothesis (H2) in K.5. The proof closes this inductively, but the closing argument (K.5, "closing the induction") notes that the prefactor C_D ≤ c₀d_G enters the saddle-point Lipschitz constant, giving a degradation of order c₁d_G per step in κ. For large N (SU(N) with large N), d_G = N²−1 grows, so the required initial κ₀ must scale at least as O(d_G) = O(N²). Balaban's CMP 109 is for SU(2) (d_G = 3); the extension in Appendix K is carried out for general G with explicit N-dependence, but for large N the required m_W grows as O(N²) and the resulting analyticity radius ρ(G) ~ m_W²/(4dd_G) ~ O(1) remains bounded away from zero only if m_W is taken O(N). This is a large-N subtlety not explicitly discussed in K.8, but it does not affect k-independence for any fixed G.

**Verdict on Attack 4:** FAILS TO BREAK for any fixed G. A minor note (not a gap) is that the explicit N-scaling of the required m_W for large-N SU(N) could be stated more precisely in K.8.

---

## Attack 5: Dimock 2013 — scalar analogue versus SU(N) gauge case

**Vector:** If Dimock's scalar φ⁴ result (arXiv:1212.5562, d=3) is cited as the primary support for analyticity in Link 3, the gap to SU(N) gauge theory in d=4 is unbridged. Scalar φ⁴ has no gauge invariance, no projection onto G, no block-spin kernel, and works in a lower dimension.

**Finding:** Dimock is cited as a "modern exposition" and supplementary illustration (H-balaban-analyticity.md, Sec. 2.5; PROOF-CHAIN IV.2). The load-bearing sources for Link 3 are Balaban CMP 109 Thm 1/3 and CMP 119 directly. Dimock's contribution is: (i) providing an explicit statement of analyticity radius in a simpler setting where Balaban leaves it implicit, and (ii) confirming that the analyticity mechanism (iterated Gaussian integration with polynomial interactions) is the same. Appendix K.2–K.9 carries the SU(N) case independently, without appeal to Dimock for anything essential. IV.3 confirms: "Dimock (arXiv:1108.1335, 2011, Thm 14) provides an explicit statement in the scalar analogue" — used only to guide the reader, not as a proof step.

**One genuine weakness (WEAKENED):** Section 5.2 of H-balaban-analyticity.md says "(B1) and (B2) are stated results in Balaban's CMP 109 (1987)" and the honest assessment in Sec. 5.3 corrects this: they are *consequences* of Balaban's stated results, not stated results themselves. This overclaim in the body text (relative to the verification appendix) is a presentation error that a referee would flag. It does not affect the mathematical validity.

**Verdict on Attack 5:** FAILS TO BREAK. Dimock is not load-bearing. The SU(N) case is handled in Appendix K. However, the body text description "(B1)-(B2) are stated results in CMP 109" should be corrected to "consequences of CMP 109" consistent with H Sec. 5.3.

---

## Summary of Attacks

| Attack | Target | Verdict |
|:-------|:-------|:--------|
| 1: κ conflation | Two uses of κ | FAILS TO BREAK — cleanly separated in K.5 |
| 2: Mayer resummation uniformity | k-dependent damping | FAILS TO BREAK — degradation k-independent |
| 3: g* k-independence | Convergence radius shrinks | FAILS TO BREAK — small-field region expands |
| 4: Minimum of controlling parameters | Any one could shrink | FAILS TO BREAK (WEAKENED: N-scaling note) |
| 5: Dimock scalar analogue | SU(N) gap | FAILS TO BREAK (WEAKENED: body text overclaim) |

---

## Overall Verdict

**SURVIVED.**

Link 3 — polymer convergence with κ k-independent — withstands all five attack vectors. The k-independence of κ is established by an explicit, non-circular inductive argument in Appendix K.5 with the closing inequality κ(G) > κ₀/2 > 0. Each controlling parameter (κ, m_W, C_D, r_proj) is independently verified k-independent in K.2–K.5. No attack succeeds in breaking the link.

Two weaknesses are noted (WEAKENED, not BROKEN):

1. **N-scaling note (Attack 4):** For large-N SU(N), the required initial m_W scales as O(N). This is implicit in K.5 but not stated explicitly in K.8. For any fixed N this is a non-issue; for the N→∞ limit it would need separate treatment.

2. **Body text overclaim (Attack 5):** The formulation "(B1)-(B2) are stated results in Balaban CMP 109" in the body is stronger than what the papers contain. The verification appendix (H, Sec. 5.3) correctly characterizes them as *consequences*; the body text should be updated to match.

Neither weakness constitutes a mathematical gap. Link 3 is sound.
