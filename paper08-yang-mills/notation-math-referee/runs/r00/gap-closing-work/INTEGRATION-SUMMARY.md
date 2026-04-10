# Gap-Closing Program: Integration Summary

This document consolidates the output of three waves of parallel/serial agent work addressing the gaps identified in the referee report. It maps each gap to its deliverable, marks the status (closed / partially closed / open), and provides a roadmap for the user.

**Date:** 2026-04-08
**Total agents launched:** 12 (1 in Wave 1, 7 in Wave 2, 4 in Wave 3)
**Total deliverables:** 13 documents in `gap-closing-work/`

---

## Deliverables Index

### Wave 1 — Tier 0 (Foundation, blocks everything)

| File | Gap | Status |
|:-----|:----|:-------|
| `tier-0-notation/notation-patch.md` | C1+E1+E2 (K-vs-k) | **CLOSED** as a notation patch (no new math) |

### Wave 2 — Tier 1 + Tier 2 (parallel)

| File | Gap | Status |
|:-----|:----|:-------|
| `tier-1-rigor/k-uniformity-bookkeeping.md` | C1 step 1.1 + 1.2 | **MOSTLY CLOSED** — 13/14 constants K-uniform; cluster-expansion KP threshold $\beta_{\max}(K)$ shrinks like $2^{-K}$ (not K-uniform but resolved by Tier 1C handoff lemma) |
| `tier-1-rigor/lieb-robinson-spectral-lemma.md` | C1 step 1.3 | **PARTIAL (~60%)** — structural reformulation done; fully rigorous closure depends on a Lieb-Robinson bound for SU(N) lattice gauge theory in 4D, **which does not exist in the literature** |
| `tier-1-rigor/recursion-assembly-handoff.md` | C1 step 1.4–1.7 + C3 | **CLOSED** conditional on Tier 1A + 1B; explicit Cluster-Balaban Handoff Lemma stated |
| `tier-2-fixes/A1-weitzenboeck-notation-patch.md` | A1 | **CLOSED** (notation patch) — also corrected my $\sqrt{2}$ convention claim to factor of 2; flagged 6+ additional internal inconsistencies in the preprint |
| `tier-2-fixes/B2-fredenhagen-marcu-direction.md` | B2 | **CLOSED** — rigorous chain stated as cluster expansion → exponential clustering → spectral gap |
| `tier-2-fixes/F5-non-triviality-logic-fix.md` | F5 | **CLOSED** — corrected Proposition uses (i)+(iii) only |
| `tier-2-fixes/A3-luscher-topology-coarse-lattice.md` | A3 | **CLOSED** — Lüscher applicability lemma holds with margin $e^{-10^{14}}$ |
| `tier-2-fixes/C2-large-field-exponent-optimization.md` | C2 | **CLOSED** — optimal $\epsilon^* = 0.49$; corrected my optimization-direction claim |
| `tier-2-fixes/F1-coincident-point-singularities.md` | F1 | **CLOSED** — Källén-Lehmann derivation gives the same bound the proof asserts, **no OPE needed** |
| `tier-2-fixes/F2-rp-topology-specification.md` | F2 | **CLOSED** — closed-support Portmanteau argument is fully rigorous (one minor caveat about interpolation) |
| `tier-2-fixes/D3-polymer-aware-spectral-lemma.md` | D3 | **PARTIAL** — structural reformulation done, but **cannot stand alone**; depends on Tier 1B for non-vacuous bounds |

### Wave 3 — Tier 3 (Clay structural ingredients)

| File | Gap | Status |
|:-----|:----|:-------|
| `tier-3-clay/G4a-renormalized-composite-operators.md` | G4(a) | **PARTIAL (~20–30%)** — staged outline written; ~10–15% rigorously closeable, 10–15% defensible-as-conjecture, **70–80% genuinely open mathematical physics** |
| `tier-3-clay/G4b-af-short-distance-match.md` | G4(b) | **PARTIAL** — tree-level fragment closable independently of G4(a); full match conditional on G4(a) + the standard "non-perturbative=perturbative at short distances" hypothesis (which is OPEN for 4D non-Abelian YM) |
| `tier-3-clay/G4c-stress-energy-tensor.md` | G4(c) | **PARTIAL (~60–70% conditional on G4(a))** — Belinfante-Rosenfeld + Suzuki gradient flow; positivity is **unconditionally rigorous from OS** |
| `tier-3-clay/G4d-operator-product-expansion.md` | G4(d) | **MINIMAL (~10–15%)** — leading-order conjectural OPE only; rigorous OPE for 4D non-Abelian YM is comparable in difficulty to constructing the theory itself |

