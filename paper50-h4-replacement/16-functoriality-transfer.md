# §16 — Functoriality Transfer: Automorphic → Gauge Theory

*The transfer map. Langlands functoriality on the automorphic side produces spectral bounds on the gauge-theory side via the S-transform. The analytic structure transfers cleanly if the L-functions have compatible functional equations.*

---

## 16.1. The map to be built

Fix the YM Wilson-loop L-function $L_{\text{YM}}(s, W_R)$ constructed in §15. The goal of the functoriality transfer is a well-defined map
$$\mathcal{T} : \{\text{Langlands-Shahidi L-functions}\} \longrightarrow \{\text{YM Wilson-loop L-functions}\}$$
such that if $L_{\text{auto}}(s, \pi, r)$ on the automorphic side has a specific analytic property (meromorphic continuation, functional equation, bounded growth in vertical strips, non-vanishing at specific points), then $\mathcal{T}(L_{\text{auto}})$ on the YM side has the corresponding property.

The image of $\mathcal{T}$ need not cover all of $L_{\text{YM}}$; what matters is that *the specific L-functions appearing in Kim-Sarnak's argument* (symmetric power L-functions on GL$_2$) land in $\mathcal{T}$'s image, with analytic properties transferred.

---

## 16.2. The transfer in three steps

Step 1: **the functional equation is the transfer kernel.**

The S-transform of Paper 60 §21 exchanges $s \leftrightarrow 1 - s$. Every Langlands-type L-function satisfies a functional equation of this form:
$$\Lambda(s, \pi, r) = \epsilon(\pi, r) \Lambda(1 - s, \tilde{\pi}, r^*).$$
This is the *content* of S-duality on the automorphic side.

The conjectural YM Wilson-loop L-function is postulated to satisfy the same structure:
$$\Lambda_{\text{YM}}(s, W_R) = \epsilon_{\text{YM}}(R) \Lambda_{\text{YM}}(1 - s, W_{\bar R}).$$

If both functional equations hold with *compatible* local factors (in a sense to be made precise), then the transfer $\mathcal{T}$ is given by matching L-factors at each prime:
$$\mathcal{T}(L_{\text{auto}})(s) = L_{\text{auto}}(s)$$
*as a Dirichlet series*, reinterpreted as a YM object via the BC/ITPFI correspondence of §15.6.

The key point: the *same Dirichlet series* is interpreted on both sides — automorphic side via GL$_n(\mathbb{A})$ representations, YM side via Wilson-loop observables.

Step 2: **the ITPFI bridge.**

Paper 13 Layer 2 establishes that the BC algebra's ground state $\omega_1$ ITPFI-factorizes as $\omega_1 = \otimes_p \omega_1^{(p)}$. Each local factor $\omega_1^{(p)}$ corresponds to a representation of the local BC algebra at prime $p$.

On the automorphic side: a cuspidal automorphic representation $\pi = \otimes_p \pi_p$ of GL$_n(\mathbb{A}_\mathbb{Q})$ factorizes over places; each $\pi_p$ is a representation of GL$_n(\mathbb{Q}_p)$, and the local L-factor is determined by $\pi_p$.

On the YM side: the Wilson-loop state, under the postulated BC-algebra factorization (§15.6), is $\omega_{\text{YM}} = \otimes_p \omega_{\text{YM}}^{(p)}$. Each $\omega_{\text{YM}}^{(p)}$ encodes local Wilson-loop data at prime $p$.

The *bridge*: at each prime $p$, there is a correspondence
$$\pi_p \longleftrightarrow \omega_{\text{YM}}^{(p)}$$
between automorphic local representations and YM local states. The local L-factors match on the two sides. Assembling over all $p$, the global L-functions match.

This step is where the BC algebra does the heavy lifting: it provides the *local* correspondence, which then assembles into the *global* correspondence by Euler-product multiplication.

Step 3: **the Sym$^k$ compatibility.**

