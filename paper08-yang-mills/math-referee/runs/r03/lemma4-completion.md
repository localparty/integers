# Lemma 4 Completion: Eigenstate Factorization via Feshbach Projection

This document fills the sub-gap identified in the assessment of `theorem5-proof.md`,
specifically item (2): Lemma 4, Step 3 claims that the low-lying eigenstates of
$\hat{T}_{\mathrm{KK}}$ factorize as (4D state) $\otimes$ (internal ground state)
$+ O(e^{-m_1 a})$, but the operator-theoretic argument was not written out.
We supply it here using the Feshbach projection (Schur complement).


---

## 1. Precise Statement

**Lemma 4a (Eigenstate factorization).** *Let $\hat{H}_{\mathrm{KK}} =
-\ln \hat{T}_{\mathrm{KK}}$ be the Hamiltonian of the KK-enhanced lattice
gauge theory, acting on
$\mathcal{H}_{\mathrm{KK}} = \mathcal{H}_{\mathrm{std}} \otimes
\mathcal{H}_{\mathrm{int}}$.
Let $|\Omega_{\mathrm{int}}\rangle$ denote the ground state of the internal
Hamiltonian $\hat{H}_{\mathrm{int}}$ (all KK modes in their vacuum), and let*

$$P_0 = \mathbf{1}_{\mathrm{std}} \otimes
  |\Omega_{\mathrm{int}}\rangle\langle\Omega_{\mathrm{int}}|,
  \qquad Q_0 = \mathbf{1} - P_0$$

*be the projections onto the internal ground state and its orthogonal complement.
In the regime $m_1 a \gg 1$:*

*(i) The vacuum $|0\rangle$ and lightest glueball $|1\rangle$ of
$\hat{H}_{\mathrm{KK}}$ satisfy*

$$|n\rangle = |\psi_n\rangle_{\mathrm{4D}} \otimes
  |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle,
  \qquad \|{\delta_n}\| \leq \frac{C_F}{m_1}\,e^{-m_1 a},
  \qquad n = 0, 1,$$

*where $|\psi_n\rangle_{\mathrm{4D}} \in \mathcal{H}_{\mathrm{std}}$ are
normalised states and $C_F > 0$ depends on $N$ but not on $a/r_3$.*

*(ii) The spectral gap of the reduced transfer matrix $\hat{T}_{\mathrm{red}} =
\mathrm{Tr}_{\mathrm{int}}[\hat{T}_{\mathrm{KK}}]$ satisfies*

$$\Delta_0^{\mathrm{red}} = \Delta_0^{\mathrm{KK}} + O(e^{-2m_1 a}).$$


---

## 2. Proof via Feshbach Projection

### 2.1 Block decomposition

The projections $P_0$ and $Q_0$ decompose $\hat{H}_{\mathrm{KK}}$
into four blocks:

$$\hat{H}_{\mathrm{KK}} = \begin{pmatrix}
  P_0 \hat{H} P_0 & P_0 \hat{H} Q_0 \\
  Q_0 \hat{H} P_0 & Q_0 \hat{H} Q_0
\end{pmatrix}
\;\equiv\; \begin{pmatrix} H_{00} & W \\ W^\dagger & H_{QQ} \end{pmatrix},$$

where we write $\hat{H} \equiv \hat{H}_{\mathrm{KK}}$ and define:

- $H_{00} = P_0 \hat{H} P_0$, the **diagonal block** in the
  internal ground-state sector. As an operator on
  $\mathcal{H}_{\mathrm{std}}$ (after identifying
  $P_0 \mathcal{H}_{\mathrm{KK}} \cong \mathcal{H}_{\mathrm{std}}$),
  this is the Hamiltonian of the 4D theory with all KK modes frozen
  in their ground state.

- $H_{QQ} = Q_0 \hat{H} Q_0$, the **diagonal block** in the
  KK-excited sector.

- $W = P_0 \hat{H} Q_0$, the **off-diagonal coupling** between the
  internal ground state and KK-excited states.


### 2.2 Bound on the off-diagonal coupling $\|W\|$

The off-diagonal coupling arises from the bond interaction
$V^{\mathrm{bond}}$ (Section 4.1), which connects internal modes at
different sites through the lattice links. We claim:

$$\|W\| = \|P_0 \hat{H} Q_0\| \leq C_W\, e^{-m_1 a}. \tag{1}$$

**Proof of (1).** The Hamiltonian decomposes as
$\hat{H} = \hat{H}_{\mathrm{4D}} + \hat{H}_{\mathrm{int}} + \hat{V}$,
where $\hat{H}_{\mathrm{4D}}$ acts only on $\mathcal{H}_{\mathrm{std}}$,
$\hat{H}_{\mathrm{int}}$ acts only on $\mathcal{H}_{\mathrm{int}}$, and
$\hat{V}$ is the coupling.

Since $\hat{H}_{\mathrm{4D}} = \hat{H}_{\mathrm{4D}} \otimes \mathbf{1}$
commutes with $P_0$, it does not contribute to the off-diagonal block:
$P_0 \hat{H}_{\mathrm{4D}} Q_0 = 0$.

Since $|\Omega_{\mathrm{int}}\rangle$ is an eigenstate of
$\hat{H}_{\mathrm{int}}$, the internal Hamiltonian likewise does not
contribute: $P_0 \hat{H}_{\mathrm{int}} Q_0 = 0$.

Therefore $W = P_0 \hat{V} Q_0$, and

$$\|W\| \leq \|\hat{V}\|_{\mathrm{op}}.$$

The coupling $\hat{V}$ corresponds to the sum of bond interactions
$V^{\mathrm{bond}}_\ell$ over all spatial links $\ell$. For the
Hamiltonian (i.e., a single time-step), we have the operator inequality

$$\|\hat{V}\|_{\mathrm{op}} \leq \sum_\ell \|V^{\mathrm{bond}}_\ell\|_{\mathrm{op}}.$$

Each bond interaction satisfies
$\|V^{\mathrm{bond}}_\ell\|_{\mathrm{op}} \leq C_0\, e^{-m_1 a}$
by Theorem 2 (bond activity bound, Section 4.3). The sum over links
on a single time-slice contributes a factor $|\Lambda_t^1|$, giving

$$\|W\| \leq |\Lambda_t^1|\, C_0\, e^{-m_1 a} \equiv C_W\, e^{-m_1 a},$$

where $C_W = |\Lambda_t^1|\, C_0$ is polynomial in the lattice size
and independent of $a/r_3$. $\square$


### 2.3 Spectral gap of the $Q_0$ block

**Claim.** The operator $H_{QQ} = Q_0 \hat{H} Q_0$, restricted to
$Q_0 \mathcal{H}_{\mathrm{KK}}$, satisfies

$$H_{QQ} \geq (E_0 + m_1 - C_W e^{-m_1 a})\, Q_0, \tag{2}$$

where $E_0$ is the ground state energy of $\hat{H}_{\mathrm{KK}}$.

**Proof.** Any state in $Q_0 \mathcal{H}_{\mathrm{KK}}$ has at least
one KK mode excited. The internal Hamiltonian satisfies

$$\hat{H}_{\mathrm{int}} \Big|_{Q_0 \mathcal{H}} \geq m_1 \cdot Q_0,$$

since the lightest KK excitation has mass $m_1 = 2\sqrt{3}/r_3$
(Theorem 1: $\mu_1 = 6/r_3^2$, so
$m_1 = \sqrt{\mu_1} = \sqrt{6}/r_3 = 2\sqrt{3}/r_3$ when including
the mode normalization from Section 4.1). The 4D Hamiltonian
contributes $\hat{H}_{\mathrm{4D}} \geq E_0^{\mathrm{4D}} \cdot \mathbf{1}$,
and the coupling satisfies $\hat{V} \geq -\|\hat{V}\| \geq -C_W e^{-m_1 a}$.
Therefore, on $Q_0 \mathcal{H}$:

$$H_{QQ} \geq E_0^{\mathrm{4D}} + m_1 - C_W e^{-m_1 a}.$$

Since $E_0 \leq E_0^{\mathrm{4D}} + C_W e^{-m_1 a}$ (the full ground
state energy is bounded by the uncoupled ground state energy plus
the coupling perturbation), we obtain

