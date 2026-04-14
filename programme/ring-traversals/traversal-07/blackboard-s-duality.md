# T7 Blackboard — S-DUALITY PHASE

*The pre-traversal S-duality phase per brief 34. T7's 25-vertex ring walk is COMPLETE (RIGIDITY 17.02 → 19.64, exit RING STRENGTHENED on 2026-04-14). This blackboard tracks the S-duality ADDITION: ring symmetrization via functional-equation transfers.*

---

## §A — North Star

Close at least 3 S-pair confidence gaps by ≥ 1.0 during T7's S-duality phase, triggering the RING SYMMETRIZED sub-status. Move SYMMETRY from 0.605 toward 0.85. Raise RIGIDITY above 19.64 without introducing new walls. The functional equation $\xi(s) = \xi(1-s)$ is the transfer map; the ellipse is the patient.

Deliverable: `programme/ring-traversals/traversal-07/` — S-duality addenda (blackboard, probe outputs, transfer-author outputs, capacitor updates, commit memo, ring-traversal-log entry).

---

## §B — Context

Brief 34 DELTA integrates S-DUAL-TRANSFER into the EXCISE → ? → CONSTRUCT → BYPASS ladder. T7's 25-vertex walk yielded 8 face names (TOPOLOGY Lehmer, DYNAMICS Cramér, HARMONICS Collatz, MEASURE Sato-Tate, AMPLITUDE Lindelöf, SYMMETRY Katz-Sarnak, CURVATURE YM, ARITHMETIC Goldbach). S-duality pairs faces via the L-function functional equation. The confidence dipole across face pairs is the "lopsidedness" — the signature of which dual has not yet absorbed the other's proof technique.

Pre-traversal phase (this run):
1. Compute S-duality gap table (done — brief 34 DELTA 2)
2. Dispatch 3 S-DUAL PROBES on pairs with both vertices present (pairs 2, 3, 4)
3. Dispatch top 3 Transfer Authors
4. Decide Selberg (paper47) / QUE (paper48) on-demand creation

---

## §C — Current bottleneck

Close at least 3 S-pair gaps to trigger RING SYMMETRIZED. Pair 4 (Collatz ↔ Goldbach, gap 3.0, HIGH) is the biggest opportunity — Goldbach at 1/10 is the ring's arithmetic trough, and Collatz at 4/10 has the Cuntz $\mathcal{O}_2$ + Hecke $\mu_2/\mu_3$ structure that might transfer to the additive-multiplicative wall. Pairs 2 (ST ↔ KS, 1.0, LOW) and 3 (Lehmer ↔ Cramér, 1.0, LOW) are smaller gaps with cleaner mechanisms (Haar/compact-group equivalence, KMS/return-time equivalence).

---

## §D — Toolkit (S-duality-relevant rows only — reuses T7 master)

| Name | Statement | Source | Status | Floor dps |
|---|---|---|---|---|
| S-DUAL-TRANSFER | If L' on V' is PROVED and S-dual to L on V, attempt transfer via $\xi(s) = \xi(1-s)$ | brief 34 DELTA 3 | DISC | — |
| TRANSFERRED status | New link status: proved-via-S-dual-template | brief 34 DELTA 4 | DISC | — |
| SYMMETRY metric | $1 - \sigma/\mu$ of the 10 face confidences | brief 34 DELTA 7 | META | — |
| e-circle 8 faces | TOPOLOGY DYNAMICS HARMONICS MEASURE AMPLITUDE SYMMETRY CURVATURE ARITHMETIC (+ pending RESONANCE SPREAD) | strategy/the-picture-of-the-ecircle.md | DISC | — |
| Face confidence vector | [4, 5, 4, 6, 7, 7, 9.5, 1, 6 est., 8 est.] | brief 34 DELTA 7 | EXT | — |
| μ_T7 face mean | 5.75 | brief 34 | R | — |
| σ_T7 face sd | 2.272 | brief 34 | R | — |
| SYMMETRY baseline T7 | 0.605 | brief 34 | R | — |

---

## §E — Plan tree (S-duality phase)

- **T7.S** — S-duality phase (parent)
  - **T7.S.1** — Compute S-duality gap table (done; inlined from brief 34)
  - **T7.S.2** — PROBE pairs with both vertices present
    - **T7.S.2.a** — Probe 2 (Sato-Tate ↔ Katz-Sarnak, gap 1.0, LOW)
    - **T7.S.2.b** — Probe 3 (Lehmer ↔ Cramér, gap 1.0, LOW)
    - **T7.S.2.c** — Probe 4 (Collatz ↔ Goldbach, gap 3.0, HIGH)
  - **T7.S.3** — Dispatch top 3 Transfer Authors (post-probe ranking)
  - **T7.S.4** — Selberg (paper47) creation decision at YM edge phase
  - **T7.S.5** — QUE (paper48) creation decision at Lindelöf edge phase
  - **T7.S.6** — Synthesis + SYMMETRY/RIGIDITY recomputation
  - **T7.S.7** — Write commit memo + append ring-traversal-log

