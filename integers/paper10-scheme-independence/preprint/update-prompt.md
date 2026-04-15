# Prompt — Update Paper 10 to Reflect Conditional Theorem Status

**Issued by:** G (principal investigator)  
**Date:** 2026-04-07  
**Output:** Edits to existing files in `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper10-scheme-independence/preprint/`

---

## Context

The three-graviton vertex computation (research memo
`/Users/gsix/quantum-geometry-in-5d-latex/integers/paper10-scheme-independence/research/01-three-graviton-vertex.md`)
has been completed. Conjecture 1 of Paper 10 is now conditionally proved.

**Read that memo in full before making any edits.**

Key results to incorporate:
1. `I_{+++}(n,n,n) = 0` for all n ≥ 1 — diagonal coupling vanishes exactly, algebraically
2. `I_{+++}(n₁, n₂, n₁+n₂) = πR/4` — triangle coupling is a universal constant,
   fully mass-independent, the geometric content of vertex mass-independence
3. C_GS = 0 assembled: leading [πR/4]² × J(0) × S₀² = 0; subleading E₂(−j;Q₂) = 0
4. Conjecture 1 is now **conditionally proved** subject to three assumptions:
   - A1: de Donder gauge vertex numerator has no n-dependent O(k²) terms beyond y-integrals
   - A2: h_{μ5} and φ fields don't contribute to leading GS counterterm  
   - A3: Internal loop momenta range over all of Z on S¹/Z₂
5. A1 is the binding constraint; A2 and A3 are standard orbifold results

---

## Files to update

### 1. `04-poisson-weyl.md`

Find Conjecture 1 and update it:
- Change label from "Conjecture 1" to "Theorem 1 (conditional on A1–A3)"
- Add the three assumptions A1, A2, A3 as clearly labelled sub-items
- Add the proof chain: I_{+++}(n₁,n₂,n₁+n₂) = πR/4 (universal) → coupling is
  n-independent → C_GS = [πR/4]² × J(0) × S₀² = 0 (leading) + subleading vanish by K.1
- Add a sentence: "The binding open item is A1; see §05 and research memo
  `integers/paper10-scheme-independence/research/02-de-donder-gauge-vertex.md` (in preparation)"
- Cross-reference: diagonal coupling I_{+++}(n,n,n) = 0 means self-loops are absent
  from the GS sunset topology; only triangle diagrams contribute

### 2. `05-open-problems.md`

Update the status table:
- Vertex mass-independence: change from "Open" to "Conditional (A1–A3)"
- Add a dedicated subsection §5.2a "Assumption A1: de Donder gauge vertex numerator"
  explaining what A1 requires, why it is the binding assumption, and that research
  memo `02-de-donder-gauge-vertex.md` is computing it
- Update A2 and A3 with brief notes that these are standard orbifold results
  (cite the relevant literature or Paper 1 sections)

### 3. `00-abstract.md`

Find the sentence about Conjecture 1 and update:
- "Conjecture 1" → "Theorem 1 (conditional)"
- Add: "subject to three explicit assumptions (A1–A3), of which A1 — the behavior of
  the de Donder gauge vertex numerator — is identified as the binding item and is the
  subject of ongoing computation"
- Keep the abstract honest: the paper does not fully close Conjecture 1, but it reduces
  it to a single explicit calculation

### 4. `01-introduction.md`

In the five-route verdict table or summary, update the vertex mass-independence row
to reflect the new status: "Conditional theorem (A1–A3); A1 in computation."

---

## Tone and constraints

- Do not oversell. The result is genuine progress but not a complete proof.
- Every theorem label must say "(conditional on A1–A3)" until A1 is closed.
- The phrase "Conjecture 1" should be replaced throughout with "Theorem 1 (conditional)"
  — search all four files for "Conjecture" and update each instance.
- Cross-reference `integers/paper10-scheme-independence/research/01-three-graviton-vertex.md` as the source.
- Do not modify `02-seeley-dewitt.md` or `03-z2-mechanism.md` — those are unaffected.

Use the Edit tool for all changes. Read each file before editing.
