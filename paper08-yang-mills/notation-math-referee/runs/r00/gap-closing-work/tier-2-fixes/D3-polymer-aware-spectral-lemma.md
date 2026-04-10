# Tier 2 / Gap D3: Polymer-Aware Spectral Lemma

**Scope.** Structural reformulation of the §5.5.3 spectral lemma so
that it handles the object it is actually applied to: not a *single*
local operator of bounded support, but a *convergent sum* of polymer
activities with unbounded individual support and decay
$e^{-\kappa|X|}$.

**What this document is NOT.** It does not fix the quantitative
K-uniformity problem in physical units (the $\exp(C|X|^d N^2)$
lattice-unit blow-up of the per-polymer constant). That is Tier 1
Step 1.3 (Lieb–Robinson reformulation). This document *surfaces* the
obstruction cleanly but does not close it; Section 6 says so
explicitly.

---

## Section 1 — Statement of the gap

### 1.1 The problematic passage

The two-derivative spectral lemma (§5.5.3, Lemma) assumes
$\mathcal{O}$ is a gauge-invariant operator on $\Lambda_{k+1}$ with:

> (i) $\|\mathcal{O}\| \leq M$;
> (ii) **Locality:** $\mathcal{O}$ supported in $\mathcal{N}(0)$ of
> diameter $R_0$ lattice spacings;
> (iii) $\mathrm{dev}(\mathcal{O}) \geq p$.

Step 3 (Summing over channels) uses (ii) through a
Combes–Thomas / Nachtergaele–Sims locality estimate:

> by the Combes–Thomas estimate (Nachtergaele–Sims 2006, Theorem 2),
> for a local operator $\hat{A}$ supported in a region of diameter
> $R_0$ […]
> $$\zeta \leq \sum_{r=0}^{\infty} e^{C_1(R_0+r)^3 N^2}
>   \cdot e^{-c\hat{\Delta} r} < \infty$$

The "single local operator" hypothesis enters twice in Step 3:
(i) structurally, because "$\mathrm{supp}(n) \setminus \mathcal{R}$"
needs a single region $\mathcal{R}$; (ii) quantitatively, in the
bound $\#\{\text{states in } B(R_0+r)\} \leq \exp(C_1(R_0+r)^3 N^2)$,
where $R_0$ is a single number, not a polymer-indexed sequence. The
final constant $C_p = 2 C_*^p (1+\zeta)^{R_0-1}$ is honest only if
$R_0$ is one $k$-, $X$-independent number.

### 1.2 Why Balaban's polymer expansion violates this

The operator to which the lemma is applied in §5.5.3's application
paragraph is $\mathcal{O} = \delta E_k^{d=6}$. By §5.6 Part I
(equation (I.1)–(I.2)), this is
$$\delta E_k^{d=6}
  = \sum_{X \in \mathcal{P}_k} K_k^{(6)}(X, V),
  \qquad |K_k(X,V)| \leq e^{-\kappa|X|},$$
a sum over all connected polymers $X$ on $\Lambda_k$, with
$\kappa > 0$ $k$-independent and Kotecký–Preiss convergence
$\sum_{X\ni 0}|K_k(X,V)| \leq C_{\mathrm{KP}} < \infty$. Nothing in
this picture gives a bounded support radius: each $X$ has its own
size $|X|$, which can be arbitrarily large, with exponential
suppression in $|X|$ providing convergence. The support of
$\delta E_k^{d=6}$ is not contained in any ball — it is the whole
lattice, with exponential tails.

So hypothesis (ii) is *false* for $\mathcal{O} = \delta E_k^{d=6}$.
The Remark (Uniform temporal extent) at the end of §5.5.3 tries to
paper over this by asserting that Balaban's polymer expansion
"generates operators supported within connected polymers of diameter
bounded by $R_0$ block lattice units (CMP 109, Theorem 1)." This is
a misreading: CMP 109 Theorem 1 bounds the polymer *activities*
$|K_k(X,V)| \leq e^{-\kappa|X|}$, not the polymer *diameter* —
large polymers exist, they are merely exponentially suppressed.

The existing Step 3 applies honestly to an *individual* $K_k(X,V)$
with $R_0 = |X|$, but it does not directly apply to the convergent
sum, because no single $R_0$ works uniformly over $X$.

