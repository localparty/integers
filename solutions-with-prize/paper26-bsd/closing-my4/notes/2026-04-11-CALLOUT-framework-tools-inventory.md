# CALLOUT — framework tools inventory available

**Source**: support runner (the Claude instance answering questions in `paper26-bsd/closing-my4-questions.md`).

**Date**: 2026-04-11.

**One-liner**: read `/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v3/05-framework-tools.md` — it inventories every compiled master file in the framework (Six Patterns method, theorem catalogues, predictive grammar, transposition mechanics, master dictionaries, anchor document, master prediction table, **and the completed RH + Yang-Mills proof chains**) that should be in Author / Critic / Synthesis spawn context but currently isn't.

**Why this matters for closing MY4**:

The BSD chain over `K = ℚ(i)` is a **transposition of the RH proof chain**. Specifically, `paper13-rh/preprint/sections-06-10.md` (the CCM operators / ITPFI / Bögli / Hurwitz layers) is the **template** the BSD chain is porting. Author M.1.1's "from scratch" attempt on the dark-state bound (per Q-1 in the questions file) was failing because that file was not in the spawn context — the answer is structurally already written, in the RH preprint, in a different alphabet (`p ↦ N(𝔭)`, `Λ ↦ Λ_K`, `ζ ↦ ζ_K`).

**Highest-leverage immediate patch** (without restarting the run):

For the next Author M.1.1.a or M.1.1.b spawn, inject these files into the spawn context:

1. `paper13-rh/preprint/00-proof-skeleton.md` (~4K tokens) — the 6-layer chain template
2. `paper13-rh/preprint/sections-06-10.md` (~17K tokens) — **THE most important file**, the CCM/ITPFI/Bögli/Hurwitz chain BSD is porting
3. `paper13-rh/research/27-arithmetic-theorem-attack.md` (~4K tokens) — methodology for porting RH-style chains to other arithmetic contexts
4. `paper08-yang-mills/preprint/PROOF-CHAIN.md` (~3K tokens) — for rigor + closure register reference
5. `paper08-yang-mills/research/21-the-rigorous-proof.md` — for the THEOREM/LEMMA/KEY LEMMA/GAP rigor labels (the same labels `04-closing-my4.md` uses)
6. `paper12/research/214-the-method-six-patterns.md` (~6K tokens) — the Six Patterns method file (the inner-loop discipline the Author is supposedly executing)
7. `paper12/27-anchor-document.md` (~7K tokens) — operational anchor + SP1-SP5 + voice canon seed
8. `paper12/research/14-transposition-CCM-and-reasoning-patterns.md` (~12K tokens) — the transposition mechanics, since BSD is a transposition

**Total**: ~62K tokens of framework canon. Trim other Author context (kill-list rows, trajectories, heuristics) to fit. The framework canon is dominant for early cycles.

**Action requested**: at next REFRAME or Plan primitive call, the runner should read `05-framework-tools.md` end-to-end and update its working understanding of what tools are available. This is structurally a §F kill-list pivot (Sig 6) — the "from-scratch" attempt's failure pattern is "Author wasn't given the framework's existing toolkit" and the search-query pivot lands on this inventory file.

**Voice canon connection**: Sig 6 ("the kill list IS the search query") + Sig 11 ("be hella explicit"). The framework's compiled tools are EXPLICIT artifacts; not having them in spawn context is the operational form of "running without the framework's voice."

**This is a CALLOUT, not a directive**: the primary runner decides what to do with this. The support runner's recommendation is to inject the 8 files above into the next Author spawn and re-run the M.1.1.a / M.1.1.b nodes with the framework tools present. Expected outcome: the dark-state bound becomes a 1-cycle port from `paper13-rh/preprint/sections-06-10.md`'s CCM/ITPFI structure rather than a from-scratch invention.

**Logged to** §I — Notes (CALLOUT tag) per v3 §3 spec.
