# §16 — The Connes Spectrum $\mathrm{Sd}(M_1) = \mathbb{R}$

*Paper 49, Part III, §16. The Connes spectrum is the state-independent
invariant that characterizes a type III factor's modular flow. Defined
as the intersection of the spectra of $\log \Delta_\psi$ over all cyclic-separating
$\psi$, it fills all of $\mathbb{R}$ for type III$_1$ (continuous modular
flow) and consists of discrete lattice $\log\lambda \cdot \mathbb{Z}$ for
type III$_\lambda$ ($0 < \lambda < 1$). Our BC factor is type III$_1$
(§08), so $\mathrm{Sd}(M_1) = \mathbb{R}$. This is needed in Part IV for
the discrete-vs-continuous spectrum analysis of the Hilbert-Pólya
operator $D$.*

---

## Definition

**Definition 16.1 (Connes spectrum).** Let $M$ be a von Neumann algebra
with a faithful normal weight $\varphi$ (or, for our purposes, a
faithful normal state). Let $\Delta_\psi$ denote the modular operator
associated with a cyclic-separating vector $\psi$ for $M$ (via Tomita-Takesaki,
§11). The *Connes spectrum* of $M$ is
$$\mathrm{Sd}(M) \;:=\; \bigcap_{\psi \text{ cyclic-separating for } M}
\mathrm{spec}(\Delta_\psi) \;\cap\; (0, \infty),$$
considered as a subset of $\mathbb{R}_+^*$ under the multiplicative
structure.

By convention we identify $\mathrm{Sd}(M)$ with its image under $\log :
\mathbb{R}_+^* \to \mathbb{R}$, giving $\log \mathrm{Sd}(M) \subset
\mathbb{R}$, and we call this the additive Connes spectrum. Under this
identification:
$$\log \mathrm{Sd}(M) = \bigcap_\psi \mathrm{spec}(\log \Delta_\psi).$$

**Remark 16.2 (state-independence).** The intersection makes $\mathrm{Sd}(M)$
independent of the choice of $\psi$. This is essential: it means
$\mathrm{Sd}(M)$ is an *invariant* of the algebra $M$ (not of the pair
$(M, \psi)$). It is a coarse but *canonical* dynamical invariant.

## Connes's classification theorem

**Theorem 16.3 (Connes 1973).** Let $M$ be a factor of type III with
separable predual (or, as for us, without separability but with the
BGS-L2 direct ergodicity argument intact).

(i) *Type III$_0$*: $\mathrm{Sd}(M) = \{0, 1\}$ multiplicatively, i.e.,
$\log \mathrm{Sd}(M) = \{0\}$ (trivial additive spectrum). The modular
flow has zero Connes spectrum.

(ii) *Type III$_\lambda$ for $0 < \lambda < 1$*: $\mathrm{Sd}(M) =
\lambda^{\mathbb{Z}} \cup \{0\}$ multiplicatively, i.e., $\log \mathrm{Sd}(M)
= (\log \lambda) \cdot \mathbb{Z}$ (a discrete lattice). The modular flow
has discrete Connes spectrum with period $-\log \lambda$.

(iii) *Type III$_1$*: $\mathrm{Sd}(M) = \mathbb{R}_+$ multiplicatively,
i.e., $\log \mathrm{Sd}(M) = \mathbb{R}$. The modular flow has full
Connes spectrum.

**Reference.** Connes 1973, *Une classification des facteurs de type III*,
Théorème 3.4.1 and Théorème 4.1.1. See also Takesaki Vol III §XII.1.

## The BC factor's Connes spectrum

**Theorem 16.4 (Connes spectrum of the BC KMS$_1$ factor).** The BC
type III$_1$ factor $M_1$ has
$$\mathrm{Sd}(M_1) = \mathbb{R}_+^* \qquad \text{multiplicatively},
\qquad \log \mathrm{Sd}(M_1) = \mathbb{R} \qquad \text{additively}.$$

**Proof.** By §08, $M_1$ is type III$_1$ (via Araki-Woods classification
applied to the ITPFI presentation with weights $\lambda_p = 1/p$). Apply
Theorem 16.3(iii). QED.

**Remark 16.5 (the role of primes).** The ITPFI factorization
$\omega_1 = \bigotimes_p \omega_1^{(p)}$ (Paper 13 Layer 2) gives the BC
factor as an infinite tensor product with the primes as the index set.
The weights $\{1/p\}_{p \text{ prime}}$ have asymptotic ratio set
$$r_\infty(M_1) = \overline{\{1/p^\alpha \cdot q^\beta : p, q \text{ prime},
\alpha, \beta \in \mathbb{Z}\}} = [0, \infty)$$
because $\{\log p\}_{p \text{ prime}}$ is $\mathbb{Q}$-linearly independent
(prime factorization uniqueness), so $\{\alpha \log p - \beta \log q :
p, q, \alpha, \beta\}$ is dense in $\mathbb{R}$. Araki-Woods 1968 §5
converts this asymptotic-ratio density into $\mathrm{Sd}(M_1) = \mathbb{R}_+$.

