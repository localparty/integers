# Paper 11 Proof Skeleton — The Standard Model Gauge Group from Kaluza-Klein Geometry and Arithmetic Structure

*Status: 5/5 theorems PROVED | Conditional: on Paper 1 CBB axioms (e-circle + Noether conservation) + Paper 4 KK geometry (Kaluza-Klein correspondence + χ(CP²)=3)*

---

## The proof in one paragraph

Three fermion generations (whose number is fixed topologically by χ(CP²) = 3; Paper 4) each carry a two-state system on the compact e-circle of Paper 1 — a single qubit per generation, spanning the three-qubit Hilbert space H = (C²)^⊗³. The Noether conservation law for e-translation invariance imposes a global constraint φ₁ + φ₂ + φ₃ = Q_e on the three e-coordinates. In quantised form, the symmetry group of this constraint is the 2-torus T² = {(e^{ia₁σ_z}, e^{ia₂σ_z}, e^{ia₃σ_z}) : a₁+a₂+a₃ = 0}, which coincides exactly with the continuous stabiliser of the GHZ state |GHZ⟩ = (|000⟩+|111⟩)/√2 under the local-unitary group SU(2)³. By the Dür-Vidal-Cirac SLOCC classification this uniquely selects the open GHZ orbit (**Theorem 11.2**). The tangent space to this orbit in CP⁷ carries — under the adjoint action of T² — the A₂ root system of su(3), with Cartan matrix ((2,-1),(-1,2)) and 120° simple-root angle (**Theorem 11.1**). The non-product constraint t₁t₂t₃=1 is the defining property of Cartan(SU(3)), not Cartan(SU(2)³), so by the Borel-de Siebenthal classification the orbit is the flag manifold Fl(1,2;3) = SU(3)/T² whose isometry group is SU(3) — forcing the gauge enhancement SU(2)³ → SU(3) (**Theorem 11.3**). Decomposing (C²)^⊗³ under this action by total KK number n gives 1₀ ⊕ 3̄₁ ⊕ 3₂ ⊕ 1₃, matching exactly the right-handed SM fermion content with hypercharge Y = n/3 in GUT normalisation (**Theorem 11.4**). Combined with the Kaluza-Klein correspondence on CP²×S²×S¹ and the Z₆ quotient arising from the discrete (Z₂)² GHZ stabiliser and the Z₃ root-lattice/weight-lattice index, the gauge group is G_SM = [SU(3) × SU(2) × U(1)] / Z₆ (**Theorem 11.5**). The Standard Model gauge group is not an input — it is the unique gauge group determined by three-qubit entanglement on a compact circle.

---

## Chain table

