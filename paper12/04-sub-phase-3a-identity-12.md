# Ledger 04: Sub-phase 3.A, Thread 3a — Identity 12 Rigorous

*The unitary equivalence between the QG5D e-circle and the Bost–*
*Connes C\*-dynamical system at β = 1 is now a theorem, with explicit*
*Hilbert spaces, an explicit unitary, and verified intertwining of*
*five operator pairs. The foundation of Phase 3 is in place.*

*Date closed: 2026-04-09*

---

## One-sentence summary

The map U: |n⟩_e ↦ μ_n Ω_1 extends to an explicit unitary
H_e → H_1^{(N\*)} between the e-circle's positive-frequency
Hilbert space and the N\*-labelled subspace of the Bost–Connes
GNS space at β = 1, intertwining five operator pairs (T_e ↔ H_BC,
D_n ↔ μ_n, E_r ↔ e(r), R̂_geom ↔ R̂, scaling-thermal state ↔ ω_1),
making Identity 12 a theorem of operator algebras rather than a
"semi-rigorous" identity.

---

## What closed

**The theorem.** Identity 12 is now a precise statement: there
exists a unitary U from the e-circle's positive-frequency Hilbert
space H_e (with the Z_2 orbifold and the zero-mode removed) to the
N\*-labelled subspace H_1^{(N\*)} ⊂ H_1 of the Bost–Connes GNS
space at the unique critical KMS state ω_1, such that:

| e-circle | ↔ | Bost–Connes |
|:---------|:---|:-----------|
| basis vector \|n⟩_e (cosine mode at frequency n/R) | ↔ | μ_n Ω_1 (n-th BC monomial on the cyclic vector) |
| scaling generator T_e = log(R · p̂_e), spec = {log n} | ↔ | BC Hamiltonian H_BC = log N̂, spec = {log n} |
| dilation operator D_n (composition rule D_n D_m = D_{nm}) | ↔ | BC isometry μ_n (relation μ_n μ_m = μ_{nm}) |
| phase operator E_r at rational angles r ∈ Q/Z | ↔ | BC phase generator e(r), Hecke relation matched |
| scaling-thermal state φ_1 = ⟨Ω_e, · Ω_e⟩ | ↔ | critical KMS state ω_1 |

The proof is direct: define U on the basis, verify by computation
that it's an isometry (using the orthonormality of {μ_n Ω_1} from
the regularised KMS condition at β = 1), extend to a unitary by
density, then verify each intertwining relation on the dense
subspace and extend by closure.

**The connection to Phase 2.** Identity 12 makes the Phase 2
operator R̂ (which lives on the Riemann subspace H_R ⊂ H_1) the
unitary image of an e-circle operator R̂_geom on the corresponding
e-circle subspace H_e^R = U\* H_R. The framework's "compact
dimension" (geometric R) and the Bost–Connes "smallest spectral
feature" (R_1 = (ℓ_P/π) · exp(γ_1 · π²/2)) are the same object in
two presentations.

---

## What this changes

Identity 12 is the **precondition** for every other Phase 3 thread.
With it rigorous:

- **Thread 3b (derive the 23 formulas).** Each γ_n × (geometric
  factor) becomes a matrix element of an operator on H_1 in the
  basis {μ_n Ω_1}. The derivation is reduced to a computation. The
  CC formula's 5 ppb match becomes a second-order perturbative
  expansion.

- **Thread 3e (cosmic transition amplitudes).** ⟨γ_m | U_BC+matter
  | γ_n⟩ is now a well-defined matrix element on H_1 — well-defined
  because H_1 itself is now a known Hilbert space with known
  operators.

- **Thread 3g.\* (transposition of the 8 framework theorems).**
  Each framework theorem about the e-circle becomes a theorem about
  H_1^{(N\*)} via the unitary U. The transposition is now mechanical
  (apply U) rather than conjectural.

- **Thread 3h.1 (RH as physical theorem).** The scaling generator
  T_e on the e-circle has spectrum {log(n) : n ∈ N\*}, all real.
  Identity 12 says T_BC on the BC side has the same spectrum after
  identification. Reality of the spectrum is manifest. The
  remaining piece for the full RH argument (the inclusion of {γ_n}
  in spec(T_BC), via the Mellin-dual extension) is now structurally
  clear.

In short: Identity 12 turns Phase 3 from "a programme of
correspondences to investigate" into "a programme of computations
to perform on a well-defined Hilbert space".

---

## What is still open inside thread 3a

| Sub-thread | Status |
|:-----------|:-------|
| Core Identity 12 (U, intertwining of 5 operator pairs) | **DONE** |
| Galois sector extension (the full equivalence H_e^full → H_1) | **DEFERRED** as sub-thread 3a' |
| Intrinsic definition of the scaling-thermal state φ_1 on A_e | **DEFERRED** to thread 3f (CCM endomotive) |

The two deferred items are not blockers. The core Identity 12 is
sufficient for every other Phase 3 thread. The deferred items
sharpen Phase 3.B and 3.C but are not preconditions.

---

## Pointers

| File | What it contains |
|:-----|:-----------------|
| `research/04-identity-12-rigorous.md` | The theorem statement, the construction of H_e and U, the proof of the unitary equivalence, the verification of the five intertwining relations, the connection to R̂ from Phase 2, the open sub-threads |
| `research/02-quantize-R-construction.md` | The Phase 2 construction of R̂ (now intertwined with R̂_geom on the e-circle side via Identity 12) |
| `03-phase-3-plan.md` Section 1.1 | The full enumeration of Phase 3 threads (3a–3h) |
| `00-attack-plan.md` Section 4 | The original Phase 3 plan |
| `../riemann-hypothesis/research/69-r27-bost-connes-realization.md` | The original semi-rigorous Identity 12 (R27, April 6, 2026) |

---

## Next move

The next thread in sub-phase 3.A is **3b: derive the 23 Riemann
formulas from BC first principles**. With Identity 12 rigorous, each
formula is a matrix element of an operator on H_1, and the
derivation is a computation. The natural starting point is the 5 ppb
CC formula, which is the deepest empirically verified relation and
the one most directly tied to R̂ (Phase 2).

In parallel, threads 3c (find γ_7, γ_12, γ_13, γ_14), 3e (cosmic
transition amplitudes for the selection rule), and 3g.\* (the
transposition of the 8 framework theorems) can all proceed. They no
longer block each other once Identity 12 is in place.

---

*Identity 12 is a theorem. Phase 3 has its foundation. Every other*
*thread now has a rigorous Hilbert-space setting in which to work.*

*The e-circle is the Bost–Connes system, exactly. The framework's*
*compact dimension is the smallest spectral feature of the explicit*
*formula. Same object, two names.*
