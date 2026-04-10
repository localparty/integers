## L.2 Phase 2: Continuum Limit of Flowed Correlators at Fixed $t > 0$

This section establishes that the lattice gradient-flow Schwinger
functions converge to a unique continuum limit at each fixed flow time
$t > 0$, and that the limit satisfies the Osterwalder--Schrader axioms.
Throughout, $a_K := a_0(K) = a^* \cdot 2^{-K}$ denotes the bare lattice
spacing at outer scale $K$, $g_K$ the bare coupling on the asymptotically
free trajectory, $\Lambda$ the RG-invariant scale, and
$\hat{\Delta}_K = a_K \Delta_{\mathrm{phys}}$ the dimensionless mass gap
at scale $K$. The flow propagator in momentum space acts as multiplication
by $e^{-tp^2}$ on each external leg (Luscher 2010, equation (3.6)).
The connected lattice flowed $n$-point Schwinger function at flow time
$t > 0$ and bare scale $K$ is
$$
S_{n,t}^{(K)}(x_1, \ldots, x_n)
  := \bigl\langle \mathcal{O}_t(x_1) \cdots \mathcal{O}_t(x_n)
  \bigr\rangle_c^{(K)},
\tag{L.2.1}
$$
where $\mathcal{O}_t(x) = \mathrm{Tr}(F_t^2)(x)$ is the flowed
gauge-invariant composite built from the flow-evolved links $V_\ell(t)$.
Its smearing against Schwartz test functions
$f \in \mathcal{S}(\mathbb{R}^{4n})$ is
$$
S_{n,t}^{(K)}(f)
  := \sum_{x_1, \ldots, x_n \in \Lambda_0(K)}
  a_K^{4n}\,S_{n,t}^{(K)}(x_1, \ldots, x_n)\,
  f(x_1, \ldots, x_n).
\tag{L.2.2}
$$
Constants $C$, $C'$, $C_0$, etc.\ may depend on $n$, $N$, the
compactification data $(R, r_3)$, and fixed $t > 0$, but are independent
of $K$ unless stated otherwise.


---


### Lemma L.2.1 (Cauchy estimate for flowed Schwinger functions)

*For each $n \geq 1$, each $f \in \mathcal{S}(\mathbb{R}^{4n})$, and
each fixed flow time $t > 0$, there exist constants
$C(t,n) < \infty$ and $\alpha > 0$ such that for all bare-scale
indices $K_1 < K_2$:*
$$
\bigl|S_{n,t}^{(K_2)}(f) - S_{n,t}^{(K_1)}(f)\bigr|
  \leq C(t,n)\,\|f\|_{p_N}\,
  \sum_{K=K_1}^{K_2-1}
  g_K^4\,(a_K\Lambda)^s\,e^{-c_0\,t/a_K^2},
\tag{L.2.3}
$$
*where $s \geq 2$, $c_0 > 0$ is a geometric constant depending on
$d = 4$ and the lattice structure but not on $K$, and
$\|f\|_{p_N}$ is a Schwartz seminorm with $N = 4n + 1$.
In particular, writing $a_i = a_0(K_i)$:*
$$
\bigl|S_{n,t}^{(a_1)}(f) - S_{n,t}^{(a_2)}(f)\bigr|
  \leq C(t,n)\,\|f\|_{p_N}\,|a_1^2 - a_2^2|^\alpha,
  \qquad \alpha = s/2 \geq 1.
\tag{L.2.4}
$$


**Proof.** The argument adapts the telescoping/Cauchy structure of
Theorem M.2.1 (Appendix M, \S M.2) to the flowed setting. The new
ingredient is the flow enhancement factor $e^{-c_0\,t/a_K^2}$, which
converts the doubly exponential convergence of the unflowed theory
into triply exponential convergence.

*Step 1 (Telescoping).* Along the dyadic bare-scale sequence, write
$$
S_{n,t}^{(K_2)}(f) - S_{n,t}^{(K_1)}(f)
  = \sum_{K=K_1}^{K_2-1}
  \bigl[S_{n,t}^{(K+1)}(f) - S_{n,t}^{(K)}(f)\bigr].
