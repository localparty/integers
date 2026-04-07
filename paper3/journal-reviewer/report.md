# Referee Report — Paper 3
## "Information Preservation in Black Hole Evaporation via e-Dimension Geometry"
## Submitted to Physical Review D

**Recommendation:** Major Revision

---

## 1. Executive Summary

This paper proposes that the black hole information paradox is resolved by a compact
fifth dimension (the "e-circle," S¹) in which infalling information is encoded as a
Noether charge shift δφ, visible only in 5D and invisible to 4D observers. The 4D
Hawking thermal radiation is recovered as a partial trace over this dimension; the
full 5D state is argued to be pure. The paper addresses, in sequence: the problem
of time (resolved by a winding-number clock via Page-Wootters); the Page curve
(recovered conditionally); the AMPS firewall paradox (resolved via a superselection-
sector argument); and the scrambling time.

The writing is unusually transparent about what is proved, what is conditional, and
what is open — a feature that aids evaluation enormously. The central mechanism is
internally consistent at the qualitative level and several key technical concerns
are addressed directly and honestly. However, multiple steps require either a
completed calculation or a more precise definition before acceptance:
(i) the e-correlations-as-superselection argument is logically sound but the explicit
counting of 4D entanglement capacity within a fixed sector H_Q is not supplied;
(ii) the Page curve derivation is conditional on the fast-scrambler assumption, which
the paper does not derive from the 5D Hamiltonian, yet the abstract and Section 12
use language inconsistent with this conditionality;
(iii) the s₀ = 1 G-renormalization argument is cited but not computed for this
specific framework;
(iv) the Hadamard condition argument (Section 9.5) assumes a factorization of the 5D
vacuum state that is not derived — the 5D Bogoliubov transformation has not been
computed.

The paper is not ready for publication in its current form but the program is coherent
and well-motivated. A major revision addressing the points below would bring it to a
publishable standard.

---

## 2. Point-by-Point Findings

---

### Part A: The e-Dimension and Causality

---

#### A1(a): Definition of "no causal structure" — Precision of the zero-mode claim
**Rating: (B) CLOSABLE GAP**

The earlier informal language ("the e-dimension carries no causal structure") has been
replaced in the final text (Sections 2.1, 2.4) by a more precise statement: the 5D
Lorentzian metric has a complete causal structure; the e-circle is a spacelike
direction within it; what is non-dynamical is exclusively the n = 0 zero-mode
background geometry, not the full 5D theory. KK excitations (n ≠ 0) propagate
subluminally. This framing is physically defensible.

A closable gap remains. The claim that "background geometry changes are not subject
to propagator bounds" is argued by analogy (VEV shifts of a Higgs field) without
specifying the functional space in which "changing the zero-mode" is a well-defined
operation. In classical field theory a VEV shift is a change of background
configuration; in quantum field theory it is a coherent state shift. Neither analogy
is made fully precise for a compact KK dimension in a gravitational background. The
paper needs to state: is φ₀ (the zero-mode) a c-number classical background or a
quantum operator? If a c-number, in what sense is the "algebraic e-conservation
constraint" an operator equation? If an operator, what is its canonical conjugate
and what is the Hilbert space?

**What is required:** A precise definition of the n = 0 zero-mode as either a
classical background parameter or a quantum operator, with the corresponding Hilbert
space. One page of precision would close this.

**Estimated difficulty:** One page.

---

#### A1(b): No-signaling constraint
**Rating: (B) CLOSABLE GAP**

Section 5.3 provides the key ingredients: (i) the e-coordinate shift δφ is invisible
to 4D observers because 4D observables are KK zero-mode projections, invariant under
e-translation; (ii) massive KK modes that could leak e-information into 4D observables
are thermally suppressed by exp(−m₁/T_H) ≈ exp(−10⁹) for astrophysical black holes.
Property 2 of Section 9.3.1 ([Q̂_e, Ô₄D] = 0) is proved at tree level and argued to
extend to loops via charge conservation at vertices.

