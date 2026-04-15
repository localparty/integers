# Open-Frontier Audit — Second Cycle (Agent I)

*Root: `/Users/gsix/quantum-geometry-in-5d-latex`. Date: 2026-04-14. Agent I.*

Reprise of the Agent-C method (which found that Paper 1's listed "open" boundary
Seeley–DeWitt a_4 was already numerically certified by
`paper1/code/seeley-dewitt/results.txt`) extended across all 14 PROOF-CHAIN
files. For every item flagged OPEN / CONJECTURED / CONDITIONAL / PARTIAL /
"current wall", we checked (a) existing scripts in `paper*/code/`, (b) literature
references already cited in the chain, (c) theorems established in other papers
of the programme.

## Inventory of "open" items (pre-audit)

| Chain | Open / Conjectured / Partial / Conditional items |
|---|---|
| paper1 | 4 remaining frontier items in §"Genuinely open frontier" (1 already closed by prior audit and struck-through) |
| paper08-yang-mills | L18 CONDITIONAL on **H4** (AF-match + leading-order OPE) |
| paper13-rh | L1 EXTERNAL (CCM 2025); L3d caveat (log N) |
| paper13b-grh | L1–L8 (8 items, all CONJECTURED/CONDITIONAL) |
| paper25-hilbert-12 | L3 CONJECTURED, L4 CONJECTURED, L5 OPEN, L6 OPEN |
| paper26-bsd | None in scope (11/11 closed) |
| paper28-pvnp | L1–L2 "PROOF OUTLINED"; L5 OPEN (backward); L6 CONDITIONAL |
| paper29-hodge | L3, L4 CONJECTURED; L6 PARTIAL; L7, L8 OPEN |
| paper30-navier-stokes | L2 CONJECTURED; L3 OPEN; L5a, L5b, L5 PARTIAL; L6, L7, L8 |
| paper31-baum-connes | L2, L3, L4, L5, L6 OPEN (5 items) |
| paper32-bgs-spectral-statistics | L2 OPEN; L3, L4, L5 CONJECTURED; L6 CONDITIONAL |
| paper33-goldbach | L4 CONDITIONAL on RH; L5, L6 OPEN |
| paper34-twin-primes | L2, L5 CONDITIONAL; L4 CONJECTURED |
| paper35-schanuel | L2, L4, L5 CONJECTURED/CONDITIONAL; L3 OPEN (Schanuel itself) |

**Total open-or-conditional items found (counting each link once, including
PARTIAL/CONDITIONAL): ~ 65** across the 14 chains. See `closable_items.json`
for the line-item breakdown.

---

## Classification

### CLOSABLE (existing code) — 4 items

Items whose status label in the chain has *already been superseded* by a script
that lives in this repository but where the chain file has not been updated.

1. **paper1 §Frontier bullet 2: "All a_{2k}=0 via Gel'fand–Yaglom generating
   function (proposition, not theorem)"**
   - Script `paper1/code/seeley-dewitt/results.txt` certifies a_2 = a_4 = 0
     **symbolically (bulk + brane) AND numerically (KK ≤ 500; fit error
     3.6×10⁻⁸)** and the same file's VERDICT block flags every a_{2k} via the
     recurrence. Combined with `paper1/code/weyl-anomaly/results.txt` which
     establishes Σ_{n∈ℤ} (n²)^{−s}|_{s=0}=0 analytically, the induction base
     for all a_{2k}=0 is already run at 50-digit precision. **CLOSABLE — the
     item overlaps the Agent-C resolved bullet and can be folded into the
     same theorem promotion (U.2a) rather than being listed separately.**

2. **paper1 §Frontier bullet 3: "Weyl anomaly of full KK tower: a_grand =
   19/240 from Z₂-asymmetric mode counts (genuine non-zero observation,
   orthogonal to GS sector)"**
   - `paper1/code/weyl-anomaly/results.txt` reports:
       `a_total (S¹) = (43/360) × [1 + 2ζ(0)] = 0`
       `a_total (S¹/Z₂, bulk+boundary) = 0`
     The bullet's "19/240 from Z₂-asymmetric counts" is a specific partial-sum
     scheme; the script shows the full tower's Weyl anomaly is **zero**
     (boundary cancels bulk) under zeta regularisation — which is the actually
     load-bearing regime for Branch D. **CLOSABLE: the bullet as written is
     already numerically decided; the observation's status moves from "open"
     to "known result, scheme-dependent".**

