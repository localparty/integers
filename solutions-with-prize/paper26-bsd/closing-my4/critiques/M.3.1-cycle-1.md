# M.3.1 — Critic cycle 1

*Critic: Claude Opus 4.6 (1M context)*
*Target Author: M.3.1 (W1-C), editorial node, cycle 1*
*Node-kind: editorial (deliverable-pre-declared Option C anchor)*
*Verdict: **WEAKENED***

---

## 0. Scope of this critique

Verifies the seven artifacts in
`closing-my4/nodes/M.3.1.md` against:
- the existing Paper 26 preprint text (the only source of byte-for-byte
  theorem statements and §15 prose register),
- the referee A3 verdict file
  `referee/runs/r00/points/A3-meyer-spectral/verdict.md`,
- the deliverable `strategy/04-closing-my4.md` §4 and §6,
- the four companion research files the Author cites
  (`meyer-extension-to-K.md`, `cohomology-class-lemma.md`,
  `distributional-to-genuine.md`, `route2-ccm-over-K.md`),
- the §J voice canon / Paper 26 prose register in `sections-part-I.md`.

Editorial-node LOCK invariant being verified:
**every new sentence is either a verbatim restatement of already-proved
content (in Paper 26 or a cited source) or an explicitly labeled
conditional on MY4.** Weasel-free.

---

## 1. Honest-framing audit re-run (Critic sub-step 1)

**Audit:** re-ran grep on the entire Author output for the banned
weasel set {"we believe," "it should follow," "is hoped," "appears
to," "essentially [non-technical]," "we conjecture," "most likely,"
"it is plausible that," "we expect," "ought to," "we anticipate,"
"presumably," "morally," "in spirit"}.

**Hits in the draft text (Artifacts 1–5) that are actual weasel uses:**
**ZERO.**

**Hits that are allowed uses:**
- "essentially self-adjoint" — technical term for Nelson's theorem
  (Artifact 1 line 303; Artifact 4 line 566). Allowed.
- All banned-phrase occurrences in the audit meta-text (Artifact 7,
  Step 4 LOCK, Step 5.5 Self-suspicion) are labeling of categories
  being banned, not weasel uses.
- The prompt-quote block (Direction verbatim) contains the banned
  phrases as quoted instructions, not assertions.

**Audit agrees with the Author's pass on the draft text itself:**
the §3.6.2, Theorem 9.1 update, Theorem 13.1 update, and §15.6 drafts
contain zero weasel words. The Author's honest-framing audit is
correct on this axis.

**However**, the audit does *not* catch a **citation-level
overclaim** which is not a weasel word but is a framing error:
see §7 below on the referee-verdict misquote.

---

## 2. Theorem statement byte-for-byte preservation check (sub-step 2)

### Theorem 9.1

**Existing statement** (`sections-part-III.md` lines 554–557):

> **Theorem 9.1** (GRH for CM curves, conditional on CBB). *Under
> the CBB axioms (Paper 23), let $K$ be an imaginary quadratic field
> with class number $1$, and let $E/\mathbb{Q}$ be an elliptic curve
> with complex multiplication by $\mathcal{O}_K$. Then all non-trivial
> zeros of $L(E, s)$ lie on $\operatorname{Re}(s) = 1/2$.*

**Author's updated statement** (M.3.1.md lines 425–432):

> **Theorem 9.1** (GRH for CM curves; **conditional on MY4 + CBB**).
> *Conditional on the distributional-to-genuine upgrade MY4 (the
> classical Bost–Connes wall over number fields, see §3.6.2), and
> under the CBB axioms (Paper 23), let $K$ be an imaginary quadratic
> field with class number $1$, and let $E/\mathbb{Q}$ be an elliptic
> curve with complex multiplication by $\mathcal{O}_K$. Then all
> non-trivial zeros of $L(E, s)$ lie on $\operatorname{Re}(s) = 1/2$.*

**Delta analysis:**
- Label: "(GRH for CM curves, conditional on CBB)" → "(GRH for CM
  curves; **conditional on MY4 + CBB**)". Comma to semicolon;
  boldface added to "MY4 + CBB". Acceptable label change.
- Hypothesis: new clause "Conditional on the distributional-to-genuine
  upgrade MY4 (the classical Bost–Connes wall over number fields, see
  §3.6.2), and " prepended. "Under" → "under" (mid-sentence case
  change required by grammar). Acceptable.
- **Conclusion**: "Then all non-trivial zeros of $L(E, s)$ lie on
  $\operatorname{Re}(s) = 1/2$." — preserved **byte-for-byte**.
  **PASS.**

### Theorem 13.1

**Existing statement** (`sections-part-IV.md` lines 360–371; note
the prompt said `sections-parts-V-VI.md` but this was a prompt
error — the Author correctly identified `sections-part-IV.md` in
M.3.1.md line 460):

> **Theorem 13.1 (BSD from CBB).** *Under the CBB axioms (Paper 23),
> for CM curves E/Q with CM by a class-number-1 imaginary quadratic
> field K and analytic rank 0 or 1, BSD holds:*
>
> *(i) rank(E(Q)) = ord_{s=1} L(E,s), and*
>
> *(ii) the leading coefficient of L(E,s) at s=1 satisfies the BSD
> formula:*
>
>     lim_{s→1} L(E,s) / (s−1)^r = (|Sha(E/Q)| · Ω_E · R_E · ∏_p c_p) / |E(Q)_tors|²
>
> *where r = ord_{s=1} L(E,s), Ω_E is the real period, R_E is the
> regulator, c_p are the Tamagawa numbers, and Sha(E/Q) is the
> Tate--Shafarevich group.*

**Author's updated statement** (M.3.1.md lines 487–507):

