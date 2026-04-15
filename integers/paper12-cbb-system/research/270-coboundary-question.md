# research/270 -- The Coboundary Question

*Date: 2026-04-09. Status: CRITICAL GAP CONFIRMED.*

## 1. The question

The RH proof chain (Paper 13, Section 6) claims an off-line zero
at delta != 0 shifts the Brauer cocycle by
Delta_c(delta) = (1 - p^{-2*delta})/(p - p^{-2*delta}),
then invokes a constraint Delta_c in (1/k)Z, then uses
Gelfond-Schneider to force delta = 0.

A referee asks: is the perturbation Delta_c a coboundary? If so,
the cohomology class [c] is unchanged, the integrality constraint
is vacuous, and the proof collapses.

## 2. Coboundaries for Z/kZ with U(1) coefficients

For G = Z/kZ acting trivially on U(1), a 2-coboundary is:

    (delta_b)(tau^i, tau^j) = b(tau^j) * b(tau^i)^{-1} * b(tau^{i+j mod k})^{-1}

for a 1-cochain b: G -> U(1). In additive notation (writing U(1)
as R/Z), this is delta_b(i,j) = b(j) - b(i) - b(i+j mod k).

The carry cocycle c_0(i,j) = zeta_k^{floor((i+j)/k)} represents
the canonical generator 1/k in H^2(Z/kZ, U(1)) = Z/kZ.

## 3. What the proof actually computes

Theorem 5.1 defines Delta_c as 1 - f_p(delta), where
f_p(delta) = Z_p(1+2*delta)/Z_p(1) is the ratio of perturbed to
unperturbed p-local Euler factors. This is a SCALAR -- the same
real number for all (i,j). The "perturbed cocycle" would be:

    c_delta(i,j) = f_p(delta) * c_0(i,j)

i.e., the original carry cocycle multiplied by a uniform real
scalar.

## 4. Is the perturbation a coboundary?

### 4.1 The scalar multiplication problem

Multiplying a U(1)-valued cocycle by a positive real r does NOT
give a U(1)-valued cochain (unless r = 1). The values
r * zeta_k^{floor((i+j)/k)} have modulus r, not 1. So the
"perturbed cocycle" is not even a cocycle with values in U(1).

This is the first problem: the perturbation formula does not
produce a valid 2-cocycle in Z^2(G, U(1)).

### 4.2 Reinterpreting as an additive shift

If we reinterpret in additive notation, writing c_0(i,j) as
floor((i+j)/k) / k in R/Z, then "shifting by Delta_c" would give:

    c_delta(i,j) = floor((i+j)/k)/k + Delta_c(delta)  (mod Z)

This IS a valid R/Z-valued 2-cochain. Is c_delta - c_0 = Delta_c
(a constant function) a coboundary?

A constant 2-cocycle phi(i,j) = alpha for all (i,j) is a
coboundary iff there exists b: Z/kZ -> R/Z with
b(j) - b(i) - b(i+j mod k) = alpha for all i,j.

Setting i = j = 0: b(0) - b(0) - b(0) = alpha, so b(0) = -alpha.
Setting i = 0, j = m: b(m) - b(0) - b(m) = alpha, so
-b(0) = alpha, so b(0) = -alpha. Consistent.
Setting i = j = 1 (for k = 3): b(1) - b(1) - b(2) = alpha,
so b(2) = -alpha.
Setting i = 1, j = 2 (for k = 3): b(2) - b(1) - b(0) = alpha,
so -alpha - b(1) + alpha = alpha, so b(1) = -alpha.

Check all (i,j) for k = 3 with b(0) = b(1) = b(2) = -alpha:

- (0,0): b(0)-b(0)-b(0) = -(-alpha) = ... wait, let me redo.

Actually b(0) = -alpha means:
- (0,0): b(0)-b(0)-b(0) = -alpha. Need = alpha. FAILS (gives
  -alpha != alpha unless alpha = 0).