---

## Section 2 — The polymer-aware spectral lemma (statement)

**Lemma (Polymer-aware two-derivative spectral bound).** *Let
$\mathcal{O}$ be a gauge-invariant operator on $\Lambda_{k+1}$ of the
form*
$$\mathcal{O} = \sum_{X \in \mathcal{P}} K(X),$$
*where $\mathcal{P}$ is a set of connected polymers and each $K(X)$
is a gauge-invariant operator supported in $X$ (with $|X|$ the
lattice-unit size of $X$). Assume:*

*(i) $\|K(X)\| \leq M(X)$ for each $X$.*

*(ii) $\mathrm{dev}(K(X)) \geq p$ for each $X$.*

*(iii) **Weighted polymer convergence.** There exists a weight
$a \colon \mathcal{P} \to [0,\infty)$ with $a(X) \to \infty$ as
$|X| \to \infty$ such that*
$$\sum_{X \ni 0} M(X)\,e^{a(X)} < \infty,
  \qquad M_{\mathrm{tot}} := \sum_X M(X) < \infty.$$

*(iv) **Per-polymer spectral constant.** The original (single-support)
spectral lemma applies to each $K(X)$ with constant $C_p(|X|)$
depending on $|X|$, $p$, and $N$ but not on $k$, $g_k$, the volume,
or the location of $X$, and $C_p(|X|) \leq e^{a(X)}$.*

*Then there exists $C_p^{\mathrm{tot}}$, independent of the lattice
volume $L$ and the RG step $k$, such that*
$$\bigl|\langle 1|\mathcal{O}|1\rangle_c\bigr|
  \leq C_p^{\mathrm{tot}}\,M_{\mathrm{tot}}\,\hat{\Delta}^p.$$

**Remark 2.1 (Application to $\delta E_k^{d=6}$).** In §5.6 Part I,
one takes $K(X) = K_k^{(d=6)}(X,V)$, $M(X) = e^{-\kappa|X|}$, and
$p = 2$. The *live* question is whether a weight $a(X)$
compatible with both (iii) and (iv) exists — i.e., whether
$C_p(|X|)$ grows slowly enough to be dominated by $e^{\kappa|X|/2}$,
say. Section 3 shows that in lattice units the answer is **no**;
Section 4 flags this as the boundary with Tier 1 Step 1.3.

**Remark 2.2 (Role of the Linear Combination Lemma).** The §5.5.3
"Deviation order under linear combination" lemma — stating that if
$\mathcal{O} = \sum_i c_i \mathcal{O}_i$ with
$\sum_i |c_i|\|\mathcal{O}_i\| < \infty$ and each $\mathcal{O}_i$
has $\mathrm{dev} \geq p$, then so does $\mathcal{O}$ with norm
$\sum_i |c_i|\|\mathcal{O}_i\|$ — is the exact structural tool
needed. What it does not provide is a *per-term* $C_p(|X|)$
independent of $i$; its proof *calls* the single-operator spectral
lemma on each $\mathcal{O}_i$. Its Remark (Uniform temporal extent)
hides this by asserting the false $R_i \leq R_0$ uniformity. The
polymer-aware lemma replaces that false uniformity with an explicit
$|X|$-dependent $C_p(|X|)$ and pushes the burden onto hypothesis
(iv).

---

## Section 3 — Proof sketch and the growth obstruction

### 3.1 Per-polymer application

Fix $X \in \mathcal{P}$. Then $K(X)$ has $\|K(X)\| \leq M(X)$, is
*honestly* supported in a region of diameter $|X|$, and has
$\mathrm{dev}(K(X)) \geq p$. The **original** §5.5.3 spectral lemma
applies to $K(X)$ with $R_0$ set to $|X|$ and gives
$$\bigl|\langle 1|K(X)|1\rangle_c\bigr|
  \leq C_p(|X|)\,M(X)\,\hat{\Delta}^p,$$
with $C_p(|X|) = 2 C_*^p\,(1+\zeta(|X|))^{|X|-1}$ and
$\zeta(|X|) = \sum_{n \geq 1} e^{-(E_n-E_1)}$ the two-particle
threshold sum built from states supported in a ball of diameter
$|X|$.

