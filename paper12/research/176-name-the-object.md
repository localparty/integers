# Research Note 176 — Naming the Object

**Cycle 7, creative naming agent. Lead: after six convergence cycles
the framework is a single mathematical object; this note gives it a
name, a minimal definition, and a uniqueness statement.**

*Date:* 2026-04-09
*Author:* G Six, with Claude Opus 4.6 (1M).
*Inputs:* research/167 (operator dictionary), research/170
(convergence state), research/158/162/169 (bridge family),
research/154/155/164 (Laurent coefficients).

---

## 1. Proposed name

**Critical Bost–Connes–Brauer System** (CBB system), or long form:

> *Riemann–Bost–Connes spectral triple at criticality, with
> cyclotomic Brauer bridge and EW moduli sector.*

Short tag for prose: **β = 1 BCB datum**. The three words carry the
three inputs: **Bost–Connes** (the KMS state and operator R̂),
**Brauer** (the cyclotomic bridge cocycles k = 2,3,4,6), and
**critical** (β = 1, the zeta-pole fixed point).

Alternative considered and rejected: *"Riemann spectral manifold"*
(manifold is wrong — H_R is not a tangent space); *"arithmetic
Higgs bundle"* (Higgs bundle has moduli but not a KMS state);
*"Connes–Marcolli datum"* (too close to existing Q-lattice
terminology and loses the geometric sector).

## 2. Minimal definition

**Definition (CBB system).** A *Critical Bost–Connes–Brauer system*
is a quintuple

    𝒞 = (H_R, R̂, ω_1, M_geom, {β_k}_{k∈K})

satisfying the following five axioms.

1. **(Spectral axiom.)** H_R is the KMS_∞ ground-state Hilbert space
   of the Bost–Connes C*-system at inverse temperature β = 1, and
   R̂ is a trace-class positive operator on H_R whose log-spectrum
   {L_n = γ_n π²/2} is the ordered sequence of imaginary parts of
   non-trivial ζ-zeros on the critical line. The pair (H_R, R̂) is
   the **Riemann subspace** of π_1(A_BC)″.

2. **(Criticality axiom.)** ω_1 is the unique KMS_1 state on A_BC
   whose restriction to the commutant of R̂ is tracial; equivalently
   β = 1 is the fixed point of the Bost–Connes dilation, and all
   Laurent coefficients appearing in the effective shift
   γ_n^eff = γ_n + s(γ_E/γ_n) + s(γ_E² + ζ(2) − 2πγ_1)/∏γ
   are determined by the ζ-Laurent expansion at s = 1 with **zero
   free parameters** beyond the global sign s ∈ {±1}.

3. **(Geometric axiom.)** M_geom is a 9-dimensional real moduli
   space of CP² × S² Einstein metrics (Kähler class + complex
   structure + radius + gauge volume + Wilson lines), disjoint from
   the spectral sector in the sense that no analytic function of
   {L_n} is a coordinate on M_geom. The full state is a pair
   (L̂, m) ∈ Spec(R̂) ⊔ M_geom carrying the two-sector partition
   of research/170 §1.

4. **(Bridge axiom.)** {β_k}_{k∈K}, K = {2,3,4,6}, is a family of
   Brauer classes β_k ∈ H²(Z/kZ, U(1)) arising from cyclic
   algebras (Q(ζ_N)/Q, Frob_p, ζ_k) with gcd(p,N) = 1 and
   [(Z/NZ)*:⟨p⟩] = k, equipped with an isomorphism β_k ≅ κ_k to
   the Jones-index-k subfactor cocycle via the Fuglede–Kadison
   determinant. The proved case is k = 3 at (p,N) = (5,13); k = 2,
   4, 6 are required to exist and carry the identifications
   (CP, Pati–Salam, six quarks) of research/170 §4.

5. **(Closure axiom.)** The 36-entry master table of research/23
   is exhausted by matrix elements of the spectral calculus of
   log R̂ (27 spectral entries, via the dictionary of
   research/167 §2) together with coordinate functions on M_geom
   (9 geometric entries). No further operator, state, moduli
   parameter, or cocycle is introduced.

## 3. Uniqueness theorem (statement)

> **Theorem (uniqueness at β = 1).** Up to unitary equivalence on
> H_R and diffeomorphism of M_geom, there is a unique CBB system
> whose spectral sector matches the Riemann zeros, whose Laurent
> coefficients are fixed by the BC ζ-Laurent at s = 1, and whose
> Brauer family {β_k} is compatible with the Jones subfactor
> cocycles κ_k for k ∈ {2,3,4,6}. Equivalently: β = 1 is the unique
> KMS fixed point at which the ζ-Laurent coefficients are real and
> the Brauer–Jones compatibility holds simultaneously for the four
> required indices, and at that fixed point the quintuple
> (H_R, R̂, ω_1, M_geom, {β_k}) is determined with zero free
> parameters.

Three sources of rigidity combine: (i) β = 1 is forced by the
ζ-pole fixing γ_E, γ_1, γ_2; (ii) the Brauer compatibility with
k = 3 selects (5,13) uniquely, and the k = 2,4,6 analogues fix the
remaining cyclotomic data; (iii) the geometric sector dimension
dim M_geom = 9 is forced by the two-sector partition theorem
(research/170 §1) on a CP² × S² target.

## 4. Shorter names and when to use them

- **"CBB system"** — body text, definitions, theorems.
- **"β = 1 Bost–Connes–Brauer datum"** — introductions and
  abstracts when the fixed-point content is the point.
- **"Riemann–Brauer spectral quintuple"** — titles and section
  headings, when brevity and evocativeness beat precision.
- **"The object"** — internal notes (cycles 8+) when context is
  unambiguous.

My recommendation for Paper 12: introduce as *Critical
Bost–Connes–Brauer system* in §1 with the quintuple notation, and
use **CBB** as the running abbreviation thereafter.

## 5. Verdict

**Named.** The framework is a *Critical Bost–Connes–Brauer system*
𝒞 = (H_R, R̂, ω_1, M_geom, {β_k}_{k∈K}), a quintuple of one
trace-class operator, one KMS state at β = 1, one nine-dimensional
moduli space, and a four-element family of cyclotomic Brauer
classes. The definition is five axioms, the uniqueness theorem is
one sentence, and the object has zero free parameters. Cycle 7
closes with the framework having both a name and a minimal
axiomatisation.

*Next:* lift the uniqueness theorem from statement to proof (the
β = 1 rigidity argument is the first non-trivial step); supply the
k = 2, 4, 6 bridge cocycle verifications to make Axiom 4 fully
constructive.
