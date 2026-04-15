# Research 20: Open Thread Map — The Seven Unclosed Threads of Paper 12

*A single map of the seven open threads in the Paper 12 programme.*
*For each thread: precise problem statement, current status, cited*
*results and assumptions, missing ingredient for closure, next*
*concrete step, and dependency pointers. This file is the weekend's*
*operational plan and the source of truth for "what remains".*

*Authors: G Six, with Claude Opus 4.6 (1M ctx)*
*Date opened: 2026-04-09*
*Gap 3 of `integers/paper12-cbb-system/15-audit-and-missing-research-files.md`.*
*Referenced by: every subsequent research note that claims to close*
*one of the seven threads.*

---

## 0. The Seven Threads at a Glance

| # | Thread | Lives in | Status | Difficulty | Blocking? |
|---|--------|----------|--------|------------|-----------|
| T1 | K_{12}(log p) rigorous (Mellin-dual ψ_1, ψ_2) | research/17, research/05 §4.1, research/07 (C1)–(C4) | OPEN (honest negative in truncated model) | H | Quantitative SM ↔ CC match |
| T2 | BC-intrinsic SU(3) derivation | research/10 Thm 10 | STRUCTURAL (transported from Paper 11) | M | Paper 11 as full corollary |
| T3 | OTOC saturation for BC scrambler | research/12 Part A | STRUCTURAL (MSS bound closed; saturation not) | M | None downstream; sharpening |
| T4 | Mellin proportionality Σ(dim R)²/C_2(R)^s ↔ ζ at β=1 | research/13 Part A | STRUCTURAL | M | CP² area law full rigour |
| T5 | Three remaining missing parameters | research/16 §7, 13-current-state §7 | OPEN | M (search) | Scoreboard 34/37 → 37/37 |
| T6 | Explicit cosmic transition amplitudes (Landau–Zener) | research/06 §5, (SR1)–(SR4) | OPEN (level-crossing sketched) | H | First-principles selection rule |
| T7 | Mathematical proof of RH (sub-phase 3.D) | research/08, Paper 13 sequel | DEFERRED | VH | Not Paper 12 |

**Critical observations.**
- T1 is the only thread whose *current best numerical estimate*
  actively contradicts the framework's empirical claim (factor of 10⁴
  gap in |V_{12}|²). Every other open thread is either consistent or
  merely incomplete.
- T2, T3, T4 are *structural*: the shape of the answer is known, the
  rigorous closure is missing.
- T5 is a search problem, not a theoretical problem.
- T6 is the deepest open sub-problem of sub-phase 3.A.
- T7 is out of scope for Paper 12 and routes to Paper 13.

---

## 1. Thread T1 — Rigorous K_{12}(log p)

### 1.1 Precise problem statement

Let U : H_e → H_1 be the Identity 12 unitary (research/04), and let
T_BC be the Connes scaling operator on the Riemann subspace H_R ⊂ H_1
with spec(T_BC) ⊇ {γ_n} (research/02). Let ψ_n(k) := ⟨k|_e · U|γ_n⟩
be the coefficients of the n-th scaling eigenvector in the
natural-number basis of H_e. Define

$$
K_{nm}(u) \;:=\; \sum_{k \geq 1} \overline{\psi_n(k)}\,\psi_m(k)\,e^{iu\log k}.
$$

**Problem.** Compute (or give rigorous bounds on) K_{12}(log p) for
p ∈ {2, 3, 5, 7, 11, ...}, with enough precision to evaluate

$$
|V_{12}|^{2}_{\mathrm{SM}} \;=\; \Bigl|\sum_p \frac{c_p}{\sqrt p}\,
         \bigl[K_{12}(\log p) + K_{21}(\log p)\bigr]\Bigr|^{2}
$$

where c_p ∼ |b_i|/(4π)² · log p/p from the one-loop SM running
(research/07), and compare to the empirical |V_{12}|²_emp ≈ 0.2425
extracted from the 5 ppb CC formula (research/05 §4.1).

### 1.2 Current status

- **Honest negative in the truncated Hecke model (research/17):** in
  a Model-B truncation T_N^{(B)} (N ≤ 5000) the numerical kernel gives
  |K_{12}(log 2)| ≈ 0.010, |K_{12}(log 3)| ≈ 0.017. Rescaled,
  |V_{12}|²_SM ∼ 2.4 × 10⁻⁵, a factor of **~10⁴ below** empirical.
- **The truncation does not resolve γ_n.** N ≤ 5000 gives eigenvalues
  ≈ 9.92, 9.72 — far from γ_1 ≈ 14.134, γ_2 ≈ 21.022. The true
  eigenvectors ψ_1, ψ_2 are not approximated by the truncation.
