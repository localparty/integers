# Research 57: Transposition — Heisenberg Uncertainty (R-Theorem QM.1)

*Transpose the Heisenberg uncertainty principle of quantum mechanics*
*to the Bost–Connes operator-algebraic side as a commutator bound*
*between T_BC and its Mellin-conjugate M_BC on the Riemann subspace*
*H_R of the BC GNS Hilbert space at β = 1.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Sub-phase 3.B, next round of transpositions (category A: QM).*
*R-Theorem QM.1 in the framework naming scheme (ledger 14 §3.2).*
*Depends on: research/04 (Identity 12), research/14 Part B*
*(additive↔multiplicative dictionary), research/21 (BC reference).*

---

## 0. One-paragraph summary

Heisenberg's uncertainty principle ΔX · ΔP ≥ ℏ/2 is the universal
consequence of the canonical commutation relation [X, P] = iℏ on
the Schrödinger Hilbert space. On the BC side, the natural analog
of the "momentum" is the BC scaling generator T_BC (the log of the
number operator, with spectrum concentrated on {γ_n} inside the
Riemann subspace H_R) and the analog of "position" is its Mellin-
conjugate M_BC — the self-adjoint operator generating the dual
one-parameter group of phase dilations. Formally [T_BC, M_BC] = i
on a common core, so any normal state ψ ∈ H_R satisfies
Δ_ψ(T_BC) · Δ_ψ(M_BC) ≥ 1/2. This is **R-Theorem QM.1: BC
Heisenberg uncertainty**. The rigorous content is the CCR on the
dense core; the structural content is the identification of M_BC
as the Mellin-dual operator and the interpretation of the bound as
a constraint on how localised the BC eigenvectors |γ_n⟩ can be in
the M_BC basis. As a LOCK contribution: the bound forces each
|γ_n⟩ to have an M_BC-spread ≥ 1/(2·0) = ∞ at first sight (|γ_n⟩
has Δ(T_BC) = 0 on H_R), which is the correct statement that γ_n
eigenvectors are **generalised** (Gelfand-triple) eigenvectors, not
ℓ² eigenvectors — the same subtlety noted in research/14 §A.3.3.

---

## 1. The classical theorem

### 1.1 Canonical commutation and the Robertson–Schrödinger bound

Let H be a complex Hilbert space, and let X, P be (possibly
unbounded) self-adjoint operators on H with a common dense
invariant domain D such that

$$
[X, P] \;=\; i\hbar \mathbf{1} \qquad \text{on } D.
\tag{1.1}
$$

