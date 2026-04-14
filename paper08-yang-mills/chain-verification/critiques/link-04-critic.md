# Link 4 Critic verdict

**Target:** (B1): analyticity of polymer activities, k-independent radius
**Source:** preprint/sections/H-balaban-analyticity.md; nodes/05-analyticity.md
**Verdict:** WEAKENED
**Confidence:** 7/10

---

## Attacks attempted

### Vector 1: Does "finitely many" operations bound grow with k?

Result: *bounced.* The composition at each RG step involves exactly four operations
(background evaluation, saddle-point, Gaussian integration, Mayer resummation),
independent of k. The Mayer resummation sums over polymers, but analyticity of that
sum follows from the Weierstrass theorem (uniform limit of analytic functions is
analytic) using the exponential decay bound — not from bounding the number of terms.
The "finite" in "finitely many" refers to the four operations, not the number of
polymers; no k-dependent growth. Attack fails.

### Vector 2: Radius = min of radii — does the composition formula apply cleanly?

Result: *exposes a gap.* (See main finding below.) The standard composition lemma
requires that the **image** of the ball $B(V_0, r_n)$ under the $n$-th operation lies
**strictly inside** the domain of the $(n+1)$-th operation — both in size (radius
condition) and position (center condition). The Run 3 repair provides a Lipschitz
bound on $G_k(V)$ to handle the size, but does not verify the **center condition**:
that the saddle-point output $u_{\mathrm{cl}}[V] = -G_k(V) \cdot \nabla_u S_{k-1}|_{u=0}$
lies in the cluster-expansion domain required by the Mayer step. The polymer decay
bound $\|K_k\| \leq e^{-\kappa|X|}$ bounds magnitudes on the boundary of the Mayer
domain but does not confirm the center lies strictly inside it. This leaves the
composition domain-tracking incomplete at the saddle-point → Gaussian interface.

### Vector 3: CMP 95 Prop 1.2 — is δ₀ background-dependent?

Result: *bounced.* The fluctuation propagator is $G_k(V) = (-D^2[V] + m_W^2)^{-1}$
where $m_W^2$ is a **fixed** infrared regulator (added by hand, not a dynamical mass).
Since $-D^2[V] \geq 0$ as a self-adjoint operator, $S_k^{(2)}[V] \geq m_W^2 > 0$
uniformly in $V \in \Omega_s$. The exponential decay rate $m_W$ is therefore
background-independent; it is the infrared regulator, not an eigenvalue of $D^2[V]$.
The preprint's formula $|G_k(x,y;V)| \leq Ce^{-m_W|x-y|}$ is correct and $m_W$ does
not depend on $V$. Attack fails.

### Vector 4: Saddle-point stability radius — k-dependent shrinkage?

Result: *bounced, but the justification in the text is incomplete.* The concern is that
the perturbation of $S_k^{(2)}$ by $\delta V_\ell$ involves the covariant Laplacian,
which carries an $a_k^{-2}$ prefactor (finite difference), so $\|\delta S_k^{(2)}\|
\sim a_k^{-2}\|\delta V\|$. The invertibility condition requires this to be $< m_W^2
\sim a_k^{-2}$, giving $\|\delta V\| < c$ — dimensionless and k-independent. So the
saddle-point radius **is** k-independent when stated correctly. However, Node 05 writes
"controlled by $m_W^2 \sim 1/a_k^2$, $k$-independent condition" without explaining
that both sides of the invertibility inequality scale identically as $a_k^{-2}$,
canceling the k-dependence. The conclusion is correct but the text is compressed to
the point of being unverifiable without this calculation. This is not a gap but a
presentation weakness.

### Vector 5: Dimock scalar-to-non-abelian transfer

Result: *bounced.* Dimock (2011, 2013) is cited only as supplementary — a "modern
exposition" for the analyticity mechanism in the scalar case. The primary sources for
the non-abelian gauge theory are Balaban CMP 95–96 (propagator), CMP 98 (kernel),
CMP 109 (inductive construction). The scalar analogy does not need to transfer; it
is illustrative only. The primary chain relies on CMP 95–109 throughout, not on
Dimock. Attack fails.

---

## Main finding: WEAKENED

**The gap:** The Run 3 repair for Node 05's domain-tracking weakness added the Lipschitz
bound $\|G_k(V) - G_k(V_0)\| \leq C\|V - V_0\|$ (with $C$ k-independent) and the
polymer decay bound $\|K_k\| \leq e^{-\kappa|X|}$ to justify that "the image of each
operation at radius $r_n$ lies within the domain of the next operation at radius
$r_{n+1}$." The radius (size) condition is handled by these bounds. The **center
condition** — that the base point of the image ball (the saddle-point value
$u_{\mathrm{cl}}[V_0]$ at the background $V_0$) lies strictly inside the Mayer
cluster-expansion domain, not merely near its boundary — is not verified in the repair.

This is not fatal: Balaban CMP 109, Section 3 formulates the inductive hypotheses for
the block-field at each scale, and one of these hypotheses asserts that the background
$V$ satisfies the small-field condition $|F_{\mu\nu}[V]| < p(g_k)$, which precisely
controls the size of $u_{\mathrm{cl}}[V_0]$ and places it well inside the Mayer domain.
The repair should invoke this hypothesis explicitly rather than relying on the magnitude
of $K_k$ at the boundary.

**Repair path:** Add one sentence to Node 05 Step 2: "The center condition — that
$u_{\mathrm{cl}}[V_0]$ lies in the Mayer domain — follows from the small-field
inductive hypothesis of CMP 109 §3: $|F_{\mu\nu}[V]| < p(g_k)$ bounds the saddle-point
size by $\|u_{\mathrm{cl}}\| \leq C_0 g_k^{1-\epsilon} a_k$, which lies well inside the
cluster-expansion domain (radius $\sim \kappa/(\beta \cdot \mathrm{poly}(N))$ by
Cauchy estimates on the Mayer sum)."

---

## Status

**WEAKENED.** One repairable gap: center condition in composition domain tracking not
explicitly cited. Repair is a one-sentence citation of CMP 109 §3 inductive hypotheses.
No fatal attack survived.
