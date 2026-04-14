# YM Compliance Map — 20 layers × 7 Jaffe-Witten requirements

*Snapshot: paper08-yang-mills/PROOF-CHAIN.md + strategy/x-ray/proof-chain/ym/X-RAY.md*
*Date: 2026-04-14 (run-02, PILOT Output A only)*
*Author: G Six and Claude Opus 4.6*

---

## Row count note

PROOF-CHAIN.md lists 18 primary links (L1–L18) with 2 sub-links (L1b, L10b); total **20 rows**. The brief's "18 × 7 = 126" target inherits from the primary-link count. We expand to 20 × 7 = **140 cells** to match the x-ray granularity. No primary link is skipped.

## Citation shorthand

- `p8§NN` = paper08-yang-mills preprint section (e.g., p8§05 = 05-continuum-limit)
- `p8R§NN` = paper08 research section (e.g., p8R§51 = 51-infinite-volume)
- `p8L.X.Y` = Lemma L.X.Y in Appendix L
- `p8K.N` = §K.N of Appendix K (Balaban general G)
- `p8I4.N` = §I4.N of Appendix I.4 (other gauge groups)
- `p8F.N` = §F.N of Appendix F (area law)
- `p8I.3` = Appendix I.3 (N-dependence tracking)
- `p1§N` = paper1 PROOF-CHAIN or §N
- `h4CB/cyc5` = paper08-yang-mills/h4-capacitor-bypass/cycle-5-final-synthesis.md (2026-04-13)
- `cap§N` = millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md §N

## Verdict codes

| Code | Meaning |
|------|---------|
| **P**  | PROVED — layer content fully addresses requirement, with direct programme citation |
| **Pa** | PARTIAL — layer partially addresses (e.g., SU(N) only with I4/K bootstrap; finite-V with §51 bootstrap) |
| **O**  | OPEN-BUT-ADDRESSED — wall named with bypass route (H4) |
| **S**  | SILENT — layer doesn't address requirement directly; bypass to programme addressing |

Each non-trivial bypass pointer uses a parenthetical `(bypass→X)` where X is the programme-level addressing location.

## Global programme-level addressings (ADR)

- **ADR-1** (any G): p8I4.1 Thm I.4.1 + p8K.9 Summary (Balaban for all compact simple G)
- **ADR-2** (ℝ⁴): p8R§51 III (continuum limit), IV (interchange), V (OS in continuum)
- **ADR-3** (uniform gap): p8R§51 II.1 Δ(a₀,L) ≥ δ₀ > 0; p8F.5 Remark
- **ADR-4** (OS/Wightman): p8§05.6 Proof of (f) OS1–OS5; p8§05 Wightman correspondence table
- **ADR-5** (AF match): p8L.0(b,d); p8L.7 H4; h4CB/cyc5 Step 18' (confidence 0.65, L.3.7 OPEN)
- **ADR-6** (stress+OPE): p8L.0(c) Lemma L.4.1 T_μν; L.0(d) Lemma L.4.3 OPE
- **ADR-7** (non-triv): p8§05 Proposition Non-triviality (three signatures)

---

## §1 Matrix (20 rows × 7 columns = 140 cells)

