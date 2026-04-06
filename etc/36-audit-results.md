# Appendix Audit Results — April 5, 2026

## Paper 3

| # | Claim | Location in paper | Location of derivation | Status | Action needed |
|---|-------|-------------------|----------------------|--------|---------------|
| 1 | Theorem 9.1 unconditional — horizon vertex factor = 1 (§9.3.2 line 478) | §9.3.2 (inline argument closing Gaps 1-3) | `etc/frontier-research/problem3-horizon-vertex.md` referenced at lines 484, 499 | IN ETC | Create Paper 3 Appendix B (`paper3/16-appendix-b-horizon-vertex.md`). The inline argument in §9.3.2 closes Gaps 1-3 but the product-space vertex factorization proof is only in etc/. |
| 2 | "exact to all orders" for horizon vertex Ward identity (§9.3.2 line 498) | §9.3.2 (brief statement) | Inherits from Theorems K.1, K.3 (Paper 1 App K) | INHERITED | OK as cross-reference. Sufficient — the claim cites Theorems K.1/K.3 explicitly. |
| 3 | Vertex factor "derived" from product structure and Ward identity (App A §A.5.1 line 250) | App A §A.5.1 | `etc/frontier-research/problem3-horizon-vertex.md` referenced at line 254 | IN ETC | Same as #1 — the new Appendix B covers this. Remove etc/ reference from App A. |
| 4 | OS3 reflection positivity "Established to 10⁻⁶⁰" (App A §A.6 lines 321, 334) | App A §A.6 (summary statement only) | `etc/frontier-research/oi3-reflection-positivity.md` referenced at line 322; `etc/frontier-research/problem4-nonpert-completion.md` at line 330 | IN ETC | Create Paper 3 Appendix C or Paper 6 Appendix A for the frozen-dilaton OS3 argument. Currently only summarized, not derived. |
| 5 | Spectral gap "Established (Δ_{5D} >= sqrt5/r_3 > 0)" (App A §A.6 line 336) | App A §A.6 (one-line statement) | `etc/frontier-research/problem4-nonpert-completion.md` | IN ETC | Create Paper 4 Appendix E (`paper4/appendix-E-spectral-gap.md`) with Lichnerowicz derivation. |
| 6 | "Unitarity is proved" (§13 line 48) | §13 conclusion (summary) | §6.4 (Noether theorem) + App A §A.5.2 | IN PAPER | Sufficient — Theorem 6.1 is proved inline via Noether + finiteness. App A confirms at all three layers. No action needed. |
| 7 | Status table: 9 rows marked **Derived** (§13.1 lines 62-71) | §13.1 table | Various sections within Paper 3 (§3, §6, §7, §8, §9, §10, §11) | IN PAPER | Sufficient — each row cites its in-paper section. These are derived from established framework results. No action needed. |
| 8 | "Theorem 9.1 is unconditional" (§13.1 line 87) | §13.1 | `etc/frontier-research/problem3-horizon-vertex.md` referenced at line 78 | IN ETC | Same as #1. The etc/ reference must be replaced with Appendix B reference. |
| 9 | One-loop finiteness "Proved" (App A status table line 93) | App A status table | Paper 1 Appendix F | INHERITED | OK — correctly cites Paper 1 Appendix F. |
| 10 | Two-loop complete vanishing "Proved" (App A line 94) | App A status table | Paper 1 Appendix G | INHERITED | OK — correctly cites Paper 1 Appendix G. |
| 11 | All-orders finiteness "Established" for KK sum factor (App A line 95) | App A status table | Paper 1 Appendix K, Theorem K.1 | INHERITED | OK — correctly cites Paper 1 Appendix K. |
| 12 | Bekenstein-Hawking entropy "derived" (§13 line 31) | §13 conclusion | §8 (inline derivation) | IN PAPER | Sufficient. |
| 13 | Hawking temperature "derived" (§3 line 151) | §3 | §3 inline derivation from Euclidean periodicity | IN PAPER | Sufficient. |

## Paper 4

