# Theorem 5: IR Equivalence (Decoupling)

This section proves that the KK-enhanced and standard $SU(N)$
lattice gauge theories share the same string tension, transferring
the mass gap of Theorem 4 to the physical theory.


---

## Statement

**Theorem 5 (IR equivalence).** *The KK-enhanced and standard
$SU(N)$ lattice gauge theories have the same string tension:*
$$\sigma_{\mathrm{std}}(\beta)
  = \sigma_{\mathrm{KK}}(\beta) + O(e^{-m_1 a}).$$
*In particular, $\sigma_{\mathrm{std}} > 0$ whenever
$\sigma_{\mathrm{KK}} > 0$ and $m_1 a \gg 1$.*


---

## Proof sketch

**Step 1 (KK mass spectrum).** The KK reduction on $\Lambda_a
\times \mathbb{CP}^{N-1}$ produces 4D fields $\phi_n$ with masses
$m_n = \sqrt{\lambda_n^{(1)}}/r_3$. The lightest mode has
$$m_1 = \frac{2\sqrt{3}}{r_3}.$$
The zero mode ($n = 0$) is the standard 4D gauge field $A_\mu$;
all other modes satisfy $m_n \geq m_1$.

**Step 2 (Long-distance suppression).** The string tension is
extracted from Wilson loops at separations $R \gg
1/\Lambda_{\mathrm{QCD}}$. KK modes contribute through virtual
exchanges suppressed by
$$\langle W_R \rangle_{\mathrm{KK}}
  - \langle W_R \rangle_{\mathrm{std}}
  \;\sim\; e^{-m_1 R}.$$
At physical separations: $e^{-m_1 R} \sim e^{-10^{28}}$.

**Step 3 (Effective action).** Integrating out all KK modes
generates irrelevant operators:
$$\Gamma_{\mathrm{eff}}[A]
  = S_{\mathrm{Wilson}}[A]
  + \sum_{n \geq 1} \frac{c_n}{m_n^{d_n - 4}}
  \int \mathcal{O}_n\,d^4x,$$
where $\mathcal{O}_n$ have dimension $d_n > 4$. The leading
correction ($d = 6$) is
$\delta S \sim m_1^{-2}\int\mathrm{Tr}\,(D_\mu F_{\nu\rho})^2$.

**Step 4 (Power counting).** The correction to $\sigma$ scales as
$$\frac{\delta\sigma}{\sigma}
  \;\sim\; \Bigl(\frac{\Lambda_{\mathrm{QCD}}}{m_1}\Bigr)^{\!2}
  \;\sim\; \Bigl(\frac{200\;\mathrm{MeV}}{10^{15}\;\mathrm{GeV}}
  \Bigr)^{\!2}
  \;\sim\; 10^{-26}.$$

**Step 5 (Conclusion).** Therefore $\sigma_{\mathrm{std}} =
\sigma_{\mathrm{KK}} + O(\Lambda_{\mathrm{QCD}}^4/m_1^2)$, and
since $\sigma_{\mathrm{KK}} > 0$ by Theorem 4 and its corollary,
$\sigma_{\mathrm{std}} > 0$. By Fredenhagen--Marcu,
$\Delta_{\mathrm{std}} \geq c\sqrt{\sigma_{\mathrm{std}}} > 0$.
$\square$


---

## Remarks

**Nature of the argument.** The proof uses standard Wilsonian
decoupling of heavy modes (Appelquist--Carazzone 1975). No
monotonicity or correlation inequalities are required.

**Validity condition.** The theorem requires $m_1 a \gg 1$, the
same regime $a \gg r_3$ where Theorem 4 applies. For physical
values ($r_3 \sim 10^{-31}$ m, $a \geq 10^{-20}$ m):
$m_1 a \geq 10^{11}$.

**What this achieves.** The standard $SU(N)$ lattice theory ---
without KK enhancement --- has $\sigma > 0$ and $\Delta > 0$ at
every $a \gg r_3$. The $\mathbb{CP}^{N-1}$ harmonics are a proof
device: they supply the spectral gap driving the cluster expansion,
but their physical effects decouple from infrared observables.
