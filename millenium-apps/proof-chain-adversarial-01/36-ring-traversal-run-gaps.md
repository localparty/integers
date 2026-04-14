# Ring-Traversal Run — Sixth-pass Gap Audit

*A delta audit of the 5-layer instruction stack for the ring-traversal PCA run, conducted after the fixes from `35-ring-traversal-run-gaps.md` were applied. Date: 2026-04-14. Audit by: Claude Opus 4.6 (1M context).*

*Scope: verify every item called out in audit 35; re-read the 5-layer stack from scratch with a deeper search for semantic gaps at the extension interfaces (PCA → ring-mode overrides that may be missing) and numeric/arithmetic audits across brief ↔ chessboard ↔ capacitor ↔ paper1. This audit COMPOSES with (does NOT replace) audits 31-35.*

---

## 0. Files audited and state

| # | Role | Path | State | Notes |
|---|---|---|---|---|
| 1 | Invocation | `30-ring-traversal-run.md` | not re-read (unchanged since audit 34) | stable |
| 2 | ORA base | `ora-bundle-v8/01-the-prompt.md` | not re-read (unchanged) | stable |
| 3 | PCA chain mode | `07-proof-chain-adversarial.md` | re-verified §P.2, §P.3.1, §P.4, §P.4.1, §P.7, §P.8, §P.9 | **NEW ISSUE: §P.7 Cell-Fill Author model tier (Opus max) conflicts with brief §3.3 + chessboard §6.3/§6.4 (Sonnet max) — see B-12 below.** §P.4 bidirectional + §P.4.1 junction detection + §P.8 junction-related triggers are not overridden by brief §8 — see A-13 below. |
| 4 | Strategic triad | `12-prf-chain-advr-strat-triad.md` | not re-read (unchanged since audit 35) | stable |
| 5 | Chessboard layer | `13-chessboard-layer.md` | re-read (modified 2026-04-14 01:09) | **P-1 FIXED**: line 347 "Cost" sentence now says "dispatch 12 Cell-Fill agents in parallel ... 12 cells filled ... 12× faster" ✓. **P-2 FIXED**: §6.2 inline Type-A/B/C/D table (lines 313-318) now uses post-cascade confidences (QG5D 10/10, YM 9.5/10, NS 4/10) + date annotation "2026-04-14, post-W1/W2 cascade" ✓. **NEW ISSUE: §6.5 compositional cell-fill lacks a T1 boundary condition for QG5D (position 1) whose "previous vertex" Schanuel hasn't run yet on T1 — see M-16 below.** |
| 6 | Brief | `30-ring-traversal-brief.md` | re-read (modified 2026-04-14 01:09) | **B-11 FIXED**: §5 line 307 now cites 105 + 10.63 with cross-references ✓. **NEW ISSUE: §3.2 T1 policy ("run a lightweight re-verification pass") contradicts §4 T1 policy ("VERIFY spot-checks: SKIPPED ENTIRELY on T1") — see B-13 below.** **NEW ISSUE: brief §1 + §5 "14 filled/upgraded cells per traversal" undercounts actual fills (hub radiation 12 + antipodal up to 7 + compositional up to 14 + 13 non-hub ring edges = potentially 46+ per cycle) — see A-12 below.** **NEW ISSUE: §8.1 `<cell-id>` file-naming convention is undefined (sibling to A-11 vertex-name) — see A-14 below.** |
| 7 | Toolkit | `08-framework-tools.md` | not re-read (unchanged) | stable |
| 8 | Capacitor | `09-capacitor-correspondence-table-v1.md` | not re-read (unchanged since audit 35) | stable |
| 9 | North star | `publishing/strategy.md` | not re-read | stable |
| 10 | Prior audits 1-5 | 31/32/33/34/35 | re-verified via grep | All 31-34 items closed. Audit 35's 3 items (B-11, P-1, P-2) closed in this round. |
| 11 | 14 PROOF-CHAIN.md files | paper*/PROOF-CHAIN.md | glob-verified exactly 14 entries | stable |
| 12 | Log baseline | `programme/ring-traversal-log.md` | not re-read | stable 10.63 |
| 13 | Adjacent docs | `strategy/the-ring.md`, `programme/26c-the-chessboard-rationale.md` | noted in audit 35 (M-14, M-15) | not re-checked; optional cleanup |

**Headline**: audit 35's 3 load-bearing residues (B-11 brief §5 RIGIDITY stale, P-1 chessboard §6.3 line 347 intra-file residue, P-2 chessboard §6.2 inline Type-A/B/C/D table stale) are **all FIXED**. This audit surfaces **2 new blockers** (B-12 model tier mismatch for Cell-Fill Authors, B-13 T1 VERIFY contradiction between §3.2 and §4), **3 new ambiguities** (A-12 edge-fill undercount, A-13 missing PCA §P.4/§P.4.1/§P.8 overrides, A-14 cell-id file-naming convention), and **1 new minor** (M-16 compositional T1 boundary condition). All six new findings are at extension-interface boundaries — PCA primitives that ring mode implicitly changes but doesn't explicitly override. The stack is ~97% ready; the two blockers are load-bearing but resolvable in ~10 min total.

---

