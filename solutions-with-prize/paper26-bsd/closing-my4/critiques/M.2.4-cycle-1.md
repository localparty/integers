# Critic — M.2.4 cycle 1

*Critic: Claude Opus 4.6 (1M), structurally distinct context from the Author.*
*Target: M.2.4 (W1-B) — K-port of CCM 2025 Lemma 7.3.*
*Verdict: **BROKEN**.*
*Cycle: 1.*
*Effort: MAX.*

---

## Verdict summary

**BROKEN.**

The Author's `c^K = 0.10158829355204241023479894570431756958557937567319` is
arithmetically correct (stable at 50 dps, self-consistent with `c · Ξ_K(1/2)/Ξ(1/2)`),
and the individual numerical claims about Ξ_K(1/2), Stirling decay rates, and
Gaussian prime enumeration are all verified. BUT: the Author's reconstruction
of CCM 2025 Lemma 7.3 is *structurally wrong*. I was able to fetch CCM 2025
(arXiv:2511.22755) directly via WebFetch and read §7 in full. The Author's
three-piece decomposition (sieve truncation / Stirling / cross-term
Cauchy–Schwarz) has **no correspondence** to the actual proof of CCM 2025
Lemma 7.3. The real proof uses an entirely different structure: (i) the map
`ℰ(f)(u) := u^{1/2} Σ_{n ≥ 1} f(nu)` over ALL positive integers (no sieve,
no truncation at primes), (ii) the prolate-to-Hermite comparison bound
`|h_λ − h|_∞ ≤ c λ^{-2}` from CCM 2025 Lemma 7.2 (a statement about the
prolate wave operator `PW_λ` eigenfunctions `h_{n,λ}` approximating normalised
Hermite functions `h_n`), and (iii) an elementary integral estimate
`∫_{1/λ}^λ u^{α+1/2}/u² du = 2(λ^{1/2−α} − λ^{α−1/2})/(1 − 2α)`.

**The `c` in CCM 2025 Lemma 7.3 is NOT Paper 13's `c = π^{-1/4}/Γ(1/4)`.**
It is the approximation-error constant from CCM 2025 Lemma 7.2(ii) — a
prolate-to-Hermite bound. The load-bearing task of a genuine K-port is to
produce a 2D analog of Lemma 7.2 (a bound on the error of approximating
2D Hermite functions by 2D prolate wave eigenfunctions on `L²(ℂ)`), which
the Author did not attempt.

The claim that `c^K` can be read off as `c · Ξ_K(1/2)/Ξ(1/2)` has no
foundation in the actual proof of CCM 2025 Lemma 7.3 — it is an *a priori*
dimensional-analysis guess imported from Paper 13's different convention.