So a nonzero constant 2-cochain is NOT a coboundary for Z/3Z.

### 4.3 General proof: constant 2-cochains are not coboundaries

For G = Z/kZ with trivial action on R/Z, a 2-coboundary satisfies:

    sum_{i,j} (delta_b)(tau^i, tau^j) = 0

Proof: sum over all i,j of [b(j) - b(i) - b(i+j mod k)].
The first sum: sum_i sum_j b(j) = k * sum_j b(j).
The second sum: sum_i sum_j b(i) = k * sum_i b(i).
The third sum: sum_i sum_j b(i+j mod k). For fixed i, as j runs
over Z/kZ, i+j mod k runs over Z/kZ. So this is
sum_i sum_m b(m) = k * sum_m b(m).

Total: k*S - k*S - k*S = -k*S where S = sum b(m).

Meanwhile, the sum of a constant alpha over k^2 pairs is k^2 * alpha.

For delta_b = alpha (constant), we need -k*S = k^2 * alpha, so
S = -k*alpha. But we also need b(0) = -alpha from the (0,0)
equation. This does not lead to a contradiction by itself -- let me
just verify computationally.

### 4.4 Explicit computation for k = 3

Coboundary condition: delta_b(i,j) = b(j) - b(i) - b(i+j mod 3)
must equal alpha for all i,j in {0,1,2}.

Nine equations (writing a = b(0), c1 = b(1), c2 = b(2)):

    (0,0): a - a - a = -a = alpha        => a = -alpha
    (0,1): c1 - a - c1 = -a = alpha      => a = -alpha (consistent)
    (0,2): c2 - a - c2 = -a = alpha      => a = -alpha (consistent)
    (1,0): a - c1 - c1 = -alpha - 2*c1 = alpha  => c1 = -alpha
    (1,1): c1 - c1 - c2 = -c2 = alpha    => c2 = -alpha
    (1,2): c2 - c1 - a = -alpha + alpha + alpha = alpha  => YES
    (2,0): a - c2 - c2 = -alpha + alpha + alpha = alpha  => YES
    (2,1): c1 - c2 - a = -alpha + alpha + alpha = alpha  => YES
    (2,2): c2 - c2 - c1 = -c1 = alpha    => c1 = -alpha (consistent)

ALL NINE EQUATIONS SATISFIED with b(0) = b(1) = b(2) = -alpha.

**RESULT: A constant 2-cochain IS a coboundary for Z/3Z.**

The 1-cochain b(m) = -alpha for all m satisfies delta_b = alpha.

### 4.5 Verification for general k

For G = Z/kZ, the constant 1-cochain b(m) = -alpha gives:

    delta_b(i,j) = b(j) - b(i) - b(i+j) = -alpha - (-alpha) - (-alpha) = alpha.

This works for ALL k. A constant 2-cochain is ALWAYS a coboundary.

## 5. Consequences for the proof chain

### 5.1 If the perturbation is additive and constant

If the off-line zero shifts the cocycle by a constant
Delta_c(delta) added uniformly to all pairs (i,j), then this
shift is a coboundary (Section 4.5). The cohomology class is
unchanged: [c_delta] = [c_0] = 1/k for ALL delta.

The integrality constraint Delta_c in (1/k)Z is vacuous because
the class never moves. The Gelfond-Schneider argument has no input.

### 5.2 The discreteness-of-H^2 argument

This is consistent with the topological argument: H^2(Z/kZ, U(1))
= Z/kZ is discrete. If [c_delta] depends continuously on delta,
it must be constant. The coboundary computation shows exactly HOW
it stays constant: the continuous perturbation is absorbed into a
coboundary at each delta.

### 5.3 The proof chain FAILS at this step

The logical chain in Paper 13 is:

    off-line zero => cocycle shift Delta_c(delta) => must be in (1/k)Z
    => Gelfond-Schneider => delta = 0

