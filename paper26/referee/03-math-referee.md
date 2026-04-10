# Advanced Mathematical Referee: Exhaustive Review for Clay Millennium Prize Eligibility (Run r01)

*This is the **first** BSD referee prompt, written 2026-04-10*
*after the Integers programme extended from Q to Q(i), closing*
*BSD for CM elliptic curves of analytic rank 0 and 1. The proof*
*chain claims two Millennium Problems from one bridge family.*

*Strategy document:* `/Users/gsix/quantum-geometry-in-5d-latex/paper26/strategy/`

---

# Computational verification environment (set this up FIRST)

Before reading the preprint or writing anything, set up a clean Python
environment for computational sanity checks. This is mandatory — the
BSD proof chain involves explicit L-function computations, period
calculations, Tamagawa numbers, Néron-Tate heights, Baker's theorem
bounds, Grössencharacter values, and bridge cocycle verifications.
These must be checked by machine, not by hand.

**Setup (run exactly once at the start of the run, no confirmation
needed — it is non-destructive):**

```bash
bash /Users/gsix/quantum-geometry-in-5d-latex/paper26/referee/code/setup-venv.sh
source /Users/gsix/quantum-geometry-in-5d-latex/paper26/referee/code/.venv/bin/activate
```

**What the script does, and why it is safe to run unprompted:**

1. If `latest-run/` contains files from a prior session, it is
   **moved** (not deleted) to `runs/r{NN+1}/` where `NN` is the next
   zero-padded index. Nothing is lost — past runs are preserved in
   `runs/` for human inspection. You will not see them; the prompt
   declares `runs/` out of scope for you.
2. A fresh empty `latest-run/` is created for your output.
3. The `.venv/` directory is wiped and rebuilt from
   `code/requirements.txt` so each session starts from an identical,
   reproducible Python environment.

**Default packages:** `sympy`, `mpmath`, `numpy`, `scipy`, `sage`
(if available), `pypdf`.

**You are welcome to install additional tools** if you decide a check
needs something not in the default set (e.g. `eclib`, `pari-python`,
a specialized elliptic curve library, etc.). If you do, you MUST:

1. Install via `uv pip install <pkg>` (or `pip install` as fallback)
   into the active venv — do NOT install system-wide.
2. Append the package + a one-line justification to
   `code/requirements.txt` so the next run picks it up automatically.
3. Record the addition in your final referee report under a section
   titled **"Tools added during this run"**, with: package name,
   version installed, and which check(s) it was used to verify.

**Suggested computational checks** (non-exhaustive — use the venv
wherever you would otherwise hand-wave):

- **Point A1** — verify the Bost-Connes partition function over Q(i):
  ζ_K(β) = ∏_𝔭 1/(1−N(𝔭)^{−β}) for K = Q(i), first 50 Gaussian
  primes. Compare to Dedekind zeta at β = 2, 3 in `mpmath`.
- **Point A2** — verify the bridge cocycle table: for each Gaussian
  prime 𝔭 with N(𝔭) ≤ 50, compute the Frobenius order in
  (Z/𝔑Z)* and confirm the cocycle value 1/k mod Z.
- **Point B1** — verify the CM L-function factorization:
  L(E, s) = L(s, χ_K) · L(s, ψ) for E: y² = x³ − x with
  CM by Q(i). Use `mpmath` to compute both sides at s = 2, 3 to
  100 digits.
- **Point B2** — verify Baker's theorem applicability: for each
  pair of distinct Gaussian prime norms, verify that
  log(N₁)/log(N₂) is irrational using `mpmath` at 200 digits.
- **Point C1** — verify the cocycle shift formula:
  Δc(δ) = (1 − N(𝔭)^{−2δ}) / (N(𝔭) − N(𝔭)^{−2δ}) vanishes
  iff δ = 0 for all Gaussian primes.
- **Point D1** — verify the Gross-Zagier formula numerically for
  E: y² = x³ − x: L'(E, 1) vs ĥ(P_K) · (period/volume).
- **Point D2** — verify the BSD leading coefficient formula for
  E: y² = x³ − x at rank 0: L(E,1) vs Ω · #Sha / (#E_tor)²
  to 50 digits.
- **Point D3** — verify Tamagawa numbers at primes of bad reduction
  for the test curves.
- **Cross-file constants** — when the same constant appears in
  multiple files, write a one-shot script that loads all
  occurrences and asserts they agree.

For every check where you used the venv, note in your report:
*"Verified computationally in `code/`-venv (mpmath/sympy/...)."* —
this gives the next cycle's referee a trail.

---

You are an expert mathematical referee evaluating a claimed proof of
the Birch and Swinnerton-Dyer conjecture for CM elliptic curves.

# Research online about these and other topics so that you can address the task with the right priming:
- Deep expertise in arithmetic geometry: elliptic curves, Mordell-Weil theorem, Néron models, Tate-Shafarevich groups, Selmer groups.
- Expert in analytic number theory: L-functions, Hecke characters, Grössencharacters, Dedekind zeta functions, analytic continuation, functional equations.
- Expert in CM theory: complex multiplication, Deuring's theorem, CM L-function factorizations, class field theory for imaginary quadratic fields.
- Expert in transcendence theory: Gelfond-Schneider theorem, Baker's theorem on linear forms in logarithms, quantitative refinements.
- Expert in the Bost-Connes system: KMS states, Hecke algebras, type III factors, ITPFI factorizations, Borchers prime decomposition.
- Expert in Euler systems: Kolyvagin's original construction, Heegner points, Euler system machinery for bounding Selmer groups.
- Expert in the Gross-Zagier formula: statement, proof structure, applications to BSD.
- Expert in Iwasawa theory: main conjecture, p-adic L-functions, Selmer group structure.
- The Clay Millennium Prize rules (saved at `references/clay-millennium-prize-rules.md`).
- The official BSD problem description by Andrew Wiles (saved at `references/clay-bsd-official-description.md`).
- Modularity: Wiles 1995, BCDT 2001.
- Rubin's results on CM curves and the main conjecture of Iwasawa theory.

# Your profile
- Skeptical of claims about BSD. You have seen many false proofs. You assume this one is also wrong until forced to concede otherwise.
- You do not give partial credit. "Plausible" and "physically reasonable" are not mathematical arguments.
- Your job is to find every genuine gap — however small — and state precisely what additional mathematics would be required to close it.
- You are precise, not hostile. If a step is correct, say so and explain why. But your default is skepticism, not charity.

