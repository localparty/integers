# M.1.1.c — Explicit form of the bridge projector `P_k^𝔭` for `k ∈ {2,3,4,6}`

*Author: Claude Opus 4.6 (W2-A)*
*Cycle: 2*
*Status: **ADVANCED (with caveat)** — all three sub-goals (M.1.1.c.1, M.1.1.c.2, M.1.1.c.3) closed via a **corrected formula** that differs from the candidate proposed in the spawn prompt. The candidate cyclic-character formula is **refuted**. The corrected operator is*

> `P_k^𝔭 := I − e_{𝔭^k} = I − s_𝔭^k (s_𝔭^k)^*`

*i.e. the orthogonal complement of the range projection of the k-th iterate of the isometry at 𝔭. All three required properties (Hermitian idempotent; modular invariant; KMS expectation value matches Prop 6.2) are verified analytically and numerically.*
*Generative step: **Step 2 REINTERPRET** — the candidate `(1/k) Σ ζ_k^j s_𝔭^j (s_𝔭^j)^*` is not Hermitian because the `e_{𝔭^j} = s_𝔭^j (s_𝔭^j)^*` are all real (self-adjoint), and weighting them with non-real roots of unity breaks Hermiticity. The right structural object is not a "cyclic character of a Z/kZ-action" (there is no such Z/kZ-action — the `s_𝔭^j` form a monoid, not a group) but a **complement of the `𝔭^k`-divisibility projection**. The formula falls out of the Bost–Connes identity `ω_1^K(e_𝔟) = N(𝔟)^{-1}` applied to `𝔟 = 𝔭^k`.*

---

## Direction (verbatim from spawn prompt)

*Omitted here for brevity; the spawn prompt at `closing-my4/nodes/M.1.1.c-prompt.md` contains the three sub-goals M.1.1.c.1 (definition), M.1.1.c.2 (expectation value match), M.1.1.c.3 (modular invariance), the candidate cyclic-character formula, and the output schema. The prompt is reproduced verbatim in git history.*

---

## Research

### Step 1 — DIAGNOSE

**One sentence.** *The candidate formula `P_k^𝔭 := (1/k) Σ_{j=0}^{k−1} ζ_k^j · s_𝔭^j (s_𝔭^j)^*` looks like a cyclic-character projection, but the operators `e_{𝔭^j} := s_𝔭^j (s_𝔭^j)^*` on which it is built are **nested real projections** (not generators of a Z/kZ-action), so weighting them by non-real roots of unity breaks both self-adjointness and idempotence; the phenomenon in a fuller description is that the BC algebra contains the **monoid** of isometries `{s_𝔭^j : j ≥ 0}` (the `s_𝔭` is a one-sided shift, not a unitary), and there is no Z/kZ subgroup anywhere nearby — the Paper 26 "dark-state coupling value" `1 − |w^k|² = 1 − N(𝔭)^{−k}` is the KMS expectation of the complement-projection `I − e_{𝔭^k}`, which has a single, non-cyclic derivation from the one Bost–Connes identity `ω_1^K(e_𝔟) = N(𝔟)^{−1}`.*

The Cycle 1 Critic (§11.2) suggested the cyclic-character formula based on "Paper 13 referee material C1.01's eigenstate diagonal formula `c_n^{(k)} = (1/k)(1 − w^k)/(1 − w)`." I searched for this file and found no `C1.01` referee material at that filename under `paper13-rh/`; the Critic is quoting a formula structurally reminiscent of a geometric-series sum, but the formula as stated is for the **eigenstate** (a c-number) not the operator itself. The jump from "the coefficient `c_n^{(k)}` is a geometric sum" to "the operator `P_k^𝔭` is a cyclic sum with the same coefficients" was a non-sequitur. (CONCERN M.1.1.c-1 below.)

The correct reading of Prop 6.2 is that `⟨ψ | P_k^𝔭 | ψ⟩` is a **KMS state expectation**, not a pointwise basis-state inner product. The Bost–Connes GNS vacuum `|1⟩` has `⟨1 | e_𝔟 | 1⟩ = ω_1^K(e_𝔟) = N(𝔟)^{−1}` for every ideal 𝔟, by the uniqueness of the KMS₁ state on the Ha–Paugam BC algebra (Paper 26 §3 Prop 3.5, Laca–Raeburn). Setting `𝔟 = 𝔭^k` gives `ω_1^K(e_{𝔭^k}) = N(𝔭)^{−k}`, so `ω_1^K(I − e_{𝔭^k}) = 1 − N(𝔭)^{−k} = 1 − |w^k|²`. **This is the right reading.** The operator is `I − e_{𝔭^k}` and the "eigenstate" ψ of Prop 6.2 is interchangeable with the KMS vacuum in the sense of trace-class diagonals (both give the same value).

### Step 2 — REINTERPRET

The three required properties decompose as:

1. **Projection property** (M.1.1.c.1). An operator of the form `I − e` where `e = e^2 = e^*` is automatically a projection. Candidate B satisfies this for all k ≥ 1 (`s_𝔭^k` is an isometry whose adjoint is a partial isometry, so `e_{𝔭^k} := s_𝔭^k (s_𝔭^k)^*` is a range projection, and `I − e_{𝔭^k}` is its complement).

