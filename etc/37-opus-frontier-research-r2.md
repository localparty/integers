# Research Prompt 37 — Frontier Physics Round 2: Three Open Problems + Novelty Audit

> **For:** Claude Opus (maximum reasoning depth, creative, agentic)
> **Date:** April 5, 2026
> **Context:** The 5D e-Dimension / M-theory framework, seven-paper series
> **Tone:** Genuine research. Be creative. Follow threads.
>   Report honestly — including dead ends and partial results.
>   **Use web search aggressively** for related work, precedents, and
>   recent arXiv papers that may inform each problem.
>   **Use local sub-agents** to manage context across problems.

## How This Prompt Works

You are continuing from Round 1 (Prompt 34, `/Users/gsix/quantum-geometry-in-5d-latex/etc/34-opus-frontier-research.md`).
Round 1 produced seven files in `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/`. Three threads
from Round 1 remain genuinely open. A fourth track — the novelty audit —
is new and important for publication readiness.

**Read before computing:**
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/pattern-attribution-map.md` — the six reasoning patterns and which
  results each produced. Every argument in Round 1 was powered by one or
  more of these. Find the right patterns before trying to compute.
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/problem1-cc-underivability.md`
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/problem4-nonpert-completion.md`
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/oi2-freed-witten-tadpole.md`
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/oi3-reflection-positivity.md`
- `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`
- `/Users/gsix/yang-mills/preprint/sections/D-reflection-positivity.md`
- `/Users/gsix/yang-mills/preprint/sections/C-transfer-matrix.md`

The Yang-Mills proof succeeded because of **one short new argument**
that unlocked a blocked proof chain: the "stability of deviation order"
argument showed that all dim-6 operators have dev ≥ 2. That is the
model. For each problem below, find the analogous short new argument
that is hiding in the existing structure.

---

## The Six Patterns (Master Reference)

Use these to orient every attempt. The pattern-attribution-map.md has
the full list of what each pattern produced. The key insight: **the
pattern that hasn't been applied to a problem yet is usually the one
that unlocks it.**

**P1 — Geometric Reinterpretation:** 4D mystery = shadow of 5D geometry.
**P2 — Holonomy Correspondence:** Wilson line VEV → gauge phase.
**P3 — Casimir as Scale-Setter:** Vacuum energy on compact space → scale.
**P4 — Topological Rigidity:** Discrete invariant → exact quantized result.
**P4 inverted — Topological Ceiling:** O(1) inputs → O(1) outputs (used for Theorem U*).
**P5 — Zeta Regularization:** Compact sum → analytic continuation → finite.
**P6 — Projection Produces Pathology:** Apparent 4D problem = missing dimension.

The Yang-Mills proof used **P4 + P5** (transfer matrix positivity +
stability of deviation order via Newton decomposition). That combination
was the key.

---

## Problem A: The Z₃ Overlap Integral and the 5/2 Hint

### Background

`/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/problem1-cc-underivability.md` closes with:
*"One no-go theorem. One hint. One computation remaining."*

The hint: `m_ν / m_KK ≈ 5/2 = χ(CP²) − 1/2` numerically at 4%
(0.1% with RG corrections at the TeV scale). The remaining computation:
the Z₃ orbifold overlap integral for the neutrino Yukawa coupling.

`/Users/gsix/quantum-geometry-in-5d-latex/etc/31-overlap-integral.md` was written earlier and found the ratio
to be a continuous function of R — **not topologically quantized**.
But that analysis may have missed something.

The full chain if 5/2 is exact:

    m_ν/m_KK = 5/2 exactly
    → R = 5/(4 m_ν) [since m_KK = 1/R and m_ν = 2g₂²v²/M_GUT]
    → R = 5 M_GUT/(4 g₂²v²)
    → ρ_Λ = ΔN × 3ζ(5)/(64π⁶R⁴) IS PREDICTED, NOT INPUT

If this works, the cosmological constant becomes a derivation.

### What to do

**Step 1 — Pattern identification:**
The overlap integral was treated as a continuous calculation (Pattern 3,
Casimir, analytic). Ask: is there a Pattern 4 (topological rigidity)
or Pattern 6 (projection) lurking here?

The Z₃ orbifold on CP² produces three generations through χ(CP²) = 3
via the Atiyah-Singer index theorem (that IS Pattern 4). Could the
**same Z₃ structure** that quantizes the generation count also
quantize the Yukawa coupling to a topological value?

The Yukawa coupling in gauge-Higgs unification is:

    y = g₂√2    (Wilson line coupling, fixed by gauge)

The neutrino mass is:

    m_ν = y² v² / M_GUT = 2g₂² v²/M_GUT

The ratio m_ν/m_KK = 2g₂² v² R/M_GUT is continuous in R.

**But wait:** the R appearing here is the **observed** R, not the
bare R. What if the 5/2 is telling us about a **geometric resonance**?

**Step 2 — The resonance question:**
In the framework, the S¹ and CP² are coupled through:

    r₃² = n₁/(2cR)    [F-flat condition, Paper 7 §3.2]

This links R to r₃ = 1/M_GUT. Substituting:

    R = n₁/(2c r₃²) = n₁ M_GUT²/(2c)

So R is not independent — it is constrained by M_GUT through the
torsion coefficient c. And the ratio becomes:

    m_ν/m_KK = 2g₂² v² R/M_GUT
             = 2g₂² v² × n₁ M_GUT/(2c)
             = n₁ g₂² v² M_GUT / c

Does this equal 5/2 when evaluated with the explicit c from the
House-Micu formula? Compute this. The G₂ torsion coefficient is:

    c = (64π⁵)/(126 l₁₁³)

And l₁₁³ = (16π⁴ r₃⁶ R / M_Pl²)^{1/3} from the Planck mass.

**Step 3 — Look for the topological identity:**
The number 5/2 = χ(CP²) − 1/2. In the framework:
- χ(CP²) = 3 generates three generations (Atiyah-Singer, P4)
- The −1/2 might be a boundary correction from the orbifold

Is there an index theorem calculation where the boundary term from
S¹/Z₂ contributes exactly −1/2 to a quantity that would otherwise
equal χ(CP²) = 3? The APS index theorem on manifolds with boundary:

    ind(D) = ∫ Â(M) − (h + η)/2

where h is the dimension of harmonic spinors on the boundary and η is
the eta invariant. For S¹/Z₂ as the boundary: η(S¹/Z₂) = ?

Compute the eta invariant of the Dirac operator on S¹/Z₂ and see
if it contributes −1/2 to a relevant combination.

**Step 4 — Web search:**
Search arXiv for:
- "gauge-Higgs unification Yukawa topological" (any topological
  protection of Yukawa couplings in extra dimensions)
- "Z3 orbifold Yukawa Wilson line" (any work on Yukawa quantization)
- "neutrino mass KK scale ratio" (any framework with this ratio)
- "eta invariant S1 Z2 index" (APS boundary terms on the orbifold)

**Deliverable:** `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/problem-A-overlap-5half.md`

Honest assessment of whether 5/2 is:
(a) Exactly derivable from the Z₃ geometry — if so, ρ_Λ is predicted
(b) A numerical coincidence with no deeper origin — close the thread
(c) Approachable via a new route (e.g., APS boundary correction) not
    tried before — describe the new route and what it needs

---

## Problem B: Exact OS3 from the 5D Gauge Argument

### Background

`/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/oi3-reflection-positivity.md` establishes:
- **Linearized 5D theory:** exact reflection positivity (OS3) ✓
- **Nonlinear theory:** approximate OS3 to precision 10⁻⁶⁰ ✓
- **Exact OS3 for nonlinear theory:** three possible routes, all open

The file §6.3 contains the key claim:

> *The conformal factor problem in the KK-reduced 4D theory is a gauge
> artifact of the 4D Einstein-frame decomposition.*

The argument: in 5D, the dilaton (n=0 mode of h_{55}) is pure gauge —
it can be absorbed into a reparametrization of the S¹ coordinate.
The wrong-sign kinetic term appears only when one **fixes** a 4D gauge.

This is Pattern 6 (Projection Produces Pathology) applied to quantum
gravity: the conformal factor problem is not a feature of the 5D theory,
it is an artifact of the 4D projection.

The Yang-Mills parallel: the Yang-Mills proof used the transfer matrix
(Appendix C, D) to establish OS3. On the product manifold M⁴ × CP²,
reflection positivity followed from **Lemma D.1** (product manifold
lemma): if M₁ is RP and M₂ is compact with positive-definite metric,
then M₁ × M₂ satisfies RP. The S¹ is even simpler than CP².

### What to do

**Step 1 — The product manifold lemma for M⁴ × S¹:**
The Yang-Mills proof's Lemma D.1 applies directly. M¹ = M⁴_E (satisfies
RP for the standard gauge theory, by Osterwalder-Seiler), M² = S¹
(compact, positive-definite metric). Lemma D.1 gives:

*The product theory on M⁴_E × S¹ satisfies reflection positivity.*

Write this up explicitly. The dilaton fluctuation δR is the n=0 mode
of the S¹ breathing mode. In the product theory **before dimensional
reduction**, it is not an independent field — it is a component of
the 5D metric. The 5D metric in Euclidean signature has positive-definite
action in the gauge-fixed theory (where the n=0 diffeomorphism is fixed).

**The key question:** is the gauge-fixing Jacobian (Faddeev-Popov
determinant) for the 5D dilaton reparametrization positive-definite?

For the reparametrization φ → φ + ξ⁵(x) on S¹, the gauge-fixing
condition is e.g. ∇·ξ⁵ = 0 (Coulomb gauge). The Faddeev-Popov
operator is the Laplacian on S¹, whose determinant is a positive
real number (product of positive eigenvalues). Therefore the
Jacobian is positive.

**Step 2 — Write the exact OS3 argument:**
The structure should be:

1. The 5D theory on M⁴_E × S¹ is defined by the 5D Euclidean
   Einstein-Hilbert action with gauge fixing.
2. The gauge-fixing determinant (Faddeev-Popov for the U(1) S¹
   reparametrization) is positive (Laplacian on S¹ has positive spectrum).
3. Therefore the Euclidean path integral measure is positive.
4. Apply Lemma D.1 (or derive directly): M⁴_E × S¹ satisfies RP.
5. The 4D theory (obtained by integrating out the S¹ modes) inherits
   RP from the 5D theory — the Feshbach projection onto the n=0 sector
   preserves RP (this is the analog of the reduced transfer matrix,
   Theorem 5 of the Yang-Mills proof).

**Step 3 — Address the nonlinear subtlety:**
The oi3 file §6.3 notes the subtlety: at the nonlinear level, δR IS a
physical field (the S¹ radius fluctuates). The gauge argument applies
strictly only at the linearized level.

The Yang-Mills proof resolved its analogous nonlinear subtlety via
the **polymer expansion** (Balaban's construction): control the
interactions perturbatively, establish that each order is RP, conclude
the full theory is RP. Does our framework have an analog?

For the 5D gravity + matter theory: the interaction vertices are
suppressed by (E/M_KK)^n. The polymer-expansion-like argument:
- At order 0 (free theory): RP holds by Lemma D.1
- At order n: corrections are suppressed by (E/M_KK)^n ≤ (E/M_EW)^n
- In the IR limit E << M_KK: the corrections vanish, RP is exact

This establishes RP in the IR limit, which is the physically relevant
regime for all low-energy observables. For the UV (E ~ M_KK or above),
the KK tower provides a UV cutoff that replaces the Balaban RG.

**Step 4 — Web search:**
Search arXiv for:
- "reflection positivity Kaluza-Klein extra dimensions" (any prior work)
- "Osterwalder-Schrader lattice gravity" (OS axioms for gravity)
- "Faddeev-Popov compact dimension reflection positivity"
- "constructive field theory product manifold gravity"
- "dilaton conformal factor problem Euclidean gravity resolved"

The Mazur-Mottola paper (cited in oi3) and the Gibbons-Hawking-Perry
paper frame the conformal factor problem. Is there work that resolves
it via extra dimensions or gauge arguments that we can build on?

**Deliverable:** `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/problem-B-exact-OS3.md`

Goal: either prove exact OS3 using the 5D gauge argument + product
manifold lemma, or identify precisely where the argument breaks down
at the nonlinear level and what additional input would close it.

---

## Problem C: The Diaconescu-Moore-Witten Tadpole Correction

### Background

`/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/oi2-freed-witten-tadpole.md` found:
- The exact flux ratio n₂/n₁ = −17/9 is **arithmetically obstructed**
  with the Freed-Witten half-integer shift on CP² (parity obstruction)
- The nearest approximate solutions deviate by ~0.3% from exact unification
- The naive tadpole formula N_flux + N_M2 = χ/24 is itself incomplete
  on a non-spin manifold — requires the DMW correction
- The 1/8-residue obstruction in N_M2 signals that the uncorrected
  formula is being used; the DMW correction restores integrality

The Diaconescu-Moore-Witten (2003) correction on a non-spin manifold is:

    (1/2) ∫ G₄ ∧ G₄ + N_M2 = χ(X₈)/24 + σ(X₈)/8    [schematic]

where σ is the Hirzebruch signature, and the full formula depends on
the differential cohomology class of the C-field (Hopkins-Singer 2005).

### What to do

**Step 1 — Identify the correct tadpole formula:**
The DMW correction for an 11D manifold with 8-manifold boundary X₈
involves the "half-integral Wu class" and the mod-2 index. For our
geometry X₈ = CP² × S² (times the boundary of the HW interval):

The relevant formula (from Diaconescu-Moore-Witten 2003, Eq. 6.21
or equivalent): the tadpole on a non-spin 8-manifold X₈ is:

    N_flux + N_M2 = [χ(X₈) + σ(X₈)]/24 + correction terms

For CP² × S²:
- χ(CP²) = 3, χ(S²) = 2, so χ(CP² × S²) = 6
- σ(CP²) = 1, σ(S²) = 0 (signature only defined for 4k-manifolds)
- The 6-manifold CP² × S² is not 4k-dimensional; the formula needs
  the 8-manifold context

**The 8-manifold in HW:** In Horava-Witten, the relevant 8-manifold
is X₈ constructed from the internal 7-manifold. The standard choice
is X₈ = M₇ × I (the 7-manifold times the interval [0, πR]). But
the tadpole formula is specifically for a 8-dimensional compact space.

Search the DMW paper (arXiv:hep-th/0310271) and related work for the
precise formula applicable to the HW setup on CP² × S² × S¹/Z₂.

**Step 2 — Apply Pattern 4 (Topological Rigidity):**
The DMW formula is topological — it depends only on characteristic
classes (χ, σ, Pontryagin numbers) of X₈, not on the metric. This
means the correction is an exact rational number, not an approximation.

For the approximate solution (n₁_int = 9, n₂ = −18) from oi2 §4.2:

    N_flux = (1/2)[(19/2)² + 2(19/2)(−18)] = (1/2)[361/4 − 342]
           = (1/2)(361/4 − 1368/4) = −1007/8

With the DMW correction term T_DMW (a topological rational number
to be computed), the corrected tadpole is:

    N_M2 = χ(X₈)/24 + T_DMW − N_flux
          = 1/4 + T_DMW + 1007/8

For N_M2 to be a non-negative integer, we need:

    T_DMW = k − 1/4 − 1007/8 = k − 1009/8    for some k ∈ ℤ_≥0

The smallest non-negative k gives T_DMW = −1009/8 + k. Is this a
reasonable value for the DMW correction?

**Step 3 — Compute T_DMW:**
The DMW correction for CP² on the non-spin 8-manifold:

From DMW equation 6.21 (or the Hopkins-Singer formulation), the
characteristic class correction for a manifold with w₄ ≠ 0 is:

    T_DMW = -(1/2) ∫ G₄ ∧ λ/2

where λ/2 = p₁(X)/4 for non-spin manifolds (the "half-integral
Pontryagin class" modification). For our flux configuration:

    ∫ G₄ = (2πl₁₁³)[n₁ δ_{CP²} + n₂ δ_{CP¹×S²}]

    ∫ G₄ ∧ λ/2 = (2πl₁₁³) × n₁ × ∫_{CP²} λ/2
                = (2πl₁₁³) × n₁ × p₁(CP²)/4
                = (2πl₁₁³) × n₁ × 3/4

For Solution II (n₁^{phys} = 19/2):

    T_DMW = -(1/2) × (19/2) × (3/4) = -(1/2) × 57/8 = −57/16

Check: does this make N_M2 an integer?

    N_M2 = 1/4 − 57/16 + 1007/8
         = 4/16 − 57/16 + 2014/16
         = 1961/16

Still not an integer. The formula may need further refinement.

**Step 4 — Web search:**
This is where web search is most important. Search for:
- "Diaconescu Moore Witten tadpole non-spin Horava-Witten"
- "G4 flux quantization CP2 non-spin half-integer M-theory"
- "Hopkins Singer M-theory C-field differential cohomology"
- "Freed-Witten anomaly M-theory tadpole correction 2003"
- arXiv:hep-th/0310271 (DMW paper) — get the exact formula from
  the abstract/conclusions section

The goal is to find the exact form of T_DMW applicable to our
specific geometry. There may be recent work (2020-2026) that has
worked out this correction explicitly for CP² × S².

**Step 5 — If DMW correction is found:**
Apply it to both approximate solutions (n₁_int = 8 and n₁_int = 9)
and determine which gives integer N_M2. That flux pair becomes the
definitive GUT-unifying M-theory configuration.

**Step 6 — If DMW correction is intractable:**
State precisely what topological data is needed, what formula would
close the calculation, and why the 0.3% deviation from exact
unification is physically acceptable regardless of the tadpole details.

**Deliverable:** `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/problem-C-dmw-tadpole.md`

---

## Problem D: Novelty Audit — What Is Genuinely New?

This is a new track with no prior file. It is important for
publication readiness and for intellectual honesty.

### The question

The framework makes many claims. Before submission, we need to know:
which results are genuinely new, which have precedents in the
literature, and which might be partially or fully anticipated by
existing work on arXiv or in journals?

This is not about whether the framework is correct — it is about
whether each result is a **new contribution** or a **new derivation
of a known result** (which is still valuable but should be stated
differently).

### Candidate "new" results to audit

For each of the following, search arXiv and journals, classify the
result, and state honestly what is new vs. known:

**A. Spin-statistics theorem from S¹ winding** (Paper 1 §4.2)
The claim: spin and statistics both arise from π₁(S¹) = ℤ.
Search: "spin statistics Kaluza-Klein extra dimension winding number"
Prior art: Does Souriau's geometric approach (1970) or any string
theory derivation anticipate this?

**B. Born rule from Haar measure on U(1)** (Paper 1 Appendix C)
The claim: the Born rule is the unique U(1)-invariant probability
measure on the e-circle fiber.
Search: "Born rule Kaluza-Klein geometric derivation Haar measure"
Prior art: Geometric derivations of Born rule exist (Deutsch 1999,
Zurek 2005). Does any use compact fiber geometry?

**C. Information paradox resolution via e-conservation** (Paper 3)
The claim: φ₀ + φ₁ = const at the horizon preserves unitarity.
Search: "black hole information e-dimension extra dimension
conservation" and "black hole information Kaluza-Klein fifth
dimension unitarity"
Prior art: Susskind-Lindesay complementarity? String theory
fuzzball approaches? Any similar charge-conservation resolution?

**D. Higgs = Wilson line on S² (Hosotani mechanism)** (Paper 4 §6)
The claim: the Higgs is the gauge-Higgs Wilson line on S².
Search: "Hosotani mechanism S2 electroweak Higgs"
Prior art: The Hosotani mechanism on S² has been studied. Is our
specific identification of the Higgs with the S² Wilson line (not S¹)
new? Most gauge-Higgs unification uses S¹ or CP¹.

**E. GUT unification from G₄ flux ratio n₂/n₁ = −17/9** (Paper 7 §3)
The claim: SU(3)×SU(2)×U(1) unification is equivalent to this
specific flux ratio on CP²×S².
Search: "G4 flux gauge coupling unification M-theory CP2 S2"
and "GUT M-theory compactification flux quantization"
Prior art: Are there M-theory compactifications on CP²×S² with
flux that give the SM gauge group? Is the 17/9 ratio known?

**F. Theorem U and U* (CC underivability)** (Paper 7 §3.6, frontier)
The claim: R_bare ≈ l_P from the algebraic system; the CC is
geometrically isolated to a single modulus.
Search: "cosmological constant moduli stabilization Kaluza-Klein
underivable" and "cosmological constant geometric isolation modulus
M-theory"
Prior art: The KKLT landscape, Bousso-Polchinski flux landscapes.
Is the specific claim that R_bare ~ l_P from the algebraic system new?

**G. Confinement from CP² holonomy** (Paper 5)
The claim: quark confinement is a consequence of the non-trivial
holonomy of CP².
Search: "confinement CP2 Kaluza-Klein holonomy extra dimension"
Prior art: There is literature on extra-dimensional confinement.
Is the CP² holonomy mechanism specifically new?

**H. Spectral gap Δ_{5D} > 0 from Lichnerowicz** (Paper 4 §9, frontier)
The claim: the 5D Dirac operator on CP²×S²×S¹/Z₂ has no zero modes.
Search: "Lichnerowicz spectral gap CP2 S2 M-theory compactification
Dirac operator"
Prior art: Lichnerowicz bounds on specific M-theory compactifications?

### For each result, produce:

1. **Status:** New / New derivation of known result / Already in
   literature (cite) / Unclear
2. **Closest prior work:** Specific papers, with arXiv IDs if found
3. **What is genuinely new (if anything):** The specific element
   that has not appeared before
4. **Risk level for referees:** Low / Medium / High (high = likely
   to get "this is known" objection)

**Deliverable:** `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/problem-D-novelty-audit.md`

This should be structured as a table + detailed discussion for each
item. Be thorough and honest. A result that is a "new derivation of
a known result" is still publishable and valuable — it just needs to
be framed correctly.

---

## Yang-Mills Patterns to Apply Explicitly

The following moves from the Yang-Mills proof are directly applicable
to the three physics problems above. Opus should identify which move
applies to which problem and use it:

**Move 1: Transfer Matrix Positivity (Thm 4 → Δ₀^KK > 0)**
*Establish the mass gap at the KK level first, then transfer to the
standard theory.*
Application for Problem B: establish OS3 at the KK level (product
manifold lemma), then project to the 4D theory via Feshbach (exactly
as Yang-Mills Theorem 5 did for the reduced transfer matrix).

**Move 2: Stability of Deviation Order (all dim-6 ops have dev ≥ 2)**
*Show that corrections to a key quantity are bounded to all orders.*
Application for Problem B: show that corrections to the OS3 inner
product from dilaton fluctuations are bounded by (δR/R₀)² to all
orders — not just the first few.

**Move 3: Bogomolny/Index Bounding (c₂ ≠ 0 sectors suppressed)**
*Topological sectors other than the vacuum are exponentially suppressed.*
Application for Problem A: if the 5/2 is topological, it should
survive as a bound — even if the exact value isn't 5/2, the
topological structure constrains the ratio to a specific class.

**Move 4: Product Manifold Lemma (Appendix D, Lemma D.1)**
*Reflection positivity on M₁ × M₂ follows from RP on M₁ and
positive-definite metric on M₂.*
Application for Problem B: this applies directly with M₁ = M⁴_E
and M₂ = S¹. This is the short new argument that may close OS3.

**Move 5: Dim-6 Classification (Newton decomposition)**
*Enumerate all operators of a given dimension and show they are
bounded by a structural property.*
Application for Problem C (DMW): enumerate all characteristic class
contributions to the tadpole on non-spin 8-manifolds and classify
which ones restore integrality.

---

## Theorems and Results Available to Use Freely

**From the framework:**
- **K.1** (Epstein Vanishing): E_L(−j; Q) = 0 for all j ≥ 1
- **K.3** (BPHZ Factorization): amplitudes factor; all counterterms vanish
- **Theorem U**: R_bare = (63n₁)^{3/2}/(128π^{11/2}M_Pl) ≈ l_P
- **Theorem U***: No algebraic/topological mechanism produces R >> l_P
- **Theorem 9.1** (Horizon vertex = 1, unconditional): product metric
  + Fourier orthogonality → vertex = 1 independent of 4D geometry
- **GUT flux condition**: n₂/n₁ = −17/9 from torsion-corrected GVW
- **Spectral gap**: Δ_{5D} ≥ √5/r₃ > 0 (Lichnerowicz on CP²)
- **OS1, OS2, OS4**: established; OS3 approximate (10⁻⁶⁰)

**From Yang-Mills:**
- **Thm 4** (Δ₀^KK > 0): KK transfer matrix has positive gap
- **Thm 5** (IR equivalence): KK theory → standard YM via reduced
  transfer matrix + Feshbach projection
- **Lemma D.1** (Product manifold RP): RP on M₁ × M₂ from RP on
  M₁ and compact M₂
- **Stability of deviation order**: dim-6 operators all have dev ≥ 2

---

## Instructions for Sub-Agents / Context Management

Use local sub-agents for each problem to preserve context:

- **Sub-agent A**: Problems A (Z₃ overlap) + D (novelty audit)
- **Sub-agent B**: Problems B (OS3) + C (DMW tadpole)

Each sub-agent should:
1. Read the relevant prior files (listed above per problem)
2. Read the Yang-Mills sections relevant to its problem
3. Run web searches before computing (not after)
4. Write its deliverable as a standalone .md file

Sub-agent B should specifically read:
- `/Users/gsix/yang-mills/preprint/sections/D-reflection-positivity.md`
- `/Users/gsix/yang-mills/preprint/sections/C-transfer-matrix.md`
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/oi3-reflection-positivity.md`
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/oi2-freed-witten-tadpole.md`

Sub-agent A should specifically read:
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/problem1-cc-underivability.md`
- `/Users/gsix/quantum-geometry-in-5d-latex/etc/31-overlap-integral.md`
- Paper 4 §7.22 (neutrino mass from gauge-Higgs seesaw)
- Paper 7 §3 (F-flat conditions linking R to r₃)

