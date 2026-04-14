# §04 — What We Have vs What We Need

*Full inventory of programme-internal tools relevant to H4. What Paper 10, Paper 11 K.4, Paper 8 Links 15-17, ITPFI, and type III$_1$ modular flow give us. What is missing: the short-distance matching technique that Routes A/B/C import.*

---

## 4.1. The accounting problem

H4 is a match statement between two objects:

- **LHS** (perturbative): the formal power series $\{S_n^{\mathrm{PT}}\}$.
- **RHS** (non-perturbative): the Schwinger-function distributions $\{S_n\}$ from OS reconstruction.

To prove the match, we need *tools on the LHS* (control over the perturbative expansion + its resummation) and *tools on the RHS* (control over the non-perturbative distributions + their short-distance structure), plus a *bridge* that converts one into the other.

This section inventories what the programme provides on each side, and what must be imported to close the bridge.

---

## 4.2. What we have on the LHS (perturbative side)

**Paper 10 scheme independence (PROVED, unconditional).**
The running coupling $g(\mu)$ and the beta function $\beta(g)$ are scheme-independent at one and two loops in the precise sense that the leading singularity of $B(t)$ at $t = 2/\beta_0$ is a genuine physical feature, not an artefact of scheme choice. The higher-order scheme dependence is absorbed by the Borel-transform structure (Paper 10 §§5-7 + scheme-independence theorem).

**Implication for H4:** the transseries structure $\{S_k, \sigma_k\}$ of Route A is scheme-independent in its *non-perturbative content*. The free parameters are constrained by physical consistency, not arbitrary.

**Paper 11 K.4 all-orders (PROVED, unconditional).**
Paper 11 extends Paper 10 to *all loop orders*: the beta-function coefficients $\beta_0, \beta_1, \beta_2, \ldots$ and the anomalous-dimension matrix are computed order-by-order with scheme dependence absorbed into a canonical scheme (MS-bar + gradient-flow definition). This gives us the perturbative expansion $\sum a_n g^{2n}$ *with explicit control over the $a_n$'s scheme dependence*.

**Implication for H4:** the coefficients $a_n$ that enter the Lipatov large-order analysis are the *programme-canonical* coefficients, not an ambiguous family. The instanton saddle actions $S_k$ and the renormalon positions $t_k = 2k/\beta_0$ are programme-computable.

**Paper 8 Link 2 + 3 (Balaban UV stability).**
The Balaban polymer expansion — now unconditional via Paper 10 + Paper 11 — gives UV finiteness of the lattice theory with polymer-convergence constant $\kappa$ independent of $k$. This means the *lattice* perturbative expansion is well-defined at every order, and the continuum limit is controlled.

**Implication for H4:** the perturbative series $S_n^{\mathrm{PT}}$ is a well-defined object — it exists as a formal power series with explicit coefficients — and the question is only its *summability*.

---

## 4.3. What we have on the RHS (non-perturbative side)

**Paper 8 Link 15 (gradient-flow well-posedness).**
The Yang-Mills gradient flow $\partial_t A = -\mathrm{grad}\, \mathcal{S}[A]$ is well-posed on $\mathbb{R}^4$ with contractivity (Lemmas 1.1-1.5). This provides a *smoothing operator* that converts the bare gauge field into a smeared, regular object at flow time $t > 0$.

**Implication for H4:** the non-perturbative Schwinger functions $S_n$ are *smooth, regular* distributions at any positive flow time. Short-distance behaviour is studied by taking $t \to 0^+$ after the continuum limit, and the regularity structure is explicit.

**Paper 8 Link 16 (OS reconstruction at fixed $t > 0$).**
The gradient-flowed Schwinger functions $\{S_n^t\}$ satisfy the Osterwalder-Schrader axioms OS0-OS4 at fixed flow time $t > 0$. In particular:

- **OS1** (Euclidean invariance): $S_n^t$ is invariant under $\mathrm{Spin}(4)$.
- **OS2** (reflection positivity): permits Wightman reconstruction.
- **OS3** (symmetry): permutation-symmetric.
- **OS4** (cluster decomposition): exponential clustering at large separation.

**Implication for H4:** we have the *full distributional structure* of the non-perturbative $S_n$. The short-distance expansion is constrained by OS1 (scaling) + OS4 (cluster structure at coincident points).

**Paper 8 Link 17 (composite operator construction).**
The operator $[\mathrm{Tr} F^2]_R$ is constructed as an operator-valued distribution via the gradient-flow smearing + renormalization. Similarly $T_{\mu\nu}^R$ (the renormalized energy-momentum tensor).

**Implication for H4:** we have access to the *OPE coefficients* of $[\mathrm{Tr} F^2]_R \cdot [\mathrm{Tr} F^2]_R$ as distributions, *non-perturbatively*. H4 asks whether these coefficients, in the limit $\mu \to \infty$, match the perturbative ones.

---

## 4.4. Programme-internal algebraic tools