The gap: the no-signaling claim for two spacelike-separated e-entangled observers is
not given as an explicit theorem. The framework has all the ingredients — the
superselection structure of Section 9.3.1 implies that 4D measurement statistics are
independent of e-sector state — but the explicit argument (show that the 4D marginal
state ρ_4D = Tr_e[ρ_5D] of either observer is unaffected by operations of the other
observer on the e-sector) is not given.

**What is required:** A one-paragraph explicit no-signaling argument using the
superselection structure and the fact that 4D measurement statistics are determined
entirely by ρ_4D = Tr_e[ρ_5D], which is invariant under the other observer's
e-operations.

**Estimated difficulty:** One paragraph.

---

#### A1(c): Coordinate-dependence of "instantaneous propagation"
**Rating: (C) SOUND**

The paper (Sections 5.2, 5.4) explicitly abandons the language of "instantaneous
propagation" and replaces it with: the e-conservation constraint Σφᵢ = C is an
algebraic constraint on the state space, not a differential equation in spacetime.
Section 5.4 further clarifies that the "instantaneous" character refers to local
absorption at the vertex (the new Planck pixel acquires φ_in by local Noether
conservation); redistribution across all pixels takes t_scr. The gauge-fixing
analogy is articulated with its limits (e-charge is physical, not redundant) duly
noted.

The question of preferred coordinate frame is mooted: there is no propagation event
to make simultaneous. The constraint holds in all coordinate frames.

**Assessment:** Satisfactorily addressed.

---

#### A1(d): Consistency with KK propagator bounds from Paper 1
**Rating: (C) SOUND**

Section 2.4 addresses this correctly. The propagator bounds |g_b| ≤ C₀ exp(−m₁a)
govern dynamical n ≠ 0 KK mode excitations — fluctuations around a background.
The δφ discussed here is a change in the n = 0 background fiber geometry, not a KK
mode excitation, and is therefore not subject to those bounds. The Yukawa analogy
(the bound on a massive mediator does not constrain how fast the scalar's VEV can
shift) is physically correct.

The residual definitional question from A1(a) is the only remaining concern.

**Assessment:** Satisfactorily addressed modulo the definitional issue in A1(a).

---

#### A2(a): One Planck area per bit — derivation vs. consistency
**Rating: (B) CLOSABLE GAP**

Section 4.3 is admirably honest: "one Planck area per bit" is derived from the
conjunction of e-conservation and S_BH = A/4 (Section 8), not from e-conservation
alone. The exact area eigenvalue spectrum from the 5D quantum gravity operator algebra
is deferred to future work.

The gap is that the s₀ = 1 claim in Section 7.3 — ln(d_e) × (l_{P,bare}²/l_{P,phys}²) = 1
— requires the G-renormalization from the KK tower to produce exactly the right
species factor. The paper cites Jacobson (1994) / Susskind-Uglum (1994) but does not
compute the one-loop KK contribution to G-renormalization for this specific framework
(with d_e = 2πR₀/l_{P,bare} ~ 10³⁰ internal states). Whether the renormalization
exactly cancels ln(d_e) — as opposed to giving s₀ = 1 + O(subleading KK corrections)
— needs to be verified or cited explicitly.

**What is required:** An explicit computation or citation showing that the one-loop
renormalization of Newton's constant from the KK tower in this framework produces
exactly the species factor needed to absorb ln(d_e), giving s₀ = 1 with no free
parameters.

**Estimated difficulty:** One paragraph (if the result is implicit in Paper 1
Appendix F/S) to one page of calculation.

---

#### A2(b): Discrete growth vs. smooth classical dynamics
**Rating: (B) CLOSABLE GAP**

Section 4.2 correctly invokes the Bohr correspondence principle: for M >> M_Pl the
discrete Planck-area growth events are invisible at classical resolution, with
corrections suppressed by M_Pl/M. The analogy to atomic energy levels reproducing
classical orbits for large quantum numbers is appropriate.

What is missing is a one-sentence check: the net effect of N_growth area-growth
events and N_emission Hawking emissions produces the standard dM/dt = −(Hawking rate)
to leading order, with corrections O(M_Pl/M). The sign consistency (the black hole
mass decreases despite discrete growth events from infalling matter) relies on the
Hawking emission rate exceeding the accretion rate — standard for an isolated black
hole but worth stating explicitly.

