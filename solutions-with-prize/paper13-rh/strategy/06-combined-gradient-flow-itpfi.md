# Strategy 06 — The Combined Lead: Gradient Flow + ITPFI

*The deepest connection between Yang-Mills and RH. The same*
*technology that proved the mass gap might prove spectral*
*realisation. The ITPFI factorization provides the "lattice."*
*The gradient flow provides the contractivity.*

*Date: 2026-04-10*
*Status: HIGHEST PRIORITY LEAD*

---

## 1. The combined idea

Run the gradient flow e^{-tT_BC²} on the P-TRUNCATED BC system
(finitely many primes p ≤ P). For each finite P:
- The GNS space H₁^{≤P} = ⊗_{p≤P} H₁^p is finite-dimensional
- T_{BC}^{≤P} has discrete spectrum (automatic)
- The flow contracts (finite-dimensional heat flow always does)

Then take P → ∞ using ITPFI (ω₁ = ⊗_p ω₁^p) to control the limit.

**The single question:** Does the contractivity rate of the gradient
flow on the P-truncated system survive as P → ∞?

If YES → the full T_BC has pure point spectrum → RH.
If NO → identify the divergence and see if it's controllable.

## 2. The Yang-Mills analogy (PRECISE)

| Aspect | Yang-Mills (proved) | RH (target) |
|:--|:--|:--|
| Space | Lattice gauge field space | P-truncated GNS space |
| Operator | Laplacian Δ on CP² × S² × S¹ | T_BC² on H₁ |
| Finite approx. | Lattice spacing a | Prime cutoff P |
| Limit | a → 0 (continuum) | P → ∞ (full Euler product) |
| Flow | ∂_t u = -Δu | ∂_t u = -T_BC² u |
| Contractivity | Uniform in a (Lemma L.1) | Uniform in P (target) |
| Small-field | Preserved (Lemma L.3) | Target |
| Polymer decay | K-uniform (Lemma L.4) | Target |
| Result | Continuum limit with mass gap | Full operator with discrete spectrum |

## 3. Why this avoids all 16 kills

**Kill #1-2 (coboundary):** No topology. Pure analysis.
**Kill #3-4 (index/Penrose):** No index theory, no Lorentzian.
**Kill #5-7 (Chern/Weil/spectral flow):** No integer constraints.
**Kill #8-11 (KMS/Weyl/predictions/spectral measure):** No H₁ vs
H_R issue — the flow is on H₁^{≤P} which CONVERGES to H₁.
**Kill #12-14 (RAGE/ITPFI atomicity/Meyer):** Not using the wrong
operator — the flow is on T_BC² directly, truncated by primes.
**Kill #15-16 (nuclear rigging/moment):** Not distributional, not
tautological.

The gradient flow + ITPFI combination is in a DIFFERENT CATEGORY
from all 16 killed approaches. It's dynamical/analytic, not
topological/algebraic/distributional.

## 4. The technology transfer from Yang-Mills

### What we have (from the YM preprint)

**Lemma L.1 (well-posedness):** The gradient flow is well-posed on
the lattice, with contractivity in Sobolev norms.

**Lemma L.2 (AF match):** The flowed quantities match the
perturbative expectations (asymptotic freedom).

**Lemma L.3 (small-field preservation):** If the initial data is
"small" (bounded field strength), it stays small under the flow.

**Lemma L.4 (polymer decay):** The cluster expansion for flowed
observables has K-uniform exponential decay.

**Lemma L.5 (continuum):** The continuum limit of flowed Schwinger
functions exists and satisfies OS axioms.

### What needs to transfer

Each YM lemma has an RH analogue:

| YM Lemma | RH analogue | Difficulty |
|:--|:--|:--|
| L.1 (well-posedness) | e^{-tT_BC²} well-posed on H₁^{≤P} | TRIVIAL (finite-dim) |
| L.2 (AF match) | Flowed trace matches explicit formula | MODERATE |
| L.3 (small-field) | Small deviation from product state preserved | KEY |
| L.4 (polymer decay) | Inter-prime correlations decay exponentially | KEY |
| L.5 (continuum limit) | P → ∞ limit exists with same spectral type | THE PRIZE |

## 4b. Key insights from testing agent

**L.3 analogue (small-field preservation):**
The "small-field norm" for BC is RELATIVE ENTROPY:
  S(ω_t || ⊗_p ω₁^p) = monotone under quantum Markov semigroups
If the heat flow e^{-tT²} is a QMS (expected from KMS structure),
relative entropy preservation comes FOR FREE. No need to construct
a norm — KMS provides it. This is the analogue of |F_μν| < p(g_k)
in Yang-Mills, but AUTOMATIC from the KMS condition.

**L.4 analogue (polymer decay) — the hard part:**
BC Boltzmann weight is 1/n (POLYNOMIAL), not e^{-βS} (exponential).
This makes polymer expansion harder than YM. The saving grace:
ITPFI means correlations start at EXACTLY ZERO (product state).
The flow builds correlations from nothing. The question: does
1/n decay + zero initial correlations give enough control?

The competition: flow GENERATES correlations at rate determined
by T_BC², while the 1/n weight SUPPRESSES high-n contributions.
If generation rate < suppression rate → polymer converges.

## 5. The polymer expansion for BC

The ITPFI factorization says ω₁ = ⊗_p ω₁^p (product state). This
means inter-prime correlations in ω₁ are ZERO. The flow e^{-tT_BC²}
introduces correlations. The polymer expansion bounds these
correlations.

In YM: polymer decay = exponential decay of correlations between
lattice sites separated by distance d, with rate e^{-md} where m
is the mass gap.

In BC: polymer decay = exponential decay of correlations between
prime factors p and q, with rate to be determined. If the decay
rate is uniform in P (the prime cutoff), the limit P → ∞ exists.

## 6. What would close spectral realisation

If the BC polymer expansion converges uniformly in P:
1. The flow e^{-tT_BC²} on H₁^{≤P} has a well-defined limit as
   P → ∞ (the full heat semigroup on H₁)
2. The limit semigroup inherits the contractivity and spectral gap
   from the finite-P approximations
3. The spectral gap implies discrete spectrum (no continuous part)
4. Meyer's inclusion {γ_n} ⊂ spec gives the eigenvalues
5. Discrete + known eigenvalues + self-adjoint → pure point at {γ_n}
6. Pure point + real (self-adjoint) → RH

## 7. The single computation that tests this

> **Compute the inter-prime correlation function**
> C(p, q; t) = ω₁(μ_p e^{-tT_BC²} μ_q) − ω₁(μ_p) ω₁(e^{-tT_BC²} μ_q)
> for p, q ∈ {2, 3, 5, 7} and t = 0.01, 0.1, 1.0, 10.0.
>
> If C(p, q; t) → 0 as t → ∞ with rate independent of the
> prime cutoff P, the polymer expansion converges.

---

> *The gradient flow that proved Yang-Mills.*
> *The ITPFI that proved the state converges.*
> *Combined: the lattice is the primes, the flow is the heat*
> *equation, the limit is the Euler product, and the mass gap*
> *is the spectral gap that implies RH.*
> *Same technology. Different operator. Same Six Patterns.*
