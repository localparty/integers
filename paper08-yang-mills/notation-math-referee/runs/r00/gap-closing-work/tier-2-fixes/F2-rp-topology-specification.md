# F2 — Reflection positivity topology specification for the Portmanteau step

**Tier:** 2 (technical fix)
**Gap owner:** §5.7(f) OS3 Step 2 "Preservation under weak limits" in `preprint/sections/05-continuum-limit.md`, lines ~2192–2216. Related: `preprint/sections/D-reflection-positivity.md` Lemma D.2 for the lattice RP input.

---

## 1. Statement of the gap

The OS3 verification argues that reflection positivity passes to the continuum limit via Portmanteau: at each lattice spacing $a>0$, $B_{\mu_a}(f) = \int F_f\,d\mu_a$ with
$$F_f(\phi) \;=\; \overline{f[\phi|_+]}\cdot f[\theta^*\phi|_+] \tag{1}$$
is non-negative by Lemma D.2, and Portmanteau lets one take $a\to 0$. But Portmanteau requires $F_f$ to be bounded continuous **on the topological space carrying the weak convergence $\mu_a\to\mu$**, and the preprint leaves that topology unspecified. Three issues must be resolved: (i) what is the topology; (ii) is $F_f$ continuous in it; (iii) is $F_f$ bounded — delta-like distributions give $|\langle f,\phi\rangle|=\infty$, so $F_f$ is *not* bounded on all of $\mathcal{S}'$. This patch specifies the topology (weak-$*$ on tempered distributions), verifies continuity, and resolves boundedness by working on the *supports* of the measures.

---

## 2. The topology on field space

**Lattice.** For each $a>0$, $\mu_a$ is a probability measure on the compact manifold $\mathcal{C}_a := \mathrm{SU}(N)^{|\Lambda^1|} \times (\mathbb{CP}^{N-1})^{|\Lambda^0|}$ (link variables and on-site KK internal connections, §4.1). Compactness is crucial: lattice configurations are automatically bounded.

**Continuum.** View lattice configurations as tempered distributions via a standard block-spin interpolation $\mathcal{I}_a$:
$$\phi_a[f] \;:=\; a^4 \sum_{x\in\Lambda_a} \mathcal{I}_a(\phi_a)(x)\cdot f(x), \qquad f\in\mathcal{S}(\mathbb{R}^4,\mathfrak{g}). \tag{2}$$
The pushforward $\tilde\mu_a := (\phi_a)_*\mu_a$ is a Borel probability measure on
$$X \;:=\; \mathcal{S}'(\mathbb{R}^4,\mathfrak{g})$$
equipped with the **weak-$*$ (= vague) topology**: $\phi_n\to\phi$ iff $\langle f,\phi_n\rangle\to\langle f,\phi\rangle$ for every $f\in\mathcal{S}$. This topology is separable metrizable on norm-bounded sets (Reed–Simon I §V.4).

**Mode of convergence.** The Banach–Alaoglu argument of OS1 — using the uniform OS0' bound $|S_n(f)|\leq n!C_0^n\|f\|_{L^1}$ — extracts a subsequence $a_j\to 0$ along which all Schwinger functions converge. By the Hamburger–Nussbaum moment criterion (Glimm–Jaffe 1987 Thm 6.1.2), since the Schwinger functions satisfy the $C^n n!$ growth, they uniquely determine a probability measure $\mu$ on $X$, and the convergence of moments is equivalent to
$$\int_X G\,d\tilde\mu_{a_j} \;\longrightarrow\; \int_X G\,d\mu \qquad \forall\, G\in C_b(X), \tag{3}$$
i.e. $\tilde\mu_{a_j}\to\mu$ weakly on $X$ in the probability-measure sense.

---

## 3. Continuity of $F_f$ in the weak-$*$ topology