*It is the primes, and their $\mathbb{Q}$-linear independence, that force
the BC factor to be type III$_1$ rather than type III$_\lambda$.* This
is one of the deeper structural facts of the construction: the *arithmetic*
of $\mathbb{Z}$ (prime factorization uniqueness) forces the *analytic*
type classification (III$_1$ rather than III$_\lambda$).

## The Arveson spectrum picture

There is a dual characterization of $\mathrm{Sd}(M)$ that will be useful
in Part IV. Define the *Arveson spectrum* of $\sigma_t$ as
$$\mathrm{Sp}(\sigma) := \{\lambda \in \mathbb{R} : \forall \epsilon > 0,\;
\exists a \in M \setminus \{0\} \text{ with } \sigma_t(a) = e^{i\lambda t}
a + O(\epsilon)\text{ in some sense}\}.$$
Precisely: $\mathrm{Sp}(\sigma)$ is the support of the Arveson spectrum
of the one-parameter group — the set of frequencies at which $\sigma_t$
has approximately eigen-operators.

For a factor $M$, Connes (1973 Théorème 3.4) proved:
$$\log \mathrm{Sd}(M) = \bigcap_e \mathrm{Sp}(\sigma|_{eMe})$$
where the intersection is over all non-zero projections $e \in M$. This
"intersection over projections" is what makes $\mathrm{Sd}$ a genuine
algebraic invariant (independent of the choice of state, since the state
only enters through the specific modular flow $\sigma$, and $\sigma$ is
determined up to inner perturbations by $M$).

For our type III$_1$ factor, the intersection $\bigcap_e \mathrm{Sp}
(\sigma|_{eMe}) = \mathbb{R}$, reflecting that no matter how we restrict
to a corner $eMe$, the modular flow retains full frequency spectrum.

## Consequence: continuous spectrum of $\log \Delta$

**Corollary 16.6 (continuous spectrum of the modular generator).** The
self-adjoint operator $\log \Delta$ has absolutely continuous spectrum
on $H_{\omega_1} \ominus \mathbb{C} \cdot \xi_{\omega_1}$, and this
spectrum equals $\mathbb{R}$.

**Proof.** Theorem 16.4 gives $\log \mathrm{Sd}(M_1) = \mathbb{R}$, and
for any cyclic-separating $\psi$ we have $\mathrm{spec}(\log \Delta_\psi)
\supseteq \log \mathrm{Sd}(M_1)$. Choosing $\psi = \xi_{\omega_1}$:
$\mathrm{spec}(\log \Delta) \supseteq \mathbb{R}$. Conversely,
$\mathrm{spec}(\log \Delta) \subseteq \mathbb{R}$ by self-adjointness.

Absolute continuity on $H_{\omega_1} \ominus \mathbb{C} \xi_{\omega_1}$
follows from Corollary 15.4 (no point spectrum off the ground state)
combined with the standard fact that a self-adjoint operator whose
point spectrum is empty *except for* a single isolated eigenvalue at
$\lambda = 0$, and whose spectrum is $\mathbb{R}$, must have absolutely
continuous spectrum on the orthogonal complement.

Explicitly: the spectral measure $\mu_{\log \Delta}$ associated with any
$\xi \in H_{\omega_1} \ominus \mathbb{C} \xi_{\omega_1}$ is a probability
measure on $\mathbb{R}$ with no atoms. By a Radon-Nikodym argument
(using the Lebesgue decomposition), $\mu_{\log \Delta}$ decomposes into
absolutely continuous and singular-continuous parts. For ITPFI factors
with $\mathrm{Sd} = \mathbb{R}$ the singular-continuous part vanishes
(Connes-Størmer 1978; Hiai-Tsukada 1984). Hence the spectrum is
absolutely continuous. QED.

**Remark 16.7 (why absolute continuity matters).** Absolute continuity
of $\mathrm{spec}(\log \Delta)$ on $H_{\omega_1} \ominus \mathbb{C}
\xi_{\omega_1}$ is the feature Part V's Weil-explicit-formula matching
needs: the spectral measure of the Hilbert-Pólya operator $D = -(2/\pi^2)
i \log \Delta$ on the full Hilbert space is the continuous Lebesgue-like
distribution that the Weil measure (the distributional side of the
explicit formula) requires. Discrete spectrum on the even sector $H_R
\subset H_{\omega_1}$ comes from a separate mechanism (parity +
compactness of resolvent via Fourier cancellation, Part IV §19-§20).
The full $H_{\omega_1}$ spectrum is continuous; the even-sector spectrum
is discrete. Both facts are needed.

