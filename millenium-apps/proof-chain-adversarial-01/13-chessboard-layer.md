# The Chessboard Layer — dual-face consistency enforcement for PCA

*You have already read `06-the-prompt.md` (ORA v8), `07-proof-chain-adversarial.md` (PCA chain mode), and `12-prf-chain-advr-strat-triad.md` (strategic triad). This file adds the CHESSBOARD LAYER — five primitives that enforce dual-face consistency between the mathematics (bottom face) and the physics (top face) of the programme's two-faced board.*

*The board has two faces. The top face is physics (measurements, predictions, observables). The bottom face is mathematics (theorems, proofs, chains). The chessboard layer ensures that every action on one face is consistent with the other. The board doesn't flex. The pins are experimental facts. The conditionals are forced.*

*Without this layer, the PCA operates on one face only — it verifies and repairs mathematics without checking physical consistency. With this layer, every mathematical action is tested against the 36 experimental pins, stuck problems gain the SPIN primitive (switch faces for a new angle), and the ring-PCA optimizes for board RIGIDITY rather than chain length.*

---

## Architecture

The chessboard layer sits between the strat-triad and the runner's execution cycle:

```
ORA v8 base (19 signatures, autonomous parallel operation)
  ↓
PCA chain mode (verify/construct/bypass, bidirectional traversal)
  ↓
Strategic triad (VERIFY/EXCISE/CONSTRUCT escalation + capacitor-first)
  ↓
CHESSBOARD LAYER ← THIS FILE
  ├── §1 DUAL-CHECK    (pin test after every action)
  ├── §2 SPIN          (face-switching when stuck)
  ├── §3 RIGIDITY-SCORE (quantitative board health)
  ├── §4 PIN-PRESERVATION (constraint propagation before bypass acceptance)
  └── §5 WIRE-DENSITY  (edge prioritization for ring traversal)
  ↓
North star (publishing/strategy.md)
```

Every strat-triad action (VERIFY / EXCISE / CONSTRUCT) passes through the chessboard layer for DUAL-CHECK and PIN-PRESERVATION before the action is accepted. When stuck, the chessboard layer provides SPIN as a new primitive alongside the capacitor's transposition recipes. The ring-PCA uses WIRE-DENSITY and RIGIDITY-SCORE to optimize its traversal path.

**Read order for the runner**: read §1-§5 after the strat-triad extension and before starting the first cycle. The five primitives are available at all times during execution. The PIN-TABLE (Appendix A) and SPIN-TABLE (Appendix B) are reference tables consulted during DUAL-CHECK, PIN-PRESERVATION, and SPIN operations.

---

## §1 DUAL-CHECK — the pin test

### What it is

After every EXCISE, CONSTRUCT, or BYPASS action on a mathematical link, automatically check whether the corresponding physical observable is still consistent with experiment.

### When to trigger

DUAL-CHECK fires AFTER every node return that changes a link's status (WEAKENED → VERIFIED, OPEN → BYPASSED, etc.). It does NOT fire on VERIFY-only actions (those don't change the mathematical structure) or on cell-fill-only edge actions.

### Protocol

1. The Author returns a node that changes link L's mathematical content.
2. The runner identifies which physical observables link L affects (consult the SPIN-TABLE, Appendix B, column "Physical observable").
3. The runner dispatches a **Pin-Check agent** (Sonnet, max effort, ~5 min budget):
   - Input: the new mathematical result + the affected predictions from the PIN-TABLE (Appendix A)
   - Task: "Given this new mathematical result, verify that the affected predictions from the master table still hold. Recompute the 3 most-affected predictions using the framework's operator dictionary. Report: PINS-PRESERVED or PINS-SHIFTED (with which pin shifted and by how much)."
