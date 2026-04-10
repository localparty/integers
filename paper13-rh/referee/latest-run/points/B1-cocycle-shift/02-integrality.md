# B1.02: The Integrality Constraint

**The claim:** For the shifted cocycle class to remain in H^2(Z/kZ, U(1)) = Z/kZ, the shift must land in (1/k)Z: Delta_c(delta) in (1/k)Z.

**Why must the shift be in (1/k)Z?**

The paper's argument: The bridge cocycle is an element of the discrete group Z/kZ. Any continuous perturbation of a discrete invariant must either leave it unchanged or jump by a full lattice unit. Therefore the shift Delta_c(delta) must be a multiple of 1/k.

**Assessment:** This argument has a fundamental conceptual issue. The cocycle c(i,j) takes values in U(1), which is a CONTINUOUS group. The cohomology class [c] is an element of H^2(Z/kZ, U(1)) = Z/kZ, which is discrete. But the paper computes the perturbation of the cocycle VALUES (which live in the continuous group U(1)), not of the cohomology CLASS (which lives in the discrete group Z/kZ).

The Euler factor ratio f_p(delta) multiplies the cocycle values. This gives a new 2-cochain c'(i,j) = f_p(delta) * c(i,j). But f_p(delta) is a SCALAR (same for all i,j), so multiplying a cocycle by a scalar gives a 2-cochain that may or may not be a cocycle. Even if it is a cocycle, its cohomology class depends on whether the scalar multiplication preserves the group structure.

For U(1)-valued cocycles, multiplication by a positive real r sends [c] = a/k mod Z to [c'] = r*a/k mod Z... but this is NOT how cohomology works. H^2(Z/kZ, U(1)) classifies central extensions; multiplying cocycle values by a real scalar does not correspond to a well-defined operation on cohomology classes unless r is itself a k-th root of unity.

**The deeper issue:** The paper's equation Delta_c = 1 - f_p is not a shift in the cohomology class. It is the fractional change in a KMS evaluation. The constraint that this must lie in (1/k)Z would need to be derived from the topology of the extension classified by the cocycle, not from a formula involving Euler factor ratios.

**Verdict: GAP.** The integrality constraint Delta_c(delta) in (1/k)Z is not rigorously justified. The paper assumes that a continuous perturbation of the KMS evaluation corresponds to a discrete jump in the cohomology class, but does not prove this correspondence.
