# Appendix E: Comparison with Other Approaches

We compare the Kaluza--Klein approach to the mass gap with the three
most developed alternatives.


## E.1 Lattice Gauge Theory

**Construction.** Replace $\mathbb{R}^4$ with a hypercubic lattice
$\Lambda = (a\mathbb{Z})^4$ of spacing $a$. The gauge field is a group
element $U_\mu(x) \in SU(3)$ on each link. The Wilson action:
$$S_W = \beta \sum_{\text{plaquettes}} \left(1 -
  \frac{1}{3} \text{Re}\,\text{Tr}\,U_P\right)$$

**Mass gap.** At strong coupling ($\beta \ll 1$), the mass gap is proven
(Osterwalder--Seiler 1978): the transfer matrix has spectral gap
$\Delta(a) > 0$ at finite $a$.

**Continuum limit.** The unsolved step. Must show:
1. $\Delta(a) \to \Delta > 0$ as $a \to 0$ (gap survives)
2. The lattice Schwinger functions converge to distributions (regularity)
3. $SO(4)$ invariance is restored (Euclidean covariance)

**Comparison with KK approach:**

| Feature | Lattice | KK |
|---------|---------|-----|
| UV regulation | Lattice spacing $a$ | Compact $\mathbb{CP}^2$ |
| Breaks $SO(4)$? | Yes (hypercubic) | No (exact) |
| Continuum limit needed? | Yes (unsolved) | No (continuum from start) |
| Mass gap proven? | At finite $a$ only | Topologically |
| Non-perturbative? | Yes (numerical) | Yes (topological) |
| Free parameters | $a$, $\beta$ | $r_3$ (fixed by geometry) |


## E.2 Constructive Quantum Field Theory

**Program.** Build the QFT satisfying the Wightman or OS axioms from
scratch, typically via:
1. Regulate (lattice, continuum cutoff)
2. Prove uniform bounds on Schwinger functions
3. Remove regulator, show limits exist
4. Verify axioms for limiting theory

**Successes.** $\phi^4$ in 2D and 3D (Glimm--Jaffe 1968--1987);
Yukawa$_2$ (Seiler 1975); Yang--Mills$_2$ (exact solution).

**Difficulty in 4D.** The theory is at the critical dimension
($d = 4$ is the upper critical dimension for Yang--Mills). The beta
function is logarithmic. Uniform bounds degrade logarithmically with
the cutoff, and controlling the limit requires estimates that are
beyond current technology.

**Comparison with KK approach:**

| Feature | Constructive QFT | KK |
|---------|-----------------|-----|
| Starting point | 4D action | 11D action |
| Regulation | External (cutoff) | Internal (compact space) |
| Symmetry preservation | Difficult | Automatic |
| Strong-coupling control | Main obstacle | Bypassed (topology) |
| Proven in $d < 4$ | Yes | Not applicable |
| Proven in $d = 4$ | No | This paper |


## E.3 AdS/CFT Holography

**Construction.** Realize the gauge theory as the boundary theory of a
gravitational bulk. For confining theories, the bulk geometry caps off
in the IR (e.g., Witten's model: Euclidean black hole in $AdS_5$).

**Mass gap.** The discrete normalizable mode spectrum in the capped
geometry corresponds to the glueball spectrum of the boundary theory.
The gap is the mass of the lightest normalizable mode.

**Limitations.** (1) Pure Yang--Mills on $\mathbb{R}^4$ has no known
exact holographic dual. (2) AdS/CFT requires $\Lambda < 0$. (3)
$\alpha'$ and $g_s$ corrections are not fully controlled.

**Comparison with KK approach:**

| Feature | AdS/CFT | KK |
|---------|---------|-----|
| Extra dimensions | Dual (different theory) | Direct (same theory) |
| Requires duality | Yes | No |
| Cosmological constant | $\Lambda < 0$ required | $\Lambda = 0$ (flat) |
| Applicable to pure YM? | Approximate | Exact |
| Mass gap mechanism | Geometric (IR cap-off) | Topological ($H_2$) |
| Quantitative predictions | Model-dependent | Parameter-free |


## E.4 Summary: Why This Approach Succeeds Where Others Do Not

The three key advantages of the KK approach:

**1. The mass gap is topological, not dynamical.**
In all other approaches, the mass gap arises from non-perturbative
dynamics (instantons, monopoles, flux tubes). Controlling these dynamics
in 4D requires strong-coupling techniques that are not available. In the
KK approach, the mass gap is a property of the topology of
$\mathbb{CP}^2$ --- it does not require controlling any dynamics.

**2. The UV problem is solved by geometry.**
The compactness of $\mathbb{CP}^2$ provides a natural UV regulator
that preserves all symmetries. There is no lattice to remove, no
cutoff to send to infinity, no renormalization group to control.

**3. The construction is explicit.**
The theory is defined by a specific action ($S_{11}$) on a specific
manifold ($M^4 \times \mathbb{CP}^2$). The gauge group, coupling
constant, mass gap, and glueball spectrum all follow from the geometry.
There are no free parameters to tune.
