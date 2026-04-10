# Research 17 — α = 1/2 and the CF Mechanism

*The perturbation exponent is exactly 1/2. Kato fails. But CCM's*
*precision comes from Carathéodory-Fejér, not perturbation decay.*
*The convergence mechanism is rational approximation, not norm bounds.*

*Date: 2026-04-10*

---

## 1. The result

α = 1/2 exactly. ‖D(N+1) − D(N)‖ ~ 1/√p_{N+1}.

Kato requires α > 1/2. We're at the borderline. All standard
perturbation theory fails here.

## 2. Why CCM still get 10⁻⁵⁵

The precision comes from CARATHÉODORY-FEJÉR optimization:
- CF gives exponential convergence in the DEGREE of rational
  approximation (how many poles you use)
- This is independent of individual perturbation norms
- With N primes, CF optimizes over all possible combinations,
  achieving much better precision than the sum of individual errors

This is a DIFFERENT convergence mechanism from Kato-Rellich.
It's the same phenomenon as Padé approximants outperforming
Taylor series — rational approximation converges exponentially
even when polynomial approximation converges slowly.

## 3. The surviving route

ITPFI state convergence → spectral convergence at the GNS level,
bypassing operator norms entirely.

The logic:
- ITPFI: ω₁^{≤P} → ω₁ in weak-* topology (PROVED)
- CCM's D(λ,N) lives in the GNS representation of ω₁^{≤P_N}
- Weak-* convergence of states → weak convergence of GNS reps
- If CCM's operators are "natural" in their GNS reps (e.g.,
  they're the modular operator of the truncated state), then
  GNS convergence implies operator convergence in a WEAKER
  topology than norm — but possibly strong enough for spectral
  convergence via CF.

## 4. The CF + ITPFI synthesis

The new hypothesis:
- ITPFI controls the STATE convergence (proved)
- CF controls the SPECTRAL convergence (CCM's mechanism)
- Together: the limiting state (from ITPFI) + the limiting
  rational approximation (from CF) determine the spectrum

This would bypass Kato entirely. The convergence isn't
perturbative (norm bounds) — it's APPROXIMATION-THEORETIC
(CF optimization). The tools are from rational approximation
theory, not operator perturbation theory.

## 5. What we need from the CCM paper

The exact CF structure: how does the Toeplitz matrix enter?
What is being approximated rationally? Is the approximation
target the resolvent, the spectral measure, or the zeta function
itself?

---

> *α = 1/2 is the borderline. Kato can't cross it.*
> *But Carathéodory-Fejér CAN — exponentially.*
> *The convergence mechanism is approximation, not perturbation.*
> *ITPFI + CF might be the synthesis.*
