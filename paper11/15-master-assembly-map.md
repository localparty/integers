# Master Assembly Map

**Where every new result goes during paper assembly**

---

## Theorem K.4 — All-Orders UV Finiteness

**Source:** `04-all-orders-inductive-proof.md`
**Computations:** `code/mercedes_route_c.py`, `code/bootstrap_L4_verify.py`
**Research note:** `research/01-mercedes-route-c-bphz-factorisation.md`,
                    `research/02-inductive-bootstrap-all-orders.md`

**Goes into:** Paper 1, Appendix K

**Specific changes:**
- Add new Section K.8: "All-Orders Vanishing by Strong Induction"
- Insert Theorem K.4 (the inductive bootstrap)
- Update Theorem K.3: change "Conditional" to "Superseded by K.4"
- Remove "conditional at L≥3" caveats throughout K.5-K.6
- Update the conclusion of Appendix K

**Cross-references to update:**
- Paper 1 abstract: change "established through L=2 explicitly..." to
  "established at all orders by strong induction (Theorem K.4)"
- Paper 4, Appendix D (Higgs naturalness): the "L≥2 corrections vanish"
  claim becomes unconditional
- Paper 6 (dilaton potential exact): same — unconditional
- Paper 10: this enables extending scheme-independence beyond L=2

---

## Theorem 7.2 — Fast Scrambler from e-Dynamics

**Source:** `06-fast-scrambler-derivation.md`
**Research note:** `research/03-fast-scrambler-from-e-dynamics.md`

**Goes into:** Paper 3, Section 7

**Specific changes:**
- Insert new Section 7.7: "Derivation of the Fast-Scrambler Property"
- Insert Theorem 7.2 (fast scrambling from Rindler dynamics)
- Update Theorem 7.1 → Theorem 7.1' (unconditional Page curve)
- Remove the "conditional on Sekino-Susskind" caveat
- Update Section 7.6 (stratification): Level 3 (open problem) becomes
  Level 2 (proved in this paper)

**Cross-references to update:**
- Paper 3 abstract: change "Page curve recovered conditionally" to
  "Page curve unconditional (Theorem 7.1')"
- Paper 3 Section 11 (scrambling time): the formula t_scr =
  (β/2π)ln(S_BH) was previously cited from Sekino-Susskind; now derived
- Paper 3 Section 12 (stratification): update Level 3 → resolved

---

## Theorem 11.1-11.5 — Gauge Group from Entanglement

**Source:** `09-paper-11-proof-chain.md`, `08-paper-11-outline.md`
**Computations:** `code/slocc_a2_roots.py`, `code/econs_ghz_bridge.py`,
                  `code/kirillov_orbit.py`, `code/fermion_quantum_numbers.py`
**Research notes:** `research/07-10`
**Caveats:** `10-paper-11-caveats.md`, `11-paper-11-caveats-closed.md`

**Goes into:** Paper 11 (NEW PAPER)

**Paper 11 structure:**
- Section 1: Introduction (the question, the answer)
- Section 2: Three qubits on the e-circle (setup)
- Section 3: The GHZ orbit and the A₂ root system (Theorem 11.1)
- Section 4: e-conservation selects the GHZ orbit (Theorem 11.2)
- Section 5: The Kirillov orbit method — SU(2)³ → SU(3) (Theorem 11.3)
- Section 6: The fermion decomposition (Theorem 11.4)
- Section 7: Main theorem — G_SM from the e-circle (Theorem 11.5)
- Section 8: Why three generations (the uniqueness argument)
- Section 9: The complete holonomy table (with CP² area law)
- Section 10: Predictions and open problems
- Appendix A: Detailed tangent space computation
- Appendix B: Numerical verifications
- Appendix C: The four caveats and their closure

---

## CP² Area Law — Confinement from Geometry

**Source:** `13-three-gap-strategies.md` (strategy)
**Computation:** `code/cp2_area_law.py`
**Research note:** `research/11-cp2-area-law-confinement.md`

**Goes into:** Paper 5, Section 3 + Paper 8, Appendix H

**Paper 5 changes:**
- Update Section 3.4: change "central open problem" language
- Insert new Section 3.5: "Proof via 2D YM on CP¹"
- Add the exact formula σ = g²C₂(fund)/2 for SU(3)
- Reference Paper 8 Appendix H for the SU(2) template
- Update Section 9 (open problems): mark area law as "PROVED"