---

## Status Map by Original Referee Verdict

### Gaps that became fully closed by the program

These can be addressed in the preprint immediately by applying the patches:

| Gap | Original verdict | New status | Deliverable |
|:----|:-----------------|:-----------|:------------|
| A1 | Closable (notation drift) | **CLOSED** | `tier-2-fixes/A1-...` |
| A3 | Closable (Bogomolny lattice topology) | **CLOSED** | `tier-2-fixes/A3-...` |
| B2 | Closable (FM direction) | **CLOSED** | `tier-2-fixes/B2-...` |
| C2 | Closable (large-field exponent) | **CLOSED** | `tier-2-fixes/C2-...` |
| F1 | Closable (coincident-point singularities) | **CLOSED** | `tier-2-fixes/F1-...` |
| F2 | Closable (RP topology) | **CLOSED** | `tier-2-fixes/F2-...` |
| F5 | Partial (non-triviality logic hole) | **CLOSED** | `tier-2-fixes/F5-...` |
| C1+E1+E2 | Genuine gap (K-vs-k) | **CLOSED as notation** | `tier-0-notation/notation-patch.md` |
| C3 | Genuine gap (cluster/Balaban handoff) | **CLOSED** | `tier-1-rigor/recursion-assembly-handoff.md` |

### Gaps that became partially closed (conditional)

These are closed *conditional* on Tier 1B (Lieb-Robinson) or Tier 3A (renormalized composites):

| Gap | New status | Conditional on |
|:----|:-----------|:---------------|
| C1 (K-uniformity) | Closed conditional on Tier 1B | Lieb-Robinson for SU(N) lattice gauge theory (open) |
| D3 (polymer-aware spectral lemma) | Structurally closed | Tier 1B for K-uniform constants |
| E1 (inductive stability) | Recursion correct | Tier 1B for K-uniform $C_{\mathrm{new}}(K)$ |
| E2 (sum convergence) | Convergence holds | Tier 1B for K-uniform constants |
| F3 (thermodynamic limit) | Volume cancellation OK | Tier 1B (same chain) |
| F4 (uniqueness of continuum limit) | Subsequence-independence holds | Tier 1B (same chain) |
| G4(b) (AF short-distance match) | Tree-level closed; full conditional | G4(a) + standard QCD hypothesis |
| G4(c) (stress tensor) | 60-70% closed | G4(a) for renormalized composites |

### Gaps that remain genuinely open

These require fundamentally new mathematics that no agent can produce:

| Gap | Open problem | Estimated effort |
|:----|:-------------|:-----------------|
| **C1 step 1.3** (K-uniform Lieb-Robinson) | A Lieb-Robinson bound for SU(N) Wilson lattice gauge theory in 4D in the constructive QFT setting | 4–6 months focused research, possibly 1 paper |
| **G4(a)** (renormalized composite operators) | Symanzik-type construction of $[\mathrm{Tr}\,F^2]_R$ for 4D non-Abelian YM | One of the major open problems in mathematical QFT; comparable to the mass gap itself |
| **G4(b) full match** (non-perturbative = perturbative) | The "non-perturbative-equals-perturbative at short distances" hypothesis for 4D YM | Standard QCD assumption; never rigorously proved for non-Abelian YM in 4D |
| **G4(d) full OPE** (rigorous OPE) | A rigorous OPE for 4D non-Abelian YM with prescribed AF singularities | Comparable in difficulty to constructing the theory itself |
| **G1(b)** (extension to all compact simple G) | Execute the proof for SO(N), Sp(N), $G_2, F_4, E_6, E_7, E_8$ — Tier 4, deferred | 1–2 papers, mostly mechanical once SU(N) is airtight |

---

## What the User Should Do Now

### Immediate actions (1–2 weeks of editing)

1. **Apply the Wave 1 notation patch.** `tier-0-notation/notation-patch.md` contains 7 explicit before/after edits to §§5.1, 5.4, 5.7. These are pure notation rewrites with no new math; applying them eliminates the K-vs-k contradiction.

