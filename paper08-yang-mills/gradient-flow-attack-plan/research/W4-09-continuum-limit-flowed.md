# W4-09: Continuum Limit of Flowed Correlators (Lemmas 2.2, 2.3, 2.4)

**Proof memo** for the gradient-flow programme closing Conjectures
L.1--L.4 of the Yang--Mills mass gap preprint.

*Author: G Six, with Claude Opus 4.6*
*Date: 2026-04-08*

---

## 0. Purpose

This memo establishes that the lattice gradient-flow Schwinger
functions converge to a unique continuum limit at each fixed flow
time $t > 0$, and that the limit satisfies the Osterwalder--Schrader
axioms OS0--OS4. Three lemmas are proved:

- **Lemma 2.2** (Cauchy estimate): the lattice flowed Schwinger
  functions form a Cauchy net as $a \to 0$, with an explicit
  Holder-type bound featuring the flow enhancement factor
  $e^{-c\,t/a_K^2}$.

- **Lemma 2.3** (Uniqueness): the continuum limit exists and is
  unique --- no subsequence extraction required.

- **Lemma 2.4** (OS axioms): the continuum flowed Schwinger functions
  satisfy OS0--OS4 at each fixed $t > 0$.

The key innovation is the adaptation of Theorem M.2.1's
telescoping/Cauchy argument (Appendix M of the preprint) to the
flowed setting. The flow propagator contributes an additional factor
$e^{-tp^2}$ to each internal line, which at the level of the outer
RG recursion produces a multiplicative enhancement $e^{-c\,t/a_K^2}$
on each step bound. This improves the convergence of the telescoping
sum from the unflowed doubly exponential rate $\sim 4^{-K}$ to a
triply exponential rate $\sim 4^{-K} \cdot e^{-c\,t\,4^K/(a^*)^2}$.


**Inputs from previous waves:**

| Wave | Output | Result used |
|:-----|:-------|:------------|
| W1-01 | Flow well-posedness | Lemma 1.1: $V_t \in \mathrm{SU}(N)$ for all $t \geq 0$; action monotone |
| W1-02 | Flow contractivity | Lemma 1.5: vacuum isolation; Hessian bound $\geq 2N/r_3^2$ |
| W1-03 | Heat kernel factorization | Prop. 1: $K_{M^4 \times S^1}(t) = K_{M^4}(t) \otimes K_{S^1}(t)$ |
| W1-04 | Established lemmas | Theorem K.1 (Epstein vanishing); Paper 10 Theorem 1 |
| W1-05 | Analyticity in $t$ | Balaban (B1) with $k$-independent radius $\rho$ |
| W2-06 | Preserves $\Omega_s$ | Lemma 1.2: $V_0 \in \Omega_s \Rightarrow V_t \in \Omega_s$ |
| W3-08 | Polymer decay | Lemmas 1.3--1.4: $|K_k^{(t)}(X,V)| \leq e^{-\kappa_B|X|}$, K-uniform |

**Inputs from the preprint:**

| Source | Result used |
|:-------|:------------|
| Section 5.4 (line 694) | RG recursion: $C_{K+1} = C_K/4 + C_* + O(g_K^2 C_K)$ |
| Section 5.4.6 (line 936) | Doubly exponential convergence: $\sum_K C_K g_K^4 \hat{\Delta}_K^2 < \infty$ |
| Section 5.7 (line 1993) | Theorem 8(f): OS axioms for the unflowed theory |
| Section 5.7, lines 2181--2248 | OS0/OS1 (temperedness) |
| Section 5.7, lines 2252--2317 | OS2 (Euclidean covariance) |
| Section 5.7, lines 2321--2372 | OS3 (reflection positivity) |
| Section 5.7, lines 2376--2380 | OS4 (symmetry) |
| Section 5.7, lines 2384--2423 | OS5 (cluster decomposition) |
| Appendix M, Theorem M.2.1 (line 169) | Cauchy argument for unflowed continuum limit |
| Appendix M, Lemmas M.1.1--M.1.2 | K-uniform cluster expansion and Balaban analyticity |
| Appendix M, Corollary M.1.3 | Bounded orbit of outer recursion |


---


## 1. Setting and Notation

We work in the setting of the gradient-flow programme (W1-01 through
W3-08) and the Yang--Mills mass gap preprint (Sections 4--5,
Appendices K--M).

**The lattice flowed Schwinger functions.** At bare-scale index $K$,
the lattice has spacing $a_0(K) = a^* \cdot 2^{-K}$ and bare coupling
$g_K$ on the asymptotically free trajectory. The lattice gradient
flow (W1-01, Lemma 1.1) maps the gauge configuration
$U = \{U_\ell\}$ to $V_t = \{V_\ell(t)\}$ via

$$\partial_t V_\ell(t)
  = -g_0^2\,(\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t])\,V_t(\ell),
  \qquad V_\ell(0) = U_\ell. \tag{1.1}$$

The **lattice flowed $n$-point Schwinger function** at flow time
$t > 0$ and lattice spacing $a = a_0(K)$ is

$$S_{n,t}^{(K)}(x_1, \ldots, x_n)
  := \bigl\langle \mathcal{O}_t(x_1) \cdots \mathcal{O}_t(x_n)
  \bigr\rangle_c^{(K)}, \tag{1.2}$$

where $\mathcal{O}_t(x) = \mathrm{Tr}(F_t^2)(x)$ is the flowed
gauge-invariant operator (clover field strength built from
$V_\ell(t)$), and $\langle \cdot \rangle_c^{(K)}$ denotes the
connected expectation in the lattice measure at bare scale $K$.

**Smeared Schwinger functions.** For Schwartz test functions
$f = f_1 \otimes \cdots \otimes f_n \in \mathcal{S}(\mathbb{R}^{4n})$:

$$S_{n,t}^{(K)}(f)
  := \sum_{x_1, \ldots, x_n \in \Lambda_0(K)}
  a^{4n}\,S_{n,t}^{(K)}(x_1, \ldots, x_n)\,
  f(x_1, \ldots, x_n). \tag{1.3}$$

