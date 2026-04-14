# §17 — Route B Proof Sketch

*Step-by-step assembly of Route B. Construct YM L-function, verify functoriality, apply Kim-Sarnak-style bounds at short distances, conclude H4. Specific obstructions named.*

---

## 17.1. The proof sketch in one paragraph

Construct the YM Wilson-loop L-function $L_{\text{YM}}(s, W_R)$ via the BC/ITPFI factorization of the YM Hilbert space (§15). Establish that $L_{\text{YM}}$ admits a Sym$^k$ lift for $k = 1, 2, 3, 4$, analogous to Kim 2003 on GL$_2$ (§14-§16). Verify that the local Satake parameters on the YM side match those of a cuspidal automorphic representation of GL$_2(\mathbb{A}_\mathbb{Q})$ via the BC bridge. Apply the Kim-Sarnak 2003 argument to $L_{\text{YM}}(s, W_{\text{Sym}^4 F})$ at $s = 1$; extract a bound on the YM two-point function's short-distance behaviour. Translate the bound into a statement about the OPE coefficient at leading order in $g^2(\mu)$. The resulting statement is H4.

---

## 17.2. The seven steps

### Step 1: Construct the YM Wilson-loop L-function

**Input:** Paper 8's Hilbert space $\mathcal{H}_{\text{phys}}$ from OS reconstruction (Link 16).

**Procedure:** Use the KK spectral decomposition of the e-circle (Paper 1) to organize $\mathcal{H}_{\text{phys}}$ into BC-compatible sectors. Define the YM Wilson-loop state $\omega_{\text{YM}}$. Assume (the first conjectural input) that $\omega_{\text{YM}}$ ITPFI-factorizes over BC primes as $\omega_{\text{YM}} = \otimes_p \omega_{\text{YM}}^{(p)}$.

**Output:** the local factors $L_{\text{YM}, p}(s, W_R)$ and their Euler product $L_{\text{YM}}(s, W_R) = \prod_p L_{\text{YM}, p}(s, W_R)$.

**Obstruction 1:** the ITPFI-factorization of $\omega_{\text{YM}}$.

### Step 2: Establish the Sym$^k$ lift on the YM side

**Input:** the L-function $L_{\text{YM}}(s, W_F)$ for the fundamental Wilson loop.

**Procedure:** For $k = 2, 3, 4$, define $L_{\text{YM}}(s, W_{\text{Sym}^k F})$ as the Wilson-loop L-function in the symmetric $k$-th power representation. Verify that this is well-defined as a Dirichlet series (from the ITPFI factorization) and has an Euler product.

**Output:** the family $\{L_{\text{YM}}(s, W_{\text{Sym}^k F})\}_{k=1}^{4}$.

**Obstruction 2:** even assuming the ITPFI-factorization, the Sym$^k$ of the local factors must combine correctly into a global L-function. This is automatic at the *Dirichlet series* level, but the interpretation as an L-function (with functional equation) is not.

### Step 3: Derive the functional equation of $L_{\text{YM}}$

**Input:** $L_{\text{YM}}(s, W_{\text{Sym}^k F})$ for $k = 1, 2, 3, 4$.

**Procedure:** Derive a functional equation
$$\Lambda_{\text{YM}}(s, W_{\text{Sym}^k F}) = \epsilon_k \Lambda_{\text{YM}}(1 - s, W_{\text{Sym}^k F^*})$$
either (i) from a gauge-theoretic theta-kernel / Poisson-summation argument, or (ii) from a Kapustin-Witten S-duality applied to N=4 SYM followed by the pure-YM scale bridge, or (iii) directly from the BC algebra's modular structure (Tomita-Takesaki on the GNS representation).

**Output:** the completed L-function $\Lambda_{\text{YM}}$ with established functional equation.

**Obstruction 3:** none of (i), (ii), (iii) is currently available in full rigour for pure YM. Route (ii) is the content of Route C; Route (iii) uses programme-internal infrastructure but has not been executed for YM.

### Step 4: Satake matching with a GL$_2$ automorphic representation

**Input:** the YM Satake parameters $\alpha_p^{\text{YM}}, \beta_p^{\text{YM}}$ at each prime $p$.

**Procedure:** Identify a cuspidal automorphic representation $\pi = \otimes_p \pi_p$ of GL$_2(\mathbb{A}_\mathbb{Q})$ whose Satake parameters match the YM ones: $\alpha_p^{\text{YM}} = \alpha_p(\pi_p), \beta_p^{\text{YM}} = \beta_p(\pi_p)$.

**Output:** a *correspondence* $\omega_{\text{YM}} \leftrightarrow \pi$ between the YM Wilson-loop state and an automorphic form.

**Obstruction 4:** there is no a priori reason $\pi$ should exist. The matching is a conjecture; its proof would be a YM-adapted version of the classical Langlands correspondence.

### Step 5: Apply Kim 2003 Sym$^4$ functoriality