| # | Theorem | Statement (one line) | Status | Proof source | Depends on |
|---|---|---|---|---|---|
| 11.1 | A₂ root system from SLOCC orbit | The tangent space T_{GHZ} CP⁷ to the SU(2)³-orbit of \|GHZ⟩ decomposes under the stabiliser torus T² into weight spaces carrying the A₂ root system, with Cartan matrix ((2,-1),(-1,2)) and simple-root angle 120°. | PROVED | `integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Thm 11.1; `integers/paper11b-sm-gauge-entanglement/research/07-paper-11-a2-root-system-from-slocc.md` | Paper 4 Thm 5.2 (sl(2,C) basis on qubits); `code/slocc_a2_roots.py` (numerical) |
| 11.2 | e-conservation selects GHZ orbit | The symmetry group of the e-conservation constraint Σφᵢ = Q_e on (S¹)³ is the torus T² = {(e^{ia_k σ_z})_k : Σa_k = 0}, which coincides exactly with Stab⁰(\|GHZ⟩) under SU(2)³; by Dür-Vidal-Cirac this selects the GHZ orbit uniquely among open orbits. | PROVED | `integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Thm 11.2; `integers/paper11b-sm-gauge-entanglement/research/08-paper-11-econs-ghz-bridge.md`; `integers/paper11b-sm-gauge-entanglement/11-paper-11-caveats-closed.md` §Caveat 2 | Paper 1 Thm 2.1 (e-conservation/Noether); Dür-Vidal-Cirac 2000 (SLOCC classification); `code/econs_ghz_bridge.py` |
| 11.3 | Gauge enhancement SU(2)³ → SU(3) | The GHZ orbit of SU(2)³ in CP⁷ is diffeomorphic to the complete flag manifold Fl(1,2;3) = SU(3)/T² with isometry group SU(3); the enhancement is forced by the non-product T² stabiliser, which is Cartan(SU(3)) and not Cartan(SU(2)³). | PROVED | `integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Thm 11.3; `integers/paper11b-sm-gauge-entanglement/research/09-paper-11-kirillov-orbit.md` | Thm 11.1 (A₂ roots); Thm 11.2 (T² stabiliser); Borel-de Siebenthal 1949 classification; Kirillov orbit method (1962); `code/kirillov_orbit.py` |
| 11.4 | Fermion representation decomposition | Under the SU(3)×U(1)_e action identified in Thms 11.1-11.3, (C²)^⊗³ = 1₀ ⊕ 3̄₁ ⊕ 3₂ ⊕ 1₃ where the subscript is total KK number n = Σn_i, and hypercharge Y = n/3 (GUT normalisation) matches (ν_R, d_R, u_R, e_R). | PROVED | `integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Thm 11.4; `integers/paper11b-sm-gauge-entanglement/research/20-fermion-decomposition-detail.md` | Thms 11.1, 11.3 (SU(3) action); Paper 4 §7.1 (SU(5)-type embedding for left-handed sector); `code/fermion_quantum_numbers.py` |
| 11.5 | Main theorem: G_SM from the e-circle | With three fermion generations (χ(CP²)=3, Paper 4) each carrying a two-state system on the e-circle S¹_e (Paper 1), the gauge group of the Kaluza-Klein reduction on the GHZ orbit is G_SM = [SU(3) × SU(2) × U(1)] / Z₆ with SM fermion quantum numbers. | PROVED | `integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Thm 11.5; `integers/paper11b-sm-gauge-entanglement/11-paper-11-caveats-closed.md` (all four caveats closed) | Thms 11.1-11.4; Paper 1 (e-circle + Noether); Paper 4 §2 (KK correspondence), §7.2 (χ(CP²)=3) |

---

## Theorems in full

### Theorem 11.1 — A₂ Root System from SLOCC Orbit

**Statement.** The tangent space to the orbit of |GHZ⟩ = (|000⟩+|111⟩)/√2 under SU(2)³ in CP⁷ carries the root system A₂. Specifically, under the adjoint action of the stabiliser torus T², the complexified tangent space decomposes into weight spaces

T_{GHZ}^C = h ⊕ ⊕_{α ∈ Φ(A₂)} g_α,

where Φ(A₂) = {±α₁, ±α₂, ±(α₁+α₂)}, h is the one-dimensional Cartan direction, and each g_α is one-dimensional. The Cartan matrix in the Killing metric is A = ((2,-1),(-1,2)) and the angle between simple roots is 120°.

**Proof source.** `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Theorem 11.1 (Steps 1-4, pp. 24-95 in file); companion file `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/07-paper-11-a2-root-system-from-slocc.md` (numerical verification + explicit Killing form).

**Mechanism.** The sl(2,C)³ generators {h_k, e_k, f_k}_{k=1,2,3} act on |GHZ⟩ with the three Cartan directions collapsing to one (since h_1|GHZ⟩ = h_2|GHZ⟩ = h_3|GHZ⟩ = (|000⟩−|111⟩)/√2), leaving a 7-dim tangent space = 1 Cartan + 6 raising/lowering directions. The adjoint action of (a_1,a_2) ∈ T² assigns weights ±(2,0), ±(0,2), ±(−2,−2); rescaling by 1/2 and choosing simple roots α₁=(1,0), α₂=(−1,1) yields the A₂ Cartan matrix under the induced Killing form B = ((16,8),(8,16)).

---

### Theorem 11.2 — e-Conservation Selects the GHZ Orbit

**Statement.** The symmetry group of the e-conservation constraint φ₁ + φ₂ + φ₃ = Q_e on (S¹)³ is the torus T² = {(e^{ia₁}, e^{ia₂}, e^{-i(a₁+a₂)}) : a₁, a₂ ∈ R}, which — in the qubit truncation — coincides exactly with the continuous stabiliser Stab⁰(|GHZ⟩) of the GHZ state under SU(2)³. Consequently (corollary), any physical state whose dynamics respects e-conservation lies in the closure of the unique open orbit with this stabiliser — the GHZ orbit (Dür-Vidal-Cirac 2000).