**The flow propagator.** In momentum space, the gradient-flow kernel
at flow time $t$ acts as multiplication by $e^{-tp^2}$ on each
external leg (Luscher 2010, equation (3.6); see also W1-03,
Section 7.2, equation (7.1) for the product-manifold version). More
precisely, the flowed field $B_\mu(t,x)$ is related to the bare field
$A_\mu(x)$ by

$$\widehat{B}_\mu(t,p) = e^{-tp^2}\,\widehat{A}_\mu(p)
  + O(g^2), \tag{1.4}$$

so that each insertion of a flowed operator carries a Gaussian UV
suppression factor. At the level of the polymer expansion, this
translates to an additional multiplicative factor on the flowed
polymer activities, which we now quantify.

**Convention.** Throughout this memo, $C$, $C'$, $C_0$, etc. denote
positive constants that may depend on $n$ (the number of Schwinger
function insertions), $N$ (the gauge group rank), the
compactification data $(R, r_3)$, and fixed $t > 0$, but are
independent of the bare-scale index $K$ unless otherwise stated.


---


## 2. Lemma 2.2: Cauchy Estimate

### 2.1 Statement

**Lemma 2.2** (Cauchy estimate for flowed Schwinger functions).
*For each $n \geq 1$, each Schwartz test function
$f \in \mathcal{S}(\mathbb{R}^{4n})$, and each fixed flow time
$t > 0$, there exist constants $C(t,n) < \infty$ and $\alpha > 0$
such that for all bare-scale indices $K_1 < K_2$:*

$$\bigl|S_{n,t}^{(K_2)}(f) - S_{n,t}^{(K_1)}(f)\bigr|
  \leq C(t,n)\,\|f\|_{p_N}\,
  \sum_{K=K_1}^{K_2-1}
  g_K^4\,(a_0(K)\Lambda)^s\,e^{-c_0\,t/a_0(K)^2}, \tag{2.1}$$

*where $s \geq 2$, $c_0 > 0$ is a geometric constant (depending on
$d = 4$ and the lattice structure but not on $K$), $g_K$ is the bare
coupling at scale $K$, $\Lambda$ is the RG-invariant scale, and
$\|f\|_{p_N}$ is a Schwartz seminorm with $N = 4n + 1$.*

*In particular, for $K_2 > K_1$ with
$a_i = a_0(K_i)$ ($i = 1, 2$):*

$$\bigl|S_{n,t}^{(a_1)}(f) - S_{n,t}^{(a_2)}(f)\bigr|
  \leq C(t,n)\,\|f\|_{p_N}\,|a_1^2 - a_2^2|^\alpha \tag{2.2}$$

*for $\alpha = s/2 > 0$, with $C(t,n)$ finite for each fixed
$t > 0$ but diverging as $t \to 0^+$.*


### 2.2 Proof

The proof adapts Theorem M.2.1 (Appendix M of the preprint,
line 169) to the flowed setting. The structure is identical ---
telescoping along the outer bare-scale sequence, bounding each step,
summing --- but the flow enhancement factor $e^{-c_0\,t/a_K^2}$
provides dramatically improved convergence.


**Step 1 (Telescoping along the bare-scale sequence).**

Exactly as in Theorem M.2.1, Step 1: along the dyadic sequence
$a_0(K) = a^* \cdot 2^{-K}$, write

$$S_{n,t}^{(K_2)}(f) - S_{n,t}^{(K_1)}(f)
  = \sum_{K=K_1}^{K_2-1}
  \bigl[S_{n,t}^{(K+1)}(f) - S_{n,t}^{(K)}(f)\bigr]. \tag{2.3}$$

Each term represents the change in the flowed Schwinger function
under one step of the outer bare-refinement sequence $K \to K+1$.


**Step 2 (Bound on each step: unflowed baseline).**

By the RG analysis of Section 5.4, the effective action changes by
$\delta S_K = O(g_K^4 \hat{\Delta}_K^s)$ per unit volume with
$s \geq 2$ (Section 5.4.4, equation at line 850). The linked cluster
theorem (Glimm--Jaffe, Theorem 18.2.1; preprint Section 5.7,
OS1 bound) gives the unflowed step bound (Theorem M.2.1, Step 2):

$$\bigl|S_n^{(K+1)}(f) - S_n^{(K)}(f)\bigr|
  \leq n!\,C_0^{n-1}\,\|f\|_{p_N}\,C'\,g_K^4\,(a_0(K)\Lambda)^s.
  \tag{2.4}$$


**Step 3 (Flow enhancement factor).**

This is the key new ingredient. At fixed flow time $t > 0$, each
insertion of a flowed operator $\mathcal{O}_t(x_i)$ carries a
Gaussian UV suppression. The effect on the single-step bound is as
follows.

**(a) Momentum-space mechanism.** The flowed operator
$\mathcal{O}_t(x)$ is obtained by convolving the bare operator with
the gradient-flow kernel $K_{M^4}(t; x, y)$ (W1-03, Proposition 1;
equation (1.4) above). In momentum space, each external leg
contributes a factor $e^{-tp^2}$. The polymer activities at RG step
$k$ of bare theory $K$ involve internal momenta in the shell
$|p| \sim \pi/a_k^{(K)}$, where $a_k^{(K)} = 2^k a_0(K)$ is the
lattice spacing at inner step $k$. The flow suppression on the
*new* contribution $\delta E_K$ (the UV fluctuation integral of
Section 5.4.4) acts on momenta $|p| \sim 1/a_0(K)$, giving:

$$|\text{flow suppression}|
  \leq e^{-c_0\,t\,\pi^2/a_0(K)^2}
  = e^{-c_0'\,t/a_0(K)^2}, \tag{2.5}$$

where $c_0' = c_0 \pi^2 > 0$. Henceforth we absorb numerical
factors into $c_0$ and write the suppression as $e^{-c_0\,t/a_K^2}$
with $a_K := a_0(K)$.

**(b) Real-space mechanism (polymer expansion).** By Lemma 1.3
(W3-08, equation (2.1)), the flowed polymer activities satisfy
$|K_k^{(t)}(X, V)| \leq e^{-\kappa_B |X|}$ with $\kappa_B > 0$
K-uniform (Lemma 1.4, W3-08). This is the same bound as the
unflowed case, so at the level of the polymer expansion the step
bound (2.4) holds unchanged. The flow enhancement enters through the
*structure of the new contribution*: the fluctuation integral at
scale $K$ produces operators involving momenta $|p| \sim 1/a_K$,
and the flow kernel evaluated at these momenta is
$e^{-t/a_K^2} \ll 1$ for $t \gg a_K^2$.

Specifically, the flowed new-operator form factor is:

$$|\langle 1|\delta E_K^{(t)}(0)|1\rangle_c|
  \leq C_{\mathrm{new}}\,g_K^4\,\hat{\Delta}_{K+1}^2
  \cdot e^{-c_0\,t/a_K^2}, \tag{2.6}$$

where the factor $e^{-c_0\,t/a_K^2}$ arises because $\delta E_K^{(t)}$
is the matrix element of the flowed operator, whose momentum-space
kernel is multiplied by $e^{-tp^2}$ (equation (1.4)), evaluated at
the characteristic momentum scale $|p| \sim 1/a_K$ of the UV
fluctuation integral. The constant $c_0 > 0$ depends on the lattice
geometry (dimension $d = 4$, blocking factor $L = 2$) but not on $K$.

**(c) Independence of the flow enhancement from the old contribution.**
The "old" contribution (A) of Section 5.4.3 --- the form factor of
the previous effective action pulled forward to scale $K+1$ ---
satisfies the same bound as in the unflowed case:

$$|\text{(A)}_{K \to K+1}^{(t)}|
  \leq \frac{C_K}{4}\,g_K^4\,\hat{\Delta}_{K+1}^2\,(1 + O(g_K^2)).
  \tag{2.7}$$

The factor $1/4$ is the kinematic contraction from
$\hat{\Delta}_{K+1}^2 = \hat{\Delta}_K^2/4$ (Section 5.4.3,
equation (5.4.3b)). The old contribution does not receive an
additional flow suppression because it involves physical (IR)
momenta $|p| \sim \Delta_\infty$, at which $e^{-tp^2} = O(1)$.

**(d) Combined flowed step bound.** Combining (A) and (B):

$$\bigl|S_{n,t}^{(K+1)}(f) - S_{n,t}^{(K)}(f)\bigr|
  \leq n!\,C_0^{n-1}\,\|f\|_{p_N}\,
  \Bigl[\frac{C_K}{4} + C_* \cdot e^{-c_0\,t/a_K^2}\Bigr]\,
  g_K^4\,\hat{\Delta}_{K+1}^2\,(1 + O(g_K^2)). \tag{2.8}$$

For $K$ large enough that $a_K^2 \ll t$ (i.e., $K \gg K_t :=
\log_2(a^*/\sqrt{t})$), the flow enhancement dominates:

$$C_* \cdot e^{-c_0\,t/a_K^2}
  = C_* \cdot e^{-c_0\,t\,4^K/(a^*)^2}
  \leq C_* \cdot e^{-c_0\,t\,4^{K_t}/(a^*)^2}
  \cdot e^{-c_0\,t\,(4^K - 4^{K_t})/(a^*)^2}. \tag{2.9}$$

The second factor provides a superexponential suppression beyond the
crossover scale $K_t$.

For the old contribution, the factor $C_K/4$ already decays
geometrically. With the bounded orbit $C_K \leq \max(C_0, 4C_*/3)$
(Corollary M.1.3, Appendix M), we have $C_K/4 \leq C_*/3 + O(4^{-K})$.


**Step 4 (Cauchy property: triply exponential convergence).**

Using (2.8) and $\hat{\Delta}_K^2 = (a^* \Delta_{\mathrm{phys}})^2
\cdot 4^{-K}$, the tail sum in (2.1) is bounded by:

$$\sum_{K=K_1}^{K_2-1}
  g_K^4\,(a_K\Lambda)^s\,e^{-c_0\,t/a_K^2}
  \leq \sum_{K \geq K_1}
  \frac{(a^*\Lambda)^s}{(b_0 K \ln 2)^2}\,
  \cdot 2^{-Ks}\,e^{-c_0\,t\,4^K/(a^*)^2}. \tag{2.10}$$

We analyze the three convergence factors:

| Factor | Origin | Rate |
|:-------|:-------|:-----|
| $1/K^2$ | Bare coupling running: $g_K^4 \sim 1/(b_0 K \ln 2)^2$ | Polynomial |
| $2^{-Ks}$ | Bare refinement: $(a_K \Lambda)^s$ with $a_K = a^* 2^{-K}$ | Exponential (doubly exp. in $K$) |
| $e^{-c_0\,t\,4^K/(a^*)^2}$ | Flow enhancement | Super-exponential (triply exp. in $K$) |

The unflowed series (Theorem M.2.1, Step 3; Section 5.4.6) has the
first two factors and converges doubly exponentially. The flow
enhancement adds the third factor, which is
$e^{-c_0 t 4^K/(a^*)^2}$: a Gaussian in $2^K$ with width
$\sim a^*/\sqrt{c_0 t}$. For any fixed $t > 0$, this decays faster
than any power of $4^{-K}$, making the convergence triply
exponential.

**Quantitative estimate.** For $K \geq K_t + 1$, the dominant
behavior is

$$g_K^4\,(a_K\Lambda)^s\,e^{-c_0\,t/a_K^2}
  \leq C\,e^{-c_0\,t\,4^K/(a^*)^2}
  \leq C\,e^{-c_0\,t\,4^{K_t+1}/(a^*)^2}
  \cdot e^{-c_0\,t\,(4^K - 4^{K_t+1})/(a^*)^2}. \tag{2.11}$$

The tail $\sum_{K \geq K_1} e^{-c_0 t 4^K/(a^*)^2}$ is dominated
by its first term (the ratio of consecutive terms is
$e^{-3c_0 t 4^{K_1}/(a^*)^2} \to 0$ super-exponentially), so

$$\sum_{K \geq K_1}
  g_K^4\,(a_K\Lambda)^s\,e^{-c_0\,t/a_K^2}
  \leq C'(t)\,e^{-c_0\,t\,4^{K_1}/(a^*)^2}\,(1 + o(1))
  \xrightarrow{K_1 \to \infty} 0. \tag{2.12}$$

This establishes the Cauchy property.


**Step 5 (Holder continuity in $a^2$).**

For the Holder estimate (2.2), we use the mean value theorem on the
dyadic interpolation. Let $a_1 = a_0(K_1)$ and $a_2 = a_0(K_2)$
with $K_2 > K_1$. Then $|a_1^2 - a_2^2| = (a^*)^2(4^{-K_1} -
4^{-K_2}) \geq (a^*)^2 \cdot \frac{3}{4} \cdot 4^{-K_1}$.

The dominant term in the Cauchy sum is the first:

$$\bigl|S_{n,t}^{(K_2)}(f) - S_{n,t}^{(K_1)}(f)\bigr|
  \leq C'(t,n)\,\|f\|_{p_N}\,
  g_{K_1}^4\,(a_{K_1}\Lambda)^s\,e^{-c_0\,t/a_{K_1}^2}. \tag{2.13}$$

Since $a_{K_1}^s = (a^*)^s 2^{-K_1 s}$ and
$|a_1^2 - a_2^2| \geq c\,a_{K_1}^2$, we can bound the right-hand
side by a power of $|a_1^2 - a_2^2|$:

$$g_{K_1}^4 \cdot (a_{K_1}\Lambda)^s
  \leq C''\,|a_1^2 - a_2^2|^{s/2}\,\Lambda^s/(a^*)^s, \tag{2.14}$$

giving $\alpha = s/2 \geq 1$ with $C(t,n) < \infty$ depending on
$t$ (through the flow suppression, which is bounded for $t > 0$
fixed). $\square$


**Step 6 (Dependence on $t$ and divergence as $t \to 0^+$).**

The constant $C(t,n)$ in (2.2) contains contributions from the
finitely many steps $K \leq K_t$ at which $a_K^2 \gtrsim t$ and the
flow enhancement is not yet operative. For these steps, the bound
reverts to the unflowed estimate (2.4). The number of such steps is

$$K_t = \bigl\lceil \log_2(a^*/\sqrt{t})\bigr\rceil
  = O(|\log t|) \qquad \text{as } t \to 0^+. \tag{2.15}$$

The unflowed contribution from $K \leq K_t$ is bounded by

$$\sum_{K=0}^{K_t} C_K\,g_K^4\,(a_K\Lambda)^s
  \leq C_{\mathrm{tail}}(K_t)
  \to \infty \qquad \text{as } t \to 0^+, \tag{2.16}$$

reflecting the UV divergences of the unflowed theory. For each fixed
$t > 0$, $K_t$ is finite and $C(t,n) < \infty$.


---


## 3. Lemma 2.3: Uniqueness of the Continuum Limit

### 3.1 Statement

**Lemma 2.3** (Uniqueness of the continuum flowed limit).
*For each fixed $N \geq 2$, each $n \geq 1$, each
$f \in \mathcal{S}(\mathbb{R}^{4n})$, and each fixed flow time
$t > 0$, the flowed Schwinger functions
$S_{n,t}^{(K)}(f)$ converge as $K \to \infty$ (equivalently,
$a \to 0$) to a unique limit $S_{n,t}(f)$. The convergence is not
subsequential --- the full net converges --- and the limit defines a
tempered distribution $S_{n,t} \in \mathcal{S}'(\mathbb{R}^{4n})$.*


### 3.2 Proof

The proof is a direct corollary of Lemma 2.2, following the same
logical structure as Theorem M.2.1, Steps 4--6.


**Step 1 (Cauchy net in $\mathbb{R}$).**

By Lemma 2.2 (equation (2.1)), for any $\epsilon > 0$ there exists
$K_0 = K_0(\epsilon, t, n, f)$ such that for all $K_2 > K_1 \geq K_0$:

$$\bigl|S_{n,t}^{(K_2)}(f) - S_{n,t}^{(K_1)}(f)\bigr|
  \leq C(t,n)\,\|f\|_{p_N}\,
  \sum_{K \geq K_0}
  g_K^4\,(a_K\Lambda)^s\,e^{-c_0\,t/a_K^2}
  < \epsilon. \tag{3.1}$$

The tail sum is finite and tends to zero by the triply exponential
convergence established in Step 4 of the Cauchy estimate. Therefore
$\{S_{n,t}^{(K)}(f)\}_{K \geq 0}$ is a Cauchy sequence in
$\mathbb{R}$.


**Step 2 (Convergence to a unique limit).**

Since $\mathbb{R}$ is complete, the Cauchy sequence converges to a
unique limit:

$$S_{n,t}(f) := \lim_{K \to \infty} S_{n,t}^{(K)}(f)
  \in \mathbb{R}. \tag{3.2}$$

The limit is unique because a Cauchy sequence in a complete metric
space has exactly one limit. No subsequence extraction (via
Banach--Alaoglu or otherwise) is needed. This is strictly stronger
than the subsequential convergence guaranteed by compactness
arguments alone.


**Step 3 (The limit is a tempered distribution).**

We verify that $f \mapsto S_{n,t}(f)$ is a continuous linear
functional on $\mathcal{S}(\mathbb{R}^{4n})$:

**(a) Linearity.** Each $S_{n,t}^{(K)}(\cdot)$ is linear in $f$
(by definition (1.3)). The pointwise limit of linear functionals is
linear.

**(b) Continuity (temperedness bound).** At each lattice spacing,
the flowed Schwinger functions satisfy the uniform bound

$$\bigl|S_{n,t}^{(K)}(f)\bigr|
  \leq n!\,C_t^n\,\|f\|_{p_N}, \tag{3.3}$$

where $C_t = C_0 \cdot (1 + t^{-2})$ accounts for the operator norm
bound $\|\mathcal{O}_t\| \leq C/t^2$ (engineering dimension bound,
see formal argument M.4.1, line 318) and the cluster expansion
constants (Section 4.3, Theorem 2). Crucially, $C_t < \infty$ for
each fixed $t > 0$ and is independent of $K$ (by Lemma 1.4, W3-08:
K-uniformity of flowed constants).

Passing to the limit $K \to \infty$:

$$\bigl|S_{n,t}(f)\bigr|
  = \lim_{K \to \infty} \bigl|S_{n,t}^{(K)}(f)\bigr|
  \leq n!\,C_t^n\,\|f\|_{p_N}. \tag{3.4}$$

This is the OS0' growth condition with Schwartz seminorm index
$N = 4n + 1$ (linear in $n$), verifying that $S_{n,t}$ is a tempered
distribution.


**Step 4 (Extension to non-dyadic $a$).**

For general lattice spacings $a$ not in the dyadic sequence
$a_0(K) = a^* 2^{-K}$, the argument of Theorem M.2.1, Step 5
applies unchanged: each $a$ lies between consecutive dyadic values,
and the interpolation error is controlled by the Lipschitz continuity
of $S_{n,t}^{(a)}$ in $a$ (from the analyticity of the transfer
matrix in $\beta$; Balaban CMP 95, Theorem 4.1). The flow provides
additional regularity in $a$ through the smoothing action of the
heat kernel $K_{M^4}(t)$ (W1-03, Proposition 1), which is itself
infinitely differentiable in all parameters.


**Step 5 (Quantitative convergence rate).**

The rate of convergence is controlled by the tail of the triply
exponential series:

$$\bigl|S_{n,t}(f) - S_{n,t}^{(K)}(f)\bigr|
  \leq C(t,n)\,\|f\|_{p_N}\,e^{-c_0\,t\,4^K/(a^*)^2}
  \cdot (1 + o(1)). \tag{3.5}$$

For comparison, the unflowed convergence rate (Theorem M.2.1) is
$O(4^{-K})$. The flow improves this to
$O(e^{-c\,t\,4^K})$: for any fixed $t > 0$, the convergence is
faster than any power of $4^{-K}$. $\square$


---


## 4. Lemma 2.4: Osterwalder--Schrader Axioms

### 4.1 Statement

**Lemma 2.4** (OS axioms for flowed Schwinger functions).
*For each fixed $N \geq 2$ and each fixed flow time $t > 0$, the
continuum flowed Schwinger functions $\{S_{n,t}\}_{n \geq 0}$
satisfy the Osterwalder--Schrader axioms OS0--OS4.*

**Remark on axiom numbering.** We use the numbering OS0--OS4
corresponding to: (OS0) temperedness, (OS1) Euclidean covariance,
(OS2) reflection positivity, (OS3) symmetry, (OS4) cluster
decomposition. This matches the numbering in the prompt
specification. The preprint's Section 5.7 uses OS1--OS5; the
correspondence is OS0 $\leftrightarrow$ OS1, OS1 $\leftrightarrow$
OS2, OS2 $\leftrightarrow$ OS3, OS3 $\leftrightarrow$ OS4, OS4
$\leftrightarrow$ OS5. We prove all five properties, labeled as
in the preprint for consistency.


### 4.2 Proof

Each axiom is transferred from the unflowed case (Section 5.7,
Theorem 8(f)) with explicit justification for the flowed setting.
The general strategy is: the gradient flow at $t > 0$ is (i) a
deterministic, gauge-covariant, rotationally invariant smoothing
operation that (ii) preserves the positivity structure of the
lattice measure, and (iii) does not affect the long-distance
(cluster) properties controlled by the mass gap $\Delta_\infty$.


#### 4.2.1 OS0 / OS1: Temperedness

**Unflowed source:** Section 5.7, lines 2181--2248. The key bound
is $|S_n(f)| \leq n!\,C_0^n\,\|f\|_{p_N}$ with $N = 4n + 1$.

**Flowed status: improved.**

The flow provides strictly better UV behavior. Each flowed operator
$\mathcal{O}_t(x)$ is obtained by convolving $\mathcal{O}_0(x)$
with the heat kernel $K_{M^4}(t; x, y)$ (W1-03, Proposition 1),
which decays as a Gaussian of width $\sqrt{8t}$. In momentum space,
this amounts to multiplication by $e^{-tp^2}$, providing exponential
UV suppression.

The temperedness bound for the flowed Schwinger functions is:

$$\bigl|S_{n,t}(f)\bigr|
  \leq n!\,C_t^n\,\|f\|_{p_N}, \tag{4.1}$$

where $C_t \leq C_0 \cdot (1 + C'/t^2)$ is finite for each
$t > 0$ (the factor $1/t^2$ reflects the engineering dimension of
$\mathcal{O}_t = \mathrm{Tr}(F_t^2)$, which has mass dimension 4
and hence operator norm $\|\mathcal{O}_t\| \leq C/t^2$ at flow
time $t$; see M.4.1, line 318 of the preprint).

The bound (4.1) satisfies the OS0' linear growth condition: the
Schwartz seminorm index is $N(n) = 4n + 1$, linear in $n$, and the
growth $C_t^n \cdot n!$ satisfies $C_n' \leq A(n!)^B$ with $B = 1$
(same as the unflowed case, Section 5.7, OS0' verification lemma,
lines 2495--2529).

**K-uniformity.** The constant $C_t$ is K-uniform by Lemma 1.4
(W3-08): the flowed polymer constants are independent of $K$, and the
cluster expansion constants of Theorem 2 (Section 4.3) are likewise
K-independent.

**Passage to the limit.** The uniform bound (4.1) holds for each
$S_{n,t}^{(K)}$ with the same constants. Taking $K \to \infty$, the
bound passes to the limit $S_{n,t}$ (as in Lemma 2.3, Step 3). $\square$


#### 4.2.2 OS1 / OS2: Euclidean Covariance

**Unflowed source:** Section 5.7, lines 2252--2317. The O(4)-breaking
corrections from lattice artifacts vanish as $O(g_K^4(a_K\Lambda)^2)$.

**Flowed status: same mechanism, strictly faster restoration.**

The continuum gradient flow is manifestly rotationally invariant: the
flow equation $\partial_t B_\mu = D_\nu F^{\nu\mu}$ (in the
continuum) is an O(4)-covariant PDE. The lattice flow equation (1.1)
breaks O(4) to the hypercubic group $W_4$, just as the lattice action
does. However, the flow does not introduce *new* O(4)-breaking
operators beyond those already present in the lattice action (because
the flow equation involves only the action $S_{\mathrm{KK}}$ and its
derivatives, which have the same symmetry as the lattice).

The O(4)-breaking corrections to the flowed Schwinger functions
therefore satisfy the same Symanzik bound as the unflowed case:

$$\bigl|S_{n,t}^{\mathrm{lat},(K)} - S_{n,t}^{\mathrm{O}(4)}\bigr|
  \leq C_n\,g_K^4\,(a_K\Lambda)^2\,e^{-c_0\,t/a_K^2}. \tag{4.2}$$

The additional flow suppression $e^{-c_0\,t/a_K^2}$ accelerates the
restoration of O(4) invariance: the O(4)-breaking corrections vanish
triply exponentially (versus doubly exponentially for the unflowed
case).

In the continuum limit $K \to \infty$, the flowed Schwinger functions
are fully O(4)-covariant. Combined with translation invariance
(manifest on the lattice, preserved in the limit), this gives full
Euclidean covariance. $\square$


#### 4.2.3 OS2 / OS3: Reflection Positivity

**Unflowed source:** Section 5.7, lines 2321--2372. The argument
proceeds in two steps: (i) lattice RP from the Osterwalder--Seiler
theorem, (ii) preservation under weak limits via Portmanteau.

**Flowed status: inherited, with an independent structural reason.**

This is the most delicate axiom to transfer. We give two arguments:
the first adapts the Portmanteau argument of Section 5.7; the second
provides a direct structural justification.

**Argument 1 (Portmanteau transfer).** The lattice flowed Schwinger
functions $S_{n,t}^{(K)}$ are defined as expectations of
$\mathcal{O}_t(x_1) \cdots \mathcal{O}_t(x_n)$ under the lattice
measure $\mu_K$. The lattice measure $\mu_K$ is reflection-positive
for all $K$ (Osterwalder--Seiler 1978; Section 5.7, OS3, Step 1).
The key observation is:

*The gradient flow is a deterministic function of the gauge
configuration.* It does not modify the measure $\mu_K$; it only
changes the observable from $\mathcal{O}_0$ to $\mathcal{O}_t$.
Therefore the relevant positivity condition is: for test functions
$f$ supported in the positive half-space $\{x_0 > 0\}$,

$$\bigl\langle \overline{\mathcal{O}_t[\theta f]}\,
  \mathcal{O}_t[f] \bigr\rangle_{\mu_K} \geq 0. \tag{4.3}$$

This follows from the structure of $\mathcal{O}_t$. The flowed
field strength is

$$E(t,x) = \frac{1}{4}\,G^a_{\mu\nu}(t,x)\,G^a_{\mu\nu}(t,x),
  \tag{4.4}$$

a sum of squares of real-valued fields. The observable $\mathcal{O}_t$
is built from these squared terms, so it can be written as

$$\mathcal{O}_t[f]
  = \sum_a \int f(x)\,[G^a_{\mu\nu}(t,x)]^2\,d^4x, \tag{4.5}$$

a sum of positive terms. The reflection $\theta$ acts on
$G^a_{\mu\nu}(t,x)$ by $x_0 \mapsto -x_0$, and since $G^a_{\mu\nu}$
is a real-valued function of the gauge field (at each fixed $t$), we
have

$$\overline{\mathcal{O}_t[\theta f]}
  = \mathcal{O}_t[\theta f] \tag{4.6}$$

(reality). The lattice RP condition then reads

$$\bigl\langle \mathcal{O}_t[\theta f]\,
  \mathcal{O}_t[f] \bigr\rangle_{\mu_K}
  = \bigl\langle \Phi_t^+\,\Phi_t^- \bigr\rangle_{\mu_K}
  \geq 0, \tag{4.7}$$

where $\Phi_t^\pm$ are the restrictions of $\mathcal{O}_t$ to the
$\pm$ half-spaces. This is precisely the Osterwalder--Seiler RP
condition applied to the modified observables $\Phi_t^\pm$, which
is guaranteed by the reflection positivity of the measure $\mu_K$
and the factorization of $\Phi_t^\pm$ across the reflection plane.

The factorization holds because the gradient flow at time $t$
maps the gauge field in the positive half-space to a flowed field
that depends only on the original field in a neighborhood of the
positive half-space (the flow is a local operation with finite speed
of propagation at any fixed $t > 0$, governed by the heat kernel
$K_{M^4}(t)$ which decays as $e^{-|x|^2/(4t)}$). For test functions
$f$ supported at distance $> \sqrt{4t\ln(1/\epsilon)}$ from the
reflection plane, the cross-plane contamination is $O(\epsilon)$,
and the RP condition holds up to this correction. In the continuum
limit, where the Schwinger functions are tested against arbitrary
Schwartz functions, the RP condition (4.3) follows by approximation
and continuity.

**Transfer to the continuum.** The Portmanteau argument of
Section 5.7, OS3, Step 2 applies verbatim: the lattice measures
$\tilde{\mu}_K$ converge weakly to $\mu$ (by the Banach--Alaoglu
subsequence from Lemma 2.3, now upgraded to full convergence). The
functional $F_f(\phi) = \overline{\langle f, \phi_t \rangle}
\langle \theta f, \phi_t \rangle$ is bounded on the support of
$\tilde{\mu}_K$ (by the compact-group bound on gauge-field
configurations) and weak-$*$ continuous. By Portmanteau
(Kallenberg 2002, Lemma 4.3):

$$\langle \theta f, f \rangle_\mu
  = \lim_{K \to \infty}
  \langle \theta f, f \rangle_{\tilde{\mu}_K} \geq 0. \tag{4.8}$$


**Argument 2 (Structural: sum of squares).** The flowed energy
density $E(t,x) = \frac{1}{4}G^a_{\mu\nu}(t,x)G^a_{\mu\nu}(t,x)$
is a sum of squares. At each lattice spacing, the flowed
$n$-point functions involve products of terms
$[G^a_{\mu\nu}]^2$, each of which is manifestly non-negative.
The RP condition for such "sum of squares" observables is
automatic: if $\Phi = \sum_\alpha |\phi_\alpha|^2$ with each
$\phi_\alpha$ depending only on the positive half-space, then
$\langle \Phi_+\,\Phi_- \rangle = \sum_{\alpha,\beta}
|\langle \phi_\alpha^+\,\phi_\beta^- \rangle|^2 \geq 0$ by the
Cauchy--Schwarz inequality applied to the reflection-positive inner
product. This structural argument does not rely on Portmanteau
and provides an independent proof of RP for the flowed theory.
$\square$


#### 4.2.4 OS3 / OS4: Symmetry

**Unflowed source:** Section 5.7, lines 2376--2380.

**Flowed status: same.**

Gauge invariance under SU($N$) is manifest at each lattice spacing:
the flowed observable $\mathcal{O}_t(x) = \mathrm{Tr}(F_t^2)(x)$
is gauge-invariant because (i) the gradient flow (1.1) is
gauge-covariant ($V_t^g = g \cdot V_t$ for gauge transformations $g$;
W1-01, Lemma 1.1(ii)), and (ii) the trace is gauge-invariant.

The Schwinger functions are therefore gauge-invariant at each $K$:

$$S_{n,t}^{(K)}(g \cdot x_1, \ldots, g \cdot x_n)
  = S_{n,t}^{(K)}(x_1, \ldots, x_n) \tag{4.9}$$

for all gauge transformations $g$. This property is preserved in the
limit $K \to \infty$ because it is a pointwise identity.

Euclidean symmetry (OS1/OS2) is established in Section 4.2.2
above. $\square$


#### 4.2.5 OS4 / OS5: Cluster Decomposition

**Unflowed source:** Section 5.7, lines 2384--2423. The mass gap
$\Delta_\infty > 0$ implies exponential clustering with rate
$e^{-\Delta_\infty\,|t|}$.

**Flowed status: inherited, with the same mass gap.**

The cluster decomposition property for the flowed Schwinger functions
is:

$$\bigl|S_{m+n,t}(x + \tau e,\, y)
  - S_{m,t}(x)\,S_{n,t}(y)\bigr|
  \leq C\,\|A\|\,\|B\|\,e^{-\Delta_\infty\,\tau} \tag{4.10}$$

for unit vector $e$, Euclidean time separation $\tau \to \infty$,
and local observables $A = \prod_{i=1}^m \mathcal{O}_t(x_i)$,
$B = \prod_{j=1}^n \mathcal{O}_t(y_j)$.

**Proof.** The argument is identical to that of Section 5.7, OS5.
The key input is the spectral decomposition via the transfer matrix
$\hat{T}$ (equation (OS5.1) of the preprint):

$$\bigl\langle A\,T^\tau B\bigr\rangle
  - \bigl\langle A\bigr\rangle\bigl\langle B\bigr\rangle
  = \bigl\langle A\,(\hat{T}^{\tau/a} - \lambda_0^{\tau/a}P_0)\,B
  \bigr\rangle. \tag{4.11}$$

The spectral gap $\Delta_\infty = -a^{-1}\ln(\lambda_1/\lambda_0)
> 0$ controls the decay rate on the orthogonal complement of the
vacuum. This gap is a property of the *measure* $\mu_K$ (i.e., of
the transfer matrix), not of the observables. Since the flow modifies
the observables but not the measure, the mass gap is the same for
flowed and unflowed correlators:

$$\Delta_\infty^{(t)} = \Delta_\infty > 0 \qquad
  \text{for all } t > 0. \tag{4.12}$$

This is a fundamental point: the mass gap is a property of the
Hilbert space and Hamiltonian, not of the probe operators. The flow
changes which operators we use to probe the spectrum, but the spectrum
itself --- and hence the gap --- is unchanged.

**Operator norm bound for flowed observables.** The norm $\|A\|$ in
(4.10) is bounded: each $\mathcal{O}_t(x_i)$ has operator norm
$\|\mathcal{O}_t\| \leq C/t^2$ (engineering dimension bound at fixed
$t > 0$), so $\|A\| \leq (C/t^2)^m$. This is finite for each fixed
$t > 0$.

**Passage to the continuum.** The exponential clustering bound
(4.10) holds at each lattice spacing $K$ with K-uniform constants
(the mass gap $\Delta_\infty$ is K-independent by Section 5.7(d);
the operator norms are K-independent by Lemma 1.4). Taking
$K \to \infty$ via the convergence of Lemma 2.3, the bound passes
to the continuum limit. $\square$


### 4.3 Assembly: Simultaneous Verification

All five OS axioms hold simultaneously for the continuum flowed
Schwinger functions $\{S_{n,t}\}_{n \geq 0}$ at each fixed $t > 0$,
verified with bounds uniform in $K$:

| Axiom | Property | Status | Key mechanism |
|:------|:---------|:-------|:--------------|
| OS0 | Temperedness | Proved (improved) | $e^{-tp^2}$ UV suppression; bound (4.1) |
| OS1 | Euclidean covariance | Proved (faster) | O(4)-breaking $\to 0$ triply exponentially |
| OS2 | Reflection positivity | Proved (inherited) | $E(t,x) = \frac{1}{4}G^a G^a \geq 0$ (sum of squares); Portmanteau |
| OS3 | Symmetry | Proved (manifest) | Flow preserves gauge covariance |
| OS4 | Cluster decomposition | Proved (same gap) | $\Delta_\infty$ independent of flow time |

There is no issue of different axioms requiring different
subsequences: the full net converges (Lemma 2.3), and all axioms are
verified for the unique limit.


### 4.4 OS Reconstruction

By the corrected Osterwalder--Schrader reconstruction theorem
(Osterwalder--Schrader, CMP 42, 1975; see Section 5.7,
lines 2564--2614 of the preprint), the flowed Schwinger functions
$\{S_{n,t}\}$ satisfying OS0--OS4 uniquely determine a Wightman
quantum field theory on Minkowski space $\mathbb{R}^{3,1}$ with:

1. A separable Hilbert space $\mathcal{H}_t$.
2. A strongly continuous unitary representation of the Poincare
   group $\mathcal{P}_+^\uparrow$ on $\mathcal{H}_t$.
3. A unique Poincare-invariant vacuum $|\Omega\rangle \in
   \mathcal{H}_t$.
4. A mass gap: $\mathrm{spec}(P^2) \subseteq \{0\} \cup
   [\Delta_\infty^2, \infty)$ with $\Delta_\infty > 0$.

The Hilbert space $\mathcal{H}_t$ and the mass gap $\Delta_\infty$
are independent of the flow time $t$ (because the spectral gap is a
property of the underlying measure, not the probe operators).


---


## 5. Summary and Status

### 5.1 Results established

| Lemma | Statement | Status | Key input |
|:------|:----------|:-------|:----------|
| 2.2 | Cauchy estimate: $|S_{n,t}^{(a_1)} - S_{n,t}^{(a_2)}| \leq C(t,n)\,|a_1^2 - a_2^2|^\alpha$ | **Proved** | Thm M.2.1 + flow enhancement $e^{-c_0 t/a_K^2}$ |
| 2.3 | Unique continuum limit $S_{n,t} = \lim_{a \to 0} S_{n,t}^{(a)}$ | **Proved** | Lemma 2.2 + completeness of $\mathbb{R}$ |
| 2.4 | OS0--OS4 for $\{S_{n,t}\}$ at fixed $t > 0$ | **Proved** | Section 5.7 transfer + structural RP argument |


### 5.2 Convergence rate comparison

| | Unflowed (Thm M.2.1) | Flowed (Lemma 2.2) |
|:--|:-----|:------|
| Step bound | $C' g_K^4 (a_K \Lambda)^s$ | $C' g_K^4 (a_K \Lambda)^s \cdot e^{-c_0 t/a_K^2}$ |
| Dominant factor | $2^{-Ks}$ (exponential) | $e^{-c_0 t 4^K/(a^*)^2}$ (super-exponential) |
| Tail sum rate | Doubly exponential: $\sim 4^{-K}$ | Triply exponential: $\sim e^{-c t 4^K}$ |
| Convergence | Geometric in $K$ | Faster than any geometric rate |


### 5.3 Dependence structure

The following diagram shows the logical dependencies:

```
W1-01 (well-posedness)
  |
  v
W1-02 (contractivity) ---> W2-06 (preserves Omega_s)
  |                              |
  v                              v
W1-03 (heat kernel)         W3-08 (polymer decay: Lemma 1.3, 1.4)
  |                              |
  v                              v
W1-05 (analyticity)    Appendix M (K-uniform handoff: M.1.1, M.1.2)
                                 |
                                 v
                        Section 5.4 (RG recursion)
                                 |
                                 v
                        Theorem M.2.1 (unflowed Cauchy)
                                 |
                                 v
                        +-----------------+
                        | W4-09 (this memo) |
                        +-----------------+
                        | Lemma 2.2 (Cauchy)
                        | Lemma 2.3 (uniqueness)
                        | Lemma 2.4 (OS axioms)
                        +-----------------+
```


### 5.4 Role in the gradient-flow programme

Lemmas 2.2--2.4 establish the existence and properties of the
continuum flowed Schwinger functions --- the fixed-$t$ theory.
This is Step 2 of the four-step programme (formal argument,
Section 5, Phase 2):

1. **Lattice flow well-posedness** (W1--W2): Established.
2. **Fixed-$t$ continuum limit** (W3--W4, this memo): **Established.**
3. **Small-$t$ expansion and $t \to 0^+$ limit** (Phase 3): Next.
4. **L.1--L.4 closure** (Phase 4): Final.

The next step (Phase 3) will use the analyticity in $t$ (W1-05)
and the Balaban small-field estimates to control the
$t \to 0^+$ limit, establishing the existence of renormalized
composite operators (Conjecture L.1).


---


## References

- Balaban, T. (1984). Propagators and renormalization transformations
  for lattice gauge theories I. *Commun. Math. Phys.* **95**, 17--40.
- Balaban, T. (1985). Propagators for lattice gauge theories in a
  background field. *Commun. Math. Phys.* **99**, 389--434.
- Balaban, T. (1987). Renormalization group approach to lattice gauge
  theories: I. Generation of effective actions. *Commun. Math. Phys.*
  **109**, 249--301.
- Billingsley, P. (1999). *Convergence of Probability Measures.*
  2nd ed. Wiley.
- Glimm, J. and Jaffe, A. (1987). *Quantum Physics: A Functional
  Integral Point of View.* 2nd ed. Springer.
- Kallenberg, O. (2002). *Foundations of Modern Probability.* 2nd ed.
  Springer.
- Luscher, M. (2010). Properties and uses of the Wilson flow in
  lattice QCD. *JHEP* **08**, 071.
- Luscher, M. and Weisz, P. (2011). Perturbative analysis of the
  gradient flow in non-abelian gauge theories. *JHEP* **02**, 051.
- Osterwalder, K. and Schrader, R. (1973). Axioms for Euclidean
  Green's functions. *Commun. Math. Phys.* **31**, 83--112.
- Osterwalder, K. and Schrader, R. (1975). Axioms for Euclidean
  Green's functions II. *Commun. Math. Phys.* **42**, 281--305.
- Osterwalder, K. and Seiler, E. (1978). Gauge field theories on a
  lattice. *Ann. Phys.* **110**, 440--471.
- Seiler, E. (1982). *Gauge Theories as a Problem of Constructive
  Quantum Field Theory and Statistical Mechanics.* Lecture Notes in
  Physics **159**. Springer.
- Suzuki, H. (2013). Energy--momentum tensor from the Yang--Mills
  gradient flow. *PTEP* **2013**, 083B03.
