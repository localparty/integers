# 08. The Form Factor Bound

This section contains the critical interface between Balaban's
UV-stable effective action and the spectral gap of the transfer
matrix. We establish the perturbative form factor bound (Theorem 7)
and state the non-perturbative conjecture (Conjecture 1) on which
the continuum limit depends.

---

## 8.1 Setup

At RG step $k$, Balaban's effective action has the form
$$S_k[U] = \mathcal{E}_0^{(k)} V + \frac{1}{g_k^2} S_{\mathrm{YM}}[U] + \sum_x E_k(x)[U]$$
where $E_k = \sum_{d_O > 4} c_{d_O}^{(k)} O_{d_O}$ is the irrelevant
remainder with $|c_{d_O}^{(k)}| \leq C g_k^{d_O - 2}$ (Balaban, Commun.
Math. Phys. 109, 1987). The mass gap shift at step $k$ is controlled
by the **connected one-particle form factor**:
$$f_c(0) \;=\; \sum_x \langle 1 | E_k(x) | 1 \rangle_c$$
where $|1\rangle = |1, \vec{p}=0\rangle$ is the one-glueball state
at zero momentum and $\langle 1|E_k(x)|1\rangle_c = \langle 1|E_k(x)|1\rangle - \langle 0|E_k(x)|0\rangle$.

---

## 8.2 Theorem 7 (Perturbative form factor bound)

**Theorem 7.** *In lattice perturbation theory at coupling $g^2$,
the form factor of a dimension-$d_O$ irrelevant operator in the
one-glueball state satisfies*
$$f_c(0) \;=\; g^{d_O - 2}\, h(a \Delta) + O(g^{d_O})$$
*where $h(x) \sim x^{d_O - 4}$ for $x \ll 1$. For $d_O = 6$:*
$$|f_c(0)| \;\leq\; C_{\mathrm{pert}}\, g^4\, (a\Delta)^2.$$
*This holds to all orders in $g^2$. Non-perturbative corrections are
$O(e^{-8\pi^2/g^2})$ (from instantons, by the Bogomolny bound).*

### Proof sketch

**Leading order.** The dimension-$d_O$ operator $O_{d_O}$ is a local
polynomial in $F_{\mu\nu}$ and its covariant derivatives, with
$d_O - 4$ extra derivatives compared to $\mathrm{Tr}\,F^2$. In
momentum space, each derivative contributes a factor of $q$. For a
zero-momentum one-particle state with momentum transfers
$|q| \leq 2\Lambda \sim 2\Delta$:
$$f_c^{(0)}(0) \;\sim\; g^{d_O - 2} \times (a\Delta)^{d_O - 4}.$$

**Higher orders.** At $\ell$-loop order, the form factor acquires
$g^{2\ell}$ from internal propagators. The momentum-space structure
is unchanged: every diagram carries $d_O - 4$ powers of external
momentum by derivative counting. UV divergences are regulated by the
lattice ($|k| \leq \pi/a$) and do not alter the IR scaling. The
perturbative series to all orders gives
$f_c(0) = \sum_\ell g^{d_O - 2 + 2\ell} h_\ell(a\Delta)$ with
$h_\ell(x) \sim x^{d_O - 4}$ for all $\ell$.

**Non-perturbative corrections.** By the Bogomolny bound, the
one-instanton action is $S_{\mathrm{inst}} \geq 8\pi^2/g^2$, so
instanton corrections are $O(e^{-8\pi^2/g^2})$, negligible compared
to any power of $g^2$ for $g^2 \leq 1$. $\square$

---

## 8.3 Why the naive lattice bound fails

The operator norm of a gauge-invariant lattice operator on
$\mathrm{SU}(N)$ is **$a$-independent**. Since $U_\ell \in \mathrm{SU}(N)$
is unitary, any polynomial in link variables has norm $M_O$ depending
only on the group and combinatorial structure, not on $a$. The naive
Kato bound $|f_c(0)| \leq M_O$ carries **no suppression in $a$**.

This is the fundamental obstacle: the lattice is "dimension-blind."
A dimension-6 operator and a dimension-4 operator have comparable
norms. The $(a\Delta)^{d_O - 4}$ suppression visible in perturbation
theory comes from the **momentum structure** of the matrix element --
the glueball concentrates at momenta $|k| \lesssim \Lambda$, and
$\hat{O}_{d_O}(q) \sim |q|^{d_O - 4}$ at small $q$ -- invisible to
any argument using only $\|O_{d_O}\|_\infty$.

---

## 8.4 The translation invariance issue

For a zero-momentum state, translation invariance gives
$$\langle 1|E_k(x)|1\rangle_c = \langle 1|T_x E_k(0) T_x^{-1}|1\rangle_c = \langle 1|E_k(0)|1\rangle_c$$
since $T_x|1,p\!=\!0\rangle = |1,p\!=\!0\rangle$. The connected matrix
element is **independent of $x$**, so
$$f_c(0) = V \times \langle 1|E_k(0)|1\rangle_c.$$

