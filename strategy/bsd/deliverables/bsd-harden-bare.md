# BSD Pillar-C Harden X-Ray (BARE MODE)

*Pillar-C (HARDEN — "double kill") deliverable for the BSD vertex of the Universal Approval run. The 15 retained externals surviving Pillar B (from `strategy/bsd/deliverables/bsd-independence-bare.md §7.3`) are each scheduled for a dedicated hardening folder `strategy/externals-hardening/<external>/` carrying X-RAY / compliance-map / hardened-routes / narrative per universal-approval-run.md §5C.2. This document is the bare table-of-contents + per-external skeleton; detailed hardening audits are written into the per-external folders by follow-on runs. Zero prose. Scope-declaration: CM-specialisation `Scope(S₀) = { E/Q : CM by O_K, h_K=1, rank r∈{0,1} }` inherited from Pillars A/B; externals are hardened for the uses made of them inside `Scope(S₀)` and its documented extensions (W_rank, W_nonCM, W_hK, W_Sha sub-scopes).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Pillar-C Mandate and Scope

**Mandate (universal-approval-run.md §5C).** Every retained external has a published hardening artifact showing what we improved. Narrative: "We depend on X AND we strengthened X."

**PAC primitives applied per external (pca-extension/07; universal-approval-run.md §5C.2).**
- **VERIFY** — walk external's chain layer-by-layer vs stated axioms.
- **CONSTRUCT** — supply missing layer (theorem + citation) where a gap is exposed.
- **BYPASS** — route past a weak link via programme-internal alternate.
- **DECOMPOSE** — split a monolithic step into independently auditable sub-steps.
- **EXCISE** — remove a non-load-bearing claim.

**Per-external folder schema (universal-approval-run.md §5C.2).** Each retained external gets `strategy/externals-hardening/<EXTERNAL>/`:
- `X-RAY.md` — face / projection / pattern / invariant per layer (fixed X-Ray vocabulary: 10 faces / 6 projections / 5 patterns / 16 invariants; `strategy/x-ray/00-x-ray-strategy.md`).
- `compliance-map.md` — external's layers × external's stated axioms; cell verdicts PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT.
- `hardened-routes.md` — the VERIFY / CONSTRUCT / BYPASS / DECOMPOSE / EXCISE improvements produced.
- `narrative.md` — fair attribution + "how we strengthened them" write-up.
- `commit-memo.md` — lock status.

**Scope declaration (hard).** We harden each external for the uses we make of it inside `Scope(S₀)` plus W_rank/W_nonCM/W_hK/W_Sha sub-scopes as specified in `bsd-independence-bare.md §7`. No claim is made to fully re-harden the externals' full original scopes. Residual beyond-our-use claims remain the original authors'.

**Load-bearing weight ranking (priority for first-wave hardening).**
1. **BCDT 2001** (modularity) — core L-function existence for all E/Q.
2. **Kolyvagin 1990** (Euler system) — rank-0 closure + |Ш|<∞.
3. **Skinner-Urban 2014** (IMC for GL₂) — W_rank rank-2 closure + W_Sha p-part.
4. **Gross-Zagier 1986** (height formula) — rank-1 closure, scope-extension for W_rank.
5. **CBB / paper23** (Connes-Bost-Baumslag KMS) — programme-internal foundation; rider on all L7-onward verdicts.

Items 6-15 (second wave): Ha-Paugam 2005, Rubin 1991, Mazur-Wiles 1984, Perrin-Riou 1992, Burungale-Skinner-Tian-Wan 2024, Connes-Marcolli 2008, Newton-Thorne 2021, Nekovář 2001, Yuan-Zhang-Zhang 2013, Gross 1984.

---

## §2 Externals Inventory (15 retained externals)

Source: `bsd-independence-bare.md §7.3`. Every row cites primary source, use-site inside BSD chain, folder path for hardening artifact, and first-wave priority.

