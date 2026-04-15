# Lindelöf Audit Brief (for the PAC Operator)

*DELTA from ring-traversal brief. Applies the generic projection-audit protocol to Lindelöf. Produces A (internal) + B_bare (community-standard skeleton) + C_bare (beyond-ask skeleton) in bare mode.*

*G Six and Claude Opus 4.6. 2026-04-15.*

---

## GOAL

Produce compliance-audited projection-audit deliverable for Lindelöf in **bare mode only**. Three files at end:

- **A** — `strategy/lindelof/pac-output/runs/run-NN/` (blackboard, compliance-map M×6, kills, critic, arbiter, commit-memo)
- **B_bare** — `strategy/lindelof/deliverables/lindelof-bare.md` (community-standard skeleton, ≤15pp)
- **C_bare** — `strategy/lindelof/deliverables/lindelof-beyond-bare.md` (programme bonuses, ≤15pp)

B_full / C_full DEFERRED.

---

## DELTAS FROM RING-TRAVERSAL BRIEF

### DELTA 1 — Mode
Dual: compliance-audit + bare-deliverable-synthesis. M layers × 6 requirements audit cells. Zero SILENT at end.

### DELTA 2 — Primitives
VERIFY / DECOMPOSE / CONSTRUCT / BYPASS / EXTRACT / DISCLOSE. EXCISE NOT APPLICABLE (all 6 requirements mandatory).

### DELTA 3 — Bare discipline
Theorem statements + definitions + equations + figures + numbers + citations only. No prose paragraphs.

### DELTA 4 — Output A
Standard PAC compliance-map.md: M × 6 matrix, verdict distribution per requirement, SILENT actions, arbiter trail.

### DELTA 5 — B_bare structure
§1 Claim verbatim / §2 Main Theorem (μ(1/2) = 0) / §3 Requirements map (6-row table) / §4 Definitions / §5-§10 Per-requirement sections / §11 Proof-Chain Analytics / §12 Named Walls / §13 Numbers Table / §14 References.

### DELTA 6 — C_bare structure
§1 5D Geometric Derivation (how CCM spectral → zeta bounds) / §2 Zero Free Parameters / §3 Pins (moment-value pins if any) / §4 Cross-Projection (RH, GRH, Katz-Sarnak connections) / §5 Bonus Theorems / §6 Computed Numerical Values / §7 Proof-Chain Analytics / §8 References.

**§N Related Work & Acknowledgments** (MANDATORY, drawn from `strategy/_research/lindelof/landscape.md`):

Researcher table (top 14):
- Larry Guth (MIT) — Decoupling, 2024 large value estimates
- James Maynard (Oxford) — Dirichlet polynomial large values
- Kannan Soundararajan (Stanford) — Moments, weak subconvexity
- Maksym Radziwiłł (Caltech) — Zero-density, moments
- Roger Heath-Brown (Oxford) — Moments, 12th moment, subconvexity
- Martin Huxley (Cardiff) — Exponent pair methods
- Jean Bourgain (IAS, d. 2018) — Decoupling, 13/84 bound 2017
- Philippe Michel (EPFL) — Subconvexity for GL(2)
- Akshay Venkatesh (IAS) — Subconvexity via trace formula
- Ritabrata Munshi (TIFR) — δ-method GL(3)
- Ian Petrow / Matt Young — Weyl subconvexity
- Paul Nelson (ETH) — Trace formula / representation-theoretic

Major approaches (6 paragraphs, from landscape §Major Approaches):
1. Large Value Estimates (Guth-Maynard 2024)
2. Moments of ζ (Heath-Brown, Ingham, Conrey-Ghosh)
3. Exponent Pairs / Van der Corput (Huxley, Watt)
4. Subconvexity Programme (Michel, Venkatesh, Nelson)
5. Decoupling / Harmonic Analysis (Bourgain, Guth)
6. δ-Method / Circle Method (Munshi)