| # | Claim | Location in paper | Location of derivation | Status | Action needed |
|---|-------|-------------------|----------------------|--------|---------------|
| 14 | Higgs mass naturalness "Established" with Z_{S2}(0) = -2/3 (§6.11 line 350) | §6.11 (summary, 1 paragraph) | `etc/frontier-research/problem2-higgs-mass.md` referenced at lines 350, 372 | IN ETC | Create Paper 4 Appendix D (`paper4/appendix-D-higgs-naturalness.md`). The three-layer protection is stated but the Z_{S2}(0) = -2/3 computation and proof that higher loops vanish is only in etc/. |
| 15 | Status table: "Proved" BPHZ factorization at L >= 3 (§8 line 40) | §8 status table | Paper 1 Appendix K §K.5.3, Theorem K.3 | INHERITED | OK — correctly cites Theorem K.3. |
| 16 | Status table: "Proved" CC underivability Theorem U* (§8 line 43) | §8 status table (one-line) | `etc/frontier-research/problem1-cc-underivability.md` (implied — no explicit reference here but referenced in Paper 7) | IN ETC | Create Paper 7 Appendix A (`paper7/appendix-A-theorem-U-star.md`). Paper 4 table should cross-reference Paper 7. |
| 17 | Status table: "Proved" non-perturbative spectral gap Δ_{5D} (§8 line 44) | §8 status table (one-line) | `etc/frontier-research/problem4-nonpert-completion.md` | IN ETC | Create Paper 4 Appendix E. Same as #5. |
| 18 | Status table: "Established to 10⁻⁶⁰" constructive QFT / OS3 (§8 line 45) | §8 status table | `etc/frontier-research/oi3-reflection-positivity.md` explicitly referenced | IN ETC | Same as #4. etc/ reference must be removed, replaced with appendix reference. |
| 19 | Status table: SLOCC-isometry map "Established (global)" (§8 line 41) | §8 status table | `etc/24-flag-manifold-cohomology.md` referenced as "(etc/24)" | IN ETC | The cohomology computation is in etc/24. Needs in-paper appendix or inline expansion of §5. |
| 20 | Status table: "Proved" S1 decoupled from G4 flux (§8 line 51) | §8 status table | Paper 7 section 2 | IN PAPER (Paper 7) | OK — correctly cites Paper 7 §2. Topological argument (no 4-cycle on S1) is short and stated inline. |
| 21 | Status table: 18 rows marked **Derived** (§8 lines 10-37) | §8 table | Various in-paper sections (§3-§7) | IN PAPER | Sufficient — each row cites its derivation section. Algebra is inline. |
| 22 | "exact to all orders" for V = V_0/phi^4 (§10 conclusion line 69) | §10 conclusion | Paper 1 Appendix S (Epstein zeros) | INHERITED | OK — cross-reference to Paper 1 is correct. |
| 23 | Spectral zeta values Z(-j) "Proved" (App C §C.5.4 line 350) | App C | App C §C.1-C.4 (inline computation) | IN PAPER | Sufficient — the computation is fully inline in Appendix C. |
| 24 | Leading-order alpha_3/alpha_2 "Derived" (App C line 352) | App C | App C §C.5.3 (inline computation) | IN PAPER | Sufficient. |
| 25 | "The gauge coupling hierarchy is derived" (App C line 429) | App C §C.6 | App C inline | IN PAPER | Sufficient. |
| 26 | Perturbative finiteness "proved" (§9.3 line 54) | §9.3 | Paper 1 Theorem S.1 | INHERITED | OK. |
| 27 | Non-perturbative stability "proved" (§9.3 line 66) | §9.3 | Paper 1 Appendix J | INHERITED | OK. |
| 28 | `etc/16-solve-stabilization.py` reference (App C line 294) | App C | etc/ working file (Python script) | IN ETC | Minor — numerical computation script. State result inline, or note "numerical verification" without etc/ path. |
| 29 | `etc/22-three-equation-system.md` reference (App C line 366, §9.5 lines 135,139,159) | App C, §9 | etc/ working file | IN ETC | Minor — regime analysis. The conclusion (kappa is 10^-38 below bifurcation) is stated inline. Remove etc/ path, keep conclusion. |
| 30 | `etc/23-g4-flux-stabilization.md` reference (App C line 410, §9.5 line 176) | App C, §9 | etc/ working file | IN ETC | Minor — superseded by Paper 7 which contains the full flux computation. Replace etc/ refs with Paper 7 cross-references. |
| 31 | `etc/12c-slocc-isometry-calculation.md` reference (§5 line 211) | §5.5 | etc/ working file | IN ETC | The tangent-space calculation should be inline or in an appendix. Currently just referenced. |
| 32 | `etc/24-flag-manifold-cohomology.md` reference (§5 line 247, §9.4 line 100) | §5, §9.4 | etc/ working file | IN ETC | Same as #19 — cohomology computation needs to be in-paper. |
| 33 | `etc/12b-moduli-freezing-analysis.md` reference (§9.1 line 38) | §9.1 | etc/ working file | IN ETC | Minor — superseded by Paper 7. Replace with Paper 7 cross-reference. |
| 34 | `etc/21` bifurcation reference (§9.5 line 132, 196) | §9.5 | etc/ working file | IN ETC | Minor — the conclusion is inline. Remove path. |
| 35 | `etc/09-creative-routes-to-R.md` reference (§7 line 865) | §7 | etc/ working file | IN ETC | Replace with Paper 6/7 cross-reference (dilaton revision). |
| 36 | `etc/07-k-resolution.md` reference (§7 line 686) | §7 | etc/ working file | IN ETC | Minor — numerical result. State inline. |