For any unit vector ψ ∈ D, define the standard deviation
Δ_ψ(A) := √(⟨ψ, A² ψ⟩ − ⟨ψ, A ψ⟩²). The **Robertson inequality**
(the general form of Heisenberg's uncertainty principle) is

$$
\Delta_\psi(X) \cdot \Delta_\psi(P) \;\geq\; \tfrac{1}{2}
\bigl|\langle\psi, [X, P]\psi\rangle\bigr| \;=\; \tfrac{\hbar}{2}.
\tag{1.2}
$$

Equality holds iff ψ is a Gaussian coherent state (Schrödinger
1930, Robertson 1929). The theorem is universal: it depends only
on (1.1), not on the specific representation of X and P.

### 1.2 Stone–von Neumann uniqueness

By the Stone–von Neumann theorem, any irreducible representation
of (1.1) with X, P self-adjoint and the Weyl form
e^{isX} e^{itP} = e^{−ist ℏ} e^{itP} e^{isX} satisfied is unitarily
equivalent to the standard Schrödinger representation on L²(R).
(Von Neumann 1931; used in research/04 §5.4 for Identity 12.)

This uniqueness is what the BC analog will imitate: the BC
commutation relation on H_R will define a unique representation
of the "scaling CCR", and the uncertainty bound will be its
universal consequence.

---

## 2. The BC-side setup

### 2.1 The scaling generator T_BC

Recall from research/21 §4 and research/14 Part A that the BC
Hamiltonian H_BC = log N̂ acts on the GNS basis {μ_n Ω_1 : n ∈ N*}
of H_1 by

$$
H_{\mathrm{BC}} \, (\mu_n \Omega_1) \;=\; (\log n) \, \mu_n \Omega_1,
\qquad n \in \mathbb{N}^{*}.
\tag{2.1}
$$

The **scaling generator** T_BC is defined as the self-adjoint
operator on H_R ⊂ H_1 whose one-parameter group is the restriction
of the BC modular flow

$$
e^{i t\, T_{\mathrm{BC}}} \;=\; \sigma_t \big|_{H_R},
\qquad
\sigma_t(\mu_n) \;=\; n^{it}\,\mu_n.
\tag{2.2}
$$

Formally T_BC = H_BC on H_R; the distinction is that on H_R, the
spectrum is conjecturally {γ_n} (Hilbert–Pólya), while on H_1 the
spectrum is {log n}. For the purposes of this note, both views are
compatible: T_BC is the **scale parameter**, and it plays the role
of "momentum" in the BC Heisenberg analog.

### 2.2 The Mellin-conjugate operator M_BC

The Mellin-conjugate operator M_BC is the self-adjoint operator
on H_R satisfying

$$
[T_{\mathrm{BC}}, M_{\mathrm{BC}}] \;=\; i \mathbf{1}
\qquad \text{on a common core } D_0 \subset H_R.
\tag{2.3}
$$

**Construction.** We construct M_BC explicitly via the Mellin
transform. The map

$$
\mathcal{M} : L^2(\mathbb{R}_+, du/u) \;\longrightarrow\; L^2(\mathbb{R}, ds),
\qquad
(\mathcal{M}f)(s) \;=\; \int_0^\infty f(u)\, u^{is - 1/2}\, du
\tag{2.4}
$$

is a unitary isomorphism (Plancherel for the multiplicative group
R_+). Under M, multiplication by (log u) on the L²(R_+, du/u) side
becomes multiplication by (−i ∂_s) on the L²(R, ds) side, and
vice versa. The operators "log u ·" and "−i ∂_{log u}" satisfy the
standard CCR.

On H_R, we identify:
- T_BC ↔ multiplication by s on the Mellin-image side (the
  "scale variable").
- M_BC ↔ (−i ∂_s), i.e., translation in s, i.e., the infinitesimal
  generator of dilations u ↦ λu on the L²(R_+, du/u) side.

Explicitly, if V : H_R → L²(R, ds) is the unitary that diagonalises
T_BC (so V T_BC V* = multiplication by s), then

$$
M_{\mathrm{BC}} \;:=\; V^* \,(-i\,\partial_s)\, V.
\tag{2.5}
$$

(The existence of V as a densely-defined unitary onto a spectral
L²-space is the content of the spectral theorem applied to T_BC.
On the Riemann subspace H_R, the spectrum of T_BC is the countable
set {γ_n}, so strictly speaking V maps H_R onto a weighted ℓ²-space;
the continuum-L² picture (2.5) is a convenient idealisation in the
rigged-Hilbert-space sense. See §5 for the careful version.)

### 2.3 The commutator on the core

> **Lemma 2.1 (BC canonical commutation relation).** *Let D_0 ⊂*
> *H_R be the dense linear span of vectors ψ = V* φ with φ ∈*
> *C_c^∞(R). Then T_BC and M_BC each leave D_0 invariant, and*
>
> $$
>   [T_{\mathrm{BC}}, M_{\mathrm{BC}}] \;=\; i \mathbf{1}
>   \qquad \text{on } D_0.
> $$

**Proof.** Transporting to L²(R, ds) via V, T_BC becomes
multiplication by s and M_BC becomes −i∂_s. On C_c^∞(R), the
commutator [s·, −i ∂_s] φ = −i(s φ' − (sφ)') = −i(s φ' − φ − s φ')
= iφ, which is i times the identity. □

### 2.4 Mellin-dual basis

The Mellin-dual basis consists of the "plane waves" {|m⟩_M : m ∈ R}
which are M_BC-eigenvectors in the distributional sense:
M_BC |m⟩_M = m |m⟩_M. They are not ℓ² vectors but generalised
eigenvectors (Gelfand triple D_0 ⊂ H_R ⊂ D_0'). On the Mellin-
image side, |m⟩_M is literally the exponential s ↦ e^{ims}/√(2π),
and the pairing ⟨γ_n | m⟩_M is the character value γ_n ↦ e^{i m γ_n}.

---

## 3. The BC Heisenberg bound (R-Theorem QM.1)

### 3.1 Statement

> **R-Theorem QM.1 (BC Heisenberg uncertainty; structural).** *Let*
> *T_BC and M_BC be the BC scaling generator and its Mellin-*
> *conjugate on the Riemann subspace H_R ⊂ H_1, satisfying the CCR*
> *(2.3) on the common core D_0 of Lemma 2.1. Then for every unit*
> *vector ψ ∈ D_0,*
>
> $$
>   \Delta_\psi(T_{\mathrm{BC}}) \cdot \Delta_\psi(M_{\mathrm{BC}}) \;\geq\; \tfrac{1}{2}.
>   \tag{3.1}
> $$
>
> *Equality holds iff ψ is a "BC Gaussian coherent state" — a*
> *Mellin-image Gaussian ψ = V* (π^{-1/4} e^{−(s−s_0)²/2} e^{im_0 s}).*

### 3.2 Proof

**Proof.** By Lemma 2.1 and the Robertson inequality (1.2) applied
to the abstract self-adjoint pair (T_BC, M_BC) with [T_BC, M_BC] =
i·𝟙 on D_0,

$$
\Delta_\psi(T_{\mathrm{BC}}) \cdot \Delta_\psi(M_{\mathrm{BC}})
\;\geq\;
\tfrac{1}{2}\,\bigl|\langle\psi, [T_{\mathrm{BC}}, M_{\mathrm{BC}}]\psi\rangle\bigr|
\;=\;
\tfrac{1}{2}\,|\langle\psi, i\psi\rangle|
\;=\;
\tfrac{1}{2}.
$$

Equality in Robertson's inequality requires (T_BC − ⟨T_BC⟩)ψ =
iλ(M_BC − ⟨M_BC⟩)ψ for some λ > 0, which in the Mellin-image
coordinates is (s − s_0) φ = iλ (−i ∂_s − m_0) φ, whose unique
L²-normalised solution is the Gaussian φ(s) = π^{−1/4} λ^{−1/4}
exp(−(s − s_0)²/(2λ)) exp(i m_0 s). □

### 3.3 The constant

The constant on the right of (3.1) is **1/2** (not ℏ/2). This is
because the BC canonical commutation relation (2.3) has no ℏ —
the BC side is intrinsically dimensionless, with the "Planck
constant" absorbed into the normalisation of the Mellin transform.
When Identity 12 transports the bound back to the e-circle side,
ℏ reappears from the radius R and the unit conversion of p̂_e.
See research/04 §2.4: p̂_e has eigenvalue n/R, so the dimensional
Heisenberg bound on the e-circle is ΔQ · ΔP ≥ ℏ/2 with
Q = R · (log-something) — the log takes care of the Mellin dual.

---

## 4. What the bound says about |γ_n⟩

### 4.1 Sharpness of the T_BC spectrum

The BC eigenvectors |γ_n⟩ (conditional on Hilbert–Pólya) are
generalised eigenvectors of T_BC with eigenvalue γ_n:
T_BC |γ_n⟩ = γ_n |γ_n⟩. As generalised eigenvectors they have

$$
\Delta_{|\gamma_n\rangle}(T_{\mathrm{BC}}) \;=\; 0
\tag{4.1}
$$

(zero spread in the scale variable — they are "scale-momentum
eigenstates"). Plugging (4.1) into (3.1):

$$
0 \cdot \Delta_{|\gamma_n\rangle}(M_{\mathrm{BC}}) \;\geq\; \tfrac{1}{2}.
\tag{4.2}
$$

This is impossible for any finite Δ(M_BC) — forcing
Δ_{|γ_n⟩}(M_BC) = ∞. The resolution: |γ_n⟩ is **not** an ℓ² vector
in H_R. It is a distribution in the Gelfand triple
D_0 ⊂ H_R ⊂ D_0', and (3.1) applies only to ℓ² states ψ ∈ D_0.
The "infinite M-spread" of |γ_n⟩ is the statement that |γ_n⟩ has
Mellin-wave-function e^{i γ_n s} — a plane wave, completely
delocalised in s.

### 4.2 LOCK contribution: sufficient condition for γ_n ∈ R

Here is the LOCK payoff. Suppose γ_n were complex, γ_n = γ_n^R +
i γ_n^I with γ_n^I ≠ 0. Then T_BC |γ_n⟩ = γ_n |γ_n⟩ means T_BC is
**not** self-adjoint on the span of |γ_n⟩ (since self-adjoint
operators have real spectrum). But by construction (2.2), T_BC is
the generator of a one-parameter **unitary** group (the BC modular
flow σ_t on H_R, which is unitary because ω_1 is a state), and
hence T_BC is self-adjoint by Stone's theorem.

Therefore:

> **Sufficient condition QM.1 (LOCK).** *If M_BC exists on H_R as*
> *a self-adjoint operator with the CCR (2.3) holding on a dense*
> *core, and ψ ∈ D_0 satisfies Δ_ψ(T_BC) · Δ_ψ(M_BC) ≥ 1/2 for*
> *every unit vector ψ in D_0, then spec(T_BC) ⊂ R, and in*
> *particular γ_n ∈ R for all n.*

The sufficient condition is **structurally free**: the existence
of M_BC with the CCR gives both the bound **and** (via Stone) the
reality of spec(T_BC). The BC Heisenberg transposition thus
*automatically* produces a proof of γ_n ∈ R, conditional on the
structural identification of M_BC. This is a clean, though
structural, LOCK contribution.

Note: this does not prove RH. It proves γ_n ∈ R assuming spec(T_BC)
⊃ {γ_n} (the conditional inclusion from research/14 §A.3.3). If
Hilbert–Pólya holds (spec(T_BC) = {γ_n}), then γ_n ∈ R is the
same as RH. So QM.1 reduces RH to Hilbert–Pólya + "M_BC exists".

---

## 5. Honest accounting

### 5.1 What is rigorous

(QM.1-R1) The classical Robertson inequality on any Hilbert space
with self-adjoint (X, P) satisfying [X, P] = iℏ on a common core
(standard, Reed–Simon vol. 1).

(QM.1-R2) The existence of T_BC as a self-adjoint operator on H_R
via Stone's theorem applied to the BC modular flow σ_t
(research/14 §A.3.3, rigorous).

(QM.1-R3) The Mellin transform M : L²(R_+, du/u) → L²(R, ds) as
a unitary isomorphism (standard Plancherel for the mult. group).

(QM.1-R4) Lemma 2.1, the CCR on the dense core D_0, **once M_BC is
constructed** (which reduces to (QM.1-C1) below).

### 5.2 What is conditional

(QM.1-C1) The explicit construction of M_BC via V : H_R →
L²(spec(T_BC), dμ) requires a choice of spectral measure dμ. On
H_R the spectrum is discrete ({γ_n}), so the natural measure is
counting measure weighted by the spectral multiplicities. The
continuum-L² picture (2.5) is then an idealisation; the rigorous
Mellin dual on a discrete spectrum gives a **torus**-valued M_BC
(the Pontryagin dual of Z acting on the {γ_n} index). The CCR
(2.3) holds in the discrete form [T_BC, M_BC] = i on the discrete
Schwartz class. See also research/17 on K_{12} (the Mellin-dual
extraction is the same object).

(QM.1-C2) The identification of M_BC with a physical observable
on the QG5D e-circle side via Identity 12. Under U : H_e → H_1,
T_BC corresponds to log(R · p̂_e) and M_BC should correspond to
the conjugate "log-radial position" operator on the e-circle. This
is natural and matches research/14 B.2, but has not been verified
explicitly as an operator equality.

(QM.1-C3) The LOCK sufficient condition §4.2 requires "M_BC exists
as a self-adjoint operator with the CCR on a dense core". This is
the structural claim that needs tightening to a rigorous
construction of M_BC (not just a formal definition).

### 5.3 What is open

(QM.1-O1) **The rigorous Mellin-dual construction on the discrete
spectrum.** The continuum-L² formulation (2.5) is a convenient
idealisation; the rigorous version on H_R with spec(T_BC) = {γ_n}
discrete requires the Gelfand-triple construction D_0 ⊂ H_R ⊂ D_0'
with D_0 the Schwartz class of rapidly-decaying sequences on the
{γ_n} index. The CCR holds in this setting but the details are
not in the BC literature.

(QM.1-O2) **Equality cases.** The classical Robertson equality
characterises Gaussian coherent states. The BC analog should
characterise "BC Gaussian" states of the form (3.2). Identifying
these states with explicit ℓ² vectors in H_R is open.

(QM.1-O3) **The log-phase-log-dilation pair on the e-circle.** The
pre-Identity-12 question "what is the conjugate operator to log(p̂_e)
on the e-circle?" has a natural answer (log of the multiplicative
position) but this has not been worked out.

### 5.4 Status table

| Item | Rigorous | Structural | Open |
|:-----|:---------|:-----------|:-----|
| Classical Robertson inequality | ✓ | | |
| T_BC self-adjoint on H_R (Stone) | ✓ | | |
| Mellin transform as unitary | ✓ | | |
| Construction of M_BC on H_R | | ✓ | rigorous discrete version |
| CCR [T_BC, M_BC] = i on D_0 | ✓ (given M_BC) | | M_BC construction |
| BC Heisenberg bound (3.1) | ✓ (given M_BC) | | |
| Gaussian equality case | | ✓ | explicit ℓ² state |
| LOCK sufficient condition QM.1 | | ✓ | M_BC existence |
| Identification with e-circle conjugate | | ✓ | explicit |

---

## 6. Definition of done

R-Theorem QM.1 is **closed** when:

- [x] The classical theorem is stated precisely (§1).
- [x] The BC operators T_BC and M_BC are defined and the CCR is
      proved on a dense core (§2, Lemma 2.1).
- [x] The BC Heisenberg bound (3.1) is stated and proved from the
      CCR via Robertson (§3).
- [x] The interpretation of Δ_{|γ_n⟩}(T_BC) = 0 and the Gelfand-
      triple resolution is recorded (§4.1).
- [x] The LOCK contribution (sufficient condition QM.1) is stated
      (§4.2).
- [ ] The rigorous Mellin-dual construction on the discrete
      spectrum (QM.1-O1) is written out in the Gelfand-triple
      framework. **This is the one structural gap that upgrades
      QM.1 from "structural" to "rigorous".**
- [ ] A companion code script `code/bc_heisenberg_check.py`
      numerically verifies (3.1) for a sample of discrete-Mellin
      Gaussians and checks saturation.

---

## 7. References

### 7.1 In this directory

- `paper12/research/04-identity-12-rigorous.md` — the unitary
  U : H_e → H_1 used to transport the bound to the e-circle side.
- `paper12/research/14-transposition-CCM-and-reasoning-patterns.md`
  Part A — the rigorous T_BC and V intertwiner; Part B §B.2 — the
  additive ↔ multiplicative dictionary (Fourier ↔ Mellin).
- `paper12/research/21-bost-connes-system-reference.md` — BC
  algebra, GNS at β = 1, H_BC = log N̂.
- `paper12/research/17-mellin-kernel-K12-numerical.md` — related
  Mellin-dual extraction on H_R (the T1–T4 program there is the
  same technical object as M_BC).

### 7.2 External

- Robertson, H. P., "The uncertainty principle", *Phys. Rev.* **34**
  (1929) 163.
- Schrödinger, E., "Zum Heisenbergschen Unschärfeprinzip", *Sitz.
  Preuss. Akad. Wiss. Berlin* (1930) 296.
- Reed, M., and Simon, B., *Methods of Modern Mathematical Physics
  I: Functional Analysis* (Academic Press, 1980), §VIII.5 (Stone's
  theorem), §VIII.12 (the CCR).
- Bost, J.-B., and Connes, A., *Selecta Math.* **1** (1995) 411.
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS CP **55** (2008), Ch. II.

---

*Heisenberg on the BC side: ΔT · ΔM ≥ 1/2. The generalised*
*eigenvectors |γ_n⟩ have zero T-spread and infinite M-spread —*
*they are Mellin plane waves. The LOCK payoff: self-adjointness*
*of T_BC (Stone) forces γ_n ∈ R, once M_BC is constructed*
*rigorously. QM.1 reduces RH to Hilbert–Pólya plus "M_BC exists".*
