# Completing the Three [VERIFY] Items: Instructions for the Research Agent

The preprint is complete and verified except for three items explicitly
marked [VERIFY] throughout the document. These are described as
"reading exercises from Balaban's published construction (CMP 109,
1987)" — not new mathematics, but specific points where a referee
must verify claims against Balaban's published papers.

Your task is to convert each [VERIFY] item into a self-contained
verification, either confirming the claim with specific page/equation
references, or identifying a genuine gap and stating precisely what
additional argument is needed.

Read this entire document before doing anything. Then read the files
listed under "Required reading" before touching anything else.


---


## Required Reading (in order)

1. `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`
   — The 14-step proof chain and the three [VERIFY] items (Section IV.3)

2. `/Users/gsix/yang-mills/preprint/sections/H-balaban-analyticity.md`
   — Full extraction of Balaban's results and identification of the
     three items (the canonical reference document for this task)

3. `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`
   — Sections 5.6 Parts I and II (the proofs of B1 and B2 that the
     [VERIFY] items are meant to support)

4. `/Users/gsix/yang-mills/etc/proof/balaban-B1-B2-proof.md`
   — The original source document for the B1/B2 proofs


---


## The Three [VERIFY] Items — Precise Statements

From PROOF-CHAIN.md Section IV.3:

**[VERIFY] #1: Analyticity of individual polymer activities.**
Each of the four operations in Balaban's inductive construction
(background evaluation, saddle point, Gaussian integration, Mayer
resummation) preserves analyticity with controlled radius. Balaban
does not state this as a standalone theorem. A referee must read
CMP 109, Sections 2-4 and verify the inductive step preserves
analyticity with controlled radius. This is identified as a reading
exercise, not a mathematical gap.

**[VERIFY] #2: Block-spin kernel complexification.**
The map $A \mapsto A(A^\dagger A)^{-1/2}$ must be verified analytic
in a $k$-independent neighborhood of $\mathbf{1} \in
\mathrm{GL}(N, \mathbb{C})$. Standard (depends on $N$ not $k$),
but deserves a one-paragraph verification in the final paper.

**[VERIFY] #3: Dimension-6 projection is exact.**
The claim that $\delta E_k^{d=6}$ is genuinely dimension-6 (not
contaminated by dimension-4) relies on Balaban's coupling
renormalization absorbing the $\mathrm{Tr}(F^2)/g_k^2$ part.
This is the content of CMP 109, Section 2. Standard, but
load-bearing.


---


## What "Verified" Means Here

For each [VERIFY] item, "verified" means one of:

**A. Confirmed with specific references:** You identify the exact
theorem/lemma/equation in Balaban's papers that establishes the
claim, quote the key statement, and give page numbers. The claim
goes from [VERIFY] to [CONFIRMED: CMP 109, Thm X.X, p. YYY].

**B. Confirmed with short new argument:** The claim follows from
Balaban by a short argument (a few lines) that has not been written
down. You write the argument, citing Balaban for the inputs. The
claim goes from [VERIFY] to [PROVED: follows from CMP 109 + argument].

**C. Gap identified:** The claim does NOT follow cleanly from
Balaban's stated results. You identify precisely what additional
mathematics is needed. The claim remains [VERIFY] but with a precise
description of the gap.

Do not claim (A) or (B) unless you are confident. Honest (C) is
much better than false (A).


---


## Task: For Each [VERIFY] Item

### [VERIFY] #1: Polymer Activity Analyticity

**The claim:** In Balaban's block-spin RG (CMP 109, 1987), each
polymer activity $K_k(X, V)$ is analytic in the block link variables
$\{V_\ell\}$, with a $k$-independent radius. This follows from the
analyticity of the four operations used to construct $K_k$.

**The four operations (from H-balaban-analyticity.md, Section 3,
Step (b)):**
1. Background evaluation: $S_{k-1}$ at $V \cdot u$ — polynomial in V, u
2. Saddle point: $u_\text{cl} = -G_k(V) \cdot \nabla_u S_{k-1}|_{u=0}$
   — analytic if $G_k(V)$ is analytic