The coboundary analysis shows the middle step is wrong. The shift
Delta_c(delta) is a shift in the COCYCLE REPRESENTATIVE, not in
the COHOMOLOGY CLASS. Since a constant additive shift is always
a coboundary, the cohomology class [c] = 1/k is preserved for all
delta. The integrality constraint is automatically satisfied (with
n = 0, i.e., no class change), and imposes no condition on delta.

## 6. Can the argument be saved?

### 6.1 Attempt: Pin the representative, not just the class

If the Bost-Connes structure at beta = 1 fixes a SPECIFIC cocycle
representative (the carry cocycle, not just its class), then any
perturbation -- even a coboundary -- would violate this pinning.

Problem: the Jones subfactor's Pimsner-Popa basis provides
unitaries u_0, u_1, u_2 satisfying u_i u_j = c(i,j) u_{i+j}.
Changing c by a coboundary corresponds to redefining
u_j -> b(j) * u_j, which gives a different but equivalent Pimsner-
Popa basis. The subfactor itself is unchanged. So the subfactor
does NOT pin the representative.

The KMS state omega_1 evaluates on whichever basis we choose.
Choosing a different basis (absorbing the coboundary) gives the
same expectation values up to the gauge transformation b. So the
KMS state does not pin the representative either.

### 6.2 Attempt: The perturbation is not purely additive

The derivation in Theorem 5.1 computes Delta_c as a scalar
multiplicative factor (f_p) on the cocycle values. In
multiplicative U(1) language, this means:

    c_delta(i,j) = f_p(delta) * c_0(i,j)

where f_p is a POSITIVE REAL, not a U(1) element. This takes the
cocycle OUT of U(1). The perturbation is not a U(1)-valued 2-cochain
at all, so asking whether it is a coboundary in H^2(G, U(1)) is
not well-posed.

This suggests the formula Delta_c = 1 - f_p is not computing a
perturbation within the cohomology theory of U(1)-valued cochains.
It is computing something else: perhaps the change in a real-valued
invariant extracted from the KMS evaluation.

### 6.3 Attempt: Work in H^2(G, R*_+) instead

If we allow cocycles valued in R*_+ (the multiplicative positive
reals), then f_p(delta) * c_0 makes sense as a cochain valued in
C* = R*_+ x U(1). But H^2(Z/kZ, R*_+) = 0 because R*_+ is
uniquely divisible (via logarithm, it is isomorphic to R, and
H^2(Z/kZ, R) = 0 for finite groups). So the R*_+ part of any
C*-valued cocycle is automatically a coboundary.

This means: decomposing c_delta into its U(1) part (the phase)
and its R*_+ part (the norm), the phase is unchanged (still
the carry cocycle) and the norm perturbation f_p(delta) is a
coboundary in H^2(G, R*_+) = 0. The cohomology class in
H^2(G, U(1)) is unchanged.

### 6.4 Attempt: Non-abelian cohomology or twisted coefficients

If the Z/kZ action on U(1) were non-trivial (twisted coefficients),
the coboundary computation in Section 4 would change. But the
bridge construction uses TRIVIAL action (the Galois group acts
trivially on the roots of unity that appear as cocycle values).
So this does not help.

### 6.5 Attempt: Rigidity of the Bost-Connes partition function

The constraint might not be on the cohomology class but on the
partition function Z_p(beta). The requirement that omega_1 is
KMS_1 fixes Z_p(1) = 1/(1-p^{-1}). An off-line zero would
require Z_p(1+2*delta) != Z_p(1), but this is just the statement
that the Euler product converges to different values at different
points -- which is trivially true and imposes no constraint on
the location of zeros.

## 7. Diagnosis

### 7.1 What Theorem 5.1 actually computes

Theorem 5.1 computes the ratio of p-local Euler factors at
beta = 1 + 2*delta vs. beta = 1. This is a well-defined real
number. The claim that this ratio equals "the cocycle shift" is
the unjustified step. The ratio f_p(delta) measures the change
in a KMS expectation value, not a change in a topological
invariant.

