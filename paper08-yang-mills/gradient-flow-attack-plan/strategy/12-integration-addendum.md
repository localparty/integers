# Integration Addendum: What's Left to Do

*Concrete task list for converting the gradient-flow proof memos*
*into the final preprint. Everything intellectual is done; what*
*remains is writing.*

*Date: 2026-04-08*
*Updated: 2026-04-08 (added parallelization analysis, Section 5)*

---

## 0. Current State

**Done:**
- 4 strategy documents (00, 02, 03, 04) — ~2,600 lines
- 17 research memos (W1-01 through W8-17) — 11,014 lines
- 5 computation scripts, 24 checks, all PASS at 50 digits
- Synthesis verification (W8-16): 19/19 lemmas VERIFIED, 0 circular
  dependencies, 0 new gaps, GO verdict
- Integration strategy report (11): methodology documented

**Not done:**
- Appendix L rewrite (conjectures → proofs)
- Appendix N (QG5D cross-references)
- PROOF-CHAIN Steps 15–18
- Abstract, conclusion, Section 5.7 IV.5 updates
- Computational verification appendix for gradient-flow numerics
- Final read-through and cross-reference audit


---


## 1. Task List

### Task 1: Rewrite Appendix L

**Input:** Current `L-clay-conjectures.md` (conjectures) + 17 research
memos (proofs).

**Output:** New `L-gradient-flow-construction.md` (~50 pages).

**Structure:**

```
L.0  Scope (rewritten: "proved" replacing "open")     [0.5 page]
L.1  Phase 1: Lattice gradient flow (Lemmas 1.1–1.5)  [5 pages]
L.2  Phase 2: Continuum limit at fixed t > 0           [4 pages]
     (Lemmas 2.1–2.4)
L.3  Phase 3: The t → 0 limit                          [10 pages]
     (Lemmas 3.1–3.9 — this is the core)
L.4  Phase 4: Stress tensor, AF match, OPE             [5 pages]
     (Lemmas 4.1–4.3)
L.5  Sub-clause resolution map                          [1 page]
L.6  Status and honest accounting                       [1 page]
L.7  Hypothesis H4: what it is and why it's mild        [2 pages]
```

**Conversion map from memos to sections:**

| Appendix L section | Source memos | What to do |
|:-------------------|:-------------|:-----------|
| L.1, Lemma 1.1 | W1-01 | Extract theorem + proof, drop strategy prose |
| L.1, Lemma 1.2 | W2-06 | Extract theorem + proof; tighten the maximum principle argument |
| L.1, Lemma 1.3 | W3-08, §§1–3 | Extract polymer decay bound |
| L.1, Lemma 1.4 | W3-08, §4 | K-uniformity paragraph |
| L.1, Lemma 1.5 | W1-02 | Contractivity — compact, mostly citations |
| L.2, Lemma 2.1 | W1-03 | Heat kernel factorization — citation of Paper 1 App. S |
| L.2, Lemma 2.2 | W4-09, §§1–3 | Cauchy estimate — main new content in Phase 2 |
| L.2, Lemma 2.3 | W4-09, §4 | Corollary (uniqueness) |
| L.2, Lemma 2.4 | W4-09, §5 | OS axiom transfer table |
| L.3, Lemma 3.1 | W1-05 | Analyticity in $t$ — the composition argument |
| L.3, Lemmas 3.2–3.6 | W1-04 | Five established lemmas — one paragraph each |
| L.3, Lemma 3.7 | W5-10, Part I | **The Cauchy estimate** — full 6-step proof |
| L.3, Lemma 3.8 | W5-10 Part II + W6-11 | Extraction + GNS reconstruction |
| L.3, Lemma 3.9 | W6-12 | KK → 4D Feshbach for operators |
| L.4, Lemma 4.1 | W7-13 | Stress tensor via Suzuki |
| L.4, Lemma 4.2 | W7-14 | AF match (conditional on H4) |
| L.4, Lemma 4.3 | W7-15 | OPE leading order |
| L.5 | W8-16, §2 | Sub-clause resolution table |
| L.6 | W8-16, §8 | Status + caveats |
| L.7 | W7-14, §5 + W8-16, §4.2 | H4 discussion |

**Effort:** ~3 days. The intellectual content exists; the work is
reformatting research prose into theorem/proof style, removing
strategy commentary, and adding consistent cross-references.

**Key decisions during conversion:**
- Keep each lemma as a formal Lemma/Theorem environment with
  numbered equations
- All QG5D citations go to Appendix N (not inline Paper 1/10 paths)
- H4-conditional results explicitly flagged with "(Conditional on
  Hypothesis H4)" in the theorem statement
- Computation scripts referenced but not inlined — point to
  `gradient-flow-attack-plan/code/`

