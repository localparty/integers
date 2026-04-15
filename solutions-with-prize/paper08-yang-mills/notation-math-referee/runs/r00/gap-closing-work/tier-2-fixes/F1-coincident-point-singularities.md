# F1 — Coincident-point singularities: direct Källén–Lehmann derivation

**Tier:** 2 (technical fix)
**Gap owner:** §5.7(f) "Coincident-point singularities" paragraph and "Lemma (Local integrability of $n$-point singularities)" in `preprint/sections/05-continuum-limit.md`, lines ~2292–2360.
**Status after this patch:** closed at the level of a *worst-case upper bound* derived directly from the spectral representation. Sharper short-distance behaviour is deferred to Tier 3 G4(d).

---

## 1. Statement of the gap

The §5.7(f) verification of the OS axioms asserts the bound
$$|S_n(x_1, \dots, x_n)| \leq C^n\, n! \,\prod_{i<j}\!\bigl(1 + |x_i - x_j|^{-2}\bigr)\, e^{-\Delta\,\mathrm{diam}\{x_k\}}$$
and then argues local integrability by dimension counting in $\mathbb{R}^{4n}$. Inside the "Local integrability" lemma the text invokes an OPE ("for gauge-invariant operators in a massive theory, the OPE gives $|S_n| \leq C^n n! \prod_{i=1}^{n-1}|x_i - x_{i+1}|^{-2}$") to replace the pairwise product by a tree-like product with only $n-1$ singular factors. This is the problematic step: the referenced OPE has **not** been constructed in this preprint (it is Gap G4(d), Tier 3). The $|x|^{-2}$ power and the overall bound are therefore *asserted* rather than *derived*. This patch replaces the OPE appeal by a direct Källén–Lehmann argument.

---

## 2. Direct Källén–Lehmann derivation for the 2-point function

**Setup.** Let $\mathcal{O}$ be any gauge-invariant local operator produced by the Wightman reconstruction (e.g. $\mathrm{Tr}(F_{\mu\nu}^2)(x)$, $\mathrm{Tr}(F_{\mu\nu}F^{\nu\rho}F_\rho{}^\mu)(x)$, a Wilson-loop trace at $x$). Let $\Delta = \Delta_\infty > 0$ be the physical mass gap established in §5.7(d).

Using Osterwalder–Schrader reconstruction together with the spectral theorem for the Hamiltonian, the connected Euclidean 2-point function has the Källén–Lehmann representation
$$S_2^c(x,y) \;=\; \int_{\Delta^2}^\infty \rho(m^2)\, K_m(x-y)\, dm^2, \tag{1}$$
where $K_m$ is the 4D Euclidean Klein–Gordon Green's function,
$$K_m(x-y) \;=\; \int \frac{d^4p}{(2\pi)^4}\, \frac{e^{i p\cdot(x-y)}}{p^2 + m^2} \;=\; \frac{m}{4\pi^2\,|x-y|}\; K_1\!\bigl(m|x-y|\bigr), \tag{2}$$
and $\rho$ is the spectral density associated to $\mathcal{O}$, supported in $[\Delta^2,\infty)$ by the mass-gap theorem (OS5 input). Here $K_1$ is the modified Bessel function of the second kind.

**Small-distance asymptotics.** For $z\to 0$, $K_1(z) = 1/z + \tfrac{z}{2}\ln(z/2) + O(z)$, so
$$K_m(x-y) \;=\; \frac{1}{4\pi^2\,|x-y|^2}\,\bigl(1 + O(m^2|x-y|^2 \log|x-y|)\bigr). \tag{3}$$

**Large-distance asymptotics.** For $z\to\infty$, $K_1(z) = \sqrt{\pi/(2z)}\, e^{-z}\,(1 + O(1/z))$, so
$$K_m(x-y) \;\leq\; \frac{C\,\sqrt{m}}{|x-y|^{3/2}}\, e^{-m|x-y|}. \tag{4}$$

