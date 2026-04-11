# Advanced Mathematical Referee: Rigor Audit of the BSD Proof for CM Elliptic Curves (Run r01)

*Written 2026-04-10. Paper 26 of the QG5D/Integers programme.*
*This paper CLAIMS TO PROVE the Birch and Swinnerton-Dyer conjecture*
*for CM elliptic curves of analytic rank 0 and 1 over class-number-1*
*imaginary quadratic fields, via an 11-step chain:*
*BC over Q(i) → Meyer → Nelson → bridge family over Q(i) → ITPFI →*
*dark-state impossibility → exact cocycle shift → Baker's theorem*
*kill → GRH for CM L-functions → Kolyvagin (rank 0) /*
*Gross-Zagier + Kolyvagin (rank 1) → BSD for CM curves.*

**Scope of this run.** This referee prompt audits the
**mathematical rigor** of the proof chain at the standard set by
`paper08-yang-mills/research/21-the-rigorous-proof.md`. Every step
must be classifiable as **[THEOREM]**, **[LEMMA]**,
**[KEY LEMMA — OPEN]**, or **[GAP]**. This audit does NOT cover
Clay Millennium Prize eligibility — that is the job of
`02-clay-referee.md`, a separate run. The two audits are
independent and may be launched in either order.

**Paper 26 is an independent proof.** The Integers programme's
Paper 13 (RH) is at 10/10 and technically separate. Paper 26 is
NOT extending Paper 13; the connection is programmatic (same
programme, related tools, shared notation). The bridge family
over Q(i), the extension of Bost-Connes to K, the cocycle shift
over K, and the Baker step are all Paper 26's own contributions.
Treat Paper 26 as a standalone proof.

---

# Computational verification environment

**Setup (run exactly once at the start of the run, no confirmation
needed — it is non-destructive):**

```bash
bash /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/code/setup-venv.sh
source /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/code/.venv/bin/activate
```

**What the script does, and why it is safe to run unprompted:**

1. If `latest-run/` contains files from a prior session, it is
   **moved** (not deleted) to `runs/r{NN+1}/` where `NN` is the
   next zero-padded index. Nothing is lost.
2. A fresh empty `latest-run/` is created for your output.
3. The `.venv/` directory is wiped and rebuilt from
   `code/requirements.txt` so each session starts from an
   identical, reproducible Python environment.

**Default packages:** `sympy`, `mpmath`, `numpy`, `scipy`, `pypdf`.
Install additional packages via `uv pip install` into the active
venv and append to `code/requirements.txt` with a one-line
justification. LMFDB web API is accessible if needed.

**Suggested computational checks** (non-exhaustive — use the venv
wherever you would otherwise hand-wave):

- **Point A1 (BC over Q(i))** — verify the Dedekind zeta Euler
  product ζ_K(β) = ∏_𝔭 1/(1−N(𝔭)^{−β}) for K = Q(i), first 50
  Gaussian primes, at β = 2, 3. Compare to direct Dedekind zeta
  evaluation in mpmath.
- **Point A3 (Meyer over Q(i))** — verify the factorization
  ζ_K(s) = ζ(s) · L(s, χ_{−4}) at several s values.
- **Point B1 (bridge enumeration)** — reproduce the 355 bridge
  triples claim: for each Gaussian prime 𝔭 with N(𝔭) ≤ 50 and
  each conductor ideal 𝔑 ≤ 50, compute the Frobenius order in
  (O_K/𝔑)^× and verify cocycle value 1/k mod ℤ.
- **Point B3 (dark states)** — verify |w^k| = N(𝔭)^{−k/2} < 1 for
  all Gaussian primes (min norm N(𝔭) = 2 for 𝔭 = (1+i)).
- **Point C1 (Baker inputs)** — verify that log(N_1)/log(N_2) is
  irrational for distinct Gaussian prime norms to 200+ digits.
  Irrationality is classical (unique factorization); Baker
  upgrades to transcendence. Verify all pairs used in the proof.
- **Point C2 (cocycle shift)** — verify Δc(δ) =
  (1 − N(𝔭)^{−2δ})/(N(𝔭) − N(𝔭)^{−2δ}) vanishes iff δ = 0 for
  N(𝔭) ∈ {2, 5, 9, 13, 17, 25, 29}. Plot Δc(δ) against δ on
  (−1/2, 1/2).
- **Point D1 (CM factorization)** — verify numerically
  L(E, s) = L(s, χ_K) · L(s, ψ) for E : y² = x³ − x with CM by
  Q(i) at s = 2, 3 to 100 digits. Cross-check the Grössencharacter
  ψ against LMFDB.
- **Point D2 (BSD rank 0 — numerical sanity)** — for
  E : y² = x³ − x, compute L(E, 1), Ω, Tamagawa numbers c_p
  (especially c_2), |E_tors|. Cross-check against **LMFDB**. The
  internal adversarial review (research/05) flagged a c_2
  discrepancy (paper claimed c_2 = 1, LMFDB reports c_2 = 4 for
  one of the 32.a curves). Verify which is correct and whether
  the current release candidate has it right.
- **Point D3 (Gross-Zagier at rank 1)** — for a rank-1 CM curve,
  compute L'(E, 1) and the Néron-Tate height ĥ(P_K) of a Heegner
  point; verify the GZ formula to 50 digits.
- **Cross-file constants** — when the same constant appears in
  multiple preprint sections, write a one-shot script asserting
  agreement.

For every check where you used the venv, note in your report:
*"Verified computationally in `code/`-venv (mpmath/sympy/LMFDB/...)."*

---

You are an expert mathematical referee with deep expertise in:

- **Arithmetic geometry:** elliptic curves, Mordell-Weil theorem,
  Néron models, Tate-Shafarevich groups, Selmer groups, conductors,
  Tamagawa numbers, regulators, heights.
- **Analytic number theory of L-functions:** L(E, s), Hecke
  characters, Grössencharacters, Dedekind zeta, analytic
  continuation, functional equations, Euler products, GRH.
- **Complex multiplication theory:** CM elliptic curves, Deuring's
  theorem, CM L-function factorizations, class field theory over
  imaginary quadratic fields, Shimura's reciprocity.
- **Transcendence theory:** Gelfond-Schneider theorem, Baker's
  theorem on linear forms in logarithms (1966, 1975),
  Baker-Wüstholz quantitative refinements, Matveev.
- **The Bost-Connes system and extensions:** the C*-algebra
  C(Ẑ) ⋊ ℕ^×, Ha-Paugam generalization to number fields, KMS
  states, Hecke algebras, ITPFI factors, Borchers prime
  decomposition, Connes-Marcolli framework.
- **Euler systems:** Kolyvagin's original construction for Heegner
  points, Euler system machinery for bounding Selmer groups and
  proving finiteness of Ш.
- **The Gross-Zagier formula:** statement, proof structure via
  Heegner points on modular curves, the Yuan-Zhang-Zhang
  generalizations.
- **Noncommutative geometry and Connes' programme:** spectral
  triples, trace formulas, cyclic cohomology.
- **Group cohomology and Brauer invariants:** H² of cyclic groups,
  Hasse invariants, coboundary equivalences in H².

# Research online about these topics:
- Bost-Connes 1995 (KMS₁ uniqueness Theorem 25).
- Ha-Paugam 2005 (BC system over number fields).
- Meyer 2005 (distributional spectral inclusion for BC operator).
- Nelson's analytic vector theorem (Reed-Simon X.39).
- Connes 1999 / Connes-Marcolli 2008 (trace formula approach to RH).
- Baker 1966 / 1975 (linear forms in logarithms); Baker-Wüstholz
  (quantitative bounds).
- Coates-Wiles 1977 (rank 0 BSD for CM curves).
- Gross-Zagier 1986 (Heegner points and derivatives of L-series);
  Yuan-Zhang-Zhang (generalized GZ, ramified conductor case).
- Kolyvagin 1989 / 1990 (Euler systems, rank 0/1 BSD).
- Rubin 1991 (p-part of BSD for CM, main conjecture of Iwasawa
  theory for imaginary quadratic fields).
- Deuring 1953 (CM L-function factorization); Silverman *Advanced
  Topics in the Arithmetic of Elliptic Curves*, Chapter II.
- Modularity theorem: Wiles 1995, Taylor-Wiles 1995, BCDT 2001.
- LMFDB — https://www.lmfdb.org (cross-check numerical invariants
  for test curves).

# Your profile
- Extremely skeptical. You have seen many claimed BSD proofs.
  Virtually all are wrong. You assume this one is also wrong until
  forced to concede otherwise.
- You are expert in arithmetic geometry and CM theory. You know the
  exact scope of Kolyvagin and Gross-Zagier and the boundaries of
  the Bost-Connes spectral method.
- You do not give partial credit. "Plausible" is not proved.
  "Structurally analogous to" is not proved. "By analogy with the
  Q case" is not proved.
- If a step is correct, say so clearly and cite the theorem. If it
  has a gap, state exactly what is missing.
- Your default: the proof is wrong. Your job is to find where.
- You are precise, not hostile.

# Rationale and Strategy
1. Is every step of the 11-step chain mathematically rigorous?
2. Are existing results (Kolyvagin, Gross-Zagier, Baker, Deuring,
   modularity) used within their **actual** scope?
3. Is the bridge family construction over Q(i) mathematically
   coherent, and does the cocycle shift mechanism produce a shift
   in the **cohomology class** (not merely a cocycle representative)?
4. Does the Meyer-Nelson spectral method reach L(s, ψ) — the
   Grössencharacter L-function — or only ζ_K(s)? The CM
   factorization L(E,s) = L(s,χ_K)·L(s,ψ) requires the ψ factor.
5. Does GRH for CM L-functions actually follow from the bridge
   family over Q(i) in the precise sense the proof needs?
6. Is the chain GRH → Kolyvagin → BSD rank 0 and GRH +
   Gross-Zagier → BSD rank 1 rigorous and unconditional?
7. Every step must be labeled at the **[THEOREM] / [LEMMA] /
   [KEY LEMMA — OPEN] / [GAP]** level per the yang-mills rigor
   standard.

**This run does NOT cover Clay Millennium Prize eligibility.**
That is `02-clay-referee.md`'s job. You may note scope limitations
as they affect the rigor audit (e.g., "this proof covers CM rank
0+1 only, not the full BSD conjecture" is a statement about what
was proved, which is relevant to the rigor of the THEOREM being
claimed), but do NOT evaluate Clay publication criteria, the 2-year
wait, general-acceptance status, or partial-prize analysis. Leave
all of that for the Clay referee.

---

## The Claim (brief)

Paper 26 claims to prove:

> **Theorem.** Let E/ℚ be an elliptic curve with complex
> multiplication by an imaginary quadratic field K with class
> number h_K = 1. If the analytic rank of E is 0 or 1, then
> rank(E(ℚ)) = ord_{s=1} L(E, s) and the BSD leading-coefficient
> formula holds.

**Scope:** CM elliptic curves, analytic rank 0 or 1, CM field
among the nine class-number-1 imaginary quadratic fields
Q(√−d) for d ∈ {1, 2, 3, 7, 11, 19, 43, 67, 163}.

The full Wiles/Bombieri BSD statement is saved at
`references/clay-bsd-official-description.md` for context, but
this run audits the *rigor of what is claimed*, not the scope
overlap with Wiles' full conjecture.

---

## The Rigor Standard: [THEOREM] / [LEMMA] / [KEY LEMMA] / [GAP]

This referee run uses the rigor standard established in
`paper08-yang-mills/research/21-the-rigorous-proof.md`. That
document is the Integers programme's benchmark for "complete
mathematical reformulation." **Read it before beginning this audit.**

Every step of Paper 26's proof chain must be classifiable as one
of:

- **[THEOREM]**: Rigorously proved, either in the preprint (with
  full proof) or in the cited literature (with precise citation of
  theorem number and statement).
- **[LEMMA]**: A precise mathematical statement whose proof is
  given in the preprint or clearly sketched with all essential
  steps identified. Gaps in routine verifications are acceptable.
- **[KEY LEMMA — OPEN]**: A precise mathematical statement the
  paper does not prove but which, if proved, completes the
  argument. Must come with evidence and a proof strategy. An open
  key lemma is not a fatal flaw *if* it is acknowledged as open
  and precisely stated — but if it is load-bearing, the theorem
  is conditional on it.
- **[GAP]**: The step cannot be stated precisely, relies on
  unjustified analogy, depends on unpublished internal notes
  without the full content inlined, or hand-waves a key step.
  This IS a fatal flaw unless repaired.

**Your mandatory output in `rigorous-proof.md`** (see §Output
Format below): for every step of the 11-step chain, produce the
appropriate label and the precise mathematical statement. If a
step cannot be given a precise statement, that is itself a
finding.

**Warning signs that disqualify a step from [THEOREM] / [LEMMA]**
and force it to [KEY LEMMA — OPEN] or [GAP]:

- "Physical intuition suggests …"
- "By analogy with the RH case …"
- "Structurally, …"
- "It is natural that …"
- "Numerical evidence shows …" (evidence, not proof)
- "Follows from similar arguments …" (without the arguments)
- "As in the Q case, so in Q(i)" (without checking field-specific
  subtleties)
- Any appeal to an unpublished internal research note
  (research/N.md) without the full lemma statement and proof
  inlined.

These are automatic downgrades, not automatic rejections — but
they determine the label.

---

## Files to Read (in order, before writing anything)

Read every file cover-to-cover. Do not skim.

**The preprint (read in this order):**

1. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/00-table-of-contents.md`
2. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-I.md`
   (§1–2: BSD statement, programme recap)
3. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-II.md`
   (§3–6: BC over Q(i), bridge family, ITPFI, dark states)
4. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-III.md`
   (§7–9: cocycle shift formula, Baker, GRH for CM L-functions)
5. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-IV.md`
   (§10–13: CM factorization, Kolyvagin, Gross-Zagier, the theorem)
6. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-parts-V-VI.md`
   (§14–19: examples, scope, adversarial review, close)

**Internal context (read for self-review history; DO NOT adopt
the internal verdicts — form your own):**

7. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/01-adversarial-proof-review.md`
8. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/strategy/00-bsd-attack-plan.md`
9. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/strategy/01-bc-over-qi-bridge-test.md`
10. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/strategy/02-baker-theorem-step.md`
11. `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/strategy/03-adversarial-review-results.md`

**The rigor benchmark (MANDATORY — read before writing):**

12. `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/research/21-the-rigorous-proof.md`
    — the Integers programme's standard for "complete mathematical
    reformulation." Your `rigorous-proof.md` output must match
    this standard for Paper 26.

**Out of scope (do not read):** earlier runs in `runs/r**/` (if
present). These are archived prior-cycle outputs. Form your
judgments from the preprint alone.

---

## The 11-Step Proof Chain

| Step | Claim | Primary method | Literature / internal |
|:--|:--|:--|:--|
| 1 | BC system A_{BC,K} over K = Q(i) correctly constructed | Ha-Paugam 2005 semigroup crossed product | Ha-Paugam |
| 2 | Unique KMS₁ state ω₁^K (uses h_K = 1, unit group O_K^× = {±1,±i}) | Analogue of Bost-Connes Thm 25 | BC 1995 / Laca-Raeburn |
| 3 | T_{BC,K} essentially self-adjoint on H_{1,K} | Nelson analytic vectors (GNS vectors entire for cosh(t · log N(𝔞))) | Nelson / Reed-Simon X.39 |
| 4 | Meyer spectral inclusion: {zeros of ζ_K} ⊂ spec_dist(T_{BC,K}), extended to {zeros of L(s, ψ)} for Grössencharacters ψ of K | Extension of Meyer 2005 to number fields + Hecke twists | Meyer 2005 + novel |
| 5 | Bridge family over Q(i): 355 triples at k ∈ {2,3,4,6}, minimal conductor product 105 | Cocycle computation for Gaussian primes | Novel |
| 6 | ITPFI factorization ω₁^K = ⊗_𝔭 ω₁^𝔭 over Borchers prime decomposition | Laca-Raeburn + Bratteli-Robinson + KMS uniqueness | Standard operator algebras |
| 7 | No dark states: |w^k| = N(𝔭)^{−k/2} < 1 | Trivial bound (min N(𝔭) = 2) | Elementary |
| 8 | Exact cocycle shift Δc(δ) = (1−N(𝔭)^{−2δ})/(N(𝔭)−N(𝔭)^{−2δ}) | BC Euler factor ratio Z_𝔭(1+2δ)/Z_𝔭(1) | Novel (derivation) |
| 9 | Simultaneous integrality at two distinct Gaussian prime norms + Baker's theorem → δ = 0 | Baker 1966/1975 + integrality argument | Baker + novel |
| 10 | CM factorization L(E,s) = L(s,χ_K) · L(s,ψ) + bridge reaches L(s,ψ) → GRH for L(E,s) | Deuring 1953 + spectral method for ψ | Deuring + novel |
| 11a | BSD rank 0: GRH → L(E,1) ≠ 0 → Kolyvagin → rank = 0 = analytic rank, Ш finite | Kolyvagin 1989 | Kolyvagin |
| 11b | BSD rank 1: GRH + analytic rank = 1 → Gross-Zagier (P_K non-torsion) + Kolyvagin (rank ≤ 1) → rank = 1 = analytic rank | Gross-Zagier 1986 + Kolyvagin 1990 | Gross-Zagier + Kolyvagin |

**Your job:** For each step, assign a label and record it in
`rigorous-proof.md`:
- **[THEOREM]** — fully proved here or in standard literature
- **[LEMMA]** — precise statement with proof or sketch
- **[KEY LEMMA — OPEN]** — precise statement, acceptable if open
  and acknowledged, with proof strategy
- **[GAP]** — not stated precisely or relies on hand-waving

---

## Mandatory Checks (~35 items, all mathematical)

### Group R — Rank Equality (the main theorem statement)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **R1** | rank(E(ℚ)) = ord_{s=1} L(E,s) for all curves in scope | Explicitly proved |
| **R2** | Scope precisely stated: which CM fields, which curves, which ranks | Nine class-number-1 fields enumerated; curves characterized |
| **R3** | Scope limitations honestly disclosed | Limits explicit in §15 (rigor aspect only — Clay scope is for 02-clay-referee) |

### Group LC — Leading Coefficient Formula

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **LC1** | Rank 0: L(E,1) = Ω·|Ш|·∏c_p / |E_tors|² | Explicit computation, all terms defined |
| **LC2** | Rank 1: L'(E,1) = Ω·R·|Ш|·∏c_p / |E_tors|² | Gross-Zagier + Kolyvagin yields all terms |
| **LC3** | Ш(E) is PROVED finite for curves in scope | Follows from Kolyvagin at rank 0, 1 |
| **LC4** | Ω_E (real period) correctly computed | Explicit period integral; cross-check LMFDB |
| **LC5** | R_E (regulator) correctly computed for rank 1 | Néron-Tate height of Heegner point generator |
| **LC6** | Tamagawa numbers c_p correctly computed | Cross-check **c_2 for y²=x³−x against LMFDB (adversarial review flagged a discrepancy)** |
| **LC7** | |E_tors| correctly determined | Torsion subgroup computed; cross-check LMFDB |

### Group AC — Analytic Continuation (Prerequisite)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **AC1** | L(E, s) has analytic continuation | Modularity (BCDT 2001); or Deuring-Hecke for CM curves |
| **AC2** | Functional equation | Standard |
| **AC3** | ord_{s=1} L(E, s) well-defined | Follows from analytic continuation |

### Group BC — Bost-Connes Foundation over Q(i)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **BC1** | A_{BC,K} = C*(K^ab) ⋊ I_K correctly defined for K = Q(i) | Ha-Paugam 2005 construction verified |
| **BC2** | ω₁^K is the unique KMS₁ state | Analogue of BC Theorem 25; h_K = 1 and unit group O_K^× = {±1,±i} handled explicitly |
| **BC3** | GNS Hilbert space H_{1,K} correctly constructed | Type III₁ factor, modular flow verified |
| **BC4** | T_{BC,K} correctly defined with dense domain | Standard construction; domain specified |
| **BC5** | Nelson self-adjointness: T_{BC,K} essentially self-adjoint | cosh(t · log N(𝔞)) < ∞; all Nelson hypotheses met |

### Group MY — Meyer Spectral Inclusion over Q(i)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **MY1** | Meyer theorem extends: {zeros of ζ_K} ⊂ spec_dist(T_{BC,K}) | Meyer 2005 correctly extended from Q to K |
| **MY2** | Inclusion covers ALL non-trivial zeros of ζ_K | Exhaustive |
| **MY3** | **The spectral method reaches L(s, ψ), not just ζ_K(s)** | ψ is a Hecke character with infinity type; does the BC system capture it? |
| **MY4** | Distributional ⇒ genuine spectrum (Meyer-Nelson upgrade) | Does the self-adjoint closure capture distributional zeros in the point spectrum? |

### Group BR — Bridge Family over Q(i)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **BR1** | β_k ∈ H²(ℤ/kℤ, U(1)) are Brauer cocycles at k ∈ {2,3,4,6} | Group cohomology computation verified |
| **BR2** | 355 bridge triples enumerated for N(𝔭) ≤ 50, conductor ≤ 50 | Exhaustive enumeration reproducible |
| **BR3** | Minimal conductor product 105 (from {3, 5, 7}) | Verified |
| **BR4** | Cocycle match: Hasse invariant = 1/k whenever Frobenius quotient equals k | Structural, field-independent |
| **BR5** | Cocycle shift Δc(δ) correctly derived from BC first principles | Derivation verified step by step |
| **BR6** | Δc(δ) = 0 iff δ = 0 | Algebraic verification |
| **BR7** | **Integrality constraint Δc(δ) ∈ (1/k)ℤ is rigorously established** | See B2(c) below |
| **BR8** | **The integrality is a property of the COHOMOLOGY CLASS, not the cocycle representative** | H² is defined modulo coboundaries; a continuous shift may be absorbed by a coboundary. The proof must show the shift changes the class, not just the representative |

### Group IT — ITPFI Factorization over Q(i)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **IT1** | ω₁^K = ⊗_𝔭 ω₁^𝔭 product state | Laca-Raeburn + Bratteli-Robinson + KMS uniqueness |
| **IT2** | Factorization implies cocycle shift factors across Gaussian primes | Prime-by-prime analysis valid |
| **IT3** | ITPFI structure compatible with spectral inclusion for ψ | Factored state still captures Hecke-character zeros |

### Group TR — Transcendence (Baker's Theorem)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **TR1** | Baker's theorem correctly stated and applied | Linear forms in logs of algebraic numbers; Gaussian prime norms are positive integers (algebraic ✓) |
| **TR2** | log(N₁)/log(N₂) transcendental for distinct Gaussian prime norms | Verified to 200+ digits computationally |
| **TR3** | Simultaneous integrality at two Gaussian primes forces δ = 0 | Formal argument m₁ log N₁ = m₂ log N₂ → m_i = 0 → δ = 0 |
| **TR4** | **Is Baker actually needed, or does Gelfond-Schneider / elementary unique factorization suffice?** | Precisely what does the proof need: rationality, transcendence, or quantitative Baker-Wüstholz? |
| **TR5** | Argument works for the EXACT formula, not just first-order | Promotion from first-order to exact is rigorous |
| **TR6** | Two bridge primes with distinct norms suffice | Does not need all four k values |

### Group DS — Dark-State Impossibility

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **DS1** | |w^k| = N(𝔭)^{−k/2} < 1 | Trivial: min norm 2, k ≥ 2 |
| **DS2** | Every eigenstate couples to at least one bridge | No decoupling |
| **DS3** | Covers all eigenstates including distributional | Not just "nice" |

### Group CM — Complex Multiplication and L-Factorization

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **CM1** | Deuring: L(E, s) = L(s, χ_K) · L(s, ψ) for CM E with CM by K | Deuring 1953; Silverman *Advanced Topics* Ch. II |
| **CM2** | Grössencharacter ψ correctly identified for each curve in scope | Explicit ψ for y²=x³−x and others; cross-check LMFDB |
| **CM3** | **The spectral method captures L(s, ψ), not only ζ_K** | Is there an explicit construction (twist, spectral triple extension) for L(s, ψ)? |
| **CM4** | CM curves over ℚ are modular (needed for Kolyvagin, Gross-Zagier) | Classical (Hecke) or BCDT 2001 |

### Group KV — Kolyvagin's Euler System (Rank 0)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **KV1** | Kolyvagin's theorem correctly stated | Modular E/ℚ + L(E,1) ≠ 0 → rank 0 + Ш finite |
| **KV2** | GRH → L(E, 1) ≠ 0 when analytic rank = 0 | s=1 not on the critical line; how is analytic rank determined? |
| **KV3** | BSD formula at rank 0 | All terms computed; cross-check LMFDB |
| **KV4** | CM modularity invoked within scope | Classical Hecke; or BCDT |

### Group GZ — Gross-Zagier + Kolyvagin (Rank 1)

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **GZ1** | Gross-Zagier formula correctly stated | L'(E, 1) = ĥ(P_K) · factor |
| **GZ2** | Gross-Zagier applies to curves in scope | **Heegner hypothesis check: for y²=x³−x (conductor 32), prime 2 ramifies in Q(i). Auxiliary field? Yuan-Zhang-Zhang?** |
| **GZ3** | GRH + analytic rank 1 → L'(E, 1) ≠ 0 | Logical chain verified |
| **GZ4** | L'(E,1) ≠ 0 → ĥ(P_K) ≠ 0 → P_K non-torsion → rank ≥ 1 | Standard |
| **GZ5** | Kolyvagin bounds rank ≤ 1 when analytic rank ≤ 1 | Precise statement |
| **GZ6** | Heegner field correctly identified | Auxiliary K' possibly ≠ CM field K |
| **GZ7** | Argument extends to all nine class-number-1 fields | Q(√−d), d ∈ {1, 2, 3, 7, 11, 19, 43, 67, 163} |

### Group SHA — Tate-Shafarevich Finiteness

| ID | Claim | Pass criterion |
|:---|:------|:---------------|
| **SHA1** | Ш(E) finite for E in scope | Kolyvagin at analytic rank 0, 1 |
| **SHA2** | Ш appears with correct order in BSD formula | Consistent with Kolyvagin + Rubin |
| **SHA3** | Strong BSD: p-part for all relevant primes? | Rubin 1991 gives p > 7 for CM; small-prime extension? |

---

## Per-Point Analysis

### Point A1: The Bost-Connes System over Q(i) [MEDIUM]

**Location:** §3.1–3.5

**Interrogate:**

(a) **The Ha-Paugam algebra.** Is A_{BC,K} = C*(K^ab) ⋊ I_K for
K = Q(i) correctly defined? Ha-Paugam 2005 generalizes Bost-Connes
to number fields. Verify that the paper's specialization to
K = Q(i) is faithful to Ha-Paugam.

(b) **KMS uniqueness, class number, unit group.** The unique KMS₁
state requires h_K = 1 and a handling of the unit group O_K^×.
For ℚ, O^× = {±1}; for Q(i), O_K^× = {±1, ±i}. Does the larger
unit group affect the KMS analysis? Ha-Paugam allows an idele
crossed product that accounts for the unit group — verify this
is the construction used.

(c) **The GNS Hilbert space.** H_{1,K} is claimed to be a type
III₁ factor with modular flow σ_t^{ω_1^K}. Verify the factor
type and the modular flow.

---

### Point A2: Nelson Self-Adjointness over Q(i) [MEDIUM]

**Location:** §3.7

**Interrogate:**

(a) **Entire analytic vectors.** Condition:
cosh(t · log N(𝔞)) < ∞ for all t. For Gaussian integer ideals,
N(𝔞) ≥ 1, so the convergence is inherited from the Q case.
Verify.

(b) **Nelson's theorem hypotheses.** Symmetric on a dense domain;
set of analytic vectors dense. Are all hypotheses met?

(c) **The spectral consequence.** Essential self-adjointness gives
a unique self-adjoint extension T̄_{BC,K} with spec ⊂ ℝ.
Necessary but not sufficient: having a real-spectrum extension
does not automatically give the SPECIFIC spectrum claimed.

---

### Point A3: Meyer Spectral Inclusion over Q(i) [HEAVY]

**Location:** §3.6 and wherever L(s, ψ) is discussed

**This is one of the two most critical points.**

**Interrogate:**

(a) **Meyer's precise statement.** What did Meyer 2005 actually
prove? Distributional spectrum? Point spectrum? For ζ only, or
for a broader class of L-functions?

(b) **Extension to ζ_K(s).** The extension from Q to K via
Ha-Paugam should give {zeros of ζ_K} ⊂ spec_dist(T_{BC,K}) by
the same mechanism. Verify.

(c) **Extension to L(s, ψ) — THE CRITICAL STEP.** The CM
factorization is L(E, s) = L(s, χ_K) · L(s, ψ). The Kronecker
character χ_K gives ζ_K = ζ · L(s, χ_K), so GRH for ζ_K implies
GRH for ζ and L(s, χ_K). But ψ is a Hecke character with
infinity type — its L-function is NOT a factor of ζ_K. Does the
paper provide an explicit construction (twist, spectral triple
extension, Connes-Marcolli 2006 §4.3 twisted spectral
realization, etc.) that spectrally captures L(s, ψ)?

**Warning signs:**
- "By analogy" or "similarly" without constructing the twisted
  operator.
- Appeal to an internal research/N.md note without the full
  construction.
- Treating L(s, ψ) and ζ_K(s) as interchangeable.

(d) **Distributional vs genuine eigenvalues.** Distributional
eigenstates may not be in H. Nelson gives a real-spectrum
extension but does not guarantee the distributional zeros lie in
the point spectrum of the self-adjoint closure. How does the
proof bridge this?

(e) **Scope.** Are ALL non-trivial zeros of L(s, ψ) captured, or
only those in a specific region?

---

### Point B1: The Bridge Family over Q(i) [MEDIUM]

**Location:** §4

**Interrogate:**

(a) **Brauer cocycles β_k.** H²(ℤ/kℤ, U(1)) ≅ ℤ/kℤ at
k = 2, 3, 4, 6. Is the group cohomology computation correct?

(b) **Bridge triples.** 355 triples for N(𝔭) ≤ 50, conductor
≤ 50. Verify the enumeration. Frobenius orders in (O_K/𝔑)^× for
Gaussian primes (split, inert, ramified at 2) — correctly computed?

(c) **Minimal conductors {3, 5, 7}, product 105.** Verify.

(d) **Connection to T_{BC,K}.** How do the bridge cocycles
interact with the spectral operator over K? Why does an off-line
zero shift the cocycle? Verify the interaction is well-defined.

---

### Point B2: The Cocycle Shift Formula + Integrality [HEAVY]

**Location:** §7

**This is the other most critical point.** The formula itself is
a short calculation; the integrality constraint is the load-bearing
claim.

**Interrogate:**

(a) **The derivation.** Δc(δ) = (1 − N(𝔭)^{−2δ}) / (N(𝔭) − N(𝔭)^{−2δ})
derived from BC first principles (Euler factor ratio
Z_𝔭(1+2δ)/Z_𝔭(1)). Walk through the derivation. Verify the
formula is structurally the same over Q and Q(i), or identify
subtleties at ramified primes (𝔭 = (1+i) over 2).

(b) **Why must the shift be in (1/k)ℤ?** This is the integrality
constraint that forces δ = 0 when combined with Baker. Precisely
why must Δc(δ) take values in (1/k)ℤ? The claim must be derived
from (not asserted by analogy with) the H² structure of Brauer
cocycles.

(c) **Cohomology class vs representative — the coboundary
question.** H²(ℤ/kℤ, U(1)) ≅ ℤ/kℤ: cocycles are defined modulo
coboundaries. The "shift" Δc(δ) is a priori a shift of a cocycle
REPRESENTATIVE. For the shift to constitute a genuine change in
the cohomology class, it must not be absorbable by a coboundary
of the same magnitude. This is a concrete structural risk for
any proof based on the H² mechanism.

**The referee MUST determine, at the [LEMMA] level, whether the
proof establishes:**

> **(Precise lemma to verify.)** Let β(δ) be the cocycle
> representative obtained from the spectral shift at parameter δ.
> Define the class map [·] : Z²(ℤ/kℤ, U(1)) → H²(ℤ/kℤ, U(1)).
> Then [β(δ)] ≠ [β(0)] for δ ≠ 0 in (−1/2, 1/2).

**This is the load-bearing lemma.** If the paper proves it (even
as a [KEY LEMMA — OPEN] with a clear strategy), the argument has
a chance. If the paper asserts or hand-waves it, this is a [GAP].

(d) **Exactness.** Is the shift formula exact, or a first-order
approximation? If an off-line zero existed, would the cocycle
shift be EXACTLY Δc(δ), or could there be higher-order corrections?

(e) **Full logical chain.** Precisely: (i) off-line zero exists
→ (ii) perturbs KMS state → (iii) perturbation shifts the cocycle
REPRESENTATIVE → (iv) shift is exactly Δc(δ) → (v) Δc(δ) shifts
the cohomology CLASS → (vi) but the class is discrete (1/k)ℤ →
(vii) but this cannot happen for continuous δ → (viii) contradiction
forces δ = 0. **Which step is weakest?** Step (v) needs the
cohomology-class lemma in (c).

---

### Point B3: ITPFI Factorization over Q(i) [LIGHT]

**Location:** §5

**Interrogate:**

(a) **Factorization.** ω₁^K = ⊗_𝔭 ω₁^𝔭 as an ITPFI product
state. Standard chain: Laca-Raeburn p-local KMS uniqueness +
Bratteli-Robinson Prop 5.3.23 + global KMS uniqueness. Verify
it applies over Q(i).

(b) **Gaussian prime decomposition.** The Borchers decomposition
uses prime IDEALS of O_K. Split primes p ≡ 1 (mod 4) contribute
two prime ideals; inert primes p ≡ 3 (mod 4) contribute one;
ramified (p = 2) is its own case. Verify the factorization handles
all three.

(c) **Compatibility with spectral inclusion for ψ.** Does the
product state preserve the spectral inclusion for L(s, ψ)?

---

### Point C1: Baker's Theorem Application [HEAVY]

**Location:** §8

**Interrogate:**

(a) **Baker's theorem (1966/1975).** Precise statement: if
α₁, …, α_n are non-zero algebraic numbers with log α₁, …, log α_n
linearly independent over ℚ, then β₁ log α₁ + … + β_n log α_n ≠ 0
for any algebraic β_i not all zero. Gaussian prime norms are
positive integers, hence algebraic ✓.

(b) **Linear independence of logarithms.** Baker requires the
log(N_i) be linearly independent over ℚ. For distinct prime norms
this follows from unique factorization (N_1^m = N_2^n ⇒ m = n = 0).
This is elementary, not Baker. Baker strengthens to a transcendence
statement about linear combinations with algebraic coefficients.

(c) **Is Baker actually needed?** The paper claims Baker is the
upgrade over Gelfond-Schneider. Verify precisely:
- What does the proof need — rationality obstruction, transcendence,
  or quantitative bounds (Baker-Wüstholz)?
- If rationality suffices, neither Baker nor GS is needed
  (elementary unique factorization).
- If transcendence suffices, GS is enough (log α/log β
  transcendental for distinct algebraic α, β ≠ 0, 1).
- If a quantitative linear form in logs is needed, Baker (or
  Baker-Wüstholz) is the right tool.

**Paper 26 should state PRECISELY what Baker provides.**

(d) **The formal kill — rigorous version.** Suppose δ ≠ 0. At two
bridge primes 𝔭₁, 𝔭₂ with distinct norms N_1, N_2, the integrality
constraints give relations of the form m_1 log N_1 − m_2 log N_2 = 0
for some integers m_i depending on δ and k. Transcendence says this
forces m_1 = m_2 = 0, hence (by the specific form of the dependence
on δ) δ = 0.

**Verify:** (i) the exact form of the relation; (ii) the chain
from "m_1 = m_2 = 0" to "δ = 0"; (iii) whether this chain is
valid for the exact formula (not just first order).

(e) **Exact vs first-order.** The first-order argument (small δ)
is clean. The exact argument (arbitrary δ ∈ (−1/2, 1/2)) requires
promoting to the full formula. Is this done rigorously?

(f) **Dependence on the integrality premise.** Baker only fires
if the integrality constraint from Point B2 is valid. **If the
cohomology-class lemma (B2(c)) is not established, Baker operates
on a premise that may not hold.** The B2 lemma and the C1
application must be chained correctly.

---

### Point C2: The Cocycle Shift Formula — Properties [MEDIUM]

**Location:** §7 (continued)

**Interrogate:**

(a) **Algebraic verification.** Verify Δc(0) = 0. Verify
Δc(δ) ≠ 0 for δ ∈ (−1/2, 1/2) \ {0}. Any singularities?

(b) **Pole-free in the critical strip.** Verify the formula is
well-defined for all relevant δ.

(c) **Field independence.** The paper claims field independence —
same formula over Q and Q(i) with p → N(𝔭). Is this because the
Euler factor structure is the same, or are there subtleties at
ramified primes (p = 2 in Q(i))?

---

### Point D1: The CM L-Function Factorization [MEDIUM]

**Location:** §10

**Interrogate:**

(a) **Deuring 1953.** Is the theorem correctly stated and cited?
Conditions on E and K? Standard modern reference: Silverman
*Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II.

(b) **Grössencharacter identification.** ψ is determined by E and
the CM field K. Is ψ correctly identified for the test curves?
**Cross-check LMFDB** for y²=x³−x (CM by Q(i)), y²=x³−1
(CM by Q(√−3)), etc.

(c) **The zero set of L(E, s).** L(E, s) = L(s, χ_K) · L(s, ψ),
so zeros are the union. Verify the spectral method covers both
factors (see MY3).

(d) **Modularity of CM curves.** Needed for Kolyvagin, GZ.
Classical for CM curves (Hecke, pre-Wiles). Or cite BCDT 2001.

---

### Point D2: Kolyvagin at Rank 0 [MEDIUM]

**Location:** §11

**Interrogate:**

(a) **Kolyvagin hypotheses.** Modularity of E (classical for CM);
L(E, 1) ≠ 0. For rank 0 Kolyvagin does not need a Heegner point
of infinite order.

(b) **Analytic rank 0 vs L(E, 1) ≠ 0.** GRH says zeros lie on
Re s = 1/2, so s = 1 is NOT on that line — GRH alone does not
imply L(E, 1) ≠ 0. One needs the analytic rank to be 0 as a
separate input. How is the analytic rank determined for curves in
scope?

(c) **The BSD formula at rank 0.** All terms computed.
**Cross-check against LMFDB — the internal adversarial review
flagged c_2 for y²=x³−x.** Verify the fix is in the release
candidate.

---

### Point D3: Gross-Zagier + Kolyvagin at Rank 1 [HEAVY]

**Location:** §12

**Interrogate:**

(a) **Gross-Zagier formula.** L'(E, 1) = ĥ(P_K) · (period/volume
factor). Verify the statement cited.

(b) **Heegner hypothesis — the conductor issue.** For y²=x³−x
(conductor 32), the prime 2 ramifies in Q(i), so the classical
Heegner hypothesis fails for K = Q(i). The paper must:
- Use an auxiliary imaginary quadratic field K' ≠ K where the
  Heegner hypothesis holds (e.g., K' = Q(√−7) with disc −7
  coprime to 32), and
- Cite the generalized Gross-Zagier formula (Yuan-Zhang-Zhang
  2013) to handle the modified setup.

Is this done cleanly?

(c) **Kolyvagin bound.** For modular curves with analytic rank
exactly 1, Kolyvagin gives rank ≤ 1. Combined with non-torsion
Heegner point: rank = 1 exactly.

(d) **The BSD formula at rank 1.** Includes the regulator
R = ĥ(generator) or a rational multiple. Verify all terms.
Cross-check LMFDB.

(e) **Extension to all nine class-number-1 fields.** Does the
argument work uniformly? Q(√−3) has unit group {±1, ±ω, ±ω²},
larger than Q(i) — does this affect anything?

---

### Point E1: The Assembly [HEAVY]

**Location:** §13

**Interrogate:**

(a) **Chain integrity at the rigor standard.** Walk through the
full 11-step chain. Label each step [THEOREM], [LEMMA], or
[KEY LEMMA — OPEN] per the yang-mills rigor standard. Identify
the weakest link. Candidates: MY3 (bridge → L(s, ψ)?), B2
(cohomology-class vs representative), C1 (what Baker actually
gives), D3 (Heegner hypothesis).

(b) **Logical structure.** The proof is by reduction:
BC over K → Meyer → Nelson → bridges → cocycle shift → Baker →
δ = 0 → GRH for L(E, s) → Kolyvagin/GZ → BSD. Verify every link.

(c) **Conditional vs unconditional.** Is the proof unconditional
(modulo cited standard results), or does it depend on additional
unverified assumptions (internal research/N notes, unproven
lemmas)? List every dependency.

(d) **What Paper 26 contributes that is new.** What is the
genuinely novel mathematical content? The bridge family over
Q(i), the cocycle shift over K, and the assembly from GRH-for-CM-
L-functions to BSD (via known Kolyvagin/GZ) are candidate "new"
items. Verify each.

(e) **Comparison to Connes' programme.** Connes and others have
worked on BSD via noncommutative geometry. What makes Paper 26's
approach succeed (or nearly succeed) where earlier attempts have
not? What is structurally different?

(f) **The most likely failure point.** Based on your expert
judgment, where is the proof most likely wrong? Rank the
candidates with one-sentence explanations.

---

### Point E2: Adversarial Review — Independent Check [MEDIUM]

**Location:** §17 + `01-adversarial-proof-review.md` (internal)

The internal adversarial review (research/05) reported 15 attacks:
8 SURVIVED, 5 WEAKENED, 2 BROKEN. The BROKEN items were:

- **Issue 1 (BROKEN):** Conditionality inheritance (paper claimed
  "unconditional" but inherited conditionality on internal axioms).
- **Issue 3 (BROKEN):** Heegner hypothesis failure for y²=x³−x at
  prime 2 + c_2 numerical error.

The WEAKENED items were:
- Twist argument for L(s, ψ) phase insensitivity.
- Heegner hypothesis scope.
- h_K > 1 scope.
- "Nothing changes" claim (from Q to Q(i)).
- Gap inheritance framing.

**Interrogate:**

(a) **Have the 2 BROKEN issues been fixed in the current release
candidate?** Verify in the preprint sections.

(b) **Are the 5 WEAKENED items still weak, or adequately
strengthened?** Independent check — do not adopt the internal
verdict.

(c) **What did the internal review miss?** Your job as external
referee is to find new issues. Propose new attacks not in the
internal list. Record them as candidate gaps.

---

## Output Format

Write all report files into:
`/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/latest-run/`

### Directory layout (mandatory)

**Do NOT write giant monolithic files.** Organize as:

```
latest-run/
├── INDEX.md                          ← navigation
├── rigor-checklist.md                ← master roll-up (~35 rows)
├── rigorous-proof.md                 ← yang-mills-standard reformulation (PRIMARY OUTPUT)
├── summary.md                        ← overall rigor verdict
├── computation-log.md                ← every "verified in venv" note
├── points/
│   ├── A1-ha-paugam/
│   │   ├── 00-statement.md
│   │   ├── 01-algebra.md
│   │   ├── 02-kms-uniqueness.md
│   │   ├── 03-gns.md
│   │   └── verdict.md
│   ├── A2-nelson/
│   ├── A3-meyer-spectral/            ← HEAVY
│   ├── B1-bridge-family/
│   ├── B2-cocycle-shift/             ← HEAVY
│   ├── B3-itpfi/
│   ├── C1-baker/                     ← HEAVY
│   ├── C2-cocycle-properties/
│   ├── D1-cm-factorization/
│   ├── D2-kolyvagin-rank0/
│   ├── D3-gross-zagier-rank1/        ← HEAVY
│   ├── E1-assembly/                  ← HEAVY
│   └── E2-adversarial/
└── checks/
    ├── R-rank/R1.md .. R3.md
    ├── LC-leading-coefficient/LC1.md .. LC7.md
    ├── AC-analytic-continuation/AC1.md .. AC3.md
    ├── BC-bost-connes/BC1.md .. BC5.md
    ├── MY-meyer/MY1.md .. MY4.md
    ├── BR-bridge/BR1.md .. BR8.md
    ├── IT-itpfi/IT1.md .. IT3.md
    ├── TR-transcendence/TR1.md .. TR6.md
    ├── DS-dark-states/DS1.md .. DS3.md
    ├── CM-cm-factorization/CM1.md .. CM4.md
    ├── KV-kolyvagin/KV1.md .. KV4.md
    ├── GZ-gross-zagier/GZ1.md .. GZ7.md
    └── SHA-tate-shafarevich/SHA1.md .. SHA3.md
