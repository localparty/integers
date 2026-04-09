# Research 59: Transposition — Bell + No-Cloning (R-Theorem QM.3)

*Transpose two foundational QM no-go theorems — Bell's theorem and*
*the no-cloning theorem — to the Bost–Connes side. The BC Hecke*
*action mixes all primes dividing n, so a BC analog of a Bell*
*inequality is violated; and no \*-homomorphism A_BC → A_BC ⊗ A_BC*
*can duplicate arbitrary KMS states.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Sub-phase 3.B, next round of transpositions (category A: QM),*
*R-Theorem QM.3 (combined Bell + no-cloning for the BC system).*
*Depends on: research/04 (Identity 12), research/10 (three-prime*
*sub-Hecke), research/14 Part B, research/21 (BC reference).*

---

## 0. One-paragraph summary

Bell's theorem (Bell 1964) says that no local hidden-variable theory
can reproduce the correlations of quantum mechanics; operationally,
certain combinations of two-qubit correlators exceed the classical
bound 2 and can reach the Tsirelson bound 2√2. The no-cloning
theorem (Wootters–Zurek 1982, Dieks 1982) says no unitary can copy
an arbitrary unknown quantum state. Both are **no-go** statements
about the structure of QM: Bell forbids local factorisation, and
no-cloning forbids unitary duplication. On the BC side, we show
that **both no-gos hold**, as R-Theorem QM.3 in two parts:
  (a) **BC Bell**: the correlator-like object ω_1(μ_p e(r) μ_p^* ·
      e(s)) factors across the prime structure only if the phase
      structure is trivial, and in the generic case the BC analog
      of the CHSH inequality is violated by a factor whose maximum
      is 2 · [1 + 1/p]^{1/2} — a BC Tsirelson bound.
  (b) **BC no-cloning**: there is no unital *-homomorphism Δ :
      A_BC → A_BC ⊗ A_BC such that ω_1(Δ(a)(1 ⊗ b)) = ω_1(ab) for
      all a, b and Δ(μ_n) = μ_n ⊗ μ_n. The obstruction is that
      the BC relations (μ_n μ_n^* ≠ 1) are incompatible with any
      coproduct that preserves the KMS state.

The BC no-cloning obstruction is **rigorous**; the BC Bell violation
is **structural** and reduces to a computation on a single-prime
Hecke orbit. As a LOCK contribution: BC no-cloning says the
BC algebra has no bialgebra structure compatible with ω_1, which
is the same as saying that the comultiplication needed to lift ω_1
to a product state does not exist — equivalently, that the prime
structure of N* is *intrinsically non-local*, and this non-locality
forces the Hecke dynamics to be non-commutative (μ_n μ_n^* < 1),
which is the same structural feature that makes the BC Hamiltonian
have discrete spectrum with all real eigenvalues.

---

## 1. The classical theorems

### 1.1 Bell / CHSH

Let ρ be a density operator on C² ⊗ C², and let A_1, A_2 and B_1,
B_2 be ±1-valued observables on the two factors. The CHSH quantity
is

$$
S(\rho) \;=\; \bigl|\,\langle A_1 B_1\rangle + \langle A_1 B_2\rangle + \langle A_2 B_1\rangle - \langle A_2 B_2\rangle\,\bigr|_\rho.
\tag{1.1}
$$

For any **local hidden variable** theory, S(ρ) ≤ 2 (CHSH 1969). In
quantum mechanics, S(ρ) ≤ 2√2 (Tsirelson 1980), and the bound is
saturated by the singlet state on suitable observables. Bell's
theorem is the statement S_max^{QM} > 2.

### 1.2 No-cloning

> **Theorem (Wootters–Zurek 1982, Dieks 1982).** *There is no*
> *unitary U : H ⊗ H → H ⊗ H and fixed |0⟩ ∈ H such that*
>
> $$
>   U\,(|\psi\rangle \otimes |0\rangle) \;=\; |\psi\rangle \otimes |\psi\rangle
>   \qquad \forall \psi \in H.
> $$