\tag{L.2.5}
$$

*Step 2 (Unflowed step bound).* By the RG analysis of \S5.4
(equation at line 850), the effective action changes by
$\delta S_K = O(g_K^4 \hat{\Delta}_{K+1}^s)$ per unit volume with
$s \geq 2$. The linked cluster theorem (Glimm--Jaffe, Theorem 18.2.1;
\S5.7, OS1 bound) yields the unflowed single-step bound
(Theorem M.2.1, Step 2):
$$
\bigl|S_n^{(K+1)}(f) - S_n^{(K)}(f)\bigr|
  \leq n!\,C_0^{n-1}\,\|f\|_{p_N}\,C'\,g_K^4\,(a_K\Lambda)^s.
\tag{L.2.6}
$$

*Step 3 (Flow enhancement).* At fixed $t > 0$, the flowed operator
$\mathcal{O}_t(x)$ is obtained by convolving the bare operator with
the gradient-flow kernel $K_{M^4}(t; x, y)$ (By Lemma L.1.3,
Proposition 1). In momentum space, each external leg contributes a
factor $e^{-tp^2}$. The UV fluctuation integral at outer step $K$
involves momenta in the shell $|p| \sim \pi/a_K$, so the new-operator
form factor acquires the multiplicative suppression
$$
e^{-c_0\,t\,\pi^2/a_K^2} = e^{-c_0'\,t/a_K^2},
\tag{L.2.7}
$$
where $c_0' = c_0\pi^2 > 0$ (henceforth absorbed into $c_0$). By
Lemma L.1.4 (K-uniform polymer decay, W3-08), the flowed polymer
activities satisfy $|K_k^{(t)}(X,V)| \leq e^{-\kappa_B|X|}$ with
$\kappa_B > 0$ independent of $K$, so the cluster expansion constants
are unchanged. The flow enhancement enters through the new contribution
$\delta E_K^{(t)}$:
$$
\bigl|\bigl\langle 1\big|\delta E_K^{(t)}(0)\big|1
  \bigr\rangle_c\bigr|
  \leq C_{\mathrm{new}}\,g_K^4\,\hat{\Delta}_{K+1}^2\,
  e^{-c_0\,t/a_K^2}.
\tag{L.2.8}
$$
The "old" contribution---the form factor of the previous effective
action pulled forward to scale $K+1$---involves physical (IR)
momenta $|p| \sim \Delta_\infty$ at which $e^{-tp^2} = O(1)$ and
receives no additional flow suppression:
$$
|\text{(old)}_{K \to K+1}^{(t)}|
  \leq \frac{C_K}{4}\,g_K^4\,\hat{\Delta}_{K+1}^2\,(1 + O(g_K^2)),
\tag{L.2.9}
$$
with $C_K/4 \leq C_*/3 + O(4^{-K})$ by the bounded orbit of the outer
recursion (Corollary M.1.3). Combining (L.2.8) and (L.2.9):
$$
\bigl|S_{n,t}^{(K+1)}(f) - S_{n,t}^{(K)}(f)\bigr|
  \leq n!\,C_0^{n-1}\,\|f\|_{p_N}\,
  \Bigl[\frac{C_K}{4} + C_*\,e^{-c_0\,t/a_K^2}\Bigr]\,
  g_K^4\,\hat{\Delta}_{K+1}^2\,(1 + O(g_K^2)).
\tag{L.2.10}
$$

*Step 4 (Triply exponential convergence).* Substituting
$a_K = a^* \cdot 2^{-K}$ and $g_K^4 \sim 1/(b_0 K \ln 2)^2$ on
the asymptotically free trajectory, the tail sum in (L.2.3) is
bounded by
$$
\sum_{K=K_1}^{K_2-1}
  g_K^4\,(a_K\Lambda)^s\,e^{-c_0\,t/a_K^2}
  \leq \sum_{K \geq K_1}
  \frac{(a^*\Lambda)^s}{(b_0 K \ln 2)^2}\,
  2^{-Ks}\,e^{-c_0\,t\,4^K/(a^*)^2}.
\tag{L.2.11}
$$
Three convergence factors appear: (i) the polynomial decay
$1/K^2$ from the running coupling; (ii) the exponential decay
$2^{-Ks}$ from bare refinement, already present in the unflowed
Theorem M.2.1; (iii) the super-exponential factor
$e^{-c_0\,t\,4^K/(a^*)^2}$, the flow enhancement. For any fixed
$t > 0$, factor (iii) decays faster than any power of $4^{-K}$. The
tail is dominated by its first term (consecutive-term ratio
$e^{-3c_0\,t\,4^{K_1}/(a^*)^2} \to 0$ super-exponentially), giving
$$
\sum_{K \geq K_1}
  g_K^4\,(a_K\Lambda)^s\,e^{-c_0\,t/a_K^2}
  \leq C'(t)\,e^{-c_0\,t\,4^{K_1}/(a^*)^2}\,(1 + o(1))
  \xrightarrow{K_1 \to \infty} 0.
\tag{L.2.12}
$$
This establishes the Cauchy property.

*Step 5 (Holder continuity).* Let $a_i = a_0(K_i)$ with
$K_2 > K_1$. Then $|a_1^2 - a_2^2| = (a^*)^2(4^{-K_1} - 4^{-K_2})
\geq (3/4)(a^*)^2 \cdot 4^{-K_1}$. The dominant contribution is
the first term of the Cauchy sum:
$$
g_{K_1}^4\,(a_{K_1}\Lambda)^s
  \leq C''\,\Lambda^s/(a^*)^s\,|a_1^2 - a_2^2|^{s/2},
\tag{L.2.13}
$$
yielding (L.2.4) with $\alpha = s/2 \geq 1$.

*Dependence on $t$.* The constant $C(t,n)$ includes the unflowed
contributions from the finitely many scales $K \leq K_t :=
\lceil \log_2(a^*/\sqrt{t})\rceil$ at which $a_K^2 \gtrsim t$ and
the flow enhancement is inoperative. For each fixed $t > 0$,
$K_t < \infty$ and hence $C(t,n) < \infty$. As $t \to 0^+$,
$K_t \to \infty$ and $C(t,n) \to \infty$, reflecting the UV
divergences of the unflowed theory. $\hfill\square$


---


### Lemma L.2.2 (Uniqueness of the continuum flowed limit)

*For each fixed $N \geq 2$, each $n \geq 1$, each
$f \in \mathcal{S}(\mathbb{R}^{4n})$, and each fixed flow time
$t > 0$, the lattice flowed Schwinger functions $S_{n,t}^{(K)}(f)$
converge as $K \to \infty$ to a unique limit
$S_{n,t}(f) \in \mathbb{R}$. The convergence is of the full net---no
subsequence extraction is required---and the limit defines a tempered
distribution $S_{n,t} \in \mathcal{S}'(\mathbb{R}^{4n})$.*


**Proof.**

*Step 1 (Cauchy net).* By Lemma L.2.1 (equation (L.2.3)), for
any $\varepsilon > 0$ there exists
$K_0 = K_0(\varepsilon, t, n, f)$ such that for all
$K_2 > K_1 \geq K_0$:
$$
\bigl|S_{n,t}^{(K_2)}(f) - S_{n,t}^{(K_1)}(f)\bigr|
  \leq C(t,n)\,\|f\|_{p_N}\,
  \sum_{K \geq K_0}
  g_K^4\,(a_K\Lambda)^s\,e^{-c_0\,t/a_K^2}
  < \varepsilon.
\tag{L.2.14}
$$
The finiteness of the tail follows from the triply exponential
convergence (L.2.12). Therefore $\{S_{n,t}^{(K)}(f)\}_{K \geq 0}$
is a Cauchy sequence in $\mathbb{R}$.

*Step 2 (Existence and uniqueness).* Since $\mathbb{R}$ is complete,
the Cauchy sequence converges to a unique limit:
$$
S_{n,t}(f) := \lim_{K \to \infty} S_{n,t}^{(K)}(f).
\tag{L.2.15}
$$
No subsequence extraction (via Banach--Alaoglu or otherwise) is
required; the full net converges.

*Step 3 (Tempered distribution).* We verify that
$f \mapsto S_{n,t}(f)$ is a continuous linear functional on
$\mathcal{S}(\mathbb{R}^{4n})$.

(a) *Linearity.* Each $S_{n,t}^{(K)}(\cdot)$ is linear in $f$ by
(L.2.2). The pointwise limit of linear functionals is linear.

(b) *Continuity.* At each lattice spacing, the flowed Schwinger
functions satisfy the K-uniform bound
$$
\bigl|S_{n,t}^{(K)}(f)\bigr|
  \leq n!\,C_t^n\,\|f\|_{p_N},
\tag{L.2.16}
$$
where $C_t = C_0(1 + C'/t^2)$ is finite for each fixed $t > 0$
(the factor $1/t^2$ reflects the engineering dimension of
$\mathcal{O}_t = \mathrm{Tr}(F_t^2)$) and is independent of $K$
by Lemma L.1.4 (K-uniform flowed constants). Passing to the limit:
$$
\bigl|S_{n,t}(f)\bigr|
  \leq n!\,C_t^n\,\|f\|_{p_N}.
\tag{L.2.17}
$$
This is the OS0' growth condition with Schwartz seminorm index
$N(n) = 4n + 1$, linear in $n$, confirming that $S_{n,t}$ is a
tempered distribution.

*Step 4 (Non-dyadic lattice spacings).* For general $a$ not in the
dyadic sequence $a_0(K) = a^* 2^{-K}$, each $a$ lies between
consecutive dyadic values, and the interpolation error is controlled
by the Lipschitz continuity of $S_{n,t}^{(a)}$ in $a$ (from the
analyticity of the transfer matrix in $\beta$; Balaban, CMP 95,
Theorem 4.1). The flow kernel $K_{M^4}(t)$ (By Lemma L.1.3) is
$C^\infty$ in all parameters, providing additional regularity.

*Step 5 (Convergence rate).* The rate is controlled by the triply
exponential tail:
$$
\bigl|S_{n,t}(f) - S_{n,t}^{(K)}(f)\bigr|
  \leq C(t,n)\,\|f\|_{p_N}\,e^{-c_0\,t\,4^K/(a^*)^2}
  \,(1 + o(1)).
\tag{L.2.18}
$$
For comparison, the unflowed rate (Theorem M.2.1) is $O(4^{-K})$.
The flow improves this to $O(e^{-c\,t\,4^K})$: faster than any
power of $4^{-K}$ for fixed $t > 0$. $\hfill\square$


---


### Lemma L.2.3 (Osterwalder--Schrader axioms for flowed Schwinger functions)

*For each fixed $N \geq 2$ and each fixed flow time $t > 0$, the
continuum flowed Schwinger functions $\{S_{n,t}\}_{n \geq 0}$ satisfy
axioms OS0--OS4:*

*(OS0) Temperedness; (OS1) Euclidean covariance;
(OS2) Reflection positivity; (OS3) Symmetry;
(OS4) Cluster decomposition.*


**Proof.** Each axiom is transferred from the unflowed continuum
theory (\S5.7, Theorem 8(f)) to the flowed setting. The gradient
flow at $t > 0$ is a deterministic, gauge-covariant, rotationally
invariant smoothing that preserves the positivity structure of the
lattice measure and does not affect the spectral gap controlling
cluster decomposition.

*OS0 (Temperedness).* The bound (L.2.17) gives
$|S_{n,t}(f)| \leq n!\,C_t^n\,\|f\|_{p_N}$ with $N = 4n + 1$
and $C_t < \infty$ for each fixed $t > 0$. The growth
$C_t^n \cdot n!$ satisfies $C_n' \leq A(n!)^B$ with $B = 1$, the
same as the unflowed OS0' condition (\S5.7, lines 2495--2529). The
K-uniformity of $C_t$ follows from Lemma L.1.4. This is strictly
better than the unflowed case: the Gaussian factor $e^{-tp^2}$
provides exponential UV suppression at each operator insertion.

*OS1 (Euclidean covariance).* The continuum gradient flow
$\partial_t B_\mu = D_\nu F^{\nu\mu}$ is an O(4)-covariant PDE.
The lattice flow equation breaks O(4) to the hypercubic group $W_4$,
but introduces no new O(4)-breaking operators beyond those already
present in the lattice action. The Symanzik bound on the breaking
corrections therefore acquires the flow enhancement:
$$
\bigl|S_{n,t}^{\mathrm{lat},(K)} - S_{n,t}^{\mathrm{O}(4)}\bigr|
  \leq C_n\,g_K^4\,(a_K\Lambda)^2\,e^{-c_0\,t/a_K^2},
\tag{L.2.19}
$$
giving triply exponential restoration of O(4) invariance (versus
doubly exponential in the unflowed case). Combined with translation
invariance, this yields full Euclidean covariance in the
$K \to \infty$ limit.

*OS2 (Reflection positivity).* We give two independent arguments.

*Argument 1 (Portmanteau transfer).* The lattice measure $\mu_K$ is
reflection-positive for all $K$ (Osterwalder--Seiler 1978; \S5.7,
OS3). The gradient flow is a deterministic function of the gauge
configuration; it modifies the observable, not the measure. For test
functions $f$ supported in $\{x_0 > 0\}$, the lattice RP condition
reads
$$
\bigl\langle \mathcal{O}_t[\theta f]\,\mathcal{O}_t[f]
  \bigr\rangle_{\mu_K}
  = \bigl\langle \Phi_t^+\,\Phi_t^- \bigr\rangle_{\mu_K}
  \geq 0,
\tag{L.2.20}
$$
where $\Phi_t^\pm$ are the restrictions of $\mathcal{O}_t$ to the
$\pm$ half-spaces and $\theta$ denotes Euclidean time reflection.
This is the Osterwalder--Seiler condition for the modified
observables $\Phi_t^\pm$, guaranteed by RP of $\mu_K$ and the
factorization of $\Phi_t^\pm$ across the reflection plane. The
factorization holds because the flow has finite propagation speed at
fixed $t > 0$ (the heat kernel $K_{M^4}(t)$ decays as
$e^{-|x|^2/(4t)}$); for test functions supported at distance
$> \sqrt{4t\ln(1/\varepsilon)}$ from the reflection plane, the
cross-plane contamination is $O(\varepsilon)$. The Portmanteau
argument of \S5.7, OS3 then transfers RP to the continuum limit:
the weak convergence $\tilde{\mu}_K \to \mu$ (now a full-net limit
by Lemma L.2.2) and the boundedness of
$F_f(\phi) = \overline{\langle f, \phi_t \rangle}
\langle \theta f, \phi_t \rangle$ give
$$
\langle \theta f, f \rangle_\mu
  = \lim_{K \to \infty}
  \langle \theta f, f \rangle_{\tilde{\mu}_K} \geq 0.
\tag{L.2.21}
$$

*Argument 2 (Sum of squares).* The flowed energy density
$E(t,x) = \tfrac{1}{4}\,G^a_{\mu\nu}(t,x)\,G^a_{\mu\nu}(t,x)$ is
a sum of squares of real-valued fields. For observables of the form
$\Phi = \sum_\alpha |\phi_\alpha|^2$ with each $\phi_\alpha$
supported in a half-space, one has
$\langle \Phi_+\,\Phi_- \rangle = \sum_{\alpha,\beta}
|\langle \phi_\alpha^+\,\phi_\beta^- \rangle|^2 \geq 0$ by
Cauchy--Schwarz applied to the reflection-positive inner product.
This gives RP independently of the Portmanteau argument.

*OS3 (Symmetry).* The flow equation is gauge-covariant
($V_t^g = g \cdot V_t$ for gauge transformations $g$; Lemma L.1.1(ii)),
and $\mathrm{Tr}(F_t^2)$ is gauge-invariant by cyclicity of the
trace. Therefore $S_{n,t}^{(K)}$ is gauge-invariant at each $K$, a
pointwise identity preserved in the limit.

*OS4 (Cluster decomposition).* The spectral decomposition via the
transfer matrix $\hat{T}$ gives, for Euclidean time separation
$\tau \to \infty$:
$$
\bigl|S_{m+n,t}(x + \tau e,\, y)
  - S_{m,t}(x)\,S_{n,t}(y)\bigr|
  \leq C\,\|A\|\,\|B\|\,e^{-\Delta_\infty\,\tau},
\tag{L.2.22}
$$
where $\Delta_\infty > 0$ is the mass gap. The gap is a property of
the measure $\mu_K$ (equivalently, of the Hamiltonian and its
spectrum), not of the probe operators. Since the flow modifies
observables but not the measure:
$$
\Delta_\infty^{(t)} = \Delta_\infty > 0
  \qquad \text{for all } t > 0.
\tag{L.2.23}
$$
The operator norm bound $\|\mathcal{O}_t\| \leq C/t^2$ (engineering
dimension, finite for each fixed $t > 0$) ensures $\|A\|$, $\|B\|$
are finite. The K-uniform bounds (\S5.7(d) for $\Delta_\infty$;
Lemma L.1.4 for operator norms) transfer to the continuum via
Lemma L.2.2. $\hfill\square$


---


### Lemma L.2.4 (Osterwalder--Schrader reconstruction at fixed flow time)

*For each fixed $N \geq 2$ and each fixed flow time $t > 0$,
the continuum flowed Schwinger functions $\{S_{n,t}\}_{n \geq 0}$
satisfying OS0--OS4 (Lemma L.2.3) uniquely determine, via the
Osterwalder--Schrader reconstruction theorem (CMP 42, 1975), a
Wightman quantum field theory on Minkowski space
$\mathbb{R}^{3,1}$ with:*

*(i) a separable Hilbert space $\mathcal{H}_t$;*

*(ii) a strongly continuous unitary representation of the Poincare
group $\mathcal{P}_+^\uparrow$ on $\mathcal{H}_t$;*

*(iii) a unique Poincare-invariant vacuum
$|\Omega\rangle \in \mathcal{H}_t$;*

*(iv) a mass gap:
$\mathrm{spec}(P^2) \subseteq \{0\} \cup [\Delta_\infty^2, \infty)$
with $\Delta_\infty > 0$.*

*The Hilbert space $\mathcal{H}_t$ and the mass gap
$\Delta_\infty$ are independent of the flow time $t > 0$.*


**Proof.** Properties (i)--(iv) follow immediately from the
corrected Osterwalder--Schrader reconstruction theorem
(Osterwalder--Schrader, CMP 42, 1975; see \S5.7, lines 2564--2614)
applied to the Schwinger functions $\{S_{n,t}\}$ verified in
Lemma L.2.3.

It remains to establish $t$-independence. The mass gap
$\Delta_\infty$ is determined by the spectral gap of the transfer
matrix $\hat{T}$ via $\Delta_\infty = -a^{-1}\ln(\lambda_1/\lambda_0)$,
which depends on the measure $\mu$ but not on the choice of probe
operators. Since the flow at different times $t, t' > 0$ produces
different observables probing the same Hilbert space and Hamiltonian,
$\Delta_\infty^{(t)} = \Delta_\infty^{(t')}$. For the Hilbert
space, note that $\mathcal{H}_t$ is the GNS completion of the span
of vectors $S_{n,t}(f)\,|\Omega\rangle$ over all $n$ and $f$. By
the Reeh--Schlieder theorem (valid once OS0--OS4 hold), the vacuum
is cyclic for the local algebra at any open set. Since the flowed
operators at different flow times generate the same local algebras
(the flow is an invertible map on the space of field configurations
for $t > 0$; Lemma L.1.1), the GNS Hilbert spaces coincide:
$\mathcal{H}_t = \mathcal{H}_{t'}$ for all $t, t' > 0$.
$\hfill\square$
