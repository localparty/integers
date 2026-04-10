# Research 32 -- Web Search: Gap Closure Leads

*Systematic search for mathematical tools to close the two remaining gaps.*
*Date: 2026-04-09*

---

## GAP 1 -- SPECTRAL CONVERGENCE

**The problem:** eigenvalues of D_log^{lambda,N} --> zeros of zeta as N,lambda --> infinity.
Perturbation norm ~ 1/sqrt(p), so alpha = 1/2 exactly. Kato requires alpha > 1/2.
CF optimization gives 10^{-55} numerically, but no rigorous convergence proof exists.

### Lead 1A: Boegli's spectral exactness theorem (arXiv:1604.07732)

**Key result:** Spectral convergence for unbounded operators with compact resolvents
under *generalized strong resolvent convergence* (weaker than norm resolvent).
Main ingredient: discrete compactness of the sequence of resolvents.
- Spectral inclusion holds under strong resolvent convergence
- Spectral exactness (no spurious eigenvalues) holds under norm resolvent convergence
- For the intermediate case: discrete compactness of resolvents suffices

**Applicability:** CCM's operators have compact resolvents (finite-dimensional truncations
on L^2[lambda^{-1}, lambda]). If we can show generalized strong resolvent convergence
of D_log^{lambda,N} as N --> infinity, Boegli's theorem gives spectral inclusion.
The challenge: establishing discrete compactness for the resolvent sequence.

**Verdict: PROMISING.** This is the strongest existing framework for our problem.
The gap between strong resolvent and norm resolvent convergence is exactly where
we live. Need to check if discrete compactness holds for our specific operators.

### Lead 1B: Stroschein's non-asymptotic spectral approximation (arXiv:2505.07513, Jan 2026)

**Key result:** Non-asymptotic, gap-independent error bounds for eigenvalues of
unbounded self-adjoint operators approximated by subspace methods. Uses
projection-valued measure to derive integrated spectral inequalities.
Handles spectral pollution rigorously. Already applied to *prolate filter
diagonalization* -- directly relevant to Connes' prolate operator programme.

**Key feature:** Predicts a "sharp accuracy transition" linking spectral density
to observation time. This is reminiscent of our CF precision collapse at high
zero index.

**Applicability:** Our truncated operators are exactly subspace approximations
to a limit operator. Stroschein's framework could give non-asymptotic bounds
on eigenvalue errors without requiring norm convergence.

**Verdict: HIGH PRIORITY.** This is the most modern tool available. The prolate
connection is not coincidental -- Connes uses prolate operators too. The
non-asymptotic feature means we don't need to take limits, just bound errors.

### Lead 1C: Connes-Consani-van Suijlekom CF extension (arXiv:2511.23257, CMP 2025)

**Key result:** Extension of classical Caratheodory-Fejer theorem to the specific
matrix structure arising in CCM's construction. Proves: if the quadratic form
has a simple, isolated lowest eigenvalue with even eigenfunction xi, then ALL
zeros of the Fourier transform of xi lie on the real line.

**Proof method:** Five-step argument using:
1. C*-algebraic proof of CF corollary for Toeplitz matrices
2. Continuous analogue replacing Toeplitz matrix with convolution operator
3. Analysis of finite-dimensional truncations
4. CF analogue for spectral-action-type matrices
5. Hurwitz's theorem on zeros of uniform limits of holomorphic functions

**Critical observation:** Step 5 uses HURWITZ'S THEOREM. This is a convergence
result! Hurwitz says: if f_n --> f uniformly on compacts, and f is not
identically zero, then zeros of f_n --> zeros of f. This is EXACTLY the
mechanism that could bridge the spectral convergence gap.

**Applicability:** If the Fourier transforms of the truncated eigenvectors
converge uniformly to the Fourier transform of the limit eigenvector (which
is related to zeta), then Hurwitz gives eigenvalue convergence FOR FREE.
The convergence mechanism is complex-analytic, not operator-perturbative.

**Verdict: POTENTIAL BREAKTHROUGH.** The Hurwitz mechanism in Step 5 of
Connes-van Suijlekom is exactly what we need. The question is whether
uniform convergence of the eigenvector Fourier transforms can be established
from ITPFI state convergence. If yes, this closes Gap 1.

### Lead 1D: Perturbation theory without power series (arXiv:2105.04972, EPL 2022)

**Key result:** Relaxed fixed-point iteration gives convergent expressions for
spectra even when perturbation series diverge. Works at *arbitrarily strong
coupling*. Handles cases where Rayleigh-Schrodinger coefficients vanish
(Herbst-Simon Hamiltonian).