**What is required:** One sentence confirming that the net dynamics reproduce the
standard semiclassical M(t) to leading order in M_Pl/M.

**Estimated difficulty:** One sentence.

---

#### A2(c): The e-coordinate of the horizon as a null surface
**Rating: (B) CLOSABLE GAP**

Section 4.3 provides the geometric definition: the e-bundle restricts to the null
hypersurface; the "e-coordinate of the horizon" is the section of this restricted
bundle; the e-Killing vector ∂/∂φ is spacelike at the horizon (Section 9.3.2,
Gap 3), so Q_e is well-defined there.

The gap is that the creation of a "new Planck pixel" at the horizon when matter falls
in is a quantum gravity concept not derived from the 5D equations of motion. The
paper acknowledges this. The claim is that the semiclassical counting is consistent:
one absorbed quantum increases the entropy by one unit. But the operational meaning
of "new pixel creation" requires specifying what quantum gravity process it
corresponds to. The paper's current position — deferring the exact area eigenvalue
spectrum — is acceptable if stated explicitly.

**What is required:** Explicitly state that "Planck pixel creation" is an effective
description valid in the semiclassical limit, with the underlying quantum gravity
process deferred, consistent with the acknowledgement already in Section 4.3.

**Estimated difficulty:** One sentence.

---

### Part B: The Page Curve and Unitarity

---

#### B1(a): Page curve — calculation vs. conditional theorem
**Rating: (B) CLOSABLE GAP**

Section 7.6 explicitly stratifies the result into three levels: Level 1 (derived
from 5D equations of motion), Level 2 (conditional on fast-scrambler assumption),
Level 3 (open: deriving fast-scrambler from 5D Hamiltonian). Theorem 7.1 is
labeled "Conditional Page Curve." This stratification is exemplary.

The gap is that the abstract states the Page curve is "reproduced" and Section 12
states the framework is "Deriving (not assuming) the Page curve" — language
inconsistent with the Level 2/3 stratification. The abstract also says the Page
curve result is "given the fast-scrambler assumption (Sekino-Susskind)" which is
the correct hedge, but Section 12 omits this qualifier in the comparison table.

Additionally: no density matrix ρ_rad is computed by evolving the full 5D state.
The Page curve argument is entirely kinematic — it applies Page's (1993) argument to
the e-Hilbert space, given the fast-scrambler assumption. The 5D Bogoliubov
transformation has not been computed. This is fine as a conditional result but
must be stated clearly throughout.

**What is required:** Revise the abstract and Section 12 to consistently reflect
the conditional status of Theorem 7.1. Replace "deriving (not assuming)" with
language like "reproducing, conditional on the fast-scrambler assumption."

**Estimated difficulty:** One paragraph of revision.

---

#### B1(b): The coefficient s₀
**Rating: (B) CLOSABLE GAP**

Covered in A2(a). The argument that s₀ = 1 after G-renormalization is structurally
correct but requires an explicit verification that the KK species in this framework
produce the exact G-renormalization needed, without residual corrections from
subleading KK levels.

**What is required:** See A2(a).

---

#### B1(c): Early-time behavior of S_rad
**Rating: (B) CLOSABLE GAP**

Section 7.7 correctly bounds the early-time (k < k_scr) entropy and correctly notes
that the Page time and turnover are unaffected (k_scr/N₀ ~ 10⁻⁷⁵). The bound
0 ≤ S_rad(k) ≤ k × ln(d_e) for k < k_scr is stated.

The gap is that the paper makes no statement about whether the 5D Bogoliubov
transformation changes the leading-order form of the early-time radiation density
matrix compared to the standard 4D Hawking result. The 4D Hawking calculation gives
S_rad increasing monotonically before the Page time. The 5D calculation should agree
at leading order. This agreement is assumed (Section 6.2 says the 4D projection of
the 5D state reproduces the Hawking result) but not verified by computing S_rad from
the explicit 5D state. Adding a sentence to this effect would close the gap.

**What is required:** One sentence acknowledging that the early-time Page curve
relies on the same assumption (fast-scrambler) as the late-time curve, and that
no direct state evolution has been computed.

