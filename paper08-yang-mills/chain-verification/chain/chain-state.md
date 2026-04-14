# Chain State — Yang-Mills Mass Gap Proof Chain

**Programme:** Paper 8 YM mass-gap proof (Clay Millennium Problem)
**Source:** `preprint/PROOF-CHAIN.md §IV.1`
**Last updated:** 2026-04-13 (post-Wave 1)

---

## Link table (19 proved links + Link 18 CONDITIONAL)

| Link | Statement (abbrev) | Domain | Status | Confidence | Blocker | Last wave |
|:-----|:--------------------|:-------|:-------|:-----------|:--------|:----------|
| 1 | KK spectral gap Δ₀^KK > 0 (Thm 4) | SPEC+QFT | **WEAKENED** | 7/10 | r₃ modulus + C₀ + Seiler adjoint | W1 |
| 1b | IR equivalence Δ₀^std > 0 (Thm 5) | SPEC+QFT | **VERIFIED** | 9/10 | (minor L-uniform scope note) | W1 |
| 2 | UV stability (Balaban) | GEOM+QFT | **WEAKENED** | 7/10 | KK-correction domain check; missing verification report; CMP 119 pin | W1 |
| 3 | Polymer convergence, κ k-indep | GEOM+QFT | **VERIFIED** | 9/10 | — | W1 |
| 4 | (B1): analyticity, k-indep radius | QFT+analysis | **WEAKENED** | 8/10 | saddle-point center condition (one-sentence CMP 109 §3 citation) | W1 |
| 5 | (B2): SL(N,ℂ) extension | GEOM | **VERIFIED** | 9/10 | — | W1 |
| 6 | 𝒞-elimination of Tr(F³) | algebraic | **VERIFIED** | 10/10 | — | W1 |
| 7 | Newton decomposition: n ≥ 2 survives | algebraic | **BROKEN** | 3/10 | ghost link: no proof body; App G repudiates; logical content already in L6+L8-9 | W1 |
| 8 | dev(Tr(DF)²) ≥ 2 | algebraic | **VERIFIED** | 9/10 | — | W1 |
| 9 | Dim-6 classification: all ops dev ≥ 2 | algebraic+symmetry | **VERIFIED** | 9/10 | — | W1 |
| 10 | dev(δE_k^{d=6}) ≥ 2 non-pert | SPEC+QFT | **VERIFIED** | 9/10 | — | W1 |
| 10b | Spectral lemma C_p k-independent | SPEC | **VERIFIED** | 8/10 | (annotated: Lieb-Robinson velocity bound uncited) | W1 |
| 11 | C_new g_k^4 Δ̂² bound | SPEC+QFT | **WEAKENED** | 7/10 | internal inconsistency §5.5.5↔§IV.1; N-dep unquantified | W1 |
| 12 | RG recursion | QFT+iterative | **VERIFIED** | 9/10 | (cosmetic: "bounded fixed point" → "bounded orbit" wording) | W1 |
| 13 | Σ C_k g_k^4 Δ̂_k² < ∞ | analysis | **VERIFIED** | 9/10 | — | W1 |
| 14 | **Δ_∞ > 0 (the mass gap)** | SPEC+QFT | **WEAKENED** | 7/10 | **headline:** 3-way contradiction on Conjecture 1 status; polymer-sum spectral lemma gap | W1 |
| 15 | Gradient-flow well-posedness (§L.1) | QFT+SPEC | **VERIFIED** | 9/10 | (residual: two-line max-principle conditions) | W1 |
| 16 | Continuum flowed Schwinger (§L.2) | QFT+SPEC | **WEAKENED** | 8/10 | OS axiom numbering conflict §5.7↔§L.2 | W1 |
| 17 | [Tr F²]_R + T_μν (§§L.3-L.4) | QFT+SPEC | **VERIFIED** | 9/10 | **L.3.7 audit resolved: zero H4 dependency** | W1 |
| 18 | AF match + OPE (§L.4) | QFT+SPEC+ANT | CONDITIONAL | 8/10 | H4 (external; not attempted per brief §2.3) | — |

---

## Wave 1 summary

**Dispatched:** 19 Critics on 19 proved links (forward + backward fronts merged; parallel wave).

**Returns:**
- **VERIFIED (12):** 1b, 3, 5, 6, 8, 9, 10, 10b, 12, 13, 15, 17
- **WEAKENED (6):** 1, 2, 4, 11, 14, 16
- **BROKEN (1):** 7