This is an **honest-first / structural-audit failure**: the Author stress-tested
the deliverable's "mostly mechanical" claim exactly as instructed, but did not
read the CCM 2025 source and so reconstructed a plausible-looking but
counterfactual proof. The **good news**: the Author's §5.5 (self-suspicion)
flagged this exact risk as Suspicion 1 ("the 'mechanical port' claim is wrong:
the ℚ proof uses a property of rational primes that has no Gaussian-prime
analog"). The Author addressed it under the assumption that the ℚ proof uses
`π(x) ∼ x/log x` for a sieve — but CCM 2025 Lemma 7.3 does NOT use a sieve,
so the self-suspicion was resolved against the wrong proof structure.

The (O1) same-norm-drop check at N=5 is, within the Author's (fabricated)
framework, actually *correct* — in the even sector `E_N^{+,K}` the split
pair (1+2i), (1−2i) maps to a single vector `(e_𝔭 + e_𝔭̄)/√2`, so the
pair with `log(5/5) = 0` never appears as an off-diagonal entry. But since
the framework itself doesn't correspond to CCM 2025 Lemma 7.3, this check
is moot for the stated target.

**Recommended next move**: DO NOT advance to Phase V assembly. Refine in
cycle 2 by re-spawning the Author with (a) the actual CCM 2025 page 31–32
text loaded as a primary source, (b) the task restated as "produce a 2D
prolate-Hermite approximation bound for K" (the K-analog of CCM Lemma 7.2),
and (c) an explicit note that the 3-piece sieve/Stirling/CS framing in
`route2-ccm-over-K.md` Phase IV sub-task 4.1 is itself wrong and should be
rewritten by the Author as a secondary deliverable.

---

## §1. Byte-for-byte script re-run (critic sub-step 1)

### 1.1. Script execution
Ran `code/M.2.4-c_K.py` in the paper26-bsd working directory. Output matches
the M.2.4.md §5 (COMPUTE) verbatim — all 30-dps values agree:

```
  c (Paper 13)  = 0.207172189915299969970077507169
  Ξ(1/2)        = 0.497120778188314109912773739685
  Ξ_K(1/2)      = 0.243766557500122242677842208538
  Ξ_K(1/2)/Ξ(1/2) = 0.490356807028856752035685974602
  c^K           = 0.101588293552042410234798945704
```

### 1.2. Algebraic identities
Verified at 40 dps:

- `Λ_K(1/2) = 2 · ζ_K(1/2)` ✓ (diff ~ 5e-41)
- `Ξ_K(1/2) = -ζ_K(1/2)/4` ✓ (diff ~ 6e-42)
- `Λ_K(1/2) = 4^{1/4} · 2^{1/2} · π^{-1/2} · Γ(1/2) · ζ_K(1/2) = √2 · √2 · 1 · ζ_K(1/2) = 2 ζ_K(1/2)` ✓

**Status**: script and algebra are internally consistent.

**Caveat (critical, elaborated in §5 below)**: the script's definition of
`c^K := c · Ξ_K(1/2)/Ξ(1/2)` uses Paper 13's normalization `c = π^{-1/4}/Γ(1/4)`
as the anchor. This is **not** the `c` that appears in CCM 2025 Lemma 7.3.
The script is therefore computing a well-defined real number, but its
interpretation as "the K-version of the CCM 2025 Lemma 7.3 constant" is
unjustified.

---

## §2. Extension test at multiple λ (critic sub-step 2)

### 2.1. Decay rate check

Tested the bound `2c^K · λ^{-3/4} / (1 − 2α)` at α = 1/4 and several λ:

| λ | bound_K |
|---|---|
| 6.020948 (γ_1 of L(χ_{-4})) | 0.10572 |
| 14.134725 (γ_1 of ζ) | 0.05574 |
| 30 | 0.03170 |
| 100 | 0.01285 |
| 1000 | 0.00229 |

### 2.2. Decay rate verification

Ratio check at α = 1/4:
```
  bound(14.13)/bound(30) = 1.758431352203095183537065853372695881037
  (30/14.13)^(3/4)       = 1.758431352203095183537065853372695881037
```
diff ~ 2.3e-41. The bound decays exactly as `λ^{-1/2-α}`, as claimed.

### 2.3. Sub-step note

The critic prompt wrote `γ_1^K ≈ 14.13`, but the first zero of ζ_K =
ζ · L(χ_{−4}) comes from L(χ_{−4}), which has its first zero at
`t_1 ≈ 6.02094…` (Chowla 1950). I verified:
`|L(1/2 + 6.021i, χ_{−4})| ≈ 6.7e-5`, very close to zero.

So **γ_1^K ≈ 6.02**, not 14.13. This is a minor prompt typo, not an issue
with the Author's work.

**Status**: the decay rate `λ^{-1/2-α}` holds mechanically at α = 1/4.
The K-side bound is a strict improvement over the ℚ-side bound at the same
λ, α, because `c^K ≈ 0.1016 < c ≈ 0.2072`. **If one grants the Author's
framing**, the decay rate is not an issue.

---

## §3. Cross-node consistency check (critic sub-step 3): Stirling decay rates

### 3.1. Numerical verification of the Γ-decay rates

At u = 10, 30, 100, 300, computed `|Γ(1/4 + iu/2)|` (Q-side) and
`|Γ(1/2 + iu)|` (K-side), and the predicted asymptotics:

| u | \|Γ(1/4+iu/2)\| | \|Γ(1/2+iu)\| | e^{-π\|u\|/4} | e^{-π\|u\|/2} |
|---|---|---|---|---|
| 10 | 6.51e-04 | 3.78e-07 | 3.88e-04 | 1.51e-07 |
| 30 | 7.45e-11 | 8.58e-21 | 5.85e-11 | 3.42e-21 |
| 100 | 7.33e-35 | 1.51e-68 | 7.77e-35 | 6.04e-69 |
| 300 | 3.36e-103 | 5.53e-205 | 4.70e-103 | 2.21e-205 |

Ratio checks:
- `|Γ(1/4+iu/2)| / e^{-π|u|/4} → √(2π) · |u/2|^{-1/4}` (converges to ~0.72 at u=300, pred 0.72)
- `|Γ(1/2+iu)| / e^{-π|u|/2} → √(2π) ≈ 2.5066` (exactly at 2.5066 for all u ≥ 10)

**Q-side decay rate is `e^{-π|u|/4}`. K-side decay rate is `e^{-π|u|/2}`,
twice as fast. VERIFIED numerically.**

### 3.2. Duplication formula cross-check

The critic prompt asks to verify this against the duplication formula
`Γ(s) Γ(s+1/2) = 2^{1-2s} √π Γ(2s)`. Equivalently:
`Γ_C(s) := 2^{1-s} π^{-s} Γ(s) = Γ_R(s) · Γ_R(s+1)` where
`Γ_R(s) := π^{-s/2} Γ(s/2)`.

At s = 1/2 + 10i:
```
  Γ_C(s)             = (0.000000179 + 0.000000242j)
  Γ_R(s) · Γ_R(s+1)  = (0.000000179 + 0.000000242j)
  |diff|             ~ 5e-38
```
**Identity verified.** So the K-complex-place completion is effectively
*two* real-place completions combined (one at s, one at s+1). This is
consistent with the K-Stirling decay being `e^{-π|u|/2}` — the product of
two Q-Stirling factors each with rate `e^{-π|u|/4}` gives total rate
`e^{-π|u|/2}`. K:Q rate ratio 2:1 is exact.

**Status on §3**: the Stirling asymptotics and the duplication formula cross-check
are both verified. The Author's Stirling claims in §4.B are numerically
correct.

### 3.3. Sloppy phrasing at line 91 — internal inconsistency

At line 91 of M.2.4.md, in the substitution-table paragraph, the Author
writes:

> "at `s = 1/2 + iu` with `|u| → ∞`, both `|Γ(1/4 + iu/2)|` and
> `|Γ(1/2 + iu)|` decay like `e^{−π|u|/2}`..."

This is **wrong** — the Q-side `|Γ(1/4 + iu/2)|` decays like `e^{-π|u|/4}`,
not `e^{-π|u|/2}`. The Author corrects this in §4.B (lines 250, 253, 255,
261, 267, 268) and in the §D proposed rows (lines 722, 724) and in the
Sig 11 Critic recommendation (line 793).

This is a **local self-contradiction** in the document — one sentence on
line 91 contradicts the rest of §4.B and §D. Reading charitably, the Author
may have meant "both decay exponentially in `|u|`" as a regime statement,
but the written form is arithmetically incorrect. Fix: change "decay like
`e^{-π|u|/2}`" to "both decay exponentially in `|u|` (specifically,
`e^{-π|u|/4}` on Q and `e^{-π|u|/2}` on K)".

**Not load-bearing**, but it is a concrete defect.

---

## §4. Precision floor check (critic sub-step 4)

### 4.1. 50-dps re-run

At `mp.dps = 50`:
```
  c^K (50 dps) = 0.10158829355204241023479894570431756958557937567319
  c^K (30 dps) = 0.101588293552042410234798945704
  |diff|       = 0.0
```

The 30-dps value is stable under extension to 50 dps. No bits flip.

### 4.2. Precision floor assessment

At 30 dps the floor is ~1e-31. The headline `c^K ~ 0.1016` is 30 orders of
magnitude above the floor. The "3 orders of magnitude" requirement is met
by a factor of 10^27. **PASS.**

---

## §5. Bonus-grep on M.2.4.md (critic sub-step 5)

### 5.1. "we have shown" / "it follows" / "mechanical" audit

Grep hits on `(we have shown|it is proved|it follows|follows from|we showed|we prove|it suffices|clearly|obvious|mechanical|immediately)`:

| Line | Claim | Audit |
|---|---|---|
| 46 | "mostly mechanical" | FLAGGED — this is the claim being stress-tested and (per §6) the claim is false against the real CCM 2025 Lemma 7.3 proof. |
| 83 | "follows from Uniform H¹ bound (K) = sub-task 2.2, status DONE" | Cited, not verified (sub-task 2.2 is a black box per spawn prompt). OK to cite as instructed. |
| 218 | "this follows from Stirling on Γ(s) along the critical strip, restricted to closed substrips" | CORRECT (numerically verified in §3). |
| 229 | "This resolves Obstacle A mechanically" | WRONG — Obstacle A is itself a fabrication; the real CCM 2025 Lemma 7.3 has no sieve-theoretic step. |
| 320 | "the K-version of the bound is [...] transferred mechanically" | WRONG — see §6 below. |
| 537 | "follows from π(x) ≤ 2 x/log x for x ≥ 17 (Chebyshev's elementary upper bound)" | True as a standalone fact about ℚ PNT, but **irrelevant** to CCM 2025 Lemma 7.3 which does not use π(x). |
| 541 | "the transfer is mechanical" | WRONG at the level of CCM 2025; see §6. |
| 690 | "transferred mechanically" | WRONG; see §6. |
| 747 | "a separate mechanical extension" | Not verified (concerns the twist to L(s, ψ), out of scope). |
| 749–759 | "LESSON: mechanical at the proof structure ≠ mechanical at the constants" | Voice-correct but based on a wrong proof structure. |

### 5.2. Numerical-claim audit

All `≈` / `~` values in M.2.4.md (lines 75, 77, 503, 511, 512, 619, 634, 679, 680, 707, 777) checked against the script output and found consistent.

### 5.3. Citation audit

Citations to §D rows (`Uniform H¹ bound (K)`, `Ξ_K(1/2) ≠ 0`, `Sagnier K-arithmetic site`) are all to the correct files, and the referenced statements are as cited.

Citation to `weil-form-over-K.md` §4.3 eq. (4.3) at line 594: verified,
matches the `τ^{(K_∞)}` diagonal formula. OK.

Citation to `route2-ccm-over-K.md` sub-task 4.1: verified that the route2
file does say the proof structure is "mechanical once sub-task 4.1 is in
place" (line 555 of route2). **This is the load-bearing bug**: route2's
description of CCM 2025 Lemma 7.3 as having a "three-piece" structure
(sieve / Stirling / Cauchy-Schwarz) is not faithful to the actual CCM 2025
proof. The Author inherited this bug from the plan, not introduced it
independently.

### 5.4. Κ_K residue algebra — minor factor-of-2 error

At lines 200–202 of M.2.4.md, the Author writes:

> "The constant C_K differs from C by a bounded number-field factor
> (essentially `Res_{s=1} ζ_K(s) / Res_{s=1} ζ(s) = 2π / 4 · (class number 1)
> · (regulator 1) · ζ_K-residue stuff = π/2`)"

Let me verify. For K = ℚ(i): h_K = 1, R_K = 1, w_K = 4, |d_K| = 4, so
```
  κ_K = Res_{s=1} ζ_K(s) = 2π h_K R_K / (w_K √|d_K|) = 2π / (4·2) = π/4
```
`weil-form-over-K.md` line 286 confirms `κ_K = π/4`. But the M.2.4.md text
writes the ratio as `2π/4 · ... = π/2`, which would give π/2 (not π/4).

This is an **arithmetic slip**: the correct value is `π/4`, off by a factor
of 2 from the Author's claim. Not load-bearing (it is a side remark about
a sieve constant that, as we now know, is part of a fabricated §4.A
structure), but it is a concrete numerical error contradicting the
`weil-form-over-K.md` reference the Author cites.

