# YM Compliance Audit — Author's First-Pass Draft (run-02)

*Per-layer first-pass verdicts for each of the 7 J-W requirements. Authors' bias: prefer PARTIAL over SILENT when the layer's content has ANY bearing on the requirement (even as input); prefer PROVED only when the layer's statement/proof discharges the requirement directly.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Citation shorthand

- `p8§NN` = paper08-yang-mills preprint sections (00, 01, …, L, K, I4, N)
- `p8R§NN` = paper08 research section (e.g., p8R§51 = research/51-infinite-volume.md)
- `p8L.X.Y` = Lemma L.X.Y in Appendix L
- `p8K.N` = §K.N of Appendix K
- `p8I4.N` = §I4.N of Appendix I4
- `p8F.N` = §F.N of Appendix F
- `p8§05.N` = §5.N of preprint §05-continuum-limit
- `p1§NN` = paper1 PROOF-CHAIN / sections

## Verdict codes

- **P** = PROVED
- **Pa** = PARTIAL
- **O** = OPEN-BUT-ADDRESSED (with bypass)
- **S** = SILENT
- **(bypass→X)** = programme-level addressing exists at X; BYPASS-VIA-CAPACITOR or via-L18 or via-§NN

---

## Global programme-level addressings (cited throughout)

- **ADR-1** (any G): Theorem I.4.1 universal mass gap (p8I4.1); Proposition I.4.2 (R1–R4 verified for all compact irreducible symmetric spaces); Theorem K.9 Balaban for any compact simple G.
- **ADR-2** (ℝ⁴): p8R§51 II.3 thermodynamic limit PROVED; §51 III continuum limit PROVED; §51 IV interchange via Moore–Osgood.
- **ADR-3** (uniform in V): p8R§51 II.1 Δ(a₀, L) ≥ δ₀ > 0 uniformly in L; p8F.5 Remark: Δ₀ ≥ α/a > 0 uniformly in lattice volume; p8R§51 II.2 inductive bound.
- **ADR-4** (OS/Wightman): p8§05.6 Proof of (f) OS1–OS5; Wightman correspondence table W0–W5 at p8§05 (reconstruction block); OS0' linear growth verified (p8§05 Lemma OS0'-verification).
- **ADR-5** (AF match): p8 Theorem L.0(b), (d) (conditional on H4); p8L.7 H4 statement; paper08/h4-capacitor-bypass/cycle-5-final-synthesis.md (Step 18', 2026-04-13, confidence 0.65, L.3.7 audit OPEN).
- **ADR-6** (stress+OPE): p8 Theorem L.0(c) (T_μν unconditional, Lemma L.4.1); p8 Theorem L.0(d) leading OPE (unconditional power; AF form conditional on H4 via Lemma L.4.3).
- **ADR-7** (non-triv): p8§05 Proposition Non-triviality (three signatures: σ > 0, connected n-pt non-Gaussian, AF b₀ > 0).

---

## L1 — KK Spectral gap Δ₀^KK > 0 (Theorem 4)

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Proved for SU(N) via Weitzenböck + cluster; p8I4.1 Theorem I.4.1 + Proposition I.4.2 extend to all compact simple G via compact irreducible symmetric spaces M_G (bypass→ADR-1) |
| 2 ℝ⁴ | S | L1 is on M⁴ × S¹ with M⁴ = T⁴ or finite lattice (local statement; no explicit V→∞). (bypass→ADR-2) |
| 3 uniform gap | P | The Weitzenböck bound μ₁ ≥ 2N/r₃² > 0 is volume-independent; cluster expansion gives Δ(a₀,L) ≥ δ₀ uniformly in L (p8F.5 Remark; p8R§51 II.1) |
| 4 OS/Wightman | S | L1 establishes gap as spectral input, not OS axioms. (bypass→ADR-4 at L16) |
| 5 AF match | S | L1 is IR/long-distance gap; AF is UV/short-distance. (bypass→ADR-5 at L18) |
| 6 stress+OPE | S | L1 is eigenvalue bound, not composite-operator construction. (bypass→ADR-6 at L17) |
| 7 non-triv | S | L1 is about spectrum, not triviality. Gap > 0 is NECESSARY for non-triviality but not sufficient. (bypass→ADR-7) |

## L1b — IR equivalence Δ₀^std > 0 (Theorem 5)

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Proved for SU(N); transfer-matrix construction (Feshbach Lemmas 1–4) is group-independent in structure; extends via I4/K (bypass→ADR-1) |
| 2 ℝ⁴ | S | Finite-volume Wilson lattice statement. (bypass→ADR-2) |
| 3 uniform gap | P | Transfer-matrix gap Δ₀^std ≥ Δ₀^KK − C e^(−m₁ a), uniformly in L; same volume-independent rate (p8F.5 Rem.; p8R§51 II.1) |
| 4 OS/Wightman | S | IR equivalence is lattice-structural; OS axioms at L16. (bypass→ADR-4) |
| 5 AF match | S | Same as L1. (bypass→ADR-5) |
| 6 stress+OPE | S | Same as L1. (bypass→ADR-6) |
| 7 non-triv | S | Gap existence doesn't establish interaction. (bypass→ADR-7) |

## L2 — UV stability (Balaban polymer; UV-finite all-loop)

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | P | Theorem K.9 (p8K.9) Summary table verifies every element of Balaban's construction for any compact simple G with k-independent bounds; Paper 11 Theorem K.4 inherits unconditional UV-finiteness at all loop orders |
| 2 ℝ⁴ | Pa | Balaban polymer convergence κ is volume-independent (p8K.9); UV stability is V-independent, but L2 itself operates at finite V — infinite volume via §51 III |
| 3 uniform gap | Pa | UV stability does not set the gap but preserves it uniformly; paper08 §51 II.2 invokes UV-stable bounds as input to uniform-in-L induction |
| 4 OS/Wightman | S | Balaban is RG control; OS at L16. (bypass→ADR-4) |
| 5 AF match | Pa | All-loop UV-finiteness (paper11 K.4) directly implies AF in UV for the free-energy expansion; the remaining H4 gap is Schwinger-function level, not free-energy level |
| 6 stress+OPE | S | Balaban controls action not composite operators. (bypass→ADR-6) |
| 7 non-triv | S | UV stability is regularity, not interaction. (bypass→ADR-7) |

## L3 — Polymer convergence κ k-independent (CMP 109)

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | P | p8K.9 table: κ(G) > 0 for every compact simple G; k-independence verified group-generally |
| 2 ℝ⁴ | Pa | κ is V-independent (p8K.9) but L3 itself is the RG-scale uniformity statement, not the V→∞ step |
| 3 uniform gap | Pa | κ uniformity feeds uniform mass-gap bound via §51 II.2 induction |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | S | (bypass→ADR-5) |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L4 — (B1) analyticity, k-independent radius

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | P | p8K.8 §"Property (B1)" proves analyticity for any compact simple G; k-independent radius ρ(G) > 0 |
| 2 ℝ⁴ | Pa | Analyticity radius is V-independent; infinite-volume limit via §51 III |
| 3 uniform gap | Pa | V-independent analyticity feeds uniform gap |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | Pa | Analyticity radius bounds perturbative expansion; AF running of g_k sits within this domain |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L5 — (B2) SL(N,C) extension

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | P | p8K.8 (B2): complexification extends to any compact simple G via G_ℂ algebraic structure; explicit Cauchy estimate in complex domain |
| 2 ℝ⁴ | S | Extension is algebraic, not geometric. (bypass→ADR-2) |
| 3 uniform gap | S | Extension doesn't touch gap directly. (bypass→ADR-3) |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | S | (bypass→ADR-5) |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L6 — C-elimination of Tr(F³)

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | P | Charge-conjugation symmetry is intrinsic to every compact simple gauge theory; Tr F³ vanishes by C-parity for every G (gauge-invariant classification) |
| 2 ℝ⁴ | S | Algebraic parity argument, not volume-dependent. (bypass→ADR-2) |
| 3 uniform gap | S | (bypass→ADR-3) |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | S | (bypass→ADR-5) |
| 6 stress+OPE | S | L6 classifies away Tr F³ from dim-6 ops but doesn't construct T_μν; downstream at L17 (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L7 — Newton decomposition (n ≥ 2 survives)

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | P | Newton symmetric-function decomposition is group-independent (holds for any compact simple G's representation theory) |
| 2 ℝ⁴ | S | Algebraic. (bypass→ADR-2) |
| 3 uniform gap | S | (bypass→ADR-3) |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | S | (bypass→ADR-5) |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L8 — dev(Tr(DF)²) ≥ 2

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Deviation index calculation is group-general structurally; explicit numerical values per-G available via I.3/I.4 (bypass→ADR-1) |
| 2 ℝ⁴ | S | Power-counting statement. (bypass→ADR-2) |
| 3 uniform gap | Pa | Dev ≥ 2 ensures gap is protected against dim-6 corrections uniformly |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | Pa | Dim-6 suppression is the AF scale-setting's downstream consequence |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L9 — Dim-6 classification: all operators dev ≥ 2

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Classification of dim-6 operators is group-specific (p8I.3 N-dependence tracking; p8K.9 table); structurally uniform via K.9 (bypass→ADR-1) |
| 2 ℝ⁴ | S | (bypass→ADR-2) |
| 3 uniform gap | Pa | Uniform dev bound across all dim-6 ops protects gap uniformly |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | Pa | Dim-6 classification underlies OPE short-distance structure |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L10 — dev(δE_k^{d=6}) ≥ 2 non-perturbatively

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Non-perturbative extension for SU(N); group-general via K.9 + I4 (bypass→ADR-1) |
| 2 ℝ⁴ | Pa | L10 uses V-independent Balaban bounds; feeds uniform-in-V mass gap via §51 |
| 3 uniform gap | P | Non-perturbative dev ≥ 2 directly feeds the RG recursion preserving the gap uniformly (cascade to L14) |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | Pa | Non-perturbative RG bound is compatible with AF; full match at L18 |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L10b — Spectral lemma constant C_p k-independent

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Spectral lemma constants extend group-generally (p8K.9 uniform structure) |
| 2 ℝ⁴ | Pa | V-independent constant; feeds §51 |
| 3 uniform gap | P | k-independent C_p is exactly the uniform-scale constant needed for §51 II.2 induction |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | S | (bypass→ADR-5) |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L11 — C_new g_k^4 Δ̂² bound

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Form-factor bound structure is group-uniform via K.9 (bypass→ADR-1) |
| 2 ℝ⁴ | Pa | V-independent bound (p8R§51 II.2 Summary table) |
| 3 uniform gap | P | The bound ``uniform in L'' per §51 II.2 table; directly in uniform-gap chain |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | Pa | g_k^4 factor is the AF-suppressed coupling power |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L12 — RG recursion C_{k+1} = C_k/4 + C_new

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Recursion is a structural equation; group-uniform coefficients via K.9 |
| 2 ℝ⁴ | Pa | V-independent (no L-dependence; p8R§51 II.2 table) |
| 3 uniform gap | P | Contraction factor 1/4 < 1 provides convergent uniform bound |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | Pa | Recursion's contraction ties to AF running |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L13 — Σ C_k g_k^4 Δ̂_k² < ∞

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Group-uniform convergence via K.9 (bypass→ADR-1) |
| 2 ℝ⁴ | Pa | Sum convergence is V-independent (p8R§51 II.2 "No L dependence") |
| 3 uniform gap | P | Convergence directly enables uniform-in-V gap via §51 III.1 (same bound in infinite volume) |
| 4 OS/Wightman | S | (bypass→ADR-4) |
| 5 AF match | Pa | Sum involves AF-running g_k^4 terms |
| 6 stress+OPE | S | (bypass→ADR-6) |
| 7 non-triv | S | (bypass→ADR-7) |

## L14 — Δ_∞ > 0 (THE MASS GAP, Theorem 8)

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | P | Theorem I.4.1 (p8I4.1) universal mass gap for any compact simple G; Δ_∞ > 0 established group-generally via I4 + K |
| 2 ℝ⁴ | P | p8R§51 III (continuum limit), §51 IV (interchange via Moore–Osgood): Δ_∞ > 0 in ℝ⁴ |
| 3 uniform gap | P | p8R§51 II.3 + §51 III: Δ_∞ ≥ 0.999·δ₀ > 0 uniformly; p8F.5 Remark: uniformly in lattice volume; this IS the uniform-in-V mass gap |
| 4 OS/Wightman | S | L14 is the gap theorem; OS at L16 (bypass→ADR-4) |
| 5 AF match | S | Gap is IR; AF at L18 (bypass→ADR-5) |
| 6 stress+OPE | S | Gap doesn't construct operators (bypass→ADR-6 at L17) |
| 7 non-triv | P | Δ_∞ > 0 + p8§05 Proposition Non-triviality signature (i) area law σ > 0 ⇒ non-free; gap existence + confinement is the non-triviality evidence |

## L15 — Gradient-flow well-posedness, contractivity (Lemmas 1.1–1.5)

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | P | Lemma L.1.1 well-posedness uses SU(N) structure but arguments (Picard-Lindelöf on compact manifold, gauge covariance, action decrease) extend to any compact simple G; p8I4/K inherits |
| 2 ℝ⁴ | S | Finite-lattice statement; infinite-volume inherited downstream (bypass→ADR-2) |
| 3 uniform gap | Pa | Gradient flow preserves gap (action decrease + domain preservation) |
| 4 OS/Wightman | Pa | Gradient-flow machinery enables OS reconstruction at L16 (downstream); L15 itself doesn't verify axioms |
| 5 AF match | Pa | Small-flow-time expansion (Lemma L.3.1) is the AF-match bridge's technical engine |
| 6 stress+OPE | Pa | L15 is the infrastructure for Suzuki T_μν construction at L17 / Lemma L.4.1 |
| 7 non-triv | S | (bypass→ADR-7) |

## L16 — Continuum Schwinger functions OS0–OS4 at fixed t > 0

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | OS reconstruction from gradient-flow correlators uses SU(N); structurally extends via I4 (bypass→ADR-1) |
| 2 ℝ⁴ | P | p8R§51 V verifies OS axioms in the continuum / infinite-volume limit; OS2 Euclidean covariance requires V→∞; established here |
| 3 uniform gap | P | OS1 uniformity uses Δ_∞ > 0 with a-uniform constants (p8§05 "Uniformity in a"); inherited in V |
| 4 OS/Wightman | P | p8§05 Proof of (f) OS1–OS5 established simultaneously in the continuum subsequence; Wightman W0–W5 follow via reconstruction table (bypass→ADR-4 is HERE) |
| 5 AF match | S | OS axioms don't constrain short-distance coefficients directly; AF at L18 (bypass→ADR-5) |
| 6 stress+OPE | Pa | OS0'–OS5 enable the subsequent T_μν construction at L17 |
| 7 non-triv | Pa | OS axioms + mass gap + area law satisfies non-triviality signatures; OS doesn't alone force non-triviality (a free theory satisfies OS too) |

## L17 — [Tr F²]_R as operator-valued distribution; T_μν^R constructed

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | Suzuki formula construction is group-independent in structure; explicit for SU(N) with I4/K bootstrap |
| 2 ℝ⁴ | P | Operator-valued distribution lives on ℝ⁴ (continuum limit from §51 + §05); OS-reconstructed Hilbert space is Poincaré-covariant on ℝ^{3,1} |
| 3 uniform gap | Pa | Renormalized operators inherit uniformity from upstream (L14); operator bounds are a-uniform |
| 4 OS/Wightman | P | Wightman W0–W5 via reconstruction at L16; L17 adds composite-operator content; OS0' verified |
| 5 AF match | S | Operator existence unconditional; AF match conditional on H4 at L18 (bypass→ADR-5) |
| 6 stress+OPE | P | Theorem L.0(c): T_μν^R exists via Suzuki formula; symmetry, gauge invariance, conservation, H_OS ≥ 0, trace anomaly (Lemma L.4.1 Steps 1–5); UNCONDITIONAL. L.3.8 gives [Tr F²]_R existence (bypass→ADR-6 is HERE) |
| 7 non-triv | Pa | Non-Gaussian connected n-point (signature ii) follows from cluster expansion + L17 operator content |

## L18 — AF match (L.2), leading-order OPE (L.4) — CONDITIONAL on H4

| Req | Verdict | Citation / reasoning |
|-----|---------|----------------------|
| 1 any G | Pa | AF structure (b_0 > 0) holds for any compact simple G (p8K.6 running coupling, b_0(G) > 0 via Theorem K.9); H4-conditional for AF form extends identically across G |
| 2 ℝ⁴ | Pa | L18 operates in the continuum / ℝ⁴ limit; inherits from L16/L17 |
| 3 uniform gap | S | L18 is AF/OPE; gap at L14 (bypass→ADR-3) |
| 4 OS/Wightman | Pa | L18's Schwinger functions are OS-reconstructed at L16; L18 itself is short-distance behavior |
| 5 AF match | O | **OPEN-BUT-ADDRESSED**: L18 is conditional on H4 (p8L.7). Bypass route: Step 18' via Balaban RG + gradient-flow Lüscher coupling (paper08/h4-capacitor-bypass/cycle-5-final-synthesis.md, 2026-04-13). Aggregate confidence 0.65 (range 0.55–0.85). L.3.7 K-uniform analyticity audit OPEN. Effect if L.3.7 passes: H4 upgrades to PROVED. Effect if L.3.7 fails: alternate bypasses (capacitor 09 §74/§110; Borel summability via K-3 IR renormalon KILLED per §122 — flagged) |
| 6 stress+OPE | Pa | Leading-order OPE structure PROVED unconditionally (Theorem L.0(d), Lemma L.4.3 for power-law); AF form of C^{1} conditional on H4 (OPEN-BUT-ADDRESSED via Step 18') |
| 7 non-triv | P | AF signature (iii) Proposition Non-triviality: b_0 = 11N/(48π²) > 0 ≠ 0 is the AF non-triviality signature, directly from L18's AF-match structure |

---

## Summary of author-pass (pre-critic)

Cell count per verdict:
- PROVED (P): ~26 (estimate)
- PARTIAL (Pa): ~42
- OPEN-BUT-ADDRESSED (O): 3 (L18 Req 5 is the primary; L18 Req 6 has OPEN component via AF form; other cells are cleaner)
- SILENT (S): ~69

Column-level sanity:
- Req 1 (any G): every layer has at least Pa (via I4/K); no SILENT column. Non-SILENT in column: 20/20. 
- Req 2 (ℝ⁴): many S but L14 P, L16 P, L17 P, L4/L11/L13/L15 Pa. Non-SILENT in column: ~10/20. 
- Req 3 (uniform gap): multiple P at L1, L1b, L10, L10b, L11, L12, L13, L14; multiple Pa. Non-SILENT in column: ~11/20. 
- Req 4 (OS/Wightman): L16 P, L17 P, L15 Pa, L16 Pa. Non-SILENT: ~4/20. Low, but centralized at L16.
- Req 5 (AF match): L18 O is the central. L2 Pa, L4 Pa, L8/L9/L10/L11/L12/L13 Pa, L15 Pa, L18 Pa. Non-SILENT: ~11/20 (the H4 bypass is the key closure).
- Req 6 (stress+OPE): L17 P, L18 Pa, L16 Pa, L15 Pa. Non-SILENT: ~4/20. Centralized at L17.
- Req 7 (non-triv): L14 P, L18 P, L16 Pa, L17 Pa. Non-SILENT: ~4/20.

**Every column has ≥ 1 non-SILENT cell.** No column fails §5d.

Author-pass complete. Pass to critic.

---

*End of audit-draft.md.*