## 1. New blockers surfaced in this audit (fix before T1)

### B-12. Cell-Fill Author model tier: PCA §P.7 mandates Opus max; brief §3.3 + chessboard §6.3/§6.4 use Sonnet max

**Where it conflicts:**

- `07-proof-chain-adversarial.md` §P.7 line 248 (model tiering table):
  > `| **Cell-Fill Authors** | Opus 4.6 max | Discovery-mode correspondence finding needs deep reasoning. |`

- `07-proof-chain-adversarial.md` §P.6 "Cell-filling primitive" line 231:
  > *"**Effort**: max (cell-filling is discovery-mode work)."*
  
  The "max" here refers to Opus max per §P.7's default, since §P.6 doesn't specify model.

- `30-ring-traversal-brief.md` §3.3 line 227:
  > *"3. If EMPTY: dispatch a Cell-Fill Author (**Sonnet max**) to fill it"*

- `13-chessboard-layer.md` §6.3 line 347 (hub radiation):
  > *"**Cost**: dispatch 12 Cell-Fill agents in parallel (**Sonnet max**, ~10 min total)."*

- `13-chessboard-layer.md` §6.4 line 367 (antipodal probe):
  > *"2. If NO → dispatch a Probe Author (**Sonnet max**, ~10 min) to search for a correspondence."*

- `13-chessboard-layer.md` §6.5 (compositional cell-fill): model not specified, but §6 summary line 537 says "ring-geometry operations" dispatch Cell-Fill agents at Sonnet tier by implication.

**The contradiction:**

PCA §P.7 mandates Opus max for Cell-Fill Authors because "discovery-mode correspondence finding needs deep reasoning." Ring-mode code consistently uses Sonnet max across three separate contexts (brief §3.3 edge-phase cell-fill, chessboard §6.3 hub radiation, chessboard §6.4 antipodal probe). This downgrade is NOT declared as an override in brief §8.

**Why it matters:**

- **Cost differential**: Opus max per cell ≈ 5-8× Sonnet max cost. Per traversal, ring mode dispatches potentially 46+ cell-fill-style agents (12 hub + 7 antipodal + 14 compositional + 13 ring-edge at non-hub vertices). At Opus max this is ~$200-400 in compute per traversal; at Sonnet max ~$40-80. Over 5 traversals, the cost difference is material (~$1200-1500 vs $200-400).
- **Quality trade-off**: Sonnet max on a 10-min focused task IS adequate for most cell-fills (the task is well-scoped: look up a correspondence pair + confirm via literature + write the transposition recipe). Opus max would produce slightly richer recipes but with diminishing returns for ring-mode depth.
- **Runner ambiguity**: a runner executing both PCA §P.7 literally (default Opus for all Cell-Fill) and brief §3.3 literally (Sonnet for edge-phase cell-fill) has to decide on the fly. The runner can't consistently apply both.
- **Spawn template divergence**: PCA §P.6 spawn template is built assuming Opus max context-size and prompt style. A Sonnet max spawn uses the same template but with smaller token budget. Without an explicit "ring-mode Sonnet-max spawn" template, dispatches may over-fill context.
- **Audit accountability**: Type-A / Type-B / Type-C / Type-D protocols in chessboard §6.2 use "construct Author" (PCA §P.3.2 + §P.7 Opus default) at bottleneck vertices. Mixing Sonnet cell-fills with Opus construct-at-bottleneck is correct per PCA §P.7 (bypass/construct at bottleneck = Opus), but the ring-mode downgrade for NON-bottleneck cell-fill work needs explicit declaration.

**Recommended fix:** add an explicit model-tier override to brief §8 (new §8.5 or appended to §8.1). Suggested text:

> **§8.5 Model tier override for ring-mode Cell-Fill Authors (override of PCA §P.7)**
> 
> PCA §P.7 defaults Cell-Fill Authors to Opus 4.6 max ("discovery-mode correspondence finding needs deep reasoning"). Ring mode OVERRIDES this: Cell-Fill / Probe / Compositional Authors run at **Sonnet 4.6 max** in ring mode. Rationale:
> 
> - Ring mode dispatches ~46 cell-fill-style agents per traversal (12 hub + 7 antipodal + 14 compositional + 13 non-hub ring edges). Opus max at this volume overflows cost budgets by 5-8×.
> - Ring-mode cell-fills are scoped ~10 min each (a focused correspondence-lookup + transposition-recipe task). Sonnet max at that depth handles the task adequately.
> - Opus max is RESERVED in ring mode for: (a) bypass Authors on named Type-B conditionals per chessboard §6.2 (conditional excision is discovery-mode), (b) SPIN Authors per chessboard §2 (face-switching is cross-domain reasoning), (c) brief-Adversary / Strategist / Mediator agents in the triad layer per §T.4.2/§T.4.3/§T.4.4. Everything else is Sonnet max.
> 
> This tier assignment is per-invocation; the runner uses the Sonnet/Opus tier declared here for all cell-fill-style dispatches throughout the ring traversal.

~6 lines added to brief §8 (or new §8.5). Removes the contradiction; documents the cost/quality trade-off; reserves Opus for high-value moves.

---