- **Caveat acknowledged in `13-current-state §6`:** the honest band is
  |K_{12}| ∈ [10⁻⁵, 10⁻¹]; the factor-of-2 claim of research/05 §4.1
  is withdrawn; the structural derivation (sign, 1/γ_m, ground-state
  eigenvalue) is unaffected.

### 1.3 Cited results and assumptions

- Identity 12 (research/04 Theorem 4): H_e ≅ H_1 unitarily. Required.
- {γ_n} ⊂ spec(T_BC) (research/02, conditional on Connes–Marcolli
  explicit formula, Gap 1 in research/18 to come). Required.
- Riemann–Weil explicit formula (operator-algebraic form). Gives the
  *distributional* spectral data of T_BC via test functions; does not
  directly produce ψ_n(k).
- SM one-loop coefficients c_p from research/07 (C1)–(C4). Currently
  semi-rigorous; the (C3) sum over KK modes is controlled, (C4) the
  absolute normalisation has an O(1) ambiguity.

### 1.4 Missing ingredient for closure

A **Mellin-dual construction of ψ_n(k) from the Riemann–Weil explicit
formula**, i.e., extracting ψ_1, ψ_2 as distributions (not as vectors
of a matrix truncation) and evaluating the pairing K_{nm}(u) in the
distributional sense.

Formally: the inverse Mellin transform of a suitable spectral
projector onto the γ_n eigenspace of T_BC, integrated against
e^{iu log k}. The right tool is the Connes–Consani–Moscovici
endomotive-trace formula (research/14 Part A), which already gives
T_CCM ↔ T_BC at the level of the trace; we need the *eigenvector*
version.

### 1.5 Next concrete step (T1–T4 program of research/17)

1. **T1.** Write down the explicit spectral projector P_n on H_1
   onto the γ_n eigenspace via the contour integral form of the
   explicit formula (test function h localised at γ_n in the
   Riemann–Weil pairing).
2. **T2.** Compute ⟨k|_e · P_n |k'⟩_e as a distribution on k, k' via
   the Mellin transform of h.
3. **T3.** Extract ψ_n(k) as the "diagonal density" (properly
   regularised) and verify normalisation via the trace.
4. **T4.** Evaluate K_{12}(log p) for p ∈ {2, 3, 5, 7, 11} and report
   with distributional error bars.

**Minimum deliverable:** an upper and lower bound |K_{12}(log p)| ∈
[a, b] that brackets the empirical value, even if not an exact number.

### 1.6 Dependencies

- **Depends on:** Gap 1 (research/18, Connes–Marcolli explicit
  formula) — the proper form of the explicit formula is the tool.
- **Feeds:** the quantitative closure of research/05 §4.1 and
  research/07, hence the entire CC-formula-as-matrix-element claim.
- **Independent of:** T2, T3, T4, T5, T6, T7.

---

## 2. Thread T2 — BC-Intrinsic SU(3)

### 2.1 Precise problem statement

In research/10 Theorem 10, the Standard Model gauge group
G_SM = SU(3) × SU(2) × U(1)/Z_6 is identified as the automorphism
group of the smallest non-trivial sub-Hecke algebra of A_BC generated
by the three primes {2, 3, 5}. The discrete and U(1), SU(2) factors
are derived **intrinsically** from the BC Hecke commutation relations.
The SU(3) factor, however, is **transported** from Paper 11's
three-qubit tangent-space calculation via the unitary U_□ : H_□ ↔
(C²)^⊗3; it is not derived from BC Lie brackets directly.

**Problem.** Give a rigorous, BC-intrinsic derivation of the
continuous SU(3) factor, using the Hecke/μ_p commutation structure
alone, without transporting Paper 11's SLOCC calculation.

### 2.2 Current status

- **Rigorous:** the sub-semigroup generated by {2, 3, 5} in N*, the
  GNS orbit of Ψ_3 := μ_2 μ_3 μ_5 Ω_1, the Z_2 × Z_3 → Z_6 discrete
  structure, and the identification U(1) ↔ center of the μ_p action.
- **Structural:** the A_2 root system emerges from the restricted
  commutation relations μ_p e(r) μ_p^* = (1/p) Σ_{ps=r} e(s) for
  p ∈ {2, 3, 5}, but the step from A_2 to su(3) via Kirillov is not
  yet written out.
- **Transported only:** the continuous SU(3) from Paper 11 along U_□.

### 2.3 Cited results and assumptions

- Paper 11 Theorem 11.5: G_SM from three-qubit entanglement (full
  proof in integers/paper11b-sm-gauge-entanglement/research/07). Assumed.
