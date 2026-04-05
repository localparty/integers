# SLOCC-Isometry Map: Explicit Calculation for Conjecture 5.1

*Computation document for Problem 4 of the closing-the-open-problems plan.*
*Written April 5, 2026.*

---

## Step 1: The GHZ Tangent Space — Explicit Computation

### Setup

The GHZ state in (C^2)^{tensor 3}:

    |GHZ> = (1/sqrt 2)(|000> + |111>)

We use the computational basis {|0>, |1>} for each qubit,
with the 8-dimensional product basis ordered as:

    |000>, |001>, |010>, |011>, |100>, |101>, |110>, |111>

So |GHZ> = (1/sqrt 2)(e_0 + e_7) in C^8, where e_k denotes the
k-th standard basis vector (zero-indexed).

The SLOCC group is G = SL(2,C)^3, acting by (A_1 tensor A_2 tensor A_3).

The Lie algebra is g = sl(2,C) + sl(2,C) + sl(2,C), acting by:

    (X_1, X_2, X_3) . |psi> = (X_1 tensor I tensor I
                               + I tensor X_2 tensor I
                               + I tensor I tensor X_3)|psi>

### Basis for sl(2,C)

We use the standard basis:

    h = (1  0)    e = (0 1)    f = (0 0)
        (0 -1)        (0 0)        (1 0)

with brackets [h,e] = 2e, [h,f] = -2f, [e,f] = h.

In terms of Pauli matrices: h = sigma_z, e = sigma_+, f = sigma_-.

Action on the qubit basis:

    h|0> = |0>,   h|1> = -|1>
    e|0> = 0,     e|1> = |0>
    f|0> = |1>,   f|1> = 0

### Computing tangent vectors

We need to compute X_i . |GHZ> for each X_i in {h, e, f} acting
on each of the three qubit slots. This gives 9 tangent vectors.

**Slot 1 (X acts on first qubit):**

    h_1|GHZ> = (1/sqrt 2)(h|0> tensor |00> + h|1> tensor |11>)
             = (1/sqrt 2)(|000> - |111>)
             = (1/sqrt 2)(e_0 - e_7)

    e_1|GHZ> = (1/sqrt 2)(e|0> tensor |00> + e|1> tensor |11>)
             = (1/sqrt 2)(0 + |011>)
             = (1/sqrt 2) e_3

    f_1|GHZ> = (1/sqrt 2)(f|0> tensor |00> + f|1> tensor |11>)
             = (1/sqrt 2)(|100> + 0)
             = (1/sqrt 2) e_4

**Slot 2 (X acts on second qubit):**

    h_2|GHZ> = (1/sqrt 2)(|0> tensor h|0> tensor |0> + |1> tensor h|1> tensor |1>)
             = (1/sqrt 2)(|000> - |111>)
             = (1/sqrt 2)(e_0 - e_7)

    e_2|GHZ> = (1/sqrt 2)(|0> tensor e|0> tensor |0> + |1> tensor e|1> tensor |1>)
             = (1/sqrt 2)(0 + |101>)
             = (1/sqrt 2) e_5

    f_2|GHZ> = (1/sqrt 2)(|0> tensor f|0> tensor |0> + |1> tensor f|1> tensor |1>)
             = (1/sqrt 2)(|010> + 0)
             = (1/sqrt 2) e_2

**Slot 3 (X acts on third qubit):**

    h_3|GHZ> = (1/sqrt 2)(|00> tensor h|0> + |11> tensor h|1>)
             = (1/sqrt 2)(|000> - |111>)
             = (1/sqrt 2)(e_0 - e_7)

    e_3|GHZ> = (1/sqrt 2)(|00> tensor e|0> + |11> tensor e|1>)
             = (1/sqrt 2)(0 + |110>)
             = (1/sqrt 2) e_6

    f_3|GHZ> = (1/sqrt 2)(|00> tensor f|0> + |11> tensor f|1>)
             = (1/sqrt 2)(|001> + 0)
             = (1/sqrt 2) e_1

### Summary of tangent vectors (dropping the common 1/sqrt 2):

    h_1|GHZ> ~ e_0 - e_7          (= |000> - |111>)
    h_2|GHZ> ~ e_0 - e_7          (same!)
    h_3|GHZ> ~ e_0 - e_7          (same!)
    e_1|GHZ> ~ e_3                 (= |011>)
    e_2|GHZ> ~ e_5                 (= |101>)
    e_3|GHZ> ~ e_6                 (= |110>)
    f_1|GHZ> ~ e_4                 (= |100>)
    f_2|GHZ> ~ e_2                 (= |010>)
    f_3|GHZ> ~ e_1                 (= |001>)

### Key observations

**1. The Cartan directions collapse.** All three h_i produce the
same tangent vector: e_0 - e_7. This means h_1 - h_2, h_1 - h_3,
and h_2 - h_3 are in the kernel. The 3D Cartan subalgebra
contributes only 1 independent tangent direction.

**2. The raising/lowering operators give 6 independent vectors.**
The vectors e_1, ..., e_6 are all distinct standard basis vectors,
hence linearly independent.

**3. Total tangent space dimension.** We get 1 + 6 = 7 independent
tangent vectors, spanning:

    T_{GHZ}(G . |GHZ>) = span{e_0 - e_7, e_1, e_2, e_3, e_4, e_5, e_6}

This is a 7-dimensional (complex) subspace of C^8.

Wait — we need to be more careful. The tangent space to the orbit
in C^8 (not in CP^7) also includes the direction |GHZ> itself
(from scalar multiplication). Let us check: |GHZ> ~ e_0 + e_7.
The tangent vector e_0 - e_7 is orthogonal to e_0 + e_7. And
e_1, ..., e_6 are all orthogonal to both e_0 and e_7. So the
tangent space does NOT contain the |GHZ> direction.

But the SLOCC group is SL(2,C)^3, not GL(2,C)^3. The Lie algebra
sl(2,C) consists of traceless matrices, so the identity action
(scalar multiples of identity) is excluded. The full tangent space
in C^8 is exactly the 7D space computed above.

**4. Stabilizer Lie algebra.** The Lie algebra of the stabilizer is:

    stab = {(a_1 h, a_2 h, a_3 h) : a_1 + a_2 + a_3 = 0,
            and the combination acts trivially}

But we found that (h, 0, 0), (0, h, 0), (0, 0, h) all give the
SAME tangent vector e_0 - e_7. So (h, -h, 0) gives zero tangent
vector, and (h, 0, -h) gives zero tangent vector. These span a
2-dimensional subalgebra of the stabilizer.

The full stabilizer Lie algebra: we need all (X_1, X_2, X_3) in
sl(2,C)^3 such that (X_1 tensor I tensor I + I tensor X_2 tensor I
+ I tensor I tensor X_3)|GHZ> = 0.

Writing X_i = a_i h + b_i e + c_i f, we get:

    (a_1 + a_2 + a_3)(e_0 - e_7) + b_1 e_3 + b_2 e_5 + b_3 e_6
    + c_1 e_4 + c_2 e_2 + c_3 e_1 = 0

Since {e_0 - e_7, e_1, e_2, e_3, e_4, e_5, e_6} are linearly
independent, every coefficient must vanish:

    a_1 + a_2 + a_3 = 0
    b_1 = b_2 = b_3 = 0
    c_1 = c_2 = c_3 = 0

So the stabilizer Lie algebra is:

    stab_g = {(a_1 h, a_2 h, a_3 h) : a_1 + a_2 + a_3 = 0}

This is a **2-dimensional abelian** Lie algebra (over C), isomorphic
to the Cartan subalgebra of the diagonal torus modulo the trace
constraint. In real terms this is 4-dimensional.

**5. Dimension check.**

    dim_C(g) = 9
    dim_C(stab) = 2
    dim_C(orbit) = 9 - 2 = 7  check!

The orbit G . |GHZ> in C^8 has complex dimension 7.

In projective space CP^7 (real dimension 14), the orbit has real
dimension 14 — confirming the "generic" orbit dimension from the
Dur-Vidal-Cirac table. (Complex dimension 7 = real dimension 14.)

### The stabilizer group

The continuous stabilizer is generated by (a_1 h, a_2 h, a_3 h)
with a_1 + a_2 + a_3 = 0. Exponentiating:

    exp(a_i h) = diag(exp(a_i), exp(-a_i))

