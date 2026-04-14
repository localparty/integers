# Schanuel's Conjecture and Algebraic Independence of Riemann Zeros

*A research programme (not a proof skeleton).*
*Status: ~1/10.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-13*

---

## Entry point

The QG5D framework uses exp(gamma_n pi^2 / 2) as literal eigenvalues
of the operator R-hat, where {gamma_n} are the imaginary parts of
the nontrivial Riemann zeros. Schanuel's conjecture (1962) states:

> If z_1, ..., z_n are Q-linearly independent complex numbers, then
> the transcendence degree of Q(z_1, ..., z_n, e^{z_1}, ..., e^{z_n})
> over Q is at least n.

Applied to z_k = gamma_k pi^2 / 2: if the {gamma_k pi^2 / 2} are
Q-linearly independent, then the eigenvalues {exp(gamma_k pi^2 / 2)}
are algebraically independent over Q. This has direct consequences
for the independence of the framework's predictions.

---

## The implication for the framework

The framework makes 36 numerical predictions derived from the
spectral data of the BC algebra. These predictions are functions of
the eigenvalues exp(gamma_n pi^2 / 2) for small n. If Schanuel
holds:

1. **Independence of predictions.** The 36 predictions are
   NECESSARILY algebraically independent if they depend on distinct
   zeros. No hidden algebraic relation can reduce the prediction
   count. Each prediction carries independent empirical content.

2. **No accidental coincidences.** Two predictions can agree
   numerically only if they are derived from the same combination of
   zeros. Schanuel forbids "accidental" algebraic relations among
   different exp(gamma_n pi^2 / 2) values.

3. **Falsifiability strengthened.** If any two predictions that
   depend on DIFFERENT zeros happen to coincide algebraically,
   Schanuel would be violated. This is logically possible but
   considered extremely unlikely.

---

## The reverse implication

If the framework's 36 predictions are empirically confirmed AND some
predictions that depend on different zeros turn out to coincide
algebraically, this would constitute:

- Evidence AGAINST Schanuel's conjecture (which would be extraordinary)
- Or evidence that the predictions do not depend on the zeros in the
  way the framework claims (which would require revising the framework)

In practice, this reverse implication is a logical observation rather
than a practical test.

---

## Connection to RH

Schanuel connects to RH through the Q-linear independence of the
Riemann zeros {gamma_n}:

1. **Simplicity of zeros.** Conjectured (not proved) that all zeros
   are simple: gamma_m != gamma_n for m != n. A prerequisite.

2. **Q-linear independence.** No nontrivial relation sum a_k gamma_k = 0
   with a_k in Q. Much stronger than simplicity. Widely believed, far
   from proved.

3. **The chain.** Q-linear independence of {gamma_n} implies same for
   {gamma_n pi^2/2}, and Schanuel gives algebraic independence of
   {exp(gamma_n pi^2/2)}.

4. **Conditional hierarchy:**
   RH (Paper 13) --> simplicity (open) --> Q-linear indep. (open)
   --> Schanuel (open) --> algebraic independence of eigenvalues

---

## What is known about Schanuel

- **Lindemann-Weierstrass theorem (1885):** If z_1, ..., z_n are
  Q-linearly independent ALGEBRAIC numbers, then e^{z_1}, ...,
  e^{z_n} are algebraically independent. This is Schanuel for
  algebraic z_k (proved).

- **Known cases:** Schanuel is proved for n = 1 (Hermite-Lindemann).
  For n >= 2, open. Even n = 2 with z_1 = 1, z_2 = pi (algebraic
  independence of e and pi) is open.

- **The Riemann zeros are transcendental.** This is not known for
  ANY specific zero. The algebraic independence of even two zeros
  is completely open.

---

## Programme structure

This is NOT a proof skeleton. The route to any result is:

    RH --> simplicity --> Q-linear indep. --> Schanuel --> alg. indep. of eigenvalues
    (Paper 13)  (open)      (open)            (open)         (conclusion)

Each arrow is a major open problem. The programme's value is not in
closing these gaps (which may be impossible with current methods) but
in:

1. Making the LOGICAL STRUCTURE explicit
2. Identifying what the framework NEEDS to be self-consistent
3. Providing a target for future transcendence theory

---

## Milestones (speculative)

1. Prove that gamma_1 = 14.134725... is transcendental (currently
   open -- not known for any specific zero)
2. Prove Q-linear independence of {gamma_1, gamma_2} (currently open)
3. Verify numerically that no algebraic relation of low degree holds
   among {gamma_n pi^2/2, exp(gamma_n pi^2/2)} for small n
4. Investigate whether the ITPFI factorization (Paper 13) constrains
   the algebraic properties of the zeros
5. Formulate a "BC Schanuel" conjecture specific to the exponentials
   arising from the BC algebra

---

## Honest accounting

Status: ~1/10. The connection between Schanuel and the framework is
clear and logically precise. But proving anything in this direction
is extremely hard: the transcendence of a single Riemann zero is
open, let alone algebraic independence of several. The programme
serves primarily as a CONSISTENCY CHECK on the framework and a map
of the logical dependencies. The entry point is solid; the closure
is not visible with current methods.

---

Next step: a dedicated cell-fill run on Milestone 3 (numerical verification of algebraic independence for small n).