- Identity 12 rigorous (research/04). Required.
- Kirillov's orbit method on the H_3-orbit at Ψ_3 (proposed route).
  Needs the coadjoint orbit of the Heisenberg group H_3 identified
  with a six-dimensional symplectic leaf carrying an SU(3) stabiliser.

### 2.4 Missing ingredient for closure

A **Kirillov coadjoint-orbit calculation on the H_3-orbit at Ψ_3.**
Specifically: identify the infinitesimal stabiliser Lie algebra of
Ψ_3 under the Lie-algebraic form of μ_p action at the three primes,
show it is isomorphic to su(3), and then exponentiate to the
continuous SU(3) factor. This is not algebraically new (the orbit
method is classical), but the identification of the relevant
infinitesimal generators inside A_BC is the new step.

### 2.5 Next concrete step

1. Write out the infinitesimal generators X_p := d/dt|_0 μ_p^{e^t}
   for p ∈ {2, 3, 5} in the GNS representation on H_1, explicitly
   on the basis {μ_k Ω_1}.
2. Compute [X_p, X_q] for p ≠ q in {2, 3, 5} and verify the A_2
   bracket structure.
3. Identify the Cartan subalgebra (two-dimensional, as expected for
   A_2), the root vectors, and the Killing form.
4. Exponentiate and compare to the transported SU(3) of Paper 11
   along U_□; the two should coincide as Lie groups acting on the
   same tangent space at Ψ_3.

**Minimum deliverable:** the brackets of the three X_p and the
identification with su(3) at the Lie-algebra level; full Lie-group
exponentiation can follow.

### 2.6 Dependencies

- **Depends on:** research/04 (Identity 12), paper11 Theorem 11.5
  (as a consistency check), Gap 2 (research/19, Galois orbit
  decomposition of H_R — the structural foundation for identifying
  the relevant orbit).
- **Feeds:** the rigorous version of research/09 (pattern of zero
  indices {1, 4, 6, 8} via SM gauge group invariants); the "Paper 11
  is a corollary" claim of `11-sub-phase-3b-transposition-closed.md`.
- **Unlocks:** the rigorous Galois-orbit decomposition of H_R
  (research/19 to come), since the Kirillov stabiliser is the
  continuous piece of the orbit decomposition.

---

## 3. Thread T3 — OTOC Saturation for the BC Scrambler

### 3.1 Precise problem statement

In research/12 Part A, the BC scrambler theorem is established as
far as the MSS bound: the BC time evolution σ_t = modular flow at
β = 1 respects λ_BC ≤ 2π · T = 2π · 1 = 2π (where T is the
inverse-temperature unit at β = 1). The bound follows from
Tomita–Takesaki modular theory plus the KMS condition.

**Problem.** Show that the bound is **saturated** — i.e., compute
the explicit out-of-time-ordered correlator

$$
F(t) \;=\; \omega_1\bigl(\,\mu_p(t)\,\mu_q\,\mu_p(t)\,\mu_q\,\bigr),
\qquad \mu_p(t) := \sigma_t(\mu_p),
$$

for primes p, q and verify that at large t the leading decay is
F(t) ∼ 1 − ε · e^{+2πt} with ε > 0, i.e., λ_BC = 2π **exactly**,
not merely ≤ 2π.

### 3.2 Current status

- **Rigorous:** MSS upper bound λ_BC ≤ 2π via modular theory.
- **Rigorous:** σ_t = modular flow for ω_1 at β = 1 (by uniqueness
  of the KMS_1 state and Tomita–Takesaki).
- **Open:** the lower bound / saturation. No explicit F(t)
  computation exists.

### 3.3 Cited results and assumptions

- Paper 3 Theorem 7.2 (Fast Scrambler from 5D Rindler). Assumed.
- Maldacena–Shenker–Stanford 2016 MSS bound. Used as black-box.
- BC-critical state ω_1 uniqueness at β = 1 (Bost–Connes 1995).
  Assumed.
- Modular theory / Tomita–Takesaki. Assumed.

### 3.4 Missing ingredient for closure

An **explicit two-prime OTOC computation** on the BC GNS space. Two
natural routes:
(i) Direct evaluation via the KMS two-point function and the
  commutation [μ_p(t), μ_q] for p ≠ q, using the Bost–Connes
  relation σ_t(μ_p) = p^{it} μ_p;
(ii) Reduction to a shifted four-point function on H_1 and evaluation
  via the explicit formula for ⟨Ω_1, μ_a μ_b^* μ_c μ_d^* Ω_1⟩ at
  β = 1.

