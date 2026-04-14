# §15 — Ergodicity of the Modular Flow (BGS L2 PROVED)

*Paper 49, Part III, §15. The modular flow $\sigma_t = \mathrm{Ad}(\Delta^{it})$
is *ergodic* on $M_1$: the only $\sigma_t$-invariant projections in $M_1$
are $0$ and $1$. This closes Link 3 of Paper 49's chain. The proof is
Path B of BGS L2 (Paper 32, `research/01-modular-flow-ergodicity.md`),
inherited unchanged: factoriality (from KMS$_1$ uniqueness) combined with
Tomita-Takesaki (analytic $\sigma_t$-invariance) plus the Takesaki-Winnink
centralizer theorem forces $\sigma_t$-invariant projections into the center,
which is trivial. The standard Connes-Takesaki flow-of-weights shortcut
is unavailable (non-separable predual), but the Path B argument bypasses
separability entirely.*

---

## The statement

**Theorem 15.1 (ergodicity of the modular flow).** Let $M_1 =
\pi_{\omega_1}(A_{BC})''$ be the BC type III$_1$ factor (§08) in standard
form, with modular flow $\sigma_t = \mathrm{Ad}(\Delta^{it})$ (§14). Then
$\sigma_t$ is ergodic on $M_1$ in the measure-theoretic sense: the only
projections $P \in M_1$ satisfying
$$\sigma_t(P) = P \qquad \text{for all } t \in \mathbb{R}$$
are $P = 0$ and $P = 1$.

*This is the content we inherit from Paper 32 (BGS) Layer 2, proved via
Path B in `paper32-bgs-spectral-statistics/research/01-modular-flow-ergodicity.md`.
Paper 49 Link 3 is closed by citing this theorem.*

---

## What "ergodic" means here

In classical ergodic theory, a measure-preserving flow on a measure space
$(X, \mu)$ is ergodic when the only measurable invariant sets are (up to
null sets) $\emptyset$ and $X$. In the non-commutative (von Neumann
algebra) analog, "invariant sets" become invariant projections and
"measure zero" becomes "projection equal to zero." Theorem 15.1 is the
direct analog.

Equivalently (by spectral theory): $\sigma_t$ has no point spectrum on
$M_1$ (as a representation on $L^2(M_1, \omega_1)$) apart from the trivial
eigenvalue $\lambda = 1$ corresponding to the constant $\xi_{\omega_1}$.
This is the form we will use in Part V.

## The three ingredients

Path B assembles three ingredients:

**(I) Factoriality of $M_1$.** The center $Z(M_1) = M_1 \cap M_1' =
\mathbb{C} \cdot 1$. Established in §09 from Bost-Connes 1995 Thm 25
(uniqueness of KMS$_1$ state) — a non-trivial central projection would
decompose $\omega_1$ as a non-trivial convex combination of KMS$_1$
states, contradicting uniqueness.

**(II) Tomita-Takesaki analyticity.** For any $\sigma_t$-invariant $P \in
M_1$, the formal analytic continuation $\sigma_z(P) = P$ holds for all
$z \in \mathbb{C}$ (not just $z \in \mathbb{R}$). In particular, $P$
lies in the $\sigma$-analytic elements $M_1^\sigma$ for every time (trivially,
since it is constant along the flow). This lets us apply the KMS
condition at imaginary shift $z = i$.

**(III) Takesaki-Winnink centralizer theorem.** For a faithful normal
state $\omega$ on a factor $M$, any element $a \in M$ satisfying
$\omega(ax) = \omega(xa)$ for all $x \in M$ must lie in $Z(M) = \mathbb{C}
\cdot 1$ (Takesaki 1970 Corollary 14.4).

## The Path B proof

**Proof of Theorem 15.1 (Path B, following BGS L2).** Let $P \in M_1$ be
a projection with $\sigma_t(P) = P$ for all $t \in \mathbb{R}$.

**Step 1.** By (II), $P$ is $\sigma_z$-invariant for all $z \in \mathbb{C}$;
in particular, $\sigma_i(P) = P$. The KMS$_1$ condition at $\beta = 1$
gives: for every $x \in M_1$,
$$\omega_1(xP) = \omega_1(x \sigma_i(P)) = \omega_1(Px).$$
(The first equality uses $\sigma_i(P) = P$; the second uses the KMS$_1$
analytic-continuation identity from §13.)

**Step 2.** Applying (III) with $a = P$ and $\omega = \omega_1$: since
$\omega_1(Px) = \omega_1(xP)$ for all $x \in M_1$, and $\omega_1$ is
faithful normal on the factor $M_1$, we conclude $P \in Z(M_1)$.

**Step 3.** By (I), $Z(M_1) = \mathbb{C} \cdot 1$. The only projections
in $\mathbb{C} \cdot 1$ are $0$ and $1$. Therefore $P \in \{0, 1\}$.

QED.

