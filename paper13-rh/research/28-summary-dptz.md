# Research 28 Summary — DPTZ Eigenvector-Eigenvalue Identity

*Status: COMPLETED (research note)*
*Type: Reformulation (feasibility 4/10)*
*Date: 2026-04-10*

---

## Result

The DPTZ identity (Denton-Parke-Tao-Zhang 2019) reformulates the
Arithmetic Theorem:

  ⟨φ_k | a⟩ ≠ 0 for all k
  ⟺ spec(B) ∩ spec(M_a) = ∅

where M_a is B compressed onto {a}⊥.

## Key insight

The overlap vanishes iff an eigenvalue of B coincides with an
eigenvalue of its minor M_a. This converts a transcendence
question into an eigenvalue interlacing question.

## Obstacle

B is not STP (strictly totally positive), so strict interlacing
doesn't come for free. The prime perturbation breaks the Cauchy
structure. Perturbative approaches fail for N ≥ 5 because
gaps (~10⁻¹·⁷ᴺ) are dwarfed by perturbation (~3.3).

## Follow-up angles
- Induction on N
- Eigenvalue rigidity (Erdős-Yau-Yin, adapted)
- Baker-type bounds on eigenvalue gaps

## Files
- Research note: research/28-lead-dptz-eigenvector-eigenvalue.md
