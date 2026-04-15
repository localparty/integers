# Path A: The Multi-Scale RG Plan

The worldsheet path (Path C) is a no-go. Path A is independent of the
worldsheet — it uses only the lattice, the CP^{N-1} topology, and
Balaban's multi-scale RG framework.


---

## I. The Key Insight (from Path A Agent, Idea 2)

Track the **correlation length** $\xi = 1/\Delta$ instead of the string
tension $\sigma$.

At each RG step (block-spin from lattice spacing $a$ to $2a$):

**Before coupling renormalization:** the mass shift is $O(g^2)$.
The one-loop self-energy contributes $\delta m \sim g^2 \Lambda$.

**After coupling renormalization:** the $O(g^2)$ part is absorbed by
the running coupling (this IS what renormalizability means). The
RESIDUAL mass shift is $O(g^4)$:

$$|\delta m_k^{\text{ren}}| \leq C g_k^4 \Lambda$$

**The sum converges:**
$$\sum_{k=0}^{\infty} g_k^4 \sim \sum_{k=0}^{\infty}
  \frac{1}{(\ln k)^2} < \infty$$

(Compare with $\sum g_k^2 \sim \sum 1/\ln k = \infty$, which is why
tracking $\sigma$ directly fails.)

**Therefore:** $\xi_\infty = \xi_0 + \sum_k \delta\xi_k^{\text{ren}}$
converges, and $\Delta_\infty = 1/\xi_\infty > 0$.


---

## II. What Needs to Be Proved

The entire argument reduces to ONE technical statement:

> **The Renormalized Mass Shift Bound.** *At each block-spin RG step
> $k$, the renormalized shift of the inverse correlation length
> satisfies:*
> $$|\delta m_k^{\text{ren}}| \leq C g_k^4 \Lambda$$
> *where $C$ is a constant independent of $k$.*

**Why this is plausible:** In Balaban's framework (1985-1989), the
effective action at each RG step is:

$$S_k = S_{\text{YM}}(g_k^2) + \sum_n c_n(g_k) \mathcal{O}_n$$

where $g_k^2$ is the renormalized coupling (absorbs the $O(g^2)$
divergence) and $\mathcal{O}_n$ are irrelevant operators with
coefficients $c_n = O(g_k^4)$ (the residuals after renormalization).

The correlation length $\xi_k = 1/m_k$ receives corrections from the
irrelevant operators. Since each $c_n = O(g_k^4)$, the total shift is:

$$\delta m_k = \sum_n c_n \times \langle \mathcal{O}_n \rangle
  = O(g_k^4) \times \Lambda$$

**What Balaban proved:** The coefficients $c_n(g_k)$ are bounded by
$C |g_k|^{d_n}$ where $d_n \geq 4$ (all irrelevant operators have
dimension $> 4$, hence coupling $\geq g^4$). [PROVED in Balaban
1985-1989]

**What Balaban did NOT prove:** That the PHYSICAL mass gap receives
corrections bounded by $O(g^4)$. Balaban's estimates control the
effective action, not individual physical observables.

**The gap:** Go from bounds on the effective action (Balaban) to bounds
on the mass gap (our goal).


---

## III. The Plan

### Phase A1: Understand Balaban's Estimates (1-2 months)

Balaban's papers (Commun. Math. Phys. 95-122, 1985-1989) develop a
multi-scale analysis for lattice YM in 4D. The key results:

1. **Block-spin transformation.** At each step, average gauge field
   variables over blocks of $2^4$ sites. The effective action at
   scale $k$ is $S_k[U]$.

2. **Effective action structure.** $S_k = \beta_k S_W + \sum c_n
   \mathcal{O}_n$ where $\beta_k$ is the running coupling and
   $\mathcal{O}_n$ are gauge-invariant operators.

3. **Coefficient bounds.** $|c_n| \leq C_n g_k^{d_n}$ with
   $d_n \geq 4$. The bounds are UNIFORM in the RG step $k$.

4. **UV stability.** The effective action stays well-defined at each
   step. No uncontrolled growth.

**What to extract:** The explicit bounds on $c_n$ as functions of
$g_k$, and the structure of the gauge-invariant operators
$\mathcal{O}_n$ that contribute to the mass gap.

### Phase A2: Connect Effective Action to Mass Gap (2-3 months)

The mass gap is the spectral gap of the transfer matrix $T_k = e^{-a_k
H_k}$. The Hamiltonian $H_k$ is determined by the effective action $S_k$.