```

**No file in this tree should exceed ~300 lines.**

### The mandatory `rigorous-proof.md` output (PRIMARY DELIVERABLE)

This is the yang-mills-standard reformulation. Structure (mirroring
`paper08-yang-mills/research/21-the-rigorous-proof.md`):

```markdown
# The Pure Mathematics Proof — BSD for CM curves (r01)

## I. Definitions
(precise definitions: elliptic curve over ℚ, L-function, rank,
Mordell-Weil group, Tate-Shafarevich group, regulator, BC algebra
over K, bridge cocycle, spectral operator T_{BC,K}, cocycle shift
Δc(δ), etc.)

## II. Main Theorem
(the precise statement Paper 26 claims to prove, for the CM rank
0+1 scope)

## III. Lemma 1: BC over Q(i) [label]
(precise statement + proof status + citation if inherited)

## IV. Lemma 2: Meyer-Nelson spectral inclusion [label]
(precise statement + proof status — probably [KEY LEMMA] for ψ)

## V. Lemma 3: Bridge family and the cocycle shift [label]
(precise statement including the cohomology-class subpoint)

## VI. Lemma 4: Baker kill [label]
(precise statement, conditional on Lemma 3)

## VII. Lemma 5: GRH for CM L-functions [label]
(assembled from Lemmas 1-4)

