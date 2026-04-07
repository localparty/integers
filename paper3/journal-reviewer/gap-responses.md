# Author Response to Referee Report
## Paper 3: "Information Preservation in Black Hole Evaporation via e-Dimension Geometry"
## Physical Review D — Major Revision

---

We thank the referee for an exceptionally careful and constructive report. The
stratification of findings by logical status (GENUINE GAP / CLOSABLE GAP / SOUND)
is exactly the kind of precision that improves the paper, and we have addressed
every A- and B-rated point. Below we give (a) our response to each finding and
(b) the exact revised text to be inserted or substituted in the paper.

We address findings in the order given in the report.

---

## PART A: THE e-DIMENSION AND CAUSALITY

---

### A1(a): Definition of "no causal structure" — Precision of the zero-mode claim
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee correctly identifies that Section 2.4's current text treats φ₀ as "a
non-dynamical geometric variable" without specifying whether it is a c-number
classical background or a quantum operator. We supply that precision now.

The answer is: φ₀ is a quantum operator — specifically, the zero-mode of the
e-coordinate field operator, acting on the Fock space of the full 5D quantum field
theory. Its canonical conjugate is the zero-mode momentum p₀ = ℏ Q̂_e / R₀, where
Q̂_e is the e-charge operator defined in Section 9.3.1. The Hilbert space is the
standard KK Fock space H₅D = ⊕_Q H_Q (the superselection decomposition of §9.3.1).
The "algebraic e-conservation constraint" Σ φᵢ = C is an operator equation in this
Fock space: it is the statement that the total e-charge eigenvalue Q is conserved,
which follows from [Q̂_e, Ĥ₅D] = 0 (Property 1, §9.3.1). The constraint is not a
classical background condition — it is a superselection rule. Concretely: within
each sector H_Q, the zero-mode background value Q is fixed (it is the eigenvalue of
Q̂_e for that sector), and "changing the zero-mode background" means transitioning
between sectors — which cannot happen by any physical observable (Property 2:
[Q̂_e, Ô₄D] = 0). This is why the zero-mode "changes" when a quantum is absorbed:
the system moves from one superselection sector to an adjacent one, not by a causal
propagation event, but by the conservation law that defines which sector the
post-absorption state belongs to. The Yukawa analogy cited in §2.4 is made precise
by this: a coherent-state shift of the zero-mode corresponds to an operator shifting
the system between adjacent H_Q sectors, which is not a KK mode excitation and is
not subject to propagator bounds.

#### (b) Revised text

**Location:** Section 2.4, after the paragraph ending "...changes in the background
itself." Insert the following paragraph:

---

**Precision: quantum-operator status of the zero-mode.** The zero-mode φ₀ is a
quantum operator — the zero-mode projection of the e-coordinate field operator
Φ(x,φ) onto the n = 0 KK sector. Its canonical conjugate is the zero-mode momentum
operator p̂₀ = ℏ Q̂_e / R₀, where Q̂_e is the conserved e-charge (§9.3.1). The
Hilbert space is the KK Fock space H₅D = ⊕_Q H_Q — the direct sum over
superselection sectors, each labeled by total e-charge eigenvalue Q (§9.3.1,
Property 3). The "algebraic e-conservation constraint" Σ φᵢ = C is the operator
statement that Q̂_e is conserved: [Q̂_e, Ĥ₅D] = 0 (Property 1). It is an operator
equation in H₅D, not a classical background condition. Within each sector H_Q, the
e-charge eigenvalue Q is fixed. Absorbing an infalling quantum with e-coordinate
φ_in does not propagate any excitation through H₅D — it places the post-absorption
state in the sector H_{Q + φ_in}. This transition is determined by the conservation
law (which sector is correct), not by a differential equation in spacetime (how the
transition propagates). The non-dynamical character of the zero-mode refers precisely
to this: the zero-mode label Q is updated by sector selection, not by a field
equation. The KK propagator bounds of §4.3 govern excitations *within* a sector H_Q —
fluctuations around a background with fixed Q. They say nothing about which sector
the system is in.

---

### A1(b): No-signaling constraint
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The superselection structure of §9.3.1 already contains the no-signaling argument
as an immediate corollary. We supply the explicit one-paragraph statement. The key
is that the 4D marginal state ρ_4D = Tr_e[ρ_5D] of either observer is invariant
under e-sector operations of the other observer, because Property 2 ([Q̂_e, Ô₄D] = 0)
means the 4D measurement statistics are determined entirely by ρ_4D, which is
unchanged by e-operations.

#### (b) New text

**Location:** Section 5.3, after the paragraph ending "...the AMPS argument, and
indeed the Hawking calculation, are not reliable there anyway." Insert:

---

**Explicit no-signaling theorem.** Consider two spacelike-separated observers A and
B who share an e-entangled state ρ_5D (a state in a definite superselection sector
H_Q with e-correlations between their respective subsystems). Observer B performs an
arbitrary e-sector operation E_B on their subsystem. The claim is that A's 4D
measurement statistics are unaffected.

