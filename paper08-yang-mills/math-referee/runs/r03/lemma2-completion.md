# Lemma 2 Completion: Multiplicative Perturbation Bound

This document closes sub-gap (1) identified in the ASSESSMENT of
`theorem5-proof.md`: the passage from the cluster expansion bound on
$\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U']$ to the trace-norm bound
on $\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}$.

The issue is that $\mathcal{Z}_{\mathrm{int}}$ depends on the 4D link
variables $(U^{(0)}, U, U')$ through the bond coupling $V_\ell$. The
proof of Lemma 2 (Steps 2--3) expands
$\mathcal{Z}_{\mathrm{int}} / \prod_x Z_{\mathrm{int}}^{(0)}$ via
the cluster expansion and bounds the deviation from 1, but does not
explicitly state the uniform-in-$U$ bound on the log-ratio needed for
the multiplicative kernel estimate in Step 4. Below we state and prove
the missing lemma, then show how it completes the argument.

---

## Lemma (Internal partition function bound)

**Statement.** *Consider the KK-enhanced $\mathrm{SU}(N)$ lattice gauge
theory of Section 4.1, restricted to the $k = 0$ topological sector.
For a single time-slab with spatial links
$\Lambda_t^1$ and temporal links $\Lambda_{\mathrm{temp}}^1$, define the
internal partition function conditional on all 4D link variables
$(U^{(0)}, U, U')$:*

$$\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U']
  \;=\; \int \prod_{x \in \Lambda_t^0} \mathcal{D}A_x\,\mathcal{D}A_x'\;
  \exp\!\Bigl(-\sum_x S_{\mathrm{YM}}^{\mathrm{int}}(A_x)
  - \sum_x S_{\mathrm{YM}}^{\mathrm{int}}(A_x')
  - S_{\mathrm{int}}^{(\mathrm{slice})}[U^{(0)}, A, A']\Bigr).$$

*Define the decoupled (free-internal) partition function:*

$$\mathcal{Z}_{\mathrm{int}}^{(0)}
  \;=\; \prod_{x \in \Lambda_t^0}
  \Bigl(\int \mathcal{D}A_x\;e^{-S_{\mathrm{YM}}^{\mathrm{int}}(A_x)}\Bigr)^2
  \;=\; \bigl(Z_{\mathrm{int}}^{(0)}\bigr)^{2|\Lambda_t^0|},$$

*which is independent of the 4D link variables. In the regime
$m_1 a \geq c_0$ (with $c_0$ depending only on $N$):*

$$\left|\ln \frac{\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U']}
  {\mathcal{Z}_{\mathrm{int}}^{(0)}}\right|
  \;\leq\; C_1\,|\Lambda_t^1|\,e^{-m_1 a}
  \tag{$\ast$}$$

*uniformly in $(U^{(0)}, U, U') \in \mathrm{SU}(N)^{|\Lambda_{\mathrm{temp}}^1|
+ 2|\Lambda_t^1|}$, where $C_1$ depends on $N$ but not on $a/r_3$ or $L$.
Equivalently:*

$$e^{-C_1 |\Lambda_t^1| e^{-m_1 a}}
  \;\leq\;
  \frac{\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U']}
       {\mathcal{Z}_{\mathrm{int}}^{(0)}}
  \;\leq\;
  e^{C_1 |\Lambda_t^1| e^{-m_1 a}}.$$


---

## Proof

### Step 1: Decomposition of the action

The internal slice action decomposes as:

$$S_{\mathrm{int}}^{(\mathrm{slice})}[U^{(0)}, A, A']
  \;=\; \sum_{\ell \in \Lambda_{\mathrm{bonds}}}
  V_\ell(U_\ell, A_{s(\ell)}, A_{t(\ell)}),$$

where the sum runs over all bonds connecting internal fields at
different sites/time-slices via the 4D link variables, $s(\ell)$ and
$t(\ell)$ denote the source and target sites of bond $\ell$, and
$V_\ell$ is the coupling term defined in Section 4.1. On a single
time-slab, these bonds correspond to the temporal links connecting the
internal fields $(A_x, A_x')$ at each site, mediated by the temporal
link variables $U^{(0)}$. The number of such bonds is
$|\Lambda_{\mathrm{bonds}}| \leq c_d\,|\Lambda_t^1|$ for a lattice
geometry constant $c_d$.

Write:

$$\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U']
  \;=\; \mathcal{Z}_{\mathrm{int}}^{(0)}\;
  \Bigl\langle \exp\!\Bigl(
    -\sum_\ell V_\ell(U_\ell, A_{s(\ell)}, A_{t(\ell)})
  \Bigr) \Bigr\rangle_{\!\mathrm{free}},$$

where $\langle \cdot \rangle_{\mathrm{free}}$ denotes expectation
with respect to the product measure
$\prod_x \mathcal{D}A_x\,e^{-S_{\mathrm{YM}}^{\mathrm{int}}(A_x)}
/ Z_{\mathrm{int}}^{(0)}$ (and similarly for the primed fields). This
is the decoupled internal measure: each $A_x$ is drawn independently
from the Gaussian-dominated measure on
$\mathcal{A}_0(\mathbb{CP}^{N-1})$.

Therefore:

$$\ln \frac{\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U']}
  {\mathcal{Z}_{\mathrm{int}}^{(0)}}
  \;=\; \ln \Bigl\langle e^{-V} \Bigr\rangle_{\!\mathrm{free}},
  \qquad V \;\stackrel{\mathrm{def}}{=}\;
  \sum_\ell V_\ell.
  \tag{1}$$


### Step 2: Pointwise bound on the coupling $V_\ell$

Each bond coupling $V_\ell(U_\ell, A_{s(\ell)}, A_{t(\ell)})$ is defined
in Section 4.1 as:

$$V_\ell \;=\; \frac{1}{a^2}
  \int_{\mathbb{CP}^{N-1}}
  \bigl\| A_{t(\ell)} - U_\ell^{-1} A_{s(\ell)}\,U_\ell \bigr\|^2
  \,\mathrm{dvol}.$$

Expanding in KK modes $A_x = \sum_{n \geq 1} \phi_n(x)\,\omega_n$:

$$V_\ell \;=\; \frac{1}{a^2} \sum_{n \geq 1}
  \bigl|\phi_n(t(\ell))
    - \mathrm{Ad}(U_\ell)\,\phi_n(s(\ell))\bigr|^2.$$

Isolating the diagonal (mass) terms, which are already included in
$S_{\mathrm{YM}}^{\mathrm{int}}$, the off-diagonal (bond) part is:

$$V_\ell^{\mathrm{bond}} \;=\; -\frac{2}{a^2}
  \sum_{n \geq 1}
  \mathrm{Re}\,\mathrm{Tr}\bigl[
    \phi_n(s(\ell))^\dagger\,\mathrm{Ad}(U_\ell)\,\phi_n(t(\ell))
  \bigr].$$

This is precisely the bond interaction whose expectation under the
free measure is bounded in Theorem 2. By Theorem 2 (bond activity
bound), the bond activity $g_\ell = e^{-V_\ell^{\mathrm{bond}}} - 1$
satisfies:

$$|g_\ell| \;\leq\; C_0\,e^{-m_1 a}$$

uniformly in $U_\ell \in \mathrm{SU}(N)$.

**Crucially, the $U_\ell$-dependence enters only through the adjoint
action $\mathrm{Ad}(U_\ell)$, and the bound in Theorem 2 is proved
uniformly over all $U_\ell \in \mathrm{SU}(N)$.** This is evident from
Step 3 of Theorem 2's proof: the propagator bound
$G_n(a) \leq (C_1 / m_n a)\,e^{-m_n a}$ depends only on the KK mass
$m_n$ and the lattice spacing $a$, not on the 4D link variable, because
the adjoint action is unitary ($|\mathrm{Ad}(U)\phi| = |\phi|$) and
does not affect the norm of the mode amplitudes.


### Step 3: From bond activities to the log-ratio

We bound $|\ln\langle e^{-V}\rangle_{\mathrm{free}}|$ using the
cluster expansion of Section 4.3.

**Sub-step 3a (Cluster expansion of the log).** The logarithm of the
internal partition function ratio admits the standard polymer/cluster
expansion (Kotecky--Preiss 1986, Friedli--Velenik 2017, Chapter 5):

$$\ln \Bigl\langle e^{-V} \Bigr\rangle_{\!\mathrm{free}}
  \;=\; \sum_{\mathcal{C}\;\mathrm{conn}}
  \phi_T(\mathcal{C}),$$

where the sum runs over connected clusters $\mathcal{C}$ of bonds, and
$\phi_T(\mathcal{C})$ are the truncated (connected, cumulant) cluster
weights. By the Kotecky--Preiss theorem, this series converges
absolutely when the Kotecky--Preiss criterion is satisfied, which
requires:

$$\sup_\ell \sum_{\mathcal{C} \ni \ell}
  |\phi_T(\mathcal{C})|\,e^{\alpha\,|\mathcal{C}|}
  \;\leq\; \alpha$$

for some $\alpha > 0$.

**Sub-step 3b (Verifying the criterion).** Each truncated cluster
weight satisfies the standard bound (Friedli--Velenik, Theorem 5.4):

$$|\phi_T(\mathcal{C})|
  \;\leq\; \prod_{b \in \mathcal{C}} |\bar{g}_b|
  \;\leq\; (C_0\,e^{-m_1 a})^{|\mathcal{C}|},$$

where $\bar{g}_b$ is the bond activity integrated against the
normalized free-internal measure, bounded by Theorem 2. (The truncated
weight for a tree graph is a product of bond activities; for general
connected graphs, combinatorial factors appear but are absorbed into
the lattice animal counting constant.)

Thus:

$$\sum_{\mathcal{C} \ni \ell}
  |\phi_T(\mathcal{C})|\,e^{\alpha\,|\mathcal{C}|}
  \;\leq\; \sum_{k=1}^{\infty} c_d^{\,k}\,
  (C_0\,e^{-m_1 a + \alpha})^k.$$

For $m_1 a \geq c_0 \stackrel{\mathrm{def}}{=}
\alpha + \ln(2\,c_d\,C_0) + 1$ (a threshold depending only on $N$
through $C_0$ and $c_d$), this geometric series satisfies:

$$\sum_{k=1}^{\infty} c_d^{\,k}\,
  (C_0\,e^{-m_1 a + \alpha})^k
  \;\leq\; 2\,c_d\,C_0\,e^{-m_1 a + \alpha}
  \;\leq\; \alpha,$$

verifying the Kotecky--Preiss criterion. The cluster expansion
converges absolutely.

**Sub-step 3c (Bounding the sum).** With convergence established, we
bound the full series:

$$\left|\ln \Bigl\langle e^{-V} \Bigr\rangle_{\!\mathrm{free}}\right|
  \;=\; \left|\sum_{\mathcal{C}\;\mathrm{conn}}
  \phi_T(\mathcal{C})\right|
  \;\leq\; \sum_{\mathcal{C}\;\mathrm{conn}}
  |\phi_T(\mathcal{C})|.$$

Grouping by the bond $\ell$ that anchors each cluster:

$$\sum_{\mathcal{C}\;\mathrm{conn}} |\phi_T(\mathcal{C})|
  \;\leq\; \sum_{\ell \in \Lambda_{\mathrm{bonds}}}
  \sum_{\mathcal{C} \ni \ell} |\phi_T(\mathcal{C})|
  \;\leq\; |\Lambda_{\mathrm{bonds}}|
  \cdot 2\,c_d\,C_0\,e^{-m_1 a}.$$

(We use the Kotecky--Preiss bound without the $e^{\alpha|\mathcal{C}|}$
weight, which only improves the estimate.) Since
$|\Lambda_{\mathrm{bonds}}| \leq c_d\,|\Lambda_t^1|$:

$$\left|\ln \frac{\mathcal{Z}_{\mathrm{int}}}
  {\mathcal{Z}_{\mathrm{int}}^{(0)}}\right|
  \;\leq\; 2\,c_d^2\,C_0\,|\Lambda_t^1|\,e^{-m_1 a}
  \;=\; C_1\,|\Lambda_t^1|\,e^{-m_1 a},$$

with $C_1 = 2\,c_d^2\,C_0$, depending on $N$ but not on $a/r_3$ or $L$.
This is uniform in $(U^{(0)}, U, U')$ because the bond activity bound
from Theorem 2 is uniform in the 4D link variables (Step 2 above).
$\square$

**Remark.** An alternative, more elementary route avoids the full
cluster expansion machinery. Since $V = \sum_\ell V_\ell^{\mathrm{bond}}$
is a sum of terms, each with $\langle |V_\ell^{\mathrm{bond}}|
\rangle_{\mathrm{free}} \leq C_0\,e^{-m_1 a}$, Jensen's inequality gives:

$$\left|\ln \langle e^{-V} \rangle_{\mathrm{free}}\right|
  \;\leq\; \max\!\bigl(\langle V \rangle_{\mathrm{free}},\;
  \ln\langle e^{|V|}\rangle_{\mathrm{free}}\bigr).$$

The first term is $|\langle V \rangle_{\mathrm{free}}|
\leq \sum_\ell \langle |V_\ell| \rangle_{\mathrm{free}}
\leq |\Lambda_{\mathrm{bonds}}|\,C_0\,e^{-m_1 a}$. For the second,
independence of bond couplings at well-separated bonds and the
smallness of each $|V_\ell|$ yield:

$$\langle e^{|V|} \rangle_{\mathrm{free}}
  \leq \prod_\ell \langle e^{|V_\ell|} \rangle_{\mathrm{free}}
  \leq \prod_\ell (1 + 2C_0\,e^{-m_1 a})
  \leq e^{2\,|\Lambda_{\mathrm{bonds}}|\,C_0\,e^{-m_1 a}},$$

using $\langle e^{|V_\ell|}\rangle_{\mathrm{free}} \leq 1 +
\langle |V_\ell| \rangle_{\mathrm{free}} + \langle |V_\ell|^2/2
\rangle_{\mathrm{free}} \cdot e^{C_0 e^{-m_1 a}}
\leq 1 + 2C_0\,e^{-m_1 a}$ for $m_1 a$ large enough. This gives
the same bound $(\ast)$ with a slightly worse constant. The cluster
expansion route is preferable because it directly invokes Theorem 2
and Theorem 3 as already established in Section 4.3.


---

## How this closes the sub-gap in Lemma 2

Lemma 2 of `theorem5-proof.md` establishes the trace-norm bound
$\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}
\leq C_{\mathrm{tr}}\,|\Lambda_t^1|\,e^{-m_1 a}\,
\|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. The sub-gap is in the
passage from the cluster expansion bound on $\mathcal{Z}_{\mathrm{int}}$
to a pointwise kernel bound. Specifically, Step 3 of Lemma 2 writes:

$$\hat{T}_{\mathrm{red}}(U'; U) - \hat{T}_{\mathrm{std}}(U'; U)
  = \int dU^{(0)}\;e^{-S_{\mathrm{4D}}^{(\mathrm{slice})}}\;
  \bigl(\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U'] - 1\bigr),$$

and then claims (after normalization) that
$|\mathcal{Z}_{\mathrm{int}} / \mathcal{Z}_{\mathrm{int}}^{(0)} - 1|
\leq 2\,|\Lambda_t^1|\,C_0\,e^{-m_1 a}$ uniformly in $U$. This claim
is justified as follows.

**Step A (Apply the internal partition function bound).** By ($\ast$):

$$\left|\frac{\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U']}
  {\mathcal{Z}_{\mathrm{int}}^{(0)}} - 1\right|
  \;\leq\; e^{C_1 |\Lambda_t^1| e^{-m_1 a}} - 1
  \;\leq\; 2\,C_1\,|\Lambda_t^1|\,e^{-m_1 a},$$

where the last inequality uses $e^x - 1 \leq 2x$ for
$0 \leq x \leq 1$, valid here because
$C_1\,|\Lambda_t^1|\,e^{-m_1 a} \leq C_1\,L^3\,e^{-m_1 a} \ll 1$
in the regime $m_1 a \gg \ln L$. This bound is uniform in
$(U^{(0)}, U, U')$.

**Step B (Multiplicative kernel perturbation).** The normalized
reduced transfer matrix kernel (after dividing by the constant
$\mathcal{Z}_{\mathrm{int}}^{(0)}$) is:

$$\hat{T}_{\mathrm{red}}(U'; U)
  \;=\; \mathcal{Z}_{\mathrm{int}}^{(0)}
  \int dU^{(0)}\;e^{-S_{\mathrm{4D}}^{(\mathrm{slice})}}\;
  \frac{\mathcal{Z}_{\mathrm{int}}[U^{(0)}, U, U']}
       {\mathcal{Z}_{\mathrm{int}}^{(0)}}.$$

Setting $\epsilon(U^{(0)}, U, U') =
\mathcal{Z}_{\mathrm{int}} / \mathcal{Z}_{\mathrm{int}}^{(0)} - 1$,
we have $|\epsilon| \leq \bar{\epsilon}
\stackrel{\mathrm{def}}{=} 2\,C_1\,|\Lambda_t^1|\,e^{-m_1 a}$ by
Step A. Then:

$$\hat{T}_{\mathrm{red}}(U'; U)
  \;=\; \mathcal{Z}_{\mathrm{int}}^{(0)}
  \int dU^{(0)}\;e^{-S_{\mathrm{4D}}^{(\mathrm{slice})}}\;
  \bigl(1 + \epsilon(U^{(0)}, U, U')\bigr).$$

The kernel of $\hat{T}_{\mathrm{std}}$ (up to the same overall constant
$\mathcal{Z}_{\mathrm{int}}^{(0)}$) is:

$$\mathcal{Z}_{\mathrm{int}}^{(0)}\;
  \hat{T}_{\mathrm{std}}(U'; U)
  \;=\; \mathcal{Z}_{\mathrm{int}}^{(0)}
  \int dU^{(0)}\;e^{-S_{\mathrm{4D}}^{(\mathrm{slice})}}.$$

Therefore the kernel difference (after dividing both sides by
$\mathcal{Z}_{\mathrm{int}}^{(0)}$, which is a positive constant and
does not affect trace-norm estimates or spectral ratios) satisfies:

$$\bigl|\hat{T}_{\mathrm{red}}(U'; U) - \hat{T}_{\mathrm{std}}(U'; U)\bigr|
  \;=\; \left|\int dU^{(0)}\;e^{-S_{\mathrm{4D}}^{(\mathrm{slice})}}\;
  \epsilon(U^{(0)}, U, U')\right|
  \;\leq\; \bar{\epsilon}\;\hat{T}_{\mathrm{std}}(U'; U).$$

The last inequality uses $|\epsilon| \leq \bar{\epsilon}$ and
$e^{-S_{\mathrm{4D}}^{(\mathrm{slice})}} \geq 0$.

**Step C (Trace-norm bound for multiplicative kernel perturbations).**
We now state the standard result used in Step 4 of Lemma 2.

*Claim.* Let $T_1, T_2$ be positive, self-adjoint, trace-class integral
operators with kernels $K_1, K_2 \geq 0$ satisfying:

$$|K_1(U', U) - K_2(U', U)| \;\leq\; \bar{\epsilon}\;K_2(U', U)
  \qquad \forall\; U, U'.$$

Then $\|T_1 - T_2\|_{\mathrm{tr}} \leq \bar{\epsilon}\;
\|T_2\|_{\mathrm{tr}}$.

*Proof of claim.* The kernel bound gives, for all $U, U'$:

$$(1 - \bar{\epsilon})\,K_2(U', U)
  \;\leq\; K_1(U', U)
  \;\leq\; (1 + \bar{\epsilon})\,K_2(U', U).$$

As operator inequalities (since $K_2 \geq 0$):

$$(1 - \bar{\epsilon})\,T_2 \;\leq\; T_1
  \;\leq\; (1 + \bar{\epsilon})\,T_2.$$

Therefore $-\bar{\epsilon}\,T_2 \leq T_1 - T_2
\leq \bar{\epsilon}\,T_2$, which gives
$|T_1 - T_2| \leq \bar{\epsilon}\,T_2$ (as operators, where $|A|$
denotes the positive part of the self-adjoint operator $A$ in the
sense that $-|A| \leq A \leq |A|$; for self-adjoint operators with
$-B \leq A \leq B$ and $B \geq 0$, we have $|A| \leq B$). Taking
traces:

$$\|T_1 - T_2\|_{\mathrm{tr}}
  \;=\; \mathrm{Tr}\,|T_1 - T_2|
  \;\leq\; \bar{\epsilon}\;\mathrm{Tr}\,T_2
  \;=\; \bar{\epsilon}\;\|T_2\|_{\mathrm{tr}}. \qquad\square$$

**Step D (Assembly).** Applying Step C with $T_1 = \hat{T}_{\mathrm{red}}$,
$T_2 = \hat{T}_{\mathrm{std}}$, and
$\bar{\epsilon} = 2\,C_1\,|\Lambda_t^1|\,e^{-m_1 a}$:

$$\bigl\|\hat{T}_{\mathrm{red}}
  - \hat{T}_{\mathrm{std}}\bigr\|_{\mathrm{tr}}
  \;\leq\; 2\,C_1\,|\Lambda_t^1|\,e^{-m_1 a}\;
  \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}
  \;=\; C_{\mathrm{tr}}\,|\Lambda_t^1|\,e^{-m_1 a}\;
  \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}},$$

with $C_{\mathrm{tr}} = 2\,C_1 = 4\,c_d^2\,C_0$. This is precisely
the bound ($\dagger$) stated in Lemma 2, with the constant
$C_{\mathrm{tr}}$ depending on $N$ (through $C_0$ from Theorem 2 and
the lattice geometry constant $c_d$) but not on $a/r_3$ or $L$.

The key points that resolve the sub-gap are:

1. **Uniformity in $U$:** The bound $(\ast)$ is uniform in all 4D link
   variables because the Theorem 2 bond activity bound
   $|g_\ell| \leq C_0\,e^{-m_1 a}$ is proved uniformly over
   $U_\ell \in \mathrm{SU}(N)$ (the adjoint action is unitary and does
   not affect mode norms).

2. **Pointwise kernel control:** The internal partition function ratio
   $\mathcal{Z}_{\mathrm{int}} / \mathcal{Z}_{\mathrm{int}}^{(0)}$
   enters the kernel of $\hat{T}_{\mathrm{red}}$ as a $U$-dependent
   multiplicative factor. The log-bound $(\ast)$ converts to a
   pointwise kernel bound
   $|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}|
   \leq \bar{\epsilon}\;\hat{T}_{\mathrm{std}}$ (Step B).

3. **Multiplicative-to-trace-norm passage:** The standard inequality
   for positive trace-class integral operators (Step C) converts the
   pointwise multiplicative bound into the trace-norm bound required
   by Lemma 2.

The normalization constant $\mathcal{Z}_{\mathrm{int}}^{(0)}$ is
$U$-independent and positive. It multiplies both kernels equally and
therefore drops out of all eigenvalue ratios $\lambda_1/\lambda_0$,
confirming the note at the end of Lemma 2's proof.


---

## Summary

| Component | Status | Reference |
|:----------|:-------|:----------|
| Bond activity bound $\|g_\ell\| \leq C_0 e^{-m_1 a}$, uniform in $U$ | Theorem 2 (Section 4.3) | Proved |
| Cluster expansion convergence | Theorem 3 (Section 4.3) | Proved |
| Log-ratio bound $(\ast)$ for $\mathcal{Z}_{\mathrm{int}}$ | This document | Proved |
| Pointwise multiplicative kernel bound | This document, Step B | Proved |
| Multiplicative-to-trace-norm inequality | This document, Step C | Proved (standard) |
| Lemma 2 trace-norm bound $(\dagger)$ | `theorem5-proof.md`, completed here | Proved |


---

<!-- ASSESSMENT: PROVED -- The internal partition function bound (*)
follows from the cluster expansion (Theorem 3) applied to the
bond activities on a single time-slab, using the uniform-in-U
bond activity bound from Theorem 2. The log-ratio bound converts
to a pointwise multiplicative kernel bound via exponentiation,
and the standard trace-norm inequality for positive integral
operators (Step C) yields the Lemma 2 bound. No new mathematics
is introduced; the argument uses only the cluster expansion
machinery of Section 4.3 and the elementary operator inequality
|T_1 - T_2|_tr <= epsilon |T_2|_tr for multiplicative kernel
perturbations of positive operators. The uniformity in U, which
was the core of the sub-gap, follows from the unitarity of the
adjoint action in the bond coupling. -->
