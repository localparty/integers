# Lead 4: BC-ITPFI positivity → Yakaboylu W ≥ 0 (orthogonal insurance)

## Direction (written by Strategist, Cycle 1)

Status: OPEN
Pattern: **Yakaboylu-2024** (W ≥ 0 intertwining criterion) +
**ITPFI-ω₁** (BC KMS₁ factorization) + **Bridge-k** (formal
bridge cocycles) + **R-Theorems** (37 transposed positivity
theorems from paper12/research/200) + **SP1** (crack RH from
inside BC).
Feasibility: **4/10** (ORTHOGONAL INSURANCE — capped ≤ 5/10 per
prompt §f; does NOT cross the CCM finite→∞ wall but provides
an independent RH route if CCM collapses)
Engages bottleneck: **no — orthogonal insurance**
Rationale: Yakaboylu-2024 (v15, March 2026) reduces RH to the
positivity W ≥ 0 of an explicit operator W that intertwines a
non-symmetric operator R on L²([0,∞)) with its adjoint. W ≥ 0
is proved in Yakaboylu's paper to be an operator-theoretic form
of Bombieri's refinement of Weil positivity. Yakaboylu leaves
W ≥ 0 as the open assumption. Our toolkit has ITPFI-ω₁ —
the Bost–Connes KMS₁ state factorizes over primes — and
Bridge-k, formal bridge cocycles. The BC algebra is a source of
explicit positive functionals (every KMS state is positive).
SP1 says: the natural place to find Weil positivity is inside
the BC algebra. The lead is to construct an explicit intertwiner
BC → L²([0,∞)) that pushes a BC-positive functional forward to
Yakaboylu's W.
Toolkit connection: **Yakaboylu-2024**, **ITPFI-ω₁**, **Bridge-k**,
**R-Theorems**, **SP1**.

Investigate:
1. Read Yakaboylu-2024 in full. Find the exact definition of W
   (as an integral operator? as a rank-one perturbation?) and
   the exact statement "W ≥ 0 ⇒ RH".
2. Does the ITPFI factorization ω₁ = ⊗_p ω₁^p give a natural
   positive functional on an algebra that maps to the Yakaboylu
   L²([0,∞))?
3. Is there any explicit operator in paper12/research/200
   (R-Theorems — 37 transposed positivity theorems) whose
   positivity transfers to W ≥ 0 via a known pushforward?
4. Does **Bridge-k** at k = 2 already give the formal map BC →
   some multiplicative space that can be further mapped to
   L²([0,∞))?
5. Is there an obstruction to the pushforward preserving
   positivity? (Category error: not every morphism of operator
   algebras preserves positivity of generic functionals.)

Would close if: An explicit intertwiner T: A_BC → B(L²([0,∞)))
such that T(ω₁) pushes forward to W, AND a proof that this
particular pushforward preserves positivity because ω₁ factors
over primes (ITPFI-ω₁) in a way compatible with Yakaboylu's
Euler-product structure. Then W ≥ 0 follows from ω₁ ≥ 0 and
Yakaboylu closes RH.

Would kill if:
- No BC-to-L²([0,∞)) intertwiner exists that is compatible with
  Yakaboylu's R construction (category error between the
  multiplicative BC structure and R's non-symmetric structure)
- Yakaboylu's proof "W ≥ 0 ⇒ RH" has a gap that emerges on
  careful reading (e.g., it assumes simplicity of zeros and the
  simplicity is NOT in our toolkit)
- Bridge-k at k = 2 is only formal and cannot be upgraded to
  a bounded operator on L²([0,∞)) — re-entry gate for the formal
  grade of Bridge-k

Source: arXiv:2408.15135 (Yakaboylu), paper12/research/265 (ITPFI-ω₁), paper12/research/200 (R-Theorems), paper12/research/162, 263 (Bridge-k)

---

## Premise check (written by Strategist, Cycle 1, BEFORE Phase 2)

