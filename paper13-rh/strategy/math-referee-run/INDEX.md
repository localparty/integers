# Referee Run r02 — Index

*Paper 13 (v2: CCM + ITPFI + Bögli + Hurwitz) — Exhaustive
Mathematical Referee Review.*

*Written 2026-04-10. Referee: Claude Opus 4.6 as advanced
math referee. Directive: find every gap; default to "the proof
is wrong"; do not be diplomatic.*

---

## Top-level

- [summary.md](summary.md) — **Start here.** Overall verdict
  and the required closing statements.
- [clay-checklist.md](clay-checklist.md) — Master roll-up of
  all ~30 mandatory checks.
- [computation-log.md](computation-log.md) — Actual computational
  checks performed, with findings (Ξ(0) value, Theorem 7.1
  inequality range, AE margin arithmetic, etc.).

## Per-point deep dives

Each point has a 00-statement.md, several subfiles, and a
verdict.md. Read verdict.md first for each point.

### A1 — CCM Construction (HEAVY)
- [A1 verdict](points/A1-ccm-construction/verdict.md)
- 00 statement, 01 operators, 02 self-adjointness, 03 theorem-510,
  04 missing-steps, 05 preprint-risk, 06 circularity.

### A2 — ITPFI Factorization (LIGHT)
- [A2 verdict](points/A2-itpfi/verdict.md)
- 00 statement, 01 factorization, 02 state-convergence,
  03 form-convergence.

### B1 — Archimedean Estimate (MEDIUM)
- [B1 verdict](points/B1-archimedean/verdict.md)
- 00 statement, 01 ratio, 02 uniformity, 03 constant.

### B2 — Eigenvector Approximation (MEDIUM)
- [B2 verdict](points/B2-eigenvector-approx/verdict.md)
- 00 statement, 01 davis-kahan, 02 itpfi-triangle, 03 error-norm,
  04 n-dependence.

### B3 — Teschl–Bögli Synthesis (HEAVY)
- [B3 verdict](points/B3-teschl-boegli/verdict.md) ← **most
  critical technical point**
- 00 statement, 01 gsrc-verification, 02 form-difference,
  03 galerkin, 04 klmn-closability, 05 discrete-compactness,
  06 boegli-application, 07 spectral-pollution,
  08 synthesis-novelty.

### C1 — Hurwitz Application (MEDIUM)
- [C1 verdict](points/C1-hurwitz/verdict.md)
- 00 statement, 01 uniform-convergence, 02 holomorphicity,
  03 normalization, 04 multiplicity, 05 coverage.

### C2 — AE Simplicity (MEDIUM)
- [C2 verdict](points/C2-ae-simplicity/verdict.md)
- 00 statement, 01 ae-meaning, 02 finite-certification,
  03 prolate-extension, 04 sufficiency, 05 crossing-gap.

### D1 — The Assembly (HEAVY)
- [D1 verdict](points/D1-assembly/verdict.md) ← **most critical
  exposition point**
- 00 statement, 01 chain-integrity, 02 logical-structure,
  03 interface-gaps, 04 connes-comparison, 05 failure-point.

### D2 — CCM Dependency (MEDIUM)
- [D2 verdict](points/D2-ccm-dependency/verdict.md)
- 00 statement, 01 conditionality, 02 ccm-error-scenario,
  03 honest-accounting, 04 layer-independence,
  05 connes-comparison.

## Check files

Per-criterion pass/fail notes with confidence ratings:

- CCM-foundation/: CCM1 through CCM5 (5 files)
- IT-itpfi/: IT1 through IT3 (3 files)
- ES-estimates/: ES1 through ES5 (5 files)
- BG-boegli/: BG1 through BG5 (5 files)
- HZ-hurwitz/: HZ1 through HZ4 (4 files)
- AE-simplicity/: AE1 through AE4 (4 files)
- CL-clay/: CL1 through CL4 (4 files)

Total: 30 check files.

---

## Headline findings (TL;DR)

1. **Architecture is right.** The six-layer chain (CCM operators
   + ITPFI state convergence + estimates + Teschl/Bögli +
   Hurwitz) is the right shape for closing the gap CCM leaves.

2. **Execution has concrete gaps.** In decreasing severity:
   - Section 10.4 Step 4 (final deduction) is tautological as
     written. The correct argument — Hurwitz in the complex
     plane applied to the real-zero property of ξ̂_N — is never
     explicit. This is the single most important exposition fix.
   - Theorem 7.1's proof is broken for λ > e^π ≈ 23.14 (I
     verified algebraically and computationally). At the paper's
     λ = √14 it is fine.
   - KLMN closability argument (Corollary 9.6) uses an
     incorrect general implication ("positivity ⇒ closability").
   - Multiple estimates depend on internal research notes not
     in the preprint.
   - AE simplicity at N > 20 is heuristic, not theorem.
   - λ-vs-N notational conflation throughout Sections 5–10.

3. **Cosmetic errors found by computational check.** Ξ(0) is
   stated as "1/2" in Section 10.3 and with a wrong formula in
   Appendix E.4. The correct value is Ξ(0) = ξ(1/2) ≈ 0.4971.
   Still nonzero, so Hurwitz applies, but the errors undermine
   reader confidence.

4. **Dependence on unrefereed CCM preprint.** Layer 1 is
   Connes-Consani-Moscovici 2025 (arXiv:2511.22755). This is a
   2025 preprint, not yet refereed. Paper 13 takes at least four
   load-bearing CCM results on authority without independent
   verification: Theorem 4.2 (self-adjointness), Theorem 5.10
   (all three parts), Lemma 7.2 (Meixner-Schäfke), Lemma 7.3
   (k̂_λ → Ξ).

5. **Theorem 1.1 framing is over-stated.** The paper claims RH
   unconditionally but the proof is conditional on CCM. The
   honest-accounting section acknowledges 8/10 but the headline
   theorem does not. A refereeable version must restate
   Theorem 1.1 as "assuming CCM 2025, RH holds".

6. **Self-rating: 8/10. My rating: 6-7/10 as written.** The paper's
   self-rating is slightly optimistic because it attributes the
   gap entirely to CCM's preprint status, ignoring the Layer 3-5
   rigor and exposition issues I identified.

7. **Clay Prize eligibility: NO**, as written. Multiple obstacles
   (unrefereed preprint dependence, framing, rigor gaps, and
   the Clay 2-year publication waiting period).

---

## Provenance note

This review was written by an AI model (Claude Opus 4.6) with
access to the full preprint, strategy documents, and Clay
reference materials. The computational checks were performed in
Python/mpmath at 50+ digit precision and are reproducible. The
review should be treated as a substantive first-pass referee
report, not a final word. A human expert in operator algebras
or spectral theory should independently verify the concrete
findings flagged here (especially the Theorem 7.1 λ ≤ e^π
restriction and the KLMN closability implication, both of which
I am confident in but which should be double-checked).
