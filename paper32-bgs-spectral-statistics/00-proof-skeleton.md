# Berry-Tabor / BGS Conjecture via Type III_1 Ergodicity

*A seven-link proof skeleton.*
*Status: ~2/7.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-13*

---

## The claim in one paragraph

The nontrivial zeros of the Riemann zeta function exhibit GUE
(Gaussian Unitary Ensemble) pair-correlation statistics. This is the
content of the Berry-Tabor / Bohigas-Giannoni-Schmit conjecture
applied to the Riemann zeros, supported by Montgomery's 1973
calculation and Odlyzko's 1987-2001 numerical verification to
10^{22}. The seven-link chain below derives GUE statistics from the
type III_1 structure of the BC algebra at KMS_1, routing through
ergodic modular flow, absolutely continuous spectral measure, and
unitary symmetry class. This provides the SPECTRAL EXPLANATION for
why the zeros look like eigenvalues of random unitary matrices.

---

## The seven-link proof chain

| Link | Content | Status | Notes |
|:-----|:--------|:-------|:------|
| 1. Type III_1 factor | BC algebra at KMS_1 is a type III_1 factor via Araki-Woods with lambda_p = 1/p | KNOWN | Bost-Connes 1995 (KMS_1 uniqueness); Araki-Woods classification; Paper 13 research/265 (ITPFI factorization) |
| 2. Ergodic modular flow | The modular automorphism group sigma_t of the KMS_1 state is ergodic | NEEDS PROOF | Type III_1 implies Sd(M) = R (Connes spectrum), which gives ergodicity of the flow of weights; need to verify this transfers to sigma_t on the BC algebra specifically |
| 3. Spectral measure | Ergodic modular flow implies absolutely continuous spectral measure for the associated unitary group U_t = exp(i Delta t) where Delta = log(modular operator) | NEEDS PROOF | Standard for ergodic flows via SNAG theorem; the spectral measure of an ergodic unitary group has no atoms |
| 4. Level repulsion | Absolutely continuous spectral measure + unitary symmetry class (time-reversal broken) implies level repulsion | NEEDS PROOF | This is the BGS heuristic made rigorous: the symmetry class determines the universality class |
| 5. GUE pair correlation | Level repulsion in unitary class implies GUE pair correlation: 1 - (sin(pi s) / (pi s))^2 | NEEDS PROOF | Random matrix theory: GUE is the unique universal distribution for the unitary symmetry class with level repulsion |
| 6. Spectral realization | GUE for BC eigenvalues = GUE for Riemann zeros, because spec(D_infinity) = {gamma_n} | CONDITIONAL | Conditional on Paper 13 (RH proof, spectral realization of zeros) |
| 7. Montgomery-Odlyzko | Montgomery pair correlation conjecture confirmed numerically by Odlyzko (10^{22} zeros) | KNOWN | Montgomery 1973; Odlyzko 1987-2001 |

---

## The proof chain diagram

```
Link 1:  BC at KMS_1 is type III_1 factor (KNOWN)
           |
Link 2:  Modular flow sigma_t is ergodic (NEEDS PROOF)
           |
Link 3:  Ergodicity --> absolutely continuous spectral measure (NEEDS PROOF)
           |
Link 4:  AC measure + unitary class --> level repulsion (NEEDS PROOF)
           |
Link 5:  Level repulsion + unitary class --> GUE pair correlation (NEEDS PROOF)
           |
Link 6:  spec(D_infinity) = {gamma_n} --> GUE for zeros (CONDITIONAL on Paper 13)
           |
Link 7:  Montgomery-Odlyzko numerical confirmation (KNOWN)
```

---

## Physical observable

**Energy-level spacing of 5D geometry.** In the QG5D framework, the
Riemann zeros are eigenvalues of the Dirac operator D on the
noncommutative space. The GUE statistics of these eigenvalues are
the energy-level statistics of the quantum geometry -- exactly the
statistics expected for a quantum chaotic system with broken
time-reversal symmetry (the BGS conjecture). The BC algebra provides
the "quantum Hamiltonian" whose level statistics are GUE.

---

## Key difficulties

**Link 2 is the bottleneck.** Type III_1 guarantees Sd(M) = R (full
Connes spectrum), which means the flow of weights on the crossed
product is ergodic. But transferring this to ergodicity of sigma_t
on the BC algebra itself requires:

- The centralizer M^{sigma} is a factor (equivalently, the modular
  flow is centrally ergodic)
- For type III_1 with separable predual, central ergodicity holds
  automatically (Connes 1973, Theorem 5.3.1)
- The remaining gap: verify that the BC algebra at KMS_1 has
  separable predual

**Link 4 is conceptually subtle.** The passage from "absolutely
continuous spectral measure" to "level repulsion" is the heart of
the BGS conjecture. The heuristic argument (Berry 1985) uses
semiclassical periodic orbit theory. A rigorous proof would need
either:

- A semiclassical limit for the BC system (unclear what this means)
- A direct random matrix argument from the spectral measure properties
- A transfer principle from the known GUE universality results
  (Erdos-Yau 2012) for Wigner matrices

---

## Connections in the programme graph

- **BGS --> RH:** Link 6 is conditional on Paper 13. If RH holds,
  the zeros ARE eigenvalues, and their statistics are GUE.
- **BGS --> Twin Primes:** GUE pair correlation at close spacing
  constrains prime gaps (see twin-primes programme).
- **BGS --> QG5D:** GUE statistics = quantum chaos of the 5D geometry.

---

## Honest accounting

Links 1 and 7 are settled. Links 2-5 constitute the core mathematical
challenge. Link 6 is conditional on Paper 13. The chain is ~2/7 complete.
The entry point (type III_1 structure) is solid; the closure requires
new results in ergodic theory of modular flows and rigorous random
matrix universality.

---

Next step: PCA verification run on Link 2 (ergodicity of modular flow for BC at KMS_1).