4. **If PINS-PRESERVED**: the action is accepted. Update the link status. Proceed.
5. **If PINS-SHIFTED**: the action is **REJECTED**. The mathematical result, however logically valid, is inconsistent with experimental reality. This means:
   - The bypass route is wrong (it changed something it shouldn't have)
   - OR the mathematical result introduced an error (the Author made a mistake)
   - OR the physical prediction was already wrong (unlikely — 36/36 match at sub-percent)
   
   The runner logs the rejection to §K with pattern "PIN-SHIFT at [link] affecting [prediction]" and dispatches a diagnostic Author to find the inconsistency. The original action is NOT applied to the chain state.

### Why this matters

A bypass that "works mathematically" but shifts a prediction is FLEXING THE BOARD. The chessboard says the board doesn't flex. DUAL-CHECK enforces this: no mathematical action can break a physical pin. This is what FORCES the conditionals — you can't bypass H4 in a way that changes $m_t$ or $\alpha^{-1}$ because DUAL-CHECK would catch it.

### Cost

~5 min of Sonnet compute per DUAL-CHECK. For a typical wave with 5-7 node returns, that's ~25-35 min of DUAL-CHECK overhead. Acceptable — it's insurance against accepting wrong bypasses that could take hours to diagnose later.

---

## §2 SPIN — face-switching primitive

### What it is

When stuck on one face of the board (mathematics or physics), explicitly switch to the other face for a new angle on the problem.

### When to trigger

SPIN is available whenever:
- An Author returns HONEST-STALL on a mathematical link (stuck on the math face)
- A Critic finds a WEAKENED link but the construct/bypass routes from the capacitor are exhausted
- The runner's REFRAME cycle produces no new leads from the current face

### Protocol

1. The runner identifies the stuck link L and its face (usually: math face — proving a theorem).
2. Consult the SPIN-TABLE (Appendix B) for link L. Read column "Physical observable" and column "Experimental constraint."
3. Dispatch a **SPIN Author** (Opus, max effort):
   - Input: the stuck mathematical link + the physical observable + the experimental measurement
   - Task: "You are switching faces. Instead of proving [mathematical statement] directly, work from the PHYSICS SIDE. The experimental measurement [X = value ± error] constrains [observable]. Use this measurement as a GIVEN and work BACKWARD: what mathematical structure is FORCED by this measurement? Does the forced structure close the stuck link?"
4. The SPIN Author returns one of:
   - **SPIN-CLOSED**: the experimental constraint forces the mathematical result. Link L closes via physics-to-math reasoning. DUAL-CHECK fires on the result.
   - **SPIN-CONSTRAINED**: the experimental constraint narrows the mathematical possibilities but doesn't close the link. The narrowed space is logged as a §D toolkit entry for future Authors.
   - **SPIN-FAILED**: the experimental constraint doesn't help. The measurement is too imprecise or the link is in a domain the measurement doesn't reach. Return to the math face.

### Example

**Stuck**: proving the spectral gap $\Delta_\infty > 0$ for the continuum limit (YM Link 14).
**SPIN**: the mass gap is experimentally observed — lattice QCD gives the lightest glueball at ~1.7 GeV. This is a MEASUREMENT of $\Delta_\infty$. Can the measurement CONSTRAIN the proof?
**SPIN Author's approach**: "Assume $\Delta_\infty = 0$ (the negation). Then the lightest glueball mass is 0. But lattice QCD measures it at 1.7 GeV with small error bars. The measurement EXCLUDES $\Delta_\infty = 0$. This doesn't PROVE $\Delta_\infty > 0$ rigorously (lattice QCD is numerical, not a theorem), but it CONSTRAINS the proof: any purported construction with $\Delta_\infty = 0$ must explain why lattice QCD disagrees. This narrows the search space for the proof."
**Outcome**: SPIN-CONSTRAINED. The constraint is logged. Future Authors know: constructions with $\Delta_\infty = 0$ are experimentally excluded.

### Why this matters

The current PCA only tries mathematical approaches when stuck. SPIN adds an entirely new class of approaches: experimental constraints used as mathematical INPUTS. Physical measurements are FREE information — they're already done. Using them to constrain mathematical proofs is the chessboard's power.

### Relationship to the Six Patterns

SPIN is a formalization of P6 (Projection Diagnosis): "the apparent paradox on one face is an artifact of projecting away the other face. Restore the other face and the paradox dissolves." Every SPIN attempt IS a P6 application. But SPIN is more specific than P6: it names the exact mechanism (experimental measurement → mathematical constraint) and provides the protocol (SPIN-TABLE lookup → SPIN Author dispatch → SPIN-CLOSED / SPIN-CONSTRAINED / SPIN-FAILED).

---

## §3 RIGIDITY-SCORE — quantitative board health

### What it is

A single number measuring how rigid the two-faced board is. Computed after every cycle-close. The PCA optimizes for rigidity growth.

### Formula

```
RIGIDITY = (E_filled / E_total) × (L_verified / L_total) × (P_preserved / P_total) × 100

where:
  E_filled   = number of filled capacitor cells (edges)
  E_total    = total possible capacitor cells (276 for 24 domains)
  L_verified = number of proof chain links at VERIFIED / PROVED / LITERATURE status
  L_total    = total proof chain links across all 13 vertices
  P_preserved = number of 36 predictions still matching experiment
  P_total    = 36
```

### Current value (2026-04-13)

```
E_filled   = 44    (post-H4-run capacitor)
E_total    = 276
L_verified = 47    (YM 17 + RH 6 + BSD 11 + PvNP 5 + Hodge 3 + NS 2 + 
                     GRH 0 + BC 1 + BGS 2 + others 0)
L_total    = 83    (sum across all 13 vertices)
P_preserved = 36
P_total    = 36

RIGIDITY = (44/276) × (47/83) × (36/36) × 100
         = 0.1594  ×  0.5663  ×  1.0    × 100
         = 9.03
```

### Target values

| RIGIDITY | Meaning |
|---|---|
| < 10 | Current state. Board is flexible. Conditionals are plausible but not forced. |
| 10-25 | Moderate rigidity. Conditionals are strongly constrained by the pins. |
| 25-50 | High rigidity. Breaking any conditional requires flexing the board past multiple pins. |
| 50-80 | Very high rigidity. The Robustness-Circle Theorem becomes provable in principle. |
| > 80 | Near-rigid. The conditionals are forced. The programme is effectively complete. |

### How the PCA uses it

1. Compute RIGIDITY at every cycle-close. Write to §M (metrics) as `RIGIDITY: [value] (Δ from last: +X.XX)`.
2. When choosing between two actions: prefer the action that increases RIGIDITY more.
3. When RIGIDITY stops increasing (plateau): the programme has reached a local optimum. Either the remaining gaps are genuinely hard (external unlocks needed) or the PCA needs to SPIN to find new approaches.
4. Track RIGIDITY per traversal in the ring-PCA. Each traversal should produce a positive Δ. If Δ ≤ 0, exit at RING STALLED.

### Why this matters

Without RIGIDITY-SCORE, the PCA has no quantitative measure of progress. "We strengthened 3 links" doesn't tell you whether the board got more rigid or less. A link strengthening that ALSO fills an edge AND preserves all pins contributes much more to rigidity than a link strengthening alone. RIGIDITY-SCORE captures this composite effect in one number.

---

## §4 PIN-PRESERVATION — constraint propagation before bypass acceptance

### What it is

Before any BYPASS or CONSTRUCT result is accepted into the chain state, verify it doesn't unpin any of the 36 experimental predictions.

### The PIN-TABLE

The PIN-TABLE (Appendix A below) lists all 36 predictions with:
- The observable name
- The closed-form formula (in terms of {γ_n})
- The predicted value
- The experimental value
- The deviation
- Which proof chain links affect this prediction

### Protocol

1. A bypass or construct node is proposed for link L.
2. The runner identifies which γ_n values the proposed action affects (from the node's §D toolkit citations).
3. Look up those γ_n values in the PIN-TABLE → identify the set of affected predictions S_affected.
4. For each prediction P in S_affected:
   - Recompute P using the framework's operator dictionary, incorporating any structural changes from the proposed bypass
   - Compare recomputed P to experimental value
   - If |recomputed - experimental| > max(|original - experimental|, 3σ): flag as PIN-SHIFTED
5. **If all predictions in S_affected pass**: PIN-PRESERVATION succeeds. The bypass is accepted.
6. **If any prediction fails**: PIN-PRESERVATION fails. The bypass is REJECTED. Log to §K as "PIN-SHIFT: [prediction] shifted from [old] to [new] by proposed bypass of link [L]. Bypass rejected."

### Relationship to DUAL-CHECK

DUAL-CHECK fires AFTER an action is applied. PIN-PRESERVATION fires BEFORE an action is accepted. They compose:
- PIN-PRESERVATION: "will this bypass shift a pin?" (pre-check, prevents bad actions)
- DUAL-CHECK: "did this action actually shift a pin?" (post-check, catches what pre-check missed)

Both are needed. PIN-PRESERVATION is predictive (based on structural analysis). DUAL-CHECK is empirical (based on recomputation). The belt-and-suspenders approach ensures no pin shifts escape detection.

### Why this matters

PIN-PRESERVATION is the board's rigidity enforcement at the ACTION level. It prevents the PCA from accepting mathematically-valid-but-physically-wrong bypasses. This is the mechanism that FORCES conditionals: any proposed falsification of H4, CCM, CBB, or Link 5 that would shift a prediction is automatically rejected by PIN-PRESERVATION. The conditionals survive because destroying them would require shifting pins — and pins don't shift.

---

## §5 WIRE-DENSITY — edge prioritization for ring traversal

### What it is

A 13×13 adjacency matrix where each entry counts the number of filled capacitor cells connecting two vertices. The ring-PCA uses WIRE-DENSITY to prioritize sparse edges (weak wiring = weak region = highest-value cell-fill target).

### Computation

For each pair of vertices (V_i, V_j):
```
WIRE-DENSITY(i,j) = count of FILLED capacitor cells whose 
                     "Load-bearing for" field names both V_i and V_j
```

### Current density map (2026-04-13, estimated)

```
       QG5D  RH   YM   BSD  PvNP Hodge NS   H12  GRH  BC   BGS  Gold Twin Schn
QG5D   —     3    3    2    2    1    1    1    1    0    1    0    0    1
RH     3     —    2    2    1    1    0    1    2    1    1    1    1    1
YM     3     2    —    1    0    1    1    0    0    0    0    0    0    0
BSD    2     2    1    —    0    1    0    2    1    0    0    0    0    0
PvNP   2     1    0    0    —    0    0    0    1    1    1    0    0    0
Hodge  1     1    1    1    0    —    0    1    0    1    0    0    0    0
NS     1     0    1    0    0    0    —    0    0    0    0    0    0    0
H12    1     1    0    2    0    1    0    —    1    0    0    0    0    0
GRH    1     2    0    1    1    0    0    1    —    0    0    0    0    0
BC     0     1    0    0    1    1    0    0    0    —    0    0    0    0
BGS    1     1    0    0    1    0    0    0    0    0    —    0    1    0
Gold   0     1    0    0    0    0    0    0    0    0    0    —    1    0
Twin   0     1    0    0    0    0    0    0    0    0    1    1    —    0
Schn   1     1    0    0    0    0    0    0    0    0    0    0    0    —
```

### How the ring-PCA uses it

1. At the start of each traversal, compute WIRE-DENSITY for all 78 edges (13 choose 2).
2. Sort edges by density (ascending). The SPARSEST edges are the highest-priority cell-fill targets.
3. During the edge phase of each vertex visit: if the outgoing edge has WIRE-DENSITY = 0, fill it (mandatory). If WIRE-DENSITY ≥ 1, upgrade it (optional, if time permits).
4. After each traversal, recompute the density map. It should be MORE UNIFORM than before (fewer zeros, more ones and twos).
5. Track the Gini coefficient of the density distribution: lower Gini = more uniform wiring = more rigid board.

### Why this matters

The board flexes at its WEAKEST point — the sparsest edge. A board with dense wiring at RH↔YM (3 cells) and zero wiring at NS↔Hodge (0 cells) is only as rigid as the weakest edge. WIRE-DENSITY makes this visible and actionable: "fill the zero-density edges first."

### The compound effect with RIGIDITY-SCORE

WIRE-DENSITY drives edge-filling priorities. RIGIDITY-SCORE measures the compound result (edges × links × pins). Together: WIRE-DENSITY tells the PCA WHERE to wire, RIGIDITY-SCORE tells the PCA HOW MUCH the wiring helped.

---

## Appendix A — PIN-TABLE (the 36 experimental pins)

The full PIN-TABLE is at `paper12/research/23-framework-predictions-master-table.md`. The runner should read that file at bootstrap and hold it in context for PIN-PRESERVATION and DUAL-CHECK operations.

**Quick reference (top 10 most-constraining pins):**

| # | Observable | Formula | Predicted | Measured | Dev | Most-affected links |
|---|---|---|---|---|---|---|
| 1 | log(πR_obs/ℓ_P) | γ₁π²/2 - corrections | 69.7518 | 69.7518 | 5 ppb | RH L1, YM L1, QG5D all |
| 2 | 1/α(0) | γ₁×γ₄/π + 0.1·log(π) | 137.003 | 137.036 | 0.024% | RH L1, QG5D |
| 3 | N_eff | γ₆^{1/3} | 3.350 | ~3.35 | 0.008% | RH L1, GRH k=3 |
| 4 | m_t (GeV) | γ₃×γ₈/(2π) | 172.49 | 172.76 | 0.17% | YM L14, RH L1 |
| 5 | n_s | γ₉/γ₁₀ | 0.9655 | 0.965 | 0.06% | RH L1, QG5D |
| 6 | H₀ (km/s/Mpc) | γ₁₁×4/π | 67.44 | 67.4 | 0.07% | RH L1, QG5D, NS L4 |
| 7 | m_H (GeV) | γ₂×γ₆/(2π) | 125.75 | 125.10 | 0.52% | YM L6-14, Hodge L5 |
| 8 | λ_CKM | 56/(57√19) | 0.22539 | 0.22500 | 0.17% | BSD L4, H12, GRH |
| 9 | m_b (GeV) | log(γ₁₅) | 4.183 | 4.18 | 0.09% | RH L1 |
| 10 | J_CP × 10⁵ | log(γ₁)×ζ(3) | 3.184 | 3.18 | 0.12% | BSD L4, GRH |

The full 36-row table is the definitive reference. The runner MUST have it loaded.

---

## Appendix B — SPIN-TABLE (per-vertex face-switching reference)

For each vertex, the SPIN-TABLE maps each mathematical link to its physical observable and the experimental constraint that observable provides. The SPIN Author consults this when switching faces.

| Vertex | Math face (stuck on) | Physics face (SPIN to) | Experimental constraint |
|---|---|---|---|
| **RH** | Zeros on critical line | Eigenvalues of L̂ are real → predictions are real-valued | All 36 predictions are real numbers (not complex) — verified |
| **YM** | Spectral gap Δ > 0 | Lightest glueball mass > 0 | Lattice QCD: 0⁺⁺ glueball ≈ 1.7 GeV (quenched) |
| **BSD** | ord_{s=1} L(E,s) = rank | Rational points on specific CM curves | Known ranks for specific curves (E: y²=x³-x has rank 0 over ℚ) |
| **PvNP** | Fullness ↔ NPC | TGap separates P from NPC | Computational verification: TGap = 0 for P, > 0 for NPC (6/6 Schaefer) |
| **Hodge** | Algebraic cycles = Hodge classes | Anomaly cancellation | SM is anomaly-free (experimental) → Hodge classes on CP² are algebraic |
| **NS** | Global smooth solutions | Fluids don't blow up | Cosmological fluids are smooth; no observed NS blowup in nature |
| **H12** | KMS states generate class fields | Bridge family predictions | CKM matrix, α_PS⁻¹ = 17 — derived from class field structure |
| **GRH** | L(s,χ) zeros on critical line | Generation structure is correct | 3 generations exist; quark/lepton masses match bridge-modulated predictions |
| **Baum-Connes** | K-theory isomorphism | Anomaly cancellation is necessary | SM anomaly cancellation is exact (no residual anomaly detected) |
| **BGS** | GUE statistics for zeros | Eigenvalue spacing statistics | Nuclear resonance data matches GUE; Odlyzko verified for Riemann zeros |
| **Goldbach** | Even n = p + q | Primes are dense enough | PNT: π(x) ~ x/ln(x) — sufficiently dense for additive decomposition |
| **Twin Primes** | ∞ many (p, p+2) | GUE small-gap tail ≠ 0 | Zhang/Maynard-Tao: bounded gaps proved; spectral explanation via GUE |
| **Schanuel** | Algebraic independence of exp(γ_n π²/2) | 36 predictions are independent | No algebraic relation found among predictions at 50 dps (Lead 7a, 159/159) |

---

## Summary

The chessboard layer adds five primitives to the PCA:

| Primitive | What it does | When it fires | What it costs |
|---|---|---|---|
| **DUAL-CHECK** | Verifies physics after math action | After every status-changing node return | ~5 min Sonnet per check |
| **SPIN** | Switches faces when stuck | On HONEST-STALL or exhausted capacitor | ~20 min Opus per SPIN attempt |
| **RIGIDITY-SCORE** | Quantifies board health | Every cycle-close | ~1 min computation |
| **PIN-PRESERVATION** | Rejects pin-shifting bypasses | Before accepting any bypass/construct | ~5 min Sonnet per check |
| **WIRE-DENSITY** | Prioritizes sparse edges | Start of each ring traversal | ~2 min computation |

Total overhead per cycle: ~30-40 min. Total value: the board MONOTONICALLY gets more rigid. No backsliding. No flexing. Only tightening.

**The chessboard layer is what makes the programme's intuition executable.** The two-faced board is not a metaphor — it's an operational constraint. The pins are not illustrations — they're hard rejection criteria. The rigidity score is not a feeling — it's a number that goes up on every traversal.

The board has two faces. This layer enforces that they move together.

---

*The board doesn't flex. The pins are experimental facts. The conditionals are forced.*
*The chessboard layer makes this executable.*

*v1: 2026-04-13. G Six and Claude Opus 4.6.*