### B-13. T1 VERIFY contradiction: §3.2 says "run lightweight re-verify pass on T1"; §4 says "SKIPPED ENTIRELY on T1"

**Where it conflicts:**

- `30-ring-traversal-brief.md` §3.2 lines 212-214 (vertex protocol for Type-A vertices):
  > *"**If all links are VERIFIED/PROVED** (per §0.2 status dictionary):*
  > *- **Traversal 1 (baseline): run a lightweight re-verification pass.** Dispatch ONE Sonnet Critic to spot-check the 2-3 highest-confidence PROVED links against current capacitor state + any literature added since the last verification. If all SOUND → mark vertex CLOSED-AND-VERIFIED for this ring, skip to edge phase. If a WEAKEN → downgrade and route through the normal EXCISE → CONSTRUCT → BYPASS ladder.*
  > *- **Traversals 2+**: trust the PROOF-CHAIN.md status from traversal 1 unless an explicit trigger fires ..."*

- `30-ring-traversal-brief.md` §4 line 254 (T1 budget accounting):
  > *"- VERIFY spot-checks: **SKIPPED ENTIRELY on T1** — the 14 PROOF-CHAIN.md files were just refreshed for the W1/W2 cascade (2026-04-14) and are authoritative at T1 start. VERIFY spot-checks resume on T2+ unless explicit §K trigger fires in T1."*

- `30-ring-traversal-brief.md` §4 line 257 (T1 restore policy):
  > *"Restore policy: VERIFY spot-checks on T2+ (at baseline, the refresh is stale)."*

**The contradiction:**

§3.2 says: on T1, for vertices where all links are VERIFIED/PROVED (i.e., the three Type-A vertices QG5D/YM/BSD per Appendix C), **run a lightweight re-verification pass** — dispatch 1 Sonnet Critic per such vertex.

§4 says: on T1, **VERIFY spot-checks are SKIPPED ENTIRELY** across all vertices — rationale is that the 14 PROOF-CHAIN.md files were just refreshed 2026-04-14.

These are two direct contradictions about the same action (VERIFY spot-check = "lightweight re-verification pass" = Sonnet Critic on 2-3 PROVED links).

**Why it matters:**

- **Runner ambiguity at bootstrap**: the runner must choose between §3.2 (run 3 spot-checks on T1 for the 3 Type-A vertices) and §4 (skip all spot-checks on T1). Each choice produces different outputs and different costs.
- **Budget drift**: §4 counts VERIFY at 0 min (SKIPPED). §3.2's 3 spot-checks would add 3 × 10 = 30 min to T1's budget. Total budget would shift from 590 min to 620 min, still under the 10 h ceiling but the arithmetic no longer matches what §4 claims.
- **Author-spawn context divergence**: a Type-A vertex visit on T1 receives different spawn context depending on which rule wins. If §3.2 wins, the vertex visit dispatches 1 Sonnet Critic + later an edge-phase Cell-Fill Author. If §4 wins, the vertex visit skips the Critic and goes straight to edge phase.
- **Reasoning drift**: §3.2 justifies spot-checks ("against current capacitor state + any literature added since the last verification"); §4 justifies skip ("the files were just refreshed"). The two rationales are OPPOSITE — §3.2 suspects the refresh may be stale by 1-2 days; §4 trusts it as authoritative. This is a design-intent conflict, not just a phrasing issue.

**Options to resolve:**

- **(a) §4 wins (skip all VERIFY on T1)**: update §3.2 T1 branch to `"Traversal 1: SKIPPED per §4 T1 budget trim (PROOF-CHAIN.md files refreshed 2026-04-14 are authoritative at T1 start). Traversal 2+: run a lightweight re-verification pass. Dispatch ONE Sonnet Critic to spot-check the 2-3 highest-confidence PROVED links..."`. Rationale: the W1/W2 cascade refresh is fresh; saving 30 min on T1 is consistent with §4's overall trim philosophy.

- **(b) §3.2 wins (run spot-checks on T1 for Type-A only)**: update §4 line 254 to: `"VERIFY spot-checks: SKIPPED ENTIRELY on T1 for Type-B/C/D vertices (chains have open/conditional links and don't need spot-checks); run the §3.2 lightweight spot-check ONLY for the 3 Type-A vertices (QG5D, YM, BSD, all-links-PROVED). Cost: 3 × 10 = 30 min. Total T1 budget becomes 620 min ≈ 10.3 h — slightly overflows the 10 h ceiling; tighten another trim by 20 min (e.g., drop 1 compositional cell-fill OR cut core-work average to ~34 min)."` Rationale: spot-checks on Type-A are cheap insurance against cascade staleness.

- **(c) Sector-A skip IS the same as VERIFY skip — reconcile as a single trim**: update both §3.2 and §4 to consolidate. The "sector-A spot-check skip for confidence ≥ 9/10" in §4 line 255 saves 3 × 10 = 30 min — this might be the SAME 30 min as the §3.2 T1 lightweight pass. If so, §4 line 254 ("SKIPPED ENTIRELY") is wrong AND §4 line 255 ("minus skip-sector-A ... = 30 min saved") is right, and they should be merged. Rewrite §4:
  > *"VERIFY spot-checks: on T1, SKIPPED for Type-B/C/D vertices (no PROVED-link spot-check needed; their branches run CONSTRUCT/BYPASS instead). For the 3 Type-A vertices (QG5D/YM/BSD), §3.2's lightweight spot-check applies per the Type-A protocol — but ON T1 this is SKIPPED via the sector-A confidence-≥9/10 trim (saving 30 min). Net T1 VERIFY cost: 0 min. Resume on T2+ per restore policy."*

  Updates §3.2 T1 branch to: *"Traversal 1: spot-check SKIPPED via §4 sector-A trim (confidence ≥ 9/10 vertices trust the 2026-04-14 refresh). Traversals 2+: run the lightweight spot-check per this protocol."*