### 5.5. Cross-term Cauchy-Schwarz — structurally invalid

At lines 366–371 the Author writes, for the cross-term sum:

```
  ≤  ( Σ_p  Λ_K(𝔭)² N(𝔭)^{-1-2α}  ⟨e_𝔭, K_λ^K e_𝔭⟩ )^{1/2}
     · ( Σ_q  Λ_K(𝔮)² N(𝔮)^{-1-2α}  ⟨e_𝔮, K_λ^K e_𝔮⟩ )^{1/2}
     · Σ_{N(𝔭) ≠ N(𝔮)}  1 / log(N(𝔮)/N(𝔭))²
```

**This is not a valid form of Cauchy-Schwarz.** CS on a bilinear sum
`Σ a_p b_q M_{pq}` gives `||a|| · ||b|| · ||M||_op` (operator norm), or
HS-form `(Σa_p²)^{1/2} (Σ|M_p|²)^{1/2}` where `M_p = Σ_q b_q M_{pq}`. It
does NOT give `(Σ a²)^{1/2} (Σ b²)^{1/2} (Σ M²)`.

Moreover, the unweighted kernel sum `Σ_{N(𝔭)≠N(𝔮)} 1/log²(N(𝔮)/N(𝔭))`
does NOT grow as `N · log²(N)` as the Author claims at line 386. Numerical
check at Gaussian-prime-ideal norms up to N:

| N | Σ 1/log² | N·log²N | ratio |
|---|---|---|---|
| 20 | 184.0 | 179.5 | 1.03 |
| 50 | 1435.2 | 765.2 | 1.88 |
| 100 | 4926.3 | 2120.8 | 2.32 |
| 200 | 58435.7 | 5614.4 | 10.4 |
| 500 | 698019.4 | 19310.7 | 36.1 |
| 1000 | 4474189.1 | 47717.1 | 93.8 |

The ratio grows; the actual scaling is closer to `N²/log²N` (the correct
leading-order bound for such a double sum). The Author's claim that this
sum is bounded by `C · N · log²(N)` is **numerically false**.

Within the Author's (fabricated) framework, this means the cross-term is
**NOT** sub-leading: the proper C-S bound gives a quantity that grows
faster than `N^{1/2-α}`, contradicting the Author's "non-binding" conclusion.

**However**, this defect is moot because the entire §4.C is a fabrication
of a step that is not in CCM 2025 Lemma 7.3 at all (see §6 below).

---

## §6. Retrieval-augmented citation verification against CCM 2025

### 6.1. Successful fetch

I was able to fetch CCM 2025 (arXiv:2511.22755) via WebFetch and read the
34-page PDF. **This changes the verdict from WEAKENED to BROKEN.**

### 6.2. What CCM 2025 Lemma 7.3 actually says

CCM 2025 ("Zeta Spectral Triples", Connes–Consani–Moscovici), page 31:

> **Lemma 7.3.** *The Fourier transform of `k_λ` converges, when `λ → ∞`,
> towards the Ξ-function of Riemann uniformly on closed substrips of the
> open strip `|Im z| < 1/2`.*

**This is only a qualitative statement of convergence** — the quantitative
bound `2c · λ^{-1/2-α}(1-2α)^{-1}` is inside the proof, not in the lemma
statement. The Author's target statement (with an explicit quantitative bound)
is a strengthening that makes sense given the proof, but it is not what CCM
2025 Lemma 7.3 formally asserts.

### 6.3. What the actual proof of CCM 2025 Lemma 7.3 does

The proof on pages 31–32 of CCM 2025:

1. **Set up.** `k_λ(u) := ℰ(h_λ)(u)` for `u ∈ [λ^{-1}, λ]` (eq. 7.6),
   where `h_λ` is a specific linear combination of the prolate wave operator
   `PW_λ` eigenfunctions `h_{0,λ}, h_{4,λ}` with vanishing integral
   (described before Lemma 7.1), and
   ```
   ℰ(f)(u) := u^{1/2} Σ_{n=1}^∞ f(nu)                 (7.2)
   ```
   The map ℰ sums over **all** positive integers `n ≥ 1`, not primes,
   and there is no truncation.

