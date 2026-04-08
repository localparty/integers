# Prompt — Write Paper 10: Scheme-Independence of UV Finiteness in 5D KK Gravity

**Issued by:** G (principal investigator)  
**Output:** Full paper scaffold in `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/`  
Write one file per section. Use the naming convention:
  `00-abstract.md`, `01-introduction.md`, `02-seeley-dewitt.md`,
  `03-z2-mechanism.md`, `04-poisson-weyl.md`, `05-open-problems.md`

---

## Context

This is Paper 10 in the QG5D series. Papers 1–9 are at:
`/Users/gsix/quantum-geometry-in-5d-latex/`

Paper 1 proves UV finiteness of 5D linearized gravity on M⁴ × S¹/Z₂ via zeta
regularization (Universal Epstein Vanishing theorem, Appendix K). Paper 1 Appendix U
§U.2c honestly states that scheme-independence is not proved.

Five research routes have now explored scheme-independence. Read ALL of these first:

**Synthesis (start here):**
`/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/06-synthesis.md`

**Route memos:**
`/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/01-number-theoretic-zeta-zeros.md`
`/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/02-heat-kernel-seeley-dewitt.md`
`/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/03-z2-parity-cancellation.md`
`/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/04-poisson-dimreg.md`
`/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/05-weyl-anomaly-kk-tower.md`

**Paper 1 Appendix U (the open problem being addressed):**
`/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/32-appendix-u-goroff-sagnotti-verification.md`

**Canonical values (do not contradict):**
- R₀ = 10.1 μm (Casimir constraint with mirror sector)
- ξ = 0.432, m_ν = 49.7 ± 0.5 meV, CMB-S4 test at 5–8σ
- 5/2 identity is a numerical coincidence, not a topological theorem (Paper 7 §B.10.3a)
- k = 2 is a fitted parameter, not derived from geometry

---

## What to write

### `00-abstract.md`
~30 lines. State:
- The question: is the UV finiteness of 5D linearized gravity on M⁴ × S¹/Z₂
  (established in Paper 1 via zeta regularization) scheme-independent?
- The answer: yes, for the one-loop sector, and conditionally for two-loop
- The two proved results (Seeley-DeWitt + Weyl anomaly)
- The three supporting demonstrations (Z₂, Poisson, number-theoretic)
- The one remaining gap (vertex mass-independence)
- Forward: Paper 10 closes the gap

### `01-introduction.md`
~120 lines. Sections:
- §1.1: Why scheme-independence matters — a result proved only in zeta reg is not
  physically unambiguous. The Goroff-Sagnotti counterterm is scheme-independent in 4D;
  its absence in 5D KK gravity should be too.
- §1.2: What Paper 1 established and where it stopped (§U.2c open problem)
- §1.3: Overview of the five routes and their verdicts
- §1.4: Paper outline
- §1.5: Notation (K: compact space = S¹/Z₂; L: Lichnerowicz operator; KK masses m_n = n/R)

### `02-seeley-dewitt.md`
~150 lines. The main proof section.
- §2.1: The Seeley-DeWitt framework — intrinsic spectral invariants, Vassilevich (2003)
- §2.2: The Lichnerowicz operator on flat M⁴ × S¹/Z₂ — symbol, background
- §2.3: Bulk contributions — all curvature polynomials vanish on flat background
- §2.4: Fixed-point (brane) contributions — extrinsic curvature = 0, η = 0, cone angle θ = π
- §2.5: Theorem U.2a (proved): a₂ = a₄ = 0. State cleanly with proof.
- §2.6: Extension to all a_{2k} — argument that flat background forces all to vanish;
  Gel'fand-Yaglom generating function approach (proposed, not yet proved for all k)
- §2.7: Numerical cross-check (cite Route 02 code at paper9/research/code/seeley-dewitt/)

### `03-z2-mechanism.md`
~130 lines. The algebraic mechanism section.
- §3.1: Mode decomposition on S¹/Z₂ — even and odd sectors, their field content
- §3.2: Z₂ parity of the GS three-vertex — sign flip from y-integral
- §3.3: Term-by-term cancellation at each KK level n (no summation needed)
- §3.4: Which regulators this covers — dim-reg, symmetric cutoff, Z₂-paired PV, zeta
- §3.5: The DOF asymmetry gap (5 vs 2 polarizations for even vs odd modes) —
  stated as an open sub-problem
- §3.6: The mixed-sector vertex gap — I_{++-} and I_{-+-} integrals (elementary,
  proposed as next computation)
- §3.7: Relationship to Route 01 (Z₂ parity is why ζ_R(0) = −1/2 enters with
  opposite signs from even and odd towers)

### `04-poisson-weyl.md`
~130 lines. Two complementary routes unified.
- §4.1: The Poisson bridge — from dim-reg to zeta via Poisson resummation
- §4.2: The exchange lemma — conditions and proof sketch (uniform convergence,
  winding mode exponential decay)
- §4.3: The scheme difference — O(e^{−2πRk}), finite, no new divergences
- §4.4: The Weyl anomaly route — mass-independence of a₄ (Vassilevich),
  a_total = (43/360)×S₀ = 0, Wess-Zumino protection
- §4.5: Why the Weyl anomaly covers all loops for the GS operator
- §4.6: Vertex mass-independence: the shared gap between Routes 04 and 05.
  State precisely what needs to be computed and why it is tractable.

### `05-open-problems.md`
~80 lines.
- §5.1: Summary of status (proved / demonstrated / open)
- §5.2: The vertex mass-independence computation — what it is, why it is elementary,
  estimated scope
- §5.3: Extension to all a_{2k} via Gel'fand-Yaglom
- §5.4: Curved backgrounds — the flat-background limitation
- §5.5: Beyond linearized gravity — what changes for the full non-linear theory
- §5.6: Connection to Paper 1 Theorem U (R cannot be derived perturbatively) —
  does scheme-independence affect the CC problem isolation?

---

## Style requirements

- Write at the level of a mathematical physics paper: precise, honest, no overselling
- Every theorem is clearly labelled Theorem/Lemma/Proposition with Proof or Proof sketch
- Every claim that is not yet proved is labelled "Conjecture" or "Proposed"
- Cross-reference Paper 1 sections by name, not just "Paper 1"
- The paper does NOT claim to fully resolve §U.2c — it partially resolves it and says so
- Tone matches Papers 1–9 in the series: formal but readable, with honest limitations

Write all six files now.