Route (i) is quick: σ_t(μ_p) = p^{it} μ_p gives μ_p(t) = p^{it} μ_p,
so F(t) = ω_1(p^{it} μ_p μ_q p^{it} μ_p μ_q) = p^{2it} ω_1(μ_p μ_q
μ_p μ_q). This factorises cleanly; the leading large-t behaviour
is controlled by the phase p^{2it}. The question is how p^{2it} is
re-expressed as e^{λt} under the modular flow in the appropriate
modular-time coordinate τ = t/(2π).

### 3.5 Next concrete step

1. Use σ_t(μ_p) = p^{it} μ_p and compute F(t) via the ω_1 KMS
   two-point function.
2. Change variables to modular time τ = t · 2π to put the leading
   exponential in the form e^{λ_BC τ} and read off λ_BC = 2π.
3. Verify the coefficient ε = 1 − F(0)/F(∞) is strictly positive,
   i.e., the OTOC genuinely decays (non-trivial scrambling).
4. Report F(t) explicitly and the saturation statement.

**Minimum deliverable:** the explicit F(t) formula as a function of
(p, q, t) and the saturation claim proved.

### 3.6 Dependencies

- **Depends on:** research/04 (Identity 12), research/12 Part A
  (MSS upper bound).
- **Feeds:** sharpens research/12 Part A; the claim "BC is a
  maximally fast scrambler at β = 1" upgraded from structural to
  theorem.
- **Independent of:** all other threads.
- **Parallelisable with:** T2, T4, T5 (no shared machinery).

---

## 4. Thread T4 — Mellin Proportionality for the CP² Area Law

### 4.1 Precise problem statement

In research/13 Part A, the CP² string tension of Paper 5 is
identified as the matrix element

$$
\sqrt{\sigma} \;=\; \langle\psi_{\mathrm{adj}}|\hat R^{-1/2}|\psi_{\mathrm{adj}}\rangle
                 \cdot \mathcal{N}_{CP^2},
$$

where |ψ_adj⟩ is built from |γ_8⟩ (the SU(3) adjoint zero) and
N_{CP²} is the CP² volume factor. The derivation goes through the
Migdal heat-kernel expansion of 2D Yang–Mills on CP¹ and the Mellin
transform, which produces an expression of the form

$$
\sum_{R \in \mathrm{irreps}\,SU(3)} \frac{(\dim R)^{2}}{C_2(R)^{s}}
\;\stackrel{?}{\propto}\; \zeta(s) \quad\text{at }s = 1.
$$

**Problem.** Prove (or disprove, with a corrected version) the
proportionality of the Migdal-Mellin sum to ζ(s) at β = s = 1, with
an explicit proportionality constant.

### 4.2 Current status

- **Rigorous:** the Migdal heat-kernel expansion on CP¹ (classical
  result).
- **Structural:** the Mellin transform identification with a
  Dirichlet series in C_2(R)^{-s}. Written out in research/13 §3–§4.
- **Open:** the identification of Σ (dim R)²/C_2(R)^s with ζ(s) at
  s = 1. The two series are **not** literally equal — they are a
  rearrangement that requires resumming over the irreps of SU(3)
  and comparing to a rearrangement over N*.

### 4.3 Cited results and assumptions

- Paper 5 CP² area law. Assumed.
- Migdal 1975 heat kernel expansion for 2D YM. Used as black-box.
- BC partition function ζ(β) (Bost–Connes 1995). Required.
- Identification of the γ_8 eigenspace as the SU(3) adjoint sector
  of H_R (research/09, research/13 §5). Structural.

### 4.4 Missing ingredient for closure

A **rearrangement lemma** that takes the SU(3)-irrep sum to a sum
over N* with the correct multiplicities, producing the factor ζ(s)
at s = 1. Candidate identities: the Weyl dimension formula gives
(dim R)² as a polynomial in the highest weight, and C_2(R) is a
quadratic form; the sum reduces to a multidimensional Dirichlet
series that can be factored by the Euler product over primes (the
SU(3) "L-function" of the adjoint rep) and compared to ζ.

### 4.5 Next concrete step

1. Write (dim R) and C_2(R) for SU(3) in terms of highest weight
   (a, b) with dim R = (1/2)(a+1)(b+1)(a+b+2) and
   C_2(R) = a² + b² + ab + 3a + 3b.
2. Compute Σ_{a,b≥0} (dim R)² / C_2(R)^s as a double Dirichlet
   series in (a, b).
3. Factor by Euler product and compare to ζ(s) · (known
   correction factors).
4. Evaluate the proportionality constant at s = 1.

