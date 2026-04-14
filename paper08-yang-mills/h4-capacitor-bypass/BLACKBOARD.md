# Blackboard — H4 Capacitor Bypass PCA Run (Track 2)

**Run started:** 2026-04-13
**Runner:** Claude Opus 4.6 (1M context)
**Mode:** PCA bypass-hunting + capacitor-first (`execute`)
**Cycle:** 0 (Wave 0 in progress)

---

## §A North Star

**Deliverable:** `paper08-yang-mills/strategy/06-h4-capacitor-bypass-brief.md` (v3)

**Target:** GROW the H4-adjacent capacitor region to Millennium-submission grade. Tier 2 (capacitor gains 3-5 cells, ~65-75%) is the TARGET outcome — H4 bypass closure (Tier 1, ~7-12%) is the bonus if a cell closes the category-shift path. The capacitor IS the Millennium deliverable; Paper 8 ships conditional either way via Track 1 (L14 Route b) already in chain-verification/.

**Success criterion:** Every Wave 1 Author produces a durable capacitor cell-fill entry regardless of bypass verdict. Capacitor fill rate grows from 14.5% baseline toward 18-19%.

---

## §B Context

**H4 (Jaffe-Witten §4):** non-perturbative Schwinger functions of 4D SU(N) YM agree with perturbation theory at short distances. Leading-order OPE of $[\mathrm{Tr}\,F^2]_R$ correlator behaves as $C_N|x|^{-8}(\log 1/|x|\Lambda)^{-2}$ with $C_N = 2(N^2-1)/\pi^6$. Mildest form (W7-14 §5.3): Taylor coefficients of $F(t) := S_{2,t}^c(x,y)/c_1(t)^2$ at $t=0$ computed by standard Feynman-diagrammatic perturbative rules.

**Prior programme (`closing-H4/`, 2026-04-11):** A/B/C routes failed; Route D shipping form adopted. 9/10 cross-node LOCK on Taylor-coefficient attack surface.

**Chain state inherited from `chain-verification/`:** 17/17 proved links VERIFIED unconditional + L18 CONDITIONAL on H4. This run targets L18 specifically.

**v3 research calibration findings:**
- No 2023-2026 paper attempts non-perturbative OPE for 4D gauge theory
- Hollands-Wald 2024 is curved-spacetime OPE, not 4D gauge
- BFR Dec 2025 arXiv:2512.14227 §4 is scalar-only
- Nissim Oct 2025 arXiv:2510.22788 is lattice-only (continuum limit is a separate open step)
- arXiv:2506.00284 (Jacobsen "SU(3) YM proof") WITHDRAWN by arXiv admin as not research-quality (K-7)
- CERN 2024 resurgence programme (arXiv:2511.15528) + Dunne 2024-2025: most live 2024-2026 machinery

---

## §C Current bottleneck

**Wave 0 LOCK introspection in progress.** Runner has just written LOCK-ANATOMY + BYPASS-PREDICTION entries (below in §K). LOCK-ANATOMY Critic dispatched; pending verdict. If SURVIVED → Wave 1 dispatches 5 parallel Authors per brief §9.

---

## §D Toolkit (seed; populated as Wave 1 returns)

| Name | Statement | Source | Status |
|---|---|---|---|
| H4 (Jaffe-Witten) | NP Schwinger fns match pert at short dist; $C_N = 2(N^2-1)/\pi^6$ | W7-14 §5.3 + Jaffe-Witten §4 | CONDITIONAL |
| Route A LOCK | Taylor-coefficient identification via identity theorem on F(t) — LOCKED at 9/10 | closing-H4 closure-digest | R (kill, scope-limited) |
| K-1 CCM port | CCM 2025 spectral triple → YM: category error | closing-H4 §F | R (kill) |
| K-2 spectral action | Connes 2007 §5 classical/bare at Λ | closing-H4 §F + Vassilevich 2003 | R (kill) |

Capacitor v1 consulted: see `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md`.

---

## §F Killed approaches (inherited + new)

