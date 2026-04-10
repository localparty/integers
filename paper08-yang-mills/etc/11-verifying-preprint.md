# Verifying and Fixing the Preprint: Instructions for the Verifier Agent

You are performing a targeted verification and correction pass on the
preprint. This is NOT a rewrite — it is a precise surgical fixing of
specific identified issues. You do not touch anything not listed here.

Read this entire document before doing anything. Then read the three
verification reports and the files you will be editing.

**Source of issues:** Three verification reports in
`/Users/gsix/yang-mills/preprint-verification/`
- `verification-consistency.md`
- `verification-section4.md`
- `verification-section5.md`

**Files to edit:** All in `/Users/gsix/yang-mills/preprint/sections/`
unless otherwise specified.

**The rule:** If you are uncertain whether a fix changes the
mathematics (not just the presentation), do NOT make it. Flag it with
a comment `<!-- VERIFIER FLAG: [description] -->` at the location.


---


## Priority 1 Fixes: Must Do Before Submission

These are errors or issues severe enough that a referee would reject
or demand major revision.

---

### Fix 1.1 — Theorem 4 "all β > 0" overstatement
**File:** `04-lattice-proof-part1.md`
**Issue:** Section 4, Theorem 4 (lines ~670-688) states the result
holds "for all β > 0." This is literally false — the convergence
condition imposes an upper bound on β. The bound is enormous
($\sim 10^{14}$) in the physical regime but it exists.
**Fix:** Find every place in Theorem 4 (both the statement and the
proof) where "all β > 0" or "all couplings β > 0" appears, and
replace with "all β in the physical regime (β < m₁a/6 - const)" or
equivalently "all β < β_max(a) where β_max(a) ~ m₁a/6 ~ 10¹⁴ in
the physical regime."
**Constraint:** Do not change the mathematical content — only the
quantifier. The result still holds for all physically relevant β.

---