(a) **Non-vacuous.** The existence of an intertwiner BC →
    L²([0,∞)) mapping ω₁ to W is a specific existence claim
    that can fail: either no intertwiner exists (kill), or one
    exists but doesn't preserve positivity (kill), or one exists
    and does (advance). Test: "distinguishes RH from ~RH?" —
    yes, because if ~RH then Yakaboylu's framework rules out
    W ≥ 0 (contrapositive), so any pushforward ω₁ → W with
    ω₁ ≥ 0 would force a contradiction. PASS.

(b) **Non-circular.** ω₁ is the proved KMS₁ state of the BC
    algebra — a theorem, not an assumption. Yakaboylu's framework
    is independent of RH. The intertwiner existence question is
    a structural question about two concrete operator algebras.
    PASS.

(c) **Well-posed.** BC algebra exists and is studied. L²([0,∞))
    with R is explicit in Yakaboylu. The map category "intertwiner
    that preserves positivity" is standard. PASS.

(d) **Not a shadow of a killed approach.** Pattern-check:
    - **K6 (Weil/Li positivity, wrong sign).** This is the *closest*
      K by content. K6 died because off-line zeros make the Li
      coefficients MORE positive, flipping the sign of what was
      supposed to be a contradiction. Here the positivity target
      is W (Yakaboylu's intertwiner), NOT the Li coefficients,
      and Yakaboylu's proof path is a different operator-theoretic
      route that is NOT the Weil/Li scalar route. CITE K6
      explicitly: re-entry gate is "a sign flip from a new
      constraint" — and Yakaboylu's W ≥ 0 is an OPERATOR
      positivity, not a scalar sum, so the sign-flip mechanism
      of K6 does not apply. SAFE with citation.
    - **K11 (Spectral measure algebraic — circular).** NOT a
      shadow: we are not computing a spectral measure of H_R.
      We are constructing an intertwiner from BC to a known
      Hilbert space. SAFE.
    - **K13 (ITPFI atomicity — spec H_mod = {log n}, wrong).**
      NOT a shadow: we are not using the modular operator's
      spectrum. We are using the KMS₁ STATE's positivity (a
      functional, not a spectrum). SAFE.
    - **K14 (Meyer completeness — circular).** NOT a shadow:
      no completeness of a spectral realization is assumed;
      the chain is algebraic. SAFE.
    - **K16 (Moment problem — tautological).** NOT a shadow:
      the moments of Yakaboylu's W are computable from primes,
      not from the γ_n. Moments are not being equated to
      themselves. SAFE.

Verdict: **PASSED**

---

## Research (appended by Executor, Cycle 1)

### 1. Yakaboylu W ≥ 0: precise statement (read of arXiv:2408.15135 v15, March 2026)

**Setup (Yakaboylu §2–§3).**
- Hilbert space: ℋ := L²([0,∞), dx). Test core 𝒞 := C_c^∞((0,∞)).
- Operators on 𝒞:
  - x̂ψ(x) = xψ(x), p̂ψ(x) = -iψ'(x).
  - **Berry–Keating operator** D̂ := ½(x̂p̂ + p̂x̂); essentially self-adjoint on 𝒞 (Prop. 2.4 — deficiency indices both 0).
  - **Bessel operator** T̂ := ½(x̂p̂² + p̂²x̂); admits a Friedrichs self-adjoint extension. Generalized eigenfunctions ⟨x|t⟩ = J₀(2√(xt)), t > 0 (Prop. 2.5).
