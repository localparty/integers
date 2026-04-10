# C2.04 — Sufficiency of AE for the Chain

## Question

The chain needs simplicity at each truncation level N to apply
CCM Theorem 5.10(iii). AE simplicity means it could fail at a
measure-zero set of spectral parameters. Does the proof handle
possible failure points?

## Paper 13's claim (Section 12.5)

> "The Bögli argument (Section 9) requires AE simplicity at ONE
> specific λ = λ_N for each N, with λ_N not in the exceptional
> set S_N. Since S_N is discrete for each N, such a choice
> always exists.
>
> The certified computation provides an explicit universal
> choice: λ_N = √14 works for *all* N = 1, …, 20."

## Assessment

### Is "simplicity at one λ per N" sufficient?

The Bögli argument (Section 9) is about the limit N → ∞ at
**fixed** λ. If we fix λ = √14, we need simplicity at λ = √14 at
every N (all the way to infinity). This is what Paper 13 is
trying to establish.

**Does the proof need simplicity at every N?** Yes, because CCM
Theorem 5.10 is invoked at each finite N. If at some N_0 the
minimum eigenvalue of A^{ev}(√14, N_0) is not simple, then CCM
Theorem 5.10 does not apply at that N_0, and the Hurwitz link
"zeros of ξ̂_{N_0} = eigenvalues of D_{N_0}" breaks at that
level.

However, **if failures are at isolated N values**, could the
identity theorem bridge over them? Paper 13 Section 12.5 argues:

> "The deeper reason AE suffices is analytic continuation. The
> eigenvalues of D_N are meromorphic functions of λ. If the
> limit spectrum spec(D_∞) is computed at a non-exceptional λ,
> the identity theorem for meromorphic functions ensures the
> result is independent of the choice of λ. Crossings at
> exceptional points are removable singularities (Kato
> perturbation theory)."

**This is a different argument** from what Section 12.5 starts
with. It says: the limit spectrum (at some "generic" λ) is
determined by analytic continuation, so isolated failures at
specific λ values can be bypassed.

But this requires the limit spec(D_∞) to be computable in a way
that is analytic in λ, and requires analytic continuation to be
valid across "exceptional" λ values. These are stronger claims
than the finite-N certification supplies.

### Is the exceptional set S_N really at isolated λ values?

From the identity theorem: yes, f_N being real-analytic and
non-zero at one point implies S_N is discrete (isolated points
in λ).

So **at each fixed N, AE simplicity fails on a discrete set S_N
in the λ variable**. And Paper 13 picks λ = √14, which is not in
any of S_1, ..., S_{20} (by certification).

For N > 20, the claim is that √14 ∉ S_N (by the Slepian-limit
plausibility argument). See C2.03 — this is the weak point.

### The "crossings are removable singularities" claim

This is interesting but not developed. If spec(D_N) at λ ∈ S_N
(an exceptional point) has an eigenvalue crossing, and if the
spectrum is analytic in λ outside S_N, then the "limit spectrum"
at a generic λ is well-defined.

But Paper 13 uses a **fixed** λ = √14 throughout, so it does not
actually vary λ. The "removable singularity" argument would be
relevant only if we were analytically continuing in λ. We are
not.

At the fixed λ = √14, we need simplicity at every N. That's the
hard thing.

## Verdict on this subpoint

**Conditional pass** at N ≤ 20 (by certification).

**Conditional pass** at N > 20 *if* the Slepian-limit argument
is converted to a rigorous theorem.

**Not passed** by the analytic-continuation-in-λ argument in
Section 12.5, which is a different and inapplicable story
(the paper uses fixed λ).

**Required fix:** choose between:

(a) Prove AE simplicity rigorously at every N (via a Slepian-
convergence theorem, per C2.03), or

(b) Provide a real analytic-continuation-in-N argument (not
λ), if such a thing exists.

Currently (a) is the more promising path but is not executed
rigorously in the preprint.