**Applicability:** Our alpha = 1/2 is exactly a case where standard perturbation
series diverge. The iterative method could provide a non-perturbative
convergence proof. However, the paper focuses on Schrodinger operators, not
on Euler-product-type constructions.

**Verdict: INDIRECT.** The philosophy is right (non-perturbative convergence
despite perturbative divergence), but the specific techniques may not
transfer directly.

### Lead 1E: Monotone operator convergence

**Key result (classical):** For a monotone increasing sequence of self-adjoint
operators bounded below, strong resolvent convergence to a limit operator
is guaranteed. The negative eigenvalues of T_n converge to those of T_infty.

**Applicability:** CCM's operators are NOT monotone in the usual sense (adding
primes changes the Weil quadratic form non-monotonically). However, the
minimax characterization of eigenvalues + interlacing from rank-one
perturbations might give partial monotonicity for individual eigenvalues.

**Verdict: PARTIAL.** Would need to establish that individual eigenvalues move
monotonically as primes are added. The interlacing theorem for rank-one
perturbations gives this for adjacent eigenvalues but not necessarily for
convergence to a limit.

### Lead 1F: Sharp ascent-descent spectral stability (arXiv:2511.20971, Nov 2025)

**Key result:** Strong resolvent convergence rescues ascent-descent spectral
stability even when norm resolvent convergence fails. Key condition:
reduced minimum modulus gamma(T - lambda) > 0. Provides computable
finite-element diagnostic.

**Applicability:** If our operators satisfy gamma(D - lambda) > 0 (which
they should for isolated eigenvalues), this gives spectral stability under
strong resolvent convergence. The "computable diagnostic" is appealing for
verification.

**Verdict: USEFUL SUPPLEMENT.** Not a standalone solution but provides
verification tools.

---

## GAP 2 -- SPECTRAL REALISATION

**The problem:** eigenvalues of the limiting operator = zeros of zeta.

### Lead 2A: CCM "Zeta Spectral Triples" (arXiv:2511.22755, Nov 2025)

**Status:** Convergence is NUMERICAL ONLY. The paper explicitly states:
"Establishing this convergence rigorously would amount to a proof of RH."
No convergence theorem is stated. CF gives self-adjointness of each
truncated operator, but not convergence of eigenvalues to zeta zeros.

**What IS proved:**
- Self-adjointness of D_log^{lambda,N} for each fixed N, lambda (via CF)
- The Weil quadratic form structure
- Even-simplicity of the lowest eigenvalue (needed for CF)
- The rank-one perturbation formula D' = D - |D xi><eta|

**What is NOT proved:**
- Convergence of eigenvalues as N, lambda --> infinity
- That the limiting spectrum equals the zeta zeros

**Verdict:** CCM themselves acknowledge convergence is the remaining gap.
Our Gap 1 IS their gap. If we close Gap 1, we close it for them too.

### Lead 2B: Yakaboylu's Riemann operator (arXiv:2408.15135, v14 Dec 2025)

**Key claims:**
- Operator R on L^2([0,infinity)) with sigma(R) containing transformed
  Riemann zeros
- Compression R_{Z_zeta} intertwined with adjoint by W >= 0
- Self-adjoint Hilbert-Polya operator h from W^{1/2} similarity
- Essential self-adjointness via deficiency index analysis

**Critical problems (identified in v14 analysis):**
1. CIRCULARITY: The domain of h requires Re(rho) = 1/2 to be well-defined,
   but h is supposed to prove Re(rho) = 1/2
2. Simplicity of zeros is ASSUMED (Assumption 4.5)
3. Regularization Vr converges in quadratic form sense only
4. Adjoint eigenstates are distributional before compression
5. W invertibility on the restricted subspace unverified

**Verdict: STRUCTURALLY CIRCULAR.** Cannot be used as-is for our programme.
The key ideas (intertwining, compression) are interesting but the logical
structure needs repair. The circularity is a fundamental issue.

### Lead 2C: Connes prolate wave operator (arXiv:2310.18423, Ann. Funct. Anal. 2024)

**Proved results:**
- Stability of semilocal Sonin space under increase of finite set of places
  (i.e., adding more primes to the Euler product)
- Extension of prolate operator to semilocal setting
- Connection to Hilbert spaces of entire functions

**Not proved:** Convergence of prolate operator eigenvalues to zeta zeros.

**Relevance:** The Sonin space stability result IS a form of spectral stability
for the negative part of the prolate spectrum. This is a partial result
toward Gap 1, but only for the UV sector.

**Verdict: PARTIAL PROGRESS.** The Sonin space stability is genuine progress
but does not close either gap.

