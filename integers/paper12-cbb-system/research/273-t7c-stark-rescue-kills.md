# 273. T7c Stark-Rescue Kill List — Six Refuted Identifications

*Author: G Six with Claude Opus 4.6 (wave harvest, 2026-04-11).*
*Canonical kill-list entry for the six pre-committed rescue candidates
that were tested and refuted in `integers/paper12-cbb-system/relaxation/research/T7c-stark-rescue-verification.md`.
This file exists so that future runs, future mathematicians, and
future search queries can find the kills by pattern category and not
re-attempt them without new structural input. Sig 6 of the ORA
runner — the kill list IS the search query — applied to the
relaxation cycle's Lead 7c.*

---

## 1. The wall

The bridge cocycle `1/k mod ℤ` is a **discrete invariant** in
`H²(ℤ/kℤ, U(1))` on all four bridges of the framework:
`(p, N, k) ∈ {(2,7,2), (5,13,3), (3,13,4), (7,19,6)}`. Lead 7b
(`integers/paper12-cbb-system/relaxation/research/T1-T2-brauer-cohomology-verification.md`)
verified this at exact integer arithmetic via the Hasse invariant
`inv_p(Q(ζ_N)/Q, Frob_p, ζ_k) = 1/k mod ℤ`. The cohomological side
is closed.

The **spectral-side companion claim** that the framework originally
carried — that the same `1/k` is encoded in the Galois phase of a
Stark unit (Paper 25 Conjecture 5, V-Hilbert 12) — has been tested
across three independent research notes (`188`, `267`, T7c) with
nine distinct candidate identifications. **Zero land on `1/k`.**
This file catalogues the six T7c candidates as kills with pattern
categories so the search engine for future work finds them.

---

## 2. The kill list

For every kill: **pattern category**, **scope**, **test record**,
**why it can't work (structural reason)**, and **what would have to
change to revisit**.

### K-T7c-1 — Raw Gauss-sum normalisation

**Claim killed**: `arg(exp(-L'(0, χ)) / τ(χ)) / (2π) mod 1 = 1/k`
and the companion `arg(L'(0, χ) / τ(χ))` where
`τ(χ) = Σ_{a mod N} χ(a) · e^{2πi·a/N}` is the Gauss sum.

**Pattern category**: `Discrete-continuous-mismatch` +
`Pointwise-evaluation-of-transcendental`.

**Scope**: Gauss-sum normalisation of the Stark-phase / L'(0,χ)
quantity, in any form where `τ(χ)` enters as a multiplicative
correction to a continuous phase.

**Test record**: 0 / 3 pass at `mp.dps = 50`, tolerance `1e-40`,
bridges `(5,13,3), (3,13,4), (7,19,6)`. See T7c §4 Candidate 1.

**Structural reason**: the Gauss sum `τ(χ)` for a primitive Dirichlet
character χ of modulus N is itself a transcendental complex number of
modulus `√N` (classical). Dividing one continuous transcendental
(`L'(0, χ)`) by another continuous transcendental (`τ(χ)`) does
not produce a rational `1/k` unless both transcendentals carry the
same arithmetic content — which is not the case here. Gauss sums
encode the conductor and the character evaluation, not the bridge
cocycle order.

**What would change the verdict**: only a theorem showing the
quotient is in `Q ∩ [0, 1)` and equals `1/k`, which research/267
already refutes numerically at 50 digits for all three bridges.

### K-T7c-2 — √N-normalised Gauss sum

**Claim killed**: `arg(exp(-L'(0, χ)) · √N / τ(χ)) / (2π) = 1/k`
(the unitary-normalised Gauss sum, with `|τ(χ)/√N| = 1` for
primitive χ).

**Pattern category**: same as K-T7c-1 — `Discrete-continuous-mismatch`.

**Scope**: any normalisation of the Gauss sum that preserves its
phase, including the unitary version that appears in the
functional-equation statement.

**Test record**: 0 / 3 pass.

**Structural reason**: the unitary normalisation rescales the modulus
to 1 but preserves the phase (which is the thing being tested).
Since the phase of `τ(χ)/√N` for primitive χ is the root number
`W(χ)` up to sign and `i^a` factors, and since `W(χ)`'s phase is
determined by Gauss-sum evaluations that are themselves transcendental
at the right branches, the unitary version is mathematically
equivalent to K-T7c-1 for this test.