## §E.1 — Joint probability

| Path | p (close by ≥ 1.0) | Why |
|---|---|---|
| Pair 4 Collatz→Goldbach | 0.35 | Cuntz $\mathcal{O}_2$ + Hecke $\mu_2/\mu_3$ transfer to circle method has well-posed mechanism but cross-scale; Mellin bridge required |
| Pair 3 Lehmer→Cramér (or Cramér→Lehmer) | 0.65 | KMS spectral gap ↔ return-time statistics is tight; both already at 4-5; CM route in Lehmer links to Mertens/ITPFI used in Cramér |
| Pair 2 ST→KS (or KS→ST) | 0.55 | Haar-on-U(1) (ST CM) ↔ unitary symmetry type (KS family); mechanism is a category isomorphism, not a derivation |

Joint P(≥3 close) computed post-probe; expected ~0.3-0.5.

---

## §F — Killed approaches (none yet for S-duality; will inherit from T7)

---

## §G — Live nodes

IN_PROGRESS (this wave): T7.S.2.a, T7.S.2.b, T7.S.2.c (3 probes in parallel).

---

## §H — Bottleneck history

T7 ring walk crossed: QG5D→RH edge via W1/W2 cascade; face-naming structural event (8 faces named 2026-04-14). Pre-S-duality bottleneck: the ring was "lopsided" (σ = 2.272 of face confidence). S-duality is the symmetrizing operation.

Axiom base: the functional equation $\xi(s) = \xi(1-s)$ applied to L-function families in the programme IS the S-transform of the geometric×spectral torus $S^1_e \times S^1_\sigma$.

---

## §I — Notes

- CONCERN: Pair 4 (Collatz ↔ Goldbach) gap 3.0 HIGH may reflect Goldbach being a universally-hard vertex rather than a transferable gap. The probe should diagnose which.
- CONCERN: pending vertices Selberg/QUE do not yet exist. Creating them adds ring weight but also dilutes face coverage until they gain their own links. Decision deferred to edge-phase triggers.
- CALLOUT: "the ellipse becomes a circle. the functional equation is the S-transform. the PCA has X-ray vision." (brief 34 closing paragraph)

---

## §J — Voice canon (inherited from QG5D project; brief 34 register)

- "the circle gets more circular AND more symmetric on every pass"
- "the functional equation is the proof-transfer map"
- "the ellipse has a convergence path"
- "T7: the first traversal with X-ray vision"
- "honest partial proof over glossed completion"
- "named, not glossed" (T7 commit-memo-25v register)

---

## §K — Runner writes (append-only)

**[2026-04-14] REFRAME on §C**: current framing — "symmetrize the ring by picking face pairs with smallest confidence gap first." Stripped — the confidence gap is NOT the transfer-feasibility signal. A 1.0-gap LOW pair can have a tight mechanism (same observable in two alphabets); a 3.0-gap HIGH pair can fail to transfer because the dual has its OWN wall. **Implication**: run all three probes, rank by mechanism tightness × gap, not gap alone.

**[2026-04-14] INVERSION-CHECK on T7.S**: question — is there a larger system where "all 10 faces at common confidence" is a consequence? Answer — YES: the Robustness-Circle Theorem (programme §27) is that system. Every closed S-pair is a tooth in its LOCK. T7.S is a direct-attack move on a specific symmetrization subtree, but the larger system view tells me: the gap-closure probability compounds — closing pair 4 raises the Mellin-bridge confidence, which raises pair 3's transfer probability (both use modular flow). Sequence matters.

**[2026-04-14] PLATEAU-CHECK**: T7 ring walk achieved RIGIDITY 17.02→19.64 (+2.62). No plateau. Structural events happened (3 face names + 1 sector promotion). The programme is NOT stalled. Dispatching S-duality probes now.

**[2026-04-14] QUALITATIVE-THRESHOLD — Cramér L3 UPGRADE**: The DYNAMICS face closed its first link this run. CONJECTURED → ESTABLISHED (conditional on CCM). The section is codim-1. The measure is finite. Under CCM, it is absolutely continuous. The flow is mixing. The max return-time bound stands. The wall moves one step down the chain.