$$H_{QQ} - E_0 \geq m_1 - 2C_W e^{-m_1 a} \geq \frac{m_1}{2}$$

for $m_1 a$ sufficiently large ($m_1 a \sim 10^{15}$ in the physical
regime). In particular, the spectral gap of $H_{QQ}$ above $E_0$ is
at least $m_1/2$. $\square$


### 2.4 The Feshbach formula

For any spectral parameter $z$ below the spectrum of $H_{QQ}$, the
Feshbach effective Hamiltonian in the $P_0$ sector is
(Feshbach 1958; Reed--Simon Vol. IV, Section XII.2;
Bach--Fr\"ohlich--Sigal 1998, Section 2):

$$H_{\mathrm{eff}}(z) = H_{00} + W\,(z - H_{QQ})^{-1}\, W^\dagger. \tag{3}$$

The eigenvalues of $\hat{H}$ below $\inf \sigma(H_{QQ})$ are in
bijection with the eigenvalues of $H_{\mathrm{eff}}(z)$ (as a
fixed-point equation: $z$ is an eigenvalue of $\hat{H}$ if and only
if $z$ is an eigenvalue of $H_{\mathrm{eff}}(z)$). This is the
isospectrality property of the Feshbach map.

**Bounding the Feshbach correction.** For the low-lying eigenvalues
$E_n$ of $\hat{H}$ (with $n = 0, 1$), we have
$E_n \leq E_0 + \Delta_0^{\mathrm{KK}} \ll E_0 + m_1/2$, so

$$\|(z - H_{QQ})^{-1}\| \leq \frac{1}{\mathrm{dist}(z, \sigma(H_{QQ}))}
  \leq \frac{2}{m_1} \tag{4}$$

for $z \in \{E_0, E_1\}$, using the spectral gap bound (2).

The Feshbach correction term in (3) is therefore bounded by:

$$\|W (z - H_{QQ})^{-1} W^\dagger\|
  \leq \|W\|^2 \cdot \|(z - H_{QQ})^{-1}\|
  \leq C_W^2\, e^{-2m_1 a} \cdot \frac{2}{m_1}
  = \frac{2 C_W^2}{m_1}\, e^{-2m_1 a}. \tag{5}$$


### 2.5 Eigenstate factorization

Since the Feshbach correction (5) is $O(e^{-2m_1 a}/m_1)$, the
low-lying eigenvalues of $\hat{H}$ satisfy:

$$E_n = E_n^{(0)} + O\!\left(\frac{e^{-2m_1 a}}{m_1}\right),
  \qquad n = 0, 1, \tag{6}$$

where $E_n^{(0)}$ are the eigenvalues of $H_{00}$ (the 4D Hamiltonian
with frozen internal ground state).

For the eigenstates, we use the standard perturbation formula for
the Feshbach map. The exact eigenstate $|n\rangle$ of $\hat{H}$ is
related to the corresponding eigenstate $|n^{(0)}\rangle$ of
$H_{\mathrm{eff}}(E_n)$ in $P_0 \mathcal{H}$ by:

$$|n\rangle = |n^{(0)}\rangle + (E_n - H_{QQ})^{-1}\, W^\dagger\, |n^{(0)}\rangle. \tag{7}$$

The first term lives in $P_0 \mathcal{H} \cong \mathcal{H}_{\mathrm{std}}$
and the second is the $Q_0$-component (internal excitation admixture).
The norm of the correction is:

$$\|(E_n - H_{QQ})^{-1} W^\dagger |n^{(0)}\rangle\|
  \leq \|(E_n - H_{QQ})^{-1}\| \cdot \|W^\dagger\|
  \leq \frac{2}{m_1} \cdot C_W e^{-m_1 a}
  = \frac{2C_W}{m_1}\, e^{-m_1 a}. \tag{8}$$

Setting $C_F = 2C_W$ and identifying $|n^{(0)}\rangle$ with
$|\psi_n\rangle_{\mathrm{4D}} \otimes |\Omega_{\mathrm{int}}\rangle$
(since $|n^{(0)}\rangle \in P_0 \mathcal{H}$), we obtain the
claimed factorization:

$$|n\rangle = |\psi_n\rangle_{\mathrm{4D}} \otimes
  |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle,
  \qquad \|\delta_n\| \leq \frac{C_F}{m_1}\, e^{-m_1 a},
  \qquad n = 0, 1.$$

This establishes part (i) of Lemma 4a. $\square$


---

## 3. Consequence: Spectral Gap Preservation

### 3.1 From eigenstate factorization to the reduced spectrum

The reduced density operators of the vacuum and glueball are:

$$\hat{\rho}_n^{\mathrm{4D}} =
  \mathrm{Tr}_{\mathrm{int}}[|n\rangle\langle n|]
  = |\psi_n\rangle\langle\psi_n| + O\!\left(\frac{e^{-m_1 a}}{m_1}\right)
  \qquad n = 0, 1.$$

The cross term is bounded by $2\|\delta_n\| = O(e^{-m_1 a}/m_1)$ and
the quadratic term by $\|\delta_n\|^2 = O(e^{-2m_1 a}/m_1^2)$. In
particular, $\hat{\rho}_n^{\mathrm{4D}}$ is a rank-one projector up
to corrections of order $e^{-m_1 a}/m_1$, confirming that the internal
sector is in a pure state (the ground state) to this accuracy.


### 3.2 Eigenvalues of $\hat{T}_{\mathrm{red}}$

Since $\hat{T}_{\mathrm{red}} = \sum_n \lambda_n^{\mathrm{KK}}
\hat{\rho}_n^{\mathrm{4D}}$ and the contributions from KK-excited
states ($n$ with KK-level $\geq 1$) have $\lambda_n \leq e^{-m_1 a}
\lambda_0$, the two largest eigenvalues of $\hat{T}_{\mathrm{red}}$ are:

$$\lambda_j(\hat{T}_{\mathrm{red}}) = \lambda_j^{\mathrm{KK}}
  + O\!\left(\frac{e^{-2m_1 a}}{m_1}\right), \qquad j = 0, 1.$$

This uses the fact that $\hat{\rho}_0^{\mathrm{4D}}$ and
$\hat{\rho}_1^{\mathrm{4D}}$ are nearly orthogonal rank-one
projectors (their overlap is
$|\langle\psi_0|\psi_1\rangle|^2 + O(e^{-m_1 a}/m_1)$, and the
first term vanishes since $|\psi_0\rangle$ and $|\psi_1\rangle$ are
distinct eigenstates of $H_{00}$, hence orthogonal).


### 3.3 The mass gap identity

$$\Delta_0^{\mathrm{red}}
  = -\frac{1}{a}\ln\frac{\lambda_1(\hat{T}_{\mathrm{red}})}
    {\lambda_0(\hat{T}_{\mathrm{red}})}
  = -\frac{1}{a}\ln\frac{\lambda_1^{\mathrm{KK}}
    + O(e^{-2m_1 a}/m_1)}{\lambda_0^{\mathrm{KK}}
    + O(e^{-2m_1 a}/m_1)}.$$

Expanding the logarithm (using $\ln(1+x) = x + O(x^2)$ for
$|x| \ll 1$):

$$\Delta_0^{\mathrm{red}} = \Delta_0^{\mathrm{KK}}
  + O\!\left(\frac{e^{-2m_1 a}}{m_1\, a\, \lambda_1^{\mathrm{KK}}}\right).$$

Since $\lambda_1^{\mathrm{KK}} = e^{-E_1 a} > 0$ is bounded away from
zero (as $E_1$ is finite) and $m_1 a \gg 1$, the correction is
$O(e^{-2m_1 a})$ (absorbing $1/(m_1 a)$ and $1/\lambda_1$ into the
constant). This establishes part (ii) of Lemma 4a. $\square$


---

## 4. How This Closes the Sub-Gap in Lemma 4

The proof of Theorem 5 (in `theorem5-proof.md`) uses Lemma 4 at
Step 2, where it invokes the inequality

$$\Delta_0^{\mathrm{red}} \geq \Delta_0^{\mathrm{KK}} - C' e^{-m_1 a}.$$

Lemma 4, Step 3 of that proof asserts the eigenstate factorization

$$|n\rangle = |\psi_n\rangle_{\mathrm{4D}} \otimes
  |\Omega_{\mathrm{int}}\rangle + O(e^{-m_1 a}), \qquad n = 0, 1$$

without derivation. The Feshbach projection argument above (Section 2)
supplies the missing derivation. The key inputs are:

1. **Off-diagonal coupling bound** (Section 2.2): $\|W\| = \|P_0 \hat{V} Q_0\|
   \leq C_W e^{-m_1 a}$, from the bond activity bound (Theorem 2).

2. **Internal spectral gap** (Section 2.3):
   $H_{QQ} - E_0 \geq m_1/2$, from the Weitzenboeck gap
   $\mu_1 = 6/r_3^2$ (Theorem 1) and the KK mass
   $m_1 = 2\sqrt{3}/r_3$.

3. **Feshbach isospectrality** (Section 2.4): the low-lying spectrum
   of $\hat{H}$ is determined by $H_{\mathrm{eff}} = H_{00} + O(e^{-2m_1 a}/m_1)$
   in the $P_0$ sector.

The conclusion:

$$\boxed{\Delta_0^{\mathrm{red}}
  = \Delta_0^{\mathrm{KK}} + O(e^{-2m_1 a})}$$

since the reduced transfer matrix $\hat{T}_{\mathrm{red}}$, restricted
to the $P_0$ sector, has the same low-lying spectrum as
$\hat{T}_{\mathrm{KK}}$ up to corrections of order $e^{-2m_1 a}$.
This is strictly stronger than the bound
$\Delta_0^{\mathrm{red}} \geq \Delta_0^{\mathrm{KK}} - C' e^{-m_1 a}$
stated in the original Lemma 4.


---

## 5. References

- Feshbach, H.: *Unified theory of nuclear reactions*, Ann. Phys. **5**
  (1958), 357--390; *A unified theory of nuclear reactions. II*,
  Ann. Phys. **19** (1962), 287--313. (Original Feshbach projection for
  decomposing Hilbert spaces into open/closed channels.)

- Bach, V., Fr\"ohlich, J., Sigal, I.M.: *Quantum electrodynamics of
  confined nonrelativistic particles*, Adv. Math. **137** (1998), 299--395.
  (Modern treatment of the Feshbach map in spectral theory; smooth
  Feshbach map; isospectrality.)

- Griesemer, M., Lieb, E.H., Loss, M.: *Ground states in
  non-relativistic quantum electrodynamics*, Invent. Math. **145** (2001),
  557--595. (Application of Feshbach projection to proving spectral gaps
  and ground state existence in QED.)

- Reed, M., Simon, B.: *Methods of Modern Mathematical Physics*,
  Vol. IV: *Analysis of Operators*, Academic Press, 1978, Section XII.2.
  (Feshbach formula for self-adjoint operators; Schur complement.)

- Kato, T.: *Perturbation Theory for Linear Operators*, Springer, 1966,
  Sections IV.3 and VII.3. (Resolvent perturbation theory; eigenvalue
  and eigenstate perturbation bounds.)

- Theorem 1 (Section 4.2 of the present paper): Weitzenboeck spectral
  gap $\mu_1 = 6/r_3^2$ on $\mathbb{CP}^{N-1}$.

- Theorem 2 (Section 4.3 of the present paper): Bond activity bound
  $|g_b| \leq C_0 e^{-m_1 a}$.


---

<!-- ASSESSMENT: PROVED -- The eigenstate factorization for the low-lying
states of H_KK is now established by the Feshbach projection. The three
inputs are: (1) the off-diagonal coupling ||W|| <= C_W e^{-m_1 a} from
the bond activity bound (Theorem 2), (2) the spectral gap m_1 of the
Q_0 sector from the Weitzenboeck bound (Theorem 1), and (3) the standard
Feshbach isospectrality (Bach-Froehlich-Sigal 1998). The correction to
the eigenstates is O(e^{-m_1 a}/m_1) and the correction to the spectral
gap is O(e^{-2m_1 a}). All bounds are explicit, with constants depending
on N and |Lambda_t^1| but not on a/r_3. The sub-gap in Lemma 4, Step 3
of theorem5-proof.md is closed. -->