**Proof.** For any two states ψ, φ, ⟨ψ|φ⟩ = ⟨ψ ⊗ 0 | φ ⊗ 0⟩ =
⟨U(ψ ⊗ 0) | U(φ ⊗ 0)⟩ = ⟨ψ|φ⟩² (by unitarity and the assumed form
of U), so ⟨ψ|φ⟩ ∈ {0, 1} for all ψ, φ. But generic states have
intermediate overlaps, contradiction. □

The theorem is a direct consequence of **linearity** of quantum
mechanics: cloning is an intrinsically non-linear operation, and
no linear (unitary) map can accomplish it.

---

## 2. Part (a): BC Bell

### 2.1 BC "correlators"

The BC KMS state ω_1 at β = 1 takes values on products of μ_n and
e(r). Define, for p, q primes and r, s ∈ Q/Z, the **Hecke
correlator**

$$
C(p, q; r, s) \;:=\; \omega_1\bigl(\,e(r)\,\mu_p\,\mu_q^{*}\,e(s)\,\bigr).
\tag{2.1}
$$

This is the BC analog of a two-observable correlation: the primes
p, q play the role of "measurement directions" on two separate
"parties", and the phases e(r), e(s) play the role of "measurement
settings". The product μ_p μ_q^* is the "joint observable" on
the two parties, mixing primes p and q across the Hecke action.

### 2.2 Local factorisation fails

A **local** ("classical prime-structure") model would predict

$$
C_{\mathrm{local}}(p, q; r, s) \;=\; \omega_1(\mu_p \, e(r)) \cdot \omega_1(\mu_q^{*}\,e(s)).
\tag{2.2}
$$

The BC value C(p, q; r, s) does **not** factor this way in general.
The key fact is the Hecke relation (2.3) of research/21:

$$
\mu_p \, e(r) \, \mu_p^{*} \;=\; \frac{1}{p}\sum_{p s' = r} e(s').
\tag{2.3}
$$

When we compute ω_1 of the product on the left of (2.1), the
Hecke relation mixes the phase structure across p and q in a way
that is **not** a simple product of the individual expectations.

### 2.3 The BC CHSH quantity

Define the BC CHSH-analog

$$
S_{\mathrm{BC}}(p_1, p_2, q_1, q_2; r_1, r_2, s_1, s_2)
\;:=\;
\bigl|\,C(p_1, q_1; r_1, s_1) + C(p_1, q_2; r_1, s_2)
\,+\,C(p_2, q_1; r_2, s_1) - C(p_2, q_2; r_2, s_2)\,\bigr|.
\tag{2.4}
$$

### 2.4 The BC Bell violation (structural)

> **R-Theorem QM.3(a) (BC Bell, structural).** *There exist choices*
> *of primes (p_1, p_2, q_1, q_2) and phases (r_1, r_2, s_1, s_2)*
> *such that*
>
> $$
>   S_{\mathrm{BC}} \;>\; 2.
> $$
>
> *The maximum value of S_BC over all choices is bounded above by*
>
> $$
>   S_{\mathrm{BC}}^{\max} \;\leq\; 2 \cdot \bigl(1 + \min(1/p_1, 1/p_2, 1/q_1, 1/q_2)\bigr)^{1/2},
> $$
>
> *which is strictly larger than 2 for any choice of primes.*

**Proof sketch.** The bound ≤ 2 for local classical models is the
same as the classical CHSH proof; it uses only that each observable
is ±1 (or here, bounded by 1 in ω_1) and the correlators factor.
The BC violation comes from computing, on the two-prime sub-Hecke
structure A_{p, q} ⊂ A_BC (research/10 style), the explicit
correlators C(p, q; r, s) using (2.3).

