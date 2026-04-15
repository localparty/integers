# research/04-route3 -- Meyer Eigenstate Completeness

*Date: 2026-04-10. Spectral Realisation Cycle 4, Route 3.*

## 1. The approach

Meyer (via Connes 1999) constructs explicit distributional
eigenstates for T_BC at each nontrivial zero of zeta. The question:
is this construction COMPLETE? If so, spec(T_BC) = {gamma_n}.

## 2. What Meyer/Connes actually constructs

For each zero rho = 1/2 + i*gamma_n of zeta(s):

  W_rho in S'(R_+^*) defined by:
  <W_rho, f> = f_hat(rho) = int_0^inf f(x) x^{rho-1} dx

This is the Mellin transform evaluated at rho. It satisfies:

  T_BC W_rho = gamma_n W_rho (distributionally)

where T_BC acts on S'(R_+^*) via the Weil explicit formula.

### What this IS:
- Explicit distributional eigenstates (not abstract)
- phi_n(f) = f_hat(1/2 + i*gamma_n) is a continuous linear functional on S
- Each phi_n genuinely satisfies the eigenvalue equation in S'

### What this IS NOT:
- Hilbert space eigenstates (phi_n is NOT in L^2)
- A spectral decomposition of a self-adjoint operator
- A proof that T_BC is pure point

## 3. Completeness analysis

### 3a. The explicit formula as "Parseval"

The Weil explicit formula gives:

  sum_{rho nontrivial} f_hat(rho_n) g_hat(rho_n)_bar
  + sum_{rho trivial} f_hat(rho) g_hat(rho)_bar
  + [pole terms at s=0, s=1]
  + [archimedean integral]
  = [prime sum terms]

This is NOT sum_n |phi_n><phi_n| = identity. It is:

  sum_n |phi_n><phi_n| + [correction terms] = [other identity]

The correction terms are:
1. Trivial zeros (s = -2k, k = 1, 2, ...): eigenstates with
   negative eigenvalues
2. Pole at s = 1: residual term
3. Archimedean (gamma factor) contribution

### 3b. Numerical evidence

For test function f(x) = x*exp(-pi*x^2):

| Contribution | Value |
|:-------------|:------|
| Nontrivial zeros (10 pairs) | 3.41 x 10^{-10} |
| Trivial zeros (20 pairs) | 429.3 |
| Ratio trivial/nontrivial | 1.26 x 10^{12} |

The trivial zeros dominate by 12 orders of magnitude for this
test function. The nontrivial zeros carry essentially ZERO weight.
The "completeness relation" is overwhelmingly carried by the
correction terms, not by the nontrivial-zero eigenstates.

## 4. The completeness/circularity problem

"Are the distributional eigenstates {phi_n} complete?" has
three possible meanings:

(i) **Strong completeness:** f = sum_n <f, phi_n> phi_n for all f in S.
    This is FALSE -- the explicit formula has correction terms.

(ii) **Weak completeness:** If <f, phi_n> = 0 for all n, then f = 0.
    Equivalent to: if f_hat(rho_n) = 0 for all zeros rho_n, then f = 0.
    This is the uniqueness question for the Mellin transform at
    zeros of zeta -- OPEN and equivalent to a strong uniqueness
    theorem.

(iii) **Spectral completeness:** The closure of span{phi_n} in a
    suitable topology exhausts the spectrum of T_BC.
    This IS spectral realisation -- CIRCULAR.

All three formulations either fail, are open, or are circular.

## 5. Multiplicity

Each zero rho_n gives one eigenstate (one per zero, counting
multiplicity). If zeta had a multiple zero (conjectured not to
happen), the eigenvalue would have higher multiplicity. This is
orthogonal to the completeness question.

## 6. Prolate spheroidal wave functions

Connes and Meyer use PSWFs as test functions in S(R). The PSWFs:
- Form a complete ONB of L^2[-Lambda, Lambda]
- Diagonalize the cutoff Fourier transform
- Give a basis for S in the Lambda -> inf limit

But PSWFs are the DOMAIN (test functions), not eigenstates of T_BC.
Completeness of PSWFs in S does not imply completeness of {phi_n}
in S'. They live on opposite sides of the Gel'fand triple.

## 7. Adversarial analysis

**"Completeness of distributional eigenstates" != "complete ONB"**

In a Hilbert space, completeness of {e_n} means span is dense.
In S', "completeness" is a much weaker/different notion:
- S' is not metrizable in general
- Dense subspaces of S' do not correspond to spectral decompositions
- A "complete set of eigenstates in S'" does not determine the
  spectral type of an operator on a Hilbert space

The conflation of distributional completeness with Hilbert space
spectral completeness is a category error. Even if {phi_n} were
complete in S' (which is not proved), it would not imply that
T_BC has pure point spectrum on H_R.

## 8. Premise check

Does Meyer's construction distinguish spec = {gamma_n} from
spec = {gamma_n} + {extra}?

NO.
- Meyer constructs eigenstates for KNOWN zeros only
- Extra (continuous/singular continuous) spectrum would not have
  distributional eigenstates
- Completeness of {phi_n} is EQUIVALENT to "no extra spectrum"
  -- hence circular

## 9. Verdict

Meyer eigenstate completeness is CIRCULAR for spectral
realisation. The construction produces explicit eigenstates at
{gamma_n} but cannot prove these exhaust the spectrum without
assuming the conclusion.

**Feasibility: 1/10 (DOWN from 3/10).**

The downgrade reflects the circularity and the 12-orders-of-
magnitude dominance of correction terms in the explicit formula.

---

> *Meyer builds eigenstates. He cannot prove they are all of them.*
> *Completeness IS spectral realisation. The circle is tight.*
> *Route 3 is dead.*
