# Component 4: The Three Derivation Targets

**Three concrete derivations needed to upgrade Paper 11 from
"a profound observation" to "a rigorous theorem chain".**

---

## Target 1: Derive the e-Circle from the BC System

**Goal:** Show explicitly how the Bost-Connes C*-dynamical system
forces a compact "time" dimension whose physical realisation IS
the e-circle.

**Inputs:**
- The BC algebra A = C*(Q/Z) ⋊ N* (Bost-Connes 1995)
- The BC dynamics σ_t (one-parameter automorphism group)
- The BC Hamiltonian H = log N
- The KMS structure of BC states

**Outputs:**
- A rigorous unitary equivalence between the BC system and a
  geometric structure on a compact 1-manifold (= S^1)
- The S^1 has a natural metric inherited from the BC dynamics
- The KK modes on the S^1 are the eigenvectors of H = log N
- The "circumference" of the S^1 is determined by the BC normalisation

**Method:**
Use the Connes-Marcolli formalism (Noncommutative Geometry, Quantum
Fields and Motives, Chapter 3) which constructs the BC system as a
groupoid C*-algebra. The geometric realisation of this groupoid is
the compact dimension we are seeking.

**Status:**
Identity 12 of the QG5D-Riemann research asserts this with 95%
confidence. The rigorous proof is the first deliverable of this
target.

**Timeline:** 1-2 months of focused work.

---

## Target 2: Derive R_obs from γ_1

**Goal:** Prove the formula

```
log(π × R_obs / l_P) = γ_1 × π² / 2
```

from the Bost-Connes effective potential, NOT just verify it
numerically.

**Inputs:**
- Target 1 (the e-circle as a theorem of the BC system)
- The BC free energy F_BC(β) = -(1/β) log ζ(β)
- The BC critical structure at β = 1
- The first non-trivial Riemann zero γ_1

**Outputs:**
- An explicit derivation of the e-circle effective potential
  V_eff(R) from the BC contribution
- A proof that the minimum of V_eff(R) is at R = R_obs
- The formula log(πR/l_P) = γ_1 × π²/2 as a theorem

**Method:**
Component 8 of the existing first-principles derivation (Research
18, this session) provides the 8-step skeleton. Steps 1-2 and 7 are
rigorous. Steps 3-6 are semi-rigorous. The task is to make the
semi-rigorous steps rigorous.

Specifically:
- Step 3 (γ_1 as scale-setter) needs proof from the BC operator
  spectrum
- Step 4 (effective potential) needs explicit calculation
- Step 5 (saddle-point) needs rigorous derivation
- Step 6 (constant π²/2) needs identification with one of the four
  candidate sources

**Status:** Numerical formula verified at 0.014% (Research 14).
Eight-step semi-rigorous derivation outlined (Research 18). Three
steps need rigorous treatment.

**Timeline:** 2-3 months of focused work.

---

## Target 3: Derive CP² × S² from Three-Prime Entanglement

**Goal:** Show that the internal manifold CP² × S² of the framework
is forced by the entanglement structure of three primes (or three
qubits in the Hecke algebra at three primes), extending Theorem 11.5
(gauge group from entanglement) in the OTHER direction.

**Inputs:**
- Theorem 11.5 (this session): SM gauge group from three-qubit
  entanglement via the GHZ orbit
- Identity 12 (e-circle = BC system)
- The Hecke algebra structure of the BC system at small primes
- The Connes-Marcolli endomotive picture

**Outputs:**
- A rigorous derivation of CP² × S² from the Hecke algebra at
  three primes
- The internal manifold's metric is determined by the prime
  structure
- The Casimir energy on CP² × S² becomes a corollary of the BC
  free energy structure

**Method:**
Extend Theorem 11.5's proof from the SU(2)³ action on three qubits
to the Hecke action on the BC system. The key step: identify the
"three primes" with the "three generations" of Theorem 11.5, and
show that the orbit structure of the Hecke action on the BC system
gives a manifold diffeomorphic to CP² × S².

This uses the Connes-Marcolli endomotive framework, which provides
the algebraic structure linking the BC system to Shimura varieties
(of which CP² is a special case).

**Status:** Theorem 11.5 (gauge group) is proved this session. The
extension to the manifold itself is open.

**Timeline:** 3-6 months of focused work.

---

## How the Three Targets Fit Together