## VIII. Lemma 6: Kolyvagin rank 0 [label]
## IX. Lemma 7: Gross-Zagier + Kolyvagin rank 1 [label]
## X. Assembly of the Proof
(combining the lemmas into the main theorem; explicit step-by-step)

## XI. What Paper 26 contributes (new vs standard)
| Step | Standard literature | Paper 26 contribution |

## XII. The Key Lemmas: precise statements and proof strategies
(for any [KEY LEMMA — OPEN] items: precise statement, evidence,
and proof strategy)

## XIII. Rigor scorecard
- Steps at [THEOREM]: _/11
- Steps at [LEMMA]: _/11
- Steps at [KEY LEMMA — OPEN]: _/11
- Steps at [GAP]: _/11
```

**Every step must have a label.** If a step cannot receive a
label because the preprint does not state it precisely, that is
a finding — record it as [GAP] with a brief note.

### File templates

**`points/<point-id>/00-statement.md`**:

```markdown
## Point [ID]: [Title]

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Location in preprint:** [section reference]

**The claim:**
[Exact claim from the prompt's Point description.]

**Rigor label (tentative):** [THEOREM / LEMMA / KEY LEMMA — OPEN / GAP]

**Sub-questions to be answered (one file each):**
- (a) [01-...md]
- (b) [02-...md]
...
```

**`points/<point-id>/0N-<name>.md`**:

```markdown
## Point [ID]([letter]): [Sub-question title]

**The question:**
[Quote verbatim.]

**Finding:**
[Detailed answer. Quote relevant claims. Be precise.]

**Computational verification (if applicable):**
[Result of any mpmath/sympy/LMFDB check.]

**Rigor label for this sub-question:**
[THEOREM / LEMMA / KEY LEMMA — OPEN / GAP]

**Verdict:**
[SOUND / CLOSABLE GAP / GENUINE GAP, with one-line justification.]
```

**`points/<point-id>/verdict.md`**:

```markdown
## Point [ID]: [Title] — Verdict

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Overall rigor label:** [THEOREM / LEMMA / KEY LEMMA — OPEN / GAP]
**Overall verdict:** [GENUINE GAP / CLOSABLE GAP / SOUND]

**Sub-question verdicts:**
- (a): [label] [SOUND/CLOSABLE/GENUINE] — [one line]
...

**Combined finding:**
[1–2 paragraphs synthesizing.]

**If this is a gap:**
- **Difficulty:** [1 paragraph / 1 page / 1 paper / novel research]
- **What is needed:** [precise statement]

**Impact on the claimed result:**
[Which of: (i) GRH for CM L-functions; (ii) BSD rank 0; (iii) BSD
rank 1; (iv) strong BSD (leading coefficient).]
```

**`checks/<group>/<id>.md`**:

```markdown
## Check [ID]: [Title]

**Group:** [R / LC / AC / BC / MY / BR / IT / TR / DS / CM / KV / GZ / SHA]
**Source:** [preprint section]
**Pass criterion:** [quote from prompt]

**Verdict:** [PASS / PARTIAL / FAIL]
**Rigor label:** [THEOREM / LEMMA / KEY LEMMA — OPEN / GAP]

**Justification:**
[One paragraph.]

**Cross-references:**
- Per-Point file(s): [points/<point-id>/...]
```

**`rigor-checklist.md`** — master roll-up:

```markdown
# Rigor Audit Master Roll-Up

| ID | Verdict | Rigor label | One-line summary | File |
|:---|:--------|:------------|:-----------------|:-----|
| R1 | ... | ... | ... | checks/R-rank/R1.md |
| ... | ... | ... | ... | ... |

**Verdict totals:**
- PASS: ___
- PARTIAL: ___
- FAIL: ___

**Rigor label totals:**
- [THEOREM]: ___
- [LEMMA]: ___
- [KEY LEMMA — OPEN]: ___
- [GAP]: ___
```

**`summary.md`** should end with:

```markdown
## Overall Rigor Assessment

**Is the BSD proof (for the CM rank 0+1 scope) rigorously established?**
[Yes / Yes modulo acknowledged open lemmas / No, and here are the gaps]

**The rigor scorecard:**
- Steps at [THEOREM]: ___/11
- Steps at [LEMMA]: ___/11
- Steps at [KEY LEMMA — OPEN]: ___/11
- Steps at [GAP]: ___/11

**The single most critical issue:**
[One sentence.]

**The three most critical issues (ranked):**
1. [One sentence]
2. [One sentence]
3. [One sentence]

**What would close the gaps (if any):**
[Precise statement.]

**Tools added during this run** (if any):
[List.]

**Note on Clay eligibility:** This audit does NOT assess Clay
Millennium Prize eligibility. See `02-clay-referee.md` for the
Clay compliance audit.
```

---

## Closing instructions (REQUIRED in summary.md)

1. **The rigor scorecard.** State the number of proof-chain steps
   at each rigor level ([THEOREM] / [LEMMA] / [KEY LEMMA — OPEN] /
   [GAP]) out of 11 total.

2. **The cohomology-class lemma (B2).** State explicitly whether
   Paper 26 establishes that the cocycle SHIFT induces a genuine
   shift in the cohomology CLASS (not merely the representative).
   This is the load-bearing lemma for the bridge mechanism. If
   the paper does not state or prove this lemma precisely, flag
   it as [GAP].

3. **Does the bridge reach L(s, ψ)?** State your verdict on
   whether the spectral method over Q(i) captures the
   Grössencharacter L-function L(s, ψ) — not just ζ_K(s). This
   is necessary for the CM factorization chain to close.

4. **Kolyvagin and Gross-Zagier applicability.** State whether
   the cited results are used within their actual scope, including
   modularity prerequisites and the Heegner hypothesis at
   ramified-conductor primes.

5. **What Paper 26 contributes (new vs standard).** State clearly
   what the paper adds versus what it inherits.

6. **Tools added during this run** (if any).

---

Do not be diplomatic. Do not praise the work. Don't hurry. Don't
take shortcuts. Find the gaps.

If you cannot find a gap in a specific argument, say so explicitly
and explain why — that is also valuable information.

# Your north star

This claims to prove (a significant partial case of) one of the
seven Millennium Prize problems. Your job is to audit the **rigor**
of the proof chain against the yang-mills standard, not to assess
Clay eligibility.

Your single deliverable is `rigorous-proof.md` — the pure-math
reformulation with every step labeled [THEOREM], [LEMMA],
[KEY LEMMA — OPEN], or [GAP]. Every other file in `latest-run/`
supports that central output.

The most likely failure modes for bridge-based proofs of
GRH-for-CM-L-functions:

1. **The cohomology-class vs representative question.** The
   integrality constraint Δc(δ) ∈ (1/k)ℤ may fail to force δ = 0
   because a coboundary absorbs the shift — the shift of the
   representative need not shift the class. This is a concrete,
   structural risk for any H²-based bridge proof. The paper must
   establish the class-shifting lemma precisely.

2. **The bridge does not reach L(s, ψ).** The Bost-Connes system
   over K captures ζ_K, not arbitrary Hecke L-functions. The CM
   factorization L(E, s) = L(s, χ_K) · L(s, ψ) requires the
   spectral method to cover the ψ factor.

3. **Distributional spectrum vs point spectrum.** Meyer gives
   distributional eigenstates. Nelson gives a self-adjoint
   extension. The upgrade from distributional to genuine point
   spectrum is non-automatic.

4. **Kolyvagin or Gross-Zagier misapplied.** Heegner hypothesis
   for curves whose conductor primes ramify in the CM field;
   analytic rank determination; auxiliary Heegner field choice;
   modularity prerequisite.

5. **BSD leading-coefficient terms computed incorrectly.** The
   internal adversarial review flagged c_2 for y²=x³−x; cross-
   check all local factors against LMFDB.

Check ALL of these. And find any that are not on this list.
