# B3.03 — Galerkin Projection

## Question

The proof routes through Galerkin projection P_N: E_∞ → E_N^+.
Is this compatible with CCM's T-inner-product structure? Does
projection commute with the relevant operations?

## The Galerkin setup

Paper 13 Def 9.2: P_N is the orthogonal projection onto
E_N^+ = span{V_0, V_2, ..., V_{2N}} (cosine basis). The "base
form" Q_0 is defined as the Galerkin limit:

  Q_0 := lim_{N → ∞} P_N QW_λ^{N,+} P_N.

## Compatibility concerns

1. **Which inner product?** E_N^+ carries two natural inner
   products: the ordinary L² inner product on [λ^{−1}, λ] (in which
   the cosine basis is orthonormal), and the T-inner product
   ⟨f|g⟩_T = ⟨Tf|g⟩ in which CCM's D' is self-adjoint.

   The orthogonal projection P_N is with respect to which one?

   If P_N is L²-orthogonal, then P_N QW_λ^{N,+} P_N is an ordinary
   L² quadratic form, and the Galerkin limit Q_0 is a limit of
   L²-based forms. Then the self-adjoint operator associated to
   Q_0 via Friedrichs is an L²-self-adjoint operator, not a
   T-self-adjoint one.

   If P_N is T-orthogonal (but T depends on N — different at each
   level), then it is not clear what "Galerkin projection" even
   means as the Hilbert space itself changes.

   Paper 13 does not disambiguate.

2. **Does P_N commute with the rank-one perturbation?** The CCM
   perturbation |D*ξ⟩⟨η| has ξ depending on N (minimum eigenvector
   of QW_λ^{N,+}). The perturbation vector at level N is naturally
   in E_N^+. But under the Galerkin projection P_{N'} for N' > N,
   the perturbation at level N restricted to a larger space
   becomes... what?

3. **The limit form Q_0 vs the "true" limiting form.** Section
   9.2 defines Q_0 as the Galerkin limit of the bare Weil form
   (without rank-one perturbation), then adds the perturbation
   via δ_N. But the bare Weil form's Galerkin limit may not be
   the "correct" limiting object — the physical limit includes
   the perturbation that makes D self-adjoint in the T-inner
   product. Separating the "base" and "perturbation" parts is a
   choice, and whether the resulting Q_0 corresponds to a
   meaningful self-adjoint operator is unclear.

## What Paper 13 says

Section 9.2: "The base form Q_0 is closed and semibounded by
standard Galerkin theory (Reed–Simon I, Theorem VIII.7): the
Galerkin limit of closed semibounded forms on an exhausting
sequence of subspaces (the even Chebyshev system {V_{2k}} is
complete in L²([0, L])) is closed and semibounded."

This invokes a Reed–Simon result about Galerkin limits of
semibounded forms. Reed–Simon I Theorem VIII.7 (if I remember
correctly, my recall is not certain) is about strong resolvent
convergence under increasing sequences of forms. The invocation
is plausible but not precisely matched to the situation at hand.

## Verdict on this subpoint

**Weakened.** The Galerkin picture is hand-wavy:
- The choice of inner product (L² vs T) is not disambiguated.
- The interaction between the Galerkin projection and CCM's
  rank-one perturbation is not tracked.
- The "base form Q_0" is a specific algebraic construction but
  its physical meaning (what self-adjoint operator does it
  correspond to?) is not discussed.

**Required fix:** Explicitly state which inner product defines
the Galerkin projection, which space the Friedrichs extension
lives on, and why this matches the CCM operators D_N. A clean
statement would reconcile the T-inner-product framework of CCM
with the L²-Galerkin framework of the convergence argument.
