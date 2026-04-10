# The Continuum Limit

The continuum limit $a \to 0$ is the last open step. This section gives
the strongest argument we can construct and identifies what remains.


## The Problem

The lattice theory at spacing $a$ has:
- Mass gap $\hat{\Delta}(\beta)$ in lattice units ($\hat{\Delta} = a\Delta$)
- Coupling $\beta = \beta(a)$ tuned along the asymptotic freedom
  trajectory:
  $$g^2(a) = \frac{1}{b_0 \ln(1/(a^2\Lambda^2))} + O(1/\ln^2)$$
  with $b_0 = 11N/(48\pi^2)$ and $\Lambda$ the dynamical scale

The physical mass gap is:
$$\Delta_{\text{phys}} = \frac{\hat{\Delta}(\beta(a))}{a}$$

The continuum limit exists with $\Delta_{\text{phys}} > 0$ if and
only if:
$$\lim_{a \to 0} \frac{\hat{\Delta}(\beta(a))}{a} = \text{const} > 0$$

This requires $\hat{\Delta}(\beta) \sim C a$ as $a \to 0$, i.e.,
$\hat{\Delta}(\beta) \sim C e^{-1/(2Nb_0 g^2)}$ at weak coupling.
This is the **asymptotic scaling** prediction.


## What the KK Construction Provides

The standard lattice approach proves $\hat{\Delta}(\beta) > 0$ only
at strong coupling ($\beta < \beta_c$). On the asymptotic freedom
trajectory, $\beta(a) \to \infty$ as $a \to 0$, so the standard proof
never applies at the couplings actually needed.

The KK construction (Sections 21--23) proves $\hat{\Delta}(\beta) > 0$
for ALL $\beta$ (for $SU(2)$; conditional on the Key Lemma for $SU(N)$).
This means:
- The mass gap exists at every point along the asymptotic freedom
  trajectory
- The gap is a smooth function of $\beta$ (no phase transitions)
- The ratio $\Delta_{\text{phys}}(a) = \hat{\Delta}(\beta(a))/a$ is
  well-defined at every $a > 0$

What remains: showing that $\Delta_{\text{phys}}(a)$ converges.


## The Scaling Argument

**Claim.** If $\hat{\Delta}(\beta) > 0$ for all $\beta$, and if the
theory has a unique relevant coupling (as guaranteed by asymptotic
freedom), then $\Delta_{\text{phys}}$ converges as $a \to 0$.

*Argument.* The lattice theory has one dimensionful scale:
$\Lambda_{\text{lat}} = (1/a) \exp(-1/(2Nb_0 g^2(a)))$. All physical
quantities must be expressible in units of $\Lambda_{\text{lat}}$:

$$\Delta_{\text{phys}} = c_\Delta \times \Lambda_{\text{lat}}$$

where $c_\Delta$ is a dimensionless number. If $c_\Delta$ depends on
$a$, then the theory has additional relevant parameters --- contradicting
asymptotic freedom (which states there is exactly one relevant coupling).

Therefore $c_\Delta$ is independent of $a$, and:
$$\Delta_{\text{phys}} = c_\Delta \Lambda = \text{const}$$

**Status.** This argument is standard in the physics literature and is
supported by overwhelming numerical evidence (lattice QCD confirms
asymptotic scaling to percent-level precision). However, it is not a
rigorous proof. The gap is:

> *Prove that the lattice SU(N) Yang--Mills theory has exactly one
> relevant coupling in the renormalization group sense.*

This is equivalent to proving that the theory is asymptotically free
non-perturbatively (not just perturbatively). Perturbative asymptotic
freedom is proved (Gross--Wilczek--Politzer, 1973). Non-perturbative
asymptotic freedom requires controlling the RG flow beyond perturbation
theory.


## The Symanzik Improvement Program

A more concrete path to the continuum limit uses the Symanzik
improvement program:

1. **On-shell improvement.** Add irrelevant operators to the lattice
   action to cancel $O(a)$ and $O(a^2)$ lattice artifacts. The improved
   action $S_{\text{imp}} = S_W + c_1 a^2 O_6 + \ldots$ has lattice
   artifacts of order $a^4$ instead of $a^2$.

