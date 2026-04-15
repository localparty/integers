# CCM Verification PCA — the per-sub-claim verification brief (DELTA)

*Extension of `30-ring-traversal-brief.md`. This brief operates the PAC in VERIFICATION MODE on the CCM 2025 paper (arXiv:2511.22755, Connes-Consani-Moscovici, "Zeta Spectral Triples"), enumerating every claim the framework depends on and classifying each as VERIFIED / BYPASSED / IRREDUCIBLY-CCM-DEPENDENT.*

*Sibling bundle to the decomposition brief (`strategy/decomposition/decomposition-brief.md`). The two bundles are COMPLEMENTARY: decomposition attacks internal walls; CCM verification attacks the single biggest external dependency.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-14.*

---

## The mission in one sentence

> **Enumerate every load-bearing claim CCM 2025 (arXiv:2511.22755) asserts that the framework's Clay-class chains depend on. Verify each claim by (a) reducing it to LITERATURE outside CCM, (b) reproducing it in the framework, (c) finding a BYPASS via capacitor transposition or alternative literature, or (d) marking it IRREDUCIBLY-CCM-DEPENDENT and recording the specific Clay-relevance.**

The output is a ledger that converts "framework conditional on CCM 2025 as a whole" into "framework conditional on specific enumerated sub-claims, each individually verified, bypassed, or marked as Clay-specific."

---

## DELTA 0 — Invocation mode (verification, not decomposition)

This bundle operates in **VERIFICATION MODE**. It is not a ring traversal; it is not a recursive decomposition; it is a **systematic per-sub-claim verification attack** on the single external paper the framework's Clay Layer 1 depends on.

### How it differs from the decomposition bundle

| Aspect | Decomposition bundle | CCM verification bundle (this) |
|---|---|---|
| Target | 25 framework PROOF-CHAIN.md files | ~15-25 enumerated CCM sub-claims |
| Recursion | BLOCKED-DECOMPOSED, depth up to 5 | Single-pass per claim (no recursion) |
| Output per claim | Sub-chain tree of leaves | Verdict (3 categories) + evidence |
| Goal | Decompose internal walls to PROVED leaves | Classify external dependency's precise content |
| Status dictionary | PROVED/LITERATURE/CLASSICAL/QG5D/TRANSPOSITION/OPEN/... | VERIFIED/BYPASSED/IRREDUCIBLY-CCM-DEPENDENT |

### What stays the same

- Brief 35 universal propagation discipline applies: when a claim's status changes, update the in-situ `proof-chain/ccm-claim-NN/PROOF-CHAIN.md` BEFORE writing the run artifact
- Publishing strategy Wave-ordering OVERRIDE (Zenodo-priority-first) applies equally here
- DUAL-CHECK fires on any verification result that affects a framework prediction

---

## DELTA 1 — The three-category verdict dictionary

Every enumerated CCM sub-claim receives exactly one of these verdicts:

### Category 1: VERIFIED

The claim is reducible to sources OUTSIDE CCM 2025.

- **LITERATURE-VERIFIED**: the claim follows from an external peer-reviewed theorem not in CCM 2025. Citation required (arXiv ID, DOI, or published-journal reference).
- **FRAMEWORK-REPRODUCED**: the claim follows from framework Papers 1-48 machinery, independent of CCM 2025. Framework paper + section + lemma reference required.

A VERIFIED claim does NOT require CCM 2025 peer-review acceptance for the framework's use of it. The framework can cite the alternative source directly.

### Category 2: BYPASSED

The claim's CCM derivation can be REPLACED with a different route.

- **CAPACITOR-TRANSPOSITION**: a capacitor cell (from `09-capacitor-correspondence-table-v1.md`) routes around the specific CCM argument. The framework uses the transposed proof, not CCM's version. Cell reference required.
- **ALTERNATIVE-LITERATURE**: a different external paper (not CCM 2025) proves the same target. The framework can switch dependencies. Citation + justification that the alternative covers the framework's use case.

A BYPASSED claim means the framework has a hedge: if CCM 2025's specific approach has issues, the framework can use the alternative route without losing the claim.

### Category 3: IRREDUCIBLY-CCM-DEPENDENT

