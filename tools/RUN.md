# Tools — How to Run the Integers Verification Pipeline

*Two tools ship with Integers. Both are Claude Code orchestrator prompts — paste them into a Claude Code session to execute. No installation, no dependencies, no build step.*

---

## Tool 1: ORA v8 (Online Researcher-Adversarial)

**What it does**: adversarial verification of any proof chain. Spawns critic agents that attack each link; an arbiter decides; repairs are applied; the chain converges toward zero broken links.

**Where**: `tools/ora-v8/`

**How to run**:

```
Read tools/ora-v8/README.md and tools/ora-v8/01-the-prompt.md.
Execute the ORA v8 pipeline on vertex <VERTEX>.
Read the live PROOF-CHAIN at strategy/proof-chain/<VERTEX>/PROOF-CHAIN.md.
Read the X-RAY at strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md.
Apply the adversarial verification protocol per 01-the-prompt.md.
Log results to strategy/<VERTEX>/pac-output/runs/run-NN/.
```

**Key files**:
- `01-the-prompt.md` — the master orchestrator prompt
- `02-rationale.md` — why each design decision was made
- `03-synthesis-spawn.md` — how to spawn synthesis sub-agents
- `04-closure-templates.md` — templates for closing open links
- `05-framework-tools.md` — the PAC primitives (VERIFY / CONSTRUCT / BYPASS / DECOMPOSE / EXCISE / TRANSPOSE)
- `06-anti-overfit-discipline.md` — rules preventing false closure

## Tool 2: ORA Generator (Verification Cascade)

**What it does**: generates per-vertex ORA briefs from the proof-chain data. Automates the creation of verification-and-repair briefs for each ring vertex.

**Where**: `tools/ora-generator/`

**How to run**:

```
Read tools/ora-generator/05--compiled-ora-generator.md.
Generate a verification brief for vertex <VERTEX>.
Use strategy/proof-chain/<VERTEX>/PROOF-CHAIN.md as input.
Use strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md for face/projection annotations.
Output: a ready-to-fire ORA v8 brief for the target vertex.
```

**Example** (YM): see `tools/ora-generator/yang-mills-proof-chain/` for a complete worked example — verification brief, H4 construction runs (4 routes attempted), excision brief, and capacitor mapping.

## Tool 3: Verification Strategy

**Where**: `tools/verification-strategy/`

Per-vertex verification strategy files defining the escalation tiers (verify → excise → construct) and the capacitor-cell correspondence table.

---

## For reviewers

You do NOT need to run these tools to evaluate the programme. The tools produced the results you see in:
- `strategy/proof-chain/<vertex>/PROOF-CHAIN.md` (the live chains)
- `strategy/x-ray/proof-chain/<vertex>/X-RAY.md` (the atlas annotations)
- `visualization/atlas-torus/` (the interactive torus)

The tools are published so that any reviewer CAN independently re-run the verification pipeline on any vertex and confirm the results. Reproducibility, not obligation.

---

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