## Paper 5

| # | Claim | Location in paper | Location of derivation | Status | Action needed |
|---|-------|-------------------|----------------------|--------|---------------|
| 37 | eta_B "Derived" from CP2 Chern-Simons (§1.4 table line 118) | §1.4 status table | §5 (inline) + App D §D.5 | IN PAPER | Sufficient — the parametric derivation is in §5 and numerical solution in App D. |
| 38 | String tension "Derived" (§1.4 table line 116) | §1.4 status table | §3 (inline derivation) | IN PAPER | Sufficient. |
| 39 | Proton mass "Derived" (§1.4 table line 119) | §1.4 table | §6 (inline derivation) | IN PAPER | Sufficient. |
| 40 | Luscher coefficient "derived, not fit" (App B line 84) | App B | App B (inline derivation from CP2 geometry) | IN PAPER | Sufficient. |
| 41 | `etc/frontier-research/oi1-boltzmann-equations.md` reference (App D lines 189, 290) | App D §D.5 | etc/ frontier-research file | IN ETC | The numerical results table IS in App D (sufficient). But the Python code is referenced as being in etc/. Replace the etc/ reference: either include code snippet inline or state "available as supplementary material". |
| 42 | `etc/12b-moduli-freezing-analysis.md` reference (App C line 7) | App C | etc/ working file | IN ETC | Minor — the Cartan-Helgason theorem is standard. Cite the theorem directly, remove etc/ path. |
| 43 | `etc/06-appendix-z-issues.md` reference (§5 line 81) | §5.3 | etc/ working file | IN ETC | Minor — washout parameter discussion. The key result is in App D §D.5. Remove etc/ path. |

## Paper 6

| # | Claim | Location in paper | Location of derivation | Status | Action needed |
|---|-------|-------------------|----------------------|--------|---------------|
| 44 | V = V_0/phi^4 "exact to all orders" (§13 conclusion line 34) | §13 | Paper 1 Appendix S / Appendix G (Epstein zeros) | INHERITED | OK — correctly cross-references Paper 1. |
| 45 | "exact to all orders" for Casimir potential (§3.4 line 88, §10 line 36) | §3.4, §10 | Paper 1 Appendix G | INHERITED | OK. |
| 46 | w_0 = -1 "to 10^-52 precision" from frozen dilaton (§13 line 36) | §13 | Stated inline (epsilon = 8piR/M_Pl^2 ~ 10^-52) | IN PAPER (partial) | The epsilon calculation is inline but the frozen-dilaton argument (WHY delta_R/R_0 < 10^-30) is in `etc/frontier-research/oi3-reflection-positivity.md` §3.2. Needs Paper 6 Appendix A for the dilaton freezing computation. |
| 47 | Dilaton potential "derived" from Casimir energy (§0 abstract line 15, §2 line 6) | §0, §2 | Paper 1 Section 6.6 | INHERITED | OK. |
| 48 | `etc/09-creative-routes-to-R.md` references (§0 line 17, §2 line 68, §3 line 5, §10 line 34) | §0, §2, §3, §10 | etc/ working file | IN ETC | These are revision notes (the Goldberger-Wise correction). The revised physics IS stated inline. Remove etc/ paths — the corrections are already incorporated into the text. |
| 49 | `etc/06-appendix-z-issues.md` reference (§5 line 112) | §5 | etc/ working file | IN ETC | Minor — corrected seesaw parameters. Remove etc/ path. |
| 50 | Dilaton freezing epsilon_eff ~ 10^-52 (§3.1 implied) | §3.1 / §13 | `etc/frontier-research/oi3-reflection-positivity.md` §3.2 | IN ETC | Create Paper 6 Appendix A (`paper6/appendix-A-dilaton-freezing.md`). The computation that the dilaton moves by 10^-52 of its value over a Hubble time is only in etc/. |
| 51 | No appendices exist for Paper 6 | -- | -- | MISSING | Paper 6 has zero appendices. At minimum, Appendix A (dilaton freezing) is needed. Reheating in §4 is qualitative — add explicit caveat if no computation exists. |

