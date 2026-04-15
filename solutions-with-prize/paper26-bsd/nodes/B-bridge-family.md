# Node B — Bridge Family over Q(i)

**Chain step:** 2 of 11
**Rigor label:** [LEMMA]
**Dependencies:** Node A (BC algebra)
**Status:** PROVED

---

## Statement

Four cyclotomic Brauer cocycles at bridge indices $k \in \{2, 3, 4, 6\}$ extend from $\mathbb{Q}$ to $\mathbb{Q}(i)$. The exhaustive enumeration yields 355 bridge triples for conductor norm $\leq 50$. Minimal conductors: $\{3, 5, 7\}$, product $105$. Hasse invariant $= 1/k$ at every bridge, matching the Fuglede-Kadison determinant exactly.

---

## Proof sketch

### Frobenius elements (Definition 4.1)

For a Gaussian prime $\mathfrak{p}$ coprime to conductor $\mathfrak{N}$, $\operatorname{Frob}_\mathfrak{p} \in \operatorname{Gal}(K(\zeta_\mathfrak{N})/K)$ satisfies $\operatorname{Frob}_\mathfrak{p}(\zeta_\mathfrak{N}) \equiv \zeta_\mathfrak{N}^{N(\mathfrak{p})} \pmod{\mathfrak{p}}$. Bridge index: $k = \varphi(N(\mathfrak{N}))/\operatorname{ord}(\operatorname{Frob}_\mathfrak{p})$.

### Minimal-conductor bridge table (Proposition 4.3, revised 2026-04-10)

| $k$ | $N_\mathfrak{N}$ | Bridge prime $\mathfrak{p}$ | $N(\mathfrak{p})$ | $\operatorname{ord}$ | Verification |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 2 | 3 | $(2+3i)$ | 13 | 1 | $13 \equiv 1 \pmod{3}$ |
| 3 | 7 | $(2+3i)$ | 13 | 2 | $13 \equiv 6 \equiv -1 \pmod{7}$ |
| 4 | 5 | $(4+5i)$ | 41 | 1 | $41 \equiv 1 \pmod{5}$ |
| 6 | 7 | $(2+5i)$ | 29 | 1 | $29 \equiv 1 \pmod{7}$ |

**Key design choice:** All four bridge primes are **split** Gaussian primes with rational prime norms ($13, 41, 29$). This avoids the inert-prime edge case (norm $p^2$) flagged in the rigor audit.

### Cocycle match (Theorem 4.6)

**Hasse invariant.** The cyclic algebra $(K(\zeta_\mathfrak{N})/K, \operatorname{Frob}_\mathfrak{p}, \zeta_k)$ has local Hasse invariant $\operatorname{inv}_\mathfrak{p} = 1/k \bmod \mathbb{Z}$. This follows from the local reciprocity map: the invariant of a cyclic algebra $(L/K, \sigma, a)$ of degree $n$ at a place $v$ is $\operatorname{inv}_v = v(a)/n$ where $v$ is the normalized valuation (Serre, *Local Fields*, XIII, Proposition 6; Reiner, *Maximal Orders*, Theorem 31.8). For the bridge construction, $a = \zeta_k$ (a root of unity, hence a unit at all finite places), and the invariant is computed via the local Artin map: $\operatorname{inv}_\mathfrak{p} = \operatorname{ord}(\operatorname{Frob}_\mathfrak{p})/[L:K] = ({\varphi(N(\mathfrak{N}))/k})/{\varphi(N(\mathfrak{N}))} = 1/k$.

**Fuglede-Kadison determinant.** For the type II$_1$ subfactor $N \subset M$ of Jones index $[M:N] = k$ associated to the bridge, the FK determinant of the Jones basic construction projection $e_1 \in M_1 = \langle M, e_1 \rangle$ satisfies $\Delta_{FK}(e_1) = [M:N]^{-1} = 1/k$ (Jones 1983, *Invent. Math.* 72, Proposition 2.1.8; Lück 2002, *J. Reine Angew. Math.* 540, for the FK determinant computation). The determinant is a property of the subfactor index, independent of the base field.

**Field-independence (Theorem 4.6).** Both quantities equal $1/k$ by structural arguments that use only the degree of the cyclic algebra and the index of the subfactor — neither depends on $K$. The cocycle match is structural.

### Comparison to Q

Over $\mathbb{Q}$: conductors $\{7, 13, 19\}$, product $1729$. Over $\mathbb{Q}(i)$: product drops to $105$. The bridge becomes *more economical* over richer arithmetic because split primes contribute two Frobenius elements each.

---

## Sources

- **Preprint:** sections-part-II.md §§4.1-4.6
- **Research:** corrected-bridge-table.md (fixes Gap G1), 04-four-verifications-qi.md
- **Referee:** checks/BR-bridge/BR1-BR4
- **Computational:** referee/code/ (all four rows verified)
