# Research 31 -- Gap B: Quantitative Slepian Convergence

*Date: 2026-04-09*
*Status: GAP B INVESTIGATED AND CLOSED (NEGATIVELY). Direct Slepian transfer via operator-norm bounds fails by 35 orders of magnitude. The route is dead. Gap A (arithmetic exclusion) is now the sole viable path.*

---

## 1. The problem

**Goal.** Show ||QW_lambda^{N,+} - PW_lambda^+||_op < delta/2 where delta = mu_2(PW) - mu_1(PW) is the prolate spectral gap. If this holds for N >= N_0, simplicity transfers from PW to QW by Kato IV.3.5.

**The Weil quadratic form** QW = W_{0,2} - W_R - Sum_{p <= lambda^2} W_p decomposes into:
- Archimedean part (W_{0,2}, W_R): digamma/log-gamma integrals, prolate-like in the limit
- Prime part (W_p): Sum_{p <= P_N} (log p / p^{1/2}) cos(gamma log p) terms

**The difference** ||QW^N - PW|| is controlled by the prime sum. By PNT, Sum_{p>P} log(p)/sqrt(p) DIVERGES. So ||QW - PW|| grows with the number of primes -- it does not converge.

**The CCM precision clue.** CCM match gamma_1 to 10^{-55} with only 6 primes (P_6=13). But this precision is in EIGENVALUE RATIOS, not operator norms. The Weil formula is exact as an identity; the convergence is in a relative sense, not absolute.

---

## 2. Computational results (slepian_convergence_test.py)

Ran at lambda = sqrt(13), grid size 60, 50-digit precision, N_primes in {1,2,3,...,20}.

### 2.1 Direct norm transfer: FAILS

||QW - PW||_op GROWS from 0.083 (1 prime) to 0.636 (20 primes). Meanwhile gap(PW)/2 ~ 2.3 x 10^{-36}. The Kato bound fails by 35 orders of magnitude. No N_0 exists.

### 2.2 Archimedean operator != prolate operator

The archimedean part has eigenvalues O(0.01-0.25), vs prolate eigenvalues in (0,1). The digamma kernel differs structurally from the sinc kernel at finite L. Confirms Research 25, Section 3.4.

### 2.3 Gap positivity: universal

The gap mu_2 - mu_1 of QW is POSITIVE for every tested prime count:

    N_p=1: gap=0.151   N_p=6: gap=0.022 (minimum)   N_p=20: gap=0.266

Non-monotonic: gap decreases to a minimum at P=13=lambda^2 (the CCM cutoff), then increases for P > lambda^2.

### 2.4 Eigenvalue ratio: no convergence to PW

mu_2/mu_1 for QW oscillates in [0.38, 0.91], while PW ratio is 2252. Completely different spectral structures. No ratio-based transfer either.

### 2.5 Key finding: gap minimum at the natural cutoff

The gap is smallest at N_p=6 (P=13=lambda^2) -- precisely the CCM construction point. The simplicity question is hardest at the physically relevant prime cutoff, not at the limits.

---

## 3. Why the approach fails

Three independent reasons:

**(a) Scale mismatch.** QW eigenvalues are O(exp(-4*pi*lambda^2)); PW eigenvalues are O(1). No normalization fixes this for operator-norm bounds.

**(b) Prime sum divergence.** Sum log(p)/sqrt(p) diverges. Adding primes increases ||QW - PW||, not decreases it.

**(c) Prolate gap is irrelevant.** The prolate gap (between eigenvalues in (0,1)) has no relationship to the Weil gap (between exponentially small eigenvalues). They describe different spectral regimes.

---

## 4. What remains viable

**(a) Eigenvector-based transfer.** QW eigenvectors may converge to PW eigenvectors (CCM Lemma 7.2) even without norm convergence. But eigenvector convergence alone does not give simplicity.

**(b) The exact CCM construction.** Our grid-based QW is approximate. The Fourier-basis construction (r49_fourier_circle.py) uses the EXACT Weil identity, which may have better properties.

**(c) Gap positivity from arithmetic structure.** The universal gap > 0 suggests simplicity might follow from QW's arithmetic structure alone, without reference to PW.

---

## 5. Revised feasibility

| Component | Rating | Notes |
|:----------|:-------|:------|
| Direct norm transfer QW -> PW | 0/10 | DEAD: 35-order-of-magnitude mismatch |
| Eigenvector-based transfer | 3/10 | Requires new machinery |
| Gap positivity from arithmetic | 5/10 | Most promising; connects to Gap A |
| Numerical verification (finite N) | 9/10 | Done to 120 digits for N <= 40 |
| **Overall Gap B via Slepian** | **2/10** | Downgraded from 5/10 |

---

## 6. Implications

**Gap B is closed (negatively).** The Slepian transfer mechanism cannot bridge the scale mismatch between QW and PW. No value of N_0 exists where operator-norm perturbation theory applies.

**Gap A is the sole remaining route.** The arithmetic exclusion argument (<phi_k|a> != 0 for all k) from Research 26/29 now carries the full burden. This is a transcendence-type question about prime logarithms vs pi.

**The gap minimum at P = lambda^2 is new and unexplained.** It suggests the even-sector simplicity question is most delicate at the CCM cutoff. This observation should inform the Gap A attack.

**For N < N_0 (all finite N): numerical verification at 120 digits (already done for N <= 40) plus VNW propagation in lambda covers the finite cases modulo the "non-generic vs impossible" upgrade (Gap A).**

---

> *The Slepian bridge is too short. The banks are in different oceans.*
> *But the gap is always positive -- in every test, at every prime count.*
> *The answer may lie not in the limit, but in the arithmetic itself.*