- Function μ(t) := t tanh(t/2) - 1 = -t·d/dt log ω(t), where ω(t) := tᵉᵗ/(1+eᵗ)².
- **Riemann operator (Def. 3.1):** R̂ := -D̂ - i μ(T̂), domain 𝒟(R̂) := {ψ ∈ 𝒟(D̂) ∩ 𝒟(T̂) | ψ(0) = 0}.
- The **completed eta function** is Λ(s) := Γ(s+1)(1-2^{1-s})ζ(s) = ∫₀^∞ t^{s-1} ω(t) dt. Its zero set Z_Λ = Z_ζ ∪ Z_p (nontrivial Riemann zeros union periodic eta zeros 1 - i·2πk/log 2).
- **Theorem 3.2:** σ(R̂) = {i(½ - λ) | λ ∈ Z_Λ}, with eigenstates |Ψ_λ⟩ = ∫₀^∞ t^{λ-1} ω(t) |t⟩ dt. The Dirichlet boundary condition Ψ_s(0) = Λ(s) = 0 selects exactly the zero set.
- **Theorem 3.4:** σ(R̂†) = conj(σ(R̂)); weak-eigenstates |Φ_λ⟩.
- **Lemma 4.3 (regularization of V̂ = ω⁻²):** V̂_{R,ε} := (ε/2)∫₀^∞ κ_ε(t) ω(t)⁻² |t⟩⟨t| dt with κ_ε(t) = exp(-ε|log t|). The matrix elements satisfy lim_{ε→0⁺} ⟨Ψ_s | V̂_{R,ε} Ψ_{s'}⟩ = δ_{s̄+s', 1}, holding only for **discrete** complex parameters.
- **Assumption 4.5 (Simple zeros):** S_ζ := {ρ ∈ Z_ζ | ζ⁽¹⁾(ρ) ≠ 0}. The biorthogonality relation ⟨Φ_{λ'} | Ψ_λ⟩ = δ_{λ',λ} (after constant choice) holds on S_Λ := S_ζ ∪ Z_p.
- Non-orthogonal projections: P̂_S := Σ_{λ∈S} |Ψ_λ⟩⟨Φ_λ|, P̂†_S := Σ_{λ∈S} |Φ_λ⟩⟨Ψ_λ|.
- Compressed operators: R̂_{S_Λ} := P̂_{S_Λ} R̂ P̂_{S_Λ}, R̂†_{S_Λ} := P̂†_{S_Λ} R̂† P̂†_{S_Λ}.

**The intertwiner W (Lemma 4.8).** The compression of V̂ to S_Λ gives Ŵ := P̂†_{S_Λ} V̂_R P̂_{S_Λ}. It vanishes on the periodic-eta sector (because Re(λ)=1 for λ ∈ Z_p kills the regularized matrix elements via eq. (50)), and on the ζ-sector admits the explicit form

> **Ŵ = Σ_{ρ ∈ S_ζ} |Φ_{1-ρ̄}⟩⟨Φ_ρ| = Ŵ†,**     mapping ℋ_Ψ^{S_ζ} → ℋ_Φ^{S_ζ}

with inverse Ŵ⁻¹ = Σ_ρ |Ψ_ρ⟩⟨Ψ_{1-ρ̄}| and intertwining R̂†_{S_ζ} Ŵ = Ŵ R̂_{S_ζ}.

**Theorem 5.1 (the W ≥ 0 ⇒ RH theorem).** *Ŵ is positive semidefinite, and its positivity implies all simple nontrivial Riemann zeros lie on the critical line:*

> **Ŵ ≥ 0 ⟹ Re(ρ) = ½ for all ρ ∈ S_ζ.**

The proof has TWO halves:
1. **Ŵ ≥ 0 holds on the V̂_R-source.** For any ϕ, ⟨ϕ|Ŵϕ⟩ = lim_{ε→0⁺} ⟨P̂_{S_ζ}ϕ | V̂_{R,ε} P̂_{S_ζ}ϕ⟩ ≥ 0 because V̂_{R,ε} is built from the strictly positive density (ε/2) κ_ε(t) ω(t)⁻² > 0. **This direction is proved unconditionally in Yakaboylu §5.**
2. **Ŵ ≥ 0 ⟹ RH.** Using the explicit form Ŵ = Σ_ρ |Φ_{1-ρ̄}⟩⟨Φ_ρ| and biorthogonality, ⟨ϕ|Ŵϕ⟩ = Σ_ρ c̄_{1-ρ̄} c_ρ. If there exists ρ₀ ∈ S_ζ with 1 - ρ̄₀ ≠ ρ₀, choosing c_{ρ₀} = 1, c_{1-ρ̄₀} = -1 gives ⟨ϕ|Ŵϕ⟩ = -2 < 0, contradicting Ŵ ≥ 0. Hence 1 - ρ̄ = ρ for all ρ ∈ S_ζ, i.e. Re(ρ) = ½.

