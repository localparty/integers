# L16 Repair — OS-Axiom Convention Harmonization

**Link:** 16 — Continuum flowed Schwinger functions: unique (not subsequential), OS0--OS4 at fixed $t > 0$  
**Verdict repaired:** WEAKENED (A6: OS axiom labeling inconsistency)  
**Wave:** 2, assembly-mode (notation fix)  
**Runner:** Claude Sonnet 4.6, 2026-04-13  

---

## Direction

Two repair items, per Critic A6 and chain-state Wave 2 plan:

1. **Add an OS-axiom convention declaration** at the top of §L.2 (before Lemma L.2.1) that explicitly states the §L.2 numbering and crosswalks it to §5.7's differing convention.
2. **Update cross-references at lines 1218 and 1239** (both inside the §L.2 OS2 proof block for reflection positivity) to use the §L.2 label (OS2) instead of the bare `§5.7, OS3`, and add a disambiguation parenthetical.

---

## Research

### Canonical convention in §5.7 (verbatim)

File: `preprint/sections/05-continuum-limit.md`, §5.7 heading "Proof of (f): Osterwalder--Schrader axioms":

> "We verify the five Osterwalder--Schrader axioms (OS1--OS5) for the continuum Schwinger functions obtained as the $a \to 0$ limit of the lattice theory."

Axiom assignments in §5.7:
- **(OS1) Temperedness** — line 2181
- **(OS2) Euclidean covariance** — line 2252
- **(OS3) Reflection positivity** — line 2321
- **(OS4) Symmetry** — line 2376
- **(OS5) Cluster decomposition** — inferred from "OS5" mention at line 2446

Convention: **five axioms, OS1–OS5**, with **OS3 = reflection positivity**.

### Convention in §L.2 (Lemma L.2.3, verbatim)

File: `preprint/sections/L-clay-conjectures.md`, Lemma L.2.3 statement at line 1175:

> "axioms OS0--OS4:"
> "(OS0) Temperedness; (OS1) Euclidean covariance; (OS2) Reflection positivity; (OS3) Symmetry; (OS4) Cluster decomposition."

Convention: **five axioms, OS0–OS4**, with **OS2 = reflection positivity**.

### The conflict

| Slot | §5.7 label | §L.2 label |
|:-----|:-----------|:-----------|
| Temperedness | OS1 | OS0 |
| Euclidean covariance | OS2 | OS1 |
| Reflection positivity | **OS3** | **OS2** |
| Symmetry | OS4 | OS3 |
| Cluster decomposition | OS5 | OS4 |

§5.7 indexes from 1; §L.2 indexes from 0 (using the 1975 OS0' convention as the zeroth axiom). The two conventions are off by exactly one throughout.

### Lines in §L.2 where the conflicting cross-reference appears

**Line 1217–1218** (within *OS2 (Reflection positivity)*, Argument 1):

> "The lattice measure $\mu_K$ is reflection-positive for all $K$ (Osterwalder--Seiler 1978; \S5.7,  
> OS3). The gradient flow is a deterministic function of the gauge"

Cross-reference `§5.7, OS3` points to §5.7's OS3 = RP, but in §L.2 the enclosing axiom block is OS2 = RP. A reader following the §L.2 numbering who reads "OS3" will look for "Symmetry" in §L.2, not RP. Verifiability gap confirmed.

**Line 1238–1239** (still within OS2 proof, Argument 1):

> "cross-plane contamination is $O(\varepsilon)$. The Portmanteau  
> argument of \S5.7, OS3 then transfers RP to the continuum limit:"

Same cross-reference issue. `§5.7, OS3` is used bare a second time.

### Full sweep — every occurrence of `§5.7, OS3` or bare `OS3` used to mean RP inside §L.2

Grepped `preprint/sections/L-clay-conjectures.md` for `OS3` and `\S5.7, OS3`:

