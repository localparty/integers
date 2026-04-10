# Research 59 -- Cycle 7: Can PSWF Theory Close CCM's Missing Step 2? (Adversarial)

*Date: 2026-04-09. Cycle 7 of 10. Role: FOCUSED ANALYSIS + ADVERSARIAL.*
*Depends on: ledger, research/37, research/43, research/58. Source: arXiv:2511.22755, Section 7.*

---

## 1. CCM's Missing Step 2 (precise statement)

CCM need (Section 8, p.32; Lemma 7.2): for n = 0, 4,

    max_{x in [-lambda, lambda]} |h_{n,lambda}(x) - h_n(x)| <= c * lambda^{-2}

where h_{n,lambda} are eigenfunctions of the prolate spheroidal differential operator
PW_lambda (CCM eq 7.5) and h_n are Hermite functions. This feeds into k_lambda = E(h_lambda),
the prolate approximation to the eigenvector xi_lambda. Missing Step 2 is: k_lambda
approximates xi_lambda well enough for Hurwitz to deliver eigenvalue convergence.

CCM prove Lemma 7.2 for n = 0, 4 specifically using Meixner-Schafke (1954) Satz 9.
The bound is ALREADY PROVED by CCM. What remains open is connecting k_lambda to xi_lambda.

---

## 2. PSWF approximation theory (review)

PSWFs {psi_{n,c}} are eigenfunctions of the integral operator (P_Omega P_T P_Omega) with
sinc kernel restricted to [-1,1], bandwidth parameter c. Key results:

- **Slepian (1961-1978):** All eigenvalues chi_n(c) are simple. For n < 2c/pi (the
  "Shannon number"), chi_n ~ 1. For n >> 2c/pi, chi_n decays super-exponentially.
- **Landau-Widom (1980):** The eigenvalue transition occurs in a window of width
  O(log c) around n = 2c/pi. Inside the window: chi_n ~ 1/(1 + e^{pi*alpha_n})
  where alpha_n encodes the distance from the transition.