---

### Task 2: Write Appendix N (QG5D Cross-References)

**Input:** Cross-reference tables from `00-formal-argument.md` §8 and
`W8-16-synthesis.md` §5.

**Output:** New `N-qg5d-infrastructure.md` (~5 pages).

**Structure:**

```
N.0  Purpose                                            [0.25 page]
N.1  From Paper 1                                       [1.5 pages]
     - Theorem K.1 (Epstein vanishing)
     - Theorem S.1 (perturbative finiteness)
     - S_0 = 1 + 2ζ(0) = 0
     - Heat kernel factorization (Appendix S)
     - Eisenstein lattice zeta (Appendix G)
     - Orbifold structure (Appendix W)
     - KK mass spectrum
N.2  From Paper 10                                      [1.5 pages]
     - Theorem 1 (C_GS = 0 all schemes)
     - Theorem U.2a (a_2 = a_4 = 0)
     - Proposition 3.1 (Z_2 cancellation)
     - Theorem 4.3 (Wess-Zumino protection)
     - Lemmas A1–A3
     - Poisson bridge (10^{-24} verification)
N.3  From Paper 6                                       [0.5 page]
     - Theorem F.1 (frozen dilaton)
N.4  From Paper 4                                       [0.5 page]
     - CP^2 × S^2 × S^1 geometry, r_3 scale
N.5  Note on the role of gravitational physics           [0.5 page]
     (Only spectral identities used; no gravitational
     dynamics enters the Yang-Mills proof)
```

**Effort:** ~1 day. Bookkeeping — extract theorem statements from
the QG5D papers, write one-paragraph context for each.

---

### Task 3: Update PROOF-CHAIN.md

**Input:** W8-16 §6 (Steps 15–18 draft).

**Output:** Add to `preprint/PROOF-CHAIN.md`:

```markdown
| 15 | Gradient-flow: well-posedness, contractivity,
|    | small-field preservation, K-uniform polymer decay
|    | | **Proved** (Lemmas 1.1–1.5) | Appendix L, §L.1 |
| 16 | Continuum flowed Schwinger functions: unique,
|    | OS0–OS4 at fixed t > 0
|    | | **Proved** (Lemmas 2.2–2.4) | Appendix L, §L.2 |
| 17 | [Tr F²]_R exists; T_μν constructed; L.1(i)(ii),
|    | L.3(i)–(v) closed
|    | | **Proved** (Lemmas 3.7–3.9, 4.1) | Appendix L, §§L.3–L.4 |
| 18 | AF match (L.2), leading OPE (L.4)
|    | | **Conditional** on H4 (Lemmas 4.2–4.3) | Appendix L, §L.4 |
```

Also update IV.5 to replace the current "does not address" language
with: "The four structural ingredients are established in Appendix L
(Steps 15–17 unconditional; Step 18 conditional on H4)."

**Effort:** 30 minutes.

---

### Task 4: Update Abstract

**Input:** W8-16 §7 (draft abstract paragraph).

**Output:** Add to `00-abstract.md`, after the current summary table:

> The four structural ingredients of the Jaffe–Witten problem
> statement — local field operators, short-distance match to
> asymptotic freedom, the stress-energy tensor, and a leading-order
> operator product expansion — are established in Appendix L via the
> Yang–Mills gradient flow on the KK background, using UV finiteness
> results from the Quantum Geometry in 5D framework (Papers 1 and
> 10). The AF match and the AF form of the OPE are conditional on
> the standard hypothesis H4 (non-perturbative Schwinger functions
> agree with perturbation theory at short distances). All other
> Clay requirements (C1–C11) are satisfied unconditionally.

**Effort:** 15 minutes.

---

### Task 5: Update Conclusion (Section 12)

**Input:** Compliance assessment.

**Output:** Add Section 12.7 to `08-conclusion.md`:

```markdown
## 12.7 Full Clay Compliance

The four structural ingredients required by Jaffe–Witten §4 beyond
the mass gap — local field operators (C6), AF matching (C7), stress
tensor (C8), and OPE (C9) — are established in Appendix L via the
gradient-flow construction.

| # | Requirement | Status | Location |
|:--|:------------|:-------|:---------|
| C1–C5 | Mass gap + axioms | **PASS** | Sections 4–5 |
| C6 | Local field operators | **PASS** | Appendix L, §L.3 |
| C7 | AF match | **PASS** (H4) | Appendix L, §L.4 |
| C8 | Stress tensor | **PASS** | Appendix L, §L.4 |
| C9 | OPE (leading order) | **PASS** (H4) | Appendix L, §L.4 |
| C10 | RP preserved | **PASS** | Appendix D |
| C11 | Volume-uniform gap | **PASS** | §5.7(e) |

The sole remaining hypothesis is H4 (non-perturbative = perturbative
at short distances), which enters only C7 and the AF form of C9.
The gradient-flow framework reduces H4 to a statement about Taylor
coefficients of a single analytic function — the mildest known
formulation.
```