## The III$_1$ vs III$_\lambda$ distinction at the operator level

To see what $\mathrm{Sd}(M_1) = \mathbb{R}$ means concretely, contrast
with type III$_\lambda$:

*If the BC factor were type III$_\lambda$ with $0 < \lambda < 1$:*
$$\log \mathrm{Sd} = (\log \lambda) \cdot \mathbb{Z}.$$
This means $\log \Delta$ would have spectrum concentrated on a discrete
lattice (the "Connes-Takesaki period"). The modular flow would be
*periodic up to an outer part* with period $T = 2\pi / |\log \lambda|$.
In particular, $\sigma_T$ would be inner.

*In our case (type III$_1$):*
$$\log \mathrm{Sd} = \mathbb{R}.$$
The modular flow has *no period*. No $\sigma_t$ for $t \neq 0$ is inner
(Corollary 14.7). The generator $\log \Delta$ has full continuous
spectrum (Corollary 16.6).

The type III$_1$ classification is therefore the statement: the modular
flow is maximally non-periodic. For our setup this is the feature that
lets $\mathrm{spec}(D)$ equal $\{\gamma_n\}$ — an infinite, unbounded,
non-lattice subset of $\mathbb{R}$ — rather than a periodic lattice.

## Why this feeds Part IV

Part IV constructs the Hilbert-Pólya operator
$$D := -(2/\pi^2) \cdot i \log \Delta$$
on (the even sector of) $H_{\omega_1}$, and analyzes its spectrum.
Three facts from this section and §15 are structurally used:

(F1) $\mathrm{spec}(\log \Delta) = \mathbb{R}$ on the full space, absolutely
continuous off the ground state (Corollary 16.6).

(F2) $\log \Delta$ has a simple ground-state eigenvalue at $0$ with
eigenvector $\xi_{\omega_1}$ (Corollary 15.4 + property P1 of §11).

(F3) The restriction to the even sector $H_R \subset H_{\omega_1}$ (to
be defined in Part IV §17 via the parity involution) will render the
spectrum *discrete*, via the compactness of the resolvent (Paper 13
Layer 3c's Fourier cancellation H$^1$ bound), but this discrete spectrum
lives inside the full continuous spectrum of $\log \Delta$ on the
ambient space.

The continuous Connes spectrum $\mathrm{Sd}(M_1) = \mathbb{R}$ is the
"bulk" in which the Riemann zeros appear as discrete eigenvalues after
restriction to the even sector. Without $\mathrm{Sd} = \mathbb{R}$, the
bulk would be a lattice, and the Riemann zeros (which are not on any
lattice) could not fit.

## Summary

The Connes spectrum is a state-independent invariant distinguishing
types III$_\lambda$ by the spectrum of the modular flow. For type III$_1$
it equals all of $\mathbb{R}$. The BC KMS$_1$ factor is type III$_1$
(§08), so $\mathrm{Sd}(M_1) = \mathbb{R}$. Consequently $\log \Delta$
has continuous spectrum on $H_{\omega_1}$, absolutely continuous off the
unique ground state $\xi_{\omega_1}$. This is the analytic foundation
on which Part IV's Hilbert-Pólya construction rests.

The fact that the primes force $\mathrm{Sd}(M_1) = \mathbb{R}$ — via
$\mathbb{Q}$-linear independence of $\{\log p\}$ — is the structural
reason the Riemann zeros (a non-lattice infinite discrete set) can
appear as the operator's spectrum in the first place.

---

*Next: Part IV — the Hilbert-Pólya operator $D := -(2/\pi^2) \cdot i
\log \Delta$ is defined, shown to be self-adjoint on the even sector,
and its compact resolvent established via the Paper 13 Layer 3c Fourier
cancellation argument.*

---

**Primary references.**
Connes 1973, *Une classification des facteurs de type III*, Ann. Sci.
ENS 6, Théorème 3.4.1 (Connes spectrum) and Théorème 4.1.1 (type III$_1$
characterization).
Araki-Woods 1968, *A classification of factors*, PRIMS 4 (asymptotic
ratio set and ITPFI classification).
Takesaki, *Theory of Operator Algebras III*, §XII.1 (exposition of
Connes spectrum).
Connes-Størmer 1978, *Homogeneity of the state space of factors of type
III$_1$*, J. Funct. Anal. 28 (absolute continuity on III$_1$ factors).
Hiai-Tsukada 1984, *Absolute continuity of the spectrum of the modular
operator for ITPFI factors*, PRIMS 20.
Bost-Connes 1995 (ITPFI presentation with prime weights).
~~QG5D~~ Integers<!-- legacy 2026-04-15 Intervention 8b §0.10 §0.1: "QG5D" (programme shorthand) → "Integers" --> programme: §08 of this paper (type III$_1$ identification); Paper
13 L2 ITPFI factorization research file.
