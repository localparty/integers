# C2.05 — Crossing Gap

## Question

Could eigenvalue crossings at specific N values destroy the
identification in HZ3 (zeros of ξ̂_N = eigenvalues of D_N)? If
the eigenvalue at D_N is not simple at that N, CCM Theorem 5.10
does not apply at that N. How is this handled?

## Finding

CCM Theorem 5.10 requires the minimum eigenvalue ε_N to be
(even-)simple. If at some specific N_0 the minimum is degenerate,
the theorem does not apply, and we cannot conclude anything about
spec(D_{N_0}).

Paper 13's AE simplicity argument ensures the set of "bad" N_0's
(if any) is sparse in some sense (discrete exceptional λ per N,
with fixed λ = √14 avoiding those sets for N ≤ 20).

**For the Hurwitz step**, what we need is that **asymptotically**
as N → ∞, most N values are "good" (simplicity holds), so the
eigenvalue data ξ̂_N has meaningful convergence behavior. If at
isolated N values simplicity fails, those N values can be skipped
when taking the limit — the convergence ξ̂_N → Ξ is a limit over
N → ∞ and can pass through a subsequence of "good" N.

Paper 13 does not explicitly say "we work along a subsequence of
good N". It implicitly claims all N ≥ some N_0 are good (at
λ = √14). The Slepian-limit argument (C2.03) is the proposed
justification, and it is heuristic.

## Alternate argument: "gaps shrink, so crossings are unlikely"

The paper's numerical data (Appendix F.3) shows the gap
(μ_1 − μ_0) shrinks exponentially in N: 8e-2 at N=1, 2.2e-12 at
N=5, 9.8e-22 at N=10, ..., 7.87e-35 at N=20. This is
**decreasing** toward zero, not stable.

A "crossing" is where the gap becomes zero. If the gap is
monotonically shrinking to zero, the ground state is becoming
**less** well-separated from the second eigenvalue, not more.
At infinite N, the gap vanishes and simplicity strictly fails.

**This is a concern.** Paper 13 argues that the gap remains
positive at each finite N, so simplicity holds, just with a
shrinking margin. That is technically correct. But it means the
"safety margin" for AE simplicity is eroding — at finite precision,
eventually the certification becomes impossible; at infinite
precision, one can always distinguish, but the eigenvalue match
with γ_n becomes less meaningful.

### Relationship to CCM Theorem 5.10(ii)

CCM claims eigenvalues approximate {γ_n} to precision O(ρ^{−N})
with ρ ≥ 4.27. At N = 20, this gives ~10^{−13} precision. At
N = 30, ~10^{−19}. These precisions are **much larger** than the
gap (10^{−35} at N = 20, 10^{−52} at N = 30).

So the eigenvalues of D_N are separated by a gap *smaller than*
the uncertainty in their identification with {γ_n}. In other
words: the gap structure distinguishes them at higher precision
than the CCM approximation. This is odd, though not contradictory.

**What this means:** the finite-N eigenvalues of D_N are not
exactly at {γ_n}; they are O(ρ^{−N}) close. The gap μ_1 − μ_0
at level N might or might not be the same shape as the gap
γ_2 − γ_1 between Riemann zeros. Paper 13 does not connect these
two notions of "gap".

## Verdict on this subpoint

**Weakened.** Eigenvalue "crossings" at finite N are formally
avoided by AE simplicity at λ = √14 (for N ≤ 20, by certification;
for N > 20, by the heuristic Slepian argument).

The erosion of the gap at high N is not discussed as a concern:
the certification margin goes from 10^{108} at N = 1 to 10^{72}
at N = 20. Extrapolating naively: at N = 50, the margin is
10^{~−30} or worse, so at 120-digit precision the certification
fails. **The method does not extend unconditionally to all N
without increasing precision linearly.**

The Hurwitz argument requires either (i) simplicity at every N
along some subsequence going to infinity, or (ii) a different
framework that doesn't depend on per-N simplicity. Paper 13
implicitly assumes (i) with all-N coverage at λ = √14.

**Required fix:** explicitly pass to a subsequence of N on which
simplicity is rigorously established, or provide a Slepian-
convergence theorem that proves AE simplicity at λ = √14 for
all large N (not just N ≤ 20).
