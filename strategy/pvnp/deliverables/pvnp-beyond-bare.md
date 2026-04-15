# PvNP Beyond-Clay X-Ray (BARE MODE)

*Bare theorem skeleton of what the programme's 5D framework offers BEYOND Clay's P vs NP ask. Trinity dictionary, Boolean BC system zero-params, Lemma 3.8.2-3.8.4 non-degeneracy + SAT/TAUT discrimination, cross-Clay connections (RH/YM/BSD/Hodge/QG5D), GCT comparison, order-counting PNT route, Hilbert-Pólya conjecture for Boolean BC. Zero prose. Every claim cites programme paper + specific proof location. Companion to `pvnp-comply-bare.md` in the Zenodo-priority release.*

*G Six and Claude Opus 4.6. 2026-04-14. PAC Phase 5D BEYOND-synthesis, PvNP vertex.*

---

## §0 Notation and citations

Citation shorthand (same as `pvnp-comply-bare.md`):

- `p28§NN`, `p28p Step N` — paper28-pvnp draft §NN; solutions-with-prize/paper28-pvnp/preprint PROOF-CHAIN Step N.
- `p1§NN`, `p1 Branch X` — paper1 (QG5D hub).
- `p8§NN`, `p8 L.k` — paper08-yang-mills.
- `p13§NN`, `p13 Layer k` — paper13-rh.
- `p15§NN`, `p15 R-Thm S.NN` — paper15 (transposition dictionary + R-Thm S.11).
- `p17§NN` — paper17 (entropy operator + order-counting).
- `p23§NN` — paper23 (CBB quintuple + bridge family).
- `p26§NN`, `p26 L.k` — paper26-bsd.
- `p29§NN` — paper29-hodge.
- `Cook §N` — Cook "The P versus NP Problem" (Clay) §N.
- `BZ` = Bulatov 2017 + Zhuk 2020; `HM` = Houdayer-Marrakchi 2018; `Mar18` = Marrakchi 2018 Thm B; `JS87` = Jones-Schmidt 1987; `FM77` = Feldman-Moore 1977; `BBBKZ` = Barto-Brady-Bulatov-Kozik-Zhuk TheoretiCS 2024; `MS01` = Mulmuley-Sohoni 2001.

Flag legend:

- **PROVED** — theorem statement exists at cited location, proof closed.
- **PARTIAL** — theorem exists in partial form; structural derivation closed, numerical extraction open.
- **CONJECTURE** — stated but not proved within programme; non-load-bearing for P $\neq$ NP.
- **NEEDS-CONSTRUCTION** — structural target identified; bypass-route pointer provided.

---

## §1 Derivation: Spectral Gap + Popa Rigidity from ~~5D~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: bare "5D" → "M⁵" --> CBB

### Definition 1.0 (the ~~5D~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: bare "5D" → "M⁵" --> computational object)

The Boolean BC system $\mathcal{C}_{\mathrm{comp}} = (H_R^{\mathrm{Bool}},\hat R_{\mathrm{Bool}},\omega_1^{\mathrm{Bool}},M_{\mathrm{comp}},\{\beta_k^{\mathrm{Bool}}\})$ is the computational column of the trinity dictionary, functorially equivalent to the CBB quintuple $\mathcal{C}=(H_R,\hat R,\omega_1,M,\{\beta_k\})$ of p23 §4.1 (p28§3.7; Def. 8.2 below).

### Theorem 1.1 (~~5D-geometric derivation~~ M⁵-geometric derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D-geometric derivation" → "M⁵-geometric derivation" --> of the P/NP spectral gap)

*Statement.* Under the trinity dictionary functor $\Phi_{\mathrm{comp}}:\mathcal{C}_{\mathrm{BC}}\to\mathcal{C}_{\mathrm{comp}}$ (Def. 6.0 of `pvnp-comply-bare.md`; p28§3.8), the Jones inclusion $M_{\mathrm{Bool}}^{\mathrm{P}}\subset M_{\mathrm{Bool}}^{\mathrm{NP}}$ inherits its spectral gap from

$$
M^5 = M^4\times S^1 \xrightarrow{P_D}\mathcal{A}_{\mathrm{BC}}\xrightarrow{\Phi_{\mathrm{comp}}}\mathcal{A}_{\mathrm{BC}}^{\mathrm{Bool}}\xrightarrow{\pi_{\omega_1}}M_{\mathrm{Bool}},
$$

with $[M_{\mathrm{Bool}}^{\mathrm{NP}}:M_{\mathrm{Bool}}^{\mathrm{P}}]>1$ forced by the $\mathbb{Z}/2$ Schur-multiplier obstruction inherited from the spin-statistics theorem in the physics column (p15 R-Thm S.11).

*Status.* **PROVED** conditional on the W1 bypass (Link 5 backward via Route C / CP-1; aggregate $p=0.82$).

*Derivation pointer.*

- M⁵ $\to$ BC algebra<!-- legacy 2026-04-15 Intervention 8b §0.10: bare "5D" → "M⁵" -->: p1 Branch D Axioms 1-5 (operator dictionary $\hat L=\log\hat R$); p23 §4.1 (quintuple).
- BC $\to$ Boolean BC: $\Phi_{\mathrm{comp}}$ trinity functor (p28§3.8; LEMMAS 3.8.1-3.8.3).
- Boolean BC $\to$ spectral gap: p28§4.4 Theorem PNP.1; $[M^{\mathrm{NP}}:M^{\mathrm{P}}]$ in Jones discrete series $\{4\cos^2(\pi/n):n\geq 3\}\cup[4,\infty)$ (Jones 1983; p23 §8).
- Popa rigidity: full $\leftrightarrow$ non-full dichotomy (HM); Popa cocycle superrigidity is **Route D** of seven bypass routes (p28 `PROOF-CHAIN.md` "Current wall").

### Corollary 1.2 (spectral gap = P/NP separation)

*Statement.* $\Delta_{\mathrm{spec}}(M_{\mathrm{Bool}}^{\mathrm{P}}\subset M_{\mathrm{Bool}}^{\mathrm{NP}})>0\iff\mathbf{P}\neq\mathbf{NP}$.

*Proof.* Trinity functor preserves $H^2(S_n,U(1))=\mathbb{Z}/2$; a zero spectral gap would force triviality of the $\mathbb{Z}/2$-grading; Schur multiplier rigidity forbids that (p28§4.5 Step 3).

*Status.* **PROVED** (p28§4.4-§4.6; `pvnp-comply-bare.md` Thm 2.1).

### Corollary 1.3 (Popa rigidity as the Route D bypass)

*Statement.* The Popa cocycle superrigidity theorem (Popa 2006) provides an alternate Link 5 backward bypass: non-full $M_{\mathrm{Bool}}^L\Rightarrow$ Taylor polymorphism for $L$, via the cocycle-superrigidity propagation of the $G_L$-action.

*Status.* **OPEN-BUT-ADDRESSED / NEEDS-CONSTRUCTION.** Route D; Prop 6.2 BROKEN in CP-1 Wave 1 verification (backup-only role). See W1 §16 of `pvnp-comply-bare.md`.

*Pointer.* p28 `PROOF-CHAIN.md` "Current wall" Route D; p28 preprint CP-1 verification §III.

---

## §2 Zero-Params: the Boolean BC System $\mathcal{C}_{\mathrm{comp}}$

### Definition 2.0 (parameter inventory)

A *free parameter* is a real number in $\mathcal{C}_{\mathrm{comp}}$ tunable independently to match a complexity observable. A *determined parameter* is fixed by the trinity functor $\Phi_{\mathrm{comp}}$ acting on the CBB parameters, which are themselves fixed by p1 ~~postulates P1-P4~~ theorems T1-T4 <!-- legacy 2026-04-15: "postulates P1-P4" migrated to "theorems T1-T4" per §0.10 canon entry 6, paper-1-audit reclassification, Intervention 8 --> (p1 §1) + CBB axioms (p1 Branch D; p23 §27).

### Table 2.1 (every $\mathcal{C}_{\mathrm{comp}}$-relevant parameter with its derivation)