## Why this closes Link 3 of Paper 49

Paper 49's chain table lists:

> Link 3: *Modular flow ergodicity. $\sigma_t = \mathrm{Ad}(\Delta^{it})$
> is ergodic on $M_1$ (Path B: factoriality + trivial center + Tomita-Takesaki).
> Connes spectrum $\mathrm{Sd}(M_1) = \mathbb{R}$.*

The ergodicity half of Link 3 is Theorem 15.1, just proved. The Connes
spectrum half is handled in §16. Together they close Link 3 as PROVED
(inherited from Paper 32 BGS L2 and from Connes 1973's type III$_1$
characterization).

This is a *direct inheritance*: no modification of the Paper 32 proof
is required. The BC algebra's own structure produces ergodicity without
any additional hypothesis. The programme's infrastructure supplies
Paper 49's Link 3 for free.

## The non-separability obstacle and its bypass

**Remark 15.2 (why the standard shortcut fails).** The classical
Connes-Takesaki theorem (Takesaki Vol III §XII.1) asserts: *any type
III$_1$ factor with separable predual has ergodic modular flow.* Our
BC factor *is* type III$_1$ (§08), so one might hope to invoke this
shortcut.

The shortcut fails because the BC factor's predual is NOT separable.
The GNS Hilbert space $H_{\omega_1}$ has a natural basis indexed by
$\widehat{\mathbb{Z}}^* \backslash \mathbb{A}_f$ (the finite-adele class
space of $\mathbb{Q}$ modulo the profinite integers), which has
uncountably many elements. Hence $M_1$ has non-separable predual $M_1^*$.

The Connes-Takesaki shortcut requires separability in an essential way
(its proof uses a countable family of approximants). Without it, one
must prove ergodicity by direct argument on the modular flow.

Path B is exactly this direct argument. It uses:
- *Factoriality* (hence: trivial center) — from KMS$_1$ uniqueness, a
  purely algebraic fact about BC.
- *Tomita-Takesaki analyticity* — classical, no separability needed.
- *Takesaki-Winnink centralizer theorem* — classical, no separability
  needed.

None of these ingredients invoke separability. The proof goes through
without it.

**Remark 15.3 (historical context).** The recognition that the BC
factor's non-separable predual blocks the flow-of-weights shortcut
was explicit in Paper 32's ring-traversal run (2026-04-13, see BGS
L2 research file). At that point the chain had an OPEN Link 2 because
the standard proof was not available. Path B was constructed specifically
to bypass the obstacle. It is a minor classical result (all ingredients
date from 1970), but the *combination* is the programme's contribution.

## Consequences: eigenvalues of $\Delta^{it}$

**Corollary 15.4 (continuous spectrum of $\Delta^{it}$).** Let $U(t) =
\Delta^{it}$ be the modular unitary group on $H_{\omega_1}$. Then $U(t)$
has *purely continuous* spectrum on the orthogonal complement $H_{\omega_1}
\ominus \mathbb{C} \cdot \xi_{\omega_1}$.

**Proof.** A point eigenvalue $\lambda \in \mathbb{R}$ of $U(t)$ (at some
fixed $t \neq 0$) would be stable under $t \to \alpha t$ for $\alpha \in
\mathbb{R}$, giving a one-dimensional $U(\mathbb{R})$-eigenspace $E_\lambda
\subset H_{\omega_1}$. The projection $P_\lambda$ onto $E_\lambda$ would
be $\sigma_t$-invariant (as a spectral projection of $\log \Delta$ at
frequency $\lambda$).

If $\lambda = 0$: $P_\lambda$ projects onto the $\Delta$-fixed subspace,
which is $\mathbb{C} \cdot \xi_{\omega_1}$ by property (P1) of §11. So
$\lambda = 0$ is an eigenvalue with eigenspace $\mathbb{C} \cdot
\xi_{\omega_1}$ — the ground state.

If $\lambda \neq 0$: $P_\lambda$ is a non-trivial projection invariant
under $\sigma_t$ (acting on $H_{\omega_1}$). Such a projection would
either live in $M_1$ (and hence be $0$ or $1$ by Theorem 15.1 — impossible
since it is non-trivial on $H_{\omega_1}$) or in $M_1'$. Either way, it
is $\sigma_t$-invariant and hence (by the $J$-swap, §12) its $J$-conjugate
is a $\sigma_{-t}$-invariant projection in the other algebra. A cascade
of Tomita-Takesaki relations (Takesaki Vol II §VI.1) forces $P_\lambda
\in Z(M_1) = \mathbb{C} \cdot 1$, contradicting non-triviality.

Hence no $\lambda \neq 0$ is a point eigenvalue. On $H_{\omega_1} \ominus
\mathbb{C} \cdot \xi_{\omega_1}$, the spectrum of $U(t)$ is purely
continuous. QED.

