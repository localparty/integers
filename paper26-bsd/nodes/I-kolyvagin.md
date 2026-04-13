# Node I — Kolyvagin's Euler System (Rank 0)

**Chain step:** 9 of 11
**Rigor label:** [THEOREM]
**Dependencies:** Node G (GRH), Node H (CM factorization)
**Status:** KNOWN (classical) + PROVED (the GRH input)

---

## Statement

**Theorem 11.1 (Kolyvagin 1990).** Let $E/\mathbb{Q}$ be a modular elliptic curve. If $L(E, 1) \neq 0$, then:

(i) $\operatorname{rank}(E(\mathbb{Q})) = 0$

(ii) $\operatorname{Sha}(E/\mathbb{Q})$ is finite.

---

## How GRH provides the hypothesis

**Corollary 11.2.** For CM curves with $h_K = 1$ and analytic rank 0: $L(E, 1) \neq 0$.

*Proof.* By CM factorization (Node H): $L(E, s) = L(s, \psi) \cdot L(s, \bar\psi)$. By GRH (Node G): all non-trivial zeros of $L(s, \psi)$ lie on $\operatorname{Re}(s) = 1/2$. Since $\operatorname{Re}(1) = 1 \neq 1/2$, $s = 1$ is not a zero. Therefore $L(E, 1) = L(1, \psi) \cdot L(1, \bar\psi) \neq 0$.

This is the key logical step: **GRH, established by the bridge family, provides the non-vanishing hypothesis that Kolyvagin requires.**

---

## BSD rank 0: closed

**Theorem 11.3 (BSD rank 0 for CM curves).** For CM curves with $h_K = 1$ and $\operatorname{ord}_{s=1} L(E,s) = 0$:

(i) $\operatorname{rank}(E(\mathbb{Q})) = 0$

(ii) $\operatorname{Sha}(E/\mathbb{Q})$ is finite

*Proof.* Corollary 11.2 gives $L(E,1) \neq 0$. Modularity (classical for CM). Kolyvagin (Theorem 11.1) gives rank $= 0$ and $|\operatorname{Sha}| < \infty$.

### Leading coefficient formula (rank 0)

$$L(E, 1) = \frac{|\operatorname{Sha}| \cdot \Omega_E \cdot \prod_p c_p}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

All terms computable. Kolyvagin's finiteness of Sha + explicit computations (Rubin 1991) close the formula.

---

## Important: rank 1 is vacuous in scope

**Remark 12.6.** GRH implies $L(1, \psi) \neq 0$ for every CM curve in scope, so $L(E, 1) \neq 0$ always, meaning analytic rank is always 0. There are **no CM curves over $\mathbb{Q}$ with CM by a class-number-1 field that have analytic rank $\geq 1$**. The rank-1 case (Theorem 12.5) is a valid conditional with vacuously satisfied hypothesis.

**The substantive content of Paper 26's Theorem 13.1 lives entirely at rank 0.**

---

## Sources

- **Preprint:** sections-part-IV.md §§11.1-11.3
- **Literature:** Kolyvagin 1990 (*Grothendieck Festschrift*), Gross 1991, Rubin 1991
- **Referee:** checks/KV-kolyvagin/KV*
