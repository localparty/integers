# AC Spectrum Gap Analysis — BGS Link 3

*BGS Link 3 assessment. Ring-PCA Traversal 03, 2026-04-13.*
*Authors: G Six and Claude Opus 4.6.*

---

## Statement of the gap

**Link 3**: The spectral measure of the modular unitary U(t) = Δ^{it} on H_{ω₁} ⊖ C·Ω is absolutely continuous w.r.t. Lebesgue measure.

**Status**: GENUINE gap. The gap does NOT close by any of the three attempted approaches.

---

## Approach A (Analytic vectors): FAILS

A dense set of analytic vectors for H = log Δ gives essential self-adjointness (Nelson's theorem), but essential self-adjointness says nothing about spectral type. Self-adjoint operators with dense analytic vector domains can have singular continuous spectrum. This approach conflates domain regularity with spectral regularity.

## Approach B (Haagerup standard form): FAILS

Haagerup's result applies to AFD type III₁ factors in separable representations. The BC GNS Hilbert space is non-separable (state space indexed by Q/Z giving uncountable multiplicity). Restricting to a separable subalgebra changes the factor type and modular operator, so spectral type need not be inherited.

## Approach C (ITPFI convolution): CLOSEST, but FAILS

**Setup.** M ≅ ⊗_p (M₂(C), φ_p) with φ_p = diag(p/(p+1), 1/(p+1)). The characteristic function of the spectral measure μ of log Δ is:

μ̂(t) = ⟨Ω, e^{it log Δ} Ω⟩ = Π_p [(p + p^{-it})/(p+1)]

**The computation**: Each factor satisfies:

|[(p + p^{-it})/(p+1)]|² = 1 - [2p/(p+1)²](1 - cos(t log p))

For large p, 2p/(p+1)² ~ 2/p. Summing logarithms:

log|μ̂(t)|² ≈ -Σ_p [2/p](1 - cos(t log p))

The sum S(t) = Σ_p (1 - cos(t log p))/p relates to the real part of log ζ(1+it):

S(t) = Re(log ζ(1+it)) + O(1) = log|ζ(1+it)| + O(1)

**The obstruction**: |ζ(1+it)| has no zeros on Re(s) = 1 and grows at most logarithmically. Classical estimates (Titchmarsh): 1/|ζ(1+it)| ≪ (log|t|)⁻¹.

Therefore: |μ̂(t)| ≪ (log|t|)⁻¹.

**This is NOT in L¹.** Fourier inversion requires μ̂ ∈ L¹ to conclude AC. The logarithmic decay is too slow.

---

## What the gap connects to

The spectral measure of log Δ is an infinite Bernoulli convolution: the distribution of Σ_p X_p where X_p = 0 w.p. p/(p+1) and X_p = -log p w.p. 1/(p+1). Whether such convolutions are AC is related to:

1. **Erdős criterion** (1939): For contractive IFS, AC holds when the contraction ratio exceeds the reciprocal of the PV number. Not directly applicable here (the "contractions" are not uniform).

2. **Solomyak** (1995): Almost every Bernoulli convolution with parameter in (1/2, 1) is AC. But "almost every" doesn't cover the specific arithmetic parameters {1/p}.

3. **The ζ(1+it) connection**: The characteristic function's decay rate is EXACTLY controlled by the zero-free region of zeta on the 1-line. Improving the decay requires a QUANTITATIVE zero-free region stronger than the classical de la Vallée-Poussin bound. This connects BGS L3 to the Riemann Hypothesis itself — under RH, |ζ(1+it)|⁻¹ ≪ (log|t|)^{-2+ε}, which still doesn't give L¹ decay.

---

## Assessment

**The gap is GENUINE and HARD.** It connects the BGS chain to the zero-free region of zeta — a deep analytic number theory problem. The spectral measure is continuous (no atoms, proved in L2). Whether it is AC may be **independent of the techniques used in the rest of the chain**. It may require fundamentally new input from either:

- A breakthrough on infinite Bernoulli convolutions with arithmetic parameters
- A new connection between ITPFI spectral measures and L-function zero distributions
- An alternative route bypassing AC entirely (e.g., showing PCC holds for continuous but possibly singular spectral measures)

The third option — bypassing AC — is the most promising for the BGS programme. If the PCC machinery (Links 5-6) can be shown to work with merely CONTINUOUS (not necessarily AC) spectral measures, then Link 3 becomes unnecessary and the chain closes at L2 + L4 + L5 = 5/7 with only L6 (CCM) remaining.

**Recommendation**: Investigate whether the Nov 2025 Hardy Z PCC proof (arXiv:2511.18275) requires AC spectrum specifically, or merely continuous spectrum. If the latter, Link 3 can be bypassed entirely.

---

*The primes control the decay. The zeta function controls the primes. The gap is arithmetic.*