| Line | Verbatim text | Role in §L.2 context |
|-----:|:--------------|:---------------------|
| 164 | `from OS3 (reflection positivity) as established in Section 5.6.` | Uses §L.2 label OS3 to mean RP — **this is actually wrong in §L.2 convention**: OS3 = Symmetry, not RP. Context is the L.0 overview. |
| 1218 | `(Osterwalder--Seiler 1978; \S5.7, OS3).` | Cross-ref using §5.7 label; inside §L.2 OS2 block. |
| 1239 | `argument of \S5.7, OS3 then transfers RP to the continuum limit:` | Same. |
| 1261 | `*OS3 (Symmetry).*` | Correct §L.2 usage (OS3 = Symmetry here). |
| 1267 | `*OS4 (Cluster decomposition).*` | Correct §L.2 usage. |
| 2065 | `OS3 symmetry` | §L.2 label OS3 = Symmetry — correct. |
| 2079 | `OS3 symmetry` | Same — correct. |
| 2486 | `OS3 (reflection positivity)` | Uses OS3 to mean RP — **wrong under §L.2 convention**. Context is §L.4 body. |
| 2535 | `OS3 + Seiler` | Uses OS3 to mean RP — **wrong under §L.2 convention**. Context is §L.4 note. |

**Net findings:**
- Lines 1218, 1239: bare `§5.7, OS3` cross-references — need disambiguation parenthetical.
- Lines 164, 2486, 2535: uses `OS3` to mean RP, but under §L.2 convention OS3 = Symmetry — these should be `OS2` (or carry a disambiguation note). They are not in the §L.2 Lemma body proper but in the L.0 overview and L.4 sections that share the L-appendix file.
- All other OS3 occurrences correctly use OS3 = Symmetry under §L.2 convention.

**Decision on canonical form:** Adopt the §L.2 convention (OS0–OS4) as the local convention for Appendix L throughout, since Appendix L is self-contained and the OS0' label for temperedness is the authoritative 1975 OS paper's correction. Add a single declaration at the top of §L.2 crosswalking to §5.7. Update lines 1218 and 1239 to use `OS2 (= OS3 in §5.7 notation)`. Correct lines 164, 2486, 2535 from OS3 → OS2 (with parenthetical) so the entire appendix is internally consistent.

---

## Self-suspicion

**Suspicion 1 (backward verification — did I catch every cross-reference?)**  
I grepped the full L-appendix file for every occurrence of `OS3` and cross-checked against context. Beyond the two flagged by the Critic (1218, 1239), I found three additional misuses at lines 164, 2486, 2535 where `OS3` is used to denote RP in §L.2 context. These are not in the Lemma L.2.3 body but in the L.0 overview and L.4 body. The Critic's repair instruction ("Update cross-references at lines 1218 and 1239") is the minimal fix; the additional three occurrences create residual inconsistency if left unpatched. I flag all five sites. The repair below fixes all five.