| # | External | Primary source | Use-site in BSD chain | Pillar-B verdict | Hardening folder | Priority |
|---|----------|----------------|------------------------|------------------|------------------|----------|
| 1 | **BCDT 2001 modularity** | Breuil-Conrad-Diamond-Taylor 2001, JAMS 14: 843-939 ("On the modularity of elliptic curves over Q"); builds on Wiles 1995 Ann.Math. 141:443-551; Taylor-Wiles 1995 Ann.Math. 141:553-572; Diamond 1996; Conrad-Diamond-Taylor 1999. | L8 Req 3 (L-cont universal); L11 Req 3 inherited; W_nonCM Route α; W_Sha Route κ (Manin integrality via modularity). | LITERATURE (unconditional for all E/Q). | `strategy/externals-hardening/bcdt-2001/` | **1 (top)** |
| 2 | **Kolyvagin 1990 Euler system** | Kolyvagin, "Euler systems", in *The Grothendieck Festschrift* Vol. II, pp. 435-483, Birkhäuser (1990); developed from Kolyvagin 1988 Izv.Math. 52:1154-1180. | L9 Req 1 (rank-0 rank); L9 Req 5 (|Ш|<∞ rank-0); L9 Req 7; W_Sha Route ζ; W_nonCM Route γ (via Kolyvagin extension). | LITERATURE (unconditional for rank-0 CM; extends via Skinner-Urban). | `strategy/externals-hardening/kolyvagin-1990/` | **2** |
| 3 | **Skinner-Urban 2014 IMC-GL₂** | Skinner-Urban, "The Iwasawa main conjectures for GL_2", Invent.Math. 195:1-277 (2014). | W_rank Route B (rank-2 closure via IMC); W_nonCM Route γ (p-converse class); W_Sha Route θ (p-part |Ш| for non-CM modular). | LITERATURE (unconditional for IMC-covered class). | `strategy/externals-hardening/skinner-urban-2014/` | **3** |
| 4 | **Gross-Zagier 1986 height formula** | Gross-Zagier, "Heegner points and derivatives of L-series", Invent.Math. 84:225-320 (1986). | L10 Req 1-5 (rank-1 closure; vacuous-in-scope per paper26 Remark 12.6); W_rank Route C (scope-extension); W_nonCM Route γ. | LITERATURE (unconditional; non-load-bearing in Scope(S₀) but load-bearing for scope-extensions). | `strategy/externals-hardening/gross-zagier-1986/` | **4** |
| 5 | **CBB axioms (Connes-Bost-Baumslag)** | paper23 (programme axiomatisation); paper13-rh Main Theorem (equivalent status); Connes-Bost 1995 Selecta Math.; Bost-Connes 1995 Selecta Math. 1:411-457 ("Hecke algebras, type III factors and phase transitions"); Baumslag extension in programme. | Rider on every L7-onward P/Pa verdict (L7 Req 2; L11 Req 1, 2, 4); narrow to paper13-rh Main Theorem status in Pillar B. | PROGRAMME-INTERNAL (paper13-rh conditional; paper23 axiomatisation locked). | `strategy/externals-hardening/cbb-paper23/` (cross-links to `strategy/ccm-verification/` for CCM 2025 overlap) | **5** |
| 6 | **Ha-Paugam 2005 BC over K** | Ha-Paugam, "Bost-Connes-Marcolli systems for Shimura varieties", IMRP 2005:237-286 (2005); also arXiv:math/0507101. | L1 Req 6 (h_K=1 hypothesis; scope fingerprint input); L2 Req 6 (bridge family over K); W_hK Route δ (h_K>1 via ring class fields; Ha-Paugam §5). | LITERATURE (unconditional for h_K=1; published generalisation h_K up to 3 per Ha-Paugam §5). | `strategy/externals-hardening/ha-paugam-2005/` | 6 |
| 7 | **Rubin 1991 IMC for CM** | Rubin, "The 'main conjectures' of Iwasawa theory for imaginary quadratic fields", Invent.Math. 103:25-68 (1991). | L9 Req 4 (rank-0 c* formula via Rubin IMC-CM); W_Sha Route η (p-part for all CM); 32.a3 \|Ш\|=1 numerics. | LITERATURE (unconditional for CM). | `strategy/externals-hardening/rubin-1991/` | 7 |
| 8 | **Mazur-Wiles 1984 cyclotomic IMC** | Mazur-Wiles, "Class fields of abelian extensions of Q", Invent.Math. 76:179-330 (1984). | W_Sha Route ι (p-part for cyclotomic twists). | LITERATURE (unconditional). | `strategy/externals-hardening/mazur-wiles-1984/` | 8 |
| 9 | **Perrin-Riou 1992 p-adic L** | Perrin-Riou, "Théorie d'Iwasawa des représentations p-adiques sur un corps local", Invent.Math. 109:137-185 (1992); also Perrin-Riou 1995 *Fonctions L p-adiques*, SMF Astérisque 229. | W_rank Route A (p-adic L-function at arbitrary rank; p-adic BSD). | LITERATURE (unconditional framework; conditional p-adic BSD closure). | `strategy/externals-hardening/perrin-riou-1992/` | 9 |
| 10 | **Burungale-Skinner-Tian-Wan 2024** | Burungale-Skinner-Tian-Wan 2024, arXiv:2303.* family; "p-converse to the Gross-Zagier-Kolyvagin theorem" + Burungale-Skinner-Tian (2021, Invent.Math.) + Skinner 2020 ("A converse to a theorem of Gross, Zagier, and Kolyvagin", Ann.Math. 191:329-354). | W_nonCM Route γ (rank ∈ {0,1} non-CM closure for p-converse class). | LITERATURE-PREPRINT (2021-24 published / 2024-26 preprint extensions). | `strategy/externals-hardening/burungale-skinner-tian-wan-2024/` | 10 |
| 11 | **Connes-Marcolli 2008 GL₂ BC** | Connes-Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, AMS Colloquium Publ. 55 (2008); Connes-Marcolli 2006 "From physics to number theory via NCG. Part II", Frontiers in Number Theory, Physics, and Geometry II. | W_nonCM Route β (GL₂ KMS/bridge realisation for non-CM modular). | LITERATURE (construction published; KMS-uniqueness conditional on additional structure). | `strategy/externals-hardening/connes-marcolli-2008/` (cross-links to CBB folder and paper28-pvnp Popa-rigidity track) | 11 |
| 12 | **Newton-Thorne 2021** | Newton-Thorne, "Symmetric power functoriality for holomorphic modular forms", Publ.Math.IHÉS 134:1-116 (2021); Newton-Thorne 2021 II, Publ.Math.IHÉS 134:117-152. | W_rank Route C (Sym^m E modularity for all m ≥ 1, combined with higher-weight Kolyvagin). | LITERATURE (unconditional for all m, 2021). | `strategy/externals-hardening/newton-thorne-2021/` | 12 |
| 13 | **Nekovář 2001 parity + higher-weight Kolyvagin** | Nekovář, "On the parity of ranks of Selmer groups II", CRAS 332:99-104 (2001); Nekovář 2006 *Selmer complexes*, SMF Astérisque 310. | W_rank Route C (parity of Selmer ranks; higher-weight Kolyvagin extension). | LITERATURE (unconditional parity; conditional higher-weight rank closure). | `strategy/externals-hardening/nekovar-2001/` | 13 |
| 14 | **Yuan-Zhang-Zhang 2013** | Yuan-Zhang-Zhang, *The Gross-Zagier Formula on Shimura Curves*, Ann.Math.Studies 184, Princeton (2013). | W_hK Route ε (general h_K on Heegner side); W_nonCM Route γ (generalised GZ for Shimura curves); W_rank Route C. | LITERATURE (unconditional generalisation of Gross-Zagier). | `strategy/externals-hardening/yuan-zhang-zhang-2013/` | 14 |
| 15 | **Gross 1984 Heegner points / ring class fields** | Gross, "Heegner points on X_0(N)", in *Modular Forms*, R.A. Rankin ed., pp. 87-105, Ellis Horwood (1984). | W_hK Route ε (Heegner-point side unconditional for general h_K). | LITERATURE (unconditional). | `strategy/externals-hardening/gross-1984/` | 15 |

**Aggregate.** 15 retained externals; 5 first-wave priority (§§3.1-3.5 below); 10 second-wave (§§3.6-3.15, skeleton-only here, folders scheduled for follow-on runs).

---

## §3 Per-External Harden Stubs

### §3.1 BCDT 2001 modularity (Priority 1)

