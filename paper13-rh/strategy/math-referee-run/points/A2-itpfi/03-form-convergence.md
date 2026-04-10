# A2.03 — Form "Convergence"

## Claim (Proposition 4.3)

> The Weil quadratic form Q_N satisfies Q_N(f, g) → Q_∞(f, g)
> for all f, g in the algebraic direct limit
> E_∞^{+,alg} = ⋃_N E_N^+. The convergence is entry-by-entry in
> the matrix elements ⟨e_m, Q_N e_n⟩.

## What the proof says

> Each matrix element ⟨e_m, Q_N e_n⟩ depends only on primes
> dividing m and n. For N large enough that P_N ≥ max(prime
> factors of mn), the matrix element stabilizes at its limiting
> value.

## Assessment

**At the algebraic level, the statement is trivial.** If each
matrix element stabilizes once N is large enough, then certainly
Q_N(f, g) stabilizes for fixed f, g supported on finitely many
basis vectors. This is an elementary "stabilization in the direct
limit" observation.

**But entry-by-entry stabilization is much weaker than form
convergence in any analytically useful sense.** In particular, it
does NOT imply:

- Strong resolvent convergence,
- Norm resolvent convergence,
- Form convergence in the sense of Kato,
- Generalized strong resolvent convergence (gsrc) of Teschl.

Entry-by-entry convergence of a sequence of symmetric bilinear
forms on a growing sequence of subspaces is a *bookkeeping*
statement about how the matrices look in a fixed basis. Spectral
conclusions require an estimate on the *uniformity* of the
convergence over the common domain, quantitative in N and in the
vector f.

## The gap this hides

Paper 13 claims that "form convergence from state convergence"
(check IT3) holds. Section 9 uses Teschl Lemma 2.7 to promote
some kind of form convergence into gsrc. Teschl Lemma 2.7's
hypothesis (Appendix C.2) is:

> **(i)** pointwise convergence on the form domain: Q_N(f) → Q_∞(f)
> for all f ∈ 𝒟.
> **(ii)** uniform relative form bound: |Q_N(f) − Q_∞(f)| ≤
> a · Q_∞(f) + b · ‖f‖² with a < 1.

Proposition 4.3 delivers (i) for f ∈ algebraic direct limit. That
is a dense subspace of the limit form domain (provided one
identifies the right topology). OK so far.

(ii) is the substantive condition. Paper 13 claims (Theorem 9.3
+ Corollary 8.3) that (ii) holds with a = 0 and
b = C_Δ · ρ_Δ^{−N}. The proof uses:

  |⟨f, Δ_N f⟩| ≤ ‖Δ_N‖_op · ‖f‖²

where Δ_N is the "form difference" defined by
δ_N := Q_N − P_N Q_0 P_N, and the norm estimate
‖Δ_N‖_op ≤ C_Δ · ρ_Δ^{−N} is Corollary 8.3 / research/40 Lemma 1.

**Two problems:**

1. **Δ_N ≠ Q_N − Q_∞.** Paper 13 defines Δ_N as the difference
   Q_N − P_N Q_∞ P_N (the "Galerkin residual"), not the difference
   Q_N − Q_∞. For Teschl's hypothesis (ii), we need |Q_N − Q_∞|
   bounded on 𝒟. On vectors in the range of P_N, P_N Q_∞ P_N = Q_∞
   so the two differ only on vectors outside range(P_N). But
   Teschl's lemma asks for the bound on 𝒟, and if 𝒟 contains
   vectors outside range(P_N), the rank-one "Δ_N" doesn't cover
   them.

2. **‖Δ_N‖_op ≤ C ρ^{−N} requires independent verification.** The
   super-exponential decay is based on research/40 Lemma 1, which
   Paper 13 cites but does not include in the preprint. This is
   the *load-bearing quantitative estimate* of Layer 4 and is
   treated as an external lemma. See B3/01-gsrc-verification.md.

## What convergence is actually established here

Proposition 4.3 establishes: **pointwise (entry-by-entry) stabilization
of matrix elements for f, g in the algebraic direct limit.**

This is sufficient for Teschl's hypothesis (i) *if* one restricts
the form domain to the algebraic direct limit (and then extends by
completion). It is *insufficient* for hypothesis (ii) on its own;
(ii) must be separately verified from CF-decay or rank-one
estimates.

So Paper 13's claim that "ITPFI state convergence gives form
convergence" is slightly misleading: ITPFI gives the pointwise
stabilization (hypothesis (i)) but the relative form bound
(hypothesis (ii)) comes from CF decay, not from the ITPFI
factorization per se.

## Verdict on this subpoint

**Pass on entry-by-entry stabilization.** Trivial consequence of
prime-factorization of matrix elements.

**Not a pass on "form convergence" in the Teschl-Lemma-2.7 sense.**
ITPFI delivers (i) of Teschl's hypotheses; (ii) is a separate
estimate routed through CF decay, and the full Teschl input comes
from the combination. Paper 13 should distinguish these clearly.
As written, Section 4.7 and Section 9.3 blur the distinction.