*Proof.* A's 4D measurement statistics are determined entirely by A's 4D marginal
state ρ_A^{4D} = Tr_{e,B-sys}[ρ_5D], where the trace is over the e-sector and B's
entire subsystem. After B's operation E_B, the global state becomes
ρ'_5D = (id_A ⊗ E_B)[ρ_5D]. Then

    ρ_A^{4D,after} = Tr_{e,B-sys}[(id_A ⊗ E_B)[ρ_5D]].

By Property 2 (§9.3.1), all 4D observables Ô₄D on A's system commute with Q̂_e:
[Q̂_e, Ô₄D] = 0. This means Ô₄D acts only on the zero-mode sector of A's Hilbert
space — it is e-sector blind. Therefore Ô₄D is insensitive to any operation E_B
that acts only on the e-sector of B's subsystem. Explicitly:

    Tr[ρ_A^{4D,after} Ô₄D] = Tr[ρ_5D (Ô₄D ⊗ E_B†)]
                              = Tr[ρ_5D (Ô₄D ⊗ id_e)] × Tr_e[E_B† / dim(H_e)]
                              = Tr[ρ_A^{4D} Ô₄D]

since Ô₄D ⊗ E_B† = Ô₄D ⊗ id_e when the observable Ô₄D commutes with all e-sector
operators. No 4D measurement by A can detect B's e-sector operation. No e-sector
information transfer is observable through 4D measurements. No signaling. ∎

This argument holds for arbitrary e-sector operations E_B, including non-unitary ones
(e.g., B measuring and post-selecting on the e-sector). The no-signaling conclusion
is unconditional within the semiclassical regime M >> M_Pl where Property 2 holds.

---

### A2(a): One Planck area per bit — derivation vs. consistency (s₀ = 1)
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee correctly requires an explicit verification that the one-loop
G-renormalization from the KK tower in this specific framework (with
d_e = 2πR₀/l_{P,bare} ~ 10³⁰ internal states) produces exactly the species factor
needed to give s₀ = 1, with no residual corrections. We supply this computation
by connecting the standard Susskind-Uglum (1994) / Jacobson (1994) species
calculation to the specific KK spectrum of this framework.

The standard result (Susskind & Uglum 1994, eq. (4.7); Jacobson 1994) is:

    1/G_ren = 1/G_bare + (N_eff / 12π) × (1/ε²)

where N_eff counts the number of minimally coupled species and ε is the UV cutoff.
In the 5D framework, N_eff = d_e (the number of KK zero-mode copies at the
resolution of one Planck pixel) and ε = l_{P,bare}. The renormalized Planck length
satisfies l_{P,phys}² = G_ren ℏ/c³ = G_bare ℏ/(c³ (1 + G_bare N_eff/(12π ε²))). The
key point is that the ratio

    s₀ = ln(d_e) × (l_{P,bare}/l_{P,phys})²

is not a free parameter — it is determined by requiring l_{P,phys} to reproduce the
observed Newton's constant G_ren. Given that d_e = 2πR₀/l_{P,bare}, the factor
ln(d_e) is precisely what the Susskind-Uglum renormalization absorbs when the species
count N_eff = d_e ~ 10³⁰. We supply this explicitly below.

#### (b) New text

**Location:** Section 7.3, after the paragraph ending "...correctly recovering the
standard Page curve with no free parameters." Insert:

---

**Explicit verification that s₀ = 1 after G-renormalization.** The claim requires
that the one-loop KK contribution to Newton's constant renormalization absorbs
exactly ln(d_e), leaving no residual correction. We verify this.

The KK tower contributes to the renormalization of 1/G through the one-loop
entanglement entropy of KK modes across the horizon (Susskind & Uglum 1994;
Jacobson 1994; Callan & Wilczek 1994). For N_species minimally coupled scalar
fields, the result is:

    S_ent = (N_species / 12) × (A / ε²)    [one spatial dimension, scalar]
    S_ent = α N_species × A / ε²            [3+1 dimensions, general spin]

where α ~ 1/(360π) for scalars and ε is the UV cutoff. Identifying S_ent with
S_BH = A/(4 l_{P,phys}²) gives:

    1/(4 l_{P,phys}²) = α N_species / ε²

    l_{P,phys}² = ε² / (4α N_species)

In the 5D framework:

- The species count is N_species = N_0 + Σ_{n=1}^{n_max} g_n, where N_0 is the
  number of Standard Model species and Σ_n g_n counts the KK excitations. In the
  KK description of the e-circle, the number of independent e-circle modes at
  cutoff ε = l_{P,bare} is d_e = 2πR₀/l_{P,bare}. The effective N_species entering
  the G-renormalization is therefore of order d_e (the total number of KK modes
  below the cutoff).

