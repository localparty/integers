# A1.04 — The Two Missing Steps

## Question

CCM leaves open: (i) the limit N → ∞, and (ii) exact spectral
identification. Does Paper 13 correctly identify these as the gaps,
or does it mischaracterize what CCM proved?

## Finding

**Correctly identified.** Paper 13 Section 3.5 lists:

> **Gap (i): The limit.** The operators D_N act on different Hilbert
> spaces E_N^+. … no a priori reason why a limit operator D_∞ should
> exist on any natural Hilbert space.
>
> **Gap (ii): The spectrum.** Even if D_∞ exists and is self-adjoint,
> the approximation spec(D_N) ≈ {γ_n} does not by itself imply
> spec(D_∞) = {γ_n}.

Both gaps are genuine. CCM's construction is inherently finite-dim
at each N; their Theorem 5.10 is a finite-dim statement plus a
numerical extrapolation rate. CCM does not claim a limit operator
nor that the limit spectrum is exactly {γ_n}.

Paper 13's strategy (Sec 3.6) is:

- Gap (i) → ITPFI form convergence (Layer 2) + Teschl Lemma 2.7
  (Layer 4) → Friedrichs extension D_∞ is self-adjoint.
- Gap (ii) → Boegli spectral exactness (Layer 4) plus Hurwitz
  (Layer 5) → spec(D_∞) = {γ_n} with no spurious eigenvalues.

Both strategies are *in principle* the right sort of tool for
closing the respective gaps. Whether Paper 13's execution of each
is rigorous is the subject of points B3, C1, D1 below.

## Does Paper 13 overclaim what CCM did?

I find no overclaim in Paper 13's characterization of CCM. Section
3.4 correctly cites CCM's three Theorem 5.10 conclusions; Section
3.5 correctly identifies the two remaining steps. The paper is
appropriately modest about what is inherited and what is added.

Two mild imprecisions:

1. **"CCM's operators are self-adjoint"** (Sec 1.3) elides the
   T-inner-product subtlety. Self-adjointness is with respect to
   a specific weighted inner product on a quotient. A reader not
   familiar with CCM may think D_N is self-adjoint in the standard
   L² sense, which it is not. This is a matter of exposition rather
   than substance.

2. **"10^{−55} precision at N = 6"** (Sec 3.4) is a numerical
   observation that Paper 13 does not independently reproduce.
   Appendix A.5 is honest: "We have NOT independently reproduced
   this computation." But the headline framing in Section 1 and
   the abstract presents it as established fact.

## Interaction with the even-sector restriction

Paper 13 layers an additional modification (even-sector E_N^+)
that is NOT in CCM. This modification:

- is needed to make the even-simple hypothesis of Theorem 5.10
  hold,
- interacts with the missing-step analysis in a non-trivial way
  (the limit is taken on the *even-sector* Hilbert spaces, not
  the full CCM Sonin spaces),
- requires an analogue of CCM's results on the even sector that
  Paper 13 does not prove.

See A1.01 for the compatibility concern.

## Verdict on this subpoint

**Pass on characterization**: the two gaps are correctly named and
the general strategy is appropriate.

**Conditional on the even-sector analogues**: whether the strategy
*applies* to the modified (even-sector) construction is what
A1.01, A1.03, and B3 interrogate.