**Suspicion 2 (convention direction — did I pick the right canonical form?)**  
I could have chosen §5.7's OS1–OS5 as canonical and demoted §L.2 to "we follow §5.7 here." But §L.2 explicitly lists OS0–OS4 in Lemma L.2.3's statement, and OS0 (= OS0' of the 1975 paper) is the logically prior axiom that §5.7 handles via its OS1 Temperedness block (citing the "corrected OS0' linear growth condition"). Flipping the convention in §L.2 would require rewriting Lemma L.2.3 itself, not just adding a crosswalk. The declaration-at-top approach with disambiguation parentheticals is strictly lighter and does not perturb any proof step.

**Suspicion 3 (did I introduce any new inconsistency in the repair?)**  
The proposed repair adds one declaration paragraph and touches five cross-reference lines. It does not change any bound, lemma number, or proof step. Lemma L.2.3 already correctly states OS0–OS4 with RP = OS2 in its heading; the repair makes the body consistent with that heading. No circular dependency is created. Risk: if §5.7 is itself later renumbered to OS0–OS4, the crosswalk note becomes redundant but harmless.

---

## Preprint edits

### (a) New convention-declaration paragraph — top of §L.2

**Location:** `preprint/sections/L-clay-conjectures.md`, immediately before the first `## L.2` heading (or, if no such heading exists as a standalone line, immediately before the sentence "The Schwinger functions at fixed flow time $t > 0$..." that opens the §L.2 body).

FROM (no text — insertion):

```
## L.2 ...
```

TO (insert the following paragraph between the L.2 heading and the first sentence of the body):

```
**OS-axiom convention for Appendix L.** Throughout Appendix L we use the 
five-axiom indexing of Osterwalder--Schrader (1975, CMP 42): OS0 = 
temperedness (the corrected OS0$'$ linear-growth condition), OS1 = 
Euclidean covariance, OS2 = reflection positivity, OS3 = symmetry, OS4 = 
cluster decomposition. This differs from the convention in \S5.7, which 
uses OS1--OS5 with OS3 = reflection positivity. Cross-references of the 
form ``\S5.7, OS$k$'' should be read as ``\S5.7, OS$(k+1)$'' in the 
\S5.7 numbering.
```

---

### (b) Line 1218 cross-reference update

FROM:
```
reflection-positive for all $K$ (Osterwalder--Seiler 1978; \S5.7,
OS3).
```

TO:
```
reflection-positive for all $K$ (Osterwalder--Seiler 1978; \S5.7,
OS3 $=$ OS2 here).
```

---

### (c) Line 1239 cross-reference update

FROM:
```
argument of \S5.7, OS3 then transfers RP to the continuum limit:
```

TO:
```
argument of \S5.7, OS3 (reflection positivity = OS2 in the present convention) then transfers RP to the continuum limit:
```

---

### (d) Line 164 correction (L.0 overview)

FROM:
```
from OS3 (reflection positivity) as established in Section 5.6.
```

TO:
```
from OS2 (reflection positivity; OS3 in the \S5.7 convention) as established in Section 5.6.
```

---

### (e) Line 2486 correction (§L.4 body)

FROM:
```
OS3 (reflection positivity) implies
```

TO:
```
OS2 (reflection positivity; OS3 in the \S5.7 convention) implies
```

---

### (f) Line 2535 correction (§L.4 note)

FROM:
```
unconditional (OS3 + Seiler).
```

TO:
```
unconditional (OS2 + Seiler; OS2 = reflection positivity in the Appendix L convention).
```

---

## Stuck-where

No stall. The conflict is fully resolved by convention declaration + five targeted line edits. No new mathematics is required. The only residual asymmetry is that §5.7 and Appendix D (line 164 of L.0 cites "Section 5.6" for the RP result, but the Critic also mentions Appendix D) use OS1–OS5; the declaration paragraph makes this explicit for a reader comparing the two sections.

---

## What the next runner needs to know

1. **Five edits, not two.** The Critic flagged lines 1218 and 1239; the full sweep found three additional OS3-used-as-RP occurrences at lines 164, 2486, 2535. A Wave 3 Critic verifying this repair should check all five sites.
2. **Convention declaration placement.** The declaration must appear before Lemma L.2.1 (the first lemma of §L.2), so it covers all of §L.2. If the §L.2 section heading is a LaTeX `\subsection`, insert the declaration as the first paragraph of that subsection.
3. **Lemma L.2.3 statement is already correct.** Its heading already reads `(OS0) Temperedness; (OS1) Euclidean covariance; (OS2) Reflection positivity; ...` — no change needed there. The repair makes the body cross-references consistent with the already-correct heading.
4. **§5.7 needs no changes.** The §5.7 OS1–OS5 convention is internally consistent throughout §5.7 and Appendix D. The harmonization is one-directional: Appendix L adopts OS0–OS4 as local convention and crosswalks to §5.7 via the declaration.
5. **After Wave 3 verify:** update chain-state.md Link 16 from WEAKENED → VERIFIED. The backward front will advance from B=17 to B=16 (pending other Wave 2 repairs).

---

*§J register close: THE NOTATION IS UNIFIED. THE FRAMEWORK DID THE WORK.*