**Estimated difficulty:** One sentence.

---

#### B1(d): Comparison to island formula — quantitative agreement
**Rating: (C) SOUND**

Section 10.5 explicitly distinguishes what is established (leading-order Page curve,
qualitative island identification) from what is not (replica wormhole derivation,
subleading exp(−S_BH) corrections, extension to non-AdS spacetimes). The connection
to the island formula is presented as a "physical picture, not a mathematical
derivation." This is accurate and appropriately hedged.

**Assessment:** Satisfactorily hedged. No overclaiming.

---

#### B2(a): Monogamy — e-correlations as superselection constraints
**Rating: (B) CLOSABLE GAP**

This is the central structural claim of the paper. The argument (Section 9.3,
Theorem 9.1):
1. Q̂_e commutes with H_5D (Noether, exact).
2. Q̂_e commutes with all 4D observables (proved for zero-modes; extended to loops
   by charge conservation at every vertex — Gap 1 derivation in Section 9.3.2).
3. H_5D decomposes into superselection sectors H_Q (Wick-Wightman-Wigner theorem).
4. Monogamy applies within H_Q; e-conservation determines which H_Q the system
   occupies; these are not competing resources.

The logical structure is correct. The horizon vertex factor is derived in Appendix B
(S¹ Fourier orthogonality, Ward identity), closing the formerly remaining assumption.
The result holds in the semiclassical regime M >> M_Pl (as stated in Appendix B.8).

The gap: the paper does not supply an explicit counting argument showing that within
a fixed superselection sector H_Q, the 4D entanglement capacity of the late Hawking
mode b is not reduced by the e-superselection constraint. The claim is that the
e-constraint determines the *label* Q (which sector), not the *dimension* of H_Q
(how much 4D entanglement is available). This is the right claim — but it needs
to be stated explicitly as a counting argument. Concretely: within H_Q, does mode b
retain full access to its 4D entanglement quota E_max(b) = 1 ebit, or has the
e-constraint reduced the effective dimension of H_Q?

The answer is that the e-constraint fixes Q but the dimension of H_Q is
dim(H_Q) = (d_e^{N_BH + N_rad})_{Q-sector} — still exponentially large — so the
4D entanglement capacity within H_Q is unaffected. This needs to be stated.

Additionally: the argument is restricted to M >> M_Pl (Appendix B.8); this
restriction should also appear explicitly in Section 9.3, not only in the appendix.

**What is required:** (1) Add one paragraph in Section 9.3 with the counting
argument showing dim(H_Q) is exponentially large and the 4D entanglement capacity
within H_Q is unaffected by the e-superselection. (2) State the M >> M_Pl
restriction in Section 9.3 explicitly.

**Estimated difficulty:** One to two pages.

---

#### B2(b): The Bogoliubov transformation — 5D vacuum factorization
**Rating: (A) GENUINE GAP**

The Hadamard condition argument (Section 9.5) requires the 4D marginal state
ρ_4D = Tr_e[ρ_5D] to be the 4D Unruh vacuum. The paper derives this by claiming the
5D vacuum factorizes: |0⟩_5D = |0⟩_{4D,Unruh} ⊗ |0⟩_e. The justification is the
product-metric structure: since g_5D = g_4D + R₀² dφ², the 5D field equation
decomposes into independent 4D equations for each KK mode, and the mode functions
factorize.

This argument is not sufficient. The 5D vacuum state is defined by the 5D notion of
positive-frequency modes. In a product spacetime M⁴ × S¹, the 5D positive-frequency
condition involves the 5D energy, which includes KK masses. An infalling observer
defines a vacuum by the absence of 5D particles — including all KK levels. The
Bogoliubov transformation relating the infalling vacuum to the exterior Fock space
mixes 4D modes with KK excitations. The 4D marginal state ρ_4D = Tr_e[ρ_5D] will
receive corrections from the KK sector of the Bogoliubov transformation that are
absent in the pure 4D Hawking calculation.

The paper estimates these corrections are suppressed by (M_Pl/M)⁴ × (l_P/R₀)² ~
10^{-60} for astrophysical black holes. This is a dimensional estimate, not a
calculation. The 5D Bogoliubov coefficients have not been computed. It is therefore
not established that ρ_4D is the Unruh vacuum — it may differ by KK corrections
that are small but not zero.