## Paper 7

| # | Claim | Location in paper | Location of derivation | Status | Action needed |
|---|-------|-------------------|----------------------|--------|---------------|
| 52 | GVW superpotential W_total "Derived" (§3.5 table line 173) | §3 (full inline derivation §§2-3) | §§2-3 (complete) | IN PAPER | Sufficient — the derivation occupies all of §§2-3 with explicit algebra. |
| 53 | F-flat conditions r_3^2, rho^2 "Derived" (§3.5 lines 174-175) | §3.5 | §3 inline | IN PAPER | Sufficient. |
| 54 | GUT condition n_2/n_1 = -17/9 "Derived" (§3.5 line 176) | §3.5 | §3.4 inline | IN PAPER | Sufficient. |
| 55 | Smallest integers n_1=9, n_2=-17 "Derived" (§3.5 line 177) | §3.5 | §3.4 inline | IN PAPER | Sufficient. |
| 56 | Theorem U — R underivability (§3.6) | §3.6 (complete proof over 100+ lines) | §3.6 inline | IN PAPER | Sufficient — full algebraic proof is in §3.6.1-3.6.4. This is the in-paper version. |
| 57 | Theorem U* — CC underivability extended (§6 "Frontier Results" line 162) | §6 (summary paragraph) | `etc/frontier-research/problem1-cc-underivability.md` referenced at line 164 | IN ETC | Create Paper 7 Appendix A (`paper7/appendix-A-theorem-U-star.md`). Theorem U is proved in-paper (§3.6) but U* (the stronger version with algebraic+non-perturbative+desert bounds) is only in etc/. |
| 58 | Non-perturbative spectral gap Lichnerowicz bound (§6 lines 176-183) | §6 (summary paragraph) | `etc/frontier-research/problem4-nonpert-completion.md` referenced at lines 183, 191 | IN ETC | Create Paper 4 Appendix E (or Paper 7 Appendix B). The Lichnerowicz computation is only in etc/. |
| 59 | Freed-Witten tadpole fully characterized (§4.4, §6 line 96) | §4.4 (detailed summary of results) | `etc/frontier-research/oi2-freed-witten-tadpole.md` referenced at lines 170, 96 | IN ETC | Create Paper 7 Appendix B (`paper7/appendix-B-freed-witten.md`). §4.4 states results but the Diophantine analysis and minimal solutions are in etc/. |
| 60 | Resonant leptogenesis solved (§6 line 106) | §6 (summary) | `etc/frontier-research/oi1-boltzmann-equations.md` referenced at line 107 | IN ETC | Already partially addressed in Paper 5 App D §D.5. But the etc/ reference here in Paper 7 must be replaced with a Paper 5 App D cross-reference. |
| 61 | OS3 reflection positivity open problem (§6 line 191) | §6 | `etc/frontier-research/problem4-nonpert-completion.md` referenced | IN ETC | Same as #4/#18 — needs appendix. Replace etc/ reference. |
| 62 | `etc/23` reference (§2 line 10) | §2.1 | etc/ working file | IN ETC | Minor — the no-scale runaway statement. The corrected computation is now in §§2-3 inline. Remove etc/ path. |
| 63 | "exact to all orders" for w_0 = -1 (§6 line 53) | §6 conclusion | Paper 1 App S | INHERITED | OK. |
| 64 | "established" for Papers 1-6 perturbative sector (§6 line 4) | §6 opening | Papers 1-6 (general summary) | INHERITED | OK — general summary statement. |
| 65 | GUT unification "fully established" (§3.5 line 182) | §3.5 | §§2-3 inline | IN PAPER | Sufficient. |

---

## Summary of etc/frontier-research/ References in Paper Files

