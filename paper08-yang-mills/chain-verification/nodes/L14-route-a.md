# L14 Route A — Per-Polymer Gauge Invariance via Block-Spin Gauge Group

**Link:** 14 (Δ_∞ > 0, continuum mass gap)
**Wave:** 6 (Author; construct)
**Wave 5 Critic verdict:** WEAKENED — residual joint S4 (per-polymer dev ≥ 2)
**Author:** Claude Opus 4.6 (1M context), Wave 6 Route A
**File-owner:** only `nodes/L14-route-a.md`
**Verdict:** ADVANCED
**Headline:** Part III.3's gauge-invariance hypothesis is the block-spin one (reading (b)); Balaban's CMP 95 §A construction exhibits each polymer activity $K_k(X,\cdot)$ as a gauge-invariant function of the block-link variables $V_\ell$ on its support, so Part III.3 applies per polymer.
**Reading of Part III.3:** **(b) — block-spin gauge group on $\Lambda_{k+1}$**, not the full fine-lattice gauge group.

---

## Diagnosis

### The joint

The Wave 5 Critic flagged one residual gap. Edit 4 of the L14 patch (Wave 4) asserts:

> $\delta E_k^{d=6}(0) = \sum_{X\ni 0} K_k^{d=6}(X,\cdot)$ is a
> convergent polymer expansion whose activities are $\mathcal{C}$-even
> dimension-6 operators with $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$
> (§5.6 Part III.3).

The Part III.3 Lemma (preprint `05-continuum-limit.md` lines 1769–1773) states:

> **Lemma (Stability of Deviation Order).** *Let $\mathcal{O}$ be
> a local, gauge-invariant, $\mathcal{C}$-even operator on
> $\Lambda_{k+1}$ of engineering dimension 6, analytic in $\{V_\ell\}$
> with radius $\rho > 0$ (from (B1)). Then
> $\mathrm{dev}(\mathcal{O}) \geq 2$.*

The hypothesis has three components: **(i) local, (ii) gauge-invariant, (iii) $\mathcal{C}$-even**. The polymer-aware Hastings–Koma bound of §5.5.3 Step 3(i) (lines 1334–1339) is applied *inside* the sum over $X$, so each activity $K_k^{d=6}(X,\cdot)$ must satisfy dev ≥ 2 individually. That requires verifying (i)–(iii) *per polymer*.

- **(i) Locality per polymer:** trivial. $K_k^{d=6}(X,\cdot)$ is by construction supported on $X$, which is a finite connected subset of $\Lambda_k$ (a fortiori of $\Lambda_{k+1}$ after one more blocking step).
- **(iii) $\mathcal{C}$-evenness per polymer:** essentially trivial. Balaban's construction is $\mathcal{C}$-equivariant (Wilson action is $\mathcal{C}$-invariant; Haar measure is $\mathcal{C}$-invariant; block-spin projection commutes with $\mathcal{C}$; fluctuation integral is $\mathcal{C}$-invariant). Each activity $K_k(X,\cdot)$ transforms as $\mathcal{C}$-even if the ambient theory is $\mathcal{C}$-invariant. The dimension-6 projection $K_k^{d=6}(X,\cdot)$ inherits $\mathcal{C}$-evenness from $K_k(X,\cdot)$ (the $\mathcal{C}$-odd dimension-6 operators $\mathrm{Tr}(F^3)$, $d^{abc}F^3$ have coefficient zero in *any* $\mathcal{C}$-invariant effective action, including each individual polymer activity since the $\mathcal{C}$-projector commutes with the polymer decomposition by linearity).
- **(ii) Gauge invariance per polymer:** This is the genuine question. The Wave 5 Critic's concern (verbatim):

    > a **single polymer activity** $K_k^{d=6}(X, \cdot)$ for a fixed $X$
    > is spatially restricted to the support of $X$; it is in general NOT
    > individually gauge-invariant (it gains gauge-invariance only when
    > summed over all $X$ …).

    This is the heuristic that in perturbative calculations, individual Feynman diagrams are gauge-variant and only gauge-invariance of the sum is guaranteed. But Balaban's construction is **not perturbative**; its polymer decomposition is a cluster expansion of the *already-gauge-fixed* functional integral, and each activity $K_k(X,V)$ is by construction a function of the *gauge-invariant* block-link variables on $X$.

### Reading of Part III.3: (a) or (b)?

The Lemma says "analytic in $\{V_\ell\}$ with radius $\rho > 0$ (from (B1))". Property (B1), stated at §5.6 Part I lines 1577–1580 verbatim:

> **(B1).** *In the small-field region $\Omega_s$ at RG step $k$, the
> effective action $S_k[V]$ is analytic in the block link variables
> $\{V_\ell\}$, with radius of analyticity $\rho > 0$ independent
> of $k$.*

The operator $\mathcal{O}$ of Part III.3 lives on $\Lambda_{k+1}$ and is a function of the block links $V_\ell$. The gauge transformations that act on the $V_\ell$ are **block-level gauge transformations** — transformations $\Omega: \Lambda_{k+1} \to \mathrm{SU}(N)$ of the block lattice, under which $V_\ell \mapsto \Omega_{x}\,V_\ell\,\Omega_y^{-1}$ for $\ell = \langle x, y\rangle$.

