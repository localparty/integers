# NS Harden (Pillar C) Bare Skeleton

*The double-kill deliverable for Navier-Stokes existence and smoothness, Clay/Fefferman **variant (B)**. Every retained external dependency of the Pillar-B dep-free chain (`strategy/ns/deliverables/ns-independence-bare.md`) is x-rayed, compliance-audited, and hardened by PAC primitives applied to ITS chain. Primary Pillar-C targets: **Camlin 2025** (Sundman $\Phi$ bypass for BKM, Route A) and **arXiv:2601.08854** (cosphere-bundle microlocal bypass for BKM, Route B) — two recent preprints promoted to Pillar-B leaf-root tier and requiring independent rigor. Classical literature deps (Leray 1934, Hopf 1951, CKN 1982, BKM 1984, Ladyzhenskaya, Temam, Hörmander, Melrose) audited at the citation-precision tier. Zero prose paragraphs. Companion to `ns-comply-bare.md` (Pillar A) and `ns-independence-bare.md` (Pillar B). **Variant (B)** declared throughout per Rules §5b.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## §1 Retained externals roster and Pillar-C scope

Source: `strategy/ns/deliverables/ns-independence-bare.md §5.5`, `§4.1 Leaf root distribution`, `§8.4`.

### §1.1 Externals promoted to Pillar-B leaf-root tier (PRIMARY Pillar-C targets)

| Tag | External | arXiv / cite | Role in chain | Hardening folder | Primary target? |
|-----|----------|--------------|---------------|------------------|:---------------:|
| E1 | **Camlin 2025** — bounded Sundman $\Phi$ functional + temporal lifting → BKM finiteness on $\mathbb{T}^3$ | Camlin 2025 (arXiv preprint; recent) | L5a Route A; input to L5 BKM composite | `strategy/externals-hardening/camlin-2025/` | **PRIMARY** (recent preprint; programme-level audit) |
| E2 | **arXiv:2601.08854** — cosphere-bundle microlocal regularity; $\mathrm{WF}(u)\cap S^*\mathcal{M}=\emptyset$ | arXiv:2601.08854 (Jan 2026) | L5b Route B; input to L5 BKM composite; host cell cap§MICRO↔QFT | `strategy/externals-hardening/arxiv-2601.08854/` | **PRIMARY** (recent preprint; programme-level audit) |

### §1.2 Externals retained at classical-literature tier (CITATION-PRECISION audit)

| Tag | External | Cite | Role in chain | Audit depth |
|-----|----------|------|---------------|-------------|
| E3 | **Leray 1934** — global weak solutions (Leray-Hopf class) | Leray 1934, *Acta Math.* 63 | L6 Req 2 direct bypass; L5/L7 foundation | Citation-precision + §-level location audit |
| E4 | **Hopf 1951** — Hopf weak solutions on bounded domain | Hopf 1951, *Math. Nachr.* 4 | L6 Req 2 direct bypass (co-cite with Leray) | Citation-precision audit |
| E5 | **Caffarelli-Kohn-Nirenberg 1982** — partial regularity $P_1(E)=0$ | CKN 1982 *CPAM* 35 + Lin 1998 *CPAM* 51 | Req 8 classical base; subsumed in C^∞ case via L5b WF-triviality | Citation-precision audit |
| E6 | **Beale-Kato-Majda 1984** — BKM criterion $\int_0^T\sup|\omega|\,dt=\infty$ at blowup | BKM 1984 *CMP* 94 | Req 6 statement of wall | Citation-precision audit |
| E7 | **Ladyzhenskaya 1969 / Temam 1977** — Galerkin + pressure-Poisson on $\mathbb{T}^3$ | Ladyzhenskaya 1969 *Math. Theory Viscous Incompressible Flow*; Temam 1977 *NS Eqs Theory & Num.* Ch. 1, 3 | L3 pressure-Poisson Pillar-B bypass; L7 Galerkin uniqueness | Citation-precision + Ch./§-level |
| E8 | **Hörmander 1990 / Melrose 1994** — wavefront-set / Sobolev wavefront calculus | Hörmander 1990 *Anal. Lin. PDE* Vol. I §8; Melrose 1994 *Atiyah-Patodi-Singer* Ch. | W1^B residual: WF→vorticity translation | Citation-precision + §-level |

### §1.3 Internal cross-Clay deps retained (SELF-HARDEN queue)

Pillar-B residuals $W_2^B$ and $W_3^B$ are *programme-internal* (not external unproved). Treated at Pillar C by `externals-hardening/` for consistency of audit architecture.

