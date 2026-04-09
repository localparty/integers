# Research 83: Wigner–Eckart Real-Symmetric Test

*Numerical test of whether H_BC and T_BC are real symmetric in the*
*Path B Galois orbit basis on the 8-dim cube sub-Hilbert space H_□,*
*with explicit computation of the Hecke reduced matrix elements*
*⟨n‖μ_p‖m⟩ for p ∈ {2, 3, 5}.*

*Authors: G Six, with Claude Opus 4.6 (1M context)*
*Date opened: 2026-04-09*
*Depends on: research/60 (R-Theorem QM.4, Wigner–Eckart LOCK),*
*research/19 (Path B tensor reading), research/10 (Theorem 10,*
*cube H_□), research/80 (BC-intrinsic SU(3) closure).*
*Companion script: `paper12/code/wigner_eckart_real_symmetric_test.py`.*

---

## 0. One-paragraph summary

Research/60 (R-Theorem QM.4) identified a potentially short path
to RH: if the Hecke reduced matrix elements ⟨n‖μ_p‖m⟩ = √(1/p) make
the BC Hamiltonian H_BC a real symmetric matrix in the Galois orbit
basis, then real symmetric implies real spectrum in one line. This note
performs the explicit numerical test on the 8-dimensional cube
sub-Hilbert space H_□ = span{μ_{2^a 3^b 5^c} Ω_1 : a,b,c ∈ {0,1}},
using the Path B Galois orbit basis (the 1 ⊕ 1 ⊕ 3 ⊕ 3̄
decomposition of research/80 §3). The results are:

1. **H_BC = log N̂ is real symmetric in the Path B basis** — trivially,
   because the Path B basis change V is a real orthogonal matrix and
   H_BC is real diagonal. This is confirmed numerically.

2. **Any diagonal operator with real eigenvalues is automatically real
   symmetric in the Path B basis** — for the same reason (V real
   orthogonal implies V^T D V real symmetric for real diagonal D).

3. **The Hecke reduced matrix elements are real, positive, and
   symmetric**: ⟨n‖μ_p‖m⟩ = √(1/p) when n = pm or m = pn, and
   zero otherwise. All three 8×8 reduced-matrix-element matrices are
   real symmetric.

4. **CRITICAL FINDING: The Path B basis does NOT independently force
   T_BC to be real symmetric.** It *preserves* real symmetry (if T_BC
   already has real spectrum, it remains real symmetric after the basis
   change) but does not *create* it. The implication runs
   (γ_n ∈ R) ⟹ (T_BC real symmetric in Path B), NOT the reverse.
   The LOCK of research/60 §4.2 is therefore a structural consistency
   constraint, not a one-line proof of RH.

---

## 1. Setup: the cube H_□ and its bases

### 1.1 Standard basis

The cube H_□ (research/10 Lemma 4.1) has orthonormal basis

$$
\{|\mathbf{v}\rangle\} = \{\mu_{2^a 3^b 5^c}\,\Omega_1 : a, b, c \in \{0, 1\}\},
$$

indexed by (a, b, c) ∈ {0, 1}³, giving 8 basis vectors corresponding
to the squarefree 30-smooth integers {1, 2, 3, 5, 6, 10, 15, 30}.
The index ordering follows research/80 §2.1: i(a,b,c) = 4a + 2b + c.

### 1.2 H_BC in the standard basis

H_BC = log N̂ is diagonal:

$$
H_{\mathrm{BC}} = \mathrm{diag}(\log 1, \log 5, \log 3, \log 15,
\log 2, \log 10, \log 6, \log 30).
$$

All eigenvalues are real and non-negative.

### 1.3 The Path B basis (Galois orbit basis)

From research/80 §3 and research/19 §4.2 (Path B tensor reading),
the Galois orbit basis of H_□ is the 1 ⊕ 1 ⊕ 3 ⊕ 3̄ decomposition
under the Z/3 cyclic symmetry of {2, 3, 5}:

| Index | Label | Vector | Sector |
|:------|:------|:-------|:-------|
| 0 | S_+ | (Ω_1 + μ_{30} Ω_1)/√2 | GHZ singlet |
| 1 | S_- | (Ω_1 - μ_{30} Ω_1)/√2 | anti-GHZ singlet |
| 2 | e_2 | μ_2 Ω_1 | fundamental 3 |
| 3 | e_3 | μ_3 Ω_1 | fundamental 3 |
| 4 | e_5 | μ_5 Ω_1 | fundamental 3 |
| 5 | e_{15} | μ_{15} Ω_1 | antifundamental 3̄ |
| 6 | e_{10} | μ_{10} Ω_1 | antifundamental 3̄ |
| 7 | e_6 | μ_6 Ω_1 | antifundamental 3̄ |

### 1.4 The basis change matrix V

The basis change V : standard → Path B is an 8×8 real orthogonal
matrix (V^T V = V V^T = I, all entries real). The only non-trivial
mixing is in the singlet sector:

$$
V = \begin{pmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & & & & & & \\
& & & & 1 & & & \\
& & & 1 & & & & \\
& & & & & 1 & & \\
& & 1 & & & & & \\
& & & & & & 1 & \\
& & & & & & & 1 \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} & & & & & &
\end{pmatrix}
$$

(blank entries are zero). The script verifies V^T V = I and V V^T = I
to machine precision.

**Key property:** V is real orthogonal. This single fact determines
whether the Path B basis change can force or merely preserve real
symmetry.

---

## 2. H_BC in the Path B basis

### 2.1 The matrix

The script computes H_BC^{(B)} = V^T H_BC V explicitly:

$$
H_{\mathrm{BC}}^{(B)} = \begin{pmatrix}
1.7006 & -1.7006 & 0 & 0 & 0 & 0 & 0 & 0 \\
-1.7006 & 1.7006 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0.6931 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1.0986 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1.6094 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 2.7081 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 2.3026 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1.7918
\end{pmatrix}.
$$

The off-diagonal entry -1.7006 = (log 1 - log 30)/2 in the singlet
block is the mixing between S_+ and S_- induced by the GHZ
superposition.

### 2.2 Verdict

> **H_BC is REAL SYMMETRIC in the Path B basis.**

This is confirmed numerically (H_BC^{(B)} = (H_BC^{(B)})^T to
machine precision, all entries real). The eigenvalues of H_BC^{(B)}
match {log 1, log 2, log 3, log 5, log 6, log 10, log 15, log 30}
exactly.

### 2.3 Why this is trivial

V is real orthogonal and H_BC is real diagonal. Therefore
V^T (real diagonal) V is automatically real symmetric. This holds
for ANY real orthogonal basis change applied to ANY real diagonal
matrix. It is a basic linear algebra fact, not a deep property of
the BC system or the Galois orbit decomposition.

---

## 3. Generic diagonal operators: the key theorem

### 3.1 Statement

> **Theorem (trivial).** *Let V ∈ O(n, R) be a real orthogonal*
> *matrix and D = diag(λ_1, ..., λ_n) a real diagonal matrix.*
> *Then V^T D V is real symmetric.*

**Proof.** (V^T D V)^T = V^T D^T (V^T)^T = V^T D V, since D is
symmetric (diagonal) and V^T = V^{-1}. All entries are real because
V and D are real. QED.

### 3.2 Application to T_BC

If T_BC were diagonal on H_□ with REAL eigenvalues λ_n (which it is
NOT — T_BC lives on H_R, not on H_□ — but structurally), then the
Path B basis change would automatically make it real symmetric. This
is what the script verifies with a random real diagonal matrix: the
result is always real symmetric, regardless of the diagonal entries.

### 3.3 The failure mode: complex eigenvalues

If T_BC had eigenvalues γ_n ∈ C (i.e., RH fails), then D would have
complex diagonal entries, and V^T D V would have complex entries.
Specifically, (V^T D V)^T = V^T D V (still symmetric as a complex
matrix), but it would NOT be Hermitian:

$$
(V^T D V)^\dagger = V^T D^* V \neq V^T D V
$$

when D ≠ D^*. So the matrix would be complex symmetric but NOT
Hermitian, and its eigenvalues could be complex.