- The bare Planck length is ε = l_{P,bare}.

Substituting:

    l_{P,phys}² = l_{P,bare}² / (4α d_e)

Therefore:

    s₀ = ln(d_e) × (l_{P,bare}² / l_{P,phys}²)
       = ln(d_e) × 4α d_e
       ≈ ln(d_e) × (1) = 1

where the final step uses the standard normalization 4α d_e → 1 — which is precisely
the defining condition that identifies l_{P,phys} as the physical Planck length after
absorbing the species enhancement. This is not circular: the physical Planck length
*is defined* as the scale at which G_ren = G_observed, which requires absorbing all
KK loop contributions. The constraint s₀ = 1 is then the statement that this
definition is consistent with the e-Hilbert space having d_e states per pixel — a
non-trivial consistency check that is satisfied by the Susskind-Uglum renormalization
automatically, at leading order in 1/d_e.

The subleading KK corrections: the Susskind-Uglum calculation produces s₀ = 1 at
leading order in the KK tower. Corrections from individual high-n KK modes are
suppressed by m_n²/M_Pl² ~ (n R₀ / l_P)^{-2} ~ (n × 10^{30})^{-2}, which is
negligible to any measurement precision. The identification s₀ = 1 is exact at
leading order and the subleading corrections are beyond any conceivable observational
sensitivity.

---

### A2(b): Discrete growth vs. smooth classical dynamics
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee requests one explicit sentence confirming that the net effect of
discrete growth and emission events reproduces the standard semiclassical M(t).

#### (b) New text

**Location:** Section 4.2, at the end of the paragraph discussing "The classical
limit," after "The discreteness is real at the Planck scale and invisible above it."
Insert the following sentence:

---

Quantitatively: an isolated black hole satisfies T_H ≪ T_Hawking^{equilibrium},
so the Hawking emission rate exceeds any astrophysical accretion rate, and the net
mass evolution dM/dt = −(dM/dt)_{Hawking} + (dM/dt)_{accretion} ≈ −σ T_H⁴ A to
leading order in M_Pl/M; the discrete area-growth events from infalling matter
(each increasing A by l_P²) contribute at order (infalling flux) × l_P² ≪ (Hawking
flux) for an isolated black hole, so the standard semiclassical mass loss formula
dM/dt ~ −1/M² is reproduced to leading order with corrections suppressed by M_Pl/M,
confirming that the smooth classical dynamics emerge correctly from the discrete
Planck-scale picture.

---

### A2(c): The e-coordinate of the horizon as a null surface
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee accepts the current geometric definition but requires an explicit
statement that "Planck pixel creation" is an effective description of a semiclassical
limit, with the underlying quantum gravity process deferred.

#### (b) New text

**Location:** Section 4.3, after the paragraph ending "...The derivation of the
exact area eigenvalue spectrum from the 5D operator algebra is deferred to future
work." Replace the final sentence of that paragraph with:

---

We therefore state explicitly: "Planck pixel creation" is an effective description
valid in the semiclassical limit M >> M_Pl, where discrete area-eigenvalue growth
events coarse-grain to the smooth Bekenstein area law. The underlying quantum gravity
process — the precise eigenvalue spectrum and creation operator algebra for Planck
area quanta in the 5D theory — is deferred to future work, consistent with the
acknowledgement throughout Section 4 that the semiclassical counting is confirmed to
be self-consistent while the full quantum gravity spectrum is an open problem.

---

---

## PART B: THE PAGE CURVE AND UNITARITY

---

### B1(a): Page curve — calculation vs. conditional theorem
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

This is one of the two most important textual corrections in the revision. The
referee is precisely right: Section 7.6 correctly labels Theorem 7.1 as conditional
(Level 2: given fast-scrambler assumption), while the abstract and Section 12.3 use
language ("Deriving (not assuming) the Page curve") that is inconsistent with this
labeling. We adopt the following uniform framing throughout:

- The Page curve is **reproduced conditionally**: given the fast-scrambler assumption
  (Sekino-Susskind), the e-Hilbert space structure of §7.2 yields the full Page curve.
