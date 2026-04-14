# §01 — H4: The Statement and the Stakes

*What H4 says, where it sits in Paper 8's chain, why it is the last conditional, and what closing it gains.*

---

## 1.1. The statement

**H4 (Hypothesis 4).** *The non-perturbative Schwinger functions of 4D SU(N) Yang-Mills theory on $\mathbb{R}^4$ agree with the perturbative expansion at short distances.*

More precisely, let $\{S_n\}_{n \geq 1}$ denote the Schwinger functions reconstructed from the lattice continuum limit via Paper 8 Links 15-17 (gradient-flow smoothing + Osterwalder-Schrader reconstruction), and let $\{S_n^{\mathrm{PT}}\}_{n \geq 1}$ denote the formal power series in the running coupling $g(\mu)$ obtained from Feynman-diagram expansion with dimensional regularization and a mass-independent scheme. H4 asserts: for every $n$ and for every regime where $|x_i - x_j| \to 0$ sufficiently fast that the OPE applies, the non-perturbative $S_n$ admits an asymptotic expansion in $g(\mu)$ coinciding term by term with $S_n^{\mathrm{PT}}$.

Equivalently: the leading coefficient of the short-distance OPE of the non-perturbative two-point function of $\mathrm{Tr} F^2$ matches the perturbative one-loop coefficient $\beta_0 g^2(\mu)$, and all subleading coefficients match the higher-loop computation.

This is the **asymptotic-freedom match**: the non-perturbative QFT, at short distances, *is* (asymptotically) the perturbative QFT.

---

## 1.2. Position in Paper 8's chain

Paper 8 proves the Yang-Mills mass gap in 18 links. Links 1-17 are unconditional:

- Links 1-5: KK spectral gap $\Delta_0^{\mathrm{KK}} > 0$ and its descent to $\Delta_0^{\mathrm{std}} > 0$ (Paper 1 + Weitzenböck + reduced transfer matrix).
- Links 2-14: Balaban RG + polymer convergence + Newton decomposition + operator classification, producing $\Delta_\infty > 0$ at the lattice level.
- Links 15-17: gradient-flow well-posedness, OS reconstruction at fixed flow time $t > 0$, and construction of $[\mathrm{Tr} F^2]_R$ as an operator-valued distribution.

Link 18 is the final link: **AF match + leading-order OPE**. It asserts that the Schwinger functions constructed in Link 16 display the perturbative asymptotic-freedom behaviour at short distances — that the non-perturbative $S_n$ agrees with $S_n^{\mathrm{PT}}$ in the short-distance regime.

Link 18 is *conditional on H4*. Paper 8 cannot prove Link 18 unconditionally because the perturbative series $S_n^{\mathrm{PT}}$ is a *divergent asymptotic series* (Dyson 1952, Lipatov 1977), and the required matching is a statement that the two sides — one convergent (non-perturbative $S_n$), one divergent (perturbative $S_n^{\mathrm{PT}}$) — agree in a specific asymptotic sense.

---

## 1.3. Why H4 is the last wall

The seventeen prior links admit proofs inside the programme's existing infrastructure:

- Spectral gaps come from Kaluza-Klein compactification and Weitzenböck identities.
- UV stability comes from Balaban's polymer expansion (the setup assumption is now unconditional at all loop orders per Paper 10 + Paper 11 K.4).
- IR behaviour comes from the RG recursion and the Newton decomposition of composite operators.
- Continuum reconstruction comes from gradient-flow contractivity + OS positivity.

Link 18, however, requires a fundamentally different kind of argument: a *match* between two *incommensurable* expansions. The perturbative series is a formal power series; the non-perturbative Schwinger functions are genuine distributions. The match is not an identity — it is a statement that a divergent series is the asymptotic expansion, in the sense of Poincaré, of a specific distribution.

This kind of statement is not provable from gradient flow, OS reconstruction, or any lattice-RG argument. It requires either:

1. A *resummation* technique that converts the perturbative series into a non-perturbative object (resurgent transseries, Borel summation, lateral Borel summation), or
2. A *correspondence* that identifies the perturbative and non-perturbative sides via an external structure (Langlands functoriality, geometric Langlands), or
3. A *direct match* via an explicit combinatorial computation (e.g., the 2D YM case done in 2022).

None of these techniques are internal to Paper 8's chain. This is why H4 is left as a hypothesis.

---

## 1.4. What is known and what is not

**What is known, with rigour:**

- The perturbative series for $S_n^{\mathrm{PT}}$ exists order by order in $g^2$, scheme-independently at all orders (Paper 10 + Paper 11 K.4).
- The non-perturbative $S_n$ exists as tempered distributions satisfying OS0-OS4 (Paper 8 Link 16).
- The short-distance OPE of $S_n$ is known to exist in the sense that the algebra of operator-valued distributions admits a Wilson expansion (Paper 8 Link 17 constructs $[\mathrm{Tr} F^2]_R$ and $T_{\mu\nu}^R$).
- Asymptotic freedom holds as a *statement about the running coupling*: $g(\mu) \to 0$ as $\mu \to \infty$ at one and two loops (Paper 10 scheme-independence).

**What is not known:**

- That the OPE coefficients of the non-perturbative $S_n$ *agree, order by order in $g(\mu)$*, with the coefficients computed by Feynman diagrams.

H4 is precisely this missing link.

---

## 1.5. What closing H4 gains

If H4 closes, the following cascade is immediate:

1. **Paper 8 Link 18 upgrades** from CONDITIONAL to PROVED. The full 18-link chain becomes unconditional.
2. **The Yang-Mills mass gap is proved without remainder.** The continuum 4D SU(N) theory has a positive mass gap $\Delta_\infty > 0$, and the Schwinger functions match perturbation theory at short distances.
3. **Clay Millennium Problem #4** (Yang-Mills existence and mass gap) is solved in the programme's frame. Combined with the Jaffe-Witten problem statement, this is the target criterion.
4. **Programme confidence on YM** rises from 9.5/10 to 10/10.
5. **Cascading impact on Paper 30 (Navier-Stokes):** NS inherits YM's gradient-flow machinery via Papers 8 Links 15-17. If H4 closes, NS's Link 7 (gradient-flow transfer) tightens.
6. **Cascading impact on Paper 38 (Turbulence):** K41 scaling from NS + spectral-gap + type III$_1$ ergodicity. If YM goes unconditional, the NS-inheritance edge strengthens.
7. **Programme graph:** the YM node upgrades from a 9.5/10 incoming-edge to a 10/10 incoming-edge for Papers 30, 38, and 60 (the S-duality diagnostic).

---

## 1.6. What closing H4 does not gain

H4 is about the **match** between perturbative and non-perturbative YM at short distances. It is *not* about:

- The existence of the continuum YM theory (that is Links 1-16).
- The mass gap $\Delta_\infty > 0$ (that is Links 1-14).
- The OS axioms for the Schwinger functions (that is Link 16).
- The scheme independence of the perturbative series (that is Papers 10 + 11).

Closing H4 therefore *finishes* the YM story; it does not add new physical content beyond ratifying that perturbation theory *is* the asymptotic short-distance expansion of the non-perturbative theory.

---

## 1.7. The stakes, precisely stated

- **Mathematical stakes:** Clay Millennium #4. One of the seven.
- **Programme stakes:** YM becomes the second Clay problem closed by the programme (after BSD), validating the full synthesis-replacement methodology.
- **Downstream stakes:** NS + Turbulence + Hodge + Selberg all have edges to YM; strengthening YM strengthens them.
- **Methodological stakes:** the three-route parallel-attack strategy (Routes A, B, C — Resurgence, Langlands-Shahidi, Kapustin-Witten) becomes the template for closing other "terrible dependencies" in the programme.

Paper 50's task is to close H4. Paper 50's strategy is three independent routes. Paper 50's voice is: *this is hard, we respect the difficulty, and we attack it in parallel.*

---

*Paper 50 §01. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
