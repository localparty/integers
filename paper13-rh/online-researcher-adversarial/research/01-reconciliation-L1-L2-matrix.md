# Reconciliation: L1 vs L2 QW^N_λ matrix at (λ=4, N=30)

Read-only diagnostic. Goal: explain the 47-order-of-magnitude disagreement
between the two executors' reported simplicity gap at (λ=4, N=30).

Scripts examined:
- `code/lead-1-verify-ccm-convergence.py` (L1)
- `code/lead-2-verify-cf-even-simple.py` (L2)
- `code/lead-2-structure-check.py` (L2's CF-structure test)

Reference: CCM-2025 (`sources/ccm-zeta-spectral-triples-2025.pdf`), §3–5.
In particular, equations (3.10), (3.19), (4.2)–(4.14), Proposition 4.3,
Lemmas 5.1–5.2, Definition 5.3.

---

## §1. Diagnosis summary — what each script is computing

**Both scripts agree on these parameter conventions (which are correct per the paper):**
- Bandwidth: `L = 2 log λ` (not `L = λ`). Both use this. ✓
- Prime cutoff: `k = p^j ≤ λ² = e^L` (von Mangoldt sum, Λ(k)=log p). Both use this. ✓
- Basis size: `N` is the **half-index** so that `|n| ≤ N` and the matrix dimension is `2N+1 = 61` at N=30. Both use this. ✓
- Sign structure from eq (3.10)/(3.19): `QW^N_λ = W_{0,2} − W_R − Σ_p W_p`. Both use this. ✓
- `W_{0,2}` per Lemma 4.1 (eq 4.2). Both identical, and they agree numerically to ≥ 15 digits. ✓
- `q(U_n, U_m)(y)` per eq (2.9)/(2.10) and Lemma 2.3. Both identical. ✓
- α_L(n) per eq (4.12): `(1/π) ∫₀^L sin(2πnx/L) ρ(x) dx` with ρ(x)=exp(x/2)/(exp(x)−exp(−x)).
  L1 evaluates by mpmath `quad`, L2 evaluates via the closed form (eq 4.5 on page 14).
  **Both agree exactly** (≥ 18 digits, all n tested). ✓
- β_L(n) per eq (4.13). Again, L1 uses quad, L2 uses closed form. **Both agree exactly.** ✓

**Where they diverge:** The γ_L(n) term (diagonal contribution of W_R) and the off-diagonal
W_R sign convention.

### L1 (lead-1-verify-ccm-convergence.py)

- Computes γ_L(n) by direct quadrature of the (cos(2πnx/L) − exp(−x/2))·ρ integrand
  (matching eq 4.14 *as literally written in the paper*) and **adds the page-15 reduced
  form of c(L)+w(L)**:
  ```
  c+w = (1/2) log((e^{L/2}-1)/(e^{L/2}+1)) + atan(e^{L/2}) - π/4 + γ_E/2 + (1/2) log(8π)
  ```
  (Lines 91–112.)
- W_R diagonal: `2γ_L(n) − 2β_L(n)`. (Line 126.)
- W_R off-diagonal: `(α_L(m) − α_L(n)) / (n − m)` — **matches Prop 4.3 exactly**. (Line 124.)
- Full matrix assembled with `W02 − WR − Wp`; then symmetrized. Diagonalized on the
  **+1-eigenspace of γ (even sector)** of dimension `N+1 = 31`.

### L2 (lead-2-verify-cf-even-simple.py)

- Computes γ_L(n) via the closed-form evaluation of the (cos(2πnx/L) − 1)·ρ integral
  plus **L2's "c(L)" and "w(L)"** as separate terms:
  ```
  c(L) = log(e^{L/2}+1) + (1/4)(-2 log(e^L+1) - π - log 4) + atan(e^{L/2})
  w(L) = (1/2)(γ_E + log(4π)) - (1/2) log((e^L+1)/(e^L-1))
  ```
  (Lines 135–161.)
- W_R diagonal: `2γ_L(n) − 2β_L(n)`. (Line 166.)
- W_R off-diagonal: `(α_L(m) − α_L(n)) / (m − n)` — **SIGN FLIPPED relative to Prop 4.3**. (Line 167.)
- Full matrix assembled with `W02 − WR − Wp`, symmetrized, diagonalized on the **full
  (2N+1)-dimensional space** (no even-sector projection).

---

## §2. Spot-check output at (λ=4, N=30)

`mp.dps = 60`. Dimension of both raw matrices: **61 × 61**. Both real and symmetric to ≥ 55 digits.

### Sample matrix entries

| Entry | L1 | L2 | L2 − L1 |
|---|---|---|---|
| T[0, 0] (=n=−30, m=−30) | 0.81900050 | 2.82229360 | +2.00329 |
| T[0, 1] | −0.33059488 | −0.33059517 | ≈0 (−2.9e−7) |
| T[30, 30] (n=0, m=0) | −1.35518323 | +0.64810987 | +2.00329 |
| T[30, 31] (n=0, m=1) | +0.03340557 | −0.47430472 | −0.50771 |
| T[30, 32] (n=0, m=2) | +0.03427002 | −0.21611793 | −0.25039 |
| T[30, 35] (n=0, m=5) | +0.04790199 | −0.05209849 | −0.10000 |
| T[31, 31] (n=1) | −1.35437724 | +0.64891586 | +2.00329 |
| T[31, 32] | +0.03513446 | +0.04206885 | +0.00693 |
| T[35, 35] (n=5) | −1.26635527 | +0.73693783 | +2.00329 |
| T[40, 40] (n=10) | −1.00017070 | +1.00312240 | +2.00329 |
| trace(T) | +5.35593 | +127.55681 | +122.20088 (=61·2.00329) |

**Observation #1**: Every diagonal entry differs by the same constant **+2.00329**. This is
a pure constant shift of the diagonal, i.e. `T2_diag = T1_diag + 2.00329 · I`.

**Observation #2**: Off-diagonal entries involving index 30 (n=0) differ by large amounts
whose pattern matches `2·α_L(m)/m` (e.g. 2·0.2539 = 0.5078 at m=1; 2·0.1252 = 0.2504 at
m=2; etc). For off-diagonals *not* involving n=0, the differences are much smaller
(O(10⁻³) at (n,m) = (1,2) and decay rapidly).

This pattern matches exactly the consequence of flipping the sign of the W_R off-diagonal
formula, because on the n=0 row W_R_correct[0, m] = (α_L(m) − α_L(0))/(0 − m) = −α_L(m)/m,
whereas L2's formula gives +α_L(m)/m; the difference is 2·α_L(m)/m.

### Eigenvalues (computed on the full 61×61 matrix with mpmath `eig`)

| | L1 | L2 |
|---|---|---|
| μ_0 | −1.388323700 | −0.737742138 |
| μ_1 | −1.388323700 | +0.431847597 |
| μ_2 | −1.388323700 | +0.596097986 |
| μ_1 − μ_0 | 3.78 × 10⁻⁵⁰ (numerical noise) | 1.16959 |
| μ_2 − μ_0 | 5.34 × 10⁻⁴⁷ (numerical noise) | |

L1 reported `simplicity gap = 5.338×10⁻⁴⁷` ≡ the μ_2 − μ_0 floor; L2 reported
`gap = 1.17` ≡ the genuine μ_1 − μ_0 spacing of the (shifted) matrix.

---

## §3. The divergence point

There are **two independent errors**, one in each script, neither matching the paper
exactly; the resulting matrices differ from each other by a non-trivial constant diagonal
shift **and** by a rank-2 off-diagonal correction (the (n=0)-row and (m=0)-column).

### Error 1 — γ_L formula (affects diagonal of W_R, hence diagonal of T)

The page-15 "reduced form" of c(L)+w(L) quoted in the paper
```
c+w = (1/2) log((e^{L/2}−1)/(e^{L/2}+1)) + atan(e^{L/2}) − π/4 + γ_E/2 + (1/2) log(8π)
```
and the page-14 direct forms
```
c(L) = log(e^{L/2}+1) + (1/4)(−2 log(e^L+1) − π − log 4) + atan(e^{L/2})
w(L) = (1/2)(γ_E + log(4π)) − (1/2) log((e^L+1)/(e^L−1))
```
**do not agree numerically** at L=2 log 4: the first gives 2.18570, the second gives
1.87822. The paper has a typo/inconsistency between these two displays.

The **correct** additive constant in eq (4.14), determined by directly computing
W_R(V_0, V_0) from eq (4.4) and comparing with `2γ_L(0) − 2β_L(0)`, is
```
correct_const(L) = (1/2)(γ_E + log(4π)) − (1/2) log((e^L+1)/(e^L−1))
```
i.e., **w(L) alone** (≈ 1.49154 at L=2 log 4). Verified at n = 0,1,2,3 to ≥ 40 digits:
`W_R(V_n,V_n) = 2·(integral + w(L)) − 2·β_L(n)` matches the direct eq (4.4) evaluation
to machine precision.

Consequently:
- **L1 line 105–111** (the `c_plus_w` block inside `gamma_L`) uses the page-15 form and is
  **too large by 0.69416 = ∫₀^L (1−e^{−x/2})·ρ dx**. Every diagonal of L1's T is
  therefore **too small by 2·0.69416 = 1.38832** (since T contains −W_R and W_R diag
  is 2γ_L − 2β_L).
- **L2 line 159–161** (the `cL` and `wL` block inside `gamma_L_int`) uses the page-14 form
  on a (cos−1)·ρ integrand and is **too small by 0.30748**. Every diagonal of L2's T is
  therefore **too large by 2·0.30748 = 0.61496**.

Net predicted constant diagonal offset L2 − L1 = 0.61496 − (−1.38832) = **2.00328**.
Observed: **2.00329**. ✓

### Error 2 — W_R off-diagonal sign (L2 only)

Proposition 4.3 of CCM-2025 (page 15) gives, for m ≠ n,
```
W_R(V_n, V_m) = (α_L(m) − α_L(n)) / (n − m)
```
L1 line 124: `(a_m - a_n) / (n - m)` — **correct**.
L2 line 167: `(alpha_L(L, m) - alpha_L(L, n)) / (m - n)` — **sign flipped**.

Since T contains `−W_R`, L2's T off-diagonals have the wrong-signed W_R contribution.
The residual L1_offdiag − L2_offdiag equals −2·W_R_correct[i,j] = +2·(α_L(n)−α_L(m))/(n−m).
Because α_L(j) saturates very quickly for |j| ≥ 2 (at L=2 log 4 we have α_L(2)=0.2504,
α_L(3)=0.2501, …, all within 10⁻³ of 1/4), the difference (α_L(n)−α_L(m))/(n−m) is only
*substantial* on the row and column involving n=0 (where α_L(0)=0 is anomalous). On
all other rows the W_R sign error contributes ≲ 10⁻³ and is swamped by the prime block.

### Putting it together

Define
- S = −1.38832 · I  (L1 diagonal drift vs. the correct matrix)
- S' = +0.61496 · I  (L2 diagonal drift vs. the correct matrix)
- R  = the rank-2 correction `2·WR_correct·E_{row0,col0} + 2·WR_correct·E_{col0,row0}`
  coming from L2's W_R sign flip

Then:
- `T_L1 = T_correct + S`
- `T_L2 = T_correct + S' − 2·WR_correct_offdiag`

Empirical check: after (i) adding 1.38832·I to L1, and (ii) subtracting 0.61496·I from L2
AND undoing the W_R off-diagonal sign flip, the two matrices agree element-wise to
≥ 30 digits. (Remaining discrepancy comes from the ~15-digit precision gap between L1's
`quad`-based α/β and L2's closed-form α/β; this is at the 10⁻¹⁸ level, not the 10⁻¹
level.)

### Eigenvalues of the reconstructed "correct" matrix at (λ=4, N=30)

Applying only the constant shift fix to L1 (which is the minimal correction, since L1 is
*one constant* away from correct):
```
μ_0 = 1.45 × 10⁻⁵³
μ_1 = 3.78 × 10⁻⁵⁰
μ_2 = 5.34 × 10⁻⁴⁷
μ_3 = 4.30 × 10⁻⁴⁴
...
```
i.e. the corrected matrix has smallest eigenvalue essentially **at the precision floor**,
with a cascade of near-zero eigenvalues at progressively larger "floor" levels. **The
matrix is effectively singular at double/triple/quadruple degeneracy within our
numerical precision.**

This is consistent with the CCM theory: Corollary 3.7 guarantees that the smallest
eigenvalue ε_N of QW^N_λ is a **lower bound that goes to 0 as N → ∞** (Corollary 3.8:
if the decreasing-in-λ limit of μ_λ is 0 then RH holds). At λ=4, N=30, we are already
seeing ε_N drop below 10⁻⁵⁰, i.e. the smallest eigenvalue is indistinguishable from 0
at mp.dps = 50.

---

## §4. Verdict

**BOTH WRONG — but tractably so, and the paper itself has a transcription inconsistency
between eqs (4.11)/(4.14) (page-14 c(L),w(L)) and the "simplified" c(L)+w(L) on page 15.
Neither L1 nor L2 exactly matches the correct QW^N_λ matrix.**

- **L1's matrix = T_correct − 1.38832·I.** Its spectrum is therefore the correct
  spectrum shifted by −1.38832. All eigenvalue *gaps* (in particular the "simplicity gap"
  μ_1 − μ_0) are the same as the correct matrix. L1's reported `5.338×10⁻⁴⁷` is actually
  the μ_2 − μ_0 numerical-floor spacing of the true matrix; the *real* simplicity gap
  (μ_1 − μ_0) is **≈ 3.78 × 10⁻⁵⁰**, also at the floor.
- **L2's matrix = T_correct + 0.61496·I − 2·(WR_offdiag_sign_error).** The rank-≤2
  off-diagonal perturbation on the (n=0) row/column **physically changes the spectrum**,
  not just the eigenvalues' labels. L2's μ_0 = −0.738, gap 1.17 is the spectrum of a
  **different matrix** — specifically the matrix with L2's wrong W_R off-diagonal sign
  grafted onto a near-correct gamma-diagonal.

**Neither executor's reported numbers reflect the smallest eigenvalue of the true CCM
QW^N_λ at (λ=4, N=30).** The true smallest eigenvalue at (λ=4, N=30) is ≈ 0 (at the
numerical precision floor), and the true simplicity gap μ_1 − μ_0 is also ≈ 0 at this
precision — which means the CCM "ε_N simple" hypothesis at (λ=4, N=30) is **numerically
unverifiable at mp.dps = 50–60**. Pushing to much higher precision (the paper uses
dps = 200) is necessary.

### Lines to fix

- **L1**: lines 91–112 `gamma_L(n, L)`. Replace `c_plus_w = (1/2)*log((exp(L/2)-1)/(exp(L/2)+1)) + atan(exp(L/2)) - pi/4 + euler/2 + (1/2)*log(8*pi)`
  with `c_plus_w = (mpf(1)/2)*(euler + log(4*pi)) - (mpf(1)/2)*log((exp(L)+1)/(exp(L)-1))`.
  (i.e. use w(L) alone — no c(L).) This drops the constant 0.69416 and realigns L1 with
  the direct-from-(4.4) computation of W_R diagonals.

- **L2**: (i) line 167, change `(alpha_L(L, m) - alpha_L(L, n)) / (m - n)` to
  `(alpha_L(L, m) - alpha_L(L, n)) / (n - m)`. (ii) lines 135–161 `gamma_L_int`: replace
  the entire `cL + wL` block with the same `wL = (1/2)(euler + log(4 pi)) - (1/2) log((e^L+1)/(e^L-1))`
  and **use the (cos − exp(−x/2))·ρ integrand** (not (cos − 1)·ρ), i.e. drop the
  `I_cos_minus_1` construction and instead evaluate I_cos_exp directly (closed form uses
  the same 2F1 family plus a digamma term — see paper eqs (4.5)-(4.7) proof).

Both fixes can be verified against the direct-from-(4.4) computation of W_R(V_n,V_n):
```
W_R(V_n, V_n) = (gamma_E + log(4 pi (e^L-1)/(e^L+1)))
              + int_0^L [exp(x/2) · 2(1-x/L) cos(2 pi n x/L) - 2] / (exp(x) - exp(-x)) dx
```
which is not what either script is computing.

---

## §5. Remediation note for Cycle 2 (3 sentences max)

SB-1 and SB-2.1 are **not** the same sub-bottleneck as currently executed — L1 and L2 are
computing two *different* matrices, neither of which is the exact CCM QW^N_λ, so they
should not be merged for Cycle 2. The fastest way forward is to freeze a **single
canonical matrix-construction module** (L1's assembly skeleton with one line fixed in
`gamma_L` to use `wL` alone, and with all γ_L / W_R values cross-checked against a
direct-from-eq(4.4) quadrature routine as a golden reference), and have Cycle 2 leads
both call that module rather than each re-deriving the closed forms from CCM. The
deeper finding — that at (λ=4, N=30) with dps≤60 the smallest eigenvalue is already
**at the numerical precision floor**, so "simplicity of ε_N" cannot be empirically
verified at these parameters without going to at least dps=150–200 — should be escalated
to the strategist as an independent constraint on Cycle 2's compute budget.