**Minimum deliverable:** either a proof of proportionality with an
explicit constant, or a counter-computation showing the sum differs
from ζ by a structured factor (e.g., L-function of the SU(3)
adjoint).

### 4.6 Dependencies

- **Depends on:** research/13 Part A, research/09 (γ_8 as SU(3)
  adjoint index).
- **Feeds:** rigorous closure of the Paper 5 transposition; the
  "QCD string tension as R̂ matrix element" claim becomes a theorem.
- **Parallelisable with:** T2, T3, T5 (no shared machinery).

---

## 5. Thread T5 — Three Remaining Missing Parameters

### 5.1 Precise problem statement

After research/15 (4 new zero placements) and research/16 (11 new
parameter fixes), the scoreboard is 34/37. The three parameters
not yet fitted to sub-percent precision by a Riemann formula:

(a) **sin θ_13 (CKM).** Current best candidate is marginal at 0.98%
(just above the sub-percent threshold).
(b) **sin²(2θ_23) (PMNS atmospheric mixing).** Likely
symmetry-enforced (near-maximal mixing suggests a discrete
symmetry on |γ_n⟩ eigenstates, not a single-zero formula).
(c) **One more.** Candidate: either a Majorana phase of PMNS
(which may be physically undetermined), or the curvature Ω_k
(consistent with zero in current cosmology, potentially not
requiring a formula).

**Problem.** Find sub-percent Riemann formulas for (a), (b), (c), or
provide a structural argument for why they should not be expected.

### 5.2 Current status

- (a) sin θ_13 CKM: best candidate 0.98%, marginal, under threshold
  but borderline.
- (b) sin²(2θ_23) PMNS: best candidate near-maximal (0.99), no
  clean γ_n formula found in the first sweep.
- (c) Pending identification; research/16 §7 has a shortlist.

### 5.3 Cited results and assumptions

- research/15 (γ_7, γ_12, γ_13, γ_14 placements).
- research/16 (11 parameter fixes including m_W = γ_2 + γ_13).
- Paper 11 G_SM structure (for symmetry-enforced arguments).
- The first 15 Riemann zeros (γ_1 through γ_15).

### 5.4 Missing ingredient for closure

A **targeted parameter sweep** using the same methods as
research/15–16, with two new ideas:
(i) Allow **composite formulas** involving two or three γ_n
  (successful for m_W = γ_2 + γ_13). Extends the search space.
(ii) Allow **symmetry-enforced zero** or **zero-up-to-corrections**
  values (atmospheric mixing, Majorana phases).

### 5.5 Next concrete step

1. For sin θ_13 CKM (current 0.98%): extend search to two-zero and
   three-zero combinations using the same pattern-fitting script
   as research/16; target sub-0.5% match.
2. For sin²(2θ_23): state the symmetry argument explicitly — if
   PMNS atmospheric mixing is maximal by a Z_2 exchange symmetry
   of |γ_a⟩ ↔ |γ_b⟩ eigenstates, identify (a, b) and verify.
3. Fix the identity of parameter (c) from research/16 §7's
   shortlist; attempt fit.
4. Write `research/37-three-remaining-parameters.md` reporting
   either fits or "physically zero/symmetry-enforced" verdicts.

**Minimum deliverable:** 37/37 scoreboard, or a principled reason
for the shortfall.

### 5.6 Dependencies

- **Depends on:** research/15, research/16.
- **Independent of:** T1, T2, T3, T4, T6, T7.
- **Parallelisable with:** everything else. This is a compute-bound
  search task, not a theorem.

---

## 6. Thread T6 — Explicit Cosmic Transition Amplitudes (γ_5 → γ_2 → γ_1)

### 6.1 Precise problem statement

Research/06 Theorem A gives the cosmic e-fold counts rigorously as
differences N_{n→m} = (γ_n − γ_m) · π²/2. The level-crossing
mechanism for *which* transitions occur (why γ_5 → γ_2 → γ_1 rather
than γ_5 → γ_1 directly, or any other path) is sketched in
research/06 §5 as the (SR1)–(SR4) conditions.

**Problem.** Compute explicitly the Landau–Zener transition rates

$$
P_{n \to m} \;=\; \exp\!\Bigl(-2\pi\,\frac{|V_{nm}|^{2}}{|d(E_n - E_m)/dt|}\Bigr)
$$

for (n, m) = (5, 2), (2, 1), and the off-path candidates (5, 1),
(5, 3), (5, 4), etc. Verify that the selected path γ_5 → γ_2 → γ_1
has maximal total amplitude. Identify the explicit time-dependence
of the BC effective Hamiltonian H_eff(β_eff(t)) that produces the
level crossings.

