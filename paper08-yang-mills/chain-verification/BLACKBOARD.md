# Blackboard — YM Chain Verification PCA Run

**Run started:** 2026-04-13
**Runner:** Claude Opus 4.6 (1M context)
**Mode:** PCA chain-verification-and-repair (`execute`)
**Cycle:** 1

---

## §A North Star

**Deliverable:** `paper08-yang-mills/strategy/05-chain-verification-brief.md`

**Target:** Independent adversarial verification of the full Yang-Mills mass-gap proof chain (18 links). Currently 17 VERIFIED + 1 CONDITIONAL on H4. Goal: CHAIN CLOSED (all 17 SURVIVE), CHAIN STRENGTHENED (any weakening repaired), or CHAIN AT RISK (honest labeling of any broken link). Link 18 remains CONDITIONAL — do NOT re-attempt H4.

**Success criterion:** Each of Links 1-17 receives a fresh adversarial Critic verdict. WEAKENED → repaired and re-verified. BROKEN → construct or bypass via capacitor or name the wall honestly. Link 18 CONDITIONAL labeling verified against W7-14 §5.3 mildest form.

---

## §B Context

**Primary chain:** `preprint/PROOF-CHAIN.md §IV.1` — 18 links, Status codes.

**Prior adversarial pass:** Run 2 (2026-04-12), 3 critics / 18 nodes, 10 SOUND / 8 WEAKENED / 0 BROKEN; all 8 repaired in Run 3. This PCA is a second, independent adversarial pass using bidirectional + capacitor architecture.

**H4 closure programme (closing-H4/):** Adjudicated 2026-04-11. Routes A/B/C failed. Route D → W7-14 §5.3 mildest form shipping. H4 stays the wall. DO NOT re-attempt.

**Chain map (18 links) — see `chain/chain-state.md` for live state.**

Domains touched by chain: SPEC, GEOM, QFT (Links 1-14 core), QFT+SPEC (Links 15-17 gradient flow), QFT+SPEC+ANT (Link 18 AF match).

---

## §C Bottleneck / open question

**The 17 proved links must withstand independent adversarial attack.** Not yet attempted: the PCA's bidirectional + capacitor architecture has not been applied to this chain. Prior adversarial pass (Run 2/3) used 3 critics; this run deploys 17 parallel critics, one per link, with dedicated Wave 1 forward/backward dispatch.

Specific vulnerability candidates (hypotheses, to be attacked):
- Links 2-3 (Balaban literature): 40-year-old polymer expansion not independently re-verified in this framework
- Links 4-5 (B1/B2 analyticity + SL(N,ℂ)): composition-of-analyticity domain tracking (repaired in Run 3; attack the repair)
- Link 10 (dev(δE_k^{d=6}) ≥ 2 non-pert): two-particle threshold at early scales (repaired in Run 3; attack the repair)
- Link 14 (Δ_∞ > 0): RG recursion telescoping (repaired in Run 3; attack the repair)
- Links 15-17 (gradient flow): Appendix L constructions not independently verified outside the YM programme
- Link 18: verify CONDITIONAL labeling matches W7-14 §5.3 mildest form

---

## §D Toolkit (named objects this run cites)

Populated on demand as Critics return verdicts. Initial seed from proof chain:

| Name | Statement | Source | Status | Rigor |
|---|---|---|---|---|
| Thm 4 (KK gap) | Δ₀^KK > 0 | preprint §4 | VERIFIED (proved) | R |
| Thm 5 (IR eq) | Δ₀^std > 0 from Δ₀^KK | preprint §4.5 | VERIFIED | R |
| B1 (analyticity) | k-indep radius for polymer activities | Part I extraction | VERIFIED | R |
| B2 (SL(N,ℂ)) | complex extension | Part II | VERIFIED | R |
| C-elim (Tr F³) | parity-odd elimination | §5.3.1 | VERIFIED | R |
| Newton dec | n ≥ 2 survives | §5.3.1 | VERIFIED | R |
| dev(Tr DF)² ≥ 2 | | §5.5.4 | VERIFIED | R |
| Dim-6 class | all ops dev ≥ 2 | §5.6 + Part III.3 | VERIFIED | R |
| RG rec | C_{k+1} = C_k/4 + C_new | §5.4 | VERIFIED | R |
| Mass gap Δ_∞ | Δ_∞ > 0 | §5.7 | VERIFIED | R |
| Grad flow L.1-L.5 | well-posedness etc. | App L §L.1 | VERIFIED | R |
| OS2'-OS4 | flowed Schwinger functions | App L §L.2 | VERIFIED | R |
| [Tr F²]_R + T_μν | L.1(i)(ii), L.3(i)-(v) | App L §§L.3-L.4 | VERIFIED | R |
| H4 | AF match + OPE | App L §L.4 | CONDITIONAL | C |

