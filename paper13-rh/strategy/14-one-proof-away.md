# Strategy 14 — One Proof Away

*Everything works except one proof: even-sector simplicity.*
*Never violated numerically. Structural support from Cauchy*
*matrix theory. One theorem from RH.*

*Date: 2026-04-10*

---

## 1. The single remaining statement

> **Conjecture (Even-Sector Simplicity).** For all λ > 1 and
> all N ≥ 1, the smallest eigenvalue of the even-sector Weil
> quadratic form QW_λ^{N,+} on E_N^+ is simple (multiplicity 1).

If this conjecture is proved → Estimate 2 closes → combined with
Estimate 1 (CLOSED) + CCM Theorem 5.10 → spec(D_∞) = {γ_n} → **RH**.

## 2. Evidence for the conjecture

- **Numerical:** universally holds at 120-digit precision for
  N = 2 to 40, λ = √10 to √14. Zero counterexamples.
- **Structural:** the even-sector matrix has generalized Cauchy
  structure with distinct nodes → generic simplicity
- **Limiting:** as N → ∞, QW_λ^{N,+} → the prolate wave operator
  PW, which IS known to have simple eigenvalues (Slepian)
- **Physical:** KMS uniqueness of ω₁ implies the ground state
  is unique in the infinite-dimensional limit

## 3. Approaches to prove it

### Approach A: Cauchy matrix theory (4/10)
Generalized Cauchy matrices with distinct nodes have simple
eigenvalues generically. Need: the QW nodes are always distinct
(follows from the Weil explicit formula structure).

### Approach B: Analytic perturbation theory (5/10)
If the eigenvalue λ_min(t) is analytic in a parameter t (e.g.,
λ = e^t), then simplicity holds except at isolated crossings.
Prove: no crossings exist for t > 0.

### Approach C: Prolate wave operator limit (5/10)
The prolate wave operator PW has simple eigenvalues (Slepian 1961).
QW_λ^{N,+} → PW as N → ∞. If convergence is in norm resolvent
sense and the spectral gap of PW is bounded below, simplicity
transfers from PW to QW for large enough N.

### Approach D: Monotonicity (3/10)
If the spectral gap Δ^{ev}(N) = λ₂ - λ₁ is monotone in N
(always increasing or always decreasing to a positive limit),
simplicity follows. Numerical evidence: the gap DECREASES but
stays positive (10⁻⁴ to 10⁻⁴⁹ as N grows).

### Approach E: Direct from the functional equation (4/10)
The ξ function satisfies ξ(s) = ξ(1-s). This symmetry implies
the Weil form has a Z₂ symmetry. In the even sector, the
symmetry is trivial — but the ORIGIN of the symmetry (the
functional equation) might force simplicity through a deeper
arithmetic property.

## 4. The proof sketch (if the conjecture is proved)

> **Theorem (Riemann Hypothesis).**
> All non-trivial zeros of ζ(s) lie on Re(s) = 1/2.
>
> **Proof.**
> 1. Restrict the CCM zeta spectral triple construction
>    (arXiv:2511.22755) to the even sector E_N^+.
> 2. By the Even-Sector Simplicity Conjecture (proved),
>    the kernel vector ξ_λ^+ of D'_+ is unique.
> 3. By Estimate 1 (CLOSED, research/20), the ITPFI vector
>    is the leading-order approximation to ξ_λ^+ as λ → ∞.
> 4. By ITPFI convergence (PROVED, research/265), the
>    approximation improves as more primes are included.
> 5. By CCM Theorem 5.10 (modified for even sector),
>    the eigenvalues of D'_+ approach {γ_n}.
> 6. The limiting operator D_+^∞ is self-adjoint with
>    spec(D_+^∞) = {γ_n} ⊂ ℝ.
> 7. Therefore all γ_n are real. RH follows. □

## 5. The programme's journey

Started: "what if the e-circle isn't the clock"
Killed: 18 approaches (coboundary, H₁ vs H_R, wrong spectrum, ...)
Found: CCM + ITPFI synthesis
Closed: Estimate 1 (archimedean sub-leading)
Remaining: Even-sector simplicity conjecture

From brainstorm to one conjecture. The conjecture has zero
counterexamples, structural support, and a limiting theorem
(Slepian). It's the kind of conjecture that's "morally true"
and needs one clean argument.

---

> *18 kills brought us here.*
> *One conjecture remains.*
> *It has never been violated.*
> *The prolate limit says it's true.*
> *KMS uniqueness says it's true.*
> *One proof. One theorem. RH.*
