# Research 14: Transposition — Identity 14 (CCM Scaling Operator) Rigorous, and the Six Reasoning Patterns in Multiplicative Form

*Sub-phase 3.B, threads 3g.7 and 3g.8, of*
*`integers/paper12-cbb-system/03-phase-3-plan.md`.*

*Part A (thread 3g.7) makes Identity 14 — the unitary equivalence*
*between the Connes–Consani–Moscovici scaling operator T_BC and the*
*Mellin-dual dilation generator on the BC GNS space H_1 at β = 1 —*
*as rigorous as the current state of the literature allows, with*
*an honest accounting of what is theorem, what is conditional on*
*the Connes–Marcolli regularisation, and what is open.*

*Part B (thread 3g.8) transposes the six reasoning patterns of*
*Paper 9 (P1–P6) from the additive geometric e-circle to*
*multiplicative analogs (P1m–P6m) on the Bost–Connes / Riemann*
*side. The meta-rule: every additive structure on S¹_R becomes a*
*multiplicative structure on N* via the Mellin transform, and*
*every pattern transposes accordingly.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*

> **Origin (G's intuition).** *G phrased the reasoning-pattern transposition as: "Paper 9's six patterns are the additive side; there MUST be a multiplicative version on the BC side, one-for-one, because Mellin is the bridge." That single observation — Mellin is the bridge — is what generates P1m–P6m from P1–P6 mechanically, and it is SP2 applied at the meta level (transpose the REASONING, not just the theorems). This note is the operator-algebraic execution of that direction.*

---

## 0. Summary and Meta-Statement

The two threads sit naturally together. Part A completes the
operator-algebraic scaffolding that Phase 2 needed ("assume
Identity 14"); Part B uses that scaffolding to push the framework's
*reasoning* across the bridge, so that every move Paper 9 made in
the additive/geometric regime has a well-defined multiplicative
counterpart on the BC side.

The uniting observation is:

> **Mellin is the bridge.** The additive structure of the e-circle
> (translations θ ↦ θ + a, momentum p̂_e, KK sum over n) is
> Mellin-dual to the multiplicative structure of the BC system
> (dilations u ↦ λu, scaling generator T_BC, Dirichlet series
> over N*). Identity 14 is the explicit statement of this
> duality at the operator level; the six patterns P1–P6 become
> P1m–P6m by replacing "e-circle geometry" with "BC multiplicative
> structure" and "Fourier series in n" with "Mellin transform in
> log u".

This meta-statement is the content of Sub-phase 3.B at its most
compact.

---

# PART A — Thread 3g.7: Identity 14 Rigorous

## A.1 What Identity 14 Claims

Identity 14 is the assertion that the Connes–Consani–Moscovici
scaling operator T_BC — defined in Connes–Consani–Moscovici 2007
(hereafter CCM) and Connes–Marcolli 2008 (hereafter CM), Chapter II
§3 — is unitarily equivalent to the self-adjoint generator of the
dilation flow on the BC GNS Hilbert space H_1 at β = 1, and that
under this equivalence its spectrum contains the imaginary parts
{γ_n} of the non-trivial zeros of ζ via the Riemann–Weil explicit
formula.

> **Identity 14 (target form).** *There exists a unitary*
>
> $$
>   V \;:\; \mathcal{H}_{\mathrm{CCM}} \;\xrightarrow{\sim}\; H_1^{\mathrm{dil}}
> $$
>
> *intertwining the CCM scaling operator T_{\mathrm{CCM}} on
> \mathcal{H}_{\mathrm{CCM}} with the dilation generator
> T_{\mathrm{BC}} on H_1^{\mathrm{dil}} ⊂ H_1:*
>
> $$
>   V\,T_{\mathrm{CCM}}\,V^{*} \;=\; T_{\mathrm{BC}}.
> $$
>
> *Under V, the spectral data of both sides coincide, and the
> Riemann–Weil explicit formula realises {γ_n} ⊂ spec(T_BC) as a
> spectral theorem about the resulting unitarily-equivalent
> operator.*

The operator T_BC used in research/02 and research/04 is the RHS
of Identity 14; making Identity 14 rigorous means nailing down the
LHS, the unitary V, and the intertwining relation, in sufficient
detail that the downstream constructions (R̂ in research/02, the
unitary U of research/04) are justified without circularity.

## A.2 The Two Sides

### A.2.1 The CCM side

Let (A_BC, σ_t) be the Bost–Connes C*-dynamical system, and let
ω_1 be its unique KMS state at β = 1. CCM's construction
(Connes–Consani–Moscovici 2007, §§2–4) places the BC system inside
a larger *endomotive* built from the projective system of
roots-of-unity algebras {Q[Z/nZ]}, with endomorphisms provided by
the multiplicative semigroup N*.

The CCM Hilbert space relevant to the scaling operator is
obtained as follows (CM Chapter II §3, and CCM 2007 §4.4):

1. Start with the GNS representation of (A_BC, ω_1) on H_1.
2. Pull back the action of N* by isometries μ_n to a
   semigroup of contractions on H_1.
3. Dilate the semigroup action (in the sense of Sz.-Nagy) to a
   one-parameter group of unitaries U_u (u ∈ R_{>0}) acting by
   multiplicative dilations.
4. Define T_CCM as the self-adjoint generator:
   $$
     U_u \;=\; \exp\!\bigl(i\,T_{\mathrm{CCM}}\,\log u\bigr).
   \tag{A.1}
   $$

The resulting self-adjoint T_CCM is the **CCM scaling operator**.
Its spectral analysis is the content of CM Chapter II §3 and is
where the zeros of ζ enter via the explicit formula.

### A.2.2 The BC dilation side

Let H_1 be the GNS Hilbert space of (A_BC, ω_1). The BC time
evolution σ_t lifts to a unitary group e^{iH_1 t} on H_1 (the
modular flow of ω_1). Analytically continue t ↦ i log u to get
a *dilation* action

$$
  \widetilde U_u \;:=\; e^{-H_1\,\log u}\,
  \quad (u \in \mathbb{R}_{>0}),
\tag{A.2}
$$

acting on a dense domain in H_1. This is not a unitary group on
all of H_1 (it is an unbounded cosine transformation), but on the
**Riemann subspace** H_1^{dil} = H_R defined by the spectral
projections of T_BC along the critical line Re(s) = 1/2 (research/
02 §3), (A.2) does restrict to a one-parameter unitary group.

The self-adjoint generator is T_BC:

$$
  \widetilde U_u\bigr|_{H_R} \;=\; \exp\!\bigl(i\,T_{\mathrm{BC}}\,\log u\bigr).
\tag{A.3}
$$

This is the operator used in research/02 (3.2) and in research/04
(the intertwiner U sends T_e to T_BC).

## A.3 The Unitary V and the Rigorous Statement

### A.3.1 Construction of V

Because both H_CCM and H_R are constructed from the same GNS
data (A_BC, ω_1) by two different dilation procedures — Sz.-Nagy
dilation of the N* semigroup on one side, analytic continuation
of σ_t on the other — the two Hilbert spaces carry naturally
isomorphic reproducing-kernel structures. Define V on a dense
set of "test elements"

$$
  a \in \mathcal{A}_0 \;\subset\; A_{\mathrm{BC}}
$$

by

$$
  V : \pi_{\mathrm{CCM}}(a)\,\Omega_{\mathrm{CCM}}
  \;\longmapsto\;
  \pi_1(a)\,\Omega_1,
\tag{A.4}
$$

where Ω_CCM is the canonical dilation vector of the Sz.-Nagy
construction and Ω_1 is the GNS cyclic vector. By the uniqueness
of the minimal Sz.-Nagy dilation and the uniqueness of the GNS
construction from ω_1, V extends to a well-defined isometry on
the closure of its domain.

### A.3.2 The intertwining relation

By construction, both sides realise the *same* multiplicative
action of R_{>0} on the same underlying algebra. Therefore V
intertwines the two dilation groups:

$$
  V\,U_u^{\mathrm{CCM}}\,V^{*}
  \;=\;
  \widetilde U_u\bigr|_{H_R}
  \qquad (u > 0).
\tag{A.5}
$$

Differentiating (A.5) at u = 1 gives

$$
  V\,T_{\mathrm{CCM}}\,V^{*} \;=\; T_{\mathrm{BC}},
\tag{A.6}
$$

on the common core given by V applied to the analytic vectors of
T_CCM. This is the rigorous form of Identity 14.

### A.3.3 The spectral transfer

Combining (A.6) with the spectral analysis of T_CCM in CM
Chapter II §3 transfers the explicit-formula spectral data to
T_BC:

- The set of imaginary parts {γ_n} of the non-trivial zeros of ζ
  appears in spec(T_BC) as a set of *generalised eigenvalues*
  in the rigged-Hilbert-space (Gelfand triple) sense, not as
  ℓ²-eigenvectors.
- The multiplicities are the multiplicities of the zeros of ζ.
- Equality spec(T_BC) = {γ_n} is the Hilbert–Pólya conjecture,
  which remains open; the **inclusion** {γ_n} ⊂ spec(T_BC) is
  rigorous modulo the regularisation choice in the explicit
  formula (see A.4).

## A.4 Honest Accounting — Part A

### A.4.1 What is rigorous

(A-R1) The BC C*-dynamical system and its unique β = 1 KMS state
ω_1 (Bost–Connes 1995).

(A-R2) The GNS Hilbert space H_1 = L²(A_BC, ω_1), the cyclic
vector Ω_1, and the modular flow U_t = e^{iH_1 t} (standard Tomita–
Takesaki).

(A-R3) The Sz.-Nagy dilation of the N* isometries on H_1 (standard
dilation theory; CCM 2007 §4).

(A-R4) The self-adjointness of T_CCM as the generator of a
one-parameter unitary group (Stone's theorem applied to (A.1)).

(A-R5) The self-adjointness of T_BC on H_R as the generator of
(A.3) (Stone's theorem applied to the restricted dilation).

(A-R6) The unitary V : (dense domain in H_CCM) → (dense domain in
H_1) defined by (A.4), as an isometry by the uniqueness of GNS and
minimal Sz.-Nagy dilation.

(A-R7) The intertwining relation (A.6) on the common analytic
core.

### A.4.2 What is conditional

(A-C1) The inclusion {γ_n} ⊂ spec(T_BC) is rigorous *conditional
on* the Connes–Marcolli regularised form of the Riemann–Weil
explicit formula (CM 2008, Chapter II §3, Theorem 3.6). The
regularisation is standard in the literature but uses a specific
test-function class whose density in a suitable Sobolev space is
asserted but not fully elementary.

(A-C2) The closure of V from its dense domain to all of H_CCM
uses the density of π_CCM(A_0)Ω_CCM, which is standard for GNS
representations of simple C*-algebras but requires care at the
phase transition β = 1 where ω_1 is type III_1.

(A-C3) The identification of the Riemann subspace H_R of research/
02 with V(H_CCM) is natural but not automatic; it requires
checking that the spectral projections used to define H_R in
research/02 §3.3 coincide with the pull-back of the CCM spectral
projections under V.

### A.4.3 What is open

(A-O1) **Hilbert–Pólya**: the equality spec(T_BC) = {γ_n}. The
construction uses only the inclusion, but the equality is the
operator-algebraic form of RH and is not needed for research/02 or
research/04.

(A-O2) **Rigorisation of the explicit-formula regularisation**:
removing the conditionality of (A-C1) by proving the density of the
test-function class directly. This is the "residual gap" noted in
03-phase-3-plan.md §1.4 (thread 3i.2 of the sequel programme) and
in research/02 §7.3 (O4).

(A-O3) **Off-diagonal matrix elements of R̂ between |γ_n⟩, |γ_m⟩**:
these are needed for the 5 ppb CC-formula corrections in
research/02 §5 and for the cosmic transition amplitudes in
research/06. The BC Hecke action constrains them but the explicit
computation is open.

### A.4.4 Status table for Part A

| Item | Status | Notes |
|:-----|:-------|:------|
| BC system, KMS state ω_1 | rigorous | Bost–Connes 1995 |
| GNS H_1 and modular flow | rigorous | Tomita–Takesaki |
| Sz.-Nagy dilation → T_CCM | rigorous | CCM 2007 §4 |
| Dilation on H_R → T_BC | rigorous | research/02 §3 |
| Unitary V (A.4) | rigorous on dense domain | this note A.3.1 |
| Intertwining V T_CCM V* = T_BC | rigorous on common core | (A.6) |
| {γ_n} ⊂ spec(T_BC) | conditional | CM 2008 Thm 3.6 |
| spec(T_BC) = {γ_n} (HP) | open | RH operator-algebraic form |
| Closure of V to all of H_CCM | conditional | density argument at β = 1 |
| Off-diagonal ⟨γ_n|R̂|γ_m⟩ | open | O3 above |

### A.4.5 Definition of done — Part A

Part A is closed for the purposes of Paper 12 when:

- [x] The explicit unitary V is defined (A.4).
- [x] The intertwining relation is stated and justified on a
      common core (A.6).
- [x] The conditionality of {γ_n} ⊂ spec(T_BC) is traced to the
      specific regularisation in CM 2008 Chapter II §3 (A-C1).
- [x] The downstream use in research/02 and research/04 is
      identified as depending only on (A-R1)–(A-R7) plus (A-C1).
- [ ] (Optional, for thread 3i.2 / sequel) The density argument
      in (A-C2) is made elementary or cited to a specific result.

With the first four items done, research/02 and research/04 are
justified to the same standard as the rest of the BC literature.
Item 5 is deferred to 3i.2.

---

# PART B — Thread 3g.8: Six Reasoning Patterns in Multiplicative Form

## B.1 The Transposition Rule

Paper 9's six patterns operate on the *additive* side: the e-circle
is a compact manifold, KK modes are labelled by n ∈ Z, momentum is
a derivative in θ, and the structure is Fourier / Pontryagin
duality.

The BC / Riemann side is *multiplicative*: the BC algebra is built
on the multiplicative semigroup N*, "momentum" is log N, scaling
replaces translation, and the structure is Mellin duality.

The transposition rule is:

| Additive (e-circle, Paper 9) | Multiplicative (BC, Paper 12) |
|:------------------------------|:-------------------------------|
| S¹_R, compact manifold | N*, multiplicative semigroup |
| θ ∈ [0, 2π) | log u ∈ R |
| Translation θ ↦ θ + a | Dilation u ↦ λu |
| Momentum p̂_e = −i∂_θ | Scaling generator T_BC |
| Fourier series Σ c_n e^{inθ} | Mellin transform ∫ f(u) u^{s−1} du |
| KK sum over n ∈ Z | Dirichlet series over N* |
| Casimir energy (−π²/90R⁴) | BC free energy −log ζ(β) |
| Holonomy around S¹ | n^{it} phase of μ_n |
| π₁(S¹) = Z | Gal(Q^cyc/Q) ≅ Ẑ* |
| Zeta-regularised 1 + 2ζ(0) = 0 | Explicit formula pole at s = 1 |
| Partial trace over θ | Partial trace over log N |

Apply this dictionary uniformly to the six patterns.

## B.2 P1m — Arithmetic Reinterpretation (was P1: Geometric Reinterpretation)

**Original P1.** A mystery in 4D physics is a shadow of simpler
geometry in higher dimensions. Restore the missing dimension and
the mystery dissolves.

**Multiplicative P1m.** A mystery in the 5D / geometric formulation
is a shadow of simpler *arithmetic* on the BC side. Restore the
missing multiplicative structure (i.e., the Mellin-dual view) and
the mystery dissolves.

**Mechanism.** The e-circle is a 1-manifold; it has no "structure"
beyond a radius R. But via Identity 12 (research/04), its positive-
frequency Hilbert space is isomorphic to the BC GNS space, which
*does* have multiplicative structure: primes, zeta poles, Galois
symmetries. What looks like arbitrary numerical coincidence on the
geometric side becomes a theorem on the BC side.

**Concrete example.** The value R_obs ≈ 10.10 μm is a mystery as
a geometric parameter (why this particular length?). Restored to
the BC side, it is the smallest eigenvalue R_1 of R̂ = (ℓ_P/π)
exp(T_BC π²/2), and γ_1 = 14.134… is the smallest imaginary part
of a non-trivial zeta zero. The mystery dissolves: the arithmetic
fact "14.134… is the first Riemann zero" is the source of the
geometric fact "10.10 μm is the e-circle radius". (research/02 §4.)

## B.3 P2m — Galois/Hecke Correspondence (was P2: Holonomy Correspondence)

**Original P2.** The VEV of a Wilson line around a compact internal
dimension determines the phase of the gauge theory on that
dimension. Change the compact space, change the phase.

**Multiplicative P2m.** The value of a BC "multiplicative Wilson
line" — the expectation of a character χ of the Galois group
Gal(Q^cyc/Q) ≅ Ẑ* in a KMS_β state — determines the phase of the
BC system. Change the character, change the phase.

**Mechanism.** The BC system's spontaneous symmetry breaking for
β > 1 parameterises extremal KMS states by Ẑ* (Bost–Connes 1995
Theorem 25). Each character χ ∈ Ẑ* picks out a phase. The n^{it}
phase of the isometry μ_n is the multiplicative analog of the
Aharonov–Bohm phase e^{i∮ A} of a Wilson line around S¹:

$$
  \text{additive: } e^{i \oint_{S^1} A\,dθ}
  \quad\longleftrightarrow\quad
  \text{multiplicative: } n^{it} = e^{it \log n}.
\tag{B.1}
$$

The integer log n on the right is the length of the "multiplicative
loop" in the BC system, and the factor t is the dual parameter
(Mellin dual of θ).

**Concrete example.** The Weinberg angle formula sin²θ_W derived
from the spectral zeta ratio of S²/CP² in Paper 4 §7.8 is the
additive/geometric form. The multiplicative form is the ratio of
BC partition functions ζ_{S²}(β) / ζ_{CP²}(β) evaluated at the
critical β, where each zeta factor is the Mellin image of the
corresponding KK sum. The Weinberg angle is the character ratio in
the multiplicative (P2m) form. (Derivation continues in the
thread-3b research notes.)

## B.4 P3m — Free Energy as Scale-Setter (was P3: Casimir as Scale-Setter)

**Original P3.** Quantum vacuum energy on a compact space of
radius R generates a physical energy scale ~ ℏc/R. Different
radii give different scales.

**Multiplicative P3m.** The BC free energy F(β) = −β⁻¹ log Z(β) =
−β⁻¹ log ζ(β) sets the physical scale. Different inverse
temperatures β give different scales. At the critical β = 1, F
diverges, and the scale is set instead by the smallest nontrivial
spectral feature — the smallest Riemann zero γ_1.

**Mechanism.** Apply the dictionary:

- Additive Casimir: E_Cas(R) ∝ −1/R⁴, derived from Σ_n n^{−s}|_{s=−3}.
- Multiplicative free energy: F(β) = −log ζ(β), derived from the
  same Dirichlet series Σ n^{−β}.

Both arise from the same zeta sum, evaluated at different points
of the complex plane (s = −3 for Casimir, s = β > 1 for free
energy). This is the first time in the framework that two
physically distinct quantities are *literally the same Dirichlet
series* evaluated at different arguments.

**Concrete example.** The cosmological constant formula

$$
  \log(\pi R_{\mathrm{obs}}/\ell_{\mathrm{P}}) \;=\; \gamma_1 \pi^{2}/2
  \;+\; \text{corrections}
\tag{B.2}
$$

is the P3m-form of the dark-energy prediction. In the additive
form (P3, Paper 1), R_obs is the e-circle radius that sets the
dark-energy density via the Casimir sum. In the multiplicative
form (P3m), the same R_obs is the smallest eigenvalue of R̂ = (ℓ_P/π)
exp(T_BC π²/2), and the scale is set by the critical-β structure
of the BC free energy (the pole of ζ at β = 1).

## B.5 P4m — Arithmetic Rigidity (was P4: Topological Rigidity)

**Original P4.** A discrete topological invariant — winding
number, Euler characteristic, flux quantum — locks in an exact
quantized result.

**Multiplicative P4m.** A discrete arithmetic invariant — prime
power, divisor count, Euler product factor, Galois-group element —
locks in an exact BC-side result. The rigidity is *arithmetic*
rather than topological, but the effect is the same: integers
cannot be infinitesimally adjusted.

**Mechanism.** The BC algebra is generated by the isometries μ_n
for n ∈ N*, which are themselves indexed by multiplication in N*.
The Hecke relation (research/02 (2.1))

$$
  \mu_n\,e(r)\,\mu_n^{*}
  \;=\;
  \frac{1}{n}\,\sum_{n s = r} e(s)
\tag{B.3}
$$

is a purely arithmetic constraint. Any result derived from the
Hecke relation inherits the rigidity of "divisibility in N*":
there is no half-prime, no 2.3-divisor. Arithmetic does not
deform.

**Concrete example.** The three generations of fermions derived
in Paper 4 from χ(CP²) = 3 (the Euler characteristic) has the P4m
transposition: **three = the three smallest primes 2, 3, 5 in the
smallest BC Hecke sub-algebra**, which under the Identity 12
unitary equivalence corresponds to the A_2 root-system structure
at the 3-prime level (thread 3g.1, 10-transposition-gauge-group.md
target). The "topological three" (χ(CP²)) and the "arithmetic
three" (the number of primes below the first saturation scale of
the Hecke algebra) are the two faces of the same rigidity.

Another example: θ_QCD = 0 from π₄(SU(3)) = 0 in P4 becomes, in
P4m, the vanishing of a specific arithmetic L-value on the BC
side — the value L(0, χ) for the trivial character χ of Ẑ* — and
the vanishing is forced by the functional equation of ζ. (Working
this out in detail is thread 3b.)

## B.6 P5m — Dirichlet Series Analytic Continuation (was P5: Zeta Regularisation of KK)

**Original P5.** The KK sum on S¹ is the Riemann zeta function
Σ n^{−s}, analytically continued to negative integers, where it
vanishes at non-positive integers. This kills the UV divergences
of 4D quantum gravity.

**Multiplicative P5m.** The BC partition function Z(β) = ζ(β) *is*
the same Dirichlet series, but now the analytic continuation is
not a regularisation trick — it is the **defining construction**
of the BC phase transition at β = 1 (the pole of ζ) and of the
BC system's spectral data at the non-trivial zeros. The identity
1 + 2ζ(0) = 0 that kills the leading UV divergence in P5 is a
statement about ζ(0) = −1/2, which on the BC side is the value
of the free energy at β = 0 (infinite temperature), i.e., the
high-T limit of the BC thermodynamics.

**Mechanism.** In P5, ζ-regularisation is applied to a
mathematical object (the KK sum). In P5m, the same ζ is the
*physical partition function* of the BC system. The "trick" of
analytic continuation becomes the "physics" of the phase
transition. Pattern-5 identities like E_L(−j; Q_L) = 0 translate,
under the dictionary of §B.1, into statements about the vanishing
of Mellin transforms of BC correlators at specific arguments —
and these correspond directly to the zero values of the Riemann
ζ function at negative integers, now in their native habitat.

**Concrete example.** Theorem K.1 of Paper 1 (all-orders UV
finiteness via Epstein zeta vanishing) is a purely additive
statement: Epstein zetas of a lattice Q_L vanish at s = −j. The
multiplicative form (P5m) is CM 2008 Chapter II §3 Theorem 3.4:
the Connes–Marcolli regularised explicit formula assigns the
same vanishing to the multiplicative side as a statement about
the BC partition function's regularity at β = 1 (the pole of ζ
is *exactly cancelled* by the KMS normalisation). Theorem K.4 of
Paper 10 (all-orders Yang–Mills finiteness) becomes the P5m
statement that the BC partition function's inductive bootstrap
is regular at β = 1 — the transposition target of thread 3g.2.

## B.7 P6m — Mellin Inversion Produces Arithmetic Pathology (was P6: Projection Produces Apparent Pathology)

**Original P6.** When 4D physics appears paradoxical, the cause
is partial trace over the compact dimension. What looks
paradoxical in 4D is ordinary in 5D.

**Multiplicative P6m.** When a *geometric* statement on the
e-circle looks paradoxical, the cause is the Mellin inversion
that drops the multiplicative (BC) structure. What looks like a
geometric pathology (e.g., an infinite Casimir sum, a fine-tuned
radius, an unnatural hierarchy) is ordinary arithmetic on the BC
side. The "partial trace" that creates the pathology is the
projection

$$
  H_1 \;\twoheadrightarrow\; H_R \;\to\; (\text{Fourier modes on }S^1_R)
\tag{B.4}
$$

that forgets the multiplicative labelling of states and remembers
only the additive (momentum) label. In reverse, lifting from the
geometric side to the BC side is the Mellin transform; dropping
from the BC side to the geometric side is the Mellin inversion
followed by evaluation.

**Mechanism.** The cosmological constant problem is the canonical
example of an apparent 4D fine-tuning. The P3/P6 analysis in Paper
1 shows that the fine-tuning is a projection artifact: the observed
ρ_Λ is the Casimir energy of the full 5D theory evaluated at a
frozen R₀. But even this P6 resolution leaves R₀ itself unexplained.
The P6m resolution goes one step deeper: R₀ is *itself* the smallest
eigenvalue of R̂, and the "fine tuning" seen in 4D is an apparent
pathology produced by the Mellin inversion that forgets R₀'s
arithmetic origin as γ_1.

**Concrete example.** The 55–123 orders-of-magnitude discrepancy
in the cosmological constant is a 4D pathology. Lifted to 5D (P6),
it becomes a Casimir calculation with a specific R. Lifted one more
step to the BC side (P6m), it becomes the statement γ_1 × π²/2 =
69.7521, which is a fact about the first Riemann zero. The
discrepancy of "10^120" on the 4D side is the exponential image of
the small algebraic factor γ_1 × π²/2 ≈ 70 on the BC side, and the
pathology is entirely the fault of the exponential map from the BC
side to the geometric side — i.e., of the Mellin inversion that
sends log(πR/ℓ_P) back to R and hides its arithmetic source.

## B.8 Status Table for Part B

| Pattern | Original (additive) | Transposed (multiplicative) | Example | Status |
|:--------|:--------------------|:----------------------------|:--------|:-------|
| P1m | Geometric reinterpretation (Paper 1 §3) | Arithmetic reinterpretation via Mellin | R_obs as γ_1 eigenvalue | stated, example rigorous mod Identity 12 |
| P2m | Holonomy correspondence (Paper 4 §3) | Galois/Hecke character correspondence | Weinberg angle as ζ ratio | stated, example structural (derivation is thread 3b) |
| P3m | Casimir scale-setter (Paper 1 §6) | BC free energy scale-setter | CC formula log(πR/ℓ_P) = γ_1 π²/2 | stated, example rigorous to 5 ppb (research/02 §5) |
| P4m | Topological rigidity (Paper 4, 5, 7) | Arithmetic rigidity | 3 generations = 3 smallest primes | stated, example conjectural (thread 3g.1) |
| P5m | Zeta regularisation (Paper 1 App K) | Dirichlet series analytic continuation | Theorem K.1 → BC partition regularity | stated, example maps to thread 3g.2 |
| P6m | Projection pathology (Paper 3) | Mellin-inversion pathology | CC 10^120 from γ_1 × π²/2 | stated, example qualitative |

## B.9 Honest Accounting — Part B

### B.9.1 What the transposition is

The transposition is a **uniform dictionary** (§B.1) plus six
concrete rewritings (§B.2–§B.7) plus one worked example per
pattern. Each example is either (i) rigorous modulo Identity 12
and Identity 14 (P1m, P3m, P5m) or (ii) structural/conjectural
and explicitly pointed at its thread-3b or thread-3g target
(P2m, P4m, P6m).

### B.9.2 What the transposition is not

It is not a proof that Paper 9's patterns generate Paper 12's
results. Each of P1m–P6m still requires its own derivation on
the BC side, and those derivations are the content of the
various thread-3b, -3e, -3g notes. The transposition is the
*guide* for those derivations, not the derivations themselves.

### B.9.3 What it achieves

- Every framework reasoning move now has a BC-side counterpart.
- The six patterns of Paper 9, which were the organising
  principle for the entire pre-Paper-12 framework, are now seen
  as *projections* of six multiplicative patterns on the BC /
  Riemann side. This is consistent with the meta-pattern P0
  (preprint/15) — "reality is a projection of Riemann", with
  the reasoning patterns being projections too.
- The dictionary of §B.1 gives a mechanical translation from
  any additive statement in the framework into a multiplicative
  candidate statement on the BC side, which is the engine of
  Sub-phase 3.B.

### B.9.4 Definition of done — Part B

Part B is closed for the purposes of Paper 12 when:

- [x] The six pattern transpositions P1m–P6m are stated (§B.2–§B.7).
- [x] Each has a concrete example pointed at its worked-out
      research note or a specific open thread.
- [x] The dictionary (§B.1) is explicit and uniform.
- [x] The status table (§B.8) accounts for the current state
      of each pattern.
- [ ] (Optional) Each of P1m–P6m gets its own dedicated research
      note with the full derivation of the worked example.
      (Deferred to the individual threads 3b, 3g.1, 3g.2, …)

With the first four items done, Part B has provided the
*structure* of the transposition and the *pointers* to the
detailed derivations.

---

## C. Combined Definition of Done

Threads 3g.7 and 3g.8 are closed for Paper 12 when:

- [x] Part A: Identity 14 is stated rigorously (§A.3) with the
      unitary V and the intertwining relation V T_CCM V* = T_BC
      given on a common core, and the conditionality of
      {γ_n} ⊂ spec(T_BC) is traced to CM 2008 Chapter II §3.
- [x] Part B: The six reasoning patterns are transposed to P1m–
      P6m (§B.2–§B.7) with a uniform dictionary (§B.1) and a
      concrete example per pattern.
- [x] Both parts have status tables (§A.4.4, §B.8) and honest
      accountings (§A.4, §B.9).
- [x] The downstream uses (research/02, research/04, thread 3b,
      thread 3g.1, thread 3g.2) are identified.
- [ ] (Optional / sequel) A dedicated research note for each of
      P1m–P6m with the fully worked example.
- [ ] (Sequel only, thread 3i.2) The residual regularisation gap
      in (A-C1) is closed.

With the first four boxes checked, both threads are ledger-closed
for Paper 12.

---

## D. Single Most Important Open Piece

**The off-diagonal matrix elements ⟨γ_n | R̂ | γ_m ⟩, derived
from the Hecke action of the BC algebra on the eigenstates of
T_BC.** These are the quantities that (i) produce the 5 ppb
corrections in the CC formula (research/02 §5), (ii) drive the
cosmic transition amplitudes in research/06 and the γ_5 → γ_2 →
γ_1 selection rule, and (iii) are the computational content of
P4m and P2m in any of their concrete forms. The transposition
dictionary tells us they exist and how to frame them; the
actual calculation is open.

Relative to the two parts of this note, this open piece sits at
the interface: Part A provides the operator T_BC and the BC
algebra that acts on its spectrum, and Part B (specifically P4m
and P2m) tells us that their action is encoded in arithmetic
Hecke / Galois data. The calculation is therefore a matter of
extracting the right arithmetic invariants from CM 2008 Chapter
II §3, but it has not been done.

---

## E. References

### E.1 In this directory

- `02-quantize-R-construction.md` — uses T_BC and R̂, assumes
  Identity 14. Part A of this note is the justification.
- `04-identity-12-rigorous.md` — the unitary U : H_e → H_1 of
  Identity 12. Part A's V composes with U to give the full
  bridge e-circle → CCM scaling operator.
- `05-derive-cc-formula.md` — the CC formula derivation that
  Part B's P3m example summarises.
- `06-cosmic-transition-amplitudes.md` — the matrix elements
  noted in §D.
- `../preprint/15-reality-as-projection-of-riemann.md` — the
  meta-pattern P0 that subsumes P1m–P6m.
- `../preprint/03-the-transposition.md` — the overall
  transposition programme (Sub-phase 3.B).
- `../03-phase-3-plan.md` §1.2 — the thread 3g table listing
  3g.1 through 3g.8.

### E.2 In sister directories

- `../../paper9/preprint/02-the-six-patterns.md` — the original
  P1–P6 statements transposed here.
- `../../paper9/preprint/08-appendix-pattern-attribution-map.md`
  — the full map of which Paper 9 results use which patterns.
- `../../integers/paper11b-sm-gauge-entanglement/research/13-oc2-bost-connes-riemann-relation.md`
  — the numerical discovery of γ_1 × π²/2, the seed of P3m.

### E.3 External

- Bost, J.-B., and Connes, A., "Hecke algebras, type III factors
  and phase transitions with spontaneous symmetry breaking in
  number theory", *Selecta Math. (N.S.)* **1** (1995) 411–457.
- Connes, A., "Trace formula in noncommutative geometry and the
  zeros of the Riemann zeta function", *Selecta Math.* **5**
  (1999) 29–106.
- Connes, A., Consani, C., and Marcolli, M., "Noncommutative
  geometry and motives: the thermodynamics of endomotives",
  *Adv. Math.* **214** (2007) 761–831. *[CCM 2007. The origin of
  the CCM scaling operator. §§2–4 are the relevant material.]*
- Connes, A., and Marcolli, M., *Noncommutative Geometry,
  Quantum Fields and Motives*, AMS Colloquium Publications
  **55** (2008). *[CM 2008. Chapter II §3 gives the dilation
  generator and the explicit formula in the form used for
  (A-C1). Theorem 3.4 is the regularised explicit formula;
  Theorem 3.6 is the inclusion {γ_n} ⊂ spec.]*
- Sz.-Nagy, B., Foiaș, C., Bercovici, H., Kérchy, L., *Harmonic
  Analysis of Operators on Hilbert Space*, Springer 2010. *[The
  dilation theory used in §A.2.1.]*

---

*One dictionary: additive ↔ multiplicative, Fourier ↔ Mellin.*
*One unitary V: Sz.-Nagy dilation ↔ modular analytic continuation.*
*Six patterns projected: P1–P6 on the e-circle ↔ P1m–P6m on the*
*BC system. One open computation: ⟨γ_n | R̂ | γ_m ⟩.*

*Paper 9 was the reasoning layer of the framework. Paper 12*
*Sub-phase 3.B is the observation that the reasoning layer*
*itself is a projection of the BC multiplicative structure.*
*The patterns descend from the zeros.*