### 3.2 Lattice-unit estimate for $C_p(|X|)$

Re-running Step 3(i) of §5.5.3 with $R_0$ replaced by $|X|$:
$$\zeta(|X|)
  \leq \sum_{r=0}^\infty e^{C_1(|X|+r)^3 N^2}\,e^{-c\hat{\Delta}\,r}
  \lesssim e^{C_1|X|^3 N^2},$$
where $(|X|+r)^3$ reflects the Hilbert-space dimension on a
*spatial* ball ($d-1 = 3$). Lifting through the $|X|-1$ internal
slots:
$$C_p(|X|)
  \lesssim (1+\zeta(|X|))^{|X|-1}
  \lesssim \exp\!\bigl(C_2\,|X|^d\,N^2\bigr), \qquad d=4.$$
So $C_p(|X|)$ is at most **exponential in $|X|^d$**, driven by the
local Hilbert-space dimension on a ball of $|X|$ lattice sites in
four spacetime dimensions.

### 3.3 The obstruction: $|X|^d$ beats $|X|$

Combining with the polymer decay $M(X) \leq e^{-\kappa|X|}$:
$$\sum_{X\ni 0} C_p(|X|)\,M(X)
  \lesssim \sum_{X \ni 0}
  \exp\!\bigl(C_2|X|^d N^2 - \kappa|X|\bigr).$$
Since $|X|^d \gg |X|$ for $|X|$ large, the exponential
$\exp(C_2 |X|^d N^2)$ beats $e^{-\kappa|X|}$ at some finite
$|X|_{\mathrm{crit}}$ and the sum **diverges**. Hypothesis (iv) of
the polymer-aware lemma therefore **fails** under the lattice-unit
estimate: no $a(X)$ compatible with $e^{a(X)} \geq C_p(|X|)
\approx \exp(C|X|^d N^2)$ will satisfy (iii) against the weight
$e^{-\kappa|X|}$.

### 3.4 Why this is a Tier 1 Step 1.3 problem

The blow-up comes from measuring the local Hilbert-space dimension
on $|X|$ **lattice sites**, not on a ball of fixed **physical**
radius. A polymer of lattice-unit size $|X|$ at RG step $k$ has
physical extent $r_{\mathrm{phys}} = |X|\cdot a_k$; the local
Hilbert-space dimension on a ball of physical radius $r$ is bounded
by $\exp(C r^d \Lambda^d N^2)$ for a physical UV cutoff $\Lambda$,
which does **not** grow with how finely the lattice is refined.

The lattice Lieb–Robinson bound (Nachtergaele–Sims, CMP 265
(2006)) delivers decay estimates on matrix elements whose rate is
bounded in physical units, so the effective per-polymer constant
$C_p(r_{\mathrm{phys}})$ becomes at worst polynomial in
$r_{\mathrm{phys}}$, not exponential in $|X|^d$. Plugging that into
§3.3, the sum reduces to
$\sum_X \mathrm{poly}(|X|)\,e^{-\kappa|X|}$, which converges by
Kotecký–Preiss times a polynomial factor. But establishing this is
the Tier 1 Step 1.3 task; the present Tier 2 task only **surfaces**
the obstruction inside a polymer-aware framework where
$C_p(|X|)$ is an explicit object.

---

## Section 4 — Two distinct fixes

The "single operator vs. polymer sum" confusion in §5.5.3 hides
**two** different defects. Both must be repaired.

### Fix 1 — Polymer-aware structural reformulation (this task)

**Defect.** Hypothesis (ii) of §5.5.3 is false for
$\mathcal{O} = \delta E_k^{d=6}$, and the Remark (Uniform temporal
extent) misreads CMP 109 Theorem 1.

**Form of the fix.** Replace the single-operator lemma by the
polymer-aware lemma of Section 2. Apply the per-polymer bound to
each $K(X)$ and invoke the Linear Combination Lemma (already in
§5.5.3, immediately after the main lemma) to combine them. The
per-polymer constant $C_p(|X|)$ becomes *visible*.

**Scope.** Structural only. Does not bound $C_p(|X|)$ at the rate
needed for convergence.

**Deliverable.** This document plus a draft replacement of Step 3
(Section 5).

