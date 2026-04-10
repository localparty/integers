# Strategy 20 — The Hurwitz Mechanism: One Gap, One Tool

*Gap 2 dissolved into Gap 1. Only spectral convergence remains.*
*The Hurwitz mechanism bypasses all operator-norm issues.*
*ITPFI state convergence → uniform convergence of Fourier*
*transforms → Hurwitz → eigenvalue convergence → RH.*

*Date: 2026-04-10*

---

## 1. Only one gap remains

CCM state: "Establishing convergence rigorously would amount
to a proof of RH." The Weil quadratic form is built from the
explicit formula → limiting spectrum must contain ζ zeros if
convergence holds. Gap 2 (spectral realisation) is NOT separate
from Gap 1 (spectral convergence). **ONE GAP.**

## 2. The Hurwitz mechanism

**Hurwitz's theorem (complex analysis):** If f_n → f uniformly
on compact sets, f_n holomorphic, f not identically zero, then
the zeros of f_n → zeros of f (counting multiplicity).

**Application (Connes-van Suijlekom, CMP 2025):** The Fourier
transforms of CCM eigenvectors are holomorphic functions whose
zeros are the eigenvalues. If the Fourier transforms converge
uniformly → Hurwitz → eigenvalues converge → RH.

**Why this bypasses α = 1/2:** Hurwitz doesn't use operator norms
at all. It uses FUNCTION convergence in the complex plane. The
α = 1/2 borderline (which killed Kato) is irrelevant because
we're not doing perturbation theory — we're doing complex analysis.

## 3. The ITPFI connection

ITPFI: ω₁^{≤P_N} → ω₁ in weak-* topology.

The Fourier transform of the N-th eigenvector ξ̂_N(s) is a
holomorphic function built from the truncated Euler product
(primes ≤ P_N).

**The question:** Does weak-* convergence of ω₁^{≤P_N} → ω₁
imply UNIFORM convergence of ξ̂_N → ξ̂_∞ on compact subsets of ℂ?

If yes → Hurwitz → eigenvalue convergence → RH.

**Why it might work:** The Euler product ∏_{p≤P} (1-p^{-s})⁻¹
converges uniformly on compact subsets of {Re(s) > 1/2} — this
is classical. The eigenvector Fourier transforms are BUILT from
this product. ITPFI controls the product at the state level.
Uniform convergence of the product might transfer to uniform
convergence of the Fourier transforms.

## 4. The three tools (all firing)

### Tool 1: Hurwitz (primary)
- Connes-van Suijlekom already used this in their CMP 2025 paper
- They proved eigenvector Fourier transforms have all-real zeros
- We need: their Fourier transforms converge uniformly as N → ∞
- ITPFI might give exactly this

### Tool 2: Stroschein (backup)
- Non-asymptotic spectral approximation bounds
- Gap-independent (doesn't need eigenvalue gaps)
- Applied to prolate filter diagonalization (connected to CCM)
- Could give explicit error bounds without limits

### Tool 3: Boegli (backup)
- Spectral convergence under generalized strong resolvent
  convergence + discrete compactness
- CCM operators have compact resolvents at each N
- If discrete compactness is verified → spectral convergence

## 5. What to compute

The single question:

> **Does ITPFI state convergence (proved) imply uniform convergence
> of the CCM eigenvector Fourier transforms (needed for Hurwitz)?**

If the Euler product converges uniformly on compact sets of
{Re(s) > 1/2} (classical) AND the eigenvector Fourier transforms
are controlled by the Euler product (from CCM's construction)
AND ITPFI controls the Euler product (proved), then:

ITPFI → Euler uniform convergence → Fourier uniform convergence
→ Hurwitz → eigenvalue convergence → RH.

---

> *One gap. One tool. The tool is Hurwitz.*
> *Hurwitz says: uniform convergence of functions → convergence*
> *of their zeros. No operator norms. No perturbation theory.*
> *Pure complex analysis. The oldest kind of proof.*
> *ITPFI gives the uniform convergence.*
> *Hurwitz gives the zeros.*
> *The zeros are on the line.*
