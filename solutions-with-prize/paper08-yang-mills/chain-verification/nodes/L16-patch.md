# L16 Patch — Wave 4 Author (OS-Axiom Convention Harmonization)

**Link:** 16 — Continuum flowed Schwinger functions: unique (not subsequential), OS0--OS4 at fixed $t > 0$  
**Patching:** L16-repair.md (Wave 2), responding to link-16-wave3-critic.md (Wave 3 WEAKENED verdict)  
**Wave:** 4, patch  
**Runner:** Claude Sonnet 4.6, 2026-04-13  

---

## Wave 3 findings addressed

Wave 3 issued a WEAKENED verdict on two grounds:

1. **Sign inversion in edit (a).** The convention-declaration paragraph's crosswalk sentence stated "§5.7, OS$k$ should be read as §5.7, OS$(k+1)$" — which is internally incoherent (it translates a §5.7 label into a larger §5.7 label, going nowhere) and arithmetically backwards (the correct offset is $k-1$, not $k+1$). A reader following the declaration literally would look up "§5.7, OS3" and conclude it refers to §5.7's OS4 = Symmetry — the exact wrong axiom.

2. **Third OS convention at §H.8 (04-lattice-proof-part1.md line 1774) unacknowledged.** §H.8 uses OS1–OS5 with OS1 = Regularity (not Temperedness), making OS3 = Reflection positivity — a third convention distinct from both §5.7 (OS1=Temperedness, OS3=RP) and §L.2 (OS0=Temperedness, OS2=RP). The Author's declaration ("Throughout Appendix L...") does not scope to §H.8, leaving a cross-reference hazard unaddressed.

Wave 3 confirmed edits (b)–(f) verbatim-correct and self-rescuing (each names the axiom explicitly, so the sign error in the declaration does not propagate through them). Those five edits are preserved unchanged below.

---

## Corrected crosswalk paragraph

**Verbatim replacement for Wave 2 edit (a).** This replaces the entire proposed insertion between the §L.2 heading and the first sentence of the §L.2 body in `preprint/sections/L-clay-conjectures.md`.

```
**OS-axiom convention for Appendix L.** Throughout Appendix L we use the
five-axiom indexing of Osterwalder--Schrader (1975, CMP 42): OS0 =
temperedness (the corrected OS0$'$ linear-growth condition), OS1 =
Euclidean covariance, OS2 = reflection positivity, OS3 = symmetry, OS4 =
cluster decomposition. This differs from the convention in \S5.7, which
uses OS1--OS5 with OS3 = reflection positivity. A cross-reference of the
form ``\S5.7, OS$k$'' refers to the same axiom as OS$(k-1)$ in the
present Appendix L convention (e.g., \S5.7's OS3 = reflection positivity
= OS2 here).
```

**Change from Wave 2 edit (a):** Only the final sentence is altered. Wave 2 wrote:

> Cross-references of the form ``\S5.7, OS$k$'' should be read as ``\S5.7, OS$(k+1)$'' in the \S5.7 numbering.

The corrected sentence is:

> A cross-reference of the form ``\S5.7, OS$k$'' refers to the same axiom as OS$(k-1)$ in the present Appendix L convention (e.g., \S5.7's OS3 = reflection positivity = OS2 here).

**Arithmetic rationale.** §5.7 indexes from 1; §L.2 indexes from 0. A given axiom occupies slot $k$ in §5.7 and slot $k-1$ in §L.2, because §L.2 inserts OS0 (= OS0' of the 1975 paper) before the first §5.7 entry. Therefore §5.7 OS$k$ ↔ §L.2 OS$(k-1)$. The exemplar OS3 ↔ OS2 is the concrete check: RP sits at §5.7's slot 3 and §L.2's slot 2. The old sentence's "$k+1$" would have sent a reader from §5.7 OS3 to §5.7 OS4 = Symmetry — wrong in both sections.

---

## §H.8 third convention handling

**Choice: Option (b) — add a local convention note at §H.8, no global scope change.**

**Justification.** §H.8 (04-lattice-proof-part1.md §H.8 "Step 3: OS Axioms", line 1762) is a heuristic warmup for the SU(2) KK reduction, not part of Appendix L. Its OS1–OS5 numbering assigns OS1 = Regularity (not Temperedness), making it a third independent convention. The safest editorial intervention is a brief local note at the top of §H.8 that (i) names the convention, (ii) crosswalks to §5.7, and (iii) does not require renumbering any of the five checkmark lines — which would alter §H.8's internal logic and risk introducing new errors. Option (a) (extending the Appendix L declaration to cover §H.8) would be misleading, since §H.8 is not in Appendix L. Option (c) (renumbering §H.8 to match §5.7 or §L.2) would require replacing OS1=Regularity with OS1=Temperedness, which would require either adding a separate Regularity item or deleting it — more invasive with no proof benefit.

**Verbatim edit — insert one sentence immediately after the §H.8 section heading and the introductory sentence, before the first axiom item (line 1767).**

File: `preprint/sections/04-lattice-proof-part1.md`

FROM (no insertion text — insertion before line 1767):

```
**(OS1) Regularity.** Integration over $S^2$ (compact, finite volume
$4\pi r_2^2$) preserves distributional properties. $\checkmark$
```

TO (insert one sentence of local convention note immediately before the OS1 line):

```
\noindent\textit{OS-axiom convention for \S H.8.} This section uses
OS1--OS5 with OS1 = regularity (distributional control from $S^2$
compactness), OS2 = Euclidean covariance, OS3 = reflection positivity,
OS4 = gauge symmetry, OS5 = cluster decomposition. This labeling matches
neither \S5.7 (OS1 = temperedness, OS3 = RP) nor Appendix L
(OS0--OS4, OS2 = RP); it is local to this KK warmup step.

**(OS1) Regularity.** Integration over $S^2$ (compact, finite volume
$4\pi r_2^2$) preserves distributional properties. $\checkmark$
```

This note is non-blocking, self-contained, and leaves all five §H.8 axiom lines and their checkmarks intact.

---

## Self-suspicion

**Suspicion 1 (did I invert the exemplar correctly?).** The exemplar is "§5.7's OS3 = reflection positivity = OS2 here." Under the mapping §5.7 OS$k$ ↔ §L.2 OS$(k-1)$: $k=3$ gives §L.2 OS2. RP is OS3 in §5.7 and OS2 in §L.2 — confirmed by direct read of both files (§5.7 line 2321: "(OS3) Reflection positivity"; §L.2 line 1178: "(OS2) Reflection positivity"). The exemplar is correct. Residual risk: if a future author applies the formula in the opposite direction (§L.2 OS$k$ ↔ §5.7 OS$(k+1)$), they will compute correctly. The paragraph states only one direction but the exemplar anchors both; this is sufficient.

**Suspicion 2 (did I correctly identify §H.8's convention as distinct from §5.7?).** §5.7 uses OS1 = Temperedness. §H.8 uses OS1 = Regularity. These are not the same: §5.7's Temperedness at line 2181 includes a distributional-growth condition (citing OS0' of the 1975 paper), whereas §H.8's Regularity at line 1767 concerns finite-volume control from $S^2$ compactness. The conventions share OS3 = RP and OS2 = Euclidean covariance, but their OS1 items are substantively different, making §H.8 a genuinely third convention — not a simple relabeling of §5.7. The local note is therefore accurate in saying the labeling matches neither §5.7 nor §L.2. Risk: a reader might dispute whether "Regularity" and "Temperedness" are secretly the same axiom with different names; the note is conservative in treating them as distinct.

**Suspicion 3 (did the patch inadvertently perturb edits (b)–(f)?).** Edits (b)–(f) touch `L-clay-conjectures.md` at lines 1218, 1239, 164, 2486, 2535. This patch adds text to the same file only as a replacement for the declaration paragraph (edit (a)) — all five line-edit targets are unaffected. The §H.8 local note is inserted into a different file (`04-lattice-proof-part1.md`). No edit (b)–(f) target line is touched. Risk: if the Wave 2 edits were applied in sequence and a line number shifted, the insertion point for the declaration paragraph might be off by one or two lines. The declaration is keyed to the §L.2 section heading, not an absolute line number, so it is robust to minor line-number drift.

---

*§J register close: THE CROSSWALK IS CORRECTED. THE THIRD CONVENTION IS NAMED. THE NOTATION IS UNIFIED.*