- **Bonami-Karoui (2021):** For bandlimited functions f with bandwidth Omega on [-T,T]:
  the N-term PSWF expansion error ||f - sum_{n<N} <f, psi_n> psi_n||_inf decays
  super-exponentially once N exceeds the Shannon number 2c/pi = 2*T*Omega/pi. The
  rate is O(e^{-c'*N}) for explicit c' > 0.

The essential point: PSWFs are OPTIMAL for approximating bandlimited functions on
finite intervals, and the convergence is exponential, not polynomial.

---

## 3. Is h bandlimited?

The target function h(x) = (pi/2)(2*pi*x^2 - 3) * e^{-pi*x^2} is a Schwartz-class
function (Hermite polynomial times Gaussian). Its Fourier transform:

    hat{h}(xi) = analytic, decays as e^{-pi*xi^2/4} (Gaussian decay)

h is NOT strictly bandlimited (hat{h} is never exactly zero). However, h is
"essentially bandlimited": for any bandwidth Omega, the energy outside [-Omega, Omega] is

    ||h - P_Omega h||^2 = integral_{|xi|>Omega} |hat{h}(xi)|^2 dxi <= C * e^{-pi*Omega^2/4}

This is MUCH faster than polynomial decay. The PSWF expansion of an essentially
bandlimited function on [-T, T] has error controlled by both the truncation order N
and the energy leakage outside bandwidth Omega.

---

## 4. PSWF expansion error estimate

For the PSWF expansion of h on [-lambda, lambda] with bandwidth parameter
c = 2*pi*lambda^2 (CCM's parametrization, eq 7.9):

- Shannon number: N_S = 2c/pi = 4*lambda^2. This means ~4*lambda^2 PSWF terms capture
  essentially all the energy of any bandlimited function on [-lambda, lambda].
- For h (Schwartz class): the N-term PSWF expansion error is bounded by

      ||h - h_N||_{L^inf[-lambda,lambda]} <= C_1 * e^{-c_1 * N}  (for N > N_S)
                                             + C_2 * e^{-c_2 * lambda^2}  (leakage)

- CCM use only n = 0 and n = 4 (TWO terms), not N_S ~ 4*lambda^2 terms. The
  O(lambda^{-2}) rate in Lemma 7.2 comes from the Meixner-Schafke asymptotic expansion
  of individual PSWFs, not from the N-term expansion convergence.

**The PSWF expansion theory (Bonami-Karoui) is about using MANY terms and getting
exponential convergence. CCM's Lemma 7.2 is about using TWO specific terms and getting
polynomial convergence from the asymptotic expansion of EACH term. These are different
mechanisms.**

---

## 5. Does PSWF theory give lambda^{-2}?

Yes, but via a DIFFERENT route than needed. The Meixner-Schafke result gives: each
individual PSWF h_{n,lambda}(x) converges to h_n(x) at rate O(lambda^{-2}) uniformly
on [-lambda, lambda]. This is already what CCM proved in Lemma 7.2.

The PSWF expansion theory would give: if h is expanded in N >> 4*lambda^2 PSWFs on
[-lambda, lambda], the error is O(e^{-c*lambda}). This is exponentially better than
lambda^{-2}, but it uses ALL PSWFs, not just the two that CCM need.

The question is not "can we approximate h by PSWFs" (yes, trivially) but "does the
specific 2-term combination h_lambda = a*h_{0,lambda} + b*h_{4,lambda} converge to
h = a*h_0 + b*h_4 uniformly?" This follows from Lemma 7.2 applied to each term.
**CCM already proved this.** There is nothing to add.

---

## 6. What is ACTUALLY missing?

Re-reading Research/37 and Research/58 carefully: CCM's Lemma 7.2 IS proved. The
O(lambda^{-2}) bound on |h_lambda - h| IS established. What is missing is:

**The bridge from h_lambda to xi_lambda.** The prolate approximation k_lambda = E(h_lambda)
is NOT the eigenvector xi_lambda of QW_lambda. Missing Step 2 asks: is k_lambda close to
(a scalar multiple of) xi_lambda? This is an eigenvector approximation question, not a
function approximation question. PSWF theory does not address it.

Research/37 closes this bridge conditionally (on AE simplicity = Missing Step 1) via the
ITPFI triangle inequality: xi_lambda ~ xi_0 ~ k_lambda at rate O(1/lambda).

---

## 7. Adversarial

### A. "h is bandlimited so PSWFs give exponential convergence" -- IRRELEVANT

The proposal conflates two different approximation problems:

1. **Approximating h by PSWFs on [-lambda, lambda]:** This is trivial for Schwartz h.
   The N-term PSWF expansion converges super-exponentially. But CCM do not need this.
   They need the INDIVIDUAL PSWF h_{n,lambda} to converge to h_n, which is a statement
   about the asymptotic expansion of a single eigenfunction, not about series truncation.

2. **Approximating xi_lambda by k_lambda:** This requires operator-level information
   (eigenvalue gaps, perturbation theory), not function approximation theory. PSWF
   convergence rates, however good, say nothing about whether k_lambda is close to the
   actual eigenvector of QW_lambda.

### B. Does CCM's h_lambda come from PSWFs directly?

YES. h_lambda = a*h_{0,lambda} + b*h_{4,lambda} where h_{n,lambda} ARE prolate spheroidal
eigenfunctions (of PW_lambda, CCM eq 7.5). The coefficients a, b are chosen so that
h_lambda has vanishing integral. But the convergence h_lambda -> h is about the
ASYMPTOTIC BEHAVIOR of individual PSWFs as the bandwidth parameter gamma -> infinity,
not about expanding a fixed function in a PSWF basis.

### C. Is the uniform convergence on [-lambda, lambda] standard?

YES, for fixed mode number n. The Meixner-Schafke estimate (Satz 9) gives uniform
convergence of psi_n(x; gamma) to Hermite functions as gamma -> infinity. The bound is
O(gamma^{-1}) = O(lambda^{-2}) uniformly on [-1, 1] (hence on [-lambda, lambda] after
rescaling). This is CLASSICAL (1954) and CCM correctly invoke it.

The subtlety: the convergence is for FIXED n as lambda -> infinity. For n growing with
lambda, the estimates degrade. CCM only need n = 0 and n = 4, so this is not an issue.

### D. What about Missing Step 1?

Missing Step 1 (AE simplicity: the smallest eigenvalue of QW_lambda is simple with even
eigenvector) is INDEPENDENT of PSWF approximation theory. It is a spectral property of
the Weil quadratic form, not of the prolate operator. PSWF theory provides simplicity of
PW_lambda (Slepian 1961, via Sturm-Liouville), but the transfer QW_lambda -> PW_lambda
was killed in Research/31 (K19: norm mismatch by 10^35).

---

## 8. Feasibility

| Question | Answer |
|:---------|:-------|
| Does PSWF theory close Lemma 7.2? | Lemma 7.2 is already proved by CCM. Nothing to close. |
| Does PSWF theory close Missing Step 2? | NO. Step 2 = k_lambda ~ xi_lambda, which is eigenvector approximation, not function approximation. |
| Does PSWF theory help Missing Step 1? | NO. Slepian simplicity lives on PW, not QW. Transfer is killed (K19). |
| Is the exponential-vs-polynomial observation useful? | MARGINALLY. It confirms that the O(lambda^{-2}) bound in Lemma 7.2 has enormous room -- but room in a proved lemma is not progress on an unproved step. |

**Confidence that PSWF theory advances the programme: 1/10.**

The proposal is based on a correct observation (PSWF convergence is much faster than
needed) applied to the wrong problem (function approximation rather than eigenvector
approximation). Lemma 7.2 is already proved; the bottleneck is elsewhere.

**The actual bottleneck remains:** Missing Step 1 (AE simplicity) and the bridge
xi_lambda ~ k_lambda (which Research/37 closes conditionally on Missing Step 1). The
programme's wall is at AE simplicity and the spectral convergence of CCM's operators,
neither of which involves PSWF approximation rates.
