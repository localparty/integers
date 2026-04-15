# Hodge Audit Draft — Per-Link Verdicts (Author Pass)

*First-pass author verdicts for 8 × 6 = 48 cells. Citations attached. Critic pass follows.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Verdict codes

| Code | Meaning |
|------|---------|
| **P**  | PROVED — link content fully addresses requirement with direct citation |
| **Pa** | PARTIAL — link partially addresses (known slice / restricted scope) |
| **O**  | OPEN-BUT-ADDRESSED — wall named with bypass route (W1/W2/W3) |
| **S**  | SILENT — link doesn't address requirement directly; bypass to programme addressing |

---

## L1 — BC encodes Artin motives as endomotives (CCM 2005) [LITERATURE]

- **Req 1 (scope)**: Pa — Artin motives come from finite étale covers of number fields; they are 0-dimensional smooth projective over ℂ after base change (CCM05 §2; p29L.1). Targets are projective but the scope generalization to higher-dim projective requires L8. Action: bypass→ADR-1 at L5/L8.
- **Req 2 (Hodge decomp+filt)**: S — endomotives encode Galois/spectral data, not Hodge-filtration structure directly. Bypass→ADR-2 (at L3).
- **Req 3 (rational/AH)**: S — Artin motives are 0-dim so H^{p,p} = ℚ trivially for p=0; AH obstruction vacuous at weight 0. Bypass→ADR-3 (framework-level rational discipline at L4).
- **Req 4 (cl(Z)/Chern)**: S — no cycle-class assignment at this link. Bypass→ADR-4 (at L5/L6).
- **Req 5 (main assertion)**: S — L1 provides encoding, not assertion. Bypass→ADR-5 (at L7/L8).
- **Req 6 (all codim/dim)**: S — Artin motives are weight-0 only. Bypass→ADR-6 (via L8 functoriality).

Citation: CCM05 §2-3; p29L.1.

## L2 — Endomotives → motivic Galois group (Tannakian) [LITERATURE]

- **Req 1 (scope)**: Pa — G_mot is reconstructed over number-field motives; extension to general smooth projective is L8-dependent. Bypass→ADR-1 (at L5/L8).
- **Req 2 (Hodge decomp+filt)**: S — Tannakian reconstruction does not by itself install Hodge structure. Bypass→ADR-2 (at L3).
- **Req 3 (rational/AH)**: Pa — Tannakian category is ℚ-linear by construction (Deligne-Milne); AH obstruction respected (no integral lattice claimed at this layer). Citation: Deligne-Milne; p29L.2.
- **Req 4 (cl(Z)/Chern)**: S — no cycle content. Bypass→ADR-4.
- **Req 5 (main assertion)**: S — no assertion. Bypass→ADR-5.
- **Req 6 (all codim/dim)**: S — weight-zero only. Bypass→ADR-6.

Citation: Deligne-Milne (Tannakian); p29L.2.

## L3 — Motivic Galois acts on de Rham → Hodge filtration [CONJECTURED → OPEN-BUT-ADDRESSED as W1]

- **Req 1 (scope)**: Pa — acts on de Rham of smooth projective (assumed scope) once G_mot is set up; Chow + GAGA bridge analytic ↔ algebraic on projective. Citation: p29L.3; Del§2 Rem (i).
- **Req 2 (Hodge decomp+filt)**: **O** — this IS W1. Action target is the Hodge filtration F^p; conjectured that G_mot-action respects F^p. Bypass route: motivic BC extension + FMS24 for ab-var-powers slice → PARTIAL closure at L4. Citation: p29§W1; p29L.3; FMS24; p31L.6.
- **Req 3 (rational/AH)**: Pa — statement is ℚ-linear (motivic Galois acts on ℚ-structure); AH obstruction addressed at framework level (rational throughout). Citation: Del§2 Rem (iv); p29L.3.
- **Req 4 (cl(Z)/Chern)**: S — L3 is structural, not cycle-producing. Bypass→ADR-4 (at L5/L6).
- **Req 5 (main assertion)**: S — no assertion at structural layer. Bypass→ADR-5 (at L7).
- **Req 6 (all codim/dim)**: S — all codim in scope in principle, but no explicit enumeration here. Bypass→ADR-6 (at L8 or L14 in B_bare).

Citation: p29L.3 (CONJECTURED status); W1 named wall.

## L4 — Standard conjecture D for BC-motivated varieties [PARTIAL]