| ID | Pattern | Kill |
|---|---|---|
| K-1 | External-source-inconsistency + Wrong-space | CCM 2025 → YM port (RH targets zeros of entire function; YM targets Taylor coefficients of analytic function; Hurwitz requires the former) |
| K-2 | External-source-inconsistency + Vacuous | Spectral action + Identity 12 + bridge family k=4: Connes 2007 §5 classical/bare at Λ; Vassilevich 11N/3 counter-term, not slope |
| K-3-extended | Structural-not-rigorous | `paper12/research/53-transposition-asymptotic-freedom.md` BC running α_BC(β) — does not address non-perturbative Schwinger function asymptotics |
| K-4 (v2) | Category-substitution-error | Feehan-Maridakis Łojasiewicz-Simon trap — energy functional analyticity ≠ flow-time Taylor analyticity |
| K-5 (v3 strengthened) | Shortcut-through-perturbative-matching + continuum-limit-elision | ERG→OPE naive reduction: Nissim 2510.22788 is lattice-only; continuum limit is a separate open step; $C_N$ derivation requires three sub-steps |
| K-6 (v2) | Perturbative-level-confusion | Hollands-Kopper 2011 perturbative OPE convergence ≠ non-perturbative OPE |
| K-7 (v3) | Discredited-primary-source | arXiv:2506.00284 (Jacobsen SU(3) YM) withdrawn by arXiv admin June 2025; do not cite |
| K-8 (v3 NEW, from W1-R2) | Structural-conflation (ambiguity magnitude vs Wilson coefficient) | **Transseries-reads-$C_N$ trap**: the IR renormalon at Borel-plane position $u=2$ encodes the *ambiguity magnitude* (dimension-4 gluon condensate via Parisi-SVZ dictionary, $\sim\Lambda^4/Q^4$ scale), NOT the leading Wilson coefficient. $C_N = 2(N^2-1)/\pi^6$ is perturbative (one-loop free-field, different object at different $1/Q$ order). Re-entry gate: requires independent derivation of $C_N$ from non-perturbative transseries structure (no candidate mechanism exists; Stokes constants for 4D SU(N) YM renormalons are unknown). |

---

## §J Voice canon

Inherited from 2026-04-11 closing-H4 programme:
- *"H4 is still the wall"*
- *"The wall stays named"*
- *"Paper 8 ships either way"*
- *"Three routes down. One route up."*

If bypass found: *"H4 is on disk"* / *"The wall fell from [domain] direction via [N] steps"*
If no bypass: *"H4 stood this attack"* / *"The capacitor gained N cells; the wall stayed named"*

---

## §K Runner writes

### Cycle 0 LOCK-ANATOMY (2026-04-13, Wave 0 mandatory per brief §3.0.5)

**What the 9/10 LOCK binds (exact scope per `closing-H4/closure/closure-digest.md`):**

The LOCK statement verbatim: *"Taylor-coefficient identification is the attack surface for H4 closure via analyticity/identity-theorem mechanisms, and it is genuinely stuck for any Route A-style closure."*

**Load-bearing failure rows (non-overlapping) from R.A.1 + R.B.1:**
- **R.A.1 failure row** (Fix 1 per Wave 0 Critic: Distributional + Wrong-space stated as non-overlapping components):
  - *Distributional component*: $F^{\mathrm{pert}}(t)$ is a formal power series (divergent, expected from renormalons in 4D YM), not a convergent series. As a distribution-theoretic object it is not an analytic function in any neighborhood of $t=0$.
  - *Wrong-space component* (distinct from distributional): even treating $F^{\mathrm{pert}}$ charitably, the two-function pair $(F, F^{\mathrm{pert}})$ is not in the function space where the identity theorem applies. The identity theorem requires two analytic functions on a common connected open domain agreeing on a set with an accumulation point; $F$ may be analytic (if it exists as a limit of Schwinger functions), but $F^{\mathrm{pert}}$ lives in the space of formal power series, not analytic functions. Different function spaces — no shared domain to apply the theorem on.
- **R.B.1 failure row**: YM target data would be Taylor coefficients of an analytic function, but CCM 2025 machinery requires zeros of an entire function. Distinct Wrong-space category error from R.A.1's: dictionary entries #12-17 map the YM side to an object CCM's machinery cannot produce. Hurwitz requires the entire-function form, which is not what the YM side delivers. Pattern: Wrong-space (category mismatch at the object level) + External-source-inconsistency.

The two failure rows are **non-overlapping**: R.A.1's Wrong-space is function-space-level (formal series vs analytic function); R.B.1's Wrong-space is category-level (analytic-function Taylor coefficients vs entire-function zeros). Different pattern categories; different closure obstructions; same surface (Taylor-coefficient identification via identity theorem).