### 6.2 Current status

- **Rigorous:** Theorem A (e-fold counts as spectral gaps).
- **Rigorous:** Theorem B (same matrix elements V_{nm} drive CC
  formula corrections and cosmic transition rates).
- **Structural:** level-crossing mechanism via three candidate
  effective free energies (Casimir, cosmic-evolution, topology), in
  research/06 §5.
- **Open:** (SR1)–(SR4) conditions. The explicit β_eff(t)
  trajectory. The Landau–Zener rates.

### 6.3 Cited results and assumptions

- research/02 (R̂ construction).
- research/05 (CC formula via V_{nm}).
- research/06 Theorems A, B.
- research/07 (C1)–(C4) for the matter perturbation V.
- Landau–Zener theory (classical).
- The three candidate effective free energies (research/03).

### 6.4 Missing ingredient for closure

**Two coupled ingredients:**
(i) The explicit form of V_{nm} = ⟨γ_n|V|γ_m⟩ — which is itself
  gated by **thread T1** (the Mellin-dual K_{12} problem).
(ii) The explicit form of β_eff(t) — the time-dependent BC
  inverse-temperature trajectory of the universe, which requires a
  principled derivation of the cooling law (candidate: Friedmann
  equation lifted to the BC side).

### 6.5 Next concrete step

1. **Assume** the rigorous V_{nm} from T1 (placeholder: use the
   empirical |V_{12}|² = 0.2425 and the pattern of off-diagonal
   matrix elements as an ansatz).
2. Derive β_eff(t) from the 4D Friedmann equation + Identity 12 via
   the map R ↔ R̂ eigenvalue, obtaining a curve β_eff : [0, ∞) →
   (0, ∞) passing through β_eff(t) = 1 at the crossing points.
3. Compute the Landau–Zener rates at each crossing and check the
   total-amplitude selection of γ_5 → γ_2 → γ_1.
4. State the four conditions (SR1)–(SR4) as derived constraints.

**Minimum deliverable:** the Landau–Zener rate formula with V_{nm}
as a free input, reducing T6 closure to the input of T1.

### 6.6 Dependencies

- **Depends on:** T1 (explicit V_{nm}), research/06, research/05.
- **Feeds:** first-principles selection rule for the inflation
  hypothesis (Component 14 of preprint/), the cosmic timeline
  (Component 16); closes thread 3e of Phase 3.A to full rigour.
- **Partially parallelisable with T1:** the Landau–Zener formula
  with V_{nm} as free input can be written *now*; only the numerical
  evaluation has to wait for T1.

---

## 7. Thread T7 — Mathematical Proof of RH (Sub-Phase 3.D)

### 7.1 Precise problem statement

Research/08 establishes RH as a **physical theorem** of QG5D via two
independent arguments: (a) structural (Stone's theorem +
spectral theorem on T_BC + Riemann–Weil explicit formula ⇒
spec(T_BC) ⊂ R and {γ_n} ⊂ spec(T_BC), hence γ_n ∈ R), and (b)
empirical (reality of 11 specific γ_n bounded by the precision of
11 parameter matches).

**Problem.** Remove the **empirical step** from the argument: show
that the consistency of the closed transposition–quantization–
deduction programme (ledger 14) *forces* all γ_n ∈ R without
appeal to any experimental measurement, thus upgrading RH from
"physical theorem" to "mathematical theorem".

### 7.2 Current status

- **Closed in Paper 12 scope:** RH as physical theorem (research/08,
  sub-phase 3.C closed, ledger 07).
- **Deferred to Paper 13:** RH as mathematical theorem
  (sub-phase 3.D).

### 7.3 Cited results and assumptions

- research/08 (the two-argument form).
- Ledger 14 §2 (the LOCK argument L1–L5).
- All transposition results (research/10–14) are precursors; the
  LOCK requires extending these to cover every QM/GR/SM theorem.

### 7.4 Missing ingredient for closure

**The closed LOCK.** Specifically, the transposition of every QM, GR,
and SM theorem (ledger 14 §3.1, categories A, B, C, D) to its BC
analog, such that each transposed theorem produces a *real*
observable. Then any complex γ_n would trigger an inconsistency
among the transposed theorems, contradicting the (provably
consistent) BC algebra.

The LOCK argument is currently **incomplete** because only 8 of
~200 physics theorems have been transposed.

### 7.5 Next concrete step

**This is Paper 13, not Paper 12.** Next step is to *scope* the sequel:

