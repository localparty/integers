# C1 — Hurwitz Application [MEDIUM]

## The claim (Section 10)

Theorem 10.1: ξ̂_λ → c · Ξ uniformly on compact subsets of
{|Im z| < 1/2}.

Theorem 10.2: the eigenvalues of D_N converge to {γ_n}, via
Hurwitz's 1893 theorem applied to the Fourier transforms.

## The underlying logic (as I reconstruct it)

The crucial facts:

1. Each ξ̂_N is a holomorphic (or meromorphic after cancellation)
   function in the strip |Im z| < 1/2.

2. Each ξ̂_N has **only real zeros in the complex plane** — this
   follows from CCM Theorem 5.10(iii) (zeros = real eigenvalues
   of a self-adjoint operator) plus the sine-factor structure.

3. ξ̂_N → Ξ uniformly on compact subsets of {|Im z| < 1/2}.

4. Ξ is not identically zero (Ξ(0) ≠ 0).

5. **Hurwitz's theorem** then says: every zero of Ξ inside
   {|Im z| < 1/2} is a limit of zeros of ξ̂_N, hence a limit of
   real numbers, hence real.

6. Zeros of Ξ in {|Im z| < 1/2} correspond via the substitution
   s = 1/2 + iz to zeros of ζ in the critical strip 0 < Re s < 1.

7. Therefore every non-trivial zero of ζ is real in z-coordinates,
   i.e., Re s = 1/2. RH.

This is the **correct** proof architecture and it works **if** the
facts 1–4 hold. The key is that step 5 uses Hurwitz in the
**complex** plane and not just on the real line — it is the
complex-analytic obstruction to off-line zeros that forces the
conclusion.

## What Paper 13 actually writes

Paper 13 Section 10.4 does NOT clearly make the above argument.
It writes:

> "Step 4: {γ_n} = spec(D_∞) ⊂ ℝ. Therefore γ_n ∈ ℝ for all n.
> Since γ_n = Im(s_n) where s_n = 1/2 + iγ_n parametrises the
> non-trivial zeros of ζ on the critical line, and the only
> non-trivial zeros that can contribute to spec(D_∞) are those
> with Re(s) = 1/2 (by the CCM construction, which places the
> operators on the critical line), we conclude: all non-trivial
> zeros of ζ satisfy Re(s) = 1/2."

This is tautological as stated:
- "γ_n" are *defined* as imaginary parts of critical-line zeros
  (Sec 1 notation). "γ_n ∈ ℝ" contains no information.
- "the only non-trivial zeros that can contribute to spec(D_∞)
  are those with Re(s) = 1/2" is **asserted**, not proved.

The *real* argument — using Hurwitz to exclude off-line zeros via
the real-zero property of ξ̂_N — is never explicitly stated.

## Why this matters

The gap between Paper 13's stated final step and the logically
sufficient version is not just an exposition issue. Without the
explicit "ξ̂_N has only real zeros" invocation plus Hurwitz in
the complex plane, the proof does not rule out complex zeros of
Ξ in the strip, and hence does not rule out off-line zeros of ζ.

A careful referee would require Section 10.4 to be rewritten to
make the correct argument explicit.

## Why MEDIUM (not HEAVY)

The correct argument exists and is natural — Hurwitz on Fourier
transforms of real-zero-only eigenvector Fourier transforms is
the textbook way to run this. The paper's flaw is exposition, not
substance. The fix is clear and the referee can supply it.

But because the substance of the proof depends on a property
(real-zero property of ξ̂_N) that the paper never explicitly
invokes, this is a real issue rather than a stylistic one.
