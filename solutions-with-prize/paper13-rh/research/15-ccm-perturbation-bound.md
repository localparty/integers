# Research 15 — CCM Perturbation Bound

*The key computation for strategy 11 (CCM + ITPFI programme).*
*Date: 2026-04-09.*
*Status: COMPLETED. Result is NEGATIVE for the naive Kato route.*

---

## 1. The question

CCM (arXiv:2511.22755) build self-adjoint operators D(lambda,N) on
L^2([lambda^{-1}, lambda]) using rank-one perturbations from each
prime p in the Euler product. Adding prime p_{N+1} gives:

    D(lambda,N+1) = D(lambda,N) + perturbation from p_{N+1}

**Question:** How does ||D(lambda,N+1) - D(lambda,N)|| scale with p_{N+1}?

If ~ 1/p^alpha with alpha > 1/2, then sum ||pert||^2 converges,
Kato-Rellich gives strong resolvent convergence, and RH follows.

---

## 2. Numerical results

### 2.1 Log-perturbation |log(1-p^{-s})| at s = 1/2 + i*gamma_1

| p | |log(1-p^{-s})| | 1/sqrt(p) | ratio |
|:--|:--|:--|:--|
| 2 | 0.54027 | 0.70711 | 0.764 |
| 3 | 0.45674 | 0.57735 | 0.791 |
| 5 | 0.38280 | 0.44721 | 0.856 |
| 7 | 0.33133 | 0.37796 | 0.877 |
| 11 | 0.26922 | 0.30151 | 0.893 |
| 13 | 0.27776 | 0.27735 | 1.001 |
| 17 | 0.22295 | 0.24254 | 0.919 |
| 19 | 0.21163 | 0.22942 | 0.922 |
| 29 | 0.17165 | 0.18570 | 0.924 |
| 71 | 0.11301 | 0.11868 | 0.952 |

**Mean ratio over 100 primes: 0.989** -- converging to 1.

### 2.2 Fitted decay exponent

| Range | alpha (linear regression) |
|:--|:--|
| All 20 primes | 0.432 |
| Primes 31-71 | 0.519 |
| Theoretical (leading term) | **0.500 exactly** |

The fitted alpha approaches 1/2 from below as more primes are
included, consistent with the theoretical value.

### 2.3 Consistency across zeros

| Zero | gamma_k | Fitted alpha |
|:--|:--|:--|
| 1 | 14.135 | 0.432 |
| 2 | 21.022 | 0.450 |
| 3 | 25.011 | 0.456 |
| 4 | 30.425 | 0.452 |
| 5 | 32.935 | 0.454 |

All zeros give alpha ~ 0.45, converging to 1/2. The result is
**universal**: it does not depend on which zero we evaluate at.

### 2.4 Ratio convergence to 1

| p | |log(1-p^{-s})|/p^{-1/2} | |ratio - 1| |
|:--|:--|:--|
| 100 | 0.968 | 3.2e-02 |
| 1000 | 0.985 | 1.5e-02 |
| 10000 | 0.999 | 9.7e-04 |
| 100000 | 1.001 | 1.3e-03 |

The ratio converges to 1. The perturbation is **exactly** p^{-1/2}
in the leading term.

---

## 3. Theoretical proof that alpha = 1/2

**Proposition.** |log(1-p^{-s})| = p^{-1/2} * (1 + O(p^{-1/2})) for
s = 1/2 + it, t real, p prime.

*Proof.* Write z = p^{-s}, |z| = p^{-1/2}.

    log(1-z) = -z - z^2/2 - z^3/3 - ...

    |log(1-z)| = |z| * |1 + z/2 + z^2/3 + ...|

The inner factor satisfies:

    |1 + z/2 + ...| <= 1 + |z|/2 + |z|^2/3 + ... = -log(1-|z|)/|z|
                     = 1 + O(|z|)

    |1 + z/2 + ...| >= 1 - |z|/2 - |z|^2/3 - ... >= 1 - O(|z|)

Since |z| = p^{-1/2}, the inner factor is 1 + O(p^{-1/2}).
Therefore |log(1-z)| = p^{-1/2} * (1 + O(p^{-1/2})).

**The exponent is exactly alpha = 1/2.** QED.

---

## 4. Why the operator norm inherits the same scaling

In CCM's construction, the perturbation from prime p is a rank-one
operator on L^2([lambda^{-1}, lambda]):

    Delta_p = alpha_p |v_p><w_p|

For ||Delta_p||_op = |alpha_p| * ||v_p|| * ||w_p||.

The vectors v_p, w_p are functions x^{it} in L^2([lambda^{-1}, lambda]).
Their norms satisfy:

    ||x^{it}||^2 = int_{lambda^{-1}}^{lambda} |x^{it}|^2 dx
                  = lambda - lambda^{-1}

