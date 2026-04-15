# L7-collapse — Editorial Repair Node

**Node kind:** editorial (chain-structure change; no new mathematics)
**Wave:** 2
**Author:** Claude Sonnet 4.6, 2026-04-13
**Input:** `critiques/link-07-critic.md` (BROKEN), `chain/chain-state.md` Wave 1 record
**File-owner:** this file only. PROOF-CHAIN edits are proposals; do NOT modify the preprint.

---

## Direction

Link 7 ("Newton decomposition: n ≥ 2 survives") is a ghost link — no proof body exists anywhere in the preprint, and the sole extended treatment of Newton decomposition (Appendix G) explicitly repudiates it as a mechanism for extracting Δ̂ factors. The logical content it purports to carry is already fully delivered by Link 6 (𝒞-elimination of cubic operators) and Links 8-9 (spectral dev ≥ 2 classification). The repair is structural collapse: remove the standalone Link 7 row from PROOF-CHAIN.md §IV.1 and from the §5.5.5 summary table; insert a one-sentence attribution note after the Link 6 row; renumber downstream links.

**Renumbering decision: YES — renumber.** See §Renumbering decision below.

---

## Research — 6-step compressed loop

**Step 1 — Diagnose (ghost link confirmed).**
Link 7 appears only in three locations across the entire preprint:
- `PROOF-CHAIN.md §IV.1` line 17 (the chain table, "Newton decomposition: n ≥ 2 survives / Proved (exact) / Algebraic identity")
- `preprint/sections/05-continuum-limit.md` §5.5.5 line 1561 (the status table: "Newton decomposition: only n ≥ 2 survives / Proved (exact) / Algebraic identity")
- `preprint/sections/05-continuum-limit.md` §5.6 Part IV §IV.1 line 1913 (duplicated chain table inside section 5)
- `preprint/sections/I3-N-dependence-tracking.md` lines 382-386 (Step 7 gloss: three sentences invoking Newton identities for power sums)

No proof, no lemma statement, no derivation appears anywhere. The I3 gloss is itself misleading: it describes Newton identities as establishing that Tr(F³) vanishes by C-symmetry — which is exactly what Link 6 (C-elimination) already proves directly and rigorously.

**Step 2 — Unify (logical content already in L6 + L8-9).**
- *What Link 7 claims to do:* Eliminate n = 1 derivative-order terms via an algebraic Newton decomposition identity, leaving only n ≥ 2.
- *What actually does that work:*
  - **n = 0 (Tr(F³) cubic operators):** Eliminated by Link 6 (𝒞-elimination, §5.3.1, proved exact). Independently: Appendix G §6.2 explicitly confirms C-symmetry elimination is "valid and exact."
  - **n ≥ 2 lower bound:** Established by Link 8 (dev(Tr(DF)²) ≥ 2, §5.5.4, spectral mechanism) + Link 9 (Dim-6 classification, §5.6 Part III.3, all operators dev ≥ 2). These use the spectral intermediate-state mechanism, not Newton decomposition.
- The logical step "only n ≥ 2 survives" is the conjunction of Link 6 (nothing with n < 2 in the C-even sector) and Links 8-9 (everything that does survive has dev ≥ 2). Link 7 adds nothing.

**Step 3 — Lock (Appendix G confirms).**
Appendix G (`preprint/sections/G-multi-time-slice-analysis.md`) is a preprint-internal self-audit. Key verbatim findings:

> §3.4: "If all derivative terms vanish and M^{(0)} = 0 by C-symmetry, we get ⟨1|δE_k^{d=6}(0)|1⟩_c = 0 — too strong. This means the Newton decomposition is the wrong tool for extracting Δ̂ factors."

> §7.3: "Conjecture 1 at d_O = 6 stands, but the derivation of Mechanism 2 requires correction. The Newton decomposition is valid as dimension counting. The Δ̂² suppression comes from the spectral gap in the intermediate-state sum of the composite operator, not from lattice forward differences acting on the external state."

> §6.2: "Mechanism 2 must be replaced... The Newton decomposition is valid as dimension-counting. Correctly identifies derivative content. Does not directly produce Δ̂ factors."

Appendix G makes three specific concessions about what Newton decomposition is still good for (it is valid as dimension-counting; it correctly identifies that the n = 0 term is killed by C-parity; the operator norm bounds in Steps 5-7 are algebraic and remain valid). None of these constitute a standalone link in the proof chain. They are subservient commentary absorbed into Link 6 and Links 8-9.

