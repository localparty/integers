# BSD Math Referee — Summary (Run r01)

*Paper 26: "The Bridge Extends — BSD for CM Elliptic Curves"*
*Reviewer: Claude Opus 4.6 as math referee (Run r01, 2026-04-10)*
*Scope: rigor audit at the yang-mills standard. Clay eligibility is*
*the job of `02-clay-referee.md`, not this run.*

---

## Bottom line

**Paper 26 is not yet a rigorous proof of BSD for CM rank 0+1 at
the yang-mills standard.** The chain is structurally plausible
and the downstream classical components (Deuring, Kolyvagin,
Gross-Zagier, Baker) are correctly cited. But the upstream
"bridge produces GRH for CM L-functions" argument has **three
[KEY LEMMA — OPEN] items** that the paper asserts but does not
prove, **one [GAP]** where the worked example table is broken,
and **two editorial errors** found by computational check.

**None individually kills the proof**, but the collective state
leaves the BSD claim short of what the yang-mills rigor bar
requires.

**The substantive novel content of Paper 26 — extending the BC
spectral method from ℚ to ℚ(i) so it reaches Hecke L-functions
and hence CM L(E, s) — is asserted but not carried out at the
level of full mathematical proof.** The rest is inherited
(Deuring, Kolyvagin, Gross-Zagier, Baker) or standard operator-
algebra (Nelson, ITPFI).

---

## The rigor scorecard

For the 11-step chain (Paper 26 §9.1 + §§10–12):