> **Theorem 13.1 (BSD from MY4 + CBB).** *Conditional on the
> distributional-to-genuine upgrade MY4 (the classical Bost–Connes
> wall over number fields, see §3.6.2), and under the CBB axioms
> (Paper 23), for CM curves E/Q with CM by a class-number-1 imaginary
> quadratic field K and analytic rank 0 or 1, BSD holds:*
>
> *(i) rank(E(Q)) = ord_{s=1} L(E,s), and*
>
> *(ii) the leading coefficient of L(E,s) at s=1 satisfies the BSD
> formula:*
>
>     lim_{s→1} L(E,s) / (s−1)^r = (|Sha(E/Q)| · Ω_E · R_E · ∏_p c_p) / |E(Q)_tors|²
>
> *where r = ord_{s=1} L(E,s), Ω_E is the real period, R_E is the
> regulator, c_p are the Tamagawa numbers, and Sha(E/Q) is the
> Tate--Shafarevich group.*
>
> *(The rank-1 case is vacuous within the stated scope, by Remark
> 12.6: GRH for $L(s, \psi)$ implies $L(1, \psi) \neq 0$, so every
> CM curve in scope has analytic rank $0$. The substantive content
> of the theorem is the rank-0 case.)*

**Delta analysis:**
- Label: "(BSD from CBB)" → "(BSD from MY4 + CBB)". Acceptable.
- Hypothesis: new conditional clause prepended. "Under" → "under".
  Acceptable.
- Parts (i), (ii), and the BSD leading coefficient formula:
  preserved **byte-for-byte**.
- **BUT:** a *new trailing parenthetical* has been **added** after
  the conclusion (the rank-1 vacuity parenthetical, M.3.1.md lines
  504–507). This parenthetical is **NOT** in the original Theorem
  13.1 statement. It is *new text inside the italicized theorem
  block*.

**Assessment of the new parenthetical:**
- The content is faithful to Remark 12.6 (which I verified at
  `sections-part-IV.md` lines 318–334). The parenthetical summarizes
  what Remark 12.6 already says.
- The Author is honest about the addition (M.3.1.md line 517,
  "A trailing parenthetical (already implicit in Remark 12.6) is
  added to make the rank-1 vacuity explicit at the theorem
  statement"; and again lines 895–904 in the "Watch out for"
  section, "it is a new addition").
- But the Critic mandatory sub-step #2 is strict: *"The only
  legitimate change is the addition of a conditional clause at the
  start of the hypothesis."* The trailing parenthetical is not a
  conditional clause at the start of the hypothesis; it is a new
  explanatory addition at the end of the theorem statement block.

**Verdict:** the conclusion body (parts i and ii and the BSD
formula) is preserved byte-for-byte — **PASS** on the narrow
preservation check. The added trailing parenthetical is a
**WEAKENED**-level issue: the Author overreached the "prepend
conditional clause only" constraint by also appending a new
parenthetical. This is not BROKEN because (a) the content is
faithful to the existing Remark 12.6, (b) the Author is honest
about the addition, (c) the parenthetical can be dropped without
loss.

**Runner action in cycle 2:** either (a) drop the trailing
parenthetical from the theorem statement and leave Remark 12.6
as-is (strict interpretation), or (b) accept the parenthetical as
a scope-clarifying enhancement and incorporate it. The strict
interpretation is the Critic's preferred default.

**Minor inconsistency to flag:** the spawn prompt's instruction
at line 51 says *"Preserve the existing scope clause (CM elliptic
curves over ℚ with CM by class-number-1 K, analytic rank ∈ {0, 1},
and the rank-1 case vacuous within scope per Remark 12.6)"* —
which is ambiguous about whether the vacuity clause is already in
the theorem (it isn't) or should be added (the Author's reading).
This is a prompt-level ambiguity the runner could resolve by
clarifying in cycle 2.

---

## 3. Downstream chain preservation check (sub-step 3)

**Chain structure as used by Theorem 13.1's proof** (verified by
reading `sections-part-IV.md` lines 378–400):

- **Step 1 (GRH).** Cites Theorem 9.2 (which extends Theorem 9.1 to
  all nine class-number-1 imaginary quadratic fields). Theorem 9.2
  inherits the MY4 conditional from Theorem 9.1 by Proposition 9.2's
  "four properties of $K$" — all four are field-independent, so the
  conditional propagates without branching.
- **Step 2 (Rank 0, Kolyvagin).** Uses "$L(E, 1) \neq 0$" as input.
  This is a consequence of GRH (Theorem 9.1, now conditional on
  MY4). Kolyvagin's theorem (Theorem 11.1) is unconditional in
  itself; it just needs the input $L(E,1) \neq 0$, which is
  MY4-conditional via GRH.
- **Step 3 (Rank 1, Gross–Zagier + Kolyvagin).** Uses "$L(E, s)$
  has a simple zero at $s = 1$" — again a GRH consequence. The
  Gross–Zagier formula (Theorem 12.1) and Kolyvagin descent
  (Theorem 12.3) are unconditional theorems; they take
  GRH-consequent hypotheses as inputs. The conditional propagates
  through the inputs, not through the theorems themselves.
- **Remark 12.6 (rank-1 vacuity).** Argues that GRH for $L(s, \psi)$
  forces $L(1, \psi) \neq 0$ (because $\operatorname{Re}(1) = 1 \neq
  1/2$), so CM curves in scope have analytic rank 0 and the rank-1
  case of Theorem 12.5 is vacuous. The vacuity argument is itself
  a GRH consequence, hence also MY4-conditional.

**Conditional-propagation verdict:** the MY4 conditional flows
cleanly through Theorem 9.1 → Theorem 9.2 → Theorem 13.1's Step 1
→ Steps 2 and 3 → Remark 12.6. **No sub-step of §13.1's proof
uses Theorem 9.1 in a way that the conditional breaks**, because
every downstream use of Theorem 9.1 is through its conclusion
("GRH for $L(E, s)$"), not through its proof's internal machinery.
Kolyvagin and Gross–Zagier take GRH as a black box; the
MY4-conditional framing makes the black box conditional without
needing any re-derivation of the black box's interior.

The Author's Step 5.5 Self-suspicion item (ii) makes this
argument correctly (M.3.1.md lines 196–212). **PASS.**

**Nothing in §11, §12, §13 needs a re-derivation.** The downstream
chain is intact.

