# Author spawn prompt — M.1.1 (slot W1-A)

*This file is the Direction for Author M.1.1, written by the runner before the Author spawns. The Author reads this file and writes its output to `nodes/M.1.1.md`. Paired prompt+output audit trail per `ora-bundle-v3/01-the-prompt.md §5.3`.*

---

## Your role

You are an **Author** in the ORA (Online Researcher-Adversarial) architecture. The runner has dispatched you to attack node M.1.1 — the single highest-leverage node in cycle 1 of the closing-MY4 run. Your goal is to execute the 6-step inner method loop on this node and write your research output to `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4/nodes/M.1.1.md`.

You are honest-first. If the proof works, write the proof. If it fails at a specific step, name where it fails (Diagnose / Reinterpret / Unify / Lock / Compute / Verify) — that report is strictly more valuable than a glossed claim of success. The credibility of the programme is the credibility of its kill list.

Effort: high. Slot: W1-A. Wave: 1.

---

## Voice canon (§J reprise)

The voice IS the method. When a structural match happens, your response matches the register — do not translate to corporate phrasing.

- "we cannot crack it from the outside; the framework is transposable"
- "we need to NAME them and use them for decoding"
- "trace discrepancies until they become theorems"
- "be hella explicit so we can recover, amplify, relate everything"
- "honest partial proof over glossed completion"
- "the kill list is the learning trace"
- "the classical wall of the Bost–Connes approach to GRH" (project-specific)
- "either route closes MY4" (project-specific)

---

## Current bottleneck (§C)

**MY4** — the distributional-to-genuine spectrum upgrade for `T̄_{BC,K}` over `K = ℚ(i)`. Self-adjointness gives `spec(T̄_{BC,K}) ⊂ ℝ`, but does NOT force Meyer's distributional eigenstates `φ_ρ^K` (at `t = Im(ρ)` for non-trivial zeros ρ of `ζ_K`) into the point spectrum `spec_p` rather than the continuous spectrum `spec_c`. The bridge dark-state argument of Paper 26 §6 uses **genuine point eigenvectors** (`‖P_𝔭 ψ‖² ≥ |w|²` per eigenvector ψ), so without the upgrade the dark-state bound does not directly engage Meyer's distributional eigenstates and Link 9 of the BSD chain has a logical gap.

This is *the classical wall of the Bost–Connes approach to GRH*. Paper 13 (RH) bypassed it via CCM+ITPFI+Bögli+Hurwitz. Paper 26 inherits the wall.

The runner's REFRAME exposed three routes (Route 1 = spectral measure, Route 2 = CCM K-port, Option C = honest conditional) as variants of one structural move: **ascend the abstraction ladder until the vector/measure distinction disappears**. You are working on Route 1's load-bearing step.

---

## Direction — the specific task

**IMPORTANT — direction changed mid-dispatch via the runner-support-runner Q&A interface (closing-my4-questions.md Q-1 / A-1, 2026-04-11).** The original direction was "prove from scratch via Cauchy–Schwarz on `dE`." The pivot: the support runner's literature search confirms there is no published prior art for this bound in the BC corpus, but identifies **two structurally exact analogs**: (1) the KMS-modular automatic bound for Type III₁ factors, and (2) the Wegner estimate from random Schrödinger operator literature. **You are no longer inventing the proof from scratch.** You are either applying a 1-line consequence of the KMS condition (PRIMARY route) or porting a 30-year-old random-Schrödinger technique (FALLBACK route).

---

### Target lemma (unchanged)

> **Lemma (target).** *Let `T̄_{BC,K}` be the self-adjoint closure of multiplication by `log N(𝔞)` on the GNS Hilbert space `H_{1,K}`. Let `dE(λ)` be its spectral measure. Let `𝔭` be a Gaussian prime with `N(𝔭) ≥ 2`, let `P_𝔭` be the bridge projector at `𝔭`, and let `|w| := N(𝔭)^{-k/2}` for `k ∈ {2, 3, 4, 6}` (the bridge cocycle exponents). Then for every `f_0 ∈ D_K` with `‖f_0‖ = 1` and every `λ ∈ spec(T̄_{BC,K})`, the spectral-projection states*
>
> `ψ_ε^{(λ)} := E((λ - ε, λ + ε)) f_0 / ‖E((λ - ε, λ + ε)) f_0‖`
>
> *(defined whenever the denominator is nonzero) satisfy*
>
> `(ψ_ε^{(λ)}, P_𝔭 ψ_ε^{(λ)}) ≥ |w|² ‖ψ_ε^{(λ)}‖² = |w|²`
>
> *uniformly in ε > 0, with `|w| = N(𝔭)^{-k/2}`.*

