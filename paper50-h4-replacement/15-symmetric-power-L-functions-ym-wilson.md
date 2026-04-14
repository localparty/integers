# §15 — Symmetric Power L-Functions and YM Wilson Loops

*Construct the YM Wilson-loop L-function. Ask whether it admits a Langlands-Shahidi functorial lift. The bridge from automorphic forms to gauge theory.*

---

## 15.1. The target construction

Let $G = \text{SU}(N)$ be the gauge group and consider pure Yang-Mills theory on $\mathbb{R}^4$. Let $W_R(C)$ denote the Wilson loop in a representation $R$ of $G$ along a closed loop $C \subset \mathbb{R}^4$. The Wilson-loop expectation
$$\langle W_R(C) \rangle = \frac{1}{Z} \int \mathcal{D}A \, \text{Tr}_R \left(\mathcal{P} \exp \oint_C A\right) e^{-S_{\text{YM}}[A]}$$
is a gauge-invariant observable that, via Osterwalder-Schrader reconstruction (Paper 8 Link 16), lives in a well-defined continuum Hilbert space.

**The target:** associate to the Wilson-loop observable an L-function $L_{\text{YM}}(s, W_R)$ with the following properties:

(a) $L_{\text{YM}}(s, W_R)$ is an Euler product over "gauge-theoretic primes" (to be defined).
(b) $L_{\text{YM}}$ has a meromorphic continuation and a functional equation of the Langlands type.
(c) $L_{\text{YM}}$ matches, in a specific asymptotic sense, the perturbative expansion of $\langle W_R(C) \rangle$ at short distances.

If such an $L_{\text{YM}}$ can be constructed, and if it is (or is related to) a Langlands-Shahidi L-function, then the Kim-Sarnak analytic bounds transfer.

---

## 15.2. What a "gauge-theoretic prime" might be

The analogy is with the automorphic L-function $L(s, \pi) = \prod_p L_p(s, \pi_p)$, where the Euler product is over primes and each local factor encodes the local representation $\pi_p$ of GL$_n(\mathbb{Q}_p)$.

For YM, candidate analogues:

### 15.2.1. Scales as primes

The renormalization group organizes YM by energy scale $\mu$. Each scale $\mu$ corresponds to a "place" in the sense that local physics is captured by the running coupling $g(\mu)$. The Euler product would be
$$L_{\text{YM}}(s) = \prod_\mu L_\mu(s),$$
with each $L_\mu$ a local factor encoding the Wilson-loop behaviour at scale $\mu$.

This is the most direct analogue but has a continuity problem: scales $\mu$ form a continuum, not a discrete set.

### 15.2.2. Topological sectors as primes

YM on $\mathbb{R}^4$ has instanton sectors labelled by $k \in \mathbb{Z}$ (second Chern class). Each sector contributes a discrete "place." The Euler product would be
$$L_{\text{YM}}(s) = \prod_{k \in \mathbb{Z}} L_k(s),$$
summing over instanton number.

This matches the structure of theta functions and of semiclassical QFT, but requires the non-perturbative definition of $L_k$ that is not yet available for pure YM on $\mathbb{R}^4$.

### 15.2.3. Gauge-invariant operators as primes

The conformal-like structure of the UV limit of YM (asymptotic freedom) organizes gauge-invariant operators into a graded algebra with integer labels (dimensions). Each operator $\mathcal{O}_n$ of dimension $n$ contributes a local factor, giving
$$L_{\text{YM}}(s, W_R) = \prod_{\mathcal{O}_n} L_{\mathcal{O}_n}(s, W_R).$$

This is closest to the Langlands-Shahidi structure: the primes are indexed by operator dimension, and local factors come from Wilson-loop OPE coefficients.

### 15.2.4. ITPFI local factors (programme-internal)

Paper 13 Layer 2 exhibits an ITPFI factorization of the programme's partition function: $\omega_1 = \otimes_p \omega_1^{(p)}$. Each prime $p$ contributes a local factor. This factorization extends, via the BC algebra, to other automorphic objects in the programme.

If YM can be embedded into the BC framework — i.e., if the YM Wilson-loop expectation can be organized as a state on an ITPFI factor — then the ITPFI decomposition gives an Euler product with honest-to-god primes.

This is the most programme-internal route, and the one Route B takes most seriously.

---

## 15.3. A concrete construction via the Wilson-loop spectrum

The Osterwalder-Schrader reconstruction (Paper 8 Link 16) produces a physical Hilbert space $\mathcal{H}_{\text{phys}}$ with a positive self-adjoint Hamiltonian $H$. The spectrum of $H$ is a discrete set of masses $\{m_n\}_{n \geq 0}$ with $m_0 = 0$ (the vacuum) and $m_1 = \Delta_\infty > 0$ (the mass gap).