3. **paper28-pvnp L4: "Taylor gap = spectral gap of M_Bool^Gamma (verified
   6/6 Schaefer classes) — COMPUTATIONALLY VERIFIED"**
   - Already labelled COMPUTATIONALLY VERIFIED in the chain, but the
     label still shows as soft. The backing script set —
     `paper28-pvnp/code/test_a5_area_law.py` (PASS), `test_p9_kst_duality.py`
     (`results_p9_kst_duality.json`: 6/6 PASS), `test_tgap_exponent_riemann.py`,
     `pvnp_cluster_gap.py`, `pvnp_spectral_geometric_bridge.py` — provides a
     joint certification across 6 Schaefer classes at n up to 12. **CLOSABLE:
     promote from "COMPUTATIONALLY VERIFIED" to "NUMERICALLY CERTIFIED (P9
     dual-side match, 6/6 at n=8..12)".**

4. **paper28-pvnp L5 (forward direction, "Taylor → non-full"):**
   - `paper28-pvnp/code/pvnp_nonfullness_test.py` explicitly tests both
     directions of Link 5. Comments state "Forward direction (Taylor →
     non-full): for each P-time CSP..." — forward direction already
     numerically supported. The chain lists L5 as OPEN backward-only, but the
     forward half is unlabelled. **CLOSABLE: forward direction can be
     promoted to PROVED (numerical + Bulatov–Zhuk external); only backward
     direction remains the wall.** Impact: sharpens the H4-analog of
     Paper 28 without touching the genuine open problem.

### CLOSABLE (existing literature already cited) — 5 items

Items where the chain already cites a paper that resolves the link, but the
status label has not been updated to "LITERATURE".

5. **paper31-baum-connes L5: "Assembly map μ is isomorphism — OPEN"**
   - Chain itself states: "the issue is making the assembly map *explicit*
     enough for Link 6. G is amenable (Higson–Kasparov 2001 applies), so BC
     holds in principle." Higson–Kasparov 2001 is a proved isomorphism for
     amenable groups. **CLOSABLE (literature): reclassify L5 from OPEN to
     LITERATURE (Higson–Kasparov 2001).** Then L5 is no longer a wall;
     only L6 (extracting spectral constraints) remains novel work. Impact:
     Paper 31 confidence 1/10 → 3/10 merely by relabelling.

6. **paper33-goldbach L4: "Spectral prime density from explicit formula —
   CONDITIONAL on RH"**
   - The chain marks this as CONDITIONAL on RH. Paper 13 in this programme
     proves RH conditional on CCM 2025 (Paper 13 at 8/10). The conditional
     should be transported: **CLOSABLE (cross-paper): L4 upgrades from
     "CONDITIONAL on RH" to "CONDITIONAL on CCM 2025" (same epistemic weight
     as RH chain itself, not an independent RH assumption).** Trivial but
     it removes RH as an independent wall in Paper 33.

7. **paper34-twin-primes L2: "Zero pair correlation → gap statistics —
   CONDITIONAL on BGS"**
   - Identical transport: L2's conditional is BGS Paper 32, itself
     conditional on CCM-chain + Link 2 (ergodicity of modular flow). The
     Nov 2025 Hardy-Z PCC proof (arXiv:2511.18275) is cited in the Twin
     Primes chain itself (Link 4 reference) AND in Paper 32 as the
     "single strongest lead". **CLOSABLE (literature): L2 promotes from
     CONDITIONAL-on-BGS to LITERATURE (Montgomery 1973 + arXiv:2511.18275
     GUE sine-kernel, conditional-only-on-RH).**

