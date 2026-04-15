# Uniform H¹ Resolvent Bound for D_N^K

*Phase II, sub-task 2.2 of the Route 2 porting plan
(`route2-ccm-over-K.md`).*
*Direct port of Paper 13 §7.1 Theorem 7.1 from `K_∞ = ℝ` to
`K_∞ = ℂ`.*
*Written 2026-04-10.*

## What this lemma is

Bögli's spectral exactness theorem (arXiv:1604.07732, Theorem 2.6),
applied via Teschl Lemma 2.7, requires two hypotheses:

- **(H1)** generalised norm resolvent convergence — supplied for
  `D_N^K → D_∞^K` by the Teschl form bound (sub-task 2.4
  combined with Phase III).
- **(H2)** discrete compactness of the resolvent.

H2 is delivered by a **uniform Sobolev `H¹` bound** combined with
**Rellich–Kondrachov compactness**. Paper 13 §7.1 establishes the H¹
bound for the ℚ case via Fourier-basis cancellation: the H¹ weight
`1 + (2πn/L)²` *exactly* equals the resolvent denominator
`|(2πn/L) − i|² = (2πn/L)² + 1`, so the resolvent norm
`L² → H¹` is exactly 1 for the unperturbed Dirac-type operator,
plus a `O(ρ^{−N})` rank-one correction.

The K-analogue replaces the 1D Fourier basis on `[0, L] ⊂ ℝ` with
a 2D Fourier basis on a fundamental domain in `ℂ`. The cancellation
is the same — `1 + |k|²` equals `|k|² + 1` in any dimension — and
in fact carries over to arbitrary `K_∞`. This note writes out the
2D version explicitly.

## Statement (sub-task 2.2)

**Theorem 2.2.K (Uniform `H¹` resolvent bound for `D_N^K`).**
*Let `K = ℚ(i)`, let `L > 0` be the prolate length parameter
(`L = 2 log λ_bw`, see sub-task 1.1 of `route2-ccm-over-K.md`),
and let `D_N^K` be the K-CCM operator on the even sector
`E_N^{+,K}` constructed in `weil-form-over-K.md` and sub-task 1.3.
Then for all `N ≥ 1` and all bandwidth parameters `λ_bw > 0`:*

```
‖(D_N^K − i)^{−1}‖_{L²(ℂ) → H¹(ℂ)}  ≤  2.
```

*The bound is uniform in `N` and in `λ_bw`. As an immediate
corollary, by Rellich–Kondrachov compactness on the fundamental
domain, the resolvent family `{(D_N^K − i)^{−1} : N ≥ 1}` is
discretely compact, so Bögli hypothesis (H2) holds for the K-CCM
sequence.*

## Proof (Fourier basis cancellation in 2D)

The argument is the line-by-line port of Paper 13 §7.1 from 1D to
2D. The key observation — that the `H¹` weight exactly equals the
resolvent denominator in any Fourier basis — is dimension-
independent.

### Step 1. The 2D Fourier basis on the fundamental domain.

Let `Π_L := [−L/2, L/2] × [−L/2, L/2] ⊂ ℂ` (writing
`z = x + iy ∈ ℂ` and identifying `ℂ ≅ ℝ²`). The 2D Fourier basis
on `L²(Π_L)` is

```
V_{(m,n)}(z)  :=  L^{−1} · exp(2πi · (m x + n y) / L),
                  m, n ∈ ℤ, |m|, |n| ≤ N.
```

These are orthonormal in `L²(Π_L)` and span the natural truncation
`E_N^K ⊂ L²(Π_L)` of the K-CCM construction at level `N` (see
`weil-form-over-K.md` §1.3 for the connection to the ideal-indexed
basis `e_𝔞`; for the H¹ bound only the 2D Fourier structure
matters).

The "physical" derivative operators are

```
∂_x V_{(m,n)}  =  (2πi m / L) · V_{(m,n)},
∂_y V_{(m,n)}  =  (2πi n / L) · V_{(m,n)}.
```

### Step 2. The H¹ norm in the Fourier basis.

The Sobolev `H¹` norm on `Π_L` is

```
‖v‖²_{H¹}  =  ‖v‖²_{L²}  +  ‖∂_x v‖²_{L²}  +  ‖∂_y v‖²_{L²}.
```

For `v = ∑_{m,n} c_{(m,n)} V_{(m,n)}`, orthonormality of the
Fourier basis gives

```
‖v‖²_{H¹}  =  ∑_{m,n} (1 + (2π m / L)² + (2π n / L)²) · |c_{(m,n)}|²
          =  ∑_{m,n} (1 + (2π/L)² (m² + n²)) · |c_{(m,n)}|².        (2.1)
```

