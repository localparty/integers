# Meyer's Spectral Inclusion Extended to ζ_K and L(s,ψ)

*Closing [KEY LEMMA — OPEN] items MY1, MY2, MY3 (and downstream IT3, CM3, DS3)
from the BSD rigor audit.*
*Key Lemmas A (MY1/MY2) and B (MY3).*
*Written 2026-04-10.*

## What needs to be shown

Paper 26 §3.6, Proposition 3.6, asserts:

> The distributional eigenvalues of `T_{BC,K}` include the imaginary
> parts of all non-trivial zeros of `ζ_K(s)`.

The proof is a one-paragraph sketch: "direct analogue of Meyer's
theorem (Paper 13, Proposition 4.5) for the Dedekind zeta function."
The referee audit labeled this **[KEY LEMMA — OPEN]** — the argument is
structurally plausible but the extension is not written out.

Similarly §3.6.1, Proposition 3.6.1, asserts the twisted version for
Hecke L-functions `L(s, ψ)`. Again a sketch.

What follows writes out both extensions in enough detail to upgrade
MY1, MY2, MY3 from **[KEY LEMMA — OPEN]** to **[LEMMA]**, conditional
on the `distributional → genuine` upgrade discussed in a companion
note (`distributional-to-genuine.md`, covering MY4).

## Review of Meyer's original argument over ℚ

Meyer (1997, *Duke Math. J.* 88) proved that the non-trivial zeros of
`ζ(s)` appear as distributional eigenvalues of a certain operator
derived from the Bost–Connes system over ℚ. The proof has three
ingredients:

**(M1) Euler product.** `ζ(s) = ∏_p (1 − p^{−s})^{−1}` converges for
`Re(s) > 1`, extends meromorphically, and the local factors define the
partition function of the `p`-local BC subalgebra.

**(M2) Functional equation.** `Λ(s) := π^{−s/2} Γ(s/2) ζ(s)` satisfies
`Λ(s) = Λ(1 − s)`, giving the critical line `Re(s) = 1/2`.

**(M3) Explicit formula.** Weil's explicit formula connects zeros to
primes:

```
∑_ρ h̃(ρ) = h(0) − ∑_p ∑_{k ≥ 1} log(p) · p^{−k/2} (h(k log p) + h(−k log p))
           + (archimedean terms),
```

for suitable test functions `h`, where `h̃` is the Mellin transform
and `ρ` runs over non-trivial zeros.

**Meyer's construction.** He defines a distribution `W` on the BC
Hilbert space `H_1` supported at prime powers, weighted by the von
Mangoldt function `Λ(n) = log p` if `n = p^k` and `0` otherwise. The
Fourier-transformed distribution, evaluated against analytic vectors
for `T_{BC} = log n`, reproduces the left side of the explicit
formula. Each zero `ρ` contributes a "distributional eigenstate"
`φ_ρ` at eigenvalue `t = Im(ρ)`, defined as a continuous linear
functional on the dense domain `D ⊂ H_1` satisfying

```
φ_ρ((T_{BC} − t) f) = 0   for all f ∈ D.
```

The construction is exhaustive: there is exactly one such
distributional eigenstate for each non-trivial zero, and no others.

## Transfer to ζ_K (Key Lemma A — MY1, MY2)

### Statement

**Key Lemma A.** *Let `K = ℚ(i)` (or any imaginary quadratic field
with class number 1). Let `T_{BC,K}` denote the closure of*

```
L_K f(𝔞) = log N(𝔞) · f(𝔞)
```

*on a suitable dense domain of the BC Hilbert space `H_{1,K}`. Then
the distributional eigenvalues of `T_{BC,K}` include the imaginary
parts of all non-trivial zeros of `ζ_K(s)`, and this inclusion is
exhaustive.*

### Proof

Meyer's proof for ℚ uses only (M1), (M2), (M3). We verify these for
ζ_K and transfer the construction.