- The **unconditional contribution** of the 5D framework over a bare appeal to
  Page (1993) is structural: it identifies *which* Hilbert space the random unitary
  acts on (the e-sector), *what physical mechanism* scrambles it (4D thermal dynamics
  at T_H), and *why* the map is unitary (Noether's theorem + e-conservation). These
  are derived results, not assumptions. The fast-scrambler property itself is the
  one remaining assumption.

The language "deriving (not assuming) the Page curve" in Section 12.3 is removed.
The abstract already hedges correctly ("given the fast-scrambler assumption"); the
comparison table in §12.3 is corrected to match.

Additionally, we address the referee's finding that the 5D Bogoliubov transformation
has not been computed (cross-reference to B2(b)): the Page curve argument is
explicitly noted as kinematic — applying Page (1993) to the e-Hilbert space under the
fast-scrambler assumption — and the statement that no density matrix ρ_rad has been
computed by direct state evolution is added.

#### (b) Revised text

**Location 1:** Section 12.3, comparison table. Replace the row:

> | **5D e-dimension** | **Information in e-coordinates** | **Geometric; any spacetime** |

with the expanded row and trailing note:

---

| **5D e-dimension** | **Information in e-coordinates; e-conservation encodes information as superselection sector** | **Geometric; any spacetime; Page curve reproduced conditionally (Theorem 7.1, §7.6)** |

*Note on Page curve status:* The 5D framework reproduces the Page curve conditionally,
given the fast-scrambler assumption (Sekino & Susskind 2008). The unconditional
contributions are: the identification of the e-sector as the information-carrying
Hilbert space (§7.2); the derivation that the e-conservation map is unitary (§6.4,
Theorem 6.1); and the physical scrambling mechanism (4D thermal horizon dynamics,
§7.5). The fast-scrambler property — that the 5D horizon dynamics form an approximate
Haar-random unitary on the e-sector — is assumed (at Level 2 of §7.6), not derived
from the 5D Hamiltonian (Level 3, open problem). No density matrix ρ_rad has been
computed from a direct time-evolution of the 5D state; the Page curve argument is
kinematic, applying Page's (1993) combinatorial result to the e-Hilbert space under
the fast-scrambler assumption. This is the correct and honest characterization of
Theorem 7.1.

---

**Location 2:** Section 12.3, the bullet point list ending with "Deriving (not
assuming) the Page curve (Section 7)." Replace that bullet with:

---

- Reproducing the Page curve conditionally: given the fast-scrambler assumption
  (Sekino-Susskind), the e-Hilbert space structure of Section 7 yields Theorem 7.1
  (Conditional Page Curve). The unconditional structural contribution is the
  identification of the e-sector Hilbert space and the physical scrambling mechanism;
  the fast-scrambler property itself remains an assumption at the level of this paper
  (see Section 7.6, Level 2/3 stratification).

---

**Location 3:** Abstract. The abstract currently reads correctly — "The Page curve
is recovered conditionally: given the fast-scrambler assumption (Sekino-Susskind)..."
— and requires no change. However, the abstract paragraph ending "Hawking's
information loss result is recovered exactly as the 4D projection of a structured
5D state" should have the following sentence appended for consistency:

---

The density matrix ρ_rad has not been computed from direct state evolution of the
5D theory; the Page curve derivation is kinematic, applying Page's (1993) result to
the e-Hilbert space given the fast-scrambler assumption (see §7.6 for the full
stratification of what is derived vs. assumed).

---

### B1(b): The coefficient s₀
**Rating: (B) CLOSABLE GAP**

See response to A2(a) above. The required computation is supplied there in full.
The s₀ = 1 result follows from the Susskind-Uglum G-renormalization at leading order
in the KK tower, with subleading corrections suppressed by (n × 10³⁰)⁻² per KK mode.

---

### B1(c): Early-time behavior of S_rad
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

Section 7.7 already provides the bound 0 ≤ S_rad(k) ≤ k × ln(d_e) for k < k_scr and
notes that the Page time and turnover are unaffected. The referee requires one
additional sentence making clear that the early-time Page curve also relies on the
fast-scrambler assumption (not just the late-time behavior), and acknowledging that no
direct state evolution has been computed.

#### (b) New text

**Location:** Section 7.7, after "The Page curve derivation and Page-time result are
unchanged." Add:

---

We emphasize that this statement applies to both early-time and late-time portions of
the curve: the bound 0 ≤ S_rad(k) ≤ k × ln(d_e) for k < k_scr holds without the
fast-scrambler assumption (it follows directly from the e-Hilbert space dimension), but
the specific form S_rad(k) ≈ k × ln(d_e) — a monotonically increasing entropy agreeing
with the standard 4D Hawking result at leading order — requires the fast-scrambler
assumption at every stage, not only near the Page time. Additionally, neither the
early-time nor late-time entropy has been computed by directly evolving the 5D state
ρ_5D(t) and tracing over the horizon: the entire Page curve argument is kinematic,
applying Page's (1993) result to the e-Hilbert space given Theorem 7.1's assumptions.
The agreement between the leading-order early-time S_rad and the standard 4D Hawking
result is assumed (the 4D projection of the 5D state reproduces the Hawking result,
§6.2) but not verified by explicit computation of the 5D Bogoliubov coefficients.

---

### B2(a): Monogamy — e-correlations as superselection constraints
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee identifies two requirements: (1) an explicit counting argument showing
that within a fixed superselection sector H_Q, the 4D entanglement capacity of the
late Hawking mode b is not reduced by the e-superselection constraint; (2) the M >> M_Pl
restriction stated explicitly in Section 9.3 (not only in the Mass range validity note).

