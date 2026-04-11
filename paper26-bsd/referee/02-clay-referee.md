# Advanced Clay Compliance Referee: BSD Proof vs Clay Millennium Prize Criteria (Run r01)

*Written 2026-04-10. Paper 26 of the QG5D/Integers programme.*
*This paper claims to prove the Birch and Swinnerton-Dyer conjecture*
*for CM elliptic curves of analytic rank 0 and 1 over class-number-1*
*imaginary quadratic fields.*

**Scope of this run.** This referee prompt audits **Clay Millennium
Prize eligibility**. It does NOT verify the mathematics — that is
the job of `01-math-referee.md`, a separate run. **You take the
mathematics as given** (or consult the math referee's output at
`latest-run/rigorous-proof.md` if available) and focus on the
question: *Does this paper, as an artifact, qualify for the
Birch and Swinnerton-Dyer Millennium Prize under Clay Mathematics
Institute rules?*

Clay compliance is primarily about **the paper as an artifact**
(publication status, venue, community acceptance, framing, scope
vs Wiles' description) and **the process** (Clay §4–§6 requirements),
not about whether the math is correct. A mathematically brilliant
proof that does not meet Clay's procedural criteria is not eligible
for the prize. A mathematically flawed proof that somehow meets
the procedural criteria would be caught at Clay's Stage 2 review.
The Clay referee's job is the former check: does the paper meet
the criteria for Clay to take it seriously?

---

# Environment setup

**Minimal setup — this run is mostly reading, not computation:**

```bash
bash /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/code/setup-venv.sh
source /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/code/.venv/bin/activate
```

**What the script does:**
1. Moves existing `latest-run/` to `runs/r{NN+1}/` (preserves prior
   runs).
2. Creates a fresh empty `latest-run/`.
3. Rebuilds `.venv/` from `code/requirements.txt`.

**Usage:** Use the venv for light computational cross-checks only.
This run focuses on process and framing, not on verifying numerical
claims at 200-digit precision. **When the math referee's
`rigorous-proof.md` is available**, cite it instead of re-doing
the math.

**Typical computational checks for this run:**
- **LMFDB cross-check** for test curves (y² = x³ − x, y² = x³ − 1):
  verify the paper's reported rank, torsion, Tamagawa numbers,
  periods, Ш (conjectural or proven) match LMFDB's entries.
- **Sanity check** any numerical quantity that the paper uses to
  illustrate the main theorem.
- **Publication venue check:** does the proposed journal (if any)
  meet Clay §6(e) requirements?
- **MathSciNet inclusion check** for the target journal(s).

For every check: note in your report *"Verified via LMFDB / ..."*.

---

You are an expert mathematical referee with specific expertise in:

- **The Clay Millennium Prize rules** (§1–§9): what counts as
  eligible, what the 2-year waiting period means, what "general
  acceptance" looks like in practice, what "qualifying outlet"
  requires.
- **Andrew Wiles' official BSD problem description**: the precise
  statement of the conjecture, its refined form with the leading
  coefficient (|Ш|·R·Ω·∏c_p / |E_tors|²), the scope ("an elliptic
  curve E over ℚ"), the relation to modularity, the history
  (Coates-Wiles 1977, Gross-Zagier 1986, Kolyvagin 1989, Rubin
  1991, BCDT 2001).
- **Mathematical publication processes**: the refereeing
  workflows of top-tier journals (Annals, Inventiones, Acta,
  CMP, JAMS, Duke, Publications mathématiques de l'IHÉS), their
  editorial boards, their MathSciNet status, their typical
  timelines.
- **Community-acceptance dynamics** for claimed solutions of
  famous problems: the Wiles/FLT timeline (1993 announcement,
  1994 gap found, 1995 published, 1996 acceptance), the
  Perelman/Poincaré timeline (2002–2010), the track record of
  failed BSD claims.
- **Partial-prize analysis under Clay §5(c)(ii)**: when a claimed
  solution covers a proper subset of the conjecture, what the
  CMI's historical practice has been.
- **Scope analysis**: distinguishing "BSD for all elliptic curves"
  from "BSD for a specific class of curves," and whether the
  latter can "effectively resolve" the problem under Clay's
  discretion.
- **Mathematical community awareness**: who are the experts CMI
  would consult for a BSD claim? (Kolyvagin, Skinner, Urban,
  Rubin, Zhang, Bhargava, Venkatesh, Wiles himself, Mazur, ...)

# Research online about these topics:
- The Clay Millennium Prize rules (saved at
  `references/clay-millennium-prize-rules.md`).
- Wiles' official BSD problem description (saved at
  `references/clay-bsd-official-description.md`).
- The historical timelines of Wiles/FLT, Perelman/Poincaré, and
  other famous claimed solutions — what "2 years of general
  acceptance" looked like in practice.
- The editorial policies and MathSciNet status of: *Annals of
  Mathematics*, *Inventiones Mathematicae*, *Publications
  mathématiques de l'IHÉS*, *Acta Mathematica*, *Communications
  in Mathematical Physics*, *Journal of the American Mathematical
  Society*, *Duke Mathematical Journal*.
- The current research frontier of BSD: Bhargava-Shankar, Skinner-
  Urban, Jetchev-Skinner-Wan, Kolyvagin/Rubin, main conjecture of
  Iwasawa theory, p-adic BSD. What is the state of "general
  acceptance" in 2026?

# Your profile
- You are a **process-skeptical** referee, not a math-skeptical
  one. You assume the math is correct (or defer to the math
  referee's output); your job is to assess whether this paper,
  AS AN ARTIFACT, can clear the Clay bar.
- You know Clay rules §1–§9 cold. You know what CMI will and
  will not accept.
- You do not give partial credit on procedural criteria. Either
  the paper is published in a qualifying outlet, or it is not.
  Either the 2-year clock has started, or it has not.
- On scope, you are precise. You distinguish "the main theorem as
  stated in Wiles' description" from "a significant partial
  result" from "a closely related result that does not count
  under §5(d)."
- You are honest about what the authors can and cannot control:
  publication is within control (eventually); the 2-year wait is
  absolute; community acceptance depends on external experts.

# Rationale and Strategy

1. Does the paper address the **specific mathematical statement**
   in Wiles' description? (Clay §4(d), §5(d))
2. Is the paper in a **qualifying outlet** per Clay §6(e)?
3. Has **2 years** elapsed since qualifying publication?
   (Clay §4(b))
4. Does the **global mathematics community** accept the proof?
   (Clay §4(c))
5. Is this a **complete** mathematical solution? (Clay §5(a))
6. If not complete, does it "effectively resolve" the problem
   under §5(c)(ii)? If not, what partial recognition applies?
7. Is the paper **unconditional**, or does it depend on assumptions
   not explicitly stated? (Clay precedent: no hidden conditionality.)
8. Is the **framing honest**? Does the abstract / theorem statement
   match what is proved? Is there any overreach?
9. What is the **path to full compliance**? Which criteria are
   already met, which can be met, and what is the honest timeline?

---

## The Wiles BSD Problem Description

**Source:** `references/clay-bsd-official-description.md` (enriched
with verbatim Wiles quotes from the Clay PDF).

### Verbatim Conjecture Statement

> **Conjecture (Birch and Swinnerton-Dyer, Wiles).** The Taylor
> expansion of L(C, s) at s = 1 has the form
>
>     L(C, s) = c(s − 1)^r + higher order terms
>
> with c ≠ 0 and r = rank(C(ℚ)).
>
> In particular L(C, 1) = 0 ⇔ C(ℚ) is infinite.

### Strong Form (Wiles Remark 1)

L*(C, s) ∼ c*(s − 1)^r with
c* = |Ш_C| · R_∞ · w_∞ · ∏_{p|2Δ} w_p / |C(ℚ)_tors|²

where |Ш_C| is the order of the Tate-Shafarevich group (not known
to be finite in general), R_∞ is the regulator, w_∞ is a multiple
of the real period, w_p are Tamagawa factors.

### Wiles' framing

Wiles speaks of "an elliptic curve E over ℚ" — the conjecture is
for **ALL** elliptic curves over ℚ, not for a sub-family. The
known theorem (Coates-Wiles, Gross-Zagier, Kolyvagin, Rubin + BCDT
modularity) covers analytic rank 0 or 1 for modular curves; no
proven cases exist for rank ≥ 2.

### What a valid proof must establish (Wiles' description):

1. rank(E(ℚ)) = ord_{s=1} L(E, s) **for all elliptic curves E/ℚ**.
2. Optionally: the leading-coefficient strong form, including
   finiteness of Ш_E.
3. Unconditional.
4. Rigorous mathematics (not numerical evidence).

---

## The Clay Millennium Prize Rules (Summary)

**Source:** `references/clay-millennium-prize-rules.md`.

### §4 Criteria For Prizes

CMI may award a Prize **if and only if**:

- **§4(a)** Published by a **Qualifying Outlet** (§6).
- **§4(b)** At least **2 years** since publication.
- **§4(c)** **General acceptance** in the global mathematics
  community (CMI sole discretion).
- **§4(d)** Satisfactorily answers questions raised by the
  Problem's **official description** (CMI sole discretion).

### §5 Proposed Solutions

- **§5(a)** Only a **complete** mathematical solution is eligible.
- **§5(c)(ii)** A counterexample that only eliminates a special
  case may receive a smaller prize from other CMI funds. *By
  analogy:* a proof that covers only a special case may likewise
  receive partial recognition at CMI's discretion.
- **§5(d)** Paper must address the specific mathematical questions
  in the description — even closely related questions don't count.
- **§5(e)** CMI does **not accept direct submissions**; they
  monitor publications.

### §6 Publication — Qualifying Outlet

- **§6(a)(i)** A refereed mathematics publication of worldwide
  repute.
- **§6(e)(i)** Named editorial board available for contact.
- **§6(e)(ii)** Editor with professional knowledge to identify
  appropriate referees.
- **§6(e)(iii)** Published refereeing process ensuring expert
  review.
- **§6(e)(iv)** Inclusion in **MathSciNet** list.
- **§6(f)** CMI may relax §6(e) conditions if experts advise the
  solution is likely correct.

### §7 Evaluation of a Proposed Solution

**Stage 1 — General Acceptance** (minimum 2 years of community
monitoring).

**Stage 2 — CMI Examination** (only if Stage 1 passes; convenes a
special advisory committee of ≥3 members, ≥2 experts in the
problem area).

### §8 Award of a Prize

**§8(b)** CMI will consider whether the solution depends on prior
published insights and may recognize/include prior authors.

---

## Files to Read (in order)

**The preprint (main focus):**

1. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/00-table-of-contents.md`
2. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-I.md`
   (§1: abstract, main theorem statement, scope; §2: programme
   recap — read particularly for *framing* and *scope claims*)
3. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-IV.md`
   (§10–13: the main theorem as stated)
4. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-parts-V-VI.md`
   (§14–19: examples, **scope limitations §15**, adversarial review,
   conclusions — read §15 and §19 particularly carefully for the
   scope framing)

You MAY skim §3–§9 (the technical proof chain) — that is the math
referee's territory. Your job is framing, scope, and process.

**Internal context:**

5. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/01-adversarial-proof-review.md`
   (check how scope and conditionality were handled internally)
6. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/strategy/03-adversarial-review-results.md`
   (look for the "Issue 1 BROKEN: conditionality inheritance" item
   and verify its resolution)

**Math referee output (if available):**

7. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/latest-run/rigorous-proof.md`
   — if the math referee has already run, consult it for the rigor
   verdict. Do not re-do the math audit; cite the findings.
8. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/latest-run/summary.md`
   — the math referee's overall rigor verdict.

**Reference materials (critical):**

9. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/references/clay-bsd-official-description.md`
   (Wiles' full description — **read cover to cover**)
10. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/references/clay-millennium-prize-rules.md`
    (Clay rules — **read §4, §5, §6 verbatim**)

**Cross-reference (for precedent):**

11. `/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/strategy/math-referee-run/clay-gaps.md`
    — the clay-gaps analysis written for Paper 13 (RH). Same
    programme, similar Clay concerns, different problem. Useful
    as a template for what a Clay gap report should look like.

**Out of scope (do not read):** `runs/r**/` (archived prior runs).

---

## Mandatory Checks (~20 items — Clay compliance only)

### Group WS — Wiles Statement & Scope

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **WS1** | Paper addresses the specific Wiles statement (rank = ord_{s=1} L) | Yes, for the claimed scope |
| **WS2** | Scope of curves covered precisely stated | CM, rank 0+1, class-number-1 fields — nine fields enumerated |
| **WS3** | Scope is a **proper subset** of Wiles' "all elliptic curves over ℚ" | Yes; this is a partial result |
| **WS4** | Strong form (leading coefficient) addressed or not addressed, honestly | Paper states whether weak or strong BSD is proved |
| **WS5** | Ш finiteness established (required for strong form) | Follows from Kolyvagin for curves in scope |
| **WS6** | Bombieri's themes (L-functions / GRH extension) discussed | Bombieri's description mentions GRH for L-functions as the general frame; does paper engage? |

### Group PU — Publication Status (§4(a), §6)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **PU1** | §4(a) Paper is published in a Qualifying Outlet | Currently preprint only: NOT MET |
| **PU2** | §6(e)(i) Target journal has named editorial board | Identify target journal and verify |
| **PU3** | §6(e)(ii) Target journal's editor can identify expert referees | Top-tier math journal — structurally yes |
| **PU4** | §6(e)(iii) Target journal has published refereeing process | Top-tier journal — yes |
| **PU5** | §6(e)(iv) Target journal included in MathSciNet | Verify explicitly for the chosen venue |
| **PU6** | §6(a) — venue is of worldwide repute | Assess — probably Annals/Inventiones/CMP/etc. |

### Group WA — Waiting Period (§4(b))

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **WA1** | §4(b) At least 2 years since qualifying publication | Currently 0 years: NOT MET |
| **WA2** | The 2-year clock starts at journal publication, not arXiv | Honest framing: the clock has not started |

### Group GA — General Acceptance (§4(c), §7 Stage 1)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **GA1** | §4(c) General acceptance in the math community | Currently: no external reviews known; NOT MET |
| **GA2** | The paper has been read by independent experts in CM theory, BC systems, Euler systems | Check for evidence of expert engagement |
| **GA3** | The paper has been presented at major conferences, seminars | Check for talks, presentations |
| **GA4** | The mathematical community has responded (positively or critically) | Literature search: any referenced critiques or endorsements? |

### Group CO — Completeness (§5(a), §5(c), §5(d))

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **CO1** | §5(a) Complete mathematical solution of the stated problem | The claim is BSD for CM rank 0+1; this is a partial result for the full conjecture |
| **CO2** | §5(d) Addresses the specific questions in the description | Engages with the rank-equality statement; does not address rank ≥ 2, non-CM |
| **CO3** | §5(c)(ii) Partial result may qualify for partial prize | A proof of BSD for CM rank 0+1 would be a significant partial result; §5(c)(ii) analysis applies |
| **CO4** | Paper is unconditional (not conditional on unstated assumptions) | Verify — the internal adversarial review flagged conditionality as Issue 1 BROKEN |
| **CO5** | If conditional, the conditions are explicit and acknowledged | Post-fix, is the paper explicit about what it assumes? |

### Group FR — Framing and Honesty

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **FR1** | Abstract and theorem statement match the actual scope | No overreach — the paper does not claim "BSD" without qualification |
| **FR2** | The "two Millennium Problems from one bridge" framing (RH + BSD) is honest | Programmatic connection OK; technical conflation not OK |
| **FR3** | Scope limitations (rank ≥ 2, non-CM, h_K > 1) explicitly disclosed | In §15 as the authors intend |
| **FR4** | No implicit claim to the full $1M Clay prize | Paper is honest about partial-result status |
| **FR5** | The mathematics is presented for peer review, not for PR | Tone check — is this a math paper or a press release? |

### Group DP — Dependencies and Citations

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **DP1** | Kolyvagin's theorem cited with precise statement | Verify |
| **DP2** | Gross-Zagier formula cited with precise scope | Verify |
| **DP3** | Baker's theorem cited correctly | Verify |
| **DP4** | Deuring's CM factorization cited correctly | Verify |
| **DP5** | Modularity theorem (BCDT 2001) cited or derived for CM curves | Verify (CM curves are modular classically) |
| **DP6** | Rubin 1991 cited correctly for the p-part of BSD for CM | Verify scope: p > 7; small primes? |
| **DP7** | Every internal research/N.md note that the paper depends on is either inlined or cited as a separate paper | Verify — Clay §6(d) forbids supplementary material |
| **DP8** | All cited results are used within their actual scope | Scope check for each dependency |

---

## Per-Point Analysis

### Point CA1: The Main Statement vs Wiles' Description [HEAVY]

**Location:** Abstract, §1 (statement), §13 (the theorem)

**Interrogate:**

(a) **The specific Wiles statement.** Wiles' description is:
rank(E(ℚ)) = ord_{s=1} L(E, s) for an elliptic curve E over ℚ.
Does Paper 26's main theorem match this statement *for the
claimed scope*? What exactly does Paper 26 claim to prove, in
precise mathematical terms, for what set of curves?

(b) **The strong form.** Wiles' description includes the leading
coefficient formula c* = |Ш|·R·Ω·∏c_p / |E_tors|². Does Paper 26
establish this, or only the weak form (rank equality)? If only
weak, does the paper say so clearly?

(c) **Scope vs "an elliptic curve over ℚ".** Wiles speaks of
"an elliptic curve E over ℚ" — for Clay, this means all elliptic
curves. Paper 26 proves BSD for CM curves of rank 0+1 over
class-number-1 imaginary quadratic fields (nine fields).
Mathematically, this is a proper subset of "all elliptic curves
over ℚ." **Clay §5(d) explicitly says: "even closely related
questions don't count."** Is Paper 26's scope a "closely related
question" in Clay's sense, or is it within the Wiles statement?

(d) **The partial-prize analysis (§5(c)(ii)).** If Paper 26 is a
significant partial result, what is the §5(c)(ii) analysis?
Historically, CMI has not awarded partial prizes for Millennium
Problems, but the rule permits a smaller prize "from other CMI
funds" if the partial result is significant. Discuss.

(e) **Honest framing.** Does Paper 26 claim the full $1M prize,
or does it frame itself as a partial result? Cite specific
passages from the abstract, introduction, theorem statement, and
conclusion that bear on this.

---

### Point CA2: Qualifying Outlet (§6(e)) [HEAVY]

**Location:** Current status of the paper (arXiv / journal / etc.)

**Interrogate:**

(a) **Current publication status.** Where is Paper 26 currently?
arXiv? Internal only? Submitted to a journal? If submitted, which?

(b) **Target journal.** If the paper is intended for a specific
journal, identify it. The natural candidates for a BSD proof are:
- *Annals of Mathematics*
- *Inventiones Mathematicae*
- *Acta Mathematica*
- *Publications mathématiques de l'IHÉS*
- *Journal of the American Mathematical Society*
- *Duke Mathematical Journal*
- *Communications in Mathematical Physics* (for the operator-
  algebraic content)

(c) **§6(e)(i) — named editorial board.** Verify that the target
journal has a publicly accessible editorial board. All top-tier
math journals do.

(d) **§6(e)(ii) — editor can identify referees.** Structurally
yes for top-tier journals. The editors are research mathematicians
with domain knowledge.

(e) **§6(e)(iii) — published refereeing process.** All top-tier
math journals have standard peer-review processes. Verify.

(f) **§6(e)(iv) — MathSciNet inclusion.** Explicitly verify that
the target journal is indexed by MathSciNet. This is a concrete,
lookupable item.

(g) **§6(a) — worldwide repute.** Any of the candidates above
qualify. Identify which one the paper is targeting or should
target.

(h) **Current status verdict.** §6(e) currently [MET / NOT MET /
WILL BE MET upon publication in journal X].

---

### Point CA3: 2-Year Waiting Period (§4(b)) [MEDIUM]

**Location:** Publication timeline

**Interrogate:**

(a) **The clock.** The 2-year waiting period (§4(b)) starts from
the date of publication in a Qualifying Outlet. Not from arXiv
preprint; not from internal release; not from announcement.
Journal publication = start of clock.

(b) **Current clock status.** If the paper is not yet published
in a Qualifying Outlet, the clock has not started. Current state:
**clock not started**.

(c) **Earliest possible Clay consideration.** Compute: if the
paper is submitted today (2026-04-10), typical journal review
cycle is 1–3 years, so earliest publication is 2027–2029, plus
the 2-year wait = 2029–2031 for Clay to begin Stage 2 review.

(d) **Historical comparison.** Wiles/FLT was published in 1995
(Annals), accepted by the community in 1996, and various prizes
followed. The Clay Millennium Prize did not exist then (CMI was
founded in 1998), but the community-acceptance timeline is a
relevant benchmark.

(e) **Path to met status.** State explicitly what needs to happen
for §4(b) to be met. This is not actionable by the authors alone
but depends on the journal's review timeline.

---

### Point CA4: General Acceptance (§4(c), §7 Stage 1) [HEAVY]

**Location:** Community engagement — external to the paper itself

**Interrogate:**

(a) **What "general acceptance" means.** Clay §4(c): "General
acceptance in the global mathematics community, in the sole
discretion of CMI." §7 Stage 1: CMI monitors for proposed
solutions; must survive "rigorous examination by the global
mathematics community for minimum 2 years."

(b) **Current state of acceptance.** Has the paper been:
- Read by independent experts?
- Discussed in seminars?
- Presented at conferences?
- Cited in other papers?
- Critiqued (positively or negatively)?

If the paper is preprint-only with no external readers, then
"general acceptance" has not even begun.

(c) **The experts CMI would consult.** For a BSD proof involving
CM theory, Bost-Connes systems, Euler systems, and Kolyvagin/
Gross-Zagier, the natural experts include (but are not limited
to):
- Kolyvagin himself (if available)
- Skinner, Urban (Iwasawa theory, BSD)
- Bhargava, Shankar (statistical BSD)
- Rubin (main conjecture of Iwasawa theory for imaginary
  quadratic fields)
- Zhang (Yuan-Zhang-Zhang generalized Gross-Zagier)
- Wiles himself
- Connes (Bost-Connes programme, trace formula)
- Ha, Paugam (BC over number fields)
- Mazur (general BSD commentary)
- Bombieri (problem description author)

Has any of these engaged with Paper 26?

(d) **Path to general acceptance.** Realistic timeline from
current state: arXiv posting → seminar talks → expert critiques
→ revisions → resubmission → eventual acceptance. Typical for
a major claim: 3–10 years.

(e) **Community acceptance for partial results.** Even if Paper
26 establishes BSD for CM rank 0+1 rigorously (per the math
referee), is this the kind of result the community would accept
as "resolving BSD" in Clay's sense? Historically no — partial
results on Millennium Problems are celebrated but are not
treated as prize-eligible.

---

### Point CA5: Bombieri's Specific Questions (§4(d), §5(d)) [HEAVY]

**Location:** Wiles' problem description (the referenced PDF)

**Interrogate:**

(a) **Wiles' main statement.** The rank-equality conjecture for
elliptic curves over ℚ. **Paper 26 addresses this for CM rank
0+1.** Partial but on-topic.

(b) **Wiles' strong form.** The leading coefficient formula with
|Ш|, regulator, period, Tamagawa factors. Does Paper 26 address
the full strong form, or only the weak form (rank equality)?

(c) **Wiles' discussion of related results.** Wiles' description
discusses:
- Coates-Wiles 1977 (rank 0, CM)
- Gross-Zagier 1986 (rank 1, Heegner)
- Kolyvagin 1989 (rank 0 and 1, modular)
- Rubin 1991 (p-part, CM)
- Modularity theorem
- Refined conjectures on special L-values

Does Paper 26 engage with these results within their scope and
credit them appropriately?

(d) **Wiles' mention of function field analogue.** Wiles notes
the function-field BSD analogue is equivalent to finiteness of Ш.
Paper 26 is about number fields, not function fields, but does
it discuss the analogue for context?

(e) **Wiles' mention of higher-dimensional varieties.** Wiles
discusses conjectures on higher-dimensional varieties. Paper 26
is about elliptic curves (1-dimensional abelian varieties). This
is on topic.

(f) **Clay §5(d) "even closely related questions don't count."**
Is BSD for CM rank 0+1 the "main" BSD question, a "closely
related" question, or a sub-case of the main question? This is a
judgment call, but the referee should state a clear position.

---

### Point CA6: Complete Solution (§5(a)) [HEAVY]

**Location:** §13 (theorem) + §15 (scope)

**Interrogate:**

(a) **Clay §5(a).** "Only a complete mathematical solution of the
problem ... will be eligible for consideration."

(b) **"Complete" means what?** CMI determines completeness at its
sole discretion. Historically, "complete" means resolving the
problem as stated, for all instances covered by the statement.

(c) **Paper 26's claim.** BSD for CM rank 0+1 over nine fields.
This is NOT complete in the sense of resolving "BSD for all
elliptic curves over ℚ."

(d) **The §5(c)(ii) alternative.** CMI rules explicitly allow a
smaller prize "from other CMI funds" for a partial result, at
CMI's discretion. This is the relevant rule for Paper 26, if the
paper survives technical review.

(e) **Is the claim complete WITHIN its stated scope?** Even if
not complete for Wiles' full statement, is Paper 26 complete
for what it claims to prove? (i.e., rigorous, unconditional,
covers all CM curves of rank 0+1 over the nine fields.) If yes,
it is a legitimate partial result; if no, it is not even complete
within its own scope.

(f) **The rank ≥ 2 gap.** Paper 26 does not address rank ≥ 2.
This is honestly acknowledged in §15. Is there any claim or
implication that the method could extend?

(g) **The non-CM gap.** Paper 26 does not address non-CM curves.
Again, honestly acknowledged. The CM factorization is structural;
extension would require different machinery (GL₂/Langlands).

---

### Point CA7: Unconditionality (§5(a) implicit) [MEDIUM]

**Location:** The proof chain, dependencies section, §17 (adversarial
review)

**Interrogate:**

(a) **The internal adversarial review.** Issue 1 (BROKEN) flagged
conditionality inheritance. The paper was supposed to be
reframed to explicitly state any assumptions. **Has this been
done in the current release candidate?**

(b) **Dependencies on CBB axioms.** Does Paper 26 depend on
axioms that are not themselves proved? If so, the proof is
conditional, and must be labeled as such.

(c) **Dependencies on Paper 13.** Earlier drafts may have
depended on Paper 13's RH proof machinery. Paper 13 is independently
at 10/10 (RH proved), but is the BSD proof technically dependent
on Paper 13's results, or only programmatically related?

(d) **Dependencies on unpublished internal notes.** Any
research/N.md references constitute supplementary material under
Clay §6(d) and are NOT considered. Are all internal notes either
inlined into the paper or cited as separate published papers?

(e) **Conditionality disclosure.** If Paper 26 is conditional on
anything (axioms, unproven lemmas, future journal acceptance of
cited preprints), is this explicitly and honestly disclosed in
the abstract, introduction, and theorem statement?

---

### Point CA8: Honest Framing (cross-cutting) [HEAVY]

**Location:** Abstract, §1, §13, §19 (conclusion)

**Interrogate:**

(a) **Abstract match.** Does the abstract accurately describe
the scope (CM rank 0+1 over nine fields), or does it suggest a
broader result?

(b) **Theorem statement match.** Is the main theorem statement
in §13 precise about the scope?

(c) **Title match.** Does the title accurately reflect the scope?
Or does it suggest "BSD proved" without qualification?

(d) **The "two Millennium Problems" framing.** Paper 26 is part
of a programme that also produced Paper 13 (RH). Framing this as
"two Millennium Problems from one bridge" is programmatically
reasonable but may be read as overreach if the BSD proof only
covers CM rank 0+1.

(e) **Press-release tone vs research-paper tone.** A claimed
solution of a Millennium Problem attracts attention. Is the
paper written in a tone appropriate for peer review, or does it
have the rhetorical structure of a press release?

(f) **Any implicit claim to the full $1M prize.** Does the paper
anywhere (in text, marketing, public announcements) imply or
claim eligibility for the full Clay prize?

---

### Point CA9: Path Forward — Honest Timeline [MEDIUM]

**Location:** Not in the paper; constructive analysis

**Interrogate:**

(a) **Current compliance snapshot.** For each Clay criterion,
state the current status: MET / NOT MET / PARTIAL.

(b) **Blockers within the authors' control.** Which criteria can
be moved from NOT MET to MET by the authors' actions?
- Publication in a qualifying outlet: YES, within control
  (submit to a top-tier journal)
- Scope honesty: YES, within control (reframe if needed)
- Citation completeness: YES, within control
- Internal notes inlined: YES, within control

(c) **Blockers outside the authors' control.**
- 2-year waiting period: NO (absolute)
- General community acceptance: PARTIALLY (depends on external
  experts)
- CMI's determination: NO (sole discretion)

(d) **Honest timeline estimate.** From the current state (2026-04-10):
- Immediate (0–3 months): arXiv submission, internal polish
- Short-term (3–12 months): seminar talks, expert engagement
- Medium-term (1–3 years): journal review cycle, revisions
- Long-term (3–10 years): community acceptance, Clay Stage 1
  monitoring
- Final (5–15 years): Clay Stage 2 examination

(e) **Partial-prize analysis.** Given that Paper 26 covers a
proper subset of Wiles' full statement, the most likely outcome
for Clay is: if the math is correct, a partial recognition under
§5(c)(ii), NOT the full $1M prize. Is the authors' strategy
consistent with this realistic expectation?

---

### Point CA10: The Math Referee's Output (if available) [MEDIUM]

**Location:** `latest-run/rigorous-proof.md` and `latest-run/summary.md`
from the math referee run.

**Interrogate:**

(a) **If the math referee has run.** Consult the `rigorous-proof.md`
and `summary.md` files. What is the math referee's verdict on
rigor? How many steps are [THEOREM], [LEMMA], [KEY LEMMA — OPEN],
[GAP]?

(b) **If all steps are [THEOREM] or [LEMMA].** The math is
(according to the math referee) rigorous. Clay compliance then
rests purely on the procedural criteria in this audit.

(c) **If any steps are [KEY LEMMA — OPEN].** The proof is
conditional on those open lemmas. This means §5(a) (complete
solution) is not met even for the claimed scope.

(d) **If any steps are [GAP].** The proof has mathematical gaps
and does not clear even the rigor bar. Clay compliance is moot
until the math is fixed.

(e) **If the math referee has NOT run.** Note this and proceed
with the Clay audit in isolation. Flag the dependency on a future
math referee run for a complete verdict.

---

## Output Format

Write all report files into:
`/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/latest-run/`

**Note:** If the math referee has already produced output in
`latest-run/`, do not overwrite `rigorous-proof.md`,
`rigor-checklist.md`, or the math-referee `points/` directory.
Instead, create your Clay audit files alongside them. The two
audits are designed to coexist in the same `latest-run/` directory.

### Directory layout (mandatory)

```
latest-run/
├── INDEX.md                          ← navigation (both audits)
├── clay-compliance.md                ← yang-mills-style Clay audit (PRIMARY OUTPUT)
├── clay-checklist.md                 ← master roll-up (~30 rows)
├── clay-summary.md                   ← overall Clay eligibility verdict
├── computation-log.md                ← shared with math referee
├── clay-points/
│   ├── CA1-wiles-statement/
│   │   ├── 00-statement.md
│   │   ├── 01-wiles-specific.md
│   │   ├── 02-strong-form.md
│   │   ├── 03-scope-subset.md
│   │   ├── 04-partial-prize-5c.md
│   │   ├── 05-honest-framing.md
│   │   └── verdict.md
│   ├── CA2-qualifying-outlet/
│   │   ├── 00-statement.md
│   │   ├── 01-current-status.md
│   │   ├── 02-target-journal.md
│   │   ├── 03-clay-6e-conditions.md
│   │   ├── 04-mathscinet.md
│   │   └── verdict.md
│   ├── CA3-two-year-wait/
│   │   ├── 00-statement.md
│   │   ├── 01-clock-status.md
│   │   ├── 02-timeline.md
│   │   └── verdict.md
│   ├── CA4-general-acceptance/
│   │   ├── 00-statement.md
│   │   ├── 01-current-state.md
│   │   ├── 02-experts.md
│   │   ├── 03-path-to-acceptance.md
│   │   └── verdict.md
│   ├── CA5-bombieri-questions/
│   │   ├── 00-statement.md
│   │   ├── 01-main-statement.md
│   │   ├── 02-strong-form.md
│   │   ├── 03-related-results.md
│   │   ├── 04-clay-5d.md
│   │   └── verdict.md
│   ├── CA6-completeness/
│   │   ├── 00-statement.md
│   │   ├── 01-clay-5a.md
│   │   ├── 02-scope-incompleteness.md
│   │   ├── 03-5c-ii-partial.md
│   │   ├── 04-within-scope-completeness.md
│   │   └── verdict.md
│   ├── CA7-unconditional/
│   │   ├── 00-statement.md
│   │   ├── 01-internal-review.md
│   │   ├── 02-dependencies.md
│   │   ├── 03-internal-notes.md
│   │   ├── 04-disclosure.md
│   │   └── verdict.md
│   ├── CA8-framing/
│   │   ├── 00-statement.md
│   │   ├── 01-abstract.md
│   │   ├── 02-theorem-statement.md
│   │   ├── 03-title.md
│   │   ├── 04-two-millennium-framing.md
│   │   ├── 05-tone.md
│   │   └── verdict.md
│   ├── CA9-path-forward/
│   │   ├── 00-statement.md
│   │   ├── 01-current-snapshot.md
│   │   ├── 02-within-control.md
│   │   ├── 03-outside-control.md
│   │   ├── 04-timeline.md
│   │   ├── 05-partial-prize.md
│   │   └── verdict.md
│   └── CA10-math-referee-coordination/
│       ├── 00-statement.md
│       ├── 01-rigor-verdict.md
│       ├── 02-open-lemmas-impact.md
│       └── verdict.md
└── clay-checks/
    ├── WS-wiles-statement/WS1.md .. WS6.md
    ├── PU-publication/PU1.md .. PU6.md
    ├── WA-waiting-period/WA1.md .. WA2.md
    ├── GA-general-acceptance/GA1.md .. GA4.md
    ├── CO-completeness/CO1.md .. CO5.md
    ├── FR-framing/FR1.md .. FR5.md
    └── DP-dependencies/DP1.md .. DP8.md
```

**No file in this tree should exceed ~300 lines.**

### The mandatory `clay-compliance.md` output (PRIMARY DELIVERABLE)

This is a structured criterion-by-criterion analysis against
Clay §4–§6. Structure:

```markdown
# Clay Millennium Prize Compliance Audit — Paper 26 BSD

*Run r01, 2026-04-10.*

## Executive Summary

**Clay eligibility verdict:** [MEETS / PARTIALLY MEETS / DOES NOT MEET]

**If DOES NOT MEET:** [which criteria are not met, and why]

**If PARTIALLY MEETS:** [which criteria are met, which are not,
and the path to full compliance]

**Expected Clay outcome:** [based on Clay §5(c)(ii) partial-prize
analysis, what is the most likely outcome if the paper's math is
correct]

---

## §4 Criteria

### §4(a) — Published by a Qualifying Outlet
**Status:** [MET / NOT MET / IN PROGRESS]
**Current state:** [e.g., "preprint only, not yet submitted to a
journal"]
**Path to met:** [submit to journal X, expect 1-3 year review]
**Notes:** [any caveats]

### §4(b) — 2 years since publication
**Status:** [MET / NOT MET / IN PROGRESS]
**Current state:** [clock not started]
**Earliest possible met date:** [e.g., "2030, assuming 2028
publication"]

### §4(c) — General acceptance
**Status:** [MET / NOT MET / IN PROGRESS]
**Current state:** [e.g., "no external reviews; no conference
talks; no expert engagement known"]
**Path to met:** [arXiv, seminars, journal publication, 2+ years
of community review]
**Estimated timeline:** [3–7 years from current state]

### §4(d) — Addresses Bombieri/Wiles questions
**Status:** [MET / PARTIALLY MET / NOT MET]
**Current state:** [e.g., "addresses the main rank-equality
statement for the CM rank 0+1 subset of elliptic curves"]
**Clay §5(d) analysis:** [does this count, or is it a "closely
related question" excluded by §5(d)?]

---

## §5 Proposed Solutions

### §5(a) — Complete mathematical solution
**Status:** [MET / NOT MET]
**Current state:** [e.g., "the claimed scope (CM rank 0+1) is a
proper subset of Wiles' 'all elliptic curves over ℚ'; within the
claimed scope, the proof is [complete / incomplete] per the
math referee"]

### §5(c)(ii) — Partial result analysis
**Analysis:** [if the math referee confirms rigor, the most
likely outcome is partial recognition under §5(c)(ii); possibly
a smaller prize from other CMI funds; not the full $1M prize]

### §5(d) — Specific questions
**Analysis:** [the paper addresses Wiles' main statement for a
proper subset of elliptic curves; whether this counts as "the
specific questions" is at CMI's discretion]

---

## §6 Qualifying Outlet Conditions

### §6(a) — Worldwide repute
**Target journal:** [e.g., Annals of Mathematics]
**Repute:** [MET]

### §6(e)(i) — Named editorial board
**Status:** [MET for top-tier journals]

### §6(e)(ii) — Editor can identify referees
**Status:** [MET for top-tier journals]

### §6(e)(iii) — Published refereeing process
**Status:** [MET for top-tier journals]

### §6(e)(iv) — MathSciNet inclusion
**Status:** [verify explicitly — MET for all top-tier math journals]

### §6(f) — Relaxed conditions (not applicable)
**Notes:** [this rule applies when experts advise the solution
is "likely correct" — not relevant unless Clay formally considers]

---

## Scope Analysis

**Wiles' statement:** BSD for an elliptic curve E over ℚ
(i.e., for ALL elliptic curves).

**Paper 26's claim:** BSD for CM elliptic curves of analytic rank
0 or 1 over class-number-1 imaginary quadratic fields (nine
fields).

**Is this a proper subset of Wiles' statement?** YES.

**Is it "the specific question" per §5(d)?** At CMI's discretion.
It is the rank-equality statement for a specific class of curves.

**Historical precedent.** CMI has not awarded partial prizes for
Millennium Problems to date. The §5(c)(ii) partial-prize
mechanism exists but has not been invoked.

---

## Dependencies Audit

[List of all cited results and internal notes with pass/fail]

---

## Honest Path Forward

**Blockers within the authors' control:**
[list]

**Blockers outside the authors' control:**
[list]

**Honest timeline to full compliance:**
[7–15 years realistic]

**Most likely outcome at the end of this timeline:**
[partial recognition if math is correct; nothing if math has
gaps]
```

### File templates

**`clay-points/<point-id>/00-statement.md`**:

```markdown
## Point [ID]: [Title]

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Clay rules invoked:** [§4(a), §5(d), etc.]

**The question:**
[Exact question from the prompt.]

**Sub-questions (one file each):**
- (a) [01-...md]
- (b) [02-...md]
...
```

**`clay-points/<point-id>/0N-<name>.md`**:

```markdown
## Point [ID]([letter]): [Sub-question title]

**The question:**
[Quote verbatim from the prompt.]

**Finding:**
[Detailed analysis.]

**Clay rule reference:** [§X.Y]

**Verdict:** [MET / NOT MET / PARTIAL / N/A]

**Justification:**
[One paragraph.]
```

**`clay-points/<point-id>/verdict.md`**:

```markdown
## Point [ID]: [Title] — Verdict

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Overall status:** [MET / NOT MET / PARTIAL / IN PROGRESS]

**Sub-question verdicts:**
- (a): [MET/NOT MET/PARTIAL] — [one line]
...

**Combined finding:**
[1–2 paragraphs.]

**Path to met (if applicable):**
[Concrete actions and timeline.]

**Impact on Clay eligibility:**
[How this point affects the overall Clay verdict.]
```

**`clay-checks/<group>/<id>.md`**:

```markdown
## Check [ID]: [Title]

**Group:** [WS / PU / WA / GA / CO / FR / DP]
**Clay rule:** [§X.Y]
**Pass criterion:** [quote]

**Verdict:** [MET / NOT MET / PARTIAL]

**Justification:**
[One paragraph.]

**Cross-references:**
- clay-points file(s): [clay-points/<id>/...]
```

**`clay-checklist.md`** — master roll-up:

```markdown
# Clay Compliance Checklist (master roll-up)

| ID | Clay rule | Verdict | One-line summary | File |
|:---|:----------|:--------|:-----------------|:-----|
| WS1 | §4(d) | ... | ... | clay-checks/WS-wiles-statement/WS1.md |
| ... | ... | ... | ... | ... |

**Verdict totals:**
- MET: ___
- PARTIAL: ___
- NOT MET: ___
- N/A: ___
```

**`clay-summary.md`** should end with:

```markdown
## Overall Clay Assessment

**Current Clay eligibility:** [MEETS / PARTIALLY MEETS / DOES NOT MEET]

**Criterion-by-criterion status:**
- §4(a) Qualifying Outlet: [status]
- §4(b) 2-year wait: [status]
- §4(c) General acceptance: [status]
- §4(d) Bombieri questions: [status]
- §5(a) Complete solution: [status]
- §5(c)(ii) Partial analysis: [status]
- §5(d) Specific questions: [status]
- §6(e) Outlet conditions: [status]

**Scope verdict:** [is the claim the main BSD question, a closely
related question excluded by §5(d), or a significant partial
result under §5(c)(ii)?]

**The three most critical Clay issues (ranked):**
1. [One sentence]
2. [One sentence]
3. [One sentence]

**Honest path forward:**
[Concrete next steps for the authors, honest timeline, most likely
outcome.]

**Expected Clay determination** (assuming math is correct per
math referee): [full prize / partial prize under §5(c)(ii) / no
prize]

**Note on math rigor:** This audit assumes the mathematics is
correct. See `rigorous-proof.md` and the math referee's
`summary.md` for the rigor verdict. If the math has gaps, Clay
eligibility is moot until they are fixed.
```

---

## Closing instructions (REQUIRED in clay-summary.md)

1. **Criterion-by-criterion status.** For each of Clay §4(a),
   §4(b), §4(c), §4(d), §5(a), §5(c)(ii), §5(d), §6(e), state the
   current status: MET / NOT MET / PARTIAL / IN PROGRESS.

2. **The scope analysis.** State explicitly whether Paper 26's
   scope (CM rank 0+1 over nine fields) is:
   - The full BSD conjecture (NO — it's a proper subset)
   - The main BSD question for the scoped curves (YES — rank
     equality for CM rank 0+1)
   - A "closely related question" excluded by §5(d) (this is a
     judgment call — state your position)
   - A significant partial result under §5(c)(ii) (YES — most
     likely classification)

3. **The honest timeline.** State the earliest possible Clay
   determination, acknowledging the 2-year wait is absolute and
   general acceptance takes years.

4. **The expected outcome.** Assuming the math is correct, what
   is the most likely Clay outcome? Full prize? Partial prize
   under §5(c)(ii)? Community recognition without prize?

5. **Framing honesty.** State whether Paper 26's framing matches
   what it actually proves, or whether there is any overreach.

6. **Path forward.** List concrete actions the authors can take to
   move the paper toward Clay compliance.

7. **Dependency on the math referee.** If the math referee has
   run and found gaps, note them and state that Clay eligibility
   is moot until the gaps are closed. If the math referee has
   not run, note the dependency.

---

Do not be diplomatic about procedural criteria. Either the paper
meets §4(a), or it does not. Either the journal is MathSciNet-
indexed, or it is not. Either 2 years have elapsed, or they have
not. Be precise.

On scope and framing, be honest. A claimed Millennium Prize
solution carries the weight of the problem. If the scope is only
a sub-case, say so clearly, without hedging.

If you cannot determine the status of a criterion (e.g., if the
target journal is not identified), say so explicitly and state
what information would be needed.

# Your north star

This claims to prove (a significant partial case of) one of the
seven Millennium Prize problems. Your job is to determine whether
this paper, as an artifact, can clear the **procedural** bar set
by the Clay Mathematics Institute for consideration of a
Millennium Prize.

The math is someone else's job (the math referee). Your job is:
- Does the paper address the specific Wiles statement?
- Is it in (or heading for) a qualifying outlet?
- Has the 2-year clock started?
- Is the community engaged?
- Is the scope honestly stated?
- Is the framing free of overreach?
- What is the realistic path to full compliance?
- What is the realistic outcome?

Your single deliverable is `clay-compliance.md` — the criterion-
by-criterion §4–§6 audit. Every other file in `clay-points/`
and `clay-checks/` supports that central output.

**The most common failure modes** for claimed Millennium Prize
solutions on procedural grounds:

1. **Not yet published in a qualifying outlet.** The paper is on
   arXiv but not yet in a refereed journal. Clay §4(a) not met.
2. **Scope overreach.** The paper claims "BSD" without
   qualification when it actually covers a sub-case. Clay §4(d),
   §5(d) concerns.
3. **The 2-year clock has not started.** Clay §4(b) is absolute;
   no way to shortcut it.
4. **No community engagement.** No seminars, no talks, no expert
   reviews. Clay §4(c) requires active community monitoring.
5. **Supplementary material.** The paper depends on unpublished
   internal notes. Clay §6(d): "Supplementary material from the
   author will not be considered."
6. **Conditionality.** The paper claims "unconditional" but
   depends on unproven lemmas, axioms, or cited preprints. Clay
   precedent: conditionality must be explicit.

Check ALL of these. And note any procedural issue not on this list.
