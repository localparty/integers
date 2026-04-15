# Node H — CM Factorization (Deuring)

**Chain step:** 8 of 11
**Rigor label:** [THEOREM]
**Dependencies:** None (classical, literature result)
**Status:** KNOWN

---

## Statement

**Theorem 10.1 (CM factorization).** Let $E/\mathbb{Q}$ have CM by $K$ with $h_K = 1$. Then

$$L(E, s) = L(s, \psi) \cdot L(s, \bar{\psi})$$

where $L(s, \psi)$ is the Hecke L-function of the Grossencharacter $\psi$ attached to $E$.

For $E: y^2 = x^3 - x$ with CM by $\mathbb{Q}(i)$:

$$L(E, s) = L(s, \chi_{-4}) \cdot L(s, \psi)$$

where $\chi_{-4} = (-4/\cdot)$ is the Kronecker character modulo 4.

---

## Key facts

1. **Complex multiplication** means $\operatorname{End}(E) \otimes \mathbb{Q} \cong K$ — the curve admits extra symmetries from the arithmetic of $K$. For $E: y^2 = x^3 - x$: $[i]: (x,y) \mapsto (-x, iy)$ squares to $[-1]$, $j = 1728$.

2. **GL$_2$ reduces to GL$_1$.** The Hecke Grossencharacter $\psi: I_K/K^\times \to \mathbb{C}^\times$ satisfies $\psi(\mathfrak{p}) = \pi_\mathfrak{p}$ (Frobenius endomorphism). This is class field theory, not Langlands.

3. **Euler product identity.** At each prime $p$ of good reduction:

$$\frac{1}{1 - a_p p^{-s} + p^{1-2s}} = \prod_{\mathfrak{p}|p} \frac{1}{1 - \psi(\mathfrak{p}) N(\mathfrak{p})^{-s}}$$

4. **Modularity is classical for CM.** CM curves are modular by the Hecke theta series $f(z) = \sum_{\mathfrak{a}} \psi(\mathfrak{a}) e^{2\pi i N(\mathfrak{a}) z}$, predating Wiles by decades.

5. **Nine class-number-1 fields:** $d \in \{-1, -2, -3, -7, -11, -19, -43, -67, -163\}$.

---

## Why this matters for BSD

Deuring gives $L(E,s) = L(s,\psi) \cdot L(s,\bar\psi)$. The bridge family (Nodes A-G) establishes GRH for $L(s,\psi)$. The combination: GRH for $L(E,s)$. **This is the bridge from the operator-algebraic world to the elliptic curve world.**

For non-CM curves, one would need a GL$_2$ analogue of the BC system — essentially the Langlands programme. This lies beyond the present construction.

---

## Sources

- **Preprint:** sections-part-IV.md §§10.1-10.4
- **Literature:** Deuring 1953, Silverman 1994 (Advanced Topics Ch. II), Shimura 1971
- **Referee:** checks/CM-cm-factorization/CM1