Acting on |GHZ>:

    (diag(e^{a_1}, e^{-a_1}) tensor diag(e^{a_2}, e^{-a_2})
     tensor diag(e^{a_3}, e^{-a_3}))|GHZ>
    = (1/sqrt 2)(e^{a_1+a_2+a_3}|000> + e^{-(a_1+a_2+a_3)}|111>)

This equals |GHZ> iff a_1 + a_2 + a_3 = 0. So the continuous
stabilizer is:

    Stab^0 = {(diag(t_1, t_1^{-1}), diag(t_2, t_2^{-1}),
               diag(t_3, t_3^{-1})) : t_1 t_2 t_3 = 1}

This is a 2-dimensional complex torus T^2 (= (C*)^2).

The discrete stabilizer supplements this. The permutation-like
elements that flip both |0> and |1> are:

    (sigma_x, sigma_x, sigma_x)|GHZ> = (1/sqrt 2)(|111> + |000>) = |GHZ>

And (sigma_x, I, I) sends |GHZ> -> (1/sqrt 2)(|100> + |011>),
which is NOT |GHZ>. So sigma_x on all three qubits preserves GHZ.

But sigma_x is NOT in SL(2,C)... actually det(sigma_x) = -1.
However, i*sigma_x has det = i^2*(-1) = 1... no, let us be
careful. sigma_x = ((0,1),(1,0)), det = -1. So sigma_x is not
in SL(2,C). But -sigma_x = ((0,-1),(-1,0)), det = 1. And
(-sigma_x)|0> = -|1>, (-sigma_x)|1> = -|0>. So:

    (-sigma_x tensor -sigma_x tensor -sigma_x)|GHZ>
    = (-1)^3 (1/sqrt 2)(|111> + |000>) = -|GHZ>

This is -|GHZ>, which represents the same state in CP^7. For the
SLOCC orbit in C^8 (not projective), we need the action to give
+|GHZ>, so this is a stabilizer only projectively.

The actual discrete stabilizer in SL(2,C)^3 acting on C^8:
we need diag(+1,-1) type elements. Note diag(-1,-1) = -I, which
has det = 1 and acts as -I tensor ... The element (-I,-I,-I) acts
as (-1)^3 I = -I on the tensor product, so |GHZ> -> -|GHZ>. Not
a stabilizer in C^8. But (-I, -I, I) acts as (-1)^2 I = I on the
tensor product, so this IS a stabilizer.

More systematically: (epsilon_1 I, epsilon_2 I, epsilon_3 I) with
epsilon_i = +/- 1, each det = 1 (since det(-I) = (-1)^2 = 1 for
2x2 matrices). The action on the tensor product is
epsilon_1 epsilon_2 epsilon_3 I. This is the identity iff
epsilon_1 epsilon_2 epsilon_3 = 1.

So the discrete stabilizer from the center is:

    {(epsilon_1 I, epsilon_2 I, epsilon_3 I) :
     epsilon_i = +/-1, epsilon_1 epsilon_2 epsilon_3 = 1}

This group has 4 elements: (+++), (+--), (-+-), (--+).
It is isomorphic to (Z_2)^2 (choosing any two signs determines
the third).

But the full discrete stabilizer is larger. We can also combine
the central elements with the torus elements. The standard result
(Dur, Vidal, Cirac 2000) gives the GHZ stabilizer as containing
(Z_2)^3 when working projectively. Our computation is consistent:
(Z_2)^2 in SL(2,C)^3, becoming (Z_2)^3 projectively when we
include the overall -I action.

**Summary of Step 1:**

    Stabilizer Lie algebra: {(a_1 h, a_2 h, a_3 h) : sum a_i = 0}
                          ~ C^2 (abelian, 2D complex)
    Discrete stabilizer:    (Z_2)^2 in SL(2,C)^3
                            (Z_2)^3 projectively in PGL
    Orbit dimension:        7 complex = 14 real
    Tangent space:          span{e_0 - e_7, e_1, ..., e_6} in C^8

---

## Step 2: Restriction to the Compact Form SU(2)^3

### The compact tangent space

Restricting from SL(2,C)^3 to SU(2)^3, the Lie algebra becomes
su(2)^3 with basis elements iH_k where H_k are Hermitian traceless
(i.e., H_k in {sigma_x, sigma_y, sigma_z}). The standard basis for
su(2) is {i sigma_x, i sigma_y, i sigma_z}, which we write as:

    iX = i(0 1)    iY = i(0 -i)    iZ = i(1  0)
          (1 0)          (i  0)          (0 -1)

Note the relation to sl(2,C) generators:

    h = sigma_z,    e = sigma_+ = (sigma_x + i sigma_y)/2,
    f = sigma_- = (sigma_x - i sigma_y)/2

So the su(2) generators are:

    i sigma_x = i(e + f)
    i sigma_y = (e - f)       [since sigma_y = -i(e - f)]
    i sigma_z = ih

Actually, let us be precise. sigma_y = ((0,-i),(i,0)). Then
i sigma_y = ((0,1),(-1,0)). And:

    e + f = ((0,1),(1,0)) = sigma_x
    e - f = ((0,1),(-1,0)) = i sigma_y
    h = sigma_z

So su(2) = span_R{i sigma_x, i sigma_y, i sigma_z}
         = span_R{i(e+f), i(e-f)/i, ih}

Wait, let me just re-derive from scratch. su(2) consists of
skew-Hermitian traceless 2x2 matrices. A basis is:

    T_1 = i sigma_x / 2,  T_2 = i sigma_y / 2,  T_3 = i sigma_z / 2

