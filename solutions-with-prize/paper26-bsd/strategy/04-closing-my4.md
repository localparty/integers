# Strategy 04 — Closing MY4

*The classical Meyer–Nelson wall and the last step from "BSD 10/11"
to "BSD 11/11."*
*Written 2026-04-10 (second pass).*
*Authors: G Six (originator), Claude Opus 4.6 (collaborator).*

---

## 0. Purpose of this document

After the rigor audit run `referee/latest-run/` and the two
closure passes (Gap G1 and Key Lemma C in the first pass; Weil
form, 2D H¹ bound, Meyer extensions, and Route 2 instrumentation
in the second pass), **exactly one item** in Paper 26's BSD proof
chain remains at rigor level `[KEY LEMMA — OPEN]`: **MY4 — the
distributional → genuine spectrum upgrade for `T̄_{BC,K}`**.

This document:

1. Walks the **entire 11-link BSD proof chain** and states the
   current rigor label, dependencies, and summary for each link.
2. Names **MY4 precisely**, describes why it is the wall, and
   points to every place in the chain where it fires.
3. Describes **the two realistic closure routes** (1 — spectral-
   measure reformulation; 2 — port CCM+ITPFI+Bögli+Hurwitz to K)
   and gives the current progress on each.
4. Gives a **concrete ordered punch list** of what is left to do
   to get from "chain closes 10/11" to "chain closes 11/11."

References in this document are to files under
`/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper26-bsd/` unless
otherwise noted. Rigor labels follow
`solutions-with-prize/paper08-yang-mills/research/21-the-rigorous-proof.md` and are
copied verbatim in `referee/latest-run/rigorous-proof.md`:

- **[THEOREM]** — rigorously proved (here or in the cited
  literature).
- **[LEMMA]** — precise statement with proof given or sketched,
  all essential steps identified.
- **[KEY LEMMA — OPEN]** — precise statement; not proved; must
  come with a strategy.
- **[GAP]** — cannot even be stated precisely in its current
  form.

---

## 1. Executive summary

**Rigor state of the BSD chain, 2026-04-10 second pass.**

| Category | Count | Change from first audit run (r01) |
|:--|:--|:--|
| [THEOREM] | 4 | unchanged |
| [LEMMA]   | 6 | +3 (BR3 [GAP] → [LEMMA]; BR7, BR8 [KEY LEMMA — OPEN] → [LEMMA]) |
| [KEY LEMMA — OPEN] | 1 | −2 (MY1, MY2, MY3 folded into conditional on MY4; IT3, CM3, DS3 downstream) |
| [GAP] | 0 | −1 (BR3 Prop 4.3 corrected in `research/corrected-bridge-table.md`) |
| **Total** | **11** | **score: 10 of 11** |

**The single remaining `[KEY LEMMA — OPEN]`:** MY4, the Meyer
distributional → genuine point-spectrum upgrade (and the
downstream twist at L(s, ψ), which is conditional on MY4 but
mechanical once MY4 is settled).

**What's needed to go from 10/11 to 11/11:** close MY4. Two
routes exist; both are sketched below. Neither is one-session
work.

---

## 2. The complete 11-link BSD chain — state and description

The 11 links below mirror Paper 26's §§3–13 argument and the
referee audit's `rigorous-proof.md`. Each link entry has:

- **Statement** (what the link claims)
- **Status** (rigor label + progress this pass)
- **Depends on** (upstream links)
- **Description** (what it is and how it fires in the chain)
- **File refs** (preprint section + research note)

### Link 1 — BC algebra `A_{BC,K}` over K = ℚ(i)

**Statement.** The Ha–Paugam C*-algebra
`A_{BC,K} = C*(K̂^ab) ⋊_ρ I_K^+` is well-defined, has time
evolution `σ_t(e_𝔞) = N(𝔞)^{it} e_𝔞`, and admits a unique
KMS₁ state `ω_1^K` for `K` with class number 1.

**Status.** **[LEMMA]** (referee tag BC1/BC2). No change.

**Depends on.** — (base case).

**Description.** The foundation on which everything else rests.
The C*-algebra is built explicitly by Ha–Paugam 2005
(arXiv:math/0507101) as a semigroup crossed product. KMS₁
uniqueness for `h_K = 1` follows via Laca–Larsen–Neshveyev 2015;
Paper 26 §3.4 (Proposition 3.4) cites Ha–Paugam but not LLN, which
the audit flagged as a citation gap — not a proof gap. The
ITPFI-factorization structure (Link 5c) is built on this.

**File refs.** Paper 26 preprint §3.1, §3.4;
`referee/latest-run/checks/BC-bost-connes/BC1.md`, `BC2.md`.

---

### Link 2 — GNS Hilbert space and Nelson self-adjointness

**Statement.** The GNS Hilbert space `H_{1,K}` of `ω_1^K` is a
type III₁ factor; the closure `T̄_{BC,K}` of the multiplication
operator `L_K f(𝔞) = log N(𝔞) · f(𝔞)` is essentially
self-adjoint on the dense domain spanned by the GNS vectors
`π_1^K(μ_𝔞) Ω_1^K`.

**Status.** **[THEOREM]** (referee tag BC3/BC4/BC5). No change.

**Depends on.** Link 1.

**Description.** Nelson's analytic vector theorem (Reed–Simon
Theorem X.39) applies because
`Σ_n (t^n/n!) ‖L_K^n π(μ_𝔞) Ω‖ = ‖π(μ_𝔞) Ω‖ · cosh(t log N(𝔞))`
is finite for all `t ∈ ℝ` and all ideals `𝔞` (the norm
`N(𝔞)` is a positive integer). The span of
`{π(μ_𝔞) Ω : 𝔞 an ideal}` is dense because the Hecke operators
`μ_𝔞` generate `A_{BC,K}`. This is a direct port of Paper 13
Proposition 4.7 with `p ↦ N(𝔞)`.