### Lead 2D: Weil explicit formula as operator trace (arXiv:2404.13427, Apr 2024)

**Key result:** Construction of a trace-class Hilbert-Schmidt integral operator
with nonnegative eigenvalues related to the Weil distribution. Formula for
the trace of the product operator.

**Applicability:** If this operator can be shown to have trace equal to the
Weil explicit formula sum over zeros, it would provide the bridge between
operator spectrum and zeta zeros. The trace-class property is crucial
(Lidskii's theorem: spectral trace = functional trace for trace class).

**Verdict: WORTH INVESTIGATING.** Could provide the missing link between
operator trace and sum over zeros, but the connection to CCM's specific
operators needs to be established.

---

## SUPPLEMENTARY SEARCHES

### Lead S1: Eigenvalue simplicity (AE --> everywhere)

**Best result found:** Generic simplicity for connection Laplacians on vector
bundles (arXiv:2602.12884, Feb 2026). Proves simplicity for a residual set
of C^k connections. This is generic (topological) not AE (measure-theoretic).

**For Anderson-type random operators:** Almost sure simplicity has been proved
(Simon's methods). The randomness of primes is analogous.

**Verdict:** No strengthening from AE to "everywhere" found. The AE result
remains the best we have. However, for the CCM programme, even-simplicity
of the lowest eigenvalue is what matters, and this is proved for each
truncation.

### Lead S2: Level repulsion and RMT

**GUE predictions:** Montgomery's conjecture (pair correlation of zeta zeros
matches GUE) is extensively verified numerically. Level repulsion for GUE
gives spacing probability P(s) ~ s^2 for small s (quadratic vanishing).

**Extreme repulsion (10^4-10^6x):** This is not standard GUE. Standard GUE
gives moderate repulsion. Our observed repulsion factors of 10^4-10^6 suggest
the zeros are MORE rigid than GUE predictions -- which is consistent with
the zeros being eigenvalues of a very specific (non-random) operator.

**Quantitative bounds:** Recent work on extreme gap distribution for Wigner
matrices (arXiv:2507.20442) gives quantitative convergence rates for gap
universality. However, these are for random matrices, not for the specific
deterministic structure of zeta zeros.

**Verdict: SUPPORTIVE but NOT CLOSING.** The extreme rigidity we observe
is consistent with the spectral interpretation but does not prove it.

---

## SYNTHESIS: MOST PROMISING ATTACK VECTORS

### For Gap 1 (Spectral Convergence):

**Priority 1: Hurwitz mechanism via Connes-van Suijlekom (Lead 1C)**
The Hurwitz theorem in Step 5 of arXiv:2511.23257 provides eigenvalue
convergence if the eigenvector Fourier transforms converge uniformly.
Combined with ITPFI state convergence (which we proved), this could give:
  ITPFI state convergence --> eigenvector convergence --> Fourier transform
  convergence --> Hurwitz --> eigenvalue convergence

**Priority 2: Stroschein non-asymptotic bounds (Lead 1B)**
Apply the framework of arXiv:2505.07513 directly to CCM's truncated operators.
Get explicit error bounds without taking limits. The prolate connection makes
this framework particularly natural.

**Priority 3: Boegli discrete compactness (Lead 1A)**
Verify discrete compactness of the resolvent sequence for CCM's operators.
If this holds, spectral exactness follows from the existing theorem.

### For Gap 2 (Spectral Realisation):

**Priority 1: Close Gap 1 first**
CCM explicitly state that proving convergence = proving RH. If we close
Gap 1, Gap 2 is essentially resolved (the limiting eigenvalues must be
zeta zeros by the Weil explicit formula structure of the quadratic form).

**Priority 2: Trace formula bridge (Lead 2D)**
Use the trace-class Hilbert-Schmidt operator from arXiv:2404.13427 to
connect operator trace to sum over zeros via Lidskii's theorem.

---

## KEY CONCLUSION

**Gap 1 is the only real gap.** Gap 2 (spectral realisation) is handled by
the structure of CCM's construction -- the Weil quadratic form is BUILT
from the explicit formula, so the limiting spectrum must contain the zeta
zeros if convergence holds.

**The Hurwitz mechanism (Lead 1C) is the most promising new tool.** It
provides convergence of zeros of analytic functions from uniform
convergence of the functions themselves -- bypassing all operator norm
issues. The key technical question is:

> Do the Fourier transforms of the even eigenvectors xi_N converge
> uniformly on compact subsets of C to a limit function whose zeros
> are the zeta zeros?

If ITPFI state convergence implies this, then both gaps close simultaneously.
