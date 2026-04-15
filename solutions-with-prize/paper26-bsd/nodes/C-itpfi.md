# Node C — ITPFI Factorization over Q(i)

**Chain step:** 3 of 11
**Rigor label:** [LEMMA]
**Dependencies:** Node A (KMS$_1$ uniqueness)
**Status:** PROVED

---

## Statement

The unique KMS$_1$ state $\omega_1^K$ on $\mathcal{A}_{BC,K}$ for $K = \mathbb{Q}(i)$ factors as an infinite tensor product over Gaussian primes:

$$\omega_1^K = \bigotimes_{\mathfrak{p}\,\text{prime}} \omega_1^{\mathfrak{p}}$$

where $\omega_1^{\mathfrak{p}}$ is the unique KMS$_1$ state on the local algebra $\mathcal{A}_\mathfrak{p}^K$. Equivalently, at the von Neumann algebra level: $M_1^K = \overline{\bigotimes}_\mathfrak{p} M_\mathfrak{p}^K$ where each $M_\mathfrak{p}^K$ is a type III$_{1/N(\mathfrak{p})}$ factor.

---

## Proof sketch

**First argument (KMS uniqueness):**

1. Each local algebra $\mathcal{A}_\mathfrak{p}^K$ has a unique KMS$_1$ state $\omega_1^\mathfrak{p}$ (Laca-Raeburn 1996).
2. The product state $\omega := \bigotimes_\mathfrak{p} \omega_1^\mathfrak{p}$ is KMS$_1$ on the full algebra (Bratteli-Robinson, Proposition 5.3.23).
3. KMS$_1$ on $\mathcal{A}_{BC,K}$ is unique (Proposition 3.4, $h_K = 1$).
4. Therefore $\omega_1^K = \bigotimes_\mathfrak{p} \omega_1^\mathfrak{p}$.

**Second argument (Euler product):**

The multiplicativity $Z_K(\beta) = \prod_\mathfrak{p} Z_\mathfrak{p}(\beta)$ of the partition function induces the state factorization at every $\beta > 1$, and by continuity at $\beta = 1$.

**No class group obstruction:** $h_K = 1$ means $\mathbb{Z}[i]$ is a PID, every ideal is principal, and every prime ideal contributes an independent tensor factor. For $h_{K'} > 1$, ideals in the same class would be identified, potentially obstructing the tensor product. Holds for all nine class-number-1 imaginary quadratic fields.

---

## What changes from Q to Q(i)

Nothing. The three-step argument is verbatim identical. The only field-dependent input is KMS$_1$ uniqueness, which requires $h_K = 1$.

---

## Sources

- **Preprint:** sections-part-II.md §§5.1-5.4
- **Research:** 04-four-verifications-qi.md (Verification 2)
- **Literature:** Laca-Raeburn 1996, Bratteli-Robinson 5.3.23, Araki-Woods ITPFI classification
- **Referee:** checks/IT-itpfi/IT1