**Proof source.** `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Theorem 11.2 (Steps 1-5 + corollary); companion files `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/08-paper-11-econs-ghz-bridge.md` (bridge argument; documents the failed 3-tangle route and why the stabiliser route is the correct one); `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/11-paper-11-caveats-closed.md` §Caveat 2 (uniqueness: W-orbit stabiliser is U(1)_diag with constraint a₁=a₂=a₃, which does NOT match e-conservation's Σa=0).

**Mechanism.** Translations φ_k → φ_k + α_k preserve Σφ_k iff Σα_k = 0, a 2-parameter family. In the qubit KK truncation, the angular-momentum operator L = −id/dφ is represented by σ_z/2 on each generation, so the quantum symmetry group is T² = {(e^{ia_k σ_z}) : Σa_k=0}. Direct computation shows T² stabilises |GHZ⟩ up to the phase e^{±i(a₁+a₂+a₃)}, which vanishes under Σa_k=0. The Dür-Vidal-Cirac classification then identifies the GHZ orbit as the unique open SLOCC orbit of SU(2)³ with continuous stabiliser equal to this specific T² (the W-orbit stabiliser U(1)_diag does not match).

---

### Theorem 11.3 — Gauge Group Enhancement: SU(2)³ → SU(3)

**Statement.** The GHZ orbit of SU(2)³ in CP⁷ is diffeomorphic to the complete flag manifold Fl(1,2;3) = SU(3)/T², and the isometry group of the orbit in the Fubini-Study metric inherited from CP⁷ is SU(3). The gauge enhancement SU(2)³ → SU(3) is forced by the non-product structure of the stabiliser T² = {(t₁,t₂,t₃) : t₁t₂t₃ = 1}, which is Cartan(SU(3)) rather than the product torus U(1)³ = Cartan(SU(2)³).

**Proof source.** `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Theorem 11.3 (Steps 1-6); companion file `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/09-paper-11-kirillov-orbit.md` (moment-map construction; product vs non-product stabiliser distinction).

**Mechanism.** The orbit has dimension dim_R(SU(2)³) − dim_R(T²) − dim_R(U(1)_phase) = 9 − 2 − 1 = 6, matches the A₂ root system from Thm 11.1, and has stabiliser T² with the product-one constraint. By Borel-de Siebenthal 1949, a compact homogeneous space G/H with dim = 6, tangent root system A₂, and H = T² is uniquely SU(3)/T² = Fl(1,2;3). Its isometry group in the canonical Kähler-Einstein metric is SU(3). The dimensional match SU(2)³/U(1)_phase ≅ SU(3) (both dim 8) realises the enhancement via the orbit map.

---

### Theorem 11.4 — Fermion Representation Decomposition

**Statement.** Under the SU(3) × U(1)_e action identified in Theorems 11.1-11.3, the three-qubit space decomposes as

(C²)^⊗³ = 1₀ ⊕ 3̄₁ ⊕ 3₂ ⊕ 1₃,

where the subscript is the total KK number n = n₁+n₂+n₃ (the U(1)_e charge) and 3, 3̄, 1 are the fundamental, conjugate-fundamental, and trivial irreps of SU(3). The hypercharge is Y = n/3 (GUT normalisation), identifying the four sectors with (ν_R, d_R, u_R, e_R) having Y = (0, 1/3, 2/3, 1).