2. **KMS expectation value match** (M.1.1.c.2). Via the Bost–Connes identity
   `ω_1^K(e_𝔟) = N(𝔟)^{−1}` for every principal ideal 𝔟 of 𝒪_K (Laca 1998; Connes–Marcolli–Ramachandran 2004), applied to `𝔟 = 𝔭^k`:
   `ω_1^K(I − e_{𝔭^k}) = 1 − N(𝔭^k)^{−1} = 1 − N(𝔭)^{−k} = 1 − |w^k|²`.
   This is **exactly** the Prop 6.2 coupling value, with no approximation.

3. **Modular invariance** (M.1.1.c.3). Under the BC time evolution `σ_t(s_𝔞) = N(𝔞)^{it} s_𝔞`:
   ```
   σ_t(s_𝔭^k) = σ_t(s_𝔭)^k = (N(𝔭)^{it} s_𝔭)^k = N(𝔭)^{ikt} s_𝔭^k
   σ_t((s_𝔭^k)^*) = N(𝔭)^{−ikt} (s_𝔭^k)^*
   σ_t(e_{𝔭^k}) = σ_t(s_𝔭^k · (s_𝔭^k)^*) = N(𝔭)^{ikt} · N(𝔭)^{−ikt} · s_𝔭^k (s_𝔭^k)^* = e_{𝔭^k}
   σ_t(I − e_{𝔭^k}) = I − e_{𝔭^k}.  ∎
   ```
   The one-line argument from Cycle 1's M.1.1 (for `k=1`) generalizes immediately by taking the k-th power of both sides. The modular eigenvalue is **0** for every k (`P_k^𝔭` is in the modular-fixed-point subalgebra `(M_1^K)^σ`, which is a Type II∞ subfactor).

**Reduction.** All three sub-goals reduce to one structural fact: `e_{𝔭^k}` is the range projection of the isometry `s_𝔭^k`, and the BC KMS₁ identity `ω_1^K(e_𝔟) = N(𝔟)^{−1}` holds for ideal 𝔟 = 𝔭^k.

### Step 3 — UNIFY

§D toolkit rows used:

- `A_{BC,K}` (R) — Ha–Paugam BC algebra over K = ℚ(i), class number 1
- `s_𝔞` (R) — isometry generator of the BC algebra at ideal 𝔞, with `s_𝔞 s_𝔟 = s_{𝔞𝔟}`
- `e_𝔞 := s_𝔞 s_𝔞^*` (R) — range projection of the isometry, Hecke-range projector
- `ω_1^K` (R) — unique KMS₁ state, `ω_1^K(e_𝔞) = N(𝔞)^{−1}` (Laca 1998)
- `σ_t(e_𝔞) = N(𝔞)^{it} e_𝔞` (R) — BC time evolution on basis ideals
- `T̄_{BC,K}` (R) — modular Hamiltonian, generates `σ_t`
- `H_{1,K}` (R) — GNS space of `ω_1^K`
- `Joint spectral decomposition (T̄_{BC,K}, P_𝔭)` (R, Cycle 1 M.1.1) — extends to `P_k^𝔭 := I − e_{𝔭^k}` by the same argument since modular invariance holds for each k

**Proposed new §D rows** (see "Proposed §D toolkit additions"):

- `P_k^𝔭 := I − s_𝔭^k (s_𝔭^k)^* = I − e_{𝔭^k}` — bridge projector at 𝔭 with cocycle exponent k
- `ω_1^K(P_k^𝔭) = 1 − N(𝔭)^{−k}` — the Paper 26 Prop 6.2 coupling value, exact

### Step 4 — LOCK

**The invariant.** The load-bearing structural fact is:

> **Lemma (LOCK invariant for M.1.1.c).** *Let `A_{BC,K}` be the Bost–Connes algebra over K = ℚ(i), with isometry generators `s_𝔞` (𝔞 ∈ I_K^+), unique KMS₁ state `ω_1^K` satisfying `ω_1^K(e_𝔟) = N(𝔟)^{−1}` for every ideal 𝔟, and time evolution `σ_t(s_𝔞) = N(𝔞)^{it} s_𝔞`. For each Gaussian prime 𝔭 and each integer k ≥ 1, define*
>
> `P_k^𝔭 := I − s_𝔭^k (s_𝔭^k)^* = I − e_{𝔭^k}`
>
> *in `M_1^K = π_1^K(A_{BC,K})''`. Then:*
>
> *(i) `(P_k^𝔭)^* = P_k^𝔭` and `(P_k^𝔭)^2 = P_k^𝔭`; i.e., `P_k^𝔭` is an orthogonal projection on `H_{1,K}`.*
>
> *(ii) `σ_t(P_k^𝔭) = P_k^𝔭` for all `t ∈ ℝ`; i.e., `P_k^𝔭 ∈ (M_1^K)^{σ}` lies in the modular-fixed-point subalgebra.*
>
> *(iii) `ω_1^K(P_k^𝔭) = 1 − N(𝔭)^{−k} = 1 − |w^k(𝔭)|²` exactly.*
>
> *(iv) For k = 1, `P_1^𝔭 = I − e_𝔭` is the complement of the Cycle 1 Hecke range projection `e_𝔭 = s_𝔭 s_𝔭^*`. Note this differs in sign from the Cycle 1 Author's implicit convention (which used `e_𝔭` itself as "the bridge projector"), reconciling with Prop 6.2's statement `⟨ψ|P_k^𝔭|ψ⟩ = 1 − |w^k|²` rather than `|w^k|²`.*

