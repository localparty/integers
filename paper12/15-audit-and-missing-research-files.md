# Ledger 15: Audit — Missing Research Files for Existing Claims

*Per G's request: a systematic check of which claims, theorems,*
*identities, and results in the program are referenced in research*
*notes but do not yet have a dedicated research file capturing them.*
*Findings + prioritisation.*

*Date: 2026-04-09*

---

## 1. Methodology

For each of the 17 research notes (research/01 through research/17),
catalogue:
- The internal results (theorems, lemmas, derivations) the note
  PROVES or CONSTRUCTS — these are captured in the note itself.
- The external references the note CITES — these are the literature.
- The intermediate results the note RELIES ON or REFERENCES but does
  NOT prove — these are the *gaps* the audit looks for.

A gap is a result that we *use* in the research but don't have a
dedicated file capturing it. Filling the gap means writing a research
file that states the result precisely, gives the proof or proof
sketch, and is cited from the existing notes that use it.

---

## 2. Gaps Identified

### 2.1 Critical gaps (block downstream work)

**Gap 1 — The Connes–Marcolli operator-algebraic form of the
Riemann–Weil explicit formula.**

Cited in: research/02 §3.2, research/04 §3.1, research/05 §5,
research/08 §2.4, research/11, research/14 §3.5, research/17.

Status: cited as "Connes 1999" or "Connes–Marcolli 2008 Ch II §3"
but never written down precisely in a paper12 research file. This
is the *single most-cited external result* in the entire program,
and it underlies:
- The inclusion {γ_n} ⊂ spec(T_BC) (the foundation of Phase 2)
- The proof of RH as physical theorem (research/08 §2.4)
- The transposition of Theorem K.4 (research/11)
- The CCM equivalence (research/14 Part A)
- The K_{12} discussion (research/17)

Without a careful statement, every downstream use is conditional on
the reader's prior knowledge of the operator-algebraic literature.
**The operator-algebraic explicit formula deserves its own
research file** with the precise statement, the test functions
involved, the regularisation choices, and the connection to the
spectrum of T_BC.

Recommended file: `research/18-connes-marcolli-explicit-formula.md`.

**Gap 2 — The Galois orbit decomposition of H_R.**

Cited in: research/03 §6.3, research/04 §6.1, research/09 §4.2,
research/14 Part B (P2m).

Status: referenced as the structural reason for the pattern of
zero indices, the way the Galois group Gal(Q^cyc/Q) ≅ Ẑ\* acts on
H_1, and the foundation for the gauge-group correspondence. Never
computed explicitly. The structural argument of research/09
(γ_1, γ_4, γ_6, γ_8 as smallest gauge-distinguished orbits)
*depends* on the existence of this decomposition.

**Without an explicit Galois orbit decomposition file, several
claims rest on intuition rather than computation.**

Recommended file: `research/19-galois-orbit-decomposition-HR.md`.

**Gap 3 — The "open thread map".**

Status: the seven open threads (K_{12}, BC-intrinsic SU(3), OTOC
saturation, Mellin proportionality, three missing parameters,
explicit cosmic transition amplitudes, math RH) are referenced
across multiple research notes but do not have a single map
capturing their precise statements, current status, and paths to
closure.

A map would: (a) state each open thread precisely as a problem,
(b) record the relevant cited results, (c) identify the missing
ingredient for closure, (d) propose the next concrete step, (e)
flag dependencies between threads.

Recommended file: `research/20-open-thread-map.md`.

### 2.2 High-value gaps (sharpen existing work)

**Gap 4 — A unified Bost–Connes system reference note.**

Cited in: every research file that uses the BC system (research/02,
04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 17 — i.e., almost all
of them).

Status: captured fragmentarily in research/02 §2, research/04 §3,
and research/14 Part A, but not in a single comprehensive
"definition + KMS structure + GNS at β=1 + critical state + Galois
action + spectral structure" reference. A reader of any individual
research note has to assemble the BC system definition from
multiple files.

Recommended file: `research/21-bost-connes-system-reference.md`.

**Gap 5 — The cosmological constant problem dedicated note.**

Status: the 30-orders hierarchy as exp(γ_1·π²/2) ≈ 2×10³⁰ is in
research/13 Part B (one of two parts of a transposition note). It
is a major result — possibly the framework's most observationally
spectacular claim — and deserves its own dedicated research file
that doesn't share space with the CP² area law transposition.

Recommended file: `research/22-cc-hierarchy-as-spectral-gap.md`.

**Gap 6 — A framework predictions table.**

Status: `preprint/11-the-standard-model-riemann-correspondence.md`
captures the original 23 fits. After research/15 (4 new placements)
and research/16 (11 new fits), the scoreboard is now 34/37, but the
preprint file is not updated. There is no single file that tabulates
all 34+ predictions with their formulas, precisions, γ_n used, and
links to derivation/source notes.

Recommended file: `research/23-framework-predictions-master-table.md`.

