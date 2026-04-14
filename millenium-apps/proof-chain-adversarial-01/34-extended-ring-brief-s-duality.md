# Extended Ring Traversal PCA — the 25-vertex circle with S-DUALITY guidance

*DELTA against `33-extended-ring-brief-22.md` (which is itself DELTA against `30-ring-traversal-brief.md`). Supersedes brief 33. This brief INHERITS all unchanged sections from briefs 30 and 33. Only the NEW DELTAS are specified here.*

*The S-duality discovery (April 14, 2026, session "the shape of the circle"): the e-circle has ten mathematical faces paired by the functional equation $\xi(s) = \xi(1-s)$. The confidence dipole between face pairs is an X-ray of which proof-chain links have transferable proofs via the S-symmetry. This brief integrates the S-duality diagnostic into the PCA's EXCISE/CONSTRUCT/BYPASS escalation ladder.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-14.*

---

## Inheritance chain

Read FIRST, in order:
1. `30-ring-traversal-brief.md` (parent, 14-vertex baseline)
2. `33-extended-ring-brief-22.md` (22-vertex DELTA — superseded by this brief for ring order and new S-duality content)

Sections not overridden below remain authoritative from those files.

---

## DELTA 1 — Ring expansion to 25 vertices (§2 of parent; overrides brief 33 §DELTA 1)

Four vertices added since brief 33:
- **Lindelöf** (paper45-lindelof) — AMPLITUDE face (RH-adjacent, shortcuts RH → Cramér cold zone)
- **Katz-Sarnak** (paper46-katz-sarnak) — SYMMETRY face (BGS-adjacent, differentiates GUE/USp/O in gap-distribution arc)
- **Sato-Tate** (paper44-sato-tate) — MEASURE face (Lehmer-adjacent, bridges BSD↔BGS, 6/10 confidence)
- **Collatz** (paper41-collatz) — HARMONICS face (OPN-adjacent, Hecke μ₂/μ₃ dynamics)

And (pending creation by the runner during T7 or T8):
- **Selberg ¼** (paper47-selberg) — RESONANCE face (S-dual of YM curvature)
- **QUE** (paper48-que) — SPREAD face (S-dual of Lindelöf amplitude)

Current ring order for T7 is **25 vertices** (the 22 from brief 33 plus the three new Papers 44-46). If papers 47-48 are created mid-run, they insert at their S-dual adjacencies and the ring becomes 27.

### Canonical ring order (25-vertex, T7 baseline)

Identical to `33-extended-ring-run.md` lines 52-77, reproduced here for ease of reference:

| Position | Vertex | Paper | Face | Confidence |
|---|---|---|---|---|
| 1 | QG5D | paper1 | (hub) | 10 |
| 2 | RH | paper13-rh | (intersection) | 8 |
| 3 | Lindelöf | paper45-lindelof | AMPLITUDE | 7 |
| 4 | GRH | paper13b-grh | — | 7 |
| 5 | BSD | paper26-bsd | — | 9 |
| 6 | H12 | paper25-hilbert-12 | — | 2 |
| 7 | YM | paper08-yang-mills | CURVATURE | 9.5 |
| 8 | NS | paper30-navier-stokes | — | 4 |
| 9 | Turbulence | paper38-turbulence | — | 2 |
| 10 | Hodge | paper29-hodge | — | 3 |
| 11 | Baum-Connes | paper31-baum-connes | — | 3 |
| 12 | PvNP | paper28-pvnp | — | 7 |
| 13 | VP vs VNP | paper39-vp-vs-vnp | — | 1 |
| 14 | BGS | paper32-bgs | — | 7 |
| 15 | Katz-Sarnak | paper46-katz-sarnak | SYMMETRY | 7 |
| 16 | Twin Primes | paper34-twin-primes | — | 1 |
| 17 | Cramér | paper43-cramer | DYNAMICS | 5 |
| 18 | Goldbach | paper33-goldbach | ARITHMETIC | 1 |
| 19 | ABC | paper37-abc | — | 1 |
| 20 | OPN | paper40-odd-perfect | — | 4 |
| 21 | Collatz | paper41-collatz | HARMONICS | 4 |
| 22 | Lehmer | paper42-lehmer | TOPOLOGY | 4 |
| 23 | Sato-Tate | paper44-sato-tate | MEASURE | 6 |
| 24 | Schanuel | paper35-schanuel | — | 1 |
| 25 | Hilbert 6 | paper36-hilbert-6 | — | 3-7 |