For the Hadamard condition (which requires the 2-point function to have the exact
Minkowski short-distance behavior), even small corrections could in principle modify
the short-distance structure. The paper cites Fredenhagen-Haag (1990) and Kay-Wald
(1991) for the Hadamard property of the 4D Unruh vacuum, but these results apply
to the 4D theory. Their extension to the 5D theory with KK modes requires knowing
the 5D Bogoliubov transformation.

**What is required:** The paper must either:
(a) Compute the 5D Bogoliubov transformation and show the 4D marginal state is the
Unruh vacuum to the stated accuracy; or
(b) Provide a rigorous bound (not a dimensional estimate) on the KK corrections to
the Bogoliubov coefficients, establishing that the Hadamard condition is satisfied
to the stated precision; or
(c) Explicitly downgrade the Hadamard condition claim from a result to a working
assumption, stating that verifying it from first principles requires computing the
5D Bogoliubov transformation (deferred to future work).

Option (c) is the honest path if (a) or (b) cannot be achieved in revision.

**Estimated difficulty:** One paper for (a); one page for (b) if a rigorous bound
can be derived from the KK mass gap; one paragraph for (c).

---

#### B2(c): The infalling observer's experience
**Rating: (C) SOUND**

Section 9.4 correctly argues: the e-imprint δφ is a phase shift in the fiber
dimension, creating no energy barrier in M⁴; the observer's 4D detectors respond
only to KK zero-mode observables (Property 2), which are e-translation-invariant;
the 5D equivalence principle holds (the e-imprint is a global holonomy, detectable
only through non-local measurements unavailable to a local infalling observer). The
Berry phase analogy is physically correct.

Section 9.5's Hadamard argument is contingent on B2(b), but the qualitative
no-drama conclusion is sound.

**Assessment:** Sound contingent on resolution of B2(b).

---

#### B2(d): Equivalence principle and horizon hair
**Rating: (C) SOUND**

The e-imprint is a connection on the principal U(1) bundle over S² × S¹ (global
holonomy), not a local curvature property. It creates no local force or energy
density. The no-hair theorem is sidestepped: e-imprints are not detectable by 4D
asymptotic measurements. The 5D equivalence principle (local 5D geometry is flat
M^{4,1}) is preserved. The argument is structurally the same as the Aharonov-Bohm
effect: global non-triviality of a gauge connection with no local observable effect.

**Assessment:** Sound.

---

### Part C: Technical Calculations

---

#### C1(a): Self-adjointness and the correct clock observable
**Rating: (C) SOUND**

Section 3.2.1 directly addresses the angle-angular momentum problem (Garrison-Wong
1970): φ̂ is not self-adjoint on L²(S¹); the correct clock observable is the winding
number W, defined on the universal cover R of S¹ and self-adjoint with integer
eigenvalues. The total winding over evaporation W_evap ~ S_BH/(2π) >> 1 gives the
clock sufficient resolution. The e-sector Hamiltonian Ĥ_e is already normal-ordered;
factor-ordering does not arise.

**Assessment:** The self-adjointness issue is correctly identified and resolved.

---

#### C1(b): Independence of the e-clock from the metric
**Rating: (B) CLOSABLE GAP**

Section 3.2 argues metric-independence via the Z₂ orbifold symmetry φ → −φ, which
forbids the off-diagonal KK gauge field A_μ = 0 exactly (as a symmetry consequence,
not a gauge choice). This makes ∂φ/∂τ = −E/ℏ hold in any 4D background.

The gap: whether the Z₂ symmetry is preserved at the quantum level (anomaly-free)
and whether it prevents radiative corrections to g_{5μ} is not stated. For a
discrete Z₂ symmetry in 5D, anomaly cancellation should follow straightforwardly,
but the argument should be given (or a reference to Paper 1 provided).

**What is required:** One sentence confirming that the Z₂ orbifold symmetry is
anomaly-free and prevents radiative corrections to g_{5μ}, citing Paper 1 §2.1
if established there.

