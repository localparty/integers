# Research 17: Numerical Evaluation of the Mellin Kernel K_{12}(log p)

*The dominant uncertainty in the SM one-loop estimate*
*|V_{12}|²_SM ≈ 0.12 (research/16, companion to research/07) is the*
*Mellin kernel K_{12}(log p) = Σ_k ψ̄_1(k) ψ_2(k) e^{i (log p)(log k)},*
*previously treated as O(1). This note computes K_{12}(log p) for*
*primes p = 2, 3, 5, 7, 11 in two truncated approximations to the*
*Bost–Connes scaling operator T_BC, reports the numerical values,*
*and updates the implied |V_{12}|²_SM with explicit uncertainty.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Sub-phase 3.A, thread 3b, follow-up to*
*`research/07-matter-content-Vnm-derivation.md` (C4) and*
*the open item "compute K_{12}(log p) numerically from a truncated*
*approximation to ψ_1, ψ_2".*

---

## 1. The Object

From `research/04-identity-12-rigorous.md` and equation (3.3) of
`research/07-matter-content-Vnm-derivation.md`, the Mellin kernel
that controls the matrix element of the prime isometry μ_p between
BC scaling-eigenstates |γ_1⟩ and |γ_2⟩ is

$$
K_{1m}(u)
\;:=\;
\sum_{k\geq 1}\,\overline{\psi_1(k)}\,\psi_m(k)\,e^{i u \log k},
\qquad
\langle\gamma_1|\mu_p|\gamma_m\rangle
\;=\;
\frac{1}{\sqrt p}\,K_{1m}(\log p),
\tag{1.1}
$$

where ψ_n(k) := ⟨k|_e · U |γ_n⟩ are the coefficients of the n-th
T_BC eigenvector in the e-circle natural-number basis
{|k⟩_e : k ∈ N*} (identified with {μ_k Ω_1} via the Identity 12
unitary U).

The matter perturbation V on H_R has off-diagonal matrix elements

$$
V_{1m}
\;=\;
\sum_p\,\frac{c_p}{\sqrt p}\,
\bigl[K_{1m}(\log p) + K_{m1}(\log p)\bigr]
\;+\;\cdots
\tag{1.2}
$$

(equation 5.1 of research/07). The previous agent
(`research/16-sm-one-loop-V12.md`) computed
|V_{12}|²_SM ≈ 0.12 using the **assumption** |K_{1m}(log p)| ∼ 1;
the empirical value from the CC formula is |V_{12}|²_emp ≈ 0.2425
(research/05 §4.1; research/07 §6).

**The task of this note.** Replace the assumption
|K_{12}(log p)| ∼ 1 by a concrete numerical estimate obtained from
a finite-dimensional approximation of T_BC, and report the
rescaled |V_{12}|²_SM with a honest uncertainty band.

---

## 2. The Problem: T_BC Is Not Tractable in Closed Form

T_BC is the Connes scaling operator on H_R (research/02 §3.2),
defined via the Mellin transform of the imaginary-time BC
correlator. Its spectrum **conditionally contains** {γ_n}
(research/02, R5+C1), but its eigenvectors have no closed form:
they are related to distributional spectral data of the
Riemann–Weil explicit formula.

To get concrete numbers, we must **truncate** T_BC to a
finite-dimensional self-adjoint operator T_N on an N-dimensional
subspace of H_1, diagonalize numerically, and read off approximate
eigenvectors. There is no canonical truncation; we explore two
natural choices below, keeping the physics honest about what each
captures.

---

## 3. Model A — Diagonal log-k (Sanity Toy Model)

### 3.1 Definition

The simplest concrete operator on {|k⟩_e : k = 1,...,N} with
spectrum related to the BC Hamiltonian is the diagonal operator

$$
T^{(A)}_N\,|k\rangle_e \;=\; \log(k)\,|k\rangle_e.
\tag{3.1}
$$

This is **not** T_BC — it is the BC Hamiltonian H_BC (research/02
eq. 2.3), whose spectrum is {log k : k ∈ N*}, not {γ_n}. But it
has exact diagonal eigenvectors ψ_n^{(A)}(k) = δ_{nk}, which makes
the kernel evaluation trivial and provides a sanity baseline.

### 3.2 Kernel

Identifying |γ_1⟩ → |1⟩_e and |γ_2⟩ → |2⟩_e (first two basis
vectors):

$$
K^{(A)}_{12}(u)
\;=\;
\sum_{k\geq 1}\,\delta_{1k}\,\delta_{2k}\,e^{i u \log k}
\;=\;
0.
\tag{3.2}
$$

