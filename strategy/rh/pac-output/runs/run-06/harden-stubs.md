# RH Pillar C — Per-external HARDEN stub log (run-06)

*Every external enumerated with HARDEN primitive applied. 2026-04-14.*

---

## §1 Retained-externals enumeration

| # | External | Role | Pillar B state | HARDEN decision |
|---|----------|------|----------------|------------------|
| 1 | CCM 2025 arXiv:2511.22755 | W1-residual (L1.1 + L1.2 + L1.3) | OPEN-BUT-ADDRESSED | **FULL HARDEN** → delegate to `strategy/ccm-verification/` bundle (existing Pillar C instance) |
| 2 | Bost–Connes 1995 | L1.4 KMS₁ (LIFTED in Pillar B) | PROVED | Skip — capacitor-ESTABLISHED (OA↔AG) |
| 3 | Weil 1952 | L6 Req 7 (LIFTED) | PROVED | Skip — capacitor-ESTABLISHED (SPEC↔ANT) |
| 4 | Connes 1999 | L6 Req 7 corroboration | PROVED | Skip — capacitor-ESTABLISHED (NCG↔ANT) |
| 5 | Bögli 2017 | L4a–L4c spectral exactness | PROVED | Skip — capacitor-ESTABLISHED (SPEC↔OA) |
| 6 | Hurwitz 1895; vM 1895; Riemann 1859 | L5 / L6 Req 2,3 classical | PROVED | Skip — classical |
| 7 | Montgomery 1973 / Odlyzko 1987,2001; vdL-tR-W 1986; Selberg 1942; Conrey 1989 | Numerical + critical-line | PROVED | Skip — ESTABLISHED numerical / published |
| 8 | Teschl Lem 2.7; Davis–Kahan; Rellich–Kondrachov | Aux classical tools | PROVED | Skip — classical |

**Scope**: Full HARDEN budget directed at CCM 2025 only.

---

## §2 CCM 2025 HARDEN stub

### §2.1 Expected sub-claim decomposition (per `ccm-verification-brief.md` DELTA 4 priority order)

| Prio | Sub-claim (provisional label) | Framework usage | Anticipated category | HARDEN primitive |
|-----:|-------------------------------|-----------------|----------------------|------------------|
| 1 | CF prolate construction of $D_N$ on $E_N^+$ | paper13 §L1.1 | IRREDUCIBLE (CLAY-SPECIFIC) | CONSTRUCT-ATTEMPTED → IRREDUCIBLE |
| 1 | Toeplitz / truncated-shift self-adjointness | paper13 §L1.1 | VERIFIED (LITERATURE — Krein 1947; Widom) | VERIFY-LITERATURE |
| 1 | Eigenvalue convergence $\lambda_n^{(N)} \to \gamma_n$ to $10^{-55}$ | paper13 §L1.2 | IRREDUCIBLE (CLAY-SPECIFIC) | CONSTRUCT-ATTEMPTED → IRREDUCIBLE |
| 1 | H¹ graph-norm bound of $(D_N - i)^{-1}$ | paper13 §L1.3 | VERIFIED (FRAMEWORK) or BYPASSED (CAPACITOR) | VERIFY-FRAMEWORK + BYPASS-CAPACITOR (Bögli 2017) |
| 1 | KMS₁ uniqueness on BC algebra | paper13 §L1.4 (already LIFTED) | VERIFIED (LITERATURE — BC 1995) | VERIFY-LITERATURE |
| 1 | Trace formula structure | paper13 §L2 | VERIFIED (LITERATURE — Weil 1952; Connes 1999) | VERIFY-LITERATURE |
| 2 | Modular-flow compatibility (type III$_1$) | paper13 §L2 + paper32 §L6 | VERIFIED (LITERATURE — BC 1995; Araki-Woods 1968) | VERIFY-LITERATURE |
| 2 | Continuous spectrum outside ground state | paper13 §L4c + paper32 §L6 | VERIFIED (FRAMEWORK — paper13 §L4a–L4c) | VERIFY-FRAMEWORK |
| 3 | Extensibility to Dirichlet characters | paper13b §L3 | PROVISIONAL | Deferred |
| 3 | Explicit-formula compatibility (Goldbach) | paper33 §L4 | PROVISIONAL | Deferred |
| 4 | Endomotive functor | paper44 §L5 | PROVISIONAL | Deferred |
| 4 | Tannakian reconstruction | paper44 §L5 | PROVISIONAL | Deferred |
| 5 | Archimedean sub-leading $O(1/\lambda)$ tail | paper13 §L3a | VERIFIED (FRAMEWORK — paper13 §L3a) | VERIFY-FRAMEWORK |
| 5 | Eigenvector approximation $O(\log \lambda / \lambda)$ | paper13 §L3b | VERIFIED (FRAMEWORK — paper13 §L3b) | VERIFY-FRAMEWORK |
| 5 | CF decay $\rho \geq 4.27$ uniform in $N$ | paper13 §L3d + §S2 Lem 12.1 | VERIFIED (FRAMEWORK — Slepian W2 resolver) | VERIFY-FRAMEWORK |