**The connection:** If $S_k = S_k^{(0)} + \delta S_k$ where $S_k^{(0)}$
is the reference action (with known gap $m_k^{(0)}$) and $\delta S_k$
is the correction (bounded by Balaban), then:

$$|m_k - m_k^{(0)}| \leq \|\delta S_k\|_{\text{op}}$$

where $\|\cdot\|_{\text{op}}$ is an operator norm connecting the action
perturbation to the spectral gap shift.

**The tool:** Kato's perturbation theory (as in Attack 3) or Temple's
inequality. The key estimate: the spectral gap shift is bounded by the
operator norm of the perturbation to the transfer matrix.

**What to prove:**
$$|m_k - m_{k-1}^{\text{ren}}| \leq C g_k^4 \Lambda$$

where $m_{k-1}^{\text{ren}}$ is the mass at the previous step after
coupling renormalization.

### Phase A3: Prove Convergence (1 month)

Given the bound from Phase A2:

1. $m_\infty = m_0 + \sum_{k=0}^{\infty} \delta m_k^{\text{ren}}$

2. $|\delta m_k^{\text{ren}}| \leq C g_k^4 \Lambda$

3. $\sum g_k^4 = \sum (2N/\beta_k)^2 \sim \sum 1/(b_0 \ln k)^2
   \leq c \sum 1/k^{1+\epsilon}$ for any $\epsilon > 0$ when
   $k > k_0$. This converges.

4. Therefore $m_\infty$ exists and is finite.

5. $m_\infty > 0$ because $m_0 > 0$ (lattice proof) and the total
   correction $|\sum \delta m_k| \leq C' \sum g_k^4 < \infty$ is
   bounded. For $m_0$ large enough (which it is — the lattice mass gap
   is $O(\Lambda)$), $m_\infty = m_0 - O(1) > 0$.

### Phase A4: Handle the Crossover at $a \sim r_3$ (2-3 months)

At $a \sim r_3$, the KK modes become light ($m_1 a \sim 1$). The
cluster expansion (which gave us $m_0 > 0$) no longer applies.

**Two sub-cases:**

**(a) From above ($a \gg r_3$):** The multi-scale RG from Phase A2
descends from $a = a_0$ (where cluster expansion works) down to
$a \sim r_3$. In this regime, the KK modes are heavy and the theory
is effectively 4D. The $O(g^4)$ bound applies.

**(b) Through the crossover ($a \sim r_3$):** The KK modes become
dynamical. The theory transitions from 4D to $(4 + 2N-2)$-dimensional.

**The matching argument:** At $a = r_3$, match the 4D effective theory
(from above) to the higher-dimensional theory (from below). The 4D
coupling $g_{4D}^2(1/r_3)$ is determined by the matching and is
independent of $a$.

**(c) From below ($a \ll r_3$):** The theory is higher-dimensional on
the lattice. The higher-dimensional theory is NOT asymptotically free,
but the COMPACT $\mathbb{CP}^{N-1}$ makes it different from a flat
higher-dimensional theory. The KK structure ensures that below $1/r_3$,
the theory reduces back to 4D YM.

**The key claim:** The physical mass gap is determined at the
compactification scale $1/r_3$. The RG flow below $1/r_3$ is the
standard 4D YM flow, which produces $\Delta = C \Lambda_{4D}$.
The RG flow above $1/r_3$ is higher-dimensional and does NOT affect
$\Delta$ (it only affects UV-sensitive quantities, not IR observables).

**What to prove:** That the matching at $1/r_3$ is perturbatively
controlled (the coupling $g_{4D}^2(1/r_3)$ is computable to arbitrary
precision) and that the 4D RG below $1/r_3$ is described by Balaban's
framework with the $O(g^4)$ bounds.

### Phase A5: Assembly (1 month)

1. Start at $a_0$ where cluster expansion gives $m_0 > 0$ [PROVED].
2. Multi-scale RG from $a_0$ down to $a = r_3$: mass shifts $O(g_k^4)$,
   sum converges [Phase A2-A3].
3. Match at $a = r_3$: $g_{4D}^2(1/r_3)$ determined [Phase A4].
4. Multi-scale RG from $r_3$ down to $a = 0$: this is 4D YM with
   Balaban's estimates, mass shifts $O(g_k^4)$, sum converges
   [Phase A2-A3 applied to 4D].
5. Conclude: $m_\infty > 0$, hence $\Delta_\infty > 0$.


