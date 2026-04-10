# D1.02 — Logical Structure

## Is it a direct proof or a proof by contradiction?

Paper 13 presents the proof as **direct**: construct operators,
prove convergence, identify the limit spectrum with {γ_n},
conclude reality. Not a contradiction argument.

From Paper 13 Sec 10 (D1 overall): "The proof is NOT a proof by
contradiction."

## Does the direct structure actually work for RH?

**For a direct proof to give RH**, it must show that *every*
non-trivial zero of ζ is on the critical line. A direct proof
usually does this via:

- A one-to-one correspondence between zeros of ζ and some set
  known to be real, OR
- An explicit construction that enumerates all zeros as real
  numbers, OR
- A spectral interpretation where all zeros appear as real
  eigenvalues of a self-adjoint operator.

Paper 13 aims for the third. The claim is:

  spec(D_∞) = {γ_n}, where {γ_n} are imaginary parts of ALL
  non-trivial zeros of ζ (not just those on the critical line).

**If** this identification is established, **and** D_∞ is self-
adjoint (hence real spectrum), then all γ_n are real.

**But** Paper 13's Section 1 notation defines {γ_n} as imaginary
parts of **critical-line** zeros only. Under this definition, the
final conclusion "γ_n ∈ ℝ" is trivial and does not exclude
off-line zeros.

## Which definition is in force?

The conflict:

- Section 1 notation: {γ_n} = imaginary parts of critical-line
  non-trivial zeros.
- Section 10.3 Theorem 10.2 conclusion: "eigenvalues of D_N
  converge to {γ_n}".
- Section 10.4 Step 4: "{γ_n} = spec(D_∞) ⊂ ℝ. Therefore
  γ_n ∈ ℝ for all n."

If {γ_n} is by definition imaginary parts of critical-line zeros,
then "γ_n ∈ ℝ" is tautological. This is not a proof.

If {γ_n} is the set of imaginary parts of **all** non-trivial
zeros (including hypothetical off-line ones), then "γ_n ∈ ℝ" is
substantive — it says off-line zeros don't exist. But this is
not what Section 1 says.

**The paper's notation and its conclusion are inconsistent.**
Either:

(A) The Section 1 definition is too narrow and should cover all
    non-trivial zeros, in which case the Hurwitz argument
    substantively delivers RH.

(B) The Section 1 definition is the correct "only critical-line
    γ_n", and the Section 10.4 Step 4 deduction is tautological
    and does not prove RH.

Under interpretation (A), the argument works **if** the Hurwitz
limit statement "spec(D_N) → {γ_n}" is interpreted as "in the
complex plane, zeros of ξ̂_N accumulate at complex zeros of Ξ,
and since zeros of ξ̂_N are real, the complex zeros of Ξ must be
real". This is the implicit-correct version.

Under interpretation (B), the argument does not prove RH.

**Paper 13 does not make the choice explicit.** Section 10.4 is
ambiguous, and the natural reading (given the Section 1 notation)
is the tautological one.

## The fix

Rewrite Section 10.4 to make the logical step explicit:

1. Define Ξ(z) as the Riemann Xi function. Its zeros in
   {|Im z| < 1/2} are in bijection with non-trivial zeros of ζ
   in the critical strip 0 < Re s < 1 via s = 1/2 + iz.

2. Lemma: ξ̂_N has only real (complex-plane) zeros. Proof: CCM
   Theorem 5.10(iii) + explicit sine-times-rational formula.

3. Theorem: ξ̂_N → Ξ uniformly on compact subsets of
   {|Im z| < 1/2}. Proof: Layers 3-4, Hurwitz chain.

4. Conclusion: By Hurwitz, every zero of Ξ in {|Im z| < 1/2} is
   a limit of zeros of ξ̂_N, hence a limit of real numbers, hence
   real. Therefore every non-trivial zero of ζ in the critical
   strip has Im(1/2 − s) = 0, i.e., Re s = 1/2. QED.

This is the correct direct proof. Paper 13 has all the
ingredients but does not assemble them this way.

## Verdict on this subpoint

**The logical structure is sound in principle** but **not
properly expressed in the preprint**. The argument as written is
either tautological or incomplete; the correct argument requires
Hurwitz in the complex plane plus the real-zero property of
ξ̂_N, neither of which is explicit.

This is the single most important exposition fix the paper
requires.