Strictly zero for orthogonal basis states. The relevant physical
object is then ⟨γ_1|μ_p|γ_2⟩, which in this toy becomes

$$
\langle 1|_e\,\mu_p\,|2\rangle_e
\;=\;
\langle 1|_e\,|2p\rangle_e
\;=\;
\delta_{1,2p}
\;=\; 0,
\tag{3.3}
$$

unless one defines the isometry action symmetrically. Under the
alternate convention μ_p |k⟩_e = |pk⟩_e the matrix element is
δ_{2,p·1} = [p = 2], giving

$$
K^{(A)}_{12}(\log p)
\;=\;
\log p\;\;\text{if}\;\;p = 2,\;\;\text{else}\;\;0.
\tag{3.4}
$$

**Verdict.** Model A is too rigid: it supports only the single
prime p = 2 at O(log 2) = 0.69, and zero for all other primes.
This is **not** an order-1 kernel uniformly in p, and it already
invalidates the naive O(1) estimate. Model A is a sanity baseline
for the more realistic Model B.

---

## 4. Model B — Truncated Log-k Plus Prime-Hecke Off-Diagonals

### 4.1 Definition

Motivated by (2.1) of research/02 — μ_p acts as a dilation mixing
different μ_k Ω_1 basis elements — we promote the diagonal log-k
operator to a **banded self-adjoint** operator on {|k⟩_e : k = 1,...,N}:

$$
T^{(B)}_N
\;=\;
\sum_{k=1}^{N}\log(k)\,|k\rangle_e\langle k|_e
\;+\;
g\sum_{p\,\mathrm{prime},\,p\leq P}\frac{1}{\sqrt p}
\sum_{j,\,pj\leq N}
\bigl(|j\rangle_e\langle pj|_e + |pj\rangle_e\langle j|_e\bigr),
\tag{4.1}
$$

with coupling g = 1, prime cutoff P = 60. The diagonal is the BC
Hamiltonian; the off-diagonals are the Hermitized BC Hecke
generators μ_p + μ_p*, weighted by 1/√p to match the natural
normalization of (1.2). This is a **band matrix** whose spectrum
interpolates between pure {log k} and the full BC Hecke algebra.

**This is still not T_BC.** The true T_BC is the *Mellin-dual*
scaling generator (research/02 eq. 3.2), not H_BC itself. Its
spectrum is {γ_n}, which bears no simple relation to {log k} at
finite N. Model B captures the **Hecke mixing** structure of the
BC algebra on the natural-number basis but not the dual scaling
dynamics that produce {γ_n}. It is therefore an order-of-magnitude
proxy, not a rigorous truncation of T_BC.

### 4.2 Numerical Diagonalization

Code (NumPy + SymPy, ~30 lines):

```python
import numpy as np
from sympy import primerange
from mpmath import zetazero

def build(N, P=60, g=1.0):
    T = np.diag([np.log(k) for k in range(1, N+1)])
    for p in primerange(2, P+1):
        w = g / np.sqrt(p)
        for j in range(1, N+1):
            if p*j <= N:
                T[j-1, p*j-1] += w
                T[p*j-1, j-1] += w
    return T

gamma = [float(zetazero(n).imag) for n in (1, 2, 3)]

for N in (500, 2000, 5000):
    T = build(N)
    w, v = np.linalg.eigh(T)
    # Pick eigenvectors whose eigenvalues are closest to gamma_1, gamma_2
    i1 = int(np.argmin(np.abs(w - gamma[0])))
    order2 = np.argsort(np.abs(w - gamma[1]))
    i2 = int(order2[0] if order2[0] != i1 else order2[1])
    psi1, psi2 = v[:, i1], v[:, i2]
    ks = np.arange(1, N+1)
    for p in (2, 3, 5, 7, 11):
        phase = np.exp(1j * np.log(p) * np.log(ks))
        K12 = np.sum(np.conj(psi1) * psi2 * phase)
        print(f"N={N}, p={p}: K_12 = {K12.real:+.4f}{K12.imag:+.4f}i,"
              f"  |K_12| = {abs(K12):.4f}")
```

### 4.3 Results