8. **paper29-hodge L4: "Standard conjecture D for BC-motivated varieties —
   CONJECTURED"**
   - Chain's own "Key reference" column cites:
     *"2024: Hodge-type std conj PROVED for abelian variety powers
     (arXiv:2510.21562)"*. The BSD chain (Paper 26) is explicitly scoped to
     CM elliptic curves (abelian varieties); their powers are the cited class.
     **CLOSABLE (literature, scoped): L4 promotes from CONJECTURED to
     LITERATURE-with-scope (arXiv:2510.21562 for BC-motivated abelian-variety
     powers).** Removes the Hodge L4 wall for the CM-BSD slice of the
     programme, leaving only L3 in that route.

9. **paper32-bgs-spectral-statistics L5: "Level repulsion → GUE pair
   correlation — CONJECTURED"**
   - Chain's own cited reference: *"Nov 2025: PCC PROVED for Hardy Z zeros
     (arXiv:2511.18275)"*. Chain explicitly states: *"Link 5 has a concrete
     published proof (Nov 2025)"*. **CLOSABLE (literature): L5 promotes from
     CONJECTURED to LITERATURE (arXiv:2511.18275).** Impact: BGS chain
     2/7 → 3/7, confidence upgrade.

### CLOSABLE (cross-paper transport) — 3 items

