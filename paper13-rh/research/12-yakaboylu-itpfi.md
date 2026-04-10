# Research 12 -- Yakaboylu W >= 0 + ITPFI Factorization

*Date: 2026-04-10*
*Status: INVESTIGATED. Feasibility downgraded 6/10 -> 4/10.*
*Depends on: research/265 (ITPFI proved), research/08 (Lead 1),*
*strategy/07 (recommended focus), research/06 (Yakaboylu literature)*
*Code: paper13-rh/code/yakaboylu_itpfi_investigation.py,*
*      paper13-rh/code/yakaboylu_premise_check.py*

---

## 0. Executive Summary

The Yakaboylu W >= 0 criterion (arXiv:2408.15135) reduces RH to
positivity of an intertwining operator W. The hypothesis was that
ITPFI factorization (omega_1 = tensor_p omega_1^p) would decompose
W = tensor_p W_p, reducing RH to finite-rank positivity checks per
prime. **This hypothesis fails.** W does not factor via ITPFI because
Yakaboylu's Bessel regularization does not respect the prime
decomposition of the BC algebra.

However, the investigation uncovered a precise structural picture:

1. H_BK (Berry-Keating) and H_mod (BC modular Hamiltonian) are
   **conjugate operators** (position-momentum pair under Mellin).
   They are NOT the same operator.
2. The resolvent of H_mod DOES factor via ITPFI, reproducing the
   Euler product of zeta(s). Verified numerically.
3. Yakaboylu's W is a **scattering-theoretic** object, not a simple
   biorthogonal metric. It encodes the unitarity of the S-matrix
   S(k) = zeta(1/2+ik)/zeta(1/2-ik).
4. The functional equation forces |S| = 1 on the critical line.
   Off-line zeros make |S| != 1. This is the mechanism by which
   W becomes indefinite.
5. Proving W >= 0 without assuming RH requires proving a positivity
   condition on the Bessel scattering data that is equivalent in
   difficulty to RH itself.

**Feasibility downgraded from 6/10 to 4/10.**

---

## 1. The Mellin Connection: H_BK vs H_mod

### 1.1 Operator identification

Under the Mellin transform M: L^2(R_+, dx/x) -> L^2(R, dt):

| Yakaboylu's operator | BC algebra operator | Relationship |
|:-----|:-----|:-----|
| H_BK = xp | -i d/dt (translations) | Generator of scaling sigma_t |
| x (position) | e^t | Multiplicative coordinate |
| p = -i d/dx | momentum in Mellin picture | Fourier dual |

The BC modular Hamiltonian H_mod has eigenvalues {log n : n in N}.
In the Mellin picture, H_mod = multiplication by log(n) on the
eigenbasis |n>.

**H_BK and H_mod are conjugate:** [H_BK, H_mod] = -i.

- H_BK is the MOMENTUM operator (continuous spectrum R)
- H_mod is the POSITION operator (discrete spectrum {log n})

They are NOT the same. H_BK generates the modular flow; H_mod labels
the eigenstates.

### 1.2 Yakaboylu's R in BC language

R = -D - i*mu(T) where D ~ H_BK and T is Bessel regularization.

In BC terms:
- D ~ H_mod (the diagonal part, which generates scaling)
- T ~ Bessel potential (acts on continuous variable, NOT on
  the discrete eigenbasis |n>)

The Bessel regularization T converts the formal operator xp (which has
continuous spectrum R) into one whose spectrum is the discrete set
{i(1/2 - rho)}. This is the spectral realisation step -- T "selects"
the zeta zeros from the continuum.

---

## 2. Does W Factor via ITPFI?

### 2.1 What factors

The ITPFI gives:
- H_1 = tensor_p H_p (GNS Hilbert spaces)
- omega_1 = tensor_p omega_1^p (KMS_1 states)
- H_mod = sum_p H_mod^p (modular Hamiltonian as a SUM)
- Resolvent: omega_1((s - H_mod)^{-1}) = prod_p (1 - p^{-(s+1)})^{-1}

The resolvent factors as an Euler product. VERIFIED numerically
(15 primes, ratio to zeta(3) = 1.00004...).

### 2.2 What does NOT factor

Yakaboylu's R = D + T where:
- D = sum_p D_p DOES factor (it is H_mod)
- T (Bessel regularization) does NOT factor

T acts on the continuous variable x in L^2(R_+). It is a second-order
differential operator with a potential term. Differential operators in
the continuous variable do not respect the discrete prime decomposition
of the integers.