**Step 4 — Compute (count links after removal).**
Current chain: 1, 1b, 2, 3, 4, 5, 6, **7**, 8, 9, 10, 10b, 11, 12, 13, 14, 15, 16, 17, 18.
After collapse: 1, 1b, 2, 3, 4, 5, 6, [note], 7, 8, 9, 10, 10b, 11, 12, 13, 14, 15, 16, 17.
Result: 17 numbered links + Link 18 (CONDITIONAL). Same count as required (one BROKEN link removed; chain remains 17 proved + 1 conditional).

**Step 5 — Verify (dependency check).**
Every Critic file in `chain-verification/critiques/` was checked for upstream citations of Link 7:

| Link | Cites L7? | Evidence |
|:-----|:----------|:---------|
| 8 | No | `link-08-critic.md`: five attack vectors, all purely spectral; no reference to Newton decomposition or L7 |
| 9 | No | `link-09-critic.md`: six attack vectors; C-parity argument, Appendix J classification; no L7 dependency |
| 10–18 | No | Grep across all `critiques/link-*.md`: the pattern "Link 7|L7|Newton decomp|Step 7" returns only `link-07-critic.md` and `chain-state.md` |

The I3 Step 7 gloss (lines 382-386) is commentary, not a logical dependency: Step 10 in I3 explicitly says it "Follows from (B1)-(B2) and Step 9" — no Step 7 upstream. **Zero downstream links cite L7 as an upstream dependency.**

**Step 6 — Integrity check.**
Appendix G §6.2 notes three things that Newton decomposition is still valid for:
1. Dimension counting (valid; absorbed by Link 9 / Appendix J classification)
2. Identifying that n = 0 Tr(F³) is killed by C-parity (valid; absorbed by Link 6)
3. Operator norm bounds Steps 5-7 (valid algebraically; absorbed into Link 11 source)

None of these requires a standalone link. All are either already attributed or are supporting commentary. The one-sentence note (§Chain-edit proposal below) preserves this context for a referee.

---

## Chain-edit proposal

### A. PROOF-CHAIN.md §IV.1 — verbatim from/to

**LOCATION:** The table in `preprint/PROOF-CHAIN.md §IV.1`, rows 6 and 7.

**FROM (lines 16-18 of PROOF-CHAIN.md):**
```
| 6 | $\mathcal{C}$-elimination of $\mathrm{Tr}(F^3)$ | **Proved** (exact) | Section 5.3.1 |
| 7 | Newton decomposition: $n \geq 2$ survives | **Proved** (exact) | Section 5.3.1, Newton decomposition |
| 8 | $\mathrm{dev}(\mathrm{Tr}(DF)^2) \geq 2$ | **Proved** | Section 5.5.4 |
```

**TO (with renumbering and attribution note):**
```
| 6 | $\mathcal{C}$-elimination of $\mathrm{Tr}(F^3)$ | **Proved** (exact) | Section 5.3.1 |
| *[note]* | *The $n \geq 2$ survival previously labeled "Newton decomposition" is accomplished by L6 ($\mathcal{C}$-elimination) $+$ L7--8 below (spectral dev $\geq 2$ classification); see Appendix G for why Newton decomposition is not the mechanism.* | — | — |
| 7 | $\mathrm{dev}(\mathrm{Tr}(DF)^2) \geq 2$ | **Proved** | Section 5.5.4 |
```

Continue renumbering: old-L9 → new-L8, old-L10 → new-L9, old-L10b → new-L10, old-L11 → new-L11 (no change on 10b→10 shifts the numbering), etc. Full renumbered table is in §Renumbering decision.

### B. §5.5.5 Status Table — verbatim from/to

**LOCATION:** `preprint/sections/05-continuum-limit.md` §5.5.5, line 1561.

**FROM:**
```
| Newton decomposition: only $n \geq 2$ survives | **Proved** (exact) | Algebraic identity |
```

**TO:**
```
| $n \geq 2$ survival (via $\mathcal{C}$-elimination $+$ spectral dev $\geq 2$; see Appendix G) | **Proved** (see L6, L7--8 chain) | $\mathcal{C}$-symmetry $+$ spectral gap |
```

### C. §5.6 Part IV §IV.1 (in-section duplicate) — verbatim from/to

**LOCATION:** `preprint/sections/05-continuum-limit.md` line 1913 (the duplicate chain table inside §5.6).

**FROM:**
```
| 7 | Newton decomposition: $n \geq 2$ survives | **Proved** (exact) | Algebraic identity |
```

**TO:** Remove this row entirely. (This in-section table is a compact summary; no note row required; the main PROOF-CHAIN.md carries the explanation.)