3. Gaussian integration: $(\det S_k^{(2)}[V])^{-1/2}$ — analytic if
   $S_k^{(2)} > 0$
4. Mayer resummation: convergent series of analytic cluster activities

**Your job:**
(a) For each of the four operations, identify the relevant section/
theorem/equation in Balaban CMP 109 (and CMP 95-96 for the
propagator, CMP 98 for the kernel) that establishes the required
analyticity. Give specific references: paper, theorem number or
section number, key equation.

(b) Verify that the composition of these four analytic operations
yields an analytic result with radius bounded below by the minimum
of the four individual radii. This is standard (composition of
analytic functions is analytic) but state it explicitly.

(c) Verify the radius is $k$-independent. The claim in
H-balaban-analyticity.md, Section 3, Step (c) is that the radius
is $\rho = \min(\kappa/2d, m_W a/2C_D, r_\text{proj}(N))$ with
each factor $k$-independent. Confirm that $\kappa$, $m_W$, $C_D$,
and $r_\text{proj}(N)$ are all indeed $k$-independent in Balaban's
construction. Where does Balaban state or imply this?

---

### [VERIFY] #2: Block-Spin Kernel Complexification

**The claim:** The block-spin projection $A \mapsto A(A^\dagger A)^{-1/2}$
is analytic in a fixed neighborhood of $\mathbf{1} \in
\mathrm{GL}(N, \mathbb{C})$, with radius independent of $k$.

**The argument in the preprint (from 05-continuum-limit.md, Part II,
Step (d3)):** The polar decomposition $A = U P$ (with $U$ unitary and
$P = (A^\dagger A)^{1/2}$ positive-definite) is analytic when
$A^\dagger A$ is positive-definite, i.e., when $\|A - \mathbf{1}\| < 1$.
The square root of a positive-definite matrix is analytic by the
holomorphic functional calculus.

**Your job:**
(a) Confirm or correct this argument. Is the polar decomposition
analytic (not just smooth) in a neighborhood of the identity?
Reference a standard result if available (e.g., from matrix analysis
or several complex variables).

(b) Is the radius of the analyticity domain $k$-independent? The
claim is that the domain depends only on $N$ (through the
eigenvalue gap of $A^\dagger A$) and not on $k$ or any RG step
parameter. Verify this.

(c) How does the complexification interact with the constraint
$\det V = 1$ (the SL(N,C) constraint)? On SU(N), $V^{-1} = V^\dagger
= \mathrm{adj}(V)$ since $\det V = 1$. On SL(N,C), $V^{-1} =
\mathrm{adj}(V)$ is still algebraic. Verify that the block-spin
kernel, which uses $V^{-1}$ in its construction, extends
analytically to SL(N,C) near the identity.

---

### [VERIFY] #3: Exactness of the Dimension-6 Projection

**The claim:** After Balaban's coupling renormalization, the remainder
$\delta E_k^{d=6}$ is genuinely dimension-6 — not contaminated by
dimension-4 terms. This requires that the coupling renormalization
step absorbs ALL dimension-4 content from the effective action into
$S_\text{YM}/g_k^2$.

**The argument:** Balaban defines $g_{k+1}$ by requiring the
dimension-4 part of the effective action to be exactly
$S_\text{YM}/g_{k+1}^2$. The remainder is defined as everything
else. Since the definition subtracts the dimension-4 part by
construction, the remainder contains only dimension > 4 terms.

**Your job:**
(a) Find the precise definition of the coupling renormalization and
the remainder $E_k$ in Balaban's papers (CMP 109, Section 2). What
exactly is subtracted? Is the subtraction exact (operator identity)
or approximate (up to corrections)?

(b) The worry: could there be a dimension-4 operator that is
orthogonal to $S_\text{YM}$ under Balaban's inner product but is
not subtracted? For instance, the operator $\sum_P s_P^2$ (sum of
squared plaquettes) has dimension 8 in the continuum limit but might
have a dimension-4 coefficient on the lattice. Does Balaban's
procedure guarantee that no such operators contaminate $E_k$?