### Fix 2 — K-uniform reformulation in physical units (Tier 1 Step 1.3)

**Defect.** Even after Fix 1, the lattice-unit estimate
$C_p(|X|) \lesssim \exp(C|X|^d N^2)$ diverges against
$e^{-\kappa|X|}$.

**Form of the fix.** Re-derive the per-polymer spectral lemma in
*physical* units, replacing lattice Combes–Thomas by a Lieb–Robinson
bound à la Nachtergaele–Sims 2006 Theorem 2. In physical units the
local Hilbert-space dimension on a ball of physical radius $r$ is
$\exp(C r^d \Lambda^d N^2)$ K-uniformly, so $C_p(|X|)$ is at most
polynomial in $r_{\mathrm{phys}}$ and the polymer sum converges.

**Scope.** Quantitative. Requires a nontrivial extension of
Nachtergaele–Sims (which covers bosonic lattice systems) to 4D
SU(N) lattice gauge theory — itself an open problem; see the
gap-closing strategy document's Phase 2.

**Deliverable.** A new version of §5.5.3 Step 3 with $R_0$ as a
physical radius, and a K-uniform Lieb–Robinson bound for 4D SU(N).
Estimated there at 4–6 months.

### 4.1 Why both are needed

Either alone is insufficient. **Fix 1 alone** gives the right
*form* of the lemma with $C_p(|X|)$ explicit, but the constant
still diverges and the lemma is vacuous. **Fix 2 alone** gives the
right *bounds* on a single polymer but cannot be plugged into
§5.5.3 as written, because §5.5.3 applies the lemma to a single
operator with pretend bounded support. Fix 1 is the skeleton; Fix 2
fills in the numbers.

---

## Section 5 — Draft replacement of §5.5.3 Step 3

Text in $[\,\cdots\,]$ flags dependencies on Tier 1 Step 1.3.

---

**Step 3 (Summing over channels, polymer-aware version).** The
operator $\mathcal{O}$ to which we apply the lemma in the
application paragraph below is
$\mathcal{O} = \sum_{X \in \mathcal{P}} K(X)$, where each $K(X)$ is
gauge-invariant and supported in the polymer $X$ of lattice-unit
size $|X|$. We work per polymer and then sum.

**(a) Per polymer.** Fix $X$. Then $K(X)$ has $\|K(X)\| \leq M(X)$,
is supported in a region of diameter $|X|$ (so hypothesis (ii) of
the single-operator spectral lemma holds with $R_0$ replaced by
$|X|$), and $\mathrm{dev}(K(X)) \geq p$. The single-operator
spectral lemma yields
$$\bigl|\langle 1|K(X)|1\rangle_c\bigr|
  \leq C_p(|X|)\,M(X)\,\hat{\Delta}^p,$$
with $C_p(|X|) = 2 C_*^p (1+\zeta(|X|))^{|X|-1}$ and $\zeta(|X|)$
the two-particle threshold sum built from excitations supported in
a ball of diameter $|X|$ [physical diameter $|X|\cdot a_k$].

[**Depends on Tier 1 Step 1.3 for the K-uniform / polynomial-in-$|X|$
bound.** In lattice units,
$C_p(|X|) \lesssim \exp(C_2 |X|^d N^2)$. Tier 1 Step 1.3's
physical-unit Lieb–Robinson reformulation replaces this by
$C_p(|X|) \leq C_p\,(|X|)^q$ with $q$ $k$-independent, so that the
polymer sum below converges.]

**(b) Sum over polymers.** By the Linear Combination Lemma
(§5.5.3, immediately after the main lemma), the convergent sum
$\mathcal{O} = \sum_X K(X)$ inherits deviation order $p$ and
satisfies
$$\bigl|\langle 1|\mathcal{O}|1\rangle_c\bigr|
  \leq \sum_X \bigl|\langle 1|K(X)|1\rangle_c\bigr|
  \leq \Bigl(\sum_X C_p(|X|)\,M(X)\Bigr)\,\hat{\Delta}^p.$$