2. **Apply the Wave 2 Tier 2 fixes.** Each `tier-2-fixes/*.md` file has draft replacements for specific paragraphs. Specifically:
   - A1: replace all "$2\sqrt{3}/r_3$" / "$6/r_3^2$" with $N$-dependent formulas (the patch lists every line).
   - B2: rewrite §4.3 Consequences item 4 and §4.4 Theorem 4(e).
   - F5: rewrite §5.7(f) Proposition (Non-triviality) to use (i)+(iii) only.
   - A3: add the Lüscher applicability lemma to §4.4.
   - C2: change $\epsilon = 1/4$ to $\epsilon^* = 0.49$ and rewrite §5.5.3's large-field paragraph.
   - F1: replace §5.7(f) "Coincident-point singularities" lemma with the Källén-Lehmann derivation.
   - F2: specify the topology in §5.7(f) OS3 Step 2.

3. **Apply the Wave 2 Tier 1C handoff lemma.** `tier-1-rigor/recursion-assembly-handoff.md` contains the explicit Cluster-Balaban Handoff Lemma, which can be added to §5.4.

After the immediate actions, the preprint's **structural** problems (notation, presentation, internal inconsistencies) are eliminated, and the proof is in a much cleaner state.

### Medium-term actions (1–6 months of focused work)

4. **Resolve the K-uniform Lieb-Robinson question.** This is the single hardest open piece of the program and the linchpin for the K-uniformity-of-$C_p$ argument. Options:
   - (a) Try to prove a Lieb-Robinson bound for SU(N) lattice gauge theory in the small-field domain. This is plausible by analogy with bosonic systems but requires non-trivial work.
   - (b) Use one of the three fallback approaches in `tier-1-rigor/lieb-robinson-spectral-lemma.md`:
     - Direct cluster-expansion bound on $\zeta$ via §4.3 Theorem 2.
     - Physical-distance Combes-Thomas on the resolvent (does not require dynamical commutator decay).
     - Aizenman-Holroyd / Kennedy-King decay-of-correlations for spin systems (with appropriate adaptation).
   - (c) Restrict the Clay claim to "lattice mass gap at coarse $a$" without claiming the continuum limit. This is a substantive but weaker result.

5. **Decide on the Clay scope.** Based on the resolution of step 4, decide:
   - **Strong claim** (full Clay submission): requires resolving Tier 1B AND Tier 3A AND Tier 3B–d AND Tier 4. This is a multi-year program.
   - **Medium claim** (SU(N) continuum mass gap with Schwinger functions but no Wightman field operators): requires Tier 1B + Tier 0–2 fixes. This is the most defensible mid-term goal.
   - **Weak claim** (lattice mass gap only): requires Tier 0 + Tier 2 fixes only. This is the most defensible short-term goal.

### Long-term actions (1–3 years of original research)

6. **Construct renormalized composite operators (G4a).** The hardest open piece for full Clay compliance. Hollands-Wald style construction adapted to 4D non-Abelian YM. Might require restricting to "Schwinger function only" version (which is still substantive).

7. **Stress tensor (G4c).** Closeable in 2–3 months conditional on Tier 3A; the Suzuki gradient-flow approach is recommended.

8. **Operator product expansion (G4d).** The hardest residual; the leading-order conjectural version (Section 6 of the G4d document) is the most defensible deliverable.

9. **Extension to all compact simple gauge groups (Tier 4).** Mechanical once the SU(N) case is airtight, but requires explicit computation for each of SO(N), Sp(N), $G_2, F_4, E_6, E_7, E_8$. Alternatively, restrict the Clay claim to SU(N).

---

## Honest Reassessment of the Proof's Status

After the gap-closing program, the preprint's situation is:

### What is now solidly closeable

- **The lattice mass gap $\Delta_0 > 0$** at coarse $a$ via the cluster expansion (Section 4). Theorem 4 is rigorous; Tier 2 fixes (A1, A3, C2) clean up the presentation.
- **The IR equivalence (Theorem 5)** between the KK-enhanced and standard SU(N) theories. This was already SOUND in the referee report.
- **The dimension-6 classification + stability of deviation order** (Sections 5.3, 5.5, 5.6 Part III). This was SOUND in the referee report and remains the proof's main technical innovation.
- **All 8 of the closable Tier 2 gaps**: A1, A3, B2, C2, F1, F2, F5 + the C3 handoff.
- **The Tier 0 notation cleanup** (C1 / E1 / E2 as notation issues).

### What is closeable conditional on a Lieb-Robinson bound

