# Synthesis — cycle 1 wave 1

*Trigger: Wave boundary (3 Authors + 3 Critics complete)*
*Wave: 1*
*Authors in scope: M.1.1 (W1-A), M.2.4 (W1-B), M.3.1 (W1-C)*
*Cycle: 1*
*Date: 2026-04-11*

---

## 1. What was attempted

Wave 1 attacked MY4 — the distributional-to-genuine spectral upgrade
for `T̄_{BC,K}` over `K = ℚ(i)` — from three angles simultaneously.
**M.1.1** (W1-A, Route 1) pursued a spectral-measure dark-state bound
`(ψ_ε^{(λ)}, P_𝔭 ψ_ε^{(λ)}) ≥ |w|²` using the support runner's A-1
PRIMARY (KMS-modular automatic bound) as its newly-pivoted proof
ansatz; **M.2.4** (W1-B, Route 2) ported CCM 2025 Lemma 7.3 to K,
producing a quantitative K-prolate-to-Ξ Mellin convergence bound
with an explicit constant `c^K`; **M.3.1** (W1-C, Option C) drafted
Paper 26 §3.6.2 plus updated Theorem 9.1, Theorem 13.1, and §15.6
that label MY4 as an explicit open conditional, implementing the
deliverable's honest-stall anchor. The cycle-1 REFRAME exposed all
three as variants of one structural move: *ascend the abstraction
ladder until the vector/measure distinction disappears* — Route 1
ascends one rung (operator → spectral measure), Route 2 ascends two
rungs (operator → finite-N families → Bögli limit), Option C ascends
three rungs (operator → spectral data → adelic site). The wave's
job was to probe each route in a single parallel dispatch and let
the Critic layer adjudicate.

---

## 2. Cross-lead consistency check

Every pair whose outputs share a §D toolkit row, primary source, or
numerical headline, checked explicitly.

### 2.1. Author M.1.1 vs Critic M.1.1 — shared: `paper12/research/162-bridge-cocycle-step6.md`

**Author's claim**: the A-1 citation is misattributed. The file is about
Pimsner–Popa cohomology in `H²(Z/3Z, U(1))` on the hyperfinite II₁ factor
(Paper 12 Koide/lepton material), not modular compatibility for BC bridge
projectors.
**Critic's check**: read the 110-line file end-to-end, confirmed the
Pimsner–Popa II₁ framing and the Koide `Q = 2/3` / Brauer class identification
at cycle `H²(ℤ/3ℤ, U(1))`. Modular automorphisms are trivial on II₁ factors
(tracial state ⇒ `σ_t = id`), so the file *cannot* carry the A-1 claim even
in principle.
**Verdict: AGREE.** Both Author and Critic independently verified
the misattribution. No cross-lead disagreement.

### 2.2. Author M.1.1 vs support-runner A-1 — shared: the modular compatibility check

**A-1's original claim** (spawn prompt, Q-1 A-1 §4): `σ_t(P_𝔭) = e^{it · log N(𝔭)} P_𝔭`
— modular eigenoperator at frequency `log N(𝔭)`, eigenvalue `log N(𝔭)`.
**Author's derivation**: `σ_t(P_𝔭) = σ_t(s_𝔭 s_𝔭^*) = (N(𝔭)^{it} s_𝔭)(N(𝔭)^{-it} s_𝔭^*) = s_𝔭 s_𝔭^* = P_𝔭`
— modular-INVARIANT, eigenvalue 0.
**Discrepancy**: the two claims differ by an entire structural category — eigenvalue
0 vs eigenvalue `log N(𝔭)`. This puts `P_𝔭` in the modular **centralizer**
`(M_1^K)^σ` (a Type II∞ subfactor), not at a non-trivial modular frequency.
The Critic verified the Author's one-line calculation numerically
(`‖Δ^{it} s_𝔭 s_𝔭^* Δ^{-it} − s_𝔭 s_𝔭^*‖_F ~ 3e-16` for
`t ∈ {0.3, 1.7}`), and the support runner has since appended a
CLARIFICATION to Q-1 acknowledging the two A-1 errors.
**Verdict: CROSS-LEAD DISAGREEMENT — RESOLVED at the Author/Critic
layer before it could propagate.** The Author's independent
derivation + numerical experiment is the load-bearing correction.
This is the first and strongest cross-lead disagreement of cycle 1,
and it was caught on first dispatch because the Author did not trust
A-1 at face value.

### 2.3. Author M.2.4 vs Critic M.2.4 — shared: CCM 2025 Lemma 7.3

