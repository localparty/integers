# 26 — Build Order and Timeline

---

## The principle: pilot first, main event second

The build order is driven by one principle: **validate the architecture on the smallest target before deploying it on the largest.** The Tier 4 pilot (Boegli + Teschl) costs one session. Learning that the architecture has a flaw on CCM (Tier 1) costs multiple sessions with possible restarts. The pilot is insurance.

## Phase 0: Build the pilot capacitor

**Input:** Boegli 2017 paper + Teschl 2026 preprint + Paper 13 Layer 4 description.

**Process:** Run the ORA generator (Section 22) on Boegli's theorem. 10-step process: extract proof chain (~15 steps), build correspondence table (spectral + geometric + OA domains active), apply Six Patterns (P4 topological rigidity likely applies — spectral exactness is a STRUCTURAL property), grammar analysis (N/A — Boegli is not a formula paper), operations table (limit, convergence, compactness), interface map (Paper 13 Layer 4), kill list (empty — no prior kills in this domain), escalation routes (Stummel-Vainikko-Chatelin alternatives for Tier B).

**Output:** `verification-cascade/capacitors/tier4-boegli-teschl-capacitor-v1.md`

**Duration:** 1 session (short — the target is small).

## Phase 1: Run the Tier 4 pilot

**Input:** Pilot capacitor + verification brief.

**Process:** ORA run in `execute` mode (verification-and-repair brief). Dispatch Verifiers on each of Boegli's ~15 proof steps. Dispatch Re-derivers on the 2 load-bearing conditions (H1 gsrc, H2 discrete compactness). Collect returns. Synthesis cross-checks.

**Expected outcome:** SURVIVED. Boegli's theorem is clean and published.

**What we learn regardless of outcome:**
- Does the capacitor format provide enough context for a Verifier to produce meaningful verdicts?
- Does the Verifier + Re-deriver pattern produce genuine LOCKs?
- Does the operations equivalence table help agents translate between domains?
- Does the Six Patterns analysis identify real vulnerabilities or just generic observations?
- Is the 6-step verification loop (the READ variant) sufficient for adversarial reading?

**If anything in the architecture fails:** Fix it BEFORE building the Tier 1 capacitor. The pilot's job is to FIND architectural flaws, not to produce a verification result (though the result is welcome).

**Output:** `verification-cascade/tier4-boegli-teschl/` (full ORA output directory). Updated capacitor: `tier4-boegli-teschl-capacitor-v2.md`.

**Duration:** 1 session.