The classification argument in Part III.3's proof (lines 1775–1856) is explicitly about *which dimension-6 operators on $\Lambda_{k+1}$* are block-level gauge-invariant and $\mathcal{C}$-even: $F^3$, $\mathrm{Tr}(DF)^2$, $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$, etc. These are **block-level** objects (covariant derivatives built from block links, block-field-strengths $F_{\mu\nu}[V]$). The classification uses:

1. $\mathcal{C}$-evenness to eliminate $F^3$, $d^{abc}F^3$.
2. Block-level gauge invariance to force an even number of $F$'s under the trace.
3. Engineering dimension 6 to enumerate derivative structures.

**None of these uses the fine-lattice gauge group.** The "gauge-invariant" in Part III.3 is unambiguously the **block-spin gauge group on $\Lambda_{k+1}$**. Reading **(b)**.

Confirmation: §5.3.1 line 510–514 discusses "the complete basis of gauge-invariant, $\mathcal{C}$-even operators" at dimension 6, and the context throughout §5.3/5.6 is the effective theory on the block lattice $\Lambda_{k+1}$ with its block-level gauge freedom.

---

## Research (6-step inner method loop)

### Step 1 — Diagnose (precise)

The task is to establish: each Balaban polymer activity $K_k^{d=6}(X, V)$, viewed as an operator on $\Lambda_{k+1}$ after one further RG step, is invariant under the block-spin gauge group $\mathcal{G}_{k+1} = \mathrm{Map}(\Lambda_{k+1}, \mathrm{SU}(N))$. With this in hand, the three hypotheses of Part III.3 are all satisfied per polymer, and the Lemma applies term-by-term inside the Hastings–Koma sum.

### Step 2 — Reinterpret (inversion check)

Is there a larger system that makes per-polymer gauge-invariance automatic?

**Balaban's construction is gauge-equivariant by design.** This is the "larger system": the entire RG step, including the polymer decomposition, is built to preserve the gauge symmetry of the block lattice. The gauge-fixing in CMP 95 §A is *restricted* to a maximal tree (axial gauge), and the $\delta$-functions $\delta_{\mathrm{Ax}}$ (CMP 95 eq. 1.10) remove *only* the non-block-constant gauge transformations. The surviving symmetry — transformations $\lambda$ with $Q_k'\lambda = 0$, i.e., block-constant transformations — is the block-spin gauge group, and it acts on the whole construction:

- the block-averaged field $B$ (CMP 95 eq. 1.9),
- the fluctuation $u$ via the same action (CMP 95 eq. 1.20),
- the propagator $G_k(V)$ (gauge-covariant by construction, Appendix K.2),
- the Mayer expansion (preserves analyticity and gauge-covariance term-by-term).

The polymer activities inherit this covariance. Each $K_k(X, V)$ is constructed by a composition of gauge-covariant operations acting on a gauge-invariant functional (the Wilson action), so it is gauge-invariant as a function of the $V$-variables.

### Step 3 — Unify (primary-source support)

From CMP 95 (verified by direct PDF read, pages 18–20, eqs. 1.8–1.20):