1. Enumerate the priority list of the next 8 transpositions (ledger 14
   §3.4): Atiyah–Singer, Wess–Zumino, Coleman–Mandula + HLS, Penrose
   singularity, asymptotic freedom, anomaly cancellation, CKM/PMNS
   unitarity, Higgs mechanism.
2. Estimate the completeness threshold at which the LOCK becomes
   rigorous (how many transpositions are enough?).
3. Draft `paper13/00-attack-plan.md` with phases (1) complete
   transposition, (2) completeness argument, (3) RH as corollary.

**Minimum deliverable for Paper 12:** none — T7 is out of scope.
Scoping the sequel is a *post-Paper-12* activity.

### 7.6 Dependencies

- **Depends on:** everything in Paper 12 (as a launching pad).
- **Feeds:** Paper 13 and beyond.
- **Out of Paper 12 scope.**

---

## 8. Dependency Graph

```
                     Gap 1: Connes–Marcolli explicit formula (research/18)
                                            |
                +---------------------------+---------------------------+
                |                           |                           |
                v                           v                           v
         [T1: K_{12}]               [Gap 2: Galois orbit         [other uses: research/02,
           rigorous                  decomposition H_R              04, 05, 08, 11, 14, 17]
                |                    (research/19)]
                |                           |
                |                           v
                |                   [T2: BC-intrinsic SU(3)]
                |                    (Kirillov on H_3-orbit)
                |                           |
                |                           v
                |                   [research/09 rigorous]
                |                   (pattern of zero indices)
                |
                v
         [T6: cosmic transition amplitudes]
         (Landau–Zener for γ_5 → γ_2 → γ_1)
                |
                v
         [first-principles selection rule]
         (closes research/06 §5 (SR1)–(SR4))


  Independent threads (parallelisable):

    [T3: OTOC saturation]   [T4: Mellin proportionality   [T5: three missing
    (explicit F(t) for       for CP² area law]             parameters]
     BC scrambler)           (Σ(dim R)²/C_2(R)^s ↔ ζ)      (targeted search)
          |                         |                             |
          v                         v                             v
    research/12 Part A          research/13 Part A           research/15–16
    upgraded to theorem         upgraded to theorem          scoreboard 37/37


  Out of Paper 12 scope:

    [T7: math RH] ← needs completed LOCK (ledger 14 §2)
                 ← routes to Paper 13
```

**Key edges (read top to bottom):**
- Gap 1 (research/18) blocks **T1** directly and is a shared
  foundation for several downstream claims. Writing research/18 is
  the prerequisite for attacking T1.
- Gap 2 (research/19) blocks the **rigorous version of research/09**
  and feeds T2; T2's output in turn makes research/19 cleanly
  computable (the Kirillov stabiliser is the continuous piece of
  the orbit decomposition), so T2 ↔ research/19 is a productive
  coupling.
- **T6 depends on T1** for the numerical V_{nm}. T6 can be written
  up with V_{nm} as a placeholder input, then instantiated once T1
  closes.
- **T3, T4, T5 are fully independent** of T1, T2, T6 and of each
  other. They can be attacked in any order or in parallel.
- **T7 is out of scope**; its scoping is post-Paper-12.

---

## 9. The Most Efficient Next Thread to Attack

**Recommendation: T1 (rigorous K_{12}).**

Reasoning:

1. **T1 is the only thread whose current numerical estimate actively
   contradicts the framework's empirical claim.** The truncated-model
   result |V_{12}|² ∼ 2.4 × 10⁻⁵ vs empirical 0.2425 is a 10⁴ gap.
   Until closed, the "CC formula = matrix element of V on H_R"
   structural story has a quantitative question mark attached.
   Every other open thread is either consistent or merely
   incomplete.

2. **T1 is the unique upstream bottleneck.** T6 depends on T1 for the
   numerical V_{nm}; the quantitative version of research/05 §4.1
   and research/07 depend on T1; the "factor of 2 SM match" of
   ledger 09 is withdrawn pending T1. Closing T1 unblocks three
   distinct downstream claims.

3. **T1 has a concrete tool to try.** The T1–T4 program of
   research/17 is a step-by-step recipe. Step 1 (writing the
   spectral projector P_n via the explicit formula) is
   immediately actionable, pending **research/18** (Gap 1, the
   Connes–Marcolli explicit formula) being written first.

4. **Attacking T1 forces writing research/18.** Research/18 is the
   most-cited external reference in the programme and Gap 1 of the
   audit. Attacking T1 is the natural forcing function for writing
   it.

**Cost of T1:** medium-to-high effort, medium risk. The distributional
calculation may reveal that K_{12}(log p) is genuinely small (in which
case the CC formula's numerical agreement is coincidental to the
leading term, and the structural claim survives but the quantitative
claim weakens further). Either outcome is **publishable** and
calibration-improving.

