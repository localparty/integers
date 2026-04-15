# B3.07 — Spectral Pollution

## Question

Bögli guarantees no spurious eigenvalues under H1 + H2. But does
"no spurious eigenvalues" mean "no extra spectrum at all"? Could
continuous spectrum appear in the limit even if no spurious
eigenvalues do?

## The distinction

In perturbation-theoretic spectral convergence, there are three
distinct failure modes:

1. **Loss of spectrum:** λ ∈ spec(T_∞) is not a limit of
   eigenvalues of T_n. (Eigenvalues disappear in the limit.)

2. **Spurious eigenvalues:** λ_n ∈ spec(T_n) with λ_n → λ but
   λ ∉ spec(T_∞). (Fake limits.)

3. **Continuous-spectrum creep:** T_∞ has continuous spectrum at
   a location where T_n has none.

Bögli's H1 + H2 rules out (1) and (2). It is less clear about (3)
because each T_n on a finite-dim space has only point spectrum,
while T_∞ on an infinite-dim space can have continuous spectrum.

## Does Paper 13 need the absence of continuous spectrum?

Layer 5 (Hurwitz) identifies lim spec(D_N) with the zeros of Ξ.
The zeros of Ξ form a **discrete** set (assuming Xi is a
nontrivial entire function, which it is). So Hurwitz gives a
discrete limit spectrum.

Layer 4 (Bögli) says spec(D_∞) = lim spec(D_N). If the RHS is
discrete (by Hurwitz), then spec(D_∞) is discrete. So continuous
spectrum is excluded *a posteriori* by Hurwitz.

**But wait:** if D_∞ is a self-adjoint operator with discrete
spectrum, its form must have compact resolvent (or some
equivalent compactness property). Does Paper 13 establish this?

Corollary 9.8: "The operator D_∞ has compact resolvent. This
follows from the uniform H¹ bound (Theorem 7.1) and the
Rellich–Kondrachov compactness theorem (Corollary 7.3)."

Compact resolvent ⇒ discrete spectrum with eigenvalues of finite
multiplicity, accumulating only at ∞. Good — this is what's
needed.

## Is the compact resolvent correctly deduced?

If (D_∞ − i)^{−1} is a limit (in some sense) of compact operators
(D_N − i)^{−1}, and the limit is in the operator-norm sense, then
(D_∞ − i)^{−1} is compact. But the convergence Paper 13
establishes is gsrc (strong), not norm. Strong limits of compact
operators are **not generally compact**.

For example: shift operators on ℓ² are strong limits of
finite-rank (hence compact) truncations but are not themselves
compact.

So the deduction "gsrc + compact finite-rank operators ⇒ compact
limit" is **not automatic**. It requires the discrete-compactness
hypothesis H2 (or equivalent), which Paper 13 claims to establish.

The correct logical chain:
- gsrc + H2 (Bögli) ⇒ spectral exactness (no spurious, no loss)
- Compact resolvent of D_∞ is a **separate** claim.

Paper 13 Cor 9.8 asserts compact resolvent from H¹ bound + Rellich
directly: "every bounded sequence in H¹ has an L²-convergent
subsequence", so (D_∞ − i)^{−1}: L² → H¹ is bounded, composed
with H¹ ↪ L² compact gives (D_∞ − i)^{−1}: L² → L² compact.

This requires:
(a) (D_∞ − i)^{−1} is L² → H¹ bounded,
(b) H¹ ↪ L² is compact.

(b) is Rellich, standard. (a) requires the uniform H¹ bound from
Theorem 7.1 to survive the N → ∞ limit. If Theorem 7.1 holds
uniformly and (D_N − i)^{−1} → (D_∞ − i)^{−1} strongly, the
limit operator has at most the same L² → H¹ bound (by strong
convergence on the unit ball and dense domain arguments).

OK so the deduction is essentially correct **if** Theorem 7.1 is
truly uniform in N. See B3.05 for the λ-dependence concern.

## Verdict on this subpoint

**Conditional pass.** If Theorem 7.1 is uniform in N (i.e., at
fixed λ), then D_∞ has compact resolvent and continuous spectrum
is excluded a priori. Bögli + Hurwitz then give discrete spectrum
identical to {γ_n} within any compact window.

**Risk:** if Theorem 7.1's proof breaks (e.g., at λ > e^π) or if
the uniformity-in-N aspect is not truly established, then
compact resolvent of D_∞ is not guaranteed, continuous spectrum
could creep in, and the identification spec(D_∞) = {γ_n} could
miss spectral components.

At the paper's numerical choice λ = √14, the bound holds and the
argument is intact.
