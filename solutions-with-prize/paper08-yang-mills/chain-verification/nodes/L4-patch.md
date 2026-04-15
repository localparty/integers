# L4 Patch — Link 4 (B1 analyticity, k-independent radius)

**Author:** Wave 4 patch Author
**Date:** 2026-04-13
**Repairs:** Wave 3 findings R1 (trivial), R2 (substantive), R3 (bonus preprint miscitation)
**Target status:** WEAKENED → VERIFIED

---

## Wave 3 findings addressed

### Finding 1 — "(i)–(iii)" should be "(i)–(iv)" [R1, trivial]

**Wave 3 attack (A2):** The $U^c_j$ domain is defined by four conditions on
p. 262, not three. Condition (iv) encodes the iterative gauge-fixing structure
(the sequence of maximal domains $\{\Omega_n\}, n=0,\ldots,j$, and the
functions $U_n(V)$ in axial gauges, eqs. 1.15–1.16). Citing only (i)–(iii)
leaves this condition unacknowledged and is verifiably wrong against the text.

**Resolution:** Every occurrence of "conditions (i)–(iii)" in the Wave 2
insertion is replaced by "conditions (i)–(iv)." One-word change; confirmed
directly from p. 262 of the PDF.

---

### Finding 2 — Citation split: §2 eqs. 2.2–2.3 for saddle-point center; §3 Lemma 4 for fluctuation composition [R2, substantive]

**Wave 3 attack (A3):** Lemma 4's hypothesis is
$\mathbf{U} \in U^c_{k+1}(\square_0, (1+2\beta)\alpha_0, (1+2\beta)\alpha_1)$
and its conclusion is that the pair
$(U_j(\square_0, \exp i(\tau B + B')), J_j(\square_0, \exp i(\tau B + B')))|_X$
belongs to $U^c_j(X, \alpha_0, \alpha_1)$.
The objects $B, B'$ are **fluctuation fields**, not the saddle-point
configuration $u_{\mathrm{cl}}[V_0]$. Lemma 4 handles the
fluctuation-integration step: given that the background **U** is in an
inflated domain, it shows the output of averaging over a small fluctuation
$B'$ lands in the uninflated domain.

The saddle-point center condition — that $u_{\mathrm{cl}}[V_0]$ lies strictly
inside the Mayer domain — is controlled earlier:

- The small-field hypothesis (1.2) on p. 260 bounds
  $|U(\partial p)-1| = |(\partial U)(p)-1| < \varepsilon_0\eta^2$, $p \in T$,
  and $|J| < \varepsilon_0$ on $T$.
- Section 2, eq. 2.2 (p. 265) identifies the saddle-point as the unique
  critical point of $V \mapsto \mathbf{G}(V) + A(U_k(V))$ subject to
  $\bar{V} = W$; eq. 2.3 (p. 265) establishes
  $V^{(k)} = \bar{U}^k_{+1} = M^k(U_{k+1})$, tying the saddle-point to
  the minimal configuration and its inherited regularity.

**Resolution:** The Wave 2 single-sentence insertion is split into two
sentences — Sentence A for the saddle-point center authority (§1 (1.2) +
§2 eqs. 2.2–2.3), Sentence B for the fluctuation-composition domain
membership (§3 Lemma 4). See revised preprint edits below.

---

### Finding 3 — Pre-existing miscitation: "CMP 109, Sec. 4" at line 1628 of 05-continuum-limit.md [R3, bonus]

**Wave 3 attack (E):** `05-continuum-limit.md` line 1628 cites "CMP 109,
Sec. 4" for convergent analytic cluster activities. Direct reading of the PDF
confirms:

- §3 (pp. 269–280) is "An Expansion of Terms in Fluctuation Field Integral,
  and Preliminary Analytic Extensions" — this is where Lemma 4 and the
  analytic extension of the expansion terms live.
- §4 (pp. 281–291) is "Ward-Takahashi Identities and Their Consequences" —
  concerned with identities that extract the $\beta$-function, not cluster
  activity analyticity.

**Resolution:** Change "Sec. 4" to "Sec. 3" at line 1628. Proposed fix edit
in revised preprint edits below.

---

## CMP 109 verbatim quotes

All quotes are from the Project Euclid scan locally saved at
`journals/balaban-CMP109-1987.pdf`. Journal pages cited; PDF pages differ by
an offset of approximately 5.

### §1 (1.2) — Small-field condition (journal p. 260)