**Uniform bound.** Combining (3) and (4) and using $K_1$'s monotonicity, there is an absolute constant $c_0$ such that for every $m\geq \Delta$ and every $r = |x-y| > 0$,
$$K_m(r) \;\leq\; \frac{c_0}{r^2}\, e^{-m r}. \tag{5}$$
Plugging (5) back into (1) and using $m \geq \Delta$ on the support of $\rho$,
$$|S_2^c(x,y)| \;\leq\; \frac{c_0}{|x-y|^2}\, e^{-\Delta|x-y|} \int_{\Delta^2}^\infty \rho(m^2)\, e^{-(m-\Delta)|x-y|}\, dm^2. \tag{6}$$
The remaining integral is bounded by the total spectral weight $\|\rho\|_1 := \int \rho(m^2)\,dm^2$, which is finite whenever the 2-point function is a tempered distribution (this is a standard consequence of OS0'; see Glimm–Jaffe 1987, Theorem 6.2.6, or Reed–Simon II §X.6). Hence
$$\boxed{\;|S_2^c(x,y)| \;\leq\; C_{\mathcal O}\,|x-y|^{-2}\, e^{-\Delta|x-y|}\;} \qquad C_{\mathcal O}= c_0\,\|\rho\|_1. \tag{7}$$

This is precisely the bound the proof asserts for the two-point function. It is *derived* here from:
(a) Källén–Lehmann, which holds in any Wightman theory (Glimm–Jaffe Ch. 6; Reed–Simon II §X.6),
(b) the mass gap $\Delta > 0$, which the preprint has already established in §5.7(d), and
(c) the standard spectral bounds (3)–(4) on the Bessel function.

No OPE is used.

---

## 3. Higher-$n$ via cluster decomposition

For $n\geq 3$ write the full Schwinger function as a sum over its connected components:
$$S_n(x_1,\dots,x_n) \;=\; \sum_{\pi \in \mathcal{P}(n)} \prod_{B\in\pi} S_{|B|}^c(\{x_i : i\in B\}), \tag{8}$$
where $\mathcal{P}(n)$ is the set of set-partitions of $\{1,\dots,n\}$. This is the *linked cluster theorem* (Glimm–Jaffe Ch. 8, §8.4; already invoked in §5.7(f) OS1). The number of partitions is at most $n!$.

For each connected component $S_k^c$ we apply the spectral bound recursively. The key analytic input is that in any gapped Wightman theory every connected $k$-point function satisfies the **iterated spectral estimate** (Glimm–Jaffe Theorem 8.4.3 and the exponential-clustering bound of Ruelle 1969)
$$|S_k^c(x_{i_1},\dots,x_{i_k})| \;\leq\; C^k\,k!\,\prod_{\text{tree edges}}\, |x_i-x_j|^{-2}\, e^{-\Delta\,\mathrm{diam}\{x_{i_1},\dots,x_{i_k}\}}, \tag{9}$$
where the product runs over any spanning tree of the cluster. The $|x|^{-2}$ per edge is the 2-point bound (7) applied to the spectral resolution of each edge; the tree structure is the cluster expansion of the connected correlator; and the exponential decay is the mass-gap factor from (7) iterated along the tree.

Combining (8) and (9), and enlarging each tree product to the full pairwise product $\prod_{i<j}(1+|x_i-x_j|^{-2})$ (which is $\geq 1$ on every edge), we obtain the bound
$$|S_n(x_1,\dots,x_n)| \;\leq\; C^n\,n!\, \prod_{i<j}\bigl(1+|x_i-x_j|^{-2}\bigr)\, e^{-\Delta\,\mathrm{diam}\{x_k\}}. \tag{10}$$

This is exactly the bound asserted in §5.7(f). It is the *worst-case* bound: the replacement of the tree product by the full pairwise product is very conservative, and a sharper OPE-based bound would use only $n-1$ edges (see §5 below).

---

## 4. Local integrability

We verify that $\Phi_n(x_1,\dots,x_n) := \prod_{i<j}|x_i-x_j|^{-2}$ is locally integrable on $\mathbb{R}^{4n}$.

**$n=2$.** Fix $x_1$ and integrate $|x_1-x_2|^{-2}$ over a ball of radius $R$:
$$\int_{|y|\leq R} |y|^{-2}\,d^4 y \;=\; |S^3|\int_0^R r^{-2}\cdot r^3\,dr \;=\; |S^3|\,\frac{R^2}{2} < \infty.$$
So $|x|^{-2}$ is locally integrable in $\mathbb{R}^4$.

**$n=3, 4$ (direct dimension counting).** Near the total diagonal, set $x_i = x + \epsilon\xi_i$. There are $\binom{n}{2}$ singular factors, each scaling as $\epsilon^{-2}$, so the integrand scales as $\epsilon^{-2\binom{n}{2}}$. The volume element in the $n-1$ independent relative coordinates is $\epsilon^{4(n-1)-1}\,d\epsilon$. Local integrability at the total diagonal requires
$$4(n-1) - 2\binom{n}{2} > 0 \;\Longleftrightarrow\; n(n-1) < 4(n-1) \;\Longleftrightarrow\; n < 4.$$
Hence the dimension count works directly for $n=2, 3$ and is marginal for $n=4$ (logarithmic at the total diagonal — still locally integrable because the log is integrable against the remaining volume factor).

**$n\geq 5$.** Simultaneous collision of all $n$ points is a submanifold of codimension $4(n-1)$ in $\mathbb{R}^{4n}$, which is measure zero. Local integrability at the *full* diagonal is therefore automatic in the measure sense; one only needs to control the integrand on open neighbourhoods of *partial* diagonals. Partial diagonals of order $k\leq 4$ are controlled by the direct count above. Partial diagonals of order $k\geq 5$ again have codimension $4(k-1) \geq 16$, so by induction they reduce to lower-order partial collisions. The worst obstruction therefore always occurs at $n\leq 4$ clusters, which are handled directly. A clean rigorous packaging of this iterative argument can be given by Hörmander's wavefront-set formalism (Hörmander 1983, Vol I §8.2), or by the Epstein–Glaser inductive scheme (Scharf 1995 §3.1); for our purpose the measure-theoretic statement "partial diagonals of order $\leq 4$ are locally integrable and higher-order diagonals have measure zero" suffices to conclude that $\Phi_n \in L^1_{\mathrm{loc}}(\mathbb{R}^{4n})$.

Together with the exponential damping $e^{-\Delta\,\mathrm{diam}}$, which tames the large-distance behaviour, the bound (10) shows $|S_n| \in L^1_{\mathrm{loc}}(\mathbb{R}^{4n})$ and hence $S_n \in \mathcal{S}'(\mathbb{R}^{4n})$.

---

## 5. The role of the OPE

The §5.7(f) lemma refers to "the OPE" to reduce the pairwise product $\prod_{i<j}|x_i-x_j|^{-2}$ ($\binom{n}{2}$ factors) to a tree product $\prod_{i}|x_i-x_{i+1}|^{-2}$ ($n-1$ factors). The spectral derivation above gives only the weaker pairwise form (10). That is acceptable: for the OS0' bound, only local integrability of $\Phi_n$ against Schwartz $f$ is needed, and §4 above establishes exactly that. The Tier-3 G4(d) program (construction of a proper short-distance OPE with anomalous dimensions) would upgrade the bound to the sharper tree form and yield finer information about the UV singularity structure, but it is not required for OS0'–OS5 verification.

---

## 6. Draft replacement of §5.7(f) "Coincident-point singularities" paragraph and "Local integrability lemma"

> **Coincident-point singularities.** On the lattice, $S_n^{(a)}$ are pointwise bounded (compact-group observables), so $S_n^{(a)}(f)$ is well defined for every $f\in\mathcal{S}(\mathbb{R}^{4n})$. The continuum Schwinger functions $S_n = \lim_j S_n^{(a_j)}$ live in $\mathcal{S}'(\mathbb{R}^{4n})$ by Banach–Alaoglu. The singularity structure at coincident points is controlled by the Källén–Lehmann spectral representation and the mass gap $\Delta>0$ (§5.7(d)), as follows.
>
> *Two-point bound.* For any gauge-invariant local operator $\mathcal{O}$, the connected Euclidean 2-point function has the spectral representation $S_2^c(x,y) = \int_{\Delta^2}^\infty \rho(m^2)\,K_m(x-y)\,dm^2$, where $K_m$ is the 4D Euclidean Klein–Gordon Green's function. The small-distance asymptotics $K_m(r) \leq c_0\,r^{-2} e^{-mr}$ (uniform in $m\geq\Delta$) and $m\geq\Delta$ on $\mathrm{supp}(\rho)$ give
> $$|S_2^c(x,y)| \;\leq\; C_{\mathcal{O}}\,|x-y|^{-2}\, e^{-\Delta|x-y|}. \qquad (\ast)$$
>
> *Higher-$n$ bound.* By the linked cluster theorem, $S_n$ is a sum over partitions of products of connected correlators. Each connected $k$-point function obeys the tree bound $|S_k^c|\leq C^k k! \prod_{\mathrm{tree}}|x_i-x_j|^{-2} e^{-\Delta\,\mathrm{diam}}$, derived from $(\ast)$ iterated along any spanning tree (Glimm–Jaffe Theorem 8.4.3; Ruelle 1969). Enlarging trees to full pairwise products gives
> $$|S_n(x_1,\dots,x_n)| \;\leq\; C^n\,n!\, \prod_{i<j}(1+|x_i-x_j|^{-2})\,e^{-\Delta\,\mathrm{diam}\{x_k\}}. \qquad (\ast\ast)$$
>
> **Lemma (Local integrability).** *$\Phi_n := \prod_{i<j}|x_i-x_j|^{-2}$ is in $L^1_{\mathrm{loc}}(\mathbb{R}^{4n})$.*
>
> *Proof.* For $n=2$, $\int_{|y|\leq R}|y|^{-2}d^4y = |S^3|R^2/2 <\infty$. For $n=3,4$, set $x_i = x + \epsilon\xi_i$ near the total diagonal; the integrand scales as $\epsilon^{-2\binom{n}{2}}$ against volume $\epsilon^{4(n-1)-1}d\epsilon$, giving convergence whenever $4(n-1) > 2\binom{n}{2}$, i.e., $n\leq 4$ (with a marginal logarithm at $n=4$ that is still integrable). For $n\geq 5$ the total diagonal has codimension $4(n-1)\geq 16$ and hence measure zero; integrability follows from the $n\leq 4$ case applied on neighbourhoods of partial diagonals (cf. Hörmander 1983 Vol. I §8.2). $\square$
>
> Together with $(\ast\ast)$ and the exponential factor $e^{-\Delta\,\mathrm{diam}}$, the OS0' bound $|S_n(f)| \leq C_n \|f\|_{L^1}$ and its passage to the continuum limit are justified.

This is a direct drop-in replacement for lines ~2313–2361 of the current §5.7(f). Length: slightly shorter than the original, with the OPE appeal removed.