The generating function of the Wilson-loop spectrum
$$Z_{\text{YM}}(s) = \sum_{n \geq 1} m_n^{-s}$$
is a candidate L-function (the "Wilson-loop zeta function"). Its Dirichlet series converges for $\text{Re}(s)$ sufficiently large (since the spectrum is bounded below by $\Delta_\infty$).

Properties desired:

1. **Meromorphic continuation.** $Z_{\text{YM}}(s)$ should extend meromorphically to $s \in \mathbb{C}$.
2. **Functional equation.** $Z_{\text{YM}}(s)$ should satisfy $\Lambda_{\text{YM}}(s) = \epsilon \Lambda_{\text{YM}}(1 - s)$ for a completed version $\Lambda_{\text{YM}}$ involving local factors.
3. **Euler product.** The spectrum's multiplicative structure should induce an Euler product over some natural index set.

Property 1 follows, in principle, from the functional-integral structure of the theory if the heat kernel $\text{Tr}(e^{-tH})$ has a specific asymptotic expansion (which the Wilson-loop OPE provides). Property 2 is a *postulate* at this stage: if the YM theory has the expected conformal-like UV symmetry (asymptotic freedom) and mass-gap IR symmetry, a functional equation should emerge from the duality between UV and IR.

Property 3 is the hardest: the multiplicative structure of the Wilson-loop spectrum is not manifest. One route is via the ITPFI factorization of Paper 13 (point 15.2.4).

---

## 15.4. The Sym$^k$ structure on YM

For Langlands-Shahidi to apply, the YM L-function needs a $\text{Sym}^k$ structure — a way of lifting the basic L-function $L_{\text{YM}}(s, W_F)$ (fundamental representation) to higher-power L-functions $L_{\text{YM}}(s, W_{\text{Sym}^k F})$.

This is natural in gauge theory: the Wilson loop $W_R$ for $R = \text{Sym}^k F$ (the symmetric $k$-th power of the fundamental) is a well-defined observable, and one can consider its expectation $\langle W_{\text{Sym}^k F}(C) \rangle$.

The Langlands-Shahidi claim, if it transfers, would be: the L-function $L_{\text{YM}}(s, W_{\text{Sym}^k F})$ has the same analytic structure as $L(s, \pi, \text{Sym}^k)$ for automorphic $\pi$ on GL$_2$.

**Test of plausibility:** at the perturbative level, the Wilson-loop expectation $\langle W_{\text{Sym}^k F}(C) \rangle$ can be computed order by order in $g^2$ via Feynman diagrams. The leading perturbative behaviour matches the $\text{Sym}^k$ structure of the gauge group. The *non-perturbative* L-function should inherit this structure from the perturbative one.

---

## 15.5. The key question

**Can pure YM be viewed as an automorphic system?**

This is the central question for Route B. Three levels of answer:

### Level 1: No direct identification

Pure YM on $\mathbb{R}^4$ is a gauge theory on Minkowski (or Euclidean) space. It is not an automorphic form on a symmetric space in the classical sense. There is no direct identification.

### Level 2: Indirect via geometric Langlands

Kapustin-Witten 2007 (detailed in §18) showed that a specific topological twist of N=4 super Yang-Mills on a 4-manifold produces geometric Langlands on the 2-manifold obtained by dimensional reduction. Pure YM is not N=4 SYM, but Paper 10's scheme-independence theorems give a potential scale bridge (§20). If this bridge is rigorous, pure YM's observables *are* organized by geometric Langlands data.

### Level 3: Via the programme's BC/ITPFI framework

The programme's BC algebra provides a natural Hecke action on the YM Hilbert space (via the KK spectral decomposition, Paper 8 Link 1). The ITPFI factorization then gives an Euler product structure, and the resulting $L_{\text{YM}}(s)$ is (potentially) a Langlands-Shahidi L-function in the BC-extended framework.

For Route B, the *working hypothesis* is Level 3: pure YM is a BC-automorphic system via its ITPFI factorization, and the Kim-Sarnak technique applies to the resulting $L_{\text{YM}}$.

---

## 15.6. Construction via BC/ITPFI

The concrete construction of $L_{\text{YM}}$ via the BC framework proceeds as follows.

1. **Identify YM's BC-algebra structure.** Paper 8 Link 1 gives the KK spectral gap via the compact e-circle. The e-circle is a BC object (Paper 13 Layer 2). The Wilson-loop Hilbert space carries an action of the BC algebra via the KK decomposition.

2. **ITPFI-factorize the Wilson-loop state.** The Wilson-loop expectation $\langle W_R(C) \rangle$ is a state on the physical Hilbert space. Under the BC-algebra action, this state factorizes (on suitably restricted observables) as $\omega_{\text{YM}} = \otimes_p \omega_{\text{YM}}^{(p)}$.