Also update Section 12.6 ("Honest Bottom Line"): change the final
sentence from "The proof is complete" to "The proof is complete;
see Appendix L for the four Clay structural ingredients."

**Effort:** 30 minutes.

---

### Task 6: Update Section 5.7, IV.5

**Input:** Current text acknowledges L.1–L.4 as open.

**Output:** Replace with forward reference:

> The four further structural ingredients of the Jaffe–Witten problem
> statement (§4) are established in Appendix L via the gradient-flow
> construction: renormalized composite operators (L.1, unconditional),
> the stress-energy tensor (L.3, unconditional), short-distance AF
> matching (L.2, conditional on H4), and a leading-order OPE (L.4,
> conditional on H4 for the AF form). See PROOF-CHAIN Steps 15–18.

**Effort:** 15 minutes.

---

### Task 7: Computational Verification Appendix

**Input:** 5 scripts in `gradient-flow-attack-plan/code/`, 24 checks.

**Output:** Footnote in Appendix L:

> Numerical verifications (24 independent checks at 50-digit
> precision) are in `gradient-flow-attack-plan/code/`. All checks
> pass. See `W8-17-computation-audit.md` for the audit report.

**Effort:** 15 minutes.

---

### Task 8: Final Read-Through and Audit

**What to check:**

1. **Every lemma in Appendix L cites its hypotheses.** Walk the
   dependency chain 1.1 → 1.2 → ... → 4.3 and verify each arrow
   has an explicit "By Lemma X.Y" reference.

2. **Every QG5D citation in Appendix L points to Appendix N.** No
   raw file paths to `quantum-geometry-in-5d-latex/` in the
   publication text.

3. **H4-conditional results are consistently flagged.** Search for
   "L.2", "4.2", "4.3", "AF match", "AF form" and verify each
   occurrence says "conditional on H4."

4. **PROOF-CHAIN Steps 1–18 are consistent with the text.** Read
   the chain table and verify each "Proved" status matches the
   appendix section cited.

5. **The abstract, conclusion, and IV.5 are mutually consistent.**
   All three should say the same thing about what's proved and
   what's conditional.

6. **No stale references to "open conjectures."** Search for
   "open", "conjecture L.", "Tier 1B", "deferred" in the full
   preprint and verify they're all updated or removed.

7. **Cross-file constant consistency.** Run the sympy script from
   the referee's venv to verify constants ($m_1$, $b_0$, $\rho$,
   $r_t$, $C_{\mathrm{flow}}$) are consistent between the mass gap
   sections and Appendix L.

**Effort:** 1 full day.


---


## 2. Schedule (Original — Sequential)

| Day | Task | Output |
|:----|:-----|:-------|
| 1 | Task 2 (Appendix N) | `N-qg5d-infrastructure.md` |
| 2–4 | Task 1 (Appendix L), Phases 1–2 | L.0–L.2 draft |
| 5–6 | Task 1 (Appendix L), Phase 3 | L.3 draft (the core — Lemma 3.7) |
| 7 | Task 1 (Appendix L), Phase 4 + L.5–L.7 | L.4–L.7 draft |
| 8 | Tasks 3–7 (PROOF-CHAIN, abstract, conclusion, IV.5, numerics) | All preprint updates |
| 9 | Task 8 (full read-through and audit) | Audit report |
| 10 | Buffer / revisions from audit | Final version |

**Total: 10 working days.** Conservative estimate.


---


## 3. What NOT to Do

1. **Don't rewrite the research memos.** They are research records,
   not publication drafts. The publication text (Appendix L) is a
   separate document that extracts the mathematical content and
   reformats it. The memos stay as-is for the audit trail.

2. **Don't merge Appendix L into the main text.** The mass gap proof
   (Sections 1–5) should remain self-contained. Appendix L is
   logically downstream — it uses the mass gap as input. A reader
   who cares only about $\Delta_\infty > 0$ should not need to read
   Appendix L.

3. **Don't try to close H4.** It's the standard hypothesis of
   lattice QCD, open for 50 years. The gradient-flow framework makes
   it more tractable than any previous formulation, but proving it
   is a separate research programme. State it honestly and move on.

4. **Don't add new results.** The 19 lemmas are the complete set.
   If the read-through reveals a missing step, it should be a
   sub-lemma within an existing lemma, not a new lemma.

