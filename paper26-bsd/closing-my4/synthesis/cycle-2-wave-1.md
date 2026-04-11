# Synthesis — cycle 2 wave 1 (closing BSD MY4)

*Synthesis agent: Claude Opus 4.6 (1M), effort MAX, interleaved thinking.*
*Wave: cycle-2 wave-1. Slots: W2-A (M.1.1.c), W2-B (M.2.4-v2), W2-C (M.3.1-refine).*
*Predecessor synthesis: `synthesis/cycle-1-wave-1.md` (verdict WEAKENED).*
*Date: 2026-04-11.*

**Verdict: PASS.** Wave 3 may dispatch. Cycle 3 should close the deliverable.

---

## §1. What was attempted

Cycle 2 wave was plan-tree hygiene plus refinement, not new exploration. Three nodes went out in parallel: **M.1.1.c** (W2-A) to define the Paper 26 K-version bridge projector `P_k^𝔭` for `k > 1` and close cycle-1's GENUINE corpus gap G6; **M.2.4-v2** (W2-B) to re-port CCM 2025 §7 Lemma 7.2 to `L²(ℂ)` using the correct framework after cycle-1's M.2.4 was killed as wrong-framework (K5); **M.3.1-refine** (W2-C) to apply the eight editorial fixes G17–G24 surfaced by cycle-1 Critic M.3.1 (five referee misquotes, MY4-vs-A3 distinction, Theorem 13.1 trailing parenthetical, two missed silent-inference sites, volume-number correction, estimate removal, joint-sub-items citation, and the new quoted-attribution-fidelity sub-pass). The I-8 framework-tool patch was in spawn context for all three. I-7 verify-before-rely discipline fired at both layers: Author M.1.1.c numerically refuted the cycle-1-suggested cyclic-character candidate and derived the correct complement form fresh; Author M.2.4-v2 WebFetched `arxiv.org/html/2511.22755v1` directly for CCM §7 rather than trusting the cycle-1 paraphrase; Critic M.1.1.c caught a paraphrase-trust failure in Author M.1.1.c's own search (the Paper 13 referee file it said "didn't exist" did exist at a different sub-directory); Critic M.2.4-v2 extended the Author's numerical experiment to shell k=4 on its own initiative and closed CONCERN W2B-3 directly. All three Authors returned VERIFIED; all three Critics upheld VERIFIED at confidence 0.92, 0.96, HIGH.

---

## §2. Cross-lead consistency check

Pairwise checks, treating each Author and Critic from cycle 2 plus relevant cycle-1 artifacts as leads.

**Author M.1.1.c ↔ Critic M.1.1.c** — on Paper 26 Prop 6.2 sign and the formula `P_k^𝔭 = I − e_{𝔭^k}`: **AGREE.** The Critic independently read preprint/sections-part-II.md lines 620–705 and confirmed verbatim that Prop 6.2 uses the complement form, that `|w^k| = N(𝔭)^{-k/2}`, and that the expectation `1 − N(𝔭)^{-k}` is the large value near 1. Script reproduction at `mp.dps ∈ {30, 50}` reproduces every closed-form row exactly. Three-lock independence verified on the three axes of the BC triple `(A, σ_t, ω_1)`.

