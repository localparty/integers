# B3.01 — Verification of Teschl Lemma 2.7

## The hypothesis of Teschl Lemma 2.7

From Paper 13 Appendix C.2 (paraphrase of Teschl–Wang–Xie–Zhou
2026, Lemma 2.7):

> Let Q_N be a sequence of closed, lower-bounded quadratic forms
> on a Hilbert space 𝐻 with common form domain 𝒟. Suppose:
>
> **(i)** Q_N(f) → Q_∞(f) for all f ∈ 𝒟 (pointwise convergence).
>
> **(ii)** There exist a < 1 and b ≥ 0 such that
> |Q_N(f) − Q_∞(f)| ≤ a · Q_∞(f) + b · ‖f‖²
> for all f ∈ 𝒟 and all N sufficiently large.
>
> Then the Friedrichs extensions D_N converge to D_∞ in gsrc.

Paper 13 claims to satisfy (i) and (ii) with **a = 0**.

## How Paper 13 verifies (i)

Section 4.7, Proposition 4.3: *entry-by-entry convergence of matrix
elements* for f, g in the algebraic direct limit. As discussed in
A2.03, this delivers pointwise convergence on a dense subspace.
The common form domain 𝒟 in Teschl's setup is **not literally the
algebraic direct limit** — it is the form domain of Q_∞. For the
hypothesis to apply, one needs pointwise convergence on 𝒟, or at
least on a core of 𝒟.

If 𝒟 = form-closure of the algebraic direct limit, and the
algebraic direct limit is a form core, then pointwise convergence
on the core plus the relative form bound in (ii) suffices. This
requires verifying that the algebraic direct limit is indeed a
core — which Paper 13 Appendix C.4 asserts via Chebyshev
completeness.

**Sub-concern:** Chebyshev completeness in L²([λ^{−1}, λ]) is
fine. Whether the cosine basis {V_n^+} is a *core* for the
Friedrichs extension of Q_∞ is a stronger property. The paper
does not prove this; it is asserted.

## How Paper 13 verifies (ii) with a = 0

Theorem 9.3 claims:

  |δ_N[f]| = |⟨f, Δ_N f⟩| ≤ ‖Δ_N‖_op · ‖f‖² ≤ C_Δ · ρ_Δ^{−N} · ‖f‖²

which matches hypothesis (ii) with a = 0 and b = C_Δ · ρ_Δ^{−N}.

**But**: the paper defines δ_N := Q_N − P_N Q_0 P_N (Def 9.2),
not δ_N = Q_N − Q_∞. Let me check whether these match.

From Def 9.2:
- Q_0 := lim P_N QW_λ^{N,+} P_N (Galerkin limit, closed and
  semibounded).
- δ_N := Q_N − P_N Q_0 P_N where Q_N includes the rank-one
  perturbation, so δ_N[f] = ⟨f, Δ_N f⟩.

For the Teschl hypothesis, we need |Q_N(f) − Q_∞(f)| ≤ ... with
Q_∞ = limiting form. **Is Q_∞ = Q_0?** Section 9.2 treats them
as different: Q_0 is the Galerkin limit of the base form, while
Q_∞ should be the "full" limit including the rank-one correction.

From Corollary 9.6: "Since b(N) → 0, the limiting form is
Q_∞ = Q_0 + lim δ_N = Q_0 + 0 = Q_0". So in the limit, Q_∞ = Q_0
because the rank-one correction vanishes super-exponentially.

OK so in the limit, Q_∞ = Q_0. And δ_N = Q_N − P_N Q_∞ P_N.

**But the Teschl hypothesis asks for a bound on Q_N − Q_∞**, not on
Q_N − P_N Q_∞ P_N. For f ∈ range(P_N) (i.e., f ∈ E_N^+ embedded
in the limit), P_N f = f, so P_N Q_∞ P_N [f] = Q_∞[f] and the two
definitions agree.

For f ∉ range(P_N), δ_N[f] as defined is zero (since P_N Q_∞ P_N
acts by zero outside range(P_N), and Q_N acts on E_N^+ which is
embedded in range(P_N)). But Q_N − Q_∞ on such f is |Q_∞[f]|,
which is generally not zero.

So **the bound** |Q_N(f) − Q_∞(f)| ≤ 0·Q_∞(f) + C·ρ^{−N}·‖f‖² is
**not established for f outside range(P_N)**. Only for f inside.

This is a real gap. The Teschl hypothesis requires the bound on
the **common form domain** 𝒟, which extends beyond any single
E_N^+. Paper 13 implicitly assumes that E_N^+ grows to fill 𝒟,
and that the bound is only needed on ⋃_N range(P_N). This is
plausible but not explicit.

A charitable reading: since 𝒟 is the form domain of Q_∞ and
⋃_N range(P_N) is dense in 𝒟 (by Chebyshev completeness), one
only needs the bound on the dense subspace, and Teschl's lemma
(in the version for Galerkin approximations) accepts this.

The correct (careful) statement would be: "Teschl Lemma 2.7 with
Galerkin projections". The form bound then reads:

  |Q_N(P_N f) − Q_∞(P_N f)| ≤ a · Q_∞(P_N f) + b · ‖P_N f‖²

and the gsrc conclusion is for the projected operators. This is
technically different from the bare Teschl Lemma 2.7.

## Is Teschl Lemma 2.7 even applicable to Galerkin sequences?

Strictly speaking, Teschl's lemma is for forms *defined on the
same Hilbert space H* — a common domain. Paper 13's Q_N lives
on E_N^+ of **growing dimension**, and the "common domain" only
exists after a Galerkin embedding P_N: E_∞ → E_N^+. Whether the
Teschl lemma as stated in arXiv:2601.10476 covers the
Galerkin-projection case is a question about the Teschl paper
that I cannot answer without reading it.

Paper 13 Appendix C treats it as applicable "directly", but this
requires the Teschl lemma to be robust to Hilbert space
refinement. Without checking Teschl's paper, I cannot confirm.

## Verdict on this subpoint

**Weakened.** The Teschl form bound with a = 0 is the right
*shape* of hypothesis, and the decaying b(N) is correctly stated.
But:

1. The identification δ_N = Q_N − Q_∞ vs δ_N = Q_N − P_N Q_∞ P_N
   is not clearly drawn; the bound is established on range(P_N)
   but Teschl's lemma is stated on the common form domain.

2. Applicability of Teschl Lemma 2.7 to Galerkin approximations
   (varying Hilbert spaces) is not explicitly verified against
   the Teschl paper.

3. The decaying bound ‖Δ_N‖ ≤ C·ρ^{−N} is from research/40 Lemma
   1 and is not included in the preprint.

A rigorous Teschl application would state the Galerkin form of
the lemma, cite it precisely, and check hypothesis (ii) on the
common form domain. Paper 13's Section 9 is a sketch of this
route, not a complete verification.