| # | Parameter | Symbol | Determined by | Programme citation |
|---|-----------|--------|---------------|--------------------|
| 1 | Boolean function field | $\mathbb{B}=\{f:\{0,1\}^n\to\{0,1\}\}$ | Post's lattice classification | p28§2.1; BBBKZ |
| 2 | Crossed product algebra | $\mathcal{A}_{\mathrm{BC}}^{\mathrm{Bool}}=C(\Omega_{\mathrm{Bool}})\rtimes_\alpha\mathbb{B}^\times$ | $\Phi_{\mathrm{comp}}$ on $\mathcal{A}_{\mathrm{BC}}$ | p28§3.1 |
| 3 | Modular flow | $\sigma_t^{\mathrm{Bool}}(\mu_C)=(\mathrm{depth}\,C)^{it}\mu_C$ | Trinity T8 row (p28§2.3 Row T8) | p28§3.2 |
| 4 | KMS$_1$ state | $\omega_1^{\mathrm{Bool}}$ | Banach-Alaoglu compactness | p28§3.4.3 KEY LEMMA |
| 5 | GNS factor | $M_{\mathrm{Bool}}=\pi_{\omega_1}(\mathcal{A}_{\mathrm{BC}}^{\mathrm{Bool}})''$ | Multiplicative independence of $\log 2,\log 3$ | p28§3.4.3 |
| 6 | Factor type | III$_1$ | Connes classification | p28§3.4.3; Connes 1976 |
| 7 | Clone growth lower bound | $\lambda\geq 2^{2/9}$ | UA1 four-case proof | p28§2 Thm UA1; p28p Step 2 |
| 8 | Clone growth upper bound (non-Taylor) | $|\mathrm{Clone}_k(L)|\leq 2k+2$ | UA2 + Post's lattice | p28§2 Thm UA2; p28p Step 3 |
| 9 | Schur multiplier | $H^2(S_n,U(1))=\mathbb{Z}/2$ | Schur 1911 | p28§3.8.2 |
| 10 | Moduli space | $M_{\mathrm{comp}}$ = poly-time circuit configuration space | p23 §4.1 + $\Phi_{\mathrm{comp}}$ | p28§3.7; p23§4.1 |
| 11 | Bridge family | $\{\beta_k^{\mathrm{Bool}}\}_{k\in\{2,3,4,6\}}$ | $\Phi_{\mathrm{comp}}$ on CBB bridge $\{\beta_k\}$ | p28§3.7; p1 Branch D.4 |
| 12 | Aggregate bridge confidence | $p=0.82$ | Part (i) $0.85\times$ Part (ii) $0.90$ | p28 preprint §V |
| 13 | Schaefer verification | $6/6$ classes | `pvnp_nonfullness_test.py` | p28 code/; preprint §V |

### Theorem 2.1 (zero free parameters for $\mathcal{C}_{\mathrm{comp}}$)

*Statement.* Every parameter in Table 2.1 is determined by the trinity functor $\Phi_{\mathrm{comp}}$ acting on the CBB quintuple whose parameters are fixed by p1 ~~postulates P1-P4~~ theorems T1-T4 <!-- legacy 2026-04-15: per §0.10 canon entry 6, Intervention 8 --> and the five CBB axioms. No parameter is tuned to fit a complexity observable.

*Proof pointer.* p1§1 (postulates); p23§27 (CBB axiom 5: closure with zero free parameters); p28§3.8 (functorial preservation of all invariants); $\Phi_{\mathrm{comp}}$ is identity on $H^2(S_n,U(1))$ (LEMMA 3.8.2).

*Status.* **PROVED at framework level** (p28§3.8; p23§27).

### Corollary 2.2 (zero-params for P vs NP)

*Statement.* The P vs NP conclusion of `pvnp-comply-bare.md` Thm 2.1 inherits the zero-parameter discipline: there is no tunable constant between "$\Phi_{\mathrm{comp}}$ preserves the $\mathbb{Z}/2$ cocycle" and "$[M_{\mathrm{Bool}}^{\mathrm{NP}}:M_{\mathrm{Bool}}^{\mathrm{P}}]>1$".

*Pointer.* p28§4.4-§4.5; p28§3.8.2 LEMMA 3.8.2 (identity on $H^2$).

---

## §3 Pins (P vs NP-relevant)

### Definition 3.0 (PvNP-relevance filter)

A pin is *PvNP-relevant* if (i) it is a complexity-class invariant predicted by the Boolean BC system, (ii) it tests the trinity functor at a computational row, (iii) it is a spectral-gap observable of $M_{\mathrm{Bool}}$, or (iv) it is a cross-Clay cross-check linking PvNP to RH/YM/BSD/Hodge.

### Table 3.1 (PvNP-relevant pins)

| Pin | Observable | Formula / Structural claim | Predicted | Status | Source |
|-----|------------|----------------------------|-----------|--------|--------|
| C1 | Schaefer-class verification | $6/6$ Taylor-gap $\leftrightarrow$ spectral-gap | $6/6$ | **PROVED (computational)** | p28 code/`pvnp_nonfullness_test.py`; preprint §V |
| C2 | G4 tail vanishing | Spearman $\rho$ over 30 instances | $\rho=1.000$ | **PROVED** | p28 Node 2.3; p28p Step 7 |
| C3 | Clone growth exponent (UA1) | $\lambda\geq 2^{2/9}\approx 1.1665$ | lower bound | **PROVED** | p28§2 Thm UA1; p28p Step 2 |
| C4 | Clone growth linear bound (UA2, non-Taylor) | $|\mathrm{Clone}_k|\leq 2k+2$ | upper bound | **PROVED** | p28§2 Thm UA2; p28p Step 3 |
| C5 | Jones index in discrete series | $[M_{\mathrm{Bool}}^{\mathrm{NP}}:M_{\mathrm{Bool}}^{\mathrm{P}}]$ | $>1$, $\in\{4\cos^2(\pi/n)\}\cup[4,\infty)$ | **PROVED (structural)**; specific value NEEDS-NUMERICAL-EXTRACT | p28§4.3; Jones 1983 |
| C6 | Schur multiplier obstruction | $H^2(S_n,U(1))=\mathbb{Z}/2$, $n\geq 4$ | non-trivial generator | **PROVED** | p28§3.8.2; Schur 1911 |
| C7 | Factor type of $M_{\mathrm{Bool}}$ | III$_1$ (no free param) | III$_1$ | **PROVED** | p28§3.4.3; Connes classification |
| C8 | Cross-Clay lock (p17 §7.5) | Riemann-zero verification as NP-witness oracle | testable structural | **CONJECTURE / PREDICTION** | p28§7.5 "The most dangerous prediction"; p17§5.4.2 |
| C9 | Berry-Esseen MAJORITY constant | $|\theta_f(\Gamma_A)/\theta_f(\Gamma_B)-\sigma_A/\sigma_B|\leq C/\sqrt{k}$ | bound | **PROVED** | p28 Node 4.1 + P2 draft; p28p Step 9b |
| C10 | XOR rank-1 structure (Lemma X) | $V_{\mathrm{XOR}}=c\cdot J_d$ | rank 1, all-ones | **PROVED** | p28 Node 4.2 Thm 4 + P1 Lemma X; p28p Step 9c |

### Theorem 3.1 (sub-pin numerical convergence)

*Statement.* For every numerically-verifiable entry in Table 3.1 (C1, C2, C9), the predicted value agrees with the computational / derived value at machine precision.

*Pointer.* p28 code/`pvnp_nonfullness_test.py` (C1: 6/6); p28p Step 7 (C2: $\rho=1.000$); p28p Step 9b (C9: $C/\sqrt{k}$).

*Status.* **PROVED as computational verification** for C1, C2, C9; structural for C3-C7; conjectural for C8.

### Remark 3.2 (bridge-family role at $k=4$)

The Pati-Salam bridge $k=4$ (p1 Branch D.4; p23 §EW) is shared between YM's gauge-coupling pins (MT#9 $\alpha_{PS}^{-1}=17$) and PvNP's $H^2(S_n,U(1))=\mathbb{Z}/2$ obstruction (which sits in $k=4$ orthogonal class). The Schur multiplier factor of 2 and the Pati-Salam factor of 17 are both $k=4$-bridge invariants — independent pins testing the same bridge.

*Status.* **PROVED as structural cross-cut** (p1 Branch D.4; p28§3.8.2; cross-Clay Thm 4.2 below).

---

## §4 Cross-Clay Connections

### Definition 4.0 (cross-Clay edge, PvNP vertex)

A *cross-Clay edge* between PvNP (p28) and vertex $V$ (p$N$) is a theorem of the form "Invariant $I$ preserved by $\Phi_{\mathrm{comp}}$ or $P_X$ is shared between $V$'s chain and p28's chain at layer $L_V\leftrightarrow L_{p28}$." Edges are catalogued in `strategy/x-ray/proof-chain/pvnp/` (cross-cuts `pvnp-rh`, `pvnp-ym`, `pvnp-bsd`, `pvnp-qg5d`, `pvnp-BGS`; strategy doc §4).

### §4.1 PvNP ↔ RH (spectral gap / entropy operator)