- **Req 1 (scope)**: Pa — std conj D is a statement on smooth projective /ℂ; scope-compatible. Citation: p29L.4; classical (Grothendieck).
- **Req 2 (Hodge decomp+filt)**: **O** — W1 continuation: D for BC-motivated = motivic Galois respects F^p-compatibility (num vs hom equivalence). Bypass: FMS24 closed ab-var-powers; generic BC-motivated OPEN. Citation: p29§W1; p29L.4; FMS24.
- **Req 3 (rational/AH)**: Pa — std conj D is stated on ℚ-algebraic classes; AH obstruction compatible (AH blocks integral, not rational). Citation: Del§2 Rem (iv); p29L.4.
- **Req 4 (cl(Z)/Chern)**: Pa — std conj D concerns numerical vs homological equivalence of algebraic cycles → directly speaks to cl(Z). Ab-var-powers slice fully PROVED; generic OPEN. Citation: FMS24; p29L.4; Del§2 Rem (ii).
- **Req 5 (main assertion)**: **O** — W1 feeds main assertion via route A. Bypass: ab-var-powers + André motivated recovery for ab-var slice; generic OPEN. Citation: p29§W1; p29L.4; FMS24; André motivated [1] Del refs.
- **Req 6 (all codim/dim)**: Pa — FMS24 covers all (p, N) for ab-var-powers; generic (p, N) OPEN. Citation: FMS24; p29L.4.

Citation: p29L.4 (PARTIAL for ab-var-powers via FMS24 arXiv:2510.21562).

## L5 — Lefschetz B for CP² × S² [KNOWN]

- **Req 1 (scope)**: P — CP² × S² is smooth projective /ℂ (S² = CP¹); classical example. Citation: p29L.5; Chow trivial.
- **Req 2 (Hodge decomp+filt)**: P — Hodge structure of CP² × S² explicit: H^{1,1} = 1 on each factor, product has standard Künneth Hodge decomposition. Citation: p29L.5; classical.
- **Req 3 (rational/AH)**: P — Hodge classes on CP^n × CP^m are all algebraic and ℚ-valued (even ℤ-valued here because projective-bundle case has no AH torsion); our claim is rational-consistent. Citation: Del§2 Rem (iii) Kodaira-Spencer / Lefschetz (1,1); p29L.5.
- **Req 4 (cl(Z)/Chern)**: P — H^{1,1}(CP² × S², ℤ) generators are c_1 of the tautological bundles (Chern classes of algebraic vector bundles); Lefschetz B is satisfied. Citation: Del§2 Rem (ii); p29L.5; classical.
- **Req 5 (main assertion)**: Pa — for this specific variety the conjecture holds (Hodge = algebraic); but L5 is an instance check, not a general route. Citation: p29L.5.
- **Req 6 (all codim/dim)**: Pa — L5 covers one specific (codim, dim) pair; functoriality to all (p, N) is at L8. Bypass→ADR-6 (at L8 W2).

Citation: p29L.5 (KNOWN, classical).

## L6 — Geometric Langlands → Hitchin → Hodge structures [PARTIAL]

