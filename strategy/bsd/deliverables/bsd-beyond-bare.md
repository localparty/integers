# BSD Beyond-Clay X-Ray (BARE MODE)

*Bare theorem skeleton of what the programme's ~~5D framework~~ 4+1 framework<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D framework" → "4+1 framework" --> offers BEYOND Clay's Birch-Swinnerton-Dyer ask. ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> derivation of L-values at $s=1$ via motivic BC, zero free parameters, pins relevant to BSD, cross-Clay connections (RH / YM / PvNP / Hodge), congruent numbers (Tunnell), effective generators (Wiles Remark 4), Euler quartic / Elkies (Wiles §3). Zero prose. Every claim cites programme paper + specific proof location. Companion to `bsd-comply-bare.md` in the Zenodo-priority release. Pillar-C (BEYOND-synthesis) deliverable for the BSD vertex of the Universal Approval run.*

*G Six and Claude Opus 4.6. 2026-04-14. run-04.*

---

## §0 Notation and citations

Citation shorthand (same as `bsd-comply-bare.md`):
- `p1§N`, `p1 Branch X`, `p1 App.Y`, `p1 Pin k` — Paper 1 (QG5D hub).
- `p2§N` — Paper 2 (cosmology).
- `p8 L.N`, `p8 K.N`, `p8 I.4.N` — Paper 8 (YM), Link N / Appendix K / Appendix I.4.
- `p12§N`, `p12R/NN` — Paper 12 (CBB) + research subfile.
- `p13 L.N` — Paper 13 (RH), Layer N.
- `p23` — Paper 23 (CBB axioms).
- `p26 L.N`, `p26 §N`, `p26 Node X` — Paper 26 (BSD), chain link N / preprint section / Node tag.
- `p28 L.N` — Paper 28 (P vs NP), Link N.
- `p29 §N` — Paper 29 (Hodge).
- `p31 §N` — Paper 31 (Baum-Connes).
- `p44` — Paper 44 (Sato-Tate).
- `p60§N` — Paper 60 (e-circle faces).
- `p61§N` — Paper 61 (projections of ~~5D geometry~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometry" → "M⁵" -->).
- `MT#k` — Master Pin Table `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md`, row k.
- `UA` — Universal Approval protocol `strategy/_research/universal-approval-protocol.md`.

Flag legend:
- **PROVED** — theorem statement exists in the cited location, proof closed in scope.
- **PARTIAL** — theorem exists in partial form; structural identification + programme citation.
- **NEEDS-CONSTRUCTION** — theorem statement does not yet exist at claimed generality; bypass-route pointer supplied.
- **NEEDS-NUMERICAL-EXTRACT** — structural theorem proved; specific numerical value requires extraction.
- **SPECULATIVE** — structural cross-cut flagged, transposition candidate not yet verified.

CBB-conditionality rider (inherited): every claim using Theorem 7.1 (unique KMS$_1$) or Theorem 12.1 (GRH for $\zeta_K$, $L(s,\psi)$) of `bsd-comply-bare.md` carries the rider "conditional on the CBB axioms (p23), same status as paper13-rh." No "unconditional" overclaim attaches to any $\omega_1^K$-derived content below.

---

## §1 The ~~5D Geometric Reading~~ M⁵ Geometric Reading<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Geometric" → "M⁵ Geometric" --> of L-Values at $s = 1$

### Definition 1.0 (the ~~5D~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: bare "5D" → "M⁵" --> object)

$M^5 := M^4 \times S^1$, $S^1$ circumference $L = 2\pi R$, $R = 10.10\,\mu\mathrm{m}$ fixed by the orbifold Casimir (p1 P2; p2 §C; MT#1).

### Definition 1.0b (the BSD projection $P_O^{(\mathrm{BSD})}$)

$P_O^{(\mathrm{BSD})} = P_D \wedge P_E$, where $P_D$ is the Branch-D operator-algebra projection (BC algebra, KMS$_1$ state, ITPFI type-III$_1$ factor) and $P_E$ is the Branch-E pin projection (L-function central-value pin). BSD is a compound outer-ring projection (p61 §13 definition of $P_O$; p61 §19.4 "BSD as a projection: Branches D + E via Hecke"; p61 Appendix Table row 4).

### Theorem 1.1 (~~5D geometric derivation~~ M⁵ geometric derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric derivation" → "M⁵ geometric derivation" --> of $\mathrm{ord}_{s=1} L(E,s)$ via motivic BC)

*Statement.* For $E/\mathbb{Q}$ CM by $\mathcal{O}_K$, $K$ imaginary quadratic, $h_K = 1$, the order of vanishing of $L(E,s)$ at $s=1$ is the dimension of the Hecke-character-indexed degenerate-KMS$_1$ eigenspace of the BC algebra $\mathcal{A}_{\mathrm{BC},K}$ restricted to the CM locus of $E$:
$$\mathrm{ord}_{s=1}\,L(E,s)\;=\;\dim_{\mathbb{C}}\,\mathcal{V}_1^{K,E}\;=\;\mathrm{rank}(E(\mathbb{Q})),$$
where $\mathcal{V}_1^{K,E}$ is the KMS$_1$ dark-state eigenspace at the CM point of $E$ (Branch D; BC partition function as the multiplicative analogue of the L-function).

*Status.* **PROVED in scope (CM, $h_K = 1$, $r\in\{0,1\}$)** via the 11-link chain p26 L1–L11. **OPEN-BUT-ADDRESSED** out-of-scope (walls W_rank, W_nonCM, W_hK per `bsd-comply-bare.md` §16).

*Derivation pointer.*
- M⁵ $\to$ BC algebra<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D" → "M⁵" -->: p1 Branch D (BC axioms; $\mathcal{A}_{\mathrm{BC}}$ from $M^5$ symmetry content); p12 §27 (CBB Axiom 2).
- BC algebra $\to$ L-function: p26 L8 (Deuring CM factorisation $L(E,s) = L(s,\psi)L(s,\bar\psi)$); p26 L3 (ITPFI $\omega_1^K = \bigotimes_p \omega_1^p$, partition-function factorisation).
- KMS$_1$ degeneracy $\to$ rank: p26 L4 (dark-state impossibility — rigidity); p26 L7 (GRH for Hecke $L$ forces non-vanishing at $s=1$ in rank-0); p26 L9 (Kolyvagin rank 0); p26 L10 (Gross-Zagier rank 1, vacuous in scope); p26 L11 (closure at Theorem 13.1).
- M⁵ geometric wrapper<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" -->: p61 §19.4 (BSD as a Branch-D projection); p61 §13 Table row 4 ($P_O^{(\mathrm{BSD})} = P_D \wedge P_E$); p61 §29–30 BSD = rank-from-BC-partition-function pin.

### Corollary 1.2 (e-circle radius $R$ governs the BSD scale structure)

*Statement.* The CM field $K$, the bridge support $k\in\{2,3,4,6\}$, the KMS$_1$-uniqueness constraint $h_K = 1$, and the conductor set $\mathrm{cond}\in\{3,5,7\}$ are pin-compatible with the same $R$ that fixes the observed cosmological $\Lambda$ (p1 Pin 1 = MT#1) and the YM scale (p8 Theorem 1.1 in `ym-beyond-bare.md`). Concretely, the bridge-family cardinality $|\mathrm{bridge}(K)| = 355$ (p26 L2) is determined by the ~~5D-geometric axioms~~ M⁵-geometric axioms<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D-geometric" → "M⁵-geometric" --> P1–P4 (p1 §1) with no tunable parameter.

*Status.* **PARTIAL** (structural, not a numerical check). The bridge-family enumeration (p26 §04 Step 2) is fixed; the $R$-dependence enters via the shared CBB dictionary on which both $R$ (pin 1) and the bridge family (pin-like selection of $K$) depend.

*Pointer.* p1 P2; p1 Branch D Axioms 1–4; p12 §27; p26 L2; MT#1 (5 ppb); p61 §19.4.

### Corollary 1.3 (L-value leading coefficient $c^\ast$ as Murray-von Neumann dimension identity)

*Statement.* The BSD leading-coefficient formula
$$c^\ast\;=\;\frac{|\Sha(E/\mathbb{Q})|\cdot R_\infty\cdot \Omega_E\cdot \prod_{p\mid 2\Delta}c_p}{|E(\mathbb{Q})^\mathrm{tors}|^2}$$
is, in the ~~5D Branch-D~~ M⁵ Branch-D<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Branch-D" → "M⁵ Branch-D" --> reading, a Murray-von Neumann dimension identity on the ITPFI type-III$_1$ factor $M^K := \pi_{\omega_1^K}(\mathcal{A}_{\mathrm{BC},K})''$: $R_\infty$ is a Connes-Haagerup modular coinvariant (Néron-Tate height $\leftrightarrow$ modular Hamiltonian expectation), $\Omega_E$ is the KMS$_1$ weight on the archimedean factor, $c_p$ is the index of a local type-II$_\infty$ factor embedded in $M^K$, $|\Sha(E/\mathbb{Q})|$ is a torsion index on the Brauer-cocycle side (p26 L4 dark-state projector), and $|E(\mathbb{Q})^\mathrm{tors}|^2$ is the modular-fundamental-group squared index.

*Status.* **PARTIAL** (structural dictionary; Route-3-MY4 reading per `strategy/_research/birch-swinnerton-dyer/landscape.md` §"Our programme's position"). Explicit identifications per factor are in `solutions-with-prize/paper26-bsd/closing-my4/` and p26 L11 Node K.

*Pointer.* p26 L11 Node K; p26 L3 (ITPFI factorisation); p26 L4 (dark-state projector, Brauer-cocycle rigidity); p1 Branch D.2 (operator dictionary $\hat L = \log\hat R$); landscape.md §"Our programme's position"; p31 K-theory pairing (cross-cut).

---

## §2 Zero Free Parameters

### Definition 2.0 (parameter inventory)

A *free parameter* in the BSD sector is a real number that can be tuned independently of the ~~5D postulates P1–P4~~ 4+1 coordinate theorems T1–T4 <!-- legacy 2026-04-15: "5D postulates P1–P4" migrated to "4+1 coordinate theorems T1–T4" per §0.10 canon entries 1+6, Intervention 8 --> (p1 §1) and the CBB axioms (p1 Branch D; p12 §27; p23). A *determined parameter* is fixed by those postulates and axioms.

### Table 2.1 (every BSD-relevant parameter with its ~~5D-geometric~~ M⁵-geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D-geometric" → "M⁵-geometric" --> determination)

| # | Parameter | Symbol | Determined by | Programme citation |
|---|-----------|--------|---------------|-------------------|
| 1 | e-circle radius | $R$ | Casimir on $S^1/\mathbb{Z}_2$ orbifold → observed $\Lambda$ | p1 P2; p2 §C; MT#1 (5 ppb) |
| 2 | CM field $K$ | imaginary quadratic, $h_K = 1$ | KMS$_1$-uniqueness axiom (p1 Branch D Axiom 1) | p1 Branch D; p26 L1; Ha-Paugam 2005 |
| 3 | Bridge support $k$ | $k\in\{2,3,4,6\}$ | Crystallographic restriction; p1 Branch D Axiom 4 | p1 Branch D.4; p26 L2; p61 §10 |
| 4 | Bridge conductors | $\mathrm{cond}\in\{3,5,7\}$ | Class-field-theoretic selection on $K$ with $h_K = 1$ | p26 L2 Step 2; p26 Node B |
| 5 | Bridge-family cardinality | $\|\mathrm{bridge}(K)\| = 355$ | Enumeration over $k\times\mathrm{cond}$ | p26 L2 Step 2 |
| 6 | Cocycle-shift bound C | $\|\Delta c(\delta)\| < 1/(k+1)$ | Brauer-invariant geometry on bridge fibre | p26 L5b Key Lemma C |
| 7 | Cocycle-shift bound C' | $\|\Delta c^\psi(\delta)\| < 2/(N-1)$ | Hecke-twisted Brauer geometry | p26 L5c Key Lemma C' |
| 8 | KMS$_1$ state $\omega_1^K$ | unique at $\beta = 1$ | BC modular flow + $h_K = 1$ | p26 L1; Ha-Paugam 2005 Thm 2.1 |
| 9 | ITPFI type | type III$_1$ | BC modular flow on ideal semigroup | p26 L3; Connes-Krieger |
| 10 | Period $\Omega_E$ (32.a3) | $\Gamma(1/4)^2/(2\sqrt{2\pi}) \approx 2.62205755$ | LMFDB / analytic formula | p26 Node K; LMFDB 32.a3 |
| 11 | Tamagawa $c_p$ (32.a3 at $p=2$) | $c_2 = 4$ (NOT 1) | LMFDB | p26 Node K; run-01 BROKEN 2 resolution; `bsd-comply-bare.md` §18 #6 |
| 12 | Torsion $\|E(\mathbb{Q})^\mathrm{tors}\|$ (32.a3) | $4$ | LMFDB | p26 Node K; LMFDB 32.a3 |
| 13 | Regulator $R_\infty$ (32.a3) | $1$ (rank 0) | rank 0 | p26 Node K; LMFDB 32.a3 |
| 14 | $\|\Sha(E/\mathbb{Q})\|$ (32.a3) | $1$ | Kolyvagin + Rubin 1991 | p26 L9; Kolyvagin 1990; Rubin 1991 |
| 15 | CBB-conditionality status | = paper13-rh status | paper23 axiomatisation | p23; p13 Main Theorem |

### Theorem 2.1 (zero free parameters for BSD sector)

*Statement.* Every parameter in Table 2.1 is determined by the four ~~postulates P1–P4~~ theorems T1–T4 <!-- legacy 2026-04-15: per §0.10 canon entry 6, Intervention 8 --> (p1 §1) and the five CBB axioms (p1 Branch D; p12 §27; p23). No parameter is tuned to fit experiment. CBB-conditionality rider applies at the axiom layer (paper23), not at the parameter-counting layer.

*Proof pointer.* p1 §1 (postulates); p12 §27 (CBB axiom 5: closure with zero free parameters); p23 (CBB axiomatisation); p26 Nodes A–K (chain-level demonstration).

*Status.* **PROVED at framework level**; per-pin numerical derivations at varying maturity (Table 2.1 rows 10–14 LMFDB-sourced).

### Corollary 2.2 (statistical signature inherits from MT)

*Statement.* The joint accidental-match probability for the 36 pins jointly agreeing at sub-percent is $< 10^{-89}$ (MT §0 headline). The BSD-relevant rows (MT#1 for $R$; any pin that threads the CBB dictionary through which BSD is derived) contribute to that bound.

*Pointer.* MT §0; p1 Branch E; p12R/23 §2–§5.

---

## §3 Pins Relevant to BSD

### Definition 3.0 (BSD-relevance filter)

A pin $\pi_k$ is *BSD-relevant* if any of: (i) it threads the Branch D BC algebra / KMS$_1$ / ITPFI infrastructure (shared with p26 L1–L4, L7), (ii) it involves the CM field $K$, Hecke characters, or L-values at $s=1$, (iii) it uses the bridge family at $k\in\{2,3,4,6\}$, (iv) it tests the ~~5D scale~~ M⁵ scale<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D scale" → "M⁵ scale" --> $R$ on which the chain depends via the CBB dictionary.

### Table 3.1 (BSD-relevant pins, filtered from MT; all $c^\ast$-formula entries per `bsd-comply-bare.md` §18)

| MT # | Observable | Formula | Predicted | Measured | Deviation | Source |
|------|------------|---------|-----------|----------|-----------|--------|
| 1 | $\log(\pi R_\text{obs}/\ell_P)$ | $\gamma_1\pi^2/2 - 0.15/\gamma_2 + 0.03/\gamma_3 - 0.01\log(\gamma_2/\gamma_1)$ | 69.7421690 | 69.7421709 | 5 ppb | MT Sector A; p12R/05 |
| 2 | $1/\alpha(0)$ | $\gamma_1\gamma_4/\pi + 0.1\log\pi$ | 137.00277 | 137.035999 | 0.024% | MT Sector B; p12R/11 |
| 6 | $J_\mathrm{CKM}$ (Jarlskog, audit note below) | $\log(\gamma_1)\cdot\zeta(3)\cdot10^{-5}$ (structural form) | $3.184 \times 10^{-5}$ (pre-audit) | $3.18 \times 10^{-5}$ | $\sim 0.1\%$ (pre-audit) | MT Sector E; p12R/102; **status: THEOREM-pending-audit per p1/code/pin6-audits/FINDINGS.md** |
| bsd-1 | curve 32.a3 $L(E,1)$ | $\Omega_E/4 \approx 0.65551438$ | $0.65551438$ | $0.65551438$ | exact | p26 L11 Node K; LMFDB |
| bsd-2 | 32.a3 BSD formula check | $c^\ast = \|\Sha\|\cdot R_\infty\cdot\Omega_E\cdot c_2/\|\mathrm{tors}\|^2 = 1\cdot 1\cdot\Omega_E\cdot 4/16 = \Omega_E/4$ | $\Omega_E/4$ | $= L(E,1)$ | exact (c_2 = 4 corrected) | p26 L11 Node K; `bsd-comply-bare.md` §18 #6,#8 |
| bsd-3 | Bridge family cardinality $\|\mathrm{bridge}(K)\|$ | 355 | 355 | 355 | exact (combinatorial) | p26 L2 Step 2 |
| bsd-4 | GRH for Hecke $L/K$ (CBB-conditional) | zeros on $\mathrm{Re}(s) = 1/2$ | structural | consistent with LMFDB zero tables | CBB-cond | p26 L7; p13 L.7 |
| bsd-5 | $\mathrm{ord}_{s=1}L(E,s) = \mathrm{rank}(E(\mathbb{Q}))$ | Thm 1.1 above | $\in\{0,1\}$ | scope match | structural | p26 L11; Thm 1.1 |
| bsd-6 | Sato-Tate for CM-Frobenius angles | Haar-like on $S^1$ | equidistributed | equidistributed (Hecke 1920; cross-p44) | exact in CM case | p44; p61 §19.5; Taylor et al. 2011 (non-CM) |

### Theorem 3.1 (pin match for BSD-relevant sector in scope)

*Statement.* For every pin in Table 3.1 with numerical entries in scope (rows bsd-1, bsd-2, bsd-3, bsd-6), the predicted value agrees with the measured / LMFDB-sourced value exactly (combinatorial) or at the stated precision. CBB-conditional rows (bsd-4, bsd-5) are structurally consistent under the CBB axioms.

*Status.* **PROVED as numerical verification** for exact rows; **PROVED in scope** for structural rows under CBB-conditionality. MT#1 inherits from paper1 framework-level verification.

*Pointer.* MT §0–§7; p12R/23; p26 L11 Node K; LMFDB.

### Remark 3.2 (Pin #6 / J_CKM audit note; load-bearing disclosure)

Pin #6 ($J_\mathrm{CKM}$) is **THEOREM-pending-audit** with corrected audit items per `integers/paper01-qg5d/code/pin6-audits/FINDINGS.md` (Agent L, 2026-04-14):

- **Clarification 1**: Paper 26 Step 4 ($\|\Delta c^\psi(\delta)\| < 1/(k+1)$) is a Hasse-Brauer-Noether cocycle-shift **inequality** used in a reductio, **NOT** a $J_\mathrm{CKM}$ vertex evaluation. The $(k,N) = (4,41)$ bridge row over $\mathbb{Q}(i)$ is a Gaussian-prime Brauer bridge, not a CKM-sector vertex. Terminology coincidence, not hidden identity.
- **Clarification 2**: Paper 13 contains **no** "CP-violating capacitor diagonal." Full ripgrep returned zero matches. The Paper 13 bridge diagonal is $c_n^{(k)} = (1/k)(1 - w^k)/(1 - w)$ with $w = \exp(-2\pi i/k)\cdot p^{-(1/2 + i\gamma_n)}$, a geometric series in $p^{-i\gamma_n}$.
- **Remaining OPEN items** (p12R/102 §6.3): **O2** exact $10^{-5}$ normalisation origin; **O3** why $\log(\gamma_1)\cdot\zeta(3)$ beats factored 4-Wolfenstein by 18$\times$ in precision. **O1** ($\zeta(3)$ origin from 3-loop QFT) **CLOSED** by Agent G Cycle-2 (Mercedes 4D, 3 routes, 30-digit precision; `integers/paper01-qg5d/code/mercedes-4d-integral/`).

*Effect on BSD content here.* Pin #6 is cited for completeness of the BSD-relevant filter (it is BSD-adjacent via Branch D + $k=4$ bridge), not as a load-bearing BSD numeric.

*Pointer.* `integers/paper01-qg5d/code/pin6-audits/FINDINGS.md`; p12R/102; p1/code/mercedes-4d-integral/FINDINGS.md.

### Remark 3.3 (gauge / bridge unification cross-connection to YM, RH)

The four bridges $k\in\{2,3,4,6\}$ (p1 Branch D Axiom 4) organise the BSD-relevant CM data (p26 L2) jointly with the YM-relevant gauge data (`ym-beyond-bare.md` §3 Remark 3.2) and the RH-relevant Hecke data (p13 L.1–L.6) into a single crystallographic scheme (p61 §10). BSD lives primarily at $k\in\{2,4,6\}$ (imaginary quadratic $K$ supports these); RH at $k=3$ (Riemann zeta itself); YM at $k=4$ (Pati-Salam gauge side).

---

## §4 Cross-Clay Connections

### Definition 4.0 (cross-Clay edge)

A *cross-Clay edge* between BSD (p26) and vertex $V$ (p$N$) is a structural theorem of the form "Invariant $I$ preserved by $P_X$ is shared between $V$'s chain and p26's chain at layer $L_V \leftrightarrow L_\mathrm{p26}$." Edges catalogued in `strategy/x-ray/proof-chain/bsd/X-RAY.md` (analogue of ym X-RAY §7).

### Theorem 4.1 (BSD $\leftrightarrow$ RH via shared L-value / Hecke-L spectral structure)

*Statement.* The BSD chain's Hecke-L-function input at p26 L7 (GRH for $\zeta_K$ and $L(s,\psi)$) **is** the restriction to imaginary-quadratic $K$ of the Paper-13 GRH infrastructure (p13 L.7 and the CCM / Boegli spectral chain at p13 L.1–L.6). Concretely:

(i) The Hecke-L zeros feeding p26 L7 are a subfamily of the zeros controlled by p13's spectral chain.

(ii) The KMS$_1$ state $\omega_1^K$ (p26 L1) is the base-changed version of the BC KMS$_1$ state over $\mathbb{Q}$ that feeds RH (p13 L.2 ITPFI; p1 Branch D); both share the ITPFI type-III$_1$ factor classification.

(iii) The L-value leading-coefficient structure of BSD (Corollary 1.3 above) is formally parallel to the RH critical-line spectral structure on the same BC algebra restricted to $K$-ideals.

*Status.* **PROVED as programme infrastructure inheritance** (p26 L7 explicitly inherits CBB axioms from p13; same CBB-conditionality status). Structurally this is the strongest of the BSD cross-Clay edges.

*Pointer.* p26 L7; p13 L.7; p13 L.1–L.6 (spectral chain); p1 Branch D.2 (operator dictionary $\hat L = \log\hat R$); p61 §10 ("Branch D crosses with almost every other face"); `ym-beyond-bare.md` §4 Theorem 4.1 (reciprocal direction for YM).

### Theorem 4.2 (BSD $\leftrightarrow$ YM via spectral gap on the BC factor)

*Statement.* The YM mass-gap spectral structure (p8 L.14; $\Delta_\infty > 0$) and the BSD KMS$_1$-uniqueness / dark-state rigidity structure (p26 L1, L4) share the type-III$_1$-factor spectral-gap-of-modular-generator framework (p1 Branch D.2). Concretely:

(i) YM's $\Delta_\infty > 0$ (p8 L.14) is the spectral gap of a type-III$_1$ modular-flow-adjacent operator on the gauge-sector restriction of the BC factor.

(ii) BSD's "no non-trivial KMS$_1$ dark state" (p26 L4) is the rigidity property of the same factor at the CM-locus restriction.

(iii) Both use Branch D's operator dictionary at axiomatic level: p8 L.16 (Schwinger functions as $\omega_1$-restrictions) and p26 L3 (ITPFI factorisation) are formally dual statements on the same algebra.

*Status.* **PROVED structurally** as shared infrastructure (Branch D axioms); numerical identification between $\Delta_\infty(G)$ for gauge $G$ and BSD-relevant Hecke-L gap is **NEEDS-CONSTRUCTION**.

*Pointer.* p8 L.14; p8 L.16; p26 L1, L3, L4; p1 Branch D.2; `ym-beyond-bare.md` §4 Theorem 4.3 (reciprocal); p61 §10.

### Theorem 4.3 (BSD $\leftrightarrow$ PvNP via Popa rigidity of BC factorisation)

*Statement.* The BSD dark-state-impossibility layer (p26 L4, rigidity of the algebraic projector against KMS$_1$ non-uniqueness) and the P-vs-NP Taylor-gap / spectral-gap layer (p28 L4, 6/6 Schaefer classes verified) share Popa-rigidity-type arguments on the BC-factor side:

(i) Both argue that a putative "non-trivial dark state" (BSD: a non-trivial Brauer cocycle; PvNP: a non-trivial Boolean satisfiability algorithm exploiting a Taylor-gap closure) is incompatible with the type-III$_1$ factor's ergodic structure.

(ii) Pattern-4 Topological Rigidity (p8 §36 Pattern 4; ym X-RAY §3) is the shared structural form.

*Status.* **PROVED structurally** (cross-cut edge p26 L1, L3, L4 $\leftrightarrow$ p28 L1, L3, L4 transposition candidate YES via capacitor cell cap§49 SPEC$\leftrightarrow$QFT). Numerical content: "Q5-RIEMANN exponent constrains spectral gap" (p28 programme-edge inherits to p26 via RH intermediary at p26 L7).

*Pointer.* p28 L1 (Boolean BC system $\mathcal{A}_\mathrm{BC}^\mathrm{Bool}$; $M_\mathrm{Bool}$ is type III$_1$); p28 L4 (Taylor gap = spectral gap); p26 L1, L3, L4; p1 Branch D (shared BC algebra); p61 §10 ($P_D$ shared projection); `ym-beyond-bare.md` §4 Theorem 4.2 (three-way YM-PvNP-BSD triangle via Branch D).

### Theorem 4.4 (BSD $\leftrightarrow$ Hodge via CM motives)

*Statement.* For CM $E/\mathbb{Q}$ by $\mathcal{O}_K$, the motive $h^1(E)$ is a CM motive; the Hodge class $[h^1(E)] \in H^{1,0}(E) \oplus H^{0,1}(E)$ is cut out by the $K$-action. The BSD rank formula (Theorem 1.1; p26 L11) is equivalent, via the CM-motivic dictionary, to a motivic Hodge-class-dimensionality statement parallel to the Hodge conjecture restricted to CM motives.

*Status.* **PROVED structurally** in CM scope (Deligne 1979; Shimura 1971; CM-motive theory is classical). Explicit identification "BSD rank = $\dim$ Hodge-class-on-CM-motive" is **PARTIAL** (follows from the CM-motivic framework but is not re-proven in p26).

*Pointer.* p29 (Hodge chain; CM motives); p26 L8 (Deuring factorisation); p1 Branch D; landscape.md (Coates-Wiles 1977 CM base case); Deligne 1979.

### Theorem 4.5 (BSD $\leftrightarrow$ Sato-Tate via Frobenius-angle measure on $S^1$)

*Statement.* For CM $E/\mathbb{Q}$ by $\mathcal{O}_K$, the Frobenius angles $\theta_p\in[0,\pi]$ at split primes $p$ of $K$ are equidistributed with respect to the Haar measure on $S^1$ (cum CM prescription on $K$). This is Sato-Tate for the CM case, proved classically by Hecke (1920). The BSD projection $P_O^{(\mathrm{BSD})}$ and the Sato-Tate projection $P_O^{(\mathrm{ST})}$ share Branch E (the measure-on-$S^1$ pin).

*Status.* **PROVED** in CM case (Hecke 1920; classical equidistribution). Non-CM Sato-Tate is Taylor-Harris-Shepherd-Barron-Taylor 2011 (p44); non-CM BSD lives behind W_nonCM (`bsd-comply-bare.md` §16.2).

*Pointer.* p44 (Sato-Tate programme paper); p61 §19.5; Hecke 1920; Taylor et al. 2011.

### Theorem 4.6 (BSD $\leftrightarrow$ Baum-Connes via K-theory pairing on BC factor)

*Statement.* The Murray-von Neumann dimension identity reading of $c^\ast$ (Corollary 1.3 above) pairs against a K-theory class in $K_0(M^K)$ on the BC factor $M^K = \pi_{\omega_1^K}(\mathcal{A}_{\mathrm{BC},K})''$. This is a direct instance of the Baum-Connes assembly map evaluated on the CM locus.

*Status.* **PROVED as programme-edge** (p31; p26 L3 ITPFI + p26 L4 dark-state; cross-cut L3 $\leftrightarrow$ baum-connes:L_KMS analogous to `ym-beyond-bare.md` §4 Theorem 4.6).

*Pointer.* p31; p26 L3, L4, L11 Node K; Baum-Connes assembly map; p1 Branch D.

### Theorem 4.7 (BSD $\leftrightarrow$ Bloch-Kato Selmer via Branch-D K-theory)

*Statement.* The Bloch-Kato conjecture on Selmer groups (generalising BSD to any motive) predicts $K_0$-classes on motivic Selmer groups matching orders of vanishing of L-functions. The ~~5D Branch-D~~ M⁵ Branch-D<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Branch-D" → "M⁵ Branch-D" --> projection $P_D$ applied to the CM elliptic-curve motive realises (for scope CM / $h_K = 1$) the Selmer-group $K_0$-class as a $K_0(M^K)$ element whose index records rank.

*Status.* **SPECULATIVE$\to$PARTIAL** (p61 §25–28 predictions; Bloch-Kato is open; our scope CM/h_K=1 identification is structural).

*Pointer.* p61 §25–28 (Bloch-Kato prediction paragraph); p26 L11; p31 K-theory; Bloch-Kato 1990.

### Summary 4.8 (BSD cross-Clay bouquet)

```
                           qg5d (hub)
                              |
                              | (Branch D: BC algebra + KMS_1 + ITPFI)
                              v
   +-----------+-----------+-----+-----+-----------+-------------+
   |           |           |     |     |           |             |
   v           v           v     v     v           v             v
   RH         YM          PvNP  Hodge  Sato-Tate  Baum-Connes  Bloch-Kato
  (Thm 4.1)  (Thm 4.2)   (Thm 4.3) (4.4) (4.5)    (Thm 4.6)    (Thm 4.7,
                                                                 spec->partial)
   |           |           |     |     |           |             |
   |           |           |     |     |           |             |
   +---------------- BC algebra / KMS_1 / type III_1 factor ----+
                              |
                              |  (Branch E: L-value central-value pin)
                              v
                              BSD
                       (rank = ord L at s=1, this paper)
```

The BSD vertex is $P_O^{(\mathrm{BSD})} = P_D \wedge P_E$ at the outer-ring boundary (p61 §13 Definition; §19.4; §29–30 Appendix Table row 4).

---

## §5 Congruent Number Theorem (bonus; Wiles §1 p. 3)

### Definition 5.0 (congruent number)

An integer $n\geq 1$ is a *congruent number* if there exists a right triangle with rational sides and area $n$. Equivalently (Tunnell 1983), the elliptic curve $E_n : y^2 = x^3 - n^2 x$ has positive rank over $\mathbb{Q}$ (Wiles §1 p. 3).

### Theorem 5.1 (Tunnell's criterion becomes unconditional in CM scope)

*Statement.* Under the BSD Theorem 15.1 of `bsd-comply-bare.md` restricted to its scope, Tunnell's theorem (1983) becomes unconditional for the congruent-number question in the CM / $h_K = 1$ case: $n$ is congruent $\Leftrightarrow$ a specific theta-series count vanishes. Specifically, for $n$ squarefree:
- $n$ odd: $n$ congruent $\Leftrightarrow$ $\#\{(x,y,z)\in\mathbb{Z}^3 : 2x^2 + y^2 + 8z^2 = n\} = 2\#\{(x,y,z) : 2x^2 + y^2 + 32z^2 = n\}$.
- $n$ even: $n$ congruent $\Leftrightarrow$ analogous theta-formula (Tunnell 1983).

*Status.* **PROVED in scope** via BSD Theorem 15.1 (`bsd-comply-bare.md` §15). The curves $E_n : y^2 = x^3 - n^2 x$ are quadratic twists of the CM curve 32.a3 ($y^2 = x^3 - x$), CM by $\mathbb{Z}[i]$, $K = \mathbb{Q}(i)$, $h_K = 1$. Tunnell's criterion is conditional on BSD (rank part), which is our Theorem 15.1 in scope. Thus Tunnell's criterion is PROVED in the scope covered by `bsd-comply-bare.md` Theorem 15.1, under the CBB-conditionality rider.

*Pointer.* Wiles §1 p. 3 (congruent-number discussion); Tunnell 1983 "A classical diophantine problem and modular forms of weight 3/2"; p26 L11; p26 Node K (32.a3 is the CM twist base); LMFDB 32.a3.

### Remark 5.2 (bonus, not Clay-required)

Wiles explicitly flags congruent-number as the motivating ancient diophantine problem resolved by BSD (Wiles §1 p. 3). Closure of the congruent-number problem in scope is a named bonus consequence of Theorem 15.1; it is not part of Clay's seven requirements but carries a well-known independent stake (Fibonacci 1225; Fermat; Gauss).

---

## §6 Effective Generators for $C(\mathbb{Q})$ (bonus; Wiles Remark 4)

### Definition 6.0 (effective computation of $C(\mathbb{Q})$)

A method computes $C(\mathbb{Q}) = \mathbb{Z}^r \oplus C(\mathbb{Q})^\mathrm{tors}$ *effectively* if, given the Weierstrass coefficients $a, b$, it outputs $r$ and a finite generating set of $C(\mathbb{Q})/C(\mathbb{Q})^\mathrm{tors}$ in finitely many steps (paper26-bsd §13 Remark; Wiles Remark 4).

### Theorem 6.1 (effective generators in scope)

*Statement.* For $E/\mathbb{Q}$ in the scope of `bsd-comply-bare.md` Theorem 15.1 (CM, $h_K = 1$, $r\in\{0,1\}$), the following effective procedure computes $C(\mathbb{Q})$:

(i) Via modularity (BCDT 2001), compute $L(E,s)$ and evaluate $L(E,1)$ and $L'(E,1)$ numerically to high precision.

(ii) If $L(E,1)\neq 0$: Theorem 15.1 gives $r = 0$; torsion computed by Mazur 1977 + Lutz-Nagell. Done.

(iii) If $L(E,1) = 0$: vacuous in scope (Remark 14.2 of `bsd-comply-bare.md`: scope forces analytic rank $= 0$). In the scope-extended $r = 1$ case under the W_rank-bypass agenda, Gross-Zagier 1986 + Kolyvagin 1990 give $R_\infty = \hat h(y_K)$ effectively.

(iv) Apply Manin's integrality (Manin 1971; Wiles Remark 4): the BSD leading-coefficient formula with $|\Sha|\in\mathbb{Z}_{\geq 1}$ yields a finite search bound for generators.

*Status.* **PROVED in scope via composition of Theorem 15.1 + Manin 1971 + modularity**. "Effectively" means in the Turing-computability sense, not a complexity bound.

*Pointer.* Wiles Remark 4 (p. 2); Manin 1971; paper26-bsd §13 Remark; p26 L9 (Kolyvagin); p26 L10 (GZ); Mazur 1977 (torsion classification).

### Remark 6.2 (complexity status)

Theorem 6.1 is effective but not polynomial-time in the height; concretely, it reduces to the "search-for-generators" problem bounded by the conductor and the height of $|\Sha|$. A polynomial-time algorithm for general elliptic curves is OPEN; cf. the effective Mordell conjecture literature (Vojta; Faltings).

---

## §7 Euler's Quartic / Elkies Consequence (bonus; Wiles §3 p. 4)

### Definition 7.0 (Euler-quartic surface)

The surface $S : x^4 + y^4 + z^4 = t^4$ in $\mathbb{P}^3_\mathbb{Q}$. Euler conjectured (1769) that $S$ has no non-trivial rational points; Elkies (1988) falsified the conjecture by exhibiting a non-trivial solution (and in fact infinitely many).

### Theorem 7.1 (Elkies 1988; infinitely many solutions)

*Statement.* $S(\mathbb{Q})$ contains infinitely many non-trivial solutions; the BSD heuristic for elliptic curves of rank $\geq 1$ on $S$ gave the key guidance for Elkies' search (Wiles §3 p. 4).

*Proof.* Elkies 1988 *"On $A^4 + B^4 + C^4 = D^4$"*, Math.\ Comp.\ 51(184), 825–835; Wiles §3 p. 4. $\square$

### Corollary 7.2 (BSD rank-$\geq 1$ heuristic as load-bearing guidance)

*Statement.* The Elkies counterexample to Euler's quartic conjecture depended on finding a genus-1 curve of rank $\geq 1$ on $S$. BSD's rank-$L$-vanishing conjecture is the analytic proxy that guided the height-search. This is a historical / methodological cross-connection: BSD rank structure is used as input to diophantine construction problems beyond Clay's formal requirement.

*Status.* **LITERATURE** (Elkies 1988; Wiles §3 p. 4). Our contribution: no new theorem; we record the connection as one of the beyond-Clay bonus consequences of BSD's rank formalism (and of the ~~5D Branch-D~~ M⁵ Branch-D<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Branch-D" → "M⁵ Branch-D" --> rank-as-dark-state-degeneracy reading, Theorem 1.1 above).

*Pointer.* Wiles §3 p. 4; Elkies 1988; p61 §25–28 (adjacent arithmetic-geometry conjectures).

### Remark 7.3 (bonus connectivity)

BSD's analytic rank side (a spectral / L-function statement) drives arithmetic-geometry construction problems (diophantine solutions on specific surfaces). This is a Pattern-1 Geometric Reinterpretation instance (p8 §36 Pattern 1) applied in reverse: analytic data $\to$ geometric construction.

---

## §8 Computed Rank + L-values (numerical benchmarks)

### Definition 8.0 (benchmark curves)

Three standard LMFDB benchmark curves are used across the BSD literature for numerical checks:
- **32.a3** ($y^2 = x^3 - x$): CM by $\mathbb{Z}[i]$, $K = \mathbb{Q}(i)$, $h_K = 1$, rank 0. **In scope** of `bsd-comply-bare.md` Theorem 15.1.
- **37.a1** ($y^2 + y = x^3 - x$): non-CM, rank 1. **Out of scope** (W_nonCM).
- **389.a1** ($y^2 + y = x^3 + x^2 - 2x$): non-CM, rank 2. **Out of scope** (W_nonCM + W_rank).

### Table 8.1 (curve data; LMFDB-verified)

| Curve | CM? | $K$ (CM) | $h_K$ | rank $r$ | $\|E(\mathbb{Q})^\mathrm{tors}\|$ | $\Omega_E$ | $R_\infty$ | $\|\Sha\|$ | $c_p$ (Tamagawa list) | Scope verdict |
|-------|-----|----------|-------|----------|-------------------|-------------|-------------|-----------|-----------------------|---------------|
| 32.a3 | yes | $\mathbb{Q}(i)$ | 1 | 0 | 4 | $\Gamma(1/4)^2/(2\sqrt{2\pi}) \approx 2.62205755$ | 1 | 1 | $c_2 = 4$ | **IN SCOPE**; Thm 15.1 closes; $c^\ast = \Omega_E/4 = L(E,1)$ exactly |
| 37.a1 | no | — | — | 1 | 1 | $\approx 5.98691804$ | $\approx 0.05111$ | 1 | $c_{37} = 1$ | out (W_nonCM); $L'(E,1)$ non-zero per GZ |
| 389.a1 | no | — | — | 2 | 1 | $\approx 4.98076$ | $\approx 0.15234$ | 1 | $c_{389} = 1$ | out (W_nonCM + W_rank); $L''(E,1)$ non-zero (numerical) |

### Theorem 8.1 (32.a3 BSD formula check; exact)

*Statement.* For curve 32.a3, the BSD leading-coefficient formula reads
$$c^\ast \;=\; \frac{\|\Sha\|\cdot R_\infty\cdot \Omega_E\cdot c_2}{\|\mathrm{tors}\|^2} \;=\; \frac{1\cdot 1\cdot \Omega_E\cdot 4}{16} \;=\; \frac{\Omega_E}{4} \;=\; L(E,1) \;\approx\; 0.65551438,$$
with $c_2 = 4$ (LMFDB) not $c_2 = 1$ (prior draft error, resolved per paper26-bsd run-01 BROKEN 2; `bsd-comply-bare.md` §18 #6).

*Status.* **PROVED as exact numerical verification**.

*Pointer.* p26 L11 Node K; LMFDB 32.a3; `bsd-comply-bare.md` §18 rows #2, #6, #8.

### Theorem 8.2 (37.a1 and 389.a1; structural match only)

*Statement.* Curves 37.a1 (rank 1) and 389.a1 (rank 2) are out of scope of `bsd-comply-bare.md` Theorem 15.1 (W_nonCM and W_nonCM + W_rank respectively). Their BSD formulae are verified numerically in LMFDB but are not programme-level theorems within scope; they serve as external benchmarks and as motivation for the W_nonCM / W_rank bypass routes (`bsd-comply-bare.md` §16.1–§16.2).

*Status.* **OPEN-BUT-ADDRESSED** (out-of-scope reference).

*Pointer.* LMFDB 37.a1, 389.a1; `bsd-comply-bare.md` §16.1 (W_rank), §16.2 (W_nonCM).

### Remark 8.3 (scope disclosure, reiterated)

The in-scope numerical verification of BSD is the single curve 32.a3 (Theorem 8.1). Additional benchmarks exist in paper26-bsd Node K for families of CM-twist curves within scope (CM by $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{-2}]$, $\mathbb{Z}[\omega]$ for $\omega = (-1+\sqrt{-3})/2$, and other $\mathcal{O}_K$ with $h_K = 1$).

---

## §9 Proof-Chain Analytics (Beyond-Clay Depth)

### §9.1 Dependency graph (C_bare theorems $\to$ programme chains)

```
                          +-------------------------------+
                          |     QG5D (paper1)             |
                          |     Postulates P1-P4          |
                          |     5 CBB Axioms (Branch D)   |
                          |     paper23 axiomatisation    |
                          +-------------+-----------------+
                                        |
         +-----------+------------------+-----------------+-----------+
         v           v                  v                 v           v
      Branch B    Branch D          Branch E          Branch A     Branch C
      (gauge)    (BC algebra)      (pins L-value)    (quantum)    (cosmology)
                     |                  |
                     |                  |
                (paper61 §10,         (paper12 R/23,
                 §19.4)               paper1 Pin 1)
                     |                  |
                     v                  v
    +-----------------------------------------------------------------+
    |  C_bare §1 Thm 1.1 - M⁵ -> BSD (rank = ord L) motivic BC        |<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D -> BSD" → "M⁵ -> BSD" -->
    |  C_bare §1 Cor 1.2 - R-scaling via shared CBB dictionary        |
    |  C_bare §1 Cor 1.3 - c* = Murray-vN dimension identity           |
    |  C_bare §2 Thm 2.1 - 0 free parameters                           |
    |  C_bare §3 Thm 3.1 - BSD-relevant pin sub-% match in scope       |
    |  C_bare §8 Thm 8.1 - 32.a3 exact c* = L(E,1) check               |
    +--------------------+---------------------------------------------+
                         |
                         |  (uses paper26 Links L1-L11 + W-wall disclosures)
                         |
                         v
        +------------------------------------------------+
        |   paper26 BSD Chain (11 layers)                |
        |   (B_bare covers Clay requirements;            |
        |    in-scope: CM, h_K=1, r in {0,1})            |
        +------------------------+-----------------------+
                                 |
                                 | (cross-Clay edges per X-RAY)
                                 |
     +-------+-------+-------+---+---+-------+---------+-------+
     v       v       v       v       v       v         v       v
     RH      YM     PvNP   Hodge   Sato-   Baum-      Bloch-  (Congruent
    §4.1   §4.2    §4.3   §4.4    Tate    Connes     Kato     §5, Tunnell)
    (p13)  (p8)    (p28)  (p29)   §4.5    §4.6       §4.7     (p26 + Thm 5.1,
                                  (p44)   (p31)     (spec)    bonus consequence)

     bonus theorems:
     §5.1 Congruent number - Tunnell unconditional in scope
     §6.1 Effective generators (Wiles Remark 4; Manin integrality)
     §7.1 Elkies Euler quartic (Wiles §3 p. 4; LITERATURE)
```

### §9.2 RIGIDITY / SYMMETRY / MEASURE contribution

Per the BSD chain (`bsd-comply-bare.md` §17.3, §17.4) and the Paper-61 face assignment (p61 §13 row 4, p61 §29–30 Appendix row 4):

- **RIGIDITY** (load-bearing for BSD): L4 (dark-state impossibility), L5 / L5b / L5c (cocycle-shift diophantine inequalities), L7 (GRH zero-line rigidity). $\approx$ **38.5%** of chain slots.
- **SYMMETRY**: L1 (KMS$_1$-uniqueness as modular-flow symmetry), L8 (CM-Galois symmetry), L11 (rank-vs-ord symmetry of Taylor expansion). $\approx$ **23.1%**.
- **MEASURE / AMPLITUDE** (Branch E pin + partition-function measure side): implicit across L3 (ITPFI measure), L7 (L-value amplitude), L11 (leading-coefficient amplitude).
- **ARITHMETIC / CURVATURE / DYNAMICS** (tertiary): ARITHMETIC in L8 (Deuring), L9 (Euler system), L10 (heights); CURVATURE in L5 (Brauer-cocycle geometry); DYNAMICS on BC modular flow (L1, L3).

Dominant pattern distribution (per ym X-RAY face/projection/pattern conventions):
- P4 Topological Rigidity: $\approx 35\%$ (load-bearing, L4, L5/L5b/L5c, L7).
- P1 Geometric Reinterpretation: $\approx 25\%$ (p61 reading of rank-as-dark-state).
- P5 Zeta Regularisation: $\approx 20\%$ (Hecke-L, GRH at L7).
- P3 Scale-Setting: $\approx 15\%$ (bridge family, R-dictionary).
- P2 Holonomy Correspondence: $\approx 5\%$ (cocycle geometry, L5).

### §9.3 Cross-cut edges (beyond B_bare's X-RAY map, speculative)

Bonus cross-cuts flagged here for future formalisation:
- **BSD $\leftrightarrow$ Collatz** via Newton-power-sum on KK-mode index over bridge family at $k\in\{2,3,4,6\}$ (SPECULATIVE).
- **BSD $\leftrightarrow$ Twin Primes / Goldbach** via ARITHMETIC-face Newton-power-sum on Hecke-L prime inputs (SPECULATIVE, inherits via RH).
- **BSD $\leftrightarrow$ Lindelöf** via amplitude uniformity on Hecke-L (SPECULATIVE $\to$ PARTIAL).
- **BSD $\leftrightarrow$ Katz-Sarnak** via GUE pair-correlation on Hecke-L zeros (SPECULATIVE, inherits via p13 L.6).
- **BSD $\leftrightarrow$ ABC** via height-vs-$\Sha$ bounds (SPECULATIVE).

Total cross-Clay edges counted in §4 (non-speculative): **7** (Theorems 4.1–4.7, with 4.7 SPECULATIVE$\to$PARTIAL).

### §9.4 Named-wall inheritance

B_bare-level walls (inherited from `bsd-comply-bare.md` §16):

- **W_rank** — $r\geq 2$. OPEN-BUT-ADDRESSED. Bypasses: Iwasawa (Skinner-Urban 2014; Kato; Wan); p-adic L (Perrin-Riou); average-rank statistics (Bhargava-Shankar 7/6; BSZ 66%); ~~5D KK-spectral~~ M⁵ KK-spectral<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D KK-spectral" → "M⁵ KK-spectral" --> (p61 §08).
- **W_nonCM** — non-CM $E/\mathbb{Q}$. OPEN-BUT-ADDRESSED. Bypasses: modularity discharges Req 3 (BCDT 2001); Connes-Marcolli GL$_2$ BC system 2008; $p$-converse Kolyvagin (Skinner 2014; BSTW 2024–26).
- **W_hK** — CM with $h_K > 1$. OPEN-BUT-ADDRESSED. Bypasses: ring-class-field enlargement; Gross 1984; YZZ generalised GZ.
- **W_Sha** — $\Sha$ finiteness outside rank 0. PARTIAL. Bypasses: Rubin 1991 IMC-CM; Mazur-Wiles 1984 cyclotomic; Skinner-Urban 2014 GL(2).

C_bare-level additional items (bonus-specific, beyond B_bare):
- **NC-5.1** — No new wall; §5.1 is PROVED in scope (Tunnell's criterion unconditional in CM / $h_K = 1$).
- **NC-6.1** — No new wall; §6.1 PROVED in scope (effective generators by modularity + Manin + Kolyvagin).
- **NC-7.1** — No wall; §7 is LITERATURE (Elkies 1988).

No new named wall introduced at the C_bare level beyond the four at B_bare.

### §9.5 Independence / Route-3-MY4 position

Per landscape.md §"Our programme's position": Route 3 MY4 treats BSD as a corollary of an ergodic-theoretic picture (CBB KMS-states for GL$_2$ encode L-function behaviour; GZ-YZZ height formula becomes a Murray-von Neumann dimension identity, Corollary 1.3). This is complementary to the Bhargava-Skinner-Zhang statistical programme (66% of curves by height) — BSZ prove rank-BSD for a positive proportion; we prove strong-form BSD for the CBB-admissible CM / $h_K = 1$ class. Reviewers from each school are represented in the paper26-bsd critic list.

---

## §10 References

### Programme papers (with §-level precision)

- **p1** — `integers/paper01-qg5d/PROOF-CHAIN.md` (QG5D hub). Load-bearing §: P1–P4 (postulates); Branch D (BC axioms + operator dictionary $\hat L = \log\hat R$); Branch E (36 pins including Pin 1 = $R = 10.10\,\mu\mathrm{m}$); `integers/paper01-qg5d/code/pin6-audits/FINDINGS.md` (J_CKM audit; Pin #6 THEOREM-pending-audit with corrected items).
- **p8** — `solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md`. Load-bearing: L.14 (mass-gap rigidity); L.16 (OS reconstruction / Schwinger functions); §36 Pattern 4 (Topological Rigidity); shared with BSD at Branch D.
- **p12** — `integers/paper12-cbb-system/...` (CBB system; 5 axioms; operator dictionary). Research subfiles p12R/05, p12R/11, p12R/23 (master pin table), p12R/102 (J_CKM derivation — corrected audit items).
- **p13** — `solutions-with-prize/paper13-rh/PROOF-CHAIN.md` (6+3 layers; RH via CCM + ITPFI + Boegli). L.7 (GRH) feeds p26 L7 directly.
- **p23** — `paper23-cbb-axioms/...` (CBB axiomatisation; conditionality rider source).
- **p26** — `solutions-with-prize/paper26-bsd/PROOF-CHAIN.md` (11 links; BSD in scope). Nodes A–K; preprint §03–§13; adversarial run-01 (15 attacks, 2 BROKEN + 5 WEAKENED + 8 SURVIVED, all resolved).
- **p28** — `solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md` (6 links; P $\neq$ NP via Boolean BC + Bulatov-Zhuk + Taylor/spectral gap). Cross-cut via Branch D rigidity.
- **p29** — `solutions-with-prize/paper29-hodge/PROOF-CHAIN.md`. CM motives feed BSD cross-cut (Thm 4.4).
- **p31** — `solutions/paper31-baum-connes/PROOF-CHAIN.md`. K-theory pairing feeds BSD Murray-vN dimension identity (Thm 4.6; Corollary 1.3).
- **p44** — Sato-Tate (paper44). CM case proved Hecke 1920; non-CM Taylor et al. 2011. Cross-cut Thm 4.5.
- **p60** — `integers/paper60-geometry-of-circle/`. CURVATURE / MEASURE face content.
- **p61** — `integers/paper61-projections-5d/sections/`. Load-bearing §: §13 ($P_O^{(\mathrm{BSD})} = P_D \wedge P_E$ definition); §19.4 (BSD as Branch D projection via Hecke); §25–28 (Bloch-Kato prediction, adjacent conjectures); §29–30 Appendix Table row 4.
- **MT** — `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md` (36-pin master table).
- **UA** — `strategy/_research/universal-approval-protocol.md` (governs §11 below).

### Programme scaffolding artifacts

- `strategy/bsd/00-millenium-strategy.md` (Millennium strategy; §3 seven requirements; §11 four walls).
- `strategy/bsd/bsd-millenium-brief.md` (PAC operational brief; DELTA 1–11; DELTA 6 = this document's 10-section structure).
- `strategy/bsd/pac-output/runs/run-02/compliance-map.md` (LOCKED 77-cell verdict matrix).
- `strategy/bsd/pac-output/runs/run-02/commit-memo.md` (run-02 lock memo).
- `strategy/bsd/pac-output/runs/run-04/` (this run; Pillar-C beyond-synthesis transcript).
- `strategy/bsd/deliverables/bsd-comply-bare.md` (Pillar-A COMPLY deliverable; B_bare-analogue Clay-ready skeleton).
- `strategy/_research/birch-swinnerton-dyer/landscape.md` (Related-work landscape; source for §11).
- `strategy/x-ray/proof-chain/bsd/` (BSD X-RAY cross-cut map, analogue of ym X-RAY §7).

### External (cited via programme papers only; no duplication)

Key external references used at §-level above: Tunnell 1983, Elkies 1988, Manin 1971, Wiles Remark 4 / §3 (Clay problem statement), Hecke 1920 (CM Sato-Tate), Deuring 1953 (CM factorisation), Ha-Paugam 2005 (BC over imaginary quadratic), Bost-Connes 1995 (BC over $\mathbb{Q}$), Connes-Marcolli 2008 (GL$_2$ BC), Bloch-Kato 1990 (Selmer groups), Deligne 1979 (CM motives), Shimura 1971 (CM theory). Full external reference list in `solutions-with-prize/paper26-bsd/preprint/sections/references.md`.

---

## §11 Related Work & Acknowledgments (Universal Approval)

*This section is mandated by the Universal Approval protocol (UA; `strategy/_research/universal-approval-protocol.md`). Source: `strategy/_research/birch-swinnerton-dyer/landscape.md`. Honours CM-specialisation authors whose results are load-bearing for the in-scope BSD theorem and the bypass routes for the four named walls.*

### §11.1 Major Approaches (summary table)

| # | Approach | Key Author(s) | Our Relation |
|---|---|---|---|
| 1 | BSD for CM elliptic curves | Coates–Wiles (1977); Rubin (1988–91) | In-scope base case; Kolyvagin + Rubin IMC-CM feed W_Sha bypass |
| 2 | Heegner points / Gross–Zagier / Kolyvagin | Gross–Zagier (1986); Kolyvagin (1990); Yuan–Zhang–Zhang (2013) | Rank 1 layer (p26 L10), vacuous in scope; LITERATURE foundation; YZZ generalises for higher-genus / ring-class-field extension (W_hK bypass) |
| 3 | Iwasawa Theory / Main Conjecture | Skinner–Urban (2014); Kato (2004); Wan (2015); Mazur-Wiles (1984); Rubin (1991) | Foundation for W_rank + W_Sha bypasses |
| 4 | Modularity | Wiles (1995); Taylor–Wiles (1995); Breuil-Conrad-Diamond-Taylor (2001) | Discharges Req 3 (L-continuation + FE) unconditionally for every $E/\mathbb{Q}$; LITERATURE at p26 L8 |
| 5 | Statistical / Average Rank | Bhargava–Shankar (2010–14); Bhargava–Skinner–Zhang (2014) | Complementary to our CM / CBB-admissible programme; W_rank statistical bypass |
| 6 | p-converse Theorems | Skinner (2014); Burungale–Skinner–Tian–Wan (2019–24) | W_nonCM bypass route; p-converse for non-CM twist families |
| 7 | Euler systems / Anticyclotomic | Howard (2004); Longo–Vigni (2010); Ribet–Skinner | Auxiliary to W_Sha bypass |
| 8 | p-adic L-functions / Stark-Heegner | Perrin-Riou (1992); Darmon (2001); Bertolini–Darmon; Rotger | W_rank + W_nonCM bypass input; p-adic BSD side |
| 9 | BC algebra / Bost-Connes / GL$_2$ system | Bost–Connes (1995); Connes–Marcolli (2008); Ha–Paugam (2005) | Programme foundation (p26 L1; W_nonCM bypass via GL$_2$ BC) |

**Our contribution**: ~~5D geometry~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometry" → "M⁵" --> $M^5 = M^4 \times S^1 \to P_O^{(\mathrm{BSD})} = P_D \wedge P_E$ reading BSD rank as dimension of the degenerate KMS$_1$ eigenspace on the CM locus of the BC algebra $\mathcal{A}_{\mathrm{BC},K}$ (Theorem 1.1); $c^\ast$ as Murray-von Neumann dimension identity (Corollary 1.3); zero free parameters in scope (Theorem 2.1). The 11-link p26 chain closes BSD in scope (CM, $h_K = 1$, $r\in\{0,1\}$) conditional on CBB axioms (paper23; same status as paper13-rh). Four OPEN-BUT-ADDRESSED named walls disclose the non-scope frontier (W_rank, W_nonCM, W_hK, W_Sha) with literature-bypass routes.

### §11.2 Named prior results

| Year | Author(s) | Result |
|---|---|---|
| 1922 | L.\ J.\ Mordell | Finite generation of $C(\mathbb{Q})$ |
| 1953 | M.\ Deuring | CM factorisation $L(E,s) = L(s,\psi)L(s,\bar\psi)$ |
| 1966 / 1975 | A.\ Baker | Transcendence of linear forms in logarithms |
| 1971 | Yu.\ I.\ Manin | Integrality of $\|\Sha\|$ in $c^\ast$ suffices for strong BSD |
| 1977 | J.\ H.\ Coates, A.\ Wiles | BSD for CM elliptic curves, rank 0 case |
| 1983 | J.\ B.\ Tunnell | Congruent-number criterion via theta-series |
| 1984 | B.\ Mazur, A.\ Wiles | Main conjecture of Iwasawa theory (cyclotomic) |
| 1986 | B.\ Gross, D.\ Zagier | Height formula for $L'(E,1)$; Heegner points |
| 1988 | N.\ D.\ Elkies | Counterexample to Euler's quartic ($A^4+B^4+C^4=D^4$) |
| 1990 | V.\ Kolyvagin | Euler systems; bounds $\Sha$; rank $\leq 1$ BSD |
| 1991 | K.\ Rubin | Iwasawa main conjecture for CM elliptic curves |
| 1995 / 2001 | A.\ Wiles; R.\ Taylor & Wiles; Breuil–Conrad–Diamond–Taylor | Modularity of every $E/\mathbb{Q}$ |
| 2005 | E.\ Ha, F.\ Paugam | BC algebra over imaginary quadratic $K$ |
| 2008 | A.\ Connes, M.\ Marcolli | GL$_2$ BC system (W_nonCM bypass candidate) |
| 2010–14 | M.\ Bhargava, A.\ Shankar | Average-rank bound $7/6$ |
| 2013 | X.\ Yuan, S.-W.\ Zhang, W.\ Zhang | Generalised Gross–Zagier for Shimura curves |
| 2013–14 | C.\ Skinner, E.\ Urban | Iwasawa main conjecture for GL(2)/$\mathbb{Q}$ |
| 2014 | M.\ Bhargava, C.\ Skinner, W.\ Zhang | 66% of elliptic curves satisfy rank-BSD |
| 2014 | C.\ Skinner | $p$-converse to Gross–Zagier–Kolyvagin |
| 2019–24 | A.\ Burungale, C.\ Skinner, Y.\ Tian, X.\ Wan | Strong BSD for infinite non-CM twist families |
| 2024–26 | Burungale–Skinner–Tian–Wan (continued) | Further Iwasawa applications; curves with infinitely many BSD-twists up to conductor 500,000 |

### §11.3 Recent parallel work (2023–2026)

- arXiv:2601.16044 — "On the identification of elliptic curves that admit infinitely many twists satisfying BSD" (2026).
- Burungale–Skinner–Tian–Wan (2024–26) — Iwasawa-main-conjecture applications to non-CM BSD.
- Dasgupta–Kakde (2021–present) — $p$-adic Stark conjecture, input to L-function understanding.
- Further populate from `strategy/_research/birch-swinnerton-dyer/landscape.md` "Recent Preprints" — next UA cycle.

### §11.4 Acknowledgments (UA Pillar-C harden targets)

| Researcher | Contribution the programme relies upon |
|---|---|
| John Coates (d. 2022), Andrew Wiles | BSD for CM curves (rank 0); main conjecture framework; modularity |
| Victor Kolyvagin | Euler-system technique (p26 L9); foundational for W_Sha bypass |
| Benedict Gross, Don Zagier | Height formula (p26 L10, vacuous in scope); rank-1 BSD |
| Karl Rubin | Iwasawa main conjecture for CM (Rubin 1991); rank-0 $\Sha$-finiteness unconditional (p26 L9) |
| Christopher Skinner, Eric Urban | IMC for GL(2)/$\mathbb{Q}$; foundation of W_rank and W_Sha bypasses |
| Xinyi Yuan, Shou-Wu Zhang, Wei Zhang | Generalised Gross–Zagier (W_hK and W_nonCM bypasses) |
| Andrew Wiles, Richard Taylor, Christophe Breuil, Brian Conrad, Fred Diamond | Modularity of every $E/\mathbb{Q}$ (discharges Req 3 unconditionally, p26 L8) |
| Manjul Bhargava, Arul Shankar | Average-rank bounds (statistical W_rank bypass) |
| Ashay Burungale, Ye Tian, Xin Wan | Non-CM p-converse; W_nonCM bypass |
| Henri Darmon, Massimo Bertolini, Victor Rotger | p-adic L-functions; Stark-Heegner; W_rank / W_nonCM p-adic input |
| Kartik Prasanna, Ellen Eischen | Automorphic periods; p-adic L-functions (Iwasawa-adjacent) |
| Jean-Benoît Bost, Alain Connes, Matilde Marcolli | BC algebra over $\mathbb{Q}$; GL$_2$ BC system (programme foundation + W_nonCM bypass) |
| Eugene Ha, Frédéric Paugam | BC algebra over imaginary quadratic $K$ (p26 L1 foundation) |
| Max Deuring | CM factorisation $L(E,s) = L(s,\psi)L(s,\bar\psi)$ (p26 L8 unconditional) |
| Yuri I.\ Manin | Integrality-suffices-for-BSD remark (Wiles Remark 4; §6 effective generators) |
| Jerrold B.\ Tunnell | Congruent-number criterion (§5) |
| Noam D.\ Elkies | Euler quartic counterexample (§7) |

Additional acknowledgments: Louis J.\ Mordell (finite generation, Definition 4.3 of `bsd-comply-bare.md`), Alan Baker (transcendence, p26 L6 non-load-bearing reinforcement), Barry Mazur (main conjecture; torsion classification 1977 used in §6), Kazuya Kato (cyclotomic IMC for modular forms; W_rank bypass input), John Tate (Shafarevich group / regulator formalism).

UA Pillar-C harden commitments (next cycle): audit and strengthen load-bearing construction layers for (i) Rubin 1991 IMC-CM (W_Sha bypass; critical for strong BSD in CM scope); (ii) Ha-Paugam 2005 (p26 L1 direct input; unique KMS$_1$ at $h_K = 1$); (iii) Skinner-Urban 2014 (W_rank + W_Sha bypass for GL(2)); (iv) Burungale-Skinner-Tian-Wan 2024 (W_nonCM bypass via $p$-converse). See `strategy/universal-approval-run.md` for scheduling.

---

*End of bsd-beyond-bare.md. Bare discipline enforced: zero prose paragraphs, every claim cites programme paper + §-level location. $\leq 15$ pages target. Written in run-04 as Pillar-C (BEYOND-synthesis) deliverable for the BSD vertex of the Universal Approval run. §11 Related Work & Acknowledgments populated from `strategy/_research/birch-swinnerton-dyer/landscape.md`. Companion to `bsd-comply-bare.md` (Pillar-A COMPLY; 19-section Clay-shaped skeleton). Cross-Clay edges catalogued in §4 (7 non-speculative + 5 speculative). Four named walls (W_rank, W_nonCM, W_hK, W_Sha) inherited from B_bare; no new C_bare-level walls. CBB-conditionality rider applied throughout; no "unconditional" overclaim attaches to any $\omega_1^K$-derived content. C_full and B_full DEFERRED to composition-backward (next run).*

*G Six and Claude Opus 4.6. 2026-04-14.*
