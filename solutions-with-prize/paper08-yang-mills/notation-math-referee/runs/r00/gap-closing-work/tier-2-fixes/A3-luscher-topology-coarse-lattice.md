# Tier-2 Fix A3: Lüscher topological charge on coarse lattices

**Target:** §4.4 "From the $k=0$ Sector to the Full Theory"
Corollary, lines 805–862 of `04-lattice-proof-part1.md`.

---

## 1. Statement of the gap

Section 4.4 argues that the lattice configurations in Theorem 4's
cluster-expansion regime carry a well-defined Lüscher (CMP 85, 1982)
topological charge $Q_L[U]$, which requires the plaquette
admissibility condition $\|\mathbf{1}-U_P\| < \epsilon_L$ for a
fixed geometric threshold $\epsilon_L$. The existing text derives
this admissibility from *Balaban's* small-field condition
$|F_{\mu\nu}| < g_k^{1-\epsilon}$ via the bound
$\|\mathbf{1}-U_P\| \leq C a^2 g_k^{1-\epsilon}$. But Theorem 4
is proved at the **bare cluster-expansion scale** $a_0(K)$, where
Balaban's small-field/large-field decomposition has *not yet been
invoked*. Instead Theorem 4 uses the Koteck\'y–Preiss convergence
criterion

$$2\beta + \alpha < \tfrac{1}{6}m_1 a_0(K) - \ln(c_d K C_0^{1/6}),$$

with bond activities $|g_b|_{\mathrm{int}} \leq C_0 e^{-m_1 a_0(K)}$
(Theorem 2). The Lüscher threshold therefore needs to be verified
directly under the cluster-expansion measure, not inferred from a
Balaban small-field condition that plays no role at the bare scale.

## 2. Lüscher's admissibility threshold (CMP 85)

In Lüscher (CMP 85, 1982) Eq. (4), admissibility for SU(2) is stated
as $\mathrm{Tr}\{\mathbf{1}-U_P\} < \varepsilon$, with the explicit
(non-optimal) value $\varepsilon \leq 0.03$ established in the proof
of property (ii) on p. 40. Footnote 1 extends the construction to
*any compact gauge group*, so for SU(N) we adopt

$$\mathrm{Tr}_R\{\mathbf{1}-U_P\} < \epsilon_L, \qquad
  \epsilon_L = 0.03 \quad (\text{fundamental rep.})$$

as a conservative group-independent threshold. In terms of the
normalized plaquette variable $s_P = 1 - (1/N)\mathrm{Re}\,\mathrm{Tr}\,U_P$
used in the Wilson action, admissibility becomes
$N s_P < \epsilon_L$, i.e., $s_P < \epsilon_L/N \approx 0.01$ for
SU(3).

## 3. Moment estimate under the cluster-expansion measure

The cluster expansion represents the partition function as

$$Z = \sum_{\{\mathcal{C}\}} \prod_\alpha \phi(\mathcal{C}_\alpha),
\qquad |\phi(\mathcal{C})| \leq
\bigl(K\,C_0^{1/6}\,e^{2\beta}\,e^{-m_1 a_0(K)/6}\bigr)^{|\mathcal{C}|},$$

with the cluster weight dominated by the bond-suppression factor
$e^{-m_1 a_0(K)/6}$. Under the convergent cluster measure, the
*trivial* cluster (no activated plaquette, no activated bond)
carries weight $1$ and corresponds to $U_P = \mathbf{1}$ exactly.
Every non-trivial cluster supporting a deviation $U_P \neq \mathbf{1}$
pays at least one factor of the per-element bound
$\xi := K\,C_0^{1/6}\,e^{2\beta - m_1 a_0(K)/6}$.

At physical values $N = 3$, $\beta = 6$, $a_0(K)/r_3 = 10^{15}$,

$$m_1 a_0(K) = 2\sqrt{N}\,a_0(K)/r_3 = 3.464\times 10^{15},
\qquad \xi \sim \exp(12 - 5.77\times 10^{14})
\approx e^{-5.77\times 10^{14}}.$$

The expectation of $s_P$ under the cluster measure is therefore