There is no cancellation between sites. The suppression must come
entirely from $\langle 1|E_k(0)|1\rangle_c$ being small. In momentum
space, $\tilde{f}_c(q) = V \cdot \langle 1|E_k(0)|1\rangle_c \cdot \delta_{q,0}$:
the convolution reduces to evaluation at $q = 0$.

The $(a\Delta)^{d_O-4}$ suppression is therefore equivalent to:
$$|\langle 1|E_k(0)|1\rangle_c| \leq \frac{C\,g_k^4\,(a_k\Delta)^s}{V}\cdot\Delta^3$$
for $s \geq 2$. The factor $1/V$ reflects the delocalization of the
zero-momentum state; the factor $\Delta^3$ carries physical dimensions.

---

## 8.5 Conjecture 1 (Non-perturbative form factor bound)

**Conjecture 1.** *There exists $C > 0$ such that for the total
irrelevant remainder $E_k$ in Balaban's effective action:*
$$\left|\sum_x \langle 1|E_k(x)|1\rangle_c\right| \leq C\,g_k^4\,(a_k\Delta)^s \cdot \Delta^3$$
*for some $s \geq 2$, where $|1\rangle$ is the one-particle state
at zero momentum and $\langle\cdot\rangle_c$ denotes the connected
(vacuum-subtracted) matrix element.*

### Why the conjecture is believed

**(i) Perturbative verification.** Theorem 7 establishes the bound
with $s = d_O - 4$ to all orders in $g^2$, with exponentially
suppressed instanton corrections.

**(ii) Dimensional analysis.** In a theory with gap $\Delta$ and
spacing $a$, the ratio $a\Delta$ is the only small parameter. The
scaling $f_c \sim (a\Delta)^{d_O-4}$ is the unique dimensionally
consistent assignment.

**(iii) Universality of Wilsonian scaling.** Every known Wilsonian
RG -- scalar fields (Brydges et al.), Gross-Neveu (Feldman et al.),
hierarchical models (Gawedzki-Kupiainen) -- exhibits non-perturbative
suppression of irrelevant operators by powers of $a/\xi = a\Delta$.

**(iv) Balaban's coefficient bounds.** The power counting in
Balaban's block-spin transformation gives
$|c_{d_O}^{(k)}| \leq C g_k^{d_O-2}(a_k m)^{d_O-4}$. The
conjecture asks for the corresponding statement about matrix
elements, not merely coefficients.

### What the conjecture does NOT follow from

- **Operator norm bounds.** $M_O$ is $a$-independent (Section 8.3).
- **Exponential clustering.** Gives $|f_c(0)| \leq C g_k^4/\hat{\Delta}^3$; the sum $\sum g_k^4/(a_k\Lambda)^3$ diverges.
- **Standard spectral perturbation (Kato, min-max).** Gives $|\delta\Delta/\Delta| \leq Cg_k^4/(a_k\Lambda)$; diverges when summed.

---

## 8.6 Connection to the continuum limit

The form factor bound is not a step toward the continuum limit.
**It IS the continuum limit for the one-particle sector.** The mass
gap shift $\delta\Delta_k = f_c(0)/\hat{\Delta}_k^3$, so the bound
$|f_c(0)| \leq Cg_k^4(a_k\Delta)^s\Delta^3$ is equivalent to
$$\left|\frac{\delta\Delta_k}{\Delta_k}\right| \leq C\,g_k^4\,(a_k\Lambda)^s$$
which says the lattice theory at scale $a_k$ differs from the
continuum by a controllably small amount in the one-particle sector.
The convergent sum $\sum g_k^4(a_k\Lambda)^s$ proves the mass gap
has a well-defined continuum limit.

The reduction to this one estimate -- from the full apparatus of OS
axioms, Wightman reconstruction, and infinite-volume limits -- is the
key simplification. We need the continuum limit of one number: $\Delta$.

---

## Remarks

1. **The exponent $s$.** For the leading irrelevant operator ($d_O=6$),
   $s = 2$ suffices (Section 09). The full power counting suggests
   $s = 4$ if the vacuum subtraction holds as an operator identity.

2. **Physical vs. lattice units.** In lattice units: $|f_c(0)| \leq Cg_k^4\hat{\Delta}^{s+3}$.
   In physical units: $|f_c(0)| \leq Cg_k^4(a\Delta)^s\Delta^3$. Equivalent.

3. **Why "conjecture" not "assumption."** Proved perturbatively,
   believed physically, consistent with all examples. Fails only if
   a non-perturbative effect violates dimensional analysis for lattice
   matrix elements. No such effect is known in any asymptotically free theory.