(This file should be the source of truth for "what does the framework
predict?" and would be cited by the manuscript directly.)

**Gap 7 — Derivations of the OTHER framework formulas (32 of them).**

Status: only the CC formula has a derivation note (research/05).
The other 32 are empirical fits awaiting their first-principles
derivations. The strategy file (`paper12/14`) Section 4.2 lists the
top 8 to derive first: N_eff, 1/α, m_t, m_H, m_W, H_0, n_s, Y_p.

Recommended files: `research/24-derive-Neff.md`,
`research/25-derive-fine-structure.md`, `research/26-derive-mt.md`,
`research/27-derive-mH.md`, `research/28-derive-mW.md`,
`research/29-derive-H0.md`, `research/30-derive-ns.md`,
`research/31-derive-Yp.md`.

(These are the next major workpush after the audit.)

### 2.3 Medium-value gaps

**Gap 8 — The KK reduction summary for what we use.**

Cited in: research/07 §4.1.

Status: the framework's KK reduction on M⁴ × CP² × S² × S¹ is in
`paper4/preprint/03-the-explicit-kk-reduction-on-cp-s-s.md`. We
use specific results from it in research/07 but don't have a brief
summary file in paper12 itself.

Recommended file: `research/32-kk-reduction-summary.md` (brief,
~150 lines, just the results we use + cross-references to paper4).

**Gap 9 — The γ_13 dual appearance note.**

Status: γ_13 appears in TWO sub-percent formulas in this session:
- m_W = γ_2 + γ_13 (research/16, 0.012%)
- Y_p = 1/log(γ_13) (research/15, 0.043%)

This dual appearance is structurally interesting. γ_13 connects
the W boson mass (electroweak sector) to primordial helium (BBN
cosmology). What does this mean? The framework's hint: γ_13
indexes a CROSS-SECTOR observable that links electroweak and BBN.

Recommended file: `research/33-gamma-13-dual-appearance.md` (~200 lines).

**Gap 10 — The cosmic timeline detailed scenario from research/06.**

Status: research/06 gives the e-fold theorem (rigorous) and the
level-crossing mechanism (structural). The detailed scenario (when
each transition happens, what β_eff threshold, what the matter
sector looks like at each epoch) is sketched but not laid out with
the explicit β_eff dependence.

Recommended file: `research/34-cosmic-timeline-detailed-scenario.md`.

### 2.4 Lower-priority gaps

**Gap 11 — The classical Riemann–Weil explicit formula reference.**

Status: cited as the underlying analytic number theory before
Connes' operator-algebraic version. Captured implicitly in
research/05 §5.1. A brief standalone reference would help.

Recommended file: `research/35-riemann-weil-explicit-formula.md`
(brief, ~150 lines).

**Gap 12 — A "what's NOT in the framework" file.**

Status: the framework deduces 34 of 37 SM parameters and 8 framework
theorems. There are things it does NOT (yet) deduce: the choice of
4 spacetime dimensions, the choice of CP² × S² internal manifold,
the initial conditions of the universe, etc. A note collecting
these would help calibrate scope.

Recommended file: `research/36-framework-limits.md`.

---

## 3. Summary of Gap Priority

| # | Gap | File to write | Priority | Effort |
|:--|:----|:--------------|:---------|:-------|
| 1 | Connes–Marcolli explicit formula | research/18 | **Critical** | medium |
| 2 | Galois orbit decomposition of H_R | research/19 | **Critical** | medium-high |
| 3 | Open thread map | research/20 | **Critical** | low |
| 4 | BC system reference | research/21 | High | low-medium |
| 5 | CC hierarchy as spectral gap | research/22 | High | medium |
| 6 | Framework predictions master table | research/23 | High | low |
| 7 | 8 formula derivation notes | research/24–31 | High | high (8 notes) |
| 8 | KK reduction summary | research/32 | Medium | low |
| 9 | γ_13 dual appearance note | research/33 | Medium | low |
| 10 | Cosmic timeline detailed scenario | research/34 | Medium | medium |
| 11 | Classical Riemann–Weil formula | research/35 | Lower | low |
| 12 | Framework limits | research/36 | Lower | low |

**Critical gaps**: 3 files (research/18, 19, 20) — block downstream
work because they capture results that are heavily cited.

**High-value gaps**: 4 single files + 8 derivation files = 12 files
total — sharpen the existing work and form the next major work
push.

**Medium and lower**: 5 files — useful but not blocking.

**Total recommended files**: 20.

---

## 4. The Recommended Order of Closing

### Phase A — Critical gaps (2026-04-09 weekend, day 1)

1. **research/18** — Connes–Marcolli explicit formula (the most
   important reference; everything downstream depends on it).

2. **research/20** — Open thread map (a quick file that gives us
   a clear plan for the rest of the closing work).

3. **research/19** — Galois orbit decomposition of H_R (the
   computational closure that makes the structural pattern of
   research/09 rigorous).

This is roughly half a day of work.

### Phase B — High-value gaps (weekend, day 1–2)

4. **research/21** — BC system reference (a low-effort high-value
   consolidation).

5. **research/22** — CC hierarchy as spectral gap (extracting the
   30-orders result into its own dedicated note).

6. **research/23** — Framework predictions master table (a
   straightforward consolidation).

7. **research/24–31** — The 8 derivation notes for N_eff, 1/α,
   m_t, m_H, m_W, H_0, n_s, Y_p. These are the most important
   work and will take most of day 2 + day 3.

This is roughly a day to a day and a half.

### Phase C — Closing the open threads (weekend, day 2–3)

After the critical and high-value gaps are filled, dive into the
seven open threads in the order of strategy file Section 8 Step 3:

1. K_{12} rigorous (T1–T4 program of research/17)
2. BC-intrinsic SU(3) (Kirillov coadjoint method)
3. OTOC saturation (explicit BC OTOC computation)
4. Mellin proportionality (the Σ(dim R)²/C_2(R)^s = ζ identification)
5. Three remaining missing parameters
6. Explicit cosmic transition amplitudes (Landau–Zener rates)
7. Math RH (begin scoping sub-phase 3.D)

This is the rest of the weekend.

### Phase D — Medium-priority gaps and the next round of transpositions

If time permits after phases A–C:

- research/32–36 (medium and lower priority gaps)
- The next 8 transpositions of strategy file Section 3.4:
  Atiyah–Singer, Wess–Zumino, Coleman–Mandula+HLS, Penrose's
  singularity theorem, asymptotic freedom, anomaly cancellation,
  CKM/PMNS unitarity, Higgs mechanism

This is the work of the following week, not just the weekend.

---

## 5. What I'm Confident the Audit Did NOT Miss

For completeness, the following are *not* gaps because they are
properly captured:

- The Phase 2 construction of R̂ → research/02
- The Phase 1 closure of adiabatic continuity → research/01
- Identity 12 (e-circle ↔ BC) → research/04
- Identity 14 (CCM scaling op) → research/14 Part A
- The CC formula's structural derivation → research/05
- The cosmic e-fold theorem → research/06 Theorem A
- The shared matrix elements (Theorem B) → research/06 §4
- The eight transpositions of sub-phase 3.B → research/10–14
- The 4 missing zero placements → research/15
- The 11 missing parameter fixes → research/16
- The K_{12} numerical (and its honest negative result) → research/17
- The pattern of zero indices structural answer → research/09
- RH as physical theorem → research/08
- The seven structural results in research/13 (current state)
- The matter content (C1)–(C4) advance → research/07

These are the 17 research files we have. The audit identifies what
is *missing* on top of what we have, not what is wrong with what we
have.

---

## 6. Action Items from This Audit

(A1) Write research/18 (Connes–Marcolli explicit formula) before
any further use of "the inclusion {γ_n} ⊂ spec(T_BC)" in a derivation.

(A2) Write research/20 (open thread map) immediately to give the
weekend's work a clear plan.

(A3) Write research/19 (Galois orbit decomposition) — needed for
the rigorous version of research/09.

(A4) Write research/23 (predictions master table) before any
further claims about "23 of 37" or "34 of 37" — the scoreboard
should have a single source of truth.

(A5) Begin the eight derivation notes (research/24–31) — these are
the bulk of the "deduction programme" of strategy file Section 4–5.

(A6) After (A1)–(A5), proceed to closing the open threads in order
of strategy file Section 8 Step 3.

---

## 7. The Honest Bottom Line

The audit finds **12 gaps**, of which **3 are critical** (block
downstream work) and **9 are high-to-medium value** (sharpen and
extend the existing work).

The most important single missing file is **research/18 — the
Connes–Marcolli operator-algebraic form of the Riemann–Weil explicit
formula** — because it underlies almost every other claim and is
currently captured only by reference to the literature.

The second most important is **research/20 — the open thread map**
— because it gives the weekend's closing work a clear plan and
makes dependencies explicit.

The third is **research/19 — the Galois orbit decomposition of H_R**
— because the pattern of zero indices (research/09) and several
transposition arguments (research/10, research/14) depend on it.

After these three, the high-value gaps form the next push: a unified
BC reference, a CC hierarchy dedicated note, a predictions master
table, and the 8 derivation notes.

The audit is closed. The action items are in Section 6. The order
of closing is in Section 4.

**Recommendation**: write research/18, research/20, research/19 in
that order, then dive into the open threads from research/20's map.
The 8 derivation notes (research/24–31) can run in parallel with
the open threads or in dedicated waves.

---

## 8. References

- `00-attack-plan.md` — master ledger
- `13-current-state.md` — snapshot of rigorous/structural/open
- `14-grand-strategy-transposition-quantization-deduction.md` — the
  full long-arc strategic vision
- All `research/01` through `research/17` — the 17 existing notes

---

*The audit found 12 gaps. Three are critical, nine are high-to-*
*medium value. The single most important gap is the Connes–Marcolli*
*operator-algebraic explicit formula reference. Closing the gaps*
*before continuing is what makes the work durable. Manuscript*
*writing waits; the research is what takes time.*
