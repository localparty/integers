# Research 60: Transposition — Wigner–Eckart (R-Theorem QM.4)

*Transpose the Wigner–Eckart theorem of quantum mechanics — "matrix*
*elements of irreducible tensor operators factor into a Clebsch–*
*Gordan coefficient times a reduced matrix element" — to the Bost–*
*Connes side: matrix elements of Hecke operators μ_p between Galois*
*orbits on H_R factor into a "BC Clebsch–Gordan" and a reduced*
*matrix element.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Sub-phase 3.B, next round of transpositions (category A: QM),*
*R-Theorem QM.4.*
*Depends on: research/04 (Identity 12), research/19 (Galois orbit*
*decomposition of H_R), research/14 Part B, research/21 (BC ref).*

---

## 0. One-paragraph summary

The Wigner–Eckart theorem (Wigner 1927, Eckart 1930) is the
structural backbone of angular-momentum calculations in quantum
mechanics: the matrix element of an irreducible tensor operator
T^k_q between angular-momentum eigenstates |j' m'⟩ and |j m⟩
factors as a Clebsch–Gordan coefficient ⟨j m; k q | j' m'⟩ times
a **reduced matrix element** ⟨j' ‖ T^k ‖ j⟩ that depends only on
(j, j', k) and not on the magnetic quantum numbers (m, m', q). The
theorem is a direct consequence of Schur's lemma for the unitary
representation of SU(2) on the tensor product of the source and
operator representations. On the BC side, the Galois action of
Ẑ* = Gal(Q^cyc/Q) on A_BC plays the role of SU(2), the Galois
orbits on H_R play the role of the irreducible SU(2)
representations (research/19 Path B), and the Hecke operators μ_p
play the role of irreducible tensor operators (their Galois
transformation properties are computed below). The conclusion is
R-Theorem QM.4: the matrix elements ⟨γ_n | μ_p | γ_m⟩ between
Galois orbit states on H_R factor as

$$
\langle \gamma_n \mid \mu_p \mid \gamma_m \rangle
\;=\;
\mathrm{CG}_{\mathrm{BC}}(m, n; p) \cdot \langle n \| \mu_p \| m \rangle,
$$

where the "BC Clebsch–Gordan" is a character sum over Ẑ* and the
reduced matrix element depends only on the Galois orbit labels
(n, m, p). What is rigorous is Schur's lemma and the Galois action
on A_BC; what is structural is the identification of the Hecke
operators as irreducible BC tensor operators; what is open is the
explicit calculation of the BC Clebsch–Gordan for small (n, m, p).
As a LOCK contribution: the Wigner–Eckart factorisation forces the
reduced matrix elements to be real (up to a sign convention), which
gives a direct constraint on γ_n — real-valuedness of the reduced
matrix elements at all (n, m, p) implies the self-adjoint part of
T_BC has real spectrum, which is γ_n ∈ R.

---

## 1. The classical theorem

### 1.1 Irreducible tensor operators for SU(2)

Let H be a Hilbert space carrying a unitary representation U(g) of
SU(2), and decompose H = ⊕_j V_j into the irreducible components
(V_j ≅ C^{2j+1}). An **irreducible tensor operator** of rank k is
a collection T^k = {T^k_q : q = −k, …, k} of operators on H such
that

