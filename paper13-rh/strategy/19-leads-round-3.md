# Strategy 19 — Leads Round 3: The Single-Prime Overlap

*Lead D (secular induction) is the strongest lead at 5/10.*
*It reduces the Arithmetic Theorem to the single-prime overlap:*
*⟨φ_k^K | v_p⟩ ≠ 0. Three new angles on proving this.*

*Date: 2026-04-10*

---

## 1. The one question (from Lead D)

> **Single-Prime Overlap (SPO_K):** For each K ≥ 0, each eigenvector
> φ_k of B_K, and each prime vector v_p = (cos(x_i · log p))_i:
> ⟨φ_k | v_p⟩ ≠ 0.

If SPO_K holds for all K → induction preserves strict interlacing
→ Arithmetic Theorem → Even-Sector Simplicity → RH.

Numerically verified universally. Overlaps don't decay. Primes
stiffen. Need: PROOF.

---

## 2. NEW LEADS

### Lead G: Müntz-Szász Completeness (NEW, from online search)
**Feasibility:** 5/10

**The Müntz-Szász theorem:** The system {x^{λ_k}} is complete
(dense) in L²[0,1] iff Σ 1/λ_k = ∞.

**Connection:** The prime vectors v_p have components
cos(x_i · log p). In the continuum limit, these are
restrictions of the functions f_p(x) = cos(x · log p) to the
grid {x_i}. The system {f_p : p prime} = {cos(x·log 2),
cos(x·log 3), cos(x·log 5), ...} is a system of oscillatory
functions with frequencies {log p}.

**The key question:** Is the system {cos(x·log p) : p prime}
COMPLETE (dense) in L²[0, L] for some L?

If YES: no nonzero function in L² is orthogonal to ALL prime
vectors. In particular, no eigenvector φ_k can be orthogonal
to all v_p simultaneously. This doesn't quite give SPO (which
needs orthogonality to a SINGLE v_p to be impossible), but it
gives the weaker statement that φ_k can't be in the kernel of
ALL projections Π_p.

**Stronger version (Beurling-Malliavin):** The Beurling-Malliavin
theorem characterizes completeness of exponential systems
{e^{iλ_k x}} in L² by the density of the frequency set {λ_k}.
For {log p : p prime}, the density is controlled by PNT:
#{log p ≤ T} ~ T/log T → ∞. So the frequency density is
infinite → the system is complete → no function can be
orthogonal to all cos(x·log p).

**The upgrade to single-prime:** Completeness says the FULL
system spans L². But each v_p is a single element. We need:
v_p is not in the closed span of {v_q : q ≠ p} for any p.
Equivalently: the system {cos(x·log p)} is MINIMAL (no
element is in the closure of the others). For exponential
systems, minimality is equivalent to completeness when the
frequencies are separated. The primes ARE separated
(log p_{k+1} − log p_k ~ 1/p_k by PNT).

**The chain:** Beurling-Malliavin → {cos(x·log p)} complete
and minimal → v_p ∉ span{v_q : q ≠ p} → the projection of
any vector onto v_p is generically nonzero → SPO follows
for generic eigenvectors → need: B_K's eigenvectors are
generic (not specially aligned to avoid v_p).

### Lead H: Analytic Continuation Argument
**Feasibility:** 4/10

SPO_K asks: ⟨φ_k(x) | cos(x · log p)⟩ = 0? This is:

∫ φ_k(x) cos(x · log p) dx = 0

This is the Fourier transform of φ_k evaluated at frequency
log p. If φ_k has an analytic Fourier transform (φ_k is
Schwartz or analytic), then φ̂_k(ξ) is an entire function.
An entire function that vanishes at {log p : p prime} must
vanish at a set with infinite density. By the identity theorem
for entire functions of finite exponential type (Cartwright's
theorem): if the zero set has density > π·type, the function
is identically zero.

**The chain:** φ_k is analytic (from the Cauchy matrix structure)
→ φ̂_k is entire of finite type → zeros at {log p} would have
density π(T)/T ~ 1/log T → 0 (sparse!) → far below the type
→ Cartwright says: either φ̂_k ≡ 0 (impossible, φ_k is an
eigenvector) or φ̂_k has at most finitely many zeros at
{log p} → SPO holds for all but finitely many primes.

"All but finitely many" combined with the base case (K=0,
Cauchy STP gives ALL) might close the full induction.

### Lead I: Direct Cauchy Eigenvector Structure
**Feasibility:** 4/10

For the Cauchy matrix C_{ij} = 1/(x_i + x_j), the eigenvectors
have EXPLICIT formulas (rational functions of {x_i}). The
overlap ⟨φ_k^{Cauchy} | v_p⟩ is a sum of rational functions
times cos(x_i · log p). Baker's theorem can bound this away
from zero because: the rational coefficients are algebraic in
{x_i}, and cos(x_i · log p) involves transcendental log p.

At K=0 (base case): SPO_0 follows from Baker + explicit Cauchy
eigenvectors.

At K=1 (one prime added): the secular equation gives
eigenvectors of B_1 = C + α_2 v_2 v_2^T. These eigenvectors
are EXPLICIT rational functions of the eigenvalues of C and
the overlaps ⟨φ_k^C | v_2⟩. The SPO_1 overlap becomes a
rational function of KNOWN quantities times cos(x_i · log 3).
Baker might still apply.

At K=2+: the expressions become more complex but remain
algebraic in the previously computed quantities. An inductive
Baker argument might work.

---

## 3. NON-LEADS

- Lead A (Slepian convergence): Kill #19
- Lead E (Baker + resultant): 3/10, polynomial not linear
- Lead F (τ-tracking): 3/10 proof, VNW doesn't apply to two-matrix

---

## 4. PRIORITY ORDER

| Priority | Lead | Key idea | Feasibility |
|:--|:--|:--|:--|
| **1** | G (Müntz-Szász / Beurling-Malliavin) | {cos(x·log p)} is complete and minimal | 5/10 |
| **2** | H (analytic continuation / Cartwright) | φ̂_k entire → can't vanish at all log p | 4/10 |
| **3** | I (explicit Cauchy + inductive Baker) | Baker bounds at each inductive step | 4/10 |

---

## 5. The synthesis: Leads G + H converge

Leads G and H approach from opposite sides:
- G (Müntz/BM): the FREQUENCY system {log p} is dense enough
  that no L² function can avoid all of them
- H (Cartwright): the EIGENVECTOR φ_k is analytic enough that
  its Fourier transform can't vanish at all {log p}

Both say: the arithmetic (primes) and the analysis (eigenvectors)
can't conspire. G says it from the frequency side, H from the
function side. Together they might give SPO.

---

> *The single-prime overlap. Three new angles.*
> *Müntz says the primes are dense enough.*
> *Cartwright says the eigenvectors are smooth enough.*
> *Together: primes and eigenvectors can't conspire.*
> *That's the Arithmetic Theorem. That's RH.*