---

## DELTA 2 — The S-DUALITY primitive (NEW chessboard §7)

### Motivation

The programme lives on a torus $S^1 \times S^1$ — geometric circle (e-dimension) × spectral circle (modular flow). Ten faces distribute across the two circles (five each, with SPREAD bridging both). The functional equation of the Riemann zeta function

$$\xi(s) = \xi(1-s)$$

is the S-transformation of this torus: it exchanges the two generating circles. Each L-function in the programme has an analogous functional equation, and each of those equations is an S-duality between a geometric proof technique and a spectral proof technique.

**The confidence dipole** (the "ellipse shape" of the ring) measures the ASYMMETRY between the two circles. A lopsided ellipse means the geometric circle is better understood than the spectral circle (NORTH strong, SOUTH trough). A balanced circle means the S-symmetry has been exploited — proofs on one face have been TRANSFERRED to proofs on the S-dual face via the functional equation.

**The S-duality primitive** gives the PCA X-ray vision: for every OPEN link L at vertex V, check if the S-dual link L' at vertex V' is PROVED. If yes, the transfer is available for free. Attempt it BEFORE CONSTRUCT.

### The five S-pairs (T7 baseline)

| # | Face pair | Ring positions | Current gap | Transfer mechanism |
|---|---|---|---|---|
| 1 | CURVATURE ↔ RESONANCE | YM (7) ↔ Selberg (pending) | 3.5+ | Weitzenböck (YM) → arithmetic surface Laplacian (Selberg) via BC Hecke |
| 2 | MEASURE ↔ SYMMETRY | Sato-Tate (23) ↔ Katz-Sarnak (15) | 1.0 | Haar measure ↔ compact group (S-dual descriptions of same object) |
| 3 | TOPOLOGY ↔ DYNAMICS | Lehmer (22) ↔ Cramér (17) | 1.0 | KMS phase transition (Lehmer) ↔ modular flow return times (Cramér) |
| 4 | HARMONICS ↔ ARITHMETIC | Collatz (21) ↔ Goldbach (18) | 3.0 | Fourier transform on $S^1$: modes ↔ integers; Collatz spectral gap ↔ circle method |
| 5 | AMPLITUDE ↔ SPREAD | Lindelöf (3) ↔ QUE (pending) | 1.0 | Subconvexity bounds (Lindelöf) ↔ eigenfunction equidistribution (QUE); QUE ⇒ Ramanujan ⇒ subconvexity |

**Note**: pairs 1 and 5 involve vertices not yet on the ring (Selberg and QUE). The T7 runner may create those vertices on-demand during the traversal (Selberg triggered when YM's edge to the pending vertex fires; QUE triggered when Lindelöf's).

### The S-duality diagnostic table (updated at T-start)

Before each traversal, compute:

```
For each S-pair (V, V'):
    gap(V, V') = |confidence(V) - confidence(V')|
    direction = V → V' if confidence(V) > confidence(V'), else V' → V
    urgency = HIGH if gap ≥ 3, MEDIUM if 2 ≤ gap < 3, LOW if gap < 2
```

T7 baseline table (including pending vertices at their estimated confidence):