> **Note 2026-04-09 (round 2 errata): truncated Hecke eigenvectors do not
> approximate true T_BC eigenvectors.**
> The eigenvalues of Model B nearest γ_1, γ_2 come out at ≈ 9.92 and ≈ 9.72
> (see "Caveat" immediately below), **not** the actual γ_1 ≈ 14.135 and
> γ_2 ≈ 21.022. This confirms that Model B's eigenvectors are eigenvectors
> of a different operator and are **not** approximations to ψ_1, ψ_2 of
> T_BC. The rigorous K_12 calculation using the Pauli–Villars regularisation
> choice is carried out in research/32-K12-rigorous-via-regularisation-choice.md
> (§3–§5), which gives |K_12| ∼ 0.15–0.22 — roughly an order of magnitude
> **larger** than Model B's ∼ 0.01 and assigning the remaining residual to
> c_p rather than to K_12. The Model B numbers in this section should
> therefore be read as a toy benchmark, not a rigorous estimate of K_12.
> See research/32 §3–§5 for the rigorous PV computation.


We pick eigenvectors of T^{(B)}_N whose eigenvalues are the closest
to γ_1 ≈ 14.135 and γ_2 ≈ 21.022 (there is no better canonical
identification, since T^{(B)}_N is not a truncation of T_BC).

**Caveat.** The eigenvalues of T^{(B)}_N nearest γ_1, γ_2 do not
actually equal γ_1, γ_2 — they fall in the bulk of the log-k
spectrum. For N = 5000 the nearest eigenvalues are ≈ 9.92 and ≈
9.72, reflecting that log N = log 5000 ≈ 8.5 + Hecke spreading. To
push eigenvalues as high as γ_2 ≈ 21 by the log-k construction
alone would require N ∼ e^{21} ≈ 10^9, which is beyond direct
diagonalization. This is the honest limitation of Model B.

| N | Re K_{12}(log 2) | Im K_{12}(log 2) | \|K_{12}(log 2)\| | \|K_{12}(log 3)\| | \|K_{12}(log 5)\| | \|K_{12}(log 7)\| | \|K_{12}(log 11)\| |
|:--|:------|:------|:-------|:-------|:-------|:-------|:-------|
| 500  | −0.006 | −0.032 | 0.032 | 0.034 | 0.023 | 0.014 | 0.008 |
| 2000 | −0.034 | +0.010 | 0.035 | 0.041 | 0.037 | 0.032 | 0.025 |
| 5000 | −0.004 | −0.009 | 0.010 | 0.017 | 0.020 | 0.021 | 0.020 |

The magnitudes are all in the range **0.01 – 0.04**, and they show
**no sign of converging to O(1)** as N increases — if anything,
|K_{12}(log 2)| decreases from 0.032 to 0.010. The eigenvectors
ψ_1^{(B)}, ψ_2^{(B)} of T^{(B)}_N are **delocalized** over ∼ N
basis states, and the oscillatory phase e^{i u log k} produces
substantial cancellation.

### 4.4 Interpretation

Two orders of magnitude below the naive O(1) estimate. This is the
key numerical finding of this note: **in the most natural
truncation available, K_{12}(log p) comes out of order 10^{−2},
not 10^{0}.**

The caveat is severe: Model B's eigenvectors are not really
approximations to ψ_1, ψ_2 of T_BC. They are eigenvectors of a
different operator that shares the Hecke mixing structure but not
the dual scaling dynamics. The true ψ_n are believed (from
Connes–Marcolli 2008, Chapter II) to be peaked on primes in a
certain sense, which Model B does not capture.

A reasonable band for the true |K_{12}(log p)| from this analysis
is therefore

$$
|K_{12}(\log p)|
\;\in\;
[\,0.01,\; 1\,]\qquad (p = 2, 3, 5),
\tag{4.2}
$$

spanning the Model B estimate (lower bound) to the naive O(1)
assumption (upper bound). The central estimate is the **geometric
mean** ≈ 0.1 – 0.3.

---

## 5. Numerical Values to Report

Taking Model B at N = 5000 as the honest lower-end estimate and
writing out K_{12} for the two primes that dominate the SM
perturbation (c_2, c_3 in research/07 eq. 4.10):

$$
\boxed{\;
K_{12}(\log 2)
\;\approx\;
-0.004 - 0.009\,i,
\qquad
|K_{12}(\log 2)|
\;\approx\;
0.01
\;}
\tag{5.1}
$$

$$
\boxed{\;
K_{12}(\log 3)
\;\approx\;
+0.009 + 0.014\,i,
\qquad
|K_{12}(\log 3)|
\;\approx\;
0.017
\;}
\tag{5.2}
$$

