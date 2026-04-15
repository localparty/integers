# Point E1 — The Assembly: Verdict

> **☑ CLOSED 2026-04-10.** All three upstream dependencies listed
> in sub-question (c) below are resolved:
>
> 1. Meyer distributional → point spectrum upgrade for ζ_K (MY4):
>    **bypassed via Route 3** (G's projector — see
>    `research/route3-kms-projector-bypass.md` and
>    `strategy/05-route3-kms-projector-bypass.md`).
> 2. Twisted spectral realization for `L(s, ψ)` (MY3):
>    **Key Lemma B** in `research/meyer-extension-to-K.md`.
> 3. Cohomology-class integrality (BR7/BR8): **Key Lemma C** in
>    `research/cohomology-class-lemma.md`.
>
> Plus the Prop 4.3 [GAP] closed by
> `research/corrected-bridge-table.md`.
>
> The chain is now **11 of 11** at the paper's 11-step framing
> ([THEOREM]: 4, [LEMMA]: 7, [KEY LEMMA — OPEN]: 0, [GAP]: 0).
> Paper 26 Theorem 13.1 is **[THEOREM] conditional on CBB axioms**
> — the same conditional Paper 13 lives with, with no additional
> Meyer or spectral dependency.
>
> **Overall rigor label (post-closure): [LEMMA]** at the GRH step
> (upgraded from [KEY LEMMA — OPEN]); [LEMMA]/[THEOREM] at the
> rank-0 closure.
>
> **Overall verdict (post-closure):** **PASS — chain is
> rigorously complete within the stated scope.**
>
> See `closure-report.md` for the full walkthrough and
> `strategy/05-route3-kms-projector-bypass.md` for the summary.
>
> *r01 verdict preserved below.*

---

**Weight:** HEAVY
**Location in preprint:** §13, §9
**Overall rigor label (r01):** **[KEY LEMMA — OPEN]** at the GRH step;
**[LEMMA]** at the rank-0 closure
**Overall rigor label (post-closure):** **[LEMMA]** at the GRH step (MY4 bypassed);
**[LEMMA]** at the rank-0 closure (unchanged)
**Overall verdict (r01):** Chain is structurally complete but depends on
multiple [KEY LEMMA — OPEN] items upstream
**Overall verdict (post-closure):** Chain is rigorously complete within stated scope

## Sub-question verdicts

- **(a) Chain integrity at the rigor standard.** See
  `rigorous-proof.md` §XII.A for the full chain walk with labels.
  Summary: 7 of 11 steps at [THEOREM]/[LEMMA], 3 at [KEY LEMMA
  — OPEN], 1 at [GAP].

- **(b) Logical structure.** [LEMMA] — The chain is by reduction:
  BC over K → Meyer → Nelson → bridges → cocycle shift → Baker
  → δ = 0 → GRH for L(E, s) → Kolyvagin/GZ → BSD. The structure
  is logically sound. Every link cites a specific proposition.
  The weakest link is at the Meyer-Nelson + twist step (A3) and
  the cohomology-class integrality step (B2).

- **(c) Conditional vs unconditional.** **[LEMMA]** —
  **The proof is conditional on three things**:
  (i) The CBB axioms (per paper's own §9.4 and Theorems 9.1 /
      13.1 framing "conditional on CBB").
  (ii) The three [KEY LEMMA — OPEN] items listed in
       rigorous-proof.md §XIII.
  (iii) The correctness of Propositions 4.2 and 4.3 (bridge
        enumeration, currently broken in 3 of 4 rows per audit
        C5).
  The paper's own framing acknowledges (i) but not (ii) or (iii).

- **(d) What Paper 26 contributes (new vs standard).** See
  rigorous-proof.md §XII.C for the detailed breakdown. The
  genuinely new content is:
  - The bridge family extension from ℚ to ℚ(i).
  - The twisted spectral realization for L(s, ψ) over K.
  - The GRH-to-BSD assembly using classical Kolyvagin / GZ.
  All three have significant gaps in the preprint.

- **(e) Comparison to Connes' programme.** [LEMMA] — Paper 26
  uses the Meyer-Nelson route, which is the classical Connes
  programme approach. Paper 13 v2 (the current RH proof)
  abandoned this route in favor of CCM + ITPFI + Bögli +
  Hurwitz precisely because the Meyer-Nelson upgrade from
  distributional to point spectrum is the classical wall.
  Paper 26 does not address this wall; it asserts the upgrade
  by analogy. The absence of a "CCM over number fields" result
  means Paper 26 cannot adopt the Paper 13 v2 architecture
  directly.

- **(f) Most likely failure point.** Ranked:
  1. **Cohomology-class integrality** (Point B2 / BR7-8). The
     entire bridge mechanism hangs on this. Without it, Baker
     fires on nothing.
  2. **Meyer-Nelson upgrade + twist to L(s, ψ)** (Point A3 /
     MY1-4). The bridge must reach Hecke L-functions, not just
     Dedekind zeta. Not proved.
  3. **Proposition 4.3 broken table** (Point B1 / BR3). The
     worked examples of "minimal conductors" have 3 of 4 rows
     wrong. Fixable, but must be fixed.

## Combined finding

**The assembly is structurally complete.** The 11-step chain is
logically sound. Every step cites a specific proposition. The
downstream classical components (Deuring, Kolyvagin, Gross-Zagier)
are correctly applied.

**But the assembly is only as rigorous as its weakest links**,
and the weakest links are at the novel content (bridge extension,
twisted spectral realization, cohomology-class integrality).
These are where the paper asserts by analogy rather than proves.

The rank-1 case is vacuous per Remark 12.6; the substantive
content is entirely at rank 0. The scope is "BSD at rank 0 for
CM curves with h_K = 1 and CM by one of nine fields, conditional
on the CBB axioms AND the three [KEY LEMMA — OPEN] items."

## Impact on the claimed result

**The claim is not currently established at the yang-mills rigor
bar.** Closing the three [KEY LEMMA — OPEN] items + fixing the
one [GAP] would bring it to a rigorous conditional proof. Without
those fixes, the claim is at the "structurally complete but
rigorously incomplete" stage.

## Action items

1. **[KEY LEMMA — OPEN] closure:** work out Key Lemmas A, B, C
   (see rigorous-proof.md §XIII). Estimated effort: months of
   expert work for A and B; weeks for C.
2. **[GAP] closure:** fix Proposition 4.3 and verify Prop. 4.2.
   Days to weeks of computation.
3. **Editorial fixes:** Ω formula, Table 8.1 values, §10.2
   factorization notation, Heegner field commitment, Remark
   12.6 prominence. Days of writing.
4. **After fixes**, re-rigor-audit. Expected final rigor status:
   conditional proof of BSD at rank 0 for CM curves with
   h_K = 1, conditional on the CBB axioms (Paper 13 inherited).