**(c) Convergence of the per-polymer weighted sum.** The polymer
expansion (§5.6 Part I, (I.2)) provides
$M(X) \leq e^{-\kappa|X|}$ with $\kappa > 0$ $k$-independent, and
Kotecký–Preiss gives $\sum_{X\ni 0} e^{-\kappa|X|} \leq
C_{\mathrm{KP}}$. The relevant sum is
$$\sum_{X\ni 0} C_p(|X|)\,e^{-\kappa|X|}.$$

[**Depends on Tier 1 Step 1.3.** Under the lattice-unit estimate,
this sum **diverges** because $\exp(C_2|X|^d N^2)$ dominates
$e^{-\kappa|X|}$. Under the Lieb–Robinson estimate of Tier 1
Step 1.3, it reduces to
$\sum_X \mathrm{poly}(|X|)\,e^{-\kappa|X|} < \infty$. The present
§5.5.3 Step 3 is valid only under that hypothesis.]

**(d) Conclusion.** With the Tier 1 Step 1.3 bound in place,
translation invariance and (c) give a $k$- and volume-independent
constant $C_p^{\mathrm{tot}}$ with
$$\bigl|\langle 1|\mathcal{O}|1\rangle_c\bigr|
  \leq C_p^{\mathrm{tot}}\,M_{\mathrm{tot}}\,\hat{\Delta}^p,
  \qquad M_{\mathrm{tot}} = \sum_X M(X) \leq C_{\mathrm{KP}}.$$
Steps 4 (connected matrix element) and the subsequent application
to $\delta E_k^{d=6}$ proceed unchanged, with $M$ replaced by
$M_{\mathrm{tot}}$.

---

**Note on the Remark (Uniform temporal extent).** The existing
Remark should be deleted or rewritten. Its claim that Balaban's
polymer expansion "generates operators supported within connected
polymers of diameter bounded by $R_0$ block lattice units" is a
misreading of CMP 109 Theorem 1, which bounds the polymer
*activities* by $e^{-\kappa|X|}$, not their *diameter*. The
polymer-aware Step 3 above is the correct replacement.

---

## Section 6 — Open issue

**Honest statement.** The polymer-aware spectral lemma of Section 2
and the draft Step 3 of Section 5 provide the correct *structural*
form of the lemma for the object it is actually applied to
($\delta E_k^{d=6}$ as a polymer sum). They fix the "single
operator of bounded support" misstatement and make the Linear
Combination Lemma do its intended job.

**They do not establish convergence of the polymer sum.** In
lattice units, $C_p(|X|) \lesssim \exp(C|X|^d N^2)$, which beats
the polymer decay $e^{-\kappa|X|}$ for $|X|$ large. The structural
reformulation makes this divergence **visible** but does not cure
it.

The cure is Tier 1 Step 1.3: re-derive the per-polymer spectral
constant in physical units via a Lieb–Robinson bound for 4D SU(N)
lattice gauge theory, so that $C_p(|X|)$ is at worst polynomial in
$|X|$ (equivalently, exponential in $|X|\cdot a_k$ with a
K-uniform rate). Under that bound, the polymer-aware lemma becomes
non-vacuous.

**If Tier 1 Step 1.3 fails** — e.g., because a K-uniform
Lieb–Robinson bound for 4D SU(N) cannot be established — then the
polymer-aware spectral lemma still has the Section 3 divergence
problem, and the preprint's strategy for bounding
$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|$ must be restructured.
The gap-closing strategy document's "Mitigation" paragraph
(Aizenman–Holroyd / Kennedy–King decay-of-correlations for spin
systems) is the natural fallback.

**Status of the Tier 2 D3 deliverable.** The structural
reformulation is done. The per-polymer bound on $C_p(|X|)$ is
**flagged, not proved**. The draft Step 3 in Section 5 localizes
the dependence on Tier 1 Step 1.3 to a single bracketed line per
sub-step.

---

## Summary

This document rewrites the §5.5.3 spectral lemma so that it handles
a convergent sum of polymer activities with unbounded individual
support. The per-polymer application plus the existing Linear
Combination Lemma gives the correct structural form. The
per-polymer constant $C_p(|X|)$ is made explicit, and its growth
rate $\exp(C|X|^d N^2)$ in lattice units is identified as the
obstruction that Tier 1 Step 1.3 (Lieb–Robinson in physical units)
must remove for the overall bound to be nontrivial.