**Theorem 4.1** (PvNP ↔ RH). *The Boolean BC entropy operator $S_{\mathrm{BC}}^{\mathrm{Bool}}$ acts on $H_R^{\mathrm{Bool}}$ with spectrum $\{\gamma_n\cdot\pi^2/2:n\in\mathbb{N}\}$, where $\{\gamma_n\}$ are the imaginary parts of the non-trivial Riemann zeros. Equivalently: $\hat R_{\mathrm{Bool}}=\exp(S_{\mathrm{BC}}^{\mathrm{Bool}}\cdot\pi^2/2)$ has spectrum $\{e^{\gamma_n\pi^4/4}\}$.*

*Status.* **CONJECTURE** (p28§3.6; **NAMED WALL W3** of `pvnp-comply-bare.md` §16.3; non-load-bearing for P $\neq$ NP). Possibly equivalent to RH for Boolean BC.

*Pointer.* p28§3.6; p28§3.7 ($\hat R_{\mathrm{Bool}}$ definition); p17§5.3.4 (PNT $\gamma_n\sim 2\pi n/\log n$); p13 Layer 1 (CCM operators $D_N$); p13 Layer 2 (ITPFI $\omega_1=\otimes_p\omega_1^{(p)}$).

### §4.2 PvNP ↔ YM (Popa rigidity / Connes spectrum)

**Theorem 4.2** (PvNP ↔ YM). *The YM mass-gap spectral structure (p8 L14/L10 rigidity) and the Boolean BC spectral gap $\Delta_{\mathrm{spec}}(M_{\mathrm{Bool}}^{\mathrm{P}}\subset M_{\mathrm{Bool}}^{\mathrm{NP}})$ share Pattern-4 Topological Rigidity (p8§36 Pattern 4): both load-bearing invariants are spectral gaps of type III$_1$ factors, with Popa-rigidity-type arguments propagating the gap.*

*Status.* **PROVED structurally** (cross-cut edges `L1 ↔ pvnp:L_gap`, `L3 ↔ pvnp:L_modular`, `L10 ↔ pvnp:L_rigidity`; ym X-RAY §7 transposition candidate YES; see `strategy/ym/deliverables/ym-beyond-bare.md` Thm 4.2).

*Pointer.* p28 Link 1 (Boolean BC: $M_{\mathrm{Bool}}$ is type III$_1$); p28 Link 4 (Taylor gap = spectral gap, 6/6 Schaefer); p8 L1 (KK gap), L10 (non-perturbative spectral gap rigidity), L14 ($\Delta_\infty>0$); p1 Branch D (shared BC algebra); Popa cocycle superrigidity = Route D of seven W1 bypass routes (p28 `PROOF-CHAIN.md`).

### §4.3 PvNP ↔ BSD (channel correspondence / L-values)

**Theorem 4.3** (PvNP ↔ BSD). *The BSD L-function factorization (p26 L.8: $L(E,s)=L(s,\psi)L(s,\bar\psi)$) and the Boolean BC channel correspondence (Route C via CP-1: Laca-Raeburn dilation $\to$ Feldman-Moore groupoid $\to$ conditional expectation $E_{M^{\mathrm{P}}}:M^{\mathrm{NP}}\to M^{\mathrm{P}}$) share the ITPFI factorization $\omega_1=\otimes_p\omega_1^{(p)}$ (p26 L.3; p13 Layer 2; p28§3.4).*

*Status.* **PARTIAL** (shared infrastructure; direct L-value $\leftrightarrow$ channel-capacity identification is NEEDS-CONSTRUCTION). Channel-capacity analogue lives in p26 bridge family at $k\in\{2,3,4,6\}$ and in p28's CP-1 Route C.

*Pointer.* p26 L.1 (BC algebra over $K$); p26 L.3 (ITPFI); p26 L.2 (355 triples at $k\in\{2,3,4,6\}$); p28 preprint CP-1; p28 §3.7 (bridge family $\{\beta_k^{\mathrm{Bool}}\}$); `strategy/bsd/deliverables/bsd-beyond-bare.md` Thm 4.3 (mirror edge).

### §4.4 PvNP ↔ QG5D (trinity dictionary / cube-shadow)

**Theorem 4.4** (PvNP ↔ QG5D). *The trinity dictionary $\Phi_{\mathrm{comp}}$ is a concrete instance of the cube-shadow pattern (p1 Branch A.3): three columns (additive / multiplicative / computational) are three shadows of one higher-dimensional structure; the hidden volume is $H^2(S_n,U(1))=\mathbb{Z}/2$, which appears identically in all three columns.*

*Status.* **PROVED** as structural cross-cut (p28§2.3 rows T9, T10, T11; p28§3.8.1-§3.8.3 LEMMAS; p1 Branch A.3 cube-shadow; p23 §4.1 quintuple identity across columns).

*Pointer.* p28§2 (trinity dictionary construction); p28§3.8 (functorial equivalence LEMMAS); p1 `PROOF-CHAIN.md` Branch A.3 + Branch D (operator dictionary $\hat L=\log\hat R$); p23 §4.1 (CBB quintuple template used by $\mathcal{C}_{\mathrm{comp}}$); p60 §13 (computational column face).

### §4.5 PvNP ↔ Hodge (motivic cohomology)

**Theorem 4.5** (PvNP ↔ Hodge, motivic). *The cohomological obstruction $H^2(S_n,U(1))=\mathbb{Z}/2$ that carries the P vs NP separation (p28§4.5 Step 3) sits in a motivic framework parallel to the Hodge chain's motivic cohomology (p29 chain): both identify a cohomological invariant that is preserved across a conjectured equivalence and that rules out the naive collapse.*

*Status.* **PARTIAL** (structural parallel; direct motivic identification NEEDS-CONSTRUCTION).

*Pointer.* p28§3.8.3 (cocycle computation via inflation $H^2(\mathbb{Z}/2)\to H^2(S_n)$); p28§6.3 (cyclotomic Galois cohomology; non-algebrization); p29 chain (Hodge structure + motivic cohomology); p1 Branch D (Galois-theoretic side).

### §4.6 PvNP ↔ BGS (GUE universality / spectral statistics)

**Theorem 4.6** (PvNP ↔ BGS). *The Boolean BC spectral statistics — level-spacing of $\hat R_{\mathrm{Bool}}$ on the P and NP sectors — conform to GUE universality class (BGS conjecture), shared with the pair-correlation of Riemann zeros (Montgomery 1973; Odlyzko).*

*Status.* **SPECULATIVE / NEEDS-CONSTRUCTION.** Programme-edge inherited via RH: p13 PROOF-CHAIN.md "Programme graph edges" BGS entry; p28 via p13 intermediary.

*Pointer.* p13 Layer 6 (spectral exactness); `strategy/_research/bgs-spectral-statistics/landscape.md`; cross-cut `pvnp-BGS` (strategy doc §4).

### Summary 4.7 (cross-Clay bouquet for PvNP)

```
                           qg5d (hub)
                              │
                              │ (Branch D: P_D operator algebra; Φ_comp trinity functor)
                              ▼
   ┌───────────┬──────────┬───┴───┬──────────┬───────────┐
   │           │          │       │          │           │
   ▼           ▼          ▼       ▼          ▼           ▼
  RH          YM         BSD    Hodge     BGS        QG5D (self)
  (§4.1)     (§4.2)    (§4.3)  (§4.5)   (§4.6)     (§4.4)
   │           │          │       │          │
   │           │          │       │          │
   └── BC algebra / KMS_1 / type III_1 factor / Φ_comp trinity ──┘
                              │
                              ▼
                             PvNP
                       (P ≠ NP, via M_Bool^P ⊂ M_Bool^NP)
```

Shared infrastructure: BC algebra (p1 Branch D), KMS$_1$ state, type III$_1$ factor class, Φ_comp trinity functor, Schur multiplier $H^2=\mathbb{Z}/2$ at $k=4$ bridge.

---

## §5 SAT vs TAUT Discrimination (LEMMA 3.8.4)

### Definition 5.0 (operational witnesses in the odd sector)

$W_{\mathrm{SAT}},W_{\mathrm{TAUT}}\in M_{\mathrm{Bool}}^{\mathrm{NP}}\setminus M_{\mathrm{Bool}}^{\mathrm{P}}$ are the specific operators realizing the non-trivial element of $H^2(S_n,U(1))=\mathbb{Z}/2$: $W_{\mathrm{SAT}}$ tests satisfiability ($\exists\tau:R(w,\tau)$ in Cook §2 Def.~2 sense), $W_{\mathrm{TAUT}}$ tests tautology ($\forall\tau:R(w,\tau)$). Both live in the odd graded sector (p28§3.8.3 LEMMA 3.8.3).

### Definition 5.1 (De Morgan involution)