**What would change the verdict**: same as K-T7c-1.

### K-T7c-3 — W-factor normalisation (both signs)

**Claim killed**: `arg(exp(-L'(0, χ)) · W(χ)^{±1}) / (2π) = 1/k`,
where `W(χ) = τ(χ) / (i^a · √N)` is the root number of the
L-function's functional equation, with `a = (1 - χ(-1))/2`.

**Pattern category**: `Discrete-continuous-mismatch` +
`Functional-equation-misapplication`.

**Scope**: any normalisation by the functional-equation root number.
Both signs of the W-factor are killed.

**Test record**: 0 / 6 pass (two sub-tests — `+1` and `-1` sign —
times 3 bridges). **Closest near-miss of the entire T7c verification**:
`Δ ≈ 5.4 × 10⁻³` on one bridge at k=4 with the `+1` sign. **Does not
extend to k=3 or k=6** — the near-miss is bridge-specific, not a
signal of a working rescue.

**Structural reason**: the W-factor is the multiplicative correction
that makes `Λ(s, χ) = ε(χ) · Λ(1-s, χ̄)` hold, where `Λ` is the
completed L-function. It absorbs the asymmetry of the Γ-factors and
the Gauss-sum phase. It is *not* a rational phase adjuster — its
value is a complex number of modulus 1 that encodes the functional
equation's symmetry, not the cocycle order of the character.

**What would change the verdict**: the closest near-miss at k=4
(`Δ ≈ 5.4 × 10⁻³`) is four orders of magnitude outside the 1e-40
tolerance and does not extend. A theorem relating `W(χ) · exp(-L'(0, χ))`
to a rational `1/k` would have to both explain the k=4 near-miss
structurally *and* show why the k=3 and k=6 bridges fall orders of
magnitude further from `1/k`. No such theorem is known.

### K-T7c-4 — Log-Stark rational approximation

**Claim killed**: `Im(log(ε_χ)) / (2π) ∈ 1/k + ℤ` within tolerance
`1e-40`, where `ε_χ = exp(-L'(0, χ))` is the Stark unit.

**Pattern category**: `Discrete-continuous-mismatch` +
`Transcendental-does-not-rationally-approximate`.

**Scope**: any test that asks whether the *continuous* imaginary
part of `log(ε_χ)` lands on a rational `p/k` for rational `p`.

**Test record**: 0 / 3 pass.

**Structural reason**: `log(ε_χ) = -L'(0, χ)` is a continuous
transcendental. Its imaginary part has no structural reason to
approximate a rational to 40 digits. Rational approximation is not
possible for generic transcendentals to infinite precision.

**What would change the verdict**: a proof that `L'(0, χ)` for the
three bridge characters is in fact a complex number with rational
imaginary part — which would be a structurally new result about
Stark L-values and has not been shown.

### K-T7c-5 — Genus-rescaled log-Stark

**Claim killed**: `log(ε_χ) / (2π i · log_N(g)) = 1/k`, where `g` is
the genus of the bridge field.

**Pattern category**: `Discrete-continuous-mismatch` +
`Ad-hoc-rescaling`.

**Scope**: any rescaling of the log-Stark quantity by field
invariants (genus, discriminant, regulator) in an attempt to land
on `1/k`.

**Test record**: 0 / 3 pass.

**Structural reason**: the genus of `Q(ζ_13)` is 0 (it is a genus-0
curve as an abelian extension of Q), so `log_N(g)` is ill-defined
or negative-infinity depending on convention. Even with an alternative
invariant substituted, no rescaling by a field invariant bridges the
discrete/continuous gap.

**What would change the verdict**: the identification of a *specific*
field invariant whose log produces exactly the right rescaling. No
candidate works in the tested set.

### K-T7c-6 — Combined Gauss sum + W-factor

**Claim killed**: `L'(0, χ) / (τ(χ) · W(χ)) = 1/k` up to phase
normalisation.

**Pattern category**: `Discrete-continuous-mismatch` +
`Cancellation-fallacy`.