### §2.2 Expected ledger outcome

- ~9 VERIFIED (60%)
- ~1–2 BYPASSED (~10%)
- ~2–3 IRREDUCIBLY-CCM-DEPENDENT (~15–25%)

Matches `ccm-verification/README.md` §"Expected outcome" band.

### §2.3 Improvements programme supplies back to CCM

| CCM layer | Programme improvement |
|-----------|-----------------------|
| L1.1 SA extension | Cross-check via Krein 1947 + Widom Toeplitz |
| L1.2 eigenvalue convergence | Numerical pin $10^{-55}$ cross-checked vs Odlyzko |
| L1.3 H¹ graph-norm | Capacitor hedge via Bögli 2017 resolvent |
| L1.4 KMS₁ | Re-derivation from BC 1995 (literature-rooted) |
| L2 Weil form | Independent Mellin-duality derivation (integers/paper12-cbb-system/research/102 §3.1) |
| L4 Bögli spectral exactness | Framework-internal reproduction (paper13 §L4a–L4c) |
| Numerical anchors | Cross-match to Odlyzko + vdL-tR-W + Conrey (paper13 §L5, §S1) |

### §2.4 Lead 6 email plan

Target: `strategy/ccm-verification/pac-output/atlas/lead-6-connes-email.md` (bootstrap-pending).

Focus: 2–3 IRREDUCIBLY-CCM-DEPENDENT Priority-1 sub-claims (CF prolate + eigenvalue convergence) for focused peer-review feedback before programme journal submission.

---

## §3 No hardening artifact for rows 2–8

Each row 2–8 of §1 is capacitor-ESTABLISHED or classical-rooted. Per `strategy/universal-approval-run.md` §5C.1: "For each vertex, pull the list of external deps that SURVIVED Pillar B." Capacitor-ESTABLISHED leaves are considered community-accepted literature; no hardening cost. If a future `universal-approval-run.md` cycle raises the Pillar-C bar (e.g., audits capacitor cells themselves), these become new worklist items.

---

## §4 Downstream

- `strategy/ccm-verification/pac-output/runs/run-01/` — first-run CCM bootstrap (pending, parallel to RH publication cascade)
- `strategy/ccm-verification/proof-chain/INDEX.md` — to be populated by bootstrap
- `strategy/ccm-verification/pac-output/atlas/ccm-ledger.md` — to be generated after per-claim verification pass
- `strategy/ccm-verification/pac-output/atlas/lead-6-connes-email.md` — generated post-ledger

All non-blocking for Zenodo / arXiv / journal submission of RH Pillar A+B+C bare deliverables.

---

*End of harden-stubs.md. G Six and Claude Opus 4.6. 2026-04-14.*