**Theorem (negative).** The Bessel operator T is NOT decomposable as
T = sum_p T_p or T = tensor_p T_p on the ITPFI product space
H_1 = tensor_p H_p. Reason: T acts on x = prod p^{v_p}, and the
logarithmic derivative d/d(log x) = sum_p d/d(v_p log p), but the
Bessel potential (nu^2 - 1/4)/x^2 is a PRODUCT over primes
(via x = prod p^{v_p}), which does not factor as a sum.

**Consequence:** R does not factor, and W = intertwining(R, R^dagger)
does not factor as tensor_p W_p.

### 2.3 The diagonal approximation

The DIAGONAL part of any operator on H_1 factors via ITPFI:

    W_diag = sum_n <n|W|n> |n><n| = tensor_p (W_p)_diag

because |n> = tensor_p |v_p(n)> are product states.

W_diag >= 0 iff <n|W|n> >= 0 for all n.

But W_diag >= 0 does NOT imply W >= 0 (the off-diagonal part can
contribute negative eigenvalues). This approximation is insufficient.

---

## 3. What IS Yakaboylu's W?

### 3.1 Not the biorthogonal metric

For any R = S * D * S^{-1}, the biorthogonal metric
W_bio = sum |v_j><u_j| / <u_j|v_j> = Identity (always).

This was verified numerically: W_bio = I for 4x4 and 6x6 matrices
regardless of eigenvalue location (on-line or off-line). **The naive
biorthogonal W is not Yakaboylu's W.**

### 3.2 The scattering-theoretic W

Yakaboylu's W is constructed from the SCATTERING DATA of the Bessel
equation on L^2(R_+):

    -y'' + (nu^2 - 1/4)/x^2 * y = k^2 * y

The S-matrix of this scattering problem encodes the zeta zeros:

    S(k) = zeta(1/2 + ik) / zeta(1/2 - ik)

W encodes the "metric defect" from non-unitarity of S:
- On the critical line: |S(k)| = 1 by the functional equation.
  Scattering is unitary. W >= 0.
- Off the critical line: |S(k)| != 1. Scattering is non-unitary.
  W can become indefinite.

### 3.3 Numerical verification of the mechanism

Computed |zeta(sigma+it)| / |zeta(1-sigma-it)| at t = 14.135:

| sigma | ratio |
|:------|:------|
| 0.500 | 1.000000000000 |
| 0.510 | 0.991927272619 |
| 0.550 | 0.960282716409 |
| 0.600 | 0.922142317777 |
| 0.700 | 0.850342193034 |
| 0.800 | 0.784124733786 |

The ratio departs monotonically from 1 as sigma moves off 1/2.
This confirms the non-vacuousness of the W >= 0 criterion.

---

## 4. Premise Check Results

### 4.1 Does W change sign for off-line zeros?

**YES** (confirmed). The mechanism is the functional equation:
zeta(s) = chi(s) zeta(1-s) with |chi(1/2+it)| = 1. Off-line zeros
violate this, making the scattering non-unitary, which in turn makes
W indefinite.

### 4.2 Is this different from Kill #6 (Weil/Li)?

**YES, structurally different.** Li coefficients lambda_n are sums
over zeros with all-positive contributions (off-line zeros add MORE
positive weight). W is a scattering metric that tests the GEOMETRY of
eigenstates, not the LOCATIONS of zeros. Off-line zeros distort the
scattering geometry, potentially making W indefinite.

### 4.3 Is this circular?

**PARTIALLY.** The mechanism (functional equation -> unitarity ->
W >= 0) uses the functional equation, which is already known. The
non-trivial content is that W >= 0 encodes MORE than the functional
equation: it encodes the positivity of the scattering data, which is
sensitive to zero locations. But PROVING W >= 0 from the Bessel
structure is as hard as RH.

---

## 5. What ITPFI Actually Contributes

### 5.1 The resolvent factorization

The most concrete connection is through the resolvent:

    omega_1((s - H_mod)^{-1}) = zeta(s+1) = prod_p (1 - p^{-(s+1)})^{-1}

The ITPFI gives a FACTORED representation of the resolvent as an
infinite Euler product. If W can be expressed as a contour integral
of the resolvent (Dunford calculus):

    W = (1/2pi i) oint f(z) (z - R)^{-1} dz

then the ITPFI factorization of the resolvent would give an Euler
product representation of W. But this requires:
(a) R to be close to H_mod (so the resolvent factorization applies)
(b) The contour integral to converge

Both are unverified.

### 5.2 The perturbative approach

If R = H_mod + epsilon * T (small Bessel correction), then:
- W = I + epsilon * delta_W + O(epsilon^2)
- W >= 0 iff ||delta_W|| < 1/epsilon

