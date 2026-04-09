# Research Note 155 — Stieltjes Derivation of the BC Eigenvalue Shift

**Follow-up to `research/147`–`research/150`.**

*Date:* 2026-04-09
*Author:* G Six, with Claude Opus 4.6.

## 1. Setup

Notes 147–150 established that the BC simple-pole correction acts at
the operator level as γ_n → γ_n + s·δ_n, and a sign-only sweep of nine
candidate δ_n found δ_n = 1/γ_n² the best unified form (24/36). The
sign-only ranking is insensitive to the absolute magnitude of δ_n,
leaving the coefficient undetermined. This note derives δ_n from first
principles using the Laurent expansion of ζ(s) at s=1 in terms of the
**Stieltjes constants** and tests the result against the master table.

## 2. Derivation from the Laurent expansion

The Laurent expansion of ζ at s=1 is

    ζ(s) = 1/(s−1) + Σ_{k≥0} ((−1)^k / k!)·γ_k·(s−1)^k
         = 1/(s−1) + γ_E − γ_1·(s−1) + (γ_2/2)·(s−1)² − …,

with Stieltjes constants γ_E = 0.5772156649…, γ_1 = −0.0728158454…,
γ_2 = −0.0096903632…

Define the **regular part** φ(s) := ζ(s) − 1/(s−1). The BC eigenvalue
equation R̂ Ω_n = R_n Ω_n at β=1 has R_n^(0) = γ_n from the simple
pole; the first-order correction from the regular part, evaluated at
the natural scale ε_n = 1/γ_n, is

    δ_n = φ(1 + 1/γ_n)
        = γ_E − γ_1/γ_n + γ_2/(2 γ_n²) − γ_3/(6 γ_n³) + …

This is an **absolute additive shift** on each eigenvalue:

    γ_n → γ_n + s·(γ_E − γ_1/γ_n + γ_2/(2 γ_n²) − …).

Numerically this converges fast: for n=1 it is 0.5772 + 0.0052 − 2·10⁻⁵
≈ 0.5823; for n≥5 it is γ_E to four decimals. The self-consistent
inversion ζ(β)=γ_n gives β−1 ≈ 1/γ_n + γ_E/γ_n² + …, so the effective
eigenvalue is γ_n^eff = 1/(β−1) ≈ γ_n − γ_E + O(1/γ_n), matching the
Laurent prediction to sign.

## 3. Test against the 36 master-table formulas

Applied with sector-aware sign s = −sign(φ_raw − φ_exp):

| Form                             | Single | Multi | Total |
|:---------------------------------|-------:|------:|------:|
| δ_n = γ_E (constant)             | 14/16  |  9/20 | 23/36 |
| δ_n = γ_E − γ_1/γ_n              | 14/16  |  9/20 | 23/36 |
| δ_n = γ_E − γ_1/γ_n + γ_2/2γ_n²  | 14/16  |  9/20 | 23/36 |
| δ_n = 1/γ_n² (150 winner)        | 14/16  | 10/20 | 24/36 |

Sign-only rankings are **identical** between the full Stieltjes series
and the constant δ_n = γ_E. Magnitude test on the two cleanest
single-zero targets (n_s, ξ):

- **n_s = γ_9/γ_10** raw residual −0.0554 %. The additive shift
  γ_n → γ_n − γ_E (s=−1 cancels in the ratio to leading order but
  leaves a first-order piece γ_E(1/γ_9 − 1/γ_10) = +0.0432 %) closes
  the residual to **−0.0122 %**, matching 148's 1/(γ_9 γ_10)=0.0419 %
  almost exactly. The equivalence 1/(γ_a γ_b) ≃ γ_E·(1/γ_a − 1/γ_b)
  is accidental: 1/(γ_9·γ_10) ≈ 4.19·10⁻⁴, γ_E·(γ_10−γ_9)/(γ_9 γ_10)
  ≈ 4.27·10⁻⁴. They agree at n~10 to 2 %.
- **ξ = γ_1/γ_5** raw −0.1931 %. Additive γ_E shift gives
  γ_E·(γ_5−γ_1)/(γ_1 γ_5) = +2.33 %, a 10× overshoot. The 148 form
  +0.215 % is correct. The two forms diverge when γ_b/γ_a is large.

## 4. Verdict

**Derived form:** δ_n = γ_E − γ_1/γ_n + γ_2/(2 γ_n²) − …, an additive
shift dominated by the Euler–Mascheroni constant γ_E, with the
Stieltjes γ_1 as the leading n-dependent subleading.

**Match quality:**
- Sign test: 23/36, indistinguishable from δ_n = 1/γ_n² (24/36) — the
  sign-only ranking is degenerate across any monotone positive δ_n.
- Magnitude test: matches 148's 1/(γ_a γ_b) on closely-spaced pairs
  (n_s, two-digit improvement) but **overshoots by 10× on widely
  separated pairs (ξ)**. The Laurent-derived form is therefore the
  correct *short-range* limit and fails at long range, confirming
  note 150's claim that the full picture requires a two-term Laurent
  shift (diagonal γ_E-constant + off-diagonal 1/∏γ product coupling).

**Verdict:** The Stieltjes Laurent expansion *does* derive an
eigenvalue shift with the correct structure — δ_n = γ_E + O(1/γ_n) —
and matches the data on closely-spaced pairs, but it **does not
reproduce** the 148/149 product-level 1/(γ_a γ_b) coupling that
dominates widely-spaced ratios. The two pieces are complementary: γ_E
is the diagonal Laurent constant from φ(1), and 1/∏γ is the
off-diagonal coupling between two Laurent inversions — exactly the
two-term structure note 150 predicted. **The Stieltjes derivation
confirms the eigenvalue-shift interpretation at the operator level
and fixes the coefficient of the diagonal shift to γ_E, but does not
subsume the product-level coupling.** First principles give δ_n → γ_E
as n → ∞, not 1/γ_n².

*One-sentence summary:* The Laurent expansion of ζ at s=1 derives an
additive eigenvalue shift δ_n = γ_E − γ_1/γ_n + γ_2/(2γ_n²) − …
dominated by the Euler–Mascheroni constant, matching the 148
correction on closely-spaced ratios (n_s) but overshooting on
widely-spaced ones (ξ) — confirming 150's two-term hypothesis rather
than replacing it.

---

*Derived form:* δ_n = γ_E − γ_1/γ_n + γ_2/(2γ_n²) − … (Stieltjes).
*Sign-test score:* 23/36 (indistinguishable from 150's 1/γ_n²).
*Magnitude match:* short-range yes (n_s), long-range no (ξ).
*Verdict:* derivation confirms operator-level interpretation and
fixes the diagonal coefficient to γ_E; the off-diagonal 1/∏γ
coupling of 148/149 is *not* derivable from the diagonal Laurent
expansion alone and requires the two-zero cross-term.