**Input:** the matched pair $(\omega_{\text{YM}}, \pi)$ from Step 4.

**Procedure:** Invoke Kim 2003: since $\pi$ is a cuspidal automorphic representation of GL$_2(\mathbb{A}_\mathbb{Q})$, the Sym$^4$ lift $\text{Sym}^4(\pi)$ is an automorphic representation of GL$_5(\mathbb{A}_\mathbb{Q})$. The L-function $L(s, \pi, \text{Sym}^4)$ has established analytic properties (meromorphic continuation, functional equation, non-vanishing at $s = 1$).

Via the matching, $L(s, \pi, \text{Sym}^4) = L_{\text{YM}}(s, W_{\text{Sym}^4 F})$, so the YM L-function inherits these analytic properties.

**Output:** established analytic properties for $L_{\text{YM}}(s, W_{\text{Sym}^4 F})$: meromorphic continuation, functional equation, non-vanishing at $s = 1$.

**Obstruction 5:** this step is *conditional on Steps 1-4*. If those conditionals close, Step 5 is the direct application of Kim 2003.

### Step 6: Apply Kim-Sarnak 2003 archimedean bound

**Input:** the established analytic properties of $L_{\text{YM}}(s, W_{\text{Sym}^4 F})$ from Step 5.

**Procedure:** Run the Kim-Sarnak 2003 argument: combine the Sym$^k$-L-function non-vanishings ($k = 1, 2, 3, 4$) with the Jacquet-Shalika positivity of the Rankin-Selberg L-function $L(s, \pi \otimes \tilde{\pi})$. The archimedean Langlands parameter of $\pi$ is constrained to lie in the complementary-series range with bound $|t_0| \leq \sqrt{1/4 - 975/4096}$, giving $\lambda_1(\pi) \geq 975/4096$.

**Output:** a spectral bound on the YM Wilson-loop state's archimedean parameter, giving a bound on the mass-spectrum discriminant at short distances.

**Obstruction 6:** the Jacquet-Shalika positivity must transfer to YM, which it does under the Satake matching of Step 4. No new obstruction here beyond Step 4.

### Step 7: Translate to OPE coefficient at short distance

**Input:** the spectral bound from Step 6.

**Procedure:** The YM Wilson-loop OPE at short distances is controlled by the Hamiltonian's spectrum (via Paper 8 Link 17's construction of $[\text{Tr} F^2]_R$). The spectral bound from Step 6 translates into a bound on the coefficient of the leading perturbative term in the OPE expansion:
$$\langle \text{Tr} F^2(0) \cdot \text{Tr} F^2(x) \rangle = \frac{c_1}{|x|^8} + c_2 g^2(\mu) \log|x| + \ldots.$$
The leading coefficient $c_1$ matches the perturbative value (vacuum diagrams), and the first correction $c_2$ matches the one-loop perturbative computation, *modulo an error bounded by the Sym$^4$ analytic bound*.

**Output:** the AF-match statement: the non-perturbative 2-point function agrees with the perturbative expansion at short distances, with controlled error.

**This is H4.**

---

## 17.3. What closes H4

Route B closes H4 if all seven steps complete. Specifically:

- Step 1 requires the BC/ITPFI factorization of the YM Wilson-loop state.
- Step 2 is structural, given Step 1.
- Step 3 requires the functional equation of $L_{\text{YM}}$.
- Step 4 requires the Satake matching to an automorphic $\pi$.
- Step 5 is Kim 2003 applied via the matching.
- Step 6 is Kim-Sarnak 2003 applied via the matching.
- Step 7 is the OPE translation, using Paper 8 Link 17's Wilson-loop OPE structure.

The routes that close H4 via Route B are conditional on Steps 1, 3, 4 — the three conjectural ingredients. Steps 5 and 6 are *purely* applications of established theorems (Kim 2003, Kim-Sarnak 2003) to the matched side.

---

## 17.4. Specific obstructions summarized

| Obstruction | Content | Difficulty | Possible resolution |
|---|---|---|---|
| **Ob.1** | BC/ITPFI factorization of the YM Wilson-loop state | Hard. Requires extending Paper 8 Link 16 (OS reconstruction) to be BC-equivariant. | Programme-internal; uses existing BC infrastructure + YM lattice + RG. |
| **Ob.2** | Sym$^k$ compatibility on the YM side | Moderate. Structural, given Ob.1. | Direct from the BC local factors. |
| **Ob.3** | Functional equation of $L_{\text{YM}}$ | Hard. Three possible derivations (theta kernel / Kapustin-Witten S-duality / Tomita-Takesaki), none currently complete. | Any one suffices; Route C's Kapustin-Witten route is most direct. |
| **Ob.4** | Satake matching with an automorphic $\pi$ | Hardest. Requires a YM-adapted Langlands correspondence. | Either (a) direct via BC-algebra representation theory, or (b) via Route C's geometric Langlands. |
| **Ob.5** | Jacquet-Shalika positivity on YM side | Mild. Follows from Ob.4. | Automatic once Ob.4 closes. |
| **Ob.6** | OPE translation of the Sym$^4$ bound to the two-point function | Mild. Uses Paper 8 Link 17. | Programme-internal. |