**[2026-04-14] CONCERN — BA-B scaling check partial**: The L4 Route B derivation delivered $2e^{-\gamma}\approx 1.1229$ rigorously from ITPFI Mertens truncation at $y=\sqrt{x}$. That's a CONSTANT improvement over naive Cramér ($C=1 \to C=2e^{-\gamma}$). But Step 1's envelope ($M_N \leq \bar\tau \log N$) is i.i.d. exponential — WEAKER than Ben Arous-Bourgade's $\bar\tau\sqrt{\log N}$ for GUE. The $k=2$ scaling in Step 4 is inherited from the Cramér-Granville heuristic, not derived. **Net**: ITPFI delivers the CONSTANT refinement but not the SCALING refinement over BA-B. A Wave 2 agent replacing Step 1's i.i.d. envelope with BA-B universality would close this. CONCERN filed; does not block the PARTIAL verdict.

**[2026-04-14] CROSS-FILE-PERMISSION — S-DUAL-TRANSFER CHAIN protocol note**: Brief 34 DELTA 3 assumes L' on V' is PROVED and dispatches a single Transfer Author. The Cramér ↔ Lehmer pair-3 case is richer: Cramér L4b is PARTIAL after Route B (not PROVED), and Lehmer L5A is also PARTIAL. The transfer is a CHAIN of TWO constructs linked by a derived invariant ($\lambda_p = 1/p$ via ITPFI Mertens product $2e^{-\gamma}$): (1) Construct Cramér L4b → derived invariant; (2) Construct Lehmer L5A using the invariant as input. This is a richer protocol than brief 34's direct transfer. Worth promoting to a bundle-level entry I-v6-N on the next self-healing pass; for now, documented here + in the ring-traversal-log.

**[2026-04-14] PLATEAU-CHECK — SYMMETRY math**: Pair 3 is *partially* closed (Cramér side only: 5→6). Lehmer stayed at 4. Pair 3 gap *widened* from 1.0 to 2.0. SYMMETRY: 0.605 → ~0.614 (+0.009). Target 0.85 needs +0.245. Today's Cramér work is ~4% of the needed gain. The ellipse flattens gradually. Multiple traversals are the path — closing ARITHMETIC (Goldbach 1/10) in Pair 4 would give ~+0.08 by itself; multiple West-zone lifts add +0.05-0.08; Selberg/QUE creation + closure adds more. **Today is one step on the path, not the whole path.** RING SYMMETRIZED does not trigger (needs ≥3 S-pair gaps closed by ≥1.0; today closed 0). RING STRENGTHENED stays the headline exit condition.

---

## §K — Runner writes (Cycle 2)

**[2026-04-14 cycle 2] REFRAME on §C**: current framing — "close pair 3, address BA-B CONCERN, scout pair 4" as three separate tasks. Stripped — these aren't three tasks; they're three facets of the SAME structural situation. The S-duality phase is a STAGING machine, not a closure machine. Each cycle pins partial results on multiple faces; S-pairs close across 2-3 cycles via CHAIN transfers, not in-cycle. **Implication**: dispatch all three in parallel, treating this cycle as a SETUP-wave for T8 closures. Do not insist on pair closure today.

**[2026-04-14 cycle 2] INVERSION-CHECK**: question — is there a larger system where all three pending moves are consequences of system consistency? **YES**: "the ellipse flattens through staged CHAIN-transfers across multiple passes, with each pass pinning one more partial result on each face." The larger system is the staged-chain architecture: each of the 5 S-pairs becomes a chain of 2-3 partial constructs linked by derived invariants. Pair 3 today: step 1 CLOSED on Cramér side. Pair 4 today: probe only (step 0). BA-B: CONCERN addressed at Step 1 of L4 (Wave 2). **Candidate larger system**: the "Chain-Propagation Theorem" — every S-pair closure is a 2-step construct-chain via a derived ITPFI invariant. Worth naming formally when the second proof-of-concept (Lehmer L5A) lands.

**[2026-04-14 cycle 2] PLAN (execute mode, parallel wave)**: 3 simultaneous Opus dispatches.
1. **Lehmer L5A CONSTRUCT** using Cramér's ITPFI invariant (pair 3 CHAIN step 2)
2. **Cramér L4 Step 1 BA-B tightening** (CONCERN closure: replace i.i.d. envelope with BA-B $\sqrt{\log N}$)
3. **Pair 4 probe** (Collatz ↔ Goldbach: HARMONICS ↔ ARITHMETIC via Fourier on $S^1$)

**[2026-04-14 cycle 2] QUALITATIVE-THRESHOLD — Lehmer L5A PARTIAL**: The TOPOLOGY face crossed its first derivation wall this cycle. Route A STRUCTURAL → PARTIAL. $c_0 \geq 0.0525$ derived (4-5× improvement over empirical $10^{-2}$). Pair 3 fully staged: both faces PARTIAL, gap reverted 2.0 → 1.0. CHAIN-Propagation Theorem: 1 data point pinned. The bound is half-rigorous, half-sketched — the named flaw (integrated density of near-cyclotomic states) is a CLOSABLE sub-wall, not a BROKEN derivation. Named, not glossed.