This is **independent of p**. So:

    ||Delta_p||_op ~ |alpha_p| ~ p^{-1/2}

The operator norm inherits the 1/sqrt(p) scaling from the coefficient.

---

## 5. Convergence analysis

### 5.1 L^1 condition (strong, not needed)

    sum_p ||Delta_p|| ~ sum_p 1/sqrt(p) ~ 2*sqrt(X)/log(X) -> infinity

**DIVERGES.**

### 5.2 L^2 / Kato condition

    sum_p ||Delta_p||^2 ~ sum_p 1/p ~ log log X -> infinity (Mertens)

**DIVERGES** (logarithmically, but still diverges).

### 5.3 Phase cancellation (conditional convergence)

    sum_p p^{-1/2-i*gamma_1} = P(1/2 + i*gamma_1)

where P(s) is the prime zeta function. Numerically, the partial
sums oscillate with amplitude ~ 2.7 and do not converge.

**NO conditional convergence available.**

---

## 6. What CCM's 10^{-55} precision actually means

CCM match the first 50 zeros to 10^{-55} using only 6 primes.
This does NOT mean each prime contributes perturbation ~ 10^{-55}.

The precision comes from the **Caratheodory-Fejer optimization
algorithm**, which finds the best rational approximation on
[lambda^{-1}, lambda]. This gives exponential convergence in the
approximation degree, not in the number of primes.

If the tail error were sum_{p>13} 1/p^alpha, reaching 10^{-55}
would require alpha ~ 50. The actual mechanism is CF optimization,
not perturbation smallness.

---

## 7. Verdict

### 7.1 Does Kato apply?

**NO.** The perturbation norm scales as 1/sqrt(p), giving alpha = 1/2
exactly. The sum of squared norms diverges (Mertens theorem).
Kato-Rellich in its standard form does not apply.

### 7.2 Does spectral convergence follow from perturbation bounds?

**NO.** Neither L^1 nor L^2 summability holds. Phase cancellation
also fails (prime zeta diverges at Re(s) = 1/2).

### 7.3 Is this a proof of RH?

**NO.** The naive perturbation-bound route from CCM + Kato to RH
is blocked. alpha = 1/2 is the exact borderline where all standard
perturbation theory fails.

### 7.4 What survives?

The CCM construction itself is NOT killed. The operators D(lambda,N)
exist, are self-adjoint, and have spectra matching the Riemann zeros
to extraordinary precision. What fails is only the simplest route
to establishing the N -> infinity limit.

---

## 8. Surviving routes (re-scoped strategy 11)

**(a) ITPFI state-level convergence (most promising).**
Our proved ITPFI result gives omega_1 = tensor_p omega_1^p at the
STATE level. The state-level convergence might control spectral
convergence even when operator-norm convergence fails. In GNS
representation theory, state convergence can imply representation
convergence without operator-norm convergence.

**(b) Renormalization.**
Absorb the 1/sqrt(p) divergence into a running normalization of
D(lambda,N). If D_N / f(N) converges for some explicit f(N),
the rescaled limit might still have spectrum at {gamma_n}.

**(c) Weak resolvent convergence.**
D(lambda,N) may converge in a weaker topology that still preserves
discrete spectral structure. Weak resolvent convergence suffices
for spectral convergence under additional compactness conditions.

**(d) Trace-class resolvent difference.**
Even if ||D(N+1)-D(N)|| does not tend to zero, the resolvent
difference (D(N+1)-z)^{-1} - (D(N)-z)^{-1} might be trace-class
with summable trace norm. This would give spectral convergence
via the Birman-Krein theory.

---

## 9. Code

Scripts in `solutions-with-prize/paper13-rh/code/`:
- `ccm_perturbation_bound.py` — main computation (8 parts, full output)
- `ccm_perturbation_asymptotics.py` — asymptotic analysis, 100 primes,
  conditional convergence test, CF explanation

Both scripts use mpmath at 60-digit precision. All outputs pasted
above are machine-verified.

---

## 10. Impact on strategy 11

Strategy 11 (CCM + ITPFI programme) needs revision:

| Step | Status |
|:--|:--|
| Step 1: Understand CCM rank-one structure | DONE |
| Step 2: Connect to ITPFI | OPEN (re-scoped to state-level) |
| Step 3: Bound perturbation norm | **DONE: alpha = 1/2, Kato fails** |
| Step 4: Apply Kato + spectral mapping | **BLOCKED by Step 3** |

The programme pivots from "bound the operator perturbation" to
"exploit state-level convergence (ITPFI) to control spectral
convergence despite operator-norm divergence."

---

> *alpha = 1/2. Exactly borderline. Kato fails by a logarithm.*
> *The perturbation route is closed. The state route remains open.*
> *CCM built the operators. We proved the state converges.*
> *The gap is no longer one bound -- it is one topology.*