- **Req 1 (scope)**: Pa — Hitchin moduli M_H(X, G) is smooth quasi-projective (open dense locus is smooth projective); scope compatible after stability restriction. Citation: p29L.6; GR24.
- **Req 2 (Hodge decomp+filt)**: Pa — Hitchin moduli carries a natural Hodge structure (Simpson's nonabelian Hodge); route B installs a Hodge decomposition via the Dolbeault ↔ Betti ↔ de Rham Simpson correspondence. Citation: p29L.6; GR24; Simpson nonabelian Hodge (landscape §6).
- **Req 3 (rational/AH)**: Pa — cohomology of Hitchin moduli has ℚ-Hodge structure; AH obstruction respected (rational claim throughout). Citation: p29L.6; Del§2 Rem (iv).
- **Req 4 (cl(Z)/Chern)**: Pa — Hitchin moduli parameterizes algebraic Higgs bundles; Chern classes of universal Higgs bundle are cl(Z) candidates producing Hodge classes. Citation: p29L.6; Simpson; Del§2 Rem (ii).
- **Req 5 (main assertion)**: Pa — GR24 gives geometric Langlands (global statement); Hodge-conjecture reduction to BC-motivated requires L7 composition. Citation: p29L.6; GR24; W3 disclosure.
- **Req 6 (all codim/dim)**: Pa — Hitchin spaces are infinite family in (rank, genus); route B covers many (p, N) after reduction but full enumeration requires L7+L8. Citation: p29L.6.

Citation: p29L.6 (PARTIAL via GR24 arXiv:2405.03599).

## L7 — Routes A + B compose: Hodge for BC-motivated varieties [OPEN → W3]

- **Req 1 (scope)**: Pa — composition targets BC-motivated (which are smooth projective); scope compatible with §5d. Citation: p29L.7.
- **Req 2 (Hodge decomp+filt)**: **O** — composition relies on Route-A Hodge filtration (W1) + Route-B Simpson filtration agreeing; 2025 preprint 5-step algorithm OPEN. Citation: p29§W3; p29L.7; L^2-25.
- **Req 3 (rational/AH)**: Pa — composition preserves ℚ-structure (both routes are ℚ-Hodge); AH obstruction respected. Citation: p29L.7; Del§2 Rem (iv).
- **Req 4 (cl(Z)/Chern)**: Pa — composition target is algebraic-cycle origin for Hodge classes on BC-motivated; depends on W3 closure. Citation: p29L.7; W3.
- **Req 5 (main assertion)**: **O** — this IS the main-assertion statement for BC-motivated class. Bypass: L^2-25 5-step algorithm. If algorithm fails: individual routes still valid, no composite. If passes: Hodge for BC-motivated class delivered. Citation: p29§W3; p29L.7; L^2-25.
- **Req 6 (all codim/dim)**: **O** — composition would cover all (p, N) within BC-motivated class; generic smooth projective OPEN (at L8). Citation: p29§W3; p29L.7; extension to generic via W2.

Citation: p29L.7 (OPEN → W3 named wall).

## L8 — Extension to all smooth projective via motivic functoriality [OPEN → W2]

- **Req 1 (scope)**: **O** — L8 IS the scope-expansion step from BC-motivated to ALL smooth projective /ℂ. Bypass: restrict Clay claim to BC-motivated + André motivated recovery for ab-var slice. Citation: p29§W2; p29L.8; Del§5.
- **Req 2 (Hodge decomp+filt)**: Pa — all smooth projective /ℂ automatically carry Hodge decomposition (classical Hodge theory, Hodge 1952); the issue is transporting motivic Hodge-filtration through the extension functor. Citation: Del§1; p29L.8.
- **Req 3 (rational/AH)**: Pa — scope preserved as rational; AH obstruction universal for smooth projective. Citation: Del§2 Rem (iv); p29L.8.
- **Req 4 (cl(Z)/Chern)**: **O** — functoriality must transport algebraic-cycle origin to all smooth projective; W2 wall. Bypass: restrict to BC-motivated. Citation: p29§W2; p29L.8.
- **Req 5 (main assertion)**: **O** — L8 IS the full Hodge conjecture statement; W2 is "arguably as hard as Hodge itself" per p29 current wall note. Bypass: restrict scope. Citation: p29§W2; p29L.8; Del§5.
- **Req 6 (all codim/dim)**: **O** — L8 IS the all-codim-all-dim functoriality step. Bypass: p=1 PROVED (Lefschetz (1,1) / Kodaira-Spencer Del[7]); ab-var-powers PROVED (FMS24); generic projective p≥2 OPEN. Citation: p29§W2; p29L.8; FMS24; Del[7].

Citation: p29L.8 (OPEN → W2 named wall).

---

## Summary (author pass, pre-critic)

Distribution per requirement:

- **Req 1 (scope)**: P: 1 (L5); Pa: 6 (L1, L2, L3, L4, L6, L7); O: 1 (L8); S: 0
- **Req 2 (Hodge decomp+filt)**: P: 1 (L5); Pa: 3 (L6, L8, partials); O: 3 (L3, L4, L7); S: 1 (L1) — **recount**: P 1, Pa 2 (L6, L8), O 3 (L3, L4, L7), S 2 (L1, L2)
- **Req 3 (rational/AH)**: P: 1 (L5); Pa: 6 (L2, L3, L4, L6, L7, L8); O: 0; S: 1 (L1)
- **Req 4 (cl(Z)/Chern)**: P: 1 (L5); Pa: 3 (L4, L6, L7); O: 1 (L8); S: 3 (L1, L2, L3)
- **Req 5 (main assertion)**: P: 0; Pa: 2 (L5, L6); O: 3 (L4, L7, L8); S: 3 (L1, L2, L3)
- **Req 6 (all codim/dim)**: P: 0; Pa: 3 (L4, L5, L6); O: 2 (L7, L8); S: 3 (L1, L2, L3)

Total: 48 cells. SILENT count pre-critic: ~12 (concentrated at L1-L3 upstream infrastructure for Req 4/5/6 — standard centralized-addressing pattern as in YM audit).

Critic pass to follow. Expect critic to:
1. Challenge L5 Req 3 "P" claim (AH may have subtle torsion even on projective bundles — verify)
2. Challenge L6 Pa verdicts (Simpson nonabelian Hodge is Kähler, not projective — scope concern)
3. Challenge L7 Req 6 "O" (should arguably be Pa since BC-motivated class already covers many (p, N))
4. Challenge L4 Req 4 "Pa" (FMS24 may not fully discharge cl(Z)/Chern requirement)

---

*End of author audit-draft.*