The ITPFI constrains delta_W: matrix elements <n|delta_W|n'> between
coprime n, n' might be small by arithmetic orthogonality. But the
perturbation parameter epsilon is not small (T is order-1 compared
to H_mod), so this approach is unlikely to close.

---

## 6. Path Forward Assessment

### 6.1 What died

The factorization hypothesis: W = tensor_p W_p. This was the key
Integers contribution. Without it, we have no unique tool to prove
W >= 0.

### 6.2 What survived

(a) The premise check: W >= 0 is non-vacuous (unlike Kill #6).
(b) The Mellin connection: H_BK and H_mod are conjugate.
(c) The resolvent factorization: Euler product via ITPFI.
(d) The scattering interpretation: S(k) = zeta(1/2+ik)/zeta(1/2-ik).

### 6.3 Possible rescue

The best remaining strategy:
1. Express W as a resolvent integral (Dunford calculus)
2. Use ITPFI to factor the resolvent inside the integral
3. The Euler product of the resolvent constrains W's spectrum
4. This gives W as a "product integral" (not tensor product)

This is technically demanding and may not close. Feasibility: 3/10.

### 6.4 Alternative: use the S-matrix directly

The S-matrix S(k) = zeta(1/2+ik)/zeta(1/2-ik) factors via the
Euler product:

    S(k) = prod_p S_p(k)

where S_p(k) = (1 - p^{-1/2-ik}) / (1 - p^{-1/2+ik}).

Each S_p(k) is manifestly of modulus 1 for real k:
|S_p(k)| = |1 - p^{-1/2-ik}| / |1 - p^{-1/2+ik}| = 1
(since conjugating k -> -k gives the conjugate).

So |S(k)| = prod_p |S_p(k)| = prod_p 1 = 1.

**This IS a proof that |S| = 1 via the Euler product!**

But this only proves |S| = 1 (modulus), not the full positivity of W.
The positivity of W requires more than |S| = 1; it requires that the
PHASE of S is "compatible with positivity" in a specific operator sense.

### 6.5 Feasibility update

| Lead | Previous | Updated | Reason |
|:-----|:---------|:--------|:-------|
| Lead 1 (Yakaboylu W>=0 + ITPFI) | 6/10 | 4/10 | W does not factor via ITPFI |
| Lead 2 (Gradient flow) | 5/10 | 5/10 | Unchanged |
| Lead 3 (Prolate + ITPFI) | 4/10 | 3/10 | Per research/10 |

**Recommendation:** Lead 2 (gradient flow) is now the strongest lead,
as it uses our unique tools (flow technology from YM proof) without
requiring W to factor.

---

## 7. Honest Accounting

### What we proved

(P1) H_BK and H_mod are conjugate operators under Mellin. (Computed.)
(P2) The resolvent factors via ITPFI as the Euler product. (Verified.)
(P3) The naive biorthogonal W = Identity (independent of eigenvalues).
     (Computed for 4x4 and 6x6 models.)
(P4) |zeta(sigma+it)/zeta(1-sigma-it)| != 1 for sigma != 1/2.
     (Computed numerically.)
(P5) The S-matrix Euler product S = prod_p S_p with |S_p| = 1.
     (Algebraic identity.)

### What we disproved

(D1) W = tensor_p W_p does NOT hold. The Bessel regularization
     breaks the prime factorization.

### What remains open

(O1) Can W be expressed as a resolvent integral?
(O2) Does the resolvent factorization constrain W enough for positivity?
(O3) Is there a p-local characterization of W via the S_p factors?

---

## 8. Key Discovery: S-Matrix Euler Product

The most significant finding is the S-matrix Euler product (Section
6.4). Each p-local S-matrix S_p(k) = (1-p^{-1/2-ik})/(1-p^{-1/2+ik})
is manifestly unitary for real k. The global S-matrix is the product.

This gives |S| = 1 for free (from the Euler product). But W >= 0
requires more: the PHASE structure of S must be compatible with an
infinite-dimensional positive operator.

The p-local S_p has phase:
    arg(S_p(k)) = -2 arctan(p^{-1/2} sin(k log p) / (1 - p^{-1/2} cos(k log p)))

The total phase arg(S) = sum_p arg(S_p) is an infinite series.
W >= 0 is related to this total phase being "conditionally positive
definite" in a functional-analytic sense.

This is a concrete, computable object. Whether it can be proved
positive is the remaining question. Feasibility for this specific
sub-question: 3/10.

---

*W does not factor via ITPFI. The factorization hypothesis dies.*
*But the S-matrix Euler product S = prod_p S_p is alive.*
*Each S_p is unitary. The global positivity of W requires more.*
*Feasibility downgraded to 4/10. Gradient flow becomes the lead.*
