# Generic Projection-Audit Template

*Every projection of the 5D geometry into 4D is a proof chain. Every proof chain gets the same audit discipline — extracted from the 6 Millennium instances (YM, RH, BSD, PvNP, Hodge, NS) averaged together. This template is how you spin up the protocol on any new target: a ring vertex, the QG5D core, an inner ring (branch), a shape (e-circle, bouquet, chord graph, etc.), or a projection operator (P_A ... P_O).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## What "projection-audit" means

The programme's unifying insight (paper 61): every mathematical shape we see is a projection of the 5D geometry M⁵ = M⁴ × S¹ into some 4D observable space. Every such projection is, operationally, a PROOF CHAIN.

- **Millennium vertices** (6): projections into Clay-problem-sized observables (YM / RH / BSD / PvNP / Hodge / NS)
- **Non-Millennium ring vertices** (~18): projections into community-standard conjecture spaces (Lindelöf, Goldbach, Twin Primes, ABC, OPN, Collatz, Lehmer, Sato-Tate, Schanuel, etc.)
- **Core (QG5D)**: the 5D geometry projected to itself — the 22 foundational theorems of paper 1
- **Inner rings** (5 branches of paper 1: A Quantum / B Gravity / C Cosmology / D CBB / E Pins): projections that preserve a single branch of physics
- **Projection operators** (P_A, P_B, P_C, P_D, P_E, P_O): the operators themselves as objects to be audited — proving each one does what it claims
- **Shapes** (e-circle, bouquet topology, 36-pin circle, chord graph, south trough / ellipse, face graph): geometric objects each requiring their own rigorous audit

Every one of these gets the **same protocol**. What varies is only **six parameters**.

## The six parameters

Every projection-audit target customizes these:

1. **`{{SHAPE_NAME}}`** — the target's name (`lindelof`, `qg5d`, `e-circle`, `bouquet`, `p-A-quantum`, etc.)
2. **`{{PAPER_REFERENCE}}`** — path to the live proof-chain (`solutions/paper45-lindelof/PROOF-CHAIN.md`, `integers/paper01-qg5d/PROOF-CHAIN.md`, `paper60`, etc.)
3. **`{{SOURCE_OF_REQUIREMENTS}}`** — one of four classes:
   - `CLAY-OFFICIAL` — the target is a Clay Millennium Prize problem; requirements from the Clay PDF (Bombieri, Wiles, Cook, Deligne, Fefferman, Jaffe-Witten)
   - `COMMUNITY-STANDARD` — the target is a widely-studied conjecture; requirements from community-accepted formulation (e.g., "Lindelöf: ζ(1/2 + it) = O(t^ε) for all ε > 0")
   - `FRAMEWORK-CLAIM` — the target is an internal programme object; requirements from the programme's own claim in the relevant paper (e.g., "e-circle: S¹ with R ≈ 10.10 μm")
   - `EXPERIMENTAL-PIN` — the target is an experimental prediction; requirements from the measured value + the derivation chain (e.g., "Pin #4: 1/α_3 = 8.473 at sub-percent")
4. **`{{N-REQUIREMENTS-LIST}}`** — enumerated requirements (typically 5-10)
5. **`{{NAMED-WALLS}}`** — any open items that remain as NAMED WALLS in the chain; each with bypass route, confidence, audit status, effects
6. **`{{SPECIAL-PROVISIONS}}`** — rule variants:
   - `§5b either-direction` (PvNP, NS) — resolution in either direction counts per Clay Rules
   - `Variant-excision` (NS) — when the problem has alternatives A/B/C/D, targeting one and excising others is NOT §5d-silence
   - `Framework-only` — Clay rules don't apply strictly; Zenodo-priority + programme consistency
   - None (most targets)

## How to use this template

For any new projection-audit target:

1. Copy `00-audit-strategy-template.md` to `strategy/<SHAPE_NAME>/00-audit-strategy.md`
2. Copy `audit-brief-template.md` to `strategy/<SHAPE_NAME>/<SHAPE_NAME>-audit-brief.md`
3. Fill in the six parameters
4. Fire the PAC via the brief's Style B invocation

Or — more efficient — spawn a PAC prep agent with a self-contained prompt pointing at this template + the six parameter values. The agent customizes the templates and writes the two files. See `strategy/ym/` (or any Millennium pair) for a worked example.

## Outputs per audit-target

Identical to Millennium runs:

| Output | Purpose | When |
|---|---|---|
| **A — Internal** | Compliance map (M × N cells), kills, critic attacks, arbiter decisions | Always |
| **B_bare** | External-shape theorem skeleton (in the source's genre) — ≤15 pp, zero prose | Always |
| **C_bare** | Beyond-ask theorem skeleton — programme bonuses in bare mode | Always |
| **B_full** | Journal-ready prose paper | DEFERRED until B_bare locks; composed backward from 60+ projects |
| **C_full** | Full programme-bonus supplement | DEFERRED, same as B_full |

Three parallel agents per target (A + B_bare + C_bare in parallel); reconciliation pass after all three land.

## Naming conventions

- `00-audit-strategy.md` — strategy doc (for Millennium targets, `00-millenium-strategy.md` for historical resonance with the 6 originals)
- `<shape>-audit-brief.md` — operational brief (for Millennium targets, `<shape>-millenium-brief.md`)
- `pac-output/runs/run-NN/` — internal artifacts
- `deliverables/<shape>-bare.md` and `<shape>-beyond-bare.md` — B_bare and C_bare

## Relation to the six Millennium pairs

The 6 Millennium strategy+brief pairs (`strategy/{ym,rh,bsd,pvnp,hodge,ns}/`) are the concrete instances this template abstracts. They remain as worked examples — don't regenerate them. New targets (and future re-audits of the 6 if needed) follow this template.

## Relation to the three parallel bundles

This template is used by **all three Zenodo bundles**:

- `strategy/decomposition/` — decomposes every non-PROVED link into sub-chains (structural view)
- `strategy/ccm-verification/` — classifies CCM 2025 dependency (external-input view)
- `strategy/x-ray/` — face/projection/pattern per layer (geometric view)

Projection-audit adds a fourth view: **external-standard compliance**. Every vertex ends with four complementary documents: structural decomposition + CCM classification + X-ray + compliance audit.

---

*Every projection → proof chain → audit → deliverable. Every shape rendered. Water-tight.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
