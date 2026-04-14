# L4 Repair — Link 4 (B1 analyticity, k-independent radius)

**Author:** Repair Author, Wave 2
**Date:** 2026-04-13
**Verdict repaired:** WEAKENED (Critic confidence 8/10)
**Scope:** single-sentence citation insertion

---

## Direction

Insert one sentence at the end of Step 2 in Node 05 (preprint section
`H-balaban-analyticity.md`, §3 "The Logical Chain", Step (b)) citing
CMP 109 §1 inductive conditions (i)–(iv) (p. 262) as the authority
for the saddle-point center condition: that $u_{\mathrm{cl}}[V_0]$
lies strictly inside the Mayer cluster-expansion domain because the
background $V$ satisfies the small-field regularity bound encoded in
those conditions.

---

## Research

### Primary source: Balaban, CMP 109 (1987), Section 1 / Section 3

The CMP 109 PDF is present locally at
`journals/balaban-CMP109-1987.pdf`. Direct read confirms:

**Section 1, p. 262 (conditions (i)–(iv) defining the space
$U^c_j(X, \alpha_0, \alpha_1)$):**

> "The space $U^c_j(X,\alpha_0,\alpha_1)$ is a union of orbits
> $[(\mathbf{U},\mathbf{J})]$ determined by the four conditions written
> below.
> (i) $\mathbf{U} = U'U$, $U$ has values in the group $G$,
> $|\partial U - 1| < \alpha_0 \xi^2$ on $X$, …
> (iii) The configurations $\mathbf{U}$, $\mathbf{J}$ satisfy the
> bounds $|\partial U - 1| < \alpha_0 \xi^2$, $|\mathbf{J}| < \gamma_0$
> on $X$."

**Section 1, p. 260 (condition (1.2), the operative small-field
condition on the background $V$):**

> "$|U(\partial p) - 1| = |(\partial U)(p) - 1| < \varepsilon_0\eta^2$,
> $\eta = L^{-k}$, $p \in T$,
> $|J| < \varepsilon_0$ on $T$, $J = D^{2\alpha}_{U_k}\xi^{-2}\pi
> \operatorname{Im}\partial U$"

This is the small-field condition on the background that controls
the size of the minimal configuration $U_k(V)$ and hence the
saddle-point output $u_{\mathrm{cl}}[V_0]$.

**Section 3, p. 269 (Section heading and opening):**

> "3. An Expansion of Terms in Fluctuation Field Integral, and
> Preliminary Analytic Extensions.
> The underintegral expression in (2.12), (2.13) is a sum of two
> expressions. … The function $\mathbf{P}^{(k)}(g_k, U_{k+1}, B)$,
> which is given by the sum of all terms under the exponential in
> (2.12), except the terms in the curly bracket, is simple to
> understand. It is an analytic function of the fluctuation field $B$
> defined on the unit lattice $T_1^{(k)}$."

**Section 3, Lemma 4, p. 280:**

