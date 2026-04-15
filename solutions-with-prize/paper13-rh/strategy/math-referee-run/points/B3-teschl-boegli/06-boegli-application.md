# B3.06 — Application of Bögli Theorem 2.5

## What Bögli proved

Paper 13 Appendix D.2 paraphrases:

> **Theorem (Bögli 2017, Theorem 2.5).** Let {T_n} be a sequence
> of closed operators on a Hilbert space H. Suppose:
>
> **H1 (gsrc):** (T_n − z)^{−1} → (T − z)^{−1} strongly for some
> z in the resolvent set of T.
>
> **H2 (discrete compactness):** Every sequence {u_n} with
> u_n ∈ Dom(T_n), ‖u_n‖ ≤ 1, and ‖T_n u_n‖ ≤ C, has a convergent
> subsequence in H.
>
> Then:
>
> (i) spec(T) = lim_{n→∞} spec(T_n) in Hausdorff metric on
> compact subsets.
>
> (ii) No spurious eigenvalues.
>
> (iii) Every λ ∈ spec(T) is a limit of some λ_n ∈ spec(T_n).

Bögli's original result is for **non-selfadjoint** sequences. The
self-adjoint case is a specialization.

## Applicability to Paper 13's setting

Paper 13 uses Bögli with:
- T_n = D_N acting on E_N^+,
- T = D_∞ acting on some limit space,
- H1 from Teschl Lemma 2.7 via the form bound with a = 0,
- H2 from uniform H¹ + Rellich.

Issues:

### 1. Different Hilbert spaces

Bögli's theorem is stated for **a single Hilbert space H** with
the operators T_n all densely defined on H. Paper 13's D_N act on
**different** spaces E_N^+ of growing dimension. To apply Bögli,
one needs to embed the D_N into a common space.

Standard trick: embed E_N^+ → E_∞^+ via the cosine basis
identification, extend D_N by zero (or identity on the
complement). Then D_N becomes a densely defined operator on
E_∞^+, and Bögli's setup applies.

Paper 13 does this implicitly (via the Galerkin projection P_N)
but does not make the embedding explicit. The crucial question is
whether the **extension-by-zero** (or similar) preserves the
gsrc and discrete-compactness properties. For self-adjoint
Galerkin approximations of a closed semibounded form, this is
standard — but requires Paper 13 to state it.

### 2. "gsrc" vs ordinary strong resolvent convergence

Bögli's H1 in the paper is "strong resolvent convergence for
some z in the resolvent set of T". Teschl Lemma 2.7 gives
**generalized** strong resolvent convergence, which may or may not
be the same thing.

Generalized srg (gsrc) typically refers to convergence in the
presence of varying domains (e.g., Friedrichs extensions of forms
with different domains). Ordinary srg requires a common domain.
These are related but not identical.

**Whether Bögli's theorem applies under gsrc rather than srg** is
a question about the Bögli paper that I cannot settle without
reading it. Paper 13 implicitly assumes the answer is yes.

### 3. Hausdorff convergence on "compact subsets"

Bögli's conclusion is Hausdorff convergence of spectra on compact
subsets. For D_N with unbounded (finite-rank-approximated)
spectrum and D_∞ with unbounded self-adjoint spectrum, this is
sensible: on any bounded window [−T, T], the finite spectra of
D_N and D_∞ within [−T, T] are Hausdorff-close.

This feeds into the Hurwitz argument, which works on compact
subsets of the complex strip. Consistent.

## Verdict on this subpoint

**Conditionally pass**, subject to:

1. **Verifying Bögli's theorem applies under gsrc** (not just
   ordinary srg). Paper 13 does not cite a specific theorem
   version that explicitly covers Galerkin sequences with gsrc.

2. **Making the embedding E_N^+ ↪ E_∞^+ explicit** and
   verifying that the extended D_N satisfy Bögli's setup.

Both are technical items that a careful referee would want
addressed. Neither is definitively blocking.

**Confidence: 7/10**, conditional on Bögli's theorem actually
covering the situation claimed.
