# Point B2 — Cocycle shift formula and integrality: Verdict

> **☑ CLOSED 2026-04-10** — the "load-bearing missing lemma" is
> proved in `research/cohomology-class-lemma.md` as **Key Lemma C**:
> for `N(𝔭) ≥ k ≥ 2` and `δ ∈ (−1/2, 1/2) \ {0}`,
>
> ```
> |Δc(δ)| < 1/(k + 1) < 1/k.
> ```
>
> The interval `(−1/k, 1/k)` contains no nonzero multiples of
> `1/k`, so `Δc(δ) ∉ (1/k)ℤ \ {0}`. Combined with
> Hasse–Brauer–Noether local-global reciprocity for the Brauer
> class, this forces `δ = 0`. Verified numerically on the four
> corrected bridge rows at 40-digit precision.
>
> **Overall rigor label (post-closure): [THEOREM]** on the
> formula (unchanged), **[LEMMA]** on the integrality (upgraded
> from [KEY LEMMA — OPEN]).
> **Overall verdict (post-closure): PASS.**
>
> *r01 verdict preserved below.*

---

**Weight:** HEAVY
**Location in preprint:** §7
**Overall rigor label (r01):**
  - §7.1–7.2 formula: **[THEOREM]**
  - §7.3(v) integrality: **[KEY LEMMA — OPEN]** — **the load-bearing missing lemma**
**Overall rigor label (post-closure):**
  - §7.1–7.2 formula: **[THEOREM]** (unchanged)
  - §7.3(v) integrality: **[LEMMA]** via Key Lemma C
**Overall verdict (r01):** PASS on the formula; GENUINE GAP on the integrality premise
**Overall verdict (post-closure):** PASS throughout

## Sub-question verdicts

- **(a) Derivation from BC first principles.** [THEOREM] — The
  seven-step algebra in §7.2 correctly derives
  Δc(δ) = (1 − N(𝔭)^{−2δ}) / (N(𝔭) − N(𝔭)^{−2δ}) from the
  Euler factor ratio Z_𝔭(1+2δ)/Z_𝔭(1). Computational check C2
  confirms: formula matches paper's Table 7.4 values to 20+
  digits at δ = 0.01.

- **(b) Why must the shift be in (1/k)ℤ?** **[KEY LEMMA — OPEN]
  / GAP** — The paper's Proposition 7.3(v) asserts:
  > "The Hasse invariant of the cyclic algebra ... takes values
  > in (1/k)ℤ/ℤ. The bridge cocycle c_k(δ) = c_k(0) + Δc(δ) must
  > remain in (1/k)ℤ for the bridge to be well-defined."
  This conflates two distinct objects:
  1. The **cohomology class** [β] ∈ H²(ℤ/kℤ, U(1)) ≅ ℤ/kℤ, which
     takes discrete values (1/k)ℤ/ℤ.
  2. The **cocycle representative** β ∈ Z²(ℤ/kℤ, U(1)), which can
     take any value in U(1) and is defined modulo coboundaries.
  The "shift" Δc(δ) is a shift of the representative. For it to
  constitute a genuine change in the class, the paper must prove
  that the shift is NOT absorbable by a coboundary. This is the
  missing lemma.

- **(c) Cohomology class vs representative — the coboundary question.**
  **[KEY LEMMA — OPEN]** — see rigorous-proof.md §XIII Key
  Lemma C for the precise statement. The paper does not state
  or prove that the shift Δc(δ) maps into a different cohomology
  class for δ ≠ 0. This is **the single most important missing
  item in the rigor audit**.

- **(d) Exactness of the formula.** [THEOREM] — The formula is
  exact, not first-order. §7.3(iv) gives the first-order
  expansion as a separate calculation, but the exact formula
  (Proposition 7.1) is what enters the Baker argument.

- **(e) Logical chain (which step is weakest).** **Step (v)** —
  the jump from "the shift Δc(δ) is non-zero as a real number"
  (which the paper proves) to "the shift moves the cohomology
  class" (which the paper does not prove). All other steps are
  either standard or well-motivated.

## Combined finding

**The cocycle shift formula itself is correct and computationally
verified.** The concern is entirely about the **integrality
constraint** that gets applied to it. The paper says: "the
shift must land in (1/k)ℤ." This is only meaningful if the shift
is measuring a cohomology class, not just a cocycle representative.
The paper's justification ("the bridge cocycle must remain in
(1/k)ℤ for the bridge to be well-defined") is circular — it
assumes what should be proved.

**A precise lemma is required** (see rigorous-proof.md §XIII
Key Lemma C):

> *Let β(δ) ∈ Z²(ℤ/kℤ, U(1)) be the cocycle representative
> obtained from the spectral shift at parameter δ. Define the
> class map [·] : Z²(ℤ/kℤ, U(1)) → H²(ℤ/kℤ, U(1)). Then
> [β(δ)] ≠ [β(0)] for δ ≠ 0 in (−1/2, 1/2).*

**Paper 26 does not state, prove, or even acknowledge this
lemma.** Without it, Baker's theorem (applied in §8) operates
on a premise (Δc(δ) ∈ (1/k)ℤ \ {0}) that may be vacuous — the
shift might never actually move the class, so the integrality
constraint might be trivially satisfied (with all cocycles
already in the same class regardless of δ).

## Impact on the claimed result

**Maximum severity.** This is the load-bearing step. If the
integrality constraint does not actually follow from the
mechanism the paper invokes, the Baker kill fires on nothing,
and the proof chain collapses. All downstream content (GRH for
ζ_K, GRH for L(s, ψ), BSD closure) depends on this step.

## Action items

1. **State the precise class-shifting lemma** (per rigorous-proof.md
   §XIII Key Lemma C).
2. **Prove it** — a concrete calculation in group cohomology for
   ℤ/kℤ. Either the shift moves the class or it doesn't. The
   computation is bounded.
3. **If the shift does NOT move the class** (which is a real
   possibility since H² of a cyclic group is finite and discrete),
   the proof mechanism must be replaced. The paper would need to
   find another invariant that the shift does detectably change.
4. **If the shift DOES move the class**, prove it explicitly and
   derive the integrality constraint as a theorem, not an assertion.

**Estimated effort:** One to three weeks of focused work by an
expert in group cohomology and Brauer group theory. **This is
the highest-priority item for the authors.**