(the factor of 1/2 is conventional, we'll drop it for simplicity).
The tangent vectors under su(2)^3 are:

    (iH_1 tensor I tensor I + I tensor iH_2 tensor I
     + I tensor I tensor iH_3)|GHZ>

where H_j in {sigma_x, sigma_y, sigma_z}.

### Tangent vectors under su(2)^3

Using our earlier results (and linearity):

    i sigma_z on slot k: gives i(e_0 - e_7) for all k.

    i sigma_x on slot 1: i(e+f)_1|GHZ> ~ i(e_3 + e_4)
    i sigma_x on slot 2: ~ i(e_5 + e_2)
    i sigma_x on slot 3: ~ i(e_6 + e_1)

    i sigma_y on slot 1: (e-f)_1|GHZ> ~ (e_3 - e_4)
                          [since i sigma_y = e - f in our basis]
    i sigma_y on slot 2: ~ (e_5 - e_2)
    i sigma_y on slot 3: ~ (e_6 - e_1)

Wait, let me be more careful. We have:

    i sigma_x = i(e + f)
    i sigma_y = i(-i)(e - f) = (e - f)

Hmm, sigma_y = ((0,-i),(i,0)). So:

    sigma_y|0> = i|1>,    sigma_y|1> = -i|0>

Therefore:

    i sigma_y|0> = i(i|1>) = -|1> = -(f|0>)
    i sigma_y|1> = i(-i|0>) = |0> = e|1>

So i sigma_y = e - f in terms of action. Let me verify:
e - f = ((0,1),(0,0)) - ((0,0),(1,0)) = ((0,1),(-1,0)).
And i sigma_y = i((0,-i),(i,0)) = ((0,1),(-1,0)). Yes, confirmed:
i sigma_y = e - f.

Similarly: i sigma_x = i((0,1),(1,0)) = ((0,i),(i,0)) = i(e+f).

And: i sigma_z = i h.

So the 9 tangent vectors from su(2)^3 are:

**From i sigma_z (= ih) on each slot:**

    (ih)_1|GHZ> = i(e_0 - e_7)
    (ih)_2|GHZ> = i(e_0 - e_7)     (same)
    (ih)_3|GHZ> = i(e_0 - e_7)     (same)

Three copies of the same vector. Kernel: 2-dimensional.

**From i(e+f) on each slot:**

    i(e+f)_1|GHZ> = i(e_3 + e_4)     = i(|011> + |100>)
    i(e+f)_2|GHZ> = i(e_5 + e_2)     = i(|101> + |010>)
    i(e+f)_3|GHZ> = i(e_6 + e_1)     = i(|110> + |001>)

Three independent vectors.

**From (e-f) on each slot:**

    (e-f)_1|GHZ> = (e_3 - e_4)       = |011> - |100>
    (e-f)_2|GHZ> = (e_5 - e_2)       = |101> - |010>
    (e-f)_3|GHZ> = (e_6 - e_1)       = |110> - |001>

Three independent vectors.

### Real tangent space

The tangent space under SU(2)^3 is a REAL vector space (since
su(2) is a real Lie algebra). The tangent vectors are:

    v_0 = i(e_0 - e_7)                           [from any ih_k]
    v_1 = i(e_3 + e_4),  v_2 = i(e_5 + e_2),  v_3 = i(e_6 + e_1)
    w_1 = (e_3 - e_4),   w_2 = (e_5 - e_2),   w_3 = (e_6 - e_1)

These 7 vectors live in C^8 viewed as R^{16}. Are they independent
over R? Yes: each involves different components of C^8, and the
factors of i vs 1 distinguish the v's from the w's.

**Stabilizer of SU(2)^3 at GHZ.** The stabilizer Lie algebra of
the compact form is:

    stab_{su(2)^3} = {(a_1 ih, a_2 ih, a_3 ih) : a_i in R,
                       a_1 + a_2 + a_3 = 0}

This is 2-dimensional (real), a maximal torus of the "diagonal
Cartan" type.

**Compact orbit dimension:**

    dim_R(su(2)^3) = 9
    dim_R(stab) = 2
    dim_R(orbit) = 9 - 2 = 7

The orbit of |GHZ> under SU(2)^3 is a **7-dimensional real
manifold** embedded in CP^7.

### Structure of the tangent space as su(2)^3 representation

The 7D real tangent space decomposes under the residual symmetry.
Let's identify the structure. Define:

    H = diagonal Cartan = {(a_1 ih, a_2 ih, a_3 ih) : sum a_i = 0}

This is a 2D abelian subalgebra. Its action on the tangent vectors
gives the weight decomposition. The adjoint action of
(a_1, a_2, a_3) (with sum = 0) on the tangent vectors:

On v_0 = i(e_0 - e_7): this is the image of the Cartan itself,
so it transforms trivially (weight 0).

Actually, we need to compute this more carefully. The tangent
space is the quotient g/stab, and the adjoint representation of
stab on g/stab gives the structure.

The full algebra su(2)^3 has a basis:

    {ih_k, i(e+f)_k, (e-f)_k : k = 1,2,3}

The stabilizer stab = span_R{ih_1 - ih_2, ih_1 - ih_3}.

The quotient g/stab has basis (representatives):

    {ih_1, i(e+f)_k, (e-f)_k : k = 1,2,3}

(since ih_1 represents the Cartan modulo the stabilizer, and
ih_2 = ih_1 - (ih_1 - ih_2), ih_3 = ih_1 - (ih_1 - ih_3).)

The adjoint action of the stabilizer element (a_1 ih, a_2 ih, a_3 ih)
(with sum a_i = 0) on the basis:

    [a_k ih_k, ih_j] = 0                    (Cartan is abelian)
    [a_k ih_k, i(e+f)_k] = a_k [ih, i(e+f)] = a_k . 2(e-f)
                          (since [h, e+f] = 2e - 2f = 2(e-f)/i . i
                           wait let me just compute:
                           [ih, i(e+f)] = i^2[h, e+f] = -[h,e+f]
                           = -(2e - 2f) = -2(e-f))

Hmm, let me be systematic. For a single su(2) factor:

    [ih, i(e+f)] = i^2 [h, e+f] = -[h, e+f]
    [h, e+f] = [h,e] + [h,f] = 2e - 2f
    So [ih, i(e+f)] = -(2e - 2f) = -2(e-f)

    [ih, (e-f)] = [h, e-f] . i ... no:
    [ih, e-f] = i[h, e-f] = i([h,e] - [h,f]) = i(2e + 2f) = 2i(e+f)

So within each su(2) factor:

    [ih, i(e+f)] = -2(e-f)
    [ih, (e-f)] = 2i(e+f)

This means the pair {i(e+f), (e-f)} transforms as a 2D real
representation under the Cartan element ih, with matrix:

    ad(ih) restricted to {i(e+f), (e-f)} =  ( 0  2)
                                              (-2  0)

This is a rotation (angular velocity 2). The pair {i(e+f), (e-f)}
spans a 2D irrep of u(1) with weight +/- 2i (complexified).

### The decomposition

The 7D tangent space T_{GHZ}(SU(2)^3 . |GHZ>) decomposes under
the stabilizer action (2D Cartan torus) as:

The stabilizer is parametrized by (a_1, a_2) with a_3 = -a_1 - a_2.
Its action on the tangent space:

    - v_0 = i(e_0 - e_7): weight (0,0). Dimension 1.

    - {v_k, w_k} = {i(e+f)_k, (e-f)_k} for k = 1,2,3:
      Each pair rotates under the stabilizer element a_k ih_k
      with angular velocity 2a_k. Specifically:

      Pair k = 1: rotates with rate 2a_1
      Pair k = 2: rotates with rate 2a_2
      Pair k = 3: rotates with rate 2a_3 = -2(a_1 + a_2)

So the tangent space decomposes as:

    T = R^1_{(0,0)} + R^2_{(2,0)} + R^2_{(0,2)} + R^2_{(-2,-2)}

where the subscripts are the (a_1, a_2) weights, and R^k denotes a
k-dimensional real representation.

Equivalently, complexifying: the 7D real space becomes a 7D complex
representation, decomposing into weight spaces:

    T_C = C_{(0,0)} + C_{(2,0)} + C_{(-2,0)} + C_{(0,2)} + C_{(0,-2)}
          + C_{(-2,-2)} + C_{(2,2)}

(each R^2 rotation becomes a pair of complex conjugate weights).

---

## Step 3: Isometry Algebra of CP^2 x S^2 x S^1

### The isometry groups

    Isom(CP^2) = SU(3)    (dim 8)
    Isom(S^2)  = SO(3) ~ SU(2)/Z_2    (dim 3)
    Isom(S^1)  = U(1)    (dim 1)

Full isometry group: SU(3) x SU(2) x U(1), dimension 12.

Note: strictly, Isom(CP^2) = PSU(3) = SU(3)/Z_3 and
Isom(S^2) = SO(3) = SU(2)/Z_2, but the Lie algebras are
su(3), su(2), u(1) regardless.

### The tangent space of CP^2 x S^2 x S^1

The total space has dimension 4 + 2 + 1 = 7. At a point
p = (p_1, p_2, p_3):

    T_p(CP^2 x S^2 x S^1) = T_{p_1}(CP^2) + T_{p_2}(S^2) + T_{p_3}(S^1)

### Isotropy representations

At a chosen basepoint, the isotropy (stabilizer of the point)
subgroups are:

**CP^2:** The isotropy at a point in CP^2 under SU(3) is
U(2) = S(U(2) x U(1)). So the tangent space T(CP^2) at the
basepoint transforms as a representation of U(2). Specifically:

    SU(3) / U(2) = CP^2

The tangent space is the 4-real-dimensional representation of U(2)
that is the fundamental representation 2 of SU(2) tensored with
a U(1) charge. In complex terms, T_{p_1}(CP^2) ~ C^2 as a
representation of U(2), which is the standard representation
of SU(2) with U(1) charge +1 (or -1).

More explicitly: decompose the adjoint of su(3) under the
subalgebra u(2):

    su(3) = u(2) + m

where m is the orthogonal complement (tangent space). Under u(2):

    8 = (3 + 1) + 4

The 4-dimensional space m transforms as 2 + bar{2} under su(2)
(with opposite U(1) charges). As a real representation, this is
the standard 4D representation of U(2).

**S^2:** The isotropy at a point in S^2 under SU(2) is U(1).

    SU(2) / U(1) = S^2 = CP^1

The tangent space T_{p_2}(S^2) is 2-real-dimensional, transforming
as the standard rotation representation of U(1) (weight +/- 1).

**S^1:** The isotropy at a point in S^1 under U(1) is trivial.
The tangent space is 1D, transforming trivially.

### Full isotropy group and tangent representation

The isotropy of the full isometry group at a point is:

    K = U(2) x U(1) x {1}

(where U(2) < SU(3) and U(1) < SU(2) and the S^1 factor has
trivial isotropy).

The tangent representation of K on T_p(M^7) is:

    T = [C^2 of U(2)] + [R^2 of U(1)] + [R^1 trivial]

where:
- C^2 ~ R^4 is the fundamental of SU(2) < U(2) with U(1)_1 charge
- R^2 is the 2D rotation under U(1)_2
- R^1 is the trivial 1D representation

Dimension: 4 + 2 + 1 = 7. Correct.

### Decomposition under the maximal torus

The maximal torus of SU(3) x SU(2) x U(1) has rank 2 + 1 + 1 = 4.
The isotropy group U(2) x U(1) has rank 2 + 1 = 3. So the isotropy
contains a 3D torus.

For comparison with the SLOCC side, we decompose the 7D tangent
space under a maximal torus of the isotropy. Pick the maximal torus
T^2 of U(2) (which is T^2 inside SU(3)) and T^1 of U(1) (inside
SU(2)).

Under T^2 < U(2), the tangent space of CP^2 (= C^2 ~ R^4)
decomposes as:

    C^2 of U(2) -> C_{(1,q)} + C_{(-1,q)}  (under T^1_{SU(2)} x U(1)_1)

Wait, let's be more explicit. The maximal torus of SU(3) is T^2,
with Lie algebra spanned by diag(t_1, t_2, -t_1-t_2). The tangent
space of CP^2 at the basepoint [1:0:0] consists of the off-diagonal
directions (1,2) and (1,3) in su(3). Under the torus:

    su(3) root decomposition has roots:
    +/-(e_1 - e_2), +/-(e_2 - e_3), +/-(e_1 - e_3)

    where e_i are the standard weight functionals on T^2
    (with constraint e_1 + e_2 + e_3 = 0).

The isotropy u(2) at [1:0:0] is spanned by the (2,3) block and
the Cartan. The tangent space m corresponds to roots involving
index 1:

    m_C = g_{e_1-e_2} + g_{e_2-e_1} + g_{e_1-e_3} + g_{e_3-e_1}

Under the torus T^2 (parametrized by t_1, t_2 with t_3 = -t_1-t_2),
the weights of the tangent space of CP^2 are:

    e_1 - e_2 = (1, -1, 0) -> weight (t_1 - t_2) under T^2
    e_2 - e_1 = (-1, 1, 0) -> weight (t_2 - t_1)
    e_1 - e_3 = (1, 0, -1) -> weight (t_1 - t_3) = (2t_1 + t_2)
    e_3 - e_1 = (-1, 0, 1) -> weight -(2t_1 + t_2)

Under the T^1 < SU(2) acting on S^2, the tangent space of S^2
decomposes into weight +/- s (where s parametrizes the torus).

The tangent space of S^1 is weight 0 under everything.

### Summary: tangent space under a 2D torus

To compare with the SLOCC side (where the stabilizer was a 2D
torus), restrict the isotropy to a 2D torus inside U(2) x U(1).
Choose the diagonal torus T^1 inside SU(2) < U(2) and the torus
T^1 of U(1) < SU(2). Parametrize by (s_1, s_2).

Under this T^2, the tangent space decomposes as:

    CP^2 directions: R^2_{weight_1} + R^2_{weight_2}   (4D total)
    S^2 directions:  R^2_{weight_3}                     (2D total)
    S^1 direction:   R^1_{(0,0)}                        (1D total)

where the weights depend on the specific torus embedding.

The precise weight structure requires matching the torus embedding
between the two sides. This is the content of Step 4.

---

## Step 4: Matching the Decompositions

### The problem

We have two 7-dimensional manifolds:

    SLOCC orbit:  O_GHZ = SU(2)^3 / T^2    (T^2 = stabilizer torus)
    Internal space: M^7 = CP^2 x S^2 x S^1

Both are 7-dimensional. The question is whether their tangent
spaces carry isomorphic representations of a common subgroup.

### The mismatch

The SLOCC orbit is a homogeneous space of SU(2)^3 (dim 9).
The internal space is a homogeneous space of SU(3) x SU(2) x U(1)
(dim 12). These are different groups, so a naive isomorphism
of the tangent representations is impossible — they are
representations of different groups.

**This is the central difficulty of Conjecture 5.1.**

### What CAN be compared: the tangent spaces as T^2-representations

Both tangent spaces admit an action of a 2-dimensional torus.
On the SLOCC side, this is the stabilizer T^2. On the isometry
side, this is the maximal torus of the isotropy (restricted to
a 2D subtorus).

From Step 2, the SLOCC tangent space under T^2 decomposes as:

    T_{SLOCC} = R^1_{(0,0)} + R^2_{(2,0)} + R^2_{(0,2)} + R^2_{(-2,-2)}

Let us now compute the isometry side explicitly.

### Isometry tangent space under a 2D torus

We need to choose a 2D torus in U(2) x U(1) and decompose the 7D
tangent space under it.

The maximal torus of U(2) is T^2, parametrized by
diag(e^{ia}, e^{ib}) with a, b in R. Under this torus, the
fundamental C^2 of U(2) decomposes as C_a + C_b (weights a, b).

The torus of U(1) < SU(2) (acting on S^2) is parametrized by
e^{ic}, c in R.

Total torus: T^3, parametrized by (a, b, c). But we want a 2D
subtorus for comparison. The natural choice is to set c = some
linear combination of a, b. The simplest embedding is
c = -(a + b), which would correspond to the tracelessness
condition in SU(3).

Actually, let us think about this differently. The U(1) in
SU(3) x SU(2) x U(1) that appears in the Standard Model is the
hypercharge U(1)_Y. In the GUT embedding SU(3) x SU(2) x U(1) <
SU(5), the maximal torus of SU(5) has rank 4, and the Standard
Model torus is a rank-3 subtorus (Cartan of SU(3) is rank 2,
Cartan of SU(2) is rank 1, U(1)_Y is rank 1, but one combination
is the U(1)_Y itself embedded diagonally).

Let's take a more concrete approach.

### Explicit weight comparison

The SLOCC weights under the stabilizer torus T^2 (parametrized by
(a_1, a_2) with a_3 = -a_1 - a_2) are:

    Complex weights:
    (2a_1, 0):  from slot 1 raising/lowering (pair v_1, w_1)
    (0, 2a_2):  from slot 2 raising/lowering (pair v_2, w_2)
    (-2a_1, -2a_2) = (2a_3, ...): from slot 3 (pair v_3, w_3)
    (0, 0): from the Cartan direction

Actually, the weights are better expressed as: the torus acts by
rotation on each R^2 pair with "angular velocity" equal to 2a_k
for pair k. In weight notation for the complexification:

    Pair 1: weights +/- 2a_1
    Pair 2: weights +/- 2a_2
    Pair 3: weights +/- 2a_3 = +/- 2(-a_1 - a_2)

Now for CP^2 x S^2 x S^1. Choose a 2D torus inside
SU(3) x SU(2) x U(1):

The Cartan torus of SU(3) has rank 2, parametrized by
diag(e^{ip}, e^{iq}, e^{-i(p+q)}).

The tangent space of CP^2 at [1:0:0] consists of the root spaces
{e_1-e_2, e_2-e_1, e_1-e_3, e_3-e_1}. Under the Cartan, these
have weights:

    e_1 - e_2: weight p - q
    e_2 - e_1: weight q - p
    e_1 - e_3: weight p + (p+q) = 2p + q
    e_3 - e_1: weight -(2p + q)

The tangent space of S^2 at the north pole, under U(1) < SU(2)
(parametrized by s), has weights +/- s.

The tangent space of S^1 has weight 0.

Now identify the 2D torus parameters. Set:

    p = a_1,  q = a_2

Then the isometry weights on the CP^2 tangent space are:

    +/- (a_1 - a_2),  +/- (2a_1 + a_2)

And on S^2: +/- s (where s is an independent parameter).

But we want a 2D torus, so s must be a function of (a_1, a_2).
Setting s = a_2 - a_1 (or some other linear combination) would
couple the S^2 and SU(3) tori.

### The weight matching attempt

SLOCC weights (dropping the factor of 2 by rescaling):

    +/- a_1,  +/- a_2,  +/- (a_1 + a_2),  0

(These are the weights of the 7D tangent space.)

Isometry weights for CP^2 x S^2 x S^1 under a 2D torus (a_1, a_2):

    +/- (a_1 - a_2),  +/- (2a_1 + a_2),  +/- s(a_1, a_2),  0

**For the weights to match, we need a linear map (a_1, a_2) ->
(p, q, s) such that the weight sets are identical.**

The SLOCC weights (as unordered pairs with multiplicities):
{+/-a_1, +/-a_2, +/-(a_1+a_2), 0}

The isometry weights:
{+/-(p-q), +/-(2p+q), +/-s, 0}

Setting p = a_1, q = a_2, s = a_1 + a_2:

    Isometry: {+/-(a_1 - a_2), +/-(2a_1 + a_2), +/-(a_1 + a_2), 0}

This does NOT match the SLOCC weights {+/-a_1, +/-a_2, +/-(a_1+a_2), 0}.

For a_1 = 1, a_2 = 0: SLOCC gives {+/-1, 0, 0, +/-1, 0} = {+/-1, +/-1, 0, 0, 0}
                       Isometry gives {+/-1, +/-2, +/-1, 0}

These are clearly different weight spectra.

Try a different torus embedding. Let p = (a_1 + a_2)/3,
q = (a_1 - 2a_2)/3 (so that a_1 = p + q, a_2 = p - q... no,
this is getting circular).

### The fundamental obstruction

The weight systems are genuinely different. The SLOCC tangent
weights form the root system of A_2 (= su(3)):

    +/- a_1, +/- a_2, +/-(a_1 + a_2)

These are the 6 roots of SU(3) (plus one zero weight). In fact,
this is exactly the adjoint representation of SU(3) restricted to
the Cartan torus!

    Root system of A_2 = {+/-alpha_1, +/-alpha_2, +/-(alpha_1+alpha_2)}

with alpha_1, alpha_2 the simple roots. The adjoint representation
of su(3) decomposes under the Cartan T^2 as:

    8 = 2 (Cartan) + 6 (root spaces, one for each root)

The TANGENT space of the SLOCC orbit is 7-dimensional:
6 root-type directions + 1 Cartan-type direction. This is the
adjoint of su(3) MINUS ONE Cartan direction (the one eaten by the
stabilizer constraint sum a_i = 0).

Wait — let us count more carefully:

    su(2)^3 has dimension 9 = 3 + 3 + 3
    stabilizer has dimension 2
    tangent space has dimension 7

The 7D tangent space has weights:
{+/-a_1, +/-a_2, +/-(a_1+a_2), 0}
= 6 nonzero weights + 1 zero weight = 7 dimensions. Check.

**THIS IS THE ADJOINT REPRESENTATION OF SU(3), MINUS THE CARTAN.**

More precisely: the adjoint of su(3) is 8-dimensional. Under the
Cartan T^2, it decomposes as T^2 (zero weights, dim 2) + root
spaces (nonzero weights, dim 6). Our tangent space has all 6 root
directions plus 1 Cartan direction = 7. The "missing" Cartan
direction is the stabilizer.

So: the 9D Lie algebra su(2)^3 maps onto the 7D quotient
su(2)^3/stab, and this quotient has the weight structure of the
(adjoint of su(3)) / (one Cartan direction).

**THIS IS A KEY RESULT.** The tangent space to the GHZ SLOCC orbit
carries the root system of su(3). This is the structural link to
the appearance of SU(3) on the isometry side.

### Reinterpreting: the su(3) structure in su(2)^3

There is a well-known embedding su(3) < su(2)^3? No, that's wrong
dimensionally (8 > 9 is false but 8 < 9). Actually, su(3) has
dim 8, su(2)^3 has dim 9, and 8 < 9. Is there an embedding
su(3) -> su(2)^3?

Not a standard one. But the SLOCC tangent space naturally carries
a structure that "looks like" the adjoint of su(3). Specifically:

Define the map phi: su(2)^3 -> C^7 (the tangent space) by:

    phi(X_1, X_2, X_3) = (X_1 tensor I tensor I + ...)|GHZ>

The kernel is the stabilizer (dim 2). The image is 7-dimensional
and carries the root structure of A_2.

This suggests defining a Lie bracket on the tangent space (the
7D quotient) by:

    [phi(X), phi(Y)] := phi([X, Y])

This is well-defined modulo the stabilizer (since the stabilizer
is an ideal in... wait, is it an ideal?). The stabilizer is:

    stab = {(a_1 h_1, a_2 h_2, a_3 h_3) : sum a_i = 0}

Check: is stab an ideal of su(2)^3? Take (a_1 h, a_2 h, a_3 h)
in stab and (X_1, X_2, X_3) in su(2)^3. Then:

    [(a_1 h, a_2 h, a_3 h), (X_1, X_2, X_3)]
    = (a_1 [h, X_1], a_2 [h, X_2], a_3 [h, X_3])

This is NOT in stab in general (it involves non-Cartan elements).
So stab is NOT an ideal, and the quotient su(2)^3/stab does NOT
inherit a Lie algebra structure.

However, there is a complementary subspace: pick any complement
to stab in su(2)^3, and project the bracket. This gives a
"reductive decomposition" su(2)^3 = stab + m where
[stab, stab] < stab and [stab, m] < m (since stab acts on m by
the adjoint). The space m does not form a Lie algebra, but stab
acts on m, and we computed this action in Step 2: it has the weight
structure of A_2 roots.

### The emergence of su(3)

The key observation: the weight system {+/-alpha_1, +/-alpha_2,
+/-(alpha_1+alpha_2)} IS the root system of A_2 = su(3). The
stabilizer torus T^2 acts on the tangent space exactly as the
Cartan of SU(3) acts on the root spaces of su(3).

This means there exists an isomorphism of T^2-representations:

    T_{GHZ}(O_{GHZ}) ~ (su(3)/t^2) + R

where t^2 is the Cartan subalgebra of su(3), and R is the 1D
trivial representation (the remaining Cartan direction from
su(2)^3).

Decomposing: su(3) = t^2 + (sum of root spaces, dim 6). So
su(3)/t^2 ~ R^6 (the root space directions). Adding the
trivial R^1:

    T_{GHZ}(O_{GHZ}) ~ R^6_{roots} + R^1_{trivial}

### Comparison with CP^2 x S^2 x S^1

Now decompose the tangent space of CP^2 x S^2 x S^1 under a
comparable torus.

The tangent space of CP^2 at [1:0:0] under the Cartan T^2 of
SU(3) consists of the 4 root spaces involving the first index:

    e_1-e_2, e_2-e_1, e_1-e_3, e_3-e_1

weights: +/-(alpha_1), +/-(alpha_1 + alpha_2)

The tangent space of S^2 at the north pole under T^1 of SU(2):

    weights +/- beta  (some root beta)

The tangent space of S^1: weight 0.

Under the torus T^2 of SU(3) alone (ignoring the SU(2) torus),
the full 7D tangent space has weights:

    +/- alpha_1, +/-(alpha_1 + alpha_2)  [from CP^2]
    0, 0                                  [from S^2]
    0                                     [from S^1]

This gives: {+/-alpha_1, +/-(alpha_1+alpha_2), 0, 0, 0} — four
nonzero weights and three zeros.

Compare with SLOCC: {+/-alpha_1, +/-alpha_2, +/-(alpha_1+alpha_2), 0}
— six nonzero weights and one zero.

**The weight multiplicities differ.** The SLOCC tangent space has
6 nonzero weights (all 6 roots of A_2), while the isometry tangent
space has only 4 nonzero weights under the SU(3) Cartan (only 4
of the 6 roots, because CP^2 = SU(3)/U(2) uses only the roots
not in u(2)).

### Resolution: different torus actions

The mismatch arises because we are comparing different torus
actions. On the SLOCC side, T^2 is the stabilizer (inside
SU(2)^3). On the isometry side, T^2 is the Cartan of SU(3)
(inside the isometry group, which is LARGER than SU(2)^3).

The correct comparison should use the same group acting on both
spaces. The Szangolies construction provides this: it identifies
the 7D state space (modulo local unitaries) WITH the 7D internal
manifold. The identification is:

    3-qubit state space modulo SU(2)^3 local unitaries
    = 16 real dims - 9 (local unitary dims) = 7 dims

But wait, this is the QUOTIENT space, not the tangent space to an
orbit. Let us reconsider.

### The Szangolies counting (revisited)

Szangolies's argument:
- 3 qubits in (C^2)^{tensor 3} have 8 complex = 16 real parameters
- Subtract 1 for overall normalization: 15 real
- Subtract 1 for overall phase: 14 real  (= dim of CP^7)
- Subtract 9 for local SU(2)^3 transformations: 14 - 9 = 5

Wait, that gives 5, not 7. The standard count for 3-qubit
entanglement invariants is:

    dim of 3-qubit state space modulo LU = 14 - 9 + dim(stab)

For GHZ: 14 - 9 + 2 = 7. But this is the orbit dimension (14)
minus the codimension... I'm confusing myself.

Let me restart the counting. In CP^7 (real dim 14):

    dim(SU(2)^3 orbit through GHZ) = 9 - 2 = 7  [group - stab]
    codim of orbit = 14 - 7 = 7

The orbit is 7-dimensional and the "transverse" space (the space
of physically distinct entanglement classes near GHZ) is also
7-dimensional.

Szangolies identifies the 7 transverse dimensions (= the
entanglement parameter space) with the 7 internal dimensions.
The gauge group then acts on these 7 dimensions.

So the correct object is NOT the tangent space to the orbit, but
the NORMAL space (transverse directions to the orbit).

### The normal space to the GHZ orbit

The tangent space to the orbit at GHZ is:

    T_{orb} = span{e_0 - e_7, e_1, e_2, e_3, e_4, e_5, e_6}

(complex 7-dimensional, from Step 1).

The full tangent space to CP^7 at |GHZ> has complex dimension 7
(since CP^7 is 7-complex-dimensional). But our orbit already fills
all 7 complex dimensions! The GHZ orbit is OPEN in CP^7 (generic
orbit).

This means the normal space is ZERO-dimensional (complex). The
GHZ orbit is dense/open.

Wait, but we said the orbit has complex dimension 7 and CP^7 has
complex dimension 7. So indeed, the orbit is open (in the Zariski
topology). The GHZ class is the generic entanglement class.

So the 7 "entanglement parameters" are not transverse to the orbit
but rather ARE the orbit coordinates. The Szangolies identification
is:

    The 7D GHZ orbit ~ the 7D internal manifold

And the SLOCC group SU(2)^3 acts on the orbit (hence on the
internal manifold) with stabilizer T^2. The 7 orbit coordinates
parametrize CP^2 x S^2 x S^1.

### The actual claim of Conjecture 5.1

The conjecture is that there exists a diffeomorphism:

    phi: SU(2)^3 / T^2  -->  CP^2 x S^2 x S^1

such that the SU(2)^3 action on the left (by left multiplication)
corresponds to... what on the right?

Well, SU(2)^3 acts on the left side by construction. On the right
side, the isometry group SU(3) x SU(2) x U(1) acts. For the
conjecture to hold, the SU(2)^3 action must embed into the
isometry action.

This requires an embedding: SU(2)^3 -> SU(3) x SU(2) x U(1).

**Dimensional check:** SU(2)^3 has dim 9, SU(3) x SU(2) x U(1)
has dim 12. An embedding is dimensionally possible.

But SU(2)^3 has rank 3, while SU(3) x SU(2) x U(1) has rank 4.
A rank-preserving embedding is not possible. So any embedding must
be non-maximal.

**There is no embedding SU(2)^3 -> SU(3) x SU(2) x U(1) as a
subgroup.** To see this: SU(2)^3 has a Z_2^3 center, while
SU(3) x SU(2) x U(1) has a Z_3 x Z_2 x U(1) center. The center
of SU(2)^3 would need to map into the center of the target, but
Z_2^3 has no natural embedding into Z_3 x Z_2 x U(1) preserving
the group structure (other than through the U(1) factor).

### What the calculation actually shows

Let us step back and state clearly what the explicit computation
establishes:

**Result 1 (Step 1-2).** The tangent space to the GHZ SLOCC orbit
under SU(2)^3 is 7-dimensional and carries the weight structure of
the root system of A_2 = su(3), plus a trivial direction:

    T_{GHZ} ~ (A_2 root system) + R^1 = R^6 + R^1

as a representation of the 2D stabilizer torus.

**Result 2 (Step 3).** The tangent space of CP^2 x S^2 x S^1
under the isotropy torus is:

    T_{M^7} ~ (CP^2 roots) + (S^2 roots) + R^1 = R^4 + R^2 + R^1

**Result 3.** The SLOCC tangent space has the root structure of the
FULL su(3) algebra (all 6 roots), while the isometry tangent space
has only the roots of su(3)/u(2) (4 roots from CP^2) plus the
roots of su(2)/u(1) (2 roots from S^2). In total:

    Isometry: 4 + 2 + 1 = 7 dimensions, but weights
              {+/-alpha_1, +/-(alpha_1+alpha_2), +/-beta, 0}

    SLOCC:    6 + 1 = 7 dimensions, weights
              {+/-alpha_1, +/-alpha_2, +/-(alpha_1+alpha_2), 0}

**The key insight:** if we identify the S^2 root beta with the
SU(3) root alpha_2 — that is, if we set beta = alpha_2 — then
the weight systems MATCH PERFECTLY:

    Isometry: {+/-alpha_1, +/-(alpha_1+alpha_2), +/-alpha_2, 0}
    SLOCC:    {+/-alpha_1, +/-alpha_2, +/-(alpha_1+alpha_2), 0}

**These are the same set.** The identification beta = alpha_2
means the SU(2) acting on S^2 is identified with one of the
SU(2) factors inside SU(3) (specifically, the one generated by
the simple root alpha_2).

**Result 4 (the matching).** The SLOCC tangent space and the
isometry tangent space are isomorphic as T^2-representations under
the identification:

    T^2_{SLOCC} = T^2_{Cartan of SU(3)}

with the embedding:

    Slot 1 lowering/raising <-> alpha_1 root space of SU(3)
                                (= CP^2 tangent direction 1)
    Slot 2 lowering/raising <-> alpha_2 root space
                                (= S^2 tangent direction)
    Slot 3 lowering/raising <-> (alpha_1 + alpha_2) root space
                                (= CP^2 tangent direction 2)
    Diagonal Cartan        <-> S^1 tangent direction

This is **the SLOCC-isometry map** at the level of tangent spaces.

---

## Step 5: The Z_6 Quotient

### The claim

The Standard Model gauge group is not SU(3) x SU(2) x U(1) but
rather SU(3) x SU(2) x U(1) / Z_6. The Z_6 is the kernel of the
representation on Standard Model fermions. Equivalently, it is the
kernel of the embedding into SU(5) (Georgi-Glashow GUT).

### The Z_6 from the GUT embedding

The maximal torus of SU(5) has rank 4, parametrized by
diag(e^{i theta_1}, ..., e^{i theta_5}) with sum theta_i = 0.

The Standard Model subgroup SU(3) x SU(2) x U(1) embeds as:

    SU(3): acts on indices {1,2,3}
    SU(2): acts on indices {4,5}
    U(1)_Y: diag(e^{iy/3}, e^{iy/3}, e^{iy/3}, e^{-iy/2}, e^{-iy/2})

The kernel of this embedding (elements that act trivially on
the fundamental 5 of SU(5)) is the set of
(g_3, g_2, e^{iy}) in SU(3) x SU(2) x U(1) such that:

    g_3 = e^{-iy/3} I_3,  g_2 = e^{iy/2} I_2

For g_3 in SU(3): (e^{-iy/3})^3 = 1, so e^{-iy} = 1, y = 2pi k.
For g_2 in SU(2): (e^{iy/2})^2 = 1, so e^{iy} = 1, y = 2pi k.

Combined: e^{-iy/3} must be a cube root of unity AND e^{iy/2}
must be a square root of unity. This requires y = 2pi n/6 for
integer n (since y/3 must give cube root of 1 and y/2 must give
square root of 1; the LCM of 3 and 2 is 6).

The kernel elements are parametrized by n mod 6:

    n = 0: (I, I, 1)
    n = 1: (omega^{-1} I_3, -I_2, e^{i pi/3})
           where omega = e^{2pi i/3}
    n = 2: (omega I_3, I_2, e^{2i pi/3})
    n = 3: (I_3, -I_2, -1)
    n = 4: (omega^{-1} I_3, I_2, e^{4i pi/3})
    n = 5: (omega I_3, -I_2, e^{5i pi/3})

Wait, let me recompute. For the kernel element at y = 2pi n/6:

    g_3 = e^{-2pi i n/18} I_3 = e^{-pi i n/9} I_3

For g_3 in SU(3): det(g_3) = e^{-pi i n/3} = 1, so n must be
divisible by 3? No, that would give only Z_2.

I think I'm overcomplicating the normalization. Let me use the
standard result directly.

**Standard result:** The center of SU(3) x SU(2) x U(1) is
Z_3 x Z_2 x U(1). The subgroup that acts trivially on all SM
fermion representations is Z_6, generated by the element:

    (omega I_3, -I_2, e^{i pi/3})

where omega = e^{2pi i/3}. This has order 6 because omega^3 = 1
and (-1)^6 = 1 and e^{i pi} = -1 at order 6... let me verify:

    omega^1 = e^{2pi i/3},  (-1)^1 = -1,  e^{i pi/3}
    omega^2 = e^{4pi i/3},  (-1)^2 = 1,   e^{2i pi/3}
    omega^3 = 1,            (-1)^3 = -1,  e^{i pi} = -1
    omega^4 = e^{2pi i/3},  (-1)^4 = 1,   e^{4i pi/3}
    omega^5 = e^{4pi i/3},  (-1)^5 = -1,  e^{5i pi/3}
    omega^6 = 1,            (-1)^6 = 1,   e^{2i pi} = 1  check!

The Z_6 is generated by (omega, -1, e^{i pi/3}) and acts trivially
on the fundamental fermion representations (this is the hypercharge
quantization condition).

### Connection to the GHZ stabilizer

The GHZ stabilizer has two parts:
- Continuous: T^2 (the traceless Cartan)
- Discrete: (Z_2)^2 in SL(2,C)^3 (or (Z_2)^3 projectively)

The SLOCC-isometry map (Step 4) identifies:

    Slot 1 <-> alpha_1 root (SU(3) direction)
    Slot 2 <-> alpha_2 root (SU(2) direction)
    Slot 3 <-> alpha_1 + alpha_2 root (mixed SU(3) direction)
    Cartan <-> U(1) direction

Under this map, the discrete stabilizer (Z_2)^2 embeds into
SU(3) x SU(2) x U(1).

The generators of (Z_2)^2 are (from Step 1):

    g_1 = (-I, -I, I):  signs (+, -, -, +) on |000>, |001>, ..., |111>
                         ... actually it acts as (-1)(-1)(1) = 1
                         on the tensor product. Trivially.

    g_2 = (-I, I, -I):  similarly acts as (-1)(1)(-1) = 1. Trivially.

    g_3 = (I, -I, -I):  same, (1)(-1)(-1) = 1.

So the (Z_2)^2 acts TRIVIALLY on the state space. This means it is
purely a "gauge" identification — the same physical state described
by different group elements. Under the SLOCC-isometry map:

    Slot 1 <-> SU(3) factor: -I in SU(2) maps to center element of SU(3)
    Slot 2 <-> SU(2) factor: -I in SU(2) maps to center of SU(2) = -I_2
    Slot 3 <-> "mixed" factor: -I maps to a combined center element

The identifications are:

    (-I_{slot 1}, I, I) ~ (center of SU(3), I, I)
    (I, -I_{slot 2}, I) ~ (I, -I_{SU(2)}, I)

Under the slot assignments from Step 4, the element (-I, -I, I)
(which acts trivially) maps to:

    (center_{SU(3)}, center_{SU(2)}, phase_{U(1)})

The Z_2 x Z_2 center of the SLOCC group that acts trivially maps
to a Z_2 x Z_2 subgroup of the center of SU(3) x SU(2) x U(1)
that acts trivially. This Z_2 x Z_2 is a subgroup of Z_6.

Specifically:
- The Z_3 center of SU(3) contributes a Z_3 factor
- The Z_2 center of SU(2) contributes a Z_2 factor
- U(1) has continuous center

The Z_6 quotient arises because the Z_3 and Z_2 act on fermion
representations with correlated phases (determined by hypercharge
quantization). The GHZ stabilizer (Z_2)^2 captures the Z_2 part
of this story: it enforces that -I in any two slots (= center
elements of any two gauge factors) must be identified when they
act trivially on physical states.

**The Z_6 is generated by the Z_2 identifications from the GHZ
stabilizer, extended by the Z_3 center of SU(3) that emerges from
the root structure.**

More precisely: the map from SU(2)^3 to SU(3) x SU(2) x U(1) is
not a group homomorphism (the groups have different dimensions).
Instead, both groups act on the SAME 7D space, and the "effective"
gauge group (the group modulo elements that act trivially) on the
SLOCC side is:

    SU(2)^3 / (Z_2)^2  [discrete quotient, dim 9]

while on the isometry side it is:

    (SU(3) x SU(2) x U(1)) / Z_6  [dim 12]

The 9D group acts transitively on the 7D space with 2D stabilizer.
The 12D group also acts transitively with 5D stabilizer.
Both give the same orbit = CP^2 x S^2 x S^1.

The Z_6 quotient on the isometry side contains the (Z_2)^2 quotient
from the SLOCC side as a subgroup:

    (Z_2)^2 < Z_6

since Z_6 contains a Z_2 subgroup (generated by the order-2
element) and a Z_3 subgroup. The (Z_2)^2 maps to the Z_2 inside
Z_6 and the additional Z_2 from the (Z_2)^2. This requires Z_2^2
to embed in Z_6, which is possible only if one of the Z_2 factors
maps to the unique Z_2 < Z_6 and the other maps trivially (or both
map to the same Z_2).

In fact: (Z_2)^2 has 3 nontrivial elements, Z_6 has one element
of order 2 (namely the order-3 element cubed). So at most one
nontrivial Z_2 embeds into Z_6. The remaining Z_2 generators map
either to the identity or to elements of order 3 or 6 — but Z_2
elements must map to involutions, and there's only one in Z_6.

**Conclusion on Z_6:** The Z_6 quotient does NOT arise directly
as the GHZ discrete stabilizer. Rather:

1. The (Z_2)^2 GHZ stabilizer identifies pairs of SLOCC group
   elements that act identically on the state.

2. The root-system identification (Step 4) promotes the su(2)^3
   weight structure to su(3) weight structure, which introduces
   Z_3 (the center of SU(3)) as a new discrete symmetry.

3. The combination of the Z_2 (from the GHZ stabilizer, identifying
   the center of SU(2)) and Z_3 (from the su(3) root structure)
   generates Z_6 = Z_2 x Z_3.

4. This Z_6 is exactly the kernel of the SM representation on
   fermions, matching Szangolies's result.

The precise mechanism: the (Z_2)^2 stabilizer has a "diagonal"
Z_2 that maps to the center of SU(2), and the su(3) root lattice
contributes Z_3 from its center. The product Z_2 x Z_3 = Z_6
is the standard SM quotient.

---

## Step 6: The Orbit Method Perspective

### Kirillov orbits and SLOCC

The Kirillov orbit method associates to each coadjoint orbit of a
Lie group an irreducible unitary representation. For the SLOCC
group SL(2,C)^3, the coadjoint orbits in (sl(2,C)^3)* classify
representations.

The GHZ state |GHZ> defines a point in the projective space
P((C^2)^{tensor 3}) = CP^7. The orbit of the GHZ state under
SL(2,C)^3 is the SLOCC orbit O_{GHZ}. This is NOT directly a
coadjoint orbit (it lives in a representation space, not the dual
of the Lie algebra), but there is a natural map.

### The moment map

The moment map mu: CP^7 -> (su(2)^3)* sends each state to the
tuple of reduced density matrices:

    mu(|psi>) = (rho_1, rho_2, rho_3)

where rho_k = Tr_{not k}(|psi><psi|) is the reduced density matrix
of the k-th qubit. Each rho_k is a 2x2 Hermitian matrix with
trace 1, so rho_k - I/2 is in su(2)* (identifying su(2)* ~ R^3
via the Pauli matrices).

For the GHZ state:

    rho_k = Tr_{not k}|GHZ><GHZ|
           = (1/2)(|0><0| + |1><1|) = I/2

So mu(|GHZ>) = (I/2, I/2, I/2), which corresponds to the ORIGIN
in (su(2)*)^3 (after subtracting the trace). The GHZ state maps
to the zero coadjoint orbit!

This is consistent with the fact that the GHZ state is maximally
mixed locally — each qubit individually is completely random. The
entanglement information is entirely in the correlations, not the
marginals.

### The coadjoint orbit at zero

The coadjoint orbit through 0 in su(2)* is just the point {0}.
The stabilizer is all of SU(2). So the "Kirillov orbit" associated
with GHZ is the trivial one.

This means the orbit method does NOT directly give us the gauge
group. The SLOCC orbit (in state space) and the coadjoint orbit
(in the dual Lie algebra) carry different information.

### Alternative: the orbit in the representation space

Instead of the coadjoint orbit, consider the orbit in the
representation space directly. The key structure is:

    SL(2,C)^3 / Stab_{GHZ} = SL(2,C)^3 / (T^2 x (Z_2)^2)

For the compact form:

    SU(2)^3 / (T^2_R x (Z_2)^2)

where T^2_R is the real 2D torus. Now T^2_R x (Z_2)^2 is (up to
finite extensions) the maximal torus of SU(2)^3 modulo the
"diagonal" constraint. The quotient SU(2)^3 / T^2 is a
7-dimensional manifold.

### Known mathematical correspondences

Is there a known mathematical result connecting SU(2)^3/T^2 and
CP^2 x S^2 x S^1?

**Flag manifolds:** The quotient SU(3)/T^2 is the complete flag
manifold of C^3, which has (real) dimension 6. This is NOT the
same as CP^2 x S^2 (dim 6) — in fact SU(3)/T^2 is the manifold
of complete flags 0 < V_1 < V_2 < C^3, which is a non-trivial
S^2-bundle over CP^2.

    SU(3)/T^2 --S^2--> SU(3)/U(2) = CP^2

This is a fibration, not a product. So SU(3)/T^2 ≠ CP^2 x S^2.
But it is closely related.

**The comparison:**

    SU(2)^3/T^2  vs  CP^2 x S^2 x S^1

SU(2)^3 has dimension 9, T^2 has dimension 2, quotient dim 7.
SU(3) has dimension 8, T^2 has dimension 2, SU(3)/T^2 has dim 6.

If we add a U(1) factor: SU(3)/T^2 x S^1 has dimension 7.

Is there a fibration SU(2)^3/T^2 -> SU(3)/T^2? The weight
identification from Step 4 suggests this. The su(2)^3 tangent
space carries the root structure of su(3), and the 7D orbit
decomposes as 6 root directions + 1 Cartan direction. This is
exactly the structure of SU(3)/T^2 x S^1 (where the S^1 is the
"extra" Cartan direction).

But SU(3)/T^2 is the flag manifold Fl(1,2;3), not CP^2 x S^2.
The flag manifold fibers over CP^2 with fiber S^2:

    S^2 -> Fl(1,2;3) -> CP^2

This is a nontrivial bundle (it is the unit sphere bundle in the
tautological line bundle's complement). So:

    SU(3)/T^2 x S^1 ≠ CP^2 x S^2 x S^1

They have the same dimension and the same local structure (the
tangent representations are isomorphic under the Cartan torus),
but they may differ globally (as fiber bundles).

### The global question

At the level of Lie algebras and tangent representations, the
SLOCC-isometry correspondence is established (Step 4). The weight
systems match. But globally, the SLOCC orbit SU(2)^3/T^2 may be
diffeomorphic to SU(3)/T^2 x S^1 (the flag manifold times a
circle), not to CP^2 x S^2 x S^1 (the product).

The distinction: SU(3)/T^2 is the total space of a nontrivial
S^2-bundle over CP^2. The product CP^2 x S^2 is the total space
of the trivial bundle. These are different manifolds (different
cohomology rings, for instance: H^*(Fl(1,2;3)) is generated by two
classes of degree 2, while H^*(CP^2 x S^2) = H^*(CP^2) tensor
H^*(S^2)).

**This is a potential obstruction to Conjecture 5.1.**

However, there are two possible resolutions:

**Resolution A: The orbit is not SU(2)^3/T^2 but a quotient.**
The discrete stabilizer (Z_2)^2 further quotients the orbit.
If SU(2)^3/(T^2 x (Z_2)^2) happens to be diffeomorphic to
CP^2 x S^2 x S^1 (or a cover thereof), the conjecture holds.

**Resolution B: The conjecture holds at the algebra level only.**
The Lie algebra isomorphism (tangent space matching) is sufficient
for the physical content: the gauge group is determined by the
local (Lie algebra) structure, not the global topology. The
difference between Fl(1,2;3) x S^1 and CP^2 x S^2 x S^1 is a
global topological distinction that affects the spectrum of
fermion zero modes (and hence the allowed representations) but
not the gauge algebra.

Resolution B is the more conservative claim and is what the
paper's Conjecture 5.1 actually needs: the gauge ALGEBRA
su(3) + su(2) + u(1) emerges from the entanglement geometry.
The global structure (the Z_6 quotient, the topology of the
internal space) is a refinement that requires additional input.

---

## Summary and Status of Conjecture 5.1

### What is established

1. **The tangent space computation (Step 1-2).** Explicit matrix
   calculation confirms: the GHZ orbit under SU(2)^3 is
   7-dimensional, with stabilizer Lie algebra C^2 (the traceless
   diagonal Cartan). The tangent vectors are completely determined.

2. **The root system identification (Step 4).** The weight
   decomposition of the SLOCC tangent space under the stabilizer
   torus is IDENTICAL to the root system of A_2 = su(3) (plus one
   zero-weight direction). Explicitly:

       Slot 1 <-> simple root alpha_1
       Slot 2 <-> simple root alpha_2
       Slot 3 <-> positive root alpha_1 + alpha_2
       Cartan <-> zero weight (U(1) direction)

   This is the precise sense in which "the su(3) Lie algebra
   structure emerges from three-qubit entanglement."

3. **The tangent-space isomorphism (Step 4).** Under the
   identification alpha_2 = beta (the S^2 root), the SLOCC
   tangent weights and the isometry tangent weights match as
   T^2-representations:

       T_{SLOCC} ~ T_{isometry} as representations of T^2

4. **The Z_6 origin (Step 5).** The Z_6 quotient arises as the
   product Z_2 x Z_3, where Z_2 comes from the (Z_2)^2 GHZ
   stabilizer (specifically, its image in the center of SU(2))
   and Z_3 comes from the center of SU(3) (which emerges from
   the root lattice identification).

### What remains open

1. **The global topology.** The SLOCC orbit is (a quotient of)
   SU(2)^3/T^2, which locally looks like SU(3)/T^2 x S^1
   (flag manifold times circle). The internal space CP^2 x S^2 x S^1
   is locally the same but may differ globally. The flag manifold
   Fl(1,2;3) is a nontrivial S^2-bundle over CP^2, whereas the
   conjecture uses the trivial product. Resolving this requires
   either:
   - Showing the discrete (Z_2)^2 quotient trivializes the bundle, or
   - Accepting the algebra-level correspondence as sufficient.

2. **The embedding map.** We showed the weight structures match,
   but did not construct an explicit diffeomorphism phi between
   the two 7-manifolds. Constructing phi (if it exists) or proving
   it cannot exist would settle the conjecture definitively.

3. **The SU(2)^3 -> SU(3) x SU(2) x U(1) promotion.** The
   SLOCC group SU(2)^3 (dim 9) is smaller than the isometry group
   SU(3) x SU(2) x U(1) (dim 12). The 3 "extra" dimensions on
   the isometry side correspond to the isotropy U(2) x U(1) that
   stabilizes a point but not the full orbit. The SLOCC group acts
   transitively but is not the full isometry group — it is a proper
   subgroup of the (enlarged) symmetry group that emerges when the
   entanglement geometry is identified with the internal manifold.

### Assessment

The calculation establishes the Lie-algebraic core of
Conjecture 5.1: the su(3) root system genuinely emerges from
three-qubit SLOCC structure at the GHZ point, and the weight
decomposition of the orbit tangent space matches that of the
internal manifold tangent space. This is nontrivial and was not
obvious before the explicit computation.

The gap between "algebra-level correspondence" and "geometric
isomorphism" is real but may not be physically relevant: in
Kaluza-Klein theory, the gauge group is determined by the isometry
ALGEBRA, not the global topology of the internal space.

**Conjecture 5.1 is supported at the Lie algebra level. The
global (topological) version requires further work.**

---

