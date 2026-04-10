# Strategy 01 — Hodge Path Synthesis

*Three paths explored. One killed. Two surviving. One target.*
*Date: 2026-04-10*

---

## Results

| Path | Verdict | Status |
|:--|:--|:--|
| Path 1 (CM abelian) | PARTIAL — A known, A^n open | SURVIVING |
| Path 2 (operator-Hodge) | KILLED — numerological | DEAD |
| Path 3 (motivic bridge) | PLAUSIBLE (5/10 for CM) | SURVIVING |

## The convergence

Both surviving paths point at the SAME target:
**Hodge for powers A^n of CM abelian varieties.**

- Path 1: direct computation of exotic Hodge classes on A×A
- Path 3: Tate→bridge→CM lift pipeline

## The key computation

> Compute Hdg*(A×A) for A with CM by Q(ζ_13) and check whether
> the bridge's inter-orbit data (β_3, Jones sub-factor, orbit
> projectors) captures all exotic Hodge classes.

## Key findings from each path

**Path 1 (research/01):**
- A has dim 6, CM type Φ = {1,2,3,4,6,8} mod 13
- Hodge group Hg(A) = maximal unitary torus, rank 5
- Orbit projectors ARE algebraic cycles (endomorphism correspondences)
- β_3 lives in group cohomology, NOT variety cohomology
- Hodge for simple A: KNOWN (Dodson 1984, Moonen-Zarhin 1999)
- Hodge for A^n: OPEN (exotic classes in products)

**Path 2 (research/02): KILLED**
- Grammar types extrinsic, Hodge types intrinsic
- No functor from operator dictionary to Hodge bigrading
- CP² test fails, CP²×S² test fails

**Path 3 (research/03):**
- Bridge steps 1-2 are algebraic/motivic
- Step 3 (Jones) is analytic — motivic content in steps 1-2 only
- Tate connection STRONG (Tate proved for CM abelian varieties)
- Pipeline: Tate (mod p) → bridge → CM lift (char 0)
- Limited to CM by abelian Langlands
- No structural obstruction found

## Feasibility

- Full Hodge: 3/10
- CM Hodge for A^n: 5/10
- This is HARDER than RH (7/10 achieved) and BSD (6/10 achieved)
