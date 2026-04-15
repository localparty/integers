# Route 2 — Porting Paper 13's CCM + ITPFI + Bögli + Hurwitz to K

*Instrumentation plan for closing MY4 (the classical Meyer–Nelson wall)
via the Connes–Consani–Moscovici architecture over imaginary quadratic
K with class number 1.*
*Written 2026-04-10. Updated 2026-04-10 with literature survey results,
the Weil-form-over-K writeup, and the negative numerical experiment.*

## Update log (2026-04-10, second pass)

After the initial instrumentation, four follow-on tasks were run in
parallel and informed the plan:

1. **Literature survey** (broad scan + Sagnier deep-dive). The key
   finding for Route 2:

   - **Sagnier 2017, arXiv:1703.10521** ("An arithmetic site of
     Connes–Consani type for imaginary quadratic fields with class
     number 1") + **Sagnier 2019**, *J. Number Theory* (with
     appendix by Connes), "An arithmetic site at the complex place"
     — explicitly constructs the Connes–Consani arithmetic *site*
     (a topos-theoretic object) for the nine class-number-1
     imaginary quadratic fields, including `K = ℚ(i)`. The set of
     points is identified with a quotient of the adèle class space
     `A_K/K^×`, mirroring the Connes–Consani picture over ℚ.
   - Sagnier's spectral interpretation is **adelic /
     distributional** (in the Connes 1999 sense — traces on the
     adèle class space recasting Weil's explicit formula), **not**
     via a concrete Hilbert-space operator. He defines no Bost–
     Connes-type operator over K, no Weil quadratic form `Q_N^K`,
     no spectral triple for `ζ_K`, and no spectral triple for Hecke
     L-functions. (His point count *does* see Hecke L-functions
     with archimedean ramification, so Grössencharacters of infinity
     type are in scope at the topological level.)
   - **CCM 2025 (arXiv:2511.22755)** does NOT cite Sagnier and is
     strictly over ℚ. A grep for "Sagnier", "imaginary quadratic",
     "Q(i)", "Gaussian", "number field", "Dedekind", "Hecke",
     "Grössencharacter" in CCM 2025 returns zero hits.
   - The **bridge from Sagnier's topos / adèle picture to a CCM-style
     Hilbert space picture** — the core of our Route 2 — has **not
     been built in the literature**. Sub-tasks 1.1, 1.2, 1.5, and
     Phase IV of this plan are yours to invent, with no
     wheel-reinvention risk.

   **Useful for Route 2:** Sagnier's adelic point count of his
   K-arithmetic site is a legitimate, peer-reviewed **target** that
   the spectrum of `D_∞^K` ought to reproduce — use it as a
   cross-check. His handling of archimedean-ramified Hecke L-functions
   tells us that Grössencharacters of infinity type are the right
   twist family for the BSD chain.

   Other relevant items:
   - **Ha–Paugam 2005, arXiv:math/0507101** — the BC algebra
     `A_{BC,K}` over number fields. Already used in Paper 26 §3.1.
   - **Laca–Neshveyev–Trifković 2013, arXiv:1010.4766** — for K
     with narrow class number 1 (which includes `ℚ(i)`), the BC
     system is a full corner of an inducted Hecke algebra. Useful
     when establishing the K-Borchers / K-Laca–Raeburn structure
     for sub-task 1.3.
   - **Connes–Marcolli, *Noncommutative Geometry, Quantum Fields
     and Motives*** (AMS, 2008), §4–5 — general framework. The
     twisted spectral realization for L(s, ψ) over **ℚ** in §4.3
     is the template for our `meyer-extension-to-K.md` Key Lemma
     B.
   - **Simons–Wang 2011** (GEM J., "Spatiospectral concentration in
     the Cartesian plane") — 2D Slepian functions in `ℝ²`. The
     closest existing thing to ℂ-prolate wave functions, but lacks
     complex-analytic / holomorphic structure. The "first `N`
     Gaussian primes + prolate cutoff" of sub-task 1.1 has no
     literature precedent.

   **Verdict:** Sagnier gives us an arithmetic/topological skeleton
   to be consistent with, but every operator-level piece is to be
   built fresh.

2. **Weil form Q_N^K written out** in `weil-form-over-K.md` (sub-task
   1.2 below, executed). Five open issues identified, the two most
   important being:
   - **(O1)** the **same-norm collision in the off-diagonal** is a
     genuinely new K-issue with no ℚ analogue. The kernel
     `1/log(N(𝔟)/N(𝔞))` diverges for distinct ideals of equal norm
     (first at the split pair `(1+2i), (1−2i)` of norm 5).
     Recommended handling (Option A): drop same-norm pairs; the
     diagonal Mangoldt kernel already separates split partners.
   - **(O2)** the **exact form of the complex-place archimedean
     term** `τ^{(K_∞)}` needs to be pinned down against Weil 1952 §III
     or Iwaniec–Kowalski Theorem 5.12 — `meyer-extension-to-K.md` and
     `weil-form-over-K.md` differ by an `s ↦ s + 1/2` shift in the
     digamma argument.

3. **First numerical D_N^K experiment** (`first_D_N_K.py`,
   `first_D_N_K_log.md`). **Negative result, with diagnosis:** a crude
   "log-ratio kernel + Mangoldt diagonal" matrix produces no signal
   (eigenvalues all in `|λ| < 1`, far from `γ_1^K ≈ 14.13`). Critically,
   **the same crude recipe applied to ℚ also fails** (best `δ ≈ 13.4`
   from `γ_1 = 14.13`), so the failure is *intrinsic to the toy
   construction*, not a porting bug. **Diagnosis:** the missing
   ingredient is the **bandwidth parameter `λ`** that scales Paper 13's
   operator (`‖T_0‖ ~ λ` per §6.2) and the **genuine prolate basis** of
   CCM 2025. **Lesson:** any numerical verification of Phase I has to
   go through (a) reproducing CCM 2025's 55-digit ℚ result first, and
   (b) building a real ℂ-prolate basis for K — there is no shortcut.

These three findings are integrated into the layer-by-layer plan below.

## The task

Paper 13 proves the Riemann Hypothesis conditional on CCM by stacking
six layers:

```
  Layer 1   CCM operators D_N on E_N^+                         (over ℚ)
  Layer 2   ITPFI factorization  ω_1 = ⊗_p ω_1^{(p)}            (over ℚ)
  Layer 3   Archimedean + Sobolev + CF estimates                (over ℚ)
  Layer 4   Teschl form bound → Bögli spectral exactness        (abstract)
  Layer 5   Hurwitz → spec(D_∞) = {zeros of Ξ}                  (over ℚ)
  Layer 6   Assembly: zeros of Ξ are real ⇒ RH                  (over ℚ)
```

Route 2 ports this stack from ℚ to `K = ℚ(i)` (and by §9.3-style
extension, to all nine class-number-1 imaginary quadratic fields),
yielding

```
  Theorem (target).  spec(D_∞^K) = {non-trivial zeros of Ξ_K(z)}
                     ⊂ ℝ, hence GRH for ζ_K.
```

and, with the Hecke-character twist of §9 below, GRH for
`L(s, ψ)` for every Hecke Grössencharacter `ψ` of `K`. This closes
MY4 and with it the last `[KEY LEMMA — OPEN]` item in the rigor
audit.

## What's already done in Paper 26 (no porting needed)

The following structures are already in the preprint and are
validated by the rigor audit:

| Ingredient | Paper 26 ref | Rigor label | Source |
|:-----------|:-------------|:------------|:-------|
| BC algebra `A_{BC,K}` | §3.1, Def. 3.1 | [THEOREM] (BC1) | Ha–Paugam 2005 |
| Unique KMS₁ state `ω_1^K` | §3.4, Prop. 3.4 | [LEMMA] (BC2) | Ha–Paugam + LLN 2015 |
| GNS Hilbert space `H_{1,K}`, type III₁ | §3.5 | [THEOREM] (BC3) | Takesaki |
| `T_{BC,K}` densely defined | §3.5 | [LEMMA] (BC4) | standard |
| Nelson self-adjointness of `T_{BC,K}` | §3.7, Prop. 3.7 | [THEOREM] (BC5) | Reed–Simon X.39 |
| ITPFI factorization `ω_1^K = ⊗_𝔭 ω_1^𝔭` | §5, Prop. 5.1 | [LEMMA] (IT1) | Laca–Raeburn + BR 5.3.23 |
| Factorization → prime-by-prime cocycle shift | §5 | [LEMMA] (IT2) | inherited |

**This is Layer 2 in full, plus the GNS/modular ingredients that feed
Layer 1.** Route 2 therefore begins at Layer 1 (the CCM operators) and
continues through Layers 3–6.

## The porting plan

### Phase I — Layer 1: CCM spectral triples over K

**Goal.** Construct a sequence of finite-dimensional Hilbert spaces
`E_N^{+,K}`, a Weil-type quadratic form `Q_N^K`, and a self-adjoint
operator `D_N^K` such that

```
  spec(D_N^K)   approximates   { Im(ρ) : ρ is a non-trivial zero of ζ_K }
```

to precision `O(ρ^{−N})` for some CF decay base `ρ > 1`.

#### Sub-task 1.1. The ambient Hilbert space

**Paper 13 (over ℚ).** Ambient space `L²(ℝ)`. The truncation `E_N ⊂
L²(ℝ)` is spanned by prolate spheroidal wave functions determined by
the first `N` rational primes `{2, 3, …, P_N}`.

**K-analogue.** Ambient space `L²(K_∞) = L²(ℂ)` (one complex place,
since `K = ℚ(i)`). The truncation `E_N^K ⊂ L²(ℂ)` is spanned by
`ℂ`-valued prolate analogues determined by the first `N` Gaussian
prime ideals, ordered by norm.

**Concrete construction.**

1. Enumerate Gaussian primes by norm:
   `𝔭_1 = (1+i), 𝔭_2 = (1+i), 𝔭_3 = (2+i), 𝔭_4 = (2−i), 𝔭_5 = (3),
   𝔭_6 = (3+2i), 𝔭_7 = (3−2i), …`
   (multiplicity handles split pairs correctly).
2. Define the `N`-smooth integers of `𝒪_K`:
   `S_N^K = { 𝔞 ⊂ 𝒪_K : 𝔭 | 𝔞 ⇒ N(𝔭) ≤ Q_N }`, where `Q_N` is the
   norm of the `N`-th Gaussian prime in the ordering.
3. For each `𝔞 ∈ S_N^K`, define a basis vector
   `e_𝔞 ∈ L²(ℂ)` by

   ```
   e_𝔞(z) = N(𝔞)^{−1/2} · exp(2πi · (Tr_{K/ℚ}(z · x_𝔞) / L))
   ```

   where `x_𝔞` is a canonical representative of `𝔞` in `K_∞ = ℂ`
   under the embedding `K ↪ ℂ`, and `L` is a length parameter
   analogous to Paper 13's `L = 2 log(λ_bw)`.

4. `E_N^{+,K}` is the even sector (fixed by the parity involution
   `z ↦ −z` on `ℂ`; see sub-task 1.4).

**Status.** Mechanical in structure but each line needs to be written
out. The key question is whether the prolate-wave-function framework
carries over; the answer should be yes because the prolate waves are a
general property of band-limited functions on any locally compact
abelian group, and `K_∞ = ℂ` is such a group.

**Dependency.** Slepian–Pollack 1961 theory of prolate waves on ℝ.
For ℂ ≅ ℝ², **Simons–Wang 2011** (GEM J., "Spatiospectral
concentration in the Cartesian plane") solves the Slepian
concentration problem in the Cartesian plane and gives 2D Slepian
functions. This is the closest existing literature, but it does NOT
include the holomorphic / complex-analytic structure that ℂ as the
infinite place of `K` would naturally inherit. Kaiser 1994 ("A
Friendly Guide to Wavelets," chapters on 2D analytic signals) is the
closest analytic-signal version. **The "first `N` Gaussian primes
+ prolate cutoff" truncation does not exist in the literature** —
this is the genuinely new piece.

**Lesson from the negative numerical experiment** (`first_D_N_K.py`):
the **bandwidth parameter `λ`** that scales `L = 2 log(λ_bw)` is
load-bearing. Without it, the matrix entries live on `O(1)` scale
and the spectrum is bounded by `O(1)` — far from `γ_1^K ≈ 14.13`.
A first sanity check at this sub-task should fix `λ` at order
`exp(γ_1^K / 2) ≈ 1100`, giving `L ≈ 14.13`, and verify that the
operator norm scales linearly with `λ` as Paper 13 §6.2 promises.

#### Sub-task 1.2. The Weil quadratic form over K

**Paper 13 (over ℚ).**

```
  Q_N(f, g)  =  ∑_{m,n ∈ S_N, m ≠ n}  ⟨f, e_m⟩ ⟨e_n, g⟩ / log(n/m)
                + (diagonal terms)
```

where the diagonal terms come from the ℚ explicit formula.

**K-analogue.**

```
  Q_N^K(f, g)  =  ∑_{𝔞, 𝔟 ∈ S_N^K, 𝔞 ≠ 𝔟}
                  ⟨f, e_𝔞⟩ ⟨e_𝔟, g⟩ / log(N(𝔟)/N(𝔞))
                  + (diagonal terms from ζ_K explicit formula)
```

The diagonal terms come from the Dedekind–Mangoldt function
`Λ_K(𝔞)`, and the archimedean contribution (one complex place)
replaces the `Γ(s/2)` contribution of the rational case with a
`Γ(s)` contribution from the complex place of `K`.

**Status.** **DONE** — see `weil-form-over-K.md` for the full
writeup (~500 lines). Off-diagonal, diagonal Mangoldt, archimedean
`τ^{(K_∞)}`, rank-2 condensation `τ^{(0,2),K}`, parity `γ_K`, and
Hermitian sanity check are all defined. The note flags five open
issues; the two most important are:

- **(O1) Same-norm collisions in the off-diagonal.** A genuinely
  new K-issue with no ℚ analogue: distinct same-norm ideals (e.g.,
  the split pair `(1+2i), (1−2i)` of norm 5) make
  `1/log(N(𝔟)/N(𝔞))` undefined. Recommended Option A: drop
  same-norm pairs from the off-diagonal sum. Justification: the
  diagonal Mangoldt kernel `Λ_K(𝔞)/√N(𝔞)` already separates split
  partners. **Verification deferred** to either a careful (M3')
  read or a small-N numerical experiment.
- **(O2) Exact form of `τ^{(K_∞)}`.** The complex-place archimedean
  contribution involves `ψ(α + iu) + ψ(α − iu) − 2 log(2π)` for
  some `α`; `meyer-extension-to-K.md` and `weil-form-over-K.md`
  differ by an `s ↦ s + 1/2` shift in `α`. To pin down: consult
  Weil 1952 §III or Iwaniec–Kowalski Theorem 5.12.

For the rank-2 condensation `τ^{(0,2),K}`: the `(1/2)·s(s−1)`
prefactor is field-independent (rank still 2). For `K = ℚ(i)`, the
two residue weights work out to **±1/2 exactly** (matching the ℚ
case by coincidence: `Res_{s=1} Λ_K = 1/2` from `κ_K = π/4`,
`Res_{s=0} Λ_K = −1/2` from `ζ_K(0) = −1/4`). For other class-
number-1 fields the weights shift but the rank-2 structure is
preserved — **(O3)** open issue: tabulate residues for the other
eight fields when extending §9.3-style.

#### Sub-task 1.3. Self-adjointness via Carathéodory–Fejér over K

**Paper 13.** Self-adjointness of `D_N` on `E_N^+` follows from CCM
2025 Theorem 4.2, which applies Carathéodory–Fejér theory to the
moment problem on the Bernstein ellipse.

**K-analogue.** The Carathéodory–Fejér framework is complex-analytic
and does not depend on the base field. What depends on the base field
is the **moment problem**: the moments are `∫ u^n dμ(u)` where `μ` is
the spectral measure of the Weil form. Over ℚ, the moments come from
sums over primes `p` weighted by `log(p)/√p`. Over `K`, they come from
sums over Gaussian primes weighted by `log(N(𝔭))/√N(𝔭)`.

**Task.** Verify that the K-version of the moment problem still
satisfies the positive-definiteness condition required for the CF
existence theorem. This should be a direct consequence of the
positivity of the Dedekind–Mangoldt function, but needs to be
written out.

**Status.** Straightforward once the Weil form is defined.

#### Sub-task 1.4. Even-sector compatibility

**Paper 13.** Parity `f(x) ↦ f(−x)` on `L²(ℝ)`, with the Weil matrix
commuting with `γ: V_j ↦ V_{−j}` (CCM Lemma 5.2(i)). The even sector
`E_N^+` captures the Riemann zeros because `Ξ(s)` is even about
`s = 1/2`.

**K-analogue.** The completed Dedekind zeta

```
  Ξ_K(s) = (1/2) s(s−1) · Λ_K(s)
```

is also even about `s = 1/2` (follows from `Λ_K(s) = Λ_K(1 − s)`
and the factor `s(s−1)` being invariant under `s ↦ 1 − s`). The
parity involution on `ℂ` is `z ↦ −z`. The Weil form `Q_N^K` should
commute with this parity by the same functional-equation argument as
the ℚ case.

**Task.** Verify the commutation `Q_N^K γ_K = γ_K Q_N^K`, where
`γ_K: V_{𝔞} ↦ V_{\bar{𝔞}}` or `V_{-𝔞}` (depending on how ideal
representatives are chosen under the `K ↪ ℂ` embedding).

**Status.** Structural; the functional equation `Λ_K(s) = Λ_K(1−s)`
is classical.

#### Sub-task 1.5. Eigenvalue identification up to O(ρ^{−N})

**Paper 13.** CCM 2025 Theorem 5.10: the eigenvalues of `D_N`
approximate `{γ_n}` (imaginary parts of the zeros of ζ) to precision
`O(ρ^{−N})`, `ρ ≥ 4.27`.

**K-analogue.** The analogous theorem over K would state:
`spec(D_N^K)` approximates `{γ_n^K := Im(ρ_n^K) : ρ_n^K a non-trivial
zero of ζ_K}` to precision `O((ρ^K)^{−N})` for some `ρ^K > 1`.

**Task.** This is the heart of Phase I and requires porting CCM 2025
Theorem 5.10 to K. The approximation bound depends on:

1. The CF decay rate of the moment problem (sub-task 1.3),
2. The density of `K`-smooth ideals in the relevant range,
3. The archimedean correction at the complex place.

**Status.** The proof structure should transfer mechanically from CCM
2025 §5, but each estimate in §5 involves specific ℚ-analytic tools
(sieve theory, Euler–Maclaurin). Porting the bounds to K requires
re-running each estimate with `p → N(𝔭)` and `log(p) → log(N(𝔭))`.

**Numerical check proposal.** Before attempting the full theorem,
verify numerically that a K-CCM-type operator `D_N^K` constructed from
the first `N` Gaussian primes has eigenvalues close to the first
`N` non-trivial zeros of `ζ_K` (from LMFDB or sage). This is the
K-analogue of Paper 13's "55 digits at N = 6" sanity check.

**Negative result from `first_D_N_K.py` (2026-04-10):** A crude
"log-ratio kernel + Mangoldt diagonal" matrix at `N ∈ {3, 4, 5}`,
`M ∈ {20, 30}` produces eigenvalues entirely within `|λ| < 1` —
nowhere near `γ_1^K ≈ 14.13`. The same crude recipe applied to ℚ
also fails (best `δ ≈ 13.4` from `γ_1 = 14.13`), so the failure is
*intrinsic to the toy construction, not a porting bug*. The
missing ingredient is the **bandwidth parameter `λ`** that scales
Paper 13's operator (`‖T_0‖ ∼ λ`) and the **genuine prolate basis**
of CCM 2025 §4. **Lesson:** any numerical verification of sub-task
1.5 must (a) reproduce CCM 2025's 55-digit ℚ result first with a
working prolate-basis implementation, then (b) substitute `Λ_K` for
`Λ`, Gaussian primes for rational primes, `Γ(s)` at the complex
place for `Γ(s/2)` at the real place. There is no shortcut.

### Phase II — Layer 3: Estimates

#### Sub-task 2.1. Archimedean sub-leading estimate (Layer 3a)

**Paper 13.** Proposition 5.1: `‖τ^{(ℝ)}‖_op / ‖∑_p τ^{(p)}‖_op =
O(1/λ)`. Proof uses Stirling asymptotics on `Γ(s/2)` and the prime
number theorem to show the prime contribution dominates the
archimedean contribution as the spectral parameter `λ → ∞`.

**K-analogue.** At the complex place of `K`, the archimedean factor
is `Γ(s)` (not `Γ(s/2)` — the complex place contributes a double
gamma factor, but in the BC framework it's packaged as `2^{1−s}
π^{−s} Γ(s)` which has the same asymptotic growth as `Γ(s/2)²` by
the duplication formula). The Stirling bound therefore carries over
with a different constant.

**The prime number theorem for K** (prime ideal theorem;
Landau 1903) states
`#{𝔭 : N(𝔭) ≤ x} ∼ x / log x`
which has the same asymptotics as PNT over ℚ. The sum `∑_{N(𝔭) ≤ x}
log N(𝔭) / √N(𝔭) ∼ 2√x` (same leading order as over ℚ), so the
archimedean/prime ratio is `O(1/λ)` by the same estimate.

**Task.** Re-derive Proposition 5.1 over K, writing out the Stirling
bound at the complex place and the prime ideal sum. Both are
one-line modifications of Paper 13's proof.

**Status.** Mechanical.

#### Sub-task 2.2. Uniform Sobolev H¹ bound (Layer 3c)

**Paper 13.** Theorem 7.1: `‖(D_N − i)^{−1}‖_{L² → H¹} ≤ 2`
uniformly in `N` and `λ`. Proof uses Fourier-basis cancellation:
the `H¹` weight `1 + (2πn/L)²` exactly cancels the resolvent
denominator `(2πn/L)² + 1`.

**K-analogue.** Over `K_∞ = ℂ`, the Fourier basis is
`V_{(m,n)}(z) = L^{−1} exp(2πi (m Re(z) + n Im(z))/L)` on the
fundamental domain. The unperturbed Dirac-type operator acts as
`D_log^{(0)} V_{(m,n)} = (2π/L) √(m² + n²) · V_{(m,n)}` (by an
analogous construction to the ℚ case, using the Laplacian on ℂ).
The `H¹` weight is `1 + (2π/L)² (m² + n²)` and the resolvent
denominator is `((2π/L)² (m² + n²) + 1)` — same cancellation
structure.

**Task.** Verify the cancellation identity carries over to two
dimensions. This should be straightforward.

**Status.** **DONE** — see `uniform-H1-bound-over-K.md` for the
full writeup. The 2D Fourier-basis cancellation is verified
explicitly: the H¹ weight `1 + (2π/L)²(m² + n²)` exactly equals
the resolvent denominator `(2π/L)²(m² + n²) + 1`, mode-by-mode,
in any dimension. The unperturbed resolvent norm `L² → H¹` is
*exactly* 1, and the rank-one quotient correction is `O((ρ^K)^{−N})`,
giving `‖(D_N^K − i)^{−1}‖_{L² → H¹} ≤ 2` uniformly in `N` and
`λ_bw` for any `ρ^K ≥ 2`. Bögli H2 (discrete compactness) follows
by Rellich on `Π_L = [−L/2, L/2]² ⊂ ℝ²`.

#### Sub-task 2.3. Carathéodory–Fejér uniform decay (Layer 3d)

**Paper 13.** Proposition 8.1: CF approximation on the Bernstein
ellipse has rank-one decay `O(ρ^{−N})` with `ρ ≥ 4.27`, uniform in
`N`.

**K-analogue.** CF theory is abstract complex analysis; it does not
depend on the number field. What changes is the **specific CF
problem** being solved: it's the moment problem of the K-Weil form
(sub-task 1.3), not the ℚ one. The decay rate `ρ^K` may differ from
4.27 because the K-moment problem has different data.

**Task.** Compute `ρ^K` numerically by running CF on the first few
levels of the K-moment problem.

**Status.** Computational; no new theory needed.

#### Sub-task 2.4. Eigenvector approximation (Layer 3b)

**Paper 13.** Theorem 6.4: `‖ξ_λ − c · k_λ‖ = O(1/λ)` by
Davis–Kahan sin θ + archimedean sub-dominance.

**K-analogue.** Davis–Kahan is abstract operator theory. The
archimedean sub-dominance is sub-task 2.1. So the theorem transfers
directly once 2.1 is in place.

**Status.** Mechanical.

### Phase III — Layer 4: Teschl–Bögli synthesis

**Paper 13.** Theorem 9.1 (Teschl–Wang–Xie–Zhou 2026, Lemma 2.7) is
an abstract functional-analytic result: if the perturbation is form-
bounded with `a < 1`, the limit operator is self-adjoint and gnrc
holds. Then Bögli's Theorem 2.6 gives spectral exactness.

**K-transfer.** Both results are abstract and apply to any sequence
of operators on any Hilbert space. There is nothing to port: just
apply them to `D_N^K → D_∞^K`.

**Task.** Verify the Teschl form bound `a = 0 < 1` for the K-form
perturbation `δ_N^K = Q_N^K − P_N Q_0^K P_N`. This follows
immediately from the K-analogue of Corollary 8.3 (rank-one
stabilization), which is in turn a consequence of the K-CF decay
(sub-task 2.3).

**Status.** Direct application of existing theorems.

### Phase IV — Layer 5: Hurwitz identification over K

#### Sub-task 4.1. Fourier transform convergence

**Paper 13.** Theorem 10.1: `ξ̂_λ(z) → c · Ξ(z)` uniformly on closed
substrips of `|Im z| < 1/2`.

**K-analogue.** Define

```
  Ξ_K(s) := (1/2) s(s−1) · Λ_K(s)
         =  (1/2) s(s−1) · 4^{s/2} 2^{1−s} π^{−s} Γ(s) · ζ_K(s),
```

which is entire and satisfies `Ξ_K(s) = Ξ_K(1−s)` (even about
`s = 1/2`). Under the change of variable `s = 1/2 + iz`, `Ξ_K(z)`
is an even entire function of `z` with zeros at
`z = Im(ρ^K)` for each non-trivial zero `ρ^K` of ζ_K.

**Target.** `(ξ̂_λ^K)(z) → c^K · Ξ_K(z)` uniformly on closed
substrips of `|Im z| < 1/2`.

**Task.** Port CCM Lemma 7.3 to the K-analogue. CCM 2025
Lemma 7.3 establishes a **prolate-to-Hermite expansion** for the
prolate eigenfunctions: as the bandwidth parameter grows, the
prolate eigenfunctions `h_{n, λ}` converge to the classical
Hermite functions `h_n` with controlled error, and the
appropriately combined and normalized object converges to the
Riemann Xi function `Ξ` uniformly on closed substrips of
`|Im z| < 1/2`. The mechanism is a Hermite expansion of the
prolate eigenfunctions on the line, not a Mellin / sieve
estimate. (Verified against the HTML rendering of arXiv:2511.22755
Section 7; the exact statement of Lemma 7.3 in CCM 2025 should
be reproduced verbatim in any final port.)

**K-analogue.** Sub-task 1.1 supplies a ℂ-prolate basis
`{e_𝔞}` on `L²(ℂ)`. The K-version of Lemma 7.3 must establish
the analogous prolate-to-Hermite-type expansion on `ℂ`, with
the limit object the K-Riemann xi `Ξ_K` of (4.1) above. Two
non-trivial pieces of new work:

1. **Identify the ℂ-Hermite analogue.** On `ℝ`, the Hermite
   functions are eigenfunctions of the harmonic oscillator
   `−∂² + x²`. On `ℂ ≅ ℝ²`, the natural analogues are
   eigenfunctions of `−∂_x² − ∂_y² + (x² + y²)`, which are
   tensor products of 1D Hermite functions and form an
   orthonormal basis of `L²(ℂ)`.
2. **Establish the K-prolate expansion in this ℂ-Hermite basis.**
   Match the leading-order coefficients to the Mellin / Hecke
   data of `Ξ_K`, control the error in the bandwidth parameter,
   and confirm uniform convergence on substrips.

**Status.** This is genuine new work. The prolate-to-Hermite
expansion for the K case has not been carried out in the
literature. The structure of the argument is mechanical (port of
the ℝ case to the ℂ case) but each step needs writing out — in
particular the ℂ-Hermite basis is well-known classically but its
combination with the "first `N` Gaussian primes" prolate cutoff
of sub-task 1.1 is new.

#### Sub-task 4.2. Hurwitz application

**Paper 13.** Theorem 10.2: each `ξ̂_λ^{(N)}` has only real zeros
(CCM 5.10(iii)), so by Hurwitz their limit `Ξ` has only real zeros.

**K-analogue.** Each `(ξ̂_λ^{K,(N)})` has only real zeros (by the
K-analogue of CCM Theorem 5.10(iii), sub-task 1.5), so by Hurwitz
their limit `Ξ_K` has only real zeros. Therefore every non-trivial
zero of `ζ_K` has `Re(ρ^K) = 1/2`.

**Non-vanishing at origin.** Paper 13 verifies `Ξ(0) = 0.4971… ≠ 0`
to ensure Hurwitz's non-vanishing hypothesis. For K = ℚ(i):

```
  Ξ_K(0) = (1/2) · 0 · (−1) · Λ_K(0) = 0 ???
```

Wait — the `s(s−1)/2` factor vanishes at `s = 0` and `s = 1`. This
is a problem; `Ξ_K(0) = 0` trivially, and Hurwitz would need to be
applied at a different point.

**Resolution.** `Ξ_K(0) = 0` is a "trivial zero" contribution from
the `s(s−1)` factor, not from a zero of `ζ_K`. Apply Hurwitz at
`z = 1/2` (i.e., `s = 1`), or more naturally, shift the change of
variable: use `Ξ̃_K(z) := Ξ_K(1/2 + iz) / (non-vanishing factor)`
so that `Ξ̃_K(0) ≠ 0`. For Paper 13's ℚ case,

```
  Ξ(0) = (1/2)(1/2)(1/2 − 1) · Λ(1/2)
       = −(1/8) · π^{−1/4} Γ(1/4) ζ(1/2)
       ≈  0.4971…
```

For K = ℚ(i), the analogous computation is

```
  Ξ_K(1/2) = (1/2)(1/2)(−1/2) · Λ_K(1/2)
           = −(1/8) · 4^{1/4} 2^{1/2} π^{−1/2} Γ(1/2) · ζ_K(1/2)
           = −(1/8) · √2 · √2 · π^{−1/2} · √π · ζ_K(1/2)
           = −(1/4) · ζ_K(1/2).
```

So `Ξ̃_K(0) = −(1/4) · ζ_K(1/2)`. Numerically, `ζ_K(1/2) =
ζ(1/2) · L(1/2, χ_{−4}) ≈ (−1.4603…) · (0.6676…) ≈ −0.9749…`, so
`Ξ̃_K(0) ≈ 0.2437…`, which is non-zero. ✓

**Computational check.** See `code/verify_xi_K_at_origin.py` below.

**Status.** Mechanical once sub-task 4.1 is in place.

### Phase V — Layer 6: Assembly

**Paper 13.** Theorem 11.1: combine Bögli (spec(D_∞) = lim spec(D_N))
with Hurwitz (zeros of the limit are real) to conclude RH.

**K-analogue.** Identical logic over K: GRH for ζ_K follows from
sub-tasks 3 (Bögli) + 4 (Hurwitz). The proof of Theorem 11.1 over K
is a one-page assembly.

**Status.** Direct.

## Twist to L(s, ψ) — the BSD-specific piece

Paper 26 needs GRH for the Hecke L-function `L(s, ψ)` where `ψ` is
the Grössencharacter attached to a CM elliptic curve `E/ℚ`. This
requires a twisted version of Phases I–V.

### Twisted Weil form

The twisted Weil quadratic form `Q_N^{K,ψ}` inserts the Hecke
character into the diagonal:

```
  Q_N^{K,ψ}(f, g) = (off-diagonal as in Q_N^K)
                    + ∑_𝔞 Λ_K(𝔞) · ψ(𝔞) · ⟨f, e_𝔞⟩⟨e_𝔞, g⟩
                    + (archimedean, depending on ψ_∞).
```

Since `|ψ(𝔭)| = 1`, the operator norms are the same as the untwisted
case, and the Sobolev and CF estimates (Phases II) carry over
unchanged.

### Twisted Ξ function

```
  Ξ_{K,ψ}(s) := (completion factor) · L(s, ψ),
```

where the completion factor is Hecke's `Γ`-factor for `L(s, ψ)`
(depends on the infinity type of `ψ`). Satisfies
`Ξ_{K,ψ}(s) = ε(ψ) · Ξ_{K,ψ̄}(1 − s)` with `|ε(ψ)| = 1`.

For CM elliptic curves over `ℚ`, the Grössencharacter `ψ`
satisfies `ψ̄ = ψ ∘ c` (complex conjugation), so `Ξ_{K,ψ}(1 − s) =
ε^{−1} Ξ_{K,ψ}(s)` in a self-conjugate way. The even sector of the
K-CCM construction must be adapted to this self-dual structure.

**Task.** Verify that the parity argument (sub-task 1.4) extends to
the twisted case when `ε(ψ) = ±1`. If `ε(ψ) = +1`, the twisted Ξ
is even; if `ε(ψ) = −1`, it is odd and the odd sector is used
instead. Either way, the Hurwitz argument gives real zeros.

**Status.** Mechanical, depending on whether `ε(ψ) = ±1`.

### Twisted Fourier convergence

The K-analogue of CCM Lemma 7.3 for the twisted case: the
prolate-to-Hermite expansion of sub-task 4.1 carries through with
`Λ_K → Λ_K · ψ` and the limit object replaced by `Ξ_{K, ψ}` of
(twisted-Ξ above). Because `|ψ(𝔭)| = 1`, the Hermite-coefficient
estimates are the same up to phase factors that drop out of the
moduli, so the expansion converges uniformly on substrips with
the same rate as the untwisted case.

## Milestones and dependency graph

```
               ┌──────────────────────────────────────┐
               │       Phase I (Layer 1: K-CCM)       │
               │  1.1 E_N^{+,K}  ──▶ 1.2 Q_N^K ──▶    │
               │       (open)        ✓ DONE           │
               │  1.3 CF-SA  ──▶ 1.4 parity ──▶       │
               │      (open)         ✓ in 1.2         │
               │  1.5 eigenvalue ID (CCM 5.10 port)   │
               │       (open — the crux)              │
               └────────────────────┬─────────────────┘
                                    │
                     ┌──────────────┼───────────────┐
                     ▼              ▼               ▼
          ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
          │ Phase II 2.1 │ │ Phase II 2.2 │ │ Phase II 2.3 │
          │  archimedean │ │ uniform H¹   │ │  CF decay    │
          │   (open)     │ │  ✓ DONE      │ │  (open)      │
          └──────┬───────┘ └───────┬──────┘ └──────┬───────┘
                 │                 │               │
                 └─────────────────┼───────────────┘
                                   │
                                   ▼
                       ┌──────────────────────┐
                       │  Phase III: Bögli    │
                       │   spectral exactness │
                       │   spec(D_∞^K)        │
                       │   = lim spec(D_N^K)  │
                       │   (abstract; ready)  │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │  Phase IV: Hurwitz   │
                       │   spec(D_∞^K)        │
                       │   = {zeros of Ξ_K}   │
                       │   4.1 (open)         │
                       │   4.2 ✓ Ξ_K(1/2)≠0   │
                       │       (verified num) │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │  Phase V: Assembly   │
                       │  GRH for ζ_K         │
                       │  (1 page; ready)     │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │  Twist: L(s, ψ)      │
                       │  GRH for Hecke L     │
                       │  (mechanical from K) │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │  MY4 CLOSED          │
                       │  BSD chain: 11 / 11  │
                       └──────────────────────┘
```

### Cross-check invariant (Sagnier consistency)

Sagnier 2017 / 2019 computes the **adelic point count** of the
Connes–Consani arithmetic site for `K` and shows it counts the
non-trivial zeros of `ζ_K` (and Hecke L-functions with archimedean
ramification, including those with non-trivial infinity type at the
complex place — i.e., the Grössencharacter family relevant to BSD).

Any successful Route 2 construction `D_∞^K` must satisfy

```
spec(D_∞^K)  =  Sagnier point count for K's arithmetic site
            ⊃  {Im(ρ) : ρ a non-trivial zero of ζ_K}
            ⊃  {Im(ρ) : ρ a non-trivial zero of L(s, ψ),
                          ψ a Hecke Grössencharacter of K}.
```

Sagnier's count is the *external sanity check*: it tells us what the
target spectrum is at the adelic / topological level, independent of
the operator-theoretic construction. If a future numerical or
analytical port of CCM 2025 over K produces a spectrum that
disagrees with Sagnier's point count, the construction is wrong.

## What's mechanical vs. what needs new ideas

**Mechanical (symbolic substitution from Paper 13 / CCM 2025):**
- 1.2 (Weil form definition)
- 1.3 (CF self-adjointness — assuming the moment problem is positive)
- 1.4 (parity from functional equation)
- 2.1 (archimedean sub-dominance)
- 2.2 (uniform H¹ bound, 2D Fourier cancellation)
- 2.4 (Davis–Kahan)
- Phase III (abstract Teschl–Bögli)
- Phase V (assembly)
- Twist (every step commutes with phase insertion)

**Needs new work (re-running estimates over K):**
- 1.1 (ℂ-prolate wave functions + K-smooth truncation — no
  literature)
- 1.5 (porting CCM 2025 Theorem 5.10 line by line)
- 2.3 (CF decay rate `ρ^K` — computational)
- 4.1 (porting CCM Lemma 7.3 — prolate-to-Hermite expansion for `Ξ_K`)

**The crux is 1.5 (CCM Theorem 5.10 over K).** Everything else hangs
off it. Paper 13 treats CCM 2025 Theorem 5.10 as a black box; we must
open the black box and replicate its proof over K.

## Computational stubs

### Stub 1: verify Ξ_K(1/2) ≠ 0

```python
# code/verify_xi_K_at_origin.py
from mpmath import mp, mpf, gamma, pi, sqrt, zeta, dirichlet, power

mp.dps = 40

def lambda_K_gaussian(s):
    """Completed Dedekind zeta for K = Q(i)."""
    # Λ_K(s) = 4^{s/2} · 2^(1-s) · π^{-s} · Γ(s) · ζ_K(s)
    # ζ_K(s) = ζ(s) · L(s, χ_{-4}) where χ_{-4} is Kronecker character mod 4
    zeta_val = zeta(s)
    # L(s, χ_{-4}) = Dirichlet L-function with character [0, 1, 0, -1]
    L_chi = dirichlet(s, [0, 1, 0, -1])
    zeta_K = zeta_val * L_chi
    completion = power(4, s/2) * power(2, 1-s) * power(pi, -s) * gamma(s)
    return completion * zeta_K

def xi_K(s):
    """Ξ_K(s) = (1/2) s(s-1) Λ_K(s)."""
    return mpf('0.5') * s * (s - 1) * lambda_K_gaussian(s)

print("Ξ_K(1/2) =", xi_K(mpf('0.5')))
print("Ξ_K(1/2) should be -(1/4) ζ_K(1/2) ≈", -zeta(mpf('0.5')) * dirichlet(mpf('0.5'), [0,1,0,-1]) / 4)
print("non-zero: ", abs(xi_K(mpf('0.5'))) > mpf('1e-10'))
```

Run this to sanity-check the Hurwitz non-vanishing hypothesis.

### Stub 2: Gaussian prime enumeration and first zeros of ζ_K

```python
# code/ccm_over_K_sanity.py
from mpmath import mp, mpf, zeta, dirichlet, mpc, findroot
from sympy import primerange, isprime

mp.dps = 40

def gaussian_primes_by_norm(max_norm):
    """Enumerate Gaussian primes up to given norm."""
    primes = []
    # p ≡ 3 mod 4: inert, norm p^2
    for p in primerange(2, max_norm + 1):
        if p == 2:
            primes.append((1, 1, 2))  # (1+i), norm 2
        elif p % 4 == 1:
            # Split: find a+bi with a^2+b^2=p
            for a in range(1, int(p**0.5) + 1):
                b2 = p - a*a
                if b2 > 0:
                    b = int(b2**0.5)
                    if b*b == b2:
                        primes.append((a, b, p))
                        primes.append((a, -b, p))
                        break
        elif p % 4 == 3 and p*p <= max_norm:
            primes.append((p, 0, p*p))  # inert
    primes.sort(key=lambda t: t[2])
    return primes

print("First 10 Gaussian primes by norm:")
for a, b, N in gaussian_primes_by_norm(50)[:10]:
    print(f"  ({a:+d} {b:+d}i), N = {N}")

def zeta_K(s):
    """Dedekind zeta for K = Q(i)."""
    return zeta(s) * dirichlet(s, [0, 1, 0, -1])

# Find the first non-trivial zero on Re(s) = 1/2
# (assuming GRH for sanity-check purposes)
print("\nFirst few non-trivial zeros of ζ_K assuming GRH:")
print("(by finding zeros of ζ_K(1/2 + it) on the real line)")

# Newton iteration from rough estimates
starting_points = [6.0, 12.0, 14.0, 18.0, 22.0]
for t0 in starting_points:
    try:
        root = findroot(lambda t: zeta_K(mpc(mpf('0.5'), t)), t0)
        print(f"  γ ≈ {float(root.real):.6f}  (starting from t₀ = {t0})")
    except Exception as e:
        print(f"  failed at t₀ = {t0}: {e}")
```

When the K-CCM machinery is built, compare `spec(D_N^K)` against
these `γ^K` values — analogous to Paper 13's 55-digit sanity check
for the ℚ case.

## Scope

Route 2, as instrumented above, is **a research program, not a
one-conversation task**. The phases are:

| Phase | Description |
|:------|:------------|
| I | Layer 1 K-CCM construction (ℂ-prolate basis + Weil form + CF self-adjointness + parity + eigenvalue identification) |
| II | Layer 3 estimates over K (archimedean, uniform H¹, CF decay, Davis–Kahan) |
| III | Layer 4 Teschl–Bögli (abstract; just applying existing theorems) |
| IV | Layer 5 Hurwitz + `Ξ_K` (prolate-to-Hermite expansion, real-zero conclusion) |
| V | Assembly (GRH for ζ_K) |
| + | Twist to `L(s, ψ)` for Hecke Grössencharacters |

The whole port would warrant its own preprint ("Paper 27:
CCM + ITPFI + Bögli + Hurwitz over imaginary quadratic fields"),
which Paper 26 would then reference.

The crux is sub-task 1.5 (the K-version of CCM Theorem 5.10).

## Recommended next steps (in order, updated 2026-04-10 second pass)

The first three recommended steps from the 2026-04-10 first pass have
been carried out. Updated list:

1. ~~**Sanity checks now**: `verify_xi_K_at_origin.py` and
   `ccm_over_K_sanity.py`.~~ **DONE.** `Ξ_K(1/2) ≈ 0.2438 ≠ 0`
   (matches `−(1/4) ζ_K(1/2)` to 40 digits). First six non-trivial
   zeros of `ζ_K` enumerated and verified.

2. ~~**Phase I start: write the Weil form `Q_N^K` explicitly.**~~
   **DONE.** See `weil-form-over-K.md` (~500 lines). Five open
   issues identified; (O1) same-norm collisions and (O2) precise
   form of `τ^{(K_∞)}` are the two genuinely new K-issues to
   resolve.

3. ~~**Phase I start: build a first numerical D_N^K and test.**~~
   **DONE — negative result.** `first_D_N_K.py`. Diagnosis: the
   bandwidth parameter `λ` and the genuine prolate basis are
   load-bearing. The same crude recipe fails over ℚ too, so the
   failure isn't a porting bug. **Lesson:** numerical verification
   of Phase I requires reproducing CCM 2025's 55-digit ℚ result
   first, then porting.

4. ~~**Literature dive.**~~ **DONE.** Sagnier 2017 / 2019 is the
   closest existing K work — gives the *adelic skeleton* for the
   K-arithmetic site but no Hilbert-space machinery. CCM 2025
   doesn't cite Sagnier. The Hilbert-space K-port is virgin. Use
   Sagnier's adelic point count as the *external sanity check
   invariant* (see "Cross-check invariant" above).

5. **Phase II completions** (next concrete batch):
   - Sub-task 2.2 (uniform H¹ bound): **DONE**, see
     `uniform-H1-bound-over-K.md`.
   - Sub-task 2.1 (archimedean estimate): port of Paper 13 §5
     Proposition 5.1 — straightforward; needs to be written out.
   - Sub-task 2.4 (Davis–Kahan eigenvector approximation): direct
     port; depends on 2.1.

6. **Phase III is ready to apply** once Phase II 2.1 + 2.4 are done
   and the form bound `a = 0` is verified for `δ_N^K`. Phase III is
   abstract Teschl + Bögli — no porting required.

7. **Phase IV (Hurwitz over K):**
   - 4.2 ✓ verified `Ξ_K(1/2) ≠ 0`.
   - 4.1 (prolate-to-Hermite expansion for `Ξ_K`): port of CCM
     Lemma 7.3 — non-trivial but structurally mechanical. Could be
     done in parallel with Phase I.

8. **Phase I crux (1.5):** the port of CCM Theorem 5.10 to K.
   This requires opening the CCM 2025 §5 black box and replicating
   each estimate over `K`. There is no obvious shortcut.

9. **Reproduce CCM 2025 over ℚ first.** Per the lesson from the
   negative numerical experiment: before any K-port, build a working
   ℚ implementation (the prolate basis + Weil form + CF moment
   problem + 55-digit `γ_n` agreement at `N = 6`). See CCM 2025
   Table 1 for the target. With a working ℚ implementation, the
   K-port becomes a substitution exercise.

## Status (as of 2026-04-10 second pass)

**Route 2 progress so far:**

| Item | Status |
|:-----|:-------|
| Layer 2 (BC, KMS₁, ITPFI, Nelson SA) | ✓ in Paper 26 §3, §5 |
| Phase I sub-task 1.1 (ℂ-prolate Hilbert space) | open — needs new construction |
| Phase I sub-task 1.2 (Weil form `Q_N^K`) | ✓ `weil-form-over-K.md` |
| Phase I sub-task 1.3 (CF self-adjointness) | open — depends on 1.2 |
| Phase I sub-task 1.4 (parity / even sector) | ✓ inside `weil-form-over-K.md` §6 |
| Phase I sub-task 1.5 (CCM 5.10 over K) | open — **the crux** |
| Phase II sub-task 2.1 (archimedean) | open — mechanical |
| Phase II sub-task 2.2 (uniform H¹ bound) | ✓ `uniform-H1-bound-over-K.md` |
| Phase II sub-task 2.3 (CF decay rate `ρ^K`) | open — computational |
| Phase II sub-task 2.4 (Davis–Kahan) | open — depends on 2.1 |
| Phase III (Teschl–Bögli) | ✓ ready (abstract; pending 2.4) |
| Phase IV sub-task 4.1 (Fourier → Ξ_K) | open — port of CCM Lemma 7.3 prolate-to-Hermite expansion |
| Phase IV sub-task 4.2 (Hurwitz non-vanishing) | ✓ `verify_xi_K_at_origin.py` |
| Phase V (assembly) | ✓ ready (1 page) |
| Twist to L(s, ψ) | open — mechanical extension |
| **Sagnier consistency invariant** | ✓ identified as cross-check target |

**Counts:** 6 sub-tasks DONE, 9 open. The 9 open items cluster as
3 mechanical ports (2.1, 2.4, twist), 3 needs-new-work (1.1, 1.5, 4.1),
2 computational (1.3, 2.3), 1 dependent (4.2 Hurwitz application is
trivial once 1.5 + 4.1 are done).

**Bottleneck.** The crux remains sub-task 1.5 (port CCM Theorem 5.10).
Everything else can be done in parallel; 1.5 requires opening the CCM
2025 §5 black box and replicating each estimate over `K`.

**For the BSD paper as it stands today:** MY4 remains
`[KEY LEMMA — OPEN]`. The chain closes to 10 of 11. With Route 2
fully executed, it would close to 11 of 11. The instrumentation
plus the 6 completed sub-tasks have already cleared the easy
mechanical pieces, and the negative numerical result tells us not
to waste effort on shortcuts.

## Cross-references

- `research/meyer-extension-to-K.md` — Key Lemmas A and B (the
  Meyer/twisted extension, conditional on MY4)
- `research/distributional-to-genuine.md` — why MY4 is the wall and
  what the two routes (1 and 2) are
- `research/cohomology-class-lemma.md` — Key Lemma C (unconditional)
- `research/corrected-bridge-table.md` — Gap G1 (unconditional)
- `research/weil-form-over-K.md` — Phase I sub-task 1.2 writeup
  (the K-Weil quadratic form, completed 2026-04-10 second pass)
- `research/uniform-H1-bound-over-K.md` — Phase II sub-task 2.2
  writeup (the 2D Fourier-cancellation H¹ bound, completed
  2026-04-10 second pass)
- `referee/code/first_D_N_K.py` — the negative-result numerical
  experiment (no signal in the toy construction; same recipe
  fails over ℚ too — diagnosis: need bandwidth + real prolate
  basis)
- `referee/code/verify_xi_K_at_origin.py` — Phase IV sub-task 4.2:
  `Ξ_K(1/2) ≈ 0.2438 ≠ 0`
- `referee/code/ccm_over_K_sanity.py` — Gaussian prime enumeration
  + first non-trivial zeros of `ζ_K`
- `/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper13-rh/preprint/sections-01-05.md`
  §3 (Layer 1), §4 (Layer 2), §5 (Layer 3a)
- `/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper13-rh/preprint/sections-06-10.md`
  §6 (Layer 3b), §7 (Layer 3c), §8 (Layer 3d), §9 (Layer 4),
  §10 (Layer 5)
- CCM 2025 arXiv:2511.22755 — the target to port (esp. §4, §5,
  Theorem 5.10, Lemma 7.3). **Does not cite Sagnier; strictly over ℚ.**
- **Sagnier 2017, arXiv:1703.10521** + Sagnier *J. Number Theory*
  2019 (with appendix by Connes) — the Connes–Consani arithmetic
  site for K = ℚ(i) and the nine class-number-1 imaginary quadratic
  fields. Provides the adelic / topological skeleton; does NOT
  build the operator-level spectral triple. **Use as the
  Sagnier consistency invariant cross-check above.**
- **Ha–Paugam 2005, arXiv:math/0507101** — the BC algebra
  `A_{BC,K}`. Already used in Paper 26 §3.1.
- **Laca–Neshveyev–Trifković 2013, arXiv:1010.4766** — BC induction
  for narrow class number 1.
- **Connes–Marcolli, *Noncommutative Geometry, Quantum Fields and
  Motives*** (AMS, 2008), §4–5 — twisted spectral realization for
  L(s, ψ) over **ℚ**, the template for Key Lemma B.
- **Simons–Wang 2011** (GEM J.) — 2D Slepian functions in `ℝ²`
  (the closest existing analogue to the ℂ-prolate functions
  needed for sub-task 1.1).
- `referee/latest-run/checks/MY-meyer/MY4.md` — the audit finding
  that motivated this plan