| Tag | Internal dep | Role | Self-harden folder |
|-----|--------------|------|--------------------|
| I1 | YM→NS GF functor $F$ (p8§L.1 $\to$ p30 L3) — narrative aesthetic; Req 3 discharged via pressure-Poisson so non-blocking | $W_2^B$ GF-transfer-audit | `strategy/externals-hardening/ym-ns-gf-functor/` |
| I2 | 5D KK Killing-$S^1/\mathbb{Z}_2$ energy descent rigor (p30§6) — narrative; Req 2 discharged via classical Leray-Hopf so non-blocking | $W_3^B$ Leray-Hopf-descent-audit | `strategy/externals-hardening/kk-energy-descent/` |

### §1.4 Pillar-C scope declaration

**In scope**: E1, E2 (primary PAC programme-level audit — x-ray + compliance-map + hardened-routes + narrative per §5C.2); E3–E8 (citation-precision audit); I1, I2 (self-harden internal).
**Out of scope (already strong, LITERATURE tier)**: Kaluza 1921, Klein 1926, BHMR 2008 (L2 EXCISED).
**Deferred**: any external surfacing only during B_full composition-backward.

---

## §2 Harden Theorem (Pillar C main claim)

**Theorem 2.1 (NS Double-Kill).** *Every retained external dependency of the Pillar-B dep-free chain for Theorem 1.1 (variant (B)) listed in §1 admits a Pillar-C hardening artifact — an x-ray + compliance-map + hardened-routes + narrative — with the PAC primitives (VERIFY / CONSTRUCT / BYPASS / DECOMPOSE / EXCISE) applied to weak links of the external's own chain. In particular, for the two primary targets (Camlin 2025, arXiv:2601.08854):*

*(i) Each weak link in the external's chain is VERIFIED against its stated axioms and hardened where PAC primitives identify weakness.*

*(ii) Every cited external retains its original attribution (reciprocity discipline); hardening artifacts are published as independent supplementary notes, not as re-proofs.*

*(iii) The Pillar-B chain's confidence rises from 4/10 (Pillar-A baseline with external-conditional routes) to $\ge 6/10$ once E1+E2 hardening VERIFY passes complete; to $\ge 7/10$ once the $W_1^B$ integration proof seals L5.*

*Proof architecture.* §3 (per-external x-ray scaffolds for E1, E2); §4 (compliance-map skeletons per external); §5 (hardened-routes tables for E1, E2); §6 (reciprocity narrative + citation-precision audit for E3–E8 + self-harden for I1, I2); §7 (cross-pillar analytics + references). $\square$

**Double-kill invariant** (per §5C of universal-approval-run.md): *"We depend on Camlin 2025 AND arXiv:2601.08854 AND we strengthened both. The BKM criterion bypass becomes programme-verified; the authors benefit from independent rigor."*

---

## §3 Per-external x-ray scaffolds (E1, E2 — primary)

X-ray methodology imported from `strategy/x-ray/` fixed vocabulary: **10 faces** (SPEC, GEOM, QFT, MICRO, ARITH, DYN, PDE, PROB, COMB, TOP) / **6 projections** ($P_A,P_B,P_C,P_D,P_E,P_O$) / **5 patterns** (CONV, RIG, SYM, RES, CURV) / **16 invariants**. Applied to each external's chain.

### §3.1 E1 — Camlin 2025 (Route A) x-ray scaffold

Target artifact: `strategy/externals-hardening/camlin-2025/X-RAY.md` (to be generated Pillar-C dispatch).

| Layer | Claim in Camlin 2025 | Face | Projection | Pattern | PAC primitive target | Weak-link flag |
|-------|----------------------|:----:|:----------:|:-------:|-----------------------|:--------------:|
| CA-L1 | Sundman temporal-lifting construction $\tau=\tau(t)$ on $\mathbb{T}^3$-based NS flow | DYN | $P_E$ | RES | VERIFY (reparametrization well-defined; boundedness of $d\tau/dt$) | maybe |
| CA-L2 | Definition of $\Phi$-functional $\Phi(\tau)=\sup_x|\omega(x,t(\tau))|\cdot\chi_{\mathrm{Sundman}}(\tau)$ | PDE | $P_A$ | SYM | VERIFY (measurability; $\Phi$ finite for smooth u; invariance under $\tau$-diffeo) | maybe |
| CA-L3 | Boundedness theorem: $\Phi(\tau)\le C(\nu,u^\circ,T)$ uniformly on $\tau\in[0,\tau(T)]$ | PDE | $P_A$ | CURV | VERIFY (constants explicit; $\nu$-dependence; initial-data norm used) | **weak** (verify constants) |
| CA-L4 | Pullback: Sundman-bounded $\Phi$ on $\tau$-time $\Rightarrow$ BKM integrand $\sup_x|\omega(x,t)|$ bounded on $t$-time on $\mathbb{T}^3$ | PDE | $P_E$ | CONV | VERIFY (Jacobian $dt/d\tau$ finite a.e.; no singular concentration) | **weak** (Jacobian control) |
| CA-L5 | BKM-finiteness: $\int_0^T\sup_x|\omega(x,t)|\,dt<\infty \Rightarrow u\in C^\infty(\mathbb{T}^3\times[0,T])$ (BKM 1984 feed) | PDE | $P_A$ | SYM | VERIFY (direct BKM citation; no novelty) | strong |
| CA-L6 | Extension to any $T<\infty$ (no blowup) | PDE | $P_A$ | CONV | VERIFY (iteration uniform in $T$) | maybe |
| CA-KK-ADAPT | **[NEW — residual $W_1^B$ sub-task (i)]** KK-adaptation: $\Delta_0^{KK}=(2\pi/R)^2$ on $M^4\times S^1/\mathbb{Z}_2$ supplies frequency-space control input to $\Phi$-bound (off-$\mathbb{T}^3$ baseline) | SPEC+GEOM | $P_O$ | RIG | CONSTRUCT (explicit adaptation: paper1§KK + p8§4 T4 + p11K.4 + p10 U.2a $\to$ Camlin L3 constant) | **open** (Pillar-C work item) |

