# Cross-Paper Coherence Check

> **Date:** April 5, 2026
> **Scope:** All six papers, abstracts, status claims, and cross-references
> **Method:** Systematic check following Track C of Prompt 22

---

## C.1 Abstract-to-Abstract Consistency

| # | Issue | Location | Status | Fix Applied |
|---|-------|----------|--------|-------------|
| 1a | Paper 1 abstract: `w₀ = −1` (revised) vs Paper 2 abstract: `w₀ = −1, w_a = 0` (revised) | `paper1/00-abstract.md`, `paper2/00-abstract.md` | **NOTED** | Both abstracts already revised to `w = −1`. Consistent. |
| 1b | Paper 2 body/appendices still show `w₀ = −0.85` | `paper2/02-sections-2-to-7.md` (line 3), `paper2/appendices/10-appendix-f-thawing-dilaton.md`, `paper2/appendices/07-appendix-c-s8-tension.md`, `paper2/appendices/06-appendix-b-expansion-history.md`, `paper2/appendices/05-appendix-a-age-computation.md` | **NOTED** | All occurrences carry explicit superseded/revision banners. Appendix F has full "superseded" warning at top. Sections 2-7 has top-level revision note. No `w₀ = −0.85` appears as an active prediction. |
| 2 | Paper 1: "conjectured `Z₃` orbifold gives three generations" vs Paper 4 §6.2: "Derived from `χ(CP²) = 3`" | `paper1/00-abstract.md` lines 75, 95 | **RESOLVED** | Updated Paper 1 abstract: "conjectured `Z₃` orbifold" changed to "derived from `χ(CP²) = 3` via the index theorem (Paper 4, §6.2)". Updated in both the speculative extensions paragraph and the "six conjectured" list. |
| 3 | Paper 3 Appendix A §A.4.2 should reference Paper 4 §2.3 for M-theory circle | `paper3/15-appendix-a-non-perturbative-completion.md` lines 206-215 | **NOTED** | Already correct: "The e-circle `S¹` of the framework is the M-theory circle `S¹_M` (Paper 4, §2.3). This identification is not a conjecture..." with explicit `[Established: Paper 4, §2.3]` tag. |
| 4 | Paper 5 should cite Paper 4 §7.8 when using `Λ_QCD` | `paper5/03-string-tension-from-geometry.md` (line 71), `paper5/06-proton-mass.md` (line 23), `paper5/00-abstract.md` (lines 60-61) | **NOTED** | Already correct. Paper 5 §3 says "From Paper 4 §7.8", §6 says "Paper 4, §7.8", and abstract says "Paper 4 (§7.8)". |
| 5 | Paper 5 §5 references "Paper 2, §E" for bulk leptogenesis | `paper5/05-baryon-asymmetry.md` (lines 10-11), `paper5/00-abstract.md` (line 53) | **NOTED** | Reference is correct. Paper 2 Appendix E ("Mirror Baryogenesis, the `1/ξ²` Law") establishes the `1/ξ²` scaling law from bulk leptogenesis on the `Z₂` orbifold. Paper 5 §5 correctly distinguishes: Paper 2 §E provides the scaling law, Paper 5 §5 provides the CP² cross-check. |
| 6 | Paper 6 and Paper 4 should both flag inflaton ≠ radion | `paper4/07-predictions.md` (lines 863-872), `paper6/03-inflation.md` (lines 1-63) | **NOTED** | Both papers flag this correctly. Paper 4 §7.15 says "The radion (e-circle radius R) is NOT the inflaton... predictions suspended." Paper 6 §3.1 says "The Inflaton Is Not the Radion" and "predictions are suspended pending identification of the correct inflaton field." Paper 4 §10 conclusion table also marks these as "Suspended (inflaton ≠ radion; §7.15)". |

---

## C.2 Status Claims Updated