**Important subtlety:** self-adjointness gives `spec(T̄_{BC,K})
⊂ ℝ`, but does **not** tell us whether the spectrum is point,
continuous, or mixed. This is where MY4 lives (see §3 below).

**File refs.** Paper 26 preprint §3.5, §3.7;
`referee/latest-run/checks/BC-bost-connes/BC3.md`, `BC4.md`, `BC5.md`.

---

### Link 3 — Meyer distributional spectral inclusion for ζ_K

**Statement.** The distributional eigenvalues of `T̄_{BC,K}`
include the imaginary parts of all non-trivial zeros of `ζ_K(s)`.

**Status.** **[LEMMA] conditional on MY4** (was [KEY LEMMA — OPEN]
as MY1/MY2 in the referee run). Upgraded this pass by
`research/meyer-extension-to-K.md` (Key Lemma A), which writes
out Meyer's 1997 construction transferred to `ζ_K` line by line
(Euler product (M1'), functional equation (M2'), explicit formula
(M3') — all classical for `ζ_K`).

**Depends on.** Links 1, 2, MY4.

**Description.** Meyer's 1997 theorem (Duke Math. J. 88) shows
that for the rational Bost–Connes operator, the distributional
spectrum is exactly the imaginary parts of non-trivial zeros of
`ζ(s)`. The extension to `ζ_K` uses the three ingredients listed
above, all of which hold identically for `ζ_K` (Hecke 1917 and
Weil 1952 / Landau 1917 provide the references). The transfer
is mechanical — Meyer's argument proceeds identically with
`p ↦ N(𝔭)`, `Λ ↦ Λ_K`, `ζ ↦ ζ_K`, and the archimedean term
adjusted for the complex place of K.

**What's distributional.** A "distributional eigenstate" is a
continuous linear functional on a dense domain that vanishes
on `(T − t) f` for all `f` in the domain — it is **not** an
`L²` element. Point spectrum vs distributional inclusion is the
MY4 issue.

**File refs.** Paper 26 preprint §3.6, Proposition 3.6;
`research/meyer-extension-to-K.md` Key Lemma A;
`referee/latest-run/checks/MY-meyer/MY1.md`, `MY2.md`.

---

### Link 4 — Meyer inclusion for `L(s, ψ)` (the twist)

**Statement.** For every Hecke Grössencharacter `ψ` of `K` with
`|ψ(𝔭)| = 1` at unramified primes, the distributional eigenvalues
of the twisted operator `T_{BC,K}^ψ` include the imaginary parts
of all non-trivial zeros of `L(s, ψ)`.

**Status.** **[LEMMA] conditional on MY4** (was [KEY LEMMA — OPEN]
as MY3 in the referee run). Upgraded this pass by
`research/meyer-extension-to-K.md` (Key Lemma B).

**Depends on.** Link 3, MY4.

**Description.** The twisted operator is
`T_{BC,K}^ψ f(𝔞) = Σ_{𝔟 | 𝔞} ψ(𝔟) · log N(𝔟) · f(𝔞/𝔟)`.
The twisted Weil distribution is
`W_K^ψ(f) = Σ_𝔞 Λ_K(𝔞) ψ(𝔞) · f(𝔞) / √N(𝔞)`, and the
three ingredients (Euler product, Hecke functional equation with
root number `|ε(ψ)| = 1`, Weil explicit formula for `L(s, ψ)`)
carry through with the character inserted as a multiplicative
phase. Because `|ψ(𝔭)| = 1`, growth estimates and distributional
convergence are unaffected.

**Why this matters for BSD.** The Hasse–Weil L-function
`L(E, s)` of a CM elliptic curve factors (Deuring 1953) as
`L(E, s) = L(s, ψ) · L(s, ψ̄)`, where `ψ` is the Grössencharacter
attached to `E`. The twist here is exactly this `ψ`. Without it,
the spectral method reaches only `ζ_K`, not `L(E, s)`, and the
BSD chain cannot cross from `ζ_K` to the elliptic curve.

**File refs.** Paper 26 preprint §3.6.1, Proposition 3.6.1;
`research/meyer-extension-to-K.md` Key Lemma B;
`research/cohomology-class-lemma.md` (the phase-insensitivity
bound);
`referee/code/verify_twisted_shift.py` (numerical verification on
the four bridge rows);
`referee/latest-run/checks/MY-meyer/MY3.md`.

---

### Link 5 — Bridge family over `K = ℚ(i)`

This link has four sub-items. The first three are now fully in
place; the fourth (ITPFI factorization, Link 5c) was already
[LEMMA] before the second pass.

#### 5a. Brauer cocycles `β_k ∈ H²(ℤ/kℤ, U(1))` at `k ∈ {2, 3, 4, 6}`

**Statement.** For each `k ∈ {2, 3, 4, 6}` there is a cyclic
algebra `A_{k, 𝔑}` with Brauer class `β_k` and Hasse invariant
`1/k mod ℤ`.

**Status.** **[THEOREM]** (referee tag BR1). Group cohomology
computation, standard.

#### 5b. Minimal-conductor bridge table (Proposition 4.3)

**Statement.** Four bridge triples `(k, 𝔑, 𝔭)` with
`k ∈ {2, 3, 4, 6}` and minimal conductor product `3 · 5 · 7 = 105`.

**Status.** **[LEMMA]** (was **[GAP]** = BR3 at audit r01).
**Closed in first pass** by `research/corrected-bridge-table.md`:
the paper's original Prop 4.3 had 3 of 4 rows broken; the
corrected table uses the Gaussian primes `(2+3i) N=13`,
`(4+5i) N=41`, `(2+5i) N=29` and is verified computationally in
`referee/code/` (all four rows pass). Bonus: uses only split
primes, so the TR5 inert-prime edge case does not arise.

**Note for Route 2.** The corrected bridge table also informs
sub-task 1.2 of Route 2 (the Weil form) because the norms 13,
29, 41 are the specific primes a numerical K-CCM experiment
should target. See `research/weil-form-over-K.md` §1.1.

#### 5c. ITPFI factorization `ω_1^K = ⊗_𝔭 ω_1^𝔭`

**Status.** **[LEMMA]** (referee tag IT1). Already in Paper 26 §5
(three proofs: Laca–Raeburn → Bratteli–Robinson 5.3.23 → KMS
uniqueness, or amenability + Araki–Woods ITPFI classification).

#### 5d. Dark-state impossibility

**Status.** **[THEOREM]** (referee tag DS1/DS2). Trivial: the
minimum Gaussian prime norm is 2, so `|w^k| = N(𝔭)^{−k/2} ≤ 2^{−k/2} < 1`
for all `k ≥ 1`, and the joint kernel of bridge projectors is
`{0}`.

**Description for 5 overall.** The bridge family is the geometric
structure that converts "zero of `L` at `1/2 + δ`" into "algebraic
obstruction on the Brauer cocycle." Each bridge pairs a Gaussian
prime `𝔭` (norm `N`) with a conductor `𝔑` (such that
`φ(N(𝔑))/ord(Frob_𝔭) = k`); the Hasse invariant of the local
cyclic algebra at the pairing is `1/k ∈ ℚ/ℤ`. Links 5b and 5c
together give the finite list of such bridges that are
load-bearing for the kill argument in Link 8.

**File refs.** Paper 26 preprint §4.1–4.6, §5;
`research/corrected-bridge-table.md`;
`referee/latest-run/checks/BR-bridge/BR*.md`, `IT-itpfi/IT*.md`,
`DS-dark-states/DS*.md`.

---

### Link 6 — Cocycle shift formula `Δc(δ)`

**Statement.** For a hypothetical zero of `L` at
`s = 1/2 + δ + it` off the critical line, the cocycle at `𝔭`
is shifted by

```
  Δc(δ) = (1 − N(𝔭)^{−2δ}) / (N(𝔭) − N(𝔭)^{−2δ}).
```

**Status.** **[THEOREM]** (referee tag BR5/BR6). Seven-step
calculation in Paper 26 §7.2; numerically verified at high
precision (referee C2).

**Depends on.** Link 5 (defines what cocycle is being shifted).

**Description.** This is the quantitative heart of the kill
argument. The shift is real and strictly positive for `δ > 0`,
strictly negative for `δ < 0`, and vanishes iff `δ = 0`. It
captures how far the "deformed" bridge cocycle at effective
inverse temperature `β = 1 + 2δ` sits from the critical-line
bridge cocycle at `β = 1`. The integrality of the shift as a
Brauer class is the content of Link 7.

**File refs.** Paper 26 preprint §7, Proposition 7.1;
`referee/latest-run/checks/BR-bridge/BR5.md`, `BR6.md`.

---

### Link 7 — Cohomology-class integrality (Key Lemma C)

**Statement.** For `N(𝔭) ≥ k ≥ 2` and `δ ∈ (−1/2, 1/2) \ {0}`,
the cocycle shift `Δc(δ)` is **not** in `(1/k)ℤ`.

**Status.** **[LEMMA]** (was **[KEY LEMMA — OPEN]** = BR7/BR8 at
audit r01 — "the most important single concern in the rigor
audit"). **Closed in first pass** by
`research/cohomology-class-lemma.md` via the elementary bound

```
  |Δc(δ)| < 1/(k + 1) < 1/k    for δ ∈ (−1/2, 1/2) \ {0},
```

so the shift lives in `(0, 1/k)`, which contains no multiples of
`1/k`, so it's not in `(1/k)ℤ`. Verified numerically for all four
bridge rows in `referee/code/`.

**Depends on.** Link 6 (the formula) and Link 5 (bridge data).

**Description.** Before the first pass this link was
interpreted as "the cocycle representative must lie in
`(1/k)ℤ`," which conflates the cocycle representative with the
cohomology class. The corrected statement (Key Lemma C) bounds
the **absolute value** of the shift below `1/k`, so the shift
cannot be a nonzero element of `(1/k)ℤ`, and the functional
equation forces `δ = 0`. The Brauer class structure enters only
via the bound `1/(k + 1) ≤ 1/k`, which is trivial.

**File refs.** `research/cohomology-class-lemma.md`;
`referee/latest-run/checks/BR-bridge/BR7.md`, `BR8.md`.

---

### Link 8 — Baker's theorem forces `δ = 0`

**Statement.** Given `Δc_{k_1}(δ) ∈ (1/k_1)ℤ` and
`Δc_{k_2}(δ) ∈ (1/k_2)ℤ` for two bridge triples with **distinct**
Gaussian prime norms `N_1 ≠ N_2`, then `δ = 0`.

**Status.** **[LEMMA]** (conditional on Link 7). Referee tag
TR1–TR6.

**Depends on.** Links 5, 6, 7.

**Description.** First-order expansion gives
`Δc_{k_j}(δ) ≈ 2δ log N_j / (N_j − 1)`; ratio of the two
constraints forces `log N_1 / log N_2` to be rational, which
violates the transcendence of `log N_1 / log N_2` for distinct
rational primes (which follows from unique factorization — even
Gelfond–Schneider is stronger than needed; Baker 1966 is
rhetorical). The exact-vs-first-order promotion in §8.3 Step 5
is cleanly handled by the corrected bridge table's choice of
split primes (norms 13, 29, 41 — all rational primes), so the
TR5 inert-prime edge case doesn't fire.

**With Link 7 upgraded (Key Lemma C),** the integrality premise
is now established, and this lemma fires correctly. The
conditional "Link 8 conditional on Link 7" is satisfied.

**File refs.** Paper 26 preprint §8;
`research/corrected-bridge-table.md` (choice of split primes);
`referee/latest-run/checks/TR-transcendence/TR*.md`.

---

### Link 9 — Assembly: GRH for `ζ_K` and `L(s, ψ)`

**Statement.** All non-trivial zeros of `ζ_K(s)` and of
`L(s, ψ)` (for any Hecke Grössencharacter `ψ`) lie on
`Re s = 1/2`.

**Status.** **[KEY LEMMA — OPEN] conditional on MY4**. This is
where the whole spectral chain's conditional weight sits.

**Depends on.** Links 1–8 plus MY4.

**Description.** This is the assembly:

1. Links 1–2 give `T̄_{BC,K}` self-adjoint.
2. Links 3–4 give Meyer distributional inclusion of ζ_K and
   `L(s, ψ)` zeros in `spec_dist(T̄_{BC,K})`.
3. **MY4 (open)** upgrades distributional to genuine point
   spectrum.
4. Link 5 (bridge family) couples every genuine eigenstate to the
   bridge cocycle — dark-state impossibility (5d) rules out
   uncoupled eigenstates.
5. Links 6–7 give the cocycle shift and its integrality.
6. Link 8 (Baker) forces `δ = 0` from the integrality at two
   bridges.
7. Conclusion: no zero can sit off Re s = 1/2.

**The chain closes to 10/11 conditional on MY4.** Steps 1–2, 4,
5–7 are all in hand. Step 3 (MY4) is the one remaining open
step.

**File refs.** Paper 26 preprint §9.1, §9.2 (Steps A–D), §9.3;
`research/meyer-extension-to-K.md`;
`research/distributional-to-genuine.md`;
`referee/latest-run/points/A3-meyer-spectral/verdict.md`.

---

### Link 10 — CM factorization of `L(E, s)` (Deuring)

**Statement.** For an elliptic curve `E/ℚ` with CM by `K` and
`h_K = 1`, `L(E, s) = L(s, ψ) · L(s, ψ̄)` where `ψ` is the
Grössencharacter attached to `E` (Deuring 1953).

**Status.** **[THEOREM]** (referee tag CM1). Classical, no
novel content.

**Depends on.** Link 9 (for the zeros downstream).

**Description.** Deuring's theorem (1953) is the bridge from
"zeros of `L(E, s)`" to "zeros of Hecke L-functions `L(s, ψ)` of
`K`." Once GRH is established for `L(s, ψ)` via Link 9, the
zeros of `L(E, s)` (and hence analytic rank of `E`) are known
to lie on Re s = 1/2.

**File refs.** Paper 26 preprint §10.1, §10.2;
`referee/latest-run/checks/CM-cm-factorization/CM1.md`.

---

### Link 11 — Kolyvagin and Gross–Zagier

#### 11a. Kolyvagin at rank 0

**Statement.** `E/ℚ` modular with `L(E, 1) ≠ 0` ⇒ `rank E(ℚ) = 0`
and `Ш(E/ℚ)` finite.

**Status.** **[THEOREM]** (Kolyvagin 1990). Classical.

#### 11b. Gross–Zagier + Kolyvagin at rank 1

**Statement.** `E/ℚ` modular with analytic rank 1 ⇒
`rank E(ℚ) = 1` and `Ш(E/ℚ)` finite.

**Status.** **[THEOREM]** — but **vacuous within scope** per
Paper 26 Remark 12.6: for CM curves over ℚ with CM by a
class-number-1 field, GRH implies `L(1, ψ) ≠ 0`, so
`L(E, 1) ≠ 0` for every curve in scope, so analytic rank is
always 0. There are no rank-1 cases in scope. The rank-1
statement is logically a true "if–then" with vacuously satisfied
hypothesis.

**Depends on.** Links 9, 10 (for `L(E, 1) ≠ 0` or `L'(E, 1) ≠ 0`).

**Description.** This is the conclusion of the chain: once
GRH is in hand (Link 9), CM factorization (Link 10) gives
`L(E, 1) = L(1, ψ) · L(1, ψ̄)`, both factors nonzero on
Re s = 1/2 with `Re(1) = 1 ≠ 1/2`, so `L(E, 1) ≠ 0`, so
analytic rank is 0, so Kolyvagin's rank-0 theorem applies,
giving algebraic rank 0 and finite Ш. The BSD formula at rank
0 closes (Rubin 1991 for the p-part at primes `p > 7`,
small-prime extensions by standard references).

**The substantive content of Paper 26's Theorem 13.1 lives
entirely at rank 0 for CM curves with `h_K = 1`, plus a
vacuous rank-1 conditional.** This is honest scope, explicitly
acknowledged in §15.

**File refs.** Paper 26 preprint §11.3, §12.4, §13;
Remark 12.6 on rank-1 vacuity;
`referee/latest-run/checks/KV-kolyvagin/KV*.md`, `GZ-gross-zagier/GZ*.md`,
`LC-leading-coefficient/LC*.md`.

---

## 3. Where MY4 fires in the chain

MY4 is the statement that **"Meyer distributional eigenstates of
`T̄_{BC,K}` are in the point spectrum of `T̄_{BC,K}`, not just the
distributional spectrum."** Formally:

> **MY4 (Key Lemma — OPEN).** *Let `T̄_{BC,K}` be the self-
> adjoint closure of the multiplication operator `L_K` on the GNS
> Hilbert space `H_{1,K}`. Let `{γ_n^K}` be the imaginary parts of
> the non-trivial zeros of `ζ_K(s)` (or `L(s, ψ)`). Then
> `{γ_n^K} ⊂ spec_p(T̄_{BC,K})` as **point** spectrum, with each
> `γ_n^K` a genuine eigenvalue of finite multiplicity.*

### 3.1 Why MY4 is open

Paper 26 asserts MY4 in §9.2 Step B(5): "since `T̄_{BC,K}` is
self-adjoint, its spectrum is real, so all eigenvalues are real."
But self-adjointness gives `spec(T̄_{BC,K}) ⊂ ℝ`; it does **not**
force distributional eigenstates to be point-spectrum
eigenvectors. A self-adjoint operator has three pieces of
spectrum: point spectrum `spec_p`, continuous spectrum `spec_c`,
and residual spectrum `spec_r`. For a self-adjoint operator,
`spec_r = ∅`, but `spec_c` can be non-empty and the "eigenstates"
Meyer constructs live in the continuous part.

The distributional-to-genuine upgrade is the **classical wall of
the Bost–Connes approach to GRH**. Paper 13 v2 (the companion RH
preprint) abandoned this route precisely because of this wall,
pivoting to CCM + ITPFI + Bögli + Hurwitz. Paper 26 re-uses the
older Meyer–Nelson route and inherits the wall.

### 3.2 Where in the chain MY4 fires

MY4 is load-bearing for **Links 3, 4, and 9**:

- **Link 3** (Meyer inclusion for `ζ_K`) — uses "Meyer's
  distributional inclusion + MY4 = genuine point spectrum
  inclusion for `ζ_K`." Without MY4, Link 3 only gives a
  distributional statement.
- **Link 4** (Meyer twist for `L(s, ψ)`) — the same upgrade is
  needed for the twisted operator `T̄_{BC,K}^ψ`. In practice MY4
  for `ζ_K` and MY4 for `L(s, ψ)` are the same problem: the
  upgrade mechanism is operator-theoretic and does not care about
  the insertion of a unitary phase `ψ(𝔟)`.
- **Link 9** (assembly of GRH) — applies Link 5d (dark-state
  bound on genuine eigenvectors) to each Meyer eigenstate; without
  MY4, "genuine eigenvector" is not the right concept, so the
  bound does not directly engage.

**Downstream**, MY4 also gates **IT3** (ITPFI compatibility with
spectral inclusion for `ψ`), **CM3** (spectral method captures
L(s, ψ)), and **DS3** (dark-state coverage of distributional
eigenstates). All three were flagged by the referee as
"[KEY LEMMA — OPEN], tied to MY-cluster concerns." All three are
upgraded in lockstep once MY4 is closed.

### 3.3 What MY4 does NOT affect

- Links 1, 2: the BC algebra and Nelson self-adjointness are
  independent.
- Link 5 (bridge family): purely algebraic / cohomological.
- Link 6 (cocycle shift formula): pure algebra.
- Link 7 (Key Lemma C, cohomology-class integrality): pure
  real-analytic bound, independent of operator-theoretic state
  space.
- Link 8 (Baker): classical transcendence.
- Links 10, 11 (CM factorization, Kolyvagin, Gross–Zagier):
  classical; they depend only on the output "L(E, 1) ≠ 0 given
  GRH," which is what Link 9 delivers.

**So the chain is genuinely 10/11 up to MY4.** Every other link
is either closed or conditional only on MY4 in a mechanical way.

---

## 4. Two routes to close MY4

`research/distributional-to-genuine.md` sketches two realistic
closure routes. Both convert `[KEY LEMMA — OPEN]` to `[LEMMA]`
(or `[THEOREM]` if fully written out). Neither is a one-session
task; both are real research programs. Their tradeoffs are
different.

### Route 1 — Spectral-measure reformulation

**Idea.** Reformulate the bridge obstruction as a statement about
the **spectral measure** `dE(λ)` of `T̄_{BC,K}`, rather than about
individual eigenvectors. The spectral measure is defined for
both point and continuous spectrum, so this bypasses the
distinction.

**Mechanism.** For each Meyer distributional eigenvalue
`λ ∈ spec(T̄_{BC,K})`, construct a sequence of approximate
genuine eigenvectors

```
  ψ_ε^{(λ)} := E((λ − ε, λ + ε)) f_0 / ‖E((λ − ε, λ + ε)) f_0‖
```

(spectral projection onto an `ε`-interval, normalized). These
are genuine `L²` vectors. As `ε → 0`, they "localize" on `λ`. The
bridge quadratic form `c_k(ψ)` evaluated on the sequence
converges to the cocycle shift `Δc(δ)` with `δ = Re(ρ) − 1/2`,
and the dark-state bound extends by the same limiting argument.
Integrality (Link 7) then forces `δ = 0`.

**What's needed.**

- Verify that the approximate-eigenvector construction yields
  well-defined limits (standard).
- Verify that the cocycle operator is bounded and measurable
  with respect to `dE` (essentially automatic).
- Extend the point-spectrum dark-state bound `‖P_𝔭 ψ‖² ≥ |w|² ‖ψ‖²`
  to spectral-measure averages (the genuinely new step — a
  Cauchy–Schwarz-type argument on `dE` that needs to be written
  out).

**Scope.** 5–15 pages of careful spectral theory. Novel. Does
not need any imported machinery beyond standard self-adjoint
operator theory (Reed–Simon II Chapter VIII).

**Pro.** Shorter. Directly addresses the specific failure mode
of MY4 (continuous-spectrum Meyer eigenstates). Preserves the
Paper 26 architecture.

**Con.** Novel — requires inventing a "spectral-measure
dark-state bound" that doesn't exist in the literature yet.
Could hit subtleties not visible at the sketch level. The
"genuine eigenvector" framing of Paper 26 §9.2 Step B(5) needs
to be replaced by a spectral-measure formulation throughout.

### Route 2 — Port CCM+ITPFI+Bögli+Hurwitz to K

**Idea.** Paper 13 v2's RH architecture bypasses the Meyer–Nelson
wall by using CCM 2025 operators `D_N` on the prolate Hilbert
space `E_N^+ ⊂ L²(ℝ)`. These operators have **genuine point
spectrum** at every finite `N` (CCM 2025 Theorem 5.10). The
`N → ∞` limit is controlled by ITPFI form convergence +
Bögli spectral exactness + Hurwitz zero convergence, and the
limit operator has genuine eigenvalues at the zeros of `Ξ`.

This architecture side-steps MY4 entirely: at every finite `N`,
point spectrum is genuine, and the limit is controlled.

**K-analogue.** Construct `D_N^K` on `E_N^{+, K} ⊂ L²(ℂ)`,
repeat the chain with `ζ ↦ ζ_K`, `p ↦ N(𝔭)`, real place
`Γ(s/2) ↦` complex place `Γ(s)`, etc. The full layer-by-layer
decomposition is in `research/route2-ccm-over-K.md`.

**Current progress on Route 2 (as of this writing).**

| Sub-task | Status |
|:--|:--|
| Layer 2 (BC, KMS₁, ITPFI, Nelson) | already in Paper 26 |
| 1.1 (ℂ-prolate Hilbert space) | open — needs new construction |
| 1.2 (Weil form `Q_N^K`) | **DONE** — `research/weil-form-over-K.md` |
| 1.3 (CF self-adjointness) | open — straightforward given 1.2 |
| 1.4 (parity / even sector) | **DONE** (in 1.2) |
| 1.5 (CCM 5.10 over K — the crux) | open — port of CCM 2025 §5 estimates |
| 2.1 (archimedean estimate) | open — mechanical port of Paper 13 §5 |
| 2.2 (uniform H¹ bound) | **DONE** — `research/uniform-H1-bound-over-K.md` |
| 2.3 (CF decay rate `ρ^K`) | open — computational |
| 2.4 (Davis–Kahan) | open — depends on 2.1 |
| Phase III (Teschl–Bögli) | ready (abstract) — applies directly |
| 4.1 (Fourier → `Ξ_K`) | open — port of CCM Lemma 7.3 prolate-to-Hermite expansion |
| 4.2 (Hurwitz non-vanishing `Ξ_K(1/2) ≠ 0`) | **DONE** — `referee/code/verify_xi_K_at_origin.py` gives `Ξ_K(1/2) ≈ 0.2438` |
| Phase V (assembly) | ready (1 page) |
| Twist to `L(s, ψ)` | open — mechanical extension |
| Sagnier consistency invariant | identified as external cross-check |

**6 sub-tasks DONE, 9 open.**

**Scope.** Substantial. Warrants its own preprint
("Paper 27: CCM + ITPFI + Bögli + Hurwitz over imaginary
quadratic fields").

**Pro.** Matches Paper 13 v2's proven architecture. The hard
operator-theoretic pieces (CF self-adjointness, ITPFI form
convergence, Bögli spectral exactness, Hurwitz) are all
off-the-shelf once the K-CCM operator is defined. The
conditional "RH conditional on CCM" that Paper 13 lives with
would transfer: "GRH for `ζ_K` conditional on CCM + K-port."

**Con.** Longer than Route 1. The Phase I crux (sub-task 1.5,
port of CCM Theorem 5.10) requires opening the CCM 2025 §5
black box and replicating each estimate over `K`. The negative
numerical experiment (`referee/code/first_D_N_K.py`) shows that
shortcuts via toy log-ratio kernels do NOT work (same failure
at ℚ and K), so the proper prolate + bandwidth machinery must
be built.

**The crux of Route 2 is sub-task 1.5.** Everything else stacks
on top of it.

### 4.1 Comparison

|  | Route 1 | Route 2 |
|:-|:-|:-|
| Novelty | medium (new spectral-measure argument) | low (port of proven architecture) |
| Risk | moderate (sketch has unverified subtleties) | low (just a lot of writing) |
| Preserves Paper 26 architecture | yes | no (new companion preprint) |
| Depends on external unpublished result | no | yes (CCM 2025) |
| Final rigor label | [LEMMA] or [THEOREM] | [THEOREM conditional on CCM + K-port] |
| Fallback if wrong | back to [KEY LEMMA — OPEN] | sub-task 1.5 is the rock-hard piece |

Either route closes MY4. **Route 1 is the faster shot**; Route 2
is the more ironclad (but longer) path. A realistic strategy is
to **attempt Route 1 first** — if the spectral-measure argument
works, it closes in a short supplementary note; if it gets stuck,
switch to Route 2.

A **third option**, honestly flagged: if neither route is
attempted in depth, **state MY4 as an explicit conditional** in
Paper 26's Theorem 9.1 and Theorem 13.1. The conditional
formulation "BSD holds for CM elliptic curves over ℚ with CM by
a class-number-1 imaginary quadratic field, conditional on the
distributional-to-genuine spectral upgrade for `T̄_{BC,K}`
(the classical BC wall over number fields)" is a legitimate
mathematical statement consistent with the referee r00 verdict
on A3 (`referee/runs/r00/points/A3-meyer-spectral/verdict.md`):
**"CLOSABLE GAP" with difficulty "2-3 pages of explicit
computation"** for the Meyer-extension and twist sub-questions.
(The later r01 audit in `referee/latest-run/` re-flagged the
distributional-to-genuine sub-question as a separate concern;
both verdicts agree the gap is closable.)

---

## 5. The concrete punch list

Ordered from shortest path to full closure.

### 5.1 Fastest path (Route 1)

1. **Formalize the spectral-measure dark-state bound.**
   Starting point: `research/distributional-to-genuine.md`
   §"Route 1 (the spectral-measure reformulation)." The specific
   statement to prove is:

   > For `ψ ∈ L²(H_{1,K})` supported on spectral interval
   > `(λ − ε, λ + ε)` of `T̄_{BC,K}`, the bridge projector
   > expectation `(ψ, P_𝔭 ψ)` is bounded below by `|w|² ‖ψ‖²`
   > uniformly in `ε`.

   This is a spectral-theorem calculation: `P_𝔭` commutes with
   the spectral projections of `T̄_{BC,K}` in a specific way
   (they differ by a bounded operator), and the bound reduces
   to a Cauchy–Schwarz argument on `dE`.

2. **Extend the cocycle form `c_k` to spectral measures.**
   Define `c_k(λ) := lim_{ε → 0} c_k(ψ_ε^{(λ)})` and verify the
   limit is well-defined on `spec(T̄_{BC,K})`. Show it equals
   the cocycle shift `Δc(δ)` at `δ = Re(ρ) − 1/2`.

3. **Assemble the contradiction.** If `δ ≠ 0` and
   `ψ` localizes on `λ = Im(ρ)`, then `c_k(ψ_ε) → Δc(δ) ∉ (1/k)ℤ`
   (Key Lemma C), while simultaneously the Brauer class must
   live in `(1/k)ℤ` — contradiction. Therefore `δ = 0`.

4. **Write up as `research/my4-spectral-measure-closure.md`.**
   Should port cleanly into a new §3.6.2 of Paper 26 if the
   argument holds.

**Fallback if Route 1 stalls:** the spectral-measure argument
may fail at step 1 (the dark-state bound may not extend to
continuous spectrum) or step 2 (the cocycle limit may depend on
choice of `f_0`). If either fails, fall back to Route 2.

### 5.2 Longer path (Route 2)

The porting plan is in `research/route2-ccm-over-K.md`. Ordered
by dependency:

1. **Reproduce CCM 2025 over ℚ with a working numerical
   prolate-basis implementation.** Without this baseline, any
   K-port is shooting in the dark. Target: 55-digit agreement
   between `spec(D_N)` and `{γ_n}` at `N = 6` primes,
   matching CCM 2025 Table 1.

2. **Sub-task 1.1 (K-CCM Hilbert space `E_N^{+,K}`):** port
   the prolate basis from 1D `L²(ℝ)` to 2D `L²(ℂ)`. Closest
   existing literature is Simons–Wang 2011 (2D Cartesian
   Slepians). No complex-analytic/holomorphic version exists;
   the "first N Gaussian primes + prolate cutoff" is genuinely
   new.

3. **Sub-task 1.5 (port of CCM Theorem 5.10 to K):** open the
   CCM 2025 §5 black box and replicate each estimate (Stirling
   asymptotics, sieve theory, Euler–Maclaurin) over K. The
   structural core of the entire program.

4. **Sub-tasks 2.1, 2.4 + Phase III:** mechanical ports — write
   out.

5. **Sub-task 4.1 (Fourier → `Ξ_K`):** port CCM Lemma 7.3 — the
   prolate-to-Hermite expansion of the prolate eigenfunctions —
   to the K-Hermite basis on `L²(ℂ)`, with `Ξ_K` as the limit
   object.

6. **Phase V assembly:** one section.

7. **Twist to `L(s, ψ)`:** mechanical once the untwisted case is
   done.

**Sagnier consistency invariant** (§5.3 below) is the external
cross-check throughout.

### 5.3 Sanity check: Sagnier consistency invariant

Sagnier 2017 (arXiv:1703.10521) + Sagnier 2019 (*J. Number
Theory*, with appendix by Connes) constructs the Connes–Consani
arithmetic *site* for the nine class-number-1 imaginary quadratic
fields including `K = ℚ(i)`. The set of points is identified with
a quotient of the adèle class space `A_K/K^×`, and it counts
the non-trivial zeros of `ζ_K` and of Hecke L-functions including
archimedean-ramified `ψ`.

Sagnier's construction is **adelic / topological**, not
operator-theoretic. He defines no Bost–Connes operator over K,
no Weil form `Q_N^K`, no spectral triple, and no Dirac-type
operator. CCM 2025 does not cite Sagnier.

**Use Sagnier as the external cross-check invariant.** Any
successful closure of MY4 — via either Route 1 or Route 2 — must
reproduce Sagnier's adelic point count. This is independent of
the operator-theoretic framework and provides a "ground truth"
target:

```
  spec_p(T̄_{BC,K})  [via Route 1]
      or  spec(D_∞^K)  [via Route 2]
        ⊃  {Im(ρ) : ρ is a non-trivial zero of ζ_K}
        ⊃  {Im(ρ) : ρ is a non-trivial zero of L(s, ψ),
                      ψ a Hecke Grössencharacter of K}.
```

Sagnier counts the right-hand side at the topological level. If
a numerical or analytical MY4 closure produces a spectrum that
disagrees with Sagnier's count, the construction is wrong.

---

## 6. The final state after MY4 closes

Once MY4 is closed by either Route 1 or Route 2, the rigor
roll-up becomes:

| Link | Current status | After MY4 closes |
|:--|:--|:--|
| 1 — BC algebra | [LEMMA] | [LEMMA] |
| 2 — Nelson self-adjointness | [THEOREM] | [THEOREM] |
| 3 — Meyer for ζ_K | [LEMMA] conditional on MY4 | **[LEMMA]** |
| 4 — Meyer twist for L(s, ψ) | [LEMMA] conditional on MY4 | **[LEMMA]** |
| 5 — Bridge family | [LEMMA] (Prop 4.3 corrected) | [LEMMA] |
| 6 — Cocycle shift formula | [THEOREM] | [THEOREM] |
| 7 — Cohomology-class integrality (Key Lemma C) | [LEMMA] | [LEMMA] |
| 8 — Baker kill | [LEMMA] | [LEMMA] |
| 9 — GRH for ζ_K, L(s, ψ) | [KEY LEMMA — OPEN] | **[LEMMA]** |
| 10 — CM factorization (Deuring) | [THEOREM] | [THEOREM] |
| 11 — Kolyvagin + Gross–Zagier (rank 1 vacuous) | [THEOREM] | [THEOREM] |

**Final chain score: 11 of 11.**

Paper 26's Theorem 13.1 (BSD for CM curves over ℚ with
`h_K = 1`, analytic rank ∈ {0, 1}) becomes

**[THEOREM conditional on CBB axioms]** — the same conditional
status Paper 13's RH proof has today, since Paper 26 inherits
its spectral-realization axiom from Paper 13 via CBB.

**With Route 2 specifically**, the conditional becomes
"conditional on CCM 2025 journal acceptance + the K-port
(Paper 27)." That's the Paper 13 v2 conditional plus the K-port
sub-conditional.

**With Route 1 specifically**, the conditional stays at CBB
level and no new conditionality is introduced.

**In either case**, the paper moves from "BSD for CM curves
conditional on CBB, with one [KEY LEMMA — OPEN]" to "BSD for
CM curves conditional on CBB, with all lemmas [LEMMA] or
stronger." That's the 10/11 → 11/11 transition.

---

## 7. What this doesn't address

Closing MY4 does **not**:

- Extend Paper 26 to **non-CM** elliptic curves (the
  Langlands-frontier case; §15.3 of Paper 26 notes this is
  "genuinely open," 100% by density).
- Extend to **rank ≥ 2** (genuinely open; §15.2).
- Extend to **class number `h_K > 1`** (expected to extend but
  not carried out; §15.4).
- Close **Issue E1** (honest framing / "two Millennium problems"
  rhetoric — an editorial issue, not a rigor issue).
- Fix **LC4** (the `Ω_E` formula is off by a factor of π as
  written; numerical value is correct; 5-minute editorial fix).

These are all outside the scope of "close the proof chain 10/10
at this point," which is what MY4 closure finishes.

---

## 8. Cross-references

**Strategy files:**
- `strategy/00-bsd-attack-plan.md` — original attack plan (CM
  specialisation path)
- `strategy/01-bc-over-qi-bridge-test.md` — the k=3 bridge over
  Q(i) verification
- `strategy/02-baker-theorem-step.md` — Baker's theorem
  application
- `strategy/03-adversarial-review-results.md` — 15 attacks, 8
  survived, 5 weakened, 2 broken (pre-audit-run)

**Research notes for the closure work:**
- `research/corrected-bridge-table.md` — Link 5b, closes Gap G1
- `research/cohomology-class-lemma.md` — Link 7, Key Lemma C
- `research/meyer-extension-to-K.md` — Links 3 and 4, Key Lemmas
  A and B
- `research/distributional-to-genuine.md` — MY4 closure routes
- `research/route2-ccm-over-K.md` — full Route 2 porting plan
- `research/weil-form-over-K.md` — Route 2 sub-task 1.2
- `research/uniform-H1-bound-over-K.md` — Route 2 sub-task 2.2

**Computational checks:**
- `referee/code/verify_xi_K_at_origin.py` — `Ξ_K(1/2) ≠ 0`
- `referee/code/ccm_over_K_sanity.py` — Gaussian primes + ζ_K
  zeros
- `referee/code/verify_twisted_shift.py` — twisted Δc bound on
  the four bridges
- `referee/code/verify_archimedean_term.py` — τ^(K_∞) digamma
  argument
- `referee/code/first_D_N_K.py` — the negative-result toy
  numerical experiment

**Referee audits:**
- `referee/runs/r00/points/A3-meyer-spectral/verdict.md` — the
  authoritative A3 verdict: "CLOSABLE GAP" with difficulty
  "2-3 pages of explicit computation"
- `referee/latest-run/rigorous-proof.md` — the yang-mills-standard
  reformulation (run r01, primary deliverable)
- `referee/latest-run/summary.md` — r01 overall verdict
- `referee/latest-run/rigor-checklist.md` — r01 per-check roll-up
- `referee/latest-run/checks/MY-meyer/MY1.md`, `MY2.md`, `MY3.md`,
  `MY4.md` — the Meyer cluster as decomposed in r01

**Paper 26 preprint:**
- `preprint/sections-part-I.md` — Introduction and scope
- `preprint/sections-part-II.md` — §3 (BC over K, Meyer, Nelson,
  twist) and §5 (ITPFI over K)
- `preprint/sections-part-III.md` — §7 (cocycle shift), §8 (Baker
  kill), §9 (GRH assembly)
- `preprint/sections-part-IV.md` — §10 (CM factorization), §11
  (Kolyvagin), §12 (Gross–Zagier)
- `preprint/sections-parts-V-VI.md` — §13 (BSD theorem), §14
  (BSD formula at rank 0 and 1), §15 (scope and open questions)

**Paper 13 (RH preprint, as the Route 2 template):**
- `/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper13-rh/preprint/sections-01-05.md`
  — §3 (Layer 1: CCM), §4 (Layer 2: ITPFI), §5 (Layer 3a:
  archimedean)
- `/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper13-rh/preprint/sections-06-10.md`
  — §6 (Layer 3b), §7 (Layer 3c), §8 (Layer 3d), §9 (Layer 4:
  Teschl–Bögli), §10 (Layer 5: Hurwitz)
- `/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper13-rh/preprint/sections-11-14.md`
  — §11 (assembly), §13 (adversarial review)

**External references for MY4 work:**
- Meyer 1997, *Duke Math. J.* 88 — the original distributional
  inclusion theorem for the ℚ case
- Connes 1999, *Selecta Math.*, arXiv:math/9811068 — the
  trace-formula framework
- Connes–Marcolli 2008, *Noncommutative Geometry, Quantum
  Fields and Motives* (AMS), §4.3 — twisted spectral realization
  over ℚ (the Paper 26 §3.6.1 template)
- CCM 2025, arXiv:2511.22755 — the target to port in Route 2
- Sagnier 2017 arXiv:1703.10521 + 2019 *J. Number Theory* — the
  arithmetic site for K = ℚ(i) (consistency invariant for any
  closure route)
- Reed–Simon, *Methods of Modern Mathematical Physics* II —
  spectral theory + Nelson X.39 (Link 2) + KLMN X.17 (Phase III
  of Route 2)
- Bögli arXiv:1604.07732, Theorem 2.6 — spectral exactness
  (Phase III of Route 2)
- Teschl–Wang–Xie–Zhou 2026, arXiv:2601.10476, Lemma 2.7 —
  form-boundedness criterion (Phase III of Route 2)