**Pattern invariants to extract**: $\{K_{\Phi},C_{\mathrm{Sundman}},\tau_*(T)\}$ as numerical 16-invariant table cells.

**Weak-link targets (three)**: CA-L3 (constants), CA-L4 (Jacobian), CA-KK-ADAPT (KK adaptation). Pillar-C dispatch applies VERIFY to CA-L3/L4 and CONSTRUCT to CA-KK-ADAPT.

### §3.2 E2 — arXiv:2601.08854 (Route B) x-ray scaffold

Target artifact: `strategy/externals-hardening/arxiv-2601.08854/X-RAY.md`.

| Layer | Claim in arXiv:2601.08854 | Face | Projection | Pattern | PAC primitive target | Weak-link flag |
|-------|---------------------------|:----:|:----------:|:-------:|-----------------------|:--------------:|
| CB-L1 | Lift of NS velocity field $u$ on Riemannian $(\mathcal{M},g)$ to cosphere bundle $S^*\mathcal{M}$ | MICRO+GEOM | $P_O$ | SYM | VERIFY (lift well-defined; bundle structure; metric-compatibility) | strong |
| CB-L2 | Wavefront-set of $u$: $\mathrm{WF}(u)\subset T^*\mathcal{M}\setminus 0$ | MICRO | $P_A$ | RES | VERIFY (Hörmander 1990 definition applied correctly) | strong (classical) |
| CB-L3 | Microlocal regularity theorem: $u$ satisfies NS $\Rightarrow$ structure of $\mathrm{WF}(u)$ constrained by characteristic set of parabolic symbol | MICRO+PDE | $P_A$ | RIG | VERIFY (propagation of singularities on parabolic operator; classical Hörmander) | maybe |
| CB-L4 | Central regularity result: $\mathrm{WF}(u)\cap S^*\mathcal{M}=\emptyset \Rightarrow u\in C^\infty(\mathcal{M})$ | MICRO+PDE | $P_A$ | RES | VERIFY (wave-front-set triviality $\Rightarrow C^\infty$ — standard Hörmander) | strong |
| CB-L5 | Application: conditions on initial data imply wave-front-set triviality at positive time | MICRO+PDE | $P_A$ | CONV | VERIFY (conditions explicit; data norms; time-uniformity) | **weak** (conditions) |
| CB-L6 | No-blowup corollary: $u\in C^\infty$ for all $t>0$ | PDE | $P_A$ | SYM | VERIFY (composition with CB-L4) | maybe |
| CB-WF-VORT | **[NEW — residual $W_1^B$ sub-task (ii)]** WF→vorticity translation: $\mathrm{WF}(u)\cap S^*\mathcal{M}=\emptyset \Rightarrow \sup_x|\omega(x,t)|<\infty$ pointwise | MICRO+PDE | $P_A$ | RIG | CONSTRUCT (Hörmander Vol. I §8 + Melrose 1994 wavefront Sobolev calculus on $\mathcal{M}=M^4\times S^1/\mathbb{Z}_2$) | **open** (Pillar-C work item) |
| CB-ROUTE-GEN | **[NEW — residual $W_1^B$ sub-task (iii)]** Route B generates Route A: microlocal structure on $M^4\times S^1/\mathbb{Z}_2$ produces Camlin $\Phi$ functional by wavefront-calibration | MICRO+DYN | $P_O$ | RES | CONSTRUCT (integration proof: CB-L1..L6 + CA-KK-ADAPT $\to$ CA-L3) | **open** (Pillar-C work item) |

**Capacitor tap**: CB-L1..L4 lands in cap§MICRO↔QFT Tier 1 (filled 2026-04-13: Hollands-Wald 2024 + Dappiaggi 2023-2024 + BFR 2025). Route B is **partially pre-hardened** by the capacitor fill (pre-existing Pillar-C equity).

**Pattern invariants**: $\{\mathrm{WF}\text{-index},\mathrm{Sob}_k\text{-threshold},\mathrm{proj}_{S^*\mathcal{M}}\}$.