**Runner-up: T2 (BC-intrinsic SU(3)).** If T1 is blocked on
research/18, T2 is the next most productive. The Kirillov
calculation is self-contained, low-risk, and closes the Paper 11 ↔
Paper 12 corollary claim cleanly. It also unlocks research/19.

---

## 10. Parallelisation

Three groups of threads can be attacked in parallel without
collision:

**Group α (BC-algebra interior, no shared machinery):**
- T2 — BC-intrinsic SU(3) (Kirillov on H_3-orbit)
- T3 — OTOC saturation (direct F(t) via σ_t(μ_p) = p^{it} μ_p)
- T4 — Mellin proportionality (SU(3) irrep sum ↔ ζ)

All three are in pure BC-algebra territory with no shared
intermediate results. They can run as three independent agents.

**Group β (data/search tasks):**
- T5 — three remaining missing parameters (targeted search)
- (Also: Gap 6, research/23 predictions master table)

These are compute-bound rather than theorem-bound and can run
in the background.

**Group γ (T1-gated chain):**
- T1 — K_{12} rigorous (requires Gap 1 / research/18 first)
- T6 — cosmic transition amplitudes (depends on T1's V_{nm})

This is a sequential chain: write research/18, then attack T1,
then instantiate T6.

**Recommended parallel attack for the next work wave:**

| Agent | Thread(s) | Output |
|:------|:----------|:-------|
| A | research/18 then T1 | Connes–Marcolli explicit formula + rigorous K_{12} |
| B | T2 | BC-intrinsic SU(3) via Kirillov |
| C | T3 | Explicit BC OTOC F(t) |
| D | T4 | Migdal–Mellin ζ identification |
| E | T5 | Three-parameter search |
| F | T6 skeleton | Landau–Zener formula with V_{nm} placeholder |

Six agents, four fully independent (B, C, D, E), one sequential
chain (A → T1), one partially blocked (F).

**T7 (math RH) is deferred to Paper 13 and is not in the work wave.**

---

## 11. Status Snapshot for the Next Ledger

| # | Thread | Before wave | Target after wave |
|---|--------|-------------|-------------------|
| T1 | K_{12} rigorous | honest negative | rigorous band [a, b] around empirical |
| T2 | BC-intrinsic SU(3) | transported | Lie-algebra level closure |
| T3 | OTOC saturation | upper bound only | saturation theorem |
| T4 | Mellin proportionality | structural | proportionality lemma or corrected form |
| T5 | 3 missing params | 34/37 | 37/37 or principled shortfall |
| T6 | Cosmic transition amplitudes | level-crossing sketch | Landau–Zener rates (pending T1) |
| T7 | Math RH | deferred | scoped for Paper 13 |

---

## 12. References

- `00-attack-plan.md` — master ledger
- `13-current-state.md` — rigorous/structural/open snapshot
- `14-grand-strategy-transposition-quantization-deduction.md` — the
  long-arc programme, L1–L5 of the LOCK
- `15-audit-and-missing-research-files.md` — the audit (this file is
  Gap 3 of the audit)
- `research/02-quantize-R-construction.md`
- `research/04-identity-12-rigorous.md`
- `research/05-derive-cc-formula.md` — CC formula as matrix element
- `research/06-cosmic-transition-amplitudes.md` — T6 home
- `research/07-matter-content-Vnm-derivation.md` — (C1)–(C4) matter
- `research/08-rh-as-physical-theorem.md` — T7 starting point
- `research/10-transposition-gauge-group-3primes.md` — T2 home
- `research/12-transposition-scrambler-and-YM-gap.md` — T3 home
- `research/13-transposition-CP2-area-and-theorem-U.md` — T4 home
- `research/15-find-gamma-7-12-13-14.md` — T5 precursor
- `research/16-fix-14-missing-parameters.md` — T5 precursor
- `research/17-mellin-kernel-K12-numerical.md` — T1 home, T1–T4 program
- `research/18` (to be written) — Connes–Marcolli explicit formula
- `research/19` (to be written) — Galois orbit decomposition of H_R

---

*Seven threads. One blocking upstream (T1, gated on research/18).*
*Three fully parallelisable (T2, T3, T4). One search task (T5). One*
*T1-dependent chain (T6). One out-of-scope (T7 → Paper 13). The most*
*efficient next move is research/18 → T1. The most effective*
*work-wave parallelisation is six agents running (A = research/18+T1,*
*B = T2, C = T3, D = T4, E = T5, F = T6 skeleton).*