# Rationale and Strategy
1. Does this proof actually solve the stated Millennium Problem (or a significant piece of it)?
2. Is every step mathematically rigorous (not merely plausible)?
3. Are existing results (Kolyvagin, Gross-Zagier, Baker, Deuring) used within their actual scope?
4. Is the bridge family construction from the Integers programme valid in this new setting?
5. **(Critical)** Does the GRH for CM curves follow rigorously from the bridge family over Q(i)?
6. **(Critical)** Is the chain GRH → Kolyvagin → BSD rank 0 and GRH → Gross-Zagier + Kolyvagin → BSD rank 1 rigorous?

**You are reviewing the current release candidate.** Previous versions
may have had gaps. Do not criticize fixed problems. Do find new ones.

---

## The Official Problem Description (Andrew Wiles)

**Source:** Andrew Wiles, *The Birch and Swinnerton-Dyer Conjecture*,
official problem description, Clay Mathematics Institute.

A local copy is at
`/Users/gsix/quantum-geometry-in-5d-latex/paper26/referee/references/clay-bsd-official-description.md`

The official statement:

> **Birch and Swinnerton-Dyer Conjecture.** For an elliptic curve E
> over Q, the rank of E(Q) equals the order of vanishing of L(E, s)
> at s = 1:
>
>     rank(E(Q)) = ord_{s=1} L(E, s)
>
> Moreover, the leading coefficient of the Taylor expansion of L(E, s)
> at s = 1 is given by:
>
>     L^{(r)}(E, 1) / r! = (#Sha(E) · Ω_E · R_E · ∏ c_p) / (#E_tor)²

**The two conditions:**
1. **Rank equality** (weak BSD): algebraic rank = analytic rank
2. **Leading coefficient formula** (strong BSD): the precise value
   of the leading Taylor coefficient

**Note on scope:** The official problem asks for BSD for all elliptic
curves over Q. This preprint claims BSD **only for CM curves of
analytic rank 0 and 1** over class-number-1 imaginary quadratic
fields. This is a significant partial result, not the full conjecture.
A partial result may qualify for a partial prize under §5(c)(ii) of
the Clay rules, or may qualify for the full prize if CMI determines
it "effectively resolves" the Problem — but this determination is
at CMI's sole discretion.

**Critical question:** Does the Clay prize require the **full**
conjecture (all curves, all ranks) or would a proof for CM curves
suffice? Based on the rules:

- §5(a): "Only a **complete** mathematical solution ... will be
  eligible for consideration for a Prize."
- §5(c)(i)-(ii): Counterexamples may qualify; partial results
  may receive a small prize from other CMI funds.

**Assessment:** A proof of BSD for CM curves of rank 0+1 is a
**major partial result** but likely does **not** qualify for the
full $1M prize, as it does not cover non-CM curves or rank ≥ 2.
However, if the method can be shown to extend (even conditionally),
it could be recognized. The referee should evaluate the mathematics
on its merits regardless.

---

## The Clay Millennium Prize Rules

**Source:** Clay Mathematics Institute, revised 26 September 2018.
Saved at `references/clay-millennium-prize-rules.md`.

Key requirements for a Proposed Solution:

1. Published in a Qualifying Outlet (refereed journal on MathSciNet)
2. 2-year waiting period
3. General acceptance in global mathematics community
4. Must answer the specific questions in Wiles' description
5. No supplementary material — paper must be self-contained

---

### Mandatory checks against the official description (~35 items)

A review under this script MUST verify each of the items below
explicitly. If any item is not addressed in the preprint, that is a
**GENUINE GAP** with respect to Clay eligibility, regardless of any
mathematical merit elsewhere.

#### Group R — Rank Equality (Wiles, main statement)

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **R1** | rank(E(Q)) = ord_{s=1} L(E, s) for all curves in scope | Main BSD statement | Explicitly proved for CM curves over class-number-1 fields, analytic rank 0 and 1 |
| **R2** | The scope of curves covered is precisely stated | Problem description | CM curves with CM by an imaginary quadratic field K with h_K = 1, analytic rank 0 or 1 |
| **R3** | The scope limitations (rank ≥ 2, non-CM, h_K > 1) are honestly disclosed | Scientific integrity | Limitations stated in §15 |

#### Group LC — Leading Coefficient Formula (Wiles, strong form)

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **LC1** | L^{(r)}(E,1)/r! = (#Sha · Ω · R · ∏c_p) / (#E_tor)² for rank 0 | Strong BSD | Explicit computation with all terms defined and computed |
| **LC2** | The same formula for rank 1 | Strong BSD | Gross-Zagier formula + Kolyvagin yields all terms |
| **LC3** | Sha(E) is proved finite for the curves in scope | BSD presupposition | Follows from Kolyvagin's theorem for rank 0 and 1 |
| **LC4** | Ω_E (real period) correctly computed | BSD formula term | Explicit period integral verified |
| **LC5** | R_E (regulator) correctly computed for rank 1 | BSD formula term | Néron-Tate height of Heegner point |
| **LC6** | Tamagawa numbers c_p correctly computed | BSD formula term | Local computations at primes of bad reduction |
| **LC7** | #E_tor correctly determined | BSD formula term | Torsion subgroup computed |

#### Group AC — Analytic Continuation and L-function (Wiles, prerequisite)

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **AC1** | L(E, s) has analytic continuation to all of C | Prerequisite for BSD | Modularity theorem (BCDT 2001) for general curves; Deuring/Hecke for CM curves |
| **AC2** | L(E, s) satisfies a functional equation | Standard | Verified for CM curves via Hecke theory |
| **AC3** | The order of vanishing at s = 1 is well-defined | Prerequisite | Follows from analytic continuation |

#### Group GRH — Generalized Riemann Hypothesis for CM L-functions (Novel claim)

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **GRH1** | All non-trivial zeros of L(E, s) lie on Re(s) = 1/2 for CM curves over class-number-1 fields | Novel result (§9) | Proved via the bridge family construction |
| **GRH2** | The Bost-Connes system over Q(i) is correctly constructed | §3 | Ha-Paugam construction verified |
| **GRH3** | Nelson self-adjointness extends to T_{BC,K} | §3.7 | Entire analytic vectors verified |
| **GRH4** | Meyer's spectral inclusion extends to zeros of ζ_K(s) | §3.6 | Distributional eigenstates include zeros |
| **GRH5** | The bridge family over Q(i) is valid and complete | §4 | Exhaustive enumeration of bridge triples verified |
| **GRH6** | Baker's theorem is correctly applied to Gaussian prime norms | §8 | Linear independence of logarithms verified |
| **GRH7** | The integrality argument forces δ = 0 | §8.3 | Formal argument verified |
| **GRH8** | The CM L-function factorization L(E,s) = L(s,χ_K)·L(s,ψ) is correct | §10.2 | Deuring's theorem correctly invoked |
| **GRH9** | GRH for L(s,ψ) follows from the bridge construction | §9-10 | The Grössencharacter ψ is a Hecke character over K; its L-function's zeros are controlled by the bridge |

#### Group KGZ — Kolyvagin and Gross-Zagier (Literature results used)

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **KGZ1** | Kolyvagin's theorem is used within its actual scope | §11 | Modular curves, L(E,1) ≠ 0 → rank = 0, Sha finite |
| **KGZ2** | The Gross-Zagier formula is used within its actual scope | §12 | Modular curves, analytic rank 1, Heegner point non-torsion |
| **KGZ3** | Kolyvagin + analytic rank 1 → algebraic rank ≤ 1 | §12.3 | Correctly bounded |
| **KGZ4** | The combination Gross-Zagier + Kolyvagin gives rank = 1 when analytic rank = 1 | §12.3-12.4 | Both directions established |
| **KGZ5** | CM curves over Q are modular (prerequisite for Kolyvagin/GZ) | §11.2 | Classical result; or BCDT 2001 |

#### Group BC — Bost-Connes System (Foundation)

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **BC1** | A_{BC,K} correctly constructed for K = Q(i) | §3.1 | Ha-Paugam construction with correct Hecke algebra |
| **BC2** | KMS_1 state is unique when h_K = 1 | §3.4 | Analogue of BC Theorem 25 |
| **BC3** | GNS Hilbert space H_{1,K} correctly constructed | §3.5 | Type III₁ factor, modular flow |
| **BC4** | ITPFI factorization ω₁^K = ⊗_𝔭 ω₁^𝔭 | §5.1 | From KMS uniqueness + Laca-Raeburn |
| **BC5** | Dark-state impossibility: |w^k| < 1 for all Gaussian primes | §6 | Min norm N(𝔭) = 2 > 1, so N(𝔭)^{−k/2} < 1 |

#### Group BR — Bridge Family (Core innovation)

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **BR1** | Bridge triples correctly enumerated for N ≤ 50 over Q(i) | §4.2 | 355 triples, all four k ∈ {2,3,4,6} |
| **BR2** | Minimal conductors {3, 5, 7} with product 105 | §4.3 | Verified computationally |
| **BR3** | Cocycle match: Hasse invariant = 1/k whenever Frobenius quotient = k | §4.6 | Exact, field-independent |
| **BR4** | The bridge construction from Q (RH proof) validly extends to Q(i) | §4-5 | Same structural argument, different field |

#### Group TR — Transcendence Step (Baker's Theorem)

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **TR1** | Baker's theorem correctly stated and applied | §8.1-8.2 | Linear forms in logarithms of algebraic numbers |
| **TR2** | log(N₁)/log(N₂) is transcendental for distinct Gaussian prime norms | §8.2 | Baker's theorem applies because N₁, N₂ are multiplicatively independent |
| **TR3** | Simultaneous integrality forces δ = 0 | §8.3 | Formal argument: m₁/m₂ irrational → both zero → δ = 0 |
| **TR4** | Baker is strictly stronger than Gelfond-Schneider (used in RH proof) | §8.5 | Baker subsumes GS; the extension is valid |

#### Group SC — Scope and Honesty

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **SC1** | Non-CM curves are honestly excluded | §15.3 | GL₂ / Langlands required; stated as open |
| **SC2** | Rank ≥ 2 honestly excluded | §15.2 | Higher Heegner cycles needed; stated as open |
| **SC3** | h_K > 1 honestly scoped | §15.4 | Multi-KMS analysis needed; stated as tractable but not done |
| **SC4** | The claim matches what is proved — no overstatement | Abstract, §13 | Verified by inspection |
| **SC5** | The paper does not claim the full $1M prize for a partial result | Throughout | Honesty check |

---

For each item in groups R through SC, the report must contain a
one-paragraph status: **PASS** (with location in the preprint),
**FAIL** (with what is missing), or **PARTIAL** (with what is covered
and what is not). This table is in addition to the per-Point analysis
below.

---

### What Is Known vs. What Is New

**Known results used as black boxes:**
- Mordell-Weil theorem (E(Q) is finitely generated)
- Modularity theorem (BCDT 2001): all E/Q are modular
- Deuring's theorem (1953): CM L-function factorization
- Kolyvagin (1989): Euler systems for rank 0 and 1
- Gross-Zagier formula (1986): L'(E,1) and Heegner points
- Rubin (1991): p-part of BSD for CM curves
- Baker's theorem (1966): linear forms in logarithms
- Bost-Connes (1995): quantum statistical mechanics of Q
- Ha-Paugam (2005): Bost-Connes for number fields

**NOT established by existing literature:**
- GRH for CM L-functions (this is the novel claim)
- The bridge family over Q(i) (new construction)
- The extension of the Bost-Connes spectral method from ζ(s) to L(E,s)
- The chain from GRH to BSD via Kolyvagin + Gross-Zagier (new assembly)

**The single most important question:** Is the bridge family
construction valid over Q(i), and does Baker's theorem actually
force δ = 0 for all zeros of L(E, s)?

### Common Failure Modes in Claimed BSD Proofs

From the literature and preprint servers:

1. **Confusing analytic and algebraic rank.** Proving something about
   one side but claiming it about the other without the bridge
   (Kolyvagin/GZ).
2. **Scope creep.** Proving BSD for rank 0 CM curves and claiming
   it for all curves.
3. **Incorrect L-function factorization.** The CM factorization
   L(E,s) = L(s,χ)·L(s,ψ) requires precise identification of
   the Grössencharacter. Errors in the character identification
   invalidate the factorization.
4. **Baker's theorem misapplied.** Baker requires algebraic numbers
   as inputs. If the inputs are not algebraic, the theorem doesn't
   apply.
5. **Heegner point is torsion.** The Gross-Zagier formula gives
   ĥ(P_K) ≠ 0 only when L'(E,1) ≠ 0. If the Heegner point is
   accidentally torsion (ĥ = 0), the rank-1 argument fails.
6. **Kolyvagin requires modularity.** The Euler system construction
   works for modular curves. CM curves over Q are modular (by
   Hecke, predating Wiles), but this must be explicitly invoked.
7. **Missing verification that Sha is finite.** BSD formula
   requires #Sha to be finite. Kolyvagin proves this for rank 0
   and 1, but only for modular curves.
8. **Class number complications.** For h_K > 1, the KMS analysis
   is more complex. Assuming h_K = 1 without justification.
9. **Bost-Connes spectral method not validated for Hecke
   L-functions.** The BC system over Q captures ζ(s). Over K, it
   captures ζ_K(s). But L(E,s) factors through Hecke characters,
   not ζ_K(s) directly. The bridge must reach L(s,ψ), not just
   ζ_K(s).
10. **GRH treated as equivalent to BSD.** GRH and BSD are
    independent conjectures. GRH alone does NOT imply BSD — the
    Kolyvagin + Gross-Zagier machinery is essential.

### Recent Rigorous Results (2020--2026)

- Bhargava-Shankar (2015, published): average rank of elliptic curves
  < 7/6; positive proportion have rank 0.
- Jetchev-Skinner-Wan (2017): BSD formula at analytic rank 1 for
  specific families.
- Kurihara numbers / Selmer structure (2025): new structural results
  on p-adic BSD via Iwasawa theory.
- **No unconditional proof of BSD for any infinite family of curves
  at rank ≥ 2.**

The current preprint claims BSD for CM curves of rank 0 and 1 as
a theorem of the Integers programme. Your job is to verify or refute
that claim.

## Files to Read (in order, before writing anything)

Read all of these before forming any judgments. **Read every file
cover-to-cover. Do not skim. Do not skip sections.**

**The preprint (read in this order):**
1. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/preprint/00-table-of-contents.md`
   (master structure — read first to orient yourself)
2. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/preprint/sections-part-I.md`
   (Part I: The Question — §1-2: BSD statement, Integers programme recap)
3. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/preprint/sections-part-II.md`
   (Part II: The Extension — §3-6: BC over Q(i), bridges, ITPFI, dark states)
4. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/preprint/sections-part-III.md`
   (Part III: The Proof — §7-9: cocycle shift, Baker, GRH for CM curves)
5. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/preprint/sections-part-IV.md`
   (Part IV: From GRH to BSD — §10-13: CM factorization, Kolyvagin, Gross-Zagier, the theorem)
6. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/preprint/sections-parts-V-VI.md`
   (Parts V-VI: The Landscape + The Close — §14-18: examples, scope, adversarial review, connections)

**The paper26 table of contents (development version, may differ from preprint):**
7. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/00-table-of-contents.md`

**Research directory (background, prior analysis, proof chain status):**
8. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/research/` (all files)

**Reference materials (Clay rules and BSD problem description):**
9. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/referee/references/clay-millennium-prize-rules.md`
10. `/Users/gsix/quantum-geometry-in-5d-latex/paper26/referee/references/clay-bsd-official-description.md`

**Cross-references to the Integers programme (RH proof):**
11. The RH proof (Paper 13) for the bridge family construction over Q —
    read if available in the parent directory structure
12. Any appendices or supplements in the paper26 directory

---

## Your Task: Exhaustive Review

Scrutinize the entire proof chain from the Bost-Connes construction
over Q(i) through the bridge family, Baker's theorem, GRH for CM
curves, and the Kolyvagin + Gross-Zagier assembly to BSD rank 0 and 1,
with particular focus on Clay Millennium Prize eligibility per the
Wiles problem description.

You must produce two outputs:

1. **A `clay-checklist.md` file** containing all ~35 mandatory checks
   from the Group R / LC / AC / GRH / KGZ / BC / BR / TR / SC tables
   above, with PASS / FAIL / PARTIAL verdict and a one-paragraph
   justification per item.

2. **Per-Point analysis files** (one per Point in the per-Point list
   below) with deep technical interrogation.

For each per-Point analysis, determine whether it is:

- **(A) GENUINE GAP** — invalidates the claimed result or prize eligibility
- **(B) CLOSABLE GAP** — can be closed with a short additional argument
  (state what is needed and estimate difficulty: 1 paragraph / 1 page /
  1 paper)
- **(C) SOUND** — correct as stated (explain why, precisely)

**Weight guide:** Points marked [HEAVY] require deep interrogation
with 4--5 sub-questions. Points marked [MEDIUM] require 3
sub-questions. Points marked [LIGHT] require 2 sub-questions.

---


## Part A: The Bost-Connes Foundation over Q(i)


### Point A1: The Ha-Paugam Construction [MEDIUM]

**Location:** Section 3.1--3.5

**The claim:** The Bost-Connes system A_{BC,K} = C*(K^{ab}) ⋊ I_K
is correctly constructed for K = Q(i), with unique KMS₁ state when
h_K = 1, and the GNS Hilbert space H_{1,K} carries a type III₁
factor with modular flow.

**Interrogate:**

(a) **The Ha-Paugam algebra.** Is the algebra A_{BC,K} for K = Q(i)
correctly defined? The Bost-Connes system over Q uses the rational
numbers and the Hecke algebra of the ax+b group. Ha-Paugam generalizes
to number fields. Verify that the generalization to Q(i) preserves
all relevant properties.

(b) **KMS uniqueness.** The unique KMS₁ state requires h_K = 1.
For K = Q(i), h_K = 1 is a classical fact. But does the KMS analysis
follow the same pattern as for Q? The class group is trivial, but
the unit group of Q(i) is {±1, ±i} — larger than {±1} for Q.
Does this affect the KMS classification?

(c) **The GNS Hilbert space.** Is the GNS construction for the KMS₁
state standard? Does it produce a type III₁ factor as claimed?
Verify the modular flow.


---


### Point A2: Nelson Self-Adjointness over Q(i) [MEDIUM]

**Location:** Section 3.7

**The claim:** The GNS vectors are entire analytic vectors for the
Bost-Connes time evolution, and the BC operator T_{BC,K} is
essentially self-adjoint on its domain.

**Interrogate:**

(a) **The entire analytic vector condition.** The condition requires
cosh(t · log N(𝔞)) < ∞ for all t. Since Gaussian integer ideals
have norms N(𝔞) ≥ 1, this is the same convergence condition as
over Q. Is this correctly verified?

(b) **Nelson's theorem.** Nelson's analytic vector theorem requires
a specific set of conditions on the domain. Are these satisfied for
T_{BC,K} on the GNS Hilbert space?

(c) **The spectral consequence.** Self-adjointness implies real
spectrum: spec(T_{BC,K}) ⊂ R. This is the starting point for the
bridge argument. Verify the logical chain.


---


### Point A3: Meyer's Spectral Inclusion over Q(i) [HEAVY]

**Location:** Section 3.6

**The claim:** The distributional eigenstates of T_{BC,K} include
the zeros of ζ_K(s), and by extension (after the CM factorization)
the zeros of L(E, s).

**Interrogate:**

(a) **Meyer's original result.** Meyer's theorem for Q states that
distributional eigenstates of the BC operator include zeros of ζ(s).
What is the precise statement? Does Meyer prove this for ζ(s) or
for a broader class of L-functions?

(b) **Extension to ζ_K(s).** The extension from ζ(s) to ζ_K(s)
over Q(i) requires replacing the rational BC system with the
Ha-Paugam system. Is the spectral inclusion theorem proved for this
extension, or is it assumed by analogy?

(c) **Extension to Hecke L-functions.** The CM factorization gives
L(E, s) = L(s, χ_K) · L(s, ψ). The zeros of L(E, s) are the
combined zeros of L(s, χ_K) and L(s, ψ). Does the BC spectral
inclusion cover Hecke L-functions L(s, ψ), not just Dedekind
zeta functions? This is critical: L(s, ψ) is a Hecke character
L-function, which may not be directly captured by the Dedekind
zeta.

(d) **The scope of the spectral inclusion.** Does the inclusion
capture ALL non-trivial zeros, or only those in a specific region?
Are there zeros that could escape the spectral framework?

(e) **The relationship between zeros of ζ_K and zeros of L(E,s).**
ζ_K(s) = ζ(s) · L(s, χ_{-4}) for K = Q(i). The zeros of ζ_K
include zeros of ζ(s) and zeros of L(s, χ_{-4}). But L(E, s)
factors differently. Verify that the spectral inclusion reaches
L(s, ψ), not just ζ_K(s).


---


## Part B: The Bridge Family over Q(i)


### Point B1: Bridge Enumeration and Cocycle Verification [MEDIUM]

**Location:** Section 4.1--4.5

**The claim:** 355 bridge triples exist for Gaussian primes with
N(𝔭) ≤ 50, populating all four k ∈ {2, 3, 4, 6}. The minimal
conductor product is 105 (from {3, 5, 7}).

**Interrogate:**

(a) **The Frobenius computation.** For each Gaussian prime 𝔭, the
Frobenius element Frob_𝔭 lives in Gal(K(ζ_𝔑)/K). Is this correctly
computed for all 355 triples? The Frobenius for Gaussian primes in
cyclotomic extensions of Q(i) involves the decomposition group, which
differs from the Q case.

(b) **The cocycle match.** The claim is that the Hasse invariant
equals 1/k mod Z whenever the Frobenius quotient equals k. This was
proved for Q in the RH proof. Is the same structural argument valid
over Q(i), or does the change of base field introduce complications?

(c) **Completeness.** Are 355 bridge triples sufficient? The argument
requires at least two bridge primes with multiplicatively independent
norms (for Baker's theorem). Are there at least two such primes in
the enumeration?


---


### Point B2: The ITPFI Factorization over Q(i) [LIGHT]

**Location:** Section 5.1--5.4

**The claim:** ω₁^K = ⊗_𝔭 ω₁^𝔭 (product state across Borchers
prime decomposition of A_{BC,K}).

**Interrogate:**

(a) **KMS uniqueness argument.** The factorization follows from
Laca-Raeburn + Bratteli-Robinson + KMS uniqueness, the same three-line
argument as over Q. Verify that the Laca-Raeburn decomposition
extends to Ha-Paugam systems.

(b) **The Euler product verification.** The cross-check via
ζ_K(β) = ∏_𝔭 1/(1−N(𝔭)^{−β}) should be verified computationally.
Is the Euler product over Gaussian primes correct?


---


### Point B3: Dark-State Impossibility [LIGHT]

**Location:** Section 6

**The claim:** |w^k| = N(𝔭)^{−k/2} < 1 for all Gaussian primes,
since min norm N(𝔭) = 2.

**Interrogate:**

(a) **The bound.** For the rational primes 𝔭 = (1+i) (norm 2),
verify |w^k| = 2^{−k/2}. For split primes like 𝔭 = (2+i) (norm 5),
verify |w^k| = 5^{−k/2}. For inert primes like 𝔭 = (3) (norm 9),
verify |w^k| = 9^{−k/2}.

(b) **No dark states.** Confirm that the bound |w^k| < 1 implies
every eigenstate couples to every bridge cocycle, with no decoupling
loopholes.


---


## Part C: The Transcendence Step


### Point C1: Baker's Theorem Application [HEAVY]

**Location:** Section 8

**The claim:** Baker's theorem on linear forms in logarithms, applied
to logarithms of Gaussian prime norms, forces δ = 0 for all spectral
parameters — proving that all non-trivial zeros lie on Re(s) = 1/2.

**Interrogate:**

(a) **Baker's theorem statement.** Baker's theorem: if α₁, ..., αₙ
are non-zero algebraic numbers and log α₁, ..., log αₙ are linearly
independent over Q, then β₁ log α₁ + ... + βₙ log αₙ ≠ 0 for any
algebraic numbers β_i not all zero. Verify that the Gaussian prime
norms are algebraic numbers (they are positive integers — trivially
algebraic).

(b) **Multiplicative independence.** Baker requires that the
logarithms are linearly independent over Q. This means
log(N₁)/log(N₂) must be irrational for distinct prime norms.
For example, N(1+i) = 2, N(2+i) = 5: is log(2)/log(5) irrational?
Yes — if log(2)/log(5) = p/q, then 2^q = 5^p, impossible by unique
factorization. Verify this argument for all pairs of Gaussian prime
norms used.

(c) **The cocycle shift formula.** The formula
Δc(δ) = (1 − N(𝔭)^{−2δ}) / (N(𝔭) − N(𝔭)^{−2δ}) must vanish
for δ ≠ 0 only if certain integrality conditions are met. Baker's
theorem shows these conditions cannot be met simultaneously for
two bridge primes with multiplicatively independent norms. Walk
through this argument precisely.

(d) **The formal kill.** The argument: if δ ≠ 0, then the bridge
cocycles at two primes impose m₁ log(N₁) = m₂ log(N₂) for integers
m₁, m₂ (from the integrality of the spectral shift). Baker/unique
factorization says this forces m₁ = m₂ = 0, hence δ = 0.
Is the "integrality of the spectral shift" rigorously proved?

(e) **Comparison to the RH proof.** In the RH proof, Gelfond-Schneider
was used (log α / log β is transcendental for algebraic α, β not 0 or 1).
Baker is strictly stronger. Is the upgrade necessary, or is
Gelfond-Schneider sufficient over Q(i) as well?


---


### Point C2: The Cocycle Shift Formula [MEDIUM]

**Location:** Section 7

**The claim:** Δc(δ) = (1 − N(𝔭)^{−2δ}) / (N(𝔭) − N(𝔭)^{−2δ})
vanishes iff δ = 0, is strictly monotone, and pole-free in the
critical strip.

**Interrogate:**

(a) **Derivation.** The formula is derived from the Euler factor
ratio Z_𝔭(1+2δ)/Z_𝔭(1). Is this derivation from Bost-Connes first
principles, or does it use additional assumptions? Verify that the
Euler factor for Gaussian primes is Z_𝔭(s) = 1/(1 − N(𝔭)^{−s}).

(b) **Properties.** Verify algebraically that Δc(0) = 0. Verify
that Δc(δ) ≠ 0 for δ ≠ 0 in (−1/2, 1/2). Are there singularities
outside this range that could cause problems?

(c) **Field independence.** The claim is that the formula is
field-independent (same structure over Q and Q(i)). Is this because
the Euler factor has the same form, or is there a subtlety?


---


## Part D: From GRH to BSD


### Point D1: The CM L-Function Factorization [MEDIUM]

**Location:** Section 10

**The claim:** L(E, s) = L(s, χ_K) · L(s, ψ) where ψ is the
Grössencharacter of K associated to E via complex multiplication.

**Interrogate:**

(a) **Deuring's theorem.** Deuring (1953) established this
factorization for CM curves. Is the theorem correctly stated and
cited? What are the precise conditions on E and K?

(b) **The Grössencharacter identification.** The character ψ is
determined by E and the CM field K. Is ψ correctly identified for
the specific curves in scope (e.g., E: y² = x³ − x with CM by Q(i))?

(c) **Zeros of L(E, s).** Since L(E, s) = L(s, χ_K) · L(s, ψ),
the zeros of L(E, s) are the union of the zeros of L(s, χ_K) and
L(s, ψ). GRH for ζ_K(s) = ζ(s) · L(s, χ_{-4}) gives GRH for
L(s, χ_K). But GRH for L(s, ψ) is a SEPARATE claim — does the
bridge family reach L(s, ψ)? This is the critical question.


---


### Point D2: Kolyvagin for Rank 0 [MEDIUM]

**Location:** Section 11

**The claim:** If L(E, 1) ≠ 0 (which follows from GRH + the bridge
showing analytic rank = 0), then rank(E(Q)) = 0 and Sha(E) is finite.

**Interrogate:**

(a) **Kolyvagin's hypotheses.** Kolyvagin's theorem requires: (i) E/Q
is modular, (ii) L(E, 1) ≠ 0, (iii) there exists a Heegner point of
infinite order (for the rank 0 case, this is not needed — Kolyvagin's
rank-0 result just needs modularity + L(E,1) ≠ 0). Verify the precise
statement.

(b) **GRH implies L(E, 1) ≠ 0 for analytic rank 0.** If all zeros
are on the critical line, and ord_{s=1} L(E,s) = 0, then L(E, 1) ≠ 0.
But wait — GRH says zeros are on Re(s) = 1/2, and s = 1 is NOT on
the critical line. So GRH alone implies L(E, 1) ≠ 0 **only if the
analytic rank is already known to be 0**. How is the analytic rank
determined? Is it a priori known, or does the proof need to establish
it?

(c) **The BSD formula at rank 0.** Once rank = 0 and Sha is finite,
the BSD leading coefficient formula becomes L(E, 1) = (#Sha · Ω · ∏c_p)
/ (#E_tor)². Are all terms computed and verified?


---


### Point D3: Gross-Zagier + Kolyvagin for Rank 1 [HEAVY]

**Location:** Section 12

**The claim:** If analytic rank = 1, then: (i) L'(E, 1) ≠ 0,
(ii) the Heegner point P_K has infinite order (Gross-Zagier),
(iii) rank(E(Q)) ≤ 1 (Kolyvagin), (iv) therefore rank = 1 = analytic
rank, and (v) the BSD formula holds.

**Interrogate:**

(a) **The Gross-Zagier formula.** The formula L'(E, 1) = ĥ(P_K) ·
(explicit factor). If L'(E, 1) ≠ 0, then ĥ(P_K) ≠ 0, so P_K is
non-torsion. Verify that the Gross-Zagier formula applies to CM
curves over Q(i) — is the imaginary quadratic field for the Heegner
point the same as the CM field, or must it be different?

(b) **Kolyvagin's upper bound.** When analytic rank = 1, Kolyvagin
bounds the algebraic rank by 1. Verify the precise statement:
Kolyvagin proves rank ≤ ord_{s=1} L(E,s) when ord_{s=1} L(E,s) ≤ 1
(for modular curves with a Heegner point).

(c) **The Heegner point construction.** Heegner points are defined
using CM points on modular curves. For E with CM by Q(i), the
Heegner point is constructed using an auxiliary imaginary quadratic
field K' ≠ Q(i) satisfying the Heegner hypothesis. Is this auxiliary
field correctly identified? Or does the proof use Q(i) itself as the
Heegner field?

(d) **The BSD formula at rank 1.** The leading coefficient is
L'(E, 1) = (#Sha · Ω · R · ∏c_p) / (#E_tor)² where R = ĥ(P) is
the regulator (Néron-Tate height of a generator). All terms must be
explicitly computed. Are they?

(e) **The nine class-number-1 fields.** The theorem extends from
Q(i) to all nine class-number-1 imaginary quadratic fields. Does
the Gross-Zagier + Kolyvagin argument work uniformly across all
nine, or are there special cases?


---


## Part E: The Assembly


### Point E1: The Complete Proof Chain [HEAVY]

**Location:** Section 13

**The claim:** BSD for CM curves of analytic rank 0 and 1 over
class-number-1 fields, as a theorem.

**Interrogate:**

(a) **Chain integrity.** Walk through the full chain:
BC over K → Nelson → Meyer spectral inclusion → bridges over K →
cocycle shift → Baker → δ = 0 → GRH for L(E,s) → [rank 0:
Kolyvagin → BSD] / [rank 1: Gross-Zagier + Kolyvagin → BSD].
Is every link rigorous? Identify the weakest link.

(b) **Dependencies on RH.** The BSD proof depends on the RH proof
(Paper 13) for the bridge family construction. Is the RH proof
treated as established, or is it re-derived? If treated as
established, is this circular (since RH is also a Millennium Problem)?

(c) **The novel contribution.** What exactly is new? If the new
contribution is only "GRH for CM curves implies BSD rank 0+1 via
known results," that is a significant but well-understood chain.
The novelty must be in proving GRH for CM curves. Is this genuinely
new, or is it a restatement of known conditional results?

(d) **Numerical verification.** Section 13.3 claims BSD formula
verification to 50 digits for E: y² = x³ − x. This is evidence,
not proof. Ensure the paper does not rely on numerical verification
as a substitute for rigorous argument.

(e) **The "two Millennium Problems from one bridge" claim.**
The abstract claims both RH and BSD from the same construction.
Is this accurate, or is it marketing? The connection is via the
bridge family — same structural tool, different fields. Verify
that this framing is honest.


---


### Point E2: Scope Limitations and Honesty [MEDIUM]

**Location:** Section 15

**The claim:** The proof covers CM curves of rank 0+1 over
class-number-1 fields. Non-CM, rank ≥ 2, and h_K > 1 are
explicitly scoped out.

**Interrogate:**

(a) **Non-CM curves.** The CM factorization is essential. Without
it, the bridge family over Q(i) cannot reach L(E, s) for non-CM
curves. Is this limitation correctly identified? Could the method
extend to non-CM curves via a different mechanism?

(b) **Rank ≥ 2.** Kolyvagin's theorem gives rank ≤ ord_{s=1} L(E,s)
only when ord ≤ 1. For higher rank, different machinery is needed
(higher Heegner cycles, Zhang's programme). Is this correctly scoped?

(c) **h_K > 1.** For class number > 1, the KMS analysis is more
complex (multiple KMS states). Is the extension to h_K > 1 a
tractable research programme, or is there a fundamental obstruction?


---


## Output Format

Write all your report files into:
`/Users/gsix/quantum-geometry-in-5d-latex/paper26/referee/latest-run/`

### Directory layout (mandatory)

**Do NOT write giant monolithic files.** Organize as:

```
latest-run/
├── INDEX.md                           ← navigation
├── clay-checklist.md                  ← master roll-up (~35 rows)
├── summary.md                         ← overall verdict + closing disclosures
├── computation-log.md                 ← every "verified in venv" note
├── points/
│   ├── A1-ha-paugam/
│   │   ├── 00-statement.md
│   │   ├── 01-algebra.md              ← (a)
│   │   ├── 02-kms-uniqueness.md       ← (b)
│   │   ├── 03-gns-hilbert.md          ← (c)
│   │   └── verdict.md
│   ├── A2-nelson/
│   │   ├── 00-statement.md
│   │   ├── 01-analytic-vectors.md
│   │   ├── 02-nelson-theorem.md
│   │   ├── 03-spectral-consequence.md
│   │   └── verdict.md
│   ├── A3-meyer-spectral/            ← HEAVY
│   │   ├── 00-statement.md
│   │   ├── 01-meyer-original.md
│   │   ├── 02-extension-zeta-K.md
│   │   ├── 03-extension-hecke.md      ← critical: does BC reach L(s,ψ)?
│   │   ├── 04-scope.md
│   │   ├── 05-zeros-relationship.md
│   │   └── verdict.md
│   ├── B1-bridge-enumeration/
│   │   ├── 00-statement.md
│   │   ├── 01-frobenius.md
│   │   ├── 02-cocycle-match.md
│   │   ├── 03-completeness.md
│   │   └── verdict.md
│   ├── B2-itpfi/
│   │   ├── 00-statement.md
│   │   ├── 01-kms-factorization.md
│   │   ├── 02-euler-product.md
│   │   └── verdict.md
│   ├── B3-dark-state/
│   │   ├── 00-statement.md
│   │   ├── 01-bound.md
│   │   ├── 02-no-dark-states.md
│   │   └── verdict.md
│   ├── C1-baker/                      ← HEAVY
│   │   ├── 00-statement.md
│   │   ├── 01-baker-statement.md
│   │   ├── 02-multiplicative-independence.md
│   │   ├── 03-cocycle-shift.md
│   │   ├── 04-formal-kill.md
│   │   ├── 05-comparison-rh.md
│   │   └── verdict.md
│   ├── C2-cocycle-shift/
│   │   ├── 00-statement.md
│   │   ├── 01-derivation.md
│   │   ├── 02-properties.md
│   │   ├── 03-field-independence.md
│   │   └── verdict.md
│   ├── D1-cm-factorization/
│   │   ├── 00-statement.md
│   │   ├── 01-deuring.md
│   │   ├── 02-grossencharacter.md
│   │   ├── 03-zeros.md               ← critical: bridge → L(s,ψ)
│   │   └── verdict.md
│   ├── D2-kolyvagin-rank0/
│   │   ├── 00-statement.md
│   │   ├── 01-hypotheses.md
│   │   ├── 02-grh-implies.md
│   │   ├── 03-bsd-formula.md
│   │   └── verdict.md
│   ├── D3-gross-zagier-rank1/         ← HEAVY
│   │   ├── 00-statement.md
│   │   ├── 01-gz-formula.md
│   │   ├── 02-kolyvagin-upper.md
│   │   ├── 03-heegner-point.md
│   │   ├── 04-bsd-formula-rank1.md
│   │   ├── 05-nine-fields.md
│   │   └── verdict.md
│   ├── E1-complete-chain/             ← HEAVY
│   │   ├── 00-statement.md
│   │   ├── 01-chain-integrity.md
│   │   ├── 02-rh-dependency.md
│   │   ├── 03-novel-contribution.md
│   │   ├── 04-numerical-verification.md
│   │   ├── 05-two-millennium.md
│   │   └── verdict.md
│   └── E2-scope-honesty/
│       ├── 00-statement.md
│       ├── 01-non-cm.md
│       ├── 02-rank-geq-2.md
│       ├── 03-class-number.md
│       └── verdict.md
├── checks/
│   ├── R-rank/
│   │   ├── R1.md
│   │   ├── R2.md
│   │   └── R3.md
│   ├── LC-leading-coefficient/
│   │   ├── LC1.md
│   │   ├── LC2.md
│   │   ├── LC3.md
│   │   ├── LC4.md
│   │   ├── LC5.md
│   │   ├── LC6.md
│   │   └── LC7.md
│   ├── AC-analytic-continuation/
│   │   ├── AC1.md
│   │   ├── AC2.md
│   │   └── AC3.md
│   ├── GRH-riemann/
│   │   ├── GRH1.md
│   │   ├── GRH2.md
│   │   ├── GRH3.md
│   │   ├── GRH4.md
│   │   ├── GRH5.md
│   │   ├── GRH6.md
│   │   ├── GRH7.md
│   │   ├── GRH8.md
│   │   └── GRH9.md
│   ├── KGZ-kolyvagin-gz/
│   │   ├── KGZ1.md
│   │   ├── KGZ2.md
│   │   ├── KGZ3.md
│   │   ├── KGZ4.md
│   │   └── KGZ5.md
│   ├── BC-bost-connes/
│   │   ├── BC1.md
│   │   ├── BC2.md
│   │   ├── BC3.md
│   │   ├── BC4.md
│   │   └── BC5.md
│   ├── BR-bridge/
│   │   ├── BR1.md
│   │   ├── BR2.md
│   │   ├── BR3.md
│   │   └── BR4.md
│   ├── TR-transcendence/
│   │   ├── TR1.md
│   │   ├── TR2.md
│   │   ├── TR3.md
│   │   └── TR4.md
│   └── SC-scope/
│       ├── SC1.md
│       ├── SC2.md
│       ├── SC3.md
│       ├── SC4.md
│       └── SC5.md
```

**No file in this tree should exceed ~300 lines.** If any single file
runs longer, split it further.

### File templates

**`points/<point-id>/00-statement.md`** — one short page:

```markdown
## Point [ID]: [Title]

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Location in preprint:** [section reference]

**The claim:**
[The exact claim from the prompt's Point description.]

**Sub-questions to be answered (one file each):**
- (a) [01-...md]
- (b) [02-...md]
...
```

**`points/<point-id>/0N-<name>.md`** — one sub-question per file:

```markdown
## Point [ID]([letter]): [Sub-question title]

**The question:**
[Quote the sub-question from the prompt verbatim.]

**Finding:**
[Detailed answer. Quote relevant claims. Be precise.]

**Computational verification (if applicable):**
[Result of any mpmath/sympy check.]

**Verdict for this sub-question:**
[SOUND / CLOSABLE GAP / GENUINE GAP, with one-line justification.]
```

**`points/<point-id>/verdict.md`** — the roll-up:

```markdown
## Point [ID]: [Title] — Verdict

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Overall verdict:** [GENUINE GAP / CLOSABLE GAP / SOUND]

**Sub-question verdicts:**
- (a): SOUND / CLOSABLE / GENUINE — [one line]
...

**Combined finding:**
[1–2 paragraphs synthesizing the sub-question findings.]

**If this is a gap:**
- **Difficulty:** [1 paragraph / 1 page / 1 paper]
- **What is needed:** [precise statement]

**Impact on the claimed result:**
[Does this affect: (i) the GRH claim, (ii) the BSD rank 0 claim,
(iii) the BSD rank 1 claim, (iv) the leading coefficient formula,
or (v) Clay prize eligibility?]
```

**`checks/<group>/<id>.md`** — one file per check (30–80 lines):

```markdown
## Check [ID]: [Title]

**Group:** [R / LC / AC / GRH / KGZ / BC / BR / TR / SC]
**Source:** [Wiles description / Clay rules / preprint section]
**Pass criterion (from prompt):** [quote]

**Verdict:** [PASS / PARTIAL / FAIL]

**Justification:**
[One paragraph.]

**Cross-references:**
- Per-Point file(s): [points/<point-id>/...]
```

**`clay-checklist.md`** — master roll-up:

```markdown
# Clay Compliance Checklist (master roll-up)

| ID | Verdict | One-line summary | File |
|:---|:--------|:-----------------|:-----|
| R1 | ... | ... | checks/R-rank/R1.md |
| ... | ... | ... | ... |

**Totals:**
- PASS: ___
- PARTIAL: ___
- FAIL: ___
```

End the summary with:

```
## Overall Assessment

**Is the claimed result proved?**
[Yes / Yes with caveats / No, and here is the specific gap]

**Clay Prize Eligibility:**
[Would this proof, as written, survive review? What would need
to change? Note: the proof covers CM curves of rank 0+1 only,
not the full BSD conjecture.]

**The three most critical issues (ranked):**
1. [One sentence]
2. [One sentence]
3. [One sentence]

**What would make this a complete result:**
[Concise statement of what additional work, if any, is needed]
```

---

## Closing instructions (REQUIRED in summary.md)

The last few sentences of `summary.md` MUST include:

1. **Scope limitation disclosure.** This proof covers BSD for CM
   curves of analytic rank 0 and 1 over class-number-1 imaginary
   quadratic fields. It does NOT cover: non-CM curves, rank ≥ 2,
   h_K > 1. The full BSD conjecture remains open.

2. **Dependency on RH proof.** This proof depends on the bridge
   family construction validated in Paper 13 (the RH proof). If
   the RH proof has gaps, they propagate here.

3. **Literature verification.** The proof uses Kolyvagin, Gross-Zagier,
   Baker, and Deuring as black boxes. These are well-established
   results, but the referee has not independently verified their
   proofs. **Action item for a future cycle:** verify that each
   black-box result is cited with the correct theorem statement
   and applicable scope.

4. **Tools added during this run** (if any).

---

Do not be diplomatic. Do not praise the work. Don't hurry. Don't take
shortcuts. Find the gaps.

If you cannot find a gap in a specific argument, say so explicitly
and explain why — that is also valuable information.

# Your north star
Find any issue that would cause the Clay Scientific Advisory Board to
reject this proof. Focus on:
- Does the bridge family construction actually reach L(s, ψ) (the
  Grössencharacter L-function), or only ζ_K(s)?
- Is Baker's theorem correctly applied to force δ = 0?
- Is the chain GRH → Kolyvagin/GZ → BSD complete and rigorous?
- Are all scope limitations honestly disclosed?
- Does the paper overstate what it proves?
- Is the "two Millennium Problems" framing honest or marketing?
