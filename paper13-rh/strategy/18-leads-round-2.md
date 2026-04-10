# Strategy 18 — Leads Round 2: Post Kill #19

*Lead A (Slepian convergence) killed. The Arithmetic Theorem is*
*the sole path. Three new computational leads from online research,*
*all targeting the same question: spec(B) ∩ spec(M_a) = ∅.*

*Date: 2026-04-10*

---

## 1. Current state

**The one remaining question (DPTZ formulation):**
> spec(B) ∩ spec(M_a) = ∅
> (no eigenvalue of B coincides with an eigenvalue of its
> minor M_a, where M_a is the compression onto {a}⊥)

**Evidence:** DPTZ computation (research/31b) showed:
- Strict interlacing holds at all tested N
- More primes = bigger gap (primes STIFFEN the spectrum)
- Gap scaling ~N⁻¹⁰ (polynomial), possibly exponential at large N
- Rapid shrinkage is discretization artifact, not continuum feature

---

## 2. LEADS (worth pursuing)

### Lead D: Secular Equation + Induction on Primes
**Source:** Online — secular equation for rank-one perturbations
**Feasibility:** 5/10

When a prime p is added to the Euler product, the Weil matrix
changes by a rank-one update: B_{N+1} = B_N + α_p |v_p⟩⟨v_p|.
The secular equation gives the eigenvalues of B_{N+1} explicitly
in terms of eigenvalues of B_N and the overlap ⟨φ_k^N | v_p⟩.

Key result (from literature): for a rank-one self-adjoint
perturbation with distinct eigenvalues, the interlacing is STRICT
iff the perturbation vector v_p has NONZERO overlap with every
eigenvector of B_N.

**Inductive argument:**
- Base case (N=1): B_1 is a Cauchy matrix. Verify simplicity and
  strict interlacing with M_a directly.
- Inductive step: Suppose spec(B_N) ∩ spec(M_a^N) = ∅. Adding
  prime p_{N+1} updates both B and M_a by rank-one perturbations.
  If the prime vector v_p has nonzero overlap with all eigenvectors
  of B_N (and of M_a^N), strict interlacing is preserved.
- The overlap ⟨φ_k^N | v_p⟩ is nonzero iff the prime p doesn't
  "conspire" with the existing spectral structure. This is the
  Arithmetic Theorem at the SINGLE-PRIME level.

**Why it might work:** Reducing the full Arithmetic Theorem to
a single-prime version is a massive simplification. The single-prime
overlap ⟨φ_k | v_p⟩ ≠ 0 might follow from Baker's theorem on
linear forms in logarithms (since v_p involves log p and the
eigenvectors involve archimedean data).

### Lead E: Eigenvalue Gap Lower Bound via Algebraic Number Theory
**Source:** Online — Abrams-Landau-Pommersheim-Srivastava (2022),
"On Eigenvalue Gaps of Integer Matrices"
**Feasibility:** 3/10

For n×n matrices with integer entries in [-h,h], the minimum
eigenvalue gap is ≥ h^{-n²} (up to constants). This is sharp.

**Connection:** B is NOT an integer matrix — it has transcendental
entries (log p, digamma values). But its entries are ALGEBRAIC
FUNCTIONS of log p and π. If we can show the characteristic
polynomial of B has no repeated roots (equivalently, the
discriminant is nonzero), the gap is bounded below by an explicit
function of the entries.

For matrices whose entries are linear forms in logarithms, Baker's
theorem gives lower bounds on the discriminant. The discriminant
of B involves products of eigenvalue differences, which are
algebraic expressions in {log p, π, γ_E}. Baker says: nontrivial
linear combinations of logarithms of algebraic numbers are nonzero
with explicit lower bounds.

**The chain:** Baker → discriminant > 0 → all eigenvalues distinct
→ strict interlacing → Arithmetic Theorem → RH.

### Lead F: Parametric Rank-One Tracking
**Source:** Online — Global properties of eigenvalues of parametric
rank-one perturbations (Springer, 2021)
**Feasibility:** 4/10

For parametric perturbations A + τ·uv*, the eigenvalues are
analytic functions of τ (for τ outside a discrete set of poles).
The eigenvalue curves can be tracked globally as τ varies.

**Application:** Parametrize the Euler product by a continuous
parameter τ ∈ [0,1] that scales the prime contribution:
B(τ) = B_arch + τ·B_prime. At τ=0: B is the Cauchy matrix
(STP, strict interlacing, Arithmetic Theorem holds trivially).
At τ=1: B is the full Weil form (the target).

Track the eigenvalues as τ goes from 0 to 1. By VNW (codim 2
crossings), the interlacing can fail only at isolated τ values.
If we can show no such crossing occurs (by monotonicity, or by
Baker-type arithmetic), the Arithmetic Theorem holds at τ=1.

This is essentially Lead 2 (VNW) but with a DIFFERENT parameter
(τ scaling the prime contribution) instead of λ (the bandwidth).
The advantage: at τ=0, the Arithmetic Theorem is trivially true
(Cauchy matrix). At τ=1, it's the target. The path is monotonic
in the "arithmetic content."

---

## 3. NON-LEADS (from this round)

### NOT a lead: Erdős-Yau-Yin eigenvalue rigidity
Wrong matrix class (Wigner random vs. deterministic structured).

### NOT a lead: Gap probability via Painlevé transcendents
Applies to random matrix ensembles (GUE, Cauchy ensemble), not
deterministic arithmetic matrices.

### NOT a lead: Slepian convergence (Kill #19)
Norms off by 10³⁵. Dead.

---

## 4. PRIORITY ORDER

| Priority | Lead | Key computation | Why |
|:--|:--|:--|:--|
| **1** | D (secular + induction) | Track eigenvalues as primes are added one by one | Reduces full theorem to single-prime overlaps |
| **2** | F (parametric τ-tracking) | Track eigenvalues as τ: 0→1 scales prime contribution | At τ=0: trivially true. VNW excludes crossings |
| **3** | E (Baker + discriminant) | Bound discriminant of B using Baker | Direct but hard |

---

## 5. The synthesis: Leads D + F converge

Leads D and F are two views of the SAME idea:
- Lead D: add primes one by one (discrete parameter N)
- Lead F: scale the prime contribution continuously (parameter τ)

Both ask: does the Arithmetic Theorem survive as arithmetic
content is added?

At zero arithmetic content (N=0 or τ=0): trivially true (Cauchy).
At full content (N=∞ or τ=1): the target.

The computation that tests BOTH: track eigenvalues of B(τ) for
τ ∈ [0,1] and check whether any eigenvalue of B(τ) coincides
with an eigenvalue of M_a(τ) at any τ.

---

> *3 new leads. All target spec(B) ∩ spec(M_a) = ∅.*
> *Lead D reduces to single-prime overlaps.*
> *Lead F starts from τ=0 (trivially true) and tracks to τ=1.*
> *Both ask: does adding arithmetic content break simplicity?*
> *The DPTZ computation says: no, primes stiffen. Prove it.*