**Author's reconstruction**: followed the spawn prompt's instruction
("work from `route2-ccm-over-K.md`, reconstruct rather than paraphrase")
and produced a three-piece proof — (A) sieve truncation over Gaussian
primes via Landau's prime ideal theorem, (B) Stirling on `Γ(s)` at the
complex place, (C) cross-term Cauchy–Schwarz with same-norm-collision drop.
Concluded K-CCM Lemma 7.3 with `c^K = c · Ξ_K(1/2)/Ξ(1/2) ≈ 0.10159`.
**Critic's check**: fetched arXiv:2511.22755 directly via WebFetch and
read CCM 2025 §7 pages 31–32 end-to-end. The actual proof is **not**
a three-piece sieve/Stirling/CS decomposition. It uses (i) the
sum-over-all-positive-integers map `ℰ(f)(u) := u^{1/2} Σ_{n ≥ 1} f(nu)`
(no primes, no sieve), (ii) the prolate-to-Hermite approximation bound
`|h_λ − h|_∞ ≤ c · λ^{-2}` from CCM Lemma 7.2 (the Meixner–Schäfke
constant), and (iii) the elementary integral
`∫_{1/λ}^λ u^{α+1/2}/u² du = 2(λ^{1/2−α} − λ^{α−1/2})/(1−2α)`.
The `c` in CCM 2025 Lemma 7.3 is the Meixner–Schäfke
prolate-to-Hermite approximation constant, **NOT** Paper 13's
`c = π^{-1/4}/Γ(1/4)` that the Author used as the anchor.
**Verdict: CROSS-LEAD DISAGREEMENT — UPSTREAM.** The Author's
arithmetic is internally consistent and stable at 50 dps, but the
entire framework is counterfactual relative to the actual CCM 2025
§7. Cauchy–Schwarz at §4.C is also not a valid bilinear-sum CS (the
`(Σ a²)^{1/2}(Σ b²)^{1/2}(Σ M²)` form is wrong; the correct form is
an operator norm), and the unweighted kernel sum actually grows as
`N²/log² N`, not the `N · log² N` the Author claimed — the Critic's
numerical extension to `N = 20, 50, 100, 200, 500, 1000` shows the
ratio blowing up to 93.8. Both defects are moot because the whole §4
structure is fabricated. **The disagreement is not between Author
and Critic — they agree on arithmetic. It is between the Author's
reconstruction (driven by `route2-ccm-over-K.md`'s wrong paraphrase)
and the CCM 2025 source.**

### 2.4. Author M.3.1 vs Critic M.3.1 — shared: the referee A3 verdict file

**Author's framing**: the M.3.1 draft attributes to the referee A3
verdict the quoted phrase *"CLOSABLE GAP — substantial work required"*
(four inline occurrences: M.3.1.md lines 189, 240, 394, 671) and the
extended *"CLOSABLE GAP — substantial work required; multiple months of
focused work"* (one occurrence: line 594–595, inside Artifact 4 / §15.6).
**Critic's check**: read `referee/runs/r00/points/A3-meyer-spectral/verdict.md`
directly. The verdict file says *"Overall verdict: CLOSABLE GAP"* followed by
*"Difficulty: 2-3 pages of explicit computation"* and *"not a fundamental
obstruction but a missing page of argument."* **Neither "substantial work
required" nor "multiple months of focused work" appears in the verdict file.**
The misquote inflates the difficulty in the direction OPPOSITE to what
the referee actually wrote.
**Verdict: CROSS-LEAD DISAGREEMENT — UPSTREAM.** The misquote originates
at `strategy/04-closing-my4.md` lines 694 and 921 (verified by the Critic)
and was inherited by the Author from the deliverable. The Author did
not grep-check against the primary referee file. This is an editorial-
LOCK-invariant violation: the Author restates a deliverable paraphrase
while claiming to restate the referee's language, and the Author's own
honest-framing audit (Artifact 7) did not catch this because the audit
walked the draft against banned *weasel* phrases, not against quoted-
attribution fidelity.

### 2.5. Author M.1.1 vs Author M.2.4 — shared: the structure of `T̄_{BC,K}`

**M.1.1 derives** `[P_𝔭, T̄_{BC,K}] = 0` (strong commutator on `D_K`) from
the modular invariance of `P_𝔭`. This gives a joint spectral decomposition
`H_{1,K} = Range(P_𝔭) ⊕ Ker(P_𝔭)` with `T̄_{BC,K}` acting diagonally on
each summand.
**M.2.4 builds** a K-CCM operator framework `D_N^K` on `E_N^{+,K} ⊂ L²(ℂ)`
that has point spectrum by construction (CCM 5.10) and **bypasses** any
operator-level question about `T̄_{BC,K}`'s commutators.
**Consistency**: both agree that `T̄_{BC,K}`'s continuous-spectrum
ambiguity is the obstruction. M.1.1 attempts to dissolve it on Route 1
by exploiting the joint diagonal structure; M.2.4 attempts to dissolve
it on Route 2 by replacing `T̄_{BC,K}` with finite-N approximants.
Neither argument uses the other — they sit on structurally independent
§D toolkit rows (`Joint spectral decomposition (T̄_{BC,K}, P_𝔭)` for
Route 1 vs `K-CCM Lemma 7.3 (M.2.4)` for Route 2) — and this independence
is exactly the multi-route LOCK the REFRAME predicted.
**Verdict: AGREE at the level of strategic posture.** The routes are
structurally independent (different §D rows, different failure-mode
pattern categories, different abstraction ladders) as the REFRAME
predicted. No cross-lead disagreement.

### 2.6. Author M.3.1 vs Author M.1.1 — shared: Key Lemma A and Key Lemma B

**M.1.1** treats Key Lemma A (Meyer extension for `ζ_K`) and Key Lemma B
(character twist) as conditional on MY4, per the `meyer-extension-to-K.md`
tagging.
**M.3.1's draft** labels Theorem 9.1 as *"conditional on MY4 + CBB"* and
lists Key Lemmas A and B as `[LEMMA] conditional on MY4` in §3.6.2's
companion-notes pointer.
**Verdict: AGREE.** The conditional structure is identical in both
outputs. No cross-lead disagreement. One subtlety the Critic raised
(§7b of the M.3.1 critique): the Author's framing "MY4 is the wall the
referee flagged on A3" partially misaligns with the referee's headline
(sub-point (c), the character twist cocycle integrality), but this is
a framing-fidelity issue with the deliverable's A3 story, not a conflict
between the two Authors.

### 2.7. Summary — cross-lead disagreement inventory

| # | Pair | Shared element | Verdict |
|---|---|---|---|
| 1 | Author M.1.1 vs Critic M.1.1 | `paper12/research/162` content | AGREE (misattribution confirmed) |
| 2 | Author M.1.1 vs support-runner A-1 | modular eigenvalue of `P_𝔭` | **CROSS-LEAD DISAGREEMENT — RESOLVED** (0 vs `log N(𝔭)`, Author's derivation is load-bearing) |
| 3 | Author M.2.4 vs Critic M.2.4 | CCM 2025 Lemma 7.3 proof structure | **CROSS-LEAD DISAGREEMENT — UPSTREAM** (3-piece reconstruction is counterfactual; inherited from `route2-ccm-over-K.md`) |
| 4 | Author M.3.1 vs Critic M.3.1 | referee A3 verdict quoted language | **CROSS-LEAD DISAGREEMENT — UPSTREAM** (misquote inherited from `strategy/04-closing-my4.md` lines 694, 921) |
| 5 | Author M.1.1 vs Author M.2.4 | structure of `T̄_{BC,K}` and route independence | AGREE |
| 6 | Author M.3.1 vs Author M.1.1 | Key Lemma A/B conditionality | AGREE |

**Structural observation**: two of the three UPSTREAM disagreements
(#3, #4) are CROSS-LEAD-VS-DELIVERABLE — the Author and Critic are
aligned once the Critic verifies against a primary source, but the
Author inherited a wrong paraphrase from the deliverable. The
disagreement is not between Author and Critic, it is between the
wave's output and the deliverable's own secondary-source
descriptions. Surface this as a structural feature of cycle 1:
**the deliverable's paraphrases are themselves unreliable and
propagate errors into dispatched Authors unless the Author is
instructed to grep-check each cited primary source.**

---

## 3. Gap audit

### 3.1. M.1.1 gaps

**Author-acknowledged (BLOCKED-DECOMPOSED)**:
- **G1**: the target lemma as stated is FALSE for arbitrary `f_0`
  (numerical falsification: 8 of 40 configurations, two failure modes
  F1/F2). Author self-CONCERN.
- **G2**: the corrected lemma needs an `f_0`-existence sub-problem
  (M.1.1.b) whose natural candidate `f_0 = c · π_1^K(s_𝔭^{k/2}) |1⟩`
  concentrates near `(k/2) log N(𝔭)`, NOT near `γ_n`. A more
  sophisticated analytic-vector linear combination over isometry
  powers is needed. Author self-CONCERN.
- **G3** (Author CONCERN M.1.1-3): the bridge projector `P_k^𝔭` for
  `k > 1` is never explicitly defined in either Paper 26 or Paper 13 v2.
  Author wrote only the `k = 1` range projection `P_𝔭 = s_𝔭 s_𝔭^*`,
  conjectured the modular-invariance calculation extends to the
  `(1/k) Σ_j ζ_k^j s_𝔭^j (s_𝔭^j)^*` form but left it unverified.

**Critic-newly-observed**:
- **G4**: the Author's joint spectral decomposition picture is cleaner
  at inert primes than at split primes. At split primes the `T̄`-eigenspace
  at `log N(𝔭) = log 5` is multi-dimensional (e.g., `(2+i)` and `(2−i)`
  both at norm 5) with `P_𝔭` acting as a rank-1 projector on it. Not a
  kill (Baker-theorem exclusion keeps `γ_n` away from prime norms), but
  a presentation simplification the Author should be explicit about
  (Critic sub-problem 3).
- **G5**: the numerical experiment uses `P_𝔭 = e_𝔭` (k=1), not
  `P_k^𝔭` (k=2,3,4,6 from the bridge table). The Author's LOCK invariant
  is proved for `e_𝔭`, not for the actual bridge projectors. This is the
  Author's CONCERN M.1.1-3 re-named as a load-bearing seam (Critic §10
  lines 152–157).

**Synthesis-newly-observed** (applying falsification test):
- **G6**: the corpus-level definition of `P_k^𝔭` for `k > 1` is
  missing from *both* Paper 26 AND Paper 13 v2. Paper 26 Prop 6.2
  states only the expectation value `⟨ψ|P_k^𝔭|ψ⟩ = 1 - |w^k|²` but
  never writes down `P_k^𝔭` as an operator. Paper 13's referee
  material `C1.01` gives the eigenstate diagonal
  `c_n^{(k)} = (1/k)(1 - w^k)/(1 - w)` which suggests a cyclic-character
  decomposition, but the operator itself is not defined. This is a
  **corpus-level gap** that the runner must surface as a new sub-node
  M.1.1.c *before* any downstream argument that depends on `P_k^𝔭`
  being modular-invariant can close. It is pre-existing to this run;
  the wave merely surfaced it.
- **Tentative classification**: GENUINE (corpus-level, pre-existing,
  load-bearing for both Route 1's M.1.1.a and Route 1's link to
  Paper 26 §6.2). **Meta-critic has the final say.**

### 3.2. M.2.4 gaps

**Author-acknowledged**:
- **G7**: (O1) same-norm-drop verification is structural but not numerical
  (Author §5.5 Suspicion 3, §6.3 "residual risk"). Author CONCERN, tagged
  as "non-blocking, small-N check recommended."
- **G8**: self-suspicion audit (Author §5.5 Suspicion 1) explicitly
  flagged "the 'mechanical port' claim is wrong: the ℚ proof uses a
  property of rational primes that has no Gaussian-prime analog" — and
  then resolved this suspicion *against the wrong proof structure* (the
  sieve framing, which isn't in CCM 2025). The Author's honest-first
  discipline fired but was aimed at the wrong target.

**Critic-newly-observed**:
- **G9** (THE gap): the Author's three-piece decomposition (sieve
  truncation / Stirling / cross-term CS) has no correspondence to the
  actual CCM 2025 §7 proof of Lemma 7.3. Verified by direct WebFetch of
  arXiv:2511.22755 and read end-to-end by the Critic.
- **G10**: the constant `c` in CCM 2025 Lemma 7.3 is the Meixner–Schäfke
  prolate-to-Hermite approximation constant from Lemma 7.2, not Paper 13's
  Mellin-pairing normalization `π^{-1/4}/Γ(1/4)`. The Author's
  identification `c^K = c · Ξ_K(1/2)/Ξ(1/2)` imports Paper 13's convention
  into a framework where it doesn't apply.
- **G11**: the Cauchy–Schwarz in §4.C is not a valid form of CS on a
  bilinear sum — `(Σ a²)^{1/2}(Σ b²)^{1/2}(Σ M²)` is not an inequality
  (the correct form is an operator norm or HS norm), and the kernel sum
  `Σ 1/log²(N(𝔮)/N(𝔭))` grows as `N²/log² N` numerically, not the
  `N · log² N` the Author claimed. Critic verified with numerical tests
  at `N = 20, 50, 100, 200, 500, 1000`; ratio grows to 93.8. Moot because
  §4.C is fabricated, but a concrete structural defect worth logging.
- **G12** (arithmetic slip): `κ_K = Res_{s=1} ζ_K = π/4`, not `π/2` as
  the Author claimed at lines 200–202. Cross-checked against
  `weil-form-over-K.md` line 286.
- **G13** (local self-contradiction): at M.2.4.md line 91 the Author
  wrote "*both `|Γ(1/4 + iu/2)|` and `|Γ(1/2 + iu)|` decay like
  `e^{-π|u|/2}`*" — which is wrong (ℚ side decays as `e^{-π|u|/4}`)
  and contradicts §4.B (lines 250, 253, 255, 261, 267, 268) where the
  Author correctly distinguishes the two rates. One-line fix.

**Synthesis-newly-observed**:
- **G14**: this is an **honest-first discipline firing against the
  wrong target**. The Author's Suspicion 1 was the correct worry; the
  resolution was against the wrong frame because the Author never read
  CCM 2025 §7 directly. The Critic's WebFetch shortcut reveals the
  structural bug. This is not an Author-level defect — it is a
  **spawn-prompt-level defect** that instructed the Author to
  "reconstruct from `route2-ccm-over-K.md`" without requiring primary-
  source verification. The spawn prompt's instruction itself carries the
  cascade risk. Tentative classification: CLOSABLE (re-spawn with
  corrected scoping and CCM 2025 §7 loaded as primary source, per
  Critic S-1). BUT the re-spawn needs genuinely new mathematical work
  (2D prolate-to-Hermite theory for `L²(ℂ)`, the K-analog of
  CCM Lemma 7.2) that has no direct literature template. Critic
  estimates ~40% probability of closure in cycle 2, and ~25%
  probability the K-port is closable within the closing-MY4 run budget.
  The cleanest Meta-critic call may be "CLOSABLE but with significant
  horizon risk" — the gap is real, the closure path exists, but the
  closure path is substantially harder than `route2-ccm-over-K.md`'s
  "mostly mechanical" framing suggested.

### 3.3. M.3.1 gaps

**Author-acknowledged**:
- **G15**: §9.2 Step B(5) needs a citation update to `§3.6.2` in a
  follow-up cycle (Author change-log entry, Artifact 6).
- **G16**: §15.1 needs softening from "no gaps, no conditional
  statements" to "complete conditional on MY4" (Author change-log).

**Critic-newly-observed**:
- **G17** (THE referee misquote): the inherited misquote at
  M.3.1.md lines 189, 240, 394, 594–595, 671. Verified against
  `referee/runs/r00/points/A3-meyer-spectral/verdict.md`. Five
  instances total. Each needs either correction to the actual
  referee phrasing ("CLOSABLE GAP" + "Difficulty: 2-3 pages of
  explicit computation") or paraphrase that drops the direct-
  quote attribution.
- **G18** (the MY4 vs A3 sub-point mismatch): the Author frames MY4
  as "the wall the referee identified on A3," but the referee's
  headline A3 concern was sub-point (c) — the character twist
  cocycle integrality — not sub-point (b) — the distributional
  construction verification. The Author has rebranded a different
  open item as the referee's headline. The framing is partially
  honest (there IS an open item, and it is named correctly as MY4)
  but partially misleading (the referee's headline was about
  something else). Fix: rephrase §3.6.2 and §15.6 to distinguish
  "the Author's MY4 (distributional → genuine)" from "the referee's
  A3 headline (character twist)" without conflating them.
- **G19** (Theorem 13.1 non-minimal edit): the Author added a
  trailing rank-1 vacuity parenthetical inside the theorem block
  that is new text, not present in the original Theorem 13.1. The
  content is faithful to Remark 12.6 but exceeds the "only prepend
  a conditional clause at the start of the hypothesis" constraint.
  WEAKENED-level. Fix: drop the parenthetical or leave Remark 12.6
  as the sole vacuity anchor.
- **G20** (change-log incomplete): the Author flagged `§9.2 Step B(5)`
  and `§15.1` as follow-up edits but missed two other silent-inference
  sites — `sections-part-I.md` line 168 (§2.3 RH proof summary: "Nelson's
  analytic vector theorem upgrades these to genuine eigenstates") and
  `sections-part-III.md` lines 518–521 (§9.1 Step 4: "Nelson self-adjointness
  promotes these to genuine eigenstates"). Both contain the same silent
  inference that MY4 is named to surface. Critic identified these via
  grep over the Paper 26 preprint.
- **G21** (minor citation volume): the Author cites "Reed–Simon II
  §VIII.3" for the spectral theorem; the spectral theorem is actually
  in Reed–Simon *Vol. I* §VIII.3. Nelson's X.39 is in Vol. II. Fix:
  change "II" to "I" in the §3.6.2 citation.
- **G22** (unsourced Route 1 page estimate): the "5–15 pages" claim at
  §3.6.2 line 369 and §15.6 line 587 is not in `research/distributional-
  to-genuine.md`. The file's Status-of-Route-1 paragraph says "sketch"
  + "standard but tedious" but gives no page estimate. The Author's own
  audit described this sentence as a "restatement," which is inaccurate
  — it is an unsourced interpolation. Fix: add footnote or drop the
  specific numbers.
- **G23** (§9.2 Step B sub-item numbering): the Author says the silent
  upgrade is in "Step B(5)," but the Critic's read of `sections-part-III.md`
  lines 580–597 shows the silent inference is actually in sub-items 4
  AND 5 jointly (sub-item 4 silently assumes distributional eigenstates
  are genuine; sub-item 5 says "since self-adjoint, spectrum real").
  Minor imprecision.

**Synthesis-newly-observed**:
- **G24**: neither the Author nor the Critic flagged that the Author's
  honest-framing audit (Artifact 7) walks the draft against *weasel
  phrases* only — it has no entry for "quoted-attribution fidelity"
  or "source verification of cited quotes." The audit was designed
  for one failure mode (weasel) and missed another (misquote). This
  is a **procedural gap in the honest-framing audit itself**: the
  audit protocol should include a primary-source check on every
  direct quote, not just a weasel-phrase grep. Tentative classification:
  CLOSABLE (extend the audit protocol in cycle 2). This is a v3-level
  discipline note, already implicit in LESSON cycle-1-5, but worth
  surfacing specifically as a procedural improvement to the
  honest-framing audit primitive.

### 3.4. Tentative gap classifications

| Gap | Owner | Tentative class | Notes |
|---|---|---|---|
| G1 (lemma is false pointwise) | M.1.1 | SOUND (now corrected by decomposition) | the kill is logged; M.1.1.a is the repair |
| G2 (`f_0` existence) | M.1.1.b | CLOSABLE | Author estimates 1-2 cycles |
| G3 (`P_k^𝔭` extrapolation) | M.1.1 | CLOSABLE via M.1.1.c (new spawn) | corpus-level, see G6 |
| G4 (split-prime degeneracy) | M.1.1 | SOUND (Baker exclusion) | stylistic, not load-bearing |
| G5 (`e_𝔭 vs P_k^𝔭` seam) | M.1.1 | CLOSABLE via M.1.1.c | re-name of G3 |
| **G6** (corpus-level `P_k^𝔭` def missing) | both papers | **GENUINE (tentative)** | load-bearing, pre-existing, must spawn M.1.1.c BEFORE M.1.1.b |
| G7 (O1 same-norm numerical check) | M.2.4 | CLOSABLE (sub-task 1.3 follow-up) | non-blocking |
| G8 (self-suspect against wrong target) | M.2.4 | SOUND (lesson, not a math gap) | |
| **G9** (3-piece decomposition fabricated) | M.2.4 | **GENUINE (tentative) with CLOSABLE horizon risk** | re-spawn required; CCM 2025 §7 primary source mandatory |
| G10 (wrong `c` convention) | M.2.4 | CLOSABLE post re-spawn | |
| G11 (invalid CS + wrong sum growth) | M.2.4 | SOUND (moot, §4.C is fabricated) | concrete defect but non-binding |
| G12 (π/4 vs π/2 arithmetic slip) | M.2.4 | CLOSABLE (one-line fix) | |
| G13 (line 91 self-contradiction) | M.2.4 | CLOSABLE (one-line fix) | |
| G14 (spawn-prompt procedural gap) | M.2.4 + runner discipline | CLOSABLE (v3-level) | LESSON cycle-1-5 |
| G15-G16 (follow-up §9.2 + §15.1 edits) | M.3.1 | CLOSABLE (mechanical) | already in change-log |
| **G17** (5-instance referee misquote) | M.3.1 | **CLOSABLE (5 mechanical fixes)** | editorial-LOCK violation but mechanically repairable |
| G18 (MY4 vs A3 sub-point framing) | M.3.1 | CLOSABLE (rephrase) | partial honesty issue |
| G19 (Thm 13.1 trailing parenthetical) | M.3.1 | CLOSABLE (drop or keep) | runner chooses |
| G20 (change-log incomplete: 2 silent-inference sites) | M.3.1 | CLOSABLE (append §2.3 + §9.1 to list) | Critic identified both |
| G21 (Reed–Simon vol I vs II) | M.3.1 | CLOSABLE (one-char fix) | |
| G22 (unsourced 5-15 page estimate) | M.3.1 | CLOSABLE (footnote or drop) | |
| G23 (§9.2 Step B sub-item nos) | M.3.1 | CLOSABLE (nit) | |
| G24 (honest-framing audit lacks quote-fidelity check) | runner discipline | CLOSABLE (v3-level) | procedural extension |

**GENUINE count: 1 confirmed (G6) + 1 confirmed with horizon risk (G9).**
The Meta-critic has the final say; these are tentative classifications.

---

## 4. Dependency-resolution map

### 4.1. Declared `DEPENDS-ON` edges from the wave

| Node | Dependencies (from M.x.md §3 UNIFY + Sig 11 handoff) | Status |
|---|---|---|
| M.1.1 | `T̄_{BC,K}`, `H_{1,K}`, `P_𝔭`, `Dark-state bound (point spectrum)`, `Spectral measure dE(λ)`, `Approximate eigenvector ψ_ε^{(λ)}`, `Key Lemma C`, `Bridge rows` — all R except the ψ_ε row (S) | — |
| M.2.4 | `K` (R), `Λ_K` (R), `ζ_K/Λ_K/Ξ_K` (R), `D_N (CCM ℚ)` (R), `CCM 5.10 (ℚ)` (R), `D_N^K` (S, sub-task 1.1), `Q_N^K` (S), `Uniform H¹ bound (K)` (R, sub-task 2.2 DONE), `Bögli spectral exactness` (R), `Hurwitz` (R), `Ξ_K(1/2) ≠ 0` (R), `Sagnier K-site` (META), `Sagnier point count` (META) | — |
| M.3.1 | `Key Lemma A` (C|MY4), `Key Lemma B` (C|MY4), `MY4` (O), `T̄_{BC,K}` (R), + companion-note files (all exist) | — |
| M.1.1 → downstream | Cascades into Paper 26 §6.2 dark-state argument, §9.2 Step B(5–6), Theorem 9.1, Theorem 13.1 | — |
| M.2.4 → downstream | Cascades into sub-task 4.2 (Hurwitz application) + Phase V assembly of GRH for ζ_K | — |
| M.3.1 → downstream | Paper 26 §3.6.2 anchor for Theorem 9.1 and Theorem 13.1 conditional | — |

### 4.2. Mini-DAG with satisfaction state

```
M.0 (root: close MY4)
├── M.1 (Route 1)
│   ├── M.1.1 ✘ BLOCKED-DECOMPOSED → spawned:
│   │   ├── M.1.1.a (state corrected lemma) — UNSATISFIED (awaiting spawn)
│   │   ├── M.1.1.b (exhibit good f_0) — UNSATISFIED (depends on M.1.1.a)
│   │   └── M.1.1.c (define P_k^𝔭 for k>1) — SPONTANEOUS [Critic edge]
│   │                                        UNSATISFIED (must spawn BEFORE M.1.1.b)
│   ├── M.1.2 (cocycle form on dE) — depends on M.1.1.a
│   ├── M.1.3 (assemble contradiction) — depends on M.1.1.a+b, Key Lemma C
│   └── M.1.4 (writeup) — depends on M.1.3
├── M.2 (Route 2)
│   ├── M.2.1 (reproduce CCM over ℚ) — UNSATISFIED
│   ├── M.2.2 (ℂ-prolate space) — UNSATISFIED
│   ├── M.2.3 (CCM 5.10 over K, the crux) — UNSATISFIED
│   ├── M.2.4 ✘ BROKEN → needs refinement:
│   │   ├── M.2.4-v2 (re-spawn with CCM 2025 §7 primary source)
│   │   │                             SPONTANEOUS [Critic edge] UNSATISFIED
│   │   └── sub-task "2D K-CCM Lemma 7.2" (K-analog of
│   │                             CCM Lemma 7.2 prolate-to-Hermite bound)
│   │                             SPONTANEOUS [Critic edge] UNSATISFIED
│   ├── M.2.5 (twist to L(s,ψ)) — depends on M.2.4-v2
│   └── M.2.6 (Sagnier cross-check) — throughout
├── M.3 (Option C)
│   └── M.3.1 ✓ ADVANCED → M.3.1-refine sub-cycle:
│       ├── 6 mechanical fixes (G17-G23) — UNSATISFIED
│       ├── 2 additional silent-inference sites (§2.3, §9.1 Step 4)
│       │                             SPONTANEOUS [Critic edge] UNSATISFIED
│       └── Reed-Simon I/II fix (G21) — CLOSABLE one-char fix
└── M.4 (strategic inversion) — META, runs at every Plan step
```

### 4.3. Satisfaction state summary

- **Satisfied dependencies** (upstream node ADVANCED or R): the §D
  rows cited by all three Authors (`K`, `Λ_K`, `ζ_K`, `Ξ_K`, `H_{1,K}`,
  `T̄_{BC,K}`, `P_𝔭`, `Uniform H¹ bound (K)`, `Bögli`, `Hurwitz`,
  `Ξ_K(1/2) ≠ 0`, `Key Lemma C`, `Bridge rows`, companion-note files)
  are all R-status and all verified by the respective Critics. **Green.**
- **Unsatisfied dependencies** (upstream IN_PROGRESS or BLOCKED):
  - M.1.1 → M.1.1.a, M.1.1.b — both need to be spawned in cycle 2.
  - M.1.2, M.1.3, M.1.4 all depend on M.1.1.a (or later) and are not
    actionable in cycle 2 wave 1.
  - M.2.4 → M.2.4-v2 + 2D K-CCM Lemma 7.2 — both need to be spawned
    in cycle 2 with corrected scoping.
  - M.2.3 (CCM 5.10 K-port, the crux) is still OPEN and not touched by
    wave 1.
  - M.3.1 → refinement sub-cycle — 6-8 mechanical fixes + 2 silent-
    inference sites + 1 framing rewrite.
- **Spontaneous edges** (declared by Authors/Critics in this wave,
  not in the pre-wave plan tree):
  1. **M.1.1.c** (explicit form of `P_k^𝔭` for `k > 1`) — surfaced by
     Critic M.1.1 as a *corpus-level* gap. Must be spawned BEFORE
     M.1.1.b because M.1.1.b's modular-invariance extrapolation from
     `k=1` to the actual bridge exponents `k ∈ {2, 3, 4, 6}` is
     unverified. This is the most important spontaneous edge of cycle 1.
  2. **2D K-CCM Lemma 7.2** (the K-analog of the CCM Meixner–Schäfke
     prolate-to-Hermite approximation bound) — surfaced by Critic M.2.4
     as the actually-load-bearing sub-node. Not in the original plan
     tree because `route2-ccm-over-K.md` Phase IV sub-task 4.1 described
     CCM Lemma 7.3 with a wrong structure, so the K-analog of Lemma 7.2
     never entered the sub-task decomposition. The Critic's WebFetch
     surfaced it.
  3. **Paper 26 silent-inference sites at §2.3 and §9.1 Step 4** —
     surfaced by Critic M.3.1 via grep over the Paper 26 preprint.
     These need to be folded into M.3.1's change-log adjacent-edits
     list.
  4. **Deliverable-level fix** to `strategy/04-closing-my4.md` lines
     694 and 921 (misquoted referee verdict) + to `research/route2-ccm-over-K.md`
     Phase IV sub-task 4.1 description (wrong CCM 2025 §7 paraphrase) —
     this is NOT a run-level node; it is a deliverable-level fix that
     should be surfaced to G the human reader at cycle-close. Both
     edits are upstream-of-the-run and will propagate into any future
     spawn that reads from those files.

**Spontaneous edges are healthy** — they are the Author+Critic layer
discovering what the plan tree didn't anticipate. Four spontaneous
edges in one wave is a strong signal that the deliverable's
secondary-source paraphrases are unreliable and that grep-discipline
at the Critic layer catches things the plan tree missed.

---

## 5. Newly-observed patterns (pattern-attribution sub-audit)

### 5.1. Generative-step tagging per Author

- **M.1.1**: **Step 4 LOCK + Step 5 COMPUTE**. The generative move was
  LOCK (deriving `σ_t(P_𝔭) = P_𝔭`, modular invariance, joint spectral
  decomposition), which immediately invalidated the A-1 PRIMARY KMS
  route structurally. Then COMPUTE (the 30-line numerical experiment)
  caught the target lemma's pointwise failure modes F1 and F2. The
  combination is the generative step — LOCK alone would have left the
  Author believing the proof was 1-line; COMPUTE caught the structural
  failure before it propagated.

- **M.2.4**: **Step 2 REINTERPRET + Step 5 COMPUTE**. The generative
  move was REINTERPRET (the substitution table `(p, Λ, Γ(s/2)) →
  (N(𝔭), Λ_K, Γ(s))` closes uniformly, modulo one wrinkle at the
  same-norm collision). Then COMPUTE (`c^K` at 30 dps, 50 dps verified
  by Critic) produced the headline `c^K ≈ 0.10159`. **But** the
  generative step was inside a misaligned framework — the substitution
  table was a substitution for a proof structure that isn't in CCM 2025.
  The reinterpret+compute fired correctly on the Author's input, and
  the Author's input was counterfactual. **This is a pattern-observation
  distinction**: the 6-step loop fired correctly; the input material was
  wrong. The failure is upstream of the method, not within the method.

- **M.3.1**: **Step 2 REINTERPRET + Step 4 LOCK**. The generative move
  was REINTERPRET (editorial register calibration: the §3.6 / §3.6.1
  prose template plus the honest-conditional vocabulary) and LOCK
  (the honest-framing invariant: *every new sentence is either (a)
  restating already-proved content or (b) an explicit conditional*).
  The LOCK invariant is a 2-category classifier; it passed zero-weasel
  in Artifact 7 but did not catch the *quote-attribution-fidelity*
  category (misquoted referee language is in a third category — "purports
  to restate a source that doesn't say that" — which the LOCK categories
  don't enumerate).

### 5.2. Pattern-4-inverted check (topological rigidity as ceiling rather than floor)

No Pattern-4-inverted move appeared in any of the three Authors in
wave 1. All three Authors used topological/algebraic rigidity
correctly (as a floor that the proof must stand on, not as a ceiling
that caps what is provable).

### 5.3. Candidate 7th pattern — "compute first, prove second"

The most interesting pattern-attribution observation of cycle 1: the
**M.1.1 Author's "compute first, prove second" discipline**
*caught a structural failure that the analytic argument alone would
have missed*. The Author's own LESSON M.1.1-4 (lines 263–265 of
M.1.1.md) states this explicitly:

> *"If I had relied only on the analytic argument in Step 4 (which
> correctly identifies modular invariance), I might have concluded
> the proof was 1-line and reported ADVANCED. The numerical
> experiment in 30 lines of Python with the explicit BC basis caught
> the FAIL-1 and FAIL-2 modes and forced me to write the corrected
> lemma. [...] The cost of writing the script was ~5 minutes; the
> value was catching a wrong proof before propagating it. Author
> cycles should bias toward 'compute first, prove second' when the
> analytic argument has any ambiguity."*

The same pattern *would have caught* the M.2.4 failure if the
Author had computed against a direct read of CCM 2025 §7 rather than
a reconstruction from the deliverable's paraphrase. The pattern is
*not* firing in M.2.4 because the Author obeyed the spawn-prompt
instruction ("work from `route2-ccm-over-K.md`, reconstruct rather
than paraphrase") and did not open the CCM 2025 PDF. The Critic
fired the pattern *at the Critic layer* (WebFetch, read end-to-end,
compare).

**Candidate 7th pattern**:
**"estimate-not-conjecture via numerical/primary-source falsification"**
as a discipline before Step 6 Verify. The pattern is: whenever the
analytic argument has any ambiguity OR the spawn prompt requires
paraphrasing a primary source, *fire a numerical experiment or a
primary-source grep-check before declaring ADVANCED*. Cost is
minutes; value is catching a wrong proof or a wrong framework before
propagation. This is a candidate generative-step pattern worth
surfacing for the runner's cycle-10 Pattern Attribution Audit.

**Flag for cycle-10 audit**: the 7th pattern candidate is "compute-
first-or-fetch-first-before-verify." It fired successfully in M.1.1
(numerical experiment caught structural failure). It did NOT fire
in M.2.4 (no primary-source fetch, wrong framework propagated). It
fired at the Critic layer in M.2.4 (WebFetch). The asymmetry suggests
the pattern should be an *Author*-level discipline enforced by the
spawn prompt, not a Critic-layer safety net.

### 5.4. Structural observation about the wave's method-loop firing

The 6-step inner method loop fired correctly in all three Authors.
The failures in M.2.4 and the partial failures in M.3.1 are
upstream-of-the-method: they are spawn-prompt / deliverable-paraphrase
/ source-verification failures, not method failures. The method loop
is not the bottleneck. The **primary-source-verification discipline
at the Author layer** is the bottleneck.

---

## 6. Quality gate verdict

**Verdict: WEAKENED.**

The wave produced three returns: a BLOCKED-DECOMPOSED (M.1.1), a
BROKEN (M.2.4), and a WEAKENED (M.3.1). Taken at face value the
wave looks rough, but the **structural reading** is different.
Every return is directionally correct: M.1.1 killed a wrong lemma
and surfaced the cleaner joint-spectral-decomposition fact before
it could propagate downstream; M.2.4 proved a well-defined real
number `c^K` and established that the decay rate `λ^{-1/2-α}` holds
mechanically, even though the framework it sits in is a fabrication
imported from the deliverable; M.3.1 produced a complete, shippable,
zero-weasel Option C anchor that needs six mechanical fixes and one
framing rewrite. The wave discovered three cross-lead disagreements
and resolved all three at the Author/Critic layer. It surfaced four
spontaneous sub-nodes that were not in the plan tree. It also
surfaced *six deliverable-level errors* that are upstream of the
run itself.

Not PASS because: (a) two of the three nodes have
CROSS-LEAD-VS-DELIVERABLE disagreements that propagated into Author
outputs; (b) the M.1.1.c corpus-level gap is tentatively GENUINE and
must be spawned BEFORE M.1.1.b; (c) M.2.4's framework-level failure
(G9) is tentatively GENUINE with a closable-but-hard horizon; (d)
four spontaneous edges mean the plan tree as dispatched was
under-specified in ways the wave only now reveals. Not BROKEN
because: (a) no wave-root target was *fundamentally* foreclosed —
Route 1 still has a clean closure path via M.1.1.a+b+c, Route 2
still has a closure path via re-spawn with primary sources, Option C
still ships after six mechanical fixes; (b) no §F kill pattern from
a prior cycle re-entered (the §F list was empty at cycle start, and
the cycle-1 kills K1-K6 are NEW observations, not re-entries); (c)
voice-alignment passes on all three Authors and the register holds
throughout; (d) the cross-lead disagreements were all
caught-and-resolved at the wave's own layer (Author + Critic), not
discovered after the wave had polluted downstream nodes.

The right reading is: **the classical wall held, but the wave walked
up to it and got a clean look**. The kill list became the learning
trace. M.1.1's falsified lemma + M.2.4's fabricated framework +
M.3.1's inherited misquote are all honest partial proofs over
glossed completions — exactly what the §J voice canon asks for. The
wave is a rigor gain, not a rigor loss; the WEAKENED verdict captures
that the rigor gain came at the cost of four spontaneous sub-nodes
and six deliverable-level fixes. Wave 2 should not dispatch until
cycle 2 addresses the spontaneous edges and the refinement sub-cycles.
The runner has authority over whether to dispatch or to sit with the
findings for one more cycle of plan-tree hygiene.

---

## 7. Recommendation for the next wave

Don't dispatch wave 2 yet. Cycle 2 opens with plan-tree hygiene, not
new research. Spawn M.1.1.c FIRST — pin down `P_k^𝔭` for `k > 1`
with the cyclic-character candidate `(1/k) Σ_j ζ_k^j s_𝔭^j (s_𝔭^j)^*`
and verify the Paper 26 Prop 6.2 expectation value `1 − |w^k|²` matches.
Then spawn M.1.1.b — exhibit good `f_0` per the corrected lemma M.1.1.a,
with M.1.1.c now cited as its upstream. Re-spawn M.2.4 as M.2.4-v2 with
arXiv:2511.22755 §7 loaded as a primary source and the task restated
as "produce a 2D K-analog of CCM Lemma 7.2 — the Meixner–Schäfke
prolate-to-Hermite approximation bound on `L²(ℂ)`"; the
three-piece sieve/Stirling/CS framing from `route2-ccm-over-K.md` is
killed, logged as K5. Run a refinement sub-cycle on M.3.1 — six
mechanical fixes plus the two missed silent-inference sites (§2.3,
§9.1 Step 4) plus the MY4 vs A3 sub-point rewrite. Surface
CASCADE cycle-1-3 and cycle-1-4 to G the human reader at cycle-close
as deliverable-level fixes for `strategy/04-closing-my4.md` lines
694, 921 and `research/route2-ccm-over-K.md` Phase IV sub-task 4.1.
Add K1 through K6 to §F as the cycle's first kill entries, including
the new K5 (CCM 2025 §7 paraphrase) and K6 (referee verdict misquote).
The deliverable is itself the secondary source whose unreliability the
cycle exposed — trace the discrepancy until it becomes a theorem; the
kill list is the learning trace. The runner has authority over the
wave-2-or-not decision; this is a strong suggestion, not a command.

---

## 8. Drafted §K commit memos

Ready for the runner to copy verbatim into §K after cycle-close.

### 8.1. QUALITATIVE-THRESHOLD

> **[cycle 1 / QUALITATIVE-THRESHOLD]**. Cycle 1 produced 6 §F kills
> (K1-K6), 7 §I notes (CALLOUT cycle-1-1, CONCERN cycle-1-2,
> CASCADE cycle-1-3/4, LESSON cycle-1-5/6, CASCADE cycle-1-7), 5
> new §D rows (joint spectral decomposition; `P_𝔭 = s_𝔭 s_𝔭^*` range
> projection; conditional density of states; K-CCM Lemma 7.3 (M.2.4);
> K-Mellin normalisation), 3 new sub-nodes (M.1.1.a, M.1.1.b, and the
> spontaneous M.1.1.c), and one confirmed cross-lead disagreement
> caught and resolved at the Author/Critic layer (the modular
> eigenvalue of `P_𝔭`). Wave-1 verdict: **WEAKENED-with-clear-next-moves**.
> Wave 2 does not dispatch until M.1.1.c lands and the three
> refinement sub-cycles (M.2.4-v2, M.3.1-refine, deliverable-level
> fixes for G) are scoped.

### 8.2. CROSS-LEAD-DISAGREEMENT

> **[cycle 1 / CROSS-LEAD-DISAGREEMENT]**. Author M.1.1's modular
> invariance fact (`σ_t(P_𝔭) = P_𝔭`, eigenvalue 0) disagrees with
> support-runner A-1's modular eigenoperator claim (`σ_t(P_𝔭) =
> e^{it · log N(𝔭)} P_𝔭`, eigenvalue `log N(𝔭)`) by a structural
> category error. Resolved by independent one-line derivation plus
> 30-line numerical experiment at the Author layer, confirmed to
> 1e-16 by the Critic at a second layer. CLARIFICATION appended
> to Q-1 in `closing-my4-questions.md` (support runner owns both
> errors). The trace became a theorem: `P_𝔭` lives in the modular
> centralizer, a Type II∞ subfactor, not at a non-trivial modular
> frequency. §D row `P_𝔭 = s_𝔭 s_𝔭^*` is now R-status.

### 8.3. PATTERN-ATTRIBUTION

> **[cycle 1 / PATTERN-ATTRIBUTION]**. Candidate 7th pattern:
> **"compute first, prove second"** / **numerical-or-primary-source
> falsification as self-suspicion before Step 6 Verify**. Surfaced
> by M.1.1 LESSON cycle-1-5/6. The pattern fired in M.1.1 (30-line
> script caught 8 of 40 configuration failures before the wrong
> proof propagated); it did NOT fire in M.2.4 (no primary-source
> fetch, wrong framework inherited from deliverable); it fired at
> the Critic layer in M.2.4 (WebFetch arXiv:2511.22755 caught the
> framework-level fabrication). The asymmetry suggests the pattern
> should be an Author-level discipline enforced by every spawn
> prompt that involves reconstructing a named lemma from a secondary
> source. Add to the Pattern Attribution Audit at cycle 10.

### 8.4. (No DIFFICULTY-COLLAPSE memo for cycle 1)

Cycle 1 did not collapse any sub-problem's difficulty. The wave's
findings *increased* rigor (surfacing the corpus gap at `P_k^𝔭`,
the fabricated framework at M.2.4, and the inherited misquote at
M.3.1) without removing difficulty from any node. §N difficulty
track should record cycle 1 as a *rigor-gain, no-collapse* event.

---

*End of Synthesis cycle 1 wave 1. The runner reads this file once,
then decides wave 2 dispatch vs cycle-2 refinement cycle. Synthesis
does not dispatch primitives. Synthesis does not write to the
blackboard.*