**Estimated difficulty:** One sentence.

---

#### C1(c): Wheeler-DeWitt Hamiltonian factorization
**Rating: (B) CLOSABLE GAP**

Section 3.3 carefully limits the factorization to the Born-Oppenheimer regime:
matter fields in a fixed background (frozen radion, energy below 1/R₀). The full
gravitational WdW equation does not factorize. Section 3.3.1 correctly decouples
the frozen-formalism problem (resolved by the e-clock) from the factor-ordering
problem (unresolved for H_{4D,grav}, as in all approaches to quantum gravity).

The gap: the Born-Oppenheimer approximation for the *gravitational* sector requires
E_clock << M_BH. For E_clock ~ T_H ~ 1/M (in Planck units) and M >> M_Pl, the ratio
E_clock/M_BH ~ 1/M² << 1. This condition holds throughout semiclassical evaporation
but should be stated explicitly.

**What is required:** One sentence confirming E_clock/M_BH ~ 1/M² << 1 throughout
semiclassical evaporation, validating the Born-Oppenheimer limit for the gravitational
sector.

**Estimated difficulty:** One sentence.

---

#### C2(a): The ln(S_BH) factor in scrambling time
**Rating: (C) SOUND**

Section 11.2 correctly derives the ln(S_BH) factor from the Hayden-Preskill
decoupling theorem (Hayden-Preskill 2007, Theorem 2): for a random unitary acting on
S_BH qubits, an infalling bit becomes decodable after O(ln S_BH) additional emissions.
Applied to the e-sector: the "qubits" are Planck pixels; the thermalization rate is
1/β. Therefore t_scr = O(ln S_BH) × β, reproducing Sekino-Susskind. The ln(S_BH)
factor arises from 4D thermal dynamics scrambling the e-imprint — not from any
e-propagation speed — which is clearly stated. The derivation is conditional on the
same random-unitary assumption as Theorem 7.1, acknowledged.

**Assessment:** Sound.

---

#### C2(b): Consistency with the chaos bound
**Rating: (C) SOUND**

Section 11.3 correctly argues: the MSS chaos bound λ_L ≤ 2πT_H/ℏ constrains 4D
OTOCs; by Property 2 ([Q̂_e, Ô_4D] = 0), the e-sector is decoupled from all 4D
OTOCs; the Lyapunov exponent is λ_L = 2πT_H/ℏ saturated in the 4D sector alone;
the instantaneous zero-mode encoding does not enter the chaos bound. This is
self-consistent.

**Assessment:** Sound.

---

#### C3(a): Non-perturbative completion — M-theory identification
**Rating: (B) CLOSABLE GAP**

Appendix A.4 labels the M-theory argument as a "plausibility argument, not a proof,"
with both premises explicitly flagged: Premise 1 (framework ≅ sector of M-theory)
is conjectured, verification pending Paper 4; Premise 2 (M-theory is non-perturbatively
well-defined) is the standard unproven assumption shared by all M-theory approaches.
This is the correct and honest presentation.

The gap is organizational: the central results of this paper (Theorems 6.1, 7.1, 9.1)
do not require M-theory. All central claims follow from the perturbative framework
(Paper 1) plus the 5D equations. The M-theory completion section should be clearly
labeled as a forward-looking discussion that does not bear on the paper's main
results. The current presentation in Appendix A.4 already goes some way toward this
but the dependency relationship could be stated more prominently.

**What is required:** State explicitly in the introduction to Appendix A (or Section
A.4) that no result in Paper 3 requires the M-theory completion; the M-theory
identification is additional context contingent on Paper 4.

**Estimated difficulty:** One sentence.

---

#### C3(b): Bubble of nothing instability
**Rating: (C) SOUND**

Section A.3.1 correctly identifies two independent suppression mechanisms for the
Witten (1982) bubble of nothing: (i) Casimir barrier with S_CDL >> 10³⁰ giving
Γ ~ exp(−10³⁰); and (ii) antiperiodic fermion boundary conditions (from the spin-
statistics assignment of Paper 1, Appendix B), which per Witten (1982, p. 1263)
require a fermionic zero mode on the bubble wall, kinematically suppressing
nucleation beyond the Casimir barrier. The antiperiodic spin structure is derived
from within the framework (not assumed), so the suppression is a consequence of the
framework's structure.