**Variants LOCK-rejected (17+ tested across Beta/Delta/Runtime Critics):**
- Beta-Critic tested 11 variant candidates for K-1 + K-2 escape (K-1.5 Laplace-transform, K-1.6 Borel-transform, K-1.7 Hermite-moment, K-1.8 Mellin-gamma zeros, Yakaboylu 2024 port, CCM prolate-wave 2024, framework BC spectral triple CM 2008 θ-summable; twisted BC $H_{BC}-s\mathbb{1}$, crossed-product $D_{M^4}+\gamma\otimes\mathrm{sign}(H_{BC}-1/2)$, hybrid R.B.1×R.C.1 flow-time Dirac, framework BC spectral triple θ-summable) — **all 11 fail**
- Delta-Critic tested 6 variant third-Route-A mechanisms (lattice-to-continuum direct match via Reisz, Borel summability, Hamburger moments, SVZ instanton-obstruction, gradient-flow spectral action, alternative NCG source) — **5/6 hit existing failure rows; 1 residual hypothetical (non-CCM-2025 NCG source) routes back through same attack surface**

**What the LOCK does NOT bind (the bypass space for this run):**

1. **Microlocal / wave-front set restatement of H4** — category shift. H4 restated as a regularity claim about the Schwinger distribution $S_2^{\mathrm{ren}}(x,y)$ at $x=y$, not as Taylor-coefficient identification of a function. Different mathematical object. Hörmander propagation-of-singularities + algebraic-QFT microlocal machinery are not LOCK-bound.

2. **Axiomatic OPE convergence (non-perturbative)** — category shift. H4 restated as a non-perturbative OPE convergence statement in an algebraic QFT framework. Different algebraic object. Hollands-Wald / BFR / Brunetti-Fredenhagen-Hollands-Wald axiomatic framework (IF extended to 4D gauge; currently scalar-only) is not LOCK-bound.

3. **Lateral Borel summation in complex $t$** (Fix 3 per Wave 0 Critic: clarify distinction from tested variant):
   - *Standard Borel summability on $\mathbb{R}_+$* WAS tested by Delta-Critic (one of its 6 variants) and FAILED — IR renormalons produce Gevrey-1 non-Borel-summability along the real positive axis. This variant is LOCK-adjacent and re-entry is gated.
   - *Lateral Borel in complex $t$* (Écalle resurgence, away from $\mathbb{R}_+$) is **structurally distinct** and was NOT tested by the closing-H4 programme. Resurgent transseries can produce H4 from renormalon cancellation structure in lateral sectors without Taylor-coefficient identification via identity theorem on the real axis. The ambiguity along the IR-renormalon cut may be resolved by median summation + instanton/anti-instanton cancellation, producing a bona fide analytic continuation in a lateral sector where identity-theorem-free mechanisms (resurgent transseries matching) apply. CERN 2024 resurgence programme (arXiv:2511.15528) + Dunne 2024-2025 lectures are the live machinery for this variant.
   - **Conclusion**: the LOCK binds standard $\mathbb{R}_+$ Borel (tested); it does NOT bind lateral Borel in complex directions (untested, structurally distinct mechanism via resurgence).

4. **Ergodic / cluster-expansion construction** (Fix 2 per Wave 0 Critic: acknowledge sub-step (b) structural risk):
   - Category shift AT THE CONSTRUCTION LEVEL. If a non-perturbative Schwinger function exists via Langevin + cluster expansion (Nissim 2510.22788 lattice-only; continuum limit is a separate step), its UV singular structure can be analyzed directly from the construction WITHOUT going through Taylor-coefficient identification.
   - **Structural risk at sub-step (b) UV extraction**: asymptotic-matching the constructed Schwinger function against $F^{\mathrm{pert}}(t)$ to extract UV behavior re-introduces Taylor-coefficient identification in disguise and lands back inside the LOCK. **Conditions under which UV extraction avoids this**: the UV singular structure must be computed intrinsically from the constructional quantities (polymer activities, Langevin stationary measure, transfer-matrix spectrum), producing $C_N$ directly as a construction-level quantity, NOT by matching to $F^{\mathrm{pert}}$. Hastings-Koma-style spectral-gap + polymer-decay arguments extracting the $|x|^{-8}$ scaling from the construction itself are outside the LOCK; asymptotic-match-to-perturbative-series arguments are inside the LOCK (hit K-5).
   - Route is NOT foreclosed but requires (a) continuum limit + (b) intrinsic UV extraction from constructional quantities (not by pert-matching) + (c) $C_N$ derivation as three open sub-steps.