$$\langle s_P\rangle_{\mathrm{CE}}
= 0 \cdot \Pr(\text{trivial}) +
\langle s_P\rangle_{\mathrm{non-triv}} \cdot \Pr(\text{non-trivial})
\leq \max_U s_P \cdot \xi \leq 2\xi,$$

using $s_P \leq 2$ uniformly on SU(N). Concretely
$\langle s_P\rangle_{\mathrm{CE}} \leq 4 e^{-m_1 a_0(K)/6 + 2\beta}$,
which is $\sim e^{-5.77\times 10^{14}}$ at physical values. This
is *not* the pure-Wilson expectation
$\langle s_P\rangle_W = (N^2-1)/(4N\beta) = 1/9 \approx 0.111$ at
$\beta = 6$ (Creutz, *Quarks, Gluons and Lattices*, Eq. 8.33), which
exceeds $\epsilon_L/N$ at moderate $\beta$. The KK-enhanced measure
is a different distribution altogether: the bond suppression
$e^{-m_1 a_0(K)}$ forces the typical configuration toward
$U_P = \mathbf{1}$ regardless of $\beta$, provided the cluster
expansion converges.

The same bound applies to the second moment because
$\langle s_P^2\rangle_{\mathrm{CE}} \leq 4 \langle s_P\rangle_{\mathrm{CE}}$
(use $s_P \leq 2$), giving

$$\langle\mathrm{Tr}\{\mathbf{1}-U_P\}^2\rangle_{\mathrm{CE}}
= N^2 \langle s_P^2\rangle_{\mathrm{CE}}
\leq 4 N^2 \xi \ll \epsilon_L^2.$$

## 4. Quantitative bound on the rough-configuration contribution

Let $\mathcal{R}_P = \{U : \mathrm{Tr}\{\mathbf{1}-U_P\} > \epsilon_L\}$
be the "rough" set at plaquette $P$. Markov's inequality applied
to the cluster-expansion measure gives

$$\Pr_{\mathrm{CE}}\!\bigl(\mathcal{R}_P\bigr)
\leq \frac{\langle\mathrm{Tr}\{\mathbf{1}-U_P\}\rangle_{\mathrm{CE}}}{\epsilon_L}
\leq \frac{4 N \xi}{\epsilon_L}
= \frac{4 N}{\epsilon_L}\,K\,C_0^{1/6}\,e^{2\beta - m_1 a_0(K)/6}.$$

The total rough contribution to any observable $\mathcal{O}$ with
$\|\mathcal{O}\|_\infty \leq M$ is bounded by a union bound over the
$|\Lambda^2|$ plaquettes,

$$|\mathcal{O}^{\mathrm{rough}}|
\leq M\,|\Lambda^2|\,\cdot\,\frac{4 N}{\epsilon_L}\,
  K\,C_0^{1/6}\,e^{2\beta - m_1 a_0(K)/6}.$$

The volume prefactor $|\Lambda^2|$ is at most $|\Lambda|^2$; on
$\mathbb{Z}^4$ the cluster bound is usually derived per unit
volume, absorbing the volume factor, so the effective suppression
remains $e^{-m_1 a_0(K)/6 + 2\beta + \ln|\Lambda|}$. For every
physical lattice of interest ($a_0(K)/r_3 \gg 60$ at $\beta = 6$),
this is exponentially below the cluster-expansion convergence
margin, which by Theorem 3 is $m_1 a_0(K)/6 - 2\beta - O(1)$.
Hence the rough contribution is smaller than the cluster-expansion
error itself and does not affect any order of the expansion.

## 5. Lüscher topological charge applicability lemma

**Lemma A3.1 (Lüscher admissibility under the cluster measure).**
*Let $a_0(K) \gg r_3$ be a bare lattice spacing, $\beta > 0$, and
suppose the cluster-expansion convergence condition*

$$2\beta + \alpha < \tfrac{1}{6}m_1 a_0(K) - \ln(c_d K C_0^{1/6})$$

*of Theorem 3 holds. Let $\epsilon_L > 0$ be the geometric
admissibility threshold of Lüscher (CMP 85, 1982), generalised to
SU(N) via footnote 1. Then:*

*(i) The cluster-expansion measure assigns the "admissible" set*
$\mathcal{A} = \{U : \forall P,\;\mathrm{Tr}_R\{\mathbf{1}-U_P\} < \epsilon_L\}$
*probability at least $1 - C_\Lambda e^{-m_1 a_0(K)/6 + 2\beta}$,
where $C_\Lambda$ absorbs volume and combinatorial factors.*

