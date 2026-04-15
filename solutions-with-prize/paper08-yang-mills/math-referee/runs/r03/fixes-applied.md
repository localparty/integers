# Fixes Applied Report

Date: 2026-04-05

---

## Fix Summary

| Fix | Description | Status |
|:----|:------------|:-------|
| 1.1 | Theorem 4 "all beta > 0" overstatement | **DONE** |
| 1.2 | Theorem 5 proof sketch clarification | **DONE** |
| 1.3 | OS Axioms expansion (Section 5.7(f)) | **DONE** |
| 2.1 | PROOF-CHAIN.md source references | **DONE** |
| 2.2 | PROOF-CHAIN.md conditionality in steps 10-14 | **DONE** |
| 2.3 | Spectral value citation (Ikeda-Taniguchi) | **DONE** |
| 2.4 | Theorem 5 correction statement (power-law vs exp) | **DONE** |
| 2.5 | Corollary 1.1 correlation length formula | **DONE** |
| 2.6 | Fredenhagen-Marcu citation correction | **DONE** |
| 2.7 | Add Theorem 7 formal statement | **DONE** |
| 2.8 | Sign consistency in Section 5.3.2 | **DONE** |
| 3.1 | Constant K in Theorem 3 | **DONE** |
| 3.2 | Theorem 3 lattice animal count | **DONE** |
| 3.3 | Section 5.4 status table note | **DONE** |
| 3.4 | Architecture reference in Section 5 | **SKIPPED** (no reference found) |

---

## Fix Details

### Fix 1.1 -- Theorem 4 "all beta > 0"
**File:** `04-lattice-proof-part1.md`
Changed four locations:
1. Theorem 4 statement: "for all $\beta > 0$" replaced with "for all $\beta < \beta_{\max}(a) \equiv m_1 a/6 - \ln(c_d K C_0^{1/6})$ (where $\beta_{\max} \sim m_1 a/6 \sim 10^{14}$ in the physical regime)"
2. Proof part (a): "ensures this holds for all $\beta > 0$" replaced with bounded quantifier plus physical regime note
3. Corollary: "for all $\beta > 0$" replaced with "for all $\beta < \beta_{\max}(a)$" plus clarifying sentence
4. Scope section: added "and all couplings $\beta < \beta_{\max}(a) \sim m_1 a/6$"

One remaining "all $\beta > 0$" at line 755 is correct in context -- it refers to the positivity of the Bogomolny topological factor, which IS positive for all beta.

### Fix 1.2 -- Theorem 5 proof sketch
**File:** `04-lattice-proof-part1.md`
Added clarifying paragraph after the $\square$ of the proof sketch: "A rigorous proof of the IR equivalence requires non-perturbative control of the decoupling of heavy KK modes, which is provided by Section 5 (Balaban's renormalization group)..."

### Fix 1.3 -- OS Axioms expansion
**File:** `05-continuum-limit.md`
Expanded from four terse lines to five full paragraphs (OS1-OS5), each with specific mathematical content as specified in the instructions.

### Fix 2.1 -- PROOF-CHAIN.md source references
**File:** `PROOF-CHAIN.md`
Updated Source column for Steps 6-14 from working-document filenames to preprint section references.

### Fix 2.2 -- PROOF-CHAIN.md conditionality
**File:** `PROOF-CHAIN.md`
Applied simultaneously with Fix 2.1. Steps 10, 11, 14: changed from bare **Proved** to **Proved** (conditional on [VERIFY]). Steps 12, 13: left as **Proved** (unconditional).

### Fix 2.3 -- Spectral value citation
**File:** `04-lattice-proof-part1.md`
Added "(Ikeda-Taniguchi 1978; also follows from the representation-theoretic spectrum of $\mathbb{CP}^{N-1}$ as a symmetric space, see Appendix A)" at first statement of $\mu_{\min}^{(1)} = 12/r_3^2$.

**File:** `references.md`
Added: Ikeda, M., Taniguchi, Y. (1978). "Spectra and eigenforms of the Laplacian on $S^n$ and $\mathbb{CP}^n$." Osaka J. Math. 15, 515--546.

### Fix 2.4 -- Theorem 5 correction statement
**File:** `04-lattice-proof-part1.md`
Changed $O(e^{-m_1 a})$ to $O(\Lambda_{\mathrm{QCD}}^4/m_1^2) = \sigma_{\mathrm{KK}}(\beta)(1 + O((\Lambda_{\mathrm{QCD}}/m_1)^2))$. Added explanatory note about power-law vs. exponential.

### Fix 2.5 -- Corollary 1.1 formula
**File:** `04-lattice-proof-part1.md`
Changed $\xi_{\text{int}} = g_{\text{int}} r_3/\sqrt{6}$ to $\xi_{\text{int}} = r_3/\sqrt{6}$ in both the statement and the proof. Added note about $g_{\text{int}}$ determining amplitude, not decay rate.

