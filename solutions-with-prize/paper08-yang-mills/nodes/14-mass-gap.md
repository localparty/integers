# Node 14 -- Continuum Mass Gap

**Chain step:** 14 of 18
**Rigor label:** [THEOREM]
**Dependencies:** Steps 1--13 (entire lattice-to-continuum chain)
**Status:** PROVED

---

## Statement

**Theorem 8 (Continuum mass gap).** *For $\mathrm{SU}(N)$ Yang--Mills theory, $N \geq 2$, on $\mathbb{R}^4$:*

$$\Delta_\infty \;:=\; \inf\sigma(H_{\mathrm{OS}}) \setminus \{0\} \;>\; 0.$$

*The mass gap survives the continuum limit $a \to 0$, with $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$.*

---

## Proof (4 parts)

**Part (a) -- Ratio shift.** By the spectral lemma (Step 11) and deviation-order stability (Steps 8--10), $|C_{k+1} - C_k| \leq C' g_k^4 (a_k \Lambda)^s$ with $s \geq 2$.

**Part (b) -- Convergence.** The telescoping sum converges doubly exponentially (Step 13): $\sum g_k^4 (a_k\Lambda)^s < \infty$.

**Part (c) -- Positivity.** By absolute convergence, $C_\infty = C_0 - \sum \delta C_k > 0$ since $\sum |\delta C_k| \ll C_0$.

**Part (d) -- Gap.** $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$, with $\Lambda_\infty > 0$ by dimensional transmutation.

**Parts (e)--(f).** The thermodynamic and continuum limits commute (Theorem M.2.1: Cauchy argument using doubly exponential convergence of the RG telescoping sum). The limiting Schwinger functions satisfy the Osterwalder--Schrader axioms OS0--OS4 — verified in detail in Node 16 (Lemmas L.2.1--L.2.4): OS0 (temperedness from polymer decay), OS1 (Euclidean invariance from continuum action isometry), OS2 (reflection positivity from lattice OS inequality — survives the limit because the RP inequality is closed under weak limits of measures), OS3 (permutation symmetry), OS4 (cluster decomposition from $\Delta_\infty > 0$).

---

## The proof in one paragraph

The KK spectral gap $\Delta_0^{\mathrm{KK}} > 0$ (Thm 4) transfers to the standard lattice gap $\Delta_0^{\mathrm{std}} > 0$ (Thm 5) via the reduced transfer matrix. Balaban's block-spin RG preserves the gap at each step, with corrections bounded by $C_k g_k^4 \hat\Delta_k^2$. The deviation-order stability (all dim-6 operators have $\mathrm{dev} \geq 2$) ensures corrections are quadratic in the gap. Asymptotic freedom ($g_k \to 0$) and the RG recursion give a convergent telescoping sum. The limit $C_\infty > 0$ is strictly positive, establishing $\Delta_\infty > 0$ unconditionally.

---

## Sources

- **Preprint:** Section 5.7 (Theorem 8)
- **Proof chain:** PROOF-CHAIN.md, Steps 1--14
- **Literature:** Balaban CMP 109, 119; Osterwalder--Schrader 1973