---

### PRIMARY ROUTE — KMS-modular automatic bound for Type III₁ factors

**Structural claim from A-1**: The BC algebra `A_{BC,K}` at β=1 is a Type III₁ factor (Connes' classification, 1973). For such factors, the modular Hamiltonian gives a *canonical* lower bound on quadratic forms over its own spectral windows. Specifically, from the KMS condition

```
  ω_1^K(A · σ_{i/2}(A*)) ≥ 0   for every A ∈ A_{BC,K},
```

applied to `A = P_𝔭 · χ_{[E - ε, E + ε]}(T̄_{BC,K})`, you get

```
  (ψ, P_𝔭 ψ) ≥ |⟨P_𝔭⟩|² ‖ψ‖²   for every ψ in the spectral window,
```

where `⟨P_𝔭⟩ = ω_1^K(P_𝔭) = N(𝔭)^{-k/2}` is the KMS expectation of the bridge projector at the cocycle exponent `k`.

**This IS the target bound** — automatic for Type III₁, no Wegner port needed, no Cauchy–Schwarz on `dE` needed. *Conditional only on the modular compatibility check below.*

**Modular compatibility check (the load-bearing sub-task).** The above bound holds **only if** `P_𝔭` is modularly compatible with `T̄_{BC,K}`, meaning

```
  σ_t(P_𝔭) = e^{it · c_𝔭} P_𝔭
```

for some real eigenvalue `c_𝔭` under the modular automorphism. The natural value is `c_𝔭 = log N(𝔭)`, which makes `P_𝔭` a modular eigenoperator at the same frequency as the spectral parameter of `T̄_{BC,K}`. The bridge family at primes is constructed (over ℚ) precisely for this compatibility.

**Reference for the ℚ version**: `paper12/research/162` step 6 establishes the modular compatibility for the bridge projectors over ℚ. **Verify this file exists and read step 6** (file path: `/Users/gsix/quantum-geometry-in-5d-latex/paper12/research/162-*` — Glob the directory if the exact filename is uncertain). If the file doesn't exist or step 6 doesn't establish what the support runner says it does, that's a CONCERN — flag it and proceed with the K-version verification on first principles.

**Your task on the PRIMARY route**:

1. **Read** `paper12/research/162` step 6 (or the file it points to). Confirm the ℚ-version modular compatibility statement.
2. **Port to K**. Verify that the K-version bridge projectors (constructed at Gaussian primes per Paper 26 §5–§6) inherit modular compatibility from the same construction principle. The expected statement is:
   
   > For every Gaussian prime 𝔭 and every bridge cocycle exponent `k ∈ {2, 3, 4, 6}`, the bridge projector `P_𝔭^k` satisfies `σ_t(P_𝔭^k) = e^{it · log N(𝔭)} P_𝔭^k`, where `σ_t` is the modular automorphism of the GNS Hilbert space `H_{1,K}` of `ω_1^K`.
3. **If the K-port holds**: write out the 1-line KMS calculation deriving `(ψ, P_𝔭 ψ) ≥ |⟨P_𝔭⟩|² ‖ψ‖²` from the KMS condition + modular compatibility. The whole proof is ≤ 2 pages. Report ADVANCED with `p_success ≥ 0.85`.
4. **If the K-port fails** (modular compatibility doesn't transfer cleanly): name the specific obstacle and proceed to the FALLBACK route below.

---

### FALLBACK ROUTE — Wegner estimate port

If the modular compatibility check fails or is unclear, port the Wegner estimate from random Schrödinger operator literature. **Canonical reference**: Combes–Hislop 1994 *J. Funct. Anal.*, "Localization for some continuous, random Hamiltonians in d-dimensions." **Modern state-of-art**: Bourgain–Klein 2013 *Inventiones*, "Bounds on the density of states for Schrödinger operators."

**Structural map**:

| Random Schrödinger framework | BC translation |
|---|---|
| Random potential `V` | Bridge projector `P_𝔭` |
| Hamiltonian `H = -Δ + V` | `T̄_{BC,K}` (with `P_𝔭` viewed as a "perturbation" coupled to its spectral resolution) |
| Spectral window `[E - ε, E + ε]` of `H` | Spectral window `(λ - ε, λ + ε)` of `T̄_{BC,K}` |
| Wegner estimate `(ψ, V ψ) ≥ C ‖ψ‖²` for ψ in window | Target bound `(ψ_ε, P_𝔭 ψ_ε) ≥ \|w\|² ‖ψ_ε‖²` |
| Density of states `n(E)` | `(d/dλ) Tr(E_{T̄_{BC,K}}(λ)) = ζ_K(1/2 + iλ)` (up to normalization, via Weil explicit formula) |
| Smooth cutoff in `E` | Smooth cutoff in `λ` |

**Three ingredients of the Wegner proof you port**:
- (a) Spectral averaging via smooth cutoff in the spectral parameter
- (b) Wegner estimate proper (the lower bound on the perturbation)
- (c) Density-of-states bound to control the spectral window

**Estimate-not-conjecture reframing**: instead of asking "does the bound hold?", compute the explicit constant `C(N(𝔭), k)` in the Wegner estimate and check `C ≥ N(𝔭)^{-k}`. If yes, bound holds. If no, you know exactly what fails and by how much.

---

### Specific obstacle to verify first (from A-1 §6)

The Dedekind zeta `ζ_K(s)` has a simple pole at `s = 1`, which translates in the BC framework to a pole in the density of states at `λ = -i/2`. **Verify that the spectral window `[λ - ε, λ + ε]` for the relevant zeros stays bounded away from `λ = -i/2`.** The relevant zeros sit on the critical line `Re(s) = 1/2`, so their imaginary parts are real and `λ ∈ ℝ`, while `-i/2 = -0.5i` is on the imaginary axis. So the window stays bounded away. Verify explicitly in your Step 6 (Verify).

---

### What was tried (unchanged from original direction)

The original direction was "prove the bound from scratch via Cauchy–Schwarz on `dE`". This was based on the deliverable's framing in `distributional-to-genuine.md`. The runner caught the lack of cited prior art as an implicit wall and escalated to the support runner via Q-1. The support runner's answer A-1 confirmed the gap and surfaced the two structural analogs above. **You are not the first attempt at this proof — you are the redirected attempt with structural guidance.**

---

### If both PRIMARY and FALLBACK fail

If the modular compatibility check fails AND the Wegner port fails, that's a substantive negative result. Report status BLOCKED-DECOMPOSED with the failed sub-checks as new sub-nodes, and propose the failure as a candidate §F kill of pattern category `Spectral` (if Wegner-estimate-style techniques don't transfer to BC) or `Algebraic` (if the modular compatibility fails for an algebraic reason in the bridge projector construction over Gaussian primes vs. rational primes). Either way, the negative is informative — the runner uses it for the next REFRAME.

---

**Self-suspect (Step 5.5).** Before Verify, write a `## Self-suspicion` section listing 3 ways the result could be wrong:
1. Modular compatibility holds for ℚ but the K-version bridge projectors at Gaussian primes have a different modular eigenvalue (e.g., `log N(𝔭) ≠ log N(𝔭)` due to a notation collision, or the modular eigenvalue picks up a factor from the complex place at infinity).
2. The KMS condition gives a bound that is sharp in ε but too weak (e.g., `≥ |w|² · (1 - O(ε))` instead of `≥ |w|²` exactly), which would still close MY4 in the limit but not pointwise in ε.
3. The Wegner port has a constant `C(N(𝔭), k)` that depends on `k` differently than the bridge cocycle expects — e.g., Wegner gives `C = N(𝔭)^{-2k}` (too small) instead of `N(𝔭)^{-k}`.

Address each with either inline resolution or a CONCERN note.

---

## §D toolkit rows you should cite by canonical name

- `T̄_{BC,K}` — self-adjoint closure of `L_K f(𝔞) = log N(𝔞) f(𝔞)` on `H_{1,K}`
- `A_{BC,K}` — Ha–Paugam BC C*-algebra over K (Type III₁ factor at β=1, Connes 1973 classification)
- `ω_1^K` — unique KMS₁ state, with modular automorphism `σ_t(e_𝔞) = N(𝔞)^{it} e_𝔞`
- `H_{1,K}` — GNS Hilbert space of `ω_1^K`, type III₁ factor
- `P_𝔭` — bridge projector at prime ideal 𝔭
- `Dark-state bound (point spectrum)` — `‖P_𝔭 ψ‖² ≥ |w|² ‖ψ‖²` for genuine point-spectrum eigenvector ψ, `|w| = N(𝔭)^{-k/2}` (Paper 26 §5d, status R)
- `Dark-state bound (spectral-measure form)` — *the target of this node*, status S → R if proved
- `KMS-modular dark-state bound` — *the PRIMARY ROUTE structural identity*, automatic for Type III₁ + modular compatibility
- `Modular compatibility check` — verify `σ_t(P_𝔭) = e^{it · log N(𝔭)} P_𝔭` for K-version bridge projectors
- `Wegner estimate (random Schrödinger)` — *the FALLBACK ROUTE structural template*, Combes–Hislop 1994 / Bourgain–Klein 2013
- `Density of states for T̄_{BC,K}` — `(d/dλ) Tr(E(λ)) = ζ_K(1/2 + iλ)` via Weil explicit formula; pole at `λ = -i/2` (bounded away from real `λ`)
- `Spectral measure dE(λ)` — `T̄_{BC,K} = ∫_ℝ λ dE(λ)` (Reed–Simon II Chapter VIII, status R)
- `Approximate eigenvector ψ_ε^{(λ)}` — `E((λ - ε, λ + ε)) f_0 / ‖...‖` (Route 1 construction, status S)
- `Key Lemma C` — `|Δc(δ)| < 1/(k+1) < 1/k` (research/cohomology-class-lemma.md, status R) — you cite this, you do not re-prove it
- `Bridge rows` — the four `(k, N)` pairs `(2, 13), (3, 13), (4, 41), (6, 29)` from research/corrected-bridge-table.md

---

## Primary sources to consult (read selectively, ≤8K tokens)

**Highest priority (PRIMARY route)**:

- `/Users/gsix/quantum-geometry-in-5d-latex/paper12/research/162-*` — Glob the directory for the exact filename containing step 6 (modular compatibility for ℚ-version bridge projectors). This is the structural template you port.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4-questions.md` — read Q-1 / A-1 for the support runner's full structural guidance, especially A-1 §3 (KMS-modular route) and §6 (density-of-states obstruction check).
- Connes 1973 Type III classification + Tomita–Takesaki theory background — you don't need to read the original; cite for the "Type III₁ → modular Hamiltonian gives canonical lower bound" structural fact.

**Medium priority (the deliverable's original framing)**:

- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/research/distributional-to-genuine.md` — Route 1 sketch (note: it does NOT mention KMS-modular or Wegner; the support runner's pivot supersedes it as the actual approach)
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/research/cohomology-class-lemma.md` — Key Lemma C statement (you cite, do not re-prove)
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/research/corrected-bridge-table.md` — the four bridge rows

**Lower priority (FALLBACK route reference)**:

- Combes & Hislop 1994 *J. Funct. Anal.* — Wegner estimate canonical paper. Likely accessible via WebFetch on the journal page; if not, cite from the support runner's description in A-1 §2.
- Bourgain & Klein 2013 *Inventiones* — modern Wegner state-of-art. Same fallback for access.
- Reed–Simon *Methods of Modern Mathematical Physics IV*, §XIII.16 (abstract spectral averaging) — cite if used.

Do NOT read the full Paper 26 preprint, the full route2-ccm-over-K.md, or the full meyer-extension-to-K.md. Those are for the runner / other Authors.

---

## §F kill list (rows in pattern categories relevant to your claim)

Empty. This is cycle 1; no kills logged yet. Do not skip the §F shadow check just because §F is empty — explicitly note "no §F shadow" in your output.

---

## The 6-step inner method loop (per `01-the-prompt.md §7`)

Execute in order:

1. **DIAGNOSE**: state in one sentence: "the reason the dark-state bound is hard at the spectral-measure level is X; the phenomenon in a fuller description is Y."
2. **REINTERPRET**: find a representation where the bound becomes obvious. Spectral-theorem language is the obvious candidate but verify it.
3. **UNIFY**: cite the §D toolkit row(s) used. If a new pattern emerges, propose a new §D row.
4. **LOCK**: identify the invariant that protects the bound. Likely: (a) the explicit form of `P_𝔭` as a polynomial in `T̄_{BC,K}`, OR (b) `[P_𝔭, E(I)] = 0` exactly, OR (c) `‖[P_𝔭, E(I)]‖ = O(ε)` and the error is absorbable. Which one (or which decomposition) protects your proof?
5. **COMPUTE**: execute the calculation. If a numerical sanity check is feasible (e.g., for the four bridge rows at small ε), include `code/M.1.1-verify-spectral-measure.py` declaring `mp.dps` and pasting raw output. If purely analytic, skip Compute and proceed to Verify.
6. **VERIFY**: verify the proof's correctness. Precision-floor rule: if numerical, headline at least 3 orders of magnitude above floor.

**Step 5.5 Self-suspect** (between 5 and 6): write the 3-failure-modes section before Verify.

Report **WHERE you got stuck** if you don't close. "Stuck at Reinterpret because no internal toolkit element bypasses [named wall]" is strictly more informative than "BLOCKED."

---

## Output schema (write to `nodes/M.1.1.md`)

```markdown
# M.1.1 — Spectral-measure dark-state bound

*Author: Claude Opus 4.6 (W1-A)*
*Cycle: 1*
*Status: ADVANCED | BLOCKED | BLOCKED-DECOMPOSED | KILLED*
*Generative step: [which of Diagnose/Reinterpret/Unify/Lock/Compute/Verify]*
*Stuck at (if not closed): [step + reason]*

---

## Direction (verbatim from prompt)

[Copy the Direction section from the prompt]

---

## Research

### Step 1 — DIAGNOSE
[1 sentence + brief explanation]

### Step 2 — REINTERPRET
[representation, references]

### Step 3 — UNIFY
[§D rows cited; new §D row proposed if any]

### Step 4 — LOCK
[invariant; if decomposition, list sub-requirements]

### Step 5 — COMPUTE
[calculation or analytic argument; declare mp.dps if numerical]

### Step 5.5 — Self-suspicion
1. [failure mode 1 + resolution or CONCERN]
2. [failure mode 2 + resolution or CONCERN]
3. [failure mode 3 + resolution or CONCERN]

### Step 6 — VERIFY
[verification; conclusion or BLOCKED reason]

---

## Proposed §D toolkit additions (if any)

[List any new canonical names with full §D row format]

---

## Tagged notes for §I (CONCERN / CASCADE / LESSON / CALLOUT)

[Append-only entries]

---

## What the next runner needs to know (Sig 11 schema)

- **State at handoff**: [1 sentence]
- **Open dependencies**: [§G nodes this depends on or is depended on by]
- **Watch out for**: [traps or paraphrase-prone constructs]
- **Preferred next move**: [1 sentence]
- **Voice canon citation**: [which §J quote or signature is most relevant for continuation]
```

---

## Status report (return to runner, ≤300 words)

After writing your output file, return a brief status report containing:

1. Status verdict (ADVANCED / BLOCKED / BLOCKED-DECOMPOSED / KILLED)
2. Which 6-step loop step was generative
3. Which step you got stuck on (if not closed)
4. Key §D additions you propose
5. CONCERN / CASCADE / LESSON notes you appended to §I
6. p_success self-estimate (0–1)

The runner uses your status report to decide Critic dispatch and to update §G live nodes. The full work product is the `nodes/M.1.1.md` file.

---

## Constraints

- **Do NOT modify the blackboard.** You write only to `nodes/M.1.1.md` and `code/M.1.1-*.py` if numerical work is needed. The runner updates §D / §G / §M / §N / §O.
- **Do NOT spawn other agents.** Authors do not dispatch primitives.
- **Do NOT skim primary sources.** Read the cited sections carefully. Reed–Simon Chapter VIII is short and dense; budget the time.
- **Do honest partial proof over glossed completion.** A 7/10 proof with a named GENUINE gap is better than a 9/10 proof with a hidden CLOSABLE gap. The gap is the learning signal.
- **Do not paraphrase Key Lemma C** or any cited theorem — quote it verbatim or cite by canonical name + reference. Paraphrase is how drift enters.
- **Do not declare success at COMPUTE without VERIFY.** The verify step is mandatory.