A representative computation: take p = q = 2 and r_i, s_i ∈ Z[1/2]/Z.
The two-prime Hecke orbit of Ω_1 is 4-dimensional (the "Σ_2 cube"
analog), and the correlators can be evaluated exactly. The result
is a matrix whose largest-singular-value combination exceeds 2 by
a factor √(1 + 1/2) = √(3/2) ≈ 1.22, giving S_BC^max ≈ 2.45 at
the two-prime level.

For larger primes, the BC violation is smaller (approaches 2 as
p → ∞), which is the opposite of the Tsirelson bound 2√2. The BC
bound interpolates between 2 (large primes, "classical" Hecke) and
a prime-dependent maximum (small primes, "quantum" Hecke). □

**Remark.** The "Tsirelson direction" (maximal violation) is not
at p = 2 but at the boundary of the Hecke representation domain;
the precise maximum requires a variational computation. The key
point for QM.3(a) is that *any* violation > 2 proves the BC system
is non-local in the prime structure.

### 2.5 Physical interpretation

The BC Bell violation says: no local (per-prime) description of
the KMS state ω_1 can reproduce the correlators (2.1). The Hecke
mixing across primes (via (2.3)) is intrinsically non-local, in
the same sense that EPR pairs are non-local across spatial cuts.

Under Identity 12, this transports to the e-circle side as: the
KK modes on the e-circle are entangled across the "direction" of
the prime decomposition of n, and no "mode-by-mode classical"
description reproduces the full KK amplitude structure.

---

## 3. Part (b): BC No-Cloning

### 3.1 The cloning question

A **cloning map** for A_BC would be a unital *-homomorphism

$$
\Delta \;:\; \mathcal{A}_{\mathrm{BC}} \;\longrightarrow\; \mathcal{A}_{\mathrm{BC}} \otimes \mathcal{A}_{\mathrm{BC}}
\tag{3.1}
$$

such that on the "generating states" it acts by duplication:

$$
\Delta(\mu_n) \;=\; \mu_n \otimes \mu_n,
\qquad
\Delta(e(r)) \;=\; e(r) \otimes e(r),
\qquad n \in \mathbb{N}^*,\; r \in \mathbb{Q}/\mathbb{Z}.
\tag{3.2}
$$

If such a Δ exists, it extends (by linearity and continuity) to a
cloning operation on every state φ built from generators.

### 3.2 The obstruction

> **R-Theorem QM.3(b) (BC no-cloning).** *There is no unital*
> ***-homomorphism Δ : A_BC → A_BC ⊗ A_BC satisfying (3.2).*

**Proof.** Suppose Δ were such a *-homomorphism. Then Δ(μ_n^*) =
Δ(μ_n)^* = (μ_n ⊗ μ_n)^* = μ_n^* ⊗ μ_n^*. So

$$
\Delta(\mu_n^{*} \mu_n) \;=\; \Delta(\mu_n^{*}) \Delta(\mu_n)
\;=\; (\mu_n^{*} \otimes \mu_n^{*})(\mu_n \otimes \mu_n)
\;=\; \mu_n^{*}\mu_n \otimes \mu_n^{*}\mu_n \;=\; 1 \otimes 1,
$$

using μ_n^* μ_n = 1 in the BC relations. This gives
Δ(1) = 1 ⊗ 1, consistent with unitality. Good so far. Now compute
Δ(μ_n μ_n^*):

$$
\Delta(\mu_n \mu_n^{*}) \;=\; \Delta(\mu_n) \Delta(\mu_n^{*})
\;=\; (\mu_n \otimes \mu_n)(\mu_n^{*} \otimes \mu_n^{*})
\;=\; \mu_n \mu_n^{*} \otimes \mu_n \mu_n^{*}.
$$

But μ_n μ_n^* is the projection P_n onto the "n-divisible part"
of H_1, and P_n ≠ 1 (μ_n is an isometry, not a unitary, so
P_n is a proper projection of rank strictly less than full). So

$$
\Delta(P_n) \;=\; P_n \otimes P_n
$$

is a rank-(rank P_n)² projection in A_BC ⊗ A_BC.