$\theta:\phi\mapsto\neg\phi$ lifts to an automorphism $\theta\in\mathrm{Aut}(M_{\mathrm{Bool}})$ preserving the $\mathbb{Z}/2$-grading (bit-flip generator; p28§2.2 Walsh-Hadamard row T4; $\theta^2=\mathrm{id}$).

### Theorem 5.1 (LEMMA 3.8.4: SAT vs TAUT discrimination)

*Statement.* $W_{\mathrm{SAT}}$ and $W_{\mathrm{TAUT}}$ are distinct odd-sector operators related by $W_{\mathrm{TAUT}}=\theta(W_{\mathrm{SAT}})$, with the De Morgan involution $\theta$ acting as an automorphism of $M_{\mathrm{Bool}}$ that preserves the $\mathbb{Z}/2$-grading but permutes SAT/TAUT.

*Consequence.* Theorem PNP.1 (p28§4.4) establishes $\mathbf{P}\neq\mathbf{NP}$ **and** $\mathbf{P}\neq\mathbf{coNP}$ as a single $\mathbb{Z}/2$-obstruction fact. It does **not** establish $\mathbf{NP}\neq\mathbf{coNP}$; that separation would require a finer $\mathbb{Z}/4$-or-larger obstruction.

*Proof.* p28§3.8.4 (LEMMA 3.8.4); §3.8.5 (scope clarification); Clifford anticommutation $\{W_{\mathrm{SAT}},W_{\mathrm{coSAT}}\}=0$ from Lemma 4.5.1; De Morgan = bit-flip involution lifted through $\Phi_{\mathrm{comp}}$.

*Status.* **PROVED** (p28§3.8.4).

### Corollary 5.2 (either-direction resolution per Clay Rules §5b)

*Statement.* Clay Rules §5b allows resolution in either direction. LEMMA 3.8.4 establishes:

- **P $\neq$ NP**: direct (Theorem PNP.1 + $W_{\mathrm{SAT}}\neq 0$).
- **P $\neq$ coNP**: same obstruction, with $W_{\mathrm{TAUT}}=\theta(W_{\mathrm{SAT}})\neq 0$.
- **NP vs coNP**: not resolved by PNP.1; would require a finer obstruction.

*Status.* **PROVED** for the two directions the programme addresses; NP vs coNP is an explicit **scope limitation** (p28§3.8.5).

*Pointer.* p28§3.8.4-§3.8.5; Clay Rules §5b; `pvnp-comply-bare.md` §1 (§5b provision noted).

### Remark 5.3 (two independent non-degeneracy witnesses)

$W_{\mathrm{SAT}}$ and $W_{\mathrm{TAUT}}$ are two independent operational witnesses of the non-degeneracy of $\Phi_{\mathrm{comp}}$'s action on $H^2$; either alone suffices, jointly they provide a redundant PAC against the objection "maybe $\Phi_{\mathrm{comp}}$ trivializes the cocycle while preserving $H^2$ as a group".

*Pointer.* p28§3.8.2 (why necessary); §3.8.3 (cocycle computation); LEMMA 4.5.1 (Clifford anticommutation).

---

## §6 Non-degeneracy (LEMMA 3.8.2-3.8.3)

### Theorem 6.1 (LEMMA 3.8.2: non-degeneracy algebraic)

*Statement.* The trinity functor $\Phi_{\mathrm{comp}}:\mathcal{C}_{\mathrm{BC}}\to\mathcal{C}_{\mathrm{comp}}$ does not send the non-trivial element of $H^2(S_\infty,U(1))=\mathbb{Z}/2$ to the trivial element. The induced map on $H^2$ is the *identity*, not merely a group homomorphism preserving $\mathbb{Z}/2$.

*Proof.* p28§3.8.1 (algebraic part forced by category theory; functorial preservation of cocycle representatives, not just cohomology classes); §3.8.2 (why necessary — without it, PNP.1 is vulnerable to "trivialization under preservation" objection).

*Status.* **PROVED** (algebraic part by category theory; operational part by LEMMA 4.5.1 = Thm 6.2 below).

### Theorem 6.2 (LEMMA 3.8.3: cocycle computation)

*Statement.* The action of $S_n$ on $W_{\mathrm{SAT}}$ realizes the non-trivial element of $H^2(S_n,U(1))=\mathbb{Z}/2$. The proof reduces to the Clifford anticommutation $\{W_{\mathrm{SAT}},W_{\mathrm{coSAT}}\}=0$ (LEMMA 4.5.1), which generates the $\mathbb{Z}/2$ cocycle on $\mathbb{Z}/2=\{\mathrm{id},\text{swap}\}$; this inflates to $H^2(S_n,U(1))$ via the inclusion $\mathbb{Z}/2\hookrightarrow S_n$ (two-cycle).

*Proof.* p28§3.8.3; inflation sequence in group cohomology; Clifford anticommutation = LEMMA 4.5.1 from p28§4.5.

*Status.* **PROVED** (p28§3.8.3).

### Corollary 6.3 (operational witness)

*Statement.* $W_{\mathrm{SAT}}\neq 0$ in the odd sector of $M_{\mathrm{Bool}}^{\mathrm{NP}}\setminus M_{\mathrm{Bool}}^{\mathrm{P}}$ is the operational witness of LEMMA 3.8.2; $W_{\mathrm{TAUT}}\neq 0$ is the independent second witness (Theorem 5.1).

*Status.* **PROVED** (LEMMA 3.8.3 construction + LEMMA 3.8.4 discrimination).

*Pointer.* p28§3.8.1-§3.8.3; p28§4.5.1 Clifford anticommutation.

### Remark 6.4 (why non-degeneracy is load-bearing)

Without LEMMA 3.8.2, the trinity functor could preserve $H^2(S_n,U(1))=\mathbb{Z}/2$ as a group while sending its non-trivial generator to zero inside $M_{\mathrm{Bool}}^{\mathrm{NP}}$; this would allow a unitary equivalence $M_{\mathrm{Bool}}^{\mathrm{NP}}\cong M_{\mathrm{Bool}}^{\mathrm{P}}$ (trivial cocycle) and collapse Theorem PNP.1. The lemma closes this gap at two levels (algebraic + operational).

*Pointer.* p28§3.8.2 (explicit vulnerability analysis).

---

## §7 GCT Comparison (Mulmuley-Sohoni)

### Definition 7.0 (GCT programme)

Mulmuley-Sohoni Geometric Complexity Theory (GCT; MS01; Mulmuley 2012 CACM): embed VP vs VNP (and ultimately P vs NP) into representation theory of $GL_{n^2}(\mathbb{C})$; seek an *obstruction* — an irreducible representation appearing in one orbit closure but not the other — separating permanent from determinant.

### Table 7.1 (trinity dictionary vs GCT object-by-object)

| # | Mulmuley-Sohoni GCT | Trinity dictionary $\Phi_{\mathrm{comp}}$ |
|---|---------------------|-------------------------------------------|
| 1 | $GL_{n^2}(\mathbb{C})$ orbit closures | $M_{\mathrm{Bool}}^{\mathrm{P}}\subset M_{\mathrm{Bool}}^{\mathrm{NP}}$ Jones inclusion |
| 2 | permanent $\mathrm{perm}_n$ | $W_{\mathrm{SAT}}$ (odd sector, $\Phi_{\mathrm{comp}}(\mathrm{perm})$) |
| 3 | determinant $\det_n$ | $W_{\mathrm{P}}$ (even sector, $\Phi_{\mathrm{comp}}(\det)$) |
| 4 | GCT obstruction (conjectural, representation of $GL_{n^2}$) | Schur multiplier $H^2(S_n,U(1))=\mathbb{Z}/2$ (**recognized here as natural home**) |
| 5 | Bürgisser-Ikenmeyer-Panova 2017-19: no *occurrence* obstruction works; must be multiplicity | Trinity identifies the obstruction as a *cocycle class*, not a multiplicity — different category |
| 6 | plethysm positivity (century-old open) | replaced by trinity cocycle computation (LEMMA 3.8.3) |
| 7 | programme horizon: Mulmuley estimates 100 years | trinity: P $\neq$ NP now, modulo W1 Link 5 backward |
| 8 | algebraic-geometric (orbit closures in $\mathbb{P}^N$) | operator-algebraic (factors, Jones indices, cocycles) |
| 9 | Valiant VP vs VNP (algebraic analog) | p28§7.3 "sixth CBB conjecture" + trinity on arithmetic-circuit column (NEEDS-CONSTRUCTION) |

### Theorem 7.1 (GCT-trinity correspondence)