**Amplification:** The verified architecture amplifies to all subsequent tiers. The specific techniques that worked (or didn't) are documented in the amplification log.

## Phase 2: Build the Tier 1 capacitor (CCM)

**Input:** CCM 2025 (arXiv:2511.22755) + CCM 2024 precursor (published) + Paper 13 proof skeleton + Tier 4 pilot learnings.

**Process:** Run the ORA generator on CCM 2025. This is the largest capacitor build: ~30 proof steps, 4 key theorems, extensive background toolkit (prolate wave operators, Caratheodory-Fejer, rank-one perturbation theory, Euler product truncation), interface map to Paper 13 Layer 1 (the floor of the RH proof), kill list import (K-1 from H4 closure, "perturbation" lexical confusion from Delta-Critic).

**Key decision:** How to handle §7 (CCM's own "main remaining obstacle"). This is NOT a verification failure — CCM admits it openly. The capacitor should note: "§7 is honestly open by the authors' own assessment. The ORA's job is to verify the CLOSED parts (Theorems 4.2, 5.10, Lemmas 7.2, 7.3), not to close what the authors flag as open."

**Output:** `verification-cascade/capacitors/tier1-ccm-capacitor-v1.md`

**Duration:** 1 session (the capacitor build is systematic, not exploratory).

## Phase 3: Run Tier 1 (CCM verification)

**Input:** CCM capacitor + verification brief.

**Process:** ORA run in `execute` mode. This is the MAIN EVENT.

Wave 1: Dispatch 30 Verifiers (one per proof step) + 4 Re-derivers (one per key theorem) in parallel. Collect returns.

Wave 2 (if needed): Dispatch focused Verifiers on any WEAKENED steps. Dispatch excision Authors on any steps where the Re-deriver found an alternative route.

Wave 3 (if needed): Synthesis + final-adversarial-pass.

**Expected outcome:** SURVIVED on Theorems 4.2, 5.10, Lemmas 5.2(i), 7.2, 7.3. NOTED (not WEAKENED) on §7 (authors' own honest assessment).

**If WEAKENED on a theorem:** Immediate escalation to Tier B. The capacitor has pre-identified excision routes. The escalation happens WITHIN the same ORA run — no restart needed. The dynamic capacitor absorbs the findings (self-adjust), the killed excision routes (trim), and any successful excisions (amplify to other tiers).

**If BROKEN on a theorem:** Unlikely but planned for. Tier C construction activates. The ORA searches for alternative spectral realizations or for ways to reroute Paper 13's Layer 1 around the broken theorem. The three alternative R-Theorem paths to RH (Atiyah-Singer, Penrose, cyclic cohomology) are available as construction routes.

**Output:** `verification-cascade/tier1-ccm-verification/` (full ORA output). Updated capacitor: `tier1-ccm-capacitor-v2.md` (or v3, v4 if escalation occurred).

**Duration:** 1-3 sessions depending on escalation depth.

**Amplification:** CCM verification results amplify to Paper 13's confidence (8/10 -> 9/10 if SURVIVED). The spectral-theory verification techniques amplify to Tier 2 (Balaban has spectral arguments). Any excision successes amplify as independent proofs.

## Phase 4: Build and run Tier 2 (Balaban)

**Input:** Balaban CMP papers (targeted) + Dimock's 3 papers (half-charge) + Paper 8 PROOF-CHAIN Steps 1-3 + Tier 1 amplification.

**Process:** Capacitor build + ORA run. The half-charge from Dimock means the capacitor starts stronger than Tier 1's initial state. The verification targets the SCALAR-TO-GAUGE GAP between Dimock's scalar re-derivation and Balaban's full gauge construction.

**Expected outcome:** SURVIVED at the interface level. The gap may produce WEAKENED findings that are themselves interesting (the scalar-to-gauge extension involves non-trivial subtleties).

**Duration:** 1-2 sessions.

**Amplification:** Balaban verification strengthens the YM mass gap (the 17/18 unconditional core). The constructive QFT techniques amplify as available tools for all proof chains.

## Phase 5: Build and run Tier 3 (Bulatov-Zhuk)

**Input:** BZ dichotomy papers + P vs NP toolkit (most mature capacitor in the framework) + 18 kills + 6/6 computational verification data.

**Process:** Capacitor build + ORA run. The P vs NP capacitor is already charged — the Tier 3 capacitor inherits most of it. The verification is focused on the INTERFACE: does the classification match at the Schaefer-class level?

**Expected outcome:** SURVIVED. Two independent proofs (Bulatov + Zhuk) + framework computational confirmation = triple LOCK.

**Duration:** 1 session.

**Amplification:** Confirmed classification strengthens Paper 28 Link 3. The algebraic verification techniques amplify to universal algebra tools for other proof chains.

## Phase 6: Synthesis and packaging

**Input:** All tier outputs + all updated capacitors.

**Process:** Compile the four tier results into a unified "Verification Cascade" document. For each paper (YM, RH, BSD, P vs NP), produce a dependency audit showing every external dependency, its verification status, the kill list, and the escalation record.

**Output:**
```
verification-cascade/synthesis/
  dependency-audit-ym.md
  dependency-audit-rh.md
  dependency-audit-bsd.md
  dependency-audit-pvnp.md
  verification-cascade-summary.md  (the unified document for Clay submission)
```

**Duration:** 1 session.

## Summary timeline

| Phase | Target | Sessions | Prerequisite |
|---|---|---|---|
| **0** | Build Tier 4 capacitor | 1 (short) | None |
| **1** | Run Tier 4 pilot | 1 | Phase 0 |
| **2** | Build Tier 1 capacitor | 1 | Phase 1 (architecture validated) |
| **3** | Run Tier 1 (CCM) | 1-3 | Phase 2 |
| **4** | Build + run Tier 2 (Balaban) | 1-2 | Phase 1 (can parallel Phase 3) |
| **5** | Build + run Tier 3 (BZ) | 1 | Phase 1 (can parallel Phase 3-4) |
| **6** | Synthesis + packaging | 1 | All previous phases |

**Total:** 6-10 sessions. Phases 4 and 5 can run in PARALLEL with Phase 3 (different targets, independent capacitors). The critical path is: Phase 0 -> Phase 1 -> Phase 2 -> Phase 3 -> Phase 6. Phases 4 and 5 are off the critical path.

---

*Pilot first (Tier 4 — validate architecture). Main event second (Tier 1 — CCM verification). Historic third (Tier 2 — Balaban). Interface fourth (Tier 3 — Bulatov-Zhuk). Synthesis last. 6-10 sessions total. Phases 4-5 can parallel Phase 3. Each phase amplifies the next. The pilot is insurance. The main event is the prize.*