---

## 4. The Hecke reduced matrix elements

### 4.1 Computation

The reduced matrix elements ⟨n‖μ_p‖m⟩ of research/60 eq. (3.2)
are computed explicitly on the cube for all p ∈ {2, 3, 5} and
n, m ∈ {1, 2, 3, 5, 6, 10, 15, 30}.

**For p = 2:** ⟨n‖μ_2‖m⟩ = 1/√2 ≈ 0.7071 for the pairs

  (m, n) ∈ {(1,2), (3,6), (5,10), (15,30)} and their transposes.

**For p = 3:** ⟨n‖μ_3‖m⟩ = 1/√3 ≈ 0.5774 for the pairs

  (m, n) ∈ {(1,3), (2,6), (5,15), (10,30)} and their transposes.

**For p = 5:** ⟨n‖μ_5‖m⟩ = 1/√5 ≈ 0.4472 for the pairs

  (m, n) ∈ {(1,5), (2,10), (3,15), (6,30)} and their transposes.

All other matrix elements vanish.

### 4.2 Properties

Each 8×8 reduced-matrix-element matrix R_p (with entries
(R_p)_{nm} = ⟨n‖μ_p‖m⟩) is:

1. **Real**: all entries are in R (specifically, √(1/p) or 0).
2. **Non-negative**: all entries are ≥ 0.
3. **Symmetric**: R_p = R_p^T.

Property 3 follows from the symmetry of the Hecke relation: n = pm
if and only if m = pn is false, but ⟨n‖μ_p‖m⟩ is defined to be
√(1/p) for BOTH n = pm (raising) and m = pn (lowering), making the
matrix symmetric by construction.

### 4.3 Relation to the Hecke operators on H_□

The reduced matrix elements R_p are NOT the same as the Hecke
operators μ_p restricted to H_□. The Hecke operator μ_p is a
**non-symmetric** partial isometry (it raises but does not lower),
while R_p is a **symmetric** matrix encoding both raising and
lowering transitions with the same weight √(1/p).

Specifically:
- μ_p (on H_□) = raising half of R_p, scaled by √p.
- μ_p^* (on H_□) = lowering half of R_p, scaled by √p.
- T_p := μ_p + μ_p^* = √p · R_p (the self-adjoint Hecke combination).

The self-adjoint combinations T_p = μ_p + μ_p^* are real symmetric
in BOTH the standard and Path B bases, with eigenvalues ±1 (each
with multiplicity 4).

---

## 5. The Hecke operators in the Path B basis

### 5.1 μ_p in the Path B basis

The script computes μ_p^{(B)} = V^T μ_p V for each p. These are
NOT symmetric — μ_p is a partial isometry, not self-adjoint. The
Hecke operators mix the singlet sector with the 3 and 3̄ sectors:

- μ_2 maps S_± into the e_2 (fundamental) direction and maps e_{15}
  (antifundamental) into the S_± sector.
- Similarly for μ_3 and μ_5 with cyclic permutation.

### 5.2 T_p = μ_p + μ_p^* in the Path B basis

The self-adjoint combinations T_p = μ_p + μ_p^* are real symmetric
in the Path B basis, verified numerically. All three have eigenvalues
{-1, -1, -1, -1, +1, +1, +1, +1}. The 2×2 singlet block of each
T_p^{(B)} has entries ±1/√2, reflecting the GHZ structure.

---

## 6. Critical analysis: does Path B force real symmetry of T_BC?

### 6.1 The one-line argument that FAILS

The hoped-for argument was:

> "The Path B Galois orbit basis makes H_BC real symmetric. Since
> T_BC lives in the same algebra, it should also be real symmetric
> in this basis. Real symmetric implies real spectrum. Therefore
> γ_n ∈ R. QED."

This argument fails at the second sentence. T_BC being "in the same
algebra" does NOT make it real symmetric in the Galois orbit basis.
The reason is elementary:

1. V is real orthogonal.
2. V^T M V is real symmetric if and only if M is real symmetric.
3. T_BC (restricted to H_R) is self-adjoint if and only if its
   eigenvalues are real — this is the CONTENT of RH, not a
   consequence of the basis change.

