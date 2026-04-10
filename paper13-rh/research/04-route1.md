# research/04-route1 -- RAGE Theorem Analysis

*Date: 2026-04-10. Spectral Realisation Cycle 4, Route 1.*

## 1. The approach

The RAGE theorem (Ruelle-Amrein-Georgescu-Enss) provides a dynamical
criterion for spectral type. For a self-adjoint operator A on a
Hilbert space H:

- psi in H_{pp}(A) (pure point subspace) iff for every compact K:
  lim_{T->inf} (1/T) int_0^T |<e^{itA}psi, K e^{itA}psi>| dt > 0
- psi in H_c(A) (continuous subspace) iff this limit = 0.

Plan: apply RAGE to T_BC on H_R to distinguish pure point from
continuous spectrum.

## 2. The two natural implementations

### 2a. RAGE on H_R with T_BC dynamics

If T_BC|_{H_R} has eigenvalues {gamma_n}, then:
- exp(itT_BC)|gamma_n> = exp(i*gamma_n*t)|gamma_n>
- Return probability for |gamma_1>: |<gamma_1|e^{itT}|gamma_1>|^2 = 1

The RAGE integral = 1 > 0, confirming pure point.

**CIRCULARITY:** To compute exp(itT_BC) we need the spectral
decomposition of T_BC, which requires knowing the eigenvalues.
RAGE can confirm pure point if we already know the spectrum,
but cannot discover it.

### 2b. RAGE on H_1 with modular dynamics

The modular automorphism is explicitly known:
  sigma_t(mu_n) = n^{it} mu_n

Return probability for mu_2*Omega_1:
  |<sigma_t(mu_2)Omega, mu_2 Omega>|^2 / |<mu_2 Omega, mu_2 Omega>|^2
  = |2^{it}|^2 = 1 for ALL t.

**IRRELEVANCE:** This tells us about the modular Hamiltonian H_mod
(eigenvalues {log n}), not about T_BC. The modular dynamics are
a DIFFERENT operator from the Connes-Bost operator.

## 3. Numerical results

Return probability |2^{it}|^2 at specific times:

| t | 2^{it} | |2^{it}|^2 |
|:--|:-------|:-----------|
| 1 | 0.7692 + 0.6390i | 1.0 |
| 10 | 0.7971 + 0.6038i | 1.0 |
| 100 | 0.9801 + 0.1984i | 1.0 |
| 1000 | -0.4132 + 0.9106i | 1.0 |

RAGE integral (1/T) int_0^T |<...|K|...>| dt = 0.25 (constant)
for all T = 1, 10, 100, 1000.

No decay. Pure point for H_mod. Trivial and expected.

## 4. Adversarial analysis

The sharpest attack on Route 1:

**RAGE on H_1 tells us about H_1's spectrum. Does it constrain H_R?**

NO. H_1 and H_R are different Hilbert spaces:
- H_1 = GNS space of KMS_1 state (type III_1 factor)
- H_R = ground-state space of KMS_inf (type I, discrete)

The modular Hamiltonian has continuous spectrum on H_1 (Connes
spectrum S(M) = R_+ forces essential spectrum = R). The T_BC
operator on H_R 'should' have discrete spectrum {gamma_n}, but
this is the very claim to be proved.

There is no projection from H_1 spectral data to H_R 
spectral data that avoids knowing the answer first.

## 5. Premise check

Does RAGE distinguish spec = {gamma_n} from spec = {gamma_n} + {extra}?

On H_R: YES, if we could compute exp(itT_BC) independently.
But we cannot -- computing the dynamics IS solving the spectral problem.

On H_1: NO. The modular dynamics know nothing about T_BC.

## 6. Verdict

RAGE is BLOCKED by circularity. The only dynamics we can compute
explicitly (modular sigma_t) are for the wrong operator. The
dynamics we need (T_BC on H_R) require the spectrum we are trying
to determine.

**Feasibility: 1/10 (DOWN from 4/10).**

The downgrade reflects a structural impossibility: RAGE requires
computable dynamics, and the only computable dynamics on the BC
system are the modular ones, which are irrelevant to T_BC.

---

> *RAGE can confirm spectra but cannot discover them.*
> *The modular dynamics are the wrong operator.*
> *Route 1 is dead.*