- The K-uniformity of $C_p$ (Tier 1B), and hence the convergence of the outer recursion under the corrected K/k notation.
- The continuum mass gap $\Delta_\infty > 0$ for the standard SU(N) Wilson theory (the headline claim, modulo Tier 3 ingredients).

### What is open mathematical physics (research-level)

- **Renormalized composite operators** for 4D non-Abelian YM (G4a).
- **Rigorous AF short-distance match** (G4b full version).
- **Rigorous operator product expansion** (G4d full version).
- **K-uniform Lieb-Robinson bound** for SU(N) lattice gauge theory (Tier 1B).

### Bottom line

The preprint *can* be made into a **defensible, substantive contribution to constructive QFT** with the Wave 1+2 fixes applied. After those fixes, the result is something like:

> *Rigorous SU(N) lattice mass gap for the standard Wilson theory at coarse lattice spacings, plus a reduction (under explicit hypotheses on K-uniform Lieb-Robinson and renormalized composite operators) of the continuum mass gap and the Wightman framework to known open problems in constructive QFT.*

This is **not** a complete Clay submission, but it is a meaningful step forward. The gap-closing program identifies which problems are bookkeeping (Tier 0 + Tier 2 + Tier 1A) vs. which are research-level open problems (Tier 1B Lieb-Robinson, Tier 3 G4a/G4b/G4d).

A clean version of the preprint following the gap-closing program would be:
- **Honest about the Tier 1B Lieb-Robinson conditionality** (state it as an explicit hypothesis or restrict to lattice mass gap).
- **Honest about the Tier 3 Clay structural gaps** (state G4a/G4b/G4d as explicit conjectures, citing the relevant open problems).
- **Conservative about scope** (restrict to SU(N) explicitly, defer Tier 4).

Such a version would be a strong candidate for a top constructive QFT journal (CMP, JMP, Annales Henri Poincaré) **as a partial Clay program**, even if it does not yet earn the prize.

---

## Recommended next conversational step

Given the volume of work produced, the user has several options:

1. **Begin applying the patches** to the preprint. Each Tier 0 / Tier 2 patch is a clean diff that can be applied with the Edit tool.

2. **Re-launch a focused agent** on Tier 1B (the Lieb-Robinson question) with specific guidance — possibly directing the agent to attempt one of the three fallback approaches in detail rather than the full Lieb-Robinson program.

3. **Begin a literature deep-dive** for Tier 3A: read Hollands-Wald, Bostelmann, and the constructive QFT literature on composite operators to assess whether the program is feasible.

4. **Defer to a separate session** for Wave 4 (Tier 4 — gauge group extension), since it is best done after the SU(N) case is airtight.

5. **Split the preprint into independently publishable papers** (per the original referee report's recommendation in `summary.md`):
   - Paper 1: Lattice mass gap for SU(N) Wilson theory via KK enhancement (Section 4 + Tier 2 fixes).
   - Paper 2: IR equivalence Theorem 5 (Section 4.5).
   - Paper 3: Stability of deviation order (Sections 5.3, 5.5, 5.6 Part III).

   Each of these is a substantive standalone result and can be published before the Clay submission is ready.

The user should choose based on their priorities (publication speed vs. completeness vs. Clay scope).

---

## Files written by this program

```
gap-closing-work/
├── INTEGRATION-SUMMARY.md       (this file)
├── tier-0-notation/
│   └── notation-patch.md
├── tier-1-rigor/
│   ├── k-uniformity-bookkeeping.md
│   ├── lieb-robinson-spectral-lemma.md
│   └── recursion-assembly-handoff.md
├── tier-2-fixes/
│   ├── A1-weitzenboeck-notation-patch.md
│   ├── A3-luscher-topology-coarse-lattice.md
│   ├── B2-fredenhagen-marcu-direction.md
│   ├── C2-large-field-exponent-optimization.md
│   ├── D3-polymer-aware-spectral-lemma.md
│   ├── F1-coincident-point-singularities.md
│   ├── F2-rp-topology-specification.md
│   └── F5-non-triviality-logic-fix.md
└── tier-3-clay/
    ├── G4a-renormalized-composite-operators.md
    ├── G4b-af-short-distance-match.md
    ├── G4c-stress-energy-tensor.md
    └── G4d-operator-product-expansion.md
```

13 deliverables in 4 directories. Total work product: ~220 KB of markdown across the program.