The Path B basis change is a **red herring** for proving RH. It
does not add information about the spectrum of T_BC; it merely
re-expresses the same operator in a different basis.

### 6.2 What the Wigner–Eckart structure DOES give

The Wigner–Eckart factorisation of research/60 gives:

$$
\langle n | T_p^{(\chi)} | m \rangle = \mathrm{CG}_{\mathrm{BC}}(\chi_m, \chi; \chi_n) \cdot \langle n \| \mu_p \| m \rangle,
$$

with ⟨n‖μ_p‖m⟩ = √(1/p) real and positive. This means:

- The Hecke transition amplitudes factor cleanly into a selection
  rule (CG_BC) and a universal real factor (√(1/p)).
- The Hecke operators have a "maximally transparent" form in the
  Galois orbit basis: all the non-trivial structure is in the
  CG coefficient, and the reduced matrix element is a trivial
  positive real number.

This is a STRUCTURAL CONSISTENCY CONDITION: if the Galois orbit
decomposition exists (Path B), then the Hecke operators are
automatically well-behaved (real reduced matrix elements). This is
a necessary condition for the framework to be self-consistent, but
it does not by itself force γ_n ∈ R.

### 6.3 The correct logical chain

The honest logical chain is:

1. (RIGOROUS) The Hecke operators μ_p are partial isometries with
   real, positive reduced matrix elements √(1/p) on H_□.

2. (RIGOROUS) The Path B basis change V is real orthogonal.

3. (RIGOROUS) H_BC = log N̂ is real symmetric in the Path B basis
   (consequence of 1 and 2).

4. (STRUCTURAL) If T_BC has real eigenvalues (i.e., RH holds),
   then T_BC is real symmetric in the Path B basis (consequence
   of 2).

5. (STRUCTURAL) If the Galois orbit decomposition makes T_BC
   manifestly self-adjoint (i.e., if T_BC can be constructed as
   a real symmetric matrix from the Hecke data alone), then
   γ_n ∈ R follows.

6. (OPEN) Step 5 requires showing that the BC algebra plus the
   Galois orbit structure DETERMINE T_BC as a self-adjoint
   operator. This is the Connes trace formula / explicit formula
   content, and it is the genuine mathematical content of the
   Hilbert-Polya programme.

### 6.4 Where the gap is

The gap is between "the Hecke reduced matrix elements are real" and
"T_BC is self-adjoint". The reduced matrix elements describe the
Hecke operators μ_p, not the BC Hamiltonian T_BC. The Hamiltonian
T_BC is built from the Hecke data via the Connes trace formula
(the BC analog of the Riemann-Weil explicit formula), and the
self-adjointness of T_BC is the OUTPUT of that construction, not
an INPUT.

In other words: the Wigner-Eckart factorisation tells us that the
BUILDING BLOCKS (Hecke operators) are well-behaved. Whether the
ASSEMBLED OBJECT (T_BC) is self-adjoint depends on HOW they are
assembled (via the trace formula), and this is where the actual
mathematical content of RH lives.

---

## 7. Comparison with research/60 §4.2

### 7.1 What research/60 claims

Research/60 §4.2 states:

> "Reality of all reduced matrix elements ⟨n‖μ_p‖m⟩ is equivalent
> to H_BC being a real symmetric matrix in the Galois orbit basis
> (up to the unitary phase absorbed into the Clebsch-Gordan
> coefficients). Real symmetric matrices have real spectrum.
> Hence γ_n ∈ R."

### 7.2 What the computation shows

The computation confirms that the reduced matrix elements are indeed
real, and that H_BC (= log N̂) is indeed real symmetric in the Path B
basis. However, the leap from "H_BC real symmetric" to "γ_n ∈ R" has
a structural gap:

- H_BC = log N̂ has eigenvalues {log n}, which are trivially real.
- T_BC (the operator whose eigenvalues are {γ_n}) is a DIFFERENT
  operator from H_BC, and its real symmetry is not a consequence of
  the Hecke reduced matrix elements alone.