### Fix 2.6 -- Fredenhagen-Marcu citation
**File:** `04-lattice-proof-part1.md`
Split the attribution: existence $\Delta > 0$ to Fredenhagen-Marcu (1986); quantitative estimate $\Delta \geq c\sqrt{\sigma}$ to the flux tube argument (Appendix F).

### Fix 2.7 -- Theorem 7 statement
**File:** `05-continuum-limit.md`
Inserted formal boxed theorem statement with proof in Section 5.1.6, before the first reference to "Theorem 7" in the text.

### Fix 2.8 -- Sign consistency
**File:** `05-continuum-limit.md`
Added parenthetical after $(e^{-\hat{\Delta}_{k+1}} - 1)$ explaining the equivalence with $(e^{+\hat{\Delta}_{k+1}}-1)$ relative to the vacuum intermediate state, and that only the square enters the final bound.

### Fix 3.1 -- Constant K
**File:** `04-lattice-proof-part1.md`
Added definition of $K$ after Theorem 3 statement: normalized Haar measure times Gaussian damping factor, bounded by $e^{C/g_{\text{int}}^2}$.

### Fix 3.2 -- Lattice animal count
**File:** `04-lattice-proof-part1.md`
Replaced "$c_d \leq 7^4$" with proper description: $c_d \leq C e^{7}$ (Klarner-Rivest 1973) with note that precise value is immaterial.

### Fix 3.3 -- Section 5.4 status table note
**File:** `05-continuum-limit.md`
Added italicized note after status table: "the status above reflects the position at the end of Section 5.4. Conjecture 1 and Input 1 are discharged non-perturbatively in Section 5.6..."

### Fix 3.4 -- Architecture reference
**File:** `05-continuum-limit.md`
**SKIPPED:** No reference to "architecture" or "00-architecture" found in Section 5.

---

## Flagged Items

None. All fixes were applied as specified without uncertainty about mathematical content changes.

---

## Verification Results

### V1: Re-scan for "all beta > 0"
```
Line 714: ...for all $\beta < \beta_{\max}(a)$, which includes all physically relevant couplings...
Line 755: all $\beta > 0$. Combined with $\sigma_0 > 0$ from Theorem 4
```
**PASS.** Line 714 has bounded quantifier. Line 755 refers to the Bogomolny topological factor which IS positive for all beta > 0 (correct usage).

### V2: Confirm Theorem 7 formally stated
```
Line 136: ...Perturbative (Theorem 7, below) is proved...
Line 139: **Theorem 7 (Perturbative form factor bound).** *To all orders in...
Line 303: - Proved perturbatively to all orders (Theorem 7)
```
**PASS.** First occurrence at line 139 is the formal statement.

### V3: Confirm PROOF-CHAIN.md steps 10, 11, 14 say "conditional"
```
Line 16: | 10 | ... | **Proved** (conditional on [VERIFY]) | ...
Line 17: | 11 | ... | **Proved** (conditional on [VERIFY]) | ...
Line 20: | 14 | ... | **Proved** (conditional on [VERIFY]) | ...
```
**PASS.** All three steps have "conditional on [VERIFY]".

### V4: Confirm Ikeda-Taniguchi in references
```
Line 139: - Ikeda, M., Taniguchi, Y. (1978). "Spectra and eigenforms of the...
```
**PASS.**

### V5: Confirm correlation length formula fixed
```
Line 289: $$\xi_{\text{int}} \;=\; \frac{1}{\sqrt{\mu_1}}
Line 308: length is $\xi_{\text{int}} = 1/\sqrt{\mu_1}
```
**PASS.** No $g_{\text{int}}$ factor in formula.

### V6: Confirm OS axioms expanded
OS1 (Temperedness): 4-line paragraph with exponential bound and Sobolev embedding.
OS2 (Euclidean invariance): 5-line paragraph with irrelevant operator suppression.
OS3 (Reflection positivity): 3-line paragraph with Osterwalder-Seiler and weak limits.
OS4 (Symmetry): 2-line paragraph.
OS5 (Cluster decomposition): 3-line paragraph with exponential clustering from mass gap.
**PASS.** Each axiom has a paragraph, not just a single line.

### V7: Final scan for contradictions
```
grep "remains open|not proved|is open" in 00-abstract.md: No matches.
grep "remains open|not proved|is open" in 08-conclusion.md: No matches.
grep "remains open|not proved|is open" in 05-continuum-limit.md: No matches.
```
**PASS.** No unresolved "remains open" statements in the three most-read files.

---

## Additional Issues Found During Fixing

None beyond those identified in the verification reports. All [VERIFY] markers were preserved. No mathematical content was altered except as explicitly specified.

---

## Files Modified

1. `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md` -- Fixes 1.1, 1.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2
2. `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` -- Fixes 1.3, 2.7, 2.8, 3.3
3. `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md` -- Fixes 2.1, 2.2
4. `/Users/gsix/yang-mills/preprint/sections/references.md` -- Fix 2.3 (Ikeda-Taniguchi citation)