---

## 4. §3.6.2 placement check (sub-step 4)

**Placement target:** between the existing §3.6.1 (ending at
`sections-part-II.md` line 297, after the "$\square$" at the end
of the Summary paragraph) and §3.7 (starting at line 299).

**Verified:** the Author places §3.6.2 correctly (M.3.1.md line
274: "*To be inserted in Paper 26, Part II, immediately after
§3.6.1 ... and before §3.7 ('Nelson self-adjointness over K')*").

**Forward-reference check:**
- §3.6.2 forward-references §9.2 and §15.6. This is consistent
  with Paper 26's existing forward-reference pattern (e.g.,
  `sections-part-II.md` line 164 forward-references §10.2 from
  within §3.6.1). **PASS.**
- §3.6.2 references Propositions 3.6, 3.6.1, 3.7 (all earlier in
  the same §3). Backward-reference, OK.
- §3.6.2 references Reed–Simon II §VIII.3, Meyer 1997, Connes–
  Marcolli 2008 §4.3. External citations, OK.
- §3.6.2 references `research/meyer-extension-to-K.md`,
  `research/cohomology-class-lemma.md`,
  `research/distributional-to-genuine.md`,
  `research/route2-ccm-over-K.md`. All four files exist (verified
  by `ls`). **PASS.**