| Paper | File | Line(s) | etc/ path referenced |
|-------|------|---------|---------------------|
| Paper 3 | 09-...md | 484, 499 | `etc/frontier-research/problem3-horizon-vertex.md` |
| Paper 3 | 13-conclusion.md | 78 | `etc/frontier-research/problem3-horizon-vertex.md` |
| Paper 3 | 15-appendix-a...md | 254, 322, 329 | `etc/frontier-research/problem3-horizon-vertex.md`, `oi3-reflection-positivity.md`, `problem4-nonpert-completion.md` |
| Paper 4 | 06-...md | 350, 372 | `etc/frontier-research/problem2-higgs-mass.md` |
| Paper 4 | 08-...md | 41, 45 | `etc/24`, `etc/frontier-research/oi3-reflection-positivity.md` |
| Paper 4 | 05-...md | 211, 247 | `etc/12c-...`, `etc/24-...` |
| Paper 4 | 09-...md | 38, 100, 132, 135, 139, 159, 176, 192, 196 | Various etc/ working files |
| Paper 4 | appendix-C...md | 294, 366, 410 | `etc/16-...`, `etc/22-...`, `etc/23-...` |
| Paper 4 | 07-predictions.md | 686, 865 | `etc/07-...`, `etc/09-...` |
| Paper 5 | appendices/appendix-D...md | 189, 290 | `etc/frontier-research/oi1-boltzmann-equations.md` |
| Paper 5 | appendices/appendix-C...md | 7 | `etc/12b-...` |
| Paper 5 | 05-baryon-asymmetry.md | 81 | `etc/06-...` |
| Paper 6 | 00-abstract.md | 17 | `etc/09-...` |
| Paper 6 | 01-introduction.md | 78 | `etc/09` |
| Paper 6 | 02-dilaton-potential.md | 68 | `etc/09-...` |
| Paper 6 | 03-inflation.md | 5 | `etc/09-...` |
| Paper 6 | 05-...md | 112 | `etc/06-...` |
| Paper 6 | 10-...md | 34 | `etc/09-...` |
| Paper 7 | 02-...md | 10 | `etc/23` |
| Paper 7 | 04-tadpole.md | 170 | `etc/frontier-research/oi2-freed-witten-tadpole.md` |
| Paper 7 | 06-conclusion.md | 96, 107, 164, 183, 191 | `etc/frontier-research/oi2-...`, `oi1-...`, `problem1-...`, `problem4-...` |

**Total: 38 etc/ references across Papers 3-7 that must be replaced.**

---

## Summary

**Total claims audited: 65**

- **In-paper (complete): 28** — Full derivation or sufficient inline algebra exists within the paper directory. No action needed.
- **In-paper (partial/referenced only): 1** — #46 (w_0 = -1 precision claim; the epsilon formula is inline but the frozen-dilaton bound is in etc/).
- **In etc/ (need converting to appendix): 24** — Derivations exist in etc/ working files but are not accessible to readers. Seven major new appendices needed plus cleanup of 38 etc/ path references.
- **Inherited from Paper 1-2 (OK as cross-reference): 11** — Correctly cite Paper 1/2 appendices (K, S, F, G, J). No action needed.
- **Missing (need writing from scratch): 1** — #51 (Paper 6 has no appendices at all; dilaton freezing computation needs to be written).

### Required New Appendices (Priority Order)

| Priority | Target file | Source | Claims covered |
|----------|-------------|--------|----------------|
| 1 | `paper3/16-appendix-b-horizon-vertex.md` | `etc/frontier-research/problem3-horizon-vertex.md` | #1, #3, #8 |
| 2 | `paper4/appendix-D-higgs-naturalness.md` | `etc/frontier-research/problem2-higgs-mass.md` | #14 |
| 3 | `paper7/appendix-A-theorem-U-star.md` | `etc/frontier-research/problem1-cc-underivability.md` | #16, #57 |
| 4 | `paper3/17-appendix-c-reflection-positivity.md` (or Paper 6 App A §A.2) | `etc/frontier-research/oi3-reflection-positivity.md` | #4, #18, #61 |
| 5 | `paper4/appendix-E-spectral-gap.md` | `etc/frontier-research/problem4-nonpert-completion.md` | #5, #17, #58 |
| 6 | `paper7/appendix-B-freed-witten.md` | `etc/frontier-research/oi2-freed-witten-tadpole.md` | #59 |
| 7 | `paper5/appendices/appendix-D...md` (cleanup only) | Already done — remove 2 etc/ refs | #41 |
| 8 | `paper6/appendix-A-dilaton-freezing.md` | `etc/frontier-research/oi3-reflection-positivity.md` §3.2 | #46, #50, #51 |

### etc/ Path Cleanup (No New Content, Just Path Removal)

18 additional etc/ references in Papers 4-7 point to working files (`etc/06`, `etc/07`, `etc/09`, `etc/12b`, `etc/12c`, `etc/16`, `etc/21`, `etc/22`, `etc/23`, `etc/24`) whose conclusions are already stated inline. These need their etc/ paths removed and replaced with either:
- Cross-references to Paper 7 (for `etc/23`)
- Inline statements of the result (for `etc/16`, `etc/21`, `etc/22`)
- Standard literature citations (for `etc/12b` Cartan-Helgason)
- "Supplementary material" notes (for Python scripts)