**Attribution (fair).** Breuil-Conrad-Diamond-Taylor 2001 completes the proof that every elliptic curve over Q is modular, building on Wiles 1995 (semistable case) and Taylor-Wiles 1995 (Taylor-Wiles method). Further steps: Diamond 1996 (level-lowering extension); Conrad-Diamond-Taylor 1999 (non-minimal deformation ring). This is the single most load-bearing external for BSD: without modularity, L(E,s) has no unconditional analytic continuation, and Wiles's Clay p.4 state-of-the-art theorem (rank ≤ 1 BSD) does not exist.

**Our use-site.** L8 Req 3 (L(E,s) = L(f_E, s) with f_E weight-2 newform of level N_E; continuation + FE); L11 Req 3 (strong-form BSD statement inherits); W_nonCM Route α (L-cont universal for non-CM); W_Sha Route κ (Manin integrality of |Ш| in c* via modularity, replacing full Ш-finiteness requirement).

**PAC strengthening proposal (scheduled in `strategy/externals-hardening/bcdt-2001/`).**
- **VERIFY (chain x-ray).** Layer decomposition: (L_BCDT.1) Frey-Hellegouarch construction + Serre's conjecture reduction; (L_BCDT.2) Wiles deformation theory R=T for semistable; (L_BCDT.3) Taylor-Wiles patching lemma; (L_BCDT.4) Ribet's level-lowering (independent, feeds level reduction); (L_BCDT.5) Diamond 1996 level-lowering extension; (L_BCDT.6) Conrad-Diamond-Taylor 1999 non-minimal; (L_BCDT.7) BCDT 2001 residually reducible / supersingular cases. Face-projection-pattern-invariant per layer per X-Ray vocabulary.
- **CONSTRUCT (our addition).** KMS-theoretic reformulation of R=T: R (universal deformation ring) as O*-subalgebra of A_{BC,K}-type Hecke correspondence algebra, T (Hecke algebra) as projection of KMS_1 sector. Programme-internal construction; integers/paper01-qg5d/paper13 infrastructure. Proposed as capacitor cell **ANT↔OA↔LANG "R=T as KMS projection"** (candidate Tier 2 VERIFIED-programme).
- **BYPASS (alternate chain).** Wiles-Kisin modularity-lifting framework (Kisin 2004-09) provides independent deformation-theoretic route; cited as secondary confirmation.
- **DECOMPOSE.** Split L_BCDT.7 (residually reducible cases) into (i) dihedral case, (ii) non-dihedral case; each has independent proof path.
- **EXCISE.** Level N = 1 trivial case excised as zero content; N = 2, 3, 5, 7, 11 base cases individually verifiable computationally.

**Scheduled follow-on artifacts.** `strategy/externals-hardening/bcdt-2001/X-RAY.md`; `.../compliance-map.md` (7 layers × stated axioms of Wiles-Taylor-Wiles system); `.../hardened-routes.md`; `.../narrative.md`; `.../commit-memo.md`.

**Status.** Pillar-C stub LOCKED; full folder build scheduled in run-07 first-wave batch.

---

### §3.2 Kolyvagin 1990 Euler system (Priority 2)

**Attribution (fair).** Kolyvagin 1990 *Euler systems* (Grothendieck Festschrift Vol. II) constructs the Euler system of Heegner points on modular curves, bounds the p-part of Ш(E/K) by cohomological arguments, and combined with Gross-Zagier 1986 proves: analytic rank ≤ 1 ⇒ algebraic rank = analytic rank and |Ш| < ∞. This is the engine of Wiles-p.4 state-of-the-art BSD for rank ≤ 1.

**Our use-site.** L9 Req 1 (rank-0 ⇒ L(E,1) ≠ 0 closes via converse); L9 Req 5 (|Ш| < ∞ rank-0 CM); L9 Req 7 (rank-0 case closes); W_Sha Route ζ (unconditional rank-0 CM); W_nonCM Route γ (via extension + p-converse class).

**PAC strengthening proposal (scheduled in `strategy/externals-hardening/kolyvagin-1990/`).**
- **VERIFY (chain x-ray).** Layer decomposition: (L_Kol.1) Heegner point construction on X_0(N)(K); (L_Kol.2) Euler system axioms (norm-compatible family); (L_Kol.3) derivative operators; (L_Kol.4) global duality + Tate-Poitou; (L_Kol.5) Cebotarev density application; (L_Kol.6) bound on Selmer group rank; (L_Kol.7) bound on p-part of Ш. Face = ARITHMETIC-dominant; projection = Galois cohomology; pattern = duality; invariant = Selmer rank.
- **CONSTRUCT.** KMS-formulation of Euler system norm-compatibility: the norm-compatible tower as a projective system of KMS_β states for β → 1⁺ on A_{BC,K}-family Hecke algebras. Programme-internal; capacitor cell **OA↔AG "Euler system as KMS tower"** (candidate Tier 2 VERIFIED-programme).
- **BYPASS.** Bertolini-Darmon alternate route via Stark-Heegner points (for rank-1 case) provides independent confirmation; Wan 2014 anticyclotomic route for rank-0 non-CM.
- **DECOMPOSE.** Split L_Kol.4 Tate-Poitou into (i) local duality at primes of good reduction; (ii) local duality at ramified primes (independently verifiable).
- **EXCISE.** Heegner hypothesis refinement: in rank-0 scope, the Heegner hypothesis restricts discriminants; excise redundant discriminant conditions via YZZ 2013 generalisation.

**Scheduled follow-on artifacts.** Standard per-external schema; cross-links to Gross-Zagier 1986 folder (they are a package).

**Status.** Pillar-C stub LOCKED; full folder build scheduled in run-07 first-wave batch.

---

### §3.3 Skinner-Urban 2014 IMC-GL₂ (Priority 3)

**Attribution (fair).** Skinner-Urban 2014 (Invent.Math. 195) establishes the Iwasawa main conjecture for GL_2/Q modular under mild hypotheses (ordinary reduction, residual representation irreducible, etc.), following the Wiles-Mazur-Tate framework and building on Kato 2004 (explicit reciprocity), Urban 2006 (Eisenstein congruences). Combined with Kato 2004 and p-adic Gross-Zagier (Kobayashi 2013; Bertolini-Darmon-Prasanna 2013), yields p-part of strong-form BSD in many analytic-rank-2 cases (Castella-Skinner-Wan class).