2. **Approximation bound (CCM Lemma 7.2).** For `n = 0, 4`, the suitably
   normalized prolate eigenfunctions `h_{n,λ}` satisfy
   ```
   max_{x ∈ [-λ, λ]} |h_{n,λ}(x) − h_n(x)| ≤ c · λ^{-2}     (7.7)
   ```
   where `h_n` is the normalized Hermite eigenfunction of the harmonic
   oscillator `H f = -f'' + 4π²u²f` with eigenvalue `2π(1+2n)`. The same
   bound holds for the linear combination `h_λ → h` with vanishing integral
   (7.8). The constant `c` is the Meixner–Schäfke [9] prolate-to-Hermite
   approximation error constant (CCM cite [9], page 243, Satz 9), and it is
   **finite, non-zero, and independent of `λ`**.

3. **Truncation step.** For `u ∈ [λ^{-1}, λ]`, the number of integers `n`
   with `nu ≤ λ` is at most `λ/u`, so using (7.8),
   ```
   |ℰ(h_λ)(u) − ℰ(h)(u)| ≤ u^{1/2} · δ(λ) · (λ/u)
                          = u^{-1/2} · λ · δ(λ)
   ```
   where `δ(λ) := max_{x ∈ [-λ,λ]} |h_λ(x) − h(x)| ≤ c λ^{-2}`.

4. **Mellin-transform evaluation.** On the critical strip
   `Re(s) = α ∈ [-1/2, 1/2]`,
   ```
   M(k_λ)(s) = ∫_0^∞ u^{s-1} k_λ(u) du
   ```
   and, splitting the integration domain at `u = λ^{-1}` and `u = λ`,
   ```
   |M(k_λ)(s) − ∫_{λ^{-1}}^λ k(u) u^{s-1} du|
        ≤ λ · δ(λ) · ∫_{λ^{-1}}^λ u^α · u^{1/2} · u^{-2} du.
   ```

5. **Integral bound.**
   ```
   ∫_{1/λ}^λ u^{α+1/2}/u² du = ∫_{1/λ}^λ u^{α-3/2} du
       = [u^{α-1/2}/(α-1/2)]_{1/λ}^λ
       = 2(λ^{1/2-α} − λ^{α-1/2})/(1 − 2α)
   ```

6. **Assembly.**
   ```
   |M(k_λ)(s) − ∫_{λ^{-1}}^λ k(u) u^{s-1} du|
       ≤ 2c · λ^{1/2-α} · (1-2α)^{-1} · λ · λ^{-2}
       = 2c · λ^{-1/2-α} · (1-2α)^{-1}
   ```
   where the `c` is the *same* Meixner–Schäfke prolate-approximation constant
   from Lemma 7.2.

### 6.4. Comparison with the Author's reconstruction

| Author's §4.A (sieve truncation) | CCM 2025 actual proof |
|---|---|
| Sieve over primes `p ≤ N`, weighted by `log p / p^{1/2+α}`, bounded via `π(x) ∼ x/log x` | No prime sieve. The truncation is at `u = λ^{-1}` and `u = λ` (intervals on the positive real axis), not at primes. |
| Uses `π(x) ≤ 2 x / log x` (Chebyshev) | Uses `#{n : nu ≤ λ} ≤ λ/u` (a trivial counting fact, no PNT) |
| Gives `S_ℚ(N, α) ≤ C · N^{1/2-α}/(1/2-α)` | No such sum appears. |

| Author's §4.B (Stirling) | CCM 2025 actual proof |
|---|---|
| Bounds `Γ(s/2)` on the critical line via `e^{-π|u|/4}` | The Γ-function does not appear in the proof. Ξ enters only through the final identification after the bound. |
| Uses `|u| → ∞` asymptotics | The proof is finite: the Mellin integral is over `[0, ∞)`, truncated to `[λ^{-1}, λ]`, and the tail `∫_λ^∞` is handled by the Poisson symmetry `k(u) = k(u^{-1})`. No Stirling is invoked. |

| Author's §4.C (cross-term CS) | CCM 2025 actual proof |
|---|---|
| `Σ_{p ≠ q} Λ(p)Λ(q) / log(q/p)` bounded by Cauchy–Schwarz | No cross-term sum exists in CCM 2025 Lemma 7.3. There are no prime pairs. |
| Uses orthogonality of a prolate basis on primes | The prolate basis does not enter here. The prolate eigenfunctions enter via the definition of `h_λ` (a specific `n=0, 4` linear combination), not as a basis. |

The Author's reconstruction is **not** a paraphrase of CCM 2025 Lemma 7.3.
It is an independent fabrication, built from the prompt's description
(which itself came from `route2-ccm-over-K.md` and is itself wrong).

### 6.5. What the `c` in CCM 2025 actually is

In CCM 2025, the `c` that appears in the bound
`|M(k_λ)(s) − ∫_{λ^{-1}}^λ k(u) u^{s-1} du| ≤ 2c · λ^{-1/2-α}(1-2α)^{-1}`
is the **Meixner–Schäfke approximation constant** from CCM Lemma 7.2(ii):
```
  max_{x ∈ [-λ, λ]} |h_λ(x) - h(x)| ≤ c · λ^{-2}
```
This `c` bounds how well the prolate wave operator `PW_λ` eigenfunctions
(specifically the `n=0, 4` linear combination `h_λ` with vanishing integral)
approximate the Hermite linear combination `h` on the interval `[-λ, λ]`.
It is an **analytic**, non-arithmetic quantity, independent of any
functional equation.