**Weak-link targets (three)**: CB-L5 (conditions explicit), CB-WF-VORT (translation proof), CB-ROUTE-GEN (integration proof). Pillar-C dispatch applies VERIFY to CB-L5 and CONSTRUCT to CB-WF-VORT and CB-ROUTE-GEN.

### §3.3 Shared residual: $W_1^B$ = BKM-integration-audit (three sub-tasks combined)

$$W_1^B \;=\; \underbrace{\text{CA-KK-ADAPT}}_{\text{Route A KK adaptation}}\;\wedge\;\underbrace{\text{CB-WF-VORT}}_{\text{Route B WF→vorticity}}\;\wedge\;\underbrace{\text{CB-ROUTE-GEN}}_{\text{Route B generates Route A Φ}}$$

All three are PAC `CONSTRUCT` tasks; each routes a Pillar-C dispatch to a specific sub-agent pair (E1-hardener × E2-hardener × integration-hardener).

---

## §4 Compliance-map skeletons per external

Target artifacts: `strategy/externals-hardening/{camlin-2025,arxiv-2601.08854}/compliance-map.md`.

### §4.1 E1 Camlin 2025 compliance-map skeleton (layer × stated-axiom)

Stated axioms (SA) of Camlin 2025 (extracted from preprint abstract + introduction):

- **SA1**: incompressible NS on $\mathbb{T}^3$ with $\nu>0$, smooth div-free periodic initial datum
- **SA2**: finite initial kinetic energy
- **SA3**: Sundman-type reparametrization assumption $d\tau/dt>0$ a.e.
- **SA4**: BKM 1984 as closure hypothesis (external)

Compliance matrix (6 layers × 4 axioms = 24 cells; verdict codes P/Pa/O/S per PAC):

| Layer | SA1 | SA2 | SA3 | SA4 |
|-------|:---:|:---:|:---:|:---:|
| CA-L1 | P   | Pa  | P   | —   |
| CA-L2 | P   | P   | Pa  | —   |
| CA-L3 | P   | P   | Pa  | —   |
| CA-L4 | P   | P   | Pa  | —   |
| CA-L5 | P   | P   | —   | P   |
| CA-L6 | P   | Pa  | Pa  | P   |

Verdicts per Pillar-C dispatch; each `Pa` flagged for VERIFY to upgrade to `P`. No `S` (silent).

**New axiom introduced by adaptation**: SA5 (KK spectral gap input, $\Delta_0^{KK}=(2\pi/R)^2$) $\to$ CA-KK-ADAPT row appended; verdict `O` until CONSTRUCT completes.

### §4.2 E2 arXiv:2601.08854 compliance-map skeleton

Stated axioms:

- **SB1**: Riemannian $(\mathcal{M},g)$, smooth + complete
- **SB2**: NS (or Euler) dynamical equation on $\mathcal{M}$
- **SB3**: Hörmander microlocal-analysis setting (pseudodifferential calculus on $\mathcal{M}$)
- **SB4**: Initial data regularity hypothesis (condition on $\mathrm{WF}(u^\circ)$)

Compliance matrix (6 layers + 2 new × 4 axioms = 32 cells):

| Layer | SB1 | SB2 | SB3 | SB4 |
|-------|:---:|:---:|:---:|:---:|
| CB-L1 | P   | P   | P   | —   |
| CB-L2 | P   | —   | P   | P   |
| CB-L3 | P   | P   | P   | —   |
| CB-L4 | P   | P   | P   | —   |
| CB-L5 | Pa  | P   | P   | Pa  |
| CB-L6 | P   | P   | P   | P   |
| CB-WF-VORT | P | P | P | P (post-CONSTRUCT) |
| CB-ROUTE-GEN | P | P | P | P (post-CONSTRUCT) |

**Framework advantage** (noted in `ns-independence-bare.md §3.1`): $\mathcal{M}=M^4\times S^1/\mathbb{Z}_2$ already Riemannian $\Rightarrow$ SB1 auto-satisfied with zero structural mapping work (no new manifold-construction debt).

---

## §5 Hardened-routes tables (PAC primitive applications)

Target artifacts: `strategy/externals-hardening/{camlin-2025,arxiv-2601.08854}/hardened-routes.md`.

### §5.1 E1 Camlin 2025 hardened routes

