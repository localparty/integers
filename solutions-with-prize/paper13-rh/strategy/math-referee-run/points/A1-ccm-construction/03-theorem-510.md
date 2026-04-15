# A1.03 — CCM Theorem 5.10

## Question

Does Theorem 5.10 require RH? Does it assume anything about the
location of zeros? Or is it a computation that happens to match?

## Finding

CCM Theorem 5.10 (as reported in Paper 13 Section 3.4 and Appendix
A.4) has three conclusions:

> **(i)** eigenvalues of D' are real and simple (in the even sector)
> **(ii)** eigenvalues approximate {γ_n} to precision O(ρ^{−N}), ρ ≥ 4.27
> **(iii)** the zeros of ξ̂_λ = 2L^{−1/2} sin(zL/2) · Σ_j ξ_j/(z − 2π j/L)
> coincide with spec(D_log^{(λ,N)})

and the numerical claim:

> At N = 6, first 10 eigenvalues match γ_1,…,γ_{10} to 10^{−55}.

### (i) Reality and simplicity

Reality is a consequence of self-adjointness (Theorem 4.2). Not RH.
Simplicity is an additional hypothesis in CCM that requires the
even-simple assumption on the minimum eigenvalue — which Paper 13
supplies via AE certification + even-sector restriction.

**No hidden RH assumption.**

### (ii) The 10^{-55} "approximation"

This is a **numerical claim**. It is a computation that *happens to
match* 10 Riemann zeros at N = 6 to 55 digits. Extraordinary
evidence but not a proof.

Critically: the *direction* of the claim matters. CCM asserts
"eigenvalues approximate γ_n with precision O(ρ^{−N})". This is an
*a priori* bound derived from CF approximation theory, not an
inference from the observed numerical match. If the a priori bound
is a theorem (not only a fitted rate), then the "approximation"
statement is mathematically substantive even before one plugs in
numerical zeros.

Paper 13 does not reproduce the CF argument. It takes the O(ρ^{−N})
bound on faith.

**No hidden RH assumption, *if* the O(ρ^{−N}) bound is genuinely a
priori** (i.e., derives from analytical CF theory, not from a
numerical fit to Riemann zeros). The latter would be circular. The
burden on the CCM paper is to show it is the former.

### (iii) The identification ξ̂_λ zeros = D_log spectrum

This is the most delicate claim. The function

  ξ̂(z) = 2L^{−1/2} sin(zL/2) · Σ_{j=−N}^{N} ξ_j / (z − 2π j/L)

is a rational function times sine, with:

- 2N+1 poles at z = 2π j/L, j ∈ [−N, N]
- zeros from the sine at z = 2π n/L for all integer n — at integer
  indices |n| > N these are genuine zeros of ξ̂; at |n| ≤ N the
  sine zero is cancelled by the rational-function pole if ξ_n ≠ 0
- additional zeros where Σ_j ξ_j/(z − 2π j/L) has its own zeros

The claim "zeros of ξ̂_λ coincide with spec(D_log^{(λ,N)})" must
be interpreted as: *the zeros of the rational-factor part inside
the principal strip* are the finite spectrum of D_log, once the
spurious sine zeros at |n| > N are separated.

Paper 13's statement (Section 11, eq. 11.1) is:

> "zeros of ξ̂_N = eigenvalues of D_N exactly at fixed (λ, N)"

This is strong and, as stated, slightly misleading because of the
sine-zero ambiguity. A careful restatement would be: *the
finitely many roots of the rational factor lying inside the
principal strip* are in bijection with spec(D_N). The Hurwitz
argument in Section 10 only cares about the limiting behavior of
these rational-factor roots as the approximation level refines,
and they correspond bijectively (by CCM 5.10(iii)) to spec(D_N).

**Critical issue:** D_log is presented as a "full operator"
(Appendix A.4). The distinction between D' (the perturbed scaling
operator on the finite-dim H) and D_log (the "full" operator
whose spectrum is identified with the zeros of ξ̂) is not clearly
drawn in Paper 13. If D_log is an infinite-dimensional auxiliary
object whose spectrum genuinely contains the infinite set of
rational-factor zeros, then a different, non-finite spectral
theorem is in play. Paper 13 does not clarify this.

### The real-zeros observation

The crucial consequence of (iii) that Paper 13 *needs* but does
**not explicitly state**:

> **Every zero of ξ̂_N in the complex plane is real.**

This follows from: the sine factor has only real zeros; the
rational factor has real poles (at 2π j/L) and, if CCM's
identification is correct, its internal zeros are the real
eigenvalues of a self-adjoint operator. Therefore the full zero
set of ξ̂_N as a meromorphic function is a subset of ℝ.

This is the property that makes the Hurwitz argument work in the
complex strip |Im z| < 1/2 (see points/C1-hurwitz). A sequence
of holomorphic functions with only real zeros converging
uniformly to Ξ forces every zero of Ξ in the domain to be real.

**Paper 13 never states "ξ̂_N has only real zeros" as a proposition.**
The Hurwitz argument in Section 10 is phrased as "eigenvalues of
D_N converge to {γ_n}", which is the *weaker* statement the paper
actually states. The stronger statement is what is *needed* to rule
out off-line zeros of ζ in the critical strip.

This is a real exposition gap, and it masks the fact that the
final step of the proof depends on the implicit claim that ξ̂_N
is real-zero-only.

## Verdict on this subpoint

Theorem 5.10 is taken from CCM and not re-derived. The three
conclusions do not contain a hidden RH assumption *given that*:

- the O(ρ^{−N}) bound in (ii) is truly a priori (not fit to
  Riemann data),
- the identification (iii) holds in the precise sense that the
  rational-factor zeros of ξ̂_N in the principal strip are the
  spectrum of the finite-dim D' (or a well-defined closure D_log),
- ξ̂_N has only real (complex-plane) zeros.

Paper 13 relies on (iii) in the strongest form for the Hurwitz
step but does not explicitly state the real-zero property.

**Flagged as a required clarification** — see C1-hurwitz/01-uniform
-convergence.md.
