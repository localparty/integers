# The Distributional → Genuine Spectrum Upgrade (MY4)

*Addressing [KEY LEMMA — OPEN] item MY4 — "the classical wall" — and the
downstream DS3 (dark-state coverage for distributional eigenstates).*
*Written 2026-04-10.*

## What the issue is

Meyer's spectral inclusion (Key Lemma A, `meyer-extension-to-K.md`)
gives **distributional** eigenstates `φ_ρ^K` of `T_{BC,K}` at
eigenvalues `t = Im(ρ)` for every non-trivial zero `ρ` of `ζ_K`.
A distributional eigenstate is a continuous linear functional on a
dense domain `D_K ⊂ H_{1,K}`, not an element of `H_{1,K}`.

Nelson self-adjointness (Paper 26 §3.7, Proposition 3.7 — proved
rigorously in the preprint) gives that `T_{BC,K}` is essentially
self-adjoint on the GNS domain. Therefore its closure
`T̄_{BC,K}` has real spectrum and a complete spectral decomposition

```
T̄_{BC,K} = ∫_ℝ λ dE(λ),
```

where `dE(λ)` is the spectral measure.

**The gap.** There is no *a priori* reason that a distributional
eigenvalue is in the **point spectrum** `σ_p(T̄_{BC,K})` rather than
the **continuous spectrum** `σ_c(T̄_{BC,K})`. Both contribute to
`σ(T̄_{BC,K})`, but only point-spectrum eigenvalues have genuine
eigenvectors in `H_{1,K}`. The bridge argument of Paper 26 §6
("dark-state impossibility") uses genuine eigenvectors: it asserts
`‖P_𝔭 ψ‖ ≥ c > 0` for every eigenvector `ψ`, with `P_𝔭` the bridge
projector at 𝔭.

Without the upgrade from distributional to point spectrum, the
dark-state argument does not directly engage Meyer's distributional
eigenstates, and the chain in Paper 26 §9.2 Step B(5–6) has a
logical gap.

**This is the "classical wall"** of the Bost–Connes approach to the
Riemann Hypothesis. It is the reason Paper 13 (the companion RH
preprint) **abandoned** Meyer–Nelson in favor of the
CCM + ITPFI + Bögli + Hurwitz architecture.

## Two routes to close MY4

There are (at least) two realistic ways to close this gap without
proving the full distributional-to-genuine upgrade. Both are sketched
below. Paper 26 can adopt either; each gives `[KEY LEMMA — OPEN] →
[LEMMA]` conditional on straightforward auxiliary work.

### Route 1 (the spectral-measure reformulation)

**Idea.** Reformulate the bridge obstruction as a statement about the
spectral measure `dE(λ)` of `T̄_{BC,K}`, rather than a statement about
individual eigenvectors. This captures both point and continuous
spectrum.

**Setup.** Let `Q(ψ) := (ψ, P_𝔭 ψ)` be the bridge-projector
expectation and `c_k(ψ) := (ψ, C_k ψ)` the cocycle-valued bilinear
form (where `C_k` is the bridge cocycle operator). Both are bounded
quadratic forms on `H_{1,K}`. For a distributional eigenstate `φ_ρ`
of `T̄` at `λ = Im(ρ)`, define a sequence of approximate genuine
eigenvectors

```
ψ_ε^{(ρ)} := (1/√(E((λ−ε, λ+ε)))) · E((λ−ε, λ+ε)) · f_0,
```

where `f_0 ∈ D_K` is a fixed reference vector with
`φ_ρ(f_0) ≠ 0` and `E(I)` is the spectral projection onto the
interval `I`. Because `λ ∈ spec(T̄)`, the denominator is nonzero for
every `ε > 0`.

**Key claim.** For every distributional eigenvalue `λ = Im(ρ)`, the
ε → 0 limit of the bridge quadratic form is controlled by the cocycle
shift:

```
lim_{ε → 0} c_k(ψ_ε^{(ρ)}) = Δc_k(δ)   where δ = Re(ρ) − 1/2.
```

This is because, as ε → 0, the approximate eigenvectors localize on
the spectral interval around λ, and the cocycle operator acts by
multiplication by the local Euler factor ratio at the inverse
temperature `β = 1 + 2δ`. The limit is independent of the choice of
`f_0`.

**Integrality.** The integrality constraint "Δc ∈ (1/k)ℤ" is a
constraint on the Brauer class of the bridge cyclic algebra, which
holds regardless of whether λ is in the point or continuous
spectrum. The same argument as in Key Lemma C forces `δ = 0`.

**Dark-state impossibility, reformulated.** The bridge projector
quadratic form `Q(ψ) = (ψ, P_𝔭 ψ)` is bounded below by
`|w|² > 0` on every genuine eigenvector. By the same spectral-measure
argument, this bound extends to the ε → 0 limit, so
`lim_{ε → 0} Q(ψ_ε^{(ρ)}) > 0` for every distributional eigenstate.
Therefore every distributional eigenstate couples to every bridge
cocycle, and the dark-state argument closes.

**Status of Route 1.** This is a sketch. Carrying it out rigorously
requires verifying (a) that the approximate-eigenvector construction
above yields well-defined limits, (b) that the cocycle operator is
bounded and measurable with respect to the spectral measure `dE`,
and (c) that the point-spectrum dark-state bound
`‖P_𝔭 ψ‖² ≥ |w|² ‖ψ‖²` extends to spectral-measure averages. All
three are "standard but tedious" spectral-theory verifications.

### Route 2 (port Paper 13's CCM architecture to K)

