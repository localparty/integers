# Prompt — Update Paper 10: Lemma A1 Proved, A2/A3 Remain Open

**Issued by:** G (principal investigator)  
**Date:** 2026-04-07  
**Output:** Edits to existing files in `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/`

---

## What was established

Read this memo in full before editing:
`/Users/gsix/quantum-geometry-in-5d-latex/paper10/research/02-de-donder-gauge-vertex.md`

**Lemma A1 is now proved.** Three independent mechanisms confirm it:

1. **UV power counting:** The 5D de Donder vertex decomposes as V = V^{(4D)} + V^{(∂_5,1)}
   + V^{(∂_5,2)} with UV scalings λ², λ·m_n, m_n² respectively. At leading UV order only
   V^{(4D)} survives — n-independent by construction.

2. **Z₂ parity (stronger than power counting alone):** The single-∂_5 terms V^{(∂_5,1)}
   — the least UV-suppressed of the ∂_5 class — are outright forbidden by the S¹/Z₂
   orbifold projection (parity product = −1). Only V^{(∂_5,2)} survives the parity filter,
   and those scale as m_n²/k² — two powers faster than needed.

3. **Epstein vanishing backstop:** All residual ∂_5 KK sums are proportional to
   E₂(−j; Q₂) = 0 for j ≥ 1 via 1/Γ(−j) = 0 (Theorem K.1). Even if mechanisms 1 and 2
   failed at some term, the KK sum kills it.

Numerical verification: V^{(∂_5)}/V^{(4D)} = 1/(k/m_n) to machine precision for
n = 1..20 and k/m_n ∈ {10, 100, 1000}. No exceptions found.

**Assumptions A2 and A3 remain open** and are proposed as the next computations.

---

## Files to update

### `04-poisson-weyl.md`

In the Theorem 1 (conditional) block and §4.6:
- Update A1's status from "binding open item" / "in computation" to **"Proved — Lemma A1"**
- Add Lemma A1 as a formally labelled lemma (before or as part of Theorem 1):
  > **Lemma A1.** In de Donder gauge, the 5D three-graviton vertex numerator, after KK
  > decomposition on S¹/Z₂, introduces no n-dependent terms at leading UV order. The ∂_5
  > contributions are either (i) forbidden by Z₂ parity projection, or (ii) O(m_n²/k²)
  > suppressed in the UV limit, or (iii) killed by Epstein vanishing (Theorem K.1).
  > *Proof:* See research memo `paper10/research/02-de-donder-gauge-vertex.md`.
- Update "binding open item is A1" → "A1 is closed (Lemma A1); binding open items
  are now A2 and A3"
- Update the cross-reference: `02-de-donder-gauge-vertex.md` is no longer "(in preparation)"
  — remove that parenthetical

### `05-open-problems.md`

- Status table: update A1 row to "**Proved** (Lemma A1; see research memo 02)"
- §5.2a: update to past tense — A1 has been computed; summarise the three mechanisms;
  note that A2 and A3 are now the remaining items
- Make A2 and A3 the new leading open problems, with their own subsections §5.2b and §5.2c:
  - **§5.2b — Assumption A2:** h_{μ5} and φ (radion/graviscalar) sectors. Do these
    contribute to the leading GS counterterm? The GS operator is built from R_{μνρσ}
    (purely 4D indices). In the 4D effective theory, h_{μ5} gives rise to graviphoton A_μ
    and φ gives rise to radion. Neither couples to R_{μνρσ}³ at tree level, but loop
    contributions are possible. State this as the open question; note it is likely
    closable by field content analysis.
  - **§5.2c — Assumption A3:** Internal loop momenta range over all of Z on S¹/Z₂.
    This is the statement that KK momentum is not restricted by the orbifold projection
    inside loops. In the path integral on S¹/Z₂, internal lines sum over both n ≥ 0
    (even sector) and n ≥ 1 (odd sector) with appropriate multiplicity. State this as
    the open question; note it is likely a standard orbifold path integral statement
    referencing Horava-Witten or Polchinski.

### `00-abstract.md`

- Update Lemma A1 status: "in computation" → "proved (three mechanisms: UV power
  counting, Z₂ parity projection, Epstein backstop)"
- Update the forward statement: "A1 is the binding item" → "A2 and A3 are the
  remaining items; both are proposed as closable by field content analysis and
  standard orbifold path integral arguments respectively"

### `01-introduction.md`

In the five-route verdict table / §1.3:
- Update vertex mass-independence status: "A1 in computation" →
  "A1 proved (Lemma A1); A2 and A3 proposed"

---

## Constraints

- Use the Edit tool; read each file before editing
- Do not modify `02-seeley-dewitt.md` or `03-z2-mechanism.md`
- Theorem 1 remains labelled "(conditional on A2–A3)" — not unconditional — until
  A2 and A3 are also closed
- Every edit should be precise and minimal — update only what changed, don't rewrite
  sections that don't need it