**Paper 8 changes:**
- Extend Appendix H to include the SU(3) generalisation
- Add new Section H.7 or H.8: "Generalisation to CP¹ ⊂ CP² for SU(3)"
- Reference Paper 5 for the geometric mechanism
- The status table should reflect this dual derivation

**Connection to Paper 11:**
- Paper 11 Section 9 (holonomy table) cites this proof
- The colour = entanglement → confined chain is now complete

---

## OC-2 Diagnosis (Not a Closure)

**Source:** `05-oc2-theorem-u-status.md`
**Research note:** `research/04-oc2-theorem-u-blockage.md`

**Goes into:** Paper 4 + Paper 7

**Paper 4 changes:**
- Update Section 6.5b/6.7: clarify that M_KK is conditional on
  the CC problem (= Theorem U), not on a missing computation
- Update Open Problem OC-2: reclassify from "Open Calculation" to
  "Connected to the Cosmological Constant Problem"

**Paper 7 changes:**
- Section 4 (Theorem U): add explicit cross-reference to OC-2
- Show OC-2 is the geometric form of the CC problem
- Connect to the future Paper 11 Candidate C (M2-instantons)

---

## Reference Index for Assembly

When Paper X cites a result from this session, use this map:

| Result | Citation in other papers |
|--------|--------------------------|
| Theorem K.4 | "Paper 1, Appendix K, Theorem K.4" |
| Theorem 7.2 / 7.1' | "Paper 3, Section 7.7, Theorem 7.2" |
| CP² area law | "Paper 5, Section 3.5; Paper 8, Appendix H.8" |
| Paper 11 Theorem 11.5 | "Paper 11, Theorem 11.5 (Main Theorem)" |
| Paper 11 colour = entanglement | "Paper 11, Theorem 11.4 and Section 7" |
| OC-2 = CC problem | "Paper 7, Theorem U; Paper 4, Open Problem OC-2 (revised)" |

---

## Files Used by Each Paper

### Paper 1 (UV finiteness update)

**Read from:**
- `04-all-orders-inductive-proof.md` (Theorem K.4 statement)
- `research/02-inductive-bootstrap-all-orders.md` (proof details)
- `code/mercedes_route_c.py` + `bootstrap_L4_verify.py` (numerics)

**Sections to update:** Abstract, Appendix K (especially K.5, K.6),
status table.

### Paper 3 (Page curve update)

**Read from:**
- `06-fast-scrambler-derivation.md` (Theorem 7.2 statement)
- `research/03-fast-scrambler-from-e-dynamics.md` (derivation)

**Sections to update:** Abstract, Section 7 (especially 7.6, 7.7 new),
Section 11 (scrambling time), Section 12 (status).

### Paper 5 + Paper 8 (CP² area law)

**Read from:**
- `research/11-cp2-area-law-confinement.md` (full proof)
- `code/cp2_area_law.py` (numerics)

**Paper 5 sections:** 3.4, 3.5 (new), 9 (open problems → resolved).
**Paper 8 sections:** Appendix H (extension to SU(3)).

### Paper 11 (NEW)

**Read from EVERYTHING in:**
- `08-paper-11-outline.md` (structure)
- `09-paper-11-proof-chain.md` (theorems)
- `10-paper-11-caveats.md` + `11-paper-11-caveats-closed.md` (caveats)
- `research/07, 08, 09, 10, 11` (computations + proofs)
- `code/slocc_a2_roots.py`, `econs_ghz_bridge.py`, `kirillov_orbit.py`,
  `fermion_quantum_numbers.py` (verification)
- `research/11-cp2-area-law-confinement.md` (for Section 9, holonomy table)

---

## Assembly Order

1. **Update Paper 1 first** — Theorem K.4 unblocks references in
   Papers 4, 6, 10 (which currently cite "conditional at L≥3").
2. **Update Paper 3** — Theorem 7.2 is independent.
3. **Update Paper 5 + Paper 8 simultaneously** — The CP² area law
   appears in both. Coordinate the cross-references.
4. **Assemble Paper 11** — This is the largest piece. Can proceed
   in parallel with the updates.
5. **Final cross-reference audit** — Run through all papers to
   ensure references to the new theorems are consistent.

---

## What's Still Missing

After this assembly map, the following items would help:

1. **Paper 11 abstract** — `16-paper-11-abstract.md`
2. **Paper 11 introduction** — `17-paper-11-introduction.md`
3. **Unification narrative** — `18-unification-narrative.md`
   (the high-level story for Section 9 of Paper 11)
4. **Notation harmonisation** — A short doc on conventions

These will be written next.
