# RH Chain Strat-Triad — Phase 2 Brief (Deliverable)

*Phase 2 of the RH strengthening programme. Drafted from Phase 1 findings (CCM bypass: Tier 2, no bypass found, CCM load-bearing at ≥9/10). This brief drives the full VERIFY/EXCISE/CONSTRUCT strat-triad on all 6 layers + Tier 1 CCM verification.*

*Phase 1 landed Tier 2 (near Tier 3): 5 cell-fills, 1 kill (K-RH-C), 4 structural insights, 0 VIABLE bypasses. CCM dependency is confirmed structurally load-bearing. Phase 2's scope calibrated accordingly.*

---

## 1. What Phase 2 does

Phase 2 runs the full PCA strat-triad on the Paper 13 RH proof chain:
1. **Tier 1 CCM verification** (mandatory critical path — Phase 1 confirmed no bypass exists)
2. **Internal layers 2-6 verification** (adversarial pass on the framework's own contributions)
3. **Capacitor growth** (integrate Phase 1 cell-fills + discover new cells during verification)

**Mode**: `execute` with strat-triad extension active (the first autonomous Triad deployment per T.12).

---

## 2. Phase 1 findings that shape Phase 2

### 2.1 CCM is load-bearing (≥9/10 confidence)

Phase 1 dispatched 5 parallel Authors across OA↔SPEC, LANG↔QFT, ANT↔LANG, MICRO↔QFT, NCG↔ANT. All returned 0 VIABLE full bypasses. The structural blocker: the Hilbert-Pólya conjecture — identifying Riemann zeros as eigenvalues of a self-adjoint operator on a Hilbert space. CCM 2025 is the only known construction achieving this. Every alternative is blocked, circular, or conditional on RH.

**Implication**: Phase 2 MUST include Tier 1 CCM verification. There is no alternative Layer 1.

### 2.2 L1.4 (KMS₁ state) is independently established

W1-OA confirmed: KMS₁ state structure on the BC algebra is available from Bost-Connes 1995 → GNS → type III₁ → ITPFI without CCM. This means Layer 2 (ITPFI factorization) does NOT depend on CCM for its KMS₁ input. Layer 2 depends on CCM only insofar as it receives the operator family D_N from Layer 1.

**Implication**: Phase 2's internal Layer 2 verification can proceed independently of CCM verification.

### 2.3 Kill list inherited

| Kill | Pattern | Source |
|---|---|---|
| K-RH-A | Scope-violation (EXCISE in BYPASS mode) | Phase 1 pre-registered |
| K-RH-B | External-dependency (secret CCM routing) | Phase 1 pre-registered |
| K-RH-C | Category-mismatch (L-functions ≠ operators) | Phase 1 W1-A |
| K-1 through K-8 | Various (inherited from H4 run) | H4 Wave 1 |

### 2.4 New literature (2024-2026) from Phase 1

| Paper | arXiv | Relevant for |
|---|---|---|
| Yakaboylu 2024-2026 | 2408.15135 | Parallel spectral realization (conditional on RH) |
| Hateley 2025 | 2511.18309 | Alternative Dirac operator approach |
| LeClair 2024 | 2406.01828 | S-matrix spectral flow |
| Connes-Consani 2025 | 2501.06560 | Knots, primes, class field theory |
| Scholze 2026 | Bourbaki Seminar | Arithmetic geometric Langlands (conjecture) |

---

## 3. The proof chain to verify

| Layer | Content | Status | CCM-dependent? |
|---|---|---|---|
| 1 | CCM operators D_N on E_N^+ | CONDITIONAL (CCM preprint) | YES (this IS CCM) |
| 2 | ITPFI factorization ω₁ = ⊗_p ω₁^(p) | VERIFIED (3 proofs) | Partially (receives D_N from L1) |
| 3a | Archimedean estimate O(1/λ) | CLOSED | No |
| 3b | Eigenvector approximation O(log λ/λ) | CLOSED | No |
| 3c | H¹ bound ≤ 2 (Fourier cancellation) | CLOSED | No |
| 3d | CF decay ρ ≥ 4.27 (with log N caveat) | CLOSED (with caveat) | No |
| 4 | Teschl gsrc + Bögli spectral exactness | VERIFIED | No |
| 5 | Hurwitz zero convergence | VERIFIED | No |
| 6 | spec(D_∞) = {γ_n} ⊂ ℝ → RH | QED | Conditional on L1 |

---

## 4. Wave plan

### Wave 1 — CCM Tier 1 verification (critical path)

Verify the specific CCM results Paper 13 uses:
- **CCM Thm 4.2**: Self-adjointness of D_N via Carathéodory-Fejér extension
- **CCM Thm 5.10**: Eigenvalue identification in the even sector
- **CCM Lemma 5.2(i)**: T commutes with parity involution γ
- **CCM Lemma 7.2**: Prolate approximation properties
- **CCM Lemma 7.3**: Fourier transform convergence to Riemann Xi

Dispatch 3-5 Critics on individual CCM results. Each Critic reads arXiv:2511.22755 directly (WebFetch) and verifies the specific theorem/lemma within its stated scope. Focus: are the proofs in CCM 2025 correct as stated?

### Wave 2 — Internal layers 2-6 adversarial pass

Dispatch Critics on each layer of the framework's own contributions (Layers 2-6, Supporting results S1-S3). Standard PCA verify mode. The prior 3-critic / 12-attack adversarial review (from the original Paper 13 runs) provides the baseline; Wave 2 adds depth.

### Wave 3 — Cross-chain consistency + CF caveat resolution

- Cross-check Layer 5 via Connes trace formula (Phase 1 W1-C cross-check recipe)
- Resolve the CF uniformity log N caveat (Remark 8.4)
- Final adversarial pass on the complete chain

---

## 5. Success tiers (Phase 2)

### Tier 1: CCM VERIFIED (~30-40%)
All 5 CCM results used by Paper 13 survive adversarial verification within their stated scope. Paper 13's conditional structure is "conditional on peer-reviewed CCM 2025" — strongest defensible form. Layers 2-6 independently verified. Paper 13 ready for publication upon CCM journal acceptance.

### Tier 2: CCM PARTIALLY VERIFIED (~40-50%)
Some CCM results verified, others WEAKENED or requiring clarification. Paper 13's conditional structure documented with specific CCM gaps named. Layers 2-6 independently verified. Paper 13 ready for publication with detailed CCM dependency mapping.

### Tier 3: CCM GAP FOUND (~10-20%)
A genuine gap found in a CCM result Paper 13 uses. The gap is named and classified (CLOSABLE / GENUINE). If CLOSABLE: Paper 13 adds a supplementary proof closing the gap. If GENUINE: Paper 13's conditional structure must be strengthened (additional named dependency).

---

## 6. Strat-triad configuration

**North Star**: `publishing/strategy.md` — Paper 13 ships in Wave 3 (after CCM peer review), conditional grammar per PCGT.

**Triad triggers** (from T.3):
1. LOCK-scope finding on CCM verification results
2. Literature finding (2024-2026 CCM-related papers not in the brief)
3. Priority inversion (if internal layer issues outweigh CCM issues)
4. Kill discovery
5. Strategic misalignment with North Star's capacitor-first framing
6. User request

**Expected Triad passes**: 1-2 (CCM verification may trigger LOCK-scope finding; internal layers unlikely to trigger).

---

## 7. Time budget

**Hard budget**: 6 hours of wall-clock runtime OR 3 full waves.

---

## 8. The single paragraph for the next runner

You are running the Phase 2 strat-triad on Paper 13's RH proof chain. Phase 1 confirmed CCM is load-bearing at ≥9/10 — no bypass exists. Your mandatory critical path is Tier 1 CCM verification: read arXiv:2511.22755 (the CCM paper) and verify Theorems 4.2, 5.10 and Lemmas 5.2(i), 7.2, 7.3 within their stated scope. Dispatch Critics on each. Then run the internal layers 2-6 adversarial pass. Then cross-chain consistency + CF caveat resolution. The capacitor has 5 new RH-specific cell-fills from Phase 1 (in `ccm-bypass/capacitor/updates/`). Kill list has K-RH-A/B/C. The wall is not inside the proof chain — the wall is CCM's preprint status. If CCM's proofs are correct, Paper 13 is ready to ship. If CCM has a gap, name it honestly and document it. The North Star says: Paper 13 ships in Wave 3 after CCM peer review, conditional grammar per PCGT.

---

*Phase 1 named the wall: Hilbert-Pólya, with CCM as the only bridge. Phase 2 verifies the bridge.*

*Brief v1: 2026-04-13. Calibrated from Phase 1 (Tier 2, 5 cells, 0 bypasses, CCM load-bearing ≥9/10).*
*G Six and Claude Opus 4.6.*