The phrase "the BC Hamiltonian H_BC on H_R has real spectrum" in
research/60 §4.2 is ambiguous: if "H_BC" means log N̂, its spectrum
is trivially real; if "H_BC" means T_BC (the scaling operator on H_R
whose zeros give {γ_n}), then its real symmetry needs an independent
argument.

### 7.3 Honest re-assessment of the LOCK

The LOCK of QM.4 should be re-stated as:

> **LOCK QM.4 (corrected).** The Wigner-Eckart factorisation with
> real reduced matrix elements is a NECESSARY CONDITION for the
> consistency of the Galois orbit decomposition of H_R under Path B.
> If T_BC is self-adjoint (i.e., RH holds), then the entire
> framework is consistent: the Hecke operators, the Galois
> decomposition, and the reduced matrix elements all fit together
> coherently. If T_BC is NOT self-adjoint (i.e., RH fails), then
> the Path B Galois orbit decomposition cannot be realized as
> stated (because the Galois orbits would involve complex
> eigenspaces that do not admit a real-orthogonal basis change).
>
> This makes the LOCK a CONSISTENCY CHECK, not a proof: the
> framework predicts γ_n ∈ R, and if γ_n ∉ R the framework breaks.
> The LOCK does not independently prove γ_n ∈ R.

---

## 8. Honest accounting

### 8.1 What is rigorous

(83-R1) The cube H_□ has orthonormal basis {μ_{2^a 3^b 5^c} Ω_1}
with dim H_□ = 8 (research/10 Lemma 4.1, Bost-Connes Theorem 25).

(83-R2) The Hecke operators μ_p (p ∈ {2,3,5}) act as Pauli raisings
σ_+^{(i)} on H_□, and their adjoints μ_p^* as Pauli lowerings.

(83-R3) The BC relations μ_p μ_q = μ_{pq}, [μ_p, μ_q] = 0 (p ≠ q),
and [H_BC, μ_p] = log(p) μ_p hold as 8×8 matrix identities.

(83-R4) The Hecke reduced matrix elements ⟨n‖μ_p‖m⟩ = √(1/p) are
real, positive, and symmetric in (n, m) for all p ∈ {2,3,5} and
n, m ∈ {1, 2, 3, 5, 6, 10, 15, 30}.

(83-R5) The Path B basis change V is real orthogonal (V^T V = I,
all entries real).

(83-R6) H_BC = log N̂ is real symmetric in the Path B basis
(consequence of R4 and R5).

(83-R7) The self-adjoint Hecke combinations T_p = μ_p + μ_p^* are
real symmetric in the Path B basis, with eigenvalues ±1.

### 8.2 What is structural

(83-S1) The Path B Galois orbit decomposition (research/19 §4.2) as
the correct interpretation of the Galois orbit structure on H_R.

(83-S2) The identification of T_BC eigenvalues with {γ_n} requires
the Hilbert-Polya conjecture for the BC system (research/02).

(83-S3) The LOCK of QM.4 (research/60 §4.2) as a consistency
constraint on the framework.

### 8.3 What is open

(83-O1) Whether the Path B basis change forces T_BC to be
self-adjoint. The computation shows it does NOT — the basis change
preserves but does not create real symmetry.

(83-O2) The construction of T_BC from Hecke data via the Connes
trace formula. This is where the self-adjointness of T_BC (and hence
RH) would need to be proved.

(83-O3) The extension of this test from the 8-dim cube H_□ to the
full infinite-dimensional H_R.

---

## 9. Status table

| Item | Status |
|:-----|:-------|
| H_□ orthonormal basis, dim = 8 | **RIGOROUS** |
| H_BC = log N̂ diagonal, real eigenvalues | **RIGOROUS** |
| Hecke μ_p as 8×8 matrices on H_□ | **RIGOROUS** |
| BC relations verified as matrix identities | **RIGOROUS** |
| Path B basis V real orthogonal | **RIGOROUS** |
| H_BC real symmetric in Path B basis | **RIGOROUS** (trivially) |
| Reduced matrix elements real, positive, symmetric | **RIGOROUS** |
| T_p = μ_p + μ_p^* real symmetric in Path B | **RIGOROUS** |
| T_BC real symmetric in Path B ⟹ γ_n ∈ R | **TAUTOLOGICAL** (real sym ⟹ real eigenvalues is true, but T_BC being real sym is what needs proof) |
| Path B forces T_BC real symmetric | **FALSE** (V preserves but does not create real symmetry) |
| LOCK QM.4 as consistency constraint | **STRUCTURAL** |