5. **Don't change the notation.** The preprint uses $g_k$,
   $\hat{\Delta}_k$, $C_K$, etc. Appendix L should use the same
   symbols. The gradient-flow-specific notation ($F(t)$, $E(t,x)$,
   $c_1(t)$, $r_t$) is introduced in Appendix L and does not
   conflict.


---


## 4. Definition of Done

The preprint is complete when:

- [ ] Appendix L exists with 19 lemmas in theorem/proof form
- [ ] Appendix N exists with all QG5D cross-references
- [ ] PROOF-CHAIN has Steps 15–18
- [ ] Abstract mentions L.1–L.4 closure and H4 caveat
- [ ] Conclusion has Section 12.7 (Full Clay Compliance)
- [ ] Section 5.7 IV.5 updated
- [ ] No stale "open conjecture" language anywhere in the preprint
- [ ] All H4-conditional results consistently flagged
- [ ] Computational scripts referenced
- [ ] Full read-through audit completed with no issues
- [ ] Constants cross-checked by sympy/mpmath

When all boxes are checked, the preprint is a complete Clay
Millennium Prize submission.


---


## 5. Parallelization Analysis (Added 2026-04-08)

The 8 tasks decompose into 3 parallel groups + 1 sequential final step.

### Dependency map

```
Task 1 (Appendix L)  ─┐
  ├─ L.1 (Phase 1)    │
  ├─ L.2 (Phase 2)    │  All independent of
  ├─ L.3 (Phase 3)    ├─ each other during
  ├─ L.4 (Phase 4)    │  writing
  ├─ L.0, L.5-L.7     │
                       │
Task 2 (Appendix N)  ─┤  Independent
                       │
Tasks 3-7 (updates)  ─┤  Independent, quick
                       │
                       ▼
Task 8 (final audit) ─── Depends on ALL above
```

### Wave 9 — Appendix L + N (7 agents, parallel)

Task 1 splits naturally by phase. Each sub-section draws from
different source memos with no cross-dependencies during writing.
Task 2 is fully independent.

| Slot | Agent | Source memos | Output | Est. time |
|:-----|:------|:-------------|:-------|:----------|
| W9-18 | L.0 + L.5 + L.6 + L.7 | W8-16, W7-14 | Scope, sub-clause map, status, H4 | 20 min |
| W9-19 | L.1 (Phase 1 lemmas) | W1-01, W1-02, W2-06, W3-08 | Lemmas 1.1–1.5 in theorem/proof form | 30 min |
| W9-20 | L.2 (Phase 2 lemmas) | W1-03, W4-09 | Lemmas 2.1–2.4 in theorem/proof form | 25 min |
| W9-21 | L.3 (Phase 3 lemmas) | W1-04, W1-05, W5-10, W6-11, W6-12 | Lemmas 3.1–3.9 — **THE CORE** | 45 min |
| W9-22 | L.4 (Phase 4 lemmas) | W7-13, W7-14, W7-15 | Lemmas 4.1–4.3 in theorem/proof form | 25 min |
| W9-23 | Appendix N | Strategy docs, QG5D papers | QG5D cross-reference appendix | 30 min |
| W9-24 | Preprint updates | W8-16, preprint sections | PROOF-CHAIN + abstract + conclusion + IV.5 + footnote | 20 min |

**7 agents, all parallel.** W9-21 (Phase 3 / L.3) is the longest —
it contains the core estimate (Lemma 3.7) and the extraction chain.

### Wave 10 — Assembly + Final Audit (1 agent, sequential)

| Slot | Agent | Task | Depends on | Est. time |
|:-----|:------|:-----|:-----------|:----------|
| W10-25 | Final read-through | Task 8: walk the chain, check H4 flags, verify constants, no stale language | All of Wave 9 | 40 min |

### Revised timeline with parallelism

```
Wave 9   ████████████████████████████  7 agents parallel  ~45 min wall-clock
Wave 10  ████████████                  1 agent sequential  ~40 min wall-clock
                                                          ─────────────────
                                                          ~85 min total
```

**Comparison:** Sequential schedule = 10 working days.
Parallel with agents = **~85 minutes wall-clock**.

### Quality gate after Wave 9

Before launching Wave 10, verify:
- All 7 outputs exist and are non-empty
- L.1–L.4 sections each contain all claimed lemmas
- Appendix N references match Appendix L citations
- Preprint updates are consistent with each other

### What Wave 9 agents must follow

**Style rules (from Section 3 above):**
1. Theorem/proof environments, numbered equations
2. QG5D citations point to "Appendix N, §N.x" not file paths
3. H4-conditional results flagged in theorem statements
4. Same notation as preprint ($g_k$, $\hat{\Delta}_k$, etc.)
5. No strategy prose — extract only the mathematical content
6. Each lemma: Statement → Proof → □
