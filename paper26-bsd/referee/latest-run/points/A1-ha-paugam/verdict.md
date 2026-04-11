# Point A1 — Ha-Paugam BC system over Q(i): Verdict

**Weight:** MEDIUM
**Location in preprint:** §3.1–3.5
**Overall rigor label:** **[LEMMA]** (with citation gap)
**Overall verdict:** PASS on CCM authority + citation gap

## Sub-question verdicts

- **(a) The Ha-Paugam algebra construction.** [THEOREM] — Ha-Paugam
  2005 constructs A_{BC,K} = C*(K̂^{ab}) ⋊ I_K as a semigroup crossed
  product. The paper's specialization to K = Q(i) is faithful.
  Standard construction.

- **(b) KMS_1 uniqueness and class number.** [LEMMA] — Correct but
  **citation incomplete**. Paper cites Bost-Connes 1995 Theorem 25
  "by the same argument," but this argument is specific to Q. The
  extension to number fields requires **Laca-Larsen-Neshveyev 2015**
  ("KMS states on the C*-algebras of finite graphs"), which
  establishes KMS_β uniqueness for BC-Hecke systems over number
  fields with h_K = 1. Paper does not cite LLN 2015. Also, the
  enlarged unit group O_K^× = {±1, ±i} does not obstruct KMS
  uniqueness (since the unit group is finite, it contributes only
  finitely many orbits to the KMS analysis). Attack 3 from internal
  adversarial review flagged this citation gap; the rigor audit
  confirms it.

- **(c) The GNS Hilbert space H_{1,K} is type III_1.** [THEOREM]
  — Proposition 3.5 argues via the Connes spectrum: the set
  {N(𝔭)^{it} : 𝔭 prime, t ∈ ℝ} generates a dense subgroup of
  ℝ_+^* because prime norms include all rational primes p ≡ 1
  (mod 4) and all p² for p ≡ 3 (mod 4). Standard Connes-Takesaki
  classification gives III_1.

## Combined finding

The Bost-Connes system over Q(i) is well-defined and inherits the
standard operator-algebraic properties from Ha-Paugam 2005. The
unique KMS_1 state exists because h_K = 1. The GNS Hilbert space
is a type III_1 factor. All of this is standard once the correct
citations are in place.

**The citation gap to Laca-Larsen-Neshveyev 2015** is an editorial
fix (add one reference). The underlying mathematics is sound. No
[KEY LEMMA — OPEN] items here.

## Impact on the claimed result

**Low-severity concern.** Layer 1 of the proof chain. All
downstream steps depend on this layer, but since the content is
standard (modulo citation completeness), it does not introduce
novel risk.

## Action item

Add citation: Laca, M., Larsen, N. S., Neshveyev, S. (2015),
"Phase transition in the Connes-Marcolli GL₂-system," alongside
Ha-Paugam 2005 in §3.1 and §3.4.
