# Node D — Dark-State Impossibility over Q(i)

**Chain step:** 4 of 11
**Rigor label:** [THEOREM]
**Dependencies:** Node C (ITPFI factorization)
**Status:** PROVED (algebraic form, revised 2026-04-10)

---

## Statement

For every Gaussian prime $\mathfrak{p}$ and every bridge index $k \geq 1$:

$$\omega_1^K(e_{\mathfrak{p}^k}) = N(\mathfrak{p})^{-k} > 0$$

where $e_{\mathfrak{p}^k} = s_\mathfrak{p}^k (s_\mathfrak{p}^k)^*$ is the range projection and $P_k^\mathfrak{p} = I - e_{\mathfrak{p}^k}$ is the bridge projector. No bridge is annihilated by the critical state $\omega_1^K$.

**This is a statement about the C\*-algebra and its KMS state, not about eigenstates of $\overline{T}_{BC,K}$.** The algebraic form bypasses the distributional-to-genuine spectrum upgrade (MY4) entirely.

---

## Proof

The ITPFI factorization (Node C) reduces to the $\mathfrak{p}$-local factor. On the $\mathfrak{p}$-local Fock space with basis $\{|n\rangle : n \geq 0\}$:

- $s_\mathfrak{p}|n\rangle = |n+1\rangle$
- $e_{\mathfrak{p}^k}$ acts as $\sum_{n \geq k} |n\rangle\langle n|$
- The local KMS$_1$ state is the Gibbs measure: $\omega_1^\mathfrak{p}(|n\rangle\langle n|) = (1 - N(\mathfrak{p})^{-1}) \cdot N(\mathfrak{p})^{-n}$

Summing:

$$\omega_1^\mathfrak{p}(e_{\mathfrak{p}^k}) = (1 - N(\mathfrak{p})^{-1}) \sum_{n \geq k} N(\mathfrak{p})^{-n} = N(\mathfrak{p})^{-k}$$

All other local factors give $1$ on the identity, so $\omega_1^K(e_{\mathfrak{p}^k}) = N(\mathfrak{p})^{-k}$.

### Extension to off-line deformations (Proposition 6.3)

For $\beta = 1 + 2\delta$: $\omega_{1+2\delta}^K(e_{\mathfrak{p}^k}) = N(\mathfrak{p})^{-k(1+2\delta)} < 1$, strictly positive for all $\delta > -1/2$. The bridge detects any hypothetical off-line deformation algebraically, without Meyer spectral inclusion.

### Numerical values on minimal-conductor rows

| $(k, N(\mathfrak{p}))$ | $\omega_1^K(e_{\mathfrak{p}^k})$ |
|:-:|:-:|
| $(2, 13)$ | $0.0059172$ |
| $(3, 13)$ | $0.0004552$ |
| $(4, 41)$ | $3.54 \times 10^{-7}$ |
| $(6, 29)$ | $1.68 \times 10^{-9}$ |

---

## Key insight (Remark 6.1.1)

The "every eigenstate couples" formulation in Paper 13 was rhetorical shorthand for "the KMS$_1$ state gives positive mass to each bridge projector." The algebraic form makes this precise. **This single change removes the Meyer spectral inclusion dependency from the proof chain.**

---

## Sources

- **Preprint:** sections-part-II.md §§6.1-6.3
- **Research:** route3-kms-projector-bypass.md (G's projector bypass), 04-four-verifications-qi.md (Verification 3)
- **Computational:** referee/code/test_projector_P.py (40-digit verification)
- **Referee:** checks/DS-dark-states/DS1-DS2
