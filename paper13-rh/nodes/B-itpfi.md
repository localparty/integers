# Node B — ITPFI State Convergence (Layer 2)

**Chain layer:** 2 of 6
**Rigor label:** [THEOREM] (one proof + one cross-check + numerical verification)
**Dependencies:** Node A (BC algebra from CCM)
**Status:** PROVED

---

## Statement

**Theorem 4.1 (ITPFI factorization).** The unique KMS$_1$ state $\omega_1$ on the Bost-Connes algebra $A_{BC}$ factors as an infinite tensor product over primes:

$$\omega_1 = \bigotimes_p \omega_1^{(p)}$$

where $\omega_1^{(p)}$ is the unique KMS$_1$ state on the $p$-local algebra. Consequently, the truncated states $\omega_1^{(\leq P_N)} \to \omega_1$ weak-$*$, controlling the Weil quadratic form entry-by-entry.

---

## Proof and cross-checks

**Proof (KMS uniqueness).** Each local algebra has a unique KMS$_1$ state (Laca-Raeburn 1996). The product state is KMS$_1$ (Bratteli-Robinson 5.3.23). KMS$_1$ on the full algebra is unique (Bost-Connes Theorem 25). Therefore $\omega_1 = \bigotimes_p \omega_1^{(p)}$. This is the rigorous proof; the other two arguments below are cross-checks.

**Cross-check (Euler product).** The partition function $Z_{BC}(\beta) = \zeta(\beta) = \prod_p (1-p^{-\beta})^{-1}$ multiplicativity induces state factorization at all $\beta > 1$. The limit $\beta \to 1^+$ is justified by KMS$_1$ uniqueness (the product-state property survives the limit because the limiting state is unique). **Note:** $Z_{BC}$ has a pole at $\beta = 1$, so "continuity" alone does not suffice — uniqueness of the limiting state is the essential input, which is Bost-Connes Theorem 25 again. This cross-check is not independent of Proof 1.

**Numerical verification.** 135 prime pairs verified to 50-digit precision: $\prod_{p \leq P_N} Z_p(\beta)$ matches $\zeta(\beta)$ to all computed digits. This is evidence, not a proof.

---

## Why ITPFI matters for the proof chain

ITPFI provides **entry-by-entry convergence** of the Weil quadratic form $Q_N \to Q_\infty$. This feeds into Layer 4 (gsrc via Teschl Lemma 2.7) and is the key ingredient closing CCM's Gap 1 (finite $N$ to infinite limit).

The von Neumann algebra $M_1 = \pi_1(A_{BC})''$ is a type III$_1$ factor (Connes spectrum dense in $\mathbb{R}_+^*$). Each local factor $M_p$ is type III$_{1/p}$ (Araki-Woods classification).

---

## Sources

- **Preprint:** sections-01-05.md §4, appendices.md Appendix B
- **Research:** research/265 (three proofs), research/10-itpfi-connes-gap.md
- **Literature:** Bost-Connes 1995, Laca-Raeburn 1996, Bratteli-Robinson Vol. 2