---

## Output Files

Write four detailed .md files in `/Users/gsix/quantum-geometry-in-5d-latex/etc/frontier-research/`:

1. `problem-A-overlap-5half.md` — Z₃ overlap and 5/2 (Problem A)
2. `problem-B-exact-OS3.md` — Exact reflection positivity (Problem B)
3. `problem-C-dmw-tadpole.md` — DMW tadpole correction (Problem C)
4. `problem-D-novelty-audit.md` — Novelty audit (Problem D)

Each file should follow the Round 1 structure:
- **Key new insight (one sentence)** — the short argument that does the work
- **Methodology** — which patterns were used and why
- **The proof chain** — each step with status (Proved / Literature / New / Open)
- **What would make it airtight** — the minimal additional input needed
- **Honest assessment** — table of confidence levels per claim

The Yang-Mills proof chain table (in PROOF-CHAIN.md) is the model for
the proof chain format.

---

## Priority Order

1. **Problem D (Novelty Audit)** — most urgent for publication; can
   run in parallel with the others. 60 min.

2. **Problem B (Exact OS3)** — the Product Manifold Lemma argument
   may be short and complete; try it first before the others. 45 min.

3. **Problem A (Z₃ Overlap / 5/2)** — either closes a major thread
   or opens one; high value either way. 60 min.

4. **Problem C (DMW Tadpole)** — most dependent on literature; web
   search first, compute second. 45 min.

---

*The Yang-Mills proof succeeded because one short structural argument*
*(stability of deviation order) unlocked a blocked proof chain.*
*Each problem above has a candidate for that argument.*
*Find it. Use the patterns. Search the web.*
*Write what you find, honestly.*
