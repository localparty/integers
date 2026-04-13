# Node A — Bost-Connes System over Q(i)

**Chain step:** 1 of 11
**Rigor label:** [LEMMA]
**Dependencies:** None (base case)
**Status:** PROVED

---

## Statement

The Ha-Paugam C*-algebra $\mathcal{A}_{BC,K} = C^*(\widehat{\mathcal{O}_K}) \rtimes \mathcal{I}_K$ for $K = \mathbb{Q}(i)$ is well-defined, with time evolution $\sigma_t(e_\mathfrak{a}) = N(\mathfrak{a})^{it} e_\mathfrak{a}$. It admits a **unique** KMS$_1$ state $\omega_1^K$ because $h_K = 1$.

---

## Proof sketch

1. **Construction.** Ha-Paugam 2005 (arXiv:math/0507101) builds $\mathcal{A}_{BC,K}$ as a semigroup crossed product for any number field $K$. Over $\mathbb{Q}$, this reduces to the original Bost-Connes algebra $C(\hat{\mathbb{Z}}) \rtimes \mathbb{N}^\times$.

2. **Gaussian integers.** $\mathbb{Z}[i]$ is a Euclidean domain (norm $N(a+bi) = a^2 + b^2$), hence a PID with unique factorization. Gaussian primes: split ($p \equiv 1 \pmod{4}$, norm $p$), inert ($p \equiv 3 \pmod{4}$, norm $p^2$), ramified ($p = 2$, norm $2$).

3. **Dedekind zeta function.** $\zeta_K(s) = \prod_\mathfrak{p} (1 - N(\mathfrak{p})^{-s})^{-1}$ with residue $\operatorname{Res}_{s=1} \zeta_K(s) = \pi/4$.

4. **KMS$_1$ uniqueness.** Laca-Larsen-Neshveyev 2015 establishes uniqueness for number fields with **narrow class number one**. For $K = \mathbb{Q}(i)$ (and all imaginary quadratic fields), the narrow class number equals the class number: there are no real embeddings, so every totally positive element is simply a nonzero element, and $\operatorname{Cl}^+(K) = \operatorname{Cl}(K)$. Since $h_K = 1$, we have $h_K^+ = 1$, so the LLN hypothesis is met. The unique KMS$_1$ state is the trace state normalized by the pole.

5. **GNS construction.** The GNS triple $(\pi_1^K, H_{1,K}, \Omega_1^K)$ yields a type III$_1$ factor $M_1^K = \pi_1^K(\mathcal{A}_{BC,K})''$, with modular automorphism group $\sigma_t^{\omega_1^K} = \sigma_t$ (Takesaki's theorem). Type III$_1$ follows from the Connes spectrum: $S(M_1^K) = \overline{\{N(\mathfrak{p})^{it}\}} = \mathbb{R}_+^*$.

6. **Nelson self-adjointness.** The GNS vectors $\pi_1^K(\mu_\mathfrak{a})\Omega_1^K$ are entire analytic vectors for $T_{BC,K} = \overline{L_K}$ (the closure of $L_K f(\mathfrak{a}) = \log N(\mathfrak{a}) \cdot f(\mathfrak{a})$), because $\cosh(t \cdot \log N(\mathfrak{a})) < \infty$ for all $t \in \mathbb{R}$. By Nelson's theorem (Reed-Simon X.39), $T_{BC,K}$ is essentially self-adjoint.

7. **Tautological partition function.** $Z_{BC,K}(\beta) = \sum_\mathfrak{a} N(\mathfrak{a})^{-\beta} = \zeta_K(\beta)$. A zero of $\zeta_K(s)$ at $s_0 = 1/2 + \delta + it$ is a zero of $Z_{BC,K}$ at $\beta_0 = 1 + 2\delta + 2it$. No spectral interpretation required.

---

## What changes from Q to Q(i)

Nothing substantive. The construction, KMS uniqueness argument, GNS type classification, Nelson self-adjointness, and partition function identity all transfer verbatim with $p \mapsto N(\mathfrak{p})$.

---

## Sources

- **Preprint:** sections-part-II.md §§3.1-3.7
- **Research:** meyer-extension-to-K.md (Key Lemma A for Meyer extension)
- **Literature:** Ha-Paugam 2005, Laca-Larsen-Neshveyev 2015, Bost-Connes 1995, Reed-Simon X.39
- **Referee:** checks/BC-bost-connes/BC1-BC5