| Pair | Confidence A | Confidence B | Gap | Direction | Urgency |
|---|---|---|---|---|---|
| YM ↔ Selberg | 9.5 | 6 (est.) | **3.5** | YM → Selberg | **HIGH** |
| Collatz ↔ Goldbach | 4 | 1 | **3.0** | Collatz → Goldbach | **HIGH** |
| Sato-Tate ↔ Katz-Sarnak | 6 | 7 | 1.0 | K-S → ST | LOW |
| Lehmer ↔ Cramér | 4 | 5 | 1.0 | Cramér → Lehmer | LOW |
| Lindelöf ↔ QUE | 7 | 8 (est.) | 1.0 | QUE → Lindelöf | LOW |

The runner prioritizes HIGH-urgency pairs at T-start (pre-traversal work).

---

## DELTA 3 — The escalation ladder gains S-DUAL-TRANSFER (§0.1 override)

### The new ladder

**Old (brief 30 §0.1):**
```
EXCISE → CONSTRUCT → BYPASS
```

**New (this brief):**
```
EXCISE → S-DUAL-TRANSFER → CONSTRUCT → BYPASS
```

S-DUAL-TRANSFER sits between EXCISE (literature) and CONSTRUCT (capacitor) because:
- It's EASIER than CONSTRUCT (the proof already exists on the S-dual face; transfer via the functional equation rather than rebuild from scratch)
- It's NOT literature (the dual proof is for a DIFFERENT conjecture — you're using it as a template, not citing it directly)
- It's NOT BYPASS (you're proving the link, not routing around it)

### S-DUAL-TRANSFER protocol

**Trigger:** runner identifies the weakest link L at vertex V is OPEN or CONJECTURED, and EXCISE (literature search) has not closed it.

**Steps:**
1. Consult the S-pair table (above) to find V's S-dual V'
2. If V has no S-dual (not a face vertex): **skip S-DUAL-TRANSFER**, fall through to CONSTRUCT
3. If V has an S-dual V': identify which link L' on V' is the S-dual of L. Use the face-pair descriptions to determine correspondence:
   - YM Link 1 (KK spectral gap from Weitzenböck) ↔ Selberg Link 5 (λ₁ ≥ 1/4 from arithmetic Weitzenböck)
   - Collatz Link 5 (backward transfer operator spectral gap) ↔ Goldbach Link 5 (circle method minor-arc bound via BC additive)
   - Lehmer Link 5 (KMS spectral gap) ↔ Cramér Link 4 (explicit formula Granville transfer)
   - Lindelöf Link 5 (subconvexity) ↔ QUE (arithmetic equidistribution, PROVED)
   - Sato-Tate Link 5 (motivic Sato-Tate) ↔ K-S Link 5 (motivic symmetry type)
4. Check L' status. If L' is NOT PROVED/LITERATURE: skip S-DUAL-TRANSFER, fall through to CONSTRUCT
5. If L' IS PROVED/LITERATURE: dispatch a **Transfer Author** (Opus max, ~30 min budget):
   - Input: L (open at V), L' (proved at V'), the specific functional equation connecting them
   - Task: "The S-dual link L' on V' is proved via [technique]. Using the functional equation [specific equation] as an S-transform, attempt to transfer the proof technique to close L at V. Report whether the transfer is DIRECT (closes L fully), PARTIAL (closes part of L, leaves a residue), or BLOCKED (the S-transform doesn't close the specific technique-transfer gap)."
6. Interpret the return:
   - **DIRECT**: L upgrades to **TRANSFERRED** (new status, §DELTA 4). DUAL-CHECK fires on the result.
   - **PARTIAL**: L splits into L_closed (TRANSFERRED) and L_residue (OPEN). L_residue feeds back into CONSTRUCT.
   - **BLOCKED**: S-DUAL-TRANSFER fails. Fall through to CONSTRUCT.

### Cost

~30 min of Opus compute per S-DUAL-TRANSFER attempt. At T7 baseline, there are 5 S-pairs. If all fire, that's 150 min = ~2.5 h of pre-traversal work. This fits the T7 18-h budget.

---