---

## §F Killed approaches (inherited from closing-H4 and prior runs)

- Route A / B / C for H4 closure: all failed (closing-H4 programme final state)
- Any bypass for H4 without Borel summability: kill pattern Distributional / External-dependency
- Redundant operators as dimension-4: kill pattern Topological (violates block-spin structure)

---

## §J Voice canon

- "THE PROOF CHAIN IS COMPLETE. THE PREPRINT IS INTEGRATED."
- "Integration Complete: The Final Report."
- "The framework did the work."
- "H4 is still the wall. The wall stays named. Paper 8 ships either way."
- From YM register: terse declarations, named ritual elements, §J register markers — match the rhythm.

---

## §K Runner writes

### Cycle 1 REFRAME (2026-04-13)

**Question:** "what if 17 proved links were proved in a register that doesn't survive independent attack?"

**Answer:** The chain survived Run 2/3 adversarial pass with 3 critics. This PCA is a second, harder test: 17 parallel critics, one per link, each instructed ONLY to break its target. Critics read primary sources, §D toolkit rows, capacitor cells. WEAKENED verdicts trigger construct; BROKEN triggers bypass via capacitor. The expectation is CHAIN STRENGTHENED — some surface weaknesses exposed and repaired. CHAIN CLOSED is the target; CHAIN AT RISK is survivable with honest labeling.

### Cycle 1 CAPACITOR-SCAN

Domain of each link:
- Links 1, 1b, 4 (KK/IR gap, B1 analyticity): SPEC+QFT → cell **Weitzenböck-Bochner spectral gap** VERIFIED; row SPEC has many filled cells
- Links 2, 3 (UV stability, polymer conv): GEOM+QFT → cell **Balaban polymer expansion** ESTABLISHED; priority cell PROB↔QFT (stochastic quant) and MICRO↔QFT (microlocal renorm) available if weakens
- Link 5 (SL(N,ℂ) ext): GEOM → standard complex analysis; cell HOM↔QFT exists as Tier-3 candidate
- Links 6-9 (C-elim, Newton dec, dev ≥ 2, dim-6): QFT+algebraic → no transposition needed (exact)
- Links 10, 10b (non-pert dev, spectral lemma): SPEC+QFT → Hastings-Koma clustering (cite as §D)
- Link 11 (C_new bound): SPEC+QFT → spectral lemma
- Link 12 (RG recursion): QFT+iterative → no transposition needed
- Link 13 (sum convergence): analytic → no transposition
- Link 14 (Δ_∞ > 0): SPEC+QFT → Weitzenböck-Bochner + telescoping
- Links 15-17 (gradient flow): QFT+SPEC → heat-kernel cell SPEC↔GEOM ESTABLISHED
- Link 18 (AF match + OPE): H4 conditional — PROB↔SPEC (Borel summability) is priority but CRITICAL for bypass only if user later wants to attempt H4

**Escape routes available** if any link weakens:
- GEOM↔QFT (Balaban polymer) — VERIFIED for Links 2-3
- SPEC↔QFT (Weitzenböck) — VERIFIED for Links 1, 4, 10b, 14
- SPEC↔GEOM (heat kernel / Seeley-DeWitt) — ESTABLISHED for Links 15-17
- MICRO↔QFT (Epstein-Glaser) — ESTABLISHED as alternative renorm framework
- PROB↔QFT (stochastic quant) — CANDIDATE, Hairer regularity structures

---

## §M Round metrics

| cycle | items touched | items CLOSED | items IN_PROGRESS | nodes SPAWNED | nodes KILLED | §D size | canary | Critic ECE | honest negatives | glossed gaps | structural events | inversion-yes ratio | token budget | bottleneck | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 17 | 0 | 17 | 0 | 0 | 14 | — | — | 0 | 0 | 0 | — | medium | 17 links OPEN | Wave 1 dispatch in progress |

---

## §O Chain state pointer

See `chain/chain-state.md` for live 18-link status.