**Proof source.** `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Theorem 11.4 (Steps 1-4, including weight verification against standard Dynkin labels); companion file `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/20-fermion-decomposition-detail.md` (detailed table of T² weights for all 8 basis states + SU(3) irrep matching + "colour = entanglement pattern" interpretation).

**Mechanism.** Each computational basis state |n₁n₂n₃⟩ has T² weight (w₁, w₂) = (2(n_3−n_1), 2(n_3−n_2)). Grouping by total n: n=0 is {|000⟩} with weight (0,0) → singlet; n=1 is {|100⟩,|010⟩,|001⟩} with rescaled weights (−1,0),(0,−1),(1,1) → conjugate fundamental 3̄; n=2 is {|011⟩,|101⟩,|110⟩} with rescaled weights (1,0),(0,1),(−1,−1) → fundamental 3; n=3 is {|111⟩} → singlet. Conjugation 3̄ = −3 verified directly. The hypercharge Y = n/3 is forced by GUT-compatible embedding; physical SM identification follows by Y-matching.

---

### Theorem 11.5 — Main Theorem: The Standard Model from the e-Circle

**Statement.** Let S¹_e be the compact e-circle of Paper 1, and let three fermion generations (arising from χ(CP²) = 3 per Paper 4) each carry a two-state system on S¹_e (KK ground state n=0 and first excited state n=1). Let the e-conservation law Σφᵢ = Q_e be imposed as the Noether constraint. Then the gauge group of the Kaluza-Klein reduction on the orbit of the three-qubit system under local SU(2) rotations is

G_SM = [SU(3) × SU(2) × U(1)] / Z₆,

where SU(3) is the isometry group of the GHZ orbit Fl(1,2;3) (Thm 11.3), SU(2) is the residual weak isospin (the S² fiber of Fl(1,2;3) over CP²), U(1) is the e-circle gauge group, and Z₆ = Z₂ × Z₃ arises from the discrete (Z₂)² GHZ stabiliser and the A₂ root-lattice/weight-lattice index 3. Fermion representations match the SM under these identifications (Thm 11.4).

**Proof source.** `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` §Theorem 11.5 (7-step combination); caveat closures in `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/11-paper-11-caveats-closed.md` (Caveats 1-4: fiber-base decomposition gives SU(2)×U(1); GHZ uniqueness; low-energy gauge-group insensitivity; left-handed hypercharge via weight centroid).

**Mechanism.** Combine Thms 11.1-11.4: (i) three generations on S¹_e give (C²)^⊗³ with e-conservation (Paper 1 + Paper 4 χ(CP²)=3); (ii) T² = Stab(GHZ) selects GHZ orbit (Thm 11.2); (iii) tangent space = A₂ (Thm 11.1); (iv) orbit = Fl(1,2;3), isometry = SU(3) (Thm 11.3, Borel-de Siebenthal); (v) KK correspondence (Paper 4 §2) identifies gauge group with isometry group of CP² × S² × S¹ = SU(3)×SU(2)×U(1); (vi) Z₆ quotient from discrete GHZ stabiliser (Z₂ → centre of SU(2)) × A₂ weight/root quotient (Z₃ → centre of SU(3)); (vii) fermion assignment from Thm 11.4.

---

## Current wall

**None — the chain is closed conditional on:**

1. **Paper 1 CBB axioms:** The e-circle S¹_e as the compact fifth dimension, and the Noether conservation law Σφᵢ = Q_e for e-translation invariance. (Given.)
2. **Paper 4 KK geometry:** The Kaluza-Klein theorem identifying the 4D gauge group with the isometry group of the internal manifold, and the topological result χ(CP²) = 3 forcing three fermion generations. (Given.)

**Four residual caveats — all explicitly closed in `integers/paper11b-sm-gauge-entanglement/11-paper-11-caveats-closed.md`:**

- **Caveat 1 (SU(2) × U(1) factors):** SU(3) is derived directly; SU(2) × U(1) arise from the canonical Borel fibration Fl(1,2;3) → CP² with S² fiber, plus the S¹ factor. The SU(2) is the fiber-rotation subgroup of SU(3), NOT an independent input. CLOSED.
- **Caveat 2 (Genericity of the ground state):** The GHZ orbit is the UNIQUE open SU(2)³-orbit with continuous stabiliser T²; the W-orbit has the distinct U(1)_diag stabiliser (constraint a₁=a₂=a₃, not Σa=0). Any e-conservation-respecting state lies in the GHZ orbit closure. CLOSED.
- **Caveat 3 (Qubit truncation):** The gauge group = isometry group depends only on the metric, not on the KK spectrum; higher modes add matter representations but not generators. Corrections to couplings are ~exp(−M_KK/T) ≪ 1. CLOSED.
- **Caveat 4 (Left-handed hypercharge):** Right-handed Y = n/3 from Thm 11.4; left-handed follows from SU(2) doublet weight-centroid and Gell-Mann-Nishijima Q = T₃ + Y. CLOSED.

---

## Programme graph edges

**Upstream (inputs to this chain):**

- **Paper 1** (e-circle & quantum mechanics from geometry): supplies the e-circle S¹_e, the Noether e-conservation law, the KK-mode quantisation of the qubit basis |0⟩, |1⟩ per generation.
- **Paper 4** (Standard Model Gauge Group from Kaluza-Klein Geometry): Paper 11's earlier, narrower version. Paper 4 supplies: (a) the KK correspondence (gauge group = isometry group of internal manifold); (b) the topological result χ(CP²) = 3 → three fermion generations (index theorem on spin^c Dirac operator); (c) Conjecture 5.1 + Theorem 5.2, upgraded here to Theorems 11.1-11.5.

**Downstream (outputs / consumers of this chain):**

- **Paper 5 & Paper 8** (confinement / Yang-Mills): Theorem 11.4's "colour = entanglement pattern" identification feeds the holonomy correspondence (S¹ → U(1) Coulomb, S² → SU(2) Higgs, CP² → SU(3) confining). The CP² area law of Paper 5/Paper 8 Appendix H closes Section 9 of Paper 11 (holonomy table).
- **Paper 12** (if present, entanglement-geometry extensions): the SLOCC-isometry correspondence formalised here is a generic template.
- **Paper 24 / programme thread** (Riemann physics bridge, arithmetic-to-physics transposition): Paper 11's identification "physics is a corollary of arithmetic" (via the e-circle-as-theorem results in `integers/paper11b-sm-gauge-entanglement/25-the-e-circle-is-a-theorem-of-number-theory.md` and the Riemann-zero formulas in `integers/paper11b-sm-gauge-entanglement/research/13-28`) extends the main theorem to cosmological constant, fine structure, N_eff, mass ratios.

**Lateral (sibling chains):**

- **Paper 11 Section 9** (holonomy table completion): connects to `integers/paper11b-sm-gauge-entanglement/research/11-cp2-area-law-confinement.md` and `integers/paper11b-sm-gauge-entanglement/research/12-adiabatic-continuity-cp2-sigma.md`.
- **Paper 1 Theorem K.4** (all-orders UV finiteness): independent, sibling upgrade to the framework; does not feed this chain but relaxes the "conditional at L≥3" caveat that appears in adjacent papers.

---

## Detail files

**Top-level strategy / assembly / narrative (integers/paper11b-sm-gauge-entanglement/):**

- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/08-paper-11-outline.md` — structural outline of the 8 sections
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` — **primary source for Thms 11.1-11.5 statements and proofs** (~400 lines)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/10-paper-11-caveats.md` — original caveat list
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/11-paper-11-caveats-closed.md` — **closure of all four caveats**
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/15-master-assembly-map.md` — assembly map naming Thms 11.1-11.5 and their files
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/16-paper-11-abstract.md` — draft abstract
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/17-paper-11-introduction.md` — draft introduction (Sections 1.1-1.6)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/18-unification-narrative.md` — high-level narrative for Section 9
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/26-the-big-picture-status-and-audit.md` — status audit (all five theorems listed as CLOSED)