Continue renumbering in this duplicate table: old rows 8-14 become 7-13.

### D. I3-N-dependence-tracking.md Step 7 gloss — verbatim from/to

**LOCATION:** `preprint/sections/I3-N-dependence-tracking.md` lines 382-386.

**FROM:**
```
**Step 7: Newton decomposition: $n \geq 2$ survives.**
The Newton identities relating power sums to elementary symmetric
polynomials hold for all $N$. For $\mathrm{SU}(N)$, the trace
$\mathrm{Tr}(F^3)$ vanishes by $\mathcal{C}$-symmetry for all $N$.
The decomposition is algebraic and $N$-independent.
```

**TO:** Merge into Step 6 as a supplementary sentence, and renumber Step 8 → Step 7, etc.:
```
**Step 6: $\mathcal{C}$-elimination of $\mathrm{Tr}(F^3)$.**
Charge conjugation symmetry is a property of the $\mathrm{SU}(N)$
action for all $N$. The elimination is exact and $N$-independent.
(The Newton decomposition's dimension-counting role — confirming that
the surviving operators have $n \geq 2$ internal covariant derivatives
— is $N$-independent by the same algebraic argument; see Appendix G §6.2.)

**Step 7: $\mathrm{dev}(\mathrm{Tr}(DF)^2) \geq 2$.**  [formerly Step 8]
```

### E. One-sentence attribution note (canonical form)

> The n ≥ 2 survival previously labeled "Newton decomposition" is accomplished by L6 (𝒞-elimination) + L7–8 (spectral dev ≥ 2 classification); see Appendix G for why Newton decomposition is not the mechanism.

*(In the PROOF-CHAIN.md table this appears as a italic note row; in the in-text narrative it can be a parenthetical.)*

---

## Renumbering decision

**Decision: RENUMBER.** Old Links 8, 9, 10, 10b, 11, 12, 13, 14, 15, 16, 17, 18 become new Links 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 respectively. The final chain has 17 numbered proved links + 1 CONDITIONAL (new Link 18 = old Link 18 = AF match).

**Justification.**
The alternative — keeping the existing numbers and leaving a blank "L7 = historical marker" — creates three practical problems:
1. A referee reading the proof chain sees 18 numbered links but only 17 proved ones, with a tombstone row labeled "removed — see L6+L8-9." This is confusing and invites re-litigation of the ghost.
2. Every downstream citation of "Link 8" (spectral dev ≥ 2) is the natural first proof step after C-elimination. Calling it "Link 8" after removing Link 7 creates a one-step gap in what should be a clean forward sequence.
3. The chain's own §IV.4 describes it as proving the gap "through a sequence of steps." A gap in step numbers weakens the rhetorical force.

Renumbering keeps the sequence clean: L6 (C-elimination) → L7 (dev ≥ 2 for Tr(DF)²) → L8 (dim-6 classification). The logical adjacency maps correctly to the numerical adjacency. The one-sentence note in the table explains to any reader why L7 in the prior draft has become a note and why the new L7 is what was previously numbered 8.

**Full renumbered PROOF-CHAIN.md §IV.1 table:**

| Step | Statement | Status | Source |
|:-----|:----------|:-------|:-------|
| 1 | Δ₀^KK > 0 | Proved (Thm 4) | Section 4 |
| 1b | Δ₀^std > 0 (IR equivalence) | Proved (Thm 5) | Section 4.5 |
| 2 | UV stability | Literature | CMP 109, 119 |
| 3 | Polymer convergence, κ k-indep | Literature | CMP 109, Thm 1 |
| 4 | (B1): analyticity, k-indep radius | Proved (Part I) | Extraction from CMP 95-109 |
| 5 | (B2): SL(N,ℂ) extension | Proved (Part II) | Standard complex analysis |
| 6 | C-elimination of Tr(F³) | Proved (exact) | Section 5.3.1 |
| *[note]* | *The n ≥ 2 survival previously labeled "Newton decomposition" is accomplished by L6 (C-elimination) + L7-8 below (spectral dev ≥ 2 classification); see Appendix G for why Newton decomposition is not the mechanism.* | — | — |
| 7 | dev(Tr(DF)²) ≥ 2 | Proved | Section 5.5.4 |
| 8 | Dim-6 classification: all ops have dev ≥ 2 | Proved | Section 5.6, Part III.3 |
| 9 | dev(δE_k^{d=6}) ≥ 2 non-pert | Proved | (B1)-(B2) + Section 5.6 classification |
| 10 | Spectral lemma constant C_p k-independent | Proved | Section 5.5.3, Step 3 |
| 11 | C_new g_k^4 Δ̂² bound | Proved | Section 5.5 + Steps 9, 10 |
| 12 | RG recursion: C_{k+1} = C_k/4 + C_new | Proved | Section 5.4 |
| 13 | Σ C_k g_k^4 Δ̂_k² < ∞ | Proved | Section 5.4.6 |
| 14 | Δ_∞ > 0 | Proved | Section 5.7 |
| 15 | Gradient-flow: well-posedness, contractivity, small-field preservation, K-uniform polymer decay | Proved (Lemmas 1.1-1.5) | Appendix L, §L.1 |
| 16 | Continuum flowed Schwinger functions: unique, OS0-OS4 at fixed t > 0 | Proved (Lemmas 2.2-2.4) | Appendix L, §L.2 |
| 17 | [Tr F²]_R operator + T_μν; L.1(i)(ii), L.3(i)-(v) closed | Proved (Lemmas 3.7-3.9, 4.1) | Appendix L, §§L.3-L.4 |
| 18 | AF match (L.2), leading-order OPE (L.4) | Conditional on H4 (Lemmas 4.2-4.3) | Appendix L, §L.4 |