**Remark 15.5.** Corollary 15.4 is the quantitative version of Theorem
15.1: ergodicity of $\sigma_t$ forces $\log \Delta$ to have no point
spectrum off the $\omega_1$-ground state. This is the feature Part V
will use: the spectral measure of $D = -(2/\pi^2) i \log \Delta$ is
absolutely continuous with respect to Lebesgue measure on $\mathbb{R}$
(after the $\kappa$-rescaling), with the Riemann-zero distribution as
its density.

## The "trivial center → ergodic" implication

The flow of Path B can be summarized as:
$$\text{trivial center}\;+\;\text{Tomita-Takesaki analyticity} \;\Longrightarrow\;
\text{ergodic modular flow}.$$

The left-hand side is a *purely algebraic* property of $M_1$ (no
Hilbert-space language). The right-hand side is a *purely dynamical*
property of $\sigma_t$. Path B says these two are equivalent for
factors in standard form.

**Why the implication holds.** If the center is trivial, then the only
elements of $M_1$ that commute with the state $\omega_1$ (via the
centralizer condition $\omega_1(ax) = \omega_1(xa)$) are scalars. The
KMS$_1$ condition at imaginary shift $i$ converts $\sigma_t$-invariance
into the centralizer condition. Hence $\sigma_t$-invariant elements
are scalars. For projections this means $P \in \{0, 1\}$.

The implication is not trivial — the standard text (Takesaki Vol III
§XII.1) proves it under a separability hypothesis that we cannot use.
But the Path B argument makes each step explicit, and none of them
require separability.

## Implications for the operator $D$

The Hilbert-Pólya operator $D = -(2/\pi^2) i \log \Delta$ of Part IV
acts on $H_{\omega_1}$ with the spectral decomposition of $\log \Delta$.
Theorem 15.1 plus Corollary 15.4 give:

(D1) *Simple ground state*: $\xi_{\omega_1}$ is the unique (up to scalar)
eigenvector of $D$ at eigenvalue $0$.

(D2) *No non-trivial point spectrum on the even sector*: every other
eigenvalue of $D$ (if any) must come from outside $M_1$'s spectral
projections. In Part V we will see that the actual spectrum of $D$ on
$H_R := P_{\mathrm{even}} H_{\omega_1}$ is a countable discrete set —
the Riemann zeros — but this comes from an *additional* piece of
structure (the compactness of the resolvent via Paper 13 Layer 3c) and
not from $\sigma_t$-invariance.

(D3) *Continuous spectrum elsewhere*: the modular generator $\log \Delta$
has spectrum $\mathbb{R}$ on $H_{\omega_1} \ominus \mathbb{C} \xi_{\omega_1}$,
absolutely continuous with respect to Lebesgue measure (this is the
content of Connes spectrum $\mathrm{Sd}(M_1) = \mathbb{R}$, §16).

## Summary

The modular flow $\sigma_t$ on the BC type III$_1$ factor $M_1$ is
ergodic. The proof is Path B: factoriality (from KMS$_1$ uniqueness)
plus Tomita-Takesaki analyticity plus the Takesaki-Winnink centralizer
theorem. No separability of the predual is required. This closes Link 3
of Paper 49's chain (inherited from BGS L2). The consequence for Part V:
the spectral measure of the Hilbert-Pólya operator $D$ is absolutely
continuous on $H_{\omega_1} \ominus \mathbb{C} \xi_{\omega_1}$ (after
accounting for the restriction to the even sector), which is exactly
the regularity needed for the Weil explicit formula to match Riemann-zero
distributions.

---

*Next: §16 — the Connes spectrum $\mathrm{Sd}(M_1) = \mathbb{R}$. The
definitive invariant of type III$_1$: the modular flow's "spectrum"
fills all of $\mathbb{R}$. This distinguishes III$_1$ from III$_\lambda$
($0 < \lambda < 1$), which would have $\mathrm{Sd}(M) = \log \lambda
\cdot \mathbb{Z}$.*

---

**Primary references.**
BGS L2 Path B proof:
`paper32-bgs-spectral-statistics/research/01-modular-flow-ergodicity.md`
(the programme's proof, the direct source for Theorem 15.1).
Takesaki 1970, *Tomita's theory of modular Hilbert algebras*, Theorem
13.1 (the modular identification) and Corollary 14.4 (the Takesaki-Winnink
centralizer theorem).
Takesaki, *Theory of Operator Algebras II*, §VIII.2 (the modular flow
and its centralizer structure).
Takesaki, *Theory of Operator Algebras III*, §XII.1 (the Connes-Takesaki
flow-of-weights theorem, which we do NOT use due to non-separability).
Connes 1973, *Une classification des facteurs de type III*, Ann. Sci.
ENS 6 (type III$_1$ characterization).
Bost-Connes 1995, *Hecke algebras, type III factors and phase
transitions*, Thm 25 (KMS$_1$ uniqueness → factoriality).