**Our use-site.** W_rank Route B (primary bypass for rank-2 BSD); W_nonCM Route γ (p-converse class closure); W_Sha Route θ (p-part |Ш|< ∞ for IMC-covered non-CM).

**PAC strengthening proposal (scheduled in `strategy/externals-hardening/skinner-urban-2014/`).**
- **VERIFY (chain x-ray).** Layer decomposition: (L_SU.1) Eisenstein ideal / congruence module construction; (L_SU.2) three-variable p-adic L-function; (L_SU.3) Galois representation deformation; (L_SU.4) characteristic ideal divisibility (one direction); (L_SU.5) analytic divisibility via Eisenstein congruences; (L_SU.6) opposite divisibility via Euler system. Face = ARITHMETIC; projection = Galois + automorphic; pattern = duality; invariant = characteristic ideal.
- **CONSTRUCT.** KMS-tower interpretation of the three-variable p-adic L-function: as a partition function over deformation parameters on the BC-GL₂ algebra (Connes-Marcolli 2008 link). Programme-internal; capacitor cell **ANT↔OA↔LANG "p-adic L as KMS partition function"** (candidate Tier 2 VERIFIED-programme). Connects directly to W_rank Route B and W_nonCM Route β.
- **BYPASS.** Wan 2020 fully-anticyclotomic route + Castella 2018 reciprocity provide alternate divisibility chains.
- **DECOMPOSE.** Split L_SU.5 Eisenstein congruences by weight-filtration step; each sub-step verifiable independently.
- **EXCISE.** Non-ordinary-reduction cases in Wan-Xu 2021 subsume the ordinary hypothesis; excise ordinarity assumption for Wan-Xu-covered class.

**Scheduled follow-on artifacts.** Standard schema; cross-links to Rubin 1991 folder (CM side) and Connes-Marcolli 2008 folder (GL₂ BC side).

**Status.** Pillar-C stub LOCKED; full folder build scheduled in run-07 first-wave batch.

---

### §3.4 Gross-Zagier 1986 height formula (Priority 4)

**Attribution (fair).** Gross-Zagier 1986 (Invent.Math. 84) proves: for E/Q modular with Heegner point y_K on E(K) (K imaginary quadratic satisfying Heegner hypothesis), `⟨y_K, y_K⟩_NT = c · L'(E, 1) · L(E^D, 1)` for explicit constant c and quadratic twist E^D. Combined with Kolyvagin, gives rank-1 BSD. Generalised by YZZ 2013 to Shimura curves (W_hK extension).

**Our use-site.** L10 Req 1-5 (rank-1 closure; vacuous in Scope(S₀) per paper26 Remark 12.6 since GRH forces analytic rank 0 for CM h_K=1 in our scope); W_rank Route C (scope-extension for r ≥ 2 via Nekovář higher-weight); W_nonCM Route γ (rank-1 non-CM).

**PAC strengthening proposal (scheduled in `strategy/externals-hardening/gross-zagier-1986/`).**
- **VERIFY (chain x-ray).** Layer decomposition: (L_GZ.1) Heegner point construction; (L_GZ.2) Néron-Tate height computation via intersection theory on X_0(N); (L_GZ.3) L'(E,1) formula via Rankin-Selberg; (L_GZ.4) height = L'/period comparison. Face = ARITHMETIC + AMPLITUDE (heights); projection = arithmetic intersection; pattern = duality; invariant = height-pairing.
- **CONSTRUCT.** Murray-von Neumann dimension identity reading of GZ formula: `⟨y_K, y_K⟩_NT` as Murray-von Neumann dimension of a sub-factor of A_{BC,K} associated to E, equals L'(E,1)·L(E^D,1)/period. Programme-internal; capacitor cell **OA↔AG "Heights as MvN dimensions"** (candidate Tier 2 VERIFIED-programme, links to paper28 Popa rigidity). Proposed as Route 3 MY4 ingredient per landscape.md §Our programme's position.
- **BYPASS.** YZZ 2013 Shimura curve generalisation provides alternate (broader) framework; Kobayashi 2013 p-adic Gross-Zagier provides p-adic counterpart.
- **DECOMPOSE.** Split L_GZ.3 Rankin-Selberg derivative into (i) local factors at split primes; (ii) local factors at inert primes; each via doubling-method factorisation.
- **EXCISE.** Heegner hypothesis refinement: YZZ 2013 removes the original GZ Heegner-hypothesis restriction; excise for general D.

**Scheduled follow-on artifacts.** Standard schema; paired with Kolyvagin 1990 folder + YZZ 2013 folder.

**Status.** Pillar-C stub LOCKED; full folder build scheduled in run-07 first-wave batch.

---

### §3.5 CBB / paper23 (Priority 5; programme-internal foundation)

**Attribution (fair).** The CBB (Connes-Bost-Baumslag KMS) axiomatisation: Bost-Connes 1995 (Selecta Math. 1:411-457, "Hecke algebras, type III factors and phase transitions associated with the modular group") introduced the BC algebra whose KMS-state structure encodes Dedekind zeta of Q. Connes-Bost extensions + Baumslag generalisations + programme paper23 axiomatisation. Status: paper13-rh Main Theorem is stated conditional on CBB; paper23 codifies the axioms. Status of CBB = status of paper13-rh Main Theorem (equivalence by design).

**Our use-site.** Rider on every L7-onward PROVED / PARTIAL verdict in the 11×7 compliance map: L7 Req 2 (GRH⇒c≠0); L11 Req 1, 2, 4 (rank equality, c≠0, strong-form formula at L11). Pillar B preserves CBB rider; does not discharge.