These are **Model B numerical values**, not rigorous T_BC matrix
elements. The true value could be larger by up to two orders of
magnitude if the true ψ_1, ψ_2 have substantial support on primes
(which Model B's delocalized eigenvectors wash out).

---

## 6. Rescaled |V_{12}|²_SM and Comparison to Empirical

From (1.2), the dominant primes contribute

$$
V_{12}^{(\mathrm{lead})}
\;\approx\;
\frac{c_2}{\sqrt 2}\bigl[K_{12}(\log 2) + K_{21}(\log 2)\bigr]
\;+\;
\frac{c_3}{\sqrt 3}\bigl[K_{12}(\log 3) + K_{21}(\log 3)\bigr].
\tag{6.1}
$$

Research/16 assumed |K_{1m}(log p)| ∼ 1, getting |V_{12}|² ≈ 0.12.
The scaling of |V_{12}|² with the kernel magnitude, for the
dominant p ∈ {2, 3}, is approximately

$$
|V_{12}|^{2}_{\mathrm{new}}
\;\approx\;
|V_{12}|^{2}_{\mathrm{old}}
\cdot
\bigl\langle|K_{12}(\log p)|^{2}\bigr\rangle_{p=2,3},
\tag{6.2}
$$

where the angle brackets denote a prime-weighted average.

### 6.1 Model B central estimate

With |K_{12}(log 2)| ≈ 0.010 and |K_{12}(log 3)| ≈ 0.017, the
average of |K|² is ≈ 2.0 × 10^{−4}, giving

$$
|V_{12}|^{2}_{\mathrm{SM,\,Model\,B}}
\;\approx\;
0.12 \times 2 \times 10^{-4}
\;=\;
2.4 \times 10^{-5}.
\tag{6.3}
$$

This is **four orders of magnitude below** the empirical 0.2425,
and should be taken as a *lower bound* rather than a central
estimate, because Model B's delocalized eigenvectors underestimate
|K_{12}|.

### 6.2 Honest band

Treating (4.2) as the true band and taking the geometric-mean
central value ⟨|K|²⟩ ≈ 10^{−2}:

| Kernel scenario | ⟨\|K_{12}\|²⟩ | \|V_{12}\|²_SM | ratio to 0.2425 |
|:---|:---|:---|:---|
| Naive (research/16) | 1 | 0.12 | 0.49 |
| Geometric mean (proposed central) | 10^{−2} | 1.2 × 10^{−3} | 5 × 10^{−3} |
| Model B (lower bound) | 2 × 10^{−4} | 2.4 × 10^{−5} | 10^{−4} |

**The honest conclusion.** The previous factor-of-2 match
(|V_{12}|²_SM = 0.12 vs empirical 0.2425) depended **critically**
on the |K_{12}| ∼ 1 assumption. The simplest concrete truncation
(Model B) drives |K_{12}| substantially below 1. Either:

(i) The true T_BC eigenvectors are much more peaked than Model B
suggests (which the structural argument of research/07 §5.4 and
Connes–Marcolli 2008 Ch. II supports), in which case the
|K_{12}| ∼ O(1) estimate is correct and the factor-of-2 agreement
is real; or

(ii) The true |K_{12}| is in the 0.1 – 0.3 range, in which case
|V_{12}|²_SM drops to ∼ 10^{−3} and the previous agreement with
0.2425 was accidental.

**The current numerical evidence does not distinguish between
these.** The open task is a genuine truncation of T_BC — not of
H_BC plus Hecke off-diagonals — which requires computing the
Riemann–Weil test-function spectral data directly
(Connes–Consani–Moscovici 2007, Connes 1999).

---

## 7. What Would Be Needed for a Rigorous Answer

To replace Model B with a genuine truncation of T_BC:

(T1) **Compute the BC correlator** ⟨Ω_1, σ_{i log u}(a) Ω_1⟩ for
a family of test elements a ∈ A_BC, as a function of u.

(T2) **Mellin-transform** the correlator numerically (e.g., via
FFT on a log-u grid) to obtain M(s) on the critical line s = 1/2 + iτ.

(T3) **Localize** M(s) near s = 1/2 + iγ_n using a windowed
Gaussian test function, and extract ψ_n(k) = ⟨k|_e · (window of
M at γ_n)⟩ as an integral transform.

(T4) **Evaluate K_{12}(log p)** on the resulting ψ_1, ψ_2 by the
finite sum (1.1).

Steps (T1)–(T4) are conceptually clean but technically
substantial. Each uses rigorous objects (the BC correlator, the
Mellin transform, Riemann–Weil test functions) and produces a
numerical answer with controlled approximation error. The full
execution is deferred but is the natural next step of research/07
(C4).

---

## 8. Status Summary

| Result | Status |
|:---|:---|
| Definition and setup of K_{12}(log p) from research/04, 07 | Recalled (Section 1) |
| Honest accounting of why T_BC is not directly tractable | Done (Section 2) |
| Model A (diagonal log-k): K_{12} ≡ 0 off the p=2 diagonal | Computed (Section 3) |
| Model B (log-k + Hecke off-diagonals): K_{12} numerical | Computed for N up to 5000 (Section 4) |
| Numerical values K_{12}(log 2), K_{12}(log 3) | Reported (Section 5), in Model B |
| Rescaled \|V_{12}\|²_SM | 2.4 × 10^{−5} (Model B) to 0.12 (naive), band 10^{−5} – 10^{−1} |
| Comparison to empirical 0.2425 | Model B 10^{4}× below; naive factor-of-2 match |
| Rigorous T_BC truncation (steps T1–T4) | Deferred |

**The dominant uncertainty in research/16's |V_{12}|²_SM = 0.12
estimate is the Mellin kernel, and this note has sharpened the
uncertainty rather than eliminated it.** The concrete takeaways:

1. The naive "K_{12} ∼ 1" assumption is not supported by any
   simple truncation; it is an upper bound, not a central estimate.
2. The simplest log-k-plus-Hecke truncation gives K_{12}(log 2,3)
   ≈ 10^{−2}, pushing |V_{12}|²_SM to 10^{−5}.
3. The true value is somewhere in between, and getting it will
   require steps (T1)–(T4) — rigorous BC correlator Mellin
   transform and Riemann–Weil test-function localization.
4. The previous factor-of-2 match between |V_{12}|²_SM ≈ 0.12 and
   empirical 0.2425 should be flagged as **assumption-dependent**,
   not a robust prediction, until the rigorous K_{12} is computed.

The CC formula's structural derivation (research/05) is unaffected:
the sign, the 1/γ_m form, the logarithmic correction, and the
convergence of the sum do not depend on the numerical value of
K_{12}. Only the **size** of |V_{12}|²_SM — and hence the exact
numerical −0.15 coefficient — depends on this kernel.

---

## 9. Definition of Done

This note closes when:

- [x] The Mellin kernel K_{12}(log p) is computed numerically in a
      concrete truncation (Model B).
- [x] Both the naive O(1) assumption and the Model B result are
      reported with explicit uncertainty bands.
- [x] The rescaled |V_{12}|²_SM is given, with an honest comparison
      to empirical 0.2425.
- [x] The path to a rigorous T_BC truncation (T1)–(T4) is
      documented as the next open task.
- [ ] A ledger entry updates the status of research/07 (C4) and
      research/16's uncertainty.
- [ ] A follow-up research note executes (T1)–(T4) for at least
      one test function, and reports whether |K_{12}| lands in
      [0.01, 0.1], [0.1, 1], or [1, 10].

Items 1–4 are done. Items 5–6 are the next actions.

---

## 10. References

### 10.1 In this directory

- `02-quantize-R-construction.md` — the operator R̂, T_BC, and the
  Riemann subspace H_R (Phase 2)
- `04-identity-12-rigorous.md` — the unitary U: H_e → H_1^{(N*)}
  on the natural-number basis
- `05-derive-cc-formula.md` — the Rayleigh–Schrödinger derivation
  of the CC formula and the identification of V_{1m}
- `07-matter-content-Vnm-derivation.md` — equation (3.3)
  defining K_{1m}, equation (5.1) relating V_{1m} to K_{1m},
  open item §9 "compute K_{12}(log p) numerically"
- `16-sm-one-loop-V12.md` — the previous agent's |V_{12}|²_SM ≈
  0.12 estimate assuming |K_{12}| ∼ 1

### 10.2 External

- Bost, J.-B., and Connes, A., *Selecta Math.* **1** (1995) 411.
- Connes, A., *Selecta Math.* **5** (1999) 29 — the explicit
  formula in operator-algebraic form; the construction of T_BC as
  a Mellin-dual scaling operator.
- Connes, A., Consani, C., and Marcolli, M., *Adv. Math.* **214**
  (2007) 761 — the endomotive picture and the matter-content
  perturbation.
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS Colloquium Publications **55** (2008),
  Chapter II §3 — the explicit formula and the test functions
  whose Mellin transforms are the ψ_n.

---

*Two truncations, one honest conclusion: the naive K_{12} ∼ 1*
*assumption is an unverified upper bound, the simplest concrete*
*truncation pushes K_{12} two orders of magnitude below that, and*
*the true value lies somewhere in between. Until a genuine T_BC*
*truncation (T1–T4) is executed, the factor-of-2 match between*
*|V_{12}|²_SM = 0.12 and empirical 0.2425 should be flagged as*
*assumption-dependent rather than robust.*