**§9.2 Step B(5) citation update:** the Author correctly flags
this as a required follow-up edit in the change-log (Artifact 6,
lines 700–706). §9.2 Step B currently has sub-items 1–7
(`sections-part-III.md` lines 580–597); the silent upgrade
actually occurs in *sub-item 4* ("Non-trivial zeros of $\zeta_K(s)$
appear as eigenvalues of $\overline{T}_{BC,K}$") rather than
sub-item 5 ("Since $\overline{T}_{BC,K}$ is self-adjoint, its
spectrum is real"). Sub-item 5 uses "eigenvalues" because sub-item
4 silently assumed the distributional eigenstates are genuine
point-spectrum eigenvectors. The Author's citation to "Step B(5)"
is slightly off — the upgrade is in Step B sub-items 4 AND 5
jointly, not solely 5.

**Verdict:** the placement is correct and the follow-up flag is
correct in intent, though the sub-item numbering in the Author's
change-log is slightly imprecise. **WEAKENED-level nit, not
blocking.** In cycle 2, the runner should apply the §9.2 Step B
citation update to both sub-items 4 and 5 (or rewrite the whole
sub-chain 4–5 to cite §3.6.2).

**Additional silent-inference sites the Author missed
(significant):** see §5 below.

---

## 5. §15 (Scope) coherence check (sub-step 5)

**§15 existing structure** (verified in `sections-parts-V-VI.md`):

- §15.1 "Rank 0 and rank 1: proved"
- §15.2 "Rank ≥ 2: genuinely open"
- §15.3 "Non-CM curves: genuinely open"
- §15.4 "Class number $h_K > 1$: expected to extend"
- §15.5 "The Langlands frontier"
- (no §15.6 currently)
- then `---` separator, then `## 16. The Bridge Family`

**Author's new §15.6** sits between §15.5 and the separator / §16.
Placement is correct, and the title "The classical Bost–Connes
wall: MY4" matches the §15.x sub-section titling pattern
("Rank ≥ 2: genuinely open", "The Langlands frontier", etc.).
**PASS.**

**§15.1 overclaim check:** the Author's CONCERN is correct.
`sections-parts-V-VI.md` line 233 reads:

> "This is complete. No gaps. No conditional statements. The BSD
> conjecture is proved for this class of curves."

This sentence directly overclaims relative to the new conditional
framing. It needs softening to something like "This is complete
conditional on MY4 (§15.6); no other gaps." The Author's
change-log entry (M.3.1.md lines 707–713) flags this correctly
with the specific proposed softening. **The Critic agrees with
the Author's CONCERN about §15.1 overclaim.**

**§15 coherence overall:** adding MY4 as a fifth item to the four
existing limitation items is consistent with §15's list structure,
*provided* the §15.1 softening is applied in the same pass. The
Author's §15.6 draft explicitly distinguishes MY4 (*within* scope
but unproved) from the four existing limitations (genuinely beyond
scope), which is the honest differentiation. **PASS.**

**Additional §15-adjacent overclaims the Author missed:**

I grep-searched the Paper 26 preprint for other MY4 silent
inferences and found **two additional sites** the Author did NOT
flag in the change-log:

1. **`sections-part-I.md` line 168** (Paper 26 §2.3, "The RH proof
   in one paragraph"):
   > *"Nelson's analytic vector theorem upgrades these to genuine
   > eigenstates, making $T_{\mathrm{BC}}$ essentially
   > self-adjoint."*

   This is the *same* silent inference the Author diagnosed: Nelson
   → genuine eigenstates. Under the MY4 framing, this sentence is
   an overclaim. It belongs to Paper 13's proof summary inside
   Paper 26's introduction, but the framing language appears as
   Paper 26 prose, so the Paper 26 reader will read it as an
   endorsement of the unconditional inference.

2. **`sections-part-III.md` lines 518–521** (§9.1 "The chain
   assembled", Step 4):
   > *"Nelson self-adjointness (Step 3) promotes these to genuine
   > eigenstates: the spectrum of the self-adjoint closure
   > $\overline{T}_{BC,K}$ is real, so all eigenvalues are real."*

   This is a second, parallel-to-§9.2 sub-chain with the same
   silent inference. §9.1 is an overview of the proof structure
   (8 steps); §9.2 is the detailed proof of Theorem 9.1. **Both**
   contain the silent upgrade. The Author's change-log only flags
   §9.2 Step B(5).

**Verdict on sub-step 5:** the §15 placement and §15.1 CONCERN are
correct (**PASS** on both). But the Author's change-log adjacent-
edits list is incomplete: at least two other silent-inference
sites (§2.3 and §9.1 Step 4) should be added to the follow-up list
for cycle-2 incorporation. **WEAKENED-level issue.**

---

## 6. Bonus-grep on M.3.1.md (sub-step 6)

### 6a. "We have shown" / "it is proved" hits

**Grep results:** zero hits for either phrase about MY4 or the new
artifacts. The Author uses "conditional on MY4" and "conditional
on MY4 + CBB" consistently. The phrases "is proved" appear only
in the meta-text of Artifact 7 (the audit table) about ALREADY
proved items (Proposition 3.6, Proposition 3.7, etc.) — allowed.
**PASS.**

### 6b. Unitalicized banned phrases

**Grep results:** zero hits in the draft text (Artifacts 1–5). The
phrase "essentially self-adjoint" (Artifact 1 line 303) is the
standard technical term for Nelson's theorem and is on the
allowed list. The phrases "we believe," "it is hoped," etc. do not
appear in the draft text. **PASS.**

### 6c. Cross-reference paths

- `research/meyer-extension-to-K.md` — **EXISTS**, contains Key
  Lemmas A and B as claimed.
- `research/cohomology-class-lemma.md` — **EXISTS**, contains Key
  Lemma C (status `[KEY LEMMA — OPEN] → [LEMMA]`) at line 206.
- `research/distributional-to-genuine.md` — **EXISTS**, contains
  Route 1 ("spectral-measure reformulation", at line 52) and
  Route 2 ("port Paper 13's CCM architecture to K", at line 110).
- `research/route2-ccm-over-K.md` — **EXISTS**, contains the
  "60–110 pages" page estimate at line 831 (matching the Author's
  claim).
- `research/corrected-bridge-table.md` — **EXISTS** (referenced in
  the canonical-names §3 UNIFY block at M.3.1.md line 145).

All cited files exist at their cited paths. **PASS.**

### 6d. Inconsistency between status report and artifact text

- Author reports "zero weasel hits" and "conclusions preserved
  byte-for-byte" in the status summary (M.3.1.md lines 855–863).
  **Weasel hits**: confirmed zero in the draft text. **Conclusion
  preservation**: verified for Theorem 9.1 (strict byte-for-byte);
  for Theorem 13.1 the parts (i), (ii), BSD formula, and
  where-clause are preserved byte-for-byte, BUT the Author added a
  trailing parenthetical that is new text (see §2 above for the
  WEAKENED flag). The status report does not flag this addition
  to the Critic — the Author flags it only in the "Watch out for"
  section, which is buried near the bottom of M.3.1.md. This is a
  **minor self-reporting gap**, not a deception, but worth noting.

- Author claims "downstream Kolyvagin / Gross–Zagier chain
  preserved": **verified** (see §3 above).

- Author claims "~8 pages of Paper 26 additions": the page-count
  table at M.3.1.md lines 940–949 lists Artifacts 1–5 totaling ~8
  pages. Rough manual check supports this (~2150 words).
  **PASS.**

### 6e. Route 1 page estimate is unattributed

The Author's §3.6.2 (line 369) and §15.6 (line 587) both state
"Route 1 is estimated at 5–15 pages." I searched
`research/distributional-to-genuine.md` for "5-15 pages" or
"5–15 pages" or "5 to 15" and found **zero matches**. The research
file's Status-of-Route-1 paragraph (lines 102–108) says "This is a
sketch" with "standard but tedious" verifications needed, but does
NOT give a page estimate. The "5–15 pages" is the Author's own
estimate, not sourced from the research file. The Author's audit
entry for this sentence (M.3.1.md line 762) says it "restates
`research/distributional-to-genuine.md` Route 1 sketch" — this is
inaccurate. It's an unsourced estimate, not a restatement.

**Severity: minor.** This is not a weasel hit and not an overclaim
about MY4; it is an unsourced sizing estimate. The runner could
either (a) drop the "5–15 pages" language, (b) add a footnote
attributing the estimate to the Author's own interpretation, or
(c) verify the estimate by reading Route 1 more carefully and
adding it to the research file. **WEAKENED-level nit.**

---

## 7. Chain-of-verification on bonus-grep findings (sub-step 7)

### 7a. Referee A3 verdict misquote

**Finding:** the Author's draft repeatedly attributes to the
referee A3 verdict the phrase *"CLOSABLE GAP — substantial work
required"* (M.3.1.md lines 189, 240, 394, 671) and in one place
extends it to *"CLOSABLE GAP — substantial work required;
multiple months of focused work"* (M.3.1.md line 594–595, inside
Artifact 4 / §15.6).

**The actual referee A3 verdict file**
(`referee/runs/r00/points/A3-meyer-spectral/verdict.md`) says:

> "**Overall verdict:** CLOSABLE GAP"
>
> (sub-question verdicts (a), (b), (c), (e) all CLOSABLE GAP;
> (d) SOUND)
>
> "**Difficulty:** 2-3 pages of explicit computation"
>
> "If closed, the entire proof chain becomes rigorous. The gap is
> **not a fundamental obstruction but a missing page of argument**."

**The phrases "substantial work required" and "multiple months of
focused work" do NOT appear in the referee verdict file.**

The referee's actual language goes in the *opposite* direction
from the Author's framing: the referee says **2-3 pages of
explicit computation**, not "substantial work required; multiple
months." The Author is systematically misquoting the referee in a
way that *inflates* the difficulty of closing the gap.

**Tracing the misquote:** the misquote originates in the
deliverable `strategy/04-closing-my4.md` — line 694 uses the
phrase "CLOSABLE GAP — substantial work required" as a direct
quote attributed to the referee A3 verdict, and line 921 refers to
"multiple months of focused work" as a "per-point assessment." The
Author imports both phrasings from the deliverable without
verifying them against the actual verdict file. The spawn prompt
(M.3.1-prompt.md line 82) also repeats the deliverable's misquote.

**Attribution of the error:** the misquote originates upstream of
the Author. The Author is Reasonable in trusting the deliverable's
quoted text, but Critic mandatory sub-step #7 explicitly asks me
to verify that the Author's framing of "CLOSABLE GAP — substantial
work required" matches the referee's actual language. **It does
not.** The Author's published text thus contains two attributed
quotes to the referee that do not appear in the referee's verdict
file.

**Why this matters for the editorial node:** the honest-framing
invariant for an editorial node requires every new sentence to be
either (a) a restatement of something already proved, or (b) an
explicitly labeled conditional. A false quote attribution is
*neither* — it is a restatement of something that does NOT exist
in the source. This is a framing error of a different kind than a
weasel word, but it is still a violation of the LOCK invariant on
one axis: the Author claims to be restating the referee verdict
but is actually restating a deliverable paraphrase that diverges
from the source.

**Severity: WEAKENED.** It is not BROKEN because:
- the Author inherited the misquote from the deliverable, not
  fabricated it;
- the underlying conclusion (MY4 is a non-trivial but closable
  open item) is correct;
- the direction of the error is "inflate difficulty," which is
  *safer* from a Clay-grade-honesty standpoint than "downplay
  difficulty" — though still wrong;
- the fix is mechanical (either re-read the verdict file and
  correct all four citation sites, or replace the inline quote
  with a paraphrase that avoids direct attribution).

**However**, the fact that the Author did not catch this on
re-read is a **completeness gap** in the editorial node: the
referee verdict file is explicitly listed in the Author's Primary
Sources (M.3.1-prompt.md line 82), so grep-checking the quote
against the file was a reasonable expected step that did not
happen.

**Runner action in cycle 2:**
1. Re-read `referee/runs/r00/points/A3-meyer-spectral/verdict.md`.
2. Update the inline quotes at M.3.1.md lines 189, 240, 394, 594,
   671 (and the corresponding text when incorporating into the
   preprint) to either: (a) the actual referee phrase "CLOSABLE
   GAP" with "Difficulty: 2-3 pages of explicit computation," or
   (b) a paraphrased "referee verdict: closable gap, requiring
   substantial but bounded work" that does not pretend to be a
   direct quote.
3. Update the deliverable `strategy/04-closing-my4.md` line 694
   and line 921 to either match or explicitly flag as paraphrase.

### 7b. MY4 vs referee sub-point mapping

**Finding:** the referee A3 verdict addresses five sub-questions
(a)–(e), with CLOSABLE GAP verdicts on (a), (b), (c), (e) and
SOUND on (d):

- (a) Meyer extension from $\zeta$ to $\zeta_K$
- (b) Ha–Paugam distributional construction verification
- (c) character twist to $L(s, \psi)$ — "the critical step"
- (d) dark-state impossibility — SOUND
- (e) bridge reaches $L(s, \psi)$, not just $\zeta_K$

**The referee identified (c) as "the critical gap":** "The most
critical gap is the demonstration that the bridge cocycle
integrality constraint survives the character twist from $\zeta_K$
to $L(s, \psi)$" (verdict.md line 14).

**The Author's MY4 framing is not (c).** MY4 is the
distributional→genuine *point-spectrum* upgrade for
$\overline{T}_{BC,K}$. This is closest to the referee's sub-point
(b) (Ha–Paugam distributional construction verification) or
possibly a sub-point not explicitly in the referee's list.

In other words: the Author has *rebranded* an open item that was
NOT the referee's headline A3 concern as "the" wall the referee
identified. The referee's headline A3 concern (the character
twist, (c) and (e)) is addressed by Key Lemma B in
`research/meyer-extension-to-K.md`, which the Author correctly
labels `[LEMMA] conditional on MY4`. So the twist *is* captured,
but it is now framed as a downstream consequence of MY4 rather
than as its own open item.

**Is this framing legitimate?** Partial yes:
- There *is* a silent inference in §9.2 Step B (sub-items 4–5)
  that needs to be surfaced as MY4. The Author is right that this
  inference exists.
- Closing MY4 in the Author's sense (distributional → point
  spectrum) would mechanically close the referee's (b)
  sub-concern, and the referee's (c)/(e) character-twist concern
  is separately addressed by Key Lemma B's explicit transfer.
