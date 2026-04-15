# Paper 9 Legacy — Theorem Index and Framework Grammar

*Consolidated archive created 2026-04-14 as part of Intervention 6 (three-corpus
reorganization). Paper 9 itself ("One Postulate, Ten Papers: The Geometric
Framework and Its Grammar") declared no new theorems — it was a documentation
paper mapping the theorem index of the series and articulating the six patterns
plus the three geometries. Its theorem-index content has been superseded:*

- **Canonical home for theorem indexing**: Paper 12's theorem catalogs
  (see `integers/paper12-cbb-system/`).
- **Machine-readable catalog**: `integers/paper01-qg5d/code/theorem-catalog/CATALOG.json`.
- **Pattern-attribution narratives**: absorbed into `strategy/north-star.md`
  (§ Programme Overview) and the per-vertex briefs in
  `strategy/<vertex>/deliverables/`.

This file preserves the theorem index verbatim (primary payload), plus a brief
content inventory of Paper 9's preprint and research material so readers can
find the historical source on disk.

---

## Part 1 — Theorem Index (Verbatim from `paper9/theorems-list.md`)

*All original theorems, corollaries, lemmas, and propositions declared across
the ten-paper series. Organized by paper. For each result: its current name or
number, its proposed name (where not yet named), its location, and what it
establishes in one sentence.*

*Total: ~27 theorems, ~14 corollaries/lemmas/propositions across Papers 1–8.
Paper 10 (Riemann) theorems pending formalization.*

---

### Paper 1
#### Spin-Statistics, Aharonov-Bohm, Perturbative Finiteness, and Twenty-Two Derivations from Kaluza-Klein Geometry

| # | Current name | Proposed name | Location | What it establishes |
|---|-------------|---------------|----------|---------------------|
| 1 | **Theorem K.1** | Universal Epstein Vanishing | App K, §K.7b | E_L(−j; Q_L) = 0 for all j ≥ 1 and all loop orders L, forced by the pole structure of the completed Epstein zeta function — the engine of UV finiteness |
| 2 | **Theorem K.3** | BPHZ Factorization | App K, §K.5.3 | BPHZ-subtracted amplitudes factor as (4D finite part) × E_L(−j; Q_L), inheriting universal vanishing — finiteness survives renormalization to all orders |
| 3 | **Theorem S.1** | Perturbative Finiteness | App S | Linearized 5D gravity on M⁴ × S¹ is perturbatively UV finite to all loop orders under zeta regularization |
| 3a | **Theorem V.1** — Complete Vanishing of the Two-Loop R³ Counterterm | Two-Loop Goroff-Sagnotti Vanishing | App V, §V.6 (line 422) | Under zeta regularization, the R³ counterterm coefficient of linearized 5D gravity on M⁴ × S¹ is identically zero at two loops — c_KK(R³) = 0 from every topology (sunset, figure-eight, vertex, ghost), upgrading Theorem S.1's conditional claim to unconditional at L=2 |
| 3b | **Theorem P.1** — CPT Invariance | CPT Theorem | App P, §P.3 (line 98) | The 5D Einstein-Hilbert action on P(M⁴, U(1)) is invariant under (x, t, ψ) → (−x, −t, 2π − ψ); CPT is a consequence of 5D general covariance rather than a separate Streater-Wightman axiom chain |
| 3c | **Theorem B.1.1** — Classification (d ≥ 3) | Half-Integer Winding Classification | App B, §B.1.2 (line 52) | In d ≥ 3 spatial dimensions, the rotation-e coupling constant s ∈ (1/2)ℤ; forced by π₁(SO(d)) = ℤ₂ via the contractibility of 4π rotations in Spin(d) |
| 3d | **Theorem B.1.2** — Stability of the Boson-Fermion Dichotomy | Topological Stability of Statistics | App B, §B.1.4 (line 115) | The parity of 2s (boson vs. fermion) is a topological invariant: no continuous physical process can change s mod 1 ∈ {0, 1/2}, because compact Lie group representations are rigid |
| 3e | **Theorem B.1.3** — Anyon Statistics (d = 2) | Anyons in Two Dimensions | App B, §B.1.5 (line 142) | In d = 2 spatial dimensions, π₁(SO(2)) = ℤ removes the half-integer constraint: s ∈ ℝ is unconstrained, giving the continuous anyon family observed in the fractional quantum Hall effect |
| 3f | **Theorem B.2.1** — Exchange Phase (d ≥ 3) | Exchange Phase Theorem | App B, §B.2.3 (line 298) | For two identical particles in d ≥ 3 with rotation-e coupling s, exchange gives X ψ(r₁, r₂) = e^{i2πs} ψ(r₁, r₂); the phase is the holonomy of the e-connection around the non-contractible exchange loop in C₂(ℝᵈ) |
| 3g | **Corollary B.2.2** — Pauli Exclusion | Pauli Exclusion Principle | App B, §B.2.6 (line 381) | Two identical fermions (half-integer s) at coincident positions yield ψ = 0; Pauli exclusion is a geometric packing constraint on the e-circle, not an independent postulate |
| 3h | **Theorem B.3.1** — Spin as E-Momentum | Spin-Noether Identification | App B, §B.3.6 (line 578) | Ŝ_z = p̂_φ = −iℏ d/dφ on L²(S¹); the spin angular momentum is the Noether charge of rigid e-translation on the U(1) fiber, with the full SU(2) algebra inherited from the geometry of 3D rotations on the e-fiber |
| 3i | **Theorem B.3.2** — Winding Number = Spin Projection | Winding-Spin Correspondence | App B, §B.3.7 (line 601) | The e-dimension winding number n equals the spin projection quantum number m_s, and the spin quantum number s = max{|n|} over allowed winding states |
| 3j | **Theorem B.3.3** — Spin Determines Statistics | Spin-Statistics Theorem (geometric form) | App B, §B.3.8 (line 624) | The exchange phase e^{i2πn} = (−1)^{2s} is uniform across all spin projections m_s; integer spin ⇒ bosons, half-integer spin ⇒ fermions — the geometric conclusion of the full three-step B.1 → B.2 → B.3 chain |

---

### Paper 2
#### The Dark Matter-Baryon Ratio, Hubble and Clustering Tensions, and Thirteen Observables from Kaluza-Klein Geometry

*No new theorems declared. Results are derived consequences of Paper 1
theorems applied to the CAMB cosmological computation.*

---

### Paper 3
#### The Black Hole Information Paradox

| # | Current name | Proposed name | Location | What it establishes |
|---|-------------|---------------|----------|---------------------|
| 4 | **Corollary 3.1** | Hawking Temperature | §3.4 | The spin structure of the e-circle matches the Euclidean thermal circle at the horizon, fixing T_H = ℏκ/2πc uniquely |
| 5 | **Theorem 6.1** | *→ e-Unitarity Theorem* | §6 | e-charge is a Noether charge conserved by the full 5D evolution; the 5D state remains pure throughout black hole evaporation |
| 6 | **Theorem 9.1** | Horizon Vertex = 1 | §9, App A | The horizon vertex amplitude equals 1 by S¹ Fourier orthogonality — a topological fact that decouples the black hole geometry from the e-correlations and resolves the AMPS firewall |

---

### Paper 4
#### The Standard Model Gauge Group from Kaluza-Klein Geometry

| # | Current name | Proposed name | Location | What it establishes |
|---|-------------|---------------|----------|---------------------|
| 7 | **Theorem 5.2** | SLOCC-Isometry | §5.6 | The A₂ root system appears in the tangent space of the three-qubit SLOCC variety; the flag manifold identification maps entanglement geometry to the isometry group SU(3) × SU(2) × U(1) |
| 8 | **Spectral Gap** *(no theorem number)* | *→ Theorem 9.2 — Stable Spectral Gap* | §9 | The Dirac operator on CP² with Fubini-Study metric satisfies Δ_5D ≥ √5/r₃, stable to all perturbative corrections by Theorems K.1 and K.3 |

---

### Papers 5 and 6

*Results in Papers 5 and 6 are derived consequences of the holonomy
correspondence, topological rigidity, and Theorem K.1. No new theorems
declared. The Yang-Mills mass gap proof is developed fully in Paper 8.*

---

### Paper 7
#### Moduli Stabilization, GUT Unification, and the Cosmological Constant

| # | Current name | Proposed name | Location | What it establishes |
|---|-------------|---------------|----------|---------------------|
| 9 | **Theorem U** | Theorem U | §3.6 | Algebraic minimization of the G₄ flux potential gives R_bare ~ l_P — the e-circle radius sits at the Planck scale before the Casimir mechanism; r₃ cancels exactly |
| 10 | **Theorem U*** | Theorem U* | Frontier | Any algebraic function of the framework's O(1) geometric inputs produces O(1) outputs; the ratio R_obs/l_P ~ 10³⁰ is structurally unreachable — the cosmological constant problem is a type error, not a fine-tuning problem |

---

### Paper 8
#### The Yang-Mills Mass Gap

##### Part I — The Lattice Proof

| # | Current name | Proposed name | Location | What it establishes |
|---|-------------|---------------|----------|---------------------|
| 11 | **Theorem 1** — Internal Spectral Gap (Weitzenböck) | Internal Spectral Gap | §4.2 | The Hessian of the internal CP^(N-1) action at the flat connection satisfies Hess ≥ μ₁/g²_int where μ₁ = 6/r₃² — the seed from which the entire proof chain grows |
| 12 | **Corollary 1.1** *(unnamed)* | *→ KK Correlation Decay* | §4.2 | Internal fluctuations decay exponentially with correlation length ξ_int = r₃/√6 in the trivial topological sector |
| 13 | **Theorem 2** — Bond Activity Bound | Bond Activity Bound | §4.3 | KK bond interactions satisfy \|g_{⟨xy⟩}\| ≤ C₀e^{−m₁a} where m₁ = 2√3/r₃ — exponential suppression of inter-site couplings |
| 14 | **Theorem 3** — Cluster Expansion Convergence | Cluster Expansion Convergence | §4.3 | The cluster expansion converges absolutely when the bond constant satisfies the explicit bound — the expansion is not merely formal |
| 15 | **Theorem 4** — Lattice Mass Gap | Lattice Mass Gap | §4.4 | For SU(N) lattice gauge theory with CP^(N-1) harmonics in the k=0 sector: cluster expansion converges, free energy is analytic, correlators decay exponentially, string tension σ₀ > 0, mass gap Δ₀ ≥ c√σ₀ > 0 |
| 16 | **Corollary 4.1** *(unnamed)* | *→ String Tension Positivity* | §4.4 | The full SU(N) KK-enhanced lattice theory satisfies σ(β) > 0 for all β > 0 |
| 17 | **Theorem 5** — IR Equivalence | IR Equivalence | §4.5 | The standard SU(N) Wilson lattice gauge theory inherits the mass gap: Δ⁰_std ≥ Δ⁰_KK − Ce^{−m₁a} > 0 — the KK gap transfers to the physical theory |
| 18 | **Lemma 1** — Well-definedness | Well-definedness | §4.5 | The reduced transfer matrix T̂_red is well-defined, bounded, self-adjoint, positive, and trace-class |
| 19 | **Lemma 2** — Trace-norm Bound | Trace-norm Bound | §4.5 | \|\|T̂_red − T̂_std\|\|_tr ≤ C_tr\|Λ_t\|e^{−m₁a}\|\|T̂_std\|\|_tr — the two transfer matrices are exponentially close |
| 20 | **Lemma 3** — Spectral Perturbation | Spectral Perturbation | §4.5 | The spectral gap of the full transfer matrix is bounded below relative to the reduced transfer matrix |
| 21 | **Lemma 4** — Spectral Gap of T̂_red | Spectral Gap of T̂_red | §4.5 | The reduced transfer matrix satisfies Δ_red > 0, implying Δ_std > 0 |

##### Part II — The Continuum Limit

| # | Current name | Proposed name | Location | What it establishes |
|---|-------------|---------------|----------|---------------------|
| 22 | **Theorem 6** — Lattice Power Counting (partial) | Lattice Power Counting | §5 | The first moment of the irrelevant remainder vanishes; the zeroth moment bound is conditional on Conjecture 1 |
| 23 | **Theorem 7** — Perturbative Form Factor Bound | Perturbative Form Factor Bound | §5 | To all perturbative orders, the one-particle matrix element of the irrelevant remainder satisfies \|⟨1\|E_k(0)\|1⟩_c\| ≤ C₇g_k⁴Ĵ² |
| 24 | **Theorem 8** — Conditional Continuum Mass Gap | *→ Gap Persistence Theorem* | §5.7 | Assuming Conjecture 1, the renormalization group flow preserves the gap all the way to the continuum limit: Δ_∞ > 0 |

##### Appendix Theorems

| # | Current name | Proposed name | Location | What it establishes |
|---|-------------|---------------|----------|---------------------|
| 25 | **Theorem F.1** — Area Law Implies Mass Gap | Area Law Implies Mass Gap | App F | If a gauge theory satisfies area law with σ > 0, then Δ ≥ cσ — confinement forces a gap |
| 26 | **Lemma D.1** — Product Manifold RP | Product Manifold RP | App D | If M₁ satisfies reflection positivity and M₂ is compact positive-definite, then M₁ × M₂ satisfies RP |
| 27 | **Lemma D.2** — RP for KK Lattice Theory | RP for KK Lattice Theory | App D | The partition function of the KK-enhanced lattice theory satisfies reflection positivity |
| 28 | **Lemma I.1** — Operator Extraction | Operator Extraction | App I | Balaban's effective action decomposes as Wilson action + dimension-d operators + remainder |
| 29 | **Lemma I.2** — Lattice Symanzik Classification | Lattice Symanzik Classification | App I | All dimension-6 operators on the d=4 lattice fall into a finite classification with deviation orders ≥ 2 — closes the continuum limit |
| 30 | **Lemma I.3.1** — N-dependence | N-dependence | App I.3 | For each fixed N ≥ 2, the sums over KK mode contributions converge — constants are finite for all N |
| 31 | **Theorem I.4.1** — Universal Mass Gap | Universal Mass Gap | App I.4 | For ANY compact simple Lie group G (SU(N), SO(N), Sp(N), all exceptional groups), the Yang-Mills mass gap Δ_∞(G) > 0 |
| 32 | **Proposition I.4.2** *(unnamed)* | *→ Gauge Universality* | App I.4 | The three proof requirements (topological sector selection, KK hierarchy, Weitzenböck spectral gap) are satisfied by every compact simple Lie group — complete and proved, awaiting a name |

---

### Paper 9
#### One Postulate, Ten Papers: The Geometric Framework and Its Grammar

*No new theorems. This paper documents and maps the theorems of the series.*

---

### Paper 10
#### Scheme-Independence of UV Finiteness in 5D KK Gravity *(in preparation)*

*Closes the open problem stated in Paper 1 §U.2c: is the vanishing of the
Goroff-Sagnotti R³ counterterm scheme-independent, or an artifact of zeta
regularization? Paper 10 proves it is scheme-independent.*

- **Theorem 1 (Two-loop scheme-independent vanishing).** For 5D linearized
  gravity on M⁴ × S¹/Z₂, the Goroff-Sagnotti coefficient C_GS = 0
  unconditionally. The proof chain: Lemma A1 + Lemma A2 + Lemma A3 → vertex
  mass-independence → C_GS = [πR/4]² × J(0) × S₀² = 0 at leading order, with
  all subleading corrections vanishing by Theorem K.1. Proved.

- **Lemma A1 (de Donder gauge vertex numerator).** UV power counting,
  Z₂ parity projection, and Epstein vanishing as backstop together force the
  three-graviton vertex numerator to be n-independent at leading UV order.
  Proved (research memo 02).

- **Lemma A2 (Graviphoton/radion decoupling).** The A_μ and φ sectors do not
  contribute to the Goroff-Sagnotti counterterm at linearized order, by index
  structure (R^{(1)}_{μνρσ} is built from h_{μν} alone) and Z₂ selection rules.
  Proved (research memo 03).

- **Lemma A3 (KK loop momentum range).** The orbifold propagator on S¹/Z₂
  satisfies G_{Z₂}(y, y') = G_{S¹}(y, y') + G_{S¹}(y, −y'), restoring the
  full ℤ sum via the method of images. Proved (research memo 04).

- **Seeley-DeWitt one-loop vanishing (Route 02).** The coefficients
  a₂ = a₄ = 0 of the Lichnerowicz operator on the flat background M⁴ × S¹/Z₂
  are intrinsic spectral invariants. One-loop UV finiteness is scheme-independent
  as a theorem. Proved.

- **Z₂ parity cancellation (Route 03).** Algebraic, term-by-term cancellation
  between even (h_{μν}) and odd (h_{μ5}) KK contributions at each KK level
  n ≥ 1, holding in every Z₂-preserving scheme (dim-reg, symmetric cutoff,
  Z₂-paired Pauli-Villars, zeta). Strong structural result.

- **Poisson dim-reg bridge (Route 04).** Exchange lemma proved by Poisson
  resummation; dim-reg and zeta-reg pole coefficients agree to all orders,
  differing only by an exponentially suppressed e^{−2πRk} residual.

- **Weyl anomaly cohomology (Route 05).** Wess-Zumino consistency protects
  (a, c); since a_total = c_total = 0 under zeta regularization (using
  mass-independence of a₄ and S₀ = 0), they vanish in every
  diffeomorphism-preserving scheme. The Goroff-Sagnotti C³ operator is in
  the c sector and is therefore not generated by the KK tower in any such
  scheme. Proved for the GS sector.

*Open observation orthogonal to Theorem 1: the combined orbifold KK tower
satisfies a_grand = 19/240 ≠ 0 in curved backgrounds, from Z₂-asymmetric mode
counts of the h_{μν} + A_μ + φ sectors. This is a real, non-zero curved-background
effect, identified as an open frontier (§5.3).*

---

### Summary Table

| Paper | Theorems | Lemmas / Corollaries / Props | Named | Awaiting name |
|-------|----------|------------------------------|-------|---------------|
| 1 | 12 | 1 | K.1, K.3, S.1, V.1, P.1, B.1.1, B.1.2, B.1.3, B.2.1, B.2.2 (Cor), B.3.1, B.3.2, B.3.3 | — |
| 2 | — | — | — | — |
| 3 | 2 | 1 | Corollary 3.1, Theorem 9.1 | Theorem 6.1 |
| 4 | 1 | 1 | Theorem 5.2 | Spectral Gap |
| 5 | — | — | — | — |
| 6 | — | — | — | — |
| 7 | 2 | — | U, U* | — |
| 8 | 10 | 11 | Thms 1–7, F.1, I.4.1, D.1–2, I.1–3 | Thm 8, Cors 1.1 & 4.1, Prop I.4.2 |
| 9 | — | — | — | — |
| 10 | TBD | TBD | TBD | TBD |
| **Total** | **27** | **14** | **~36** | **6** |

---

### Named Theorems — Current and Proposed

| # | Theorem | Status | Paper | Why it travels |
|---|---------|--------|-------|----------------|
| 1 | **Theorem K.1** — Universal Epstein Vanishing | Named | 1 | Cited by any future work on KK UV finiteness |
| 2 | **Theorem K.3** — BPHZ Factorization | Named | 1 | Cited whenever all-orders renormalizability is discussed |
| 3 | **Theorem S.1** — Perturbative Finiteness | Named | 1 | The headline finiteness result |
| 3a | **Theorem V.1** — Two-Loop R³ Vanishing | Named | 1 | The unconditional two-loop Goroff-Sagnotti result; the bridge from conditional (S.1) to unconditional (Paper 10 Thm 1) |
| 3b | **Theorem P.1** — CPT Invariance | Named | 1 | CPT from 5D general covariance; cited whenever CPT or the spin-statistics-CPT nexus is discussed |
| 3c | **Theorem B.1.1** — Half-Integer Winding Classification | Named | 1 | The topological root of the spin-statistics chain: s ∈ (1/2)ℤ from π₁(SO(d)) = ℤ₂ |
| 3d | **Theorem B.2.1** — Exchange Phase Theorem | Named | 1 | The exchange phase e^{i2πs} from e-bundle holonomy; unifies Aharonov-Bohm and Pauli exclusion |
| 3e | **Theorem B.3.3** — Spin-Statistics (geometric form) | Named | 1 | The closing theorem of the B.1 → B.2 → B.3 chain; the geometric spin-statistics theorem |
| 4 | **Corollary 3.1** — Hawking Temperature | Named | 3 | Ties Hawking's result to e-circle spin structure |
| 5 | **Theorem 6.1** → *e-Unitarity Theorem* | **Proposed** | 3 | Central to any quantum gravity discussion of information |
| 6 | **Theorem 9.1** — Horizon Vertex = 1 | Named | 3 | Sharp topological result; cited in quantum gravity |
| 7 | **Theorem 5.2** — SLOCC-Isometry | Named | 4 | Bridges quantum information and gauge theory |
| 8 | **Spectral Gap** → *Theorem 9.2 — Stable Spectral Gap* | **Proposed** | 4 | Feeds the Yang-Mills proof chain; needs a number and name |
| 9 | **Theorem U** | Named | 7 | Cited in any discussion of moduli stabilization |
| 10 | **Theorem U*** | Named | 7 | The sharpest statement about the CC problem ever made |
| 11 | **Corollary 1.1** → *KK Correlation Decay* | **Proposed** | 8 | Internal to the proof chain; functional name helps navigation |
| 12 | **Corollary 4.1** → *String Tension Positivity* | **Proposed** | 8 | Extends the lattice gap to the full KK theory |
| 13 | **Theorem 8** → *Gap Persistence Theorem* | **Proposed** | 8 | The penultimate step in the Millennium proof — will be cited |
| 14 | **Theorem F.1** — Area Law Implies Mass Gap | Named | 8 | Foundational for confinement proofs |
| 15 | **Theorem I.4.1** — Universal Mass Gap | Named | 8 | The Millennium result, extended to all compact simple groups |
| 16 | **Proposition I.4.2** → *Gauge Universality* | **Proposed** | 8 | Complete and proved; pairs with Theorem I.4.1 |

---

## Part 2 — Paper 9 Preprint Content Inventory (Historical Pointers)

*The preprint material is preserved on disk. These pointers record where each
section lives so future readers can find the original text. The canonical
treatments of these topics have migrated — see the header for targets.*

- `paper9/preprint/00-abstract.md` — Framework abstract (superseded by
  `strategy/north-star.md` §0)
- `paper9/preprint/01-the-postulate.md` — The one-postulate statement
- `paper9/preprint/02-the-six-patterns.md` — Six structural patterns
  (now threaded through per-vertex briefs in `strategy/<vertex>/deliverables/`)
- `paper9/preprint/03-the-three-geometries.md` — Three geometries narrative
- `paper9/preprint/04-consequences-not-fits.md` — Why predictions are
  consequences, not parameter fits
- `paper9/preprint/04b-the-mirror-sector-prediction.md` — Mirror sector
  (now in Paper 2 cosmology, Paper 6 thermal history)
- `paper9/preprint/04c-the-5-2-identity.md` — The 5-2 identity narrative
- `paper9/preprint/04d-R-is-the-quantization.md` — R as quantization
- `paper9/preprint/05-how-the-geometry-was-found.md` — Discovery narrative
- `paper9/preprint/06-one-postulate-ten-papers.md` — Series overview
- `paper9/preprint/07-the-open-frontier.md` — Open questions (now in
  `strategy/to-be-done.md`)
- `paper9/preprint/08-appendix-pattern-attribution-map.md` — Pattern ↔ paper map
- `paper9/preprint/09-the-alarm.md` — The alarm narrative

## Part 3 — Paper 9 Research Inventory

- `paper9/research/00-research-index.md` — research index
- `paper9/research/01-number-theoretic-zeta-zeros.md` + prompt
- `paper9/research/02-heat-kernel-seeley-dewitt.md` + prompt
- `paper9/research/03-z2-parity-cancellation.md` + prompt
- `paper9/research/04-poisson-dimreg.md` + prompt
- `paper9/research/05-weyl-anomaly-kk-tower.md` + prompt
- `paper9/research/06-synthesis.md` + prompt

These research memos are the provenance of Paper 10's proof chain
(scheme-independence). Canonical forms live in
`integers/paper10-scheme-independence/research/`.

## Part 4 — Paper 9 etc Inventory

- `paper9/etc/01-cross-paper-referee.md` — cross-paper referee plan
- `paper9/etc/02-full-review-cycle-runbook.md` — review cycle runbook
- `paper9/etc/03-update-and-run-computations.md` — computation runbook
- `paper9/etc/04-tensions-and-resolutions-plan.md` — tensions plan

## Part 5 — Paper 9 Journal-Reviewer Artifacts

- `paper9/journal-reviewer/report.md` — reviewer report
- `paper9/journal-reviewer/gap-responses.md` — gap responses

---

*End of consolidation.*