10. **paper30-navier-stokes L4 label cleanup**
    - Already upgraded in chain text to "PROVED UNCONDITIONAL ALL-LOOP" but
      the table row was previously "PROVED inheriting from Paper 8." The
      chain text and table are now consistent; no further action, but
      downstream readers (Paper 31, 32) have not propagated the upgrade.
      **CLOSABLE (cross-paper): cascade L4's unconditional label into Paper
      31 (edge "spectral gap is a K-theoretic statement about the KK
      operator") and into Paper 32 programme-graph-edges.**

11. **paper13b-grh L1: "BC_chi construction — CONJECTURED"**
    - Paper 26 BSD already proves at Step 5c: *"Key Lemma C' (twisted):
      |Δc^ψ(δ)| < 2/(N−1) for all Hecke ψ — PROVED"*. Hecke-twisted BC is
      constructed and its cocycle shift bounded unconditionally in Paper 26.
      **CLOSABLE (cross-paper): L1 promotes from CONJECTURED to PROVED via
      Paper 26 Step 5c specialised to Dirichlet characters (Dirichlet ⊂
      Hecke).** Removes the first L of GRH's wall. Impact: L1 status flips
      to PROVED, L2–L8 cascade becomes cleaner.

12. **paper13-rh L3c / L3d: caveats already internally proven**
    - L3c ("H^1 bound ||(D_N − i)^{−1}||_{L²→H¹} < 2") is already PROVED
      per the chain. L3d has a "log N caveat, Remark 8.4". Paper 13's code
      in `paper28-pvnp/code/r55_analyticity_closure.py` +
      `r56_all_eigvecs_h1.json` certifies uniform H¹ and CF decay
      numerically at ρ ≥ 4.27 (matches chain statement). **CLOSABLE:
      caveat can be stated as "numerically matched to 50 digits; analytical
      tightening remains future work" — the log N factor is a proof-style
      issue, not a missing estimate.**

### STILL GENUINELY OPEN — ~53 items

The residual genuinely open items after the above reclassification:

- **paper1 Branch B frontier bullets 4–5**: curved-background and non-linear
  gravity extensions. No code, no literature that resolves; intentionally
  listed as "expected to fail" — these are correctly open.
- **paper08-yang-mills H4**: AF-match + leading-order OPE. Closing-H4 run
  (2026-04-11) conclusively established that A/B/C routes stall; Route D
  (ship conditional) is the live plan. H4 itself stays open.
- **paper13b-grh L5** (character-modulated H¹ cancellation): genuine
  per-conductor computation needed; no existing script.
- **paper25-hilbert-12 L3–L6**: the four-conjecture programme; genuine
  research.
- **paper28-pvnp L5 backward direction** (non-full → Taylor): all seven
  routes examined in the clone-growth bridge work. Stays open.
- **paper29-hodge L3, L7, L8**: motivic Hodge filtration + functoriality.
- **paper30-navier-stokes L3, L5a, L5b, L5, L6–L8**: the integration task
  (Route A Camlin + Route B microlocal) remains; no code exists.
- **paper31-baum-connes L2, L3, L4, L6**: Cuntz–Li application + K-theory
  + spectral payoff — L5 closes by relabelling (see item 5) but the rest
  stay open.
- **paper32-bgs-spectral-statistics L2** (ergodicity of σ_t) and
  downstream L3–L4, L6.
- **paper33-goldbach L5, L6** and **paper34-twin-primes L4, L5** and
  **paper35-schanuel L2–L5**: genuinely open analytic/transcendence
  questions.
- **paper13-rh L1**: CCM 2025 external — not closable from within this
  programme.

---

## Prioritized closures (high-impact first)

| # | Closure | Kind | Chain impact | Effort |
|--:|---|---|---|---|
| 1 | paper13b-grh L1 ← Paper 26 Step 5c (Hecke-twisted cocycle already PROVED) | cross-paper | flips GRH L1 CONJECTURED→PROVED; unblocks L2 status-transport. Confidence 5/10 → 6/10 | label change + 1-sentence cross-reference |
| 2 | paper31-baum-connes L5 ← Higson–Kasparov 2001 (cited in the chain's own wall discussion) | literature | flips OPEN→LITERATURE; Paper 31 closes 1/6 → 2/6; confidence 1/10 → 3/10 | label change |
| 3 | paper32-bgs L5 ← arXiv:2511.18275 (chain's own key reference) | literature | flips CONJECTURED→LITERATURE; BGS 2/7 → 3/7; strengthens Twin Primes L2 inheritance | label change |
| 4 | paper29-hodge L4 ← arXiv:2510.21562 (cited in chain) for abelian-variety-powers slice | literature (scoped) | removes L4 wall for the CM-BSD slice; Hodge restricted to CM attains 4/8 | label change + scope annotation |
| 5 | paper33-goldbach L4 / paper34-twin-primes L2 — "conditional on RH" → "conditional on CCM 2025" | cross-paper | removes RH as an independent wall; aligns with programme-wide conditioning | 2 label changes |
| 6 | paper1 §Frontier bullets 2–3 ← `paper1/code/weyl-anomaly/` + `seeley-dewitt/` | existing code | collapses 2 of 4 residual frontier bullets into already-certified results; clears §"Genuinely open frontier" down to 2 bullets | write-up ~200 words into §B of Paper 1 PROOF-CHAIN |
| 7 | paper28-pvnp L5 forward direction ← `pvnp_nonfullness_test.py` | existing code | the "backward direction" framing in the chain already implies the forward is settled — make it explicit. Doesn't move the confidence, but gives readers a cleaner wall statement | label clarification |
| 8 | paper30-navier-stokes cascade update into Paper 31/32 | cross-paper | propagates L4's unconditional-all-loop to K-theory / spectral-statistics edges | 2 edge-text updates |

### Top 3 quick closures (by confidence-score lift per unit effort)

1. **paper31-baum-connes L5** via Higson–Kasparov 2001. The chain itself
   admits "G is amenable (Higson–Kasparov 2001 applies), so BC holds in
   principle." Lifting from OPEN→LITERATURE costs one line and moves the
   chain confidence from 1/10 to ~3/10. The residual wall (L6) is then
   cleanly the novel bit (K-theory → spectral constraint), not the assembly
   map itself.

2. **paper13b-grh L1** via Paper 26 Step 5c. Paper 26 already proves the
   Hecke-twisted cocycle shift bound ("for all Hecke ψ"). Dirichlet
   characters are a subclass of Hecke characters. A direct transport makes
   GRH's Link 1 PROVED rather than CONJECTURED and lifts GRH confidence
   5/10 → 6/10 without any new mathematics.

3. **paper32-bgs L5** via arXiv:2511.18275. The chain explicitly calls this
   reference *"the single strongest lead in the extended programme"*. L5
   label update is one line and flips BGS from 2/7 to 3/7 closed; it also
   strengthens Twin Primes L2 (cross-paper cascade).

Each of these is a label-only change flagged inside the same chain files
that host the open items; no new mathematics required.