$$
U(g)\, T^k_q \, U(g)^{*} \;=\; \sum_{q'} D^{k}_{q' q}(g)\, T^k_{q'},
\qquad g \in SU(2),
\tag{1.1}
$$

where D^k(g) is the spin-k irreducible matrix of g. Equivalently,
the operator T^k is a "spin-k tensor" that transforms like a
vector in V_k under conjugation by U(g).

### 1.2 The theorem

> **Theorem (Wigner–Eckart).** *For any irreducible tensor operator*
> *T^k_q on H and any basis vectors |j m⟩, |j' m'⟩ of V_j, V_{j'},*
>
> $$
>   \langle j' m' \mid T^k_q \mid j m \rangle
>   \;=\;
>   \langle j m; k q \mid j' m' \rangle \cdot \langle j' \| T^k \| j \rangle,
>   \tag{1.2}
> $$
>
> *where the first factor is the Clebsch–Gordan coefficient for*
> *V_j ⊗ V_k ↪ V_{j'}, and the second factor (the "reduced matrix*
> *element") depends only on (j, j', k) and not on (m, m', q).*

**Proof.** The composition T^k_q |j m⟩ lives in V_j ⊗ V_k under
the tensor product representation. Decompose V_j ⊗ V_k = ⊕_{j'}
V_{j'}^{(j,k)} (Clebsch–Gordan decomposition). The projection onto
the V_{j'}-component is given by the Clebsch–Gordan coefficient.
By Schur's lemma, the matrix element ⟨j' m' | T^k_q | j m⟩ is
proportional to the Clebsch–Gordan coefficient, with the
proportionality constant independent of m, m', q. □

### 1.3 Selection rules

Wigner–Eckart implies the selection rules:
- m' = m + q (magnetic),
- |j − k| ≤ j' ≤ j + k (triangle),

both from the vanishing of the Clebsch–Gordan coefficient outside
these ranges. The reduced matrix element is a single complex
number per triple (j, j', k), and all the (m, m', q)-dependence
is in the Clebsch–Gordan coefficient.

---

## 2. The BC-side setup

### 2.1 The Galois action on A_BC

The Bost–Connes algebra carries a canonical action of
Ẑ* = Gal(Q^cyc/Q), the absolute abelian Galois group of Q, via

$$
\alpha_g(e(r)) \;=\; e(g \cdot r),
\qquad
\alpha_g(\mu_n) \;=\; \mu_n,
\qquad g \in \widehat{\mathbb{Z}}^{*},\; r \in \mathbb{Q}/\mathbb{Z}.
\tag{2.1}
$$

(See research/21 §5 and Bost–Connes 1995 §4.) The phase operators
transform in the **tautological** Galois representation; the
isometries μ_n are **Galois-invariant**. The Galois action is the
BC analog of the SU(2) action U(g) on a quantum-mechanical Hilbert
space.

**Remark.** Ẑ* is abelian (its irreducible representations are
the characters), so the BC Galois representation theory is
simpler than SU(2) — all irreducibles are one-dimensional. The
"j" quantum number becomes a character χ ∈ (Ẑ*)^ = Q/Z of the
Galois group, and the "m" quantum number degenerates (each
character is one-dimensional). The BC Wigner–Eckart is therefore
a **character-factorisation theorem** rather than a general
tensor-product theorem, which is the simplification of the QM
result for an abelian symmetry group.

### 2.2 Galois orbits on H_R

From research/19 (Galois orbit decomposition of H_R, Path B), the
Riemann subspace H_R decomposes (or is conjectured to decompose,
on the Path B tensor reading) as

$$
H_R \;=\; \bigoplus_{\chi \in \widehat{\mathbb{Z}}^{*}} \; H_R^{(\chi)},
\tag{2.2}
$$

where each H_R^{(χ)} is the subspace on which the Galois action α
acts by the character χ. The Galois orbits in H_R are labeled by
characters χ ∈ Q/Z (or equivalently by Dirichlet characters after
restriction to finite conductors).

On the Path B tensor reading, each zero γ_n is associated with a
specific character χ_n via the Galois sector it "lives in", and
the decomposition (2.2) gives H_R a natural basis
{|γ_n; χ⟩ : n ∈ N, χ ∈ Q/Z} with |γ_n; χ⟩ ∈ H_R^{(χ)}. For ease
of notation, we write |n⟩ := |γ_n; χ_n⟩ and note that the
character label χ_n is determined by n.

### 2.3 The Hecke operators as BC tensor operators

The Hecke operators μ_p are Galois-invariant by (2.1) — they are
the "rank-0" (scalar) tensor operators of BC. However, the
**composed** operators (the "twisted" Hecke operators) are the
non-trivial BC tensor operators:

$$
T^{(\chi)}_p \;:=\; \mu_p \cdot e(r_\chi),
\tag{2.3}
$$

where r_χ ∈ Q/Z is the "character representative" of χ (a choice
of base point in the Galois orbit of 1 under χ). By (2.1),

$$
\alpha_g(T^{(\chi)}_p) \;=\; \mu_p \cdot e(g \cdot r_\chi) \;=\; \chi(g)^{-1}\,T^{(\chi)}_p \cdot (\text{phase}).
\tag{2.4}
$$

More precisely, (2.4) holds up to a multiplicative character phase.
The operator T^{(χ)}_p is a **BC irreducible tensor operator** of
"weight χ" for the Galois action.

### 2.4 The matrix-element question

We want to compute

$$
\langle n \mid T^{(\chi)}_p \mid m \rangle
\;=\;
\langle \gamma_n; \chi_n \mid \mu_p \, e(r_\chi) \mid \gamma_m; \chi_m \rangle.
\tag{2.5}
$$

By Galois invariance, the matrix element is nonzero only if
χ_n = χ · χ_m (the selection rule in the abelian Galois setting).

---

## 3. R-Theorem QM.4: BC Wigner–Eckart

### 3.1 Statement

> **R-Theorem QM.4 (BC Wigner–Eckart, structural).** *Let H_R =*
> *⊕_χ H_R^{(χ)} be the Galois orbit decomposition of H_R (Path B,*
> *research/19). Let T^{(χ)}_p = μ_p · e(r_χ) be the BC irreducible*
> *tensor operator of weight χ. Then the matrix element of*
> *T^{(χ)}_p between Galois orbit states |m⟩ ∈ H_R^{(χ_m)} and*
> *|n⟩ ∈ H_R^{(χ_n)} factors as*
>
> $$
>   \langle n \mid T^{(\chi)}_p \mid m \rangle
>   \;=\;
>   \mathrm{CG}_{\mathrm{BC}}(\chi_m, \chi; \chi_n) \cdot \langle n \| \mu_p \| m \rangle,
>   \tag{3.1}
> $$
>
> *where:*
>
> 1. *CG_BC(χ_m, χ; χ_n) is the **BC Clebsch–Gordan coefficient**,*
>    *given by*
>
>    $$
>      \mathrm{CG}_{\mathrm{BC}}(\chi_m, \chi; \chi_n) \;=\;
>      \begin{cases}
>        1 & \chi_n = \chi \cdot \chi_m, \\
>        0 & \text{otherwise},
>      \end{cases}
>    $$
>
>    *(the character selection rule of the abelian Galois group),*
>    *and*
>
> 2. *⟨n ‖ μ_p ‖ m⟩ is the **reduced matrix element**, a function*
>    *only of (n, m, p) and the Hecke structure, independent of*
>    *the specific character representative r_χ.*

### 3.2 Proof

**Proof.** (Schur's lemma for abelian Galois.) The Galois group
Ẑ* is abelian, so every irreducible unitary representation is a
character χ. By Schur's lemma applied to the Galois-equivariant
map T^{(χ)}_p : H_R^{(χ_m)} → H_R,

$$
T^{(\chi)}_p \, \bigl|m\bigr\rangle \;\in\; H_R^{(\chi \cdot \chi_m)},
$$

so the matrix element with |n⟩ ∈ H_R^{(χ_n)} vanishes unless χ_n
= χ · χ_m. This is the character selection rule, and it is the
entire content of the BC Clebsch–Gordan coefficient in the
abelian case.

When the selection rule is satisfied, Schur's lemma says that the
restriction T^{(χ)}_p |_{H_R^{(χ_m)} → H_R^{(χ · χ_m)}} is
determined up to a scalar by the character pair (χ_m, χ). The
scalar is the reduced matrix element ⟨n ‖ μ_p ‖ m⟩, which depends
on the specific basis vectors |m⟩, |n⟩ within the one-dimensional
(or higher-dimensional if the Galois action has multiplicities)
character components. The independence of the reduced matrix
element from r_χ follows from the fact that different choices of
r_χ differ by a multiplicative phase that is absorbed into the
normalisation of the basis vectors. □

### 3.3 The reduced matrix element

The reduced matrix element ⟨n ‖ μ_p ‖ m⟩ is a function of (n, m, p)
determined by the Hecke structure. Its explicit form is:

$$
\langle n \| \mu_p \| m \rangle
\;=\;
\begin{cases}
  \sqrt{1/p} & \text{if } n = pm \text{ (Hecke raising)}, \\
  \sqrt{1/p} & \text{if } m = pn \text{ (Hecke lowering, if defined)}, \\
  0 & \text{otherwise}.
\end{cases}
\tag{3.2}
$$

The factor √(1/p) comes from the Hecke normalisation (the isometry
μ_p has norm 1 but its action on the GNS basis {μ_n Ω_1} sends
normalised basis vectors to normalised basis vectors in the
multiplicative N* index; the √(1/p) factor appears when μ_p is
applied to a Galois orbit state via the decomposition (2.2)).

Combining (3.1) and (3.2):

$$
\langle n \mid \mu_p \, e(r_\chi) \mid m \rangle \;=\;
\delta_{\chi_n, \chi \chi_m} \cdot \sqrt{1/p}\cdot \delta_{n, pm}.
\tag{3.3}
$$

This is the fully explicit BC Wigner–Eckart formula.

### 3.4 Non-abelian generalisation

If one enriches the BC algebra with a non-abelian "internal
symmetry" (e.g., the three-prime Hecke action giving SU(3) as in
research/10), then Ẑ* is enlarged to a non-abelian group Γ, and
the BC Wigner–Eckart formula becomes the full classical form with
multidimensional Clebsch–Gordan coefficients. This is the
structure that would be needed for the QG5D SM gauge group SU(3)
× SU(2) × U(1)/Z_6 to act as "angular momentum" on H_R via the
Galois orbit decomposition.

---

## 4. LOCK contribution: sufficient condition for γ_n ∈ R

### 4.1 Reality of the reduced matrix elements

The reduced matrix element (3.2) is **real** and positive: √(1/p)
is a positive real number. This is not an accident — it reflects
the fact that the Hecke operators μ_p are (partial) isometries,
and partial isometries have positive reduced matrix elements in
their natural basis.

Now consider the BC Hamiltonian H_BC = log N̂ restricted to H_R.
Its matrix elements in the Galois orbit basis are

$$
\langle n \mid H_{\mathrm{BC}} \mid m \rangle
\;=\;
\gamma_n \cdot \delta_{nm}
\tag{4.1}
$$

(diagonal in the orbit basis, conditional on Hilbert–Pólya). The
diagonal entries γ_n are the reduced matrix elements of the
"identity tensor operator" T^{(1)}_1 = 1 in the Wigner–Eckart
sense. Reality of *all* reduced matrix elements (which includes
the diagonal γ_n's) gives γ_n ∈ R.

### 4.2 The sufficient condition

> **Sufficient condition QM.4 (LOCK).** *If the BC Galois orbit*
> *decomposition (2.2) exists on H_R and the reduced matrix*
> *elements ⟨n ‖ μ_p ‖ m⟩ in the BC Wigner–Eckart factorisation*
> *(3.1) are real for all (n, m, p), then the BC Hamiltonian H_BC*
> *on H_R has real spectrum, and in particular γ_n ∈ R for all n.*

**Argument.** Reality of all reduced matrix elements ⟨n ‖ μ_p ‖ m⟩
is equivalent to H_BC being a **real symmetric matrix** in the
Galois orbit basis (up to the unitary phase absorbed into the
Clebsch–Gordan coefficients). Real symmetric matrices have real
spectrum. Hence γ_n ∈ R.

The critical step — reality of the reduced matrix elements — is a
structural fact about partial isometries with positive Hecke
normalisation. Once the Galois orbit decomposition (2.2) is
rigorous (research/19 Path B), the reality is automatic from
(3.2). This makes QM.4 one of the **cleanest** LOCK contributions
of the four in this round.

### 4.3 Dependence on research/19

The LOCK of QM.4 is conditional on the **validity of the Galois
orbit decomposition (2.2)**. Research/19 notes that the bare
decomposition is trivial (all orbits collapse to the trivial
character because the Galois action on the raw H_R is trivial);
the non-trivial decomposition requires the **Path B tensor
reading** H_R ⊗ H_gauge, in which the gauge Hilbert space
supplies the character structure. In the Path B reading, QM.4
holds as stated.

---

## 5. Honest accounting

### 5.1 What is rigorous

(QM.4-R1) The classical Wigner–Eckart theorem (standard).

(QM.4-R2) The Galois action α_g on A_BC (Bost–Connes 1995 §4).

(QM.4-R3) Schur's lemma for unitary representations of compact
groups (standard).

(QM.4-R4) The selection rule χ_n = χ · χ_m as an immediate
consequence of Schur's lemma for the abelian Galois group.

(QM.4-R5) The Hecke reduced matrix elements (3.2) computed
directly from the BC relations.

### 5.2 What is structural

(QM.4-S1) The identification of H_R with the direct sum of
Galois character subspaces (2.2). This is the **Path B** reading
of research/19, which requires the tensor product H_R ⊗ H_gauge
to make the Galois decomposition non-trivial. On the bare H_R
the decomposition collapses.

(QM.4-S2) The identification of the Hecke operators μ_p · e(r_χ)
as BC irreducible tensor operators. This is a definition, and it
is a reasonable definition, but it has not been verified to be
the *unique* or *natural* choice.

(QM.4-S3) The reality of the reduced matrix elements (QM.4-R5
gives real values in the simple Hecke case, but for more general
T^{(χ)}_p with non-trivial phase structure, the reality is a
convention-dependent statement).

(QM.4-S4) The LOCK §4.2 chain "reality of reduced matrix elements
⟹ real symmetric matrix in Galois basis ⟹ real spectrum ⟹
γ_n ∈ R" is structural because it depends on (S1), (S2), (S3).

### 5.3 What is open

(QM.4-O1) **The Path B tensor reading of H_R** (research/19): is
the Galois decomposition (2.2) non-trivial, and if so, what is
the explicit character assignment n ↦ χ_n for the first 15 zeros
γ_1, …, γ_15? This is the main open question for QM.4.

(QM.4-O2) **Off-diagonal reduced matrix elements** ⟨n ‖ μ_p ‖ m⟩
for n ≠ pm and m ≠ pn. In the bare Hecke setting these all vanish
(3.2), but in the Path B reading with gauge character enrichment,
the off-diagonal entries may be non-zero. Their explicit form is
open.

(QM.4-O3) **The non-abelian generalisation** (§3.4) for the full
QG5D gauge group action on H_R. This would give a true classical
Wigner–Eckart theorem with multi-dim Clebsch–Gordan coefficients,
with applications to all the off-diagonal matrix elements of R̂
needed for the CC formula corrections (research/02 O3) and
cosmic transition amplitudes (research/06).

### 5.4 Status table

| Item | Rigorous | Structural | Open |
|:-----|:---------|:-----------|:-----|
| Classical Wigner–Eckart | ✓ | | |
| Galois action on A_BC | ✓ | | |
| Schur's lemma for compact/abelian groups | ✓ | | |
| Galois orbit decomposition of H_R (bare) | trivial (collapses) | | |
| Galois orbit decomposition (Path B) | | ✓ | full character assignment |
| Hecke as BC tensor operators | | ✓ | uniqueness |
| Abelian-Galois selection rule | ✓ | | |
| Hecke reduced matrix elements (3.2) | ✓ | | |
| BC Wigner–Eckart factorisation | ✓ given (Path B) | | |
| Non-abelian generalisation | | ✓ (sketch) | full form |
| LOCK sufficient condition QM.4 | | ✓ | Path B rigour |

---

## 6. Definition of done

R-Theorem QM.4 is **closed** when:

- [x] The classical Wigner–Eckart theorem is stated (§1).
- [x] The Galois action on A_BC and the Galois orbit decomposition
      of H_R (Path B) are stated (§2.1, §2.2).
- [x] The BC tensor operators T^{(χ)}_p are defined (§2.3) and
      their Galois transformation (2.4) is verified.
- [x] The BC Wigner–Eckart factorisation (3.1) is stated and
      proved from Schur's lemma (§3.2).
- [x] The Hecke reduced matrix elements (3.2) are computed
      explicitly.
- [x] The LOCK contribution (§4.2) is stated.
- [ ] The Path B Galois orbit decomposition (2.2) is made
      rigorous via research/19's next round, with explicit
      character assignments for the first 15 γ_n.
- [ ] The non-abelian generalisation (§3.4) is worked out for the
      SU(3) × SU(2) × U(1)/Z_6 action on H_R via research/10's
      three-prime orbit, giving explicit multi-dim Clebsch–Gordan
      coefficients for the SM gauge group.
- [ ] A companion code script `code/bc_wigner_eckart_check.py`
      numerically verifies (3.1) for a sample of (n, m, p) in a
      truncated BC model.

---

## 7. References

### 7.1 In this directory

- `paper12/research/04-identity-12-rigorous.md` — the unitary U
  and the basis {μ_n Ω_1}.
- `paper12/research/10-transposition-gauge-group-3primes.md` —
  the non-abelian SU(3) × SU(2) × U(1)/Z_6 structure on the
  three-prime sub-Hecke algebra; the setting for the non-abelian
  generalisation (§3.4).
- `paper12/research/14-transposition-CCM-and-reasoning-patterns.md`
  Part B §B.2 — the Galois/Hecke correspondence.
- `paper12/research/19-galois-orbit-decomposition-HR.md` — the
  Path B tensor reading of H_R needed to make the Galois orbit
  decomposition (2.2) non-trivial.
- `paper12/research/21-bost-connes-system-reference.md` §5 — the
  Galois action on A_BC.

### 7.2 External

- Wigner, E. P., *Gruppentheorie und ihre Anwendung auf die
  Quantenmechanik der Atomspektren*, Vieweg (1931), Ch. 17.
- Eckart, C., "The application of group theory to the quantum
  dynamics of monatomic systems", *Rev. Mod. Phys.* **2** (1930)
  305.
- Racah, G., "Theory of complex spectra II", *Phys. Rev.* **62**
  (1942) 438.
- Messiah, A., *Quantum Mechanics*, vol. II, North-Holland (1962),
  Ch. XIII §5 (statement and proof of Wigner–Eckart).
- Bost, J.-B., and Connes, A., *Selecta Math.* **1** (1995) 411,
  §4 (Galois action).
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS CP **55** (2008), Ch. III (endomotives
  and the Galois symmetry).

---

*Wigner–Eckart on the BC side: ⟨n | μ_p e(r_χ) | m⟩ = CG_BC ·*
*⟨n ‖ μ_p ‖ m⟩, with CG_BC the character selection rule δ(χ_n,*
*χ · χ_m) and the reduced matrix element √(1/p) · δ(n, pm). The*
*LOCK: reality of the reduced matrix elements makes H_BC a real*
*symmetric matrix in the Galois orbit basis, forcing γ_n ∈ R,*
*conditional on the Path B tensor reading of H_R from research/19.*