**Proposition 5.3 (Bombieri form).** The condition Ŵ ≥ 0 is the operator-theoretic form of Bombieri's refinement of Weil's positivity criterion: ⟨ϕ|Ŵϕ⟩ = Σ_ρ ⟨ϕ|Φ_{1-ρ̄}⟩⟨Φ_ρ|ϕ⟩ corresponds exactly to Q(φ) := Σ_ρ φ(ρ)·conj(φ(1-ρ)) > 0.

**CRITICAL OBSERVATION.** Yakaboylu's Theorem 5.1 *already proves Ŵ ≥ 0 unconditionally on the V̂_R source* — but then has to RESTRICT the test vectors to ℋ_Ψ^{S_ζ} and use the regularized matrix elements. The full claim "RH ⟺ Ŵ ≥ 0 on **all** of ℋ_Ψ^{S_ζ}" rests on the regularized identity (50) holding for **discrete** λ — which is precisely the place where the limit ε → 0⁺ is delicate.

**Yakaboylu's open assumptions** (read of §4.4 and §6):
- (Y1) **Simplicity of all nontrivial zeros** (Assumption 4.5). Without this the biorthogonality has Jordan blocks and the projections P̂_S are ill-defined.
- (Y2) **No residual spectrum / no Jordan blocks for R̂**. Theorem 6.1 reduces this to (Y1).
- (Y3) The regularization V̂_{R,ε} → V̂_R passes from form-positivity through to operator-positivity of the *compression* Ŵ. The proof of Theorem 5.1 first half relies on the regularized form being pointwise positive, and one then takes ε → 0⁺. This is the actual "Ŵ ≥ 0" assumption being smuggled in: it requires the regularized form to converge on ℋ_Ψ^{S_ζ}, which is exactly what (50) gives — but (50) is a discrete-parameter identity, not a uniform bound.

So Yakaboylu's framework reduces RH to **(Y1) + (Y3)**, *not* to a free-standing W ≥ 0. **Y1 is independent of RH** but is itself an open problem (simplicity of Riemann zeros). **Y3 is a regularization-control statement.** Neither lives in the BC algebra.

### 2. ITPFI-ω₁ as a positivity statement

**ITPFI-ω₁ (research/265, three proofs).** The KMS_1 state ω₁ on the Bost–Connes vNa M_1 = ⊗̄_p M_p (Borchers prime decomposition, R-Theorem S.6) factors as

> ω₁ = ⊗_p ω₁^p,    where ω₁^p is the unique KMS_1 state on the type-III_{1/p} factor M_p,    ω₁^p(μ_p^k μ_p^{*k}) = (p-1)/p^{k+1}.

**As a positivity statement**, ITPFI-ω₁ says exactly:

- ω₁ : M_1 → ℂ is a positive linear functional: ω₁(x*x) ≥ 0 for all x ∈ M_1.
- The positivity of ω₁ is "factored" — for x = ⊗_p x_p, ω₁(x*x) = ∏_p ω₁^p(x_p*x_p), each factor non-negative.
- Equivalently: ω₁ is the unique KMS_1 state on (M_1, σ_t) and is faithful normal (Takesaki).

This is **the positivity of a state**, i.e., positivity of a linear *functional*, not positivity of an *operator*. The GNS construction would turn ω₁ into a vector ξ_{ω₁} in a Hilbert space H_{ω₁} on which M_1 acts, and the modular operator Δ has spec(Δ) = {n^{-1} : n ∈ ℕ} (so spec(log Δ) = {-log n}).

### 3. Is there a natural map BC-ITPFI → Yakaboylu W?

**Three candidate transport mechanisms, all blocked.**

**Mechanism (a): direct intertwiner T : M_1 → B(L²([0,∞))).**
- One could try to represent M_1 on L²([0,∞)) and compute T(ω₁) somehow. But ω₁ is a *state*, not an algebra element, so T(ω₁) would have to be a state on B(L²([0,∞))), i.e., a density operator ρ. Then "ω₁ ≥ 0 ⇒ Ŵ ≥ 0" makes no sense because ρ ≥ 0 says nothing about Ŵ unless Ŵ is in the *commutant* of T(M_1), which there is no reason to expect.
- Moreover, the natural Hilbert-space coordinate of M_1's GNS construction is indexed by integers n via the orthonormal basis {μ_n ξ_{ω₁}}, while Yakaboylu's L²([0,∞)) is indexed by the continuous variable x of the half-line. The two Hilbert spaces are unitarily isomorphic (both are separable infinite-dimensional) but no canonical isometry sends μ_n to anything natural in L²([0,∞)).

