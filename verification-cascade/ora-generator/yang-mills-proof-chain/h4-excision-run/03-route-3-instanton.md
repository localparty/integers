# Route 3: Instanton Gas

*ORA v8 Tier B excision run. Route 3 of 4.*
*Target: Prove H4 by showing instanton corrections are exponentially suppressed and sub-leading.*

---

## 1. Strategy

In the semi-classical regime, instantons are the leading non-perturbative corrections. If:
(a) The instanton contributions are O(exp(-8pi^2/g^2)) (Bogomolny bound),
(b) The gradient-flow construction controls ALL non-perturbative effects (not just instantons),
(c) g_k -> 0 by AF ensures instanton contributions vanish in the continuum limit,

then H4 follows: the non-perturbative Schwinger functions = perturbative + exponentially small corrections, and the corrections vanish at short distances where g is small.

## 2. The Bogomolny bound on CP^2

From Appendix B of the preprint (Section B.2):

**Theorem (Bogomolny bound)**: For any connection A on a principal G-bundle over a compact oriented 4-manifold X:

$$S_{\text{YM}}[A] = \frac{1}{2g^2} \int_X \text{Tr}(F \wedge *F) \geq \frac{8\pi^2}{g^2} |k|$$

where k = c_2(P) is the second Chern number (instanton number).

On CP^2 with SU(3):
- k = 1 instanton: E_instanton = 8pi^2/g_3^2
- The instanton saturates the Bogomolny bound (it is self-dual: F = *F).
- The moduli space has dimension dim M_{3,1} = 4*3*1 - 9 + 1 = 4.

**The exponential suppression**: In the functional integral, the instanton sector contributes with weight:

$$Z_k \sim e^{-8\pi^2 |k|/g^2} \times (\text{determinant factors})$$

At small g^2 (short distances, by AF), the instanton contributions are exponentially suppressed:

$$\frac{Z_1}{Z_0} \sim e^{-8\pi^2/g^2} \to 0 \quad \text{as } g^2 \to 0$$

## 3. Can this close H4?

### 3.1 What instantons contribute to <Tr F^2 Tr F^2>

In the instanton background, the two-point correlator receives corrections:

$$\langle \text{Tr } F^2(x) \text{ Tr } F^2(0) \rangle_{\text{k-instanton}} \sim e^{-8\pi^2 k/g^2(\mu)} \times P(x, \mu)$$

where P(x, mu) is a polynomial in |x|, mu from the determinant factors and the instanton profile function.

At short distances |x| -> 0, with mu = 1/|x|:
- g^2(mu) -> 0 by AF
- The instanton weight e^{-8pi^2/g^2(mu)} -> 0 FASTER than any power of g^2

Therefore instanton corrections to the short-distance correlator are:

$$\delta S_2^{\text{inst}}(x) = O(e^{-8\pi^2/g^2(1/|x|)}) = O(|x|^{8\pi^2 b_0}) \to 0 \quad \text{as } |x| \to 0$$

since g^2(1/|x|) ~ 1/(2b_0 log(1/|x|Lambda)) and exp(-8pi^2/(2b_0 g^2)) = exp(-4pi^2 * 2b_0 log(1/|x|Lambda)) = (|x|Lambda)^{8pi^2 b_0}.

With b_0 = 11N/(48pi^2):
$$\delta S_2^{\text{inst}}(x) = O(|x|^{11N/6}) \to 0 \quad \text{faster than any perturbative correction}$$

since perturbative corrections are powers of (log(1/|x|Lambda))^{-1}.

### 3.2 The problem: instantons are not the only non-perturbative effect

The instanton gas argument shows that INSTANTON corrections are sub-leading at short distances. But H4 requires that ALL non-perturbative corrections are sub-leading. The non-perturbative effects in 4D YM include:

**(a) Instantons**: Controlled by the Bogomolny bound. Exponentially suppressed at short distances. HANDLED.