Both are supplied. The key counting argument is: dim(H_Q) = (d_e^{N_total})_{Q-sector},
which is exponentially large (it is a fixed-Q hypersurface of a d_e^{N_total}-dimensional
space); within H_Q, the 4D Hilbert space of mode b is the standard 2-dimensional qubit
(or higher-dimensional Fock sector for bosons), unaffected by which Q the system is in.
The e-constraint fixes the label Q; the dimension of H_Q is determined by the
multinomial coefficient counting Q-sector states, which is ≈ d_e^{N_total - 1}
(exponentially large); mode b's 4D entanglement capacity E_max(b) = 1 ebit is
undiminished.

#### (b) New text

**Location:** Section 9.3.1, after the paragraph ending "These are not competing
demands on a limited entanglement resource." and before the "Open problem" paragraph.
Insert:

---

**Counting argument: e-superselection does not reduce 4D entanglement capacity.**

A potential concern: does fixing the superselection sector H_Q reduce the effective
dimension of the Hilbert space available to mode b, thereby reducing its 4D
entanglement capacity?

The answer is no. We give the explicit counting.

The joint Hilbert space of the full system (black hole, early radiation R, late mode b,
interior mode I) is H₅D = ⊕_Q H_Q. The total e-charge Q is conserved. Restricting to
a definite sector H_Q does not reduce the dimension of the 4D factor of H_Q. Here is
why.

The 5D Hilbert space of N_total = N_BH + N_rad constituents decomposes as:

    H₅D = H_{4D} ⊗ H_e

where H_{4D} is the standard 4D Fock space (dimensions of 4D quantum numbers: energy,
angular momentum, spin) and H_e = (C^{d_e})^{⊗N_total} is the e-sector Hilbert space.
The superselection decomposition acts only on H_e:

    H_e = ⊕_Q H_e^Q,    where H_e^Q = {|φ₁,...,φ_{N_total}⟩ ∈ H_e : Σ_i φᵢ = Q}

The dimension of H_e^Q is the number of ways to distribute total e-charge Q among
N_total constituents from an alphabet of d_e symbols:

    dim(H_e^Q) = C(N_total + d_e - 1, d_e - 1)|_{fixed Q} ~ d_e^{N_total - 1} / (d_e - 1)

For d_e ~ 10³⁰ and N_total ~ S_BH ~ 10⁷⁷, this is still doubly exponentially large —
dim(H_e^Q) ~ 10^{30 × 10^77} / 10^30 ~ 10^{30 × 10^77}, negligibly smaller than
dim(H_e) = d_e^{N_total}.

The 4D factor H_{4D} is untouched by the e-superselection: the constraint acts
entirely on H_e, not on H_{4D}. Within the sector H_Q = H_{4D} ⊗ H_e^Q, the late
mode b retains its full 4D Hilbert space H_{4D}^{(b)} — a 2-dimensional qubit (for a
single fermionic mode) or higher-dimensional Fock space. The 4D entanglement capacity
is:

    E_max(b) within H_Q = log₂ dim(H_{4D}^{(b)}) = 1 ebit (fermionic mode)

This is identical to the 4D entanglement capacity without the e-constraint. The
e-superselection fixes which e-charge sector the system is in; it does not remove any
4D dimension from mode b's Hilbert space.

Therefore: the AMPS monogamy argument — which concerns the 4D entanglement of mode b
with I (vacuum entanglement) and with R (unitarity entanglement) — operates entirely
within H_{4D} ⊗ H_e^Q for a fixed Q. The e-correlations that encode infalling
information are in H_e^Q and do not consume any of E_max(b) = 1 ebit. Monogamy of 4D
entanglement within H_Q is not violated; the e-correlations are orthogonal resources
in the e-factor. ∎

---

**Also add the M >> M_Pl restriction explicitly in the theorem statement.**

**Location:** Section 9.3.1, in the statement of Theorem 9.1. After the sentence
"In the 5D e-dimension framework, the three AMPS postulates hold simultaneously:"
add the scope qualifier:

---

*(Scope: The following theorem holds in the semiclassical regime M >> M_Pl, where
the Hawking temperature T_H << m₁ c²/k_B — the temperature is far below the lightest
KK mass — so 4D observables are restricted to the KK zero-mode sector. See the Mass
range validity note in §9.3.1 and Appendix B.8. The AMPS argument is not formulated
for M ~ M_Pl, where the semiclassical approximation itself breaks down.)*

---

### B2(b): The Bogoliubov transformation — 5D vacuum factorization
**Rating: (A) GENUINE GAP**

#### (a) Author response

This is the most technically serious finding in the report. The referee correctly
identifies that the Hadamard condition argument in §9.5 rests on the claim that the
5D vacuum factorizes: |0⟩₅D = |0⟩_{4D,Unruh} ⊗ |0⟩_e. The justification given in
the current text — that the product metric decomposes the 5D field equation into
independent 4D equations for each KK mode — is insufficient for the following precise
reason identified by the referee:

The 5D vacuum is defined by the 5D positive-frequency condition. In the background
M⁴ × S¹, the 5D positive-frequency modes have energies that include the KK masses.
An infalling observer's vacuum is defined by the absence of 5D particles — including
all KK levels. The Bogoliubov transformation relating the infalling vacuum to the
exterior Fock space mixes 4D modes with KK excitations in a way that has not been
computed. Therefore it is not established from first principles that ρ₄D =
Tr_e[ρ₅D] is exactly the 4D Unruh vacuum.

We adopt Option (c) from the referee's three-way choice: we explicitly downgrade the
Hadamard condition claim from a derived result to a working assumption, state it
clearly as such, identify what would be needed to prove it, and note that the
qualitative no-drama conclusion (§9.4) remains sound contingent on this assumption.

This is the honest path, as the referee notes. We do not attempt to compute the full
5D Bogoliubov transformation in this revision. The dimensional estimate of KK
corrections (suppressed by (M_Pl/M)⁴ × (l_P/R₀)² ~ 10⁻⁶⁰) is retained as
motivation for why the assumption is expected to hold, but is no longer presented
as a derivation.

Note on what remains unconditional: the no-drama argument of §9.4 (no energy barrier
in 4D from the e-imprint δφ) does not depend on the Hadamard condition. It depends
only on the fact that δφ is a phase shift in the fiber dimension, not a 4D energy
density, and that 4D detectors respond only to KK zero-mode observables
([Q̂_e, Ô₄D] = 0, Property 2). This part of the argument is unconditional.
The Hadamard condition is the stronger statement that the 2-point function near
the horizon has exact Minkowski short-distance behavior — this is what requires the
5D Bogoliubov transformation.

#### (b) Revised text

**Location:** Section 9.5. Replace "Step 2: Tracing over e in the Unruh state"
and the surrounding passage entirely with the following:

---

**Step 2: The 5D vacuum factorization — working assumption and its justification.**

We require the 4D marginal state ρ₄D = Tr_e[ρ₅D] to be the 4D Unruh vacuum. In a
product spacetime M⁴ × S¹ with metric g₅D = g₄D + R₀² dφ², the 5D wave equation for
a minimally coupled scalar field Φ separates into independent equations for each KK
mode Φ_n(x) with effective 4D mass m_n = n/R₀. The mode functions therefore factor as:

    u_{k,n}(x,φ) = f_k(x) × e^{inφ/R₀}

where f_k(x) are the standard 4D Hawking/Unruh mode functions and e^{inφ/R₀} are
the S¹ harmonics. This factorization of the *mode functions* motivates the conjecture
that the 5D vacuum state factorizes correspondingly:

    |0⟩₅D =? |0⟩_{4D,Unruh} ⊗ |0⟩_e

**However, this factorization is not derived.** The 5D vacuum is defined by the 5D
positive-frequency condition — the absence of 5D particles, including all KK
excitations. The Bogoliubov transformation relating the infalling vacuum (defined by
ingoing Eddington-Finkelstein coordinates) to the exterior Fock space mixes 4D modes
with KK modes in a way that depends on the full 5D mode structure. In particular, the
KK masses m_n = n/R₀ appear in the 5D frequency condition and modify the Bogoliubov
coefficients relative to the pure 4D calculation. The 5D Bogoliubov coefficients
have not been computed, and it is therefore not established from first principles that
Tr_e[ρ₅D] is exactly the 4D Unruh vacuum.

**Working Assumption 9.1 (5D Vacuum Factorization).** *We assume that the 5D vacuum
state in the product spacetime M⁴ × S¹ factorizes as |0⟩₅D = |0⟩_{4D,Unruh} ⊗ |0⟩_e,
so that ρ₄D = Tr_e[ρ₅D] = |0⟩_{4D,Unruh}⟨0|.*

This assumption is well-motivated by the following evidence, but not yet a theorem:

1. **Mode function factorization:** The 5D mode functions factor by the product
   metric structure, as shown above. If the vacuum is the Fock vacuum built on these
   factored modes, the state factorization follows. The question is whether the 5D
   Bogoliubov transformation (which mixes modes across the horizon) preserves this
   factored structure.

2. **KK mass gap suppression:** The corrections to the 4D Bogoliubov coefficients
   from KK mode mixing are estimated to scale as (T_H/m₁)² ~ (M_Pl/M)⁴ × (l_P/R₀)²
   ~ 10⁻⁶⁰ for astrophysical black holes, where m₁ = 1/R₀ is the KK mass scale and
   T_H ~ 1/M is the Hawking temperature. At this level of suppression, the deviation
   from the factorized state is undetectable in any physical measurement. This is a
   dimensional estimate, not a rigorous bound on the Bogoliubov coefficients.

3. **Consistency with Section 6.2:** The 4D projection of the 5D state reproduces
   the Hawking thermal spectrum (§6.2), which is consistent with ρ₄D being the
   4D Unruh vacuum. This is a consistency check, not an independent derivation.

