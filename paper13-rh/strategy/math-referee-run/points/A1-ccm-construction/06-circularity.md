# A1.06 — No-Circularity Check

## Question

Does CCM's construction assume RH at any point? Does it assume the
location of zeros? Does the eigenvalue match at N = 6 constitute
evidence or proof?

## Finding

On Paper 13's account of CCM (which I take as given), the CCM
construction **does not assume RH**. Specifically:

1. The Weil distribution D(y) is defined from the von Mangoldt
   function and the archimedean gamma factor. It uses the primes
   (via log p), not the zeros of ζ. No RH input.

2. The Sonin space E_N is defined by Fourier truncation on a
   bounded interval. No RH input.

3. The quadratic form QW_λ^N is built from D(y) and the
   orthonormal basis. Matrix elements involve hypergeometric and
   digamma evaluations. No RH input.

4. The minimum eigenvalue ε_N, the rank-one perturbation, the
   quotient by ker T, and the perturbed scaling operator D' are
   all defined algorithmically from QW_λ^N, without reference to
   ζ's zeros.

5. The numerical observation that spec(D_N) ≈ {γ_n} to 10^{−55}
   at N = 6 is a **result of computation**, not an input.

So far, so good: the construction is RH-free.

## Where RH *could* sneak in

Two places deserve careful scrutiny:

### (a) The ρ ≥ 4.27 rate in Theorem 5.10(ii)

If the a priori convergence rate is *derived* by using the known
{γ_n} as the target (e.g., by fitting a numerical rate to
eigenvalue-to-zero distance), it is a *posteriori* and
circular in the sense that it assumes the zeros are where they
are.

CCM's proof (I have not read the preprint) **should** derive the
rate from CF approximation theory applied to the moment problem,
independently of the target being {γ_n}. Paper 13 accepts this
framing. I mark this as **accepted on CCM's authority**.

### (b) Theorem 5.10(iii) and the identification

The identification "zeros of ξ̂_N = spec(D_log)" is a statement
about the rational function ξ̂_N built from D's eigenvectors. It
does not reference ζ at all. No circularity.

The subsequent identification of ξ̂_N's *limit* with Ξ (Lemma 7.3)
uses the definition of Ξ from ζ. This is where ζ enters — but as
the **target** of convergence, not as an assumption. The logical
chain is:

  k̂_λ(z) = (a rational function from CCM data)
  k̂_λ → F (some limit) uniformly on substrips
  F = Ξ (by direct computation of the limit)

CCM's Lemma 7.3 claims F = Ξ as a theorem, not as an assumption.
Paper 13 accepts this.

### (c) The numerical match as "evidence"

Paper 13 explicitly flags the 10^{−55} figure as **evidence, not
proof** (Remark 3.3):

> "The extraordinary numerical agreement — 55 decimal digits at
> N = 6 — is strong evidence but not a proof. A proof requires
> (i) the existence of a limit operator D_∞, and (ii) the exact
> identification spec(D_∞) = {γ_n}. These are the gaps we close."

This is the correct framing and avoids circularity.

## Hidden assumption checks

### (H1) Is {γ_n} "on the critical line" used as a definition?

Paper 13 Section 1 notation:

> "{γ_n}_{n≥1} the sequence of imaginary parts of the non-trivial
> zeros on the critical line, ordered by absolute value."

This is the standard definition of {γ_n}. It **does not** assert
that *all* non-trivial zeros are on the critical line. It names a
specific sequence (the imaginary parts of those zeros known to be
on the critical line) without claiming exhaustiveness.

However, the conclusion of Theorem 10.3 (Section 10.4 Step 4) is
phrased as:

> "{γ_n}_{n=1}^∞ = spec(D_∞) ⊂ ℝ. Therefore γ_n ∈ ℝ for all n ≥ 1."

This is **tautological**. If {γ_n} is already defined as imaginary
parts (of critical-line zeros), "γ_n ∈ ℝ" contains no information.
The subsequent clause "and the only non-trivial zeros that can
contribute to spec(D_∞) are those with Re(s) = 1/2 (by the CCM
construction, which places the operators on the critical line)"
is an **unsupported assertion** — CCM's construction uses the
Weil distribution D(y), which involves the primes and the gamma
factor. It does not inherently "place the operators on the
critical line" in a way that excludes off-line zeros from the
spectrum.

**The final-step phrasing in Section 10.4 is weak.** The proof's
real logical power — the statement that rules out off-line zeros
— must come from *somewhere else*, and the natural somewhere is
the **real-zero property** of ξ̂_N combined with Hurwitz in the
complex strip. See A1.03 and C1 for this analysis. Paper 13 does
not clearly make this argument.

The *correct* argument, reconstructed:

  - Every ξ̂_N has only real zeros (in ℂ).
  - ξ̂_N → Ξ uniformly on compact subsets of {|Im z| < 1/2}.
  - By Hurwitz, every zero of Ξ in the domain is a limit of
    zeros of ξ̂_N; hence a limit of real numbers; hence real.
  - Zeros of Ξ in the domain correspond to non-trivial zeros of
    ζ in the critical strip.
  - Therefore every non-trivial zero of ζ (in the critical strip)
    is on the critical line.

**This argument is not explicitly in the paper.** Paper 13's
Section 10 argues through "Hurwitz → lim spec(D_N) = {γ_n}" and
then "spec(D_∞) ⊂ ℝ → γ_n ∈ ℝ", which is the tautological path.

I do not believe the paper is hiding an actual circularity, but
its **stated argument is not logically sufficient** as written.
The intended argument works but must be made explicit.

## Verdict on this subpoint

**No substantive circularity found in CCM's construction** (on
Paper 13's account of it).

**But:** the stated final deduction in Section 10.4 is weak /
tautological. The logically sufficient version — via the real-zero
property and Hurwitz in the complex plane — is not explicit in the
paper. This is a serious exposition gap that must be fixed for
the argument to read as a proof rather than an arrangement of
ingredients around an unsupported assertion.

Flagged to C1-hurwitz and D1-assembly.