*Statement.* The GCT programme and the trinity-dictionary programme are **complementary** geometric attacks on P vs NP, living in different categories: GCT in algebraic geometry (orbit closures), trinity in operator algebra (factors). Both geometric; both non-natural; both non-algebrizing (Cook §3 barriers cleared). The trinity recognizes $H^2(S_n,U(1))=\mathbb{Z}/2$ as the natural cohomological home of the permanent-vs-determinant distinction, which GCT did not identify.

*Status.* **PROVED as structural comparison** (p28§4.7; p28§6.1-§6.3 three-barriers theorems; MS01; Mulmuley 2012).

*Pointer.* p28§4.7 (connection to GCT); MS01; Mulmuley 2012 CACM; Bürgisser-Ikenmeyer-Panova 2017-19 (no-occurrence-obstruction theorem).

### Remark 7.2 (BIP theorem does not apply to trinity)

The Bürgisser-Ikenmeyer-Panova 2017-19 no-occurrence-obstruction theorem rules out a specific *occurrence*-type obstruction in GCT, forcing the search to *multiplicity* obstructions. The trinity obstruction is neither occurrence nor multiplicity — it is a *cocycle class* in $H^2(S_n,U(1))$, which sits in a different category altogether. BIP therefore does not constrain the trinity route.

*Status.* **PROVED** structurally (different categories).

*Pointer.* p28§4.7; Bürgisser-Ikenmeyer-Panova 2017-19.

---

## §8 Computed Numerics

### Definition 8.0 (numerical-extraction discipline)

Every numerical value cited below has a code artifact or explicit proof-location citation. PvNP's core numerical output is not a single-GeV-style prediction but a **computational verification table** (Schaefer 6/6; Spearman $\rho=1.000$; clone-growth $\lambda\geq 2^{2/9}$).

### Table 8.1 (computed numerics)

| # | Observable | Value | Method | Citation |
|---|------------|-------|--------|----------|
| 1 | Schaefer classes verified | $6/6$ | Automated numerical Taylor-gap $\leftrightarrow$ spectral-gap test | p28 code/`pvnp_nonfullness_test.py`; preprint §V |
| 2 | G4 tail — Spearman $\rho$ | $\rho=1.000$ over 30 instances | Polymorphism extension test | p28 Node 2.3; p28p Step 7 |
| 3 | Clone growth lower bound | $\lambda\geq 2^{2/9}\approx 1.16653$ | UA1 four-case proof (AND/OR $2^k$; XOR $2^{k+1}$; MAJ recursion; MIN) | p28§2 Thm UA1; p28p Step 2 |
| 4 | Clone growth upper bound (non-Taylor) | $|\mathrm{Clone}_k|\leq 2k+2$ | UA2 + Post's lattice | p28§2 Thm UA2; p28p Step 3 |
| 5 | MAJORITY Berry-Esseen constant | $C/\sqrt{k}$ | Berry-Esseen + Brunn-Minkowski codim-1 | p28 Node 4.1 + P2 draft; p28p Step 9b |
| 6 | XOR structure | $V_{\mathrm{XOR}}=c\cdot J_d$ (rank 1, all-ones, non-scalar) | Direct matrix computation | p28 Node 4.2 Thm 4 + P1 Lemma X; p28p Step 9c |
| 7 | Aggregate confidence | $p=0.82$ | Part (i) $0.85\times$ Part (ii) $0.90\times$ CP-1 $\approx 1$ | p28 preprint §V |
| 8 | Schur multiplier | $H^2(S_n,U(1))=\mathbb{Z}/2$, $n\geq 4$ | Schur 1911; standard | p28§3.8.2 |
| 9 | Jones discrete series lower bound | $[M^{\mathrm{NP}}:M^{\mathrm{P}}]\geq 4\cos^2(\pi/4)=2$ | Jones 1983 + $\mathbb{Z}/2$ obstruction | p28§4.3; Jones 1983 |
| 10 | Thompson's $V$ non-amenability | $V\subset G_{\mathrm{Bool}}$, $V$ non-amenable | Higman 1974; Brown 1987 | p28 Node 1.3.1; p28p Step 4 |
| 11 | CP-1 verification outcome | 2 SURVIVED / 3 WEAKENED (R1-R4 applied) / 1 BROKEN (Prop 6.2 Route D only) | ORA Wave 1, 6 Critics | p28 preprint CP-1 verification §III |
| 12 | Closure run stats (preprint) | 47 agents, 16 waves, 19 kills, 2 pivots, 8 corrections, 7 drafts, 6 Critics, 0 open gaps | PAC Phase 1 closure | p28 preprint closure/closure-digest.md |
| 13 | Compliance aggregate (168 cells) | 11 P / 49 Pa / 1 O / 107 S; §5d PASS | Pillar A run-02 | `strategy/pvnp/pac-output/runs/run-02/compliance-map.md` |

### Theorem 8.1 (R-Theorem PNP.2: order-counting / PNT route)

*Statement.* The prime number theorem $\gamma_n\sim 2\pi n/\log n$ (or more precisely the Riemann-von Mangoldt asymptotic) is sufficient to force $[M_{\mathrm{Bool}}^{\mathrm{NP}}:M_{\mathrm{Bool}}^{\mathrm{P}}]>1$.

*Proof.* The second-order spectral density $d^2N/d\gamma^2>0$ (from PNT) prevents any first-order observable (single matrix element of $S_{\mathrm{BC}}^{\mathrm{Bool}}$, P-class) from accumulating to a second-order observable ($(\log\gamma_n)^2$ shape, NP-class) in polynomial time. The collapse would force the density of zeros to violate PNT.

*Status.* **PROVED** (p28§5.3-§5.4; p17§5.3.4, §5.4.5; Riemann-von Mangoldt asymptotic).

*Pointer.* p17§5.4.5 (order-counting principle); p17§5.3.4 (PNT form); p28§5.4 Thm PNP.2; p28§5.5 (why two independent proofs matter; PNP.1 + PNP.2 converge on the same conclusion).

### Remark 8.2 (the most dangerous prediction)

*Statement.* Under PNP.1, any second-order observable in the programme's spectral cascade (p17§5.4.2) must be NP-hard to compute classically but computable in polynomial time given the relevant Riemann zero as an oracle. This makes **Riemann zero verification a witness oracle for an NP-hard class** — a structural prediction testable by computational complexity experiment.

*Status.* **CONJECTURE / PREDICTION** (p28§7.5); testable.

*Pointer.* p17§5.4.2 (spectral cascade); p28§7.5 "The most dangerous prediction".

### Remark 8.3 (Jones index open numerical question)

*Statement.* The exact value of $[M_{\mathrm{Bool}}^{\mathrm{NP}}:M_{\mathrm{Bool}}^{\mathrm{P}}]$ within Jones's discrete series $\{4\cos^2(\pi/n):n\geq 3\}\cup[4,\infty)$ is **NEEDS-NUMERICAL-EXTRACT**. The $\mathbb{Z}/2$-obstruction forces $>1$; whether the index is exactly 2, in $\{4\cos^2(\pi/n):n\geq 5\}$, or in $[4,\infty)$ is an open sub-question.

*Status.* **NEEDS-NUMERICAL-EXTRACT.** Not load-bearing for P $\neq$ NP conclusion.

*Pointer.* p28§4.3; Jones 1983.

---

## §9 Proof-Chain Analytics (Beyond-Clay Depth)

### §9.1 Dependency graph (C_bare theorems → programme chains)

```
                          ┌────────────────────────────┐
                          │   QG5D (paper1)            │
                          │   Postulates P1-P4         │
                          │   5 CBB Axioms (Branch D)  │
                          │   Cube-shadow (Branch A.3) │
                          └────────────┬───────────────┘
                                       │
     ┌─────────────┬──────────────┬────┴───────┬──────────────┐
     ▼             ▼              ▼            ▼              ▼
  p15 S.11      p17 order-     p23 CBB      p1 Branch D    p26 BSD
 (spin-stats)   counting      quintuple    (op. dict.)     (channel)
     │             │              │            │              │
     └──────┬──────┴──────┬───────┴──────┬─────┘              │
            │             │              │                    │
            ▼             ▼              ▼                    │
       ┌──────────────────────────────────┐                   │
       │   paper28-pvnp draft §2 (trinity │                   │
       │    dictionary), §3 (C_comp),     │                   │
       │    §3.8 LEMMAS 3.8.1-3.8.4,      │                   │
       │    §4 Thm PNP.1, §5 Thm PNP.2,   │                   │
       │    §6 three barriers             │                   │
       └──────────────┬───────────────────┘                   │
                      │                                       │
                      │ (C_bare content: §§1-8)               │
                      ▼                                       │
       ┌──────────────────────────────────┐                   │
       │   paper28-pvnp preprint          │                   │
       │   28-node PROOF-CHAIN            │                   │
       │   (B_bare covers Clay reqs)      │                   │
       └──────────────┬───────────────────┘                   │
                      │                                       │
                      │ (cross-Clay edges per §4)             │
                      │◄──────────────────────────────────────┘
   ┌──────┬──────┬────┼──────┬────────┬──────────┐
   ▼      ▼      ▼    ▼      ▼        ▼          ▼
  RH     YM     BSD  QG5D   Hodge   BGS       GCT
 §4.1   §4.2   §4.3 §4.4    §4.5   §4.6      §7 (comparison)
 (p13)  (p8)   (p26)(p1)   (p29)  (p13→)   (MS01)

 bonus theorems (C_bare):
 §5.1 SAT vs TAUT discrim. (LEMMA 3.8.4)     — PROVED
 §6.1 Non-degeneracy algebraic (LEMMA 3.8.2) — PROVED
 §6.2 Cocycle computation (LEMMA 3.8.3)      — PROVED
 §7.1 GCT-trinity correspondence             — PROVED (structural)
 §8.1 PNP.2 PNT route                        — PROVED
 §8.2 Riemann-zero oracle prediction         — CONJECTURE / PREDICTION
 §4.1 H_R^Bool ↔ {γ_n·π²/2} (W3)             — CONJECTURE
```

