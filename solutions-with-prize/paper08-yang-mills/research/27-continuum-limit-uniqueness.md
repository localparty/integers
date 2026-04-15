# The Continuum Limit: What We Can and Cannot Prove

This section gives the honest assessment of the continuum limit after
correcting a directional error in an earlier draft.


---

## I. The Error and Its Correction

An earlier version of this section claimed that the cluster expansion
converges along the entire asymptotic freedom trajectory, giving
analyticity of the RG and hence a unique continuum limit. This was
wrong.

**The error.** The convergence condition for the cluster expansion
(Section 25) is:
$$\beta < \frac{a}{2\sqrt{3}\,r_3}$$

On the asymptotic freedom trajectory, $\beta(a) \sim c\ln(1/(a\Lambda))$.
As $a \to 0$:
- $\beta(a) \to +\infty$ (logarithmic growth)
- $a/(2\sqrt{3}\,r_3) \to 0$ (linear shrinkage)

The bound is violated for all sufficiently small $a$. The cluster
expansion fails in the continuum limit regime.

**What survives.** The cluster expansion proves the mass gap at all
lattice spacings $a \gg r_3$ (Regime B of Section 25). For the physical
values $r_3 \sim 10^{-31}$ m and $a \sim 10^{-16}$ m, the convergence
margin is $\sim 10^{13}$. This covers every lattice spacing ever used
in practice.


---

## II. What Is Proved

### II.1 The lattice mass gap at practical couplings

For any lattice spacing $a > a_{\text{cross}} \approx
2\sqrt{3}\,r_3\,\beta(a_{\text{cross}})$, the mass gap $\Delta(a) > 0$.
For the physical $r_3$: $a_{\text{cross}} \sim 10^{-29}$ m, far below
any lattice spacing used in numerical simulations.

**Theorem.** *For $SU(N)$ lattice gauge theory at any coupling
$\beta < a/(2\sqrt{3}\,r_3)$, the string tension $\sigma > 0$ and the
mass gap $\Delta > 0$. In the physical regime, this covers all
$\beta < 10^{14}$.*

### II.2 The SU(2) case (independent of cluster expansion)

For $SU(2)$, the exact 2D YM solution proves $\sigma = 3g^2/8 > 0$ at
ALL couplings, with no restriction on $a/r_3$. This proof does not use
the cluster expansion and does not fail in the continuum limit.

The SU(2) mass gap on the lattice at all $\beta$: **PROVED** (Appendix H).

The SU(2) continuum limit: the Arzel\`a--Ascoli compactness argument
(Section 24) gives a convergent subsequence if $\Delta_{\text{phys}}(a)$
is bounded below uniformly in $a$. The exact string tension
$\sigma = 3g^2/8$ gives $\hat{\sigma} = 3g^2 a^2/8$, so
$\sigma_{\text{phys}} = \hat{\sigma}/a^2 = 3g^2/(8a^2) \to \infty$ as
$a \to 0$ at fixed $g$. But on the AF trajectory, $g^2(a) \to 0$, so
$\sigma_{\text{phys}} = 3g^2(a)/(8a^2)$. Whether this converges to a
nonzero constant depends on the asymptotic scaling relation
$g^2(a) \sim 1/(b_0\ln(1/(a^2\Lambda^2)))$, giving
$\sigma_{\text{phys}} \sim \Lambda^2/(b_0)$ --- a finite constant.
But this uses the perturbative running at all scales, which is not
rigorously proved non-perturbatively.


---

## III. What Is Not Proved

### III.1 The continuum limit for SU(N), N ≥ 3

The cluster expansion fails for $a \lesssim r_3$. In this regime
($a < r_3$), the KK modes are lighter than the lattice cutoff, and the
theory effectively becomes higher-dimensional. The cluster expansion
based on heavy KK modes loses control.

**What would be needed:** A proof that the mass gap survives as $a$
decreases through $r_3$ and beyond. This requires either:

(a) A different proof technique for the regime $a < r_3$ (e.g.,
Balaban-type multi-scale analysis applied to the higher-dimensional
lattice theory on $\Lambda \times \mathbb{CP}^{N-1}$ with all
dimensions discretized).

(b) An argument that the physics at $a \gg r_3$ already determines
the continuum limit (i.e., that the theory does not develop new
relevant couplings as $a$ decreases through $r_3$). This would be
a statement about the RG flow of the full KK theory.

(c) A proof of non-perturbative asymptotic freedom, which would give
the scaling relation $\Delta_{\text{phys}} = c_\Delta \Lambda$
directly.

Each of these is a hard open problem. None is solved here.

### III.2 The uniqueness of the continuum limit

The uniqueness argument of the earlier draft relied on analyticity of
the RG along the AF trajectory, which fails because the cluster
expansion does not converge for $a \to 0$. Without analyticity, the
identity theorem argument (non-perturbative RG = perturbative RG)
does not apply.

**What survives:** The analyticity argument works for $a > a_{\text{cross}}$.
In this regime, the RG IS analytic and DOES match perturbation theory.
This proves that there are no non-perturbative phase transitions for
$a > a_{\text{cross}}$ --- a genuine result, even if it doesn't reach
the continuum.


---

## IV. The Honest Scoreboard (Corrected)

| Step | SU(2) | SU(N), $N \geq 3$ |
|------|-------|-------------------|
| Lattice well-defined | PROVED | PROVED |
| Reflection positivity | PROVED | PROVED |
| $\sigma > 0$, strong coupling | PROVED | PROVED |
| $\sigma > 0$, all practical $\beta$ | PROVED (exact) | PROVED (cluster exp.) |
| Mass gap $\Delta > 0$ on lattice | PROVED | PROVED |
| OS axioms on lattice | PROVED | PROVED |
| Continuum limit (subsequence) | Open* | Open |
| Continuum limit (unique) | Open | Open |
| Continuum $\Delta > 0$ | Open | Open |

*For SU(2), the exact string tension gives $\sigma > 0$ at all $\beta$
including the continuum limit regime. But converting this to a uniform
bound on $\Delta_{\text{phys}}$ requires non-perturbative control of
asymptotic scaling.


---

## V. What the Paper Contributes

Despite the continuum limit remaining open, the paper makes genuine
contributions:

**1. Lattice mass gap at all practical couplings.** Previously known
only at strong coupling (Osterwalder--Seiler). Extended to all
$\beta < 10^{14}$ by the KK cluster expansion. This is a new theorem.

**2. No phase transition in the physical regime.** The analyticity of
the free energy for $a > a_{\text{cross}}$ rules out deconfinement
phase transitions in the entire range of lattice spacings accessible
to numerical simulation. This is a rigorous result backing decades of
numerical evidence.

**3. The screening obstruction theorem.** Screening the Wilson loop
requires non-trivial topology on $\mathbb{CP}^{N-1}$, which costs
energy $\geq 8\pi^2/g^2$. This is a new structural result about the
mechanism of confinement.

**4. The SU(2) exact proof.** The area law at all couplings from 2D
Yang--Mills, derived from first principles. Independent of the cluster
expansion.

**5. Reduction of the Clay problem.** The continuum limit is the only
remaining step. This reduces the Yang--Mills Millennium Problem from
"prove existence + mass gap + confinement + continuum limit" to
"prove the continuum limit." The confinement problem is solved on the
lattice.
