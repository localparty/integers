# B2.02 — The ITPFI Triangle

## The structure

The "ITPFI triangle" is the name Paper 13 gives to the triangle
inequality routed through ξ_0:

  ξ_λ ∼ ξ_0 ∼ c · k_λ,

where:
- ξ_λ = minimal eigenvector of QW_λ^{N,+} (the "true" target),
- ξ_0 = minimal eigenvector of T_0 (the Euler product part),
- k_λ = prolate approximation from CCM (a specific linear
  combination of prolate spheroidal wave functions with vanishing
  integral, CCM eq 7.6).

The first inequality (ξ_λ ≈ ξ_0) is the Davis–Kahan step in B2.01
(perturbation by the archimedean term τ^{(ℝ)}).

The second (ξ_0 ≈ c · k_λ) comes from CCM Lemma 7.2
(Meixner–Schäfke) + an ITPFI-tail argument.

## Lemma 6.3: ξ_0 ≈ c · k_λ

The bound ‖k_λ − c' · ξ_0‖ = O(λ^{−2}) (Paper 13 Lemma 6.3). The
proof:

1. CCM Lemma 7.2: max_{x ∈ [−λ, λ]} |h_λ(x) − h(x)| ≤ c · λ^{−2}.
2. The map E: L²([−λ, λ]) → E_N^+ is bounded with norm independent
   of λ (CCM eq 7.6).
3. Therefore ‖k_λ − E(h)‖ ≤ ‖E‖ · ‖h_λ − h‖_{L²} = O(λ^{−2}).
4. In the ITPFI framework, the Hermite functions h_0, h_4 generate
   the representation space of the KMS_1 state, and the
   eigenvector ξ_0 of T_0 converges to the vector E(h) in the
   large-λ limit.
5. The Euler product tail beyond λ² contributes O(λ^{−2}) by PNT
   estimate Σ_{p > λ²} (log p)/√p = O(1/λ).
6. Therefore ‖E(h) − c' · ξ_0‖ = O(λ^{−2}).
7. Triangle inequality gives ‖k_λ − c' · ξ_0‖ = O(λ^{−2}).

## Concerns

### Step 4: "ξ_0 of T_0 converges to E(h) in the large-λ limit"

This is stated but not proved. It is essentially a claim that in
the large-λ limit, the minimal eigenvector of the Euler product
operator T_0 converges to a specific Hermite-like function. Why?
What topology? How fast?

The paper offers no proof. This is a **significant gap**: it is
where the Hermite/prolate limit of the ITPFI spectrum appears,
and it is the structural reason why ξ_0 ≈ k_λ. A reader cannot
verify this without additional references.

### Step 5: PNT estimate Σ_{p > λ²} (log p)/√p = O(1/λ)

Let me check: by the prime number theorem,

  Σ_{p > X} (log p)/√p ∼ ∫_X^∞ (log t)/(√t · log t) dt = ∫_X^∞ dt/√t = ∞.

Wait — Σ_{p > X} (log p)/√p is a divergent series in the upper
limit. Setting X = λ² gives a partial sum starting above λ².
That is divergent. The claim "= O(1/λ)" cannot be right as stated.

Let me reparse. Maybe Paper 13 means Σ_{p > λ²} (log p)/p^s for
some s > 1, where it is convergent. Or maybe (log p)/p^{s/2}
with s > 2 effectively. The formulation "Σ (log p)/√p" diverges.

This looks like a **real error**, or a notational slip that makes
an estimate unverifiable. If the actual formula is different
(e.g., (log p) · p^{−3/2}, which converges), the O(1/λ) rate
would be derivable. But as stated, the cited estimate is
nonsense.

### Step 6: ‖E(h) − c' · ξ_0‖ = O(λ^{−2})

Depends on the (slipped?) PNT estimate in Step 5.

## What is actually needed downstream

Lemma 6.3 is used in Theorem 6.4 (eigenvector approximation) to
get the O(λ^{−2}) term in the triangle inequality. The dominant
term from Lemma 6.1 is O(1/λ), so the final rate O(1/λ) only
needs Lemma 6.3 to give anything o(1/λ). A slightly weaker
Lemma 6.3 (O(1/λ) instead of O(λ^{−2})) would still give the
same final rate. So the PNT-estimate issue, if it can be patched
at all, only needs to give an O(1/λ) tail bound rather than
O(λ^{−2}).

Still, the as-stated estimate in Step 5 is not right, and this
needs to be fixed.

## Verdict on this subpoint

**Weakened.** The structural idea (routing through ξ_0 via the
Euler product gap) is sensible. The Meixner–Schäfke bound is
standard and correct. But:

1. The claim "ξ_0 → E(h) in the large-λ limit" is stated without
   proof and is a load-bearing structural statement.

2. The PNT estimate Σ_{p > λ²} (log p)/√p = O(1/λ) is not
   literally true — the series diverges. Paper 13 has a slip
   here.

3. The O(λ^{−2}) rate claim is not verifiable as written; an
   O(1/λ) rate would still suffice for Theorem 6.4.

**Required fix:** Correct the PNT-tail estimate (probably intended
as Σ (log p) · p^{−3/2} or similar convergent form). Supply or
cite a proof that ξ_0 → E(h) in the appropriate norm with
explicit rate.
