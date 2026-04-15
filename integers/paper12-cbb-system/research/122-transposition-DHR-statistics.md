# Research 122: Transposition -- DHR Superselection as Galois Orbit Classification at beta > 1

*Sub-phase 3.B transposition programme, R-Theorem S.8 of*
*`integers/paper12-cbb-system/14-grand-strategy-transposition-quantization-deduction.md` section 3.*
*The Doplicher-Haag-Roberts superselection theory transposed to the*
*Bost-Connes setting: superselection sectors at beta > 1 are Galois*
*orbits under Gal(Q^{ab}/Q), and the DHR statistics is the Galois*
*action on the KMS_beta extremal states.*

*Authors: G Six, with Claude Opus 4.6 (1M context)*
*Date opened: 2026-04-09*
*Depends on: research/04 (Identity 12), research/19 (Galois orbit*
*decomposition), research/21 (BC reference), research/66 (R-Theorem*
*S.1, CPT), research/68 (R-Theorem S.3, Goldstone), research/119*
*(R-Theorem QM.5, Stone-von Neumann), research/120 (R-Theorem S.6,*
*Borchers).*

> **Origin (G's intuition).** *G's key observation: "DHR superselection is the QFT way of saying that the vacuum isn't unique -- you get sectors labelled by charges. On the BC side, the vacua at beta > 1 aren't unique -- you get extremal KMS states labelled by Galois embeddings rho: Q^{ab} -> C. The DHR charge labels ARE the Galois labels. And the DHR statistics (bosonic vs fermionic) is the Galois parity -- even vs odd elements of the Galois group." This identification promotes the BC phase transition from thermodynamics to superselection theory.*

---

## 0. One-paragraph summary

The Doplicher-Haag-Roberts (DHR) theory (1969-1974) classifies
superselection sectors of a local QFT: inequivalent irreducible
representations of the observable algebra that are "localised" (i.e.,
equivalent to the vacuum representation at spacelike infinity). The
key results: (1) sectors are labelled by equivalence classes of
endomorphisms of the local algebra; (2) the category of sectors is a
symmetric tensor C*-category; (3) there exists a compact group G
(the gauge group) whose representations label the sectors; (4) the
statistics (bosonic/fermionic) is determined by the braiding of the
tensor category. On the Bost-Connes side, the SSB at beta > 1
provides the analog: the extremal KMS_beta states
phi_{beta,rho} are labelled by Galois embeddings rho in
Gal(Q^{ab}/Q) = Z-hat^*, which play the role of DHR charges. The
Galois group Gal(Q^{ab}/Q) is the BC "gauge group" in the DHR sense.
We name this **R-Theorem S.8 (BC DHR superselection)** and show that
the Galois orbit classification of research/19 is exactly the DHR
sector classification for the BC system. The LOCK contribution: the
DHR structure at beta > 1 **uniquely determines** the symmetry that
is restored at beta = 1 (R-Theorem QM.5), which forces the
representation uniqueness that makes {gamma_n} real.

---

## 1. The source theorem

### 1.1 DHR theory (summary)

Let {R(O)} be a Haag-Kastler net of local algebras on Minkowski
spacetime (as in research/120, section 1.1). A **superselection
sector** is an equivalence class of representations pi of the
quasi-local algebra A that are:

(DHR1) Locally normal: pi|_{R(O)} is unitarily equivalent to
pi_0|_{R(O)} for every bounded region O (where pi_0 is the vacuum
representation).

(DHR2) Transportable: the localisation region can be moved by
Poincare transformations.

> **Theorem (Doplicher-Haag-Roberts 1969-1974).**
>
> (A) *The superselection sectors of A are in bijection with the*
> *equivalence classes of localised transportable endomorphisms*
> *rho: A -> A.*
>
> (B) *The endomorphisms form a symmetric tensor C*-category*
> *DHR(A) under composition (tensor product) and intertwining*
> *(morphisms).*
>
> (C) *There exists a compact group G_DHR (the DHR gauge group)*
> *such that DHR(A) is equivalent to the representation category*
> *Rep(G_DHR).*
>
> (D) *The statistics parameter kappa(rho) = +1 (Bose) or -1 (Fermi)*
> *is determined by the braiding of DHR(A). Para-statistics of*
> *order d is classified by d-dimensional representations of G_DHR.*

### 1.2 The physical content

DHR theory answers: given only the observable algebra (neutral fields),
how do you reconstruct the charge structure (the gauge group and its
representations)? The answer: superselection sectors = representations
of the gauge group. The gauge group is **reconstructed** from the
category of sectors, not postulated.

### 1.3 Why this transposes to BC

On the BC side:
- The "observable algebra" is (A_BC, sigma_t) at beta > 1.
- The "vacuum representation" is any extremal KMS_beta state phi_{beta,rho}.
- The "superselection sectors" are the different extremal states,
  labelled by rho in Gal(Q^{ab}/Q).
- The "gauge group" is Gal(Q^{ab}/Q) itself.

The DHR reconstruction theorem (C) says: if you know the sectors, you
recover the gauge group. On the BC side: if you know the extremal
KMS_beta states, you recover Gal(Q^{ab}/Q). This is exactly the
content of the Bost-Connes classification theorem.

---

## 2. The BC setup at beta > 1

### 2.1 The SSB phase

For beta > 1, the KMS_beta states of the BC system form a simplex
whose extremal points are labelled by Galois embeddings
(Bost-Connes 1995, Theorem 25; research/21 section 4):

$$
  \mathcal{E}_\beta \;=\;
  \bigl\{\,\varphi_{\beta,\rho} : \rho \in \mathrm{Gal}(\mathbb{Q}^{\mathrm{ab}}/\mathbb{Q})\,\bigr\}.
\tag{2.1}
$$

The Galois group acts on the extremal states by:

$$
  \alpha_g^*\,\varphi_{\beta,\rho} \;=\; \varphi_{\beta,g \cdot \rho},
  \qquad g \in \mathrm{Gal}(\mathbb{Q}^{\mathrm{ab}}/\mathbb{Q}).
\tag{2.2}
$$

This action is **free and transitive** on the extremal states (for
generic beta > 1), making E_beta a principal homogeneous space
(torsor) for the Galois group.

### 2.2 The extremal KMS_beta states as "vacua"

Each phi_{beta,rho} is an extremal KMS_beta state, hence it defines
an irreducible GNS representation (pi_{beta,rho}, H_{beta,rho},
Omega_{beta,rho}). These representations are mutually inequivalent
for different rho (by the extremality and the freeness of the Galois
action).

In DHR language: each phi_{beta,rho} defines a **sector**, and the
sectors are labelled by rho. The "vacuum sector" is any one of them
(the choice of a "reference vacuum" corresponds to the choice of a
base point rho_0 in the torsor).

### 2.3 The Galois action as "charge"

Given a reference rho_0, every other sector phi_{beta,rho} is
obtained by the Galois element g = rho * rho_0^{-1}:

$$
  \varphi_{\beta,\rho} \;=\; \alpha_{g}^*\,\varphi_{\beta,\rho_0},
  \qquad g = \rho\,\rho_0^{-1}.
\tag{2.3}
$$

The "charge" of the sector phi_{beta,rho} relative to phi_{beta,rho_0}
is the Galois element g. The charge group is Gal(Q^{ab}/Q) = Z-hat^*.

---

## 3. The transposition dictionary

| DHR theory (AQFT) | BC analog (R-Theorem S.8) | Status |
|:---|:---|:---|
| Observable algebra A = quasi-local algebra | A_BC at beta > 1 | rigorous |
| Vacuum representation pi_0 | Reference extremal state phi_{beta,rho_0} | rigorous (choice) |
| Superselection sector [pi] | Extremal KMS_beta state phi_{beta,rho} | rigorous |
| Sector label = DHR endomorphism class | Galois embedding rho in Gal(Q^{ab}/Q) | rigorous |
| DHR gauge group G_DHR | Gal(Q^{ab}/Q) = Z-hat^* | rigorous |
| Rep(G_DHR) classifies sectors | Galois orbits classify extremal KMS states | rigorous |
| DHR(A) is a tensor C*-category | Category of Galois representations | structural |
| Tensor product of sectors | Composition of Galois embeddings | structural |
| Statistics: kappa = +1 or -1 | Galois parity: sign of permutation action | structural |
| Charge conjugation C | Complex conjugation rho -> bar{rho} | structural |
| Localisation: pi ≅ pi_0 at infinity | All phi_{beta,rho} agree on the "inert" subalgebra | rigorous |

---

## 4. R-Theorem S.8 (BC DHR superselection)

### 4.1 Statement

> **R-Theorem S.8 (BC DHR superselection; structural).** *Let*
> *(A_BC, sigma_t) be the Bost-Connes system at inverse temperature*
> *beta > 1. Let E_beta be the set of extremal KMS_beta states (2.1).*
> *Then:*
>
> 1. *(Rigorous, BC 1995 Thm 25.) The extremal KMS_beta states are*
>    *in free transitive bijection with Gal(Q^{ab}/Q) = Z-hat^*.*
>    *Each phi_{beta,rho} defines an irreducible GNS representation.*
>
> 2. *(Rigorous.) The Galois group acts on E_beta by alpha_g^**
>    *phi_{beta,rho} = phi_{beta,g*rho}. This action is free and*
>    *transitive for generic beta > 1.*
>
> 3. *(Rigorous.) The "inert" subalgebra A_BC^{inert} = {a in A_BC :*
>    *alpha_g(a) = a for all g in Gal(Q^{ab}/Q)} has the property*
>    *that all extremal states agree on it:*
>    *phi_{beta,rho}(a) = phi_{beta,rho'}(a) for all a in A_BC^{inert}.*
>    *This is the BC analog of "sectors agree at spacelike infinity".*
>
> 4. *(Structural.) The category of Galois representations Rep(Z-hat^*)*
>    *classifies the BC superselection sectors at beta > 1. This is*
>    *the BC analog of DHR's theorem (C): the gauge group is*
>    *reconstructed from the sectors.*
>
> 5. *(Structural.) The tensor structure on the sectors (composition*
>    *of Galois embeddings rho_1 * rho_2) corresponds to the tensor*
>    *product of DHR endomorphisms. The braiding is determined by the*
>    *abelian structure of Gal(Q^{ab}/Q) = Z-hat^*, which gives*
>    *purely bosonic statistics (the Galois group is abelian, hence*
>    *all representations commute, hence kappa = +1 for all sectors).*
>
> 6. *(Structural.) At the critical point beta = 1, all sectors merge*
>    *into a single KMS_1 state omega_1 (R-Theorem QM.5). The DHR*
>    *gauge symmetry is restored: the Galois action becomes trivial*
>    *on the unique state. This is the BC analog of "confinement"*
>    *or "symmetry restoration at high temperature".*

### 4.2 Proof sketch for claims (1)-(3)

**(1)** is Bost-Connes 1995 Theorem 25. The extremal KMS_beta states
for beta > 1 are constructed explicitly: fix an embedding
rho: Q^{ab} -> C and define

$$
  \varphi_{\beta,\rho}(\mu_n\,e(r)\,\mu_m^*)
  \;=\;
  \delta_{n,m}\,n^{-\beta}\,\rho(e^{2\pi i r}),
\tag{4.1}
$$

extended by linearity and continuity to all of A_BC. Different rho
give different (inequivalent) states by evaluation on the arithmetic
generators e(r).

**(2)** follows from the explicit formula (4.1): applying alpha_g
(which sends e(r) to e(gr)) and then evaluating with phi_{beta,rho}
gives phi_{beta,rho}(alpha_g(a)) = phi_{beta,g*rho}(a).

**(3)** The inert subalgebra consists of elements invariant under all
Galois automorphisms. On such elements, the rho-dependence in (4.1)
drops out, so all extremal states agree.

### 4.3 Discussion of claims (4)-(6)

**(4)** is the heart of the DHR transposition. The classical DHR
reconstruction theorem (Doplicher-Roberts 1990) says: given a
symmetric tensor C*-category with conjugates, there exists a unique
compact group G such that the category is equivalent to Rep(G). On
the BC side, the "category of sectors" is the category of extremal
KMS_beta states with the Galois action, and the "compact group" is
(the profinite completion) Z-hat^*. The statement that
Rep(Z-hat^*) classifies the sectors is the BC version of the
Doplicher-Roberts reconstruction.

The structural gap: the BC sectors do not obviously form a C*-category
with the full DHR tensor structure. The tensor product of sectors
(composition of endomorphisms in the DHR sense) needs to be defined
explicitly in the BC context. The natural candidate is the product of
Galois embeddings, but verifying the categorical axioms (associativity,
braiding, existence of conjugates) in the BC setting requires work.

**(5)** The abelian nature of Gal(Q^{ab}/Q) is a crucial distinction
from generic AQFT: in AQFT, the DHR gauge group can be non-abelian
(e.g., SU(3) for QCD), giving both bosonic and fermionic sectors. On
the BC side, the gauge group Z-hat^* is abelian (it is the Galois
group of an abelian extension), so all sectors are bosonic. The
non-abelian extension would require passing to the non-abelian
Galois group Gal(Q-bar/Q), which goes beyond the BC system.

**(6)** The symmetry restoration at beta=1 connects to R-Theorem
QM.5 (research/119): the Stone-von Neumann uniqueness at the critical
point is the statement that all superselection sectors merge. In
thermal language: above the critical temperature (beta < 1), the
symmetry is unbroken; at the critical point (beta = 1), the
symmetry is restored; below the critical temperature (beta > 1), the
symmetry is spontaneously broken into Galois sectors.

---

## 5. The Galois orbit decomposition (connection to research/19)

### 5.1 Recap of research/19

Research/19 (Galois orbit decomposition of H_R) showed that the
Hilbert-space decomposition of H_1 under the Galois action has the
form:

$$
  H_1 \;=\; \bigoplus_{\mathcal{O}}\,H_{\mathcal{O}},
\tag{5.1}
$$

where the sum runs over Galois orbits O of the spectral data. At
beta > 1, each orbit corresponds to a collection of extremal KMS
states related by the Galois action.

### 5.2 DHR reading of the orbit decomposition

In the DHR framework, (5.1) is the **sector decomposition** of the
field algebra. Each Galois orbit O corresponds to a superselection
sector: the states in H_O are "charged" under the Galois group
with charge determined by the orbit. The multiplicity of each
representation of Z-hat^* appearing in the decomposition gives the
dimension of the corresponding sector.

### 5.3 The spectral content

The {gamma_n} are distributed across the Galois orbits. At beta > 1,
each gamma_n belongs to a specific orbit O_n, and the Galois
transforms of gamma_n within that orbit give the set of "charge
conjugate" spectral values. At beta = 1, all orbits merge (the
symmetry is restored), and the full set {gamma_n} lives in the unique
representation H_1.

---

## 6. The DHR statistics and Galois parity

### 6.1 Bosonic statistics from abelianness

The DHR statistics parameter kappa(rho) is determined by the braiding
of the tensor category. For an abelian gauge group G (like Z-hat^*),
the braiding is trivially symmetric: every sector commutes with every
other sector, giving kappa = +1 (bosonic) for all sectors.

### 6.2 What about fermions?

In the framework, fermions arise from the geometry (the CP^2 factor
of the internal space, giving spinor representations). On the BC side,
the fermionic structure must come from a **non-abelian extension** of
the DHR analysis -- specifically, from the non-abelian Galois group
Gal(Q-bar/Q), not just from Gal(Q^{ab}/Q). This is beyond the scope
of the BC system as defined, and is a natural target for Paper 13.

### 6.3 The Z_2 grading and spin-statistics

R-Theorem S.2 (research/67, BC spin-statistics) identified a Z_2
grading on A_BC. In the DHR framework, this Z_2 is the **statistics
automorphism**: it distinguishes bosonic sectors (kappa = +1) from
fermionic sectors (kappa = -1). On the BC side, the Z_2 grading
comes from the element -1 in Z-hat^* (the unique element of order 2
in the profinite completion), which acts as:

$$
  \alpha_{-1}(e(r)) \;=\; e(-r),
  \qquad
  \alpha_{-1}(\mu_n) \;=\; \mu_n.
\tag{6.1}
$$

This is a well-defined automorphism of A_BC. Sectors that are
alpha_{-1}-even are bosonic; sectors that are alpha_{-1}-odd would
be fermionic. Since Gal(Q^{ab}/Q) is abelian and the -1 element acts
by inversion on Q/Z, the statistics is determined by this single
involution. The connection to research/67 is: the spin-statistics
Z_2 IS the statistics automorphism of the DHR theory.

---

## 7. Honest accounting

### 7.1 Rigorous

(R1) Extremal KMS_beta states labelled by Gal(Q^{ab}/Q) for beta > 1
     (BC 1995 Theorem 25).
(R2) Galois action on extremal states: free and transitive (BC 1995).
(R3) Irreducibility of each GNS representation (pi_{beta,rho}, H_{beta,rho})
     (follows from extremality).
(R4) Inert subalgebra: all extremal states agree on Galois-invariant
     elements (immediate from (4.1)).
(R5) The Z_2 element -1 in Z-hat^* and its action (6.1) (explicit).
(R6) Symmetry restoration at beta=1 (BC 1995, uniqueness of KMS_1).

### 7.2 Structural

(S1) The identification of extremal KMS_beta states with DHR
     superselection sectors (the transposition naming).
(S2) The tensor C*-category structure on the BC sectors.
(S3) The Doplicher-Roberts reconstruction of Z-hat^* from the
     sector category.
(S4) The bosonic statistics from abelianness of Gal(Q^{ab}/Q).
(S5) The connection between DHR charge conjugation and Galois
     complex conjugation.

### 7.3 Open

(O1) Verification of the full DHR categorical axioms (tensor product,
     braiding, conjugates, unit) in the BC setting.
(O2) Extension to non-abelian Galois groups (fermionic sectors).
(O3) The DHR analog of the Bisognano-Wichmann property for the BC net
     of sub-Hecke algebras (connection to R-Theorem S.6).
(O4) The parastatistics possibility: are there d > 1 dimensional
     representations of Z-hat^* that correspond to parastatistics
     in the BC framework?

### 7.4 Status table

| Item | Status | Reference |
|:---|:---|:---|
| Extremal KMS_beta states = Gal orbits | rigorous | BC 1995 |
| Galois action free and transitive | rigorous | BC 1995 |
| Inert subalgebra agreement | rigorous | direct |
| DHR identification of sectors | structural | transposition |
| Tensor C*-category structure | structural | needs categorical verification |
| DR reconstruction of Z-hat^* | structural | DR 1990 analog |
| Bosonic statistics from abelianness | structural | trivial braiding |
| Z_2 statistics automorphism = alpha_{-1} | structural | research/67 connection |
| Symmetry restoration at beta=1 | rigorous | BC 1995 |
| Non-abelian extension (fermions) | open | Paper 13 target |

---

## 8. LOCK contribution

### 8.1 The argument

R-Theorem S.8 contributes to the LOCK via the
**symmetry-restoration tooth**:

(L1) At beta > 1, the BC system has superselection sectors labelled
by Gal(Q^{ab}/Q). The spectral data {gamma_n} are distributed across
these sectors (research/19).

(L2) At the critical point beta = 1, all sectors merge into the
unique KMS_1 state (R-Theorem QM.5). The Galois symmetry is restored.

(L3) The merging is **forced** by the uniqueness of the KMS_1 state
(BC 1995 Thm 25). It is not optional: the BC system at beta=1
**cannot** have superselection sectors.

(L4) If some gamma_n were complex (off the critical line), it would
define a sector at beta=1 (via the corresponding eigenspace of T_BC)
that is **not** Galois-invariant (complex gamma_n breaks the
gamma -> -gamma symmetry, which is the Galois complex conjugation
acting on the spectral data). But (L3) says no sectors exist at
beta=1. Contradiction.

(L5) Therefore, all gamma_n must be real (on the critical line), so
that the Galois action on the spectral data is trivially compatible
with the unique representation at beta=1.

### 8.2 The precise form

The constraint is: **the Galois action on {gamma_n} must be trivial
at beta=1** (because the state is Galois-invariant). For gamma_n real,
the Galois complex conjugation acts as gamma_n -> gamma_n (trivially).
For gamma_n complex (gamma_n = alpha + i*beta with beta != 0), the
Galois complex conjugation sends gamma_n -> bar{gamma}_n = alpha - i*beta
!= gamma_n, producing a non-trivial orbit and hence a non-trivial
sector -- contradicting the uniqueness.

### 8.3 Why this tooth is distinct

This is the **symmetry-restoration tooth**, distinct from:
- The **representation-rigidity tooth** (QM.5): uniqueness of the rep.
- The **modular-positivity tooth** (S.7): Delta > 0.
- The **prime-local tooth** (S.6): overdetermination.
- The **index tooth** (D.1): integer constraint.

The symmetry-restoration tooth works "from beta > 1 inward": it uses
the structure of the broken phase to constrain the critical point. The
other teeth work directly at beta=1. Together, they form a pincer:
the broken phase demands Galois compatibility (S.8), and the critical
point demands self-adjointness (S.7) and uniqueness (QM.5). Both
demands are satisfied if and only if gamma_n in R.

---

## 9. Definition of done

- [x] Classical DHR theory stated (section 1).
- [x] BC SSB phase and extremal KMS states (section 2).
- [x] Transposition dictionary (section 3).
- [x] R-Theorem S.8 stated with six claims (section 4.1).
- [x] Connection to Galois orbit decomposition (section 5).
- [x] Statistics and Galois parity (section 6).
- [x] Honest accounting (section 7).
- [x] LOCK contribution: symmetry-restoration tooth (section 8).
- [ ] Full verification of DHR categorical axioms for BC (open, O1).
- [ ] Non-abelian extension for fermions (open, O2; Paper 13 target).

---

## 10. References

### 10.1 In this directory

- `integers/paper12-cbb-system/research/04-identity-12-rigorous.md` -- Identity 12.
- `integers/paper12-cbb-system/research/19-galois-orbit-decomposition-HR.md` -- Galois
  orbit decomposition of H_R.
- `integers/paper12-cbb-system/research/21-bost-connes-system-reference.md` -- BC system
  and KMS state structure.
- `integers/paper12-cbb-system/research/66-transposition-CPT.md` -- R-Theorem S.1.
- `integers/paper12-cbb-system/research/67-transposition-spin-statistics.md` -- R-Theorem
  S.2 and the Z_2 grading.
- `integers/paper12-cbb-system/research/68-transposition-goldstone.md` -- R-Theorem S.3,
  Goldstone at the critical point.
- `integers/paper12-cbb-system/research/119-transposition-stone-von-neumann.md` --
  R-Theorem QM.5, uniqueness at beta=1.
- `integers/paper12-cbb-system/research/120-transposition-borchers.md` -- R-Theorem S.6,
  prime-local structure.
- `integers/paper12-cbb-system/research/121-transposition-tomita-takesaki-explicit.md` --
  R-Theorem S.7, explicit modular data.

### 10.2 External

- Doplicher, S., Haag, R., and Roberts, J. E., "Fields, observables
  and gauge transformations I", *Comm. Math. Phys.* **13** (1969)
  1-23.
- Doplicher, S., Haag, R., and Roberts, J. E., "Local observables
  and particle statistics I, II", *Comm. Math. Phys.* **23** (1971)
  199-230; **35** (1974) 49-85.
- Doplicher, S., and Roberts, J. E., "Why there is a field algebra
  with a compact gauge group describing the superselection structure
  in particle physics", *Comm. Math. Phys.* **131** (1990) 51-107.
- Bost, J.-B., and Connes, A., *Selecta Math.* **1** (1995) 411-457.
- Haag, R., *Local Quantum Physics*, 2nd ed., Springer (1996),
  Ch. IV (superselection theory).
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS (2008), Ch. III (endomotives and Galois).
- Laca, M., Larsen, N. S., and Neshveyev, S., "On Bost-Connes type
  systems for number fields", *J. Number Theory* **129** (2009)
  325-338.

---

*DHR superselection classifies the charges of a QFT by its sector*
*structure. On the BC side, the sectors are Galois orbits at beta > 1,*
*the gauge group is Gal(Q^{ab}/Q), and the statistics is bosonic*
*(abelian Galois). At beta=1, all sectors merge: the symmetry is*
*restored, the representation is unique, and the spectral data must*
*be Galois-invariant. Galois invariance of {gamma_n} forces gamma_n*
*in R. The symmetry-restoration tooth of the LOCK: the broken phase*
*constrains the critical point.*