For Kim-Sarnak to apply, the transfer must commute with the Sym$^k$ operation. That is:
$$\mathcal{T}(L_{\text{auto}}(s, \pi, \text{Sym}^k)) = L_{\text{YM}}(s, W_{\text{Sym}^k F}).$$

On the automorphic side, $L_{\text{auto}}(s, \pi, \text{Sym}^k)$ is the Langlands-Shahidi L-function for the symmetric $k$-th power representation of ${}^L \text{GL}_2 = \text{GL}_2(\mathbb{C})$.

On the YM side, $L_{\text{YM}}(s, W_{\text{Sym}^k F})$ is the Wilson-loop L-function for the Wilson loop in the $\text{Sym}^k$ representation of the gauge group.

The compatibility claim: these two L-functions have the *same local L-factors* at each prime $p$, under the BC correspondence $\pi_p \leftrightarrow \omega_{\text{YM}}^{(p)}$.

If Sym$^k$-compatibility holds, the Kim-Sarnak bound transfers: the bound on $L_{\text{auto}}(s, \pi, \text{Sym}^4)$ at $s = 1$ gives a corresponding bound on $L_{\text{YM}}(s, W_{\text{Sym}^4 F})$, which via the Wilson-loop OPE gives a short-distance bound on $\langle W_{\text{Sym}^4 F}(C) \rangle$ — the YM analogue of $975/4096$.

---

## 16.3. What the transfer does NOT require

A common misreading: the transfer $\mathcal{T}$ is not a *bijection* between the automorphic and gauge-theoretic worlds. It does not claim that pure YM is an automorphic representation. It does not claim that Wilson-loop states equal Maass forms.

The transfer is a *functorial map on L-functions*: given an L-function on one side, it produces an L-function on the other side, with compatible analytic properties. The underlying objects (cuspidal automorphic representations vs Wilson-loop observables) are different; only the L-functions they produce are matched.

This is a weaker claim than a full correspondence, and it is what makes Route B tractable.

---

## 16.4. Why the functional equation is sufficient

The transfer's power comes from a simple observation: *all of Kim-Sarnak's analytic manipulations are statements about L-functions, not about the underlying automorphic representations*.

Kim-Sarnak uses:
- $L(s, \pi, \text{Sym}^k)$ has meromorphic continuation.
- $L(s, \pi, \text{Sym}^k)$ satisfies a functional equation.
- $L(s, \pi, \text{Sym}^k) \neq 0$ at $s = 1$.
- The Dirichlet coefficients of $L(s, \pi \otimes \tilde{\pi})$ are non-negative.

Each of these is a *property of the L-function as an analytic object*. If the transfer $\mathcal{T}$ preserves these properties — i.e., if $\mathcal{T}(L_{\text{auto}})$ has meromorphic continuation, functional equation, non-vanishing at $s = 1$, and non-negative Dirichlet coefficients whenever $L_{\text{auto}}$ does — then the Kim-Sarnak argument applies on the YM side.

The functional equation is the key *symmetry* that encodes all of these properties. The meromorphic continuation follows from the Eisenstein-series analytic continuation, which in turn follows from the functional equation and bounded growth. The non-vanishing at $s = 1$ follows from the residue structure, controlled by the functional equation. Positivity follows from the Jacquet-Shalika argument, which is structural and transfers as long as the local representations do.

Hence: **if the YM L-function $L_{\text{YM}}$ satisfies a functional equation of the Langlands type, the transfer is automatic.**

---

## 16.5. The transfer in the BC/ITPFI framework

Concretely, the transfer is implemented as follows.

### 16.5.1. Automorphic side

Let $\pi = \otimes_p \pi_p$ be a cuspidal automorphic representation of GL$_2(\mathbb{A}_\mathbb{Q})$. For each prime $p$ where $\pi_p$ is unramified, the Satake parameters are $\alpha_p, \beta_p \in \mathbb{C}^*$ (with $\alpha_p \beta_p = 1$ by the central-character normalization). The local L-factor is
$$L_p(s, \pi_p, \text{Sym}^k) = \prod_{j=0}^{k} \frac{1}{1 - \alpha_p^{k-j} \beta_p^j \cdot p^{-s}}.$$