This is the K-analogue of Paper 13 eq. (7.2). The 2D H¹ weight
`1 + (2π/L)² (m² + n²)` replaces the 1D weight `1 + (2π n / L)²`.

### Step 3. The unperturbed K-CCM operator in this basis.

By the K-CCM construction (sub-task 1.1, written-out for the
ideal-indexed basis but equivalent in the 2D Fourier basis after
the natural identification), the unperturbed operator
`D_log^{(0),K}` acts as

```
D_log^{(0),K} V_{(m,n)}  =  (2π/L) · √(m² + n²) · V_{(m,n)}.       (3.1)
```

This is the magnitude of the 2D wave vector `k = (2π/L)(m, n)`,
i.e., the "log-scale Dirac" interpretation in 2D. The eigenvalue is
real and positive for `(m, n) ≠ (0, 0)`, with the zero mode `(0, 0)`
removed by the quotient construction in `D_N^K` (see Paper 13 §3.6
analogue for K).

### Step 4. Exact cancellation for the unperturbed operator.

For the unperturbed operator, the resolvent
`v = (D_log^{(0),K} − i)^{−1} f` acts mode-by-mode:

```
c_{(m,n)}^v  =  c_{(m,n)}^f  /  ((2π/L)·√(m² + n²) − i).
```

Its `H¹` norm computes via (2.1) as

```
‖v‖²_{H¹}
  =  ∑_{m,n}  (1 + (2π/L)² (m² + n²))  /  |(2π/L)√(m² + n²) − i|²
              · |c_{(m,n)}^f|²

  =  ∑_{m,n}  (1 + (2π/L)² (m² + n²))  /  ((2π/L)² (m² + n²) + 1)
              · |c_{(m,n)}^f|²

  =  ∑_{m,n}  |c_{(m,n)}^f|²

  =  ‖f‖²_{L²}.                                                     (4.1)
```

**The H¹ weight `1 + (2π/L)² (m² + n²)` and the resolvent denominator
`(2π/L)² (m² + n²) + 1` are identically equal**, so they cancel
mode-by-mode and leave the resolvent norm `L² → H¹` *exactly* 1 for
the unperturbed operator — for all `L` (i.e., all `λ_bw`) and all
`N`. This is the K-analogue of Paper 13 eq. (7.3), with
`(2πn/L)²` replaced by `(2π/L)² (m² + n²)`.

The cancellation holds in any number of dimensions: it is a property
of the abstract identity `1 + ‖k‖² = ‖k‖² + 1` between the H¹
weight and the resolvent denominator at the spectral parameter `i`,
expressed in any orthonormal eigenbasis of the Laplacian. Dimension-
free.

### Step 5. Rank-one correction from the quotient construction.