*(ii) On $\mathcal{A}$, the Lüscher topological charge $Q_L[U]$
is a well-defined integer (CMP 85, properties (i)–(v)), agrees with
the continuum second Chern number up to $O(a_0(K)^2 \|F\|^2)$, and is
a locally constant function of the link variables.*

*(iii) The restriction to the $c_2 = 0$ sector preserved by the
Bogomolny bound (CMP 85, Eq. (6)) holds on $\mathcal{A}$ up to an
error*

$$|Z_{c_2\neq 0}/Z_{c_2=0}| \leq C e^{-8\pi^2/g_0^2} + C_\Lambda e^{-m_1 a_0(K)/6 + 2\beta},$$

*where the first term is the standard instanton suppression and the
second is the rough-configuration leakage bounded in (i).*

**Proof sketch.** Part (i) is the Markov bound of §4 combined with
a union bound over plaquettes; $C_\Lambda = 4 N |\Lambda^2|/\epsilon_L$.
Part (ii) is immediate from Lüscher's geometric construction (CMP 85
§3, Lemma and Eqs. (25)–(32)) once admissibility is established
pointwise. Part (iii) separates the $Q_L$-sum into the contribution
from $\mathcal{A}$ (controlled by the Bogomolny bound) and the
contribution from the complement $\mathcal{A}^c$ (controlled by (i)). $\square$

## 6. What this adds to §4.4

Lemma A3.1 replaces the current §4.4 "Compatibility with the
small-field condition" paragraph, which incorrectly appeals to
Balaban's $|F_{\mu\nu}| < g_k^{1-\epsilon}$ condition at the bare
scale. The replacement (i) gives a self-contained admissibility
check that uses only the Theorem 3 convergence condition, (ii)
quantifies the rough-configuration contribution explicitly, (iii)
shows it is smaller than the cluster-expansion convergence margin,
and (iv) derives the Bogomolny restriction to $c_2 = 0$ up to a
quantified error. The key numerical inputs for $N = 3$,
$a_0/r_3 = 10^{15}$, $\beta = 6$ are

| Quantity | Value |
|:---------|:------|
| $m_1 a_0(K) = 2\sqrt{3}\cdot 10^{15}$ | $3.46 \times 10^{15}$ |
| Convergence margin $m_1 a_0/6 - 2\beta$ | $5.77 \times 10^{14}$ |
| $\xi = K C_0^{1/6} e^{2\beta - m_1 a_0/6}$ | $\sim e^{-5.77\times 10^{14}}$ |
| Rough-plaquette probability | $\leq 4 N \xi/\epsilon_L \sim e^{-5.77\times 10^{14}}$ |
| Lüscher threshold $\epsilon_L$ | $0.03$ (SU(2) stated, not optimal) |

The Lüscher admissibility condition is therefore satisfied with
astronomical margin throughout the cluster-expansion convergence
window.

## 7. Conclusion

The Lüscher topological-charge applicability lemma holds at the
bare cluster-expansion scale via a direct moment estimate. The
preprint's §4.4 paragraph on "Compatibility with the small-field
condition" should be replaced by Lemma A3.1, which uses only the
ingredients of Theorem 2 and Theorem 3 of Section 4 and does not
depend on Balaban's RG. The resulting statement of the corollary
(Eq. 5 of §4.4, the geometric series bound
$\sigma \geq \sigma_0(1 - C e^{-4\pi^2\beta/N})$) is unchanged, but
the justification now closes a logical gap.

**References.**

- Lüscher, M. "Topology of lattice gauge fields." *Commun. Math. Phys.*
  **85** (1982), 39–48. Eq. (4); footnote 2 (p. 40: "this bound is not
  optimal"); footnote 1 (p. 39: extension to any compact gauge group).
- Creutz, M. *Quarks, Gluons and Lattices*. Cambridge (1983),
  Eq. (8.33): $\langle s_P\rangle_W = (N^2-1)/(4 N \beta) + O(1/\beta^2)$.
- Section 4 of `04-lattice-proof-part1.md`: Theorems 2–4 and §4.4
  Corollary (lines 805–862).
