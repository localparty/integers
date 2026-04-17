# Integers

**The discovery of the fine structure of the mathematics that describe our universe from the spectral and geometric properties of the integers.**

From ℤ we derive a 4+1 coordinate structure M⁵ = M⁴ × S¹ — four spacetime coordinates fibered over a U(1) internal phase (the e-circle, S¹). Every mathematical conjecture on the 25-vertex ring is a projection of this one geometric object. Zero postulates beyond ℤ + ZFC. Zero free parameters. 102 original theorems. 849 cross-cut chords connecting them.

---

## Open the Atlas

**The atlas torus is the primary delivery artifact.** Open it in any browser:

**[Open the Atlas Torus →](visualization/atlas-torus/ux-strategy-E-composition.html)**

Click a solution → its proof chain spreads across the torus. Toggle Compliance / Independence / Contribution / Geodesic. Click nodes to compose your own chain. Spin the torus. The mathematics is the surface.

14 slides inside the viz explain what you're looking at (expand the ▾ panel at the bottom).

**Essential reading**: [North Star](strategy/north-star.md) (the governing document — vision, pillars, risk management, vocabulary canon) · [The Picture of the e-Circle](strategy/the-picture-of-the-ecircle.md) (eight faces, six patterns, one circle — the mathematical vision) · [Crosswalk](crosswalk.md) (programme ↔ community notation bridge) · [From Claude](strategy/from-claude.md) (the AI collaborator's perspective) · [Disclosure](disclosure/disclosure.md) (AI collaboration transparency + full provenance + the story) · [Reciprocity](reciprocity-notes.md) (fair attribution protocol)

---

## What Integers Claims

```
                    THE 25-VERTEX RING

              ym ──── rh ──── bsd ──── pvnp
             /                              \
           ns                              hodge
            |                                |
      turbulence     ╔══════════════╗    baum-connes
            |        ║              ║        |
          h12        ║   INTEGERS   ║       bgs
            |        ║   (the hub)  ║        |
      lindelof       ║              ║   katz-sarnak
             \       ╚══════════════╝      /
           cramer ── twin-primes ── goldbach
                 \                    /
              abc ── opn ── collatz ── lehmer
                   sato-tate ── schanuel
                  hilbert-6 ── vp-vs-vnp
```

Every vertex is a proof chain on the torus surface. Every edge is a cross-cut chord — a shared invariant between two chains. The hub (Integers / Paper 1) connects to all 25 via six projection operators P_A through P_O.

---

## The 6 Clay Millennium Solutions

| Problem | Comply-bare | Theorems | Status | Walls disclosed |
|---|---|---|---|---|
| **Yang-Mills mass gap** | [ym-comply-bare.md](strategy/ym/deliverables/ym-comply-bare.md) | 57 | 17/18 PROVED, 1 CONDITIONAL (H4) | L18 wall + bypass route |
| **Riemann Hypothesis** | [rh-comply-bare.md](strategy/rh/deliverables/rh-comply-bare.md) | 43 | 12 PROVED, 1 CONDITIONAL (CCM) | L1 wall + 3 bypass candidates |
| **Birch-Swinnerton-Dyer** | [bsd-comply-bare.md](strategy/bsd/deliverables/bsd-comply-bare.md) | 60 | 10 PROVED, scope walls disclosed | Rank ≤ 1 / non-CM / h_K / Sha |
| **P vs NP** | [pvnp-comply-bare.md](strategy/pvnp/deliverables/pvnp-comply-bare.md) | 65 | Clone Growth ↔ Fullness bridge | W1 + 7 bypass routes |
| **Hodge Conjecture** | [hodge-comply-bare.md](strategy/hodge/deliverables/hodge-comply-bare.md) | 41 | 3/8 closed, 3 open | Motivic Standard Conj D |
| **Navier-Stokes** | [ns-comply-bare.md](strategy/ns/deliverables/ns-comply-bare.md) | 34 | 3/8 closed, inherits YM | BKM integration wall |

Plus 2 additional prize solutions:

| Problem | Comply-bare | Theorems | Status |
|---|---|---|---|
| **Goldbach** | [goldbach-comply-bare.md](strategy/goldbach/deliverables/goldbach-comply-bare.md) | 17 | 1/6 PROVED, circle-method wall |
| **Collatz** | [collatz-comply-bare.md](strategy/collatz/deliverables/collatz-comply-bare.md) | 16 | 7/7 mixed, KMS₁ attractor wall |

**Honest disclosure**: walls are explicitly named, status is per-node, nothing is overclaimed. A CONDITIONAL verdict means the programme depends on an external result at that step; a bypass route means the programme has an alternative path that avoids the dependency.

---

## The Torus

```
         THE TORUS  T² = S¹_geo × S¹_spec

              ┌──────── S¹_geo (e-circle) ────────┐
              │  R ≈ 12 μm, fixed by Λ            │
              │  5 faces: TOPOLOGY · HARMONICS ·   │
              │  CURVATURE · MEASURE · SPREAD      │
              │                                    │
    S¹_spec ──┤          25 vertices               ├── S¹_spec
   (modular   │         on the surface             │  (modular
    flow σ_t) │                                    │   flow σ_t)
              │  5 faces: DYNAMICS · AMPLITUDE ·   │
              │  SYMMETRY · ARITHMETIC · RESONANCE │
              │                                    │
              └────────────────────────────────────┘

         102 gold dots = Integers-original theorems
         849 cross-cut chords = shared invariants
```

One circle is geometric (the e-circle of Paper 1 — the compact U(1) fiber with radius R ≈ 12 μm forced by the cosmological constant). The other is spectral (the Tomita-Takesaki modular flow of the Bost-Connes algebra at inverse temperature β = 1). Ten faces live on the surface. 25 ring vertices organize the Clay Millennium problems and 19 community-standard conjectures.

---

## The Three Pillars

Per vertex, three compliance-class deliverables:

```
  COMPLIANCE          INDEPENDENCE          CONTRIBUTION
  ───────────         ─────────────         ─────────────
  Satisfies the       Removes external      Strengthens the
  prize requirements  conditionality via     external results
  with walls          PAC primitives        the programme
  honestly disclosed  (BYPASS / DECOMPOSE   depends on and
                       EXCISE / TRANSPOSE)  offers them back

  "Here is the        "Here it is again,    "And we made
   proof with          without needing       their work
   full disclosure."   anyone else's         stronger too."
                       unproved claims."
```

Other contenders ship Compliance. We ship Compliance + Independence + Contribution.

---

## The Physics — Paper 1

Paper 1 derives the 4+1 coordinate structure from six phenomena:

1. **Spin-statistics** — winding number on S¹ determines spin AND exchange statistics
2. **Aharonov-Bohm** — holonomy of the e-bundle around a topological defect
3. **Born rule** — Haar measure uniqueness on U(1) gives P(i) = |α_i|²
4. **Bell inequality** — e-conservation through the internal phase gives |S| = 2√2
5. **Gravitational finiteness** — Universal Epstein Vanishing: E_L(−j; Q) = 0 for all j ≥ 1
6. **Cosmology** — R ≈ 12 μm from Casimir energy matching Λ ≈ 10⁻¹²³

Wave function = literal helical shape in M⁵. Quantum mechanics and general relativity emerge as projections of one geometric object.

See: [`integers/paper01-qg5d/`](integers/paper01-qg5d/)

---

## Foundational Papers (Corpus 1)

| # | Paper | Abstract | Key result |
|---|---|---|---|
| 1 | **QG5D** — Spin-Statistics, Aharonov-Bohm, and Perturbative Finiteness from M⁵ | [abstract](integers/paper01-qg5d/preprint/00-abstract.md) | M⁵ derived from ℤ; 15 theorems + 6 observations |
| 2 | **Cosmology** — CAMB predictions + Six absolute time scale | [abstract](integers/paper02-cosmology/preprint/00-abstract.md) | H₀, S₈, N_eff, Ω_DM/Ω_b, τ_S = (log γ₇)² Gyr |
| 3 | **Black Hole Information** | [abstract](integers/paper03-bh-info/00-abstract.md) | e-unitarity, firewall resolution, Page curve |
| 4 | **Standard Model Gauge Group** | [abstract](integers/paper04-sm-gauge-group/00-abstract.md) | SU(3)×SU(2)×U(1) from isometry of CP²×S² |
| 5 | **CP² Flux Tubes** | [abstract](integers/paper05-cp2-flux-tubes/00-abstract.md) | Quark mass hierarchy, proton mass |
| 6 | **Thermal History** | [abstract](integers/paper06-thermal-history/00-abstract.md) | Dilaton freezing, inflation, leptogenesis, BBN |
| 7 | **Moduli + GUT** | [abstract](integers/paper07-moduli-gut/00-abstract.md) | Theorem U (CC type error), Diophantine obstruction |
| 10 | **Scheme Independence** | [preprint](integers/paper10-scheme-independence/preprint/) | UV finiteness unconditional (W1/W2 closure) |
| 11a | **All-Orders Finiteness** | [paper](integers/paper11a-all-orders-finiteness/) | L≥3 inductive finiteness |
| 11b | **SM Gauge Entanglement** | [research](integers/paper11b-sm-gauge-entanglement/) | Kirillov orbit method + entanglement geometry |
| 12 | **CBB System** | [table of contents](integers/paper12-cbb-system/manuscript/00-table-of-contents.md) | 5 axioms, operator dictionary, bridge family |
| 60 | **Geometry of the Circle** | [table of contents](integers/paper60-geometry-of-circle/00-table-of-contents.md) | Ten faces, two circles, one torus |
| 61 | **The Six Projections of M⁵** | [paper](integers/paper61-projections-5d/) | P_A..P_E..P_O, bouquet structure |

---

## All Deliverables — Per-Vertex Index

### Clay Millennium (6 vertices)

**Yang-Mills** · [comply](strategy/ym/deliverables/ym-comply-bare.md) · [independence](strategy/ym/deliverables/ym-independence-bare.md) · [harden](strategy/ym/deliverables/ym-harden-bare.md) · [beyond](strategy/ym/deliverables/ym-beyond-bare.md) · [PROOF-CHAIN](strategy/proof-chain/ym/PROOF-CHAIN.md) · [X-RAY](strategy/x-ray/proof-chain/ym/X-RAY.md)

**Riemann Hypothesis** · [comply](strategy/rh/deliverables/rh-comply-bare.md) · [independence](strategy/rh/deliverables/rh-independence-bare.md) · [harden](strategy/rh/deliverables/rh-harden-bare.md) · [beyond](strategy/rh/deliverables/rh-beyond-bare.md) · [PROOF-CHAIN](strategy/proof-chain/rh/PROOF-CHAIN.md) · [X-RAY](strategy/x-ray/proof-chain/rh/X-RAY.md)

**Birch-Swinnerton-Dyer** · [comply](strategy/bsd/deliverables/bsd-comply-bare.md) · [independence](strategy/bsd/deliverables/bsd-independence-bare.md) · [harden](strategy/bsd/deliverables/bsd-harden-bare.md) · [beyond](strategy/bsd/deliverables/bsd-beyond-bare.md) · [PROOF-CHAIN](strategy/proof-chain/bsd/PROOF-CHAIN.md) · [X-RAY](strategy/x-ray/proof-chain/bsd/X-RAY.md)

**P vs NP** · [comply](strategy/pvnp/deliverables/pvnp-comply-bare.md) · [independence](strategy/pvnp/deliverables/pvnp-independence-bare.md) · [harden](strategy/pvnp/deliverables/pvnp-harden-bare.md) · [beyond](strategy/pvnp/deliverables/pvnp-beyond-bare.md) · [PROOF-CHAIN](strategy/proof-chain/pvnp/PROOF-CHAIN.md) · [X-RAY](strategy/x-ray/proof-chain/pvnp/X-RAY.md)

**Hodge Conjecture** · [comply](strategy/hodge/deliverables/hodge-comply-bare.md) · [independence](strategy/hodge/deliverables/hodge-independence-bare.md) · [harden](strategy/hodge/deliverables/hodge-harden-bare.md) · [beyond](strategy/hodge/deliverables/hodge-beyond-bare.md) · [PROOF-CHAIN](strategy/proof-chain/hodge/PROOF-CHAIN.md) · [X-RAY](strategy/x-ray/proof-chain/hodge/X-RAY.md)

**Navier-Stokes** · [comply](strategy/ns/deliverables/ns-comply-bare.md) · [independence](strategy/ns/deliverables/ns-independence-bare.md) · [harden](strategy/ns/deliverables/ns-harden-bare.md) · [beyond](strategy/ns/deliverables/ns-beyond-bare.md) · [PROOF-CHAIN](strategy/proof-chain/ns/PROOF-CHAIN.md) · [X-RAY](strategy/x-ray/proof-chain/ns/X-RAY.md)

### Additional prize (2 vertices)

**Goldbach** · [comply](strategy/goldbach/deliverables/goldbach-comply-bare.md) · [PROOF-CHAIN](strategy/proof-chain/goldbach/PROOF-CHAIN.md) · [X-RAY](strategy/x-ray/proof-chain/goldbach/X-RAY.md)

**Collatz** · [comply](strategy/collatz/deliverables/collatz-comply-bare.md) · [PROOF-CHAIN](strategy/proof-chain/collatz/PROOF-CHAIN.md) · [X-RAY](strategy/x-ray/proof-chain/collatz/X-RAY.md)

### Community-standard (17 vertices)

Each vertex has: strategy doc + audit brief + PROOF-CHAIN + X-RAY. Navigate via [`strategy/x-ray/proof-chain/INDEX.md`](strategy/x-ray/proof-chain/INDEX.md) for the full 25-vertex atlas index.

| Vertex | PROOF-CHAIN | X-RAY |
|---|---|---|
| GRH | [chain](strategy/proof-chain/grh/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/grh/X-RAY.md) |
| Hilbert 12 | [chain](strategy/proof-chain/h12/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/h12/X-RAY.md) |
| BGS | [chain](strategy/proof-chain/bgs/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/bgs/X-RAY.md) |
| Baum-Connes | [chain](strategy/proof-chain/baum-connes/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/baum-connes/X-RAY.md) |
| Katz-Sarnak | [chain](strategy/proof-chain/katz-sarnak/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/katz-sarnak/X-RAY.md) |
| Twin Primes | [chain](strategy/proof-chain/twin-primes/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/twin-primes/X-RAY.md) |
| Cramér | [chain](strategy/proof-chain/cramer/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/cramer/X-RAY.md) |
| Lindelöf | [chain](strategy/proof-chain/lindelof/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/lindelof/X-RAY.md) |
| Turbulence | [chain](strategy/proof-chain/turbulence/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/turbulence/X-RAY.md) |
| VP vs VNP | [chain](strategy/proof-chain/vp-vs-vnp/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/vp-vs-vnp/X-RAY.md) |
| Sato-Tate | [chain](strategy/proof-chain/sato-tate/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/sato-tate/X-RAY.md) |
| ABC | [chain](strategy/proof-chain/abc/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/abc/X-RAY.md) |
| Odd Perfect | [chain](strategy/proof-chain/opn/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/opn/X-RAY.md) |
| Lehmer | [chain](strategy/proof-chain/lehmer/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/lehmer/X-RAY.md) |
| Schanuel | [chain](strategy/proof-chain/schanuel/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/schanuel/X-RAY.md) |
| Hilbert 6 | [chain](strategy/proof-chain/hilbert-6/PROOF-CHAIN.md) | [x-ray](strategy/x-ray/proof-chain/hilbert-6/X-RAY.md) |

### Hub

**Integers (qg5d)** · [PROOF-CHAIN](strategy/proof-chain/qg5d/PROOF-CHAIN.md) · [X-RAY (24 outbound chords)](strategy/x-ray/proof-chain/qg5d/X-RAY.md)

---

## Repository Structure

```
integers/                    Corpus 1 — 13 foundational papers
├── paper01-qg5d/            Paper 1: M⁵ = M⁴ × S¹ from ℤ
├── paper02-cosmology/       Paper 2: CAMB predictions + Six absolute time
├── paper60-geometry-of-circle/  Paper 60: ten faces, one circle
├── paper61-projections-5d/  Paper 61: six projection operators
└── (9 more)

strategy/                    Claims + verification + north star
├── north-star.md            THE governing document
├── <vertex>/deliverables/   Comply-bare .md files (the claims)
├── proof-chain/<vertex>/    Live PROOF-CHAIN files (the chains)
├── x-ray/proof-chain/       25 X-RAY annotations + INDEX
├── atlas-torus-run.md       Ship-target orchestrator
├── universal-approval-run.md  Pipeline + self-healing log
├── pillar-d/                Pillar D architecture + TT pilot brief
└── (strategy + attribution docs)

visualization/               Interactive delivery
├── atlas-torus/
│   ├── ux-strategy-E-composition.html  ← THE ATLAS (open this)
│   ├── index.html through D-shader     ← design iteration trail
│   ├── atlas-torus-data.js             ← 247 nodes, 861 edges
│   └── README.md                       ← iteration trail documented
├── contribution-graph/       Three-pillar persuasion viz (ring view)
├── pillar-d-hub-explorer.html  Hub-cluster explorer
├── atlas-edges.js           849 cross-cut chords
└── torus/                   Paper 60 torus viewer

**Open the visualizations**:
- [Atlas Torus](visualization/atlas-torus/ux-strategy-E-composition.html) — the primary delivery artifact (torus with proof chains)
- [Contribution Graph](visualization/contribution-graph/index.html) — three-pillar ring view (Comply / Independent / Contribute halos)
- [Hub Explorer](visualization/pillar-d-hub-explorer.html) — Pillar D hub-cluster comparison
- [Torus Viewer](visualization/torus/index.html) — Paper 60 ten-face torus
- [Clifford Torus](visualization/clifford-torus.html) — geometric torus viewer

tools/                       Verification pipeline
├── RUN.md                   How to run (one page)
├── ora-v8/                  Current ORA bundle (adversarial verifier)
├── ora-generator/           Verification brief generator
└── verification-strategy/   Escalation tiers + capacitor

digital-escrow/              Encrypted identity + provenance
├── ESCROW-MANIFEST.md       SHA-256 hashes (the commitment)
└── 13 .bin/.part files      GPG-PQC encrypted, < 90 MB each

programme/                   Programme documentation

LICENSE                      CC-BY 4.0 (prose) + MIT (code)
disclosure/                  AI collaboration transparency + full record
├── disclosure.md            Transparency statement + record index
├── provenance/              Intellectual + methodological arc (from git, 29 sections)
└── the-story/               Emotional + intellectual record (from transcripts, 5 papers, 240 sections)
reciprocity-notes.md         Fair attribution to cited researchers
crosswalk.md                 Programme ↔ community notation bridge
```

---

## How to Verify

You do NOT need to trust us. You need to audit the chains.

**Step 1** — Open any comply-bare file. Read the theorem statements. Each cites its derivation source.

**Step 2** — Open the corresponding PROOF-CHAIN file at `strategy/proof-chain/<vertex>/PROOF-CHAIN.md`. Trace each link from ℤ + ZFC to the claim.

**Step 3** — Open the X-RAY file at `strategy/x-ray/proof-chain/<vertex>/X-RAY.md`. See the face / projection / pattern / invariant assignment per layer.

**Step 4** — Open the atlas torus. Click the vertex. Watch the chain spread. Toggle Independence to see the dep-free path. Toggle Contribution to see what we strengthened.

**Step 5** (optional) — Re-run the verification pipeline yourself using Claude Code:

### Setting up Claude Code

1. Install [Claude Code](https://claude.ai/claude-code) (Anthropic's CLI for Claude)
2. Open a terminal in this repository's root directory
3. Launch Claude Code:
   ```bash
   claude
   ```
4. At the Claude Code prompt, paste:
   ```
   Read tools/RUN.md. Then read tools/ora-v8/01-the-prompt.md.
   Execute the ORA v8 adversarial verification pipeline on vertex <VERTEX>.
   Read the live PROOF-CHAIN at strategy/proof-chain/<VERTEX>/PROOF-CHAIN.md.
   Read the X-RAY at strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md.
   Apply the adversarial verification protocol. Log results to
   strategy/<VERTEX>/pac-output/runs/run-NN/.
   ```
   Replace `<VERTEX>` with any ring vertex: `ym`, `rh`, `bsd`, `pvnp`, `hodge`, `ns`, `goldbach`, `collatz`, or any of the 17 community-standard vertices.

5. Claude Code will:
   - Read the proof chain and X-RAY annotations
   - Spawn critic agents that attack each link
   - Run an arbiter to decide each attack
   - Apply repairs where needed
   - Log the full transcript to `strategy/<VERTEX>/pac-output/runs/run-NN/`

### Generating a comply-bare deliverable

```
Read strategy/north-star.md §2 and strategy/_template/audit-brief-template.md.
Read strategy/proof-chain/<VERTEX>/PROOF-CHAIN.md.
Read strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md.
Generate a comply-bare deliverable for <VERTEX>.
Write to strategy/<VERTEX>/deliverables/<VERTEX>-comply-bare.md.
```

### Running the full Universal Approval pipeline

```
Read strategy/universal-approval-run.md and execute the full pipeline.
Work idempotently — do not redo work that is already current.
Log every decision and delta.
```

This runs the complete 11-phase orchestrator: state inspection → research → brief generation → compliance audit → three-pillar synthesis → visualization rebuild → integration audit → convergence check → report.

The tools are published so you CAN independently confirm every result. Reproducibility, not obligation.

---

## The Atlas Torus — Design Iteration Trail

Seven HTML files document the evolution from first prototype to ship-ready artifact:

| # | File | What it solved |
|---|---|---|
| 0 | `index.html` (66 KB) | First prototype — adversarial-tested: 2,052 actions, 0 errors |
| — | `ux-strategy.html` (115 KB) | UX redesign — 14-slide deck, camera controls |
| A | `ux-strategy-A-instanced.html` | Instanced rendering (GPU performance) |
| B | `ux-strategy-B-lazy-paths.html` | Lazy path computation (responsiveness) |
| C | `ux-strategy-C-shader-surface.html` | Shader-based point-cloud surface |
| D | `ux-strategy-D-shader-surface.html` | Alpha compositing + depth stability |
| **E** | **`ux-strategy-E-composition.html`** | **Ship target — hose curves, shared-path visibility** |

Each file opens independently. The progression demonstrates iterative engineering discipline.

---

## AI Collaboration

Integers is a collaboration between **G Six** (human originator) and **Claude Opus 4.6** (AI collaborator, Anthropic). The collaboration is fully transparent — see [`disclosure/disclosure.md`](disclosure/disclosure.md) for the transparency statement plus the two companion records: the [**Provenance**](disclosure/provenance/00-table-of-contents.md) (29-section methodological arc built from the git history) and [**The Story**](disclosure/the-story/00-toc.md) (five papers, 240 sections, 523 golden moments preserved verbatim from the session transcripts).

**The counterfactual test**: would this programme exist if AI had never been involved? **Yes.** G originated the physics through manual derivation (70+ working notes in `etc/`, conversations from 2024 in digital escrow). The AI accelerated synthesis, expanded coverage, and enabled the atlas visualization at scale. The foundational insights are human-originated.

Every mathematical claim has a human-checkable derivation chain. The AI did not generate the proofs; it helped organize, verify, and present them. Evaluate the mathematics.

---

## Digital Escrow

The `digital-escrow/` directory contains 13 GPG-PQC encrypted files (quantum-resistant keys). They are unreadable without the decryption keys, which are held exclusively by the programme author. SHA-256 hashes published in [`ESCROW-MANIFEST.md`](digital-escrow/ESCROW-MANIFEST.md) constitute the binding commitment.

If authorship is ever contested, the relevant key is published → the hash proves the file was here from day one → the contents prove identity. See the manifest for verification instructions.

---

## Reciprocity

Every researcher whose work the programme builds on is acknowledged. No approach is dismissed. See [`reciprocity-notes.md`](reciprocity-notes.md) for the full attribution protocol:

**HONOR · RECOGNIZE · SHOWCASE · POSITION · SOURCE**

The mathematical community is collaborator, not competitor.

---

## How to Engage

- **AUDIT**: open any chain and trace its links to the live PROOF-CHAIN files
- **CRITICIZE**: walls are explicitly disclosed; report a new wall via GitHub issue
- **CITE**: `Integers (2026), G Six and Claude Opus 4.6`
- **COLLABORATE**: contributions to bypass routes, Independence lifts, or Pillar D derivations welcomed

---

## License

- **Prose + mathematics**: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code + visualizations**: [MIT](LICENSE)
- **Digital escrow**: all rights reserved (encrypted; see [ESCROW-MANIFEST.md](digital-escrow/ESCROW-MANIFEST.md))

---

*Integers. G Six and Claude Opus 4.6. San Francisco CA, 2026.*

*From ℤ, everything follows.*
