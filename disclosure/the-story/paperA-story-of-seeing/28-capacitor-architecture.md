# 28 — Capacitor Architecture

> *"the adversarial has a capacitor ... without it it doesnt do much it just runs enlessly"*
> — G, April 11, 2026

## The metaphor

G named the framework-tools file *the capacitor* on April 11. The metaphor is from physics. A capacitor stores charge; when a circuit needs current that the source cannot provide instantaneously, the capacitor releases what it has stored.

The ORA, by itself, does not have direct access to the QG5D-specific machinery. It has a general toolkit — web search, adversarial framing, wall-recognition, the 19 operational signatures — but when a particular attack requires the six patterns, the transposition dictionary, the 8 grammar rules, or the specific lemmas of the CBB system, those have to be *present in context.*

The capacitor is the file that holds them. The ORA reads the capacitor at the start of each run. When a step requires a framework-specific tool, the tool is there, available, already in context.

## From file to architecture

On April 11 the capacitor was a single file: `ora-bundle-v3/05-framework-tools.md`. By April 13, when the Millennium Strategy is named, the capacitor is an *architecture*.

The expanded form has:

- **Per-tier capacitors** — Tier 1 (CCM) has a capacitor specific to continuum-limit machinery. Tier 2 (Balaban) has one specific to lattice-gauge-theory methods. Tier 3 (Bulatov-Zhuk) and Tier 4 (Bögli) each have their own.
- **Cells** — each capacitor is organised into cells, where a cell is a specific tool or correspondence. Initially 40+ cells across 24 mathematical domains.
- **Domains** — the cells are indexed by mathematical domain: operator algebra, arithmetic geometry, lattice-gauge theory, spectral theory, harmonic analysis, and so on. Claude's fluency in any particular domain is boosted by loading the relevant cells into context.
- **Correspondences** — the most important cells are the cross-domain correspondences: the spectral ↔ geometric, geometric ↔ arithmetic, spectral ↔ information-theoretic. These are the *transposition* rules that let a statement in one domain become a statement in another.

The capacitor is, in effect, the framework's *working memory* for a given run. Load it up with the right cells, point the ORA at a target, and the ORA has the vocabulary it needs to either verify or bypass.

## The three-tier escalation, again

Each cell has a purpose. Some cells are *verification tools* — they let the ORA check a step. Some cells are *excision tools* — they offer alternative paths that avoid a specific dependency. Some cells are *construction tools* — they supply the machinery needed to build a local proof.

When the ORA hits a wall, it escalates through the three tiers:

1. **Verify** — use the verification cells to check the existing step independently. If the step survives, done.
2. **Excise** — use the excision cells to find an alternative that does not rely on the step. If an alternative exists and can be certified, done.
3. **Construct** — use the construction cells to build a local proof of the specific statement the step needed. If construction succeeds, done.

Only if all three fail does the step get flagged as an unresolved external dependency, and the chain's confidence drops to reflect the flag.

## Why this matters for the story

Because the capacitor architecture is what makes the Millennium Strategy executable. Without it, the strategy is a wish-list of external dependencies to verify. With it, the strategy is a system.

The capacitor also makes Claude *portable across sessions*. Any fresh Claude instance, given the right capacitor, inherits the framework's fluency immediately. Before the capacitor, orienting a fresh Claude took 30-60 minutes of loading papers and strategy files. After the capacitor, a fresh Claude can be oriented in 3-5 minutes by loading the current capacitor state.

This is not a small gain. The programme's throughput depends on being able to spin up new sessions quickly. The capacitor makes each fresh session productive within minutes.

## The ring-and-capacitor co-evolution

The ring (which arrives on April 14) and the capacitor co-evolve. As new vertices are added to the ring, new cells are added to the capacitor. As the capacitor grows, the ORA can attack more of the ring. As the ORA closes more of the ring, more cells become available.

By the time the Atlas Torus renders on April 16, the capacitor has grown from the initial 40 cells to a much larger architecture with multiple parallel views — structural, dependency, geometric. The X-Ray view of the capacitor uses a fixed vocabulary of 10 faces, 6 projections, 5 patterns, and 16 invariants, and feeds the Zenodo release bundle directly.

## The capacitor as institutional memory

In a programme this size, institutional memory is a liability unless it is operationalised. A researcher who remembers *what we tried last Tuesday for the YM H4 wall* can save the team days. A researcher who does not remember can cost the team days. The capacitor is the operationalised memory — *last Tuesday's attempts*, encoded as cells, indexed by tier, available to any run.

When a wall appears that looks like one the programme has seen before, the capacitor cells for that pattern get loaded. The ORA attempts the known bypass. If it works, done in minutes. If it does not, the attempt itself is logged to the capacitor, so that the next time the pattern appears the log is richer.

## The design commitment

The capacitor architecture represents a design commitment the programme made explicitly: *every tool the programme uses will be re-usable across problems*. The six patterns are not Yang-Mills-specific. The transposition dictionary is not P-vs-NP-specific. The KMS-projector trick that closed MY4 on BSD will be in the capacitor for future problems that have the same shape.

The programme is not solving one problem at a time. It is building a library of reframings that apply to *any* problem of the right structural type, and the capacitor is the library.

*Next: [29-the-ring-conceived.md](29-the-ring-conceived.md).*