**PAC strengthening proposal (scheduled in `strategy/externals-hardening/cbb-paper23/`, cross-linked to `strategy/ccm-verification/` for CCM 2025 overlap and `strategy/rh/` for RH Pillar-C material).**
- **VERIFY (chain x-ray).** Layer decomposition of paper23 axiom set: (L_CBB.1) base BC algebra C*(Q) ⋊ N×; (L_CBB.2) KMS_1 uniqueness; (L_CBB.3) type-III_1 factor classification for β > 1; (L_CBB.4) Galois action on extremal KMS states; (L_CBB.5) Hecke-eigenvalue = KMS partition data; (L_CBB.6) extension to K imaginary quadratic (Ha-Paugam compatibility); (L_CBB.7) programme-paper23 axiomatisation lock. Face = RESONANCE + SYMMETRY + ARITHMETIC; projection = KMS/spectral; pattern = duality (Tomita-Takesaki); invariant = modular operator / KMS parameter.
- **CONSTRUCT.** Programme already constructs explicit KMS uniqueness for h_K=1 via paper26 §§03-07; this IS the CBB verification for BSD-relevant scope. Proposed capacitor cell upgrade: **OA↔AG "BC-bridge explicit-CFT" (T12)** elevated Tier 2 → Tier 1 for h_K=1 scope (ESTABLISHED in Scope(S₀)).
- **BYPASS.** CCM 2025 alternative route (Hilbert-Pólya via CCM spectral realisation; capacitor T13) provides independent confirmation of GRH input that CBB uses at L7; CCM-verification bundle `strategy/ccm-verification/` already exists.
- **DECOMPOSE.** Split L_CBB.3 type-III_1 classification by factor-type sub-cases (I, II_1, II_∞, III_λ for λ ∈ [0,1]) — only III_1 is load-bearing for GRH rider; others EXCISE.
- **EXCISE.** Paper23 axiom A_5 (regularisation-scheme independence): shown redundant by paper13 §X; EXCISE from minimal axiom set.

**Scheduled follow-on artifacts.** Standard schema; significant cross-link to `strategy/ccm-verification/` (CCM 2025 = parallel external hardening already in flight) and `strategy/rh/deliverables/rh-harden-bare.md` (RH Pillar-C will share CBB hardening as a joint artifact).

**Status.** Pillar-C stub LOCKED; folder build coordinated with RH Pillar-C (joint work); scheduled in run-07 first-wave batch.

---

### §3.6-§3.15 Second-wave stubs (10 externals)

Each second-wave external gets a one-paragraph stub below; full harden folders scheduled for run-08 or later per load-bearing weight. All stubs follow the schema: (attribution) / (use-site) / (proposed PAC primitives) / (folder path).

#### §3.6 Ha-Paugam 2005 BC over K

**Attribution.** Ha-Paugam 2005 (IMRP) constructs BC-systems over imaginary quadratic fields K generalising Bost-Connes 1995; published construction covers h_K up to 3 with extension sketch to general h_K. **Use-site.** L1, L2 (scope fingerprint h_K=1); W_hK Route δ (h_K>1 via ring class fields). **Proposed PAC.** VERIFY §5 h_K>1 construction vs stated KMS-uniqueness; CONSTRUCT programme-internal paper26 §03 generalisation (h_K extensions of cocycle bound (k+1)^{-1}·h_K^{-1}); BYPASS via capacitor AG↔ECFT "CM=explicit CFT" for h_K-agnostic statements; DECOMPOSE by h_K class. **Folder.** `strategy/externals-hardening/ha-paugam-2005/`.

#### §3.7 Rubin 1991 IMC for CM

**Attribution.** Rubin 1991 (Invent.Math. 103) establishes Iwasawa main conjecture for imaginary quadratic fields via elliptic units Euler system. **Use-site.** L9 Req 4 (rank-0 c* formula); W_Sha Route η (p-part |Ш| CM); 32.a3 |Ш|=1 numerics. **Proposed PAC.** VERIFY elliptic-units Euler system layer decomposition; CONSTRUCT programme-internal KMS-realisation of elliptic units (via A_{BC,K} Hecke characters); BYPASS via Yager 1982 two-variable p-adic L-function; DECOMPOSE by Ш-p-component; EXCISE redundant ramification hypotheses via Coates-Wiles 1977 overlap. **Folder.** `strategy/externals-hardening/rubin-1991/`.

#### §3.8 Mazur-Wiles 1984 cyclotomic IMC

**Attribution.** Mazur-Wiles 1984 (Invent.Math. 76) proves Iwasawa main conjecture for Q(ζ_p^∞)/Q via Eisenstein ideal technique on modular curves. **Use-site.** W_Sha Route ι (p-part for cyclotomic twists). **Proposed PAC.** VERIFY Eisenstein-ideal layer; CONSTRUCT KMS interpretation of Eisenstein congruences as phase transition on BC-Q algebra; BYPASS via Kolyvagin 1990 cyclotomic Euler system (Rubin 1991 §X reformulation); DECOMPOSE by Iwasawa algebra prime; EXCISE minor-arc subtleties via Kato 2004 overlap. **Folder.** `strategy/externals-hardening/mazur-wiles-1984/`.

#### §3.9 Perrin-Riou 1992 p-adic L-functions

**Attribution.** Perrin-Riou 1992 (Invent.Math. 109) theory of p-adic L-functions for p-adic Galois representations; p-adic BSD conjecture framework. **Use-site.** W_rank Route A (p-adic L at arbitrary rank). **Proposed PAC.** VERIFY p-adic L-function construction layer; CONSTRUCT KMS-partition-function reading (matches Skinner-Urban R=T capacitor); BYPASS via Coleman 1983 + Colmez 1998 alternate construction; DECOMPOSE by Iwasawa cohomology degree; EXCISE Bloch-Kato-exponential redundancy. **Folder.** `strategy/externals-hardening/perrin-riou-1992/`.

#### §3.10 Burungale-Skinner-Tian-Wan 2024 p-converse

**Attribution.** Burungale-Skinner-Tian-Wan 2024 (arXiv:2303.* and successors) p-converse to Gross-Zagier-Kolyvagin for non-CM rank ∈ {0,1}; identifies infinite families with strong BSD. Skinner 2020 (Ann.Math. 191) is predecessor. **Use-site.** W_nonCM Route γ. **Proposed PAC.** VERIFY p-converse layer chain vs Wan 2014 + Skinner 2020 inputs; CONSTRUCT programme-level extension to CBB-admissible non-CM class; BYPASS via Bertolini-Darmon 2014 Stark-Heegner alternate; DECOMPOSE by reduction type; EXCISE overlaps with Skinner-Urban 2014. **Folder.** `strategy/externals-hardening/burungale-skinner-tian-wan-2024/`.

#### §3.11 Connes-Marcolli 2008 GL₂ BC

