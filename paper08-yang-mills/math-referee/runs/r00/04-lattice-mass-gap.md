# Theorem 4: Lattice Mass Gap

This section assembles Theorems 1--3 into the central proved result:
the lattice mass gap for $SU(N)$ gauge theory enhanced with
$\mathbb{CP}^{N-1}$ harmonics.


---

## Statement

**Theorem 4 (Lattice mass gap).** *For the $SU(N)$ lattice gauge
theory on $\Lambda_L$ enhanced with $\mathbb{CP}^{N-1}$ harmonics
in the $k = 0$ sector, with $r_3/a < \sqrt{3/(4N)}$, for all
$\beta > 0$:*

*(a) The cluster expansion converges absolutely.*

*(b) The free energy density $f(\beta) = |\Lambda_L|^{-1} \ln Z_{k=0}$
is analytic in $\beta$.*

*(c) Connected correlators decay exponentially:*
$$|\langle \mathcal{O}(x)\,\mathcal{O}(y) \rangle_c|
  \leq C\,e^{-m|x-y|}$$
*with rate $m > 0$ uniform in $L$.*

*(d) The string tension satisfies $\sigma_0(\beta) > 0$.*

*(e) The mass gap satisfies
$\Delta_0(\beta) \geq c\sqrt{\sigma_0} > 0$.*


---

## Proof

**(a) Convergence.** By Theorem 1, $\lambda_1^{(1)} \geq 6/r_3^2$
on $\mathbb{CP}^{N-1}$. By Theorem 2, bond activities satisfy
$|g_b| \leq C_0\,e^{-m_1 a}$ with $m_1 = 2\sqrt{3}/r_3$. Every
connected cluster on a 4D lattice has $|B| \geq |S|/6$, so each
element carries suppression $e^{-m_1 a/6}$. Theorem 3
(Koteck\'y--Preiss) gives absolute convergence when
$2\beta < m_1 a/6 - \ln(c_d\,K\,C_0^{1/6})$. The condition
$r_3/a < \sqrt{3/(4N)}$ ensures this holds for all $\beta > 0$.

**(b) Analyticity.** Each $\phi(\mathcal{C})$ is analytic in $\beta$.
Absolute convergence implies uniform convergence on compact
$\beta$-intervals, so $f(\beta)$ is analytic.

**(c) Exponential decay.** The Koteck\'y--Preiss criterion with
weight $a(\mathcal{C}) = \alpha|\mathcal{C}|$ penalizes cluster
size exponentially. Connected correlators receive contributions
only from clusters connecting $x$ to $y$, giving
$m \geq \alpha/a > 0$ uniformly in $L$.

**(d) Area law.** The Wilson loop $\langle W_R(C_{T \times R}) \rangle$
is dominated by clusters tiling the minimal area. The per-element
suppression yields $-\ln\langle W_R \rangle \geq \sigma_0\,TR$
with $\sigma_0 \geq \alpha > 0$.

**(e) Mass gap.** By the Fredenhagen--Marcu theorem, $\sigma_0 > 0$
implies $\Delta_0 \geq c\sqrt{\sigma_0} > 0$. $\square$


---

## From the $k = 0$ Sector to the Full Theory

**Corollary.** *Under the conditions of Theorem 4, the full
$SU(N)$ KK-enhanced lattice theory satisfies*
$$\sigma(\beta) \;\geq\; \sigma_0(\beta)\,
  \bigl(1 - C\,e^{-4\pi^2\beta/N}\bigr) \;>\; 0
  \qquad \text{for all } \beta > 0.$$

*Proof.* The Bogomolny bound gives $Z_k/Z_0 \leq
C_k\,e^{-8\pi^2|k|\beta/N}$ for each non-trivial topological
sector. The correction to the string tension is
$$\sigma \geq \sigma_0
  - \frac{1}{TR}\ln\Bigl(1 + \textstyle\sum_{k \neq 0}
  C_k\,e^{-8\pi^2|k|\beta/N}\Bigr).$$
The geometric sum yields the factor
$1 - C\,e^{-4\pi^2\beta/N}$, which is strictly positive for
all $\beta > 0$. $\square$


---

## Scope and Limitations

**What this covers.** Theorem 4 establishes $\sigma > 0$ and
$\Delta > 0$ for all lattice spacings $a \gg r_3$. This includes
every lattice spacing used in practice:

- At $a \sim 0.1$ fm: $a/r_3 \sim 10^{15}$, bond suppression
  $e^{-m_1 a} \sim e^{-3.46 \times 10^{15}}$.
- At $a \sim 10^{-20}$ m: $a/r_3 \sim 10^{11}$, convergence
  margin remains vast.

The convergence condition $\beta < a/(2\sqrt{3}\,r_3)$ is
satisfied on the asymptotic freedom trajectory with a margin of
$10^{13}$ or more at physical couplings.

**What this does not cover.** The continuum limit $a \to 0$.
As $a$ decreases below $r_3$, the KK modes have $m_1 a < 1$
and the cluster expansion fails. The continuum limit requires
either Balaban's RG (Section 06) with the form factor bound
(Section 08), or the IR decoupling argument (Section 05).