Fix $f\in\mathcal{S}(\mathbb{R}^4,\mathfrak{g})$ supported in the positive-time half-space. The map $\phi\mapsto\langle f,\phi\rangle$ is continuous on $X$ by the very definition of the weak-$*$ topology. The reflection is handled via the adjoint identity $\langle f,\theta^*\phi\rangle = \langle \theta f,\phi\rangle$, and since $\theta f\in\mathcal{S}$, $\phi\mapsto\langle\theta f,\phi\rangle$ is also weak-$*$ continuous. Therefore
$$F_f(\phi) \;=\; \overline{\langle f,\phi\rangle}\cdot\langle\theta f,\phi\rangle$$
is continuous as a product of continuous complex-valued functions. No extra assumptions are needed.

---

## 4. Boundedness: the support argument

**The obstruction.** On all of $X = \mathcal{S}'$, $F_f$ is unbounded: $\phi_n = n\delta_0$ gives $|F_f(\phi_n)|\to\infty$. Portmanteau in the form "bounded continuous on all of $X$" does not apply.

**The fix.** We use the version of Portmanteau that only requires boundedness on a closed set containing the supports:

**Lemma (closed-support Portmanteau, Kallenberg 2002 Lemma 4.3; Billingsley 1999 Thm 2.1 applied to a closed subspace).** *Let $X$ be separable metrizable, $\{\mu_n\}$ Borel probability measures on $X$ with $\mu_n\to\mu$ weakly. Suppose there exists a closed $K\subseteq X$ with $\mathrm{supp}(\mu_n)\subseteq K$ for all $n$ and $\mathrm{supp}(\mu)\subseteq K$. If $G:X\to\mathbb{R}$ is bounded continuous on $K$, then $\int G\,d\mu_n\to\int G\,d\mu$.*

**Construction of $K_f$.** By compactness of $\mathrm{SU}(N)$ and $\mathbb{CP}^{N-1}$, the interpolated field $\mathcal{I}_a(\phi_a)(x)$ has norm bounded by an $a$-independent constant $C_N$ (depending only on the gauge group diameter). Hence for any lattice configuration,
$$|\langle f,\phi_a\rangle| \;\leq\; C_N\cdot a^4\sum_{x\in\Lambda_a}|f(x)| \;\leq\; C_N\cdot\|f\|_{L^1}\cdot(1+o(1)) \;\leq\; M_f, \tag{4}$$
with $M_f := 2C_N\|f\|_{L^1}$ (the $o(1)$ is the Riemann-sum error, uniformly small for $a$ below a threshold; for $a$ above the threshold we absorb a finite correction into $M_f$). Define
$$K_f \;:=\; \{\phi\in X : |\langle f,\phi\rangle|\leq M_f,\;|\langle\theta f,\phi\rangle|\leq M_f\}. \tag{5}$$
$K_f$ is closed in $X$ (intersection of preimages of closed intervals under continuous maps) and contains $\mathrm{supp}(\tilde\mu_a)$ for all $a$ by (4).

**Support propagation to the limit.** Apply weak convergence (3) to the bounded continuous truncation $G_k(\phi) := \min\bigl(k,\,(|\langle f,\phi\rangle|-M_f)_+\bigr)$. Each $\int G_k\,d\tilde\mu_a = 0$ since $\tilde\mu_a$ lives in $K_f$, so $\int G_k\,d\mu = 0$ by weak convergence. Letting $k\to\infty$ (monotone convergence), $\int(|\langle f,\phi\rangle|-M_f)_+\,d\mu = 0$, so $\mu$-almost every $\phi$ satisfies $|\langle f,\phi\rangle|\leq M_f$. Running the same argument with $\theta f$ gives $\mathrm{supp}(\mu)\subseteq K_f$.

**Boundedness of $F_f$ on $K_f$.** By (5), for $\phi\in K_f$, $|F_f(\phi)|\leq M_f^2$.

---

## 5. Rigorous Portmanteau application