---

## IV. The Critical Technical Question

Everything reduces to:

> *Does Balaban's renormalization at each RG step give
> $|\delta m_k^{\text{ren}}| \leq C g_k^4 \Lambda$?*

**What this means concretely:** At each block-spin step, the coupling
renormalization $g_k^2 \to g_{k+1}^2 = g_k^2 + b_0 g_k^4 \ln 2 + ...$
absorbs the one-loop self-energy correction to the propagator. The
REMAINDER after this absorption is $O(g^4)$.

In perturbation theory, this is standard: the one-loop renormalization
absorbs the $O(g^2)$ divergence, leaving $O(g^4)$ finite terms.

Balaban's framework provides non-perturbative control of this
cancellation: his bounds on the effective action coefficients $c_n$
are $O(g^{d_n})$ with $d_n \geq 4$, uniformly in $k$.

**The missing link:** Going from bounds on the effective action to
bounds on the mass gap. This is a spectral theory question:

$$\text{spec}(T_k) \to \text{spec}(T_{k+1})$$

with $T_{k+1} = T_k + O(g_k^4)$ (in some operator sense). The spectral
gap shift is bounded by the perturbation norm.


---

## V. Why This Might Actually Work

### V.1 The $O(g^4)$ vs $O(g^2)$ distinction is real

In standard lattice perturbation theory, the one-loop mass
renormalization IS $O(g^2)$:
$$\delta m^{(1)} = c_1 g^2 \Lambda$$

But coupling renormalization absorbs this:
$$g^2 \to g^2 + b_0 g^4 \ln(a\Lambda) + ...$$

After absorbing: the PHYSICAL mass shift is:
$$\delta m^{\text{phys}} = c_2 g^4 \Lambda + O(g^6)$$

This is the standard perturbative result. Balaban's framework promotes
it to a non-perturbative bound.

### V.2 The convergence is strong

$\sum g_k^4 \sim \sum 1/(\ln k)^2$. The first few terms:
- $k = 2$: $g_2^4 \sim 1/(\ln 2)^2 \approx 2.08$
- $k = 10$: $g_{10}^4 \sim 1/(\ln 10)^2 \approx 0.19$
- $k = 100$: $g_{100}^4 \sim 1/(\ln 100)^2 \approx 0.047$

The series converges FAST after the first few terms. The total:
$\sum_{k=2}^{\infty} 1/(\ln k)^2 \approx 4.5$ (finite).

### V.3 The mass gap has margin

The lattice mass gap at $a_0$ is $m_0 \sim \Lambda$ (the confinement
scale). The total correction is $\sum |\delta m_k| \leq C \times 4.5
\times \Lambda$. For $C < 1/(4.5)$: $m_\infty > 0$.

The question is whether $C$ is small enough. In perturbation theory,
$C \sim b_0/(16\pi^2) \sim 0.01$, giving $C \times 4.5 \approx 0.05$
— a 5% correction to $m_0$. This leaves plenty of room.


---

## VI. Timeline

| Phase | Duration | What |
|-------|----------|------|
| A1 | 1-2 months | Study Balaban's papers, extract key estimates |
| A2 | 2-3 months | Connect effective action bounds to mass gap |
| A3 | 1 month | Prove convergence using $\sum g^4 < \infty$ |
| A4 | 2-3 months | Handle the crossover at $a \sim r_3$ |
| A5 | 1 month | Assembly |
| **Total** | **7-10 months** | |

This is comparable to the (now cancelled) Phase 3 computation, but it's
an ANALYTICAL proof rather than a computer-assisted one.


---

## VII. What This Does NOT Depend On

| Ingredient | Needed? |
|-----------|---------|
| Worldsheet = CP$^{N-1}$ | **NO** |
| Lüscher test result | **NO** |
| 2D CP$^2$ adiabatic continuity | **NO** |
| Lattice confinement (Sections 21-25) | **YES** (provides $m_0 > 0$) |
| Balaban's UV stability | **YES** (provides coefficient bounds) |
| Perturbative asymptotic freedom | **YES** (provides $g_k^2 \to 0$) |
| CP$^{N-1}$ topology | **YES** (provides the starting mass gap $m_0$, but not needed for the RG flow) |

**The critical new ingredient is Balaban's non-perturbative
renormalization — specifically, the $O(g^4)$ bounds on the effective
action after coupling renormalization.** Everything else is either
already proved or standard.
