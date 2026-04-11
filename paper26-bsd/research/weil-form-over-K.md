# The Weil Quadratic Form Q_N^K over K = Q(i)

*Phase I, sub-task 1.2 of the Route 2 porting plan
(`route2-ccm-over-K.md`).*
*Definition + basic properties writeup, not a convergence proof.*
*Written 2026-04-10.*

## 0. Scope

K-analogue of Paper 13 §3.3's Weil quadratic form `Q_N`, with
`K = Q(i)`. Off-diagonal, diagonal, archimedean, rank-2, parity,
even sector. Definitions + basic properties only — not a proof
that `D_N^K` is self-adjoint (sub-task 1.3) or has the right
spectrum (sub-task 1.5).

References ported from:
- Paper 13 §3.3 (`Q_N`), §3.4 (parity), and §6.1 eq. (6.1)–(6.2)
  for the decomposition `QW_λ = T_0 + τ^(R)` with
  `T_0 = τ^(0,2) + Σ_p τ^(p)`.
- `meyer-extension-to-K.md` (M3') for the explicit formula for
  `ζ_K` (provides the diagonal data).
- CCM 2025, arXiv:2511.22755, §4–5.

## 1. Setup

### 1.1. Gaussian prime enumeration (cited, not reproduced)

The first `N` Gaussian primes ordered by absolute norm are
enumerated by `paper26-bsd/referee/code/ccm_over_K_sanity.py`,
function `gaussian_primes_by_norm(max_norm)`. The convention there:

- The ramified prime `(1+i)` of norm `2` is listed once.
- For each rational prime `p ≡ 1 mod 4`, the **two** split factors
  `(a + bi)` and `(a − bi)` (each of norm `p`) are listed
  separately as ordered pairs.
- For each rational prime `p ≡ 3 mod 4`, the inert prime `(p)` of
  norm `p²` is listed once.

The first ten by norm (output of the script):

```
  rank  prime         norm   type
  ----  ------------  ----   ----
   1    (1 + 1i)       2     ramified
   2    (1 + 2i)       5     split
   3    (1 − 2i)       5     split
   4    (3 + 0i)       9     inert
   5    (2 + 3i)      13     split
   6    (2 − 3i)      13     split
   7    (1 + 4i)      17     split
   8    (1 − 4i)      17     split
   9    (2 + 5i)      29     split
  10    (2 − 5i)      29     split
```

Norm `9` is the first inert square; norms `5, 13, 17, 29, …` are
split pairs. The script `ccm_over_K_sanity.py` is the canonical
source — this note refers to it rather than re-deriving. Let `𝔭_1,
𝔭_2, …, 𝔭_N` denote that ordering.

### 1.2. The truncation set S_N^K

Define

```
S_N^K  :=  { 𝔞 ⊂ 𝒪_K nonzero : 𝔭 | 𝔞 ⇒ N(𝔭) ≤ Q_N },
```

where `Q_N := N(𝔭_N)`. By unique factorization in `𝒪_K = ℤ[i]`,
`S_N^K ≅ ℕ^N` via `𝔞 = 𝔭_1^{a_1} ⋯ 𝔭_N^{a_N} ↔ (a_1, …, a_N)`,
and `N(𝔞) = ∏_i N(𝔭_i)^{a_i}`. This is the K-analogue of the
`N`-smooth positive integers `S_N` of Paper 13 §3.3 / CCM 2025 §4.
The structural difference from ℚ: distinct prime ideals can have
the same norm (split pairs), so the norm is not injective on
`S_N^K`. This is the source of the same-norm issue (§2.2).

### 1.3. The Fourier basis

For each `𝔞 ∈ S_N^K` define a basis vector `e_𝔞 ∈ L²(K_∞) = L²(ℂ)`
following sub-task 1.1 of the porting plan:

```
e_𝔞(z) := N(𝔞)^{−1/2} · exp(2πi · Tr_{K/ℚ}(z · x_𝔞) / L)
```

where `x_𝔞 ∈ K_∞ = ℂ` is a canonical generator of `𝔞` (chosen
in the fundamental domain `{a + bi : a > 0} ∪ {bi : b > 0}`),
`Tr_{K/ℚ}(w) = 2 Re(w)`, and `L = 2 log(λ_bw)` is the prolate
bandwidth length parameter (Paper 13 §3.1; sub-task 1.1). Different
section choices change `e_𝔞` by an overall phase, which cancels in
the matrix entries of `Q_N^K`. The truncated Hilbert space is

```
E_N^K  :=  span{ e_𝔞 : 𝔞 ∈ S_N^K }  ⊂  L²(ℂ).
```

## 2. The off-diagonal, logarithmic part

### 2.1. Naive form (port of Paper 13 §3.3)

The K-analogue of the Paper 13 off-diagonal piece is

```
Q_N^K(f, g)|_off-diag  =
   Σ_{𝔞, 𝔟 ∈ S_N^K, N(𝔞) ≠ N(𝔟)}
        ⟨f, e_𝔞⟩ ⟨e_𝔟, g⟩  /  log(N(𝔟) / N(𝔞))                 (2.1)
```

The restriction is `N(𝔞) ≠ N(𝔟)` rather than `𝔞 ≠ 𝔟` because of
the same-norm issue (§2.2). Over ℚ, Paper 13 §3.3 has
`Σ_{m ≠ n} ⟨f, e_m⟩⟨e_n, g⟩ / log(n/m) + (diagonal)` and the
condition `m ≠ n` is the same as different norms because the norm
on `S_N` is the identity. Over `K` the two conditions diverge,
which is the point of §2.2.

### 2.2. The same-norm issue

If `𝔞 ≠ 𝔟` but `N(𝔞) = N(𝔟)` then `log(N(𝔟)/N(𝔞)) = 0` and the
naive coefficient `1/log(N(𝔟)/N(𝔞))` is undefined. This happens
already at level `N = 2` for the split pair `(1 + 2i)` and
`(1 − 2i)`, both of norm 5, and it is the **first genuinely new
phenomenon** in the K-port that has no analogue over ℚ.

Two candidate handlings:

**Option A — restrict to N(𝔞) ≠ N(𝔟).** Drop same-norm pairs from
the off-diagonal sum entirely, as in (2.1). The form is then
well-defined. Justification: the right-hand side of (M3') sums over
**prime ideals** `𝔭` weighted by `log N(𝔭) / √N(𝔭)`, with each
split factor `𝔭` contributing its own term — so at the prime-power
layer the form already separates split partners through the
**diagonal** kernel (§3). The off-diagonal log-kernel only sees
non-prime-power composites like `(1 + 2i)(2 + 3i)` vs.
`(1 − 2i)(2 − 3i)` (both of norm 65), and discarding those pairs
appears to be consistent with how the explicit formula assigns
weight to each ideal class.

**Option B — secondary ordering / regularization.** Replace the
single parameter `log N(𝔞)` by `(log N(𝔞), σ(𝔞))` with a
tie-breaker `σ : S_N^K → ℝ` (e.g., `σ(𝔞) = arg(x_𝔞) mod π`,
distinguishing `(1 + 2i)` from `(1 − 2i)` by complex argument).
The denominator becomes `log(N(𝔟)/N(𝔞)) + iε(σ(𝔟) − σ(𝔞))` and
the limit `ε → 0` gives a principal-value distribution. Cost: the
`iε` regulator breaks manifest reality of the kernel and must be
taken inside the operator construction.

**Recommendation.** Use Option A for the writeup. Revisit only if
a small-`N` numerical experiment with a `D_N^K` matrix shows that
ignoring same-norm pairs corrupts the spectrum relative to the
ground-truth zeros of `ζ_K` from `ccm_over_K_sanity.py`.

## 3. Diagonal terms from the explicit formula for ζ_K

The diagonal of `Q_N^K` is read off the right side of the explicit
formula (M3') in `meyer-extension-to-K.md`. For test functions
`f, g ∈ E_N^K`, the diagonal contribution is

```
Q_N^K(f, f)|_diag  =
   Σ_{𝔞 ∈ S_N^K}  Λ_K(𝔞) · |⟨f, e_𝔞⟩|² / N(𝔞)^{1/2}
   + (archimedean correction τ^{(K_∞)}, see §4)                  (3.1)
```

where the **Dedekind–Mangoldt function** `Λ_K` is

```
Λ_K(𝔞)  =  log N(𝔭)   if 𝔞 = 𝔭^k for some prime ideal 𝔭 and k ≥ 1
       =  0           otherwise.                                  (3.2)
```

This is the pure prime-power-supported part of the right side of
(M3'). Cite: Weil 1952 (*Sur les "formules explicites" de la
théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund); Landau
1917 for `ζ_K`. The sesquilinear extension to `f, g`:

```
Q_N^K(f, g)|_diag  =
   Σ_{𝔞 ∈ S_N^K}  Λ_K(𝔞) · ⟨f, e_𝔞⟩ ⟨e_𝔞, g⟩ / N(𝔞)^{1/2}
   + (archimedean).                                               (3.3)
```

The diagonal kernel is real, positive, manifestly self-adjoint,
and bounded below by 0 on `E_N^K`.

**Compatibility with Paper 13.** Over ℚ, the analogous diagonal is
`Σ_n Λ(n) |⟨f, e_n⟩|² / √n`, which is exactly the prime-power sum
on the right side of Riemann–Weil (M3) — see Paper 13 §6.1, eq.
(6.2), where this part is called `T_0 = τ^(0,2) + Σ_p τ^(p)`. The
K-version is the direct substitution `n → 𝔞`, `Λ → Λ_K`, `√n →
√N(𝔞)`. No new ideas.

## 4. The archimedean term τ^{(K_∞)}

### 4.1. Origin

For `K = ℚ(i)` (one complex place, `r_2 = 1`, no real places), the
gamma factor at the complex place is `Γ_C(s) := 2 (2π)^{−s} Γ(s)`
and the completed zeta is `Λ_K(s) = 4^{s/2} · 2^{1−s} π^{−s} Γ(s)
· ζ_K(s)` (Hecke 1917; (M2') of `meyer-extension-to-K.md`). The
"archimedean contribution" on the test-function side of the
Riemann–Weil explicit formula (M3') is the Mellin pairing of `h`
against the logarithmic derivative of `Γ_C` along `Re(s) = 1/2`.

### 4.2. The archimedean Weil distribution

By the standard derivation (Weil 1952 §III; Iwaniec–Kowalski
Theorem 5.12), this one-complex-place contribution is

```
τ^{(K_∞)}(h)  =  −(1/2π) ∫_{−∞}^∞  h(u) ·
                  [ ψ(1/2 + iu) + ψ(1/2 − iu) − 2 log(2π) ] du   (4.2)
```

where `ψ(s) := Γ'(s)/Γ(s)` is the digamma function. The digamma
argument is `1/2 ± iu` because the explicit formula is evaluated
**on the critical line `s = 1/2 + iu`**: the log-derivative of
`Γ_C(s) = (2π)^{−s} Γ(s)` (or its `2`-multiple, depending on
convention — the constant `2` drops out of the log-derivative) is
`−log(2π) + ψ(s)`, and at `s = 1/2 + iu` this gives
`−log(2π) + ψ(1/2 + iu)`. The functional-equation symmetry
`Λ_K(s) = Λ_K(1 − s)` doubles this to `−2 log(2π) + ψ(1/2 + iu)
+ ψ(1/2 − iu)` (from the `s` and `1 − s` contributions, both
evaluated *on the critical line*: at `s = 1/2 + iu` we get
`ψ(1/2 + iu)` and at `1 − s = 1/2 − iu` we get `ψ(1/2 − iu)`).
The pole at `u = 0` is absorbed into the `s(s − 1)` factor (§5).
This **matches `meyer-extension-to-K.md`'s archimedean term**
(the previous version of this section had an arithmetic slip in
the `s ↔ 1 − s` folding, putting the digamma argument at
`1 ± iu`, not `1/2 ± iu`; verified numerically by
`code/verify_archimedean_term.py`).

### 4.3. Matrix elements on the Fourier basis

Since `{e_𝔞}` are eigenvectors of `T_{BC,K} : f ↦ log N(𝔞) · f`
(cf. `meyer-extension-to-K.md` §A) with eigenvalues `log N(𝔞)`,
the operator `τ^{(K_∞)}` is **diagonal in the Fourier basis** with
entries

```
⟨e_𝔞, τ^{(K_∞)} e_𝔟⟩  =  δ_{𝔞,𝔟} ·
   (−1/2π) ∫_{−∞}^∞ [ψ(1/2+iu) + ψ(1/2−iu) − 2 log(2π)] N(𝔞)^{iu} du  (4.3)
```

This is the K-analogue of Paper 13 eq. (6.5) / §5.2, where the
analogous expression for `K = ℚ` involves `(Γ'/Γ)(1/4 + iλ/2) +
log π`. The shift `1/4 + iλ/2` over ℚ becomes `1/2 + iu` over a
complex place — the difference reflects the `Γ(s/2)` factor at a
real place (with `s/2 = 1/4 + iλ/2` on the critical line) vs. the
`Γ(s)` factor at a complex place (with `s = 1/2 + iu` on the
critical line). The integral in (4.3) converges in distribution
sense (Stirling gives `O(log u)` integrand against the oscillatory
`N(𝔞)^{iu}`); its closed form is not needed for this note. The
operator bound `‖τ^{(K_∞)}‖_op = O(log λ)` is sub-task 2.1 of
Route 2.

## 5. Rank-2 condensation τ^{(0,2)}

### 5.1. The s(s−1) factor over ℚ (recap of Paper 13 §6.1)

Paper 13 §6.1 eq. (6.2) writes the Euler-product part of `QW_λ`
over ℚ as

```
T_0  =  τ^{(0,2)}  +  Σ_{p ≤ P_N} τ^{(p)}                        (5.1)
```

where `τ^{(0,2)}` is a **rank-2** correction coming from the two
factors `s` and `s − 1` in `Ξ(s) = (1/2) s(s−1) Λ(s)`. These
factors cancel the poles of `Λ(s)` at `s = 0, 1`, and the two
cancelled points contribute one rank-1 piece each — hence the
index `(0, 2)`. Each piece is weighted by the residue of `Λ` at
the cancelled point.

### 5.2. The K-analogue τ^{(0,2),K}

Define

```
Ξ_K(s)  :=  (1/2) s (s − 1) Λ_K(s).                              (5.2)
```

The prefactor `(1/2) s (s − 1)` is **identical** to the ℚ case;
its two zeros at `s = 0, 1` cancel the two poles of `Λ_K(s)`. The
Dedekind zeta `ζ_K` has residue `κ_K = 2π h_K R_K / (w_K √|d_K|)`
at `s = 1`; for `K = ℚ(i)` (class number 1, regulator 1, `w_K = 4`,
`|d_K| = 4`), `κ_K = π/4`. Direct computation:

- `Res_{s=1} Λ_K(s) = 4^{1/2} · 2^0 · π^{−1} · Γ(1) · κ_K = 1/2.`
- `Res_{s=0} Λ_K(s) = 2 · ζ_K(0) = 2 · (−1/4) = −1/2.`

(Here `ζ_K(0) = −h_K R_K / w_K = −1/4` for `K = ℚ(i)`, by the
functional equation; Iwaniec–Kowalski §5.10.) Both residues have
absolute value `1/2`, with opposite signs as forced by
`Λ_K(s) = Λ_K(1 − s)`.

The rank-2 condensation for K is therefore

```
τ^{(0,2),K}  =  (1/2) · π_{s = 0}  −  (1/2) · π_{s = 1}          (5.3)
```

where `π_{s=*}` is the rank-1 projector onto the
`T_{BC,K}`-eigenstate at the spectral parameter corresponding to
`s = *`, projected into `E_N^K`. The `(±1/2)` weights are exactly
the residues computed above. **The rank is 2**, the same as the ℚ
case, because the prefactor `(1/2) s (s − 1)` has the same two
zeros regardless of base field. The rank-2 structure is preserved;
only the numerical weights would differ for other imaginary
quadratic fields where `κ_K ≠ π/4`. For `K = ℚ(i)` it happens
that the absolute weights `1/2` match the ℚ case exactly. See §8
(O3) for the K ≠ ℚ(i) extension.

### 5.3. The full Euler-part T_0^K

Putting (5.3) together with the prime-power diagonal of §3:

```
T_0^K  :=  τ^{(0,2),K}  +  Σ_{N(𝔭) ≤ Q_N} τ^{(𝔭),K}              (5.4)
```

where `τ^{(𝔭),K}` is the diagonal operator with matrix elements
`⟨e_𝔞, τ^{(𝔭),K} e_𝔞⟩ = Σ_{k ≥ 1 : 𝔭^k | 𝔞} log N(𝔭) · N(𝔭)^{−k/2}`
(finite sum, since `𝔞` has bounded `𝔭`-adic valuation in `S_N^K`).
Summing over `𝔭` recovers (3.1).

The full Weil quadratic form is

```
QW_λ^K  :=  T_0^K  +  τ^{(K_∞)}                                 (5.5)
```

(K-version of Paper 13 §6.1 eq. (6.1)). The off-diagonal
log-kernel of §2 enters when one passes from the form `QW_λ^K` to
the operator `D_N^K` via the CCM / Friedrichs construction
(sub-task 1.3).

## 6. Parity and the even sector

### 6.1. The parity involution γ_K

Complex conjugation `c : a + bi ↦ a − bi` is multiplicative and
norm-preserving on `𝒪_K`, so it descends to a norm-preserving
involution `c_* : S_N^K → S_N^K` on K-smooth ideals. On primes:
split pairs are swapped (`(a + bi) ↔ (a − bi)`); the ramified prime
`(1 + i)` and inert primes `(p)`, `p ≡ 3 mod 4`, are fixed (the
ramified case because `c(1 + i) = (1 − i) = −i (1 + i)` differs by
a unit). Define the unitary parity operator on `E_N^K` by

```
γ_K e_𝔞  :=  e_{c_*(𝔞)}                                          (6.1)
```

with the section of §1.3 chosen `c`-equivariantly
(`x_{c_*(𝔞)} = c(x_𝔞)`), which is always possible for `K = ℚ(i)`
because the standard fundamental domain is `c`-invariant after
fixing a sign on the boundary. `γ_K` is involutive, unitary, and
self-adjoint.

### 6.2. Commutation Q_N^K γ_K = γ_K Q_N^K

All four pieces of `Q_N^K` commute with `γ_K`, because each
depends on the data of `𝔞` only through its norm `N(𝔞)` (off-
diagonal log-kernel; archimedean diagonal of (4.3)), through the
prime-power valuations and norm (diagonal Mangoldt kernel), or
through `c_*`-invariant spectral parameters (rank-2 projectors at
`s = 0, 1`). All of these are `c_*`-invariant since `c_*` is a
norm-preserving permutation on `S_N^K` that maps prime powers to
prime powers. So **`Q_N^K γ_K = γ_K Q_N^K`** — the K-version of
Paper 13 §3.4 / CCM Lemma 5.2(i). The proof is exactly the same
modulo replacing `p ↔ p` (trivial parity over ℚ) by `𝔭 ↔ 𝔭̄`
(genuine parity over `K`).

### 6.3. The even sector E_N^{+, K}

Define

```
E_N^{+, K}  :=  { f ∈ E_N^K : γ_K f = f }                        (6.2)
```

(the `+1` eigenspace of the involution `γ_K`). Concretely,
`E_N^{+, K}` is spanned by the `γ_K`-fixed basis vectors
`e_{(1+i)^k}, e_{(p)^k}` (`p ≡ 3 mod 4` inert) and the symmetric
sums `(e_𝔭 + e_𝔭̄)/√2` for split pairs (and analogously for
products). Roughly `dim E_N^{+,K} ≈ (1/2) dim E_N^K` with the
ramified/inert generators contributing fully and the split pairs
contributing half. Since `Q_N^K` commutes with `γ_K`, it preserves
`E_N^{+, K}` and `D_N^K` acts there independently.

**Why the even sector captures ζ_K zeros.** Using `Λ_K(s) = Λ_K(1
− s)` and `(1 − s)(−s) = s(s − 1)`, one has `Ξ_K(1 − s) = Ξ_K(s)`,
so `z ↦ Ξ_K(1/2 + iz)` is even in `z` and its zeros come in `±`
pairs — exactly as for ℚ (Paper 13 §3.2).

## 7. Hermitian property — sanity check

The diagonal Mangoldt kernel (§3), the archimedean diagonal of
(4.3), and the rank-2 combination of (5.3) are all real linear
combinations of orthogonal projections and are manifestly
self-adjoint.

The off-diagonal kernel `K_off(𝔞, 𝔟) := 1/log(N(𝔟)/N(𝔞))` for
`N(𝔞) ≠ N(𝔟)` is real but **antisymmetric**:
`K_off(𝔟, 𝔞) = −K_off(𝔞, 𝔟)`. A real antisymmetric matrix is
anti-Hermitian, not Hermitian, so as written in (2.1) the
off-diagonal block represents `i × (Hermitian)` rather than a
Hermitian operator directly. **This is the same situation as Paper
13 §3.3 over ℚ:** the kernel `1/log(n/m)` is also real and
antisymmetric. The CCM construction takes `D_N` to be the
Friedrichs extension of the **`i`-twisted** version of this form,
i.e., `D_N^K` is built from `i · Q_N^K|_off-diag + Q_N^K|_diag +
τ^{(K_∞)} + τ^{(0,2),K}` (CCM 2025 §5; sub-task 1.3). This is
Connes' standard "log-derivative `−i d/du`" convention, under
which the eigenvalues are real.

After the `i`-twist on the off-diagonal, `Q_N^K` is Hermitian on
`E_N^{+, K}`. The `i`-twist is not a new K-specific issue; flagged
here only because (2.1) does not display the `i` explicitly.

## 8. Open issues

The K-port of `Q_N` introduces several genuinely new questions
that have no counterpart over ℚ. Listed in roughly decreasing
order of how much they affect the rest of Phase I.

**(O1) Same-norm collisions in the off-diagonal (§2.2).** *Clearly
the most important.* The kernel `1/log(N(𝔟)/N(𝔞))` diverges for
distinct ideals of equal norm — first at `(1 + 2i), (1 − 2i)` of
norm 5. Option A (drop those pairs) is the recommended starting
choice and is plausibly correct because the explicit formula (M3')
already handles each split prime through the **diagonal** Mangoldt
kernel, but this needs verification by either (i) a careful read
of the K-Weil distribution side of (M3') or (ii) a small-`N`
numerical experiment comparing spectra of `D_N^K` constructed with
each option against the ground-truth zeros from
`ccm_over_K_sanity.py`.

**(O2) ~~The exact form of τ^{(K_∞)} (§4)~~ — RESOLVED
2026-04-10.** The correct form is

```
τ^{(K_∞)}(h)  =  −(1/2π) ∫ h(u)
                 [ψ(1/2 + iu) + ψ(1/2 − iu) − 2 log(2π)] du
```

with digamma argument `1/2 ± iu`. The earlier draft of (4.2) used
`1 ± iu`, which was an arithmetic slip in the `s ↔ 1 − s` folding
(at `s = 1/2 + iu` the dual point is `1 − s = 1/2 − iu`, not
`1 − iu`). Verified numerically by `code/verify_archimedean_term.py`
and matches `meyer-extension-to-K.md`'s formulation. (4.2) and
(4.3) above have been corrected.

**(O3) Numerical residues for K ≠ ℚ(i) (§5.2).** For other
imaginary quadratic class-number-1 fields `K = ℚ(√−d)`,
`d ∈ {2, 3, 7, 11, 19, 43, 67, 163}`, the residue formula
`κ_K = 2π h_K R_K / (w_K √|d_K|)` gives weights different from
`(±1/2)` in (5.3). The **rank** is still 2 and the **structure**
of `τ^{(0,2),K}` is unchanged; only the two numerical coefficients
shift. This should be tabulated when extending to all nine fields.

**(O4) Section choice and ramified-prime phase.** The basis
`e_𝔞` depends on choosing a generator `x_𝔞 ∈ K` for each ideal,
fixed up to units (`{±1, ±i}` for `K = ℚ(i)`). At the ramified
prime, `(1 + i)` and `(1 − i) = −i (1 + i)` differ by a unit,
which introduces a phase `−i` when computing the `γ_K`-image of
`e_{(1+i)}`. The phase is consistent and does not affect `Q_N^K`,
but a numerical implementation must fix the section convention
once globally.

**(O5) The `i`-twist convention (§7).** The off-diagonal kernel is
anti-Hermitian as written; the self-adjoint operator `D_N^K` is
built from the `i`-twisted form. This is the same convention as
Paper 13 / CCM 2025; flagged here only because (2.1) does not
display the `i` explicitly.

## 9. Status

**Defined here:** `S_N^K` (§1.2), Fourier basis `e_𝔞` (§1.3),
`Q_N^K` as off-diagonal + diagonal + `τ^{(K_∞)}` + `τ^{(0,2),K}`
(§2–§5), parity `γ_K`, even sector `E_N^{+, K}` (§6), Hermitian
property modulo the standard `i`-twist (§7).

**Deferred:** self-adjointness of `D_N^K` (sub-task 1.3); its
spectrum (sub-task 1.5); operator-norm bounds (Phase II);
numerical experiment with `D_N^K` for small `N` against the zeros
of `ζ_K` from `ccm_over_K_sanity.py`.

**Honest summary.** Off-diagonal, diagonal, rank-2, and parity
pieces are all line-by-line ports of the ℚ construction. The two
genuinely new K-issues are (O1) the same-norm collision in split
pairs and (O2) the precise form of the complex-place archimedean
term. Both are resolvable but the resolutions are not unique a
priori; the correct choice is the one that matches the K-Weil
explicit formula, which is the content of sub-task 1.5.

## Cross-references

- `route2-ccm-over-K.md` — the porting plan; this note executes
  Phase I sub-task 1.2.
- `meyer-extension-to-K.md` — provides (M3') and (L3), the
  explicit formulas used to read off the diagonal and to define
  `τ^{(K_∞)}`.
- `paper13-rh/preprint/sections-01-05.md` §3.3 (the ℚ template
  for `Q_N`), §3.4 (parity), §3.2 (even sector).
- `paper13-rh/preprint/sections-06-10.md` §6.1 eq. (6.1)–(6.2)
  (the decomposition `QW_λ = T_0 + τ^(R)` with
  `T_0 = τ^(0,2) + Σ_p τ^(p)`).
- `paper26-bsd/referee/code/ccm_over_K_sanity.py` — Gaussian
  prime enumeration, used as the canonical source for `S_N^K`.
- CCM 2025, arXiv:2511.22755, §4–5 — the original construction.
- Weil 1952, *Sur les "formules explicites" de la théorie des
  nombres premiers*, Comm. Sém. Math. Univ. Lund — the explicit
  formula for general number fields.
- Landau 1917, *Einführung in die elementare und analytische
  Theorie der algebraischen Zahlen* — the original explicit
  formula for `ζ_K`.
- Iwaniec–Kowalski, *Analytic Number Theory*, AMS Colloquium
  Publications 53, §5.5 and Theorem 5.12 — modern reference for
  the explicit formula at archimedean places.