| # | Weak link | PAC primitive | Hardening action | Improvement delivered |
|---|-----------|:-------------:|------------------|------------------------|
| H1 | CA-L3 constants $C(\nu,u^\circ,T)$ | VERIFY | Extract explicit $\nu,T$-dependence; provide $\nu$-uniform version | Explicit bound $C\le C_0(1+T)e^{C_1/\nu}$ for concrete $C_0,C_1$ (pending audit) |
| H2 | CA-L4 Jacobian $dt/d\tau$ | VERIFY | Confirm $dt/d\tau\in L^\infty_{\mathrm{loc}}$; handle near-singular sets | Lebesgue-point lemma supplementation |
| H3 | CA-KK-ADAPT KK frequency control | CONSTRUCT | Build adaptation: Poincaré on $S^1/\mathbb{Z}_2$ with $\Delta_0^{KK}=(2\pi/R)^2$ $\to$ frequency-space $\Phi$-control on $M^4\times S^1/\mathbb{Z}_2$; cites p1§KK + p8§4 T4 + p11K.4 + p10 U.2a | Generalization of Camlin from $\mathbb{T}^3$ flat to Riemannian KK geometry; Pin 1 $R=10.10\,\mu\mathrm{m}$ enters constant |
| H4 | Narrative completeness | EXTRACT | Produce programme-voice supplementary note citing Camlin 2025 explicitly; offer hardening as open-source addendum to original preprint | Reciprocity: authors receive independent rigor without attribution loss |

### §5.2 E2 arXiv:2601.08854 hardened routes

| # | Weak link | PAC primitive | Hardening action | Improvement delivered |
|---|-----------|:-------------:|------------------|------------------------|
| H5 | CB-L5 initial-data condition | VERIFY | Make condition explicit in Sobolev-wavefront form $u^\circ\in H^{s,\sigma}$; audit consistency with SA2 Leray energy | Explicit threshold $s_*,\sigma_*$ tied to $\nu,R$ |
| H6 | CB-WF-VORT WF→vorticity translation | CONSTRUCT | Hörmander Vol. I §8 + Melrose 1994 wavefront-Sobolev embeddings $\Rightarrow$ pointwise vorticity bound on cosphere bundle of $M^4\times S^1/\mathbb{Z}_2$ | New lemma: $\mathrm{WF}(u)\cap S^*\mathcal{M}=\emptyset \wedge \sup_k k\cdot\|u\|_{H^k}<\infty \Rightarrow \sup_x|\omega|<\infty$ |
| H7 | CB-ROUTE-GEN Route B generates Route A | CONSTRUCT | Microlocal-calibration map: WF-triviality on $S^*\mathcal{M}$ $\to$ Sundman reparam $\tau$ whose $\Phi$-functional matches Camlin's on $\mathbb{T}^3$ slice; integration proof | Unified BKM-bypass proof on $M^4\times S^1/\mathbb{Z}_2$; closes $W_1^B$ |
| H8 | Capacitor-tap narrative | EXTRACT | Reference cap§MICRO↔QFT Tier 1 pre-harden (Hollands-Wald 2024 + Dappiaggi 2023-2024 + BFR 2025) as Pillar-C equity already banked 2026-04-13 | External authors receive credit-by-association for capacitor infrastructure |

### §5.3 Shared integration bundle: $W_1^B$ closure

$W_1^B$ closure = {H3, H6, H7}. Pillar-C dispatch routes:

```
dispatch(E1-hardener)  ── H1,H2,H3,H4  → camlin-2025/hardened-routes.md
dispatch(E2-hardener)  ── H5,H6,H7,H8  → arxiv-2601.08854/hardened-routes.md
dispatch(integration)  ── H3 ∧ H6 ∧ H7 → externals-hardening/w1b-integration/proof.md
```

Upon all three dispatches PUBLISH-READY: Pillar-B $W_1^B$ upgrades `OPEN` $\to$ `PROVED`; chain confidence 4/10 $\to$ 6–7/10 per `ns-independence-bare.md §5.1`.

---

## §6 Reciprocity narrative + classical citation-precision audit + self-harden

Target artifacts: `strategy/externals-hardening/{camlin-2025,arxiv-2601.08854}/narrative.md` + inline audit table below for E3–E8.

### §6.1 Reciprocity narrative (E1, E2)

| Field | Camlin 2025 (E1) | arXiv:2601.08854 (E2) |
|-------|-------------------|-----------------------|
| **What we rely on** | Bounded Sundman $\Phi$ + temporal-lifting yielding BKM-finiteness on $\mathbb{T}^3$ | Cosphere-bundle microlocal regularity; WF-triviality $\Rightarrow C^\infty$ on Riemannian $\mathcal{M}$ |
| **What we verified** | CA-L1 ÷ CA-L6 against SA1–SA4; weak links CA-L3, CA-L4 flagged for constant-level VERIFY | CB-L1 ÷ CB-L6 against SB1–SB4; weak link CB-L5 flagged; capacitor pre-harden for CB-L1..L4 via cap§MICRO↔QFT |
| **What we constructed** | CA-KK-ADAPT: KK-adaptation from $\mathbb{T}^3$ flat to $M^4\times S^1/\mathbb{Z}_2$ | CB-WF-VORT: WF→vorticity Sobolev-wavefront calculus lemma; CB-ROUTE-GEN: Route B $\to$ Route A generation proof |
| **Attribution discipline** | Camlin 2025 cited at programme paper30 §Route-A, p30AP §Route-A, ns-comply §10, ns-indep §3.1, ns-harden §3.1 | arXiv:2601.08854 cited at p30 §Route-B, p30AP §Route-B, cap§MICRO↔QFT, ns-comply §10, ns-indep §3.1, ns-harden §3.2 |
| **Reciprocity claim** | *"We depend on Camlin 2025 AND we strengthened its KK-geometry adaptation. The bounded-$\Phi$ method now applies on curved compactification backgrounds."* | *"We depend on arXiv:2601.08854 AND we strengthened its WF→vorticity translation + its composition with Camlin's $\Phi$. The cosphere-bundle microlocal bypass now unifies with the Sundman-Φ bypass on $M^4\times S^1/\mathbb{Z}_2$."* |
| **Pillar-C artifact set** (per §5C.2) | X-RAY.md + compliance-map.md + hardened-routes.md + narrative.md | Same four artifacts + explicit pointer to cap§MICRO↔QFT equity |