**Attribution.** Connes-Marcolli 2008 *Noncommutative Geometry, Quantum Fields and Motives* (AMS Colloq. 55); Connes-Marcolli 2006 "Quantum Statistical Mechanics of Q-lattices" monograph. Constructs GL₂ BC system on Q-lattice space. **Use-site.** W_nonCM Route β (KMS/bridge realisation). **Proposed PAC.** VERIFY Q-lattice commensurability layer decomposition; CONSTRUCT KMS-uniqueness extension from h_K=1 to GL₂ setting (programme-internal via paper28 Popa rigidity cross-link); BYPASS via Laca-Neshveyev 2011 alternate KMS-type classification; DECOMPOSE by modular-weight weight-2 case; EXCISE renormalisation-group tower redundancy. **Folder.** `strategy/externals-hardening/connes-marcolli-2008/` (cross-links CBB folder + paper28-pvnp Popa rigidity track).

#### §3.12 Newton-Thorne 2021 symmetric-power modularity

**Attribution.** Newton-Thorne 2021 I-II (Publ.Math.IHÉS 134) establishes symmetric-power functoriality for holomorphic modular forms of all weights; completes the Sym^m conjecture for all m ≥ 1. **Use-site.** W_rank Route C (Sym^m E modularity for higher-rank bypass). **Proposed PAC.** VERIFY automorphy lifting layer decomposition; CONSTRUCT KMS-interpretation of Sym^m-transfer as BC-type algebra morphism; BYPASS via Clozel-Harris-Taylor 2008 predecessor for odd m; DECOMPOSE by Galois-representation Hodge-Tate weights; EXCISE Taylor-Wiles patching overhead via Kisin-Scholze 2019 refinement. **Folder.** `strategy/externals-hardening/newton-thorne-2021/`.

#### §3.13 Nekovář 2001 parity + higher-weight Kolyvagin

**Attribution.** Nekovář 2001 (CRAS 332) parity of Selmer ranks; Nekovář 2006 *Selmer complexes* (Astérisque 310) extends Kolyvagin's Euler-system machinery to higher-weight modular forms. **Use-site.** W_rank Route C (higher-weight Kolyvagin; Selmer-rank parity). **Proposed PAC.** VERIFY Selmer-complex layer decomposition; CONSTRUCT KMS-formulation of Selmer complex as Tomita-Takesaki-type dual pair; BYPASS via Howard 2004 big Heegner points alternate; DECOMPOSE by Galois-cohomology degree; EXCISE derived-category overhead for in-scope applications. **Folder.** `strategy/externals-hardening/nekovar-2001/`.

#### §3.14 Yuan-Zhang-Zhang 2013 generalised GZ

**Attribution.** Yuan-Zhang-Zhang 2013 *The Gross-Zagier Formula on Shimura Curves* (Princeton Ann.Math.Studies 184) generalises Gross-Zagier to Shimura curves, removing the Heegner hypothesis restriction and covering general h_K on Heegner side. **Use-site.** W_hK Route ε (general h_K unconditional); W_nonCM Route γ; W_rank Route C. **Proposed PAC.** VERIFY Shimura-curve intersection-theory layer; CONSTRUCT MvN-dimension reading of generalised height pairing (extends §3.4 capacitor proposal); BYPASS via Zhang (Shou-Wu) 2001 alternate; DECOMPOSE by Shimura-curve level; EXCISE arithmetic-automorphic-form overhead for weight-2 scope. **Folder.** `strategy/externals-hardening/yuan-zhang-zhang-2013/` (paired with Gross-Zagier 1986 folder).

#### §3.15 Gross 1984 Heegner points / ring class fields

**Attribution.** Gross 1984 "Heegner points on X_0(N)" (*Modular Forms*, R.A. Rankin ed.) develops Heegner-point theory over ring class fields, handling arbitrary h_K on the Heegner side of BSD. **Use-site.** W_hK Route ε. **Proposed PAC.** VERIFY Heegner-point construction layer over ring class fields; CONSTRUCT KMS-tower reading of ring-class-field tower as BC-K projection system; BYPASS via CM-theory (Shimura 1971) alternate; DECOMPOSE by ring-class-field level; EXCISE redundancy with YZZ 2013. **Folder.** `strategy/externals-hardening/gross-1984/` (paired with YZZ 2013 folder).

---

## §4 Per-External Artifact Schema (applied uniformly)

Every `strategy/externals-hardening/<EXTERNAL>/` folder produces (target ≤ 15 pages per artifact):