3. **Define local L-factors.** For each prime $p$, $\omega_{\text{YM}}^{(p)}$ is a state on the local BC algebra $\mathfrak{A}_{\text{BC}}^{(p)}$. The local L-factor $L_{\text{YM}, p}(s, W_R)$ is the Dirichlet series of the spectrum of $\omega_{\text{YM}}^{(p)}$'s Hamiltonian.

4. **Assemble the Euler product.**
$$L_{\text{YM}}(s, W_R) = \prod_p L_{\text{YM}, p}(s, W_R).$$

5. **Establish analytic properties.** Use ITPFI spectral theory + Paper 13 infrastructure to establish meromorphic continuation, functional equation, and non-vanishing at specific points.

This construction is *plausible* but not yet *rigorous*. The key missing ingredient is step 2 — the ITPFI-factorization of the YM Wilson-loop state. Step 2 is a nontrivial claim about pure YM and requires either:

(a) A direct construction via Paper 8's lattice + RG machinery, extended to BC-compatible states.
(b) An indirect construction via the Kapustin-Witten bridge (Route C), using the BC structure on the geometric Langlands side to pull back to YM.

---

## 15.7. What Route B needs from this construction

For the Kim-Sarnak technique to transfer, the construction of $L_{\text{YM}}$ must satisfy:

1. **$L_{\text{YM}}(s, W_{\text{Sym}^k F})$ is defined for $k = 1, 2, 3, 4$.** (Analogue of Sym$^k$ functoriality.)
2. **$L_{\text{YM}}(s, W_{\text{Sym}^k F})$ has a meromorphic continuation and a functional equation.** (Analogue of Langlands-Shahidi analytic continuation.)
3. **$L_{\text{YM}}(s, W_{\text{Sym}^k F}) \neq 0$ at $s = 1$** (or at the relevant edge point, adjusted for the YM normalization). (Analogue of Kim-Sarnak's non-vanishing input.)
4. **The Dirichlet coefficients of $L_{\text{YM}}(s, W_F \otimes W_{\bar F})$ are non-negative.** (Analogue of Jacquet-Shalika positivity.)

If all four hold, Kim-Sarnak's argument goes through on the YM side, and the output is a specific short-distance bound on $\langle W_R(C) \rangle$ as $|C| \to 0$.

---

## 15.8. Obstructions named explicitly

The construction sketched in §15.6 has the following specific obstructions:

### Obstruction 1: ITPFI-factorization of YM

The claim that the Wilson-loop state on the YM Hilbert space ITPFI-factorizes under the BC action is not yet rigorous. It is plausible but unproven. The proof would require extending Paper 8's Link 16 (OS reconstruction) to be compatible with the BC-algebra action — a significant technical task.

### Obstruction 2: Local factor positivity

The Jacquet-Shalika positivity of Dirichlet coefficients for $L(s, \pi \otimes \tilde{\pi})$ is a delicate representation-theoretic fact. Its YM analogue — positivity of $L_{\text{YM}}(s, W_F \otimes W_{\bar F})$'s Dirichlet coefficients — would follow from a representation-theoretic analysis of the BC action on the YM Hilbert space. This has not been done.

### Obstruction 3: Functional equation

The functional equation $\Lambda_{\text{YM}}(s) = \epsilon \Lambda_{\text{YM}}(1 - s)$ is *postulated* by the S-duality framing but needs an explicit derivation. One route is via the KK-tower decomposition and the e-circle's modular structure; another is via the Kapustin-Witten bridge. Neither is yet complete.

### Obstruction 4: Gauge-group structure

Kim-Sarnak uses $\text{Sym}^k$ on GL$_2$, i.e., the gauge-theoretic analogue would be for $G = \text{U}(2)$ or $\text{SU}(2)$. For general $N$, the Sym$^k$ of the fundamental representation of $\text{SU}(N)$ is a different object, and Langlands-Shahidi functoriality for these representations is open even on the classical side (for automorphic representations of GL$_N$, the full Sym$^k$ functoriality for $k \geq 3, N \geq 3$ is partial).

---

## 15.9. Summary

Route B's heart is the construction of $L_{\text{YM}}(s, W_R)$, the YM Wilson-loop L-function, and the verification that it admits a Langlands-Shahidi structure (specifically, Sym$^k$ functoriality for $k \leq 4$). Via the programme's BC/ITPFI infrastructure, a concrete construction is available, but four explicit obstructions (ITPFI-factorization of YM, positivity, functional equation, gauge-group structure) remain to be addressed.

§16 handles the transfer map — how Langlands-Shahidi structure on $L_{\text{YM}}$, once established, produces short-distance bounds on $\langle W_R(C) \rangle$.

---

*Paper 50 §15. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