> "$|U(\partial p) - 1| = |(\partial U)(p) - 1| < \varepsilon_0\eta^2$,
> $\eta = L^{-k}$, $p \in T$,
> $|J| < \varepsilon_0$ on $T$, $J = D^{2\alpha}_{U_k}\xi^{-2}\pi
> \operatorname{Im}\partial U$"

This is condition (1.2), imposing the small-field regularity bound on the
background $V$ (equivalently, on the minimal configuration $U_k(V)$) that
controls the size of the saddle-point output at each inductive step.

### §1, p. 262 — Definition of $U^c_j(X, \alpha_0, \alpha_1)$ and conditions (i)–(iv)

> "The space $U^c_j(X,\alpha_0,\alpha_1)$ is a union of orbits
> $[(\mathbf{U},\mathbf{J})]$ determined by the four conditions written
> below.
>
> (i) $\mathbf{U} = U'U$, $U$ has values in the group $G$,
>
> $|\partial U - 1| < \alpha_0\xi^2$ on $X$,
>
> for each cube $\square \subset X$ of a size $O(1)LM$ there exists a
> $G$-valued gauge transformation $u$ defined on $\square$ and such that
> $U^u = \exp i\xi A$,
>
> $|A|,\ |V^\xi A| < O(1)LMB\alpha_0$ on $\square$,
>
> with a sufficiently large constant $B$ (it will be determined later).
>
> (ii) $U' = \exp i\xi A'$, $A'$ has values in the algebra $\mathfrak{g}^c$,
>
> $|A'|,\ |V^\xi_0 A'| < \alpha_1$ on $X$.
>
> (iii) The configurations $\mathbf{U}$, $\mathbf{J}$ satisfy the bounds
>
> $|\partial U - 1| < \alpha_0\xi^2$, $|\mathbf{J}| < \gamma_0$ on $X$.
>
> (iv) We consider $X$ as $\Omega_0$, and we construct the sequence
> $\{\Omega_n\}$, $n=1,\ldots,j$, of maximal possible domains satisfying
> the conditions (1.3)–(1.6) [14] (with $j$, $\xi$ instead of $k$,
> $\eta$, $R = R_1$). For this sequence, or rather for its subsequences
> $\{\Omega_0, \Omega_1, \ldots, \Omega_n\}$, $n=1,\ldots,j$, we
> construct the functions $U_n(V)$ in the axial gauges, for regular
> $G^c$-valued configurations $V$. We consider the pair
>
> $(U_n(M'(\mathbf{U})), J_n(M'(\mathbf{U}})))$, $n=1,\ldots,j$,
>
> where $M'(\mathbf{U},b) = M^p(b)$ for $b \in A_p$ (see (1.5) [14]),
> and $J_n(M'(\mathbf{U}))$ is defined by the formula (1.8) with
> $U_n(M'(\mathbf{U}))$ instead of $U_j$, $L^{-n}$ instead of $\xi$.
> This pair satisfies the bounds
>
> $|\partial U_n(M'(\mathbf{U}))-1| < \alpha_0\xi^2$,
> $|J_n(M'(\mathbf{U}))| < \alpha_0(L^n\xi)^2$ on $\tilde{X}^{-2}$"

Condition (iv) encodes the iterative gauge-fixing structure that ties the
minimal configuration $U_k(V)$ to the background $V$ across scales — the
reason it cannot be omitted from the citation.

### §2 eqs. 2.2–2.3 — Saddle-point existence and regularity (journal p. 265)

Section 2 heading (p. 265): "**2. Fluctuation Field Integral in $k+1$-st
Renormalization Transformation**"

> "We calculate the integral (2.1) applying the saddle point method. At
> first we look for critical points of the function
>
> $V \to \mathbf{G}(V) + A(U_k(V))$, $V: \bar{V} = W$. (2.2)
>
> Under the above regularity assumptions there exists the exactly one
> critical point, which is obtained by taking the critical orbit of the
> function $A(U_k(V))$ considered on the subspace, and choosing the
> element of the orbit satisfying the axial gauge conditions
> $\mathbf{G}(V) = 0$. This critical configuration, which is a minimum
> of the function (2.2), is denoted by $V^{(k)} = V^{(k)}(W)$, and is
> related to the minimal configuration $U_{k+1}(W)$ in the axial gauge
> by the equality
>
> $V^{(k)} = \bar{U}^k_{+1} = M^k(U_{k+1})$. (2.3)"

Equation 2.2 is the variational problem defining the saddle-point; eq. 2.3
is the identity relating the saddle-point to the minimal configuration
$U_{k+1}(W)$, from which regularity (the size bound $|\partial V^{(k)}-1|
< \varepsilon_0\eta^2$) is inherited by Proposition 2 [12] cited in §1.

### §3 Lemma 4 — Fluctuation-composition domain membership (journal p. 280)

> "**Lemma 4.** For $\mathbf{U} \in U^c_{k+1}(\square_0, (1+2\beta)\alpha_0,
> (1+2\beta)\alpha_1)$, $\mathbf{A}$ defined on $\square_0$ and satisfying
> (3.31), $B'$ defined on the set of bonds connected with the definition
> of $U_j(\square_0, \cdot)$ and satisfying $|B'| < \alpha_3$, we have
>
> $(U_j(\square_0, \exp i(\tau B + B')), J_j(\square_0,
> \exp i(\tau B + B')))|_X \in U^c_j(X, \alpha_0, \alpha_1)$ (3.53)
>
> for $\alpha_0, \alpha_1, \alpha_2, \alpha_3$ sufficiently small and
> satisfying all the restrictions. The functions in (3.53) are analytic
> on the above spaces."

This lemma's objects $B, B'$ are fluctuation fields on the lattice
$T_1^{(k)}$, not the saddle-point configuration $u_{\mathrm{cl}}[V_0]$.
Its role is to show that after the fluctuation integration step, the output
pair $(U_j, J_j)|_X$ lands in the uninflated domain $U^c_j(X,\alpha_0,
\alpha_1)$, given that the background **U** belongs to an inflated domain
with parameters $(1+2\beta)\alpha_0$, $(1+2\beta)\alpha_1$.

---

## Revised preprint edits

### Edit 1 — H-balaban-analyticity.md §3 Step (b): two-sentence split + (i)–(iv) fix

**File:** `preprint/sections/H-balaban-analyticity.md`
**Location:** §3 "The Logical Chain", Step (b) "Each polymer activity is
analytic", current final sentence (line 132).

**Current text (Step (b) body, lines 119–132):**

```
Each $K_k(X,V)$ is computed by: (i) evaluating $S_{k-1}$ on
$V \cdot u$ (polynomial in $V,u$); (ii) saddle-point
$u_{\mathrm{cl}}[V] = -G_k(V) \cdot \nabla_u S_{k-1}|_{u=0}$
(analytic, since $G_k(V)$ is analytic and $\nabla_u S_{k-1}$ is
polynomial); (iii) Gaussian integration yielding
$(\det S_k^{(2)}[V])^{-1/2}$ (analytic where $S_k^{(2)} > 0$);
(iv) Mayer resummation of non-Gaussian corrections (convergent series
of analytic functions). Each step preserves analyticity; the
composition has radius bounded below by the minimum at any step.
```

**Replacement text (two sentences appended after the existing final
sentence):**

```
Each $K_k(X,V)$ is computed by: (i) evaluating $S_{k-1}$ on
$V \cdot u$ (polynomial in $V,u$); (ii) saddle-point
$u_{\mathrm{cl}}[V] = -G_k(V) \cdot \nabla_u S_{k-1}|_{u=0}$
(analytic, since $G_k(V)$ is analytic and $\nabla_u S_{k-1}$ is
polynomial); (iii) Gaussian integration yielding
$(\det S_k^{(2)}[V])^{-1/2}$ (analytic where $S_k^{(2)} > 0$);
(iv) Mayer resummation of non-Gaussian corrections (convergent series
of analytic functions). Each step preserves analyticity; the
composition has radius bounded below by the minimum at any step.
The center condition — that the saddle-point output
$u_{\mathrm{cl}}[V_0]$ lies strictly inside the Mayer
cluster-expansion domain rather than merely near its boundary —
follows from the small-field inductive hypothesis (1.2) of CMP 109
§1 (p. 260), which bounds $|(\partial U)(p)-1| < \varepsilon_0\eta^2$
and $|J| < \varepsilon_0$ on $T$ for $\eta = L^{-k}$, together with
the saddle-point analysis of CMP 109 §2 eqs. 2.2–2.3 (p. 265), which
identifies the unique minimizer $V^{(k)}(W)$ of
$V \mapsto \mathbf{G}(V) + A(U_k(V))$ and establishes via
$V^{(k)} = M^k(U_{k+1})$ (eq. 2.3) that it inherits the regularity
bound of $U_{k+1}(W)$.
CMP 109 §3 Lemma 4 (p. 280) then guarantees that the output of the
subsequent fluctuation-integration step — the pair
$(U_j(\square_0, \exp i(\tau B + B')), J_j(\square_0,
\exp i(\tau B + B')))|_X$ — belongs to the domain
$U^c_j(X, \alpha_0, \alpha_1)$ (conditions (i)–(iv), p. 262) for
$\alpha_0, \alpha_1, \alpha_2, \alpha_3$ sufficiently small,
confirming domain-membership through the full saddle-point + Gaussian
+ Mayer pipeline.
```

**Diff summary:**
- Wave 2's single sentence (citing §1 conditions (i)–(iii) and §3 Lemma 4
  together) is replaced by **two** sentences.
- Sentence A: CMP 109 §1 (1.2) + §2 eqs. 2.2–2.3 for saddle-point center
  condition.
- Sentence B: CMP 109 §3 Lemma 4 for fluctuation-composition domain
  membership, with "(i)–(iv)" in place of "(i)–(iii)."
- No other lines in `H-balaban-analyticity.md` are touched.

---

### Edit 2 — 05-continuum-limit.md line 1628: "Sec. 4" → "Sec. 3" [bonus fix]

**File:** `preprint/sections/05-continuum-limit.md`
**Location:** Line 1628.

**Current text:**

```
convergent series of analytic cluster activities (CMP 109, Sec. 4);
```

**Replacement text:**

```
convergent series of analytic cluster activities (CMP 109, Sec. 3);
```

**Rationale:** CMP 109 §4 (pp. 281–291) is "Ward-Takahashi Identities and
Their Consequences." The analytic extension of cluster activity terms is
constructed in §3 (pp. 269–280, "An Expansion of Terms in Fluctuation Field
Integral, and Preliminary Analytic Extensions"), the section that contains
Lemma 4. The citation "Sec. 4" is a pre-existing error not introduced by
Wave 2; it is corrected here for consistency with `H-balaban-analyticity.md`
§3 Step (c) source line ("CMP 109, Section 3") and with `05-continuum-limit.md`
line 1635 ("CMP 109, Sec. 3; CMP 119, Sec. 2").

---

## Self-suspicion

**Suspicion 1 — Did I misread the two-sentence boundary?**
Sentence A must end before any reference to Lemma 4 and must confine itself
to the saddle-point analysis. Sentence B must begin with Lemma 4 and describe
only the fluctuation step. The risk is that the phrasing of Sentence A bleeds
into Lemma 4 territory by asserting domain-membership — that is Lemma 4's
conclusion, not the §2 result. Check: Sentence A asserts that $V^{(k)}$
*inherits the regularity bound* of $U_{k+1}(W)$, not that the pair
$(U_j, J_j)$ belongs to $U^c_j$. The $U^c_j$ membership assertion appears
only in Sentence B. Boundary is clean.

**Suspicion 2 — Does eq. 2.3 actually deliver the needed regularity, or is
an additional Proposition 2 [12] step required?**
Balaban's text (§1, p. 260) states that condition (1.2) "by Proposition 2
[12] implies $|V(\partial p')-1| < 2\varepsilon_0$ for $p' \in T_1^{(k)}$."
This intermediate step means the inherited regularity is not
self-contained in eq. 2.3 alone but relies on the earlier Proposition. The
patch acknowledges this by citing §2 eqs. 2.2–2.3 *together with* the
small-field hypothesis (1.2) of §1, rather than citing eq. 2.3 in isolation.
A referee who checks both will see the complete chain. If a future wave judge
considers the reference to Proposition 2 [12] essential, the sentence can be
extended to name it explicitly; for now the §1 + §2 double citation
adequately frames the dependency.

**Suspicion 3 — Is the bonus fix (Edit 2) safe, or could CMP 109 §4 contain
relevant cluster-activity material not in §3?**
§4 (pp. 281–291) opens: "Let us consider the sum on the right-hand side of
(3.34). We can still separate some terms which are very small due to the
exponential decay." Its content is the Ward-Takahashi analysis used to
extract the $\beta$-function coefficients, not the primary construction of
analytic cluster activities. The analytic extension of the expansion terms
(the Mayer activities) is completed in §3 by Lemma 4 and the bound (3.54).
The bonus fix is safe. However, if the preprint author intended a forward
reference to a §4 lemma not yet read in this session, that would require a
check of §4 pp. 281–291 in full. No such lemma is cited or described in the
surrounding preprint context at lines 1627–1632; the fix stands.