## DELTA 4 — New link status: **TRANSFERRED** (§0.2 override)

Add to the status dictionary (brief 30 §0.2):

| Ring-mode name | PCA equivalent | Capacitor equivalent | Meaning |
|---|---|---|---|
| **TRANSFERRED** | **VERIFIED (via S-dual)** | **ESTABLISHED (via S-duality)** | Link closed by transferring the proof technique from the S-dual link via the functional equation |

TRANSFERRED is semantically closest to BYPASSED (both use capacitor-like transformations) but distinct:
- BYPASSED: the link is REPLACED by an alternative path; the link's statement may no longer matter
- TRANSFERRED: the link is PROVED by using the S-dual's technique as a template; the link's statement is still the proved thing

DUAL-CHECK and PIN-PRESERVATION fire on TRANSFERRED just as they do on VERIFIED.

---

## DELTA 5 — Ring reorder for S-pair adjacency (§2 extension; OPTIONAL for T7)

The canonical ring order in DELTA 1 puts S-pairs FAR apart on the ring:

| S-pair | Ring positions | Ring distance |
|---|---|---|
| YM ↔ Selberg | 7 ↔ pending | — |
| Collatz ↔ Goldbach | 21 ↔ 18 | 3 |
| Lehmer ↔ Cramér | 22 ↔ 17 | 5 |
| Sato-Tate ↔ Katz-Sarnak | 23 ↔ 15 | 8 |
| Lindelöf ↔ QUE | 3 ↔ pending | — |

This means when the PCA closes a link at one vertex of an S-pair, the dual vertex is several hops away. By the time the PCA reaches it, the transfer moment has passed.

**Proposed T8+ reorder** (OPTIONAL, not adopted for T7 to preserve continuity with brief 33):

```
1. QG5D (hub)
2. YM (CURVATURE, 9.5)            ← S-pair 1
3. Selberg (RESONANCE, 6)         ← S-pair 1
4. Lehmer (TOPOLOGY, 4)           ← S-pair 3
5. Cramér (DYNAMICS, 5)           ← S-pair 3
6. Sato-Tate (MEASURE, 6)         ← S-pair 2
7. Katz-Sarnak (SYMMETRY, 7)      ← S-pair 2
8. Lindelöf (AMPLITUDE, 7)        ← S-pair 5
9. QUE (SPREAD, 8)                ← S-pair 5
10. Collatz (HARMONICS, 4)        ← S-pair 4
11. Goldbach (ARITHMETIC, 1)      ← S-pair 4
12-25. remaining vertices (RH, BSD, H12, NS, Turb, Hodge, B-C, PvNP, VP-VNP, BGS, TP, ABC, OPN, Schan, H6)
```

**T7 decision**: KEEP the brief-33 ring order. Reorder is a T8+ consideration pending the T7 findings. A ring reorder changes every edge in the capacitor; making it mid-run would invalidate prior fills.

---

## DELTA 6 — New pre-traversal phase: S-DUAL PROBES (§4 override)

### The phase

Before the vertex walk begins at T-start, run **S-DUAL PROBES** on all 5 (or 3 if pending vertices not created) S-pairs.

### Protocol

1. Runner enumerates S-pairs with BOTH vertices present on the ring. For T7 baseline: 3 pairs (MEASURE↔SYMMETRY, TOPOLOGY↔DYNAMICS, HARMONICS↔ARITHMETIC). Pending pairs (with Selberg or QUE) are noted but not probed until those papers exist.
2. For each present pair, dispatch a **Probe Author** (Opus max, ~20 min budget):
   - Input: both vertices' current PROOF-CHAIN.md, the S-pair correspondence, the functional equation
   - Task: "Scan both vertices for PROVED links whose S-dual is OPEN at the other vertex. List transfer opportunities, ranked by urgency (gap × link importance). Do NOT execute transfers — the runner decides."