With $X$, $K_f$, $\mu = \lim\tilde\mu_{a_j}$, and $G = F_f$ as above:
- $X$ is separable metrizable on the norm-bounded set $K_f$;
- $K_f$ is closed in $X$ and contains $\mathrm{supp}(\tilde\mu_{a_j})$ for all $j$ and $\mathrm{supp}(\mu)$;
- $F_f$ is continuous on $X$ (§3) and bounded by $M_f^2$ on $K_f$ (§4).

By the closed-support Portmanteau lemma,
$$\langle\theta f,f\rangle_\mu \;=\; \int F_f\,d\mu \;=\; \lim_{j\to\infty}\int F_f\,d\tilde\mu_{a_j} \;=\; \lim_{j\to\infty}\langle\theta f,f\rangle_{\tilde\mu_{a_j}} \;\geq\; 0,$$
the inequality from lattice RP (Lemma D.2). Therefore $\mu$ satisfies OS3.

---

## 6. Draft replacement of §5.7(f) OS3 Step 2

> **Step 2: Preservation under weak limits.** The continuum field space is $X := \mathcal{S}'(\mathbb{R}^4,\mathfrak{g})$ equipped with the weak-$*$ topology. The lattice measures $\tilde\mu_a$, obtained by pushing $\mu_a$ onto $X$ via the standard block-spin interpolation, converge weakly to the continuum measure $\mu$ along the Banach–Alaoglu subsequence of Step 1 (by Hamburger–Nussbaum applied to the OS0' moment bound; Glimm–Jaffe Thm 6.1.2). For $f\in\mathcal{S}$ supported in the positive-time half-space, $F_f(\phi) = \overline{\langle f,\phi\rangle}\langle\theta f,\phi\rangle$ is weak-$*$ continuous on $X$ (direct from the definition of the weak-$*$ topology and $\theta f\in\mathcal{S}$). $F_f$ is *not* bounded on all of $X$, but by compactness of $\mathrm{SU}(N)$ and $\mathbb{CP}^{N-1}$ the interpolated field is pointwise bounded by an $a$-independent constant, so there is $M_f<\infty$ with $|\langle f,\phi_a\rangle|\leq M_f$ for every lattice configuration. Let $K_f := \{\phi\in X : |\langle f,\phi\rangle|\leq M_f,\, |\langle\theta f,\phi\rangle|\leq M_f\}$; then $\mathrm{supp}(\tilde\mu_a)\subseteq K_f$ for every $a$, and applying weak convergence to the bounded continuous truncations $\min(k,(|\langle f,\cdot\rangle|-M_f)_+)$ and letting $k\to\infty$ shows $\mathrm{supp}(\mu)\subseteq K_f$ as well. On $K_f$, $|F_f|\leq M_f^2$.
>
> Now apply Portmanteau in the closed-support form (Kallenberg 2002, Lemma 4.3; Billingsley 1999, Theorem 2.1 on the closed subspace $K_f$): if $\tilde\mu_a\to\mu$ weakly and $G$ is bounded continuous on $K_f\supseteq\bigcup_a\mathrm{supp}(\tilde\mu_a)\cup\mathrm{supp}(\mu)$, then $\int G\,d\tilde\mu_a\to\int G\,d\mu$. With $G=F_f$:
> $$\langle\theta f,f\rangle_\mu = \int F_f\,d\mu = \lim_{a\to 0}\int F_f\,d\tilde\mu_a = \lim_{a\to 0}\langle\theta f,f\rangle_{\tilde\mu_a}\geq 0,$$
> the last inequality from lattice RP (Lemma D.2). Therefore OS3 holds for $\mu$. $\square$

This replaces lines ~2192–2216. The topology (weak-$*$ on $\mathcal{S}'(\mathbb{R}^4,\mathfrak{g})$) is named, the boundedness is stated on the common support set $K_f$, support containment is propagated to the limit, and the Portmanteau form used is explicit (closed-support version, Kallenberg 2002 Lemma 4.3).