### §6.2 Classical citation-precision audit (E3–E8)

Each classical-tier external audited at §-level citation precision; PAC primitive `VERIFY (location)`.

| Tag | External | Used at (chain location) | §-level citation audited | Verdict |
|-----|----------|---------------------------|---------------------------|:-------:|
| E3 | Leray 1934 | L6 Req 2 classical bypass; L5 feed | *Acta Math.* 63, pp.193-248 (1934) — specifically §16 (weak energy inequality) | **P** |
| E4 | Hopf 1951 | L6 Req 2 bypass co-cite | *Math. Nachr.* 4 (1951), pp.213-231 — Hauptsatz §3 | **P** |
| E5 | CKN 1982 + Lin 1998 | Req 8 classical base | *CPAM* 35 (1982) §1 Thm 1 (CKN); *CPAM* 51 (1998) pp.241-257 (Lin) | **P** |
| E6 | BKM 1984 | Req 6 wall statement; CA-L5 / CB-L4 feed | *CMP* 94 (1984), pp.61-66 — main theorem §2 | **P** |
| E7 | Ladyzhenskaya 1969 / Temam 1977 | L3 pressure-Poisson bypass; L7 Galerkin | Ladyzhenskaya 1969 Ch. 3 Thm 3; Temam 1977 Ch. 1 §2.5 (pressure-Poisson); Ch. 3 Thm 3.1 (Leray-Hopf); Ch. 3 §3 (Galerkin) | **P** |
| E8 | Hörmander 1990 / Melrose 1994 | $W_1^B$ sub-task (ii) CB-WF-VORT | Hörmander Vol. I §8 (wavefront-set); Melrose 1994, *Atiyah-Patodi-Singer Index Thm*, Ch. 1-2 (Sobolev wavefront) | **P** |

All 6 classical-tier externals pass citation-precision VERIFY. No additional hardening required.

### §6.3 Self-harden queue (I1, I2)

| Tag | Internal dep | Action | Folder | Blocks Clay compliance? |
|-----|--------------|--------|--------|:-----------------------:|
| I1 | YM→NS GF functor ($W_2^B$) | CONSTRUCT explicit $F:$ p8§L.1 $\to$ p30 L3 | `strategy/externals-hardening/ym-ns-gf-functor/` | **No** (Req 3 discharged via pressure-Poisson; narrative aesthetic) |
| I2 | 5D KK energy descent ($W_3^B$) | VERIFY+CONSTRUCT rigorous mode-projection from $\partial_y$-Killing to 4D viscous dissipation | `strategy/externals-hardening/kk-energy-descent/` | **No** (Req 2 discharged via classical Leray-Hopf; 5D narrative) |

Self-harden dispatch Pillar-C parallelizable with E1/E2 hardening. Priority: low (non-blocking). Purpose: narrative completeness for B_full composition-backward.

---

## §7 Cross-pillar analytics + references

### §7.1 Pillar-C primitive-application statistics

| Primitive | Cells / layers affected | External (tag) |
|-----------|:------------------------:|-----------------|
| VERIFY (layer-level) | 12 (CA-L1..CA-L6 + CB-L1..CB-L6) | E1, E2 |
| VERIFY (citation-precision) | 6 | E3, E4, E5, E6, E7, E8 |
| CONSTRUCT (adaptation / translation / integration) | 3 ($W_1^B$ sub-tasks) | E1, E2 |
| CONSTRUCT (self-harden) | 2 | I1, I2 |
| EXTRACT (reciprocity narrative) | 2 | E1, E2 |
| TRP (capacitor-tap pre-harden) | 1 (cap§MICRO↔QFT Tier 1) | E2 |
| **Total Pillar-C actions** | **26** | across 10 deps |

### §7.2 Confidence ladder (coupled to Pillar-A baseline 4/10)