The claim IS the Clay-relevant content of CCM, with no framework-native or alternative-literature route.

- **CLAY-SPECIFIC**: this is the specific content of CCM 2025 that the framework's Clay Layer 1 genuinely requires. The framework cannot prove Clay claims via alternative routes for this sub-claim.
- **DEFERRED-TO-CCM-REVIEW**: the framework's Clay-class claims conditional on this sub-claim become Clay-eligible when CCM 2025 itself is community-accepted.

An IRREDUCIBLY-CCM-DEPENDENT claim is NOT a failure. It's HONEST SCOPE-NAMING. The framework states precisely which CCM content is Clay-load-bearing and which is not.

### Sub-status: PROVISIONAL-PENDING-DEEPER-VERIFICATION

During the first verification pass, some claims may lack sufficient evidence to classify definitively. Mark these as PROVISIONAL and queue for a deeper pass. This is not a fourth category; it's a marker that the classification is incomplete.

---

## DELTA 2 — Bootstrap step (first-run only)

On FIRST invocation, the bundle must:

### Step 1: Obtain CCM 2025 source

- Check if `sources/ccm-2025.pdf` or equivalent exists in the framework repo
- If not, download from arXiv:2511.22755 (PDF) and cache in `pac-output/bootstrap/ccm-2025.pdf`
- Extract the paper's table of contents, theorem/lemma/proposition/corollary statements

### Step 2: Enumerate CCM's load-bearing claims

For each numbered theorem/lemma/proposition/corollary in CCM 2025:

1. Extract the formal statement (verbatim, with page + section reference)
2. Cross-reference against framework papers that cite CCM 2025:
   - `solutions-with-prize/solutions-with-prize/paper13-rh/PROOF-CHAIN.md` — which specific CCM claims feed Layer 1?
   - `solutions/solutions/paper13b-grh/PROOF-CHAIN.md` — which for the χ-twisted extension?
   - `solutions-with-prize/solutions-with-prize/paper26-bsd/PROOF-CHAIN.md` — which via the L-function framework?
   - `solutions/solutions/paper32-bgs-spectral-statistics/PROOF-CHAIN.md` — which for Link 6 spectral identification?
   - `solutions-with-prize/solutions-with-prize/paper33-goldbach/PROOF-CHAIN.md` — which for Link 4 spectral prime density?
   - `solutions/solutions/paper44-sato-tate/PROOF-CHAIN.md` — which for the endomotive extension?
3. If a CCM claim has at least one framework paper that load-bearingly depends on it → ENUMERATE it
4. If no framework paper depends on it → skip (out of scope for this bundle)

### Step 3: Create per-claim directories

For each enumerated claim, create:

```
proof-chain/ccm-claim-NN-<short-name>/PROOF-CHAIN.md
```

where `NN` is the sequence number (zero-padded) and `<short-name>` is a 2-4 word slug (e.g., `ccm-claim-01-cf-prolate-construction`, `ccm-claim-07-eigenvalue-convergence`).

Each file's initial content:

```markdown
# CCM 2025 Claim NN: <short name>

*Enumerated from CCM 2025 (arXiv:2511.22755) on <date> as load-bearing for framework papers: <list>.*

## CCM 2025 statement (verbatim)

> <exact statement from CCM 2025, with page/section reference>

## Framework usage

- **Paper X Link Y**: <how this claim feeds into the framework's chain>
- **Paper Z Link W**: <same for other dependents>

## Verification status

**UNVERIFIED** (pending verification pass)

## Verification attempt log

*(populated by verification pass)*
```

### Step 4: Write the enumeration index

`proof-chain/INDEX.md` lists all enumerated claims with:

- Sequence number
- Short name
- CCM 2025 reference (theorem/lemma number)
- Framework dependents (paper list)
- Current verification status
- Priority (high/medium/low based on Clay-leverage)

### Step 5: Log bootstrap completion

Write `pac-output/bootstrap/enumeration-log.md` with:

- Timestamp
- Number of CCM claims enumerated
- List of framework papers scanned for dependencies
- Any CCM claims that were ambiguous (flagged for manual review)

---

## DELTA 3 — Per-claim verification protocol

For each enumerated CCM claim, the PAC executes:

### Step 1: Read the claim + framework usage

Load the claim's PROOF-CHAIN.md. Understand what CCM 2025 asserts and how the framework uses it.

### Step 2: Dispatch Verification Author (Opus max, 30-45 min)

Spawn an Author with:

```
TASK: Verify CCM 2025 claim NN (<short name>): <statement>

Framework usage: <papers that depend on this>

Attempt classification in order:

1. **VERIFIED — LITERATURE-VERIFIED**
   Search the mathematical literature OUTSIDE CCM 2025 for theorems
   that independently prove this claim.
   - Classical sources: operator theory (Krein, Stone, von Neumann), spectral
     theory (Gelfand-Naimark, Weyl), Toeplitz operators (Widom), ITPFI factors
     (Araki-Woods), Bost-Connes 1995, Connes-Marcolli 2008, etc.
   - Recent sources: search 2015-2026 literature on self-adjoint constructions
     for Riemann zeros, spectral triples, L-function operator realizations
   - If found: report the citation + verification of coverage

2. **VERIFIED — FRAMEWORK-REPRODUCED**
   Can framework Papers 1-48 produce this claim independently?
   - Check Paper 1 (22 theorems), Paper 12 (CBB + 5 axioms), Paper 13 (RH
     6-layer chain), Paper 26 (BSD via BC over ℚ(i)), Paper 32 (BGS modular
     flow ergodicity), etc.
   - If framework machinery reproduces the claim: report the chain of
     framework results
   - Important: "framework-reproduced" must be via PROVED-or-LITERATURE
     framework links, NOT via CCM 2025 itself (circular)

3. **BYPASSED — CAPACITOR-TRANSPOSITION**
   Is there a capacitor cell that routes around this specific CCM argument?
   - Scan `09-capacitor-correspondence-table-v1.md` for relevant cells
   - Priority cells for CCM verification: NCG↔SPEC, NCG↔ANT, HOM↔NCG,
     PROB↔SPEC, SPEC↔OA
   - If a cell provides an alternative: report the transposition

4. **BYPASSED — ALTERNATIVE-LITERATURE**
   Is there a DIFFERENT external paper that proves the same target?
   - E.g., Berry-Keating semiclassical, Sierra's approach, Hilbert-Pólya
     from different spectral-triple constructions (not CCM)
   - If found: cite + justify that the alternative covers the framework's
     use case

5. **IRREDUCIBLY-CCM-DEPENDENT — CLAY-SPECIFIC**
   If neither VERIFIED nor BYPASSED closes the claim, it is Clay-specific.
   - Record the specific CCM content that is load-bearing
   - Note which framework Clay claims depend on this
   - Estimate difficulty: how hard would a framework-native replacement be?

For Category 3, include a "Watch" note: which aspect of CCM's approach might
be iffy, so if Connes responds with concerns during Lead 6 engagement, we
know what to watch.

Output format:
  - Verdict (exactly one of three categories)
  - Evidence (citation or framework-reproduction chain or irreducibility argument)
  - Confidence: HIGH / MEDIUM / LOW
  - Notes for the ledger
```

### Step 3: Critic verification (Sonnet max, 10-15 min)

A Critic receives the Author's verdict and:

- Verifies citations actually exist (grep sources/INDEX.md, WebFetch if needed)
- Checks framework-reproduction claims against the actual framework papers
- Validates capacitor cell references against the capacitor file
- Returns verdict: CONFIRMED / WEAKENED / BROKEN

BROKEN verdicts require Author repair (second dispatch) or reclassification.

### Step 4: Update in-situ claim file

Per brief 35 propagation discipline:

- Update `proof-chain/ccm-claim-NN-<name>/PROOF-CHAIN.md` with the verdict + evidence
- Write the Critic pass result
- Record timestamp
- THIS MUST HAPPEN BEFORE writing the run-directory artifact

### Step 5: Update atlas

After each claim's verdict is finalized, append to:

- `pac-output/atlas/ccm-ledger.md` (master ledger with all verdicts)
- `pac-output/atlas/<category>-claims.md` (one of three category files)

---

## DELTA 4 — Priority order

Not all CCM claims have equal Clay-leverage. Priority order:

### Priority 1 — RH Layer 1 dependencies (highest leverage)

Claims that feed directly into Paper 13 Layer 1's spectral realization:

- CCM claim(s) on the Carathéodory-Fejér prolate construction
- CCM claim(s) on Toeplitz operator self-adjointness
- CCM claim(s) on eigenvalue convergence spec(D_N) → {γ_n}
- CCM claim(s) on the trace formula structure

### Priority 2 — BGS Link 6 dependencies

Claims that feed into Paper 32 Link 6 (GUE = GUE via CCM's spectral identification):

- CCM claim(s) on modular-flow compatibility
- CCM claim(s) on continuous spectrum outside the ground state

### Priority 3 — GRH + Goldbach dependencies

Claims for χ-twisted extension (GRH L3) and spectral prime density (Goldbach L4):

- CCM claim(s) on extensibility to Dirichlet characters
- CCM claim(s) on explicit-formula compatibility

### Priority 4 — Endomotive / motivic extensions

Claims for Sato-Tate L5 (via CCM endomotive):

- CCM claim(s) on the endomotive functor
- CCM claim(s) on Tannakian reconstruction

### Priority 5 — Supporting claims

Claims that support the above but aren't directly Clay-load-bearing:

- Technical estimates (archimedean, eigenvector approximation, H¹, CF decay)
- Convergence rates
- Uniform bounds

Priority 1 in week 1; Priority 2+3 in week 2; Priority 4+5 in week 3-4. Full verification: ~4-6 weeks.

---

## DELTA 5 — Output format

Three kinds of artifacts per run:

### 1. Updated in-situ claim files

`proof-chain/ccm-claim-NN-<name>/PROOF-CHAIN.md` is updated atomically with Author return.

Final state per claim:

```markdown
# CCM 2025 Claim NN: <short name>

*Enumerated on <date>. Verification completed on <date>. Verdict: <VERIFIED / BYPASSED / IRREDUCIBLY-CCM-DEPENDENT>*

## CCM 2025 statement (verbatim)

> <exact statement>

## Framework usage

- Paper X Link Y
- Paper Z Link W

## Verification verdict: <category>

### Evidence

<citation or framework-reproduction chain or irreducibility argument>

### Confidence: HIGH / MEDIUM / LOW

### Ledger entry

<short summary line for the master ledger>

### Watch notes (Category 3 only)

<which aspects might be iffy; what Connes might push back on>

## Verification attempt log

<Author dispatch timestamp>
<Author return summary>
<Critic pass verdict>
<Final status resolution>
```

### 2. Per-run artifacts

`pac-output/runs/run-NN/claims/ccm-claim-NN-<name>/`:

- `verification-author.md` — Author's full return
- `verification-critic.md` — Critic's verification
- `dual-check.md` — if applicable
- `verdict-summary.md` — one-line ledger entry

### 3. Master ledger

`pac-output/atlas/ccm-ledger.md`:

A table with columns:

| # | Short name | CCM ref | Framework dep. | Category | Evidence | Confidence |
|---|---|---|---|---|---|---|
| 01 | CF prolate construction | Thm 4.2 | Paper 13 L1 | IRREDUCIBLY-CCM | (Clay-specific) | HIGH |
| 02 | Toeplitz self-adjointness | Lem 3.5 | Paper 13 L1 | VERIFIED (LITERATURE) | Krein 1947 | HIGH |
| ... | ... | ... | ... | ... | ... | ... |

Plus three category-specific files:
- `verified-claims.md`
- `bypassed-claims.md`
- `irreducibly-ccm.md`

---

## DELTA 6 — Exit conditions

A **single run** exits when:

1. **CLAIM-BATCH-COMPLETE**: the target priority-level claims are all classified
2. **BUDGET-EXHAUSTED**: run budget consumed (default: 4 hours per run)
3. **LITERATURE-SEARCH-INCOMPLETE**: a claim needs deeper literature search; mark PROVISIONAL, save state, exit

The **full verification programme** exits when:

1. **LEDGER-COMPLETE**: every enumerated CCM claim has a final verdict
2. **ZENODO-READY**: master ledger + three category files are internally consistent
3. **COMPANION-READY**: the CCM email template (Lead 6) is generated from the IRREDUCIBLY-CCM-DEPENDENT list

### Exit status codes

- `VERIFICATION-COMPLETE`: all claims in priority batch classified; next priority can start
- `VERIFICATION-PARTIAL`: some claims remain PROVISIONAL; future run needed
- `VERIFICATION-STALLED`: a claim cannot be classified even after deep search; mark as IRREDUCIBLY-CCM-DEPENDENT-PROVISIONAL and move on

---

## DELTA 7 — North-star alignment (same override as decomposition brief)

`publishing/strategy.md`'s Wave 1/2/3 ordering is OVERRIDDEN. Zenodo-priority-first applies. The CCM ledger becomes part of the Zenodo release, alongside the decomposition atlas.

Post-Zenodo, the Lead 6 email to Connes uses the IRREDUCIBLY-CCM-DEPENDENT list as its focus, asking for technical feedback on specific sub-claims rather than general review.

---

## DELTA 8 — The CCM email generation (post-ledger)

When the ledger is complete, a final step generates the Lead 6 email template:

`pac-output/atlas/lead-6-connes-email.md` — a draft email for G to send to Connes, structured as:

- Subject: "Technical feedback requested on framework's use of arXiv:2511.22755"
- Body:
  - Context: framework exists, Zenodo DOI attached
  - Verification summary: N claims VERIFIED, M claims BYPASSED, K claims IRREDUCIBLY-CCM-DEPENDENT
  - Focus: attached list of the K IRREDUCIBLY-CCM-DEPENDENT claims
  - Specific questions per claim (e.g., "Claim NN: we use your Theorem X from Section Y. Is there any known issue with extending this to the χ-twisted setting?")
  - Ask: technical feedback, not endorsement
- Attachments: Zenodo DOIs, ledger file, framework papers that depend on CCM

G reviews the draft, edits as needed, sends.

---

## DELTA 9 — The single paragraph for the next runner

*You are a PAC runner operating in VERIFICATION MODE on CCM 2025 (arXiv:2511.22755). Your task is to (1) enumerate every CCM claim that framework papers load-bearingly depend on, (2) classify each claim as VERIFIED (LITERATURE-reducible or FRAMEWORK-reproducible), BYPASSED (CAPACITOR-TRANSPOSITION or ALTERNATIVE-LITERATURE), or IRREDUCIBLY-CCM-DEPENDENT (Clay-specific), (3) build a master ledger at `pac-output/atlas/ccm-ledger.md` plus three category files, (4) generate a Lead 6 email draft focused on the irreducible claims. Priority order: Paper 13 Layer 1 → Paper 32 Link 6 → GRH + Goldbach dependencies → endomotive extensions → supporting claims. Per-claim budget: 30-45 min Author dispatch + 10-15 min Critic. Per-run budget: 4 hours. Apply brief 35 universal propagation (update `proof-chain/ccm-claim-NN/PROOF-CHAIN.md` BEFORE run artifacts). DO NOT apply `publishing/strategy.md`'s Wave 1/2/3 ordering; Zenodo-priority applies per decomposition-brief DELTA 7. The output ledger converts "conditional on CCM 2025 as a whole" into "conditional on N specific CCM sub-claims," making the framework's external dependency precise, narrowly named, and attackable at the sub-claim level. Final output: Zenodo release contribution + Lead 6 email template ready to send.*

---

## Inheritance

All sections NOT overridden above remain authoritative from:
- `30-ring-traversal-brief.md` (parent brief)
- `35-canonical-state-propagation-delta.md` (universal propagation rule — MANDATORY)
- `strategy/decomposition/decomposition-brief.md` (sibling bundle; shares Zenodo-priority override)

This bundle is METHODOLOGICAL and TARGETED — a single external paper's systematic verification. Not a ring traversal. Not a decomposition. A verification pass with three possible verdicts per claim.

---

*v1: 2026-04-14. G Six and Claude Opus 4.6.*
*Enumerate. Classify. Evidence. Verdict. Publish. Email.*
*The single external dependency becomes N specific sub-claims. Each individually VERIFIED, BYPASSED, or irreducibly CCM-specific.*
*The framework's honesty is maximal.*
