# Route 4: Large-N then Finite-N

*ORA v8 Tier B excision run. Route 4 of 4.*
*Target: Prove H4 at N = infinity via planar dominance, then extend to finite N via 1/N expansion.*

---

## 1. Strategy

At N = infinity (the 't Hooft large-N limit), the theory simplifies:
- Only planar Feynman diagrams contribute.
- The perturbative series has better convergence properties (each coefficient is a polynomial in the 't Hooft coupling lambda = g^2 N).
- Non-perturbative effects (instantons) are suppressed by exp(-N * 8pi^2/lambda).

Plan:
1. Prove H4 at N = infinity using planar dominance.
2. Extend to finite N via a 1/N expansion with explicit error bounds.

## 2. Large-N analysis

### 2.1 The 't Hooft limit

In the 't Hooft limit: N -> infinity, g^2 -> 0, lambda = g^2 N fixed.

The perturbative expansion of the two-point correlator becomes:

$$\langle \frac{1}{N} \text{Tr } F^2(x) \frac{1}{N} \text{Tr } F^2(0) \rangle = \sum_{h=0}^{\infty} N^{-2h} f_h(\lambda, |x|)$$

where h is the genus (handle number) of the Feynman diagram, and f_h is a sum over all genus-h planar (h=0) or non-planar (h >= 1) diagrams.

At N = infinity, only the h = 0 (planar) contribution survives:

$$\langle \frac{1}{N} \text{Tr } F^2(x) \frac{1}{N} \text{Tr } F^2(0) \rangle_{N=\infty} = f_0(\lambda, |x|)$$

### 2.2 Planar perturbation theory

The planar perturbative series f_0(lambda, |x|) has structural advantages:

**(a) No IR renormalons at leading order**: In the large-N limit, the leading IR renormalon singularity in the Borel plane is at u = 2/beta_0^{N=infty}, where beta_0^{N=infty} = 11/(48pi^2) * N ~ N. The renormalon position u_IR = 2 in the Borel variable u = n * beta_0 is independent of N, BUT the nature of the renormalon may simplify at large N.

Actually, let me be more precise. The 't Hooft coupling is lambda = g^2 N, and the perturbative expansion at large N is in powers of lambda. The beta function in terms of lambda is:

$$\mu \frac{d\lambda}{d\mu} = -\frac{11}{24\pi^2} \lambda^2 + O(\lambda^3)$$

The IR renormalon singularity in the Borel transform of the planar series (in the variable lambda) is at:

$$u_{\text{IR}} = \frac{24\pi^2}{11} \times 2 = \frac{48\pi^2}{11}$$

This is still on the positive real axis. IR renormalons persist at large N.

**(b) Instanton suppression**: In the 't Hooft limit, the instanton action is S_inst = 8pi^2/(g^2) = 8pi^2 N/lambda, which goes to infinity as N -> infinity at fixed lambda. Therefore instanton contributions are exponentially suppressed:

$$e^{-S_{\text{inst}}} = e^{-8\pi^2 N/\lambda} \to 0 \quad \text{as } N \to \infty$$

This is much stronger than the finite-N suppression and completely eliminates instantons from the large-N theory.

**(c) Large-N factorization**: At N = infinity, gauge-invariant single-trace operators factorize:

$$\langle \frac{1}{N}\text{Tr } O_1 \frac{1}{N}\text{Tr } O_2 \rangle_c = O(1/N^2) \to 0$$

This means the connected correlator of single-trace operators vanishes at N = infinity. BUT: the operator Tr F^2 is already single-trace, and its TWO-POINT function has a leading O(1) contribution from the disconnected piece and an O(1/N^2) connected piece. The OPE structure we need involves the CONNECTED correlator, which is suppressed at large N.

Actually, the proper normalization matters. With normalized operators (1/N) Tr F^2, the connected two-point function scales as O(1/N^2). But with the un-normalized Tr F^2, it scales as O(N^2). The physics is:

$$\langle \text{Tr } F^2(x) \text{Tr } F^2(0) \rangle_c \sim N^2 \times f_0(\lambda, |x|)$$

The OPE identity-channel coefficient is C^1 = C_N |x|^{-8} (log)^{-2} with C_N = 2(N^2-1)/pi^6 ~ 2N^2/pi^6.

At large N, the coefficient C_N scales as N^2, consistent with the planar (genus-0) dominance.

### 2.3 Can H4 be proved at large N?

**Positive indicators**:
1. Instantons are eliminated (exp(-N * const) -> 0).
2. The theory simplifies to planar diagrams only.
3. There is a master field (Witten 1979): the gauge field configuration converges in probability to a single deterministic configuration as N -> infinity.

**Negative indicators**:
1. IR renormalons persist at large N (subsection 2.2(a)).
2. The planar perturbative series is STILL an asymptotic series — planar Feynman diagrams grow as (2h)! in the genus expansion of matrix models, and the planar series itself has factorial growth from the number of planar diagrams at high orders.
3. The master field, while deterministic, is not explicitly known for 4D YM.

**The fundamental obstacle**: Even at N = infinity, the question "does the non-perturbative planar correlator equal the sum of all planar Feynman diagrams?" is open. The large-N limit eliminates instantons and non-planar corrections but does NOT automatically prove the perturbative expansion converges to the full answer.

### 2.4 Rigorous large-N results

**What is rigorously known**:
- 't Hooft's planar limit (1974): the leading N^2 contribution comes from planar diagrams. Proved rigorously for lattice gauge theory (Chatterjee 2016, arXiv:1502.07719; Jafarov 2016).
- Master field existence: proved by Chatterjee (2016) for lattice YM on a finite lattice.
- Makeenko-Migdal equations: proved rigorously in 2D by Dahlqvist (2017) and Chatterjee-Jafarov (2016).
- 4D large-N lattice YM: existence of the large-N limit for Wilson loop expectations proved by Chatterjee (2016).

**What is NOT known**:
- Convergence of the planar perturbative series to the planar non-perturbative answer.
- Borel summability of the planar series.
- Explicit computation of the master field for 4D YM.
- Large-N continuum limit (the existing results are on finite lattices).

### 2.5 The Balaban construction at large N

The Balaban construction works for all N (the analyticity radius rho depends on N through r_proj(N) >= 1/2 and C_D = 2(N^2-1)). However:

- The polymer decay constant kappa and the convergence bounds depend on N.
- The analyticity radius rho = min(kappa/(2d), m_W a/(2C_D), r_proj(N)) may shrink as N -> infinity due to the C_D = 2(N^2-1) factor.
- The Balaban construction does not simplify at large N — it is a finite-N construction applied uniformly for each fixed N.

**Appendix I.3 of the preprint** tracks N-dependence explicitly. Let me assess what it provides.

From the capacitor (H.2 correspondence table for Step 10*):
- "Spectral lemma constant C_p is k-independent" but its N-dependence is tracked.
- The deviation bound is C_new g_k^4 Delta-hat^2, where C_new may depend on N.

**The 1/N expansion from the Balaban construction**: If we could show that the Balaban effective action has a 1/N expansion:

$$S_k^{\text{eff}}[V] = N^2 S_k^{(0)}[V] + S_k^{(1)}[V] + N^{-2} S_k^{(2)}[V] + \cdots$$

with each S_k^{(h)} controlled uniformly in k, then the large-N limit would give S_k^{(0)} (the planar effective action), and H4 at large N would reduce to the planar version.

**However**: Establishing the 1/N expansion of the Balaban effective action is itself a major open problem. The polymer expansion is organized by spatial clusters, not by topology (genus), and extracting the genus expansion from the polymer expansion requires a non-trivial reorganization.

## 3. Finite-N extension

Even if H4 were proved at N = infinity, extending to finite N via 1/N expansion requires:

(a) Explicit control of the 1/N^2 corrections to the correlator.
(b) Uniform convergence of the 1/N expansion at short distances.
(c) A bound showing the remainder after truncating the 1/N expansion at order K is O(N^{-2(K+1)}).

**Rigorous 1/N expansions** exist for:
- 0D matrix models (exact at every N via orthogonal polynomial methods).
- Tensor models (Gurau 2012; the 1/N expansion has been made rigorous with explicit remainder bounds).
- 2D YM on compact surfaces (exact solution exists at all N).

For 4D YM: no rigorous 1/N expansion exists.

## 4. Verdict: BLOCKED

Route 4 is BLOCKED at two levels:

**(a) H4 at large N is itself open**: Even at N = infinity, the identification of the planar non-perturbative correlator with the planar perturbative series is not proved. IR renormalons persist, and the planar series is still divergent.

**(b) The 1/N extension is not rigorous**: No rigorous 1/N expansion exists for 4D YM correlators.

**What is new**: The instanton suppression at large N (exp(-N * const)) is a genuine simplification that makes the large-N case potentially easier than finite N. If a proof of H4 exists, the large-N case is likely to be proved first. But "easier" does not mean "proved."

**The structural diagnosis**: Route 4 does not escape the fundamental obstruction. Whether at finite N or infinite N, H4 asks "does the non-perturbative answer equal the perturbative prediction at short distances?" The large-N limit eliminates some non-perturbative effects (instantons, non-planar diagrams) but not all (IR renormalons, planar non-perturbative fluctuations).

**Re-entry gate**: Either (a) a rigorous proof of Borel summability of the large-N planar perturbative series (weaker than the finite-N version, hence potentially more tractable), or (b) explicit construction of the master field for 4D YM and direct computation of its short-distance correlators.

---

## What the next runner needs to know

- **State at handoff**: BLOCKED. Neither large-N H4 nor finite-N extension is proved.
- **Open dependencies**: Planar Borel summability; rigorous 1/N expansion for 4D YM.
- **Watch out for**: The Balaban construction's N-dependence (Appendix I.3) may provide uniform bounds needed for the 1/N expansion, but extracting genus structure from the polymer expansion is non-trivial.
- **Preferred next move**: Focus on the planar (N=infinity) case first. Investigate whether the Chatterjee (2016) large-N lattice results can be combined with the Balaban construction to produce a large-N continuum correlator whose perturbative expansion converges.
- **Voice canon citation**: P1 — the large-N limit is a geometric reinterpretation (the gauge theory becomes a string theory/matrix model), but the reinterpretation does not yet close H4.