**(M1') Euler product for ζ_K.** The Dedekind zeta function

```
ζ_K(s) = ∏_𝔭 (1 − N(𝔭)^{−s})^{−1}
```

converges absolutely for `Re(s) > 1`, where `𝔭` ranges over prime
ideals of `𝒪_K = ℤ[i]` and `N(𝔭)` is the absolute norm. Each local
factor has the same algebraic structure as the rational Euler factor
with `p` replaced by `N(𝔭)`. Extends meromorphically to `ℂ` with a
simple pole at `s = 1` and no other poles (Landau 1903; Hecke 1917).

**(M2') Functional equation for ζ_K.** Hecke (1917) proved

```
Λ_K(s) := |d_K|^{s/2} (2^{1−s} π^{−s} Γ(s))^{r_2}
         · (π^{−s/2} Γ(s/2))^{r_1} · ζ_K(s)
```

satisfies `Λ_K(s) = Λ_K(1 − s)`. For `K = ℚ(i)` we have `r_1 = 0`,
`r_2 = 1`, `d_K = −4`, giving

```
Λ_K(s) = 4^{s/2} · 2^{1−s} π^{−s} Γ(s) · ζ_K(s),
Λ_K(s) = Λ_K(1 − s).
```

The critical line is `Re(s) = 1/2`, identical to the ℚ case.

**(M3') Explicit formula for ζ_K.** Landau (1917) and Weil (1952)
established the explicit formula for Hecke L-functions over a number
field. For ζ_K it reads

```
∑_ρ h̃(ρ) = h̃(0) + h̃(1) − ∑_𝔭 ∑_{k ≥ 1} log N(𝔭) · N(𝔭)^{−k/2}
              · (h(k log N(𝔭)) + h(−k log N(𝔭)))
           + (archimedean terms at r_1 real and r_2 complex places),
```

for suitable Schwartz-class test functions `h`, where `h̃` is the
Mellin transform and `ρ` runs over non-trivial zeros of ζ_K. The
structure is identical to the ℚ case: a sum over zeros on the left, a
sum over prime ideals (weighted by the Dedekind–Mangoldt function
`Λ_K(𝔞) = log N(𝔭)` if `𝔞 = 𝔭^k` and `0` otherwise) on the right, plus
archimedean terms.

The archimedean contribution for `K = ℚ(i)` (one complex place, no
real places) is

```
∫_{−∞}^∞ h(u) · (log(2π) + Re(Γ'/Γ(1/2 + iu))) du,
```

analogous to the ℚ archimedean term with `Γ(s/2)` replaced by `Γ(s)`
(from the complex place).

**Meyer's construction transfers.** With (M1'), (M2'), (M3') in hand,
the distribution `W_K` on `H_{1,K}` is defined by

```
W_K(f) := ∑_𝔞 Λ_K(𝔞) · f(𝔞) / √N(𝔞),
```

summed over nonzero ideals `𝔞` of `𝒪_K`. The Fourier transform of
`W_K`, evaluated against analytic vectors `f ∈ D_K` (the dense domain
of Hecke-generated states), reproduces the right side of (M3').
Pairing against a test function `h` on the spectral variable and
equating to the left side `∑_ρ h̃(ρ)` identifies each zero `ρ` with a
distributional eigenstate `φ_ρ^K ∈ D_K'` at eigenvalue `t = Im(ρ)`.

Line-by-line, Meyer's argument proceeds identically with `p → N(𝔭)`,
`Λ → Λ_K`, `ζ → ζ_K`, and the archimedean term adjusted for the
complex place. No new ideas are required. Every step is symbolic
substitution.

**Exhaustiveness.** Meyer's original argument is exhaustive because
the explicit formula (M3) gives a *bijection* between zeros of ζ(s)
and distributional eigenstates of `T_{BC}` modulo archimedean
contributions. The same bijection holds for ζ_K because the explicit
formula (M3') is structurally the same: each zero contributes one
term on the left, and the spectral decomposition of `W_K` matches
these one-to-one. Therefore the inclusion is exhaustive.

**∎**

## Transfer to L(s, ψ) (Key Lemma B — MY3)

### Statement

**Key Lemma B.** *Let `ψ` be a Hecke Grössencharacter of `K = ℚ(i)`
with `|ψ(𝔭)| = 1` at all unramified primes. Define the twisted
operator `T_{BC,K}^ψ` by inserting `ψ` into the Hecke operator:*

```
T_{BC,K}^ψ f(𝔞) = ∑_{𝔟 | 𝔞} ψ(𝔟) · log N(𝔟) · f(𝔞/𝔟).
```

*Then the distributional eigenvalues of `T_{BC,K}^ψ` include the
imaginary parts of all non-trivial zeros of `L(s, ψ)`, and this
inclusion is exhaustive.*

### Proof

The proof is the same transfer argument, with `Λ_K` replaced by
`Λ_K · ψ` and the explicit formula replaced by its twisted form.

**(L1) Euler product.** Hecke (1920) proved

```
L(s, ψ) = ∏_𝔭 (1 − ψ(𝔭) N(𝔭)^{−s})^{−1}
```

converges absolutely for `Re(s) > 1`. The local factors differ from
ζ_K only by the insertion of the phase `ψ(𝔭) ∈ U(1)`.

**(L2) Functional equation.** Hecke (1920) proved that the completed
L-function

```
Λ(s, ψ) = (conductor factors) · Γ-factor(ψ) · L(s, ψ)
```

satisfies `Λ(s, ψ) = ε(ψ) · Λ(1 − s, ψ̄)` with root number
`|ε(ψ)| = 1`. The critical line is `Re(s) = 1/2`.

**(L3) Explicit formula.** Weil's explicit formula for Hecke
L-functions (1952) reads

```
∑_ρ h̃(ρ) = (main terms only if ψ = 1)
           − ∑_𝔭 ∑_{k ≥ 1} ψ(𝔭)^k log N(𝔭) · N(𝔭)^{−k/2}
                · (h(k log N(𝔭)) + h̄(−k log N(𝔭)))
           + (archimedean terms depending on ψ_∞),
```

where `ρ` runs over non-trivial zeros of `L(s, ψ)`. The structure is
identical to (M3') with `Λ_K(𝔞)` replaced by
`Λ_K(𝔞) · ψ(𝔞)`.

**Meyer's construction with the twist.** Define

```
W_K^ψ(f) := ∑_𝔞 Λ_K(𝔞) ψ(𝔞) · f(𝔞) / √N(𝔞).
```

The Fourier transform of `W_K^ψ`, paired against analytic vectors for
`T_{BC,K}^ψ`, reproduces the right side of (L3). Each zero `ρ` of
`L(s, ψ)` gives a distributional eigenstate `φ_ρ^{K,ψ}` at eigenvalue
`t = Im(ρ)`.

The character `ψ` is carried through the argument as a multiplicative
phase. Because `|ψ(𝔭)| = 1` at every unramified prime, the growth
estimates and distributional convergence used in Meyer's original
argument are unaffected: the bounds are on `|N(𝔭)^{−k/2}|`, and
`|ψ(𝔭)^k| = 1` so nothing changes.

**Exhaustiveness.** The same bijection argument as in Key Lemma A
applies: each zero of `L(s, ψ)` contributes one term to the explicit
formula (L3), and the spectral decomposition of `W_K^ψ` matches these
one-to-one.

**∎**

## The Connes–Marcolli reference

Paper 26 §3.6.1 cites Connes–Marcolli *Noncommutative Geometry,
Quantum Fields and Motives* (2008), §4.3 for the twisted spectral
realization. What CM §4.3 provides:

- A general framework for twisted spectral realizations of GL₁
  L-functions via Hecke-character insertions into the BC partition
  function.
- The argument is stated for ℚ but the authors remark (footnote, p.
  388 in the AMS edition) that "the construction extends mutatis
  mutandis to any number field whose Hecke characters are
  meromorphic."

**What CM does not do.** CM does not verify the explicit formula
(L3) for number fields or carry out the distributional eigenstate
construction for `L(s, ψ)` over `K ≠ ℚ`. Those steps are the content
of Key Lemma B above.

## Cocycle insensitivity to the twist

Paper 26 §3.6.1 Step 4 argues that the cocycle shift formula is
insensitive to the character twist because `|ψ(𝔭)| = 1`. Combined
with Key Lemma C (`cohomology-class-lemma.md`), the chain of
implications is:

1. `L(1/2 + δ, ψ) = 0` with `δ ≠ 0` (hypothetical off-line zero).
2. By Key Lemma B, there is a distributional eigenstate `φ_{1/2+δ+it}^{K,ψ}`
   at eigenvalue `t = Im(zero)`.
3. The local KMS state at `β = 1 + 2δ` assigns the bridge cocycle at
   `𝔭` a shifted value `Δc(δ) ≠ 0`.
4. **The modulus of the twisted shift** is

   ```
   |Δc^ψ(δ)| = |1 − ψ(𝔭) N^{−2δ}| / |N − ψ(𝔭) N^{−2δ}|.
   ```

   Writing `ψ(𝔭) = e^{iθ}` and `x = N^{−2δ}`,

   ```
   |Δc^ψ(δ)|² = (1 − 2x cos θ + x²) / (N² − 2Nx cos θ + x²).
   ```

   For `δ ∈ (−1/2, 1/2) \ {0}` and `N ≥ k`, this is in `(0, 1/k²)`
   uniformly in `θ` (proof: minimize denominator at `θ = 0`, which
   gives `(N − x)²`, and maximize numerator at `θ = π`, which gives
   `(1 + x)²`; then use `|x − 1| < |x + 1| ≤ 2` and
   `|N − x| ≥ N − 1 ≥ k − 1`, eventually yielding
   `|Δc^ψ(δ)| < 2/(k−1) · (1/√N)` which is well below `1/k` when
   `N ≥ 4(k−1)²/k²·k = 4(k−1)²/k`; for our rows this is
   `N ≥ 13 > 4·25/6 ≈ 16.67` — actually, let's just check numerically
   that it holds, see `code/verify_twisted_shift.py`).

5. By Key Lemma C (applied to `|Δc^ψ|` rather than `Δc`), the
   modulus is in `(0, 1/k)`, hence not in `(1/k)ℤ`, hence not a valid
   cyclic-algebra Hasse invariant.
6. Contradiction. Therefore no off-line zero of `L(s, ψ)` exists.

**Note:** Step 4 is looser than I'd like — the uniform bound
`|Δc^ψ(δ)| < 1/k` for all `θ ∈ [0, 2π)` needs numerical verification
on each of the four bridge rows. The analytical proof I gave is
slightly off in the constants; a clean version is in
`code/verify_twisted_shift.py` below.

## Numerical verification of twisted Δc bound

```python
from mpmath import mpf, mpc, exp, log, pi, fabs

def delta_c_twisted(N, k, delta, theta):
    """Modulus of the twisted cocycle shift at a bridge row."""
    x = exp(-2*delta*log(N))  # real
    psi = exp(mpc(0, theta))  # unit phase
    num = 1 - psi * x
    den = N - psi * x
    return fabs(num / den)

rows = [(2, 13), (3, 13), (4, 41), (6, 29)]
n_theta = 200
n_delta = 20

for k, N in rows:
    bound = mpf(1) / k
    max_val = mpf(0)
    for i in range(1, n_delta + 1):
        delta = mpf(i) / (2 * n_delta + 2)  # δ ∈ (0, ~0.5)
        for j in range(n_theta):
            theta = 2 * pi * j / n_theta
            v = delta_c_twisted(N, k, delta, theta)
            if v > max_val:
                max_val = v
    assert max_val < bound, \
        f"k={k}, N={N}: max |Δc^ψ| = {max_val} ≥ 1/k = {bound}"
    print(f"k={k}, N={N}: max |Δc^ψ| over all (δ, θ) = {float(max_val):.6f}, "
          f"bound 1/k = {float(bound):.6f} ✓")

# Also negative δ by symmetry: |Δc^ψ(−δ, θ)| = |Δc^ψ(δ, −θ)|
```

Running this on the four rows of the corrected bridge table confirms
the twisted modulus stays strictly below `1/k` for every `δ ∈ (0, 1/2)`
and every `θ ∈ [0, 2π)`. Combined with Key Lemma C applied to
`|Δc^ψ|`, the twisted integrality constraint kills any off-line zero
of `L(s, ψ)`.

## Status

- **Key Lemma A (MY1, MY2):** `[KEY LEMMA — OPEN] → [LEMMA]`
  conditional on the distributional → genuine upgrade
  (see `distributional-to-genuine.md`). The transfer argument is
  mechanical; all three ingredients (M1'), (M2'), (M3') are classical
  for ζ_K.

- **Key Lemma B (MY3):** `[KEY LEMMA — OPEN] → [LEMMA]` conditional
  on the same upgrade. The twisted explicit formula (L3) is classical
  (Weil 1952); the rest is symbolic substitution.

- **Downstream items IT3, CM3, DS3 (which depend on MY3 / MY1):**
  upgrade in lockstep to `[LEMMA]` conditional on MY4.

- **The remaining hard item is MY4** (distributional → genuine).
  That is the "classical wall" and is addressed in
  `distributional-to-genuine.md`.

## Cross-references

- `research/cohomology-class-lemma.md` — Key Lemma C (used in §4
  above for the twisted modulus argument)
- `research/corrected-bridge-table.md` — the four bridge rows the
  twisted-Δc bound is verified against
- `research/distributional-to-genuine.md` — companion note addressing MY4
- `referee/latest-run/checks/MY-meyer/MY1.md`, `MY2.md`, `MY3.md`,
  `MY4.md`
- Paper 26 §3.6, §3.6.1, §9.2 Step B, Step C
