# Web Search: Recent Progress on Spectral Realisation of Riemann Zeros

**Date:** 2026-04-09  
**Scope:** 2020--2026, all major lines of attack

---

## 1. THE CONNES PROGRAMME (2023--2026): STILL THE MAIN EVENT

### 1A. Connes--Consani--Moscovici: Prolate Wave Operators (2024)
- **Paper:** "Zeta zeros and prolate wave operators," *Annals of Functional Analysis* (2024)
  [arXiv:2310.18423](https://arxiv.org/abs/2310.18423)
- **Main result:** Introduces a *semilocal analogue* of the prolate wave operator within the
  semilocal trace formula framework. The prolate operator = (scaling operator)^2 + grading
  of orthogonal polynomials. Its positive spectrum gives the low-lying zeros; the Sonin space
  (negative spectrum) controls UV behaviour.
- **Status:** Advanced but *still partial*. They prove stability of the semilocal Sonin space
  under enlargement of the finite set of places. A "forthcoming paper" is promised for a
  second candidate operator.
- **Closes spectral realisation?** NO. Framework is incomplete.
- **New tool for us?** The prolate operator construction and Sonin space stability are
  potentially useful as an independent cross-check on our operator's UV asymptotics.

### 1B. Connes--Consani--Moscovici: Zeta Spectral Triples (Nov 2025)
- **Paper:** "Zeta Spectral Triples," [arXiv:2511.22755](https://arxiv.org/abs/2511.22755)
- **Main result:** Self-adjoint operators obtained as *rank-one perturbations* of the spectral
  triple associated with the scaling operator on [lambda^{-1}, lambda]. Euler products over
  primes p <= x = lambda^2. Caratheodory--Fejer theorem for Toeplitz matrices ensures
  self-adjointness.
- **Key finding:** Spectra *converge* towards zeros of zeta(1/2 + is) as N, lambda -> infty,
  with "striking numerical precision."
- **Closes spectral realisation?** NO. Rigorous proof of convergence would establish RH,
  but this is not yet achieved. Remains a "research programme."
- **New tool for us?** The rank-one perturbation technique and the Toeplitz/Caratheodory--Fejer
  machinery are potentially valuable. The numerical precision is encouraging validation data.

### 1C. Connes--Consani: Riemann-Roch for Spec Z (2024)
- **Paper:** Rend. Lincei Mat. Appl., DOI 10.4171/RLM/1036
- **Main result:** A novel Riemann-Roch theorem for divisors on the Arakelov compactification
  of Spec Z. Three key concepts: cohomologies H^0(D), H^1(D); integer-valued dimension;
  Serre duality. Built over the "absolute base" (sphere spectrum) using Segal Gamma-rings.
- **Formula:** chi(D) = deg(D) + 1, paralleling the function field case exactly.
- **Closes spectral realisation?** NO, but builds essential algebraic infrastructure.
- **New tool for us?** This is the deepest structural advance. If our KK framework can
  interface with the Gamma-ring foundations, the Riemann-Roch formula provides the
  missing piece for converting trace formula positivity into zero-location.

### 1D. Connes--Consani: Knots, Primes, Adele Class Space (Jan 2024)
- **Paper:** [arXiv:2401.08401](https://arxiv.org/abs/2401.08401)
- **Main result:** Geometric realisation of the knots-primes analogy within the scaling site.
  Periodic orbits C_p of length log p; mapping torus of Frobenius at p shows how primes
  "link" with each other.
- **New tool for us?** Conceptually beautiful but not directly spectral. Low priority.

### 1E. Connes' 2026 Retrospective
- **Paper:** "The Riemann Hypothesis: Past, Present and a Letter Through Time"
  [arXiv:2602.04022](https://arxiv.org/abs/2602.04022)
- **Key statement:** Connes demonstrates "remarkable approximations to the zeros of zeta"
  using a quadratic form approach expressible in 19th-century mathematics. Approximating
  values lie exactly on the critical line.
- **Remaining obstacle (per Connes):** Establishing convergence of zeros from finite to
  infinite Euler products. Requires geometric methods beyond classical analysis.
- **Assessment:** Connes himself identifies the finite-to-infinite Euler product convergence
  as THE remaining gap.

---

## 2. YAKABOYLU: INTERTWINING OPERATOR (2024--2026)

- **Paper:** "Nontrivial Riemann Zeros as Spectrum," [arXiv:2408.15135](https://arxiv.org/abs/2408.15135)
  (v15, March 2026)
- **Author:** Enderalp Yakaboylu (MPI)
- **Operator:** R = -D - i*mu(T), where D is the Berry-Keating Hamiltonian, T is a Bessel
  operator. Domain: L^2([0,infty)) with Dirichlet BC at 0.
- **Spectrum:** sigma(R) = {i(1/2 - rho) : rho in Z}, where Z includes nontrivial zeta zeros.
- **Key result:** R is non-symmetric, but an intertwining operator W exists such that
  W*R = R^dagger*W with W >= 0. If W >= 0 is proven, then Re(rho) = 1/2 for all
  nontrivial zeros. This is an operator-theoretic form of Bombieri's refinement of Weil
  positivity.
- **Critical insight:** "RH does not follow from the existence of a self-adjoint operator;
  rather, both the Hilbert-Polya conjecture and RH emerge jointly from the underlying
  positivity condition W >= 0."
- **Assumption:** Requires simplicity of all nontrivial zeros (standard conjecture).
- **Closes spectral realisation?** NO. Reduces RH to proving W >= 0.
- **New tool for us?** YES. The intertwining/positivity reformulation is potentially very
  useful. If our framework can independently establish W >= 0 via the KK heat kernel,
  this would close the argument through Yakaboylu's machinery.

---

## 3. LeCLAIR: SPECTRAL FLOW VIA SCATTERING (2024)

- **Paper:** "Spectral Flow for the Riemann zeros," [arXiv:2406.01828](https://arxiv.org/abs/2406.01828)
  Published in *Advances in Theoretical and Mathematical Physics* (2025).
- **Earlier:** "Riemann zeros as quantized energies of scattering with impurities," JHEP 2024.
- **Construction:** Single particle scattering with impurities on a circle. S-matrix from
  Euler product, unitary by construction => Hamiltonian is Hermitian, eigenvalues real.
  Quantized energy levels = zeros of zeta(s).
- **Key result:** Spectral flow criterion for RH validity. Energy gap in the free Hamiltonian.
- **Extends to:** Generalized and Grand Riemann Hypotheses.
- **Closes spectral realisation?** NO. The scattering model is suggestive but proving RH
  requires proving the spectral flow criterion.
- **New tool for us?** The S-matrix/Euler product construction is a nice cross-check.
  The scattering-with-impurities picture could interface with our gradient flow framework
  if the impurities are identified with KK modes.

---

## 4. NEGATIVE RESULTS / OBSTRUCTIONS

### 4A. Spectral-Dimension Obstruction (March 2026)
- **Paper:** "Spectral-Dimension Obstructions for Operators with Superlinear Counting Laws"
  [arXiv:2604.00052](https://arxiv.org/abs/2604.00052)
- **Authors:** Watson & Valentinuzzi
- **Result:** Single-valuation exponential kernel operators, under mild regularity, converge
  in continuum limit to a fourth-order operator with spectral dimension d_s = 1/2.
  Operators with superlinear counting (like Riemann zeros, which have N(T) ~ T log T)
  have d_s = 2. These are mutually exclusive under unitary equivalence.
- **Impact:** Rules out a *specific class* of kernel-based operators. Does NOT rule out all
  self-adjoint approaches. The Connes programme and Yakaboylu's construction are not
  affected since they don't use this kernel class.
- **Relevance for us:** Low. Our operator is not in this class.

### 4B. De Bruijn--Newman Constant
- **Rodgers--Tao (2020):** Lambda >= 0 proven. Combined with RH <=> Lambda <= 0, this means
  RH is equivalent to Lambda = 0 exactly. "If true, it's only barely so."
- **Polymath upper bound:** Lambda <= 0.22 unconditionally.
- **Implication:** No room for deformation. Any proof must be exact, not perturbative.

---

## 5. MOMENT PROBLEM / HAMBURGER-CARLEMAN APPROACH

- **Finding:** No published work connecting the Hamburger moment problem or Carleman's
  condition directly to Riemann zeros spectral realisation was found (2020--2026).
- **Assessment:** This appears to be an *unexplored* direction. If our operator has a
  discrete spectrum with known moments, the Carleman condition could provide an independent
  route to proving the moment sequence is determinate, hence the operator essentially
  self-adjoint. This is a potential novelty for our approach.

---

## 6. GEL'FAND TRIPLE / NUCLEAR RIGGING

- **Finding:** A 2024 paper on "Quasi Gelfand Triples" (Integral Equations and Operator
  Theory, 2024) generalises the standard Gel'fand triple by dropping continuous embedding
  in favour of closed embedding of a dense subspace.
  [arXiv:2301.04610](https://arxiv.org/abs/2301.04610)
- **No direct application** to Riemann zeros found in the literature.
- **Assessment:** The nuclear rigging approach appears to be *our unique contribution*.
  No one else is using Gel'fand triples for spectral realisation of zeta zeros.

---

## 7. OVERALL LANDSCAPE ASSESSMENT

### What has NOT been done (gaps we can fill):
1. **No one has a complete spectral realisation.** Connes is closest but still lacks
   convergence proof for the Euler product limit.
2. **No one is using gradient flow / heat kernel methods** for the spectral problem.
3. **No one is using Gel'fand triples / nuclear rigging** for this problem.
4. **No one has connected the Hamburger moment problem** to zeta zero spectral realisation.
5. **No one has a KK-geometric origin** for their operator.

### What HAS been done (we must be compatible with):
1. Connes' trace formula framework is the gold standard. Any new construction must reduce
   to it or be demonstrably equivalent.
2. Yakaboylu's W >= 0 positivity condition is an elegant reformulation. If we can prove
   this independently, we get RH through his machinery.
3. The de Bruijn--Newman Lambda = 0 result means our construction must be non-perturbative.
4. The spectral-dimension obstruction rules out certain kernel classes (but not ours).

### Compatibility with Integers/CBB framework:
- Connes' Arakelov/Spec Z Riemann-Roch is the most compatible with algebraic structures.
- Yakaboylu's Berry-Keating + Bessel operator could interface with KK modes.
- LeClair's scattering-with-impurities maps naturally to KK impurity picture.
- The prolate wave operator / Sonin space framework is less obviously compatible but
  could provide UV control.

---

## 8. BOTTOM LINE

**No breakthrough closes spectral realisation as of April 2026.** The Connes programme
has made significant structural advances (Riemann-Roch for Spec Z, prolate wave operators,
zeta spectral triples with numerical convergence) but the convergence proof remains open.
Yakaboylu's reformulation as W >= 0 positivity is the cleanest new tool. The field is
wide open for a construction that combines geometric origin (KK), analytic control
(heat kernel / gradient flow), and the right functional-analytic framework (nuclear rigging).
This is exactly what Paper 13 proposes to do.