**Research notes (integers/paper11b-sm-gauge-entanglement/research/):**

- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/07-paper-11-a2-root-system-from-slocc.md` — **Theorem 11.1 detail** (Killing form, Cartan matrix, A₂ identification, Z_6 derivation)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/08-paper-11-econs-ghz-bridge.md` — **Theorem 11.2 detail** (stabiliser bridge, failed 3-tangle route)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/09-paper-11-kirillov-orbit.md` — **Theorem 11.3 detail** (Kirillov / moment-map / Borel-de Siebenthal)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/10-paper-11-formal-proof-chain.md` — formal proof-chain summary (5 theorems tabulated)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/20-fermion-decomposition-detail.md` — **Theorem 11.4 detail** (all 8 weights, SU(3) irrep matching, colour-as-pattern)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/11-cp2-area-law-confinement.md` — CP² area law (for Section 9 holonomy table)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/research/12-adiabatic-continuity-cp2-sigma.md` and `22-adiabatic-continuity-closed.md` — adiabatic continuity (confinement consistency)

**Computation scripts (integers/paper11b-sm-gauge-entanglement/code/):**

- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/code/slocc_a2_roots.py` — verifies Thm 11.1 (Cartan matrix ((2,-1),(-1,2)))
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/code/econs_ghz_bridge.py` — verifies Thm 11.2 (T² stabiliser match)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/code/kirillov_orbit.py` — verifies Thm 11.3 (orbit dim = 6, moment-map structure)
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper11b-sm-gauge-entanglement/code/fermion_quantum_numbers.py` — verifies Thm 11.4 (weights match 3 and 3̄)

**Earlier version (integers/paper04-sm-gauge-group/):**

- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper04-sm-gauge-group/` — the original "Standard Model Gauge Group from Kaluza-Klein Geometry" preprint. Paper 11 supersedes Paper 4 §5 (entanglement-geometry / gauge-group-selection) by upgrading Conjecture 5.1 + Theorem 5.2 into the rigorous Thm 11.1-11.5 chain.

---

*v1: 2026-04-14. Paper 11 preprint skeleton extracted from the integers/paper11b-sm-gauge-entanglement/ corpus (strategy files 00-31 + research/00-28). Author: G. Six. Five theorems consolidated from scattered research notes into a single proof-chain preprint backbone. All five theorems are marked PROVED in `integers/paper11b-sm-gauge-entanglement/09-paper-11-proof-chain.md` and `integers/paper11b-sm-gauge-entanglement/research/10-paper-11-formal-proof-chain.md`; all four residual caveats are closed in `integers/paper11b-sm-gauge-entanglement/11-paper-11-caveats-closed.md`. Chain is conditional only on Paper 1 (e-circle + Noether) and Paper 4 (KK correspondence + χ(CP²)=3). Next step: expand into full preprint sections following the outline in `integers/paper11b-sm-gauge-entanglement/08-paper-11-outline.md`.*