### 7.2 The fundamental confusion

The proof conflates:
- The COCYCLE c(i,j) = omega_1(u_i u_j u_{i+j}^{-1}), which
  depends continuously on the state omega_1 and hence on delta.
- The COHOMOLOGY CLASS [c] in H^2(G, U(1)) = Z/kZ, which is a
  discrete topological invariant.

A continuous family of cocycles c_delta parametrised by delta
gives a continuous path in the cocycle space Z^2(G, U(1)). The
projection to H^2(G, U(1)) = Z/kZ is locally constant (because
the target is discrete and the source is connected). Therefore
[c_delta] = [c_0] for all delta in a connected neighbourhood
of 0. The proof needs [c_delta] != [c_0] for delta != 0, but
topology guarantees the opposite.

### 7.3 Why the Gelfond-Schneider argument is irrelevant

The Gelfond-Schneider argument proves that Delta_c(delta) cannot
be a nonzero element of (1/k)Z for delta != 0. This is correct
and interesting mathematics. But it is answering the wrong
question. The cohomology class does not shift at all -- the
constraint Delta_c in (1/k)Z is satisfied trivially with
Delta_c = 0 at the level of cohomology, for any delta.

## 8. Verdict

**The perturbation is a coboundary.** More precisely: however one
interprets the "cocycle shift" (additive, multiplicative, or
mixed), the perturbation cannot change the cohomology class,
because H^2(Z/kZ, U(1)) is discrete and the perturbation is
continuous in delta. The specific coboundary that absorbs the
perturbation is b(m) = -Delta_c(delta) (constant 1-cochain) in
the additive interpretation.

**The proof chain fails at Step 1 of Section 6** (equation 6.2):
the constraint Delta_c(delta) in (1/k)Z. This constraint is
vacuous because the cohomology class is topologically frozen at
1/k for all delta. The Gelfond-Schneider argument, while
mathematically correct, has no force.

**No obvious fix exists** within the current framework. The
bridge cocycles are topological invariants, and topological
invariants cannot detect continuous perturbations. This is not
a gap that can be patched -- it is a structural feature of
cohomology with discrete target.

### 8.1 Possible salvage directions (speculative)

1. **Non-topological constraint.** Find a constraint on the
   cocycle REPRESENTATIVE (not class) that is dictated by the
   BC algebra. This would require proving that the KMS_1 state
   selects a unique representative, and that moving delta away
   from 0 changes this representative in a way that violates a
   BC algebraic identity (not just cohomology).

2. **Different invariant.** Replace the H^2 class with a
   NON-DISCRETE invariant that still has integrality properties.
   For example, the Connes-Chern character in cyclic cohomology
   takes values in R but has integrality properties from index
   theory. If the cocycle shift could be reinterpreted as a
   shift in a Chern number, the argument might work.

3. **Analytic (non-cohomological) constraint.** Abandon the
   cohomological framework entirely. Use the Euler factor ratio
   f_p(delta) directly as an analytic quantity, and find an
   analytic (not topological) reason why f_p(delta) = 1 is
   forced. This would be a fundamentally different argument.

4. **Spectral flow.** The perturbation delta -> c_delta may
   define a spectral flow in the sense of Atiyah-Patodi-Singer.
   Spectral flow is an integer-valued invariant of continuous
   paths of operators. If the bridge cocycle can be reinterpreted
   as a spectral flow, the integrality constraint might be
   non-trivial. But this requires a specific operator-theoretic
   construction not present in the current proof.

---

*This is the most critical gap in the RH proof chain. The
coboundary question is not a technicality -- it strikes at the
mechanism by which continuous (analytic) information about zero
locations is converted into discrete (topological) constraints.
The conversion fails because cohomology with discrete coefficients
is topologically rigid against continuous perturbations.*