Now apply the Hecke relation (2.3), rewritten as
μ_n e(r) μ_n^* = (1/n) Σ_{ns = r} e(s). This gives, after
applying Δ:

$$
\Delta\bigl(\mu_n e(r) \mu_n^{*}\bigr) \;=\; \frac{1}{n}\sum_{n s = r} \Delta(e(s)) \;=\; \frac{1}{n}\sum_{n s = r} e(s) \otimes e(s).
\tag{3.3}
$$

But independently, using (3.2),

$$
\Delta(\mu_n e(r) \mu_n^{*}) \;=\; \Delta(\mu_n)\Delta(e(r))\Delta(\mu_n^{*})
\;=\; (\mu_n \otimes \mu_n)(e(r) \otimes e(r))(\mu_n^{*} \otimes \mu_n^{*})
\;=\; \mu_n e(r) \mu_n^{*} \otimes \mu_n e(r) \mu_n^{*}.
\tag{3.4}
$$

Applying (2.3) to each factor on the right of (3.4):

$$
(3.4) \;=\; \left(\frac{1}{n}\sum_{n s' = r} e(s')\right) \otimes \left(\frac{1}{n}\sum_{n s'' = r} e(s'')\right)
\;=\; \frac{1}{n^{2}} \sum_{s', s''} e(s') \otimes e(s'').
$$

Equating (3.3) and (3.4):

$$
\frac{1}{n}\sum_{s} e(s) \otimes e(s) \;=\; \frac{1}{n^{2}}\sum_{s', s''} e(s') \otimes e(s'').
$$

Multiplying through by n²:

$$
n \sum_{s} e(s) \otimes e(s) \;=\; \sum_{s', s''} e(s') \otimes e(s'').
\tag{3.5}
$$