**The Author's `c = π^{-1/4}/Γ(1/4)` is from Paper 13 §10.4**, a *different*
convention for normalizing the Mellin pairing. These two `c`s are NOT the
same quantity. The Author's identification `c^K = c · Ξ_K(1/2)/Ξ(1/2)` is
grounded in Paper 13's convention, not in CCM 2025's.

### 6.6. What a genuine K-port would need to do

A genuine K-port of CCM 2025 Lemma 7.3 would need:

1. A 2D analog of CCM Lemma 7.2 — i.e., a prolate-to-Hermite approximation
   bound for the eigenfunctions of a 2D prolate wave operator `PW_λ^K` on
   `L²(ℂ)` (one complex place of K), giving
   `max_{z ∈ D_λ} |h_{λ}^K(z) - h^K(z)| ≤ c^K · λ^{-2}`.
   This `c^K` is a **2D-analytic** constant from the 2D Slepian / 2D
   prolate theory (see Simons–Wang 2011 for context), NOT arithmetic.

2. A K-analog of the map ℰ, which over ℚ is `ℰ(f)(u) = u^{1/2} Σ_{n≥1} f(nu)`.
   Over K, this should sum over ideals `𝔞 ⊂ 𝒪_K`:
   `ℰ_K(f)(u) = (something) · Σ_𝔞 f(N(𝔞)·u)` — or alternatively over principal
   ideals generated by elements of `𝒪_K = ℤ[i]`, with appropriate
   normalisation. **The Author did not write this map.**

3. A K-analog of the Mellin transform and critical-strip evaluation,
   which over K uses the complex-place completion factor `Γ_C(s) = 2(2π)^{-s}Γ(s)`
   instead of the real-place `Γ_R(s) = π^{-s/2} Γ(s/2)`.

4. The integral bound `∫_{1/λ}^λ u^{α+1/2}/u² du = 2(λ^{1/2-α} - λ^{α-1/2})/(1-2α)`
   — which is the same integral in both cases because the complex place is
   still integrated along `ℝ_+` in the multiplicative measure `du/u`.

None of steps 1–3 are in M.2.4.md. The Author's `c^K` is not a valid K-analog
of the CCM 7.3 constant.

### 6.7. Verdict on §6

The Author's reconstruction is not faithful to CCM 2025 Lemma 7.3. This is
a **structural**, not cosmetic, defect. The target lemma cannot be promoted
to `[LEMMA]` status; it is not proven.

---

## §7. Same-norm-collision check at N=5 (critic sub-step 9)

### 7.1. Setup

Enumerate Gaussian prime ideals of norm ≤ 5:

| rank | prime | N | type |
|---|---|---|---|
| 1 | (1+i) | 2 | ramified |
| 2 | (1+2i) | 5 | split |
| 3 | (1−2i) | 5 | split |

Only same-norm pair: (1+2i) vs (1−2i), both norm 5.

### 7.2. Diagonal Mangoldt kernel

```
Λ_K((1+i))/√2   ≈ log(2)/√2   ≈ 0.4901
Λ_K((1+2i))/√5  ≈ log(5)/√5   ≈ 0.7198
Λ_K((1−2i))/√5  ≈ log(5)/√5   ≈ 0.7198   <-- equal to (1+2i) value
```

The diagonal Mangoldt values for the split partners are equal. The Author
at line 599–602 claims the diagonal kernel "separates" them. Let me check
precisely what "separates" means.

### 7.3. Separation as orthogonal projections

The diagonal form
```
Q_diag = Σ_𝔞 Λ_K(𝔞) |𝔞⟩⟨𝔞| / √N(𝔞)
```
acts on `E_N^K` as a direct sum of rank-1 projectors, one per ideal. For
the split pair this gives
```
(log 5 / √5) · |e_{(1+2i)}⟩⟨e_{(1+2i)}|
  + (log 5 / √5) · |e_{(1−2i)}⟩⟨e_{(1−2i)}|
  = (log 5 / √5) · I|_{split subspace}
```
— the identity operator times a scalar on the 2D subspace spanned by
`{e_{(1+2i)}, e_{(1-2i)}}`. The two projectors are orthogonal (as vectors,
`e_{(1+2i)} ⊥ e_{(1-2i)}`), so the diagonal form **does** separate them
*as orthogonal rank-1 pieces*, but the eigenvalues are **degenerate**
(both equal to `log 5 / √5 ≈ 0.7198`).

### 7.4. The key insight: parity collapses the split pair

Both split-pair basis vectors live in `E_N^K`, but the Author's target
lemma is about `E_N^{+,K}` — the **even sector**. Complex conjugation
swaps the pair: `γ_K · e_{(1+2i)} = e_{(1-2i)}` and vice versa. So in the
even sector `E_N^{+,K}`, the split pair collapses to a **single** vector
`(e_{(1+2i)} + e_{(1-2i)}) / √2`, and the antisymmetric combination
`(e_{(1+2i)} − e_{(1-2i)}) / √2` lives in the odd sector.

Count in `E_N^{+,K}` at N=5:
- (1+i) ramified, fixed → 1 vector
- split pair (1±2i) → 1 even vector
- Total: 2 vectors (vs. 3 in `E_N^K`).