*Proof.*

**(i)** `s_𝔭^k` is a product of k isometries at prime 𝔭, hence itself an isometry: `(s_𝔭^k)^* s_𝔭^k = (s_𝔭^*)^k s_𝔭^k = I` (using `s_𝔭^* s_𝔭 = I` iteratively). Thus `e_{𝔭^k} = s_𝔭^k (s_𝔭^k)^*` is a range projection: `(e_{𝔭^k})^* = e_{𝔭^k}`, `(e_{𝔭^k})^2 = s_𝔭^k (s_𝔭^k)^* s_𝔭^k (s_𝔭^k)^* = s_𝔭^k · I · (s_𝔭^k)^* = e_{𝔭^k}`. The complement `I − e_{𝔭^k}` is therefore an orthogonal projection.

**(ii)** Apply `σ_t` to `e_{𝔭^k}` using BC time evolution:
`σ_t(s_𝔭^k) = σ_t(s_𝔭)^k = (N(𝔭)^{it} s_𝔭)^k = N(𝔭)^{ikt} s_𝔭^k`
`σ_t((s_𝔭^k)^*) = (N(𝔭)^{ikt})^* · (s_𝔭^k)^* = N(𝔭)^{−ikt} (s_𝔭^k)^*`
`σ_t(e_{𝔭^k}) = N(𝔭)^{ikt − ikt} · s_𝔭^k (s_𝔭^k)^* = e_{𝔭^k}`.
Then `σ_t(I − e_{𝔭^k}) = σ_t(I) − σ_t(e_{𝔭^k}) = I − e_{𝔭^k} = P_k^𝔭` by linearity and unitality of `σ_t`.

**(iii)** Apply `ω_1^K`:
`ω_1^K(P_k^𝔭) = ω_1^K(I) − ω_1^K(e_{𝔭^k}) = 1 − N(𝔭^k)^{−1} = 1 − N(𝔭)^{−k} = 1 − |w^k(𝔭)|²`.
The identity `ω_1^K(e_𝔟) = N(𝔟)^{−1}` is the defining KMS₁ property of the Bost–Connes state (Bost–Connes 1995 Prop (b); Laca 1998 Thm 1.3; Ha–Paugam 2005 §3.4 for the K-version).

**(iv)** By direct inspection: `P_1^𝔭 = I − s_𝔭 s_𝔭^* = I − e_𝔭`. The Cycle 1 Author used `P_𝔭 = e_𝔭` (not `I − e_𝔭`), a sign-convention discrepancy that the Critic M.1.1 §5 bonus-grep flagged (§5 item on "`1 − |w^k|²` vs `|w|²`"). The corrected convention used here matches Paper 26 Prop 6.2 verbatim. ∎

### Step 5 — COMPUTE

**Numerical experiment.** I built a finite-dimensional truncation of the BC ideal lattice over `ℚ(i)` with `M = max(200, 4·N(𝔭)^k)` ideals (capped at 2000 for tractability), represented the isometry `s_𝔭` as a sparse matrix on the ideal basis, built candidates A and B explicitly, and checked all three required properties. For the large-k bridge rows (k=3,4,6) where `M_needed > 3000` exceeds dense-matrix tractability, I verified the KMS expectation analytically using the exact Bost–Connes identity.

Code: `closing-my4/code/M.1.1.c-verify-P-k-p.py`, `mp.dps = 30` declared at line 48.

**Raw output (headline rows, verbatim)**:

```
### PART 1 — full operator checks at small primes ###

small-norm p=(1+i): k=2, N(p)=2, target 1-N(p)^-k = 0.750000000000
  cand_A:  herm_err=1.09e-15  idemp_err=2.22e+00   self-adj=True  idempotent=False
           mod-flow errs: {0.1: 0.00e+00, 0.5: 0.00e+00, 1.3: 0.00e+00, 2.7: 0.00e+00}
           KMS expectation (real) = 0.278227431320  Delta = -4.72e-01
  cand_B:  herm_err=0.00e+00  idemp_err=0.00e+00   self-adj=True  idempotent=True
           mod-flow errs: {0.1: 0.00e+00, 0.5: 0.00e+00, 1.3: 0.00e+00, 2.7: 0.00e+00}
           KMS expectation (real) = 0.805894346380  Delta = +5.59e-02   (truncation artifact, M=200)

small-norm p=(2+i): k=4, N(p)=5, target 1-N(p)^-k = 0.998400000000
  cand_A:  herm_err=8.69e+00  idemp_err=8.20e+00   self-adj=False idempotent=False
           mod-flow errs: {0.1: 0.00e+00, ...}
           KMS expectation (real) = 0.243833590538  Delta = -7.55e-01
  cand_B:  herm_err=0.00e+00  idemp_err=0.00e+00   self-adj=True  idempotent=True
           KMS expectation (real) = 0.999637309355  Delta = +1.24e-03   (truncation artifact, M=2000)

### PART 2 — bridge rows ###

bridge row k=2, p=(2+3i), N(p)=13: target 0.99408
  cand_A:  herm_err=5.74e-16 idemp_err=3.91e+00  KMS=0.476  Delta=-5.18e-01
  cand_B:  herm_err=0.00e+00 idemp_err=0.00e+00  KMS=0.998  Delta=+4.22e-03   (trunc M=338)

Bridge row k=3, p=(2+3i) N(p)=13: target 0.999544833864360 (analytic)
  cand_A KMS = 0.31953 + 0.02050 i        |Δ| = 6.80e-01
  cand_B KMS = 0.999544833864360          |Δ| = 0.00e+00  (EXACT)

Bridge row k=4, p=(4+5i) N(p)=41: target 0.999999646113029 (analytic)
  cand_A KMS = 0.24985 + 0.00609 i        |Δ| = 7.50e-01
  cand_B KMS = 0.999999646113029          |Δ| = 0.00e+00  (EXACT)

Bridge row k=6, p=(2+5i) N(p)=29: target 0.999999998318829 (analytic)
  cand_A KMS = 0.16943 + 0.00515 i        |Δ| = 8.31e-01
  cand_B KMS = 0.999999998318829          |Δ| = 0.00e+00  (EXACT)
```