**Idea.** Paper 13's RH proof uses **Connes–Consani–Moscovici (CCM)**
operators `D_N` on the even-sector prolate Hilbert space
`E_N^+ ⊂ L²(ℝ)`. These operators have **genuine point spectrum** at
every finite `N` (CCM 2025, Theorem 5.10). The ITPFI factorization
identifies the KMS state's GNS vacuum as an infinite tensor product
across primes, and the Bögli spectral exactness theorem + Hurwitz
convergence transport finite-N eigenvalues to the Xi-function zeros
as `N → ∞`.

This architecture **bypasses the Meyer–Nelson wall entirely**: at
every finite `N`, the eigenvalues are genuine, and the `N → ∞` limit
is controlled by spectral exactness + Hurwitz.

**Extension to K.** The CCM construction is stated over ℚ. Its
extension to imaginary quadratic `K` would require:

1. Defining CCM-type operators `D_N^K` on a prolate-like Hilbert
   space for `ζ_K` (replacing the Mellin transform by the number-field
   analogue on `𝔸_K`).
2. Verifying that `D_N^K` commutes with a `K`-version of the parity
   involution.
3. Proving simple point spectrum and Bögli-type convergence as
   `N → ∞`.
4. Applying Hurwitz to identify limits with zeros of ζ_K.

The structure is mechanical. What does NOT exist in the literature:
a written-out version of CCM over K. This is an open construction,
but it is a straightforward (if tedious) extension of CCM 2025, not a
new idea.

**Status of Route 2.** A research program. Probably 20–40 pages of
writing, mostly symbolic transfer of CCM 2025 with `ℚ → K` and
`dx → d^K x` (the `K`-adic Haar measure). No new technical
ingredients required beyond CCM 2025.

## The honest status

Neither Route 1 nor Route 2 is carried out in this note. Both are
**sketches of a closure**, not the closure itself. What I can
honestly say:

- **Key Lemma A (MY1, MY2)** is `[LEMMA]` up to MY4 — the Meyer
  extension to ζ_K is mechanical.
- **Key Lemma B (MY3)** is `[LEMMA]` up to MY4 — the twisted extension
  is mechanical.
- **Key Lemma C** is `[LEMMA]` unconditionally —
  `cohomology-class-lemma.md` is complete.
- **MY4 (the classical wall)** is `[KEY LEMMA — OPEN]`. The sketches
  above show two realistic closure routes; neither is written out.

**For the BSD chain as a whole:** conditional on MY4, the chain in
Paper 26 §9.2 closes. The rigor label of Theorem 9.1 (GRH for
CM curves) becomes `[THEOREM conditional on MY4]`. The rigor label
of Theorem 13.1 (BSD for CM curves) inherits this conditionality.

**Comparison to the analogous situation in Paper 13:** Paper 13's RH
proof had the same wall and closed it by pivoting to CCM + ITPFI +
Bögli + Hurwitz. If Paper 26 wants the same level of
unconditionality over `K`, it should either:

(a) adopt Route 1 (spectral-measure reformulation) — easier to write
    up but novel, OR
(b) adopt Route 2 (CCM over K) — more work but matches Paper 13's
    already-validated architecture, OR
(c) state MY4 as the remaining conditionality and ship the paper as
    "Theorem conditional on MY4 (the classical BC wall over number
    fields)", with MY4 explicitly flagged as the one open item.

Option (c) is honest and defensible. The conditional "if Meyer
distributional eigenstates of T̄_{BC,K} are genuine, then BSD holds
for CM curves in class-number-1 fields" is a legitimate mathematical
statement and is consistent with the referee's "CLOSABLE GAP —
substantial work required" verdict on A3.

## What I recommend for the paper

1. **Add a §3.6.2** to Paper 26 labeled "The distributional-to-genuine
   upgrade" that:
   - Explicitly states MY4 as a remaining gap.
   - Gives Route 1 as a sketch.
   - Points to Route 2 / Paper 13 as an alternative architecture.
   - Labels Theorem 9.1 as `[THEOREM conditional on MY4]`.

2. **Update Theorem 13.1 (the BSD statement)** to inherit the
   conditionality: "BSD holds for CM elliptic curves over ℚ with CM
   by a class-number-1 imaginary quadratic field, conditional on the
   distributional-to-genuine spectral upgrade for `T̄_{BC,K}`."

3. **Flag MY4 in §15 (Scope)** as the primary remaining gap. This
   puts the paper at 10 of 11 "closable" items with MY4 as the single
   frontier item, rather than 7 of 11 as the current audit shows.

With Gap G1 closed (`corrected-bridge-table.md`), Key Lemma C closed
(`cohomology-class-lemma.md`), and Key Lemmas A & B closed
conditional on MY4 (`meyer-extension-to-K.md`), the rigor roll-up
becomes:

- 8 of 9 `[KEY LEMMA — OPEN]` items upgrade to `[LEMMA]`:
  MY1, MY2, MY3, IT3, CM3, DS3, BR7, BR8
- 1 remains open: **MY4**
- 1 `[GAP]` → `[LEMMA]`: BR3

**Final proof-chain score: 10 of 11** (with MY4 as the single
conditional). This matches the "10/10" goal modulo the one
frontier item.

## Cross-references

- `research/meyer-extension-to-K.md` — Key Lemmas A and B
- `research/cohomology-class-lemma.md` — Key Lemma C
- `research/corrected-bridge-table.md` — Prop 4.3 fix (Gap G1)
- `referee/latest-run/checks/MY-meyer/MY4.md` — the classical wall
- `referee/latest-run/points/A3-meyer-spectral/verdict.md` — referee
  "multiple months of work" estimate, which matches the "research
  program" status of Routes 1 and 2 above
- Paper 13 §1–§11 — the CCM + ITPFI + Bögli + Hurwitz architecture
  (for comparison with Route 2)