The critical obstructions are Ob.1, Ob.3, Ob.4. If these close, Route B completes.

---

## 17.5. How Route C can help Route B close

Route C (Kapustin-Witten + Gaitsgory-Raskin) provides independent resolution of Ob.3 and Ob.4:

- **Ob.3 (functional equation):** Kapustin-Witten 2007 showed that N=4 SYM has an S-duality at $\tau \to -1/\tau$. Under the scale bridge to pure YM (Paper 10 scheme independence, §20), this S-duality descends to a functional equation on $L_{\text{YM}}$. Route C provides this derivation.

- **Ob.4 (Satake matching):** Gaitsgory-Raskin 2024 proved geometric Langlands, which produces a correspondence between quasi-coherent sheaves on the Hitchin moduli of a Riemann surface and D-modules on the moduli of G-bundles. Under the scale bridge, this correspondence produces the YM side of the Satake matching.

Thus: if Route C closes the scale bridge (Ob.C.1 of §23), it *automatically* closes Ob.3 and Ob.4 of Route B. The two routes are not independent; they share the hardest obstructions and can reinforce each other.

Equivalently: Ob.3 and Ob.4 of Route B are *the same as* the scale-bridge obstruction of Route C, re-stated in Langlands language.

---

## 17.6. The ship criterion for Route B

**If Ob.1, Ob.3, Ob.4 all close, Route B ships.**

Minimum viable product:
- A lattice-level proof of Ob.1 (BC-compatible OS reconstruction on a finite lattice), with extrapolation to continuum via Paper 8's existing machinery.
- Either a theta-kernel derivation of the functional equation (Ob.3) or an appeal to Route C's Kapustin-Witten route.
- Either a direct BC-algebra construction of the Satake matching (Ob.4) or an appeal to Route C's geometric-Langlands route.

If Route B ships with appeals to Route C, the two are *jointly* closing H4. The programme accepts this: the shipping criterion is not "Route B alone," but "Route B + whichever other routes it needs."

---

## 17.7. Honest confidence assessment

**Before Route B is attempted:** 4/10. The S-duality framing is natural; Kim-Sarnak is well-established; the BC infrastructure is in place. The three obstructions are hard but not obviously intractable.

**After Ob.1 is attempted:** TBD. If the BC/ITPFI factorization of YM is constructed, confidence rises to 6-7/10. If it is not, Route B stalls at Ob.1 and must rely on Route C.

**After Ob.3 and Ob.4 via Route C:** 5-6/10. Route C's scale bridge is itself conjectural; using it to resolve Route B's obstructions doesn't increase total confidence but does streamline the attack.

**Combined Route B + Route C (shared obstructions closed):** 6-7/10. The two routes attacking the same target from two directions (classical Langlands + geometric Langlands) is more persuasive than either alone.

---

## 17.8. What Route B adds to the programme even if it does not close H4

Even if Route B fails to close H4, the *construction* of $L_{\text{YM}}$ via the BC/ITPFI factorization is a permanent addition to the programme:

1. **A new L-function in the programme's library.** $L_{\text{YM}}$ joins the zeta function, Dirichlet L-functions, modular form L-functions, etc., as a programme-accessible object.
2. **A test of the BC framework.** If BC/ITPFI factorization of YM fails, we learn that the BC framework has limits — specifically, it does not apply to non-abelian gauge theories in their natural formulation. This is *diagnostic* information.
3. **A bridge to Route C.** Even if Route B's classical-Langlands route fails, its construction of $L_{\text{YM}}$ provides a concrete target for Route C's geometric-Langlands route.

Route B is therefore valuable *as exploration*, independent of its success on H4.

---

## 17.9. Summary of Route B

Seven steps. Three critical obstructions (Ob.1, Ob.3, Ob.4). Two of the three (Ob.3, Ob.4) share the scale-bridge obstruction of Route C. Confidence 4/10 initially, 6-7/10 if the shared obstructions close via either route.

Route B's attack vector: *the S-duality of Paper 60 §21 says Kim-Sarnak's Selberg bound is the RESONANCE-side dual of H4. The Langlands-Shahidi machinery that produced Kim-Sarnak's bound should transfer to H4 via the functional equation, provided the YM Wilson-loop L-function can be constructed and matched to an automorphic representation via BC/ITPFI. All three conjectural pieces are programme-internal or can be imported from Route C.*

Route B is Langlands attacking YM through the spectral side. Route C is Langlands attacking YM through the geometric side. Both attack the same target via the same programme (Langlands), using different machinery.

---

*Paper 50 §17. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
*Part III complete. Part IV begins with Kapustin-Witten 2007.*
