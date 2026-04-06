# Research Prompt 36 — Appendix Audit and Generation

> **For:** Claude Opus (systematic, long-running, capable of spawning agents)
> **Date:** April 5, 2026
> **Priority:** CRITICAL — papers cannot be submitted without this
> **Task type:** Audit + generation. Two phases.

---

## The Problem

Papers 1–2 of this series have full appendices for every derivation.
Starting from Paper 3, appendices exist only for some results. The
most recent theorems and proofs — produced during intensive sessions
starting around prompt 18 — exist only in `etc/` working files. The
papers reference these with `etc/frontier-research/...` paths, but
those paths are internal working files, not part of the published
papers. A reader of the arXiv submission will not have access to `etc/`.

Every claim marked **Proved**, **Derived**, **Established**, or
**unconditional** in a paper must have its full derivation either
(a) inline in the paper section itself, or (b) in a numbered appendix
within that paper's directory. Currently, at least 7 major results
violate this requirement.

---

## Phase 1: The Audit

Before generating any appendices, produce a complete audit of the
gap between claims and backing. The audit output goes to
`etc/36-audit-results.md`.

### What to audit

For each paper (3 through 7), check every:
- Section that says a result is "proved", "derived", "established",
  "unconditional", or "exact to all orders"
- Status table row tagged **Proved** or **Derived**
- Theorem statement (Theorem K.1, K.3, 9.1, U, U*, 5.2, etc.)
- Reference to `etc/frontier-research/` from within a paper

For each claim found, determine:
1. **Where is the derivation?** Options:
   - IN PAPER: in a section or existing appendix within the paper directory
   - IN ETC: in `etc/` or `etc/frontier-research/` (working file, not part of paper)
   - INHERITED: from Paper 1 or 2 appendix (cite the appendix label)
   - MISSING: no derivation found anywhere
2. **Is it sufficient?** Even if it's in-paper, is the algebra complete
   or just referenced?
3. **What appendix is needed?** If IN ETC or MISSING, what should the
   new appendix be called and in which paper?

### Audit template (for `etc/36-audit-results.md`)

```markdown
# Appendix Audit Results — April 5, 2026

## Paper 3

| Claim | Location of derivation | Status | Action needed |
|-------|----------------------|--------|---------------|
| Theorem 9.1 unconditional (horizon vertex) | etc/frontier-research/problem3-horizon-vertex.md | IN ETC | Add as Paper 3 Appendix B |
| ...

## Paper 4
...

## Paper 5
...

## Paper 6
...

## Paper 7
...

## Summary
Total claims audited: N
- In-paper (complete): N
- In-paper (partial/referenced only): N
- In etc/ (need converting to appendix): N
- Inherited from Paper 1-2 (OK as cross-reference): N
- Missing (need writing from scratch): N
```

---

## Phase 2: Generate the Missing Appendices

After the audit, generate each missing appendix. Priority order:

### PRIORITY 1 — Paper 3, Appendix B: Horizon Vertex Derivation

**Source:** `etc/frontier-research/problem3-horizon-vertex.md`
**Target:** `paper3/16-appendix-b-horizon-vertex.md`
**Claim:** Theorem 9.1 is unconditional — the horizon vertex factor = 1
is derived, not assumed.

Convert the frontier research document into a clean paper appendix.
The appendix should:
- Be self-contained (no references to `etc/`)
- State the theorem formally at the top
- Provide the proof chain with each step labeled (Proved/New argument/Standard result)
- Be written at the level of a physics journal appendix
- Cross-reference Paper 1 Theorem 2.1 (Noether) and Paper 3 §9.3.2 (Killing vector)
- Remove the "investigation" framing; present as established mathematics

**Key content to include:**
1. The product structure of the 5D BH metric (M⁴ × S¹ with constant R₀)
2. The KK decomposition and S¹ Fourier orthogonality identity
3. The Ward identity factorization
4. The formal statement of the Proposition (vertex = 1 in BH background)
5. The proof (Steps A–D from the frontier file, cleaned up)
6. A brief note on the near-singularity regime (M ~ M_Pl)

---

### PRIORITY 2 — Paper 4, Appendix D: Higgs Mass Naturalness

**Source:** `etc/frontier-research/problem2-higgs-mass.md`
**Target:** `paper4/appendix-D-higgs-naturalness.md`
**Claim:** δm_H² = (g₂²/16π²)(1/r₂²)(−2/3) — one-loop exact, no hierarchy problem