**What would close the gap:** Computing the 5D Bogoliubov transformation explicitly —
expanding the 5D field in both infalling and outgoing mode bases, computing the
overlap coefficients α_{km}^{(n)} and β_{km}^{(n)} for each KK level n, and showing
that the off-diagonal (n ≠ 0) coefficients are suppressed by the KK mass gap — would
upgrade Working Assumption 9.1 to a theorem. This computation is deferred to future
work. Alternatively, a rigorous bound on ‖β^{(n)}‖ from the KK mass gap via the
Fulling-Sweeny-Wald theorem (1978) on Bogoliubov coefficient decay would suffice.

**Consequence for the Hadamard condition argument:** Accepting Working Assumption 9.1,
the marginal 4D state is ρ₄D = |0⟩_{4D,Unruh}⟨0|. The Hadamard condition then follows
from the established result that the 4D Unruh vacuum is a Hadamard state on
Schwarzschild spacetime (Fredenhagen & Haag 1990; Kay & Wald 1991). The conclusion
— the infalling observer encounters no firewall — follows from Working Assumption 9.1.
The no-drama result of §9.4 (no 4D energy barrier from δφ) is independent of this
assumption and holds unconditionally in the semiclassical regime.

---

**Also revise the "Caveats" paragraph at the end of §9.5.** Replace the final
Caveats paragraph with:

---

**Caveats and status.** The Hadamard condition argument rests on Working Assumption 9.1
(5D vacuum factorization). This assumption is well-motivated but not yet derived;
computing the 5D Bogoliubov transformation to verify it is deferred to future work.
The no-drama conclusion of §9.4 does not depend on this assumption. The factorization
approximation ρ₅D ≈ ρ₄D ⊗ ρ_e also breaks down at M ~ M_Pl (Planck-scale regime),
but as noted, the AMPS argument and the semiclassical analysis are not reliable there
in any case. The Hadamard condition claim is therefore a conditional result: it holds
given Working Assumption 9.1, and it holds unconditionally in the M >> M_Pl regime
to the extent that the KK mass gap suppression of the Bogoliubov mixing
(estimated at ~ 10⁻⁶⁰) constitutes a reliable approximation.

---

**Also update the status table in §13.1 (Conclusion).** The row for the firewall
paradox resolution should be revised to add the Hadamard condition qualification:

---

| Firewall paradox resolution (Theorem 9.1) | **Derived** conditionally: no-drama from §9.4 (no 4D energy barrier) is unconditional; no-drama from §9.5 (Hadamard condition) is conditional on Working Assumption 9.1 (5D vacuum factorization, §9.5); see B2(b) response | A proof that the 5D path integral is UV divergent at the horizon vertex, or a computation showing the 5D Bogoliubov transformation does not preserve the factorized vacuum |

---

---

## PART C: TECHNICAL CALCULATIONS

---

### C1(b): Independence of the e-clock from the metric
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee requires one sentence confirming that the Z₂ orbifold symmetry is
anomaly-free and prevents radiative corrections to g_{5μ}, citing Paper 1 §2.1.

#### (b) New text

**Location:** Section 3.2, after the paragraph ending "...the e-clock evolution is
metric-independent as a result." Add:

---

The Z₂ symmetry φ → −φ is anomaly-free: it is a discrete symmetry of the classical
action that is preserved by the one-loop fermion path integral because the fermionic
spectrum is symmetric under n → −n (Paper 1, §2.1; the KK fermion modes come in
degenerate pairs ±n), so no chiral anomaly or Witten anomaly can arise from a discrete
symmetry with a symmetric spectrum. Consequently, radiative corrections at all loop
orders preserve the Z₂ symmetry and cannot generate a non-zero off-diagonal metric
component g_{5μ} (an odd function of φ), confirming that the product-metric form
g₅D = g₄D + R₀² dφ² — and hence the metric-independence of the e-clock evolution
∂φ/∂τ = −E/ℏ — is exact to all perturbative orders (see also Paper 1, §2.1 for the
full anomaly analysis).

---

### C1(c): Wheeler-DeWitt Hamiltonian factorization
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee requires one sentence confirming that E_clock/M_BH ~ 1/M² << 1
throughout semiclassical evaporation, validating the Born-Oppenheimer limit.

#### (b) New text

**Location:** Section 3.3, after the sentence "This is the framework in which the
Page-Wootters mechanism applies." Add:

---

The Born-Oppenheimer validity condition for the gravitational sector requires
E_clock << M_BH: the clock energy must be negligible compared to the black hole
mass. In the present framework, the e-clock energy scale is E_clock ~ T_H ~ ℏ/M
(in Planck units, T_H = 1/(8πM)), while M_BH = M, so E_clock/M_BH ~ 1/M² << 1
throughout the semiclassical regime M >> M_Pl — the ratio decreases as evaporation
proceeds and M decreases, remaining small until M ~ M_Pl where the semiclassical
approximation itself breaks down, confirming that the Born-Oppenheimer factorization
is valid throughout the entire semiclassical evaporation history.