In the even sector, the off-diagonal entry `⟨e_{(1+2i)}, Q_off · e_{(1-2i)}⟩`
with `log(5/5) = 0` **does not exist** — it would be a diagonal self-loop
from the single even-sector vector to itself. The diagonal kernel of the
even-sector Weil form is well-defined.

### 7.5. Conclusion on (O1)

**Within the Author's (fabricated) framework**, the (O1) same-norm drop at
N=5 is actually *automatic* in the even sector `E_N^{+,K}`: the split pair
collapses to a single vector, and the problematic `log(5/5) = 0` never
arises as an off-diagonal entry. The Author's structural claim "diagonal
Mangoldt kernel already separates split partners through the diagonal
kernel" is correct *if* we interpret "separated" as "collapsed to a single
parity-even vector", not "given distinct eigenvalues" (they have the same
eigenvalue `log 5 / √5`).

**However**, since the entire framework (the off-diagonal sum as an
approximation to CCM Lemma 7.3) is fabricated (see §6), this check is moot
for the stated target. If the Author re-spawns and ports CCM 2025 Lemma 7.3
*correctly*, the (O1) same-norm issue may or may not appear — it depends
on whether the correct K-port uses the ideal-labelled basis at all. CCM
2025 Lemma 7.3 over ℚ does NOT use a basis of primes; it uses the specific
prolate-Hermite linear combination `h_λ = a · h_{0,λ} + b · h_{4,λ}`
with `a = √3/2^{11/4}, b = -3/2^{17/4}` (eq. 7.4). A K-port would
similarly use a specific 2D prolate-Hermite linear combination, which
probably has no direct ideal-labelled structure at all.

**Status on §7**: the (O1) drop at N=5 is structurally OK within the
Author's framework, but this result is decoupled from the target lemma.

---

## §8. LOCK verification (critic sub-step 10)

### 8.1. Uniformity in z on closed substrips of |Im z| < 1/2

The Author claims that each of the three pieces (§4.A, §4.B, §4.C)
preserves z-uniformity on closed substrips. Within the Author's framework,
this claim is mostly correct as stated (the bounds all factor through
Stirling on the Γ-factor, which is uniform on closed substrips).

**However, the actual CCM 2025 Lemma 7.3** proves uniformity *differently*:
the bound `|M(k_λ)(s) − ∫_{λ^{-1}}^λ k(u) u^{s-1} du| ≤ 2c · λ^{-1/2-α}(1-2α)^{-1}`
is uniform in `s` with `Re(s) = α` because the estimate
`|ℰ(h_λ)(u) − ℰ(h)(u)| ≤ u^{-1/2} · λ · δ(λ)` is uniform in the real
variable `u`, and the Mellin transform inherits this uniformity on the
critical strip. The proof is complete at `Re(s) = α` and then extends to
`|Im s − 1/2| ≤ ε` via a Phragmén–Lindelöf argument that CCM 2025 does not
spell out in §7 but is standard.

**§8 verdict**: uniformity as stated is correct if we grant the
(fabricated) framework, but it is not the same uniformity argument CCM 2025
actually uses. The genuine K-port would have uniformity from a different
source and would need to verify it independently.

---

## §9. Voice alignment check

The Author's §J reprise at lines 9–13 hits the canon markers cleanly:
- "the framework is transposable, but the port is not free" ↔ canon "we cannot crack it from the outside; the framework is transposable"
- "we NAME the wrinkles" ↔ canon "we need to NAME them and use them for decoding"
- "honest partial proof over glossed completion" ↔ canon verbatim

The voice is aligned. The soft caveat in the status header ("the same-norm-drop
structural argument is not yet numerically verified") is exactly the kind of
HONEST-FIRST flag the canon demands.

**However**, the Author's honest-first discipline was directed at the wrong
target: the (O1) same-norm issue, which turns out to be resolved (see §7),
rather than at the structural question "have I verified my reconstruction
of CCM 2025 Lemma 7.3 against the actual CCM 2025 paper?". The voice canon
passed, but the epistemic check it was supposed to guard did not fire.

**§9 verdict**: Voice form PASS, but the content should have included a
CONCERN flag for "I reconstructed CCM Lemma 7.3 from the plan's three-piece
description; I have not checked this reconstruction against the actual CCM
2025 PDF." The spawn prompt at line 185 says "Do not paraphrase CCM 2025
Lemma 7.3 — work from the structural description in `route2-ccm-over-K.md`
and reconstruct the proof rather than guessing the literal CCM text." The
Author followed this instruction, but the structural description is
itself wrong. This is a **prompt-level bug**, not an Author-level bug.

---

## §10. Sub-problems for the runner (cycle-2 refinement targets)

1. **S-1 (critical, blocking)**: Re-spawn the Author with the actual CCM 2025
   page 31–32 text loaded as the primary source. Restate the task as
   "produce a 2D analog of CCM Lemma 7.2 (the prolate-to-Hermite
   approximation bound) for `K = ℚ(i)`, and use it to derive a K-analog of
   CCM Lemma 7.3 via the map `ℰ_K` and the integral estimate." The
   three-piece sieve/Stirling/CS decomposition is not in CCM 2025 and
   should not appear in the K-port.