The appendix should:
- State the theorem at the top (Radiative Stability of the Gauge-Higgs Mass)
- Derive Z_{S²}(0) = −2/3 via two methods (direct zeta sum, heat kernel)
- Show the three-layer protection mechanism clearly
- State explicitly: "The one-loop result is exact to all perturbative orders
  by Theorems K.1 and K.3 (Paper 1, Appendix K)"
- Include the proof chain table (Steps 1–12 from the frontier file)
- Remove: the "Standard Hierarchy Problem" framing at the top
  (that goes in the paper section, not the appendix)

---

### PRIORITY 3 — Paper 7, Appendix A: Theorem U* (CC Underivability)

**Source:** `etc/frontier-research/problem1-cc-underivability.md`
**Target:** `paper7/appendix-A-theorem-U-star.md`
**Claim:** ρ_Λ is structurally underivable from any algebraic or
topological mechanism in M-theory on CP²×S²×S¹/Z₂

The appendix should:
- State Definition 1.1 (Geometric input set G) precisely
- State Theorem U* formally
- Give the three-step proof (algebraic bound → non-perturbative bound → desert)
- Include the meV coincidence analysis (§6 of the source) as a subsection
- Include the proof chain table
- Remove: the "Definitions and Setup" numbering; renumber for appendix style

---

### PRIORITY 4 — Paper 3, Appendix C (or expand App A): OS3 to 10⁻⁶⁰

**Source:** `etc/frontier-research/oi3-reflection-positivity.md`
**Target:** Either expand `paper3/15-appendix-a-non-perturbative-completion.md`
with a new §A.7, or create `paper3/16-appendix-b-...` (adjusting numbering)
**Claim:** OS3 (reflection positivity) holds to 10⁻⁶⁰ precision via
frozen dilaton

The content should:
- Be added as a new section (§A.7) at the end of Appendix A, OR
  as a standalone Appendix B (if A is too large already)
- State the result: approximate OS3 to 10⁻⁶⁰
- Give the factorization argument (healthy KK modes + bounded dilaton sector)
- State the bound: |violation| / |positive part| ≤ (δR/R₀)² < 10⁻⁶⁰
- Note the 5D perspective: the 5D theory is exactly reflection-positive;
  the problem is an artifact of the 4D Einstein-frame decomposition
- Compare to other approaches (the 10⁻⁶⁰ bound vs order-1 violation in
  standard 4D gravity)

---

### PRIORITY 5 — Paper 4, Appendix E: Spectral Gap Δ_{5D} > 0

**Source:** `etc/frontier-research/problem4-nonpert-completion.md`
**Target:** `paper4/appendix-E-spectral-gap.md`
**Claim:** Δ_{5D} ≥ √5/r₃ > 0 from Lichnerowicz bound on spin^c CP²

The appendix should:
- Define Δ_{5D} as the spectral gap of D_{M₇}
- Give the Lichnerowicz formula for spin^c CP² (D² ≥ R/4 + F_L/2)
- Compute: R_{CP²} = 24/r₃², worst-case F_L contribution = −1/r₃²
  → D² ≥ 5/r₃²
- State: no zero modes on M₇ (product structure blocks them)
- State: perturbative stability from Theorems K.1 + K.3
- State: non-perturbative stability from exp(−10³⁰) (cross-reference Appendix J)
- The OS3 connection: this gap feeds into the OS reconstruction
- Include the proof chain table (Steps 1–4 from the frontier file)

---

### PRIORITY 6 — Paper 7, Appendix B: Freed-Witten Tadpole

**Source:** `etc/frontier-research/oi2-freed-witten-tadpole.md`
**Target:** `paper7/appendix-B-freed-witten.md`
**Claim:** Exact unification ratio obstructed; minimal solution gives 0.31% deviation

The appendix should:
- State the precise FW shift: +1/2 on CP² cycle, 0 on CP¹×S² cycle
- Give the Diophantine obstruction (18n₂ + 34n₁_int = −17, gcd=2∤17)
- Identify the two minimal solutions (Section 4.1 of source)
- Compute: δ(ρ²)/ρ² = −0.65%, δ(α₃/α₂)/(α₃/α₂) ~ 0.7%
- State: within 2-loop threshold uncertainties, unification preserved
- Compute N_flux = −1007/8 for (19/2, −18) and note DMW correction needed
- Three-level summary (Section 7.1 of source)

---

### PRIORITY 7 — Paper 5, Appendix D §D.5: Boltzmann equations solved

**Already partially done** (updated in previous session). But check that:
- The Python code is included or referenced properly
- The numerical results table is complete (it is)
- The three key physics ingredients are stated clearly (they are)
- No reference to `etc/` remains in the appendix text (CHECK THIS)

