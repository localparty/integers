# A1.01 — The Operators D_N

## Question

How are the D_N defined on E_N^+? Is the restriction to the even
sector standard in CCM's framework, or is it a modification
introduced by Paper 13?

## Finding

The operators are constructed by CCM (arXiv:2511.22755) on the
full Sonin space E_N, with the T-inner product obtained after
quotienting by the kernel of T = QW_λ^N − ε_N·Id. The even-sector
restriction E_N^+ is a **modification introduced by Paper 13**
(Section 12 and Appendix A.6), not CCM.

CCM's Theorem 5.10 has as hypothesis: *the minimum eigenvalue
ε_N is (i) simple and (ii) even* ("even-simple"). Paper 13 notes
(Sec 12.4, research/21) that in the full (even+odd) sector, the
minimum eigenvalue alternates between even and odd parity with an
even–odd gap of O(10^{−7}) — so the even-simple hypothesis does
not hold unconditionally on the full sector. Paper 13's resolution
is to **impose the even-sector restriction from the outset**: do
all constructions on E_N^+, not on E_N.

## Is the even-sector restriction "clean"?

The paper claims (Sec 12.4):

> "CCM's construction preserves the γ-symmetry, so the restriction
> is clean: the T-inner product, the rank-one perturbation
> D' = D − |D*ξ⟩⟨η|, and the quotient by the radical all restrict
> naturally to the even sector. Theorem 5.10 applies to the
> restricted operators without modification."

This assertion is **plausible but not verified in the paper**. What
needs to hold:

1. The parity involution 𝒫 commutes with QW_λ^N (so E_N^+ is a
   QW_λ^N-invariant subspace). Paper 13 does not prove this, but it
   is natural given that QW_λ^N is constructed from the Weil
   distribution, which is even in its argument.

2. The minimum eigenvector ξ of QW_λ^N on E_N^+ is in E_N^+ (trivial
   if (1) holds).

3. The radical ℂ·ξ is a subspace of E_N^+, so the quotient
   H = E_N^+ / ℂ·ξ is well-defined. If ξ ∈ E_N^+ (from (2)), OK.

4. The rank-one perturbation |D*ξ⟩⟨η| restricts to E_N^+. This
   requires η ∈ E_N^+ (or at least its E_N^+ component is used). The
   Dirichlet kernel η = (1/√L) Σ_j V_j — whether this is even
   depends on the basis conventions and on whether the sum is over
   symmetric indices. Paper 13 **does not address this**.

5. Theorem 5.10(iii) continues to hold on E_N^+: the zeros of the
   restricted ξ̂_λ coincide with spec(D') on H ∩ E_N^+. This is a
   claim about the even-sector analogue of CCM's identification
   theorem, and it is **not obviously a consequence** of the full-
   sector theorem.

## Independent verification note (research/43)

Appendix A.7 cites an "adversarial verification" of CCM (research/43)
claiming "self-adjointness of D' in T-inner product: SOUND" and
"Eigenvalue identification (Theorem 5.10(iii)): SOUND (exact at
fixed λ, N)". But this is Paper 13's *own* reading of CCM, not an
independent assessment, and the listed caveats include:

- "δ_N(ξ) ≠ 0 ASSERTED, not proved (severity: LOW)"
- "Numerical precision 10^{−55} PLAUSIBLE, not independently verified"

The first caveat is nontrivial. "δ_N(ξ) ≠ 0" is the non-vanishing
of a functional on the ground eigenvector, which is needed to
avoid a degeneracy in the rank-one perturbation. Asserting it
without proof is a live gap.

## Verdict on this subpoint

**Weakened.** The even-sector restriction is a non-trivial
modification of CCM, not merely a notational convenience. Paper 13
asserts that CCM's Theorem 5.10 continues to apply after restriction,
but does not prove the required compatibility (parity commutation
with QW_λ^N, evenness of the Dirichlet kernel component used in
the rank-one perturbation, and the even-sector analogue of the
identification theorem). A refereeable version must either:

(a) Cite a result in CCM that explicitly covers the even sector, or

(b) Provide a self-contained proof that the restriction preserves
    all three CCM ingredients (Theorems 4.2, 5.10, Lemma 7.3).

Currently neither is done.