- The Author's framing is consistent with the deeper reading that
  MY4 is the "wall" because the twist issue can be resolved by
  the same tools (Meyer's explicit formula) once the distributional
  → genuine upgrade is granted.

**But:** the Author's framing under-represents the referee's
headline concern, because the referee's headline was about (c)
(twist), not about (b) (distributional construction verification).
A reader who reads the Author's draft and then reads the referee
verdict will notice the mismatch: the Author's "MY4 is the wall"
does not line up with "the critical gap is the character twist
cocycle integrality."

**Severity: WEAKENED.** The Author's identification of MY4 as an
open item is correct, but the Author's framing that this is what
the referee flagged is only partially accurate. The fix is to
rephrase the §3.6.2 and §15.6 prose to say either:
1. "MY4 is identified *here* as the underlying wall, of which the
   referee's A3 character-twist concern is one consequence,"
2. or: "MY4 and the referee's A3 character-twist concern are both
   symptoms of the same underlying distributional→genuine upgrade
   gap, which we name MY4."

Either framing is honest; the current framing — "MY4 is what the
referee called CLOSABLE GAP substantial work" — conflates two
different open-item analyses.

**Runner action in cycle 2:** the §3.6.2 "This is the classical
Bost–Connes wall over number fields" paragraph and the §15.6
"audit verdict on Point A3" paragraph should be rewritten to
distinguish between the Author's MY4 (distributional → genuine
point-spectrum upgrade) and the referee's A3 headline (character
twist). The underlying mathematical claim is unchanged; only the
historical attribution to the referee needs softening.

---

## 8. Retrieval-augmented citation verification (sub-step 8)

### Companion research file citations