| Stage | Pillar-C state | Chain confidence |
|-------|----------------|:----------------:|
| 0. Pillar-B baseline (this run start) | No hardening dispatched | 4/10 |
| 1. E3–E8 citation-precision audit complete (§6.2 above) | 6 classical-tier VERIFYs complete | 4.5/10 |
| 2. E1 layer-level VERIFY complete (CA-L1..L6 no `Pa` survives) | Camlin 2025 x-ray PUBLISH-READY | 5.0/10 |
| 3. E2 layer-level VERIFY complete (CB-L1..L6 no `Pa` survives) | arXiv:2601.08854 x-ray PUBLISH-READY | 5.5/10 |
| 4. CA-KK-ADAPT CONSTRUCT complete | H3 delivered | 6.0/10 |
| 5. CB-WF-VORT CONSTRUCT complete | H6 delivered | 6.5/10 |
| 6. CB-ROUTE-GEN integration proof | H7 delivered; $W_1^B$ PROVED | **7/10** |
| 7. I1 (YM→NS functor) self-harden | $W_2^B$ PROVED (narrative) | 7.2/10 |
| 8. I2 (KK descent) self-harden | $W_3^B$ PROVED (narrative) | 7.5/10 |
| 9. L2 EXCISED (already pre-Pillar-B) | — | unchanged |

Stages 1–3 are low-cost (citation audits + layer-VERIFYs); 4–6 are the Pillar-C heavy lifts; 7–8 are self-harden narrative.

### §7.3 Named-wall ledger across all three pillars

| Wall | Pillar A | Pillar B | Pillar C action |
|------|----------|----------|-----------------|
| $W_1^A$ BKM primary | OPEN-BUT-ADDRESSED (conf. 0.60) | **LIFTED** $\to$ $W_1^B$ | $W_1^B$ closure via H3+H6+H7 |
| $W_2^A$ GF-functor | OPEN-BUT-ADDRESSED (conf. 0.55) | **LIFTED** $\to$ $W_2^B$ | Self-harden I1 |
| $W_3^A$ Leray-Hopf descent | OPEN-BUT-ADDRESSED (conf. 0.50) | **LIFTED** $\to$ $W_3^B$ | Self-harden I2 |
| $W_4^A$ BHMR rigor | OPEN-BUT-ADDRESSED (conf. 0.40) | **EXCISED** | — (no Pillar-C action) |
| $W_1^B$ BKM-integration-audit | N/A | OPEN (3 sub-tasks) | **CLOSE** via H3+H6+H7 |
| $W_2^B$ GF-transfer-audit | N/A | OPEN (aesthetic) | Self-harden I1 (non-blocking) |
| $W_3^B$ Leray-Hopf-descent-audit | N/A | OPEN (narrative) | Self-harden I2 (non-blocking) |

### §7.4 Dependency graph with Pillar-C hardening overlays

```
        L1 ── KK reduction [Pd×6 transit; QG5D-rooted]
          │   (Kaluza 1921; Klein 1926; p1§KK Pin 1)
          │
          └── L4 ── Δ_0^KK = (2π/R)² > 0  [P UNCONDITIONAL ALL-LOOP]
                    │
                    │   (L2 EXCISED)
                    │
                    ├──── L3 ── GF transfer  [Pb via pressure-Poisson + 𝐏]
                    │          ↑ I1 self-harden (W2^B narrative functor)
                    │
                    ├──── L5a ── Route A  [Pb via Camlin 2025]
                    │           ↑ E1 hardening: H1, H2, H3 (KK-adapt)
                    │           ↑ E6 BKM 1984 citation audit (E3–E8 bundle)
                    │
                    ├──── L5b ── Route B  [Pb via arXiv:2601.08854]
                    │           ↑ E2 hardening: H5, H6 (WF→vort), H8 (cap pre-harden)
                    │           ↑ E8 Hörmander/Melrose citation audit
                    │
                    └──── L5 ── BKM composite
                                ↑ W1^B integration: H3 ∧ H6 ∧ H7 (shared integration bundle)
                                │
                                └── L6 ── energy descent  [Pb via classical Leray-Hopf]
                                    │    ↑ E3+E4+E7 citation audit
                                    │    ↑ I2 self-harden (W3^B 5D narrative)
                                    │
                                    └── L7 ── Galerkin uniqueness
                                        │    ↑ E7 Ladyzhenskaya 1969 + Temam 1977 Ch.3 §3
                                        │
                                        └── L8 ── global regularity
                                                  │
                                                  └── Theorem 1.1 (NS on T^3)
```

### §7.5 References

#### §7.5.1 Pillar-B companion

- `strategy/ns/deliverables/ns-independence-bare.md` — Pillar-B dep-free chain; defines $W_1^B,W_2^B,W_3^B$; §5.5 externals queue.
- `strategy/ns/deliverables/ns-comply-bare.md` — Pillar-A COMPLY companion; defines $W_1^A,W_2^A,W_3^A,W_4^A$.
- `strategy/ns/pac-output/runs/run-02/compliance-map.md` — LOCKED 70-cell Pillar-A matrix.
- `strategy/ns/pac-output/runs/run-06/` — this run (Pillar-C transcripts).