### 16.5.2. YM side

Under the BC/ITPFI factorization of the Wilson-loop state, the local factor at prime $p$ is a state $\omega_{\text{YM}}^{(p)}$ on $\mathfrak{A}_{\text{BC}}^{(p)}$. This state is characterized by a pair of "Satake-like" parameters $\alpha_p^{\text{YM}}, \beta_p^{\text{YM}}$ reading off the spectral data at prime $p$.

The local L-factor on the YM side is
$$L_p^{\text{YM}}(s, W_{\text{Sym}^k F}) = \prod_{j=0}^{k} \frac{1}{1 - (\alpha_p^{\text{YM}})^{k-j} (\beta_p^{\text{YM}})^j \cdot p^{-s}}.$$

### 16.5.3. Matching

The transfer $\mathcal{T}$ is the claim that, under the BC correspondence $\pi_p \leftrightarrow \omega_{\text{YM}}^{(p)}$, the Satake parameters match:
$$\alpha_p = \alpha_p^{\text{YM}}, \quad \beta_p = \beta_p^{\text{YM}}.$$

If this matching holds at every prime, the global L-functions coincide:
$$L_{\text{auto}}(s, \pi, \text{Sym}^k) = L_{\text{YM}}(s, W_{\text{Sym}^k F}).$$

The transfer is then the *identity* on L-functions, with the automorphic and gauge-theoretic interpretations being two different readings of the same Dirichlet series.

---

## 16.6. What the transfer gives, specifically

If Sym$^k$-compatible transfer holds for $k \leq 4$, then Kim-Sarnak 2003 gives the following YM statement.

**Theorem (conditional on Route B transfer).** *Assume the BC/ITPFI factorization of the YM Wilson-loop state holds with Satake-matching to an automorphic representation of GL$_2(\mathbb{A}_\mathbb{Q})$. Then the YM two-point function*
$$\langle \text{Tr} F^2(0) \cdot \text{Tr} F^2(x) \rangle$$
*has a short-distance expansion in which the leading perturbative coefficient matches the non-perturbative value to within an error bounded by the $975/4096$ analogue on the YM side.*

The precise formulation of "the $975/4096$ analogue on the YM side" requires unwinding the Wilson-loop OPE; the bound takes the form
$$\left| \frac{\text{(non-perturbative 2-pt function)}}{\text{(perturbative 2-pt function)}} - 1 \right| = O\left(g^{2(k+1)}(\mu)\right),$$
with $k = 4$ corresponding to the Sym$^4$ bound. This is *precisely* the AF-match statement at short distances.

Thus: **if the transfer holds, Route B closes H4 via Kim-Sarnak 2003 modulo the obstructions named in §15.8.**

---

## 16.7. Obstructions to the transfer

The transfer is conditional on four things:

### 16.7.1. BC/ITPFI factorization of YM

(From §15, Obstruction 1.) The Wilson-loop state must factorize over BC primes. Not yet proven.

### 16.7.2. Satake matching

The Satake parameters on the two sides must actually match. This is *not* a tautology: the automorphic Satake parameters are representation-theoretic (coming from unramified representations of GL$_2(\mathbb{Q}_p)$); the YM Satake-like parameters are spectral (coming from the KK decomposition of the Wilson-loop state). The matching is a nontrivial claim.

### 16.7.3. Functional equation of $L_{\text{YM}}$

The functional equation is postulated, not derived. A direct derivation from YM's gradient-flow structure is not yet available.

### 16.7.4. Sym$^k$-compatibility