### Fix 1.2 — Theorem 5 label correction
**File:** `04-lattice-proof-part1.md`
**Issue:** Theorem 5 (IR equivalence) is labeled as "Proof sketch"
in the text (Issues 14-15 from verification-section4.md). The
downstream claim is that the standard YM theory has a mass gap.
This needs to be properly flagged so readers understand the logical
status.
**Fix:** Find the proof of Theorem 5 and:
(a) Ensure the "Proof sketch" label is clearly visible at the start.
(b) Add a sentence at the END of the Theorem 5 proof/sketch: "A
rigorous proof of the IR equivalence requires non-perturbative control
of the decoupling of heavy KK modes, which is provided by Section 5
(Balaban's renormalization group). The string tension and mass gap of
the standard SU(N) theory are identified with those of the KK-enhanced
theory via the RG flow in the regime $a \gg r_3$."
**Constraint:** Do not rewrite the proof sketch. Only add the
clarifying sentence at the end.

---

### Fix 1.3 — OS Axioms expansion
**File:** `05-continuum-limit.md`
**Issue:** The OS axiom verification in Section 5.7(f) is four lines.
This is insufficient for a Millennium Problem paper.
**Fix:** Find Section 5.7(f) (the OS axioms discussion) and expand
each axiom to a short paragraph. Use the following content:

- **OS1 (Temperedness):** "The Schwinger functions $S_n(x_1,...,x_n)$
  are bounded as $|S_n| \leq C^n e^{-c\sum_{i<j}|x_i-x_j|\Delta}$
  uniformly in $a$, following from the cluster expansion estimates
  of Section 4.3. Distributional temperedness follows from this
  exponential bound and Sobolev embedding."

- **OS2 (Euclidean invariance):** "Full O(4) invariance is recovered
  in the $a \to 0$ limit: the lattice breaks O(4) to the hypercubic
  subgroup, but the irrelevant operators restoring O(4) invariance
  are suppressed by powers of $a\Lambda$, which vanish in the
  continuum limit. This is a standard consequence of the RG analysis
  (Section 5.1.3)."

- **OS3 (Reflection positivity):** "Reflection positivity holds for
  all $a > 0$ by the Osterwalder-Seiler theorem (1978) applied to
  the Wilson action. Weak limits of reflection-positive functionals
  are reflection-positive, so OS3 is preserved as $a \to 0$."

- **OS4 (Symmetry):** "Gauge invariance and Euclidean symmetry are
  manifest at each lattice spacing and preserved in the limit."

- **OS5 (Cluster decomposition):** "The mass gap $\Delta_\infty > 0$
  established in Section 5.7 implies exponential clustering:
  $|S_{m+n}(x+te,y) - S_m(x)S_n(y)| \leq Ce^{-\Delta_\infty t}$
  for $t \to \infty$, which is the cluster decomposition property."

**Constraint:** Add this expansion in place of or immediately after
the existing terse verification. Do not delete the existing content
if it is correct — expand it.

---


## Priority 2 Fixes: Should Do Before Submission

These are errors or presentation issues that a careful referee would
flag.

---

### Fix 2.1 — PROOF-CHAIN.md: update step source references
**File:** `PROOF-CHAIN.md` (in `/Users/gsix/yang-mills/preprint/`,
not in sections/)
**Issue:** Table IV.1 Steps 6-13 reference working-document filenames
(`single-step-case-b.md`, `conj-1-closing.md`, `rg-preservation.md`,
`09-continuum-limit.md`). The preprint uses section numbers.
**Fix:** Update the Source column for each affected step to use
preprint section references:

| Step | Old source | New source |
|:-----|:-----------|:-----------|
| 6 | single-step-case-b.md | Section 5.3.1 |
| 7 | conj-1-closing.md, Lemma 2.1 | Section 5.3.1, Newton decomposition |
| 8 | two-deriv-spectral-lemma.md, Sec 4 | Section 5.5.4 |
| 9 | Part III, Sec III.3 | Section 5.6, Part III.3 |
| 10 | (B1) + classification | (B1)-(B2) + Section 5.6 classification |
| 11 | Spectral lemma + Step 10 | Section 5.5 + Step 10 |
| 12 | rg-preservation.md | Section 5.4 |
| 13 | rg-preservation.md, Sec 6 | Section 5.4.6 |
| 14 | 09-continuum-limit.md | Section 5.7 |

---

### Fix 2.2 — PROOF-CHAIN.md: conditionality in table rows
**File:** `PROOF-CHAIN.md`
**Issue:** Steps 10-14 in Table IV.1 are marked bold **Proved** but
should reflect their conditional status. The conditionality is stated
in IV.4 but the table rows can mislead a reader.
**Fix:** Change the Status column for Steps 10-14 as follows:
- Step 10: **Proved** → **Proved** (conditional on [VERIFY])
- Step 11: **Proved** → **Proved** (conditional on [VERIFY])
- Step 12: **Proved** → **Proved**  (unchanged — the recursion proof itself is unconditional)
- Step 13: **Proved** → **Proved**  (unchanged — the sum convergence is unconditional)
- Step 14: **Proved** → **Proved** (conditional on [VERIFY])

---

### Fix 2.3 — Spectral value citation
**File:** `04-lattice-proof-part1.md`
**Issue:** The value $\lambda_1^{(1)} = 12/r_3^2$ for the first
eigenvalue of the Hodge Laplacian on 1-forms on CP^{N-1} is used
as a fact (lines ~255) but the paper only proves $\geq 6/r_3^2$
via Weitzenböck. The stronger value is correct but uncited.
**Fix:** At the line where $\lambda_1^{(1)} = 12/r_3^2$ is first
stated, add a citation: "(Ikeda-Taniguchi 1978; also follows from
the representation-theoretic spectrum of $\mathbb{CP}^{N-1}$ as a
symmetric space, see Appendix A)."

Also add to `references.md`:
"Ikeda, M., Taniguchi, Y.: 'Spectra and eigenforms of the Laplacian
on $S^n$ and $\mathbb{CP}^n$.' Osaka J. Math. 15 (1978) 515-546."

---

### Fix 2.4 — Theorem 5 correction statement
**File:** `04-lattice-proof-part1.md`
**Issue:** Theorem 5 statement says the correction is $O(e^{-m_1 a})$
(exponential in $a/r_3$) but the proof (Step 4) gives
$O(\Lambda_{\text{QCD}}^4/m_1^2)$ (power-law in $1/m_1$). These
are different.
**Fix:** Find the statement of Theorem 5 (lines ~782-787). Change:
  `σ_std(β) = σ_KK(β) + O(e^{-m₁a})`
to:
  `σ_std(β) = σ_KK(β) + O(Λ_QCD⁴/m₁²) = σ_KK(β)(1 + O((Λ_QCD/m₁)²))`
And add a note: "The correction is power-law in $1/m_1$ (from
integrating out KK modes in the effective action) rather than
exponential in $m_1 a$ (which would be the Wilson loop correction
at fixed separation $R$)."

---