**ITPFI factorization (Paper 13 Layer 2 + the programme's BC/modular-flow infrastructure).**
The modular flow on the KMS$_1$ state of the Bost-Connes algebra induces an ITPFI factorization: the algebra decomposes as an infinite tensor product indexed by primes $p$, each factor a type III$_{\lambda(p)}$ algebra. For YM, the analogous decomposition (proposed in §10) is by momentum scale $\mu$ rather than prime $p$, but the algebraic structure — restricted tensor product + type III classification — is parallel.

**Implication for H4:** the perturbative series and the non-perturbative Schwinger functions admit a *scale-local* decomposition, enabling scale-by-scale matching. This is the ingredient §10 exploits.

**Type III$_1$ modular flow (Paper 29 + Paper 13 Layer 2).**
The programme's type III$_1$ classification of the vacuum algebra implies that the modular flow generates a canonical scaling structure. Connes-Takesaki duality provides a flow on the algebra that, restricted to suitable subalgebras, corresponds to renormalization-group evolution.

**Implication for H4:** the renormalization-group flow that *defines* the running coupling $g(\mu)$ is *algebraically* the modular flow. This provides a direct link between the RG (perturbative side) and the algebraic structure (non-perturbative side).

**Bost-Connes algebra structure.**
The BC algebra provides a spectral realization of the running coupling via KMS states. The coupling $g(\mu)$ becomes a parameter on the KMS-state phase portrait.

**Implication for H4:** phase transitions in the KMS structure (at $\beta = 1$ in Paper 13; analogous phase transitions in YM) correspond to Stokes phenomena in the transseries. The programme's infrastructure anticipates Stokes-line structure.

---

## 4.5. What the programme does NOT provide

Against the LHS/RHS inventory, what is *missing* for H4 is the **bridge**: the technique that takes the perturbative series (LHS) and converts it to a *distribution* matching the non-perturbative $S_n$ (RHS) at short distances.

Specifically, the programme does not provide:

1. **A resummation procedure for a non-Borel-summable series.** The programme has Borel summation as a tool (used in Paper 13 Layer 4's spectral exactness), but not *lateral* Borel summation or resurgent transseries completion for an IR-renormalon-obstructed series.

2. **A Langlands-Shahidi functorial lift for YM Wilson loops.** The programme has access to Langlands theory via Paper 13 (RH) and Paper 25 (Hilbert 12), but the specific functorial-lift apparatus of Kim-Sarnak-Shahidi applied to YM is external.

3. **A geometric Langlands correspondence for pure YM.** The programme has Kapustin-Witten-twisted N=4 SYM available through Paper 29 (Hodge) and Paper 25, but the rigorous bridge from N=4 SYM to pure YM (the scale-bridge limit) is not programme-internal.

These are the three gaps that Routes A, B, C respectively aim to fill.

---

## 4.6. What imported machinery each route needs

| Route | Imported machinery | External source |
|---|---|---|
| **A — Resurgent Transseries** | Écalle-Voros resurgence, alien calculus, lateral Borel summation | Écalle 1981, Voros 1983, Costin 2009 |
| **A** | Dyson-Schwinger + transseries framework | Klaczynski 2016 |
| **A** | 2D YM complete resurgent analysis | Okuyama-Sakai 2022 (arXiv:2212.11988) |
| **B — Langlands-Shahidi** | Symmetric power L-function construction | Kim-Shahidi 1999, Kim-Sarnak 2003 |
| **B** | Eisenstein series on exceptional groups | Shahidi 1978-1988 series |
| **B** | Langlands functoriality | Langlands 1970, Arthur 2013 |
| **C — Kapustin-Witten** | Topological twist of N=4 SYM | Kapustin-Witten 2007 |
| **C** | Geometric Langlands | Gaitsgory-Raskin 2024 |
| **C** | BV quantization of KW theories | Elliott-Gwilliam-Williams 2024 |

Each route imports a substantial external apparatus. Paper 50's task is to *integrate* these imports with programme-internal tools and to produce a proof sketch sufficient for formalization.

---

## 4.7. The programme-specific contributions

Paper 50's novel contributions, beyond importing external machinery, are:

- **§10 ITPFI connection (Route A):** the proposal that the transseries parameters $\{\sigma_k\}$ admit a scale-local (analogue of local-at-$p$) decomposition inherited from the programme's type III$_1$ modular structure. No prior literature has made this connection.
- **§12 S-duality identification (Route B setup):** Paper 60 §21's S-duality diagnostic pairs H4 with Selberg's eigenvalue bound. The Kim-Sarnak bound becomes a *dual* of what Route B computes. This framing is programme-specific.
- **§20 scale-bridge theorem (Route C):** Paper 10's scheme independence is used to rigidify the N=4 SYM → pure YM scale-bridge. The programme's scheme-independence infrastructure gives rigidity that non-programme analyses lack.

These contributions are *auxiliary* — they make the external machinery applicable to the programme's H4. They do not constitute independent proofs of H4; they constitute programme-specific leverage on the three external routes.

---

## 4.8. Summary

**What we have:**
- Full perturbative control: coefficients $a_n$ explicitly computable via Paper 10 + Paper 11 K.4.
- Full non-perturbative control: $S_n$ exists, OS axioms satisfied, OPE accessible via Paper 8 Links 15-17.
- Algebraic structure: ITPFI factorization, type III$_1$ modular flow, BC algebra.
- Scheme independence: Paper 10's theorems.

**What we need:**
- A resummation technique that matches LHS to RHS at short distances.

**What we import:**
- Écalle-Voros resurgence (Route A).
- Langlands-Shahidi functoriality (Route B).
- Geometric Langlands (Route C).

**What we add that is novel:**
- §10 ITPFI-transseries connection.
- §12 S-duality-based route identification.
- §20 scheme-independence rigidity for scale bridge.

The imbalance is honest: Paper 50 imports more than it originates. The imports are where the hard mathematics lives. The programme's role is to *channel* the imports into a specific attack on H4 and to add the algebraic structure that makes the attacks programme-compatible.

---

*Paper 50 §04. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