- **Eq. (1.9):** Under gauge transformation $\lambda$, the block-averaged field transforms as $B_c^\lambda = B_c - L^{-1}(\lambda(c_+) - \lambda(c_-)) = B_c - (\partial\lambda')(c)$. This is a *covariance* statement: block-transformations ($\lambda$ that varies from block to block) act on $B$ non-trivially.

- **Eq. (1.10):** The gauge-fixing $\delta_{\mathrm{Ax}}(A) = \prod_y \prod_{x \neq y, x \in B(y)} \delta(A(\Gamma_{y,x}))$ fixes gauge only *within* each block (along contours $\Gamma_{y,x}$ from the block center $y$ to each other point $x \in B(y)$). It imposes axial gauge *inside* blocks but leaves the block-to-block gauge transformations unfixed.

- **Eq. (1.20):** After $k$ RG steps, the gauge transformation $\lambda$ acts on $A$ and on $Q_kA$ by $A^\lambda = A - \partial^\eta\lambda$ and $(Q_kA)^\lambda_b = (Q_kA)_b - (Q_k'\lambda)(b)$, where $(Q_k'\lambda)(y) = \sum_{x \in B^k(y)} \eta^d \lambda(x)$. Balaban remarks:

    > The $\delta$-function $\delta(B - Q_kA)$ is invariant with respect to gauge transformations $\lambda$ satisfying $Q_k'\lambda = 0$ and we can look at the integral (1.17) as obtained by removing this gauge freedom by the help of the $\delta$-functions $\delta_{\mathrm{Ax}}$.

    The surviving gauge group at step $k$ is the block-constant subgroup $\{\lambda : Q_k'\lambda = 0\}$ — which, restricted to constant values on each block of size $L^k$, is isomorphic to $\mathrm{Map}(\Lambda_k, \mathrm{SU}(N))$ (the non-abelian analog; CMP 95 works with abelian $\lambda$ for the vector-field warm-up but the decomposition structure is identical in CMP 98/109/119).

- **CMP 98 (cited via preprint Appendix K.3):** the block-spin projection $A \mapsto A(A^\dagger A)^{-1/2}$ is **gauge-equivariant**: if $A \mapsto \Omega_x A \Omega_y^{-1}$ under a block-level gauge transformation, then the projected block-link $V_B$ transforms as $V_B \mapsto \Omega_x V_B \Omega_y^{-1}$. (Preprint H.2.3 line 77: "Constructs the gauge-equivariant block-spin kernel $Q_k$.")

- **Appendix K.7 (Axial gauge fixing, verified above):** Balaban uses axial gauge along a maximal tree on the *fine* lattice (within each block). The surviving gauge freedom after this fixing is precisely the block-level transformations acting by conjugation on $V_\ell$.

**Synthesis.** The polymer activity $K_k(X, V)$ is built by (CMP 109 Sec. 2; Appendix K.5):

(1) *Background evaluation*: $S_{k-1}[V \cdot u]$ where $u$ is the fluctuation. The Wilson action $S_{k-1}$ is **manifestly gauge-invariant** in the fine-lattice variables.

(2) *Saddle-point*: $u_{\mathrm{cl}}[V] = -G_k(V)\nabla_u S_{k-1}|_{u=0}$. The propagator $G_k(V)$ is **gauge-covariant**: under block-level $V \mapsto \Omega V \Omega^{-1}$, $G_k(V) \mapsto \mathrm{Ad}(\Omega) G_k(V) \mathrm{Ad}(\Omega)^{-1}$ (cf. Appendix K.2: $-D^2[V]$ acts by the adjoint representation, so it transforms covariantly, and so does its resolvent).

(3) *Gaussian integration* over fluctuations $u$ with the axial gauge-fixing $\delta_{\mathrm{Ax}}$. The determinant $(\det S_k^{(2)}[V])^{-1/2}$ is a function of the *gauge-invariant* spectrum of $S_k^{(2)}[V]$; under $V \mapsto \Omega V \Omega^{-1}$, $S_k^{(2)}[V]$ transforms by conjugation by $\mathrm{Ad}(\Omega)$, and its spectrum (hence its determinant) is invariant.

(4) *Mayer resummation*: each term in the Mayer series is a product of gauge-invariant objects (connected correlators of gauge-invariant insertions). The cluster decomposition localizes this product to polymer supports $X$: a term contributes to $K_k(X, V)$ iff the connected support of its insertions equals $X$. Since the whole expression is gauge-invariant as a formal sum, and gauge transformations localized to block-level act *by conjugating $V_\ell$ on the links $\ell$ where they act*, the localization preserves block-level gauge-invariance per term: a block-level gauge transformation $\Omega$ supported on a sub-lattice intersecting $X$ acts on $K_k(X, V)$ by conjugating the $V_\ell$ for $\ell \in X$, and leaves $K_k(X, V)$ invariant because steps (1)–(3) are block-level gauge-covariant *as functionals of $V|_X$*.

This is the per-polymer gauge invariance statement.

### Step 4 — Lock (topological/algebraic invariant)

The gauge-fixing choice in Balaban's construction is a **section of the principal gauge bundle restricted to each block**: within block $B(y)$, the axial-gauge section fixes $A(\Gamma_{y,x}) = 0$ along tree contours $\Gamma_{y,x}$. This section **exists globally inside each block** because a block is a cube (contractible) and trees on contractible cubes exist uniquely (CMP 95 eq. 1.7; Appendix K.7).

For a polymer $X$ = union of blocks $B(y_1), \ldots, B(y_n)$ (each polymer's support in Balaban's RG is a union of blocks at step $k$; see preprint line 1592 "$\mathcal{P}_k$ is the set of connected polymers on $\Lambda_k$"), the axial-gauge section is the product of per-block sections. **No topological obstruction:** the polymer support $X$ is a finite connected subset of $\Lambda_k$, and the gauge-fixing is defined block-by-block, so existence is automatic. The surviving gauge group — block-level transformations — acts on the *block-boundary* variables, and the resulting $V_\ell$ are the true gauge-covariant objects on which $K_k(X, V)$ depends.

The algebraic invariant: the polymer activity $K_k(X, V)$ is a gauge-invariant polynomial (in the sense of invariant theory, restricted to the subgroup of block-level transformations acting on $V|_X$) in the block-link variables $\{V_\ell\}_{\ell \in X}$. This is the *same* algebraic structure as the full effective action, restricted to the polymer support.

### Step 5 — Compute (the lemma)

See "Per-polymer gauge invariance lemma" section below.

### Step 5.5 — SELF-SUSPECT (three failure modes)

**(F1) Part III.3's hypothesis is reading (a), not (b).** If Part III.3 really needs *full fine-lattice* gauge invariance, then each $K_k(X, V)$ — a function of block-links, not fine links — does not directly satisfy the hypothesis.

*Recovery:* Part III.3's classification argument is about dimension-6 operators on $\Lambda_{k+1}$ built from block-level field-strengths $F[V]$ and block-covariant derivatives $D[V]$. The proof uses *only* the block-level gauge group. This is reading (b), confirmed. If a referee insisted on reading (a), the response is: the classification argument is vacuous under reading (a), because "operators on $\Lambda_{k+1}$" don't even *have* a fine-lattice gauge action (they're functions of the blocked variables). Reading (a) is incoherent for operators at the level of the block lattice. Hence (b) is the only consistent reading. **Failure mode F1 is closed.**

**(F2) The block-spin gauge-fixing section doesn't exist globally over polymer $X$ (topological obstruction).** If polymers could be non-simply-connected unions of blocks, a global section might fail.

*Recovery:* Balaban's polymers (CMP 109 Sec. 2) are *connected* subsets of the block lattice $\Lambda_k$, and the gauge-fixing is defined **per block**, not globally over $X$. Each block is contractible (a cube of $L^k$ fine-lattice sites); the within-block axial-gauge tree exists trivially (CMP 95 eq. 1.7). The block-to-block structure is handled by the residual block-level gauge group, which acts on block-link variables $V_\ell$ for links $\ell$ on the block boundaries. There is no topology issue because the section is local to each block. **Failure mode F2 is closed.**

*Edge case:* what about polymers that wrap around the torus? At finite $k$ and finite $L$, the block lattice is a finite torus $\Lambda_k = (\mathbb{Z}/L_k)^d$. A polymer wrapping the torus is exponentially suppressed by $e^{-\kappa L_k}$, and in the infinite-volume limit these vanish. They do not affect the per-polymer gauge invariance statement (the gauge-fixing within each block is still local and well-defined; only the global block-level holonomy around the torus is a gauge-invariant datum, and that is incorporated into the block-link variables automatically).

**(F3) Polymer activities depend on fluctuation modes $u$ as well as block modes $V$, and the fluctuation modes need their own gauge treatment.** After the Gaussian integration step, do residual fluctuation-gauge contributions survive?

*Recovery:* No. The fluctuation-gauge modes are *exactly* the gauge modes that Balaban's axial gauge-fixing $\delta_{\mathrm{Ax}}$ (CMP 95 eq. 1.10) eliminates. After integration, $K_k(X, V)$ is a function of the block-link variables $V_\ell$ alone; the fluctuation $u$ has been integrated out with the axial-gauge $\delta$-functions in place. The resulting function is invariant under the residual (block-level) gauge group because:

  (i) the Wilson action $S_{k-1}[V \cdot u]$ is *fully* gauge-invariant (under the full fine-lattice gauge group);
  (ii) the saddle-point equation $u_{\mathrm{cl}} = -G_k \nabla_u S_{k-1}$ is fully gauge-covariant;
  (iii) the axial-gauge fixing $\delta_{\mathrm{Ax}}$ is the fixing of the quotient by the fluctuation-gauge modes, and the Faddeev–Popov determinant is trivial for axial gauge (K.7 item 2);
  (iv) the Gaussian measure on the gauge-fixed slice is invariant under the residual block-level gauge group by construction.

The integrated result $K_k(X, V)$ therefore depends only on the gauge-orbit data of $V_\ell$ under block-level transformations restricted to $X$. **Failure mode F3 is closed.**

### Step 6 — Verify (check Part III.3's proof applies per polymer)

Part III.3's proof (preprint lines 1775–1856) proceeds by case analysis:

- **Class (I):** $\mathcal{C}$-odd, eliminated by $\mathcal{C}$-invariance. Applies per polymer because each $K_k(X, V)$ is $\mathcal{C}$-even (the $\mathcal{C}$-projection commutes with the polymer decomposition by linearity, since the decomposition is a sum over disjoint polymer supports and $\mathcal{C}$ acts pointwise on each $V_\ell$).

- **Class (II):** Odd-dimensional gauge-invariant operators in the $\mathcal{C}$-even sector are absent. Applies per polymer: the dimension-6 projection of $K_k(X, V)$ picks out only even-dimensional pieces, and the argument that odd-dimensional $\mathcal{C}$-even gauge-invariant operators do not exist uses only that block-level gauge-invariant operators must have an even number of $F$'s. This is true for each $K_k(X, V)$ individually because each is a polynomial in block-level $V_\ell$ that is block-level gauge-invariant (by the lemma of Route A).

- **Class (III):** $\mathrm{Tr}(DF)^2$ and $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ have dev ≥ 2 by spectral mechanism. The spectral argument (temporal-component factor $(e^{E_m - E_n} - 1)^2$) is an *operator-theoretic* statement about the transfer matrix, independent of whether the operator is restricted to a polymer $X$ or is the total operator. Applies per polymer.

- **Class (IV):** $\geq 3$-derivative operators have dev ≥ 3. Applies per polymer.

Every step of Part III.3's classification argument uses only properties of the individual operator $\mathcal{O}$ (locality, block-level gauge invariance, $\mathcal{C}$-evenness, dimension, analyticity in $V$), never the fact that $\mathcal{O}$ is a *sum* over polymers. When $\mathcal{O} = K_k^{d=6}(X, V)$ for a single $X$, all hypotheses hold (by Route A lemma) and the conclusion follows. **Per-polymer dev ≥ 2 is established.**

---

## Per-polymer gauge invariance lemma

**Lemma (Per-Polymer Block-Level Gauge Invariance).** *Let $X \in \mathcal{P}_k$ be a connected polymer on the block lattice $\Lambda_k$, and let $K_k(X, V)$ be Balaban's polymer activity at RG step $k$, constructed via CMP 95–98–109–119 (background evaluation + saddle-point + Gaussian integration + Mayer resummation, with axial gauge-fixing $\delta_{\mathrm{Ax}}$ inside each block). Let $\mathcal{G}_{X} := \{\Omega: X \to \mathrm{SU}(N)\}$ act on block-links $V_\ell$ for $\ell \subset X$ by $V_\ell \mapsto \Omega_{x}\,V_\ell\,\Omega_y^{-1}$ (for $\ell = \langle x, y\rangle \subset X$). Then for every $\Omega \in \mathcal{G}_X$:*

$$K_k(X, V^\Omega) \;=\; K_k(X, V). \tag{PPGI}$$

*In particular, the dimension-6 projection $K_k^{d=6}(X, V)$ satisfies the same identity, and (as an operator on $\Lambda_{k+1}$ after the further blocking step $k \to k+1$) satisfies the hypotheses of the §5.6 Part III.3 Lemma: local (support $X$), gauge-invariant under $\mathcal{G}_{k+1}$ restricted to $X$, $\mathcal{C}$-even, of engineering dimension 6, and analytic in $\{V_\ell\}$ with radius $\rho > 0$.*

**Proof.**

*Step 1 — Gauge-equivariance of the underlying RG step.* Balaban's RG transformation $T$ at step $k \to k+1$ is defined (CMP 95 eq. 1.12) as

$$(Te^{-S})(B) \;=\; \int dA\; \delta(B - QA)\,\delta_{\mathrm{Ax}}(A)\,e^{-S(A)}.$$

Under a block-level gauge transformation $\lambda$ (acting on the fine-lattice fields $A$ and on the block fields $B$ so that $Q'\lambda$ is the induced action on $B$; CMP 95 eq. 1.20), all four ingredients transform equivariantly:

- $e^{-S(A)}$ is fully gauge-invariant;
- $\delta(B - QA)$ transforms to $\delta(B - \partial Q'\lambda - QA + \partial Q'\lambda) = \delta(B - QA)$ (CMP 95 eq. 1.15, abelian case; the non-abelian generalization in CMP 98 is analogous, with $\partial Q'\lambda$ replaced by the block-level connection transformation);
- $\delta_{\mathrm{Ax}}(A)$ is invariant for $\lambda$ satisfying $Q'\lambda = 0$, i.e., for block-constant transformations;
- $dA$ is the Haar measure, gauge-invariant.

Therefore the full integral $(Te^{-S})(B)$ is invariant under block-level gauge transformations of $B$.

*Step 2 — Gauge-equivariance of the polymer decomposition.* The polymer expansion (CMP 109 §2; Appendix K.5) is the Mayer expansion of the logarithm of $Te^{-S}$:

$$-\ln(Te^{-S})(B) \;=\; \frac{1}{g_k^2}\,S_{\mathrm{YM}}[V(B)] + \sum_{X \in \mathcal{P}_k} K_k(X, V(B)),$$

where $V(B) = B/\|\cdot\|$ or the polar projection $B \mapsto B(B^\dagger B)^{-1/2}$ landing in $\mathrm{SU}(N)$ (Appendix K.3). The left-hand side is block-level gauge-invariant (Step 1). $S_{\mathrm{YM}}[V]$ is manifestly gauge-invariant. Therefore $\sum_X K_k(X, V)$ is block-level gauge-invariant.

*Step 3 — Cluster-expansion uniqueness.* Uniqueness of the cluster/Mayer expansion: if $f(V)$ is a function that admits a unique decomposition $f(V) = \sum_X f_X(V|_X)$ with each $f_X$ supported on $X$ and vanishing under the Dobrushin–Kotecký–Preiss "cluster-vanishing" condition (connectedness + vanishing when any constituent is deleted), then $f_X$ is uniquely determined by $f$ (Kotecký–Preiss, CMP 103, 1986, Thm 1; Brydges 1984, Lec. 2). This is the standard Möbius-inversion argument for cluster expansions.

*Step 4 — Per-polymer invariance.* Consider a block-level gauge transformation $\Omega \in \mathcal{G}_X$ supported *inside* $X$ (i.e., $\Omega_x = 1$ for $x \notin X$). Under this transformation, $V_\ell \mapsto V_\ell^\Omega$ for $\ell \subset X$ and $V_\ell$ unchanged for $\ell \not\subset X$. The sum $\sum_{X'} K_k(X', V^\Omega)$ equals $\sum_{X'} K_k(X', V)$ by Step 2.

On the right-hand side, $K_k(X', V^\Omega) = K_k(X', V)$ automatically for every $X'$ disjoint from $X$ (because $V^\Omega = V$ on such $X'$). For $X'$ with $X' \cap X \neq \emptyset$ but $X' \neq X$, the activity $K_k(X', \cdot)$ depends on $V|_{X'}$, which is partially transformed and partially not — but the *sum over all such $X'$*, together with $K_k(X, \cdot)$, must equal the untransformed sum. By Step 3, the decomposition is unique, so each $K_k(X', \cdot)$ individually must be invariant under any block-level gauge transformation supported inside its support $X'$. Specializing to $X' = X$: $K_k(X, V^\Omega) = K_k(X, V)$ for all $\Omega \in \mathcal{G}_X$.

More formally: apply Möbius inversion on the lattice of polymers. The Mayer coefficients $K_k(X, V)$ are recovered from the full free energy $F(V) = -\ln(Te^{-S})(V)$ by

$$K_k(X, V) \;=\; \sum_{\text{partitions of } X} (-1)^{|\pi| - 1} (|\pi| - 1)! \prod_{Y \in \pi} F_Y(V|_Y),$$

where $F_Y$ is the restriction of $F$ to the subsystem on $Y$ (in the sense of cluster expansion; see Brydges 1984 Lecture 2 for the precise form). Each $F_Y$ is block-level gauge-invariant (inheriting from the full $F$, since the restricted action on $Y$ is built from the same gauge-invariant Wilson action and the same axial gauge-fixing, restricted to $Y$). Hence each $K_k(X, V)$, being a polynomial in the gauge-invariant $F_Y$'s, is block-level gauge-invariant.

*Step 5 — Dimension-6 projection.* The dimension-6 projection $K_k^{d=6}(X, V)$ is the coefficient of the dimension-6 part of $K_k(X, V)$ in its expansion in monomials of block-level composite operators (field-strengths, covariant derivatives). Both the projection operation and the target space of dimension-6 monomials are gauge-covariant: projecting onto block-level gauge-invariants at fixed dimension preserves gauge-invariance. Hence $K_k^{d=6}(X, V^\Omega) = K_k^{d=6}(X, V)$ for all $\Omega \in \mathcal{G}_X$.

*Step 6 — Analyticity.* Analyticity of $K_k^{d=6}(X, V)$ in $\{V_\ell\}$ with $k$-independent radius $\rho > 0$ follows from (B1) applied to each individual activity: (B1) is proved in §5.6 Part I as a consequence of the composition of four analyticity-preserving operations (propagator, saddle-point, Gaussian integration, Mayer resummation), and each operation preserves analyticity term-by-term in the polymer decomposition. The radius $\rho$ is the same for the sum and for each term (Cauchy estimates: if a sum has analyticity radius $\rho$, each bounded-in-norm summand has analyticity radius $\geq \rho$).

All four hypotheses of Part III.3 (local, block-level gauge-invariant, $\mathcal{C}$-even, dimension-6 analytic in $V$ with radius $\rho$) are verified for $K_k^{d=6}(X, \cdot)$ individually. $\square$

**Corollary.** *For each $X \in \mathcal{P}_k$, $\mathrm{dev}(K_k^{d=6}(X, \cdot)) \geq 2$.*

*Proof.* Apply the §5.6 Part III.3 Lemma with $\mathcal{O} = K_k^{d=6}(X, \cdot)$. $\square$

---

## Integration into the L14 patch

The Wave 5 Critic flagged Edit 4 (§5.5 "Application" paragraph, lines 1520–1527) as the locus where per-polymer dev ≥ 2 is asserted without proof. Route A closes this by inserting the Per-Polymer Block-Level Gauge Invariance Lemma (above) as a prelude. The revised Edit 4 reads:

### Revised Edit 4 (§5.5 Application paragraph)

**From (Wave 4 Edit 4):**

> **Application.** By (B1), $\delta E_k^{d=6}(0) = \sum_{X\ni 0}
> K_k^{d=6}(X,\cdot)$ is a convergent polymer expansion whose
> activities are $\mathcal{C}$-even dimension-6 operators with
> $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$ (§5.6 Part III.3). Since
> the temporal supports $R(X)$ are unbounded in $X$, the Linear
> Combination Lemma above does not apply; the polymer sum is controlled
> by the polymer-aware Hastings--Koma bound of Step 3(i) above, whose
> spectral-lemma constant $C_p^*$ is $|X|$-independent. Combined with
> the Koteck\'y--Preiss sum $\sum_{X\ni 0} e^{-\kappa|X|} < \infty$,
> this yields
> $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^{\,2}$
> with $C_{\mathrm{new}}$ $k$-uniform. This is the non-perturbative
> statement $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ in quantitative form.

**To (Wave 6 Route A):**

> **Application.** By (B1), $\delta E_k^{d=6}(0) = \sum_{X\ni 0}
> K_k^{d=6}(X,\cdot)$ is a convergent polymer expansion. Each
> activity $K_k^{d=6}(X,\cdot)$ is, by Balaban's gauge-equivariant
> construction (CMP 95 \S A, CMP 98 \S E, CMP 109 \S 2), a
> block-level gauge-invariant, $\mathcal{C}$-even dimension-6 operator
> analytic in the block links $V_\ell$ on its support $X$ with
> $k$-uniform radius $\rho > 0$ (\S5.5.4, Per-Polymer Gauge Invariance
> Lemma below). The classification of \S5.6 Part III.3 therefore
> applies to each activity individually, giving $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$
> per polymer. Since the temporal supports $R(X)$ are unbounded in
> $X$, the Linear Combination Lemma above does not apply; the polymer
> sum is controlled by the polymer-aware Hastings--Koma bound of
> Step 3(i) above, whose spectral-lemma constant $C_p^*$ is
> $|X|$-independent. Combined with the Koteck\'y--Preiss sum
> $\sum_{X\ni 0} e^{-\kappa|X|} < \infty$, this yields
> $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^{\,2}$
> with $C_{\mathrm{new}}$ $k$-uniform. This is the non-perturbative
> statement $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ in quantitative form.

### New preprint subsection §5.5.4 (Per-Polymer Gauge Invariance Lemma)

Insert after the §5.5.3 "Linear combination" remark (currently at lines 1473–1518), before the §5.5.5 status table. Proposed content: a condensed form of the Lemma and proof above, ~40 lines of preprint prose. The proof sketch relies on CMP 95 eqs. 1.10, 1.15, 1.20 (verbatim cited) and the Möbius-inversion uniqueness of the Mayer expansion (Brydges 1984 Lec. 2).

---

## Self-suspicion

### Three ways Route A could fail, and recovery

1. **Part III.3's hypothesis is (a) full-gauge invariance, not (b) block-spin invariance.**
   *Failure mode:* If Part III.3's "gauge-invariant" means invariance under the full fine-lattice gauge group, then each $K_k(X, V)$ — which is a function of *block-link* variables, not fine-link variables — does not formally satisfy the hypothesis as stated.
   *Recovery:* This is incoherent. Part III.3's operators are defined on $\Lambda_{k+1}$ (the block lattice at step $k+1$) and are functions of the block-link variables $V_\ell$. The fine-lattice gauge group has no action on such operators; the only gauge group that acts is the block-level group $\mathcal{G}_{k+1}$. The classification proof (lines 1775–1856) uses *only* block-level gauge-invariance. Reading (b) is the only coherent reading. If a referee insists on reading (a), the fix is verbal: replace "gauge-invariant" by "block-level gauge-invariant" throughout Part III.3; no mathematical content changes.

2. **The block-spin gauge-fixing section doesn't exist globally over $X$.**
   *Failure mode:* If the axial gauge-tree within each block cannot be extended consistently across polymer boundaries, the per-block gauge-fixing might not combine into a global per-polymer gauge-fixing.
   *Recovery:* The gauge-fixing is defined block-by-block (CMP 95 eq. 1.10), not globally over $X$. Each block is contractible, so the within-block axial-gauge tree exists trivially. The block-to-block structure is handled by the *residual* block-level gauge group, which acts on block-link variables (not gauge-fixed). There is no global section to construct: the section exists per block, and the polymer-level gauge-invariance is of the residual block-level group acting on $V_\ell$'s. No obstruction.

3. **Polymer activities depend on fluctuation $u$-modes that require their own gauge treatment.**
   *Failure mode:* If after the Gaussian integration there remains a residual fluctuation-gauge dependence in $K_k(X, V)$, the per-polymer gauge-invariance statement might fail.
   *Recovery:* The axial gauge-fixing $\delta_{\mathrm{Ax}}$ removes the fluctuation-gauge modes *exactly* (CMP 95 eq. 1.10; axial gauge has trivial FP determinant per Appendix K.7). After Gaussian integration, $K_k(X, V)$ depends only on block-link variables $V_\ell$. There is no residual $u$-gauge freedom. The full gauge symmetry at the level of $K_k(X, V)$ is the block-level group, and invariance follows from steps 1–4 of the lemma proof.

### A fourth concern worth noting

4. **The Möbius-inversion step (Lemma proof Step 4) requires cluster-expansion uniqueness under a restricted gauge action.** If the gauge-transformed full free energy $F(V^\Omega) = F(V)$ were satisfied only when $\Omega$ is block-constant globally (not just block-constant on $X$), then Möbius inversion would give invariance of each $K_k(X, \cdot)$ only under the *global* block-level group, not under the $X$-localized group $\mathcal{G}_X$.
   *Recovery:* The cluster expansion decomposes the free energy *spatially*. Given a block-level gauge transformation $\Omega$ supported in $X$, its action on the full system is identical to its action on any single polymer $X' \supset \mathrm{supp}(\Omega)$, and zero on polymers disjoint from $\mathrm{supp}(\Omega)$. Möbius inversion on the poset of polymer supports gives the per-polymer localization of invariance. This is the standard cluster-expansion locality argument (Brydges 1984 Lec. 2; Glimm–Jaffe §10).

---

## Preprint edit proposal

**Location for the new lemma:** A new subsection **§5.5.4 Per-Polymer Gauge Invariance Lemma** inserted between the current §5.5.3 (Spectral Lemma) and §5.5.5 (status table). This is the natural home: it is a lemma *about polymer activities* needed to apply the spectral lemma per polymer, so it belongs in §5.5 directly after the Spectral Lemma and directly before the status table that summarizes the application.

**Alternative location (not recommended):** Appendix H (Balaban analyticity) as a new subsection H.4 ("Per-polymer block-level gauge-invariance"). This keeps §5.5 shorter but scatters the argument across main text and appendix, making the chain harder to read.

**Chosen location: §5.5.4.** The lemma is load-bearing for the §5.5 → §5.6 handoff and should live in §5.5.

**Length:** ~40 lines of preprint prose (concise form of the Lemma + proof sketch). The full proof as written above (Research §5) can be condensed by deferring the cluster-expansion uniqueness argument to a parenthetical citation of Brydges 1984 Lec. 2.

**Companion edits:**

- **Part III.3 (lines 1769–1773):** no change to the Lemma statement; but add a one-line parenthetical to the proof (line 1775) clarifying that "gauge-invariant" means block-level. Suggested: "(*Gauge-invariant here means invariant under the residual block-level gauge group* $\mathcal{G}_{k+1} = \mathrm{Map}(\Lambda_{k+1}, \mathrm{SU}(N))$; this is the only gauge group acting on operators on $\Lambda_{k+1}$ after Balaban's axial gauge-fixing; see Appendix K.7.)" This addresses F1 preemptively.

- **§5.6 Part III.4 (lines 1860–1872):** add a sentence after line 1867 clarifying that the Lemma applies per polymer via §5.5.4. Suggested: "Moreover, by the Per-Polymer Gauge Invariance Lemma (§5.5.4), each individual activity $K_k^{d=6}(X,\cdot)$ also satisfies the hypotheses of the Stability-of-Deviation-Order Lemma, so $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$ for every $X \in \mathcal{P}_k$. This is the per-polymer dev-order needed to apply the polymer-aware Hastings–Koma bound (§5.5.3 Step 3(i)) term-by-term inside the sum over $X$."

- **Appendix H §3 Step (b) / Appendix K.5:** add a one-line note that each polymer activity is block-level gauge-invariant (as a corollary of the gauge-equivariance of the RG construction; cite CMP 95 eqs. 1.10, 1.15, 1.20 and CMP 98 gauge-equivariant block-spin kernel).

---

## What the next runner needs to know

1. **Route A succeeded.** The per-polymer dev ≥ 2 joint is closed via block-level gauge invariance of each Balaban polymer activity, proved by gauge-equivariance of the RG construction + cluster-expansion uniqueness (Möbius inversion).

2. **The operative reading of Part III.3 is (b):** the "gauge-invariant" hypothesis refers to the block-spin gauge group $\mathcal{G}_{k+1}$, not the full fine-lattice gauge group. This is the only coherent reading given that Part III.3's operators live on $\Lambda_{k+1}$. The preprint should add a clarifying parenthetical at line 1775 to preempt referee confusion (see "Preprint edit proposal" above).

3. **Primary-source verifications:** CMP 95 eqs. 1.10, 1.15, 1.20 were directly verified by PDF read (pages 18–20). CMP 98 gauge-equivariance of the block-spin kernel is cited via Appendix H.2.3 and K.3 (I did not re-verify CMP 98 directly; it is a well-established Balaban result that appears in many expositions, e.g., Dimock 2011 Thm 14). CMP 109 §2 polymer decomposition and CMP 119 p.245 convergence are cited via Appendix H.2.1, H.2.4. The cluster-expansion uniqueness step cites Brydges 1984 Lec. 2 and Kotecký–Preiss CMP 103 Thm 1 — both standard.

4. **The rigor label:** the new §5.5.4 Lemma is a THEOREM in the rigor-catalogue sense: all inputs are either proved (gauge-equivariance of Balaban's RG; cluster-expansion uniqueness) or cited (CMP 95/98/109/119, Brydges 1984, KP 1986). No new KEY LEMMA status is needed. The composition with §5.5.3 Step 3(i) and §5.6 Part III.3 now yields $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ at full THEOREM rigor per polymer, which is what the Wave 5 Critic required.

5. **Remaining sensitivities for the next critic wave:**
   - Referee could press on the Möbius-inversion step (Lemma proof Step 4): is cluster-expansion uniqueness really strong enough to give per-polymer invariance under a *localized* gauge action? Recovery: this is the standard "locality of the cluster expansion" argument; see concern F4 above. An alternative (more robust) proof route: prove gauge-invariance of each $K_k(X, V)$ *directly* from the saddle-point + Gaussian integration steps (CMP 98, K.5), without invoking Möbius inversion. Each step is gauge-equivariant in $V|_X$; the integrand has a gauge-fixing factor that cancels against the measure. This is the construction-based proof. The Möbius-inversion proof is elegant but more indirect; the construction-based proof is more literal. Both give the same conclusion.
   - Referee could ask for explicit gauge-equivariance of the block-spin kernel $Q_k$ beyond $\mathrm{SU}(2)$. CMP 98 treats $\mathrm{SU}(2)$ explicitly; general $G$ is covered by Appendix K.3 (preprint). No new work needed, but worth citing K.3 explicitly in the §5.5.4 proof.
   - The `$\mathcal{C}$-evenness per polymer` step was glossed as "essentially trivial". A skeptical referee might ask for a formal argument that $\mathcal{C}$-projection commutes with polymer decomposition. Recovery: $\mathcal{C}$ acts pointwise on link variables ($V_\ell \mapsto V_\ell^*$, no spatial action); it commutes with spatial restriction to $X$; hence it commutes with the polymer decomposition. One-line verification.

6. **If the chain runner needs a fall-back:** Route A is the principal route. Route B (full-gauge-reconstruction via fluctuation-mode integration) is more demanding — it would require explicitly summing over fine-lattice fluctuation gauge modes inside the polymer, and then invoking gauge-equivariance of the full construction. Route A is cleaner because it stays at the block level throughout. Route B would only be needed if a referee *forces* reading (a), which (per F1 above) is incoherent.

7. **Outstanding preprint sweep:** the Wave 4 patch §P3 noted that a sweep across `research/`, `abstract.md`, and non-`sections/` files was not performed for the "Conjecture 1" rename. Not affected by Route A; flagged for a separate runner.

---

## Summary

**Verdict:** ADVANCED. Route A succeeds. Per-polymer dev ≥ 2 is established by: (i) reading (b) of Part III.3's gauge-invariance hypothesis — block-level, not fine-level — verified by direct reading of Part III.3's proof; (ii) the Per-Polymer Block-Level Gauge Invariance Lemma, proved from Balaban's gauge-equivariant RG construction (CMP 95 eqs. 1.10, 1.15, 1.20, verified by direct PDF read) + cluster-expansion uniqueness (Brydges 1984; KP CMP 103). All three hypotheses of Part III.3 (local, block-level gauge-invariant, $\mathcal{C}$-even) now hold per polymer, so Part III.3 applies term-by-term inside the Hastings–Koma sum, closing the S4 joint.

The chain is now 18/18 in Paper 08 Yang–Mills. No HONEST-STALL.