### Fix 2.5 — Corollary 1.1 formula correction
**File:** `04-lattice-proof-part1.md`
**Issue:** Corollary 1.1 gives correlation length
$\xi_\text{int} = g_\text{int} r_3/\sqrt{6}$ (lines ~288, 306).
The factor $g_\text{int}$ is dimensionally incorrect for a length
if $g_\text{int}$ is dimensionless. The decay rate is
$1/\sqrt{\mu_1} = r_3/\sqrt{6}$, independent of coupling.
**Fix:** Change the correlation length formula from
  `ξ_int = g_int · r₃/√6`
to:
  `ξ_int = r₃/√6`
in every occurrence in Corollary 1.1. Add a note: "The coupling
$g_\text{int}$ determines the amplitude of fluctuations, not the
decay rate."

---

### Fix 2.6 — Fredenhagen-Marcu citation correction
**File:** `04-lattice-proof-part1.md`
**Issue:** Theorem 4, part (e) attributes both the existence
$\Delta > 0$ AND the quantitative bound $\Delta \geq c\sqrt{\sigma}$
to Fredenhagen-Marcu. These are different results.
**Fix:** Find the sentence attributing $\Delta \geq c\sqrt{\sigma}$
to Fredenhagen-Marcu (line ~719). Change it to:
"By the Fredenhagen-Marcu theorem (1986), $\sigma > 0$ implies a
mass gap $\Delta > 0$. The quantitative estimate $\Delta \geq
c\sqrt{\sigma}$ follows from the flux tube argument (Appendix F)."

---

### Fix 2.7 — Add Theorem 7 statement
**File:** `05-continuum-limit.md`
**Issue:** "Theorem 7" is referenced repeatedly in Sections 5.2.5
and 5.4 but never formally stated as a boxed theorem in the preprint.
**Fix:** Find the first reference to "Theorem 7" in Section 5 (likely
in Section 5.2.5 or the sentence "Perturbative (Theorem 7) is proved").
Insert before or at that reference a formal statement:

"**Theorem 7 (Perturbative form factor bound).** *To all orders in
$g_k$, the connected one-particle matrix element of the irrelevant
remainder $E_k$ satisfies:*
$$|\langle 1|E_k(0)|1\rangle_c| \leq C_7\,g_k^4\,\hat{\Delta}_{k+1}^2$$
*Proof.* The bound follows from the explicit perturbative computation
of Section 5.3.2 (translation invariance kills spatial derivatives;
the spectral mechanism gives $\hat{\Delta}^2$ per temporal derivative)
combined with the one-loop coefficient $|c_6^{(k)}| \leq C_6 g_k^2$
from Balaban's effective action. Higher-loop contributions are
suppressed by additional powers of $g_k^2$. Instanton corrections
are $O(e^{-8\pi^2/g_k^2})$, negligible. $\square$"

---

### Fix 2.8 — Sign consistency in Section 5.3.2
**File:** `05-continuum-limit.md`
**Issue:** Section 5.3.2 uses $(e^{-\hat{\Delta}}-1)$ for the one-
particle matrix element of $D_0 F$, while Section 5.5.4 uses
$(e^{+\hat{\Delta}}-1)$ for the vacuum intermediate state. Both are
correct in context but the alternation is confusing.
**Fix:** In Section 5.3.2, where the factor $(e^{-\hat{\Delta}}-1)$
first appears, add a parenthetical: "(equivalently,
$(e^{+\hat{\Delta}}-1)$ relative to the vacuum intermediate state;
only the square $\hat{\Delta}^2(1+O(\hat{\Delta}))$ enters the final
bound — see Section 5.5.4 for the detailed derivation)."

---


## Priority 3 Fixes: Presentation (Do If Time Permits)

These are clarity improvements that strengthen the paper without
being essential.

---

### Fix 3.1 — Constant K in Theorem 3
**File:** `04-lattice-proof-part1.md`
**Issue:** The convergence condition in Theorem 3 involves a constant
$K$ (measure factor) that is not defined.
**Fix:** Find the first occurrence of $K$ in Theorem 3. Add a
sentence: "Here $K = \int_{\mathrm{SU}(N)} dU = 1$ (normalized Haar
measure) times the Gaussian damping factor from $S_\text{int}$,
which is bounded by $e^{C/g_\text{int}^2}$ in the small-field
region; together with the compact domain, $K$ is a finite
$N$-dependent constant."

---