Our programme's position: Lindelöf byproduct of RH via CCM spectral. Zero-free regions consistent with RH → classical moment bounds at Lindelöf quality. Unconditional backup via Guth-Maynard large values.

### DELTA 7 — Composition-backward
B_full / C_full DEFERRED until B_bare + C_bare LOCK.

### DELTA 8 — Citation discipline
Every claim cites `(paper45-lindelof §X Theorem T.Y)` format.

### DELTA 9 — Publication override
Zenodo → GitHub → arXiv → Annals / Invent / JAMS → 2-year clock. Overrides `publishing/strategy.md`.

### DELTA 10 — Named wall disclosure
- W_L1 (RH-conditional bound) — chain location TBD after audit; programme location paper45 §X; status OPEN-BUT-ADDRESSED; bypass route = Guth-Maynard 2024 large value + CCM unconditional zero-free region; aggregate confidence 0.7; effect-if-pass W_L1→PROVED; effect-if-fail alternate via Heath-Brown 12th moment.

### DELTA 11 — Special provisions
None. Community-standard target. No §5b-equivalent either-direction.

---

## PROCEDURE

Step 1 — Read inputs (mandatory, in order)
1. `strategy/lindelof/00-audit-strategy.md`
2. `solutions/paper45-lindelof/PROOF-CHAIN.md`
3. `strategy/x-ray/proof-chain/lindelof/X-RAY.md` (if exists)
4. `strategy/_research/lindelof/outlet.md`
5. `strategy/_research/lindelof/landscape.md`

Step 2 — Build compliance map (M × 6 cells; verdict + citation + arbiter per cell)

Step 3 — Address SILENT (DECOMPOSE / CONSTRUCT / BYPASS)

Step 4 — Synthesize B_bare (fixed 14-section structure above)

Step 5 — Synthesize C_bare (fixed 8-section structure + §N Related Work)

Step 6 — Verification pass (critic: no prose / all cited / no SILENT / all walls disclosed / ≤15pp)

Step 7 — Commit memo (LOCKED / NOT-LOCKED)

---

## SUCCESS CRITERIA

- M × 6 audited, zero SILENT
- B_bare + C_bare bare discipline, every claim cited
- Named walls disclosed with DELTA 10 fields
- Critic PUBLISH-READY verdict
- §N Related Work populated from landscape.md

---

## INVOCATION STYLE B — Agent-tool sub-agent spawning

```
You are the PAC operator for lindelof. Run <RUN-NN>. BARE MODE ONLY.

READ FIRST (in order):
1. /Users/gsix/quantum-geometry-in-5d-latex/strategy/lindelof/00-audit-strategy.md
2. /Users/gsix/quantum-geometry-in-5d-latex/strategy/lindelof/lindelof-audit-brief.md
3. /Users/gsix/quantum-geometry-in-5d-latex/solutions/paper45-lindelof/PROOF-CHAIN.md
4. /Users/gsix/quantum-geometry-in-5d-latex/strategy/_research/lindelof/outlet.md
5. /Users/gsix/quantum-geometry-in-5d-latex/strategy/_research/lindelof/landscape.md

READ AS NEEDED:
- integers/paper01-qg5d/PROOF-CHAIN.md (QG5D hub)
- strategy/ccm-verification/ledger.md (for CCM bypass)
- online-researcher-adversarial/ora-bundle-v8/
- millenium-apps/proof-chain-adversarial-01/

OUTPUTS:
- A → strategy/lindelof/pac-output/runs/<RUN-NN>/
- B_bare → strategy/lindelof/deliverables/lindelof-bare.md
- C_bare → strategy/lindelof/deliverables/lindelof-beyond-bare.md

HARD DISCIPLINE: bare mode; M×6 compliance; every claim cited; named walls disclosed; ≤15pp; §N Related Work from landscape.md.

Begin.
```

---

*G Six and Claude Opus 4.6. 2026-04-15.*