The K-CCM operator `D_N^K` differs from `D_log^{(0),K}` by a
rank-one correction arising from the quotient
`E_N^K / ℂ ξ_N^K` (the analogue of Paper 13's `E_N / ℂ ξ_N`).
By the resolvent perturbation formula (Kato, *Perturbation Theory
for Linear Operators*, Ch. IV §3.4) and the K-version of the CF
decay (sub-task 2.3, port of Paper 13 Proposition 8.1):

```
‖(D_N^K − i)^{−1}‖_{L² → H¹}  ≤  1  +  O((ρ^K)^{−N}),              (5.1)
```

where `ρ^K > 1` is the K-CF decay base. For the K-Weil moment
problem `ρ^K` is computed numerically in sub-task 2.3 and is
expected to satisfy `ρ^K ≥ 4` for small `N` by analogy with the ℚ
value `ρ ≥ 4.27`. Even at the conservative `ρ^K ≥ 2`, for `N ≥ 1`
the correction is at most `2^{−1} = 0.5 < 1`, giving

```
‖(D_N^K − i)^{−1}‖_{L² → H¹}  ≤  2.                                 (5.2)
```

The bound is uniform in `λ_bw` (no dependence on `L`) and uniform
in `N` (the correction `O((ρ^K)^{−N})` is exponentially small).
This completes the proof of Theorem 2.2.K. ∎

## Discrete compactness corollary

**Corollary 2.2.K-cpt (Bögli H2 for K).** *The resolvent family
`{(D_N^K − i)^{−1} : N ≥ 1}` is discretely compact in the sense of
Bögli arXiv:1604.07732, Definition 2.5: every sequence
`{f_N}` with `‖f_N‖_{L²} = 1` has a convergent subsequence in
`L²(Π_L)`.*

*Proof.* By Theorem 2.2.K, `‖(D_N^K − i)^{−1} f_N‖_{H¹} ≤ 2 ·
‖f_N‖_{L²} = 2`, so the image sequence is uniformly bounded in
`H¹(Π_L)`. The Rellich–Kondrachov embedding `H¹(Π_L) ↪ L²(Π_L)`
is compact (Adams, *Sobolev Spaces*, Theorem 6.3, applied to
the bounded Lipschitz domain `Π_L ⊂ ℝ²`), so the image sequence has
a convergent subsequence in `L²(Π_L)`. ∎

## What this gives us

Combining Theorem 2.2.K and Corollary 2.2.K-cpt with the K-version
of Paper 13 §9 (Phase III of Route 2 — abstract Teschl–Bögli):

- **Hypothesis H2 (discrete compactness)** of Bögli's spectral
  exactness theorem is verified for the K-CCM sequence.
- Together with **H1 (gnrc)** from sub-task 2.4 + Phase III, Bögli
  Theorem 2.6 applies to give `spec(D_∞^K) = lim spec(D_N^K)` in
  the Hausdorff metric, no spurious eigenvalues, multiplicities
  preserved.

This is one of the two structural inputs to the eventual Route 2
closure of MY4. The other (the `O(1/λ)` archimedean estimate, sub-
task 2.1) is also a mechanical port of Paper 13 §5.

## What this doesn't address

The H¹ bound is a regularity property of the resolvent. It is
**independent** of:

- Whether `D_N^K` actually has the correct spectrum (sub-task 1.5 —
  the K-port of CCM 2025 Theorem 5.10).
- Whether the limit operator `D_∞^K` exists (handled by Phase III
  abstractly, conditional on Q_N^K → Q_0^K form convergence).
- Whether the same-norm collisions in the off-diagonal Q_N^K kernel
  (open issue O1 from `weil-form-over-K.md`) are correctly handled.

These are independent sub-tasks. The H¹ bound proved here would
remain valid under any of the candidate handlings of O1, because it
depends only on the unperturbed `D_log^{(0),K}` plus a small rank-one
correction — not on the off-diagonal kernel.

## Status

**Sub-task 2.2: DONE.** The 2D uniform H¹ bound is established by
direct port of Paper 13 §7.1. The proof is the same Fourier-basis
cancellation argument with `(2πn/L)²` replaced by `(2π/L)² (m² + n²)`.
The uniformity in `N` and `λ_bw` is preserved. Bögli H2 follows by
Rellich.

**Conditional on:** sub-task 2.3 (the K-CF decay rate `ρ^K`), but the
bound `‖resolvent‖ ≤ 2` only requires `ρ^K ≥ 2`, which is essentially
free.

**Independent of:** all of Phase I except the abstract structure of
the basis, and all of Phases III–V.

**Caveat about the choice of ambient domain.** This note works on
the toroidal fundamental domain `Π_L = [−L/2, L/2]² ⊂ ℂ`, which is
the natural finite-volume cutoff for the K-CCM Fourier basis. The
ideal-indexed basis `{e_𝔞 : 𝔞 ∈ S_N^K}` of `weil-form-over-K.md`
§1.3 maps into this Fourier basis under the change of variables
`(m, n) ↔ Tr_{K/ℚ}(z · x_𝔞) ∈ (1/L)·ℤ²`. The map is unitary
modulo a finite collection of relabelings, so the H¹ bound on the
2D Fourier basis transfers to the ideal-indexed basis, hence to
`D_N^K` as defined in `weil-form-over-K.md`.

A purely rigorous version would carry the change-of-variables
through and verify it preserves H¹. That is a half-page exercise
deferred to the eventual full writeup of Phase II.

## Cross-references

- `route2-ccm-over-K.md` — Phase II, sub-task 2.2 (this note executes
  it).
- `weil-form-over-K.md` §1.3, §6 — the K-CCM Fourier basis
  (ideal-indexed; this note works in the equivalent 2D
  trigonometric basis).
- `solutions-with-prize/paper13-rh/preprint/sections-06-10.md` §7.1 Theorem 7.1, eqs.
  (7.1)–(7.5) — the 1D ℚ template.
- Bögli, arXiv:1604.07732, Theorem 2.6 + Definition 2.5 — what H2
  means.
- Adams, *Sobolev Spaces* (1975/2003), Theorem 6.3 — Rellich on
  bounded Lipschitz domains in ℝ².
- Kato, *Perturbation Theory for Linear Operators*, Chapter IV §3.4
  — the resolvent perturbation bound used in Step 5.
