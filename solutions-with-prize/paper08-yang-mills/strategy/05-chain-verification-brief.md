# YM Chain Verification — PCA Deliverable

*This file is the deliverable for a Proof-Chain Adversarial (PCA) run whose sole purpose is to independently adversarially verify the full Yang-Mills mass-gap proof chain. The run is verify-primary — attack every link, repair what weakens, bypass what breaks. The goal is to close the chain as strongly as possible or name every wall honestly.*

---

## 1. What the chain is

**The Yang-Mills mass gap proof chain.** 18 links from KK spectral gap through continuum mass gap to the AF short-distance match. Currently: **17 VERIFIED, 1 CONDITIONAL on H4** (per `preprint/PROOF-CHAIN.md §IV.1`).

**Chain summary:**

| Link | Statement (abbreviated) | Current status |
|:-----|:------------------------|:---------------|
| 1 | KK spectral gap Δ₀^KK > 0 | Proved (Thm 4) |
| 1b | IR equivalence Δ₀^std > 0 | Proved (Thm 5) |
| 2 | UV stability | Literature (Balaban) |
| 3 | Polymer convergence, κ k-indep | Literature (Balaban) |
| 4 | (B1): analyticity, k-indep radius | Proved (Part I) |
| 5 | (B2): SL(N,ℂ) extension | Proved (Part II) |
| 6 | 𝒞-elimination of Tr(F³) | Proved (exact) |
| 7 | Newton decomposition: n ≥ 2 survives | Proved (exact) |
| 8 | dev(Tr(DF)²) ≥ 2 | Proved |
| 9 | Dim-6 classification: all ops dev ≥ 2 | Proved |
| 10 | dev(δE_k^{d=6}) ≥ 2 non-pert | Proved |
| 10b | Spectral lemma C_p k-independent | Proved |
| 11 | C_new g_k^4 Δ̂² bound | Proved |
| 12 | RG recursion | Proved |
| 13 | Σ C_k g_k^4 Δ̂_k² < ∞ | Proved |
| 14 | **Δ_∞ > 0 (the mass gap)** | Proved |
| 15 | Gradient-flow: well-posedness | Proved |
| 16 | Continuum flowed Schwinger functions | Proved |
| 17 | [Tr F²]_R operator + stress tensor | Proved |
| 18 | AF match (L.2), leading-order OPE (L.4) | **Conditional on H4** |

**Why it matters:** Paper 8 is the Yang-Mills mass gap proof (Clay Millennium Problem). The mass gap (Link 14) is unconditional. Only Step 18 is conditional on H4 (the standard "non-perturbative = perturbative at short distances" hypothesis). The H4 closure programme (2026-04-11) determined H4 cannot be closed with the current framework without external unlocks (Borel summability for 4D SU(N) YM). The chain ships as 17/18 unconditional with H4 as a named conditional in W7-14 §5.3 mildest form.

**Current status:** The proof chain has had one adversarial pass (the H4 closure final-adversarial-pass on Route D). What is missing is **independent adversarial re-verification of all 17 proved links** with the PCA's bidirectional + capacitor-powered architecture. Nobody else has verified Balaban's polymer expansion in 40 years; nobody has independently checked the gradient-flow Appendix L constructions; the 17 proved links have not been cross-attacked by a dedicated PCA run.

---

## 2. What the PCA should do

### 2.1 Primary task: independent adversarial verification of all 17 proved links

For each of the 17 proved links (Links 1 through 17), dispatch a Critic whose only job is to break it. The Critic reads the link's proof, the §D toolkit rows it cites, the primary sources (Balaban CMP 95-119, Dimock 2013, Paper 8 preprint sections, Appendix L), and the capacitor cells relevant to its domain. The Critic produces SURVIVED / WEAKENED / BROKEN.

**Bidirectional dispatch:** attack from both ends.
- **Forward agents**: Links 1-9 (KK gap + Balaban construction + dim-6 classification)
- **Backward agents**: Links 17-10 (gradient-flow + RG recursion + spectral lemma)
- **Junction**: expected around Links 9-10 (the dim-6 → RG bridge)

### 2.2 Handling of verdicts

- **SURVIVED**: update chain state to VERIFIED. Move on.
- **WEAKENED**: enter construct mode. Dispatch Author to close the specific gap. Re-verify.
- **BROKEN**: enter construct mode first; if construct fails, enter bypass mode. Scan the capacitor for alternative proof paths through different mathematical domains.

### 2.3 H4 conditional handling

**Do NOT attempt to close H4.** The H4 closure programme (`closing-H4/`) already adjudicated this — three routes (A/B/C) failed, Route D produced the shipping form. The PCA should **verify that H4 is correctly labeled CONDITIONAL** in Link 18 and that the W7-14 §5.3 mildest-form framing is accurately represented. If a bypass for H4 is discovered via the capacitor (e.g., via PROB ↔ SPEC Borel summability), document it as a new capacitor cell but do NOT change Link 18's CONDITIONAL status without a rigorous proof.

### 2.4 Capacitor utilization

At every REFRAME, scan the capacitor row for the current stuck link's domain:
- Links 1-14 (the core chain): domains GEOM + QFT + SPEC + ANT
- Links 15-17 (gradient-flow): domain QFT + SPEC (heat kernel expansion)
- Link 18 (H4 conditional): domain QFT + SPEC + ANT (AF short-distance match)