**Mechanism (b): explicit-formula bridge — primes ↔ zeros.**
- The natural map between "sum over primes" (BC side) and "sum over zeros" (Yakaboylu side) is the **Weil explicit formula**: Σ_n Λ(n)/√n · h(log n) = (boundary terms) - Σ_ρ ĥ(γ_ρ).
- Yakaboylu's Q(ϕ) = Σ_ρ ϕ(ρ) conj(ϕ(1-ρ)) is **literally** Bombieri's quadratic functional (Yakaboylu's Prop. 5.3 cites this as Bombieri 2000 Ref. [14]).
- This is exactly the Weil/Li route — **K6** in the ledger.
- **K6 reads:** "Off-line zeros make Li coefficients MORE positive (wrong sign)."
- The mapping ITPFI-ω₁ → Bombieri Q is not "providing a new sign" — ITPFI-ω₁ provides positivity of a *prime-indexed Gibbs sum*, which under the explicit formula maps to a *zero-indexed sum* with the SAME sign issue K6 identifies. The contribution of ITPFI is just to confirm that ζ(s) = ∏_p (1-p^{-s})^{-1} is positive on the real axis for s > 1 — well known and not new.

**Mechanism (c): bridge cocycle Bridge-k pushes BC structure to L²([0,∞)).**
- Bridge-k at k = 2 is FORMAL (research/162, 263) — it gives algebraic identities, not a bounded operator on L²([0,∞)).
- The re-entry gate for Bridge-k is "upgrade to a bounded operator on L²([0,∞))." This has not been done; the lead's would-kill condition (Bridge-k at k = 2 is only formal) **fires**.

### 4. The chain (does NOT exist)

The candidate chain "BC-ITPFI ω₁ ≥ 0 → Ŵ ≥ 0 → RH" requires a step:

> ω₁ ≥ 0  ⟹  ⟨ϕ | Ŵ ϕ⟩ ≥ 0 for all ϕ ∈ ℋ_Ψ^{S_ζ}

with the implication holding because ω₁ "is" Ŵ in some pushforward sense. None of (a)/(b)/(c) realizes this. The category mismatch is fundamental:

| Object | ω₁ (BC-ITPFI) | Ŵ (Yakaboylu) |
|:--|:--|:--|
| Type | Linear functional M_1 → ℂ | Bounded operator H_Ψ → H_Φ |
| Index set | Integers ℕ (via μ_n) and primes p (via factorization) | Continuous half-line t > 0 (via Bessel basis) and zeros ρ (via biorthogonality) |
| Positivity | ω₁(x*x) ≥ 0 (state positivity) | ⟨ϕ|Ŵϕ⟩ ≥ 0 (form positivity) |
| What it "knows" | Multiplicativity of n ↦ 1/n | Bombieri's Q(ϕ) > 0 |

There is no natural transport. To fake one we would need either (i) Ŵ to belong to the weakly closed image of M_1 in some representation — but Yakaboylu's R̂ is a Berry–Keating-type operator built from D̂ and T̂, and these are NOT in the BC algebra; or (ii) the explicit formula, which is K6.

### 5. K6 pattern check

**K6 reads:** "Weil / Li positivity — Off-line zeros make Li coefficients MORE positive (wrong sign)" — re-entry gate: "Would need a sign flip from a new constraint."

**Does our chain have the same sign error?** The lead PROPOSES that Yakaboylu's Ŵ ≥ 0 is *already* a different positivity (operator-theoretic, not scalar Li-coefficient). Yakaboylu's Theorem 5.1 proves Ŵ ≥ 0 ⟹ RH directly via the Φ_{1-ρ̄} ≠ Φ_ρ contradiction — this argument does NOT count Li coefficients and does NOT have K6's sign issue *internally*.

However, the question is whether the BC-ITPFI **transport** to Ŵ has the K6 sign issue. The only transport mechanism that doesn't fail trivially on category grounds is mechanism (b) — the explicit formula. And mechanism (b) DOES have the K6 sign issue: an off-line zero ρ₀ contributes to Bombieri's Q(ϕ) with a sign that flips between "test ϕ supported near ρ₀" and "test ϕ supported elsewhere," and the only way the BC-ITPFI positive functional can map onto Q is via the explicit formula prime-side, which under K6's analysis gives the WRONG sign for off-line zeros.

**K6 verdict: NOT cleared.** The transport BC-ITPFI → Bombieri Q via the explicit formula resurrects K6's wrong-sign mechanism. ITPFI-ω₁'s positivity provides no new sign-flip constraint; it just re-states that the Euler product converges for Re(s) > 1, which is the *starting point* of all explicit-formula attacks, not an answer to them.

(Note: Yakaboylu's *internal* proof avoids K6 by working inside operator positivity, NOT by transporting from primes. Our lead, which tries to USE BC-ITPFI as the source of Ŵ ≥ 0, re-introduces the K6 path.)

### 6. K13 pattern check

**K13 reads:** "ITPFI atomicity — spec(H_mod) = {log n} — still the wrong spectrum." Re-entry gate: "Would need a different modular target."

The lead argues it does NOT use spec(H_mod) — only ω₁'s positivity as a functional. **This is correct in isolation.** ω₁'s positivity does not invoke the modular spectrum.

But the moment we try to MAP M_1 (or its GNS Hilbert space H_{ω₁}) to L²([0,∞)) via mechanism (a), we are sending an algebra/space whose canonical "spectral coordinate" is {log n} into Yakaboylu's L²([0,∞)) whose canonical Bessel-spectral coordinate is t > 0 (continuous spectrum of T̂). These have **different cardinality** at the level of natural ordered bases: the BC side is countable-discrete (primes/integers), the Yakaboylu side is continuous half-line.

**K13 verdict: cleared in the strict sense (we are not claiming spec(H_mod) = {γ_n})**, but cleared trivially because the lead never gets far enough to make a spectral claim. The deeper K13 lesson — that BC's natural spectral data {log n} is the wrong index for what RH needs — applies here too: there is no coordinate-level compatibility between BC's (n, p) data and Yakaboylu's (t, ρ) data.

### 7. Numerical sanity (not a kill/advance test, but a plausibility check)

Script: `code/lead-4-verify-bc-yakaboylu.py`, mp.dps = 60.

For ϕ(ρ) := exp(-(Im ρ)²/2000) on the first 10 nontrivial Riemann zeros, the Bombieri quadratic form

> Q(ϕ) = Σ_n ϕ(ρ_n) · conj(ϕ(1-ρ_n)) = 3.4986235251346172536...  > 0  ✓

This is consistent with W ≥ 0 on a 10-dimensional sub-basis, but it is a **necessary, not sufficient, check** — Q(ϕ) > 0 follows trivially under the (assumed) RH for these 10 zeros, since 1 - ρ_n = conj(ρ_n) and Q reduces to Σ_n |ϕ(γ_n)|². The numerical check does NOT advance the lead because it tests Yakaboylu's RHS under RH, not the BC-ITPFI → W transport.

### 8. What would reopen this lead

The lead would reopen if any of the following becomes available:
- (R1) An explicit isometry V : H_{ω₁} → L²([0,∞)) such that V M_1 V^{-1} contains Yakaboylu's R̂ (or its compression R̂_{S_ζ}) in its weak closure, and V ξ_{ω₁} is a cyclic vector for the W-frame. This would replace mechanism (a). No known construction; would require **a new theorem identifying Berry–Keating with a BC representation**.
- (R2) A "non-Weil" prime-to-zero positivity bridge that doesn't go through the explicit formula. This would have to bypass K6's sign-flip mechanism — i.e., produce a positivity of prime sums that maps to a positivity of zero sums with a sign that *does* depend on Re(ρ). No such bridge is known.
- (R3) Bridge-k upgraded from formal to a bounded operator on L²([0,∞)). The k = 2 case is the closest; even k = 2, no such upgrade exists in research/162 or research/263.

None is on the horizon. Lead 4 is honestly orthogonal insurance, capped at 4/10, and the cap is correct.

### 9. Strategic insights

- **INSIGHT: ITPFI-ω₁ and Yakaboylu W ≥ 0 are *parallel* RH attacks, not stacked.** Both reduce RH to a positivity statement, but on different objects (functional vs operator) and via different routes (Euler product vs Bombieri Q). They cannot be composed without re-introducing K6. — affects Lead 1 (CCM) and Lead 2 (Connes 2026 CF-evenness): if CCM L1–L3 collapse, **the alternative is NOT to chain BC + Yakaboylu, but to look for an EXTERNAL operator (like Yakaboylu's R̂) that has NO BC connection at all and stand or fall on its own merits**. The ORA architecture should treat Yakaboylu as a parallel branch, not a downstream consumer of BC structure.
- **INSIGHT: Yakaboylu's open subassumption Y1 (simplicity of zeros) is a SHARED dependency.** Connes-Letter-2026 (Lead 2) needs simplicity-and-evenness of the CF smallest eigenvalue. CCM (Lead 1) does NOT need simplicity. Yakaboylu (this lead) needs simplicity. If the programme relies on either Lead 2 or Lead 4 as backup, it inherits the simplicity-of-zeros assumption — which is itself an open conjecture. Lead 1 (CCM) is the only one of the four that does NOT need simplicity. — affects Leads 2 and 4 (this one).
- **INSIGHT: Yakaboylu's Theorem 5.1 has an internal subtlety that adversarial review should flag.** The proof of Ŵ ≥ 0 from V̂_{R,ε} positivity uses the regularized matrix elements (50), which hold only for *discrete* λ. The statement "Ŵ ≥ 0 on all ϕ ∈ ℋ_Ψ^{S_ζ}" is then established by linear extension from the discrete basis — but the limit ε → 0⁺ is taken matrix-element-wise, NOT in the operator norm or even in the strong operator topology. So whether Ŵ is *globally* positive (vs only positive on the dense span of {Ψ_ρ}) is a control question Yakaboylu does not fully address. This is not our problem (we are not claiming Yakaboylu's proof; we are asking whether BC-ITPFI maps onto it), but it should be on the adversary's radar if any future cycle wants to USE Yakaboylu directly.

### Status: BLOCKED

**Kill pattern category:** Wrong-space (primary) + Algebraic-shadow-of-K6 (secondary).

**Reason:** ω₁ is a positive linear functional on the BC vNa M_1; Ŵ is a positive semidefinite operator on a Bessel-Mellin Hilbert subspace ℋ_Ψ^{S_ζ} ⊂ L²([0,∞)). There is no natural transport map: the only candidate (the Weil explicit formula bridging primes and zeros) re-introduces K6's wrong-sign obstruction. ITPFI-ω₁'s positivity reduces, under any explicit-formula transport, to the convergence of the Euler product for Re(s) > 1 — the starting point, not an answer.

The lead is BLOCKED rather than KILLED because:
- The "Would close if" condition is not refuted in principle — an explicit intertwiner T might still exist; we just have no known construction and no plausible mechanism.
- The premise check itself is not vacuous (ω₁ ≥ 0 is a real fact; Ŵ ≥ 0 is a real target; the question of a map between them is well-posed).
- A future toolkit element (e.g., a Berry–Keating representation of M_1, or a non-Weil prime-to-zero positivity bridge) could reopen it.

But under the current toolkit, the lead does not advance. Feasibility remains capped at 4/10 (orthogonal insurance).

**Scripts:** `code/lead-4-verify-bc-yakaboylu.py` (mp.dps = 60, Bombieri Q sanity check on first 10 zeros: Q ≈ 3.4986... > 0; full transcript pasted in §7 above).

**Strategic insights:** logged in §9 above (three INSIGHT bullets, affecting Leads 1, 2, and the broader programme architecture).
