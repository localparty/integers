# B1.01 — The Archimedean Ratio

## The proof Paper 13 gives (Proposition 5.1)

Paper 13 Section 5.2:

> The archimedean contribution is controlled by the Stirling
> asymptotics of the gamma function:
>
>   τ^{(ℝ)}(λ) ∼ (1/2) log(λ/2π) − (1/2) ψ(1/4 + iλ/2),
>
> where ψ is the digamma function. The real part satisfies
> Re ψ(1/4 + iλ/2) = log(λ/2) + O(1/λ²) by Stirling, so
> ‖τ^{(ℝ)}(λ)‖ = O(log λ).
>
> The p-adic contributions satisfy
> ‖Σ_p τ^{(p)}(λ)‖ ≥ c · λ · log λ
> for an absolute constant c > 0, by the explicit formula for
> the p-adic Weil distributions. The ratio is therefore
> O(log λ / (λ log λ)) = O(1/λ).

## Assessment

This is a **sketch**, not a proof. The two concrete numerical
claims need closer examination:

### Claim 1: ‖τ^{(ℝ)}(λ)‖ = O(log λ)

The digamma asymptotics ψ(z) ∼ log z − 1/(2z) − Σ B_{2k}/(2k z^{2k})
for |arg z| < π is standard. At z = 1/4 + iλ/2 with λ → ∞:

  ψ(1/4 + iλ/2) = log(iλ/2) + O(1/λ) = log(λ/2) + iπ/2 + O(1/λ).

So Re ψ = log(λ/2) + O(1/λ), which matches the paper. The scalar
τ^{(ℝ)}(λ) *as a scalar* is of order log λ. That checks out.

BUT: the paper is claiming a bound on **operator norm**
‖τ^{(ℝ)}(λ)‖_op, not a scalar. τ^{(ℝ)} is a test-function that acts
as an *operator* on some function space (the form-theory setting
makes it a bilinear form). The operator norm depends on the
domain. At λ = γ_n, what is the domain, and why is the operator
norm of order log λ?

Paper 13 does not make this explicit. Section 6.1 later quotes
Estimate 1 as "‖τ^{(ℝ)}‖_op ≤ 5.5 bounded, independent of λ for
large λ". Wait — **that's a bounded constant, not O(log λ).**

So there's an inconsistency between the rate claimed in Section 5
(O(log λ)) and the constant claimed in Section 6 (bounded by
5.5). Perhaps the 5.5 bound is what "Estimate 1 (research/20)"
actually delivers, and the Section 5 "proof" is a heuristic.
Paper 13 is inconsistent about which rate is the actual theorem.

### Claim 2: ‖Σ_p τ^{(p)}(λ)‖ ≥ c λ log λ

This is a *lower bound*. The paper gives no proof, only a hand-
wave ("by the explicit formula for the p-adic Weil distributions").
A lower bound on an operator norm from "the explicit formula" is
not automatic; it requires showing that the p-adic sum is actually
*large* as an operator, not merely that it dominates some
particular vector. The paper does neither.

### What the downstream argument actually needs

Lemma 6.1 uses the estimate ‖ξ_λ − ξ_0‖ ≤ ‖τ^{(ℝ)}‖_op / gap(T_0).
Section 6.2 claims ‖τ^{(ℝ)}‖_op ≤ 5.5 and gap(T_0) ≥ C'' · λ, so
the ratio is O(1/λ). The 5.5 bound is cited as Estimate 1,
research/20, "closed". The lower bound c · λ · log λ is not
actually invoked in Section 6 — Section 6 uses the gap lower
bound gap(T_0) ≥ C'' · λ instead.

So Proposition 5.1 as stated (the ratio O(1/λ)) is *presented* as
the downstream input, but Section 6 *actually uses* different
quantities (‖τ^{(ℝ)}‖ ≤ 5.5 constant, and gap(T_0) ≥ C'' λ). The
two formulations are not the same.

## Finding

**The Section 5.2 "proof" is not rigorous**. It is a sketch that
states the right sort of asymptotic (O(log λ) for the scalar
archimedean term, lower bound for the p-adic sum) but does not
properly compute operator norms, does not establish uniformity,
and does not match the formulation used downstream.

**The downstream Section 6 formulation** (‖τ^{(ℝ)}‖ ≤ 5.5,
gap(T_0) ≥ C'' λ) is cited to research/20 and research/24, which
are internal research notes not included in the preprint. I
cannot verify these without access to the notes.

## Verdict on this subpoint

**Weakened as stated in the preprint.** The rigorous statement of
Estimate 1 is somewhere in research/20 and research/24, not in the
paper. Section 5.2's sketch is inconsistent with Section 6.2's
usage. A referee cannot close this without reading the internal
research notes.

**Required fix:** State Proposition 5.1 precisely. Choose ONE
formulation:
- the ratio bound O(1/λ), with complete proof from Stirling and
  the explicit formula, OR
- the separate bounds ‖τ^{(ℝ)}‖ ≤ 5.5 (constant) and
  gap(T_0) ≥ C'' λ (linear growth), which is what the downstream
  argument uses.

Currently the paper states the first and uses the second.