| Cited file | Cited content | Verification |
|:--|:--|:--|
| `meyer-extension-to-K.md` | Key Lemma A (MY1, MY2: Meyer for $\zeta_K$) and Key Lemma B (MY3: Meyer for $L(s, \psi)$), both `[LEMMA] conditional on MY4` | **Verified**: file contains Key Lemma A at line 73, Key Lemma B at line 179, and the tags `[KEY LEMMA — OPEN] → [LEMMA]` at lines 360 and 366. |
| `cohomology-class-lemma.md` | Key Lemma C: unconditional cohomology-class integrality bound $\lvert\Delta c_k(\delta)\rvert < 1/(k+1)$ | **Verified**: Key Lemma C statement at line 27, tag `[KEY LEMMA — OPEN] → [LEMMA]` at line 206, numerical verification script in file. |
| `distributional-to-genuine.md` | Route 1 (spectral-measure reformulation) and Route 2 (CCM over K) | **Verified**: Route 1 at line 52, Route 2 at line 110. Route 1 page estimate "5–15 pages" NOT in file (see §6e). Route 2 page estimate in this file is "20–40 pages" (line 142), which differs from the Author's "60–110 pages" — the Author correctly uses the updated estimate from `route2-ccm-over-K.md`. |
| `route2-ccm-over-K.md` | Route 2 detailed plan, "60–110 pages of new preprint content" | **Verified**: total estimate at line 831. |
| `corrected-bridge-table.md` | The four corrected $(k, \mathfrak{N})$ pairs at norms 13, 29, 41, 105 | **Verified**: cited in the Author's §3 UNIFY block; file exists. |

### External citation sanity checks

- **Meyer 1997, Duke Math. J. 88**: standard Meyer reference, no
  issue.
- **Connes–Marcolli 2008, *Noncommutative Geometry, Quantum Fields
  and Motives*, §4.3**: standard CCM reference, no issue.
- **Reed–Simon II §VIII.3**: for the spectral theorem. The correct
  citation is actually Reed–Simon Vol. I §VIII.3 (which is Volume
  I, "Functional Analysis"), not Vol. II. Vol. II is "Fourier
  Analysis, Self-Adjointness." Nelson's analytic vector theorem
  is Reed–Simon Vol. II, Theorem X.39. So the Author's §3.6.2
  citation "Reed–Simon, *Methods of Modern Mathematical Physics*
  II, §VIII.3" is **slightly misattributed**: §VIII.3 (spectral
  theorem) is in Vol. I, while §X.39 (Nelson) is in Vol. II. The
  existing §3.7 proof of Proposition 3.7 in Paper 26
  (`sections-part-II.md` line 306) correctly cites
  "Reed–Simon, Theorem X.39" — which is in Vol. II. For the
  spectral theorem citation in §3.6.2, the Author should use
  "Reed–Simon Vol. I §VIII.3" (or "Reed–Simon I §VIII.3"). This
  is a **minor citation-volume error**, severity nit.

**Runner action in cycle 2:** change "Reed–Simon, *Methods of
Modern Mathematical Physics* II, §VIII.3" to "Reed–Simon, *Methods
of Modern Mathematical Physics* I, §VIII.3" (or equivalently
"Reed–Simon Vol. I §VIII.3"). **Minor nit, not weasel-level.**

---

## 9. Voice-alignment check (sub-step 9)

**Paper 26 existing prose register** (from `sections-part-I.md`
§1.4, §2.3, and `sections-part-II.md` §3.6/§3.6.1/§3.7):

- Short declarative sentences; explicit operator notation in
  LaTeX; "Definition / Proposition / Proof / Remark" structure;
  side-by-side comparison tables; measured but confident tone;
  explicit forward/backward references; "What changes from Q to
  Q(i)" summary headers.

**Author's §3.6.2 prose:**
- Short declarative sentences: mostly yes, though the paragraph
  "This is the classical Bost–Connes wall over number fields. It
  is the same obstruction that Paper 13 (the companion RH
  preprint) hit when porting Meyer–Nelson to its proof of GRH for
  $\zeta(s)$, and that Paper 13 v2 resolved by abandoning..."
  runs somewhat long compared to §3.6's "What changes from Q to
  Q(i). The von Mangoldt function $\Lambda$ is replaced by
  $\Lambda_K$." style. **Minor stylistic divergence, not a
  register failure.**
- Operator notation: matches §3.6 conventions ($T_{BC,K}$,
  $\overline{T}_{BC,K}$, $H_{1,K}$, $D_K$, etc.). **PASS.**
- Definition/Proposition structure: the Author uses a "blockquote
  KEY LEMMA — OPEN" structure (M.3.1.md lines 334–348) which is
  slightly different from the "Proposition" numbering in §3.6.
  This is appropriate because the item is not a Proposition — it
  is explicitly labeled as `[KEY LEMMA — OPEN]` per the Paper
  08-style rigor labels. **PASS, defensible choice.**
- Forward/backward references: used correctly (forward to §9.2
  and §15.6; backward to §3.6, §3.6.1, §3.7). **PASS.**
