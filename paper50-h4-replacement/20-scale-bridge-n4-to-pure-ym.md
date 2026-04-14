# §20 — The Scale Bridge: N=4 SYM → Pure YM

*The critical step of Route C. Pure YM as a limit of N=4 SYM. Decoupling extended supersymmetry. Paper 10's scheme independence theorems as the rigorous control. What can be rigorously taken; what cannot yet.*

---

## 20.1. The problem

Kapustin-Witten 2007 (§18) produces geometric Langlands from *N=4* super Yang-Mills, the maximally supersymmetric gauge theory. Gaitsgory-Raskin 2024 (§19) proved geometric Langlands on a smooth projective curve.

But H4 is a statement about *pure* Yang-Mills on $\mathbb{R}^4$ — a theory with no supersymmetry and no matter fields, only the gauge connection $A$ and the field strength $F$.

N=4 SYM $\neq$ pure YM. The *scale bridge* is the procedure that identifies pure YM as an appropriate limit of N=4 SYM.

If the scale bridge is rigorous, Route C closes: the proved geometric Langlands correspondence of Gaitsgory-Raskin applies to the Kapustin-Witten twist of N=4 SYM, and the scale bridge descends this to pure YM, whose Wilson-loop L-function inherits the Langlands-type functional equation and spectral structure needed for H4.

If the scale bridge is not rigorous, Route C stalls, and Route B's Ob.3 and Ob.4 (which Route C was supposed to resolve, §17.5) remain open.

This section addresses: what the scale bridge requires, what can be rigorously taken today, and what cannot.

---

## 20.2. Two directions of decoupling

Pure YM is obtained from N=4 SYM by *decoupling* the extra fields:

**Matter decoupling.** N=4 SYM has 6 scalar fields $\phi^I$ and 4 fermions $\lambda^a$ in the adjoint representation. Pure YM has no matter. Decoupling requires giving mass to the matter fields and taking the mass to infinity.

**Supersymmetry breaking.** N=4 SYM has 16 supercharges. Pure YM has 0 supercharges. All supersymmetry must be broken.

Both decouplings are *soft* in the standard gauge-theory sense: they are achieved by adding mass terms to the Lagrangian and taking the mass parameter to infinity while holding the gauge coupling $g$ fixed.

---

## 20.3. The soft breaking route

Consider N=4 SYM with a mass deformation:
$$S_{N=4^*} = S_{N=4} + \int d^4 x \, \text{Tr}\left(\sum_I M_I^2 (\phi^I)^2 + \sum_a m_a \bar\lambda^a \lambda^a\right).$$

The theory with non-zero mass parameters is called *N = 4$^*$* or *N = 1$^*$* depending on the choice of masses. As $M_I, m_a \to \infty$, the massive fields decouple; at energies $\mu \ll \min(M_I, m_a)$, the effective theory is pure YM (provided the gauge coupling runs appropriately).

**Issue 1:** the decoupling limit is *infrared* (low-energy). The theory at energies $\mu \gg M_I$ is the full N=4 SYM; the theory at $\mu \ll M_I$ is approximately pure YM. In between, there is a transition regime.

**Issue 2:** the gauge coupling $g(\mu)$ runs differently in N=4 SYM (where $\beta = 0$ to all orders — N=4 is finite) and in pure YM (where $\beta_0 = -\frac{11 N}{3}$ for SU(N), asymptotically free). The transition at $\mu \sim M_I$ is where the coupling begins running: at $\mu > M_I$, it is approximately constant (N=4 behaviour); at $\mu < M_I$, it runs with the pure-YM beta function.

**Issue 3:** supersymmetry is broken softly but not cleanly. The massive theory N=4$^*$ is not itself supersymmetric; it is a theory with supersymmetry at high energy and no supersymmetry at low energy.

---

## 20.4. Paper 10 scheme independence as the controlling theorem

Paper 10 (scheme independence of the YM chain) establishes that Paper 8 Link 4's Setup Assumption holds *in any renormalization scheme*. The content: scheme choices (MS vs MOM vs explicit lattice schemes) produce equivalent physics at all orders in $g^2$, with the scheme-dependence captured by well-defined scheme transformations.

**For the scale bridge**, Paper 10's theorem provides the rigorous control on the transition regime:

1. **Running coupling across scales.** Paper 10 shows that $g(\mu)$ is well-defined across all $\mu$ via scheme-invariant combinations. This gives rigorous meaning to "the coupling at scale $\mu$" independently of how one parameterizes the theory.

2. **Matching of UV (N=4) and IR (pure YM) couplings.** At the transition scale $\mu \sim M_I$, the high-energy coupling (constant, $\beta_{N=4} = 0$) must match the low-energy coupling (running, $\beta_{\text{YM}} = -\frac{11 N}{3}$). Paper 10's scheme-invariant machinery ensures the match is well-defined.