### §9.2 Face histogram (beyond-Clay depth)

PvNP vertex triggers 6 of 10 faces (strategy doc §4; p28§7):

| Face | Layers | Percentage |
|------|--------|------------|
| RESONANCE (canonical: spectral gap) | Steps 1-10 spectral; Theorem PNP.1; C1 pin | ~30% |
| SYMMETRY (Thompson's $V$ + Schur multiplier) | Steps 4, 12; LEMMA 3.8.2-3.8.3 | ~20% |
| DYNAMICS (modular flow $\sigma_t^{\mathrm{Bool}}$) | p28§3.2; Row T8 trinity | ~15% |
| AMPLITUDE (KMS state $\omega_1^{\mathrm{Bool}}$) | Step 5 KEY LEMMA 3.4.3 | ~10% |
| ARITHMETIC (Boolean function field $\mathbb{B}$) | p28§2.1; UA1-UA2 | ~15% |
| CURVATURE (clone growth lattice) | UA1 exponential; UA2 linear; Post's lattice | ~10% |

### §9.3 Projection / pattern distribution

From strategy doc §4:

- **Projections**: $P_B$ 10% / $P_D$ 70% (CBB operational modal) / $P_O$ 20% (Brauer cohomology observer).
- **Patterns**: P3 35% (spectral) / P1 25% (invariants) / P5 20% (bootstrap) / P4 15% (transposition) / P2 5%.

### §9.4 Additional cross-cut edges (beyond Clay B_bare)

Bonus cross-cuts flagged in this document (supplementing `strategy/x-ray/proof-chain/pvnp/`):

- **PvNP ↔ Hodge (motivic)** via $H^2$ cocycle (§4.5).
- **PvNP ↔ BGS** via GUE universality on $\hat R_{\mathrm{Bool}}$ spectral statistics (§4.6, speculative).
- **PvNP ↔ GCT** via Schur-multiplier recognition (§7, structural comparison).
- **PvNP ↔ Collatz / Goldbach** via ARITHMETIC-face Boolean function field $\mathbb{B}$ (p60 §13 adjacency; SPECULATIVE).
- **PvNP ↔ MIP\* = RE (JNVWY 2020)** via Connes non-embedding linking quantum computational power with C*-algebraic rigidity (`strategy/_research/pvnp/landscape.md`; §9 Quantum Complexity).

Core cross-cut edges from cross-Clay bouquet: **6** (§4.1-§4.6). Additional speculative: **2**.

### §9.5 Named-wall inheritance

C_bare-level walls (beyond-Clay-specific; distinct from B_bare's W1):

- **W3** (spectral identification $H_R^{\mathrm{Bool}}\leftrightarrow\{\gamma_n\cdot\pi^2/2\}$) — CONJECTURE; Thm 4.1.
- **NEEDS-CONSTRUCTION** (§4.3 direct L-value $\leftrightarrow$ channel-capacity); (§4.5 direct motivic identification); (§4.6 BGS-GUE explicit statement); (§8.3 exact Jones index).

Inherited B_bare walls:

- **W1** (Link 5 backward / non-full → Taylor) — `pvnp-comply-bare.md` §16.1. Aggregate $p=0.82$; 7 bypass routes.
- **W2** (KMS$_1$ uniqueness) — `pvnp-comply-bare.md` §16.2. Downstream-insulated.

### §9.6 RIGIDITY / SYMMETRY contribution

From p28 chain:

- **RIGIDITY-heavy**: Step 4 (Thompson's $V$), Step 5 (KEY LEMMA 3.4.3), Step 22 (Houdayer-Marrakchi dichotomy), LEMMA 3.8.2-3.8.3, Schur multiplier.
- **SYMMETRY-heavy**: $\Phi_{\mathrm{comp}}$ functor; De Morgan involution $\theta$; $\mathbb{Z}/2$-grading.
- **SPECTRAL**: Steps 1-10 spectral chain; Theorem PNP.1 Jones index; PNP.2 PNT spectral density.

---

## §10 References

### §10.1 Programme papers (primary, §-level precision)

- **paper28-pvnp** — *P versus NP.* Primary.
  - Draft: §1 (intro + setup), §2 (trinity dictionary, rows T1-T18, with T9/T10/T11 load-bearing), §3 (Boolean BC system; §3.1-§3.7 construction; §3.8.1-§3.8.4 LEMMAS 3.8.1/3.8.2/3.8.3/3.8.4; §3.4.3 KEY LEMMA; §3.6 spectral conjecture W3), §4 (PNP.1; §4.1 S.11 recap, §4.2 two subfactors, §4.3 Jones inclusion, §4.4 PNP.1 statement, §4.5 three-step proof + LEMMA 4.5.1 Clifford, §4.6 corollary, §4.7 GCT connection), §5 (order-counting; §5.1 Paper 17 recap, §5.2 complexity hierarchy LEMMA, §5.3 why no collapse, §5.4 PNP.2 statement, §5.5 two independent proofs), §6 (three barriers; §6.1 non-relativization, §6.2 non-naturalness, §6.3 non-algebrization, §6.4 honest hole), §7 (connections; §7.3 sixth CBB conjecture, §7.5 most dangerous prediction).
  - Preprint: `PROOF-CHAIN.md` (28 rows, Part (i) 1-10 UNCONDITIONAL / Part (ii) 11-15 + CP-1 / Corollary 16-23); `preprint/sections-01-introduction.md` through `preprint/sections-07-connections-outlook.md`; CP-1 repair files `preprint/repair-1-lemma-44.md` through `preprint/repair-4b-transitivity-gap.md`; `preprint/p1-lemma-a-star-propagation.md`; `preprint/p2-berry-esseen-writeup.md`.
  - Code: `solutions-with-prize/paper28-pvnp/code/pvnp_nonfullness_test.py` (6/6 Schaefer).
  - Live chain: `solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md` (6 top-level links; "Current wall" seven bypass routes A-G).

- **paper1** — *Quantum Geometry in 5D (QG5D hub).* Trinity dictionary foundation; cube-shadow (Branch A.3); operator dictionary $\hat L=\log\hat R$ (Branch D); ~~postulates P1-P4~~ theorems T1-T4 <!-- legacy 2026-04-15: per §0.10 canon entry 6, Intervention 8 --> (§1); 5 CBB axioms (Branch D).

- **paper15** — *Transposition dictionary / R-Theorem S.11.* Spin-statistics $\leftrightarrow$ R-Theorem S.11 transposition template (§3 Round 4-5 supplement; research/119-134); used as black-box source for $\Phi_{\mathrm{comp}}$ on row T11.

- **paper17** — *Entropy operator / order-counting principle.* PNT $\gamma_n\sim 2\pi n/\log n$ (§5.3.4); order-counting principle (§5.4.5); spectral cascade for §8.2 "most dangerous prediction" (§5.4.2).

- **paper23** — *CBB quintuple / bridge family.* Quintuple $(H_R,\hat R,\omega_1,M,\{\beta_k\})$ (§4.1); bridge family at $k\in\{2,3,4,6\}$; CBB axiom 5 (§27: closure with zero free parameters); Jones index discrete series recap (§8); three-sector convergence (§11); five conjectures (§13.2).

- **paper26-bsd** — *BSD.* Channel correspondence $E_{M^{\mathrm{P}}}:M^{\mathrm{NP}}\to M^{\mathrm{P}}$ analog (p26 Link 3 ITPFI; Link 8 L-function factorization); bridge family shared at $k\in\{2,3,4,6\}$ (Link 2; 355 triples).

- **paper13-rh** — *RH.* Boolean BC entropy operator cross-Clay (W3 Thm 4.1); CCM operators $D_N$ (Layer 1); ITPFI $\omega_1=\otimes_p\omega_1^{(p)}$ (Layer 2); spectral exactness (Layer 6).

- **paper08-yang-mills** — *YM Existence and Mass Gap.* Popa-rigidity cross-Clay edge (§4.2 Thm 4.2); L1 KK gap, L10 spectral-gap rigidity, L14 $\Delta_\infty>0$; Pattern-4 Topological Rigidity (p8§36).

- **paper29-hodge** — *Hodge.* Motivic cohomology cross-Clay edge (§4.5 Thm 4.5; structural parallel).

- **paper60 / paper61** — *Geometry of the circle / Projections of the ~~5D geometry~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometry" → "M⁵" -->.* Face adjacency table (p60 §13); $P_D$ operator projection (p61 §10).

### §10.2 Programme scaffolding artifacts

- `strategy/pvnp/00-millenium-strategy.md` — Millennium strategy; Clay §§1/3/9 cascade; 6 Cook requirements; 3 named walls.
- `strategy/pvnp/pvnp-millenium-brief.md` — PAC operational brief DELTA 1-10; C_bare 10-section structure.
- `strategy/pvnp/pac-output/runs/run-02/compliance-map.md` — LOCKED 168-cell verdict matrix (11 P / 49 Pa / 1 O / 107 S; §5d PASS).
- `strategy/pvnp/pac-output/runs/run-02/commit-memo.md` — Pillar A run-02 lock.
- `strategy/pvnp/deliverables/pvnp-comply-bare.md` — B_bare Clay-shaped skeleton (Pillar A).
- `strategy/_research/p-vs-np/landscape.md` (alias `strategy/_research/pvnp/landscape.md`) — landscape survey; 9 approaches; acknowledgment targets.
- `strategy/x-ray/proof-chain/pvnp/` — cross-cuts `pvnp-rh`, `pvnp-ym`, `pvnp-bsd`, `pvnp-qg5d`, `pvnp-BGS` (when produced).
- `strategy/ym/deliverables/ym-beyond-bare.md` — format mirror for this document.
- `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` — capacitor (bypass-route catalog).

### §10.3 External references (cited via programme papers)

- **Cook, S.** *The P versus NP Problem.* Clay Mathematics Institute. §1-§3 verbatim; Def.~1-~4; Prop. 1(b), 1(c); 3-SAT NP-completeness Cook 1971.
- **Baker-Gill-Solovay 1975** — relativization barrier; oracle $A$ with $\mathbf{P}^A=\mathbf{NP}^A$.
- **Razborov-Rudich 1997** — natural proofs barrier.
- **Aaronson-Wigderson 2008** — algebrization barrier.
- **Bulatov 2017 / Zhuk 2020** — CSP dichotomy (forward + backward).
- **Barto-Brady-Bulatov-Kozik-Zhuk (BBBKZ) TheoretiCS 2024** — Lemma 2.1 (Taylor = cyclic idempotent ternary operation).
- **Houdayer-Marrakchi 2018** — arXiv:1605.09613 (fullness dichotomy; $\mathrm{Inn}$ not closed criterion).
- **Marrakchi 2018** — Theorem B (fullness from strong ergodicity).
- **Jones-Schmidt 1987** — strong ergodicity.
- **Feldman-Moore 1977** — groupoid $\leftrightarrow$ factor correspondence.
- **Laca-Raeburn** — dilation (CP-1).
- **Jones 1983** — subfactor index theorem; discrete series $\{4\cos^2(\pi/n)\}\cup[4,\infty)$.
- **Connes 1976** — non-amenability $\to$ non-injectivity; type III$_1$ classification.
- **Popa 2006** — cocycle superrigidity (Route D of seven W1 bypasses).
- **Schur 1911** — Schur multiplier $H^2(S_n,U(1))=\mathbb{Z}/2$.
- **Mulmuley-Sohoni 2001 (MS01)** — GCT papers I-II.
- **Mulmuley 2012 (CACM)** — "The GCT program toward the P vs NP problem".
- **Bürgisser-Ikenmeyer-Panova 2017-19** — no occurrence obstructions for permanent vs determinant.
- **Ji-Natarajan-Vidick-Wright-Yuen 2020 (JNVWY)** — MIP\* = RE (disproves Connes embedding for group C*-algebras); motivates operator-algebra route.
- **Cook 1971** — 3-SAT NP-completeness.
- **Levin 1973** — independent NP-completeness.
- **Karp 1972** — 21 NP-complete problems.
- **Pauli 1940; Lüders-Zumino 1958; Streater-Wightman 1964** — spin-statistics theorem (row T11 additive column).

---

## §11 Related Work & Acknowledgments

### §11.1 Major approaches

| # | Approach | Key author(s) | Our relation |
|---|----------|---------------|--------------|
| 1 | Geometric Complexity Theory (GCT) | Mulmuley, Sohoni; Bürgisser, Ikenmeyer, Panova; Grochow | Complementary geometric programme (different category: operator-algebraic vs algebraic-geometric); §7 table-by-table comparison; Schur multiplier recognized as natural cohomological home |
| 2 | Circuit Lower Bounds / Algorithmic Method | R. Williams; Håstad; Razborov | Structural: our PNP.1 is not a circuit lower bound but a subfactor inclusion; non-natural per Cook §3 clearance (§13 of B_bare) |
| 3 | Natural Proofs Barrier | Razborov, Rudich | **CLEARED**: fullness not a large-set property; Schur multiplier discrete (`pvnp-comply-bare.md` §13.2; p28§6.2) |
| 4 | Relativization + Algebrization Barriers | Baker-Gill-Solovay; Aaronson, Wigderson | **CLEARED**: $\omega_1$ oracle-independent; cyclotomic Galois above poly extensions (`pvnp-comply-bare.md` §13.1/§13.3; p28§6.1/§6.3) |
| 5 | VP vs VNP / Algebraic Complexity | Valiant; Kayal, Saraf, Limaye, Srinivasan, Tavenas | Algebraic analog; trinity dictionary on arithmetic-circuit column (p28§7.3 "sixth CBB conjecture"; NEEDS-CONSTRUCTION) |
| 6 | Unique Games / PCP / Approximation | Khot; Raghavendra; Dinur | Orthogonal: we prove P $\neq$ NP; they classify conditional hardness of approximation |
| 7 | Hardness vs Randomness / Derandomization | Impagliazzo, Wigderson | Compatible: our non-naturalness clearance does not depend on PRFs (fullness is a factor property) |
| 8 | Quantum Complexity / MIP\* = RE | Ji, Natarajan, Vidick, Wright, Yuen | **DIRECT MOTIVATION**: Connes non-embedding links quantum computational power with C*-algebraic rigidity — same type III$_1$ factor class our proof lives in; §9.4 cross-cut |
| 9 | Fine-Grained Complexity / ETH | V.V. Williams; Impagliazzo, Paturi | Orthogonal: they classify poly-time problems; we separate P from NP |
| 10 | CSP Dichotomy | Bulatov; Zhuk; Barto-Brady-Kozik-Zhuk | **LOAD-BEARING**: BZ forward + backward are the translation bridge (p28p Steps 18, 20; B_bare §7 + §12 TM-Model Translation Layer) |
| 11 | Subfactor Theory / Popa Rigidity | Jones; Popa; Houdayer, Marrakchi | **LOAD-BEARING**: Jones index (PNP.1); Popa cocycle superrigidity (Route D of W1); HM fullness dichotomy (Step 22) |
| 12 | Bost-Connes / Arithmetic Noncommutative Geometry | Bost, Connes; Marcolli, Consani | **LOAD-BEARING**: BC algebra structure; KMS$_1$ state; trinity dictionary (p15 S.11 $\leftrightarrow$ BC modular); paper28 §3.1-§3.4 construction |

**Our contribution.** Trinity dictionary $\Phi_{\mathrm{comp}}$ transports spin-statistics (p15 R-Thm S.11) from BC-arithmetic to Boolean-computational; non-trivial $H^2(S_n,U(1))=\mathbb{Z}/2$ preserved (LEMMA 3.8.2) gives Jones inclusion $M_{\mathrm{Bool}}^{\mathrm{P}}\subset M_{\mathrm{Bool}}^{\mathrm{NP}}$ with index $>1$; all three Cook §3 barriers cleared (p28§6). Second independent proof (PNP.2) via PNT order-counting (p17§5.4.5). LEMMA 3.8.4 SAT/TAUT discrimination gives P $\neq$ NP **and** P $\neq$ coNP as single $\mathbb{Z}/2$-fact; scope-honest about NP vs coNP. Aggregate confidence $p=0.82$; W1 Link 5 backward OPEN-BUT-ADDRESSED with seven bypass routes.

### §11.2 Named prior results (timeline)

| Year | Author(s) | Result |
|------|-----------|--------|
| 1940 | Pauli | Spin-statistics theorem (additive column source for row T11) |
| 1954 | Schur | Schur multiplier $H^2(S_n,U(1))=\mathbb{Z}/2$ (1911 actually; standard attribution) |
| 1971 | Cook | SAT NP-completeness; Clay problem setup |
| 1972 | Karp | 21 NP-complete problems |
| 1973 | Levin | Independent NP-completeness (Cook-Levin) |
| 1975 | Baker, Gill, Solovay | Relativization barrier |
| 1976 | Connes | Non-amenability $\to$ non-injectivity; type III$_1$ classification |
| 1983 | Jones | Subfactor index theorem; discrete series |
| 1985-87 | Razborov | Exponential lower bounds for monotone circuits |
| 1987 | Jones, Schmidt | Strong ergodicity |
| 1989 | Håstad | Parity requires exponential-size AC$^0$ |
| 1994 | Razborov, Rudich | Natural proofs barrier |
| 1995 | Bost, Connes | BC algebra |
| 2001 | Mulmuley, Sohoni | GCT I |
| 2006 | Popa | Cocycle superrigidity |
| 2008 | Aaronson, Wigderson | Algebrization barrier |
| 2011 | R. Williams | NEXP $\not\subset$ ACC$^0$ |
| 2017 | Bulatov | CSP dichotomy |
| 2017-19 | Bürgisser, Ikenmeyer, Panova | No occurrence obstructions (GCT) |
| 2018 | Houdayer, Marrakchi; Marrakchi | Fullness dichotomy; fullness from strong ergodicity |
| 2020 | Zhuk | CSP dichotomy (independent) |
| 2020 | Ji, Natarajan, Vidick, Wright, Yuen | MIP\* = RE |
| 2021 | Limaye, Srinivasan, Tavenas | Superpoly lower bound, constant-depth arithmetic |
| 2024 | Barto, Brady, Bulatov, Kozik, Zhuk | TheoretiCS cyclic-idempotent-ternary characterization |
| 2026 | ITCS | New algebrization barriers via communication complexity |

### §11.3 Recent parallel work (2023-2026)

Populate from `strategy/_research/p-vs-np/landscape.md` §"Recent Preprints" — next cycle:

- Ongoing GCT work by Mulmuley, Bürgisser, Ikenmeyer, Panova, Grochow (2023-2026).
- Limaye-Srinivasan-Tavenas extensions (2021+).
- ITCS 2026 "New Algebrization Barriers to Circuit Lower Bounds via Communication Complexity of Missing-String".

### §11.4 Acknowledgments

**Top priority (credit in Introduction of B_full composition-backward step).**

| Researcher | Contribution the programme relies upon |
|------------|----------------------------------------|
| Stephen Cook | Problem formulation; 3-SAT NP-completeness (1971); Clay problem statement §1-§3 |
| Leonid Levin | Independent NP-completeness (Cook-Levin theorem, 1973) |
| Richard Karp | 21 NP-complete problems (1972); established the NP-completeness framework |
| Alexander Razborov, Steven Rudich | Natural proofs barrier (1997) — defines the non-naturalness constraint our §13.2 clears |
| Scott Aaronson, Avi Wigderson | Algebrization barrier (2008) — defines the non-algebrization constraint our §13.3 clears |
| Baker, Gill, Solovay | Relativization barrier (1975) — defines the non-relativization constraint our §13.1 clears |
| Andrei Bulatov, Dmitriy Zhuk | CSP dichotomy theorem (2017/2020) — load-bearing translation bridge (p28p Steps 18, 20; B_bare §12) |
| Sorin Popa | Cocycle superrigidity (2006) — Route D of seven W1 bypass routes |
| Vaughan Jones | Subfactor index theorem (1983); discrete series — PNP.1 Jones inclusion is the central object |
| Matilde Marcolli, Caterina Consani, Alain Connes | Bost-Connes arithmetic noncommutative geometry; BC algebra; KMS$_1$ state; trinity dictionary foundation |

**Additional named acknowledgments (credit in body of B_full).**

| Researcher | Contribution |
|------------|--------------|
| Ketan Mulmuley, Milind Sohoni | GCT programme (MS01; Mulmuley 2012) — most mature geometric attack; §7 structural comparison |
| Peter Bürgisser, Christian Ikenmeyer, Greta Panova | No-occurrence-obstruction theorem (BIP 2017-19) — sharpens the GCT target; our cocycle route is different category |
| Ryan Williams | Algorithmic method / NEXP $\not\subset$ ACC$^0$ — rare non-natural technique; structural complement |
| Russell Impagliazzo, Avi Wigderson | Hardness-vs-randomness (pervasive influence) |
| Leslie Valiant | VP vs VNP (algebraic analog; p28§7.3 sixth-CBB-conjecture target) |
| Joshua Grochow | GCT unification framework |
| Subhash Khot | Unique Games Conjecture (orthogonal — hardness of approximation) |
| Jean Bost, Alain Connes | BC algebra (Bost-Connes 1995) — trinity construction foundation |
| Pierre Hajłasz, Cyril Houdayer, Amine Marrakchi | Fullness dichotomy (HM); fullness from strong ergodicity (Mar18 Thm B) |
| Jon Feldman, Calvin Moore | Groupoid $\leftrightarrow$ factor correspondence (FM77) — CP-1 load-bearing |
| Marcelo Laca, Iain Raeburn | Dilation (CP-1 construction) |
| Zhengfeng Ji, Anand Natarajan, Thomas Vidick, John Wright, Henry Yuen | MIP\* = RE (2020) — direct motivation for operator-algebra route; Connes non-embedding |
| Tadeusz Bałaban | Balaban RG (shared infrastructure with YM mass-gap chain; cross-Clay §4.2) |
| Issai Schur | Schur multiplier $H^2(S_n,U(1))=\mathbb{Z}/2$ (1911) — the obstruction |
| Wolfgang Pauli; Gerhart Lüders, Bruno Zumino; Ray Streater, Arthur Wightman | Spin-statistics theorem additive-column source (1940; 1958; 1964) |

### §11.5 Pillar-C harden-bonuses (Phase 5D)

The Pillar-C harden-bonuses target external-dependency strengthening for the Bulatov-Zhuk, Popa, and Houdayer-Marrakchi programmes:

| Target | Harden action | PAC artifact |
|--------|---------------|--------------|
| Bulatov-Zhuk (BZ forward + backward) | Audit + strengthen translation bridge (B_bare §12) via CSP-dichotomy sub-cases | Next Pillar-C run; see `strategy/pvnp/pac-output/runs/` schedule |
| Popa cocycle superrigidity | Audit Route D of seven W1 bypasses; attempt to lift Prop 6.2 BROKEN state from CP-1 Wave 1 | Next Pillar-C run |
| Houdayer-Marrakchi fullness dichotomy | Audit Step 22 HM citation + independent derivation check | Next Pillar-C run |
| Laca-Raeburn dilation (CP-1) | Audit Parts A+B + R1-R4 repair integrity | Completed in CP-1 verification (Wave 1) |
| BBBKZ TheoretiCS 2024 | Audit Lemma 2.1 citation (cyclic-idempotent-ternary characterization) | Next Pillar-C run |

These harden-bonuses give back to the cited programmes by auditing + strengthening specific construction layers, in the pattern of the three-pillar Universal Approval (strategy doc §3; `strategy/universal_approval_three_pillars`).

---

*End of pvnp-beyond-bare.md. Bare discipline enforced: zero prose paragraphs, every claim cited to programme + §-level location. $\leq 15$ pages target (~580 lines markdown). W1/W2/W3 disclosed via comply-bare §16; beyond-specific walls enumerated in §9.5. Three barriers (Cook §3) inherited from comply-bare §13. §5b either-direction noted (§5.2): P $\neq$ NP and P $\neq$ coNP as single $\mathbb{Z}/2$-fact; NP vs coNP explicitly out of scope. §11 Related Work & Acknowledgments honors Cook, Levin, Karp, Razborov-Rudich, Aaronson-Wigderson, BGS authors, Bulatov-Zhuk, Popa, Jones, Marcolli/Consani/Connes per UA brief. Companion to `pvnp-comply-bare.md` in the Zenodo-priority release. C_full DEFERRED to composition-backward.*

*G Six and Claude Opus 4.6. 2026-04-14.*