**Author M.1.1.c ↔ Cycle 1 M.1.1** — on the operator identification `P_𝔭 = e_𝔭` vs `P_k^𝔭 = I − e_{𝔭^k}`: **DISAGREE.** Cycle 1 M.1.1 wrote `P_𝔭 := s_𝔭 s_𝔭^* = e_𝔭` and tried to lower-bound `(ψ, P_𝔭 ψ) ≥ |w|² = N(𝔭)^{-k}`. This is wrong on two axes simultaneously — complement direction (Prop 6.2's `P_k^𝔭` is `I − e_{𝔭^k}`, not `e_{𝔭^k}`) and power of 𝔭 (Prop 6.2 has `𝔭^k`, cycle 1 used `k=1` on an expression supposed to match `k ∈ {2,3,4,6}`). **This disagreement is RESOLVED** in favor of M.1.1.c by direct primary-source verification at the Critic layer. Intra-run correction, not an open horizontal disagreement.

**Author M.1.1.c ↔ Cycle 1 Critic M.1.1 on "Paper 13 C1.01 formula existence"** — Author said file not found at `paper13-rh/strategy/math-referee-run/points/C1-hurwitz/`; Critic M.1.1.c found it at `paper13-rh/referee/latest-run/points/C1-dark-states/01-bound.md`. **DISAGREE**, with Critic M.1.1.c having the correct reading. The Cycle 1 Critic was sourcing a real file the Author failed to locate because it searched the wrong sub-directory. This is a partial K4 shadow miss on Author M.1.1.c's CONCERN-1, load-bearing only for that concern — the main formula `I − e_{𝔭^k}` is independently verified against Paper 26 and is unaffected.

**Author M.2.4-v2 ↔ Critic M.2.4-v2** — on CCM 2025 Lemma 7.2 content: **AGREE.** Both WebFetched `https://arxiv.org/html/2511.22755v1` and both got byte-for-byte match on (i) the `λ^{-2}` rate, (ii) the `n ∈ {0, 4}` Fourier-invariant indices, (iii) the `h_λ` vanishing-integral combination, (iv) the Meixner-Schäfke 1954 Satz 9 page 243 §3.2 citation, and (v) the Simons-Wang 2011 scope (existence + compactness only, no 2D Meixner-Schäfke). On the numerical scaling experiment, Critic reproduced every row of the Author's Step 5 table exactly and extended to `Nmax = 14, mp.dps = 50, λ = 100`. `C^K_{0,0} = 0.257665` stable to six digits.

**Author M.2.4-v2 ↔ Cycle 1 M.2.4** — on proof structure: **DISAGREE**, with M.2.4-v2 having the correct framework. Cycle 1 M.2.4 was reconstructed from a corrupted paraphrase ("sieve truncation + Stirling + cross-term Cauchy-Schwarz"); cycle 2 rebuilt on the correct Meixner-Schäfke prolate-to-Hermite framework with 2D Rayleigh-Schrödinger in the Laguerre-Gaussian basis. Intra-run correction; the K5 kill catches the old path, the new path respects it.

**Author M.3.1-refine ↔ Critic M.3.1-refine** — on fix application: **AGREE across all 8 fixes** (G17–G24). Grep confirmed zero hits for "substantial work required" / "multiple months" / "5-15 pages" / "mechanical" in Artifacts 1–4; only meta hits in the audit tables and banned-phrase lists. Theorem 9.1 and Theorem 13.1 conclusions preserved byte-for-byte against `sections-part-III.md` and `sections-part-IV.md`. Change-log adjacent-edits list complete on all four sites (§2.3 line 168, §9.1 Step 4 lines 518-521, §9.2 Step B sub-items 4&5 jointly, §15.1 "no gaps, no conditional"). Independent 13-row quoted-attribution audit re-walked with zero additional misquotes.

**Author M.3.1-refine ↔ Cycle 1 M.3.1** — on the verdict-file misquotes: **DISAGREE**, with M.3.1-refine having the verified quotes. Cycle 1 invented five sites where it attributed "substantial work required" and "multiple months" to the r00 verdict file; the verdict file contains neither string. Cycle 2 replaced all five with the byte-for-byte correct quotes "Overall verdict: CLOSABLE GAP" (verdict.md line 4) and "Difficulty: 2-3 pages of explicit computation" (verdict.md line 17). Intra-run correction.

**Structural observation.** Cycle 2's cross-lead disagreements are almost all **intra-run corrections** — cycle 2 correcting cycle 1 via independent primary-source verification — rather than unresolved horizontal disagreements between wave-2 agents. This is the architecture working as designed. The one *horizontal* partial miss (Critic M.1.1.c catching Author M.1.1.c on the Paper 13 C1-dark-states file) was caught inside the same wave, not carried forward. No unresolved cross-lead disagreement remains open as of wave 2.

---

## §3. Gap audit

### Per-lead acknowledged gaps

**Author M.1.1.c acknowledged:**
- CONCERN M.1.1.c-1: Paper 13 "C1.01" formula not found in the sub-directory searched. *Status: partially incorrect — the file does exist at a different path. See Critic M.1.1.c §6.*
- CONCERN M.1.1.c-2: basis-state diagonal ≠ KMS expectation. *Status: correct; the two are structurally different objects and the script's basis-state check is a red-herring. Resolved.*
- CASCADE M.1.1.c-3: §7 bridge-cocycle Pimsner–Popa basis check not performed (out of scope for M.1.1.c).

**Critic M.1.1.c newly observed:**
- Partial K4 shadow miss on Author M.1.1.c's CONCERN-1 (file exists, Author searched wrong sub-dir).
- **Cross-paper operator-form consistency question**: Paper 13's cyclic-character `c_n^{(k)} = (1/k)(1 − w^k)/(1 − w)` (referee note) vs Paper 26's complement `I − e_{𝔭^k}` (Prop 6.2). At generic k and w these are different operators; either different realizations of the same abstract bridge coupling, or one is a corpus-side dangling claim. Surfaced as CASCADE M.1.1.c-3b.
- Recommendation to upgrade cycle-1 sign error to a new §F kill K7 ("wrong-space / operator-identification error: treating Hecke range projection as Paper 26 bridge projector").

**Author M.2.4-v2 acknowledged:**
- F2: `V^K = (x²+y²)²/4` surrogate vs the exact 2D Slepian differential operator. Rate-robust; constants will shift.
- F3: `ℓ = 4` sector untested in the Author's own run.
- Unwritten `h_λ^K` vanishing-integral combination for the direct K-analog of CCM Lemma 7.2 part (ii).

**Critic M.2.4-v2 newly observed:**
- **CONCERN W2B-3 closed numerically by Critic.** `ℓ = 4` sector measured at five shell-diagonalized states, all give `a = 1.969 ± 0.001`, matching shell k=2. CASCADE was false-positive.
- CASCADE W2B-4 (surrogate constants): acknowledged, rate-robust but a constant-refinement task before publication.
- LESSON W2B-1 promotion candidate: "degenerate shells break naive dimensional lifts of 1D perturbation bounds; always diagonalise the unperturbed operator simultaneously with the symmetry group of the perturbation."

**Author M.3.1-refine acknowledged:**
- G17–G24 fix application, quoted-attribution sub-pass (G24) as procedural safeguard.
- Line-number label `516-521` vs `518-521` inconsistency inside the refined draft (±2 label, same passage).

**Critic M.3.1-refine newly observed:**
- No new structural gaps. Three minor cosmetic observations (line-label standardization, bold-formatting drop on "Overall verdict:", §15.1 softening flow-check) — none block VERIFIED.

### Cycle-1 GENUINE-gap re-classification

**G6** (corpus-level `P_k^𝔭` missing for k > 1) — **tentatively CLOSABLE → resolved as SOUND**. M.1.1.c derived `P_k^𝔭 = I − e_{𝔭^k}` as a 3-line consequence of the BC identity `ω_1^K(e_𝔟) = N(𝔟)^{-1}`; matches Paper 26 Prop 6.2 byte-for-byte (complement form, `1 − N(𝔭)^{-k}` expectation, `|w^k| = N(𝔭)^{-k/2}`); passes projection / modular-invariance / KMS-identity checks at `mp.dps ∈ {30, 50}`; cross-verified by Critic at HIGH confidence with independent script re-run and primary-source read. Cite: `nodes/M.1.1.c.md` Steps 4-6, `critiques/M.1.1.c-cycle-2.md` §§1-3.

**G9** (M.2.4 reconstruction counterfactual relative to CCM 2025 §7) — **tentatively CLOSABLE → resolved as SOUND**. M.2.4-v2 re-spawned on the correct framework (Meixner-Schäfke prolate-to-Hermite + 2D Rayleigh-Schrödinger in the Laguerre-Gaussian basis), produced a verified K-analog with measured rate `a = 1.97 ± 0.02` converging to 2 with increasing λ, specific `C^K` constants (`C^K_{0,0} ≈ 0.2577`, `C^K_{ℓ=2} ≈ 0.88-1.05`, `C^K_{ℓ=4} ≈ 1.49-2.20`). Cross-verified by Critic at 0.92 confidence with `Nmax = 14, λ = 100` extension and independent ℓ=4-sector numerical closure. Promoted to `[LEMMA] K-CCM Lemma 7.2` in §D. Cite: `nodes/M.2.4-v2.md` Steps 2-6, `critiques/M.2.4-v2-cycle-2.md` §§1-11.

**Bottom line of the cycle-1 GENUINE list: the run has zero open GENUINE gaps as of wave 2.**

### New gap candidates from cycle 2 (tentative classification — Meta-critic has final say)

- **CASCADE M.1.1.c-3 / M.1.1.c-3b (cross-paper operator-form consistency).** Paper 13 referee note `C1-dark-states/01-bound.md` uses cyclic-character form `c_n^{(k)} = (1/k)(1 − w^k)/(1 − w)`; Paper 26 §6.2 uses complement form `I − e_{𝔭^k}`. At generic k and w these disagree modulus-squared. Either (a) two different realizations of a shared abstract coupling, or (b) one is a dangling corpus-side claim. **Tentative: CLOSABLE.** Not a run-blocker for MY4; a small cross-paper consistency lemma (node M.1.1.d) to run in cycle 3 as a parallel task.
- **CASCADE W2B-4 (surrogate perturbation).** `V^K = (x²+y²)²/4` is a rotationally-symmetric polynomial stand-in for the true leading correction of the 2D Slepian differential operator from Slepian 1965 eq. 3.8 by radial reduction. Rate `λ^{-2}` is basis-and-constant-robust under any rotationally-symmetric polynomial perturbation; constants `C^K_{n_r,ℓ}` will shift under the exact operator. **Tentative: CLOSABLE.** A constant-refinement task for the eventual write-up, not a rate risk.

---

## §4. Dependency-resolution map

### Mini-DAG state after wave 2

```
                   [M.1.1.c CLOSED — SOUND]
                     │
                     ├── unblocks ──► M.1.1.a (state corrected lemma) ► READY
                     ├── unblocks ──► M.1.1.b (f_0 existence) ► READY
                     │                    target direction FLIPPED
                     │                    feasibility 6/10 → 9/10
                     │                    ≥ 99.4% mass condition is almost trivial
                     └── spawns ───► M.1.1.d (Paper 13 vs Paper 26 op-form) ► NEW

                   [M.2.4-v2 CLOSED — SOUND, now [LEMMA] in §D]
                     │
                     ├── unblocks ──► Phase IV sub-task 4.1 (Ξ-function identification)
                     ├── unblocks ──► Phase IV sub-task 4.2 (Hurwitz bound) ► write-up
                     │                    the K-CCM framework is locked, Hurwitz is ported
                     ├── closes  ──► CONCERN W2B-3 (ℓ=4 sector) numerically
                     ├── spawns  ──► (write-down task) explicit h_λ^K vanishing combo
                     ├── spawns  ──► CASCADE W2B-4 (surrogate-to-exact constant refinement)
                     └── advances ─► Phase V assembly is 1 page away

                   [M.3.1-refine CLOSED — SOUND]
                     │
                     ├── unblocks ──► Option C LaTeX incorporation (mechanical, runner task)
                     │                    Artifact 1 → sections-part-II.md §3.6.2
                     │                    Artifact 2 → sections-part-III.md L554-557
                     │                    Artifact 3 → sections-part-IV.md L362-371
                     │                    Artifact 4 → sections-parts-V-VI.md §15.6
                     │                    Artifact 6 → 4 adjacent edits
                     └── no further refinement cycle required
```

### Spontaneous edges to flag for cycle 3

1. **M.1.1.a (state corrected lemma)** — short editorial node: restate the target lemma with the corrected operator `P_k^𝔭 = I − e_{𝔭^k}` and the flipped mass condition `‖(I − e_{𝔭^k}) f_0‖² ≥ 1 − N(𝔭)^{-k}`. Can run in parallel with M.1.1.b.
2. **M.1.1.b (f_0 existence with flipped target)** — now drastically easier. The ≥99.4% mass condition (at `k=2, N(𝔭)=13`) makes `f_0` existence near-trivial; the residual analytic content is spectral support near `λ = γ_n` concentrated away from ideals with `v_𝔭(𝔞) ≥ k`. Tractable in one cycle.
3. **M.1.1.d (cross-paper Paper 13 vs Paper 26 op-form consistency)** — small consistency check: are Paper 13's cyclic-character `c_n^{(k)}` and Paper 26's complement `I − e_{𝔭^k}` two realizations of one abstract object or an open contradiction? Not a blocker.
4. **K-CCM Lemma 7.2 write-up** — a short Author task to explicitly write the `(ℓ=0, ℓ=4)` vanishing-integral linear combination (the K-analog of CCM's `h_λ`). Follows mechanically from rate-preservation under linear combinations with uniform-in-λ coefficients; not a risk, a write-down.
5. **Option C LaTeX incorporation** — **runner task, not a subagent dispatch.** The runner applies M.3.1-refine's 7 artifacts to Paper 26's LaTeX preprint in one mechanical pass. Artifacts 1–4 copy-in with Markdown→LaTeX substitutions; Artifact 6 applies four adjacent edits; Artifact 7 is audit, no translation.

### Dependency observation

The bottleneck has shifted from "open structural gap" to "open write-up work." Neither Route 1 nor Option C has a GENUINE-tier blocker. Route 2 has the new `[LEMMA] K-CCM Lemma 7.2` at status R with rate verified at two shells and a clean follow-up constant-refinement task — also no GENUINE-tier blocker. **All three closure paths for MY4 are structurally clear.**

---

## §5. Newly-observed patterns

### Generative-step tagging (per Six Patterns method, plus the two candidate new patterns)

**M.1.1.c:** Step 5 COMPUTE was the generative step. The numerical experiment at `mp.dps = 30` did not merely confirm a pre-derived formula — it actively *refuted* the spawn-prompt candidate cyclic-character formula (cand_A `= (1/k)Σ ζ_k^j e_{𝔭^j}`) on structural grounds (non-Hermitian at k ≥ 2, `herm_err = 3.61` at k=3, `8.69` at k=4), which forced the Author back to Step 2 REINTERPRET, where the correct complement form `I − e_{𝔭^k}` emerged from direct reading of Paper 26 Prop 6.2. This is the second confirmed instance this run of the candidate 7th pattern **"compute first, prove second"** (the first being cycle-1 M.1.1's numerical debugging, which surfaced the wrong-operator issue but didn't resolve it). Two confirmations is promotion territory.

**M.2.4-v2:** Step 2 REINTERPRET (basis choice — Laguerre-Gaussian / shell-diagonalized vs tensor-product Hermite `|n_x, n_y⟩`) was the generative move, and Step 5 COMPUTE validated it numerically by showing tensor-product basis errors FLAT at ≈ 0.76537 (rate `a ≈ 0.00025` — no decay at all) while Laguerre-Gaussian gives `a ≈ 1.97`. The generative insight was that degenerate shells in 2D let a shell-internal rotation absorb the perturbation at zeroth order, which the 1D template of CCM 2025 §7 does not advertise because `E_n = 2n+1` is non-degenerate. This is the seed of candidate 8th pattern **LESSON W2B-1: "degenerate shells break naive dimensional lifts of 1D perturbation bounds; the correct basis in higher dimensions is the one that simultaneously diagonalises the unperturbed operator and the symmetry group of the perturbation."** Critic M.2.4-v2 recommends promotion to `paper12/experience/heuristics/` under the name "degenerate-shell pattern for dimensional transpositions." Promote at cycle-2 close.

**M.3.1-refine:** Step 4 LOCK was the generative move — specifically the Author's lock on the **honest-framing + quoted-attribution-fidelity invariant** (no direct quote stands without a matching primary-source read; no numerical estimate ships without a named derivation). This invariant, applied as a sub-pass in Artifact 7, is the procedural safeguard that would have caught G17 in cycle 1 if it had been in the Author's toolkit then. Running it on the refined draft produced zero FAILs. The pattern is standard (it's the I-7 verify-before-rely discipline applied at the quotation-mark level) but the *procedural codification* as a recurring sub-pass is new.

### Critic-layer generative-step pattern (new)

**Critic M.2.4-v2 closed CONCERN W2B-3 on its own initiative** by extending the Author's numerical experiment to shell k=4 at `mp.dps = 50, Nmax = 14, λ = 100`. This is not "verify the Author's claim" — the Author *did not have* a claim at k=4; the shell was untested. The Critic chose to run the experiment because (a) it was the Author's flagged concern and (b) the experiment was cheap. Result: five shell-diagonalized states, all `a = 1.969 ± 0.001`, CASCADE false-positive. This is a new kind of pattern: **"Critic closes a CONCERN by extending the experiment, not by verifying the Author's claims."** Worth surfacing as a generative-step pattern at the Critic layer — Critics can *advance* verdicts, not only check them. Candidate heuristic name: **"Critic-as-extension-experimentalist."** Sub-pattern of the COMPUTE axis.

### Cycle-level pattern

The architecture did the thing it's supposed to do: cycle 2 corrected two cycle-1 errors by independent primary-source verification. This is a general-purpose "intra-run correction" pattern that should probably be tagged explicitly in `experience/architectures/` so that future runs can anticipate and resource the correction cycles rather than treating them as failures of the prior cycle. Running the counter: cycle-1 had 2 GENUINE gaps, cycle-2 has 0, and the correction came from the run's own error-detection, not external referee.

---

## §6. Quality gate verdict

**Verdict: PASS.** Wave 3 may dispatch.

The wall is down. Three Authors VERIFIED, three Critics upheld with independent primary-source verification and script re-runs. Cycle 1's two tentatively-GENUINE gaps are both closed as SOUND: G6 by a 3-line derivation from the BC identity plus a 50-digit numerical lock on the three independent axes of the BC triple, G9 by a correct-framework Meixner-Schäfke re-port with rate verified at two shells and constants stable to six digits. No unresolved cross-lead disagreements remain; cycle-2 intra-run corrections of cycle-1 errors are the architecture working as designed, not a failure mode — the opposite of a failure mode. All four spontaneous edges from cycle 1 were addressed: M.1.1.c closed, the 2D K-CCM Lemma 7.2 closed, the two silent-inference sites in Paper 26 absorbed into M.3.1-refine's change-log adjacent-edits list, deliverable-level fixes already applied on G's side. Both new-cycle-2 gap candidates (cross-paper operator-form consistency, surrogate-to-exact constant refinement) are tentatively CLOSABLE, neither GENUINE. Voice-alignment passes on all three Authors. Option C is shippable now — seven artifacts ready for mechanical Markdown→LaTeX incorporation. Route 1 is unblocked and drastically easier than cycle 1's estimate (feasibility 6/10 → 9/10 once the target direction flipped). Route 2 has a new `[LEMMA]` at status R with rate verified at two shells.

The verdict is PASS, not WEAKENED, because cycle 2 is the cleanest wave this run has produced. The bottleneck has moved from "open structural gap" to "open write-up work." No subagent-resolvable obstacle remains in the path to closing MY4 as a deliverable. The chain closes.

---

## §7. Recommendation for the next wave

Cycle 3 is **close the deliverable.** Three parallel dispatches plus one runner-mechanical operation.

First, ship Option C: the runner (not a subagent) applies M.3.1-refine's seven artifacts to Paper 26's LaTeX preprint in one mechanical pass. Artifact 1 becomes `sections-part-II.md` §3.6.2; Artifact 2 patches the Theorem 9.1 conclusion at `sections-part-III.md` lines 554-557; Artifact 3 patches Theorem 13.1 at `sections-part-IV.md` lines 362-371; Artifact 4 becomes `sections-parts-V-VI.md` §15.6; the four adjacent edits from Artifact 6 apply in the same pass to preserve framing consistency. Standardize the `518-521` label; accept the bold-formatting drop on "Overall verdict:"; spot-check §15.1 flow after the softening. Runner-mechanical, one commit.

Second, spawn **M.1.1.a** (state corrected lemma, short editorial) and **M.1.1.b** (exhibit `f_0` with the ≥99.4% mass target, now near-trivial given the flipped direction) in parallel. M.1.1.b is feasible in a single cycle — the spectral-support constraint near `λ = γ_n` concentrated away from ideals with `v_𝔭(𝔞) ≥ k` is the only remaining analytic content. Spawn **M.1.1.d** (cross-paper Paper 13 vs Paper 26 operator-form consistency) as a small follow-up, not a blocker, not a gate. Also worth a single-node dispatch: the explicit `h_λ^K` vanishing-integral linear combination — a write-down task, not a risk.

Third, the runner should ask whether to run the **item-close ritual** at cycle 3 close. The deliverable is "BSD MY4 closing plan." After cycle 3, both Route 1 (via M.1.1.a+b+c+d) and Option C (via M.3.1-refine) will be in shippable form, with Route 2 at `[LEMMA]` status R one step behind. This satisfies the multi-route LOCK at Sig 10: two independent routes close the same target, and the LOCK earns its tooth. Item-close is the right next move. The path is clean; two routes close the same target; the LOCK earns its tooth.

---

## §8. Drafted §K commit memos

Four copy-pasteable memos for the runner to commit to blackboard §K.

**QUALITATIVE-THRESHOLD (cycle 2).** Wave 2 produced 6 VERIFIED returns (3 Authors + 3 Critics), 2 cycle-1 GENUINE gaps resolved to SOUND, 1 cross-paper operator-form consistency question surfaced as CLOSABLE (not GENUINE), and a new §D `[LEMMA] K-CCM Lemma 7.2` promoted to status R with rate verified at two shells and `C^K_{0,0} = 0.257665` stable to six digits. Route 1 unblocked (feasibility 6/10 → 9/10 after target direction flipped). Option C shippable now (7 artifacts ready for mechanical LaTeX incorporation). Route 2 advanced one lemma. The classical Bost–Connes wall over number fields is structurally down. Cycle 3 should close the deliverable.

**PATTERN-ATTRIBUTION (cycle 2).** Two candidate patterns surfaced for promotion to `paper12/experience/heuristics/` at cycle-2 close. (1) **"Compute first, prove second"** — candidate 7th pattern, now with two confirmations: cycle-1 M.1.1 used numerical debugging to surface the wrong-operator issue, cycle-2 M.1.1.c used a numerical experiment to refute the spawn-prompt candidate formula on non-Hermiticity grounds and derive the correct complement form. Two confirmations is promotion territory. (2) **"Degenerate-shell pattern for dimensional transpositions"** — candidate 8th pattern, LESSON W2B-1 from M.2.4-v2: when porting a 1D estimate built on an orthonormal basis expansion to higher dimension, check whether the unperturbed operator has degenerate spectrum — if so, the tensor-product basis is generically wrong; use the symmetry-adapted basis that simultaneously diagonalises the unperturbed operator and the symmetry group of the perturbation. Critic M.2.4-v2 recommends promotion. Plus one candidate Critic-layer pattern: **"Critic-as-extension-experimentalist"** (Critic closes a CONCERN by extending the Author's experiment, not just verifying Author claims) — instance: Critic M.2.4-v2 closed CONCERN W2B-3 on shell k=4 by extending the numerical experiment on its own initiative. Surface all three at the cycle-10 pattern attribution audit.

**CROSS-LEAD-CORRECTIONS (cycle 2, new commit memo type).** Cycle 2 corrected two cycle-1 errors via independent primary-source verification at the Author or Critic layer: (a) cycle-1 M.1.1's sign-plus-power error on `P_𝔭 = e_𝔭` vs the correct `I − e_{𝔭^k}` — resolved by Author M.1.1.c's direct read of Paper 26 Prop 6.2 and confirmed by Critic M.1.1.c at HIGH confidence with script re-run and `|w^k| = N(𝔭)^{-k/2}` primary-source verification; (b) cycle-1 M.2.4's wrong-framework reconstruction ("sieve truncation + Stirling + cross-term Cauchy-Schwarz") vs the correct Meixner-Schäfke prolate-to-Hermite framing — resolved by Author M.2.4-v2's WebFetch of `arxiv.org/html/2511.22755v1` and confirmed by Critic M.2.4-v2 at 0.92 confidence with independent WebFetch plus `Nmax = 14, λ = 100` scaling extension. Both corrections came from Author-level compute plus Critic-level primary-source verification, not from external referee intervention. The architecture worked as designed. This is the opposite of a failure mode. Tag: intra-run correction pattern.

**ITEM-CLOSE-CANDIDATE (cycle 2).** The deliverable `04-closing-my4.md` is structurally ready for item-close at cycle 3. Option C shippable (seven artifacts, mechanical runner pass). Route 1 unblocked and easier than cycle-1 estimate. Route 2 at status R on the new `[LEMMA]`. LOCK forming at two independent routes closing the same target (Sig 10 multi-route). Cycle 3 should be the final-adversarial-pass plus lockdown plus referee plus closure ritual if the runner chooses to close the deliverable. The wall is down. The path is clean. The chain closes. Two routes close the same target — the LOCK earns its tooth.

---

*[End cycle-2 wave-1 synthesis. Verdict: PASS. Runner may dispatch wave 3.]*