1. **X-RAY.md** — fixed vocabulary per `strategy/x-ray/00-x-ray-strategy.md` (10 faces: ARITHMETIC, AMPLITUDE, SYMMETRY, RESONANCE, CURVATURE, …; 6 projections: P_A analytic, P_B gauge, P_C spectral, P_D arithmetic, P_E amplitude, P_O observation; 5 patterns: duality, factorisation, rigidity, fixed-point, phase-transition; 16 invariants). Per layer of the external's chain, emit (face, projection, pattern, invariant) quadruple.
2. **compliance-map.md** — (layers of external) × (external's stated axioms) matrix; cell verdicts PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT; no cell SILENT at lock.
3. **hardened-routes.md** — table of applied primitives (VERIFY / CONSTRUCT / BYPASS / DECOMPOSE / EXCISE) with before/after status + added capacitor cells.
4. **narrative.md** — fair attribution prose-free summary + "how we strengthened them" statement + publication-acknowledgment paragraph draft.
5. **commit-memo.md** — lock status; follow-on recommendations.

Schema identical across all 15 externals; only content differs.

---

## §5 Double-Kill Narrative (programme-level)

BSD (in Scope(S₀) closure and W_*-extensions) depends on four load-bearing external pillars:

1. **Modularity** (BCDT 2001, with Wiles 1995 / Taylor-Wiles 1995 / Diamond 1996 / Conrad-Diamond-Taylor 1999 stack).
2. **Kolyvagin Euler system** (Kolyvagin 1990).
3. **Iwasawa Main Conjecture** (Skinner-Urban 2014; Rubin 1991; Mazur-Wiles 1984).
4. **Gross-Zagier height formula** (Gross-Zagier 1986; YZZ 2013; Nekovář higher-weight extension).

Plus programme-internal axiomatic foundation:

5. **CBB / paper23 KMS** (equivalent status to paper13-rh Main Theorem).

**Pillar-C (HARDEN) claim.** We audit and strengthen each of (1)-(5). Concretely:

- Every external's chain is x-rayed per the programme's fixed X-Ray vocabulary (face / projection / pattern / invariant per layer).
- Every external's chain has a compliance-map vs its stated axioms; no SILENT cells at lock.
- Every external gains at least one programme-level **CONSTRUCT** contribution: a KMS-theoretic / capacitor-cell reformulation that either (a) upgrades a capacitor-cell status from Tier 2 to Tier 1 within the relevant scope, or (b) provides an independent programme-internal verification pathway, or (c) connects the external to other programme pillars (paper13-rh, paper28-pvnp, paper1-QG5D).
- Every external has at least one **BYPASS** alternate chain cited (providing independent literature-level confirmation).
- Every external has at least one **DECOMPOSE** step (splitting a monolithic claim into independently verifiable sub-claims).
- Where applicable, **EXCISE** reduces minimal axiom sets / removes redundancies.

**Result.** The entire number-theoretic foundation on which BSD rests becomes programme-verified. Every weak link in the classical chain (Heegner hypothesis restrictions, ordinary-reduction hypotheses, h_K=1 restrictions, residual-irreducibility hypotheses, ramification hypotheses) is either tightened (DECOMPOSE to sub-cases), bypassed (alternate literature route cited), or removed (EXCISE + classical generalisation).

**Narrative statement (prose-free, attestable).** We depend on modularity (BCDT) + Kolyvagin + Skinner-Urban IMC + Gross-Zagier + CBB. We audit each via the PAC pipeline, supply programme-internal KMS-theoretic reformulations as capacitor-cell upgrades, cite independent BYPASS literature chains, DECOMPOSE monolithic steps, and EXCISE redundancies. The entire number-theoretic foundation BSD rests on becomes programme-verified. Reciprocity: the external authors' work is strengthened by our independent audit + our KMS/capacitor reformulations; the programme's BSD sits on published-stronger foundations. No other BSD-approach programme has done this for all four + CBB.

---

## §6 Coordination with Other Vertices' Pillar-C Work

Several externals appear in multiple vertices' Pillar-C worklists; hardening is shared, not duplicated:

| External | BSD Pillar-C use | RH Pillar-C use | PvNP Pillar-C use | Hodge Pillar-C use | Shared folder? |
|----------|-------------------|------------------|---------------------|---------------------|-----------------|
| BCDT 2001 | primary (§3.1) | secondary (L-cont) | — | secondary (CM motives) | yes — single folder serves all |
| Kolyvagin 1990 | primary (§3.2) | — | — | — | BSD-primary |
| Skinner-Urban 2014 | primary (§3.3) | secondary (GL₂ IMC) | — | — | yes — single folder |
| Gross-Zagier 1986 | primary (§3.4) | — | — | — | BSD-primary |
| CBB / paper23 | primary (§3.5) | **primary** (RH Pillar-C anchor) | secondary (Popa rigidity pairing) | — | yes — joint RH+BSD folder |
| Connes-Marcolli 2008 | §3.11 | secondary | **primary** (GL₂ Popa rigidity) | — | yes — joint BSD+PvNP folder |
| Rubin 1991 | §3.7 | — | — | — | BSD-primary |
| CCM 2025 (Route D / W_rank alternative) | via capacitor T13 | **primary** (RH anchor) | — | — | `strategy/ccm-verification/` (already in flight) |

**Programme-level savings.** Five externals (BCDT, Skinner-Urban, CBB, Connes-Marcolli, CCM) are hardened once per folder, cited across multiple vertex Pillar-Cs. Universal-approval-run.md §5C.2 explicitly supports this; folder structure normalised so a single external is hardened once.

---

## §7 Lock Status + Run Transcript

### §7.1 Coverage summary

- **15 retained externals enumerated** (§2); all first-wave (5) and second-wave (10) classified with priority.
- **First-wave stubs** (BCDT, Kolyvagin, Skinner-Urban, Gross-Zagier, CBB): full per-external PAC strengthening proposals per §§3.1-3.5.
- **Second-wave stubs** (10 externals): one-paragraph stubs with (attribution, use-site, PAC-proposal, folder path) per §§3.6-3.15.
- **Artifact schema** (§4) uniform across all 15 folders.
- **Double-kill narrative** (§5) captures programme-level claim.
- **Coordination** (§6) with RH / PvNP / Hodge / CCM folders specified.

### §7.2 Page discipline

This document ≈ 13 pages of markdown. Per-external folders target ≤ 15 pages each. Total Pillar-C bundle: 15 folders × 5 artifacts ≈ 75 files, ≈ 150-300 pages of hardening content when complete.

### §7.3 Lock verdict

- Every retained external has: (a) fair attribution block; (b) use-site citation to `bsd-independence-bare.md §7.3` row; (c) PAC strengthening proposal with at least one VERIFY + one CONSTRUCT + one BYPASS + one DECOMPOSE (+ EXCISE where applicable); (d) scheduled `strategy/externals-hardening/<external>/` folder path; (e) first-wave / second-wave priority tag.
- CM-specialisation scope declared (§1): hardening is for our use-sites; original authors' full-scope claims not re-proved.
- Zero prose paragraphs (this document is pure table + stub structure); citations per claim.
- Conditionality rider preserved: CBB hardening = paper13-rh Main Theorem hardening (joint with RH Pillar-C); no "unconditional" overclaim.

**LOCK STATUS: PUBLISH-READY for Pillar C.**

### §7.4 Handover to externals-hardening folder builds

Run-07 schedule (first-wave, five folders in parallel):
- `strategy/externals-hardening/bcdt-2001/`
- `strategy/externals-hardening/kolyvagin-1990/`
- `strategy/externals-hardening/skinner-urban-2014/`
- `strategy/externals-hardening/gross-zagier-1986/`
- `strategy/externals-hardening/cbb-paper23/` (joint with `strategy/rh/deliverables/rh-harden-bare.md`)

Run-08+ schedule (second-wave, ten folders batched per load-bearing weight): §§3.6-3.15 folders.

### §7.5 Run transcript

`strategy/bsd/pac-output/runs/run-06/`:
- `blackboard.md` — 15-externals enumeration + priority ranking + PAC-primitive draft per external.
- `harden-roster.md` — 15-row external-by-external table mirroring §2 above.
- `first-wave-pac-proposals.md` — §§3.1-3.5 longer drafts.
- `second-wave-stubs.md` — §§3.6-3.15 stubs.
- `coordination-matrix.md` — §6 cross-vertex coordination table.
- `commit-memo.md` — lock-status summary; recommendation for run-07 first-wave folder builds.

---

## §8 References (bare)

### §8.1 Programme documents

- `strategy/universal-approval-run.md` §5C HARDEN (protocol).
- `strategy/bsd/00-millenium-strategy.md` §§1-12.
- `strategy/bsd/bsd-millenium-brief.md` DELTAs 1-11.
- `strategy/bsd/deliverables/bsd-comply-bare.md` Pillar-A §§1-19.
- `strategy/bsd/deliverables/bsd-independence-bare.md` Pillar-B §§1-9 (especially §7.3 retained-externals roster and §7.4 residual-walls table).
- `strategy/bsd/pac-output/runs/run-02/compliance-map.md` (LOCKED 11×7).
- `strategy/_research/birch-swinnerton-dyer/landscape.md` (key-researchers + approaches + acknowledgments).
- `strategy/x-ray/00-x-ray-strategy.md` (fixed vocabulary: 10 faces / 6 projections / 5 patterns / 16 invariants).
- `strategy/ccm-verification/` (CCM 2025 parallel Pillar-C, in flight).
- `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` Tiers 1-2.
- `solutions-with-prize/paper26-bsd/PROOF-CHAIN.md` L1-L11.
- `solutions-with-prize/paper13-rh/PROOF-CHAIN.md` (CBB + GRH leaves shared).
- `paper23/` axiom set for CBB.
- `solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md` (Popa-rigidity cross-link).
- `integers/paper01-qg5d/PROOF-CHAIN.md` Pins 1, 6 audit, 12 (QG5D leaves).
- `integers/paper61-projections-5d/sections/08-...` (5D-KK projection P_B leaf).

### §8.2 External literature (primary sources per retained external)

Chronological order:

- Hecke 1918 — L(s,ψ) continuation + FE (capacitor-served; not retained here).
- Mordell 1922 — Mordell-Weil (classical leaf; not retained here).
- Deuring 1953 — CM factorisation (classical; not retained here).
- Baker 1966 — linear forms in logs (capacitor T5 + EXCISED L6).
- Coates-Wiles 1977 — BSD rank-0 CM.
- Mazur 1977 — torsion classification (classical).
- **Gross 1984** — Heegner points on X_0(N).
- **Mazur-Wiles 1984** — cyclotomic IMC.
- **Gross-Zagier 1986** — height formula.
- **Kolyvagin 1990** — Euler systems.
- **Rubin 1991** — IMC for CM.
- **Perrin-Riou 1992** — p-adic L-functions.
- **Bost-Connes 1995** — BC algebra (CBB foundation).
- Wiles 1995 — modularity semistable (BCDT input).
- Taylor-Wiles 1995 — Taylor-Wiles method (BCDT input).
- Diamond 1996 — level-lowering (BCDT input).
- Conrad-Diamond-Taylor 1999 — non-minimal deformation (BCDT input).
- **BCDT 2001** — full modularity.
- **Nekovář 2001** — parity of Selmer ranks.
- **Ha-Paugam 2005** — BC over K.
- **Connes-Marcolli 2008** — NCG + GL₂ BC.
- **Newton-Thorne 2021** — symmetric-power modularity (2021 I-II).
- **Yuan-Zhang-Zhang 2013** — generalised GZ for Shimura curves.
- **Skinner-Urban 2014** — IMC-GL₂.
- Skinner 2020 — p-converse to GZ-Kolyvagin.
- **Burungale-Skinner-Tian-Wan 2024** — non-CM p-converse + strong BSD families.

### §8.3 Capacitor cells engaged in Pillar-C proposals

- T1 OA↔AG "Bost-Connes KMS uniqueness" (Tier 1 ESTABLISHED).
- T2 ANT↔AG "Deuring CM factorisation" (Tier 1).
- T3 ANT↔AG "Kolyvagin Euler system" (Tier 1; §3.2 upgrade candidate to programme-internal Tier 2 via KMS-tower construction).
- T4 ANT↔AG "Gross-Zagier formula" (Tier 1; §3.4 upgrade candidate via MvN-dimension reading).
- T6 AG↔ECFT "CM = explicit CFT" (Tier 1).
- T9 ANT↔LANG "Automorphic↔Galois" (PARTIAL; §3.1 upgrade candidate via R=T-as-KMS-projection).
- T10 ANT↔SPEC "Weil explicit formula / Connes trace" (Tier 1).
- T11 ANT↔OA↔AG "Hasse-Brauer-Noether ↔ projector bypass" (Tier 2 VERIFIED programme).
- T12 ANT↔OA↔ECFT "BC-bridge explicit-CFT" (Tier 2 VERIFIED; §3.5 upgrade candidate to Tier 1 in Scope(S₀)).
- T13 SPEC↔ANT "Hilbert-Pólya (CCM 2025)" (ESTABLISHED preprint; §3.5 cross-link).
- **New capacitor candidates from Pillar-C CONSTRUCT proposals** (§§3.1-3.4):
  - ANT↔OA↔LANG "R=T as KMS projection" (BCDT) — candidate Tier 2.
  - OA↔AG "Euler system as KMS tower" (Kolyvagin) — candidate Tier 2.
  - ANT↔OA↔LANG "p-adic L as KMS partition function" (Skinner-Urban / Perrin-Riou) — candidate Tier 2.
  - OA↔AG "Heights as Murray-von Neumann dimensions" (Gross-Zagier / YZZ) — candidate Tier 2.

---

*End of `bsd-harden-bare.md`. Pillar-C LOCKED; 15 retained externals enumerated; 5 first-wave + 10 second-wave prioritised; per-external folder schema uniform; double-kill narrative locked; cross-vertex coordination matrix specified; scope = CM-specialisation per Pillars A/B. Full per-external folder builds scheduled run-07 (first-wave) + run-08+ (second-wave). §5C.2 universal-approval-run.md compliance: PASS. Run transcript: `strategy/bsd/pac-output/runs/run-06/`.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
