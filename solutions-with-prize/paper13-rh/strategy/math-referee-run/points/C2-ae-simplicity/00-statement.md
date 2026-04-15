# C2 — AE Simplicity [MEDIUM]

## The claim

CCM Theorem 5.10 requires the minimum eigenvalue ε_N of QW_λ^N to
be (i) simple and (ii) even. The "even-simple" hypothesis. Paper
13 Section 12 supplies this via an "AE simplicity" argument:

1. Restrict to the even sector E_N^+ from the outset; the minimum
   is then automatically even.

2. Prove simplicity: the minimum eigenvalue of A^{ev}(λ, N) is
   simple for all λ except possibly a discrete exceptional set
   S_N. This is "almost-everywhere simplicity" (AE).

3. AE suffices because the proof chain only requires simplicity
   at **one** λ (not all); any choice outside S_N works.

## The mechanism

Paper 13 Section 12.2:

- Define the "overlap function" f_N(λ) := ⟨φ_0(λ) | a(λ)⟩ where
  φ_0 is the ground eigenvector of A^{ev} and a is the
  archimedean cosine-basis vector.

- f_N is real-analytic in λ (Kato–Rellich) and a(λ) is a rational
  function of L = 2 log λ.

- If f_N(λ_0) ≠ 0 at a single point λ_0, the identity theorem
  says {f_N = 0} is discrete.

- AE simplicity fails at most on {f_N = 0}, which is discrete.

- At λ_0 = √14, the paper certifies f_N(√14) ≠ 0 to 120-digit
  precision for N = 1, ..., 20.

- For N > 20, the paper invokes a "Slepian limit" argument: as
  N → ∞, the even-sector matrix converges to a prolate spheroidal
  wave operator whose ground state has a positive overlap with
  the archimedean cosine vector.

## Why MEDIUM

The argument is largely structural and numerical. The structural
part (identity theorem, Kato–Rellich analyticity) is standard. The
numerical certification at N = 1, ..., 20 is careful (120-digit
precision, 10^{72} safety margin). The "Slepian limit" extension
to N > 20 is the weakest link.
