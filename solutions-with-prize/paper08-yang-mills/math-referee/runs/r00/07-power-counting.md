# 7. Lattice Power Counting

## 7.1 Setup

Let $E_k$ denote the total irrelevant remainder in Balaban's effective
action at RG step $k$ (Section 6.3), with spatial decomposition

$$E_k \;=\; \sum_{x \in \Lambda_k} E_k(x),$$

where $E_k(x)$ is gauge-invariant and supported in a ball of radius
$R_{\mathcal{O}} = O(1)$ (block lattice units) around $x$.  Define

$$\hat{E}_k(q) \;=\; \sum_{x \in \Lambda_k} e^{i q \cdot x}\,E_k(x),
  \qquad q \in \Lambda_k^*.$$


## 7.2 Statement

**Theorem 6 (Lattice power counting, partial).**
*Let $\|E_k\| \leq C g_k^4$ per unit volume.  Then:*

*(a) (Proved.)  The first moment vanishes:*

$$\nabla_q \hat{E}_k(0) \;=\; i \sum_{x \in \Lambda_k} x_\mu\,E_k(x)
  \;=\; 0 \qquad \text{for all } \mu = 1,\dots,4.$$

*(b) (Claimed, with gap.)  The zeroth moment vanishes as an operator
identity:*

$$\hat{E}_k(0) \;=\; \sum_{x \in \Lambda_k} E_k(x) \;=\; 0.$$

*(c) (Conditional on (a) and (b).)  For all $q \in \Lambda_k^*$,*

$$|\hat{E}_k(q)| \;\leq\; C_{\mathrm{Hess}}\,g_k^4\,|q|^2,$$

*where $C_{\mathrm{Hess}}$ is bounded uniformly in $k$.*


## 7.3 Proof of Part (a): Parity Vanishing

The Wilson action has exact parity symmetry $P_\mu : x_\mu \mapsto
-x_\mu$, with $U_\ell \mapsto U_{P_\mu(\ell)}$.

**Step 1.**  Balaban's block-spin commutes with parity.  Under $P_\mu$,
blocks map to blocks ($P_\mu(B)$ is the block centered at $P_\mu(y)$),
and the averaging + $\mathrm{SU}(N)$ projection commutes with $P_\mu$
by Haar-measure invariance.

**Step 2.**  The effective action $S_k$ inherits parity at each RG step
(integration against parity-invariant measure, parity-equivariant map).
Therefore $E_k = S_k - (1/g_k^2)S_{\mathrm{YM}} - \sum_n c_n
\mathcal{O}_n$ is parity-even:

$$E_k(P_\mu(x)) \;=\; E_k(x) \qquad \text{for all } x, \mu.$$

**Step 3.**  The first moment:

$$\sum_{x \in \Lambda_k} x_\mu\,E_k(x)
  \;=\; \sum_{x \in \Lambda_k} x_\mu\,E_k(P_\mu(x))
  \;=\; -\sum_{x' \in \Lambda_k} x'_\mu\,E_k(x')
  \;=\; 0,$$

substituting $x' = P_\mu(x)$ gives $x'_\mu = -x_\mu$ and uses
parity-evenness.  This is an **operator identity**: it holds
configuration by configuration.  $\square$


## 7.4 Part (b): The Vacuum Subtraction -- FALSE as Operator Identity

**Original claim.**  $\hat{E}_k(0) = \sum_{x} E_k(x) = 0$ as an
operator identity (i.e., for every gauge field configuration on
$\Lambda_k$).

**Status: FALSE.**  This identity cannot hold.  Two independent
arguments establish this (see `the-zero-mode-lemma.md` for full
details):

**Argument 1 (from Balaban's construction).**  Balaban's vacuum energy
$\mathcal{E}_0$ is a numerical constant (field-independent).  The
spatial integral $\sum_x E_k(x)[U]$ equals the total irrelevant part
of the effective action evaluated on configuration $U$:

$$\sum_x E_k(x)[U] = S_k[U] - \mathcal{E}_0 V
  - \frac{1}{g_k^2} S_{\mathrm{YM}}[U]$$

This is a nontrivial functional of $U$, generically nonzero for
$U \neq \mathbf{1}$.  Making $\mathcal{E}_0$ field-dependent to force
the identity is a relabeling that shifts the problem into the coupling
renormalization, not a proof.

**Argument 2 (from the block-spin free energy).**  The block-spin
transformation gives:

$$\sum_x E_k(x)[V] = -\ln Z(V) + \ln Z(\mathbf{1})
  - \frac{1}{g_k^2}\bigl[S_{\mathrm{YM}}(V) - S_{\mathrm{YM}}(\mathbf{1})\bigr]$$

At one loop, the remainder after coupling renormalization is the
one-loop determinant ratio $\ln\det(\Delta_V/\Delta_{\mathbf{1}})$,
which is a nontrivial functional of $V$ starting at $O(\mathrm{Tr}\,F^3)$.

**What Balaban DOES provide:**

$$\langle 0 \,|\, \hat{E}_k(0) \,|\, 0 \rangle \;=\; 0$$

The vacuum expectation vanishes (by choice of $\mathcal{E}_0$).  This
is a weaker statement than the operator identity.

**Consequence for the proof.**  The Taylor bound in Part (c) cannot be
established via the operator identity route.  The correct target is the
**matrix element bound** (Conjecture 1 in Section 8):

$$\bigl|\langle 1 \,|\, \hat{E}_k(0) \,|\, 1 \rangle_c\bigr|
  \;\leq\; C\,g_k^4\,\hat{\Delta}^2$$

This does not require $\hat{E}_k(0) = 0$ on every configuration ---
only that the one-particle connected matrix element is suppressed.
At the starting scale ($\hat{\Delta}_0 \sim 1$), this is trivially
satisfied by the cluster expansion.  Propagating it through the RG
requires extending Balaban's framework to three-point functions
(see Section 10 and `the-zero-mode-lemma.md`, Approach 4).


## 7.5 Part (c): Taylor Bound -- Requires New Approach

Since Part (b) is false, the Taylor bound $|\hat{E}_k(q)| \leq
C g_k^4 |q|^2$ **cannot be established** via the operator Fourier
transform route.

Using only Part (a) (the parity vanishing, which IS proved), the
Taylor expansion gives:

$$\hat{E}_k(q) = \hat{E}_k(0) + \tfrac{1}{2}\sum_{\mu,\nu}
  q_\mu q_\nu \partial_{q_\mu}\partial_{q_\nu}\hat{E}_k(\xi)$$

(the linear term vanishes by parity).  The leading term $\hat{E}_k(0)$
is generically nonzero and $O(g_k^4 V)$ in operator norm.  This is
not useful for bounding the form factor.

**The correct path** bypasses the operator Fourier transform entirely
and bounds the **connected matrix element** directly:

$$\bigl|\langle 1|\hat{E}_k(0)|1\rangle_c\bigr|
  \leq C g_k^4 \hat{\Delta}^s \quad \text{for some } s \geq 2$$

This is Conjecture 1 (Section 8).  It is:
- Trivially satisfied at the starting scale ($\hat{\Delta}_0 \sim 1$)
- Proved perturbatively to all orders (Theorem 7)
- Open non-perturbatively (requires extending Balaban to three-point
  functions)

See Sections 8 and 10 for the full discussion.


## 7.6 Summary of Status

| Statement | Status | Method |
|:----------|:-------|:-------|
| (a) $\nabla_q \hat{E}_k(0) = 0$ | **Proved** | Parity symmetry of Wilson action + block-spin |
| (b) $\hat{E}_k(0) = 0$ (operator) | **False** | Disproved: two independent arguments |
| (c) $|\hat{E}_k(q)| \leq C g_k^4 |q|^2$ | **Not provable** via this route | Requires (b), which is false |

Part (a) is a clean symmetry argument that survives.  Part (b) is
definitively false: the spatial integral of $E_k$ is a nontrivial
functional of the gauge field.  Part (c) cannot be established as an
operator norm bound.

**The proof continues via the matrix element bound** (Conjecture 1,
Section 8), which does not require the operator identity.  The key
insight: at the starting scale, $\hat{\Delta}_0 \sim O(1)$ and
the bound is trivially satisfied by the cluster expansion.  The RG
propagation of this bound is the single remaining open problem
(Section 10).
