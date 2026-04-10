# C2.03 — The Prolate ("Slepian") Extension to N > 20

## What Paper 13 argues

Section 12.3 "$N > 20$":

> "Prolate spheroidal wave function (Slepian) limit. For large N,
> the even-sector matrix converges to the prolate spheroidal wave
> operator. The Slepian ground state is positive, and the cosh
> kernel is positive. Therefore the limiting overlap is strictly
> positive. The certified computation shows
> |⟨φ_0|a⟩| > 0.509 at N = 20, converging monotonically toward
> ~1/2. For N > 20, the overlap remains bounded below by ~0.49,
> far from zero."

## Issues

### (a) "The even-sector matrix converges to the prolate spheroidal wave operator"

This is a **limit statement** without a specific theorem citation
or a rate. What topology? What is the target "prolate spheroidal
wave operator"? In what sense does A^{ev}(λ, N) → this operator
as N → ∞?

The prolate spheroidal wave functions (Slepian's work) are
eigenfunctions of an integral operator on an interval, with
specific bandwidth and interval parameters. The connection between
Paper 13's finite-dimensional A^{ev} and the continuous Slepian
operator is **not spelled out** in the preprint.

### (b) "The Slepian ground state is positive"

The prolate spheroidal wave function ψ_0 (ground state of the
Slepian operator) is the Slepian sequence's leading function,
famously positive on the interval and concentrated there. Standard.

### (c) "The cosh kernel is positive"

The archimedean cosine vector a(λ) has components
a_0 = 1/L², a_n = √2 / (L² + 16 π² n²) (Sec 12.2). All components
positive. So "a is a positive vector" in the cosine basis.

### (d) "Therefore the limiting overlap is strictly positive"

If ψ_0 is positive and a is positive (in the same basis), their
inner product is positive. **This is correct for the LIMITING
overlap**. But the limiting overlap being strictly positive does
not imply the finite-N overlaps are uniformly bounded away from
zero.

The correct argument would be: (1) f_N(√14) → f_∞(√14) as N → ∞;
(2) f_∞(√14) > 0; (3) by continuity, f_N(√14) ≥ c > 0 for all N
sufficiently large.

Paper 13 gestures at (1)–(3) but does not establish them
rigorously. In particular, (1) requires a convergence theorem
that is not in the paper.

### (e) "Monotonically toward ~1/2"

The certified values at N = 1, 5, 10, 15, 20 are 0.782, 0.587,
0.536, 0.518, 0.509. This is monotonically decreasing toward 0.5.

**"Monotone" based on 5 data points is not a theorem**. Numerical
monotonicity at N = 1, 5, 10, 15, 20 is consistent with
non-monotone behavior at intermediate N or at N > 20. Without a
proof of monotonicity (e.g., via a comparison inequality between
A^{ev}(λ, N) and A^{ev}(λ, N+1)), this is a heuristic.

### (f) The ~0.49 lower bound

If the values converge to ~0.5 and the last certified value is
0.509 at N = 20, the claim "> 0.49 for all N > 20" is not
guaranteed. The convergence could overshoot and come back up, or
dip below 0.49 before returning to 0.5.

## What's actually required

For the proof chain, Paper 13 needs f_N(√14) ≠ 0 for all N, not
just for N ≤ 20. The finite certification covers N ≤ 20. The
Slepian-limit argument is supposed to cover N > 20.

**The Slepian argument as written is a plausibility argument, not
a theorem.** It establishes a reasonable expectation that
f_N(√14) is bounded below as N → ∞, but it does not rigorously
prove it.

A truly rigorous version would:

1. Define the prolate operator P^{(λ)} explicitly.
2. Prove that A^{ev}(λ, N) converges to P^{(λ)} in the
   operator-norm sense (or at least in the appropriate sense to
   control eigenvector convergence).
3. Apply a stability theorem (e.g., Kato's) to conclude
   f_N(λ) → f_∞(λ).
4. Verify f_∞(√14) > 0 directly from the Slepian/prolate
   theory.
5. Conclude f_N(√14) ≥ c > 0 for all N sufficiently large.
6. Combine with the certified N ≤ 20 to cover all N.

Paper 13 does (4) (positivity of the limit) and (6) (certification
for small N), but not (1), (2), (3), or (5). The argument has a
real gap.

## Verdict on this subpoint

**Weakened.** The prolate/Slepian limit argument is a
heuristic extension, not a proof. It suggests that AE simplicity
likely holds for all N at λ = √14, but it does not establish it.

A refereeable version needs either:

(a) **A rigorous Slepian-convergence theorem** for A^{ev}(λ, N)
as N → ∞, with operator-norm or spectral convergence giving
eigenvector continuity, OR

(b) **Extended certification** to larger N (expensive — precision
must grow linearly in N), reaching beyond any N that could
arise in the downstream use, OR

(c) **A different argument** that does not rely on simplicity at
every N. For example, if the proof can be run at finitely many
values of N and then extended by real-analyticity, the "every N"
requirement can be sidestepped.

As currently written, **AE simplicity for N > 20 is not proved**.
This is one of the concrete gaps of the paper.