---

### PRIORITY 8 — Paper 6: Missing appendices

Paper 6 has NO appendices. Identify which results in Paper 6 need
appendix backing and what would be sufficient. In particular:

**Dilaton freezing argument (ε_eff ~ 10⁻⁵²):**
Where is the derivation that the dilaton moves by 10⁻⁵² of its value
over a Hubble time? This is claimed in Paper 6 §3.1 and used in
Paper 3 App A §A.7 (OS3). The calculation appears in
`etc/frontier-research/oi3-reflection-positivity.md` §3.2.
It should be a Paper 6 Appendix A.

**Reheating mechanism:**
Paper 6 §4 describes reheating. Is there a computation? If the
reheating estimate is purely qualitative, state that explicitly in
the section. If there is a computation in etc/, convert it to an appendix.

---

## What to Produce

### Phase 1 output:
- `etc/36-audit-results.md` — complete audit table for all papers

### Phase 2 outputs (in priority order):
- `paper3/16-appendix-b-horizon-vertex.md`
- `paper4/appendix-D-higgs-naturalness.md`
- `paper7/appendix-A-theorem-U-star.md`
- Addition to `paper3/15-appendix-a-non-perturbative-completion.md` (§A.7)
  OR new `paper3/17-appendix-c-reflection-positivity.md`
- `paper4/appendix-E-spectral-gap.md`
- `paper7/appendix-B-freed-witten.md`
- Verify `paper5/appendices/appendix-D-resonant-leptogenesis.md` has no etc/ refs
- `paper6/appendix-A-dilaton-freezing.md`

### Format requirements for each appendix:
1. **No references to `etc/`** — the appendix must be self-contained
2. **Journal style** — written as a physics paper appendix, not as
   "investigation notes"
3. **Cross-references to other paper sections/appendices** are fine
   (e.g., "By Theorem K.1 (Paper 1, Appendix K §K.7b)...")
4. **Theorem statements** at the top of each appendix
5. **Proof chain table** for new theorems (in style of PROOF-CHAIN.md)
6. **Honest caveats** preserved — if something is "approximate" or has
   a remaining assumption, say so explicitly

---

## Files to Read Before Starting

**Frontier research files (sources):**
- `etc/frontier-research/problem1-cc-underivability.md` (Theorem U*)
- `etc/frontier-research/problem2-higgs-mass.md` (Higgs naturalness)
- `etc/frontier-research/problem3-horizon-vertex.md` (Theorem 9.1)
- `etc/frontier-research/problem4-nonpert-completion.md` (Lichnerowicz + OS3)
- `etc/frontier-research/oi1-boltzmann-equations.md` (η_B numerical)
- `etc/frontier-research/oi2-freed-witten-tadpole.md` (FW characterization)
- `etc/frontier-research/oi3-reflection-positivity.md` (OS3 to 10⁻⁶⁰)

**Existing paper sections that reference these:**
- `paper3/09-the-firewall-paradox-resolution-via-e-dimension-ge.md` §9.3
- `paper3/15-appendix-a-non-perturbative-completion.md`
- `paper4/06-the-higgs-mechanism-electroweak-symmetry-breaking-.md` §6.11
- `paper4/08-what-is-established-vs-what-is-conjectured.md`
- `paper5/appendices/appendix-D-resonant-leptogenesis.md`
- `paper7/03-moduli-minimum.md` §3.6 (Theorem U — already in paper)
- `paper7/04-tadpole.md` §4.4
- `paper7/06-conclusion.md`

**Models for appendix style:**
- `paper1/appendices/22-appendix-k-higher-loop-epstein.md` (Theorem K.1)
- `paper1/appendices/30-appendix-s-finiteness-theorem.md`
- `paper4/appendix-A-anomaly-cancellation.md`
- `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md` (proof chain format)

---

## Critical Rule

**No claim in any paper may say "proved" or "derived" if the derivation
is only in `etc/`. If the derivation is in `etc/`, either:**
1. The derivation is converted to a paper appendix (preferred), OR
2. The paper claim is reworded to say "argued" or "supported by calculation
   in [companion document]" with an honest caveat.

The papers are the permanent scientific record. The `etc/` files are
working notes that will not be published.

---

*This prompt was written April 5, 2026, after auditing 7 etc/frontier-research/
files that contain the complete derivations for claims made in Papers 3–7.
The audit revealed that these derivations exist but are not accessible to
readers of the published papers. This prompt closes that gap.*