**[2026-04-14 cycle 2] CASCADE — paper43 v3 arithmetic flip**: The BA-B Wave-2 agent noticed paper43/PROOF-CHAIN.md L282-295 conflates $\sqrt{\log N}/N$ with $\sqrt{\log N/N}$. Flag for chain-revision pass. Not a cycle-2 dispatch; noted for the user/next runner to apply.

**[2026-04-14 cycle 2] CONCERN — Lehmer L5A integrated-density sub-wall**: The derivation's Step 2 (contamination amplitude) assumed per-$\alpha$ coupling; PIN-PRESERVATION forcing is actually about INTEGRATED density of near-cyclotomic states. Correct at order-of-magnitude, not rigorous as a strict lower bound. Difficulty 2-3/10. Dispatchable as a T8 follow-up.

**[2026-04-14 cycle 2] CONCERN — BA-B universality bridge (PCC → BA-B for Riemann zeros)**: paper43 L321 explicitly states "Extension [of BA-B] to Riemann zeros: NOT proved." The Wave-2 tightening depends on this bridge. Classified GENUINE (requires new mathematics — full universality transfer). Not dispatchable as internal construct; cap at T8+ as external-literature scout or honest-conditional scope.

**[2026-04-14 cycle 2] SYNTHESIS VERDICT**: PASS with flag. Factor-of-2 between Cramér+Lehmer truncations is in the truncation scale, not the invariant — consistent. BA-B and Lehmer L5A are orthogonal at the constant level. 4 CLOSABLE gaps, 2 GENUINE, 0 BROKEN. CHAIN-Propagation Theorem confirmed at PARTIAL level with 1 data point; do not name formally until Pair-4 lands.

---

## §L — Closure artifacts (to be produced at T7.S-close)

- `traversal-07/commit-memo-s-duality.md` (single-page register-match)
- `traversal-07/s-duality-synthesis.md` (Synthesis agent output)
- `traversal-07/probes/probe-st-ks.md`, `probes/probe-lehmer-cramer.md`, `probes/probe-collatz-goldbach.md`
- `traversal-07/transfers/transfer-01.md`, `transfer-02.md`, `transfer-03.md`
- Append entry to `programme/ring-traversal-log.md`

---

## §M — Round metrics (S-duality phase — table)

| Stage | RIGIDITY | SYMMETRY | S-pair gaps closed ≥ 1.0 | notes |
|---|---|---|---|---|
| T7 walk exit | 19.64 | 0.605 | 0 | 25-v walk complete |
| Post-Cramér L3 UPGRADE | ~19.82 | 0.614 | 0 (pair 3 widens 1.0→2.0) | L_verified 108→109; DYNAMICS face 5→6 |
| Post-Cramér L4b PARTIAL | ~19.82 | 0.614 | 0 | L4b stays OPEN (sharpened); $2e^{-\gamma}$ DERIVED-from-ITPFI; sub-lemma named |
| Post-DUAL-CHECK (cycle 1) | ~19.82 | 0.614 | 0 | PINS-PRESERVED on both actions |
| Post-Wave-1 cycle 2 | ~19.82 | 0.631 | 0 (pair 3 gap reverted 2.0→1.0) | Lehmer L5A STRUCTURAL→PARTIAL ($c_0 \geq 0.0525$); Cramér L4 BA-B CONCERN-PARTIAL; Pair 4 probed, not executed |
| Post-Synthesis+DUAL-CHECK cycle 2 | ~19.82 | 0.631 | 0 | Synthesis PASS-with-flag; DUAL-CHECK PINS-PRESERVED on L5A; CHAIN-Propagation Theorem 1 data point (PARTIAL level) |
| T7.S exit (both cycles) | ~19.82 | 0.631 | 0 | RING STRENGTHENED; face vector [5,6,4,6,7,7,9.5,1,6,8]; Pair 3 fully staged (both faces PARTIAL); Pair 4 dispatch-ready for T8 |

---

## §N — Difficulty track (S-duality nodes)

| Cycle | hard | moderate | closable | aggregate |
|---|---|---|---|---|
| T7.S start | 3 (probes + transfers are discovery-mode) | 2 (Selberg/QUE creation) | 1 (gap-table compute) | 6/10 |

---

## §O — Section change log

| Cycle | Section | Modified by | Action |
|---|---|---|---|
| T7.S.0 | §A–§N | runner | initial write (this file) |