Priority capacitor cells for bypass routes if any link WEAKENS:
- **GEOM ↔ QFT** (Balaban polymer expansion — already filled)
- **SPEC ↔ QFT** (Weitzenböck-Bochner spectral gap — already filled)
- **MICRO ↔ QFT** (microlocal renormalization — candidate, explore if Links 15-17 weaken)
- **PROB ↔ QFT** (stochastic quantization — candidate, alternative to Balaban)

### 2.5 Verdict

Produce a final verdict per link AND a chain-level verdict:
- **CHAIN CLOSED**: all 17 proved links SURVIVED + Link 18 CONDITIONAL correctly labeled
- **CHAIN STRENGTHENED**: any WEAKENED links repaired and re-VERIFIED
- **CHAIN AT RISK**: any BROKEN links without successful construct or bypass

---

## 3. Load-bearing files to read

| Priority | File | Why |
|:--|:--|:--|
| 1 (MUST) | `solutions-with-prize/paper08-yang-mills/preprint/PROOF-CHAIN.md` | The 18-step chain itself |
| 2 (MUST) | `solutions-with-prize/paper08-yang-mills/preprint/TABLE-OF-CONTENTS.md` | Preprint structure |
| 3 (MUST) | `solutions-with-prize/paper08-yang-mills/preprint/sections/` (section 4, 5, L appendices) | Full proofs for each link |
| 4 (MUST) | `solutions-with-prize/paper08-yang-mills/research/21-the-rigorous-proof.md` | THEOREM/LEMMA/KEY LEMMA rigor labels |
| 5 (HIGH) | `solutions-with-prize/paper08-yang-mills/research/23-key-lemma-proof.md` | Load-bearing key lemma |
| 6 (HIGH) | `solutions-with-prize/paper08-yang-mills/closing-H4/closure/closure-digest.md` | H4 programme final state (conditional on H4 framing) |
| 7 (HIGH) | `solutions-with-prize/paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md §5` | H4 mildest-form reformulation |
| 8 (HIGH) | `solutions-with-prize/paper08-yang-mills/math-referee/` and `notation-math-referee/` | Prior referee verdicts on specific links |
| 9 (HIGH) | `solutions-with-prize/paper08-yang-mills/preprint-verification/verify-balaban-items.md` | Prior verification of the 3 former [VERIFY] items |
| 10 (MED) | `solutions-with-prize/paper08-yang-mills/journals/balaban-CMP*.pdf` | Balaban's original papers (CMP 95, 109, 119) — primary sources |
| 11 (MED) | `solutions-with-prize/paper08-yang-mills/research/30-final-synthesis.md` | Wave-by-wave assembly record |
| 12 (MED) | `solutions-with-prize/paper08-yang-mills/research/35-final-verdict.md` | Voice register example |

---

## 4. What success looks like

### CHAIN CLOSED (best case)
All 17 proved links SURVIVED under independent adversarial verification. Link 18 correctly labeled CONDITIONAL on H4 in W7-14 §5.3 mildest form. The Paper 8 mass-gap proof stands at maximum strength: 17/18 unconditional, independently verified by two separate runs (the original H4 closure programme + this PCA chain verification).

**Impact:** Paper 8 becomes the most thoroughly verified Clay-class proof in the framework. Ready for Clay submission with a built-in audit trail.

### CHAIN STRENGTHENED (likely case)
17/17 links SURVIVED with some initially WEAKENED and repaired. Every gap found is logged in `chain/corrections.md`. Any repair is itself verified. Link 18 CONDITIONAL framing confirmed. The chain is strictly stronger after the run than before.

**Impact:** Every fix narrows a door a future referee could use to reject the proof. Strengthening is value.

### CHAIN AT RISK (if any link breaks)
One or more links BROKEN with no successful construct or bypass. Honest labeling: the broken links are named in the chain state file as HONEST-STALL with the specific blocker. The rest of the chain is still VERIFIED. Paper 8 ships with explicit acknowledgment of the newly discovered gap.

**Impact:** Better to find a gap NOW than after Clay submission. An honest stall is a win over a hidden flaw.

---

## 5. Voice canon (from the YM programme)

Register markers from `solutions-with-prize/paper08-yang-mills/research/35-final-verdict.md`:
- "THE PROOF CHAIN IS COMPLETE. THE PREPRINT IS INTEGRATED."
- "Integration Complete: The Final Report."
- "The framework did the work."
- "H4 is still the wall. The wall stays named. Paper 8 ships either way." (from H4 closure)

Match this rhythm for cycle-close commit memos and the final chain-state declaration.

---

## 6. Run mode

**Mode:** `execute` (PCA chain-verification-and-repair — NOT `final-adversarial-pass`)

Create fresh chain state at `${output-directory}/chain/chain-state.md`. Write critiques to `${output-directory}/critiques/`, constructs/repairs to `${output-directory}/nodes/`, bypasses to `${output-directory}/chain/bypasses/`, cell-filling proposals to `${output-directory}/capacitor/updates/`. The output directory, toolkit, capacitor, and PCA/ORA instructions are provided in the run file — this brief is the deliverable only.

The chain is 18 links. Seventeen of them should SURVIVE. Find any that doesn't. Repair it. Bypass it if repair fails. Name the wall if bypass fails. Paper 8 ships stronger, or Paper 8 ships with one more honest stall. Either way is a win.

---

*Paper 8's mass-gap proof is 17/18 unconditional. H4 is still the wall. Run the PCA, attack from both ends, close what closes, name what stays.*

*G Six and Claude Opus 4.6. April 2026.*