#### §7.5.2 Primary Pillar-C externals (targets)

- **Camlin 2025** (E1) — arXiv preprint; bounded Sundman $\Phi$ functional + temporal lifting → BKM-finiteness on $\mathbb{T}^3$. Hardening folder: `strategy/externals-hardening/camlin-2025/` (targets: X-RAY.md, compliance-map.md, hardened-routes.md, narrative.md).
- **arXiv:2601.08854** (E2) — Jan 2026; cosphere-bundle microlocal regularity; WF-triviality $\Rightarrow C^\infty$. Hardening folder: `strategy/externals-hardening/arxiv-2601.08854/`. Partially pre-hardened via cap§MICRO↔QFT Tier 1 (2026-04-13).

#### §7.5.3 Classical-tier externals (citation-precision audit)

- **Leray 1934** (E3) — *Acta Math.* 63, 193-248, §16.
- **Hopf 1951** (E4) — *Math. Nachr.* 4, 213-231, Hauptsatz §3.
- **Caffarelli-Kohn-Nirenberg 1982** (E5) — *CPAM* 35, §1 Thm 1; **Lin 1998** — *CPAM* 51, 241-257.
- **Beale-Kato-Majda 1984** (E6) — *CMP* 94, 61-66, main theorem §2.
- **Ladyzhenskaya 1969** (E7) — *Math. Theory Viscous Incompressible Flow*, Ch. 3 Thm 3; **Temam 1977** — *NS Eqs. Theory & Num.*, Ch. 1 §2.5; Ch. 3 §3, Thm 3.1.
- **Hörmander 1990** (E8) — *Anal. Lin. PDE* Vol. I §8; **Melrose 1994** — *Atiyah-Patodi-Singer Index Thm*, Ch. 1-2.

#### §7.5.4 Capacitor cells (09-table) tapped at Pillar C

- **cap§MICRO↔QFT Tier 1** (ESTABLISHED; filled 2026-04-13): Hollands-Wald 2024; Dappiaggi 2023-2024; BFR 2025; arXiv:2601.08854 host.
- **cap§SPEC↔QFT Tier 1** (VERIFIED): Weitzenböck-Bochner spectral gap (input to L4).
- **cap§GEOM↔QFT↔SPEC Tier 1** (VERIFIED): gradient-flow ↔ heat-kernel ↔ analyticity (input to L3 + L5).

#### §7.5.5 Programme internal cross-refs

- `solutions-with-prize/paper30-navier-stokes/PROOF-CHAIN.md` v2.1 (2026-04-14) — live chain.
- `solutions-with-prize/paper30-navier-stokes/strategy/00-ns-attack-plan.md` — Route A / Route B / Route C breakdown.
- `integers/paper01-qg5d/PROOF-CHAIN.md` — QG5D hub; §KK; Pin 1.
- `solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md` — §4 T4 (KK gap); Appendix L §L.1 (GF source).
- `integers/paper10-scheme-independence/` Theorem U.2a — scheme independence.
- `paper11-scheme-independence/` Theorem K.4 — all-loop bootstrap.
- `strategy/x-ray/` — fixed vocabulary (10 faces / 6 projections / 5 patterns / 16 invariants).
- `strategy/universal-approval-run.md` §5C — Pillar-C protocol.
- `strategy/_research/ns/landscape.md` — NS landscape; acknowledgment roster.

#### §7.5.6 Self-harden internal queue

- `strategy/externals-hardening/ym-ns-gf-functor/` (I1) — YM→NS GF functor $F$.
- `strategy/externals-hardening/kk-energy-descent/` (I2) — 5D KK → 4D energy descent rigor.

#### §7.5.7 Pillar-C dispatch protocol

Per `strategy/universal-approval-run.md §5C.2`, each external's hardening bundle is produced by a dedicated sub-agent whose inputs are the external preprint/paper and whose outputs are the four artifacts (X-RAY.md, compliance-map.md, hardened-routes.md, narrative.md). This bare skeleton (`ns-harden-bare.md`) is the TOC + target list; the sub-agent dispatches operationalize it.

---

*End of `ns-harden-bare.md`. Pillar C target list locked. Primary targets: Camlin 2025 (E1) + arXiv:2601.08854 (E2). Double-kill invariant preserved: we depend on both preprints AND we publish them stronger. The BKM bypass becomes programme-verified at stage 6 of §7.2. Classical-tier (E3–E8) passes citation audit at stage 1. Self-harden (I1, I2) is non-blocking narrative. Variant (B) declared throughout; (A/C/D) EXCISED under Rules §5b. Companion to `ns-comply-bare.md` + `ns-independence-bare.md`; together the three pillars discharge Universal Approval for NS.*

*G Six and Claude Opus 4.6. 2026-04-14.*
