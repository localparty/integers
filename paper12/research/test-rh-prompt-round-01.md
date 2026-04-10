# Test Report: RH Convergence Prompt — Round 01

*Date: 2026-04-09. Tester: Claude Opus 4.6 (1M). Cycle executed: 1.*

---

## 1. Did the prompt run end-to-end?

**Yes.** All four phases executed: infrastructure read (Phase 1), path identification (Phase 2), three-layer agents (Phase 3), and synthesis/ledger (Phase 4). 11 files produced (215-225 + ledger). No breaks.

## 2. Were the 4 provisioning files sufficient?

**Mostly yes.** The anchor document, theorem catalogue, RH compendium, and spectral realisation argument provided enough context for construction agents to identify open steps and attempt closure. Two gaps:
- **Path-specific research files** (research/76, 82, 08, 54, 18, 70) were referenced in the path table but NOT included in the 4-file stack. Construction agents had to infer frontier status from the compendium and catalogue summaries rather than reading the actual frontier files.
- **Paper 25 sections** (the actual conjecture statements) were referenced but not available. The catalogue summaries were adequate substitutes.

## 3. Was the path status table clear enough?

**Yes.** The 5-path table in Phase 2 clearly identified mechanisms, key files, and status. The "open:" annotations pinpointed the next step for each path. One improvement: add estimated difficulty (easy/medium/hard) per open step.

## 4. Did construction agents have enough context?

**Adequate but not ideal.** The catalogue provided theorem names and statuses. The compendium provided the constraint web. Missing: the actual mathematical CONTENT of the open steps (e.g., the explicit form of f(gamma) in Path 1). Construction agents could identify what needs to be done but could not DO it without deeper mathematical source material.

## 5. Did adversarial agents have enough separation?

**Yes.** The adversarial agents read only construction output + catalogue + compendium (not path-specific files). This prevented anchoring. The adversarial agents successfully identified weaknesses the construction agents missed (e.g., ind_BC(e_2)=0 kill risk on Path 2, ungrounded analogy on Path 4).

## 6. Was the ledger format workable?

**Yes.** The table + summary statistics format is compact and scannable. The cumulative append-only design is appropriate. One improvement: add a "risk" column (kill risk / blocked / on track).

## 7. Output quality: **6/10**

Mapping cycle — correctly identified all 5 open steps, correctly marked all as BLOCKED, produced useful adversarial challenges, and identified the strategic hub (Path 5). No false closures. But no mathematical progress: the cycle diagnosed rather than advanced.

## 8. Top 3 fixes for round 2

1. **Include path-specific frontier files** in the agent stack. The construction agents need research/76, 82, 08, 54, 70 (not just the compendium summaries) to attempt actual mathematical steps.

2. **Add a "warm-up computation" requirement** to each construction agent. Instead of "close the next step," try "close the next step; if blocked, perform the most informative sub-computation and report results." This prevents pure diagnosis cycles.

3. **Add a "kill/no-kill" check** to adversarial agents for damaged paths. The current adversarial format has no mechanism to formally KILL a path, only DAMAGE it. Paths 2 and 4 may need explicit kill decisions.

## 9. Single biggest weakness

**The prompt produces diagnosis, not mathematics.** The construction agents correctly identify what needs to be proved but cannot perform the actual computations (e.g., compute f(gamma), check KMS => Weil). The prompt needs either (a) access to a CAS/symbolic computation tool, or (b) a human mathematician to perform the identified sub-computations between cycles.
