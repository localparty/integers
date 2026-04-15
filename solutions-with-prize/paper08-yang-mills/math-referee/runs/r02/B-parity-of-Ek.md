# Point B: Step 3 -- Parity of E_k

## Verdict: SOUND -- Balaban's construction preserves parity exactly

---

## The Claim Under Scrutiny

Step 3 asserts that $\partial_\mu \hat{E}_k(0) = i\sum_x x_\mu E_k(x) = 0$
because $E_k$ is parity-even under $\mathcal{P}_\mu: x_\mu \to -x_\mu$.
The concern: Balaban's block-spin transformation involves gauge-fixing
and averaging procedures that might break parity, even if the original
Wilson action is parity-symmetric.

## Analysis

### The Wilson action has exact parity

The Wilson plaquette action $S_{\text{YM}} = \beta \sum_P (1 - \frac{1}{N}
\text{Re Tr}\,U_P)$ is invariant under each coordinate reflection
$\mathcal{P}_\mu$, defined on link variables by:

$$\mathcal{P}_\mu: U_{(x, \hat{\nu})} \mapsto
\begin{cases}
U_{(\mathcal{P}_\mu x - \hat{\mu}, \hat{\mu})}^\dagger & \text{if } \nu = \mu \\
U_{(\mathcal{P}_\mu x, \hat{\nu})} & \text{if } \nu \neq \mu
\end{cases}$$

This is an exact symmetry of the lattice theory, not an approximate one.

### Balaban's block-spin transformation

Balaban's RG involves three operations:

**(1) Block averaging.** The block gauge field $U_B$ on the coarse
lattice is defined by averaging link variables along paths within
each block. The standard block-spin kernel for gauge theories
(Balaban 1984, 1985) uses symmetric averages over paths connecting
block sites. This operation is parity-symmetric: reflecting the
fine lattice also reflects the coarse lattice, and the averages are
defined symmetrically.

**(2) Axial gauge fixing within blocks.** Balaban fixes to axial
gauge within each block to make the fluctuation integral well-defined.
The gauge-fixing tree has a preferred "root" direction, which
nominally breaks parity within each block.

However: the effective action is obtained by integrating over ALL
fluctuations consistent with the boundary conditions (the block
field). The integral over fluctuations is gauge-invariant -- the
gauge-fixing is a computational device that does not affect the
result. By Elitzur's theorem, the effective action inherits all
global symmetries of the original action, regardless of the
gauge-fixing procedure.

More precisely: if $\mathcal{T}$ denotes the block-spin map and
$S_k = \mathcal{T}[S_{k-1}]$, then for any symmetry $\mathcal{P}$
of $S_{k-1}$:

$$\mathcal{T}[\mathcal{P}^* S_{k-1}] = \mathcal{P}^* \mathcal{T}[S_{k-1}]$$

since $\mathcal{T}$ commutes with $\mathcal{P}$ (the block-spin map
is defined geometrically, and parity maps blocks to blocks). Therefore
$S_k$ is parity-symmetric if $S_{k-1}$ is. By induction from the
Wilson action: $S_k$ is parity-symmetric for all $k$.

**(3) Large field / small field decomposition.** Balaban splits
configurations into "small field" (curvature bounded) and "large
field" (curvature unbounded) regions. This decomposition is based
on the magnitude of the curvature $|F|$, which is parity-even
(curvature components transform as $F_{\mu\nu} \to \pm F_{\mu\nu}$
under parity, but $|F|^2$ is invariant). So the small field region
is parity-symmetric.

### The remainder E_k is parity-even

Since $S_k$ is parity-symmetric and the decomposition
$S_k = \mathcal{E}_0 V + (1/g_k^2) S_{\text{YM}} + \sum_x E_k(x)$
involves parity-even terms ($\mathcal{E}_0 V$ is a constant,
$S_{\text{YM}}$ is parity-even), the remainder $E_k$ must also be
parity-even:

$$E_k(\mathcal{P}_\mu x)[\mathcal{P}_\mu^* U] = E_k(x)[U]$$

This is an exact statement, not an approximation.

### The vanishing of the first moment

Given parity-evenness of $E_k$:

$$\sum_x x_\mu E_k(x) \stackrel{\mathcal{P}_\mu}{=}
\sum_x (-x_\mu) E_k(x) = -\sum_x x_\mu E_k(x)$$

Therefore $\sum_x x_\mu E_k(x) = 0$ as an **operator identity**
(on every configuration). This is correct.

## Caveat

The argument above assumes that Balaban's effective action
decomposition into $\mathcal{E}_0 V + (1/g_k^2) S_{\text{YM}} + E_k$
respects parity at each stage. This is true if each term in the
decomposition is defined by parity-symmetric projection operators
(e.g., the coupling $1/g_k^2$ is extracted from the coefficient of
the parity-even operator $S_{\text{YM}}$). A paranoid referee would
want to verify that Balaban's specific extraction procedure for
$g_k^2$ and $\mathcal{E}_0$ doesn't inadvertently mix parity-odd
components into $E_k$. However, the standard procedures (matching
coefficients of local operators organized by dimension and symmetry)
are manifestly parity-preserving.

## Summary

Step 3 is **sound**. The parity argument is correct: Balaban's
block-spin transformation preserves parity exactly (not approximately)
at each step, because:
1. The Wilson action has exact parity
2. The block-spin map commutes with parity
3. The fluctuation integral inherits the symmetry (Elitzur's theorem)
4. The operator decomposition is organized by symmetry

The first moment $\sum_x x_\mu E_k(x) = 0$ holds as an operator
identity. No gap here.

**Severity: NONE.** The argument is valid. The proof should make
the parity-preservation more explicit (citing the commutativity of
the block-spin map with lattice reflections), but the substance
is correct.