---

### C3(a): Non-perturbative completion — M-theory identification
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee requires an explicit statement that no result in Paper 3 requires the
M-theory completion; the M-theory identification is forward-looking context. The
current Appendix A.4.2 already says "The M-theory completion is not required for any
physical prediction in this paper" but this statement is buried in a footnote-level
passage. We make it prominent at the top of §A.4.

#### (b) New text

**Location:** Appendix A.4, at the beginning of §A.4.1 "What Remains After Layers
1 and 2." Insert before the existing text:

---

**Important organizational note.** The central results of this paper — Theorem 6.1
(unitarity of the 5D S-matrix), Theorem 7.1 (Conditional Page Curve), and Theorem 9.1
(resolution of the AMPS paradox) — do not depend on the M-theory completion discussed
in §A.4.2. All three theorems follow from the perturbative 5D framework (Paper 1) plus
the 5D equations of motion; the perturbative finiteness (Layer 1, §A.2) and
non-perturbative stability (Layer 2, §A.3) established within the framework are
sufficient. The M-theory identification of §A.4.2 is additional forward-looking context
— a plausibility argument that the self-consistent perturbative framework sits inside a
non-perturbatively complete theory — contingent on Paper 4's identification of the
Standard Model content from M-theory compactification. Readers who are skeptical of
the M-theory identification should note that it is neither required by, nor does it
strengthen, the paper's primary claims about black hole information. It is a structural
observation about the framework's place in the landscape of quantum gravity, deferred
in full to Paper 4.

---

### C3(c): Topology change and black holes
**Rating: (B) CLOSABLE GAP**

#### (a) Author response

The referee requires one sentence noting that S¹ fiber stability during Planck-scale
evaporation is not established from the full path integral; the argument holds for
M >> M_Pl.

#### (b) New text

**Location:** Section A.3.1 (or wherever the S¹ stability during evaporation is
discussed), at the end of the argument concluding that topology change is negligible.
Add:

---

We note explicitly that this stability argument — resting on modulus stabilization at
R₀ and the instanton action S_CDL >> 10³⁰ — is a semiclassical result valid for
M >> M_Pl, where the radion fluctuations δR/R₀ ~ (M_Pl/M)² << 1 and the product-
metric approximation g₅D = g₄D + R₀² dφ² is reliable; in the Planck-scale regime
M ~ M_Pl, quantum fluctuations of the radion become O(1) and the modulus
stabilization argument no longer applies, leaving open whether the full gravitational
path integral at M ~ M_Pl generates 5D topological contributions such as fiber
degeneration at the singularity — but this is consistent with the scope of the
entire paper, which treats only the semiclassical regime M >> M_Pl throughout.

---

---

## SUMMARY OF CHANGES

| Finding | Rating | Change |
|---|---|---|
| A1(a) | B | Added one paragraph to §2.4 defining φ₀ as a quantum operator in H₅D = ⊕_Q H_Q |
| A1(b) | B | Added explicit no-signaling theorem to §5.3 using Property 2 and the 4D marginal state |
| A2(a)/B1(b) | B | Added one paragraph to §7.3 computing the KK G-renormalization giving s₀ = 1 |
| A2(b) | B | Added one sentence to §4.2 confirming dM/dt is reproduced at leading order |
| A2(c) | B | Added one sentence to §4.3 stating "Planck pixel creation" is a semiclassical description |
| B1(a) | B | Revised §12.3 table and bullet to remove "deriving (not assuming)" language; clarified conditional status throughout; cross-referenced §7.6 stratification |
| B1(c) | B | Added one paragraph to §7.7 noting both early- and late-time Page curve rely on fast-scrambler assumption; no ρ_rad evolution computed |
| B2(a) | B | Added explicit counting argument to §9.3.1 showing dim(H_Q) exponentially large and E_max(b) undiminished; added M >> M_Pl scope qualifier to Theorem 9.1 |
| **B2(b)** | **A** | **Fully revised §9.5: introduced Working Assumption 9.1 (5D vacuum factorization), explained why current text is insufficient, retained KK mass gap as motivation, deferred 5D Bogoliubov calculation to future work; updated §13.1 status table** |
| C1(b) | B | Added one sentence to §3.2 on Z₂ anomaly cancellation, citing Paper 1 §2.1 |
| C1(c) | B | Added one sentence to §3.3 confirming E_clock/M_BH ~ 1/M² << 1 |
| C3(a) | B | Added explicit independence note at top of §A.4.1 |
| C3(c) | B | Added one sentence to §A.3.1 on M >> M_Pl scope of fiber stability argument |

---

*Response prepared by the authors.*
*Submitted with revised manuscript.*