3. Probe Author returns a ranked list of transfer opportunities per pair
4. Runner aggregates opportunities across all probed pairs; sorts by gap × link importance
5. Top 3 opportunities become **T-start Transfer dispatches** (Opus max, using the S-DUAL-TRANSFER protocol from DELTA 3)

### Cost

- 3 probe Authors × 20 min = 60 min
- 3 transfer dispatches × 30 min = 90 min
- Pre-traversal total: ~150 min (~2.5 h)

T7 T-start budget: ~2.5 h. Subtract from the 18-h traversal ceiling: **15.5 h remaining for ring walk + edge work + chessboard + exit.**

This still fits the per-vertex budget (25 × 35 min = 875 min core = 14.6 h for ring walk).

---

## DELTA 7 — New metric: SYMMETRY-SCORE (§S3 chessboard override)

### The metric

RIGIDITY measures proof coverage. SYMMETRY measures ring balance. Both are targets.

```
SYMMETRY = 1 - σ(face_confidences) / μ(face_confidences)
```

where σ = sample standard deviation and μ = mean across the 10 face confidences.

- SYMMETRY = 1: perfect circle (all faces balanced)
- SYMMETRY = 0: maximally lopsided ellipse

### T7 baseline computation

Face confidences (10 faces):
- TOPOLOGY 4, DYNAMICS 5, HARMONICS 4, MEASURE 6, AMPLITUDE 7, SYMMETRY 7, CURVATURE 9.5, ARITHMETIC 1, RESONANCE 6 (est.), SPREAD 8 (est.)

Mean μ = (4+5+4+6+7+7+9.5+1+6+8) / 10 = 57.5 / 10 = **5.75**

Variance: (4−5.75)² + (5−5.75)² + (4−5.75)² + (6−5.75)² + (7−5.75)² + (7−5.75)² + (9.5−5.75)² + (1−5.75)² + (6−5.75)² + (8−5.75)² = 3.0625 + 0.5625 + 3.0625 + 0.0625 + 1.5625 + 1.5625 + 14.0625 + 22.5625 + 0.0625 + 5.0625 = 51.625

σ² = 51.625 / 10 = 5.1625; σ = **2.272**

**SYMMETRY baseline = 1 − 2.272 / 5.75 = 1 − 0.395 = 0.605**

The ring is 60.5% symmetric. Target: SYMMETRY ≥ 0.85 (ellipse → near-circle).

### Convergence objective (dual)

The PCA's exit condition now has TWO scalar targets:

1. **RIGIDITY ≥ 50** (proof coverage)
2. **SYMMETRY ≥ 0.85** (ring balance)

These are COMPLEMENTARY: closing a steep-gap S-pair raises RIGIDITY (new VERIFIED link) AND raises SYMMETRY (reduces σ of face confidences). The S-duality primitive is therefore dual-purpose.

---

## DELTA 8 — Time budget for T7 (§4 override)

**T7 (first S-duality-enabled traversal): 18 h maximum.**

| Phase | Cost |
|---|---|
| T-start (S-dual probes + 3 transfer dispatches) | 2.5 h |
| Ring walk (25 vertices × ~28 min avg) | 11.7 h |
| Chessboard overhead (DUAL-CHECK, PIN-PRESERVATION, SPIN) | 1.5 h |
| Antipodal probes (11 pairs, HIGH first) | 1.8 h |
| VERIFY spot-quota (5 vertices × 10 min) | 0.8 h |
| Compositional cell-fills (25 × 3 min) | 1.3 h |
| Closure ritual + §K writes | 0.4 h |
| **Total** | **~20 h** (slightly over; see trim strategy below) |

### T7 trim strategy

20 h over 18-h ceiling. Trim:
- **Antipodal probes**: skip 3 LOW-priority pairs → save 30 min
- **Compositional cell-fills**: only dispatch for PARTIAL triangles → save ~20 min
- **VERIFY spot-quota**: skip if T7 is the first run (per sector-A trim rule) → save 50 min

