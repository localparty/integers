# Check TR5: Argument works for exact formula, not just first order

**Group:** TR
**Source:** Paper 26 §8.3 Step 5
**Pass criterion:** Promotion from first-order to exact rigorous.

**Verdict:** PARTIAL
**Rigor label:** [LEMMA] with edge-case concern

**Justification:** The paper's Step 5 promotes the first-order
argument to an exact one by arguing that N_j^{−2δ_0} must be
rational, which forces δ_0 = 0 (for RATIONAL prime norm N_j).

**Edge case:** For **inert Gaussian primes** (p ≡ 3 mod 4),
N(𝔭) = p² (a square of a rational prime). Then N^{−2δ_0} =
p^{−4δ_0} ∈ ℚ forces 4δ_0 ∈ ℤ, i.e., δ_0 ∈ (1/4)ℤ. Combined
with |δ_0| < 1/2: δ_0 ∈ {−1/4, 0, 1/4}. The paper's Step 5
does not address this edge case.

**Fix:** Either restrict to split/ramified primes (norms 2, 5,
13, 17, 29, ... — rational primes), or handle the inert-prime
case separately.

**Cross-references:**
- Per-Point: C1