| Count | Label | Steps |
|:-----:|:------|:------|
| 4/11 | **[THEOREM]** | BC existence (Ha–Paugam); Nelson self-adjointness; cocycle shift formula; CM factorization (Deuring) |
| 3/11 | **[LEMMA]** | KMS_1 uniqueness (citation gap to LLN 2015); ITPFI factorization; Baker kill (conditional on integrality premise) |
| 3/11 | **[KEY LEMMA — OPEN]** | Meyer distributional → point spectrum upgrade; twisted spectral inclusion for L(s, ψ); cohomology-class integrality |
| 1/11 | **[GAP]** | Proposition 4.3 bridge table (3 of 4 rows broken per the audit's computational check) |

Note: Kolyvagin (rank 0) and Gross-Zagier + Kolyvagin (rank 1)
are [THEOREM] from the literature but apply within the proof only
**conditional** on the upstream GRH, which is itself [KEY LEMMA
— OPEN]. The rank-1 case is additionally **vacuous** within the
claimed scope (Paper 26's own Remark 12.6: GRH implies L(1, ψ) ≠
0, so CM curves in scope cannot have analytic rank 1 over ℚ).

---

## The single most critical issue

**The cohomology-class integrality premise (Proposition 7.3(v)).**

The entire bridge kill mechanism rests on the claim that a shift
Δc(δ) ≠ 0 of the cocycle **representative** produces a shift of
the cohomology **class** in H²(ℤ/kℤ, U(1)) ≅ ℤ/kℤ. The paper
asserts this by saying "the bridge cocycle must remain in (1/k)ℤ
for the bridge to be well-defined," which conflates the
representative with the class. Without an explicit class-shifting
lemma, Baker's theorem (which fires on the integrality constraint)
operates on a premise that may not hold.

The referee-required precise lemma:

> *Let β(δ) ∈ Z²(ℤ/kℤ, U(1)) be the cocycle representative
> obtained from the spectral shift at parameter δ. Let
> [·] : Z² → H² be the class map. Then [β(δ)] ≠ [β(0)] for
> δ ∈ (−1/2, 1/2) \ {0}.*

Paper 26 does not state, prove, or even acknowledge this lemma.

---

## The three most critical issues (ranked)

1. **Cohomology-class integrality premise is asserted, not
   proved** (Proposition 7.3(v) / Key Lemma C in rigorous-proof.md).
   This is the load-bearing item for the Baker kill.

2. **Meyer–Nelson upgrade for ζ_K and twisted spectral inclusion
   for L(s, ψ)** (Key Lemmas A and B). The paper asserts both by
   analogy with Meyer 1997 and Connes–Marcolli 2008 §4.3 (both
   stated for ℚ); neither extension to K = ℚ(i) is carried out.
   Without these, GRH for CM L-functions is not established.

3. **Proposition 4.3's "minimal conductor" bridge table is broken.**
   Three of its four rows are wrong (per computational check C5):
   - k=2: paper's own [ERRATUM] admits wrong Frobenius
   - k=4: ((2+i), (5)) is invalid — (2+i) divides (5), so
     Frobenius is undefined
   - k=6: paper claims ord(2) = 1 in (ℤ/7ℤ)^×, but actually
     ord(2) = 3, giving k = φ(7)/3 = 2, not 6
   Only the k=3 row ((3+2i), (7)) is correct.

---

## What would close the gaps

### For Key Lemma C (cohomology class)

A direct computation in H²(ℤ/kℤ, U(1)) showing that the spectral
shift map δ ↦ [β(δ)] is injective on (−1/2, 1/2). This is a
well-defined group-cohomology exercise; either the shift changes
the class or it doesn't.

### For Key Lemmas A + B (Meyer-Nelson + twist)

Either:
- **Direct route:** state Meyer 1997 precisely, extend it to ζ_K
  by re-verifying the explicit formula computation with Λ → Λ_K,
  then carry out the distributional-to-genuine upgrade via the
  Connes trace formula technology over number fields.
- **Alternative architecture:** adopt the Paper 13 v2 route
  (CCM + ITPFI + Bögli + Hurwitz) and extend it to number fields.
  This would require a "CCM for number fields" result that does
  not appear to be in the current literature.

### For Proposition 4.3 (bridge table)

Recompute the minimal-conductor table using correct Frobenius
orders. Independently verify Proposition 4.2's claim of 355
bridge triples. Supply at least two valid bridge triples with
distinct norms explicitly, so that Baker's argument has concrete
inputs to operate on.

### For the editorial errors

- **Table 8.1** (E1): recompute all log-ratios in mpmath at 30+
  digits.
- **Ω formula** (E2): replace `Γ(1/4)² / (2π)^{3/2}` with
  `Γ(1/4)² / (2·√(2π))`. The numerical value 2.62205755 and
  downstream BSD closure are correct.

---

## Computational verification summary

All checks run in the venv at
`paper26-bsd/referee/code/.venv/` using mpmath at 60–150 digit
precision. Details in `computation-log.md`.

| Check | Target | Result |
|:------|:-------|:-------|
| C1 | Dedekind zeta Euler product ζ_K(s) at s = 2, 3, 4 | PASS (diff < 1e-4 at s=2 with 2000 primes) |
| C2 | Cocycle shift formula + Table 7.4 | PASS (paper's 7.856835e-3 at N=5 matches) |
| C3 | Table 8.1 log-ratios | **4 of 5 WRONG** (Editorial E1) |
| C4a | Ω_E formula in §13.3 | **WRONG BY FACTOR OF π** (E2) |
| C4b | Ω_E numerical value and BSD closure at rank 0 | PASS (with c_2 = 4 per LMFDB) |
| C5 | Proposition 4.3 bridge table | **3 of 4 rows broken** (Gap G1) |
| C6 | Proposition 4.2 "355 triples" | NOT VERIFIED |

---

## Closing statements (mandatory per 01-math-referee.md)

### 1. The cohomology-class lemma (B2/VII.B)

**Verdict:** Paper 26 does NOT establish that the cocycle SHIFT
induces a genuine shift in the cohomology CLASS. The paper's
Proposition 7.3(v) asserts the integrality constraint by saying
"the bridge cocycle must remain in (1/k)ℤ for the bridge to be
well-defined," which is a statement about the class but is
justified as if it were a statement about the representative.
The precise class-shifting lemma (see Key Lemma C in
rigorous-proof.md §XIII) is not stated or proved. **Flagged as
[KEY LEMMA — OPEN]**, bordering on [GAP].

### 2. Does the bridge reach L(s, ψ)?

**Verdict:** Paper 26 ASSERTS that the twisted spectral
realization of Connes–Marcolli 2008 §4.3 extends from ℚ to
K = ℚ(i), giving a twisted BC operator T_{BC,K}^ψ whose
distributional spectrum contains the zeros of L(s, ψ). The
extension is **asserted by analogy**; it is not carried out.
The critical technical step (twisting over number fields, not
just over ℚ) is not verified. **Flagged as [KEY LEMMA — OPEN].**

### 3. Kolyvagin and Gross-Zagier applicability

**Verdict:** Kolyvagin's theorem at rank 0 and Gross-Zagier +
Kolyvagin at rank 1 are correctly cited and applied within their
actual scope. Modularity for CM curves is classical (Hecke theta
series), so the modularity prerequisite is met. The Heegner
hypothesis for y² = x³ − x (where prime 2 ramifies in ℚ(i)) is
correctly flagged by the paper as requiring either the
Yuan–Zhang–Zhang 2013 generalization or an auxiliary field like
ℚ(√−7); the paper mentions both but does not commit to one. This
is sufficient for the literature existence check but not for a
watertight proof. **Rank-1 is vacuously satisfied per Paper 26's
own Remark 12.6** — all CM curves in scope have analytic rank 0
once GRH is established.

### 4. What Paper 26 contributes (new vs standard)

The genuinely new mathematical content of Paper 26, reduced to
essentials:
- **The extension of the BC spectral method from ℚ to ℚ(i)** so
  that it reaches Hecke L-functions and hence CM L(E, s).
- **The bridge family over ℚ(i)** (claimed 355 triples; only the
  k=3 example at ((3+2i), (7)) is verified; the other minimal-
  conductor examples are broken).
- **The assembly** from GRH-for-CM-L-functions to BSD at rank
  0 and 1 (using classical Kolyvagin/Gross-Zagier).

Everything else is either inherited from the standard literature
(Ha–Paugam, Nelson, Meyer, Baker, Deuring, Kolyvagin, Gross–
Zagier, BCDT modularity) or from Paper 13 (the bridge family
construction and cocycle shift derivation over ℚ).

**The synthesis is programmatically interesting but mathematically
under-developed at the yang-mills rigor standard.** The novel
pieces are not carried out in the preprint; they are asserted by
analogy.

### 5. Tools added during this run

None. All checks performed with the default venv packages
(sympy, mpmath, numpy, scipy, pypdf). No additional libraries
needed for the rigor audit.

---

## Is BSD for CM rank 0+1 established?

**Conditional on the three [KEY LEMMA — OPEN] items being
closed** and **Proposition 4.3 / 4.2 being rebuilt correctly**,
the chain as Paper 26 presents it would yield BSD for CM curves
with CM by a class-number-1 imaginary quadratic field and analytic
rank 0 (the rank-1 case being vacuous per Remark 12.6).

**As currently written**, the proof is at the "structurally
complete but rigorously incomplete" stage. It is plausible;
the pattern is right; the classical downstream components are
sound. But the bridge → GRH step — the novel content — is
asserted more than proved.

---

## Rating

- **Rigor of the overall architecture:** 7/10 (plausible,
  correct shape, classical downstream components sound)
- **Rigor of the novel content (bridge → GRH for L(s, ψ)):**
  4/10 (three [KEY LEMMA — OPEN] items, one [GAP])
- **Numerical/editorial quality:** 6/10 (Ω formula wrong,
  Table 8.1 wrong in 4/5, Prop 4.3 broken in 3/4)
- **Overall rigor audit verdict:** 5-6/10 — in the same state as
  Paper 13 was before its 9 referee fixes, but for a harder target
  (BSD is a more demanding theorem than RH, even for CM rank 0+1).

**Projected rating after closing the 3 key lemmas + fixing the
gap and editorial errors:** 7-8/10, comparable to Paper 13's
current post-fix state. Reaching 9/10 would additionally require
having the cited preprints (Ha–Paugam, Laca–Larsen–Neshveyev,
Yuan–Zhang–Zhang) integrated into a complete bibliography and
independent expert review.

---

## Coordination with the Clay referee

This rigor audit is the input the Clay compliance audit
(`02-clay-referee.md`) needs. Specifically:

- The **rigor scorecard** (4/3/3/1) means that the mathematics is
  not yet "complete" in the sense of Clay §5(a).
- The **three [KEY LEMMA — OPEN] items** and **one [GAP]** mean
  the paper is "conditional" on open lemmas, regardless of whether
  the paper's own framing calls itself "unconditional."
- The **rank-1 vacuity (Remark 12.6)** means the substantive
  content is entirely at rank 0, which is a narrower claim than
  the paper's "BSD for rank 0 AND 1" framing suggests.

When the Clay referee runs next (see `02-clay-referee.md` Point
CA10), it should reference this file (`rigorous-proof.md` and
this summary) and conclude that **Clay §5(a) (complete solution)
is not met at the mathematical level**, regardless of publication
status (Clay §4(a-c)).

---

*End of summary. Primary deliverable: `rigorous-proof.md` (the
yang-mills-standard reformulation). Supporting outputs:
`rigor-checklist.md`, `computation-log.md`, and the per-point
and per-check files in `points/` and `checks/`.*
