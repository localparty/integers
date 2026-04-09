# Research 161: Standard Invariant of N ⊂ M of Index 3 — Lepton Masses as Principal-Graph Eigenvalues

*Cycle 4. Authors: G Six, with Claude Opus 4.6. Date: 2026-04-09.*
*Builds on: research/47 (γ-template), research/140 (Jones index 3 ⇒ Q=2/3
structurally), research/151 (direct Frobenius-orbit periods fail on Koide
by 23.7%), research/157 (mixed scheme fails), research/158 (Frobenius Z/3Z
= Jones Z/3Z bridge theorem, ~60%).*

---

## 1. Goal

Execute research/157 §5.1's recommendation: derive m_τ and m_μ **directly**
from the standard invariant of the index-3 subfactor N ⊂ M (not from
γ-zero products, not from orbit relabellings), and ask whether the 0.08 %
Koide residual of research/47 closes.

## 2. The standard invariant of index 3

By Jones' restriction, admissible finite indices below 4 are
4cos²(π/n). The value 3 is reached at **n = 6**, so the Temperley–Lieb
algebra is TL_6(δ) with δ = √3, and the principal graph of the
hyperfinite type-A index-3 subfactor is **A_5** (5 vertices in a line),
not A_4 (A_4 would give index φ² ≈ 2.618 at n = 5). We compute both for
completeness.

### 2.1 A_5 adjacency eigenvalues (index 3)

Eigenvalues of the 5×5 tridiagonal adjacency matrix:

    {−√3, −1, 0, +1, +√3}.

Perron–Frobenius eigenvalue = √3 = δ, as required by Jones.
The normalised PF eigenvector (quantum dimensions) is

    (sin(kπ/6))_{k=1..5} ∝ (1/2, √3/2, 1, √3/2, 1/2).

The three *distinct* non-negative entries are

    q = {1, √3/2, 1/2}  =  {1.0000, 0.8660, 0.5000}.

### 2.2 A_4 adjacency eigenvalues (index φ², for control)

Eigenvalues {±φ, ±(φ−1)}; only two distinct magnitudes {φ, φ−1}, so
A_4 cannot support a 3-generation ansatz.

## 3. Candidate ansätze and Koide test

### 3.1 Eigenvalues as √m (magnitude spectrum of adjacency)

Distinct non-negative eigenvalues of A_5: {√3, 1, 0}. The zero
eigenvalue forces m_e → 0, so Koide

    Q = (3 + 1 + 0)/(√3 + 1 + 0)² = 4/(√3+1)² = 0.5359

— residual vs 2/3: **−19.6 %**. Moreover m_e ≡ 0 is phenomenologically
excluded. **Fails.**

### 3.2 Quantum dimensions as √m (PF eigenvector)

Take (√m_τ, √m_μ, √m_e) ∝ (1, √3/2, 1/2). Then

    Σ m_i   = 1 + 3/4 + 1/4 = 2,
    (Σ √m)² = (1 + √3/2 + 1/2)² = 5.598,
    Q       = 2/5.598 = **0.3573**,

— residual vs 2/3: **−46.4 %**. Normalising to m_e = 0.511 MeV gives
m_τ = 2.044 MeV, m_μ = 1.533 MeV — wrong by **three orders of
magnitude**. **Fails.**

### 3.3 Squared eigenvalues as m

(√3)², 1², 0² = 3, 1, 0 reproduces §3.1. **Fails.**

### 3.4 Why every A_5 ansatz fails

The spectrum of A_5 spans only √3 ≈ 1.73 (ratio max/min among
non-zero eigenvalues = √3, squared = 3). The lepton hierarchy requires
m_τ/m_e ≈ 3477, i.e. a √m spread of ~59. The principal graph of an
index-3 subfactor is *combinatorially too small* to host this spread —
the same structural failure that killed research/151's Gaussian periods
(spread ≈ 19 there; even smaller here).

## 4. Koide ratio summary

| Scheme                              | Q       | residual |
|:------------------------------------|:-------:|:--------:|
| γ-template (research/47 §6.4)       | 0.66613 | **0.08 %** |
| A_5 eigenvalues as √m (§3.1)        | 0.5359  | −19.6 %  |
| A_5 q-dims as √m (§3.2)             | 0.3573  | −46.4 %  |
| Frobenius periods (research/151)    | 0.5088  | −23.7 %  |

Every standard-invariant ansatz is **orders of magnitude worse** than
the γ-template floor of 0.08 %. The 0.08 % residual does **not** close.

## 5. Verdict

- **Filename**: `paper12/research/161-subfactor-standard-invariant-koide.md`
- **A_5 eigenvalues**: {−√3, −1, 0, 1, √3}; PF = √3 = δ. Quantum
  dimensions (1/2, √3/2, 1, √3/2, 1/2).
- **Best Koide Q achievable from the standard invariant alone**:
  0.5359 (eigenvalue ansatz), residual −19.6 %.
- **Residual closure**: **No.** The 0.08 % residual of research/47
  does not shrink — it blows up by ~250×.
- **Structural diagnosis**: research/140's identity Q = 2/[M:N] = 2/3
  is a statement about the Fuglede–Kadison determinant of E_N (global
  trace invariant), *not* about individual eigenvalues on the A_5
  principal graph. The standard invariant fixes Koide **as an identity
  on the whole trace**, but the individual charged-lepton masses are
  **not** eigenvalues on A_5: the combinatorial spread of A_5 is too
  small by a factor of ~60 in √m.
- **Converging conclusion with research/151 and research/157**: the
  0.08 % residual lives in the γ-zero formulas γ_7·γ_8 and
  γ_7·γ_8^{1/4} themselves (a statement about Riemann zeros meeting
  PDG m_τ, m_μ), not in the Z/3Z / subfactor layer. Three independent
  routes (direct orbit periods, mixed Fourier/power progression,
  standard-invariant eigenvalues) now fail, all for the same reason:
  insufficient multiplicative spread in the combinatorial data.
- **Recommended next step**: abandon "m_i = eigenvalue" ansätze.
  The only remaining subfactor-theoretic handle that could close
  0.08 % is a **matrix element** of T_BC on the level-13 CM tower
  restricted to N — i.e. a Connes–Marcolli-type L-function value
  rather than a graph eigenvalue. This is orthogonal to the present
  programme and is left as an open task for a separate cycle.

## 6. References

- research/47 §6.4 — γ-template Koide, 0.08 %
- research/140 — [M:N] = 3 fixes Q = 2/3 structurally
- research/151 — direct Frobenius orbit periods, 23.7 %
- research/157 — mixed Koide scheme, closed
- research/158 — bridge theorem, Frobenius Z/3Z = Jones Z/3Z
- Jones, *Invent. Math.* **72** (1983) 1 — index restriction
- Goodman–de la Harpe–Jones, *Coxeter Graphs and Towers of Algebras*,
  MSRI **14** (1989), §4.7 — principal graph A_n and TL(δ)
- Popa, *Acta Math.* **172** (1994) 163 — classification of
  hyperfinite subfactors of index ≤ 3

---

*The standard invariant of N ⊂ M at index 3 is A_5 with PF eigenvalue
√3 and quantum dimensions (1/2, √3/2, 1, √3/2, 1/2). Neither the
adjacency eigenvalues nor the quantum dimensions reproduce (m_e, m_μ,
m_τ): the Koide ratio is at best 0.5359 (−19.6 %), far worse than the
γ-template floor of 0.08 %. The 0.08 % residual does not close via the
subfactor's standard invariant; it is a statement about γ_7·γ_8 meeting
PDG, not about principal-graph combinatorics.*
