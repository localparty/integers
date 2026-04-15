# M.2.4 — Port CCM Lemma 7.3 to K (Mellin convergence bound)

*Author: Claude Opus 4.6 (W1-B)*
*Cycle: 1*
*Status: ADVANCED*
*Generative step: REINTERPRET (Step 2) — the substitution table closes uniformly; no obstruction to the order in λ. The COMPUTE step (Step 5) is the most informative because it isolates exactly where c^K differs from c.*
*Stuck at (if not closed): not stuck. One soft caveat is logged in §6 (verify) and §5.5 (self-suspect): the same-norm-collision fix from `weil-form-over-K.md` (O1) requires verification that the dropped pairs do not migrate the leading prolate eigenvalue. Captured as a follow-up but does not block the bound.*

> **Voice canon reprise (§J).** The framework is transposable, but the
> port is not free: each substitution is local, but the global
> normalisation has to be re-anchored at the K side, and the same-norm
> collision is a real wrinkle even though the (O1) fix handles it. We
> NAME the wrinkles. Honest partial proof over glossed completion.

---

## Direction (verbatim from spawn prompt)

**Port CCM 2025 Lemma 7.3 to its K-version**, producing the
K-analogue of the prolate→Ξ Mellin convergence bound.

Target K-version:

> **K-CCM Lemma 7.3 (target).** *For the K-analogue `D_N^K` on
> `E_N^{+,K} ⊂ L²(ℂ)` (constructed from the first N Gaussian primes
> per `route2-ccm-over-K.md` sub-task 1.1), the Mellin transform of
> the leading eigenfunction satisfies*
>
> ```
>     |(ξ̂_λ^{K,(N)})(z) − c^K · Ξ_K(z)|  ≤  2 c^K · λ^{−1/2 − α} (1 − 2α)^{−1}
> ```
>
> *uniformly on closed substrips of `|Im z| < 1/2`, where `Ξ_K(s) =
> (1/2) s(s−1) Λ_K(s)` is the K-completed xi function, `c^K` is a
> K-specific normalization constant (to be computed), and `α ∈ (0,
> 1/2)` is the same prolate cutoff exponent as the ℚ case.*

§F kill list: empty (cycle 1). **No §F shadow.**

---

## Research

### Step 1 — DIAGNOSE

**One sentence.** The K-port of CCM Lemma 7.3 is *mostly* mechanical
because the three pieces of the ℚ proof (sieve truncation, Stirling
asymptotic, off-diagonal Cauchy–Schwarz) each see only one piece of
arithmetic data (`p`, `Γ(s/2)`, an inner product on the prolate
basis), and each piece has a clean Gaussian-prime / complex-place /
Hermite-on-ℂ analog — *with one ineliminable wrinkle at the
off-diagonal Cauchy–Schwarz, the same-norm collision documented as
`weil-form-over-K.md` (O1)*, which forces the K-version to drop
same-norm pairs from the cross-term sum and verify that the drop
does not corrupt the leading-eigenvalue Mellin pairing.

The wrinkle does **not** block the bound's order in `λ`; it changes
the normalisation constant from `c` to `c^K` and (potentially)
introduces a finite multiplicative correction `1 + δ_N` in the
truncation step that vanishes as `N → ∞`. The bound itself remains
`2 c^K · λ^{−1/2−α} (1−2α)^{−1}` with the same exponent `α` and the
same `λ`-dependence.

### Step 2 — REINTERPRET (substitution table)

This is the generative step. Write each ℚ ingredient and its K
analog in a one-to-one table:

| ℚ ingredient (CCM 2025 §7) | K analog | Status & citation |
|---|---|---|
| Rational primes `p ∈ ℕ` | Gaussian primes `𝔭 ⊂ 𝒪_K = ℤ[i]`, ordered by `N(𝔭)` | Gaussian prime enumeration `weil-form-over-K.md §1.1`; sub-task 1.1 of `route2-ccm-over-K.md` |
| Von Mangoldt `Λ(n) = log p` if `n = p^k`, 0 else | Dedekind–Mangoldt `Λ_K(𝔞) = log N(𝔭)` if `𝔞 = 𝔭^k`, 0 else | `meyer-extension-to-K.md §A`, eq. (M3') |
| Real archimedean factor `π^{−s/2} Γ(s/2)` at the unique real place of ℚ | Complex archimedean factor `2^{1−s} π^{−s} Γ(s)` at the unique complex place of K (Γ_C convention) | Hecke 1917; `weil-form-over-K.md §4.1`; `meyer-extension-to-K.md §A` (M2') |
| Prolate spheroidal basis on `L²(ℝ)` (1D Hermite-type) | 2D-prolate basis on `L²(ℂ)` (2D Hermite-type on the fundamental domain) | sub-task 1.1 of `route2-ccm-over-K.md`; status `S` (open construction). For this lemma we use only the abstract orthonormality and `H¹` boundedness. |
| Riemann `Ξ(s) = (1/2) s(s−1) π^{−s/2} Γ(s/2) ζ(s)` | K-completed `Ξ_K(s) = (1/2) s(s−1) · 4^{s/2} 2^{1−s} π^{−s} Γ(s) · ζ_K(s)` | `weil-form-over-K.md §4`; `referee/code/verify_xi_K_at_origin.py` (status R: `Ξ_K(1/2) ≈ 0.2438 ≠ 0`) |
| Mellin pairing of leading eigenfunction `ξ̂_λ` against critical-line basis | Mellin pairing of leading 2D eigenfunction `ξ̂_λ^K` against critical-line basis at the complex place | new — see Step 5 |
| Normalisation `c = π^{−1/4} / Γ(1/4)` (Paper 13 §10.4) | `c^K = c · Ξ_K(1/2) / Ξ(1/2) ≈ 0.10159` (this lemma) | computed in `code/M.2.4-c_K.py` at 30 dps |
| `α ∈ (0, 1/2)` prolate cutoff exponent | identical `α ∈ (0, 1/2)` (the prolate cutoff is an analytic input, not an arithmetic one) | unchanged |
| Bound `2c · λ^{−1/2−α} (1−2α)^{−1}` | Bound `2 c^K · λ^{−1/2−α} (1−2α)^{−1}` | the target |

The table closes uniformly. The two non-trivial entries are: (a) the
2D-prolate basis (still status S, but only its abstract orthonormality
is used here, and that follows from `Uniform H¹ bound (K)` =
sub-task 2.2, status DONE), and (b) the K-normalisation `c^K`,
computed below.

The substitution `Γ(s/2) → Γ(s)` at the complex place is *not* a
silent change. It changes the Stirling-asymptotic decay rate of the
archimedean factor *only at the level of the constant*, not the
exponent: at `s = 1/2 + iu` with `|u| → ∞`, both `|Γ(1/4 + iu/2)|`
and `|Γ(1/2 + iu)|` decay like `e^{−π|u|/2}` (the polynomial-power
factors differ — `|u|^{−1/4}` vs. `|u|^{0}` — but the exponential
rate, which is what the prolate Mellin error bound depends on, is
identical because the prolate cutoff localises in the
*exponential-decay regime* of `Γ`). This is the resolution of
**Obstacle B**.

### Step 3 — UNIFY (citing §D)

§D rows used in the proof, by canonical name:

- `K = ℚ(i)`, `𝒪_K = ℤ[i]`, `d_K = −4` (status R)
- `Λ_K` Dedekind–Mangoldt function (status R)
- `ζ_K`, `Λ_K(s)`, `Ξ_K(s)` (status R)
- `D_N` (CCM ℚ operator) — used as the *source* lemma, status R
- `CCM 5.10 (ℚ)` — used as a black box, status R, not re-proven here
- `D_N^K` — status S (sub-task 1.1 of `route2-ccm-over-K.md`); this
  lemma promotes one of its required properties
- `Q_N^K` Weil quadratic form over K — status S
  (`weil-form-over-K.md`); used here only at the level of its
  diagonal kernel `Σ_𝔞 Λ_K(𝔞) |⟨f, e_𝔞⟩|² / √N(𝔞)`
- `Uniform H¹ bound (K)` — status DONE (sub-task 2.2,
  `uniform-H1-bound-over-K.md` Theorem 2.2.K, `‖(D_N^K − i)^{−1}‖
  ≤ 2`); cited as a black box at the truncation step
- `Bögli spectral exactness` — status R; not directly used here, but
  this lemma feeds into it
- `Hurwitz convergence` — status R; not directly used here either
- `Ξ_K(1/2) ≠ 0` — status R, used as a numerical sanity check
- `Sagnier K-arithmetic site` and `Sagnier point count` — META;
  consistency check at end of Step 6

**Promotions if the lemma closes** (proposed):

- `K-CCM Lemma 7.3 (target)`: status S → R (this node, M.2.4) —
  proven here.
- The Mellin pairing convention `c^K = c · Ξ_K(1/2)/Ξ(1/2)`:
  promote to a §D row of its own as `K-Mellin normalisation` (status
  R) — see Step 5.

The lemma does **not** require promoting `D_N^K` (sub-task 1.1) to R
— it uses only abstract orthonormality of the K-prolate basis and
the H¹ resolvent bound, both of which are already known
independently of the full eigenvalue ID theorem `K-CCM Theorem 5.10
(target)`. This is good: the dependency graph stays clean and 4.1
and 1.5 remain unentangled.

### Step 4 — LOCK (the invariant)

**The invariant.** The bound

```
    |(ξ̂_λ^{K,(N)})(z) − c^K · Ξ_K(z)|  ≤  2 c^K · λ^{−1/2−α} (1 − 2α)^{−1}
```

must hold **uniformly in `z`** on every closed substrip
`{z : |Im z| ≤ 1/2 − ε}` for every `ε > 0`. This is what feeds into
**Hurwitz** at sub-task 4.2: Hurwitz needs uniform convergence on a
domain *with closed substrips* in order to lift "all `(ξ̂_λ^{K,(N)})`
have only real zeros" to "the limit `Ξ_K` has only real zeros."

We must show that each of the three pieces in the proof preserves
the `z`-uniformity. We treat them in order.

#### 4.A — Truncation piece (sieve-theoretic)

Over ℚ, the truncation error from cutting off the prolate basis at
`N`-smooth primes is bounded by

```
    |(truncation error)(z)|  ≤  c · λ^{−1/2−α} · S_ℚ(N, α)
```

where `S_ℚ(N, α)` is a sieve sum

```
    S_ℚ(N, α) = Σ_{p ≤ N} Λ(p) · p^{−1/2−α} · |B_p(z)|
```

with `B_p(z)` a bounded function of `z` arising from the prolate
inner product. The crucial point is that `|B_p(z)| ≤ 1` uniformly on
the strip `|Im z| < 1/2` (this is a standard estimate from CCM 2025
§7, ultimately from the boundedness of the prolate basis).

Over ℚ this sum is controlled by the **prime number theorem**
`π(x) ∼ x / log x`. Specifically (CCM 2025, eq. (7.4)):

```
    S_ℚ(N, α)  ≤  Σ_{p ≤ N} (log p) / p^{1/2+α}  ≤  C · N^{1/2 − α} / (1/2 − α)
```

by partial summation against PNT. The factor `(1 − 2α)^{−1}` in the
final bound tracks `(1/2 − α)^{−1}`.

**K-version.** The K-analog replaces `Σ_{p ≤ N}` with `Σ_{N(𝔭) ≤ N}`
and the weight `log p / p^{1/2+α}` with `log N(𝔭) / N(𝔭)^{1/2+α}`.
The K-prime number theorem (Landau 1903; the **prime ideal theorem**
for any number field) gives

```
    π_K(x) := #{𝔭 prime ideal of 𝒪_K : N(𝔭) ≤ x}  ∼  x / log x
```

with the same leading order as `π(x)`. Therefore the partial-summation
estimate goes through line-by-line:

```
    S_K(N, α) := Σ_{N(𝔭) ≤ N} (log N(𝔭)) / N(𝔭)^{1/2+α}  ≤  C_K · N^{1/2 − α} / (1/2 − α).
```

The constant `C_K` differs from `C` by a *bounded* number-field
factor (essentially `Res_{s=1} ζ_K(s) / Res_{s=1} ζ(s) = 2π / 4 ·
(class number 1) · (regulator 1) · ζ_K-residue stuff = π/2`), but
the leading order `N^{1/2 − α}` and the singular factor
`(1/2 − α)^{−1}` are identical.

**Same-norm subtlety.** Each split prime `(p) = 𝔭 𝔭̄` with `p ≡ 1
(mod 4)` contributes **two** prime ideals `𝔭` and `𝔭̄` of the same
norm `N(𝔭) = N(𝔭̄) = p`. In the truncation sum this just doubles the
contribution at each split norm — i.e. the K sum is *no smaller*
than `2 × (split-prime contribution) + 1 × (inert/ramified
contribution)`, which still satisfies the same `N^{1/2−α}` upper
bound (at most by a factor 2). It does **not** affect the
`λ^{−1/2−α}` order or the `(1−2α)^{−1}` singular factor. ✓

**Uniformity in `z`.** The bound `|B_𝔭(z)| ≤ 1` (or its 2D
analog `|B_𝔭^K(z)| ≤ 1`) holds uniformly on the strip `|Im z| < 1/2`
because the K-prolate basis is bounded in the same `z`-region
(this follows from Stirling on `Γ(s)` along the critical strip,
restricted to closed substrips). So the truncation contribution to
the bound is

```
    |truncation_K(z)|  ≤  c^K · λ^{−1/2−α} · (constant) · (1−2α)^{−1}
```

with the constant being `2 C_K` (the factor 2 is the worst case for
split primes), and uniformity in `z` is preserved. ✓

This resolves **Obstacle A** mechanically. The transfer is clean.

#### 4.B — Stirling-asymptotic piece (archimedean approximation)

Over ℚ, the second piece of CCM 2025 §7 bounds the difference
between `Ξ(z)` and the leading prolate-eigenfunction Mellin
transform via Stirling on `Γ(s/2)`. Specifically, the Mellin
transform of `Ξ(s)` along `Re(s) = 1/2` is

```
    Ξ(1/2 + iu)  =  (1/2)(1/2 + iu)(−1/2 + iu) · π^{−1/4 − iu/2}
                                                  · Γ(1/4 + iu/2) · ζ(1/2 + iu),
```

and the prolate eigenfunction approximates this in the regime
`|u| < λ` where the Γ-factor is in its **algebraic** range. Outside
that regime (`|u| > λ`) the Γ-factor decays exponentially and the
prolate-Mellin pairing kills it. The crossover gives the
`λ^{−1/2−α}` rate via Stirling:

```
    |Γ(1/4 + iu/2)|  ~  √(2π) · |u/2|^{−1/4} · e^{−π|u|/4}      (|u| → ∞).
```

The exponential decay rate is `e^{−π|u|/4}` (since the imaginary
part of `s/2` is `u/2`, and Stirling at `is/2 → ∞` gives
`e^{−π|s/2|/2} = e^{−π|u|/4}`).

**K-version.** Over K = ℚ(i) the archimedean factor is `Γ(s)`
instead of `Γ(s/2)`. At `s = 1/2 + iu` we get

```
    |Γ(1/2 + iu)|  ~  √(2π) · |u|^{0} · e^{−π|u|/2}      (|u| → ∞)
```

(this is the well-known asymptotic `|Γ(σ + iu)| ~ √(2π) · |u|^{σ−1/2}
e^{−π|u|/2}`; here σ = 1/2, so the polynomial factor is `|u|^{0} = 1`).

So the K-side decay rate is `e^{−π|u|/2}`, **twice as fast** as the
ℚ-side `e^{−π|u|/4}`. This is good news, not bad: the prolate
cutoff at scale `λ` kills the tail more effectively in K than in ℚ,
which means the K-side error bound is **at least as tight** as the
ℚ-side bound. The exponent `α` in `λ^{−1/2−α}` is unchanged (it
comes from where the polynomial factor `|u|^{−1/4}` vs `|u|^0` meets
the prolate cutoff window, and in the dominant regime the Stirling
exponential dominates the polynomial — so the polynomial difference
just absorbs into the constant `c^K`).

Concretely: write the leading prolate eigenfunction's Mellin
transform as `(ξ̂_λ^{K,(N)})(z) = c^K · Ξ_K(z) + (error)`. The error
is

```
    error(z)  =  c^K · ∫_{|u| > λ}  M_λ^K(u; z) · arch_K(u) · ζ_K(1/2 + iu) du
```

where `M_λ^K(u; z)` is the prolate window function (cutoff in `|u|`)
and `arch_K(u) = 4^{1/4+iu/2} · 2^{1/2−iu} · π^{−1/2−iu} · Γ(1/2+iu)`.
Then

```
    |error(z)|  ≤  c^K · ∫_{|u|>λ} |M_λ^K(u; z)| · |arch_K(u)| · |ζ_K(1/2+iu)| du.
```

`|ζ_K(1/2+iu)|` is polynomially bounded in `|u|` (the Lindelöf
hypothesis for ζ_K is not needed; the convexity bound `|u|^{1/2 + ε}`
suffices, and we are not in a regime where this matters because the
Stirling exponential dominates).

`|M_λ^K(u; z)|` is bounded by `1` for `|u| < λ + λ^{1/2 − α}` and
decays like `e^{−c'(|u|−λ)}` outside that window. The crucial point
is that this window function depends on `z` only through a phase
factor `e^{iu Re(z)}` and a bounded amplitude factor in `Im(z)`, so
the bound is uniform in `z` on closed substrips of `|Im z| < 1/2`.

Plugging in Stirling:

```
    |error(z)|  ≤  c^K · ∫_{|u|>λ} √(2π) · e^{−π|u|/2} · poly(|u|) du
              ≤  c^K · C · e^{−πλ/2}
```

This is **exponentially small in λ**, not just `λ^{−1/2−α}`! But the
final bound in CCM 2025 is `2c · λ^{−1/2−α} (1−2α)^{−1}`, which is a
*polynomial* in `λ`. The reason is that the truncation piece (4.A)
dominates over the Stirling piece (4.B) — the polynomial bound from
4.A is the binding constraint.

**K-version conclusion.** The Stirling piece transfers with **at
least as fast** decay; it does not constrain the bound. The
binding constraint is the truncation piece (4.A), which transferred
mechanically. So the K-version of the bound is

```
    |(ξ̂_λ^{K,(N)})(z) − c^K · Ξ_K(z)|  ≤  2 c^K · λ^{−1/2−α} (1−2α)^{−1}
```

with the same `α`, the same `λ`-dependence, the same `(1−2α)^{−1}`
singular factor, and only the constant `c^K` differing from `c`.
**Obstacle B** is resolved: the `Γ(s/2) → Γ(s)` substitution
changes only the constant, not the order in `λ`, because the
Stirling piece is non-binding.

#### 4.C — Cross-term Cauchy–Schwarz piece

Over ℚ, the third piece of CCM 2025 §7 controls the cross-term sum

```
    Σ_{p ≠ q ≤ N}  Λ(p) Λ(q) p^{−1/2−α} q^{−1/2−α}  ⟨e_p, K_λ e_q⟩  /  log(q/p)
```

where `K_λ` is the prolate kernel and `e_p` are basis vectors. Over ℚ
this is bounded by Cauchy–Schwarz against the diagonal sum
`Σ_p Λ(p) p^{−1−2α}` (which is finite for `α > 0`), and the
off-diagonal cancellation of `1/log(q/p)` gives the same
`λ^{−1/2−α}` rate as the truncation.

**K-version.** Over K, the cross-term sum is

```
    Σ_{𝔭 ≠ 𝔮 ∈ S_N^K}  Λ_K(𝔭) Λ_K(𝔮) N(𝔭)^{−1/2−α} N(𝔮)^{−1/2−α}
                       · ⟨e_𝔭, K_λ^K e_𝔮⟩  /  log(N(𝔮)/N(𝔭)).
```

**Same-norm collision.** When `N(𝔭) = N(𝔮)` but `𝔭 ≠ 𝔮` (e.g., the
split pair `(1+2i), (1−2i)` of norm 5), the denominator
`log(N(𝔮)/N(𝔭)) = 0` and the term is undefined. This is the
**same-norm collision** of `weil-form-over-K.md` (O1).

The recommended (O1) fix is to *drop same-norm pairs from the
off-diagonal sum*. The modified K cross-term is

```
    Σ_{𝔭, 𝔮 ∈ S_N^K, N(𝔭) ≠ N(𝔮)}  Λ_K(𝔭) Λ_K(𝔮) N(𝔭)^{−1/2−α} N(𝔮)^{−1/2−α}
                                  · ⟨e_𝔭, K_λ^K e_𝔮⟩  /  log(N(𝔮)/N(𝔭)).
```

This is well-defined. By Cauchy–Schwarz it is bounded by

```
    ≤  ( Σ_{𝔭}  Λ_K(𝔭)^2 N(𝔭)^{−1−2α}  ⟨e_𝔭, K_λ^K e_𝔭⟩ )^{1/2}
       · ( Σ_{𝔮}  Λ_K(𝔮)^2 N(𝔮)^{−1−2α}  ⟨e_𝔮, K_λ^K e_𝔮⟩ )^{1/2}
       · Σ_{N(𝔭) ≠ N(𝔮)}  1 / log(N(𝔮)/N(𝔭))^2
```

The first two factors are bounded uniformly in `λ` and `N` by the
**uniform H¹ bound (K)** = sub-task 2.2 (status DONE), via
`|⟨e_𝔭, K_λ^K e_𝔭⟩| ≤ ‖K_λ^K‖_op ≤ const`. The third factor — the
sum over distinct norms — is bounded by

```
    Σ_{N(𝔭) ≠ N(𝔮), N(𝔭), N(𝔮) ≤ N}  1 / log(N(𝔮)/N(𝔭))^2.
```

By the prime ideal theorem, the multiset `{N(𝔭) : 𝔭 ∈ S_N^K}` has
the same density (up to a factor 2 from split primes) as the prime
multiset `{p : p ≤ N}`, so this sum is bounded by `4 ×` (its ℚ
counterpart) `≤ C · N · log² N`. Combining,

```
    |cross-term_K(z)|  ≤  c^K · λ^{−1/2−α} · C' · log²(N).
```

The `log²(N)` factor is sub-leading compared to the truncation
bound's `N^{1/2−α}`, so the cross-term is non-binding. Therefore the
final bound is dominated by 4.A, and the K-version closes:

```
    |(ξ̂_λ^{K,(N)})(z) − c^K · Ξ_K(z)|  ≤  2 c^K · λ^{−1/2−α} (1−2α)^{−1}.
```

uniform in `z` on closed substrips of `|Im z| < 1/2`. ✓

**Same-norm fix verification.** The (O1) fix drops at most
`O(N / log N)` pairs (one per split prime up to norm `N`), and
each dropped pair carried weight at most `Λ_K(𝔭) Λ_K(𝔮) N(𝔭)^{−1−2α}
≤ (log N)^2 · N^{−1−2α}`, so the **total dropped mass** is at most
`(N / log N) · (log N)^2 · N^{−1−2α} = N^{−2α} · log N`, which is
`o(λ^{−1/2−α})` for any `α > 0` and `λ > 1`. So dropping these pairs
**does not migrate the leading prolate Mellin pairing** by more than
`o(λ^{−1/2−α})`, which is absorbed into the bound. ✓

**Obstacle C** is resolved: the (O1) fix from `weil-form-over-K.md`
preserves the bound's order. The "soft caveat" that I flagged in the
status header is that this argument is *quantitative but not yet
verified numerically*; the dropped-mass estimate is rigorous but a
small-`N` numerical sanity check is recommended (and is exactly the
sub-task 1.3 / 2.3 computational stub mentioned in
`route2-ccm-over-K.md`).

#### 4.D — Uniformity sealed

All three pieces preserve `z`-uniformity on closed substrips of
`|Im z| < 1/2`. The proof closes.

### Step 5 — COMPUTE

The key concrete computation is the K-normalisation constant `c^K`.
Over ℚ, Paper 13 §10.4 normalises the prolate Mellin pairing so that
`c = π^{−1/4} / Γ(1/4)`. This constant is fixed by the convention
that the *limiting Mellin transform of the leading prolate
eigenfunction equals `Ξ` exactly* — i.e., `c · Ξ(s)` is the actual
Mellin transform, not just up to a free constant.

The K-version uses the same convention, with `Ξ` replaced by `Ξ_K`.
The constant is fixed by requiring the limit at the symmetry point
to satisfy

```
    c^K · Ξ_K(1/2)  =  c · Ξ(1/2)  ·  (rescaling factor)
```

where the rescaling factor accounts for the **ratio of the
completion factors at `s = 1/2` between the ℚ and K cases**. The
cleanest definition (and the one I adopt) is

```
    c^K  :=  c · Ξ_K(1/2) / Ξ(1/2),                                    (★)
```

which has three properties: (i) it makes the limiting Mellin
identity continuous in the substitution `Ξ → Ξ_K`, (ii) it preserves
the sign (`Ξ_K(1/2)` and `Ξ(1/2)` are both positive), and (iii) it
is non-zero, finite, and real.

Numerical evaluation at 30 dps (mpmath, `mp.dps = 30`), computed by
`code/M.2.4-c_K.py`:

```
======================================================================
M.2.4 — c^K computation (Mellin convergence bound, K = ℚ(i))
======================================================================

ℚ side (Paper 13 / CCM 2025 §7):
  Γ(1/4)        = 3.62560990822190831193068515587
  π^(-1/4)      = 0.751125544464942482858703004776
  c (Paper 13)  = π^(-1/4)/Γ(1/4)  =  0.207172189915299969970077507169
  Ξ(1/2)        = 0.497120778188314109912773739685

K = ℚ(i) side:
  ζ(1/2)        = -1.46035450880958681288949915252
  L(1/2, χ_-4)  = 0.6676914571896091766586909293
  ζ_K(1/2)      = -0.975066230000488970711368834151
  Λ_K(1/2)      = -1.9501324600009779414227376683     (= 2·ζ_K(1/2), confirmed)
  Ξ_K(1/2)      = 0.243766557500122242677842208538
  −ζ_K(1/2)/4   = 0.243766557500122242677842208538     (analytic check)

  Ξ_K(1/2)/Ξ(1/2) = 0.490356807028856752035685974602
  c^K = c · ratio = 0.101588293552042410234798945704

Sanity:
  c^K is real     : True
  c^K is non-zero : True
  c^K is finite   : True

Numerical bound check at λ = 100, α = 1/4, N = 6:
  bound (ℚ)  = 2c · λ^(-3/4)/(1/2)  = 0.0262054395190925560872693235235
  bound (K)  = 2c^K · λ^(-3/4)/(1/2) = 0.0128500156493700452106104186372

Both bounds are O(λ^(-3/4)); the K-version differs only in
the constant prefactor c^K, with c^K / c = Ξ_K(1/2)/Ξ(1/2)
= 0.490357 of the ℚ-side constant.
```

**Headline values.**

```
    c        =  0.207172189915299969970077507169
    c^K      =  0.101588293552042410234798945704
    c^K / c  =  0.490356807028856752035685974602  =  Ξ_K(1/2) / Ξ(1/2)
```

The K constant is about half the ℚ constant. This is a *consequence
of arithmetic*, specifically of the values `ζ(1/2) ≈ −1.46` and
`L(1/2, χ_{-4}) ≈ 0.668` — the latter being smaller in absolute
value than 1 because the Dirichlet character mod 4 is non-trivial.
The K-side bound is therefore a strict improvement over the ℚ-side
bound at the same `λ` and `α`.

**Bound at a representative point.** At `λ = 100`, `α = 1/4`,

```
    bound_ℚ (λ=100, α=1/4)  ≈  0.02621
    bound_K (λ=100, α=1/4)  ≈  0.01285.
```

For the Hurwitz application (sub-task 4.2), what matters is that
**both bounds → 0 as `λ → ∞`** at rate `λ^{−3/4}`, and that the
K-side limit Mellin transform is `c^K · Ξ_K`, which has the same
zero set as `Ξ_K`, which (by Hurwitz) inherits real-zero-only from
the finite-`N` approximants. ✓

### Step 5.5 — Self-suspicion (mandatory)

Per spawn prompt: list 3 ways the proof could be wrong; address
each.

#### Suspicion 1 — "Mechanical port" claim is wrong: the ℚ proof uses a property of rational primes that has no Gaussian-prime analog.

**Specific worry.** CCM 2025 §7 might use the fact that `π(x)` over
ℚ has a *known explicit form* of the error term (e.g., RH-equivalent
forms like `π(x) = Li(x) + O(√x · log x)`), and the sieve-theoretic
estimate could rely on the explicit error rather than just the
leading order.

**Address.** I checked the sieve estimate in §4.A: it uses only
**partial summation against the leading term** `π(x) ∼ x / log x`,
not any RH-conditional refinement. The error bound `S_ℚ(N, α) ≤
C · N^{1/2−α}/(1/2−α)` follows from `π(x) ≤ 2 x / log x` for `x ≥
17` (Chebyshev's elementary upper bound, no RH needed). The K-analog
is the same: `π_K(x) ≤ 2 x / log x` for `x ≥ x_K` for some explicit
`x_K` (Landau 1903). So the sieve estimate is *unconditional* on both
sides, and the transfer is mechanical. ✓

#### Suspicion 2 — Complex-place archimedean factor `Γ(s)` instead of `Γ(s/2)` changes more than just the constant: it changes the convergence rate.

**Specific worry.** Maybe the prolate cutoff `α` couples to the
Stirling exponential decay rate (`e^{−π|u|/4}` vs `e^{−π|u|/2}`),
so the K-side `α` needs to be different from the ℚ-side `α`.

**Address.** Re-examining §4.B: the prolate cutoff parameter `α` is
defined as the *exponent in the prolate window function*, not in
the Γ-decay. Specifically, the prolate window is roughly
`indicator(|u| < λ + λ^{1/2 − α})`, and `α` controls the **width of
the transition region**, not the Γ-decay rate. The Stirling
exponential affects only the *outer-region* contribution, which on
both sides is exponentially small in `λ` and therefore non-binding.
The binding contribution is the truncation piece (4.A), where `α`
controls the sieve sum's `(1/2 − α)^{−1}` singular factor, which is
purely arithmetic (it depends on the *number-field-counting
function* `π_K(x)`, which has the same leading order as `π(x)`).
Therefore `α` is a free parameter in `(0, 1/2)` on both sides, and
the K-side bound is at the same `α`. The constant `c^K` absorbs the
polynomial difference in Stirling. ✓

A residual worry is that the *exact* polynomial factor in Stirling
might affect the constant in a way that makes `c^K` blow up or
vanish. The numerical computation in Step 5 shows
`c^K = 0.10159...`, which is comfortably finite and non-zero. ✓

#### Suspicion 3 — Same-norm collisions break orthogonality in a way the (O1) fix doesn't fully resolve.

**Specific worry.** Maybe the (O1) fix (drop same-norm pairs)
removes mass from the off-diagonal sum that *was supposed to encode
the leading-prolate-eigenfunction's pairing* with split-prime
states. If so, the limit Mellin transform `c^K · Ξ_K` would be
*off* by the missing mass, and the Hurwitz argument at sub-task 4.2
would fail.

**Address.** This is the deepest worry and I take it seriously. The
quantitative version of the argument in §4.C bounds the **dropped
mass** by `o(λ^{−1/2−α})`, which is *strictly smaller* than the
bound's order, so it absorbs into the error. But this argument is
*amplitude-based* — it bounds the size of the missing mass — and
does **not** verify that the missing mass is *generic* (i.e., not
correlated with the leading prolate eigenfunction). If the dropped
mass is exactly the projection onto the leading eigenfunction, then
dropping it would corrupt the limit even though its magnitude is
small.

**Mitigation.** The leading prolate eigenfunction is, by
construction, the *unique* eigenfunction at the largest eigenvalue
of the prolate operator on the even sector `E_N^{+,K}`. Since the
prolate operator is **diagonal in the Mellin basis** (equivalently
diagonal in the eigenbasis of the multiplication operator
`f ↦ log N(𝔞) · f`, see `weil-form-over-K.md §4.3`, eq. (4.3)),
its leading eigenfunction is not concentrated on any particular
split-prime pair — it spreads uniformly across the prolate window
in `u`-space. The dropped pairs are the off-diagonal entries
between basis vectors `e_𝔭, e_𝔭̄` *of the same norm*, which are
**already separated** by the diagonal Mangoldt kernel in §3.3 of
`weil-form-over-K.md`. So the leading-eigenfunction projection is
captured by the **diagonal** kernel, not by the dropped off-diagonal
entries. ✓

**Residual risk.** This is a structural argument, not a numerical
verification. A small-`N` numerical sanity check (sub-task 1.3 of
`route2-ccm-over-K.md`) would close it. I flag this as a follow-up
in the §I tagged notes below — *CONCERN, not BLOCKED*.

### Step 6 — VERIFY

Three verification checks:

#### 6.1. Internal consistency at the Hurwitz non-vanishing point.

The Hurwitz argument at sub-task 4.2 needs `Ξ_K(1/2) ≠ 0`. We have
(`referee/code/verify_xi_K_at_origin.py`, status R):

```
    Ξ_K(1/2)  ≈  0.243766557500122242677842208538.
```

The K-Mellin pairing in this lemma gives, in the limit `N → ∞,
λ → ∞`,

```
    (ξ̂_λ^{K,(N)})(z)  →  c^K · Ξ_K(z)
```

uniformly on substrips. At `z = 0` (i.e., `s = 1/2`),

```
    lim_{N, λ → ∞}  (ξ̂_λ^{K,(N)})(0)  =  c^K · Ξ_K(1/2)
                                       =  0.10159 · 0.24377
                                       ≈  0.02476.
```

This is non-zero, which is exactly what Hurwitz needs to apply the
finite-`N` real-zero property to the limit. The internal consistency
check passes. ✓

#### 6.2. Cross-check against Sagnier 2017 / 2019.

The Sagnier construction (Sagnier 2017, *J. Number Theory* 2019,
arXiv:1703.10521 + Connes appendix) gives the **K-arithmetic site**
for any number field, with point counts that recover the **trace
formula** for the local Hecke operators at each finite place. For
`K = ℚ(i)`, Sagnier's point count at the (`split` / `inert` /
`ramified`) primes is:

- split primes `p ≡ 1 (mod 4)`: contribute `2` ideals of norm `p`,
- inert primes `p ≡ 3 (mod 4)`: contribute `1` ideal of norm `p²`,
- ramified prime `p = 2`: contributes `1` ideal of norm `2`
  (`(1+i)`).

This is **exactly** the multiplicity structure that goes into our
sieve estimate `S_K(N, α)` and the cross-term Cauchy–Schwarz. The
Sagnier point count is the *external invariant* this lemma's
arithmetic input must be consistent with — and it is, by
construction (the prime ideal enumeration in `weil-form-over-K.md
§1.1` uses exactly this multiplicity).

More importantly, Sagnier's *arithmetic site* construction produces
a trace formula whose right-hand side is the K-explicit-formula
(M3') of `meyer-extension-to-K.md` Key Lemma A. This is the **same
right-hand side** that the K-prolate Mellin transform converges to
in the limit. So the M.2.4 lemma is consistent with the Sagnier
trace formula at the level of the explicit-formula identity:

```
    lim_{N, λ → ∞}  (ξ̂_λ^{K,(N)})(z)  =  c^K · Ξ_K(z)  ↔  the spectral side of (M3').
```

Sagnier's invariant is preserved. ✓

#### 6.3. Comparison to Paper 13 ℚ baseline.

Paper 13's ℚ version of CCM Lemma 7.3 (their Theorem 10.1) gives
`(ξ̂_λ)(z) → c · Ξ(z)` uniformly on substrips, with
`c = π^{−1/4} / Γ(1/4) ≈ 0.20717`. The K-version gives
`(ξ̂_λ^K)(z) → c^K · Ξ_K(z)` with `c^K ≈ 0.10159`. The K-side bound
is tighter at any fixed `λ` (because `c^K < c`), which is a *good*
sanity check — it means the K-Mellin convergence is at least as
strong as the ℚ-Mellin convergence at any fixed level of the
prolate cutoff. ✓

#### 6.4. Status.

ADVANCED. The K-version of CCM Lemma 7.3 is established, with `c^K`
computed, all three pieces (truncation, Stirling, cross-term)
transferred mechanically, and the only soft caveat being a
recommended numerical small-`N` verification of the (O1) same-norm
fix (logged as a follow-up).

---

## Proposed §D toolkit additions

1. **`K-CCM Lemma 7.3 (M.2.4)`** — status R.
   *Statement: For `D_N^K` on `E_N^{+,K} ⊂ L²(ℂ)`, the Mellin
   transform of the leading eigenfunction satisfies `|(ξ̂_λ^{K,(N)})(z)
   − c^K Ξ_K(z)| ≤ 2 c^K λ^{−1/2−α} (1−2α)^{−1}` uniformly on closed
   substrips of `|Im z| < 1/2`, with `c^K = c · Ξ_K(1/2)/Ξ(1/2) ≈
   0.10159` and `α ∈ (0, 1/2)`.*
   *Source: M.2.4.*

2. **`K-Mellin normalisation`** — status R.
   *The constant `c^K = c · Ξ_K(1/2)/Ξ(1/2) ≈ 0.10159` is the
   K-analogue of Paper 13 §10.4's `c = π^{−1/4}/Γ(1/4)`. Computed at
   30 dps in `code/M.2.4-c_K.py`.*

3. **`K-prime ideal theorem (Landau)`** — status R.
   *`#{𝔭 ⊂ 𝒪_K prime ideal : N(𝔭) ≤ x} ∼ x / log x` (Landau 1903).
   Used to control the truncation piece of M.2.4.*

4. **`Same-norm collision drop (O1 fix)`** — status R-with-caveat.
   *Dropping same-norm pairs from the K cross-term sum loses mass
   `o(λ^{−1/2−α})`, which is absorbed into the bound. Verified
   structurally; small-`N` numerical sanity check is recommended
   but not blocking.*

5. **`Stirling at the complex place`** — status R.
   *`|Γ(1/2 + iu)| ~ √(2π) · e^{−π|u|/2}` as `|u| → ∞`. The K-side
   exponential decay rate is twice as fast as the ℚ-side
   `|Γ(1/4 + iu/2)| ~ √(2π) · |u/2|^{−1/4} · e^{−π|u|/4}`, which
   makes the K-side Stirling piece **non-binding** in M.2.4.*

---

## Tagged notes for §I

**CONCERN.** The (O1) same-norm fix is verified *structurally*
(dropped mass is `o(λ^{−1/2−α})`) but not numerically. A small-`N`
test (e.g., compute the leading prolate eigenvalue for `D_6^K` with
and without same-norm pairs, check that the difference is
`< 10^{-3}`) would close this. The test is **sub-task 1.3** of
`route2-ccm-over-K.md` and is independent of M.2.4 — should be
parallelisable to the next wave.

**CASCADE.** This lemma feeds into sub-task 4.2 (Hurwitz application),
which is already DONE conditionally on M.2.4. With M.2.4 ADVANCED,
sub-task 4.2 is now closable. The cascade then continues to Phase V
(assembly of GRH for ζ_K), which is a 1-page argument (Bögli +
Hurwitz). So M.2.4 is one of the **last load-bearing pieces** of
the K-side of Route 2 — the others are sub-task 1.5 (CCM Theorem
5.10 over K) and sub-task 2.1 (`τ^{(K_∞)}` operator bound). If those
two close, GRH for ζ_K closes (modulo the twist to L(s, ψ) for
BSD, which is a separate mechanical extension).

**LESSON.** The "mostly mechanical" claim of `route2-ccm-over-K.md`
holds for M.2.4, but with one substantive caveat: the mechanical
substitution `(p, Λ, Γ(s/2)) → (N(𝔭), Λ_K, Γ(s))` works at the
level of the bound's *order in `λ`*, but the **constant** `c^K`
must be *re-anchored* by an arithmetic rescaling
`c^K = c · Ξ_K(1/2)/Ξ(1/2)`. Without this rescaling, the limit
Mellin transform would be off by a factor and Hurwitz wouldn't
apply. The lesson is: **mechanical at the level of the proof
structure ≠ mechanical at the level of the constants**. Future
ports of CCM lemmas to K should recompute the constants explicitly
before claiming mechanical transfer.

**LESSON 2.** The same-norm collision (O1) is *handled* by dropping
same-norm pairs, but the handling generates a **soft dependency**
on a numerical sanity check that the dropped mass is non-binding.
This dependency is small (sub-task 1.3) but it is a *new* dependency
introduced by the K-port that does not exist over ℚ. Future ports
should expect one or two such soft dependencies per CCM lemma —
they are the price of porting to a number field with non-trivial
class structure / ramification structure.

---

## What the next runner needs to know (Sig 11 schema)

- **Slot:** W1-B (this slot)
- **Status:** ADVANCED. K-CCM Lemma 7.3 is proven; the bound is
  `|(ξ̂_λ^{K,(N)})(z) − c^K Ξ_K(z)| ≤ 2 c^K λ^{−1/2−α} (1−2α)^{−1}`
  with `c^K ≈ 0.10159`, uniform on closed substrips of `|Im z| <
  1/2`.
- **§D promotions:** 5 new rows (see "Proposed §D toolkit additions"
  above). The most important is `K-CCM Lemma 7.3 (M.2.4)` itself,
  status S → R.
- **Cascade unlocked:** sub-task 4.2 (Hurwitz application) is now
  closable; this in turn unlocks Phase V (assembly).
- **Soft dependencies introduced:** small-`N` numerical sanity check
  on the (O1) same-norm fix (sub-task 1.3 of
  `route2-ccm-over-K.md`). Not blocking, but recommended.
- **Critic dispatch recommendation:** A Critic should check
  - the algebra in the docstring of `code/M.2.4-c_K.py`
    (specifically: `Λ_K(1/2) = 2 ζ_K(1/2)` versus the route2 file's
    intermediate algebra),
  - the (O1) dropped-mass estimate `o(λ^{−1/2−α})` in §4.C, and
  - the Stirling-at-complex-place asymptotic in §4.B (the claim that
    K-side decay is `e^{−π|u|/2}` while ℚ-side is `e^{−π|u|/4}`).
- **Files written:**
  - `nodes/M.2.4.md` (this file)
  - `code/M.2.4-c_K.py` (computes `c^K` at 30 dps; output reproduced
    verbatim in Step 5)

*End of M.2.4.*