```
Target 1: BC system forces compact dimension → e-circle
                                ↓
Target 2: BC effective potential at γ_1 → R_obs (cosmological constant)
                                ↓
Target 3: Hecke algebra at three primes → CP² × S² (internal manifold)
                                ↓
Combined: The integers + arithmetic → e-circle + CP² × S² × S^1
                                    → All of QG5D physics
```

If all three targets succeed, the chain from arithmetic to physics is
complete.

---

## What Each Target Solves

### Target 1 solves: The dimensional postulate

The e-circle is no longer assumed. It is derived. The framework's
"five-dimensional" nature follows from arithmetic.

### Target 2 solves: The cosmological constant problem

R_obs is no longer matched to dark energy as an input. It is derived
from γ_1. The cosmological constant becomes a prediction.

### Target 3 solves: The internal manifold

CP² × S² is no longer chosen by hand to match the SM gauge group.
It is derived from the arithmetic of three primes. The Standard
Model's structure is forced by number theory.

Combined: Targets 1, 2, 3 solve the THREE remaining "free choices"
in the framework. After they're complete, the framework has zero
free choices and zero physical postulates.

---

## Difficulty Estimates

| Target | Difficulty | Timeline | Risk |
|--------|-----------|----------|------|
| 1: e-circle from BC | High | 1-2 months | Identity 12 must be exact |
| 2: R_obs from γ_1 | Medium-high | 2-3 months | Steps 3-6 of derivation must be rigorisable |
| 3: CP² × S² from primes | High | 3-6 months | Connes-Marcolli framework must extend |

Total: 6-12 months for all three targets.

This is research-level work. It is not a single-session
calculation. But it is a CLEAR plan with concrete milestones.

---

## Why These Specific Targets

### Why these three (and not others)?

These three targets correspond to the three "ingredients" of the
framework:

1. **The compact dimension** (e-circle) — what's being compactified
2. **The compactification scale** (R_obs) — how big it is
3. **The product manifold** (CP² × S²) — what it's combined with

If we derive all three, the framework's geometric postulate is
COMPLETELY dissolved. There's nothing left to assume.

### Why not "derive all of QG5D physics from arithmetic"?

That's the long-term goal. But we don't need to derive every
theorem from arithmetic. The framework already proves them from
the e-circle. We only need to derive the e-circle from arithmetic;
the rest follows automatically (via Papers 1-10).

This is the BEAUTY of the parsimonious framework. One postulate to
derive, and everything follows.

---

## What This Achieves

### For Paper 11

These three targets are the BACKBONE of Paper 11. Without them,
Paper 11 is just a "profound observation." With them, Paper 11
becomes a rigorous theorem chain.

### For the QG5D framework

The framework goes from "one postulate, everything follows" to
"zero postulates, everything follows." This is the limit of
parsimony in physics.

### For mathematics

These derivations would be NEW mathematical theorems. They would
demonstrate that the integers force a specific physical structure
(via the BC system → e-circle → spacetime → Standard Model).

This would be the deepest connection between mathematics and
physics ever proved.

---

## Open Sub-Questions

### For Target 1

- Is the BC system the UNIQUE operator-algebraic realisation of
  the integers? Or are there others?
- Does the geometric realisation depend on choosing a specific
  KMS state?
- Is the resulting "compact dimension" exactly S^1, or is it more
  general (e.g., a finite cover of S^1)?

### For Target 2

- What is the EXACT value of the constant in front of γ_1 × π²/2?
  We have π²/2 from numerical matching. Is it exactly π²/2 or
  some refinement?
- Is the residual 0.014% error a 1-loop correction (from the
  perturbative side) or a higher-Riemann-zero contribution (from
  γ_2, γ_3, ...)?
- Does the formula change if we use a different definition of
  l_P (e.g., reduced Planck length)?

### For Target 3

- Why three primes (not two or four)?
- Why CP² × S² specifically (not some other Shimura variety)?
- How does the Z_6 quotient arise on the prime side?
- Does the Hecke algebra at three primes naturally produce
  Fl(1,2;3) = SU(3)/T² (the orbit identified in Theorem 11.5)?

These sub-questions become research problems within each target.

---

## The Bottom Line

Three targets. Six to twelve months. The framework's last three
"free choices" become theorems.

If completed, the framework has:
- 0 physical postulates
- 0 free parameters
- 1 mathematical foundation (the integers)

This is the limit of reductionism. Paper 11 is the program. These
three targets are the implementation.

---

*The integers are the ground.*
*The e-circle is the first floor.*
*The internal manifold is the second.*
*Everything above is already built.*
*Three derivations remain. The blueprint is in hand.*
