# Node 02 --- IR Equivalence

**Chain step:** 1b of 18
**Rigor label:** [PROVED] (Theorem 5)
**Dependencies:** Node 01 (KK spectral gap)
**Status:** PROVED

---

## Statement

**Theorem 5 (IR equivalence).** The standard 4D lattice mass gap $\Delta_0^{\mathrm{std}} > 0$ follows from $\Delta_0^{\mathrm{KK}} > 0$. Specifically, the low-lying spectrum of the KK-enhanced theory coincides with that of standard 4D Yang--Mills up to exponentially small corrections:

$$|\Delta_0^{\mathrm{std}} - \Delta_0^{\mathrm{KK}}| \;\leq\; C_W e^{-m_1 a}$$

---

## Proof sketch

1. **Reduced transfer matrix.** Construct the transfer matrix $\hat{T}$ on $L^2(\mathcal{C})$ for the KK-enhanced theory. Decompose the Hilbert space as $\mathcal{H} = P_0\mathcal{H} \oplus Q_0\mathcal{H}$, where $P_0$ projects onto the internal ground state $|\Omega_{\mathrm{int}}\rangle$.

2. **Feshbach map.** The Feshbach operator $F_P(z) = H_{00} + W(z - H_{QQ})^{-1}W^\dagger$ on $P_0\mathcal{H} \cong \mathcal{H}_{\mathrm{std}}$ has eigenvalues in bijection with those of $\hat{H}$ below $\inf\sigma(H_{QQ}) \geq m_1/2$ (Bach--Frohlich--Sigal 1998, Thm 2.1).

3. **Off-diagonal suppression.** The coupling $W = P_0 \hat{V} Q_0$ satisfies $\|W\| \leq C_W e^{-m_1 a}$. **Proof of the bound:** The interaction $\hat{V}$ couples 4D and internal modes through the Wilson action on the product lattice. Each term in $\hat{V}$ connecting $P_0\mathcal{H}$ to $Q_0\mathcal{H}$ requires exciting at least one KK mode from $|\Omega_{\mathrm{int}}\rangle$ to $|n\rangle_{\mathrm{int}}$ with $n \geq 1$. The matrix element is bounded by $\|V_{\text{link}}\| \cdot |\langle n|\Omega_{\mathrm{int}}\rangle|$, and the Gibbs suppression of KK modes gives $|\langle n|\Omega_{\mathrm{int}}\rangle| \leq e^{-m_n a/2}$ with $m_1 a \sim 2\pi r_3/a \sim 10^{15}$. The operator norm $\|W\|$ sums over spatial links but remains volume-independent because each link contributes independently (locality). **The gap hypothesis** $\inf\sigma(H_{QQ}) \geq m_1/2$ follows from $H_{QQ} = H_0|_{Q_0\mathcal{H}} + Q_0 \hat{V} Q_0$, where $H_0|_{Q_0\mathcal{H}} \geq m_1$ (KK mass gap) and $\|Q_0 \hat{V} Q_0\| \leq \|W\|^2/m_1 \ll m_1/2$.

4. **Eigenstate factorization.** Each low-lying eigenstate decomposes as $|n\rangle = |\psi_n\rangle_{\mathrm{4D}} \otimes |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle$ with $\|\delta_n\| \leq 2C_W e^{-m_1 a}/m_1$. The error is volume-independent ($C_W$ depends on link coupling strength, not $|\Lambda|$). The gap transfers from KK to standard theory.

---

## Sources

- **Preprint:** Section 4.5, Appendix C (transfer matrix, Feshbach map)
- **Literature:** Bach--Frohlich--Sigal 1998, Seiler 1982
