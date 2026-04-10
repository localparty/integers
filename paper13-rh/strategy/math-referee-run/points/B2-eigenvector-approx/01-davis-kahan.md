# B2.01 — Davis–Kahan and the Spectral Gap

## The Davis–Kahan step (Lemma 6.1)

For rank-one perturbation T_0 → T_0 + τ^{(ℝ)}, Davis–Kahan gives

  sin ∠(ξ_λ, ξ_0) ≤ ‖τ^{(ℝ)}‖_op / gap(T_0),

where gap(T_0) = μ_2(T_0) − μ_1(T_0) is the spectral gap between
the two smallest eigenvalues of T_0.

## Critical structural point (Paper 13 Remark 6.2)

The paper **insists** on using gap(T_0) — the gap of the Euler
product part — and **not** gap(QW_λ) — the gap of the full
perturbed form. The reason:

> "The gap of QW_λ decreases exponentially in N (research/24:
> gap ∼ e^{−α t} where t = log λ), and a direct Davis–Kahan bound
> through QW_λ diverges. The ITPFI decomposition reveals the
> correct perturbation-theory target."

So the paper's strategy is: perturb around T_0 (whose gap is
large), not around QW_λ (whose gap is exponentially small).

## Where does "gap(T_0) ≥ C'' · λ" come from?

Paper 13 (Eq 6.6) claims

  gap(T_0) ≥ C'' · λ

with C'' > 0 "depending only on the truncation geometry". The
argument sketch:

> The operator norm ‖T_0‖_op grows as λ by the prime number
> theorem (Σ_{p ≤ λ²} (log p)/√p ∼ 2λ), and the relative gap
> μ_1/μ_2 ∼ 10^{−6} is stable in N (research/24).

This is **NOT a proof of a gap bound**. Having operator norm ∼ λ
and a "stable relative gap" does NOT imply an absolute gap of
order λ. If the relative gap is a constant ratio and the operator
norm grows, you get an absolute gap growing at the same rate only
if the relative gap is stable for the **smallest two eigenvalues**,
which is a distinct claim.

Moreover, "verified at all tested truncation levels" is numerics.

Further: what **is** T_0? From Section 6.1:

  T_0 := τ^{(0,2)} + Σ_{p ≤ P_N} τ^{(p)}

i.e., the rank-2 condensation τ^{(0,2)} plus the p-adic sum. This
is a sum of finitely many operators depending on both λ (bandwidth)
and N (prime count). The gap structure of a sum of operators is
not controlled by the norms of summands in general.

## The ‖τ^{(ℝ)}‖_op ≤ 5.5 bound

Paper 13 Eq (6.5) cites:

  ‖τ^{(ℝ)}‖_op ≤ 5.5, bounded, independent of λ for large λ.

Source: research/20. No derivation in the preprint.

## Is Davis–Kahan correctly applied?

The standard Davis–Kahan sin-θ theorem applies to rank-one-like
perturbations with an assumption like: the perturbed eigenvalue
is separated from other eigenvalues of the unperturbed operator
by at least the gap. If μ_1(T_0) is simple and
μ_2(T_0) − μ_1(T_0) = gap(T_0), then the nearest-neighbor form of
Davis–Kahan gives:

  sin ∠(ξ(T_0 + V), ξ(T_0)) ≤ ‖V‖ / gap(T_0)

where ξ(·) is the ground eigenvector. This is the right form.

Paper 13's application is valid *provided* the gap(T_0) ≥ C'' · λ
bound holds. The concern is solely whether this gap bound is
proved.

## Verdict on this subpoint

**Davis–Kahan application is standard** and correctly shaped.

**The gap lower bound gap(T_0) ≥ C'' · λ is not proved in the
preprint.** It is inherited from research/24 and supported only by
numerics. This is the substantive missing step.

The paper's "insight" that one should perturb around T_0 instead
of QW_λ (to avoid the exponentially small gap of QW_λ) is a sound
strategic observation, but it requires a genuine gap estimate on
T_0 to be effective. That estimate is not in the preprint.