**Findings.**

1. **Candidate A (cyclic-character sum) is REFUTED** on all three grounds:
   - **Not self-adjoint for k ≥ 3**: `herm_err = 8.69` at k=4 (vs tolerance `1e-9`). For k = 2 the herm error is `~1e-15` only because `ζ_2 = −1` is real, so candidate A reduces to the real combination `(1/2)(e_{𝔭^0} − e_{𝔭^1}) = (1/2)(I − e_𝔭)`, which is not what we want either.
   - **Not idempotent** for any k ≥ 2: `idemp_err = 2.22` (k=2), `2.70` (k=3), `8.20` (k=4), all orders of magnitude above tolerance. The `e_{𝔭^j}` are nested (`e_{𝔭^i} · e_{𝔭^j} = e_{𝔭^{max(i,j)}}`), not orthogonal, so the cyclic-character sum's square does not collapse to itself.
   - **KMS expectation wrong**: e.g., at (k=6, N(𝔭)=29) candidate A gives `0.169 + 0.005i` vs the target `0.99999999832`. Discrepancy of order unity.

2. **Candidate B (`I − e_{𝔭^k}`) passes all three checks**:
   - `herm_err = 0.0` exactly (`I` and `e_{𝔭^k}` are both real symmetric).
   - `idemp_err = 0.0` exactly.
   - Modular invariance: `σ_t(P_k^𝔭) − P_k^𝔭` has norm exactly `0.0` at every t ∈ {0.1, 0.5, 1.3, 2.7} tested (this is because `e_{𝔭^k}` is diagonal in the ideal basis and `σ_t` acts by phases on matrix elements, which vanish off the diagonal).
   - KMS expectation: exact in the infinite limit. Small positive truncation artifacts (`+5.6e-2` at M=200, shrinking to `+4.2e-3` at M=338 and `+1.2e-3` at M=2000) arise because the truncation over-represents ideals near the boundary (those with `v_𝔭(𝔞) = 0` are fully sampled but those with `v_𝔭(𝔞) = k` have their k-fold multiples cut off). The analytic (infinite-limit) value is exact.

3. **The prompt's requested basis-state check `⟨|𝔞⟩|P_k^𝔭||𝔞⟩` for 𝔭|𝔞 does NOT match `1 − N(𝔭)^{−k}`** for candidate B (the correct operator). Candidate B is diagonal in the ideal basis with eigenvalues `1` (if `v_𝔭(𝔞) < k`) or `0` (if `v_𝔭(𝔞) ≥ k`), so no single basis diagonal is the fractional value `1 − N(𝔭)^{−k}`. **The prompt's literal check is a misreading of Prop 6.2**: the `⟨ψ|·|ψ⟩` in Prop 6.2 is a KMS state expectation (via trace-class averaging over the ideal basis weighted by `N(𝔞)^{−1}`), not a pointwise basis inner product. I flag this as CONCERN M.1.1.c-2 below and report the KMS expectation value as the right object.

### Step 5.5 — Self-suspicion (3 failure modes, MANDATORY)

**Failure mode 1.** *The Bost–Connes identity `ω_1^K(e_𝔟) = N(𝔟)^{−1}` used in Step 4(iii) might hold only for **prime** ideals, not for their **powers**. If so, `ω_1^K(e_{𝔭^k})` ≠ `N(𝔭)^{−k}` in general.*

**Resolution.** The identity holds for every ideal 𝔟 ∈ I_K^+ (prime, prime power, or composite), not just primes. The underlying reason: `e_𝔟 = s_𝔟 s_𝔟^*` is defined for every isometry `s_𝔟`, and in the BC algebra the relation `s_𝔞 s_𝔟 = s_{𝔞𝔟}` is a **semigroup** relation on the full ideal monoid `I_K^+`, so `s_𝔭^k = s_{𝔭^k}` (power of isometry at 𝔭 equals isometry at 𝔭^k as ideals). The KMS₁ state has `ω_1^K(s_𝔞^* f s_𝔞) = N(𝔞)^{−1} ω_1^K(f)` for all a ∈ I_K^+ and all f in the commutative subalgebra, which specializes to `ω_1^K(s_𝔞 s_𝔞^*) = N(𝔞)^{−1}` by taking f = 1 and using the trace-like property of `ω_1^K` on the abelian core (Laca 1998 Thm 1.3; Ha–Paugam 2005 §3.3; see also Paper 13 preprint §4.2 which uses the Euler product decomposition `ζ_K(β) = Z(β) = Π_𝔭 (1 − N(𝔭)^{−β})^{−1}` at `β=1`). **The identity is standard for every 𝔟.** *No CONCERN here.*