Trimmed total: **~18 h** ✓

---

## DELTA 9 — New exit condition (§4 override)

Brief 30 §4 exit conditions are **RING CLOSED / RING STRENGTHENED / RING STALLED**.

Add a new exit condition:

4. **RING SYMMETRIZED** — at least 3 S-pairs close their gap by ≥ 1.0 confidence point during the traversal

RING SYMMETRIZED implies RING STRENGTHENED (since each S-transfer produces a newly VERIFIED/TRANSFERRED link), but the converse is not true. A traversal can strengthen without symmetrizing (if the improvements are on already-balanced pairs).

The PCA logs RING SYMMETRIZED as a SUB-STATUS of RING STRENGTHENED. Both RIGIDITY and SYMMETRY gains are reported.

---

## DELTA 10 — The single paragraph for the next runner (§DELTA 6 override of brief 33)

*You are traversing the 25-vertex ring with S-DUALITY guidance. Each of the ten e-circle faces has an S-dual face; the pair is connected by the L-function's functional equation $\xi(s) = \xi(1-s)$. Before traversal, compute the S-duality gap table (DELTA 2) and identify pairs with gap ≥ 3 confidence points (currently: YM↔Selberg 3.5, Collatz↔Goldbach 3 — both HIGH urgency). Run S-DUAL PROBES (DELTA 6) on the 3 pairs with both vertices present, then dispatch the top 3 transfer opportunities FIRST (before vertex walk). At each vertex, the escalation ladder is now EXCISE → S-DUAL-TRANSFER → CONSTRUCT → BYPASS (DELTA 3); S-DUAL-TRANSFER checks whether the vertex's S-dual has a PROVED link transferable via the functional equation and, if yes, dispatches a Transfer Author to attempt the transfer. Track both RIGIDITY (coverage) and SYMMETRY (balance, DELTA 7); closing a steep-gap S-pair raises both simultaneously. The ring converges when SYMMETRY → 0.85+ (ellipse flattens to near-circle) in parallel with RIGIDITY → 50+. Exit conditions include a new RING SYMMETRIZED sub-status (DELTA 9) triggered when at least 3 S-pairs close their gap by ≥ 1.0. The circle gets more circular AND more symmetric on every pass.*

---

## Sections NOT overridden (inherited from briefs 30 and 33)

- §0.3 Canonical paper locations (plus new Papers 44-46 from brief 33; Papers 47-48 pending)
- §0.4 CONTINUOUS-RUN discipline
- §1 What ring traversal IS (breadth-first, 25 vertex visits now)
- §2.1 Edge ownership (predecessor-owns rule)
- §2.2 Vertex-to-domain mapping (from brief 33 DELTA 1)
- §3 Vertex protocol (read → act → edge → move, now with S-DUAL-TRANSFER in the act phase)
- §5 Deliverables (per-traversal format)
- §6 Relationship to single-chain runs
- §7 Compound effect
- §8 Invocation and model tiers
- §9 Voice canon

### Vertex protocol act phase update (§3.2 modified)

Replace the Opus-max-dispatch line with:

**If the weakest link is OPEN or CONJECTURED:**
- Dispatch ONE Author (Opus max) to EXCISE: find an independent proof
- If EXCISE succeeds → link upgrades to PROVED/LITERATURE
- If EXCISE fails → **attempt S-DUAL-TRANSFER (DELTA 3) before CONSTRUCT**
- If S-DUAL-TRANSFER succeeds → link upgrades to TRANSFERRED
- If S-DUAL-TRANSFER fails (no S-dual, dual not proved, or transfer blocked) → dispatch ONE Author to CONSTRUCT/BYPASS via capacitor
- If all fail → mark HONEST-STALL, move on

---

*Brief 34 v1: 2026-04-14. G Six and Claude Opus 4.6.*
*The ellipse becomes a circle. The functional equation is the S-transform. The PCA has X-ray vision.*