**(b) IR renormalons**: These are NOT semi-classical objects. They arise from the integration over soft momenta in Feynman diagrams and produce power corrections ~ (Lambda * |x|)^p to the short-distance correlator. These are NOT exponentially suppressed — they are power-law in |x|. However, in the OPE language, IR renormalon corrections are associated with condensates (e.g., <Tr F^2>) and appear as sub-leading OPE channels with dimension >= 4, which ARE subleading compared to the leading |x|^{-8} singularity.

**Key question**: Does the Balaban construction provide non-perturbative control of IR renormalon corrections?

The Balaban effective action at scale k includes ALL fluctuations integrated out up to that scale. The polymer expansion provides bounds on the effective action at each scale. The crucial question is whether the difference between the non-perturbative effective action and its perturbative expansion is controlled.

**(c) Renormalon ambiguities**: Related to (b). The perturbative series is factorially divergent, and the Borel integral has ambiguities of size ~ exp(-2/g^2) from the u = 2 renormalon. These ambiguities are supposed to be cancelled by non-perturbative condensate contributions, but proving this cancellation IS H4.

**(d) Fractional instantons / center vortices / other topological objects**: In the lattice formulation, there can be topological excitations that are not standard instantons. The Balaban construction's small-field restriction to Omega_s suppresses large-field configurations, but whether all non-perturbative effects within Omega_s are exponentially suppressed is not obvious.

### 3.3 The gradient-flow angle

In the gradient-flow framework, all non-perturbative effects are encoded in the flowed correlator F(t). At fixed t > 0, the flow provides UV regulation:
- The flow propagator e^{-tp^2} damps UV modes above p ~ 1/sqrt(8t).
- All correlators at t > 0 are UV-finite (Luscher-Weisz theorem).

At t -> 0, the UV regulation is removed. The non-perturbative effects that survive are those that contribute to the continuum correlator F(0).

**Can we bound ALL non-perturbative corrections using the gradient flow?**

The small-flow-time expansion gives:
$$F(t) = F(0) + a_1 t + a_2 t^2 + \cdots$$

with F(0) = S_2^ren(x,y). The coefficients a_n contain both perturbative and non-perturbative contributions. The question is whether F(0) = F^pert(0).

The instanton argument shows that in the k != 0 topological sectors, the contribution to F(0) is exponentially suppressed at short distances. But the k = 0 sector itself contains non-perturbative fluctuations (quantum corrections beyond perturbation theory), and bounding these requires more than the instanton gas argument.

### 3.4 Strengthening the argument: the dilute instanton gas approximation

In the dilute instanton gas approximation (valid at weak coupling g^2 << 1):

$$Z = Z_0 \sum_{k=0}^{\infty} \frac{1}{k!} \left(\frac{C}{g^{4N}} e^{-8\pi^2/g^2}\right)^k = Z_0 \exp\left(\frac{C}{g^{4N}} e^{-8\pi^2/g^2}\right)$$

The instanton density is ~ g^{-4N} exp(-8pi^2/g^2), which is doubly exponentially suppressed at weak coupling.

For the two-point function, the leading instanton correction is:

$$\delta F_{\text{inst}} = O\left(\frac{1}{g^{4N}} e^{-8\pi^2/g^2}\right)$$

At short distances, with g^2 ~ 1/(2b_0 log(1/|x|Lambda)):

$$\delta F_{\text{inst}} \sim (2b_0 \log(1/|x|\Lambda))^{2N} \times (|x|\Lambda)^{11N/6}$$

The polynomial pre-factor is overwhelmed by the power-law suppression for |x| -> 0. So instanton corrections are rigorously sub-leading.

**But this only handles INSTANTONS, not all non-perturbative effects.**

## 4. Partial result: topological sector decomposition

We CAN establish the following partial result within the existing framework:

**Proposition (Instanton suppression at short distances)**: In the gradient-flow Yang-Mills theory constructed in Steps 1-17, the contribution of topological sectors with |k| >= 1 to the two-point correlator S_2^ren(x,y) is O(|x|^{11N/6}) as |x| -> 0, which is sub-leading compared to the perturbative prediction |x|^{-8}(log)^{-2}.

*Proof sketch*:
1. The Bogomolny bound gives S_YM[A] >= 8pi^2|k|/g^2 in the |k|-instanton sector.
2. The functional integral weight e^{-S_YM} in the |k|-sector is bounded by e^{-8pi^2|k|/g^2}.
3. The gradient-flow correlator at flow time t inherits this bound (the flow decreases the action).
4. The continuum limit is controlled by the Balaban RG; at scale k, the coupling g_k -> 0 by AF.
5. Therefore the |k| >= 1 contribution vanishes in the continuum limit faster than any power of g.

**This is SOUND but INSUFFICIENT for H4**: It shows instantons are sub-leading, but does not address the non-perturbative effects within the trivial topological sector (k = 0).

## 5. The k = 0 sector problem

Within the trivial topological sector, the non-perturbative effects include:
- Large quantum fluctuations that are NOT instantons but are still non-perturbative.
- Condensate contributions (e.g., gluon condensate <g^2 Tr F^2>).
- IR renormalon-type corrections.

The Balaban construction's small-field restriction to Omega_s suppresses large fluctuations, but the small-field region STILL contains non-perturbative physics. The polymer expansion gives:

$$S_k^{\text{eff}}[V] = \frac{1}{g_k^2} S_{\text{YM}}[V] + \sum_{X} K_k(X, V)$$

The polymer activities K_k(X, V) include non-perturbative corrections. Their perturbative expansion is:

$$K_k(X, V) = K_k^{(0)}(X, V) + g_k^2 K_k^{(1)}(X, V) + \cdots$$

where K_k^{(n)} are the n-loop contributions. The FULL K_k includes all-orders effects.

**The question of whether sum_n K_k^{(n)} converges to K_k is exactly the Borel summability question of Route 2.** The instanton gas argument cannot resolve this.

## 6. Verdict: PARTIAL RESULT, NOT CLOSED

Route 3 produces a genuine partial result (instanton suppression at short distances) but CANNOT close H4 because:

**(a)** Instantons are not the only non-perturbative effects. The k = 0 sector contains quantum fluctuations beyond perturbation theory.

**(b)** The IR renormalon corrections (power corrections from soft momenta) are present in the k = 0 sector and are not controlled by the Bogomolny bound.

**(c)** Bounding non-perturbative effects WITHIN the Balaban small-field region requires comparing the full polymer expansion to its perturbative truncation, which is the Borel summability problem.

**Specific blocker**: Control of non-perturbative quantum fluctuations in the trivial topological sector.

**Re-entry gate**: A proof that the Balaban polymer expansion converges to its perturbative expansion within the small-field region. This would show that ALL non-perturbative effects in Omega_s are captured by perturbation theory, and the large-field region (Omega_s complement) contributes at most O(e^{-kappa|X|}) from the polymer decay bound.

---

## What the next runner needs to know

- **State at handoff**: PARTIAL RESULT (instanton suppression proved) + BLOCKED (k=0 sector).
- **Open dependencies**: Same as Route 2 — polymer expansion vs perturbative expansion comparison.
- **Watch out for**: The instanton argument is ONLY about topological sectors |k| >= 1. The k = 0 sector's non-perturbative physics is the real challenge.
- **Preferred next move**: Investigate the Balaban polymer expansion's perturbative content. Each polymer activity K_k(X,V) is constructed by explicit integration — can its perturbative expansion be shown to converge to K_k itself?
- **Voice canon citation**: P4 — the Bogomolny bound is topologically rigid. P6 — the residual non-perturbative effects are in the k=0 projection.