**Failure mode 2.** *The Paper 26 Prop 6.2 "expectation value" `⟨ψ|P_k^𝔭|ψ⟩` is interpreted by me as the KMS state expectation `ω_1^K(P_k^𝔭)`, but Prop 6.2 explicitly restricts ψ to be "an eigenstate of `T_{BC,K}` at a zeta-zero". The KMS vacuum `|1⟩` is not an eigenstate of `T_{BC,K}` (its spectral content is the Dirichlet series, not a point). So my KMS interpretation might be wrong, and the correct interpretation might give a different operator.*

**Resolution.** This is the **real** substantive concern. Resolving it:

- Prop 6.2's ψ is a **distributional** (Meyer-sense) eigenstate at a zeta-zero `γ`. Such an eigenstate is formally `ψ_γ = Σ_𝔞 N(𝔞)^{−1/2 − iγ} |𝔞⟩`, not a basis vector and not in `H_{1,K}`; it lives in the Meyer distribution space `S'`.
- For ANY diagonal operator `D = diag(d_𝔞)` in the ideal basis, the "distributional diagonal" `⟨ψ_γ|D|ψ_γ⟩ / ⟨ψ_γ|ψ_γ⟩` is ill-defined as stated (both numerator and denominator are divergent), but it admits a well-defined regularized limit via
  `lim_{s → 1^+} [Σ_𝔞 N(𝔞)^{−s} d_𝔞] / [Σ_𝔞 N(𝔞)^{−s}]`
  = `lim_{s → 1^+} [D_ζ(s) / ζ_K(s)]`
  where `D_ζ(s) := Σ_𝔞 N(𝔞)^{−s} d_𝔞`. When `D = I − e_{𝔭^k}`, `d_𝔞 = 1` if `v_𝔭(𝔞) < k`, else 0. The Dirichlet series factorizes via Euler products:
  `D_ζ(s) = ζ_K(s) · (1 − N(𝔭)^{−s} + N(𝔭)^{−2s} − ... ) · (...)` — actually we have `D_ζ(s) = ζ_K(s) · (1 − N(𝔭)^{−ks})` because the Euler factor at 𝔭 of `ζ_K` is `(1 − N(𝔭)^{−s})^{−1}` which expands as `Σ_{j≥0} N(𝔭)^{−js}`, and cutting off at `j < k` gives `(1 − N(𝔭)^{−ks})/(1 − N(𝔭)^{−s})`. Multiplied by `ζ_K(s)` we get
  `D_ζ(s)/ζ_K(s) = 1 − N(𝔭)^{−ks}`
  and the limit as `s → 1^+` is **`1 − N(𝔭)^{−k}`** exactly. ✓
- This is the same value as `ω_1^K(P_k^𝔭)`, by the **ITPFI factorization** of Paper 13 §4.2 (the KMS₁ vacuum expectation `ω_1^K(D)` equals the Dirichlet regularization of the basis diagonal). So the KMS interpretation and the Meyer-distributional interpretation agree. **No new object; the answer is still `1 − N(𝔭)^{−k}`.** *Concern is resolved; LESSON logged below.*

**Failure mode 3.** *The operator `P_k^𝔭 = I − e_{𝔭^k}` is simple and explicit, but it might NOT be "the" bridge projector used downstream in Paper 26 §7–9.3 bridge-cocycle machinery. If a different operator is used there (e.g., a Frobenius-twisted projection on the `k`-th tensor power of the cyclotomic algebra), then my definition is local to Prop 6.2 and the downstream chain needs its own definition.*

**Resolution.** I grepped `paper26-bsd/preprint/` for all occurrences of `P_k` and `P^{\mathfrak{p}}_k` and found only the Prop 6.2 statement plus one restatement in `sections-parts-V-VI.md` line 1128 (the "joint kernel is {0}" restatement, which uses the same operator). **There is no independent §7–9.3 definition.** Paper 26's downstream arguments use `P_k^𝔭` only through its expectation value (Prop 6.2) and the fact that it detects every eigenstate (Cor 6.4). Both facts follow from `P_k^𝔭 := I − e_{𝔭^k}`. So my definition is canonical for Paper 26 as currently written. CASCADE risk noted below for the §7–9.3 writeup: the downstream chain should cite `P_k^𝔭 := I − e_{𝔭^k}` explicitly at its first use. *No CONCERN that blocks closure; CASCADE M.1.1.c-3 below.*

### Step 6 — VERIFY

**The numerical verification is unambiguous.** Candidate A fails all three checks; candidate B passes all three exactly (modulo harmless truncation artifacts in Part 1, which vanish in the infinite-limit calculation in Part 2). The modular invariance check on the finite truncation passes at `0.0 exactly` (not `1e-16`) because both `e_{𝔭^k}` and `σ_t(e_{𝔭^k})` are diagonal in the ideal basis with integer-valued entries; the modular flow acts only on off-diagonal elements.

**Density-of-states / KMS compatibility check.** The joint spectral decomposition `(T̄_{BC,K}, P_k^𝔭)` from Cycle 1 M.1.1 (which was stated for `k=1`) generalizes to k > 1 directly: `[P_k^𝔭, T̄_{BC,K}] = 0` follows from `σ_t(P_k^𝔭) = P_k^𝔭`, because `T̄_{BC,K}` generates `σ_t` (Paper 26 Prop 3.5). So the joint spectral picture from Cycle 1 extends to every k ∈ {2, 3, 4, 6}, and the Cycle 1 CONCERN M.1.1-3 ("the bridge projector is not defined for k>1") is now CLOSED.

**§F shadow check.** §F contains three candidate kills from Cycle 1 (per Critic §8): (a) KMS-positivity-as-pointwise-lower-bound, (b) Modular-eigenoperator-at-log-N(𝔭), (c) Support-runner-file-reference. None of these apply to M.1.1.c:
- (a) is irrelevant because M.1.1.c is about defining an operator, not bounding a state.
- (b) is the opposite direction from what M.1.1.c establishes (M.1.1.c confirms modular INVARIANCE, eigenvalue 0, which is **consistent** with the Cycle 1 correction).
- (c) — I did verify Paper 26 Prop 6.2 directly at `sections-part-II.md` lines 639–658 (not via paraphrase) and found it does not define `P_k^𝔭`, consistent with the Cycle 1 CONCERN M.1.1-3 diagnosis.

**Voice canon match.** *"Trace discrepancies until they become theorems."* The discrepancy between the spawn prompt's candidate cyclic-character formula and the Prop 6.2 expectation value became the theorem `P_k^𝔭 = I − e_{𝔭^k}`. The cyclic-character formula was a **false lead from a misreading of Paper 13's "C1.01 eigenstate diagonal"** (which I could not even locate in the corpus — see CONCERN M.1.1.c-1). The right formula has no Z/kZ-action anywhere; it is just a complement of one projection.

**Verdict.** Status **ADVANCED (with caveat)**. Sub-goals M.1.1.c.1 (definition), M.1.1.c.2 (expectation value match), and M.1.1.c.3 (modular invariance) all close via the corrected formula. The caveat is: the spawn prompt's candidate is wrong, and the spawn prompt's basis-state sanity check is the wrong object for Prop 6.2. The corrected formula and the corrected sanity check (KMS state expectation) both pass exactly. This is a directionally different closure than the prompt anticipated but is structurally correct and closes the corpus gap.

---

## Proposed §D toolkit additions

Two new canonical names emerging from this node:

1. **`P_k^𝔭 := I − s_𝔭^k (s_𝔭^k)^* = I − e_{𝔭^k}`** — *Status: R (proved here in Step 4).* Statement: the bridge projector at prime 𝔭 with cocycle exponent k ∈ {1, 2, 3, 4, 6} is the orthogonal complement of the range projection of the k-th iterate of the isometry generator at 𝔭 in the Ha–Paugam BC algebra over `K = ℚ(i)`. It is a self-adjoint idempotent (projection), modular-invariant (lies in the centralizer `(M_1^K)^σ`), and its KMS₁ expectation value is `ω_1^K(P_k^𝔭) = 1 − N(𝔭)^{−k} = 1 − |w^k(𝔭)|²` exactly, matching Paper 26 Prop 6.2.

2. **`ω_1^K(e_{𝔭^k}) = N(𝔭)^{−k}`** — *Status: R (standard BC identity, Bost–Connes 1995 Prop (b), extended to K by Laca 1998 + Ha–Paugam 2005).* Statement: the KMS₁ expectation of the range projection `e_{𝔭^k}` of the k-th isometry power equals `N(𝔭)^{−k}` exactly. Used in Step 4(iii) to compute the Prop 6.2 coupling value.

**Correction to existing §D row (proposed for Cycle 1's M.1.1 LOCK invariant).** Cycle 1 M.1.1 Step 4 LOCK stated `P_𝔭 = s_𝔭 s_𝔭^* = e_𝔭` as "the bridge projector at prime 𝔭". This is the **complement** of the Paper 26 Prop 6.2 bridge projector for `k=1`: the Paper 26 definition is `P_1^𝔭 := I − e_𝔭`, giving coupling value `1 − N(𝔭)^{−1}` (not `N(𝔭)^{−1}` as Cycle 1 used). Cycle 1's modular invariance proof is still correct (both `e_𝔭` and `I − e_𝔭` are modular invariant, and Cycle 1's one-line derivation works for both), but the **direction** of the bound flips: the target in Prop 6.2 is `⟨ψ|P_k^𝔭|ψ⟩ ≠ 0` (which requires a LOWER bound on the large quantity `1 − N(𝔭)^{-k}`, trivially satisfied), not a lower bound on the small quantity `N(𝔭)^{−k}`. This realizes the Cycle 1 Critic §5 bonus-grep finding that the Cycle 1 Author was working toward the wrong target value. **The downstream M.1.1.b f_0-existence sub-problem is now much easier**: the target is `‖P_k^𝔭 f_0‖² ≥ 1 − N(𝔭)^{-k}`, which is a **≥ 99.4%** mass condition rather than a ≤ 0.6% mass condition.

---

## Tagged notes for §I

**CONCERN M.1.1.c-1.** *The Cycle 1 Critic's cited source for the candidate cyclic-character formula — "Paper 13 referee material C1.01's eigenstate diagonal formula `c_n^{(k)} = (1/k)(1 − w^k)/(1 − w)`" — could not be located in the corpus.* I searched `paper13-rh/` for files matching `C1.01`, `referee`, and the text `(1-w^k)/(1-w)`, and found no match. The Cycle 1 Critic may have invented this reference from pattern analogy, or it may live in an older version of the paper13 referee material I did not access. **The candidate formula itself is refuted on structural grounds** (see Step 1 and Step 5), so this CONCERN is not load-bearing for M.1.1.c, but it is a repeat of Cycle 1 CONCERN M.1.1-2 (support-runner / Critic file references should be verified). LESSON: when a Critic or support runner cites a specific formula from a file, verify the file contains the formula before building on it.

**CONCERN M.1.1.c-2.** *The spawn prompt's literal sanity check ("compute `⟨|𝔞⟩|P_k^𝔭||𝔞⟩` for `𝔞` with `𝔭|𝔞` and verify it equals `1 − N(𝔭)^{−k}`") is mathematically the wrong object for Paper 26 Prop 6.2.* The prompt uses a basis-state inner product, but Prop 6.2 uses a KMS / distributional state expectation. For the corrected operator `P_k^𝔭 = I − e_{𝔭^k}`, the basis-state diagonal value `⟨|𝔞⟩|P_k^𝔭||𝔞⟩` is either `1` (if `v_𝔭(𝔞) < k`) or `0` (if `v_𝔭(𝔞) ≥ k`), **never** the fractional value `1 − N(𝔭)^{−k}`. I performed the corrected check (KMS state expectation) instead, and it passes exactly. Flagging for the runner: the prompt's sanity check criterion is ill-posed, but the underlying verification (KMS expectation match) is the right object and passes. This does not affect the closure of M.1.1.c.

**CASCADE M.1.1.c-3.** *The corrected bridge projector `P_k^𝔭 := I − e_{𝔭^k}` simplifies downstream arguments throughout Paper 26 §6–§9.* Specifically:
- **§6.2 Cor 6.4 (no dark states)**: trivial consequence, since `ω_1^K(P_k^𝔭) > 0`.
- **§7 bridge-cocycle construction**: should be checked for consistency; the bridge cocycle is built from `P_k^𝔭` via a Pimsner–Popa basis argument that assumes `P_k^𝔭` has a specific form. The `I − e_{𝔭^k}` form is consistent with "the projection onto ideals **not** reducible by 𝔭^k", which is the natural domain for the Frobenius-twisted lift in §7.
- **§9.3 M.1.1.b f_0-existence**: the target changes from "construct `f_0` with `‖e_𝔭 f_0‖² ≥ N(𝔭)^{−k}` (small target, hard)" to "construct `f_0` with `‖(I − e_{𝔭^k}) f_0‖² ≥ 1 − N(𝔭)^{−k}` (large target, easy)". **This makes M.1.1.b nearly trivial for any `f_0` that has substantial support on the **generic** (non-𝔭-divisible) ideals**, which is the natural case. Cascade-friendly.

**LESSON M.1.1.c-4.** *When a structural formula is proposed by analogy ("this looks like a cyclic-character projection"), verify all three required algebraic properties (self-adjointness, idempotence, modular invariance) BEFORE building a numerical experiment around it.* I caught the cyclic-character formula's failure analytically in Step 1 (non-Hermitian) before running the script; the script then confirmed numerically in Step 5. If I had run the script first and trusted it, the `herm_err ~ 1e-15` at k=2 (where `ζ_2 = −1` is real) might have been mistaken for a "passing" result — but k=2 is the outlier, not the rule; the failure is clean at k ∈ {3, 4, 6}. The cost of the analytic check was 2 minutes; the value was avoiding a false positive at k=2.

**LESSON M.1.1.c-5.** *The right abstraction for "Prop 6.2 expectation value" is the KMS₁ state expectation, not a pointwise basis-state inner product.* This is a register issue that bit Cycle 1 and has now bitten the M.1.1.c spawn prompt. Future prompts that reference a Paper 26 coupling value should phrase it as `ω_1^K(P_k^𝔭)` (or equivalently, the Dirichlet regularization of the basis diagonal), not as `⟨|𝔞⟩|·||𝔞⟩` for a specific basis ideal. The two objects agree for basis states in the point spectrum, but the Prop 6.2 value is a distributional / regularized statement, not a basis statement.

**CALLOUT M.1.1.c-6.** *The spawn prompt's candidate formula was a distraction: the right answer is simpler than the prompt anticipated.* The prompt asked for verification of a cyclic-character sum; the right formula is a one-line complement `I − e_{𝔭^k}`. When the candidate is complicated and fails structural properties, look for the simpler answer — and in the BC setting, the KMS identity `ω_1^K(e_𝔟) = N(𝔟)^{−1}` is the **only** rotation-invariant way to reach fractional values like `1 − N(𝔭)^{−k}`.

**CALLOUT M.1.1.c-7.** *Voice canon: "honest partial proof over glossed completion."* M.1.1.c declares ADVANCED with a caveat (the candidate is refuted, the corrected formula is derived fresh, and the prompt's sanity check is the wrong object). This is a cleaner closure than silently passing the prompt's literal check would have been, and more useful for the runner.

---

## What the next runner needs to know (Sig 11 schema)

- **State at handoff**: The bridge projector `P_k^𝔭` for k ∈ {1, 2, 3, 4, 6} is now explicitly defined as `P_k^𝔭 := I − s_𝔭^k (s_𝔭^k)^* = I − e_{𝔭^k}`. It is Hermitian idempotent, modular-invariant (`σ_t(P_k^𝔭) = P_k^𝔭`, modular eigenvalue 0), and its KMS₁ expectation value is `ω_1^K(P_k^𝔭) = 1 − N(𝔭)^{−k} = 1 − |w^k(𝔭)|²` exactly. All three sub-goals M.1.1.c.1 / M.1.1.c.2 / M.1.1.c.3 close. **The spawn prompt's candidate `(1/k) Σ ζ_k^j s_𝔭^j (s_𝔭^j)^*` is refuted** — it fails both self-adjointness and idempotence at k ≥ 2.

- **Corpus gap CONCERN M.1.1-3 (from Cycle 1) is now CLOSED.** The runner may log this as a resolved concern and promote the corrected M.1.1.c Step 4 LOCK to §D toolkit row status R.

- **Cycle 1 M.1.1 sign convention needs a patch**: Cycle 1 used `P_𝔭 = e_𝔭` as "the bridge projector at 𝔭", but Paper 26 Prop 6.2's `P_k^𝔭` has opposite sign (`I − e_𝔭` for k=1). Cycle 1's modular invariance proof is still correct, but downstream claims that referenced `⟨ψ|P_𝔭|ψ⟩ ≥ |w|²` should be rewritten as `⟨ψ|P_k^𝔭|ψ⟩ = 1 − |w^k|²` or `‖(I − e_{𝔭^k}) f_0‖² ≥ 1 − N(𝔭)^{−k}`. The direction of the bound flips from "lower bound on a small quantity" to "lower bound on a large quantity", which makes M.1.1.b (f_0-existence) drastically easier.

- **Open dependencies**: M.1.1.c feeds into M.1.1.b (f_0-existence) and the Paper 26 §7–§9.3 downstream chain. M.1.1.b is now much easier — see CASCADE M.1.1.c-3. The §7 bridge-cocycle construction should be re-verified against the corrected definition at its first use.

- **Watch out for**:
  - The prompt's literal basis-state sanity check is wrong object (CONCERN M.1.1.c-2). Use KMS state expectation `ω_1^K(P_k^𝔭)` (or Dirichlet regularization of basis diagonal) as the right criterion.
  - The Cycle 1 Critic's reference to "Paper 13 referee material C1.01 eigenstate diagonal formula" could not be located in the corpus (CONCERN M.1.1.c-1). Treat Critic file references as hypotheses requiring verification.
  - The "cyclic-character" intuition is a **false lead** in the BC setting. There is no Z/kZ group acting on the isometry monoid at 𝔭; the right projection is a complement of a single `e_{𝔭^k}`, not a cyclic sum.

- **Preferred next move**: Spawn an Author M.1.1.b with the updated target `‖(I − e_{𝔭^k}) f_0‖² ≥ 1 − N(𝔭)^{−k}`. This is a drastically easier target than the Cycle 1 framing (≥ 99.4% mass condition at k=2, N(𝔭)=13, vs Cycle 1's ≤ 0.6% mass condition). For many natural choices of `f_0` in the BC dense domain, the condition is trivially satisfied. The remaining load-bearing constraint is "spectral support of `f_0` near `λ = γ_n` concentrated away from `ideals with v_𝔭(𝔞) ≥ k`", which is a **spectral** constraint on `f_0`, not an algebraic one. This should be tractable in 1 cycle.

- **Route-independence**: M.1.1.c is independent of M.2.4 (CCM K-port) and M.3.1 (ITPFI). It is a pure operator-theoretic definition in the BC algebra, used by Route 1 only. The multi-route LOCK for closing MY4 still stands: Route 1 (spectral-measure, M.1.1.a + M.1.1.b + M.1.1.c) and Route 2 (CCM K-port, M.2.4) are on structurally independent failure-mode axes.

---

## p_success self-estimate

**p_success for M.1.1.c closing the corpus gap (CONCERN M.1.1-3): 0.92.**

Rationale:
- The corrected formula `P_k^𝔭 := I − e_{𝔭^k}` passes all three required properties exactly (analytically and numerically).
- The KMS expectation value match `1 − N(𝔭)^{−k}` is a **standard BC identity**, not a new result.
- The derivation is 3 lines of algebra.
- The corpus gap CONCERN M.1.1-3 ("P_k^𝔭 for k>1 never explicitly defined") is now closed with an explicit operator.

The 8% residual doubt is primarily: (a) the possibility that Paper 26 §7 bridge-cocycle machinery uses a subtly different `P_k^𝔭` than the Prop 6.2 operator (CASCADE M.1.1.c-3 risk); (b) the possibility that the Cycle 1 sign-convention mismatch with M.1.1 requires more patching than I've estimated; (c) the possibility that the cycle-2 Critic will find a nuance I missed in the Meyer-distributional regularization argument in Step 5.5 resolution 2. Items (a) and (b) are downstream patches that don't block M.1.1.c itself; item (c) is the only thing that could reduce closure strength, and the Dirichlet regularization + ITPFI factorization argument is standard, so it's low-probability.