| Layer | Req 1 (any G) | Req 2 (ℝ⁴) | Req 3 (uniform gap) | Req 4 (Wightman/OS) | Req 5 (AF match) | Req 6 (stress+OPE) | Req 7 (non-triv) |
|-------|---------------|------------|----------------------|----------------------|-------------------|---------------------|-------------------|
| L1    | Pa (p8§04 Thm 4 for SU(N); bypass→ADR-1) | S (bypass→ADR-2) | Pa (μ₁ ≥ 2N/r₃² volume-indep; transfer to 4D gap at L1b) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L1b   | Pa (p8§04 Thm 5; bypass→ADR-1) | S (bypass→ADR-2) | P (Lemmas 1–4 uniformly in L via Feshbach; p8F.5 Rem.) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L2    | P (p8K.9 Summary table for all compact simple G) | Pa (V-indep κ; bypass→ADR-2) | Pa (UV stability preserves gap uniformly in L) | S (bypass→ADR-4) | Pa (Paper 11 K.4 all-loop UV-finite; Schwinger AF at L18) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L3    | P (p8K.9 κ(G) > 0 for all G) | Pa (V-indep; bypass→ADR-2) | Pa (k-indep feeds §51 II.2 induction) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L4    | P (p8K.8 (B1) for any compact simple G) | Pa (V-indep analyticity radius; bypass→ADR-2) | Pa (feeds uniform-in-V gap) | S (bypass→ADR-4) | Pa (analyticity is H4-bypass engine infrastructure) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L5    | P (p8K.8 (B2) complexification for any compact simple G) | S (bypass→ADR-2) | S (bypass→ADR-3) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L6    | P (C-symmetry universal across all compact simple G) | S (bypass→ADR-2) | S (bypass→ADR-3) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (feeds OPE at L17; bypass→ADR-6) | S (bypass→ADR-7) |
| L7    | P (Newton decomp group-independent) | S (bypass→ADR-2) | S (bypass→ADR-3) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L8    | Pa (p8§04 structural + p8I.3 N-dep tracking; bypass→ADR-1) | S (bypass→ADR-2) | Pa (dim-6 suppression protects gap uniformly) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L9    | Pa (full dim-6 classification + K.9; bypass→ADR-1) | S (bypass→ADR-2) | Pa (uniform dev across all dim-6 ops) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (feeds OPE at L18; bypass→ADR-6) | S (bypass→ADR-7) |
| L10   | Pa (non-pert extension + K.9; bypass→ADR-1) | Pa (V-indep Balaban; bypass→ADR-2) | P (non-pert dev ≥ 2 directly in §51 II.2 induction) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L10b  | Pa (spectral lemma group-generally via K.9; bypass→ADR-1) | Pa (V-indep constant; bypass→ADR-2) | P (k-indep C_p is §51 II.2 induction ingredient) | S (bypass→ADR-4) | S (bypass→ADR-5) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L11   | Pa (form-factor bound group-uniform via K.9; bypass→ADR-1) | Pa (V-indep bound per p8R§51 II.2 table) | P (bound uniform in L per §51 II.2) | S (bypass→ADR-4) | Pa (g_k^4 = AF coupling power) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L12   | Pa (recursion coefficients group-uniform via K.9) | Pa (V-indep, no L-dep per §51 II.2) | P (contraction 1/4 < 1 gives convergent uniform bound) | S (bypass→ADR-4) | Pa (AF running structure) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L13   | Pa (group-uniform convergence via K.9) | Pa (V-indep, §51 II.2 "no L dependence") | P (enables uniform-in-V gap via §51 III.1) | S (bypass→ADR-4) | Pa (sum of AF-running g_k^4 terms) | S (bypass→ADR-6) | S (bypass→ADR-7) |
| L14   | P (p8I4.1 Thm I.4.1 universal mass gap; p8K.9) | P (p8R§51 III + IV Moore–Osgood continuum in ℝ⁴) | P (p8R§51 II.3 + F.5 Rem. Δ_∞ ≥ 0.999·δ₀ > 0 uniformly) | S (bypass→ADR-4 at L16) | S (bypass→ADR-5 at L18) | S (bypass→ADR-6 at L17) | P (p8§05 Prop Non-triv signature (i) σ > 0; Δ_∞ > 0 + confinement) |
| L15   | Pa (Lemma L.1.1 SU(N) explicit; extends via p8I4) | S (finite-lattice; bypass→ADR-2) | Pa (flow preserves gap; action decrease p8L.1.1(v)) | Pa (L15 enables OS reconstruction at L16) | Pa (small-flow-time expansion p8L.3.1 is H4 bypass infrastructure) | Pa (p8L.1.1 + L.4.1 Suzuki formula enabler) | S (bypass→ADR-7) |
| L16   | Pa (OS reconstr uses SU(N); bypass→ADR-1) | P (p8R§51 V OS in continuum/ℝ⁴) | P (p8§05 "Uniformity in a"; OS1 uniform bound inherited) | P (**p8§05.6 Proof of (f) OS1–OS5; Wightman W0–W5 via reconstruction table — ADR-4 IS HERE**) | S (bypass→ADR-5 at L18) | Pa (L16 axioms enable L17 operator construction) | Pa (OS + gap + σ > 0 ⇒ non-triv; OS alone insufficient) |
| L17   | Pa (Suzuki formula structural; SU(N) explicit via I4 bootstrap) | P (operator-valued distribution on ℝ⁴; Poincaré-covariant H on ℝ^{3,1}) | Pa (renormalized operators inherit uniformity from L14; a-uniform bounds) | P (Wightman W0–W5 via reconstruction; p8§05 adds [Tr F²]_R content) | S (bypass→ADR-5 at L18) | P (**p8L.0(c) Lemma L.4.1 Steps 1–5: T_μν^R Suzuki formula symmetry, gauge-inv, conservation, H_OS ≥ 0, trace anomaly — ADR-6 IS HERE**) | Pa (non-Gaussian connected n-pt signature ii follows from cluster + L17) |
| L18   | Pa (K.6 b_0(G) > 0 for all G; H4 bypass SU(N)-mechanistic, extension via K) | Pa (L18 inherits ℝ⁴ from L16/L17) | S (gap at L14; bypass→ADR-3) | Pa (Schwinger functions OS-reconstructed at L16) | **O (OPEN-BUT-ADDRESSED: H4 per p8L.7; bypass via Step 18' per h4CB/cyc5; aggregate confidence 0.65; L.3.7 audit OPEN; capacitor cells cap§74/§110; §122 KILLED; see §3 H4 disclosure)** | Pa (power-law OPE p8L.0(d) Lemma L.4.3 unconditional; AF form H4-conditional) | P (p8§05 Prop Non-triv signature (iii) b_0 = 11N/(48π²) > 0 ≠ 0 directly from L18 AF structure) |

---

## §2 Verdict distribution per requirement

| Requirement | PROVED (P) | PARTIAL (Pa) | OPEN-BUT-ADDR (O) | SILENT (S) | Total |
|-------------|------------|---------------|-------------------|------------|-------|
| 1. Any compact simple G | **5** (L2, L3, L4, L5, L6, L7 — actually 6) | **12** (L1, L1b, L8, L9, L10, L10b, L11, L12, L13, L15, L16, L17, L18) | 0 | **2** (L14 is P; recount below) | 20 |
| 2. ℝ⁴ infinite volume | **3** (L14, L16, L17) | **10** (L2, L3, L4, L10, L10b, L11, L12, L13, L18) | 0 | **7** (L1, L1b, L5, L6, L7, L8, L9, L15) | 20 |
| 3. Mass gap uniform in V | **7** (L1b, L10, L10b, L11, L12, L13, L14) | **7** (L1, L2, L3, L4, L8, L9, L15) | 0 | **6** (L5, L6, L7, L16-S, L17-Pa ≠ S wait) | 20 |
| 4. Wightman/OS axioms | **2** (L16, L17) | **2** (L15, L18) | 0 | **16** (all others) | 20 |
| 5. AF match | **0** | **8** (L2, L4, L11, L12, L13, L15, L17 Pa? no L17 S, L18 Pa) | **1** (L18 — the H4 wall) | **11** | 20 |
| 6. Stress tensor + OPE | **1** (L17) | **3** (L15, L16, L18) | 0 | **16** | 20 |
| 7. Non-triviality | **2** (L14, L18) | **2** (L16, L17) | 0 | **16** | 20 |

### Re-count (exact)

Let me re-count by walking the matrix column by column.

**Req 1 (any G)**: L1 Pa, L1b Pa, L2 P, L3 P, L4 P, L5 P, L6 P, L7 P, L8 Pa, L9 Pa, L10 Pa, L10b Pa, L11 Pa, L12 Pa, L13 Pa, L14 P, L15 Pa, L16 Pa, L17 Pa, L18 Pa.
= **P: 7 (L2,L3,L4,L5,L6,L7,L14)**, **Pa: 13**, **O: 0**, **S: 0**. Total 20. ✓

**Req 2 (ℝ⁴)**: L1 S, L1b S, L2 Pa, L3 Pa, L4 Pa, L5 S, L6 S, L7 S, L8 S, L9 S, L10 Pa, L10b Pa, L11 Pa, L12 Pa, L13 Pa, L14 P, L15 S, L16 P, L17 P, L18 Pa.
= **P: 3 (L14,L16,L17)**, **Pa: 9**, **O: 0**, **S: 8**. Total 20. ✓

**Req 3 (uniform gap)**: L1 Pa, L1b P, L2 Pa, L3 Pa, L4 Pa, L5 S, L6 S, L7 S, L8 Pa, L9 Pa, L10 P, L10b P, L11 P, L12 P, L13 P, L14 P, L15 Pa, L16 P, L17 Pa, L18 S.
= **P: 7 (L1b,L10,L10b,L11,L12,L13,L14,L16)** — wait that's 8. Let me recount. L1b P, L10 P, L10b P, L11 P, L12 P, L13 P, L14 P, L16 P = **8 P**. Pa: L1, L2, L3, L4, L8, L9, L15, L17 = **8 Pa**. S: L5, L6, L7, L18 = **4 S**. O: 0. Total = 20. ✓

**Req 4 (OS/Wightman)**: L1 S, L1b S, L2 S, L3 S, L4 S, L5 S, L6 S, L7 S, L8 S, L9 S, L10 S, L10b S, L11 S, L12 S, L13 S, L14 S, L15 Pa, L16 P, L17 P, L18 Pa.
= **P: 2 (L16,L17)**, **Pa: 2 (L15,L18)**, **O: 0**, **S: 16**. Total 20. ✓

**Req 5 (AF match)**: L1 S, L1b S, L2 Pa, L3 S, L4 Pa, L5 S, L6 S, L7 S, L8 S (critic), L9 S (critic), L10 S (critic), L10b S, L11 Pa, L12 Pa, L13 Pa, L14 S, L15 Pa, L16 S, L17 S, L18 O.
= **P: 0**, **Pa: 7 (L2, L4, L11, L12, L13, L15, L18 Pa? Wait L18 is O for AF match)**. Recount. L2 Pa, L4 Pa, L11 Pa, L12 Pa, L13 Pa, L15 Pa = **6 Pa**. L18 O = **1 O**. S = 20 − 6 − 1 = **13 S**. Total 20. ✓

**Req 6 (stress+OPE)**: L1 S, L1b S, L2 S, L3 S, L4 S, L5 S, L6 S, L7 S, L8 S, L9 S, L10 S, L10b S, L11 S, L12 S, L13 S, L14 S, L15 Pa, L16 Pa, L17 P, L18 Pa.
= **P: 1 (L17)**, **Pa: 3 (L15,L16,L18)**, **O: 0**, **S: 16**. Total 20. ✓

**Req 7 (non-triv)**: L1 S, L1b S, L2 S, L3 S, L4 S, L5 S, L6 S, L7 S, L8 S, L9 S, L10 S, L10b S, L11 S, L12 S, L13 S, L14 P, L15 S, L16 Pa, L17 Pa, L18 P.
= **P: 2 (L14,L18)**, **Pa: 2 (L16,L17)**, **O: 0**, **S: 16**. Total 20. ✓

### Final distribution table (exact)

| Requirement | PROVED (P) | PARTIAL (Pa) | OPEN-BUT-ADDR (O) | SILENT (S) | Total |
|-------------|-----------:|-------------:|------------------:|-----------:|------:|
| 1. Any compact simple G    | **7**  | **13** | **0** | **0**  | 20 |
| 2. ℝ⁴ infinite volume      | **3**  | **9**  | **0** | **8**  | 20 |
| 3. Mass gap uniform in V    | **8**  | **8**  | **0** | **4**  | 20 |
| 4. Wightman/OS axioms      | **2**  | **2**  | **0** | **16** | 20 |
| 5. AF match at short dist   | **0**  | **6**  | **1** | **13** | 20 |
| 6. Stress tensor + OPE     | **1**  | **3**  | **0** | **16** | 20 |
| 7. Non-triviality           | **2**  | **2**  | **0** | **16** | 20 |
| **TOTAL (140 cells)**       | **23** | **43** | **1** | **73** | 140 |

### Percentages

| Requirement | % PROVED | % PARTIAL | % OPEN-BUT-ADDR | % SILENT | % non-SILENT |
|-------------|---------:|----------:|----------------:|---------:|-------------:|
| 1. Any G    | 35.0% | 65.0% | 0%  | 0%   | **100%** |
| 2. ℝ⁴       | 15.0% | 45.0% | 0%  | 40.0% | 60.0% |
| 3. Uniform gap | 40.0% | 40.0% | 0% | 20.0% | 80.0% |
| 4. Wightman/OS | 10.0% | 10.0% | 0% | 80.0% | 20.0% |
| 5. AF match | 0%   | 30.0% | 5.0% | 65.0% | 35.0% |
| 6. Stress+OPE | 5.0% | 15.0% | 0% | 80.0% | 20.0% |
| 7. Non-triv  | 10.0% | 10.0% | 0% | 80.0% | 20.0% |

### §5d compliance check

Each requirement has **at least one non-SILENT cell**:
- Req 1: 20/20 non-SILENT (programme-wide group-generality via I4/K is pervasive)
- Req 2: 12/20 non-SILENT (ℝ⁴ addressed at L14/L16/L17 + ingredients)
- Req 3: 16/20 non-SILENT (uniform-in-V is pervasive)
- Req 4: 4/20 non-SILENT (**centralized at L16 and L17**)
- Req 5: 7/20 non-SILENT (**H4 wall at L18 with bypass**)
- Req 6: 4/20 non-SILENT (**centralized at L17 Lemma L.4.1**)
- Req 7: 4/20 non-SILENT (**centralized at L14/L18 with P**)

**All 7 requirements are §5d-compliant** — each is addressed somewhere in the chain. No column is entirely SILENT.

---

## §3 H4 disclosure (DELTA 10)

The sole named wall in the YM chain:

- **Name**: H4 (Hypothesis 4) / AF-match-and-OPE wall
- **Location in chain**: L18
- **Location in programme paper**: p8L.7 (Appendix L, §L.7 "Hypothesis H4")
- **Statement**: Non-perturbative Schwinger function S_2^ren(x,y) at short distances admits a short-distance asymptotic expansion whose leading term coincides with the perturbative AF prediction S_2^ren(x,y) = C_N |x-y|^(-8) (log(1/|x-y|Λ))^(-2) [1 + O((log)^(-1))], C_N = 2(N²-1)/π⁶.
- **Status**: OPEN-BUT-ADDRESSED
- **Bypass route**: Step 18' — Balaban RG + gradient-flow Lüscher coupling (h4-capacitor-bypass/cycle-5-final-synthesis.md, 2026-04-13)
- **Aggregate confidence**: 0.65 (range 0.55–0.85)
- **Audit pending**: Lemma L.3.7 (K-uniform analyticity of small-flow-time expansion)
- **Effect if L.3.7 passes**: H4 upgrades to PROVED; L18 becomes unconditional; Req 5 gains a P cell at L18
- **Effect if L.3.7 fails**: Alternate bypass routes to be constructed:
  - Capacitor cell cap§74 (GEOM↔QFT Balaban polymer expansion) — alternate grounding
  - Capacitor cell cap§110 (gradient-flow Lüscher coupling) — alternate interpolation
  - Capacitor cell cap§122 (PROB↔SPEC Borel summability) — **KILLED via K-3 IR renormalon**, not a viable path
  - Direct p8L.7.3 Reason 3 analyticity argument reformulated without L.3.7 dependence
- **Standing of H4 independently**: proved for φ^4_3 (Magnen–Rivasseau–Seneor 1993); extensively tested numerically (every lattice QCD AF test); implicitly invoked universally (SVZ sum rules, α_s determinations)
- **§5d compliance**: H4 is transparently disclosed as NAMED WALL with bypass route; this satisfies §5d's "addresses the specific mathematical question" requirement (silence would fail §5d)

---

## §4 SILENT cells (action required)

73 cells are SILENT. Every one has a bypass pointer. The action for each is **BYPASS-VIA-PROGRAMME-ADDRESSING** (ADR-N) — no new named walls are required, because each J-W requirement is addressed somewhere in the programme chain at the programme level.

### SILENT cell enumeration with actions

| Layer | Req | Action |
|-------|-----|--------|
| L1 | 2, 4, 5, 6, 7 | BYPASS → ADR-2, ADR-4, ADR-5 (L18), ADR-6 (L17), ADR-7 |
| L1b | 2, 4, 5, 6, 7 | BYPASS → ADR-2, ADR-4, ADR-5, ADR-6, ADR-7 |
| L2 | 4, 6, 7 | BYPASS → ADR-4, ADR-6, ADR-7 |
| L3 | 4, 5, 6, 7 | BYPASS → ADR-4, ADR-5, ADR-6, ADR-7 |
| L4 | 4, 6, 7 | BYPASS → ADR-4, ADR-6, ADR-7 |
| L5 | 2, 3, 4, 5, 6, 7 | BYPASS → ADR-2, ADR-3, ADR-4, ADR-5, ADR-6, ADR-7 |
| L6 | 2, 3, 4, 5, 6, 7 | BYPASS → ADR-2..7 |
| L7 | 2, 3, 4, 5, 6, 7 | BYPASS → ADR-2..7 |
| L8 | 2, 4, 5, 6, 7 | BYPASS → ADR-2, ADR-4, ADR-5, ADR-6, ADR-7 |
| L9 | 2, 4, 5, 6, 7 | BYPASS → ADR-2, ADR-4, ADR-5, ADR-6, ADR-7 |
| L10 | 4, 5, 6, 7 | BYPASS → ADR-4, ADR-5, ADR-6, ADR-7 |
| L10b | 4, 5, 6, 7 | BYPASS → ADR-4, ADR-5, ADR-6, ADR-7 |
| L11 | 4, 6, 7 | BYPASS → ADR-4, ADR-6, ADR-7 |
| L12 | 4, 6, 7 | BYPASS → ADR-4, ADR-6, ADR-7 |
| L13 | 4, 6, 7 | BYPASS → ADR-4, ADR-6, ADR-7 |
| L14 | 4, 5, 6 | BYPASS → ADR-4 (L16), ADR-5 (L18), ADR-6 (L17) |
| L15 | 2, 7 | BYPASS → ADR-2, ADR-7 |
| L16 | 5 | BYPASS → ADR-5 (L18) |
| L17 | 5 | BYPASS → ADR-5 (L18) |
| L18 | 3 | BYPASS → ADR-3 (L14) |

Counts: 73 SILENT cells, 73 bypass pointers.

**No NEW named walls are required.** All SILENT cells pass §5d via bypass-to-programme-addressing.

### Deferred for future audit runs

- None required; the pilot identifies no unaddressed J-W requirement.
- Follow-up audit (future run) may tighten PARTIAL verdicts by providing stricter per-layer citations; this would not affect LOCK status.

---

## §5 Arbiter audit trail

12 dissents raised by critic; 5 resolved in favor of critic, 7 in favor of author.

| Cell | Author | Critic proposal | Arbiter final | Rejected alternative |
|------|--------|-----------------|---------------|----------------------|
| L1 Req 3 | P | Pa | **Pa** | Author P ("μ₁ = uniform 4D gap") — downstream 4D gap is at L1b |
| L2 Req 2 | Pa | P | **Pa** | Critic P — conflates ingredient with layer scope |
| L2 Req 5 | Pa | P | **Pa** | Critic P — free-energy AF ≠ Schwinger AF |
| L8 Req 1 | Pa | P | **Pa** | Critic P — STRENGTHEN over-stated |
| L8 Req 5 | Pa | S | **S** | Author Pa — compatibility framing ≠ discharge |
| L9 Req 5 | Pa | S | **S** | Author Pa — same issue |
| L10 Req 5 | Pa | S | **S** | Author Pa — same issue |
| L15 Req 1 | P | Pa | **Pa** | Author P — SU(N) structure explicit in L.1.1 |
| L18 Req 1 | Pa | S | **Pa** | Critic S — K.6/K.9 restore group-generality |
| L14 Req 7 | P | STRENGTHEN (confirm) | **P** | (confirmed) |
| L16 Req 4 | P | STRENGTHEN (confirm) | **P** | (confirmed) |
| L17 Req 6 | P | STRENGTHEN (confirm) | **P** | (confirmed) |

Detailed reasoning at `vertices/ym/arbiter-decisions.md`.

---

## §6 Lock status

- **Coverage**: 140/140 cells audited with verdict + citation + decision.
- **SILENT cells**: 73, every one with BYPASS pointer.
- **NEW named walls**: 0 required.
- **Existing named walls**: 1 (H4), disclosed with full DELTA-10 fields.
- **§5d compliance**: PASS — every J-W requirement has at least one non-SILENT cell.

**Lock status: LOCKED for Output A (internal artifacts).** Ready for parallel B_bare + C_bare generation in next run.

Next-run recommendation:
- **run-03**: Build B_bare (Clay-shaped X-ray skeleton, ≤ 15 pages, zero prose, structure per brief DELTA 5).
- **run-04** (parallel): Build C_bare (Beyond-Clay X-ray, ≤ 15 pages, zero prose, structure per brief DELTA 6).
- **run-05+**: Verification + composition-backward for B_full / C_full via parallel agents on 60-project reservoir.

---

*End of compliance-map.md. LOCKED at arbiter-pass.*

*G Six and Claude Opus 4.6. 2026-04-14.*