Note: Link 11's source field updated from "Steps 10, 10b" to "Steps 9, 10" reflecting the renumbering (old 10 → new 9, old 10b → new 10).

---

## Self-suspicion

**S1 — Did I miss a hidden L7 dependency in Links 10-18?**
Grep across all `critiques/link-*.md` for "Link 7|L7|Newton decomp|Step 7" returned only `link-07-critic.md` and `chain-state.md`. The I3 tracking file mentions Step 7 but Step 10's I3 entry explicitly reads "Follows from (B1)-(B2) and Step 9" — no Step 7 upstream. The chain table in PROOF-CHAIN.md §IV.1 shows Link 10's source as "(B1)-(B2) + Section 5.6 classification" — no L7 dependency listed. Link 11's source is "Section 5.5 + Steps 10, 10b" — no L7. **Dependency check: CLEAN.**

**S2 — Does the note-row format work in a Markdown table?**
An italic note row inside a `|:--|:--|` table is non-standard. A referee compiling LaTeX from this Markdown may find the note row problematic if the table is auto-converted. **Mitigation:** the next runner should verify whether PROOF-CHAIN.md is compiled directly or processed by a LaTeX pipeline. If the latter, the note row should be replaced by a table footnote or a parenthetical paragraph immediately below the table. Flag in §What the next runner needs to know.

**S3 — Backward verification: did I check ALL 18 link critic files, not just 8 and 9?**
Yes. The grep command was run against the entire `chain-verification/critiques/` directory (not just links 8-9), searching for L7/Newton decomp/Step 7 across all critic files. The only returns were the L7 critic file itself and the chain-state summary. Links 10, 10b, 11, 12, 13, 14, 15, 16, 17, 18 all clear. **Confirmed: backward verification complete.**

---

## What the next runner needs to know

1. **Apply the four edits (A through D above) to the preprint.** This is a pure editorial pass: replace the four FROM blocks with the four TO blocks. No new mathematics. No lemma changes.

2. **Update chain-state.md:** Change Link 7's row from BROKEN to COLLAPSED. Renumber rows 8-18 to 7-18. Update the §D toolkit row "Newton dec | n ≥ 2 survives | §5.3.1 | VERIFIED | R" to read "n ≥ 2 survival | via L6 + L7-8 (spectral); App G | absorbed | —".

3. **Note-row format caveat (S2):** If PROOF-CHAIN.md feeds a LaTeX compilation pipeline, replace the italic note row with a \footnote or a paragraph immediately following the table. If it is Markdown-only, the italic note row as written is acceptable.

4. **I3 Step numbering:** The `I3-N-dependence-tracking.md` Step 7 gloss must be merged into Step 6 and subsequent steps renumbered (old Steps 8-10b → new Steps 7-10). This file is a supplementary tracking document; renumbering is low-priority but necessary for consistency.

5. **The mass gap (Link 14, now renumbered) is a separate WEAKENED repair.** This collapse does not touch the Conjecture 1 / polymer-sum spectral lemma issue that is the highest-priority Wave 2 item. The two repairs are independent.

6. **Voice register:** "Link 7 was a ghost. The ghost is gone. The chain is 17 proved links, numbered cleanly 1 through 17. THE PROOF CHAIN IS COMPLETE."