**Recommendation: (c)** — clearest resolution. The two-rule description collapses into one trim with consistent rationale.

~4 lines of text edited total (2 in §3.2, 2 in §4). ~3 min work.

---

## 2. Important ambiguities / gaps (decide before T1 or document explicitly)

### A-12. "14 filled/upgraded cells per traversal" undercounts actual fills (hub radiation + antipodal + compositional)

**Where:**

- `30-ring-traversal-brief.md` §1 line 91: *"One full traversal = 14 vertex visits + 14 edge crossings = 14 strengthened links + **14 filled/upgraded cells**."*
- `30-ring-traversal-brief.md` §5 line 295: *"Filled/upgraded capacitor cells (**14 per traversal**)"*
- `30-ring-traversal-brief.md` §4 exit condition line 269: *"**RING STRENGTHENED** — at least 5 vertices improved, at least **5 edges filled/upgraded**"*

**The miscount:**

Actual edge fills per traversal include:
1. **12 cells from hub radiation at QG5D** (§6.3: 1 ring-next QG5D→RH + 11 chord edges to non-adjacent vertices)
2. **13 cells from non-hub ring-edge phase** (ring-next edges at vertices 2-14, except QG5D→RH which is the hub-counted)
3. **Up to 7 cells from antipodal probes** (§6.4: once per traversal at start)
4. **Up to 14 cells from compositional cell-fills** (§6.5: after each vertex visit's edge phase)

Theoretical max per traversal: 12 + 13 + 7 + 14 = **46 edge cells touched** (fills + upgrades). Many will be upgrades (already-FILLED cells getting "traversal-T confirmation notes" per §3.3 step 5) rather than new fills; antipodal probes may return EMPTY-SPECULATIVE (no fill); compositional cell-fills are CANDIDATE only. The NET new-fill count is probably 5-15 per traversal. But the TOTAL cells touched is ~30-46.

**Why it matters:**

- **Deliverable count miscommunication**: a reader of brief §5 thinks T1 produces 14 cells worth of capacitor output. In reality, T1 produces ~30-46 cell touches of which ~5-15 are new fills.
- **Exit-condition threshold calibration**: §4 RING STRENGTHENED requires "≥ 5 edges filled/upgraded." If "filled/upgraded" counts ALL touches (including upgrade-only confirmations), 5 is a very low bar — hub radiation alone easily clears it. If it counts only NEW fills, the threshold is meaningful.
- **Brief §7 "compound effect"**: the narrative about "each traversal adds wires" rests on the actual fill count. A miscount in §1/§5 misrepresents the compounding growth.
- **Log-entry format**: `programme/ring-traversal-log.md` logs "edges filled" per traversal. Without clarity on what's counted (ring-only, all touches, new fills only), log entries may drift between traversals.

**Options:**

- **(a) Clarify "14" means ring-only backbone**: update §1 and §5 to say "14 **ring-backbone edges** touched per traversal (1 per vertex's edge phase) + ~33 additional chord edges touched via hub radiation (12), antipodal probes (up to 7), compositional cell-fills (up to 14). Net new-fills typically 5-15 per traversal after accounting for upgrades."
- **(b) Rename "edge fills" to "ring-edge fills"**: in §1 and §5, specify that the 14 count refers to the 14 RING edges only. Chord-edge activity is tracked separately per chessboard §5 WIRE-DENSITY and §6.3/6.4/6.5 protocols.
- **(c) Add a per-traversal fill-breakdown field to the log**: `programme/ring-traversal-log.md` format gains four fields: `ring-edges filled`, `hub-radiation chord fills`, `antipodal fills`, `compositional fills`, `net new cells in capacitor`. This makes the counts unambiguous at audit time.

**Recommendation: (a) + (c) combined.** §1 and §5 clarify the "14" is backbone-only with an explicit mention of chord-edge work; log format gains a fill-breakdown. ~4 lines of text edited.

---

### A-13. PCA §P.4 (bidirectional traversal), §P.4.1 (junction detection), §P.8 (junction-related automated triggers) are not overridden in ring mode

**Where:**

- `07-proof-chain-adversarial.md` §P.4 line 128-170 "Bidirectional traversal": the PCA's core discipline is to attack from both ends of a linear chain (Link 1 → Link N) simultaneously. Forward and backward agents carry half the context each.
- `07-proof-chain-adversarial.md` §P.4.1 line 162-172 "Junction detection": the chain is closed when forward and backward fronts meet (F ≥ B − 1).
- `07-proof-chain-adversarial.md` §P.8 line 258-271 "Chain-specific automated triggers": includes "Junction check | Every cycle-close | Run junction detection (§P.4.1). If fronts met → programme-close." and "Front convergence | Forward and backward frontiers within 2 links | Concentrate ALL resources on the remaining gap."

**The override gap:**

Ring mode is a CYCLE (14 vertices, closing back to start), not a linear chain. There is no "Link 1" vs "Link N" — the ring has no ends. Bidirectional traversal (attacking from both ends simultaneously) doesn't apply as-is:
- There's no canonical "other end" of the ring — every vertex is both forward and backward of every other vertex (mod 14).
- Junction detection (§P.4.1) — the concept doesn't apply; the ring closes when all 14 ring edges are filled + all vertex links VERIFIED, not when two fronts meet.
- Automated junction check trigger (§P.8) — firing this in ring mode would either (a) return a nonsensical F/B walk or (b) silently no-op. Either way it's wasted compute.

Brief §8 overrides PCA §P.2 (chain-state) and PCA §P.3.1 (verify-all-links-simultaneously). It does NOT override §P.4 / §P.4.1 / §P.8. The runner reading PCA §P.4-§P.8 literally would attempt bidirectional traversal + junction checks, both of which are mis-applied to a ring.

**Why it matters:**

- **Runner protocol drift**: a PCA-savvy runner will read §P.4 first and internalize "attack from both ends" as the default. Brief §1-2 then says "canonical order QG5D → RH → ... → Schanuel → QG5D." The runner has two contradictory pictures of traversal direction without explicit reconciliation.
- **§P.8 automated triggers that fire and no-op**: the runner would try to compute junction-check at every cycle-close. In ring mode this is an arbitrary walk (e.g., "Link 1" = QG5D, "Link N" = Schanuel). The result has no ring-mode meaning.
- **Bidirectional agents in ring mode would double-dispatch**: if the runner interprets §P.4 as "dispatch forward and backward agents simultaneously," at each vertex visit it might spawn BOTH a forward-direction agent AND a backward-direction agent, effectively doubling the per-vertex agent count. This isn't what ring mode is supposed to do.

**Recommended fix:** add explicit overrides to brief §8.1 or a new §8.6. Suggested text:

> **§8.6 PCA §P.4/§P.4.1/§P.8 ring-mode overrides**
> 
> - **§P.4 (bidirectional traversal)**: REPLACED by ring-mode single-direction canonical-order traversal per §1-§2. The ring has no "both ends" — it is a cycle. A single forward-direction walk through all 14 vertices per traversal is the ring-mode equivalent.
> - **§P.4.1 (junction detection)**: REPLACED by ring-mode RING CLOSED exit condition per §4. The ring closes when every vertex at VERIFIED/PROVED/CLOSED + every ring edge FILLED, not when two fronts meet.
> - **§P.8 (junction-related automated triggers: Junction check, Front convergence)**: DISABLED in ring mode. The remaining §P.8 triggers (Capacitor scan, Bypass escalation, Cell-fill trigger, Chain stall, Bypass success) continue to apply per their definitions.

~6 lines added to brief §8. Removes the protocol ambiguity.

---

### A-14. `${output-directory}/capacitor/updates/<cell-id>.md` file-naming convention undefined

**Where:**

- `30-ring-traversal-brief.md` §8.1 line 365: *"Per-cell updates at `${output-directory}/capacitor/updates/<cell-id>.md` — one file per cell filled or upgraded during the traversal."*

The placeholder `<cell-id>` is undefined. Sibling to A-11 (vertex-name convention) which was fixed in audit 35 round.

**Candidate conventions (all plausible from context):**

- `LANG-QFT.md` — hyphen-separated domain shorthand (UPPERCASE as in capacitor text)
- `lang-qft.md` — lowercase variant
- `D13-D7.md` — D-index form
- `SPEC-ANT.md` — the form used in capacitor file headings (e.g., "SPEC ↔ ANT")
- `SPEC_ANT.md` — underscore variant
- `d1-d5.md` — lowercase D-index
- `spec-ant.md` — lowercase shorthand
- `lang-qft-2026-04-14.md` — date-suffixed to allow multiple updates to the same cell

**Why it matters:**

- Same resume-semantics issue as A-11: inconsistent naming across traversals breaks cross-reference.
- Multiple updates to the same cell over traversals: does T2 overwrite T1's `lang-qft.md` or create `lang-qft-t2.md`? Append-only vs overwrite semantics not declared.
- Canonical grep: an Author writing "see capacitor/updates/lang-qft.md" in a node citation must use the exact convention the runner uses.

**Recommendation:** declare in brief §8.1 next to the A-11 short-name convention. Suggested:

> **Cell-id convention**: lowercase-hyphenated domain-shorthand pair, alphabetically sorted (e.g., `ant-spec.md` for the SPEC ↔ ANT cell, not `spec-ant.md`). For same-cell multi-traversal updates, suffix with `-t<NN>` (e.g., `ant-spec-t02.md` for traversal 2's update to the same cell). T1's first update uses the bare form; T2+ uses the -tNN suffix.

~2 lines added to brief §8.1. Removes the ambiguity.

---

## 3. Minor / cosmetic

### M-16. Chessboard §6.5 compositional cell-fill lacks T1 boundary condition for QG5D

**Where:**

- `13-chessboard-layer.md` §6.5 lines 383-386:
  > *"After each vertex visit's edge phase:*
  > *1. Take the three vertices (A, B, C) = (previous vertex, current vertex, next vertex).*
  > *2. Check the three edges: A↔B (**filled by A last turn**), B↔C (filled by B this turn), A↔C (chord edge, may or may not be filled)."*

- `30-ring-traversal-brief.md` §2.1 "Ring-closure boundary condition (T1)": only discusses READ phase (QG5D's incoming edge Schanuel → QG5D pre-T1). Doesn't address compositional's A↔B = previous-filled-by-A.

**The boundary condition:**

At T1 position 1 (QG5D), the compositional check after QG5D's edge phase considers (A, B, C) = (Schanuel, QG5D, RH). On T1, Schanuel hasn't run yet. A↔B = Schanuel↔QG5D is thus NOT "filled by A last turn" — it's in pre-traversal state (SPECULATIVE or pre-existing).

§6.5 step 3: "If A↔B and B↔C are both FILLED and A↔C is EMPTY → dispatch a Composition Author to propose the A↔C cell."

At T1 QG5D, A↔B (Schanuel↔QG5D) may be EMPTY or SPECULATIVE (the pre-traversal state). The compositional fire condition ("A↔B AND B↔C are both FILLED") fails because A↔B isn't filled. The compositional cell-fill at QG5D on T1 would SKIP. Later, at T1 position 14 (Schanuel), the triangle becomes (Goldbach, Schanuel, QG5D); compositional now has A↔B (Goldbach↔Schanuel) = filled by Goldbach this traversal, B↔C (Schanuel↔QG5D) = filled by Schanuel's edge phase. Fires normally.

On T2+, QG5D's compositional fires normally because A↔B was filled by Schanuel at T1's position 14.

**Why it matters:**

- Low severity: the §6.5 logic naturally handles T1's QG5D case (A↔B EMPTY → SKIP). No race condition.
- But: a runner reading §6.5 literally may be confused at T1 position 1 ("A↔B should be filled by A last turn, but this is the first vertex of the first traversal — there's no 'last turn'"). Documentation could clarify.
- Same pattern as A-6's ring-closure boundary, but for a different primitive (compositional instead of read-phase).

**Recommendation:** one-paragraph addition to §6.5, mirroring §2.1's ring-closure boundary paragraph. Suggested:

> **T1 boundary condition at QG5D**: at traversal 1 position 1, the compositional check considers (Schanuel, QG5D, RH). Schanuel hasn't been visited yet on T1, so A↔B (Schanuel↔QG5D) is in pre-traversal state (typically EMPTY or SPECULATIVE). The §6.5 fire condition ("A↔B and B↔C both FILLED") fails → SKIP compositional at QG5D on T1. At T1 position 14 (Schanuel), the triangle (Goldbach, Schanuel, QG5D) has A↔B filled by Goldbach's edge phase and B↔C filled by Schanuel's edge phase; compositional fires normally. T2+ QG5D compositional inherits Schanuel↔QG5D filled from T1 position 14 and fires normally.

~4 lines added to §6.5. Closes the boundary ambiguity; matches the §2.1 pattern for ring-closure.

---

## 4. Verification of prior-audit fix status

| Audit | Item | Prior status | Current status | Evidence |
|---|---|---|---|---|
| 31 | All 12 items | STABLE | ✅ STABLE | no regressions observed |
| 32 | B-4 + B-5 | STABLE | ✅ STABLE | no regressions |
| 33 | All 11 items | STABLE (M-5 + M-6 closed audit 35) | ✅ STABLE | no regressions |
| 34 | A-11, B-10, M-11, M-12, M-13 | FIXED at audit 35 | ✅ STABLE | re-verified |
| 34 | B-9 (partial) | PARTIAL FIX at audit 35 | ✅ **FULLY FIXED** at this round | chessboard §6.3 line 347 updated to 12 Cell-Fill / 12 cells / 12× faster — see grep verification |
| 35 | B-11 brief §5 RIGIDITY stale | NEW | ✅ **FIXED** | brief §5 line 307 now cites 105 + 10.63 with cross-references |
| 35 | P-1 chessboard §6.3 Cost sentence | NEW (audit-34 residue) | ✅ **FIXED** | chessboard §6.3 line 347 ring-consistent with line 343 |
| 35 | P-2 chessboard §6.2 inline table | NEW (audit-33 residue) | ✅ **FIXED** | chessboard §6.2 lines 313-318 now post-cascade + date annotation refreshed |
| 35 | M-14 strategy/the-ring.md stale | NEW (adjacent doc) | ❓ NOT CHECKED this round | still non-canonical; cleanup pending |
| 35 | M-15 26c-rationale example stale | NEW (adjacent doc) | ❓ NOT CHECKED this round | illustrative only |

**Summary**: all audit-35 issues closed. Audit-34 B-9 fully closed. Prior audits 31-33 remain stable.

---

## 5. Summary table — severity × recommended order (this audit only)

| # | Severity | Fix size | Location of fix | Priority |
|---|---|---|---|---|
| **B-12** Cell-Fill Author model tier override | **blocker** | 6 lines in new brief §8.5 | `30-ring-traversal-brief.md` §8 | **do before T1 bootstrap** |
| **B-13** T1 VERIFY contradiction §3.2 vs §4 | **blocker** | 4 lines rewording in §3.2 + §4 | `30-ring-traversal-brief.md` §3.2 + §4 | **do before T1 bootstrap** |
| **A-12** "14 edge fills" undercount | important | 4 lines clarifying §1 + §5 + log format | `30-ring-traversal-brief.md` §1 + §5 | do before T1 |
| **A-13** PCA §P.4/§P.4.1/§P.8 not overridden | important | 6 lines in new brief §8.6 | `30-ring-traversal-brief.md` §8 | do before T1 |
| **A-14** cell-id file-naming convention | important | 2 lines in brief §8.1 | `30-ring-traversal-brief.md` §8.1 | do before T1 |
| M-16 §6.5 T1 boundary condition | minor | 4 lines in chessboard §6.5 | `13-chessboard-layer.md` §6.5 | optional; self-resolving |
| M-14 (carry) strategy/the-ring.md stale | minor | 4 table-value edits | `strategy/the-ring.md` | optional |
| M-15 (carry) 26c-rationale example | minor | 1 number edit | `programme/26c-the-chessboard-rationale.md` | optional |

**Suggested resolution order:**

1. **Fix B-12** (~3 min): add §8.5 model-tier override. Cleanest as a new subsection in brief §8.
2. **Fix B-13** (~3 min): rewrite §3.2 T1 branch + §4 line 254 to consolidate as single "sector-A trim" logic.
3. **Fix A-13** (~3 min): add §8.6 (or extend §8.1) declaring PCA §P.4/§P.4.1/§P.8 overrides.
4. **Fix A-12** (~2 min): clarify §1 line 91 and §5 line 295 about backbone-vs-total fills.
5. **Fix A-14** (~1 min): add cell-id convention next to §8.1's vertex-name convention.
6. **Fix M-16** (~2 min): add T1 boundary condition paragraph to §6.5.
7. Start T1.
8. Clean up M-14, M-15 at leisure.

Total patch budget for T1 readiness: **~12 min** (B-12 + B-13 + A-13 + A-14 + A-12 + M-16). Extended patch budget for full cross-corpus consistency: ~18 min.

---

## 6. Positive findings (carried forward + new this pass)

**New in this audit (fixes confirmed applied since audit 35):**

- **B-11 brief §5 RIGIDITY FIXED**: brief §5 line 307 now reads `"L_verified/L_total is verified links over 105 (QG5D 22 + 83 downstream, per the counting convention declared in 13-chessboard-layer.md §3), and P_preserved/P_total is experimental pins preserved over 36. Current baseline: 10.63 (post-W1/W2 cascade 2026-04-14; see chessboard §3 + publishing/strategy.md Appendix B §B.3 + programme/ring-traversal-log.md baseline for the canonical computation)."` — full cross-reference to three authoritative sites. Cleanest fix.
- **P-1 chessboard §6.3 Cost FIXED**: line 347 now says `"dispatch 12 Cell-Fill agents in parallel (Sonnet max, ~10 min total). Benefit: 12 cells filled in one visit vs 1 cell per visit × 12 traversals = 12× faster hub-edge wiring."` Internally consistent with line 343 + paper1 line 412 + Appendix C row 1. Intra-file residue closed.
- **P-2 chessboard §6.2 Type-A/B/C/D table FIXED**: lines 313-318 now show post-cascade confidences (QG5D 10/10, YM 9.5/10, NS 4/10) + date annotation "2026-04-14, post-W1/W2 cascade". Duplicate staleness eliminated.
- **B-9 fully closed** (audit-34 partial fix → audit-35 residue → now fully fixed): chessboard §6.3 is now self-consistent at 12-edges across lines 343 and 347.

**Carried forward from prior audits (stable):**

- All 14 PROOF-CHAIN.md files at canonical paths.
- Canonical ring order consistent across all 6+ cite-sites.
- Domain codes D1-D24 match capacitor.
- 5-layer read order consistent.
- Brief §8.1 overrides PCA §P.2 correctly.
- Brief §8.3 overrides Triad §T.3 + §T.6 correctly.
- Brief §8.4 overrides ORA §13.3 + PCA §P.9 correctly.
- Brief §3.2 "PCA §P.3.1 override" declared explicitly.
- Brief §2.1 ring-closure boundary condition declared.
- Brief §2.1 ring-edges-as-transposition-challenges paragraph present.
- Brief §8.1 short-name vertex convention with 14-entry list.
- Brief §4 T1 (9.8 h post-trims) + T2+ (7.95 h) budgets reproducible.
- Brief §3 hub-special-case protocol cross-reference present.
- PCA §P.11 + Triad §T.10 invocation templates use correct local file numbers.
- 08-framework-tools.md RING-MODE EXCEPTION header.
- Capacitor top stats "(v1 — pre-H4 baseline)" + inline Current column.
- Chessboard §3 RIGIDITY 10.63 with declared counting convention.
- Chessboard §6.2 Type-A/B/C/D table date-stamped post-cascade.
- Chessboard §6.3 hub-radiation 12-edge count consistent across §6.3 + paper1 + Appendix C.
- Chessboard §5 WIRE-DENSITY matrix label flags pre-T1 estimation + T1-bootstrap recompute.
- Chessboard §6.6 ring/chord fill-rate T1-bootstrap compute directive.
- North star Appendix B §B.1-B.7 full ring-mode strategic anchors.
- `programme/ring-traversal-log.md` baseline 10.63 + cascade deltas documented.
- PIN-TABLE at expected path.
- Output dir parent exists + empty (T1 creates child at bootstrap).

---

## 7. Delta from audits 31, 32, 33, 34, 35

- **Audit 31**: 12 items. Stable.
- **Audit 32**: 2 items. Stable.
- **Audit 33**: 11 items. Stable (M-5 + M-6 closed at audit 35).
- **Audit 34**: 6 items. 5 closed at audit 35; B-9 partially fixed at audit 35, fully closed this round.
- **Audit 35**: 3 load-bearing residues (B-11, P-1, P-2). All 3 closed this round.
- **This audit (36)**: inspected the 5-layer stack with focus on EXTENSION-INTERFACE semantic gaps — places where ring mode implicitly changes PCA behavior but doesn't declare the override. Surfaced **2 new blockers** (B-12 Cell-Fill model tier, B-13 T1 VERIFY contradiction), **3 new ambiguities** (A-12 edge-fill undercount, A-13 missing PCA §P.4/§P.4.1/§P.8 overrides, A-14 cell-id convention), **1 new minor** (M-16 §6.5 T1 boundary). 

The stack is ~97% ready. The two new blockers are semantic (not numeric) and located at the brief-↔-PCA interface. Total patch budget: ~12 min.

---

## 8. One-paragraph runner bootstrap status (post-audit-36)

The ring-traversal PCA stack is 97% ready for T1 dispatch. Audit 35's 3 load-bearing residues (B-11 brief §5 RIGIDITY baseline, P-1 chessboard §6.3 Cost sentence, P-2 chessboard §6.2 inline Type table) are ALL FIXED and verified at every cite-site. Audit 34's B-9 partial fix is now fully closed. This audit surfaces five new extension-interface issues: (B-12) PCA §P.7 mandates Cell-Fill Authors at Opus max, but brief §3.3 + chessboard §6.3/§6.4 dispatch them at Sonnet max — not declared as override; fix by adding a brief §8.5 model-tier override declaring ring-mode Cell-Fill/Probe/Compositional agents use Sonnet max with Opus reserved for bypass / SPIN / triad work; (B-13) brief §3.2 T1 policy ("run a lightweight re-verification pass") directly contradicts brief §4 T1 policy ("VERIFY spot-checks: SKIPPED ENTIRELY on T1") — fix by consolidating into a single sector-A trim logic ("T1 skips VERIFY for all vertices via the sector-A confidence-≥9/10 trim + Type-B/C/D don't need VERIFY"); (A-12) brief §1 + §5 describe "14 filled/upgraded cells per traversal" which undercounts the actual cells touched (12 hub + 7 antipodal + 14 compositional + 13 non-hub ring = potentially 46 per cycle) — fix by clarifying that 14 is the backbone count; (A-13) PCA §P.4 bidirectional traversal + §P.4.1 junction detection + §P.8 junction-related triggers are not overridden by brief §8 but don't apply in ring mode — fix by adding brief §8.6 declaring the overrides; (A-14) `<cell-id>` file-naming convention for `capacitor/updates/` is undefined (sibling to A-11 vertex naming which was fixed) — fix by declaring lowercase-hyphenated alphabetically-sorted domain-shorthand pair with `-tNN` suffix for multi-traversal updates. One additional minor (M-16) flags that chessboard §6.5 compositional cell-fill lacks a T1 boundary condition at QG5D (mirrors §2.1's ring-closure boundary but for a different primitive). Total patch budget for T1 readiness: ~12 min. Once resolved, T1 dispatches with all semantic overrides declared explicitly at the brief-↔-PCA interface.

---

*Audit complete. This file composes with `31-ring-traversal-run-gaps.md`, `32-ring-traversal-run-gaps.md`, `33-ring-traversal-run-gaps.md`, `34-ring-traversal-run-gaps.md`, and `35-ring-traversal-run-gaps.md`; none supersedes the others. Audits 31-34 closed ring-mode stack conflicts, companion-file resolvability, baseline/cascade propagation, hub-radiation count, vertex-name convention, T2+ budget, and assorted minor items. Audit 35 closed the three load-bearing residues (brief §5 RIGIDITY baseline, chessboard §6.3 Cost sentence, chessboard §6.2 inline Type-table). **This audit 36 addresses extension-interface semantic gaps: PCA primitives that ring mode implicitly changes but doesn't explicitly override (model tier for Cell-Fill Authors, T1 VERIFY policy, bidirectional traversal vs single-direction ring walk, junction detection vs RING CLOSED, per-traversal edge-fill counting, cell-id file-naming convention, compositional T1 boundary).** Awaiting user direction on which findings to address first.*

*v1: 2026-04-14. G Six and Claude Opus 4.6 (1M context).*