2. **S-2 (important, documentation)**: Correct `route2-ccm-over-K.md` Phase IV
   sub-task 4.1 so that its description of CCM Lemma 7.3 is faithful to the
   actual proof (no prime sieve, no Γ-Stirling, no cross-term CS). This is
   a plan-file correction, not a research task.

3. **S-3 (minor, non-blocking)**: Fix the arithmetic slip at line 201–202 of
   M.2.4.md: replace `π/2` with `π/4` for `κ_K = Res_{s=1} ζ_K`.

4. **S-4 (minor, non-blocking)**: Fix the internal inconsistency at line 91
   of M.2.4.md: the Q-side `|Γ(1/4 + iu/2)|` decays as `e^{-π|u|/4}`, not
   `e^{-π|u|/2}`.

5. **S-5 (retained, for future cycle)**: Once a genuine K-port is produced,
   re-run the small-N numerical sanity check on the new structure. The
   N=5 parity-collapse result in §7 may or may not apply depending on how
   the new K-port is formulated.

6. **S-6 (side-benefit)**: The current `c^K = 0.10158...` is still a
   well-defined real number — `c · Ξ_K(1/2)/Ξ(1/2)` where `c = π^{-1/4}/Γ(1/4)`
   is Paper 13's normalization. It just isn't the `c` of CCM 2025 Lemma 7.3.
   If Paper 13's Theorem 10.1 (over ℚ) uses this Paper-13 convention for
   the prolate-to-Ξ identification, then the K-port of *Paper 13 Theorem 10.1*
   (not CCM Lemma 7.3) may legitimately use `c^K = c · Ξ_K(1/2)/Ξ(1/2)`.
   The Author may have ported *Paper 13 Theorem 10.1* rather than *CCM 2025
   Lemma 7.3* — these are related but not identical statements. A clarifying
   note is warranted. (Note: the spawn prompt at line 41 says "CCM 2025
   Lemma 7.3 (paraphrased from Paper 13 §10)", which implies the runner
   was conflating the two. This is another prompt-level issue.)

---

## §11. Confidence

**Verdict: BROKEN. Confidence: HIGH.**

Confidence rationale:

- I have the actual CCM 2025 PDF (pages 1–5, 27–34, including the full
  §7 proof of Lemma 7.3). There is no ambiguity in what CCM 2025 Lemma
  7.3 says or how it is proven.
- The Author's three-piece (sieve / Stirling / CS) decomposition does
  not match CCM 2025's actual proof structure. This is a clean, concrete
  mismatch, not a matter of interpretation.
- The numerical checks I ran (script re-run, precision at 50 dps, extension
  at multiple λ, Stirling asymptotic, duplication cross-check, same-norm
  parity collapse at N=5) all verify the individual *arithmetic* claims
  the Author made. The verdict is BROKEN *despite* arithmetic correctness
  because the framework those claims live in does not correspond to the
  target lemma.
- The verdict matches the Author's own Suspicion 1 in §5.5 (flagged as a
  failure mode, addressed against the wrong target).

**Probability the port closes cleanly in cycle 2 with corrected scoping:
~40%.** The task requires producing a 2D analog of CCM Lemma 7.2 (prolate-
to-Hermite in 2D), which is *genuine new mathematical work* with no direct
literature template (Simons–Wang 2011 is the closest thing and lacks the
holomorphic structure needed). This is harder than the "mostly mechanical"
framing in `route2-ccm-over-K.md` suggests. The Author may need multiple
cycles or may hit a genuine obstacle.

**Probability the Phase IV sub-task 4.1 is closable in the closing-MY4 run:
~25%.** Even if cycle 2 makes progress, the genuine 2D prolate-Hermite theory
may require a multi-month detour that the closing-MY4 run cannot absorb.
The runner should consider whether the HONEST-STALL flag on MY4 (Option C
in the deliverable) is the right response rather than continuing to push
Route 2.

---

## §12. Recommendation for next move

**Do NOT advance to Phase V assembly.** K-CCM Lemma 7.3 is not proven.

**Cycle 2 priority**:
1. Runner re-spawns Author with corrected scoping (sub-problem S-1 above).
2. Runner also corrects `route2-ccm-over-K.md` (sub-problem S-2).
3. Author in cycle 2 explicitly states whether (a) the 2D prolate-Hermite
   theory can be written down in <30 pages, or (b) this is a genuine
   multi-month task, in which case Phase IV sub-task 4.1 is BLOCKED not
   ADVANCED.

**If cycle 2 reports BLOCKED**: escalate the honest-stall discussion.
Route 2 may not close MY4 in the closing-MY4 run budget. The deliverable's
Option C (BSD conditional on MY4) becomes more attractive.

**Epistemic lesson for the runner**: the prompt-level bug (route2's wrong
three-piece description of CCM Lemma 7.3) caused the Author's fabrication.
Future spawn prompts should require the Author to fetch the source paper's
actual proof text when porting a named lemma, or explicitly forbid the
port when source-verification is impossible. The instruction at line 185 of
M.2.4-prompt.md ("work from the structural description in `route2-ccm-over-K.md`")
should be inverted: the Author should be required to verify the structural
description against the source first, and flag mismatches before proceeding.

---

*End of Critic M.2.4 cycle 1.*