**Scope**: attempts to cancel the Gauss sum and W-factor together
against `L'(0, χ)`, hoping the residual is rational.

**Test record**: 0 / 3 pass.

**Structural reason**: both the Gauss sum and the W-factor carry
phase information that is *not* the cocycle order. Combining them
does not cancel anything that leaves a rational residue. The hope
that "cancellation" produces rational output from two transcendentals
is a pattern we catalogue here as the **cancellation fallacy** —
it is not a theorem-like structure.

**What would change the verdict**: a theorem relating the product
`τ(χ) · W(χ)` to something computable from the cocycle order. No
such theorem is known.

### K-T7c-7 — Stickelberger element

**Claim killed**: `arg(θ(χ)) / (2π) = 1/k` where
`θ(χ) = Σ_{a=1}^{N-1} χ(a) · (a/N)` is the Stickelberger element.

**Pattern category**: `Exact-algebraic-value-does-not-equal-target` +
`Structural-vanishing`.

**Scope**: any test of whether the Stickelberger element's phase
(or any continuous derivative) encodes the bridge cocycle.

**Test record**: 0 / 3 pass, with **two interesting structural
by-products**:
- **k=3**: `θ(χ) = 0` exactly, forced by `χ(-1) = +1` for even
  characters of odd order (classical fact — Stickelberger elements
  for even characters vanish by the functional equation of the
  Bernoulli polynomials). The phase is undefined at 0; no match
  possible by vacuity.
- **k=4 and k=6**: `θ(χ)` computes to exact algebraic complex
  numbers — `-1 - i` (k=4) and `-1 - √3·i` (k=6). Their phases are
  `5/8` and `2/3` respectively, **neither equal to 1/4 or 1/6**.

**Structural reason**: Stickelberger elements are the "natural"
algebraic home of Stark-unit arguments, but they are valued in a
cyclotomic lattice, not in the cyclic group of the cocycle. Their
phases are determined by the character evaluation on `(a/N)` fractions,
not by the cocycle order of χ.

**What would change the verdict**: a theorem showing that the
*lattice class* of `θ(χ)` in the appropriate cyclotomic lattice
modulo the trace lattice *is* `1/k mod ℤ` for the three bridges.
This is closer in spirit to Option A of research/267 §6 (the
boundary-map direction) but is a structurally different test from
the pointwise phase evaluation tested here. **K-T7c-7 does not
foreclose the lattice-class version**; it only forecloses the
pointwise phase.

### K-T7c-8 — Conductor-adjusted phase

**Claim killed**: `arg(exp(-L'(0, χ))) / (2π) · (k/f(χ)) mod 1 = 1/k`
where `f(χ)` is the conductor of χ.

**Pattern category**: `Discrete-continuous-mismatch` +
`Ad-hoc-rescaling`.

**Scope**: rescaling the Stark phase by `k/f(χ)` or related
conductor-rational multiples.

**Test record**: 0 / 3 pass.

**Structural reason**: `k/f(χ)` is a rational multiplier but
multiplying a transcendental by a rational does not produce a
rational. The rescaling is numerically arbitrary.

**What would change the verdict**: no obvious path.

---

## 3. Pattern summary and the one unambiguous structural wall

Across the eight numbered kills (T7c tests six named candidates, two
of which have sub-tests, giving 10 sub-tests × 3 bridges = 30
numerical tests total in T7c §4), a **single pattern category
dominates**:

> **`Discrete-continuous-mismatch`**: the target is a discrete invariant
> (`1/k mod ℤ` in a finite cyclic group); the tested quantity is the
> continuous Galois phase / continuous log / continuous rescaling of
> a continuous transcendental. Pointwise evaluation of the continuous
> quantity cannot generically land on the discrete invariant without
> a theorem that forces it, and no such theorem is known for any of
> the tested identifications.

This is not a local-difficulty kill; it is a **structural wall**. The
wall has a name now: the **discrete-continuous mismatch** between the
cyclotomic Brauer cohomology side (where the cocycle lives) and the
L-function side (where Stark units live). The wall is not broken by
rescaling. It is not broken by normalisation. It is not broken by
functional-equation factors. It is not broken by exact algebraic
Stickelberger elements. These are the eight tests the framework has
run against the wall and none of them have crossed it.