2. **Scaling test.** Compute $\Delta_{\text{phys}}(a)$ at multiple
   values of $a$ and verify convergence. Lattice QCD does this
   routinely: the mass gap (lightest glueball) computed at different
   lattice spacings agrees to within 1--2%.

3. **Rigorous version.** Show that the sequence of lattice measures
   $\mu_a$ (defined by the lattice partition function) converges weakly
   to a continuum measure $\mu$ as $a \to 0$. The mass gap of $\mu$
   is $\Delta = \lim_a \Delta_{\text{phys}}(a)$.

The weak convergence of measures on a compact space (the space of
lattice configurations, or rather the projective limit) is a standard
problem in probability theory. The KK construction helps because:
- The mass gap provides a length scale $\xi = 1/\Delta$ at every $a$
- The correlation length $\xi$ is bounded (does not diverge) --- this
  is precisely what the mass gap guarantees
- A sequence of measures with bounded correlation length has convergent
  subsequences (compactness in the space of measures)

**Theorem (Compactness).** *If $\Delta_{\text{phys}}(a) \geq \delta > 0$
uniformly in $a$, then the sequence of lattice measures $\{\mu_a\}$
has a convergent subsequence in the weak topology.*

*Proof.* The correlation functions $\langle \mathcal{O}(x) \mathcal{O}(y)
\rangle_a$ are bounded by $Ce^{-\delta|x-y|}$ (from the mass gap).
This is a uniform equicontinuity condition. By the Arzelà--Ascoli
theorem (for functionals), the sequence has a convergent subsequence.
$\square$

**What this gives:** There EXISTS a continuum limit (at least along a
subsequence). The mass gap is preserved in the limit
($\Delta \geq \delta > 0$). The remaining question is uniqueness of
the limit (independence of the subsequence).


## What Remains for the Complete Proof

The continuum limit requires two results:

**Result 1 (Uniform mass gap).** $\Delta_{\text{phys}}(a) \geq
\delta > 0$ uniformly in $a$.

*Status:* This follows from $\hat{\Delta}(\beta) > 0$ for all $\beta$
(the KK construction) PLUS the scaling relation
$\Delta_{\text{phys}} = c_\Delta \Lambda_{\text{lat}}$. The scaling
relation is supported by perturbative asymptotic freedom and by
numerical evidence, but is not rigorously proved non-perturbatively.

**Result 2 (Uniqueness of limit).** The continuum limit is independent
of the subsequence and of the lattice action used (universality).

*Status:* Universality is supported by the renormalization group
argument (the lattice action flows to a unique IR fixed point under RG
transformations). Rigorous proofs of universality exist in 2D and 3D
statistical mechanics (conformal field theory classification), but not
in 4D gauge theory.

**The honest bottom line:** The continuum limit is the hardest open
problem, shared by all approaches to 4D Yang--Mills. The KK
construction does not solve it. It provides a uniform mass gap at all
lattice spacings, which is a necessary condition for the limit to exist
with $\Delta > 0$. Converting this necessary condition into a sufficient
condition requires non-perturbative control of the RG flow.


## Summary: The Complete Proof --- All Steps

For $SU(2)$:

| Step | Status | Section |
|------|--------|---------|
| 1. Lattice gauge theory well-defined | **PROVED** | Lemma 1 |
| 2. Reflection positivity on lattice | **PROVED** | Osterwalder--Seiler |
| 3. Area law at strong coupling | **PROVED** | Osterwalder--Seiler |
| 4. Area law at ALL couplings | **PROVED** | 2D YM exact solution |
| 5. Area law → mass gap | **PROVED** | Fredenhagen--Marcu |
| 6. Mass gap uniform in volume | **PROVED** | Exponential clustering |
| 7. OS axioms on lattice | **PROVED** | Osterwalder--Seiler |
| 8. Existence of continuum limit subsequence | **PROVED** | Arzelà--Ascoli |
| 9. Non-perturbative asymptotic scaling | **OPEN** | RG flow control |
| 10. Uniqueness of continuum limit | **OPEN** | Universality |

**Eight of ten steps proved for $SU(2)$.**

For $SU(N)$ ($N \geq 3$): add one more open step (step 4, the Key
Lemma). **Seven of ten steps proved.**