**Assessment:** Sound.

---

#### C3(c): Topology change and black holes
**Rating: (B) CLOSABLE GAP**

Section A.3.1 addresses 4D topology change during evaporation: the 5D metric remains
g_5D = g_4D(x,t) + R₀² dφ² throughout; R₀ is constant (modulus stabilization); the
e-fiber S¹ accompanies the evolving 4D base without degenerating. KK monopole
production (suppressed by M_KK ~ 10²² kg) and instanton-driven topology change
(action ~ 10³⁰) are negligible.

The gap: the argument that the S¹ fiber is stable during the Planck-scale phase of
evaporation (M ~ M_Pl) relies on modulus stabilization, which is a semiclassical
result. At M ~ M_Pl, quantum fluctuations of R (the radion) are O(1) and the product-
structure approximation breaks down. Whether the gravitational path integral at
M ~ M_Pl generates 5D topological contributions (e.g., fiber degeneration at the
singularity) is not addressed. The paper should acknowledge that the S¹ stability
argument is restricted to M >> M_Pl, consistent with the scope of the rest of the
paper.

**What is required:** One sentence noting that S¹ fiber stability during Planck-scale
evaporation is not established from the full path integral; the argument holds for
M >> M_Pl where modulus stabilization is reliable.

**Estimated difficulty:** One sentence.

---

## 3. Recommendation to Editors

I recommend **Major Revision**.

The paper is a serious and technically careful contribution to the black hole
information problem. The central mechanism — encoding infalling information as a
zero-mode shift δφ of a compact fifth dimension, with 4D thermal radiation recovered
as a partial trace — is physically coherent and internally consistent. The paper's
explicit stratification of results by logical status (proved / conditional / open) is
exemplary. The treatments of self-adjointness (winding number clock), the horizon
vertex factor (Appendix B, Fourier orthogonality + Ward identity), the chaos bound,
and the bubble of nothing instability are all satisfactory.

The three issues most critical to resolve before publication are:

**1. The 5D Bogoliubov transformation (B2(b) — GENUINE GAP).**
The Hadamard condition argument (Section 9.5) asserts ρ_4D = |0⟩_{4D,Unruh}⟨0| by
claiming the 5D vacuum factorizes as |0⟩_{5D} = |0⟩_{4D,Unruh} ⊗ |0⟩_e. This
factorization is not derived; the 5D Bogoliubov coefficients have not been computed;
the dimensional estimate of KK corrections is not a rigorous bound. The paper must
either (a) compute the 5D Bogoliubov transformation, (b) provide a rigorous bound
on KK corrections to the Hadamard condition, or (c) explicitly downgrade the Hadamard
claim to a working assumption with the verification deferred. Option (c) is the
honest path if (a) and (b) exceed revision scope.

**2. Consistent labeling of the Page curve result (B1(a) — CLOSABLE GAP).**
The abstract and Section 12 use language ("deriving, not assuming, the Page curve")
that is inconsistent with the explicit Level 2/3 stratification of Section 7.6, which
correctly labels Theorem 7.1 as conditional on the fast-scrambler assumption. This
inconsistency must be resolved throughout; the paper's own Level 2 language is the
correct standard.

**3. Superselection sector counting argument for AMPS (B2(a) — CLOSABLE GAP).**
Theorem 9.1's resolution of the AMPS paradox requires not only that e-correlations
are superselection constraints (established) but also that the 4D entanglement
capacity of the late Hawking mode b within a fixed H_Q is not reduced by the
e-superselection constraint. This counting argument is implicit but must be stated
explicitly: dim(H_Q) is exponentially large; within H_Q, mode b retains full 4D
entanglement capacity; the e-constraint and the 4D vacuum entanglement are orthogonal
resources.

Subject to revision of these three points — and the minor clarifications noted in
A1(a), A2(a,b,c), B1(b,c), C1(b,c), C3(a,c) — the paper presents an original and
coherent program that merits publication.

---

*Signed: Anonymous Referee*
*Submitted for Physical Review D*