The transfer commutes with Sym$^k$ only if the gauge-group representations and the Langlands-group representations are compatible. For $G = \text{SU}(2)$ and ${}^L \text{GL}_2 = \text{GL}_2(\mathbb{C})$, Sym$^k$ operations are directly compatible. For general $G = \text{SU}(N)$, the compatibility requires additional structure (specifically, a choice of L-group homomorphism ${}^L G \to \text{GL}_N(\mathbb{C})$, which is standard for classical groups).

---

## 16.8. Honest status of the transfer

The transfer $\mathcal{T}$ is, at this writing (April 2026), a *conjectural framework*, not a theorem. What is established:

- The BC/ITPFI factorization of the programme's ground state $\omega_1$ (Paper 13 Layer 2).
- The Langlands-Shahidi construction of automorphic L-functions on exceptional groups (§14).
- Kim-Sarnak 2003's bound $975/4096$ via Sym$^4$ functoriality (§13).
- The S-duality identification of H4 and Selberg as dual faces (§12, Paper 60 §21).

What is conjectural:

- The BC/ITPFI factorization of the YM Wilson-loop state.
- The Satake matching between automorphic and YM local data.
- The functional equation of $L_{\text{YM}}$.
- The Sym$^k$-compatibility of the transfer.

Route B's plausibility rests on the observation that *all four conjectural pieces are structurally natural* and have partial support from the programme's infrastructure. None is contradicted by known results. Each requires specific technical work.

---

## 16.9. What would make the transfer rigorous

The transfer would be rigorous if the following were achieved:

1. **ITPFI-factorization of pure YM on $\mathbb{R}^4$**, compatible with the BC algebra. Requires extending Paper 8's OS reconstruction (Link 16) to be BC-equivariant.

2. **Construction of the YM adèles**: a ring of "gauge-theoretic adèles" $\mathbb{A}_{\text{YM}}$, analogous to $\mathbb{A}_\mathbb{Q}$, on which Wilson-loop operators act. The local factors at each prime $p$ give the Satake parameters.

3. **Functional equation of $L_{\text{YM}}$**, derived either from a theta-kernel construction (gauge-theoretic theta function?) or from a Kapustin-Witten-style S-duality.

4. **Matching theorem**: a proof that the Satake parameters of the automorphic representation $\pi$ and the YM state $\omega_{\text{YM}}$ agree when the Wilson loop and the automorphic form are "dual" in the appropriate sense.

Each of these is a substantial theorem. Their combined execution is what Route B would require.

---

## 16.10. Route C as an alternative source of transfer

Route C (Kapustin-Witten + Gaitsgory-Raskin) provides an *alternative* source for the transfer via geometric Langlands. In Route C, the Wilson-loop operators on the YM side correspond to objects in the derived category of coherent sheaves on the Hitchin moduli space; the automorphic side (classical Langlands-Shahidi) is replaced by the geometric side (perverse sheaves on the moduli of G-bundles).

The matching of local data in Route C comes from the geometric Langlands correspondence itself, which Gaitsgory-Raskin 2024 PROVED. This gives, in principle, a rigorous transfer for N=4 SYM; the scale bridge (§20) is what extends it to pure YM.

Routes B and C therefore provide *independent mechanisms* for the transfer: B uses classical Langlands via the BC algebra; C uses geometric Langlands via Kapustin-Witten. If either mechanism works, the transfer is established and Kim-Sarnak (for B) or Gaitsgory-Raskin (for C) applies.

---

## 16.11. Summary

The functoriality transfer $\mathcal{T}$ is the bridge from automorphic L-functions (Langlands-Shahidi side) to gauge-theoretic L-functions (YM side). Implemented via BC/ITPFI factorization and Satake matching, the transfer would make Kim-Sarnak 2003's bound directly applicable to the YM Wilson-loop two-point function, yielding the AF-match at short distances. The transfer's rigor depends on four conjectural pieces (ITPFI-factorization of YM, Satake matching, functional equation, Sym$^k$-compatibility); none is contradicted, each is structurally natural, all require technical work.

§17 assembles the complete Route B proof sketch, names the specific obstructions, and gives the ship criterion.

---

*Paper 50 §16. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