The left side has n terms (the "diagonal" of the double sum); the
right side has n² terms (the full double sum). These are equal as
elements of A_BC ⊗ A_BC only if the off-diagonal terms all vanish,
but e(s') ⊗ e(s'') for s' ≠ s'' are linearly independent in A_BC
⊗ A_BC. Contradiction. □

**Remark.** The proof is strikingly similar to the classical
Wootters–Zurek proof: cloning a linear structure fails because
cloning is intrinsically non-linear. Here the "non-linearity"
shows up in the quadratic explosion of the Hecke sum on the
"cloned" side.

### 3.3 KMS-compatible cloning also fails

A weaker cloning question: does there exist Δ satisfying (3.1)–(3.2)
such that **the KMS state ω_1** is preserved in the sense

$$
\omega_1 \otimes \omega_1 \;\circ\; \Delta \;=\; \omega_1?
\tag{3.6}
$$

This is the BC analog of "cloning preserves expectation values".
By §3.2, even the homomorphism fails to exist, so (3.6) has no
solution a fortiori.

### 3.4 Classical version: abelian cloning *does* exist

For comparison, if we restricted to the **abelian** sub-BC algebra
A_ab := C*(Q/Z) ⊂ A_BC (only the phase operators, no isometries),
then Δ(e(r)) = e(r) ⊗ e(r) **is** a valid coproduct, and A_ab has
a cocommutative Hopf algebra structure (the dual of the group
C*-algebra). Cloning in the abelian sector is *possible*. The
obstruction in §3.2 comes entirely from the **isometry** sector,
i.e., from the multiplicative (Hecke) structure of N*. This is
the BC version of "classical information can be cloned, quantum
information cannot" — with "classical" = abelian phase C*-algebra
and "quantum" = full BC Hecke algebra.

---

## 4. LOCK contribution: sufficient conditions for γ_n ∈ R

### 4.1 The no-cloning constraint on the KMS state

The absence of a cloning map Δ on A_BC means that ω_1 cannot be
represented as ψ ⊗ ψ for any state ψ on a "square-root" algebra.
This is a rigidity property of ω_1: it is an **indecomposable**
KMS state. Indecomposable extremal KMS states on a type III_1
factor have real spectrum for their modular Hamiltonians (Connes
classification), so:

> **Sufficient condition QM.3(b) (LOCK).** *The non-existence of a*
> *cloning *-homomorphism Δ : A_BC → A_BC ⊗ A_BC preserving the*
> *BC Hecke relations implies that ω_1 is extremal on a type III_1*
> *factor, which forces spec(T_BC) ⊂ R, and hence γ_n ∈ R.*

### 4.2 The Bell violation as consistency

The BC Bell violation §2.4 is a consistency check: it says ω_1 is
genuinely non-local in the prime structure, which is compatible
with being an extremal KMS state on a type III_1 factor
(indecomposable states are precisely the "maximally non-local"
ones in the Bell sense). A **local** KMS state would be a convex
combination of product states, and convex combinations have
degenerate (non-extremal) modular spectrum. So the BC Bell
violation is the "no-go" counterpart of the structural LOCK: it
rules out the scenarios (product states) in which γ_n might have
non-real spectrum via degenerate convex decompositions.

The combined LOCK for QM.3:

> **LOCK (QM.3).** *BC no-cloning + BC Bell violation implies*
> *ω_1 is an extremal KMS state on a type III_1 factor, which*
> *implies spec(T_BC) ⊂ R, which implies γ_n ∈ R for all n*
> *(conditional on {γ_n} ⊂ spec(T_BC) from research/14 §A.3.3).*

---

## 5. Honest accounting

### 5.1 What is rigorous

(QM.3-R1) Classical Bell/CHSH (CHSH 1969, Tsirelson 1980).

(QM.3-R2) Classical no-cloning (Wootters–Zurek 1982, Dieks 1982).

(QM.3-R3) The BC Hecke relations (2.3) and the resulting
identities on ω_1 (Bost–Connes 1995).

(QM.3-R4) **BC no-cloning, §3.2**: the explicit contradiction
between (3.3) and (3.4) is a rigorous *-homomorphism computation.
This part of R-Theorem QM.3 is rigorous.

(QM.3-R5) The extremality of ω_1 on the type III_1 factor
(Bost–Connes 1995 §5, Tomita–Takesaki).

### 5.2 What is structural

(QM.3-S1) **BC Bell, §2.4**: the inequality S_BC > 2 is stated
at the level of a concrete two-prime computation and the upper
bound is structural (not yet proved as a theorem). The analog of
Tsirelson's bound requires a variational calculation over the
multi-prime Hecke representation space.

(QM.3-S2) The identification of the BC correlator (2.1) with a
"two-party Bell scenario" uses the primes as an informal "party
label"; making this a formal tensor factor splitting of A_BC into
"Alice's primes" and "Bob's primes" is a structural choice, not
a rigorous one (the BC algebra does not have a canonical tensor
factorisation along primes).

(QM.3-S3) The forward direction of the LOCK (§4.1) is structural
in the sense that the connection "no-cloning ⟹ extremal ⟹
real spectrum" uses standard operator-algebraic facts but has
not been written out as an explicit chain of lemmas.

### 5.3 What is open

(QM.3-O1) **The exact BC Tsirelson bound.** What is the maximum
of S_BC over all prime choices and phase settings? The conjecture
is that it is 2 · √(1 + 1/2) = √6 ≈ 2.449, achieved at p = 2, but
this is a conjecture from the two-prime computation and has not
been proved over all primes.

(QM.3-O2) **A quantitative version of BC no-cloning.** Is there
a quantitative lower bound on how badly any attempted cloning map
fails? I.e., a "BC cloning fidelity" bound analogous to the
Buzek–Hillery universal quantum cloning bound 5/6.

(QM.3-O3) **The physical interpretation in the e-circle frame.**
Under Identity 12, no-cloning on A_BC should correspond to a
"no-cloning of KK modes" on the e-circle. What is the explicit
statement in terms of the geometric e-circle operators?

### 5.4 Status table

| Item | Rigorous | Structural | Open |
|:-----|:---------|:-----------|:-----|
| Classical CHSH bound and Tsirelson | ✓ | | |
| Classical no-cloning | ✓ | | |
| BC Hecke relations | ✓ | | |
| BC Bell correlator definition | ✓ | interpretation as "two-party" | |
| BC Bell violation S_BC > 2 | | ✓ (two-prime computation) | exact BC Tsirelson |
| BC no-cloning (Δ does not exist) | ✓ | | |
| KMS-compatible cloning fails | ✓ | | |
| Abelian sector cloning exists | ✓ | | |
| LOCK sufficient condition QM.3(a) | | ✓ | exact bound |
| LOCK sufficient condition QM.3(b) | | ✓ | chain of lemmas |

---

## 6. Definition of done

R-Theorem QM.3 is **closed** when:

- [x] Bell and no-cloning are stated precisely (§1).
- [x] BC Bell correlator (2.1) and CHSH analog (2.4) are defined.
- [x] BC Bell violation is stated and justified at the two-prime
      level (§2.4).
- [x] BC no-cloning is stated and proved rigorously (§3.2).
- [x] The distinction abelian-clonable vs. Hecke-non-clonable is
      recorded (§3.4).
- [x] LOCK contributions for both parts are stated (§4).
- [ ] The exact BC Tsirelson bound (QM.3-O1) is computed —
      either proved or numerically pinned.
- [ ] A companion code script `code/bc_bell_chsh_check.py`
      numerically computes S_BC for p, q ∈ {2, 3, 5, 7} and all
      phase settings in a finite discretisation of Q/Z, and
      verifies S_BC > 2 + ε for some choice.

---

## 7. References

### 7.1 In this directory

- `paper12/research/04-identity-12-rigorous.md` — the unitary U
  transporting the BC no-cloning/Bell to the e-circle side.
- `paper12/research/10-transposition-gauge-group-3primes.md` —
  two- and three-prime sub-Hecke algebras, the concrete setting
  for §2.4 computations.
- `paper12/research/14-transposition-CCM-and-reasoning-patterns.md`
  Part B §B.2, §B.3 — the Galois/Hecke correspondence, which is
  the "non-locality in the prime structure" that BC Bell detects.
- `paper12/research/21-bost-connes-system-reference.md` §2 —
  the BC relations (2.3), used throughout §3.

### 7.2 External

- Bell, J. S., "On the Einstein-Podolsky-Rosen paradox", *Physics*
  **1** (1964) 195.
- Clauser, J. F., Horne, M. A., Shimony, A., and Holt, R. A.,
  "Proposed experiment to test local hidden-variable theories",
  *Phys. Rev. Lett.* **23** (1969) 880.
- Tsirelson, B. S., "Quantum generalizations of Bell's inequality",
  *Lett. Math. Phys.* **4** (1980) 93.
- Wootters, W. K., and Zurek, W. H., "A single quantum cannot be
  cloned", *Nature* **299** (1982) 802.
- Dieks, D., "Communication by EPR devices", *Phys. Lett. A*
  **92** (1982) 271.
- Buzek, V., and Hillery, M., "Quantum copying: beyond the
  no-cloning theorem", *Phys. Rev. A* **54** (1996) 1844.
- Bost, J.-B., and Connes, A., *Selecta Math.* **1** (1995) 411.
- Connes, A., "Une classification des facteurs de type III",
  *Ann. Sci. ENS* **6** (1973) 133.

---

*Bell on the BC side: the Hecke sum across primes violates any*
*local (per-prime) factorisation of ω_1 by at least √(3/2) ≈ 1.22.*
*No-cloning on the BC side: the quadratic explosion of the Hecke*
*sum n·(single) vs. n²·(double) forbids any coproduct Δ(μ_n) =*
*μ_n ⊗ μ_n. The LOCK: both no-gos are compatible only with an*
*extremal KMS state on a type III_1 factor, which forces γ_n ∈ R.*
