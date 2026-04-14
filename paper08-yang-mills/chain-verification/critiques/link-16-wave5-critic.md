# Link 16 Wave 5 Critic — OS-Axiom Convention Harmonization

**Target:** Continuum flowed Schwinger functions: unique (not subsequential), OS0--OS4 at fixed $t > 0$  
**Patch under review:** L16-patch.md (Wave 4 Author)  
**Prior verdict:** Wave 3 WEAKENED (inverted crosswalk sign; §H.8 third convention unacknowledged)  
**Wave:** 5, final verification  
**Runner:** Claude Sonnet 4.6, 2026-04-13  

---

## Verdict: SURVIVED

All four checks pass. The Wave 4 patch correctly resolves both grounds of the Wave 3 WEAKENED verdict. The five per-site edits from Wave 2 remain intact. No new defects introduced.

---

## C1 — Crosswalk inversion: CORRECT

**Check:** Is the crosswalk in the Wave 4 declaration correctly stated as §5.7 OS$k$ ↔ §L.2 OS$(k-1)$?

**Evidence verified directly from preprint:**

- `05-continuum-limit.md` line 2321: `**(OS3) Reflection positivity.**` — §5.7 places RP at slot 3.
- `L-clay-conjectures.md` lines 1177--1178: `(OS2) Reflection positivity` — §L.2 places RP at slot 2.

The offset is exactly $k-1$: slot 3 in §5.7 corresponds to slot 2 in §L.2. The Wave 4 declaration reads:

> "A cross-reference of the form `\S5.7, OS$k$' refers to the same axiom as OS$(k-1)$ in the present Appendix L convention."

This is arithmetically correct. The Wave 3 error — "$k+1$" instead of "$k-1$" — is fixed.

**C1 result: PASS.**

---

## C2 — Exemplar sentence: CORRECT

**Check:** Is "§5.7's OS3 = reflection positivity = OS2 here" accurate?

**Evidence:**

- §5.7 (line 2321): OS3 = Reflection positivity. Confirmed.
- §L.2 (lines 1177--1178): OS2 = Reflection positivity. Confirmed.
- Under the formula §5.7 OS$k$ ↔ §L.2 OS$(k-1)$: $k=3$ gives §L.2 OS$(3-1)$ = OS2. Confirmed.

The exemplar is consistent with both the formula and the preprint text. It correctly anchors the crosswalk in both directions: a reader translating from §5.7 into §L.2 gets OS3 → OS2; a reader translating from §L.2 out to §5.7 gets OS2 → OS3. No ambiguity.

**C2 result: PASS.**

---

## C3 — §H.8 local convention note: WELL-PLACED AND CORRECTLY SCOPED

**Check:** Does the Option (b) note at §H.8 clearly scope to the KK warmup only?

**Evidence verified directly:**

`04-lattice-proof-part1.md` lines 1762--1783 (§H.8 "Step 3: OS Axioms") confirm the third convention: OS1 = Regularity (line 1767), OS2 = Euclidean covariance (line 1770), OS3 = Reflection positivity (line 1774), OS4 = Gauge symmetry (line 1779), OS5 = Cluster decomposition (line 1782). This is neither §5.7 (OS1 = Temperedness, OS3 = RP) nor §L.2 (OS0--OS4, OS2 = RP).

The Wave 4 patch proposes inserting a local note immediately before the §H.8 OS1 line that (i) names the §H.8 convention explicitly, (ii) states that the labeling matches neither §5.7 nor Appendix L, and (iii) scopes the note with the phrase "local to this KK warmup step." The note does not claim to extend Appendix L scope; it does not touch any checkmark line. Option (a) (extending the Appendix L declaration to §H.8) is correctly rejected because §H.8 is not in Appendix L. Option (c) (renumbering §H.8) is correctly rejected as unnecessarily invasive.

The note is structurally non-blocking, self-contained, and appropriately scoped. Placement immediately before the OS1 item at line 1767 is the earliest point at which a reader encounters the convention — correct placement.

**C3 result: PASS.**

---

## C4 — Wave 2 edits (b)--(f) intact and unaffected

**Check:** Do the five per-site edits (b)--(f) remain verbatim-correct and untouched by the Wave 4 patch?

The Wave 4 patch modifies only two targets:
- Edit (a) replacement: the convention-declaration paragraph in `L-clay-conjectures.md` (inserted at the §L.2 section heading, before Lemma L.2.1).
- §H.8 note insertion: a new sentence in `04-lattice-proof-part1.md` before line 1767.

Neither target overlaps with the five per-site edit locations ((b) line 1218, (c) line 1239, (d) line 164, (e) line 2486, (f) line 2535 — all in `L-clay-conjectures.md`).

Verified that all five preprint sites remain in their original (pre-Wave-2-repair) form — none of the proposed edits have been applied to the preprint yet. This is consistent with the patch pipeline: edits are proposed in repair files and applied in a separate editorial pass. The Wave 4 patch explicitly confirms (Suspicion 3) that it does not touch any (b)--(f) line target, and the §H.8 note is in a different file entirely.

Wave 3 independently confirmed edits (b)--(f) as verbatim-correct and self-rescuing (each names the axiom explicitly, insulating against sign errors in the declaration). That confirmation stands: the Wave 4 patch does not perturb those edits.

**C4 result: PASS.**

---

## Summary (≤150 words)

The Wave 4 patch **SURVIVED** all checks. The crosswalk is correctly inverted to OS$(k-1)$: arithmetic verified directly against §5.7 line 2321 (OS3=RP) and §L.2 lines 1177--1178 (OS2=RP). The exemplar sentence is accurate and anchors both translation directions. The §H.8 local convention note is well-placed (immediately before the §H.8 OS1 item), correctly names the three-way divergence, and scopes itself explicitly to the KK warmup — no false claims of Appendix L coverage. Edits (b)--(f) occupy different line targets and a different conceptual layer (per-site disambiguation vs. governing declaration); the Wave 4 changes are orthogonal to them. Both Wave 3 WEAKENED grounds are resolved. No new defects detected.

---

*§J register close: THE INVERSION IS CORRECTED. THE THIRD CONVENTION IS SCOPED. THE FIVE EDITS STAND.*
