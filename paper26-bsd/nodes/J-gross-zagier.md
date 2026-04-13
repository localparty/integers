# Node J — Gross-Zagier Formula (Rank 1)

**Chain step:** 10 of 11
**Rigor label:** [THEOREM]
**Dependencies:** Node G (GRH), Node H (CM factorization)
**Status:** KNOWN (classical) — vacuous within scope (Remark 12.6)

---

## Statement

**Theorem 12.1 (Gross-Zagier 1986).** Let $E/\mathbb{Q}$ be modular of conductor $N$, and $K$ an imaginary quadratic field satisfying the Heegner hypothesis (every prime dividing $N$ splits in $K$). Let $P_K \in E(K)$ be the Heegner point. Then:

$$L'(E/K, 1) = c_{E,K} \cdot \hat{h}(P_K)$$

where $\hat{h}$ is the Neron-Tate height and $c_{E,K}$ is an explicit non-zero constant.

---

## Application: analytic rank 1 implies algebraic rank 1

**Corollary 12.2.** If $L'(E, 1) \neq 0$ (analytic rank 1), then $\hat{h}(P_K) \neq 0$, so $P_K$ has infinite order and $\operatorname{rank}(E(K)) \geq 1$.

**Theorem 12.3 (Kolyvagin, rank 1).** If a Heegner point of infinite order exists, then $\operatorname{rank}(E(K)) = 1$ and $\operatorname{Sha}(E/K)$ is finite.

Combined: $L'(E,1) \neq 0 \implies \operatorname{rank}(E(K)) = 1$, $|\operatorname{Sha}| < \infty$.

---

## Heegner hypothesis fix

For $E: y^2 = x^3 - x$ (conductor $N = 32$), the classical Heegner hypothesis fails: $2$ ramifies in $\mathbb{Q}(i)$.

**Fix:** Use the auxiliary field $\mathbb{Q}(\sqrt{-7})$ (discriminant $-7$, coprime to 32). The prime 2 splits in $\mathbb{Q}(\sqrt{-7})$ since $-7 \equiv 1 \pmod{8}$. Alternatively, cite Yuan-Zhang-Zhang 2013 (*Annals of Mathematics Studies* 191) for the generalized Gross-Zagier formula removing the Heegner hypothesis.

---

## Vacuity within scope (Remark 12.6)

GRH for $L(s, \psi)$ implies $L(1, \psi) \neq 0$, hence $L(E, 1) \neq 0$ for **every** CM curve in scope. Analytic rank is always 0. There are no rank-1 cases.

Theorem 12.5 (BSD rank 1 for CM curves) is a valid conditional with vacuously satisfied hypothesis — included for logical completeness and because the argument is instructive. CM curves *can* have positive rank over larger number fields (e.g., over $K$ itself via base change), but this is not addressed here.

---

## Leading coefficient formula (rank 1)

$$\frac{L'(E, 1)}{\hat{h}(P)} = \frac{|\operatorname{Sha}| \cdot \Omega_E \cdot \prod_p c_p \cdot R_E}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

Gross-Zagier provides the bridge $L'(E,1) \leftrightarrow \hat{h}(P_K)$; Kolyvagin's finiteness of Sha closes the formula.

---

## Sources

- **Preprint:** sections-part-IV.md §§12.1-12.4
- **Literature:** Gross-Zagier 1986 (*Invent. Math.* 84), Yuan-Zhang-Zhang 2013, Kolyvagin 1990
- **Referee:** checks/GZ-gross-zagier/GZ*