**Future attempts to close Anchor 5's spectral side must operate by
a mechanism other than pointwise Galois-phase evaluation of an
L-function-derived quantity**. Candidate mechanisms that would
*not* hit this wall (but are not framework open problems after
the Conjecture 5 retraction):

- **(a) Cohomological boundary maps** — `δ : H¹(G, O_K*) → H²(G, ℤ)`
  applied to the *class* of the Stark unit, not its phase. The
  target of `δ` is naturally discrete. Would require computing the
  full Galois-module structure of the Stark unit, not just its norm
  or argument. Closed as framework work; open as general Hilbert 12.
- **(b) Beilinson regulator torsion** — the image of the Stark unit
  in the Beilinson regulator's lattice, with its torsion (finite
  part of the cokernel) being a discrete group that could in
  principle carry `1/k`. Closed as framework work; open as general
  Hilbert 12.
- **(c) Weil pairing on J₀(N)[k]** — a Weil pairing of k-torsion
  points on the Jacobian of the modular curve X₀(N) produces a
  bilinear form valued in `μ_k`, which is naturally discrete. Closed
  as framework work; open as general Hilbert 12.

**These three directions are not kills.** They are logically possible
mechanisms that have not been tested and cannot be tested with the
same methods as K-T7c-1 through K-T7c-8. They are also **not load-bearing
for the framework**. The framework claims Anchor 5 as the
cyclotomic-Brauer-side statement alone (per T7c §8 Option A). The
three directions (a), (b), (c) are logged here as *non-kills* so the
search engine distinguishes "tested and refuted" from "untested and
not a framework priority."

---

## 4. Cross-references

- **Paper 25 retraction (primary)**:
  `paper25/sections-05-08.md §8.0` — formal retraction notice for
  Conjecture 5 (V-Hilbert 12).
- **Paper 25 TOC**: `paper25/00-table-of-contents.md` — "four active
  conjectures + one retracted" framing.
- **Seven-anchor strategy (primary)**:
  `integers/paper12-cbb-system/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md §4 Anchor 5` —
  "Cyclotomic Brauer class, half-standing" restatement.
- **Strategy rationale (T7 retirement)**:
  `integers/paper12-cbb-system/relaxation/01-strategy-rationale.md` — T7 entry marked
  REFUTED with wave harvest note at top.
- **T7c full verification record**:
  `integers/paper12-cbb-system/relaxation/research/T7c-stark-rescue-verification.md` —
  30 numerical tests at mp.dps = 50, all FAIL.
- **T7c script**: `integers/paper12-cbb-system/relaxation/research/code/T7c-stark-rescue.py`.
- **Prior refutations**:
  `integers/paper12-cbb-system/research/188-character-decomposed-rbc.md` (L'(1,χ)/L(1,χ)),
  `integers/paper12-cbb-system/research/267-stark-units-computation.md` (raw Stark phase + exhaustive character scan).
- **Lead 7b hardening of the cohomology side**:
  `integers/paper12-cbb-system/relaxation/research/T1-T2-brauer-cohomology-verification.md` —
  4/4 cyclic Brauer classes verified.
- **Lead 7e hardening of Anchor 4 (minimality / forcing)**:
  `integers/paper12-cbb-system/relaxation/research/T7e-bridge-minimality-verification.md` —
  4/4 lex-unique minima in a zero-SM-input sieve.

---

## 5. Verdict

Anchor 5 is half-standing: **cyclotomic Brauer side verified exactly
(Lead 7b, 4/4); Stark-phase spectral side refuted in every form
tested to date (research/188, research/267, T7c eight named
candidates)**. The framework's contribution to Hilbert 12 via V's
matrix elements as Stark unit logarithms is formally retracted. The
bridge cocycle `1/k mod ℤ` exists in cyclotomic Brauer cohomology
alone. The framework's empirical content (36/36 master table,
Wolfenstein, `α_PS⁻¹ = 17`, cosmic age, Theoretical-Precision Table)
is unaffected.

*The credibility of the programme is the credibility of its kill
list. The kill list is now larger by eight.*