---

## 10. Definition of done

This note is closed when:

- [x] The cube H_□ basis is constructed and verified (§1).
- [x] H_BC is computed in the Path B basis and confirmed real
      symmetric (§2).
- [x] The generic diagonal operator test is performed, showing that
      V real orthogonal trivially preserves real symmetry (§3).
- [x] The Hecke reduced matrix elements are computed explicitly for
      all (n, m, p) with p ∈ {2,3,5} (§4).
- [x] The Hecke operators and self-adjoint combinations are computed
      in the Path B basis (§5).
- [x] The critical analysis is performed: Path B does NOT force T_BC
      real symmetric (§6).
- [x] The LOCK of QM.4 is re-assessed as a consistency constraint
      rather than a proof (§7).
- [x] The companion script runs end-to-end with all assertions
      passing.

---

## 11. Key finding for the programme

The hoped-for "one-line proof" does not work as stated. The Path B
Galois orbit basis is a REAL ORTHOGONAL basis change, which trivially
preserves real symmetry of any self-adjoint operator but does not
create it. The Wigner-Eckart reduced matrix elements being real is a
necessary condition for framework consistency, not a sufficient
condition for γ_n ∈ R.

However, the computation reveals a positive structural insight: the
self-adjoint Hecke combinations T_p = μ_p + μ_p^* have eigenvalues
exactly ±1 in the cube, and are real symmetric in the Path B basis.
This means the BUILDING BLOCKS of the BC algebra are as well-behaved
as possible for a self-adjointness argument. The gap is in the
ASSEMBLY — the Connes trace formula that builds T_BC from the Hecke
data — not in the building blocks themselves.

The next step is to investigate whether the Connes trace formula
construction of T_BC from {T_p} inherits the real-symmetric property
of its ingredients. This is thread T7 of research/20 (trace formula
self-adjointness), not thread QM.4.

---

## 12. References

### 12.1 In this directory

- `paper12/research/04-identity-12-rigorous.md` — the unitary
  U : H_e → H_1 and the basis {μ_n Ω_1}.
- `paper12/research/10-transposition-gauge-group-3primes.md` —
  Theorem 10, the cube H_□, the GHZ state Ψ_3.
- `paper12/research/19-galois-orbit-decomposition-HR.md` — the
  Path B tensor reading of H_R.
- `paper12/research/60-transposition-wigner-eckart.md` — R-Theorem
  QM.4, the Wigner-Eckart LOCK.
- `paper12/research/80-finite-C8-bracket-calculation.md` — the
  1 ⊕ 1 ⊕ 3 ⊕ 3̄ decomposition of H_□ and BC-intrinsic SU(3).
- `paper12/code/wigner_eckart_real_symmetric_test.py` — companion
  script performing all numerical checks.

### 12.2 External

- Bost, J.-B., Connes, A., "Hecke algebras, type III factors and
  phase transitions with spontaneous symmetry breaking in number
  theory", *Selecta Math.* **1** (1995) 411-457.
- Connes, A., "Trace formula in noncommutative geometry and the
  zeros of the Riemann zeta function", *Selecta Math.* **5** (1999)
  29-106.
- Wigner, E. P., *Gruppentheorie und ihre Anwendung auf die
  Quantenmechanik der Atomspektren*, Vieweg (1931).

---

*The Path B basis is real orthogonal. Real orthogonal preserves real*
*symmetry but does not create it. The Hecke building blocks are as*
*well-behaved as possible (real, positive, symmetric reduced matrix*
*elements). The gap is in the assembly: the Connes trace formula that*
*builds T_BC from {T_p}. The LOCK of QM.4 is a consistency constraint,*
*not a proof. The one-line argument does not close.*