3. **Gradient flow on both sides.** Paper 8 Links 15-17 use gradient flow for the pure-YM side. Gradient flow also works for N=4 SYM (and indeed for N=4$^*$). The gradient-flow formalism is scheme-invariant (Paper 10's result), so observables computed via gradient flow in N=4$^*$ at scale $\mu$ match, as $M_I \to \infty$, observables computed via gradient flow in pure YM at the same scale.

Paper 10 is not, by itself, the scale bridge. But it is the *necessary precondition*: without scheme invariance, the N=4 → pure YM limit cannot be formulated rigorously.

---

## 20.5. What can be rigorously taken today

Three pieces of the scale bridge are rigorous (April 2026):

### 20.5.1. Perturbative decoupling

At the perturbative (Feynman-diagram) level, the decoupling limit $M_I \to \infty$ is controlled order-by-order in $g^2$. Each Feynman diagram of N=4$^*$ reduces, in the $M_I \to \infty$ limit, to a Feynman diagram of pure YM plus corrections of order $M_I^{-k}$ for some $k \geq 1$. The corrections vanish.

This is classical gauge-theory computation, well-established since the 1980s.

### 20.5.2. Gradient-flow transfer

Gradient flow (Paper 8 Links 15-17) produces a smooth transition from lattice or perturbative observables to continuum Schwinger functions. For both N=4$^*$ and pure YM, gradient flow is well-defined. The scheme-independence of gradient-flow observables (Paper 10) ensures that, as $M_I \to \infty$, the N=4$^*$ gradient-flow observables converge to the pure-YM ones.

This is *partial* rigour: the perturbative/semi-classical transfer is controlled; the fully non-perturbative transfer requires additional work.

### 20.5.3. Kapustin-Witten twist survival

The Kapustin-Witten twist of N=4 SYM (§18) requires the supersymmetry of N=4 SYM for its construction — the twist uses a specific supercharge $Q_t$. On the deformed theory N=4$^*$, supersymmetry is broken; the twist is no longer well-defined in the strict sense.

However, there is a *soft version*: the twist extends to N=4$^*$ with corrections of order $M_I / g^2$ (or similar scale-dependent factors). At $M_I \ll g^{-2}$, the soft breaking is small, and the twist is *approximately* well-defined. At $M_I \to \infty$, the twist reduces to the pure-YM "topological sector" — which is the set of observables that are controlled by the Hitchin moduli geometry even in the pure-YM limit.

This survival is conjectural but supported by physics-level analyses (Moore, Schweigert, and others, 2010s).

---

## 20.6. What cannot yet be rigorously taken

Three pieces of the scale bridge are *not* rigorous (April 2026):

### 20.6.1. Non-perturbative decoupling

The perturbative decoupling (§20.5.1) is controlled. The *non-perturbative* decoupling — i.e., the claim that non-perturbative Schwinger functions of N=4$^*$ converge to those of pure YM as $M_I \to \infty$ — is not yet rigorous.

The obstruction: non-perturbative effects in gauge theories are notoriously delicate. Instantons, renormalons, and other non-perturbative phenomena change behaviour across scales. The decoupling limit, if it exists, requires control over these effects that is not currently available.

### 20.6.2. Kapustin-Witten twist in the pure-YM limit

The Kapustin-Witten twist requires supersymmetry. In N=4$^*$ (soft-broken), the twist is approximately defined. In pure YM ($M_I = \infty$, no SUSY), the twist does not exist in the strict Kapustin-Witten sense.

There are proposed replacements:
- *Donaldson-Witten twist* (original, 1988): N=2 SYM twisted to give Donaldson invariants. Exists without requiring N=4.
- *Vafa-Witten twist* (1994): N=4 SYM twisted differently, producing Vafa-Witten invariants.
- *Pure-YM analogue* (conjectural): a topological sector of pure YM defined via gradient-flow fixed points, claimed to match the Kapustin-Witten output.

The third item is the Route C target; it is not yet rigorous.

### 20.6.3. Geometric Langlands in the pure-YM limit

Gaitsgory-Raskin 2024 proves geometric Langlands for the full categorical setup on complex curves. The Kapustin-Witten reduction (§18) produces this from N=4 SYM on $M = \Sigma \times C$. In the pure-YM limit, Kapustin-Witten's construction no longer strictly applies, and the descent of geometric Langlands to pure YM is the central open question of Route C.

Physics-level arguments (Nakajima, Gukov, Witten) suggest that *a version* of geometric Langlands survives in pure YM — roughly, the version corresponding to Wilson loops only (without 't Hooft loops) and without the mirror symmetry structure. But this survival is not yet proven.

---

## 20.7. The conjectural scale bridge

Combining §20.5 and §20.6, Route C's conjectural scale bridge is:

**Conjecture (Route C scale bridge).** *For pure YM on $\mathbb{R}^4$, obtained from N=4$^*$ in the limit $M_I \to \infty$, the following hold:*

(i) *Perturbative observables of pure YM are the $M_I \to \infty$ limits of N=4$^*$ perturbative observables.* [PROVED, §20.5.1.]

(ii) *Gradient-flow observables of pure YM are the $M_I \to \infty$ limits of N=4$^*$ gradient-flow observables.* [PARTIALLY PROVED, §20.5.2; perturbative part rigorous, non-perturbative part conjectural.]

(iii) *Wilson-loop observables of pure YM inherit, from N=4$^*$, a "Langlands-like" spectral structure: the Wilson-loop L-function has a functional equation and a Euler product derived from the Kapustin-Witten twist's survival under soft breaking.* [CONJECTURAL, §20.5.3 + §20.6.2.]

(iv) *The geometric Langlands correspondence on curves (Gaitsgory-Raskin 2024) descends to a Wilson-loop-only version on pure YM, providing Satake-matching data for $L_{\text{YM}}$.* [CONJECTURAL, §20.6.3.]

Route C succeeds if the bridge is made rigorous. The critical conjectural pieces are (ii) (non-perturbative part), (iii), and (iv).

---

## 20.8. Programme-internal tools for the scale bridge

The programme's infrastructure contains several tools relevant to the scale bridge:

### 20.8.1. Paper 10 scheme independence

Already discussed (§20.4). Provides the precondition: rigorous comparison across schemes.

### 20.8.2. Paper 11 K.4 (all-orders)

Paper 11 K.4 establishes all-orders scheme-invariance (extending Paper 10 to all loops). This is needed for the perturbative part of the scale bridge at all orders.

### 20.8.3. Paper 8 Links 15-17 (gradient flow)

Gradient flow, used for OS reconstruction in Paper 8, is the tool that converts lattice data to continuum Schwinger functions. It also works for N=4$^*$. The scale-bridge extension is: gradient flow commutes with $M_I \to \infty$.

### 20.8.4. BC/ITPFI factorization (Paper 13)

If the BC/ITPFI factorization of pure YM holds (as conjectured in §15.6 for Route B), then the scale bridge can be checked at the level of local BC factors: the $M_I \to \infty$ limit of $\omega_{\text{N=4}^*}^{(p)}$ should be $\omega_{\text{YM}}^{(p)}$.

### 20.8.5. Paper 10's gradient-flow machinery extended to mass deformations

Paper 10 primarily treats pure YM. Extending it to N=4$^*$ (with mass-deformation fields) requires additional work. This is a natural next step for the programme, not yet done.

---

## 20.9. Alternative scale bridges

Three alternatives to the soft-breaking scale bridge are considered:

### 20.9.1. Dimensional reduction

N=4 SYM in 4D has avatars in lower dimensions (N=8 SYM in 3D, etc.). Dimensional reduction from 4D to 3D produces a different theory. The scale bridge from 3D N=8 SYM to 3D pure YM might be more tractable (there is no asymptotic freedom in 3D, so the IR behaviour is different).

Drawback: the 4D result on pure YM is what we want. 3D results do not directly transfer.

### 20.9.2. Holographic dual

N=4 SYM on $S^3 \times \mathbb{R}$ has a holographic dual (AdS$_5 \times S^5$ string theory). The mass deformation to N=4$^*$ corresponds to a specific deformation on the gravity side. This may provide an alternative rigorous description of the scale bridge, at least for specific quantities.

Drawback: the holographic dual uses string theory, which is itself non-rigorous. Using it in a rigorous argument requires care.

### 20.9.3. Lattice regularization

Put both N=4$^*$ and pure YM on a lattice; take $M_I \to \infty$ at fixed lattice spacing; then take the continuum limit. Lattice implementation of N=4$^*$ is delicate but partial results exist (Catterall et al., various).

This is the most programme-friendly route, but has not been executed.

---

## 20.10. Status and realistic assessment

As of April 2026, the scale bridge is **partially rigorous**:

- Perturbative part: rigorous.
- Gradient-flow part (leading order): rigorous.
- Non-perturbative part: conjectural but with physics-level support.
- Kapustin-Witten twist survival: conjectural.
- Descent of geometric Langlands: conjectural.

Route C's plausibility depends on the conjectural parts closing. The most tractable next step is the non-perturbative gradient-flow transfer, which extends Paper 10's scheme independence to mass deformations.

---

## 20.11. Summary

The scale bridge from N=4 SYM to pure YM is Route C's central obstruction. Via soft supersymmetry breaking (N=4 → N=4$^*$ → pure YM), decoupling of matter fields, and the $M_I \to \infty$ limit, one obtains pure YM as a limit of supersymmetric theory. Paper 10's scheme independence provides the precondition for a rigorous scale bridge. The perturbative and leading gradient-flow parts are rigorous; the non-perturbative and Kapustin-Witten-twist-survival parts are conjectural.

If the scale bridge closes, Route C inherits geometric Langlands (Gaitsgory-Raskin 2024) on pure YM, providing the functional equation of $L_{\text{YM}}$ and the Satake matching for Route B. If the scale bridge does not close, Route C stalls.

The next sections develop: §21 (Elliott-Gwilliam-Williams 2024, BV quantization of KW theories), §22 (short-distance extraction), §23 (Route C proof sketch).

---

*Paper 50 §20. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