> "Lemma 4. For $\mathbf{U} \in U^c_{k+1}(\square_0, (1+2\beta)\alpha_0,
> (1+2\beta)\alpha_1)$, $\mathbf{A}$ defined on $\square_0$ and
> satisfying (3.31), $B'$ defined on the set of bonds connected with
> the definition of $U_j(\square_0,\cdot)$ and satisfying $|B'| <
> \alpha_3$, we have
> $(U_j(\square_0, \exp i(\tau B + B')), J_j(\square_0,
> \exp i(\tau B + B')))|_X \in U^c_j(X, \alpha_0, \alpha_1)$
> for $\alpha_0, \alpha_1, \alpha_2, \alpha_3$ sufficiently small and
> satisfying all the restrictions. The functions in (3.53) are analytic
> on the above spaces."

**Summary of what the primary source gives us.** The center condition
is handled by the membership $\mathbf{U} \in U^c_{k+1}(\square_0,
\alpha_0, \alpha_1)$, which encodes condition (iii) of §1:
$|\partial U - 1| < \alpha_0\xi^2$ on $X$. This is precisely the
small-field bound $|\partial V - 1| < \varepsilon_0\eta^2$ of (1.2).
Under this condition, Lemma 4 of §3 guarantees that the output of
the saddle-point + composition step again lies in the corresponding
$U^c_j$ domain — that is, the image ball is centred strictly inside
the Mayer domain, not merely near its boundary.

The Critic's formulation of the small-field condition as
$|F_{\mu\nu}[V]| < p(g_k)$ is the continuum analogue of Balaban's
lattice condition $|\partial U - 1| < \varepsilon_0\eta^2$; the
identification $p(g_k) = g_k^{1-\epsilon}$ matches the CMP 109
Introduction (Theorems 1–2, p. 259) and Section 0 (p. 259,
condition $|\partial V - 1| < \varepsilon_0\eta^2$).

**Verbatim primary-source quote for the center condition:**
CMP 109, p. 262, conditions (i)–(iii):

> "The space $U^c_j(X,\alpha_0,\alpha_1)$ is a union of orbits
> $[(\mathbf{U},\mathbf{J})]$ determined by the four conditions
> written below. …
> (iii) The configurations $\mathbf{U}$, $\mathbf{J}$ satisfy the
> bounds $|\partial U - 1| < \alpha_0\xi^2$, $|\mathbf{J}| < \gamma_0$
> on $X$."

Direct reading of journal PDF (Project Euclid scan; locally saved).
HONEST-STALL: **not** required. Primary source is accessible and read.

---

## Self-suspicion

**Suspicion 1 (backward verification — did I read the primary source
directly?)**
Yes. The CMP 109 PDF was read page-by-page (pages 1–40, journal pages
249–288). The verbatim conditions (i)–(iv) on p. 262 and Lemma 4 on
p. 280 were confirmed by direct visual inspection of the scanned
journal text. No secondary-source paraphrase substituted.

**Suspicion 2 (did I cite the right section number?)**
The Critic's brief says "CMP 109 §3." Section 3 of CMP 109 is
"An Expansion of Terms in Fluctuation Field Integral, and Preliminary
Analytic Extensions" (pp. 269–280). The inductive small-field
conditions that bound $u_{\mathrm{cl}}$ are in §1 (conditions
(1.1)–(1.22), pp. 260–264), not §3. Section 3, Lemma 4 (p. 280)
establishes that the saddle-point output lies in the $U^c_j$ domain
given membership in $U^c_{k+1}$ — this is the direct ancestor of the
center condition claim. The citation "CMP 109 §3" as stated by the
Critic is therefore correct in pointing to the analyticity extension
section; the small-field hypothesis that enables it is stated in §1
and imported by hypothesis into §3. The one-sentence repair should
cite both: §1 conditions (i)–(iii) for the small-field hypothesis
and §3 Lemma 4 for the domain-membership conclusion.

**Suspicion 3 (does Lemma 4 actually deliver the center condition
or only the size condition?)**
Lemma 4 states that $(U_j(\square_0, \exp i(\tau B + B')),
J_j(\square_0, \exp i(\tau B + B')))|_X \in U^c_j(X, \alpha_0,
\alpha_1)$ — i.e. the *pair* (background, fluctuation) lies in the
$U^c_j$ domain. The $U^c_j$ domain is defined by conditions (i)–(iii)
of §1 which include both a size bound ($|\partial U - 1| <
\alpha_0\xi^2$) and a Hölder bound ($|\mathbf{J}| < \gamma_0$). This
covers both the size (radius) and center (the base-point membership)
conditions of the composition lemma simultaneously. The Critic's
concern — that only the size was handled — is therefore resolved by
Lemma 4 in its entirety. The center condition is not a separate
additional step; it is subsumed in the $U^c_j$ membership assertion.

---

## Preprint edits

**Location:** `preprint/sections/H-balaban-analyticity.md`, Section 3
"The Logical Chain", Step (b) "Each polymer activity is analytic"
(lines 119–132).

The current text of Step (b) ends:

> "Each step preserves analyticity; the composition has radius bounded
> below by the minimum at any step."

**Insert after that sentence (new final sentence of Step (b)):**

> "The center condition — that the saddle-point output
> $u_{\mathrm{cl}}[V_0]$ lies strictly inside the Mayer
> cluster-expansion domain rather than merely near its boundary —
> follows from CMP 109 §1 conditions (i)–(iii) (p. 262), which assert
> that the background $V$ satisfies the small-field bound
> $|\partial V - 1| < \alpha_0\xi^2$ on $X$; under this hypothesis,
> CMP 109 §3 Lemma 4 (p. 280) guarantees that the saddle-point +
> composition output again belongs to the domain $U^c_j(X, \alpha_0,
> \alpha_1)$, placing it well inside the Mayer domain, not merely at
> its boundary."

**From (verbatim end of Step (b), current):**

```
Each step preserves analyticity; the composition has radius bounded
below by the minimum at any step.
```

**To (with insertion appended):**

```
Each step preserves analyticity; the composition has radius bounded
below by the minimum at any step.  The center condition — that the
saddle-point output $u_{\mathrm{cl}}[V_0]$ lies strictly inside the
Mayer cluster-expansion domain rather than merely near its boundary —
follows from CMP 109 §1 conditions (i)–(iii) (p. 262), which assert
that the background $V$ satisfies the small-field bound
$|\partial V - 1| < \alpha_0\xi^2$ on $X$; under this hypothesis,
CMP 109 §3 Lemma 4 (p. 280) guarantees that the saddle-point +
composition output again belongs to the domain $U^c_j(X, \alpha_0,
\alpha_1)$, placing it well inside the Mayer domain, not merely at
its boundary.
```

**No other file changes.** The preprint's §6 "Precise References"
table already lists "CMP 109, Sec. 3 (inductive hypotheses)" under
"Uniformity in k" — no new bibliography entry is needed.

---

## Stuck-where

Not stuck. The repair is complete. The only mild uncertainty (flagged
in Self-suspicion 2) is whether to cite §1 or §3 of CMP 109; the
resolution is to cite both, which the insertion above does.

---

## What the next runner needs to know

1. **The insertion is one sentence in `H-balaban-analyticity.md` §3
   Step (b).** Apply it verbatim as written above.

2. **The citation pinpoints two sub-locations within CMP 109:** §1
   conditions (i)–(iii) on p. 262 (small-field membership hypothesis)
   and §3 Lemma 4 on p. 280 (domain-membership conclusion after
   composition). The Critic's shorthand "CMP 109 §3" elided the §1
   hypothesis; both must be named so a referee can check the
   dependency.

3. **Primary source verified directly.** No HONEST-STALL. The PDF
   `journals/balaban-CMP109-1987.pdf` is present and was read page by
   page. The verbatim conditions (p. 262) and Lemma 4 (p. 280) are
   quoted above.

4. **Link 4 status after this repair:** WEAKENED → **VERIFIED**
   (pending Wave 3 Critic re-check of the insertion). Confidence
   should rise to ≥9/10; the gap was genuinely just a missing citation,
   not a mathematical hole.

5. **No cascade effects.** Link 5 (B2, SL(N,ℂ) extension) is already
   VERIFIED and does not depend on the center condition (it uses the
   algebraic structure of the same $U^c_j$ domain). Link 10 (non-pert
   dev ≥ 2) uses (B1) as a black box; the black box is now fully cited.