5. **Cross-domain exploration via unexplored capacitor cells** — category shift by construction. LANG↔QFT (Kapustin-Witten S-duality), or other candidate cells from capacitor v1 §Candidates, may give an H4-equivalent statement on the dual side without ever touching Taylor coefficients. Capacitor-first deliverable.

**LOCK-adjacent approaches in THIS run that must NOT be re-attempted** (Fix 4 per Wave 0 Critic: expanded to mirror §F — Wave 1 Authors read §K, not §F):
- Direct Route A variants (Taylor-coefficient identification via identity theorem on F(t)) — any approach attempting to make F(t) and F^pert(t) agree at the Taylor-coefficient level via analyticity is LOCK-bound
- CCM port variants (K-1: 7 new Beta variants tested, all fail)
- Spectral action variants (K-2: 4 new Beta variants tested, all fail)
- BC running $\alpha_{BC}(\beta)$ mechanism from `paper12/research/53-transposition-asymptotic-freedom.md` (K-3-extended: structural not rigorous; doesn't address non-perturbative Schwinger function asymptotics)
- Feehan-Maridakis energy-functional analyticity claim (K-4 trap — energy functional on connection space ≠ flow-time Taylor coefficients; wrong object)
- Naive ERG→OPE reduction via asymptotic-match-to-pert-series (K-5 strengthened: shortcut-through-perturbative-matching + continuum-limit-elision — lands back in LOCK; Nissim is lattice-only anyway)
- Hollands-Kopper perturbative OPE convergence claim (K-6 trap — this is perturbative OPE convergence, not non-perturbative OPE matching)
- Citing arXiv:2506.00284 (K-7 — withdrawn crank paper; discredited primary source)
- Standard Borel summability on $\mathbb{R}_+$ for 4D YM (Delta-Critic variant, tested, failed on IR renormalons — Gevrey-1 non-Borel-summability on real axis; lateral Borel in complex directions is OPEN and NOT in this list)

---

### Cycle 0 BYPASS-PREDICTION (2026-04-13, per brief §3.0.6)

**Expected compound bypass shape for THIS run (pre-registration):**

A successful Tier 1 bypass in this run would most likely route through:
- **Step 1 (category shift):** MICRO↔QFT — restate H4 as wave-front-set regularity claim for $S_2^{\mathrm{ren}}(x,y)$ at $x=y$
- **Step 2 (framework construction):** a non-perturbative 4D gauge OPE framework (a gauge extension of BFR's scalar-only non-perturbative C*-algebra) would need to be constructed or at minimum characterized as a well-posed research programme
- **Step 3 (Schwinger distribution existence):** possibly via ERG↔QFT (Nissim continuum extension) providing the non-perturbative object
- **Step 4 (AF structure extraction):** axiomatic argument that the gauge OPE framework's axioms force the $C_N|x|^{-8}(\log)^{-2}$ asymptotic

Alternative Tier 1 shape:
- **Step 1:** PROB↔SPEC / resurgence — lateral Borel in complex $t$ produces F(t) as the Borel sum of a genuinely analytic function (in a Gevrey class)
- **Step 2:** identity theorem now applies (because F(t) is actually analytic in a lateral sector); Taylor coefficients match $F^{\mathrm{pert}}$ in the sense of the Borel transform
- **Step 3:** renormalon cancellation structure (resurgent transseries) encodes the AF logarithmic correction

Total expected steps if Tier 1 lands: **3-5 steps, composed through 2-4 capacitor cells**.

**If Wave 1 returns a DIFFERENT shape from both of the above**, the strategy was miscalibrated; the runner re-plans.

### Wave 1 post-return annotation (2026-04-13): BYPASS-PREDICTION Alternative-1 has a structural gap

W1-E (ERG↔QFT) returned CONJECTURED-NEGATIVE with a specific coordination finding: **the BYPASS-PREDICTION Alternative-1 Step 3 (ERG↔QFT supplies the non-perturbative Schwinger distribution for MICRO Step 3) is REFUTED**. Nissim 2510.22788 is lattice-only; no continuum Schwinger distribution is available for MICRO to consume. W1-M (MICRO) independently characterized its 5-step compound bypass assuming a non-perturbative Schwinger distribution existed; without ERG supplying it, MICRO Step 3 has no extant source. The compound-bypass shape Alternative-1 had a hidden dependency that Wave 1 exposed.

**Updated bypass shape** (for future runners): the compound Alternative-1 requires an additional upstream unlock — a continuum non-perturbative Schwinger distribution existence theorem for 4D SU(N) YM — which neither Nissim (lattice) nor Magnen-Rivasseau-Sénéor 1993 (IR-cutoff uncut) supplies. This is a **distinct open step** not listed in the original pre-registration.

**Tier 2 expected outcome (target):** each Wave 1 Author returns a durable cell-fill entry in capacitor v1 format (Statement / Mechanism / Source / Status — including CONJECTURED-NEGATIVE status / Verification data / Load-bearing for / Transposition recipe). Capacitor gains 3-5 cells (MICRO↔QFT, PROB↔SPEC resurgence, ERG↔QFT, LANG↔QFT candidate, possibly others discovered during Wave 1). Capacitor fill rate: 14.5% → ~18-19%. Millennium deliverable grows.

---

### Cycle 1 SYNTHESIS-INSIGHT (2026-04-13, post-Wave 1 / post-Synthesis)

**$C_N$ is perturbative; the lateral-Borel task is Gevrey-analyticity only.**

W1-R2 produced a key structural clarification that W1-R1 implicitly relied on: **$C_N = 2(N^2-1)/\pi^6$ does NOT need to be re-derived from the transseries or from any non-perturbative machinery.** It is a one-loop perturbative Feynman-rule computation, and its value is already in hand (from free-field OPE calculations at $g=0$). What H4 requires — via the W7-14 §5.3 mildest form — is not a new derivation of $C_N$ but **establishment that $F(t)$ is analytic in a neighborhood of $t=0$ in some sector** so that Taylor coefficients match the known perturbative series.

**Implication for the PROB↔SPEC lateral-Borel route**: the sole open question is whether the lateral Borel sum is Gevrey-analytic in a sector allowing Watson-type boundary-value matching. Two named unlocks:
- **UNLOCK-1**: extend BZJ/Dunne-Ünsal resurgent closure from $\mathbb{R}\times T^3$ twisted BC to uncompactified $\mathbb{R}^4$ (currently CONJECTURED per Yamazaki-Yonekura 2017; Dunne CERN 2024 calls it active research)
- **UNLOCK-2**: establish Watson-type sectorial boundary-value matching $F^{\mathrm{lateral}}|_{\arg t \to 0} = F^{\mathrm{physical}}$ for 4D YM

If UNLOCK-1 + UNLOCK-2 land, lateral-Borel DOES close H4 — because $C_N$ is already computed perturbatively, and the Gevrey analyticity supplies what the identity theorem needs on the physical side. This is the **cleanest Tier 1 shape** remaining after Wave 1. It does NOT require resolving transseries structure for $C_N$ (K-8). It requires UNLOCK-1 + UNLOCK-2.

---

### Cycle 0 CAPACITOR-SCAN

Domain of H4 (single-link target): QFT + SPEC + ANT. Priority cells for Wave 1 dispatch per brief §3.1 v3 reprioritization:

- **co-P1 MICRO↔QFT** (Hollands-Wald + BFR + Dappiaggi — framework construction expected)
- **co-P1 PROB↔SPEC lateral** (CERN 2024 + Dunne — most live machinery)
- **P2 ERG↔QFT** (Nissim lattice-only; K-5 strengthened warning)
- **P3 LANG↔QFT** candidate cell (Kapustin-Witten S-duality, pure capacitor exploration)

Dropped: THERMO↔QFT (P2 v1), DTOP↔SPEC (P4 v1, K-4 trap).

---

## §M Round metrics

| cycle | wave | authors | critics | cells filled | kills added | notes |
|---|---|---|---|---|---|---|
| 0 | W0 | 0 | 1 (pending) | 0 | 0 | LOCK-ANATOMY Critic dispatched |

---

## §O Pointers

- Chain state inherited from `../chain-verification/chain/chain-state.md` (17/17 proved VERIFIED + L18 CONDITIONAL)
- Capacitor `../../millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md`
- Prior H4 programme `../closing-H4/closure/closure-digest.md`