| # | Claim | Previous Status | Updated Status | Location | Fix Applied |
|---|-------|----------------|----------------|----------|-------------|
| 1 | All-orders finiteness (KK sum factor) | Not in table | **Established** (Theorem K.1, Paper 1 Appendix K §K.6) | `paper4/08-what-is-established-vs-what-is-conjectured.md` | **RESOLVED** | Added row to table. |
| 2 | SLOCC-isometry map | Listed as "Conjectured (Section 5.5)" | **Established at Lie algebra level** (Theorem 5.2, §5.6); global topology open (§9.4) | `paper4/08-what-is-established-vs-what-is-conjectured.md` | **RESOLVED** | Added row to table. |
| 3 | Moduli stabilization | Listed in §9.1 as open | **Partially established**: S² and CP² dynamically stabilized by spectral zeta nonvanishing; κ from Planck mass constraint (§9.5, OC-2) | `paper4/08-what-is-established-vs-what-is-conjectured.md` | **RESOLVED** | Added row to table. |
| 4 | Gauge coupling hierarchy | Not addressed | **Leading order derived**: α₃/α₂ = 1 at GUT scale for κ = 3.545 × 10⁻²; first-principles κ via three-equation system (§9.5) | `paper4/08-what-is-established-vs-what-is-conjectured.md` | **RESOLVED** | Added row to table. |

---

## C.3 Promises Not Yet Redeemed

| # | Promise | Location | Status | Action |
|---|---------|----------|--------|--------|
| 1 | "Remaining open problems (future papers): Inflation from the dilaton (Paper 6), Full thermal history (Paper 6)" | `paper5/08-holonomy-correspondence.md` lines 104-106 | **RESOLVED** | Paper 6 exists and addresses both. Updated: moved to "Completed in later papers" section with cross-reference to Paper 6 §3. |
| 2 | "Remaining open problems: The cosmological constant — simultaneous stabilization (Paper 7), Logarithmic BH entropy corrections (Paper 8)" | `paper5/08-holonomy-correspondence.md` lines 107-108 | **NOTED** | Papers 7 and 8 do not exist yet. Updated references to point to current locations: Paper 4 §7.21 (CC) and Paper 4 §7.18 (BH entropy). Retained as open. |
| 3 | `[CITE: ]` markers | Reported in `etc/paper1/25-in-depth-review.md` lines 225-227 as being in Sections 6.1, 6.3, 6.5 | **NOTED** | No `[CITE:]` markers found in any `paper*/` files. The review document's Fix 5 appears to have been applied previously. All clear. |
| 4 | "companion paper" references | `paper1/00-abstract.md` (line 12, 114), `paper2/00-abstract.md` (line 9) | **NOTED** | These are legitimate cross-references between papers in the series (Papers 1-6 exist). Not stale placeholders. |
| 5 | "future work" / "open calculation" — resonant leptogenesis with Z₃ mass spectrum | `paper5/05-baryon-asymmetry.md` lines 136, 162 | **NOTED** | Genuine open problem. Listed in Paper 5 §5.5. The leading-order calculation overshoots by ~10³; resonant leptogenesis calculation is genuinely pending. No paper in the series claims to have done it. |

---

## C.4 The R Ambiguity

| Issue | Location | Status | Fix Applied |
|-------|----------|--------|-------------|
| Two R values (12 um orbifold vs 21 um circle) — IC1 from in-depth review | `paper1/02-framework.md` §2.7.2 | **NOTED** | §2.7.2 "A Note on Two Scenarios" already exists and addresses this directly: "The **circle scenario** (`S¹`) has circumference `L ~ 50-200 um` (`R ~ 8-32 um`)... The **orbifold scenario** (`S¹/Z₂`) has brane separation `R ~ 12 um`... The two scenarios make different predictions for the Yukawa gravitational deviation scale (21 um vs 12 um) and are experimentally distinguishable. See Section 6.6 for the full comparison." Fix 14 from the hostile review was already applied. |

---

## Summary

| Category | Issues Checked | Already Correct | Fixes Applied | Flagged Open |
|----------|---------------|-----------------|---------------|--------------|
| C.1 Abstract consistency | 6 | 5 | 1 | 0 |
| C.2 Status claims | 4 | 0 | 4 | 0 |
| C.3 Promises not redeemed | 5 | 3 | 1 | 1 |
| C.4 R ambiguity | 1 | 1 | 0 | 0 |
| **Total** | **16** | **9** | **6** | **1** |

**6 fixes applied, 1 flagged open** (resonant leptogenesis calculation in Paper 5 §5 -- genuinely pending, not a stale promise).

### Files Edited

1. `paper1/00-abstract.md` -- Updated "conjectured Z₃ orbifold" to "derived from χ(CP²) = 3 (Paper 4, §6.2)" in two places
2. `paper4/08-what-is-established-vs-what-is-conjectured.md` -- Added 4 new rows: all-orders finiteness, SLOCC map, moduli stabilization, gauge coupling hierarchy
3. `paper5/08-holonomy-correspondence.md` -- Updated "future papers" list: Paper 6 topics moved to "Completed", remaining items given current-paper references