**Headline findings:**
1. **Link 14 (the mass gap itself) WEAKENED.** Theorem 8 is titled "Conditional continuum mass gap" and begins "Assume Conjecture 1 holds," while the §5.4.7 status table declares Conjecture 1 "Proved (Section 5.6)" and line 1035 simultaneously says "The remaining problem is Conjecture 1." The §5.6 discharge is for single operators of bounded temporal support, but Balaban's operators are polymer-cluster sums of support |X| — the spectral lemma needs the summed-over-polymers version (absorbing |X|^p via e^{-κ|X|}), not the single-operator bound. **This is the highest-priority repair.**
2. **Link 7 (Newton decomposition) BROKEN.** Ghost link: no proof body in preprint; Appendix G explicitly proves the Newton decomposition is the *wrong* tool for extracting Δ̂ factors. Logical content of "n ≥ 2 survives" is already fully accomplished by Link 6 (𝒞-elimination of cubic operators) + Links 8-9 (spectral classification for dim-6+). **Repair: collapse Link 7 into Link 6 as a note, remove as standalone step.**
3. **Link 17 L.3.7 audit CLOSED.** Zero H4 dependency found. Resolves the "17/18 → 18/18 pending L.3.7 audit" flag from the prior YM H4 bypass session (2026-04-13 memory).
4. **Five other WEAKENED links (1, 2, 4, 11, 16) all have short cited repairs** — domain-tracking sentences, cross-reference fixes, explicit hypothesis statements. No bypass required; each closable in construct mode.

---

## Bidirectional front state (post-W1)

- **Forward front:** Walking from Link 1 forward while VERIFIED or BYPASSED:
  - Link 1 is WEAKENED → **F = 0** (forward front blocked at Link 1).
- **Backward front:** Walking from Link 17 backward while VERIFIED or BYPASSED:
  - Link 17 VERIFIED → 16 WEAKENED → **B = 17** (backward front blocked at Link 16).
- **Gap:** Links 1-16 need Wave 2 repair/verify before chain closes.
- **Key intermediate islands of VERIFIED links:** {3, 5, 6, 8, 9, 10, 10b, 12, 13, 15}.

**Junction not yet reached.** Wave 2 must repair the 6 WEAKENED links and bypass/collapse the 1 BROKEN link before forward and backward fronts can merge.

---

## Wave 2 plan (next cycle)

Dispatch 7 parallel construct/repair Authors:
- **L1 repair:** state r₃-stabilization hypothesis; compute C₀(N); cite Seiler for adjoint bound
- **L2 repair:** verify KK corrections stay inside Balaban inductive domain (~1-2 pages new math); re-path verification report; pin CMP 119 theorem reference
- **L4 repair:** one-sentence CMP 109 §3 citation for saddle-point center condition
- **L7 collapse:** rewrite PROOF-CHAIN IV.1 to remove standalone Link 7; note that n ≥ 2 survival follows from L6 + L8-9
- **L11 repair:** reconcile §5.5.5 vs §IV.1 status; quantify N-dependence ζ(R₀, N)
- **L14 repair (HIGHEST PRIORITY):** resolve 3-way Conjecture 1 contradiction; establish polymer-sum spectral lemma (summed-over-polymers version)
- **L16 repair:** add OS-axiom-convention declaration at top of §L.2; update lines 1218, 1239 cross-references

After Wave 2 returns, dispatch Wave 3 Critics to verify each repair. Junction detection every cycle-close.

---

## Status legend

- **OPEN** — not yet adversarially attacked
- **IN_PROGRESS** — Critic/Author dispatched
- **VERIFIED** — Critic returned SURVIVED
- **WEAKENED** — Critic found repairable gap; construct pending or underway
- **BROKEN** — Critic found fatal gap; construct/bypass/collapse pending
- **BYPASSED** — replaced by alternate path via capacitor
- **CONDITIONAL** — depends on named external hypothesis
- **HONEST-STALL** — stuck, no bypass; wall named

---

## Wave log

**Wave 1 (complete, 2026-04-13):** 19 Critics parallel, Sonnet 4.6 max effort per PCA §P.7. 12 VERIFIED / 6 WEAKENED / 1 BROKEN / 0 HONEST-STALL. Verdicts in `critiques/link-*-critic.md`.

**Wave 2 (planned):** 7 Authors parallel (L1, L2, L4, L7, L11, L14, L16). Opus 4.6 max effort for L14 (headline bottleneck); Sonnet medium for other 6 assembly-mode repairs.
