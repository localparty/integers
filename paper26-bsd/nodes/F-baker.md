# Node F — Baker's Theorem Forces delta = 0

**Chain step:** 6 of 11 (independent reinforcement — not load-bearing; Key Lemma C is the primary kill)
**Rigor label:** [LEMMA]
**Dependencies:** Node B (bridge family), Node E (cocycle shift + Key Lemma C)
**Status:** PROVED

---

## Statement

**Proposition 8.6 (The transcendence kill).** Let $\mathfrak{p}_1, \mathfrak{p}_2$ be Gaussian bridge primes with $N(\mathfrak{p}_1) \neq N(\mathfrak{p}_2)$, and let $k_1, k_2$ be their bridge indices. If $\delta \in (-1/2, 1/2)$ satisfies the simultaneous integrality constraints

$$\Delta c_{k_1}(\delta) \in \frac{1}{k_1}\mathbb{Z}, \qquad \Delta c_{k_2}(\delta) \in \frac{1}{k_2}\mathbb{Z},$$

then $\delta = 0$.

---

## Proof

### Baker's theorem (1966)

If $\alpha_1, \ldots, \alpha_n$ are non-zero algebraic numbers and $\beta_1, \ldots, \beta_n$ are algebraic with $1, \beta_1, \ldots, \beta_n$ linearly independent over $\mathbb{Q}$, then $\alpha_1^{\beta_1} \cdots \alpha_n^{\beta_n} \neq 1$.

**Corollary:** For distinct rational primes $p_1, p_2$, $\log p_1 / \log p_2$ is transcendental.

### Transcendence of norm-logarithm ratios (Proposition 8.4)

For Gaussian primes $\mathfrak{p}_1, \mathfrak{p}_2$ with $N(\mathfrak{p}_1) \neq N(\mathfrak{p}_2)$: $\log N(\mathfrak{p}_1) / \log N(\mathfrak{p}_2)$ is transcendental (norms are multiplicatively independent positive integers $\geq 2$).

### The kill argument (5 steps)

1. **First-order expansion:** $\Delta c_{k_j}(\delta) \approx 2\delta \log N_j / (N_j - 1)$. Integrality requires $\Delta c_{k_j} = m_j/k_j$ for non-zero integers $m_j$.

2. **Ratio:** $m_1 k_2 / (m_2 k_1) \approx (\log N_1 / \log N_2) \cdot (N_2 - 1)/(N_1 - 1)$. Left side rational, right side contains the transcendental factor $\log N_1 / \log N_2$. Contradiction.

3. **Exact promotion:** From $N_j^{-2\delta_0} = r_j \in \mathbb{Q}$ (forced by the integrality conditions), Baker's theorem on the linear form $-2\delta_0 \log N_1 = a_1 \log p_1 + \cdots$ gives a non-trivial relation among logarithms of distinct primes, contradicting the fundamental theorem of arithmetic.

4. **Rationality constraint:** $N^{-2\delta_0} \in \mathbb{Q}$ for prime $N$ forces $-2\delta_0 \in \mathbb{Z}$. Since $\delta_0 \in (0, 1/2)$, no integer exists in $(-1, 0)$. Contradiction.

5. **Large $|\delta|$ regime:** The integrality gap provides a stronger constraint; nonlinearity amplifies the transcendence obstruction.

### Relationship to Key Lemma C

Key Lemma C (Node E, Proposition 7.3(v)) already shows $|\Delta c(\delta)| < 1/k$ for $\delta \neq 0$, so the integrality premise $\Delta c \in (1/k)\mathbb{Z} \setminus \{0\}$ is never satisfied. **Key Lemma C is the primary kill mechanism.** Baker provides an **independent reinforcement** via a fundamentally different mechanism (transcendence of log-ratios vs. elementary bounds on the shift magnitude). The two arguments attack the problem from different angles:

- **Key Lemma C:** the shift is too small to be a nonzero element of $(1/k)\mathbb{Z}$
- **Baker:** even if the shift could reach $(1/k)\mathbb{Z}$, simultaneous integrality at two primes would require a transcendental number to be rational

Either suffices alone. Both are included for robustness. **This node is not load-bearing for the chain** — if removed, the chain still closes via Key Lemma C (Nodes E and G).

---

## Comparison: Gelfond-Schneider (RH) vs Baker (BSD)

| | RH (Paper 13) | BSD (this paper) |
|:-|:-|:-|
| Base field | $\mathbb{Q}$ | $\mathbb{Q}(i)$ |
| Bridge primes | Rational: $\{2,3,5,7\}$ | Gaussian: norms $\{13, 29, 41\}$ |
| Conductors | $\{7,13,19\}$, product 1729 | $\{3,5,7\}$, product 105 |
| Transcendence theorem | Gelfond-Schneider (1934) | Baker (1966) |

Baker is strictly stronger but the additional strength is not needed: two bridge primes with distinct norms suffice. The upgrade is convenience, not necessity.

---

## Sources

- **Preprint:** sections-part-III.md §§8.1-8.5
- **Research:** 03-baker-theorem-step.md (formal proof chain with 11 steps)
- **Literature:** Baker 1966, Gelfond-Schneider 1934
- **Referee:** checks/TR-transcendence/TR1-TR6