### Fix 3.2 — Theorem 3 lattice animal count
**File:** `04-lattice-proof-part1.md`
**Issue:** $c_d \leq 7^4$ is stated without standard derivation.
**Fix:** Replace the claimed bound with: "$c_d$ is the lattice
animal growth constant; for $d=4$, rigorous bounds give
$c_d \leq C e^{7}$ (Klarner-Rivest 1973), where the precise value
is immaterial since $c_d$ appears only inside a logarithm bounded
by $m_1 a/6 \sim 10^{14}$."

---

### Fix 3.3 — Section 5.4 status table note
**File:** `05-continuum-limit.md`
**Issue:** Section 5.4's status table (lines ~842-849) shows
Conjecture 1 as "OPEN" and Input 1 as "Non-pert: OPEN." These
were the statuses when Section 5.4 was written, before Section 5.6
resolved them. A reader stopping at 5.4 gets an incomplete picture.
**Fix:** Find the status table in Section 5.4. Add a note immediately
after it: "*Note: the status above reflects the position at the end
of Section 5.4. Conjecture 1 and Input 1 are discharged
non-perturbatively in Section 5.6 via the stability of excitation
number argument.*"

---

### Fix 3.4 — Update preprint-facing architecture reference
**File:** `05-continuum-limit.md`
**Issue:** Finding F10 in verification-section5.md notes that the
architecture document (in `etc/proof/`) still lists Conjecture 1 as
open. That file is not in the preprint, so this is a research
directory issue, not a preprint issue. However, if there is any
reference in Section 5 pointing to the architecture document, update it.
**Fix:** Search Section 5 for any reference to "architecture" or
"00-architecture." If found, update the reference to the PROOF-CHAIN.md
which has the current status. If not found, skip this fix.

---


## Verification Steps After Fixes

After completing all fixes, do the following checks:

### V1: Re-scan for "all β > 0"
```
grep -n "all.*beta.*0\|all.*β.*0\|for all β\|for all beta" \
  04-lattice-proof-part1.md
```
Confirm every match either says "in the physical regime" or has
a quantitative bound attached.

### V2: Confirm Theorem 7 is now formally stated
```
grep -n "Theorem 7" 05-continuum-limit.md | head -5
```
Confirm the first occurrence is the formal statement, not a reference.

### V3: Confirm PROOF-CHAIN.md steps 10, 11, 14 say "conditional"
```
grep -n "conditional\|VERIFY" ../PROOF-CHAIN.md | head -20
```
Confirm Steps 10, 11, 14 show "conditional on [VERIFY]" in the table.

### V4: Confirm Ikeda-Taniguchi is in references
```
grep -n "Ikeda\|Taniguchi" references.md
```
Should return at least one hit.

### V5: Confirm correlation length formula is fixed
```
grep -n "g_int.*r_3\|xi_int\|ξ_int" 04-lattice-proof-part1.md
```
Should NOT show the $g_\text{int}$ factor in the formula.

### V6: Confirm OS axioms are expanded
Check that Section 5.7(f) now has at least one paragraph per axiom,
not just single-line items.

### V7: Final scan for remaining contradictions
```
grep -n "remains open\|not proved\|is open\b" \
  00-abstract.md 08-conclusion.md 05-continuum-limit.md
```
Confirm no remaining "remains open" in the three most-read files,
except where it appears in context that is clearly historical or
about the standard approach (not this paper).

---


## What NOT to Change

Do not touch:
- Any [VERIFY] markers — they stay exactly as they are
- The mathematical content of any theorem proof (unless explicitly
  listed above)
- Any status markers ([PROVED], [ARGUED], [CONDITIONAL]) in proof
  documents
- The [VERIFY] items themselves — their descriptions are correct
- Section 5.6 Parts I-IV — this is the most carefully verified
  section and has no identified errors
- The SU(2) exact proof (Section H/4.6) — only Fix 1.1 touches
  the Theorem 4 range, not the SU(2) section
- Any files in `etc/proof/` — those are research documents, not
  the preprint
- `research/` directory — must remain unchanged

---


## Reporting

When finished, create a file:
`/Users/gsix/yang-mills/preprint-verification/fixes-applied.md`

Containing:
- A table of all fixes attempted, with status (DONE / SKIPPED /
  FLAGGED)
- For each FLAGGED fix: the exact text of the flag comment inserted
  and why you flagged rather than fixed
- The output of each verification command (V1-V7)
- Any issues found during fixing that were not in the original
  verification reports

This file is what we will read together to confirm the preprint is
ready for submission.