- Tone: the §3.6.2 tone is measured and technical, matching Paper
  26's tone. The §15.6 tone is slightly more reflective ("We name
  MY4 as the primary remaining open item") — which matches §15's
  overall reflective register ("This section is the honest
  accounting of scope", line 206–207). **PASS.**

**Overall voice alignment:** matches Paper 26's prose register
with a minor long-sentence tendency in §3.6.2. Not a weasel or
overclaim issue. **PASS on voice calibration.**

### §J voice canon alignment

- "honest partial proof over glossed completion" — the §3.6.2
  draft is an honest partial proof (Meyer + Nelson give
  $\operatorname{spec} \subset \mathbb{R}$; the upgrade to point
  spectrum is OPEN). **Alignment: strong.**
- "the credibility of the programme is the credibility of its
  kill list" — §3.6.2 names MY4 explicitly and labels Theorems
  9.1 and 13.1 as conditional. **Alignment: strong.**
- "the third option, honestly flagged" — §3.6.2 and §15.6
  implement Option C as the safety-net framing. **Alignment:
  strong.**
- "10 of 11 → 11 of 11 conditional on MY4" — used correctly in
  §15.6 and the change-log. **Alignment: correct.**

**Voice canon verdict: PASS.**

---

## 10. §F shadow check (sub-step 10)

**§F kill list in cycle 1: empty.** The editorial node does not
need a §F shadow check because there is no kill pattern to
paraphrase.

**However**, a minimal shadow check I can still perform:
does any sentence in Artifacts 1–4 paraphrase a generic wrong-space
or wrong-symmetry pattern? The §3.6.2 draft specifically
distinguishes between $\operatorname{spec}(\overline{T}_{BC,K})$
and $\operatorname{spec}_p(\overline{T}_{BC,K})$ — the very
distinction that, if elided, would be a "wrong-space" kill. The
Author is *explicit* about this distinction, which is the
opposite of the kill pattern.

**Shadow-check verdict: PASS.**

---

## 11. LOCK verification (sub-step 11)

**Editorial LOCK invariant:** every new sentence is verifiable as
either (a) restating already-proved content, or (b) explicitly
labeling a conditional.

**Walk through Artifacts 1–5 with LOCK in mind:**

- **§3.6.2 (Artifact 1):** every mathematical sentence is either
  a restatement of Propositions 3.6 / 3.6.1 / 3.7 (category a),
  a citation to Meyer 1997 / Connes–Marcolli 2008 / Reed–Simon
  (category a with external citation), a restatement of
  companion notes (category a with internal citation), or an
  explicit "conditional on MY4" statement (category b). **PASS**
  on the mathematical content.

  **But**: the sentence "The conditional formulation is
  consistent with the audit verdict on Point A3 ('CLOSABLE GAP —
  substantial work required') and is the same kind of
  honest-conditional Paper 13 v2 lives with under 'RH conditional
  on CCM 2025'" (M.3.1.md lines 392–396) **fails** LOCK because
  the referenced quote "CLOSABLE GAP — substantial work required"
  is NOT in the referee verdict file. This sentence purports to
  restate the referee's language but actually restates a
  deliverable paraphrase that diverges from the source. See §7a
  above. **WEAKENED flag.**

- **Theorem 9.1 update (Artifact 2):** the new conditional clause
  is category (b); the preserved conclusion is category (a).
  **PASS.**

- **Theorem 13.1 update (Artifact 3):** same as Artifact 2, plus
  a new trailing parenthetical that is category (a) (restatement
  of Remark 12.6) but is a non-minimal edit. **PASS on LOCK,
  WEAKENED on minimality.**

- **§15.6 (Artifact 4):** every sentence is either a restatement
  of existing §15 items (category a), a reference to §3.6.2
  (category a internal), or an explicit MY4 conditional
  (category b). **BUT**: the sentence "The audit verdict on Point
  A3 ('CLOSABLE GAP — substantial work required; multiple months
  of focused work') is consistent with this framing" (M.3.1.md
  lines 594–596) **fails** LOCK for the same reason as in
  Artifact 1. Additionally, "We name MY4 as the primary remaining
  open item for Paper 26" (line 599) is a *framing claim*, not a
  restatement — but it is defensible because the §G dependency
  analysis (the four other limitations of §15.2–§15.5 are
  out-of-scope, only MY4 is in-scope) supports the "primary"
  label. The Author's audit (line 811) defends this by saying "the
  word 'primary' is justified by the §G dependency analysis." I
  accept this defense. **PASS** on the "primary" claim,
  **WEAKENED** on the quoted-referee sentence.

- **Companion-notes pointer (Artifact 5):** meta-content, no
  LOCK-relevant claims beyond the citations. **PASS.**

**LOCK verification verdict: mostly PASS with two WEAKENED flags
on the referee-misquote sentences in §3.6.2 and §15.6.** Both
flags are fixable mechanically by re-reading the verdict file
and correcting or paraphrasing the inline quote. Neither flag is
BROKEN-level.

---

## 12. Verdict justification

**Verdict: WEAKENED.**

### Reasons for NOT issuing VERIFIED

1. **Referee A3 verdict misquote** (sub-step 7a, §7a above). The
   phrase "CLOSABLE GAP — substantial work required" appears four
   times in the Author's draft and one extended variant "multiple
   months of focused work" appears once, all attributed to the
   referee's A3 verdict file. The actual verdict file contains
   neither phrase and instead says "Difficulty: 2-3 pages of
   explicit computation" — the opposite direction. The misquote
   originates upstream in `strategy/04-closing-my4.md`, but the
   editorial node's honest-framing invariant requires the Author
   to verify quoted text against sources, and this did not
   happen.

2. **MY4 vs referee sub-point mismatch** (sub-step 7b, §7b above).
   The Author's MY4 ("distributional → genuine point-spectrum
   upgrade") is not what the referee's A3 headline concern was
   (the headline was the character twist (c) and (e)). The Author
   rebranded a different open item as "the wall the referee
   identified," which is partially honest (there IS an open item
   and the Author correctly names it) but partially misleading
   (the referee's headline was about something else).

3. **Theorem 13.1 trailing parenthetical** (sub-step 2, §2 above).
   The Author added a new rank-1 vacuity parenthetical to the
   theorem statement. The parenthetical is faithful to Remark
   12.6 but is NOT in the original theorem, and the Critic
   mandatory constraint is "only add a conditional clause at the
   start of the hypothesis." This is a non-minimal edit that the
   Author acknowledges but that exceeds the strict instruction.

4. **Change-log adjacent-edits list is incomplete** (sub-step 5,
   §5 above). The Author correctly flags §9.2 Step B(5) and §15.1
   as follow-up edits, but misses at least two other silent-
   inference sites in Paper 26:
   - `sections-part-I.md` line 168 (§2.3 overview: "Nelson's
     analytic vector theorem upgrades these to genuine
     eigenstates")
   - `sections-part-III.md` lines 518–521 (§9.1 Step 4:
     "Nelson self-adjointness (Step 3) promotes these to
     genuine eigenstates")
   Both are the same silent inference the Author diagnosed. The
   change-log should include them as required follow-up edits so
   the runner applies them in the same cycle-2 incorporation
   pass.

5. **Minor citation misattribution** (sub-step 8, §8 above). The
   §3.6.2 draft cites "Reed–Simon II §VIII.3" for the spectral
   theorem, but the spectral theorem is in Reed–Simon Vol. I
   §VIII.3 (not Vol. II). Nelson's theorem X.39 is in Vol. II.
   Minor nit, fixable by changing "II" to "I" in the citation.

6. **Unsourced Route 1 page estimate** (sub-step 6, §6e above).
   The "5–15 pages" estimate for Route 1 is the Author's own
   estimate, not sourced from
   `research/distributional-to-genuine.md`. The Author's audit
   entry describes this as a "restatement" but it isn't. Minor
   nit.

### Reasons for NOT issuing BROKEN

- **Honest-framing audit passes on the draft text:** zero weasel
  hits in the mathematical artifacts (confirmed by re-grep).
- **Theorem 9.1 conclusion preserved byte-for-byte.**
- **Theorem 13.1 conclusion body (parts i, ii, BSD formula)
  preserved byte-for-byte.** The only addition is a trailing
  parenthetical that is faithful to Remark 12.6 and flagged by the
  Author.
- **Downstream Kolyvagin / Gross–Zagier chain is intact.** The
  MY4 conditional propagates cleanly through Theorem 9.1, not
  around it.
- **§3.6.2 placement is correct.** Forward-references are
  consistent with Paper 26's pattern.
- **§15 placement and §15.1 CONCERN are correct.** The Critic
  agrees with the Author that §15.1 line 233 ("This is complete.
  No gaps. No conditional statements") needs softening.
- **Voice/register alignment passes.** The §3.6.2 and §15.6 prose
  matches Paper 26's measured technical register, with minor
  long-sentence tendencies that are stylistic rather than
  structural.

The draft is substantially correct. The issues above are
refinements, not load-bearing errors. **WEAKENED (not BROKEN)**
captures the right severity: the Author should refine before
incorporation, but the core work stands.

---

## 13. Sub-problems for the runner (cycle-2 to-do list)

1. **Correct the referee A3 verdict misquotes** at M.3.1.md lines
   189, 240, 394, 594–595, 671. Replace the inline quoted phrase
   "CLOSABLE GAP — substantial work required" with either (a) the
   actual referee phrase "CLOSABLE GAP; Difficulty: 2-3 pages of
   explicit computation," or (b) a paraphrased "referee verdict:
   closable gap, requiring bounded but substantive work" that
   does not pretend to be a direct quote. Apply the same
   correction to `strategy/04-closing-my4.md` lines 694 and 921
   (the upstream source of the misquote).

2. **Rewrite the "MY4 is the referee's A3 concern" framing** in
   §3.6.2 and §15.6 to distinguish the Author's MY4 (distributional
   → genuine point-spectrum upgrade) from the referee's A3
   headline (character twist cocycle integrality). Use either
   framing option from §7b above: MY4 as the underlying wall of
   which A3 twist is one consequence, OR MY4 and A3 as symptoms
   of the same underlying gap. Honest about the distinction.

3. **Decide on the Theorem 13.1 trailing parenthetical.** Two
   options: (a) drop it entirely and leave Remark 12.6 as-is
   (strict preservation), or (b) accept the addition as a scope-
   clarifying enhancement. Critic default: drop it.

4. **Add two silent-inference sites to the change-log adjacent-
   edits list:**
   - `sections-part-I.md` line 168 (§2.3 RH proof summary):
     soften "Nelson's analytic vector theorem upgrades these to
     genuine eigenstates" to something like "Nelson's analytic
     vector theorem gives essential self-adjointness; the
     distributional-to-genuine upgrade is conditional on the MY4
     closure of the corresponding wall (§3.6.2 over $K$)."
   - `sections-part-III.md` lines 518–521 (§9.1 Step 4 of the
     overview chain): similar softening.

5. **Fix the sub-item numbering in the §9.2 Step B follow-up
   edit.** The silent upgrade is in Step B sub-items 4 AND 5
   jointly, not solely 5. Update the change-log entry to reflect
   this.

6. **Fix the Reed–Simon citation volume.** Change "Reed–Simon II
   §VIII.3" to "Reed–Simon I §VIII.3" (the spectral theorem is in
   Vol. I, not Vol. II).

7. **Source or drop the Route 1 "5–15 pages" estimate.** Either
   add a footnote attributing it to the Author's interpretation
   of the spectral-theory work required, or remove the specific
   page estimate and replace with "several pages of spectral-
   theory work."

8. **Verify before incorporation that the §15.6 page will
   actually fit** between §15.5 and the `---` separator / §16
   break in `sections-parts-V-VI.md`. This is a LaTeX-level
   placement question that will be visible when the preprint is
   compiled. Low risk — the §15 structure is list-like and easily
   extended — but worth a sanity check.

---

## 14. Summary

**Verdict:** WEAKENED.

**Core work:** the editorial draft correctly names MY4, identifies
the silent inference in Paper 26's §9.2 Step B (and §9.1 Step 4
and §2.3, though the latter two were missed in the adjacent-edits
list), preserves Theorem 9.1 and Theorem 13.1 conclusions for the
most part byte-for-byte, and implements Option C as a shippable
conditional framing. The honest-framing audit on the draft text is
clean (zero weasel hits in the artifact prose).

**Issues:** the Author's attribution of quoted text to the
referee's A3 verdict diverges from the actual verdict file, the
MY4 vs A3 sub-point mapping is partially misleading, the Theorem
13.1 update has a non-minimal trailing parenthetical addition, the
adjacent-edits list is incomplete, and there are minor citation
and sourcing nits.

**Recommendation:** refine the six items in §13 above in cycle 2
before incorporation into the Paper 26 LaTeX preprint. After
refinement, the artifacts are shippable and will move Paper 26
from "10 of 11 with one open key lemma" to "11 of 11 conditional
on MY4" in an honest-framed way.

**Confidence level:** high (0.90). The issues are specific and
mechanically fixable. The Author did the work correctly on the
mathematical axis and on the majority of the editorial axis. The
failures are framing-inheritance errors (misquote imported from
the deliverable, MY4 vs A3 sub-point framing inherited from the
deliverable) rather than independent errors of judgment.