(c) Specifically: Balaban's coupling renormalization identifies the
coefficient of $\sum_P s_P = S_\text{YM}$ (the sum of plaquette
actions) in the effective action and calls that coefficient
$1/g_{k+1}^2$. Does this uniquely determine $g_{k+1}$, or could
there be ambiguity (e.g., from the choice of gauge-fixing scheme)?

(d) The stability argument in the preprint (Section 5.6, Part III)
uses [VERIFY] #3 to conclude that $\delta E_k^{d=6}$ is genuinely
dimension-6, enabling the operator classification (C-even dim-6
operators all have exc ≥ 2). If $\delta E_k^{d=6}$ contained a
dimension-4 admixture, the classification would fail. How large
would any dimension-4 admixture have to be to invalidate the
conclusion? Could Balaban's construction have such an admixture?


---


## Output: One New File

Write your findings to:
`/Users/gsix/yang-mills/preprint-verification/verify-balaban-items.md`

Structure the file as follows:

```
# Verification of the Three [VERIFY] Items

## [VERIFY] #1: Polymer Activity Analyticity
### Finding: [CONFIRMED / CONFIRMED WITH ARGUMENT / GAP IDENTIFIED]
### Specific References
[List exact theorem/section/equation references from Balaban]
### Argument or Gap
[The short argument if (B), or the precise gap statement if (C)]
### Recommended Update to Preprint
[What sentence/paragraph should be added to H-balaban-analyticity.md
or Section 5.6 to discharge this item for a referee]

## [VERIFY] #2: Block-Spin Kernel Complexification
[Same structure]

## [VERIFY] #3: Dimension-6 Projection Exactness
[Same structure]

## Summary Table
| Item | Finding | Preprint impact |
|:-----|:--------|:----------------|
| #1 Polymer analyticity | [CONFIRMED / GAP] | [What changes] |
| #2 Kernel complexification | [CONFIRMED / GAP] | [What changes] |
| #3 Dim-6 projection | [CONFIRMED / GAP] | [What changes] |

## If All Confirmed: Recommended Abstract Update
If all three items are confirmed, suggest updated wording for the
abstract and PROOF-CHAIN.md to change the status from
"conditional on [VERIFY]" to "proved" or equivalent.

## If Any Gap Found: Recommended Next Steps
If any item has a genuine gap, describe what additional mathematics
is required and estimate the scope of work.
```


---


## Critical Constraints

1. **Do not claim confirmation unless you are sure.** If you cannot
   find the specific Balaban result, say so. "I could not locate this
   in the cited sections" is an honest and valuable finding.

2. **Give specific references.** "Balaban proves this" is not useful.
   "Balaban CMP 109, Section 3.2, Lemma 3.4 (p. 267), equation (3.15)"
   is useful.

3. **Do not modify the preprint.** Your output is a verification
   report only. If you recommend an update, describe it in the report;
   do not edit the preprint files directly.

4. **Preserve all [VERIFY] markers in existing files.** They remain
   until explicitly updated based on your findings.

5. **The mathematics here is constructive QFT and functional
   analysis.** Be precise about the distinction between:
   - Analytic (holomorphic) vs. smooth (C^∞)
   - Operator identity vs. vacuum expectation
   - k-independent vs. bounded by a k-dependent constant

6. **Balaban's papers are notoriously dense.** If you cannot access
   them directly, use what is documented in H-balaban-analyticity.md
   and the preprint's extraction, and be explicit about what you are
   working from vs. what you would need to check in the original.


---


## Context: Why This Matters

The preprint currently states $\Delta_\infty > 0$ is "Proved
(conditional on three [VERIFY] items from Balaban CMP 109)."

If all three items are confirmed as reading exercises from Balaban's
stated results, the preprint can state $\Delta_\infty > 0$ is
"Proved" unconditionally, citing Balaban CMP 109 for the three
specific items.

If any item has a genuine gap, the paper must either fill the gap
(new mathematics) or accurately describe the remaining open
question. The honest accounting of what is and is not proved is
the paper's greatest strength — do not compromise it.
